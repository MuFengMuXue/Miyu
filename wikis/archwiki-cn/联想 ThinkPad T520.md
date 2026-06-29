**翻译状态：**

  * 本文（或部分内容）译自 [Lenovo ThinkPad T520](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_T520> "arch:Lenovo ThinkPad T520")，最近一次同步于 2020-04-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_T520?diff=0&oldid=605278>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_T520_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

##  安装

安装工作无需进行进一步的设置调整。 

##  显卡

BIOS选项 Display->Graphics Device 可以切换到以下设置： 

###  集成显卡

使用 xf86-video-intel 驱动程序。nvidia 卡将被关闭，这意味着系统将消耗更少的电量，并且您不必担心安装 nvidia 驱动程序。 

集成的图形足够快，可以运行某些较旧的游戏。 如果您不使用要求苛刻的3D应用程序，则这是一个不错的选择。 

此模式的主要缺点是 DisplayPort 无法工作，因为它已硬连线至 Nvidia 卡。 

###  离散显卡

这将为您在所有应用程序中提供良好的一致3D性能，而不必担心大黄蜂的复杂性。如果您想要一种简单的方法来连接和使用DisplayPort监视器，这也是一个不错的选择。 

您无法从 intel-gfx 上运行并关闭分立的 nvidia 卡来省电。另一个缺点是您不能使用此模式在 VGA 和 DP 上运行带有2个外接显示器的三重云台。这是硬件限制，离散的 nvidia 卡和集成的 Intel 卡都只能驱动最多2个不同的屏幕。 

### NVidia Optimus

如果选择此选项，请将 "OS Detection for NVIDIA Optimus" BIOS选项设置为 Disabled. 

有关如何在Linux上同时使用两张卡的详细信息，请参见[Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee")页面。 

##  使用 dock

见 [dockd](</wzh/index.php?title=Dockd&action=edit&redlink=1> "Dockd（页面不存在）"). 

##  故障排除

###  使用离散显卡时，屏幕会在登录提示之前冻结

如果您使用 GRUB2 启动，则其帧缓冲区图形模式会在以后的启动过程中引起问题。请参阅 [GRUB/Tips and tricks#Disable framebuffer](<../zh-cn/GRUB/Tips_and_tricks.html#Disable_framebuffer> "GRUB/Tips and tricks")。 

您也可以尝试设置 nomodeset 内核命令行标志：: 

[Kernel mode setting#Disabling modesetting](<../zh-cn/Kernel_mode_setting.html#Disabling_modesetting> "Kernel mode setting")

尽管当前（2013年10月，内核3.11.6），仅当我禁用 GRUB2 帧缓冲区但不设置任何 nomodeset 内核选项时，我的T520才以“离散显卡”模式启动。 
