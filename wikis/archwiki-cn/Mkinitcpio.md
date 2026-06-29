**翻译状态：**

  * 本文（或部分内容）译自 [mkinitcpio](<https://wiki.archlinux.org/title/mkinitcpio> "arch:mkinitcpio")，最近一次同步于 2025-12-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/mkinitcpio?diff=0&oldid=858491>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/mkinitcpio_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Booster](<../zh-cn/Booster.html> "Booster")
  * [Boot debugging](<../zh-cn/Boot_debugging.html> "Boot debugging")
  * [dracut](<../zh-cn/Dracut.html> "Dracut")
  * [Kernel modules](<../zh-cn/Kernel_modules.html> "Kernel modules")
  * [mkinitcpio/极简 initramfs](<../zh-cn/Mkinitcpio/%E6%9E%81%E7%AE%80_initramfs.html> "Mkinitcpio/极简 initramfs")
  * [systemd](<../zh-cn/Systemd.html> "Systemd")
  * [统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像")

[mkinitcpio](<https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio>) 是用于创建 initramfs 映像的 bash 脚本。有关对 initramfs 的一般性介绍，请参阅 [Arch 的启动流程#initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Arch 的启动流程")。 

需要注意的是，存在两种截然的不同方式用于执行[早期用户空间](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E6%97%A9%E6%9C%9F%E7%94%A8%E6%88%B7%E7%A9%BA%E9%97%B4> "Arch 的启动流程")阶段的各项任务： 

基于 systemd 的 initramfs（版本 40 起默认）

    systemd 在早期用户空间阶段开始时即被启动。需要执行的任务由常规的 systemd 单元文件决定。参见 [systemd 启动流程](<https://www.freedesktop.org/software/systemd/man/latest/bootup.html>)。

     **优点** ： 

  * 与 systemd 生态系统的其余部分紧密集成，带来更一致、流畅的启动流程。
  * 能更有效地并行化某些启动任务，在某些场景下可能缩短整体启动时间。
  * 提供更全面的功能集，例如 [systemd-cryptsetup-generator](<../zh-cn/Dm-crypt/%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE.html#%E4%BD%BF%E7%94%A8systemd-cryptsetup-generator> "Dm-crypt/系统配置") 与 [GPT 分区自动挂载](<../zh-cn/Systemd.html#GPT%E5%88%86%E5%8C%BA%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Systemd")功能。

     **缺点** ： 

  * 依赖较多，生成映像较大。由于包含 systemd 二进制文件及其依赖项，通常会导致 initramfs 增大，可能会稍稍延长启动时间。

基于 BusyBox 的 initramfs

    启动一个 init 脚本，该脚本随后扫描 initramfs 查找需要执行的脚本（即本文中的“运行时钩子”）。

     **优点** ： 

  * 轻量级，依赖较少，生成映像较小。

具体采用哪种方案取决于 `/etc/mkinitcpio.conf` 的 `HOOKS` 数组中是否包含 `systemd` 钩子。详见 [#常用钩子](<#%E5%B8%B8%E7%94%A8%E9%92%A9%E5%AD%90>)。 

mkinitcpio 由 Arch Linux 开发者及社区贡献者共同开发。参见[公开 Git 仓库](<https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio>)。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [mkinitcpio](<https://archlinux.org/packages/?name=mkinitcpio>)包。这个软件包是 [linux](<https://archlinux.org/packages/?name=linux>)包 等软件包的依赖，应该已经自动被安装了。高级用户可以从 [mkinitcpio-git](<https://aur.archlinux.org/packages/mkinitcpio-git/>)AUR 获取 mkinitcpio 的最新开发版本。 

**注意：** 若要使用 git 开发版本，强烈建议同时加入 [arch-projects](<https://lists.archlinux.org/mailman3/lists/arch-projects.lists.archlinux.org/>) 邮件列表！

##  创建和启用映像

###  自动匹配生成

每次安装或升级内核时，一 [pacman 钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")会自动在 `/etc/mkinitcpio.d/` 生成 .preset 文件。例如，`linux.preset` 文件是官方稳定内核 [linux](<https://archlinux.org/packages/?name=linux>)包 生成的。.preset 文件本质上是一个创建 initramfs 映像所需信息的列表，避免手动指定各项参数及输出文件位置。 

可自动创建两个映像： 

  * default（默认）映像，根据 [#配置](<#%E9%85%8D%E7%BD%AE>)中的指令创建。
  * fallback（后备）映像，与上述类似，但不使用 [autodetect 钩子](<#%E5%B8%B8%E8%A7%81%E9%92%A9%E5%AD%90>)，因此包含支持大多数硬件的完整模块集。

默认仅创建 default 映像，fallback 映像必须[显式启用](<#%E7%94%9F%E6%88%90_fallback_initramfs_%E6%98%A0%E5%83%8F>)。 

创建预设文件后，该 pacman 钩子会调用 `mkinitcpio`，利用 .preset 文件中提供的信息生成映像。 

**注意：**.preset 文件用于在内核更新后自动重新生成 initramfs，编辑时请务必小心。

###  手动生成

手动运行脚本，参照[mkinitcpio(8)](<https://man.archlinux.org/man/mkinitcpio.8>) 帮助页面获得指引。尤其是当利用内核包生成（重新生成）预设时，使用`-p`/`--preset`选项按照预设生成映像。例如 为 [linux](<https://archlinux.org/packages/?name=linux>)包 包生成映像，使用这个命令： 
    
    # mkinitcpio -p linux
    
利用`-P`/`--allpresets`选项，根据所有现存的预设文件生成映像。常见的用法是当全局设置[#配置](<#%E9%85%8D%E7%BD%AE>)变化后用此法重新生成全部的内存映像： 
    
    # mkinitcpio -P
    
可以按照不同的配置文件创建任意数量的内存映像。想要引导加载的映像必须在相应的[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "Arch 的启动流程")配置中明确写出。 

###  自定义生成

可以使用相应的配置文件产生一个映像。例如，接下来会根据`/etc/mkinitcpio-custom.conf`里指令生成初始化内存映像，并且将后者保存在 `/boot/initramfs-custom.img`。 
    
    # mkinitcpio --config /etc/mkinitcpio-custom.conf --generate /boot/initramfs-custom.img
    
如果为一个不是当前运行的内核创建映像，增加内核版本号到命令行。已安装的内核版本号可以在`/usr/lib/modules/`中找到，对于每个内核语法结构和`uname -r`命令输出结果一致。 
    
    # mkinitcpio --generate /boot/initramfs-custom2.img --kernel 5.7.12-arch1-1
    
###  统一内核映像

mkinitcpio 既可自行构建[统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像")（UKI），也可通过 [systemd-ukify](<https://archlinux.org/packages/?name=systemd-ukify>)包 构建。如果系统中未安装 [systemd-ukify](<https://archlinux.org/packages/?name=systemd-ukify>)包 或使用 `--no-ukify` 参数明确禁用它，mkinitcpio 将使用自有实现，但此时将无法使用 ukify 提供的高级功能。 

关于构建 UKI 的详细信息，请参阅[统一内核映像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核映像")。 

##  配置

**mkinitcpio** 的主配置文件是`/etc/mkinitcpio.conf`。也支持附加配置文件（Drop-in），如`/etc/mkinitcpio.conf.d/mkhooks.conf`（当使用 `-c`/`--config` 选项和/或使用了含 `ALL_config` 的预设时无效）。此外，内核软件包的预配置文件位于`/etc/mkinitcpio.d`（例如：`/etc/mkinitcpio.d/linux.preset`）。 

用户可以编辑配置文件中的七个变量，参见[mkinitcpio.conf(5) § VARIABLES](<https://man.archlinux.org/man/mkinitcpio.conf.5#VARIABLES>)获得更多细节： 

`MODULES`
    在钩子扩展运行前需要加载的内核模块。
`BINARIES`
    内存盘映像中包含的额外的二进制文件（一般是可执行的命令）。
`FILES`
    内存盘映像中包含的其他文件。
`HOOKS`
    要执行的钩子扩展，它是在生成映像时执行的脚本。
`COMPRESSION`
    内存盘映像的压缩方式。
`COMPRESSION_OPTIONS`
    传递给压缩工具的额外参数，强烈不建议使用， _mkinitcpio_ 可以自动根据压缩算法传递需要的参数(例如对 xz 传递 `--check=crc32` to xz), 手动设置了错误的参数可能导致系统无法启动。
`MODULES_DECOMPRESS`
    解压可加载内核模块和固件文件或保持未解压原样。

**注意：**

  * 一些系统需要的钩子像 **lvm2** , **mdadm_udev** , and **encrypt** 默认 **不是开启的** 。参见 [#钩子（HOOKS）](<#%E9%92%A9%E5%AD%90%EF%BC%88HOOKS%EF%BC%89>) 仔细遵循指示。
  * 存在多个硬盘控制器使用相同的节点名字，但是拥有不同的内核模块（例如，两个SCSI/SATA控制器或2个IDE控制器）应该使用 持久化设备命名[persistent block device naming](<../zh-cn/Persistent_block_device_naming.html> "Persistent block device naming") 保证正确的设备被挂载。否则在两次系统启动时根系统的位置可能改变导致内核崩溃。

###  模块（MODULES）

`MODULES`数组指定了启动过程最开始时就要加载的模块。 

如果模块名称后加上一个`?`问号，那么即使系统无法找到该模块也不会报错。对于自己编译的内核，其中内置了某些模块，在这些模块在钩子或配置文件中显式的列出来时，该功能可能有用。 

**注意：**

  * 如果使用树外文件系统，且需要在早期用户空间挂载时（比如作为根文件系统），对应模块（如 **reiser4** ）**必须** 加入 `MODULES` 数组中。
  * 当使用 **encrypt** 或 **sd-encrypt** 钩子时,目标系统和运行 _mkinitcpio_ 系统不同时，键盘模块和/或启动系统期间需要解锁LUKS设备的文件系统模块加入 `MODULES` 数组。例如，如果需要使用位于一个ext2系统的钥匙文件，但是运行 _mkinitcpio_ 的系统中ext2文件系统没有被挂载，增加`ext2`。参见 [dm-crypt/System configuration#cryptkey](<https://wiki.archlinux.org/title/Dm-crypt/System_configuration#cryptkey>) 获得更多细节。
  * 如果使用USB3接口的键盘，希望用它来解锁LUKS设备。增加`usbhid xhci_hcd`。
  * 如果使用显示器连接扩展坞，可能需要加入你的显卡模块使初始化输出信息可见(例如，为大多数英特尔显卡加入 `i915` )。

###  二进制文件和普通文件（BINARIES、FILES）

这两个选项允许用户添加任何文件到映像中。`BINARIES`、`FILES`数组在钩子运行之前指定了要加入内存盘映像的文件，可以覆盖钩子扩展提供的文件。`BINARIES`中的二进制文件会自动放入一个标准的`PATH`路径，而且会自动加入可执行文件依赖的函数库。`FILES`中的文件则不进行上述处理， _as-is_ 直接原样放入映像。例如： 
    
    FILES=(/etc/modprobe.d/modprobe.conf)
    BINARIES=(kexec)
    
注意 `BINARIES` 和 `FILES` 是 [Bash](<../zh-cn/Bash.html> "Bash")数组，配置支持多个选项，用空格隔开。 

###  钩子（HOOKS）

`HOOKS`设置是此文件中最重要的设置。钩子是一系列的小脚本，描述哪些东西需要加入到映像里面。有些钩子还包含了运行组件，可以提供额外的行特定动作，像启动服务、构建存储栈的块设备等。钩子按照配置文件中`HOOKS`项中给出的顺序执行。 

默认的`HOOKS`可以满足大部分简单的单硬盘系统。对于堆栈的或多块设备像 [LVM](<../zh-cn/LVM.html> "LVM"), [RAID](<../zh-cn/RAID.html> "RAID"), or [dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt") 等复杂根分区系统，请查看相应的 Wiki 页面，进行必要的进一步设置。 

####  构建时钩子

构建时钩子位于`/usr/lib/initcpio/install`，自定义的构建时钩子可能位于`/etc/initcpio/install/`。这些文件会在运行 mkinitcpio 时被包含进脚本，应该提供如下两个函数：`build` 和 `help`。`build` 函数描述了需要加入映像的模块、文件和二进制文件。mkinitcpio(8) 中的记录的 API 帮助添加这些项目。`help` 函数在钩子执行后输出描述信息。 

列出可用的钩子列表： 
    
    $ mkinitcpio -L
    
使用 mkinitcpio 的 `-H`/`--hookhelp` 选项输出对于某一钩子的帮助。例如： 
    
    $ mkinitcpio -H udev
    
####  运行时钩子

运行时钩子可以在`/usr/lib/initcpio/hooks`中找到自定义的运行时钩子在`/etc/initcpio/hooks/`。 对于任何运行时挂钩，都应该始终有一个同名的构建钩子，它会调用`add_runscript`将运行时挂钩添加到映像中。 这些文件是由早期用户空间中的BusyBox ash shell调用。除清理钩子以外（清理钩子是倒序执行的），它们始终将按照`HOOKS`设置中列出的顺序运行。 运行时钩子可能包含以下函数： 

`run_earlyhook`: 一旦挂载了API文件系统并且已经解析了内核命令行，便会运行这个函数。 通常，从此处启动早期引导过程所需的额外守护程序（例如udev，它从早期引导过程的开始就被需要）。 

`run_hook`: 这个函数在早期钩子挂接后不久便运行。 这是最常见的钩子特点，应在此处进行诸如堆叠块设备的组装之类的操作。 

`run_latehook`: 此名称的函数在挂载根设备后运行。 应当谨慎地将其用于根设备的进一步设置，或用于挂载其他文件系统，例如`/usr`。 

`run_cleanuphook`: 该名称的函数将尽可能晚地运行，并且以与配置文件的`HOOKS`数组中列出函数的相反顺序来运行。 这些钩子应该用于所有的最终清理操作，例如关闭由早期钩子启动的所有守护程序。 

**注意：** 运行时钩子仅仅被BusyBox的init使用。**systemd** 钩子触发一个 systemd 基础的初始化, 它不需要运行任何运行时钩子，而是使用systemd单元。

####  映像后处理钩子

映像后处理钩子（post hook）是位于 `/usr/lib/initcpio/post/`（软件包提供）和 `/etc/initcpio/post/`（自定义）目录下的可执行文件或 shell 脚本。这些文件会在（重新）生成映像后执行，以执行签名等附加任务。 

每个可执行文件会按以下顺序接收参数： 

  1. 使用的**内核** （某些情况下可能为空）；
  2. 生成的**initramfs 映像** 位置；
  3. （可选）生成的**统一内核映像** 位置。

此外，还会设置以下环境变量：`KERNELVERSION` 表示完整内核版本，`KERNELDESTINATION` 表示内核要想正常启动应位于的默认位置。 

####  常用钩子

下面是一个常见钩子和它们如何影响映像的创建以及运行时的次序。注意这个表格是不完整的，因为一些包会提供一些自定义的钩子。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 增加关于`hostdata`, `memdisk`, `sleep` 和`strip`的信息, 找出`dmraid`等是否在 systemd 为基础的映像中正常工作或被需要。 (在 [Talk:Mkinitcpio#Improvements for the Common hooks table and section about systemd hook](</wzh/index.php?title=Talk:Mkinitcpio&action=edit&redlink=1> "Talk:Mkinitcpio（页面不存在）") 中讨论)

BusyBox init | systemd init | [构建时钩子](<#%E6%9E%84%E5%BB%BA%E6%97%B6%E9%92%A9%E5%AD%90>) |  [运行时钩子](<#%E8%BF%90%E8%A1%8C%E6%97%B6%E9%92%A9%E5%AD%90>)（仅BusyBox init）   
---|---|---|---  
**base** | 设置所有初始目录并安装基础工具和库。除非清楚自己在做什么，否则请始终将此钩子置于首位，因为如果没有 **systemd** 钩子，该钩子是必需的，提供关键的 BusyBox init 程序。 当使用 **systemd** 钩子时，此钩子可选，仅提供一个 BusyBox 恢复 shell。启用 **base** 后，在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中临时添加 `SYSTEMD_SULOGIN_FORCE=1` 使用该 shell。  | –   
**udev** | **systemd** | 增加 udevd, udevadm,和一小套udev规则进映像。 | 从内核中启动udev守护进程和uevents过程; 创建设备节点。因为不需要用户清晰的明确出必须设备这是简化的引导过程，推荐使用。   
**usr** | 增加支持`/usr` 在独立分区。参见[#/usr 放到单独分区](<#/usr_%E6%94%BE%E5%88%B0%E5%8D%95%E7%8B%AC%E5%88%86%E5%8C%BA>) 获得更多细节。 | 在挂载真正根分区后挂载 `/usr` 分区 。   
**resume** | 添加`lzo`和`lz4`内核模块，以允许在使用编译时默认值以外的休眠映像压缩算法时恢复。添加 [systemd-hibernate-resume(8)](<https://man.archlinux.org/man/systemd-hibernate-resume.8>) 二进制文件以支持从通过 `HibernateLocation` UEFI 变量指定的休眠映像恢复。 | 试图从"suspend to disk" 状态重新开始。 参见 [休眠](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86/%E6%8C%82%E8%B5%B7%E4%B8%8E%E4%BC%91%E7%9C%A0.html#%E4%BC%91%E7%9C%A0> "电源管理/挂起与休眠") 做进一步设置。   
**btrfs** | – | 设置必备模块能够让[Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 支持Btrfs的多设备分区。需要安装 [btrfs-progs](<https://archlinux.org/packages/?name=btrfs-progs>)包 开启功能。Btrfs在单设备时此钩子不需要（`filesystems`足矣）。 | 当**udev** 钩子或**systemd** 不存在时，运行 `btrfs device scan` 组装多设备Btrfs根文件系统。安装[btrfs-progs](<https://archlinux.org/packages/?name=btrfs-progs>)包 包使用此钩子。   
**autodetect** | 系统扫描后创建设备白名单从而减少内存映像的尺寸。确定校验进入的模块正确性和完整性。为了自动侦测发挥作用，必须放在其他子系统钩子之前。放在'autodetect'钩子之前的钩子将会被完整安装。 | –   
**microcode** | 在未压缩的 initramfs 映像前添加适用于 Intel 和 AMD 处理器的早期[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "微码")更新文件。使用`/usr/lib/firmware/amd-ucode`和`/usr/lib/firmware/intel-ucode`（若可用），否则从`/boot/amd-ucode.img`和`/boot/intel-ucode.img`提取。 若在此之前 **autodetect** 钩子已调用，则只会添加对应处理器的微码更新文件。  此挂钩已经取代了弃用的`--microcode`参数和在预设文件中的`microcode`选项。这使得启动配置中微码的`initrd`参数行可以删除了，因为它们已被打包进主要的 initramfs 映像中。  | –   
**modconf** | 从`/etc/modprobe.d/`和`/usr/lib/modprobe.d/`中包含探测模块配置文件。 | –   
**kms** | 为 [KMS 早启动](<../zh-cn/Kernel_mode_setting.html#KMS_%E6%97%A9%E5%90%AF%E5%8A%A8> "Kernel mode setting")添加 GPU 模块。另外还添加了某些笔记本电脑液晶面板中内置的隐私屏幕所需的模块。 | –   
**keyboard** | 为键盘设备增加必要的模块。如果USB或串口键盘在早期用户空间起作用加入此钩子（可以输入密码或和shell交互）。有一个副作用，一些非键盘的输入设备也可能加进来，但这并不可靠。此钩子代替老的 _usbinput_ 钩子。  **注意：** 使用不同的硬件配置启动的系统（例如笔记本电脑连接外置键盘和内置键盘或[headless systems](<https://en.wikipedia.org/wiki/Headless_computer> "wikipedia:Headless computer")）时，此钩子需要放在**autodetect** 之前才能在引导中使用键盘，例如使用`encrypt`钩子解密加密设备。 | –   
**keymap** | **sd-vconsole** | 自`/etc/vconsole.conf`加入特定的 [键盘映射keymap(s)](<../zh-cn/Linux_console/Keyboard_configuration.html#Persistent_configuration> "Linux console/Keyboard configuration") 到映像。在早期用户空间如果使用[系统加密](<../zh-cn/Dm-crypt/%E5%8A%A0%E5%AF%86%E6%95%B4%E4%B8%AA%E7%B3%BB%E7%BB%9F.html> "Dm-crypt/加密整个系统"), 尤其全盘加密, 此钩子放在`encrypt`钩子之前。 | 在早期用户空间从 `/etc/vconsole.conf` 加载指定的键盘映射。   
**consolefont** | 自`/etc/vconsole.conf`中加入特定的 [终端字体](<../zh-cn/Linux_console.html#Persistent_configuration> "Linux console") 到映像。 | 在早期用户空间自`/etc/vconsole.conf`里，使用特定的终端字体。   
**block** | 加载块设备模块。若在 `autodetect` 挂钩后调用此挂钩，之添加系统中使用的块设备的模块。模块`ahci`、`sd_mod`、`usb_storage`、`uas`、`mmc_block`、`nvme`、`virtio_scsi`和`virtio_blk` 会无条件地添加 | –   
**net** | _未实现_ | 增加必要网络设备模块。必须安装 [mkinitcpio-nfs-utils](<https://archlinux.org/packages/?name=mkinitcpio-nfs-utils>)包 包, 参见 [#使用 net](<#%E4%BD%BF%E7%94%A8_net>) | 支持NFS为基础的根文件系统。   
**dmraid** | _?_ | 支持fakeRAID根设备。必须安装 [dmraid](<https://archlinux.org/packages/?name=dmraid>)包 包。注意如果你的控制器支持，更好选择是[mdadm](<../zh-cn/RAID.html> "Mdadm") 联合 **mdadm_udev** 钩子支持fakeRAID根设备。参见 [#使用 RAID 磁盘阵列](<#%E4%BD%BF%E7%94%A8_RAID_%E7%A3%81%E7%9B%98%E9%98%B5%E5%88%97>) 。 | 使用`dmraid`定位组装fakeRAID块设备。   
**mdadm_udev** | 通过udev支持组装RAID阵列。必须安装 [mdadm](<https://archlinux.org/packages/?name=mdadm>)包 包。若在FakeRAID使用这个钩子推荐将 `mdmon` 加入 `BINARIES`. 参见 [#使用 RAID 磁盘阵列](<#%E4%BD%BF%E7%94%A8_RAID_%E7%A3%81%E7%9B%98%E9%98%B5%E5%88%97>) 。 | –   
**encrypt** | **sd-encrypt** | 增加`dm_crypt` 内核模块 和 `cryptsetup` 工具到映像。 必须安装[cryptsetup](<https://archlinux.org/packages/?name=cryptsetup>)包包。  **注意：** 启动时反复确认 _keyboard_ 钩子放在解密设备前面。和/或当使用钥匙文件解锁时，存放钥匙文件的文件系统加入[#模块（MODULES）](<#%E6%A8%A1%E5%9D%97%EF%BC%88MODULES%EF%BC%89>) 里。 | 侦测和解锁加密根系统。参见 [#运行时配置](<#%E8%BF%90%E8%A1%8C%E6%97%B6%E9%85%8D%E7%BD%AE>) 。 **sd-encrypt** 参见 [dm-crypt/系统配置#使用systemd-cryptsetup-generator](<../zh-cn/Dm-crypt/%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE.html#%E4%BD%BF%E7%94%A8systemd-cryptsetup-generator> "Dm-crypt/系统配置")。   
**lvm2** | 加入设备映射内核模块和`lvm` 工具到映像。 必须安装[lvm2](<https://archlinux.org/packages/?name=lvm2>)包 包。 如果根系统在[LVM](<../zh-cn/LVM.html> "LVM")这是必须的钩子。 | –   
**fsck** | 增加fsck二进制文件和特定系统帮助文件，允许fsck在挂载前处理根系统（和/usr分区如果有）。如果放在**autodetect** 钩子前仅仅加载的定的帮助文件到根系统。强烈推荐使用此钩子，独立`/usr`分区需要它。强烈建议如果使用的此钩子同时要加入必要模块保证键盘在早期用户空间使用。 使用这个钩子需要在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")加入 `rw` 参数（[讨论](<https://bbs.archlinux.org/viewtopic.php?pid=1307895#p1307895>)）。参见 [fsck#启动时检查](<../zh-cn/Fsck.html#%E5%90%AF%E5%8A%A8%E6%97%B6%E6%A3%80%E6%9F%A5> "Fsck")。  | –   
**filesystems** | 除非在`MODULES`中加入了文件系统，不然此钩子是必须的。 | –   
**acpi_override** | 从 `/usr/initcpio/acpi_override/` 和 `/etc/initcpio/acpi_override/` 添加 ACPI 机器语言文件（ _.aml_ ）到早期未压缩的 initramfs 映像中，使得内核可以在启动早期重载 ACPI 表（比如 [DSDT](<../zh-cn/DSDT.html> "DSDT")）[[1]](<https://docs.kernel.org/admin-guide/acpi/initrd_table_override.html>) | –   
  
###  压缩方式(COMPRESSION)

内核支持几种initramfs的压缩方式 - [gzip](<https://archlinux.org/packages/?name=gzip>)包, [bzip2](<https://archlinux.org/packages/?name=bzip2>)包, lzma, [xz](<https://archlinux.org/packages/?name=xz>)包, [lzo](<https://archlinux.org/packages/?name=lzo>)包, [lz4](<https://archlinux.org/packages/?name=lz4>)包 and [zstd](<https://archlinux.org/packages/?name=zstd>)包。mkinitcpio默认使用zstd压缩映像，注意zstd运行的多线程模式（使用了`-T0`选项，以侦测到内核数量作为线程数量。） 

系统中的 `mkinitcpio.conf` 已经注释掉了各种 `COMPRESSION` 选项，要使用某个压缩方式，请取消前面的注释，并确认安装了相应的压缩工具包。不指定 `COMPRESSION` 选项会使用 zstd 压缩的 initramfs 文件。想要创建一个未压缩的映像，在配置中指定`COMPRESSION=cat` 或者在命令行使用 `-z cat`。 

**提示：** lz4 在高压缩率模式(`-9`)下映像有2.5的压缩比率，以付出最慢的单线程压缩速度为代价，可以获得最快的解压缩速度。lzo使用轻度较好的压缩模式后仍然有较快的解压速度。 zstd 提供多样解决方案, 通过参数使用多线程压缩方式和大范围压缩水平，参见 [zstd(1) § Operation modifiers](<https://man.archlinux.org/man/zstd.1#Operation_modifiers>)。 xz在其高压缩预设(`-9`)中以大约5的缩减因子实现了最小的体积，但代价是解压速度要慢得多。

###  压缩选项(COMPRESSION_OPTIONS)

还有一些额外的标准可以传递到 `COMPRESSION` 指定的程序，例如： 
    
    COMPRESSION_OPTIONS='-9'
    
这个选项可以留空， _mkinitcpio_ 会确保任何支持的压缩方法有必要的标志来产生一个可以工作的映像。 

**警告：** 使用错误的参数选项可能导致**内核不能引导** ，因为错误参数导致内核不能解压生成的压缩档。

使用默认的 zstd 压缩时，`--long`选项在节省自定义内核的空间（特别是在使用 EFI 系统分区作为`/boot`时的[双系统](<../zh-cn/Dual_boot_with_Windows.html> "Dual boot with Windows")设置）非常有效。但是，内存有限的系统可能无法使用此选项解压缩 initramfs。还可能需要`-v` 选项来查看 initramfs 生成期间的详细信息。例如： 
    
    COMPRESSION="zstd"
    COMPRESSION_OPTIONS=(-v -5 --long)
    
通过使用 xz 的 `-9e` 压缩级别并解压可加载内核模块和固件，可以实现最高（但最慢）的压缩： 
    
    COMPRESSION="xz"
    COMPRESSION_OPTIONS=(-9e)
    MODULES_DECOMPRESS="yes"
    
###  模块解压缩(MODULES_DECOMPRESS)

`MODULES_DECOMPRESS` 控制内核模块与固件文件是否在 initramfs 创建时解压缩。默认为 `no`。 

Arch 使用 19 级 zstd 压缩[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")模块和 [linux-firmware](<https://archlinux.org/packages/?name=linux-firmware>)包。 当为 initramfs 使用更高的压缩等级，设置`MODULES_DECOMPRESS="yes"` 可以更大幅度地减少 initramfs 的大小。这会导致在早期启动阶段更高的内存和 CPU 占用，对于内存有限、CPU 性能不足的系统有影响，因为内核将花费更多的时间来解压缩整个 initramfs 映像，而不是加载单个模块和固件时解压缩它们。 

**提示：** 在 initramfs 生成过程接近结束时，所有剩余的 _.bz2_ 、 _.gz_ 、 _.lz4_ 、 _.lzma_ 、 _.lzo_ 、 _.xz_ 和 _.zst_ 文件被移动到早期未压缩的 initramfs 映像以避免双重压缩。

##  运行时配置

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 哪个选项可以在 `systemd` 钩子工作， 哪个只能在 `base`-only? (在 [Talk:Mkinitcpio](<../zh-cn/Talk:Mkinitcpio.html>) 中讨论)

。 

运行时配置选项可以通过内核命令行传递到 `init` 以及某些钩子。内核命令行参数通常是由启动引导器提供。下面讨论的参数可以附加到内核命令行以改变默认行为。参见 [Arch 启动过程](<../zh-cn/Arch_boot_process.html> "Arch boot process")和[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")以获取更多信息。 

###  从基本钩子启动

`root=`
    这是内核命令行中指定的最重要的参数，因为它决定了哪一个设备会被挂载为你的正确的 root 设备。mkinitcpio 允许不同的格式，详见[Persistent_block_device_naming#Kernel_parameters](<../zh-cn/Persistent_block_device_naming.html#Kernel_parameters> "Persistent block device naming")

**注意：** 下面的选项会改变 `init` 在 initramfs 环境中的默认行为。参见 `/lib/initcpio/init` 获取更多信息。但当启用`systemd`钩子时，这些参数不起作用，因为来自`base`钩子的 `init` 被取代了。

`break`
    如果`break` 或者 `break=premount` 被指定，`init` 会暂停启动过程（在加载钩子之后，但是在挂载根文件系统之前）然后启动一个交互式终端，一般用来排障。如果指定为`break=postmount`，这个终端会在根目录挂载后启动。退出这个 shell 之后可以继续正常的启动流程。

`disablehooks=`
    在运行时可以通过添加 `disablehooks=hook1{,hook2,...}` 禁用某些钩子。例如
    
    disablehooks=resume

`earlymodules=`
    改变模块加载的顺序。可以通过 `earlymodules=mod1{,mod2,...}` 指定一些模块提前加载。 (例如，这可以用来确保多个网络接口的正确顺序。)

参见: [常规故障排除#系统启动问题](<../zh-cn/%E5%B8%B8%E8%A7%84%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html#%E7%B3%BB%E7%BB%9F%E5%90%AF%E5%8A%A8%E9%97%AE%E9%A2%98> "常规故障排除")和 [mkinitcpio(8)](<https://man.archlinux.org/man/mkinitcpio.8>)。 

###  使用 RAID 磁盘阵列

参见 [RAID#Configure mkinitcpio](<../zh-cn/RAID.html#Configure_mkinitcpio> "RAID")。 

###  使用 net

**警告：** NFSv4 仍然不被支持 [FS#28287](<https://bugs.archlinux.org/task/28287>)。

**必须的包**

`net` 需要 [mkinitcpio-nfs-utils](<https://archlinux.org/packages/?name=mkinitcpio-nfs-utils>)包 包。 

**内核参数**
    
    [内核文档](<https://docs.kernel.org/admin-guide/nfs/nfsroot.html>)包含最新的信息和清晰的说明。
    
**ip=**

这个参数告诉内核怎样生成设备IP地址和怎样安装路由表。它最多可选9个参数： `ip=<client-ip>:<server-ip>:<gw-ip>:<netmask>:<hostname>:<device>:<autoconf>:<dns0-ip>:<dns1-ip>:<ntp0-ip>`。 

如果这些参数在内核命令行缺失，所有区域将被认为是空白，则根据 [kernel documentation](<https://docs.kernel.org/admin-guide/nfs/nfsroot.html>) 使用默认参数。通常这就意味这内核利用自动配置表来配置。 

`<autoconf>` 参数单独作为 `ip` 的值出现 (没有上面提及的任一参数)。如果值是 `ip=off` 或 `ip=none`, 将不会执行自动配置，否则会执行自动配置。最常见的是`ip=dhcp`. 

获取参数具体说明，参见 [kernel documentation](<https://docs.kernel.org/admin-guide/nfs/nfsroot.html>). 

_例子：_
    
     ip=127.0.0.1:::::lo:none  --> 启用 loopback 接口。
     ip=192.168.1.1:::::eth2:none --> 启用静态 eth2 接口。
     ip=:::::eth0:dhcp --> 为 eth0 启用 dhcp。
    
**注意：** 请确保使用内核设备命名 (例如 _eth0_) 作为 `<device>` 参数, 不要使用 [网络配置#Network interfaces](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#Network_interfaces> "网络配置") 命名 (例如 _enp2s0_) 因为这个不起作用。

**BOOTIF=** 使用多个网卡的时候，此参数可以指定要使用网卡的 Mac 地址。在接口号可能变化或与 IPAPPEND 2 、IPAPPEND 3 选项共用时比较有用。默认使用 eth0. 

示例： 
    
    BOOTIF=01-A1-B2-C3-D4-E5-F6  # 注意前缀加"01-" 并且字母要大写。
    
**nfsroot=**

如果命令行中没有给出 `nfsroot` 参数，那么默认的 `/tftpboot/%s` 会被使用。 
    
     nfsroot=[<server-ip>:]<root-dir>[,<nfs-options>]
    
运行`mkinitcpio -H net` 查看参数详细解释。 

###  使用 lvm

如果你的根分区在 [LVM](<../zh-cn/LVM.html> "LVM")文件系统中, 参见 [Install Arch Linux on LVM#Adding mkinitcpio hooks](<https://wiki.archlinux.org/title/Install_Arch_Linux_on_LVM#Adding_mkinitcpio_hooks>). 

###  使用加密根目录

如果使用[加密根目录](<https://wiki.archlinux.org/title/Dm-crypt/Encrypting_an_entire_system>)，请参考 [Dm-crypt/System configuration#mkinitcpio](<https://wiki.archlinux.org/title/Dm-crypt/System_configuration#mkinitcpio>)。 

###  /usr 放到单独分区

如果将 /usr 放在单独分区，必须满足： 

  * 添加 `fsck` 钩子, `/usr`在`/etc/fstab`分区表中的`passno` 参数设置为`2` ，以便启动时检查该分区。作为常规推荐 如果想要`/usr`分区可以在启动时被检查，以上设置是中肯的。没有这个钩子 `/usr` 永远不能被检查（fsck）。

  * 如果没使用systemd钩子，请添加`usr`钩子。这样将会在挂载根系统后挂载`/usr` 分区。

##  提示与技巧

###  生成 fallback initramfs 映像

自 mkinitcpio 版本 40 起，默认不生成 fallback initramfs 映像。若需要启用： 

  * 调整 `/etc/mkinitcpio.d/` 目录下相应的 **.preset** 文件： 
    * 注释掉 `PRESETS=('default')` 行，并取消注释 `PRESETS=('default' 'fallback')` 行
    * 取消注释 `fallback_image="/boot/initramfs-linux-fallback.img"`
    * 取消注释 `fallback_options="-S autodetect"`
  * 重新生成 initramfs。
  * 更新[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")配置。

**警告：** 缺少后备 initramfs 可能会使您在默认 initramfs 启动失败时，失去另一个启动系统的选项。请务必手头准备一个可启动的[安装介质](</wzh/index.php?title=USB_%E9%97%AA%E5%AD%98%E5%AE%89%E8%A3%85%E4%BB%8B%E8%B4%A8&action=edit&redlink=1> "USB 闪存安装介质（页面不存在）")以备救援之用。

##  疑难解答

###  解压缩映像

如果你对 initrd 映像的内容感到好奇，你可以解压缩它然后看看里面的文件。 

initrd 映像是一个 SVR4 CPIO 压缩包，通过 `find` 和 `bsdcpio` 命令生成，利用可被内核理解的压缩方式被有选择的压缩，参考[#压缩方式(COMPRESSION)](<#%E5%8E%8B%E7%BC%A9%E6%96%B9%E5%BC%8F\(COMPRESSION\)>)。 

mkinitcpio 包含了一个叫做 [lsinitcpio(1)](<https://man.archlinux.org/man/lsinitcpio.1>) 的工具，可以列出和/或解压缩出 initramfs 映像的内容。 

你可以用下面的命令列出映像中的文件： 
    
    # lsinitcpio /boot/initramfs-linux.img
    
然后全部解压缩到当前文件夹： 
    
    # lsinitcpio -x /boot/initramfs-linux.img
    
你也可以用更对人类友好的方式列出映像中的重要的部分： 
    
    # lsinitcpio -a /boot/initramfs-linux.img
    
###  重新压缩解压之后修改过的映像

激活`/usr/bin/mkinitcpio`脚本的 `build_image` 功能使用此参数： 
    
    build_image _outfile_ _compression_
    
将会产生一个拥有`build_image`功能的新脚本，用上面的参数运行它（ _outfile_ 输出文件名字， _compression_ 压缩工具），将会把当前目录下的内容压缩到一个名字为` _outfile_`的新文件里。 

**警告：** 建议在运行上面的命令产生一个新的`/boot/initramfs-linux.img`之前把现有的映像重命名作为备份，以便情况不妙时有后悔药吃。如果因为失误导致系统无法启动，你需要用fallback映像或者boot CD启动，然后运行mkinitcpio来overwrite掉之前做的更改，或者你自己修好它然后重新压缩映像。

###  "/dev must be mounted" when it already is

_mkinitcpio_ 使用这个检测通过判断`/dev/fd/` 是否存在来判断`/dev`是否被挂载。如果其他一切看起来都很好，可以通过以下方式手动“创建”： 
    
    # ln -s /proc/self/fd /dev/
    
(显然, `/proc` 必须被安装. _mkinitcpio_ 无论如何要求这样,指示它要检测的下一件事。) 

### Possibly missing firmware for module XXXX

当内核更新后，initramfs映像被重新构建时，你可能得到以下警告： 
    
    ==> WARNING: Possibly missing firmware for module: wd719x
    ==> WARNING: Possibly missing firmware for module: aic94xx
    ==> WARNING: Possibly missing firmware for module: xhci_pci
    
如果产生 _default_ 映像时出现这些或相近的信息，那么按照警告要求安装额外的被需要的固件。绝大部分固件通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")安装 [linux-firmware](<https://archlinux.org/packages/?name=linux-firmware>)包包获得。其他提供固件的包可以查看下表或在[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")或 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中搜索固件模块名字。 

除此以外，警告信息只出现在 _fallback_ 映像生成时，可以按照下面的建议来： 

  * 如果不需要使用缺失模块的硬件，可以安全地忽略这些警告。
  * 如果想要消除这些警告，安装缺失的固件，元包 [mkinitcpio-firmware](<https://aur.archlinux.org/packages/mkinitcpio-firmware/>)AUR 包括绝大部分可选的固件。也可以手动安装需要的包：

     模块 | 包   
---|---  
aic94xx |  [aic94xx-firmware](<https://aur.archlinux.org/packages/aic94xx-firmware/>)AUR  
ast  |  [ast-firmware](<https://aur.archlinux.org/packages/ast-firmware/>)AUR  
bfa |  [linux-firmware-qlogic](<https://archlinux.org/packages/?name=linux-firmware-qlogic>)包  
bnx2x |  [linux-firmware-broadcom](<https://archlinux.org/packages/?name=linux-firmware-broadcom>)包  
liquidio |  [linux-firmware-liquidio](<https://archlinux.org/packages/?name=linux-firmware-liquidio>)包  
mlxsw_spectrum |  [linux-firmware-mellanox](<https://archlinux.org/packages/?name=linux-firmware-mellanox>)包  
nfp |  [linux-firmware-nfp](<https://archlinux.org/packages/?name=linux-firmware-nfp>)包  
qat_420xx |  [linux-firmware-intel](<https://archlinux.org/packages/?name=linux-firmware-intel>)包  
qed |  [linux-firmware-qlogic](<https://archlinux.org/packages/?name=linux-firmware-qlogic>)包  
qla1280 |  [linux-firmware-qlogic](<https://archlinux.org/packages/?name=linux-firmware-qlogic>)包  
qla2xxx |  [linux-firmware-qlogic](<https://archlinux.org/packages/?name=linux-firmware-qlogic>)包  
wd719x |  [wd719x-firmware](<https://aur.archlinux.org/packages/wd719x-firmware/>)AUR  
xhci_pci  
xhci_pci_renesas |  [upd72020x-fw](<https://aur.archlinux.org/packages/upd72020x-fw/>)AUR  
  
如果想去掉警告，但不想浪费磁盘空间在不需要的固件包上，可以禁用 [#生成 fallback initramfs 映像](<#%E7%94%9F%E6%88%90_fallback_initramfs_%E6%98%A0%E5%83%8F>)。 

对于不可用的固件，也可以通过创建占位文件来抑制警告，例如： 
    
    # echo "设备不可用" > /usr/lib/firmware/qat_420xx.bin
    # echo "设备不可用" > /usr/lib/firmware/qat_420xx_mmp.bin
    
###  没有发现 PS/2 控制器

在一些主板（主要是早期的但是也有一些新的主板）， i8042 控制器不能被自动侦测到。这很罕见，但是一些人确定没有键盘使用。 可以提前侦测到这种情况。PS/2 接口得到 `i8042: PNP: No PS/2 controller found. Probing ports directly` 信息，加 **atkbd** 到 `MODULES` 数组。 

###  标准急救过程

使用不正确的初始化内存映像盘经常出现不可引导。因此遵守以下的系统急救过程： 

####  在一台机器引导成功，但在另一台引导失败

在主要映像 initramfs 扫描 `/sys` 时 _mkinitcpio_ 的 `autodetect` 钩子 过滤掉了 [kernel modules](<../zh-cn/Kernel_modules.html> "Kernel modules") ，这些模块在启动被调用。 如果转移`/boot` 目录到其他机器，在早期用户空间造成启动失败，原因是新的硬件由于缺失内核模块不能被侦测到。注意USB 2.0 和 3.0 需要不同的模块。 

修正这个缺陷，首先试着从引导记录[bootloader](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "Bootloader") 中选择 [fallback](<#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E6%98%A0%E5%83%8F>) 映像 ，因为这个映像不使用`autodetect`过滤模块。 一旦引导成功，在新机器上运行 _mkinitcpio_ 用正确的模块重建主要映像。如果fallback映像失败，试着用 Arch Linux live CD/USB，使用 arch-chroot 进入系统中, 在新机器上运行 _mkinitcpio_ 。最后的手段，手工增加模块到[#MODULES|手动]]映像中。 

###  无法访问控制台，root 用户被锁定

`systemd` 钩子[会禁用 root 用户](<https://gitlab.archlinux.org/archlinux/packaging/packages/systemd/-/commit/292cdf8a2f7dd7c6c7d91d2b59617391935c837c>)。要启用紧急 shell，请临时在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中添加 `SYSTEMD_SULOGIN_FORCE=1`。 

或者，也可以使用 [initcpio-hook-shadowcopy](<https://aur.archlinux.org/packages/initcpio-hook-shadowcopy/>)AUR。安装后，在 `/etc/mkinitcpio.conf` 中将 `shadowcopy` 钩子置于 `systemd` 之后，并使用 `mkinitcpio -P` 重新生成 initramfs。更多文档请参见其 [GitHub 仓库](<https://github.com/iTrooz/initcpio-hook-shadowcopy>)。 

##  另见

  * Linux Kernel documentation on [initramfs, "What is rootfs?"](<https://docs.kernel.org/filesystems/ramfs-rootfs-initramfs.html#what-is-rootfs>)
  * Linux Kernel documentation on [initrd](<https://docs.kernel.org/admin-guide/initrd.html>)
  * Wikipedia article on [initrd](<https://en.wikipedia.org/wiki/initrd> "wikipedia:initrd")
