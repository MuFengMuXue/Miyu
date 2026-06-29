相关文章

  * [SANE/扫描仪特定问题](<../zh-cn/SANE/%E6%89%AB%E6%8F%8F%E4%BB%AA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html> "SANE/扫描仪特定问题")
  * [Scanner Button Daemon](</wzh/index.php?title=Scanner_Button_Daemon&action=edit&redlink=1> "Scanner Button Daemon（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [SANE](<https://wiki.archlinux.org/title/SANE> "arch:SANE")，最近一次同步于 2024-12-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/SANE?diff=0&oldid=823888>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SANE_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[SANE](<http://www.sane-project.org/>) ([Scanner Access Now Easy](<https://en.wikipedia.org/wiki/Scanner_Access_Now_Easy> "wikipedia:Scanner Access Now Easy")) 提供了在 GNU/Linux 下使用扫描仪的库和命令行工具。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sane](<https://archlinux.org/packages/?name=sane>)包 软件包。无论如何，大多数前端和驱动程序都会将其作为依赖项，因此通常无需明确安装。 

###  扫描仪驱动

许多现代扫描仪都支持"无驱动"扫描。[[1]](<https://help.ubuntu.com/community/sane#Installing_Network_Scanners>) 您可以在 [sane-airscan GitHub](<https://github.com/alexpevzner/sane-airscan#compatibility>) 或 [Apple AirPrint devices](<https://support.apple.com/en-us/HT201311#printers>) 上查找设备的兼容性。 

如果扫描仪已知可以在"无驱动"模式下工作，则[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sane-airscan](<https://archlinux.org/packages/?name=sane-airscan>)包软件包。如果扫描仪使用 USB，还需[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ipp-usb](<https://archlinux.org/packages/?name=ipp-usb>)包 软件包并[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `ipp-usb.service` 以便通过 USB 连接使用 IPP 协议。 

否则，请检查 [SANE - 支持的设备](<http://www.sane-project.org/sane-supported-devices.html>)和 [SANE/扫描仪特定问题](<../zh-cn/SANE/%E6%89%AB%E6%8F%8F%E4%BB%AA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html> "SANE/扫描仪特定问题")，查看您的扫描仪是否可以使用不同的驱动程序。 

大多数扫描仪开箱即可使用。如果您的扫描仪不能正常工作，请参阅 [SANE/扫描仪特定问题](<../zh-cn/SANE/%E6%89%AB%E6%8F%8F%E4%BB%AA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html> "SANE/扫描仪特定问题")获取安装说明。 

**注意：** Some drivers, including [sane-airscan](<https://archlinux.org/packages/?name=sane-airscan>)包, use multicast to search for network scanners. See [iptables#Allowing multicast traffic](<../zh-cn/Iptables.html#Allowing_multicast_traffic> "Iptables") to correctly configure your firewall.

###  前端

SANE 有许多前端，不完全列表可在 [SANE 项目网站](<http://www.sane-project.org/sane-frontends.html>)上找到。 

  * **[GNOME Document Scanner](<https://en.wikipedia.org/wiki/Simple_Scan> "wikipedia:Simple Scan")** — 简化的图形用户界面，与 XSane 相比更易于使用，并能更好地集成到 [GNOME](<../zh-cn/GNOME.html> "GNOME") 桌面中。属于 [gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组 的一部分。

     <https://apps.gnome.org/SimpleScan/> || [simple-scan](<https://archlinux.org/packages/?name=simple-scan>)包

  * **[Skanlite](<https://en.wikipedia.org/wiki/Skanlite> "wikipedia:Skanlite")** — 简单的图像扫描应用程序，基于 KSane 后端，只需扫描和保存图像。是 [kde-graphics](<https://archlinux.org/groups/x86_64/kde-graphics/>)包组 的一部分。

     <https://apps.kde.org/skanlite/> || [skanlite](<https://archlinux.org/packages/?name=skanlite>)包

  * **Skanpage** — 一款简单的扫描应用程序，用于多页扫描并保存文档和图像。属于 [kde-utilities](<https://archlinux.org/groups/x86_64/kde-utilities/>)包组 的一部分。

     <https://apps.kde.org/skanpage/> || [skanpage](<https://archlinux.org/packages/?name=skanpage>)包

  * **[XSane](<https://en.wikipedia.org/wiki/Scanner_Access_Now_Easy#XSane> "wikipedia:Scanner Access Now Easy")** — 基于 GTK 的全功能前端，看起来有点老旧，但可提供扩展功能。

     <http://www.xsane.org/> || [xsane](<https://aur.archlinux.org/packages/xsane/>)AUR

  * **Scantailor** — 一款扫描应用程序，可与项目协同工作，并允许在扫描过程中进行实时编辑。

     <https://github.com/4lex4/scantailor-advanced> || [scantailor-advanced](<https://archlinux.org/packages/?name=scantailor-advanced>)包

Some [OCR software](<../zh-cn/List_of_applications/Documents.html#OCR_software> "List of applications/Documents") can scan images using SANE: gImageReader, [gscan2pdf](<https://en.wikipedia.org/wiki/Scanner_Access_Now_Easy#gscan2pdf> "wikipedia:Scanner Access Now Easy"), Linux-Intelligent-Ocr-Solution, [OCRFeeder](<https://en.wikipedia.org/wiki/OCRFeeder> "wikipedia:OCRFeeder"), [Paperwork](<https://openpaper.work>). 

**注意：**

  * 使用 XSane 在 16 位色深模式下直接扫描为 PDF 时，已知会生成 [已损坏文件](<https://bugs.launchpad.net/ubuntu/+source/xsane/+bug/539162>)，`pacman` 输出中的注释对此提出了警告。已知 8 位模式可以正常工作。

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** skanlite does not need to _handle_ mDNS. As long as [mDNS hostname resolution](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）") is set up correctly and the scanner 's address is specified as `_hostname_.local`, it should just work. This looks like a hplip limitation/bug.（在 [Talk:SANE](<../zh-cn/Talk:SANE.html>) 中讨论）

  * Using a frontend does not mean you do not have to apply some tricks. This is especially true with devices configured via [mDNS](</wzh/index.php?title=MDNS&action=edit&redlink=1> "MDNS（页面不存在）"). For example, `skanlite` needs to have additional info specified on the command line in order to detect a network scanner properly as it cannot handle mDNS. Here is an example with an HP Officejet Pro L7590: `skanlite --device "hpaio:/net/Officejet_Pro_L7500?ip=192.168.0.17"`.

## Verification

Now you can try to see if sane recognizes your scanner. 
    
    $ scanimage -L
    
If that fails, run the command again as root to check for permission problems. If that fails as well, check that your scanner is plugged into the computer. You also might have to unplug/plug your scanner for `/usr/lib/udev/rules.d/65-sane.rules` to recognize your scanner. 

Now you can see if it actually works 
    
    $ scanimage --format=png --output-file test.png --progress
    
If the scanning fails with the message `scanimage: sane_start: Invalid argument` you may need to specify the device. 
    
    $ scanimage -L
    
    device `v4l:/dev/video0' is a Noname Video WebCam virtual device
    device `pixma:04A91749_247936' is a CANON Canon PIXMA MG5200 multi-function peripheral
    
Then you would need to run 
    
    $ scanimage --device "pixma:04A91749_247936" --format=tiff --output-file test.tiff --progress
    
Sane provides many special backend options for numerous scanner types. To see what these are for your device: 
    
    $ scanimage -A
    
## Firmware

**注意：** This section is only needed if you need to upload firmware to your scanner.

Firmwares usually have the _.bin_ extension. 

Firstly you need to put the firmware someplace safe, it is recommended to put it in a subdirectory of `/usr/share/sane/`. 

Then you need to tell sane where the firmware is: 

  * Find the name of the backend for your scanner from the [sane supported devices list](<http://www.sane-project.org/sane-supported-devices.html>).
  * Open the file `/etc/sane.d/_backend-name_.conf`.
  * Make sure the firmware entry is uncommented and let the file-path point to where you put the firmware file for your scanner. Be sure that members of the group `scanner` can access the `/etc/sane.d/_backend-name_.conf` file.

If the backend of your scanner is not part of the sane package (such as `hpaio.conf` which is part of [hplip](<https://archlinux.org/packages/?name=hplip>)包), you need to uncomment the relevant entry in `/etc/sane.d/dll.d` or in `/etc/sane.d/dll.conf`. 

## Sharing your scanner over a network

You can share your scanner with other hosts on your network who use _sane_ , _xsane_ or xsane-enabled _GIMP_. To set up the server, first indicate which hosts on your network are allowed access. 

Change the `/etc/sane.d/saned.conf` file to your liking, for example: 
    
    # required
    localhost
    # allow local subnet
    192.168.0.0/24
    
Second, install, start and enable [avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）")-daemon on your server (if it is not already active) so your scanner can be found by multicast. Or, if your scanner is supported by Airscan installing the [sane-airscan](<https://archlinux.org/packages/?name=sane-airscan>)包 package is an alternative. 

If you use [iptables](<../zh-cn/Iptables.html> "Iptables"), [insert](<../zh-cn/Kernel_modules.html> "Kernel modules") the `nf_conntrack_sane` module to let the firewall track `saned` connections. 

Conntrack helper seems to be disabled by default.[[2]](<https://home.regit.org/netfilter-en/secure-use-of-helpers/>) You can activate it with 
    
    # echo 1 > /proc/sys/net/netfilter/nf_conntrack_helper  
    
To configure this permanently, set the `nf_conntrack_helper=1` option for the `nf_conntrack` module, see [Kernel module#Using files in /etc/modprobe.d/](<../zh-cn/Kernel_module.html#Using_files_in_/etc/modprobe.d/> "Kernel module"). 

Now [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `saned.socket`. Your scanner is now available over the network. For more information, see [saned(8)](<https://man.archlinux.org/man/saned.8>). 

**注意：** saned intentionally refuses to share scanners that use the net: backend (which includes some USB scanners). There is a crude patch to allow this in [FS#54786](<https://bugs.archlinux.org/task/54786>), but note it may cause problems on some networks. Check output of `scanimage -L` on the server to see the scanner url.

### Accessing your scanner from a remote workstation

[![](../File:Tango-edit-cut.png)](<../File:Tango-edit-cut.png>)**这一章节正在考虑移除。**

**原因:** Once a local scanner is shared (above), remote workstations should follow the normal instructions (i.e. Installation's [#Scanner_drivers](<#Scanner_drivers>)). Static IPs & avahi-daemon should move to that section. (在 [Talk:SANE](<../zh-cn/Talk:SANE.html>) 讨论)

**注意：** Some network scanners require a different approach. See [SANE/Scanner-specific problems](</wzh/index.php?title=SANE/Scanner-specific_problems&action=edit&redlink=1> "SANE/Scanner-specific problems（页面不存在）").

You can access your network-enabled scanner from a remote Arch Linux workstation. 

First, specify the server's host name or IP address in the `/etc/sane.d/net.conf` file: 
    
    # static IP address
    192.168.0.1
    # or host name
    stratus
    
Second, depending on what you configured at the server side, install, start and enable avahi-daemon or install sane-airscan at the remote workstation. 

Now test your workstation's connection: 
    
    $ scanimage -L
    
The network scanner should now also show up in some [front-end](<#Frontends>)s. 

### Windows clients

Since the Windows port of SANE seems to be [unsupported, outdated and difficult to get](<https://web.archive.org/web/20151207111023/http://www.xsane.org/xsane-download.html>), you can try [SANEWinDS](<https://sourceforge.net/projects/sanewinds/>) or [SaneTwain](<https://sanetwain.ozuzo.net/>) (old). 

##  疑难解答

另请参阅 [SANE/扫描仪特定问题](<../zh-cn/SANE/%E6%89%AB%E6%8F%8F%E4%BB%AA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html> "SANE/扫描仪特定问题")。 

###  参数无效

如果在使用 xsane 或其他 sane 前端时出现"Invalid argument"错误，可能是由以下原因造成的： 

####  固件文件缺失

未提供所用扫描仪的固件文件（详情请参见 [#固件](<#%E5%9B%BA%E4%BB%B6>)。） 

####  固件文件权限错误

所用固件文件的权限有误。用以下方法更正： 
    
    # chown root:scanner /usr/share/sane/_SCANNER_MODEL_ /_FIRMWARE_FILE_
    # chmod ug+r /usr/share/sane/_SCANNER_MODEL_ /_FIRMWARE_FILE_
    
#### Multiple backends claim scanner

可能会出现这样的情况：多个后端都支持（或假装支持）您的扫描仪，而 sane 却选择了一个最终不支持的后端（此时 `scanimage -L` 将无法显示扫描仪）。老式爱普生扫描仪和 `epson2` 以及 `epson` 后端就会出现这种情况。在这种情况下，解决办法是在 `/etc/sane.d/dll.conf` 中注释掉不需要的后端。在爱普生案例中，就是注释掉 epson2： 
    
    /etc/sane.d/dll.conf
    
    #epson2
    epson
    
也有可能是独立的 [iscan](<https://aur.archlinux.org/packages/iscan/>)AUR `epkowa` 后端与 `snapscan` 后端（爱普生扫描仪）相互干扰。使用 `scanimage -L` 命令后，可能会立即出现此错误。启动扫描仪应用程序（如 [xsane](<https://aur.archlinux.org/packages/xsane/>)AUR）两次也能解决问题。否则，请检查 `/etc/sane.d/epkowa.conf` 是否存在错误配置，或删除 [iscan](<https://aur.archlinux.org/packages/iscan/>)AUR 软件包。 

####  Communication via xHCI not working (older scanner models)

Some older scanner models do not work when connected via an USB3 port. If you experience this issue, try setting the `SANE_USB_WORKAROUND=1` [environment variable](<../zh-cn/Environment_variable.html> "Environment variable") before starting your frontend.[[3]](<https://lists.alioth.debian.org/pipermail/sane-announce/2017/000036.html>)[[4]](<https://salsa.debian.org/debian/sane-backends/-/blob/master/ChangeLog#L2251-2262>)

If that does not work, try one of the following workarounds: 

  * Use an USB2 port instead of an USB3 port, if available.
  * Disable xHCI via BIOS/EFI. eHCI will consequently be used and communication with the scanner will work. On the downside, USB3 speed can not be reached on any port.
  * On (some) intel chipsets the `setpci` command can be used to route specific usb ports to either the xHCI or the eHCI controller. See [force-a-single-usb-3-0-port-to-work-as-usb-2-0](<https://superuser.com/questions/812022/force-a-single-usb-3-0-port-to-work-as-usb-2-0>) (scroll down to where it says "setpci") for further information. With this it is possible to toggle single USB ports with a simple shell script.
  * Connect the scanner over the network instead if it is supported.

####  防火墙

当网络扫描扫描仪挂起时，会出现无效参数错误。 

saned 使用数据端口范围，因此必须在 `/etc/sane.d/saned.conf` 中启用与 6566/tcp 和 data_portrange 的连接，或如上所述使用 sane 的 conntrack 防火墙模块启用数据端口。 

###  启动缓慢

如果遇到启动缓慢的问题（例如，`xsane` 或 `scanimage -L` 无法立即返回结果），可能是其中一个未使用的驱动程序造成的。 

您可以通过编辑 `/etc/sane.d/dll.conf` 并注释掉不使用的扫描仪驱动程序来解决这一问题。您可以使用 `scanimage -L` 来确定需要哪些驱动程序： 
    
    $ scanimage -L
    
    device `brother4:net1;dev0' is a Brother DCP-L2550DW
    device `v4l:/dev/video0' is a Noname Logitech Webcam C925e virtual device
    device `escl:http://192.168.1.2:80' is a Brother DCP-L2550DW series adf,platen scanner
    
输出中 ``` 和 `:`} 之间的部分表示设备的驱动程序。例如，如果只想使用 Brother 扫描仪，而不想使用 [webcam](</wzh/index.php?title=Webcam&action=edit&redlink=1> "Webcam（页面不存在）") 或通用扫描仪驱动程序，则可以在 `/etc/sane.d/dll.conf` 中注释掉除 `brother4` 驱动程序之外的所有内容。 

###  设备忙

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 用户不需要在扫描仪组中（请参阅[用户和用户组#预 systemd 组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E9%A2%84_systemd_%E7%BB%84> "用户和用户组")）。（在 [Talk:SANE](<../zh-cn/Talk:SANE.html>) 中讨论）

If your USB device is listed with `scanimage -L` but launching the test `scanimage pixma:04A9173E_11DAD1 --format=tiff --output-file test.tiff` always return the 'Device busy' error, you might try to add your username to the scanner group `usermod -a -G scanner yourusername` then blacklist the `usblp` kernel module by writing `blacklist usblp` in `/etc/modprobe.d/no-usblp.conf` (it prevents `usblp` from loading to support scanning, not needed by xsane and related tools, might also [conflict with CUPS](</wzh/index.php?title=CUPS/Troubleshooting&action=edit&redlink=1> "CUPS/Troubleshooting（页面不存在）")). Reboot to finish. [[5]](<https://cromwell-intl.com/linux/canon-pixma-printer-scanner.html>)

In addition to this, some Cannon printers return "device busy" if the scan mode is set to "Computer". Setting this to the "Remote Scanner" mode should fix the issue.[[6]](<https://alioth-lists.debian.net/pipermail/sane-devel/2014-March/032169.html>)

###  权限问题

在 systemd 中，`scanner` 和 `lp` 组已被弃用。无需将用户添加到这些组中。详见[用户和用户组#systemd 之前的群组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#systemd_%E4%B9%8B%E5%89%8D%E7%9A%84%E7%BE%A4%E7%BB%84> "用户和用户组")。 

你也可以尝试更改 USB 设备的权限，但不建议这样做，更好的办法是修复 [Udev 规则](<../zh-cn/Udev_%E8%A7%84%E5%88%99.html> "Udev 规则")，使扫描仪能够被识别。 

首先使用 `lsusb` 检查已连接的 USB 设备： 
    
    Bus 006 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 003 Device 003: ID 04d9:1603 Holtek Semiconductor, Inc.
    Bus 003 Device 002: ID 04fc:0538 Sunplus Technology Co., Ltd
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 001 Device 006: ID 03f0:2504 Hewlett-Packard
    Bus 001 Device 002: ID 046d:0802 Logitech, Inc. Webcam C200
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    
In our example we see the scanner: `Bus 001 Device 006: ID 03f0:2504 Hewlett-Packard`. Here `03f0` is the _vendorID_ and `2504` is the _productID_. 

Alternatively, running `sane-find-scanner` with root permission will also give you the same _vendorID_ and _productID_. 

Now open `/usr/lib/udev/rules.d/65-sane.rules` and see if there is there is a line with the _vendorID_ and _productID_ of your scanner. If there is not any, create the new file `/etc/udev/rules.d/65-sane-missing-scanner.rules`, with the following contents: 
    
    ATTRS{idVendor}=="**vendorID** ", ATTRS{idProduct}=="**productID** ", MODE="0664", GROUP="lp", ENV{libsane_matched}="yes"
    
保存文件，拔出并重新插入扫描仪，此时文件权限应该正确无误。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 扫描仪需要添加到正确的后端文件中，`hp4200.conf` 不适用于任何扫描仪。（在 [Talk:SANE](<../zh-cn/Talk:SANE.html>) 中讨论）

另一个小窍门是可以在后台文件中添加设备（扫描仪）： 

在 `/etc/sane.d/hp4200.conf` 中添加 `usb 0x03f0 0x2504` ，使其看起来像这样： 
    
    #
    # Configuration file for the hp4200 backend
    #
    #
    # HP4200
    #usb 0x03f0 0x0105
    usb 0x03f0 0x2504
    
#### Parallel port scanners

All devices attached to a parallel port are assumed to be printers, and are given a `lp` group. Either create a [udev](<../zh-cn/Udev.html> "Udev") rule to mark the relevant parallel port as `libsane_matched`, or add your user to the `lp` [user group](<../zh-cn/User_group.html> "User group"). CUPS also uses the `lp` group for read-only access to configuration files, so there are potential security implications to adding users to the `lp` group - see [CUPS#Connection interfaces](<../zh-cn/CUPS.html#Connection_interfaces> "CUPS") for more information. 

### avahi-daemon is not mandatory

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 这是配置，不是疑难解答。（在[Talk:SANE](<../zh-cn/Talk:SANE.html>)讨论）

Some scanner applications may require you to start the _avahi-daemon_ upon startup. This is actually the cause of SANE. If for some reason you do not want to enable the _avahi-daemon_ service because you use a wired scanner or do not need it because your scanner's driver supports networking already on setup, then comment out the `net` backend in the SANE configuration: 
    
    /etc/sane.d/dll.conf
    
    # The next line enables the network backend; comment it out if you do not
    # need to use a remote SANE scanner over the network -- see sane-net(5)
    # and saned(8) for details.
    #net
    
然后重启 `saned` 守护进程。 

###  设备输入/输出时出错

如果您在尝试使用惠普扫描仪扫描时收到 `SANE: Error during device I/O (code=9)`，请确保您安装了 [hplip-plugin](<https://aur.archlinux.org/packages/hplip-plugin/>)AUR （请参阅 [CUPS/打印机特定问题#HP](<../zh-cn/CUPS/%E6%89%93%E5%8D%B0%E6%9C%BA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html#HP> "CUPS/打印机特定问题")）。 

## See also

  * [Wikipedia:WS-Discovery](<https://en.wikipedia.org/wiki/WS-Discovery> "wikipedia:WS-Discovery"), Microsoft's "driverless" protocol
