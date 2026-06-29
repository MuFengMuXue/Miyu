**翻译状态：**

  * 本文（或部分内容）译自 [rEFInd](<https://wiki.archlinux.org/title/rEFInd> "arch:rEFInd")，最近一次同步于 2021-03-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/rEFInd?diff=0&oldid=653879>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/rEFInd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Arch boot process](<../zh-cn/Arch_boot_process.html> "Arch boot process")
  * [Boot loaders](<../zh-cn/Boot_loaders.html> "Boot loaders")
  * [EFISTUB](</wzh/index.php?title=EFISTUB&action=edit&redlink=1> "EFISTUB（页面不存在）")
  * [booster](<../zh-cn/Booster.html> "Booster")
  * [Unified Extensible Firmware Interface](<../zh-cn/Unified_Extensible_Firmware_Interface.html> "Unified Extensible Firmware Interface")

[rEFInd](<https://www.rodsbooks.com/refind/>) 是一个 [UEFI](<../zh-cn/Unified_Extensible_Firmware_Interface.html> "Unified Extensible Firmware Interface") 能够启动 [EFISTUB](</wzh/index.php?title=EFISTUB&action=edit&redlink=1> "EFISTUB（页面不存在）") 内核的启动管理器。它是 [rEFIt](<https://refit.sourceforge.net/>) （不再维护）的一个分支并且针对非 Mac 硬件修复了若干问题。它被设计为平台无关，可启动多个操作系统。 

**注意：** 整篇文章中 `_esp_` 代表 [EFI system partition](<../zh-cn/EFI_system_partition.html> "EFI system partition") 的挂载点。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [refind](<https://archlinux.org/packages/?name=refind>)包 包。 

##  安装 rEFInd 启动管理器

rEFInd 附带了实现了对 ReiserFS, Ext2, Ext4, Btrfs, ISO-9660 and HFS+ **只读** 支持的 [UEFI drivers](<../zh-cn/Unified_Extensible_Firmware_Interface.html#UEFI_drivers> "Unified Extensible Firmware Interface")。而且 rEFInd 能够访问任何 UEFI 本身能够存取的文件系统，包括 FAT (由 UEFI 规范强制要求), 在 Mac 上的 HFS+ 和一些系统上的 ISO-9660。 

额外的驱动可以参考 [The rEFInd Boot Manager: Using EFI Drivers: Finding Additional EFI Drivers](<https://www.rodsbooks.com/refind/drivers.html#finding>)。 

为了使用 rEFInd, 务必将它安装到 EFI 分区， 使用 [rEFInd 安装脚本](<#%E4%BB%A5_rEFInd_%E5%AE%89%E8%A3%85%E8%84%9A%E6%9C%AC%E5%AE%89%E8%A3%85>)或者[手动复制文件并设置启动入口](<#%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85>). 

**警告：** 你的内核和 initramfs 必须在一个 rEFInd 能够读取的文件系统上。

###  以 rEFInd 安装脚本安装

rEFInd 包含有一个 _refind-install_ 脚本来简化将你的 rEFInd 设置为默认 EFI 启动项的过程。这个脚本有几个选项用于处理不同的设置和 UEFI 实现。想要了解不同选项的含义，请参见 [refind-install(8)](<https://man.archlinux.org/man/refind-install.8>) 或者读安装脚本里面的注释。 

对于许多系统来说，运行下面的命令就足够了： 
    
    # refind-install
    
此操作会尝试找到并挂载您的 [ESP](<../zh-cn/EFI_system_partition.html> "EFI system partition")，将 rEFInd 的文件复制到 `_esp_ /EFI/refind/`，并使用 [efibootmgr](<../zh-cn/Unified_Extensible_Firmware_Interface.html#efibootmgr> "Unified Extensible Firmware Interface") 将 rEFInd 设置为默认的 UEFI 启动项。 

或者您可以将 rEFInd 安装到默认/回退（fallback）启动路径 `_esp_ /EFI/BOOT/bootx64.efi`。这对于可启动的 USB 驱动器或者在那些 _efibootmgr_ 做的 NVRAM 更改有问题的系统上会有帮助： 
    
    # refind-install --usedefault _/dev/sdXY_
    
其中 `_/dev/sdXY_` 是你的 EFI 分区 (块设备, 不是挂载点). 

**提示：** 默认情况下 `refind-install` 只会为内核所在的文件系统安装驱动。 其他的文件系统需要手动安装，通过将 `/usr/share/refind/drivers_x64/` 复制到 `_esp_ /EFI/refind/drivers_x64/`, 或者你可以以 `--alldrivers` 选项安装。 这对于可启动的 USB 驱动器有帮助。

将 rEFInd 的文件安装到 ESP 之后， 验证 rEFInd 已经在你的内核所在文件夹创建了包含[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")的 `refind_linux.conf` 文件。如果你用了 `--usedefault` 选项，该文件不会被创建，请以 root 身份运行 `mkrlconf` 来创建它。 

**警告：** 当 `refind-install` 运行在chroot环境下 (例如：安装Arch Linux时的live环境) `/boot/refind_linux.conf` 内将会添加live系统的内核选项，而不是安装它的系统。 

编辑 `/boot/refind_linux.conf` 并确保其中的 [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") 对于你的系统是正确的，否则下次启动可能会出现内核错误。 

查看示例：[rEFInd#refind_linux.conf](<#refind_linux.conf>)。

默认情况下，rEFInd 会扫描你的所有的驱动器（它有驱动的那些）并为它找到的每一个 EFI bootloader 添加一个启动入口，其中就包含你的内核（因为 Arch 默认启用了 [EFISTUB](</wzh/index.php?title=EFISTUB&action=edit&redlink=1> "EFISTUB（页面不存在）") ）。因此你在这时候就可能有一个可以启动的系统。 

#### Secure Boot

要在 rEFInd 中使用 [Secure Boot](<../zh-cn/Unified_Extensible_Firmware_Interface/Secure_Boot.html> "Unified Extensible Firmware Interface/Secure Boot")，请参考 [Managing Secure Boot](<https://www.rodsbooks.com/refind/secureboot.html>)。 

#####  使用 PreLoader

要获取经过签名的 `PreLoader.efi` 和 `HashTool.efi` 二进制文件，请参考 [Secure Boot#Set up PreLoader](<../zh-cn/Secure_Boot.html#Set_up_PreLoader> "Secure Boot")。 

以 `--preloader _/path/to/preloader_` 选项执行 `refind-install`。 
    
    # refind-install --preloader /usr/share/preloader-signed/PreLoader.efi
    
当你下次以 Secure Boot 开启状态启动时，HashTool 会启动并让你注册 rEFInd (`loader.efi`) 、rEFInd 的驱动器 (如 `ext4_x64.efi`)和内核 (如 `vmlinuz-linux`) 的 hash。 

更多信息参见 [refind-install(8)](<https://man.archlinux.org/man/refind-install.8>)。 

**提示：** 经过签名的 HashTool 只能够访问启动它的分区。 这意味着如果你的内核不在 EPS 上, 你就不能从 HashTool 注册它的 hash. 你可以使用 [#KeyTool](<#KeyTool>) 来替代这种情况, 因为它可以将一个 hash 注册到 MokList 并且不被限制在一个分区。在使用之前，请记住要先注册 KeyTool 的 hash。

#####  使用 shim

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [shim-signed](<https://aur.archlinux.org/packages/shim-signed/>)AUR。阅读 [Secure Boot#shim](<../zh-cn/Secure_Boot.html#shim> "Secure Boot")，但是跳过所有的文件复制。 

######  使用 hash

要只使用带有 hash 的 shim，请以 `--shim _/path/to/shim_` 参数执行 `refind-install`： 
    
    # refind-install --shim /usr/share/shim-signed/shimx64.efi
    
当你下次以 Secure Boot 开启状态启动时, MokManager 会启动并让你注册 rEFInd (`loader.efi`) 、rEFInd 的驱动器 (如 `ext4_x64.efi`)和内核 (如 `vmlinuz-linux`) 的 hash。 

######  使用机器所有者密钥（Machine Owner Key）

要使用计算机所有者密钥（MOK）对 rEFInd 进行签名，请安装 [sbsigntools](<https://archlinux.org/packages/?name=sbsigntools>)包。 

**提示：** 如果您已经[创建了一个计算机所有者密钥](<../zh-cn/Secure_Boot.html#shim_with_key> "Secure Boot")，则将文件命名为 `refind_local.key`（PEM 格式私钥）、`refind_local.crt` （PEM 格式证书）和 `refind_local.cer` （DER 格式证书），并放置在`/etc/refind.d/keys`目录中。

以 `--shim _/path/to/shim_` 和 `--localkeys` 选项执行 `refind-install`： 
    
    # refind-install --shim /usr/share/shim-signed/shimx64.efi --localkeys
    
refind-install 会为你创建密钥并为它和它的驱动器签名。你需要用同一个密钥为内核签名，如： 
    
    # sbsign --key /etc/refind.d/keys/refind_local.key --cert /etc/refind.d/keys/refind_local.crt --output /boot/vmlinuz-linux /boot/vmlinuz-linux
    
**提示：** 内核签名可以由 [pacman 钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")自动化, 参见 [Secure Boot#Signing the kernel with a pacman hook](<../zh-cn/Secure_Boot.html#Signing_the_kernel_with_a_pacman_hook> "Secure Boot")。

进入 MokManager 之后，将 `refind_local.cer` 添加到 MoKList。在 rEFInd 的安装目录下，如 `_esp_ /EFI/refind/keys/refind_local.cer`，一个叫做 `keys` 的文件夹里面可以找到 `refind_local.cer`。 

更多信息参见 [refind-install(8)](<https://man.archlinux.org/man/refind-install.8>)。 

#####  使用你自己的密钥

跟随 [Secure Boot#Using your own keys](<../zh-cn/Secure_Boot.html#Using_your_own_keys> "Secure Boot") 来创建密钥。 

创建目录 `/etc/refind.d/keys` 并将 Signature Database (**db**) 密钥和证书放在其中。 将文件命名为： `refind_local.key` (PEM 格式私钥), `refind_local.crt` (PEM 格式证书) 和 `refind_local.cer` (DER 格式证书)。 

在运行安装脚本时添加 `--localkeys` 选项，如： 
    
    # refind-install --localkeys
    
rEFInd EFI 二进制文件将会被用提供的密钥和证书签名。 

###  手动安装

**提示：** rEFInd 能够以多种方式启动 Linux。参见 [The rEFInd Boot Manager: Methods of Booting Linux](<https://www.rodsbooks.com/refind/linux.html>)。本节将阐述使用 [EFISTUB](</wzh/index.php?title=EFISTUB&action=edit&redlink=1> "EFISTUB（页面不存在）") 的过程。

**注意：** 对于 32 位 EFI，请将 **x64** 替换为 **ia32** 。

如果 `refind-install` 脚本没有正常工作，您可以手动设置 rEFInd。 

首先，将可执行文件复制到 ESP: 
    
    # mkdir -p _esp_ /EFI/refind
    # cp /usr/share/refind/refind_x64.efi _esp_ /EFI/refind/
    
如果想要将 rEFInd 安装到默认/回退（fallback) 启动路径，请在下面将 `_esp_ /EFI/refind/` 替换为 `_esp_ /EFI/BOOT/`，并将 rEFInd EFI 可执行文件复制到 `_esp_ /EFI/BOOT/bootx64.efi`: 
    
    # mkdir -p _esp_ /EFI/BOOT
    # cp /usr/share/refind/refind_x64.efi _esp_ /EFI/BOOT/bootx64.efi
    
然后使用 [efibootmgr](</wzh/index.php?title=Efibootmgr&action=edit&redlink=1> "Efibootmgr（页面不存在）") 来在 UEFI NVRAM 中创建一个启动入口，其中 `_/dev/sdX_` 和 `_Y_` 是你的 EFI 分区的设备和分区号。如果你要将 rEFI 安装到默认/回退（fallback) 启动路径 `_esp_ /EFI/BOOT/bootx64.efi`，你可以跳过这一步。 
    
    # efibootmgr --create --disk _/dev/sdX_ --part _Y_ --loader /EFI/refind/refind_x64.efi --label "rEFInd Boot Manager" --verbose
    
此时，你应该能重启到 rEFInd，但是它无法引导你的内核。如果你的内核不在你的 ESP 上，那么 rEFInd 可以挂载你的分区来查找它，只要它具有正确的驱动程序即可。 

rEFInd 会从其安装目录中的子目录 `drivers` 和 `drivers__arch_`（例如 `drivers_x64`）自动加载所有驱动程序。 
    
    # mkdir _esp_ /EFI/refind/drivers_x64
    # cp /usr/share/refind/drivers_x64/**drivername** _x64.efi _esp_ /EFI/refind/drivers_x64/
    
现在，rEFInd应该为你的内核提供了一个启动项，但是不会传递正确的内核参数。设置[#传递内核参数](<#%E4%BC%A0%E9%80%92%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0>)。现在，你应该可以使用 rEFInd 引导内核了。如果仍然无法启动或想要调整 rEFInd 的设置，则可以使用配置文件来更改许多选项： 
    
    # cp /usr/share/refind/refind.conf-sample _esp_ /EFI/refind/refind.conf
    
该示例配置文件具有很好的注释并且不言自明。 

除非你在配置文件中设置了`textonly`，否则你应该复制 rEFInd 的图标以摆脱难看的占位符： 
    
    # cp -r /usr/share/refind/icons _esp_ /EFI/refind/
    
你可以尝试通过复制不同的字体并更改 `refind.conf` 中的 `font` 设置来进行尝试： 
    
    # cp -r /usr/share/refind/fonts _esp_ /EFI/refind/
    
**提示：** 在 rEFInd 中按 `F10`将会保存屏幕截图到 ESP 分区的根目录。

###  更新 rEFInd

Pacman 只更新在 `/usr/share/refind` 中的文件，不会将新文件复制到 ESP。 如果最初 `refind-install` 成功安装了 rEFInd，则可以再次运行以更新文件。 新的配置文件会被复制为 `refind.conf-sample` ，你可以使用一个 [diff](<../zh-cn/Core_utilities.html#%E5%9F%BA%E7%A1%80> "Core utilities") 工具选择、改变合并到你的配置文件。如果你的 rEFInd 需要[#手动安装](<#%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85>)，你需要自己找出需要复制哪些文件。 

####  Pacman 钩子

你可以使用一个 [pacman 钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")来自动化更新过程: 
    
    /etc/pacman.d/hooks/refind.hook
    
    [Trigger]
    Operation=Upgrade
    Type=Package
    Target=refind
    
    [Action]
    Description = Updating rEFInd on ESP
    When=PostTransaction
    Exec=/usr/bin/refind-install

你可能需要为你的设置将 `Exec=`更改为正确的更新命令。如果您进行了[#手动安装](<#%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85>)，则可以创建自己的更新脚本以使用钩子进行调用。 

**提示：** 如果你使用 [#Secure Boot](<#Secure_Boot>) 设置 rEFInd，则可能需要在 `refind-install` 命令中额外添加选项 `--yes`。如果在禁用 Secure Boot 后执行该命令，它将防止该命令失败。更多信息参见 [refind-install(8)](<https://man.archlinux.org/man/refind-install.8>)。

**注意：** 如果 ESP 未挂载到 `/boot`，而你依靠自动挂载来挂载它，请确保按照 [EFI system partition#Alternative mount points](<../zh-cn/EFI_system_partition.html#Alternative_mount_points> "EFI system partition") 来预加载 `vfat` 模块。否则，如果 [refind](<https://archlinux.org/packages/?name=refind>)包与内核一起升级，ESP 将变得不可访问。

##  配置

rEFInd 的配置文件 `refind.conf` 存放在 rEFInd EFI 应用的同一目录下（通常为 `_esp_ /EFI/refind` 或 `_esp_ /EFI/BOOT`）。默认的配置文件包含了解释了所有选项的扩展注释，更详细的解释参考 [Configuring the Boot Manager](<https://www.rodsbooks.com/refind/configfile.html>)。 

###  传递内核参数

有两种方法可以设置 rEFInd 传递给内核的[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。 

####  对于 rEFInd 自动检测到的内核

对于自动检测到的内核，你可以在 `/boot/refind_linux.conf` 中显式指定内核参数，也可以依靠 rEFInd 识别 root 分区和内核参数的能力。更多信息参见[Methods of Booting Linux: For Those With Foresight or Luck: The Easiest Method](<https://www.rodsbooks.com/refind/linux.html#easiest>)。 

**提示：**

  * 当 `/etc/os-release` 与内核位于同一分区时，rEFInd 会自动为启动项选择 Arch Linux图标 (`os_arch.png`)。如果你的 `/boot` 是一个单独的分区，参考 [Configuring the Boot Manager: Setting OS Icons](<https://www.rodsbooks.com/refind/configfile.html#icons>)。
  * rEFInd [不支持检测统一内核映像的分布](<https://sourceforge.net/p/refind/discussion/general/thread/c3865a4e3a/>)。要为[统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核镜像")提供图标，请将 `/usr/share/refind/icons/os_arch.png` 复制到 `_esp_ /EFI/Linux/` 并确保文件名匹配。例如，如果你有 `_esp_ /EFI/Linux/Arch-linux.efi`，则将对应的图标命名为 `_esp_ /EFI/Linux/Arch-linux.png`。

为了使 rEFInd 支持 Arch Linux [内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernel")的命名方案并因此使其与各自的 initramfs 镜像相匹配，必须取消注释并编辑 `refind.conf` 中的 `extra_kernel_version_strings`选项。例如： 
    
    _esp_ /EFI/refind/refind.conf
    
    ...
    extra_kernel_version_strings linux-hardened,linux-zen,linux-lts,linux
    ...
    
**注意：**

  * rEFInd 仅支持为每个内核检测一个 initramfs 镜像，这意味着它将不检测 fallback initramfs 或[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "Microcode")镜像，必须手动指定它们。
  * 如果没有上述 `extra_kernel_version_strings` 行，`refind_linux.conf` 中的 `%v` 变量将不适用于 Arch Linux [内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernel")。

##### refind_linux.conf

如果 rEFInd 自动检测到你的内核，你可以将包含内核参数的 `refind_linux.conf` 文件放置在与内核相同的目录中。你可以使用 `/usr/share/refind/refind_linux.conf-sample` 作为起点。 `refind_linux.conf` 未注释的第一行将是内核的默认参数。随后的行将在子菜单中创建可使用 `+`, `F2`, 或 `Insert` 访问的条目。 

或者，尝试以 root 身份运行 `mkrlconf`。它将会尝试在 `/boot` 中找到你的内核，并自动生成 `refind_linux.conf`。该脚本只会设置最基本的内核参数，因此请确保检查其创建的文件的正确性。 

如果未指定 `initrd=` 参数，rEFInd 将通过在与内核相同的目录中搜索常用RAM磁盘文件名来自动添加它。如果需要多个 `initrd=` 参数，则必须在 `refind_linux.conf` 中手动指定它们。例如，一个在 initramfs 之前传递的[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "Microcode")： 
    
    /boot/refind_linux.conf
    
    "Boot using default options"     "root=PARTUUID=_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_ rw add_efi_memmap initrd=boot\intel-ucode.img initrd=boot\amd-ucode.img initrd=boot\initramfs-%v.img"
    "Boot using fallback initramfs"  "root=PARTUUID=_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_ rw add_efi_memmap initrd=boot\intel-ucode.img initrd=boot\amd-ucode.img initrd=boot\initramfs-%v-fallback.img"
    "Boot to terminal"               "root=PARTUUID=_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_ rw add_efi_memmap initrd=boot\intel-ucode.img initrd=boot\amd-ucode.img initrd=boot\initramfs-%v.img systemd.unit=multi-user.target"

**警告：**

  * `initrd` 路径是相对于内核所在文件系统的根目录。这可能是 `initrd=\boot\initramfs-%v.img` 或者 `initrd = initramfs-％v.img`（如果 `/boot` 是一个单独的分区，例如 ESP）。
  * 在参数 `initrd` 中使用反斜杠 (`\`) 作为路径分隔符，否则内核可能无法找到 initramfs 镜像：`EFI stub: ERROR: Failed to open file: /boot/intel-ucode.img`。

**注意：** rEFInd用内核的版本替换 ` refind_linux.conf` 中的 `％v`}（通过从文件名中提取if）。为了使 rEFInd 支持Arch Linux内核，必须按照 [#对于 rEFInd 自动检测到的内核](<#%E5%AF%B9%E4%BA%8E_rEFInd_%E8%87%AA%E5%8A%A8%E6%A3%80%E6%B5%8B%E5%88%B0%E7%9A%84%E5%86%85%E6%A0%B8>)中的说明编辑 `esp/EFI/refind/refind.conf` 中的 `extra_kernel_version_strings`。 

#####  无需配置的情况

如果你仅将 rEFInd 安装到 ESP 上并毫不费力地启动它（例如通过 UEFI Shell 或 KeyTool，或直接从固件），您仍然可以通过自动检测从启动菜单，而无需进行任何配置。 

这之所以可行，是因为 rEFInd 具有回退机制，可以： 

  * 通过 [Discoverable Partitions Specification](<https://uapi-group.org/specifications/specs/discoverable_partitions_specification/>) 或者 `/etc/fstab` 分辨 root 分区（对于 `root=` 参数）。
  * 从 [GPT partition attributes](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_entries_.28LBA_2-33.29> "wikipedia:GUID Partition Table") 检测内核选项 (`ro` 或者 `rw`)。 （使用属性 `60` "read-only") 或者 `/etc/fstab`。

**注意：** rEFInd 不支持转义码 (如 `/etc/fstab` 中的 [路径名空格](<../zh-cn/Fstab.html#%E8%B7%AF%E5%BE%84%E5%90%8D%E6%9C%89%E7%A9%BA%E6%A0%BC> "Fstab"))。

####  手动启动项

如果未自动检测到内核，或者你只想对菜单项的选项进行更多控制，则可以使用 `refind.conf` 中的 stanzas 来手动创建引导项。确保 `scanfor` 包含 `manual`，否则这些条目将不会出现在 rEFInd 的菜单中。内核参数使用 `options` 关键字设置。 rEFInd 将使用 stanza 中的 `initrd` 关键字指定的文件附加 `initrd=` 参数。如果你需要其他 initrd（例如[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "Microcode")），则可以在 `options` 中指定它们（并且 `initrd` 关键字指定的会添加到末尾）。 

手动启动项在 [Creating Manual Boot Stanzas](<https://www.rodsbooks.com/refind/configfile.html#stanzas>) 中有详细解释。 
    
    _esp_ /EFI/refind/refind.conf
    
    ...
    
    menuentry "Arch Linux" {
    	icon     /EFI/refind/icons/os_arch.png
    	volume   "Arch Linux"
    	loader   /boot/vmlinuz-linux
    	initrd   /boot/initramfs-linux.img
    	options  "root=PARTUUID=_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_ rw add_efi_memmap initrd=boot\intel-ucode.img initrd=boot\amd-ucode.img"
    	submenuentry "Boot using fallback initramfs" {
    		initrd /boot/initramfs-linux-fallback.img
    	}
    	submenuentry "Boot to terminal" {
    		add_options "systemd.unit=multi-user.target"
    	}
    }

您可能需要更改 `volume`以匹配文件系统的标签、PARTLABEL 或内核镜像所在分区的 PARTUUID。PARTUUID 必须大写的。有关分配卷标的示例，请参见 [Persistent block device naming#通过标签](<../zh-cn/Persistent_block_device_naming.html#%E9%80%9A%E8%BF%87%E6%A0%87%E7%AD%BE> "Persistent block device naming")。如果未指定 `volume`，则默认为启动 rEFInd 的卷（通常是EFI系统分区）。 

**警告：**

  * `loader` 和 `initrd` 的路径是相对于 `volume` 的根目录的相对路径。如果 `/boot` 是一个单独的分区（例如 ESP ），那么加载程序和 initrd 路径分别是 `/vmlinuz-linux` 和 `/initramfs-linux.img`。
  * 在所有引用的 `initrd` 参数中使用反斜杠 (`\`) 作为路径分隔符，否则内核可能无法找到 initramfs 镜像：`EFI stub: ERROR: Failed to open file: /boot/initramfs-linux.img`。

##  在已有的 Windows UEFI 安装中使用 rEFInd

**注意：** 在页面 [Windows and Arch Dual Boot](<../zh-cn/Windows_and_Arch_Dual_Boot.html> "Windows and Arch Dual Boot") 中查看通常的注意事项。

rEFInd 兼容 UEFI Windows 安装时创建的 EFI 系统分区，因此没有必要创建或格式化另一个 FAT32 分区。只需挂载 Windows 的 ESP 并像往常一样安装 rEFInd。默认情况下，rEFInd 的自动检测功能应该识别任何现有的 Windows 引导程序。 

**注意：** 在某些情况下，Windows 的行为不同（低分辨率启动屏幕、OEM logo 被 Windows logo 替换、启动屏幕后出现黑屏、伪影）。如果您遇到这样的问题，请尝试在 `_esp_ /EFI/refind/refind.conf` 中设置 `use_graphics_for +,windows` 或者将 `graphics on` 添加到Windows 引导项。 

##  工具

rEFInd支持运行各种[第三方工具](<https://www.rodsbooks.com/refind/installing.html#addons>)。工具需要单独安装。在 `refind.conf` 中编辑 `showtools` 文件选择要显示的内容。 
    
    _esp_ /EFI/refind/refind.conf
    
    ...
    showtools [shell](<#UEFI_shell>), [memtest](<#Memtest86>), [mok_tool](<#%E5%AF%86%E9%92%A5%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7>), [gdisk](<#GPT_fdisk_\(gdisk\)>), [fwupdate](<#fwupdate>) ...
    ...
    
### UEFI shell

参见 [Unified Extensible Firmware Interface#UEFI Shell](<../zh-cn/Unified_Extensible_Firmware_Interface.html#UEFI_Shell> "Unified Extensible Firmware Interface")。 

复制 `shellx64.efi` 到 [EFI 分区](<../zh-cn/EFI_system_partition.html> "EFI system partition")的根目录。 

### Memtest86

安装 [memtest86-efi](<https://aur.archlinux.org/packages/memtest86-efi/>)AUR 并将它复制到 `_esp_ /EFI/tools/`。 
    
    # cp /usr/share/memtest86-efi/bootx64.efi _esp_ /EFI/tools/memtest86.efi
    
###  密钥管理工具

rEFInd 能够检测 Secure Boot 密钥管理工具，如果他们被放在 EPS 上的 rEFInd 的文件夹内，如 `_esp_ /` 或 `_esp_ /EFI/tools/`。 

#### HashTool

参照 [#使用 PreLoader](<#%E4%BD%BF%E7%94%A8_PreLoader>)， `HashTool.efi` 将被放在 rEFInd 的文件夹内。 

#### MokManager

参照 [#使用 shim](<#%E4%BD%BF%E7%94%A8_shim>)，MokManager 将被放在 rEFInd 的文件夹内。 

#### KeyTool

安装 [efitools](<https://archlinux.org/packages/?name=efitools>)包。 

将 KeyTool EFI 二进制文件放在 `_esp_ /` 或者 `_esp_ /EFI/tools/` 中，并命名为 `KeyTool.efi` 或 `KeyTool-signed.efi`。 

关于签名 `KeyTool.efi` 的指导，请参考 [Secure Boot#Using KeyTool](<../zh-cn/Secure_Boot.html#Using_KeyTool> "Secure Boot")。 

###  GPT fdisk (gdisk)

下载 [gdisk EFI 应用](<../zh-cn/GPT_fdisk.html#gdisk_EFI_application> "Gdisk")并将 `gdisk_x64.efi` 复制到 `_esp_ /EFI/tools/`。 

### fwupdate

安装并设置好 [fwupd](<../zh-cn/Fwupd.html> "Fwupd")。 

将 `fwupx64.efi` 和固件复制到 `_esp_ /EFI/tools/`： 
    
    # cp /usr/lib/fwupd/efi/fwupdx64.efi _esp_ /EFI/tools/
    
###  关机或重启

据报道，rEFInd 内置了关机和重启菜单项。由于这个工具列表是这个 wiki 中的同类工具中最广泛的，因此 UEFI shell 或其他 UEFI 引导管理器（如 [systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") ）的用户可能会对 [powerofforreboot.efi](<https://aur.archlinux.org/packages/powerofforreboot.efi/>)AUR 感兴趣。 

##  提示与小技巧

###  在 UEFI shell 中使用驱动

要在 UEFI shell 中使用 rEFInd 的驱动，请使用`load` 命令来加载它们，并使用 `map -r` 来刷新驱动器映射。 
    
    Shell> load FS0:\EFI\refind\drivers\ext4_x64.efi
    Shell> map -r
    
现在你可以从 UEFI shell 访问你的文件系统了。 

###  设置 efifb 分辨率

如果 `refind.conf` 中的分辨率被设置为一个不正确的值，在除了 Apple [Mac](<../zh-cn/Mac.html> "Mac") 的所有系统中， rEFInd 都会展示一个支持的分辨率列表。对于 Apple Mac, 它会静默使用默认分辨率。 

要确定 [efifb](<https://docs.kernel.org/fb/efifb.html>) 支持的帧缓冲区分辨率，请 [gnu-efi](<https://archlinux.org/packages/?name=gnu-efi>)包 将 `/usr/share/gnu-efi/apps/x86_64/modelist.efi` 复制到 [ESP](<../zh-cn/EFI_system_partition.html> "EFI system partition") 的根目录。进入 [UEFI shell](<../zh-cn/UEFI_shell.html> "UEFI shell") 并运行 `modelist.efi`。 
    
    Shell> FS0:\modelist.efi
    
    GOP reports MaxMode 3
     0: 640x480 BGRR pitch 640
    *1: 800x600 BGRR pitch 800
     2: 1024x768 BGRR pitch 1024
    
在 `refind.conf` 中设置一个。重启并用 `dmesg | grep efifb` 来检查设置是否已被应用。 

###  Btrfs 子卷支持

**提示：** 确保安装了 `btrfs_x64.efi` 驱动程序, 可以将 `/usr/share/refind/drivers_x64/btrfs_x64.efi` 复制到 `_esp_ /EFI/refind/drivers_x64/btrfs_x64.efi`来手动安装, 或者你也可以以 `refind-install /dev/sdx --alldrivers` 选项安装所有驱动程序。

**警告：**`btrfs_x64.efi` 不支持 `raid1c3/4`。

####  自动检测

要允许在 Btrfs 子卷上进行内核自动检测，请取消注释并编辑 `refind.conf` 中的 `also_scan_dirs`。 
    
    _esp_ /EFI/refind/refind.conf
    
    ...
    also_scan_dirs +,_subvolume_ /boot
    ...
    
然后在 `refind_linux.conf` 中将 `subvol=_subvolume_` 添加到 `rootflags`，之后将 `_subvolume_` 添加到 initrd 路径之前。 
    
    /boot/refind_linux.conf
    
    "Boot using standard options"  "root=PARTUUID=_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_ rw **rootflags=subvol=_subvolume_** initrd=_**subvolume**_ \boot\initramfs-%v.img"

####  手动启动项

如果将一个 [btrfs](<../zh-cn/Btrfs.html> "Btrfs") 子卷作为根目录引导，请将子卷的路径预先添加到 loader 和 initrd 路径之前，并用 `rootflags=subvol=_root_subvolume_` 修改 `options` 行。在下面的示例中，root 已作为名为“ROOT”的btrfs子卷挂载（例如 `mount -o subvol=ROOT /dev/sdxY /mnt`）： 
    
    _esp_ /EFI/refind/refind.conf
    
    ...
    menuentry "Arch Linux" {
            icon     /EFI/refind/icons/os_arch.png
            volume   "[bootdevice]"
            loader   **/ROOT** /boot/vmlinuz-linux
            initrd   **/ROOT** /boot/initramfs-linux.img
            options  "root=PARTUUID=_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_ rw **rootflags=subvol=ROOT** "
    ...
    }

如果失败将导致以下错误信息：`ERROR: Root device mounted successfully, but /sbin/init does not exist.`

### LoaderDevicePartUUID

从 0.13.1 版本开始，rEFInd 支持设置 UEFI 变量 [LoaderDevicePartUUID](<https://systemd.io/BOOT_LOADER_INTERFACE/>)。启用此选项允许 [systemd-gpt-auto-generator(8)](<https://man.archlinux.org/man/systemd-gpt-auto-generator.8>) 自动挂载 EFI 系统分区，而无需在 `/etc/fstab` 中指定它。请参阅 [systemd#GPT partition automounting](<../zh-cn/Systemd.html#GPT_partition_automounting> "Systemd")。 

对于 rEFInd， 要设置 `LoaderDevicePartUUID`, 请编辑 `refind.conf` 并取消注释 `write_systemd_vars true`: 
    
    _esp_ /EFI/refind/refind.conf
    
    ...
    write_systemd_vars true
    ...

您可以通过使用 `cat /sys/firmware/efi/efivars/LoaderDevicePartUUID-4a67b082-0a4c-41cf-b6c7-440b29bb8c4f` 检查它的值，或者通过查看 `bootclt` 输出中 “Boot loader sets ESP partition information” 的状态来验证它是否已设置。 

##  疑难解答

### Apple Macs

[AUR](<../zh-cn/Arch_User_Repository.html> "Arch User Repository") 上的 [mactel-boot](<https://aur.archlinux.org/packages/mactel-boot/>)AUR 是 "bless" 工具的实验性替代品。如果它不能正常工作， 在 OS X 中使用 "bless" 来将 rEFInd 设置为默认启动项。 
    
     # bless --setBoot --folder _esp_ /EFI/refind --file _esp_ /EFI/refind/refind_x64.efi
    
### VirtualBox

6.1 版本之前的 VirtualBox 将只引导默认的 `_esp_ /EFI/BOOT/bootx64.efi` 路径，因此 `refind-install` 至少需要与 `--usedefault` 选项一起使用。有关详细信息，请参阅 [VirtualBox/Install Arch Linux as a guest#Installation in EFI mode on VirtualBox < 6.1](<../zh-cn/VirtualBox/Install_Arch_Linux_as_a_guest.html#Installation_in_EFI_mode_on_VirtualBox_<_6.1> "VirtualBox/Install Arch Linux as a guest")。 

##  参见

  * [The rEFInd Boot Manager](<https://www.rodsbooks.com/refind/>) by Roderick W. Smith.
  * [Wikipedia:rEFInd](<https://en.wikipedia.org/wiki/rEFInd> "wikipedia:rEFInd")
  * `/usr/share/refind/docs/README.txt`
  * [rEFInd discussion forum on Sourceforge](<https://sourceforge.net/p/refind/discussion/>)
