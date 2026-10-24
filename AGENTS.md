# Personal fork maintenance

The user authorized daily synchronization of blackmatrix7/ios_rule_script/master
to WhiteSoulss/ios_rule_script/master on 2026-10-11. Keep this fork separate from
WhiteSoulss/wool_scripts; retain that repository's existing fmz/Kelee maintenance.

Read rewrite/Surge/AllInOne/UPSTREAM-SYNC.md and the current pinterest-review.json.
The user confirmed the two-keyword Pinterest exclusion works and requested it
be preserved. Only advertisement and advertising keyword rejects have personal
matching exclusions. Keep pinterest.com, pinimg.com and their subdomains excluded
from those two rules. The other eight previously modified rules are restored.
Do not publish split diagnostic modules or broaden these exclusions silently.

Downloads, builds, merging and checks run only on VPS 107.174.244.24. Use the
authorized root SSH connection; the Mac is for editing, SSH and task records.
Do not operate the user's Surge/Loon/Stash devices or local browser.
The user restored ad.quietvales.com on 2026-10-22; maintain that website separately
on 107 under /opt/kelee-surge-hub/MANUAL_UPDATES.md, with independent Surge/Stash
and fmz source scopes. Cloud migration remains paused. This fork sync does not
deploy the website. Keep /etc/nginx/stream-conf.d/silvervales-router.conf unchanged.

Pin both branch heads, retain an immutable upstream baseline, review real diffs,
and merge upstream changes while preserving all personal files and user changes.
Do not reset the fork to upstream, use force pushes, overwrite the personalized
AllInOne with an unreviewed generated file, or enable upstream GitHub workflows.
Do not use ScriptHub, a generic Loon converter, automatic approval, or hash-only
acceptance for personal adaptations. Preserve upstream authors and licenses.

Review changed AllInOne configuration and relevant dependencies by semantics.
Run relevant ICU URL-matching regression checks, script syntax without executing
upstream scripts, metadata/host/port/resource checks, then update exact provenance.
The old verifier's pinned counts and hashes must track actually inspected source;
a verifier pass does not itself approve upstream changes. Preserve the two-rule
scope and behavior on other hosts. Server checks are not client effectiveness tests.

Publish reviewed changes through the authorized GitHub connector with a fresh
expected-head lease. Retain merge ancestry where applicable (current fork head
and reviewed upstream commit as parents). Verify raw public bytes after publication.
On unresolved conflicts, unknown behavior, download or validation failure, keep
the last reviewed affected version and record pending-review. No empty commits.
