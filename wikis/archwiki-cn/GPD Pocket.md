**翻译状态：**

  * 本文（或部分内容）译自 [GPD_Pocket](<https://wiki.archlinux.org/title/GPD_Pocket> "arch:GPD Pocket")，最近一次同步于 2020-3-5，若英文版本有所[更改](<https://wiki.archlinux.org/title/GPD_Pocket?diff=0&oldid=599835>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GPD_Pocket_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文是关于[GPD Pocket](<http://softwincn.com/gpdpocket2>)的说明。 

##  参数

  * 显示屏: 7英寸IPS 1920x1200
  * CPU: Intel Atom X7-Z8750
  * RAM: 8GB LPDDR3-1600
  * 存储: 128GB eMMC SSD（不可更换）
  * 电池: 7000mAh
  * WiFi: Broadcom 4356 802.11ac
  * 蓝牙: Broadcom 2045
  * 音频: Realtek ALC5645
  * 接口: 1 x USB 3 type A, 1 x MicroHDMI, 1 x USB 3 type C, 1 x 3.5mm 耳机插孔

##  安装

###  自动

可以从[这里](<https://github.com/sigboe/GPD-ArchISO/releases>)下载预先打好补丁的ISO映像。 

###  手动

由于WiFi在默认配置下无法工作，需要首先解决WiFi问题(见[#WiFi](<#WiFi>))，或使用受支持的USB外置以太网/WiFi网卡。 

##  配置

###  自动

安装期间请将以下内容加入/etc/pacman.conf： 
    
    /etc/pacman.conf
    
    ...
    [gpd-pocket-arch]
    SigLevel = Never
    Server = https://github.com/joshskidmore/gpd-pocket-arch/raw/master
    ...
    
运行以下命令，安装GPD Pocket正常运行Arch所需要的更改： 

`# pacman -Syu gpd-pocket-support`

由于alsa-lib的补丁是可选依赖，必须手动安装它才能让音频工作： 

`# pacman -S gpd-pocket-alsa-lib`

###  手动

#### WiFi

安装软件包[gpd-pocket-support-bcm4356-git](<https://aur.archlinux.org/packages/gpd-pocket-support-bcm4356-git/>)AUR并重新加载WiFi内核模块: 
    
    # modprobe -r brcmfmac
    # modprobe brcmfmac
    
####  背光与KMS

修改`/etc/mkinitcpio.conf`如下，以通过KMS早启动来启用背光控制： 
    
    /etc/mkinitcpio.conf
    
    ...
    MODULES=(pwm_lpss pwm_lpss_platform i915)
    ...

#### Wayland

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Wayland和Xorg节都提到旋转触摸屏，但似乎Wayland节只提到了旋转触控输入，Xorg节只提到了旋转图形界面显示，故需要进一步核实，看是否两项操作都需要进行，不论图形后端为何。（在 [Talk:GPD Pocket](<../zh-cn/Talk:GPD_Pocket.html>) 中讨论）

#####  基本配置

创建`/etc/udev/rules.d/99-goodix-touch.rules`文件，并在其中填入如下内容以旋转触摸屏： 
    
    ACTION=="add|change", KERNEL=="event[0-9]*", ATTRS{name}=="Goodix Capacitive TouchScreen", ENV{LIBINPUT_CALIBRATION_MATRIX}="0 1 0 -1 0 1"
    
#####  右键模拟滚动

与Xorg中可以通过标准Xorg配置文件启用右键模拟滚动不同，在Wayland中此类配置应当是由混成器提供的；但不幸的是，一些混成器（如GNOME Wayland）并没有正确地提供这些配置接口。不过相应的功能仍然可以通过`libinput`实现。由于这些混成器通常加载`/etc/profile.d`，可以使用`LD_PRELOAD`挂钩至`libinput`从而强制应用这些配置。 

该方法的示例实现见[此处](<https://github.com/PeterCxy/scroll-emulation>)。 

#### Xorg

#####  基本配置

创建`/etc/X11/xorg.conf.d/30-monitor.conf`以旋转触摸屏： 

**注意：** 标识符（Identifier）可能因你所选择的显示驱动而不同（`DSI-1` (modesetting)或`DSI1` (xf86-video-intel))
    
    /etc/X11/xorg.conf.d/30-monitor.conf
    
    Section "Monitor"
      Identifier "DSI-1"
      Option     "Rotate" "right"
    EndSection
    
#####  Gnome与GDM

编辑`~/.config/monitors.xml`（默认状态下可能不存在该文件）： 
    
    ~/.config/monitors.xml
    
    <monitors version="2">
      <configuration>
        <logicalmonitor>
          <x>0</x>
          <y>0</y>
          <scale>2</scale>
          <primary>yes</primary>
          <transform>
            <rotation>right</rotation>
            <flipped>no</flipped>
          </transform>
          <monitor>
            <monitorspec>
              <connector>DSI-1</connector>
              <vendor>unknown</vendor>
              <product>unknown</product>
              <serial>unknown</serial>
            </monitorspec>
            <mode>
              <width>1200</width>
              <height>1920</height>
              <rate>60.384620666503906</rate>
            </mode>
          </monitor>
        </logicalmonitor>
      </configuration>
    </monitors>

这样即可设置正确的旋转方向（`<rotation>right</rotation>`）以及缩放因子2（`<scale>2</scale>`）。关于非整数倍缩放，见[HiDPI#GNOME](<../zh-cn/HiDPI.html#GNOME> "HiDPI")。 

对于[GDM](<../zh-cn/GDM.html> "GDM")，将以上的`~/.config/monitors.xml`文件复制到`/var/lib/gdm/.config/monitors.xml`以设置正确的旋转方向。 

##### KDE

在 _系统设置_ > _显示和监控_ 中，将 _方向_ 改为 _90°顺时针_ ，并调整 _缩放显示_ 至合适尺寸。 

#####  右键模拟滚动

创建`/etc/X11/xorg.conf.d/50-trackpoint.conf`从而实现按住右键来滚动屏幕： 
    
    /etc/X11/xorg.conf.d/50-trackpoint.conf
    
    Section "InputClass"
      Identifier      "GPD trackpoint"
      MatchProduct    "SINO WEALTH Gaming Keyboard"
      MatchIsPointer  "on"
      Driver          "libinput"
      Option          "MiddleEmulation" "1"
      Option          "ScrollButton" "3"
      Option          "ScrollMethod" "button"
    EndSection
    
##### SDDM

为了改变DPI使文字可读，将以下行加入`/usr/share/sddm/scripts/Xsetup`： 
    
    /usr/share/sddm/scripts/Xsetup
    
    # Set DPI  
    xrandr --dpi 168"  
    
#####  触摸屏手势

安装[touchegg](<https://aur.archlinux.org/packages/touchegg/>)AUR，然后编辑`/usr/share/touchegg/touchegg.conf`中的下列行： 
    
    /usr/share/touchegg/touchegg.conf
    
    ...
    <action type="SCROLL">SPEED=7:INVERTED=true</action>
    ...

创建`/etc/X11/xinit/xinitrc.d/01_touchegg`： 
    
    /etc/X11/xinit/xinitrc.d/01_touchegg
    
    ...
    #!/bin/bash
    
    # starts touchegg application
    PREFIX="$HOME/.config/touchegg/.run"
    mkdir -p "$PREFIX"
    PIDFILE="$PREFIX/touchegg.$USER$DISPLAY.pid"
    LOCK="$PREFIX/touchegg.$USER$DISPLAY.lock"
    
    start_touchegg() {
            (
                    flock -n 9 || exit 1
                    touchegg 2>/dev/null >/dev/null &
                    PID=$!
                    echo "$!" >"$PIDFILE"
                    wait $PID
            ) 9>"$LOCK"
    }
    
    start_touchegg &
    
对`/etc/X11/xinit/xinitrc.d/01_touchegg`设置权限： 
    
    # chmod 0755 /etc/X11/xinit/xinitrc.d/01_touchegg
    
#####  利用Pocket 2上的“半/全”键

出厂状态下`半/全`被设定为发送```符号及按键码49，导致其与原本的``/~`键形成重复。为了把它映射到更有用的功能，请前往[GPD2 Firmware](<https://www.gpd.hk/gpdp2firmware>)然后下载"GPD Pocket 2 Keyboard Firmware (Japan)"（中国大陆地区下载可能需使用代理工具）。此固件必须在Windows 10操作系统（设备原装的）下刷入。由于更新期间键盘和鼠标无法使用，建议使用USB鼠标。 

更新完成后`半/全`会发送按键码49及```符号，而``/~`键会发送按键码132。创建`~/.Xmodmap`文件以进行修正： 
    
    ~/.Xmodmap
    
    keycode  132 = grave asciitilde
    keycode  49  = XF86Launch1 NoSymbol

现在进行测试： 
    
    $ xmodmap ~/.Xmodmap
    
更多信息请参阅[Xmodmap](<../zh-cn/Xmodmap.html> "Xmodmap")

####  风扇

使用最新内核时风扇应当直接可以工作。 

**注意：** 如果你的风扇有问题，未能按期望的方式运转，请尝试以下方法：
    
    # modprobe -r gpd-pocket-fan
    # modprobe gpd-pocket-fan temp_limits=40000,40001,40002
    
当以上操作完成之后——应当能够在40℃时听到风扇起转，如果听到了咔哒声——关闭设备电源，卸下后盖，之后用手轻轻转几圈风扇。然后重新装上后盖并开机，登录之后再次运行上面的命令。部分设备似乎存在问题，风扇一段时间没有通电之后无法正确地启动。 

一旦完成了以上步骤并且风扇工作正常，应当重启系统或重新加载风扇内核模块，从而将温度阈值恢复到默认： 
    
    # modprobe -r gpd-pocket-fan
    # modprobe gpd-pocket-fan
    
**注意：** 默认状态下，连接交流电源时风扇会一直转动[[1]](<https://github.com/stockmind/gpd-pocket-ubuntu-respin#gpd-fan-always-spinning-on-ac>)。要更改这一行为，请在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中添加`gpd-pocket-fan.speed_on_ac=0`。

####  节能

安装[tlp](<https://archlinux.org/packages/?name=tlp>)包，然后编辑`/etc/default/tlp`中的下列行： 
    
    /etc/default/tlp
    
    ...
    # improve disk IO
    DISK_DEVICES="mmcblk0"
    DISK_IOSCHED="deadline"
    ...
    # disable wifi power saving mode (wifi speed drops MASSIVELY!)
    WIFI_PWR_ON_AC=off
    WIFI_PWR_ON_BAT=off
    ...

#### PulseAudio

将下列行加入`/etc/pulse/default.pa`： 
    
    /etc/pulse/default.pa
    
    set-card-profile alsa_card.platform-cht-bsw-rt5645 HiFi
    set-default-sink alsa_output.platform-cht-bsw-rt5645.HiFi__hw_chtrt5645_0__sink
    set-sink-port alsa_output.platform-cht-bsw-rt5645.HiFi__hw_chtrt5645_0__sink [Out] Speaker
    
编辑`/etc/pulse/daemon.conf`以关闭实时调度： 
    
    /etc/pulse/daemon.conf
    
    realtime-scheduling = no

####  充电控制

可以控制充电电流、充电终止电压及一些其他设定。 

更多信息及示例脚本见[这篇reddit帖子](<https://reddit.com/r/GPDPocket/comments/cfyekh/limit_battery_charge/eudbwto>)（中国大陆地区访问可能需使用代理工具）。 

##  已知问题

###  USB-C电源状态

USB-C电源状态在内核版本4.14-15下不工作。Hans的内核有修复此问题的补丁。 

### systemd-gpt-auto-generator failed to dissect

由于[此原因](<https://github.com/systemd/systemd/issues/5806>)，启动时会出现报错信息： 

`systemd-gpt-auto-generator[199]: Failed to dissect: Input/output error`. 

向启动引导器添加以下启动参数，可避免该信息出现。 
    
    systemd.gpt_auto=0
    
##  参见

  * <https://github.com/njkli/gpd-pocket/>
  * <https://hansdegoede.livejournal.com/>
