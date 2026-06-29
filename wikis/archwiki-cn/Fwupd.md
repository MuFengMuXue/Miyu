**翻译状态：**

  * 本文（或部分内容）译自 [Fwupd](<https://wiki.archlinux.org/title/Fwupd> "arch:Fwupd")，最近一次同步于 2022-12-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/Fwupd?diff=0&oldid=761750>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Fwupd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Secure Boot](<../zh-cn/Secure_Boot.html> "Secure Boot")
  * [Unified Extensible Firmware Interface](<../zh-cn/Unified_Extensible_Firmware_Interface.html> "Unified Extensible Firmware Interface")

[fwupd](<https://fwupd.org/>) 是一个进行设备固件更新的简单守护程序，虽然是为桌面计算机设计，但是同样也支持手机和服务器。 

设备支持情况请查看[支持的设备列表](<https://fwupd.org/lvfs/devicelist>)和[厂商支持计划](<https://fwupd.org/vendorlist>)。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [fwupd](<https://archlinux.org/packages/?name=fwupd>)包。 

如果您将其用于 UEFI 固件升级，请参阅 [#UEFI 升级设置](<#UEFI_%E5%8D%87%E7%BA%A7%E8%AE%BE%E7%BD%AE>)。 

###  图形化前端

某些[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")前端解决方案具有内置的 fwupd 支持： 

  * **GNOME Software** — 将定期检查更新，并在 GNOME 的后台自动下载固件。下载固件后，将在 [Gnome](<../zh-cn/GNOME.html> "GNOME") Software 中显示一个弹出窗口以执行更新。

     <https://wiki.gnome.org/Apps/Software> || [gnome-software](<https://archlinux.org/packages/?name=gnome-software>)包

  * **KDE Discover** — 与 [Plasma](<../zh-cn/KDE.html> "Plasma") 一起使用的软件中心。随着 KDE Plasma 5.14 的发布，KDE Discover中已实现了新的 fwupd 后端以进行固件更新。这些固件更新与其他系统更新一起显示。

     <https://userbase.kde.org/Discover> || [discover](<https://archlinux.org/packages/?name=discover>)包

  * **GNOME Firmware** — 在 fwupd 支持的设备上升级，降级和重新安装固件的应用程序。它可以解锁锁定的 fwupd 设备，验证支持的设备上的固件并显示 fwupd 设备的所有发行。

     <https://gitlab.gnome.org/hughsie/gnome-firmware-updater> || [gnome-firmware](<https://archlinux.org/packages/?name=gnome-firmware>)包

##  使用

要显示 fwupd 检测到的所有设备： 
    
    $ fwupdmgr get-devices
    
**注意：** 列表中的部分设备可能不能使用该工具更新， _例如_ Intel 核芯显卡，可以替代地提供的供应商解决方案。

要从 [Linux Vendor firmware Service (LVFS)](<https://fwupd.org/>) 下载最新的元数据： 
    
    $ fwupdmgr refresh
    
要列出系统上任何设备可用的更新： 
    
    $ fwupdmgr get-updates
    
要安装更新： 
    
    $ fwupdmgr update
    
**注意：**

  * 可以实时应用的更新将立即完成。
  * 在启动时运行的更新将为下一次重新启动做好准备。
  * 可能需要使用 [root 用户](</wzh/index.php?title=Root_%E7%94%A8%E6%88%B7&action=edit&redlink=1> "Root 用户（页面不存在）")执行特定设备的更新。

##  UEFI 升级设置

**警告：** UEFI 固件更新可能会损坏您的[引导程序](<../zh-cn/Boot_loaders.html> "Boot loaders")，成功安装固件更新后，可能需要重新创建 NVRAM 条目（例如，使用 [efibootmgr](<../zh-cn/Unified_Extensible_Firmware_Interface.html#efibootmgr> "Unified Extensible Firmware Interface")）

  1. 使用 UEFI 模式启动系统，efibootmgr 无法在旧版启动模式下工作。
  2. 验证[您的 EFI 变量是否可以获取](<../zh-cn/Unified_Extensible_Firmware_Interface.html#UEFI_%E5%8F%98%E9%87%8F%E6%AD%A3%E5%B8%B8%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%9C%80%E6%B1%82> "Unified Extensible Firmware Interface")。
  3. 正确挂载 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区") (ESP)，` _esp_` 用于表示此部分中的挂载点。
  4. 请安装可选依赖 [udisks2](<https://archlinux.org/packages/?name=udisks2>)包，这个软件包提供了 UEFI 升级支持。

###  准备 ESP 目录

fwupd 会将所有必需的文件复制到 `_esp_` 上，但是要使其正常工作，"esp" 上必须存在基本的文件夹布局。 

**注意：** 由于您所使用的引导加载程序或其他操作系统的存在，此目录可能已经存在。

这会在 `_esp_` 目录创建 `EFI` 目录 。 
    
    mkdir _esp_ /EFI/
    
**警告：** 'EFI' 目录**必须** 全部大写。如果使用小写字母，fwupd 可能会将 _esp_ 检测为 _esp_ /efi/，并开始寻找 _esp_ /efi/EFI/

创建后，必须[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `fwupd.service` 服务。 

您现在可以 `$ fwupdmgr refresh` 和 `$ fwupdmgr update`。它将要求重新启动，现在应该自动重新启动到固件更新程序。 

**注意：** 在某些设备上，例如 [Lenovo ThinkPad P50](</wzh/index.php?title=Lenovo_ThinkPad_P50&action=edit&redlink=1> "Lenovo ThinkPad P50（页面不存在）")，固件更新时将显示 **无任何信息的黑屏** ——别紧张, **不要** 中断设备或强制重启，过几分钟后，系统会自动重启到操作系统。

###  安全启动

在[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")开启的系统下，fwupd 使用 [shim](<../zh-cn/Secure_Boot.html#shim> "Secure Boot") 来引导 fwupd EFI 文件。使用前请确保正确安装 shim。 

####  用自己的密钥

或者，您必须手动签名用于执行升级的 UEFI 可执行文件，该文件位于 `/usr/lib/fwupd/efi/fwupdx64.efi`。 已签名的 UEFI 可执行文件应放在 `/usr/lib/fwupd/efi/fwupdx64.efi.signed`. 使用 [sbsigntools](<https://archlinux.org/packages/?name=sbsigntools>)包，可以通过运行以下命令来实现： 
    
    # sbsign --key _keyfile_ --cert _certfile_ /usr/lib/fwupd/efi/fwupdx64.efi
    
为了使安装或者升级时自动签名，使用 [Pacman 挂钩](</wzh/index.php?title=Pacman_%E6%8C%82%E9%92%A9&action=edit&redlink=1> "Pacman 挂钩（页面不存在）")： 
    
    /etc/pacman.d/hooks/sign-fwupd-secureboot.hook
    
    [Trigger]
    Operation = Install
    Operation = Upgrade
    Type = Path
    Target = usr/lib/fwupd/efi/fwupdx64.efi
    
    [Action]
    When = PostTransaction
    Exec = /usr/bin/sbsign --key _keyfile_ --cert _certfile_ /usr/lib/fwupd/efi/fwupdx64.efi
    Depends = sbsigntools

确保用密钥的相应路径替换 `<keyfile>` 和 `<certfile>`。 

除了 Pacman 挂钩，您也可以创建从 `/usr/lib/fwupd/efi/fwupdx64.efi` 到 `/usr/lib/fwupd/efi/fwupdx64.efi.signed` 的符号链接，并将文件添加到 `/etc/sbupdate.conf` 中的 `EXTRA_SIGN` 列表中。 

最后，您必须将 `/etc/fwupd/uefi_capsule.conf` 中包含 `DisableShimForSecureBoot` 的行更改为 `DisableShimForSecureBoot=true` 并重新启动 `fwupd.service`。 

**注意：** 如果在 fwupd 1.4 之前进行了此设置，请注意配置选项的名称已更改。

查阅[此 GitHub issue](<https://github.com/fwupd/fwupd/issues/669>)，以获取更多讨论此问题的信息。 

##  故障排除

###  一直卡在重启

`fwupdmgr update` reports no error, but the reboot it prompts stuck and holding the power button has no response. Try switching off the power, or press the reset button (on a laptop, it might be a hole on the back) to force-reboot. 

###  没有错误，但重启后没有升级

**状况：**`fwupdmgr update` 未报告任何错误并提示重新启动（例如，在 BIOS 更新中）。 但是，系统将正常重启，并且不会进行固件更新。 

**可能的原因：** 在 BIOS 设置中，必须允许更改引导顺序。 

**Possible other solution if there are multiple updates pending:** Try updating packages one at a time. Use the following to select packages: 
    
    $ fwupdmgr update _update_ID_
    
(Where `_update_ID_` is something like `f95c9218acd12697af946874bfe4239587209232`.) 

### read-only filesystem error

At least `fwupdmgr` 1.5.2 deduces the wrong mount point if bind is used to mount `_esp_` to `/boot` [[1]](<https://wiki.archlinux.org/index.php?title=EFI_system_partition#Using_bind_mount>). Consequently it fails to write the UEFI update file to `/boot/EFI/arch/fw` (`fwupdmgr` while it should be written to `_esp_ /EFI/arch/fw`.) This results in a (misleading) "file system is read-only" error message. In case the update was performed by `Discover` (or any other fwupd-capable Update GUI), no error or misleading errors may be shown. 

As a workaround, run `umount /boot` first if it was bind-mounted to `_esp_ /EFI/arch` before, then run `fwupdmgr update` to write the UEFI update file to `_esp_ /EFI/arch/fw`, `mount /boot` and reboot the system to perform the UEFI update. 

### UEFI ESP partition not detected or configured

如果按上面 UEFI 更新的要求执行了操作，还是无法识别 ESP 分区，可以手动指定挂载点： 
    
    /etc/fwupd/uefi_capsule.conf
    
    [uefi_capsule]
    OverrideESPMountPoint=/efi   # Change according to your setup

Also see [the relevant article](<https://github.com/fwupd/fwupd/wiki/PluginFlag:esp-not-found>) in the _fwupd_ wiki. 

### MSR plugin is failing to load

The MSR plugin allows querying the state of DCI, a debugging interface available for Intel CPUs that should be disabled on production machines according to [fwupd's documentation](<https://github.com/fwupd/fwupd/blob/master/plugins/msr/README.md>). 

This plugin needs the `msr` kernel module loaded. `msr` is a built-in kernel module in all the official Arch Linux kernel packages, but unofficial kernel packages might have it as a loadable kernel module. In the latter case, we need to explicitly [load the module at boot](<../zh-cn/Load_the_module_at_boot.html> "Load the module at boot"). 

### Failed to load daemon: failed to load engine: No ESP with path

When starts fwupd, it checks the esp location as `EspLocation` from `/etc/fwupd/daemon.conf`. Modify it to your corresponding setup if encounter this error. 
