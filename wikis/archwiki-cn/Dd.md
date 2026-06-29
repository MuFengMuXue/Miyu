**翻译状态：**

  * 本文（或部分内容）译自 [Dd](<https://wiki.archlinux.org/title/Dd> "arch:Dd")，最近一次同步于 2025-08-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dd?diff=0&oldid=832071>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [硬盘克隆](<../zh-cn/%E7%A1%AC%E7%9B%98%E5%85%8B%E9%9A%86.html> "硬盘克隆")
  * [U_盘安装介质#使用基本命令行工具](<../zh-cn/U_%E7%9B%98%E5%AE%89%E8%A3%85%E4%BB%8B%E8%B4%A8.html#%E4%BD%BF%E7%94%A8%E5%9F%BA%E6%9C%AC%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7> "U 盘安装介质")
  * [基准测试#dd](<../zh-cn/%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%95.html#dd> "基准测试")
  * [安全地擦除磁盘#dd](<../zh-cn/%E5%AE%89%E5%85%A8%E5%9C%B0%E6%93%A6%E9%99%A4%E7%A3%81%E7%9B%98.html#dd> "安全地擦除磁盘")

[dd](<https://en.wikipedia.org/wiki/dd_\(Unix\)> "wikipedia:dd \(Unix\)") 是一个[核心工具](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html> "核心工具")，其主要用途是复制文件，并可在复制过程中选择性地对文件进行转换。 

与`cp`类似，默认情况下`dd`会按位复制文件，但还提供了更底层的 I/O 流控制功能。 

更多信息参见[dd(1)](<https://man.archlinux.org/man/dd.1>)或[完整文档](<https://www.gnu.org/software/coreutils/dd>)。 

**提示：** 默认情况下，`dd`在执行复制操作过程中不会有任何输出。要监控操作进度，可添加`status=progress`选项。

**警告：** 使用`dd`等磁盘操作类命令时应格外小心，错误使用可能会不可逆转地破坏数据。

##  安装

`dd`是GNU [coreutils](<https://archlinux.org/packages/?name=coreutils>)包的一部分。该软件包中的其它工具，可参见[核心工具](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html> "核心工具")。 

##  硬盘克隆与恢复

`dd`是一个简单而又功能多样的强大工具。其可逐块从源（source）到目标（destination）复制内容，而不关心源或目标的文件系统类型、操作系统。可通过live 环境（如 Live CD）便捷的在任何计算机上使用`dd`。 

**警告：** 作为磁盘操作类命令，使用`dd`时应格外小心，避免破坏其它数据。使用时必须注意输入文件（`if=`）、输出文件（`of=`）的顺序，切勿颠倒！务必确保目标设备或分区（`of=`）的大于等于源（`if=`）的大小。 

###  克隆分区

若要将硬盘`/dev/sda`上的第一个分区克隆到硬盘`/dev/sdb`的第一个分区上： 
    
    # dd if=/dev/sda1 of=/dev/sdb1 bs=64K conv=noerror,sync status=progress
    
**注意：** 请确保`of=`中指定的输出分区（`sdb1`）存在。否则，`dd`会在根文件系统下创建同名文件并写入，而不是写入到目标分区中。

###  克隆整个硬盘

若要将硬盘`/dev/sda`上的所有内容克隆到另一个硬盘`/dev/sdb`上： 
    
    # dd if=/dev/sda of=/dev/sdb bs=64K conv=noerror,sync status=progress
    
这将克隆整个硬盘，包括分区表、[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")、所有分区、UUID 和数据。 

  * `bs=`用于设置块大小，默认为512字节。512字节是自20世纪80年代初以来的硬盘的“经典”块大小。但在现代硬盘上，这并非最佳设置。建议使用64K、128K等更大的值。另外，请详细阅读下文的说明，该选项不仅设置“块大小”，还影响读取错误的处理方式。详情请参阅[[1]](<https://www.mail-archive.com/eug-lug@efn.org/msg12073.html>)、[[2]](<http://blog.tdg5.com/tuning-dd-block-size/>)。
  * `noerror`表示当遇到读取错误时，忽略错误继续操作。在默认情况下，`dd`将在遇到任何错误时停止。
  * `sync`表示当遇到读取错误时，用零填充输入块的末尾，以保持数据偏移量同步（若认为输入设备可能产生读取错误，建议阅读下文关于sync在遇到读取错误时的行为的详细解释）。
  * `status=progress`显示传输统计信息，可用于估算操作完成时间。

**注意：** 块大小设置会影响读取错误的处理方式，详见下文。若正在进行数据恢复，请使用[ddrescue](</wzh/index.php?title=Ddrescue&action=edit&redlink=1> "Ddrescue（页面不存在）")。

实际上，`dd`存在“输入块大小”（IBS）和“输出块大小”（OBS）。 

当设置`bs`时，将同时设置IBS和OBS。在通常情况下，若设置块大小为1MiB，`dd`将从输入文件读取1024×1024字节，并写入输出文件。但若发生读取错误，则读取会提前终止。 

在使用`noerror,sync`选项时，一种常见的错误看法是，设置`bs`为1MiB，若读取过程中发生错误，`dd`只会将发生错误的磁盘块（例如，大小可能为512字节）用零填充，而1MiB块的其它部分仍然包含正确的数据；但实际上，根据文档，`dd`会先尝试从输入文件读取IBS个字节，一旦发生读取错误，读取就立刻停止，之后用零将输入块填充到OBS个字节，再写入输出文件。这意味着，对于磁盘而言，若在当前1MiB数据块的头部便发生读取错误（例如，1个512字节的扇区无法读取），则将用零填充整个1MiB数据块，而不是只填充发生错误的扇区。若用ERROR表示错误，则12ERROR89会变成128900000，而不是120000089。 

若确定磁盘没有错误，则可以使用更大的块大小以大幅提高复制速度。例如，在一个普通的 Celeron 2.7 GHz系统上，将`bs`从512改为64K，复制速度从35 MB/s提高到了120 MB/s。但需要注意，若发生读取错误，源磁盘上一个扇区的读取错误最终会成为目标磁盘上一整个块的错误，即一个512字节的读取错误可能会导致整个64 KiB的输出块被填充零。 

**注意：**

  * 在克隆后，若要为ext2/3/4文件系统重新生成UUID，以确保UUID的唯一性，可对每个需要调整的分区执行`tune2fs /dev/sd _XY_ -U random`。对于交换分区，需要执行`mkswap -U random /dev/sd _XY_`。
  * 在克隆[GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT")磁盘后，可使用[sgdisk](<../zh-cn/GPT_fdisk.html#%E5%A4%87%E4%BB%BD%E5%92%8C%E6%81%A2%E5%A4%8D%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT fdisk")来随机化磁盘和分区的GUID，以保证其唯一性。
  * 使用`dd`克隆磁盘导致的分区表更改不会自动被内核注册。要在不重启的情况下通知内核检查更改，可使用类似`partprobe`（[GNU Parted](<../zh-cn/GNU_Parted.html> "GNU Parted") 的一部分）的工具。

###  备份分区表

参见[Fdisk#备份和恢复分区表](<../zh-cn/Fdisk.html#%E5%A4%87%E4%BB%BD%E5%92%8C%E6%81%A2%E5%A4%8D%E5%88%86%E5%8C%BA%E8%A1%A8> "Fdisk")、[GPT_fdisk#备份和恢复分区表](<../zh-cn/GPT_fdisk.html#%E5%A4%87%E4%BB%BD%E5%92%8C%E6%81%A2%E5%A4%8D%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT fdisk")。 

###  创建磁盘镜像

首先，从 live 介质启动，并确保要备份的源硬盘上没有任何分区被挂载。 

然后，挂载用于备份的外部硬盘，备份源硬盘到镜像中： 
    
    # dd if=/dev/sda conv=sync,noerror bs=64M status=progress | lz4 -z  > _/path/to/backup.img.lz4_
    
如果需要（例如，当生成的文件将存储在[FAT32](<../zh-cn/FAT.html> "FAT32")等单文件大小限制较小的文件系统上时），可将磁盘镜像分割成多个部分（另见[split(1)](<https://man.archlinux.org/man/split.1>)）： 
    
    # dd if=/dev/sda conv=sync,noerror bs=64M status=progress | lz4 -z | split -a3 -b2G - _/path/to/backup.img.lz4_
    
如果本地没有足够的磁盘空间用于存储镜像文件，可以通过`ssh`发送镜像： 
    
    # dd if=/dev/sda conv=sync,noerror bs=64M status=progress | lz4 -z | ssh user@local dd of=backup.img.lz4
    
最后，保存有关源磁盘物理结构的额外信息（其中最重要的是扇区大小）。这些信息可用于解析镜像中的分区表。 
    
    # fdisk -l /dev/sda > _/path/to/list_fdisk.info_
    
**提示：**

  * 可设置块大小（`bs=`）为要备份的硬盘的缓存容量。例如，若源硬盘的缓存为512 MiB，可使用`bs=512M`。上文使用的64 MiB块大小的备份速度已经比默认的`bs=512`字节快，使用更大的块大小可能进一步提升备份速度。
  * 上例使用[lz4(1)](<https://man.archlinux.org/man/lz4.1>)进行压缩，其支持多线程，也可使用[其它压缩工具](<../zh-cn/%E5%BD%92%E6%A1%A3%E4%B8%8E%E5%8E%8B%E7%BC%A9.html#%E4%BB%85%E5%8E%8B%E7%BC%A9> "归档与压缩")。

###  恢复系统

要从镜像文件中恢复系统： 
    
    # lz4 -dc _/path/to/backup.img.lz4_ | dd of=/dev/sda status=progress
    
若镜像文件使用分卷方式储存，改用以下命令： 
    
    # cat _/path/to/backup.img.lz4*_ | lz4 -dc | dd of=/dev/sda status=progress
    
##  备份与恢复MBR

在对磁盘进行更改之前，可能希望备份设备的分区表和分区方案。此外，还可以通过备份与恢复的方式将相同的分区布局复制到多个设备。 

MBR存储在磁盘的前512字节中，由4个部分组成： 

  1. 前440字节包含引导加载程序代码（[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")）。
  2. 接下来的6字节包含磁盘签名。
  3. 再接下来的64字节包含分区表（4个条目，每个16字节，每个条目对应一个主分区）。
  4. 最后2字节包含引导签名。

要将MBR保存到`mbr_file.img`镜像中： 
    
    # dd if=/dev/sd _X_ of=_/path/to/mbr_file.img_ bs=512 count=1
    
此外，也可以从完整磁盘备份镜像中提取MBR： 
    
    # dd if=_/path/to/disk.img_ of=_/path/to/mbr_file.img_ bs=512 count=1
    
要将备份的MBR恢复到磁盘上（注意，这将销毁现有的分区表，导致磁盘上所有数据无法访问）： 
    
    # dd if=/_path/to/mbr_file.img_ of=/dev/sd _X_ bs=512 count=1
    
**警告：** 若恢复的MBR与磁盘上的实际分区布局不匹配，则由于分区识别错误，磁盘上的数据将无法读取，且很难修复。如果只是需要重新安装引导加载程序，不应通过恢复MBR的方式进行，因为除了MBR区域外，引导加载程序还可能需要使用[DOS 兼容区域](<https://www.pixelbeat.org/docs/disk/>)，参见：[GRUB](<../zh-cn/GRUB.html> "GRUB")、[Syslinux](<../zh-cn/Syslinux.html> "Syslinux")。

若只需要恢复引导加载程序代码部分，而不恢复主分区表，则只需恢复MBR的前 440 字节： 
    
    # dd if=_/path/to/mbr_file.img_ of=/dev/sd _X_ bs=440 count=1
    
若要只恢复主分区表，不恢复引导加载程序代码部分，使用： 
    
    # dd if=_/path/to/mbr_file.img_ of=/dev/sd _X_ bs=1 skip=446 count=64
    
###  移除引导加载程序

要清除MBR中引导程序加载程序的代码（可能在需要完全重新安装另一操作系统时有用），只需将前440字节清零： 
    
    # dd if=/dev/zero of=/dev/sd _X_ bs=440 count=1
    
##  除磁盘操作外的额外用法

虽然[dd(1)](<https://man.archlinux.org/man/dd.1>)支持[一些其他常用工具中不支持的独特功能](<https://unix.stackexchange.com/a/12538#12538>)，但其与其它[核心工具](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html> "核心工具")的命令行语法差距较大，许多默认行为并不符合预期，且在应用于特定场景时[容易出错](<#%E9%83%A8%E5%88%86%E8%AF%BB%E5%8F%96%EF%BC%9A%E5%A4%8D%E5%88%B6%E7%9A%84%E6%95%B0%E6%8D%AE%E9%87%8F%E5%B0%8F%E4%BA%8E%E8%A6%81%E6%B1%82%E7%9A%84%E5%A4%A7%E5%B0%8F>)。因此，若可能，推荐使用在特定方面更易使用的其它工具。 

不过，由于`dd`是[核心工具](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html> "核心工具")，默认安装于Arch和其它众多系统上。因此，对于不便在系统上安装新软件包的情况，可能仍需使用`dd`进行操作，而不能使用其它更好的替代品。 

为了同时涵盖上述两个方面，本节聚焦于[dd(1)](<https://man.archlinux.org/man/dd.1>)的独特功能。这些功能在其它常用工具中很少见。本节的形式类似于[Pacman/各软件包管理器命令对应关系](<../zh-cn/Pacman/%E5%90%84%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%AE%A1%E7%90%86%E5%99%A8%E5%91%BD%E4%BB%A4%E5%AF%B9%E5%BA%94%E5%85%B3%E7%B3%BB.html> "Pacman/各软件包管理器命令对应关系")，同时给出使用`dd`实现与使用其它工具实现的示例，但减少了其它工具的示例的数量，以聚焦于`dd`的功能。其它工具的示例将在“提示”框中通过实际指令或伪代码体现。 

**注意：** 为保持本节简洁，只考虑官方仓库中的替代工具，并着重展示`dd`具有明显优势的情况。如有必要，我们会详细解释其优势。  
更多替代方案，可参见[核心工具#dd_替代品](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#dd_%E6%9B%BF%E4%BB%A3%E5%93%81> "核心工具")。

###  原地逐块修补二进制文件

在自动化的shell脚本中，经常使用`dd`作为二进制文件修补程序。尽管其功能相比专用工具有限，但支持： 

  * 通过`seek`选项，在输出文件特定偏移量处开始写入。
  * 覆盖输出文件中的特定部分，但不将输出文件截断到写入结束的位置（使用`conv=notrunc`选项）。

在下例中，使用`dd`修改了符合[cpio(5) § Portable ASCII Format](<https://man.archlinux.org/man/cpio.5#Portable_ASCII_Format>)格式的归档文件中第一个成员的时间戳，该时间戳起始于文件的第49（十六进制`0x30`）字节： 
    
    $ touch a-randomly-chosen-file
    $ bsdtar -cf example-modify-ts.cpio --format odc -- a-randomly-chosen-file
    
    $ printf '%011o' "$(date -d "2019-12-21 00:00:00" +%s)" | dd conv=notrunc of=example-modify-ts.cpio seek=**48** oflag=seek_bytes
    
**注意：** 在上例中，使用了尚未写入文档的[`seek_bytes` 输出标志](<https://github.com/coreutils/coreutils/commit/140eca15c4a3d3213629a048cc307fde0d094738>)，用于以字节而不是块为单位，指定写入输出文件的偏移量。

**提示：** 若要将命令行中输入的十六进制表示转换为二进制字节流，可使用[basenc(1) § base16](<https://man.archlinux.org/man/basenc.1#base16>)或[printf(1)](<https://man.archlinux.org/man/printf.1>)。

**提示：** 若需要在输出文件指定偏移量处开始写入数据，且不截断输出文件，除了使用`dd`外，还可以考虑使用支持在shell打开的文件描述符上调用[lseek(2)](<https://man.archlinux.org/man/lseek.2>)的shell。若有以下需求： 

  * 输入文件是一个管道，其连接到一个使用[splice(2)](<https://man.archlinux.org/man/splice.2>)系统调用的程序，且希望避免`dd`产生的不必要的用户空间I/O，以获得更好的性能
  * 为避免在shell脚本的循环中频繁[fork(2)](<https://man.archlinux.org/man/fork.2>)，以减少性能开销

那么需要让shell先打开文件描述符，在文件描述符上执行定位操作，并最终连接到相应程序的输出端。“相应程序”可以是上面提到的使用[splice(2)](<https://man.archlinux.org/man/splice.2>)系统调用的工具、不进行fork的shell内建命令（例如：[zshmodules(1) § sysseek](<https://man.archlinux.org/man/zshmodules.1#sysseek>)）： 
    
    $ zsh
    
    $ local +xr openToWriteFD
    $ zmodload zsh/system
    $ sysopen -wu openToWriteFD example-modify-ts.cpio
    $ sysseek -u $openToWriteFD 48
    $ printf '%011o' "$(date -d "2019-12-21 00:00:00" +%s)" >&${openToWriteFD}
    ...
    $ : finally close the fd {openToWriteFD}>&-

**警告：** 若不能确定产生输出的相应程序是否使用了[splice(2)](<https://man.archlinux.org/man/splice.2>)，请避免使用此方法。因为这意味着对于该程序而言，不应在其输出上执行任何类型的定位或截断操作。 一些程序可能会自行在输入/输出文件描述符上进行定位/截断，即使未在命令行参数中要求该行为。程序执行的定位/截断操作将导致shell的[lseek(3)](<https://man.archlinux.org/man/lseek.3>)调用无效，或导致打开的文件描述被意外截断。

###  输出VFAT文件系统镜像的卷标

**提示：** 对于该需求，更好的选择是使用[file](<https://archlinux.org/packages/?name=file>)包。

VFAT文件系统的[卷标](<https://wiki.osdev.org/FAT#FAT_32_2>)位于偏移量`0x047`处，长度为11字节，卷标长度小于11字节的，由ASCII空格填充到11字节。要读取存储在镜像文件中的VFAT文件系统的卷标： 
    
    $ truncate -s 36M empty-hole.img
    $ mkfs.fat -F 32 -n LabelMe empty-hole.img
    
    $ dd iflag=skip_bytes,count_bytes count=11 skip=$((0x047)) if=empty-hole.img | sed -e 's% *$%%'
    
**注意：**[使用到的两个输入标志当前均未写入文档](<https://github.com/coreutils/coreutils/commit/140eca15c4a3d3213629a048cc307fde0d094738>)： 

  * `skip_bytes`：在开始从输入文件[read(2)](<https://man.archlinux.org/man/read.2>)之前，先定位到指定偏移量，偏移量以字节数而不是块数指定。若输入不支持定位操作，则跳过该输入文件。
  * `count_bytes`：以字节而不是块为单位指定从输入文件复制的数据量。注意，即使使用了该标志，仍可能遇到“部分读取”问题。其实际行为类似[`count`](<#%E9%83%A8%E5%88%86%E8%AF%BB%E5%8F%96%EF%BC%9A%E5%A4%8D%E5%88%B6%E7%9A%84%E6%95%B0%E6%8D%AE%E9%87%8F%E5%B0%8F%E4%BA%8E%E8%A6%81%E6%B1%82%E7%9A%84%E5%A4%A7%E5%B0%8F>)。

**提示：** 在shell脚本中，若要实现从输入文件指定偏移量开始，读取指定长度的数据作为输出的功能，也可以考虑使用[curl(1) § r,](<https://man.archlinux.org/man/curl.1#r,>)。

**注意：** 若输入文件是设备/管道，`curl`不支持进行定位/跳过操作。此时可使用[socat(1)](<https://man.archlinux.org/man/socat.1>)，其支持对输入文件（包括块设备，但不包括管道和字符设备）进行这些定位操作，但不如`curl`常用：
    
    $ socat -u -,seek=$((0x047)),readbytes=11 - < empty-hole.img | sed -e 's% *$%%'

###  在管道命令之间充当缓冲（sponge）

**提示：** 对于该需求，也可使用[sponge(1)](<https://man.archlinux.org/man/sponge.1>)，其先读取所有输入数据，将输入数据写入到临时目录（通过`$TMPDIR`环境变量指定；若未指定，则为`/tmp`），再一次性写入到输出中。从而实现原子写入。

在下例中，若输出端长时间阻塞，则输入端将长时间等待，导致建立的TCP连接持续时间过长。此时可以在两个命令之间“拼接”一个`dd`。`dd`的输出块大小应明显大于输入，同时需要小于可用内存容量： 
    
    $ curl -qgsfL http://example.org/mirrors/ftp.archlinux.org/mirrored.md5deep | dd ibs=128k obs=200M | <一个逐行对输入文件中存储的路径信息执行镜像，但不会先缓冲整个输入文件的低效镜像脚本>
    
**警告：** 这绝不应被视为[sponge(1)](<https://man.archlinux.org/man/sponge.1>)的通用替代方案，因为`dd`在开始复制操作之前会截断输出文件。

###  传输有大小限制的数据

在数据流式 shell 脚本中，可以使用`dd`来限制管道命令可能消耗的数据总长度。例如，以流式方式使用shell脚本函数检查ustar头部块[tar(5) § POSIX ustar Archives](<https://man.archlinux.org/man/tar.5#POSIX_ustar_Archives>)）： 

**注意：** 在`count`选项的参数中使用`B`后缀是GNU coreutils v9.1中[新引入的功能](<https://github.com/coreutils/coreutils/commit/97e9778296ead515e77a64942b84f88dcf36a176>)，其效果与[count_bytes输入标志](<#%E8%BE%93%E5%87%BAVFAT%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E9%95%9C%E5%83%8F%E7%9A%84%E5%8D%B7%E6%A0%87>)相同。注意，在不使用`B`后缀时，`count`指定的是块数量，而不是字节数量，即使附加了其它后缀（例如，`k`）。例如，`count=256k`表示复制262144个输入块而不是262144字节。
    
    hexdump-field() {
      set -o pipefail
      printf '%s[%d]:\n' $1 $2
      dd count=${2}B status=none | hexdump -e $2'/1 "%3.2x"' -e '" | " '$2'/1 "%_p" "\n"'
    }
    
    inspect-tar-header-block() {
      local -a hdrstack=(
        name 100
        mode 8
        uid 8
        gid 8
        size 12
        mtime 12
        checksum 8
        typeflag 1
        linkname 100
        magic 6
        version 2
        uname 32
        gname 32
        devmajor 8
        devminor 8
        prefix 155
        pad 12
      )
      set - ${hdrstack[@]}
      while test $# -gt 0; do
        hexdump-field $1 $2 || return
        shift 2
      done
    }
    
    $ bsdtar -cf - /dev/tty /dev/null 2>&- | dd count=1 skip=1 status=none | inspect-tar-header-block
    
**提示：** 为实现“使用流式方式，将给定长度的数据从输入传输到输出”的功能，可使用[pv(1) § S,](<https://man.archlinux.org/man/pv.1#S,>)，其支持[splice(2)](<https://man.archlinux.org/man/splice.2>)系统调用。 

**注意：** 另一个替代方案是[head(1) § c](<https://man.archlinux.org/man/head.1#c>)。不过，若在glibc上使用[GNU coreutils之外的`head`实现](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#Alternatives> "Coreutils")，则[读取的输入数据量可能比指定的更多](<https://unix.stackexchange.com/a/12538#12538>)，导致在流式shell脚本中出现数据错位问题。

**提示：** 除上述介绍外，如果输入文件在流式传输前需要[lseek(2)](<https://man.archlinux.org/man/lseek.2>)到特定偏移量，并且`dd`的输出端是一个管道，且该管道连接到的程序使用[splice(2)](<https://man.archlinux.org/man/splice.2>)。那么，作为替代方案，可以考虑使用： 

  * 内置[lseek(2)](<https://man.archlinux.org/man/lseek.2>)定位功能的shell（见前之前[中的替代方案](<#%E5%8E%9F%E5%9C%B0%E9%80%90%E5%9D%97%E4%BF%AE%E8%A1%A5%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6>)）。
  * 使用类Bourne shell（例如[bash](<../zh-cn/Bash.html> "Bash")），通过使用[xxd(1) § s](<https://man.archlinux.org/man/xxd.1#s>)在shell打开的文件描述符上进行一次性[lseek(2)](<https://man.archlinux.org/man/lseek.2>)操作，

并使用[pv(1) § S,](<https://man.archlinux.org/man/pv.1#S,>)（上文已提及）。例如，下面的示例使用[bash](<../zh-cn/Bash.html> "Bash")（假设文件描述符最初未被shell分配。在bash中，可通过`ls -l /proc/self/fd`查看已分配的文件描述符）：
    
    $ bash
    
    $ exec 9<dummy-but-rather-large.img
    $ xxd -g 0 -l 0 -s $((0x47ffff)) <&9
    $ pv -qSs 104857601200 <&9 | <一个处理大量数据但不会按需限制读取长度，也不支持按偏移量读取的程序>
    $ exec 9<&-

**注意：** 如[coreutils测试套件中的一个示例](<https://github.com/coreutils/coreutils/blob/4fd708810ce0e0d967c4c14e1ff2ff7b43440b58/tests/dd/skip-seek-past-file.sh#L74>)所示，上例中的[xxd(1) § s](<https://man.archlinux.org/man/xxd.1#s>)可使用`dd`并配合`count=0`、`skip`选项代替。虽然这种用法与POSIX标准和一些非GNU实现不兼容。

###  将可引导的磁盘镜像写入块设备，并按需显示进度信息

不推荐直接将`dd`用于该用途。其它常用工具参见[U_盘安装介质#使用基本命令行工具](<../zh-cn/U_%E7%9B%98%E5%AE%89%E8%A3%85%E4%BB%8B%E8%B4%A8.html#%E4%BD%BF%E7%94%A8%E5%9F%BA%E6%9C%AC%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7> "U 盘安装介质")。 

**提示：** 若要将文件内容写入块设备，并同时显示进度信息，相比直接使用`dd`，建议使用[dd_rescue(1) § W](<https://man.archlinux.org/man/dd_rescue.1#W>)替代。若块设备中已经存储了旧版本的镜像内容，在写入新版本的镜像时，其能避免不必要的写入操作。

##  故障排除

###  部分读取：复制的数据量小于要求的大小

若`dd`在尝试进行读取操作时，一个完整的输入块暂时不可用，则输出文件的最终的大小可能比要求复制的大小要小。如[文档所述](<https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html#dd-invocation>)： 

    此外，如果未指定`conv`数据转换操作数（即本文中提到过的选项），从输入读取到的内容会立即被复制到输出，即使读取到的数据量小于块大小。

在Linux上，底层的[read(2)](<https://man.archlinux.org/man/read.2>)系统调用在从管道（[pipe(7)](<https://man.archlinux.org/man/pipe.7>)）或某些设备文件（例如`/dev/urandom`、`/dev/random`，由于[底层内核设备驱动程序硬编码的限制](<https://unix.stackexchange.com/a/178957#178957>)）读取时，可能会在读取到部分数据，数据量还未达到参数指定的值时便提前返回（即“部分读取”）。这导致在结合使用`bs`和`count=_n_`选项时，复制的数据总大小小于预期。其中`count=_n_`指定了要复制到输出的输入块的数量，但每个输入块的大小可能小于`bs`字节。 

在发生部分读取时，`dd`可能显示警告，但不保证一定会显示警告： 
    
    dd: warning: partial read (_X_ bytes); suggest iflag=fullblock
    
解决方案是依照警告的提示，在`dd`命令中添加`iflag=fullblock`输入选项。例如，要创建一个大小为40MiB、填充了随机数据的新文件： 
    
    $ dd if=/dev/urandom of=new-file-filled-by-urandom.bin bs=40M count=1 iflag=fullblock
    
**注意：** 当需要从管道或特殊设备（详见下文）中复制特定长度的一段内容时（通过`count=_n_`选项指定），强烈建议添加`iflag=fullblock`选项，特别是在[擦除](<../zh-cn/%E5%AE%89%E5%85%A8%E5%9C%B0%E6%93%A6%E9%99%A4%E7%A3%81%E7%9B%98.html> "安全地擦除磁盘")[特定文件](<../zh-cn/%E5%AE%89%E5%85%A8%E5%9C%B0%E6%93%A6%E9%99%A4%E7%A3%81%E7%9B%98/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html#%E6%93%A6%E9%99%A4%E5%8D%95%E4%B8%AA%E6%96%87%E4%BB%B6> "安全地擦除磁盘/提示和技巧")或[设备的一部分](<#%E7%A7%BB%E9%99%A4%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F>)时。

当从管道读取时，`iflag=fullblock`的[一个替代方案](<https://unix.stackexchange.com/questions/556016/cat-dd-pipe-causes-partial-reads-without-iflag-fullblock-why-truncated-to-128>)是将`bs`设置为[linux/limits.h](<https://elixir.bootlin.com/linux/latest/A/ident/PIPE_BUF>)中定义的`PIPE_BUF`常量值，以使得[pipe(7)](<https://man.archlinux.org/man/pipe.7>) I/O成为原子操作。例如，若要创建总长度为5MiB，填充了随机字母数字字符串的文本文件： 
    
    $ LC_ALL=C tr -dc '[:alnum:]' < /dev/urandom | dd of=passtext-5m.txt bs=**4k** count=1280
    
若输出文件不是管道，可使用`ibs`、`obs`选项分别为输入管道和输出文件设置块大小。例如，由于输出文件存储在磁盘上，可设置更大的块大小，以提高效率： 
    
    $ LC_ALL=C tr -dc '[:alnum:]' < /dev/urandom | dd of=passtext-5m.txt ibs=4k obs=**64k** count=1280
    
**提示：** 在某些情况下，保持输出块大小与输入块大小相同且等于`PIPE_BUF`常量定义的值，可能就已经是最佳的了。

###  总传输字节数读数错误

如果在写入输出时遇到错误（例如收到SIGPIPE信号、发生介质故障或网络块设备意外断开），命令显示的总传输字节数可能会大于实际值（“部分写入”）。如下例所示，其中第二个`dd`从输入中读取的字节数显然不会超过512200字节，但第一个`dd`实例仍然报告了复制了512400字节： 
    
    $ yes 'x' | dd bs=4096 count=512400B | dd ibs=1 count=512200 status=none >/dev/null
    125+1 records in
    125+1 records out
    512400 bytes (512 kB, 500 KiB) copied, 10.7137 s, 47.8 kB/s
    
对于类似上述例子的情况，当要恢复中断的传输时，建议以已经完整复制的输出块的数量为依据（`125+1 records out`中“+”号前面的数字，即125）。 

**注意：** 若即使添加`iflag=fullblock`选项后，部分I/O块数（“+”号后面的数字仍大于1，则说明部分I/O发生了不止一次。在这种情况下，为可靠地恢复传输进度，建议： 

  * 改用[ddrescue](</wzh/index.php?title=Ddrescue&action=edit&redlink=1> "Ddrescue（页面不存在）")重新进行传输，以更灵活地处理可能存在故障的介质上发生的部分读取。
  * 若网络连接不稳定且需要写入网络设备，使用[dd_rescue(1)](<https://man.archlinux.org/man/dd_rescue.1>)以直接I/O方式重新进行传输。
  * 避免向可能发生故障的介质写入。

##  另见

  * [dd(1p)](<https://man.archlinux.org/man/dd.1p>): POSIX specification of dd core utility in [manpage](</wzh/index.php?title=Manpage&action=edit&redlink=1> "Manpage（页面不存在）") form
