**翻译状态：**

  * 本文（或部分内容）译自 [Gitweb](<https://wiki.archlinux.org/title/Gitweb> "arch:Gitweb")，最近一次同步于 2025-01-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Gitweb?diff=0&oldid=825856>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Gitweb_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Gitweb 是 [Git](<../zh-cn/Git.html> "Git") 自带的默认网络界面。 

[Gitweb](<https://git-scm.com/docs/gitweb>) 实际上原生支持 FCGI，因此无需将其包装成 CGI 脚本。[[1]](<https://sixohthree.com/1402/running-gitweb-in-fastcgi-mode>)

##  安装

要安装 Gitweb，首先要安装 [git](<https://archlinux.org/packages/?name=git>)包 和[网络服务器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1%E5%99%A8> "网络服务器")。如果想快速测试，请参阅 `git instaweb` 的帮助。否则，如果你想要一个全面的设置，请继续阅读。 

以下所有示例都需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [perl-cgi](<https://archlinux.org/packages/?name=perl-cgi>)包 软件包。（[FS#45431](<https://bugs.archlinux.org/task/45431>)）。 

##  配置网络服务器

### Apache

将以下内容添加到 `/etc/httpd/conf/httpd.conf` 的末尾： 
    
    Alias /gitweb "/usr/share/gitweb"
    <Directory "/usr/share/gitweb">
       DirectoryIndex gitweb.cgi
       Options ExecCGI
       Require all granted
       <Files gitweb.cgi>
       SetHandler cgi-script
       </Files>
       SetEnv  GITWEB_CONFIG  /etc/gitweb.conf
    </Directory>
    
或者将其添加到另一个文件中，如 `etc/httpd/conf/extra/gitweb.conf` 然后在 `httpd.conf` 末尾添加以下内容： 
    
    # gitweb configuration
    Include conf/extra/gitweb.conf
    
如果 Apache 拒绝显示 Gitweb，而是打印 perl 脚本的纯源代码，则很可能是 Apache 的配置不允许执行 CGI。请确保 `httpd.conf` 中的以下内容未被注释： 
    
    <IfModule !mpm_prefork_module>
       LoadModule cgid_module modules/mod_cgid.so
    </IfModule>
    <IfModule mpm_prefork_module>
       LoadModule cgi_module modules/mod_cgi.so
    </IfModule>
    
然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `httpd.service` 来应用这些更改。有关使用 Apache 执行 CGI 的更多详情，请参阅 [https://httpd.apache.org/docs/2.4/howto/cgi.html。](<https://httpd.apache.org/docs/2.4/howto/cgi.html%E3%80%82>)

### Lighttpd

在 `/etc/lighttpd/lighttpd.conf` 中添加以下内容： 
    
    server.modules += ( "mod_alias", "mod_cgi", "mod_redirect", "mod_setenv" )
    url.redirect += ( "^/gitweb$" => "/gitweb/" )
    alias.url += ( "/gitweb/" => "/usr/share/gitweb/" )
    $HTTP["url"] =~ "^/gitweb/" {
           setenv.add-environment = (
                   "GITWEB_CONFIG" => "/etc/gitweb.conf",
                   "PATH" => env.PATH
           )
           cgi.assign = ( ".cgi" => "" )
           server.indexfiles = ( "gitweb.cgi" )
    }
    
然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `lighttpd.service` 来应用这些更改。 您可能还需要在 `mimetype.assign` 行添加 `".css" => "text/css"` 以便 GitWeb 正常显示。 

### Nginx

将此位置添加到 nginx 配置中（可能需要更改位置）： 
    
    /etc/nginx/nginx.conf
    
    location /gitweb.cgi {
        include fastcgi_params;
        gzip off;
        fastcgi_param   SCRIPT_FILENAME  /usr/share/gitweb/gitweb.cgi;
        fastcgi_param   GITWEB_CONFIG  /etc/gitweb.conf;
        fastcgi_pass    unix:/run/fcgiwrap.sock;
    }
    
    location / {
        root /usr/share/gitweb;
        index gitweb.cgi;
    }
    
如果您遵循 [Nginx#CGI 实现](<../zh-cn/Nginx.html#CGI_%E5%AE%9E%E7%8E%B0> "Nginx")，请尝试将`include fastcgi_params;`替换为`include fastcgi.conf;`。 

##  配置 Gitweb

所有配置选项的列表，请参见 [gitweb.conf(5)](<https://man.archlinux.org/man/gitweb.conf.5>) 。 

###  基本配置

打开（如果不存在，则创建）文件 `/etc/gitweb.conf`，并将此内容放入其中： 
    
    /etc/gitweb.conf
    
    # The directories where your projects are. Must not end with a slash.
    our $projectroot = "/path/to/your/repositories"; 
    
    # Base URLs for links displayed in the web interface.
    our @git_base_url_list = qw(git://<your_server> <http://git@><your_server>);

要启用 "blame" 视图（显示源文件中每一行的作者），请添加以下一行： 
    
    $feature{'blame'}{'default'} = [1];
    
配置完成后，[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启")网络服务器。 

###  添加仓库

要添加版本库，请进入版本库文件夹，像这样创建版本库： 
    
    $ mkdir my_repository.git
    $ git init --bare my_repository.git/
    $ cd my_repository.git/
    $ touch git-daemon-export-ok
    $ echo "Short project's description" > description
    
接下来打开 `config` 文件并添加以下内容： 
    
    config
    
    [gitweb]
    owner = _Your Name_

这将填写 Gitweb 中的 "Owner" 字段。这不是必填项。 

这里假定您希望将此仓库作为 "central" 仓库，将您的提交推送至此，因此 git-daemon-export-ok 和 --bare 的作用是将开销降至最低，并允许在此仓库上使用 git 守护进程。 

这就是创建版本库的全部过程。现在你可以在 <http://localhost/gitweb> 上看到它了（假设一切顺利）。由于 Gitweb CGI 脚本只需读取版本库文件夹，因此无需为新版本库重启 Apache。 

###  语法高亮

要在 Gitweb 上启用语法高亮，必须先安装 [highlight](<https://archlinux.org/packages/?name=highlight>)包 软件包： 

安装 highlight 后，只需在 `gitweb.conf` 中添加此行即可： 
    
    $feature{'highlight'}{'default'} = [1];
    
保存文件后，高亮显示就会启用。 

##  参见

  * [How To Install A Public Git Repository On A Debian Server](<https://www.howtoforge.com/how-to-install-a-public-git-repository-on-a-debian-server>)——HowtoForge 页面用作本文的主要资料来源。
