[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:SystemTap](<../zh-cn/Talk:SystemTap.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Systemtap](<https://wiki.archlinux.org/title/Systemtap> "arch:Systemtap")，最近一次同步于 2018-12-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Systemtap?diff=0&oldid=512991>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Systemtap_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Systemtap](<https://sourceware.org/systemtap/>) 是一种在运行时收集 Linux 系统信息的自由软件(GPL)框架。 

## SystemTap

安装 [systemtap](<https://aur.archlinux.org/packages/systemtap/>)AUR 或 [systemtap-git](<https://aur.archlinux.org/packages/systemtap-git/>)AUR。和上游版本的对比：[[1]](<https://sourceware.org/systemtap/wiki/SystemTapReleases>). 

要从源代码编译，请访问[这里](<https://sourceware.org/git/?p=systemtap.git;a=summary>)。最新代码会包含新内核版本和发行版的支持。 

##  标准内核

至少需要安装软件包 [linux-headers](<https://archlinux.org/packages/?name=linux-headers>)包。 

Arch 会从发布的二进制文件,包括内核中删除调试数据。很多 systmetap 功能就不能使用了。[stapprobes 手册](<https://sourceware.org/systemtap/man/stapprobes.3stap.html>)记录了 NON-DWARF 和 AUTO-DWARF 类型下什么功能可用： 

  * kernel tracepoints: kernel.trace("*")
  * user-space probes: process("...").function("...") (for programs you build yourself with -g)
  * user-space markers: process("...").mark("...") (if they were configured with the _< sys/sdt.h>_ markers)
  * perfctr-based probes: perf.*
  * non-dwarf kernel probes: kprobe.function("...") and nd_syscall.* tapset (if a /boot/System.map* file is available, see below).

##  内核重新编译

可用自定义 _linux-custom_ 软件包之后再运行 SystemTap。重新编译 [linux](<https://archlinux.org/packages/?name=linux>)包 软件包也非常方便。参考 [Kernels/Traditional compilation](</wzh/index.php?title=Kernels/Traditional_compilation&action=edit&redlink=1> "Kernels/Traditional compilation（页面不存在）")。 

###  准备

首先，运行 `cd ~/ && mkdir build && cd build/ && asp checkout linux && cd linux/trunk` 来获取原始内核构建文件。然后使用 `makepkg --verifysource` 获取附加文件。通过执行验证，您可以安全地跳过“更新校验和”步骤。 

###  修改config文件

编辑 **config** (32位内核) 或 **config.x86_64** (64位内核), 确保打开这些选项: 

  * CONFIG_KPROBES=y
  * CONFIG_KPROBES_SANITY_TEST=n
  * CONFIG_KPROBE_EVENT=y
  * CONFIG_NET_DCCPPROBE=m
  * CONFIG_NET_SCTPPROBE=m
  * CONFIG_NET_TCPPROBE=y
  * CONFIG_DEBUG_INFO=y
  * CONFIG_DEBUG_INFO_REDUCED=n
  * CONFIG_X86_DECODER_SELFTEST=n
  * CONFIG_DEBUG_INFO_VTA=y

默认只有 _CONFIG_DEBUG_INFO_ 和 _CONFIG_DEBUG_INFO_REDUCED_ 没被打开，修改这两个即可. 

###  更新校验值

执行 `md5sum config[.x86_64]` 获得新的文件校验值. 

编辑 **PKGBUILD** 文件, 这一部分 `md5sums=('sum-of-first' ... 'sum-of-last')` 和这一部分 `source=('first-source' ... 'last-source')` 是个数相同，顺序相同的, 把新获得的校验值在合适的位置替换. 

`makepkg --skipchecksums` 使用命令可以跳过校验，但这样做对其它文件（比如下载的内核源码包）来说不安全，**因此建议按这里给出的方法操作** 。 

###  编译并安装

可选步骤: 可以在 `/etc/makepkg.conf` 文件中设置 `MAKEFLAGS="-j16"` 加速编译. 

执行 `makepkg` 开始编译, 然后 `sudo pacman -U *.pkg.tar.gz` 安装编译好的包. **pacman** 会提示你这是重新安装 （**reinstall** ）, 这就对了！ 

[linux](<https://archlinux.org/packages/?name=linux>)包 和 [linux-headers](<https://archlinux.org/packages/?name=linux-headers>)包 需要安, [linux-docs](<https://archlinux.org/packages/?name=linux-docs>)包 则随意. 

通过这个方法, 外部内核模块 (例如 [nvidia](<https://archlinux.org/packages/?name=nvidia>)包 和 [virtualbox](<https://archlinux.org/packages/?name=virtualbox>)包) 就不需要被重新编译了. 

### Systemtap

从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中安装systemtap即可: [systemtap](<https://aur.archlinux.org/packages/systemtap/>)AUR, 完成. 

##  编译自定义内核

参考这个[官方README](<https://sourceware.org/git/?p=systemtap.git;a=blob_plain;f=README;hb=HEAD>)

##  问题处理

###  版本匹配问题

如果出现如下错误： 
    
       /usr/share/systemtap/runtime/stat.c:214:2: error: 'cpu_possible_map' undeclared (first use in this function)
    
请安装 systemtap-git。 

###  System.map丢失

你可以再启用 DEBUG_INFO 的情况下构建Linux内核时恢复它： 
    
       cp src/linux-3.6/System.map /boot/System.map-3.6.7-1-ARCH
    
或者执行以下命令， 
    
       sudo cp /proc/kallsyms /boot/System.map-`uname -r`
    
### Process return probes not available

如果你确定内核配置正确，但再启动 `stap` 时收到以下两条信息： 
    
       WARNING: Kernel function symbol table missing [man warning::symbols]
    
       semantic error: process return probes not available [man error::inode-uprobes]
    
那么SystemTap可能未能验证此功能的支持，你可以在 [System.map丢失](<#System.map%E4%B8%A2%E5%A4%B1>)这个步骤中解决此问题。 
