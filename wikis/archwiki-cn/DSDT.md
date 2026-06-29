**翻译状态：**

  * 本文（或部分内容）译自 [DSDT](<https://wiki.archlinux.org/title/DSDT> "arch:DSDT")，最近一次同步于 2025-04-09，若英文版本有所[更改](<https://wiki.archlinux.org/title/DSDT?diff=0&oldid=827491>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/DSDT_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [ACPI modules](<../zh-cn/ACPI_modules.html> "ACPI modules")
  * [acpid](<../zh-cn/Acpid.html> "Acpid")

DSDT(Differentiated System Description Table)是[ACPI](<https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface> "wikipedia:Advanced Configuration and Power Interface")规格的一部分。它提供了关于一个给定系统中受支持的电源事件的信息。ACPI表是由制造商在固件里提供的。通常，Linux遇到的问题是某些ACPI功能的缺失，比如风扇不转，盖子合上时屏幕不熄灭等等。这些问题可以归咎于DSDT是为Windows所定制的。安装后可以打补丁来修复这些问题。这篇文章的目标是分析并且重建一个有错误的DSDT，这样内核就会略过默认的DSDT。 

基本上来说，一个DSDT表是运行在ACPI(电源管理)上的代码。 

**注意：**[Linux ACPI](<https://01.org/linux-acpi>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-09-16 ⓘ]项目的目标让Linux工作在未修改的固件上。如果你还是觉得这种方法在现代内核上是必要的，那么你应该考虑一下[报告bug](<../zh-cn/Reporting_bug_guidelines.html> "Reporting bug guidelines")。 

##  在你开始之前

硬件制造商可能已经发布了更新的固件，修复了与ACPI相关的问题。安装更新的固件通常比这种方法更可取，因为它可以避免重复劳动。 

此过程会修改你安装中的一些相当基础的代码。你需要绝对确定所做的更改。你可能还希望在之前[克隆你的磁盘](<../zh-cn/Disk_cloning.html> "Disk cloning")。 

即使在尝试自己修复DSDT之前，你也可以尝试以下几种捷径： 

###  让内核报告某个Windows版本

使用变量`acpi_os_name`作为[内核参数](<../zh-cn/Kernel_parameter.html> "Kernel parameter")。例如： 
    
    acpi_os_name="Microsoft Windows NT"
    
要添加一个被识别的操作系统接口，使用变量`acpi_osi`。 
    
    acpi_osi="Linux"
    
要仅使用一个操作系统接口，添加`acpi_osi=!`。这会告诉固件只有一个支持的操作系统，因此这通常是推荐的解决方案。 
    
    acpi_osi=! acpi_osi="Windows 2022"
    
要移除一个接口，在字符串的开头使用感叹号。 
    
    acpi_osi="!Windows 2012"
    
其他可以测试的字符串： 

  * "Microsoft Windows XP"
  * "Microsoft Windows 2000"
  * "Microsoft Windows 2000.1"
  * "Microsoft Windows ME: Millennium Edition"
  * "Microsoft WindowsME: Millennium Edition"
  * "Windows 2001"
  * "Windows 2006"
  * "Windows 2009"
  * "Windows 2012"
  * "Windows 2015"
  * "Windows 2020"

**提示：** 虽然不推荐，但你可以尝试"Linux"。

出于好奇，你可以按照以下步骤提取你的DSDT并搜索 _.dsl_ 文件。只需grep "Windows"并查看结果。 

###  找到一个修复过的DSDT

DSDT文件最初是用ACPI源语言（一个 _.asl_ /_.dsl_ 文件）编写的。使用编译器可以生成一个'ACPI机器语言'文件（ _.aml_ ）或一个十六进制表（ _.hex_ ）。要将该文件整合到你的Arch安装中，你需要获取一个编译好的 _.aml_ 文件——无论是自己编译还是信任互联网上的某个陌生人，这取决于你。如果你从互联网上下载文件，它很可能是一个压缩的 _.asl_ 文件。因此，你需要解压并编译它。这样做的好处是你不必自己研究特定的代码修复。 

像你一样使用同一种笔记本的Arch用户是少数中的少数中的少数。尝试浏览其他发行版/Linux论坛，寻找关于相同型号的讨论。很可能他们有相同的问题，并且因为有很多人，或者因为他们技术娴熟——有人已经制作了一个可用的DSDT，甚至可能提供预编译版本（再次提醒，使用时需自行承担风险）。 搜索引擎是你的最佳工具。尝试保持简短：'型号名称' + 'dsdt' 可能会产生结果。 

##  自己重新编译

在这个过程中你的最好的资源将会是[ACPI Spec homepage](<https://uefi.org/acpi/specs>)，和[Linux ACPI Project](<https://01.org/linux-acpi>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-09-16 ⓘ]，这些将会替代 _acpi.sourceforge.net_ 。 简而言之，你可以使用英特尔的ASL编译器将你系统的DSDT表转换成源代码，定位并修复错误，最后重新编译。 

你将会需要安装[acpica](<https://archlinux.org/packages/?name=acpica>)包来修改代码。 **什么编译器编译了原始代码？** 查看你系统的DSDT使用英特尔的还是微软的编译器编译的： 
    
     # dmesg|grep DSDT 
    
    ACPI: DSDT 00000000bf7e5000 0A35F (v02 Intel  CALPELLA 06040000 INTL 20060912)
    ACPI: EC: Look up EC in DSDT
    
如果是微软的编译器，INTL将会变成MSFT。 在这个例子中，在反编译/编译的DSDT时共有五个错误，有两个在谷歌一下和研究ACPI规范之后很容易解决。另外三个是由于使用了不同版本的编译器。后来你会发现，它们三个会在启动时被ACPICA处理。内核的ACPICA部分可以处理编译DSDT时产生的的大部分不重要的错误.所以如果你的系统正在 _按照正常方式运行_ ，请不要为了编译错误烦恼。 

1.) 提取ACPI表(作为超级用户): `# cat /sys/firmware/acpi/tables/DSDT > dsdt.dat`

2.) 反编译: `iasl -d dsdt.dat`

3.) 重新编译: `iasl -tc dsdt.dsl`

4.) 检查错误并修复。例如:
    
    dsdt.dsl   6727:                         Name (_PLD, Buffer (0x10)  
    Error    4105 -          Invalid object type for reserved name ^  (found BUFFER, requires Package) 
    
     nano +6727 dsdt.dsl
    
    (_PLD, Package(1) {Buffer (0x10)...

5.) 增添OEM版本，否则内核不会应用修改过的ACPI表。例如在修改前: 
    
    DefinitionBlock ("DSDT.aml", "DSDT", 2, "INTEL ", "TEMPLATE", 0x00000000)

修改后: 
    
    DefinitionBlock ("DSDT.aml", "DSDT", 2, "INTEL ", "TEMPLATE", 0x00000001)

6.) 编译被修复过的代码: `iasl -tc dsdt.dsl` (你可能需要使用命令行参数`-ic`来将C语言头文件插入内核) 

如果没有错误，你应该可以接着往下进行了。 

##  使用修改过的代码

**警告：** 每次BIOS更新后你都要重新修复DSDT表并且重复这些步骤！

至少有两种方式来使用定制的DSDT: 

  * 创建一个由内核在启动早期加载的未压缩CPIO文档
  * 把它编译进内核

###  使用mkinitcpio的acpi_override钩子

[mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")提供了一个`acpi_override`钩子，它会将`/usr/initcpio/acpi_override/`和`/etc/initcpio/acpi_override/`中找到的所有 _.aml_ 文件放入`/kernel/firmware/acpi/`中的一个早期未压缩CPIO文档中。这避免了手动创建单独的CPIO文档或更改引导加载程序配置的需要，因为 _mkinitcpio_ 将未压缩的CPIO文档与主initramfs映像打包到一个文件中。 

首先，创建`/etc/initcpio/acpi_override`目录并将所有需要的 _.aml_ 文件复制到其中。例如： 
    
    # mkdir /etc/initcpio/acpi_override
    # cp dsdt.aml /etc/initcpio/acpi_override/
    
将`acpi_override`添加到`/etc/mkinitcpio.conf`中的`HOOKS`数组： 
    
    /etc/mkinitcpio.conf
    
    HOOKS=(... **acpi_override**)

最后，[重新生成initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs")并重启。 

###  使用一个CPIO文档

这个方法有一个优点就是你不用重新编译你的内核，升级内核后你也无需重复这些步骤 

这个方法要求内核参数`ACPI_TABLE_UPGRADE=y`被启用(对于[linux](<https://archlinux.org/packages/?name=linux>)包被设置为true)。浏览[[1]](<https://docs.kernel.org/admin-guide/acpi/initrd_table_override.html>) 来查看更多详细内容。 

首先，创建下面的目录结构: 
    
    $ mkdir -p kernel/firmware/acpi
    
将修复过的ACPI表拷贝进刚刚创建的`kernel/firmware/acpi`文件夹，例如: 
    
    $ cp dsdt.aml ssdt1.aml kernel/firmware/acpi
    
在新创建的`kernel/`目录所在的目录下，运行: 
    
    $ find kernel | cpio -H newc --create > acpi_override
    
这条命令会创建含有修复了的ACPI表的CPIO文档。将文档拷贝到`boot`目录。 
    
    # cp acpi_override /boot
    
最后，配置[bootloader](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "Bootloader")来加载你的CPIO文档。例如，使用[Systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot")的话， `/boot/loader/entries/arch.conf`可能看起来像这样: 
    
    title	 Arch Linux
    linux	 /vmlinuz-linux
    initrd   /acpi_override
    initrd	 /initramfs-linux.img
    options  root=PARTUUID=ec9d5998-a9db-4bd8-8ea0-35a45df04701 resume=PARTUUID=58d0aa86-d39b-4fe1-81cf-45e7add275a0 ...
    
现在，剩下需要做的事情就是重启电脑并且[确认结果](<#%E7%A1%AE%E8%AE%A4%E8%A6%86%E7%9B%96%E6%88%90%E5%8A%9F>)。 

###  编译进内核

你会想要熟悉[编译自己的内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernels")。最直接的方式就是用“传统”方法。 编译DSDT之后，iasl产生两个文件:`dsdt.hex`和`dsdt.aml`。 

**使用`menuconfig`:**

  * 禁用"Select only drivers that don't need compile-time external firmware"。位于"Device Drivers -> Generic Driver Options"。
  * 启用"Include Custom DSDT"并且指明你修复过的DSDT文件的绝对路径(`dsdt.hex`，而不是`dsdt.aml`)。位于"Power management and ACPI options -> ACPI (Advanced Configuration and Power Interface) Support"。

###  在GRUB中使用AML

如果你使用[GRUB](<../zh-cn/GRUB.html> "GRUB")，你可以使用一个更简单的方法。将上面创建的 _.aml_ 文件复制到你的引导分区： 
    
    # cp dsdt_patch.aml /boot
    
然后在你的GRUB配置中添加以下行： 
    
    acpi /dsdt_patch.aml
    
你可以将其添加到`/etc/grub.d/40_custom`中，别忘了之后生成你的GRUB配置。 

###  在dracut中使用AML

如果你使用[Dracut](<../zh-cn/Dracut.html> "Dracut")，你可以简单地将上面创建的 _.aml_ 文件复制到一个定义的位置。必须创建一个相应的配置文件`/etc/dracut.conf.d/acpi-fix.conf`： 
    
    acpi_override="yes"
    acpi_table_dir="/usr/local/lib/firmware/acpi"
    
##  确认覆盖成功

查找确认覆盖的消息，例如： 
    
    # dmesg | grep ACPI
    
    [    0.000000] ACPI: Override [DSDT-   A M I], this is unsafe: tainting kernel
    [    0.000000] ACPI: DSDT 00000000be9b1190 Logical table override, new table: ffffffff81865af0
    [    0.000000] ACPI: DSDT ffffffff81865af0 0BBA3 (v02 ALASKA    A M I 000000F3 INTL 20130517)
    
##  参见

  * [通过 initrd 升级 ACPI 表](<https://docs.kernel.org/admin-guide/acpi/initrd_table_override.html>)
  * [如何使用 _OSI 在 ACPI 中识别 Windows 版本](<https://docs.microsoft.com/en-us/windows-hardware/drivers/acpi/winacpi-osi>)
  * [如何使用 dracut 覆盖 ACPI 表](<https://man.archlinux.org/man/dracut.conf.5>)
