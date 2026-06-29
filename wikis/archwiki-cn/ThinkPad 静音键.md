[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:ThinkPad 静音键](<../zh-cn/Talk:ThinkPad_%E9%9D%99%E9%9F%B3%E9%94%AE.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [ThinkPad mute button](<https://wiki.archlinux.org/title/ThinkPad_mute_button> "arch:ThinkPad mute button")，最近一次同步于 2021-03-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/ThinkPad_mute_button?diff=0&oldid=657483>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/ThinkPad_mute_button_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** No standard sections. Maybe move page so it can be a /Troubleshooting one?（在[Talk:ThinkPad 静音键](<../zh-cn/Talk:ThinkPad_%E9%9D%99%E9%9F%B3%E9%94%AE.html>)讨论）

##  问题

当使用较新的内核时，绝大多数ThinkPad和IdeaPad上的静音键无法正常工作。具体表现为： 

###  静音键完全不工作

静音键没有任何反应：键盘上的LED指示灯不亮（部分ThinkPad的静音键上有一个指示静音状态的LED灯），同时扬声器的音量也没有任何变化。在这种情况下，只有按了静音键之后再按音量键小键，才能真正静音。 

###  外接音频设备不静音

按下静音键后，内置扬声器被静音了（静音键上的LED指示灯状态也正确改变），但是外接音频设备依然未被静音。 

##  解决方案

###  旧型号的IBM ThinkPad

尝试这个页面提供的解决方案："<https://www.thinkwiki.org/wiki/Mute_button>" 

###  静音键完全不工作

编辑`/etc/modprobe.d/modprobe.conf`，添加以下内容： 
    
    /etc/modprobe.d/modprobe.conf
    
    ...
    options thinkpad_acpi enabled=0 # enables Mute-Button on ThinkPads with IdeaPad-Firmware

保存后重启，检查静音键是否正确工作。 

###  外接音频设备不静音

从[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")安装[tpb](<https://aur.archlinux.org/packages/tpb/>)AUR，并创建文件`/root/.tpbrc`： 
    
    /root/.tpbrc
    
    #tpb-Settings:
    CALLBACK "/root/tp-key-handler"
    OSD off
    
然后创建文件`/root/tp-key-handler`： 
    
    /root/tp-key-handler
    
    #!/bin/bash
    echo $1 $2
    if [ $1 = mute ]; then
    	if [ $2 = on ]; then
    		mset="off";
    	else
    		mset="on";
    	fi
    	sudo -u USERNAME amixer sset Master $mset; # I had to sudo to me, because I use PulseAudio
    fi

创建后还需要给`/root/tp-key-handler`增加可执行权限： 
    
    chmod +x /root/tp-key-handler 
    
由于tpb和[X](<../zh-cn/Xorg.html> "X")一样需要root权限，启动tpb需要在`.xinitrc`添加`sudo tpb`，并且需要编辑[sudo](<../zh-cn/Sudo.html> "Sudo")设置（使用`visudo`），或者在任何的X启动脚本中增加`gksudo tpb`（这个方法会在系统启动时要求输入密码）。 

###  外接音频设备不静音（Xfce环境）

前往“应用程序-设置-键盘-应用程序快捷键”选项卡。点击“添加”，在“命令”处输入`amixer sset Master toggle`，在“按键”处按下静音键。温馨提示：为了确保静音键上的LED指示灯的状态和系统静音状态保持一致，在设定快捷键前请将静音键上的LED指示灯与系统静音状态保持相反（译者注：即静音键LED指示灯亮起的同时系统处于未静音状态，或静音键LED指示灯熄灭的同时系统处于静音状态）。如此，在设定快捷键后，静音键上的LED指示灯与系统静音状态才能保持一致。如果恰好弄反了，重启电脑，在进入[Xfce](<../zh-cn/Xfce.html> "Xfce")会话前将静音键上的LED指示灯熄灭即可。 
