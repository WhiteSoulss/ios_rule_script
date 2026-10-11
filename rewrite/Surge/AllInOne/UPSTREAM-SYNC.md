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
ad.quietvales.com 保持停用，共享 nginx router 字节不变。

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
83f37120c155f67c8eef43221dabe15cc3c95fec
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
   不操作用户设备，不自动启用 fork 的 GitHub Actions，不恢复旧网站。

当新的上游 AllInOne 仍含这两条旧关键词时，排除规则必须保留。
用户已授权正常、验证通过后的日常同步和发布，无需每次再询问。
只有有意义更新、失败或确实需要用户处理时报告；无变化保持安静。
