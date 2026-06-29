**翻译状态：**

  * 本文（或部分内容）译自 [Trac](<https://wiki.archlinux.org/title/Trac> "arch:Trac")，最近一次同步于 2020-04-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Trac?diff=0&oldid=608081>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Trac_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

从[项目网页](<https://trac.edgewall.org>): 

    Trac is an enhanced wiki and issue tracking system for software development projects. Trac uses a minimalistic approach to web-based software project management. Our mission is to help developers write great software while staying out of the way. Trac should impose as little as possible on a team's established development process and policies.

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [trac](<https://aur.archlinux.org/packages/trac/>)AUR 包。配置是基于每个环境进行的。请参阅下文，了解如何创建环境。有关详细说明，请访问 <https://trac.edgewall.org/wiki/TracGuide> 。 

##  快速入门

###  创建和初始化环境

初始化环境 
    
    # cd /srv/;
    # mkdir tracenv;
    # trac-admin /srv/tracenv initenv;
    
环境配置可以在 `/srv/tracenv/conf/trac.ini` 找到。 

###  配置 systemd 服务文件

默认服务文件位于 `/usr/lib/systemd/system/tracd.service`。将此文件复制到 `/etc/systemd/system/tracd.service`，然后编辑它以指向您的新环境。该 `ExecStart` 条目应如下所示： 
    
    ExecStart=/usr/bin/tracd -b localhost -p 8080 /srv/tracenv
    
###  查看 Web 服务器

之后[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")（并可选地[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")）服务（或直接运行 `/usr/bin/tracd`））之后，可以使用 Web 浏览器在 `<http://localhost:8080>` 上查看 Web 界面。 

##  后续步骤

###  Trac 用户

专门为 trac 服务创建[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户")是一个好主意。创建该用户后，您可以使用该用户创建环境： 
    
    # cd /srv/;
    # mkdir tracenv;
    # chown trac:trac tracenv;
    # sudo -u trac trac-admin /srv/tracenv initenv;
    
将以下内容添加到 systemd Unit 文件中，以确保它以 `trac` 用户身份启动： 
    
    [Service]
    User=trac
    Group=trac
    
###  Trac中的用户和权限

（本节涉及在 trac 环境中创建用户，而不是 GNU/Linux 用户。） 

接下来，您将要添加用户并向这些用户授予权限。要添加用户，请参阅 <https://trac.edgewall.org/wiki/TracStandalone#UsingAuthentication> （您必须更改 `.service` 文件以引用您选择的身份验证机制）。要向用户授予权限，请在 trac 服务器上运行以下命令： 
    
    # trac-admin /srv/tracenv permission add <username> TRAC_ADMIN
    