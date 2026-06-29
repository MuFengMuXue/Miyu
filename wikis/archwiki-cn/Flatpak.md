**翻译状态：**

  * 本文（或部分内容）译自 [Flatpak](<https://wiki.archlinux.org/title/Flatpak> "arch:Flatpak")，最近一次同步于 2025-04-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Flatpak?diff=0&oldid=829550>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Flatpak_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Snapd](</wzh/index.php?title=Snapd&action=edit&redlink=1> "Snapd（页面不存在）")
  * [bubblewrap](<../zh-cn/Bubblewrap.html> "Bubblewrap")

引自项目 [README](<https://github.com/flatpak/flatpak/blob/master/README.md>)：“[Flatpak](<https://flatpak.org>) 是一个 Linux 桌面程序的构建、分发和沙箱化运行系统。” 

引自 [flatpak(1)](<https://man.archlinux.org/man/flatpak.1>)： 

    Flatpak 是一个用来管理应用和应用所使用的运行时的工具。在 Flatpak 模型中，应用的构建和分发不依赖其主系统，并且它们在运行时一定程度上独立于主系统（'沙箱化'）。
    Flatpak 使用 [OSTree](<https://netmodule-linux.readthedocs.io/en/latest/gettingstarted/3_ostree.html?highlight=ostree>) 以分发和部署数据。它使用的仓库是 OSTree 仓库并且可以用 ostree 的工具来操作，已安装的运行时和应用都是 OSTree 检出。

**警告：**

  * [flathub](<https://flathub.org/home>) 上的很多 Flatpak 应用默认并未有效地沙箱化[[1]](<https://hanako.codeberg.page>)。在未检查 flatpak 相关权限清单是否有沙箱逃逸问题前，请勿依赖提供的检查隔离功能。
  * 运行不受信任的软件永不安全，沙箱化也无法改变这一点。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [flatpak](<https://archlinux.org/packages/?name=flatpak>)包 软件包。如果需要构建 flatpak，请一并安装 `flatpak-builder`。 

###  桌面环境整合

对于与桌面环境交互的 flatpak 应用（例如使用应用打开 URL、共享屏幕等），先确保已配置了 [XDG 桌面门户](<../zh-cn/XDG_%E6%A1%8C%E9%9D%A2%E9%97%A8%E6%88%B7.html> "XDG 桌面门户")。取决于桌面环境的实现不同，在应用调用功能前会出现一个确认窗口。 

###  应用管理

  * **Discover** — Flatpak 的 KDE 前端，可用于搜索和安装应用、游戏和工具，是 [plasma](<https://archlinux.org/groups/x86_64/plasma/>)包组 的一部分。

     <https://apps.kde.org/discover/> || [discover](<https://archlinux.org/packages/?name=discover>)包

  * **GNOME Software** — Flatpak 的 GNOME 前端，可用于安装和更新应用及系统扩展，是 [gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组 的一部分。

     <https://apps.gnome.org/Software/> || [gnome-software](<https://archlinux.org/packages/?name=gnome-software>)包

###  权限管理

  * **Flatpak 权限管理 KCM** — KDE 配置模块，可以修改已安装 Flatpak 应用的权限，是 [plasma](<https://archlinux.org/groups/x86_64/plasma/>)包组 的一部分。

     <https://invent.kde.org/plasma/flatpak-kcm> || [flatpak-kcm](<https://archlinux.org/packages/?name=flatpak-kcm>)包

  * **Flatseal** — 用于检查并修改 Flatpak 应用权限的图形化工具。

     <https://github.com/tchx84/Flatseal> || [flatseal](<https://aur.archlinux.org/packages/flatseal/>)AUR

  * **malcontent（家长控制）** — 实现了控制非管理员账户能访问的内容类型的功能，是 [gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组 的一部分。

     <https://gitlab.freedesktop.org/pwithnall/malcontent> || [malcontent](<https://archlinux.org/packages/?name=malcontent>)包

##  管理仓库

**注意：** 默认情况下，每个 flatpak 命令都是全局可用的，具体来说，软件包是安装给当前机器的所有用户的，并且要求用户提供 root 密码。如果想针对单个用户安装软件包或操作仓库，你可以添给每个命令加 `--user` 参数，此时不需要提供超级权限。例如，你想添加一个仅自己可见的仓库，你应该执行 `flatpak remote-add --user _name_ _location_`。

###  添加一个仓库

要添加一个远程 flatpak 仓库，执行： 
    
    $ flatpak remote-add _name_ _location_
    
这其中 _name_ 是新远程仓库的名字，而 _location_ 是仓库的路径或 URL。 

安装 flatpak 时默认会全局添加官方 [Flathub 仓库](<https://flathub.org/>)。如果要添加用户独立的官方仓库，可以执行： 
    
    $ flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
    
####  官方仓库的镜像站

对于中国大陆用户，有上海交通大学的 Flathub 缓存可供选择。 

使用方法： 
    
    sudo flatpak remote-modify flathub --url=<https://mirror.sjtu.edu.cn/flathub>
    
如果出现错误可尝试： 
    
    wget <https://mirror.sjtu.edu.cn/flathub/flathub.gpg>
    sudo flatpak remote-modify --gpg-import=flathub.gpg flathub
    
**注意：** 由于重分发授权问题，[NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 驱动、JetBrains 系列等软件需要从官方服务器下载，无法使用镜像站加速。

###  删除一个仓库

要删除一个远程 flatpak 仓库，执行： 
    
    $ flatpak remote-delete _name_
    
这其中 _name_ 是要删除的远程仓库的名字。 

###  仓库列表

要列出所有已添加的仓库列表，执行： 
    
    $ flatpak remotes
    
##  管理运行时和应用

**注意：** 如果仓库是[用户独立](<#%E6%B7%BB%E5%8A%A0%E4%B8%80%E4%B8%AA%E4%BB%93%E5%BA%93>)的，可以在 flatpak 命令添加 `--user` 选项。例如，如果要安装一个只有你可见的应用，可以执行 ` flatpak install --user _软件包名称_`。

###  搜索远程仓库的运行时和应用

在能搜索新添加的远程仓库中的运行时和应用之前，我们需要获取其软件应用流的数据： 
    
    $ flatpak update
    
    Looking for updates...
    Updating appstream data for remote _name_
    
之后我们可以通过 `flatpak search _packagename_` 命令来实现搜索，例如在配置完成的远程仓库 `flathub` 中搜索 `libreoffice` 软件包： 
    
    $ flatpak search libreoffice
    
    Application ID              Version Branch Remotes Description
    org.libreoffice.LibreOffice         stable flathub The LibreOffice productivity suite
    
###  列出所有可用的运行时和应用

要列出远程仓库 _remote_ 中所有可用的运行时和应用，执行： 
    
    $ flatpak remote-ls _remote_
    
###  安装一个运行时或应用

要安装一个运行时或应用，执行： 
    
    $ flatpak install _remote_ _name_
    
这其中 _remote_ 是远程仓库的名字，而 _name_ 是待安装的应用或运行时的名字。 

**提示：** 您可以使用部分标识符 `flatpak install _partial-name_` (例如 `flatpak install libreoffice`)。

###  列出所有已安装的运行时和应用

要列出所有已安装的运行时和应用，执行： 
    
    $ flatpak list
    
###  运行应用

二进制文件位于 `/var/lib/flatpak/exports/bin` 目录下，已自动通过 `/etc/profile.d/flatpak-bindir.sh` 添加到 $PATH 中，可能需要重新登录才会应用更改。 

Flatpak 应用也可以通过命令行运行： 
    
    $ flatpak run _name_
    
###  升级一个运行时或应用

列出所有可更新的运行时和应用： 
    
    $ flatpak remote-ls --updates
    
要升级一个名为 _name_ 的运行时或应用，执行： 
    
    $ flatpak update _name_
    
要更新所有应用和运行时，执行： 
    
    $ flatpak update
    
####  通过 systemd 自动更新

**警告：** 不建议通过 systemd 托管更新，应用可能会在用户不知道的情况下获取到新权限，相关案例可参考[该文](<https://ejona.ersoft.org/archive/2024/03/02/flatpak-perms-upgrade/>)。

要自动更新运行时和应用，先创建以下文件： 
    
    /etc/systemd/system/flatpak-update.service
    
    [Unit]
    Description=Update Flatpak
    After=network-online.target
    Wants=network-online.target
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/flatpak update --noninteractive --assumeyes
    
    [Install]
    WantedBy=multi-user.target
    
    /etc/systemd/system/flatpak-update.timer
    
    [Unit]
    Description=Update Flatpak
    
    [Timer]
    OnBootSec=2m
    OnActiveSec=2m
    OnUnitInactiveSec=24h
    OnUnitActiveSec=24h
    AccuracySec=1h
    RandomizedDelaySec=10m
    
    [Install]
    WantedBy=timers.target

然后执行 [daemon-reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Daemon-reload")，并[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `flatpak-update.timer` [单元](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")。 

**注意：**

  * 该部分适用于默认下的系统全局 flatpak 环境。对于用户独立的 flatpak 环境： 
    * 在 `/etc/systemd/user/` 目录下创建以上文件
    * 在 `flatpak-update.service` 中的 `ExecStart` 一行添加 `--user` 选项
    * 搭配 `--user` 选项执行 `systemctl` 命令

###  卸载一个运行时或应用

要卸载一个名为 _name_ 运行时或应用，执行： 
    
    $ flatpak uninstall _name_
    
要在卸载时从 `~/.var/app` 清除应用数据，并清除权限记录，执行： 
    
    $ flatpak uninstall --delete-data _name_
    
**提示：** 你可以通过 `flatpak uninstall --unused` 卸载不再使用的 flatpak 依赖（即无应用/运行时依赖的孤立包）。

###  降级一个运行时或应用

要降级一个运行时或应用，需要先获取到对应的提交（commit）ID： 
    
    $ flatpak remote-info --log _remote_ _name_
    
其中 _remote_ 是仓库名称（例如 flathub）， _name_ 是应用或运行时的名称。接下来是部署提交： 
    
    $ flatpak update --commit=_commit_ _name_
    
其中 _commit_ 是目标版本对应的的提交， _name_ 与上文一致。 

该操作也可以将软件包选择性地升级到非最新的一个版本。 

要禁止 `flatpak update` 升级该软件包，请参考[#禁止运行时或应用更新](<#%E7%A6%81%E6%AD%A2%E8%BF%90%E8%A1%8C%E6%97%B6%E6%88%96%E5%BA%94%E7%94%A8%E6%9B%B4%E6%96%B0>)。 

###  禁止运行时或应用更新

要禁止自动或手动升级运行时或软件包，请使用 `flatpak mask` 命令： 
    
    $ flatpak mask _name_
    
这也同时会禁止选择性升级和降级。 

如果要重新启用升级功能，请使用 `flatpak mask --remove`： 
    
    $ flatpak mask --remove _name_
    
###  添加 Flatpak .desktop 文件到您的菜单

Flatpak 期望窗口管理器按照 [XDG_DATA_DIRS](<../zh-cn/XDG_%E5%9F%BA%E6%9C%AC%E7%9B%AE%E5%BD%95.html#%E7%B3%BB%E7%BB%9F%E7%9B%AE%E5%BD%95> "XDG 基本目录") [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")来查找应用，该变量通过 `/etc/profile.d/flatpak.sh` 脚本进行配置。在更新系统环境后，有可能需要重新登录系统。如果启动器不支持 `XDG_DATA_DIRS`，可以编辑目录扫描列表并添加以下两个文件夹： 
    
    ~/.local/share/flatpak/exports/share/applications
    /var/lib/flatpak/exports/share/applications
    
目前已知此方法在 [Awesome](<../zh-cn/Awesome.html> "Awesome") 中是必须的。 

###  覆盖应用的沙箱权限

如果你发现应用的预定义权限过松或过紧，你可以使用 `flatpak override` 命令进行修改。 

例如： 
    
    $ flatpak override --nofilesystem=home _name_
    
这会禁止应用访问你的用户主目录。 

所有可以赋予权限的类型，如设备、文件系统或 socket ，都有对应的命令行选项以允许或禁止确切的权限。例如，可以使用 `--device=_device_name_` 允许访问特定设备，而 `--nodevice=_device_name_` 会禁用设备访问权限。 

对于所有可操作的权限类型，详见：[flatpak-override(1)](<https://man.archlinux.org/man/flatpak-override.1>)

下面的命令可将所有更改过的权限重设为默认： 
    
    $ flatpak override --reset _name_
    
如果更偏好图形界面，可以使用 _Flatseal_ ；在 KDE Plasma 上， _Flatpak 权限管理 KCM_ 在系统设置中提供了类似的图形界面： _System Settings > Applications > Flatpak Permission Settings_

##  创建自定义基本运行时

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 有待完善，且对于 GNOME 应用存在 D-Bus 问题。 (在 [Talk:Flatpak](<../zh-cn/Talk:Flatpak.html>) 中讨论)

**警告：** 如果要将你的应用作为 Flatpak 发布，不要使用基于 Arch 的运行时。请参考[官方文档](<https://docs.flatpak.org>)使用[通用运行时](<https://flatpak.org/runtimes.html>)将你的软件正确地整合到 Flatpak 生态中。

**注意：**

  * 鉴于在创建应用和运行时期间软件并没有沙箱化，你可能会想使用一个单独的非受信、非特权用户对不信任的软件进行打包。
  * 在分发软件包时，你可能会有法律义务提供一些包内软件的源码。你可能会想使用 [ABS](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "ABS") 从源码构建软件包。

除了使用默认的 `org.freedesktop.BasePlatform` 和 `org.freedesktop.BaseSdk` 运行时外，你还可以在自用的情况下，通过 pacman 为 Flatpak 创建一个基于 Arch 的自定义运行时和基本 SDK，然后用其构建并打包软件。 

除 [flatpak](<https://archlinux.org/packages/?name=flatpak>)包 外，你还需要安装 [fakeroot](<https://archlinux.org/packages/?name=fakeroot>)包，对于 pacman 钩子支持还需安装 [fakechroot](<https://archlinux.org/packages/?name=fakechroot>)包。 

首先创建一个目录，用于构建运行时或应用： 
    
    $ mkdir _myflatpakbuilddir_
    $ cd _myflatpakbuilddir_
    
然后就可以准备一个用于构建运行时基本平台的目录，其中的文件将被打包到沙箱中的 `/usr` 目录。因此，你会需要创建一些软链接，以使 Arch 下的 `/usr/share` 等目录仍可通过正常路径访问： 
    
    $ mkdir -p _myruntime_ /files/var/lib/pacman
    $ touch _myruntime_ /files/.ref
    $ ln -s /usr/usr/share _myruntime_ /files/share
    $ ln -s /usr/usr/include _myruntime_ /files/include
    $ ln -s /usr/usr/local _myruntime_ /files/local
    
使主机下的字体在 Arch 运行时中可用： 
    
    $ mkdir -p _myruntime_ /files/usr/share/fonts
    $ ln -s /run/host/fonts _myruntime_ /files/usr/share/fonts/flatpakhostfonts
    
在安装软件包到运行时前，需要修改一下你的 `pacman.conf` 文件。将 `/etc/pacman.conf` 复制到构建目录中，然后进行以下修改： 

  * 移除 `CheckSpace` 选项，以使 pacman 不会因检查硬盘空间产生找不到根文件系统的报错。
  * 移除不需要的自定义仓库，以及只有主机需要的 `IgnorePkg`，`IgnoreGroup`，`NoUpgrade` 和 `NoExtract` 设置。

接下来为运行时安装软件包： 
    
    $ fakechroot fakeroot pacman -Syu --root _myruntime_ /files --dbpath _myruntime_ /files/var/lib/pacman --config pacman.conf base
    $ mv pacman.conf _myruntime_ /files/etc/pacman.conf
    
编辑 `_myruntime_ /files/etc/locale.gen`，配置需要使用的 [locales](<../zh-cn/Locale.html> "Locale")，然后生成 locale： 
    
    $ fakechroot chroot _myruntime_ /files locale-gen
    
可以通过为基础运行时添加构建软件包和运行 pacman 所需的应用来创建基础 SDK： 
    
    $ cp -r _myruntime_ mysdk
    $ fakechroot fakeroot pacman -S --root mysdk/files --dbpath mysdk/files/var/lib/pacman --config mysdk/files/etc/pacman.conf base-devel fakeroot fakechroot --needed
    
添加运行时和 SDK 的元数据： 
    
    _myruntime_ /metadata
    
    [Runtime]
    name=org.mydomain.BasePlatform
    runtime=org.mydomain.BasePlatform/x86_64/2016-06-26
    sdk=org.mydomain.BaseSdk/x86_64/2016-06-26
    
    mysdk/metadata
    
    [Runtime]
    name=org.mydomain.BaseSdk
    runtime=org.mydomain.BasePlatform/x86_64/2016-06-26
    sdk=org.mydomain.BaseSdk/x86_64/2016-06-26

将基础运行时和 SDK 添加到位于当前目录的本地仓库，你还可以为仓库添加例如“My Arch base runtime”和“My Arch base SDK”等提交（commit）信息： 
    
    $ ostree init --mode archive-z2 --repo=.
    $ EDITOR="nano -w" ostree commit -b runtime/org.mydomain.BasePlatform/x86_64/2016-06-26 --tree=dir=_myruntime_
    $ EDITOR="nano -w" ostree commit -b runtime/org.mydomain.BaseSdk/x86_64/2016-06-26 --tree=dir=mysdk
    $ ostree summary -u
    
安装运行时和 SDK： 
    
    $ flatpak remote-add --user --no-gpg-verify myarchos file://$(pwd)
    $ flatpak install --user myarchos org.mydomain.BasePlatform 2016-06-26
    $ flatpak install --user myarchos org.mydomain.BaseSdk 2016-06-26
    
###  使用 pacman 创建应用

除了构建应用的[通用方式](<https://flatpak.org/developer.html>)外，我们还可以创建通常 Arch 软件包的容器化版本。注意，在创建应用时 `/usr` 是只读的，因此在构建应用时无法使用 Arch 软件包。有两种方式可以通过 pacman 创建软件： 

  * 使用 pacman 创建包含所有依赖的运行时
  * 然后根据[正常方式](<https://flatpak.org/developer.html>)自行构建应用，或是将 pacman 搭配为 Flatpak 定制的 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")，其中在 `configure` 脚本中使用了 `--prefix=/app`。

或是 

  * 使用 pacman 创建一个运行时，其中包含通过 pacman 安装完成的应用
  * 然后使用一个虚拟应用进行启动

对于后一种方式，以 [gedit](<https://archlinux.org/packages/?name=gedit>)包 为例，首先通过 pacman 创建一个运行时，该运行时已为 pacman 进行了初始化和准备： 
    
    $ flatpak build-init -w geditruntime org.mydomain.geditruntime org.mydomain.BaseSdk org.mydomain.BasePlatform 2016-06-26
    $ flatpak build geditruntime sed -i "s/^#Server/Server/g" /etc/pacman.d/mirrorlist
    $ flatpak build geditruntime ln -s /usr/var/lib /var/lib
    $ flatpak build geditruntime fakeroot pacman-key --init
    $ flatpak build geditruntime fakeroot pacman-key --populate
    
然后安装软件包，这一步需要联网： 
    
    $ flatpak build --share=network geditruntime fakechroot fakeroot pacman --root /usr -S gedit
    
可以在完成运行时前测试一下（此时还没有完全沙箱化）： 
    
    $ flatpak build --socket=x11 geditruntime gedit
    
接下来完成运行时，并将其导出到新的本地仓库中。pacman 的 GnuPG 带有权限，可能会产生些问题，因此需要先将其移除： 
    
    $ flatpak build geditruntime rm -r /etc/pacman.d/gnupg
    $ flatpak build-finish geditruntime
    $ sed -i "s/\[Application\]/\[Runtime\]/;s/runtime=org.mydomain.BasePlatform/runtime=org.mydomain.geditruntime/" geditruntime/metadata
    $ flatpak build-export -r geditrepo geditruntime
    
然后创建一个虚拟应用： 
    
    $ flatpak build-init geditapp org.gnome.gedit org.mydomain.BaseSdk org.mydomain.geditruntime
    
接下来完成虚拟应用，你可以在完成应用时追加额外选项来调整应用权限，具体可用选项请参考 [Flatpak 文档](<#%E5%8F%82%E9%98%85>)和 [GNOME manifest files](<https://gitlab.gnome.org/GNOME/gnome-apps-nightly/tree/master>)。你还可以在完成构建后和导出前按需修改 `geditapp/metadata`。在完成元数据修改后，将应用导出到仓库： 
    
    $ flatpak build-finish geditapp --socket=x11 _[possibly other options]_ --command=gedit
    $ flatpak build-export geditrepo geditapp
    
安装应用和运行时： 
    
    $ flatpak --user remote-add --no-gpg-verify geditrepo geditrepo
    $ flatpak install --user geditrepo org.mydomain.geditruntime
    $ flatpak install --user geditrepo org.gnome.gedit
    $ flatpak run org.gnome.gedit
    
##  排障

###  Flatpak 无法在 linux-hardened 内核上运行

[linux-hardened](<https://archlinux.org/packages/?name=linux-hardened>)包 内核将 `kernel.unprivileged_userns_clone` 设为 `0`，使得只有特权用户才能创建新的用户命名空间。 

其中一个解决方案是[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [bubblewrap-suid](<https://archlinux.org/packages/?name=bubblewrap-suid>)包，该包提供了启用 `setuid` 的 [bwrap(1)](<https://man.archlinux.org/man/bwrap.1>)，使得 bubblewrap 可以自行提升权限并创建新命名空间。 

或者，也可以通过 [sysctl(8)](<https://man.archlinux.org/man/sysctl.8>) 将 `kernel.unprivileged_userns_clone` 设为 `1`，以允许非特权用户创建新的用户命名空间。 
    
    # sysctl kernel.unprivileged_userns_clone=1
    
**警告：** 该操作将给安全性带来负面影响，具体信息请参考[安全#沙盒程序](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E6%B2%99%E7%9B%92%E7%A8%8B%E5%BA%8F> "安全")。

要将该更改持久化，可以在 [sysctl.d(5)](<https://man.archlinux.org/man/sysctl.d.5>) 中添加一个配置文件： 
    
    /etc/sysctl.d/flatpak.conf
    
    kernel.unprivileged_userns_clone=1

更多信息请参考 [Bubblewrap#安装](<../zh-cn/Bubblewrap.html#%E5%AE%89%E8%A3%85> "Bubblewrap")。 

### Failed to connect to Wayland display

如果应用未能正常启动，并在使用 `flatpak run` 时出现类似如下报错： 

`Failed to connect to Wayland display: No such file or directory`

可能是因为像 `ELECTRON_OZONE_PLATFORM_HINT="auto"` 等选项使 Flatpak 应用调用了 Wayland，同时又未将 Wayland 权限授予应用导致的。 

可以使用 Flatseal 等工具将 `socket=wayland` 的访问添加到白名单解决。 

###  xdg-desktop-portal 无法启动

If you are starting X with [manually-configured run commands](<../zh-cn/Xinit.html#xinitrc> "Xinit"), ensure you are including all essential components of the reference `xinitrc`. One of which sources a script which runs an update of the environment used for D-Bus session services. 
    
    systemctl --user import-environment DISPLAY XAUTHORITY
    if command -v dbus-update-activation-environment >/dev/null 2>&1; then
       dbus-update-activation-environment DISPLAY XAUTHORITY
    fi
    
###  Flatpak 应用没有使用系统默认主题

根据 flatpak 文档，当前不存在理想的为 flatpak 软件应用系统主题的方法[[2]](<https://docs.flatpak.org/en/latest/desktop-integration.html?highlight=theme#applying-themes>) [[3]](<https://docs.flatpak.org/en/latest/desktop-integration.html?highlight=theme#theming>)。最简单的方式是使用 Flathub 中可用的主题。然而，[有办法](<https://web.archive.org/web/20230106121332/https://itsfoss.com/flatpak-app-apply-theme/>)可以将主题应用到 flatpak 软件中，该方法的自动化版本为 [stylepak-git](<https://aur.archlinux.org/packages/stylepak-git/>)AUR。 

###  Flatpak 应用没有使用系统安装的 Fcitx5 皮肤

如果系统从 X11 会话切换至 Wayland 会话，由于环境变量 `QT_IM_MODULE` 和 `GTK_IM_MODULE` 仍被设置为 `fcitx`，可能导致 Flatpak 应用无法加载 Fcitx 5 的主题皮肤。 

**解决方法** ：通过 `flatpak override` 命令为 Flatpak 应用取消设置这两个环境变量。 
    
    $ flatpak override --env=QT_IM_MODULE= --user
    $ flatpak override --env=GTK_IM_MODULE= --user
    
若要应用于全局系统环境，请去掉 `--user` 参数并使用 root 权限执行： 
    
    # flatpak override --env=QT_IM_MODULE=
    # flatpak override --env=GTK_IM_MODULE=
    
执行完毕后，需关闭所有 Flatpak 应用并重新打开以使更改生效。 

详见 Github 相关讨论：[Theme not being applied when used in Flatpak applications](<https://github.com/fcitx/fcitx5/discussions/808>)

###  "File not found" error when Open local HTML pages in Firefox

By default, the Flatpak version of Firefox will display a "File not found" error page when opening a local HTML. This is because [permission must be granted](<#Override_sandbox_permissions_of_applications>) to the app for accessing the folder containing the file. 

However, note that when granting permission to access the entire Home folder, Firefox will then check for an existing profile in `~/.mozilla` and load it instead of those previously in use from the sandboxed folder `~/.var/app/org.mozilla.firefox/cache/mozilla/`. If your previous session's tabs and browsing history is missing after changing a permission (e.g. with Flatseal), either modify the permission to exclude access to `~/.mozilla`, or consider copying the profile from `~/.var/app/org.mozilla.firefox/cache/mozilla/` to `~/.mozilla`. 

### Links fail to open on wlroots-based compositors

Flatpak applications that attempt to open URIs make use of the `org.freedesktop.portal.OpenURI.OpenURI` [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") interface exposed by [xdg-desktop-portal](<../zh-cn/XDG_%E6%A1%8C%E9%9D%A2%E9%97%A8%E6%88%B7.html> "Xdg-desktop-portal"). The [xdg-desktop-portal-wlr backend](<https://github.com/emersion/xdg-desktop-portal-wlr/issues/42>) does not support this call and therefore you will need an additional backend to fill the gap, for example [xdg-desktop-portal-gtk](<https://archlinux.org/packages/?name=xdg-desktop-portal-gtk>)包. 

### Applications do not use the correct cursor theme

There is no single standard to set the cursor properly. Some programs only need read access to the cursors directory, others also rely on other mechanisms. For [GTK](<../zh-cn/GTK.html> "GTK") applications, ensure that [xdg-desktop-portal-gtk](<https://archlinux.org/packages/?name=xdg-desktop-portal-gtk>)包 is installed. 

Otherwise, the following overrides should work for most common desktop applications. 
    
    $ flatpak -u override --filesystem=/usr/share/icons/:ro
    $ flatpak -u override --filesystem=/home/$USER/.icons/:ro
    $ flatpak -u override --filesystem=xdg-config/gtk-3.0:ro
    $ flatpak -u override --env=XCURSOR_PATH=~/.icons
    
In some cases you may also need to override the environment variables `XCURSOR_THEME` and `XCURSOR_SIZE`: 
    
    $ flatpak -u override --env=XCURSOR_THEME=Adwaita
    $ flatpak -u override --env=XCURSOR_SIZE=24
    
See [this discussion](<https://github.com/flatpak/flatpak/issues/709>) for additional details. 

Apparently it is not possible anymore to enable access to applications to directories under `/usr/`. The following hints at this when launching a program: 
    
    $ flatpak run com.spotify.Client
    
    F: Not sharing "/usr/share/icons" with sandbox: Path "/usr" is reserved by Flatpak
    
One possible workaround would be to manually copy your icon theme from `/usr/share/icons` to `/home/$USER/.icons/`. 

### Flatpak Qt applications do not use Gnome Adwaita dark theme

If you switched your theme to Adwaita-dark and Flatpak Qt applications still use the light version, install the required KStyle: 
    
    # flatpak install flathub org.kde.KStyle.Adwaita
    
### Permission denied error when running Flatpak applications

Flatpak applications will not run if the mount point that contains the folder in which the application is stored, typically `/var/lib/flatpak/` for system wide installations, and `~/.local/share/flatpak/` for user-specific installations, is mounted with the `noexec` option. 

With `noexec` set you will get errors such as this: 
    
    $ bwrap: execvp ldconfig: Permission denied
    $ error: ldconfig failed, exit status 256
    
##  参阅

  * [官方网站](<https://flatpak.org>)
  * [官方 Github 维基](<https://github.com/flatpak/flatpak/wiki>)
  * [维基百科页面](<https://zh.wikipedia.org/wiki/Flatpak> "zhwp:Flatpak")
  * [Gnome SandboxedApps](<https://wiki.gnome.org/Projects/SandboxedApps>)
  * [KDE 测试运行时及应用](<https://community.kde.org/Guidelines_and_HOWTOs/Flatpak>)
