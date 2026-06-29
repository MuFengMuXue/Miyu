相关文章

  * [分类:虚拟机管理](<../zh-cn/Category:%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%AE%A1%E7%90%86.html> "Category:虚拟机管理")
  * [/安装 Arch Linux 为虚拟机](<../zh-cn/VMware/%E5%AE%89%E8%A3%85_Arch_Linux_%E4%B8%BA%E8%99%9A%E6%8B%9F%E6%9C%BA.html> "VMware/安装 Arch Linux 为虚拟机")
  * [Moving an existing install into (or out of) a virtual machine](</wzh/index.php?title=Moving_an_existing_install_into_\(or_out_of\)_a_virtual_machine&action=edit&redlink=1> "Moving an existing install into \(or out of\) a virtual machine（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [VMware](<https://wiki.archlinux.org/title/VMware> "arch:VMware")，最近一次同步于 2025-07-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/VMware?diff=0&oldid=835397>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/VMware_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** need translation（在 [Talk:VMware#](<../zh-cn/Talk:VMware.html>) 中讨论）

本文介绍的是最新的主要 [VMware](<https://zh.wikipedia.org/wiki/VMware> "zhwp:VMware") 版本，即 [VMware Workstation](<https://zh.wikipedia.org/wiki/VMware_Workstation> "zhwp:VMware Workstation") Pro 和 Player 17、16、15、14 和 12.5。 

你可能也会想了解下 [/安装 Arch Linux 为虚拟机](<../zh-cn/VMware/%E5%AE%89%E8%A3%85_Arch_Linux_%E4%B8%BA%E8%99%9A%E6%8B%9F%E6%9C%BA.html> "VMware/安装 Arch Linux 为虚拟机")。 

##  安装

**注意：** 自版本 14 以来，VMware 已放弃对许多 CPU 的支持，包括早期的 Intel Core i7 CPU。请检查[主机 CPU 要求](<https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/17-0/using-vmware-workstation-pro/introduction-and-system-requirements/host-system-requirements-for-workstation-pro/processor-requirements-for-host-systems.html>)，并确保 BIOS/UEFI 固件中启用了 CPU 的虚拟化技术（AMD-V 或 VT-x）。如果较新版本不支持您的 CPU，则可以使用 [vmware-workstation12](<https://aur.archlinux.org/packages/vmware-workstation12/>)AUR。

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [vmware-workstation](<https://aur.archlinux.org/packages/vmware-workstation/>)AUR 和已安装内核对应的头文件包（例如 [linux-headers](<https://archlinux.org/packages/?name=linux-headers>)包 或 [linux-lts-headers](<https://archlinux.org/packages/?name=linux-lts-headers>)包）。 

然后[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `vmware-networks-configuration.service` 来生成 `/etc/vmware/networking` 文件。 

最后，根据需要启用以下一些服务： 

  * `vmware-networks.service` 用于虚拟机网络访问（否则您将收到错误 `could no connect 'ethernet 0' to virtual network` 并且您将无法使用 _vmware-netcfg_ ）
  * `vmware-usbarbitrator.service` 用于将 USB 设备连接到虚拟机
  * `vmware-hostd.service` 用于共享虚拟机（从版本 16 起不可用）

最后，加载 VMware 模块： 
    
    # modprobe -a vmw_vmci vmmon
    
如果加载时长时间无响应，请参考 [#无法加载 vmmon 模块](<#%E6%97%A0%E6%B3%95%E5%8A%A0%E8%BD%BD_vmmon_%E6%A8%A1%E5%9D%97>)。 

##  用法

打开 VMware Workstation Pro： 
    
    $ vmware
    
打开 VMware Player： 
    
    $ vmplayer
    
##  技巧和诀窍

###  输入 Workstation Pro 许可证密钥

####  从终端输入
    
    # /usr/lib/vmware/bin/vmware-vmx-debug --new-sn XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    
其中 `XXXXX-XXXXX-XXXXX-XXXXX-XXXXX` 是许可证密钥 

**注意：**`-debug` 二进制文件会遇到无效许可证时提示用户。

####  从 GUI 输入

如果上述方法不起效，您可以尝试： 
    
    # /usr/lib/vmware/bin/vmware-enter-serial
    
###  提取 VMware BIOS
    
    $ objcopy /usr/lib/vmware/bin/vmware-vmx -O binary -j bios440 --set-section-flags bios440=a bios440.rom.Z
    $ perl -e 'use Compress::Zlib; my $v; read STDIN, $v, '$(stat -c%s "./bios440.rom.Z")'; $v = uncompress($v); print $v;' < bios440.rom.Z > bios440.rom
    
###  提取安装程序

要查看安装程序 `.bundle` 中的内容： 
    
    $ sh VMware-_edition_ -_version_._release_._architecture_.bundle --extract _/tmp/vmware-bundle/_
    
####  使用修改后的 BIOS

如果您决定修改提取的 BIOS，您可以通过将其移动到以下位置让虚拟机使用它：`~/vmware/_虚拟机名称_`： 
    
    $ mv bios440.rom ~/vmware/_虚拟机名称_ /
    
然后将名称添加到 `_虚拟机名称_.vmx` 文件: 
    
    ~/vmware/_虚拟机名称_ /_虚拟机名称_.vmx
    
    bios440.filename = "bios440.rom"

###  在 Intel、Optimus 和 AMD 上启用 3D 图形加速

由于 3D 图形加速的性能或稳定性原因，有些图形驱动默认被禁用。在启用 _Accelerate 3D graphics_ 后，可能会出现如下日志： 
    
    Disabling 3D on this host due to presence of Mesa DRI driver.  Set mks.gl.allowBlacklistedDrivers = TRUE to override.
    
日志提到的设置对应的配置文件为 `~/.vmware/preferences`。 

VMware Workstation 16.2 从 OpenGL 改用到了 Vulkan，因此设置会有些不同。如果你的驱动不受支持，日志会显示： 
    
    mks Vulkan Renderer: Only the AMDVLK driver is supported at this time.
    mks Vulkan Renderer: No supported Vulkan device/driver found (See mks.vk.allowUnsupportedDevices or mks.vk.forceDevice configuration options).
    
如果你的驱动被禁用，你得把 `mks.vk.allowUnsupportedDevices = "TRUE"` 添加到 `~/.vmware/preferences` 或者换一个支持的驱动 - 如果不确定要进行哪种操作，就看看虚拟机目录里的 `vmware.log`。 

**注意：** You might need to add the `mks.gl.allowBlacklistedDrivers = "TRUE"` inside the `.vmx` file for the specific virtual machine as well, for 3D acceleration with `intel` drivers to be enabled.

###  在主机挂起/休眠之前挂起虚拟机

创建一个[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")文件： 
    
    /usr/lib/systemd/system-sleep/vmware_suspend_all.sh
    
    #!/bin/bash
    
    set -eu
    
    if [[ $# -ne 2 ]]; then
        echo "Usage: $0 <period> <action>"
        exit 1
    fi
    
    period=$1
    action=$2
    
    echo "vmware system-sleep hook argv: ${period} ${action}"
    
    if ! command -v vmrun &>/dev/null; then
        echo "command not found: vmrun"
    fi
    
    if [[ "${period}" = "pre" ]]; then
        readarray -t vms < <(vmrun list | tail -n +2)
    
        echo "Number of running VMs: ${#vms[@]}"
    
        if [[ ${#vms[@]} -eq 0 ]]; then
            exit
        fi
    
        for vm in "${vms[@]}"; do
            echo -n "Suspending ${vm}... "
            vmrun suspend "${vm}"
            echo "done"
        done
    
        sleep 1
    else
        echo "Nothing to do"
    fi
    
See also [Power management/Suspend and hibernate#Hooks in /usr/lib/systemd/system-sleep](<../zh-cn/Power_management/Suspend_and_hibernate.html#Hooks_in_/usr/lib/systemd/system-sleep> "Power management/Suspend and hibernate"), [suspend all virtual machines with vmrun](<https://superuser.com/questions/119313/vmware-workstation-suspend-all-virtual-machines-with-vmrun>) and [Support for hibernation](<https://communities.vmware.com/thread/439380>). 

###  系统提速技巧

参考[性能优化](<../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96.html> "性能优化")。 

####  禁用透明大页

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[Improving performance](<../zh-cn/Improving_performance.html> "Improving performance")。**

**附注：** Not specific to VMware.（在 [Talk:VMware](<../zh-cn/Talk:VMware.html>) 中讨论）

If you notice the guest and/or the host frequently freezing when running a VM, you may want to disable transparent hugepages. To disable them for the current session, run (on the host): 
    
    # echo never > /sys/kernel/mm/transparent_hugepage/enabled
    
To make the change persistent across boots, add the [kernel parameter](<../zh-cn/Kernel_parameter.html> "Kernel parameter") `transparent_hugepage=never`. 

You can also use `madvise` instead of `never` to still allow applications that are optimized for transparent hugepages to obtain the performance benefits[[1]](<https://blog.nelhage.com/post/transparent-hugepages/>). This does the same for vmware as above. 

####  确保直接访问内存

默认情况下，VMware 会将虚拟机系统的内存写入到硬盘上的文件内。如果你确定内存空间足够，可以添加以下设置到虚拟机的 `.vmx` 文件内以确保虚机系统直接写入到内存中： 
    
    _Virtual_machine_name_.vmx
    
    MemTrimRate = "0"
    sched.mem.pshare.enable = "FALSE"
    prefvmx.useRecommendedLockedMemSize = "TRUE"
    mainmem.backing = "swap"

###  性能提示

要提升虚拟机的性能，可以参考下列技巧： 

####  准虚拟化 SCSI 适配器

[VMware 准虚拟化 SCSI（PVSCSI）适配器](<https://kb.vmware.com/kb/1010398>)是用于 VMware ESXi 的高性能存储适配器，可以达到更高的吞吐量和更低 CPU 占用。PVSCSI 适配器适用于需要高 I/O 吞吐量的软硬件环境。 

SCSI 适配器类型 `VMware Paravirtual` 可在虚拟机设置中应用。 

如果在虚拟机设置中没有这些选项，也还是可以启用准虚拟化 SCSI 适配器。首先，通过修改 `mkinitcpio.conf` 确保准虚拟化 SCSI 适配器包含在内核镜像中： 
    
    /etc/mkinitcpio.conf
    
    ...
    MODULES=(... vmw_pvscsi)
    ...

[重新生成 initramfs](<../zh-cn/%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90_initramfs.html> "重新生成 initramfs")。 

关闭虚拟机，并修改 SCSI 适配器：修改 `.vmx` 中的对应项为如下： 
    
    scsi0.virtualDev = "pvscsi"
    
####  准虚拟化网络适配器

VMware 为客户机系统提供了[多种网络适配器](<https://kb.vmware.com/kb/1001805>)。默认适配器通常为 `e1000`，它会模拟一张 Intel 82545EM 千兆以太网卡。该 Intel 网卡通常兼容包括 Arch 在内的多数操作系统的内置驱动。 

为了获得[更高性能和更多特性](<https://rickardnobel.se/vmxnet3-vs-e1000e-and-e1000-part-1/>)（例如多队列支持），可以使用 VMware 原生的 `vmxnet3` 网络适配器。 

Arch 的默认安装方式已包含了 `vmxnet3` 内核模块。通过 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 启用（或者自动检测启用；可通过执行 `lsmod | grep vmxnet3` 检查是否已加载模块）后，关机并按如下步骤在 _.vmx_ 中修改网络适配器类型： 
    
    ethernet0.virtualDev = "vmxnet3"
    
在修改网络适配器后，需要修改网络和 [dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd") 设置以使用新网卡名称和 MAC 地址。 
    
    # dhcpcd _new_interface_name_
    # systemctl enable dhcpcd@_new_interface_name_.service
    
可通过执行 `ip link` 来获取新的网卡名称。 

####  虚拟机设置

下列设置以主机内存占用为代价降低硬盘 I/O,可以提升虚拟机响应度。[Vmware 的 KB1008885](<https://knowledge.broadcom.com/external/article?legacyId=1008885>) 提供了下列优化设置： 
    
    mainMem.useNamedFile = "FALSE"
    MemTrimRate = "0"
    prefvmx.useRecommendedLockedMemSize = "TRUE"
    MemAllowAutoScaleDown = "FALSE"
    sched.mem.pshare.enable = "FALSE"
    
  * **mainMem.useNamedFile** ：仅适用于 Windows 主机，适用于关闭虚拟机时出现高硬盘占用率的情况，该选项会阻止 VMware 创建 _.vmem_ 文件。在 Linux 主机上请使用 _mainmem.backing = "swap"_ 。
  * **MemTrimRate** ：该选项阻止虚拟机释放的内存同时被主机释放掉。
  * **prefvmx.useRecommendedLockedMemSize** ：该选项似乎没有具体功能解释；其作用似乎为防止主机交换虚拟机的部分内存。
  * **MemAllowAutoScaleDown** ：防止 VMware 在无法分配足够内存的情况下调整虚拟机的内存大小。
  * **sched.mem.pshare.enable** ：如果同时运行了多个虚拟机，VMware 会试图在多个虚拟机间寻找并共享相同的内存页。可能产生高 I/O 负载。

也可以在 VMware workstation 的配置窗口内添加如下设置（ _Edit - > Preferences... -> Memory/Priority_）： 
    
    prefvmx.minVmMemPct = "100"
    mainMem.partialLazySave = "FALSE"
    mainMem.partialLazyRestore = "FALSE"
    
  * **prefvmx.minVmMemPct** ：在主机上为虚拟机预留的内存大小百分比。更低的值会允许为虚拟机分配比主机系统可用大小更多的内存。但请注意，该情况很可能会导致高硬盘占用率。如果主机上的内存足够，建议保留该值为 100。
  * **mainMem.partialLazySave** 和 **mainMem.partialLazyRestore** ：这两个选项会防止虚拟机在挂起时创建部分快照。在使用这两个选项时，虚拟机挂起耗时会稍微增加，但会降低 VMware 存储这些数据产生的磁盘占用率。

##  解难答疑

###  Kernel headers for version x.y-zzzz were not found. If you installed them[...]

安装你使用内核所对应的 headers，如 [linux](<https://archlinux.org/packages/?name=linux>)包 对应[linux-headers](<https://archlinux.org/packages/?name=linux-headers>)包

**注意：** 较常见的错误有：更新内核及头文件后，重启一次才能启动到与头文件版本一致的新内核。

###  无法加载 vmmon 模块

根据 [VMware 社区](<https://communities.vmware.com/t5/VMware-Workstation-Pro/Kernel-module-vmmon-not-loading-on-Fedora-21-w-Workstation-11/m-p/2242975#M133526>)中的描述，需要禁用[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")才能加载 `vmmon` 模块。 

###  远程连接 VMware 时提示登录凭据错误

可以通过 `vmware-workstation-server` 服务远程管理 VMware Workstation 已共享的虚拟机，但是，`vmware-authd` 服务中的 [PAM](<../zh-cn/PAM.html> "PAM") 配置问题会导致 `"incorrect username/password"` 报错出现。要修复该问题，需参考如下编辑 `/etc/pam.d/vmware-authd` 文件： 
    
    /etc/pam.d/vmware-authd
    
    #%PAM-1.0
    auth     _required       pam_unix.so_
    account  _required       pam_unix.so_
    password _required       pam_permit.so_
    session  _required       pam_unix.so_
    
然后重启 `vmware` [systemd](<../zh-cn/Systemd.html> "Systemd") 服务。 

你现在可以使用安装过程提供的凭据连接到服务器了。 

**注意：** 启动虚拟机可能需要安装 [libxslt](<https://archlinux.org/packages/?name=libxslt>)包。

###  ALSA 输出问题

要[修复](<https://bankimbhavsar.blogspot.co.nz/2011/09/hd-audio-in-vmware-fusion-4-and-vmware.html>)音频质量问题或启用正确的 HD 音频输出，首先执行： 
    
    $ aplay -L
    
如果要在虚拟机中使用 5.1 声道，请找到 `surround51:CARD=_vendor_name_ ,DEV=_num_`；如果遇到音频质量问题，请找到 `front:CARD=_vendor_name_ ,DEV=_num_`。最后，将名称填入到 `.vmx` 内： 
    
    ~/vmware/_Virtual_machine_name_ /_Virtual_machine_name_.vmx
    
    sound.fileName=_"surround51:CARD=Live,DEV=0"_
    sound.autodetect=_"FALSE"_

另外，需要禁用 [OSS 模拟](<../zh-cn/ALSA.html#OSS_%E5%85%BC%E5%AE%B9%E6%80%A7> "ALSA")。 

###  基于内核的虚拟机（KVM）尚在运行

可以通过如下方法在启动时禁用 `KVM`： 
    
    /etc/modprobe.d/vmware.conf
    
    blacklist kvm
    blacklist kvm-amd   # For AMD CPUs
    blacklist kvm-intel # For Intel CPUs
    
**提示：** 如果加入黑名单后 `kvm` 模块还会加载，且你使用的设备带有 Intel 集成显卡（i915，i965），那有可能需要同时在内核命令行选项中将 `kvmgt` 模块添加到黑名单。详细信息请查阅[内核模块#使用内核命令行_2](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E4%BD%BF%E7%94%A8%E5%86%85%E6%A0%B8%E5%91%BD%E4%BB%A4%E8%A1%8C_2> "内核模块")。

###  在 HiDPI 显示器上，VMware 应用 UI 上的图标及间距没有正确缩放

参阅 [HiDPI#VMware](<../zh-cn/HiDPI.html#VMware> "HiDPI")。 

###  Wayland 问题

####  GNOME 下键盘捕获无效

VMWare Player/Workstation 17.5（及更旧版本）中存在问题：[具体信息](<https://community.broadcom.com/vmware-cloud-foundation/communities/community-home/digestviewer/viewthread?GroupId=7171&MessageKey=b5468d18-1e9f-49f3-8964-95ce88d9d700&CommunityKey=fb707ac3-9412-4fad-b7af-018f5da56d9f>)

要允许用户界面捕获键盘： 
    
    $ gsettings set org.gnome.mutter.wayland xwayland-allow-grabs "true"
    $ gsettings set org.gnome.mutter.wayland xwayland-grab-access-rules "['vmplayer','vmware-vmx','mksSandbox']"
    
另外，也可以在 Windows 下使用以下快捷键： 

  * 使用 `Super+Alt+Tab` 取代 `Alt+Tab` 以切换任务
  * 使用 `Ctrl+Esc` 显示开始菜单

###  模块问题

####  找不到 /dev/vmmon

完整报错如下： 
    
    Could not open /dev/vmmon: No such file or directory.
    Please make sure that the kernel module 'vmmon' is loaded.
    
这表示至少 `vmmon` 模块没有被加载。可参考[#安装](<#%E5%AE%89%E8%A3%85>)一节[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")自动加载相关的服务。 

另一种可能是由 5.18 版本内核以及 11 代和更新 Intel 处理器的间接分支跟踪功能导致。 

在这种情况下，将 `ibt=off` 添加到你的[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中。具体信息请参考 [[2]](<https://communities.vmware.com/t5/VMware-Workstation-Player/kernel-6-3-4-may-break-vmware-player/td-p/2971432>)。 

####  找不到 /dev/vmci

完整报错如下： 
    
    Failed to open device "/dev/vmci": No such file or directory
    Please make sure that the kernel module 'vmci' is loaded.
    
首先尝试手动加载内核： 
    
    # modprobe -a vmw_vmci
    
也可以试试重新编译 VMware 内核模块： 
    
    # vmware-modconfig --console --install-all
    
###  无法启动 VMware

####  CPUIDEarly 模块上电失败

版本 14 比 12 有更严格的 CPU 需求。如果你尝试在不兼容的 CPU 上启动虚拟机，会出现如下报错： 
    
     This host does not support virtualizing real mode.
     The Intel "VMX Unrestricted Guest" feature is necessary to run this virtual machine on an Intel processor.
    
解决方法为卸载版本 14，并重新安装版本 12（[vmware-workstation12](<https://aur.archlinux.org/packages/vmware-workstation12/>)AUR）。 

如果 VMware 平时可用，但忽然出现该错误，那有可能是在暖/软启动或系统挂起后导致的。请尝试进行一次冷启动（关机并重新开机）。 

####  旧 Intel 微码导致的分段错误

旧 Intel 微码可能会在启动时导致如下分段报错： 
    
    /usr/bin/vmware: line 31: 4941 Segmentation fault "$BINDIR"/vmware-modconfig --appname="VMware Workstation" --icon="vmware-workstation"
    
微码更新方法请参考[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "微码")一文。 

####  vmplayer/vmware 版本 14 启动失败

在 `librsvg` 版本 2:2.44.0 及以上的系统中，`/tmp/vmware-<id>` 位置下的日志文件会显示数条如下报错： 
    
    appLoader| I125+ undefined symbol
    
一种临时处理方法为将 `librsvg` 降级到更早版本；更好的方法为强制 VMware 使用其自带的 `librsvg`： 
    
    # export LD_LIBRARY_PATH=/lib/vmware/lib/librsvg-2.so.2:$LD_LIBRARY_PATH
    
VMware 同时提供了一个 `VMWARE_USE_SHIPPED_LIBS` 变量： 
    
    $ env VMWARE_USE_SHIPPED_LIBS=1 vmware
    
####  从 12.5.4 版本开始无法启动 vmplayer/vmware

参考 [[3]](<https://bbs.archlinux.org/viewtopic.php?id=224667>)，临时解决方法为将 `libpng` 降级到 1.6.28-1 版本，并将其写入到 [/etc/pacman.conf](<../zh-cn/Pacman.html#%E5%9C%A8%E5%8D%87%E7%BA%A7%E6%97%B6%E8%B7%B3%E8%BF%87%E8%BD%AF%E4%BB%B6%E5%8C%85> "Pacman") 中的 `IgnorePkg` 参数： 

更简单的方法为让 VMware 使用系统提供的 zlib，而不是其自带的版本： 
    
    # cd /usr/lib/vmware/lib/libz.so.1
    # mv libz.so.1 libz.so.1.old
    # ln -s /usr/lib/libz.so.1 .
    
####  无法启动 12.5.3 至 12.5.5 版本的 vmplayer/vmware

似乎是 `/usr/lib/vmware/lib/libstdc++.so.6/libstdc++.so.6` 文件缺少 `CXXABI_1.3.8` 导致的问题。 

如果系统安装了 [gcc-libs](<https://archlinux.org/packages/?name=gcc-libs>)包，那就已有了该库文件。因此，可以尝试将其移除，然后 vmplayer 会转而使用 gcc-libs 提供的文件。以根用户权限执行： 
    
    # mv /usr/lib/vmware/lib/libstdc++.so.6/libstdc++.so.6 /usr/lib/vmware/lib/libstdc++.so.6/libstdc++.so.6.bak
    
另一种绕过方法为： 
    
    # export VMWARE_USE_SHIPPED_LIBS='yes'
    
####  启动 vmware 12 后进程闪退，未能加载图形界面

Registered bug at [Mageia](<https://bugs.mageia.org/show_bug.cgi?id=9739>), but it seems that there are no error messages shown in terminal with arch. When inspecting the logs, which are in `/tmp/vmware-<id>`, there are `VMWARE_SHIPPED_LIBS_LIST is not set`, `VMWARE_SYSTEM_LIBS_LIST is not set`, `VMWARE_USE_SHIPPED_LIBS is not set`, `VMWARE_USE_SYSTEM_LIBS is not set` issues. Process simply terminates with `Unable to execute /usr/lib/vmware/bin/vmware-modconfig.` after vmware or vmplayer is executed. Solution is the same, as root do: 
    
    # mv /etc/vmware/icu/icudt44l.dat /etc/vmware/icu/icudt44l.dat.bak
    
Also there is a workaround: 
    
    # export VMWARE_USE_SHIPPED_LIBS='yes'
    
Despite setting the VMWARE_USE_SHIPPED_LIBS variable, VMWare may still fail to find certain libraries. An example is the libfontconfig.so.1 library. Check vmware logs in the tmp directory to see which libraries are still not found. Copy them to the appropriate path with libraries existing on the system: 
    
    # cp /usr/lib/libfontconfig.so.1 /usr/lib/vmware/lib/libfontconfig.so.1/
    
Instead of copying all these files manually, you may want to try exporting an additional setting: 
    
    # export VMWARE_USE_SYSTEM_LIBS='yes'
    
On systems with fontconfig version **2.13.0** and above, it may be needed to force VMware to use the shipped libfontconfig file instead of the newer system file. In such case, it is also necessary to provide a shared object library file `libexpat.so.0` for the shipped fontconfig. This applies for at least VMware version **12.5.9**. As root do: 
    
    # ln -s /usr/lib/libexpat.so /usr/lib/vmware/lib/libfontconfig.so.1/libexpat.so.0
    # export LD_LIBRARY_PATH=/usr/lib/vmware/lib/libfontconfig.so.1:$LD_LIBRARY_PATH
    
###  虚拟机问题

####  无法为客户机下载 VMware Tools

可以通过访问 [VMware 存储库](<https://softwareupdate.vmware.com/cds/vmw-desktop/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2025-04-06 ⓘ]手动下载工具： 

访问 "_application name_ / _version_ / _build ID_ / linux / packages/" 路径并下载对应的工具。 

使用如下命令解压： 
    
    $ tar -xvf vmware-tools-_name_ -_version_ -_buildID_.x86_64.component.tar
    
然后使用 VMware 安装器进行安装： 
    
    # vmware-installer --install-component=_/path/_ vmware-tools-_name_ -_version_ -_buildID_.x86_64.component
    
如果以上方法无效，可以尝试安装 [ncurses5-compat-libs](<https://aur.archlinux.org/packages/ncurses5-compat-libs/>)AUR。 

####  虚拟机的系统时间错误或无法启动："[...]timeTracker_user.c:234 bugNr=148722"

[![](../File:Tango-edit-cut.png)](<../File:Tango-edit-cut.png>)**这一章节正在考虑移除。**

**原因:** `ondemand` is [no longer](<https://gitlab.archlinux.org/archlinux/packaging/packages/linux/-/commit/83345a2f829af62ce6fd4b4fa3a875b8f6560f43#dfba7aade0868074c2861c98e2a9a92f3178a51b_677_679>) the default governor, does this still apply to the `schedutil` governor? (在 [Talk:VMware](<../zh-cn/Talk:VMware.html>) 讨论)

This is due to [incomplete](<https://kb.vmware.com/selfservice/microsites/search.do?cmd=displayKC&externalId=1591>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-10-12 ⓘ] support of power management features ([Intel SpeedStep](<https://en.wikipedia.org/wiki/Intel_speedstep> "wikipedia:Intel speedstep") and [AMD PowerNow!](<https://en.wikipedia.org/wiki/AMD_powernow> "wikipedia:AMD powernow")/[Cool'n'Quiet](<https://en.wikipedia.org/wiki/Cool%27n%27Quiet> "wikipedia:Cool'n'Quiet")) in VMware Linux that vary the CPU frequency. In March 2012, with the release of [linux 3.3-1](<https://gitlab.archlinux.org/archlinux/packaging/packages/linux/-/commit/61a739ce77ef83a38f74f7d650b47e3e77ee258a>) the maximum frequency [Performance](</wzh/index.php?title=CPU_frequency_governors&action=edit&redlink=1> "CPU frequency governors（页面不存在）") governor was replaced with the dynamic _Ondemand_. When the host CPU frequency changes, the Guest system clock runs too quickly or too slowly, but may also render the whole Guest unbootable. 

To prevent this, the maximum host CPU frequency can be specified, and [Time Stamp Counter](<https://en.wikipedia.org/wiki/Time_Stamp_Counter> "wikipedia:Time Stamp Counter") (TSC) disabled, in the global configuration: 
    
    /etc/vmware/config
    
    host.cpukHz = "X"  # The maximum speed in KHz, e.g. 3GHz is "3000000".
    host.noTSC = "TRUE" # Keep the Guest system clock accurate even when
    ptsc.noTSC = "TRUE" # the time stamp counter (TSC) is slow.

**提示：** To periodically correct the time (once per minute), in the _Options_ tab of VMware Tools, enable: _"Time synchronization between the virtual machine and the host operating system"_.

####  系统重启后客户机丢失网络连接

该问题很可能由 `vmnet` 未被加载导致 [[4]](<https://www.linuxquestions.org/questions/slackware-14/could-not-connect-ethernet0-to-virtual-network-dev-vmnet8-796095/>)。可参考[#安装](<#%E5%AE%89%E8%A3%85>)一节[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")自动加载相关的服务。 

####  鼠标问题

#####  超出 5 个后的鼠标按键无法使用

如果你鼠标的拇指或其它额外按钮无法正常工作，可以[设置客户机使用高级鼠标](<../zh-cn/%E9%BC%A0%E6%A0%87%E6%8C%89%E9%94%AE.html#%E5%A6%82%E6%9E%9C_Arch_%E6%98%AF%E4%B8%80%E4%B8%AA%E8%99%9A%E6%8B%9F%E6%9C%BA%E5%AE%A2%E6%88%B7%E6%9C%BA> "鼠标按键")。 

#####  客户机上的鼠标滚轮表现怪异

This is related to the current Xorg keyboard layout on Host system. Keep primary layout (e.g., English) selected on Host while working on Guest. 

####  嵌套虚拟机没有 IP 地址及网络连接

该问题与混杂模式有关。根据标准 Linux 实践，该模式仅能由根用户启用。为了绕过该限制，需要修改对应网络设备的权限。 

对单个用户组给予权限： 
    
    # chgrp _group_ /dev/vmnetX
    
    # chmod g+rw /dev/vmnetX
    
对所有用户给予权限： 
    
    # chmod a+rw /dev/vmnetX
    