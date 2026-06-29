**翻译状态：**

  * 本文（或部分内容）译自 [Udev](<https://wiki.archlinux.org/title/Udev> "arch:Udev")，最近一次同步于 2023-01-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Udev?diff=0&oldid=765060>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Udev_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

udev 是一个用户空间的设备管理器，用于为事件设置处理程序。作为守护进程， udev 接收的事件主要由 linux 内核生成，这些事件是外部设备产生的物理事件。总之， udev 探测外设和热插拔，将设备控制权传递给内核，例如加载内核模块或设备固件。 

_udev_ 是一个用户空间系统，可以让操作系统管理员为事件注册用户空间处理器。为了实现外设侦测和热插拔， _udev_ 守护进程接收 Linux 内核发出的外设相关事件; 加载内核模块、设备固件; 调整设备权限，让普通用户和用户组能够访问设备。 

作为 devfsd 和 hotplug 的替代品， udev 还负责管理 `/dev` 中的设备节点，即添加、链接和重命名节点，取代了 _hotplug_ 和 _hwdetect_ 。 

udev 并行处理事件，具有潜在的性能优势，但是无法保证每次加载模块的顺序，例如如果有两个硬盘， `/dev/sda` 在下次启动后可能变成 `/dev/sdb` 。[本文后面](<#%E8%AE%BE%E7%BD%AE%E9%9D%99%E6%80%81%E8%AE%BE%E5%A4%87%E5%90%8D>)有更详细的信息。 

##  安装

Udev 现在是 [systemd](<https://archlinux.org/packages/?name=systemd>)包 的组成部分，默认已安装。有关信息请查阅 `systemd-udevd.service(8)` 的[手册页](<../zh-cn/Man_page.html> "Man page")。 

##  udev 规则

udev 规则以管理员身份编写并保存在 `/etc/udev/rules.d/` 目录，其文件名必须以 `.rules` 结尾。各种软件包提供的规则文件位于 `/lib/udev/rules.d/`。如果 `/usr/lib` 和 `/etc` 这两个目录中有同名文件，则 `/etc` 中的文件优先。 

要学习 _udev_ 规则，请参考 [udev(7)](<https://man.archlinux.org/man/udev.7>) 手册和[编写 udev 规则](<http://www.reactivated.net/writing_udev_rules.html>)及其提供的一些[实用案例](<http://www.reactivated.net/writing_udev_rules.html#example-printer>)。 

###  编写 udev 规则

**警告：** 要挂载可移动设备，请**不要** 通过在 udev 规则中调用 `mount` 命令的方法。对 FUSE 文件系统将会导致 `Transport endpoint not connected` 错误。应代之以 [udisks](<../zh-cn/Udisks_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Udisks \(简体中文\)") 以正确处理自动挂载。或者把挂载动作放在 udev 规则内部： 

将 `/usr/lib/systemd/system/systemd-udevd.service` 复制到 `/etc/systemd/system/systemd-udevd.service`，将 `MountFlags=slave` 替换为 `MountFlags=shared`。[（来源）](<https://unix.stackexchange.com/a/154318>)

udev 不应该用于启动长期运行的进程.

  * 要想学习写udev规则，请访问[编写 udev 规则](<http://www.reactivated.net/writing_udev_rules.html>)。
  * 要想查看 udev 规则的例子，请查阅上述文章的[范例](<http://www.reactivated.net/writing_udev_rules.html#example-printer>)章节。

下面是一个规则的实例，当接入摄像头时创建符号链接 `/dev/video-cam1` 。 

假设摄像头已经连接，加载的设备为 `/dev/video2`。编写此规则的原因是下次引导时这个设备名可能变化，比如变成 `/dev/video0`。 
    
    $ udevadm info --attribute-walk --path=$(udevadm info --query=path --name=/dev/video2)
    
    Udevadm info starts with the device specified by the devpath and then walks up the chain of parent devices.
    It prints for every device found, all possible attributes in the udev rules key format.
    A rule to match, can be composed by the attributes of the device and the attributes from one single parent device.
    
    looking at device '/devices/pci0000:00/0000:00:04.1/usb3/3-2/3-2:1.0/video4linux/video2':
      KERNEL=="video2"
      SUBSYSTEM=="video4linux"
       ...
    looking at parent device '/devices/pci0000:00/0000:00:04.1/usb3/3-2/3-2:1.0':
      KERNELS=="3-2:1.0"
      SUBSYSTEMS=="usb"
      ...
    looking at parent device '/devices/pci0000:00/0000:00:04.1/usb3/3-2':
      KERNELS=="3-2"
      SUBSYSTEMS=="usb"
      ATTRS{idVendor}=="05a9"
      ATTRS{manufacturer}=="OmniVision Technologies, Inc."
      ATTRS{removable}=="unknown"
      ATTRS{idProduct}=="4519"
      ATTRS{bDeviceClass}=="00"
      ATTRS{product}=="USB Camera"
      ...

为了确认 webcamera 设备，我们使用 `KERNEL=="video2"` 和 `SUBSYSTEM=="video4linux"`，向上两极到 `SUBSYSTEMS=="usb"`，使用厂商和产品 ID 进行定位： `ATTRS{idVendor}=="05a9"` 和 `ATTRS{idProduct}=="4519"`。 

可以为此设备编写规则: 
    
    /etc/udev/rules.d/83-webcam.rules
    
    KERNEL=="video[0-9]*", SUBSYSTEM=="video4linux", SUBSYSTEMS=="usb", ATTRS{idVendor}=="05a9", ATTRS{idProduct}=="4519", SYMLINK+="video-cam"

这里使用 `SYMLINK+="video-cam"` 创建了软链接，这样可以设置用户 `OWNER="john"` 或用户组 `GROUP="video"` 或者通过 `MODE="0660"` 设置权限。 

如果要编写设备移除时执行的脚本，请注意此时可能无法访问设备属性。需要使用提前设置的[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。要监控这些环境变量，在拔掉设备时执行如下命令： 
    
    $ udevadm monitor --property --udev
    
在命令输出中可以看到类似 `ID_VENDOR_ID` 和 `ID_MODEL_ID` 这样的值，它们对应 `idVendor` 和 `idProduct` 属性。下面是一个使用设备环境变量的规则示例： 
    
    /etc/udev/rules.d/83-webcam-removed.rules
    
    ACTION=="remove", SUBSYSTEM=="usb", ENV{ID_VENDOR_ID}=="05a9", ENV{ID_MODEL_ID}=="4519", RUN+="_/path/to/your/script_ "

###  列出设备属性

要列出所有设备的属性以用来编写规则的话，运行下面的命令： 
    
    $ udevadm info --attribute-walk --name=_device_name_
    
将 `device name` 替换为系统中存在的设备，比如 `/dev/sda` 或 `/dev/ttyUSB0`。 

如果你不知道设备名，你也可以列出某个系统路径的属性： 
    
     $ udevadm info --attribute-walk --path=/sys/class/backlight/acpi_video0
    
可以通过类型过滤掉不需要的输出: 
    
    $ ls /dev/_class_ /by-id
    
可以在 `--name` 中使用最终文件或软连接: 
    
    $ udevadm info --attribute-walk --name=/dev/input/by-id/usb-foostan_Corne-event-kbd
    
要获得裸 USB 设备(未创建任何子设备) 的信息，需要使用完整的 USB 设备路径, 先启动监控模式，然后插入 USB 设备： 
    
    $ udevadm monitor
    
    ...
    KERNEL[26652.638931] add      /devices/pci0000:00/0000:00:01.2/0000:02:00.0/0000:03:05.0/0000:05:00.0/usb1/1-3 (usb)
    KERNEL[26652.639153] add      /devices/pci0000:00/0000:00:01.2/0000:02:00.0/0000:03:05.0/0000:05:00.0/usb1/1-3/1-3:1.0 (usb)
    ...

可以使用最深的路径， `_--attribute-walk_` 会显示全部父属性： 
    
    $ udevadm info --attribute-walk --path=_/devices/pci0000:00/0000:00:01.2/0000:02:00.0/0000:03:05.0/0000:05:00.0/usb1/1-3/1-3:1.0_
    
###  加载前测试规则
    
    # udevadm test $(udevadm info --query=path --name=_device_name_) 2>&1
    
这不会运行你的规则中的所有命令，但会处理已有设备的符号连接，如果你不能加载它们这也许会变得方便。也可以直接输入你测试的设备路径： 
    
    # udevadm test /sys/class/backlight/acpi_video0/
    
###  加载新规则

Udev 自动侦测规则文件的变化，所以修改会立即生效，无需重启 udev。但已接入设备的规则不会自动触发。像 USB 这类热插拔设备也许需要重新插拔才能使新规则生效，也可能需要卸载并重载内核的 ohci-hcd 和 ehci-hcd 模块以重新挂载所有 USB 设备。 

如果规则自动重载失败 
    
    # udevadm control --reload
    
可以手工强制触发规则 
    
    # udevadm trigger
    
## Udisks

参阅 [Udisks](<../zh-cn/Udisks_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Udisks \(简体中文\)"). 

##  提示与技巧

### Mounting drives in rules

To mount removable drives, do not call `mount` from _udev_ rules. This is ill-advised for two reasons: 

  1. systemd by default runs `systemd-udevd.service` with a separate "mount namespace" (see [namespaces(7)](<https://man.archlinux.org/man/namespaces.7>)), which means that mounts will not be visible to the rest of the system.
  2. Even if you change the service parameters to fix this (commenting out the `PrivateMounts` and `MountFlags` lines), there is another problem which is that processes started from Udev are killed after a few seconds. In case of FUSE filesystems, such as [NTFS-3G](<../zh-cn/NTFS-3G.html> "NTFS-3G"), _mount_ starts a user-space process to handle the filesystem internals; when this is killed you will get `Transport endpoint not connected` errors if you try to access the filesystem.

There are some options that work: 

  * Start a custom systemd service from the Udev rule; the systemd service can invoke a script which can start any number of long-running processes (like FUSE). A concise example which automatically mounts USB disks under `/media` is [udev-media-automount](<https://github.com/Ferk/udev-media-automount>). A variant of the same idea is explained in [this blog post](<http://jasonwryan.com/blog/2014/01/20/udev/>).
  * Use `systemd-mount` instead of `mount` in your Udev rule. This is [recommended by systemd developers](<https://github.com/systemd/systemd/issues/11982#issuecomment-472529566>). For example this Udev rule should mount USB disks under `/media`:

    ACTION=="add", SUBSYSTEMS=="usb", SUBSYSTEM=="block", ENV{ID_FS_USAGE}=="filesystem", RUN{program}+="/usr/bin/systemd-mount --no-block --automount=yes --collect $devnode /media"

  * Use a package like [udisks](<../zh-cn/Udisks.html> "Udisks") or [udiskie](</wzh/index.php?title=Udiskie&action=edit&redlink=1> "Udiskie（页面不存在）"). These are very powerful, but difficult to set up. Also, they are meant to be used in single user sessions, since they make some filesystems available under the ownership of the unprivileged user whose session is currently active.

### Allowing regular users to use devices

When a [kernel](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernel") driver initializes a device, the default state of the device node is to be owned by `root:root`, with permissions `600`. [[1]](<https://github.com/torvalds/linux/blob/v5.19/drivers/base/devtmpfs.c#L11-L13>) This makes devices inaccessible to regular users unless the driver changes the default, or a udev rule in userspace changes the permissions. 

The `OWNER`, `GROUP`, and `MODE` udev values can be used to provide access, though one encounters the issue of how to make a device usable to all users without an overly permissive mode. Ubuntu's approach is to create a `plugdev` group that devices are added to, but this practice is not only discouraged by the systemd developers, [[2]](<https://bugzilla.redhat.com/show_bug.cgi?id=815093>) but considered a bug when shipped in udev rules on Arch ([FS#35602](<https://bugs.archlinux.org/task/35602>)). Another approach historically employed, as described in [Users and groups#Pre-systemd groups](<../zh-cn/Users_and_groups.html#Pre-systemd_groups> "Users and groups"), is to have different groups corresponding to categories of devices. 

The modern recommended approach for systemd systems is to use a `MODE` of `660` to let the group use the device, and then attach a `TAG` named `uaccess` [[3]](<https://github.com/systemd/systemd/blob/main/rules.d/70-uaccess.rules.in>). This special tag makes udev apply a [dynamic user ACL](<https://github.com/systemd/systemd/blob/main/src/udev/udev-builtin-uaccess.c>) to the device node, which coordinates with [systemd-logind(8)](<https://man.archlinux.org/man/systemd-logind.8>) to make the device usable to logged-in users. For an example of a udev rule implementing this: 
    
    /etc/udev/rules.d/71-device-name.rules
    
    SUBSYSTEMS=="usb", ATTRS{idVendor}=="_vendor_id_ ", ATTRS{idProduct}=="_product_id_ ", MODE="0660", TAG+="uaccess"

### Execute when HDMI cable is plugged in or unplugged

Create the rule `/etc/udev/rules.d/95-hdmi-plug.rules` with the following content: 
    
    ACTION=="change", SUBSYSTEM=="drm", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="/home/_username_ /.Xauthority", RUN+="_/path/to/script.sh_ "
    
**注意：** If the rule triggers before the X server starts, it may not work as intended. See [#X programs in RUN rules hang when no X server is present](<#X_programs_in_RUN_rules_hang_when_no_X_server_is_present>).

###  VGA 线缆接入时执行规则

创建包含下列内容的规则文件 `/etc/udev/rules.d/95-monitor-hotplug.rules` ，可以在 VGA 线缆插入时执行 [arandr](<https://archlinux.org/packages/?name=arandr>)包： 
    
    KERNEL=="card0", SUBSYSTEM=="drm", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="/home/_username_ /.Xauthority", RUN+="/usr/bin/arandr"
    
**提示：** 某些显示管理器把 .Xauthority 文件保存在用户家目录以外的位置，需要修改 ENV{XAUTHORITY} 的内容。例如，[GNOME 显示管理器](</wzh/index.php?title=GDM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "GDM \(简体中文\)（页面不存在）") 里的.Xauthority 文件路径如下所示： 
    
    $ printenv XAUTHORITY
    
    /run/user/1000/gdm/Xauthority

**注意：** If the rule triggers before the X server starts, it may not work as intended. See [#X programs in RUN rules hang when no X server is present](<#X_programs_in_RUN_rules_hang_when_no_X_server_is_present>).

###  侦测新的 eSATA 设备

If your eSATA drive is not detected when you plug it in, there are a few things you can try. You can reboot with the eSATA plugged in. Or you could try 
    
    # echo 0 0 0 > /sys/class/scsi_host/host*/scan
    
Or you could install [scsiadd](<https://aur.archlinux.org/packages/scsiadd/>)AUR (from the AUR) and try 
    
    # scsiadd -s
    
Hopefully, your drive is now in `/dev`. If it is not, you could try the above commands while running 
    
    # udevadm monitor
    
to see if anything is actually happening. 

###  将内置 SATA 接口标记为 eSATA

If you connected a eSATA bay or an other eSATA adapter the system will still recognize this disk as an internal SATA drive. [GNOME](<../zh-cn/GNOME.html> "GNOME") and [KDE](<../zh-cn/KDE.html> "KDE") will ask you for your root password all the time. The following rule will mark the specified SATA-Port as an external eSATA-Port. With that, a normal GNOME user can connect their eSATA drives to that port like a USB drive, without any root password and so on. 
    
    /etc/udev/rules.d/10-esata.rules
    
    DEVPATH=="/devices/pci0000:00/0000:00:1f.2/host4/*", ENV{UDISKS_SYSTEM}="0"
    
**注意：** The `DEVPATH` can be found after connection the eSATA drive with the following commands (replace `sdb` accordingly): 
    
    # udevadm info -q path -n /dev/sdb
    /devices/pci0000:00/0000:00:1f.2/host4/target4:0:0/4:0:0:0/block/sdb
    
    # find /sys/devices/ -name sdb
    /sys/devices/pci0000:00/0000:00:1f.2/host4/target4:0:0/4:0:0:0/block/sdb
    
###  设置静态设备名

由于 udev 异步加载所有模块，使得它们被初始化的次序不同。这将导致设备会随机改变名称。可以添加一条 udev 规则使得设备使用静态名称。 

对于块设备和网络设备的规则配置，请分别参阅[块设备持久化命名](</wzh/index.php?title=Persistent_block_device_naming_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Persistent block device naming \(简体中文\)（页面不存在）")和[网络配置-设备命名](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E6%9B%B4%E6%94%B9%E6%8E%A5%E5%8F%A3%E5%90%8D%E7%A7%B0> "网络配置")。 

####  视频设备

For setting up the webcam in the first place, refer to [网络摄像机配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E6%91%84%E5%83%8F%E6%9C%BA%E9%85%8D%E7%BD%AE.html> "网络摄像机配置"). 

Using multiple webcams will assign video devices as `/dev/video*` randomly on boot. The recommended solution is to create symlinks using a _udev_ rule as in the [#udev rule example](<#udev_rule_example>): 
    
    /etc/udev/rules.d/83-webcam.rules
    
    KERNEL=="video[0-9]*", SUBSYSTEM=="video4linux", SUBSYSTEMS=="usb", ATTRS{idVendor}=="05a9", ATTRS{idProduct}=="4519", SYMLINK+="video-cam1"
    KERNEL=="video[0-9]*", SUBSYSTEM=="video4linux", SUBSYSTEMS=="usb", ATTRS{idVendor}=="046d", ATTRS{idProduct}=="08f6", SYMLINK+="video-cam2"

**注意：** Using names other than `/dev/video*` will break preloading of `v4l1compat.so` and perhaps `v4l2convert.so`

####  打印机

If you use multiple printers, `/dev/lp[0-9]` devices will be assigned randomly on boot, which will break e.g. [CUPS](<../zh-cn/CUPS.html> "CUPS") configuration. 

You can create following rule, which will create symlinks under `/dev/lp/by-id` and `/dev/lp/by-path`, similar to [Persistent block device naming](<../zh-cn/Persistent_block_device_naming.html> "Persistent block device naming") scheme: 
    
    /etc/udev/rules.d/60-persistent-printer.rules
    
    ACTION=="remove", GOTO="persistent_printer_end"
    
    # This should not be necessary
    #KERNEL!="lp*", GOTO="persistent_printer_end"
    
    SUBSYSTEMS=="usb", IMPORT{builtin}="usb_id"
    ENV{ID_TYPE}!="printer", GOTO="persistent_printer_end"
    
    ENV{ID_SERIAL}=="?*", SYMLINK+="lp/by-id/$env{ID_BUS}-$env{ID_SERIAL}"
    
    IMPORT{builtin}="path_id"
    ENV{ID_PATH}=="?*", SYMLINK+="lp/by-path/$env{ID_PATH}"
    
    LABEL="persistent_printer_end"
    
### Identifying a disk by its serial

To perform some action on a specific disk device `/dev/sd _X_` identified permanently by its unique serial `ID_SERIAL_SHORT` as displayed with `udevadm info /dev/sd _X_`, one can use the below rule. It is passing as a parameter the device name found if any to illustrate: 
    
    /etc/udev/rules.d/69-disk.rules
    
    ACTION=="add", KERNEL=="sd[a-z]", ENV{ID_SERIAL_SHORT}=="_X5ER1ALX_ ", RUN+="/path/to/script /dev/%k"

###  唤醒挂起的 USB 设备

A udev rule can be useful to enable the [wakeup triggers](<../zh-cn/Wakeup_triggers.html> "Wakeup triggers") of a USB device, like a mouse or a keyboard, so that it can be used to wake the system from sleep. 

**注意：** By default, the USB host controllers are all enabled for wakeup. The status can be checked using `cat /proc/acpi/wakeup`. The rule below is in this case not necessary but can be used as a template to perform other actions, like disabling the wakeup functionality for example. 

First, identify the vendor and product identifiers of the USB device. They will be used to recognize it in the udev rule. For example: 
    
    $ lsusb | grep Logitech
    
    Bus 007 Device 002: ID **046d** :**c52b** Logitech, Inc. Unifying Receiver
    
Then, find where the device is connected to using: 
    
    $ grep _c52b_ /sys/bus/usb/devices/*/idProduct
    
    /sys/bus/usb/devices/**1-1.1.1.4/** idProduct:c52b
    
Now create the rule to change the `power/wakeup` attribute of both the device and the USB controller it is connected to whenever it is added: 
    
    /etc/udev/rules.d/50-wake-on-device.rules
    
    ACTION=="add", SUBSYSTEM=="usb", DRIVERS=="usb", ATTRS{idVendor}=="**046d** ", ATTRS{idProduct}=="**c52b** ", ATTR{power/wakeup}="enabled", ATTR{driver/**1-1.1.1.4** /power/wakeup}="enabled"

###  触发事件

It can be useful to trigger various udev events. For example, you might want to simulate a USB device disconnect on a remote machine. In such cases, use `udevadm trigger`: 
    
     # udevadm trigger --verbose --type=subsystems --action=remove --subsystem-match=usb --attr-match="idVendor=abcd"
    
This command will trigger a USB remove event on all USB devices with vendor ID `abcd`. 

### Triggering desktop notifications from a udev rule

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** This is a lengthy monologue on how to hardcode variables（在 [Talk:Udev](<../zh-cn/Talk:Udev.html>) 中讨论）

Invoking an external script containing calls to `notify-send` via _udev_ [can sometimes be challenging](<https://bbs.archlinux.org/viewtopic.php?id=212364>) since the notification(s) never display on the Desktop. Here is an example of what commands and environmental variables need to be included in which files for `notify-send` to successfully be executed from a _udev_ rule. 

**注意：** A number of variables are hardcoded in this example, thus consider making them portable (i.e., $USER rather than user's shortname) once you understand the example. 

1) The following _udev_ rule executes a script that plays a notification sound and sends a desktop notification when screen brightness is changed according to power state on a laptop. Create the file: 
    
    /etc/udev/rules.d/99-backlight_notification.rules
    
    # Rule for when switching to battery
    ACTION=="change", SUBSYSTEM=="power_supply", ATTR{type}=="Mains", ATTR{online}=="0", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="/home/USERNAME/.Xauthority" RUN+="/usr/bin/su USERNAME_TO_RUN_SCRIPT_AS -c /usr/local/bin/brightness_notification.sh"
    # Rule for when switching to AC
    ACTION=="change", SUBSYSTEM=="power_supply", ATTR{type}=="Mains", ATTR{online}=="1", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="/home/USERNAME/.Xauthority" RUN+="/usr/bin/su USERNAME_TO_RUN_SCRIPT_AS -c /usr/local/bin/brightness_notification.sh"

  * `USERNAME_TO_RUN_SCRIPT_AS` and `USERNAME` need to be changed to that of the shortname for the user of the graphical session where the notification will be displayed;
  * the script needs to be executed with `/usr/bin/su`, which will place its ownership under the user of the graphical session (rather than root/the system) where the notification will be displayed.

2) Contents of the executable script to be run on trigger of the _udev_ rule: 
    
    /usr/local/bin/brightness_notification.sh
    
    #!/bin/sh
    
    export XAUTHORITY=/home/USERNAME_TO_RUN_SCRIPT_AS/.Xauthority
    export DISPLAY=:0
    export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/UID_OF_USER_TO_RUN_SCRIPT_AS/bus"
    
    /usr/bin/sudo -u USERNAME_TO_RUN_SCRIPT_AS /usr/bin/paplay --server=/run/user/UID_OF_USER_TO_RUN_SCRIPT_AS/pulse/native /home/USERNAME/.i3/sounds/Click1.wav > /dev/null 2>&1
    
    /usr/bin/notify-send --icon=/usr/share/icons/gnome/256x256/status/battery-full-charging.png 'Changing Power States' --expire-time=4000

  * `USERNAME_TO_RUN_SCRIPT_AS`, `UID_OF_USER_TO_RUN_SCRIPT_AS` and `USERNAME` needs to be changed to that of the shortname for the user and user's UID of the graphical session where the notification will be displayed;
  * `/usr/bin/sudo` is needed when playing audio via pulseaudio;
  * three environmental variables (i.e., `XAUTHORITY`, `DISPLAY` and `DBUS_SESSION_BUS_ADDRESS`) for the user of the graphical session where the notification will be displayed need to be defined and exported.

**提示：** See also [xpub](<https://aur.archlinux.org/packages/xpub/>)AUR as a method for getting the user's display environment variables and exporting the last into _udev_ rules via `IMPORT` key. 

3) Load/reload the new _udev_ rule (see above) and test it by unplugging the power supply to the laptop. 

**注意：** If the rule triggers before the X server starts, it may not work as intended. See [#X programs in RUN rules hang when no X server is present](<#X_programs_in_RUN_rules_hang_when_no_X_server_is_present>).

##  排错

###  屏蔽模块

极个别情况下，udev 也会犯错或加载错误的模块。为了防止错误的发生，你可以使用模块禁用列表。只要模块加入该列表，无论是启动时，或者是运行时（如usb硬盘等）udev都不会加载这些模块。参见[blacklisting](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%BB%91%E5%90%8D%E5%8D%95> "Blacklisting"). 

### Debug output

To get hardware debug info, use the [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") `udev.log-priority=debug`. Alternatively you can set 
    
    /etc/udev/udev.conf
    
    udev_log="debug"

This option can also be compiled into your initramfs by adding the config file to your `FILES` array 
    
    /etc/mkinitcpio.conf
    
    FILES="... /etc/udev/udev.conf"

and then rebuilding the initramfs with 
    
    # mkinitcpio -p linux
    
###  udevd 引导时挂起

After migrating to LDAP or updating an LDAP-backed system udevd can hang at boot at the message "Starting UDev Daemon". This is usually caused by udevd trying to look up a name from LDAP but failing, because the network is not up yet. The solution is to ensure that all system group names are present locally. 

Extract the group names referenced in udev rules and the group names actually present on the system: 
    
    # grep -Fr GROUP /etc/udev/rules.d/ /usr/lib/udev/rules.d/ | sed 's:.*GROUP="\([-a-z_]\{1,\}\)".*:\1:' | sort -u >udev_groups
    # cut -d: -f1 /etc/gshadow /etc/group | sort -u >present_groups
    
To see the differences, do a side-by-side diff: 
    
    # diff -y present_groups udev_groups
    ...
    network							      <
    nobody							      <
    ntp							      <
    optical								optical
    power							      |	pcscd
    rfkill							      <
    root								root
    scanner								scanner
    smmsp							      <
    storage								storage
    ...
    
In this case, the `pcscd` group is for some reason not present in the system. [Add the missing groups](<../zh-cn/Users_and_groups.html#Group_management> "Users and groups"). Also, make sure that local resources are looked up before resorting to LDAP. `/etc/nsswitch.conf` should contain the following line: 
    
    group: files ldap
    
###  一些移动设备不可移除

You need to create a custom _udev_ rule for that particular device. To get definitive information of the device you can use either `ID_SERIAL` or `ID_SERIAL_SHORT` (remember to change `/dev/sdb` if needed): 
    
    $ udevadm info /dev/sdb | grep ID_SERIAL
    
Then we set `UDISKS_AUTO="1"` to mark the device for automounting and `UDISKS_SYSTEM="0"` to mark the device as "removable". See [udisks(8)](<https://man.archlinux.org/man/udisks.8>) for details. 
    
    /etc/udev/rules.d/99-removable.rules
    
    ENV{ID_SERIAL_SHORT}=="_serial_number_ ", ENV{UDISKS_AUTO}="1", ENV{UDISKS_SYSTEM}="0"

Remember to reload _udev_ rules with `udevadm control --reload`. Next time you plug your device in, it will be treated as an external drive. 

###  声音问题和一些不能自动加载的模块

一些用户发现 `/etc/modprobe.d/sound.conf` 中的遗留配置会引起这些问题，请清理配置并重试。 

**注意：** 从 `udev>=171` 开始 OSS 模拟模块(`snd_seq_oss, snd_pcm_oss, snd_mixer_oss`) 默认不会自动装载。

###  IDE CD/DVD 驱动器的支持

Starting with version 170, udev does not support CD-ROM/DVD-ROM drives that are loaded as traditional IDE drives with the `ide_cd_mod` module and show up as `/dev/hd*`. The drive remains usable for tools which access the hardware directly, like _cdparanoia_ , but is invisible for higher userspace programs, like KDE. 

A cause for the loading of the ide_cd_mod module prior to others, like sr_mod, could be e.g. that you have for some reason the module piix loaded with your [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs"). In that case you can just replace it with ata_piix in your `/etc/mkinitcpio.conf`. 

###  光驱被标识为磁盘

If the group ID of your optical drive is set to `disk` and you want to have it set to `optical`, you have to create a custom udev rule: 
    
    /etc/udev/rules.d
    
    # permissions for IDE CD devices
    SUBSYSTEMS=="ide", KERNEL=="hd[a-z]", ATTR{removable}=="1", ATTRS{media}=="cdrom*", GROUP="optical"
    
    # permissions for SCSI CD devices
    SUBSYSTEMS=="scsi", KERNEL=="s[rg][0-9]*", ATTRS{type}=="5", GROUP="optical"

### X programs in RUN rules hang when no X server is present

When _xrandr_ or another X-based program tries to connect to an X server, it falls back to a TCP connection on failure. However, due to `IPAddressDeny` in the [systemd-udev service configuration](<https://github.com/systemd/systemd/blob/main/units/systemd-udevd.service.in#L43>), this hangs. Eventually the program will be killed and event processing will resume. 

If the rule is for a drm device and the hang causes event processing to complete once the X server has started, this can cause 3D acceleration to stop working with a `failed to authenticate magic` error. 

##  参阅

  * [udev manual](<https://www.freedesktop.org/software/systemd/man/udev.html>)
  * [An Introduction to udev](<https://opensource.com/article/18/11/udev>)
  * [udev 邮件列表](<http://vger.kernel.org/vger-lists.html#linux-hotplug>)
  * [编写 udev 规则](<http://jasonwryan.com/blog/2014/01/20/udev/>)
  * [Writing udev rules](<http://www.reactivated.net/writing_udev_rules.html>)
  * [LFS 系统设备与模块处理](<https://www.linuxfromscratch.org/lfs/view/stable/chapter09/udev.html>)
  * [Running GUI or accessing display variables from udev rules](<https://github.com/Ventto/xpub>)
  * [openSUSE udev documentation](<https://doc.opensuse.org/documentation/leap/reference/html/book-reference/cha-udev.html>)
  * 中文读者可参阅[金步国](<http://www.jinbuguo.com/>)先生翻译的 [udev 中文手册](<http://www.jinbuguo.com/systemd/udev.html>)
