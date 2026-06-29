**翻译状态：**

  * 本文（或部分内容）译自 [Kernel/Arch Build System](<https://wiki.archlinux.org/title/Kernel/Arch_Build_System> "arch:Kernel/Arch Build System")，最近一次同步于 2023-7-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Kernel/Arch_Build_System?diff=0&oldid=780736>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Kernel_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Arch_Build_System_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

参阅[内核](<../../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")。 

利用 [Arch 编译系统](<../../zh-cn/Arch_Build_System.html> "Arch Build System")，可以基于官方的 [linux](<https://archlinux.org/packages/?name=linux>)包 包编译自定义内核。这种编译方法可以自动化整个过程，并且是基于一个已经经过详细测试过的内核包。你可以编辑 PKGBUILD 来使用一个自定义内核配置或者添加附加的补丁。 

##  获取所需内容

因为要使用到 [makepkg](<../../zh-cn/Makepkg.html> "Makepkg"), 请先了解 makepkg 的使用方法和最佳实践建议。例如不要用 root/sudo 运行 makepkg. 

首先建立一个编译目录 `build`： 
    
    $ mkdir ~/build/
    $ cd ~/build/
    
[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [devtools](<https://archlinux.org/packages/?name=devtools>)包 和 [base-devel](<https://archlinux.org/groups/x86_64/base-devel/>)包组. 

首先需要一个原始内核作为自定义的基础，从[Git获取PKGBUILD](<../../zh-cn/Arch_Build_System.html#%E4%BD%BF%E7%94%A8_Git_%E8%8E%B7%E5%8F%96_PKGBUILD> "Arch Build System")等文件，放到编译目录： 
    
    $ pkgctl repo clone --protocol=https linux
    
此时，目录树应该看起来像这样： 
    
    ~/build/linux/-+
                   +--config
                   \__PKGBUILD

然后从相应的来源获取其他需要的文件 (例如自定义配置文件、补丁等)。 

##  修改 PKGBUILD

编辑 `PKGBUILD`，找到 `pkgbase` 修改为自定义软件包的名称: 
    
    PKGBUILD
    
    pkgbase=linux-custom

**警告：****切勿** 将`linux`添加到`provides`数组中，因为你的定制内核和为原`linux`包编译的内核模块不兼容，不满足`provides`所需的依赖关系。同样，也不要把`linux-headers`添加到头文件包的`provides`数组。

###  避免创建文档

编译内核的冗长过程中，很大一部分时间被用于编译文档。2022年8月25日之后，可以应用以下补丁到PKGBUILD中，来避免生成文档： 
    
    63c63
    <   make htmldocs all
    ---
    >   make all
    195c195
    < pkgname=("$pkgbase" "$pkgbase-headers" "$pkgbase-docs")
    ---
    > pkgname=("$pkgbase" "$pkgbase-headers")

这一补丁删除了#63行，更改了#195行。如果补丁没法直接应用，那就需要手动进行修改。 

###  修改 prepare()

可以在`prepare()`中[打上需要的补丁](<../../zh-cn/Patching_packages.html#%E5%BA%94%E7%94%A8%E8%A1%A5%E4%B8%81> "Patching packages")，或修改内核配置文件。 

若要修改配置选项，可以直接编辑源文件。 

亦可改用 GUI 工具调整编译选项。从 PKGBUILD 的 prepare() 函数中取消注释`make olddefconfig`，然后添加你所需的工具： 
    
    PKGBUILD
    
    ...
      msg2 "Setting config..."
      cp ../config .config
      #make olddefconfig
    
      make nconfig     # new CLI menu for configuration
      #make menuconfig # CLI menu for configuration
      #make xconfig    # X-based configuration
      #make oldconfig  # using old config from previous kernel version
      # ... or manually edit .config
      make prepare
    ...

**警告：**[systemd](<https://archlinux.org/packages/?name=systemd>)包对内核配置有一些要求，无论是一般使用、特定使用条件（比如UEFI）还是某个功能（比如bootchart），不满足这些要求可能导致不稳定或者性能下降。[systemd](<https://archlinux.org/packages/?name=systemd>)包推荐的配置列表可在`/usr/share/doc/systemd/README`中查看。在编译前应先行检查是否已经满足要求。另外，随着其版本更迭，这些要求可能会改变，arch不会对这些改变进行公告。为了确保你的定制内核满足systemd的要求，在更新systemd之前应检视其发行注记。

###  生成新校验和

[#修改 prepare()](<#%E4%BF%AE%E6%94%B9_prepare\(\)>)步骤意味着你已经修改了`$_srcname/.config`文件。需要生成新的校验和（需[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[pacman-contrib](<https://archlinux.org/packages/?name=pacman-contrib>)包）： 
    
    $ updpkgsums
    
##  编译

现在可以用`makepkg`命令编译内核了，如果配置时选择了交互编译(例如 menuconfig)，编译时需要进行配置。 
    
     $ makepkg -s
    
选项 `-s` 会在编译时下载需要的依赖关系，比如 xml 和 docs. 

**注意：**

  * 内核代码是 [PGP 签名](<https://www.kernel.org/signature.html#kernel-org-web-of-trust>), makepkg 会尝试进行校验，详情请参考 [makepkg#Signature checking](<../../zh-cn/Makepkg.html#Signature_checking> "Makepkg").

  * 编译时间可能长达数小时，取决于你的硬件性能。[并行编译](<../../zh-cn/Makepkg.html#Parallel_compilation> "Makepkg")可以在多核系统上显著减少编译时间。

  * 可以用`time makepkg`来知道这次生成在你的系统上占用了多长时间。

##  安装

编译完成后，`build/linux`文件夹中应有两个包，分别是内核和内核的头文件。命名类似： 
    
    linux-custom-5.8.12-x86_64.pkg.tar.zst
    linux-custom-headers-5.8.12-x86_64.pkg.tar.zst
    
最好同时安装这两个包，因为他们可能相互依赖（比如[DKMS](<../../zh-cn/DKMS.html> "DKMS")）： 
    
    # pacman -U _linux-custom-5.8.12-x86_64.pkg.tar.zst_ _linux-custom-headers-5.8.12-x86_64.pkg.tar.zst_
    
（需要执行的命令是你实际的包名） 

##  引导加载程序

如果你的定制内核和默认内核共存（修改`pkgbase`），为了开机时能够引导你的内核，安装完成后需更新引导加载程序的配置文件，为新的内核和initramfs映像添加新的引导菜单项。 

如果使用[grub](<https://archlinux.org/packages/?name=grub>)包，可以执行以下命令自动生成新的配置文件（假设配置文件是`/boot/grub/grub.cfg`）： 
    
    # grub-mkconfig -o /boot/grub/grub.cfg
    
##  更新

假设已有arch内核的源码，要对其进行更新，一种方法是使用https://github.com/archlinux/linux。本节以下内容假设内核源码树根目录位于`~/build/linux/`。 

一般而言，放置内核源码需要使用两个本地git仓库，一个本地裸[git](<../../zh-cn/Git.html> "Git")仓库位于`archlinux-linux`，指向 `https://github.com/archlinux/linux.git`。另一个拉取自裸仓库，位于`**src/** archlinux-linux/`。本地的补丁、构建很可能位于`**src/** archlinux-linux/`。 

在本例中，本地位于`archlinux-linux/`的裸仓库的HEAD指向 
    
    $ cd ~/build/linux/archlinux-linux/
    $ git log --oneline --max-count 1 HEAD
    
    4010b622f1d2 Merge branch 'dax-fix-5.3-rc3' of git://git.kernel.org/pub/scm/linux/kernel/git/nvdimm/nvdimm

可以看到，这个HEAD的指向位于 v5.2.5-arch1 和 v5.2.6-arch1 之间的某个版本。 
    
    $ git fetch --verbose
    
执行后可以看到它获取了v5.2.7-arch（编写wiki时最新的archlinux版本）。若没有获取到新的版本，则说明已是最新。 

此时可把源码更新到进行编译的位置。 
    
    $ cd ~/build/linux/src/archlinux-linux/
    $ git checkout master
    $ git pull
    $ git fetch --tags --verbose
    $ git branch --verbose 5.2.7-arch1 v5.2.7-arch1
    $ git checkout 5.2.7-arch1
    
可进行检查 
    
    $ git log --oneline 5.2.7-arch1 --max-count=7
    
    13193bfc03d4 **Arch Linux kernel v5.2.7-arch1**
    9475c6772d05 netfilter: nf_tabf676926c7f60les: fix module autoload for redir
    498d650048f6 iwlwifi: Add support for SAR South Korea limitation
    bb7293abdbc7 iwlwifi: mvm: disable TX-AMSDU on older NICs
    f676926c7f60 ZEN: Add CONFIG for unprivileged_userns_clone
    5e4e503f4f28 add sysctl to disallow unprivileged CLONE_NEWUSER by default
    5697a9d3d55f **Linux 5.2.7**

上述信息显示了一些在`Arch Linux kernel v5.2.7-arch1` and `Linux 5.2.7`之间的archlinux补丁。 

使用下列命令拉取最新的PKGBUILD和内核配置文件： 
    
    $ cd ~/build/linux/
    $ git pull
    
然后应将`~/build/linux/linux/*`[合并](<../../zh-cn/Vim.html#Merging_files> "Vim")到`~/build/linux/`中。合并可以手动完成，也可以使用[合并工具](<../../zh-cn/List_of_applications.html#Comparison,_diff,_merge> "List of applications")。参照[#修改 prepare()](<#%E4%BF%AE%E6%94%B9_prepare\(\)>)一节进行所需的修改。 

此时应可成功执行`makepkg --verifysource`。 

然后可进行[#编译](<#%E7%BC%96%E8%AF%91>)，确保执行`makepkg`时添加`--noextract`选项。它应该能成功构建，因为源代码是`makepkg --nobuild`解压出的。编译完成后，可进行[#安装](<#%E5%AE%89%E8%A3%85>)。 

##  清理

合并之后可以删除`~/build/linux/linux/`。另外，随着更新，`~/build/linux/src/archlinux`会积累很多分支（形如`5.2.7-arch1`）。这些可以使用下列命令清理掉： 
    
    $ cd ~/build/linux/src/archlinux
    $ git branch --delete --force --verbose 5.2.7-arch1
    
##  参阅

  * <https://docs.kernel.org/kbuild/kconfig.html> and the parent directory
