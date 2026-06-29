相关文章

  * [多引导 USB 设备](<../zh-cn/%E5%A4%9A%E5%BC%95%E5%AF%BC_USB_%E8%AE%BE%E5%A4%87.html> "多引导 USB 设备")

**翻译状态：**

  * 本文（或部分内容）译自 [Ventoy](<https://wiki.archlinux.org/title/Ventoy> "arch:Ventoy")，最近一次同步于 2024-07-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ventoy?diff=0&oldid=812538>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ventoy_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Ventoy](<https://www.ventoy.net/cn/index.html>) 是一个免费且开源的引导工具，您可以在驱动器分区上复写 EFI，IMG，ISO，VHD(x) 或者 WIM 文件，而后选择、引导。 

支持绝大多数的操作系统（Windows/WinPE/Linux/ChromeOS/Unix/VMware/Xen 等）。参见[全表](<https://www.ventoy.net/cn/isolist.html>)。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ventoy-bin](<https://aur.archlinux.org/packages/ventoy-bin/>)AUR 或 [ventoy](<https://aur.archlinux.org/packages/ventoy/>)AUR 软件包。 

##  使用方法

**警告：** Ventoy 安装时会擦除驱动器上所有数据。

安装媒介有三个实用工具： 

  1. `/opt/ventoy/Ventoy2Disk.sh`：从命令行运行的 shell 脚本。
  2. `/opt/ventoy/VentoyGUI.x86_64`：图形化程序。若程序不能以 root 权限启动，需要 `xauth` 或类似程序以提升权限。
  3. 用网络浏览器打开 `file:///opt/ventoy/WebUI/index.html`。

这些实用工具同样可以用来升级驱动器上的 Ventoy 安装。 

Ventoy 在驱动器上创建两个分区。默认名 Ventoy 和 VTOYEFI。Ventoy 分区用于储存可引导镜像（iso 文件），以及其他数据。VTOYEFI 存储 Ventoy 的二进制文件。 

欲添加要引导的镜像，[挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Mount") Ventoy 分区，将镜像复制过去。 

**提示：** 您可以将镜像复制到 Ventoy 分区任意目录下，它们没有必要放在根目录下或放一起。

###  无安装的使用

如果您只是想要创建一个多引导的驱动器，您仅需在 [Github releases 页面](<https://github.com/ventoy/Ventoy/releases>)下载预构建的可执行文件。您需要 [dosfstools](<https://archlinux.org/packages/?name=dosfstools>)包 以安装，因为 vfat 分区是由 _mkfs.vfat_ 创建的。核对 sha256 校验和并解压后，您可以运行不带参数的 shell 脚本来显示附带的 CLI（终端用户接口）[[1]](<https://www.ventoy.net/en/doc_start.html>) 帮助页面： 
    
    # ./ventoy-_VERSION_ /Ventoy2Disk.sh
    
然后，您可以执行相似过程以将驱动器升级到未来版本。下载新版文件，校验、解压并执行： 
    
    # ./ventoy-_NEWER-VERSION_ /Ventoy2Disk.sh
    
遵从提供的帮助信息。 

对此处提到的 shell 脚本有一个替代品，包括一个 [GTK](<../zh-cn/GTK.html> "GTK")/[qt](<../zh-cn/Qt.html> "Qt")[[2]](<https://www.ventoy.net/en/doc_linux_gui.html>)图形化用户接口，以及一个 [web](</wzh/index.php?title=Web&action=edit&redlink=1> "Web（页面不存在）") 用户接口[[3]](<https://www.ventoy.net/en/doc_linux_webui.html>)。 

##  锦囊妙计

###  如何查看已安装的版本？

用上文提及的 `Ventoy2Disk.sh` 实用工具，启动更新过程 (`-u`)，但别确认更新：确认更新前，它会告诉你当前版本。 

###  校验文件

如[上游文档](<https://www.ventoy.net/en/doc_checksum.html>)所述，有一个内置的校验实用工具可以校验文件。 

##  参见

  * [Ventoy 文档](<https://www.ventoy.net/en/doc_start.html>)
  * [Wikipedia:Ventoy](<https://en.wikipedia.org/wiki/Ventoy> "wikipedia:Ventoy")
