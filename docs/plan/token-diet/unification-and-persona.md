# 工具统一化 + 角色扮演文风方案（2026-08-21 只读探讨稿）

用户提出的六个议题的完整方案。均未动工，等逐项拍板。

## 1. 移除 claude_code 工具

- 删注册（src/tools/claude_code/ 整模块）+ descriptions/claude_code.json + 宏行 + SUBAGENT_EXCLUDED 表项。
- **与 claude-code 中转协议无关**（llm/openai_compatible/claude_code/ 是把 Claude Code 当供应商用的那条线，保留）。实施时验证二者无共享代码。
- 收益：normal/stub −1 stub 行（~40 tok），代码 −约 500 行。

## 2. write_file / edit_string / edit_file

已随 schema 裁定落地时整删（write.rs、edit_replace.rs、两份 JSON）。edit_file 更早（只有孤儿 JSON，已删）。此项完成。

## 3. 编辑/读取三套并一套（核心方案）

现状三套：文件系统（apply_patch/read_file/glob/grep/trash_path）、Artifact（create/patch/present/read 四件）、知识库（upload/edit/read/remove/search 五件）。

### 方案 C（推荐）：路径命名空间统一

apply_patch 与 read_file 认三种路径：普通路径=文件系统、`artifact:名字`=Artifact 库、`kb:路径`=知识库。于是：

| 旧工具 | 去向 |
|---|---|
| create_artifact | apply_patch 的 Add File `artifact:report.md` |
| apply_artifact_patch | apply_patch 的 Update File `artifact:…` |
| read_artifact | read_file `artifact:…`（列表模式=read_file `artifact:`） |
| upload_text_to_knowledge_base | apply_patch 的 Add File `kb:…` |
| edit_knowledge_base_file | apply_patch 的 Update File `kb:…`（行区间替换退场，统一 patch 语义） |
| remove_knowledge_base_file | apply_patch 的 Delete File `kb:…` |
| read_knowledge_base_file | read_file `kb:…` |
| present_artifact | **保留**（发布是展示动作不是编辑） |
| search_knowledge_base | **保留**（语义检索不是读取） |
| vision_analyze / print_image | 按用户要求分开不动 |

收尾形态：**apply_patch + read_file + present_artifact + search_knowledge_base** 四个工具覆盖全部编辑/读取，normal 注册表净减 7 个工具。

- 收益：normal/stub 减 4 条 kb stub 行（~160 tok）；WebUI 每请求减 3 个 AL artifact 工具（~450 tok，胜过此前"四合一"方案的 250）；模型心智从三套契约变一套。
- 关键设计点：
  - **权限**：artifact/kb 原是 Presentation/独立权限，并入 apply_patch(Writes) 后按前缀在 handler 内分流；restricted 平台本就不注册 apply_patch，无泄漏面。WebUI artifact 工具本就只在 owner 回合注册，无损失。
  - **kb 索引钩子**：kb: 前缀写入路由到知识库模块原函数（索引/清理逻辑复用，不绕过）。
  - **搜索结果引路**：search_knowledge_base 返回的路径带 `kb:` 前缀，read_file 直接可用，形成闭环。
  - **双兼容**：compact_artifact_tool_report 等消费者按旧工具名的分支保留（历史回放）。
- 分批：第一批 artifact 并入；第二批 kb 并入（涉及索引钩子，单独验收）。

### 方案 B（保守备选）：域内合并

artifact 四合一（action 枚举）、kb CRUD 四合一，文件系统不动。收益约为 C 的六成，无权限/命名空间设计，两天内稳收。若对 C 的命名空间心智有顾虑选 B。

### 改名 Edit / Read

纯改名零 token 收益，但一次到位的话与合并同批做最便宜。风险：全仓引用点（描述/hint/文档/测试/渲染分支）+ 模型对 apply_patch 的既有习惯。建议：**合并做完观察一版，改名单独批**；或干脆不改（apply_patch/read_file 语义已自明）。

## 4. get_avatar 行为矫正

现状：user_id 可选（缺省=群头像），download 默认 false 只回 URL——模型拿到 URL 用不了（QQ 受限会话无 web_fetch 下图能力，URL 又进不了 send_message_to_user 的本地路径校验）。

新行为：**必须传 user_id 或 group_id 二选一；一律下载到平台文件目录；返回本地路径**（+尺寸/格式一行）。模型拿路径即可 vision_analyze（若可用）、send_message_to_user 发图（非管理员的"本回合工具产物"校验天然通过）、生图 reference。download 参数删除。schema：user_id/group_id 互斥二选一，写进描述一句。

## 5. delete_real_chat_history 去两步确认

删 action(request/confirm) 与 confirmation_token：单次调用直接执行，返回删除条数。保留 admin-only 门槛。schema 从 11 参降到 8 参。风险认知：误删防线只剩 admin 身份 + 模型自身判断，用户已知情拍板。

## 6. 文风与角色扮演（讨论稿）

用户论点：书面语标点（`总述：分句；分句；分句`）与非系统式散文进入上下文后被模型模仿 → OOC；网页版裸 chat 一句提示词就够，是因为上下文干净。

### 机制分析（同意，且可细化）

上下文里的一切文本对模型都是"这里该怎么写字"的证据。但污染力分层：

1. **同语言同语域的最毒**。人格输出是中文口语，所以**中文书面语注入（QQ 撤回规则、审核初判、群管规则这类满是分号顿号的中文条款）污染力最强**——它和人格输出同语言同场景，模型分不开语域。
2. **英文工具机械文本次之**。英文描述/schema 对模型是明确的"系统语域"，与中文人格输出天然隔离。**推论：工具描述定稿应译回英文（既定流程），这不止是惯例，本身就是抗 OOC 措施**；中文只该出现在人格侧文本里。
3. **XML 标签是语域栅栏**。`<qq-xxx>` 包裹的内容被模型归为机械信息，裸文本注入（如部分中文提醒）比带标签的更容易被模仿。
4. 工具结果本轮已大幅文本化，JSON 噪音在降——方向一致。

### 方案

- **《提示词文风规范》**（写进 docs，作为后续所有描述/hint 的验收标准）：
  1. 机械文本（描述/schema/注入条款）一律英文短句，一句一个句号，禁分号串联、禁`总述：分述`结构、禁修辞；
  2. 中文只用于人格文本与必须让模型中文复述的内容；
  3. 所有注入必须有 XML 标签外壳，不裸奔；
  4. 每条注入先问"删掉会怎样"再问"怎么写短"。
- **现存中文注入的处理**：撤回规则/群管规则/审核初判等条款改写为英文短句版（语义逐条保真，因为 08-20 刚修过），这比精简字数的收益可能更大——它们直接从"人格语域"退场。
- **实验先行**（[[verify-before-shipping]]）：testkit/persona-ab 已有两套体制方法论。新增一组 A/B：现状 vs 文风规范化（描述+注入改写后），15 轮深度对话测 OOC 率。**08-14 实验结论"位置>>措辞"提示我们别高估措辞收益，先测再全面铺开**。
- 顺带：webui 标题 prompt 的 13 连空格、`sent meme` 等新输出的文风也按规范复核。

## 决策清单

| # | 事项 | 推荐 | 待拍板 |
|---|---|---|---|
| 1 | claude_code 工具移除 | 做 | 已拍板（做） |
| 3 | 编辑/读取统一 | 方案 C 分两批 | C or B？改名要不要？ |
| 4 | get_avatar 矫正 | 做 | 行为描述如上确认 |
| 5 | delete 去两步确认 | 做 | 已拍板（做） |
| 6 | 文风规范 + 中文注入英文化 + persona-ab 实验 | 按序做 | 方向确认 |
| — | 生图 bug：DB 重建 + B/C/D 代码修 | 尽快 | 上轮已列，待拍板 |
