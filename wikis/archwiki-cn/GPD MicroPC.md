**翻译状态：**

  * 本文（或部分内容）译自 [GPD_MicroPC](<https://wiki.archlinux.org/title/GPD_MicroPC> "arch:GPD MicroPC")，最近一次同步于 2020-3-5，若英文版本有所[更改](<https://wiki.archlinux.org/title/GPD_MicroPC?diff=0&oldid=599840>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GPD_MicroPC_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文是关于[GPD MicroPC](<http://softwincn.com/gpd_micropc>)的说明。 

##  参数

  * 显示：6英寸 720x1280 （没错，侧过去了）
  * CPU：Intel Gemini Lake N4100 4x 1.10GHz
  * 内存：8GB LPDDR4-2133
  * 存储：128GB M2-2242 SATA固态硬盘（可更换）
  * 电池：6200mAh
  * WiFi：Intel Dual Band Wireless-AC 3165
  * LAN：Realtek RTL8168
  * 音频：Intel 8086:3198
  * 输入设备：QWERTY键盘、3个鼠标按键、触摸板、电源按钮、CPU风扇实体开关、复位键
  * 接口：3个USB 3 type A、1个HDMI、1个USB 3 type C、1个microSDXC读卡器、1个RJ45以太网口、1个DB9（RS232）串口、1个3.5mm耳机插孔

USB-C接口用于充电，支持PD 2.0但也兼容5V USB充电器 

##  安装

请确保安装映像Linux内核至少为5.1版本。 

##  配置

###  内核模块

为使启动时键盘能够工作，将电池（battery）加入到预加载的模块中： 
    
    /etc/mkinitcpio.conf
    
    ...
    MODULES=(battery)
    ...
    
###  启动时的屏幕旋转

为使启动时屏幕方向正确，将fbcon=rotate:1加入引导加载器配置： 
    
    /boot/loader/entries/arch.conf
    
    ...
    options root=/dev/mapper/crypt cryptdevice=UUID=000ccc23-4223-0ccc-4223-deadbeaf2342:btrfs rw fbcon=rotate:1
    ...
    
### wayland

屏幕位于DSI-1，被旋转了90°，所以需要进行配置： 
    
    ~/.config/sway/config
    
    ...
    # configure display
    # get the names of your outputs by: swaymsg -t get_outputs
    output DSI-1 resolution 720x1280 transform 90
    ...
    