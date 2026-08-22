# 工具 schema 冗余审计表（想法 3）

在「裁定」列填你的决定：`删` / `留` / `合并` / 其他意见。空着 = 按我的推荐执行。

计费背景：默认 stub 加载模式下，**懒加载工具不发送 schema**（只发一行 stub），所以 schema 精简的收益集中在**常驻(AL)工具**和**平台内联工具**；懒加载工具的 schema 只在被 load 后计费，性价比低，只挑最离谱的。

## 一、常驻工具（每请求计费，收益最高）

| 工具 | 参数 | 现状 | 我的推荐 | 理由 | 裁定 |
|---|---|---|---|---|---|
| run_command | `title` | 后台任务 UI 标题，≤16 字符 | 删 | 纯 UI 装饰；后台任务没标题时 UI 可回退用命令前缀。省 schema + 模型每次后台命令多想一个参数 | 留 |
| task | `max_steps` | 可选步数上限 | 留 | 有真实控制价值 | 留 |
| task | `resume_id` | 断连续传（同进程内有效） | 留 | 0.4.4 刚修的功能，描述可精简 | 留 |
| use_meme | `size`/`width`/`height` | 三个参数控制 chafa 尺寸 | 合并 | 只留 `size`（"40x15"格式），width/height 删掉。print_image 同理 | 合并 |
| use_meme | `library` | 表情库覆盖 | 删 | 多库场景极少，配置侧已有默认库 | 删 |
| use_meme | `limit` | search 候选上限，默认已配置 | 删 | 默认值够用；模型极少需要改 | 删 |
| web_search | `provider` | 8 值枚举选搜索后端 | 删 | 后端选择是配置层的事，模型基本不该选；枚举里还有内部实现名(script/anysearch) | 删 |
| web_fetch | `timeout` | 超时秒数 | 删 | 默认值够用 | 删 |
| share_file | `snapshot` | 快照到托管存储 | 留 | 语义有用 | |
| remember_fact | `source` | 来源标签 | 留 | 记忆溯源在用 | |
| grep/glob | `max_results` | 上限 | 留 | 常用 | |

## 二、平台内联工具（QQ 回合全部常驻计费）

| 工具 | 参数 | 现状 | 我的推荐 | 理由 | 裁定 |
|---|---|---|---|---|---|
| search_real_chat_history | `user_id` | 明写"sender_id 的旧别名" | 删出 schema | 处理器保留兼容解析，模型看不到别名即可；纯重复 | 删 |
| search_real_chat_history | `group_id` | 与 `conversation_id` 语义重叠（群号） | 删出 schema | 同上，处理器留兼容 | 删 |
| delete_real_chat_history | `group_id` | 同上重叠 | 删出 schema | 同上 | 删 |
| search_real_chat_history / delete_real_chat_history | `all_conversations`+`all_groups` | 两个布尔开关语义相近 | 留 | 合并成 scope 枚举是语义变更，不动 | 这么多real_chat_history的工具，是不是可以合并一下？ |
| qq_group_manage | `duration`（title 有效期） | 默认 -1 永久；QQ 协议侧头衔有效期基本不生效 | 删 | 实际无效的参数 | 删 |
| qq_group_manage_history_query | `sort_order` | asc/desc，默认 desc | 删 | 默认排序够用，节省一整行枚举 | 删 |
| get_real_chat_activity_ranking | `include_bot` | 默认 true | 留 | 有真实使用场景（排除自己看排行） | 删 |
| job | `offset` 描述 | 85 词长描述 | 精简描述 | 功能留，描述在草稿里改 | 可以 |
| send_message_to_user / qq_mention_users / get_avatar 等 | — | 参数都精干 | 不动 | | |

## 三、懒加载工具（load 后才计费，只挑离谱的）

| 工具 | 参数 | 现状 | 我的推荐 | 理由 | 裁定 |
|---|---|---|---|---|---|
| scientific_calculator | `operation` | 单值枚举 `['evaluate']` | 删 | 只有一个取值的枚举是纯浪费 | 删 |
| print_image | `size`/`width`/`height` | 三选一控制尺寸 | 合并 | 只留 `size` | 合并 |
| manage_script | `always_loaded`/`load_policy`/`groups` | 加载策略覆盖 | 删 | 高级配置应走配置文件/JSON 真相源，不该由对话内模型填 | 留 |
| search_web_images | `preview_count` | chafa 预览数量 | 删 | `preview` 布尔已够；数量走配置 | 这里是不是有搜几张，还有看几张？我觉得搜几张就代表了看几张？所以可以删？ |
| check_issue | `launch_timeout_seconds` | 启动探针等待秒数 | 删 | `allow_launch_probe` 已是开关，秒数走默认 | 删 |
| divine | dice 三参数 | count/sides/modifier | 留 | 骰子语义需要 | |
| manage_meme | 11 参数 | add/update/delete 共用 | 留 | 字段都有真实语义，且懒加载 | |

## 四、顺带发现的死资产（建议一并清理，零风险）

| 项 | 现状 | 推荐 | 裁定 |
|---|---|---|---|
| `descriptions/edit_file.json` | 工具已无注册点，JSON 是孤儿 | 删文件 + 宏行 | 删 |
| `descriptions/share_file.json` | 从未被 include_str!（宏列表漏了它），改了不生效 | 二选一：补进宏（转正）或删 JSON 留 Rust 内联。推荐补进宏，统一真相源 | 补 |
| `write_file`/`edit_string` 的 register 函数 | 无人调用（随 dev 同步退场） | 留（未来可能回归），但对应 JSON 归入懒加载不计费，不动 | 删，现在applypatch这一个工具就能干所有编辑的活了 |
| `query_token_usage` 描述两处逐字重复 | usage_query.rs 与 platforms/tool.rs | 收敛到一处常量 | 可以 |
