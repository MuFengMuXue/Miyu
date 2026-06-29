神舟的战神笔记本完美支持ArchLinux，在安装轻量级窗口管理器时，需要一些额外设置。 

##  触摸板

如果安装的是Gnome、KDE之外的轻量桌面管理器，需要额外安装[xf86-input-synaptics](<https://archlinux.org/packages/?name=xf86-input-synaptics>)包驱动触摸板。有些时候，触控板不能正确执行单击、双击及中键击，需要以下额外设置： 
    
    /etc/X11/xorg.conf.d/70-synaptics.conf
    
    Section "InputClass"
        Identifier "touchpad"
        Driver "synaptics"
        MatchIsTouchpad "on"
            Option "TapButton1" "1"
            Option "TapButton2" "3"
            Option "TapButton3" "2"
    EndSection
    
更多细节，请参考[Touchpad Synaptics](<../zh-cn/Touchpad_Synaptics.html> "Touchpad Synaptics")。 

##  屏幕背光

安装ArchLinux后，屏幕背光快捷键会失效。需要安装[xorg-xbacklight](<https://archlinux.org/packages/?name=xorg-xbacklight>)包来调整背光，请参考[Backlight#xbacklight](<../zh-cn/%E8%83%8C%E5%85%89.html#xbacklight> "Backlight")。 

##  显卡驱动设置

战神系列的笔记本都有两块显卡（一个Intel核显和一个NVIDIA的独显），需要安装[Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee")支持双显卡，平时会自动关闭NVIDIA独显，节能和降温，请参考[这里](<../zh-cn/Bumblebee.html> "Bumblebee")。NVIDIA显卡的驱动最好安装官方的[nvidia-dkms](<https://archlinux.org/packages/?name=nvidia-dkms>)包，以方便升级内核时显卡的自动配置，具体请参考[NVIDIA#Installation](<../zh-cn/NVIDIA.html#Installation> "NVIDIA")。 

很重要的是，如果出现鼠标滑轮浏览网页卡顿、切换NVIDIA玩游戏黑屏等现象，请需要把Intel核显的加速模式修改为uxa模式，请参考[Intel graphics#AccelMethod](<../zh-cn/Intel_graphics.html#AccelMethod> "Intel graphics")。 

##  声音

系统支持声音系统，但是根据[官方文档](<../zh-cn/Advanced_Linux_Sound_Architecture.html> "Advanced Linux Sound Architecture")调整后仍然无声音，这是因为系统同时有多个音频输出，需要在用户目录下建立配置文件，进行指定默认声卡。 先运行`aplay -l`命令，看看系统的声卡有哪些，然后找到本机模拟信号声卡的卡号和设备号，本例子中卡号是1，设备号是0。最后建立配置文件即可。 
    
    ~/.asoundrc
    
    defaults.pcm.card 1
    defaults.pcm.device 0
    defaults.ctl.card 1

之后，运行`alsamixer`命令调整音量。 

##  摄像头

系统默认支持摄像头，可以直接用 [MPlayer](<../zh-cn/%E7%BD%91%E7%BB%9C%E6%91%84%E5%83%8F%E6%9C%BA%E9%85%8D%E7%BD%AE.html#MPlayer> "网络摄像机配置") 或者 [FFmpeg](<../zh-cn/%E7%BD%91%E7%BB%9C%E6%91%84%E5%83%8F%E6%9C%BA%E9%85%8D%E7%BD%AE.html#FFmpeg> "网络摄像机配置") 进行测试。 

##  Wi-Fi 热点

根据[Software access point](<../zh-cn/Software_access_point.html> "Software access point")，网卡可以设置为Wi-Fi 热点。但是，WPA/WPA2在1～9[频道](<https://en.wikipedia.org/wiki/List_of_WLAN_channels#Interference_Concerns> "wikipedia:List of WLAN channels")不能正确工作，需要在配置文件里设置[频道](<https://en.wikipedia.org/wiki/List_of_WLAN_channels#Interference_Concerns> "wikipedia:List of WLAN channels")为10或更高： 
    
    /etc/hostapd/hostapd.conf
    
    channel=10 

##  其他建议

参阅 [Laptop](<../zh-cn/%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91.html> "Laptop")

  * 由于是Intel的CPU，所以最好安装[Microcode](<../zh-cn/%E5%BE%AE%E7%A0%81.html#Installation> "Microcode")。
  * 最好把系统BIOS设置为UEFI启动，并以此方式安装系统，提高启动速度，并且开机的默认的眼睛Logo也不显示了。
  * 平时最好把麦克风音量调整为0，用黑胶布粘贴住摄像头，并且把uvcvideo模块blacklist掉，就会感觉好一些。
