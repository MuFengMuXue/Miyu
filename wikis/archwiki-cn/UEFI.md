**翻译状态：**

  * 本文（或部分内容）译自 [Unified Extensible Firmware Interface](<https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface> "arch:Unified Extensible Firmware Interface")，最近一次同步于 2026-02-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface?diff=0&oldid=862698>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")
  * [GUID 分区表](<../zh-cn/GUID_%E5%88%86%E5%8C%BA%E8%A1%A8.html> "GUID 分区表")
  * [安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")
  * [统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像")

[统一可扩展固件接口](<https://zh.wikipedia.org/wiki/%E7%BB%9F%E4%B8%80%E5%8F%AF%E6%89%A9%E5%B1%95%E5%9B%BA%E4%BB%B6%E6%8E%A5%E5%8F%A3> "zhwp:统一可扩展固件接口")**（Unified Extensible Firmware Interface，简称 UEFI）** 是操作系统和固件之间的接口。UEFI 提供了启动操作系统或运行预启动程序的标准环境。 

UEFI 有别于传统 [BIOS](<https://zh.wikipedia.org/wiki/BIOS> "zhwp:BIOS") 系统所使用的 [MBR 引导代码](<../zh-cn/%E5%88%86%E5%8C%BA.html#MBR%EF%BC%88%E5%BC%95%E5%AF%BC%E4%BB%A3%E7%A0%81%EF%BC%89> "分区")。二者的区别和使用 UEFI 启动的过程见 [Arch 的启动流程](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html> "Arch 的启动流程")。要配置 UEFI 引导加载程序，请参见 [Arch 的启动流程#引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "Arch 的启动流程")。 

**注意：**

  * 主板制造商的早期 UEFI 实现可能相比其 BIOS 版本有着更多的错误。如果遇到无法解决的问题，请考虑对这类系统使用传统 BIOS 引导。
  * 苹果的 UEFI 实现不符标准。除非特别支持，本文内容皆为通用指南，部分可能不适用或与 [Mac](<../zh-cn/Mac.html> "Mac") 上的操作有所不同。

##  UEFI 固件位数

UEFI 下每一个程序，无论它是某个 OS 引导器还是某个内存测试或数据恢复的工具，都要兼容于 EFI 固件位数或体系结构。 

无论是系统引导器还是工具（例如内存测试或数据恢复工具），UEFI 下的所有程序都是 EFI 应用，都需要兼容对应的 UEFI 固件位数或架构。 

当前大部分 x86_64 架构系统（包括较新的苹果 Mac）都使用了 x64（64 位）UEFI 固件。目前已知还在使用 IA32（32 位）UEFI 固件的有 2008 年前生产的苹果 Mac、Intel Atom SoC 设备（截至 2013 年 11 月 2 号）[[1]](<https://web.archive.org/web/20201224150025/https://software.intel.com/content/www/us/en/develop/blogs/why-cheap-systems-run-32-bit-uefi-on-x64-systems.html>)和一些使用 Intel EFI 1.10 固件的 Intel 服务器主板。 

与 x86_64 Linux 和 Windows 系统不同，x64 UEFI 固件不兼容 32 位 EFI 程序，所以必须针对特定固件处理器的位数和架构编译 EFI 应用。 

**注意：** IA32 UEFI 平台上的系统需要使用支持混合引导模式的[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")。

###  检查固件位数

可以在已启动的系统上检查固件位数。 

####  Linux 系统

在运行 Linux 4.0 及以上版本内核的发行版中，可以通过 sysfs 接口查看 UEFI 系统位数。试着运行： 
    
    $ cat /sys/firmware/efi/fw_platform_size
    
如果返回 `64` 则代表 64 位（x64） UEFI 系统，如果返回 `32` 则代表 32 位（IA32） UEFI 系统。如果文件不存在，那么代表并没有[以 UEFI 模式启动](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html#%E9%AA%8C%E8%AF%81%E5%BC%95%E5%AF%BC%E6%A8%A1%E5%BC%8F> "安装指南")。 

####  macOS 系统

2008 年以前的 [Mac](<../zh-cn/Mac.html> "Mac") 大都使用 IA32 EFI 固件，2008 年及以后大都使用 x64 EFI。有能力运行 Mac OS X Snow Leopard 64 位内核的 Mac 使用的都是 x64 EFI 1.x 版的固件。 

在 Mac OS X 的终端输入以下命令可以找出该 Mac 的 EFI 固件架构： 
    
    $ ioreg -l -p IODeviceTree | grep firmware-abi
    
如果命令返回 `EFI32`。则对应的是 IA32（32 位）EFI 固件，返回 `EFI64` 对应的则是 x64 EFI 固件。由于苹果的 EFI 实现不完全符合 UEFI 2.x 标准，因此大部分 Mac 没有 UEFI 2.x 固件。 

####  Windows 系统

64 位的 Windows 系统不支持在 32 位 UEFI 上启动。所以如果你在 UEFI 模式下启动了 32 位 Windows，那么你使用的是 32 位 UEFI。 

可以通过运行 `msinfo32.exe` 来查看固件位数。请看 _系统摘要_ 条目下“系统类型”和“BIOS 模式”对应的值。 

如果是 64 位 UEFI 上的 64 位 Windows，则会显示 `系统类型：基于x64的电脑` 和 `BIOS 模式：UEFI`；如果是 32 位 UEFI 上的 32 位 Windows，则会显示 `系统类型：基于x86的电脑` 和 `BIOS 模式：UEFI`。如果“BIOS 模式”不是 `UEFI`，那么 Windows 并没有用 UEFI 模式启动。 

##  UEFI 变量

UEFI 定义了一些变量，操作系统可以通过它们与固件进行交互。UEFI 引导变量只在早期系统启动时由引导加载程序和操作系统使用。UEFI 运行时变量允许操作系统管理固件的某些设置，例如 UEFI 引导管理器或 UEFI 安全启动协议的密钥等。你可通过下面的命令来获得变量列表： 
    
    $ efivar -l
    
###  Linux 内核中的 UEFI 变量支持

从 3.8 版本开始，Linux 内核通过 **efivarfs** （**EFI** **VAR** iable **F** ile**S** ystem，EFI 变量文件系统）接口（`CONFIG_EFIVAR_FS`），使用 `efivarfs` 内核模块将 UEFI 变量数据挂载到了 `/sys/firmware/efi/efivars` 下，并暴露到用户空间。它不限制单个变量的大小，并支持 UEFI 安全启动变量。 

###  UEFI 变量正常工作的需求

  1. 内核需通过 [EFI boot stub](</wzh/index.php?title=EFI_boot_stub&action=edit&redlink=1> "EFI boot stub（页面不存在）")（可选使用[引导管理器](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导管理器")）或 UEFI [引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")启动，而不是 BIOS/CSM（Compatibility Support Module，兼容性支持模块）或者苹果同为 CSM 的 Boot Camp 启动。
  2. 内核需带有 EFI 运行时服务支持（`CONFIG_EFI=y`，可运行 `zgrep CONFIG_EFI /proc/config.gz` 来检查是否满足）。
  3. **不应** 通过[内核命令行参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")禁用 EFI 运行时服务，即**不应使用** `noefi` 内核参数。
  4. `efivarfs` 文件系统应被挂载在 `/sys/firmware/efi/efivars`，否则参考下文 [#挂载 efivarfs](<#%E6%8C%82%E8%BD%BD_efivarfs>) 部分。
  5. `efivar` 在使用 `-l`/`--list` 选项列出 UEFI 变量时不应出现任何报错。

如果 EFI 变量支持在满足以上条件后仍有问题，尝试以下解决方案： 

  1. 如果在列出 UEFI 变量时出现以下报错：`efivar: error listing variables: Function not implemented`，且系统启动到了[实时内核](</wzh/index.php?title=Realtime_kernel&action=edit&redlink=1> "Realtime kernel（页面不存在）")，尝试添加 `efi=runtime` 到[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")并重启（这类内核默认会禁用 efivarfs）。
  2. 更多排障信息请参考 [#Userspace tools are unable to modify UEFI variable data](<#Userspace_tools_are_unable_to_modify_UEFI_variable_data>)。

####  挂载 efivarfs

如果 `efivarfs` 启动时并没有被 [systemd](<../zh-cn/Systemd.html> "Systemd") 自动挂载在 `/sys/firmware/efi/efivars`，你需要通过手动挂载来把 UEFI 变量暴露给类似 _efibootmgr_ 的[用户空间工具](<#%E7%94%A8%E6%88%B7%E7%A9%BA%E9%97%B4%E5%B7%A5%E5%85%B7>)： 
    
    # mount -t efivarfs efivarfs /sys/firmware/efi/efivars
    
**注意：** 如果适用，以上命令需要在 [chroot](<../zh-cn/Chroot.html> "Chroot") **之外（之前） _和_ 之内**都执行一次。

更多内核文档请参考 [efivarfs.html](<https://docs.kernel.org/filesystems/efivarfs.html>)。 

###  用户空间工具

有多个工具可以读取/修改 UEFI 变量： 

  * **efivar** — 操作 UEFI 变量的库和工具（被 efibootmgr 用到）

     <https://github.com/rhboot/efivar> || [efivar](<https://archlinux.org/packages/?name=efivar>)包

  * **efibootmgr** — 操作 UEFI 固件启动管理器设置的工具

     <https://github.com/rhboot/efibootmgr> || [efibootmgr](<https://archlinux.org/packages/?name=efibootmgr>)包

  1. **uefivars** — 转储 UEFI 变量和 PCI 相关信息（内部使用 efibootmgr 源码）

     <https://github.com/fpmurphy/Various/tree/master/uefivars-2.0> || [uefivars-git](<https://aur.archlinux.org/packages/uefivars-git/>)AUR

  1. **efitools** — 控制 UEFI 安全启动平台的工具

     <https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git> || [efitools](<https://archlinux.org/packages/?name=efitools>)包

  1. **Ubuntu 固件测试套件** — 对 Intel/AMD 主机固件进行检查的测试套件

     <https://wiki.ubuntu.com/FirmwareTestSuite/> || [fwts-git](<https://aur.archlinux.org/packages/fwts-git/>)AUR

  * **QEFI 启动项管理器** — 这是一个基于 Qt 的图形界面应用，用于管理 EFI 启动项和 EFI 系统分区

     <https://github.com/Inokinoki/QEFIEntryManager> || [qefientrymanager](<https://aur.archlinux.org/packages/qefientrymanager/>)AUR

#### efibootmgr

首先需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [efibootmgr](<https://archlinux.org/packages/?name=efibootmgr>)包。 

**注意：**

  * 如果 _efibootmgr_ 完全无效，你可以重启进入 [#UEFI Shell](<#UEFI_Shell>) 使用 `bcfg` 命令来给引导器创建一个启动条目。
  * 如果你不能使用 `efibootmgr`，某些 UEFI 固件允许用户用内建的启动时界面管理启动条目。例如，有些固件带有“Add New Boot Option”选项，能让你选择本地 EFI 系统分区并手动输入 EFI 应用位置（例如 `\EFI\refind\refind_x64.efi`）。
  * 下面的命令用 [rEFInd](<../zh-cn/REFInd.html> "REFInd") 引导器作为例子。

要通过 _efibootmgr_ 添加新的启动参数，需要确认： 

  1. 包含 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")（ESP）的磁盘编号，例如：`/dev/sda`，`/dev/nvme0n1`
  2. ESP 分区在其硬盘上的分区编号，即 `/dev/sda _Y_` 或 `/dev/nvme0n1p _Y_` 中的 `_Y_`。
  3. EFI 程序相对 ESP 根目录的路径

假设要为 `/efi/EFI/refind/refind_x64.efi` 添加启动项，其中 `/efi` 是 ESP 的挂载目录，需要执行： 
    
    $ findmnt /efi
    
    TARGET SOURCE    FSTYPE OPTIONS
    /efi   /dev/sda1 vfat   rw,flush,tz=UTC

在以上示例中，[findmnt(8)](<https://man.archlinux.org/man/findmnt.8>) 指出 `/dev/sda` 上 ESP 分区的编号为 1，EFI 程序相对于 ESP 根的路径是 `/EFI/refind/refind_x64.efi`。因此，需要使用以下命令创建启动项： 
    
    # efibootmgr --create --disk /dev/sda --part 1 --loader '\EFI\refind\refind_x64.efi' --label 'rEFInd Boot Manager' --unicode
    
查看所有启动项和启动顺序： 
    
    # efibootmgr --unicode
    
如需配置启动顺序，使用： 
    
    # efibootmgr --bootorder _XXXX_ ,_XXXX_ --unicode
    
其中 _XXXX_ 是上述 _efibootmgr_ 命令输出显示的数字。 

如需删除不需要的启动项，使用： 
    
    # efibootmgr --delete-bootnum --bootnum _XXXX_ --unicode
    
更多信息请参考 [efibootmgr(8)](<https://man.archlinux.org/man/efibootmgr.8>) 或 [efibootmgr README](<https://raw.githubusercontent.com/rhinstaller/efibootmgr/master/README>)。 

**注意：** UEFI 标准使用反斜杠 `\` 作为路径分隔符，不过 _efibootmgr_ 会自动把 UNIX 的 `/` 路径分隔符转换为 `\`。

###  禁止访问 UEFI 变量

UEFI 变量访问有可能会导致超出系统范围的破坏。有些 UEFI 漏洞（例如 [LogoFAIL](<https://binarly.io/posts/finding_logofail_the_dangers_of_image_parsing_during_system_boot/index.html>)）会让黑客获得系统的完整权限，在有些不完善的 UEFI 实现中甚至能导致硬件故障[[2]](<https://github.com/systemd/systemd/issues/2402#issuecomment-176806817>)。 

因此，鉴于日常使用系统时不会访问 UEFI 变量，可以选择将其禁用，以防止潜在安全漏洞和误操作产生破坏。 

可选方法有： 

  * 使用 [fstab](<../zh-cn/Fstab.html> "Fstab") 以只读模式挂载 `efivars`，例如：
        
        efivarfs /sys/firmware/efi/efivars efivarfs ro,nosuid,nodev,noexec 0 0

  * 使用 `noefi` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")完全禁用系统对 UEFI 的访问

**注意：** 禁用后将无法使用 UEFI [用户空间工具](<#%E7%94%A8%E6%88%B7%E7%A9%BA%E9%97%B4%E5%B7%A5%E5%85%B7>)，因此需要在进行前完成所有必要配置。另外，UEFI 相关命令也将无法使用（例如 `systemctl reboot --firmware-setup`)。

## UEFI Shell

UEFI Shell 是一个用于固件的命令行终端，可用于启动如 UEFI 引导器等 EFI 程序。除此之外，它还可用于采集固件和系统的各种信息，例如内存映射（memmap），修改启动管理器变量（bcfg），运行分区程序（diskpart），加载 UEFI 驱动，编辑文本文件（edit），十六进制编辑等等。 

###  获取 UEFI Shell

可以从 TianoCore EDK2 项目获取到以 BSD 许可证发布的 UEFI Shell： 

你可从 Intel 的 Tianocore UDK/EDK2 Sourceforge.net 工程下载以 BSD 许可证发布的 UEFI Shell. 

  * Shell v2： 
    * 在 Arch 安装媒介上的位置为 `/shellx64.efi`，在构建 ISO 时从 `/usr/share/edk2-shell/x64/Shell_Full.efi` 复制而来。
    * [edk2-shell](<https://archlinux.org/packages/?name=edk2-shell>)包 \- 从 TianoCore EDK2 最新版本编译而来，为 x64（64 位）UEFI 提供了 x64 Shell，以及为 IA32（32 位）UEFI 提供了 IA32 Shell。
    * [uefi-shell-git](<https://aur.archlinux.org/packages/uefi-shell-git/>)AUR \- 从 TianoCore EDK2 最新源码编译而来，为 x64（64 位）UEFI 提供了 x64 Shell，以及为 IA32（32 位）UEFI 提供了 IA32 Shell。
  * Shell v1： 
    * 源自 TianoCore 的[预编译 UEFI Shell v1 二进制文件](<https://github.com/tianocore/edk2/tree/UDK2018/EdkShellBinPkg>)（从 2014 年 1 月 10 号开始上游就不再更新）。
  * 打过补丁的 shells： 
    * 源自 Clover EFI 启动引导器的[预编译 UEFI Shell v2 二进制文件](<https://drive.google.com/uc?export=download&id=1OBXYj6MEs7VAZbYnjD9FxOYcZYIQoq36>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-07-30 ⓘ]，修改了 bcfg 以与 UEFI pre-2.3 固件配合使用。
    * 源自 OpenCore 启动引导器的[预编译 UEFI Shell v2 二进制文件](<https://github.com/acidanthera/OpenCorePkg/releases>)，与大量固件兼容，可从发布包中的 `EFI/OC/Tools/OpenShell.efi` 位置获取。

Shell v2 在 UEFI 2.3+ 系统上表现最好，在这些系统上建议使用 v2 版本。Shell v1 应在所有 UEFI 系统上都可用，与固件遵循的 UEFI 标准无关。更多信息请参考 [ShellPkg](<https://github.com/tianocore/tianocore.github.io/wiki/ShellPkg>) 和 EDK2 邮件清单 - [Inclusion of UEFI shell in Linux distro iso](<https://edk2-devel.narkive.com/zCN4CEnb/inclusion-of-uefi-shell-in-linux-distro-iso>)。 

###  启动 UEFI Shell

从 Sandy Bridge 开始，少数华硕和其它使用 AMI Aptio x64 UEFI 固件的主板提供了一个叫做 _Launch EFI Shell from filesystem device_ 的选项。对于这些主板，需要将 x64 UEFI Shell 复制到 EFI 系统分区的根目录下，并重命名为 `shellx64.efi`。 

**提示：**

  * Arch Linux 安装媒介的根目录包含 `shellx64.efi`。
  * 如果 EFI 系统分区的根目录下存在 `shellx64.efi`，那么 [rEFInd](<../zh-cn/REFInd.html> "REFInd") 和 [systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") 会自动为其添加启动项。

Phoenix SecureCore Tiano UEFI 固件已内嵌 UEFI Shell, 可按 `F6`, `F11` 或 `F12` 键来启动。 

**注意：** 如果你用以上方法不能启动 UEFI Shell，可以创建一个 [FAT32](<../zh-cn/FAT.html> "FAT32") 格式的 U 盘，并把 EFI 二进制文件复制到 `_/U_盘挂载点_ /EFI/BOOT/BOOTx64.EFI`。这个 U 盘将会出现在固件的启动菜单里，启动它就会启动到 UEFI Shell。

###  重要 UEFI Shell 命令

UEFI Shell 命令通常支持 `-b` 选项，它会在输出的每页末尾暂停。运行 `help -b` 可以列出所有可用命令，这些命令都是内置在 shell 或单独的 EFI 应用中。 

详细信息请参考 [Intel 脚本编写指南 2008](<https://software.intel.com/en-us/articles/efi-shells-and-scripting/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-07-30 ⓘ] 和 [Intel“教程”2011](<https://software.intel.com/en-us/articles/uefi-shell>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-07-30 ⓘ]。 

#### bcfg

_bcfg_ 命令用于修改 UEFI NVRAM 条目，它能让用户改变启动条目或驱动器选项，在[UEFI Shell Specification 2.2](<https://uefi.org/sites/default/files/resources/UEFI_Shell_2_2.pdf>) PDF 文档的 96 页(Section 5.3) 有详细说明。 

**注意：**

  * 仅当 _efibootmgr_ 无法创建启动条目时才推荐尝试 _bcfg_ 。
  * UEFI Shell v1 官方二进制文件不支持 `bcfg` 命令，可以参考[#获取 UEFI Shell](<#%E8%8E%B7%E5%8F%96_UEFI_Shell>)下载一个修改过的 UEFI Shell v2 二进制文件，有可能在 UEFI 2.3 版本前的固件上可用。

转储当前启动条目： 
    
    Shell> bcfg boot dump -v
    
以为 rEFInd 为例，将其添加为第 4 个（从 0 开始计数）启动项： 
    
    Shell> bcfg boot add 3 FS0:\EFI\refind\refind_x64.efi "rEFInd Boot Manager"
    
其中 `FS0:` 是 EFI 系统分区映射到的路径，`FS0:\EFI\refind\refind_x64.efi` 是要启动的文件。 

如需添加直接启动到系统而非通过引导加载器的条目，参见 [EFI boot stub#bcfg](</wzh/index.php?title=EFI_boot_stub&action=edit&redlink=1> "EFI boot stub（页面不存在）"). 

删除第 4 个启动选项： 
    
    Shell> bcfg boot rm 3
    
把第 3 个启动选项移动到第 0 个（也就是第 1 个选项，是 UEFI 启动菜单的默认启动选项）： 
    
    Shell> bcfg boot mv 3 0
    
bcfg 帮助信息： 
    
    Shell> help bcfg -v -b
    
或: 
    
    Shell> bcfg -? -v -b
    
#### map

`map` 显示设备的映射列表，即可用的文件系统（`FS0`）和存储设备（`blk0`） 

在执行 `cd` 或 `ls` 等文件系统命令前，你需要输入其名称来进入相应的文件系统。 
    
    Shell> FS0:
    FS0:\> cd EFI/
    
#### edit

`edit` 命令提供了类似于 nano 界面的基本编辑器，但是功能略少一点。它以 UTF-8 编码，并且兼容 LF 和 CRLF 行尾结束符。 

本例中，编辑在固件 EFI 系统分区 (`fs0:` 中 rEFInd 的 `refind.conf`： 
    
    Shell> edit FS0:\EFI\refind\refind.conf
    
按下 `Ctrl+e` 可显示帮助信息。 

##  UEFI 驱动

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 解释 UEFI 驱动是什么及如何使用；添加 efibootmgr 使用 `-r`/`--driver` 选项自动加载 UEFI 驱动的方法 (在 [Talk:UEFI](<https://aw.lilydjwg.me/wiki/Talk:UEFI>) 中讨论)

UEFI 驱动是一些用于提供额外功能的软件。例如，UEFI shell 通常无法访问 NTFS 格式的分区，而 [efifs](<https://archlinux.org/packages/?name=efifs>)包 提供了从 EFI shell 访问多种文件系统读取文件的驱动。其中一种用法是先将驱动复制到 UEFI shell 能访问的分区，然后在 UEFI shell 中执行如下命令： 
    
    Shell> load ntfs_x64.efi
    Shell> map -r
    
执行命令后，用户就可以在 UEFI shell 中访问 NTFS 格式的分区。 

**提示：**

  * [systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") 会自动从 `_esp_ /EFI/systemd/drivers/` 加载 UEFI 驱动。
  * [rEFInd](<../zh-cn/REFInd.html> "REFInd") 会自动从其 ESP 下的安装目录中的 `drivers` 和 `drivers_x64` 子目录加载 UEFI 驱动，例如 `_esp_ /EFI/refind/drivers_x64/`。可以配置扫描更多其它目录。

##  UEFI 可启动介质

###  从光学介质里移除 UEFI 启动支持

**注意：**

  * 本部分内容为从**仅 CD/DVD** （利用 EL Torito 的光学介质启动）介质移除 UEFI 启动支持，而不是 U 盘。
  * 为了隐藏USB启动盘上的 UEFI 设备，在将 ISO 文件复制到闪存驱动器后，使用分区编辑器。删除类型为 `EF` 的分区。**切勿** 接受转换为 GPT 的提示。

大部分 32 位 EFI Mac 和部分 64 位 EFI Mac 无法从 UEFI（X64）+ BIOS 可启动 CD/DVD 启动。如果希望使用光学介质完成安装，可能首先需要移除 UEFI 启动支持。 

提取 ISO 内容，并跳过 UEFI 特定目录： 
    
    $ mkdir extracted_iso
    $ bsdtar -x --exclude=EFI/ --exclude=loader/ -f archlinux-_version_ -x86_64.iso -C extracted_iso
    
确保已经设置了正确的卷标，比如`ARCH_202103`; 可以在原 ISO 中运行 [file(1)](<https://man.archlinux.org/man/file.1>) 获得。然后重新构建 ISO，并使用 [libisoburn](<https://archlinux.org/packages/?name=libisoburn>)包 的 [xorriso(1)](<https://man.archlinux.org/man/xorriso.1>) 移除 UEFI 光学介质启动支持。请确保已设置正确的卷标（例如 `ARCH_202103`），可以对原始 ISO 使用 [file(1)](<https://man.archlinux.org/man/file.1>) 获取： 
    
    $ xorriso -as mkisofs \
        -iso-level 3 \
        -full-iso9660-filenames \
        -joliet \
        -joliet-long \
        -rational-rock \
        -volid "ARCH__YYYYMM_ " \
        -appid "Arch Linux Live/Rescue CD" \
        -publisher "Arch Linux <<https://archlinux.org>>" \
        -preparer "prepared by $USER" \
        -eltorito-boot syslinux/isolinux.bin \
        -eltorito-catalog syslinux/boot.cat \
        -no-emul-boot -boot-load-size 4 -boot-info-table \
        -isohybrid-mbr "extracted_iso/syslinux/isohdpfx.bin" \
        -output archlinux-_version_ -x86_64-noUEFI.iso extracted_iso/

把 `archlinux-_version_ -x86_64-noUEFI.iso` 烧录进光学介质并照常完成安装。 

##  无原生支持情况下测试 UEFI

###  虚拟机使用 OVMF

[OVMF](<https://github.com/tianocore/tianocore.github.io/wiki/OVMF>) 是一个为虚拟机添加 UEFI 支持的 TianoCore 项目。OVMF 包含了一个 UEFI 固件示例，和单独一个用于 [QEMU](<../zh-cn/QEMU.html> "QEMU") 的非易失性变量存储。 

可以从 extra 仓库安装 [edk2-ovmf](<https://archlinux.org/packages/?name=edk2-ovmf>)包。 

[建议](<https://www.linux-kvm.org/downloads/lersek/ovmf-whitepaper-c770f8c.txt>)先将虚拟机的非易失变量存储本地保存一份： 
    
    $ cp /usr/share/edk2/x64/OVMF_VARS.4m.fd my_OVMF_VARS.4m.fd
    
要使用 OVMF 固件和该变量存储，请在 QEMU 命令中添加以下内容： 
    
    -drive if=pflash,format=raw,readonly,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
    -drive if=pflash,format=raw,file=my_OVMF_VARS.4m.fd
    
示例: 
    
    $ qemu-system-x86_64 -enable-kvm -m 1G -drive if=pflash,format=raw,readonly,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd -drive if=pflash,format=raw,file=my_OVMF_VARS.4m.fd …
    
###  仅 BIOS 的系统使用 DUET

DUET 是一个 TianoCore 项目，使得可以从 BIOS 设备连锁启动到完整 UEFI 环境，与 BIOS 操作系统启动类似。该方法在[这里](<https://www.insanelymac.com/forum/topic/186440-linux-and-windows-uefi-boot-using-tianocore-duet-firmware/>)有广泛讨论。预构建的 DUET 可以从[代码库](<https://gitlab.com/tianocore_uefi_duet_builds/tianocore_uefi_duet_installer>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-04-07 ⓘ]下载，使用指南请参考[这里](<https://gitlab.com/tianocore_uefi_duet_builds/tianocore_uefi_duet_installer/blob/master/Migle_BootDuet_INSTALL.txt>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-04-07 ⓘ]。然而，从 2018 年 11 月开始，DUET 代码库已被从 TianoCore git 仓库移除。 

也可考虑 [Clover](<../zh-cn/Clover.html> "Clover")，它提供的 DUET 镜像可能包含了一些系统的专用补丁，并且比 gitlab 源更新得更频繁。 

##  疑难问题

###  困在 Windows 时启动到 Arch Linux

当被困在 Windows 时，要启动到 Arch Linux，可以通过 Windows PowerShell 命令 `shutdown /r /o` 进入 _高级启动_ ，或是通过 _设置 > 更新与安全 > 恢复 > 高级启动_，选择 _现在重启_ 。当你进入 _高级启动_ 菜单时，选择 _使用设备_ （该项中为 UEFI 启动项，包括 U 盘，CD 或硬盘上的操作系统），并选择“Arch Linux”。 

###  无法使用热键进入固件设置

在一些笔记本电脑上，比如联想小新15are 2020，按 F2 或 F12 等按键可能没有任何反应。这种情况有可能通过返厂让OEM修复主板信息来解决，但有时这既不可能也不被希望。不过，还有其他方法可以进入固件设置： 

  * 使用 [systemctl](<../zh-cn/Systemd.html#Power_management> "Systemd"): 
        
        $ systemctl reboot --firmware-setup

这会让电脑重启到固件。
  * 使用 [GRUB](<../zh-cn/GRUB.html> "GRUB"): 按 `c` 进入 GRUB 命令行并输入 `fwsetup`
  * 在 Windows 中进入: 使用 Windows 高级重启，参见 [#Boot back to Arch Linux when stuck with Windows](<#Boot_back_to_Arch_Linux_when_stuck_with_Windows>).

###  用户空间工具无法修改 UEFI 变量

如果任何用户空间工具无法修改 UEFI 变量，检查是否存在 /sys/firmware/efi/efivars/dump-* 文件。如果这些文件存在，删除它们，重启后再尝试。如果上述步骤无法解决问题，尝试使用内核参数 `efi_no_storage_paranoia` 启动系统，以禁用内核对UEFI变量存储空间的检查，这种检查可能会阻止对 UEFI 变量的写入或修改。 

**警告：**`efi_no_storage_paranoia` 应仅在必要时使用，不应作为正常的启动选项保留。该内核命令行参数的作用是关闭一个保护机制，该机制旨在防止当 NVRAM 过满时导致设备变砖。更多信息请参见 [FS#34641](<https://bugs.archlinux.org/task/34641>)。

###  efibootmgr 无法创建启动条目

某些内核与 efibootmgr 版本组合可能会拒绝创建新的启动项。这可能是 NVRAM 空间不足所致。你可以尝试章节 [#Userspace tools are unable to modify UEFI variable data](<#Userspace_tools_are_unable_to_modify_UEFI_variable_data>) 中提供的解决方案。 

你也可以尝试将 efibootmgr [downgrade](<../zh-cn/%E9%99%8D%E7%BA%A7%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "降级软件包") 到版本0.11.0。该版本兼容 Linux 内核 4.0.6。更多信息请参见错误讨论 [FS#34641](<https://bugs.archlinux.org/task/34641>)，尤其是 [closing comment](<https://bugs.archlinux.org/task/34641#comment111365>) 。 

###  Windows 改变了启动次序

如果你使用 [Arch + Windows 双系统](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html> "Arch + Windows 双系统")，且主板直接启动到了 Windows，没有出现 EFI 应用选择菜单，那么有多个可能的原因和解决方案。 

  * 确保 Windows 电源选项中的[“快速启动”](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html#%E5%BF%AB%E9%80%9F%E5%90%AF%E5%8A%A8%E5%92%8C%E4%BC%91%E7%9C%A0> "Arch + Windows 双系统")选项已禁用
  * 如果引导管理器没有签名过，请确保固件中的[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")选项已禁用
  * 确保 Windows Boot Manager 不是 UEFI 启动首项，可以使用 [efibootmgr](<#efibootmgr>) 或查看 UEFI 配置工具中的信息。有些主板会默认覆盖掉 Windows 通过 efibootmgr 做出的任何修改（例如 Packard Bell 笔记本）。
  * 如果你的主板启动到了默认启动路径（`\EFI\BOOT\BOOTx64.EFI`），那么该文件有可能会被 Windows boot loader 覆写。请尝试使用 [efibootmgr](<#efibootmgr>) 配置正确的启动路径。
  * 如果以上步骤无效，还可以直接让 Windows boot loader 运行其它 EFI 应用。进入 Windows 管理员提示符终端，执行 `bcdedit /set "{bootmgr}" path "\EFI\_path_ \_to_ \_app.efi_ "`
  * 或者，以根用户权限执行 `efibootmgr -A -b _bootnumber_`（` _bootnumber_` 为 Windows Boot Manager 的启动编号）禁用 Windows Boot Manager，效果可通过不带参数执行 `efibootmgr` 查看。
  * 或者可以在 Windows 上配置一个启动脚本，在每次启动 Windows 时配置正确的启动顺序： 
    1. 使用管理员权限打开命令提示符终端，执行 `bcdedit /enum firmware` 并找到目标启动项。
    2. 复制启动项的标识符（包括大括号），例如 `{31d0d5f4-22ad-11e5-b30b-806e6f6e6963}`
    3. 创建一个 batch 脚本文件，内容为 `bcdedit /set "{fwbootmgr}" DEFAULT "_{复制来的启动项标识符}_ "`
    4. 打开 _gpedit.msc_ ，进入 _Local Computer Policy > Computer Configuration > Windows Settings > Scripts (Startup/Shutdown)_，选择 _Startup_
    5. 在 _Scripts_ 选项卡下，点击 _Add_ 按钮，选择上面创建的 batch 文件

    注意：[Windows 10 家庭版默认不包含 gpedit.msc，但有非官方方法可以手动进行安装。](<https://answers.microsoft.com/en-us/windows/forum/windows_10-performance/how-to-install-gpeditmsc-in-window-10/f5e9c4fa-8d46-444c-acd7-5cabaea9fc71>)

  * 或者也可以使用 Windows 任务管理器执行启动脚本： 
    1. 参照步骤 1-3 创建 batch 文件
    2. 执行 _taskschd.msc_ ，然后在 _Action_ 菜单中选择 _Create Task..._ 。
    3. 在 _General_ 选项卡中： 

    输入合适的 _Name_ 和 _Description_ 。
    确保选择的管理员账号属于“管理员”，而不是“标准用户”。
    选中 "_Run whether user is logged in or not_ "。
    选中 "_Run with highest privileges_ "。
    4. 在 _Triggers_ 选项卡下，在菜单中选择“ _At startup_ “，然后点击 _OK_ 。
    5. 在 _Actions_ 选项卡下，点击 _New..._ ， _Browse..._ ，然后选择步骤 1 创建的 batch 文件。
    6. 在 _Conditions_ 选项卡下，取消选择 _Power_ 选项，使得在使用电池时（例如笔记本）也会执行该脚本。
    7. 点击 _OK_ ，在出现提示框时输入步骤 4 选择的用户账户的密码。

###  USB 介质卡在黑屏界面

可能是 [KMS](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "KMS") 的问题，从 USB 启动时请尝试[禁用 KMS](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html#%E7%A6%81%E7%94%A8_KMS> "内核级显示模式设置")。 

###  固件中不显示引导加载器

有些固件不支持自定义启动项，它们只会从硬编码的启动项启动。 

一种常见的解决方法是不依赖NVRAM中的启动项，而是将引导加载程序安装到EFI系统分区上的常见回退路径之一。 

以下章节将介绍这些回退路径。 

####  适用于可移除硬盘的默认启动路径

UEFI 标准规定了从可移除媒介启动时的默认 EFI 二进制文件路径： 

  * x64 UEFI 固件 - `_esp_ /EFI/BOOT/BOOTx64.EFI`
  * IA32 UEFI 固件 - `_esp_ /EFI/BOOT/BOOTIA32.EFI`

虽然标准只针对了可移除硬盘，但大多数固件都支持从任意硬盘启动。 

关于如何安装或从引导加载器迁移到默认/后备启动路径的信息，请参考对应的[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")文章。 

#### Microsoft Windows boot loader location

On certain UEFI motherboards like some boards with an Intel Z77 chipset, adding entries with `efibootmgr` or `bcfg` from the UEFI Shell will not work because they do not show up on the boot menu list after being added to NVRAM. 

This issue is caused because the motherboards can only load Microsoft Windows. To solve this you have to place the _.efi_ file in the location that Windows uses. 

Copy the `BOOTx64.EFI` file from the Arch Linux installation medium (`FSO:`) to the Microsoft directory your [ESP](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "ESP") partition on your hard drive (`FS1:`). Do this by booting into EFI shell and typing: 
    
    Shell> mkdir FS1:\EFI\Microsoft
    Shell> mkdir FS1:\EFI\Microsoft\Boot
    Shell> cp FS0:\EFI\BOOT\BOOTx64.EFI FS1:\EFI\Microsoft\Boot\bootmgfw.efi
    
After reboot, any entries added to NVRAM should show up in the boot menu. 

###  UEFI/BIOS is stuck on loading screen

This is a recurring problem with Acer laptops, which occurs if `.efi` files have not been manually authorized. See [Laptop/Acer#Firmware Setup became inaccessible after Linux installation](</wzh/index.php?title=Laptop/Acer&action=edit&redlink=1> "Laptop/Acer（页面不存在）"). 

### Boot entries created with efibootmgr fail to show up in UEFI

_efibootmgr_ can fail to detect EDD 3.0 and as a result create unusable boot entries in NVRAM. See [efibootmgr issue 86](<https://github.com/rhboot/efibootmgr/issues/86>) for the details. 

To work around this, when creating boot entries manually, add the `-e 3` option to the _efibootmgr_ command. E.g. 
    
    # efibootmgr --create --disk /dev/sda --part 1 --loader '\EFI\refind\refind_x64.efi' --label 'rEFInd Boot Manager' --unicode **-e 3**
    
To fix boot loader installers, like `grub-install` and `refind-install`, create a wrapper script `/usr/local/bin/efibootmgr` and make it [executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable"): 
    
    /usr/local/bin/efibootmgr
    
    #!/bin/sh
    
    exec /usr/bin/efibootmgr -e 3 "$@"
    
### UEFI boot entry disappears after removing its referenced drive

Some firmware will remove boot entries referencing drives that are not present during boot. This could be an issue when frequently detaching/attaching drives or when booting from a removable drive. 

The solution is to install the [boot loader](<../zh-cn/Boot_loader.html> "Boot loader") to [the default/fallback boot path](<#Default_boot_path_for_removable_drives>). 

### Boot entries are randomly removed

Some motherboards may remove boot entries due to lack of free space in the NVRAM instead of giving an error at creation. To prevent this from occurring, reduce the amount of boot entries being added by minimizing your entry creation process, as well as reducing the amount of automatic drive boot entries by the [Compatibility Support Module (CSM)](<https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface#CSM_booting> "wikipedia:Unified Extensible Firmware Interface") by disabling it from your UEFI settings. See [BBS#1608838](<https://bbs.archlinux.org/viewtopic.php?pid=1608838#p1608838>). 

Another reason why boot entries might have been removed is the fact that UEFI specification allows OEMs to do "NVRAM maintenance" during boot process. Those manufacturers do it simply: they just look up for EFI applications in predefined, hardcoded paths on the device. If they fail to find any, they conclude there is no operating system on the device and wipe all boot entries from NVRAM associated with it, because they assume the NVRAM contains some corrupted or outdated data. If you do not plan to install Windows and still want to load the Linux kernel directly from the firmware, one possible workaround is to create an empty file `_esp_ /EFI/BOOT/BOOTx64.EFI`: 
    
    # mkdir -p _esp_ /EFI/BOOT 
    # touch _esp_ /EFI/BOOT/BOOTx64.EFI
    
And restore the deleted boot entry. Now after reboot the motherboard will see the "Fake OS" and should not wipe other boot entries from NVRAM. You can change the fake operating system loader with an actual EFI application if you want, of course, as long as you keep the standard fallback name. 

###  Lenovo ThinkPad: boot entries not persistent due to "OS Optimized Defaults"

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[Lenovo](</wzh/index.php?title=Lenovo&action=edit&redlink=1> "Lenovo（页面不存在）")。**

**附注：** Brand-specific issues should be on the dedicated page.（在 [Talk:UEFI](<https://aw.lilydjwg.me/wiki/Talk:UEFI>) 中讨论）

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Missing links to the "user reports". (在 [Talk:UEFI](<https://aw.lilydjwg.me/wiki/Talk:UEFI>) 中讨论)

On recent Lenovo ThinkPad laptops (e.g. T16 Gen 2 AMD models), users report that custom UEFI boot entries (created with `efibootmgr` or `bootctl`) are automatically deleted at each boot, with only Windows Boot Manager and Lenovo’s own entries (PXE, Recovery, Diagnostics) restored. 

This is caused by the BIOS option "Restart / OS Optimized Defaults", which resets the UEFI boot variables at each reboot to defaults optimized for Windows. 

Solution: Disable "OS Optimized Defaults" in the BIOS/UEFI setup. After doing so, manually created boot entries persist correctly, allowing systemd-boot or other custom boot managers to work as intended. 

##  参见

  * [UEFI Forum](<https://www.uefi.org/home/>) \- contains the official [UEFI Specifications](<https://uefi.org/specifications>) \- GUID Partition Table is part of UEFI Specification
  * [UEFI boot: how does that actually work, then? - A blog post by AdamW](<https://web.archive.org/web/20191127011631/https://www.happyassassin.net/2014/01/25/uefi-boot-how-does-that-actually-work-then/>)
  * [Linux Kernel UEFI documentation for x86_64 platforms](<https://docs.kernel.org/arch/x86/x86_64/uefi.html>)
  * [Intel's page on EFI](<https://www.intel.com/content/www/us/en/architecture-and-technology/unified-extensible-firmware-interface/efi-homepage-general-technology.html>)
  * [Intel Architecture Firmware Resource Center](<https://firmware.intel.com/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-07-30 ⓘ]
  * [Matt Fleming - The Linux EFI Boot Stub](<https://web.archive.org/web/20191230095118/https://firmware.intel.com/blog/linux-efi-boot-stub>)
  * [Matt Fleming - Accessing UEFI Variables from Linux](<https://web.archive.org/web/20190319175019/https://firmware.intel.com/blog/accessing-uefi-variables-linux>)
  * [Rod Smith - Linux on UEFI: A Quick Installation Guide](<https://www.rodsbooks.com/linux-uefi/>)
  * [UEFI Boot problems on some newer machines (LKML)](<https://lore.kernel.org/lkml/20110608192950.GA29235@srcf.ucam.org/>)
  * [LPC 2012 Plumbing UEFI into Linux](<https://linuxplumbers.ubicast.tv/videos/plumbing-uefi-into-linux/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ]
  * [LPC 2012 UEFI Tutorial : part 1](<https://linuxplumbers.ubicast.tv/videos/uefi-tutorial-part-1/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ]
  * [LPC 2012 UEFI Tutorial : part 2](<https://linuxplumbers.ubicast.tv/videos/uefi-tutorial-part-2/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ]
  * [Intel's TianoCore Project](<https://www.tianocore.org/>) for Open-Source UEFI firmware which includes DuetPkg for direct BIOS based booting and OvmfPkg used in QEMU and Oracle VirtualBox
  * [FGA: The EFI boot process](<http://jdebp.info/FGA/efi-boot-process.html>)
  * [Microsoft's Windows and GPT FAQ](<https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-and-gpt-faq>)
  * [Convert Windows x64 from BIOS-MBR mode to UEFI-GPT mode without Reinstall](<https://gitlab.com/tianocore_uefi_duet_builds/tianocore_uefi_duet_installer/wikis/Windows_x64_BIOS_to_UEFI>)
  * [Create a Linux BIOS+UEFI and Windows x64 BIOS+UEFI bootable USB drive](<https://gitlab.com/tianocore_uefi_duet_builds/tianocore_uefi_duet_installer/wikis/Linux_Windows_BIOS_UEFI_boot_USB>)
  * [Rod Smith - A BIOS to UEFI Transformation](<https://rodsbooks.com/bios2uefi/>)
  * [EFI Shells and Scripting - Intel Documentation](<https://web.archive.org/web/20190404074007/https://software.intel.com/en-us/articles/efi-shells-and-scripting/>)
  * [UEFI Shell - Intel Documentation](<https://web.archive.org/web/20190117223426/https://software.intel.com/en-us/articles/uefi-shell/>)
  * [UEFI Shell - bcfg command info](<https://web.archive.org/web/20130929114218/http://www.hpuxtips.es/?q=node/293>)
  * [The bootstrap process on EFI systems](<https://lwn.net/Articles/632528/>)
