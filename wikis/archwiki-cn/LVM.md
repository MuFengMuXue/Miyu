**翻译状态：**

  * 本文（或部分内容）译自 [LVM](<https://wiki.archlinux.org/title/LVM> "arch:LVM")，最近一次同步于 2019-07-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/LVM?diff=0&oldid=570838>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/LVM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Install Arch Linux on LVM](</wzh/index.php?title=Install_Arch_Linux_on_LVM&action=edit&redlink=1> "Install Arch Linux on LVM（页面不存在）")
  * [LVM on software RAID](</wzh/index.php?title=LVM_on_software_RAID&action=edit&redlink=1> "LVM on software RAID（页面不存在）")
  * [dm-crypt/Encrypting an entire system#LVM on LUKS](</wzh/index.php?title=Dm-crypt/Encrypting_an_entire_system&action=edit&redlink=1> "Dm-crypt/Encrypting an entire system（页面不存在）")
  * [dm-crypt/Encrypting an entire system#LUKS on LVM](</wzh/index.php?title=Dm-crypt/Encrypting_an_entire_system&action=edit&redlink=1> "Dm-crypt/Encrypting an entire system（页面不存在）")
  * [Resizing LVM-on-LUKS](</wzh/index.php?title=Resizing_LVM-on-LUKS&action=edit&redlink=1> "Resizing LVM-on-LUKS（页面不存在）")

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 本文没有涵盖关于 [精简配置](<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_logical_volumes/assembly_thinly-provisioned-logical-volumes_configuring-and-managing-logical-volumes>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-19 ⓘ]的内容。您可以同时在 [此处](<https://wiki.gentoo.org/wiki/LVM#Thin_provisioning>)找到更全面的解释。 (在 [Talk:LVM#Logical volume types](</wzh/index.php?title=Talk:LVM&action=edit&redlink=1> "Talk:LVM（页面不存在）") 中讨论)

引用 [Wikipedia:Logical Volume Manager (Linux)](<https://en.wikipedia.org/wiki/Logical_Volume_Manager_\(Linux\)> "wikipedia:Logical Volume Manager \(Linux\)") 的解释： 

    LVM 是一种可用在 [Linux 内核](<https://en.wikipedia.org/wiki/Linux_kernel> "wikipedia:Linux kernel")的[逻辑分卷管理器](<https://en.wikipedia.org/wiki/logical_volume_management> "wikipedia:logical volume management")；可用于管理磁盘驱动器或其他类似的大容量存储设备。

##  LVM基本组成

LVM利用Linux内核的[device-mapper](<http://sources.redhat.com/dm/>)功能来实现存储系统的虚拟化（系统分区独立于底层硬件）。 通过LVM，你可以实现存储空间的抽象化并在上面建立虚拟分区（virtual partitions），可以更简便地扩大和缩小分区，可以增删分区时无需担心某个硬盘上没有足够的连续空间，避免为正在使用的磁盘重新分区的麻烦、为调整分区而不得不移动其他分区的不便。 

LVM的基本组成部分如下： 

物理卷 (PV)
    一个可供存储LVM的块设备. 例如: 一块硬盘, 一个MBR或GPT[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning"), 一个回环文件, 一个被内核映射的设备 (例如 [dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt")).它包含一个特殊的LVM头。
卷组 (VG)
    物理卷的一个组，作为存放逻辑卷的容器。 PEs are allocated from a VG for a LV.
逻辑卷 (LV)
    "虚拟/逻辑卷"存放在一个卷组中并由物理块组成。是一个类似于物理设备的块设备，例如，你可以直接在它上面创建一个文件系统[文件系统](<../zh-cn/File_systems.html> "File systems")。
物理块 (PE)
    一个卷组中最小的连续区域(默认为4 MiB)，多个物理块将被分配给一个逻辑卷。你可以把它看成物理卷的一部分，这部分可以被分配给一个逻辑卷。

示例: 
    
     '''物理硬盘'''
                     
       硬盘1 (/dev/sda):
          _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
         |分区1 50GB (物理卷)           |分区2 80GB (物理卷)            |
         |/dev/sda1                    |/dev/sda2                     |
         |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _ _ _ _ _ __|
                                       
       硬盘2 (/dev/sdb):
          _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
         |分区1 120GB (物理卷)                         |
         |/dev/sdb1                                   |
         | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
    
     '''LVM逻辑卷'''
     
       卷组（Volume Group1） (/dev/MyVolGroup/ = /dev/sda1 + /dev/sda2 + /dev/sdb1):
          _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ 
         |逻辑卷1 15GB                  |逻辑卷2 35GB                        |逻辑卷3 200GB                         |
         |/dev/MyVolGroup/rootvol        |/dev/MyVolGroup/homevol             |/dev/MyVolGroup/mediavol              |
         |_ _ _ _ _ _ _ _ _ _ _ _ _ _ __|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
    
##  优点

比起普通的硬盘分区管理方式，LVM更富于灵活性： 

  * 将多块硬盘看作一块大硬盘
  * 使用逻辑卷（LV），可以创建跨越众多硬盘空间的分区。
  * 可以创建小的逻辑卷（LV），在空间不足时再动态调整它的大小。
  * 在调整逻辑卷（LV）大小时可以不用考虑逻辑卷在硬盘上的位置，不用担心没有可用的连续空间。
  * 可以在线（online）对逻辑卷（LV）和卷组（VG）进行创建、删除、调整大小等操作。不过LVM上的文件系统也需要重新调整大小，好在某些文件系统（例如ext4）也支持在线操作。
  * 无需重新启动服务，就可以将服务中用到的逻辑卷（LV）在线（online）/动态（live）迁移至别的硬盘上。
  * 允许创建快照，可以保存文件系统的备份，同时使服务的下线时间（downtime）降低到最小。
  * 支持各种设备映射目标（device-mapper targets），包括透明文件系统加密和缓存常用数据（caching of frequently used data）。这将允许你创建一个包含一个或多个磁盘、并用LUKS加密的系统，使用[LVM on top](</wzh/index.php?title=Dm-crypt/Encrypting_an_entire_system&action=edit&redlink=1> "Dm-crypt/Encrypting an entire system（页面不存在）") 可轻松地管理和调整这些独立的加密卷 （例如. `/`, `/home`, `/backup`等) 并免去开机时多次输入密钥的麻烦。

##  缺点

  * 在系统设置时需要更复杂的额外步骤。
  * Windows系统并不支持LVM，若使用双系统，你将无法在Windows上访问LVM分区。

##  准备

确保已安装[lvm2](<https://archlinux.org/packages/?name=lvm2>)包包。 

##  在LVM上安装Arch Linux

你应该在[安装过程](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")中的的[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning")和[创建文件系统](<../zh-cn/File_systems.html#%E5%88%9B%E5%BB%BA%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "File systems")这一步中创建LVM卷。不要直接格式化一个分区作为你的根文件系统（/），而应将其创建在一个逻辑卷（LV）中。 

快速导览： 

  * 创建物理卷（PV）所在的[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning")。
  * 创建物理卷（PV）。如果你只有一个硬盘，那么你最好只创建一个分区一个物理卷；如果你有多个硬盘，你可以创建多个分区，在每个分区上分别创建一个物理卷。
  * 创建卷组（VG），并把所有物理卷加进卷组。
  * 在卷组（VG）上创建逻辑卷（LV）。
  * 继续[安装指南](<../zh-cn/Installation_guide.html#%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%88%86%E5%8C%BA> "Installation guide")中的格式化分区步骤。
  * 当你做到安装指南中的“Initramfs”步骤时，把 `lvm2`加入到 `mkinitcpio.conf`文件中（请参考下文）。

**警告：** 若你使用不支持LVM的引导程序，`/boot`不能置于LVM中。你必须创建一个独立的`/boot`分区并直接格式化它。已知支持LVM的引导程序只有[GRUB](<../zh-cn/GRUB.html> "GRUB")。

###  创建分区

在继续配置LVM前，必须对设备进行[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning")。 

创建分区： 

  * 若使用MBR,设置[分区类型](<https://en.wikipedia.org/wiki/Partition_type> "wikipedia:Partition type")为`8e` (在"fdisk"中为`Linux LVM`).
  * 若使用GPT, 设置[分区类型](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs> "wikipedia:GUID Partition Table")为`E6D6D379-F507-44C2-A23C-238F2A3DF928` (在"fdisk"中为`Linux LVM`；在"gdisk"中为`8e00`).

###  创建物理卷（PV）

可通过以下命令列出可被用作物理卷的设备： 
    
    # lvmdiskscan
    
**警告：** 请确认你对正确的设备进行操作，否则会导致文件丢失！

在列出的设备上创建物理卷： 
    
     # pvcreate _DEVICE_
    
该命令在各个设备上创建LVM头。如[#LVM基本组成](<#LVM%E5%9F%BA%E6%9C%AC%E7%BB%84%E6%88%90>)所示, _DEVICE_ 可以是磁盘（如`/dev/sda`），分区（如`/dev/sda2`）或环回设备。例如： 
    
    # pvcreate /dev/sda2
    
你可以用以下命令查看已创建好的物理卷： 
    
    # pvdisplay
    
**注意：** 如果你用的是未格式化过且擦除块（erase block）大小小于1M的SSD，请采用以下命令`pvcreate --dataalignment 1m /dev/sda`来设置对齐（alignment），可以参考[链接（英文）](<https://serverfault.com/questions/356534/ssd-erase-block-size-lvm-pv-on-raw-device-alignment>)

###  创建卷组（VG）

创建完成物理卷（PV）之后，下一步就是在该物理卷创建卷组（VG）了。 首先必须先在其中一个物理卷（PV）创建一个卷组： 
    
    # vgcreate <_volume_group_ > <_physical_volume_ >
    
可用作字符卷组的名称可在[lvm(8)](<https://man.archlinux.org/man/lvm.8>)中查到。 

例如： 
    
    # vgcreate VolGroup00 /dev/sda2
    
然后让该卷组扩大到其他所有的物理卷: 
    
    # vgextend <_卷组名_ > <_物理卷_ >
    # vgextend <_卷组名_ > <_其它物理卷_ >
    # ...
    
例如： 
    
    # vgextend VolGroup00 /dev/sdb1
    # vgextend VolGroup00 /dev/sdc
    
其中，“VolGroup00”名字换成你自己起的名字即可。 接下来可以用以下命令查看卷组： 
    
    # vgdisplay
    
**注意：** 你可以创建多个的卷组，但这将使你的硬盘空间分布在不同（逻辑）磁盘上。

###  一步创建卷组

LVM支持将卷组与物理卷的创建聚合在一个命令中。例如，为了在前文提到的三个设备中创建名为VolGroup00的卷组，可以执行如下命令： 
    
    # vgcreate VolGroup00 /dev/sda2 /dev/sdb1 /dev/sdc
    
该命令首先会在分区上创建物理卷（如果之前没有创建过），再创建一个包含三个物理卷的卷组。如果设备上已经存在文件系统，命令会提出警告。 

###  创建逻辑卷（LV）

**提示：** 若想在LVM上使用快照, 逻辑卷缓存（logical volume caching）, thin provisioned logical volumes 或 RAID，请参见 [#逻辑卷类型](<#%E9%80%BB%E8%BE%91%E5%8D%B7%E7%B1%BB%E5%9E%8B>).

创建完卷组（VG）之后，就可以开始创建逻辑卷（LV）了。输入下面命令以指定新逻辑卷的名字、大小及其所在的卷组： 
    
    # lvcreate -L <_卷大小_ > <"卷组名 _> -n <_卷名 _>_
    
例如： 
    
    # lvcreate -L 10G VolGroup00 -n lvolhome
    
该逻辑卷创建完后，你就可以通过`/dev/mapper/Volgroup00-lvolhome`或`/dev/VolGroup00/lvolhome`来访问它。与卷组命名类似，你可以按你的需要将逻辑卷命名。 

你可以指定一个或多个物理卷来限制LVM分配数据空间的位置。比如你希望在较小的SSD硬盘上创建根文件系统，并在较慢的机械硬盘上创建家目录卷，仅需把物理卷设备加入到命令中，例如： 
    
    # lvcreate -L 10G VolGroup00 -n lvolhome /dev/sdc1
    
如果你想让要创建的逻辑卷拥有卷组（VG）的所有未使用空间，请使用以下命令： 
    
    # lvcreate -l +100%FREE  <_volume_group_ > -n <_logical_volume_ >
    
可以通过以下命令来查看逻辑卷： 
    
    # lvdisplay
    
**注意：** 为了使上述命令能正常运行，你可能需要加载 _device-mapper_ 内核模块（请使用命令**modprobe dm-mod** ）。

**提示：** 一开始可以创建小一点的逻辑卷，在卷组里留下一部分未使用空间，以后就可以根据需要再作扩展了。

###  建立文件系统与挂载逻辑卷

现在你的逻辑卷应该已经在`/dev/mapper/`和`/dev/_YourVolumeGroupName_`中了。如果你无法在以上位置找到它，请使用以下命令来加载模块、并扫描与激活卷组： 
    
    # modprobe dm-mod
    # vgscan
    # vgchange -ay
    
现在你可以在逻辑卷上创建文件系统并像普通分区一样挂载它了（如果你正在安装Arch linux，需要更详细的信息，请参考[挂载分区](<../zh-cn/Installation_guide.html#%E6%8C%82%E8%BD%BD%E5%88%86%E5%8C%BA> "Installation guide")）： 
    
    # mkfs.<_类型_ > /dev/mapper/<_卷组名_ >-<_卷名_ >
    # mount /dev/mapper/<_卷组名_ >-<_卷名_ > <_挂载点_ >
    
例如： 
    
    # mkfs.ext4 /dev/mapper/VolGroup00-lvolhome
    # mount /dev/mapper/VolGroup00-lvolhome /home
    
**警告：** 挂载点请选择你所新建的逻辑卷（例如：`/dev/mapper/Volgroup00-lvolhome`），**不要** 使用逻辑卷所在的实际分区设备（即不要使用：`/dev/sda2`）。

###  配置mkinitcpio

如果你的根文件系统基于LVM，你需要启用适当的[mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")钩子，否则你的系统可能无法启动。 

  * 若使用基于busybox的initramfs，请启用`udev`和`lvm2`。
  * 若使用基于systemd的initramfs，请启用`systemd`和`sd-lvm2`。

`udev`默认已经预设好，不必手动启用了。你只需要编辑`/etc/mkinitcpio.conf`文件，在`block`与`filesystem`这两项中间插入`lvm2`： 

基于busybox的initramfs 
    
    /etc/mkinitcpio.conf
    
    HOOKS="base udev ... block **lvm2** filesystems"

基于systemd的initramfs: 
    
    /etc/mkinitcpio.conf
    
    HOOKS=(base **systemd** ... block **lvm2** filesystems)

之后你就可以继续下一步的[创建和启用镜像](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio")操作了。 

**提示：**

  * `lvm2`和`sd-lvm2`钩子被[lvm2](<https://archlinux.org/packages/?name=lvm2>)包安装，而不是[mkinitcpio](<https://archlinux.org/packages/?name=mkinitcpio>)包。如果你在"arch-chroot"中新安装的Arch Linux中运行"mkinitcpio"，必须在环境中安装[lvm2](<https://archlinux.org/packages/?name=lvm2>)包以使 _mkinitcpio_ 找到`lvm2`或`sd-lvm2`钩子。如果[lvm2](<https://archlinux.org/packages/?name=lvm2>)包未安装, _mkinitcpio_ 将报错：`Error: Hook 'lvm2' cannot be found`.
  * 若根文件系统在LVM + RAID上，请参见[#为RAID配置mkinitcpio](<#%E4%B8%BARAID%E9%85%8D%E7%BD%AEmkinitcpio>).

###  内核参数

如果你的根文件系统位于逻辑分卷，则`root=` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")必须指向一个映射设备，比如`/dev/mapper/_vg-name_ -_lv-name_`。 

##  配置

###  高级选项

可以通过修改`/etc/lvm/lvm.conf`文件中的`auto_activation_volume_list`参数限制自动激活的卷。如果存在问题，可以将此选项注释掉。 

###  调整卷

####  物理卷

对于存在物理卷的设备，在扩增其容量之后或缩小其容量之前，必须使用`pvresize`命令对应地增加或减少物理卷的大小。 

#####  扩增

增大[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning")`/dev/sda1`的容量之后，需要执行以下命令扩展物理卷的大小 
    
    # pvresize /dev/sda1
    
命令将自动探测设备当前大小并将物理卷扩展到其最大容量。 

**注意：** 该命令可在卷在线（on-line）时运行。

#####  缩小

在减少某个物理卷所在设备大小之前，需要通过指定`--setphysicalvolumesize _大小_`参数缩小物理卷大小，例如： 
    
    # pvresize --setphysicalvolumesize 40G /dev/sda1
    
该命令可能会提示以下错误： 
    
     /dev/sda1: cannot resize to 25599 extents as later ones are allocated.
     0 physical volume(s) resized / 1 physical volume(s) not resized
    
即该物理卷已分配物理区域超过了命令指定的新大小边界，`pvresize`会拒绝将物理卷缩小。若磁盘空间足够，可通过[pvmove](<#%E7%A7%BB%E5%8A%A8%E7%89%A9%E7%90%86%E5%8C%BA%E5%9F%9F>)将物理区域重新分配至别的卷组来解决这个问题。 

######  移动物理区域

在移动空闲的物理区域到卷尾部之前，需要运行`# pvdisplay -v -m`命令查看物理分段。如下例所示，仅有一个物理卷`/dev/sdd1`, 一个卷组`vg1`和一个逻辑卷`backup`
    
    # pvdisplay -v -m
    
        Finding all volume groups.
        Using physical volume(s) on command line.
      --- Physical volume ---
      PV Name               /dev/sdd1
      VG Name               vg1
      PV Size               1.52 TiB / not usable 1.97 MiB
      Allocatable           yes 
      PE Size               4.00 MiB
      Total PE              399669
      Free PE               153600
      Allocated PE          246069
      PV UUID               MR9J0X-zQB4-wi3k-EnaV-5ksf-hN1P-Jkm5mW
       
      --- Physical Segments ---
      Physical extent 0 to 153600:
        FREE
      Physical extent 153601 to 307199:
        Logical volume	/dev/vg1/backup
        Logical extents	1 to 153599
      Physical extent 307200 to 307200:
        FREE
      Physical extent 307201 to 399668:
        Logical volume	/dev/vg1/backup
        Logical extents	153601 to 246068

可用空间在卷中段。为了减小物理卷大小，首先必须把所有的已用分段移到前部。 

此例中，第一个可用空间在第0至第153600分段共153601个可用区域。我们可以从最后的分段中移动相同数目的物理区域来填补这段空间 
    
    # pvmove --alloc anywhere /dev/sdd1:307201-399668 /dev/sdd1:0-92466
    
    /dev/sdd1: Moved: 0.1 %
    /dev/sdd1: Moved: 0.2 %
    ...
    /dev/sdd1: Moved: 99.9 %
    /dev/sdd1: Moved: 100,0%

**注意：**

  * 命令将92467 (399668-307201)个物理区域**从** 最后一个分段**移动到** 第一个分段。由于第一个分段共有153600个空闲的物理区域，可以容纳92467个物理区域，命令可以成功执行。
  * 参数`--alloc anywhere`可以用于在同一个分区中移动物理区域的。若要在不同分区中移动，命令形式应该是`# pvmove /dev/sdb1:1000-1999 /dev/sdc1:0-999`
  * 当操作的数据较多时，移动操作将持续很久（一到两个小时）。最好在[Tmux](<../zh-cn/Tmux.html> "Tmux")或[GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen")会话中执行此过程。任何形式的意外中断都可能会导致致命错误。
  * 当操作完成后，可运行[Fsck](<../zh-cn/Fsck.html> "Fsck")保证文件系统完整性。

######  调整物理卷大小

当所有空闲分段都移动到最后的物理区域时，运行`# vgdisplay`查看。 

之后可以再次运行命令： 
    
    # pvresize --setphysicalvolumesize _size_ _PhysicalVolume_
    
结果类似： 
    
    # pvs
    
      PV         VG   Fmt  Attr PSize    PFree 
      /dev/sdd1  vg1  lvm2 a--     1t     500g
    
######  调整分区大小

最后，你可以用你喜欢的[分区工具](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E5%B7%A5%E5%85%B7> "Partitioning")来缩小该分区。 

####  逻辑卷

**提示：**[lvresize(8)](<https://man.archlinux.org/man/lvresize.8>)提供一些与[lvextend(8)](<https://man.archlinux.org/man/lvextend.8>)和[lvreduce(8)](<https://man.archlinux.org/man/lvreduce.8>)相同的命令与选项，并同时允许两种类型的操作。然而，这几个命令都提供一个`-r`/`--resizefs`选项，使用[fsadm(8)](<https://man.archlinux.org/man/fsadm.8>)在调整逻辑卷时同时调整其中的文件系统（支持 _ext2_ , [ext3](</wzh/index.php?title=Ext3&action=edit&redlink=1> "Ext3（页面不存在）"), [ext4](<../zh-cn/Ext4.html> "Ext4"), _ReiserFS_ 和 [XFS](<../zh-cn/XFS.html> "XFS") ）。 因此，对普通使用来说，使用`lvresize`和`--resizefs`将会更容易, 除非您有特定的需求或希望完全控制流程。

**警告：** 尽管扩大一个文件系统可以“在线”(on-line)，也就是当它已挂载时)完成，甚至对根分区。缩小一个文件系统却往往要求先卸载（umount）它，以避免丢失数据。请先确保你的文件系统支持相关操作。

#####  同时缩小逻辑卷和其文件系统

**注意：** 只有 _ext2_ ，[ext3](</wzh/index.php?title=Ext3&action=edit&redlink=1> "Ext3（页面不存在）")，[ext4](<../zh-cn/Ext4.html> "Ext4")， _ReiserFS_ 和 [XFS](<../zh-cn/XFS.html> "XFS") [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")支持以下操作。对于其他文件系统，请参见[#单独设置文件系统大小](<#%E5%8D%95%E7%8B%AC%E8%AE%BE%E7%BD%AE%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E5%A4%A7%E5%B0%8F>)。

将`MyVolGroup`组中的逻辑卷`mediavol`扩大10GiB，并同时扩大其文件系统： 
    
    # lvresize -L +10G --resizefs MyVolGroup/mediavol
    
将`MyVolGroup`组中的逻辑卷`mediavol`大小调整为15GiB，并同时调整其文件系统： 
    
    # lvresize -L 15G --resizefs MyVolGroup/mediavol
    
将卷组中的所有剩余空间分配给`mediavol`： 
    
    # lvresize -l +100%FREE --resizefs MyVolGroup/mediavol
    
更多选项请参见[lvresize(8)](<https://man.archlinux.org/man/lvresize.8>)。 

#####  单独设置文件系统大小

对于不支持[fsadm(8)](<https://man.archlinux.org/man/fsadm.8>)的文件系统，请在缩小逻辑卷前或扩大逻辑卷后，使用[适当的工具](<../zh-cn/File_systems.html#%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E7%B1%BB%E5%9E%8B> "File systems")来调整文件系统的大小。 

先将`MyVolGroup`组中的逻辑卷`mediavol`扩大2 GiB，但不调整其文件系统： 
    
    # lvresize -L +2G MyVolGroup/mediavol
    
然后在调整其文件系统，是其达到逻辑卷的大小：（以[ext4](<../zh-cn/Ext4.html> "Ext4")为例） 
    
    # resize2fs /dev/MyVolGroup/mediavol
    
要将逻辑卷`mediavol`缩小500 MiB，先计算调整后文件系统的大小并调整文件系统(以[ext4](<../zh-cn/Ext4.html> "Ext4")为例)： 
    
    # resize2fs /dev/MyVolGroup/mediavol _调整后的大小_
    
然后再缩小逻辑卷的大小： 
    
    # lvresize -L -500M MyVolGroup/mediavol
    
更多选项请参见[lvresize(8)](<https://man.archlinux.org/man/lvresize.8>)。 

###  重命名卷

####  重命名卷组

要重命名一个卷组，请使用[vgrename(8)](<https://man.archlinux.org/man/vgrename.8>)命令。 

可使用下面的任意一条命令将卷组`vg02`重命名为`my_volume_group`
    
    # vgrename /dev/vg02 /dev/my_volume_group
    
    # vgrename vg02 my_volume_group
    
####  重命名逻辑卷

要重命名一个逻辑卷，请使用[lvrename(8)](<https://man.archlinux.org/man/lvrename.8>)命令。 

可使用下面的任意一条命令将`vg02`组中的逻辑卷`lvold`重命名为`lvnew`. 
    
    # lvrename /dev/vg02/lvold /dev/vg02/lvnew
    
    # lvrename vg02 lvold lvnew
    
###  移除逻辑卷

**警告：** 在移除逻辑卷之前，请先备份好数据以免丢失！

首先，找到你所要移除的逻辑卷的名称。你可以使用以下命令来查看系统的所有逻辑卷： 
    
    # lvs
    
接下来，找到你所要移除的逻辑卷的挂载点 
    
    $ lsblk
    
并卸载它： 
    
    # umount /<_mountpoint_ >
    
最后，使用以下命令来移除逻辑卷： 
    
    # lvremove <_volume_group_ >/<_logical_volume_ >
    
例如： 
    
    # lvremove VolGroup00/lvolhome
    
请输入`y`来确定你要执行移除逻辑卷操作。 

此外，请不要忘了更新`/etc/fstab`。 

你可以再次使用`lvs`命令来确认你的逻辑卷已被移除。 

###  添加物理卷到卷组中

首先创建一个新的物理卷，再把卷组扩充到该物理卷上： 
    
    # pvcreate /dev/sdb1
    # vgextend VolGroup00 /dev/sdb1
    
这将增加你卷组中的物理区域总数，你可以按需要将它们分配到逻辑卷中。 

**注意：** 将[分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning")保存在LVM所在媒体设备是个值得借鉴的方式。对于MBR可以使用类型`8e`，或GPT类型`8e00`。

###  从卷组中移除（物理）分区

如果在这个物理分区上创建了一个逻辑卷，请先[移除](<#%E7%A7%BB%E9%99%A4%E9%80%BB%E8%BE%91%E5%8D%B7>)它。 

首先，分区中的所有数据需要被转移到别的分区，幸而LVM提供了以下的简便方式： 
    
    # pvmove /dev/sdb1
    
如果你想指定所要转移的目标分区，那么可以把该分区作为`pvmove`的第二个参数： 
    
    # pvmove /dev/sdb1 /dev/sdf1
    
接着，从卷组（VG）中移除物理卷（PV）： 
    
    # vgreduce myVg /dev/sdb1
    
或者把所有的空物理卷（PV）都移除掉： 
    
    # vgreduce --all vg0
    
最后，如果你仍然想要使用该分区，而且不想让LVM以为它是一个物理卷，那么你可以执行以下命令： 
    
    # pvremove /dev/sdb1
    
###  停用卷组

只需执行： 
    
    # vgchange -a n my_volume_group
    
这将停用此卷组，以便你卸载存储它的容器。 

##  逻辑卷类型

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 是否需要为thin-provisioned卷和RAID卷的创建提供说明？（在 [Talk:LVM#](<../zh-cn/Talk:LVM.html>) 中讨论）

除了普通的逻辑卷, LVM还支持：快照, logical volume caching, thin provisioned逻辑卷，以及RAID. 

###  快照功能

####  介绍

LVM可以给系统创建一个快照，由于使用了写入时复制(copy-on-write) 策略，相比传统的备份更有效率。 初始的快照只有关联到实际数据的inode的实体链接(hark-link)而已。只要实际的数据没有改变，快照就只会包含指向数据的inode的指针，而非数据本身。一旦你更改了快照对应的文件或目录，LVM就会自动拷贝相应的数据，包括快照所对应的旧数据的拷贝和你当前系统所对应的新数据的拷贝。这样的话，只要你修改的数据（包括原始的和快照的）不超过2G，你就可以只使用2G的空间对一个有35G数据的系统创建快照。要创建快照，在卷组中必须有未被分配的空间。和其他逻辑卷一样，快照也会占用卷组中的空间。所以，如果你计划使用快照来备份你的根（root）分区，不要将整个卷组的空间都分配给根（root）逻辑卷。 

####  配置

你可以像创建普通逻辑卷一样创建快照逻辑卷。 
    
    # lvcreate --size 100M --snapshot --name snap01 /dev/vg0/lv
    
你可以修改少于100M的数据，直到该快照逻辑卷空间不足为止。 

要将逻辑卷卷'lv' 恢复到创建快照'snap01'时的状态，请使用： 
    
    # lvconvert --merge /dev/vg0/snap01
    
如果逻辑卷处于活动状态，则在下次重新启动时将进行合并（merging）(合并（merging）甚至可在LiveCD中进行)。 

**注意：** 合并后快照将被删除。

也以拍摄多个快照，每个快照都可以任意与对应的逻辑卷合并。 

快照也可以被挂载，并可用**dd** 或者**tar** 备份。使用**dd** 备份的快照的大小为拍摄快照后对应逻辑卷中变更过文件的大小。 要使用备份，只需创建并挂载一个快照，并将备份写入或解压到其中。再将快照合并到对应逻辑卷即可。 

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 是否需要单独的文章来介绍：创建在系统更新前自动备份根目录的脚本，用于回滚。并修改`menu.lst`以引导备份？（在 [Talk:LVM#](<../zh-cn/Talk:LVM.html>) 中讨论）

快照主要用于提供一个文件系统的拷贝，以用来备份; 比起直接备份分区，使用快照备份可以提供一个更符合原文件系统的镜像。 

###  LVM 缓存

来自[lvmcache(7)](<https://man.archlinux.org/man/lvmcache.7>): 

    Cache逻辑卷将使用一个较小而快速的逻辑卷，来提高较大但慢速的逻辑卷的性能。它将大型逻辑卷中经常使用的块存储到较快的缓存卷中。 LVM将这个小而快速的逻辑卷称为缓冲池逻辑卷（cache pool LV）。 大而慢的逻辑卷则被称为源逻辑卷（origin LV）。由于dm-cache（内核驱动）的要求，LVM进一步将缓存池逻辑卷分为两个设备 - 缓存数据逻辑卷和缓存元数据逻辑卷。缓存数据逻辑卷存放源逻辑卷中常用块的拷贝，以提升源逻辑卷的速度。 缓存元数据逻辑卷则存储记录信息，这些信息指定了源逻辑卷中的数据被存放到缓存逻辑卷中的位置。 (即，确定源逻辑卷中的一个块是存储到自身空间还是缓存逻辑卷中？)。要想创建最好、最稳定的缓存逻辑卷，你必须熟悉这些信息。所有这些被提到的逻辑卷都必须存放在一个卷组中。

####  创建缓存

最快速的方法是直接在快速的设备上创建一个物理卷，并把它添加到一个卷组中： 
    
    # vgextend dataVG /dev/sdx
    
只需一步，即可在sdb上创建一个缓存池，自动生成元数据，将逻辑卷dataLV缓存到sdb上： 
    
    # lvcreate --type cache --cachemode writethrough -L 20G -n dataLV_cachepool dataVG/dataLV /dev/sdx
    
显然，如果你想让缓存变得更大，可更改 `-L`参数。 

**注意：** Cachemode有两个可能的参数： 

  * `writethrough` 确保任何数据写入都会被同时存储到缓存池逻辑卷和源逻辑卷中。 在这种情况下，丢失与缓存池逻辑卷关联的设备不会丢失任何数据；
  * `writeback` 可提供更好的性能, 如果用于缓存的设备发生故障，数据丢失的风险会更高。

如果未指定`--cachemode`，将会自动选择`writethrough`。 

####  删除缓存

如果需要撤消上面的创建操作： 
    
    # lvconvert --uncache dataVG/dataLV
    
这会将缓存中挂起的写入操作提交到源逻辑卷， 然后删除缓存逻辑卷。 其它可用的参数和介绍，请参见：[lvmcache(7)](<https://man.archlinux.org/man/lvmcache.7>). 

### RAID

来自[lvmraid(7)](<https://man.archlinux.org/man/lvmraid.7>): 

     [lvm(8)](<https://man.archlinux.org/man/lvm.8>) RAID是一种创建逻辑卷的方法，它使用多个物理设备来提高性能或容错能力。在LVM中，这些物理设备是单个卷组中的物理卷。

LVM RAID支持RAID 0，RAID 1，RAID 4，RAID 5，RAID 6和RAID 10。每个RAID等级的细节请见：[Wikipedia:Standard RAID levels](<https://en.wikipedia.org/wiki/Standard_RAID_levels> "wikipedia:Standard RAID levels")

####  配置RAID

创建物理卷： 
    
    # pvcreate /dev/sda2 /dev/sdb2 
    
创建卷组： 
    
    # vgcreate VolGroup00 /dev/sda2 /dev/sdb2
    
使用`lvcreate --type _raidlevel_`参数创建逻辑卷。更多选项，请参见[lvmraid(7)](<https://man.archlinux.org/man/lvmraid.7>)和[lvcreate(8)](<https://man.archlinux.org/man/lvcreate.8>)。 
    
    # lvcreate --type RaidLevel [OPTIONS] -n Name -L Size VG [PVs]
    
例如： 
    
    # lvcreate --type raid1 --mirrors 1 -L 20G -n myraid1vol VolGroup00 /dev/sda2 /dev/sdb2
    
这将会在设备`/dev/sda2`、`/dev/sdb2`上和"VolGroup00"卷组中创建一个20GiB的镜像（mirrored）逻辑卷"myraid1vol"。 

####  为RAID配置mkinitcpio

如果你的根文件系统在LVM RAID上，除了`lvm2`或`sd-lvm2`钩子，你还需添加`dm-raid`以及恰当的RAID模块(例如`raid0`，`raid1`，`raid10`或`raid456`)到`mkinitcpio.conf`中的MODULES数组中。 

对于基于busybox的initramfs： 
    
    /etc/mkinitcpio.conf
    
    MODULES=(**dm-raid raid0 raid1 raid10 raid456**)
    HOOKS=(base **udev** ... block **lvm2** filesystems)

对于基于systemd的initramfs： 
    
    /etc/mkinitcpio.conf
    
    MODULES=(**dm-raid raid0 raid1 raid10 raid456**)
    HOOKS=(base **systemd** ... block **sd-lvm2** filesystems)

##  图形化配置

目前没有“官方的”管理LVM卷的GUI工具，不过[system-config-lvm](<https://aur.archlinux.org/packages/system-config-lvm/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]涵盖了大多数常见操作，并提供卷状态的简单可视化。它还可以在调整逻辑卷大小时自动调整许多文件系统的大小。 

##  常见问题

###  由于禁用lvmetad带来的开/关机问题

”必须“在`/etc/lvm/lvm.conf`中设置`use_lvmetad = 1`。 现在这已时默认设置 - 如果存在 `lvm.conf.pacnew`文件，你必须合并这个更改。 

###  LVM 命令不起作用

  * 加载以下模块:

    # modprobe dm_mod
    
正常情况下，`dm_mod`模块应当被自动加载。假如该模块无法被自动加载，你可以试着修改`/etc/mkinitcpio.conf`： 

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 英文章不正。是否应当考虑加入到"/etc/modules-load.d"？（在 [Talk:LVM#](<../zh-cn/Talk:LVM.html>) 中讨论）
    
    /etc/mkinitcpio.conf:
    
    MODULES="dm_mod ..."

你需要[重建initramfs](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio")来提交你对`/etc/mkinitcpio.conf`的更改。 

  * 测试以 _lvm_ 开头的命令是否可以被正确执行，例如：

    # lvm pvdisplay
    
###  逻辑卷无法显示

如果你在挂载某个已创建好的逻辑卷时，发现它没有出现在`lvscan`命令的结果列表里，但是使用`lvdisplay -a`可找到此卷且状态为Not Available，那么你可以用以下命令去激活它： 
    
    # vgscan
    # vgchange -ay
    
###  在可移除设备上的LVM问题

症状： 
    
    # vgscan
     Reading all physical volumes.  This may take a while...
     /dev/backupdrive1/backup: read failed after 0 of 4096 at 319836585984: Input/output error
     /dev/backupdrive1/backup: read failed after 0 of 4096 at 319836643328: Input/output error
     /dev/backupdrive1/backup: read failed after 0 of 4096 at 0: Input/output error
     /dev/backupdrive1/backup: read failed after 0 of 4096 at 4096: Input/output error
     Found volume group "backupdrive1" using metadata type lvm2
     Found volume group "networkdrive" using metadata type lvm2
    
产生原因： 

    在停用卷组（VG）之前就移除掉外部的LVM设备。在你断开连接之前，请确保以下命令被执行：
    
    # vgchange -an _volume group name_
    
解决方案：如果你已经用`# vgchange -ay _vg_`命令来激活卷组，但仍有 _Input/output error_ 的错误信息。执行以下命令： 
    
    # vgchange -an _volume group name_
    
移除外部设备，稍候几分钟后再执行以下命令： 
    
    # vgscan
    # vgchange -ay _volume group name_
    
###  无法调整相邻逻辑卷的大小

在尝试扩大一个逻辑卷时出现以下错误： 
    
    " Insufficient suitable contiguous allocatable extents for logical volume "
    
其原因是此逻辑卷在创建时使用了显式连续分配策略（an explicit contiguous allocation policy）(`-C y`选项或`--alloc contiguous`)，并且没有其他相邻的连续数据块可用(另见[reference](<https://www.hostatic.ro/lvm-inherit-and-contiguous-policies/>))。 

要修复此错误，在扩展逻辑卷之前，使用`lvchange --alloc inherit <logical_volume>`更改其分配策略。 如果需要保持连续分配策略，另一种方法是将卷移动到具有足够可用区域的磁盘区域(见[[1]](<https://superuser.com/questions/435075/how-to-align-logical-volumes-on-contiguous-physical-extents>))。 

###  "grub-mkconfig"命令报告"unknown filesystem"错误

请确保在生成grub.cfg前移除了快照卷。 

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 内容未翻译（在 [Talk:LVM#](<../zh-cn/Talk:LVM.html>) 中讨论）

### Thinly-provisioned root volume device times out

With a large number of snapshots, `thin_check` runs for a long enough time so that waiting for the root device times out. To compensate, add the `rootdelay=60` kernel boot parameter to your boot loader configuration. Or, make `thin_check` skip checking block mappings (see [[2]](<https://www.redhat.com/archives/linux-lvm/2016-January/msg00010.html>)) and [regenerate the initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs"): 
    
    /etc/lvm/lvm.conf
    
    thin_check_options = [ "-q", "--clear-needs-check-flag", "--skip-mappings" ]

### Delay on shutdown

If you use RAID, snapshots or thin provisioning and experience a delay on shutdown, make sure `lvm2-monitor.service` is [started](</wzh/index.php?title=Started&action=edit&redlink=1> "Started（页面不存在）"). See [FS#50420](<https://bugs.archlinux.org/task/50420>). 

##  更多资源

  * [LVM2 Resource Page](<https://sourceware.org/lvm2/>) on SourceWare.org
  * [LVM HOWTO](<https://tldp.org/HOWTO/LVM-HOWTO/>) article at The Linux Documentation project
  * [LVM](<https://wiki.gentoo.org/wiki/LVM>) article at Gentoo wiki
  * [LVM2 Mirrors vs. MD Raid 1](<http://www.joshbryan.com/blog/2008/01/02/lvm2-mirrors-vs-md-raid-1/>) post by Josh Bryan
  * [Ubuntu LVM Guide Part 1](<https://www.tutonics.com/2012/11/ubuntu-lvm-guide-part-1.html>)[Part 2 detals snapshots](<https://www.tutonics.com/2012/12/lvm-guide-part-2-snapshots.html>)
