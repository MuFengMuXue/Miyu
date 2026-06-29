[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:YOURLS](<../zh-cn/Talk:YOURLS.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [YOURLS](<https://wiki.archlinux.org/title/YOURLS> "arch:YOURLS")，最近一次同步于 2020-04-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/YOURLS?diff=0&oldid=608935>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/YOURLS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[YOURLS](<https://yourls.org/>) 是用 PHP 编写的自托管链接缩短程序服务。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [yourls](<https://aur.archlinux.org/packages/yourls/>)AUR 包。 

##  设置

需要 [MySQL](</wzh/index.php?title=MariaDB_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "MariaDB \(简体中文\)（页面不存在）") 数据库和用户才能完成 `/etc/webapps/yourls/config.php` 处的配置文件。 

在同一个配置文件中，将 `YOURLS_SITE` 设置为您的短域名 `https://_example.org_` 或子域名 `http://_example.org_ /_s_`，但始终不带 `/` 尾随。 

设置一个随机的 cookie 密钥，例如使用 `pwgen 50 1` 和 admin 用户的用户/密码组合。您可以编写哈希或纯文本，但是在后一种情况下，[web 服务器](</wzh/index.php?title=List_of_applications/Internet_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "List of applications/Internet \(简体中文\)（页面不存在）")需要 `rw` 权限才能对其进行 hash。 
