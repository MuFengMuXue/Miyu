**翻译状态：**

  * 本文（或部分内容）译自 [CUPS](<https://wiki.archlinux.org/title/CUPS> "arch:CUPS")，最近一次同步于 2025-02-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/CUPS?diff=0&oldid=824488>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/CUPS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [CUPS/共享打印机](</wzh/index.php?title=CUPS/%E5%85%B1%E4%BA%AB%E6%89%93%E5%8D%B0%E6%9C%BA&action=edit&redlink=1> "CUPS/共享打印机（页面不存在）")
  * [CUPS/打印机特定问题](<../zh-cn/CUPS/%E6%89%93%E5%8D%B0%E6%9C%BA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html> "CUPS/打印机特定问题")
  * [CUPS/疑难解答](</wzh/index.php?title=CUPS/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94&action=edit&redlink=1> "CUPS/疑难解答（页面不存在）")
  * [Samba](<../zh-cn/Samba.html> "Samba")
  * [LPRng](</wzh/index.php?title=LPRng&action=edit&redlink=1> "LPRng（页面不存在）")

[CUPS](<https://openprinting.github.io/cups/>) 是 [OpenPrinting](<https://openprinting.github.io/>) 为 Linux® 和其他类 UNIX® 操作系统开发的基于标准的、开源的打印系统。 

Arch Linux 所打包的是 [OpenPrinting CUPS 分支](<https://openprinting.github.io/cups/>)，而非 [Apple CUPS 分支](<https://www.cups.org/>)。 

目前在市场上可以购买到多种打印扫描一体机，关于这些机器的扫描功能的信息，请参阅 [SANE](<../zh-cn/SANE.html> "SANE")。 

##  安装

请先[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [cups](<https://archlinux.org/packages/?name=cups>)包 软件包。 

**注意：** 因为 CUPS 不再推荐使用驱动，转而支持 IPP Everywhere，所以你可能需要安装 [cups-pdf](<https://archlinux.org/packages/?name=cups-pdf>)包 以使打印功能正常工作。未安装此软件包可能会出现类似 _client-error-document-format-not-supported_ 的错误。该软件包是必需的，因为 IPP Everywhere 直接将 PDF 发送给打印机，因此需要 cups-pdf 将您要打印的所有内容先转换为 PDF。

如果想将文件“打印”成一个 PDF 文档，也请安装 [cups-pdf](<https://archlinux.org/packages/?name=cups-pdf>)包 软件包。默认情况下，PDF 文件存储在 `/var/spool/cups-pdf/_username_ /` 目录里。可以在 `/etc/cups/cups-pdf.conf` 配置文件中变更位置。 

然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `cups.service` 服务，或者也可使用[套接字激活](<../zh-cn/Systemd.html#%E6%BF%80%E6%B4%BB%E5%A5%97%E6%8E%A5%E5%AD%97> "套接字激活")方式，使得仅当有程序需要使用服务时才启动 CUPS。 

###  打印工作步骤

要解决一些相关问题，了解 CUPS 的工作原理很重要： 

  1. 当选择“打印”时，应用程序会发送一个 PDF 文件（若应用程序发送的是其他格式则先转换为 PDF）给 CUPS；
  2. 然后，CUPS 查询打印机的 PPD 文件（打印机描述文件），并确定需要使用何种过滤器将 PDF 文件转换为打印机可以理解的语言（如 PJL、PCL、位图或原生 PDF）；
  3. 过滤器将 PDF 文件转换为打印机可以理解的格式；
  4. 然后数据被发送到后端。例如，如果打印机连接到了 USB 端口，则会使用 USB 后端。

##  连接接口

下面列出了适用于各种连接接口的额外打印机检测步骤。 

###  USB 接口

要查看是否检测到 USB 打印机，请确保安装了[usbutils](<https://archlinux.org/packages/?name=usbutils>)包软件包，然后执行以下操作： 
    
    $ lsusb
    
    (...)
    Bus 001 Device 007: ID 03f0:1004 Hewlett-Packard DeskJet 970c/970cse
    
###  并口

要使用并口打印机，需要 `lp`, `parport` 和 `parport_pc` [内核模块](<../zh-cn/Kernel_modules.html> "Kernel modules")。 
    
    # dmesg | grep -i parport
    
     parport0: Printer, Hewlett-Packard HP LaserJet 2100 Series
     lp0: using parport0 (polling)
    
###  网络

####  添加已知位置的打印机

当打印机的地址已知时（例如通过打印机的显示屏或其他网络扫描方法获得），不需要依赖网络上的动态打印机发现（DNS-SD/mDNS）。可以直接添加 CUPS 队列来使用打印机。有关使用 _lpadmin_ 添加队列的文档可以在以下部分和官方文档[设置打印机](<https://github.com/OpenPrinting/cups/?tab=readme-ov-file#setting-up-printers>)中找到。 

####  打印机发现

要使用 DNS-SD/mDNS 查找、使用或共享打印机，请使用 [Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）") 设置 [.local 主机名解析](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）")，然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `cups.service` 服务。 

**注意：** 只有使用 [Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）") 时才支持 DNS-SD。 CUPS 不支持对 DNS-SD 使用 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")，参见 [CUPS issue 5452](<https://github.com/apple/cups/issues/5452>)。但是，您可以使用 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 进行域名解析（与浏览器兼容，不像 [Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）")），并运行 `avahi-daemon.service` 以进行 SD（服务发现）本身。

要用 [Samba](<../zh-cn/Samba.html> "Samba") 共享打印机，例如：如果系统要用作 Windows 客户端的打印服务器，则需要安装 [samba](<https://archlinux.org/packages/?name=samba>)包 软件包。 

##  打印机驱动

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** CUPS 计划放弃对 PPD 和驱动程序的支持（[CUPS issue 103](<https://github.com/OpenPrinting/cups/issues/103>)），转而完全依赖 IPP Everywhere。解释哪些功能将由 [cups](<https://archlinux.org/packages/?name=cups>)包 处理，哪些将由 [cups-filters](<https://archlinux.org/packages/?name=cups-filters>)包 和/或其他软件处理。 (在 [Talk:CUPS#CUPS 打印机驱动和后端已被弃用](</wzh/index.php?title=Talk:CUPS&action=edit&redlink=1> "Talk:CUPS（页面不存在）") 中讨论)

大多数较新的打印机（2010 年以后）通过实现 AirPrint 和/或 IPP Everywhere 支持了无驱动使用（参见下文）。 

打印机的驱动程序可能来自以下任何来源。请参阅 [CUPS/打印机特定问题](<../zh-cn/CUPS/%E6%89%93%E5%8D%B0%E6%9C%BA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html> "CUPS/打印机特定问题")获取其他人设法使用的驱动程序的不完整列表。 

要驱动一台打印机，CUPS 需要一个 PPD 文件，对于大多数打印机来说，还需要一些[过滤器](<https://www.cups.org/doc/man-filter.html>)。有关 CUPS 如何使用 PPD 和过滤器的详细信息，请参阅 [[1]](<https://www.cups.org/doc/postscript-driver.html>)。 

[OpenPrinting 打印机列表 (英语)](<https://www.openprinting.org/printers>) 提供了许多打印机的推荐驱动程序。它还为每台打印机提供了相应的 PPD 文件，但是大多数文件都可以通过 [foomatic](<#Foomatic>) 或其它推荐的驱动程序包获得。 

将 PPD 文件提供给 CUPS 后，CUPS 服务器将重新生成 PPD 文件并将其保存在 `/etc/cups/ppd/` 中。 

要在创建 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 之前测试它们是否正常工作，可以手动将 PPD 文件添加到 `/usr/share/cups/_model_`，驱动程序应在下次重启 cups 服务后可用。 

###  AirPrint 和 IPP Everywhere

CUPS 包括对 [AirPrint](<https://en.wikipedia.org/wiki/AirPrint> "wikipedia:AirPrint") 和 [IPP Everywhere](<https://www.pwg.org/ipp/everywhere.html>) 打印机的支持。如果 `avahi-daemon.service` 正在运行，这些打印机应该会被自动发现，无需额外配置。 

###  OpenPrinting CUPS 过滤器

Linux 基金会旗下的 OpenPrinting 工作组提供了 [cups-filters (CUPS 过滤器)](<https://wiki.linuxfoundation.org/openprinting/cups-filters>)。这里面是一些后端软件、过滤器和其他二进制文件，它们曾经是 CUPS 本体的一部分，但被项目丢弃。这些文件可通过 [cups-filters](<https://archlinux.org/packages/?name=cups-filters>)包 软件包获得，后者是 [cups](<https://archlinux.org/packages/?name=cups>)包 的依赖项之一。 

非 PDF 打印机需要安装 [ghostscript](<https://archlinux.org/packages/?name=ghostscript>)包。对于 PostScript 打印机可能还需要安装 [gsfonts](<https://archlinux.org/packages/?name=gsfonts>)包。 

### Foomatic

Linux 基金会旗下 OpenPrinting 工作组维护的 [foomatic](<https://wiki.linuxfoundation.org/openprinting/database/foomatic>) 为许多打印机提供了 PPD 文件，既有自由的也有非自由的。有关 foomatic 功能的更多信息，请参阅[开发者眼中的 Foomatic (英语)](<https://www.openprinting.org/download/kpfeifle/LinuxKongress2002/Tutorial/IV.Foomatic-Developer/IV.tutorial-handout-foomatic-development.html>)。 

要使用 foomatic，请安装 [foomatic-db-engine](<https://archlinux.org/packages/?name=foomatic-db-engine>)包 和下列的至少一个软件包： 

  * [foomatic-db](<https://archlinux.org/packages/?name=foomatic-db>)包 \- foomatic-db-engine 用来生成 PPD 文件的 XML 文件集合。
  * [foomatic-db-ppds](<https://archlinux.org/packages/?name=foomatic-db-ppds>)包 \- 预构建好的 PPD 文件。
  * [foomatic-db-nonfree](<https://archlinux.org/packages/?name=foomatic-db-nonfree>)包 \- 打印机制造商提供的、非自由许可协议下的、foomatic-db-engine 用于生成 PPD 文件的 XML 文件集合。
  * [foomatic-db-nonfree-ppds](<https://archlinux.org/packages/?name=foomatic-db-nonfree-ppds>)包 \- 非自由许可协议下的预构建 PPD 文件。

Foomatic 的 PPD 文件可能还需要额外的过滤器，比如 [min12xxw](<https://aur.archlinux.org/packages/min12xxw/>)AUR。 

### Gutenprint

[Gutenprint 项目](<https://gimp-print.sourceforge.net/>)提供了可与 CUPS 和 GIMP 搭配使用的佳能(Canon)、爱普生(Epson)、利盟(Lexmark)、索尼(Sony)、奥林巴斯(Olympus)、兄弟(Brother)、惠普(HP)、理光(Ricoh)、PCL 打印机以及一些通用打印机的驱动程序。 

安装 [gutenprint](<https://archlinux.org/packages/?name=gutenprint>)包 和 [foomatic-db-gutenprint-ppds](<https://archlinux.org/packages/?name=foomatic-db-gutenprint-ppds>)包 即可。 

**注意：** 当 Gutenprint 软件包更新时，使用 Gutenprint 驱动的打印机将会停止工作，直到以 root 身份运行 `cups-genppdupdate` 并重新启动 CUPS。 _cups-genppdupdate_ 将会升级已配置打印机的 PPD 文件，参见 [cups-genppdupdate(8)](<https://man.archlinux.org/man/cups-genppdupdate.8>) 获取更多细节。

###  制造商特定的驱动程序

许多打印机厂商提供它们自己的 Linux 驱动。这些驱动通常可以在 Arch 官方仓库和 AUR 里找到。 

其中一些驱动在 [CUPS/打印机特定问题](<../zh-cn/CUPS/%E6%89%93%E5%8D%B0%E6%9C%BA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html> "CUPS/打印机特定问题")一文里有更详细的描述。 

##  打印机 URI

下面列出了一些用于在需要时手动生成 URI 的额外步骤。[CUPS/打印机特定问题](<../zh-cn/CUPS/%E6%89%93%E5%8D%B0%E6%9C%BA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html> "CUPS/打印机特定问题")一文里说明了一些需要特别 URI 的打印机或驱动。 

###  USB 打印机

CUPS 应该能够为 USB 打印机自动生成 URI, 例如 `usb://HP/DESKJET%20940C?serial=CN16E6C364BH`。 

如果没有，请参阅 [CUPS疑难解答#USB 打印机](</wzh/index.php?title=CUPS/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94&action=edit&redlink=1> "CUPS/疑难解答（页面不存在）")进行故障排除。 

###  并口打印机

并口打印机的 URI 格式应为`parallel:_device_`。例如，如果打印机连接在 `/dev/lp0` 上，则 URI 使用 `parallel:/dev/lp0`。如果使用了 USB 转并行端口适配器，请使用 `parallel:/dev/usb/lp0` 作为打印机 URI。 

###  网络打印机

如果已经按照 [#网络共享](<#%E7%BD%91%E7%BB%9C%E5%85%B1%E4%BA%AB>)一节中配置好了 [Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）")，CUPS 应该能检测到打印机 URI。另外还可以使用 `avahi-discover` 查找需要的打印机的名称及其地址（例如 `BRN30055C6B4C7A.local/10.10.0.155:631`）。 

也可以不使用 [Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）") 来手动生成 URI。 [CUPS 文档](<https://www.cups.org/doc/network.html#PROTOCOLS>)里提供了一张网络打印机可用 URI 方案列表。由于不同打印机的 URI 具体细节有所差异，请查看打印机的用户手册或 [CUPS/打印机特定问题](<../zh-cn/CUPS/%E6%89%93%E5%8D%B0%E6%9C%BA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html> "CUPS/打印机特定问题")。 

[smbspool(8)](<https://man.archlinux.org/man/smbspool.8>) 手册页中介绍了 [SMB](</wzh/index.php?title=SMB&action=edit&redlink=1> "SMB（页面不存在）") 共享打印机的 URI。 

**注意：** 打印机 URI 中的任何特殊字符都需要正确地转义引用，否则，如果您的 Windows 打印机名称或用户密码里含有空格，CUPS 会报出 `lpadmin: Bad device-uri` 错误。 

例如， `smb://BEN-DESKTOP/HP Color LaserJet CP1510 series PCL6` 要写成 `smb://BEN-DESKTOP/HP%20Color%20LaserJet%20CP1510%20series%20PCL6`。 

可通过运行以下命令来获取此结果字符串： 
    
    $ python -c 'from urllib.parse import quote; print("smb://" + quote("BEN-DESKTOP/HP Color LaserJet CP1510 series PCL6"))'
    
远程 CUPS 打印服务器可通过 `ipp://_hostname_ :631/printers/_queue_name_` 这样格式的 URI 来访问。关于如何配置远程打印服务器的详细信息，请参阅 [CUPS/共享打印机#共享打印机](</wzh/index.php?title=CUPS/%E5%85%B1%E4%BA%AB%E6%89%93%E5%8D%B0%E6%9C%BA&action=edit&redlink=1> "CUPS/共享打印机（页面不存在）")。 

有关其它问题和相应解决方案，请参阅 [CUPS/疑难解答#Networking issues](</wzh/index.php?title=CUPS/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94&action=edit&redlink=1> "CUPS/疑难解答（页面不存在）")。 

**警告：** 避免使用同一个打印机过滤器配置服务器和客户端——客户端或服务器上的打印队列应为“原始 (raw)”状态。这样可以避免通过过滤器向打印机发送两次打印作业，不然可能导致问题，例如：共享打印机在本地工作，但远程计算机却无法打印 ([[2]](<https://bbs.archlinux.org/viewtopic.php?pid=1589908#p1589908>))。有关将打印队列设置为“原始”的示例，请参见 [#lp*](<#lp*>) 一节。

##  使用方法

可以通过 _lp*_ 和 _cups*_ CLI 工具完全控制 CUPS。 此外，也可以使用 [#网页界面](<#%E7%BD%91%E9%A1%B5%E7%95%8C%E9%9D%A2>)和几种 [#GUI 应用](<#GUI_%E5%BA%94%E7%94%A8>)之一来控制 CUPS。 

  * _队列 (queue)_ 名称是系统上用来标识队列的简短但有描述性的名称。这个名称不应该含有空格或任何特殊字符。比如，对应打印机 HP LaserJet 5P 的打印队列可以命名为“ hpljet5p”。一台物理打印机可以关联多个队列。
  * _位置 (location)_ 用来描述打印机的物理位置（比如说“卧室”或者“厨房”）。这有助于维护多台打印机。
  * _描述 (description)_ 是打印队列的完整描述。一个常见用法是填写打印机的全名（比如说 "HP LaserJet 5P"）。

###  命令行工具

有关命令行工具的更多技巧，请参阅 [CUPS 本地文档](<http://localhost:631/help/options.html>)。 

**注意：** 命令行开关不可聚合使用。

使用 SNMP 查询 URI： 
    
    $ /usr/lib/cups/backend/snmp _ip_address_
    
####  lp*

_lpinfo_`-v` 可以列出已连接打印机的 URI ，加上 `-m` 选项可列出所有系统上安装的驱动型号。 

_lpadmin_ 实用程序加上 `-p _queue_name_`可创建新队列。`-E` 开关与 `-p` 一起使用可启用并接受打印机上的任务。`-v` 指定设备 URI， `-m` 指定型号或要使用的 PPD 文件。 也可使用 `-x` 开关删除打印机（请先阅读[下面一节](<#cups*>)）。 

例子: 
    
    # lpadmin -p HP_DESKJET_940C -E -v "usb://HP/DESKJET%20940C?serial=CN16E6C364BH" -m drv:///HP/hp-deskjet_940c.ppd.gz
    
对于免驱动打印队列（Apple AirPrint 或 IPP Everywhere）： 
    
    # lpadmin -p AirPrint -E -v "ipp://10.0.1.25/ipp/print" -m everywhere  
    
原始队列，不含 PPD 文件或过滤器： 
    
    # lpadmin -p SHARED_PRINTER -m raw   
    
指定一个 PPD 文件而不是型号： 
    
    # lpadmin -p Test_Printer -E -v "ipp://10.0.1.3/ipp/print" -m pxlmono.ppd    
    
**注意：**

  * 指定 PPD 时，请只使用文件名，而不要用完整路径（例如，应该使用 `pxlmono.ppd` 而不是 `/usr/share/ppd/cupsfilters/pxlmono.ppd`）。或者也可通过 `-P` 命令行开关使用完整路径。
  * 到2021年时，许多新款打印机支持免驱打印设置。如上述第二个例子一样指定 `-m everywhere`，即可定义打印机，并通过查询网络上的打印机在 `/etc cups/ppd/` 中生成 _.ppd_ 文件。

_lpq_ 实用程序可查看队列。加上 `-a` 开关可查看所有队列。 

_lprm_ 实用程序可清除队列。加上 `-` 可删除所有项目，而不是像默认情况下只删除最后一项。 

_lpr_ 实用程序可进行打印。使用 `-# _N_` 可打印文件 _N_ 遍，使用 `-p` 开关可加入标头。 

使用 _lpr_ 的测试打印示例： 
    
    $ lpr /usr/share/cups/data/testprint
    $ echo 'Hello, world!' | lpr -p 
    
_lpstat_ 实用程序加上 `-s` 开关可检查状态。 `-p` 开关允许指定检查哪个队列。 

_lpoptions_ 实用程序使用与上述的 _lpadmin_ 相同的 `-p _queue_name_` 开关。加上 `-l` 开关可列出选项。 `-d` 开关可通过参数 `_queue_name_` 设置默认打印机。 `-o` 开关设置选项的值： 
    
    $ lpoptions -p HP_DESKJET_940C -o PageSize=A4
    $ lpoptions -p HP_DESKJET_940C -o cupsIPPSupplies=true -o Duplex=DuplexNoTumble
    
####  cups*

_cupsaccept_ 、 _cupsdisable_ 、 _cupsenable_ 及 _cupsreject_ 工具的作用分别是：设置打印机接受任务、禁用打印机、激活打印机、设置打印机拒绝所有收到的任务。 

以下用法示例会彻底删除一台打印机： 
    
    # cupsreject _queue_name_
    # cupsdisable _queue_name_
    # lpadmin -x _queue_name_
    
#### ink

安装 [ink](<https://aur.archlinux.org/packages/ink/>)AUR 查看墨量。 

**注意：** 参阅[打印机支持列表](<https://libinklevel.sourceforge.net/index.html#supported>)。

将你的用户添加到 `lp` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")，注销然后再登录。 

有关用法的信息，请不带参数运行 `ink`。 

###  网页界面

可以通过 <http://localhost:631/> 上的网页界面完全管理 CUPS 服务器。 

**注意：** 如果使用 HTTPS 连接 CUPS，第一次访问时 _可能_ 要花好长时间才能见到界面出现。这是因为第一次请求会触发 SSL 证书的生成，这会是一项耗时的工作。

要从网页界面执行管理任务，需要验证身份；见 [#权限](<#%E6%9D%83%E9%99%90>)。 

添加队列

转到 **Administration** 页面。 

修改现有队列

转到 **Printers** 页面，然后选择一个队列来修改。 

测试队列

转到 **Printers** 页面，然后选择一个队列。 

###  GUI 应用

如果用户没有足够权限来管理 CUPS，应用启动时会要求输入 root 用户密码。要授予用户管理权而无需 root 用户访问权限，参见 [#配置](<#%E9%85%8D%E7%BD%AE>)小节。 

  * **Deepin Print Manager** — 深度桌面环境的打印机配置界面。

     <https://github.com/linuxdeepin/dde-printer> || [deepin-printer](<https://archlinux.org/packages/?name=deepin-printer>)包

  * **GtkLP** — CUPS 的 GTK 界面。

     <https://gtklp.sirtobi.com/index.shtml> || [gtklp](<https://aur.archlinux.org/packages/gtklp/>)AUR

  * **print-manager** — 管理打印任务和打印机的工具 ([KDE](<../zh-cn/KDE.html> "KDE"))。

     <https://invent.kde.org/plasma/print-manager> || [print-manager](<https://archlinux.org/packages/?name=print-manager>)包

  * **system-config-printer** — GTK 打印机配置工具和状态小程序。

     <https://github.com/OpenPrinting/system-config-printer> || [system-config-printer](<https://archlinux.org/packages/?name=system-config-printer>)包

##  配置

CUPS 服务器配置位于 `/etc/cups/cupsd.conf` 和 `/etc/cups/cups-files.conf` (参见 [cupsd.conf(5)](<https://man.archlinux.org/man/cupsd.conf.5>) 和 [cups-files.conf(5)](<https://man.archlinux.org/man/cups-files.conf.5>))。编辑完上述文件之后，[重启](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd") `cups.service` 以应用所有更改。默认设置对大多数用户已足够。 

###  权限

####  群组

`/etc/cups/cups-files.conf` 文件里的 `SystemGroup` 一处定义了有打印机管理权限的[用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")。默认情况下使用 `sys`、`root` 和 `wheel` 组。 

CUPS 助手程序以 `cups` 用户及组运行。这样助手程序就可以访问打印机设备，并读取由 `cups` 组拥有的 `/etc/cups/` 内的配置文件。 

**注意：**[cups](<https://archlinux.org/packages/?name=cups>)包 2.2.6-2 之前[使用的是lp组](<https://gitlab.archlinux.org/archlinux/packaging/packages/cups/-/commit/b6ebb9850aa9a27c27e668fe066d063a7711c15b>)。在升级之后，`/etc/cups` 中的文件应该由 `cups` 组和 `User 209` 及 `Group 209` 拥有，如 `/etc/cups/cups-files.conf` 中所设置的那样。

###  允许通过 PolicyKit 进行管理员身份验证

可配置 [PolicyKit](</wzh/index.php?title=PolicyKit&action=edit&redlink=1> "PolicyKit（页面不存在）")，允许用户使用一个 GUI 来配置打印机，而无需使用管理员密码。 

**注意：** 你可能需要安装 [cups-pk-helper](<https://archlinux.org/packages/?name=cups-pk-helper>)包 来使这个规则生效。

这是一个允许 wheel [用户组](<../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86> "Users and groups")的成员无需密码即可管理打印机的示例： 
    
    /etc/polkit-1/rules.d/49-allow-passwordless-printer-admin.rules
    
    polkit.addRule(function(action, subject) { 
        if (action.id == "org.opensuse.cupspkhelper.mechanism.all-edit" && 
            subject.isInGroup("wheel")){ 
            return polkit.Result.YES; 
        } 
    });
    
###  默认纸张尺寸

[cups](<https://archlinux.org/packages/?name=cups>)包 构建时开启了 [libpaper](<https://archlinux.org/packages/?name=libpaper>)包 支持并且 libpaper 默认纸张尺寸设为 **Letter** （该选项在 `lpoptions` 中被称为 `PageSize`）。要避免得一个一个更改添加的打印队列的纸张尺寸，请编辑 `/etc/papersize` 并设置系统默认纸张尺寸。参见 [paper(1)](<https://man.archlinux.org/man/paper.1>)。 

###  归档 PDF/A

为了以高度兼容的格式保存 PDF 文件，通常称为归档 PDF，或 PDF/A，或 PDFA，或 ISO 19005。 

目前没有选项，因此必须将其添加到 CUPS 用于调用 _gs_ 的命令中。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** `/etc/cups/cups.conf` 在 [cups](<https://archlinux.org/packages/?name=cups>)包 包中不存在，因此注释中没有带有默认参数的 `GSCall`。（在 [Talk:CUPS](<../zh-cn/Talk:CUPS.html>) 中讨论）

    /etc/cups/cups.conf
    
    # GSCall %s -q -dCompatibilityLevel=%s -dNOPAUSE -dBATCH -dSAFER  -sDEVICE=pdfwrite -sOutputFile="%s" -dAutoRotatePages=/PageByPage -dAutoFilterColorImages=false -dColorImageFilter=/FlateEncode -dPDFSETTINGS=/prepress -c .setpdfwrite -f %s
    			
    # 上面的行显示了 GSCall 值的默认值。在 -dNOPAUSE 之前添加 -dPDFA 并删除注释前缀：（不要从这里复制该行，因为它可能已更改。使用您自己文件中的“默认”值）
    GSCall %s -q -dCompatibilityLevel=%s **-dPDFA** -dNOPAUSE -dBATCH -dSAFER  -sDEVICE=pdfwrite -sOutputFile="%s" -dAutoRotatePages=/PageByPage -dAutoFilterColorImages=false -dColorImageFilter=/FlateEncode -dPDFSETTINGS=/prepress -c .setpdfwrite -f %s

###  日志文件

默认情况下，所有日志都会发送到 `/var/log/cups/` 中的文件里。 

将 `/etc/cups/cups-files.conf` 中的 `AccessLog`、`ErrorLog` 和 `PageLog` 指令的值改为 `syslog`，CUPS 可以把日志记录到 [systemd 日志](<../zh-cn/Systemd/Journal.html> "Systemd/日志")中。有关原始建议更改的信息，请参阅 [Fedora 维基页面 (英文)](<https://fedoraproject.org/wiki/Changes/CupsJournalLogging>) 和 [cupsd.conf 文档](<https://www.cups.org/doc/man-cupsd.conf.html>). 

###  打印服务器和远程管理

参见 [CUPS/共享打印机](</wzh/index.php?title=CUPS/%E5%85%B1%E4%BA%AB%E6%89%93%E5%8D%B0%E6%9C%BA&action=edit&redlink=1> "CUPS/共享打印机（页面不存在）")和 [CUPS/共享打印机#远程管理](</wzh/index.php?title=CUPS/%E5%85%B1%E4%BA%AB%E6%89%93%E5%8D%B0%E6%9C%BA&action=edit&redlink=1> "CUPS/共享打印机（页面不存在）")。 

###  不使用本地 CUPS 服务器

CUPS 可以被配置为直接连接到远程打印机服务器，而不是在本地运行打印服务器。这需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading") [libcups](<https://archlinux.org/packages/?name=libcups>)包 软件包。某些应用程序仍需要依赖 [cups](<https://archlinux.org/packages/?name=cups>)包 软件包进行打印。 

**警告：** 开发人员不建议在没有本地 CUPS 服务器的情况下访问远程打印机。 [[3]](<https://lists.cups.org/pipermail/cups/2015-October/027229.html>)

要使用远程 CUPS 服务器，请将 `CUPS_SERVER` [环境变量](<../zh-cn/Environment_variables.html> "Environment variables")设定为 `printerserver.mydomain:port`。例如，如果你想让单个 [Firefox](<../zh-cn/Firefox.html> "Firefox") 实例使用不同的打印服务器(将 `printserver.mydomain:port` 替换为您的打印服务器名称/端口)： 
    
    $ CUPS_SERVER=printserver.mydomain:port firefox
    
要想永久性应用设置，创建配置文件 `/etc/cups/client.conf` 并向其添加远程 CUPS 服务器的主机名： 
    
    ServerName server
    
也可以指定自定义的端口： 
    
    ServerName server:port
    
详见[[4]](<https://www.cups.org/doc/sharing.html#AUTO_IPP>)。 

##  故障排除

请参阅 [CUPS/疑难解答](</wzh/index.php?title=CUPS/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94&action=edit&redlink=1> "CUPS/疑难解答（页面不存在）")和 [CUPS/打印机特定问题](<../zh-cn/CUPS/%E6%89%93%E5%8D%B0%E6%9C%BA%E7%89%B9%E5%AE%9A%E9%97%AE%E9%A2%98.html> "CUPS/打印机特定问题")。 

##  另请参阅

  * [官方 CUPS 文档](<http://localhost:631/help>), _安装在本地_
  * [Wikipedia:CUPS](<https://en.wikipedia.org/wiki/CUPS> "wikipedia:CUPS")
  * [OpenPrinting 主页](<https://wiki.linuxfoundation.org/openprinting/start>)
  * [OpenSuSE 打印概念指南 - 解释完整的打印工作流程](<https://en.opensuse.org/Concepts_printing>)
  * [OpenSuSE CUPS 简述 - CUPS 快速概览](<https://en.opensuse.org/SDB:CUPS_in_a_Nutshell>)
  * [Gentoo 的打印指南](<https://wiki.gentoo.org/wiki/Printing> "gentoo:Printing")
  * [Debian 的打印门户站 - 详细的技术指南](<https://wiki.debian.org/Printing> "debian:Printing")
  * [Debian 的打印概览 - CUPS 打印系统的基本概述](<https://wiki.debian.org/SystemPrinting> "debian:SystemPrinting")
  * [CUPS printing-architecture 和 printing-users 邮件列表](<https://subspace.kernel.org/lists.linux.dev.html>)
  * [CUPS 邮件列表 (Apple fork)](<https://lists.cups.org/mailman/listinfo/cups>)
  * [CUPS 问题跟踪器](<https://github.com/OpenPrinting/cups/issues>)
  * [CUPS 问题跟踪器 (Apple fork)](<https://github.com/apple/cups/issues>)
