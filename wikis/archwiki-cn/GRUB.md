**翻译状态：**

  * 本文（或部分内容）译自 [GRUB](<https://wiki.archlinux.org/title/GRUB> "arch:GRUB")，最近一次同步于 2024-11-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/GRUB?diff=0&oldid=820882>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GRUB_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Arch boot process](<../zh-cn/Arch_boot_process.html> "Arch boot process")
  * [分区#主引导记录](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "分区")
  * [分区#GUID 分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "分区")
  * [Unified Extensible Firmware Interface](<../zh-cn/Unified_Extensible_Firmware_Interface.html> "Unified Extensible Firmware Interface")
  * [GRUB Legacy](<../zh-cn/GRUB_Legacy.html> "GRUB Legacy")
  * [/EFI examples](</wzh/index.php?title=GRUB/EFI_examples&action=edit&redlink=1> "GRUB/EFI examples（页面不存在）")
  * [GRUB/技巧和窍门](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html> "GRUB/技巧和窍门")
  * [多引导USB设备](<../zh-cn/%E5%A4%9A%E5%BC%95%E5%AF%BC_USB_%E8%AE%BE%E5%A4%87.html> "多引导USB设备")

[GRUB](<https://www.gnu.org/software/grub/>)（GRand Unified Bootloader，大一统启动加载器），是一个[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "Arch 的启动流程")。当前的 GRUB 也被称作 **GRUB 2** ，而原始 GRUB（GRUB Legacy）表示 0.9x 版本。本页只描述 GRUB 2。 

**注意：** 在本文中，` _esp_` 表示[EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")（ESP）的挂载点。

##  受支持的文件系统

GRUB捆绑了由自己支持的[多种文件系统](<https://www.gnu.org/software/grub/manual/grub/html_node/Features.html#Features>)，尤其是[FAT32](<../zh-cn/FAT.html> "FAT32")，[ext4](<../zh-cn/Ext4.html> "Ext4")，[Btrfs](<../zh-cn/Btrfs.html> "Btrfs")和[XFS](<../zh-cn/XFS.html> "XFS")。有关一些注意事项，参见[#不支持的文件系统](<#%E4%B8%8D%E6%94%AF%E6%8C%81%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F>)

**警告：** 文件系统可能会获得一些GRUB还未支持的新特性，除非关闭这些不兼容的特性，否则这些特性无法适用于`/boot`。通常规避这个问题的方式是使用一个单独的[/boot分区](<../zh-cn/%E5%88%86%E5%8C%BA.html#/boot> "分区")，并格式化为通用的文件系统，如[FAT32](<../zh-cn/FAT.html> "FAT32")。

##  UEFI 系统

**注意：**

  * 建议阅读并理解[统一可扩展固件接口 (UEFI)](<../zh-cn/Unified_Extensible_Firmware_Interface.html> "Unified Extensible Firmware Interface")，[分区#GUID 分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "分区") 和 [Arch 的启动流程#UEFI](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#UEFI> "Arch 的启动流程")这几个页面。

  * 使用UEFI安装时，一定要让安装介质以UEFI模式启动，否则 _efibootmgr_ 将无法添加 GRUB UEFI 启动项。 但即使在 BIOS 模式工作时，安装到[后备启动路径](<#%E7%BC%BA%E7%9C%81/%E5%90%8E%E5%A4%87%E5%90%AF%E5%8A%A8%E8%B7%AF%E5%BE%84>)仍然可行，因为这一过程用不到 NVRAM。

  * 要从一个磁盘上使用 UEFI 模式启动，磁盘上必须要先有一个 EFI 分区。按照 [EFI 系统分区#检查现有的分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html#%E6%A3%80%E6%9F%A5%E7%8E%B0%E6%9C%89%E7%9A%84%E5%88%86%E5%8C%BA> "EFI 系统分区") 上说的来查看你是否已经有一个 EFI 分区，如若没有，就创建一个。

  * 本页所有内容假定GRUB2是能够通过`insmod`加载额外模块的。[#Shim-lock](<#Shim-lock>)中讨论了相关问题，这种情况下UEFI系统无法启用安全启动（Secure Boot）功能。在一个启用了安全启动的系统上，如果你想要使用任何不包含在标准GRUB EFI `grubx64.efi`文件中的额外GRUB模块，你必须通过`grub-mkstandalone`或者使用`grub-install`重新安装GRUB，以重新生成包含所需模块的`grubx64.efi`文件。

###  安装

**注意：**

  * 不同硬件厂商的 UEFI 实现方式不一样，下面描述的步骤应该可以在大部分 UEFI 系统上面正常应用。对于用了下面的方法却遇到问题的用户，请将在特定的硬件上所遇到的问题的细节，以及可能的解决办法分享出来。这些案例可以添加到页面 [GRUB/EFI examples](</wzh/index.php?title=GRUB/EFI_examples&action=edit&redlink=1> "GRUB/EFI examples（页面不存在）") 上面。

  * 本节假设您正在 x64（64位）UEFI系统上安装 GRUB。对于 IA32 （32 位） UEFI 系统（不要和 32 位 CPU 相混淆）， 将`x86_64-efi`替换成`i386-efi`。根据[UEFI#检查系统位数](<../zh-cn/UEFI.html#%E6%A3%80%E6%9F%A5%E7%B3%BB%E7%BB%9F%E4%BD%8D%E6%95%B0> "UEFI")中的说明来确定你的UEFI系统位数。

**警告：** 自[grub](<https://archlinux.org/packages/?name=grub>)包 2:2.06.r566.g857af0e17-1起，无法从IA32 UEFI(`i386-efi`)系统启动。参见[FS#79098](<https://bugs.archlinux.org/task/79098>)。

首先[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [grub](<https://archlinux.org/packages/?name=grub>)包 和 [efibootmgr](<https://archlinux.org/packages/?name=efibootmgr>)包。其中“GRUB”是启动引导器，“efibootmgr”被 GRUB 脚本用来将启动项写入 NVRAM。 

然后按照下列步骤将GRUB安装到你的硬盘上： 

  1. [挂载 EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html#%E6%8C%82%E8%BD%BD%E5%88%86%E5%8C%BA> "EFI 系统分区")。需要注意的是在本节的内容里，把 `_esp_` 替换成ESP分区挂载点；
  2. 选择一个bootloader-id，在本例被称为 `GRUB`。这将在 `_esp_ /EFI/` 中创建一个与标识同名的目录来储存 EFI 二进制文件，而且这个名字还会用于在 UEFI 启动菜单中区分 GRUB 启动项；
  3. 执行下面的命令来将 GRUB EFI 应用 `grubx64.efi` 安装到 `_esp_ /EFI/GRUB/`，并将其模块安装到 `/boot/grub/x86_64-efi/`。

**注意：**

  * 确保你安装 GRUB 软件包和运行命令的系统是你想用 GRUB 引导的系统。也就是说如果你是通过安装介质引导的，你需要在 chroot 之后再运行 `grub-install`。如果因为某些原因不得不在安装的系统之外运行 `grub-install`，在后面加上 `--boot-directory=` 选项来指定挂载 `/boot` 目录的路径，例如 `--boot-directory=/mnt/boot`。
  * 某些主板无法处理包含空格的 `bootloader-id` 。

    # grub-install --target=x86_64-efi --efi-directory=_esp_ --bootloader-id=GRUB

上述安装完成后， GRUB 的主目录将位于 `/boot/grub/`。注意上述例子中，`grub-install` 还将[在固件启动管理器中创建一个条目](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html#%E5%9C%A8%E5%9B%BA%E4%BB%B6%E5%90%AF%E5%8A%A8%E7%AE%A1%E7%90%86%E5%99%A8%E4%B8%AD%E5%88%9B%E5%BB%BA_GRUB_%E6%9D%A1%E7%9B%AE> "GRUB/技巧和窍门")，名叫 `GRUB`。如果你的启动项已满，这个命令会执行失败。你需要使用 [efibootmgr](<../zh-cn/UEFI.html#efibootmgr> "UEFI") 来删除不必要的条目。 

在配置完成后，记得[#生成主配置文件](<#%E7%94%9F%E6%88%90%E4%B8%BB%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)。 

**提示：** 如果你使用了 `--removable` 选项，那 GRUB 将被安装到 `_esp_ /EFI/BOOT/BOOTX64.EFI` （当使用 `i386-efi` 时是 `_esp_ /EFI/BOOT/BOOTIA32.EFI` ），此时即使 EFI 变量被重设或者你把这个驱动器接到其他电脑上，你仍可从这个驱动器上启动。通常来说，你只要像操作 BIOS 设备一样在启动时选择这个驱动器就可以了。如果设备是同时安装了Windows的多引导启动，注意 Windows 通常会在这里安装一个 EFI 可执行程序，该程序的目的是仅重建Windows的UEFI启动项。如果你想在[Mac](<../zh-cn/Mac.html> "Mac")上安装GRUB，那你必须要使用该选项。某些台式机主板只会在此位置寻找 EFI 可执行文件，因此该选项是必需的，尤其是微星（MSI）主板。 如果你更新了UEFI，启动项可能会在更新后丢失。因此可以创建一个“removable”启动项作为后备。

**注意：**

  * `--efi-directory` 和 `--bootloader-id` 是 GRUB UEFI 特有的。`--efi-directory` 替代了已经废弃的 `--root-directory`。
  * 您可能注意到在 `grub-install` 命令中没有 _device_path_ 选项（例如 `/dev/sda`）。事实上即使提供了 _device_path_ ，也会被 GRUB UEFI 安装脚本忽略，因为 UEFI 启动加载器不使用 MBR 启动代码或启动扇区。

如果遇到问题，查看 [UEFI 故障排查](<#UEFI_%E5%BC%82%E5%B8%B8>)。参见[GRUB/技巧和窍门#UEFI 延伸阅读](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html#UEFI_%E5%BB%B6%E4%BC%B8%E9%98%85%E8%AF%BB> "GRUB/技巧和窍门")。 

###  启用安全启动

GRUB支持使用CA密钥或shim进行安全启动，安装命令受你选择的方法而不同。 

**警告：**

  * 错误配置[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "UEFI/安全启动")会造成你的系统无法启动。如果启用安全启动后系统因某种原因无法启动，你应该在固件设置中关闭它并重启系统。
  * 启动引导器加载不必要的模块会带来潜在安全风险，没有必要不要使用这些命令。

####  CA密钥

下列命令使用CA密钥： 
    
    # grub-install --target=x86_64-efi --efi-directory=_esp_ --bootloader-id=GRUB --modules="tpm" --disable-shim-lock
    
#### Shim-lock

**注意：** 进行下面的操作前，你应该确保已经按照[UEFI/安全启动#shim](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html#shim> "UEFI/安全启动")中的指示完成设置，并已经安装了[sbsigntools](<https://archlinux.org/packages/?name=sbsigntools>)包用于接收密钥。

当使用Shim-lock时，只有当GRUB二进制文件包含了全部用于读取含有[vmlinuz](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Vmlinuz")和[initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs")镜像的文件系统的必要模块时，才可以成功进入安全启动模式。 

自GRUB版本`2.06.r261.g2f4430cc0`起，无法在安全启动模式下通过`insmod`加载模块，因为这违背了不允许侧加载任意代码的要求。如果GRUB模块没有嵌入在EFI二进制文件中，而GRUB又通过`insmod`侧加载它们，GRUB会产生启动失败的信息： 
    
    error: prohibited by secure boot policy
    
根据Ubuntu的[官方构建脚本](<https://git.launchpad.net/~ubuntu-core-dev/grub/+git/ubuntu/tree/debian/build-efi-images?h=debian/2.06-2ubuntu12>)，整合下列模块到已签名的GRUB EFI二进制文件`grubx64.efi`： 

  * ["基础"模块](<https://git.launchpad.net/~ubuntu-core-dev/grub/+git/ubuntu/tree/debian/build-efi-images?h=debian/2.06-2ubuntu12#n87>)，用于从CD或简单分区硬盘启动： `all_video`, `boot`, `btrfs`, `cat`, `chain`, `configfile`, `echo`, `efifwsetup`, `efinet`, `ext2`, `fat`, `font`, `gettext`, `gfxmenu`, `gfxterm`, `gfxterm_background`, `gzio`, `halt`, `help`, `hfsplus`, `iso9660`, `jpeg`, `keystatus`, `loadenv`, `loopback`, `linux`, `ls`, `lsefi`, `lsefimmap`, `lsefisystab`, `lssal`, `memdisk`, `minicmd`, `normal`, `ntfs`, `part_apple`, `part_msdos`, `part_gpt`, `password_pbkdf2`, `png`, `probe`, `reboot`, `regexp`, `search`, `search_fs_uuid`, `search_fs_file`, `search_label`, `sleep`, `smbios`, `squash4`, `test`, `true`, `video`, `xfs`, `zfs`, `zfscrypt`, `zfsinfo`

  * ["平台特定"的模块](<https://git.launchpad.net/~ubuntu-core-dev/grub/+git/ubuntu/tree/debian/build-efi-images?h=debian/2.06-2ubuntu12#n147>)用于x86_64-efi架构，如： 
    * `play`：启动时播放声音
    * `cpuid`：启动时检查CPU功能
    * `tpm`：提供可度量启动（Measured Boot） / [可信平台模块](<../zh-cn/%E5%8F%AF%E4%BF%A1%E5%B9%B3%E5%8F%B0%E6%A8%A1%E5%9D%97.html> "可信平台模块")支持
  * ["高级"模块](<https://git.launchpad.net/~ubuntu-core-dev/grub/+git/ubuntu/tree/debian/build-efi-images?h=debian/2.06-2ubuntu12#n159>)，包含以下模块： 
    * `cryptodisk`：从[Dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt")加密磁盘启动
    * `gcry__algorithm_`：支持特定散列和加密算法
    * `luks`：从[LUKS](<../zh-cn/Dm-crypt.html> "LUKS")加密的磁盘启动
    * {{ic|lvm}：从[LVM](<../zh-cn/LVM.html> "LVM")逻辑卷磁盘启动
    * `mdraid09`, `mdraid1x`, `raid5rec`, `raid6rec`：从[RAID](<../zh-cn/RAID.html> "RAID")虚拟磁盘启动

你必须通过设置shell变量的方式构造GRUB模块列表，我们将变量设置为`GRUB_MODULES`。你也可以使用[最新的Ubuntu脚本](<https://git.launchpad.net/~ubuntu-core-dev/grub/+git/ubuntu/tree/debian/build-efi-images>)作为出发点，然后去除你系统不需要的模块。去除模块会让启动速度相对更快，并节省一些EFI系统分区的空间。 

如果GRUB从UEFI shim 加载器启动，你还需要一个[Secure Boot Advanced Targeting (SBAT)](<https://github.com/rhboot/shim/blob/main/SBAT.md>) 文件/部分包含在EFI二进制文件中，来提高安全性。这个SBAT文件/部分包含GRUB二进制文件的元数据（版本，维护者，开发者，上游URL），能够让shim更容易确认存在安全漏洞的GRUB版本，并拒绝加载[[1]](<https://eclypsium.com/2020/07/29/theres-a-hole-in-the-boot/#additional>)[[2]](<https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/GRUB2SecureBootBypass2021>)，如[UEFI shim 启动加载器安全启动生命周期改进](<https://github.com/rhboot/shim/blob/main/SBAT.md>)文档所述。 

如果`grubx64.efi`缺少SBAT部分，第一阶段UEFI启动加载器shim会拒绝加载启动`grubx64.efi`。 

GRUB安装后，会提供一个简单的SBAT _.csv_ 文件在`/usr/share/grub/sbat.csv`。 

重新安装GRUB，使用提供的SBAT文件和包含所有需要模块的`GRUB_MODULES`，并签名： 
    
    # grub-install --target=x86_64-efi --efi-directory=_esp_ --modules=${GRUB_MODULES} --sbat /usr/share/grub/sbat.csv
    # sbsign --key MOK.key --cert MOK.crt --output _esp_ /EFI/GRUB/grubx64.efi _esp_ /EFI/GRUB/grubx64.efi
    # cp _esp_ /EFI/GRUB/grubx64.efi _esp_ /EFI/BOOT/grubx64.efi
    
重启，选择 _MokManager_ 中的密钥，安全启动应该就可以工作了。 

####  使用安全启动

安装完成后，参考[安全启动#实施安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html#%E5%AE%9E%E6%96%BD%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8> "安全启动")来启用安全启动。 

如果使用CA密钥，则可以使用 [sbctl](<https://archlinux.org/packages/?name=sbctl>)包 自动执行密钥管理、注册和文件签名，有关详细信息，请参阅[安全启动#sbctl](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html#sbctl> "安全启动")。 

##  BIOS 系统

###  GUID 分区表 (GPT) 特殊操作

使用BIOS引导[GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT")的分区情况（BIOS/[GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT")）下，必须使用 [BIOS 启动分区](<https://www.gnu.org/software/grub/manual/grub/html_node/BIOS-installation.html#BIOS-installation>)。GRUB将`core.img`嵌入到这个分区。 

**注意：**

  * 在尝试这种方法之前请记住不是所有的系统都支持这种分区方案，请参阅 [GUID 分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_Partition_Table> "Partitioning")。
  * 此额外分区只由 GRUB 在 BIOS/GPT 分区方式中使用。对于 BIOS/MBR 分区方式，GRUB 会把`core.img`放到 [MBR 后间隙(post-MBR gap)](<../zh-cn/Arch_boot_process.html#BIOS> "Arch boot process")中去，而在 GPT 中并不能保证在第一个分区之前有可以这样使用的空间。
  * [UEFI](<../zh-cn/UEFI.html> "UEFI") 系统也不需要这额外分区，因为它不需要嵌入启动扇区。UEFI 系统需要有 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")。

安装 GRUB 前，在一个没有文件系统的磁盘上，创建一个1兆字节（使用 [fdisk](<../zh-cn/Fdisk.html> "Fdisk") 或 [gdisk](<../zh-cn/GPT_fdisk.html> "Gdisk") 和参数`+1M`）的分区，将分区类型设置为 GUID `21686148-6449-6E6F-744E-656564454649`。 

  * 对于 [fdisk](<../zh-cn/Fdisk.html> "Fdisk")，选择分区类型 `BIOS boot`。
  * 对于 [gdisk](<../zh-cn/GPT_fdisk.html> "Gdisk")，选择分区类型代码 `ef02`。
  * 对于 [parted](<../zh-cn/Parted.html> "Parted")， 在新创建的分区上设置/激活 `bios_grub` 标记。

这个分区可以处于磁盘的前 2TB 空间中的任意位置，但需要在安装 GRUB 之前创建好。分区建立好后，按下面的命令安装启动管理器。 

第一个分区之前的空间也可以用作 BIOS 启动分区，但是这会违反 GPT 对齐规范。因为这个分区不会经常访问，所以性能的影响很小，只不过有些分区工具会发出警告。可以在 [fdisk](<../zh-cn/Fdisk.html> "Fdisk") 或 [gdisk](<../zh-cn/GPT_fdisk.html> "Gdisk") 中创建一个从 34 扇区开始，一直到 2047扇区的分区，然后按照上述方式设置类型。为了让其它分区对齐，可以最后再创建此分区。 

###  主引导记录 (MBR) 特殊操作

一般来说，如果使用兼容 DOS 的分区对齐模式，[主引导记录](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "分区") 512 字节结束位置和第一个分区之间都有 31KB 的空闲空间。不过，为了提供足够的空间嵌入 GRUB 的`core.img`文件，建议将这个空间设置为 1 到 2 MB ([FS#24103](<https://bugs.archlinux.org/task/24103>))。 建议使用支持 1 MB [分区对齐](<../zh-cn/%E5%88%86%E5%8C%BA.html#Partition_alignment> "Partitioning")的分区软件来分区, 因为这样也能满足非 512 字节扇区磁盘分区的需求（这一点就与嵌入`core.img`没有关系了）。 

###  安装

（在 [archiso](<../zh-cn/Archiso.html> "Archiso") 环境下，比如[安装系统](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")时，请记得在 arch-chroot 环境中操作。）[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [grub](<https://archlinux.org/packages/?name=grub>)包。如果之前安装过 [grub-legacy](<https://aur.archlinux.org/packages/grub-legacy/>)AUR，安装完成后 [grub](<https://archlinux.org/packages/?name=grub>)包 会取代它。然后运行 
    
    # grub-install --target=i386-pc _/dev/sdX_
    
**注意：** 这里的`i386-pc`是有意为之，与你机器的实际架构无关， 其中 `_/dev/sdX_` 是要安装 GRUB 的**磁盘**(**不是分区**)，比如磁盘 `/dev/sda`、`/dev/nvme0n1`或者`/dev/mmcblk0`，而**不是** 分区 `/dev/sda1`，你可以查看[Device file#Block device names](<../zh-cn/Device_file.html#Block_device_names> "Device file")来获得块设备命名方案的详细描述。

现在你需要[生成主配置文件](<#%E7%94%9F%E6%88%90%E4%B8%BB%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)。 

如果你的 `/boot` 使用了 [LVM](<../zh-cn/LVM.html> "LVM")（逻辑分卷管理器），GRUB 可以安装到多个物理磁盘上。 

**提示：** 对于安装 GRUB 的其他方式，例如安装到一个U盘上，可以参考 [其它安装方式](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html#%E5%85%B6%E5%AE%83%E5%AE%89%E8%A3%85%E6%96%B9%E5%BC%8F> "GRUB/技巧和窍门")。

`grub-install` 命令的详细信息请参考 [grub-install(8)](<https://man.archlinux.org/man/grub-install.8>) 和 [GRUB 手册](<https://www.gnu.org/software/grub/manual/grub/html_node/BIOS-installation.html#BIOS-installation>)。 

##  配置

完成安装之后，GRUB 在每次启动的时候加载配置文件 `/boot/grub/grub.cfg`。你可以使用工具来[#生成 grub.cfg](<#%E7%94%9F%E6%88%90_grub.cfg>)，或者可以手动[#定制 grub.cfg](<#%E5%AE%9A%E5%88%B6_grub.cfg>)。 

###  生成 grub.cfg

本节只讲述如何编辑配置文件 `/etc/default/grub`。更多信息请见 [GRUB/技巧和窍门](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html> "GRUB/技巧和窍门")。 

**注意：** 请记住，每当修改 `/etc/default/grub` 或者 `/etc/grub.d/` 中的文件之后，都需要再次[生成主配置文件](<#%E7%94%9F%E6%88%90%E4%B8%BB%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)。

**警告：** 如果新版本的GRUB改变了配置文件的句法规则，比如新版本的配置文件可能会使用现有GRUB二进制文件不支持的功能，错误的配置文件可能会导致系统无法引导，请更新或重新安装引导器（见[GRUB#UEFI 系统](<#UEFI_%E7%B3%BB%E7%BB%9F>)或[GRUB#BIOS 系统](<#BIOS_%E7%B3%BB%E7%BB%9F>)）

####  生成主配置文件

安装后,需要生成主配置文件 `/boot/grub/grub.cfg`。配置文件的生成过程受到 `/etc/default/grub` 中的选项和 `/etc/grub.d/` 下脚本的影响。对于`/boot/grub/grub.cfg`中的选项，GNU的[文档](<https://www.gnu.org/software/grub/manual/grub/html_node/Simple-configuration.html>)有各个选项的简明描述。 

如果你没有进行额外配置，自动生成程序会在当前启动的系统的根文件系统中侦测配置文件。所以请确保系统已经启动或者已经通过 chroot 进入。 

**注意：**

  * 默认的文件路径是 `/boot/grub/grub.cfg`，而非 `/boot/grub/i386-pc/grub.cfg`。

  * 如果你是在 chroot 或者 systemd-nspawn 容器中运行 grub-mkconfig，可能会报 grub-probe 无法获取 "canonical path of /dev/sdaX" 错误而无法正常执行。此时可以尝试使用 arch-chroot，参见 [BBS post](<https://bbs.archlinux.org/viewtopic.php?pid=1225067#p1225067>)。

使用 grub-mkconfig 工具来生成 `/boot/grub/grub.cfg`： 
    
    # grub-mkconfig -o /boot/grub/grub.cfg
    
自动生成脚本默认将在生成的配置文件中为所有已安装的 Arch Linux [内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernels")添加条目。 

**提示：**

  * 每次安装或者移除一个[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernels")后，你都需要重新运行一次 grub-mkconfig 命令。
  * 若要管理多个 GRUB 条目，比如既使用 [linux](<https://archlinux.org/packages/?name=linux>)包 又使用 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 内核，相关的提示可以参见 [GRUB/技巧和窍门#多个启动条目](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html#%E5%A4%9A%E4%B8%AA%E5%90%AF%E5%8A%A8%E6%9D%A1%E7%9B%AE> "GRUB/技巧和窍门")。

如果想要自动为其他操作系统添加条目，请见[#探测其他操作系统](<#%E6%8E%A2%E6%B5%8B%E5%85%B6%E4%BB%96%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F>)。 

如果想要添加自定义条目，你可以编辑 `/etc/grub.d/40_custom` 文件，然后重新生成 `/boot/grub/grub.cfg`。或者你可以创建 `/boot/grub/custom.cfg` 文件然后把条目添加进这里面。修改 `/boot/grub/custom.cfg` 文件后不用再运行 grub-mkconfig 程序，因为 `/etc/grub.d/41_custom` 文件已经在生成的主配置文件中添加了相关的 `source` 语句来引用 `/boot/grub/custom.cfg`。 

**提示：**`/etc/grub.d/40_custom` 可以用做创建 `/etc/grub.d/_nn_ _custom` 文件的模板，其中 `_nn_` 为优先级，规定脚本文件的执行顺序。而脚本文件的执行顺序决定了其所添加的条目在 GRUB 启动菜单中的位置。` _nn_` 应当比 `06` 大，以此保证重要的脚本能够优先执行。

如要参考自定义菜单条目的例子，请看[#启动菜单条目示例](<#%E5%90%AF%E5%8A%A8%E8%8F%9C%E5%8D%95%E6%9D%A1%E7%9B%AE%E7%A4%BA%E4%BE%8B>)。 

####  探测其他操作系统

想要让 grub-mkconfig 探测其他已经安装的系统并自动把他们添加到启动菜单中，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [os-prober](<https://archlinux.org/packages/?name=os-prober>)包 并[挂载](<../zh-cn/File_systems.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "File systems")包含其它系统引导程序的磁盘分区。然后重新运行 grub-mkconfig。如果你得到以下输出：`Warning: os-prober will not be executed to detect other bootable partitions`，你需要编辑`/etc/default/grub`并取消下面这一行的注释，如果没有相应注释的话就在文件末尾添加上： 
    
    GRUB_DISABLE_OS_PROBER=false
    
然后运行 grub-mkconfig 再试一次。 

**注意：**

  * 分区挂载点并不重要， _os-prober_ 读取`mtab`信息来确认并搜索引导程序的位置。
  * 记得每次运行 grub-mkconfig 之前都把包含其他操作系统引导程序的分区挂载上，以免这些操作系统的启动项丢失。
  * _os-prober_ 在chroot中可能无法正常运作。如果遇到这种情况，重启并引导进入系统后再次尝试。

**提示：** 你可能想让grub记住你上次选择的启动项，参见[GRUB/技巧和窍门#调用之前的启动条目](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html#%E8%B0%83%E7%94%A8%E4%B9%8B%E5%89%8D%E7%9A%84%E5%90%AF%E5%8A%A8%E6%9D%A1%E7%9B%AE> "GRUB/技巧和窍门")

##### Windows

对于以 UEFI 模式安装的Windows，确保含有 Windows Boot Manager (`bootmgfw.efi`，Windows EFI 引导程序) 的分区被挂载，以root身份运行[os-prober](<https://archlinux.org/packages/?name=os-prober>)包来检测并为其生成启动菜单项。 

对于以 BIOS 模式安装的 Windows，挂载 Windows 的 _系统分区_ （其[文件系统标签](<../zh-cn/Persistent_block_device_naming.html#%E9%80%9A%E8%BF%87%E6%A0%87%E7%AD%BE> "Persistent block device naming")应该为`System Reserved`或`SYSTEM`），以root身份运行[os-prober](<https://archlinux.org/packages/?name=os-prober>)包来检测并为其生成启动菜单项。 

**注意：**

  * `os-prober` 会尝试使用 `grub-mount` 来挂载并检测某个分区中是否存在所必需的 `.efi` 文件。可能需要安装 [fuse3](<https://archlinux.org/packages/?name=fuse3>)包 以确保 `grub-mount` 正常工作，否则将无法检测到 Windows 系统。
  * 通过默认 Linux 驱动挂载的 NTFS 分区可能无法被检测到。如果 GRUB 无法检测到，尝试安装[NTFS-3G](<../zh-cn/NTFS-3G.html> "NTFS-3G")并重新挂载分区。

####  额外的参数

如想为 Linux 镜像添加额外的参数，你可以在 `/etc/default/grub` 中设置 `GRUB_CMDLINE_LINUX` 和 `GRUB_CMDLINE_LINUX_DEFAULT` 变量。生成普通启动项时，这两个参数的值会合并在一起传给内核。生成 recovery 启动项时, 仅使用 `GRUB_CMDLINE_LINUX` 参数。 

两个参数不是一定要一起用。例如要系统支持[休眠](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86/%E6%8C%82%E8%B5%B7%E4%B8%8E%E4%BC%91%E7%9C%A0.html#%E4%BC%91%E7%9C%A0> "电源管理/挂起与休眠")后恢复,可以使用 `GRUB_CMDLINE_LINUX_DEFAULT="resume=UUID=_uuid-of-swap-partition_ quiet"`，其中 `_uuid-of-swap-partition_` 是你的交换分区的 [UUID](<../zh-cn/Persistent_block_device_naming.html#%E9%80%9A%E8%BF%87_uuid> "Persistent block device naming")。这样在生成 recovery 启动项时，将不会启用 resume 功能，也不会有 `quiet` 参数来省略启动时的内核信息。而其他的普通启动项会包含它们。 

grub-mkconfig 默认使用 [UUID](<../zh-cn/Persistent_block_device_naming.html#%E9%80%9A%E8%BF%87_uuid> "Persistent block device naming") 定位根文件系统，要禁用此设置，取消 `GRUB_DISABLE_LINUX_UUID=true` 的注释。 

要生成 GRUB recovery 启动项，需要确保在 `/etc/default/grub` 中 `GRUB_DISABLE_RECOVERY` 没有设置为 `true`。 

更多信息请参考[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。 

####  设置启动菜单的顶层启动项

默认情况下 _grub-mkconfig_ 使用`sort -V`对内核进行排序，并把第一个内核作为顶层启动项。也就是说，如果你同时安装了[linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包和[linux](<https://archlinux.org/packages/?name=linux>)包 ，因为`/boot/vmlinuz-linux-lts`排在`/boot/vmlinuz-linux`前面，LTS内核会作为顶层启动项，这可能是不希望的结果。在`/etc/default/grub`中指定`GRUB_TOP_LEVEL=_内核路径_`可以覆盖自动排序结果。要让普通内核作为顶层启动项，设置为`GRUB_TOP_LEVEL="/boot/vmlinuz-linux"`。 

#### LVM

**警告：** GRUB 不支持 thin-provisioned 逻辑卷。

如果你的 `/boot` 或者 `/` 分区使用了 [LVM](<../zh-cn/LVM.html> "LVM")，确保 `lvm` 模块已经预先加载好。 
    
    /etc/default/grub
    
    GRUB_PRELOAD_MODULES="... lvm"

####  独立磁盘冗余阵列（RAID）

GRUB 可以很方便地操作 [RAID](<../zh-cn/RAID.html> "RAID") 卷，你只需加载 GRUB 模块 `mdraid09` 或者 `mdraid1x` 就可以像其他卷一样进行操作了。 
    
    /etc/default/grub
    
    GRUB_PRELOAD_MODULES="... mdraid09 mdraid1x"

例如 `/dev/md0` 写成： 
    
    set root=(md/0)
    
而 RAID 卷上的分区（如 `/dev/md0p1`）则是： 
    
    set root=(md/0,1)
    
如要在 `/boot` 分区使用 RAID1 时（或者 `/boot` 位于使用了 RAID1 的根分区之中）安装 GRUB，对于 BIOS 系统，直接在各个驱动器上运行 grub-install 即可，就像这样： 
    
    # grub-install --target=i386-pc --debug /dev/sda
    # grub-install --target=i386-pc --debug /dev/sdb
    
上例中 `/boot` 所在的 RAID 1 序列位于 `/dev/sda` 和 `/dev/sdb` 上。 

**注意：** GRUB 支持从 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") RAID 0/1/10 启动，但 **不支持** RAID 5/6。对 RAID 5/6，你可以使用 [mdadm](<../zh-cn/RAID.html#%E5%AE%89%E8%A3%85> "RAID")，这个 GRUB 是支持的。

####  加密的/boot

GRUB 还专门支持从加密的 `/boot` 启动。这需要解锁一个 [LUKS](<../zh-cn/Dm-crypt.html> "Dm-crypt") 块设备，来读取配置文件以及加载 [initramfs](<../zh-cn/Arch_boot_process.html#initramfs> "Arch boot process") 和[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernels")。这个选项试图解决[未加密的 boot 分区](<../zh-cn/Dm-crypt/%E7%89%B9%E6%AE%8A%E5%BA%94%E7%94%A8.html#%E4%BF%9D%E6%8A%A4%E6%9C%AA%E5%8A%A0%E5%AF%86%E7%9A%84boot%E5%88%86%E5%8C%BA> "Dm-crypt/特殊应用")问题。 

**提示：**`/boot` **不需要** 专门放到一个单独的分区，它也可以就留在系统的根目录 `/` 下面。

**警告：** GRUB 2.12rc1 仅对 LUKS2 提供了有限的支持，详情请见[#LUKS2](<#LUKS2>)节。

要启用这个功能，使用 [LUKS](<../zh-cn/Dm-crypt.html> "Dm-crypt") 将 `/boot` 所在的分区加密，然后在 `/etc/default/grub` 中添加如下选项： 
    
    /etc/default/grub
    
    GRUB_ENABLE_CRYPTODISK=y

grub-install 使用这个选项来生成 `core.img`，所以在修改这个选项或加密分区之后要重新[安装 grub](<#%E5%AE%89%E8%A3%85>)。 

如果没有进一步的修改，你需要两次输入一个密码：第一次是为了让 GRUB 在启动伊始解锁 `/boot` 的挂载点，第二次是在 initramfs 的要求下解锁根文件系统。你可以用 [keyfile](<../zh-cn/Dm-crypt/Device_encryption.html#With_a_keyfile_embedded_in_the_initramfs> "Dm-crypt/Device encryption") 来避免密码输入过程。 

**警告：**

  * 如果你想要 [生成主配置文件](<#%E7%94%9F%E6%88%90%E4%B8%BB%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)，确保 `/boot` 已经挂载好了。
  * 为了进行与 `/boot` 的挂载点有关的系统更新，确保在进行更新之前已经对加密的 `/boot` 进行了解锁和挂载。如果使用了独立的 `/boot` 分区，这个可以通过使用 [crypttab](<../zh-cn/Dm-crypt/%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE.html#crypttab> "Crypttab") 和一个 [keyfile](<../zh-cn/Dm-crypt/Device_encryption.html#With_a_keyfile_embedded_in_the_initramfs> "Dm-crypt/Device encryption") 在启动的时候自动完成。

**注意：**

  * 如果你使用了特别的键盘映射，默认安装的 GRUB 是不知道的。这关系到如何输入密码来解锁 LUKS 块设备。请查阅 [GRUB/技巧和窍门#为早期启动手动配置核心映像](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html#%E4%B8%BA%E6%97%A9%E6%9C%9F%E5%90%AF%E5%8A%A8%E6%89%8B%E5%8A%A8%E9%85%8D%E7%BD%AE%E6%A0%B8%E5%BF%83%E6%98%A0%E5%83%8F> "GRUB/技巧和窍门")
  * 如果你遇到问题没法显示输入密码的界面（与 cryptouuid, cryptodisk相关的错误，或者 "device not found"），可以试着重新安装 GRUB，并在 `grub-install` 命令的尾部加上 `--modules="part_gpt part_msdos"`。

**提示：** 你可以使用 [pacman hooks](<https://bbs.archlinux.org/viewtopic.php?id=234607>) 来在升级时涉及到 `/boot` 中的文件的时候自动挂载它。

##### LUKS2

根据[#安装](<#%E5%AE%89%E8%A3%85>)一节的内容，使用`grub-install`创建支持LUKS的可引导GRUB镜像。请注意下面的事项： 

  * GRUB 2.06 添加了对 LUKS2 的初步支持，GRUB 2.12rc1 也只是部分解决了一些限制，参见 [GRUB bug #55093](<https://savannah.gnu.org/bugs/?55093>) 。
  * GRUB 2.12rc1 版本的`grub-install`可以创建一个解锁LUKS2的镜像。但是仅支持PBKDF2，不支持Argon2。
  * Argon2id (_cryptsetup_ 默认) 和 Argon2i PBKDFs是不支持的，仅支持 PBKDF2 。

**提示：** 你可以使用 [grub-improved-luks2-git](<https://aur.archlinux.org/packages/grub-improved-luks2-git/>)AUR ，该包为LUKS2和Argon支持打了补丁。但请注意该包的Argon支持需要UEFI系统。[[3]](<https://aur.archlinux.org/packages/grub-improved-luks2-git#comment-911119>)

**注意：** 早于 GRUB 2.12rc1 的版本需要配合一个定制GRUB配置文件，使用`grub-mkimage`手动创建一个EFI二进制文件。例如，通过`/boot/grub/grub-pre.cfg`调用`cryptomount`，`insmod normal`和`normal`。这在新版里不再需要，`grub-install` 已经足够了。但是从2.06版升级后，你可能需要至少运行`grub-mkconfig -o /boot/grub/grub.cfg`一次。

如果在启动过程中遇到密码无效（invalid passphrase）的提示并最后进入GRUB救急模式，尝试运行命令：`cryptomount -a`来挂载所有加密分区，或者使用`cryptomount -u $crypto_uuid`挂载指定分区，接下来和平常一样，运行`insmod normal` 和 `normal`。 

如果确定输入的密码正确，但密码输入后立刻返回密码无效（invalid passphrase）的错误，检查是否指定了正确的加密模块。使用`cryptsetup luksDump _/dev/nvme0n1p2_`检查 hash function（SHA-256， SHA-512）是否匹配镜像安装的模块（`gcry_sha256`， `gcry_sha512`），PBKDF算法是否为pbkdf2。可以使用 `cryptsetup luksConvertKey --hash _sha256_ --pbkdf pbkdf2 _/dev/nvme0n1p2_`更改加密分区的 hash 和 PBDKDF 算法。正常情况下，输入密码后需要花费几秒时间处理，而不是立刻返回结果。 

###  定制 grub.cfg

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 添加指导如何编写一个定制的 `/boot/grub/grub.cfg`。[User:Eschwartz/Grub](</wzh/index.php?title=User:Eschwartz/Grub&action=edit&redlink=1> "User:Eschwartz/Grub（页面不存在）") 中有一个草稿可以查阅。 (在 [Talk:GRUB#Manually generate grub.cfg](<../zh-cn/Talk:GRUB.html#Manually_generate_grub.cfg> "Talk:GRUB") 中讨论)

这一节讲述如何在 `/boot/grub/grub.cfg` 中手工创建 GRUB 启动条目，而非使用 grub-mkconfig。 

基础的 GRUB 配置文件使用如下的设置： 

  * `(hd _X_ ,_Y_)` 为磁盘 _X_ 上的分区 _Y_ ，分区编号从 1 开始，磁盘编号从 0 开始。
  * `set default=_N_` 为在用户选择时间内没有进行选择时的默认启动条目。
  * `set timeout=_M_` 即在使用默认条目启动前，等待用户自行选择的时间为 _M_ 秒。
  * `menuentry "title" {entry options}` 为一个标题为 `title` 的启动条目。
  * `set root=(hd _X_ ,_Y_)` 设置 `\boot` 分区，即内核和 GRUB 模块存储的位置。（`\boot` 不一定要位于一个独立的分区，可能是根分区(`/`) 下面的一个目录。）

#### LoaderDevicePartUUID

[GPT分区自动挂载](<../zh-cn/Systemd.html#GPT%E5%88%86%E5%8C%BA%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Systemd")使用的[systemd-gpt-auto-generator(8)](<https://man.archlinux.org/man/systemd-gpt-auto-generator.8>)需要`LoaderDevicePartUUID`UEFI变量以正常工作。要使GRUB设置该变量，在`grub.cfg`中加载`bli`模块： 
    
    if [ "$grub_platform" = "efi" ]; then
      insmod bli
    fi

####  启动菜单条目示例

**提示：** 在使用由 grub-mkconfig 所生成的 `/boot/grub/grub.cfg` 时，这些启动条目仍然是可以用的。将它们添加到 `/etc/grub.d/40_custom` 中然后[重新生成主配置文件](<#%E7%94%9F%E6%88%90%E4%B8%BB%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)，或者将它们添加到 `/boot/grub/custom.cfg`中。

若要管理多个 GRUB 条目，比如既使用 [linux](<https://archlinux.org/packages/?name=linux>)包 又使用 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 内核，相关的提示可以参见 [GRUB/技巧和窍门#多个启动条目](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html#%E5%A4%9A%E4%B8%AA%E5%90%AF%E5%8A%A8%E6%9D%A1%E7%9B%AE> "GRUB/技巧和窍门")。 

对于 [Archiso](<../zh-cn/Archiso.html> "Archiso") 和 [Archboot](<https://archboot.com>) 启动菜单条目，参见 [Multiboot USB drive#Boot entries](<../zh-cn/Multiboot_USB_drive.html#Boot_entries> "Multiboot USB drive"). 

#####  GRUB 命令

######  "关机" 菜单项
    
    menuentry "System shutdown" {
    	echo "System shutting down..."
    	halt
    }
    
######  "重启" 菜单项
    
    menuentry "System restart" {
    	echo "System rebooting..."
    	reboot
    }
    
######  "UEFI固件设置" 菜单项
    
    if [ ${grub_platform} == "efi" ]; then
    	menuentry 'UEFI Firmware Settings' --id 'uefi-firmware' {
    		fwsetup
    	}
    fi

#####  EFI 可执行文件

在启用了 UEFI 模式时，GRUB 可以 chainload 其它 EFI 可执行文件。 

**提示：** 如要让这些启动条目仅在 GRUB 处于 UEFI 模式的时候显示，只需把它们放到下面的 `if` 语句中： 
    
    if [ ${grub_platform} == "efi" ]; then
    	_放入仅 UEFI 显示的启动条目_
    fi

###### UEFI Shell

要启动 [UEFI Shell](<../zh-cn/Unified_Extensible_Firmware_Interface.html#UEFI_Shell> "Unified Extensible Firmware Interface")，你可以将它放在 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")的根目录里，然后添加如下菜单条目： 
    
    menuentry "UEFI Shell" {
    	insmod fat
    	insmod chain
    	search --no-floppy --set=root --file /shellx64.efi
    	chainloader /shellx64.efi
    }

###### gdisk

下载 [gdisk EFI application](<../zh-cn/GPT_fdisk.html#gdisk_EFI_application> "Gdisk") 然后复制 `gdisk_x64.efi` 到 `_esp_ /EFI/tools/`。 
    
    menuentry "gdisk" {
    	insmod fat
    	insmod chain
    	search --no-floppy --set=root --file /EFI/tools/gdisk_x64.efi
    	chainloader /EFI/tools/gdisk_x64.efi
    }

######  Chainload 一个统一的内核镜像

如果你有一个按照 [Secure Boot](<../zh-cn/Secure_Boot.html> "Secure Boot") 或者其他方法生成的 _.efi_ 文件，你可以把它添加到启动菜单里。例如： 
    
    menuentry "Arch Linux " {
    	insmod fat
    	insmod chain
    	search --no-floppy --set=root --fs-uuid _FILESYSTEM_UUID_
    	chainloader /EFI/Linux/arch-linux.efi
    }

#####  多系统启动

######  GNU/Linux

假设另一个发行版位于 `sda2`： 
    
    menuentry "Other Linux" {
    	set root=(hd0,2)
    	linux /boot/vmlinuz (add other options here as required)
    	initrd /boot/initrd.img (if the other kernel uses/needs one)
    }

或者让 GRUB 根据 UUID 或文件系统标签查找正确的分区： 
    
    menuentry "Other Linux" {
            # 假设 UUID 为 763A-9CB6
    	search --no-floppy --set=root --fs-uuid 763A-9CB6
    
            # 按照 label OTHER_LINUX 来搜索（确保分区 label 是精确的）
            #search --no-floppy --set=root --label OTHER_LINUX
    
    	linux /boot/vmlinuz （按需求在这里添加其他的选项，例如： root=UUID=763A-9CB6 ）
    	initrd /boot/initrd.img （如果其他的内核需要的话）
    }

如果其他发行版已经有一个有效的`/boot`文件夹，并安装了GRUB、`grub.cfg`、kernel和initramfs，可以指示GRUB在启动时即时加载这些其他`grub.cfg`文件。例如，对于`hd0`和第四个GPT分区： 
    
    menuentry "configfile hd0,gpt4"  {
        insmod part_gpt
        insmod btrfs
        insmod ext2
        set root='hd0,gpt4'
        configfile /boot/grub/grub.cfg
    }

选择此条目时，GRUB会从另一卷加载`grub.cfg`文件并显示该菜单。在`configfile`返回后，文件中的命令所做的任何环境变量改变将不会被保留。按`Esc`返回到第一个GRUB菜单。 

######  UEFI/GPT 模式下安装的 Windows

这个模式寻找 Windows 的启动加载器的位置，然后当用户选择了相应的菜单条目的时候，通过链式加载的方法在 GRUB 之后加载它。这里主要的任务是找到 EFI 系统分区然后从上面运行启动加载器。 

**注意：** 这个启动项仅在 UEFI 模式下才起作用，而且 Windows 和 UEFI 的位数必须相同。如果 GRUB 是 BIOS 模式，这个方法无效。参考 [Arch + Windows 双系统#Windows 在 UEFI 和 BIOS 上的限制](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html#Windows_%E5%9C%A8_UEFI_%E5%92%8C_BIOS_%E4%B8%8A%E7%9A%84%E9%99%90%E5%88%B6> "Arch + Windows 双系统") 和 [Arch + Windows 双系统#UEFI 和 BIOS 引导加载程序的限制](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html#UEFI_%E5%92%8C_BIOS_%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F%E7%9A%84%E9%99%90%E5%88%B6> "Arch + Windows 双系统")。 
    
    if [ "${grub_platform}" == "efi" ]; then
    	menuentry "Microsoft Windows Vista/7/8/8.1 UEFI/GPT" {
    		insmod part_gpt
    		insmod fat
    		insmod chain
    		search --no-floppy --fs-uuid --set=root $hints_string $fs_uuid
    		chainloader /EFI/Microsoft/Boot/bootmgfw.efi
    	}
    fi

其中 `$hints_string` 和 `$fs_uuid` 由下述两个命令得到。 

`$fs_uuid` 命令检测 EFI 系统分区的 UUID： 
    
    # grub-probe --target=fs_uuid _esp_ /EFI/Microsoft/Boot/bootmgfw.efi
    
    1ce5-7f28

或者你可以运行 `blkid --fs` 然后从结果中找到 EFI 系统分区的 UUID。 

`$hints_string` 命令可以确定 EFI 系统分区的位置，在当前的例子中是 harddrive 0： 
    
    # grub-probe --target=hints_string _esp_ /EFI/Microsoft/Boot/bootmgfw.efi
    
    --hint-bios=hd0,gpt1 --hint-efi=hd0,gpt1 --hint-baremetal=ahci0,gpt1

这两个命令都是假设 Windows 使用的 ESP 是挂载在`$esp`上的。当然，Windows的 EFI 文件路径可能有变,因为这就是Windows.... 

######  BIOS/MBR 模式下安装的 Windows

**注意：** GRUB 支持直接启动 `bootmgr`，如今启动 BIOS/MBR 模式下安装的 Windows 时不再需要[链式加载](<https://www.gnu.org/software/grub/manual/grub.html#Chain_002dloading>)分区启动扇区了。

**警告：**`bootmgr` 位于**系统分区**(**system partition**)，而不是 Windows 系统所在的分区（通常为 `C:` 盘）。系统分区的[文件系统标签](<../zh-cn/Persistent_block_device_naming.html#%E9%80%9A%E8%BF%87%E6%A0%87%E7%AD%BE> "Persistent block device naming") 是 `System Reserved` 或者 `SYSTEM` 而且这个分区的容量只有大概 100 到 549 MB。详情参考 [Wikipedia:System partition and boot partition](<https://en.wikipedia.org/wiki/System_partition_and_boot_partition> "wikipedia:System partition and boot partition")。

本节假设你的 Windows 分区是 `/dev/sda1`。如果分区不同，需要对每一处 `hd0,msdos1` 进行修改。 

**注意：** 这些菜单条目仅在 BIOS 启动模式下可用，不能在 UEFI 模式下安装的 GRUB 上使用。参考 [Arch + Windows 双系统#Windows 在 UEFI 和 BIOS 上的限制](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html#Windows_%E5%9C%A8_UEFI_%E5%92%8C_BIOS_%E4%B8%8A%E7%9A%84%E9%99%90%E5%88%B6> "Arch + Windows 双系统") 和 [Arch + Windows 双系统#UEFI 和 BIOS 引导加载程序的限制](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html#UEFI_%E5%92%8C_BIOS_%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F%E7%9A%84%E9%99%90%E5%88%B6> "Arch + Windows 双系统")。

在所有例子里，` _XXXX-XXXX_`是指文件系统的 UUID，可以通过 `lsblk --fs` 命令得到。 

对于 Windows Vista/7/8/8.1/10： 
    
    if [ "${grub_platform}" == "pc" ]; then
    	menuentry "Microsoft Windows Vista/7/8/8.1/10 BIOS/MBR" {
    		insmod part_msdos
    		insmod ntfs
    		insmod ntldr
    		search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 _XXXX-XXXX_
    		ntldr /bootmgr
    	}
    fi

对于 Windows XP： 
    
    if [ "${grub_platform}" == "pc" ]; then
    	menuentry "Microsoft Windows XP" {
    		insmod part_msdos
    		insmod ntfs
    		insmod ntldr
    		search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 _XXXX-XXXX_
    		ntldr /ntldr
    	}
    fi

**注意：** 在某些情况下，可能在安装 Windows 8 之前就已经安装了GRUB。启动 Windows 时可能会出现`\boot\bcd` 报错（错误代码为 `0xc000000f`）。要修复这个问题，可以进入 Windows Recovery Console（安装磁盘中的 `cmd.exe`）然后运行： 
    
    X:\> bootrec.exe /fixboot
    X:\> bootrec.exe /RebuildBcd
    
**不要** 使用 `bootrec.exe /Fixmbr`，因为那会将 GRUB 清除掉。或者你可以用 Troubleshooting 菜单里的 Boot Repair 函数，它不会清除 GRUB 而且可以修复大部分错误。而且最好是保证连接电脑的介质 **只有** 目标硬盘和你的可启动介质，如果你连接了其他的设备，Windows 很可能会没法修复启动信息。 

#####  使用标签

通过使用`search`的`--label`选项，可以使用人类易于阅读的文件系统标签。首先请[确保你的文件系统有唯一标签](<../zh-cn/Persistent_block_device_naming.html#by-label> "Persistent block device naming")； 

然后你就可以使用标签来添加一个条目： 
    
    menuentry "Arch Linux, session texte" {
      search --label --set=root archroot
      linux /boot/vmlinuz-linux root=/dev/disk/by-label/archroot ro
      initrd /boot/initramfs-linux.img
    }
    
##  使用 GRUB 命令行

MBR 太小，不足以存储所有的 GRUB 模块，所以 MBR 里面只有启动目录和一些很基本的命令。GRUB 的主要功能通过 `/boot/grub` 里的模块实现，按需加载。出现错误时，GRUB 可能不能引导启动（比如磁盘分区发生了变化）。这时候，一般会出现命令行界面。 

GRUB 不止提供一个 shell，如果 GRUB 不能读取到启动目录配置，但是能找到磁盘，你很可能会进入 "正常" shell： 
    
    grub>
    
如果有更严重的问题（比如 GRUB 找不到必须的文件了），GRUB 就可能会让你进入 "救急" shell： 
    
    grub rescue>
    
救急模式下的 shell 是正常 shell 的一个严格的子集，其支持的功能更少。如果不幸进入了救急模式的 shell 里，首先尝试加载 normal 模块，然后启动正常 shell： 
    
    grub rescue> set prefix=(hdX,Y)/boot/grub
    grub rescue> insmod (hdX,Y)/boot/grub/i386-pc/normal.mod
    rescue:grub> normal
    
###  分页支持

GRUB 支持对长输出进行分页（比如运行 `help` 的输出）。不过只能在正常 shell 中支持，在救急 shell 中则不支持。开启分页支持需要在 GRUB 命令行中键入： 
    
    sh:grub> set pager=1
    
###  使用命令行引导操作系统
    
    grub> 
    
可以使用 GRUB 命令行引导操作系统，一个典型的应用场景是通过“chainloading”来引导储存在一个驱动器或者分区中的 Windows 或 Linux 系统。 

ChainLoading 的意思是用当前的启动加载器去加载另一个启动加载器，所以叫做**链式** 加载。 

要被加载的另一个启动加载器可能嵌入在一个有分区表的磁盘的头部 (MBR)，或在一个未分区磁盘或者一个分区的头部 (VBR)，也可能在使用 UEFI 的情形下是一个 EFI 可执行文件。 

####  链式加载一个分区的 VBR
    
    set root=(hdX,Y)
    chainloader +1
    boot
    
X=0,1,2... Y=1,2,3... 

比如链式加载一个位于首磁盘,首分区上的 Windows： 
    
    set root=(hd0,1)
    chainloader +1
    boot
    
同样也可以使用 GRUB 链式加载另一个分区引导扇区上的 GRUB。 

####  链式加载磁盘的 MBR 或未分区磁盘的 VBR
    
    set root=hdX
    chainloader +1
    boot
    
####  链式加载 UEFI 模式下安装的 Windows/Linux
    
    insmod fat
    set root=(hd0,gpt4)
    chainloader (${root})/EFI/Microsoft/Boot/bootmgfw.efi
    boot
    
`insmod fat` 用来加载 FAT 文件系统模块，以访问 EFI 系统分区上的 Windows 启动加载器。 `(hd0,gpt4)` 或 `/dev/sda4` 是该示例中的 EFI 系统分区。 `chainloader` 一行中的条目用来指定需要被链式加载的 .efi 文件。 

####  正常加载

请参考[#使用救急控制台](<#%E4%BD%BF%E7%94%A8%E6%95%91%E6%80%A5%E6%8E%A7%E5%88%B6%E5%8F%B0>)中的例子。 

###  使用救急控制台

请先阅读[#使用 GRUB 命令行](<#%E4%BD%BF%E7%94%A8_GRUB_%E5%91%BD%E4%BB%A4%E8%A1%8C>)。如果无法进入正常的命令行，请尝试使用 Live CD 或者其他救急磁盘引导，然后修正配置错误，重新安装 GRUB。不过有些时候我们手上没有此类救急磁盘，这时救急控制台就可以派上用场了。 

GRUB 应急控制台里可用的命令有 `insmod`，`ls`，`set` 和 `unset`。这个例子里用了 `set` 和 `insmod`。`set` 用来修改变量，`insmod` 用来加载模块以添加功能。 

首先，用户必须知道启动分区 (`/boot`) 所在位置（是一个独立的分区或者是根目录下的子目录），然后设置： 
    
    grub rescue> set prefix=(hdX,Y)/boot/grub
    
其中 X 是物理驱动器的编号，而 Y 是分区的编号。 

**注意：** 如果启动分区是个独立的分区，要在路径中省略 `/boot`（例如键入 `set prefix=(hdX,Y)/grub`）。

通过加载 `linux` 模块来扩展命令行的功能： 
    
    grub rescue> insmod i386-pc/linux.mod
    
或者直接 
    
    grub rescue> insmod linux
    
这个模块会启动对我们熟悉的 `linux` 和 `initrd` 命令的支持。 

比如要启动 Arch Linux： 
    
    set root=(hd0,5)
    linux /boot/vmlinuz-linux root=/dev/sda5
    initrd /boot/initramfs-linux.img
    boot
    
如果 `/boot` 在单独分区上（例如在用 UEFI 的时候），适当地进行修改： 

**注意：** 因为 boot 是一个单独的分区而不是根分区的一部分，你得手动把它的地址写清楚，格式和前面的 prefix 一样。
    
    set root=(hd0,5)
    linux (hdX,Y)/vmlinuz-linux root=/dev/sda6
    initrd (hdX,Y)/initramfs-linux.img
    boot
    
**注意：** 如果你在执行 `linux` 命令的时候遇到了 `error: premature end of file /YOUR_KERNEL_NAME`，你可以尝试用 `linux16` 来替代。

成功启动 Arch Linux 后，用户可以修正 `grub.cfg` 然后重新安装 GRUB。 

为了完全修正错误和重新安装 GRUB，可能需要修改 `/dev/sda`。详情请参考[#安装](<#%E5%AE%89%E8%A3%85>)（BIOS）或者[#安装 2](<#%E5%AE%89%E8%A3%85_2>)（UEFI）章节。 

##  移除 GRUB

###  UEFI系统

删除 _grub_ 前，确保安装了其它启动加载器并配置其接管启动引导工作。 
    
    $ efibootmgr
    
    BootOrder: 0003,0001,0000,0002
    Boot0000* Windows Boot Manager  HD(2,GPT,4dabbedf-191b-4432-bc09-8bcbd1d7dabf,0x109000,0x32000)/File(\EFI\Microsoft\Boot\bootmgfw.efi)
    Boot0001* GRUB  HD(2,GPT,4dabbedf-191b-4432-bc09-8bcbd1d7dabf,0x109000,0x32000)/File(\EFI\GRUB\grubx64.efi)
    Boot0002* Linux-Firmware-Updater        HD(2,GPT,5dabbedf-191b-4432-bc09-8bcbd1d7dabf,0x109000,0x32000)/File(\EFI\arch\fwupdx64.efi)
    Boot0003* Linux Boot Manager    HD(2,GPT,4dabbedf-191b-4432-bc09-8bcbd1d7dabf,0x109000,0x32000)/File(\EFI\systemd\systemd-bootx64.efi)
    
如果`BootOrder`第一项是 _grub_ ，安装其它启动加载器并放在其前面（比如上面的[systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot")），然后 _grub_ 可以通过使用 _bootnum_ 删除： 
    
    # efibootmgr --delete-bootnum -b 1
    
再删除` _esp_ /EFI/grub` 和 `/boot/grub` 目录。 

###  BIOS系统

要将 _grub_ 替换为其它BIOS启动加载器，只需要安装该加载器，[MBR启动代码](<../zh-cn/%E5%88%86%E5%8C%BA.html#MBR%EF%BC%88%E5%BC%95%E5%AF%BC%E4%BB%A3%E7%A0%81%EF%BC%89> "分区")将会被覆盖。 

`grub-install`还创建了`/boot/grub`目录，需要手动删除。如果你还想再次安装 _grub_ ，可以保留该目录。 

在迁移到UEFI/GPT后，[使用dd移除MBR启动代码](</wzh/index.php?title=%E4%BD%BF%E7%94%A8dd%E7%A7%BB%E9%99%A4MBR%E5%90%AF%E5%8A%A8%E4%BB%A3%E7%A0%81&action=edit&redlink=1> "使用dd移除MBR启动代码（页面不存在）")（英语：[dd#Remove bootloader](<https://wiki.archlinux.org/title/dd#Remove_bootloader> "en:dd")）。 

##  疑难解答

###  os-prober 段错误

**提示：** 此问题已于 2:2.12.r260.gaae2ea61-1 被修复。

  * [archlinux/packaging/packages/grub#11](<https://gitlab.archlinux.org/archlinux/packaging/packages/grub/-/issues/11>)
  * [论坛主题](<https://bbs.archlinux.org/viewtopic.php?pid=2228660#p2228660>)

在将 [grub](<https://archlinux.org/packages/?name=grub>)包 升级到 _grub 2:2.12.r212.g4dc616657-2_ 后，运行 `grub-mkconfig` 时 [os-prober](<https://archlinux.org/packages/?name=os-prober>)包 会出现段错误。 

`grub-mkconfig` 的输出类似于： 
    
    Generating grub configuration file ...
    Warning: os-prober will be executed to detect other bootable partitions.
    Its output will be used to detect bootable binaries on them and create new boot entries.
    /usr/lib/os-probes/50mounted-tests: line 72: 164878 Segmentation fault      grub-mount "$partition" "$tmpmnt" 2> /dev/null
    Adding boot menu entry for UEFI Firmware Settings ...
    done
    
此时尝试进入 Windows 系统，会显示： 
    
    Setting partition type to 0x83
    error: invalid signature.
    
    Press any key to continue..._

这似乎是上游问题[[4]](<https://git.savannah.gnu.org/cgit/grub.git/commit/?id=067b6d225d482280abad03944f04e30abcbdafa1>)，同样的问题影响了 [archlinux/packaging/packages/grub#12](<https://gitlab.archlinux.org/archlinux/packaging/packages/grub/-/issues/12>)。已有部分用户提供了解决方案： 

####  降级 grub

将 [grub](<https://archlinux.org/packages/?name=grub>)包 [降级](<../zh-cn/%E9%99%8D%E7%BA%A7%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "降级软件包")至 _2:2.12-3_ 。 

####  自行编写启动条目

参照[#定制 grub.cfg](<#%E5%AE%9A%E5%88%B6_grub.cfg>) 一节自行编写启动条目。 

对于 BIOS/MBR 模式下安装的 Windows，使用[上文](<#BIOS/MBR_%E6%A8%A1%E5%BC%8F%E4%B8%8B%E5%AE%89%E8%A3%85%E7%9A%84_Windows>)提供的示例配置（使用 _search_ 关键字）很可能不奏效，对此，请使用以下配置： 
    
    menuentry "Microsoft Windows Vista/7/8/8.1/10 BIOS/MBR" {
        insmod part_msdos
        insmod ntfs
        set root=(hd _X_ ,msdos _Y_)
        chainloader +1
    }

###  不支持的文件系统

如果根目录分区是一个GRUB不支持的文件系统，那就需要为 `/boot` 单独分区，并使用一个支持的文件系统。某些情况下，GRUB 的开发版 [grub-git](<https://aur.archlinux.org/packages/grub-git/>)AUR 可能已经支持了那个文件系统。 

如果将 GRUB 和一个不支持的文件系统一起用，它将无法提取到你的驱动器的 [UUID](<../zh-cn/Persistent_block_device_naming.html#%E9%80%9A%E8%BF%87_uuid> "Persistent block device naming")，只能使用传统的名称 `/dev/_sdXx_` 来代替，而这个名称是可能会变化的。此时你可能需要手动编辑 `/boot/grub/grub.cfg`，将 `root=/dev/_sdXx_` 改为 `root=UUID=_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_`。你可以使用 `blkid` 命令来获取你的设备的 UUID ，参见 [Persistent block device naming](<../zh-cn/Persistent_block_device_naming.html> "Persistent block device naming")。 

尽管 GRUB 自2.0.4起支持 [F2FS](<../zh-cn/F2FS.html> "F2FS") 文件系统，GRUB还是不能从启用`extra_attr` flag 的 F2FS 分区正确读取引导文件。 

###  启用调试信息

**注意：** 每当你[#生成主配置文件](<#%E7%94%9F%E6%88%90%E4%B8%BB%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)的时候，这个设定就会被覆盖掉。

在 `grub.cfg` 中添加： 
    
    set pager=1
    set debug=all
    
###  出现 “msdos-style” 错误消息
    
    grub-setup: warn: This msdos-style partition label has no post-MBR gap; embedding will not be possible!
    grub-setup: warn: Embedding is not possible. GRUB can only be installed in this setup by using blocklists.
                However, blocklists are UNRELIABLE and its use is discouraged.
    grub-setup: error: If you really want blocklists, use --force.
    
这个错误可能当你在 VMware 容器里面安装 GRUB 的时候出现。请阅读[相关链接](<https://bbs.archlinux.org/viewtopic.php?pid=581760#p581760>)。这种情况是因为首分区直接从 MBR 后开始（即第 64 个扇区），而不是和正常的那样在 MBR 后面有 1MB（2048个扇区）的间隙。请参阅[#主引导记录 (MBR) 特殊操作](<#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95_\(MBR\)_%E7%89%B9%E6%AE%8A%E6%93%8D%E4%BD%9C>)。 

###  UEFI 异常

####  常见安装错误

  * 一些UEFI设备会遇到`Could not prepare Boot variable: Read-only file system`错误。请通过
        
        # mount -o remount,rw,nosuid,nodev,noexec --types efivarfs efivarfs /sys/firmware/efi/efivars

重新挂载`/sys/firmware/efi/efivars`开启读写权限，参见[Gentoo Wiki](<https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Bootloader#Install> "gentoo:Handbook:AMD64/Installation/Bootloader")。
  * 如果你在将 _sysfs_ 或者 _procfs_ 与 _grub-install_ 一起使用的时候，遇到要求你必须运行 `modprobe efivarfs` 的问题，尝试[使用上文的命令挂载efivarfs](<../zh-cn/Unified_Extensible_Firmware_Interface.html#%E6%8C%82%E8%BD%BD_efivarfs> "Unified Extensible Firmware Interface")
  * 如果不用 `--target` 或者 `--directory` 选项，grub-install 不知道应该安装哪一个固件。此时 `grub-install` 会输出 `source_dir does not exist. Please specify --target or --directory`。
  * 如果在运行 grub-install 以后，被告知`error: _esp_ doesn't look like an EFI partition`，那这个分区很可能不是[FAT32](<../zh-cn/FAT.html> "FAT32")格式。

####  在固件启动管理器中创建一个GRUB条目

`grub-install`会自动尝试在启动管理器中创建一个菜单项。如果没有，请参见[UEFI#efibootmgr](<../zh-cn/UEFI.html#efibootmgr> "UEFI")，了解使用`efibootmgr`来创建菜单项的说明。问题也可能在于你没有以UEFI模式启动CD/USB，参见[UEFI#Create UEFI bootable USB from ISO](<../zh-cn/UEFI.html#Create_UEFI_bootable_USB_from_ISO> "UEFI")。 

另一种在固件引导管理器中创建GRUB条目的方法是使用`efibootmgr -c`，这个命令默认 `/dev/sda1` 是EFI系统分区，并且挂载到了`/boot/efi`，这也是`efibootmgr`的默认行为。该命令在引导选项表顶部创建了一个名为“Linux”的启动项目，传递其它参数可调整默认行为。生成的OS引导器位于`\EFI\arch\grub.efi`。 

####  启动时进入了救急控制台

如果 GRUB 直接就启动到了救急控制台下，而且没报错，这可能是因为如下两种原因： 

  * 可能是因为 `grub.cfg` 丢失或者位置不对。如果 GRUB UEFI 安装时设定了 `--boot-directory` 参数，而 `grub.cfg` 文件却不在那里，就会发生这样的问题。
  * 如果启动分区的分区号发生了变化（这个分区号会被直接编码到 `grubx64.efi` 文件中），也会出现这个问题。

####  GRUB UEFI 无法加载

下面是一个正常的 UEFI 的示例： 
    
    # efibootmgr -u
    
    BootCurrent: 0000
    Timeout: 3 seconds
    BootOrder: 0000,0001,0002
    Boot0000* GRUB HD(1,800,32000,23532fbb-1bfa-4e46-851a-b494bfe9478c)File(\EFI\GRUB\grubx64.efi)
    Boot0001* Shell HD(1,800,32000,23532fbb-1bfa-4e46-851a-b494bfe9478c)File(\shellx64.efi)
    Boot0002* Festplatte BIOS(2,0,00)P0: SAMSUNG HD204UI
    
如果启动后，屏幕直接变黑，几秒后就跳到了下一个启动项，根据[相关链接](<https://bbs.archlinux.org/viewtopic.php?pid=981560#p981560>)的说法是，将 GRUB 移动到 root 分区上可能会解决这个问题。必须先删除启动项，然后在移动 GRUB 后重建。操作之后上述命令的输出中，GRUB 条目应该像这样： 
    
    Boot0000* GRUB HD(1,800,32000,23532fbb-1bfa-4e46-851a-b494bfe9478c)File(\grubx64.efi)
    
####  缺省/后备启动路径

一些 UEFI 固件在显示 UEFI NVRAM 启动条目之前，需要在一个已知的位置上有一个可启动文件。如果是这种情况， `grub-install` 会说明 `efibootmgr` 添加了一个启动 GRUB 的条目，但这个条目不会在 VisualBIOS 启动顺序选择器中显示。解决方法是把 GRUB 安装到缺省/后备启动路径当中： 
    
    # grub-install --target=x86_64-efi --efi-directory=_esp_ **--removable**
    
或者你可以把已经安装好的 GRUB EFI 执行文件移动到缺省/后备路径中： 
    
    # mv _esp_ /EFI/grub _esp_ /EFI/BOOT
    # mv _esp_ /EFI/BOOT/grubx64.efi _esp_ /EFI/BOOT/BOOTX64.EFI
    
###  "Invalid signature"（无效签名错误）

如果在启动 Windows 时出现了 "invalid signature" 错误（比如在重新分区或者添加了新硬盘后），删除 GRUB 的设备配置，然后让它重建一个： 
    
    # mv /boot/grub/device.map /boot/grub/device.map-old
    # grub-mkconfig -o /boot/grub/grub.cfg
    
`grub-mkconfig` 此时就应该生成了新的启动项了，包括 Windows。确认能启动成功后，再将备份文件 `/boot/grub/device.map-old` 删除。 

###  引导过程卡死

如果在 GRUB 加载内核并初始化 ramdisk 后引导过程卡死了，又没有错误信息的话，请尝试移除 `add_efi_memmap` 这个内核参数。 

###  其他系统不能自动发现 Arch Linux

有人发现有些发行版不能使用 `os-prober` 自动发现 Arch Linux。据说如果 `/etc/lsb-release` 文件存在的话，可以提高探测能力。这个文件和和更新工具可以在 [lsb-release](<https://archlinux.org/packages/?name=lsb-release>)包 包中找到。 

###  在 chroot 环境下安装时遇到警告

当位于 chroot 环境里，要在 LVM 系统上安装 GRUB 的时候（比如在安装系统的时候），你可能会收到一个这样的警告： 
    
    /run/lvm/lvmetad.socket: connect failed: No such file or directory
    
或者 
    
    WARNING: failed to connect to lvmetad: No such file or directory. Falling back to internal scanning.
    
这是因为在 chroot 环境里面 `/run` 是不可用的。只要每个步骤都做对了，这些警告不会影响系统启动，你可以放心继续进行下一步的系统安装。 

###  GRUB 加载非常慢

当磁盘空间很小的时候 GRUB 的加载时间可能会很长。如果你遇到了这样的问题，检查一下你的 `/boot` 或者 `/` 分区是不是有足够的剩余空间。 

###  error: unknown filesystem（未知文件系统错误）

因某些原因，GRUB 可能会不能启动并输出 `error: unknown filesystem`。如果你确定所有的 [UUID](<../zh-cn/Persistent_block_device_naming.html#%E9%80%9A%E8%BF%87_uuid> "Persistent block device naming") 都对了而且所有的文件系统都是有效而且被 GRUB 支持的，问题的原因可能是你的 [BIOS 启动分区](<#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8_\(GPT\)_%E7%89%B9%E6%AE%8A%E6%93%8D%E4%BD%9C>)不在驱动器的前 2 TB 空间里 [[5]](<https://bbs.archlinux.org/viewtopic.php?id=195948>)。 选择一个分区工具调整这个分区，让它完全在前 2 TB 空间中，然后重新安装和配置 GRUB。 

这个错误也可能是因为一个 [ext4](<../zh-cn/Ext4.html> "Ext4") 文件系统拥有 GRUB 不支持的特性： 

  * `large_dir` \- 不被支持。
  * `metadata_csum_seed` \- GRUB 2.11 将会支持([commit](<https://git.savannah.gnu.org/cgit/grub.git/commit/?id=7fd5feff97c4b1f446f8fcf6d37aca0c64e7c763>))。

**警告：** 当你在`/boot`中启用文件系统特性时，请确保grub支持你的 [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统") 特性。

###  grub-reboot 不能重新设定

GRUB 好像不能写入 Btrfs 格式的根分区[[6]](<https://bbs.archlinux.org/viewtopic.php?id=166131>)。如果你使用 grub-reboot 来启动到另一个启动条目，就会没法更新其 on-disk 环境。要么换一个启动条目来运行 grub-reboot（例如在不同发行版之间切换的时候），要么考虑换个文件系统。你可以通过运行 `grub-editenv create` 来重设一个 "sticky" 条目，然后在 `/etc/default/grub` 中设置 `GRUB_DEFAULT=0`（不要忘了运行 `grub-mkconfig -o /boot/grub/grub.cfg`）。 

###  不能在旧的 Btrfs 上进行安装

如果一个驱动器在没有创建分区表的情形下被格式化成 BTRFS（比如 /dev/sdx)，之后又创建了一个分区表，那么会有部分 Btrfs 格式保留下来。大部分功能和操作系统都不会注意这个，但是 GRUB 则无法安装，即使使用 --force 参数也不行。 
    
    # grub-install: warning: Attempting to install GRUB to a disk with multiple partition labels. This is not supported yet..
    # grub-install: error: filesystem `btrfs' does not support blocklists.
    
你可以把整个驱动器置零来解决问题，但还有一个办法既简单又能保留你的数据，那就是用 `wipefs -o 0x10040 /dev/sdx` 命令来擦掉 Btrfs superblock。 

###  未找到 Windows 8/10

Windows 8/10 如果启用了 "Hiberboot", "Hybrid Boot" 或 "Fast Boot"，可能会导致 Windows 分区无法被挂载。所以 `grub-mkconfig` 无法找到安装的 Windows。在 Windows 里禁用 Hiberboot，然后它就可以被添加到 GRUB 菜单了。 

###  GRUB 救急与加密启动

在使用加密启动，而你没法键入正确的密码的时候，就会进入 GRUB 救急命令行。 

这个救急命令行只有有限的功能，可以使用下面的命令来完成启动： 
    
    grub rescue> cryptomount <分区>
    grub rescue> insmod normal
    grub rescue> normal
    
更好的介绍参见[这个帖子](<https://blog.stigok.com/2017/12/30/decrypt-and-mount-luks-disk-from-grub-rescue-mode.html>)。 

###  GRUB 已安装但引导过程没有显示菜单

检查`/etc/default/grub`中的`GRUB_TIMEOUT` 是否设置成了`0`，设置为一个正数来调整GRUB条目加载前的等待时间，按秒计时。另外要检查`GRUB_TIMEOUT_STYLE`是否为`hidden`，设置为`menu`确保菜单显示。[重新生成主配置文件](<#%E7%94%9F%E6%88%90%E4%B8%BB%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)后，重启检查设置是否生效。 

如果仍然没有解决问题，可能存在图形终端的兼容问题。设置`/etc/default/grub`中的`GRUB_TERMINAL_OUTPUT`为`console`关闭GRUB图形终端。 

###  在旧的 Lenovo 设备上安装好 GRUB 后依然有“ERROR CODE 1962 - No operating system found”的错误消息

参见[这个链接](<https://www.reddit.com/r/ManjaroLinux/comments/e682d6/fixing_lenovos_error_code_1962_by_spoofing_the/>)。 

##  参阅

  * [Wikipedia:GNU GRUB](<https://en.wikipedia.org/wiki/GNU_GRUB> "wikipedia:GNU GRUB")
  * [官方 GRUB 手册](<https://www.gnu.org/software/grub/manual/grub.html>)
  * [GRUB 的 Ubuntu wiki 页面](<https://help.ubuntu.com/community/Grub2>)
  * [描述为 UEFI 系统编译的 GRUB wiki 页面](<https://help.ubuntu.com/community/UEFIBooting>)
  * [Wikipedia:BIOS Boot partition](<https://en.wikipedia.org/wiki/BIOS_Boot_partition> "wikipedia:BIOS Boot partition")
  * [怎样配置 GRUB](<https://web.archive.org/web/20160424042444/http://members.iinet.net/~herman546/p20/GRUB2%20Configuration%20File%20Commands.html#Editing_etcgrub.d05_debian_theme>)
