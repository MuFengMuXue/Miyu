**翻译状态：**

  * 本文（或部分内容）译自 [Pacman/Pacnew and Pacsave](<https://wiki.archlinux.org/title/Pacman/Pacnew_and_Pacsave> "arch:Pacman/Pacnew and Pacsave")，最近一次同步于 2024-10-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/Pacman/Pacnew_and_Pacsave?diff=0&oldid=802868>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Pacman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Pacnew_and_Pacsave_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

在使用 pacman 移除一个带有配置文档的软件包时，pacman 通常会将配置文档复制为一个后缀名为 `.pacsave` 的备份文档。 

同样的，当 pacman 升级一个软件包，而新软件包含有与与当前配置不同的新配置文件时，pacman 会将新配置写入 `pacnew` 文件。当写入这些文件时，pacman 会输出提示信息。 

##  为什么会创建这些文件

当升级某个软件包（命令为 `pacman -Syu`，`pacman -Su` 或者`pacman -U`）时，可能会创建一个 `.pacnew` 文件，以避免覆盖一个之前被用户修改过的已存在文件。此时，pacman会输出如下信息： 
    
    warning: /etc/pam.d/usermod installed as /etc/pam.d/usermod.pacnew
    
当卸载某个软件包（命令为 `pacman -R`）或升级某个软件包（该软件包必须首先被卸载）时，可能会创建一个 `.pacsave` 文件。当 pacman 数据库记录了应当备份该软件包的某个文件时，pacman 会创建一个 `.pacsave` 文件。此时，pacman 会输出如下信息： 
    
    warning: /etc/pam.d/usermod saved as /etc/pam.d/usermod.pacsave
    
这些文件需要用户手动干预，我们推荐您在每次软件包升级或卸载之后马上处理它们。如果不处理，不当的配置可能导致软件功能出问题，甚至完全无法使用。 

##  包备份文件

软件包的 [PKGBUILD](<../../zh-cn/PKGBUILD.html> "PKGBUILD") 文件指定了升级或卸载软件包时需要被保存或备份的文件。例如，[PulseAudio](<../../zh-cn/PulseAudio.html> "PulseAudio") 的 [PKGBUILD](<../../zh-cn/PKGBUILD.html> "PKGBUILD") 文件包含如下行： 
    
    backup=(etc/pulse/{daemon.conf,default.pa,system.pa})
    
安装后，可以使用 `pacman -Qii _软件包名_` 从 pacman 数据库中查询此列表。 

要阻止任何软件包覆盖某文件，请阅读 [Pacman#在升级时跳过文件](<../../zh-cn/Pacman.html#%E5%9C%A8%E5%8D%87%E7%BA%A7%E6%97%B6%E8%B7%B3%E8%BF%87%E6%96%87%E4%BB%B6> "Pacman"). 

##  类型说明

### .pacnew

对于每一个 [#包备份文件](<#%E5%8C%85%E5%A4%87%E4%BB%BD%E6%96%87%E4%BB%B6>)，在升级过程中，Pacman 会将从文件内容生成的三个 [MD5](<https://zh.wikipedia.org/wiki/MD5> "zhwp:MD5") 校验和进行交叉比较：一个校验和对应最初由软件包安装的版本，一个对应当前在文件系统中的版本，还有一个对应新软件包中的版本。如果当前在文件系统中的文件版本已经被修改过，那么Pacman无法知道如何将这些更改与新版本合并。因此，在升级过程中，为了避免覆盖已修改的文件，Pacman会保存新版本，并附加上 `.pacnew` 后缀，而不会对已修改的版本做任何改动。 

**注意：** 软件包的安装可能会导致其他软件包所拥有的文件发生变化（例如 [FS#77404](<https://bugs.archlinux.org/task/77404>)）。因此，即使您没有手动更改某些文件，也可能生成 `.pacnew` 文件。

进一步详细说明，三重 MD5 校验和对比会导致以下几种结果之一： 

原始版本 = _X_ ，当前版本 = _X_ ，新版本 = _X_
    所有三个版本的内容完全相同，所以覆盖是没有问题的。用新版本覆盖当前版本，并且不通知用户（尽管文件内容相同，这次覆盖将会更新文件系统的有关该文件的安装、修改及访问时间的信息，并确保应用任何文件权限变更）。

原始版本 = _X_ ，当前版本 = _X_ ，新版本 = _Y_
    当前版本的内容与原始版本一致，但新版本不同。由于用户没有修改当前版本，而新版本可能包含改进或修复，所以用新版本覆盖当前版本，并且不通知用户。这是 Pacman 能够执行的唯一一种自动合并新更改的情况。

原始版本 = _X_ ，当前版本 = _Y_ ，新版本 = _X_
    原始软件包和新软件包都包含了文件的完全相同版本，但是当前文件系统中的版本已被修改。保留当前版本，并丢弃新版本而不通知用户。

原始版本 = _X_ ，当前版本 = _Y_ ，新版本 = _Y_
    新版本与当前版本完全相同。用新版本覆盖当前版本，并且不通知用户（尽管文件内容相同，这次覆盖将会更新文件系统的有关该文件的安装、修改及访问时间的信息，并确保应用任何文件权限变更）。

原始版本 = _X_ ，当前版本 = _Y_ ，新版本 = _Z_
    所有三个版本都不相同，因此保留当前版本，并以 `.pacnew` 后缀安装新版本，同时警告用户有关新版本的存在。用户需要手动合并新版本中必要的更改到当前版本中。

有时升级后的软件包罕见地包含了一个之前版本不存在的备份文件，这种情况会被正确处理为 X/Y/Y 或 X/Y/Z，其中 X 代表不存在。 

### .pacsave

如果用户修改了 `backup` 中指定的某个文件，那么在软件包其余部分移除后该文件将被重命名，带上 `.pacsave` 扩展名，仍然存于文件系统中。 

**注意：** 使用命令 `pacman -R` 中的 `-n` 选项会移除指定软件包中的所有文件，因此不会创建 `.pacsave` 文件。

##  定位 .pac* 文件

Pacman 不会自动处理 `.pacnew` 文件，需要自己维护。下面提供帮助你处理这些文件的一些工具。如果需要手动处理，首先需要找到这些文件。在升级或移除大量软件包时，可能会忽略一些更新的 .pac* 文件。可以使用以下方法之一检查存在的 .pac* 文件： 

在用于存放大多数全局配置文件的 `/etc` 目录中搜索： 
    
    $ find /etc -regextype posix-extended -regex ".+\.pac(new|save)" 2> /dev/null
    
或者在将上述命令中的 `/etc` 替换为 `/` 以在整个磁盘上进行搜索（在这种情况下，你可能想要选择性地跳过某些目录以加快搜索速度）。 

如果你安装了 [locate](<../../zh-cn/Locate.html> "Locate")，还可以使用它来搜索。首先需要更新索引数据库： 
    
    # updatedb
    
然后: 
    
    $ locate --existing --regex "\.pac(new|save)$"

或者使用 pacman 日志来找到它们： 
    
    $ egrep "pac(new|save)" /var/log/pacman.log
    
**注意：** 日志不会跟踪当前在文件系统中的文件，也不会跟踪已经被删除的文件；上述命令将列出系统上曾经存在过的所有 `.pac*` 文件。为了只获取最近的10个 `.pac*` 文件，可以将结果通过管道传输给 `tail` 命令。

##  管理 .pac* 文件

### pacdiff

[pacman-contrib](<https://archlinux.org/packages/?name=pacman-contrib>)包 提供了一个简单的 [pacdiff(8)](<https://man.archlinux.org/man/pacdiff.8>) 工具来管理 _.pac*_ 文件。 

它会搜索 `.pacnew`、`.pacsave` 和 `.pacorig` 文件，然后提示对它们采取行动。 

默认情况下，它使用 `--pacmandb` 来搜索当前已安装包的 `backup` 列表信息。如果这不够用，您可以指定 `--find` 或 `--locate` 来进行更彻底的搜索。 

默认情况下，它使用 [vimdiff](<../../zh-cn/Vim.html#%E6%96%87%E4%BB%B6%E5%90%88%E5%B9%B6> "Vim")，但您可以通过 `DIFFPROG=_your_editor_ pacdiff` 指定一个不同的工具。查看[应用程序列表/工具#比较，差异，合并](<../../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#%E6%AF%94%E8%BE%83%EF%BC%8C%E5%B7%AE%E5%BC%82%EF%BC%8C%E5%90%88%E5%B9%B6> "应用程序列表/工具")了解其他常见的比较工具。 

###  第三方工具

一些第三方工具提供了不同程度的自动化功能来处理这些任务： 

  * **dotpac** — 基本的交互式脚本，带有基于 ncurses 的文本界面和有用的向导。没有合并或自动合并功能。

     <https://github.com/AladW/dotpac> || [dotpac](<https://aur.archlinux.org/packages/dotpac/>)AUR

  * **etc-update** — _Gentoo_ 的实用工具，兼容包括 Arch 在内的其他发行版。它提供了一个简单的命令行界面来查看、合并和交互式编辑更改。像注释这样的简单更改可以自动合并。

     [Gentoo:Handbook:Parts/Portage/Tools#etc-update](<https://wiki.gentoo.org/wiki/Handbook:Parts/Portage/Tools#etc-update> "gentoo:Handbook:Parts/Portage/Tools") || [etc-update](<https://archlinux.org/packages/?name=etc-update>)包

  * **p3wm** — 三方合并 `.pacnew` 文件。它可以自动合并简单更改。如果发生冲突，它将启动 vimdiff、meld 或 kdiff3 来解决它们。

     <https://github.com/5long/p3wm> || [p3wm](<https://aur.archlinux.org/packages/p3wm/>)AUR

  * **pacnews-git** — 一个简单的脚本，旨在找到所有的 `.pacnew` 文件，然后用 [vimdiff](<../../zh-cn/Vim.html#%E6%96%87%E4%BB%B6%E5%90%88%E5%B9%B6> "Vim") 编辑它们。

     <https://github.com/pbrisbin/scripts/blob/master/pacnews> || [pacnews-git](<https://aur.archlinux.org/packages/pacnews-git/>)AUR

  * **pacfiles-mode** — 一个用于 [Emacs](<../../zh-cn/Emacs.html> "Emacs") 管理和合并 _.pacnew_ 文件的包。

     <https://github.com/UndeadKernel/pacfiles-mode> || 在 [melpa](<https://melpa.org/#/pacfiles-mode>) 中可用

  * **pacdiff-pacman-hook-git** — Pacman 钩子，自动运行 pacdiff。

     <https://github.com/desbma/pacman-hooks> || [pacdiff-pacman-hook-git](<https://aur.archlinux.org/packages/pacdiff-pacman-hook-git/>)AUR

##  参阅

  * Arch Linux 论坛: [处理 .pacnew 文件](<https://bbs.archlinux.org/viewtopic.php?id=53532>)
