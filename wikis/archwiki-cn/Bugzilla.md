**翻译状态：**

  * 本文（或部分内容）译自 [Bugzilla](<https://wiki.archlinux.org/title/Bugzilla> "arch:Bugzilla")，最近一次同步于 2024-7-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Bugzilla?diff=0&oldid=761272>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Bugzilla_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [LAMP](<../zh-cn/Category:%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8.html> "LAMP")
  * [MariaDB](<../zh-cn/MariaDB.html> "MariaDB")
  * [Sqlite](<../zh-cn/SQLite.html> "Sqlite")

[Bugzilla](<https://www.bugzilla.org/>) 是一个设计为帮助你管理软件开发的服务器软件。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [bugzilla](<https://archlinux.org/packages/?name=bugzilla>)包 软件包。 

##  配置

###  模块依赖

首先执行模块检查: 
    
    # cd /srv/http/bugzilla
    # ./checksetup.pl --check-modules
    
通过输出查看哪些模块是必须的,哪些模块是可选的。用于安装缺失模块的 Shell 命令会显示出来。 

使用一下命令安装所有必须和可选的模块: 
    
    # perl install-module.pl --all
    
###  最终模块检查

接下来的更多配置会让 BugZilla 连接到 [MySQL](<../zh-cn/MySQL.html> "MySQL") 并在其中创建初始化表。 

再次运行 `checksetup.pl`,这次不带 `-check-modules`选项: 
    
    # ./checksetup.pl
    
如果一切正常,会创建一个 `localconfig` 文件。然后,修改文件中的一些参数: 
    
    $webservergroup = 'http';
    $db_driver = 'DATABASE_TO_USE_HERE';
    $db_name = 'DATABASE_NAME_HERE';
    $db_user = 'DATABASE_USER_HERE';
    $db_pass = 'YOUR_PASSWORD_HERE';
    
### Apache

最后,配置 [Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server") 来使用 mod_cgi (也可以使用 [mod_perl](</wzh/index.php?title=Mod_perl&action=edit&redlink=1> "Mod perl（页面不存在）") 来配置;详情请参考此节) 运行 Bugzilla。 

首先在 `/etc/httpd/conf/httpd.conf` 中将下列行取消注释: 
    
    LoadModule cgi_module modules/mod_cgi.so
    
然后把下列行加入 `/etc/httpd/conf/httpd.conf`: 
    
    <Directory /srv/http/bugzilla>
      AddHandler cgi-script .cgi
      Options +ExecCGI
      DirectoryIndex index.cgi
      AllowOverride All
    </Directory>
    
现在重启 Apache 和 需要的模块。 

使用你的网页浏览器访问 `http://_server_domain_or_ip_ /bugzilla/`。 

##  参见

  * [bugzilla 文档](<https://www.bugzilla.org/docs/>)
  * <https://web.archive.org/web/20200111080219/http://blog.samsonis.me/2009/04/bugzilla-on-archlinux/>
