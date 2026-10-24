# 每日上游同步与个人改动保留

用户在 2026-10-11 授权定时同步，并明确保留已成功的 Pinterest 排除改动。
本仓库独立于 WhiteSoulss/wool_scripts，不把 AllInOne 合入其总模块。

## 范围与日程

上游：blackmatrix7/ios_rule_script 的 master 分支。
目标：WhiteSoulss/ios_rule_script 的 master 分支。
同步整个上游仓库，同时保留本 fork 的所有个人文件及用户修改。

沿用本聊天现有 heartbeat：surge-github，每天北京时间 08:00。
保持原有 wool_scripts 的 fmz/可莉维护，不另建重复任务，不迁移云端。
当前 America/Los_Angeles 调度为前一天 17:00；
每次运行按时区计算下一次北京时间 08:00，跨夏令时调整同一个任务。

所有下载、合并、构建和验证仅在 107.174.244.24 服务器执行。
root SSH 密钥：/Users/samcheng/.ssh/codex_vps_107_uptime_kuma。
当前服务器工作目录：/root/allinone-fork-20261011。
本机只编辑、SSH 和读取任务记录；不操作本机代理客户端或浏览器。
ad.quietvales.com 已按用户最新要求恢复，独立在 107 维护；此 fork 同步不部署网站。
云端迁移仍暂停，共享 nginx router 字节不变。

## 已确认的个人行为

AllInOne.sgmodule 相比已复核上游，仅两条运行时匹配有个人改动：

- (?i)\badvertisement
- (?i)\badvertising

这两条全 URL 关键词 Reject 跳过 HTTP(S) 的 pinterest.com、pinimg.com
及其子域名，包含大小写、可选端口和主机末尾点处理。
以 URL 主机为界，其他网站仅在参数中引用 Pinterest 不会因此放行。

原来的另外 8 条排除已经恢复上游匹配。用户确认缩小后的版本成功，
无需拆分模块。保留现有独立 Pinterest 原生 JQ 模块及其 MITM；
AllInOne 的域名排除不应被扩展成全配置的 MITM 禁用。

当前已复核上游提交：
00d82f6c6c374abb947fabc9c1b69f2a22e71dbc
上游 AllInOne SHA256：
66a8282facc2c339363bdf924b0a65eeaf11b57acf4b5839538044303a2d388d
用户确认的两条规则版本提交：
d11dc3fb24f0d9604ff0a9508080fd8d42d67933
其 AllInOne SHA256：
43bdfbba457be8a9eb8fab3ff62d018505b296a5e2351c31841fa3ad5038a77a

这是用户报告的连接正常，不代表服务器实际测试了设备或全部去广告效果。
没有收到原始失败 URL，尚不能确定两条规则中具体哪一条命中过真实请求。

## 每次运行

1. 读取本仓库 AGENTS.md、本文件、当前 pinterest-review.json 和
   PINTEREST-COMPATIBILITY.md。获取并固定两边最新 master 头及 Git tree。
   使用已复核上游提交/merge-base 作独立基线，检查真实提交和文件差异。
2. 合并整个上游仓库。使用三方合并或等价的已复核 Git tree，保留个人
   AGENTS.md、本同步说明、验证器、审核记录、AllInOne 修改以及其他用户更改。
   处理上游的新增、变更和删除；不 reset 覆盖个人分支，不 force push。
3. 逐项阅读 AllInOne 及相关原生规则、脚本和依赖的实际变化。
   手工保留或重新适配这两条域名排除。若上游关键词规则、语法或语义变化，
   必须复核后调整，不能机械替换或仅改哈希。若上游删除某规则，不凭旧模板
   重新引入它；记录该排除已不再需要并复核剩余行为。
   其他上游文件按原版同步，保留作者、许可证及个人修改说明。
4. 在 VPS 运行 verify-pinterest.py，输入固定上游原版 AllInOne。
   核对两条关键词对 Pinterest 的排除、其他域名行为、其余规则原版一致、
   捕获组、ICU 编译、模块元数据、MITM/端口及相关资源。
   源规则数量改变时，先阅读差异再更新验证器的真实基线和样例；
   不把更新统计或哈希当作审核。脚本只作语法检查，不执行下载的上游代码。
5. 更新 pinterest-review.json 的原版提交、原版/个人文件精确哈希及行为记录。
   保留用户确认的历史与当前变化的区别。下载失败、验证失败、冲突或未知动作
   时，保持已审核版本，并在服务器记录 pending-review；不要发布未审核稿。
6. 用 GitHub 连接器发布单个原子提交，以最新个人分支头作 expected_sha。
   有实际上游更新时，提交父项包含当前个人头和已复核上游头，保留合并历史；
   必要的个人修正和审核记录一起提交。重读头以防并发更改；不强制更新。
   发布后核对 raw 文件和资源的公开内容/哈希。无变化不创建空提交。
   不操作用户设备，不自动启用 fork 的 GitHub Actions，不修改独立网站部署。

当新的上游 AllInOne 仍含这两条旧关键词时，排除规则必须保留。
用户已授权正常、验证通过后的日常同步和发布，无需每次再询问。
只有有意义更新、失败或确实需要用户处理时报告；无变化保持安静。


## 2026-10-12 已复核同步

上游新增一次提交，仅更新 rule/ 下 246 个规则集、时间戳和说明文件。
已归档并核对全部实际新字节及 Git blob SHA；三方对照无冲突，全部个人文件保留。
AllInOne 原版、个人模块、脚本目录、作者、许可证和工作流均未变化；两条 Pinterest
排除保持原样。该模块通过既有 ICU 范围/等价样例，两个脚本资源已归档并仅作语法编译。
上游数据按其原格式同步，没有把规则集项目当作新 App 或混入 wool_scripts。
具体文件记录、实际数据差异及资源哈希见 upstream-sync-review-20261012.json。
后续读取 pinterest-review.json 的 latest_upstream_sync 指向最新完整复核记录；
原版/依赖有真实变化必须阅读全文和差异，不能用 hash/计数替代批准。


## 2026-10-13（America/Los_Angeles）已复核同步

已固定上游 d8363caa2c1e47fb735615316032bed3f475ee57，新增一次提交，仅修改 rule/
目录的 278 个数据、计数和时间戳文件。逐文件归档新旧实际字节并核对 Git blob；
完整三方树无冲突，全部个人文件与旧审核记录保留。
实际 Surge 差异包括广告域名更新、China 系列域名/CIDR 调整、Global 增加
91short.com；DOMAIN-SET 的前导点按后缀匹配单独核对，不把纯域名误作规则类型。
4,114 条变更域名/关键词行及 160 条 CIDR 行（含 no-resolve 格式变体）通过结构检查，
59 个 YAML payload 完整解析。README 仅时间戳与数量变化。
AdGuard AdvertisingLite/Privacy 只更新时间；Surge AdvertisingLite 的规则文件未变。

AllInOne 原版、个人模块和两个实际脚本资源均未变，保留已经确认的两条 Pinterest
关键词排除；既有 ICU 范围/等价检查通过。没有扩展排除、修改脚本或拆分诊断模块。
详见 upstream-sync-review-20261014.json。旧模块/依赖哈希复用建立在实际字节一致上，
不把新提交编号或计数当作转换审核。服务器检查仍不等于客户端广告效果验证。


## 2026-10-15（America/Los_Angeles）已复核同步

固定上游 933875d42861a7fdfd9f945cd18605d74fa7e943，新增一次提交，仅修改 rule/ 下
265 个数据、计数和时间戳文件。全部 530 份新旧字节已归档并核对 Git blob，完整三方
对照无冲突，保留所有个人文件与历史复核记录。

实际变化包括 Advertising 增加 730/移除 39 条域名，AdvertisingTest 增加 998/移除
22 条；China 系列域名及 IPv4/IPv6 网段调整；TikTok 增加 capcutapi.com、
capcutapi.us、capcutstatic.com。9,366 条变更域名/关键词行与 538 条 CIDR 行
（包含各格式变体）通过检查；6 份 DOMAIN-SET 与完整规则的变更语义对应，56 个
YAML payload 完整解析。47 份 README 仅时间戳和数量变化。AdGuard Lite/Privacy
活动规则及 Surge AdvertisingLite 不变。

AllInOne、脚本目录、许可证和工作流均未变化；两个实际运行脚本的可变 URL 与固定
版本字节一致。保留用户确认的两条 Pinterest 排除与全部其他原版动作，既有 ICU
范围及其他域名等价检查通过，脚本仅编译未执行。详见 upstream-sync-review-20261016.json。
没有转换新的 Loon 项目，没有操作客户端、启用工作流、恢复网站或迁移云端。
服务器检查不代表客户端广告效果验证。


## 2026-10-17（America/Los_Angeles）已复核同步

固定上游 7dd06b44f5093dd5404e1e5f3bca5452d97146ef，新增一次提交，仅修改 rule/ 下
297 个数据、计数和时间戳文件。594 份新旧实际字节已归档并核对 Git blob，完整三方
对照无冲突，保留全部个人文件及历史复核记录。

Advertising 增加 1,017/移除 8 条后缀，AdvertisingTest 增加 715/移除 7 条。
China 系列调整域名和 IPv4/IPv6 段，保留 download.microsoft.com 的精确主机规则；
Global 增加六个域名，Proxy 增加 7x24hrs.com、meta.ai、metaaivm.com。
6,624 条变更域名/关键词行及 2,364 条 CIDR 行（含各格式变体）通过结构检查；
八份 DOMAIN-SET 与完整规则的差异对应，64 个 YAML payload 完整解析。
52 份 README 仅时间戳与数量变化。AdGuard Lite/Privacy 活动规则及 Surge
AdvertisingLite 不变。

AllInOne、脚本目录、作者/许可证和工作流均未变。两个实际运行脚本的可变 URL
与固定版本字节一致；脚本仅编译未执行。保留用户确认的两条 Pinterest 排除，既有
ICU 范围/其他主机等价检查通过。详见 upstream-sync-review-20261018.json。
没有转换新 Loon 项目、操作客户端、启用工作流、恢复网站或迁移云端；服务器检查
不代表客户端去广告验证。


## 2026-10-19（America/Los_Angeles）已复核同步

固定上游 f9e403a75bbc4bee939c6d8dd766cf78f1b512f3，新增一次提交，仅修改 rule/ 下
226 个数据、计数和时间戳文件。452 份新旧实际字节已归档并核对 Git blob；完整三方
对照无冲突，保留全部个人文件及历史复核记录。

Advertising 新增 689 条后缀；AdvertisingTest 新增 3,168/移除 196 条域名。
ChinaIPs 拆分 211.99.8.0/21，ChinaIPsTest 同时调整 110.40/110.42 及 IPv6 段。
Global 新增 18/移除 2 条后缀；Lan 新增 localhost.weixin.qq.com 与
localhost.work.weixin.qq.com 两条精确主机规则。12,223 条变更域名/关键词行及
68 条 CIDR 行（含各格式变体）通过结构检查；三份 DOMAIN-SET 差异对应完整规则，
47 个 YAML payload 完整解析。32 份 README 仅时间戳与数量变化。
Apple、Blizzard、Game、ChinaMax、AdGuard Lite/Privacy 活动规则及 Surge
AdvertisingLite 均不变。

AllInOne、脚本目录、作者/许可证和工作流均未变。两个运行脚本的可变 URL
与固定版本字节一致；脚本仅编译未执行。保留用户确认的两条 Pinterest 排除，既有
ICU 范围与其他主机等价检查通过。详见 upstream-sync-review-20261020.json。
没有转换新 Loon 项目、操作客户端、启用工作流、恢复网站或迁移云端；服务器检查
不代表客户端去广告验证。


## 2026-10-23（America/Los_Angeles）已复核同步

固定上游 00d82f6c6c374abb947fabc9c1b69f2a22e71dbc，更新 rule/ 内 292 个文件，
包含三份新的 Steam_Resolve.list，未删除源文件。581 份实际新旧版本已归档并核对
Git blob，完整三方比较无冲突，保留全部个人文件、历史审核和合并父提交。
Advertising 新增 5,393/移除 910 条域名，AdvertisingTest 新增 2,951/移除 727 条。
ChinaIPs/ChinaIPsTest 与 ChinaMax 系列域名和 IPv4/IPv6 数据调整；Global 新增
51 条后缀。Steam/Game 各新增三个后缀和十二个 IPv4 段。三份 Steam_Resolve
完整 69 行与原 Steam 列表仅 no-resolve 参数不同；八条 README 新说明已单独核对。
30,186 条域名/关键词变体和 708 条 CIDR 变体通过校验，61 个 YAML payload 解析，
七份 DOMAIN-SET 差异与完整规则对应。AdGuard Lite/Privacy 活动数据、Surge
AdvertisingLite、AllInOne 原版/个人版本和两个运行脚本均未变。保留两条已经用户
确认的 Pinterest 排除，既有 ICU 与脚本语法检查通过；服务器检查不等于设备实测。
详见 upstream-sync-review-20261024.json。可莉网站与 wool_scripts 分别复核且无变化，
保留滴滴独立客户端状态，不操作设备、不启用工作流、不迁移云端。
