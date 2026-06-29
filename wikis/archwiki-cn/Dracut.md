**翻译状态：**

  * 本文（或部分内容）译自 [dracut](<https://wiki.archlinux.org/title/dracut> "arch:dracut")，最近一次同步于 2025-07-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/dracut?diff=0&oldid=841318>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/dracut_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [booster](<../zh-cn/Booster.html> "Booster")
  * [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")
  * [统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像")

[dracut](<https://dracut-ng.github.io>) 会为内核创建初始映像，用于预载访问根文件系统所需的块设备模块（如 IDE、SCSI 或 [RAID](<../zh-cn/RAID.html> "RAID")）。安装 [linux](<https://archlinux.org/packages/?name=linux>)包 时，可以在 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 和 _dracut_ 之间进行选择。Fedora、RHEL、Gentoo 和 Debian 等系统都使用 _dracut_ ，而Arch 默认使用[mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")。 

你可以[在此](<https://dracut-ng.github.io>)查看 _dracut_ 的完整项目文档。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [dracut](<https://archlinux.org/packages/?name=dracut>)包，你也可以安装 [dracut-git](<https://aur.archlinux.org/packages/dracut-git/>)AUR 使用最新的开发版本。 

**提示：** 如果 _dracut_ **测试后功能一切正常** ，你可以[卸载](<../zh-cn/Pacman.html#%E5%88%A0%E9%99%A4%E8%BD%AF%E4%BB%B6%E5%8C%85> "卸载") [mkinitcpio](<https://archlinux.org/packages/?name=mkinitcpio>)包。

##  用法

`dracut` 的用法非常简单，而且通常就算在非标准环境下也不需要用户进行配置（如[在 LUKS 上配置 LVM](<../zh-cn/Dm-crypt/%E5%8A%A0%E5%AF%86%E6%95%B4%E4%B8%AA%E7%B3%BB%E7%BB%9F.html#%E5%9C%A8LUKS%E4%B8%8A%E9%85%8D%E7%BD%AELVM> "Dm-crypt/加密整个系统")）。 

使用如下命令为当前运行的内核生成 initramfs： 
    
    # dracut --hostonly --no-hostonly-cmdline --add-confdir no-network /boot/initramfs-linux.img
    
为了永久启用仅主机（hostonly）模式以便无需在命令行中进行指定，你可以在 dracut 的配置中添加： 
    
    /etc/dracut.conf.d/hostonly.conf
    
    hostonly="yes"
    hostonly_cmdline="no"

[dracut-git](<https://aur.archlinux.org/packages/dracut-git/>)AUR 已默认启用仅主机模式。 

**注意：** 在某些情况下，特别是在首次安装系统的时候，无法使用上述命令。在这种情况下可以改用： 
    
     # dracut -f --regenerate-all
    
使用如下命令生成后备 initramfs： 
    
    # dracut /boot/initramfs-linux-fallback.img
    
`/boot/initramfs-linux.img` 指代输出的镜像文件。如果你使用了其它内核，请考虑更改文件名。例如，对于 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 内核，输出文件应使用 `/boot/initramfs-linux-lts.img`。不过，只要[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")的配置使用了相同的文件名，就可以随意命名这些文件。 

**注意：** 创建出的文件内嵌所有已安装的[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "微码")映像。

###  额外选项

`--force` 选项会覆写现有映像文件。 

`--kver` 选项用于指定要使用的内核。该选项的输入需要匹配 `/usr/lib/modules` 目录下文件夹之一的名称。 

其它选项可参考 [dracut(8)](<https://man.archlinux.org/man/dracut.8>)。 

##  进阶配置

要注意的是，initial ramdisk 阶段有两种执行各种任务的不同方式： 

_基于 Shell（bash/busybox/dash）_ 的 initial ramdisk：该方式会启动一个初始化脚本，然后扫描 initial ramdisk 的文件系统来查找要执行的 dracut 脚本。

_基于 systemd（默认）_ 的 initial ramdisk：systemd 在 initial ramdisk 阶段时就已启动。具体要执行的任务由标准的 systemd 单元文件指定，相关信息可参考 [systemd 启动流程](<https://www.freedesktop.org/software/systemd/man/latest/bootup.html>)。

这两种方式的主要区别在于 systemd dracut 模块的存在与否。详细信息请参考 [#dracut 模块](<#dracut_%E6%A8%A1%E5%9D%97>)。 

`dracut` 可通过直接传入命令行参数进行配置（参考 [dracut(8) § OPTIONS](<https://man.archlinux.org/man/dracut.8#OPTIONS>)）。如果你希望执行 `dracut` 命令时始终带上特定参数，可以在 `/etc/dracut.conf.d/` 目录下的 `.conf` 文件中进行指定。例如： 
    
    /etc/dracut.conf.d/myflags.conf
    
    hostonly="yes"
    compress="lz4"
    add_drivers+=" i915 "
    omit_dracutmodules+=" systemd network "

更多配置选项可参考 [dracut.conf(5)](<https://man.archlinux.org/man/dracut.conf.5>)。各个选项的完整说明可参考 [dracut(8)](<https://man.archlinux.org/man/dracut.8>)。在下文中会对部分常用选项进行说明。 

###  dracut 模块

_dracut_ 使用模块化流程构建 initramfs（参考 [dracut.modules(7)](<https://man.archlinux.org/man/dracut.modules.7>)）。 _dracut_ 的所有内置模块位于 `/lib/dracut/modules.d`，可通过 `dracut --list-modules` 命令列出。更多模块可通过其它软件包提供（如 [dracut-sshd-git](<https://aur.archlinux.org/packages/dracut-sshd-git/>)AUR）。遗憾的是， _dracut_ 的内置模块缺乏文档说明，尽管它们的名称通常不言自明。 

部分模块默认被激活/禁用，可通过 `--add`/`--omit` 选项分别激活或禁用，也可以在配置文件中使用 `add_dracutmodules+=""` 或 `omit_dracutmodules+=""` 持久化更改： 
    
    /etc/dracut.conf.d/myflags.conf
    
    # ...
    add_dracutmodules+=" _dracut modules to activate_ "
    omit_dracutmodules+=" _dracut modules to deactivate_ "
    # ...

dracut 模块文档请参考[上游文档](<https://dracut-ng.github.io/dracut-ng/modules/core.html>)。 

大多数 dracut 模块都依赖于其它 dracut 模块。例如，蓝牙 dracut 模块就依赖于 dbus dracut 模块。 

#### TPM2

要使用 _systemd_ 通过 [systemd-cryptenroll](</wzh/index.php?title=Systemd-cryptenroll&action=edit&redlink=1> "Systemd-cryptenroll（页面不存在）") 调用 TPM2 解锁 _luks2_ 加密卷的功能，需要安装 [tpm2-tools](<https://archlinux.org/packages/?name=tpm2-tools>)包 并启用 `tpm2-tss` _dracut_ 模块。 

###  早期内核模块加载

可以通过 `--force_drivers` 命令行选项或 `force_drivers+=""` 配置项启用 dracut 早期加载功能（在 initramfs 阶段通过 `modprobe` 加载）。例如： 
    
    /etc/dracut.conf.d/myflags.conf
    
    # ...
    force_drivers+=" nvidia nvidia_modeset nvidia_uvm nvidia_drm "
    # ...

###  内核命令行参数

内核命令行选项可放置在 `/etc/dracut.conf.d/` 的 _.conf_ 文件内，并通过 `kernel_cmdline=` 选项进行配置。Dracut 会自动读取配置，然后创建并写入到 initramfs `/etc/cmdline.d/` 目录下的 `01-default.conf` 文件中。举个例子，你的内核命令行选项文件内容可能如下： 
    
    /etc/dracut.conf.d/cmdline.conf
    
    kernel_cmdline="rd.luks.uuid=luks-f6c738f3-ee64-4633-b6b0-eceddb1bb010 rd.lvm.lv=arch/root rd.lvm.lv=arch/swap root=/dev/arch/root rootfstype=ext4 rootflags=rw,relatime"

####  其它说明

不需要为 `dracut` 指定根块设备。参考 [dracut.cmdline(7)](<https://man.archlinux.org/man/dracut.cmdline.7>)： 

    内核使用的根设备从来都是在启动配置文件的内核命令行选项中指定的。

不过，提前设置一些参数可能会很有用，而且还可以启用一些其它功能，如提示输入额外命令行参数。所有选项请参见 [dracut.cmdline(7)](<https://man.archlinux.org/man/dracut.cmdline.7>)。下面是一些配置选项示例： 

  * 从交换分区恢复：`resume=UUID=80895b78-7312-45bc-afe5-58eb4b579422`
  * 提示输入额外内核命令行参数：{ic|1=rd.cmdline=ask}}
  * 在设定了 `quiet` 的前提下输出更多信息：`rd.info`

###  统一内核映像

_dracut_ 可以通过 `--uefi` 命令行参数或 `uefi="yes"` 配置项生成[统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像")。 

##  小提示

###  查看生成映像的信息

你可以查看生成的映像的信息，并输出到单页上： 
    
    # lsinitrd _/path/to/initramfs_or_uefi_image_ | less
    
该命令会列出生成映像时传入到 `dracut` 的参数、包含的 `dracut` 模块以及包含的所有文件。 

###  修改压缩软件

要减少压缩生成映像所消耗的时间，可以更换使用的压缩软件。 

**警告：** 请确保你的内核编译了所选软件对应的解压支持，否则系统将无法启动。你还需要安装所选压缩程序的软件包。

只需添加下列任意一行（不能多选）到 [dracut 配置文件](<#%E8%BF%9B%E9%98%B6%E9%85%8D%E7%BD%AE>)中： 
    
    compress="cat"
    compress="gzip"
    compress="bzip2"
    compress="lzma"
    compress="xz"
    compress="lzo"
    compress="lz4"
    compress="zstd"
    
默认使用的是 [gzip](<https://archlinux.org/packages/?name=gzip>)包。选择 `compress="cat"` 将不会压缩 initramfs。 

你也可以使用非官方支持的压缩软件： 
    
    compress="_program_ "
    
###  性能考虑

有些方法可以优化启动和生成 initramfs 的性能： 

  * 理解并配置最快的压缩方式。如果内核模块已经被压缩过，可能在生成 initramfs 时就不需要再次进行压缩。

  * 理解在 initramfs 中添加 systemd 可能造成的影响。如果它会降低性能，就将其移除；如果会提升性能，就纳入进来。

  * 在使用写时复制文件系统时，考虑使用 dracut-cpio。具体适用性请参考 `--enhanced-cpio` 选项。

  * 减少 initramfs 中嵌入的内核模块和 dracut 模块的数量。例如：如果安装了 [nfs-utils](<https://archlinux.org/packages/?name=nfs-utils>)包，但不依赖其进行启动，就需要显式移除 nfs dracut 模块，否则在默认配置下生成的 initramfs 会启用网络启动 - 详细信息请参考 <https://github.com/dracut-ng/dracut-ng/pull/297> 。

  * 考虑使用 [busybox](<https://archlinux.org/packages/?name=busybox>)包 dracut 模块替换掉 bash。

  * 考虑使用 `hostonly` 和 `hostonly_mode=strict`。

###  升级内核时生成新 initramfs

[linux](<https://archlinux.org/packages/?name=linux>)包 和 [dracut-git](<https://aur.archlinux.org/packages/dracut-git/>)AUR 包自带了用于在内核更新后自动生成新 initramfs 映像的 pacman 钩子。 

**提示：**

  * [dracut-ukify](<https://aur.archlinux.org/packages/dracut-ukify/>)AUR 软件包是使用 [systemd-ukify](<https://archlinux.org/packages/?name=systemd-ukify>)包 生成[统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像")的现代方法。与以下方法不同，你可以对整个内核映像[签名](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "UEFI/安全启动")，[包括 initramfs](<https://0pointer.net/blog/brave-new-trusted-boot-world.html>)。需要在 dracut 配置中使用 `uefi_secureboot_cert` 和 `uefi_secureboot_key` 选项（[dracut.conf(5)](<https://man.archlinux.org/man/dracut.conf.5>)）。
  * 另外，如果你希望 initramfs 映像也是 EFI 可执行文件（即 `_esp_ /EFI/Linux/linux-_kernel_ -_machine_id_ -_build_id_.efi`），也可以使用 [dracut-uefi-hook](<https://aur.archlinux.org/packages/dracut-uefi-hook/>)AUR。在该目录下的 EFI 二进制文件会被 [systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") 自动检测到，因此不需要在 `/boot/loader/loader.conf` 中额外创建条目。

你还需要通过卸载 [mkinitcpio](<https://archlinux.org/packages/?name=mkinitcpio>)包 或使用以下命令来阻止 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 创建和移除 initramfs 映像： 
    
    # ln -sf /dev/null /etc/pacman.d/hooks/90-mkinitcpio-install.hook
    # ln -sf /dev/null /etc/pacman.d/hooks/60-mkinitcpio-remove.hook
    
###  蓝牙键盘支持

如果检测到了蓝牙键盘，dracut 会自动启用蓝牙模块。但 dracut 需要处于 hostonly 模式才能自动发现蓝牙键盘。 

### Limine boot loader support

The [limine-dracut-support](<https://aur.archlinux.org/packages/limine-dracut-support/>)AUR package utilizes [limine-entry-tool](<https://gitlab.com/Zesko/limine-entry-tool>) with dracut and pacman hooks to automate the installation and removal of kernels and boot entries in the [Limine](</wzh/index.php?title=Limine&action=edit&redlink=1> "Limine（页面不存在）") [boot loader](<../zh-cn/Boot_loader.html> "Boot loader"). See [Limine#Boot entry automation](</wzh/index.php?title=Limine&action=edit&redlink=1> "Limine（页面不存在）") for more information. 

##  排障

###  休眠

如果从休眠中恢复无效，你可能需要配置 `dracut` 以包含 `resume` 模块。[添加一个配置文件](<#dracut_%E6%A8%A1%E5%9D%97>)： 
    
    /etc/dracut.conf.d/resume-from-hibernate.conf
    
    add_dracutmodules+=" resume "

如果适用于你的系统，你可能也需要看下[从加密交换分区恢复指南](<../zh-cn/Dm-crypt/%E4%BA%A4%E6%8D%A2%E5%88%86%E5%8C%BA%E5%8A%A0%E5%AF%86.html#Using_a_swap_partition> "Dm-crypt/交换分区加密")以及 [dracut 特定指南](<../zh-cn/Dm-crypt/%E4%BA%A4%E6%8D%A2%E5%88%86%E5%8C%BA%E5%8A%A0%E5%AF%86.html#dracut> "Dm-crypt/交换分区加密")。 

###  LVM / 软 RAID / LUKS

如果内核无法自动发现并挂载 LVM / 软 RAID / LUKS 块设备，你可以加上以下内核命令行选项重新生成 initramfs： 
    
    rd.auto rd.lvm=1 rd.dm=1 rd.md=1 rd.luks=1
    
###  A stop job is running for "brltty"

If you have issues booting or very long shutdown processes while the system waits for `brltty`, add the following to the dracut configuration line: 
    
    omit_dracutmodules+=" brltty "
    
Alternatively, uninstall [brltty](<https://archlinux.org/packages/?name=brltty>)包 if it is not needed. 

### No usable keyslot is available
    
    Cannot use whirlpool hash for keyslot encryption. 
    Keyslot open failed. 
    No usable keyslot is available.
    
A failure to boot with a message similar to the above typically will only require the user to include the `crypt` module via `add_dracutmodules`. 

##  参考

  * [Wikipedia:dracut (software)](<https://en.wikipedia.org/wiki/dracut_\(software\)> "wikipedia:dracut \(software\)")
  * [Gentoo:Dracut](<https://wiki.gentoo.org/wiki/Dracut> "gentoo:Dracut")
