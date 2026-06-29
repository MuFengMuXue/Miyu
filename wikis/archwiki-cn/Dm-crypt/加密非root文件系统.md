**翻译状态：**

  * 本文（或部分内容）译自 [Dm-crypt/Encrypting a non-root file system](<https://wiki.archlinux.org/title/Dm-crypt/Encrypting_a_non-root_file_system> "arch:Dm-crypt/Encrypting a non-root file system")，最近一次同步于 2025-07-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dm-crypt/Encrypting_a_non-root_file_system?diff=0&oldid=841239>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dm-crypt_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Encrypting_a_non-root_file_system_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

以下是一些用 dm-crypt 加密辅助（secondary）文件系统（即，非根文件系统）的例子。 

##  总览

加密辅助文件系统不会对操作系统、程序文件进行加密，因此通常只用于单独保护敏感数据。对于USB驱动器等外部介质，进行加密可确保在不同计算机上使用时，数据安全不受威胁。此外，也可按照数据访问人员将数据分类，分别使用不同的密钥加密。 

dm-crypt 是[块级别加密](<../../zh-cn/%E9%9D%99%E6%80%81%E6%95%B0%E6%8D%AE%E5%8A%A0%E5%AF%86.html#%E5%9D%97%E8%AE%BE%E5%A4%87%E5%8A%A0%E5%AF%86> "静态数据加密")层，其将加密整个块设备（例如，[分区](<#%E5%88%86%E5%8C%BA>)和[回环设备](<#%E6%96%87%E4%BB%B6%E5%AE%B9%E5%99%A8>)）。 

若要加密单个文件，需要使用文件系统层级的加密。例如使用[eCryptfs](</wzh/index.php?title=ECryptfs&action=edit&redlink=1> "ECryptfs（页面不存在）") 或 [EncFS](</wzh/index.php?title=EncFS&action=edit&redlink=1> "EncFS（页面不存在）")。有关保护隐私数据的更多信息，参见[静态数据加密](<../../zh-cn/%E9%9D%99%E6%80%81%E6%95%B0%E6%8D%AE%E5%8A%A0%E5%AF%86.html> "静态数据加密")。 

##  分区

本例介绍的是对 `/home` 分区的加密，但相关方法也可以应用到其它包含用户数据的非根分区。 

**提示：** 可以为每个用户的`/home`目录单独分配一个分区，也可以所有用户的`/home`目录共享一个分区。

下文假定用于`/home`目录的[分区已经创建](<../../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")。若该分区曾用于其它用途，因而包含了数据，可能需要[使用dm-crypt专用方案安全擦除分区](<../../zh-cn/Dm-crypt/%E5%87%86%E5%A4%87%E7%A3%81%E7%9B%98.html#dm-crypt_%E4%B8%93%E7%94%A8%E6%96%B9%E6%A1%88> "Dm-crypt/准备磁盘")。注意，只擦除一个分区，而不擦除整个磁盘，可能仍会泄露一些数据。 

建立 LUKS 头： 
    
    # cryptsetup _options_ luksFormat _device_
    
`_device_`应对应已创建的分区。` _options_`的取值参见[Dm-crypt/设备加密#LUKS_模式的加密选项](<../../zh-cn/Dm-crypt/%E8%AE%BE%E5%A4%87%E5%8A%A0%E5%AF%86.html#LUKS_%E6%A8%A1%E5%BC%8F%E7%9A%84%E5%8A%A0%E5%AF%86%E9%80%89%E9%A1%B9> "Dm-crypt/设备加密")。 

使用设备映射器对设备进行解密，以对加密的分区进行操作： 
    
    # cryptsetup open _device_ _name_
    
分区解密之后，会被映射成块设备 `/dev/mapper/_name_`。之后，建立[文件系统](<../../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")： 
    
    # mkfs._fstype_ /dev/mapper/_name_
    
若所有用户共享`/home`目录，则可将创建好的文件系统挂载到`/home`；若该文件系统是某个用户专用的，则挂载到`/home/_username_`。参见 [#手动挂载和卸载](<#%E6%89%8B%E5%8A%A8%E6%8C%82%E8%BD%BD%E5%92%8C%E5%8D%B8%E8%BD%BD>)。 

**提示：** 卸载并再挂载一次文件系统，可确定映射有无问题。

###  手动挂载和卸载

挂载分区： 
    
    # cryptsetup open _device_ _name_
    # mount /dev/mapper/_name_ /mnt/home
    
卸载： 
    
    # umount /mnt/home
    # cryptsetup close _name_
    
**提示：**[GVFS](<../../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html#%E6%8C%82%E8%BD%BD> "GVFS") 也可以挂载加密的分区。若使用支持 gvfs 的文件管理器（例如，[Thunar](<../../zh-cn/Thunar.html> "Thunar")）挂载加密分区，则会弹出密码输入框。对于其他桌面环境，可使用[zulucrypt](<https://aur.archlinux.org/packages/zulucrypt/>)AUR进行图形化挂载。

###  自动解锁并挂载

有三种不同方法来自动化解锁分区并挂载文件系统。 

####  启动时解锁

配置 `/etc/crypttab` 文件，systemd会在系统启动过程中自动解析该文件，并以此解密相应设备。若要挂载所有用户共用的home分区，或要自动挂载其它加密的块设备，推荐使用本方法。 

可参考[Dm-crypt/系统配置#crypttab](<../../zh-cn/Dm-crypt/%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE.html#crypttab> "Dm-crypt/系统配置")。此外，[Dm-crypt/系统配置#在启动时挂载](<../../zh-cn/Dm-crypt/%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE.html#%E5%9C%A8%E5%90%AF%E5%8A%A8%E6%97%B6%E6%8C%82%E8%BD%BD> "Dm-crypt/系统配置")中提供了示例配置。 

####  用户登录时解锁

  * 使用[pam_exec](</wzh/index.php?title=Pam_exec&action=edit&redlink=1> "Pam exec（页面不存在）")：若需要为每个用户挂载单独的加密home分区，推荐使用该方式。
  * 使用[pam_mount](</wzh/index.php?title=Pam_mount&action=edit&redlink=1> "Pam mount（页面不存在）")。

##  文件容器

Cryptsetup 对设备进行操作。因此，若要使用文件容器，需要配置回环设备。好在，在后台，cryptsetup可自动管理回环设备(请见 [Gentoo:Custom_Initramfs#Encrypted_keyfile](<https://wiki.gentoo.org/wiki/Custom_Initramfs#Encrypted_keyfile> "gentoo:Custom Initramfs"))，无需手动调用 `losetup`。 

首先，使用恰当的[随机数生成器](<../../zh-cn/%E9%9A%8F%E6%9C%BA%E6%95%B0%E7%94%9F%E6%88%90.html> "随机数生成")用 [dd](<../../zh-cn/Dd.html> "Dd") 创建一个加密容器： 
    
    $ dd if=/dev/urandom of=bigsecret.img bs=100M count=1 iflag=fullblock
    
这会创建大小为 100 MiB 的 `bigsecret.img` 文件。 

注意，不要遗漏`iflag=fullblock`选项。否则，可能出现“部分读”问题。详见[Dd#部分读取：复制的数据量小于要求的大小](<../../zh-cn/Dd.html#%E9%83%A8%E5%88%86%E8%AF%BB%E5%8F%96%EF%BC%9A%E5%A4%8D%E5%88%B6%E7%9A%84%E6%95%B0%E6%8D%AE%E9%87%8F%E5%B0%8F%E4%BA%8E%E8%A6%81%E6%B1%82%E7%9A%84%E5%A4%A7%E5%B0%8F> "Dd")。 

要避免之后[调整](<../../zh-cn/Dm-crypt/Device_encryption.html#Loopback_file_system> "Dm-crypt/Device encryption")容器大小的麻烦，在创建文件容器时，确保其大小大于要加密的文件的总大小、文件系统内部数据/元数据开销和LUKS头的总和。若使用LUKS，则仅其元数据就可能需要多达16MiB的空间。创建一个小于 LUKS头（16MiB）大小的文件容器会在打开设备时报错`Requested offset is beyond real size of device bigsecret.img`。 

之后的操作和[#分区](<#%E5%88%86%E5%8C%BA>)中的相同，但要将 `device` 替换为 `bigsecret.img`。 

cryptsetup 会自动寻找可用的回环设备设备并将文件附加到设备上。在卸载之后，文件容器应该相应地关闭，cryptsetup之后会分离使用的回环设备。 

**提示：** 使用dm-crypt加密容器非常灵活。可查看[Tomb](<../../zh-cn/Tomb.html> "Tomb")的功能和文档详细了解。[Tomb](<../../zh-cn/Tomb.html> "Tomb")提供了一系列dm-crypt脚本，以便快速灵活地处理加解密操作。

###  使用 losetup 手动挂载和卸载

首先，查找未使用的回环设备： 
    
    # losetup --find
    
然后，将文件容器附加到回环设备，例如，要附加到`loop0`： 
    
    # losetup /dev/loop0 bigsecret.img
    
**注意：** 如果出现`/dev/loop0: No such file or directory`错误，需要先以 root 用户执行命令`modprobe loop`以加载内核模块。较新的内核中（内核版本3.2及更高），回环设备是按需创建的。可通过以 root 用户执行 `losetup -f` 命令请求创建新的回环设备。

之后，按照常规方式进行cryptsetup设置即可： 
    
    # cryptsetup open /dev/loop0 secret
    # mount -t ext4 /dev/mapper/secret /mnt/secret
    
卸载容器时，需要以相反的顺序执行对应的操作： 
    
     # umount /mnt/secret
     # cryptsetup close secret
    
若要分离使用的回环设备: 
    
     # losetup --detach /dev/loop0
    