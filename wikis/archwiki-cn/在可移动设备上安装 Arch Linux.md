相关文章

  * [安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")
  * [建议阅读](<../zh-cn/%E5%BB%BA%E8%AE%AE%E9%98%85%E8%AF%BB.html> "建议阅读")
  * [常规故障排除](<../zh-cn/%E5%B8%B8%E8%A7%84%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html> "常规故障排除")
  * [VirtualBox/在虚拟机中安装 Arch Linux](<../zh-cn/VirtualBox/%E5%9C%A8%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%E5%AE%89%E8%A3%85_Arch_Linux.html> "VirtualBox/在虚拟机中安装 Arch Linux")
  * [固态硬盘](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html> "固态硬盘")

**翻译状态：**

  * 本文（或部分内容）译自 [Install Arch Linux on a removable medium](<https://wiki.archlinux.org/title/Install_Arch_Linux_on_a_removable_medium> "arch:Install Arch Linux on a removable medium")，最近一次同步于 2025-04-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Install_Arch_Linux_on_a_removable_medium?diff=0&oldid=832608>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Install_Arch_Linux_on_a_removable_medium_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文介绍如何在可移动磁盘（如 U 盘）上进行常规的 Arch 安装，结果是与正常安装到硬盘一样的持久化安装。与此相对的是制作 LiveUSB（[U 盘安装介质](<../zh-cn/U_%E7%9B%98%E5%AE%89%E8%A3%85%E4%BB%8B%E8%B4%A8.html> "U 盘安装介质")）。 

##  安装

**注意：** 请阅读[分区#分区方案](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E6%96%B9%E6%A1%88> "分区")以决定需要的磁盘空间。

取决于您的操作系统，可通过多种方式在可移动磁盘上安装 Arch： 

  * 若您有另一台 Linux 计算机（不必是 Arch），您可按照[从现有 Linux 发行版安装 Arch Linux](<../zh-cn/%E4%BB%8E%E7%8E%B0%E6%9C%89_Linux_%E5%8F%91%E8%A1%8C%E7%89%88%E5%AE%89%E8%A3%85_Arch_Linux.html> "从现有 Linux 发行版安装 Arch Linux") 安装。
  * Arch Linux CD/USB 可用于将 Arch 安装到可移动磁盘，只需从 CD/USB 启动并按照[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")进行安装。如果从 Live USB 启动，则无法安装到同一个可移动磁盘。
  * 若您运行 Windows 或 macOS，则可以下载 VirtualBox，安装 VirtualBox 扩展，将您的可移动磁盘连接到 Linux 虚拟机（已安装好或从 live ISO 启动），然后按照[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")安装到连接的磁盘。
  * 可以在您启动安装环境的 USB 设备上安装 Arch Linux，但是您不能在安装过程中重启。若如此做，您可能需要再次制作安装介质。

###  安装时的微调

  * 在[创建初始 RAM disk](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio") 前，修改 `/etc/mkinitcpio.conf`，将 `block` 和 `keyboard` 钩子移动到 `autodetect` 钩子之前。这样才能在分别需要早期用户空间中不同模块的系统上启动。
  * 如果您希望能在其他操作系统中使用安装完的磁盘，可以创建使用适当文件系统的分区（如 NTFS 或 exFAT）。注意，数据分区可能需要是设备的第一个分区，因为 Windows 会假定可移动磁盘仅有一个分区，并将自动挂载 EFI 系统分区。记得安装 [dosfstools](<https://archlinux.org/packages/?name=dosfstools>)包 和 [ntfs-3g](<https://archlinux.org/packages/?name=ntfs-3g>)包。网上的一些工具可能可以翻转可移动磁盘的可移动媒体位（RMB）。这将使得操作系统把它看作外置硬盘，这样您就可以随意使用您选择的分区方式。
  * 如果您的 Arch 所在的可移动磁盘需要有两家制造商的微码，请安装 [amd-ucode](<https://archlinux.org/packages/?name=amd-ucode>)包 和 [intel-ucode](<https://archlinux.org/packages/?name=intel-ucode>)包。见 [Microcode#加载微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html#%E5%8A%A0%E8%BD%BD%E5%BE%AE%E7%A0%81> "Microcode")。
  * 确保在生成的 `/etc/fstab` 文件内删除了主机上的文件系统的相关条目。启动时，若相关条目的文件系统不存在，Arch 会等待该文件系统较长时间。

**警告：** 不是所有的 U 盘都可以翻转可移动媒体位（RMB），并且使用不兼容您的设备的软件可能会造成损坏。**不建议** 尝试翻转RMB。

##  引导加载程序配置

**注意：** Systemd 会自动探测根文件系统 `/`，因此不必在 `/etc/fstab` 中为其建立条目。

### GRUB

按照 [GRUB#BIOS 系统](<../zh-cn/GRUB.html#BIOS_%E7%B3%BB%E7%BB%9F> "GRUB")和 [GRUB#UEFI 系统](<../zh-cn/GRUB.html#UEFI_%E7%B3%BB%E7%BB%9F> "GRUB")中的说明为 BIOS 和 UEFI 启动安装 GRUB： 
    
    # grub-install --target=i386-pc /dev/_sdX_ --recheck
    # grub-install --target=x86_64-efi --efi-directory=_esp_ --removable --recheck
    
**注意：** 此处安装grub时必须使用--removable参数，该参数可以使efi被安装于uefi固件的默认检索位置，对于多设备启动至关重要，缺失几乎必然导致其他设备下无法检索引导程序。 再次检查 device map，即使 `/boot/grub/device.map` 已经存在。每当您添加/删除计算机中的磁盘时都应使用这一选项[[1]](<https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dinstall.html>)。

### Syslinux

使用UUID: 
    
    LABEL Arch
            MENU LABEL Arch Linux
            LINUX ../vmlinuz-linux
            APPEND root=UUID=3a9f8929-627b-4667-9db4-388c4eaaf9fa rw
            INITRD ../initramfs-linux.img
    
### rEFInd
    
    menuentry "Arch Linux" {
       icon     /EFI/BOOT/icons/os_arch.png
       volume   5028fa50-0079-4c40-b240-abfaf28693ea
       loader   _/path/to/vmlinux_image_
       initrd   _/path/to/initramfs_
       options  "root=PARTUUID=5028fa50-0079-4c40-b240-abfaf28693ea rw"
    }
    
请参阅 [rEFInd#手动启动项](<../zh-cn/REFInd.html#%E6%89%8B%E5%8A%A8%E5%90%AF%E5%8A%A8%E9%A1%B9> "REFInd")以获取更多有关创建手动启动项的信息。 

安装 rEFInd 时，您还必须使用 `--usedefault /dev/sd _XY_` 参数。 

##  提示和技巧

###  在多个机器上使用您的设备

####  显卡驱动

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 唯一剩下的专有驱动 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 运行良好，而 [nouveau](<../zh-cn/Nouveau.html> "Nouveau") 自从阻止 reclocking 后就一直在退步。（在 [Talk:在可移动设备上安装 Arch Linux](<../zh-cn/Talk:%E5%9C%A8%E5%8F%AF%E7%A7%BB%E5%8A%A8%E8%AE%BE%E5%A4%87%E4%B8%8A%E5%AE%89%E8%A3%85_Arch_Linux.html>) 中讨论）

**注意：**

  * 对于这种安装，**不** 建议使用专有的显卡驱动。
  * 在决定安装 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 和 [xf86-video-nouveau](<https://archlinux.org/packages/?name=xf86-video-nouveau>)包 前请先阅读 [Intel 图形处理器#安装](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html#%E5%AE%89%E8%A3%85> "Intel 图形处理器") 和 [Nouveau#安装](<../zh-cn/Nouveau.html#%E5%AE%89%E8%A3%85> "Nouveau") 中分别关于此二者的注释。

为支持最常见的 GPU，请安装 [xf86-video-vesa](<https://archlinux.org/packages/?name=xf86-video-vesa>)包、[xf86-video-ati](<https://archlinux.org/packages/?name=xf86-video-ati>)包、[xf86-video-amdgpu](<https://archlinux.org/packages/?name=xf86-video-amdgpu>)包 和 [xf86-video-fbdev](<https://archlinux.org/packages/?name=xf86-video-fbdev>)包。 

####  声卡驱动

为支持最常见的声卡，请安装 [sof-firmware](<https://archlinux.org/packages/?name=sof-firmware>)包 和 [alsa-firmware](<https://archlinux.org/packages/?name=alsa-firmware>)包。请参阅 [ALSA](<../zh-cn/ALSA.html> "ALSA") 以获取更多关于配置音频设备的信息。 

####  块设备持久化命名

建议在 [fstab](<../zh-cn/Fstab.html> "Fstab") 和启动管理器配置中使用 [UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID")。详情请参阅[块设备持久化命名](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")。 

或者，您可以自行创建 udev 规则为您的磁盘创建符号链接，然后在 [fstab](<../zh-cn/Fstab.html> "Fstab") 和启动管理器配置中使用。详情请参阅 [udev#设置静态设备名](<../zh-cn/Udev.html#%E8%AE%BE%E7%BD%AE%E9%9D%99%E6%80%81%E8%AE%BE%E5%A4%87%E5%90%8D> "Udev")。 

####  内核参数

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 该问题是否依然存在？未链接到错误报告。（在 [Talk:在可移动设备上安装 Arch Linux](<../zh-cn/Talk:%E5%9C%A8%E5%8F%AF%E7%A7%BB%E5%8A%A8%E8%AE%BE%E5%A4%87%E4%B8%8A%E5%AE%89%E8%A3%85_Arch_Linux.html>) 中讨论）

您可能由于各种各样的原因希望禁用 KMS，例如在使用 Intel 显卡时遇到空白屏幕、显示器“无信号”错误等。要禁用 KMS，添加 `nomodeset` 内核参数。详情请参阅[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。 

**警告：** KMS 禁用时某些 [Xorg](<../zh-cn/Xorg.html> "Xorg") 驱动将无法工作。请在您的驱动对应的 wiki 页面上查找详细信息。特别是 Nouveau，它需要 KMS 才能判断正确的分辨率。如果您已添加 `nomodeset`，那么您可能需要在使用 Nvidia 显卡的设备上手动调整分辨率。详情请参阅 [Xrandr](<../zh-cn/Xrandr.html> "Xrandr")。

###  兼容性

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 这里应该独立成节，建议仅生成 fallback 镜像。 (在 [Talk:在可移动设备上安装 Arch Linux](<../zh-cn/Talk:%E5%9C%A8%E5%8F%AF%E7%A7%BB%E5%8A%A8%E8%AE%BE%E5%A4%87%E4%B8%8A%E5%AE%89%E8%A3%85_Arch_Linux.html>) 中讨论)

使用 fallback 镜像可获得最大的兼容性。 

###  最小化磁盘访问

当安装到总写入量有限的设备（如 U 盘、SD 卡等）上时，减少写入量可以延长设备的寿命。这也可以减小写入慢对性能的影响。 

  * 强烈建议在选择文件系统前阅读[性能优化#减少磁盘读写](<../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96.html#%E5%87%8F%E5%B0%91%E7%A3%81%E7%9B%98%E8%AF%BB%E5%86%99> "性能优化")。概括起来，对于基于闪存的磁盘（如 U 盘、SD 卡等），[无日志的 ext4](<https://fenidik.blogspot.com/2010/03/ext4-disable-journal.html>) 应该就可以了，它可通过 `mkfs.ext4 -O "^has_journal" /dev/sdXX` 创建。使用无日志的文件系统的明显的缺点就是在 ungraceful dismount 时会丢失数据。不过要意识到闪存的总写入量是有限的，而日志会占用其中的一部分。由于同样的原因，最好也不要想着 swap 分区了。注意这并不影响安装到可移动硬盘。
  * 您可能想将 [systemd 日志](<../zh-cn/Systemd/Journal.html> "Systemd/日志")配置为在内存中存储日志。为此，可以创建一个配置文件：

    /etc/systemd/journald.conf.d/usbstick.conf
    
    [Journal]
    Storage=volatile
    RuntimeMaxUse=30M

  * 要在网页浏览器和其他不写入关键数据的应用程序中禁用 `fsync` 和相关的系统调用，可以使用来自 [libeatmydata](<https://archlinux.org/packages/?name=libeatmydata>)包 的 `eatmydata` 命令：

    $ eatmydata firefox
    
###  UI 响应速度

高 I/O 负载可能会导致 UI 冻结，特别是在慢磁盘上。[更改 I/O 调度器](<../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96.html#%E6%9B%B4%E6%94%B9_I/O_%E8%B0%83%E5%BA%A6%E5%99%A8> "性能优化")，或者切换到默认使用不同调度器的内核，可以极大地改进 UI 的响应速度。例如 [BFQ](<https://docs.kernel.org/block/bfq-iosched.html>) 可以改进 UI 的响应速度（它在 [linux-zen](<https://archlinux.org/packages/?name=linux-zen>)包 和 [linux-ck](<https://aur.archlinux.org/packages/linux-ck/>)AUR 上默认启用）。 

详见[性能优化#调度算法](<../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96.html#%E8%B0%83%E5%BA%A6%E7%AE%97%E6%B3%95> "性能优化")。 

##  另请参阅

  * [Arch Linux USB](<https://mags.zone/help/arch-usb.html>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-18 ⓘ] \- c-magyar 关于创建持久化 Live USB 安装的精彩内容。
  * [archuseriso](<https://github.com/laurent85v/archuseriso>) \- 用于构建 Arch Linux Live ISO 镜像的配置文件。具有持久存储和加密功能的可启动 USB 驱动器创建工具。
