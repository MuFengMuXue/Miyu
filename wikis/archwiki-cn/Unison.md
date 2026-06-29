[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Unison](<../zh-cn/Talk:Unison.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Unison](<https://wiki.archlinux.org/title/Unison> "arch:Unison")，最近一次同步于 2014-07-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Unison?diff=0&oldid=317386>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Unison_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Last updated in 2014（在 [Talk:Unison#](<../zh-cn/Talk:Unison.html>) 中讨论）

**Unison** 是一款可以在类UNIX操作系统(包括 Linux, Mac OS X, 和Solaris) 和Windows 环境下运行的双向文件同步工具。他可以把一个文件或目录的两个备份分别储存在两个不同的主机(或同一个主机的不同的磁盘上)，分别修改，并且通过把双方的改变传递到对方来完成同步。同时，他也不限制哪一方做主机。 

##  安装

请从[official repositories](<../zh-cn/Official_repositories.html> "Official repositories") [安装](<../zh-cn/Pacman.html> "Pacman") [unison](<https://archlinux.org/packages/?name=unison>)包, 那里有提供 CLI, GTK+ 和 GTK+ 2.0 接口. 如果有线下文档需求的话，请从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装 [unison-doc](<https://aur.archlinux.org/packages/unison-doc/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]. 

##  配置

为了使用Unison，你需要创建一份配置文件. 

### GUI

如果想在GUI环境下配置的话 请运行: 
    
    $ unison-gtk2
    
###  手动操作

或者，在`~/.unison`里手动创建配置文件，并且将接下来的几行加入到默认配置文件`~/.unison/_profilename_.prf`里。 

为被同步文件定义根目录 
    
    root=/home/user/
    
定义一个远程目录，文件将被同步到那里 
    
    root=<ssh://example.com//path/to/server/storags>
    
为[SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH")提供参数(可选) 
    
    sshargs=-p 4000
    
定义同步哪些文件和目录: 
    
    # dirs
    path=Documents
    path=Photos
    path=Study
    # files
    path=.bashrc
    path=.vimrc
    
你还可以定义无视哪些文件: 
    
    ignore=Name temp.*
    ignore=Name .*~
    ignore=Name *.tmp
    
**注意：** 如若需要更多咨询请看 [User Manual and Reference Guide](<https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html>)中的 [Sample profiles](<https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html#profileegs>)。

##  使用

设定好配置文件以后就可以开始同步了: 
    
    $ unison _profilename_
    
如果你选择使用GUI工具的话就这么干: 
    
    $ unison-gtk2
    
然后选择配置文件。Unison的界面很赞，你可以看到变动和进度。 

##  版本不兼容性

如果你希望Unison能正常工作的话，请**确保** 每一个客户端上安装的版本都是一样的。举个例子，如果一套电脑上安装了2.40版本而另外一台上安装的是2.32，那他们就没法互相同步了。这对于**所有全部一切** 你希望进行同步作业的计算机都适用。 

由于Linux发行版数目众多，Unison的release错综复杂，所以你很有可能会陷入老版本的泥潭。Arch Linux在上游的Extra repository里提供有最新版本的Unison。同时在 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 有非官方的 2.32版本 ([unison-232](<https://aur.archlinux.org/packages/unison-232/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found])和 2.27版本([unison-227](<https://aur.archlinux.org/packages/unison-227/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]) 的 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")，这样各种发行版的用户们都可以在他们的系统上愉快的使用Unison啦 

##  提醒与小技巧

###  人生苦短，少敲键盘

如果哪位在一个有能力维持一个合适的scrollback buffer的VDT环境下运行Unison的话，他就没有确认每一个无冲突改变的必要了；设定 `auto` 为 true 来避开这些提示。 

###  常规配置文件同步

在同步那些在不同的系统(比如服务器，工作站，笔记本，智能手机)但却含有通用构造(比如键盘映射，基本shell同义名)的配置文件(比如针对本地程序，对安全性敏感的配置)时，最好把这些内容放到分散的配置文件中(比如`.bashrc_common`)并且只对他们进行同步。 

**警告：** 通过让被同步方(甚至也许还包括其他与被同步方同步的机器)的配置文件接受恶意的篡改，配置文件的双向同步可能会打开一条入侵的光明大道。这对于对手来说很有吸引力，尤其是在比如公共shell服务器vs个人工作站这样双方"实力悬殊"的情况下，因为要瓦解一个安全等级更低的系统看起来真不是什么难事。你并不需要在两台特定的机器间进行双向同步时一直使用`noupdate`；如果真的有这个必要，请在同步时确认每一处变动。在对待自动的双向同步行为的时候,当心点。

##  参阅

  * [Unison (file synchronizer)](</wzh/index.php?title=Wikipedia&action=edit&redlink=1> "Wikipedia（页面不存在）")
  * [Official website](<https://www.cis.upenn.edu/~bcpierce/unison/>)
  * [Yahoo! user group](<http://tech.groups.yahoo.com/group/unison-users>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ]
  * _[Liberation through data replication](<https://web.archive.org/web/20200509182622/http://www.pgbovine.net/unison_guide.htm>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ]_ by Philip Guo
  * _[Setting up Unison for your mom](<http://www.pgbovine.net/unison-for-your-mom.htm>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-19 ⓘ]_ by Philip Guo
  * _[Replication using Unison](<https://twiki.org/cgi-bin/view/Codev/ReplicationUsingUnison>)_ on TWiki
