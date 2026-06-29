**翻译状态：**

  * 本文（或部分内容）译自 [Home Assistant Supervised](<https://wiki.archlinux.org/title/Home_Assistant_Supervised> "arch:Home Assistant Supervised")，最近一次同步于 2025-08-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Home_Assistant_Supervised?diff=0&oldid={{{3}}}>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Home_Assistant_Supervised_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Home Assistant](<../zh-cn/Home_Assistant.html> "Home Assistant")
  * [AppArmor](<../zh-cn/AppArmor.html> "AppArmor")

[Home Assistant](<https://www.home-assistant.io/>) 是一个开源的家庭自动化软件，它把本地控制和隐私放在首位。由全球的 DIY 爱好者和技术爱好者组成的社区提供支持。 

Supervised 是一种安装方式，可提供更多功能，例如通过 UI 安装插件。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [homeassistant-supervised](<https://aur.archlinux.org/packages/homeassistant-supervised/>)AUR 软件包。 

并确保 [AppArmor](<../zh-cn/AppArmor.html> "AppArmor") 已正确安装并配置。 

**注意：**

  * 从 3.0.0 版起，不再强制要求 CGroup v1，因此可删除早期版本所需的 [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") `systemd.unified_cgroup_hierarchy=false`。
  * Supervised 安装方式已被上游弃用，将不再获得支持。详见 [[1]](<https://www.home-assistant.io/blog/2025/05/22/deprecating-core-and-supervised-installation-methods-and-32-bit-systems/>)。

##  配置

Home Assistant Supervised 的配置文件保存在 `/var/lib/homeassistant/` 中。若不存在配置文件，启动时会写入默认配置。 

若只想访问 Home Assistant 自身的配置文件，请前往 `/var/lib/homeassistant/homeassistant/`。 

###  若早于 v3.0.0 安装

Supervised 的默认配置目录已由 `/usr/lib/hassio/` 更改为 `/var/lib/homeassistant/`。你可以继续使用旧配置。如需更改路径，请在配置文件 `/etc/hassio.json` 中设置 _data_ 值。 

##  用法

启动 Home Assistant，请 [启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `hassio-apparmor.service` 与 `hassio-supervisor.service`。 

第一次启动可能需要 20 分钟，因为将下载并安装所需的软件包。[[2]](<https://www.home-assistant.io/docs/installation/>) 。 

默认情况下，Web 界面位于 `<http://localhost:8123>`。 

##  疑难解答

在进行任何操作前，请先确认 Supervisor 已连接且安装状态为良好。可通过访问 [监控插件](<https://github.com/home-assistant/plugin-observer>)（地址为 `<http://localhost:4357>` ）进行检查。 

###  Supervisor 未连接

  1. 确认 `hassio-supervisor.service` 已[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")。
  2. 确认 supervisor 容器正在运行：

    # docker ps | grep hassio_supervisor

###  Supervisor 已连接但安装状态不良好

  1. 确认 [AppArmor](<../zh-cn/AppArmor.html#%E6%98%BE%E7%A4%BA%E5%BD%93%E5%89%8D%E7%8A%B6%E6%80%81> "AppArmor") 已正确安装并配置。
  2. 确认已[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `hassio-apparmor.service` 服务。
  3. 查看 Supervisor 日志获取更多信息：

    # docker logs -f hassio_supervisor

###  文件 /etc/hassio.json 不存在

请确保 `/etc/hassio.json` 配置文件存在。 

若不存在，请创建该文件并填写以下示例内容： 
    
    {
        "supervisor": "ghcr.io/home-assistant/amd64-hassio-supervisor",
        "machine": "generic-x86-64",
        "data": "/var/lib/homeassistant"
    }
    