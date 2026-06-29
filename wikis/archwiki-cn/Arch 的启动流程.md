**翻译状态：**

  * 本文（或部分内容）译自 [Arch boot process](<https://wiki.archlinux.org/title/Arch_boot_process> "arch:Arch boot process")，最近一次同步于 2025-12-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_boot_process?diff=0&oldid=858944>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_boot_process_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [主引导记录](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "主引导记录")
  * [GUID 分区表](<../zh-cn/GUID_%E5%88%86%E5%8C%BA%E8%A1%A8.html> "GUID 分区表")
  * [UEFI](<../zh-cn/UEFI.html> "UEFI")
  * [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")
  * [init](<../zh-cn/Init.html> "Init")
  * [systemd](<../zh-cn/Systemd.html> "Systemd")
  * [fstab](<../zh-cn/Fstab.html> "Fstab")
  * [自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "自动启动")

为了启动 Arch Linux，必须配置一个与 Linux 兼容的[引导加载程序](<#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F>)。引导加载程序负责在初始化启动进程之前，加载好内核和 [initramfs](<#initramfs>)，具体过程因 [BIOS](<https://zh.wikipedia.org/wiki/BIOS> "zhwp:BIOS") 和 [UEFI](<../zh-cn/UEFI.html> "UEFI") 系统而异。 

##  固件类型

[固件](<https://zh.wikipedia.org/wiki/%E5%9B%BA%E4%BB%B6> "zhwp:固件")是开机时最先执行的程序。 

**提示：**

  * 本文时常以 _BIOS_ 和 _UEFI_ 代称 _固件_ 。
  * 勿与 [Linux 固件](<../zh-cn/Linux_%E5%9B%BA%E4%BB%B6.html> "Linux 固件")混淆。

### UEFI

[统一可扩展固件接口](<../zh-cn/UEFI.html> "UEFI")（Unified Extensible Firmware Interface，UEFI）支持读取分区表和文件系统。UEFI 不从[主引导记录（MBR）中启动任何引导代码](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "分区")（无论其是否存在），相反，UEFI 的启动过程依赖[非易失性随机访问存储器（NVRAM）](<https://en.wikipedia.org/wiki/Non-volatile_random-access_memory> "wikipedia:Non-volatile random-access memory")中的引导条目。 

UEFI 规范要求支持 [FAT12、FAT16 和 FAT32](<../zh-cn/FAT.html> "FAT") 文件系统（参见 [UEFI 规范 2.11 版 13.3.1.1 小节](<https://uefi.org/specs/UEFI/2.11/13_Protocols_Media_Access.html#file-system-format-1>)），但每个符合规范的厂商可以选择添加对其它文件系统的支持；比如，苹果的固件支持 [HFS+](<https://zh.wikipedia.org/wiki/HFS%2B> "zhwp:HFS+") 或 [APFS](<https://zh.wikipedia.org/wiki/%E8%8B%B9%E6%9E%9C%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "zhwp:苹果文件系统") 文件系统。UEFI 的一些实现方案还支持光盘的 [ISO 9660](<https://zh.wikipedia.org/wiki/ISO_9660> "zhwp:ISO 9660") 文件系统。 

UEFI 会启动 EFI 应用程序，例如[引导加载程序](<#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F>)、引导管理器和 [UEFI Shell](<../zh-cn/UEFI.html#UEFI_Shell> "UEFI") 等等。这些应用程序通常以文件形式存储在 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")中。厂商可以将其特定文件存储在 EFI 系统分区中的 `/EFI/_vendor_name_` 文件夹下。应用程序可以通过在 NVRAM 中添加引导项或从 UEFI shell 中启动。 

UEFI 规范通过[兼容性支持模块](<https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface#CSM_booting> "wikipedia:Unified Extensible Firmware Interface")（Compatibility Support Module，CSM）来支持传统 [BIOS](<#BIOS>) 引导。如果在 UEFI 中启用了 CSM，UEFI 会为所有驱动器生成 CSM 引导项。如果选择从某一个 CSM 引导项启动，UEFI 的 CSM 会尝试从这个磁盘的 MBR 引导代码启动。 

**注意：** 英特尔正逐渐取消对 CSM 的支持。以后也许不能再依赖此特性。[[1]](<https://www.intel.com/content/dam/support/us/en/documents/intel-nuc/Legacy-BIOS-Boot-Support-Removal-for-Intel-Platforms.pdf>)

### BIOS

[BIOS](<https://zh.wikipedia.org/wiki/BIOS> "zhwp:BIOS")，又称基本输入输出系统（Basic Input-Output System），大多数情况下储存在主板自身的一块闪存内，独立于其它系统存储。其最早是为 [IBM PC](<https://zh.wikipedia.org/wiki/IBM_PC> "zhwp:IBM PC") 开发，用于处理硬件初始化和启动过程。从 2010 年起已逐渐被技术上没有类似限制的 UEFI 替换。 

##  系统初始化

系统上电时，会执行[加电自检](<https://zh.wikipedia.org/wiki/%E5%8A%A0%E7%94%B5%E8%87%AA%E6%A3%80> "zhwp:加电自检")（Power-on self-test，POST）。详细信息可参考 Hugo Landau 的 [Modern CPUs have a backstage cast](<https://www.devever.net/~hl/backstage-cast>) 一文。 

###  在 UEFI 下的情况

  1. 加电自检后，UEFI 初始化引导所需的硬件（硬盘、键盘控制器等等）。
  2. 固件读取 NVRAM 中的引导项，以决定要启动哪一个 EFI 应用程序，以及从哪启动（比如从哪一个硬盘和分区）。 
     * 一个引导项可能对应的只是一块硬盘。在这种情况下，固件会寻找硬盘上的 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")，并尝试在后备引导路径 `\EFI\BOOT\BOOTx64.EFI` 处（在 [IA32（32 位）UEFI](<../zh-cn/UEFI.html#UEFI_%E5%9B%BA%E4%BB%B6%E4%BD%8D%E6%95%B0> "UEFI") 的系统上为 `BOOTIA32.EFI`）查找 EFI 应用程序。这就是UEFI 可引导可移除介质的工作原理。
  3. 固件启动 EFI 应用程序。 
     * 这可以是一个[#引导加载程序](<#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F>)，或者是使用 [EFISTUB](</wzh/index.php?title=EFISTUB&action=edit&redlink=1> "EFISTUB（页面不存在）")（英语：[EFISTUB](<https://wiki.archlinux.org/title/EFISTUB> "en:EFISTUB")） 的 Arch [内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")本体。
     * 还可以是一些其他的 EFI 应用程序，比如 [UEFI shell](<../zh-cn/UEFI.html#UEFI_Shell> "UEFI") 或[引导管理器](<#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F>)（例如 [systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") 或 [rEFInd](<../zh-cn/REFInd.html> "REFInd")）。

如果启用了[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")，启动过程将会通过签名验证 EFI 二进制文件的真实性。 

**注意：** 一些 UEFI 系统只能从后备引导路径启动。

####  多重引导

由于每个操作系统或厂商都可以维护自己在 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")中的文件，同时不影响其他系统，所以 UEFI 的多重引导的原理就是启动不同的、与特定操作系统引导加载程序所对应的 EFI 应用程序。这避免了依赖一个[#引导加载程序](<#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F>)去加载另一个操作系统的[链式加载](<https://en.wikipedia.org/wiki/Chain_loading> "wikipedia:Chain loading")机制。 

另请参阅 [Arch + Windows 双系统](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html> "Arch + Windows 双系统")。 

###  在 BIOS 下的情况

  1. 上电自检后，BIOS 初始化引导所需的硬件（硬盘、键盘控制器等等）。
  2. BIOS 启动在“BIOS 硬盘顺序”中第一块硬盘上的前 440 字节代码（即[主引导记录引导代码区域](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "主引导记录")）。
  3. 引导加载程序在 MBR 引导代码的第一阶段，之后会从下列任意一处启动第二阶段代码（如果有的话）： 
     * MBR 之后的下一个磁盘扇区，即所谓 MBR 后间隙（post-MBR gap，仅在 MBR 分区表上有）。
     * 分区或者无分区磁盘的[卷引导记录](<https://en.wikipedia.org/wiki/Volume_boot_record> "wikipedia:Volume boot record")（Volume Boot Record，VBR）。
     * GRUB 特定 [BIOS 引导分区](<../zh-cn/GRUB.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8_\(GPT\)_%E7%89%B9%E6%AE%8A%E6%93%8D%E4%BD%9C> "GRUB")（仅限 GPT 分区硬盘上的 [GRUB](<../zh-cn/GRUB.html> "GRUB")，用于 GPT 上没有 MBR 后间隙的情况）
  4. 真正的[#引导加载程序](<#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F>)启动。
  5. 随后，引导加载程序通过链式加载或直接加载操作系统内核的方式加载操作系统。

##  引导加载程序

[引导加载程序](<https://zh.wikipedia.org/wiki/%E5%BC%95%E5%AF%BC%E7%A8%8B%E5%BA%8F> "zhwp:引导程序")（boot loader，又称引导加载器、启动加载器或启动引导器）是由计算机[固件](<https://zh.wikipedia.org/wiki/%E5%9B%BA%E4%BB%B6> "zhwp:固件")（[BIOS](<https://zh.wikipedia.org/wiki/BIOS> "zhwp:BIOS") 或 [UEFI](<../zh-cn/UEFI.html> "UEFI")）启动的软件，负责用指定[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")加载[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")和其它外置 [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs") 映像。 

[引导管理器](<https://www.rodsbooks.com/efi-bootloaders/principles.html>)（boot manager，又称启动管理器）让用户使用启动选项菜单或其他方式控制启动过程——也就是说，仅用于运行其他 EFI 应用程序。 

**提示：** 一些程序，例如 [GRUB](<../zh-cn/GRUB.html> "GRUB") 及 [GRUB Legacy](<../zh-cn/GRUB_Legacy.html> "GRUB Legacy") 兼具引导加载程序和引导管理器的功能。

在 UEFI 的情况下，内核本身可以由 UEFI 使用 [EFI boot stub](</wzh/index.php?title=EFI_boot_stub&action=edit&redlink=1> "EFI boot stub（页面不存在）")（英语：[EFI boot stub](<https://wiki.archlinux.org/title/EFI_boot_stub> "en:EFI boot stub")） 直接启动。要在引导前编辑内核参数，可以使用引导管理器或是单独的引导加载程序。 

使用 [32 位 IA32 UEFI](<../zh-cn/UEFI.html#UEFI_%E5%9B%BA%E4%BB%B6%E4%BD%8D%E6%95%B0> "UEFI") 固件的系统需要使用支持混合启动模式的引导加载程序。 

**警告：** 引导加载程序必须能够访问通常位于 `/boot` 目录下的内核和 initramfs 映像才能成功引导 Arch 系统。也就是说，引导加载程序必须解决从块设备、堆叠块设备（LVM、RAID、dm-crypt、LUKS 等）开始，到内核和 initramfs 映像所在文件系统为止的访问。 

因为几乎没有引导加载程序支持堆叠块设备，并且文件系统引入的一些新特性可能尚未有任何引导加载程序支持（例如 [archlinux/packaging/packages/grub#7](<https://gitlab.archlinux.org/archlinux/packaging/packages/grub/-/issues/7>)、[FS#79857](<https://bugs.archlinux.org/task/79857>)、[FS#59047](<https://bugs.archlinux.org/task/59047>)、[FS#58137](<https://bugs.archlinux.org/task/58137>)、[FS#51879](<https://bugs.archlinux.org/task/51879>)、[FS#46856](<https://bugs.archlinux.org/task/46856>)、[FS#38750](<https://bugs.archlinux.org/task/38750>)、[FS#21733](<https://bugs.archlinux.org/task/21733>) 和 [fscrypt](</wzh/index.php?title=Fscrypt&action=edit&redlink=1> "Fscrypt（页面不存在）")（英语：[fscrypt](<https://wiki.archlinux.org/title/fscrypt> "en:fscrypt")） 加密目录），所以用广泛支持的文件系统（例如 [FAT32](<../zh-cn/FAT.html> "FAT32")）单独创建 [/boot 分区](<../zh-cn/%E5%88%86%E5%8C%BA.html#/boot> "分区")通常更可行。 

###  功能比较

**注意：**

  * 由于 GPT 是 UEFI 规范的一部分，因此所有的 UEFI 引导加载程序都支持 GPT 磁盘。在 BIOS 上使用 GPT 磁盘是可行的，可以使用 [Hybrid MBR](<https://www.rodsbooks.com/gdisk/hybrid.html>) 的“混合引导（hybrid booting）”，或者使用新的[纯 GPT](<https://repo.or.cz/syslinux.git/blob/HEAD:/doc/gpt.txt>) 协议。但是这个协议可能在某些 BIOS 实现上会出问题，详情请参考 [Rodsbooks](<https://www.rodsbooks.com/gdisk/bios.html#bios>)。
  * 作为 UEFI 规范的一部分，所有 UEFI 引导加载程序都支持[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")，但有可能会存在一些限制。

名称  | 固件  |  [分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E8%A1%A8> "分区表") | 多重引导  |  [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统") | 注意   
---|---|---|---|---|---  
BIOS |  [UEFI](<../zh-cn/UEFI.html> "UEFI") | [MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "MBR") |  [GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT")  
[Clover](<../zh-cn/Clover.html> "Clover") | 是  | 是  | 否 | 是  | 是  |  [可扩展](<../zh-cn/Clover.html#Supported_file_systems> "Clover")2,5 | 可以在过时 BIOS 系统上模拟 UEFI。   
[EFI boot stub](</wzh/index.php?title=EFI_boot_stub&action=edit&redlink=1> "EFI boot stub（页面不存在）")（英语：[EFI boot stub](<https://wiki.archlinux.org/title/EFI_boot_stub> "en:EFI boot stub")） | –  | 是1 | 是 | 是  | –  | 继承自固件2 | 内核是有效的 EFI 可执行文件，可直接从 UEFI 或其它 UEFI 引导加载器启动。   
[GRUB](<../zh-cn/GRUB.html> "GRUB") | 是  | 是3 | 是 | 是  | 是  |  [内置](<../zh-cn/GRUB.html#%E5%8F%97%E6%94%AF%E6%8C%81%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "GRUB") | 支持 RAID，LUKS（Argon2 PBKDFs 除外）和 LVM（但是不支持精简配置卷）。平台相关限制请参考 [GRUB](<../zh-cn/GRUB.html> "GRUB")。   
[Limine](</wzh/index.php?title=Limine&action=edit&redlink=1> "Limine（页面不存在）") | 是  | 是3 | 是 | 是  | 是  |  [有限](</wzh/index.php?title=Limine&action=edit&redlink=1> "Limine（页面不存在）") |   
[rEFInd](<../zh-cn/REFInd.html> "REFInd") | 否  | 是  | 是 | 是  | 是4 |  [可扩展](<../zh-cn/REFInd.html#Supported_file_systems> "REFInd")2,5 | 支持自动检测内核和参数，无需明确配置，并支持快速启动[[2]](<https://bbs.archlinux.org/viewtopic.php?id=258805>)。   
[Syslinux](<../zh-cn/Syslinux.html> "Syslinux") | 是  |  [部分](<../zh-cn/Syslinux.html#UEFI_Syslinux_%E7%9A%84%E5%B1%80%E9%99%90%E6%80%A7> "Syslinux")1 | 是 | 是  |  [部分](<../zh-cn/Syslinux.html#%E9%93%BE%E5%BC%8F%E5%8A%A0%E8%BD%BD> "Syslinux") |  [有限](<../zh-cn/Syslinux.html#Supported_file_systems> "Syslinux") | 不支持某些文件系统功能。  
只能访问[自身所处](<../zh-cn/Syslinux.html#%E9%93%BE%E5%BC%8F%E5%8A%A0%E8%BD%BD> "Syslinux")的文件系统。   
[systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") | 否  | 是3 | [手动](<https://github.com/systemd/systemd/issues/1125>) | 是  | 是4 |  [可扩展](<../zh-cn/Systemd-boot.html#%E6%94%AF%E6%8C%81%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Systemd-boot")2,5 | 无法从 [ESP](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "ESP") 或扩展引导加载程序分区（XBOOTLDR）以外的分区启动二进制文件。  
支持自动检测放入 `_esp_ /EFI/Linux/` 的[统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像")。   
[统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像") | –  | 是3 | 是 | 是  | –  | 继承自固件2 |  [systemd-stub(7)](<https://man.archlinux.org/man/systemd-stub.7>)、内核、initramfs、内核命令行打包而成的 EFI 可执行文件，可直接从 UEFI 固件或另一个引导加载程序加载。   
[GRUB Legacy](<../zh-cn/GRUB_Legacy.html> "GRUB Legacy") | 是  | 否  | 是 | 否  | 是  |  [有限](<../zh-cn/GRUB_Legacy.html#Supported_file_systems> "GRUB Legacy") |  [停止开发](<https://www.gnu.org/software/grub/grub-legacy.html>)，转为 [GRUB](<../zh-cn/GRUB.html> "GRUB")。   
[LILO](</wzh/index.php?title=LILO&action=edit&redlink=1> "LILO（页面不存在）") | 是  | 否  | 是 |  [部分](<https://salsa.debian.org/joowie-guest/upstream_lilo/-/commit/29a64e6b92cac22d472f4b352de5b1535e4afc5f>) | 是  |  [有限](</wzh/index.php?title=LILO&action=edit&redlink=1> "LILO（页面不存在）") | 因为局限性（如与 Btrfs、GPT 和 RAID 搭配使用时）已[停止开发](<https://web.archive.org/web/20180323163248/http://lilo.alioth.debian.org/>)。   
  
  1. 虽然二进制文件可以被签名用于[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")，但它不会进行后续验证，从而破坏了信任链。
  2. 文件系统支持是从固件继承的。[UEFI 规范要求支持 FAT12，FAT16 和 FAT32 文件系统](<https://uefi.org/specs/UEFI/2.11/13_Protocols_Media_Access.html#file-system-format-1>)，但厂商可选择添加对其他文件系统的支持。比如说，苹果 [Mac](<../zh-cn/Mac.html> "Mac") 中的固件支持 HFS+ 文件系统。如果固件提供在启动时加载 [UEFI 驱动程序](<../zh-cn/UEFI.html#UEFI_%E9%A9%B1%E5%8A%A8> "UEFI")的接口，则可以通过加载文件系统驱动程序（需单独获取）的方式添加对其他文件系统的支持。
  3. 支持混合模式启动，即可以在 [32 位 IA32 UEFI](<../zh-cn/UEFI.html#UEFI_%E5%9B%BA%E4%BB%B6%E4%BD%8D%E6%95%B0> "UEFI") 固件上启动 64 位 x86_64 Linux 内核
  4. 一种[启动管理器](<https://www.rodsbooks.com/efi-bootloaders/principles.html>)。它只能启动其他的 EFI 应用程序，例如，使用 `CONFIG_EFI_STUB=y` 参数编译的 Linux 内核映像和 [Windows Boot Manager](<https://learn.microsoft.com/en-us/windows-hardware/drivers/bringup/boot-and-uefi#understanding-the-windows-boot-manager>) `bootmgfw.efi`。
  5. 支持加载 [UEFI 文件系统驱动](<../zh-cn/UEFI.html#UEFI_%E9%A9%B1%E5%8A%A8> "UEFI")。

另请参见[维基百科：引导加载程序比较](<https://en.wikipedia.org/wiki/Comparison_of_boot_loaders> "wikipedia:Comparison of boot loaders")。 

##  内核

[引导加载器](<#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F>)会启动包含[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")的 [vmlinux 映像](<https://zh.wikipedia.org/wiki/vmlinux> "zhwp:vmlinux")。 

内核是操作系统的核心。它运行于一个叫 _内核空间_ 的底层上，负责机器硬件和应用程序之间的交流。在继续进入用户空间前，内核会首先执行硬件枚举和初始化。具体细节请参考[zhwp:内核](<https://zh.wikipedia.org/wiki/%E5%86%85%E6%A0%B8> "zhwp:内核")和[zhwp:Linux内核](<https://zh.wikipedia.org/wiki/Linux%E5%86%85%E6%A0%B8> "zhwp:Linux内核")。 

## initramfs

_initramfs_ （初始内存文件系统， _**init**_ ial _**RAM**_ _**f**_ ile _**s**_ ystem）映像是一个 [cpio](<https://zh.wikipedia.org/wiki/cpio> "zhwp:cpio") 存档文件，为 _早期用户空间_ （见下文）启动晚期用户空间提供了必要的文件。这包括了所有用于定位，访问和挂载根文件系统的内核模块、用户空间工具、相关库文件、类似 udev 规则的支持文件等。得益于 initramfs 的概念，它可以处理更加复杂的配置场景，例如从外置硬盘启动，堆叠设备（例如逻辑卷，软 RAID，压缩和加密），或是在早期用户空间中运行一个微型 SSH 服务器，以供远程解锁或为根文件系统执行维护任务。 

绝大部分内核模块都将在初始化流程的后期阶段，由 [udev](<../zh-cn/Udev.html> "Udev") 在根切换到根文件系统后加载。 

具体流程如下： 

  1. `/` 下的根文件系统原本是一个空的 [rootfs](<https://docs.kernel.org/filesystems/ramfs-rootfs-initramfs.html>)，它是一个特殊的 tmpfs 或 ramfs 实例。这里就是 initramfs 会解压到的临时根文件系统。
  2. 内核会将其内置 initramfs 解压到临时根文件系统下。Arch Linux [官方支持的内核](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E5%AE%98%E6%96%B9%E6%94%AF%E6%8C%81%E7%9A%84%E5%86%85%E6%A0%B8> "内核")使用空白存档作为内置 initramfs，即构建内核时的默认行为。
  3. 然后，内核会按照[引导加载器](<#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F>)传递的命令行参数指定的顺序解压外置 initramfs 映像，覆盖掉之前内置 initramfs 或其它解压出来的文件。注意，可以将多个 initramfs 映像合并为一个文件，内核会按照文件内的顺序加载映像。 
     * 如果首个 initramfs 映像未经压缩，那么内核会在解包该映像后在 `/kernel/x86/microcode/` 目录查找 CPU [微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "微码")更新，在 `/kernel/firmware/acpi/` 目录查找 ACPI 表更新。
     * 在适用的情况下，在处理完 CPU 微码和 ACPI 表更新后，内核会继续解压剩余的 initramfs 映像。

initramfs 映像是 Arch Linux 推荐的早期用户空间配置方法，并可通过 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")，[dracut](<../zh-cn/Dracut.html> "Dracut") 或 [booster](<../zh-cn/Booster.html> "Booster") 来生成。 

###  不使用 initramfs

从 6.13.8 版本开始，[官方支持的内核](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E5%AE%98%E6%96%B9%E6%94%AF%E6%8C%81%E7%9A%84%E5%86%85%E6%A0%B8> "内核")已内置 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 和 [Ext4](<../zh-cn/Ext4.html> "Ext4") 的驱动[[3]](<https://gitlab.archlinux.org/archlinux/packaging/packages/linux/-/commit/a7e2a17f9c0e55937ea3e18c4d5b905a8e4f8047>)。 

因此内核可以直接使用这些文件系统格式的根分区，然后再加载其它需要的外部模块。但有几点需要注意： 

  * 不能使用 [GPT 分区自动挂载](<../zh-cn/Systemd.html#GPT%E5%88%86%E5%8C%BA%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Systemd")，必须使用 `root` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。
  * 只能使用 `PARTUUID` 和 `PARTLABEL` 作为根分区（`root`）的[块设备持久化名称](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")[[4]](<https://github.com/torvalds/linux/blob/v6.14/block/early-lookup.c#L216-L243>)。
  * `rootflags` 的[挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载")选项比较有限，例如 `noatime` 就无法使用[[5]](<https://bugzilla.kernel.org/show_bug.cgi?id=61601>)。要绕过该问题，可以先以只读进行挂载（`rootflags=ro`），然后使用 [fstab](<../zh-cn/Fstab.html> "Fstab") 进行重新挂载来应用所需的挂载选项。
  * 由于 GPT 分区自动挂载不可用，无需启用 [systemd-gpt-auto-generator(8)](<https://man.archlinux.org/man/systemd-gpt-auto-generator.8>)，启用甚至还会导致问题出现[[6]](<https://github.com/systemd/systemd/issues/16953>)，可以通过 `systemd.gpt_auto=no` 将其禁用。

**注意：** 目前只内置了 SCSI/SATA/AHCI 的模块，其它存储设备（例如 [NVMe](</wzh/index.php?title=NVMe&action=edit&redlink=1> "NVMe（页面不存在）")（英语：[NVMe](<https://wiki.archlinux.org/title/NVMe> "en:NVMe")），[USB](<../zh-cn/USB_%E5%AD%98%E5%82%A8%E8%AE%BE%E5%A4%87.html> "USB 存储设备")，[device mapper](<https://en.wikipedia.org/wiki/Device_mapper> "w:Device mapper") 等）不适用于该节内容。另外，[LVM](<../zh-cn/LVM.html> "LVM") 和加密也必须搭配 initramfs 使用，这两者需要用户空间工具才能正常工作。

另外，[早期微码加载](<../zh-cn/%E5%BE%AE%E7%A0%81.html#%E6%97%A9%E6%9C%9F%E5%8A%A0%E8%BD%BD> "微码")也必须搭配 initramfs 使用，但没必要为其构建完整映像，Arch 可以[将微码放置在单独的 initramfs 文件](<../zh-cn/%E5%BE%AE%E7%A0%81.html#%E5%BE%AE%E7%A0%81%E5%9C%A8%E5%8D%95%E7%8B%AC%E7%9A%84initramfs%E6%96%87%E4%BB%B6%E4%B8%AD> "微码")中，以供单独使用。 

即使没有提供 initramfs 映像，内核仍会包含一个空映像以供启动[[7]](<https://docs.kernel.org/filesystems/ramfs-rootfs-initramfs.html#populating-initramfs>)，以防止根分区[固定](<https://github.com/torvalds/linux/blob/1b907d0507354b74a4f2c286380cd6059af79248/fs/namespace.c#L4222>)出现问题。 

##  早期用户空间

早期用户空间阶段（亦称“initramfs 阶段”）在由 [#initramfs](<#initramfs>) 映像提供文件的 rootfs 中进行，始于内核以 PID 1 执行 `/init`。 

早期用户空间的功能[可以进行配置](<../zh-cn/Mkinitcpio.html#%E5%B8%B8%E7%94%A8%E9%92%A9%E5%AD%90> "Mkinitcpio")，但主要是引导系统到能够访问真正根文件系统的状态，这主要包括： 

  * [systemd-modules-load(8)](<https://man.archlinux.org/man/systemd-modules-load.8>) 加载内核模块（基于 systemd 的 initramfs），例如挂载真正根文件系统所需的任何块设备模块。
  * 构建访问真正根文件系统所需的存储栈（例如通过 [dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt")、[dm-verity](</wzh/index.php?title=Dm-verity&action=edit&redlink=1> "Dm-verity（页面不存在）")（英语：[dm-verity](<https://wiki.archlinux.org/title/dm-verity> "en:dm-verity")）、[mdadm](<../zh-cn/RAID.html> "Mdadm")、[LVM](<../zh-cn/LVM.html> "LVM")、[systemd-repart](</wzh/index.php?title=Systemd-repart&action=edit&redlink=1> "Systemd-repart（页面不存在）")（英语：[systemd-repart](<https://wiki.archlinux.org/title/systemd-repart> "en:systemd-repart")） 等）。 
    * 解密真正根文件系统（若适用）。
  * [udev](<../zh-cn/Udev.html> "Udev") 将[块设备持久化名称](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")解析为实际设备。
  * 加载 DRM 模块（因为默认启用的 [KMS 早启动](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html#KMS_%E6%97%A9%E5%90%AF%E5%8A%A8> "内核级显示模式设置")）。

需要注意的是，早期用户空间不仅仅用于设置真正根文件系统。有些任务只能在挂载真正根文件系统之前执行，例如 [fsck](<../zh-cn/Fsck.html> "Fsck")和从[休眠](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86/%E6%8C%82%E8%B5%B7%E4%B8%8E%E4%BC%91%E7%9C%A0.html#%E4%BC%91%E7%9C%A0> "电源管理/挂起与休眠")中恢复。 

在早期用户空间的最后阶段，真正根文件系统会被挂载到 `/sysroot/`（基于 [systemd](<../zh-cn/Systemd.html> "Systemd") 的 initramfs）或 `/new_root/`（基于 BusyBox 的 initramfs），然后通过 `systemctl switch-root`（基于 systemd 的 initramfs）或 [switch_root(8)](<https://man.archlinux.org/man/switch_root.8>)（基于 BusyBox 的 initramfs）切换到真正根文件系统。最后通过执行真正根文件系统中的 [init](<../zh-cn/Init.html> "Init") 程序启动晚期用户空间。 

##  晚期用户空间

晚期用户空间从 [init](<../zh-cn/Init.html> "Init") 进程开始。Arch 官方支持的 [systemd](<../zh-cn/Systemd.html> "Systemd") 基于单元和服务的概念，但这里描述的功能在很大程度上与其它 init 系统重叠。 

### getty

[init](<../zh-cn/Init.html> "Init") 会为每个[虚拟终端](<https://en.wikipedia.org/wiki/Virtual_console> "wikipedia:Virtual console")（通常有六个）调用一次 [getty](<../zh-cn/Getty.html> "Getty")，它会初始化终端并保护其免受未授权访问。在提供用户名和密码后， _getty_ 会对照 `/etc/passwd` 和 `/etc/shadow` 检查是否正确。如果正确，就接着调用 [login(1)](<https://man.archlinux.org/man/login.1>)。 

#### login

_login_ 会根据 `/etc/passwd` 设置环境变量并启动用户 shell，从而为用户配置一个会话。在成功登录后，启动登录 shell 前， _login_ 程序会显示 [/etc/motd](<https://en.wikipedia.org/wiki/motd_\(Unix\)> "wikipedia:motd \(Unix\)")（ _**m**_ essage _**o**_ f _**t**_ he _**d**_ ay）的内容，你可以用它来显示服务条款以提醒用户你的本地策略，也可以显示其它提示信息。 

#### shell

用户的 [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell") 启动后，在显示命令行提示符前，通常会执行一个运行时配置文件（例如 [bashrc](<../zh-cn/Bash.html#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6> "Bashrc")）。如果用户账户配置为在[登录时自动启动 X](<../zh-cn/%E7%99%BB%E5%BD%95%E6%97%B6%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8_X.html> "登录时自动启动 X")，那么运行时配置文件会调用 [startx](<../zh-cn/Xinit.html> "Startx") 或 [xinit](<../zh-cn/Xinit.html> "Xinit")，具体内容请参考[#图形会话（Xorg）](<#%E5%9B%BE%E5%BD%A2%E4%BC%9A%E8%AF%9D%EF%BC%88Xorg%EF%BC%89>)。 

###  显示管理器

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 该部分只提到 [Xorg](<../zh-cn/Xorg.html> "Xorg")，缺少 [Wayland](<../zh-cn/Wayland.html> "Wayland") 相关内容。 (在 [Talk:Arch 的启动流程](<../zh-cn/Talk:Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html>) 中讨论)

另外，在特定虚拟终端下，[init](<../zh-cn/Init.html> "Init") 可配置为启动[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")，而不是 _getty_ 。要达成该效果，需要手动[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")其 [systemd 服务文件](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")，之后显示管理器就会启动一个图形会话。 

####  图形会话（Xorg）

[xinit](<../zh-cn/Xinit.html> "Xinit") 会调用用户的 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 运行时配置文件，后者一般会启动一个[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")或[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")。如果用户退出了窗口管理器， _xinit_ 、 _startx_ 、shell、login 就会依次中断，返回到 _getty_ 或显示管理器。 

##  参见

  * [Wikipedia:Booting process of Linux](<https://en.wikipedia.org/wiki/Booting_process_of_Linux> "wikipedia:Booting process of Linux")
  * [Inside the Linux boot process](<https://web.archive.org/web/20230313210814/https://developer.ibm.com/articles/l-linuxboot/>)
  * [Rod Smith - Managing EFI Boot Loaders for Linux](<https://www.rodsbooks.com/efi-bootloaders/>)
  * [NeoSmart: The BIOS/MBR Boot Process](<https://neosmart.net/wiki/mbr-boot-process/>)
  * [Lennart Poettering - Linux Boot Partitions and How to Set Them Up](<https://0pointer.net/blog/linux-boot-partitions.html>)
  * [Wikipedia:initramfs](<https://en.wikipedia.org/wiki/initramfs> "wikipedia:initramfs")
  * [Early Userspace in Arch Linux](<https://web.archive.org/web/20150430223035/http://archlinux.me/brain0/2010/02/13/early-userspace-in-arch-linux/>)
  * [Kernel Newbie Corner: initrd and initramfs](<https://www.linux.com/learn/kernel-newbie-corner-initrd-and-initramfs-whats>)
  * [bootup(7)](<https://man.archlinux.org/man/bootup.7>)（主要涉及 systemd 早期用户空间部分）
