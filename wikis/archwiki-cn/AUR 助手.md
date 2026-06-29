**翻译状态：**

  * 本文（或部分内容）译自 [AUR_helpers](<https://wiki.archlinux.org/title/AUR_helpers> "arch:AUR helpers")，最近一次同步于 2025-01-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/AUR_helpers?diff=0&oldid=822007>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/AUR_helpers_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [yay](<../zh-cn/Yay.html> "Yay")
  * [pacman](<../zh-cn/Pacman.html> "Pacman")

**警告：** Arch Linux 不对 AUR 助手相关问题提供支持。您应当熟悉[手动构建过程](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#%E5%AE%89%E8%A3%85%E4%B8%8E%E6%9B%B4%E6%96%B0%E8%BD%AF%E4%BB%B6%E5%8C%85> "Arch 用户仓库")，以准备好解决可能遇到的问题。

**提示：** 优先使用讨论页而非编辑此文：[Talk:AUR 助手](</wzh/index.php?title=Talk:AUR_%E5%8A%A9%E6%89%8B&action=edit&redlink=1> "Talk:AUR 助手（页面不存在）")。

使用 [Arch 用户仓库](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html> "Arch 用户仓库")时，AUR 助手可以自动完成以下任务： 

  * 查找 AUR 上发布的包；
  * 解析 AUR 包之间的依赖关系；
  * 获取并构建 AUR 软件包；
  * 获取在线内容，例如用户评论；
  * 提交 AUR 软件包。

[Pacman](<../zh-cn/Pacman.html> "Pacman") 只处理其仓库内预构建的软件包的更新。AUR 软件包以 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 的形式分发，并需要 AUR 助手自动完成构建。然而切记：即使该包自身没有更新，但其依赖的共享库（shared library）有更新，您可能仍需重新构建该包。 

##  说明

[#对比表](<#%E5%AF%B9%E6%AF%94%E8%A1%A8>)各表头释义： 

文件检查
     _默认_ 不 [source](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Source> "Source") [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")；或在此之前，提醒并允许用户手动检查 PKGBUILD。有些助手会在用户能检查 PKGBUILD 之前就执行了 [source](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Source> "Source")，**给隐含的恶意代码带来可能性** 。
差异比较：有能力检查包之间差异。除了 PKGBUILD，还要检查对附加文件的改动，例如 `.install` 或 `.patch` 文件。
Git clone
    默认使用 [git-clone(1)](<https://man.archlinux.org/man/git-clone.1>) 从 AUR 获取构建文件。
可靠的解析器：能通过运用提供的元数据 ([RPC](</wzh/index.php?title=Aurweb_RPC_interface&action=edit&redlink=1> "Aurweb RPC interface（页面不存在）")/.SRCINFO) 而非[解析](<https://en.wikipedia.org/wiki/Parsing#Parser> "w:Parsing") PKGBUILD 来处理复杂软件包，例如 [aws-cli-git](<https://aur.archlinux.org/packages/aws-cli-git/>)AUR。
可靠的求解器：有能力正确解决并构建复杂的依赖链，例如 [ros-noetic-desktop-full](<https://aur.archlinux.org/packages/ros-noetic-desktop-full/>)AUR。
包拆分：有能力正确地构建并安装：
    
  * 对于有相同包基础的多个软件包，不重复构建和安装其基础，例如 [clion](<https://aur.archlinux.org/packages/clion/>)AUR。
  * 拆分依赖于同一基础的多个软件包，例如 [samsung-unified-driver](<https://aur.archlinux.org/packages/samsung-unified-driver/>)AUR。
  * 独立拆分软件包，例如 [nxproxy](<https://aur.archlinux.org/packages/nxproxy/>)AUR 以及 [nxagent](<https://aur.archlinux.org/packages/nxagent/>)AUR。

Shell 补全
     [Tab 补全](<https://en.wikipedia.org/wiki/Command-line_completion> "w:Command-line completion")在所列出的 [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell") 中可用。

**注意：**

  * _可选_ 意味着该功能可用，但是需要通过命令行参数或配置文件启用。
  * _部分_ 意味着该功能尚未完全实现，或与给定标准有部分差异。

##  对比表

###  查找并下载

名称 | 编写语言 | 文件检查 | 差异比较 | Git clone | 可靠的解析器 | 可靠的求解器 | Shell 补全 | 特性   
---|---|---|---|---|---|---|---|---  
[auracle-git](<https://aur.archlinux.org/packages/auracle-git/>)AUR | C++ | 是 | 否 | [是](<https://github.com/falconindy/auracle/commit/c73bbee>) | 是 | 是 | bash | 显示构建顺序   
[pbget](<https://aur.archlinux.org/packages/pbget/>)AUR | Python | 是 | 否 | 是 | 是 | – | – | –   
[repoctl](<https://aur.archlinux.org/packages/repoctl/>)AUR | Go | 是 | 否 | 否 | [是](<https://github.com/goulash/pacman/blob/master/aur/aur.go>) | – | bash, zsh, fish |  [本地仓库](</wzh/index.php?title=Local_repository&action=edit&redlink=1> "Local repository（页面不存在）")  
[yaah](<https://aur.archlinux.org/packages/yaah/>)AUR | Bash | 是 | 否 | 可选 | 是 | – | bash | –   
  
###  查找并构建

名称 | 编写语言 | 文件检查 | 差异比较 | Git clone | 可靠的解析器 | 可靠的求解器 | 包拆分 | Shell 补全 | 特性   
---|---|---|---|---|---|---|---|---|---  
[aurutils](<https://aur.archlinux.org/packages/aurutils/>)AUR | Bash | 是 | 是 | 是 | 是 | 是 | 是 | bash, zsh |  [本地仓库](</wzh/index.php?title=Local_repository&action=edit&redlink=1> "Local repository（页面不存在）")，应用本地补丁，[包签名](</wzh/index.php?title=Package_signing&action=edit&redlink=1> "Package signing（页面不存在）")，[干净的 chroot](</wzh/index.php?title=DeveloperWiki:Building_in_a_clean_chroot&action=edit&redlink=1> "DeveloperWiki:Building in a clean chroot（页面不存在）")  
[bauerbill](<https://aur.archlinux.org/packages/bauerbill/>)AUR | Python | 是 | 否 | 是 | 是 | 是 | 是 | bash, zsh |  `bb-wrapper` 用于 _pacman_ 封装和信任管理   
[PKGBUILDer](<https://aur.archlinux.org/packages/PKGBUILDer/>)AUR | Python | 否 | [否](<https://github.com/Kwpolska/pkgbuilder/issues/36>) | 是 | 是 | 是 | [部分](<https://github.com/Kwpolska/pkgbuilder/issues/39>) | – |  `pb` 用于 _pacman_ 封装   
[rua](<https://aur.archlinux.org/packages/rua/>)AUR | Rust | 是 | [是](<https://github.com/vn971/rua/commit/0459a8b>) | 是 | [是](<https://github.com/vn971/rua/commit/fc8c2f3>) | 是 | [是](<https://github.com/vn971/rua/commit/7889045>) | bash, zsh, fish | l应用本地补丁，[bubblewrap](<../zh-cn/Bubblewrap.html> "Bubblewrap")， `.pkg.tar` 检查   
  
###  Pacman 封装

**警告：**[pacman(8)](<https://man.archlinux.org/man/pacman.8>) 封装将包管理器的工作抽象化。这些封装可能（可选或默认地）引入 [不安全标志](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E9%81%BF%E5%85%8D%E6%9F%90%E4%BA%9B_pacman_%E5%91%BD%E4%BB%A4> "系统维护")，或其他导致系统缺陷的异常行为。

**注意：** 下列 pacman 封装支持批量（而非按需）操作：[pacaur](<https://aur.archlinux.org/packages/pacaur/>)AUR, [pikaur](<https://aur.archlinux.org/packages/pikaur/>)AUR, [yay](<https://aur.archlinux.org/packages/yay/>)AUR, [aura](<https://aur.archlinux.org/packages/aura/>)AUR, [paru](<https://aur.archlinux.org/packages/paru/>)AUR, [aurman](<https://aur.archlinux.org/packages/aurman/>)AUR

名称 | 编写语言 | 文件检查 | 差异比较 | Git clone | 可靠的解析器 | 可靠的求解器 | 包拆分 | 不安全标志 | Shell 补全 | 特性   
---|---|---|---|---|---|---|---|---|---|---  
[aura](<https://aur.archlinux.org/packages/aura/>)AUR | Rust | 否 | [部分](<https://github.com/aurapm/aura/blob/89bf702/aura/src/Aura/Pkgbuild/Records.hs>) | [是](<https://github.com/fosskers/aura/commit/ca9c38d>) | [是](<https://github.com/aurapm/aura/commit/7848e98>) | [是](<https://github.com/fosskers/aura/pull/479>) | [是](<https://github.com/fosskers/aura/pull/479>) | – | bash, fish, zsh |  [干净的 chroot](</wzh/index.php?title=DeveloperWiki:Building_in_a_clean_chroot&action=edit&redlink=1> "DeveloperWiki:Building in a clean chroot（页面不存在）")  
[aurman](<https://aur.archlinux.org/packages/aurman/>)AUR | Python | 是 | 是 | 是 | 是 | [部分](<https://github.com/polygamma/aurman/issues/259>) | 是 |  [-Sy](<https://github.com/polygamma/aurman/commit/6c02ba3>)  
[\--ask](<https://github.com/polygamma/aurman#make-use-of-the-undocumented---ask-flag-of-pacman>) | bash, fish | 提取 PGP 密钥   
[pacaur](<https://aur.archlinux.org/packages/pacaur/>)AUR | Bash | 是 | 是 | 是 | 是 | 是 | 是 | [\--ask](<https://github.com/E5ten/pacaur/commit/12707cc>) | bash, zsh | –   
[pakku](<https://aur.archlinux.org/packages/pakku/>)AUR | Nim | 是 | [是](<https://github.com/kitsunyan/pakku/commit/396e9f4>) | 是 | 是 | 是 | 是 | [-Sy](<https://github.com/kitsunyan/pakku/wiki/Native-Pacman-Explanation>) | bash, zsh | –   
[paru](<https://aur.archlinux.org/packages/paru/>)AUR | Rust | 是 | 是 | 是 | 是 | 是 | 是 |  [-Sy](<https://github.com/Morganamilo/paru/blob/15394a7db80d045f038ea4d0ee94d00211070c96/man/paru.8#L543-L552>)  
[\--ask](<https://github.com/Morganamilo/paru/blob/32b75ac1cb7e0fccd21a0f795f25fd9fb1a14d8a/man/paru.conf.5#L110-L116>) | bash, fish, zsh |  [本地仓库](</wzh/index.php?title=Local_repository&action=edit&redlink=1> "Local repository（页面不存在）")，[干净的 chroot](</wzh/index.php?title=DeveloperWiki:Building_in_a_clean_chroot&action=edit&redlink=1> "DeveloperWiki:Building in a clean chroot（页面不存在）")  
[pikaur](<https://aur.archlinux.org/packages/pikaur/>)AUR | Python | 是 | 是 | 是 | 是 | 是 | 是 | [-Sy](<https://github.com/actionless/pikaur#pikaur>) | bash, fish, zsh |  [动态用户](<https://0pointer.net/blog/dynamic-users-with-systemd.html>)  
[trizen](<https://aur.archlinux.org/packages/trizen/>)AUR | Perl | 是 | 是 | [是](<https://github.com/trizen/trizen/commit/6fb0cc9>) | [是](<https://github.com/trizen/trizen/commit/7ab7ee5f>) | 是 | [部分](<https://github.com/trizen/trizen/issues/46>) | – | bash, fish, zsh | –   
[yay](<https://aur.archlinux.org/packages/yay/>)AUR | Go | 是 | [是](<https://github.com/Jguer/yay/pull/447>) | [是](<https://github.com/Jguer/yay/pull/297>) | 是 | [是](<https://github.com/Jguer/yay/pull/866>) | 是 | [\--ask](<https://github.com/Jguer/yay/commit/ea5a94e>) | bash, fish, zsh | –   
  
##  图形化

**警告：** 使用图形化的 AUR 助手可能导致系统缺陷，例如执行无人值守的[部分更新](</wzh/index.php?title=Partial_upgrade&action=edit&redlink=1> "Partial upgrade（页面不存在）")。

  * **Argon** — 使用 Python 编写的 GTK 3 pacman 封装。

     <https://github.com/14mRh4X0r/arch-argon> || [argon](<https://aur.archlinux.org/packages/argon/>)AUR

  * **Bauh** — 使用 Python 编写的 Qt 5 应用，支持 AppImage，Debian，Arch 软件包（含 AUR），Flatpak，Snap 以及 原生 Web 应用。

     <https://github.com/vinifmor/bauh> || [bauh](<https://aur.archlinux.org/packages/bauh/>)AUR

  * **Cylon** — 使用 Bash 编写的 TUI（终端界面）pacman 封装。

     <https://github.com/gavinlyonsrepo/cylon> || [cylon](<https://aur.archlinux.org/packages/cylon/>)AUR

  * **Kalu** — 系统托盘通知图标，使用 libalpm 和 [PolicyKit](</wzh/index.php?title=PolicyKit&action=edit&redlink=1> "PolicyKit（页面不存在）") 编写，有可选的更新器。

     <https://github.com/Thulinma/kalu> || [kalu](<https://aur.archlinux.org/packages/kalu/>)AUR

  * **Octopi** — 使用 C++ 编写的 Qt 5 pacman 封装。

     <https://tintaescura.com/projects/octopi> || [octopi](<https://aur.archlinux.org/packages/octopi/>)AUR

  * **Pacseek** — 一个终端用户界面封装，可以查找并安装 Arch Linux 软件包。

     <https://github.com/moson-mo/pacseek> || [pacseek](<https://aur.archlinux.org/packages/pacseek/>)AUR

  * **Pamac** — 使用 [libalpm(3)](<https://man.archlinux.org/man/libalpm.3>)、为 Manjaro 编写的、独立的 GTK 4（或终端界面）包管理器。有托盘程序；也可在命令行界面中使用。

     <https://wiki.manjaro.org/index.php/Pamac> || [pamac-aur](<https://aur.archlinux.org/packages/pamac-aur/>)AUR

  * **Pakku GUI** — 使用 python 编写的 pakku 的 GTK 3 前端。

     <https://gitlab.com/mrvik/pakku-gui> || [pakku-gui](<https://aur.archlinux.org/packages/pakku-gui/>)AUR

  * **PkgBrowser** — 使用 python 编写的 Qt 5 程序、查看官方仓库/AUR 软件包的只读浏览器。

     <https://osdn.net/projects/pkgbrowser/> || [pkgbrowser](<https://aur.archlinux.org/packages/pkgbrowser/>)AUR

  * **Yup** — 使用 Go 和 Ncurses 编写的 TUI pacman 封装。

     <https://github.com/ericm/yup> || [yup](<https://aur.archlinux.org/packages/yup/>)AUR

##  维护

  * **aur-out-of-date** — 借助主机服务提供者的 API，检查 AUR 软件包的上游更改。

     <https://github.com/simon04/aur-out-of-date> || [aur-out-of-date](<https://aur.archlinux.org/packages/aur-out-of-date/>)AUR

  * **aurpublish** — AUR 助手脚本：借助 [git-subtree(1)](<https://man.archlinux.org/man/git-subtree.1>) 管理和上传 AUR 软件包。会使用 [githooks(5)](<https://man.archlinux.org/man/githooks.5>) 校验 PKGBUILD，自动生成 .SRCINFO，以及创建需提交信息的模板。

     <https://github.com/eli-schwartz/aurpublish> || [aurpublish](<https://archlinux.org/packages/?name=aurpublish>)包

  * **[devtools](</wzh/index.php?title=DeveloperWiki:Building_in_a_clean_chroot&action=edit&redlink=1> "DeveloperWiki:Building in a clean chroot（页面不存在）")** — 在干净的环境（[systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn") 容器）中构建软件包，以确保正确性。被 [aura](<https://aur.archlinux.org/packages/aura/>)AUR，[aurutils](<https://aur.archlinux.org/packages/aurutils/>)AUR，[clean-chroot-manager](<https://aur.archlinux.org/packages/clean-chroot-manager/>)AUR，和 [paru](<https://aur.archlinux.org/packages/paru/>)AUR 封装。

     <https://gitlab.archlinux.org/archlinux/devtools> || [devtools](<https://archlinux.org/packages/?name=devtools>)包

  * **pkgoutofdate** — 解析 PKGBUILD 中的源 URL，并以发送递增版本号的方式，尝试寻找软件包的较新版本。

     <https://github.com/anatol/pkgoutofdate> || [pkgoutofdate-git](<https://aur.archlinux.org/packages/pkgoutofdate-git/>)AUR

  * **repman** — 用于管理本地和远程仓库的命令行工具。

     <https://gitlab.com/mipimipi/repman> || [repman-git](<https://aur.archlinux.org/packages/repman-git/>)AUR

##  其他

  * **aur-talk** — 提取并显示 AUR 评论。

     <https://github.com/GermainZ/aur-talk> || [aur-talk-git](<https://aur.archlinux.org/packages/aur-talk-git/>)AUR

  * **aurvote-utils** — 一系列管理 AUR 投票的实用工具。

     <https://github.com/jadenPete/aurvote-utils> || [aurvote-utils](<https://aur.archlinux.org/packages/aurvote-utils/>)AUR

  * **haskell-aur** — 用于访问 [Aurweb RPC 界面](</wzh/index.php?title=Aurweb_RPC_interface&action=edit&redlink=1> "Aurweb RPC interface（页面不存在）")的 Haskell 库。

     <https://hackage.haskell.org/package/aur> || [haskell-aur](<https://aur.archlinux.org/packages/haskell-aur/>)AUR

  * **package-query** — 用于查询 [libalpm(3)](<https://man.archlinux.org/man/libalpm.3>) 和 AUR 的工具。

     <https://github.com/archlinuxfr/package-query> || [package-query](<https://aur.archlinux.org/packages/package-query/>)AUR

  * **python3-aur** — 用于访问 AUR 包信息、自动化 AUR 交互过程的 Python 3 模块和 AUR 助手工具。

     <https://xyne.dev/projects/python3-aur> || [python3-aur](<https://aur.archlinux.org/packages/python3-aur/>)AUR

  * **raur** — 用于访问 [Aurweb RPC 界面](</wzh/index.php?title=Aurweb_RPC_interface&action=edit&redlink=1> "Aurweb RPC interface（页面不存在）")的 Rust 库。

     <https://gitlab.com/davidbittner/raur> ||

##  参见

  * [适用于 Arch Linux 的图形化包管理器](<https://www.debugpoint.com/arch-linux-gui-package-managers/>) (DebugPoint, 2023) 提供[#图形化](<#%E5%9B%BE%E5%BD%A2%E5%8C%96>)中某些选项的截屏和简单信息。
