# AllInOne：Pinterest 兼容修改

此文件独立使用，原作者为 blackmatrix7，沿用仓库 GPL-2.0 许可证。
2026-10-11 基于上游提交 83f37120c155f67c8eef43221dabe15cc3c95fec 修改。

## 安装

在 Surge 停用原版 AllInOne，改用本仓库的 AllInOne.sgmodule：

https://raw.githubusercontent.com/WhiteSoulss/ios_rule_script/master/rewrite/Surge/AllInOne/AllInOne.sgmodule

Pinterest 去广告仍使用现有独立原生 JQ 模块，或已包含它的 wool_scripts 总模块。

## 改动

10 条不限定应用域名的通用 URL Reject 规则排除 HTTP(S) 的
pinterest.com、pinimg.com 及其子域名。包含大小写、可选端口和域名末尾点；
匹配范围以 URL 的域名为界，不因其他网站的查询参数提到 Pinterest 而放行。

原版的 advertisement / advertising 规则匹配整个 URL。
例如 Pinterest 首页 URL 携带 advertising_id 时，原版会拒绝该请求。
这说明规则存在误拦风险；目前没有实际失败请求的完整 URL，未确认设备故障原因。

所有其余重写、分流、24 条脚本、MITM 和 HTTP engine 设置保持原版。
本修改没有引入运行时 JS，没有修改 wool_scripts，也没有加入 Pinterest JQ。

## 验证和后续维护

pinterest-review.json 记录精确原版/修改哈希和逐条规则差异。
verify-pinterest.py 在 Linux 的 ICU 正则引擎上检查原版匹配风险、
Pinterest 排除、其他域名行为、原版应用样例、捕获组和所有模块正则编译。
验证命令：

python3 verify-pinterest.py --upstream /path/to/original/AllInOne.sgmodule

服务器验证通过不等于 Surge 设备端连接及去广告验证。
这里只修改 AllInOne.sgmodule，AllInOne_Mock.sgmodule 保留原版。
同步上游后需阅读新差异、重新复核这 10 条排除规则并验证，
不能用自动生成的原版文件直接覆盖个人修改。
