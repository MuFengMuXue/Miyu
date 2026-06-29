**翻译状态：**

  * 本文（或部分内容）译自 [Dual boot with Windows](<https://wiki.archlinux.org/title/Dual_boot_with_Windows> "arch:Dual boot with Windows")，最近一次同步于 2025-01-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dual_boot_with_Windows?diff=0&oldid=813745>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dual_boot_with_Windows_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

##  重要信息

###  Windows 在 UEFI 和 BIOS 上的限制

不同版本的 Windows 对固件启动模式和分区表有不同的需求。以下依版本列出。 

**注意：** 下列情形是 [Windows安装程序](<https://en.wikipedia.org/wiki/Windows_Setup> "wikipedia:Windows Setup") 的限制。但 Windows 本身仍可能在 Windows安装程序 不支持的情况下正常运行。例如，在绕过相关安装检测后，Windows 11 仍可在 BIOS/MBR 的配置上运行。

  * **Windows 8/8.1** 和 **10** 的 **x86 32位** 版本只支持从 GPT 磁盘启动IA32 UEFI模式，或者从 MBR 磁盘启动 BIOS 模式。它们不支持从 GPT/MBR 磁盘启动 x86_64 UEFI，从MBR 磁盘启动 x86_64 UEFI，或者从 GPT 磁盘启动 BIOS。目前市面上，唯一已知装载 IA32 (U)EFI 的系统是一些较老的 Intel Mac（2010年前的型号？）以及 Intel Atom 系统级芯片（Clover Trail 和 Bay Trail）的Windows平板电脑，这些设备只支持在IA32 UEFI模式下并且只从 GPT 磁盘启动。
  * **Windows 8/8.1** 和 **10** 的 **x86_64** 版本只支持从 GPT 磁盘启动 x86_64 UEFI 模式，或者从 MBR 磁盘启动 BIOS 模式。它们不支持IA32 UEFI启动，从 MBR 磁盘启动 x86_64 UEFI，或者从 GPT 磁盘启动 BIOS。
  * **Windows 11** 只支持 **x86_64** 并从 GPT 磁盘以 UEFI 模式启动。

对于预装系统的计算机： 

  * 所有预装 Windows XP、Vista 或 7 32位的系统，无论服务包级别、位宽度、版本（SKU），或固件中是否支持UEFI，都默认以 BIOS/MBR 模式启动。
  * 大部分预装 Windows 7 x86_64的系统，无论服务包级别、位宽度还是版本（SKU），默认均以 BIOS/MBR 模式启动。极少数较新的预装 Windows 7 的系统默认以 x86_64 UEFI/GPT 模式启动。
  * 所有预装 Windows 8/8.1、10 和 11 的系统都默认以 UEFI/GPT 模式启动。在 Windows 10 之前，固件位宽与 Windows 位宽匹配，即 x86_64 Windows 在 x86_64 UEFI 模式下启动，32位 Windows 在IA32 UEFI模式下启动。

判断 Windows 启动模式的简单方式[[1]](<https://www.eightforums.com/tutorials/29504-bios-mode-see-if-windows-boot-uefi-legacy-mode.html>)： 

  * 启动到Windows
  * 按`Win+R`打开“运行”
  * 在“运行”对话框中输入`msinfo32`并回车
  * 系统信息->系统摘要->BIOS模式 
    * 如果值为 `UEFI`，Windows 以 UEFI/GPT 模式启动。如果值为 `Legacy`，Windows 以 BIOS/MBR 模式启动。

通常，Windows 安装程序基于固件模式强制选择磁盘分区类型：UEFI 启动只能装到 GPT 盘，BIOS 启动只能装到 MBR 盘。这是Windows安装程序强加的限制，截至2014年4月，没有官方（Microsoft）支持的 在UEFI/MBR或BIOS/GPT配置中安装Windows 的方法。因此，Windows只支持UEFI/GPT启动或BIOS/MBR配置。 

**提示：** Windows 10的1703版本及以后的版本支持使用[MBR2GPT.EXE](<https://docs.microsoft.com/en-us/windows/deployment/mbr-to-gpt>)从BIOS/MBR转换为UEFI/GPT。

Linux 内核没有这样的限制，但可能取决于使用的[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")以及/或者 其配置。如果用户希望从同一磁盘启动Windows和Linux，那么应该考虑Windows的这个限制，因为boot loader的安装过程取决于固件类型和磁盘[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")配置。建议遵循Windows使用的方法，即选择UEFI/GPT启动或BIOS/MBR启动。请参见<https://support.microsoft.com/kb/2581408>获取更多信息。 

###  UEFI 和 BIOS 引导加载程序的限制

大多数某类（UEFI 或 BIOS 之一）固件上的 Linux 引导加载程序，不能启动或链式加载另一种固件上的引导加载程序。例如，如果 Arch 以 UEFI 模式安装在一块硬盘下、Windows 以 BIOS 模式安装在另一块硬盘下，Arch 的 UEFI 引导加载程序不能链式加载 Windows 的 BIOS 引导加载程序。这与分区表类型无关。反之亦然。 

有几个例外： 

  * 装在苹果电脑上的 [GRUB](<../zh-cn/GRUB.html> "GRUB")。这里，UEFI 模式的 GRUB 可以用`appleloader`命令启动 BIOS 模式安装的操作系统（在非苹果电脑上无效）。
  * [rEFInd](<../zh-cn/REFInd.html> "REFInd") 理论上也支持从 UEFI 固件启动 BIOS 操作系统，但作者称在非苹果电脑上不总是正常工作。
  * 一块硬盘上的 BIOS/GPT Arch 所使用的引导加载程序可以启动另一块硬盘上的 BIOS/MBR Windows，如果该引导加载程序本身支持链式加载其他硬盘的系统。

**注意：** 如果要在同一硬盘上与Windows双启动，Arch应该遵循与Windows安装相同的固件引导模式和分区组合。

[Windows 安装程序](<https://en.wikipedia.org/wiki/Windows_Setup> "w:Windows Setup")会创建一个100 MiB的[EFI系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")（对于[先进格式化](<../zh-cn/%E5%85%88%E8%BF%9B%E6%A0%BC%E5%BC%8F%E5%8C%96.html> "先进格式化") 4K本地驱动器，它会创建一个300 MiB的ESP），因此多[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")使用受到限制。解决方法包括： 

  * 将ESP挂载到`/efi`，并使用具有文件系统驱动程序的[boot loader](<../zh-cn/Boot_loader.html> "Boot loader")，它能够启动位于其他分区的内核。
  * 减小 Windows 分区的大小，并[替换现有的 ESP 为一个新的、更大的分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html#%E6%9B%BF%E6%8D%A2%E4%B8%BA%E6%9B%B4%E5%A4%A7%E7%9A%84%E5%88%86%E5%8C%BA> "EFI 系统分区")。
  * 备份并删除`esp/EFI/Microsoft/Boot/Fonts/`中不需要的字体 [[2]](<https://support.microsoft.com/en-us/help/3086249/we-couldn-t-update-system-reserved-partition-error-installing-windows>)。
  * 在` _esp_ /EFI/Microsoft/Boot/`中备份和删除不必要的语言目录（例如，仅保留`en-US`）。
  * 使用更高但更慢的[initramfs 压缩方式](<../zh-cn/Mkinitcpio.html#COMPRESSION> "Mkinitcpio")，并确保解压缩可加载的内核模块和固件。例如：

    COMPRESSION="xz"
    COMPRESSION_OPTIONS=(-9e)
    MODULES_DECOMPRESS="yes"
    
###  UEFI 安全启动

一切预装的 Windows 8/8.1/10/11 系统都默认使用 UEFI/GPT 方式启动且默认启用 UEFI 安全启动 (Secure Boot)。对于所有 OEM 预装系统 Microsoft 都强制要求这么做。 

目前 Arch Linux 的安装媒介尚不支持安全启动。参见 [UEFI/安全启动#引导安装介质](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html#%E5%BC%95%E5%AF%BC%E5%AE%89%E8%A3%85%E4%BB%8B%E8%B4%A8> "UEFI/安全启动")。 

目前建议的做法是，在试图启动 Arch Linux 之前在固件设置中手动禁用 UEFI 安全启动。这样，Windows 8/8.1/10/11 **应该** 也还能正常启动。然而， Microsoft 已经明确禁止在预装的Windows 8/8.1及以上系统中以远程或编程的方式（从操作系统内部）禁用安全启动，因此，这种做法的唯一问题是需要操作者能够亲自坐在目标电脑前并直接访问该电脑。。 

**注意：**

  * 如果使用 BitLocker 加密 Windows 且将密钥保存在 TPM 内以便启动时自动解锁，则一旦禁用安全启动，Windows 将无法启动，并显示 BitLocker 恢复屏幕。虽然如此，该问题并不永久，只要再次启用安全启动即可再次启动 Windows。亦可在禁用加密后安装 Arch Linux。
  * 如果使用的是 Windows 11，在安装后禁用安全启动不会导致问题，只要TPM正常工作即可。

**警告：**

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：**

安全启动的更改不应影响 BitLocker：问题可能是自签名 Windows 引导加载程序并从引导加载程序链式加载它：只要 Windows 引导加载程序保持使用 MS 密钥签名，并且 Microsoft 证书已注册，它应该没问题。 问题是禁用它并启动 Windows，还是禁用、重新启用它然后启动 Windows？ 第一个是可以理解的，第二个是需要警告的。 

（在 [Talk:Arch + Windows 双系统](<../zh-cn/Talk:Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html>) 中讨论）

如果您打算也为 Linux 使用安全启动，您可能需要对安全启动设置进行更改。这些更改会阻止在没有恢复密钥的情况下解锁 BitLocker 磁盘，导致**永久数据丢失** 。在继续之前，请检查是否是这种情况，如果尚未完成，请[备份您的 BitLocker 恢复密钥](<https://support.microsoft.com/en-us/windows/back-up-your-bitlocker-recovery-key-e63607b4-77fb-4ad3-8022-d6dc428fbd0d>)。如果 Windows 是由供应商预装的，这一点尤其重要。 

###  快速启动和休眠

两个系统都可以休眠，既可以休眠 Windows 而启动 Linux （或者另一个 OS），又可以休眠 Linux 而启动 Windows，或者同时休眠两个系统。 

**警告：** 如果在 Windows 休眠时使用双启动进入另一 OS 并在二者皆可读/写的（如 NTFS）且已经被 Windows 挂载的某个文件系统上做出更改，有可能发生数据损失。（参见[[3]](<https://superuser.com/questions/39532/hibernating-and-booting-into-another-os-will-my-filesystems-be-corrupted/136814#136814>)。）同样，如果 Linux 休眠而启动另一个 OS，也可能出现数据损失，如此之类。在选择关闭 Windows 时，Windows 也有可能实际上在休眠而不是在关机。参见[#Windows 设置](<#Windows_%E8%AE%BE%E7%BD%AE>)。

同样的原因，如果 Windows 和 Linux 使用同一个 EFI 系统分区，如果休眠（或在启用快速启动时关机）Windows 并启动 Linux，或者休眠 Linux 并启动 Windows， EFI 系统分区可能遭到破坏。 

[ntfs-3g](<https://archlinux.org/packages/?name=ntfs-3g>)包 加入了一种[保护机制](<https://sourceforge.net/p/ntfs-3g/ntfs-3g/ci/559270a8f67c77a7ce51246c23d2b2837bcff0c9/>)以阻止以读/写方式挂载已休眠的 NTFS 文件系统，但是 Linux 内核中的 NTFS 驱动并没有该机制。 

一般情况下，Windows 是无法读取像目前广泛用于 Linux 的 ext4 之类的文件系统的。除非你为这些 Windows 所不支持的文件系统安装 Windows 驱动，否则这些文件系统可以忽略。 

####  Windows 设置

快速启动在 Windows 8 引入，其在关机时会休眠而非真正意义上关闭 Windows 以加快启动速度。 

在之后的章节中会谈到关于快速启动和休眠的 Windows 设置项。 

  * 关闭快速启动并关闭休眠
  * 关闭快速启动并启用休眠
  * 启用快速启动并启用休眠

禁用快速启动的方法：[Windows 8](<https://www.eightforums.com/tutorials/6320-fast-startup-turn-off-windows-8-a.html>)，[Windows 10](<https://www.tenforums.com/tutorials/4189-turn-off-fast-startup-windows-10-a.html>), [Windows 11](<https://www.elevenforum.com/t/turn-on-or-off-fast-startup-in-windows-11.1212/>)。无论如何，如果你要禁用某项设置，请确保在禁用该设置之后关闭 Windows，再安装 Linux；请注意不应只是重启。 

#####  关闭快速启动并关闭休眠

这是最安全的方法，并且如果对该问题不确定，那么推荐使用该方法。因为该方法在重启进入另一 OS 时对用户感知要求并不高。这时可以让 Windows 和 Linux 共享 EFI 系统分区。 

可在具有管理员权限的 Windows 命令行 shell 中用下面的指令代替鼠标操作： 
    
    > powercfg /H off
    
#####  关闭快速启动并启用休眠

该方法在重启进入另一 OS 时要求用户感知。如果你想在 Windows 休眠时启动 Linux（这种情况很常见）那么： 

  * 必须为 Windows 和 Linux 使用不同的 EFI 系统分区 (ESP)，并确保 Windows 在休眠前没有挂载 Linux 的 ESP。由于**每个硬盘只能有一个 ESP** ，Linux 的 ESP 所处的盘必须与 Windows 的不同。即使在这种情况下， 如果你将Linux使用的ESP放在与Linux根分区不同的硬盘上，Windows 和 Linux 仍然可以安装在同一硬盘的不同分区中。
  * 不能在 Linux 下以 读/写方式 挂载任何在 Windows 休眠时已经由 Windows 挂载的任何文件系统。必须非常小心对待此事，对此还应考虑[Automount](</wzh/index.php?title=Automount&action=edit&redlink=1> "Automount（页面不存在）")行为。
  * 如果完全关闭 Windows 而非将其休眠，那么这些文件系统可以读/写挂载。

**注意：** 在 Windows 中将某盘挂载为可移动磁盘并在休眠前将其弹出可以为该盘避免此问题。

#####  启用快速启动并启用休眠

此情况下，应该考虑与“关闭快速启动并启用休眠”时同样的情况。但是由于此时无法将 Windows 完全关闭，而只能将其休眠，在 Windows 休眠时由 Windows 挂载的分区将永远不能读/写挂载。 

**注意：** Windows Update 更新可能导致快速启动被重新启用。见[[4]](<https://tedstechshack.com/2017/07/03/warning-multi-booting-uefi-system-windows-10-fast-startup-doubt-reboot/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ]

###  Windows 文件名限制

Windows 限制文件路径小于[260 个字符](<https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file#maximum-path-length-limitation>)。 

由于一些可以追溯到 DOS 的原因，Windows 同时禁止文件名中出现[某些字符](<https://msdn.microsoft.com/en-us/library/aa365247\(VS.85\).aspx#naming_conventions>)： 

  * `<` (小于号)
  * `>` (大于号)
  * `:` (半角冒号)
  * `"` (半角双引号)
  * `/` (反斜杠)
  * `\` (斜杠)
  * `|` (竖杠)
  * `?` (半角问号)
  * `*` (星号)

这属于 Windows 而非 NTFS 本身的限制——任何使用 NTFS 分区的其它 OS 都不受影响。Windows 将无法检测到这些文件，并且运行 `chkdsk` 很可能会使它们被删除，造成数据丢失的风险。 

如果使用`windows_names`选项，[NTFS-3G](<../zh-cn/NTFS-3G.html> "NTFS-3G")将会把和 Windows 一样的限制应用于新文件的名字上：[ntfs-3g(8) § Windows_Filename_Compatibility](<https://man.archlinux.org/man/ntfs-3g.8#Windows_Filename_Compatibility>)。（见[fstab](<../zh-cn/Fstab.html> "Fstab")） 

##  安装

设置 Linux/Windows 双启动的推荐方式是，先安装 Windows， 但是只为其分区划一部分硬盘空间。在 Windows 设置完毕后，启动 Linux 的安装环境以便为 Linux 创建分区并调整分区大小，但 Windows 分区保持原样。Windows 的安装已经创建了一个能够用于你的 Linux [启动引导程序](<../zh-cn/Boot_loader.html> "Boot loader")的 [EFI 系统分区](<../zh-cn/EFI_system_partition.html> "EFI system partition")。如果您从头开始安装 Windows，请注意 Windows 安装程序创建的 EFI 系统分区对于大多数用例来说太小。请参见[#Windows 安装程序创建的 EFI 系统分区太小](<#Windows_%E5%AE%89%E8%A3%85%E7%A8%8B%E5%BA%8F%E5%88%9B%E5%BB%BA%E7%9A%84_EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA%E5%A4%AA%E5%B0%8F>)。 

###  先 Windows 后 Linux

####  BIOS 系统

#####  使用 Linux 启动引导程序

你可以使用任何具有多启动支持的 BIOS [启动引导程序](<../zh-cn/Boot_loader.html> "Boot loader")。 

#####  使用 Windows Vista/7/8/8.1 启动引导程序

本章节将讲述如何在某一分区而非 MBR 上安装一个 Linux 启动引导程序、将该程序复制到某个可被 Windows 引导程序读取的分区，以及用 Windows 引导程序启动该 Linux 引导程序。 

**注意：** 某些文档声明能被 Windows 引导器读取的分区必须是主分区，但是扩展分区的使用也有成功记录。

  * 在安装引导程序时，请将其安装在你的`/boot`分区而非 MBR 上。如果使用 GRUB，请见[GRUB/技巧和窍门#安装到分区上或者无分区磁盘上](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html#%E5%AE%89%E8%A3%85%E5%88%B0%E5%88%86%E5%8C%BA%E4%B8%8A%E6%88%96%E8%80%85%E6%97%A0%E5%88%86%E5%8C%BA%E7%A3%81%E7%9B%98%E4%B8%8A> "GRUB/技巧和窍门")；如果是 Syslinux，见[Syslinux#Manual install](<../zh-cn/Syslinux.html#Manual_install> "Syslinux")处的附注；如果是 LILO，见[LILO#Install to partition or partitionless disk](</wzh/index.php?title=LILO&action=edit&redlink=1> "LILO（页面不存在）")。
  * 建立一份 VBR 的拷贝：

    dd if=/dev/_disk_ of=_/path/to/_ linux.bin bs=512 count=1

其中`/dev/_disk_`是你安装启动引导程序的分区的路径，`/path/to/`是你想要 Windows 启动引导程序可以读取该拷贝的且已经挂载的文件系统。 

  * 现在你的 linux.bin 应该可以在 Windows 下访问了。以管理员权限运行**cmd** （进入 _开始菜单-全部应用程序-(Windows)附件_ 。右键 _命令提示符_ 并选择 _以管理员权限运行_ ）并执行以下命令：

    bcdedit /create /d "Linux" /application BOOTSECTOR

BCDEdit 将会返回该项的[UUID](<https://en.wikipedia.org/wiki/Universally_unique_identifier> "wikipedia:Universally unique identifier")。该 UUID 在下面的步骤中将会用` _UUID_`代替。 
    
    bcdedit /set _UUID_ device partition=X: (X:为linux.bin所处分区的分卷号)
    bcdedit /set _UUID_ path \path\to\linux.bin
    bcdedit /displayorder _uuid_ /addlast
    bcdedit /timeout 30

重启之后，Windows 和 Linux 应该都显示在 Windows 的启动引导程序当中。 

**注意：** 在某些电脑上，Windows 引导程序用另一电源按钮启动另一 OS（例如：Dell Precision M4500）。

参见 <https://www.iceflatline.com/2009/09/how-to-dual-boot-windows-7-and-linux-using-bcdedit/>

####  UEFI 系统

如果你已经安装 Windows，它已经在一张[GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT")格式的硬盘上创建如下分区： 

  * 一个[WinRE（ **W** indows **R** ecovery **E** nvironment）](<https://en.wikipedia.org/wiki/Windows_Recovery_Environment> "wikipedia:Windows Recovery Environment")分区，一般大小为499 MiB，包含启动 Windows 所需的文件，等同于 Linux 下的`/boot`分区;
  * 一个具有 [FAT32](<../zh-cn/FAT.html> "FAT32") 文件系统的 [EFI 系统分区](<../zh-cn/EFI_system_partition.html> "EFI system partition");
  * 一个[MSR 分区(Microsoft Reserved Partition)](<https://en.wikipedia.org/wiki/Microsoft_Reserved_Partition> "wikipedia:Microsoft Reserved Partition");
  * 一个格式化为 NTFS 的 Microsoft Basic Data 分区，对应`C:`;
  * 可能是系统恢复/备份/非主要数据分区（对应`D:`等）;

在 Windows 下，使用磁盘管理工具查看各分区的标签以及报告的类型。这样能使人清楚哪些分区属于必要的 Windows 分区，以及可能随时改变用途的其它分区。Windows 磁盘管理同样可以缩小 Windows (NTFS) 分区以便为 Linux 腾出空间。 

**警告：** 上述分区中前 4 种为关键系统分区，不能删除。

现在可以继续按需进行[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning")。引导加载程序需要支持链式加载其他EFI应用程序，以实现Windows和Linux的双重启动。 

不应创建额外的EFI系统分区，因为这可能会[导致Windows无法启动](<https://support.microsoft.com/en-us/help/2879602/unable-to-boot-if-more-than-one-efi-system-partition-is-present>)。[直接挂载现有分区](<../zh-cn/EFI_system_partition.html#Mount_the_partition> "EFI system partition")即可。

**注意：** 只有 Linux 被安装在另一块硬盘并在磁盘上创建了新的 EFI 系统分区时才会出现此问题。

启动引导程序须支持链式载入其它 EFI 应用程序以进行 Windows-Linux 双启动。 

**提示：** * [rEFInd](<../zh-cn/REFInd.html> "REFInd")和[systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot")都会自动检测 _Windows Boot Manager_(`\EFI\Microsoft\Boot\bootmgfw.efi`)并将其显示于自己的启动菜单中。如果使用 GRUB，见[GRUB#Windows installed in UEFI/GPT mode](<../zh-cn/GRUB.html#Windows_installed_in_UEFI/GPT_mode> "GRUB")（手动添加启动项）或[GRUB#Detecting other operating systems](<../zh-cn/GRUB.html#Detecting_other_operating_systems> "GRUB")（自动生成配置文件）。 

  * 为了节省EFI系统分区的空间，特别是对于多个内核，请[增加initramfs的压缩率](<../zh-cn/Mkinitcpio.html#%E5%8E%8B%E7%BC%A9%E6%96%B9%E5%BC%8F\(COMPRESSION\)> "Mkinitcpio")。

预装较新版本的 Windows 的电脑通常启用[安全启动](<../zh-cn/Secure_Boot.html> "Secure Boot")。需要进行额外操作以禁用安全启动或使你的安装媒体支持安全启动（详见上文）。 

###  先 Linux 后 Windows

即使设置 Windows-Linux 双启动时一般推荐先安装 Windows，换成 Linux 在前也可以实现双启动。与 Windows 在前的方式相比，这种方式需要在启动 Windows 安装之前创建并搁置一个（比如 40GB 或者更高的）Windows 分区，或者预留一些空闲的未分区空间，或者从 Linux 安装中创建/调整 Windows 分区。 

####  UEFI 固件

Windows 将会使用已有的[EFI 系统分区](<../zh-cn/EFI_system_partition.html> "EFI system partition")。 假设[安全启动](<../zh-cn/Secure_Boot.html> "Secure Boot")已禁用。 

  1. 启动 Windows 安装。注意让安装器使用你希望其使用的分区，然后让它如同没有安装 Linux 一样工作。
  2. 按照[#快速启动和休眠](<#%E5%BF%AB%E9%80%9F%E5%90%AF%E5%8A%A8%E5%92%8C%E4%BC%91%E7%9C%A0>)的说明操作。
  3. 恢复 Linux 启动（可参阅[#安装 Windows 后 Linux 无法启动](<#%E5%AE%89%E8%A3%85_Windows_%E5%90%8E_Linux_%E6%97%A0%E6%B3%95%E5%90%AF%E5%8A%A8>)）。[前面](<#UEFI_%E7%B3%BB%E7%BB%9F>)已经提到过，某些 Linux 引导启动程序会自动检测 _Windows Boot Manager_ 。即使较新的 Windows 安装都有一个能用于启动到 Linux 的“高级启动”选项，仍然建议使用 Arch 安装媒体或 LiveCD 之类的方式启动 Linux。

#####  Windows 10 和 GRUB

这里假设使用[GRUB](<../zh-cn/GRUB.html> "GRUB")作为启动引导程序（对于其它引导程序大致思路也相似）且 Windows 10 将会安装到一个已经有 EFI 系统分区的 GPT 块设备上。详见[这篇](<https://docs.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/configure-uefigpt-based-hard-drive-partitions?view=windows-11>) Microsoft 文档的“系统分区”章节。 

用`gdisk`在块设备上创建如下分区：（更精确的分区大小见[[5]](<https://docs.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/configure-uefigpt-based-hard-drive-partitions?view=windows-11>)） 

标题文本  最小尺寸 | 分区类型代码 | 分区类型名 | 文件系统   
---|---|---|---  
16 MB | 0C01 | Microsoft reserved | N/A   
约 40 GB或更大 | 0700 | Microsoft basic data | NTFS   
300 MB | 2700 | Windows RE | NTFS   
  
用来自[ntfs-3g](<https://archlinux.org/packages/?name=ntfs-3g>)包的`mkntfs`工具在新创建的 Microsoft basic data 和 Windows RE 分区上创建新的 NTFS 文件系统。 

将系统重启到 Windows 10 安装媒体。选择“自定义”安装选项并将 Windows 安装到先前创建的 Microsoft basic data 分区上。这样应该也会将 Microsoft EFI 文件安装到 EFI 分区中。 

安装完毕后（不需要 OOBE 和登录），重启进入 Linux 并[生成一个 GRUB 配置文件](<../zh-cn/GRUB.html#Generate_the_main_configuration_file> "GRUB")以便 Windows 的启动管理器在下次启动时启动在 GRUB 菜单中。 

###  故障排除

####  无法创建新分区或无法找到已有分区

见 [#Windows 在 UEFI 和 BIOS 上的限制](<#Windows_%E5%9C%A8_UEFI_%E5%92%8C_BIOS_%E4%B8%8A%E7%9A%84%E9%99%90%E5%88%B6>)。 

####  安装 Windows 后 Linux 无法启动

见 [Unified Extensible Firmware Interface#Windows changes boot order](<../zh-cn/Unified_Extensible_Firmware_Interface.html#Windows_changes_boot_order> "Unified Extensible Firmware Interface")

####  恢复 Windows 启动记录

按照惯例（且为了更简易的安装过程），Windows 通常安装在第一分区并将其分区表和其启动引导程序的引用安装到该分区的第一扇区。如果不慎把一个 GRUB 之类的启动引导器安装到 Windows 分区上，或者用其它什么方式弄坏了 Windows 的启动记录，就需要使用工具对其进行修复。Microsoft 在他们的恢复光盘（有些时候，安装光盘）上提供一个叫做`FIXBOOT`的启动扇区修复工具和一个名为`FIXMBR`的 MBR 修复工具。这种方式可以分别更正第一分区的启动扇区对启动引导程序的引用以及 MBR 上对第一分区的引用。在此之后需要按原先计划[将 GRUB 重新安装](<../zh-cn/GRUB.html#Installation> "GRUB")到 MBR 上（GRUB 可以配置为链式加载 Windows 启动引导程序）。 

如果你希望回退到 Windows，你可以用`FIXBOOT`命令链接 MBR 和第一分区启动扇区以恢复 Windows 的自动启动。 

有一个叫做[ms-sys](<https://aur.archlinux.org/packages/ms-sys/>)AUR的工具可以用于安装 MBR。但是，该工具目前只能写新 MBR 或 FAT 文件系统的启动扇区（又称为启动记录；等效于`FIXBOOT`）。许多 LiveCD 默认都没有该工具，所以其需要提前安装，或者可以考虑包含该工具的急救 CD，如[Parted Magic](<https://partedmagic.com/>)。 

首先，重新写一遍分区信息（表）： 
    
    # ms-sys --partition /dev/sda1

接下来，写 Windows 2000/XP/Server 2003 MBR： 
    
    # ms-sys --mbr /dev/sda  #查阅 options 列表以获取不同版本的信息

最后，写启动扇区： 
    
    # ms-sys -(1-6) #查阅 options 列表以查找正确的 FAT 记录类型

`ms-sys`同样可以写 Windows 98/ME 及 Windows Vista/7 MBR。详见`ms-sys -h`。 

####  恢复意外删除的EFI系统分区

如果您的磁盘采用GPT分区，并且擦除了（例如使用 `mkfs.fat -F32 /dev/sd _x_` 擦除）EFI系统分区，您会发现Windows引导管理器要么从启动选项中消失，要么选择它会将您送回UEFI界面。 

欲解决这个问题，请使用Windows安装介质启动，按下 `Shift+F10` 打开控制台（或点击 _NEXT > Repair Computer > Troubleshoot... > Advanced > Command Prompt_ ），然后启动diskpart实用程序： 
    
    X:\Sources> diskpart
    DISKPART> list disk
    
选择适当的硬盘： 
    
    DISKPART> select disk _number_
    
确保存在一个系统类型的分区（EFI系统分区） 
    
    DISKPART> list partition
    
选择该分区， 
    
    DISKPART> select partition _number_
    
并为其分配一个临时驱动器号：
    
    DISKPART> assign letter=_G_ :
    
    DiskPart successfully assigned the drive letter or mount point.

为确保正确分配驱动器号，请检查一下：
    
    DISKPART> list vol
    
    Volume ###  Ltr  Label        Fs     Type        Size     Status     Info
     ----------  ---  -----------  -----  ----------  -------  ---------  --------
     Volume 0     E                       DVD-ROM         0 B  No Media
     Volume 1     C                NTFS   Partition    195 GB  Healthy    Boot
     Volume 2         WINRE        NTFS   Partition    400 MB  Healthy    Hidden
     Volume 3     **G**                **FAT32**  Partition    **499 MB**  Healthy    System

关闭diskpart 
    
    DISKPART> exit
    
导航到 `C:\` （或者你的系统驱动器卷标）： 
    
     X:\Sources> cd /d _C_ :\
    
接下来是"magic"命令，重新创建BCD存储（使用 `/s` 作为挂载点， `/f` 作为固件类型，可选择添加 `/v` 以获取详细信息）： 
    
    C:\> bcdboot C:\Windows /s _G_ : /f UEFI
    
**提示：** 如果一分钟后卡住了，点击 `Ctrl+c`。有时会发生这种情况，但你会收到一个类似 `boot files successfully created` 的消息，而且它会正常工作。

现在，您应该已经将 _Windows引导管理器（Windows Boot Manager）_ 设置为启动选项，从而可以访问Windows。只需确保再也不要格式化您的EFI系统分区！

**注意：** 删除分配给EFI系统分区的G盘符，以防止它在 _我的电脑_ 中显示出来。

参见 [[6]](<https://www.reddit.com/r/archlinux/comments/yprrhr/guide_what_to_do_if_you_accidentally_format_your/>), [[7]](<https://superuser.com/a/1111656>) 和 [[8]](<https://superuser.com/a/1507645>). 

####  Windows 安装程序留下的 EFI 系统分区太小

默认情况下，[Windows 安装程序](<https://en.wikipedia.org/wiki/Windows_Setup> "wikipedia:Windows Setup")会创建一个 100 MiB 的 [EFI 系统分区](<../zh-cn/EFI_system_partition.html> "EFI system partition")（在[Advanced Format](<../zh-cn/Advanced_Format.html> "Advanced Format")盘上为 300 MiB）。一般来说，这种容量并不足以放下所需要的所有文件。您可以[替换现有的 EFI 系统分区为一个新的、更大的分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html#%E6%9B%BF%E6%8D%A2%E4%B8%BA%E6%9B%B4%E5%A4%A7%E7%9A%84%E5%88%86%E5%8C%BA> "EFI 系统分区")。 

不过，如果你从头开始安装Windows，就可以在安装过程中指定EFI系统分区的大小[[9]](<https://www.ctrl.blog/entry/how-to-esp-windows-setup.html>)： 

  1. 选择您的安装目标，并确保它没有分区。
  2. 点击 _“New”_ 按钮，然后点击 _“Apply”_ 按钮。Windows安装程序将生成预期的分区（将几乎所有内容分配给其主分区），并将仅分配100MB给EFI。
  3. 用安装程序的图形界面删除 `System` 、 `MSR` 和 `Primary` 分区。保留 `Recovery` 分区（如果存在）不变。
  4. 按下 `Shift+F10` 键打开命令提示符。
  5. 输入 `diskpart.exe` 并按下 `Enter` 打开磁盘分区工具。
  6. 输入 `list disk` 并按下 `Enter` 列出您的磁盘。找到您打算修改的磁盘并记录其磁盘编号。
  7. 输入 `select disk _disk_number_` 和磁盘号以进行修改。
  8. 输入 `create partition efi size=_size_` 和所需的ESP大小（以Mebibytes（MiB）为单位），然后按 `Enter` 。请参阅[EFI 系统分区#创建分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html#%E5%88%9B%E5%BB%BA%E5%88%86%E5%8C%BA> "EFI 系统分区")获取EFI的推荐大小。
  9. 输入 `format quick fs=fat32 label=System` 并按 `Enter` 键以格式化ESP
  10. 输入 `exit` 并按 `Enter` 键退出磁盘分区工具，然后再次输入 `exit` 和 `Enter` 。

一旦安装了Windows，你就可以在Windows中调整主分区的大小，然后重新启动并进行常规的Arch安装，填充刚刚创建的空间。 

或者，可以将 Windows 安装到盘上**之前** 就用 Arch 安装媒体创建一个自定大小（且较大）的[EFI 系统分区](<../zh-cn/EFI_system_partition.html> "EFI system partition")。Windows 安装程序将会使用你自己创建的 EFI 分区，而非再为自己创建一个。 

####  无法在BIOS系统上安装Windows累积更新

在BIOS系统上，Windows累积更新可能会失败，并显示错误信息：无法完成更新。正在撤销更改。请勿关闭计算机。在这种情况下，在Windows中，您需要[将Windows分区设置为活动分区](<https://superuser.com/a/1405702>)。 
    
    C:\> diskpart
    DISKPART> list disk
    DISKPART> select disk _number_
    DISKPART> list partition
    DISKPART> select partition _number_
    DISKPART> active
    DISKPART> exit
    
成功安装Windows更新后，再使用上述命令将Linux分区标记为活动状态。 

##  时间标准

  * 建议：将 Arch Linux 和 Windows 皆设置为UTC时间（见[系统时间#Windows 系统使用 UTC](<../zh-cn/%E7%B3%BB%E7%BB%9F%E6%97%B6%E9%97%B4.html#Windows_%E7%B3%BB%E7%BB%9F%E4%BD%BF%E7%94%A8_UTC> "系统时间")）。某些 Windows 版本在设置为自动同步网络时间时会将 RTC（硬件时钟） 回退到本地时间 _（localtime）_ 。该问题在 Windows 10 中似乎已修复。

  * 不建议：将Arch Linux的硬件时钟模式设为 _localtime_ 并禁用任何时钟同步服务。这将让Windows负责硬件时钟的校正，并且你需要在一年中至少启动Windows两次(分别在春季与秋季)以正确应用[夏令时](<https://en.wikipedia.org/wiki/Daylight_savings_time> "wikipedia:Daylight savings time")。所以请**不要** 忘记启动 Windows 而在论坛问为什么时钟会快/慢一个小时。

##  蓝牙配对

对于将蓝牙设备同时与 Linux 和 Windows 配对，两个系统均使用相同的 MAC 地址，但是配对过程中会使用不同的 _link keys_ ，导致在蓝牙设备与其中一个系统配对后就无法连接到另一个系统。如果想要使蓝牙设备不用重新配对就在两个系统下都可用，见[Bluetooth#Dual boot pairing](<../zh-cn/%E8%93%9D%E7%89%99.html#Dual_boot_pairing> "Bluetooth")。 

##  参见

  * [Booting Windows from a desktop shortcut](<https://bbs.archlinux.org/viewtopic.php?id=140049>)
  * [One-time boot into Windows partition from desktop shortcut](<https://github.com/kaipee/grub-reboot2win>)
  * [Windows 7/8/8.1/10 ISO to Flash Drive burning utility for Linux (MBR/GPT, BIOS/UEFI, FAT32/NTFS)](<https://github.com/ValdikSS/windows2usb>)
