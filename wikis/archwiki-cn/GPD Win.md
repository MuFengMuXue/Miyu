**翻译状态：**

  * 本文（或部分内容）译自 [GPD_Win](<https://wiki.archlinux.org/title/GPD_Win> "arch:GPD Win")，最近一次同步于 2020-3-5，若英文版本有所[更改](<https://wiki.archlinux.org/title/GPD_Win?diff=0&oldid=599928>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GPD_Win_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[GPD Win](<http://softwincn.com/gpd_win_2>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ]是一款小巧的（5.5英寸屏幕）手持设备。 

##  修补

**没有在下面提及的功能应当是直接可用的。**

###  内置Wi-Fi

在[Linux Bug 185661](<https://bugzilla.kernel.org/show_bug.cgi?id=185661>)得到解决之前，需要进行修补才能使内置Wi-Fi工作。目前的解决办法是从[此处](<https://chromium.googlesource.com/chromiumos/third_party/linux-firmware/+/f151f016b4fe656399f199e28cabf8d658bcb52b/brcm/brcmfmac4356-pcie.txt>)获取 **brcmfmac4356-pcie.txt** （中国大陆地区访问可能需要代理工具），然后将其放在**/lib/firmware/brcm** ，再重新加载**brcmfmac** 模块。 

**注意：** 网页右下角的“txt”按钮不会下载正确的文件。你需要手动将内容复制粘贴至brcmfmac4356-pcie.txt。

在Arch Linux安装程序中让内置Wi-Fi工作，最简单的方法是：在Windows 10下将上述文件下载到C:\。然后在安装程序中进行以下操作： 

创建一个目录并挂载Windows 10分区（**将下面的mmcblk0p2换成你的Windows 10分区，可以通过运行lsblk找到** ） 
    
    mkdir windows
    mount /dev/mmcblk0p2 windows
    
复制文件 
    
    cp windows/brcmfmac4356-pcie.txt /lib/firmware/brcm
    
重新加载模块 
    
    modprobe -r brcmfmac
    modprobe brcmfmac
    
连接到Wi-Fi 
    
    wifi-menu
    
**注意：** 如果Wi-Fi看起来不能用，可能需要在BIOS中进行一项附加设置。重启并在设备启动同时按住Del键，在BIOS画面中进入芯片组（Chipset）选项卡，选择南桥（South Bridge），之后是LPSS & SCC配置（LPSS & SCC Configuration），将SCC SDIO支持（SCC SDIO Support）切换到PCI模式（PCI Mode）。保存BIOS更改，回到复制文件步骤再试一次。

###  电池监控

从内核4.12开始直接可用。更早版本的内核需要[Hans de Goede的带补丁内核](<https://hansdegoede.livejournal.com/17445.html>)，他的内核也会修复开机后插电源线不充电以及只能以500mA慢速充电的问题。 

###  旋转X会话

由于该设备使用了一块手机屏幕，显示画面需要旋转才能正常。从内核4.9.2开始，旋转X会话（通过[xrandr](<../zh-cn/Xrandr.html> "Xrandr")手动设置或在桌面环境的设置中操作）直接可用。（注：不同批次设备之间可能存在差异，原作者的GPD Win运行4.9.11-1内核未能解决屏幕旋转问题） 

如果使用GNOME时发现所有显示内容被过度放大，运行以下命令恢复缩放： 
    
    $ gsettings set org.gnome.desktop.interface scaling-factor 1
    
###  旋转触摸屏

从内核4.9.2开始，旋转X会话就会自动使触摸屏旋转（迄今为止，只测试过gnome-control-center）。 

**注意：** Gnome会应用正确的触摸屏方向，即使在使用arandr等第三方应用程序改变显示方向时也是如此。而截至2018-02-16，XFCE并不会自动旋转触摸坐标系。

如果你的系统没有自动旋转触摸屏，运行以下命令可能会有用，但结果似乎因人而异。 
    
    xinput set-prop 'Goodix Capacitive TouchScreen' 'Coordinate Transformation Matrix' -1 0 1 0 -1 1 0 0 1
    
###  修复在使用全核时的偶发崩溃问题

该CPU的睿频是由软件控制的，而Linux核心（4.4）无法将CPU频率降到足够低的程度。CPU会一直运行在2.4Ghz或接近的频率，即使全部4个核心活跃也是如此，最终会导致CPU崩溃。禁用睿频功能（BIOS中的“Turbo Mode”）可修复此问题。更多信息见[此处](<https://www.reddit.com/r/gpdwin/comments/5o2m1v/solved_linux_44_crashing_when_using_all_4_cores/>)。 

###  声音

在使用最新内核以及[linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包内核的情况下直接可用。耳机插孔可用，但目前需要[Hans de Goede的带补丁内核](<https://hansdegoede.livejournal.com/17445.html>)。 

###  存储卡读卡器

在使用最新内核以及[linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包内核的情况下直接可用。 

###  实体电源与音量键

可用，但目前需要[Hans de Goede的带补丁内核](<https://hansdegoede.livejournal.com/17445.html>)。 

###  调整屏幕亮度

从内核4.14开始直接可用。更早版本的内核需要[Hans de Goede的带补丁内核](<https://hansdegoede.livejournal.com/17445.html>)。 

###  挂起、恢复以及开盖时唤醒

从内核4.14开始直接可用。更早版本的内核需要[Hans de Goede的带补丁内核](<https://hansdegoede.livejournal.com/17445.html>)。 

##  安装指南

###  启动安装器

重启时按住**Del** 或**Esc** 键以进入BIOS。在BIOS画面中，修改启动顺序将U盘设为优先，或者选择单次从U盘启动。 

在Arch Linux引导选项画面，高亮选中第一项，按**e** 键编辑引导选项并添加**“fbcon=rotate:1”** 使画面能够转到正确的方向。 

###  格式化并挂载分区，以与Windows 10共存

使用Windows中的“磁盘管理”或类似工具缩小Windows 10分区，并使用空闲空间为Arch Linux建立一个新分区。 

运行lsblk来列出分区，注意以下分区的编号： 

  * （**X** ） Windows引导加载器，一个100MB的分区
  * （**Y** ） Windows 10分区
  * （**Z** ） 新的Linux分区

格式化并挂载新的Linux分区 
    
    mkfs.ext4 /dev/mmcblk0p**Z**
    mount /dev/mmcblk0p**Z** /mnt
    
创建boot目录并挂载Windows引导加载器分区 
    
    mkdir /mnt/boot
    mount /dev/mmcblk0p**X** /mnt/boot
    
###  安装Arch Linux

安装基本系统 
    
    pacstrap -i /mnt base base-devel
    
将Wi-Fi补丁复制到新安装的系统 
    
    cp /lib/firmware/brcm/brcmfmac4356-pcie.txt /mnt/lib/firmware/brcm
    
接下来按照[通常安装指南](<../zh-cn/Installation_guide.html#%E9%85%8D%E7%BD%AE%E7%B3%BB%E7%BB%9F> "Installation guide")进行，到安装引导程序时再按照以下说明操作。 

###  安装引导程序

安装引导程序 
    
    bootctl install
    
创建并填写**/boot/loader/entries/arch.conf**

**注意：** 如果使用[linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包内核，请将**/vmlinuz-linux** 改成**/vmlinuz-linux-lts** ，**/initramfs-linux.img** 改成**/initramfs-linux-lts.img**
    
    title   Arch Linux
    linux   /vmlinuz-linux
    initrd  /initramfs-linux.img
    options fbcon=rotate:1 root=/dev/mmcblk0p**Z** rw
    
**GPD Win上Arch Linux的安装到此完成。**
