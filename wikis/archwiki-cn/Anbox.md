[![](../File:User-trash-full.svg.png)](<../File:User-trash-full.svg.png>)**本文已被弃用。**

**本文所述教程或工具由于已经过时而被弃用，请使用其他替代方案：** [Waydroid](<../zh-cn/Waydroid.html> "Waydroid") 等。 (在[Talk:Anbox](<../zh-cn/Talk:Anbox.html>)讨论)

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 部分内容可能由机器翻译。（在 [Talk:Anbox#](<../zh-cn/Talk:Anbox.html>) 中讨论）

相关文章

  * [Linux 容器](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html> "Linux 容器")

**注意：**[Anbox 已经停止开发](<https://github.com/anbox/anbox/blob/2102e1be999984dbfb25d1ddeaf42179de071020/README.md>)，开发者建议使用 [Waydroid](<../zh-cn/Waydroid.html> "Waydroid") 。

Anbox 是一个可以在 GNU/Linux 发行版上运行 Android App 的一个 [容器](<../zh-cn/Linux_Containers.html> "Linux Containers")。 

##  准备工作

**注意：** Anbox 的 dkms 模块在内核版本 ≥5.7 下不会工作。请按照以下说明进行操作。 对于较老的内核请参阅 [较老的内核](<#%E8%BE%83%E8%80%81%E7%9A%84%E5%86%85%E6%A0%B8>)[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]。

您需要运行带有 ashmem 和 binder 模块的内核。但是它们不是 Arch Linux 的默认内核 ( linux ) 的一部分，所以您需要安装一个包含这些模块的内核。 

您可能还需要配置引导加载程序以使用不同的内核。 

您有多种选择： 

###  使用 Linux-Zen

[linux-zen](<https://archlinux.org/packages/?name=linux-zen>)包 内核自带 Anbox 需要的模块。这可能是最简单的方式，因为您不必编译内核并且版本会定期更新。

**警告：** 根据 linux 内核中的这个[commit](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=721412ed3d819e767cac2b06646bf03aa158aaec>)，从 5.18 开始的版本中 ashmem 被 memfd 取代。 然而，anbox 开发人员并没有修复他们的软件以使用 memfd，因此 anbox 很可能在一段时间内根本无法与 linux-zen 内核一起工作。

###  编译内核

当然，您也可以自己重新编译 [linux](<https://archlinux.org/packages/?name=linux>)包 内核。请阅读 [Kernel#编译](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E7%BC%96%E8%AF%91> "Kernel") and [配置模块](<#%E9%85%8D%E7%BD%AE%E6%A8%A1%E5%9D%97>)。 

您还可以从[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")里构建一个已经包含特定补丁的内核包, 请参阅 [AUR search "linux+anbox"](<https://aur.archlinux.org/packages/?K=linux+anbox>). 

####  配置模块

模块同样也可以被编译进内核里 (`y`), 模块里 (`m`), 或者不编译 (`n`).此外，并非配置中的所有组合都是可能的，某些选项将需要其他选项。 

下面的的内核配置将把 ashmem 和 binder 编译为模块，而最后一个选项指定在 `/dev/` 加载 binder 模块时在目录中创建三个设备。 
    
    CONFIG_ASHMEM=m 
    CONFIG_ANDROID=y
    CONFIG_ANDROID_BINDER_IPC=m
    CONFIG_ANDROID_BINDERFS=n
    CONFIG_ANDROID_BINDER_DEVICES="binder,hwbinder,vndbinder"

如果您要从 AUR 构建内核，那么您可以参考下面的步骤: 

  1. 运行 `makepkg --nobuild`, 它将下载源代码，验证并提取。最后运行 `prepare()` 函数.
  2. 编辑位于内核目录底部的 `.config` 文件。
  3. 在 `prepare()` 函数的末尾可能是一个命令，它使用来自配置的信息重新生成 makefile，也可能是 `make olddefconfig`. 将它移动到 `build()` 函数内，或自己执行一遍。
  4. 运行 `makepkg --noextract`, 它将在 `makepkg --nobuild` 停止的地方继续。

####  使用 binderfs 进行配置

并不是每个人都对 Linux 中的 binder 模块感到满意。为了解决这些问题，binderfs诞生了。编译内核时必须在新旧两种方式之间进行选择。比如下面的选项就是针对于 binderfs 的。 

内核源代码还提供了一个简单的脚本来设置配置选项。它不会进行依赖项检查。当您在 `.config` 文件所在的同一目录中时，执行以下命令: 
    
    scripts/config --module  CONFIG_ASHMEM
    scripts/config --enable  CONFIG_ANDROID
    scripts/config --enable  CONFIG_ANDROID_BINDER_IPC
    scripts/config --enable  CONFIG_ANDROID_BINDERFS
    scripts/config --set-str CONFIG_ANDROID_BINDER_DEVICES ""
    
当您正在从从 AUR 构建内核时，这个脚本很方便，因为只需要在 PKGBUILD 中的正确位置插入这些命令就足够了。 

###  启动新内核

请参阅引导加载程序的 wiki 页面了解如何使用新内核引导。您应该在启动 Anbox 之前切换到新的内核。 

##  安装

###  加载模块

Anbox 不会自动加载模块，但是如果您在使用 linux-zen，就可以跳过此步骤。 

要临时加载，请使用： 
    
    # modprobe -a binder-linux ashmem-linux
    
要始终在启动时加载它们，可以通过 `systemd-modules-load.service` 文件来实现。 为此，请在 `/etc/modules-load.d/` 创建一个包含以下内容的 anbox.conf文件： 
    
    /etc/modules-load.d/anbox.conf
    
    ashmem_linux
    binder_linux
    
###  挂载 binderfs

**注意：** [linux-zen](<https://archlinux.org/packages/?name=linux-zen>)包 内核必须挂载 binderfs。

如果您的内核正在使用 binderfs，则还有一个步骤要做：挂载 binderfs 文件。 

首先，您需要一个挂载点。默认情况下，Anbox 将使用 `/dev/binderfs`。 您可以直接创建该目录，但它会在启动时被删除。所以这里建议使用 [systemd-tmpfiles](<../zh-cn/Systemd.html#systemd-tmpfiles_-_%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6> "Systemd-tmpfiles") 实现在启动时创建 `/dev/binderfs`。为此，您需要在 `/etc/tmpfiles.d/` 创建一个包含以下内容的文件： 
    
    /etc/tmpfiles.d/anbox.conf
    
    d! /dev/binderfs 0755 root root
    
其次您需要挂载 binder 文件系统。 这可以通过： 
    
    # mount -t binder none /dev/binderfs
    
如果想要在启动时挂载它，只需要在 [fstab](<../zh-cn/Fstab.html> "Fstab") 中添加下面这一行。 
    
    /etc/fstab
    
    none                         /dev/binderfs binder   nofail  0      0
    
**警告：** 添加 `nofail` 参数后，当您启动没有 binderfs 支持的内核时，您将无法进入恢复 shell。

##  安装 Android 镜像

**注意：** 现在的镜像均已过时 (基于 Android 7.1). 目前，上游没有可用的更新的镜像。另请参阅 [Talk:Anbox#Anbox-Images outdated](</wzh/index.php?title=Talk:Anbox&action=edit&redlink=1> "Talk:Anbox（页面不存在）").

选择一个镜像来安装: 

  * [anbox-image](<https://aur.archlinux.org/packages/anbox-image/>)AUR (官方镜像)
  * [anbox-image-houdini](<https://aur.archlinux.org/packages/anbox-image-houdini/>)AUR (包含 Houdini)
  * [anbox-image-houdini-rooted](<https://aur.archlinux.org/packages/anbox-image-houdini-rooted/>)AUR (包含 Houdini 和 SuperSU)
  * [anbox-image-gapps](<https://aur.archlinux.org/packages/anbox-image-gapps/>)AUR (包含 Houdini 和 OpenGApps)
  * [anbox-image-gapps-rooted](<https://aur.archlinux.org/packages/anbox-image-gapps-rooted/>)AUR (包含 Houdini, OpenGApps 和 SuperSU)
  * 您也可以通过在 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 内搜索 [anbox-image](<https://aur.archlinux.org/packages/?K=anbox-image>)找到更多的镜像。

**提示：**

  * 通常，在 x86_64 计算机上运行 ARM 应用程序需要 Houdini。
  * 如果您使用 GMS，OpenGApps 是一个不错的选择。

###  安装 Anbox

安装 [anbox-git](<https://aur.archlinux.org/packages/anbox-git/>)AUR。 

然后, [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `anbox-container-manager.service`. 

恭喜您现在已经完成了使用 Anbox 所需的所有步骤！在您的桌面环境菜单中，您应该会在 Others 类别中找到 anbox。 第一次启动将花费很长的时间，anbox session-manager将会被自动打开。当然，您也可以手动执行 `anbox session-manager` 。如果 anbox 崩溃并且您想报告或修复这个错误，这将**非常** 有用。只需启动它，然后等到它崩溃。 

还有一个给用户使用的 _systemd_ unit，可用于在开机时启动 session-manager；如果你想这么干，只需要 [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `anbox-session-manager.service`。该 unit 的一个优点是可以在崩溃时找到日志： 
    
    $ journalctl --user -b -u anbox-session-manager
    
但是请记住，如果您打开一个 Android app 时崩溃崩溃了，它将会再启动一个独立于 _systemed_ 的 session-manager。 

##  网络

###  使用 NetworkManager

如果您正在使用 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") ，则可以使用它来配置网络。 

执行以下命令来创建 bridge connection： 
    
    $ nmcli con add type bridge ifname anbox0 -- connection.id anbox-net ipv4.method shared ipv4.addresses 192.168.250.1/24
    
  * `ifname anbox0` 指定网桥接口名称，在本例中为 `anbox0`. 不要改变这个名称，因为 Anbox 仅会在名为 `anbox0` 的网桥接口。
  * `connection.id anbox-net` 当其运行于 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")时使用 `anbox-net` 这个名称. 你可随愿更改.
  * `ipv4.method shared` 指示 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 来创建一个NAT网络，并根据系统的路由规则对出站数据包进行路由。为此，在 [dnsmasq](<https://archlinux.org/packages/?name=dnsmasq>)包 包完备. [dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq") 不需要配置，也不需要作为systemd服务启动, 其将作为NetworkManager的后端使用——如果它不可用，这一步将无提示地失败。. 如果你想让Anbox直接连接一个特定的网络，你也可以让这一个参数和`ipv4.addresses`参数留空，参见 [Network bridge#With NetworkManager](<../zh-cn/Network_bridge.html#With_NetworkManager> "Network bridge")。如果你想这么做，你还必须把在`anbox-container-manager.service`的容器网络配置修改掉，详见下一个要点。
  * `ipv4.addresses 192.168.250.1/24` specifies the default gateway and subnet of the NAT network. If you wish to change this (e.g. to `192.168.42.1/24`) you must also indicate the new subnet to anbox in the `anbox-container-manager.service` using: `--container-network-address=192.168.42.2/24 --container-network-gateway=192.168.42.1`

[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 将在每次重新启动时自动设置桥接，因此您只需要执行一次命令。 

### Via systemd-networkd

The package [anbox-git](<https://aur.archlinux.org/packages/anbox-git/>)AUR provides configuration files for `systemd-networkd` in `/usr/lib/systemd/network/` to enable networking in anbox. 

Therefore, you can [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `systemd-networkd` before starting `anbox-container-manager.service`. 

### Via anbox-bridge script

Alternatively you can use the anbox-bridge script [used by the project](<https://raw.githubusercontent.com/anbox/anbox/master/scripts/anbox-bridge.sh>). 

You must execute `anbox-bridge` every time before starting `anbox-container-manager.service` in order to get network working in Anbox. The easiest solution for that is to create a drop-in file for the service. 
    
    /etc/systemd/system/anbox-container-manager.service.d/enable-anbox-bridge.conf
    
    [Service]
    ExecStartPre=/usr/bin/anbox-bridge start
    ExecStopPost=/usr/bin/anbox-bridge stop

## Usage

You can run the Android applications on your desktop's launcher on **Other** category. 

If you want to use [adb](<../zh-cn/Android_%E8%B0%83%E8%AF%95%E6%A1%A5.html> "Adb") to debug, install [android-tools](<https://archlinux.org/packages/?name=android-tools>)包. The `anbox session-manager` must already be running when launching it. 
    
    $ adb shell
    
###  安装应用

除非你用 Houdini 挑选了一个镜像, 否则 Anbox 不支持 ARM 应用. 所以应用必须是 x86_64 架构. 

####  通过 adb

安装 `_/path/to/app.apk_`
    
    $ adb install _/path/to/app.apk_
    
获取已经安装的应用列表 
    
    $ adb shell pm list packages
    
注意：输出会与 `_package:app.name_` 相似, 此 `_app.name_` 会与Anbox容器内显示的不同。 

卸载 `_app.name_`
    
    $ adb uninstall _app.name_
    
如果 `_app.name_` 是一个系统应用 
    
    $ adb uninstall --user 0 _app.name_
    
####  通过应用商店

应用商店可以轻松安装应用，包括 [anbox-image-gapps](<https://aur.archlinux.org/packages/anbox-image-gapps/>)AUR PlayStore商店. 

### Sensor data

Via dbus different sensors can be set. Documentation on that can be found at [dbus.md](<https://github.com/anbox/anbox/blob/master/docs/dbus.md>). 

#### Temperature data

That is the example from the author (PRs [#1522](<https://github.com/anbox/anbox/pull/1522>) & [#1540](<https://github.com/anbox/anbox/pull/1522>)): 
    
    $ dbus-send --session --dest=org.anbox --print-reply /org/anbox org.freedesktop.DBus.Properties.Set string:org.anbox.Sensors string:Temperature variant:double:25.1
    
#### GPS data

(introduced by PR [#1606](<https://github.com/anbox/anbox/pull/1606>)) 

GPS sensor data can also be manipulated. 

If your PC has a WWAN card, you can use [gpsd](<https://archlinux.org/packages/?name=gpsd>)包 and the code from the PR to feed Anbox with GPS data. You do not need to have a SIM-Card for GPS. 

Otherwise, you can also look at the PR to learn how to feed it fake data with the help of [[1]](<https://www.nmeagen.org>). 

### Root shell

With this [script](<https://github.com/anbox/anbox/blob/master/scripts/anbox-shell.sh>) from the Anbox project one can get a root shell inside the Android container. 

It is not part of the [anbox-git](<https://aur.archlinux.org/packages/anbox-git/>)AUR package, and it also does not use [adb](<../zh-cn/Android_%E8%B0%83%E8%AF%95%E6%A1%A5.html> "Adb"). 

## Tips and tricks

### Android developer options

Some extra steps need to be done besides unlocking them the same way you do on an android phone. When installing the [android image](<#Install_Android_Image>)[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节], some modifications to `products/anbox.xml` are required: 

  * `<unavailable-feature name="android.hardware.usb.host" />` is the reason why they are not available.
  * `<feature name="android.software.backup" />` will be needed too, to avoid a NullPointerException.

(reference: [Github issue #444](<https://github.com/anbox/anbox/issues/444>)) 

### Getting debugging information

Obviously, it is helpful to have debugging symbols in the Anbox build. For that, when [compiling Anbox](<#Install_Anbox>)[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节], add `options=('!strip')` to the PKGBUILD, as by default they are removed. And, use either `-DCMAKE_BUILD_TYPE=RelWithDebInfo` or `-DCMAKE_BUILD_TYPE=Debug` in the cmake call. 

But there is more to it! Anbox uses [backward-cpp](<https://github.com/anbox/anbox/tree/master/external/backward-cpp>). If you do not delete the build files for Anbox, it will print pretty stack traces when crashing, which point out the places in the source code. 

Also see the remarks in [Install Anbox](<#Install_Anbox>)[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]. 

## Troubleshooting

If you run into issues, take a look at the official Issue Tracker: [[2]](<https://github.com/anbox/anbox/issues>)

### Old CPUs

Anbox requires support for SSE 4.1/4.2 and SSSE 3, because Android wants that too. Some older CPUs do not provide that, so you probably cannot use Anbox, see: [Anbox Github Issue 499](<https://github.com/anbox/anbox/issues/499#issuecomment-399118684>). 

### Old kernels

Before the kernel modules were mainlined, they were out of tree modules, which needed to be installed seperately from the kernel (Like it is the case for the nvidia kernel modules). They are not compatible with kernel 5.7 or newer. 

It is still possible to use that approach with the [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 or other old kernels. The package to install the modules via [DKMS](<../zh-cn/DKMS.html> "DKMS") is not available in the AUR anymore, but can be retrieved with `git clone https://aur.archlinux.org/anbox-modules-dkms`, or resurected from [[3]](<https://aur.archlinux.org/cgit/aur.git/commit/?h=anbox-git&id=0c9a9385694e680f5b277ca6f9326ad5d5df7dd3>). 

### Secure Boot error

If you get this error message: 
    
    modprobe: ERROR: could not insert 'ashmem_linux': Operation not permitted
    
[Secure Boot](<../zh-cn/Secure_Boot.html> "Secure Boot") is likely blocking the module. You can either disable Secure Boot or sign the ashmem module yourself. 

More info can be found in the [Anbox Github Docs](<https://github.com/anbox/anbox/blob/master/docs/install.md#on-ubuntu-1904-and-later>). 

## See also

  * [Official Anbox Github Repo](<https://github.com/anbox/anbox>)
  * [Anbox Website](<https://anbox.io/>)
  * [Posting by the main Anbox developer](<https://mm.gravedo.de/blog/posts/2020-01-21-taking-the-anbox-journey-to-the-next-level>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ]
  * [Explanation about binderfs](<https://brauner.github.io/2019/01/09/android-binderfs.html>)
