**翻译状态：**

  * 本文（或部分内容）译自 [Android Debug Bridge](<https://wiki.archlinux.org/title/Android_Debug_Bridge> "arch:Android Debug Bridge")，最近一次同步于 2024-11-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Android_Debug_Bridge?diff=0&oldid=815785>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Android_Debug_Bridge_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Android 调试桥](<https://developer.android.com/studio/command-line/adb>)（ADB）是一种命令行工具，可用于安装、卸载和调试应用程序，传输文件和访问设备的 shell。 

##  安装

ADB 是平台-工具 [SDK 软件包](<../zh-cn/Android.html#SDK_packages> "Android")和 [android-tools](<https://archlinux.org/packages/?name=android-tools>)包 软件包的一部分。 

##  使用

###  连接设备

**提示：**

  * 对于部分设备，你可能需要先在设备上启用 [MTP](<../zh-cn/%E5%AA%92%E4%BD%93%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE.html> "MTP")，ADB 才能正常工作。其他一些设备需要启用 PTP 模式才能工作。
  * 许多设备的 [udev](<../zh-cn/Udev.html> "Udev") 规则都包含在 [libmtp](<https://archlinux.org/packages/?name=libmtp>)包 中，所以如果已安装该包，可能不再需要下面的部分步骤。
  * 确保你的 USB 线能够同时进行充电和数据传输。许多与移动设备捆绑的 USB 线不包含 USB 数据针。

要在 Arch 下通过 ADB 连接实体设备或手机，你必须： 

  1. 如果希望将设备连接到适当的 `/dev/` 项，可能需要安装 [android-udev](<https://archlinux.org/packages/?name=android-udev>)包。
  2. 将你的 Android 设备通过 USB 插入到电脑。
  3. 在你的手机或设备上启用 USB 调试功能： 
     * Jelly Bean（4.2）及更新的版本：进入 _设置 >关于手机_点击 _版本号_ 七次，直到出现一个弹出窗口说你已经成为开发者。在较新的 Android 操作系统版本上，版本号可能在一个名为 _软件信息_ 的菜单中。然后进入 _设置 >开发者>USB 调试_并启用它。设备会要求允许有特定指纹的电脑进行连接。勾选 _永久允许_ 选项会把 `~/.android/adbkey.pub` 复制到设备的 `/data/misc/adb/adb_keys` 位置中。
     * 较早的版本：这通常是在 _设置 >应用程序>开发>USB 调试_中进行。检查该选项后重新启动手机，以确保 USB 调试被启用。

如果 [ ADB 识别你的设备](<#%E6%A3%80%E6%B5%8B%E8%AE%BE%E5%A4%87>)（`adb devices` 为 `“device”而不是“unauthorized”`，或者它在 IDE 中可见并可访问，那么你已成功连接到手机。否则请看下面的说明。 

###  识别设备标识符

每个 Android 设备都有 USB 制造商/产品标识符。以 HTC Evo 为例： 
    
    vendor id: 0bb4
    product id: 0c8d
    
插入你的设备并执行： 
    
    $ lsusb
    
    ...
    Bus 002 Device 006: ID 0bb4:0c8d High Tech Computer Corp.
    ...
    
###  添加 udev 规则

如果你的设备没有包含在 [android-udev](<https://archlinux.org/packages/?name=android-udev>)包（或 [android-udev-git](<https://aur.archlinux.org/packages/android-udev-git/>)AUR），使用以下模板创建一个自定义的 [udev 规则](<../zh-cn/Udev.html#udev_%E8%A7%84%E5%88%99> "Udev")，将 `[VENDOR ID]` 和 `[PRODUCT ID]` 替换为[你的设备标识符](<#%E8%AF%86%E5%88%AB%E8%AE%BE%E5%A4%87%E6%A0%87%E8%AF%86%E7%AC%A6>)。 
    
    /etc/udev/rules.d/51-android.rules
    
    SUBSYSTEM=="usb", ATTR{idVendor}=="[VENDOR ID]", MODE="0660", GROUP="adbusers", TAG+="uaccess"
    SUBSYSTEM=="usb", ATTR{idVendor}=="[VENDOR ID]", ATTR{idProduct}=="[PRODUCT ID]", SYMLINK+="android_adb"
    SUBSYSTEM=="usb", ATTR{idVendor}=="[VENDOR ID]", ATTR{idProduct}=="[PRODUCT ID]", SYMLINK+="android_fastboot"
    
然后[重新加载 udev 规则](<../zh-cn/Udev.html#%E5%8A%A0%E8%BD%BD%E6%96%B0%E8%A7%84%E5%88%99> "Udev")。 

###  检测设备

设置好 udev 规则后，拔掉你的设备并重新插入。 

之后执行： 
    
    $ adb devices
    
    List of devices attached 
    HT07VHL00676    device
    
如果 _adb_ 在你把设备插回去之后仍然没有检测到设备，请以 root 身份杀死并重新启动 _adb_ 服务，然后再次检查设备。 
    
    # adb kill-server
    # adb start-server
    $ adb devices
    
如果 _adb devices_ 仍然在你连接的设备显示 _未授权_ ，请确保已授予该设备调试权限。当你物理连接到该设备时，应该出现一个 _允许 USB 调试？_ 的对话框。选择 _总是允许..._ ，然后点击 _确定_ 。如果从未出现过该对话框，请尝试点击 _设置_ >_开发人员选项_ >_撤销 USB 调试授权_ ,然后点击 _确定_ ，并重复本节的步骤。如果你仍然没有看到 _允许 USB 调试？_ 对话框，而且设备被列为未授权，那么进入设备的 _开发者选项_ ，首先取消 _USB 调试_ ，然后再次勾选。 

###  传输文件

现在可以使用 adb 在设备和电脑之间传输文件。一般来说，安卓设备的文件在/sdcard/目录下。 

要向设备传输文件，请用： 
    
    $ adb push _what-to-copy_ _where-to-place_
    
要从设备传输文件，请用： 
    
    $ adb pull _what-to-pull_ _where-to-place_
    
也可参见[#用 ADB 构建的工具](<#%E7%94%A8_ADB_%E6%9E%84%E5%BB%BA%E7%9A%84%E5%B7%A5%E5%85%B7>)。 

###  备份和恢复

**注意：** _**adb backup/restore**_ 已被弃用，可能会在未来被移除。

你也可以用 _adb_ 备份和恢复你的设备。此外，不需要 root 就可以完成这个操作。下面的命令会将你的设备备份到单个文件，可用于后续恢复。 

创建备份的命令是： 
    
    $ adb backup -apk -shared -all -f _backupFileName.ab_
    
命令参数列表为： 
    
    adb backup [-f <file>] [-apk|-noapk] [-shared|-noshared] [-all] [-system|nosystem] [<packages...>]
    
然后在设备的显示屏上确认这个操作，并提供一个密码，无论之前是否已经设置备份密码。 

恢复以前备份的命令为： 
    
    $ adb restore _backupFileName.ab_
    
**注意：** 请记住，恢复操作会将你的设备内容替换成备份内容。

##  用 ADB 构建的工具

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 请使用 [Template:App](<../zh-cn/Template:%E5%BA%94%E7%94%A8.html> "Template:App") 格式。（在[Talk:Android 调试桥](<../zh-cn/Talk:Android_%E8%B0%83%E8%AF%95%E6%A1%A5.html>)讨论）

  * [adbfs-rootless-git](<https://aur.archlinux.org/packages/adbfs-rootless-git/>)AUR – 挂载一台通过 USB 连接的 Android 设备。
  * [adb-sync-git](<https://aur.archlinux.org/packages/adb-sync-git/>)AUR – 一个通过 ADB 协议在 PC 和 Android 设备之间同步文件的工具。
  * [androidscreencast-bin](<https://aur.archlinux.org/packages/androidscreencast-bin/>)AUR – 通过 ADB 从 PC 查看和控制你的 Android 设备。
  * [logcat-color](<https://aur.archlinux.org/packages/logcat-color/>)AUR – 一种丰富多彩、高度可配置，可替代标准 `adb logcat` 命令。
  * [scrcpy](<https://archlinux.org/packages/?name=scrcpy>)包 – 显示和控制你的 Android 设备。
  * [qtscrcpy](<https://aur.archlinux.org/packages/qtscrcpy/>)AUR – Android 实时显示控制软件。
  * [adbmanager-bin](<https://aur.archlinux.org/packages/adbmanager-bin/>)AUR \- 该出现设计用于可视化并简化 ADB 服务器管理及 Android 手机连接。它可以让你监控 adb 服务状态，进行管理并控制已连接的设备。它也可以管理你的手机：使用名称搜索已安装的软件包，安装/删除 APK，截屏，重启（正常重启，重启到 Bootloader 或恢复模式）及关机。对于高阶用户，它同时提供了 Android Shell 终端和 SD 卡管理器。

##  故障排除

###  空设备列表

可能的原因有： 

  * 未启用 USB 调试。参见[启用 USB 调试](<#%E8%BF%9E%E6%8E%A5%E8%AE%BE%E5%A4%87>)。
  * USB 线只提供充电功能，没有数据传输功能。

###  无权限错误

如果设备显示“无权限”标签，它可能与 [android-udev](<https://archlinux.org/packages/?name=android-udev>)包 收集的制造商/产品标识符不同。 

例如，当设备使用定制 ROM，或者从 MTP 模式切换到 USB 连接模式、sideload 和/或 fastboot 模式时，就会发生这种情况。 用 [lsusb](<#%E8%AF%86%E5%88%AB%E8%AE%BE%E5%A4%87%E6%A0%87%E8%AF%86%E7%AC%A6>) 验证实际设备标识符，并[#添加 udev 规则](<#%E6%B7%BB%E5%8A%A0_udev_%E8%A7%84%E5%88%99>)。 

###  守护进程出现权限不足报错

如果在运行 _adb_ 时出现以下报错： 
    
    E adb     : usb_libusb.cpp:571 failed to open device: Access denied (insufficient permissions)
    
请检查你是否在 `adbusers` 用户组中。 
