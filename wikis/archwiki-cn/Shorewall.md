[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Shorewall](<../zh-cn/Talk:Shorewall.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Shorewall](<https://wiki.archlinux.org/title/Shorewall> "arch:Shorewall")，最近一次同步于 2016-07-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/Shorewall?diff=0&oldid=442339>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Shorewall_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:Shorewall#](<../zh-cn/Talk:Shorewall.html>) 中讨论）

[The Shoreline Firewall](<http://www.shorewall.net/>), more commonly known as "Shorewall", is high-level tool for configuring Netfilter. 

You describe your firewall/gateway requirements using entries in a set of configuration files. Shorewall reads those configuration files and with the help of the iptables utility, Shorewall configures Netfilter to match your requirements. 

Shorewall can be used on a dedicated firewall system, a multi-function gateway/router/server or on a standalone GNU/Linux system. Shorewall does not use Netfilter's ipchains compatibility mode and can thus take advantage of Netfilter's connection state tracking capabilities. 

##  安装

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [shorewall](<https://aur.archlinux.org/packages/shorewall/>)AUR or [shorewall6](<https://aur.archlinux.org/packages/shorewall6/>)AUR package. 

##  配置

These settings are based on the [two-interface documentation on the Shorewall web site](<http://www.shorewall.net/two-interface.htm>). 

Use some example configuration files that come with the shorewall package 
    
    # cp /usr/share/doc/shorewall/Samples/one-interface/* /etc/shorewall/     # If you have a desktop-type system with a single network interface
    # cp /usr/share/doc/shorewall6/Samples6/one-interface/* /etc/shorewall6/  # If you have a desktop-type system with a single network interface, pkg shorewall6
    # cp /usr/share/doc/shorewall/Samples/two-interfaces/* /etc/shorewall/    # If you have a router with two network interfaces
    # cp /usr/share/doc/shorewall/Samples/three-interfaces/* /etc/shorewall/  # If you have a router with three network interfaces
    
###  /etc/shorewall/interfaces

**Change** the interface settings to match the names used for our Ethernet devices and to allow DHCP traffic on the local network. Edit `/etc/shorewall/interfaces`

original 
    
    net     eth0          dhcp,tcpflags,nosmurfs,routefilter,logmartians
    loc     eth1          tcpflags,nosmurfs,routefilter,logmartians
    
new 
    
    net     wan          dhcp,tcpflags,nosmurfs,routefilter,logmartians
    loc     lan          dhcp,tcpflags,nosmurfs,routefilter,logmartians
    
###  /etc/shorewall/policy

**Change** the policy file to allow the router (this machine) to access the Internet. Edit `/etc/shorewall/policy`

original 
    
    ###############################################################################
    #SOURCE         DEST            POLICY          LOG LEVEL       LIMIT:BURST
    
    loc             net             ACCEPT
    net             all             DROP            info
    # THE FOLLOWING POLICY MUST BE LAST
    all             all             REJECT          info
    
new 
    
    ###############################################################################
    #SOURCE         DEST            POLICY          LOG LEVEL       LIMIT:BURST
    $FW             net             ACCEPT
    loc             net             ACCEPT
    net             all             DROP            info
    # THE FOLLOWING POLICY MUST BE LAST
    all             all             REJECT          info
    
###  /etc/shorewall/rules

DNS look-ups are handled (actually forwarded) by dnsmasq, so Shorewall needs to allow those connections. **Add** these lines to `/etc/shorewall/rules`
    
    #       Accept DNS connections from the local network to the firewall
    #
    DNS(ACCEPT)     loc              $FW
    
###  /etc/shorewall/masq

**Change** the network interface to the one connected to your external (WAN) network and **change** the IP to the one used in your local network. 
    
    eth0        192.168.1.0/24
    
#### SSH

**OPTIONAL:** You can **add** these lines to /etc/shorewall/rules if you want to be able to SSH into the router from computers on the Internet 
    
    #       Accept SSH connections from the internet for administration
    #
    SSH(ACCEPT)     net             $FW         TCP      <SSH port used>
    
####  Port forwarding (DNAT)

  * /etc/shorewall/rules : here is an example for a webserver on our LAN with IP 10.0.0.85. You can reach it on port 5000 of our "external" IP.

    DNAT        net        loc:10.0.0.85:80        tcp        5000
    
###  /etc/shorewall/stoppedrules

If you have a network name other than eth1 for the network interface in /etc/shorewall/interfaces, you need to update stoppedrules with the correct name. 

###  /etc/shorewall/shorewall.conf

When you are finished making above changes, enable shorewall by a **change** in its config file `/etc/shorewall/shorewall.conf`: 

original 
    
    STARTUP_ENABLED=No
    
new 
    
    STARTUP_ENABLED=Yes
    
See [shorewall(8)](<https://man.archlinux.org/man/shorewall.8>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-06-25] for more info. 

##  启动

[Start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start")/[enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `shorewall.service`. 

## Traffic shaping

Read [Shorewall's Traffic Shaping/Control](<http://www.shorewall.net/traffic_shaping.htm>) guide. 

Here is my config as an example: 

  * /etc/shorewall/tcdevices : here is where you define the interface you want to have shaped and its rates. I have got a ADSL connection with a 4MBit down/256KBit up profile.

    ppp0        4mbit        256kbit 
    
  * /etc/shorewall/tcclasses : here you define the minimum (rate) and maximum (ceil) throughput per class. You will assign each one to a type of traffic to shape.

    # interactive traffic (ssh)
    ppp0            1       full    full    0
    # online gaming
    ppp0            2       full/2  full    5
    # http
    ppp0            3       full/4  full    10
    # rest
    ppp0            4       full/6  full    15              default
    
  * /etc/shorewall/tcrules : this file contains the types of traffic and the class it belongs to.

    1       0.0.0.0/0       0.0.0.0/0       tcp     ssh
    2       0.0.0.0/0       0.0.0.0/0       udp     27000:28000
    3       0.0.0.0/0       0.0.0.0/0       tcp     http
    3       0.0.0.0/0       0.0.0.0/0       tcp     https
    
I have split it up my traffic in 4 groups: 

  1. interactive traffic or ssh: although it takes up almost no bandwidth, it is very annoying if it lags due to leechers on the LAN. This gets the highest priority.
  2. online gaming: needless to say you cannot play when your ping sucks. ;)
  3. webtraffic: can be a bit slower
  4. everything else: every sort of download, they are the cause of the lag anyway.
