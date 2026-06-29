**翻译状态：**

  * 本文（或部分内容）译自 [Waydroid](<https://wiki.archlinux.org/title/Waydroid> "arch:Waydroid")，最近一次同步于 2025-11-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/Waydroid?diff=0&oldid=851480>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Waydroid_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Linux 容器](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html> "Linux 容器")

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 需要改进文章风格。（在[Talk:Waydroid](<../zh-cn/Talk:Waydroid.html>)讨论）

[Waydroid](<https://waydro.id>) 是一种基于容器的、能在常规的 Linux 系统上启动完整 Android 系统的方法。 

##  准备工作

###  CPU 要求

CPU 要求取决于 CPU 架构。更多信息可参阅[此表格](<https://developer.android.com/ndk/guides/abis#sa>)。 

可以使用 `cat /proc/cpuinfo` 检查是否具备所需的 CPU 指令集。 

###  GPU 要求

Waydroid 目前最适合在 Intel GPU 上使用（可开箱即用）。 

已支持所有 AMD GPU；如果 Waydroid 不工作，您可能需要构建一个新的 Waydroid 映像（在 Radeon 680M 上正常工作），或者尝试以下有关 NVIDIA 的说明。 

NVIDIA GPU 目前不被支持。有两种解决方法： 

  1. 可能的话，切换到集成显卡
  2. 使用软件渲染（参见[#软件渲染](<#%E8%BD%AF%E4%BB%B6%E6%B8%B2%E6%9F%93>)）

###  Wayland 会话管理器

Waydroid 只在 [Wayland](<../zh-cn/Wayland.html> "Wayland") 会话管理器中工作，因此请确保您处于 Wayland 会话中。 

请注意，即使处于 X11 会话中，许多 Wayland 会话管理器也支持嵌套会话，因此可以在 X11 会话中运行 Waydroid（最简单的例子是 [cage](<https://archlinux.org/packages/?name=cage>)包）。 

###  内核模块

需要运行包含 binder 模块的内核，[linux](<https://archlinux.org/packages/?name=linux>)包、[linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包、[linux-zen](<https://archlinux.org/packages/?name=linux-zen>)包 和 [linux-lily](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/linux-lily>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")均包含该模块。若您使用不同的[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")，则可能需要重新编译或通过 DKMS 安装 。 

####  DKMS 模块

安装 [binder_linux-dkms](<https://aur.archlinux.org/packages/binder_linux-dkms/>)AUR 并使用 `devices=binder,hwbinder,vndbinder` 内核选项加载 `binder_linux` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")（参见 [bug 报告](<https://github.com/waydroid/waydroid/issues/904#issuecomment-1869579022>)）。 
    
    # modprobe binder-linux devices=binder,hwbinder,vndbinder
    
此外，您也可以通过在 `/etc/modules-load.d/` 和 `/etc/modprobe.d/` 创建配置文件来让 `binder_linux` 在启动时被加载（这是可选的，参阅[内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")以获取更多信息）。 
    
    /etc/modules-load.d/binder_linux.conf
    
    # Load binder_linux at boot
    binder_linux
    
    /etc/modprobe.d/binder_linux.conf
    
    # Options for binder_linux
    options binder_linux devices=binder,hwbinder,vndbinder
    
您还需要使用 `ibt=off` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")来解决 5.18+ 版本内核上的一个问题，参阅 [Segmentation fault when mounting `/dev/binderfs`](<https://bbs.archlinux.org/viewtopic.php?id=293566>)

####  构建内核

另外，可以用必要的选项重新编译 [linux](<https://archlinux.org/packages/?name=linux>)包 内核——或者其他内核版本 (>=5.7)。参见[内核#编译](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E7%BC%96%E8%AF%91> "内核")。 

当构建一个最小内核时，请遵循以下需求： 

  * IPv6 支持：若内核没有构建 IPV6，Waydroid 会没有 IPv4 连接。
  * Netlink 套接字 （`CONFIG_NF_CT_NETLINK=y`）。
  * PSI （`CONFIG_PSI=y`）。
  * Loop block 设备 （`CONFIG_BLK_DEV_LOOP=m`）：`loop` 模块必须在 Waydroid 启动前被加载。

当设置编译选项时，有两个选项： _binder_ 和 _binderfs_ 。下面提供了有关这两者的说明。 

#####  使用 binder

模块既可以被编译到内核中 (`y`)，也可以被编译到模块中 (`m`)，或者不编译 (`n`) 。此外，配置中的选项不能任意组合，有些选项依赖于其他选项。 

以下配置选项会将 binder 编译成模块，与此同时最后一个选项指定了在 binder 模块加载时，将在 `/dev/` 目录下创建 3 个设备。
    
    CONFIG_ANDROID=y
    CONFIG_ANDROID_BINDER_IPC=m
    CONFIG_ANDROID_BINDERFS=n
    CONFIG_ANDROID_BINDER_DEVICES="binder,hwbinder,vndbinder"

当从 AUR 构建内核时，可以按照以下步骤更新配置： 

  1. 执行 `makepkg --nobuild`，将会下载源代码、验证并解压源代码包，然后执行 `prepare()` 函数。
  2. 编辑位于内核根目录下的 `.config` 文件 (注意文件名里的点)。
  3. 在 `prepare()` 函数尾部的命令很可能被用于从配置文件信息重新生成 Makefile (可能是 `make olddefconfig`) 。将这条命令移动到 `build()` 函数里，或者单独执行。
  4. 执行 `makepkg --noextract`，将自动从 `makepkg --nobuild` 停下的位置继续执行。

#####  使用 binderfs

已知 binder 内核模块会给部分用户造成一些问题。为了解决这些问题，binderfs 应运而生。编译内核时，必须要在新旧方式之间做出选择。使用以下选项，可以使用 binderfs 来替代 binder。 

内核源代码也附带了用于设置配置选项的简单脚本。此脚本不会做依赖检查，就像手动编辑配置文件一样。当与 `.config` 处于相同目录时，可以执行以下命令：
    
    $ scripts/config --enable  CONFIG_ANDROID
    $ scripts/config --enable  CONFIG_ANDROID_BINDER_IPC
    $ scripts/config --enable  CONFIG_ANDROID_BINDERFS
    $ scripts/config --set-str CONFIG_ANDROID_BINDER_DEVICES ""
    
当从 AUR 构建内核时，将这几行插入到 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 中的合适位置即可 (通常在 `prepare()` 中) 。 

####  设置 binder 设备

确保已经安装 Waydroid 软件包的最新版本。Waydroid 将自动处理此问题。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [waydroid](<https://archlinux.org/packages/?name=waydroid>)包 软件包。 

可以选择通过 AUR 安装 [waydroid-image](<https://aur.archlinux.org/packages/waydroid-image/>)AUR 或 [waydroid-image-gapps](<https://aur.archlinux.org/packages/waydroid-image-gapps/>)AUR 来提供所需的 Android 映像。然而，让 Waydroid 自己下载映像是更推荐的做法。 

**提示：** 中国用户可能会下载映像极为缓慢，可以通过添加 [archlinuxcn](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Archlinuxcn") 仓库之中国大陆镜像后安装 [waydroid-image](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/waydroid-image>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")，这可以显著提高下载速度。

在初始化 Waydroid 之后，如果映像不可用，将会自动下载最新的 Android 映像（可能会耗时很久；你也可以自行下载之后将文件放到 `/etc/waydroid-extra/images/`[[1]](<https://docs.waydro.id/faq/using-custom-waydroid-images>)）。 
    
    # waydroid init
    
初始化支持 GApps 的 Waydroid： 
    
    # waydroid init -s GAPPS
    
接下来[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `waydroid-container.service`。 
    
    # systemctl enable --now waydroid-container
    
Waydroid 现在应该能正常工作了。 

##  用法

确保 `waydroid-container.service` 已[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")，然后执行： 
    
    $ waydroid session start
    
Waydroid 会话现在已处于活动状态，以下是一些与 Waydroid 交互的实用命令： 

启动 GUI： 
    
    $ waydroid show-full-ui
    
启动 shell： 
    
    # waydroid shell
    
安装应用程序： 
    
    $ waydroid app install $path_to_apk
    
运行应用程序： 
    
    $ waydroid app launch $package-name
    
**注意：**`$package_name` 是 list 命令所示的 `packageName`（包名）属性，并非 `Name`（应用名称）属性。

获取应用程序列表： 
    
    $ waydroid app list
    
##  网络

网络应该开箱即用，否则可能需要确保在执行 `waydroid session start` 之前，内核中已启用[包转发](<../zh-cn/%E7%BD%91%E7%BB%9C%E5%88%86%E4%BA%AB.html#%E5%90%AF%E7%94%A8%E5%8C%85%E8%BD%AC%E5%8F%91> "网络分享")并且允许以下规则通过防火墙： 

以 [ufw](<https://archlinux.org/packages/?name=ufw>)包 为例： 

  * 允许 DNS 流量： 
    * # ufw allow 67

    * # ufw allow 53

  * 允许包转发： 
    * # ufw default allow FORWARD

对于 [firewalld](<https://archlinux.org/packages/?name=firewalld>)包, 可以使用这些命令： 

  * DNS： 
    * # firewall-cmd --zone=trusted --add-port=67/udp

    * # firewall-cmd --zone=trusted --add-port=53/udp

  * 包转发： 
    * # firewall-cmd --zone=trusted --add-forward

**注意：** Waydroid 可能默认使用 nftables 作为流量转发工具，如果没有开启该服务，记得把 `/usr/lib/waydroid/data/scripts/waydroid-net.sh` 文件中的 `LXC_USE_NFT` 设置为 `false`，否则会出现ip分配正确，但是流量发送出去但是转发不回来的现象。

**注意：** 请确保在运行 `waydroid-container.service` 前没有启用 TUN Proxy，避免导致错误的网络设置；在启动后可以启用。

  * 将 waydroid 接口添加为可信： 
    * # firewall-cmd --zone=trusted --add-interface=waydroid0

**注意：** 正常情况下，Waydroid 创建的接口应该自动位于 firewalld 区域 `trusted` 内。如果不是这样，请调整上述命令，或将 `waydroid0` 移动到 `trusted`。为了使重新启动时能保留更改，可能还需要执行以下命令：
    
    # firewall-cmd --runtime-to-permanent

##  提示和技巧

###  在桌面环境中整合窗口

Waydroid 默认全屏运行，若您想让 Waydroid 上的应用与您的桌面环境实现窗口整合（即应用拥有独立的窗口而不影响其他 Linux 应用窗口），请先启动 Waydroid 会话： 
    
    $ waydroid session start
    
然后设定所需属性： 
    
    $ waydroid prop set persist.waydroid.multi_windows true
    
重启会话： 
    
    $ waydroid session stop
    $ waydroid session start
    
现在应用可以在其独立的窗口中运行了。另请参阅[Waydroid 官方文档](<https://docs.waydro.id/usage/install-on-desktops#launch-waydroid-in-multi-window-mode>)。 

###  软件渲染

确保您已经执行： 
    
    # waydroid init
    
（参阅[#安装](<#%E5%AE%89%E8%A3%85>)章节以获取更多信息） 

接下来，向 `waydroid.cfg` 添加以下内容： 
    
    /var/lib/waydroid/waydroid.cfg
    
    [properties]
    ro.hardware.gralloc=default
    ro.hardware.egl=swiftshader

然后执行以下命令以应用配置： 
    
    # waydroid upgrade --offline
    
最后，[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `waydroid-container.service`。 

###  调整视图尺寸

用以下命令将 Waydroid 窗口尺寸调整到您喜欢的大小： 
    
    $ waydroid prop set persist.waydroid.width 576
    $ waydroid prop set persist.waydroid.height 1024
    
然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `waydroid-container.service`。 

##  故障排除

如果您遇到了问题，可参见官方的问题跟踪：[Waydroid 问题跟踪](<https://github.com/waydroid/waydroid/issues>)

###  一般建议

Waydroid 正在快速发展中，因此如果您遇到问题，这里有一系列值得尝试的步骤： 

  1. 确保 Waydroid 软件包处于最新。
  2. 通过执行以下命令，确保已安装最新的 Waydroid 映像：
         
         # waydroid upgrade

  3. 重置 Waydroid：[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止") `waydroid-container.service`，执行 
         
         # waydroid init -f

并重新[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")服务。
  4. 可能还需要做一下简单的清理，执行以下命令： 
         
         # rm -rf /var/lib/waydroid /home/.waydroid
         
         $ rm -rf ~/waydroid ~/.share/waydroid ~/.local/share/applications/*aydroid* ~/.local/share/waydroid

**提示：** 如果您是在 [2021-09](<https://github.com/waydroid/waydroid/commit/eef036b3f814a9fc4869ebfe6c9d2bd51fa19f26>) 后安装，那么您不必移除 `/home/.waydroid/`。

###  不兼容 ARM 应用

使用 casualsnek 的 [waydroid-script-git](<https://aur.archlinux.org/packages/waydroid-script-git/>)AUR 或 [waydroid-helper](<https://aur.archlinux.org/packages/waydroid-helper/>)AUR 安装翻译层。 

为提高翻译性能，推荐在 AMD CPU 上使用 libndk，在英特尔 CPU 上使用 libhoudini。然而部分应用仅支持一种翻译层，因此当某个游戏不工作或性能极差时，您可能需要把两个翻译层都试一遍。 

_安装 libndk arm 翻译层_
    
    # waydroid-extras install libndk 
    
_安装 libhoudini arm 翻译层_
    
    # waydroid-extras install libhoudini
    
###  旋转的应用程序无法使用

参见 [[2]](<https://github.com/waydroid/waydroid/issues/70>)。 

按 _F11_ 可将当前应用切换到窗口模式。 

###  无法启动剪贴板管理服务

安装 [python-pyclip](<https://archlinux.org/packages/?name=python-pyclip>)包 及其依赖（为 X11 安装 [xclip](<https://archlinux.org/packages/?name=xclip>)包，为 Wayland 安装 [wl-clipboard](<https://archlinux.org/packages/?name=wl-clipboard>)包）。 

###  无法使用物理键盘

按 _左 Alt_ 键。 

###  **dnsmasq: failed to open pidfile /run/waydroid-lxc/dnsmasq.pid: Permission denied**

没有设置 apparmor 规则，在 `/etc/apparmor.d/usr.sbin.dnsmasq` 的末尾添加 
    
    #/etc/apparmor.d/usr.sbin.dnsmasq
    
    @{run}/waydroid-lxc/ r,
    @{run}/waydroid-lxc/* rw, 

###  Waydroid shell 中的命令输出无法访问或命令未找到

在基于 Arch 的发行版上，[使用 lxc-attach 时可能会出现一个 "bug"](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html#%E5%9F%BA%E6%9C%AC%E7%94%A8%E6%B3%95> "Linux 容器")，可能会导致 `waydroid shell` 内的命令出现此问题，如 `adbd` 或 `settings`。 

一个可能的解决方案是用 
    
    # lxc-attach -P /var/lib/waydroid/lxc/ -n waydroid --clear-env

替代 `# waydroid shell` 。 

###  WARNING: Service manager /dev/binder has died

参见 [Issue 136](<https://github.com/waydroid/waydroid/issues/136>)。 

启用 [PSI](<https://docs.kernel.org/accounting/psi.html>)，在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中添加 `psi=1`。 

若启用 PSI 未能修复改错误，则很有可能是因为禁用了 ia32 模拟。请尝试执行以下命令以启用 ia32 vdso： 
    
    # echo 1 > /proc/sys/abi/vsyscall32
    
请注意 [Waydroid 不在 Liquorix 内核上工作](<https://github.com/damentz/liquorix-package/commit/2dd0b878dbd27bdc5e796a7bd7384676df9e6764>)，因为其使用的某些调度器不兼容 PSI。 

###  多 GPU 系统上图形损坏

目前 Waydroid 需要与其窗口混成器运行在同一 GPU 上。有两种方法修复，一种是编辑 `/var/lib/waydroid/lxc/waydroid/config_nodes`，选择合适的 GPU，另一种是让窗口混成器切换 GPU。 

可以使用一个[脚本](<https://raw.githubusercontent.com/Quackdoc/waydroid-scripts/refs/heads/main/waydroid-choose-gpu.sh>)来快速选择 GPU。 

###  无网络连接

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 本小节需要更深入解释为什么有冲突。 (在 [Talk:Waydroid](<../zh-cn/Talk:Waydroid.html>) 中讨论)

根据 [waydroid/issue/509](<https://github.com/waydroid/waydroid/issues/509>)，Waydroid 与 docker 存在 nftable 冲突。 

欲修复，请关闭 `LXC_USE_NFT`： 
    
    /usr/lib/waydroid/data/scripts/waydroid-net.sh
    
    LXC_USE_NFT="false"

或执行以下命令： 
    
    # systemctl stop docker
    # systemctl restart iptables
    # ip link delete docker0
    # systemctl restart waydroid-container
    
部分[用户报告](<https://github.com/waydroid/waydroid/issues/143>)称该以上方法不足以解决问题，因为禁用 LXC_USE_NFT 使得脚本回落到使用 iptables-legacy，而其工作效果不佳。 

[此评论](<https://github.com/waydroid/waydroid/issues/143#issuecomment-1520857943>)建议执行以下命令以使用 iptables： 
    
    # sed -i~ -E 's/=.\$\(command -v (nft|ip6?tables-legacy).*/=/g' \
        /usr/lib/waydroid/data/scripts/waydroid-net.sh
    
###  该设备未通过 Play Protect 认证

参阅[官方文档](<https://docs.waydro.id/faq/google-play-certification>)。 若您收到该错误，请进入 waydroid shell 并检索 Android ID： 
    
    # waydroid shell
    # ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";"
    
之后将 ID 输入这个网站：<https://www.google.com/android/uncertified> 稍等几分钟后重启 Waydroid。 

###  无法输入中文

默认的安卓系统不包括中文输入法。在容器内部安装一个中文输入法即可。 

###  Waydroid 挂起

可能是由于音频服务器死机，请参阅 [Issue 576](<https://github.com/waydroid/waydroid/issues/576>) 和 [Issue 829](<https://github.com/waydroid/waydroid/issues/829>) 以获取详细信息。 

一种方法是运行： 
    
    # sysctl -w kernel.pid_max=65535 
    
要使其持久化，请在 `/etc/sysctl.d/` 创建一个 `.conf` 文件，并向其添加 `kernel.pid_max=65535`。 
    
    /etc/sysctl.d/99-sysctl.conf
    
    kernel.pid_max=65535

###  应用程序需要未 root 的设备

根据 [Issue 1060](<https://github.com/waydroid/waydroid/issues/1060#issuecomment-1732325955>)，添加以下内容可以通过 root 检测： 
    
    /var/lib/waydroid/waydroid.cfg
    
    [properties]
    ro.product.brand=google
    ro.product.manufacturer=Google
    ro.system.build.product=redfin
    ro.product.name=redfin
    ro.product.device=redfin
    ro.product.model=Pixel 5
    ro.system.build.flavor=redfin-user
    ro.build.fingerprint=google/redfin/redfin:11/RQ3A.211001.001/eng.electr.20230318.111310:user/release-keys
    ro.system.build.description=redfin-user 11 RQ3A.211001.001 eng.electr.20230318.111310 release-keys
    ro.bootimage.build.fingerprint=google/redfin/redfin:11/RQ3A.211001.001/eng.electr.20230318.111310:user/release-keys
    ro.build.display.id=google/redfin/redfin:11/RQ3A.211001.001/eng.electr.20230318.111310:user/release-keys
    ro.build.tags=release-keys
    ro.build.description=redfin-user 11 RQ3A.211001.001 eng.electr.20230318.111310 release-keys
    ro.vendor.build.fingerprint=google/redfin/redfin:11/RQ3A.211001.001/eng.electr.20230318.111310:user/release-keys
    ro.vendor.build.id=RQ3A.211001.001
    ro.vendor.build.tags=release-keys
    ro.vendor.build.type=user
    ro.odm.build.tags=release-keys

然后使用以下命令以应用配置： 
    
    waydroid upgrade --offline
    
##  另请参阅

  * [Waydroid GitHub 仓库](<https://github.com/waydroid/waydroid>)
  * [Waydroid 文档](<https://docs.waydro.id/>) (English)
  * [Waydroid Matrix 用户组](<https://matrix.to/#/#waydroid:connolly.tech>)
  * [Waydroid Telegram 用户组](<https://t.me/WayDroid>)
