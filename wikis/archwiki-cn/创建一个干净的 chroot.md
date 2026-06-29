**翻译状态：**

  * 本文（或部分内容）译自 [Building in a clean chroot](<https://wiki.archlinux.org/title/Building_in_a_clean_chroot> "arch:Building in a clean chroot")，最近一次同步于 2025-03-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/Building_in_a_clean_chroot?diff=0&oldid=820739>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Building_in_a_clean_chroot_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** [#处理大规模重构](<#%E5%A4%84%E7%90%86%E5%A4%A7%E8%A7%84%E6%A8%A1%E9%87%8D%E6%9E%84>) 需要翻译（在 [Talk:创建一个干净的 chroot#](<../zh-cn/Talk:%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%B9%B2%E5%87%80%E7%9A%84_chroot.html>) 中讨论）

##  使用 clean chroot 的意义

clean chroot 可以直译为 干净/洁净的 [chroot](<../zh-cn/Chroot.html> "Chroot")。在 clean chroot 环境中构建可以避免软件包依赖缺失问题。不然可能会出现意外的动态链接或是在 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 依赖数组 `depends` 中出现未声明的依赖。此外，它还允许用户参与 [core-testing](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html#core-testing> "官方仓库") 或 [extra-testing](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html#extra-testing> "官方仓库") 测试仓库情况下，为稳定仓库 ([core](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html#core> "官方仓库")、[extra](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html#extra> "官方仓库")) 构建软件包。 

##  便捷方式

为了快速在 clean chroot 环境中构建软件包而无需复杂配置，你可以使用 [devtools](<https://archlinux.org/packages/?name=devtools>)包 中的辅助脚本来帮助你。 

这些辅助脚本应在 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 的同一目录中调用，就像使用 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 时一样。例如，`extra-x86_64-build ` 将会自动从 `/var/lib/archbuild` 的 clean chroot 模板中创建 chroot 环境，更新它，并为 [extra](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html#extra> "官方仓库") 仓库构建软件包。对于 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html#multilib> "官方仓库") 构建则使用无架构参数的 `multilib-build`。请参考下表了解不同目标仓库和架构对应的构建脚本。 

`-c`参数用于重置chroot模板，这在环境损坏时非常有用。在建立全新的 clean chroot 时不需要此参数。 

**注意：**

  * _[core](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html#core> "官方仓库")_ 仓库被省略，因为这些软件包必须先通过 _[core-testing](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html#core-testing> "官方仓库")_ 仓库测试才能进入正式仓库
  * 如果目标是为本地使用构建 _[core](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html#core> "官方仓库")_ 仓库的软件包，建议直接使用稳定仓库而非测试仓库。此时可以直接使用`extra`构建脚本

目标仓库 | 架构 | 构建脚本 | 使用的 Pacman 配置文件   
---|---|---|---  
extra | x86_64 | extra-x86_64-build | /usr/share/devtools/pacman.conf.d/extra.conf   
core-testing / extra-testing | x86_64 | extra-testing-x86_64-build | /usr/share/devtools/pacman.conf.d/extra-testing.conf   
core-staging / extra-staging | x86_64 | extra-staging-x86_64-build | /usr/share/devtools/pacman.conf.d/extra-staging.conf   
multilib | x86_64 | multilib-build | /usr/share/devtools/pacman.conf.d/multilib.conf   
multilib-testing | x86_64 | multilib-testing-build | /usr/share/devtools/pacman.conf.d/multilib-testing.conf   
multilib-staging | x86_64 | multilib-staging-build | /usr/share/devtools/pacman.conf.d/multilib-staging.conf   
  
**提示：**[pkgctl-build(1)](<https://man.archlinux.org/man/pkgctl-build.1>)会自动选择正确的构建脚本在 clean chroot 中构建

##  传统方法

###  设置 chroot 环境

[devtools](<https://archlinux.org/packages/?name=devtools>)包 提供了用于创建 clean chroot 并在其中构建软件包的功能，请确保您已[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")该软件包。 

之后，为创建 clean chroot，请创建一个新文件夹用于存放 chroot，比如 `$HOME/chroot/`： 
    
    $ mkdir ~/chroot
    
之后定义 `CHROOT` 变量: 
    
    $ CHROOT=$HOME/chroot
    
现在就可以开始创建 clean chroot 环境了： 

**注意：** chroot 需要 `root` 文件夹的访问权限，因为 `$CHROOT` 目录需要复制其中的必要文件来创建一个干净的工作环境
    
    $ mkarchroot $CHROOT/root base-devel
    
**注意：**

  * 若您经常使用 clean chroot 构建软件包，在 `$HOME/.bashrc` 里添加 export 命令以引入 `CHROOT` 变量是一个不错的选择

  * 在 [btrfs](<../zh-cn/Btrfs.html> "Btrfs") 文件系统中，chroot 会以分卷（subvolume）的形式被创建，因此您必须以 root 用户的身份运行 `btrfs subvolume delete $CHROOT/root` 才能删除这个分卷。

所有相关信息，比如打包者名称、makeflags 等都在 `~/.makepkg.conf` 中，毋庸置疑，您需要编辑 `~/.makepkg.conf` 以确保其被正常构建。别忘了修改 `$CHROOT/root/etc/pacman.d/mirrorlist` 以更换[镜像源](<../zh-cn/%E9%95%9C%E5%83%8F%E6%BA%90.html> "镜像源")。 

如果需要，您也可以在 `$CHROOT/root/etc/pacman.conf` 中启用 [testing](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Testing") 软件仓库以在 chroot 中获取测试版本的软件包。 

**注意：**`~` 和 `$HOME` 变量在"makechrootpkg"构建脚本中会被自动定义为 `/root/`

####  自定义 pacman.conf

或者，提供一个自定义的 `pacman.conf` 和` makepkg.conf`，其中包含以下内容： 
    
    $ mkarchroot -C <pacman.conf> -M <makepkg.conf> $CHROOT/root base-devel
    
**警告：** 在首次创建 clean chroot 时使用自定义的 `pacman.conf` 或 `makepkg.conf` 可能会导致对 chroot 环境进行预期外的自定义调整。 _请谨慎使用。_

###  在 chroot 里构建

首先，请确保 base chroot (`$CHROOT/root`) 是最新的： 
    
    $ arch-nspawn $CHROOT/root pacman -Syu
    
其次，在包含其 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 的目录中调用 `makechrootpkg` 来构建软件包： 
    
    $ makechrootpkg -c -r $CHROOT
    
**注意：** 传递 `-c` 参数给 `makechrootpkg` 可确保在构建前清理工作 chroot (`$CHROOT/$USER`)。

####  预装必要依赖包

要在 `$CHROOT/root/pacman.conf` 中启用的仓库无法提供所需依赖的情况下构建软件包，请使用 `-I _package_` 预先将它们安装到工作 chroot 中： 
    
    $ makechrootpkg -c -r $CHROOT -I build-dependency-1.0-1-x86_64.pkg.tar.xz -I required-package-2.0-2-x86_64.pkg.tar.xz
    
####  向 makepkg 传递参数

要向 [makepkg](<../zh-cn/Makepkg.html#Usage> "Makepkg") 传递参数，请在 [end-of-options marker (选项结束符)](<https://wiki.bash-hackers.org/dict/terms/end_of_options>) 之后列出它们；例如，若要强制执行 `check()`： 
    
    $ makechrootpkg -c -r $CHROOT -- --check
    
##  处理大规模重构

处理大型重构最简洁的方法是使用 _staging_ 仓库。先针对 _extra_ 构建第一个软件包并推送到 _staging_ 仓库。然后将后续所有软件包都基于 _staging_ 重新构建，并一同推送到那里。 

如果无法使用 _staging_ 仓库，也可以通过如下命令，使用自定义软件包进行构建： 
    
    # extra-x86_64-build -- -I ~/packages/foobar/foobar-2-1-any.pkg.tar.xz
    
You can specify more than one package to be installed using multiple `-I` arguments. 

A simpler, but dirtier way to handle a major rebuild is to install all built packages in the chroot, never cleaning it. Build the first package using: 
    
    # extra-x86_64-build
    
And build all following packages using: 
    
    # makechrootpkg -n -r /var/lib/archbuild/extra-x86_64
    
Running namcap (the `-n` argument) implies installing the package in the chroot. _*-build_ also does this by default. 

##  小提示和小技巧

###  在tmpfs中构建

若系统拥有足够内存，可为 [devtools](<https://archlinux.org/packages/?name=devtools>)包 构建脚本指定 [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs") 文件系统。 
    
    # mount --mkdir -t tmpfs -o defaults,size=20G tmpfs /mnt/chroots/arch
    # extra-x86_64-build -c -r /mnt/chroots/arch
    