[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Wifi Radar](<../zh-cn/Talk:Wifi_Radar.html>)讨论)

##  介绍

[Wifi雷达（Wifi Radar）](<http://wifi-radar.systemimager.org/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2020-08-06 ⓘ]是一个小巧的GUI程序，你可以用它很容易的切换无线网络连接。 

##  安装

要安装Wifi雷达，只需执行： 
    
    # pacman -S wifi-radar
    
##  配置
    
    # visudo
    
增加下面一行： 
    
    你的用户名     ALL=(ALL) NOPASSWD: /usr/sbin/wifi-radar
    
按 ESC, 接着冒号 (:), 然后按 x, 然后按 ENTER 保存并退出。 

增加 _wifi-radar_ 到 /etc/rc.conf 中的DAEMONS组。 

从你的程序菜单运行wifi-radar。如果你想查看可用的网络连接，执行 _sudo wifi-radar_ 。 

##  小技巧

  1. 你可能需要编辑 /etc/conf.d/wifi-radar，设置适合你的特殊网络接口。

  1. 有的用户可能要设置‘Ifup required’为开启，以便wifi-radar能正常工作。

##  附加资料

[Wireless network configuration](<../zh-cn/Wireless_network_configuration.html> "Wireless network configuration") \- 无线网络安装wiki。 
