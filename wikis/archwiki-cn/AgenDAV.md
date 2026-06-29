**翻译状态：**

  * 本文（或部分内容）译自 [AgenDAV](<https://wiki.archlinux.org/title/AgenDAV> "arch:AgenDAV")，最近一次同步于 2020-05-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/AgenDAV?diff=0&oldid=615841>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/AgenDAV_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [DAViCal](</wzh/index.php?title=DAViCal&action=edit&redlink=1> "DAViCal（页面不存在）")
  * [Kcaldav](<../zh-cn/KDE.html> "Kcaldav")
  * [Radicale](</wzh/index.php?title=Radicale&action=edit&redlink=1> "Radicale（页面不存在）")

[AgenDAV](<https://agendav.org/>) 是一个用 PHP 编写的开源多语言 CalDAV Web 应用程序，具有丰富的 AJAX 界面和共享日历支持。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [agendav](<https://aur.archlinux.org/packages/agendav/>)AUR 包。 

###  数据库

您必须向 AgenDAV 提供一个 SQL 数据库。 这是一个 PostgreSQL 示例。 

根据 [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL") 文章安装 PostgreSQL。创建一个 `agendav` 用户和数据库： 
    
    # createuser agendav
    # createdb -O agendav agendav
    
###  配置

设置数据库后，必须手动填充它： 
    
    # psql -U agendav agendav < /usr/share/webapps/agendav/sql/pgsql.schema.sql
    # bash /usr/share/webapps/agendav/bin/agendavcli dbupdate
    
确保在 `php.ini` 中启用 `extension=pgsql`（或使用的任何数据库）和 `extension=iconv` 扩展。 

根据您的喜好编辑配置文件 `/etc/webapps/agendav/{config,caldav,database}.php`。 

通过 apache：`/etc/webapps/agendav/apache.example.conf`，nginx/php-fpm：`/etc/webapps/agendav/nginx.example.conf` 或其他一些 Web 服务器来服务该应用程序。 
