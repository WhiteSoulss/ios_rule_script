# AllInOne：Pinterest 小范围修改

原作者为 blackmatrix7，沿用仓库 GPL-2.0 许可证。
2026-10-11 基于上游提交 83f37120c155f67c8eef43221dabe15cc3c95fec 修改。

## 安装

在 Surge 停用原版 AllInOne，使用本仓库的模块：

https://raw.githubusercontent.com/WhiteSoulss/ios_rule_script/master/rewrite/Surge/AllInOne/AllInOne.sgmodule

Pinterest 去广告继续使用现有独立原生 JQ 模块，或已包含它的 wool_scripts 总模块。

## 改动范围

当前仅修改 [URL Rewrite] 的两条关键词 Reject：

- (?i)\badvertisement
- (?i)\badvertising

这两条规则排除 HTTP(S) 的 pinterest.com、pinimg.com 及其子域名。
大小写、可选端口和域名末尾点均已考虑；以 URL 主机为界，
不会因其他网站的参数中出现 Pinterest 而放行。

原版对整个 URL 搜索关键词。合成样例中的 Pinterest 请求携带
advertising_id 或 field_set=advertisement，会命中原版规则。

先前 10 条规则均排除 Pinterest 的版本由用户确认有效：
https://raw.githubusercontent.com/WhiteSoulss/ios_rule_script/df4eae07033c138b4c37e61db55c7385ac518e64/rewrite/Surge/AllInOne/AllInOne.sgmodule

用户随后要求缩小范围并取消拆分。本次将另外 8 条规则恢复为上游原样，
保留上述两条关键词排除。它们是目前能够演示风险的两个关键词，
但没有实际失败 URL，不能据此认定其余 8 条排除一定多余；
用户随后已确认缩小后的版本成功。没有发布拆分诊断模块。

其余运行时重写、分流、24 条脚本、MITM 和 HTTP engine 配置保持上游字节。
模块名称、描述和仓库地址提供个人修改标识；作者、许可证保留。
这里只修改 AllInOne.sgmodule，AllInOne_Mock.sgmodule 保留原版。

## 验证与维护

pinterest-review.json 记录原版、当前版本及用户确认有效版本的哈希、
两条差异、8 条还原记录和设备复测状态。

verify-pinterest.py 使用 VPS 的 Linux ICU 编译全部正则，
检查 Pinterest 仅两条关键词变化、其他规则仍匹配上游、其他域名行为、
捕获组和原版应用样例。执行：

python3 verify-pinterest.py --upstream /path/to/original/AllInOne.sgmodule

用户已报告缩小版本连接正常；服务器未操作设备，也未验证全部应用去广告效果。
同步上游后需阅读实际变化，重新复核这两条规则；不能直接覆盖个人修改。

## 每日同步

已授权每天北京时间 08:00 同步整个上游仓库，保留这两条 Pinterest 排除和所有个人修改。
沿用现有 surge-github 任务，复核、验证后发布。具体流程见 [UPSTREAM-SYNC.md](UPSTREAM-SYNC.md)。
