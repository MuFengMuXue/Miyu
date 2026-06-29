**翻译状态：**

  * 本文（或部分内容）译自 [Git](<https://wiki.archlinux.org/title/Git> "arch:Git")，最近一次同步于 2025-07-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Git?diff=0&oldid=841424>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Git_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Bisecting bugs with Git](</wzh/index.php?title=Bisecting_bugs_with_Git&action=edit&redlink=1> "Bisecting bugs with Git（页面不存在）")
  * [Concurrent Versions System](</wzh/index.php?title=Concurrent_Versions_System&action=edit&redlink=1> "Concurrent Versions System（页面不存在）")
  * [Git 服务器](<../zh-cn/Git_%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "Git 服务器")
  * [Gitweb](<../zh-cn/Gitweb.html> "Gitweb")
  * [HTTP tunneling#Tunneling Git](</wzh/index.php?title=HTTP_tunneling&action=edit&redlink=1> "HTTP tunneling（页面不存在）")
  * [Subversion](<../zh-cn/Subversion.html> "Subversion")
  * [VCS 软件打包准则](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则")

    "我遇到过一些人，他们认为 Git 是 GitHub 的前端。他们错了，Git 其实是 AUR 的前端。"—— [Linus Torvalds](<https://public-inbox.org/git/#didyoureallythinklinuswouldsaythat>)

[Git](<https://zh.wikipedia.org/wiki/Git> "zhwp:Git") 是由 Linux 内核作者 Linus Torvalds 设计并开发的版本控制系统（VCS），现在被用来维护 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 软件包以及数以千计的其他项目，其中包括 Linux 内核。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [git](<https://archlinux.org/packages/?name=git>)包 软件包。要使用开发版本，请安装 [git-git](<https://aur.archlinux.org/packages/git-git/>)AUR 软件包。当使用 _git svn_ 、 _git gui_ 和 _gitk_ 等工具时请检查可选依赖项是否安装。 

###  图形化前端

参考 [git GUI Clients](<https://git-scm.com/download/gui/linux>)。 

  * **Commit** — 帮助编写更好的 Git 和 Mercurial 提交消息的编辑器。

     <https://apps.gnome.org/Commit/> || [commit](<https://archlinux.org/packages/?name=commit>)包

  * **Forge Sparks** — 支持 Github、GitLab、Gitea 和 Forgejo 的简单通知应用。

     <https://apps.gnome.org/ForgeSparks/> || [forge-sparks](<https://archlinux.org/packages/?name=forge-sparks>)包

  * **Giggle** — 用于 git 的 GTK+ 前端。

     <https://wiki.gnome.org/Apps/giggle/> || [giggle](<https://archlinux.org/packages/?name=giggle>)包

  * **GitAhead** — 一个包含内置合并工具的 git 前端。

     <https://gitahead.github.io/gitahead.com/> || [gitahead](<https://aur.archlinux.org/packages/gitahead/>)AUR

  * **GitButler** — 基于 Git 的版本控制客户端，使用 Tauri/Rust/Svelte 构建。

     <https://gitbutler.com/> || [gitbutler](<https://aur.archlinux.org/packages/gitbutler/>)AUR

  * **Git Cola** — 用 Python 编写的丝滑而强大的 git 图形前端。

     <https://git-cola.github.io/> || [git-cola](<https://aur.archlinux.org/packages/git-cola/>)AUR

  * **Git Extensions** — 允许用户不使用命令行就可以完成 git 各项操作的图形前端。

     <https://gitextensions.github.io/> || [gitextensions](<https://aur.archlinux.org/packages/gitextensions/>)AUR

  * **gitg** — 用于查看 git 仓库的 GNOME GUI 客户端。

     <https://wiki.gnome.org/Apps/Gitg> || [gitg](<https://archlinux.org/packages/?name=gitg>)包

  * **git-gui** — Tcl/Tk 库编写的可移植 git 图形前端。

     <https://git-scm.com/docs/git-gui> || [git](<https://archlinux.org/packages/?name=git>)包 \+ [tk](<https://archlinux.org/packages/?name=tk>)包
    
**注意：** 要打开 _git-gui_ 的拼写检查功能，请安装 [aspell](<https://archlinux.org/packages/?name=aspell>)包，同时还需要与 `LC_MESSAGES` [环境变量](<../zh-cn/Environment_variables.html> "Environment variables") 相对应的字典文件。参阅 [FS#28181](<https://bugs.archlinux.org/task/28181>) 和 [aspell](<../zh-cn/%E8%AF%AD%E8%A8%80%E6%A3%80%E6%9F%A5.html> "Aspell")。

  * **GitHub Desktop** — 由 GitHub 开发的一个基于 Electron 的 GitHub 客户端。

     <https://github.com/desktop/desktop> || [github-desktop](<https://aur.archlinux.org/packages/github-desktop/>)AUR [github-desktop-bin](<https://aur.archlinux.org/packages/github-desktop-bin/>)AUR

  * **gitk** — Tcl/Tk 库编写的 Git 仓库查看器。

     <https://git-scm.com/docs/gitk> || [git](<https://archlinux.org/packages/?name=git>)包 \+ [tk](<https://archlinux.org/packages/?name=tk>)包

  * **Gittyup** — 基于 Qt 的 Git 客户端。

     <https://github.com/Murmele/Gttyup> || [gittyup](<https://aur.archlinux.org/packages/gittyup/>)AUR

  * **Guitar** — 一个 Git 的图形化前端。

     <https://github.com/soramimi/Guitar> || [guitar](<https://aur.archlinux.org/packages/guitar/>)AUR

  * **gitui** — 用 Rust 编写的快速的 Git 终端用户界面。

     <https://github.com/extrawurst/gitui> || [gitui](<https://archlinux.org/packages/?name=gitui>)包

  * **Kommit** — KDE 的 Git GUI 客户端。

     <https://apps.kde.org/kommit/> || [kommit](<https://archlinux.org/packages/?name=kommit>)包

  * **lazygit** — 一个简洁的 Git TUI 工具。

     <https://github.com/jesseduffield/lazygit> || [lazygit](<https://archlinux.org/packages/?name=lazygit>)包

  * **QGit** — 可图形化地按照不同开发分支显示修订历史记录、查阅补丁内容、查看被修改文件的 Git GUI 查看器。

     <https://github.com/tibirna/qgit> || [qgit](<https://archlinux.org/packages/?name=qgit>)包

  * **[RabbitVCS](<https://en.wikipedia.org/wiki/RabbitVCS> "wikipedia:RabbitVCS")** — 一组图形化工具，用于轻松、直接地访问您使用的版本控制系统。

     <http://rabbitvcs.org/> || [rabbitvcs](<https://aur.archlinux.org/packages/rabbitvcs/>)AUR

  * **Sublime Merge** — 由 Sublime Text 开发商开发的 Git 前端。

     <https://www.sublimemerge.com/> || [sublime-merge](<https://aur.archlinux.org/packages/sublime-merge/>)AUR

  * **Tig** — 基于 ncurses 的 git 字符模式前端。

     <https://jonas.github.io/tig/> || [tig](<https://archlinux.org/packages/?name=tig>)包

  * **ungit** — 在不牺牲 git 各种功能的情况下使其变得更加友好。

     <https://github.com/FredrikNoren/ungit> || [nodejs-ungit](<https://aur.archlinux.org/packages/nodejs-ungit/>)AUR

##  配置

你至少需要设置好姓名和邮箱之后才能开始使用 Git： 
    
    $ git config --global user.name  "_John Doe_ "
    $ git config --global user.email "_johndoe@example.com_ "
    
参阅[起步 - 初次运行 Git 前的配置](<https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%88%9D%E6%AC%A1%E8%BF%90%E8%A1%8C-Git-%E5%89%8D%E7%9A%84%E9%85%8D%E7%BD%AE>)。 

更多设置选项可参阅[#提示与技巧](<#%E6%8F%90%E7%A4%BA%E4%B8%8E%E6%8A%80%E5%B7%A7>)。 

##  基本用法

一个 Git 版本库包含在一个名为 `.git` 的目录内，该目录包含了修订历史以及其他元数据。版本库所跟踪的目录（默认为父目录）称为工作目录。在工作树进行的更改在被提交 (commit) 前需要先暂存 (stage) 起来。Git 还可以让你恢复以前提交的工作树文件。 

参见[起步](<https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%85%B3%E4%BA%8E%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6>)。 

###  获取 Git 仓库

参见[获取 Git 仓库 - Git 基础](<https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E8%8E%B7%E5%8F%96-Git-%E4%BB%93%E5%BA%93>)

###  记录更改

参见[记录每次更新到仓库 - Git 基础](<https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E8%AE%B0%E5%BD%95%E6%AF%8F%E6%AC%A1%E6%9B%B4%E6%96%B0%E5%88%B0%E4%BB%93%E5%BA%93>)

###  查看提交记录

参见[查看提交历史 - Git 基础](<https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E6%9F%A5%E7%9C%8B%E6%8F%90%E4%BA%A4%E5%8E%86%E5%8F%B2>)

###  撤销修改

参见[撤消操作 - Git 基础](<https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E6%92%A4%E6%B6%88%E6%93%8D%E4%BD%9C>)

###  远程操作

参见[远程仓库的使用 - Git 基础](<https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E8%BF%9C%E7%A8%8B%E5%BA%93%E7%9A%84%E4%BD%BF%E7%94%A8>)

###  分支 (branch)

参见[分支简介 - Git 分支](<https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%AE%80%E4%BB%8B>)

####  分支与合并基础

参见[分支的新建与合并 - Git 分支](<https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E6%96%B0%E5%BB%BA%E4%B8%8E%E5%90%88%E5%B9%B6>)

####  分支管理

参见[分支管理 - Git 分支](<https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%AE%A1%E7%90%86>)

####  分支开发工作流

参见[分支开发工作流 - Git 分支](<https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E5%BC%80%E5%8F%91%E5%B7%A5%E4%BD%9C%E6%B5%81>)

####  远程分支

参见[远程分支 - Git 分支](<https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E8%BF%9C%E7%A8%8B%E5%88%86%E6%94%AF>)

####  变基

参见[变基 - Git 分支](<https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%8F%98%E5%9F%BA>)

###  多人合作

####  分布式工作流

参见[分布式工作流程 - 分布式 Git](<https://git-scm.com/book/zh/v2/%E5%88%86%E5%B8%83%E5%BC%8F-Git-%E5%88%86%E5%B8%83%E5%BC%8F%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B>)

####  为已有项目贡献

参见[向一个项目贡献 - 分布式 Git](<https://git-scm.com/book/zh/v2/%E5%88%86%E5%B8%83%E5%BC%8F-Git-%E5%90%91%E4%B8%80%E4%B8%AA%E9%A1%B9%E7%9B%AE%E8%B4%A1%E7%8C%AE>)

####  维护自己的项目

参见[维护项目 - 分布式 Git](<https://git-scm.com/book/zh/v2/%E5%88%86%E5%B8%83%E5%BC%8F-Git-%E7%BB%B4%E6%8A%A4%E9%A1%B9%E7%9B%AE>)

###  Git 工具

####  选择修订版本

参见[选择修订版本 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%80%89%E6%8B%A9%E4%BF%AE%E8%AE%A2%E7%89%88%E6%9C%AC>)

####  交互式暂存

参见[交互式暂存 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E4%BA%A4%E4%BA%92%E5%BC%8F%E6%9A%82%E5%AD%98>)

####  贮藏与清理

参见[贮藏与清理 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E8%B4%AE%E8%97%8F%E4%B8%8E%E6%B8%85%E7%90%86>)

####  签署工作

参见[签署工作 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E7%AD%BE%E7%BD%B2%E5%B7%A5%E4%BD%9C>)

####  搜索

参见[搜索 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E6%90%9C%E7%B4%A2>)

####  重写历史

参见[重写历史 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E5%86%99%E5%8E%86%E5%8F%B2>)

####  重置揭密

参见[重置揭密 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E7%BD%AE%E6%8F%AD%E5%AF%86>)

####  高级合并

参见[高级合并 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%AB%98%E7%BA%A7%E5%90%88%E5%B9%B6>)

#### Rerere

参见[Rerere - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-Rerere>)

####  使用 Git 调试

参见[使用 Git 调试 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E4%BD%BF%E7%94%A8-Git-%E8%B0%83%E8%AF%95>)

####  子模块

参见[子模块 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97>)

####  打包

参见[打包 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E6%89%93%E5%8C%85>)

####  替换

参见[替换 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E6%9B%BF%E6%8D%A2>)

####  凭证存储

参见[凭证存储 - Git 工具](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%87%AD%E8%AF%81%E5%AD%98%E5%82%A8>)

##  提示与技巧

###  使用 git-config

Git 从 4 个 ini 类型的配置文件里读取配置： 

  * `/etc/gitconfig` 是应用于整个系统的默认配置文件
  * `~/.gitconfig` 和 `~/.config/git/config` （自 1.7.12 起）是应用于特定用户的配置文件
  * `.git/config` 是应用于特定仓库的配置文件

这些文件可以直接编辑，但是更常用的方法是使用 _git config_ ，下面是一些示范。 

列出当前已配置的变量： 
    
    $ git config list {--local,--global,--system}
    
将默认文本编辑器从 [vim](<../zh-cn/Vim.html> "Vim") 改成 [nano](<../zh-cn/Nano.html> "Nano")： 
    
    $ git config --global core.editor "nano -w"
    
设置默认的推送 (push) 行为： 
    
    $ git config --global push.default simple
    
设置不同的 _git difftool_ 工具（默认是 _meld_ ）： 
    
    $ git config --global diff.tool vimdiff
    
更多信息请参阅 [git-config(1)](<https://man.archlinux.org/man/git-config.1>) 和[配置 Git](<https://git-scm.com/book/zh/v2/%E8%87%AA%E5%AE%9A%E4%B9%89-Git-%E9%85%8D%E7%BD%AE-Git>)。 

####  包含单独的配置文件

自 [2012 年的 v1.7.10 版本](<https://github.com/gitster/git/commit/9b25a0b52e09400719366f0a33d0d0da98bbf7b0>)起，Git 能够使用 `include` 关键字在 `gitconfig` 文件中构建分割成多个配置文件的配置。 

**提示：** 当使用 `--local` 或 `--global` 标志时，默认禁用加载包含的配置文件。要启用它，请将 `--includes` 标志与 `git config get` 和 `git config list` 命令一起使用。

###  保持良好的礼仪

  * 当你想为一个现有的项目贡献时，请先阅读并理解这个项目的许可，因为它可能会过度限制你更改代码的权力。有些许可会在代码的所有权方面引起争议。
  * 理解这个项目的社区，以及你可以融入其中的程度。要了解项目的主要方向，可以阅读所有文档甚至是代码库的 [log](<#%E5%8E%86%E5%8F%B2%E8%AE%B0%E5%BD%95%E5%92%8C%E7%89%88%E6%9C%AC%E8%AE%B0%E5%BD%95>)。
  * 当发起一个合并请求，或者提交一个补丁时，保证它是小改动并且有完善的文档；这将有助于项目维护者理解你的改动，并决定是否合并这些改动或是让你再改一下。
  * 如果贡献被拒绝，不要气馁，毕竟这是他们的项目。如果它很重要，请尽可能清楚和耐心地讨论这次贡献的理由，最终可能通过这种方法解决问题。

###  加快身份验证

每次向 Git 服务器推送时都要认证身份，你可能会想要避免这种麻烦。 

  * 如果你是用 SSH 密钥来认证的，请使用 [SSH agents](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html#SSH_agents> "SSH 密钥")。参阅 [OpenSSH#Speeding up SSH](<../zh-cn/OpenSSH.html#Speeding_up_SSH> "OpenSSH") 和 [OpenSSH#保活](<../zh-cn/OpenSSH.html#%E4%BF%9D%E6%B4%BB> "OpenSSH")。
  * 如果你是用账号和密码来认证的，在服务器支持 SSH 的情况下请切换至 [SSH 密钥](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html> "SSH 密钥")，否则请尝试 [git-credential-cache](<https://git-scm.com/docs/git-credential-cache>) 或 [git-credential-store](<https://git-scm.com/docs/git-credential-store>)。

###  使用 git-credential-libsecret 作为凭证帮助程序

Git 可能会从 [org.freedesktop.secrets](<https://archlinux.org/packages/?q=org.freedesktop.secrets>) 兼容密钥环（如 [GNOME Keyring](<../zh-cn/GNOME_Keyring.html> "GNOME Keyring")、[KeePassXC](</wzh/index.php?title=KeePass&action=edit&redlink=1> "KeePass（页面不存在）")（英语：[KeePass#Secret Service](<https://wiki.archlinux.org/title/KeePass#Secret_Service> "en:KeePass")） 或 [KDE Wallet](<../zh-cn/KDE_Wallet.html> "KDE Wallet")）获取您的凭据。因此，设置一个兼容的密钥环，并使用以下命令检查密钥环是否已注册到 dbus： 
    
    $ dbus-send --session --print-reply --dest=org.freedesktop.DBus / \
        org.freedesktop.DBus.GetConnectionUnixProcessID \
        string:org.freedesktop.secrets
    
然后运行 
    
    $ git config --global credential.helper /usr/lib/git-core/git-credential-libsecret
    
设置 git。 

###  使用 git-credential-netrc 作为凭证帮助程序

Git 可以读取 [netrc](<https://www.gnu.org/software/inetutils/manual/html_node/The-_002enetrc-file.html>) 文件来访问凭据。首先，将 Git 指向 netrc 帮助程序脚本： 
    
    $ git config --global credential.helper /usr/share/git/credential/netrc/git-credential-netrc.perl
    
然后，[创建](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建") `.netrc` 文件： 
    
    ~/.netrc
    
    machine git-host
    login username
    password password
    
如果您想保护您的机密安全，凭证帮助程序还支持 [gpg](<../zh-cn/GnuPG.html> "GnuPG") 加密文件 (`~/.netrc.gpg`)。 

###  默认通讯协议

如果你正在使用一个上述那种复用的 SSH 连接，让 Git 使用 SSH 可能比使用 HTTPS 更快。同时，一些服务器（比如 AUR）只允许通过 SSH 推送更改。例如，像下面这样配置可以使得 Git 通过 SSH 访问 AUR 上的任何仓库。 
    
    ~/.gitconfig
    
    [url "ssh://aur@aur.archlinux.org/"]
    	insteadOf = https://aur.archlinux.org/
    	insteadOf = http://aur.archlinux.org/
    	insteadOf = git://aur.archlinux.org/
    
###  Bash 自动补全

要启用 Bash 的自动补全，请在 [Bash 启动文件](<../zh-cn/Bash.html#Configuration_files> "Bash")里用 source 加载 `/usr/share/git/completion/git-completion.bash` 文件。或者也可以安装 [bash-completion](<https://archlinux.org/packages/?name=bash-completion>)包。 

###  Git 提示符

Git 包带有一个提示符脚本。要启用它，请用 source 加载 `/usr/share/git/completion/git-prompt.sh` 脚本，然后使用 `%s` 参数设置一个自定义 shell 提示符： 

  * [Bash](<../zh-cn/Bash.html> "Bash") 用户： `PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ '`
  * [Zsh](<../zh-cn/Zsh.html> "Zsh") 用户： `setopt PROMPT_SUBST ; PS1='[%n@%m %c$(__git_ps1 " (%s)")]\$ '`

**提示：** Zsh 提供了 `vcs_info` 函数作为替代方案。参见 [zshcontrib(1) § GATHERING INFORMATION FROM VERSION CONTROL SYSTEMS](<https://man.archlinux.org/man/zshcontrib.1#GATHERING_INFORMATION_FROM_VERSION_CONTROL_SYSTEMS>)。

注意命令替换必须被转义，详情见 [Bash/Prompt customization#Embedding commands](</wzh/index.php?title=Bash/Prompt_customization&action=edit&redlink=1> "Bash/Prompt customization（页面不存在）")。持久化配置见[命令行解释器#配置文件](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6> "命令行解释器")。 

当切换至一个 Git 仓库所在目录时，shell 提示符会变成所在分支名称。也可以配置提示符来显示其他信息： 

Shell 变量 | 信息   
---|---  
GIT_PS1_SHOWDIRTYSTATE | 已暂存 (staged) 显示 `+`，未暂存 (unstaged) 显示 `*`。   
GIT_PS1_SHOWSTASHSTATE | 已储藏 (stashed) 显示 `$`。   
GIT_PS1_SHOWUNTRACKEDFILES | 有未跟踪文件时显示 `%`。   
GIT_PS1_SHOWUPSTREAM |  `<`, `>`, `<>` 分别表示落后、领先或偏离上游。   
GIT_PS1_STATESEPARATOR | 分支名称和状态符号之间的分隔符   
GIT_PS1_DESCRIBE_STYLE | 分离 HEAD 时，相对于标签/分支显示提交   
GIT_PS1_SHOWCOLORHINTS | 显示颜色   
  
环境变量的完整文档可在脚本的注释中找到。 

**注意：**

  * 如果发生了 `$(__git_ps1)` 返回 `((unknown))` 的情况，是因为有一个 `.git` 文件夹在你当前的文件夹里面，但却不包含任何存储库，因此 Git 不认识它。例如，将 Git 在`~/.gitconfig` 的配置文件误认为在 `~/.git/config` 就会发生这种情况。
  * 如果提示符在遇到非常大的存储库时延迟，很可能是由于 `GIT_PS1_SHOWUNTRACKEDFILES` 选项，该选项每次都会触发完整的目录树扫描以检测新文件，从而导致明显的性能影响。要为这些存储库本地禁用此选项，您可以使用命令 `git config --local bash.showUntrackedFiles false`。

你也可以使用来自 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 的自定义 git shell 提示符软件包，例如 [bash-git-prompt](<https://aur.archlinux.org/packages/bash-git-prompt/>)AUR 或 [gittify](<https://aur.archlinux.org/packages/gittify/>)AUR。 

###  可视化显示

要了解已经完成了多少工作： 
    
    $ git diff --stat
    
带有 fork 显示的 _git log_ ： 
    
    $ git log --graph --oneline --decorate
    
给图形化的 _git log_ 做一个别名（使用 _git graph_ 即可显示经过修饰的 log）： 
    
    $ git config --global alias.graph 'log --graph --oneline --decorate'
    
###  关于提交 (commit) 的小提示

重置为以前的提交（非常危险，这会擦除所有跟踪文件到指定提交）： 
    
    $ git reset --hard HEAD~
    
如果远程仓库的地址发生变化，可以这样更新它的位置： 
    
    $ git remote set-url origin git@_address_ :_user_ /_repo_.git
    
自动附加签名行到提交（将某个 姓名-电邮 签名添加到提交中，某些项目会要求这样做）： 
    
    $ git commit -s
    
自动附加签名到补丁（使用 `git format-patch _commit_` 时生效）： 
    
    $ git config --local format.signoff true
    
提交已更改文件的特定部分。如果有大量更改时，最好拆分成多个提交，这种情况下这个命令通常很有用： 
    
    $ git add -p
    
###  对提交 (commit) 签名

Git 允许使用 [GnuPG](<../zh-cn/GnuPG.html> "GnuPG") 对提交和标签进行签名，请参见[签署工作](<https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E7%AD%BE%E7%BD%B2%E5%B7%A5%E4%BD%9C>)。 

**注意：** 如果是借助 [pinentry](<https://archlinux.org/packages/?name=pinentry>)包 来进行 GPG 签名，请确保 `export GPG_TTY=$(tty)`（或者使用 pinentry-tty），否则当 GPG 处于锁定状态时签名这一步会失败（因为它无法在 shell 提示符里询问 pin 码）。

配置 Git 使它自动对提交进行签名： 
    
    $ git config --global commit.gpgSign true
    
###  在非主分支上工作

偶尔项目维护人员会要求你在其他分支上完成工作。这些分支通常被称为 `devel` 或 `testing`。首先要克隆存储库。 

要进入不是主分支的分支（ _git clone_ 只会显示主分支，但其他分支其实也是存在的，用 `git branch -a` 可以显示出来）： 
    
    $ git checkout -b _branch_ origin/_branch_
    
然后就可以像平常一样编辑文件，但是要使得整个仓库都保持同步，下面这两个命令都要用： 
    
    $ git pull --all
    $ git push --all
    
###  直接将补丁发送至邮件列表

如果你想直接将补丁发送至一个邮件列表，需要安装以下软件包：[perl-authen-sasl](<https://archlinux.org/packages/?name=perl-authen-sasl>)包 和 [perl-io-socket-ssl](<https://archlinux.org/packages/?name=perl-io-socket-ssl>)包。 

确保你已经配置了用户名和邮件地址（参见[#配置](<#%E9%85%8D%E7%BD%AE>)）。 

配置你的邮箱设置： 
    
    $ git config --global sendemail.smtpserver _smtp.example.com_
    $ git config --global sendemail.smtpserverport _587_
    $ git config --global sendemail.smtpencryption _ssl_
    $ git config --global sendemail.smtpuser _foobar@example.com_
    
现在你应该可以将补丁发送至某个邮件列表了（可参阅[OpenEmbedded: 通过电子邮件发送补丁](<https://docs.yoctoproject.org/dev/contributor-guide/submit-changes.html#sending-the-patches-via-email>)和 [git-send-email.io](<https://git-send-email.io/>)）： 
    
    $ git add _filename_
    $ git commit -s
    $ git send-email --to=_openembedded-core@lists.openembedded.org_ --confirm=always -M -1
    
###  远程库很大时的注意事项

使用大型远程存储库时，必须获取大量数据。以下示例使用 Linux 内核来说明如何使用此类代码库。 

####  接收整个仓库

最简单的解决方案是获取整个存储库： 
    
    $ git clone <git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git>
    
**注意：**`git clone` 不支持断点续传。

可以通过 `git pull` 更新存储库。 

####  部分接收

为了将本地存储库限制为原存储库的较小子集，例如在 v4.14 之后分离出错误，请使用浅克隆 (shallow clone)： 
    
    $ git clone --shallow-exclude v4.13 <git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git>
    
将获取 v4.14 及更高版本，但不会获取 v4.13 及更早版本。 

如果您只想要最新的快照，则可以忽略所有历史记录。（如果有可用且足够完整的 tarball，请选择它。从 git 存储库下载需要更大的带宽。）您可以使用以下命令获取它： 
    
    $ git clone --depth 1 <git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git>
    
可以在之后获取较旧的提交，如以下两个示例： 
    
    $ git fetch --tags --shallow-exclude v4.1
    $ git fetch --tags --shallow-since 2016-01-01
    
**注意：** 如果不指定 `--tags`，就不会获取标签。

####  使用 Scalar

[Scalar](<https://github.com/microsoft/scalar>)，前身是 [Virtual File System for Git](<https://en.wikipedia.org/wiki/Virtual_File_System_for_Git> "wikipedia:Virtual File System for Git") (VFS for Git)，允许无需本地实例访问 git 仓库。 

参见 [scalar(1)](<https://man.archlinux.org/man/scalar.1>)。 

####  获取其他分支

在上面的示例中，本地的仓库仅跟踪主线内核，即"最新开发"的内核。假设你想获取最近的 LTS 内核，比如最新的 4.14 分支，可以这么做： 
    
    $ git remote set-branches --add origin linux-4.14.y
    $ git fetch --shallow-exclude v4.14
    $ git branch --track linux-4.14.y origin/linux-4.14.y
    
最后一行不是必须的，但你应该需要执行它。 （要获取需要的那个分支的具体名称，没有什么通用的方法，或许可以靠 [Gitweb](<../zh-cn/Gitweb.html> "Gitweb") 页面的"ref"链接来猜测） 

如果需要 linux-4.14.y 的快照，这样做： 
    
    $ git checkout linux-4.14.y
    
或者将它解压到其他目录里： 
    
    $ mkdir /path/to/src-4.14; cd /path/to/src-4.14
    $ git clone --no-local --depth 1 -b linux-4.14.y ../linux-stable
    
然后像平常一样，执行 `git pull` 来更新你的快照。 

###  过滤机密信息

有时，软件可能会将纯文本密码保存在配置文件中，而不是挂接到密钥环中。在这些情况下，git clean-filters 可能很方便，可以避免意外提交机密信息。例如，以下文件将过滤器分配给文件"some-dotfile"： 
    
    .gitattributes
    
    some-dotfile filter=remove-pass
    
每当文件"some-dotfile"添加到 git 时，git 都会在添加之前对文件调用过滤器"remove-pass"。必须在 git 配置文件中定义过滤器，例如： 
    
    .git/config
    
    [filter "remove-pass"]
    clean = "sed -e 's/^password=.*/#password=TODO/'"
    
**注意：** 在这种情况下，转义 sed 表达式的特殊字符可能是一项[棘手的任务](<https://stackoverflow.com/questions/49652495/git-filter-and-sed-fight-over>)。请记住，git 会将两个反斜杠变成一个，而 git 调用来运行命令的 shell 会再次将两个反斜杠变成一个。有关更多详细信息，请参阅[Git 过滤器和 sed 争夺 `\$`（英文）](<https://stackoverflow.com/a/49654653>)。

###  HTML 帮助文件

通过安装 [git-htmldocs](<https://aur.archlinux.org/packages/git-htmldocs/>)AUR，可以以 HTML 形式获取 `git help` 文档。安装后，可以通过传递 `-w` 标志来访问 HTML 文档。例如： 
    
    $ git help -w merge
    
可以通过设置 `git config` 选项默认加载 HTML 文档： 
    
    $ git config --global help.format html
    
##  扩展

###  助手和工具

  * **git-extras** — Git 实用工具集合（仓库摘要、repl、变更日志、作者提交百分比等）

     <https://github.com/tj/git-extras> || [git-extras](<https://aur.archlinux.org/packages/git-extras/>)AUR \- 如果使用 [oh-my-zsh](<https://ohmyz.sh>)，还可以启用 [git-extras 插件](<https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git-extras>)

  * **gitflow-cjs** — 使用 [Vincent Driessen 的分支模型](<https://nvie.com/posts/a-successful-git-branching-model/>)扩展 Git。CJS 版本是一个积极维护的分支。

     <https://github.com/CJ-Systems/gitflow-cjs> || [gitflow-cjs](<https://aur.archlinux.org/packages/gitflow-cjs/>)AUR

  * **gitmoji-cli** — 一个 [gitmoji](<https://gitmoji.dev/>) 交互式 NodeJS 客户端，用于在提交消息中使用 gitmojis。

     <https://github.com/carloscuesta/gitmoji-cli> || [nodejs-gitmoji-cli](<https://aur.archlinux.org/packages/nodejs-gitmoji-cli/>)AUR

###  大文件同步支持

  * **git-annex** — 用 Haskell 编写的分布式文件同步系统，允许使用 Git 管理大数据。

     <https://git-annex.branchable.com> || [git-annex](<https://archlinux.org/packages/?name=git-annex>)包

###  多 Git 仓库管理

  * **git-bulk** — 用 Bash 编写的命令行工具，用于管理多个 Git 仓库。

     <https://github.com/tj/git-extras> || [git-extras](<https://aur.archlinux.org/packages/git-extras/>)AUR

  * **mani** — 用 Go 编写的命令行工具和 TUI，用于管理多个 Git 仓库。

     <https://github.com/alajmo/mani> || [mani](<https://aur.archlinux.org/packages/mani/>)AUR

  * **gita** — 用 Python 编写的命令行工具，用于管理多个 Git 仓库。

     <https://github.com/nosarthur/gita> || [gita](<https://aur.archlinux.org/packages/gita/>)AUR

  * **mu-repo** — 用 Python 编写的命令行工具，用于管理多个 Git 仓库。

     <https://github.com/fabioz/mu-repo> || [mu-repo](<https://aur.archlinux.org/packages/mu-repo/>)AUR

  * **myrepos (mr)** — 用 Perl 编写的命令行工具，用于管理多个 Git 仓库。

     <https://myrepos.branchable.com/> || [myrepos](<https://archlinux.org/packages/?name=myrepos>)包

##  参见

  * Git 手册页，见 [git(1)](<https://man.archlinux.org/man/git.1>)
  * [Pro Git book](<https://git-scm.com/book/en/>)
  * GitHub 的 [Git Reference](<https://git.github.io/git-reference/>)
  * [Git workflow: Forks, remotes, and pull requests](<https://web.archive.org/web/20150316035247/https://nathanhoad.net/git-workflow-forks-remotes-and-pull-requests>)
  * [VideoLAN wiki article](<https://wiki.videolan.org/Git>)
  * [Git Protocols - Git on the Server](<https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols>)
  * [<https://gun.io/blog/how-to-github-fork-b>
