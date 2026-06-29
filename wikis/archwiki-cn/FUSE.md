**翻译状态：**

  * 本文（或部分内容）译自 [FUSE](<https://wiki.archlinux.org/title/FUSE> "arch:FUSE")，最近一次同步于 2024-05-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/FUSE?diff=0&oldid=804465>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/FUSE_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [File systems](<../zh-cn/File_systems.html> "File systems")

[用户空间中的文件系统 (Filesystem in Userspace)](<https://en.wikipedia.org/wiki/Filesystem_in_Userspace> "wikipedia:Filesystem in Userspace") (FUSE) 是一种用于类 Unix 操作系统的机制，它使非特权用户可以创建自己的文件系统而无需编辑内核代码。这是通过在用户空间中运行文件系统代码来实现的，而 FUSE 内核模块仅提供了到实际内核接口的“桥梁”。 

##  卸载

可以使用 [fuse3](<https://archlinux.org/packages/?name=fuse3>)包 提供的 [fusermount3(1)](<https://man.archlinux.org/man/fusermount3.1>) 或 [fuse2](<https://archlinux.org/packages/?name=fuse2>)包 提供的 [fusermount(1)](<https://man.archlinux.org/man/fusermount.1>) 卸载 FUSE 文件系统。例如： 
    
    $ fusermount3 -u _mountpoint_
    
##  FUSE 文件系统列表

  * **adbfs-rootless** — 挂载通过 USB 连接的 Android 设备。

     <https://github.com/spion/adbfs-rootless> || [adbfs-rootless-git](<https://aur.archlinux.org/packages/adbfs-rootless-git/>)AUR

  * **apfs-fuse** — 用于 APFS（Apple 文件系统 (Apple File System)）的 FUSE 驱动程序。

     <https://github.com/sgan81/apfs-fuse> || [apfs-fuse-git](<https://aur.archlinux.org/packages/apfs-fuse-git/>)AUR

  * **astreamfs** — 异步流式 fuse 文件系统。(A(synchronous) Stream(ing) (fuse) F(ile)S(ystem))

     <https://gitlab.com/BylonAkila/astreamfs/tree/master> || [astreamfs-git](<https://aur.archlinux.org/packages/astreamfs-git/>)AUR

  * **AVFS** — 虚拟文件系统，可浏览压缩文件（档案）。

     <https://avf.sourceforge.net> || [avfs](<https://archlinux.org/packages/?name=avfs>)包

  * **[CurlFtpFS](<../zh-cn/CurlFtpFS.html> "CurlFtpFS")** — 基于 FUSE 和 libcurl 的用于访问 FTP 主机的文件系统。

     <https://curlftpfs.sourceforge.net/> || [curlftpfs](<https://archlinux.org/packages/?name=curlftpfs>)包

  * **[davfs2](<../zh-cn/Davfs2.html> "Davfs2")** — 文件系统驱动程序，可让您挂载 WebDAV 文件夹。

     <https://savannah.nongnu.org/projects/davfs2> || [davfs2](<https://aur.archlinux.org/packages/davfs2/>)AUR

  * **[EncFS](</wzh/index.php?title=EncFS&action=edit&redlink=1> "EncFS（页面不存在）")** — 用户空间可堆叠加密文件系统。

     <https://vgough.github.io/encfs/> || [encfs](<https://archlinux.org/packages/?name=encfs>)包

  * **fuse-archive** — 将存档或压缩文件作为只读 FUSE 文件系统提供服务。

     <https://github.com/google/fuse-archive> || [fuse-archive](<https://aur.archlinux.org/packages/fuse-archive/>)AUR

  * **fuseiso** — 以普通用户身份挂载 ISO。

     <https://sourceforge.net/projects/fuseiso/> || [fuseiso](<https://archlinux.org/packages/?name=fuseiso>)包

  * **GDriveFS** — 用于 Google Drive 的创新型 FUSE 包装器。

     <https://github.com/dsoprea/GDriveFS> || [gdrivefs](<https://aur.archlinux.org/packages/gdrivefs/>)AUR

  * **[gitfs](<../zh-cn/Gitfs.html> "Gitfs")** — gitfs 是与 git 完全集成的 FUSE 文件系统。

     <https://www.presslabs.com/gitfs/> || [gitfs](<https://aur.archlinux.org/packages/gitfs/>)AUR

  * **[gocryptfs](</wzh/index.php?title=Gocryptfs&action=edit&redlink=1> "Gocryptfs（页面不存在）")** — gocryptfs 是一个用户空间可堆叠的加密文件系统。

     <https://nuetzlich.net/gocryptfs/> || [gocryptfs](<https://archlinux.org/packages/?name=gocryptfs>)包

  * **google-drive-ocamlfuse** — 使用 OCaml 编写的 Google Drive 支持的基于 FUSE 的文件系统。

     <https://astrada.github.io/google-drive-ocamlfuse/> || [google-drive-ocamlfuse](<https://aur.archlinux.org/packages/google-drive-ocamlfuse/>)AUR

  * **gphotofs** — 将相机作为文件系统挂载的 FUSE 模块。

     <http://www.gphoto.org/proj/gphotofs/> || [gphotofs](<https://aur.archlinux.org/packages/gphotofs/>)AUR

  * **HubicFuse** — 用于访问 HubiC 云存储的 FUSE 文件系统。

     <https://github.com/TurboGit/hubicfuse> || [hubicfuse](<https://aur.archlinux.org/packages/hubicfuse/>)AUR

  * **iFuse** — 用于访问 iPhone 或 iPod Touch 内容的 FUSE 文件系统。

     <https://libimobiledevice.org/> || [ifuse](<https://archlinux.org/packages/?name=ifuse>)包

  * **[NTFS-3G](<../zh-cn/NTFS-3G.html> "NTFS-3G")** — 具有扩展功能的 NTFS 驱动程序。

     <https://github.com/tuxera/ntfs-3g> || [ntfs-3g](<https://archlinux.org/packages/?name=ntfs-3g>)包

  * **s3fs** — 由 Amazon S3 支持的基于 FUSE 的文件系统。

     <https://github.com/s3fs-fuse/s3fs-fuse> || [s3fs-fuse](<https://archlinux.org/packages/?name=s3fs-fuse>)包

  * **splitviewfuse** — 将文件拆分/合并为段的目录视图。

     <https://github.com/seiferma/splitviewfuse> || [splitviewfuse](<https://aur.archlinux.org/packages/splitviewfuse/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

  * **[SSHFS](<../zh-cn/SSHFS.html> "SSHFS")** — 基于 FUSE 的文件系统客户端，用于通过 SSH 挂载目录。

     <https://github.com/libfuse/sshfs> || [sshfs](<https://archlinux.org/packages/?name=sshfs>)包

  * **TMSU** — 一种命令行工具，用于标记文件并通过虚拟文件系统访问它们。

     <https://tmsu.org/> || [tmsu](<https://aur.archlinux.org/packages/tmsu/>)AUR

  * **vdfuse** — 挂载 VirtualBox 磁盘映像 (VDI/VMDK/VHD)。

     <https://github.com/muflone/virtualbox-includes> || [vdfuse](<https://aur.archlinux.org/packages/vdfuse/>)AUR

  * **vramfs** — 基于 VRAM 的文件系统。

     <https://github.com/Overv/vramfs> || [vramfs-git](<https://aur.archlinux.org/packages/vramfs-git/>)AUR

  * **wimmount** — 挂载 Windows 映像格式 (WIM) 映像。

     <https://wimlib.net/> || [wimlib](<https://archlinux.org/packages/?name=wimlib>)包

  * **xbfuse** — 挂载 Xbox (360) 的 ISO。

     <https://multimedia.cx/xbfuse/> || [xbfuse-git](<https://aur.archlinux.org/packages/xbfuse-git/>)AUR

  * **xmlfs** — 将 XML 文件表示为易于访问的目录结构。

     <https://github.com/halhen/xmlfs> || [xmlfs](<https://aur.archlinux.org/packages/xmlfs/>)AUR

  * [媒体传输协议#FUSE 文件系统](<../zh-cn/%E5%AA%92%E4%BD%93%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE.html#FUSE_%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "媒体传输协议")

##  另请参见

  * [Wikipedia:Filesystem in Userspace#Applications](<https://en.wikipedia.org/wiki/Filesystem_in_Userspace#Applications> "wikipedia:Filesystem in Userspace")
