宏碁 C720 Chromebook 使用 [SeaBIOS](<https://www.coreboot.org/SeaBIOS>) 作为 BIOS，因而可以方便的引导其他 Linux 发行版，也就很容易在该笔记本上安装 Arch Linux 或者其他发行版。 

##  安装

首先，我们要在 Chrome OS 的开发者模式下启用 legacy boot/SeaBISO 模式。然后就可以像平常在 x86 机器上安装 Arch 那样进行安装了。 

###  启用开发者模式

**警告：****这会清除您硬盘中的所有数据！**

要进入开发者模式，需要： 

  * 按住 `Esc+F3 (Refresh)`，然后按 `Power`，接着就会进入恢复模式。
  * 接着，按 `Ctrl+D`，它会提示您确认进入开发者模式，您的数据会被清除。
  * 再次按 `Ctrl+D`，或者等待 30 秒左右，系统会引导您进入开发者模式。

进入开发者模式之后，您需要获得 root 权限，切换到 root 的方法取决于您是否已经开机配置过您的 Chrome OS。 

####  还没有配置过您的 Chrome OS 的情况下

如果您从未开机配置过您的 Chrome OS，请按 `Ctrl+Alt+F2(→)`， 

  * 以 `chronos` 用户登录，无需密码
  * 输入 `sudo bash` 切换到 root

####  已经配置过您的 Chrome OS 的情况下

这时候，您只需要： 

  * 按 `Ctrl+Alt+T` 打开一个 crosh 终端窗口
  * 输入命令 `shell` 打开 shell
  * 输入 `sudo bash` 切换到 root

###  启用 Legacy Bios

切换到 root 之后， 

  * 输入以下命令

    # crossystem dev_boot_usb=1 dev_boot_legacy=1
    
启用 legacy boot 

  * 重启机器

现在，我们每次开机要按 `Ctrl-L` 进入 SeaBIOS。当然，如果您想要默认启动 SeaBIOS，但是鉴于危险性太高，不建议您这么做。如果您一定要省去按 `Ctrl-L` 的时间的话，请参考本文的英文版。 

###  安装 Arch Linux

您需要创建一个 [USB Installation Media](<../zh-cn/USB_Installation_Media.html> "USB Installation Media")，然后把 USB 插入本子的 USB 口，开机并启动 SeaBIOS，按 `Esc` 进入 SeaBIOS 菜单，选择您的 USB，启动。接着您就可以看到 Arch 的安装菜单了 

几点安装提示： 

  * 使用内核版本 > 4.0 的 ISO，可以开箱即用。相关触摸板补丁已经合并。
  * 建议选择 [GRUB](<../zh-cn/GRUB.html> "GRUB") 作为您的引导程序，而非 Syslinux。
  * 安装完成之后，开机启动是要按 `Ctrl-L` 而非 `Ctrl-D`。

###  Xorg Video 驱动

您需要的是 `xf86-video-intel`。 
    
    $ sudo pacman -S xf86-video-intel
    
###  触摸板内核模块

从 kernel 4.0 开始，Chromebook 相关驱动补丁已经合并，无需手动编译内核。也无需修改配置文件，只需安装 [Libinput](<../zh-cn/Libinput.html> "Libinput") 即可。关于 libinput 的配置可以参考 [Libinput](<../zh-cn/Libinput.html> "Libinput") 页面。 

##  提高 WLAN 和 BT 效率

这个 chromebook 使用了高通的 AR9462 WLAN+BT 作为无线网卡，蓝牙和无线网络都可以使用 2.4GHz，会有冲突。而这个芯片也出了名的丢包率高，常常断线。因此，您需要创建并编辑配置文件： 
    
    /etc/modprobe.d/ath9k.conf
    
    options ath9k btcoex_enable=1 ps_enable=1 bt_ant_diversity=1

这里设置 ps_enable=1 虽然可以节约电量，但是有可能会导致死机，如果您不幸遇上了，可以设置为 ps_enable=0 即可。 

##  快捷键

Chromebook 将 F1 到 F10 绑定到了各种方便的快捷键，您也可以使用 [Sxhkd](<../zh-cn/Sxhkd.html> "Sxhkd")，[xbindkeys](</wzh/index.php?title=Xbindkeys&action=edit&redlink=1> "Xbindkeys（页面不存在）") 等工具来自定义您的快捷键。值得注意的是，搜索键，位置在 `Caps Lock` 那里，被识别为 `Meta` 键。如果您不是经常输入英文，应该无需在意。 

##  alsa 声音设置

想要您的 C720 与 [alsa](<../zh-cn/ALSA.html> "Alsa") 配合得相得益彰，您只需要编辑 `/etc/modprobe.d/alsa.conf` ，若文件不存在则新建一个，并加入 
    
    /etc/modprobe.d/alsa.conf
    
    options snd_hda_intel index=1

也可以创建一个 .asoundrc 文件， 
    
    ~/.asoundrc
    
    # Standard
    pcm.!default {
      type hw
      card 1
      device 0
    }
    
    ctl.!default {
      type hw
      card 1
    }
    
    pcm_slave.slavej {
      pcm "hw:1"
      channels 2
      rate 44100
    }
    
    pcm.plugj {
      type plug
      slave slavej
    }
    
    # HDMI
    #pcm.!default {
      #type hw
      #card 1
      #device 3
    #}
    
    #ctl.!default {
      #type hw
      #card 0
    #}
    
##  电源键设置

因为由于 Chromebook 的电源键就在键盘右上角，很容易误触。可以忽略按下电源键以及关闭屏幕时的关机或休眠，编辑`logind.conf`： 
    
    /etc/systemd/logind.conf
    
    HandlePowerKey=ignore
    HandleLidSwitch=ignore

然后重启 logind： 
    
    # systemctl restart systemd-logind
    