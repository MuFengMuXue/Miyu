**翻译状态：**

  * 本文（或部分内容）译自 [Mailman](<https://wiki.archlinux.org/title/Mailman> "arch:Mailman")，最近一次同步于 2024-5-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Mailman?diff=0&oldid=815870>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Mailman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 需要翻译。（在 [Talk:Mailman#](<../zh-cn/Talk:Mailman.html>) 中讨论）

[Mailman](<https://gitlab.com/mailman/mailman>) 是一个邮件列表管理系统。它与[邮件服务器](<../zh-cn/%E9%82%AE%E4%BB%B6%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "邮件服务器")结合使用。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[mailman3](<https://archlinux.org/packages/?name=mailman3>)包软件包。 

Mailman 可与[Postorius](</wzh/index.php?title=Postorius&action=edit&redlink=1> "Postorius（页面不存在）")（用于配置）和[Hyperkitty](</wzh/index.php?title=Hyperkitty&action=edit&redlink=1> "Hyperkitty（页面不存在）")（用于存档）结合使用。 

**注意：** _Mailman_ 以`mailman`专用用户的身份运行，因此任何对`mailman`可执行文件的调用都必须以`mailman`用户的身份进行。

##  配置

All configuration for Mailman takes place in `/etc/mailman.cfg`. The schema explaining all possible configuration options and setting the defaults is stored in `/usr/lib/python3.8/site-packages/mailman/config/schema.cfg`. 

The configuration is also accessible via the command line. Run the following command as the `mailman` user (e.g. using [sudo](<../zh-cn/Sudo.html> "Sudo") or [su](<../zh-cn/Su.html> "Su")): 
    
    [mailman]$ mailman conf
    
###  数据库

Mailman by default uses an [SQLite](<../zh-cn/SQLite.html> "SQLite") [database](<https://mailman.readthedocs.io/en/latest/src/mailman/docs/database.html>) in `/var/lib/mailman/data/`, but can be configured to use [MariaDB](<../zh-cn/MariaDB.html> "MariaDB") or [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL"). 

#### SQLite

The default location for the [SQLite](<../zh-cn/SQLite.html> "SQLite") database is already reflected in the `schema.cfg` and therefore does not have to be set in Mailman's configuration. 
    
    /etc/mailman.cfg
    
    [database]
    url: sqlite:////var/lib/mailman/data/mailman.db
    
#### MariaDB

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [python-pymysql](<https://archlinux.org/packages/?name=python-pymysql>)包 package and configure a database on [MariaDB](<../zh-cn/MariaDB.html> "MariaDB"). 
    
    /etc/mailman.cfg
    
    [database]
    class: mailman.database.mysql.MySQLDatabase
    url: mysql+pymysql://_myuser_ :_mypassword_ @_mymysqlhost_ /mailman?charset=utf8&use_unicode=1

#### PostgreSQL

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [python-psycopg2](<https://archlinux.org/packages/?name=python-psycopg2>)包 package and create a database using [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL"). 
    
    /etc/mailman.cfg
    
    [database]
    class: mailman.database.postgresql.PostgreSQLDatabase
    url: postgres://_myuser_ :_mypassword_ @_mypghost_ /mailman
    
### REST API

Mailman exposes its REST API based on the settings in the `[webservice]` section of the configuration. Make sure to replace the default values for `admin_user` and `admin_pass` (do **not** use the example values below). 
    
    /etc/mailman.cfg
    
    [webservice]
    admin_user: my_new_admin_user_name
    admin_pass: my_new_admin_user_password
    
### ARC

By default [DMARC](<https://en.wikipedia.org/wiki/DMARC> "wikipedia:DMARC") and [DKIM](<https://en.wikipedia.org/wiki/DKIM> "wikipedia:DKIM") are disabled. The configuration takes place in the `[ARC]` section of the configuration file. Make sure to set necessary values and read the documentation about the defaults. 
    
    /etc/mailman.cfg
    
    [ARC]
    enabled: yes
    authserv_id: mailserver.tld
    trusted_authserv_ids: subdomain.mailserver.tld, other.mailserver.tld
    privkey: /path/to/privatekey.pem
    selector: test
    domain: mailserver.tld
    
### MTA

To connect a mail-transfer-agent (MTA), it is necessary to configure the `[mta]` section in the configuration file. [Upstream documentation](<https://mailman.readthedocs.io/en/latest/src/mailman/docs/mta.html>) covers examples for [postfix](<../zh-cn/Postfix.html> "Postfix"), [exim](</wzh/index.php?title=Exim&action=edit&redlink=1> "Exim（页面不存在）") and [sendmail](<../zh-cn/Sendmail.html> "Sendmail"), but other MTAs are technically possible. 

#### Postfix

To connect to a local [postfix](<../zh-cn/Postfix.html> "Postfix") instance the following configuration section can be used: 
    
    /etc/mailman.cfg
    
    [mta]
    incoming: mailman.mta.postfix.LMTP
    outgoing: mailman.mta.deliver.deliver
    lmtp_host: mail.example.com
    lmtp_port: 8024
    smtp_host: mail.example.com
    smtp_port: 25
    
The [postfix](<../zh-cn/Postfix.html> "Postfix") configuration has to be extended to ensure compatibility (see [upstream notes](<https://mailman.readthedocs.io/en/latest/src/mailman/docs/mta.html#basic-postfix-connections>)). 
    
    /etc/postfix/main.cf
    
    [..]
    recipient_delimiter = +
    unknown_local_recipient_reject_code = 550
    owner_request_special = no
    [..]
    
Additionally, [postfix](<../zh-cn/Postfix.html> "Postfix") needs to be made aware of mailman's [transport maps](<https://mailman.readthedocs.io/en/latest/src/mailman/docs/mta.html#transport-maps>). Depending on the postfix configuration these may look similar to the following. 

**注意：** The following examples assume that existing values for `transport_maps`, `local_recipient_maps`, `relay_domains`, `virtual_mailbox_domains` and `virtual_alias_maps` are merged with the additional values.
    
    /etc/postfix/main.cf
    
    [..]
    transport_maps = hash:/var/lib/mailman/data/postfix_lmtp
    local_recipient_maps = hash:/var/lib/mailman/data/postfix_lmtp
    relay_domains = hash:/var/lib/mailman/data/postfix_domains
    [..]
    
If `postmap` is not directly accessible by mailman for creating the default hash-based alias maps, it is possible to generate regular expression based alias maps instead. To overwrite the default Python-class based configuration, mailman allows the use of a configuration file. Create the following file: 
    
    /etc/postfix-mailman.cfg
    
    [postfix]
    postmap_command: /usr/bin/postmap
    transport_file_type: regex
    
Add the file to the `[mta]` section in mailman's configuration file. 
    
    /etc/mailman.cfg
    
    [mta]
    _[..]_
    configuration: /etc/postfix-mailman.cfg
    
Afterwards the `regexp` based exports can then be used in the [postfix](<../zh-cn/Postfix.html> "Postfix") configuration. 
    
    /etc/postfix/main.cf
    
    [..]
    transport_maps = regexp:/var/lib/mailman/data/postfix_lmtp
    local_recipient_maps = regexp:/var/lib/mailman/data/postfix_lmtp
    relay_domains = regexp:/var/lib/mailman/data/postfix_domains
    [..]
    
**注意：** Make sure to create the new alias maps after changing their type (e.g. from `hash` to `regexp`): `[mailman]$ mailman aliases`

To connect to a local [postfix](<../zh-cn/Postfix.html> "Postfix") instance with a [virtual mail](<../zh-cn/Postfix.html#Virtual_mail> "Postfix") setup, first [set an alias domain](</wzh/index.php?title=Postorius&action=edit&redlink=1> "Postorius（页面不存在）"). Afterwards alter the respective configuration. 
    
    /etc/postfix/main.cf
    
    [..]
    local_recipient_maps = regexp:/var/lib/mailman/data/postfix_lmtp
    transport_maps = regexp:/var/lib/mailman/data/postfix_lmtp
    virtual_mailbox_domains = regexp:/var/lib/mailman/data/postfix_domains
    virtual_alias_maps = regexp:/var/lib/mailman/data/postfix_vmap
    [..]
    
##  运行

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `mailman3.service`。 

有几个[systemd](<../zh-cn/Systemd.html> "Systemd")定时器服务，负责列表管理的各个方面： 

  * `mailman3-digests.timer`：用于向订阅者发送每日摘要。
  * `mailman3-gatenews.timer`：每小时轮询[NNTP](<https://en.wikipedia.org/wiki/Network_News_Transfer_Protocol> "wikipedia:Network News Transfer Protocol")服务器以获取新闻
  * `mailman3-notify.timer`：用于每天向管理员发送待处理请求的通知。

##  安装

###  与邮件服务器集成

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Example for setup with [mail server](<../zh-cn/Mail_server.html> "Mail server") (based on [upstream documentation](<https://mailman.readthedocs.io/en/latest/src/mailman/docs/mta.html>)). (在 [Talk:Mailman](<../zh-cn/Talk:Mailman.html>) 中讨论)

###  与 Hyperkitty 集成

Mailman does not automatically archive mails on its own. The [Hyperkitty](</wzh/index.php?title=Hyperkitty&action=edit&redlink=1> "Hyperkitty（页面不存在）") web application is used for this purpose. Based on a plugin, mailman is able to send mails to a [Hyperkitty](</wzh/index.php?title=Hyperkitty&action=edit&redlink=1> "Hyperkitty（页面不存在）") instance for archival. 

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [mailman3-hyperkitty](<https://archlinux.org/packages/?name=mailman3-hyperkitty>)包 package and configure `/etc/mailman-hyperkitty.cfg`. 
    
    /etc/mailman-hyperkitty.cfg
    
    [general]
    base_url: https://example.tld/hyperkitty/
    api_key: super_secret_password
    
Afterwards, make mailman aware of the plugin: 
    
    /etc/mailman.cfg
    
    [archiver.hyperkitty]
    class: mailman_hyperkitty.Archiver
    enable: yes
    configuration: /etc/mailman-hyperkitty.cfg
    
##  提示与技巧

###  从 mailman < 3.0 迁移

Mailman 可以导入基于 mailman < 3.0 的列表数据库（`config.pck`）。以 `mailman` 用户身份（例如使用 [sudo](<../zh-cn/Sudo.html> "Sudo") 或 [su](<../zh-cn/Su.html> "Su") ）运行以下命令： 
    
    [mailman]$ mailman import21 _LISTSPEC_ _PICKLE_FILE_
    
这里，` _LISTSPEC_` 表示要导入的列表的全称（例如 `list@example.com`），` _PICKLE_FILE_` 表示列表的 `config.pck` 文件路径。 

**注意：** 要导入的 mailman2 列表**必须** 已经存在于目标 mailman 实例中。

### REST API

Mailman 公开了[REST API](<https://mailman.readthedocs.io/en/latest/src/mailman/rest/docs/rest.html#the-rest-server>)，可使用基于 [python-mailmanclient](<https://archlinux.org/packages/?name=python-mailmanclient>)包 的自定义工具进行连接。 

##  参见

  * [Mailman 文档](<https://mailman.readthedocs.io/en/latest/>) \- 上游文档
  * [Mailmanclient 文档](<https://mailmanclient.readthedocs.io/en/latest/>) \- 上游文档
  * [连接到 Mailman](<https://hyperkitty.readthedocs.io/en/latest/install.html#connecting-to-mailman>) \- 关于[mailman3-hyperkitty](<https://archlinux.org/packages/?name=mailman3-hyperkitty>)包的上游文档
  * [Mailman Suite 文档](<https://docs.mailman3.org/en/latest/>) \- 整个 Mailman 套件（Mailman、Hyperkitty 和 Postorius）的（高级）上游文档
