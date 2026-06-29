**翻译状态：**

  * 本文（或部分内容）译自 [Intel GVT-g](<https://wiki.archlinux.org/title/Intel_GVT-g> "arch:Intel GVT-g")，最近一次同步于 2022-12-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/Intel_GVT-g?diff=0&oldid=749854>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Intel_GVT-g_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [PCI passthrough via OVMF](<../zh-cn/PCI_passthrough_via_OVMF.html> "PCI passthrough via OVMF")
  * [QEMU](<../zh-cn/QEMU.html> "QEMU")
  * [Intel graphics](<../zh-cn/Intel_graphics.html> "Intel graphics")

[Intel GVT-g](<https://github.com/intel/gvt-linux/wiki/GVTg_Setup_Guide>) 是一项为Intel GPU (Broadwell之后的架构)提供中介设备直通的技术，可以在不妨碍宿主机正常使用GPU的同时，将GPU虚拟化出多个性能接近原生硬件的虚GPU供多个虚拟机使用。这对于硬件加速虚拟机中的Windows图形是很有用的，对于没有独立显卡可用于[全设备直通](<../zh-cn/PCI_passthrough_via_OVMF.html> "PCI passthrough via OVMF")的笔记本来说尤其如此。(英伟达和AMD的GPU也有类似的功能，但只给Quadro、Radeon Pro这类“专业版”GPU提供。) 

Intel还有另一名字相似的技术叫做GVT-d，即使用vfio-pci驱动进行全设备直通。若使用GVT-d，宿主机不能在虚拟化后使用GPU。 

##  准备步骤

Intel GVT-g在Intel Broadwell (5代) 到 Comet Lake (10代)上是受支持的，但在Ice Lake (10代移动处理器)、Rocket Lake (11th台式机处理器)缺少i915驱动的支持。参见[Intel Support Post](<https://www.intel.com/content/www/us/en/support/articles/000058558/graphics.html>) 以及 [Github Issue](<https://github.com/intel/gvt-linux/issues/126>) 了解具体细节。 

有关Intel显卡对虚拟化支持可以参考官网<https://www.intel.cn/content/www/cn/zh/support/articles/000093216/graphics.html?wapkw=gvt-g>

目前Ice Lake只支持 GVT-d。 对于[Xe Architecture (Gen12)](<https://en.wikipedia.org/wiki/Intel_Graphics_Technology#Xe_LP_Architecture_.28Gen12.29> "wikipedia:Intel Graphics Technology")GPU，则需要SR-IOV特性。参考[QEMU/Guest graphics acceleration#SR-IOV](</wzh/index.php?title=QEMU/Guest_graphics_acceleration&action=edit&redlink=1> "QEMU/Guest graphics acceleration（页面不存在）")了解具体细节。 

首先，你需要创建一个虚GPU，然后将它分配给某个虚拟机。客户机（guest）会将虚GPU视为“正常”的GPU，因此直接安装原生驱动即可，不需要使用特殊驱动（但要保证驱动不过时）。 

步骤如下： 

  * 使用Linux 4.16（或更新） 和 [QEMU](<../zh-cn/QEMU.html> "QEMU") 2.12（或更新）
  * 将 `intel_iommu=on` 添加到 [kernel parameters](<../zh-cn/Kernel_parameters.html> "Kernel parameters")以启用IOMMU
  * [启用](<../zh-cn/Kernel_module.html#Automatic_module_loading> "Kernel module")内核模块: `kvmgt`, `vfio-iommu-type1` 和 `mdev`
  * [设置](<../zh-cn/Kernel_module.html#Setting_module_options> "Kernel module") i915 模块启动参数 `enable_gvt=1` 以启用GPU虚拟化
  * 把 `i915.enable_guc=0` 添加到 [kernel parameters](<../zh-cn/Kernel_parameters.html> "Kernel parameters"), 参见 [Intel graphics#Enable GuC / HuC firmware loading](<../zh-cn/Intel_graphics.html#Enable_GuC_/_HuC_firmware_loading> "Intel graphics")的警告
  * 检索GPU的PCI地址和区域号（下文分别记为`$GVT_PCI` 和 `$GVT_DOM`， as it resides in `/sys/bus/pci/devices`。 可以用 `lspci -D -nn`检视含有`VGA compatible controller: Intel Corporation HD Graphics ...`的那一行，左边的地址即为`$GVT_PCI`，大概形同`0000:00:02.0`
  * 为虚GPU生成一个GUID（下文记为`$GVT_GUID`），之后将用于创建和分配虚GPU。虚GPU与GUID一一对应，如果要创建多个虚GPU，那么它们的GUID必须不同。可以使用`uuidgen`生成随机的GUID。

**警告：** 一些用户报告在 5.12 或更新版本的内核上，会导致宿主机和客户机崩溃，参见 <https://github.com/intel/gvt-linux/issues/188>

###  创建虚GPU

正确设置上文的内核参数和模块参数，重启后即可创建虚GPU。 

虚GPU的类型有多种，区别在于分配给他们的资源量。用以下命令查看可用类型（另外，在对应类型的目录下`cat description`可以查看此类型的细节）： 
    
    # ls /sys/devices/pci${GVT_DOM}/$GVT_PCI/mdev_supported_types
    
    i915-GVTg_V5_1  # Video memory: <512MB, 2048MB>, resolution: up to 1920x1200
    i915-GVTg_V5_2  # Video memory: <256MB, 1024MB>, resolution: up to 1920x1200
    i915-GVTg_V5_4  # Video memory: <128MB, 512MB>, resolution: up to 1920x1200
    i915-GVTg_V5_8  # Video memory: <64MB, 384MB>, resolution: up to 1024x768
    
**注意：** If the directory is presented but contains nothing, you may try to increase the AGP aperture size in your computer firmware.

选择一个类型（下文记为`$GVT_TYPE`），用下面的命令创建指定类型的虚GPU： 
    
    # echo "$GVT_GUID" > "/sys/devices/pci${GVT_DOM}/$GVT_PCI/mdev_supported_types/$GVT_TYPE/create"
    
要创建多个虚GPU，则修改GUID，重复上面的指令多次。创建好的虚GPU将出现在 `/sys/bus/pci/devices/$GVT_PCI/`中。 

要删除已经创建的虚GPU，执行下面的指令 
    
    # echo 1 > /sys/bus/pci/devices/$GVT_PCI/$GVT_GUID/remove
    
###  libvirt qemu 钩子

[libvirt qemu 钩子](<https://www.libvirt.org/hooks.html>)可在对应虚拟机启动的时自动创建虚GPU、关闭时自动删除虚GPU。按照实际情况替换下面变量的值（`DOMAIN name`是对应虚拟机的domain）。 
    
    /etc/libvirt/hooks/qemu
    
    #!/bin/sh
    GVT_PCI=<GVT_PCI>
    GVT_GUID=<GVT_GUID>
    MDEV_TYPE=<GVT_TYPE>
    DOMAIN=<DOMAIN name>
    if [ $# -ge 3 ]; then
        if [ "$1" = "$DOMAIN" ] && [ "$2" = "prepare" ] && [ "$3" = "begin" ]; then
            echo "$GVT_GUID" > "/sys/bus/pci/devices/$GVT_PCI/mdev_supported_types/$MDEV_TYPE/create"
        elif [ "$1" = "$DOMAIN" ] && [ "$2" = "release" ] && [ "$3" = "end" ]; then
            echo 1 > /sys/bus/pci/devices/$GVT_PCI/$GVT_GUID/remove
        fi
    fi

记得给予此文件[executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable")权限，变量的值记得使用引号，例如`GVT_PCI='0000:00:02.0'`. 

**注意：**

  * 如果使用libvirt用户会话, 此脚本需要使用[权限提升](<../zh-cn/General_recommendations.html#Security> "General recommendations")命令，如 [pkexec(1)](<https://man.archlinux.org/man/pkexec.1>)或者[sudo](<../zh-cn/Sudo.html> "Sudo").
  * domain的XML将通过标准输入传入此脚本。可以使用`xmllint`和XPath表达式从标准输入提取 `GVT_GUID`，如: 
        
        GVT_GUID="$(xmllint --xpath 'string(/domain/devices/hostdev[@type="mdev"][@display="on"]/source/address/@uuid)' -)"

###  使用systemd service

可以使用systemd service在启动时自动创建虚GPU。优点如下： 

  * 不依赖于 libvirt
  * 可不使用权限提升，因为你可以让systemd直接以root身份执行脚本
  * 虽然不是按需创建虚GPU，但虚GPU闲置的时候似乎不会影响宿主机的GPU性能

创建一个 [bash 脚本](<https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Shell-Scripts>)，内容即[#准备步骤](<#%E5%87%86%E5%A4%87%E6%AD%A5%E9%AA%A4>)中提到的步骤。给予其可执行权限。确保脚本有修改权限，因为它将在启动的时候被root用于运行。 接下来[创建](<../zh-cn/Systemd.html#Writing_unit_files> "Systemd") [systemd 服务](<https://man.archlinux.org/man/systemd.service.5#EXAMPLES>)，使之启动时执行此脚本，并设置下列属性： 
    
    After=graphical.target
    Type=oneshot
    User=root
    
##  分配虚GPU

如果以普通用户身份运行 `qemu` 或 `libvirtd` ，可能会报告 `/dev/vfio/_number_` 不可写，那么需要给予此用户写对应目录的权限（使用 `chmod` 或者 `setfacl` 修改权限） 

### QEMU CLI

要创建一个带有虚GPU的虚拟机，将此参数添加到QEMU命令中: 
    
    -device vfio-pci,sysfsdev=/sys/bus/mdev/devices/$GVT_GUID
    
**注意：** KVM 需要用 `-enable-kvm`启用

### libvirt

把这一设备添加对应虚拟机XML的 `_devices_` 元素中 
    
    $ virsh edit _vmname_
    
    ...
        <hostdev mode='subsystem' type='mdev' managed='no' model='vfio-pci' display='off'>
          <source>
            <address uuid=''GVT_GUID''/>
          </source>
        </hostdev>
    ...

把 `_GVT_GUID_` 替换成你虚GPU的UUID。 

##  获取虚GPU的显示内容

有几种不同的方式可以从虚GPU中获取显示内容。 

###  使用 DMA-BUF 显示

**警告：** 根据这一 [issue](<https://github.com/intel/gvt-linux/issues/20>), 此方法不适用于使用(未修改的)OVMF的UEFI虚拟机。使用基于BIOS的虚拟机(比如SeaBISO) 或者参考下文的补丁或者处理方法。

#### QEMU CLI

把 `display=on,x-igd-opregion=on` 添加到 `-device vfio-pci` 参数的后面，如: 
    
    -device vfio-pci,sysfsdev=/sys/bus/mdev/devices/$GVT_GUID,display=on,x-igd-opregion=on
    
#### libvirt

首先，修改虚拟机的XML，以便于之后使用QEMU相关的元素。修改： 
    
    $ virsh edit _vmname_
    
    <domain type='kvm'>
    
至 
    
    $ virsh edit _vmname_
    
    <domain xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0' type='kvm'>
    
然后把本配置文件添加到`<domain>`元素的的末尾，比如，把这段文本插入到`</domain>`标签的上面： 
    
    $ virsh edit _vmname_
    
    ...
      <qemu:override>
        <qemu:device alias="hostdev0">
          <qemu:frontend>
            ...
            <qemu:property name="x-igd-opregion" type="bool" value="true"/>
          </qemu:frontend>
        </qemu:device>
      </qemu:override>
    ...
    
###  使用带UEFI/OVMF的DMA-BUF

如上文所说，DMA-BUF显示不能与使用（未修改过的）OVMF的UEFI客户机一同工作，原因在于它不会通过QEMU的非标准fw_cfg接口暴露出所需的ACPI OpRegion。参见[this OVMF bug](<https://bugzilla.tianocore.org/show_bug.cgi?id=935>)。 

根据 [GitHub上的讨论](<https://github.com/intel/gvt-linux/issues/23#issuecomment-468125999>)，OVMF bug报告提出了几种解决方案。可以 

  * 为OVMF[打补丁](<https://bugzilla.tianocore.org/attachment.cgi?id=165>) ([细节见此](<https://bugzilla.tianocore.org/show_bug.cgi?id=935#c4>)) 以添加针对Intel的特殊行为 (最直接，但和上游不一致);
  * 为宿主机的内核[打补丁](<https://bugzilla.tianocore.org/attachment.cgi?id=168>) ([细节见此](<https://bugzilla.tianocore.org/show_bug.cgi?id=935#c12>)) 以自动为虚GPU提供一个可选的ROM;
  * 从内核补丁中[提取OpROM](<http://120.25.59.132:3000/vbios_gvt_uefi.rom>)([来源](<https://www.reddit.com/r/VFIO/comments/av736o/creating_a_clover_bios_nonuefi_install_for_qemu/ehdz6mf/>)) 供QEMU重载。不需要打补丁。

在此选择最后一种方法。 

**注意：** if the link _and_ [the archive](<https://web.archive.org/web/20201020144354/http://120.25.59.132:3000/vbios_gvt_uefi.rom>) go down, the OpROM can be extracted from the kernel patch by hand. 

下载 `vbios_gvt_uefi.rom` 并将其置与某处。(本例中为`/`)。 

#### libvirt

然后编辑虚拟机的XML定义，把下面这段配置添加到先前创建的`qemu:commandline`元素中。 
    
    $ virsh edit _vmname_
    
    ...
        <qemu:arg value='-set'/>
        <qemu:arg value='device.hostdev0.romfile=**/vbios_gvt_uefi.rom** '/>
    ...
    
###  启用RAMFB显示 (可选)

本操作是上文的DMA-BUF配置的补充，用于显示虚拟机Intel驱动载入前的显示画面（如POST，固件界面，客户机初始化） 

#### QEMU CLI

把`ramfb=on,driver=vfio-pci-nohotplug`添加到`-device vfio-pci`参数的末尾，如： 
    
    -device vfio-pci,sysfsdev=/sys/bus/mdev/devices/$GVT_GUID,display=on,x-igd-opregion=on,ramfb=on,driver=vfio-pci-nohotplug
    
#### libvirt

首先，参照[这一小节](<#libvirt_2>)修改虚拟机的XML定义。 

然后把下面的配置添加到`<domain>`元素中，即插入到`</domain>`标签前面： 
    
    $ virsh edit _vmname_
    
    ...
      <qemu:override>
        <qemu:device alias="hostdev0">
          <qemu:frontend>
            ...
            <qemu:property name="driver" type="string" value="vfio-pci-nohotplug"/>
            <qemu:property name="ramfb" type="bool" value="true"/>
          </qemu:frontend>
        </qemu:device>
      </qemu:override>
    ...
    
##  显示虚GPU输出

由于spice-gtk相关的[问题](<https://gitlab.freedesktop.org/spice/spice-gtk/issues/100>)，不同EGL实现的SPICE客户端的配置方法不同。 

###  使用QEMU GTK显示器输出

在性能较弱的CPU上，本方法的刷新率较高、显示延迟较小，至少对于Windows虚拟机来说是如此。并且相比于Looking Glass，本方法的CPU负载较小。代价是得放弃一些SPICE GPU特性，如: 

  * 共享剪贴板
  * 自动 USB 重定向 (需要在启动虚拟机前手动分配USB)
  * 鼠标指针自由进出虚拟机
  * 与virt-manager的显示器输入整合 (会在另一个窗口里显示)

只有在虚拟机加载了正确的Intel GPU驱动后才会开始输入显示内容（通常是登录界面）。这意味着： 

  * 最好预先安装好正确的Intel GPU驱动。安装前，可以暂时使用另一种虚拟显示器适配器与Intel vGPU一起工作(如 [-vga std](<../zh-cn/QEMU.html#std> "QEMU") 或者 [-std-vga（针对libvirt](<https://wiki.libvirt.org/page/QEMUSwitchToLibvirt#-std-vga>))，安装后移除std视频适配器.
  * 无法看到系统的启动过程。如果系统在登录前崩溃，只能暂用另一种虚拟显示器适配器以排查错误。
  * 要进入BIOS，得[启用RAMFB显示](<#Enable_RAMFB_display_\(optional\)>).

**提示：** 在QEMU GTK中, `Ctrl+Alt+G` 可以捕获或释放鼠标指针，`Ctrl+Alt+F`可以在全屏模式和窗口模式间切换。

#### QEMU CLI

把`-display gtk,gl=on`添加到命令后面。QEMU VGA适配器可以通过添加`-vga none`禁用。或者也可以同时用两个虚拟显示屏，只不过连接到QEMU VGA适配器的那个是空白的。 

#### libvirt

  * 确保上面添加的`<hostdev>`设备把`display`属性设为`'off'`。
  * 确保已经把`xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0'`添加到`domain`(步骤[使用DMA-BUF显示器](<#libvirt_2>))。
  * 移除所有`<graphics>`和`<video>`设备。

QEMU GTK显示窗口需要你指定运行OpenGL的显示输出。如果使用笔记本电脑，则先把所有外接显示器断开，确保笔记本电脑屏幕是唯一的显示器。使用这行的命令获取显示器编号`echo $DISPLAY`，形如`:0`。获取编号后即可重连外接显示器。把刚才获取的编号插入到下面`env name='DISPLAY'`的这行中。 

  * 添加下面的QEMU命令行参数

    $ virsh edit _vmname_
    
    ...
      <qemu:commandline>
        <qemu:arg value="-display"/>
        <qemu:arg value="gtk,gl=on,zoom-to-fit=off"/>
        <qemu:env name="DISPLAY" value=":0"/>
      </qemu:commandline>
      <qemu:override>
        <qemu:device alias="hostdev0">
          <qemu:frontend>
            <qemu:property name="display" type="string" value="on"/>
            ...
          </qemu:frontend>
        </qemu:device>
      </qemu:override>
    ...

####  缩放

窗口模式中，`-display gtk,gl=on,zoom-to-fit=off`使GTK显示窗口大小和虚拟机的屏幕的分辨率一致，保证像素纵横比是1:1。不启用这个参数（或缺省）会使虚拟机的显示匹配窗口的大小，不能保持像素纵横比为1:1,这种缩放不太好看。 

在全屏模式中，缩放自动启用。在修改客户机的分辨率的时，只有降低分辨率会更新缩放，如果虚拟机的分辨率调得比宿主机要高，则需手动退出重进全屏模式。 

####  GTK显示产生的CPU负载

`gl=es`可能可以降低CPU负载，但2021年11月过后。`gl=on`似乎更有优势。 

###  使用MESA EGL实现的SPICE输出

#### QEMU CLI

把`-display spice-app,gl=on`添加到命令行。须安装`virt-viewer`。 

#### libvirt

  * 确保上面添加的`<hostdev>`设备的`display`属性设为`'on'`。
  * 移除所有的{ic|<graphics>}}和`<video>`设备。
  * 添加下面的设备：

    $ virsh edit _vmname_
    
    ...
        <graphics type='spice'>
          <listen type='none'/>
          <gl enable='yes'/>
        </graphics>
        <video>
          <model type='none'/>
        </video>
    ...
    
`gl`标签中的可选属性`rendernode`可以用于指定渲染器，如： 
    
    <gl enable='yes' rendernode='/dev/dri/by-path/pci-0000:00:02.0-render'/>
    
###  使用NVIDIA EGL实现的SPICE或VNC输出

#### libvirt

  1. 确保上面添加的<hostdev> 设备的`display`属性设为`'on'`。
  2. 移除所有`<graphics>` and `<video>`设备。
  3. 添加下面的设备：

    $ virsh edit _vmname_
    
    ...
        <graphics type='spice' autoport='yes'>
          <listen type='address'/>
        </graphics>
        <graphics type='egl-headless'/>
        <video>
          <model type='none'/>
        </video>
    ...
    
要使用VNC，则须将`<graphics type='spice'>`的`type`属性改为`'vnc'`。 

`<graphics type='egl-headless'>`标签中的`<gl>`可选属性可以用来指定渲染器（由于前面提到的bug，不要把这一可选属性添加到`spice`图形中）。例如： 
    
    <graphics type='egl-headless'>
      <gl rendernode='/dev/dri/by-path/pci-0000:00:02.0-render'/>
    </graphics>
    
###  禁用所有输出

如果禁用了所有输出，那么只能使用RDP、VNC、Looking Glass等软件获取显示内容。参见[PCI passthrough via OVMF#Using Looking Glass to stream guest screen to the host](<../zh-cn/PCI_passthrough_via_OVMF.html#Using_Looking_Glass_to_stream_guest_screen_to_the_host> "PCI passthrough via OVMF")。 

#### QEMU CLI

在`-device vfio-pci`参数中，将`ramfb=on`改为`display=off`。添加`-vga none`以禁用QEMU VGA适配器。 

#### libvirt

要确保没有加载任何模拟的GPU，可以编辑虚拟机的配置： 

  1. 移除所有`<graphics>`设备。
  2. 把`<video>`设备的类型都改为`'none'`。
  3. 确保上面添加的`<hostdev>`设备的`display`属性设为`'off'`。

##  故障排查

###  mdev_supported_types目录缺失

如果你按步骤操作，在添加`i915.enable_gvt=1`内核参数后仍然找不到`/sys/bus/pci/devices/0000:02:00.0/mdev_supported_types`目录，请再次检查`kvmgt`模块是否已载入。 

然后检查你的硬件是否支持，检视[dmesg](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "Dmesg")的输出里是否有这条信息： 
    
    # dmesg | grep -i gvt 
    
    [    4.227468] [drm] Unsupported device. GVT-g is disabled

如果都没有问题，检查上游是否有支持计划。如，对于"Coffee Lake" (CFL)平台的支持可以参见https://github.com/intel/gvt-linux/issues/53 

###  Windows提示内存损坏错误（bad memory error）

如果Windows虚拟机由于内存损坏错误卡死，检视宿主机 _dmesg_ 的输出以获取更多细节。如果内核日志中有类似超出内存限制（rlimit memory exceeded）的内容，则可能需要增加Linux分配给QEMU的内存限制。若用户在`kvm`组中，把下面的内容添加到`/etc/security/limits.d/42-intel-gvtg.conf`然后重启。 
    
    # qemu kvm, need high memlock to allocate memory for vga-passthrough
    @kvm - memlock 8388608
    
###  同时使用Intel GVT-G和PRIME render offload

在宿主机上同时使用Intel GVT-G和NVIDIA的[PRIME render offload](<../zh-cn/PRIME.html#PRIME_render_offload> "PRIME")会导致客户机出现一些[问题](<https://github.com/intel/gvt-linux/issues/162>)。建议使用[bbswitch](<../zh-cn/Bumblebee.html#%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86> "Bbswitch")关闭独立显卡或者与[Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee")、[nvidia-xrun](<../zh-cn/Nvidia-xrun.html> "Nvidia-xrun")或者[optimus-manager](<../zh-cn/NVIDIA_Optimus.html#Using_optimus-manager> "NVIDIA Optimus")一同使用。 

###  无显示器

如果虚拟机使用RAMFB显示器并且没有输出任何显示内容，尝试增加以下选项到`<qemu:commandline>`标签： 
    
    $ virsh edit _vmname_
    
    ...
      <qemu:commandline>
        <qemu:arg value="-set"/>
        <qemu:arg value="device.hostdev0.display=on"/>
      </qemu:commandline>
    ...

###  花屏

如果鼠标移入后虚拟机屏幕花屏，下面的[方法](<https://github.com/intel/gvt-linux/issues/152#issuecomment-637790127>)可能有效 

首先，按照[#libvirt 2](<#libvirt_2>)修改虚拟机的XML定义。 

然后，把下面的内容插入到`</domain>`标签的上面。如果`<qemu:commandline>`标签已经存在，就直接插入到其中去： 
    
    $ virsh edit _vmname_
    
    ...
      <qemu:commandline>
        <qemu:env name="MESA_LOADER_DRIVER_OVERRIDE" value="i965"/>
      </qemu:commandline>
    ...

###  宿主机在挂起时卡死

创建GVT-g虚GPU后，宿主机可能在挂起时卡死。参见[github](<https://github.com/intel/gvt-linux/issues/156>)以追踪此bug。 

一个可行的解决方法是，在挂起前将GVT-g虚GPU移除，唤醒后才重新创建。你可以安装[gvtg_vgpu-git](<https://aur.archlinux.org/packages/gvtg_vgpu-git/>)AUR自动化这个过程。 

###  修改虚GPU的显示分辨率

虚GPU默认使用其支持的最大分辨率。无论虚拟机设置了多大的分辨率，所显示的内容都会被缩放到虚GPU的分辨率，造成显示效果不佳。 

要真正改变显示分辨率，将下面的内容添加到XML的`<qemu:commandline>`元素中： 
    
    $ virsh edit _vmname_
    
    ...
        <qemu:arg value='-set'/>
        <qemu:arg value='device.hostdev0.xres=1440'/>
        <qemu:arg value='-set'/>
        <qemu:arg value='device.hostdev0.yres=900'/>
    ...

##  参见

  * [Official GVT-g Setup Guide](<https://github.com/intel/gvt-linux/wiki/GVTg_Setup_Guide>)
  * [Official GVT-g DMA-BUF User Guide](<https://github.com/intel/gvt-linux/wiki/Dma_Buf_User_Guide>).
  * [Running Windows via QEMU/KVM and Intel GVT-g](<https://www.reddit.com/r/VFIO/comments/8h352p/guide_running_windows_via_qemukvm_and_intel_gvtg/>)
  * [Blog post about using GVT](<https://blog.bepbep.co/posts/gvt/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-18 ⓘ]
