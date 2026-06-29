**翻译状态：**

  * 本文（或部分内容）译自 [IPMI](<https://wiki.archlinux.org/title/IPMI> "arch:IPMI")，最近一次同步于 2022-07-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/IPMI?diff=0&oldid=712119>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/IPMI_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[智能平台管理接口](<https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface> "w:Intelligent Platform Management Interface") (IPMI) 是用于自治计算机子系统的一组计算机接口规范，该子系统提供独立于主机系统的 CPU、固件（BIOS 或 [UEFI](<../zh-cn/UEFI.html> "UEFI")）和操作系统的管理和监视功能。 

Arch Linux 具有以下与 IPMI 相关的软件包： 

  * **freeipmi** — Sensor monitoring, system event monitoring, power control, and serial-over-LAN (SOL).

     <https://www.gnu.org/software/freeipmi/> || [freeipmi](<https://archlinux.org/packages/?name=freeipmi>)包

  * **openipmi** — Full-function IPMI (Intelligent Platform Management Interface) system.

     <http://openipmi.sourceforge.net/> || [openipmi](<https://archlinux.org/packages/?name=openipmi>)包

  * **ipmiutil** — A simple program that lists results from the hardware detection library.

     <https://sourceforge.net/projects/ipmiutil/> || [ipmiutil](<https://aur.archlinux.org/packages/ipmiutil/>)AUR

  * **ipmitool** — Command-line interface to IPMI-enabled devices.

     <https://github.com/ipmitool/ipmitool> || [ipmitool](<https://archlinux.org/packages/?name=ipmitool>)包

  * **ipmiview** — Supermicro IPMI tool.

     <https://www.supermicro.com/products/nfo/ipmi.cfm> || [ipmiview](<https://aur.archlinux.org/packages/ipmiview/>)AUR

##  固件

可以使用 [supermicro-update-manager](<https://aur.archlinux.org/packages/supermicro-update-manager/>)AUR 更新 Supermicro 服务器上的 bmc 固件。 

##  参见

  * [Wikipedia:out-of-band management](<https://en.wikipedia.org/wiki/out-of-band_management> "wikipedia:out-of-band management")
