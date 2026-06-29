相关文章

  * [Archiso as pxe server](</wzh/index.php?title=Archiso_as_pxe_server&action=edit&redlink=1> "Archiso as pxe server（页面不存在）")
  * [Offline installation](<../zh-cn/Offline_installation.html> "Offline installation")
  * [USB flash installation medium](<../zh-cn/USB_flash_installation_medium.html> "USB flash installation medium")

**翻译状态：**

  * 本文（或部分内容）译自 [archiso](<https://wiki.archlinux.org/title/archiso> "arch:archiso")，最近一次同步于 2025-01-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/archiso?diff=0&oldid=819941>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/archiso_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Archiso](<https://gitlab.archlinux.org/archlinux/archiso>) 是一个高度可定制的工具，用于构建 Arch Linux live CD/USB ISO 映像。[官方映像](<https://archlinux.org/download/>)是用 archiso 构建的，包含[这些软件包](<https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/configs/releng/packages.x86_64>)。它可以用作救援系统、linux 安装程序或其他系统的基础。这篇 Wiki 文章介绍了如何安装 archiso，以及如何配置它以控制生成的 ISO 映像的各个方面，例如随附的软件包和文件。 技术需求和构建步骤可以在[官方项目文档](<https://gitlab.archlinux.org/archlinux/archiso/tree/master/docs>)中找到。 archiso 通过许多 bash 脚本实现。 archiso 的核心组件是 _mkarchiso_ 命令。 它的选项记录在 _mkarchiso -h_ 中，这里不作介绍。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [archiso](<https://archlinux.org/packages/?name=archiso>)包 或 [archiso-git](<https://aur.archlinux.org/packages/archiso-git/>)AUR 包。 

##  准备自定义配置文件

Archiso 带有两个配置文件，**releng** 和 **baseline** 。 

  * **releng** 用于创建正式的每月安装ISO。它可以作为创建自定义ISO映像的起点。

  * **baseline** 是一种最低限度的配置，它只包括从介质启动 Live 环境所需的最低限度的软件包。

要构建配置文件的未修改版本，请参阅 [#构建 ISO 映像](<#%E6%9E%84%E5%BB%BA_ISO_%E6%98%A0%E5%83%8F>)。否则，如果您希望调整或自定义 archiso 的已发布配置文件之一，请将其从 `/usr/share/archiso/configs/_profile-name_ /` 复制到一个可写目录，并使用您的名称选择。例如： 
    
    $ cp -r /usr/share/archiso/configs/releng/ archlive
    
现在，根据所选的配置文件和您的目标进入不同的章节。 

###  配置文件结构

Archiso 配置文件包含定义生成的 ISO 映像的配置。配置文件结构记录在 `/usr/share/doc/archiso/README.profile.rst`[[1]](<https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/docs/README.profile.rst>)。 

###  选择包

编辑 `packages.x86_64` 以选择要在 Live 系统映像上安装的软件包，逐行列出软件包。 

####  自定义本地仓库

要添加不在标准 Arch 仓库中的包（例如来自 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 或采用 [ABS](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "ABS") 定制的包），请建立一个[自建本地仓库](<../zh-cn/Custom_local_repository.html> "Custom local repository")并将您的自定义包添加到其中。然后将您的仓库添加到 `pacman.conf`，如下所示： 
    
    _archlive_ /pacman.conf
    
    ...
    [_customrepo_]
    SigLevel = Optional TrustAll
    Server = file://_/path/to/customrepo_
    ...

**注意：**

  * `pacman.conf` 中的顺序很重要。要为您的自定义存储库提供最高优先级，请将其置于其他存储库条目之上。
  * 这个 `pacman.conf` 仅用于在构建映像，而不会在 live 环境中有效。要在 live 环境里使用，请参考 [#向映像中添加仓库](<#%E5%90%91%E6%98%A0%E5%83%8F%E4%B8%AD%E6%B7%BB%E5%8A%A0%E4%BB%93%E5%BA%93>)
  * 确保 _mkarchiso_ 过程（包括 chroot）可以访问仓库，应将仓库放在合适的目录下（如 `/tmp`），以确保映像构建时正确读取仓库。

####  安装 multilib 中的软件包

要从 [Multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 资源库中安装软件包，仅需在`pacman.conf`中取消注释如下的相关行以启用 _multilib_ ： 
    
    [multilib]
    Include = /etc/pacman.d/mirrorlist
    
###  向映像里添加文件

Airootfs 目录用作映像上 Live 系统的[根目录](<https://en.wikipedia.org/wiki/Root_directory> "wikipedia:Root directory") (`/`) 的起点。在安装包之前，它的所有内容都将被复制到工作目录中。 

将任何自定义文件和/或目录放在 `airootfs/` 下的所需位置。例如，如果您在当前系统上有一组 iptables 脚本，您希望在您的 Live 映像上使用它们，请按如下方式复制它们： 
    
    $ cp -r /etc/iptables _archlive_ /airootfs/etc
    
同样，对于驻留在层次结构中某处的特殊配置文件也需要格外小心。使用 [mkdir(1)](<https://man.archlinux.org/man/mkdir.1>) 可以轻松地创建目录结构的缺失部分。 

**提示：** 要将文件添加到安装用户的主目录，请将其放在 `_archlive_ /airootfs/root/` 中。要将文件添加到所有其他用户的主目录，请将其放在 `_archlive_ /airootfs/etc/skel/`。

**注意：** 与软件包提供的冲突的自定义文件将被覆盖，除非软件包将它们指定为 [备份文件](<../zh-cn/Pacman/Pacnew_and_Pacsave.html#Package_backup_files> "Pacman/Pacnew and Pacsave")。

默认情况下，[权限](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "Permissions")将是 `644` （对于文件）和 `755`（对于目录）。所有这些都将归根用户所有。要为特定文件和/或文件夹设置不同的权限或所有权，请使用 `profiledef.sh` 中的 `file_permissions` 关联列表。有关详细信息，请参阅 [README.profile.rst](<https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/docs/README.profile.rst>)。 

###  向映像中添加仓库

要在 live 环境中添加一个可用的仓库，请创建一个[适当修改](<../zh-cn/Pacman.html#%E4%BB%93%E5%BA%93%E5%92%8C%E9%95%9C%E5%83%8F> "Pacman")的`pacman.conf`，并将其置于` _archlive_ /airootfs/etc/`下。 

若仓库也使用密钥，将密钥放置在 `_archlive_ /airootfs/usr/share/pacman/keyrings/` 下。密钥文件名须以 `.gpg` 结尾。并且，密钥必须被信任。可以在同目录下创建 GnuPG 导出的信任文件，来实现这一点。文件名须以 `-trusted` 结尾。文件的第一部分是密钥指纹，第二部分是信任信息。您可以参考 `/usr/share/pacman/keyrings/archlinux-trusted` 作为实例。 

####  archzfs 实例

实例中文件如下： 
    
    airootfs
    ├── etc
    │   ├── pacman.conf
    │   └── pacman.d
    │       └── archzfs_mirrorlist
    └── usr
        └── share
            └── pacman
                └── keyrings
                    ├── archzfs.gpg
                    └── archzfs-trusted
    
    airootfs/etc/pacman.conf
    
    ...
    [archzfs]
    Include = /etc/pacman.d/archzfs_mirrorlist
    ...
    
    airootfs/etc/pacman.d/archzfs_mirrorlist
    
    Server = https://archzfs.com/$repo/$arch
    Server = https://mirror.sum7.eu/archlinux/archzfs/$repo/$arch
    Server = https://mirror.biocrafting.net/archlinux/archzfs/$repo/$arch
    Server = https://mirror.in.themindsmaze.com/archzfs/$repo/$arch
    Server = https://zxcvfdsa.com/archzfs/$repo/$arch
    
    airootfs/usr/share/pacman/keyrings/archzfs-trusted
    
    DDF7DB817396A49B2A2723F7403BD972F75D9D76:4:

`archzfs.gpg`本身可直接从 <https://archzfs.com/archzfs.gpg> 的仓库网站获取。 

###  内核

尽管两个 Archiso 包含的配置文件都只有[linux](<https://archlinux.org/packages/?name=linux>)包，但可以使映像包含其他甚至多个[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernels")。 

首先，编辑 `packages.x86_64` 以包含您想要的内核包名称。当 _mkarchiso_ 运行时，它将包括所有 `_work_dir_ /airootfs/boot/vmlinuz-*` 和 `_work_dir_ /boot/initramfs-*.img` ISO 中的文件（以及用于 UEFI 引导的 FAT 映像中）。 

[mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 默认情况下预设将构建后备 initramfs 映像。对于 ISO，主 initramfs 映像通常不包含 `autodetect` 挂钩，因此不需要额外的备用映像。为防止创建后备 initramfs 映像，使其不占用空间或减慢构建过程，请在 `_archlive_ /airootfs/etc/mkinitcpio.d/_pkgbase_.preset` 中放置自定义预设。例如，对于 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包： 
    
    _archlive_ /airootfs/etc/mkinitcpio.d/linux-lts.preset
    
    PRESETS=('archiso')
    
    ALL_kver='/boot/vmlinuz-linux-lts'
    ALL_config='/etc/mkinitcpio.conf'
    
    archiso_image="/boot/initramfs-linux-lts.img"

最后，创建[引导加载程序配置](<#%E5%BC%95%E5%AF%BC%E5%99%A8>)文件来启动内核。 

###  引导器

Archiso 支持 [syslinux](<../zh-cn/Syslinux.html> "Syslinux") 用于 BIOS 引导和 [systemd-boot](<../zh-cn/GRUB.html> "GRUB") 或 [GRUB](<../zh-cn/GRUB.html> "GRUB") 用于 UEFI 引导。有关其配置语法的信息，请参阅引导加载程序的文章。 

**提示：**

  * 当使用 El Torito 刻录到光盘时，或使用 [Isohybrid](<https://wiki.syslinux.org/wiki/index.php?title=Isohybrid>) 写入硬盘（或 USB 闪存驱动器或类似驱动器）时， _releng'_ 配置文件默认构建到支持 BIOS 和 UEFI 启动的 ISO 中。
  * 由于 isolinux 的模块化特性，您可以使用许多插件，因为所有 _.c32_ 文件都已复制并可供您使用。看看 [官方 syslinux 站点](<https://wiki.syslinux.org/wiki/index.php/SYSLINUX>) 和 [configs/releng/syslinux archiso git repo](<https://gitlab.archlinux.org/archlinux/archiso/-/tree/master/>)。使用所述插件，可以制作具有视觉吸引力的复杂菜单。参见 [[1]](<https://wiki.syslinux.org/wiki/index.php?title=Comboot/menu.c32>)。

mkarchiso 期望 [GRUB](<../zh-cn/GRUB.html> "GRUB") 配置位于 `grub` 目录中，[systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") 配置位于 `efiboot` 目录中，而 [syslinux](<../zh-cn/Syslinux.html> "Syslinux") 配置位于 `syslinux` 目录中。 

####  UEFI 安全启动

如果要使 archiso 在启用 UEFI 安全启动的环境下可启动，则必须使用签名过的启动加载程序。您可以按照 [安全启动#引导安装介质](<../zh-cn/Secure_Boot.html#%E5%BC%95%E5%AF%BC%E5%AE%89%E8%A3%85%E4%BB%8B%E8%B4%A8> "Secure Boot") 中的说明进行操作。 

###  systemd 单元

要为 Live 环境 [启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") systemd 服务/套接字/计时器，您需要像 `systemctl enable` 那样手动创建符号链接。 

例如，要启用包含 `WantedBy=multi-user.target` 的 `gpm.service`，请运行： 
    
    $ mkdir -p _archlive_ /airootfs/etc/systemd/system/multi-user.target.wants
    $ ln -s /usr/lib/systemd/system/gpm.service _archlive_ /airootfs/etc/systemd/system/multi-user.target.wants/
    
可以通过读取 systemd 单元找到所需的符号链接，或者如果您安装了服务，则通过 [启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") 它并观察 systemctl 输出。 

####  登录管理器

通过启用登录管理器的 [systemd](<../zh-cn/Systemd.html> "Systemd") 服务来在启动时 Start X。如果您不知道要启用哪个 _.service_ ，您可以轻松找出是否在您构建 ISO 的系统上使用相同的程序。只需使用： 
    
    $ ls -l /etc/systemd/system/display-manager.service
    
现在在 `_archlive_ /airootfs/etc/systemd/system/` 中创建相同的符号链接。对于 LXDM： 
    
    $ ln -s /usr/lib/systemd/system/lxdm.service _archlive_ /airootfs/etc/systemd/system/display-manager.service
    
这将在您的 Live 系统上的系统启动时启用 LXDM。 

###  改变自动登录

Getty 的自动登录配置位于 `airootfs/etc/systemd/system/getty@tty1.service.d/autologin.conf`。 

您可以修改这个文件来更改自动登录用户： 
    
    [Service]
    ExecStart=
    ExecStart=-/sbin/agetty --autologin _**username**_ --noclear %I 38400 linux
    
或者干脆删除 `autologin.conf` 来禁用自动登录。 

如果使用串行控制台，请创建 `airootfs/etc/systemd/system/serial-getty@ttyS0.service.d/autologin.conf` 并添加以下内容： 

###  用户和密码

要创建在 Live 环境中可用的 [用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "User")，您必须手动编辑 `_archlive_ /airootfs/etc/passwd`、` _archlive_ /airootfs/etc/shadow`、` _archlive_ /airootfs/etc/group` 和 `_archlive_ /airootfs/etc/gshadow`。 

**注意：** 如果这些文件存在，它们必须包含 root 用户和组。

例如，添加用户 `archie`。按照 [passwd(5)](<https://man.archlinux.org/man/passwd.5>) 语法将它们添加到 `_archlive_ /airootfs/etc/passwd` ： 
    
    _archlive_ /airootfs/etc/passwd
    
    root:x:0:0:root:/root:/usr/bin/zsh
    archie:x:1000:1000::/home/archie:/usr/bin/zsh
    
**注意：**`passwd` 文件须以换行符结尾。

按 [shadow(5)](<https://man.archlinux.org/man/shadow.5>) 的语法将用户添加到 `_archlive_ /airootfs/etc/shadow`。若要为用户设置密码，请使用 `openssl passwd -6` 生成密码哈希值，并将其添加到文件中。例如： 
    
    _archlive_ /airootfs/etc/shadow
    
    root::14871::::::
    archie:$6$randomsalt$cij4/pJREFQV/NgAgh9YyBIoCRRNq2jp5l8lbnE5aLggJnzIRmNVlogAg8N6hEEecLwXHtMQIl2NX2HlDqhCU1:14871::::::

您也可以将密码字段留空。这意味着，该用户无需密码即可登录。 

根据 [group(5)](<https://man.archlinux.org/man/group.5>) 将用户的组和他们将加入的组添加到 `_archlive_ /airootfs/etc/group`。例如： 
    
    _archlive_ /airootfs/etc/group
    
    root:x:0:root
    adm:x:4:archie
    wheel:x:10:archie
    uucp:x:14:archie
    archie:x:1000:

根据 [gshadow(5)](<https://man.archlinux.org/man/gshadow.5>) 创建相应的 `_archlive_ /airootfs/etc/gshadow`： 
    
    _archlive_ /airootfs/etc/gshadow
    
    root:!*::root
    archie:!*::

确保 `/etc/shadow` 和 `/etc/gshadow` 具有正确的权限： 
    
    _archlive_ /profiledef.sh
    
    ...
    file_permissions=(
      ...
      ["/etc/shadow"]="0:0:0400"
      ["/etc/gshadow"]="0:0:0400"
    )

☢软件包安装后， _mkarchiso_ 将为 `_archlive_ /airootfs/etc/passwd` 中列出的用户创建所有指定的主目录并复制 `_work_directory_ /x86_64/ airootfs/etc/skel/*` 给他们。复制的文件将具有适当的用户和组所有权。 

###  更改 ISO 中使用的分发名称

首先将文件 `/etc/os-release` 复制到 rootfs 的 `etc/` 文件夹中。然后，相应地编辑文件。您还可以更改 GRUB 和 syslinux 内部的名称。 

##  构建 ISO 映像

通过运行以下命令构建一个 ISO 映像，然后您可以将其刻录到 CD 或 USB： 
    
    # mkarchiso -v -w _/path/to/work_dir_ -o _/path/to/out_dir_ _/path/to/profile/_
    
  * `-w` 指定工作目录。如果未指定该选项，则默认为当前目录中的 `work`。
  * `-o` 指定将放置构建的 ISO 映像的目录。如果未指定该选项，则默认为当前目录中的 `out`。
  * 需要注意的是配置文件 `profiledef.sh` 在运行 mkarchiso 时不能指定，只能指定文件的路径。

将 `_/path/to/profile/_` 替换为您的自定义配置文件的路径，或者如果您正在构建一个 `/usr/share/archiso/configs/releng/`未修改的配置文件。 

**提示：** 如果内存允许，最好将工作目录放在 [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs") 上。例如： 
    
    # mkarchiso -v -w /tmp/archiso-tmp _/path/to/profile/_
    
运行时，脚本将下载并安装您指定到 `_work_directory_ /x86_64/airootfs` 的包，创建内核和初始化映像，应用您的自定义选项，最后将 ISO 构建到输出目录中。 

###  删除工作目录

**警告：** 如果 _mkarchiso_ 被中断，运行 [findmnt(8)](<https://man.archlinux.org/man/findmnt.8>) 以确保在删除之前没有挂载绑定 - 否则，**你可能会丢失数据** （例如安装在 `/run/media/_user_ /_label_` 的外部设备绑定在 `work/x86_64/airootfs/run/media/_user_ /_label_` 在构建过程中）。

临时文件被复制到工作目录中。成功构建 ISO 后，可以删除工作目录及其内容。例如： 
    
    # rm -rf _/path/to/work_dir_
    
##  使用 ISO

有关各种选项，请参见 [Installation guide#准备安装介质](<../zh-cn/Installation_guide.html#%E5%87%86%E5%A4%87%E5%AE%89%E8%A3%85%E4%BB%8B%E8%B4%A8> "Installation guide")。 

##  在 QEMU 中测试 ISO

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") 可选依赖项 [qemu-desktop](<https://archlinux.org/packages/?name=qemu-desktop>)包 和 [edk2-ovmf](<https://archlinux.org/packages/?name=edk2-ovmf>)包。 

使用便捷脚本 `run_archiso` 使用 [QEMU](<../zh-cn/QEMU.html> "QEMU") 运行构建的映像。 
    
    $ run_archiso -i _/path/to/_ archlinux-_yyyy.mm.dd_ -x86_64.iso
    
虚拟机也可以使用 UEFI 仿真运行： 
    
    $ run_archiso -u -i _/path/to/_ archlinux-_yyyy.mm.dd_ -x86_64.iso
    
##  技巧提示

###  准备 ISO 以通过 SSH 进行安装

**注意：** 自从 `archlinux-2021.02.01-x86_64.iso`，提供[cloud-init 支持](<https://gitlab.archlinux.org/archlinux/archiso/-/tree/bd2b861aa39167e4fc658a354071b95fbd050c0f/configs/releng/airootfs/etc/systemd/system/cloud-init.target.wants>)，`sshd.service`是[默认启用的](<https://gitlab.archlinux.org/archlinux/archiso/-/blob/bd2b861aa39167e4fc658a354071b95fbd050c0f/configs/releng/airootfs/etc/systemd/system/multi-user.target.wants/sshd.service>)。

要 [通过 SSH 安装 Arch Linux](<../zh-cn/Install_Arch_Linux_via_SSH.html> "Install Arch Linux via SSH") 而不与系统进行任何交互，必须将 SSH 公钥放在 `authorized_keys` 中。 

添加 SSH 密钥可以手动完成（在此处解释），也可以通过 [cloud-init](<../zh-cn/Install_Arch_Linux_via_SSH.html#Installation_on_a_headless_server> "Install Arch Linux via SSH")。 

要手动添加密钥，首先 [复制 archiso 的 releng 配置文件](<#%E5%87%86%E5%A4%87%E8%87%AA%E5%AE%9A%E4%B9%89%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>) 到可写目录。以下示例使用 `archlive`。 
    
    $ cp -r /usr/share/archiso/configs/_profile/_ archlive
    
在将用于登录的用户的主目录中创建一个 `.ssh` 目录。以下示例将使用 root 用户。 
    
    $ mkdir archlive/airootfs/root/.ssh
    
将用于登录的 SSH 公钥添加到 `authorized_keys`： 
    
    $ cat ~/.ssh/_key1_.pub >> archlive/airootfs/root/.ssh/authorized_keys
    $ cat ~/.ssh/_key2_.pub >> archlive/airootfs/root/.ssh/authorized_keys
    
为 `.ssh` 目录和 `authorized_keys` 文件设置正确的 [权限](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "Permissions") 和所有权： 
    
    archlive/profiledef.sh
    
    ...
    file_permissions=(
      ...
      ["/root"]="0:0:0750"
      ["/root/.ssh"]="0:0:0700"
      ["/root/.ssh/authorized_keys"]="0:0:0600"
    )

最终 [构建 ISO 映像](<#%E6%9E%84%E5%BB%BA_ISO_%E6%98%A0%E5%83%8F>)。启动 ISO 后，[OpenSSH](<../zh-cn/OpenSSH.html> "OpenSSH") 将启动，并且可以使用相应的 SSH 私钥登录。 

###  使用 iwd 自动连接到 Wi-Fi 网络

在配置文件的 `airootfs` 目录中创建 `/var/lib/iwd/` 并设置正确的权限： 
    
    $ mkdir -p _archlive_ /airootfs/var/lib/iwd
    
    archlive/profiledef.sh
    
    ...
    file_permissions=(
      ...
      ["/var/lib/iwd"]="0:0:0700"
    )

按照 [iwd#Network configuration](<../zh-cn/Iwd.html#Network_configuration> "Iwd") 和 [iwd.network(5)](<https://man.archlinux.org/man/iwd.network.5>) 中的说明为您的 Wi-Fi 网络创建网络配置文件。 

将配置文件保存在 `_archlive_ /airootfs/var/lib/iwd/` 中。 

###  调整根文件系统的大小

在 live 环境中，例如在需要使用 [DKMS](<../zh-cn/DKMS.html> "DKMS") 模块的硬件上安装软件包时，根文件系统的默认大小可能不允许包的下载和安装。 

**提示：** 选中大小的理由请参见 [BBS#210389](<https://bbs.archlinux.org/viewtopic.php?pid=1628972#p1628972>)，历史细节请参见 [FS#45618](<https://bugs.archlinux.org/task/45618>)。

当在 live 环境中下载文件或安装软件包时，它将表现为以下错误信息： 
    
    error: partition / too full: 63256 blocks needed, 61450 blocks free
    error: not enough free disk space
    error: failed to commit transaction (not enough free disk space)
    Errors occurred: no packages were upgraded.
    
您亦可通过运行以下命令以动态调整根分区大小： 
    
    # mount -o remount,size=_SIZE_ /run/archiso/cowspace
    
关于 `_SIZE_` 可能的参数，请参见 [tmpfs(5) § size](<https://man.archlinux.org/man/tmpfs.5#size>)。 

要在引导程序阶段调整大小（按 `e` 或 `Tab`），请使用以下引导选项： 
    
    cow_spacesize=_SIZE_
    
要在构建映像阶段调整大小，请将引导选项添加至： 

  * `efiboot/loader/entries/*.cfg`
  * `grub/*.cfg`
  * `syslinux/*.cfg`

您可以通过运行以下命令检查文件系统的大小： 
    
    $ df -h
    
查看 mkinitcpio-archiso 启动参数于[此](<https://gitlab.archlinux.org/mkinitcpio/mkinitcpio-archiso/blob/master/docs/README.bootparams>)

###  Google Compute Engine 映像

Google Compute Engine 兼容的 `releng` 压缩映像以 [archlinux-gce](<https://aur.archlinux.org/packages/archlinux-gce/>)AUR 的形式提供。 

###  Libvirt 虚拟机配置

运行 `releng` 映像的 [libvirt](<../zh-cn/Libvirt.html> "Libvirt") 配置可用作 [archlinux-libvirt](<https://aur.archlinux.org/packages/archlinux-libvirt/>)AUR。 

##  疑难解答

###  窗口管理器冻结

如果您想在 Live CD 中使用[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")，则必须添加必要且正确的[显卡驱动](</wzh/index.php?title=%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8&action=edit&redlink=1> "显卡驱动（页面不存在）")，否则 WM 可能会在加载时冻结。 

##  参见

  * [Archiso 项目主页](<https://gitlab.archlinux.org/archlinux/archiso>)
  * [官方档案](<https://gitlab.archlinux.org/archlinux/archiso/-/tree/master/docs>)
  * [Arch Linux 发布工程邮件列表](<https://lists.archlinux.org/mailman3/lists/arch-releng.lists.archlinux.org/>)
  * [#archlinux-releng——Arch Linux 发布工程 IRC 频道](<ircs://irc.libera.chat/archlinux-releng>)
  * [archiso-manager——用于构建官方每月 ISO 的工具](<https://github.com/pierres/archiso-manager>)
