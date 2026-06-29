**翻译状态：**

  * 本文（或部分内容）译自 [Git server](<https://wiki.archlinux.org/title/Git_server> "arch:Git server")，最近一次同步于 2024-5-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/Git_server?diff=0&oldid=810719>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Git_server_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 需要翻译。（在 [Talk:Git 服务器#](<../zh-cn/Talk:Git_%E6%9C%8D%E5%8A%A1%E5%99%A8.html>) 中讨论）

本文概述了如何托管 [Git](<../zh-cn/Git.html> "Git") 服务器。有关更多信息，请参阅 Pro Git 书籍的 [Git on the Server 一章](<https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols>)。 

##  协议

请参阅[Git on the Server - The Protocols](<https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols>)，了解详细说明以及优缺点。 

###  普通（General）

[设置 git 服务器 的分步指南](<https://miracoin.wordpress.com/2014/11/25/step-by-step-guide-on-setting-up-git-server-in-arch-linux-pushable/>)设置 git Server 的分步指南描述了如何在 Arch 上设置不安全的服务器。 

默认情况下，git 用户已过期（"您的账户已过期，请联系您的系统管理员"）。使用 [chage](</wzh/index.php?title=Chage&action=edit&redlink=1> "Chage（页面不存在）") 可移除过期条件，举例如下： 
    
    # chage -E -1 git
    
### SSH

您只需要设置一个 [SSH 服务器](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH"). 

您可以进一步确保 SSH 用户账户的安全，只允许在该用户账户上执行推拉命令。方法是用 git-shell 代替默认登录 shell。请参阅[设置服务器](<https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server>)。 

在 Arch 上，使用 [#General](<#General>) 中的说明和本节([#SSH](<#SSH>))中的说明创建 git 服务器时，需要采取以下额外步骤： 

  1. 更改主目录： 为了让 ssh 能够读取 `/srv/git/.ssh/authorized_keys`，需要将 `/etc/passwd` 中 git 的主目录从`/`更改为 `/srv/git`。
  2. home目录更改之时更改基本路径： 如果仓库是从 git 的主目录提供服务的，为了让 git 能够为仓库提供服务，需要将`git-daemon\@.service`中的`--base-path`改为 `/srv/git`。

### Dumb HTTP

这里的 "Dump"是指只有 [WebDAV](<../zh-cn/WebDAV.html> "WebDAV") 参与了拉取和推送。 

#### nginx

Follow the basic WebDAV instructions for nginx. Pushing via WebDAV also requires Locking. Here is an example location block: 
    
    /etc/nginx/nginx.conf
    
    location /repos/ {
            auth_basic "Authorized Personnel Only!";
            auth_basic_user_file /etc/nginx/htpasswd;
            dav_methods PUT DELETE MKCOL COPY MOVE;
            dav_ext_methods PROPFIND OPTIONS LOCK UNLOCK;
            dav_access user:rw group:rw all:r;
            dav_ext_lock zone=general;
            create_full_put_path on;
            client_body_temp_path /tmp;
        }

Note the `dav_ext_lock zone`. Add the specified locking zone to the http section of your config: 
    
    /etc/nginx/nginx.conf
    
    dav_ext_lock_zone zone=general:10m;

Now do the ususal steps when preparing a git repo for the server: 

  * `git clone --bare /path/to/myrepo myrepo.git`
  * copy the bare repo to the server
  * run `git update-server-info` in the bare repo
  * chown the repo to be owned by http:http

You might have noticed that I added HTTP Basic Authentication to have at lease some means of access control. Everyone who has an password entry in the htaccess file can push. 

Now you can clone as usual: 
    
    $ git clone https://www.example.com/repos/myrepo.git
    Cloning into 'myrepo'...
    $
    
Make some changes, add, commit, and push: 
    
    $ git push origin main
    error: Cannot access URL https://www.example.com/repos/myrepo.git/, return code 22
    fatal: git-http-push failed
    error: failed to push some refs to 'https://www.example.com/repos/myrepo.git'
    
Oh noes! For some reason PROPFIND reports 401 Unauthorized and that's all. Nothing in the nginx error logs. Appearently the git client has a problem passing the username and password for all subsequent requests. Running a git credential cache does not help. The only solution that works so far is editing the ~/.netrc (obviously git uses curl for http): 
    
    ~/.netrc
    
    machine www.example.com
    login git
    password topsecret
    
    $  > git push origin main
    Fetching remote heads...
     refs/
     refs/heads/
     refs/tags/
    updating 'refs/heads/main'
     from 03f8860418facfbecedd5e0a81b480131b31bcba
     to   ec5536091e31ebf172a34c6d1ebddfc36e3bd3a6
       sending 3 objects
       done
    Updating remote server info
    To https://www.example.com/repos/myrepo.git
      0318860..ec55560  main -> main
    
Don't even think to specify the clone URL as `https://username:password@www.example.com/repos/myrepo.git`. This works for the initial clone but for a subsequent push you get an error message in your error log stating that the destination URL is handled by a different repository. 

### Smart HTTP

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** There are many [web server](</wzh/index.php?title=Web_server&action=edit&redlink=1> "Web server（页面不存在）")s with CGI support. (在 [Talk:Git 服务器](<../zh-cn/Talk:Git_%E6%9C%8D%E5%8A%A1%E5%99%A8.html>) 中讨论)

The [git-http-backend(1)](<https://man.archlinux.org/man/git-http-backend.1>) is a CGI program, allowing efficient cloning, pulling and pushing over HTTP(S). 

#### Apache

设置非常简单，只需安装[Apache HTTP 服务器](<../zh-cn/Apache_HTTP_%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "Apache HTTP 服务器")，并启用 `mod_cgi`、`mod_alias` 和 `mod_env`，当然还有 [git](<https://archlinux.org/packages/?name=git>)包。 

运行基本设置后，在 Apache 配置文件中添加以下内容，该文件通常位于： 
    
    /etc/httpd/conf/httpd.conf
    
    <Directory "/usr/lib/git-core">
        Require all granted
    </Directory>
     
    SetEnv GIT_PROJECT_ROOT /srv/git
    SetEnv GIT_HTTP_EXPORT_ALL
    ScriptAlias /git/ /usr/lib/git-core/git-http-backend/
    
这假设的是：您的 Git 仓库位于 `/srv/git`，并且您希望通过以下方式访问它们： `http(s)://your_address.tld/git/your_repo.git`。 

**注意：** 确保 Apache 可以读写您的版本库。

有关更详细的文档，请访问以下链接： 

  * <https://git-scm.com/book/en/v2/Git-on-the-Server-Smart-HTTP>
  * <https://git-scm.com/docs/git-http-backend>

### Git

The Git protocol is not encrypted or authenticated, and only allows read access. 

The Git daemon ([git-daemon(1)](<https://man.archlinux.org/man/git-daemon.1>)) can be [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start")ed with `git-daemon.socket`. 

The service uses the `--export-all` and `--base-path` parameters to serve all repositories placed in `/srv/git/`. 

##  访问控制

对于保险（fine-grained）的访问控制，可采用以下解决方案： 

  * **[Gitolite](</wzh/index.php?title=Gitolite&action=edit&redlink=1> "Gitolite（页面不存在）")** — 一个 Git 访问控制层，用 Perl 编写。

     <https://github.com/sitaramc/gitolite> || [gitolite](<https://archlinux.org/packages/?name=gitolite>)包

  * **[Gitosis](</wzh/index.php?title=Gitosis&action=edit&redlink=1> "Gitosis（页面不存在）")** — 一个用于托管 Git 仓库的软件，用 Python 编写。

     <https://github.com/tv42/gitosis> || [gitosis-git](<https://aur.archlinux.org/packages/gitosis-git/>)AUR

请注意，如果您愿意为所有应该访问版本库的人创建[用户账户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户账户")，并且不需要 git 对象（如分支）级别的访问控制，也可以使用标准的[文件权限](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "文件权限")来进行访问控制。[[1]](<https://github.com/sitaramc/gitolite/blob/d74e58b5de8c78bddd29b009ba2d606f7fcb4f2d/doc/overkill.mkd>)

##  Web 界面

###  简易 web 应用程序

  * [Gitweb](<../zh-cn/Gitweb.html> "Gitweb")——Git 自带的默认 Web 界面
  * **[cgit](</wzh/index.php?title=Cgit&action=edit&redlink=1> "Cgit（页面不存在）")** — 一个用纯 C 语言编写的 git 网页界面。

     <https://git.zx2c4.com/cgit/> || [cgit](<https://archlinux.org/packages/?name=cgit>)包

###  高级 web 应用程序

  * **[Forgejo](</wzh/index.php?title=Forgejo&action=edit&redlink=1> "Forgejo（页面不存在）")** — 自托管轻量级软件。Gitea 的社区管理分支。

     <https://forgejo.org> || [forgejo](<https://archlinux.org/packages/?name=forgejo>)包

  * **[Gitea](<../zh-cn/Gitea.html> "Gitea")** — 无偿自托管 Git 服务。它最初是 Gogs 的一个社区管理分支，但在 2022 年由 Gitea Limited 以商业模式拥有。

     <https://gitea.io> || [gitea](<https://archlinux.org/packages/?name=gitea>)包

  * **[GitLab](<../zh-cn/GitLab.html> "GitLab")** — 用 Ruby 编写的项目管理和代码托管应用程序。

     <https://gitlab.com/gitlab-org/gitlab-ce> || [gitlab](<https://archlinux.org/packages/?name=gitlab>)包

  * **[Gogs](</wzh/index.php?title=Gogs&action=edit&redlink=1> "Gogs（页面不存在）")** — 用 Go 编写的自助托管 Git 服务。

     <https://gogs.io> || [gogs](<https://aur.archlinux.org/packages/gogs/>)AUR
