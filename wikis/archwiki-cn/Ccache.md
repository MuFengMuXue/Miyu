**翻译状态：**

  * 本文（或部分内容）译自 [Ccache](<https://wiki.archlinux.org/title/Ccache> "arch:Ccache")，最近一次同步于 2022-10-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ccache?diff=0&oldid=720873>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ccache_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Ccache](<https://ccache.dev/>) 是一个编译器的包装，它将已编译的二进制文件存储在指定位置，并将其提供给用户，以加快同一代码的重新编译。虽然第一次编译程序可能要时间长些，但随后的编译会快得多，因为不需要进行重复编译，只需要对之前存储的二进制文件进行查找。`ccache` 与 [GCC](<../zh-cn/GNU_Compiler_Collection.html> "GCC") 和 [Clang](<../zh-cn/Clang.html> "Clang") 兼容。 

##  安装

[安装](<../zh-cn/Pacman.html> "Pacman")位于[官方软件仓库](<../zh-cn/Official_repositories.html> "Official repositories")的 [ccache](<https://archlinux.org/packages/?name=ccache>)包 软件包。 

##  配置

可以用配置文件修改默认行为，优先级由高到低为: 

  1. 环境变量
  2. 单个 Cache 的配置文件 (`$HOME/.config/ccache/ccache.conf`)
  3. 系统配置文件 (`/etc/ccache.conf`)

详见 [ccache(1)](<https://man.archlinux.org/man/ccache.1>)。 

###  为 makepkg 启用 ccache

要在 makepkg 启用 _ccache_ ，请编辑 `/etc/makepkg.conf`. 在 `BUILDENV` 中删除 ccache 前的感叹号： 
    
     BUILDENV=(fakeroot !distcc color ccache !xdelta)
    
###  在命令行中启用

如果要从中命令行编译而不是生成软件包，同样可以使用 _ccache_ 提高速度。 

为此，你可以在每个编译命令前加上 `ccache`。 
    
    $ ccache cc hello_world.c
    
或者修改你的 `$PATH`，在编译器的路径之前加上 _ccache_ 的二进制文件目录。 
    
    export PATH="/usr/lib/ccache/bin/:$PATH"
    
你他可以把它设置到你的环境变量里，方便多次使用。 

**注意：** 如果用这个方法，将同时对 _makepkg_ 启用 _ccache_ 。

###  启用 colorgcc 支持

由于 colorgcc 也是一个编译器的包装，所以需要确保包装的调用顺序是正确的。 
    
    export PATH="/usr/lib/colorgcc/bin/:$PATH"    # 按照正常安装 colorgcc 的情况保持不变（不要添加 _ccache_ ）
    
    export CCACHE_PATH="/usr/bin"                 # 告诉 _ccache_ 只使用这里的编译器
    
_colorgcc_ 需要调用 _ccache_ 而不是真正的编译器。编辑 `/etc/colorgcc/colorgccrc` 修改所有 `/usr/bin` 路径为 `/usr/lib/ccache/bin`： 
    
    /etc/colorgcc/colorgccrc
    
    g++: /usr/lib/ccache/bin/g++
    gcc: /usr/lib/ccache/bin/gcc
    c++: /usr/lib/ccache/bin/g++
    cc: /usr/lib/ccache/bin/gcc
    g77:/usr/bin/g77
    f77:/usr/bin/g77
    gcj:/usr/bin/gcj
    
新版本的 _ccache_ 在设置 `GCC_COLORS` 时，将始终为GCC启用颜色支持，同时 Clang 默认启动多色输出。如果输出对象不是 TTY， _ccache_ 会让编译器生成颜色，将它们保存在缓存中，但从输出中剥离。在统一 [-fdiagnostics-color](<https://github.com/ccache/ccache/issues/224>) 方面仍然存在一些问题。 

## Misc

**注意：** 此章节未进行翻译。

###  修改缓存目录

可以将缓存目录 `~/.cache/.ccache` 配置到其它地方，例如 SSD 或 [ramdisk](</wzh/index.php?title=Ramdisk&action=edit&redlink=1> "Ramdisk（页面不存在）"): 

要在修改当前 shell 的缓存目录： 
    
    $ export CCACHE_DIR=/ramdisk/ccache
    
要修改默认缓存目录： 
    
    ~/.config/.ccache/ccache.conf
    
    cache_dir = /ramdisk/ccache

###  设置最大缓存大小

默认值是 5G，可以通过配置修改： 
    
    /home/<user>/.ccache/ccache.conf
    
    max_size = 2.0G

###  通过环境变量禁用缓存

如果你想只在当前的shell中禁用 _ccache_ : 
    
     $ export CCACHE_DISABLE=1
    
### CLI

此外可以使用 ‘’ccache‘’ 命令行工具。 

显示统计数据: 
    
    $ ccache -s
    
清空缓存: 
    
    $ ccache -C
    
### makechrootpkg
    
    [devtools](<https://archlinux.org/packages/?name=devtools>)包 中 makechrootpkg 也可以使用 _ccache_ ，要在清理 chroot 后保留缓存，可以使用 _makechrootpkg_ 的 -d 选项将 cache 目录从普通系统绑定到 chroot: 
    $ mkdir /path/of/chroot/ccache
    
    $ makechrootpkg -d /path/to/cache/:/ccache -r /path/of/chroot -- CCACHE_DIR=/ccache
    
这样 chroot 中就可以和正常系统中一样配置和使用 _ccache_. 

##  注意事项

_ccache_ 只有在编译 _完全相同_ 的源代码时才有效。(或者说是预处理过的源码） 

在 Gentoo Linux 社区，一个基于源代码的发行版， _ccache_ 因其安慰剂效应、编译失败（由于不受欢迎的遗留对象）等而臭名昭著。Gentoo要求在报告编译失败之前关闭 _ccache_ 。参见 [Gentoo:Handbook:Parts/Working/Features#Caching compilation objects](<https://wiki.gentoo.org/wiki/Handbook:Parts/Working/Features#Caching_compilation_objects> "gentoo:Handbook:Parts/Working/Features") 和 [the blog post](<https://flameeyes.blog/2008/06/21/debunking-ccache-myths/>) 题为 "Debunking ccache myths"，作者是 Diego Pettenò，一位前 Gentoo 开发者。 

##  参阅

  * [ccache manual](<https://ccache.dev/manual/latest.html>)
