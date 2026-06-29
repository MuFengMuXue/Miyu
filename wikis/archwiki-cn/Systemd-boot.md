**翻译状态：**

  * 本文（或部分内容）译自 [Systemd-boot](<https://wiki.archlinux.org/title/Systemd-boot> "arch:Systemd-boot")，最近一次同步于 2025-08-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Systemd-boot?diff=0&oldid=845136>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Systemd-boot_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Arch 的启动流程](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html> "Arch 的启动流程")
  * [安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")
  * [UEFI](<../zh-cn/UEFI.html> "UEFI")

[systemd-boot(7)](<https://man.archlinux.org/man/systemd-boot.7>)（有时被称为 _sd-boot_ ），曾用名 **gummiboot** （德语里“橡皮筏”的意思），是一款易于配置的 [UEFI](<../zh-cn/UEFI.html> "UEFI") [引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")。它提供了一个用于选择启动项的文本菜单，以及一个用于配置内核命令行的编辑器。 

注意， _systemd-boot_ 只能从安装到的 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")或同一硬盘上的扩展引导加载程序分区（XBOOTLDR 分区）启动 EFI 可执行程序（例如 Linux 内核 [EFI boot stub](</wzh/index.php?title=EFI_boot_stub&action=edit&redlink=1> "EFI boot stub（页面不存在）")，[UEFI shell](<../zh-cn/UEFI_shell.html> "UEFI shell")，[GRUB](<../zh-cn/GRUB.html> "GRUB") 或者 [Windows Boot Manager](<https://learn.microsoft.com/en-us/windows-hardware/drivers/bringup/boot-and-uefi#understanding-the-windows-boot-manager>)）。 

**注意：** 本文将使用 `_esp_` 指代 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")的挂载点，以及使用 `_boot_` 指代可选 XBOOTLDR 分区的挂载点。下文将假设你已经 [chroot](<../zh-cn/Chroot.html> "Chroot") 到了系统挂载点下。

##  支持的文件系统

systemd-boot [从固件](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#UEFI> "Arch 的启动流程")继承了文件系统兼容性（例如至少支持 FAT12，FAT16 和 FAT32），还可以加载 `_esp_ /EFI/systemd/drivers/` 目录下的 [UEFI 驱动](<../zh-cn/Unified_Extensible_Firmware_Interface.html#UEFI_drivers> "Unified Extensible Firmware Interface")。 

##  安装

_systemd-boot_ 随 [systemd](<https://archlinux.org/packages/?name=systemd>)包 包一同安装，其为 [base](<https://archlinux.org/packages/?name=base>)包 元软件包的依赖，因此无需手动安装额外软件包。 

###  安装 UEFI 启动管理器

要安装 _systemd-boot_ ，首先确保启动方式是 UEFI 模式，可以访问 [UEFI 变量](<../zh-cn/Unified_Extensible_Firmware_Interface.html#UEFI_variables> "Unified Extensible Firmware Interface")。用 `efivar --list` 命令进行检查，如果没有安装 [efivar](<https://archlinux.org/packages/?name=efivar>)包 ，使用 `ls /sys/firmware/efi/efivars` （如果目录存在，则表明系统是以 UEFI 模式启动的）。 

使用 [bootctl(1)](<https://man.archlinux.org/man/bootctl.1>) 将 _systemd-boot_ 安装到 ESP： 
    
    # bootctl install
    
这将把 _systemd-boot_ UEFI 启动管理器复制到 ESP，同时为其创建一项 UEFI 启动入口，并将其设置为 UEFI 启动顺序的第一项。 

  * 在 x64 UEFI 环境中，`/usr/lib/systemd/boot/efi/systemd-bootx64.efi` 将被复制到 `_esp_ /EFI/systemd/systemd-bootx64.efi` 和 `_esp_ /EFI/BOOT/BOOTX64.EFI` 。
  * 在 IA32 UEFI 环境中，`/usr/lib/systemd/boot/efi/systemd-bootia32.efi` 将被复制到 `_esp_ /EFI/systemd/systemd-bootia32.efi` 和 `_esp_ /EFI/BOOT/BOOTIA32.EFI` 。

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 从 systemd v257 版本开始，在运行于 pid 命名空间中（例如使用 [arch-chroot(8)](<https://man.archlinux.org/man/arch-chroot.8>)）时， _bootctl_ [将不会在 NVRAM 中创建 UEFI 引导条目](<https://github.com/systemd/systemd/issues/36174>)。在尚未发布的 v258 及更新版本中，可添加以下选项来绕过该问题：`--variables=yes` (在[User talk:Scimmia#Revert on systemd-boot about sd-boot not creating EFI entries inside chroot](</wzh/index.php?title=User_talk:Scimmia&action=edit&redlink=1> "User talk:Scimmia（页面不存在）")讨论)

UEFI 启动选项将被命名为“Linux Boot Manager”，根据 [UEFI 位数](<../zh-cn/UEFI.html#UEFI_%E5%9B%BA%E4%BB%B6%E4%BD%8D%E6%95%B0> "UEFI")不同，启动选项将指向到 ESP 的 `\EFI\systemd\systemd-bootx64.efi` 或 `\EFI\systemd\systemd-bootia32.efi` 位置下。 

**注意：**

  * 在运行 `bootctl install` 时， _systemd-boot_ 会尝试在 `/efi`，`/boot` 和 `/boot/efi` 目录下寻找 ESP。可以通过 `--esp-path=_esp_` 参数指定 `_esp_` 目录（详细信息请参考 [bootctl(1) § OPTIONS](<https://man.archlinux.org/man/bootctl.1#OPTIONS>)）。
  * 安装 _systemd-boot_ 将覆盖现有的 `_esp_ /EFI/BOOT/BOOTX64.EFI`（或是 IA32 UEFI 下的 `_esp_ /EFI/BOOT/BOOTIA32.EFI`），例如 Microsoft 版本的文件。

要完成安装，请[配置](<#%E9%85%8D%E7%BD%AE>) _systemd-boot_ 。 

###  通过 XBOOTLDR 安装

[![](../File:Tango-go-next.png)](<../File:Tango-go-next.png>)**此页面或章节适合移动到[分区#多分区](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%A4%9A%E5%88%86%E5%8C%BA> "分区")。**

**附注：** 所有分区相关的信息都需要移到“分区”页，仅保留与 systemd-boot 相关的步骤。（在 [Talk:Systemd-boot](<../zh-cn/Talk:Systemd-boot.html>) 讨论）

可以单独创建一个“Linux extended boot”（XBOOTLDR）类型的 [/boot 分区](<../zh-cn/%E5%88%86%E5%8C%BA.html#/boot> "分区")将内核和 initramfs 从 ESP 中分离出来，有助于在现有 ESP 过小的情况下配置 [Arch + Windows 双系统](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html> "Arch + Windows 双系统")。 

跟随通常步骤配置 ESP，然后在同一物理硬盘上为 XBOOTLDR 创建另一分区。XBOOTLDR 分区的类型 GUID 必须是 `bc13c2ff-59e6-4262-a352-b275fd6f7172` [[1]](<https://uapi-group.org/specifications/specs/boot_loader_specification/>)（[gdisk](<../zh-cn/GPT_fdisk.html> "Gdisk") 下是 `ea00`，[fdisk](<../zh-cn/Fdisk.html> "Fdisk") 下是 `xbootldr`）。XBOOTLDR 的容量必须至少为要安装的所有内核的总大小。 

**注意：**

  * _systemd-boot_ 不会像 ESP 那样检查 XBOOTLDR 的文件系统，因此可以使用你的 UEFI 实现可读取的任意文件系统类型。
  * 在启用“快速启动”时，UEFI 可能会跳过加载除 ESP 外的所有分区，可能会导致 _systemd-boot_ 无法在 XBOOTLDR 分区上找到启动项。在这种情况下，请禁用“快速启动”。
  * XBOOTLDR 分区必须与 ESP 位于同一物理硬盘，否则 _systemd-boot_ 将无法识别到该分区。

在安装时，将 ESP 挂载到 `/mnt/efi`，将 XBOOTLDR 分区挂载到 `/mnt/boot`。 

chroot 后，执行： 
    
    # bootctl --esp-path=/efi --boot-path=/boot install
    
最后[配置](<#%E9%85%8D%E7%BD%AE>) _systemd-boot_ 。 

###  更新 EFI 启动管理器

每当 _systemd-boot_ 有新版本时，用户可以选择重新安装启动管理器。该操作可以手动或自动进行，具体方式将在下文中描述。 

**注意：** UEFI 启动管理器是一个独立 EFI 可执行文件，任意版本都可以被用于启动系统（由于 pacman 仅会安装 _systemd-boot_ 安装器而不是 _systemd-boot_ 自身，因此该项不适用于部分升级）。但是，更新版本可能会加入新功能或错误修正，因此建议持续更新 _systemd-boot_ 。

**警告：** 如果你启用了 [安全启动](<../zh-cn/Secure_Boot.html> "Secure Boot")，你需要在更新引导加载程序后为其签名。请查看下方[#为安全启动进行签名](<#%E4%B8%BA%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8%E8%BF%9B%E8%A1%8C%E7%AD%BE%E5%90%8D>)一节的相关说明。

####  手动更新

使用 _bootctl_ 更新 _systemd-boot_ ： 
    
    # bootctl update
    
**注意：** 与 `bootctl install` 类似， _systemd-boot_ 会尝试在 `/efi`，`/boot` 和 `/boot/efi` 三个位置下寻找 ESP。可以用 `--esp-path=_esp_` 参数指定 `_esp_` 位置。

####  自动更新

如果你需要自动更新 _systemd-boot_ ，你可以尝试使用 [systemd 服务](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")或 [Pacman 钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")，下方介绍了这两种方法。 

#####  systemd 服务

在版本 250 后， [systemd](<https://archlinux.org/packages/?name=systemd>)包 添加了 `systemd-boot-update.service`。[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")这个服务后将在每次启动系统时执行以下命令： 
    
    # bootctl --no-variables --graceful update
    
与[手动更新](<#%E6%89%8B%E5%8A%A8%E6%9B%B4%E6%96%B0>)类似，它会在 `/efi`、`/boot` 和 `/boot/efi` 目录下寻找 ESP。该命令将在 `/usr/lib/systemd/boot/efi/` 目录下存在新版本时更新 ESP 中安装的所有 systemd-boot。它会先寻找以 `.efi.signed` 结尾的 systemd-boot 文件，以允许用户为[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")对映像进行签名。 

#####  pacman 钩子

软件包 [systemd-boot-pacman-hook](<https://aur.archlinux.org/packages/systemd-boot-pacman-hook/>)AUR 提供了一个 Pacman 钩子，将在每次更新 [systemd](<https://archlinux.org/packages/?name=systemd>)包 后自动执行。该钩子与 [systemd 服务方式](<#systemd_%E6%9C%8D%E5%8A%A1>)不同，它会在 [systemd](<https://archlinux.org/packages/?name=systemd>)包 被更新时立即尝试更新引导管理器。 

如果不想安装 AUR 包，可以在 `/etc/pacman.d/hooks/` 目录下手动添加以下文件： 
    
    /etc/pacman.d/hooks/95-systemd-boot.hook
    
    [Trigger]
    Type = Package
    Operation = Upgrade
    Target = systemd
    
    [Action]
    Description = Gracefully upgrading systemd-boot...
    When = PostTransaction
    Exec = /usr/bin/systemctl restart systemd-boot-update.service

###  为安全启动进行签名

如果你启用了[安全启动](<../zh-cn/Secure_Boot.html> "Secure Boot")，你需要添加一个 Pacman 钩子以在更新后自动为其重新签名： 
    
    /etc/pacman.d/hooks/80-secureboot.hook
    
    [Trigger]
    Operation = Install
    Operation = Upgrade
    Type = Path
    Target = usr/lib/systemd/boot/efi/systemd-boot*.efi
    
    [Action]
    Description = Signing systemd-boot EFI binary for Secure Boot
    When = PostTransaction
    Exec = /bin/sh -c 'while read -r f; do /usr/lib/systemd/systemd-sbsign sign --private-key _/path/to/keyfile.key_ --certificate _/path/to/certificate.crt_ --output "${f}.signed" "$f"; done;'
    Depends = sh
    Depends = sbsigntools
    NeedsTargets

将 `_/path/to/keyfile.key_` 和 `_/path/to/certificate.crt_` 替换为你的签名密钥和证书，具体信息可参考 [systemd-sbsign(1)](<https://man.archlinux.org/man/systemd-sbsign.1>)。 

已经创建的 `/usr/lib/systemd/boot/efi/systemd-boot*.efi._signed_` 会自动地被 `bootctl install` 和 `bootctl update` 识别并使用。参见 [bootctl(1) § SIGNED .EFI FILES](<https://man.archlinux.org/man/bootctl.1#SIGNED_.EFI_FILES>). 

另一个选择是，使用 [UEFI/安全启动#sbctl](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html#sbctl> "UEFI/安全启动"). 

##  配置

**提示：** 修改配置后，可以不带参数执行 `bootctl` 来确保 systemd-boot 能够正常读取配置内容。

###  启动选单配置

配置文件保存于 `_esp_ /loader/loader.conf`，具体信息可参考 [loader.conf(5) § OPTIONS](<https://man.archlinux.org/man/loader.conf.5#OPTIONS>) 。 

以下是一个简单的示例： 
    
    _esp_ /loader/loader.conf
    
    default  arch.conf
    timeout  4
    console-mode max
    editor   no
    
**提示：**

  * systemd-boot 不支持使用制表符进行缩进，请使用空格进行替代。
  * `default` 和 `timeout` 可在启动选单中修改，变更将覆盖保存到 `LoaderEntryDefault` 和 `LoaderConfigTimeout` 这两个 UEFI 变量中。
  * `bootctl set-default ""` 和 `bootctl set-timeout ""` 可分别用于清除覆盖了 `default` and `timeout` 选项的 UEFI 变量。
  * 如果你设置了 `timeout 0`，可以通过按下`空格键`来访问启动菜单。
  * 基本配置文件示例位于 `/usr/share/systemd/bootctl/loader.conf`。
  * 如果在选择启动项页面时菜单显示异常或分辨率不对，可以尝试将 `console-mode` 设置为 `auto`（启发式选择最佳分辨率），`keep`（保持固件提供的分辨率）或 `2`（尝试使用第一个非 UEFI 标准的分辨率）。

####  记住上一次的启动项

可以将默认启动项设为 `@saved` 来记住上次使用的启动项。该选项对 Windows 双系统或 Windows 更新自动启动到了 Linux 的情况非常有用。 
    
    _esp_ /loader/loader.conf
    
    default @saved
    ...
    
更多信息请参考 [loader.conf(5)](<https://man.archlinux.org/man/loader.conf.5>)。 

###  增加启动选项

_systemd-boot_ 会在它启动的 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")下的 `/loader/entries/` 目录和同硬盘下的 [XBOOTLDR](<#%E9%80%9A%E8%BF%87_XBOOTLDR_%E5%AE%89%E8%A3%85>) 分区中寻找 _.conf_ 文件。 

**注意：**

  * `_esp_ /loader/entries/*.conf` 下的启动项只能调用 `_esp_` 下的文件（例如内核，initramfs，映像等），` _boot_ /loader/entries/*.conf` 下的启动项也一样只能调用 `_boot_` 下的文件。
  * 文件路径参数是相对于 EFI 系统分区或 XBOOTLDR 分区的根的。例如，如果你的 EFI 系统分区或 XBOOTLDR 挂载到了 `/boot` 目录，那么就必须在 `linux` 参数中将 `/boot/vmlinuz-linux` 指定为 `/vmlinuz-linux`。
  * 启用[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")后，内嵌 `.cmdline` 的[统一内核映像（UKI）](<../zh-cn/Unified_kernel_image.html> "Unified kernel image")将忽略所有传入的命令行选项（无论是使用 `options` 传入启动选项还是交互式传入的）。当未启用安全启动时，通过命令行传入的选项会覆盖掉 `.cmdline` 内置的选项。

以下为从卷启动 Arch 的启动选项文件示例，其中卷的 [UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID") 为 `_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx_`： 
    
    _esp_ /loader/entries/arch.conf
    
    title   Arch Linux
    linux   /vmlinuz-linux
    initrd  /initramfs-linux.img
    options root=UUID=_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx_ rw
    
    _esp_ /loader/entries/arch-fallback.conf
    
    title   Arch Linux (fallback initramfs)
    linux   /vmlinuz-linux
    initrd  /initramfs-linux-fallback.img
    options root=UUID=_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx_ rw

所有配置选项可参考[引导加载器规范](<https://uapi-group.org/specifications/specs/boot_loader_specification/#type-1-boot-loader-specification-entries>)。 

_systemd-boot_ 会在启动时自动搜索位于 `/EFI/Microsoft/Boot/Bootmgfw.efi` 的 **Windows Boot Manager** ，固件中的 **Apple macOS Boot Manager** ，`/shellx64.efi`（[UEFI shell](<../zh-cn/UEFI_shell.html> "UEFI shell")）和 `/EFI/BOOT/bootx64.efi`（**EFI Default Loader** ），同时也会在 `/EFI/Linux/` 内查找内核文件。在检测到后，会自动生成名称分别为 `auto-windows`，`auto-osx`，`auto-efi-shell` 和 `auto-efi-default` 的启动选项，因此这些选项不需要手动配置引导器。但和 [rEFInd](<../zh-cn/REFInd.html> "REFInd") 不同，不会为其它 EFI 应用程序创建启动选项，所以这些还需要进行进一步设置。 

**提示：**

  * 可以用 `bootctl list` 列出所有可用启动选项。
  * 启动选项配置示例位于 `/usr/share/systemd/bootctl/arch.conf` 。
  * 适用于如 [LVM](<../zh-cn/LVM.html> "LVM")，[LUKS](<../zh-cn/Dm-crypt.html> "LUKS")，[dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt") 或 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 的[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")可在对应的页面中获取。

**注意：** 如果使用了[外置微码 initramfs 映像](<../zh-cn/%E5%BE%AE%E7%A0%81.html#Microcode_in_a_separate_initramfs_file> "微码")（如使用了 [Booster](<../zh-cn/Booster.html> "Booster") 作为 initramfs 生成器），那么必须在单独的 `initrd` 中指定 `/boot/amd-ucode.img` 或`/boot/intel-ucode.img`，并将其放置到主 initramfs 之前的**首位** 。

####  UEFI Shells 或其他 EFI 应用程序

如果你通过 [edk2-shell](<https://archlinux.org/packages/?name=edk2-shell>)包 安装了 [UEFI shell](<../zh-cn/UEFI_shell.html> "UEFI shell")，那么在对应 EFI 文件放置到了 `_esp_ /shellx64.efi` 的情况下 _systemd-boot_ 会自动检测到并为其创建新启动选项。 要启用自动检测，可以在安装软件包后执行如下命令： 
    
    # cp /usr/share/edk2-shell/x64/Shell.efi /boot/shellx64.efi
    
另外如果你安装了[其他 EFI 应用程序](<../zh-cn/REFInd.html#%E5%B7%A5%E5%85%B7> "REFInd")到 ESP，也可以像这样进行加载： 

**注意：**`efi` 参数的文件路径是相对于你的 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")的。如果你的 EFI 系统分区挂载到了 `/boot`，且你的 EFI 二进制文件位于 `/boot/EFI/xx.efi` 和 `/boot/yy.efi`，那么你需要指定对应参数分别为 `efi /EFI/xx.efi` 和 `efi /yy.efi`。
    
    _esp_ /loader/entries/fwupd.conf
    
    title  Firmware updater
    efi     /EFI/tools/fwupdx64.efi
    
    _esp_ /loader/entries/gdisk.conf
    
    title  GPT fdisk (gdisk)
    efi     /EFI/tools/gdisk_x64.efi
    
#####  Memtest86+

首先需要安装 [memtest86+-efi](<https://archlinux.org/packages/?name=memtest86%2B-efi>)包。如果使用了安全启动，需要同时对 EFI 二进制文件进行签名。 
    
    _esp_ /loader/entries/memtest.conf
    
    title Memtest86+
    efi /memtest86+/memtest.efi
    
#####  网络引导

_systemd-boot_ 可以串联加载[网络引导](<../zh-cn/%E7%BD%91%E7%BB%9C%E5%BC%95%E5%AF%BC.html> "网络引导")。下载 `ipxe-arch.efi` EFI 二进制文件和签名，验证并将其放置到如 `_esp_ /EFI/arch_netboot/arch_netboot.efi` 的位置下： 
    
    _esp_ /loader/entries/arch_netboot.conf
    
    title Arch Linux Netboot
    efi /EFI/arch_netboot/arch_netboot.efi
    
##### GRUB

_systemd-boot_ 可以串联加载 [GRUB](<../zh-cn/GRUB.html> "GRUB")。`grubx64.efi` 二进制文件的位置与安装 GRUB 到 ESP 时使用的 `--bootloader-id=` 参数一致。 
    
    _esp_ /loader/entries/grub.conf
    
    title GRUB
    efi /EFI/GRUB/grubx64.efi
    
####  从其它硬盘启动

_systemd-boot_ [不能](<https://github.com/systemd/systemd/issues/3252>)从它启动的 ESP 或 XBOOTLDR 分区所在硬盘外的分区中启动 EFI 二进制文件，但可以引导其它 [UEFI shell](<../zh-cn/UEFI_shell.html> "UEFI shell") 进行这一操作。 

首先，按照[上面的步骤](<#UEFI_Shells_%E6%88%96%E5%85%B6%E4%BB%96_EFI_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F>)安装 [edk2-shell](<https://archlinux.org/packages/?name=edk2-shell>)包。接着，在 UEFI shell 环境下，使用 _map_ 命令获取带有对应 PARTUUID 的分区的 **FS alias** （例如 HD0a66666a2、HD0b、FS1 或 BLK7）并记录下来。 

下一步，使用 `exit` 命令启动回到 LInux 环境，然后创建一条新启动选项来通过 UEFI shell 启动目标 EFI 应用： 
    
    _esp_ /loader/entries/windows.conf
    
    title   Windows
    efi     /shellx64.efi
    options -nointerrupt -nomap -noversion HD0b:EFI\Microsoft\Boot\Bootmgfw.efi
    
确保 `efi` 路径和复制到 _esp_ 路径下的 `shellx64.efi` 位置一致。顺带一提，可以将 `shellx64.efi` EFI 文件移动到其它位置来防止 _systemd-boot_ 自动创建启动选项。 

将 `HD0b` 替换为之前记录的 _FS alias_ 。 

  * `-nointerrupt` 选项可以避免通过 `Ctrl+c` 选项终端目标 EFI 程序允许。
  * `-nomap -noversion` 选项会隐藏掉默认 UEFI shell 欢迎信息。
  * 如需让 UEFI shell 在目标 EFI 程序退出后（如出现错误等原因）自动回到启动引导器，可以添加 `-exit` 选项。
  * 如果 UEFI shell 还会出现无用输出，可以添加 `-noconsoleout` 选项。

###  启动到 UEFI 固件设置

如果你设备的固件支持从操作系统重启到固件设置，那 systemd-boot 会自动检测到并添加启动到 UEFI 固件设置的选项。 

###  为内核参数编辑器加上密码保护

你也可以安装 [systemd-boot-password](<https://aur.archlinux.org/packages/systemd-boot-password/>)AUR，它支持 `password` 基本配置选项。使用 `sbpctl generate` 可以为该选项生成值。 

使用如下命令安装 _systemd-boot-password_ ： 
    
    # sbpctl install _esp_
    
启用编辑器后，系统会提示你输入密码，然后才能编辑内核参数。 

##  小提示

###  启动选单中的按键操作

在启动选单中，你可以使用 `t` 和 `T` 调整超时时间，使用 `e` 编辑当前启动项的内核参数。按下 `h` 可以看到一个简略的快捷键列表，完整的启动选单内可用快捷键列表可参考 [systemd-boot(7) § KEY BINDINGS](<https://man.archlinux.org/man/systemd-boot.7#KEY_BINDINGS>) 。 

###  选择下一次启动选项

启动管理器与 systemctl 命令集成，允许你选择重启后的启动选项。举个例子，假设你构建了一个自定义内核，并创建了一个启动项文件 `_esp_ /loader/entries/arch-custom.conf` 来启动它，只需执行： 
    
    $ systemctl reboot --boot-loader-entry=arch-custom.conf
    
然后系统就会重启到对应的启动项，同时系统后续启动将保留现有设定不变。所有可用启动项清单可通过 `--boot-loader-entry=help` 选项查看。 

可以通过以下命令直接启动到主板固件： 
    
    $ systemctl reboot --firmware-setup
    
###  统一内核映像

位于 `_esp_ /EFI/Linux/` 的[统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像")会自动地被 systemd-boot 识别，无需在 `_esp_ /loader/entries` 中添加条目。需要注意的是，拥有`.efi` 扩展名的统一内核镜像才会被 systemd-boot 识别。 

**提示：** 如果在 `_esp_ /loader/loader.conf` 中未设置 `default`，则会优先启动位于 `_esp_ /loader/entries/` 的文件。请移除这些条目，或使用完整档名来设置预设项目，例如 `default arch-linux.efi`

### Grml on ESP

**注意：** 以下指令并非仅限于 Grml，稍作调整后，也能用来安装其他系统，例如：[SystemRescueCD](<https://www.system-rescue-cd.org/>)

**提示：** 有可用 AUR ：[grml-systemd-boot](<https://aur.archlinux.org/packages/grml-systemd-boot/>)AUR。

[Grml](<https://grml.org/>) 是精简的 Live 系统，包含一系列用于系统管理和救援的软件。 

如需将 Grml 安装到 ESP，只需将 iso 镜像中的内核文件 `vmlinuz`、initramfs 镜像 `initrd.img` 和压缩镜像 `grml64-small.squashfs` 复制到 ESP. 

首先，下载 [grml64-small.iso](<https://grml.org/download/>) 并挂载（下文中称挂载点为 mnt）; 内核和 initramfs 位于 `_mnt_ /boot/grml64small/`，压缩镜像位于 `_mnt_ /live/grml64-small/`。 

然后，在你的 ESP（EFI 系统分区）中新建一个 Grml 目录。 
    
    # mkdir -p _esp_ /grml
    
将上文提到的文件复制到目录中： 
    
    # cp _mnt_ /boot/grml64small/vmlinuz _esp_ /grml
    # cp _mnt_ /boot/grml64small/initrd.img _esp_ /grml
    # cp _mnt_ /live/grml64-small/grml64-small.squashfs _esp_ /grml
    
最后在 `_esp_ /loader/entries` 中创建一个 `grml.conf` 文件，以在 systemd-boot 中创建一个启动项： 
    
    _esp_ /loader/entries/grml.conf
    
    title   Grml Live Linux
    linux   /grml/vmlinuz
    initrd  /grml/initrd.img
    options apm=power-off boot=live live-media-path=/grml/ nomce net.ifnames=0

要查看所有可用引导选项，请参考 [cheatcode for Grml](<https://github.com/grml/grml-live/blob/master/config/media-files/GRMLBASE/GRML/GRML_NAME/grml-cheatcodes.txt>)。 

### Archiso on ESP

**提示：** 有可用的 AUR：[archiso-systemd-boot](<https://aur.archlinux.org/packages/archiso-systemd-boot/>)AUR。

与 Grml 相同，也可以使用 Arch Linux 的 ISO 创建启动环境。为此，需要将 ISO 文件中的以下内容复制到 EFI 系统分区（ESP）： 

内核文件：`vmlinuz-linux`

初始内存盘：`initramfs-linux.img`

压缩的根文件系统映像：`airootfs.sfs`

这些文件是系统启动所需的基本组件。后续步骤将说明如何挂载 ISO 并执行文件复制操作。 

第一步，下载 [archlinux-YYYY.MM.DD-x86_64.iso](<https://archlinux.org/download/>)

然后，在 EFI 系统分区（ESP）中创建一个名为 archiso 的目录，用于存放这些文件： 
    
    # mkdir -p _esp_ /EFI/archiso
    
将 `arch` 目录中所有内容解压或复制到此文件夹中： 
    
    # bsdtar -v -x --no-same-permissions --strip-components 1 -f archlinux-_YYYY_._MM_._DD_ -x86_64.iso -C _esp_ /EFI/archiso arch
    
最后在 `_esp_ /loader/entries` 中创建一个 `arch-rescue.conf` 文件，以便在 systemd-boot 中添加一个启动项： 
    
    _esp_ /loader/entries/arch-rescue.conf
    
    title   Arch Linux (rescue system)
    linux   /EFI/archiso/boot/x86_64/vmlinuz-linux
    initrd  /EFI/archiso/boot/x86_64/initramfs-linux.img
    options archisobasedir=/EFI/archiso archisosearchfilename=/EFI/archiso/boot/x86_64/vmlinuz-linux

如需了解可用的开机选项，参见 [README.bootparams for mkinitcpio-archiso](<https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio-archiso/-/blob/master/docs/README.bootparams>)。 

####  在启用了安全启动的系统制作 Arch Linux 恢复环境

官方的 Arch ISO 目前不支持[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "UEFI/安全启动")。所以，进入 ISO 进行恢复或者维护前必须禁用安全启动。这也会破坏系统的安全性，并不是个好办法。 

一个可能的选择是使用 [mkosi](<https://wiki.archlinux.org/title/Mkosi> "en:Mkosi") 创建签名的[统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像")，前提是系统上的安全启动已经正确配置并可以运行。这可以让你引导进一个签名的 Arch 恢复环境而无需禁用安全启动或随身携带一个 ISO USB 驱动器。 

<https://swsnr.de/archlinux-rescue-image-with-mkosi/> 描述了配置兼容安全启动的 Arch 恢复镜像的方法。开箱即用的 mkosi 配置可在 <https://codeberg.org/swsnr/rescue-image> 获取，可以自行添加软件包。 

###  在 BIOS 系统上使用 systemd-boot

如果需要一个符合 [The Boot Loader Specification](<https://uapi-group.org/specifications/specs/boot_loader_specification/>) 的 BIOS 系统启动加载器，也可以使用 systemd-boot. [Clover](<../zh-cn/Clover.html> "Clover") 支持在 BIOS 系统中启动并模拟一个 UEFI 环境（以便使用 systemd-boot）. 

##  排除问题

###  systemd-boot 无法显示我的启动项

该问题可能是由配置文件问题（如内核路径错误）导致的。可以执行以下命令进行检查： 
    
    # bootctl
    
###  在传统启动（BIOS 模式）下安装

**注意：** 不建议进行该操作!

如果你以 BIOS 模式启动电脑，你还是可以正常安装 _systemd-boot_ ，但需要在安装后手动向你的固件提供如何启动 _systemd-boot_ EFI 文件的相关信息,为此你需要下列工具之一： 

  * 一个 UEFI Shell
  * 你的 UEFI 固件设置中提供了更改启动选项的选项.
  * 如果 UEFI 没有其它启动项，某些固件会直接使用 `_esp_ /EFI/BOOT/BOOTX64.EFI` 。

满足条件后，进入你的 UEFI Shell 或是 UEFI 固件设置，修改你的默认 EFI 启动加载器为 `_esp_ /EFI/systemd/systemd-bootx64.efi` 。 

**注意：** 在某些 Dell Latitude 计算机上，UEFI 固件设置界面提供了设置 UEFI 启动所需的工具,而 EFI Shell 无法修改那些设置.

###  通过 efibootmgr 手动添加启动选项

如果运行`bootctl install` 命令失败,你可以通过 [efibootmgr](<https://archlinux.org/packages/?name=efibootmgr>)包手动增加选项: 
    
    # efibootmgr --create --disk /dev/sd _X_ --part _Y_ --loader '\EFI\systemd\systemd-bootx64.efi' --label "Linux Boot Manager" --unicode
    
用 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")的设备名称替换 `/dev/sd _XY_` 。 

###  在 Windows 上通过 bcdedit 添加启动选项

如需从 Windows 添加 UEFI 启动入口，你可以用管理员权限执行这些指令： 
    
    > bcdedit /copy {bootmgr} /d "Linux Boot Manager"
    > bcdedit /set {_guid_} path \EFI\systemd\systemd-bootx64.efi
    
用第一条指令返回的 id 替换 `_guid_`. 你也可以使用以下指令将它设置为默认入口： 
    
    > bcdedit /default {_guid_}
    
###  在 Windows 升级后看不到启动菜单

参阅 [UEFI#Windows 改变了启动次序](<../zh-cn/UEFI.html#Windows_%E6%94%B9%E5%8F%98%E4%BA%86%E5%90%AF%E5%8A%A8%E6%AC%A1%E5%BA%8F> "UEFI")。 

###  添加 Windows BitLocker TPM 解锁支持

在 _loader.conf_ 中添加以下内容以阻止 BitLocker 请求恢复密钥： 
    
    _esp_ /loader/loader.conf
    
    reboot-for-bitlocker yes
    
这一步会设定 _BootNext_ UEFI 变量，从而无需使 BitLocker 请求恢复密钥就能加载 _Windows Boot Manager_ 。该操作只需进行一次，且 _systemd-boot_ 仍是默认引导加载程序。如果已自动检测到 Windows，则无需将其指定为条目。 

注意，这是实验性功能，使用前请查阅 [loader.conf(5)](<https://man.archlinux.org/man/loader.conf.5>)。 

##  参阅

  * <https://systemd.io/BOOT/>
  * <https://bbs.archlinux.org/viewtopic.php?id=254374>
  * <https://uapi-group.org/specifications/specs/boot_loader_specification/>
