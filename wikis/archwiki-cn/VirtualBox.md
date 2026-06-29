**翻译状态：**

  * 本文（或部分内容）译自 [VirtualBox](<https://wiki.archlinux.org/title/VirtualBox> "arch:VirtualBox")，最近一次同步于 2026-02-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/VirtualBox?diff=0&oldid=862949>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/VirtualBox_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [/在虚拟机中安装 Arch Linux](<../zh-cn/VirtualBox/%E5%9C%A8%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%E5%AE%89%E8%A3%85_Arch_Linux.html> "VirtualBox/在虚拟机中安装 Arch Linux")
  * [Moving an existing install into (or out of) a virtual machine](</wzh/index.php?title=Moving_an_existing_install_into_\(or_out_of\)_a_virtual_machine&action=edit&redlink=1> "Moving an existing install into \(or out of\) a virtual machine（页面不存在）")
  * [PhpVirtualBox](</wzh/index.php?title=PhpVirtualBox&action=edit&redlink=1> "PhpVirtualBox（页面不存在）")
  * [RemoteBox](</wzh/index.php?title=RemoteBox&action=edit&redlink=1> "RemoteBox（页面不存在）")

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:VirtualBox#](<../zh-cn/Talk:VirtualBox.html>) 中讨论）

[VirtualBox](<https://zh.wikipedia.org/wiki/VirtualBox> "zhwp:VirtualBox") 是运行于现有操作系统之上的[虚拟机监视器](<https://zh.wikipedia.org/wiki/Hypervisor> "zhwp:Hypervisor")，用途是在特制环境（即[虚拟机](<https://zh.wikipedia.org/wiki/%E8%99%9A%E6%8B%9F%E6%9C%BA> "zhwp:虚拟机")）里运行操作系统。[VirtualBox](<https://www.virtualbox.org>) 处于活跃开发状态，时常会引入新功能。VirtualBox 支持使用 [Qt](<../zh-cn/Qt.html> "Qt") 图形界面，以及在[无界面](<https://zh.wikipedia.org/wiki/%E6%97%A0%E5%A4%B4%E8%BD%AF%E4%BB%B6> "zhwp:无头软件")模式下搭配 [SDL](<https://zh.wikipedia.org/wiki/SDL> "zhwp:SDL") 命令行工具运行和管理虚拟机。 

为了实现某些主-客户机间的整合功能，例如共享目录与剪贴板、显卡加速渲染、无缝窗口整合，VirtualBox 为部分操作系统提供了[客户机插件](<#%E5%AE%A2%E6%88%B7%E6%9C%BA%E6%8F%92%E4%BB%B6>)。 

更多信息请参考 [官方文档](<https://docs.oracle.com/en/virtualization/virtualbox/>)。 

##  在 Arch 里安装 VirtualBox

参考以下步骤在 Arch 主机系统中安装 VirtualBox。 

###  安装基本软件包

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [virtualbox](<https://archlinux.org/packages/?name=virtualbox>)包，并安装以下内核模块之一： 

  * 对于 [linux](<https://archlinux.org/packages/?name=linux>)包 内核，使用 [virtualbox-host-modules-arch](<https://archlinux.org/packages/?name=virtualbox-host-modules-arch>)包
  * 对于 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 内核，使用 [virtualbox-host-modules-lts](<https://archlinux.org/packages/?name=virtualbox-host-modules-lts>)包
  * 对于其它[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")，使用 [virtualbox-host-dkms](<https://archlinux.org/packages/?name=virtualbox-host-dkms>)包

为了编译 [virtualbox-host-dkms](<https://archlinux.org/packages/?name=virtualbox-host-dkms>)包 提供的 VirtualBox 内核模块，还需要安装你使用的内核所对应的头文件包（如 [linux-rt](<https://archlinux.org/packages/?name=linux-rt>)包 需安装 [linux-rt-headers](<https://archlinux.org/packages/?name=linux-rt-headers>)包）。[[1]](<https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/message/X6D3UNFV6TXYYNF74ES2AX5ETREAIBCG/>) 当 VirtualBox 或内核更新的时候，[DKMS](<../zh-cn/DKMS.html> "DKMS") 的 [pacman 钩子](<../zh-cn/Pacman_%E9%92%A9%E5%AD%90.html> "Pacman 钩子")会自动重新编译内核模块。 

###  模块签名

如果你的 Linux 内核是自行编译的，并启用了 `CONFIG_MODULE_SIG_FORCE` 选项，那么你需要用编译内核时所使用的密钥为所有模块签名。 

可以用根用户（root）身份执行以下命令来为模块进行签名： 
    
    # find "/lib/modules/$(uname -r)/" '(' -name 'vboxdrv.ko*' -o -name 'vboxnetadp.ko*' -o -name 'vboxnetflt.ko*' ')' -exec /lib/modules/$(uname -r)/build/scripts/sign-file sha256 /lib/modules/$(uname -r)/build/certs/signing_key.pem /lib/modules/$(uname -r)/build/certs/signing_key.x509 {} ';'
    
**注意：** 哈希算法不必与配置时选择的算法相匹配，但必须已被编译进内核。

If you experience an error such as the following: 
    
    At main.c:171:
    - SSL error:FFFFFFFF80000002:system library::No such file or directory: crypto/bio/bss_file.c:67
    - SSL error:10000080:BIO routines::no such file: crypto/bio/bss_file.c:75
    sign-file: certs/signing_key.pem
    
Then run the command `cd /lib/modules/$(uname -r)/build` to navigate to your kernel tree folder and check if the `certs` folder actually has a `signing_key.pem` file. If not, create a file somewhere on your system (does not have to be in the kernel tree folder) named `x509.genkey` with the following contents (based on [Gentoo:Signed kernel module support#Building the kernel with proper keys](<https://wiki.gentoo.org/wiki/Signed_kernel_module_support#Building_the_kernel_with_proper_keys> "gentoo:Signed kernel module support")): 
    
    [ req ]
    default_bits = 4096
    distinguished_name = req_distinguished_name
    prompt = no
    string_mask = utf8only
    x509_extensions = myexts
    
    [ req_distinguished_name ]
    CN = Modules
    
    [ myexts ]
    basicConstraints=critical,CA:FALSE
    keyUsage=digitalSignature
    subjectKeyIdentifier=hash
    authorityKeyIdentifier=keyid

Then run `openssl req -new -nodes -utf8 -sha512 -days 36500 -batch -x509 -config x509.genkey -outform DER -out signing_key.x509 -keyout signing_key.pem` in the directory you created the `x509.genkey` file and move the resulting files to the `certs` directory in the kernel tree folder, then run `mokutil --import signing_key.x509` as root. You should then be able to rerun the signing command without an error. 

If this still does not work, try updating your kernel to a newer version that has signing files already available (most kernel packages should), or if you are [compiling your own](<../zh-cn/%E5%86%85%E6%A0%B8.html#Compilation> "Kernel"), make sure that you copy the `src/(kernel version)/certs/signing_key.x509` and `src/(kernel version)/certs/signing_key.pem` from the folder you are building the kernel with to the `/lib/modules/$(uname -r)/build/certs` directory after you have built the kernel and are running it. 

###  加载 VirtualBox 内核模块

[virtualbox-host-modules-arch](<https://archlinux.org/packages/?name=virtualbox-host-modules-arch>)包 和 [virtualbox-host-dkms](<https://archlinux.org/packages/?name=virtualbox-host-dkms>)包 使用 `systemd-modules-load.service` 在启动时自动加载 VirtualBox 的内核模块。若要在安装之后立即加载模块，可以手动加载一次，或者干脆重启。可以从 `/usr/lib/modules-load.d/virtualbox-host-modules-arch.conf`，`/usr/lib/modules-load.d/virtualbox-host-modules-lts.conf` 或 `/usr/lib/modules-load.d/virtualbox-host-dkms.conf` 中查看加载的模块列表。 

**注意：** 如果希望启动时不自动加载 VirtualBox 模块，需要将默认的 `/usr/lib/modules-load.d/virtualbox-host-modules-arch.conf`，`/usr/lib/modules-load.d/virtualbox-host-modules-lts.conf` 或 `/usr/lib/modules-load.d/virtualbox-host-dkms.conf` 配置文件屏蔽掉，具体做法是在 `/etc/modules-load.d/` 目录里创建同名的空文件，或是创建同名并链接到 `/dev/null` 的符号链接。

在 VirtualBox 所使用的[内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")中，只有 `vboxdrv` 是必须的。该模块必须在虚拟机运行之前加载。 

手动加载模块的命令是： 
    
    # modprobe vboxdrv
    
以下模块仅用于高级功能： 

  * `vboxnetadp` 和 `vboxnetflt`：这两个模块在使用[桥接网络](<https://www.virtualbox.org/manual/ch06.html#network_bridged>)或[仅主机网络](<https://www.virtualbox.org/manual/ch06.html#network_hostonly>)功能时，都是需要的。具体来说，`vboxnetadp` 模块用于在 VirtualBox 全局配置里创建主机虚拟网卡；`vboxnetflt` 模块会在启动使用了该网卡的虚拟机时用到。

**注意：** 如果在 VirtualBox 内核模块运行期间你更新了模块（所属的软件包），为了使用新版本，你需要手动重新加载这些模块。在 root 权限下运行 `vboxreload` 即可重新加载。

###  从客机系统访问主机 USB 设备

要让虚拟机访问主机的 USB 端口，需将允许使用该功能的用户添加到 `vboxusers` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")中。 

###  客户机插件

建议在运行 VirtualBox 的主机系统上安装 [virtualbox-guest-iso](<https://archlinux.org/packages/?name=virtualbox-guest-iso>)包 软件包。这个包里有个 `.iso` 镜像文件，用来为 Arch 之外的客户机系统安装插件。镜像文件的位置在 `/usr/lib/virtualbox/additions/VBoxGuestAdditions.iso`，手动在虚拟机的虚拟光驱里加载这个文件之后，即可在客户机里安装插件。对于 Arch Linux 客户机，请一并参考 [/在虚拟机中安装 Arch Linux#安装客户机插件](<../zh-cn/VirtualBox/%E5%9C%A8%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%E5%AE%89%E8%A3%85_Arch_Linux.html#%E5%AE%89%E8%A3%85%E5%AE%A2%E6%88%B7%E6%9C%BA%E6%8F%92%E4%BB%B6> "VirtualBox/在虚拟机中安装 Arch Linux")

###  扩展包

_Oracle VM VirtualBox Extension Pack_ 为虚拟机提供了[额外功能](<https://www.virtualbox.org/manual/ch01.html#intro-installing>)。但它并不是以自由软件协议发布的， _仅供个人使用_ 。这些扩展包可以从 [virtualbox-ext-oracle](<https://aur.archlinux.org/packages/virtualbox-ext-oracle/>)AUR 安装，也可以从 [seblu](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#seblu> "非官方用户仓库") 仓库安装编译好的版本。 

如果你喜欢使用传统的手动方法来安装扩展包，可以手动下载扩展包，然后通过 GUI 进行安装（ _File > Tools > Extension Pack Manager_），也可以在命令行中执行 `VBoxManage extpack install _<.vbox-extpack>_`。确保你有类似 [Polkit](<../zh-cn/Polkit.html> "Polkit") 的工具来在安装时为 VirtualBox 授予 [root 权限](<https://www.virtualbox.org/ticket/8473>)。 

You can also install the [extension pack](<https://www.virtualbox.org/wiki/Downloads>) without using Polkit via the following command: 
    
    # vboxmanage extpack install _path-to-extension-pack_
    
One of the non-free extension pack features is support for the Remote Desktop Protocol (RDP). This part of functionality can also be obtained with the open source _VNC Extension Pack_ , by installing the [virtualbox-ext-vnc](<https://archlinux.org/packages/?name=virtualbox-ext-vnc>)包 package. 

###  前端

VirtualBox 自带四个前端： 

  * 如果你想通过常规 GUI 使用 VirtualBox，使用 `VirtualBox` 命令来启动 VirtualBox。
  * 如果你想在命令行下启动与管理 VirtualBox，可以使用 `VBoxSDL` 命令。从 VBoxSDL 启动的虚拟机，其窗口仅包含虚拟机的画面，没有菜单或是其他控制项。
  * 如果你想在使用 VirtualBox 不使用任何 GUI（例如在服务器上），使用 `VBoxHeadless` 命令。这时可以通过 VRDP 扩展来远程访问虚拟机的图形界面。
  * If you want to remotely manage virtual machines, the _VirtualBox web service_ (`vboxwebsrv`) provides the server side backend. It can be used with [RemoteBox](</wzh/index.php?title=RemoteBox&action=edit&redlink=1> "RemoteBox（页面不存在）") (GUI) or [phpVirtualBox](</wzh/index.php?title=PhpVirtualBox&action=edit&redlink=1> "PhpVirtualBox（页面不存在）") (WebUI).

Refer to the [VirtualBox manual](<https://www.virtualbox.org/manual>) to learn how to create virtual machines. 

**警告：** If you intend to store virtual disk images on a [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") file system, before creating any images, you should consider disabling [copy-on-write](<../zh-cn/Btrfs.html#Copy-on-Write_\(CoW\)> "Btrfs") for the destination directory of these images.

A security feature in Wayland (i.e. when using GDM) disallows VirtualBox to grab all keyboard input. This is annoying when you want to pass window manager shortcuts to your guest operating system. It can be bypassed by whitelisting VirtualBox: 
    
    $ gsettings get org.gnome.mutter.wayland xwayland-grab-access-rules
    $ gsettings set org.gnome.mutter.wayland xwayland-grab-access-rules "['VirtualBox Machine']"
    
The first command will show if any other applications are already whitelisted. If so, add _VirtualBox Machine_ to that list, rather than having it as the only one. 

##  在 VirtualBox 中安装 Arch Linux

请参阅 [/在虚拟机中安装 Arch Linux](<../zh-cn/VirtualBox/%E5%9C%A8%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%E5%AE%89%E8%A3%85_Arch_Linux.html> "VirtualBox/在虚拟机中安装 Arch Linux")。 

##  虚拟磁盘管理

另请参阅 [#Import/export VirtualBox virtual machines from/to other hypervisors](<#Import/export_VirtualBox_virtual_machines_from/to_other_hypervisors>)。 

###  VirtualBox 支持的格式

VirtualBox 支持下列虚拟硬盘格式： 

  * **VDI** : Virtual Disk Image 格式是 VirtualBox 新建虚拟机时默认选用的格式，也是 VirtualBox 自有的开放容器格式。

  * **VMDK** : Virtual Machine Disk 最初是由 VMware 为其产品研发的格式。该格式技术设计文档最初是闭源的，而现在已经开源，在 VirtualBox 里完全可用。这种格式有个功能是：把一个虚拟机的虚拟硬盘分割成多个 2GB 大小的文件。如果你要把虚拟机镜像放在不支持大文件的文件系统（例如 FAT32）上，那么这个功能就非常有用。在其它的虚拟磁盘格式里，能做到同样功能的只有 Parallels 的 HDD。

  * **VHD** : Virtual Hard Disk 是 Microsoft 为 Windows Virtual PC 与 Hyper-V 研发的格式。如果你想把虚拟机部署到这些平台上，那么你只能用这种格式。

**提示：** Windows 7 开始可以直接挂载 VHD 文件进行读写，不需要额外安装软件。

  * **VHDX** (只读): 这是由 Microsoft 研发的 Virtual Hard Disk 格式的加强版。于 2012-09-04 与 Hyper-V 3.0 同步发布，二者都是 Windows Server 2012 的功能。该加强版的改进包括性能优化（源于区块对齐），支持大区块单位，还有应对断电的磁盘日志。VirtualBox [支持该格式的只读访问](<https://www.virtualbox.org/manual/ch15.html#idp63002176>)。

  * **HDD** (V2): HDD 格式是由 Parallels Inc 研发的，由他们的虚拟机方案（如 Parallels Desktop for Mac）所使用。该格式的新版（v3 和 v4）由于缺少文档，又是专有格式，未能被 VirtualBox 支持。

**注意：** 关于该格式“仅支持 V2 版”的说法目前有争议。VirtualBox 官方手册 [声称只支持 V2 版](<https://www.virtualbox.org/manual/ch05.html#vdidetails>)，但 Wikipedia 上的说法是 [V1 版也能正常工作](<https://en.wikipedia.org/wiki/Comparison_of_platform_virtual_machines#Image_type_compatibility> "wikipedia:Comparison of platform virtual machines")。欢迎你对 V1 的支持状况做测试验证。

  * **QED** : QEMU Enhanced Disk 是旧版 QEMU 使用的格式。QEMU 也是一个开源免费的虚拟机监视器。该格式设计于 2010 年，目的是要比 QCOW2 等格式更优秀。这种格式支持的功能包括全异步 I/O，数据高度完整性，文件备份及稀疏文件。VirtualBox 支持 QED 格式只是为了兼容由旧版 QEMU 创建的虚拟机。

  * **QCOW** : QEMU Copy On Write 是 QEMU 现有版本支持的格式。QCOW 支持基于 zlib 实现的透明压缩与加密（加密功能有缺陷，不推荐使用）。QCOW 包括两个版本：QCOW 与 QCOW2。QCOW2 取代了旧版。[VirtualBox 完全支持旧版 QCOW](<https://www.virtualbox.org/manual/ch15.html#idp63002176>)。QCOW2 包含两个修订版：QCOW2 0.10 和 QCOW2 1.1（QEMU 新建的虚拟机默认使用 1.1）。然而 VirtualBox 并不支持 QCOW2。

  * **OVF** : Open Virtualization Format 是设计用于解决不同虚拟机监视器间的虚拟机互操作性和分发性的开放格式。VirtualBox 支持该格式的所有修订版，具体的支持方式是 [VBoxManage import/export 命令](<https://www.virtualbox.org/manual/ch08.html#idp55423424>)，但也有[部分功能受限](<https://www.virtualbox.org/manual/ch14.html#KnownProblems>)。

  * **RAW** : 该模式下虚拟硬盘会直接暴露到物理硬盘上，不以任何容器格式进行封装。VirtualBox 对此有多种支持方案：将 RAW 磁盘[转换成上述某种格式](<https://www.virtualbox.org/manual/ch08.html#idp59139136>)；[将物理盘复制到 RAW 格式](<https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevdi>)；直接挂载一个[指向物理盘或 RAW 格式文件](<https://www.virtualbox.org/manual/ch09.html#idp57804112>)的 VMDK 文件。

###  转换虚拟磁盘文件格式

[VBoxManage clonehd](<https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevdi>) 这个命令可以实现 VDI, VMDK, VHD 与 RAW 格式间的互转： 
    
    $ VBoxManage clonehd _inputfile_ _outputfile_ --format _outputformat_
    
以 VDI 转成 VMDK 为例： 
    
    $ VBoxManage clonehd _source.vdi_ _destination.vmdk_ --format VMDK
    
#### QCOW

VirtualBox 不支持 [QEMU](<../zh-cn/QEMU.html> "QEMU") 的 QCOW2 格式。若要让 VirtualBox 使用 QCOW2 格式的文件，你只能使用类似 [qemu-img](<https://archlinux.org/packages/?name=qemu-img>)包 的工具将其转换成已支持的格式。 _qemu-img_ 可以实现 QCOW 格式与 VDI, VMDK, VHDX, RAW 等其它格式间的互转。具体支持的格式可以通过运行 `qemu-img --help` 命令查看。 

该命令的一般形式是： 
    
    $ qemu-img convert -O _output_fmt_ _inputfile_ _outputfile_
    
以 QCOW2 转成 VDI 为例： 
    
    $ qemu-img convert -O vdi _source.qcow2_ _destination.vdi_
    
**提示：** 转换时加上 `-p` 参数可以实时查看转换进度

QCOW2 有两个修订版：0.10 和 1.1，用 `-o compat=_revision_` 参数可以指定具体版本。 

###  在主机挂载虚拟硬盘

#### VDI

只能挂载固定大小的 VDI 镜像（又名静态镜像），挂载动态镜像较为困难。 

首先要拿到 VDI 里数据分区的偏移量 `offData`： 
    
    $ VBoxManage internalcommands dumphdinfo _storage_.vdi | grep "offData"
    
然后再加上 `32256`（例如 69632 + 32256 = 101888），然后用这个命令来挂载： 
    
    # mount -t ext4 -o rw,noatime,noexec,loop,offset=101888 _storage_.vdi /mntpoint/
    
For VDI disks with more partitions you can also use `losetup`: 
    
    # losetup -o $offData -Pf
    
After this you should find the partitions under `/dev/loop*` (e.g. `/dev/loop0p1`). Then you can mount them as usual (e.g. `mount mount /dev/loop0p1 /mnt/`). 

另一个办法是用 [mount.vdi](<https://github.com/pld-linux/VirtualBox/blob/master/mount.vdi>) 脚本来完成挂载。首先要把脚本安装到 `/usr/bin/`，然后： 
    
    # mount -t vdi -o fstype=ext4,rw,noatime,noexec _vdi_file_location_ _/mnt/_
    
还可以使用 [qemu-img](<https://archlinux.org/packages/?name=qemu-img>)包 提供的 nbd 内核模块和 _qemu-nbd_ 工具[[2]](<https://bethesignal.org/blog/2011/01/05/how-to-mount-virtualbox-vdi-image/>)： 
    
    # modprobe nbd max_part=16
    # qemu-nbd -c /dev/nbd0 _storage_.vdi
    # mount /dev/nbd0p1 /mnt/dir/
    
需要卸载镜像时执行： 
    
    # umount /mnt/dir/
    # qemu-nbd -d /dev/nbd0
    
如果未能生成分区节点，试试运行命令：`partprobe /dev/nbd0`。另外，VDI 分区还可以直接用这个命令来映射到节点：`qemu-nbd -P 1 -c /dev/nbd0 _storage_.vdi`。 

#### VHD

与 VDI 类似，可以使用 [QEMU](<../zh-cn/QEMU.html> "QEMU") 的 nbd 模块挂载 VHD 镜像： 
    
    # modprobe nbd
    # qemu-nbd -c /dev/nbd0 _storage_.vhd
    # mount /dev/nbd0p1 /mnt
    
需要卸载镜像时执行： 
    
    # umount /mnt
    # qemu-nbd -d /dev/nbd0
    
###  压实虚拟硬盘

只有 _.vdi_ 格式的虚拟磁盘文件可以压实，具体操作步骤如下： 

启动虚拟机，手动删除无用文件，或者使用类似 [bleachbit](<https://archlinux.org/packages/?name=bleachbit>)包 的自动清理工具，[该工具也有 Windows 版](<https://www.bleachbit.org/download/windows>)。 

下一步要用零字节来填充可用空间。这有如下的可行方案： 

  * 如果你已经在用 Bleachbit 了，在 GUI 菜单里选择 _System > Free disk space_，或者在命令行执行：`bleachbit -c system.free_disk_space`；
  * 在类 UNIX 系统里，可以使用 `dd` 或 [dcfldd](<https://aur.archlinux.org/packages/dcfldd/>)AUR（参阅[这里](<https://superuser.com/a/355322>)来了解两者的区别）：

    # dcfldd if=/dev/zero of=_/fillfile_ bs=4M

    当 `fillfile` 文件快占满分区时，会出现这样的错误信息：`1280 blocks (5120Mb) written.dcfldd:: No space left on device`。这意味着所有的可用空间与未保留区块都已经被零字节填满了。因为 ext 类系统会为 root 用户默认保留一部分硬盘空间（见 `mkfs.ext4` 手册页对 `-m` 参数的解释，或者用 `tune2fs -l` 命令来查看具体为 root 保留了多少空间），所以运行这一命令时需要有 root 权限。
    前面一步操作完成后，手动把 `_fillfile_` 删掉。

  * 在 Windows 系统里有两种办法： 
    * 由 [Sysinternals Suite](<https://technet.microsoft.com/en-us/sysinternals/bb842062.aspx>) 提供的 `sdelete` 命令，用法是 `sdelete -s -z _c:_`。在虚拟机里的每一个分区都要执行一遍（当然 _c:_ 这个参数要对应地改成各个分区的盘符）；
    * 如果你喜欢脚本，可以用这个 [PowerShell 实现的方案](<https://blog.whatsupduck.net/2012/03/powershell-alternative-to-sdelete.html>)，但依然要每个分区执行一次：

    PS> ./Write-ZeroesToFreeSpace.ps1 -Root _c:\_ -PercentFree 0

**注意：** 该脚本需要在有管理员权限的 PowerShell 环境才能运行。默认的 PowerShell 配置下无法运行任何脚本，需要把执行策略至少调整到 `RemoteSigned`，而不能是 `Restricted`。用 `Get-ExecutionPolicy` 命令可以看到当前的执行策略，用 `Set-ExecutionPolicy RemoteSigned` 可以设置想要的执行策略。

完成这一步之后，将虚拟机关机。 

下一次启动虚拟机时，推荐先进行文件系统检查： 

  * 在类 UNIX 系统上可以手动运行 `fsck` 来检查； 
    * 在 GNU/Linux 系统上（包括 Arch）可以通过[内核启动参数](<../zh-cn/Fsck.html#%E5%BC%BA%E5%88%B6%E6%A3%80%E6%9F%A5> "Fsck")在系统启动时强制执行硬盘检查；
  * 在 Windows 系统上： 
    * 可以使用 `chkdsk _c:_ /F`，其中 `_c:_` 可以替换成所有你希望检查的盘符；
    * 或者从[这里](<https://archive.org/details/ChkDskAll>)下载 `FsckDskAll`。这和前面的 `chkdsk` 基本一样，只是不必手动为每个分区执行一遍了。

接下来通过 [VBoxManage modifyhd](<https://www.virtualbox.org/manual/ch08.html#vboxmanage-modifyvdi>) 移除 _.vdi_ 文件中的零即可完成压实过程： 
    
    $ VBoxManage modifyhd _your_disk.vdi_ --compact
    
**注意：**

  * 如果你的虚拟机有保存过快照，那么每个 _.vdi_ 文件都要单独执行一遍压实操作。
  * This concept of writing zeroes and compacting/reclaiming/cleanup space only works if there is no encryption on the virtual disk. 
    * On Windows you can check whether BitLocker is enabled using the `manage-bde -status` command and disable it with `manage-bde -off c:`, where `c:` refers to the encrypted drive. After that, repeat the steps mentioned above.

#### TRIM

VirtualBox offers simulation of TRIM in VDI files via an experimental "discard" attachment option. This option is undocumented and can be accessed by [commandline or .vbox file editing](<https://superuser.com/a/728469/>). When enabled, TRIM commands from the guest operating system causes the corresponding part of the VDI file to be compacted away. 

**警告：** Using this option without Host I/O Cache is known to cause lockups.

###  扩充虚拟硬盘容量

####  一般方法

如果你在创建虚拟机时给虚拟硬盘分配的容量太小了，VirtualBox 推荐的扩容方案是使用 [VBoxManage modifyhd](<https://www.virtualbox.org/manual/ch08.html#vboxmanage-modifyvdi>) 这个命令。然而这个命令只支持 VDI 和 VHD 这两种格式的动态分配容量版本。如果你想为固定大小的虚拟磁盘扩容，下面的办法适用于 Windows 或类 UNIX 系统的虚拟机。 

首先创建一个新的虚拟磁盘： 
    
    $ VBoxManage createmedium disk -filename _new.vdi_ --size _10000_
    
`--size` 参数的值的单位是 MiB，在例子里 10000 MiB ~= 10 GiB， _new.vdi_ 是新创建的镜像文件。 

**注意：** 该命令默认会创建 _标准_ （即动态分配）版本的文件格式，如果想创建固定大小的镜像，需要追加参数 `--variant Fixed`。

接下来要把旧镜像的内容复制到新镜像里去，这一步骤可能会花些时间： 
    
    $ VBoxManage clonemedium disk _old.vdi_ _new.vdi_ --existing
    
卸载旧硬盘镜像，挂载新镜像，下面命令中的斜体字部分需要按照你的使用环境来换成真实的值： 
    
    $ VBoxManage storageattach _virtual_machine_name_ --storagectl _SATA_ --port _0_ --medium none
    $ VBoxManage storageattach _virtual_machine_name_ --storagectl _SATA_ --port _0_ --medium _new.vdi_ --type hdd
    
在上面的命令中，若要获知存储控制器的名字与端口号，可以使用命令：`VBoxManage showvminfo _virtual_machine_name_`。这会打印出如下的输出（斜体标注的信息是有用的）： 
    
    [...]
    Storage Controller Name (0):            IDE
    Storage Controller Type (0):            PIIX4
    Storage Controller Instance Number (0): 0
    Storage Controller Max Port Count (0):  2
    Storage Controller Port Count (0):      2
    Storage Controller Bootable (0):        on
    Storage Controller Name (1):            SATA
    Storage Controller Type (1):            IntelAhci
    Storage Controller Instance Number (1): 0
    Storage Controller Max Port Count (1):  30
    Storage Controller Port Count (1):      1
    Storage Controller Bootable (1):        on
    IDE (1, 0): Empty
    _SATA_ (_0_ , 0): /home/wget/IT/Virtual_machines/GNU_Linux_distributions/ArchLinux_x64_EFI/Snapshots/{6bb17af7-e8a2-4bbf-baac-fbba05ebd704}.vdi (UUID: 6bb17af7-e8a2-4bbf-baac-fbba05ebd704)
    [...]
    
下载 [GParted Live 镜像](<https://gparted.org/download.php>)，在虚拟机里将其挂载到虚拟光驱中，启动虚拟机，调整分区大小 / 位置，卸载镜像并重启。这样扩容就完成了。 

**注意：** 如果虚拟盘使用了 GPT 分区表，扩容会导致 GPT 备份头不再位于硬盘末尾。GParted 会询问是否要将其修复，此时两次询问都要点 _Fix_ 。如果是 MBR 分区，就不存在这一问题。

最后，从 VirtualBox 里注销旧的镜像文件，并把它删掉： 
    
    $ VBoxManage closemedium disk _old.vdi_
    $ rm _old.vdi_
    
####  扩容 VDI 硬盘

如果你的虚拟硬盘是 VDI 格式的，请使用： 
    
    $ VBoxManage modifymedium disk _your_virtual_disk.vdi_ --resize _the_new_size_
    
然后回到上面的 Gparted 步骤，继续完成扩容操作。 

###  修改 .vbox 文件来替换虚拟硬盘

如果你觉得编辑 _XML_ 文件比用 GUI 或 `VBoxManage` 更方便，那可以通过在虚拟机的 _.vbox_ 配置文件中替换 GUID、文件路径和格式来替换或添加虚拟硬盘： 
    
    ArchLinux_vm.vbox
    
    <HardDisk uuid="_{670157e5-8bd4-4f7b-8b96-9ee412a712b5}_ " location="_ArchLinux_vm.vdi_ " format="_VDI_ " type="Normal"/>

然后找到 `<StorageController>` 的子元素 `<AttachedDevice>`，把 GUID 属性改成新镜像文件的值： 
    
    ArchLinux_vm.vbox
    
    <AttachedDevice type="HardDisk" port="0" device="0">
      <Image uuid="_{670157e5-8bd4-4f7b-8b96-9ee412a712b5}_ "/>
    </AttachedDevice>

**注意：** 如果你还不知道新镜像文件的 GUID 值，可以用命令 `VBoxManage showhdinfo _file_` 来查看。如果你用 `VBoxManage clonehd` 命令来处理过虚拟盘，那么在复制或转换过程完成时，也会打印出 GUID 值。随便写一个 GUID 上去是不行的，必须与[镜像文件里的 UUID 值](<https://www.virtualbox.org/manual/ch05.html#cloningvdis>)相对应才行。

####  在 Linux 宿主机和其它系统间迁移

_.vbox_ 配置文件把虚拟盘和快照文件的位置记录在 `<HardDisks> .... </HardDisks>` 标签里。如果新宿主系统存放虚拟机文件的路径与旧宿主系统不同，你可以手动修改路径值；如果 _.vbox_ 文件与虚拟盘和快照文件夹位于相同目录，也可以使用以下脚本，它会将修改后的新配置打印到标准输出。 
    
    #!/bin/sh
    NewPath="${PWD}/"
    Snapshots="Snapshots/"
    Filename="$1"
    
     awk -v SetPath="$NewPath" -v SnapPath="$Snapshots" '{if(index($0,"<HardDisk uuid=") != 0){A=$3;split(A,B,"=");
    L=B[2];
     gsub(/\"/,"",L);
      sub(/^.*\//,"",L);
      sub(/^.*\\/,"",L);
     if(index($3,"{") != 0){SnapS=SnapPath}else{SnapS=""};
      print $1" "$2" location="\"SetPath SnapS L"\" "$4" "$5}
    else print $0}' "$Filename"

**注意：**

  * 如果你想把虚拟机迁移到 Windows 宿主系统上去，文件路径里应该使用 `\` 而不是 `/`。
  * 这个脚本判断快照的逻辑是：文件名是否包含 `{`。
  * 为了在新宿主机上运行起来，首先得在管理界面注册：点选菜单项 **Machine - > Add...** 或者按快捷键 `Ctrl+a` ，然后找到 _.vbox_ 配置文件。也可以用命令行：`VBoxManage registervm _filename_.vbox`

###  复制虚拟盘并为其分配新 UUID

VirtualBox 广泛应用了 UUID。每个虚拟机和虚拟机的各个虚拟盘必须有不同的 UUID，在启动虚拟机时，VirtualBox 会跟踪虚拟机实例的所有 UUID。用 [VBoxManage list](<https://www.virtualbox.org/manual/ch08.html#vboxmanage-list>) 命令可以列出 VirtualBox 管理的所有资源。 

如果你想复制一台虚拟机，仅复制虚拟盘镜像文件是不够的。你还得给复制出的新镜像文件分配一个新的 UUID。否则在同一个 VirtualBox 的环境里无法同时注册两个具有相同 UUID 的镜像文件。 

下面这个命令可以用来为虚拟盘分配新 UUID： 
    
    $ VBoxManage internalcommands sethduuid _/path/to/disk.vdi_
    
**提示：** 用 [VBoxManage clonehd](<https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevdi>) 可以一次性完成复制内容与分配新 UUID

**注意：** 上述命令可以用于任意 [VirtualBox 所支持的镜像格式](<#VirtualBox_%E6%94%AF%E6%8C%81%E7%9A%84%E6%A0%BC%E5%BC%8F>)。

##  使用技巧

###  Import/export VirtualBox virtual machines from/to other hypervisors

If you plan to use your virtual machine on another hypervisor or want to import in VirtualBox a virtual machine created with another hypervisor, you might be interested in reading the following steps. 

#### Remove additions

Guest additions are available in most hypervisor solutions: VirtualBox comes with the [Guest Additions](<#Guest_additions>), VMware with the VMware Tools, Parallels with the Parallels Tools, etc. These additional components are designed to be installed inside a virtual machine after the guest operating system has been installed. They consist of device drivers and system applications that optimize the guest operating system for better performance and usability [by providing these features](<https://www.virtualbox.org/manual/ch04.html>). 

If you have installed the additions to your virtual machine, please uninstall them first. Your guest, especially if it is using an operating system from the Windows family, might behave weirdly, crash or even might not boot at all if you are still using the specific drivers in another hypervisor. 

#### Use the right virtual disk format

This step will depend on the ability to convert the virtual disk image directly or not. 

##### Automatic tools

Some companies provide tools which offer the ability to create virtual machines from a Windows or GNU/Linux operating system located either in a virtual machine or even in a native installation. With such a product, you do not need to apply this and the following steps and can stop reading here. 

  * _[Parallels Transporter](<https://www.parallels.com/products/transporter>)_ which is non free, is a product from Parallels Inc. This solution basically consists in an piece of software called _agent_ that will be installed in the guest you want to import/convert. Then, Parallels Transporter, _which only works on OS X_ , will create a virtual machine from that _agent_ which is contacted either by USB or Ethernet network.
  * _[VMware vCenter Converter](<https://www.vmware.com/products/converter/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ]_ which is free upon registration on the VMware website, works nearly the same way as Parallels Transporter, but the piece of software that will gather the data to create the virtual machine only works on a Windows platform.

##### Manual conversion

First, familiarize yourself with the [formats supported by VirtualBox](<#Formats_supported_by_VirtualBox>) and [those supported by third-party hypervisors](<https://en.wikipedia.org/wiki/Comparison_of_platform_virtual_machines#Image_type_compatibility> "wikipedia:Comparison of platform virtual machines"). 

  * Importing or exporting a virtual machine from/to a VMware solution is not a problem at all if you use the VMDK or OVF disk format, otherwise converting [VMDK to VDI and VDI to VMDK](<#Disk_image_format_conversion>) is possible and the aforementioned VMware vCenter Converter tool is available.
  * Importing or exporting from/to QEMU is not a problem neither: some QEMU formats are supported directly by VirtualBox and conversion between [QCOW2 to VDI and VDI to QCOW2](<#QCOW>) is still available if needed.
  * Importing or exporting from/to Parallels hypervisor is the hardest way: Parallels does only support its own HDD format (even the standard and portable OVF format is not supported!).

  * To export your virtual machine to Parallels, you will need to use the Parallels Transporter tool described above.
  * To import your virtual machine to VirtualBox, you will need to use the VMware vCenter Converter described above to convert the virtual machine to the VMware format first. Then, apply the solution to migrate from VMware.

#### Create the virtual machine configuration for your hypervisor

Each hypervisor have their own virtual machine configuration file: _.vbox_ for VirtualBox, _.vmx_ for VMware, a `config.pvs` file located in the virtual machine bundle (_.pvm_ file), etc. You will have thus to recreate a new virtual machine in your new destination hypervisor and specify its hardware configuration as close as possible as your initial virtual machine. 

Pay a close attention to the firmware interface (BIOS or UEFI) used to install the guest operating system. While an option is available to choose between these 2 interfaces on VirtualBox and on Parallels solutions, on VMware, you will have to add manually the following line to your _.vmx_ file. 
    
    ArchLinux_vm.vmx
    
    firmware = "efi"

Finally, ask your hypervisor to use the existing virtual disk you have converted and launch the virtual machine. 

**提示：**

  * On VirtualBox, if you do not want to browse the whole GUI to find the right location to add your new virtual drive device, you can [Replace a virtual disk manually from the .vbox file](<#Replace_a_virtual_disk_manually_from_the_.vbox_file>), or use the `VBoxManage storageattach` described in [#Increasing the size of VDI disks](<#Increasing_the_size_of_VDI_disks>) or in the [VirtualBox manual page](<https://www.virtualbox.org/manual/ch08.html#vboxmanage-storageattach>).
  * Similarly, in VMware products, you can replace the location of the current virtual disk location by adapting the _.vmdk_ file location in your _.vmx_ configuration file.

### Virtual machine launch management

####  Starting virtual machines with a service (autostart)

Find hereafter the implementation details of a systemd service that will be used to consider a virtual machine as a service. 
    
    /etc/systemd/system/vboxvmservice@.service
    
    [Unit]
    Description=VBox Virtual Machine %i Service
    Requires=systemd-modules-load.service
    After=systemd-modules-load.service
    
    [Service]
    User=_username_
    Group=vboxusers
    ExecStart=/usr/bin/VBoxManage startvm %i --type _startmode_
    ExecStop=/usr/bin/VBoxManage controlvm %i _stopmode_
    RemainAfterExit=yes
    
    [Install]
    WantedBy=multi-user.target

**注意：**

  * Replace `_username_` with a user that is a member of the `vboxusers` group. Make sure the user chosen is the same user that will create/import virtual machines, otherwise the user will not see the virtual machine appliances.
  * Replace `_startmode_` with a virtual machine frontend type, usually `gui`, `headless` or `separate`
  * Replace `_stopmode_` with desired state switch, usually `savestate` or `acpipowerbutton`
  * If you have multiple virtual machines managed by systemd and they are not stopping properly, try to add `KillMode=none` and `TimeoutStopSec=40` at the end of `[Service]` section.

[Enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") the `vboxvmservice@_your_virtual_machine_name_` systemd unit in order to launch the virtual machine at next boot. To launch it directly, simply [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") the systemd unit. 

VirtualBox 4.2 introduces [a new way](<https://lifeofageekadmin.com/how-to-set-your-virtualbox-vm-to-automatically-startup/>) for UNIX-like systems to have virtual machines started automatically, other than using a systemd service. 

#### Starting virtual machines with a keyboard shortcut

It can be useful to start virtual machines directly with a keyboard shortcut instead of using the VirtualBox interface (GUI or CLI). For that, you can simply define key bindings in `.xbindkeysrc`. Please refer to [Xbindkeys](</wzh/index.php?title=Xbindkeys&action=edit&redlink=1> "Xbindkeys（页面不存在）") for more details. 

Example, using the `Fn` key of a laptop with an unused battery key (`F3` on the computer used in this example): 
    
    "VBoxManage startvm 'Windows 7'"
    m:0x0 + c:244
    XF86Battery
    
**注意：** If you have a space in the name of your virtual machine, then enclose it with single apostrophes like made in the example just above.

### Use specific device in the virtual machine

####  Using USB webcam / microphone

**注意：** You will need to have [extension pack](<#Extension_pack>) installed before following the steps below.

  1. Make sure the virtual machine is not running and your webcam / microphone is not being used.
  2. Bring up the main VirtualBox window and go to settings for Arch machine. Go to USB section.
  3. Make sure _Enable USB Controller_ is selected. Also make sure that _Enable USB 2.0 (EHCI) Controller_ is selected too.
  4. Click the _Add filter from device_ button (the cable with the _+_ icon).
  5. Select your USB webcam/microphone device from the list.
  6. Now click OK and start your virtual machine.

**注意：** If your Microphone does not show up in the "Add filter from device" menu, try the USB 3.0 and 1.1 options instead (In Step 3).

#### Detecting web-cams and other USB devices

**注意：** This will not do much if you are running a Linux/Unix operating system inside of your virtual machine, as most do not have autodetection features.

If the device that you are looking for does not show up on any of the menus in the section above and you have tried all three USB controller options, boot up your virtual machine three separate times. Once using the USB 1.1 controller, another using the USB 2.0 controller, etc. Leave the virtual machine running for at least 5 minutes after startup. Sometimes Windows will autodetect the device for you. Be sure you filter any devices that are not a keyboard or a mouse so they do not start up at boot. This ensures that Windows will detect the device at start-up. 

### Access a guest server

To access [Apache server](<https://en.wikipedia.org/wiki/Apache_HTTP_Server> "wikipedia:Apache HTTP Server") on a Virtual Machine from the host machine **only** , simply execute the following lines on the host: 
    
    $ VBoxManage setextradata GuestName "VBoxInternal/Devices/_pcnet_ /0/LUN#0/Config/Apache/HostPort" _8888_
    $ VBoxManage setextradata GuestName "VBoxInternal/Devices/_pcnet_ /0/LUN#0/Config/Apache/GuestPort" _80_
    $ VBoxManage setextradata GuestName "VBoxInternal/Devices/_pcnet_ /0/LUN#0/Config/Apache/Protocol" TCP
    
where `_8888_` is the port the host should listen on and `_80_` is the port the virtual machine will send Apache's signal on. 

To use a port lower than 1024 on the host machine, changes need to be made to the firewall on that host machine. This can also be set up to work with SSH or any other services by changing "Apache" to the corresponding service and ports. 

**注意：**`pcnet` refers to the network card of the virtual machine. If you use an Intel card in your virtual machine settings, change `pcnet` to `e1000`.

To communicate between the VirtualBox guest and host using ssh, the server port must be forwarded under Settings > Network. When connecting from the client/host, connect to the IP address of the client/host machine, as opposed to the connection of the other machine. This is because the connection will be made over a virtual adapter. 

### D3D acceleration in Windows guests

Recent versions of VirtualBox have support for accelerating OpenGL inside guests. This can be enabled with a simple checkbox in the machine's settings, right below where video ram is set, and installing the VirtualBox [guest additions](<#Guest_additions>). However, most Windows games use Direct3D (part of DirectX), not OpenGL, and are thus not helped by this method. However, it is possible to gain accelerated Direct3D in your Windows guests by borrowing the d3d libraries from Wine, which translate d3d calls into OpenGL, which is then accelerated. These libraries are now part of VirtualBox guest additions. 

After enabling OpenGL acceleration as described above, reboot the guest into safe mode (press F8 before the Windows screen appears but after the VirtualBox screen disappears), and install VirtualBox [guest additions](<#Guest_additions>), during install enable checkbox _Direct3D support_. Reboot back to normal mode and you should have accelerated Direct3D. 

**注意：**

  * This hack may or may not work for some games depending on what hardware checks they make and what parts of D3D they use.
  * This was tested on Windows XP, 7 and 8.1. If method does not work on your Windows version please add data here.

### VirtualBox on a USB key

When using VirtualBox on a USB key, for example to start an installed machine with an ISO image, you will manually have to create VMKDs from the existing drives. However, once the new VMDKs are saved and you move on to another machine, you may experience problems launching an appropriate machine again. To get rid of this issue, you can use the following script to launch VirtualBox. This script will clean up and unregister old VMDK files and it will create new, proper VMDKs for you: 

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** The following script parses the output of ls, which is [very brittle](<https://github.com/koalaman/shellcheck/wiki/SC2010>) and [known to break](<https://github.com/koalaman/shellcheck/wiki/SC2012>).（在[Talk:VirtualBox](<../zh-cn/Talk:VirtualBox.html>)讨论）
    
    #!/bin/sh
    # Erase old VMDK entries
    rm ~/.VirtualBox/*.vmdk
    
    # Clean up VBox-Registry
    sed -i '/sd/d' ~/.VirtualBox/VirtualBox.xml
    
    # Remove old harddisks from existing machines
    find ~/.VirtualBox/Machines -name \*.xml | while read -r file; do
      line=$(grep -e "type\=\"HardDisk\"" -n "$file" | cut -d ':' -f 1)
      if [ -n "$line" ]; then
        sed -i "${line}"d "$file"
        sed -i "${line}"d "$file"
        sed -i "${line}"d "$file"
      fi
      sed -i "/rg/d" "$file"
    done
    
    # Delete prev-files created by VirtualBox
    find ~/.VirtualBox/Machines -name \*-prev -exec rm '{}' \;
    
    # Recreate VMDKs
    ls -l /dev/disk/by-uuid | cut -d ' ' -f 9,11 | while read -r ln; do
      if [ -n "$ln" ]; then
        uuid=$(echo "$ln" | cut -d ' ' -f 1)
        device=$(echo "$ln" | cut -d ' ' -f 2 | cut -d '/' -f 3 | cut -b 1-3)
    
        # determine whether drive is mounted already
        checkstr1=$(mount | grep "$uuid")
        checkstr2=$(mount | grep "$device")
        checkstr3=$(ls ~/.VirtualBox/*.vmdk | grep "$device")
        if [ -z "$checkstr1" ] && [ -z "$checkstr2" ] && [ -z "$checkstr3" ]; then
          VBoxManage internalcommands createrawvmdk -filename ~/.VirtualBox/"$device".vmdk -rawdisk /dev/"$device" -register
        fi
      fi
    done
    
    # Start VirtualBox
    VirtualBox
    
Note that your user has to be added to the "disk" group to create VMDKs out of existing drives. 

### Run a native Arch Linux installation inside VirtualBox

If you have a dual boot system between Arch Linux and another operating system, it can become tedious to switch back and forth if you need to work in both. You may also experience performance or compatibility issues when using a virtual machine, which can impact your ability to do certain tasks. 

This guide will let you reuse, in a virtual machine, your native Arch Linux installation when you are running your second operating system. This way, you keep the ability to run each operating system natively, but have the option to run your Arch Linux installation inside a virtual machine. 

#### Make sure you have a persistent naming scheme

Depending on your hard drive setup, device files representing your hard drives may appear differently when you will run your Arch Linux installation natively or in virtual machine. This problem occurs when using [FakeRAID](<../zh-cn/RAID.html#Implementation> "RAID") for example. The fake RAID device will be mapped in `/dev/mapper/` when you run your GNU/Linux distribution natively, while the devices are still accessible separately. However, in your virtual machine, it can appear without any mapping in `/dev/sdaX` for example, because the drivers controlling the fake RAID in your host operating system (e.g. Windows) are abstracting the fake RAID device. 

To circumvent this problem, we will need to use an addressing scheme that is persistent to both systems. This can be achieved using [UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID")s. Make sure your [boot loader](<../zh-cn/Boot_loader.html> "Boot loader") and [fstab](<../zh-cn/Fstab.html> "Fstab") file is using UUIDs, otherwise fix this issue. Read [fstab](<../zh-cn/Fstab.html> "Fstab") and [Persistent block device naming](<../zh-cn/Persistent_block_device_naming.html> "Persistent block device naming"). 

**警告：**

  * Make sure your host partition is only accessible in read only from your Arch Linux virtual machine, this will avoid risk of corruptions if you were to corrupt that host partition by writing on it due to lack of attention.
  * You should NEVER allow VirtualBox to boot from the entry of your second operating system, which, as a reminder, is used as the host for this virtual machine! Take thus a special care especially if your default boot loader/boot manager entry is your other operating system. Give a more important timeout or put it below in the order of preferences.

#### Make sure your mkinitcpio image is correct

Make sure your [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") configuration uses the [HOOK](<../zh-cn/Mkinitcpio.html#HOOKS> "Mkinitcpio") `block`: 
    
    /etc/mkinitcpio.conf
    
    ...
    HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont **block** filesystems fsck)
    ...

If it is not present, add it and [regenerate the initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs"). 

#### Create a virtual machine configuration to boot from the physical drive

##### Create a raw disk VMDK image

Now, we need to create a new virtual machine which will use a [RAW disk](<https://www.virtualbox.org/manual/ch09.html#rawdisk>) as virtual drive, for that we will use a ~ 1Kio VMDK file which will be mapped to a physical disk. Unfortunately, VirtualBox does not have this option in the GUI, so we will have to use the console and use an internal command of `VBoxManage`. 

Boot the host which will use the Arch Linux virtual machine. The command will need to be adapted according to the host you have. 

On a GNU/Linux host
    
There are 3 ways to achieve this: login as root, changing the access right of the device with `chmod`, adding your user to the `disk` group. The latter way is the more elegant, let us proceed that way: 
    
    # gpasswd -a _your_user_ disk
    
Apply the new group settings with: 
    
    $ newgrp
    
Now, you can use the command: 
    
    $ VBoxManage internalcommands createrawvmdk -filename _/path/to/file.vmdk_ -rawdisk _/dev/sdb_ -register
    
Adapt the above command to your need, especially the path and filename of the VMDK location and the raw disk location to map which contain your Arch Linux installation. 

On a Windows host
    
Open a command prompt must be run as administrator. 

**提示：** On Windows, open your start menu/start screen, type `cmd`, and type `Ctrl+Shift+Enter`, this is a shortcut to execute the selected program with admin rights.

On Windows, as the disk filename convention is different from UNIX, use this command to determine what drives you have in your Windows system and their location:
    
    # wmic diskdrive get name,size,model
    
    Model                               Name                Size
    WDC WD40EZRX-00SPEB0 ATA Device     \\.\PHYSICALDRIVE1  4000783933440
    KINGSTON SVP100S296G ATA Device     \\.\PHYSICALDRIVE0  96024821760
    Hitachi HDT721010SLA360 ATA Device  \\.\PHYSICALDRIVE2  1000202273280
    Innostor Ext. HDD USB Device        \\.\PHYSICALDRIVE3  1000202273280

In this example, as the Windows convention is `\\.\PhysicalDriveX` where X is a number from 0, `\\.\PHYSICALDRIVE1` could be analogous to `/dev/sdb` from the Linux disk terminology. 

To use the `VBoxManage` command on Windows, you can either, change the current directory to your VirtualBox installation folder first with `cd C:\Program Files\Oracle\VirtualBox\`
    
    # .\VBoxManage.exe internalcommands createrawvmdk -filename C:\file.vmdk -rawdisk \\.\PHYSICALDRIVE1
    
or use the absolute path name: 
    
    # "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" internalcommands createrawvmdk -filename C:\file.vmdk -rawdisk \\.\PHYSICALDRIVE1
    
On another operating system host
    
There are other limitations regarding the aforementioned command when used in other operating systems like OS X, please thus [read carefully the manual page](<https://www.virtualbox.org/manual/ch09.html#rawdisk>), if you are concerned. 

##### Create the virtual machine configuration file

**注意：**

  * To make use of the VBoxManage command on Windows, you need to change the current directory to your VirtualBox installation folder first: `cd C:\Program Files\Oracle\VirtualBox\`.
  * Windows makes use of backslashes instead of slashes, please replace all slashes `/` occurrences by backslashes `\` in the commands that follow when you will use them.

After, we need to create a new machine (replace the _virtual_machine_name_ to your convenience) and register it with VirtualBox. 
    
    $ VBoxManage createvm -name _virtual_machine_name_ -register
    
Then, the newly raw disk needs to be attached to the machine. This will depend if your computer or actually the root of your native Arch Linux installation is on an IDE or a SATA controller. 

If you need an IDE controller: 
    
    $ VBoxManage storagectl _virtual_machine_name_ --name "IDE Controller" --add ide
    $ VBoxManage storageattach _virtual_machine_name_ --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium /path/to/file.vmdk
    
otherwise: 
    
    $ VBoxManage storagectl _virtual_machine_name_ --name "SATA Controller" --add sata
    $ VBoxManage storageattach _virtual_machine_name_ --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium /path/to/file.vmdk
    
While you continue using the CLI, it is recommended to use the VirtualBox GUI, to personalise the virtual machine configuration. Indeed, you must specify its hardware configuration as close as possible as your native machine: turning on the 3D acceleration, increasing video memory, setting the network interface, etc. 

Finally, you may want to seamlessly integrate your Arch Linux with your host operating system and allow copy pasting between both operating systems. Please refer to [VirtualBox/Install Arch Linux as a guest#Install the Guest Additions](<../zh-cn/VirtualBox/Install_Arch_Linux_as_a_guest.html#Install_the_Guest_Additions> "VirtualBox/Install Arch Linux as a guest") for that, since this Arch Linux virtual machine is basically an Arch Linux guest. 

**警告：** For [Xorg](<../zh-cn/Xorg.html> "Xorg") to work in natively and in the virtual machine, since obviously it will be using different drivers, it is best if there is no `/etc/X11/xorg.conf`, so Xorg will pick up everything it needs on the fly. However, if you really do need your own Xorg configuration, maybe is it worth to set your default systemd target to `multi-user.target` with `systemctl isolate graphical.target` as root (more details at [systemd#Targets](<../zh-cn/Systemd.html#Targets> "Systemd") and [systemd#Change current target](<../zh-cn/Systemd.html#Change_current_target> "Systemd")). In that way, the graphical interface is disabled (i.e. Xorg is not launched) and after you logged in, you can `startx`} manually with a custom `xorg.conf`.

### Install a native Arch Linux system from VirtualBox

In some cases it may be useful to install a native Arch Linux system while running another operating system: one way to accomplish this is to perform the installation through VirtualBox on a [raw disk](<https://www.virtualbox.org/manual/ch09.html#rawdisk>). If the existing operating system is Linux based, you may want to consider following [Install from existing Linux](<../zh-cn/Install_from_existing_Linux.html> "Install from existing Linux") instead. 

This scenario is very similar to [#Run a native Arch Linux installation inside VirtualBox](<#Run_a_native_Arch_Linux_installation_inside_VirtualBox>), but will follow those steps in a different order: start by [#Create a raw disk VMDK image](<#Create_a_raw_disk_VMDK_image>), then [#Create the virtual machine configuration file](<#Create_the_virtual_machine_configuration_file>). 

Now, you should have a working virtual machine configuration whose virtual VMDK disk is tied to a real disk. The installation process is exactly the same as the steps described in [VirtualBox/Install Arch Linux as a guest](<../zh-cn/VirtualBox/Install_Arch_Linux_as_a_guest.html> "VirtualBox/Install Arch Linux as a guest"), but [#Make sure you have a persistent naming scheme](<#Make_sure_you_have_a_persistent_naming_scheme>) and [#Make sure your mkinitcpio image is correct](<#Make_sure_your_mkinitcpio_image_is_correct>). 

**警告：**

  * For BIOS systems and MBR disks, do not install a boot loader inside your virtual machine, this will not work since the MBR is not linked to the MBR of your real machine and your virtual disk is only mapped to a real partition without the MBR.
  * For UEFI systems without [CSM](<https://en.wikipedia.org/wiki/Compatibility_Support_Module#CSM> "wikipedia:Compatibility Support Module") and GPT disks, the installation will not work at all since: 
    * the [EFI system partition](<../zh-cn/EFI_system_partition.html> "EFI system partition") is not mapped to your virtual disk and Arch Linux requires to have the Linux kernel on it to boot as an EFI application (see [EFI boot stub](</wzh/index.php?title=EFI_boot_stub&action=edit&redlink=1> "EFI boot stub（页面不存在）") for details);
    * and the efivars, if you are installing Arch Linux using the EFI mode brought by VirtualBox, are not the one of your real system: the bootmanager entries will hence not be registered.
  * This is why, it is recommended to create your partitions in a native installation first, otherwize the partitions will not be taken into consideration in your MBR/GPT partition table.

After completing the installation, boot your computer natively with an GNU/Linux installation media (whether it be Arch Linux or not), [chroot](<../zh-cn/Installation_guide.html#Chroot> "Installation guide") into your installed Arch Linux installation and install and configure a [boot loader](<../zh-cn/Boot_loader.html> "Boot loader"). 

### Install MacOS guest

Before starting the virtual machine, run the following commands on the host machine [[3]](<https://medium.com/@twister.mr/installing-macos-to-virtualbox-1fcc5cf22801>): 
    
    $ VBoxManage modifyvm "MyMacVM" --cpuid-set 00000001 000106e5 00100800 0098e3fd bfebfbff
    $ VBoxManage setextradata "MyMacVM" "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "iMac11,3"
    $ VBoxManage setextradata "MyMacVM" "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"
    $ VBoxManage setextradata "MyMacVM" "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Iloveapple"
    $ VBoxManage setextradata "MyMacVM" "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"
    $ VBoxManage setextradata "MyMacVM" "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1
    $ VBoxManage setextradata "MyMacVM" VBoxInternal2/EfiGopMode 4
    
If you use an AMD processor and the first boot gets stuck, you also have to run 
    
    $ VBoxManage modifyvm "MyMacVM" --cpu-profile "Intel Core i7-6700K"
    
####  No keyboard/mouse input when attempting to install Mojave

If you are attempting to install Mojave, after doing the aforementioned steps, the installer will load up but you might not be able to send keyboard or mouse input. The reason seems to be that Mojave no longer supports the USB 1.1 controllers and in order to fix the issue you need to emulating USB 3.0. To do that first install the [extension pack](<#Extension_pack>). 

Then go to _Machine > Settings > USB_ and select _USB 3.0_. Input should work from this point onwards. 

#### UEFI interactive shell after restart

If the installer is unable to properly format the bootable drive during installation and you end up in an UEFI shell, enter the following: 

  1. Type `exit` at the UEFI prompt
  2. Select _Boot Maintenance Manager_
  3. Select _Boot From File_

You will now be brought to couple of obscure PCI paths. The first one is the one that you just attempted to boot from and it did not work. The second (or third) one should be the one with the MacOS recovery partition that you need to load to continue the installation. Click the second Entry. If it is empty, press `Esc` to go back and select the third entry. Once you get one with folders click though the folders. It should be something like _macOS Install Data > Locked Files > Boot Files > boot.efi_. Once you click enter on the _boot.efi_ you should boot into the MacOS installer and resume installation. Note that some of the subdirectories might be missing. Remember that you need to get to a `boot.efi`.[[4]](<https://superuser.com/questions/1235970/stuck-on-uefi-interactive-shell-with-mac-os-x-high-sierra-vm>)

### Move a native Windows installation to a virtual machine

If you want to migrate an existing native Windows installation to a virtual machine which will be used with VirtualBox on GNU/Linux, this use case is for you. This section only covers native Windows installation using the MSDOS/Intel partition scheme. Your Windows installation must reside on the first MBR partition for this operation to success. Operation for other partitions are available but have been untested (see [#Known limitations](<#Known_limitations>) for details). 

**警告：** If you are using an OEM version of Windows, this process is unauthorized by the end user license license. Indeed, the OEM license typically states the Windows install is tied with the hardware together. Transferring a Windows install to a virtual machine removes this link. Make thus sure you have a full Windows install or a volume license model before continuing. If you have a full Windows license but the latter is not coming in volume, nor as a special license for several PCs, this means you will have to remove the native installation after the transfer operation has been achieved.

A couple of tasks are required to be done inside your native Windows installation first, then on your GNU/Linux host. 

#### Tasks on Windows

The first three following points comes from [this outdated VirtualBox wiki page](<https://www.virtualbox.org/wiki/Migrate_Windows#HAL>), but are updated here. 

  * Remove IDE/ATA controllers checks (Windows XP only): Windows memorize the IDE/ATA drive controllers it has been installed on and will not boot if it detects these have changed. The solution proposed by Microsoft is to reuse the same controller or use one of the same serial, which is impossible to achieve since we are using a Virtual Machine. [MergeIDE](<https://www.virtualbox.org/wiki/Migrate_Windows#HardDiskSupport>), a German tool, developped upon another other solution proposed by Microsoft can be used. That solution basically consists in taking all IDE/ATA controller drivers supported by Windows XP from the initial driver archive (the location is hard coded, or specify it as the first argument to the _.bat_ script), installing them and registering them with the regedit database.
  * Use the right type of Hardware Abstraction Layer (old 32 bits Windows versions): Microsoft ships 3 default versions: `Hal.dll` (Standard PC), `Halacpi.dll` (ACPI HAL) and `Halaacpi.dll` (ACPI HAL with IO APIC). Your Windows install could come installed with the first or the second version. In that way, please [disable the _Enable IO/APIC_ VirtualBox extended feature](<https://www.virtualbox.org/manual/ch08.html#idp56927888>).
  * Disable any AGP device driver (only outdated Windows versions): If you have the files `agp440.sys` or `intelppm.sys` inside the `C:\Windows\SYSTEM32\drivers\` directory, remove it. As VirtualBox uses a PCI virtual graphics card, this can cause problems when this AGP driver is used.
  * Create a Windows recovery disk: In the following steps, if things turn bad, you will need to repair your Windows installation. Make sure you have an install media at hand, or create one with _Create a recovery disk_ from Vista SP1, _Create a system repair disc_ on Windows 7 or _Create a recovery drive_ on Windows 8.x).

#### Using Disk2vhd to clone Windows partition

Boot into Windows, clean up the installation (with [CCleaner](<https://www.piriform.com/ccleaner>) for example), use [disk2vhd](<https://technet.microsoft.com/en-us/library/ee656415.aspx>) tool to create a VHD image. Include a reserved system partition (if present) and the actual Windows partition (usually disk C:). The size of Disk2vhd-created image will be the sum of the actual files on the partition (used space), not the size of a whole partition. If all goes well, the image should just boot in a virtual machine and you will not have to go through the hassle with MBR and Windows boot loader, as in the case of cloning an entire partition. 

####  Tasks on GNU/Linux

**提示：** Skip the partition-related parts if you created VHD image with [Disk2vhd](<#Using_Disk2vhd_to_clone_Windows_partition>).

  * Reduce the native Windows partition size to the size Windows actually needs with `ntfsresize` available from [ntfs-3g](<https://archlinux.org/packages/?name=ntfs-3g>)包. The size you will specify will be the same size of the VDI that will be created in the next step. If this size is too low, you may break your Windows install and the latter might not boot at all.

    Use the `--no-action` option first to run a test:
    
    # ntfsresize --no-action --size _52Gi_ _/dev/sda1_

    If only the previous test succeeded, execute this command again, but this time without the aforementioned test flag.

  * Install VirtualBox on your GNU/Linux host (see [#Installation steps for Arch Linux hosts](<#Installation_steps_for_Arch_Linux_hosts>) if your host is Arch Linux).

  * Create the Windows disk image from the beginning of the drive to the end of the first partition where is located your Windows installation. Copying from the beginning of the disk is necessary because the MBR space at the beginning of the drive needs to be on the virtual drive along with the Windows partition. In this example two following partitions `sda2` and `sda3`will be later removed from the partition table and the MBR boot loader will be updated.

    # sectnum=$(( $(cat /sys/block/_sda/sda1_ /start) + $(cat /sys/block/_sda/sda1_ /size) ))

    Using `cat /sys/block/_sda/sda1_ /size` will output the number of total sectors of the first partition of the disk `sda`. Adapt where necessary.

    # dd if=_/dev/sda_ bs=512 count=$sectnum | VBoxManage convertfromraw stdin _windows.vdi_ $(( $sectnum * 512 ))

    We need to display the size in byte, `$(( $sectnum * 512 ))` will convert the sector numbers to bytes.

  * Since you created your disk image as root, set the right ownership to the virtual disk image: 
        
        # chown _your_user_ :_your_group_ windows.vdi

  * Create your virtual machine configuration file and use the virtual disk created previously as the main virtual hard disk.

  * Try to boot your Windows virtual machine, it may just work. First though remove and repair disks from the boot process as it may interfere (and likely will) booting into safe-mode.

  * Attempt to boot your Windows virtual machine in safe mode (press the F8 key before the Windows logo shows up)... if running into boot issues, read [#Fix MBR and Microsoft boot loader](<#Fix_MBR_and_Microsoft_boot_loader>). In safe-mode, drivers will be installed likely by the Windows plug-and-play detection mechanism [view](<https://i.imgur.com/hh1RrSp.png>). Additionally, install the VirtualBox [Guest Additions](<#Guest_additions>) via the menu _Devices_ > _Insert Guest Additions CD image..._. If a new disk dialog does not appear, navigate to the CD drive and start the installer manually.

  * You should finally have a working Windows virtual machine. Do not forget to read the [#Known limitations](<#Known_limitations>).

  * Performance tip: according to [VirtualBox manual](<https://www.virtualbox.org/manual/ch05.html#harddiskcontrollers>), SATA controller has a better performance than IDE. If you cannot boot Windows off virtual SATA controller right away, it is probably due to the lack of SATA drivers. Attach virtual disk to IDE controller, create an empty SATA controller and boot the virtual machine - Windows should automatically install SATA drivers for the controller. You can then shutdown the virtual machine, detach virtual disk from IDE controller and attach it to SATA controller instead.

#### Fix MBR and Microsoft boot loader

If your Windows virtual machine refuses to boot, you may need to apply the following modifications to your virtual machine. 

  * Boot a GNU/Live live distribution inside your virtual machine before Windows starts up.

  * Remove other partitions entries from the virtual disk MBR. Indeed, since we copied the MBR and only the Windows partition, the entries of the other partitions are still present in the MBR, but the partitions are not available anymore. Use `fdisk` to achieve this for example.

    fdisk ''/dev/sda''
    Command (m for help): a
    Partition number (''1-3'', default ''3''): ''1''

  * Write the updated partition table to the disk (this will recreate the MBR) using the `m` command inside `fdisk`.

  * Use [testdisk](<https://archlinux.org/packages/?name=testdisk>)包 (see [here](<https://www.cgsecurity.org/index.html?testdisk.html>) for details) to add a generic MBR:

    # testdisk > _Disk /dev/sda..._ > [Proceed] > [Intel] Intel/PC partition > [MBR Code] Write TestDisk MBR to first sector > Write a new copy of MBR code to first sector? (Y/n) > Y > Write a new copy of MBR code, confirm? (Y/N) > A new copy of MBR code has been written. You have to reboot for the change to take effect. > [OK]

  * With the new MBR and updated partition table, your Windows virtual machine should be able to boot. If you are still encountering issues, boot your Windows recovery disk from on of the previous step, and inside your Windows RE environment, execute the commands [described here](<https://support.microsoft.com/kb/927392>).

#### Known limitations

  * Your virtual machine can sometimes hang and overrun your RAM, this can be caused by conflicting drivers still installed inside your Windows virtual machine. Good luck to find them!
  * Additional software expecting a given driver beneath may either not be disabled/uninstalled or needs to be uninstalled first as the drivers that are no longer available.
  * Your Windows installation must reside on the first partition for the above process to work. If this requirement is not met, the process might be achieved too, but this had not been tested. This will require either copying the MBR and editing in hexadecimal see [VirtualBox: booting cloned disk](<https://superuser.com/questions/237782/virtualbox-booting-cloned-disk/253417#253417>) or will require to fix the partition table [manually](<https://gparted.org/h2-fix-msdos-pt.php>) or by repairing Windows with the recovery disk you created in a previous step. Let us consider our Windows installation on the second partition; we will copy the MBR, then the second partition where to the disk image. `VBoxManage convertfromraw` needs the total number of bytes that will be written: calculated thanks to the size of the MBR (the start of the first partition) plus the size of the second (Windows) partition. `{ dd if=/dev/sda bs=512 count=$(cat /sys/block/sda/sda1/start) ; dd if=/dev/sda2 bs=512 count=$(cat /sys/block/sda/sda2/size) ; } | VBoxManage convertfromraw stdin windows.vdi $(( ($(cat /sys/block/sda/sda1/start) + $(cat /sys/block/sda/sda2/size)) * 512 ))`.

### Run a native Windows installation inside VirtualBox

**注意：** The technique outlined in this section only applies to [UEFI](<../zh-cn/UEFI.html> "UEFI") systems.

In some cases, it is useful to be able to [dual boot with Windows](<../zh-cn/Dual_boot_with_Windows.html> "Dual boot with Windows") _and_ access the partition in a virtual machine. This process is significantly different from [#Move a native Windows installation to a virtual machine](<#Move_a_native_Windows_installation_to_a_virtual_machine>) in several ways: 

  * The Windows partition is not copied to a virtual disk image. Instead, a raw VMDK file is created;
  * Changes in the virtual machine will be mirrored in the partition, and vice versa;
  * OEM licenses should still be satisfied, since the Windows partition still boots directly on the hardware.

**警告：** Some of the commands used here can corrupt either the Windows partition, the Arch Linux partition, or both. Use extreme caution when executing commands, and double check that they are being run in the correct shell. It would be a good idea to have a backup of the entire drive ready before beginning this process.

**注意：** Before proceeding be sure to have access to a Windows installation media (such as the [Windows 11 ISO](<https://www.microsoft.com/en-us/software-download/windows11>)).

#### Creating the virtual machine

A VirtualBox virtual machine must be manually created. As of now do not add any storage device any disk to the virtual machine, it will be done manually later. 

Configure the virtual machine with the following settings (settings panel can be opened by clicking the "Settings" button in the main toolbar): 

  * View: System: 
    * Tab: Motherboard: 
      * mark _Enable I/O APIC_ ;
      * mark _Enable EFI_ ;
      * mark _Hardware Clock in UTC Time_ if is your case.
    * Tab: Processor: 
      * mark _Enable PAE/NX_ ;
      * mark _Enable Nested VT-x/AMD-V_ ;
    * Tab: Acceleration: 
      * Choose the paravirtualization interface _Hyper-V_ from the drop down menu;
      * mark _Enable Nested Paging_.

Optionally you can enable also the following settings: 

  * View: Display 
    * Tab: Screen 
      * mark _Enable 3D Acceleration_. Note that it could cause glitches.

**注意：** The _Hyper-V_ setting is not required in order for the system to operate correctly, but it may help avoid licensing issues.

#### Creating virtual machine disks

To access the Windows partitions, create a [raw VMDK file](<https://www.virtualbox.org/manual/ch09.html#rawdisk-access-disk-partitions>) pointing to the relevant Windows partitions (root privileges are required to read disk partition table): 
    
    # VBoxManage createmedium disk -filename _VM_DIRECTORY_ /windows.vmdk --format=VMDK --variant RawDisk --property RawDrive=_DISK_ --property Partitions=_RESERVED_PARTITION_NUMBER_ ,_BASIC_DATA_PARTITION_NUMBER_
    
Replace capitalized placeholder strings as follow: 

  * `_VM_DIRECTORY_` with the path of the virtual machine folder (usually a subdirectory of `~/VirtualBox VMs`;
  * `_DISK_` must be replaced with the block device containing all the Windows partitions (e.g.: `/dev/sda` or `/dev/nvme0n1`);
  * `_RESERVED_PARTITION_NUMBER_` must be replaced with the number of partition labeled "Microsoft reserved partition" (e.g.: if the partition is the `/dev/sda2` the number will be `2`);
  * `_BASIC_DATA_PARTITION_NUMBER_` must be replaced with the partition containing the Windows installation (e.g.: if the partition is the `/dev/sda3` the number will be `3`);

Example: 
    
    # VBoxManage createmedium disk -filename "/home/user/VirtualBox VMs/windows.vmdk" --format=VMDK --variant RawDisk --property RawDrive=/dev/nvme0n1 --property Partitions=2,3
    
The command will also create an extra file inside the virtual machine folder, "windows-pt.vmdk", that will be just ignored. 

**注意：**`windows.vmdk` must be re-created if the partition table is changed.

**提示：**

Partition numbers can be found also by running this command and looking at the MIN column: 
    
    lsblk --output NAME,PARTLABEL,FSTYPE,MAJ:MIN,SIZE
    
    NAME        PARTLABEL                    FSTYPE UUID                                 MAJ:MIN   SIZE
    nvme0n1                                                                              259:0   931,5G
    ├─nvme0n1p1 EFI system partition         vfat   90DC-A6B3                            259:1     100M
    ├─nvme0n1p2 Microsoft reserved partition                                             259:2      16M
    ├─nvme0n1p3 Basic data partition         ntfs   D2A2A104A2A0EE63                     259:3     200G
    ...

Now change the virtual disk owner to give access the user and group running VirtualBox. 
    
    # chown _VIRTUALBOX_RUNNING_USER_ :_VIRTUALBOX_RUNNING_GROUP_ _VM_DIRECTORY_ /windows.vmdk _VM_DIRECTORY_ /windows-pt.vmdk

Replace `_VIRTUALBOX_RUNNING_USER_` and `_VIRTUALBOX_RUNNING_GROUP_` with the user and the group that will run VirtualBox, which most likely will be your user. 

#### Allowing VirtualBox to read physical partitions

VirtualBox must have [raw disk access](<https://www.virtualbox.org/manual/ch09.html#rawdisk>) in order to run a Windows partition. Normally, this would require VirtualBox to be run with full root privileges, but more elegant options are available. 

##### Higher security option: using a dedicated group for the Windows partitions

Here [udev](<../zh-cn/Udev.html> "Udev") is configured to restrict the access to partitions Windows partitions to the _vboxusers_ group, and then the user running VirtualBox is added to the group. 

Assigning the disks to the _vboxusers_ group can be done automatically by creating the following file: 
    
    /etc/udev/rules.d/99-vbox.rules
    
    #
    # Rules to give VirtualBox users raw access to Windows partitions
    #
    
    # Microsoft Reserved partition
    SUBSYSTEM=="block", ENV{ID_PART_ENTRY_TYPE}=="e3c9e316-0b5c-4db8-817d-f92df00215ae", GROUP="vboxusers"
    
    # Windows partition
    SUBSYSTEM=="block", ENV{ID_PART_ENTRY_TYPE}=="ebd0a0a2-b9e5-4433-87c0-68b6b72699c7", GROUP="vboxusers"
    
    #
    # Rules to give VirtualBox users raw access to Windows disk
    #
    
    # sdb
    ENV{ID_PART_TABLE_UUID}=="WINDOWS_DISK_ID_PART_TABLE_UUID", GROUP="vboxusers"
    
`WINDOWS_DISK_ID_PART_TABLE_UUID` must be replaced with the value obtained from `udevadm info /dev/WINDOWS_DISK ` (replace `WINDOWS_DISK` with the disk containing Windows partitions). The UUIDs in these rules correspond to particular [GPT partition types](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs> "wikipedia:GUID Partition Table") while the other capitalized strings are supposed to be written that way, so those does not have to be replaced. 

Then the user running VirtualBox must be added to the _vboxusers_ group. This can be done with the following command: 
    
    # usermod -aG vboxusers VIRTUALBOX_RUNNING_USER
    
Replace `VIRTUALBOX_RUNNING_USER` and with the user that will run VirtualBox, which most likely will be your user. 

#####  Lower security option: using 'disk' group

To be able to add the VMDK file in VirtualBox Virtual Media Manager without running VirtualBox as root, the user running VirtualBox need to be in `vboxusers` and `disk` groups. 
    
    # usermod -aG disk,vboxusers VIRTUALBOX_RUNNING_USER

Replace `VIRTUALBOX_RUNNING_USER` and with the user that will run VirtualBox, which most likely will be your user. 

**警告：** Be aware of the potential security implications of this edit, as you are giving your user account full read-write access all storage devices owned by the disk group.

#### Setting up a separate EFI system partition

Virtual machine EFI boot files will refer to different disks than the ones in the physical EFI system partition, so VirtualBox must not make use of the latter but instead of an EFI system partition inside a dedicated virtual disk. This disk can be created with the following command: 
    
    $ VBoxManage createmedium disk --filename _VM_DIRECTORY/esp.vmdk_ --size 512 --format VMDK
    
Replace `VM_DIRECTORY` with the folder containing the virtual machine being built. 

#### Adding virtual disks to the virtual machine

Configure the virtual machine storage devices (Settings panel - Storage) as following: 

  * add `esp.vmdk` as a SATA hard disk attached to the "SATA Port 0";
  * add `windows.vmdk` as a SATA hard disk attached to the "SATA Port 1";
  * mount Windows installation iso into the virtual optical drive .

**注意：**

  * for adding a SATA hard disk use the second button on the right of the "Controller: SATA" device;
  * the virtual optical drive should already be there as "Optical Drive".

#### Configuring the virtual UEFI firmware and creating Windows boot files

Now start the virtual machine and it should automatically boot from Windows installation disk. After choosing the installation locales click on the "Repair your computer" link, then choose "Troubleshoot" and then " Command Prompt" in order to launch a command prompt from the install media. 

Enter the following commands to create a new GPT table in the esp.vmdk disk and install the Windows boot loader onto it using configuration from the existing Windows partition: 

Open Diskpart: 
    
    X:\ diskpart
    
List all disks identified by the system: 
    
    DISKPART> list disk
    
The `esp.vmkd` disk should be labeled as `disk 0` due to the fact that was attached to the SATA port 0, ~512 MiB in size and unpartitioned. The `windows.vmdk` disk should be labeled as `disk 1`; note that the column "Size" displays the disk size, not the partition one. 

Select the esp.vmdk disk: 
    
    DISKPART> select Disk 0
    
Now create a GPT partition table, an EFI system partition, big as the whole disk, and assign to it a label and drive letter: 
    
    DISKPART> clean
    DISKPART> convert gpt
    DISKPART> create partition efi size=500
    DISKPART> format quick fs=fat32 label="System"
    DISKPART> assign letter="S"

Check that the partition has been correctly created: 
    
    DISKPART> list volume
    
Our newly created EFI system partition will be labeled as "SYSTEM" with letter as "S". 

Take note of the Windows installation volume letter because it will be used in next steps. Usually its `D` but it could be different: you can infer it from its label and its size. The size is the same as the Windows installation partition size on your physical hard disk. 

Exit diskpart: 
    
    DISKPART> exit
    
Install the Windows boot loader into the EFI system partition. 
    
    D:
    cd Windows\System32
    bcdboot D:\Windows /s S: /f UEFI
    
Now close the command prompt, power off the virtual machine and detach the Windows installation disk (from "Preferences > Devices" remove the optical disk). The virtual machine should now boot from the newly installed boot partition and load the physical Windows installation. It may show some UEFI related errors on the top of the virtual machine window and the first boot may take a while, but if everything has been done correctly you will be able to access your windows installation. 

### Run an entire physical disk in VirtualBox

**注意：** You may refer to VirtualBox official documentation [9.8.1. Using a Raw Host Hard Disk From a Guest](<https://www.virtualbox.org/manual/ch09.html#rawdisk>).

This works the same way as [#Run a native Windows installation inside VirtualBox](<#Run_a_native_Windows_installation_inside_VirtualBox>) but the vmdk will contain the entire disk rather than one partition, and so you will not need to create a separate ESP or MBR partition as the one in the physical disk will be used. 

Create the raw disk: 
    
    # VBoxManage internalcommands createrawvmdk -filename /path/to/file.vmdk -rawdisk /dev/sdb
    
Then follow the same method as in [#Run a native Windows installation inside VirtualBox](<#Run_a_native_Windows_installation_inside_VirtualBox>) for the configuration and virtual disk attachement. 

### Set guest starting resolution

Typically after installing Guest Additions, a fullscreen Arch guest running X will be set to the optimal resolution for your display; however, the virtual console's framebuffer will be set to a standard, often smaller, resolution detected from VirtualBox's custom VESA driver. 

To use the virtual consoles at optimal resolution, Arch needs to recognize that resolution as valid, which in turn requires VirtualBox to pass this information along to the guest OS. 

First, check if your desired resolution is not already recognized by running the command ([hwinfo](<https://archlinux.org/packages/?name=hwinfo>)包 need to be installed): 
    
    hwinfo --framebuffer
    
If the optimal resolution does not show up, then you will need to run the `VBoxManage` tool on the host machine and add "extra resolutions" to your virtual machine (on a Windows host, go to the VirtualBox installation directory to find `VBoxManage.exe`). For example: 
    
    $ VBoxManage setextradata "Arch Linux" "CustomVideoMode1" "1360x768x24"
    
The parameters "Arch Linux" and "1360x768x24" in the example above should be replaced with your virtual machine name and the desired framebuffer resolution. Incidentally, this command allows for defining up to 16 extra resolutions ("CustomVideoMode1" through "CustomVideoMode16"). Recommended resolutions are 1280x720, 1920x1080, 2048x1080, 2560x1440, 3840x2160, 1280x800, 1280x1024, 1440x900, 1600x900. 

Afterwards, restart the virtual machine and run `hwinfo --framebuffer` once more to verify that the new resolutions have been recognized by your guest system (which does not guarantee they will all work, depending on your hardware limitations). 

**注意：** As of VirtualBox 5.2, `hwinfo --framebuffer` might not show any output, but you should still be able to set a custom resolution following this procedure.

Finally, add a `video=_resolution_` [kernel parameter](<../zh-cn/Kernel_parameter.html> "Kernel parameter") to set the framebuffer to the new resolution, for example: 
    
    video=1360x768
    
Additionally you may want to configure your [boot loader](<../zh-cn/Boot_loader.html> "Boot loader") to use the same resolution. If you use GRUB, see [GRUB/Tips and tricks#Setting the framebuffer resolution](<../zh-cn/GRUB/Tips_and_tricks.html#Setting_the_framebuffer_resolution> "GRUB/Tips and tricks"). 

**注意：** Neither the kernel parameter `vga` nor the boot loader's resolution settings (e.g. GRUB's `GRUB_GFXPAYLOAD_LINUX`) will fix the framebuffer, since they are overriden by virtue of Kernel Mode Setting. The framebuffer resolution must be set by the kernel parameter `video` as described above.

### SSH from host to guest

The network tab of the virtual machine settings contains, in "Advanced", a tool to create port forwarding. It is possible to use it to forward the Guest ssh port `22` to a Host port, e.g. `3022` : 
    
    user@host$ ssh -p 3022 $USER@localhost
    
will establish a connection from Host to Guest. 

#### SSHFS as alternative to shared folders

Using this port forwarding and [SSHFS](<../zh-cn/SSHFS.html> "SSHFS") it is straightforward to mount the Guest filesystem onto the Host one: 
    
    user@host$ sshfs -p 3022 $USER@localhost:$HOME ~/shared_folder
    
and then transfer files between both. 

### Specify Host-Only Network

For security reasons, the VirtualBox network driver limits the usable subnet ranges. This will cause `E_ACCESSDENIED` errors when changing the virtual network adapter settings[[5]](<https://www.virtualbox.org/manual/ch06.html#network_hostonly>). You can change the allowed list of networks by adding them to `/etc/vbox/networks.conf`. 

For example: 
    
         * 10.0.0.0/8 192.168.0.0/16
         * 2001:db8:1234::/48
    
**注意：** The spaces and asterisk are important.

For IPv6 it is best practice to generate a new, randomized [ULA prefix](<https://datatracker.ietf.org/doc/html/rfc4193>). 

Do not forget to reload the driver and restart VirtualBox after changing `/etc/vbox/networks.conf`: 
    
    # modprobe -r vboxnetadp vboxnetflt
    # modprobe vboxnetadp vboxnetflt
    
##  故障排除

###  鼠标键盘都锁死在虚拟机里了

这是因为你的虚拟机捕获了键盘与鼠标的输入。只要按下右 `Ctrl` 键即可让输入焦点回到宿主系统。 

如果想要不按切换键就能让鼠标在宿主机与虚拟机之间无缝切换，需要在客户机中安装[客户机插件](<#%E5%AE%A2%E6%88%B7%E6%9C%BA%E6%8F%92%E4%BB%B6>)。如果你的虚拟机系统是 Arch Linux，请参考 [/在虚拟机中安装 Arch Linux#安装客户机插件](<../zh-cn/VirtualBox/%E5%9C%A8%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%E5%AE%89%E8%A3%85_Arch_Linux.html#%E5%AE%89%E8%A3%85%E5%AE%A2%E6%88%B7%E6%9C%BA%E6%8F%92%E4%BB%B6> "VirtualBox/在虚拟机中安装 Arch Linux")，其他系统请参阅 VirtualBox 的官方帮助文档。 

###  无法新建 64 位虚拟机

如果新建虚拟机时看不到 64 位系统选项，需先确保已在 BIOS 中启用 CPU 虚拟化技术（通常称作 `VT-x`）。 

如果你的宿主系统是 Windows，那么你得禁用 Hyper-V 功能，因为 Hyper-V 会妨碍 VirtualBox 使用 VT-x。[[6]](<https://www.virtualbox.org/ticket/12350>)

###  VirtualBox 图形管理界面和主机 GTK 主题样式不匹配

如需修改类似 VirtualBox 的 Qt 应用的外观，请参考[统一 Qt 和 GTK 应用程序的外观](<../zh-cn/%E7%BB%9F%E4%B8%80_Qt_%E5%92%8C_GTK_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%A4%96%E8%A7%82.html> "统一 Qt 和 GTK 应用程序的外观")。 

###  无法向虚拟机键入 Ctrl+Alt+Fn

如果你在虚拟机安装了某个 Linux 发行版，有时会需要按 `Ctrl+Alt+F2` 进入它的 TTY 界面，或者按 `Ctrl+Alt+Backspace` 来退出 X 会话。如果你的宿主系统也是 Linux，这些组合键默认会首先被宿主系统捕获。正确的做法是按 _Host Key_ （默认是右 `Ctrl`）加 `F2` 来向虚拟机键入 `Ctrl+Alt+F2`。 

###  USB 功能不可用

在宿主系统里使用虚拟机的用户需被加入到 `vboxusers` 用户组。如果想要支持 USB 2 设备，还要安装[扩展包](<#%E6%89%A9%E5%B1%95%E5%8C%85>)。此后在虚拟机的设置里即可开启 USB 2 支持，并能通过过滤规则来允许客体系统访问指定的 USB 设备。 

如果用 root 身份运行 `VBoxManage list usbhost` 命令也没有列出任何 USB 设备，需要确认一下 `/etc/udev/rules.d/` 目录里没有遗留的 VirtualBox 4.x 的 udev 规则。VirtualBox 5.0 起会把 udev 规则文件安装到 `/usr/lib/udev/rules.d/` 目录。用 `pacman -Qo /usr/lib/udev/rules.d/60-vboxdrv.rules` 命令可以查看这些 udev 文件是否已经过期。 

有时某些旧 Linux 宿主系统无法自动检测到 USB 子系统，就会出现这个错误：`Could not load the Host USB Proxy service: VERR_NOT_FOUND`。或者可能让宿主机也识别不了 USB 磁盘，[哪怕用户已经加入了 **vboxusers** 用户组](<https://bbs.archlinux.org/viewtopic.php?id=121377>)。出现这类问题的原因是 VirtualBox 从 3.0.8 版本开始，从 _usbfs_ 转向使用 _sysfs_ 。如果宿主系统不支持这一改动，你可以在 shell 的启动脚本（举例：如果在用 _bash_ 的话，就修改 `~/.bashrc` 文件）里声明这一环境变量，让 VirtualBox 回退到旧的行为： 
    
    ~/.bashrc
    
    VBOX_USB=usbfs

然后确保这行代码对环境变量的修改生效：重新登录，手动加载该文件，启动一个新 shell 会话，或者干脆重启。 

另外，还应确保用户加入到了 `storage` 用户组。 

###  USB 调制解调器在宿主系统不可用

如果你的客户机正在使用 USB 调制解调器，杀掉虚拟机进程可能会造成它在宿主系统里不可用。杀掉并重启余下的 `VBoxSVC` 进程应该可以解决这一问题。 

### USB device crashes guest

If attaching a USB device to the guest causes a crash or any other erroneous behavior, try switching the USB controller from USB 2 (EHCI) to USB 3 (xHCI) or vice versa. 

###  虚拟机启动时宿主系统卡死

一般来说，这类问题都是在 VirtualBox 或 Linux 内核版本更新之后出现。降级回到前一个版本就有可能解决问题。 

###  模拟信号麦克风不可用

如果从模拟信号麦克风输入的音频信号在宿主机可用，但在客户机里不可用，可以试试在宿主机上安装 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 之类的[音频服务器](<../zh-cn/%E9%9F%B3%E9%A2%91%E7%B3%BB%E7%BB%9F.html#%E9%9F%B3%E9%A2%91%E6%9C%8D%E5%8A%A1%E5%99%A8> "音频系统")。 

如果装了 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 之后麦克风还是不能用，在菜单项 _VirtualBox > Machine > Settings > Audio_ 里把 _Host Audio Driver_ 的值改成 _ALSA Audio Driver_ 也许有用。 

###  映像转换成的 ISO 文件有问题

有些映像文件格式无法可靠地转换到 ISO 格式。例如：[ccd2iso](<https://archlinux.org/packages/?name=ccd2iso>)包 在转换时会忽略 .ccd 和 .sub 文件里的信息，最终产出的 ISO 镜像里的文件就可能出现损坏。 

为了避免这种情况，可以使用 [CDemu](<../zh-cn/CDemu.html> "CDemu") 或类似软件在 Linux 客户机里挂载光盘映像。 

###  仅主机网卡创建失败

确保所需的内核模块都已成功加载。详见 [#加载 VirtualBox 内核模块](<#%E5%8A%A0%E8%BD%BD_VirtualBox_%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97>)。 

如果还是不行，点击 _文件 > 主机网络管理器_，点击 _创建_ 进行手动创建。 

###  插入模块失败

如果你在加载模块时遇到如下错误信息： 
    
    Failed to insert 'vboxdrv': Required key not available
    
将[模块签名](<#%E6%A8%A1%E5%9D%97%E7%AD%BE%E5%90%8D>)，或者在内核配置中禁用 `CONFIG_MODULE_SIG_FORCE`。 

###  VBOX_E_INVALID_OBJECT_STATE (0x80BB0007)

如果虚拟机没有正常退出，就可能出现这个错误。试试下面这个命令： 
    
    $ VBoxManage controlvm _virtual_machine_name_ poweroff
    
###  NS_ERROR_FAILURE 且菜单项缺失

在没有更新[扩展包](<#%E6%89%A9%E5%B1%95%E5%8C%85>)，导致其与新版 VirtualBox 不兼容时就会出现该报错。 

如果在创建虚拟机时选择了 _QCOW_ /_QCOW2_ /_QED_ 虚拟盘格式，有时也可能会出现这个错误。 

如果初次启动虚拟机时遇到下面的错误消息： 
    
    Failed to open a session for the virtual machine debian.
    Could not open the medium '/home/.../VirtualBox VMs/debian/debian.qcow'.
    QCow: Reading the L1 table for image '/home/.../VirtualBox VMs/debian/debian.qcow' failed (VERR_EOF).
    VD: error VERR_EOF opening image file '/home/.../VirtualBox VMs/debian/debian.qcow' (VERR_EOF).
    
    Result Code:
    NS_ERROR_FAILURE (0x80004005)
    Component:
    Medium
    
退出 VirtualBox，把新虚拟机的文件都删除，并且在 VirtualBox 的配置文件中找到 `MachineRegistry` 元素，从这里删除你所创建的格式错误的虚拟机（一般是其最后一个子元素）： 
    
    ~/.config/VirtualBox/VirtualBox.xml
    
    ...
    <MachineRegistry>
      <MachineEntry uuid="{00000000-0000-0000-0000-000000000000}" src="/home/void/VirtualBox VMs/debian/debian.vbox"/>
      <MachineEntry uuid="{00000000-0000-0000-0000-000000000000}" src="/home/void/VirtualBox VMs/ubuntu/ubuntu.vbox"/>
      ~~< MachineEntry uuid="{00000000-0000-0000-0000-000000000000}" src="/home/void/VirtualBox VMs/lastvmcausingproblems/lastvmcausingproblems.qcow"/>~~
    </MachineRegistry>
    ...

###  缺少硬件虚拟化导致 OpenBSD 不稳定

据称在其他的虚拟机平台上，OpenBSD 可以不依赖虚拟化指令集（VT-X，AMD-V）正常运行，VirtualBox 上的 OpenBSD 则不然。具体现象是出现大量的分段错误（segfault）。在启动虚拟机时加上 _-norawr0_ 参数[可能有效](<https://www.virtualbox.org/ticket/3947>)，例如： 
    
    $ VBoxSDL -norawr0 -vm _name_of_OpenBSD_virtual_machine_
    
###  Windows: "The specified path does not exist. Check the path and then try again."

当在 Windows 客户机里运行位于共享目录里 _.exe_ 程序，而这一程序又需要管理员权限时，就可能出现这一错误信息。[[7]](<https://www.virtualbox.org/ticket/5732#comment:39>)

一个解决办法是把文件复制到虚拟硬盘上再运行。或者直接从 [UNC 路径](<https://en.wikipedia.org/wiki/Uniform_Naming_Convention> "wikipedia:Uniform Naming Convention") (`\\vboxsvr`) 运行程序。详见 [[8]](<https://support.microsoft.com/de-de/help/2019185/copying-files-from-a-mapped-drive-to-a-local-directory-fails-with-erro>)。 

###  Windows 8.x 出现错误代码 0x000000C4

如果你在创建虚拟机时选择了 Win 8 系统，但在启动时还是遇到这一错误，可以尝试启用 `CMPXCHG16B` CPU 指令集。命令如下： 
    
    $ vboxmanage setextradata _virtual_machine_name_ VBoxInternal/CPUM/CMPXCHG16B 1
    
###  Windows 8, 8.1 或 10 无法安装、启动或报错 "ERR_DISK_FULL"

修改虚拟机设置，在菜单项 _Settings > Storage > Controller:SATA_ 里勾选 "Use Host I/O Cache"。 

###  WinXP: 颜色深度不得多于 16 位

如果只显示 16 位色，桌面图标看起来会模糊 / 结块。但是将色深调高时，系统可能会将桌面分辨率限制得较低，或者根本不允许改变色深。解决办法是在 Windows XP 虚拟机里运行 `regedit`，并写入这一项注册表值： 

If you are running at 16-bit color depth, then the icons may appear fuzzy/choppy. However, upon attempting to change the color depth to a higher level, the system may restrict you to a lower resolution or simply not enable you to change the depth at all. To fix this, run `regedit` in Windows and add the following key to the Windows XP virtual machine's registry: 
    
    [HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services]
    "ColorDepth"=dword:00000004
    
然后再去“桌面属性”窗口里修改色深。如果还是不见效，强制让屏幕重绘（比如按 `Host+f` 进入全屏模式）试试。 

###  Windows: 开启 3D 加速后屏幕闪烁

VirtualBox > 4.3.14 存在问题，会导致启用 3D 加速的 Windows 虚拟机出现闪烁。r120678 版本引入了一个补丁，可以参考如下通过[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")添加设置： 
    
    $ CR_RENDER_FORCE_PRESENT_MAIN_THREAD=0 VirtualBox
    
请确保没有 VirtualBox 服务还在运行，并参考[VirtualBox bug 13653](<https://www.virtualbox.org/ticket/13653>)。 

###  无法在 Wayland 上启动 VirtualBox：段错误

该问题是由于 Qt 检测到了 Wayland（例如 `XDG_SESSION_TYPE=wayland`），而 VirtualBox 暂不支持 Wayland。请参考 [FS#58761](<https://bugs.archlinux.org/task/58761>) 和 [上游 bug 工单](<https://www.virtualbox.org/ticket/18679>)。 

可以通过设置 `QT_QPA_PLATFORM=xcb` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") 来禁用 Qt 平台检测，并强制使用 X11。 

为避免影响其它在 Wayland 中可以正常使用的 Qt 应用，应只在启动 VirtualBox 时配置 `QT_QPA_PLATFORM=xcb` 环境变量。 

如果 VirtualBox 是通过[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")启动的，请参考[桌面项#编辑环境变量](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html#%E7%BC%96%E8%BE%91%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F> "桌面项")将 `Exec=VirtualBox ...` 开头的一行修改为 `Exec=env QT_QPA_PLATFORM=xcb VirtualBox ...`。如果是从 shell 命令行启动的，可以将 `virtualbox` 别名（[Bash#别名](<../zh-cn/Bash.html#%E5%88%AB%E5%90%8D> "Bash")）设为 `env QT_QPA_PLATFORM=xcb virtualbox`。 

**注意：** 如果你在 Wayland 下有鼠标和键盘相关的问题，也可以试试上述配置。

### Random freezing in guests with Intel GPU

With Intel CPU and graphics, allocating more processors for the guest can lower render performance, thus cause random freezing. Allocating less processors can help. 

### Unable to view desktop in fullscreen mode

Disable the Mini Toolbar by selecting _Machine > Settings_, select the _User Interface_ tab and uncheck the _Mini Toolbar_ checkbox 

### Random crashes with Windows 10 guest operating system with Intel Tiger Lake chipset

Disable split lock detection by adding `split_lock_detect=off` to the [kernel parameter](<../zh-cn/Kernel_parameter.html> "Kernel parameter")s. 

Details are described in VirtualBox's [Ticket #20180](<https://www.virtualbox.org/ticket/20180#comment:8>). 

### Failed to save the settings when enabling Secure Boot

In VirtualBox 7.0.0, enabling Secure Boot in a virtual machine that was created in a previous VirtualBox version will fail with a nondescript error ([FS#76234](<https://bugs.archlinux.org/task/76234>)): 
    
    Failed to save the settings.
    
The solution is to click the _Reset Keys to Default_ button right below the _Enable Secure Boot_ checkbox. 

### Failed to start VirtualBox machine after using Android Studio emulator

KVM and VirtualBox kernel modules can be loaded but not used simultaneously. Android Studio emulator is a QEMU emulator, which uses KVM for acceleration. So Android Studio emulator and VirtualBox machine (if hardware acceleration is enabled) cannot run at the same time. We have to use one after the other stopped completely. 

Sometimes, VirtualBox kernel module can still be used unexpectedly by some process, and keep all VirtualBox machines failing to start, the error message on VirtualBox GUI is "A critical error has occurred". 

At this time, we can check and reload VirtualBox kernel modules using `vboxreload` as root. If it saying some modules is still be in use, you need to manually kill related process and rerun the command. 

### 3D Acceleration is not working

  * Make sure guest additions are installed on guest, and the host modules are installed on the host
  * Make sure the guest additions and host kernel modules versions match 
    * host: `modinfo vboxdrv | grep '^version:'`
    * guest: open logs of your VM, find "Guest Additions information report"
  * Make sure vulkan is installed and [working](<../zh-cn/Vulkan.html#Verification> "Vulkan") on the host

### VirtualBox UI elements are improperly rendered with Kvantum installed

On some configurations of Kvantum ([kvantum](<https://archlinux.org/packages/?name=kvantum>)包) with third party themes, some UI elements such as toolbars and menus are rendered black or improperly. This seems to be limited to translucent windows being enabled. See Kvantum's issue [#418](<https://github.com/tsujan/Kvantum/issues/418>). 

To fix this behavior, do one of: 

  * Disable _Translucent windows_ under section _Configure Active Theme > Compositing & General Look_ of _Kvantum Manager_.
  * Add `VirtualBox,VirtualBoxVM` in _Kvantum Manager_ , to the _Configure Active Theme > Compositing & General Look > Opaque apps:_ menu field. 
    * This makes an exception for virtualbox windows to be ignored.

###  VirtualBox is taking exclusive control of an audio device, preventing PipeWire from accessing it while the virtual machine is running

By default, VirtualBox should auto-select the best audio driver. However, on PipeWire systems this often falls back to ALSA (see [Pipewire issue](<https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/1672>)). 

It could cause journal records like these: 
    
    pipewire[2370]: spa.audioadapter: params Spa:Enum:ParamId:EnumFormat: 1:0 (convert format) Device or reso>
    pipewire[2370]: pw.node: (alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Speaker__sink-6>
    pipewire[2370]: spa.alsa: '_ucm0001.hw:sofhdadsp': playback open failed: Device or resource busy
    
The solution is to configure VirtualBox to use the PulseAudio backend (which PipeWire will handle [via pipewire-pulse](<../zh-cn/PipeWire.html#PulseAudio_clients> "PipeWire")): 
    
    $ VBoxManage modifyvm "_Your_virtual_machine_name_ " --audio-driver pulse --audio-controller hda
    
##  参阅

  * [User Guide](<https://www.virtualbox.org/manual/UserManual.html>) on a single HTML page
