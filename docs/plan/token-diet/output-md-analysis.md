# 想法 1 全量分析：工具输出 JSON→md/文本

口径：实测数据来自真实库 08-11~08-21（410 次调用、833KB 输出）；"开销%" = JSON 结构字节（键名/括号/引号/转义）÷ 该工具 JSON 输出字节。"消费者" = 除 LLM 外解析该输出 JSON 的本地代码。改造原则：**功能语义零变化**；旧回合 tool_flow 逐字节回放，所有旧 JSON 解析器保留双兼容（先例：render/command.rs:789）。

## 0. 全局设计约束（改任何一个工具前都要解决）

| 约束 | 现状 | 迁移方案 |
|---|---|---|
| 成败判定 | `agent/artifacts.rs:9 tool_output_succeeded` 读顶层 `success`/`ok` 布尔；非 JSON 一律判成功。WebUI 卡片配色 `web/dto.rs:109` 同源 | 硬失败已走 `Err`→`tool error:` 前缀，不受影响。**业务失败**（ok:false 但 Ok 返回）的工具改造时必须同步改为返回 `Err` 或保留 JSON——逐工具核对，表中"业败"列标注 |
| WebUI 面板 | todos.js / shared.js 解析输出 JSON 渲染面板（首字符 `{` 短路，非 JSON 静默降级） | todowrite 改走既有 `GET /api/sessions/{id}/todos`（todos.js:39 注释自证同构）；share_file 本轮不动（保留 JSON） |
| 结构化侧信道 | `agent/reports.rs`/`tool_report.rs` 从输出 JSON 提取加载清单、持久化报告、compact 摘要 | 涉及工具（load_tools/task/deep_research/use_meme:show/remember_fact/artifact 类）改造时解析器同步迁移，或改走内部结构体侧信道（handler 返回时另挂元数据，不进 LLM 字节） |

## 1. 全量工具表

推荐列：**改**（md/文本化）、**少回显**（比换格式收益更大）、**留 JSON**（结构即功能）、**缓**（低频低收益，不值得动）。

### A. 高收益（有实测浪费，优先）

| 工具 | 30 天实测 | 开销% | 消费者 | 目标形态 | 推荐 |
|---|---|---|---|---|---|
| todowrite | 28 次 / 41.6KB | 65% | todos.js 面板、REPL 表格渲染(render/table.rs:313) | 一行确认 + 变更摘要（"3 项：2 done 1 pending"），不回显全表；REPL/WebUI 面板改走 todos API | **少回显+改** |
| load_tools | 21 次 / 31.3KB | 54% | `agent/reports.rs:62 loaded_items_from_output`（懒加载核心！） | 文本清单（"已加载: web_search, group:gaming"），**不回显契约/schema**（下一请求 tools 数组本来就有全文，纯重复）；loaded_items 解析器迁移为文本解析+旧 JSON 双兼容 | **少回显+改** |
| search_real_chat_history | 22 次 / 39.5KB | 31% | 无 | md 行格式（`[时间] 会话/发送者: 内容`），键名只出现一次于表头 | **改** |
| qq_group_manage_history_query | 1 次 / 7.2KB | 57% | 无 | 同上，md 行/表 | **改** |
| qq_group_manage | 9 次 / 6.1KB | 46% | 测试断言 `response["success"]` | 一行结果文本（"已禁言 123456 600 秒"）；业败核对 | **改** |
| use_meme (search) | 12 次 / 3.9KB | 41% | 无（show 才有 compact 报告） | 候选列表 md（id/名称/标签 一行一条） | **改** |
| use_meme (show) | 34 次合计 / 16.2KB | 19% | `agent/reports.rs:100 compact_sent_meme_report`（id/description） | 一行确认；compact 报告解析器同步迁移 | **改** |
| task | 3 次 / 1.1KB | 45% | `tool_report.rs:52` 持久化提取 `result` 字段 | 子代理最终文本直接作为输出正文（往往本来就是文本），元信息一行头部；提取器迁移 | **改** |

### B. 中等（格式换了有小赚，业务低频）

| 工具 | 30 天实测 | 开销% | 消费者 | 推荐 |
|---|---|---|---|---|
| get_weather | 0 次 | — | 无 | **改**（结构是逐小时/逐天数组，md 表收益大，但样本 0 → 顺手做） |
| job (status/output) | 样本混入 run_command | — | 无 | **改**（status 一行 + 日志正文裸文本） |
| check_issue / deep_diagnose | 0 次 | — | `tool_report.rs` 提取 `final_report` | **改**（final_report 本是文本，直接作正文；提取器迁移） |
| generate_image | 8 次 / 2.4KB | 20% | 平台出图管线核对（path 字段） | **缓**（QQ 投递链依赖 path 字段，动收益小风险大） |
| search_web_images | 0 次 | — | 预览管线 | **缓** |
| memory 四件套 (recall 等) | 少量 | — | `reports.rs` remembered_fact 报告 | **改**（召回结果 md 列表天然合适；报告解析器迁移） |
| 知识库四件套 (search 等) | 3 次 / 10.4KB | 29% | 无 | **改**（搜索结果 md 列表） |
| aur / archlinux 家族 | 0 次 | — | aur_review_install_guard 看的是调用不是输出 | **改**（包信息 md 表） |
| codec / scientific_calculator / get_exchange_rate | 0 次 | — | 无 | **改**（一行结果） |
| moegirl/archwiki/fcitx/man/deepseek_status/query_api_quota | 低 | — | 无 | **改**（部分已是文本；补齐 JSON 分支） |
| manage_script (list) | 0 次 | — | 无 | **改** |
| claude_code | 0 次（近期） | — | `session_id` 字段续传 | **缓**（resume 依赖结构字段） |
| deep_research | 0 次（近期） | — | `final_report` 提取 + 引用注册流 | **缓**（内部管线多，单独评估） |

### C. 留 JSON（结构即功能，不动）

| 工具 | 理由 |
|---|---|
| ask_question | `status` 字段被 journal redo 计数（context.rs:419）与问答流程消费；输出极短 |
| read_clipboard | `agent/images.rs:33` 靠字段决定是否送视觉模型；输出短 |
| write_file / edit_string / apply_patch / trash_path | `artifact_candidate_paths` 读 `created`/`files[]`；输出是一行 JSON 很短，改了省不了几个字节 |
| artifact 三件套 | compact_artifact_tool_report 读 files/path/title；WebUI 发布流 |
| share_file | shared.js 卡片；输出短 |
| send_message_to_user | 平台投递回执结构；输出短 |
| goal 三件套 | goal_value 结构被 goal 流程消费；输出短 |
| alarm / manage_skill / manage_meme 等 CRUD 确认 | 输出一行 JSON，省不出肉；测试断言密集 |
| 用户脚本工具 | 脚本自定输出，壳层不该碰 |
| MCP 工具 | 已是上游 text 拼接 |

## 2. 收益预估

- A 组落地 ≈ 省 56KB/833KB ≈ **6.7%** 的工具输出字节（其中"少回显"贡献大于换格式：todowrite 全表回显与 load_tools 契约回显本身就是纯浪费）
- B 组全部落地再 +1~1.5%
- token 视角：JSON 键名/引号/转义的 tokenize 效率低于自然文本，实际 token 节省率会略高于字节率

## 3. 建议的执行切分（等拍板）

1. **第一批（A 组 8 个）**：先立成败信号与双兼容基建，再逐工具改造 + 消费者迁移 + 测试更新；stub-LLM 测具跑改前/改后 tool result 字节对比
2. **第二批（B 组标"改"的）**：机械性套用第一批模式
3. C 组与标"缓"的：本轮不动，理由已注明
