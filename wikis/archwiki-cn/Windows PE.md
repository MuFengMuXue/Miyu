**翻译状态：**

  * 本文（或部分内容）译自 [Windows PE](<https://wiki.archlinux.org/title/Windows_PE> "arch:Windows PE")，最近一次同步于 2021-08-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Windows_PE?diff=0&oldid=662585>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Windows_PE_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 翻译已经过期，请阅读英文页面中的内容。（在 Prepare a bootable Windows PE ISO 中有较大修改。）（在 [Talk:Windows PE#](<../zh-cn/Talk:Windows_PE.html>) 中讨论）

[Windows PE](<https://technet.microsoft.com/en-us/library/cc766093\(v=ws.10\).aspx>) 是 Windows 的轻量级版本，旨在用于安装 Windows Vista 或更高版本的 Windows，或是用于系统维护。它完全运行在内存中，并可以从网络启动。本页面描述了如何创建定制化的 Windows PE 镜像文件（也可选择发布在网络上的），我们只需用到 Arch Linux 设备上的自由软件包和微软 Windows 自动安装工具包（Microsoft's Windows Automated Installation Kit，简称 WAIK）。WAIK 可以免费下载，并且我们只需解压其中的 `boot.wim` 文件，该文件包含了 Windows PE 的最初备份, 还有一些启动文件。 

**警告：** 下载 Windows Automated Installation Kit 时, 您可能会受到其许可的约束，这会阻止您将 Windows PE 用作通用操作系统。

##  使用场合

通常，只能使用 Windows 计算机上的 Windows 自动安装工具包 (WAIK) 创建 Windows PE 的映像。但是，也可以使用 (Arch) Linux 机器创建和修改 Windows PE 的映像，并可选择将它们发布到网络上以进行 PXE 引导。不使用 Windows 机器是可能的。在以下情况出现时，您可能想要这样做： 

  * 您需要使用 Arch Linux 的服务器从网络安装 Windows ，或者从网络启动 Windows PE 来进行系统管理。这样做可能是因为您没有基于 Windows 的服务器，或者因为绝佳的安全性和可配置特性就是喜欢用 Linux 服务器，又或是您因为别的原因已经拥有了一台 Linux 服务器。
  * 您需要在 Windows 环境下运行 Win32 应用程序，但您并没有可用的 Windows 设备，也不想用 [Wine](<../zh-cn/Wine.html> "Wine") 或者您的程序在 [Wine](<../zh-cn/Wine.html> "Wine") 下没有正确执行。

##  创建可启动的 Windows PE 镜像

安装 [wimlib](<https://archlinux.org/packages/?name=wimlib>)包. 

###  配置 Windows PE 镜像

要启动到命令提示符，请创建一个启动脚本，该脚本将包含在下一步的可启动映像中： 
    
    start.cmd
    
    cmd.exe
    pause
    
`mkwinpeimg` 脚本支持使用 `--overlay` 选项对 Windows PE 进行进一步修改。 有关 `mkwinpeimg` 的更多信息，请参阅它的手册页。您可能希望这样做以添加要在 Windows PE 中运行的 Windows 应用程序或者额外的驱动程序。(可以用 Windows PE 中的命令 `drvload` 加载所需的驱动程序). 

###  获取 Windows ISO 或 WAIK 镜像

`mkwinpeimg` 可以从各种来源创建可启动的 Windows PE ISO。您首先需要获得： 

  * **选项 A** （适用于 Windows 7 及更高版本）: Windows 安装镜像ISO文件。它可以在微软网站上免费下载： [Windows 10 ISO](<https://www.microsoft.com/zh-cn/software-download/windows10ISO>). 这是最简单的方法。
  * **选项 B** : Windows自动安装工具包镜像 (WAIK) 文件。 对于 Windows Vista/7, 它可以在此处下载：[一个单独的 WAIK 发行版](<https://www.microsoft.com/zh-cn/download/details.aspx?id=5753>). 从 Windows 8 开始, WAIK 被重命名为 WADK 并通过 `adksetup.exe` 分发。

**警告：** 确保根据您的实际需要选择正确的目标架构: x86 (32 位) 或 x64 (64 位)。在 x64 版 Windows PE 上运行 x86 程序并没有那么简单。

不同版本的 Windows 安装介质包含不同版本的 Windows PE。Windows 版本和 Windows PE 版本之间的关系，请参考[维基百科](<https://en.wikipedia.org/wiki/Windows_Preinstallation_Environment#Versions> "wikipedia:Windows Preinstallation Environment"). 

**提示：** 也许可以使用 [httpfs](<https://httpfs.sourceforge.net/>) 来避免下载整个镜像文件。Windows PE 只占其中的 118MB。 

###  准备可启动的 Windows PE ISO

成功获取 Windows 安装镜像或者 WAIK/WADK 镜像后，你需要挂载它。假设它叫做 `winimg.iso`: 
    
    # mkdir /media/winimg
    # mount winimg.iso /media/winimg
    
使用 [wimlib](<https://archlinux.org/packages/?name=wimlib>)包 提供的 `mkwinpeimg` 脚本创建可启动的 Windows PE ISO 文件 `winpe.iso`, 启动脚本在上一节中已经创建: 

**选项 A** : 源镜像是 Windows 安装介质 
    
    $ mkwinpeimg --iso --windows-dir=/media/winimg --start-script=start.cmd winpe.iso
    
**选项 B** : 源镜像是 WAIK/WADK 
    
    $ mkwinpeimg --iso --waik-dir=/media/winimg --start-script=start.cmd winpe.iso
    
有关更多信息，请参阅 [mkwinpeimg(1)](<https://man.archlinux.org/man/mkwinpeimg.1>), 包含 `--overlay` 选项以把文件复制到镜像中。 

卸载源 ISO: 
    
    # umount /media/winimg
    
###  为 UEFI 系统准备 Windows PE 启动U盘

不幸的是，从 1.13.1-1 版的 [wimlib](<https://archlinux.org/packages/?name=wimlib>)包 开始，`mkwinpeimg` 无法构建可引导的 UEFI 系统，但是我们依然可以构建包含必要的 UEFI 启动文件的 Windows 10 安装 ISO。 

**警告：** 确保为 Windows ISO 映像（x86 或 x64）选择了合适的体系结构。本指南仅在 x64 上进行过测试，即它使用 `/efi/boot/bootx64.efi`。能否以这种方式启动 Windows 的 x86 映像尚不得而知。如果您可以测试，请更新此页面。

在启动盘上, 创建一个 GPT 分区表，其中包含一个类型为“EFI System”的 FAT32 分区。这可以通过 `cfdisk` 或 fdisk 交互式地完成，比如使用 fdisk : 
    
    # fdisk /dev/sdX
    (fdisk) g  # 建立新的 GPT 分区表
    (fdisk) n  # 使用默认设置创建新分区
    (fdisk) t  # 修改分区类型
    (fdisk) 1  # 类型 1 表示 "EFI System Partition"
    (fdisk) w  # 保存并退出
    
然后把此分区格式化为 FAT32: 
    
    # mkfs.vfat /dev/sdX1
    
挂载由 `mkwinpeimg` 创建的 `winpe.iso` 文件，挂载你的启动盘, 复制以下内容: 
    
    # mkdir /media/{winpe,usb}
    # mount winpe.iso /media/winpe
    # mount /dev/sdX1 /media/usb
    # cp -r /media/winpe/* /media/usb/
    
最后，挂载原始 Windows ISO 文件并复制 `efi` 中的所有文件: 
    
    # mount winimg.iso /media/winimg
    # cp -r /media/winimg/efi /media/usb/
    
现在，你可以卸载所有 ISO 和启动盘，你的启动盘已经准备就绪。 

**注意：** 不需要 syslinux 或 grub magic。UEFI 固件会找到 FAT 分区并加载 Windows 提供的 `/efi/boot/bootx64.efi` 引导文件。

##  引导启动 Windows PE

按照上一节所述创建可启动的 Windows PE ISO (`winpe.iso`) 之后，你也许想通过如下几种方式引导启动 Windows PE 。 

###  在虚拟机中

在虚拟机中运行 `winpe.iso` 作为 CD-ROM。确保分配了足够的内存，绝对要大于 ISO 文件的大小，因为 Windows PE 是从内存启动的。 

###  使用启动盘

如果你已经如前文所述为 UEFI 系统准备好了启动盘，你只需从启动盘启动即可。启动过程可能需要耗费一些时间（10至20秒是正常的，具体取决于启动盘的读取速度），因为加载程序需要把数据复制到内存中。 

###  使用光盘

只需把 `winpe.iso` [烧录](<../zh-cn/%E5%85%89%E7%9B%98%E9%A9%B1%E5%8A%A8%E5%99%A8.html#%E5%88%BB%E5%BD%95> "光盘驱动器")到光盘上，就可以从该光盘启动 Windows PE。 

###  从网络启动

在 BIOS 系统中，Windows PE 可以从网络启动，通过 [PXELINUX](<https://wiki.syslinux.org/wiki/index.php/PXELINUX>) 和它的 [MEMDISK](<https://wiki.syslinux.org/wiki/index.php/MEMDISK>) 模块。对于 UEFI 系统,可以使用 [wimboot](<http://ipxe.org/wimboot>) 和 [iPXE](<https://ipxe.org>)。 

安装 [syslinux](<https://archlinux.org/packages/?name=syslinux>)包 和 [tftp-hpa](<https://archlinux.org/packages/?name=tftp-hpa>)包。 

复制需要的 PXELINUX 文件到 [TFTP server](</wzh/index.php?title=Tftpd_server&action=edit&redlink=1> "Tftpd server（页面不存在）") 的根目录。 
    
    # rsync -aq /usr/lib/syslinux/bios/ /var/tftpboot/
    
把 `winpe.iso` 文件放进 [TFTP server](</wzh/index.php?title=Tftpd_server&action=edit&redlink=1> "Tftpd server（页面不存在）") 的根目录。 
    
    # mv winpe.iso /var/tftpboot
    
创建 PXELINUX 的[配置文件](<../zh-cn/Syslinux.html#Configuration> "Syslinux")，类似这个: 
    
    /var/tftpboot/pxelinux.cfg/default
    
    UI         menu.c32
    MENU TITLE Network Boot
    TIMEOUT    50
    
    LABEL      winpe
    MENU LABEL Boot Windows PE from network
    KERNEL     /memdisk
    INITRD     winpe.iso
    APPEND     iso raw
    
    LABEL      localboot
    MENU LABEL Boot from local disk
    LOCALBOOT  0
    
启动 [TFTP server](</wzh/index.php?title=Tftpd_server&action=edit&redlink=1> "Tftpd server（页面不存在）"). 

配置你的 DHCP server (例如 [Dhcpd](<../zh-cn/Dhcpd.html> "Dhcpd") 和 [Dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq"))，用 Linux 服务器的 IP 地址指向作为引导文件的 `pxelinux.0`。注意：如果您的 DHCP 服务器在路由器上，则可能无法在不安装自定义固件的情况下执行此操作。 

完成以上全部步骤后，你将能够从网络启动 Windows PE 。 

**注意：** 根据上面给出的 PXELINUX 配置文件, Windows PE 将在 5 秒后默认启动

**提示：** TFTP 并非为传输大文件而设计, `winpe.iso` 足足有 118MB 或更大，可能需要花费超过 30 秒的时间加载。使用 `gpxelinux.0` bootloader 而不是 `pxelinux.0`，使用 HTTP 而不是 TFTP 加载 `winpe.iso` 或许可以提高性能

##  从 Windows PE 安装 Windows

启动到 Windows PE 后，您可以从安装介质安装 Windows。 

安装介质可以是网络共享 (Samba)。有关在局域网中的另一台机器上设置 Samba 服务器的信息，请参阅 [Samba](<../zh-cn/Samba.html> "Samba")。要分享挂载在 `/media/winimg` 的安装镜像，请加以下内容添加到 `/etc/samba/smb.conf`: 
    
    /etc/samba/smb.conf
    
    [REMINST]
    browsable = true
    read only = no
    guest ok = yes
    path = /media/winimg
    
启动到 Windows PE 命令提示符后，运行以下命令来初始化网络接口，获取 Samba 服务器的 IP (假设 Windows PE 是从运行 DHCP、TFTP 和 Samba 服务器的机器上通过 PXE 启动的，服务器 IP 通常也是网关 IP），挂载网络共享，并运行图形化安装程序: 
    
     > wpeinit
     > ipconfig
     > net use I: \\IP.ADDRESS.OF.SAMBA.SERVER\REMINST
     > I:\setup.exe
    
##  问题解决

###  出现系统错误 58，指定的服务器无法执行请求的操作

如果你在执行 `net use` 命令时看到以下错误提示: 
    
    System error 58 has occurred.
    
    The specified server cannot perform the requested operation.
    
1\. 确保你没有误卸载 `/media/winimg` 文件夹. 

2\. 添加一个 `map to guest` 到 `/etc/samba/smb.conf` 文件中。即在文件开头添加如下内容: 
    
    /etc/samba/smb.conf
    
    [global]
    map to guest = Bad User
    ...
    
3\. 重启 `smbd.service`。 

4\. 使用命令在 net 中明指定任意一个用户名和对应密码: 
    
    net use I: \\IP.ADDRESS.OF.SAMBA.SERVER\REMINST /user:user pass
    
发生这种情况，是因为 Windows 10 连接到匿名共享时，需要用一对用户名和密码检查是否能够登录，如果可以，则允许匿名连接。显然，只要有地方阻止用户验证是否可以登录，就无法在 PE 系统中访问 Samba 共享。 

##  参阅

  * [关于 Windows PE 的微软文档](<https://technet.microsoft.com/en-us/library/cc766093\(v=ws.10\).aspx>)
  * [另一篇有关在 Linux 上制作 Windows PE 镜像的文章](<https://www.thinkwiki.org/wiki/Windows_PE>)
  * [A guide with scripts for unattended installation of Windows 7 from Linux using Windows PE](<http://www.ultimatedeployment.org/win7pxelinux1.html>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-23 ⓘ]
  * [Windows 10 PE Unable to map network drive anonymously](<https://serverfault.com/a/858269>)
