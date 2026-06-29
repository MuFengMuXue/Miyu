**翻译状态：**

  * 本文（或部分内容）译自 [F2FS](<https://wiki.archlinux.org/title/F2FS> "arch:F2FS")，最近一次同步于 2022-08-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/F2FS?diff=0&oldid=733959>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/F2FS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [File systems](<../zh-cn/File_systems.html> "File systems")

[F2FS](<https://en.wikipedia.org/wiki/F2FS> "wikipedia:F2FS") (Flash-Friendly File System) 是一个为配备了 Flash Transition Layer 的 NAND 闪存开发的文件系统，与 JFFS 或 UBIFS 不同，它依靠 FTL 来处理写入分发。 Linux从内核3.8开始支持 F2FS 。 

**警告：** 若运行的内核版本比创建F2FS文件系统的内核版本低，则文件系统可能无法使用。例如，使用[linux](<https://archlinux.org/packages/?name=linux>)包提供的内核创建文件系统，当系统需要降级到[linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包提供的内核时，就可能出现问题。详见[FS#69363](<https://bugs.archlinux.org/task/69363>)。

##  已知问题

###  fsck错误

F2FS的fsck不完善，可能在系统突然断电后导致数据丢失[[1]](<https://www.usenix.org/system/files/atc19-jaffer.pdf>)[[2]](<https://web.archive.org/web/20200925120546/https://archived.forum.manjaro.org/t/record-fsync-data-failed-on-f2fs-file-system-how-to-fix-foregt-the-help-i-reinstalled-its-just-easier/121051>)。 

如果经常遭遇突然断电，建议使用其它[文件系统](<../zh-cn/File_systems.html> "File systems")。 

###  GRUB 支持

尽管GRUB从2.0.4版本开始就支持F2FS，但它无法从启用了`extra_attr`flag的F2FS分区中正确读取启动文件。（详见[GRUB#不支持的文件系统](<../zh-cn/GRUB.html#%E4%B8%8D%E6%94%AF%E6%8C%81%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "GRUB")） 

##  创建 F2FS 文件系统

本文假定设备已[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning")。 

首先，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[f2fs-tools](<https://archlinux.org/packages/?name=f2fs-tools>)包软件包。 

用`mkfs.f2fs`命令创建一个文件系统（` _/dev/sdxY_` 是想要设置成 F2FS 的分区。）： 
    
    # mkfs.f2fs -l mylabel -O extra_attr,inode_checksum,sb_checksum _/dev/sdxY_
    
**注意：** 推荐至少要设置上例中的选项，这些选项能帮助`f2fs.fsck`检测并修复某些文件系统损坏。对于所有可用的选项，见[mkfs.f2fs(8)](<https://man.archlinux.org/man/mkfs.f2fs.8>)。

###  压缩

**注意：** 与其它支持inline compression的文件系统不同，F2FS的压缩默认情况下并不会提供额外的可用空间。不论是否启用压缩，F2FS都会保留相同数目的block，这主要是为了减少写入放大以延长闪存寿命，同时可能带来[微小的性能提升](<https://lz4.github.io/lz4/>)。详见内核文档中的[Compression Implementation](<https://docs.kernel.org/filesystems/f2fs.html#compression-implementation>)。可以通过iotcl系统调用传递`F2FS_IOC_RELEASE_COMPRESS_BLOCKS`命令将对应文件未使用的空间暴露出来，但这将使该文件不可变。

要使用压缩，添加`compression`选项，例如： 
    
    # mkfs.f2fs -l mylabel -O extra_attr,inode_checksum,sb_checksum,**compression** _/dev/sdxY_
    
挂载文件系统时，指定`compress_algorithm=(lzo|lz4|zstd|lzo-rle)`挂载选项。此外，`compress_extension=txt`挂载选项可自动压缩所有创建的txt文件。 

要指定F2FS压缩某一文件或目录，使用： 
    
    $ chattr -R +c [FOLDER]
    
###  文件层面的加密

从Linux内核4.2开始，F2FS原生支持文件加密。F2FS的加密是目录层级的，不同的目录可以使用不同的密钥。这不同于 [dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt")（块设备层级）或[eCryptfs](</wzh/index.php?title=ECryptfs&action=edit&redlink=1> "ECryptfs（页面不存在）")（嵌套在已有文件系统上）。要使用F2FS的原生加密支持，用如下命令创建文件系统： 
    
     # mkfs.f2fs -l mylabel -O extra_attr,inode_checksum,sb_checksum,**encrypt** _/dev/sdxY_
    
对于已有的文件系统，可使用`fsck.f2fs -O encrypt /dev/sdxY`启用加密。关于如何使用加密，见[fscrypt](</wzh/index.php?title=Fscrypt&action=edit&redlink=1> "Fscrypt（页面不存在）")。 

##  挂载F2FS文件系统

既可以手动挂载文件系统，也可以使用其它挂载机制： 
    
    # mount /dev/sdxY /mnt/foo
    
###  推荐的挂载选项

因为F2FS是设计为在闪存设备上使用的，建议启用压缩。要启用压缩，必须在使用`mkfs.f2fs`创建文件系统时就指定相应选项。 可以使用以下挂载选项略微提升性能： 
    
    # mount -o compress_algorithm=zstd:6,compress_chksum,atgc,gc_merge,lazytime /dev/sdxY /mnt/foo
    
  * `compress_algorithm=zstd:6`：使用[zstd](<https://en.wikipedia.org/wiki/Zstandard> "w:Zstandard")压缩等级6进行压缩, 可提供很好的压缩率。
  * `compress_chksum`：使用校验码检查压缩的block，可防止数据损坏。
  * `atgc,gc_merge`：启用更好的GC方式，异步执行某些前台GC。
  * `lazytime`：不使用同步方式更新文件的访问与修改时间，可提升IO性能与闪存寿命。

###  discard实现方式

默认情况下，F2FS使用混合型TRIM模式（类似[continuous TRIM](<../zh-cn/Solid_state_drive.html#Continuous_TRIM> "Solid state drive")）。该实现方式使用异步的discard线程来缓解RW IO的高discard延迟。其在内存中维护一个discard操作的等待队列，并在空闲时执行它们（详见[[3]](<https://sourceforge.net/p/linux-f2fs/mailman/message/36957687>)）。若要使用[periodic TRIM](<../zh-cn/Solid_state_drive.html#Periodic_TRIM> "Solid state drive")，则需要指定`nodiscard`挂载选项。 

##  检查与修复

检查与修复F2FS文件系统需要使用[f2fs-tools](<https://archlinux.org/packages/?name=f2fs-tools>)包提供的`fsck.f2fs`工具。要检查一个F2FS文件系统，执行： 
    
    # fsck.f2fs _/dev/sdxY_
    
根据结果选择不同的选项来修复不一致问题（详见[fsck.f2fs(8)](<https://man.archlinux.org/man/fsck.f2fs.8>)），例如： 
    
    # fsck.f2fs -f _/dev/sdxY_
    
##  扩容 F2FS 文件系统

如果文件系统未被挂载，且对应的分区已经被拓展，则可以扩容文件系统。[但目前不支持收缩](<https://lore.kernel.org/linux-f2fs-devel/1461630518-16944-1-git-send-email-jaegeuk@kernel.org/>)。 首先使用[分区工具](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E5%B7%A5%E5%85%B7> "Partitioning")调整分区大小。例如，假设`parted`控制台中`print`命令的输出如下： 
    
    Number  Start   End     Size        File system     Name                  Flag
     1      1049kB  106MB   105MB       fat32           EFI system partition  boot, esp
     2      106MB   11,0GB  10,9GB      ext4
     3      11,0GB  12,3GB  1322MB      f2fs
     4      31,0GB  31,3GB  261MB       ext4
    
要调整使得`f2fs`对应分区（3号）占据4号分区前的所有空闲空间，执行`resizepart 3 31GB`。使用`exit`退出`parted`。 

然后扩容文件系统来填充新的分区，使用以下命令: 
    
    # resize.f2fs /dev/sdxY
    
`_/dev/sdxY_`是要扩容的 F2FS 分区。可用的选项见 [resize.f2fs(8)](<https://man.archlinux.org/man/resize.f2fs.8>)。 

**注意：** 如果使用 GPT，分区的 GUID (可通过`/dev/disk/by-partuuid/`查看) 可能会改变，但是文件系统的 UUID (可通过`/dev/disk/by-uuid/`查看) 应该保持不变。
