**翻译状态：**

  * 本文（或部分内容）译自 [Linux firmware](<https://wiki.archlinux.org/title/Linux_firmware> "arch:Linux firmware")，最近一次同步于 2025-07-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/Linux_firmware?diff=0&oldid=840734>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Linux_firmware_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")
  * [微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "微码")
  * [fwupd](<../zh-cn/Fwupd.html> "Fwupd")

Linux 固件是和 Linux 内核一同发行的软件包，其包含某些硬件所需的部分或全部功能所需的固件的[二进制 blob](<https://en.wikipedia.org/wiki/Binary_blob> "wikipedia:Binary blob")。这些二进制 blob 不允许被包含于使用了 GPL 许可证的工程，但可以以其他许可证重新发行。 

通常需要固件的几种硬件包括： 

  * 现代 [GPU](<https://en.wikipedia.org/wiki/Graphics_processing_unit> "wikipedia:Graphics processing unit")
  * [有线](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE/%E4%BB%A5%E5%A4%AA%E7%BD%91.html> "网络配置/以太网")网络适配器
  * [无线](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE/%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置/无线网络配置")网络适配器
  * [蓝牙](<../zh-cn/%E8%93%9D%E7%89%99.html> "蓝牙")控制器
  * 声卡（[专业音频](<../zh-cn/%E4%B8%93%E4%B8%9A%E9%9F%B3%E9%A2%91.html> "专业音频")或板载音频）

##  安装

对于多数用户，推荐[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [linux-firmware](<https://archlinux.org/packages/?name=linux-firmware>)包 元包以获取所有常用固件。 

###  单独安装不同供应商的固件

您可以仅安装您系统所使用的部分硬件的固件以节省存储空间。 

**警告：** 缺少必需固件可能导致系统无法操作！

作为 [linux-firmware](<https://archlinux.org/packages/?name=linux-firmware>)包 的依赖与其一同安装的固件： 

  * [linux-firmware-amdgpu](<https://archlinux.org/packages/?name=linux-firmware-amdgpu>)包 \- [AMD](<../zh-cn/AMDGPU.html> "AMDGPU") Radeon GPU
  * [linux-firmware-atheros](<https://archlinux.org/packages/?name=linux-firmware-atheros>)包 \- [高通 Atheros](<https://en.wikipedia.org/wiki/Atheros> "wikipedia:Atheros") Wi-Fi 及蓝牙适配器
  * [linux-firmware-broadcom](<https://archlinux.org/packages/?name=linux-firmware-broadcom>)包 \- [博通](<../zh-cn/%E5%8D%9A%E9%80%9A%E6%97%A0%E7%BA%BF%E7%BD%91%E5%8D%A1.html> "博通无线网卡")和 [Cypress](<https://en.wikipedia.org/wiki/Cypress_Semiconductor> "wikipedia:Cypress Semiconductor") 网络适配器
  * [linux-firmware-cirrus](<https://archlinux.org/packages/?name=linux-firmware-cirrus>)包 \- [Cirrus Logic](<https://en.wikipedia.org/wiki/Cirrus_Logic> "wikipedia:Cirrus Logic") 音频设备
  * [linux-firmware-intel](<https://archlinux.org/packages/?name=linux-firmware-intel>)包 \- [英特尔](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html> "Intel 图形处理器")音频设备，蓝牙适配器，GPU，网络适配器，NPU，网络摄像头和一些其他设备
  * [linux-firmware-mediatek](<https://archlinux.org/packages/?name=linux-firmware-mediatek>)包 \- [MediaTek](<https://en.wikipedia.org/wiki/MediaTek> "wikipedia:MediaTek") 和 [Ralink](<https://en.wikipedia.org/wiki/Ralink> "wikipedia:Ralink") 网络适配器
  * [linux-firmware-nvidia](<https://archlinux.org/packages/?name=linux-firmware-nvidia>)包 \- [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") GPU 和 SoC
  * [linux-firmware-other](<https://archlinux.org/packages/?name=linux-firmware-other>)包 \- 其他未分类的设备
  * [linux-firmware-radeon](<https://archlinux.org/packages/?name=linux-firmware-radeon>)包 \- [ATI](<../zh-cn/ATI.html> "ATI") Radeon GPU
  * [linux-firmware-realtek](<https://archlinux.org/packages/?name=linux-firmware-realtek>)包 \- [Realtek](<https://en.wikipedia.org/wiki/Realtek> "wikipedia:Realtek") 网络及蓝牙适配器

可选软件包： 

  * [linux-firmware-liquidio](<https://archlinux.org/packages/?name=linux-firmware-liquidio>)包 \- [Cavium](<https://en.wikipedia.org/wiki/Cavium> "wikipedia:Cavium") LiquidIO server adapters
  * [linux-firmware-marvell](<https://archlinux.org/packages/?name=linux-firmware-marvell>)包 \- [Marvell](<https://en.wikipedia.org/wiki/Marvell_Technology> "wikipedia:Marvell Technology") 网络适配器
  * [linux-firmware-mellanox](<https://archlinux.org/packages/?name=linux-firmware-mellanox>)包 \- for [Mellanox](<https://en.wikipedia.org/wiki/Mellanox_Technologies> "wikipedia:Mellanox Technologies") Spectrum switches.
  * [linux-firmware-nfp](<https://archlinux.org/packages/?name=linux-firmware-nfp>)包 \- for [Netronome](<https://en.wikipedia.org/wiki/Netronome> "wikipedia:Netronome") Flow Processors.
  * [linux-firmware-qcom](<https://archlinux.org/packages/?name=linux-firmware-qcom>)包 \- for [Qualcomm](<https://en.wikipedia.org/wiki/Qualcomm> "wikipedia:Qualcomm") SoCs.
  * [linux-firmware-qlogic](<https://archlinux.org/packages/?name=linux-firmware-qlogic>)包 \- for [QLogic](<https://en.wikipedia.org/wiki/QLogic> "wikipedia:QLogic") networked devices.

Third-party packages: 

  * [alsa-firmware](<https://archlinux.org/packages/?name=alsa-firmware>)包 \- for loader programs in alsa-tools and hotplug firmware loader. See [ALSA#Firmware](<../zh-cn/ALSA.html#Firmware> "ALSA").
  * [sane-gt68xx-firmware](<https://archlinux.org/packages/?name=sane-gt68xx-firmware>)包 \- for [gt68xx](<http://www.meier-geinitz.de/sane/gt68xx-backend/>)-based scanners.
  * [sigrok-firmware-fx2lafw](<https://archlinux.org/packages/?name=sigrok-firmware-fx2lafw>)包 \- for [FX2 logic analyzers](<https://sigrok.org/wiki/Fx2lafw>).
  * [sof-firmware](<https://archlinux.org/packages/?name=sof-firmware>)包 \- [Sound Open Firmware](<https://www.sofproject.org/>). See [ALSA#Firmware](<../zh-cn/ALSA.html#Firmware> "ALSA").

##  提示和技巧

###  探测已加载的固件

在调试或选择固件包时，您可能想知晓您的系统加载了哪些固件，请使用[动态调试（dynamic debug）](<https://docs.kernel.org/admin-guide/dynamic-debug-howto.html>)： 

  * 添加 `dyndbg="func fw_log_firmware_info +p"` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。请注意引号可能需要转义，具体取决于您使用的[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")。
  * 执行以下命令以列出已加载的固件：

    # journalctl -kg 'loaded f'

##  另请参阅

  * [上游仓库](<https://gitlab.com/kernel-firmware/linux-firmware>)
  * [Gentoo:Linux firmware](<https://wiki.gentoo.org/wiki/Linux_firmware> "gentoo:Linux firmware")
