**翻译状态：**

  * 本文（或部分内容）译自 [SELinux](<https://wiki.archlinux.org/title/SELinux> "arch:SELinux")，最近一次同步于 2026-04-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/SELinux?diff=0&oldid={{{3}}}>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SELinux_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Security](<../zh-cn/%E5%AE%89%E5%85%A8.html> "Security")
  * [AppArmor](<../zh-cn/AppArmor.html> "AppArmor")
  * [TOMOYO Linux](</wzh/index.php?title=TOMOYO_Linux&action=edit&redlink=1> "TOMOYO Linux（页面不存在）")

安全增强型 Linux (SELinux)是一项 Linux 特性，它通过在 Linux 内核中使用 Linux 安全模块(LSM)提供多种安全策略，其中包括美国国防部风格的强制访问控制(MAC)。SELinux 并不是一个 Linux 发行版，而是一套可以应用于Linux和BSD等类 Unix 操作系统的修改补丁集。 

在 Linux 发行版下运行 SELinux 需要满足三个条件：开启了 SELinux 支持的内核、SELinux 用户空间工具与库，以及 SELinux 策略（通常基于参考策略(Reference Policy)）。一些常见的 Linux 程序还需要应用补丁或在编译时开启SELinux特性。 

##  在 Arch Linux 中的状态

SELinux 并不是 Arch Linux 官方支持的功能（参见[[1]](<#cite_note-1>)[[2]](<#cite_note-2>)）。非官方支持的状态如下： 

名称  | 状态  | 获取渠道   
---|---|---  
SELinux 启用的内核  | 适用于所有官方支持的内核  | 自 4.18.8 版本以来已在官方仓库中提供   
SELinux 用户空间工具和库  | 已在 AUR 中提供：[https://aur.archlinux.org/packages/?O=0&K=selinux](<https://aur.archlinux.org/packages/?O=0&K=selinux>) | 相关开发工作正在 <https://github.com/archlinuxhardened/selinux> 进行   
SELinux 策略  | 正在开发中，以 [Reference Policy](<https://github.com/SELinuxProject/refpolicy>) 作为基础  | 上游：<https://github.com/SELinuxProject/refpolicy>（自 20170805 版本以来，该策略已集成了对 systemd 和单一-/usr/bin 目录的支持）   
  
与官方核心包相比，以下是 AUR 中的一些包的变更摘要： 

名称  | 状态与说明   
---|---  
linux, linux-lts, linux-zen, linux-hardened  | 需要[设置 lsm= 内核参数](</wzh/index.php?title=%E8%AE%BE%E7%BD%AE_lsm%3D_%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0&action=edit&redlink=1> "设置 lsm= 内核参数（页面不存在）")  
coreutils  | 需要带上 `--with-selinux` 选项重新构建以链接 libselinux   
cronie  | 需要带上 `--with-selinux` 选项重新构建   
dbus  | 需要带上 `--enable-libaudit` 和 `--enable-selinux` 选项重新构建   
findutils  | 需要使用 libselinux 并重新构建以启用 SELinux 特定选项   
iproute2  | 需要带上 `--with-selinux` 选项重新构建   
logrotate  | 需要带上 `--with-selinux` 选项重新构建   
openssh  | 需要带上 `--with-selinux` 选项重新构建   
pam  | 对于 Linux-PAM，需要使用 `--enable-selinux` 编译选项重新构建；对于 pam_unix2 ，需要应用一个补丁，该补丁仅用于删除一个在近版本的 libselinux 中已实现的重复函数   
pambase  | 修改配置，将 pam_selinux.so 添加到 `/etc/pam.d/system-login`  
psmisc  | 需要带上 `--with-selinux` 选项重新构建   
shadow  | 需要带上 `--with-selinux` 选项重新构建   
sudo  | 需要带上 `--with-selinux` 选项重新构建   
systemd  | 需要带上 `--enable-audit` 和 `--enable-selinux` 选项重新构建   
util-linux  | 需要带上 `--with-selinux` 选项重新构建   
  
所有其他 SELinux 相关软件包均可直接引入，无需修改，且无安全风险。 

##  概念：强制访问控制

**注意：** 本节面向初学者。如果您已了解 SELinux 的功能及其工作原理，可以跳过直接进入[#安装](<#%E5%AE%89%E8%A3%85>)部分

在启用 SELinux 之前，了解它的功能很有必要。简单直接的来说，SELinux在Linux上执行 _强制访问控制(MAC)_ 。与之相对，传统的用户/组/rwx权限属于 _自主访问控制(DAC)_ 。MAC与DAC的不同之处在于：安全策略和执行是完全分离的 

以 _sudo_ 命令为例：在执行DAC时， _sudo_ 允许临时提权至root，从而赋予所产生的进程无限制的全系统访问权限。然而，在使用MAC时，如果安全管理员规定该进程只能访问某个文件集合，那么无论使用何种提权手段，除非更改安全策略本身，否则该进程仍将被限制在该文件范围内。因此，如果在运行SELinux的机器上尝试使用 _sudo_ 让进程访问未授权的文件，该操作将会失败。 

另一个例子是传统的(-rwxr-xr-x)类型权限。在DAC机制下，这些权限是用户可修改的。但在MAC下，安全管理员可以选择“冻结”特定文件的权限，除非更改相关策略，否则任何用户都无法修改这些权限。 

正如你所想象的那样，这对于可能被攻破的进程（如Web服务器等）非常有用。如果使用DAC，一旦具备提权能力的程序被攻破，极有可能会对系统造成严重破坏。 

欲了解更多信息，请访问[维基百科: 强制访问控制](<https://zh.wikipedia.org/wiki/%E5%BC%BA%E5%88%B6%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6> "wiki-zh:强制访问控制")。 

##  安装 SELinux

###  软件包说明

所有 SELinux 相关软件包都属于AUR中的`selinux`包组。在手动安装这些包之前，请先阅读[#安装](<#%E5%AE%89%E8%A3%85>)章节 

####  支持 SELinux 的系统工具

[coreutils-selinux](<https://aur.archlinux.org/packages/coreutils-selinux/>)AUR
    经过修改的 coreutils 软件包，编译时已启用 SELinux 支持，它会替换[coreutils](<https://archlinux.org/packages/?name=coreutils>)包软件包。
[cronie-selinux](<https://aur.archlinux.org/packages/cronie-selinux/>)AUR
    由 Fedora维护的 Vixie cron 派生版本，已启用 SELinux 支持。它会替换[cronie](<https://archlinux.org/packages/?name=cronie>)包软件包。
[dbus-selinux](<https://aur.archlinux.org/packages/dbus-selinux/>)AUR
    支持 SELinux 的 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 版本. 它会替换 [dbus](<https://archlinux.org/packages/?name=dbus>)包 软件包。
[findutils-selinux](<https://aur.archlinux.org/packages/findutils-selinux/>)AUR
    经过补丁修改并开启了 SELinux 支持的 findutils 软件包，使得按特定安全上下文搜索文件成为可能。它会替换 [findutils](<https://archlinux.org/packages/?name=findutils>)包 软件包。
[iproute2-selinux](<https://aur.archlinux.org/packages/iproute2-selinux/>)AUR
    开启了 SELinux 支持的 iproute2 软件包；例如，它为`ss`命令增加了`-Z`选项。它会替换[iproute2](<https://archlinux.org/packages/?name=iproute2>)包软件包
[logrotate-selinux](<https://aur.archlinux.org/packages/logrotate-selinux/>)AUR
    开启了 SELinux 支持的 logrotate 软件包，它会替换[logrotate](<https://archlinux.org/packages/?name=logrotate>)包软件包
[openssh-selinux](<https://aur.archlinux.org/packages/openssh-selinux/>)AUR
    开启了 SELinux 支持的[OpenSSH](<../zh-cn/OpenSSH.html> "OpenSSH")软件包。它会替换[openssh](<https://archlinux.org/packages/?name=openssh>)包软件包
[pam-selinux](<https://aur.archlinux.org/packages/pam-selinux/>)AUR 与 [pambase-selinux](<https://aur.archlinux.org/packages/pambase-selinux/>)AUR
    包含`pam_selinux.so`的PAM软件包及其基础(base)软件包。它们分别替换[pam](<https://archlinux.org/packages/?name=pam>)包和[pambase](<https://archlinux.org/packages/?name=pambase>)包软件包
[psmisc-selinux](<https://aur.archlinux.org/packages/psmisc-selinux/>)AUR
    开启了 SELinux 支持的 psmisc 软件包；例如，它为`killall`增加了`-Z`选项。它会替换[psmisc](<https://archlinux.org/packages/?name=psmisc>)包软件包
[shadow-selinux](<https://aur.archlinux.org/packages/shadow-selinux/>)AUR
    开启了 SELinux 支持的 shadow 软件包；包含修改后的 `/etc/pam.d/login` 文件，用于在用户登录后设置正确的安全上下文。它会替换 [shadow](<https://archlinux.org/packages/?name=shadow>)包 软件包。
[sudo-selinux](<https://aur.archlinux.org/packages/sudo-selinux/>)AUR
    经过修改且开启了 SELinux 支持的 [sudo](<../zh-cn/Sudo.html> "Sudo") 软件包，可正确设置安全上下文。它会替换 [sudo](<https://archlinux.org/packages/?name=sudo>)包 软件包。
[systemd-selinux](<https://aur.archlinux.org/packages/systemd-selinux/>)AUR
    支持 SELinux 的 [systemd](<../zh-cn/Systemd.html> "Systemd") 版本。它会替换 [systemd](<https://archlinux.org/packages/?name=systemd>)包 软件包。
[util-linux-selinux](<https://aur.archlinux.org/packages/util-linux-selinux/>)AUR
    经过修改的 util-linux 软件包，编译时已启用 SELinux 支持。它会替换 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 软件包。

####  SELinux 用户空间实用程序

[checkpolicy](<https://aur.archlinux.org/packages/checkpolicy/>)AUR
    用于构建 SELinux 策略的工具。
[mcstrans](<https://aur.archlinux.org/packages/mcstrans/>)AUR
    供 libselinux 使用，用于转换 MCS 标签的守护进程。
[libselinux](<https://aur.archlinux.org/packages/libselinux/>)AUR
    为支持安全感知的应用程序提供的库。现已包含 _semanage_ 和 _setools_ 所需的 Python 绑定。
[libsemanage](<https://aur.archlinux.org/packages/libsemanage/>)AUR
    用于策略管理的库。现已包含 _semanage_ 和 _setools_ 所需的 Python 绑定。
[libsepol](<https://aur.archlinux.org/packages/libsepol/>)AUR
    用于操作二进制策略的库。
[policycoreutils](<https://aur.archlinux.org/packages/policycoreutils/>)AUR
    SELinux 核心工具，例如 _newrole_ 、 _setfiles_ 等。
[restorecond](<https://aur.archlinux.org/packages/restorecond/>)AUR
    用于维护部分文件标签的守护进程。
[secilc](<https://aur.archlinux.org/packages/secilc/>)AUR
    针对以 CIL（通用中间语言）编写的 SELinux 策略的编译器。
[selinux-dbus-config](<https://aur.archlinux.org/packages/selinux-dbus-config/>)AUR
    允许管理 SELinux 配置的 DBus 服务。
[selinux-gui](<https://aur.archlinux.org/packages/selinux-gui/>)AUR
    SELinux 图形界面工具（system-config-selinux）。
[selinux-python](<https://aur.archlinux.org/packages/selinux-python/>)AUR
    SELinux Python 工具与库（包含 _semanage_ 、 _sepolgen_ 、 _sepolicy_ 等）。
[selinux-sandbox](<https://aur.archlinux.org/packages/selinux-sandbox/>)AUR
    SELinux 沙箱工具。
[semodule-utils](<https://aur.archlinux.org/packages/semodule-utils/>)AUR
    在构建策略时用于处理 SELinux 模块的工具。

####  SELinux 策略相关软件包

[selinux-refpolicy-src](<https://aur.archlinux.org/packages/selinux-refpolicy-src/>)AUR
    参考策略(Reference Policy)的源码。
[selinux-refpolicy-git](<https://aur.archlinux.org/packages/selinux-refpolicy-git/>)AUR
    参考策略的 Git 主分支版本 (<https://github.com/SELinuxProject/refpolicy>) ，针对 Arch Linux的具体配置进行了构建。适合尝鲜/开发场景。
[selinux-refpolicy-arch](<https://aur.archlinux.org/packages/selinux-refpolicy-arch/>)AUR
    预编译的模块化参考策略，包含头文件和文档，但不含源码。该版本包含了正在开发中的 Arch Linux Refpolicy 补丁，用以修复路径标签和 systemd 支持的相关问题；在[selinux-refpolicy-arch](<https://aur.archlinux.org/packages/selinux-refpolicy-arch/>)AUR 中包含这些补丁，主要是为了在 Refpolicy 正式版发布间隙进行及时的滚动更新。推荐大多数用户使用。

####  其他 SELinux工具

[setools](<https://aur.archlinux.org/packages/setools/>)AUR
    用于管理SELinux的命令行和图形界面工具。
[selinux-alpm-hook](<https://aur.archlinux.org/packages/selinux-alpm-hook/>)AUR
    pacman 钩子；在安装和更新软件包时，根据 SELinux 策略自动为文件标记标签

###  安装

安装所需的 SELinux 软件包共有三种方法： 

####  通过 Github 上的二进制软件包

所有软件包均可通过[selinux](<../zh-cn/Unofficial_user_repositories.html#selinux> "Unofficial user repositories")非官方仓库获取。在系统安装阶段的`arch-bootstrap`阶段，可以使用 _base-selinux_ 替换 _base_ 软件包。 

**警告：** 目前该仓库不提供软件包签名，这意味着 pacman 将无法验证下载的二进制文件。这存在风险；慎重执行。

####  通过 Github 上的构建脚本

该仓库还包含一个名为`build_and_install_all.sh`的脚本，它会按照所需顺序构建并安装（或更新）所有软件包。以下是在用户终端中使用该脚本安装所有软件包的实例（包含下载用于验证软件包源码的GPG密钥）： 
    
    $ git clone <https://github.com/archlinuxhardened/selinux.git>
    $ cd selinux
    $ ./recv_gpg_keys.sh
    $ ./build_and_install_all.sh
    
当然，在运行脚本之前可以修改`build_and_install_all.sh`的内容；例如，如果你已经拥有支持 SELinux 的内核，则可以调整相关内容。 

####  通过 AUR

  * **首先** ，按照以下顺序（受依赖关系限制）安装 SELinux 用户空间工具和库：[libsepol](<https://aur.archlinux.org/packages/libsepol/>)AUR、[libselinux](<https://aur.archlinux.org/packages/libselinux/>)AUR、[checkpolicy](<https://aur.archlinux.org/packages/checkpolicy/>)AUR、[secilc](<https://aur.archlinux.org/packages/secilc/>)AUR、[setools](<https://aur.archlinux.org/packages/setools/>)AUR、[libsemanage](<https://aur.archlinux.org/packages/libsemanage/>)AUR、[semodule-utils](<https://aur.archlinux.org/packages/semodule-utils/>)AUR、[policycoreutils](<https://aur.archlinux.org/packages/policycoreutils/>)AUR、[selinux-python](<https://aur.archlinux.org/packages/selinux-python/>)AUR（依赖于[python-ipy](<https://aur.archlinux.org/packages/python-ipy/>)AUR）、[mcstrans](<https://aur.archlinux.org/packages/mcstrans/>)AUR以及[restorecond](<https://aur.archlinux.org/packages/restorecond/>)AUR。
  * **然后** ，安装[pambase-selinux](<https://aur.archlinux.org/packages/pambase-selinux/>)AUR和[pam-selinux](<https://aur.archlinux.org/packages/pam-selinux/>)AUR。请务必确保在安装完成后能够再次正常的登录，因为当[pambase](<https://archlinux.org/packages/?name=pambase>)包被替换为[pambase-selinux](<https://aur.archlinux.org/packages/pambase-selinux/>)AUR时，`/etc/pam.d/`中的文件会被删除并重新创建。
  * **接着** ，安装以下包以重新编译部分核心组件：[coreutils-selinux](<https://aur.archlinux.org/packages/coreutils-selinux/>)AUR、[findutils-selinux](<https://aur.archlinux.org/packages/findutils-selinux/>)AUR、[iproute2-selinux](<https://aur.archlinux.org/packages/iproute2-selinux/>)AUR、[logrotate-selinux](<https://aur.archlinux.org/packages/logrotate-selinux/>)AUR、[openssh-selinux](<https://aur.archlinux.org/packages/openssh-selinux/>)AUR、[psmisc-selinux](<https://aur.archlinux.org/packages/psmisc-selinux/>)AUR、[shadow-selinux](<https://aur.archlinux.org/packages/shadow-selinux/>)AUR、[cronie-selinux](<https://aur.archlinux.org/packages/cronie-selinux/>)AUR。
  * **下一步** ，如果你没有使用[Sudo#配置|sudo的drop-in配置文件]]，请先备份`/etc/sudoers`。安装[sudo-selinux](<https://aur.archlinux.org/packages/sudo-selinux/>)AUR后恢复该文件（因为该包替换[sudo](<https://archlinux.org/packages/?name=sudo>)包时会覆盖原有配置）
  * **随后** 处理 util-linux 和 systemd。由于这两个包存在无法修复的循环构建依赖（[FS#39767](<https://bugs.archlinux.org/task/39767>)），你需要按照以下步骤操作：构建源码包[systemd-selinux](<https://aur.archlinux.org/packages/systemd-selinux/>)AUR -> 安装[systemd-libs-selinux](<https://aur.archlinux.org/packages/systemd-libs-selinux/>)AUR -> 构建并安装[util-linux-selinux](<https://aur.archlinux.org/packages/util-linux-selinux/>)AUR（包含[util-linux-libs-selinux](<https://aur.archlinux.org/packages/util-linux-libs-selinux/>)AUR） -> 最后重新构建并安装[systemd-selinux](<https://aur.archlinux.org/packages/systemd-selinux/>)AUR。
  * **接着** ，安装[dbus-selinux](<https://aur.archlinux.org/packages/dbus-selinux/>)AUR。
  * **最后** ，安装[selinux-alpm-hook](<https://aur.archlinux.org/packages/selinux-alpm-hook/>)AUR，以便在每次 pacman 安装软件包时自动运行 restorecon（ _restore context_ ，恢复安全上下文）。

完成上述所有步骤后，你可以安装支持 SELinux 的内核（如[linux](<https://archlinux.org/packages/?name=linux>)包）以及相关策略（如[selinux-refpolicy-arch](<https://aur.archlinux.org/packages/selinux-refpolicy-arch/>)AUR 或 [selinux-refpolicy-git](<https://aur.archlinux.org/packages/selinux-refpolicy-git/>)AUR）。 

###  启用 SELinux LSM

若要在每次启动时默认启用 SELinux 作为安全模型，请设置以下[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")： 

`lsm=landlock,lockdown,yama,integrity,selinux,bpf`

**注意：** 内核参数`lsm=`用于设置 Linux 安全模块的初始化顺序。你可以通过`zgrep CONFIG_LSM= /proc/config.gz`查看内核配置的`lsm=`默认值，通过`cat /sys/kernel/security/lsm`查看当前运行时的值。 

  * 请确保`selinux`是列表中的第一个“主要(major)”模块。[[1]](<https://docs.kernel.org/admin-guide/LSM/index.html>)有效值及其顺序的实例可以在[security/Kconfig](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/security/Kconfig>)中找到。
  * `capability`应当从`lsm=`参数中省略，因为它总是会自动被包含。

####  自定义内核

在[编译内核](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E7%BC%96%E8%AF%91> "内核")时，必须至少设置以下选项： 

`CONFIG_SECURITY_SELINUX=y`

`CONFIG_AUDIT=y`

若要默认启用 SELinux 安全模型，从而省去手动设置内核参数的麻烦，请额外设置`CONFIG_LSM`选项，并将`selinux`指定为列表中第一个“主要(major)”模块： 

`CONFIG_LSM="landlock,lockdown,yama,integrity,selinux,bpf"`

###  检查 PAM 配置

正确配置[PAM](<../zh-cn/PAM.html> "PAM")对于在登录状态后获得正确的安全上下文至关重要。请检查`/etc/pam.d/system-login`文件中是否存在以下行： 
    
    # pam_selinux.so close 应当是会话(session)规则中的第一条
    session         required        pam_selinux.so close
    
    # pam_selinux.so open 之后应当只跟随需要在用户上下文中执行的会话(session)
    session         required        pam_selinux.so open
    
###  安装策略

**警告：** 由[SELinuxProject](<https://github.com/SELinuxProject/refpolicy/wiki>)提供的参考策略 (Reference Policy) 对 Arch Linux 的支持并不理想。大多数提交补丁以改进策略的人使用的是其他发行版（如 Debian、Gentoo、RHEL等），因此该策略与 Arch Linux 软件包的兼容并不完美（例如，策略可能不支持程序的最前沿特性）。

策略是 SELinux 的支柱，决定了系统的行为，目前 AUR 中唯一可用的策略是参考策略(Reference Policy)。为了安装它，你应该采用以下方法： 

####  使用 AUR 软件包

这是最简单且快捷的方法。安装[selinux-refpolicy-arch](<https://aur.archlinux.org/packages/selinux-refpolicy-arch/>)AUR或[selinux-refpolicy-git](<https://aur.archlinux.org/packages/selinux-refpolicy-git/>)AUR，该软件包会自动处理编译和基础配置。 

####  手动安装

当你需要对策略源码进行深度定制时使用，可以通过安装[selinux-refpolicy-src](<https://aur.archlinux.org/packages/selinux-refpolicy-src/>)AUR软件包获取，也可以从 <https://github.com/SELinuxProject/refpolicy/wiki/DownloadRelease#current-release> 下载最新发行版本 
    
    # make bare
    # make conf
    # make install
    
上述命令将按原样安装参考策略。了解如何编写 SELinux 策略的用户可以在运行命令前根据喜好自行调整。编译过程需要一段时间，且会占满系统的一个 CPU 核心，这属于正常现象，无需担心。只需要坐下来等待命令运行完成即可。 

运行以下命令加载参考策略： 
    
    # make load
    
然后创建内容如下的`/etc/selinux/config`文件（仅当你使用上述默认设置时才有效；如果你更改了策略名称，则需要对文件进行相应调整）： 
    
    /etc/selinux/config
    
    # 此文件控制系统上 SELinux 的状态。
    # SELINUX= 可以取以下三个值之一:
    #       enforcing - 强制执行 SELinux 安全策略。
    #                   当你确认 SELinux 已按预期配置完毕并且系统已经准备好部署，请设置此值。
    #       permissive - SELinux 仅打印警告而非强制阻断.
    #                    在部署前使用此模式来自定义 SELinux 策略和布尔值。
    #       disabled - 不加载 SELinux 策略。
    #                  不推荐此设置，因为它可能导致文件标签(Labeling)问题
    SELINUX=permissive
    # SELINUXTYPE= 指定要使用的 SELinux 策略名称。
    # 当前选项为:
    #       refpolicy（原生参考策略）
    #       <自定义策略> - 将<自定义策略>替换为你选择加载的任何自定义策略名称
    SELINUXTYPE=refpolicy

现在可以重启系统了，重启系统后运行以下命令： 
    
    # restorecon -r /
    
以为你的文件系统标记标签。 

接着，创建一个名为`requiredmod.te`的文件，内容如下 
    
    requiredmod.te
    
    module requiredmod 1.0;
    
    require {
            type devpts_t;
            type kernel_t;
            type device_t;
            type var_run_t;
            type udev_t;
            type hugetlbfs_t;
            type udev_tbl_t;
            type tmpfs_t;
            class sock_file write;
            class unix_stream_socket { read write ioctl };
            class capability2 block_suspend;
            class dir { write add_name };
            class filesystem associate;
    }
    
    #============= devpts_t ==============
    allow devpts_t device_t:filesystem associate;
    
    #============= hugetlbfs_t ==============
    allow hugetlbfs_t device_t:filesystem associate;
    
    #============= kernel_t ==============
    allow kernel_t self:capability2 block_suspend;
    
    #============= tmpfs_t ==============
    allow tmpfs_t device_t:filesystem associate;
    
    #============= udev_t ==============
    allow udev_t kernel_t:unix_stream_socket { read write ioctl };
    allow udev_t udev_tbl_t:dir { write add_name };
    allow udev_t var_run_t:sock_file write;

**警告：** 以下代码是为了解决Refpolicy在 Arch Linux 上的兼容性报错，如果你发现系统正常且没有相关审计错误，可以跳过此步骤

接着运行以下命令： 
    
    # checkmodule -m -o requiredmod.mod requiredmod.te
    # semodule_package -o requiredmod.pp -m requiredmod.mod
    # semodule -i requiredmod.pp
    
这样做是为了消除`/var/log/audit/audit.log`中一些在参考策略(Reference Policy)里处理起来非常麻烦的干扰信息。**这是一个非常“丑陋”的临时方案(Ugly hack)** ；必须明确指出，这样安装策略仅仅是为了修补参考策略，从而掩盖因标签(Labeling)错误产生的影响。 

###  在 Vagrant 虚拟机中进行测试

可以使用[Vagrant](</wzh/index.php?title=Vagrant&action=edit&redlink=1> "Vagrant（页面不存在）")来配置一个预装并配置好 SELinux 的Arch Linux 虚拟机。这是一种在不修改当前系统的情况下，测试运行 SELinux 的 Arch Linux 系统的便捷方法。你可以使用以下命令来实现： 
    
    $ git clone <https://github.com/archlinuxhardened/selinux.git>
    $ cd selinux/_vagrant
    $ vagrant up
    $ vagrant ssh
    
##  安装后的后续步骤

你可以使用`sestatus`命令来检查 SELinux 是否正在正常运行。你应该会看到类似如下的输出： 
    
    SELinux status:                 enabled
    SELinuxfs mount:                /sys/fs/selinux
    SELinux root directory:         /etc/selinux
    Loaded policy name:             refpolicy
    Current mode:                   permissive
    Mode from config file:          permissive
    Policy MLS status:              disabled
    Policy deny_unknown status:     allowed
    Max kernel policy version:      28
    
为了保证正确的安全上下文，你可以[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")`restorecond.service`服务。 

若要在不重启系统的情况下切换到**强制(enforcing)** 模式，可以使用以下命令： 
    
    # echo 1 > /sys/fs/selinux/enforce
    
###  交换文件

如果你使用的是交换文件(swap file)而非交换分区(swap partition)，请运行以下命令以设置正确的安全上下文： 
    
    # semanage fcontext -a -t swapfile_t "_/path/to/swapfile_ "
    # restorecon _/path/to/swapfile_
    
##  使用 SELinux

SELinux 定义安全性的机制与传统的 Unix 访问控制(DAC)不同。理解它的最佳方式是通过实例。例如，Apache 主页文件的 SELinux 安全上下文如下所示： 
    
    $ ls -lZ /var/www/html/index.html
    
    -rw-r--r--  username username system_u:object_r:httpd_sys_content_t /var/www/html/index.html

任何(Arch) Linux 用户都应该熟悉前三个字段和最后一个字段。第四字段是新增内容，格式如下： 
    
    用户(user):角色(role):类型(type)[:级别(level)]
    
解释: 

  1. **用户(User)：** SELinux 用户身份。他可以关联到一个或多个该用户允许使用的角色。
  2. **角色(Role)：** SELinux 角色。他可以关联到一个或多个该用户允许访问的类型。
  3. **类型(Type)：** 当类型与进程关联时，它定义了该进程（即域/Domain）可以访问哪些资源。当类型与对象（如文件）关联时，它定义了主体对该对象拥有的访问权限。
  4. **级别(Level)：** 此可选字段也称为“范围(range)”，仅在策略支持 MCS 或 MLS 时出现。

如果你想了解如何构建自己的策略，这些基础知识至关重要，因为它们是 SELinux 的基本构建基块。但在大多数情况下无需深入了解，因为参考策略(Reference Policy)已经足够成熟。不过，如果你是高级用户或有非常特定需求的人，学习如何制作自己的 SELinux 策略将是理想的选择。 

[这系列文章](<https://web.archive.org/web/20210310014356/http://www.fosteringlinux.com/tag/selinux/>)是寻求理解如何使用 SELinux 的绝佳资源。 

##  故障排除

查找 SELinux 错误的主要地方是[systemd/Journal](<../zh-cn/Systemd/Journal.html> "Systemd/Journal")。例如，若要查看与`system_u:system_r:policykit_t:s0`标签相关的 SELinux 消息，你需要运行： 
    
    # journalctl _SELINUX_CONTEXT=system_u:system_r:policykit_t:s0
    
###  实用工具

以下是一些能对使用 SELinux 提供极大帮助的工具和命令： 

restorecon
    根据参考策略(Reference Policy)规则恢复文件或目录的上下文（配合`-R`参数可进行递归处理）。
chcon
    修改特定文件的上下文。

###  报告问题

请在Github上报告相关问题：<https://github.com/archlinuxhardened/selinux/issues>

##  参见

  * [Security Enhanced Linux](<https://en.wikipedia.org/wiki/Security-Enhanced_Linux> "wikipedia:Security-Enhanced Linux")
  * [Gentoo:SELinux](<https://wiki.gentoo.org/wiki/SELinux> "gentoo:SELinux")
  * [Fedora:SELinux](<https://fedoraproject.org/wiki/SELinux> "fedora:SELinux")
  * [NSA's Official SELinux Homepage](<https://web.archive.org/web/20201022103915/https://www.nsa.gov/what-we-do/research/selinux/>)
  * [SELinux Project Homepage](<https://github.com/SELinuxProject>)
    * [Reference Policy Homepage](<https://github.com/SELinuxProject/refpolicy/wiki>)
    * [SETools Homepage](<https://github.com/SELinuxProject/setools/wiki>)
  * [ArchLinux, SELinux and You (archived)](<https://web.archive.org/web/20140816115906/http://jamesthebard.net/archlinux-selinux-and-you-a-trip-down-the-rabbit-hole/>)

  1. [↑](<#cite_ref-1>) <https://lists.archlinux.org/archives/list/arch-general@lists.archlinux.org/message/4LXUXQSFEPVLN7S2DDBIGVUS7L7ES5S2/>
  2. [↑](<#cite_ref-2>) <https://lists.archlinux.org/archives/list/arch-general@lists.archlinux.org/message/VM72SI36VDX4PVUP4ZZEDIOSBVYTI7OG/>
