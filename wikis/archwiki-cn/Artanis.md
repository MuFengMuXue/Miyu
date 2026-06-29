相关文章

  * [MySQL](<../zh-cn/MySQL.html> "MySQL")
  * [SQLite](<../zh-cn/SQLite.html> "SQLite")
  * [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")
  * [Scheme](<../zh-cn/Scheme.html> "Scheme")
  * [GNU](<../zh-cn/GNU.html> "GNU")
  * [分类:网络服务器](<../zh-cn/Category:%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "Category:网络服务器")

[GNU Artanis](<https://artanis.dev/>) 是 [Scheme](<../zh-cn/Scheme.html> "Scheme") 编程语言的第一个产品级现代网络框架。它的设计和维护都以稳健、快速和易于使用为目标，适用于专业的网络开发。 

GNU Artanis 以 GPLv3+ & LGPLv3+ 发布。它非常轻量级——新手也能轻松破解和学习。它具有一个完整的[网络服务器](<../zh-cn/Category:%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "Category:网络服务器")实现，包括一个错误页面处理程序。它支持的数据库（通过 guile-dbi）有 [MySQL](<../zh-cn/MySQL.html> "MySQL")、[SQLite](<../zh-cn/SQLite.html> "SQLite")、[PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")。 

##  安装

### Guix

**提示：** 推荐的方案。

如果您已经安装 [Guix](<../zh-cn/GNU_Guix.html> "Guix") 包管理器，可以直接使用以下命令安装： 
    
    guix install artanis
    
###  手动安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [guile](<https://archlinux.org/packages/?name=guile>)包、[base-devel](<https://archlinux.org/packages/?name=base-devel>)包、[nss](<https://archlinux.org/packages/?name=nss>)包 等基础软件包。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [guile-curl](<https://aur.archlinux.org/packages/guile-curl/>)AUR、[guile-json](<https://aur.archlinux.org/packages/guile-json/>)AUR、[guile-redis](<https://aur.archlinux.org/packages/guile-redis/>)AUR。 

切换至一个新目录，下载[最新版本源代码压缩文件](<http://ftp.gnu.org/gnu/artanis/artanis-latest.tar.bz2>)并[解压](<../zh-cn/%E5%BD%92%E6%A1%A3%E4%B8%8E%E5%8E%8B%E7%BC%A9.html> "归档与压缩")，切换至解压得到的目录，运行： 
    
    $ ./autogen.sh –no-configure 
    $ ./configure 
    $ make 
    # make install 
    
### AUR

安装 [artanis](<https://aur.archlinux.org/packages/artanis/>)AUR 或 [artanis-git](<https://aur.archlinux.org/packages/artanis-git/>)AUR。 

##  配置

首次运行 Artanis 时需要配置文件。 

  * 如果使用最小模式，例如，所有代码都在脚本文件中，而不在应用程序目录下。配置文件必须命名为 `/etc/artanis/artanis.conf`。

  * 如果使用应用程序目录，配置文件 `conf/artanis.conf` 会自动生成。

##  使用

在控制台中键入 `guile`，进入 **Guile REPL** 。屏幕上将显示以下文本： 
    
    GNU Guile 3.0.9
    Copyright (C) 1995-2023 Free Software Foundation, Inc.
    
    Guile comes with ABSOLUTELY NO WARRANTY; for details type `,show w'.
    This program is free software, and you are welcome to redistribute it
    under certain conditions; type `,show c' for details.
    
    Enter `,help' for help.
    scheme@(guile-user)>

本文许多对 Artanis 的操作都会在这里完成。 

###  运行

####  简单 HTTP 服务器

在控制台中运行这段代码： 
    
    guile -c "(use-modules (artanis artanis))(init-server)(run)"
    
您会看到这个屏幕： 
    
    Anytime you want to quit just try Ctrl+C, thanks!
    <http://127.0.0.1:3000>

####  运行一个使用 GNU Artanis 的站点

这是最简单的网站运行方式： 
    
    #!/bin/env guile
    !#
    (use-modules (artanis artanis))
    (init-server)
    (get "/hello" (lambda () "hello world"))
    (run)

####  运行服务器
    
    scheme@(guile-user)> (run #:host #f #:port #f #:debug #f #:use-db? #f #:dbd #f #:db-username #f #:db-passwd #f #:db-name #f)
    
关键字的值为 #f，默认情况下将从配置文件中获取值。 

但你也可以定义它们： 

  * **#:host** ：主机名。
  * **#:port** ：服务器的套接字端口。
  * **#:debug** ：设置 #t 如果您想要启用调试模式，日志将更加详细。
  * **#:use-db?** ：设置 #t 如果您想使用数据库，GNU Artanis 将初始化数据库连接。
  * **#:dbd** ：选择一个 dbd。这些是支持的三个：[postgresql](<../zh-cn/PostgreSQL.html> "PostgreSQL")、[mysql](<../zh-cn/MySQL.html> "MySQL") 和 [sqlite3](<../zh-cn/SQLite.html> "SQLite")。
  * **#:db-username** ：你的数据库服务器的用户名。
  * **#:db-passwd** ：上述用户的数据库密码。
  * **#:db-name** ：要使用的数据库名称。

####  与 Nginx 一起工作

您可以使用反向代理尝试 GNU Artanis+Nginx。 

虽然 GNU Artanis 有很好的服务器核心，但官方还是建议使用 [Nginx](<../zh-cn/Nginx.html> "Nginx") 作为前端服务器。除了性能增强外，它还不易受到攻击。 

以下是 `/etc/nginx/nginx.conf` 的一些示例行： 
    
    location / {
    proxy_pass http://127.0.0.1:''1234'';
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

要使其正常工作，请在[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑")文件后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") [Nginx](<../zh-cn/Nginx.html> "Nginx")，并运行 GNU Artanis： 
    
    scheme@(guile-user)> (run #:port _1234_)
    
##  参见

  * [GNU Artanis web-framework Manual](<https://www.gnu.org/software/artanis/manual/>)
  * `$ info artanis`
  * [官方网站](<https://artanis.dev/>)
  * [Savannah 页面](<https://savannah.gnu.org/projects/artanis>)
  * [Gitlab 仓库](<https://gitlab.com/hardenedlinux/artanis>)
