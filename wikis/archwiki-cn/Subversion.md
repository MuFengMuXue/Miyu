**翻译状态：**

  * 本文（或部分内容）译自 [Subversion](<https://wiki.archlinux.org/title/Subversion> "arch:Subversion")，最近一次同步于 2023-02-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/Subversion?diff=0&oldid=765372>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Subversion_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

_"[Apache Subversion](<https://subversion.apache.org/features.html>) 是一套功能全面的版本控制系统，最初被设计为[CVS](</wzh/index.php?title=CVS&action=edit&redlink=1> "CVS（页面不存在）")的改进版本。其后Subversion的发展大大超出了取代CVS的原始目标，但它的基本模型、设计和接口仍然受到了这一目标的深刻影响。"_

本文主要介绍架设svn服务器的方法。有两种流行的svn服务器，内建的`svnserve`以及更高级的选择——结合了svn插件的[Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server")。 

##  用于Subversion安装的Apache服务器

###  目标

这篇指南的目标是结合Apache安装Subversion。选用Apache是因为其提供了单机`svnserve`不具备的诸多特性。 

  * 支持 HTTPS，比 svnserve 使用的 md5 认证更加安全。
  * 细粒度的控制权。可以使用 Apache 的认证限制目录的访问权限。可以允许所有文件可读，但仅允许提交 trunk，同时对另一组用户赋予提交 tags 和 branches 的权限。
  * 一个自由的源码库查看器
  * Subversion 团队正在进行无缝 webdav 集成的工作。不久你就能用任何 webdav 接口更新源码库中的文件。

###  安装

安装 [Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server")。除了 apache 之外，还需要安装 [subversion](<https://archlinux.org/packages/?name=subversion>)包。 

###  配置 Subversion

####  创建一个目录
    
    # mkdir -p /home/svn/repositories
    
####  编辑 httpd.conf

请确认下列模块加载指令在文件中列出。如果没有请添加它们(通常你只需要添加后两行)，保持先后顺序： 
    
    /etc/httpd/conf/httpd.conf
    
    LoadModule dav_module           modules/mod_dav.so
     LoadModule dav_fs_module        modules/mod_dav_fs.so
     LoadModule dav_svn_module       modules/mod_dav_svn.so
     LoadModule authz_svn_module     modules/mod_authz_svn.so

####  用不用SSL？

SSL允许用户使用Apache的AuthType Basic而不必担心有人嗅探密码。 

生成证书： 
    
    # cd /etc/httpd/conf/
    # openssl req -new -x509 -keyout server.key -out server.crt -days 365 -nodes
    
然后添加下面的配置到`/etc/httpd/conf/extra/httpd-ssl.conf`，以便在虚拟主机配置指令中包含它们。 
    
    <Location /svn>
       DAV svn
       SVNParentPath /home/svn/repositories
       AuthzSVNAccessFile /home/svn/.svn-policy-file
       AuthName "SVN Repositories"
       AuthType Basic
       AuthUserFile /home/svn/.svn-auth-file
       Satisfy Any
       Require valid-user
    </Location>
    
为了确保SSL设置已加载，取消`/etc/httpd/conf/httpd.conf`中SSL配置行的注释： 
    
    Include /etc/httpd/conf/extra/httpd-ssl.conf
    LoadModule ssl_module modules/mod_ssl.so	
    LoadModule socache_shmcb_module modules/mod_socache_shmcb.so
    
####  创建/home/svn/.svn-policy-file
    
    [/]
    * = r
    
    [REPO_NAME:/]
    USER_NAME = rw
    
/部分中的*用来匹配匿名用户。对除只读以外的任何访问Apache AuthType Basic都会提示输入用户名和密码。REPO_NAME:/一节继承了之前的权限设置，于是匿名用户对其有只读权限。最后一项设置为用户USER_NAME授予来REPO_NAME源码库的读写权限。 

####  创建/home/svn/.svn-auth-file

这个文件可以用htpasswd或htdigest创建。这里使用了htpasswd。同样，因为SSL，不用过多担心密码嗅探。htdigest甚至会对嗅探提供更好的安全特性。 
    
    # htpasswd -cs /home/svn/.svn-auth-file USER_NAME
    
以上创建了文件(-c)并使用SHA1保存密码(-s)用户USER_NAME被创建。要添加其他用户，可以去掉 -c 选项： 
    
    # htpasswd -s /home/svn/.svn-auth-file OTHER_USER_NAME
    
####  创建源码库
    
    # svnadmin create /home/svn/repositories/REPO_NAME
    
####  设置权限

对Apache用户设置新源码库的权限： 
    
    # chown -R http.http /home/svn/repositories/REPO_NAME
    
###  创建项目

####  项目的目录结构

创建 `branches` `tags` `trunk` 临时目录结构： 
    
    $ cd /path/to/directory _of_ choice
    $ mkdir -p ~/svn-import/{branches,tags,trunk}
    
####  将源码添加到目录

将源代码文件放入创建的 trunk 目录： 
    
    $ cp -R /my/existing/project/* ~/svn-import/trunk
    
####  导入项目
    
    $ svn import -m "Initial import" ~/svn-import <https://yourdomain.net/svn/REPO_NAME/>
    
####  测试SVN检出
    
    $ svn checkout <https://yourdomain.net/svn/REPO_NAME/> /my/svn/working/copy
    
如果以上所有配置都成功，你应该能得到一个受版本控制的新源码库的副本。 

##  设置 Svnserve

###  安装软件包

安装 [subversion](<https://archlinux.org/packages/?name=subversion>)包。 

###  创建源码库

创建你的源码库 
    
    mkdir /path/to/repos/
    svnadmin create /path/to/repos/repo1
    
初始源码库是空的，如果想导入文件，使用以下命令： 
    
    svn import ~/code/project1 file:///path/to/repos/repo1 --message 'Initial repository layout'
    
###  设置访问策略

编辑文件/path/to/repos/repo1/conf/svnserve.conf，在[general]中取消以下行的注释或者添加之： 
    
    password-db = passwd
    
你也许想改变对匿名用户的默认设置 
    
    anon-access = read
    
对允许任何人提交的源码库，替换"read"为"write"，或者将其改为"none"来禁止所有匿名访问。 

编辑文件/path/to/repos/repo1/conf/passwd 
    
    [users]
    harry = foopassword
    sally = barpassword
    
以上定义了用户harry和sally，分别使用密码foopassword和barpassword，可以按需修改。 

###  启动服务器守护进程

在启动服务器之前，编辑配置文件 
    
    /etc/conf.d/svnserve
    
    SVNSERVE_ARGS="--root=/path/to/repos"

The `--root=/path/to/repos` option set the root of repository tree. If you have multiple repositories use `--root=/path-to/reposparent`. Then access independent repositories by passing in repository name in the URL: `<svn://host/repo1>`. make sure that the user has read/write access to the repository files) 

Optionally add a `--listen-port` if you want a different port, or other options. 

By default, the service runs as root. If you want to change that, add a drop-in: 
    
    /etc/systemd/system/svnserve.service.d/50-custom.conf
    
    [Service]
    User=svn

Now start the _svnserve.service_ [daemon](<../zh-cn/Systemd.html> "Daemon"). 

###  svn+ssh

To use svn+ssh://, we have to have a wrapper written for svnserve. 

check where the svnserve binary is located: 
    
    # which svnserve
    
    /usr/local/bin/svnserve
    
Our wrapper is going to have to fall in PATH prior to this location... 

[Create](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Create") a wrapper with the following content: 
    
    /usr/bin/svnserve
    
    #!/bin/sh
    # wrapper script for svnserve
    umask 007
    /usr/local/bin/svnserve -r /path/to "$@"
    
Then, make it [executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable"). 

`-r /path/to` is what makes use of the svn co svn+<ssh://server.domain.com:/reponame> instead of `:/path/to/reponame`. 

Start svnserve with new wrapper script like so: 
    
    # /usr/bin/svnserve -d  ( start daemon mode )
    
we can also check the perms for remote users like this: 
    
    $ svn ls svn+ssh://server.domain.com:/reponame
    
    ++server.domain.com++
    dev/
    qa/
    release/
    
## Subversion backup and restore

To back up your subversion repositories, do this for each repository you have. 
    
    $ svnadmin dump /path/to/_repo_ > /tmp/_repo_.dump
    
To restore the backup, create the corresponding repositories first: 
    
    $ svnadmin create /path/to/_repo_
    
Then load svn dump into new repo: 
    
    $ svnadmin load /path/to/_repo_ < /tmp/_repo_.dump
    
Setting permissions: 
    
    $ chown -R svn:svnusers /path/to/_repo_
    $ chmod -R g+w /path/to/_repo_ /db/
    
These repositories should now be all setup. 

## Subversion clients

See also [Wikipedia:Comparison of Subversion clients](<https://en.wikipedia.org/wiki/Comparison_of_Subversion_clients> "wikipedia:Comparison of Subversion clients"). 

  * **kdesvn** — Subversion client for KDE.

     <https://invent.kde.org/sdk/kdesvn> || [kdesvn](<https://archlinux.org/packages/?name=kdesvn>)包

  * **[RabbitVCS](<https://en.wikipedia.org/wiki/RabbitVCS> "wikipedia:RabbitVCS")** — Set of graphical tools written to provide simple and straightforward access to the version control systems you use.

     <http://rabbitvcs.org/> || [rabbitvcs](<https://aur.archlinux.org/packages/rabbitvcs/>)AUR

  * **[RapidSVN](<https://en.wikipedia.org/wiki/RapidSVN> "wikipedia:RapidSVN")** — GUI front-end for the Subversion revision system written in C++ using the wxWidgets framework.

     <http://rapidsvn.tigris.org/> || [rapidsvn](<https://aur.archlinux.org/packages/rapidsvn/>)AUR

## See also

  * <https://svnbook.red-bean.com/en/1.1/svn-book.html#svn-ch-9-sect-2.2-re-load>
  * <https://subversion.apache.org/>
