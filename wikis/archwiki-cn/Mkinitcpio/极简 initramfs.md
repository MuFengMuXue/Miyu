**翻译状态：**

  * 本文（或部分内容）译自 [mkinitcpio/Minimal initramfs](<https://wiki.archlinux.org/title/mkinitcpio/Minimal_initramfs> "arch:mkinitcpio/Minimal initramfs")，最近一次同步于 2024-7-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/mkinitcpio/Minimal_initramfs?diff=0&oldid=812636>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/mkinitcpio_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Minimal_initramfs_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文介绍如何为具有特定、已知和静态硬件配置的系统创建精简、最小的 initramfs。 Falconindy (Dave Reisner) 的 [Optimizing Bootup With mkinitcpio](<http://blog.falconindy.com/articles/optmizing-bootup-with-mkinitcpio.html>) 详细阐述了该过程。 

##  Udev 要求

创建自己的 initramfs 映像的一大优点是可以移除 `udev` 钩子。这个钩子在 initramfs 中占了相当大一块空间（使用 LZ4 和 LZOP 压缩时约为 700-800 KiB，其他算法较小）。因此它不仅导致启动时加载耗时更长（需要解压更多的数据），而且初始化其自身时也要额外的时间。**但是，仍有部分操作需要** `udev`，包括解析 UUID、LABEL、PARTUUID 和 PARTLABEL 标识符（[workaround hook without-udev](<https://unix.stackexchange.com/questions/352381/how-to-boot-into-root-btrfs-file-system-with-minimal-initramfs-without-udev-hook/352932#answer-352932>)）以及包含 `root` 分区的 LVM 和 mdadm 设备。 若您不确定是否需要 `udev`，请继续按照本页上的说明操作，直到 [#初步测试](<#%E5%88%9D%E6%AD%A5%E6%B5%8B%E8%AF%95>)章节。如果在没有 `udev` 的时候出了问题，请重新启用此钩子，再试一次。 

另请注意，虽然大部分键盘（AT，PS/2，USB）不需要 `udev` 钩子也能正常工作，但使用罗技统一接收器（Logitech Unified Receiver）的 USB 设备需要。此时，您可以在所有映像中包含 `udev` 或依赖 `fallback` 映像正常工作。 

如果您确实需要 `udev`，最小化映像的努力可能就白费了。映像大小也许能减小约 600 KiB，但是启动时间不会有显著改变。在此情况继续下去，不失为一次学习机会。 

##  编辑 .preset 文件

在 Falconidy 的教程中，他编辑 `/etc/mkinitcpio.conf` 并运行 `mkinitcpio -g` 来创建测试 initramfs 映像，使系统上已知正常启动的 initramfs 映像保持不变。 但是，如果您事后盲目运行 `mkinitcpio -P`，甚至 `fallback` 映像也会被删除。 

准备自行创建 initramfs 的更安全方法是修改 `/etc/mkinitcpio.d` 中的 `.preset` 文件。以下的示例设定将以最小的 initramfs 映像取代`default`，并依照 The Arch Way 的方式建立一个新的正常映像文件。 如果出现问题，您仍可以使用 `normal` 或 `fallback` 映像。 完成后，您可以从配置中删除 `normal_*` 行并删除 `initramfs-linux*-normal.img` 文件。 
    
    ...
    
    PRESETS=('default' 'normal' 'fallback')
    ...
    
    default_options="-S udev,block,mdadm_udev,filesystems,keyboard,fsck,consolefont"
    ...
    
    #normal_config="/etc/mkinitcpio.conf"
    normal_image="/boot/initramfs-linux-normal.img"
    #normal_options=""
    ...

`mdadm_udev` 和 `consolefont`钩子不在 Arch Linux 默认的配置中，在 `*_options` 行的 `-S` 参数中包含无关的钩子不会导致错误。 

##  找出需要的模块

[![](../../File:Tango-preferences-desktop-locale.png)](<../../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 需要翻译（在 [Talk:Mkinitcpio/极简 initramfs#](<../../zh-cn/Talk:Mkinitcpio/%E6%9E%81%E7%AE%80_initramfs.html>) 中讨论）

找出机器需要的模块的最快方法是重启电脑，使用 `fallback` 映像并通过引导加载程序（boot loader）添加 `break=postmount` 内核参数。于是在根文件系统挂载好后便可进入命令行界面。 

重启电脑后，通过以下命令来获取需要的模块： 
    
    lsmod | awk 'NF==3{print $1}'
    
**注意：**`awk` 命令会返回每一行的第一个字段（使用 `{print $1`），但只限于那些刚好有三个字段的行，这是通过 `NF==3` 来强制筛选的。 模块依赖关系会包含第四个字段，用来显示是由哪个模块引入这个依赖，因此这些行会因为有第四个字段而被过滤掉。Arch 的 `mkinitcpio` 会处理那些正当包含在 `MODULES=()`、`FILES=()` 和 `BINARIES=()` 数组中的依赖项目。

保存已加载模块的清单，输入 `exit` 继续启动机器。 

另一种方式是[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [hwdetect](<https://archlinux.org/packages/?name=hwdetect>)包 来帮助确定所需的模块。虽然此软件包已停止维护，它仍可提供有价值的信息。另外，请参阅[内核模块](<../../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")以开始使用本机工具。 

##  初步编辑 mkinitcpio.conf

编辑 `/etc/mkinitcpio.conf` 修改 `MODULES=` 数组。值得注意 `/etc/mkinitcpio.conf` [作为脚本调用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Source> "Source")，可以使用 bash 脚本构建 MODULES 数组。 
    
    MODULES=()   # filesystems
    MODULES+=()  # storage
    MODULES+=()  # keyboard
    MODULES+=()  # miscellaneous
    
把模块添加到配置中最后的 `miscellaneous` 行中，整理时再将模块移至合适的行去。 

若需要对 `root` 分区设备和在 `/etc/fstab` 的**任何其他挂载点** 进行文件系统检查操作，请按下文配置： 

  * 对于 ext[2|3|4] 设备：

    BINARIES=(fsck fsck.ext[2|3|4] e2fsck)
    
  * 对于 vfat (UEFI boot) 设备：

    BINARIES=(fsck fsck.vfat dosfsck)
    
  * 对于 btrfs 单盘设备：

    BINARIES=(fsck fsck.btrfs btrfsck)
    
  * 对于 btrfs 多盘设备：

    BINARIES=(fsck fsck.btrfs btrfs btrfsck)
    
  * 对于 xfs 设备：

    BINARIES=(fsck fsck.xfs xfs_repair)
    
**注意：**

  * 上述示例中的第三个选项都是可选的，但除去它们将导致无法修复损坏的文件系统，此时需要从另一个 initramfs 启动。
  * 鼓励添加其他文件系统的条目。

##  初步测试

编辑 `/etc/mkinitcpio.conf` 并运行 `mkinitcpio -P` 重建所有 initramfs 镜像。 然后重启。 

**如果不需要`udev`**，第一次启动应该会成功。 如果出现故障（例如，Arch 找不到根分区或键盘失灵），则需要返回并从`default_options`行的`-S`参数中删除`udev`，然后再试一次。 如果需要使用 `udev`，请注意启动时间不会有明显改善，继续尝试只能作为学习经验。 

##  整理模块

现在您已经有了一个已知正常的可启动 initramfs，是时候进一步精简 initramfs 了。通常是一次删除几个模块，重建 initramfs 映像，然后重新启动以查看一切是否仍然正常。若有功能异常，请使用 `fallback` initramfs 映像重启并重新添加已删除的模块，直到再次恢复正常。多次重复，直到只剩下所需的模块。 这可能是相对乏味的过程，因此提供了以下列表，以便减少前期工作。 

**注意：** 以下仅作示例参考，并不意味着适合每台设备。

###  文件系统模块

**注意：** 只需要对应的模块：启动时需要检查文件系统的 `root` 设备和在 `/etc/fstab` 中的其他设备

  * `ext[2,3,4]`
  * `xfs`
  * `jfs`
  * `reiserfs`

###  存储设备模块

  * `sd_mod` 用于所有 SCSI、SATA 和 PATA（IDE）设备
  * `ahci` 用于现代 AHCI 控制器上的 SATA 设备
  * `nvme` 和 `nvme_core` 用于 NVMe（M.2、PCI-E）设备
  * `sata_*` 用于 IDE 模式控制器上的 SATA 设备
  * `pata_*` 用于 PATA（IDE）设备
  * `ehci_pci` 和 `usb_storage` 用于 USB 存储设备
  * `virtio_blk` 和 `virtio_pci` 用于使用 VirtIO 进行存储的 QEMU/KVM 虚拟机

###  键盘模块

  * `atkbd` 用于 AT 和 PS/2 键盘，以及 QEMU/KVM 中的模拟键盘。
  * `hid_generic`、`ohci_pci`和 `usbhid` 用于普通 USB 键盘。
  * `hid_logitech_dj`、`uhci_hcd` 和 `usbhid` 适用于使用罗技统一接收器的罗技 USB 键盘（**需要** {ic|udev}} **钩子** ）。

##  收尾工作

将 initramfs 压缩到最小后，移除（或注释掉）`.preset` 文件中的 `normal_*` 行，并移除 `/boot` 中的 `initramfs-linux*-normal.img` 文件。 
