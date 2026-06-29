相关文章

  * [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")
  * [极简 initramfs](<../zh-cn/%E6%9E%81%E7%AE%80_initramfs.html> "极简 initramfs")
  * [启动调试](<../zh-cn/%E5%B8%B8%E8%A7%84%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html#%E7%B3%BB%E7%BB%9F%E5%90%AF%E5%8A%A8%E9%97%AE%E9%A2%98> "启动调试")
  * [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")
  * [dracut](<../zh-cn/Dracut.html> "Dracut")
  * [Clevis](</wzh/index.php?title=Clevis&action=edit&redlink=1> "Clevis（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [Booster](<https://wiki.archlinux.org/title/Booster> "arch:Booster")，最近一次同步于 2024-6-9，若英文版本有所[更改](<https://wiki.archlinux.org/title/Booster?diff=0&oldid=810174>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Booster_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 需要翻译。（在 [Talk:Booster#](<../zh-cn/Talk:Booster.html>) 中讨论）

[Booster](<https://github.com/anatol/booster>) 是一个快速的[initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs")生成器，类似于[mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")和[dracut](<../zh-cn/Dracut.html> "Dracut")。 Booster 的灵感来源于["distri" 项目](<https://michael.stapelberg.ch/posts/2020-01-21-initramfs-from-scratch-golang/>)，旨在创建小而快的启动映像。 

Booster 提供了 `/usr/bin/booster` 用户空间工具，以生成 initramfs 映像。生成的映像默认位于 `/boot/`。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [booster](<https://archlinux.org/packages/?name=booster>)包。软件包安装钩子会生成 initramfs 镜像，每个已安装的内核生成一个镜像（例如 [linux](<https://archlinux.org/packages/?name=linux>)包, {[linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包）。镜像文件位于 `/boot` 目录下： 
    
    $ ls -lh /boot/booster*
    
    -rwxr-xr-x 1 root root 4.0M Dec 16 16:20 /boot/booster-linux.img
    
也可以手动创建镜像： 
    
    $ booster build mybooster.img
    
##  配置

Booster 配置文件位于 `/etc/booster.yaml`。如果文件为空，那么booster将会使用默认配置 (host-specific images, no network)。配置详见 [booster(1) § CONFIG FILE](<https://man.archlinux.org/man/booster.1#CONFIG_FILE>)。 

###  早期加载内核模块

有时，一些内核模块需要在 initramfs 阶段加载。 

例如，当你需要加载 `nvidia` 模块时，可以在配置文件中采取以下设置： 
    
    /etc/booster.yaml
    
    modules_force_load: nvidia
    
然后[#重新生成 booster 镜像](<#%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90_booster_%E9%95%9C%E5%83%8F>)。 

###  加密

Booster supports [LUKS](<../zh-cn/Dm-crypt.html> "LUKS") based full-disk encryption out-of-the-box like [Clevis](</wzh/index.php?title=Clevis&action=edit&redlink=1> "Clevis（页面不存在）"). The generator does not need any extra configuration. Yet, for the initramfs you need to append information about the LUKS partition where the root resides. This is done with either `rd.luks.uuid=_LUKSUUID_` or `rd.luks.name=_LUKSUUID_ =_LUKSNAME_` [kernel parameter](<../zh-cn/Kernel_parameter.html> "Kernel parameter") that need to be specified in the boot loader configuration file. `_LUKSUUID_` specifies the [UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID") of the encrypted LUKS partition that needs to be unlocked by Booster. The [booster(1) § UUID parameters](<https://man.archlinux.org/man/booster.1#UUID_parameters>) manual recommends that the UUID does not contain any quotes. `_LUKSNAME_` specifies name of the unlocked partition (as in `/dev/mapper/_LUKSNAME_`). See [booster(1) § BOOT TIME KERNEL PARAMETERS](<https://man.archlinux.org/man/booster.1#BOOT_TIME_KERNEL_PARAMETERS>) for related options. 

No image rebuild is required. Once the boot loader configuration is done, reboot the computer. After that you will see a `Enter passphrase for _YOURROOT_ :` prompt at boot time asking for a password for the encrypted root partition. 

#### systemd style binding

Booster also supports partitions [bound with systemd](<https://0pointer.net/blog/unlocking-luks2-volumes-with-tpm2-fido2-pkcs11-security-hardware-on-systemd-248.html>) such as `systemd-fido2` and `systemd-tpm2`. 

If you use `systemd-fido2` then please install [libfido2](<https://archlinux.org/packages/?name=libfido2>)包 package and add fido2-assert to the image using following configuration: 
    
    /etc/booster.yaml
    
    extra_files: fido2-assert
    
[Regenerate the booster images](<#Regenerate_booster_images>). Booster will detect this configuration during boot and use the present YubiKey to unlock the drive. 

**注意：** Before commit 1b65577, it has been reported Booster may not load some necessary kernel modules early enough to unlock encrypted partitions with a FIDO2 key. In this case, add the following modules to be forcibly loaded:
    
    /etc/booster.yaml
    
    modules_force_load: **usbhid** ,**hid_sensor_hub**
    extra_files: fido2-assert
    
###  重新生成 booster 镜像

完成 Booster 配置后，需要更新 `/boot` 中的 Booster 镜像。可以使用 `booster build booster-foo.img` 手动生成镜像，也可以使用便捷脚本 `/usr/lib/booster/regenerate_images` 遍历所有已安装的内核，为每个内核生成 Booster 镜像。 

##  引导加载程序配置

生成映像后，就该配置[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")了。 

### rEFInd

如果配置已经依赖于[自动检测](<../zh-cn/REFInd.html#%E5%AF%B9%E4%BA%8E_rEFInd_%E8%87%AA%E5%8A%A8%E6%A3%80%E6%B5%8B%E5%88%B0%E7%9A%84%E5%86%85%E6%A0%B8> "REFInd")]，则无需额外更改配置。[rEFInd](<../zh-cn/REFInd.html> "REFInd") 支持 [initrd 文件命名为 booster*](<https://sourceforge.net/p/refind/code/ci/778878f7f30f68b7fa0282074e5dd8fc5894a212/>)。 

如果在[refind.conf](<../zh-cn/REFInd.html#refind_linux.conf> "REFInd")或[ 手动启动项](<../zh-cn/REFInd.html#%E6%89%8B%E5%8A%A8%E5%90%AF%E5%8A%A8%E9%A1%B9> "REFInd")中手动指定 initramfs 路径，请确保使用正确的文件名。例如，`**booster** -linux.img` 而不是 `**initramfs** -linux.img`。 

### systemd-boot

要使用 [systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") 启用新的 initramfs 映像，只需像这样创建一个新的引导加载器条目： 
    
    /boot/loader/entries/booster.conf
    
    title Arch Linux with booster
    linux /vmlinuz-linux
    initrd /booster-linux.img
    options root=UUID=08f83949-bcbb-47bb-bc17-089aaa59e17e rw

根文件系统在 `UUID=08f83949-bcbb-47bb-bc17-089aaa59e17e`。运行 `blkid /dev/_ROOTDEVICE_` 查找您的根设备 UUID。 

##  问题解决

###  调试

如果 Booster 出现问题，不能按预期运行，请启用调试信息输出，以提供更多信息说明发生了什么： 

  * 对于生成器，有一个 `-debug` 命令行参数： `booster -debug`。
  * 对于 init，有一个 `boost.debug` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。

如果您认为这是 Booster 本身的问题，那么[请在 GitHub 上提交ticket](<https://github.com/anatol/booster/issues>)。 

###  Booster生成器出现 "too many open files"错误

如果启用了 `strip` 和 `universal`，并出现类似 `/usr/lib/modules/glue_helper.ko: pipe2: too many open files` 的错误，则需要增加每个进程的打开文件限制。请参见[Limits.conf#nofile](</wzh/index.php?title=Limits.conf&action=edit&redlink=1> "Limits.conf（页面不存在）")。 

##  参见

  * [上游 README](<https://github.com/anatol/booster/blob/master/README.md>)
