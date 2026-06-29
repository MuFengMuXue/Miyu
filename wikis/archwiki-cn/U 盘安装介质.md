**翻译状态：**

  * 本文（或部分内容）译自 [USB flash installation medium](<https://wiki.archlinux.org/title/USB_flash_installation_medium> "arch:USB flash installation medium")，最近一次同步于 2023-11-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/USB_flash_installation_medium?diff=0&oldid=792523>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/USB_flash_installation_medium_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [光盘驱动器](<../zh-cn/%E5%85%89%E7%9B%98%E9%A9%B1%E5%8A%A8%E5%99%A8.html> "光盘驱动器")
  * [Archiso](<../zh-cn/Archiso.html> "Archiso")
  * [多引导 USB 设备](<../zh-cn/%E5%A4%9A%E5%BC%95%E5%AF%BC_USB_%E8%AE%BE%E5%A4%87.html> "多引导 USB 设备")

USB 驱动器，也被称为闪存驱动器、USB记忆棒、U盘等。可以从 ISO 制作 Arch LiveUSB 系统，从 UEFI 或 BIOS 系统上直接启动 Arch Linux 安装环境。由于 `/` 根目录使用了 [Overlayfs](</wzh/index.php?title=Overlayfs&action=edit&redlink=1> "Overlayfs（页面不存在）")，关机后所有的更改都会丢失。这样的系统可用于 Arch Linux 安装、系统维护或者系统恢复。 

要在 U 盘上运行完整的 Arch Linux（即能保留设置），请阅读[在可移动设备上安装 Arch Linux](<../zh-cn/%E5%9C%A8%E5%8F%AF%E7%A7%BB%E5%8A%A8%E8%AE%BE%E5%A4%87%E4%B8%8A%E5%AE%89%E8%A3%85_Arch_Linux.html> "在可移动设备上安装 Arch Linux")。如果想将 Arch Linux U 盘当作救援 USB 来用，参见 [chroot](<../zh-cn/Chroot.html> "Chroot")。 

在进行下列任何操作前，先从 <https://archlinux.org/download/> 下载 ISO 并[验证其完整性](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html#%E9%AA%8C%E8%AF%81%E7%AD%BE%E5%90%8D> "安装指南")。 

##  直接使用 ISO（BIOS 和 UEFI）

**警告：** 这一操作将不可恢复地删除 USB 驱动器上的所有数据，所以在操作前先确保驱动器上没有存放任何重要文件。

**注意：** 如果你想将 ISO 写入到机械硬盘或是固态硬盘上，而不是使用 U 盘或是 SD 卡，请确保硬盘的逻辑扇区大小不大于 2048 字节（[ISO 9660](<https://en.wikipedia.org/wiki/ISO_9660> "wikipedia:ISO 9660") 扇区大小），并按此数值进行对齐。这也意味着不能用此方法将 ISO 写入到 4Kn [先进格式化](<../zh-cn/%E5%85%88%E8%BF%9B%E6%A0%BC%E5%BC%8F%E5%8C%96.html> "先进格式化")硬盘中。

###  GNU/Linux

####  使用基本命令行工具

推荐该方法是因为它简单，且由于这些工具是 [coreutils](<https://archlinux.org/packages/?name=coreutils>)包（由 [base](<https://archlinux.org/packages/?name=base>)包 [元软件包](<../zh-cn/%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%84.html> "元软件包和软件包组")引入）的一部分，其通用性也很广。 

使用 `ls -l /dev/disk/by-id/usb-*` 找到 U 盘的名字，然后使用 `lsblk` 检查确保其**没有** 被挂载。 

将下列命令中的 `/dev/disk/by-id/usb-_My_flash_drive_` 替换为你的 U 盘（例如`/dev/disk/by-id/usb-Kingston_DataTraveler_2.0_408D5C1654FDB471E98BED5C-0:0`）。(**不要** 加上分区编号，也就是**不要** 输入类似 `/dev/disk/by-id/usb-Kingston_DataTraveler_2.0_408D5C1654FDB471E98BED5C-0:0**-part1**` 或者是 `/dev/sdb**1**` 的东西）： 

  * 使用 [cat(1)](<https://man.archlinux.org/man/cat.1>)：
        
        # cat _path/to/_ archlinux-_version_ -x86_64.iso > /dev/disk/by-id/usb-_My_flash_drive_

  * 使用 [cp(1)](<https://man.archlinux.org/man/cp.1>)：
        
        # cp _path/to/_ archlinux-_version_ -x86_64.iso /dev/disk/by-id/usb-_My_flash_drive_

  * 使用 [dd](<../zh-cn/Dd.html> "Dd")：
        
        # dd bs=4M if=_path/to/_ archlinux-_version_ -x86_64.iso of=/dev/disk/by-id/usb-_My_flash_drive_ conv=fsync oflag=direct status=progress

  * 使用 [tee](</wzh/index.php?title=Tee&action=edit&redlink=1> "Tee（页面不存在）")：
        
        # tee < _path/to/_ archlinux-_version_ -x86_64.iso > /dev/disk/by-id/usb-_My_flash_drive_

  * 使用 [pv](<https://archlinux.org/packages/?name=pv>)包：
        
        # pv _path/to/_ archlinux-_version_ -x86_64.iso > /dev/disk/by-id/usb-_My_flash_drive_

可参考 [[1]](<https://unix.stackexchange.com/questions/224277/is-it-better-to-use-cat-dd-pv-or-another-procedure-to-copy-a-cd-dvd/224314#224314>) 和 [[2]](<https://www.vidarholen.net/contents/blog/?p=479>) 来对比这些工具并了解它们的大致用法，以及为何 _dd_ 可能是最不适用的方法。 

**提示：**

  * 执行完命令后，使用根权限执行 `sync` 来确保在移除硬盘前缓冲区数据已完全写入。
  * If the UEFI version of the USB's Arch ISO hangs or is unable to load, try repeating the medium creation process on the same USB drive one or more times. If this does not work, you may also try updating your motherboard's firmware.

**注意：** 如果在使用完 Arch ISO 镜像后要 U 盘恢复为空的可用 USB 存储设备，须在[重分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")和[重新格式化](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E5%88%9B%E5%BB%BA%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "文件系统") U 盘前使用根权限运行 `wipefs --all /dev/disk/by-id/usb-_My_flash_drive_` 将 ISO 9660 文件系统签名移除。

####  使用 GNOME Disk Utility

Linux distributions running GNOME can easily make a live CD through [nautilus](<https://archlinux.org/packages/?name=nautilus>)包 and [gnome-disk-utility](<https://archlinux.org/packages/?name=gnome-disk-utility>)包. Simply right-click on the _.iso_ file, and select _Open With Disk Image Writer_. When GNOME Disk Utility opens, specify the flash drive from the _Destination_ drop-down menu and click _Start Restoring_. 

####  使用 MultiWriter

[gnome-multi-writer](<https://archlinux.org/packages/?name=gnome-multi-writer>)包 是一个基于 [GTK](<../zh-cn/GTK.html> "GTK")3 的图形化工具，用于将 ISO 文件同时写入到单个或多个 U 盘中。 

####  使用 Kindd

[Kindd](<https://github.com/LinArcX/Kindd>) 是基于 Qt 的 dd 图形化前端，可通过 [kindd](<https://aur.archlinux.org/packages/kindd/>)AUR 获取。 

####  使用 Popsicle

[Popsicle](<https://github.com/pop-os/popsicle>) 是由 PopOS 开发团队制作的工具，用于同时向多个 U 盘写入 ISO 文件。它使用 Rust 和 GTK 编写，可通过 [popsicle](<https://aur.archlinux.org/packages/popsicle/>)AUR 获取。 

####  使用 SUSE Studio ImageWriter

[SUSE Studio ImageWriter](<https://github.com/openSUSE/imagewriter>) 是由 OpenSUSE 开发团队基于 Qt 制作的 Qt，可通过 [imagewriter](<https://aur.archlinux.org/packages/imagewriter/>)AUR 获取。 

####  使用 xorriso-dd-target

[xorriso-dd-target](<https://dev.lovelyhq.com/libburnia/libisoburn/raw/master/xorriso-dd-target/xorriso-dd-target>)（来自 [libisoburn](<https://archlinux.org/packages/?name=libisoburn>)包）是一个 shell 脚本，尝试降低覆盖到错误存储设备的风险。它最安全的模式名为 `-plug_test`。以可以通过 [sudo](<../zh-cn/Sudo.html> "Sudo") 提升到 root 权限的普通用户为例： 
    
    $ xorriso-dd-target -with_sudo -plug_test -DO_WRITE -image_file archlinux-_version_ -x86_64.iso
    
更多信息可参考 [xorriso-dd-target(1)](<https://man.archlinux.org/man/xorriso-dd-target.1>)。 

####  使用 USBImager

[USBImager](<https://gitlab.com/bztsrc/usbimager/>) 是一个跨平台的图形化程序，用于将压缩的磁盘镜像写入到 U 盘中并进行验证，并可以创建备份。可通过 [usbimager](<https://aur.archlinux.org/packages/usbimager/>)AUR 获取。 

### Windows

####  使用 win32diskimager

[win32diskimager](<https://sourceforge.net/projects/win32diskimager/>) 是另一个用于在 Windows 上写入镜像到 USB 或者 SD/CF 卡上的工具。只需选择 ISO 映像和目标 USB 盘符（可能需要先格式化 USB 驱动器后才能分配驱动器号），然后点击“Write”即可。 

####  使用 USBwriter

这一方法和 Linux 下的 `dd` 一样简单，只要下载 Arch Linux 安装镜像，并通过本地管理员权限使用 [USBwriter](<https://sourceforge.net/p/usbwriter/wiki/Documentation/>) 写入 U 盘即可。 

####  使用 USBImager

[USBImager](<https://gitlab.com/bztsrc/usbimager/>) 是一个跨平台的图形化程序，用于将压缩的磁盘镜像写入到 U 盘中并进行验证，并可以创建备份。可通过 [usbimager](<https://aur.archlinux.org/packages/usbimager/>)AUR 获取。 

####  使用 Rufus

[Rufus](<https://rufus.ie/zh/>) 是一款多用途的 USB ISO 写入工具。它提供了图形化用户界面，并不关心驱动器是否被正确地格式化。 

只要简单地选择 Arch Linux ISO、要创建可启动 Arch Linux 的 USB 驱动器，然后点击 _开始_ 即可。 

**注意：** 如果USB设备使用默认USB镜像模式无法正确引导，请选用""DD Image 模式""。如果要切换到这个模式，请在“分区方案”下拉菜单中选择“GPT”，点击“开始”后你会看到选项提示框，最后选择“DD Image 模式”

**提示：** 要添加 [一个用于持久存储的额外分区](<https://github.com/pbatard/rufus/issues/691>) ，请使用滑块选择持久分区的大小。在使用持久分区功能时，请确保在 “分区方案 ”下拉菜单中选择 “MBR”，并在 “目标系统 ”中选择 “BIOS 或 UEFI”，否则硬盘将无法同时用于 BIOS 和 UEFI 启动。 

####  使用 Cygwin

先确保你的 [Cygwin](<https://www.cygwin.com/>) 环境包含了 `dd` 包。 

将您的镜像文件放在您的 home 目录中： 
    
    C:\cygwin\home\_User_ \
    
以管理员身份运行 cygwin（以允许 cygwin 访问硬件）。用下列命令写入到您的 USB 设备： 
    
    dd if=archlinux-_version_ -x86_64.iso of=\\.\_x_ : bs=4M
    
其中 `archlinux-_version_ -x86_64.iso` 是 `cygwin` 目录下的 ISO 镜像路径，而 `\\.\_x_ :` 是你的 U 盘，里面的 `_x_` 是 Windows 为您的 USB 设备指定的盘符，例如 `\\.\d:`。 

Cygwin 6.0 版本中可以这样找到正确的分区： 
    
    cat /proc/partitions
    
然后根据输出信息写入ISO映像，例如： 
    
    dd if=archlinux-_version_ -x86_64.iso of=/dev/sdb bs=4M
    
####  使用 dd for Windows

<http://www.chrysocome.net/dd> 上有基于 GPL 协议的 Windows 版 dd。相比于 Cygwin，它的优势在于需下载量较小。使用方法参考上面的 Cygwin 部分。 

首先下载最新版本的 dd for Windows，并把内容解压到 `Downloads` 目录或者别的什么地方。 

现在以管理员身份运行 _命令提示符_ 。然后切换目录（`cd`）到 `Downloads` 目录。 

如果你的 Arch Linux ISO 在别的地方，你可能需要列出完整路径。为了方便起见，你可能会想把它放在 _dd_ 程序的同一目录中。命令的基本格式像这样： 
    
    # dd if=archlinux-_version_ -x86_64.iso od=\\.\_x_ : bs=4M
    
**注意：** Windows 的驱动器盘符链接到的是分区。为了选择完整的硬盘，上述命令使用了 _dd for Windows_ 提供的 `od` 参数。需要注意，这一参数仅适用于 _dd for Windows_ ，并不适用于其它 _dd_ 实现。

####  使用 flashnul

[flashnul](<https://github.com/amarao/flashnul/blob/master/README.md>) 是一款用于验证和维护闪存（USB 闪存、IDE 闪存、SecureDigital、MMC、MemoryStick、SmartMedia、XD、CompactFlash 等）功能的实用程序。 

在命令提示符下，用 `-p` 调用 flashnul，并确定 USB 驱动器的设备索引，例如 
    
    C:\>flashnul -p
    
    Avaible physical drives:
    Avaible logical disks:
    C:\
    D:\
    E:\
    
确定了正确的设备后，您就可以将镜像写入硬盘，通过用`-L`设备索引和镜像的路径来调用 flashnul，例如： 
    
    C:\>flashnul **E:** -L _path\to\_ archlinux-_version_ -x86_64.iso
    
只要你已经确定要开始写入数据，就输入 yes ，稍等片刻等待写入完成。如果出现了拒绝访问的错误，请关闭所有打开的资源管理器窗口。 

**注意：** 请以管理员身份打开命令提示符，否则 flashnul 将无法将镜像作为块设备打开，只能通过 windows 提供的驱动器句柄写入。

### macOS

####  使用 macOS dd

首先确认设备，打开 `/Applications/Utilities/Terminal` 然后通过下面命令查看所有存储设备： 
    
    $ diskutil list
    
USB 设备应该类似于 `/dev/disk2 (external, physical)`。通过名称和大小确认设备是否正确，在后面的命令中用其替换掉 `/dev/disk _X_`。 

macOS 通常会自动挂载 USB 设备，在使用 `dd` 前需要将其卸载（不是弹出）。打开 _Terminal_ ，然后输入： 
    
    $ diskutil unmountDisk /dev/disk _X_
    
然后将 ISO 镜像复制到设备上： 

{{Note| 

  * BSD 的 `dd` 衍生版本（包括 macOS 预装的）使用小写 `m` 后缀。这与本文其它地方使用的 GNU 版本 `dd` 不同。
  * `disk` 前的 `r} 意味着使用 raw 模式，可以大幅提升传输速率。`
`
  * 在新版 macOS 中，dd 命令支持使用 `status=progress` 来显示进度。你也可以通过下方描述手动显示进度。
` 
``

``
    
    # dd if=_path/to_ /archlinux-_version_ -x86_64.iso of=/dev/**r** disk _X_ bs=1m
    
这一命令将静默执行。如果要显示进度，可以按下 {{ic|Ctrl+t} 来传递 SIGINFO 信号。注意，这里的 `disk _X_` 不应包含 `s1` 后缀，否则 U 盘将仅支持 UEFI 模式启动。完成后，macOS 可能抱怨 _The disk you inserted was not readable by this computer_ ，选择忽略就行。启动盘就做好了。 

####  使用 USBImager

[USBImager](<https://gitlab.com/bztsrc/usbimager/>) 是一个跨平台的图形化程序，用于将压缩的磁盘镜像写入到 U 盘中并进行验证，并可以创建备份。可通过 [usbimager](<https://aur.archlinux.org/packages/usbimager/>)AUR 获取。 

### Android

####  使用 EtchDroid

[EtchDroid](<https://etchdroid.depau.eu/>) 是一个安卓平台上的系统镜像烧录器，从安卓 5 开始不再需要 root 权限。如果遇到任何问题，可查看 [GitHub](<https://github.com/EtchDroid/EtchDroid/issues/>) 上游。 

要创建 Arch Linux 安装盘，需先将 ISO 镜像下载到安卓设备上。将 U 盘插入到设备，有需要的话可以使用 USB-OTG 转接器。接下来打开 EtchDroid，选择 _Flash raw image_ ，选择 Arch ISO 文件，然后选择 U 盘。最后授予 USB API 权限并确认。 

刷入镜像时请将手机放在桌子上：很多 USB-OTG 转接器的连接都不太稳，很容易不小心被拔掉。 

##  手动方法

###  BIOS 和 UEFI

####  GNU/Linux

这种方法比通过 `dd` 直接写入镜像复杂，但能够保持 U 盘可用于数据存储（ISO 被装在[分了区的设备](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")的特定分区里而无需改变其他分区）。 

**注意：** 接下来会用 `/dev/disk/by-id/usb-_My_flash_drive_ -part _n_` 指代目标分区，请根据实际情况修改命令中的 `_My_flash_drive_` 和 `_n_`。

  * 预先在 `/dev/disk/by-id/usb-_My_flash_drive_` 创建[分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E8%A1%A8> "分区表")。
  * 预先在设备上创建一个分区，`/dev/disk/by-id/usb-_My_flash_drive_ -part _n_` 分区必须格式化为 [FAT32](<../zh-cn/FAT.html> "FAT32")。
  * 挂载 U 盘上的 FAT32 文件系统，并将 ISO 镜像中的内容[解压](<../zh-cn/%E5%BD%92%E6%A1%A3%E4%B8%8E%E5%8E%8B%E7%BC%A9.html> "解压")到其中。

    # mount /dev/disk/by-id/usb-_My_flash_drive_ -part _n_ /mnt
    # bsdtar -x -f archlinux-_version_ -x86_64.iso -C /mnt
    
在 BIOS 平台上启动时需指定文件所在的卷，默认情况下会使用 UUID `_YYYY-mm-dd-HH-MM-SS_ -00`（即 UTC 时区的镜像发布时间）。可以将 `/mnt/boot/syslinux/archiso_sys-linux.cfg` 中的 `archisodevice=` 参数替换为对应设备的[持久化设备识别符](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")，例如：`archisodevice=UUID=_YOUR-UUID_`

**注意：** 错误的 `archisolabel` 或 `archisodevice` 将导致无法从创建好的介质中启动。

用于 BIOS 的 [Syslinux](<../zh-cn/Syslinux.html> "Syslinux") 文件已被拷入到 `/mnt/boot/syslinux/`。[卸载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E5%8D%B8%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "文件系统") FAT 文件系统，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [syslinux](<https://archlinux.org/packages/?name=syslinux>)包 和 [mtools](<https://archlinux.org/packages/?name=mtools>)包 包，并运行以下命令来使分区变为可启动： 
    
    # umount /mnt
    # syslinux --directory boot/syslinux --install /dev/disk/by-id/usb-_My_flash_drive_ -part _n_
    # dd bs=440 count=1 conv=notrunc if=/usr/lib/syslinux/bios/mbr.bin of=/dev/disk/by-id/usb-_My_flash_drive_
    
**注意：**

  * 如果 `/dev/disk/by-id/usb-_My_flash_drive_` 使用 [GUID 分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "分区")，需将 `mbr.bin` 替换为 `gptmbr.bin`。详细信息可参考 [Syslinux#手动安装](<../zh-cn/Syslinux.html#%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85> "Syslinux")。
  * 对于 [MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "MBR") 分区表，需要设定“boot”标记。详细信息可参考 [Syslinux#MBR_分区表](<../zh-cn/Syslinux.html#MBR_%E5%88%86%E5%8C%BA%E8%A1%A8> "Syslinux")。

#### Windows

**注意：**

  * 对于手动方法而言，不要使用任何**可启动 USB 创建工具** 制作 UEFI 启动 U 盘，也不要用 _dd for Windows_ 将 ISO 镜像写入 U 盘。
  * 下列命令假定 U 盘盘符为 `_X_ :`。
  * Windows 使用反斜杠 `\` 作为路径分隔符，这一规则同样用于下列命令中。
  * 所有命令都应该在**以管理员身份运行** 的命令提示符内执行。
  * `>` 表示 Windows 命令提示符。

  * 使用 [Rufus USB partitioner](<https://rufus.ie/zh/>)对 U 盘进行分区和格式化。在分区类型一项选择 **MBR for BIOS and UEFI** ，文件系统选择 **FAT32** 。反选“Create a bootable disk using ISO image”和“创建扩展的标签和图标文件”两项。
  * 如果用的是官方 ISO 镜像（[Archiso](<../zh-cn/Archiso.html> "Archiso")），需修改 U 盘的**卷标** 到你想要的值。这一步骤也可以在“分区并格式化”这一步中通过 Rufus 来完成。
  * 使用 [7-Zip](<https://www.7-zip.org/>) 将 ISO 中的文件解压（与解压 ZIP 压缩包类似）到 U 盘中。
  * 编辑 `_X_ :\boot\syslinux\archiso_sys-linux.cfg`，将所有 `archisodevice=UUID=_YYYY-mm-dd-HH-MM-SS_ -00` 替换为 `archisodevice=LABEl=_YOUR_LABEL_`，其中 `_YOUR_LABEL_` 为上一步设定的卷标。
  * 从 <https://www.kernel.org/pub/linux/utils/boot/syslinux/> 下载官方 Syslinux 6.xx 二进制文件（ZIP 打包文件）并解压。Syslinux 的版本应与 ISO 镜像所使用的版本一致。

  * 在命令提示符内，以管理员身份运行以下命令：

    > cd bios\
    > for /r %Y in (*.c32) do copy "%Y" "_X_ :\boot\syslinux\" /y
    > copy mbr\*.bin _X_ :\boot\syslinux\ /y
    
  * 通过以下命令将 Syslinux 安装到 U 盘（64 位系统则使用 `win64\syslinux64.exe`）：

    > cd bios\
    > win32\syslinux.exe -d /boot/syslinux -i -a -m _X_ :
    
**注意：**

  * 仅复制文件并不能使得可以从 U 盘启动；最后一条命令将 Syslinux 的文件安装到了 U 盘的 VBR 分区，在 MBR 分区表中将该分区设置为“活跃/启动”，并将 MBR 启动代码写入到了 U 盘中。
  * `-d` 参数需要使用正斜杠作为路径分隔符，与类 unix 系统上类似。

###  仅 BIOS

####  GNU/Linux

#####  制作 USB-ZIP 盘

某些旧的 BIOS 设备仅支持从 USB-ZIP 盘启动。该方法让你可以继续从 USB 硬盘上启动。 

  * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [syslinux](<https://archlinux.org/packages/?name=syslinux>)包 和 [mtools](<https://archlinux.org/packages/?name=mtools>)包。
  * 通过 `ls /dev/disk/by-id/usb-*` 命令找到你的 U 盘。
  * 输入 `mkdiskimage -4 /dev/disk/by-id/usb-_My_flash_drive_ 0 64 32`，完成需要一段时间。

接下来继续按手动方法进行操作。由于 ZIP 硬盘的工作方式，分区将使用 `/dev/disk/by-id/usb-_My_flash_drive_ -part4`。 

**注意：** 不要将盘格式化为 FAT32 格式，必须使用 FAT16。

###  仅 UEFI

如果仅使用 UEFI 启动，只需将 ISO 中文件解压到 FAT 格式的 U 盘中即可。 

由于所有 UEFI 系统都可以 U 盘的任何 FAT 卷中启动，不需要单独创建 EFI 系统分区。兼容性最强的配置方法为使用 MBR 分区表，并创建单个活动（可启动）主分区，类型为 `0c`“W95 FAT32 (LBA)”。[[3]](<https://lists.gnu.org/archive/html/grub-devel/2019-05/msg00063.html>)

**提示：** See [Secure Boot#Sign the official ISO with custom keys](<../zh-cn/Secure_Boot.html#Sign_the_official_ISO_with_custom_keys> "Secure Boot") to understand which files need to be signed if Secure Boot is configured with custom keys.

####  GNU/Linux

This method extracts files from the ISO image to a USB flash drive. 

  1. If not done yet, create a [partition table](</wzh/index.php?title=Partition_table&action=edit&redlink=1> "Partition table（页面不存在）") on `/dev/disk/by-id/usb-_My_flash_drive_` and a [partition](</wzh/index.php?title=Partition&action=edit&redlink=1> "Partition（页面不存在）") (`/dev/disk/by-id/usb-_My_flash_drive_ -part _n_`) on the device.
  2. If not done yet, format the partition to [FAT32](<../zh-cn/FAT.html> "FAT32"): 
         
         # mkfs.fat -F 32 /dev/disk/by-id/usb-_My_flash_drive_ -part _n_

  3. [Mount](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Mount") the file system: 
         
         # mount /dev/disk/by-id/usb-_My_flash_drive_ -part _n_ /mnt

  4. Extract the ISO image to the mounted file system: 
         
         # bsdtar -x -f archlinux-_version_ -x86_64.iso -C /mnt

  5. [Unmount](</wzh/index.php?title=Unmount&action=edit&redlink=1> "Unmount（页面不存在）") the file system.

#### Windows

This method copies files from the ISO image to a USB flash drive. 

  1. Partition the USB flash drive and format it to FAT32.
  2. Right click on `archlinux-_version_ -x86_64.iso` and select _Mount_.
  3. Navigate to the newly created DVD drive and copy all files and folders to the USB flash drive.
  4. When done copying, right click on the DVD drive and select _Eject_.
  5. Eject the USB flash drive.

#### macOS

Neither _DiskImageMounter_ nor _Disk Utility_ can mount isohybrid ISOs, but since macOS ships with _libarchive_ , the ISO can simply be extracted onto the flash drive using _bsdtar_. 

  1. If not done yet, partition the USB flash drive and format the partition to FAT32 using _Disk Utility_.
  2. Mount the volume.
  3. Open the _Terminal_ application and use _bsdtar_ to extract the ISO image to the mounted file system: 
         
         $ bsdtar -x -f archlinux-_version_ -x86_64.iso -C /Volumes/_your-flash-drive_

  4. When done, unmount and eject the USB flash drive.

##  使用多引导 USB 设备

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[多引导USB设备](<../zh-cn/%E5%A4%9A%E5%BC%95%E5%AF%BC_USB_%E8%AE%BE%E5%A4%87.html> "多引导USB设备")。**

**附注：** For [Multiboot USB drive#Using Syslinux and memdisk](<../zh-cn/Multiboot_USB_drive.html#Using_Syslinux_and_memdisk> "Multiboot USB drive"), this is the same method, only Syslinux is installed from Windows. This whole section should be merged there, since [Ventoy](<../zh-cn/Ventoy.html> "Ventoy") is already mentioned over there too.（在 [Talk:U 盘安装介质](<../zh-cn/Talk:U_%E7%9B%98%E5%AE%89%E8%A3%85%E4%BB%8B%E8%B4%A8.html>) 中讨论）

该方法允许从单个 U 盘启动包括 archiso 在内的多个 ISO。将现有 U 盘升级到新版 ISO 的流程比其余多数方法都简单，详情可参考[多引导USB设备](<../zh-cn/%E5%A4%9A%E5%BC%95%E5%AF%BC_USB_%E8%AE%BE%E5%A4%87.html> "多引导USB设备")。 

###  使用 ventoy

[Ventoy](<../zh-cn/Ventoy.html> "Ventoy") 是一个适用于 ISO/WIM/IMG/VHD(x)/EFI 文件的开源可启动 U 盘制作工具。通过使用 ventoy，你不需要反复格式化硬盘，而只需将 ISO/WIM/IMG/VHD(x)EFI 文件复制到 U 盘，然后直接启动即可。你可以一次性复制多个文件，ventoy 会显示一个启动清单让你进行选择。ventoy 可通过 [ventoy-bin](<https://aur.archlinux.org/packages/ventoy-bin/>)AUR 获取。 

### Windows

####  从内存加载安装介质

这个方法使用 [Syslinux](<../zh-cn/Syslinux.html> "Syslinux") 和一个 [Ramdisk](</wzh/index.php?title=Ramdisk&action=edit&redlink=1> "Ramdisk（页面不存在）")（[MEMDISK](<https://wiki.syslinux.org/wiki/index.php/MEMDISK>)）来把整个 Arch Linux ISO 镜像加载到内存中。由于它将完全运行于系统内存中，您要确保使用这种方法安装的设备上有足够的内存。至少 500MB 到 1G 内存就足以在 MEMDISK 上安装 Arch Linux。 

Arch Linux 和 MEMDISK 系统要求参见[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")和[这里](<http://www.etherboot.org/wiki/bootingmemdisk#preliminaries>)，也可以参考[之前的论坛帖](<https://bbs.archlinux.org/viewtopic.php?id=135266>)。 

**提示：** 一旦安装程序加载完毕，您就可以移除 U 盘，甚至再在另一台机器上用它开始执行整个安装步骤。使用 MEMDISK 还允许你在同一个 U 盘中引导并安装 Arch Linux 到它上面。

#####  准备 U 盘

首先将 U 盘格式化为 **FAT32** 文件系统。然后在格式化后的磁盘中创建以下目录： 

  * `Boot`
    * `Boot/ISOs`
    * `Boot/Settings`

#####  复制需要的文件到 U 盘

然后，把要引导的 ISO 复制到 `Boot/ISOs` 目录。接着，从[这里](<https://www.kernel.org/pub/linux/utils/boot/syslinux/>)下载最新版的 [syslinux](<https://archlinux.org/packages/?name=syslinux>)包，并从中提取以下文件并复制到下列目录： 

  * `./win32/syslinux.exe` 到桌面或者系统中的 Downloads 目录。
  * `./memdisk/memdisk` 到 U 盘中的 `Settings` 目录。

#####  创建配置文件

复制完所需文件后，在 U 盘的 /Boot/Settings 目录中创建文件 `syslinux.cfg`。 

**注意：** 在 `INITRD` 一行中，确保使用了复制到 `ISOs` 文件夹中的 ISO 文件名。
    
    /Boot/Settings/syslinux.cfg
    
    DEFAULT arch_iso
    
    LABEL arch_iso
            MENU LABEL Arch Setup
            LINUX memdisk
            INITRD /Boot/ISOs/archlinux-_version_ -x86_64.iso
            APPEND iso

更多信息可参考 [Syslinux](<../zh-cn/Syslinux.html> "Syslinux")。 

#####  最后一步

最后，在 `syslinux.exe` 所在目录创建一个 `*.bat` 文件并运行（如果是在 Vista 或者 Windows 7 下，需要“以管理员身份运行”）： 
    
    C:\Documents and Settings\username\Desktop\install.bat
    
    @echo off
    syslinux.exe -m -a -d /Boot/Settings X:
    
##  不推荐的方法

**警告：** 不推荐使用下列方法。

###  使用 etcher

etcher 包含分析数据收集和第一方广告。可参考[[4]](<https://github.com/balena-io/etcher/issues/2057>)，[[5]](<https://github.com/balena-io/etcher/blob/37769efbeda0abe7993d95e2b2aea2f461edd307/lib/gui/app/pages/main/MainPage.tsx#L151>) 和 [[6]](<https://github.com/balena-io/etcher/blob/37769efbeda0abe7993d95e2b2aea2f461edd307/docs/MAINTAINERS.md#publishing>)。 

###  使用 Universal USB Installer

  * 下载页包含可能带毒的假 _下载_ 按钮。
  * Universal USB Installer 不会按原样写入 ISO 数据，会由于 syslinux 版本的差异导致 BIOS 环境无法启动，可参考 [[7]](<https://bbs.archlinux.org/viewtopic.php?pid=1344629>)。
  * Arch Linux 安装镜像的引导加载器期望 ISO 数据位于卷标为 `ARCH__YYYYXX_` 的卷上。Universal USB Installer 不会更新卷标，也不会修正引导加载器的配置。

###  使用 UNetbootin

  * UNetbootin 不会按原样写入 ISO 数据，会由于 syslinux 版本的差异导致 BIOS 环境无法启动。
  * Arch Linux 安装镜像的引导加载器期望 ISO 数据位于卷标为 `ARCH__YYYYXX_` 的卷上。UNetbootin 不会更新卷标，也不会修正引导加载器的配置。

##  故障排除

###  未显示设备

如果由于 `/dev/disk/by-label/ARCH__YYYYMM_` 未挂载而出现 `device did not show up after 30 seconds` 报错，可以尝试将 U 盘重命名为 `ARCH__YYYYMM_` 来让 Arch 进行自动搜寻（例如 ISO 名为 `archlinux-2021.02.01-x86_64.iso`，设备名应为 `ARCH_202102`）。 

### Failed to set up loop devices: No such file or directory

如果你看到了 `losetup: /run/archiso/bootmnt/arch/x86_64/airootfs.sfs: failed to set up loop devices: No such file or directory` 报错，请尝试换用 USB 2.0 接口，有时 USB 集线器的部分 USB 3.0 接口会失效。 

###  其它报错

对于其它报错，请尝试换一个 U 盘，通常情况下可以解决所有问题。 

##  参见

  * [Gentoo:LiveUSB/Guide](<https://wiki.gentoo.org/wiki/LiveUSB/Guide> "gentoo:LiveUSB/Guide")
  * [Fedora wiki - How to create and use Live USB](<https://fedoraproject.org/wiki/How_to_create_and_use_Live_USB>)
  * [openSUSE wiki - SDB:Live USB stick](<https://en.opensuse.org/SDB:Live_USB_stick>)
