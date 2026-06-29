**翻译状态：**

  * 本文（或部分内容）译自 [Syslinux](<https://wiki.archlinux.org/title/Syslinux> "arch:Syslinux")，最近一次同步于 2020-07-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Syslinux?diff=0&oldid=626182>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Syslinux_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Arch Boot Process](<../zh-cn/Arch_Boot_Process.html> "Arch Boot Process")

[Syslinux](<https://en.wikipedia.org/wiki/SYSLINUX> "wikipedia:SYSLINUX")是一个启动加载器集合，可以从硬盘、光盘或通过 [PXE](<../zh-cn/Preboot_Execution_Environment.html> "Preboot Execution Environment") 的网络引导启动系统。支持的[文件系统](<../zh-cn/File_systems.html> "File systems")包括 [FAT](<https://en.wikipedia.org/wiki/File_Allocation_Table> "wikipedia:File Allocation Table")，[ext2](<https://en.wikipedia.org/wiki/ext2> "wikipedia:ext2")，[ext3](</wzh/index.php?title=Ext3&action=edit&redlink=1> "Ext3（页面不存在）")，[ext4](<../zh-cn/Ext4.html> "Ext4") 和非压缩单设备 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 文件系统。 

**警告：** 在 Syslinux 6.03 版本中，启动加载器可能不支持某些文件系统的部分功能。详情请参考 [[1]](<https://wiki.syslinux.org/wiki/index.php/Filesystem>)。

**注意：** Syslinux 本身只能访问其所在分区上的数据，参阅 [#链式加载](<#%E9%93%BE%E5%BC%8F%E5%8A%A0%E8%BD%BD>) 来了解如何绕过这个限制。

##  BIOS 系统

###  启动流程

  1. **第一阶段 - 第一部分** \- **加载MBR** 电脑启动时，BIOS 会先加载磁盘开始的 440 字节 [MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#Master_Boot_Record> "Partitioning")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节] 启动代码 (`/usr/lib/syslinux/bios/mbr.bin` 或 `/usr/lib/syslinux/bios/gptmbr.bin`)。
  2. **第一阶段 - 第二部分** \- **寻找活动分区** 第一阶段的MBR启动代码会寻找活动分区（设置了可启动标记的 MBR 分区），此处我们假设是 `/boot` 分区。
  3. **第二阶段 - 第一部分** \- **执行卷启动记录程序** MBR 启动代码会执行上面找到的 `/boot` 分区的卷启动记录程序（VBR，volume boot record）。对于 Syslinux 来说，VBR 就是由 `extlinux --install` 命令创建的 `/boot/syslinux/ldlinux.sys` 位于开始扇区的部分。请注意 `ldlinux.sys` 和 `ldlinux.c32` 是不同的。
  4. **第二阶段 - 第二部分** \- **执行`/boot/syslinux/ldlinux.sys`** VBR 会加载 `ldlinux.sys` 剩余的部分。`ldlinux.sys` 所处在的扇区位置不可更改，否则 syslinux 无法启动。

**注意：** 对于 Btrfs 来说，因为文件不断移动导致`ldlinux.sys`扇区的位置不断变化，上述的方法将不会工作。因此在 Btrfs 中整个 `ldlinux.sys` 文件会直接紧接着嵌入卷启动记录程序，而不是像其他文件系统那样保存在 `/boot/syslinux/ldlinux.sys` 处。

  5. **第三阶段** \- **加载`/boot/syslinux/ldlinux.c32`** `ldlinux.sys` 加载剩下的 syslinux 的核心部分 `/boot/syslinux/ldlinux.c32`（这部分是因为文件大小限制无法放入 `ldlinux.sys` 中的核心模块）。`ldlinux.c32` 文件应该在每一个装有 syslinux 的实例中出现，并且与分区中的 `ldlinux.sys` 版本相匹配，否则 Syslinux 将无法启动。更多资料请参阅 [[2]](<https://bugzilla.syslinux.org/show_bug.cgi?id=7>)。
  6. **第四阶段** \- **查找并加载配置文件** 当 syslinux 完全加载完毕，它将自动查找配置文件 `/boot/syslinux/syslinux.cfg` (或某些情况下的 `/boot/syslinux/extlinux.conf`)，如果找到即加载。否则会进入 Syslinux `boot:` 的命令提示符。这一步和剩下的**非核心** Syslinux 部分(除 `lib*.c32` 和 `ldlinux.c32`的`/boot/syslinux/*.c32` 模块) 需要提供 `/boot/syslinux/lib*.c32` (库)模块[[3]](<https://wiki.syslinux.org/wiki/index.php/Common_Problems#ELF>)。同样，{ic|lib*.c32}} 库模块和非核心的 `*.c32` 模块需要与分区中的 `ldlinux.sys` 版本相匹配。

###  在 BIOS 上安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [syslinux](<https://archlinux.org/packages/?name=syslinux>)包。 

**注意：**

  * [GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "Partitioning") 支持需要安装软件包 [gptfdisk](<https://archlinux.org/packages/?name=gptfdisk>)包。请参考[#自动安装](<#%E8%87%AA%E5%8A%A8%E5%AE%89%E8%A3%85>)部分。
  * [FAT](<../zh-cn/FAT.html> "FAT") 支持需要安装软件包 [mtools](<https://archlinux.org/packages/?name=mtools>)包。

安装软件包并不是安装启动加载器。在安装完相关的包后，还需要安装启动加载器代码（到适合的位置，一般是 VBR）才能启动系统；接下来的部分对您的特定系统的特性提供了替代的指令。 

####  自动安装

**注意：** 脚本 `syslinux-install_update` 是 Arch Linux 特有的，并不被 Syslinux 的上游提供/支持。请不要向上游，而是直接向 [Arch Bug Tracker](<https://bugs.archlinux.org/>) 提交关于这个特定脚本的 bug 报告。

  * 执行完 `syslinux-install_update` 脚本后，请不要忘记按照[#配置](<#%E9%85%8D%E7%BD%AE>)和[#内核参数](<#%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0>)两节编辑 `/boot/syslinux/syslinux.cfg`。

**警告：**`syslinux-install_update` 脚本很有可能会设置一个与您的特定系统不同的默认根分区。将 `/boot/syslinux/syslinux.cfg` 文件中的根分区修改正确对于成功启动是至关重要的。参见[#内核参数](<#%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0>)。

syslinux-install_update脚本将自动安装启动加载器代码（一般到 VBR）、复制 `*.c32` 模块到`/boot/syslinux`、设置分区启动标记并将启动代码安装到 MBR。它可以处理软 RAID、[MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#Master_Boot_Record> "Partitioning")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节] 和 [GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "Partitioning") 磁盘。 

如果您使用分开的启动分区，请用 `lsblk` 命令确保它们都已被挂载。如果您没有看到 `/boot` 挂载点，请在继续之前将其挂载。 

  * `syslinux-install_update` 的参数：`-i` (安装文件)，`-a` (将活动分区标上启动标记)，`-m` (安装 MBR 启动代码): 如果 
        
        # syslinux-install_update -i -a -m

命令失败并报错 _Syslinux BIOS install failed_ ，问题可能出在 `extlinux` 可执行文件不能找到包含 `/boot` 的分区：

    # extlinux --install /boot/syslinux/
    
    extlinux: cannot find device for path /boot/syslinux
    extlinux: cannot open device (null)
    
例如，这可能发生在从 [LILO](</wzh/index.php?title=LILO&action=edit&redlink=1> "LILO（页面不存在）") 升级时，后者在引导当前的自定义内核时，将诸如 `root=/dev/sda1` 的内核命令行参数转写成了等效的数字参数 `root=801`。这可以从 `/proc/cmdline` 和 `mount` 等命令的输出确认。 可以通过向 `extlinux` 手动指定 `--device=/dev/sda1` 来解决下文手动安装时的问题，或者先重启到现有的Arch Linux内核，这样会使用 initramfs 来避免此问题。 

**注意：**

  * 如果您现在重新启动系统，则会出现 Syslinux 的提示符。如果想要实现系统自动引导或显示引导目录，您需要创建（或编辑）配置文件。
  * 如果您位于另一个根目录（例如，从安装磁盘上），则可以通过 chroot，重定向后安装：

    # syslinux-install_update -i -a -m -c /mnt
    
  * 现在您需要按照接下来的[#配置](<#%E9%85%8D%E7%BD%AE>)和[#内核参数](<#%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0>)两节编辑 `/boot/syslinux/syslinux.cfg`文件。

####  手动安装

**注意：** 如果您尝试使用Live CD拯救已安装的系统，请确保在执行这些命令之前已经 [chroot](<../zh-cn/Chroot.html> "Chroot") 到目标系统。否则您必须在所有文件（除了`/dev/`）路径之前添加挂载点。

您计划安装Syslinux的启动分区必须包含 FAT，ext2，ext3，ext4 或 Btrfs 文件系统。您不必把它安装在文件系统的根目录上，比如把磁盘 `/dev/sda1` 挂在到 `/boot`。 例如，可以在`syslinux`子目录里安装 Syslinux: 
    
     # mkdir /boot/syslinux
    
如果您希望使用除基本引导提示之外的任何目录或配置，请把 `/usr/lib/syslinux/bios/` 里的所有的 `.c32` 文件复制到 `/boot/syslinux/` 中。请不要使用符号链接。 
    
     # cp /usr/lib/syslinux/bios/*.c32 /boot/syslinux/     
    
现在安装启动加载器。对 挂载后的 FAT，ext2/3/4，或 btrfs 启动分区使用 _extlinux_ 安装: 
    
    # extlinux --install /boot/syslinux
    
替代的，对一个**没有被挂载** 的 FAT 启动分区使用 _syslinux_ 安装: 
    
     # syslinux --directory syslinux --install /dev/sda1
    
在此之后，继续安装适用于对应分区表的 Syslinux 引导代码： 

  * [#MBR 分区表](<#MBR_%E5%88%86%E5%8C%BA%E8%A1%A8>)上会安装 `mbr.bin`
  * [#GPT 分区表](<#GPT_%E5%88%86%E5%8C%BA%E8%A1%A8>)上会安装 `gptmbr.bin`

这些会在下面的内容中详细描述。 

更多信息，请参考 [MBR 分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#Master_Boot_Record> "Partitioning")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]。 

**提示：** 如果您不确定您的分区表类型，可以通过 `blkid -s PTTYPE -o value /dev/sda` 来检查。

**注意：** 对于一个无盘安装实例，不需要向MBR中安装Syslinux 引导代码。您可以跳过这一段，直接跳到[#配置](<#%E9%85%8D%E7%BD%AE>)部分。更多信息请参考[[4]](<https://unix.stackexchange.com/questions/103501/boot-partiotionless-disk-with-syslinux>)。

#####  MBR 分区表

对于一个安装在 [MBR 分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#Master_Boot_Record> "Partitioning")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]上的实例，请确保您的启动分区已经被标记为活动分区（有启动标志）。您可以用 [fdisk](<../zh-cn/Fdisk.html> "Fdisk")、[parted](<../zh-cn/Parted.html> "Parted") 等工具确认。它应该看起来像这个样子： 
    
    # fdisk -l /dev/sda
    
    [...]
      Device Boot      Start         End      Blocks   Id  System
    /dev/sda1   *        2048      104447       51200   83  Linux
    /dev/sda2          104448   625142447   312519000   83  Linux
    
安装 MBR 启动代码： 
    
    # dd bs=440 count=1 conv=notrunc if=/usr/lib/syslinux/bios/mbr.bin of=/dev/sda
    
Syslinux 提供一个替代的分区表 `altmbr.bin`。这个分区表 _不会_ 扫描可启动分区，而是从 MBR 的最后一个字节中的值读取用于启动的分区。下面的操作会将这个分区表写入。 
    
    # printf '\x5' | cat /usr/lib/syslinux/bios/altmbr.bin - | dd bs=440 count=1 iflag=fullblock of=/dev/sda
    
在这个例子中，一个数值为5（十六进制的）的单个字节会被添加到 `altmbr.bin` 的内容后，并向 `sda` 的 MBR 分区表中写入440字节的内容。Syslinux 会被安装到磁盘的第一个逻辑分区(`/dev/sda5`)。 

#####  GPT 分区表

对于一个安装在 [GPT 分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "Partitioning")上的实例, 请确保您的启动分区 `/boot` 被设置上了 2 号属性"传统BIOS可启动"（legacy BIOS bootable）。[Parted](<../zh-cn/Parted.html> "Parted") 可以使用"legacy_boot"参数实现，而 [sgdisk](<../zh-cn/GPT_fdisk.html> "GPT fdisk") 则需要输入下面的命令： 
    
    # sgdisk /dev/sda --attributes=1:set:2
    
这会在 `/dev/sda` 的第一个分区设置"传统BIOS可启动"属性。检查命令： 
    
    # sgdisk /dev/sda --attributes=1:show
    
    1:2:1 (legacy BIOS bootable)

安装 MBR 启动代码： 
    
    # dd bs=440 count=1 conv=notrunc if=/usr/lib/syslinux/bios/gptmbr.bin of=/dev/sda
    
##  UEFI 系统

**注意：**

  * `efi64` 对应 x86_64 UEFI 系统。如果是 IA32（32位） EFI 您需要在下面的命令中将 `efi64` 替换为 `efi32`。
  * 因为 Syslinux（目前）没有办法访问它自己所在以外的分区，因此内核与 initramfs 文件需要位于 Syslinux 同在的 [EFI 系统分区](<../zh-cn/EFI_system_partition.html> "EFI system partition")（也叫ESP）。因此，这里推荐将ESP分区挂载在 `/boot`。
  * `/usr/bin/syslinux-install_update` 自动安装脚本不支持 UEFI 安装。
  * `syslinux.cfg` 文件的配置与 BIOS 的配置方法相同。

###  UEFI Syslinux 的局限性

  * UEFI Syslinux 程序 `syslinux.efi` 不能通过 `sbsign`([sbsigntools](<https://archlinux.org/packages/?name=sbsigntools>)包 软件包提供)签名，导致无法进行 UEFI 安全启动。查看关于此的 Bug 报告：[[5]](<https://bugzilla.syslinux.org/show_bug.cgi?id=8>)
  * 在 UEFI Syslinux 目录中编辑内核参数时使用 TAB 缩进会导致显示错误（重叠显示）。查看关于此的 Bug 报告：[[6]](<https://bugzilla.syslinux.org/show_bug.cgi?id=9>)
  * UEFI Syslinux 程序不支持链式加载其他如 `UEFI Shell`、`Windows Boot Manager` 等 EFI 应用程序。查看关于此的增强请求：[[7]](<https://bugzilla.syslinux.org/show_bug.cgi?id=17>)
  * 在某些情况下，UEFI Syslinux 可能不能在通过 [QEMU](<../zh-cn/QEMU.html> "QEMU")/OVMF、[VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox") 和 [VMware](<../zh-cn/VMware.html> "VMware") 的一些特定产品或版本构建的虚拟机的中启动。一些如 DUET 等 UEFI 模拟环境中也是如此。Syslinux 的贡献者已经确认，在 VMware Workstation 10.0.2 版本、Syslinux 6.02 版本以后不会发生这个问题。查看关于此的 Bug 报告：[[8]](<https://bugzilla.syslinux.org/show_bug.cgi?id=21>), [[9]](<https://bugzilla.syslinux.org/show_bug.cgi?id=23>) 和 [[10]](<https://bugzilla.syslinux.org/show_bug.cgi?id=72>)
  * Memdisk 不被 UEFI 支持。查看关于此的增强请求：[[11]](<https://bugzilla.syslinux.org/show_bug.cgi?id=30>)

###  在 UEFI 上安装

**注意：** 在与 UEFI 有关的命令中，` _esp_` 指的是 [EFI 系统分区](<../zh-cn/EFI_system_partition.html> "EFI system partition")(ESP)所挂载的位置。

  * 安装来自[官方软件源](<../zh-cn/Official_repositories.html> "Official repositories")的 [syslinux](<https://archlinux.org/packages/?name=syslinux>)包 和 [efibootmgr](<https://archlinux.org/packages/?name=efibootmgr>)包。然后按如下步骤安装 Syslinux 到 EFI 系统分区(ESP)：
  * 复制 Syslinux 文件到 EFI 系统分区:

    # mkdir -p _esp_ /EFI/syslinux
    # cp -r /usr/lib/syslinux/efi64/* _esp_ /EFI/syslinux
    
  * 使用 [efibootmgr](<../zh-cn/Unified_Extensible_Firmware_Interface.html#efibootmgr> "Unified Extensible Firmware Interface") 安装引导记录:

    # efibootmgr --create --disk /dev/sdX --part Y --loader /EFI/syslinux/syslinux.efi --label "Syslinux" --verbose
    
其中，`/dev/sdXY`是包含启动加载器的分区。 

  * 按照[#配置](<#%E9%85%8D%E7%BD%AE>)创建或编辑` _esp_ /EFI/syslinux/syslinux.cfg`文件。

**注意：**

  * UEFI 的配置文件是 `_esp_ /EFI/syslinux/syslinux.cfg` 而非 `/boot/syslinux/syslinux.cfg`。在 `/boot/syslinux/` 中的文件是 BIOS 启动专用的，和 UEFI Syslinux 无关。

在BIOS模式下启动时， [efibootmgr](<https://archlinux.org/packages/?name=efibootmgr>)包 将无法为 ` /EFI/syslinux/syslinux.efi` 设置 EFI 存储于非易失性存储器（nvram）的条目。欲实现此，请将资源放在默认 EFI 位置：` _esp_ /EFI/syslinux/* -> _esp_ /EFI/BOOT/*` 和 `_esp_ /EFI/syslinux/syslinux.efi -> _esp_ /EFI/BOOT/bootx64.efi` 处。 

##  配置

Syslinux 的配置文件 `syslinux.cfg` 必须和 Syslinux 放在同一个目录下。在我们的示例中，BIOS 系统放在 `/boot/syslinux/` 处，UEFI 系统放在 `_esp_ /EFI/syslinux/` 处。 

启动器将自动寻找 `syslinux.cfg` (优先)和 `extlinux.conf`这两个配置文件之一。 

**提示：**

  * 除了 `LINUX`，您也可以使用 `KERNEL` 关键字。`KERNEL` 关键字会试图去检测内核文件的类型，而 `LINUX` 总是会将其按照 Linux 内核处理。
  * `TIMEOUT` 的单位是 **0.1 秒** ，也就是说 50 代表 5 秒。

###  示例

**注意：**

  * 示例这一节中的所有配置文件都需要编辑并设定合适的内核参数。参见[#内核参数](<#%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0>)节。
  * 请一定仔细检查路径。这个实例可能不能够直接照搬到您的安装实例，尤其是 UEFI 系统。
  * 接下来的例子假设内核与 initrd 文件都位于 `syslinux.cfg` 的父目录。(准确的说，是工作目录的父目录)。

####  启动提示符

这是一个非常简单的配置文件，会显示 `boot:` 提示符并在 5 秒后自动启动。如果您不希望看见提示符，请将 `PROMPT` 设置为 `0`。 

配置文件： 
    
    * BIOS: /boot/syslinux/syslinux.cfg
    * UEFI: _esp_ /EFI/syslinux/syslinux.cfg
    
    PROMPT 1
    TIMEOUT 50
    DEFAULT arch
    
    LABEL arch
    	LINUX ../vmlinuz-linux
    	APPEND root=/dev/sda2 rw
    	INITRD ../initramfs-linux.img
    
    LABEL archfallback
    	LINUX ../vmlinuz-linux
    	APPEND root=/dev/sda2 rw
    	INITRD ../initramfs-linux-fallback.img
    
####  文本启动目录

Syslinux 允许您使用一个文本启动目录来选择。要做到这一点，请将 `menu` 和 `libutil` 模块复制到您的 Syslinux 目录： 
    
    # cp /usr/lib/syslinux/bios/{menu,libutil}.c32 /boot/syslinux/
    
在 5.00 版本之后，其他的 `lib*.c32` 库模块也会频繁地被调用。参考 [Syslinux 维基](<https://wiki.syslinux.org/wiki/index.php?title=Library_modules#Syslinux_modules_working_dependencies>)来查看依赖树。 

配置文件： 
    
    * BIOS: /boot/syslinux/syslinux.cfg
    * UEFI: _esp_ /EFI/syslinux/syslinux.cfg
    
    UI menu.c32
    PROMPT 0
    
    MENU TITLE Boot Menu
    TIMEOUT 50
    DEFAULT arch
    
    LABEL arch
    	MENU LABEL Arch Linux
    	LINUX ../vmlinuz-linux
    	APPEND root=/dev/sda2 rw
    	INITRD ../initramfs-linux.img
    
    LABEL archfallback
    	MENU LABEL Arch Linux Fallback
    	LINUX ../vmlinuz-linux
    	APPEND root=/dev/sda2 rw
    	INITRD ../initramfs-linux-fallback.img
    
更多关于启动目录的信息，请参考 [Syslinux 维基](<https://wiki.syslinux.org/wiki/index.php/Menu>)。 

####  图形化启动目录

Syslinux 允许您使用一个文本启动目录来选择。要做到这一点，请将 `vesamenu` COM32 模块复制到您的 Syslinux 目录： 
    
    # cp /usr/lib/syslinux/bios/vesamenu.c32 /boot/syslinux/
    
在 5.00 版本之后，其他的 `lib*.c32` 库模块也会频繁地被调用。参考 [Syslinux 维基](<https://wiki.syslinux.org/wiki/index.php?title=Library_modules#Syslinux_modules_working_dependencies>)来查看依赖树。 

**注意：** 如果您使用的是 [UEFI](<../zh-cn/UEFI.html> "UEFI") 系统，请一定从 `/usr/lib/syslinux/efi64/` 目录(或者 IA32 (32位) EFI 的 `efi32`) 中复制。否则电脑会黑屏。如果出现这个情况，请从 Live CD 中启动并使用 [chroot](<../zh-cn/Chroot.html> "Chroot") 来进行正确的修改。

这个配置文件使用了和 Arch Linux 安装光盘相同的目录设计，您可以在 [gitlab.archlinux.org](<https://gitlab.archlinux.org/archlinux/archiso/-/tree/master/configs/releng/syslinux>) 上找到。[Arch Linux 启动背景图像](<https://gitlab.archlinux.org/archlinux/archiso/-/raw/master/configs/releng/syslinux/splash.png?inline=false>)也可以在那儿下载。请把图像复制到 `/boot/syslinux/splash.png` 处。 

配置文件： 
    
    * BIOS: /boot/syslinux/syslinux.cfg
    * UEFI: _esp_ /EFI/syslinux/syslinux.cfg
    
    UI vesamenu.c32
    DEFAULT arch
    PROMPT 0
    MENU TITLE Boot Menu
    MENU BACKGROUND splash.png
    TIMEOUT 50
    
    MENU WIDTH 78
    MENU MARGIN 4
    MENU ROWS 5
    MENU VSHIFT 10
    MENU TIMEOUTROW 13
    MENU TABMSGROW 11
    MENU CMDLINEROW 11
    MENU HELPMSGROW 16
    MENU HELPMSGENDROW 29
    
    # Refer to https://wiki.syslinux.org/wiki/index.php/Comboot/menu.c32
    
    MENU COLOR border       30;44   #40ffffff #a0000000 std
    MENU COLOR title        1;36;44 #9033ccff #a0000000 std
    MENU COLOR sel          7;37;40 #e0ffffff #20ffffff all
    MENU COLOR unsel        37;44   #50ffffff #a0000000 std
    MENU COLOR help         37;40   #c0ffffff #a0000000 std
    MENU COLOR timeout_msg  37;40   #80ffffff #00000000 std
    MENU COLOR timeout      1;37;40 #c0ffffff #00000000 std
    MENU COLOR msg07        37;40   #90ffffff #a0000000 std
    MENU COLOR tabmsg       31;40   #30ffffff #00000000 std
    
    LABEL arch
    	MENU LABEL Arch Linux
    	LINUX ../vmlinuz-linux
    	APPEND root=/dev/sda2 rw
    	INITRD ../initramfs-linux.img
    
    LABEL archfallback
    	MENU LABEL Arch Linux Fallback
    	LINUX ../vmlinuz-linux
    	APPEND root=/dev/sda2 rw
    	INITRD ../initramfs-linux-fallback.img
    
从 Syslinux 3.84 版本开始，`vesamenu.c32` 支持 `MENU RESOLUTION $WIDTH $HEIGHT` 指令。 使用这个指令，请将 `MENU RESOLUTION 1440 900` 插入您的配置文件，这样可以将分辨率设置为 1440x900。 但是，背景图像需要和分辨率完全一致，否则 Syslinux 将拒绝加载目录。 

如果想要将目录居中并调整分辨率，请调节 `MENU RESOLUTION`、`MENU HSHIFT $N` 和 `MENU VSHIFT $N` 三个参数。将 `$N` 设置为非负值会将其从左上角开始移动。默认值都是 `0`，因此目录会显示在显示器的左上角。反过来，如果这个数值为负，则会从反方向开始移动。(比如说 `VHSHIFT -4`是从底部向上移动四行)。 

如果想要使目录居中，请添加或改为这些值： 
    
    * BIOS: /boot/syslinux/syslinux.cfg
    * UEFI: _esp_ /EFI/syslinux/syslinux.cfg
    
    MENU RESOLUTION 800 600 # or whatever your screen resolution is
    MENU WIDTH 78           # width of the menu also required to bring the menu box to size
    MENU VSHIFT 10          # moves menu down
    MENU HSHIFT 10          # moves menu right
    
VESA 标准通常最大允许 25 行 80 列，因此如果将其设置得过大可能会将目录移出屏幕外，可能需要使用救援介质才能改回来。 

###  内核参数

在 `syslinux.cfg` 中，[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")的设定使用 `APPEND` 指令： 对每一个 `LABEL` 记录， [APPEND](<https://wiki.syslinux.org/wiki/index.php/Config#APPEND>) 命令只能出现在一行内(就是说，把命令拆分成多行是无效的)。 

推荐将下列的设置同时作为回滚条目。 

**最简单的情形** ，`root` 参数中的分区名称需要被修改。 将 `/dev/sda2` 改为正确的启动分区。 
    
    APPEND root=/dev/sda2
    
**如果您想使用[UUID](<../zh-cn/Persistent_block_device_naming.html#by-uuid> "Persistent block device naming")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]**，通过[块设备持久化命名](<../zh-cn/Persistent_block_device_naming.html> "Persistent block device naming")制定启动分区，请如下改变 `APPEND` 行。这里我们用`1234`来代表您需要修改的`UUID`： 
    
    APPEND root=UUID=_1234_ rw
    
**如果您想使用[dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt") 加密设备**请如下改变 `APPEND` 行。 
    
    APPEND root=/dev/mapper/_name_ cryptdevice=/dev/sda2:_name_ rw
    
**如果您使用[mdadm](<https://neil.brown.name/blog/mdadm>) 构建的软 RAID** , 请如下改变 `APPEND` 行来适配您的 RAID 阵列。下面是一个适配 3 RAID-1 阵列、并将一个合适的分区设为根分区的示例。 
    
    APPEND root=/dev/md1 rw md=0,/dev/sda2,/dev/sdb2 md=1,/dev/sda3,/dev/sdb3 md=2,/dev/sda4,/dev/sdb4
    
如果在内核设备节点模式下通过软 RAID 启动失败，下面是一个替代的更可靠的方法：使用分区标签： 
    
    APPEND root=LABEL=_THEROOTPARTITIONLABEL_ rw
    
**如果从一个[btrfs](<../zh-cn/Btrfs.html> "Btrfs") 子卷启动**，向 `APPEND` 添加 `rootflags=subvol=<root subvolume>` 这一行。举个例子，我们称 `/dev/sda2` 被挂载到一个叫 'ROOT' 的 btrfs 子卷。(例如 `mount -o noatime,subvol=ROOT /dev/sda2 /mnt`)，这时应该将 `APPEND` 行改为这样： 
    
    APPEND root=/dev/sda2 rw rootflags=subvol=ROOT
    
如果此处错误，会收到 `ERROR: Root device mounted successfully, but /sbin/init does not exist.`错误信息。 

###  自动启动

If you do not want to see the Syslinux menu at all, use the 如果您根本不想看见 Syslinux 的目录，请参考[#启动提示符](<#%E5%90%AF%E5%8A%A8%E6%8F%90%E7%A4%BA%E7%AC%A6>)一节，将 `PROMPT` 设置为 `0` 并将任何 `UI` 的目录记录注释掉。将 `TIMEOUT` 设置为 `0` 也可以。确保您在 `syslinux.cfg` 设置的有默认回滚 `DEFAULT` 选项。按下 `Shift` 或者 `Alt`，或者设置为按下 `Caps Lock` 或 `Scroll Lock`， 在启动时可以允许更多除了默认选项以外的操作。更多可以设置的替代键，请参考[上游的维基](<https://wiki.syslinux.org/wiki/index.php/Directives/special_keys>)。 

###  安全措施

Syslinux 有两级启动加载器安全措施，可以在 `syslinux.cfg` 中配置目录主密码，和分别针对每个条目的密码。使用 
    
    MENU MASTER PASSWD passwd 
    
来配置目录主密码，在 `LABEL` 的块中使用 
    
    MENU PASSWD passwd 
    
来设定针对这个条目的密码。 

密码可以是明文，也可以是哈希值。更多信息，请参考[官方文档](<https://wiki.syslinux.org/wiki/index.php/Comboot/menu.c32>)。 

###  链式加载

在 BIOS 上配置的 Syslinux 不能直接链式加载其他分区上的文件，但是 `chain.c32` 模块可以启动其他启动分区上的卷启动记录程序(VBR)，或是另一个磁盘上的 MBR 启动代码。 

####  链式加载卷启动记录程序

如果您想要链式加载另一个操作系统（比如 Windows）或启动加载器，请将 `chain.c32` 模块复制到 Syslinux 目录(还需要复制其他需要的 `lib*.c32` 库模块。更多信息请参考前面几节)，然后在配置文件中建立下面这一节： 
    
    /boot/syslinux/syslinux.cfg
    
    ...
    LABEL windows
    	MENU LABEL Windows
    	COM32 chain.c32
    	APPEND hd0 3
    ...
    
`hd0 3` 是第一个 BIOS 控制驱动器上的第三个分区。请注意，驱动器计数从 0 开始，而分区计数则是从 1 开始。 

**注意：** 对于引导 Windows，这样会跳过 Windows 自己的启动管理器环节 (`bootmgr`)，而一些系统更新（[例子](<https://support.microsoft.com/kb/2883200>)）会需要这个组件才能完成。如果更新需要，在这种情况下建议临时将 MBR 的启动分区标记设在 Windows 所在分区(可以使用 [GParted](<../zh-cn/Parted.html> "GParted"))并完成更新安装，再将启动分区标记改回 Syslinux 所在的分区。(可以使用 Windows自带的 [DiskPart](<https://www.online-tech-tips.com/computer-tips/set-active-partition-vista-xp>))。

####  链式加载 MBR 启动代码

如果您不知道 BIOS 会怎么安排驱动器的编号，您也可以使用 MBR 标记，或者说 GPT 的文件系统标签。使用 MBR 标记请如下文所示设置： 
    
    # fdisk -l /dev/sdb
    
    Disk /dev/sdb: 128.0 GB, 128035676160 bytes 
    255 heads, 63 sectors/track, 15566 cylinders, total 250069680 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0xf00f1fd3
     
    Device Boot      Start         End      Blocks   Id  System
    /dev/sdb1            2048     4196351     2097152    7  HPFS/NTFS/exFAT
    /dev/sdb2         4196352   250066943   122935296    7  HPFS/NTFS/exFAT
    
将 `/dev/sdb` 改成您想要链式加载的驱动器。这里需要使用您磁盘的十六进制标识符，这个例子中是 `0xf00f1fd3`。`syslinux.cfg` 需要改成这个样子： 
    
    /boot/syslinux/syslinux.cfg
    
    ...
    LABEL windows
    	MENU LABEL Windows
    	COM32 chain.c32
    	APPEND mbr:0xf00f1fd3
    ...
    
更多关于链式启动的信息，请参阅 [Syslinux 维基](<https://wiki.syslinux.org/wiki/index.php/Comboot/chain.c32>)。 

####  链式加载另一个启动加载器

如果您在同一个分区安装了 [GRUB](<../zh-cn/GRUB.html> "GRUB") 引导程序，您可以像这样来链式加载它： 
    
    /boot/syslinux/syslinux.cfg
    
    ...
    LABEL grub2
    	MENU LABEL Grub2
    	COM32 chain.c32
    	APPEND file=../grub/boot.img
    ...
    
作为替代，也可以将 [GRUB](<../zh-cn/GRUB.html> "GRUB") 作为一个 linux 内核来引导。只需要用 `lnxboot.img` 来替代 `core.img`。`lnxboot.img` 文件是 `core/grub` 提供的，您可以在 `/usr/lib/grub/i386-pc` 处找到它。 
    
    /boot/syslinux/syslinux.cfg
    
    ...
    LABEL grub2lnx
    	MENU LABEL Grub2 (lnxboot)
    	LINUX ../grub/i386-pc/lnxboot.img
    	INITRD ../grub/i386-pc/core.img
    ...
    
对于需要从 ISO 镜像引导的系统，这可能会被用到。 

###  使用内存测试 memtest

安装来自[官方软件源](<../zh-cn/Official_repositories.html> "Official repositories")的 [memtest86+](<https://archlinux.org/packages/?name=memtest86%2B>)包。 

用这个 `LABEL` 片段来启动[内存测试](<https://en.wikipedia.org/wiki/Memtest86> "wikipedia:Memtest86")： 
    
    /boot/syslinux/syslinux.cfg
    
    ...
    LABEL memtest
    	MENU LABEL Memtest86+
    	LINUX ../memtest86+/memtest.bin
    ...
    
**注意：** 如果您使用 PXELINUX，请将 `memtest.bin` 重命名为 `memtest`。因为 PXELINUX 会把有 _.bin_ 后缀名的文件当作启动扇区，这样就只会读取文件的前 2KB。

###  硬件检测工具

[硬件检测工具(HDT)](<https://wiki.syslinux.org/wiki/index.php/Hdt_\(Hardware_Detection_Tool\)>) 可以显示硬件信息。和前文所述的一样，`.c32` 模块需要从 `/boot/syslinux/` 中复制，其他需要的 `lib*.c32` 库模块也需要一并复制。 如果想要显示 PCI 总线信息请将 `/usr/share/hwdata/pci.ids` 复制到 `/boot/syslinux/pci.ids`，并在您的配置文件中添加这些行： 
    
    /boot/syslinux/syslinux.cfg
    
    LABEL hdt
    	MENU LABEL Hardware Info
    	COM32 hdt.c32
    
###  重启和关机

**注意：** 对于 Syslinux 6.03 版本，`poweroff.c32` 只能在[高级电源管理（APM）](<https://en.wikipedia.org/wiki/Advanced_Power_Management> "wikipedia:Advanced Power Management")下使用，而不适配[高级配置与电源接口（ACPI）](<https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface> "wikipedia:Advanced Configuration and Power Interface")。您可以参考[acpioff: 一种关闭使用 ACPI 控制机器的 COM32 模块](<https://www.syslinux.org/archives/2012-March/017661.html>)，这是一种可能的解决办法。

使用下面的片段来重启或关机： 
    
    /boot/syslinux/syslinux.cfg
    
    LABEL reboot
    	MENU LABEL Reboot
    	COM32 reboot.c32
    
    LABEL poweroff
    	MENU LABEL Power Off
    	COM32 poweroff.c32
    
###  清空屏幕

当退出时清空屏幕，在配置文件中加入下面这一行： 
    
    /boot/syslinux/syslinux.cfg
    
    MENU CLEAR
    
###  键盘布局

如果您需要经常修改 Syslinux 启动提示符下的参数，您可能想要匹配您的键盘布局。这样您就可以在一个非美式英语键盘上方便地输入"="、"/"等字符了。 

**注意：**[syslinux](<https://archlinux.org/packages/?name=syslinux>)包 软件包下的 `keytab-lilo` 是一个调用 _键位加载_ 的 perl 脚本。

生成一个适配的键盘布局映射表，（比如说，德语键盘），运行： 
    
    # keytab-lilo /usr/share/kbd/keymaps/i386/qwerty/us.map.gz /usr/share/kbd/keymaps/i386/qwertz/de.map.gz > /boot/syslinux/de.ktl
    
现在在 `syslinux.cfg` 文件中加入 
    
    /boot/syslinux/syslinux.cfg
    
    KBDMAP de.ktl
    
更多细节，请参考 [Syslinux 维基](<https://wiki.syslinux.org/wiki/index.php/Directives/kbdmap>)。 

###  隐藏目录

在配置文件中使用 
    
    /boot/syslinux/syslinux.cfg
    
    MENU HIDDEN
    
参数来隐藏目录并只显示超时倒计时。按下任意按键来显示目录。 

### PXELINUX

**注意：** 对于 UEFI 设备，Syslinux 使用相同的二进制文件来从磁盘和网络启动。从 TFTP 或其他网络协议中启动要求 Syslinux 的网络启动。

PXELINUX 和 [syslinux](<https://archlinux.org/packages/?name=syslinux>)包 软件包一起提供。 

对于一个 BIOS 客户机，将 `{l,}pxelinux.0` 启动加载器复制到客户机的启动目录。对于 5.00 版本及以上的 Syslinux，还需要将同一个软件包中的 `ldlinux.c32` 复制过去。 
    
    # cp /usr/lib/syslinux/bios/pxelinux.0 "_TFTP_root_ /boot/"
    # cp /usr/lib/syslinux/bios/ldlinux.c32 "_TFTP_root_ /boot/"
    # mkdir "_TFTP_root_ /boot/pxelinux.cfg"
    
这时，我们同时也创建了 `pxelinux.cfg` 目录。PXELINUX 会默认在这个目录中寻找配置文件。我们不想对每一个不同的主机 MAC 地址都作出单独的设置，我们需要创建 `default` 作为默认配置。 
    
    _TFTP_root_ /boot/pxelinux.cfg/default
    
    DEFAULT linux
    
    LABEL linux
    	KERNEL vmlinuz-linux
    	APPEND initrd=initramfs-linux.img quiet ip=:::::eth0:dhcp nfsroot=10.0.0.1:/arch
    
如果您使用 NBD 网络存储启动，添加下面这行： 
    
    append ro initrd=initramfs-linux.img ip=:::::eth0:dhcp nbd_host=10.0.0.1 nbd_port=10809 nbd_name=arch root=/dev/nbd0

**注意：** 您需要对应修改 `nbd_host` 和/或 `nfsroot` 来与您的网络配置（NFS/NBD 服务器的地址）相匹配。

PXELINUX 的配置和 SYSLINUX 使用相同的语法。参考上游的文档来获取更多信息。 

内核与 initramfs 会通过 TFTP 传输，因此需要设置对 TFTP 根目录的相对路径。否则，根文件系统需要挂载在 NFS 挂载点上。 

若要加载 PXELINUX, 请将 `/etc/dhcpd.conf` 文件中的 `filename "/grub/i386-pc/core.0";` 替换为 `filename "/pxelinux.0"` (或 `filename "/lpxelinux.0"`)。 

###  通过 memdisk 启动 ISO9660 镜像

Syslinux 支持通过 [memdisk](<https://wiki.syslinux.org/wiki/index.php/MEMDISK>) 模块从 ISO 镜像中启动。参考[Multiboot USB drive#Using Syslinux and memdisk](<../zh-cn/Multiboot_USB_drive.html#Using_Syslinux_and_memdisk> "Multiboot USB drive")中的示例。 

###  串行控制台

参考 [Working with the serial console#Syslinux](</wzh/index.php?title=Working_with_the_serial_console&action=edit&redlink=1> "Working with the serial console（页面不存在）")。 

###  单次引导到另一个操作系统

可以临时改变 Syslinux 的行为，让其仅在下一次启动时引导进入另一个操作系统。下面的命令展示了怎样临时引导 `archfallback`。 
    
    # extlinux -o archfallback /boot/syslinux
    
在下一次启动的过程中，上面制定的启动标签会在没有任何 Syslinux 启动提示符的情况下直接启动。默认的启动行为会在下一次重启的时候复原。 

##  常见问题

###  无法加载 ldlinux

启动时出现 "Failed to load ldlinux.c32" 错误提示可能会有很多原因。 其中的一种可能是文件系统工具或者文件系统结构遭到了更改。 

**警告：** 在 Syslinux 6.03 版本中，启动加载器可能不支持某些文件系统的部分功能。详情请参考 [[12]](<https://wiki.syslinux.org/wiki/index.php/Filesystem>)。

**注意：** 出现 `Failed to load ldlinux.c32` 并不一定与文件系统出现问题直接相关： 

  * 文件系统可能出现的其他症状，除了这条信息，还可能指出另一些与文件系统有关的问题。
  * 这条信息并不说明问题处在了文件系统。还有其他的一些问题会导致这条信息出现。

您也可以参考 [[13]](<https://wiki.syslinux.org/wiki/index.php/Common_Problems#Failed_to_load_ldlinux>)。 (这一整页都和常见问题有关)。 

###  使用 Syslinux 启动提示符

您可以输入(在您的 `syslinux.cfg` 配置过的) `LABEL` 的名称来启动对应的系统。如果您是按照上述的例子进行的配置，您只需要输入： 
    
    boot: arch
    
如果您收到了配置文件无法加载的错误信息，您可以向启动提示符中直接输入您的启动参数。比如说： 
    
    boot: ../vmlinuz-linux root=/dev/sda2 rw initrd=../initramfs-linux.img
    
如果在[ramfs](</wzh/index.php?title=Ramdisk&action=edit&redlink=1> "Ramdisk（页面不存在）")中您没有 `boot:` 的访问权限，并且您暂时无法启动内核， 

    1\. 创建一个临时的目录，来加载您的根分区 (如果不存在的话)：
    
     # mkdir -p /new_root
    
    2\. 将 `/` 挂载到 `/new_root` (我们假设 `/boot/` 也在同一个分区，否则您需要将这些分区全部挂载):

**注意：** 如果 `/boot` 在自己的 ext2 分区，Busybox 将无法挂载。
    
     # mount /dev/sd[a-z][1-9] /new_root
    
    3\. 使用 `vim` 来重新将 `syslinux.cfg` 编辑正确。保存文件。
    4\. 重启。

###  根分区文件系统检测失败

如果根分区被严重损坏（分区日志受损），在ramfs的应急 shell 中，加载根分区文件系统： 
    
    # mount /dev/_root partition_ /new_root
    
将二进制程序 tune2fs 从根分区中复制出来（这个不包含在 Syslinux 中）。 
    
    # cp /new_root/sbin/tune2fs /sbin/
    
按照下面的指示[ext2fs: 日志损坏](<../zh-cn/Fsck.html#ext2fs:_no_external_journal> "Fsck")重建根分区日志。 

###  没有找到默认回滚和界面设置

有些主板厂家对 USB 设备启动的支持会差一些。此时一个在通常的现代电脑上都能启动的 ext4 格式的 U 盘，一些要求内核与 initrd 文件必须存储在 FAT16 分区的电脑可能无法正常运作。为了避免这种老设备无法读取 `syslinux.cfg` 而去加载 `ldlinux`，用 [dosfstools](<https://archlinux.org/packages/?name=dosfstools>)包 工具建立一个 [FAT16](</wzh/index.php?title=FAT16&action=edit&redlink=1> "FAT16（页面不存在）") 的小分区(≤ 2 GB)： 
    
    # mkfs.fat -F 16 /dev/sda1
    
再来安装配置 Syslinux。 

###  找不到操作系统

  * 确保您在[#MBR 分区表](<#MBR_%E5%88%86%E5%8C%BA%E8%A1%A8>)上安装的是 `mbr.bin`，在[#GPT 分区表](<#GPT_%E5%88%86%E5%8C%BA%E8%A1%A8>)上安装的是 `gptmbr.bin`。如果安装错误，`mbr.bin` 会显示 "Missing operating system" 错误信息，而 `gptmbr.bin` 会显示 "Missing OS" 信息。
  * 检查包含 `/boot` 的分区是否有可启动标记。
  * 检查第一个分区是否是从 1 扇区，而不是 63 扇区或 2048 扇区开始的。您可以使用 `fdisk -l` 命令确认。如果是从 1 扇区开始的，您可以通过救援介质上的 `gparted` 修改。如果您有另一个启动分区，您可以将 `/boot` 备份：

    # cp -a /boot /boot.bak
    
然后使用 Arch 安装磁盘启动。接下来，使用 `cfdisk` 删掉 `/boot` 分区，再重建它。现在这个分区应该从正确的 **63** 扇区开始。现在挂载您的分区，并按照[安装指南](<../zh-cn/Installation_guide.html> "Installation guide")中写的那样 `chroot` 进入待修复系统。使用以下指令恢复 `/boot`。 
    
    # cp -a /boot.bak/ /boot/
    
检查 `/etc/fstab` 是否正确： 
    
    # syslinux-install_update -iam
    
然后重启。 

如果您试图从用一个太新以至于 Syslinux 无法识别其元数据的工具创建的 md [RAID](<../zh-cn/RAID.html> "RAID")-1 阵列启动，您也会得到这个错误信息。在 2013 年 8 月 mdadm 会创建使用 1.2 版本的元数据的阵列，但是 Syslinux 不能够识别高于 1.0 版本的元数据。如果是因此而出错，您需要重建您的序列，并在使用 mdadm 时添加 `--metadata=1.0` 参数。 

###  启动了 Windows，Syslinux 被忽略掉了

**解决办法：** 确保包含 `/boot` 的分区上有可启动标记。同时，确保 Windows 分区上没有这个标记。请参考上面的[#链式加载卷启动记录程序](<#%E9%93%BE%E5%BC%8F%E5%8A%A0%E8%BD%BD%E5%8D%B7%E5%90%AF%E5%8A%A8%E8%AE%B0%E5%BD%95%E7%A8%8B%E5%BA%8F>)部分。 

Syslinux 所在的 MBR 会找到第一个有可启动标记的活动分区。Windows 分区很可能最先被发现。如果您想要修改，您可以使用 Windows 或 MS-DOS 上的 `fdisk`。 

###  目录项失效

您选择了一个目录项，但是什么都没有发生，只是 _"刷新"_ 了一下目录。这通常意味着您的 `syslinux.cfg` 文件出了问题。按下 `Tab` 键来修改您的启动参数。或者您也可以按下 `Esc` 键，并输入您的启动项的 `LABEL`。（比如说， _arch_ ）。另一种可能导致这个情况的原因可能是您没有安装内核。想个办法进入您的文件系统（比如说，用live CD），检查 `/mount/vmlinuz-linux` 文件存在并且非空。如果是这里出错，请重新安装您的内核。 

###  无法删除 ldlinux.sys

`ldlinux.sys` 文件设置了[不可变属性](<../zh-cn/File_permissions_and_attributes.html#File_attributes> "File permissions and attributes")，禁止您删除或覆盖它。这样保证了除了重装 Syslinux，没有别的办法来修改这个文件。若要删除这个文件，请运行下面的指令： 
    
    # chattr -i /boot/syslinux/ldlinux.sys
    # rm /boot/syslinux/ldlinux.sys
    
###  vesamenu的左上角有白色块

问题： _从 linux-3.0 开始，模式设置驱动程序会在更改分辨率后尝试保留屏幕的当前内容（至少在我的 Intel 设备上，使用 Syslinux 的文本模式的情况下如此）。而 Syslinux 中的 vesamenu 模块会与这个特性冲突。（白色方框实际上是驱动程序试图保留 Syslinux 目录，但是驱动程序无法从 vesa 图形模式下捕获图片）。_

如果您的分辨率是自定义的，而 `vesamenu` 在很早就进行了模式设置，请尝试在 `syslinux.cfg` 添加这一行来消除白色块： 
    
    APPEND root=/dev/sda6 rw 5 **vga=current** quiet splash
    
###  当 Windows 安装在另一张磁盘上时，链式启动失效

如果 Windows 安装在在另一张磁盘上，您又不能通过链式启动来引导 Windows， 请尝试下列配置： 
    
    LABEL Windows
    	MENU LABEL Windows
    	COM32 chain.c32
    	APPEND mbr:0xdfc1ba9e swap
    
将 MBR 代码换成您的 Windows 驱动器的值(详见[上文](<#%E9%93%BE%E5%BC%8F%E5%8A%A0%E8%BD%BD>))，并将 `swap` 加入选项。 

###  查看启动加载器日志

在一些情况下（比如启动加载器无法启动内核），我们很想得到启动的更多信息。Syslinux 会显示错误信息，但是文字一闪而过，看不清。为了保留日志信息，请禁用 `syslinux.cfg` 中的 `UI menu`，并使用默认的命令提示符。这意味着 

  * 不使用 `UI` 命令
  * 不使用 `ONTIMEOUT`
  * 不使用 `ONERROR`
  * 不使用 `MENU CLEAR`
  * 将 `TIMEOUT` 设为更高的值
  * 使用 `PROMPT 1`
  * 使用 `DEFAULT _problematic_label_`

若要得到更详细的调试日志，To get more detailed debug log, 添加下面的 C 编译标志并[重新编译](<../zh-cn/Arch_Build_System.html> "Arch Build System") [syslinux](<https://archlinux.org/packages/?name=syslinux>)包 软件包： 
    
    -DDEBUG_STDIO=1 -DCORE_DEBUG=1
    
###  Btrfs 压缩

从压缩 Btrfs 文件系统启动不受支持。[[14]](<https://wiki.syslinux.org/wiki/index.php/Syslinux_4_Changelog#Changes_in_4.02>) 会显示下列错误信息： 
    
    btrfs: found compressed data, cannot continue!
    invalid or corrupt kernel image.
    
###  多设备 Btrfs

从多设备 Btrfs 文件系统启动不受支持。[[15]](<https://repo.or.cz/syslinux.git/blob/HEAD:/extlinux/main.c>) (21-Jul-2016 版本，main.c 文件第 1246 行validate_device_btrfs()会对此进行检查) 这个令人抓狂的问题会显示下列错误信息：(假设您将 Syslinux 装在 sda1): 
    
    /boot/syslinux is device /dev/sda1
    extlinux: path /boot/syslinux doesn't match device /dev/sda1
    
##  更多信息

  * [官方网站](<https://www.syslinux.org>)
