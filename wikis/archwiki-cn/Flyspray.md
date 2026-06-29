**翻译状态：**

  * 本文（或部分内容）译自 [Flyspray](<https://wiki.archlinux.org/title/Flyspray> "arch:Flyspray")，最近一次同步于 2025-02-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/Flyspray?diff=0&oldid=800907>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Flyspray_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [LAMP](<../zh-cn/Category:%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8.html> "LAMP")

[Flyspray](<https://www.flyspray.org/>) 是一个用 [PHP](<../zh-cn/PHP.html> "PHP") 编写的错误跟踪系统。尤为值得一提的是，Arch Linux 发行版自身就曾使用过 FlySpray 该系统。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [flyspray](<https://archlinux.org/packages/?name=flyspray>)包 软件包。Flyspray 需要 Web 服务器（例如带有 [PHP](<../zh-cn/PHP.html> "PHP") 的 [Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server")）和 SQL 服务器（例如 [MySQL](<../zh-cn/MySQL.html> "MySQL") 或 [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")）。 

###  Apache 配置

**注意：** 您需要将 [Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server") 配置为与 [PHP](<../zh-cn/PHP.html> "PHP")。查看 [Apache HTTP Server#PHP](<../zh-cn/Apache_HTTP_Server.html#PHP> "Apache HTTP Server") 以获得说明。确保取消注释 `/etc/php/php.ini` 中的 `extension=mysqli`。

您将需要为 apache 创建一个配置文件以找到您的 Flyspray 安装。创建以下文件： 
    
    /etc/httpd/conf/extra/flyspray.conf
    
    Alias /flyspray "/usr/share/webapps/flyspray"
    <Directory "/usr/share/webapps/flyspray">
    	AllowOverride All
    	Options FollowSymlinks
    	Require all granted
    	php_admin_value open_basedir "/srv/http/:/tmp/:/usr/share/webapps/flyspray"
    </Directory>

然后，您将需要编辑 `/etc/webapps/flyspray/.htaccess` 并将 `deny from all` 更改为 `allow from all`。现在，您应该能够导航到 flyspray 界面（例如 <http://localhost/flyspray> ），它将显示一个预安装检查页面。此处的所有问题都应先解决，然后再继续。 
