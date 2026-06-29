相关文章

  * [挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载")

**翻译状态：**

  * 本文（或部分内容）译自 [USB storage devices](<https://wiki.archlinux.org/title/USB_storage_devices> "arch:USB storage devices")，最近一次同步于 2024-08-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/USB_storage_devices?diff=0&oldid=814959>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/USB_storage_devices_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文介绍了如何在 Linux 下使用流行的 USB 闪存盘。不过，它也适用于其他设备，如数码相机，这些设备就像 USB 存储设备一样。 

如果你的系统是最新的 Arch 内核，并使用现代[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")，你的设备就会直接显示在桌面上，无需打开控制台。 

##  使用 udisks 自动安装

这是最简单、最常用的方法。许多[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")都使用这种方法，但也可以单独使用。 

详细信息，包括挂载助手列表，请参阅 [Udisks](<../zh-cn/Udisks.html> "Udisks")。 

##  手动挂载

**注意：** 在确定 Arch Linux 无法挂载 USB 设备之前，请务必检查所有可用端口。有些端口可能不共享同一个控制器，从而导致无法挂载设备。

###  获取支持 usb_storage 的内核

如果不使用定制的内核，就可以使用，因为所有 Arch Linux 内核都已正确配置。如果使用定制内核，请确保其编译了 SCSI-Support、SCSI-Disk-Support 和 usb_storage。如果使用最新的 [udev](<../zh-cn/Udev.html> "Udev")，只需插入设备，系统就会自动加载所有必要的内核模块。 

###  识别设备

访问存储设备首先需要内核分配的标识符。详见[文件系统#查看现有文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%9F%A5%E7%9C%8B%E7%8E%B0%E6%9C%89%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "文件系统")。 

新插入的设备通常会显示在 [Journal](<../zh-cn/Systemd/Journal.html> "Journal") 中。 

###  挂载 USB 存储器

请参阅[文件系统#挂载文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "文件系统")。 

如果 `mount` 无法识别设备的[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")，可以尝试使用 `-t` 参数，详情请参见 [mount(8)](<https://man.archlinux.org/man/mount.8>) 。如果挂载失败，可以尝试[重新创建文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E5%88%9B%E5%BB%BA%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "文件系统")，甚至[重新分区磁盘](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")。 

**注意：** 有关使用 [sudo](<../zh-cn/Sudo.html> "Sudo") 的挂载/卸载脚本示例，请参阅 [[1]](<https://gist.github.com/anonymous/a69093a51f83b53d9fc5>)。

####  允许普通用户写入

如果想让非 root 用户写入 U 盘，可以发出以下命令： 
    
    # mount -o gid=_users_ ,fmask=113,dmask=002 /dev/sda1 /mnt/usbstick
    
如果不起作用，请确保[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")可以以根用户身份挂载和写入，详见上一节。 

####  使用 fstab 以作为普通用户操作

如果想让普通用户执行挂载/卸载操作，请参阅 [FAT#以普通用户身份写入 FAT32](<../zh-cn/FAT.html#%E4%BB%A5%E6%99%AE%E9%80%9A%E7%94%A8%E6%88%B7%E8%BA%AB%E4%BB%BD%E5%86%99%E5%85%A5_FAT32> "FAT")。 

####  挂载工具

多个[挂载工具](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#%E6%8C%82%E8%BD%BD%E5%B7%A5%E5%85%B7> "应用程序列表/工具")便于以普通用户身份挂载。 

##  问题解决

###  未检测到 USB 存储设备

如果您已连接 USB 存储设备，但它未被 [lsblk](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#lsblk> "Lsblk") 列出，而是出现在 [journal](<../zh-cn/Systemd/Journal.html> "Journal") 中，但未被分配块设备，请参阅[常规故障排除#内核升级后部分外设无法使用](<../zh-cn/%E5%B8%B8%E8%A7%84%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html#%E5%86%85%E6%A0%B8%E5%8D%87%E7%BA%A7%E5%90%8E%E9%83%A8%E5%88%86%E5%A4%96%E8%AE%BE%E6%97%A0%E6%B3%95%E4%BD%BF%E7%94%A8> "常规故障排除")。 

此外，请确保您的 BIOS 已启用 XHCI Handoff 和 EHCI Handoff，但对于大多数现代设备来说，这通常不是问题。 

###  卸载所有分区后设备未关闭

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 请建议如何在卸载后自动关闭设备。 (在 [Talk:USB 存储设备](<../zh-cn/Talk:USB_%E5%AD%98%E5%82%A8%E8%AE%BE%E5%A4%87.html>) 中讨论)

如果不关闭设备电源，可能会导致： 

  * 硬盘驱动器没有停放磁头，在旋转时发出微弱的刮擦声并降低设备性能 [[2]](<http://linuxfocus.org/~guido/scripts/spin-down-usb-hard-drive-linux.html>)，或者
  * 固态硬盘（尤其是老式固态硬盘）不刷新缓存缓冲区或更新映射表，导致数据丢失 [[3]](<https://www.kingston.com/us/solutions/servers-data-centers/ssd-power-loss-protection>)。

卸载分区时，设备仍处于开机状态。为了安全地卸载，您应该要求系统先将其关闭： [[4]](<https://unix.stackexchange.com/a/43450>)
    
    # echo 1 > /sys/block/_disk_name_ /device/delete
    
如果使用 [udisks](<../zh-cn/Udisks.html> "Udisks")，则可以使用这些命令： [[5]](<https://unix.stackexchange.com/a/178648>)
    
    $ udisksctl unmount -b /dev/sd _XY_
    $ udisksctl power-off -b /dev/sd _X_
    
###  设备已检测到，但未注册为可安装设备

有[一套 udev 规则](<../zh-cn/Udev.html#u_dev_%E8%A7%84%E5%88%99> "Udev")，其中包括一条出于各种原因忽略某些特定设备的规则。某些硬件设备，如数码相机、便携式录音机等，可能会以某种方式格式化 usb 存储，从而触发忽略规则。你可以使用以下命令检查是否应用了这些规则，然后在默认设置中找到相应的条件： 
    
    $ udevadm info --attribute-walk --name=_device_name_ | grep UDISKS_IGNORE
    
如果是这种情况您的设备已将此属性设置为 _1_ ，您可以按照。[udev](<../zh-cn/Udev.html#%E7%BC%96%E5%86%99_udev_%E8%A7%84%E5%88%99> "Udev") 页面使用自定义规则来覆盖它。 
