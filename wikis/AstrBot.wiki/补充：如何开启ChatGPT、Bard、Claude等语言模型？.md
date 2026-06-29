> 过时。请看 https://astrbot.soulter.top/center
> 过时。请看 https://astrbot.soulter.top/center

# 🌍支持的AI语言模型一览：
- OpenAI GPT-3模型（原生支持）
- OpenAI GPT-3.5模型（原生支持）
- OpenAI GPT-4模型（原生支持）
- ChatGPT网页版 GPT-3.5模型（免费，原生支持）
- ChatGPT网页版 GPT-4模型（需订阅Plus账户，原生支持）
- Bing（免费，原生支持）
- Claude模型（免费，由[LLMs插件](https://github.com/Soulter/LLMS)支持）
- HuggingChat模型（免费，由[LLMs插件](https://github.com/Soulter/LLMS)支持）
- Google Bard（免费，由[LLMs插件](https://github.com/Soulter/LLMS)支持）
- 任何与OpenAI ChatGPT接口一致的第三方语言模型服务


# 获取并填写

## 1. OpenAI系

> 至少需要：
> 1. 一个OpenAI账号
> 2. 一个稳定的国外梯子

### 官方ChatGPT

**如果您有OpenAI API Key**，可以在`QQChannelChatGPT/configs/config.yaml`下约86行处找到：
```yaml
openai:
  key: 
    - 这里填写你的apikey
    - 这里填写你的apikey，支持多个key，如果只有一个就把这一行删了
  api_base: none
  # 这里是GPT配置，语言模型默认使用gpt-3.5-turbo
  chatGPTConfigs:
    model: gpt-3.5-turbo # 这里可以是gpt-4，前提是你的账号有gpt-4的api权限
    max_tokens: 3000
    temperature: 0.9
    top_p: 1
    frequency_penalty: 0
    presence_penalty: 0
    
  total_tokens_limit: 5000
```
### 逆向ChatGPT

**如果您没有OpenAI API Key**，可以在[此处](https://chat.openai.com/api/auth/session)获得您OpenAI账号下的`session_token`，找到session_token那一段，然后复制双引号内的内容：
<img width="1277" alt="image" src="https://github.com/Soulter/QQChannelChatGPT/assets/37870767/4d11196c-0426-4ba5-8933-a5984df9a3a0">

然后，在`QQChannelChatGPT/configs/config.yaml`下约132行处找到：
```
# 支持使用access_token登录
rev_ChatGPT:
  enable: true
  account:
    - access_token: 这里填写你刚刚复制的access_token。
    - access_token: 这里填写你刚刚复制的access_token，支持多个，如果只有一个就把这一行删了
```

注意：默认是gpt-3.5。如果您是Plus账户，想用插件、网页搜索能力和gpt-4，请**先确保机器人程序是最新版本（使用update latest r指令更新并重启程序）**，然后找到并打开`cmd_config.json`，如果您是最新版本，那么会看到如下四个字段：
```json
    "rev_chatgpt_model": "",   // 可选。可以填gpt-4-browsing, text-davinci-002-render-sha, gpt-4, gpt-4-plugins，为空时默认是3.5
    "rev_chatgpt_plugin_ids": [], // 可选。插件的id。如["plugin-d1d6eb04-3375-40aa-940a-c2fc57ce0f51"]则使用wolfram Alpha
    "rev_chatgpt_PUID": "", // 可选。只有当你有Plus账户时必填
    "rev_chatgpt_unverified_plugin_domains": [] // 可选。未经验证的插件
```

⚠ 2023/09/29：默认启动已不能正常使用，需要在`cmd_config.json`修改`CHATGPT_BASE_URL`的值为自己搭建的 bypass 服务器链接，或者可以使用我自建的，链接详情请加QQ群`322154837`

### 免费ChatGPT

当然，你也可以使用完全免费的OpenAI ChatGPT，由 https://github.com/chatanywhere/GPT_API_free 提供支持。
打开这个链接，然后点击**申请免费内测**，就可以得到一个免费的第三方key，把它复制下来。

在`QQChannelChatGPT/configs/config.yaml`下约86行处找到：
```yaml
openai:
  key: 
    - 这里填写刚刚复制的key
  api_base: https://api.chatanywhere.com.cn # 无需梯子
  chatGPTConfigs:
    model: gpt-3.5-turbo # 如果申请的是免费内测key，那么只能用gpt-3.5-turbo
    max_tokens: 3000
    temperature: 0.9
    top_p: 1
    frequency_penalty: 0
    presence_penalty: 0
  total_tokens_limit: 5000
```
如果文件夹下有`chatgpt_key_record`，将其删除再重启即可。

有经济能力可以支持一下https://github.com/chatanywhere/GPT_API_free 购买低价key，获得更多模型。

Enjoy~



## 2. Claude、HuggingChat、Bard

> 对于Claude，需要美国或者英国的梯子；对于HuggingChat，需要梯子；对于Bard，需要梯子

在聊天区内对机器人发送`plugin i https://github.com/Soulter/LLMS`来安装LLMs插件，安装完成之后，发送`llm`查看细节。

如何获取 Claude、Bard 的Cookie？ / 如何注册HuggingChat？ 
1. Claude：https://github.com/KoushikNavuluri/Claude-API
2. HuggingChat：https://github.com/Soulter/hugging-chat-api
3. Bard：https://github.com/acheong08/Bard
