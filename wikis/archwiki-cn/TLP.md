**翻译状态：**

  * 本文（或部分内容）译自 [TLP](<https://wiki.archlinux.org/title/TLP> "arch:TLP")，最近一次同步于 2024-06-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/TLP?diff=0&oldid=778524>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/TLP_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Laptop](<../zh-cn/%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91.html> "Laptop")
  * [Laptop Mode Tools](<../zh-cn/Laptop_Mode_Tools.html> "Laptop Mode Tools")

来自[项目主页](<https://linrunner.de/en/tlp/tlp.html>): 

    TLP 是 Linux 系统上一个功能丰富的命令行工具，能够在不需要深入了解技术细节的情况下**节省笔记本电脑电池电量** 。

    TLP 的默认设置已经针对电池寿命进行了**优化** ，并且开箱即用就实现了 Powertop 的建议。所以你只需要**安装并忘记** 它。

    尽管如此，TLP 仍然是**高度可定制的** ，以满足你的特定需求。

TLP [故意排除](<https://linrunner.de/tlp/faq/misc.html>)了一些设置，特别是[风扇转速控制](<../zh-cn/%E9%A3%8E%E6%89%87%E8%BD%AC%E9%80%9F%E6%8E%A7%E5%88%B6.html> "风扇转速控制")和[背光](<../zh-cn/%E8%83%8C%E5%85%89.html> "背光")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [tlp](<https://archlinux.org/packages/?name=tlp>)包。安装可选依赖项可能有助于提供额外的节能效果。 

[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `tlp.service`。 

还应该[屏蔽](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")服务 `systemd-rfkill.service` 和套接字 `systemd-rfkill.socket`，以避免冲突并确保 TLP 的无线电设备切换选项正常工作。 

###  无线设备向导（tlp-rdw）

当使用无线电设备向导（[tlp-rdw](<https://archlinux.org/packages/?name=tlp-rdw>)包）时，需要使用 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `NetworkManager-dispatcher.service`。 

详情请参阅 [TLP 设置](<https://linrunner.de/tlp/settings/rdw.html>)。 

###  图形界面

  * [tlpui](<https://aur.archlinux.org/packages/tlpui/>)AUR 是用 Python 编写的 TLP 的 [GTK](<../zh-cn/GTK.html> "GTK") 用户界面。
  * [slimbookbattery](<https://aur.archlinux.org/packages/slimbookbattery/>)AUR 是另一种与 AMD 和 NVIDIA 等附加驱动程序兼容的 GTK 界面。

###  对于 ThinkPads

使用 [threshy](<https://aur.archlinux.org/packages/threshy/>)AUR 及其示例 Qt 用户界面 [threshy-gui](<https://aur.archlinux.org/packages/threshy-gui/>)AUR，可以在没有 root 权限的情况下通过 D-Bus 控制充电阈值。 

####  对于 Sandy Bridge 之前的型号（2010 年及以前）

对于 2010 年及以前 ThinkPad 型号，需要 [tp_smapi](</wzh/index.php?title=Tp_smapi&action=edit&redlink=1> "Tp smapi（页面不存在）")（英语：[tp_smapi](<https://wiki.archlinux.org/title/tp_smapi> "en:tp smapi")） 内核模块。请参阅 [tp_smapi#安装](</wzh/index.php?title=Tp_smapi&action=edit&redlink=1> "Tp smapi（页面不存在）")（英语：[tp_smapi#Installation](<https://wiki.archlinux.org/title/tp_smapi#Installation> "en:tp smapi")）获取特定内核的安装说明。 

##  配置

配置文件位于 `/etc/tlp.conf`，并且默认情况下提供了大部分优化的节能功能。要获取选项的完整解释，请参阅：[TLP 设置](<https://linrunner.de/tlp/settings/>)。 

###  禁用 USB 自动挂起

使用默认配置启动 TLP 时，一些 USB 设备（如音频 DAC）在运行电池时将由于 TLP 的自动挂起功能而被**关闭电源** 。一些设备如键盘和扫描仪默认被排除在自动挂起之外。 

您可能只想通过以下设置完全禁用 USB 自动挂起： 
    
    /etc/tlp.conf
    
    # 不挂起 USB 设备
    USB_AUTOSUSPEND=0

或者将特定设备列入黑名单以避免自动挂起。详情请查看 [TLP 关于 USB 设备的文档](<https://linrunner.de/tlp/settings/usb.html>)。 

###  强制使用电池（BAT）配置

当无法检测到电源时，像台式机和嵌入式硬件这样的设备将使用 AC 设置。 

您可能希望在使用 TLP 时强制使用电池（BAT）设置，以启用更多的节能措施： 
    
    /etc/tlp.conf
    
    # 当无法检测到电源时的操作模式：AC 或 BAT。
    TLP_DEFAULT_MODE=BAT
    
    # 操作模式选择：0=依赖电源，1=始终使用 TLP_DEFAULT_MODE
    TLP_PERSISTENT_DEFAULT=1

###  Bumblebee 与 NVIDIA 驱动

如果您正在运行 [Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee") 并使用 NVIDIA 驱动，您需要在 TLP 中禁用 GPU 的电源管理，以便让 Bumblebee 控制 GPU 的电源。 

根据您的驱动使用情况，将一个或多个驱动列入黑名单，防止 TLP 管理它们的电源状态： 
    
    /etc/tlp.conf
    
    RUNTIME_PM_DRIVER_DENYLIST="nouveau nvidia"

###  命令行

TLP 提供多个命令行工具。详情访问 [TLP commands](<https://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html#commands>)。 

##  问题解决

对于调试，您可以显示有关当前使用的模式（AC/BAT）和应用的配置的信息： 
    
    # tlp-stat
    
另请参阅[上游故障排除指南](<https://linrunner.de/tlp/support/troubleshooting.html>)。 

### hci0: link tx timeout

如果您的蓝牙耳机突然停止工作，并且您从 [dmesg](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "Dmesg") 看到这个错误，这可能是由于 TLP 挂起了您的设备。在 `/etc/tlp.conf` 中的 `USB_BLACKLIST` 添加设备 ID： 
    
    # 禁用蓝牙自动挂起
    USB_DENYLIST="8087:0aaa"
    
从 `lsusb -v` 获取您蓝牙设备的设备 ID。重启 TLP 和 `bluetooth` 服务。 

##  参见

  * [TLP - Linux Advanced Power Management](<https://linrunner.de/tlp>) \- 项目主页及文档。
  * [Project FAQ](<https://linrunner.de/tlp/faq/>)
