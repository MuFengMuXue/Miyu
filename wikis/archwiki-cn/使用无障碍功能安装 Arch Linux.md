**翻译状态：**

  * 本文（或部分内容）译自 [Install Arch Linux with accessibility options](<https://wiki.archlinux.org/title/Install_Arch_Linux_with_accessibility_options> "arch:Install Arch Linux with accessibility options")，最近一次同步于 2021-02-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/Install_Arch_Linux_with_accessibility_options?diff=0&oldid=653039>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Install_Arch_Linux_with_accessibility_options_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Arch Linux的官方安装媒介提供了多种辅助功能（ [Accessibility](</wzh/index.php?title=Accessibility&action=edit&redlink=1> "Accessibility（页面不存在）") ）： 

  * 朗读功能由[espeakup](<https://archlinux.org/packages/?name=espeakup>)包提供
  * [盲文终端](<https://en.wikipedia.org/wiki/Refreshable_braille_display> "wikipedia:Refreshable braille display")支持由[brltty](<https://archlinux.org/packages/?name=brltty>)包提供

本文档用于说明如何使用上述辅助功能安装[Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux")。 

**注意：** 本页面仅说明与官方[Installation guide](<../zh-cn/Installation_guide.html> "Installation guide")不同的步骤。

##  安装前

###  启动安装环境

**注意：** 安装媒介的引导加载程序在启动默认菜单项前有15秒的等待时间。

当安装媒介启动后，按`下`，然后按`回车`以使用朗读功能。 

USB盲文显示设备会通过[udev](<../zh-cn/Udev.html> "Udev")被自动检测到。 

###  多个音频输出设备

如果电脑拥有多个音频输出设备，将会听到如下信息： _Please select your sound card for speech output_ （请选择朗读功能使用的音频输出设备）。 

在希望使用的音频输出设备听到“嘀”声时，按`回车`选择该音频输出设备。 

##  安装

###  安装必要的软件包

在新安装的系统使用朗读功能，需[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[espeakup](<https://archlinux.org/packages/?name=espeakup>)包和[alsa-utils](<https://archlinux.org/packages/?name=alsa-utils>)包。如果使用盲文显示设备，需要安装[brltty](<https://archlinux.org/packages/?name=brltty>)包。 

在使用[pacstrap(8)](<https://man.archlinux.org/man/pacstrap.8>)安装系统时，使用以下命令添加所需的软件包： 
    
    # pacstrap /mnt base linux linux-firmware espeakup alsa-utils
    
##  配置系统

###  音频输出设备

如果检测到 [#多个音频输出设备](<#%E5%A4%9A%E4%B8%AA%E9%9F%B3%E9%A2%91%E8%BE%93%E5%87%BA%E8%AE%BE%E5%A4%87>)，需要使用以下命令将安装媒介生成的`/etc/asound.conf`复制到新安装的系统： 
    
    # cp /etc/asound.conf /mnt/etc/
    
###  激活开机启动

为了在进入新安装的系统时使用朗读功能，需要将`espeakup.service`设置为开机自动启动（方法参照[systemd#使用单元](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")）。 

##  重新启动

在启动至新安装的系统后，朗读功能应该会自动开始工作。 
