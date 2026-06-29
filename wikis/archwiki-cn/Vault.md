[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Vault](<../zh-cn/Talk:Vault.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Vault](<https://wiki.archlinux.org/title/Vault> "arch:Vault")，最近一次同步于 2020-04-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Vault?diff=0&oldid=605503>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Vault_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [vault](<https://archlinux.org/packages/?name=vault>)包 包。 

##  服务

Vault 由 [systemd 单元](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd") `vault.service` 控制。[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")这个单元。 

###  配置

[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `/etc/vault.hcl` 文件。 

###  在开发人员模式下运行服务器

遵循 <https://www.vaultproject.io/docs/concepts/dev-server.html> 。 注意 API 的更改： <https://stackoverflow.com/questions/49872480/vault-error-while-writing> 。 
