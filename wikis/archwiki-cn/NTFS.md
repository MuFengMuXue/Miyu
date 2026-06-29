相关文章

  * [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")
  * [NTFS-3G](<../zh-cn/NTFS-3G.html> "NTFS-3G")
  * [Ufsd](</wzh/index.php?title=Ufsd&action=edit&redlink=1> "Ufsd（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [NTFS](<https://wiki.archlinux.org/title/NTFS> "arch:NTFS")，最近一次同步于 2025-11-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/NTFS?diff=0&oldid=850180>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/NTFS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

来自[维基百科](<https://en.wikipedia.org/wiki/NTFS> "wikipedia:NTFS")： 

     **NTFS (New Technology File System)** 是一个由微软开发的专有日志文件系统。从 Windows NT 3.1 开始是 Windows NT 系列的默认文件系统。

[ntfs3](<https://docs.kernel.org/filesystems/ntfs3.html>) 内核驱动提供了读写支持。 

内核驱动并没有配套的用户空间工具，因此仍需使用 Windows 机器或 [NTFS-3G](<../zh-cn/NTFS-3G.html> "NTFS-3G") 等外部工具来格式化分区或进行维护。 

##  提示与技巧

###  提高性能

你可以启用为 [mount(8)](<https://man.archlinux.org/man/mount.8>) 启用 `prealloc` 选项来为并行写入操作减少碎片（对机械硬盘更有用）。 

###  防止创建 Windows 不支持的命名

NTFS 本身对字符和名称没有限制，但 [Windows 对此有限制](<https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file#naming-conventions>)。 

从内核版本 6.2 开始，ntfs3 支持 `windows_names` [mount(8)](<https://man.archlinux.org/man/mount.8>) 选项。使用该选项可严格保证兼容性。 

**提示：**[udisks](<../zh-cn/Udisks.html> "Udisks") 默认启用该选项。

##  已知问题

###  挂载时需要明确的文件系统类型

`ntfs3` 挂载时需要明确的文件系统类型，否则可能会将文件系统挂载为只读，详见[#文件系统挂载为只读](<#%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E6%8C%82%E8%BD%BD%E4%B8%BA%E5%8F%AA%E8%AF%BB>)。 

要挂载文件系统，请将其类型指定为 `ntfs3`。例如，使用 [mount(8)](<https://man.archlinux.org/man/mount.8>) 的 `-t`/`--types` 选项： 
    
    # mount -t ntfs3 /dev/_sdxY_ _/mnt_
    
##  排障

###  文件系统挂载为只读

[linux](<https://archlinux.org/packages/?name=linux>)包提供的内核启用了`CONFIG_NTFS_FS`兼容性选项 [[1]](<https://gitlab.archlinux.org/archlinux/packaging/packages/linux/-/commit/ec29b86317f1c6c2e6c698684a4cc149bd492f9d>)。它会模仿旧版驱动的行为，把挂载选项中文件系统类型为`ntfs`的文件系统挂载为只读。 

要挂载文件系统为可读写，请使用`ntfs3`类型。详见[#挂载时需要明确的文件系统类型](<#%E6%8C%82%E8%BD%BD%E6%97%B6%E9%9C%80%E8%A6%81%E6%98%8E%E7%A1%AE%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E7%B1%BB%E5%9E%8B>)。 

###  unknown filesystem type 'ntfs'

[挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载") NTFS 时，可能会遇到如下错误： 
    
    mount: _/mnt_ : unknown filesystem type 'ntfs'
    
请检查是否已安装 ntfs-3g： 
    
    $ pacman -Qi ntfs-3g
    
如果尚未安装，可[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")之。也可以使用 `-t ntfs3` 参数来指定使用内核的 ntfs3 驱动。 

若将 `ntfs3` 作为 `ntfs` 分区的默认驱动程序，那么 [udev](<../zh-cn/Udev.html> "Udev") 规则可以解决问题： 
    
    /etc/udev/rules.d/ntfs3_by_default.rules
    
    SUBSYSTEM=="block", ENV{ID_FS_TYPE}=="ntfs", ENV{ID_FS_TYPE}="ntfs3"

不过这仅为一种方法而非建议，并且可能弄晕一些第三方工具。 

###  无法用 ntfs3 挂载被标记为脏的分区

尝试挂载一个正常的 NTFS 分区时（成功地使用 NTFS-3G 挂载，执行 `ntfsfix --no-action` 不汇报任何错误时），你可能会获得下面的错误： 
    
    mount: _/mnt_ : wrong fs type, bad option, bad superblock on _/dev/sdb1_ , missing codepage or helper program, or other error.
           dmesg(1) may have more information after failed mount system call.
    
当分区被标记为“脏的”时，ntfs3 将不会挂载它。`dmesg` 会帮助你判断这个情况，会说： 
    
    _sdb1_ : volume is dirty and "force" flag is not set!
    
你可以尝试用 `--clear-dirty` 参数来使用 {[ntfsfix(8)](<https://man.archlinux.org/man/ntfsfix.8>) 来清理它。 [[2]](<https://bbs.archlinux.org/viewtopic.php?id=271650>)

##  参见

  * [NTFS3 内核文档](<https://docs.kernel.org/filesystems/ntfs3.html>)
  * [NTFS3 驱动 FAQ](<https://www.paragon-software.com/home/ntfs3-driver-faq/>) – Paragon Software Group
  * [NTFS3 性能比较](<https://openbenchmarking.org/result/2009092-NE-NTFSCOMPA56>)
