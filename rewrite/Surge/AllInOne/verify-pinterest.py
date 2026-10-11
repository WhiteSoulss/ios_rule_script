#!/usr/bin/env python3
# WhiteSoulss, 2026-10-11. GPL-2.0; see repository LICENSE.
"""Check the Pinterest exclusion using Linux ICU; does not operate Surge."""
import argparse
import ctypes as C
import ctypes.util
import hashlib
import itertools
import json
from pathlib import Path
import re

parser = argparse.ArgumentParser()
parser.add_argument("--upstream", required=True, type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parent
review = json.loads((root / "pinterest-review.json").read_text())
old_bytes = args.upstream.read_bytes()
new_bytes = (root / "AllInOne.sgmodule").read_bytes()
assert hashlib.sha256(old_bytes).hexdigest() == review["upstream_sha256"]
assert hashlib.sha256(new_bytes).hexdigest() == review["module_sha256"]

library_name = ctypes.util.find_library("icui18n")
if not library_name:
    raise RuntimeError("Linux ICU library is required; run this check on the VPS")
lib = C.CDLL(library_name)
suffix = re.search(r"\.so\.(\d+)", library_name)
suffix = "_" + suffix.group(1) if suffix else ""
def bind(name, arguments, result):
    fn = getattr(lib, name + suffix)
    fn.argtypes, fn.restype = arguments, result
    return fn
U16 = C.c_uint16
I32 = C.c_int32
PTR = C.c_void_p
open_regex = bind("uregex_open", [C.POINTER(U16), I32, C.c_uint32, PTR, C.POINTER(I32)], PTR)
set_text = bind("uregex_setText", [PTR, C.POINTER(U16), I32, C.POINTER(I32)], None)
find = bind("uregex_find", [PTR, I32, C.POINTER(I32)], C.c_int8)
close = bind("uregex_close", [PTR], None)
group_count = bind("uregex_groupCount", [PTR, C.POINTER(I32)], I32)
def utf16(text):
    data = text.encode("utf-16-le")
    return (U16 * (len(data) // 2)).from_buffer_copy(data), len(data) // 2
class Regex:
    def __init__(self, expression):
        self.expression = expression
        self.pattern, length = utf16(expression)
        status = I32()
        self.handle = open_regex(self.pattern, length, 0, None, C.byref(status))
        if status.value > 0 or not self.handle:
            raise AssertionError(("ICU compilation failed", status.value, expression))
        status = I32()
        self.groups = group_count(self.handle, C.byref(status))
        assert status.value <= 0
    def search(self, text):
        self.text, length = utf16(text)
        status = I32()
        set_text(self.handle, self.text, length, C.byref(status))
        assert status.value <= 0, (status.value, self.expression)
        status = I32()
        result = bool(find(self.handle, 0, C.byref(status)))
        assert status.value <= 0, (status.value, self.expression)
        return result
    def release(self):
        if self.handle:
            close(self.handle)
            self.handle = None

def sections(text):
    result, section = {}, None
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1]
            result[section] = []
        else:
            assert section is not None, line
            result[section].append(line)
    return result
def rewrites(rows):
    result = []
    for line in rows:
        match = re.fullmatch(r'"((?:[^"\\]|\\.)*)" (.+)', line)
        assert match, line
        result.append((match.group(1), match.group(2)))
    return result

old_sections = sections(old_bytes.decode())
new_sections = sections(new_bytes.decode())
assert old_sections.keys() == new_sections.keys()
for section in old_sections:
    if section != "URL Rewrite":
        assert old_sections[section] == new_sections[section], section
old_rows = rewrites(old_sections["URL Rewrite"])
new_rows = rewrites(new_sections["URL Rewrite"])
assert len(old_rows) == len(new_rows) == 807
actual = [(old, new) for old, new in zip(old_rows, new_rows) if old != new]
expected = [((c["before"], "- reject"), (c["after"], "- reject")) for c in review["changes"]]
assert actual == expected
assert len(actual) == 2
assert "#!author=blackmatrix7\n" in new_bytes.decode()
assert "#!name=AllInOne · Pinterest兼容\n" in new_bytes.decode()
assert len(new_sections["Script"]) == 24

old_regexes = [Regex(pattern) for pattern, _ in old_rows]
new_regexes = [Regex(pattern) for pattern, _ in new_rows]
for old, new in zip(old_regexes, new_regexes):
    assert old.groups == new.groups, (old.expression, new.expression)
extra = []
for row in new_sections["Rule"]:
    if row.startswith("URL-REGEX,"):
        extra.append(Regex(row[len("URL-REGEX,"):].rsplit(",", 1)[0]))
for row in new_sections["Script"]:
    match = re.search(r"\bpattern=(.*?)(?:,\s*[a-z][\w-]*=|$)", row)
    assert match, row
    extra.append(Regex(match.group(1).strip('"')))

suffixes = [
    "/outadservice/", "/ting/preload/", "/ad/", "/api/v3/adRealTime",
    "/brand/search/v1.json", "/promotion/display_cache",
    "/promotion/display_ad", "/promotion/feed_display", "/promotion/search_ad",
    "/splash/getSplashV1.action", "/x/v1/version", "/x/v1/notice?",
    "/x/v1/top_notice?", "/x/v1/advert?position=3", "/x/v1/advert?position=2",
    "/?x=advertisement", "/?advertising_id=example", "/?x=splash_screen",
    "/v3/feeds/home/?page_size=25", "/v3/feeds/home/?advertising_id=example",
    "/v3/pins/123/related/modules/?field_set=advertisement",
    "/v3/feeds/home/?nested=https://example.org/ad/",
    "/?x=notadvertising", "/?x=ADVERTISING", "/?x=advertisement&next=advertising",
    "/?next=https://api.pinterest.com/ad/", "/?x=%61dvertising",
]
protected_hosts = [
    "pinterest.com", "api.pinterest.com", "www.pinterest.com",
    "a.b.pinterest.com", "pinimg.com", "i.pinimg.com",
    "API.PINTEREST.COM", "Api.Pinterest.Com:443", "api.pinterest.com.",
    "api.pinterest.com.:443", "i.pinimg.com:8443",
]
protected_urls = [
    scheme + host + path
    for scheme, host, path in itertools.product(
        ("https://", "http://", "HTTPS://"), protected_hosts, suffixes)
]
changed_indexes = {i for i, (old, new) in enumerate(zip(old_rows, new_rows)) if old != new}
assert {old_rows[i][0] for i in changed_indexes} == {
    r"(?i)\badvertisement", r"(?i)\badvertising"}
for url in protected_urls:
    before = {i for i, rx in enumerate(old_regexes) if rx.search(url)}
    after = {i for i, rx in enumerate(new_regexes) if rx.search(url)}
    assert after == before - changed_indexes, (
        "Only the two keyword rejects may change on Pinterest", url, before, after)
    assert not any(rx.search(url) for rx in extra), ("Rule/script intercept", url)

controls = [
    "example.org", "api.example.org", "pinterest.com.evil.invalid",
    "pinimg.com.evil.invalid", "notpinterest.com", "notpinimg.com",
    "evil-pinterest.com", "pinterest.com@evil.invalid",
    "api.pinterest.com:443.evil.invalid", "advertisement.example.org",
    "example.org:443", "192.0.2.1", "API.EXAMPLE.ORG",
]
control_urls = [
    scheme + host + path
    for scheme, host, path in itertools.product(
        ("https://", "http://", "HTTPS://", "wss://"), controls, suffixes)
]
for url in control_urls:
    before = [i for i, rx in enumerate(old_regexes) if rx.search(url)]
    after = [i for i, rx in enumerate(new_regexes) if rx.search(url)]
    assert before == after, ("Other-host behavior changed", url, before, after)

risk_urls = [
    "https://api.pinterest.com/v3/feeds/home/?advertising_id=example",
    "https://api.pinterest.com/v3/pins/123/related/modules/?field_set=advertisement",
]
for url in risk_urls:
    assert any(rx.search(url) for rx in old_regexes), ("Missing original risk", url)
    assert not any(rx.search(url) for rx in new_regexes), url
clean_url = "https://api.pinterest.com/v3/feeds/home/?page_size=25"
assert not any(rx.search(clean_url) for rx in old_regexes)

app_samples = {
    "Inoreader": "https://www.inoreader.com/adv/banner",
    "iCleaner": "https://ib-soft.net/icleaner/txt/ad_priority.txt",
    "VUE": "https://api.vuevideo.net/api/v1/ad/",
    "MixC": "https://app.mixcapp.com/mixc/api/v1/ad",
    "WaitWaitPay": "https://api.waitwaitpay.com//api/splash",
    "Yizhibo": "https://api.yizhibo.com/common/api/pz",
    "YueMeTV": "https://zjh5api.189smarthome.com:8091/xygj-config-api/queryData",
    "Bodivis": "https://www.bodivis.com.cn/app/splashAdvertise",
    "QiuDuoDuo": "https://api.qiuduoduo.cn/guideimage",
    "Haidilao": "https://superapp.kiwa-tech.com/app/ads/selectList",
    "YingShiGongChang": "https://app.yinlun.cc/xgapp.php/v1/top_notice?",
}
for app, url in app_samples.items():
    before = [i for i, rx in enumerate(old_regexes) if rx.search(url)]
    after = [i for i, rx in enumerate(new_regexes) if rx.search(url)]
    assert before and before == after, (app, url, before, after)

result = {
    "status": "passed",
    "regex_engine": library_name,
    "changed_generic_rejects": len(actual),
    "compiled_original_url_rewrites": len(old_regexes),
    "compiled_modified_module_regex_entries": len(new_regexes) + len(extra),
    "pinterest_two_rule_scope_cases": len(protected_urls),
    "remaining_pinterest_rejects_match_upstream": True,
    "non_pinterest_equivalence_cases": len(control_urls),
    "original_false_reject_samples": len(risk_urls),
    "retained_other_app_examples": len(app_samples),
    "script_rows_preserved": len(new_sections["Script"]),
    "all_other_sections_identical": True,
    "capture_group_counts_preserved": True,
    "client_effectiveness_verified": False,
}
for rx in old_regexes + new_regexes + extra:
    rx.release()
print(json.dumps(result, ensure_ascii=False))
