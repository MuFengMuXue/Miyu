**翻译状态：**

  * 本文（或部分内容）译自 [Mac](<https://wiki.archlinux.org/title/Mac> "arch:Mac")，最近一次同步于 2022-04-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/Mac?diff=0&oldid=724367>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Mac_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Installation guide](<../zh-cn/Installation_guide.html> "Installation guide")
  * [General Recommendations](<../zh-cn/General_Recommendations.html> "General Recommendations")
  * [MacBook5,2 (early-mid 2009)](</wzh/index.php?title=MacBook5,2_\(early-mid_2009\)&action=edit&redlink=1> "MacBook5,2 \(early-mid 2009\)（页面不存在）")
  * [MacBookPro7,1](</wzh/index.php?title=MacBookPro7,1&action=edit&redlink=1> "MacBookPro7,1（页面不存在）")
  * [MacBookPro8,1/8,2/8,3 (2011)](</wzh/index.php?title=MacBookPro8,1/8,2/8,3_\(2011\)&action=edit&redlink=1> "MacBookPro8,1/8,2/8,3 \(2011\)（页面不存在）")
  * [MacBookPro9,2 (Mid-2012)](</wzh/index.php?title=MacBookPro9,2_\(Mid-2012\)&action=edit&redlink=1> "MacBookPro9,2 \(Mid-2012\)（页面不存在）")
  * [MacBookPro10,x](</wzh/index.php?title=MacBookPro10,x&action=edit&redlink=1> "MacBookPro10,x（页面不存在）")
  * [MacBookPro11,x](</wzh/index.php?title=MacBookPro11,x&action=edit&redlink=1> "MacBookPro11,x（页面不存在）")
  * [iMac Aluminum](</wzh/index.php?title=IMac_Aluminum&action=edit&redlink=1> "IMac Aluminum（页面不存在）")
  * [iMac (21.5-inch, Mid 2010)](</wzh/index.php?title=IMac_\(21.5-inch,_Mid_2010\)&action=edit&redlink=1> "IMac \(21.5-inch, Mid 2010\)（页面不存在）")
  * [Apple Fusion Drive](</wzh/index.php?title=Apple_Fusion_Drive&action=edit&redlink=1> "Apple Fusion Drive（页面不存在）")

**警告：**[Arch Linux ARM](<https://archlinuxarm.org/>) 项目提供了对 ARM 架构们的支持。然而，其尚不支持 M1 芯片或后续型号。请参见 [Asahi Linux](<https://asahilinux.org/>) 项目网站了解 M1 芯片版 Mac 上 Linux 支持的情况。Arch Linux ARM 和 Asahi Linux 均为未受到 Arch Linux 官方背书的下游项目。可前往 [Arch Linux ARM 论坛](<https://archlinuxarm.org/forum>)或 [Asahi Linux 社区](<https://asahilinux.org/community>)获取帮助。

在 MacBook（12 寸、Air 或 Pro 版本）或 iMac 上安装 Arch Linux 与在其他电脑上安装非常相似。然而，由于 Mac 特有的硬件配置，存在些许偏差和一些特殊的考虑，因此需要单独的指南。更多背景信息，请参见[安装指南](<../zh-cn/Installation_guide.html> "Installation guide")和 [UEFI](<../zh-cn/UEFI.html> "UEFI")。本指南所包含的安装指导可用于任何受 Linux 内核支持的硬件的 Apple 电脑。请查看“相关页面”（在本页面的右上角）了解特定型号的提示和疑难解答。 

##  概述

具体而言，在 MacBook 上安装 Arch Linux 的步骤可分为： 

  1. **[固件更新](<#%E5%AE%89%E8%A3%85_Mac_OS_X_%E4%BB%A5%E5%8F%8A%E5%9B%BA%E4%BB%B6%E6%9B%B4%E6%96%B0>)[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]**：从干净的、备好份的和最新的 OS X 安装开始总是有帮助的。
  2. **[分区](<#%E5%88%86%E5%8C%BA>)** ：调整 OS X 分区大小或删除其分区来为 Arch Linux 创建分区。
  3. **[配置引导加载器](<#%E9%85%8D%E7%BD%AE%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E5%99%A8>)** ：确保新分区可以引导。
  4. **[安装 Arch Linux](<#%E5%AE%89%E8%A3%85>)** ：真正安装 Arch Linux 的过程。
  5. **[安装后配置](<#%E5%AE%89%E8%A3%85%E5%90%8E%E9%85%8D%E7%BD%AE>)** ：针对 MacBook 特定的配置。

##  固件更新

在进行 Arch Linux 安装之前，确保已为 Macbook 安装好最新的固件更新是很重要的。这步需要 OS X（macOS）来操作。在 OS X（macOS）中，打开 App Store 并检查更新。如果 Mac 找到并安装了任意更新，请确保**重启** 您的电脑，然后再次检查更新以确保所有东西都安装好了。 

**注意：** 如果想卸载或重新安装 OS X（macOS），[Apple](<https://support.apple.com/zh-cn/HT204904>) 对此有很好的说明。

保留 OS X（macOS）安装是比较明智的，因为 Macbook 的固件更新只能用 OS X（macOS）安装。但是，如果打算完全移除 OS X（macOS），请备份以下文件，在 Linux 中调整[色彩配置](<#%E8%89%B2%E5%BD%A9%E9%85%8D%E7%BD%AE>)时会有需要： 
    
    /Library/ColorSync/Profiles/Displays/*
    
接下来阅读[#分区](<#%E5%88%86%E5%8C%BA>)小节。 

##  分区

存储磁盘的分区和其他 PC 或笔记本电脑并无二致。但是，如果打算保留 OS X（macOS）来做双系统，需要对此所有考虑。默认情况下，MacBook 的磁盘使用 GPT 分区表格式化，至少包含了 3 个分区： 

  * **EFI** ：大约 200 MB 的 [EFI 系统分区](<../zh-cn/EFI_system_partition.html> "EFI system partition")。
  * **OS X** ：OS X 安装主分区。使用 [HFS+](<../zh-cn/File_systems.html> "File systems") 文件系统格式化。
  * **Recovery** ：恢复分区，存在于几乎所有搭载 OS X 10.7 及以上版本 MacBook 中。在 OS X 系统中通常被隐藏，但是可以使用分区工具看见它。

**注意：** 使用 [Apple 融合硬盘](</wzh/index.php?title=Apple_Fusion_Drive&action=edit&redlink=1> "Apple Fusion Drive（页面不存在）")的 Mac，分区方案会有所不同。

怎么来分区取决于想安装多少个操作系统。接下来将讲解以下选项： 

  * 单系统：[#仅安装 Arch Linux](<#%E4%BB%85%E5%AE%89%E8%A3%85_Arch_Linux>)
  * 双系统：[#Arch Linux 与 OS X 或其他操作系统共存](<#Arch_Linux_%E4%B8%8E_OS_X_%E6%88%96%E5%85%B6%E4%BB%96%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%85%B1%E5%AD%98>)（ _推荐，这样可以在需要时回到 OS X 系统_ ）
  * 三系统：[#OS X、Windows XP 和 Arch Linux 三系统共存](<#OS_X%E3%80%81Windows_XP_%E5%92%8C_Arch_Linux_%E4%B8%89%E7%B3%BB%E7%BB%9F%E5%85%B1%E5%AD%98>)[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]

###  仅安装 Arch Linux

这种情况最好办。分区操作就和其他可以安装 Arch Linux 的硬件一样。请参考标准[安装指南](<../zh-cn/Installation_guide.html> "Installation guide")了解详情。 

**注意：** 建议在分区之前**禁用** MacBook 启动声音。只需启动进 OS X，将系统音量调至静音，然后在重启进入 Arch Linux 安装媒介。MacBook固件依赖于Mac OS X的配置。请记住，启动声音的音量只能在 OS X 中可靠地修改。

如果想要配置系统以获得全盘加密，请参见 [Dm-crypt/Encrypting an entire system](</wzh/index.php?title=Dm-crypt/Encrypting_an_entire_system&action=edit&redlink=1> "Dm-crypt/Encrypting an entire system（页面不存在）") 了解更多详情。 

不考虑单独 `/home` 分区、加密或 LVM 分区方案，一个非常基本的分区示例如下所示： 
    
    (分区)     (挂载点)    (大小) (类型) (标签)
    partition  mountpoint  size    type  label
    /dev/sda1  /boot       200MiB  vfat  EFI
    /dev/sda2  /swap       adjust  swap  swap
    /dev/sda3  /           remain  ext4  root
    
完成后，就可以继续阅读[#安装](<#%E5%AE%89%E8%A3%85>)小节了。 

###  Arch Linux 与 OS X 或其他操作系统共存

你需要对硬盘进行分区，同时保留用于 OS X 或 Windows 的分区。如果希望保留 OS X，最简单的方法是使用 OS X 的分区工具进行调整，然后使用 Arch Linux 的工具完善。 

**警告：** 如果 OS X 分区使用了 FileVault 2 加密，**必须** 在继续以下过程之前禁用磁盘加密。在调整 OS X 分区大小之后，可以重新启用 FileVault 2。

**步骤** ： 

  * 在 OS X 中，运行 _Disk Utility.app_ （磁盘工具，位于 `/Applications/Utilities`）
  * 在左侧栏选择要进行分区的硬盘（注意不是选择分区！）。点击**分区** 标签页。
  * 点击 **+** 号按钮添加新分区，并选择要给 OS X 和新分区各留存多少空间。请记得新分区会在 Arch Linux 里进行格式化，所以这里可以选择随意设置任意分区类型。
  * 如果上述步骤都顺利完成，那么就可以接着往下走了。如果没有完成，你或许需要在 OS X 里先修好分区问题。
  * **在启动时** 按住 `Alt` 键引导至 Arch 安装媒介或 [LiveUSB](<../zh-cn/USB_flash_installation_media.html> "USB flash installation media")。之后按照[#安装](<#%E5%AE%89%E8%A3%85>)小节进行操作。

在 Arch 安装媒介中，可以重新调整已创建的分区的大小，或者删除分区以对其他分区们进行创建（比如交换分区（swap））。 

**提示：** 为避免弄乱磁盘分区，可使用[交换文件](</wzh/index.php?title=Swapfile&action=edit&redlink=1> "Swapfile（页面不存在）")代替专门的交换分区。另一种解决方案是配置 [LVM](<../zh-cn/LVM.html> "LVM") 将新建的分区作为容器使用。详情请参考链接文章。

####  选项一：EFI

  * 运行 _cgdisk_

  * 删除在 OS X 中用 _Disk Utility.app_ 创建的分区，并为 Arch Linux 创建必要的分区。OS X 喜欢看看分区后面有没有 128 MiB 大小的空隙，因此在 OS X 的分区后创建第一个分区时，当 _cgdisk_ 询问分区的第一个扇区大小时输入 **+128M** 。了解更多关于 Apple 分区策略的信息可阅读[这里](<https://developer.apple.com/library/mac/technotes/tn2166/_index.html#//apple_ref/doc/uid/DTS10003927-CH1-SUBSECTION5>)。下面举一个简单的例子（没有 LVM 和加密）：

**注意：**

  * 交换分区在 4GB 或以上内存的机器上可有可无。可以之后创建**[交换文件](<../zh-cn/Swap_file.html> "Swap file")** 。
  * 最简单的双系统引导选项是从 OS X 内部安装 rEFInd 到其根目录 (`install.sh` 脚本的默认设置)。接着，从安装压缩包中复制 driver（驱动）文件夹到新的 rEFInd 位置，并在 `refind.conf` 配置文件中取消对 _"scan_all_linux_kernels"_ 行和 _"also_scan_dirs"_ 选项的注释。之后，可以通过 Arch 的 `/boot` 目录下放置 `refind_linux.conf` 文件来配置启动选项。
  * 如果想能从 Apple 引导加载器中引导 GRUB，可以创建一个小的 hfs+ 格式分区（为了方便，请稍后用 OS X 在 _Disk Utility.app_ 中对其格式化）。按照 GRUB EFI 安装步骤操作，并将创建的 hfs+ 分区挂载到 `/efi` 目录。最后，让分区在祝福声中在 OS X 中完成配置。这会将 GRUB 设为默认引导选项（仍然需要在启动时按住 `Alt` 键来转入 Mac 引导选项屏。参见 [https://mjg59.dreamwidth.org/7468.html）。](<https://mjg59.dreamwidth.org/7468.html%EF%BC%89%E3%80%82>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-21 ⓘ]
  * OS X 的 EFI 分区可与 Arch Linux 共享，因此可以不用为 Arch 专门创建一个额外的 EFI 分区。

**注意：** 了解更多有关分区的信息，参见[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning")一文。
    
    (分区)     (挂载点)     (大小)         (类型) (标签) 
    partition  mountpoint  size          type  label
    /dev/sda1  /efi        200MiB        vfat  EFI
    /dev/sda2  -           ?             hfs+  OS X
    /dev/sda3  -           ?             hfs+  Recovery
    /dev/sda4  -           100MiB        hfs+  Boot Arch Linux from the Apple boot loader (optional)
    /dev/sda5  /boot       100MiB        boot  boot
    /dev/sda6  -           ?             swap  swap (optional)
    /dev/sda7  /           15-20GiB      ext4  root
    /dev/sda8  /home       remaining     ext4  home
    
完成后，就可以继续阅读[#安装](<#%E5%AE%89%E8%A3%85>)小节了。 

####  选项二：BIOS 兼容

  * 以 root 身份运行 _parted_ 。

  * 删除空分区，并按照自己的想法为其他要安装的操作系统重新分区空间。请注意，主引导记录（MBR）限制了主分区数量不能超过 4 个（包括 EFI 分区）。这样的话也就两个主分区留给 Arch 了。一种分区策略是分配一个系统（根）分区和一个家（home）分区，并使用交换文件（笔者没有尝试过使用逻辑分区）。另一种策略就是专门分配一个分区用于共享（参见下文）。

  * 下一步，为需要的那些分区创建新的文件系统，尤其是要包含 `/boot` 的那个分区。如果不确定怎么使用 `mkfs.ext2`（或别的什么命令），请运行 `/arch/setup` 来逐步解决前面的问题，直到来到 Prepare Hard Drive（准备硬盘）这一步，并使用 _"Manually configure block devices ..."（手动配置块设备)_ 选项，然后退出安装器。这很必要，会便于 rEFIt 在下一步在主引导记录（MBR）中设置分区类型（没有文件系统的话，rEFIt 似乎会忽略由 parted 设置的分区类型），没有这一步的话 GRUB 会拒绝安装到相应的分区上。

  * 此时，应当重启电脑，让 rEFIt 来修复磁盘上的分区表（如果不这样做，那或许稍后你需要重新安装 GRUB 来让 Mac 认出 Linux 分区）。当进入到 rEFIt 菜单后，选择 **update partition table（更新分区表）** ，然后按 `y`。重启。

  * 完成了，可以继续按照[#安装](<#%E5%AE%89%E8%A3%85>)小节操作。

##  配置引导加载器

###  搭配 systemd-boot 使用 Apple 原生引导加载器（建议）

Apple 原生的 EFI 引导加载器会读取位于 `/EFI/BOOT/BOOTX64.EFI` 的 [EFI 系统分区](<../zh-cn/EFI_system_partition.html> "EFI system partition")下的 `.efi` 文件。幸运的是，这也是 [systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") 二进制文件的默认安装位置。这意味着，使用 _systemd-boot_ 来引导 Linux 会非常简单。 

  * 首先，确保已经将 EFI 系统分区挂载到 `/boot`
  * 正常进行[#安装](<#%E5%AE%89%E8%A3%85>)过程
  * 进入到 chroot 环境后，输入以下命令安装 _systemd-boot_ ：

    # bootctl --path=/boot install

上述命令会将 _systemd-boot_ 二进制文件复制到 `/boot/EFI/BOOT/BOOTX64.EFI`，并添加 _systemd-boot_ 自身作为由 EFI 引导管理器加载的默认 EFI 应用（默认引导条目）。 

  * 继续进行 [systemd-boot#配置](<../zh-cn/Systemd-boot.html#Configuration> "Systemd-boot")以正确配置引导加载器

下次重启时，按住 Option 键显示 Apple 引导管理器，后者在启动 MacBook 时应该会显示 Arch Linux 条目（其可能会显示为 `EFI Boot` 引导选项）。 

**提示：** 如果将 Arch Linux 与 OS X 安装在一起，可以从 OS X 中的系统“设置”中更改默认引导位置。如果 Arch Linux 没有显示为可能的引导选项，则必须在选择引导选项之前在 OS X 中挂载 EFI 系统分区： 
    
    $ diskutil mount disk0s1

###  使用苹果原生的引导器，结合 GRUB 使用

尽管使用了UEFI，但Mac原生的EFI引导器 [[1]](<http://refit.sourceforge.net/myths/%EF%BC%8C%E4%B8%8D%E4%BD%BF%E7%94%A8EFI%E5%88%86%E5%8C%BA%E8%BF%9B%E8%A1%8C%E5%90%AF%E5%8A%A8>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-21 ⓘ] 。相反，它在内部和外部驱动器的所有分区里寻找 .efi 文件，并在满足某些条件的情况斗它们显示为可能的启动选项。例如，Mac可以在根据以下检查后检测到现有的OS X安装： 

  * 存在 HFS+ 或 APFS 格式分区
  * 该分区包括分区ID `af00`
  * 该分区的根目录存在`mach_kernel`文件
  * 该分区`/System/Library/CoreServices`下存在`boot.efi`文件

这意味着，将Arch安装配置成能被MacBook引导器自动识别的情况是可能的。此外，它只需要一个正确格式化的 `/boot`分区。这种方法的好处是，它可以与OS X很好地共存，并允许避免其他启动加载器，如rEFInd。然而这需要手动配置。下面的步骤将说明如何使用GRUB进行这种配置。 

  * 首先，在配置新的Arch安装时，创建一个单独的`/boot`分区。Arch的ISO中提供了许多工具，例如'_cgdisk_ 。
  * 确保该分区至少有250MB大小，因为它将用于存储内核以及将来要安装的任何自定义内核。此外，确保分区类型被设置为Apple HFS/HFS+（在fdisk/cgdisk中显示为`Apple HFS/HFS+`，在gdisk中显示为`af00`）。
  * 由于Arch安装ISO不包括[hfsprogs](<https://aur.archlinux.org/packages/hfsprogs/>)AUR包，我们需要在安装环境中安装它，然后再继续将新分区格式化为HFS+，安装[hfsprogs](<https://aur.archlinux.org/packages/hfsprogs/>)AUR，然后：

  1. modprobe hfsplus

    # mkfs.hfsplus /dev/sd**Xp** -v "Arch Linux"
    
    注意：更换 /dev/sd**Xp** 与适当的设备和**p** artition编号。
    
  * 完成之后，继续安装步骤

  * 当你 chroot 到新环境之后，安装 [grub](<https://archlinux.org/packages/?name=grub>)包 和 [efibootmgr](<https://archlinux.org/packages/?name=efibootmgr>)包软件包。
  * 另外，创建一个假的 `mach_kernel` 文件

    # touch /boot/mach_kernel
    # mkdir -p /boot/EFI/arch && touch /boot/EFI/arch/mach_kernel
    
     # grub-install --target=x86_64-efi --efi-directory=/boot
    
在这之后，不要忘记创建一个基础的配置文件 
    
    # grub-mkconfig -o /boot/grub/grub.cfg
    
    如你所见，boot.efi的目录结构并不正确，因为/System/Library/CoreServices目录不应该是/boot/EFI/文件夹的子目录。由于这个原因，我们需要将boot.efi存根重新定位到MacBook引导加载器能够识别的位置。
    
     # mv /boot/EFI/arch/System/ /boot/
     # rm -r /boot/EFI/
    
    在这之后，你需要创建下列文件
    
    /boot/System/Library/CoreServices/SystemVersion.plist
    
    <?xml version="1.0" encoding="UTF-8"?>
    <plist version="1.0">
    <dict>
           <key>ProductBuildVersion</key>
           <string></string>
           <key>ProductName</key>
           <string>Linux</string>
           <key>ProductVersion</key>
           <string>Arch Linux</string>
    </dict>
    </plist>

在下次重新启动时，在启动 MacBook 时按住 option 键时显示的引导器应将 Arch Linux 显示为可能的启动选项。 选择该选项将引导 GRUB。 

好了！GRUB 现在已经是 MacBook 引导器了，你可以启动新安装的 Arch Linux 

**注意：** 安装后，可以选择设置将在 MacBook 引导加载程序中显示的自定义图标。 为此，您需要安装 [wget](<https://archlinux.org/packages/?name=wget>)包、[librsvg](<https://archlinux.org/packages/?name=librsvg>)包 和 [libicns](<https://archlinux.org/packages/?name=libicns>)包 软件包。 之后，只需执行以下命令： 
    
    $ wget -O /tmp/archlinux.svg <https://archlinux.org/logos/archlinux-icon-crystal-64.svg>
    $ rsvg-convert -w 128 -h 128 -o /tmp/archlogo.png /tmp/archlinux.svg
    # png2icns /boot/.VolumeIcon.icns /tmp/archlogo.png
    $ rm /tmp/archlogo.png
    $ rm /tmp/archlinux.svg
    
显然，你可以将 Arch logo 更换为你喜欢的任何其他 logo 

###  一种简便的方法

在安装 Arch Linux 之前，创建一个额外的分区，格式化为 FAT32 并挂载在 /mnt/efi。在安装完成后，chroot 进入 /mnt，并安装引导程序 
    
    # pacman -S grub efibootmgr 
    
\--removable 参数可以解决很多型号 Mac 的主板 NVRAM 兼容性问题。 
    
    # grub-install --target=x86_64-efi --efi-directory=/efi --removable
    # grub-mkconfig -o /boot/grub/grub.cfg
    
**注意：** 除此之外，如果你的 Mac 是一些较老的型号，此方法可能并不适用。

###  其他方式

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 描述其他设置的boot loader设置的章节应该被修改，并重新组织成更易读的方式 (在[Talk:Mac](<../zh-cn/Talk:Mac.html>)讨论)

。 

###  从GRUB直接启动

在efi上直接启动GRUB2而不用rEFIt是可以的。以下的操作在MacBook7,1上是可行的。建议将GRUB安装在fat32或者HFS+分区上，ext2或者ext3应该也行。GRUB的苹果加载命令在7,1上还暂时不能使用，但可以用过下面的补丁实现[补丁地址](<https://savannah.gnu.org/bugs/index.php?33185>)。 

GRUB装上硬盘分区后，固件需要知道从哪儿启动它。这步操作可以在OS X或者OS X安装光盘。下面的命令指明了GRUB是安装在OS X系统的/efi/grub中 
    
    sudo bless --folder /efi/grub --file /efi/grub/grub.efi
    
###  编译

有些型号可能需要将EFI_ARCH设置成i386。 
    
    bzr branch --revision -2 bzr://bzr.savannah.gnu.org/grub/trunk/grub grub
    cd grub
    ./autogen.sh
    patch -p1 < appleloader_macbook_7_1.patch
    export EFI_ARCH=x86_64
    ./configure --with-platform=efi --target=${EFI_ARCH} --program-prefix=""
    make
    cd grub-core
    ../grub-mkimage -O ${EFI_ARCH}-efi -d . -o grub.efi -p "" part_gpt part_msdos ntfs ntfscomp hfsplus fat ext2 normal chain boot configfile linux multiboot
    cp grub.efi *.mod *.lst yourinstalllocation
    
####  grub.cfg示例

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** kernel26 (在[Talk:Mac](<../zh-cn/Talk:Mac.html>)讨论)

此处应该有更好的方法来加载Windows系统。 
    
    set debug=video
    insmod efi_gop
    
    menuentry "Arch Linux EFI" {
      set root=(hd0,3)
      #search --set -f /boot/vmlinuz-linux-efi-physical
      #loadbios /boot/vbtrace_bios.bin /boot/int10.bin
      linux /boot/vmlinuz-linux-efi-physical root=/dev/sda3 reboot=pci resume=/dev/sda3 resume_offset=151552
      initrd /boot/initramfs-linux-efi-physical.img
    }
    
    menuentry "MacOSX" {
      set root=(hd0,2)
      # Search the root device for Mac OS X's loader.
      #search --set -f /usr/standalone/i386/boot.efi
      # Load the loader.
      chainloader /usr/standalone/i386/boot.efi
    }
    
    menuentry "Windows 7" {
      appleloader HD
    }
    
    menuentry "Boot from CD" {
      appleloader CD
    }
    
    menuentry "Boot from USB" {
      appleloader USB
    }

##  安装

**注意：** 本部分安装过程只是用于Mac OS X与Arch Linux共存的情况，如果你只想单独使用Arch Linux，可以按照官方安装指南，然后跳到[安装后配置](<#%E5%AE%89%E8%A3%85%E5%90%8E%E9%85%8D%E7%BD%AE>)

  * 从Arch Linux安装光盘启动

**注意：** 有些MacBook用户反映键盘不能正确响应，那就按照下面的参数来启动键盘。
    
    boot: arch noapic irqpoll acpi=force
    
  * 以root登录

  * 打开Arch Linux安装程序

    /arch/setup
    
  * 按照[官方安装文档](<../zh-cn/Installation_guide.html> "Installation guide")中说明的过程来做，但是在下面几个部分中请留意： 
    * 在[准备磁盘](<../zh-cn/Installation_guide.html#Partition_the_disks> "Installation guide")部分，只要做设置磁盘挂载这步，注意要设对磁盘挂载点。
    * 在[安装启动器](<../zh-cn/Arch_boot_process.html#Boot_loader> "Arch boot process")部分，编辑menu.lst文件，添加**reboot=pci** 到**kernel** 行的末尾，例如下面这行：
          
          kernel /vmlinuz-linux root=/dev/sda5 ro reboot=pci

这样你的MacBook才能从Arch Linux正常重启
    * 还是在[安装启动器](<../zh-cn/Arch_boot_process.html#Boot_loader> "Arch boot process")部分，将GRUB安装至`/boot`所在的分区。

**警告：** 别把GRUB安装到 _/dev/sda_ 这样的地方！！！这样做会造成系统不稳定。

    * 在[配置系统](<../zh-cn/Installation_guide.html#Configure_the_system> "Installation guide")部分，编辑 /etc/mkinitcpio.conf，添加**usbinput** 到**HOOKS** 行的**autodetect** 之后。这样才能在Arch Linux启动之前加载键盘驱动

  * 安装完成之后就可以重启系统了。

    # reboot
    
  * 把Arch Linux安装光盘从光驱中退出。

##  安装后配置

###  微码

  * 由于 x86_64体系的Mac使用的是Intel芯片，你还需要安装Intel微码 [intel-ucode](<https://archlinux.org/packages/?name=intel-ucode>)包

    # pacman -S intel-ucode
    
### Xorg

按照[Xorg](<../zh-cn/Xorg.html> "Xorg")来安装Xorg。 

####  视频

不同的MacBook有不同型号的显卡，可以通过下面命令来查看显卡种类 
    
    $ lspci | grep VGA
    
  * 如果返回的字符串中包含**intel** ，那你只需要安装**xf86-video-intel** 驱动，用如下命令：

    # pacman -S xf86-video-intel
    
  * 如果返回的是nVidia，可以参看[NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")

  * 如果返回ATI或者AMD，参见[ATI](<../zh-cn/ATI.html> "ATI")

#####  NVIDIA注意

**提示：** MacBookPro 6,2 - 使用合适的[NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")驱动，在使用[NVIDIA#Hardware accelerated video decoding](<../zh-cn/NVIDIA.html#Hardware_accelerated_video_decoding> "NVIDIA")

对于使用NVIDIA显卡的MacBook，背景亮度可以通过[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")中的[nvidia-bl-dkms](<https://aur.archlinux.org/packages/nvidia-bl-dkms/>)AUR{包解决。 

#####  MacBook 6,2+-EFI

截至2011年4月30日，nvidia驱动在此类EFI型号的机子下不能正常工作。可以了解一下[mesa-git](<https://aur.archlinux.org/packages/mesa-git/PKGBUILD>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-21 ⓘ]这个包。 

####  触摸板

触摸板应该已经有了基本的功能。可以安装AUR中的[xf86-input-multitouch-git](<https://aur.archlinux.org/packages/xf86-input-multitouch-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]包来达到和Mac OS X类似的多点触控效果，最多支持三点触控，包含了三指水平与垂直滑动。可以从[项目主页](<https://bitmath.org/code/multitouch/>) 获取更多消息。 

xf86-input-multitouch-git除了编辑源代码外不支持配置。一些用户也正面临这从palm上得到错误的点击。现在有个可定制度更高的包[xf86-input-mtrack-git](<https://aur.archlinux.org/packages/xf86-input-mtrack-git/>)AUR。在其[readme](<https://github.com/BlueDragonX/xf86-input-mtrack>)中能得到更多配置信息。 

下面的配置在MacBook 7,1中正常工作 
    
     Option "Thumbsize" "50"
     Option "ScrollDistance" "100"
    
可能你还需要添加下面的内容 
    
    MatchDevicePath "/dev/input/event10"
    
在更旧的MacBook机型上，比如MacBook 2,1中，可能需要安装xf86-input-synaptics包才能正常工作。可以查看[Touchpad Synaptics](<../zh-cn/Touchpad_Synaptics.html> "Touchpad Synaptics")获取更多信息。 

####  键盘

MacBook的键盘默认是能正常工作的。如果想切换fn键，可以查看[Apple Keyboard](</wzh/index.php?title=Apple_Keyboard&action=edit&redlink=1> "Apple Keyboard（页面不存在）")。 

可以通过**xbindkeys** 来重新设置键，或者通过DE配置。有另一种很好的方法，安装[pommed](<https://aur.archlinux.org/packages/pommed/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

根据你MacBook的硬件来配置**/etc/pommed.conf** ，可以以**/etc/pommed.conf.mac** 或者**/etc/pommed.conf.ppc** 为模板来建立这个配置。 

#####  NVIDIA配置

如果在使用 pommed 后亮度仍然不正常， 请确认你安装了 [nvidia-bl-dkms](<https://aur.archlinux.org/packages/nvidia-bl-dkms/>)AUR 并添加以下命令： 
    
    find . -name "*" -exec sed -i 's/mbp_backlight/nvidia_backlight/' '{}' \;
    
到 pommed PKGBUILD build() 函数中，然后重新编译。引用自 [this forum post](<https://bbs.archlinux.org/viewtopic.php?id=105091>). 

另一个解决方案是修改 pommed PKGBUILD build(): 
    
    find . -name "*" -exec sed -i 's/nvidia_backlight/apple_backlight/' '{}' \;
    
如果上面两种方法都不能解决，那么你需要尝试以下方法： 

运行 nvidia-settings，编辑 '/etc/X11/xorg.conf' 添加以下代码到 Device 部分： 
    
    Option "RegistryDwords" "EnableBrightnessControl=1"
    
保存并重启，检查亮度调节是否正常工作。 点击查看更多信息 [Ubuntu MacBookPro5,5](<https://help.ubuntu.com/community/MacBookPro5-5/Precise#LCD>)

### Wi-Fi

不同型号的MacBook使用不同的网卡模块。 

使用以下命令查看你的Macbook使用的网卡型号： 
    
    # lspci | grep Network
    
  * 如果你使用的是 Atheros，无需任何设定即可正常工作。

  * 如果你使用的是 Broadcom，请在 [Broadcom BCM4312](<../zh-cn/Broadcom_BCM4312.html> "Broadcom BCM4312") 页面查看教程。

  * MacBook 5.0 和 6.0 使用 BCM43xx，在 [Broadcom wireless](<../zh-cn/Broadcom_wireless.html> "Broadcom wireless") 页面查看有关 broadcom-wl 驱动的部分。 网络接口在重启后会互换，所以最好使用 udev 规则来定义它们（教程在 [Broadcom wireless](<../zh-cn/Broadcom_wireless.html> "Broadcom wireless") 页面）。

  * MacBook 8.1 使用 BCM4331，即不被Linux支持 (3.0 和 3.1) ，Broadcom 也没有提供闭源驱动，直到在 Linux 3.2 中才被初步支持。如果你需要在旧的内核上使用，你需要安装这里的驱动[compat-drivers](<https://backports.wiki.kernel.org/index.php/Documentation/compat-drivers>)

**注意：** 如果你经常丢失连接，你需要关闭无线电源管理。

###  电源管理

####  笔记本模式工具

####  睡眠（内核挂起）

####  休眠

###  声音配置

###  蓝牙

###  iSight配置

###  温度感应

###  色彩配置

###  苹果远程控制

###  HFS分区共享

###  HFS+ 分区

###  Home目录共享

####  在OS X中

#####  第一步：改变UID与GID

#####  第二步：改变Home目录权限

####  在Arch中

###  避免GRUB启动前EFI长时间执行

###  关闭启动响铃

## rEFIt

**注意：** rEFIt只是在开机是给你提供OS X和Linux的启动菜单而已。如果没有这个需求的话，rEFIt不是必须的。

详情参考[refit myths](<https://refit.sourceforge.net/myths/>). 

在OS X下，从[Refit主页](<https://refit.sourceforge.net/>)下载".dmg"格式的安装包，并像其他苹果软件一样安装。 

**注意：** 如果你此前已经对磁盘分过区的话（比如准备安装ArchLinux之前的准备），那rEFIt默认是不启用的。你需要手动执行安装到系统路径/efi/refit/的"enable.sh"脚本

手动启用rEFIt的方法： 

  * 打开**终端** ：
  * 执行**cd /efi/refit; ./enable.sh** 命令

###  rEFIt可能会遇到的问题

如果你在安装Arch或者rEFIt后遇到了问题，特别是启动时在启动菜单中看不到启动项，或者出现下面的GRUB提示时： 
    
    GRUB>_
    
请您参考下 <http://mac.linux.be/content/problems-refit-and-grub-after-installation>

该页面将会教你如何启动的Arch系统，将有问题的Arch系统挂载上去，然后chroot进入该系统，通过gptsyc重新安装GRUB。文中提到的那些用于debian系统的命令基本上都可以在Arch上工作。不过注意不要将GRUB安装错地方了（wrong spot怎么翻译？） 

你可从 <https://packages.debian.org/sid/gptsync> 获取到gptsync。 或者通过下面两个命令之一分别下载32/64位版本的： 
    
    wget <http://ftp.us.debian.org/debian/pool/main/r/refit/gptsync_0.14-2_i386.deb>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ]
    wget <http://ftp.us.debian.org/debian/pool/main/r/refit/gptsync_0.14-2_amd64.deb>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ]
    
由于是.deb包，所以你可能需要先安装deb2targz 
    
    pacman -S deb2targz
    
##  参考资料

  * <http://www.netsoc.tcd.ie/~theorie/interblag/2010/01/30/installing-arch-linux-on-a-mac-pro/>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-21 ⓘ]
  * <http://allanmcrae.com/2010/04/installing-arch-on-a-macbook-pro-5-5/>
  * <https://web.archive.org/web/20130917192747/https://blog.abhijeetr.com/2011/08/triple-boot-archlinux-windows-7-and-mac.html>

##  MacBook Air (4,2) 内核补丁

Linus的内核树中的当前版本（Linux 3.0.7）中，包含几个问题。我（telmich）已经搜集了下面几个问题的修复补丁： 

  * 分辨率是1280x800而非正确的1440x900
  * 触摸板不能正常工作或被检测为Synaptics
  * FN + F1～F12组合键不工作（例如：fn啥都干不了）
  * FN+F5～F12等多媒体键映射错误
  * 网络处理的驱动/brcmsmac驱动（Hanging network applications / brcmsmac driver）

您可以从 <http://git.schottelius.org/?p=foreign/linux-macbook-air;a=summary>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2020-08-04 ⓘ] 获取到打好补丁的内核，其中包括如下分支： 

  1. keith-jiri: Keith Packard提供的显卡驱动补丁、Jiri Kosina提供的FN功能键补丁
  2. keith-jiri-brcmsmac: 上面提到的补丁加上网络处理的驱动
  3. jiri-kbdmapping: FN功能键和映射关系修复补丁
  4. keith-jiri-kbdmapping: 第一个分支加上多媒体键补丁
  5. keith-jiri-kbdmapping-brcmsmac: 以上所有的集合 (**不确定的情况下，推荐使用这个分支**)

你可以很简单的用当前ArchLinux的配置文件来编译内核： 
    
    # 请先通过git检出对应分支的源代码!
    cd linux-macbook-air
    
    # 使用当前的配置作为基础
    zcat /proc/config.gz > .config
    
    # 编译内核时，可能会询问几个未配置的选项
    make -j5
    