相关文章

  * [Bridge with netctl](</wzh/index.php?title=Bridge_with_netctl&action=edit&redlink=1> "Bridge with netctl（页面不存在）")
  * [网络配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")
  * [Wireless network configuration](<../zh-cn/Wireless_network_configuration.html> "Wireless network configuration")

[netctl](<https://gitlab.archlinux.org/archlinux/netctl>) 是一个基于命令行与配置文件的网络管理器和一个Arch项目。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [netctl](<https://archlinux.org/packages/?name=netctl>)包 软件包. 

_netctl_ 用于自动连接的的 [#特殊 systemd 单元](<#%E7%89%B9%E6%AE%8A_systemd_%E5%8D%95%E5%85%83>)需要一些额外的依赖项目。有关更多信息，请参阅该部分。 

其他可选依赖如下表所示。 

功能  | 依赖   
---|---  
WPA |  [wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包  
DHCP |  [dhcpcd](<https://archlinux.org/packages/?name=dhcpcd>)包 or [dhclient](<https://archlinux.org/packages/?name=dhclient>)包  
_wifi-menu_ |  [dialog](<https://archlinux.org/packages/?name=dialog>)包  
PPPoE |  [ppp](<https://archlinux.org/packages/?name=ppp>)包  
  
**警告：** 不要启用并发、导致冲突的网络服务。在启用 _netctl_ 服务或配置文件前，先使用 `systemctl --type=service` 命令来确保没有其他网络服务正在运行。

##  配置

_netctl_ 通过配置文件来管理网络连接和设置自动/手动/按需启动等不同操作模式。 

_netctl_ 配置文件存放于 `/etc/netctl/` 文件夹中，而示例配置存放在 `/etc/netctl/examples/` 里。 

要使用示例配置文件，只需把它从 `/etc/netctl/examples/` 下复制到 `/etc/netctl/` 下，然后按照自己的需要进行配置。请参考下文中的 [#示例配置](<#%E7%A4%BA%E4%BE%8B%E9%85%8D%E7%BD%AE>)。创建配置文件所需的第一个参数是网络接口（`Interface`）， 详情请参考[网络配置#网络接口](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E6%8E%A5%E5%8F%A3> "网络配置")。 

**提示：**

  * 对于无线设置，您可以以 root 权限运行 `wifi-menu` as 命令来在 `/etc/netctl/` 下创建配置文件。您需要 [dialog](<https://archlinux.org/packages/?name=dialog>)包 软件包才能使用 _wifi-menu_ 命令
  * 在您的配置文件中使用 `SkipNoCarrier=yes` 指令，可以在无论网线是否连接的情况下都启用静态 IP 配置文件。

参考 [netctl.profile(5)](<https://man.archlinux.org/man/netctl.profile.5>) 来获得配置文件选项的完整列表。for a complete list of profile options. 

##  用法

参考 [netctl(1)](<https://man.archlinux.org/man/netctl.1>) 来获得 _netctl_ 指令的完整列表。 

###  启动配置文件

创建配置文件后，您就可以尝试建立连接了。以下命令中的 _profile_ 仅为配置文件名称，而非完整路径： 
    
    # netctl start _profile_
    
如果以上命令运行出错，请以 root 权限运行 `journalctl -xn` 或运行 `netctl status _profile_` 来获得更详细的错误说明。 

###  启用配置文件

您可以用以下命令来让配置文件随系统启动： 
    
    # netctl enable _profile_
    
这会创建一个随计算机一起启动的 systemd 服务。但对配置文件的修改不会自动反映到服务文件中，所以在您修改配置文件之后，请重新启用它： 
    
    # netctl reenable _profile_
    
启用配置文件后，它将在下次启动时启动。显然，只有插好网线或者设备位于要使用的无线接入点范围内才能成功。 

如果您需要频繁切换多个配置文件（例如，携带笔记本电脑旅行），请使用 [#特殊 systemd 单元](<#%E7%89%B9%E6%AE%8A_systemd_%E5%8D%95%E5%85%83>)，而不是启用配置文件。 

###  特殊 systemd 单元

_netctl_ 为自动切换有线和无线连接配置文件提供了一个特殊的 systemd 服务。有关特殊 systemd 单元的完整列表，请参见 [netctl.special(7)](<https://man.archlinux.org/man/netctl.special.7>)。 

####  有线网络

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html> "Help:阅读") [ifplugd](<https://archlinux.org/packages/?name=ifplugd>)包 软件包然后[启动或启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `netctl-ifplugd@_interface_.service` systemd 单元。DHCP 配置文件会在网线插入或拔出时自动启动/停止。 

  * `netctl-ifplugd@_interface_.service` 服务将首选使用 DHCP 的配置文件。
  * 要自动启动静态IP配置文件，需要在其中设置 `ExcludeAuto=no` 选项。
  * 要想调高静态 IP 配置文件的优先级，您可以设置 `Priority=2`，这高于 DHCP 配置文件的默认优先级 `Priority=1`。

####  无线网络

[启动或启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `netctl-auto@_interface_.service` systemd 单元。 _netctl_ 会在您从一个无线网络移动到另一个无线网络的时候自动切换配置文件（也就是无线漫游）。 

  * 配置文件必须设置 `Security=wpa-configsection` 或者 `Security=wpa` 才能使用 _netctl-auto。_ 不能用 _`Security=wpa-config`_
  * 如果你希望某些无线网络配置文件**不** 被 `netctl-auto@_interface_.service` 自动启动，您必须在配置里明确指定 `ExcludeAuto=yes` 选项。
  * 您可以在 _WPAConfigSection_ 里设置 `priority=` 属性(参考 `/etc/netctl/examples/wireless-wpa-configsection`) 当多个无线接入点可用时，该选项的值越大表示对应的配置文件优先级越高。

记得用您设备的实际接口名称来替换上面的 _interface 。_ 比如 `netctl-auto@wlp4s0.service`。有关详细信息，请参考 [netctl.profile(5)](<https://man.archlinux.org/man/netctl.profile.5>) 。 

**注意：** * 如果任何配置文件包含错误，例如一个空的或错误引用的 `Key=` 变量，该单元将无法加载并报错 `"Failed to read or parse configuration '/run/network/wpa_supplicant_wlan0.conf'`，即使该配置文件未被使用。 

  * 如果您曾经用 _netctl_ 来 [#启用配置文件](<#%E5%90%AF%E7%94%A8%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)，请运行 `netctl disable _profile_` 来防止该配置文件在系统启动时被启动两次。

可以通过 _netctl-auto_ 命令手动控制 _netctl-auto_ 管理的接口，而不必停止 `netctl-auto.service`服务。有关可用操作的完整列表，请参见 [netctl-auto(1)](<https://man.archlinux.org/man/netctl-auto.1>) 。 

##  技巧和窍门

###  示例配置

####  有线网络

对于使用 DHCP 的网络连接，您只需把 `/etc/netctl/examples/ethernet-dhcp` 复制到 `/etc/netctl` 下，然后配置其中的 `Interface` 项即可。 

例如： 
    
    /etc/netctl/_my_dhcp_profile_
    
    Interface=enp1s0
    Connection=ethernet
    IP=dhcp
    
要设置静态 IP，请把 `/etc/netctl/examples/ethernet-static` 复制到 `/etc/netctl` 下然后自行修改 `Interface`、 `Address` 、`Gateway` 和 `DNS` 选项。 

例如： 
    
    /etc/netctl/_my_static_profile_
    
    Interface=enp1s0
    Connection=ethernet
    IP=static
    Address=('10.1.10.2/24')
    Gateway='10.1.10.1'
    DNS=('10.1.10.1')
    
注意其中的子网大小 `/24`。这是用[无类别域间路由](<https://zh.wikipedia.org/wiki/%E6%97%A0%E7%B1%BB%E5%88%AB%E5%9F%9F%E9%97%B4%E8%B7%AF%E7%94%B1> "zhwp:无类别域间路由")（英语：Classless Inter-Domain Routing，简称CIDR）表示法表示的，相当于子网掩码 `255.255.255.0`。 

要在一个接口上设置多个 IP，可以这样设置 
    
    Address=('10.1.10.2/24' '192.168.1.2/24')
    
要添加多个 DNS 服务器地址： 
    
    DNS=('1.1.1.1' '1.0.0.1')
    
####  无线网络 (WPA-PSK)

以下内容适用于使用预共享密钥（WPA-PSK）的标准无线连接。 
    
    /etc/netctl/wireless-wpa
    
    Description='A simple WPA encrypted wireless connection using 256-bit PSK'
    Interface=wlp2s2
    Connection=wireless
    Security=wpa
    IP=dhcp
    ESSID=_your_essid_
    Key=\"64cf3ced850ecef39197bb7b7b301fc39437a6aa6c6a599d0534b16af578e04a

**注意：**

  * 确保对 `Key` 变量使用 **特殊引用规则** ，如 [netctl.profile(5) § SPECIAL QUOTING RULES](<https://man.archlinux.org/man/netctl.profile.5#SPECIAL_QUOTING_RULES>) 中所述。
  * 如果密码短语失败，请尝试删除 `Key` 变量中的 `\"`。
  * 虽然是 Key 看起来是加密的，但是仅凭您在配置文件配置中输入的密钥就已经足以连接到 WPA-PSK 网络。因此，这只能隐藏明文的密码短语，而不会阻止对该文件具有读访问权限的任何人连接到网络。

###  混淆无线密码

您还可以按照以下步骤来混淆无线密码短语 (_wifi-menu_ 在使用 `-o` 标志时自动执行此操作 ) : 

**不** 希望将其无线网络的密码以**明文** 形式存储的用户可以选择存储相应的 256 位预共享密钥，该密钥使用标准算法从密码和 SSID 计算得出。 

使用 [wpa_passphrase](<../zh-cn/Wpa_supplicant.html#Connecting_with_wpa_passphrase> "Wpa supplicant") 命令来计算 256 位 PSK： 
    
    $ wpa_passphrase _your_essid_
    
    network={
      ssid="_your_essid_ "
      #psk="_passphrase_ "
      psk=64cf3ced850ecef39197bb7b7b301fc39437a6aa6c6a599d0534b16af578e04a
    }

然后用 _预共享密钥_ (PSK) 来替换 `Key` 变量中的明文密码短语。 The _pre-shared key_ (psk) now needs to replace the plain text passphrase of the `Key` variable in the profile. 

###  使用实验性 GUI

如果您想要一个图形用户界面来管理 _netctl_ 和您的连接，并且您不担心使用高度实验性的非官方软件包，那么有一些选项可用。[netctl-gui](<https://aur.archlinux.org/packages/netctl-gui/>)AUR 提供了一个基于 Qt 的图形界面、DBus 守护程序和 KDE 小部件。[netmenu](<https://aur.archlinux.org/packages/netmenu/>)AUR 使用 [dmenu](<https://archlinux.org/packages/?name=dmenu>)包 作为其图形界面，[gnome-shell-extension-netctl-auto-gnome-git](<https://aur.archlinux.org/packages/gnome-shell-extension-netctl-auto-gnome-git/>)AUR 是 gnomeshell 扩展。 

还有一个应用程序能显示托盘图标，和在配置文件更改时显示桌面通知 : [netctl-tray](<https://aur.archlinux.org/packages/netctl-tray/>)AUR。 

###  链路聚合

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 由于 [ifenslave 已被移出内核](<https://github.com/torvalds/linux/commit/b1098bbe1b24d5d90cff92fbd716d2ef4bed2cff>)，以下内容现已过时，需要更新，故暂不翻译 (在[Talk:Netctl](<../zh-cn/Talk:Netctl.html>)讨论)

From [kernel documentation](<https://docs.kernel.org/networking/bonding.html>): 

    The Linux bonding driver provides a method for aggregating multiple network interfaces into a single logical "bonded" interface. The behavior of the bonded interfaces depends on the mode. Generally speaking, modes provide either hot standby or load balancing services. Additionally, link integrity monitoring may be performed.

####  负载均衡

To use bonding with netctl, additional package from official repositories is required: [ifenslave](<https://archlinux.org/packages/?name=ifenslave>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]. 

Copy `/etc/netctl/examples/bonding` to `/etc/netctl/bond0` and edit it, for example: 
    
    /etc/netctl/bond0
    
    Description='Bond Interface'
    Interface='bond0'
    Connection=bond
    BindsToInterfaces=('eth0' 'eth1')
    IP=dhcp
    IP6=stateless

Now you can disable your old configuration and set _bond0_ to be started automatically. Switch to the new profile, for example: 
    
    # netctl switch-to bond0
    
**注意：** This uses the round-robin policy, which is the default for the `bonding` driver. See [official documentation](<https://docs.kernel.org/networking/bonding.html>) for details. 

Setting the MODE in the netctl configuration is not always successful and it may be necessary to pass options directly to the bonding module on load as noted [here](<https://bbs.archlinux.org/viewtopic.php?id=203255>). This may be needed to use LACP / mode 4. 

**提示：** To check the status and bonding mode: 
    
    $ cat /proc/net/bonding/bond0

####  有线到无线网络故障切换

This example describes how to use _bonding_ to fallback to wireless when the wired Ethernet goes down. This is most useful when both the wired and wireless interface will be connected to the same network. Your wireless router/access point must be configured in [bridge](</wzh/index.php?title=Bridge&action=edit&redlink=1> "Bridge（页面不存在）") mode. 

You will need additional packages from the official repositories: [ifenslave](<https://archlinux.org/packages/?name=ifenslave>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] and [wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包. 

First, [load the module at boot](<../zh-cn/Load_the_module_at_boot.html> "Load the module at boot"): 
    
    /etc/modules-load.d/bonding.conf
    
    bonding

Then, configure the options of the `bonding` driver to use `active-backup` and configure the `primary` parameter to the device you want to be the active one (normally the wired interface). Also, be sure to use the same device name as returned when running `ip link`: 
    
    /etc/modprobe.d/bonding.conf
    
    options bonding mode=active-backup miimon=100 primary=eth0 max_bonds=0

The `miimon` option is needed, for the link failure detection. The `max_bonds` option avoids the `Interface bond0 already exists` error. More information can be obtained on the [kernel documentation](<https://docs.kernel.org/networking/bonding.html>). 

Next, configure a netctl profile to enslave the two hardware interfaces. Use the name of all the devices you want to enslave. If you have more than two wired or wireless interfaces, you can enslave all of them on a bond interface. But, for most cases you will have only two devices, a wired and a wireless one: 
    
    /etc/netctl/failover
    
    Description='A wired connection with failover to wireless'
    Interface='bond0'
    Connection=bond
    BindsToInterfaces=('eth0' 'wlan0')
    IP='dhcp'

Disable any other profiles (specially a wired or wireless) you had enabled before and then enable the failover profile on startup: 
    
    # netctl enable failover
    
Now you need to configure _wpa_supplicant_ to connect to any known network you wish. You should create a file for each interface and enable it on systemd. Create the following file with this content: 
    
    /etc/wpa_supplicant/wpa_supplicant-wlan0.conf
    
    ctrl_interface=/run/wpa_supplicant
    update_config=1

And append to the end of this file any network you want to connect to: 
    
    network={
        ssid="SSID"
        psk=PSK
    }
    
To generate the obfuscated PSK you can run _wpa_passphrase_ as on the [wpa_supplicant#Connecting with wpa_passphrase](<../zh-cn/Wpa_supplicant.html#Connecting_with_wpa_passphrase> "Wpa supplicant") page. 

Now, [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") the `wpa_supplicant@` template service on the network interface, for example `wpa_supplicant@wlan0`. 

You can try now to reboot your machine and see if your configuration worked. 

**注意：** If you get this error on boot bonding: 
    
    wlan0 is up - this may be due to an out of date ifenslave
    
Then this is happening because the _wpa_supplicant_ is being run before the `failover` netctl profile. This happens because [systemd](<../zh-cn/Systemd.html> "Systemd") runs everything in parallel, unless told otherwise. _ifenslave_ need all the interfaces to be down before bonding them to the `bond0` interface. And, since the _wpa_supplicant_ need to put the interface up to be able to scan for networks, this might cause the interface to not be enslaved and your bonding to only have the wired interface. 

If this is your case, then you will need to setup a custom dependency on the `wpa_supplicant@wlan0` service in relation with the `netctl@failover` profile. More specifically, the _wpa_supplicant_ must be started **after** the netctl profile. To accomplish this, create a custom dependency file based on the instructions provided here: [systemd#Handling dependencies](<../zh-cn/Systemd.html#Handling_dependencies> "Systemd")
    
    /etc/systemd/system/wpa_supplicant@wlan0.service.d/customdependency.conf
    
    [Unit]
    After=netctl@failover.service

After that you can try to reboot your system again and see if it works. You can check the status of your bonding by checking [journalctl](<../zh-cn/Systemd/Journal.html> "Journalctl") for the `netctl@failover.service` unit. 

And by checking: 
    
    # ip link
    
You should see something like this: 
    
    1: eth0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT group default qlen 1000
        link/ether xx:xx:xx:xx:xx:xx brd ff:ff:ff:ff:ff:ff
    2: wlan0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond0 state UP mode DORMANT group default qlen 1000
        link/ether xx:xx:xx:xx:xx:xx brd ff:ff:ff:ff:ff:ff
    3: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default 
        link/ether xx:xx:xx:xx:xx:xx brd ff:ff:ff:ff:ff:ff
    
Now, you can test your failover setup, by initiating a big download. Unplug your wired interface. Your download should keep going over the wireless interface. Then, plug your wired interface again and it should keep working. You can debug by checking [journalctl](<../zh-cn/Systemd/Journal.html> "Journalctl") for the `netctl@failover.service` and `wpa_supplicant@wlan0.service` units. 

###  使用任意接口

在某些情况下，可能需要允许配置文件使用系统上的任何接口。一个常见的用例是在具有不同硬件的许多机器上使用通用的磁盘映像（如果它们没有显示输出，这特别有用）。如果您使用内核的命名方案，并且您的机器只有一个以太网接口，那么 eth0 可能是是正确的接口。如果您使用 udev 的[可预测的网络接口名称](<https://systemd.io/PREDICTABLE_INTERFACE_NAMES/>)，则名称将根据特定硬件本身 ( 例如 enp1s0) 分配，而不是简单地根据检测到硬件的顺序 (例如 eth0、 eth1) 分配。这意味着 netctl 配置文件可能仅在一台机器上工作，而不能在另一台机器上工作，因为它们各有不同的接口名称。 

一个简单粗暴的解决方案是使用 `/etc/netctl/interfaces/` 目录。首先设置一个接口别名 (本例中为 `en-any`) ，然后在目录下创建一个同名文件 (确保它[具有可执行权限](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Help:阅读"))。 
    
    /etc/netctl/interfaces/en-any
    
    #!/bin/sh
    for interface in /sys/class/net/en*; do
            break;
    done
    Interface=$(basename "$interface")
    echo "en-any: using interface $Interface";

然后创建一个使用该接口的配置文件。特别注意 `Interface` 指令，请把它设置为刚刚创建的接口别名。其余部分仅作为示例提供。 
    
    /etc/netctl/wired
    
    Description='Wired'
    Interface=en-any
    Connection=ethernet
    IP=static
    Address=('192.168.1.15/24')
    Gateway='192.168.1.1'
    DNS=('192.168.1.1')
    
当 `wired` 配置文件启动时，使用上述两个文件的任何机器都会自动启动并配置系统上找到的第一个以太网接口，而不管 udev 分配给它什么名称。请注意，这不是配置接口的最可靠的方法。如果您使用多个接口，netctl 可能会尝试为它们分配相同的接口，这可能会导致连接中断。如果您不介意更复杂的解决方案，`netctl-auto` 可能更可靠。 

###  使用钩子

netctl 支持 `/etc/netctl/hooks/` 中的钩子和 `/etc/netctl/interfaces/` 中的每个接口钩子，您可以在钩子中设置任何配置文件支持的选项。其中包括最重要的 `ExecUpPost` 和 `ExecDownPre`。 

在读取配置文件前，netctl 会先运行 `hooks` 目录下的**所有可执行的脚本** ，然后才读取配置文件来建立连接。最后它会运行 `interfaces` 目录下与接口同名的可执行脚本（接口钩子）。因此，配置文件中的选项可以被接口钩子覆盖，而 `/etc/netctl/hooks/` 下的钩子选项又可以被配置文件所覆盖。 

**只有** 在使用 `netctl-auto` 时，变量 `$INTERFACE` 和 `$ACTION` 才能在钩子或接口钩子中使用。 

####  示例

#####  连接建立时执行命令
    
    /etc/netctl/hooks/myservices
    
    #!/bin/sh
    ExecUpPost="systemctl start crashplan.service; systemctl start dropbox@<username>.service"
    ExecDownPre="systemctl stop crashplan.service; systemctl stop dropbox@<username>.service"
    
#####  设置默认 DHCP 客户端

要设置或更改用于所有配置文件的 DHCP 客户端，请执行以下操作： 
    
    /etc/netctl/hooks/dhcp
    
    #!/bin/sh
    DHCPClient='dhclient'
    
不要忘记给文件[添加可执行权限](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Help:阅读")

或者也可以对某个特定的网络接口设置单独的 DHCP 客户端，只需要创建一个接口钩子（`/etc/netctl/interfaces/<interface>` 脚本）并设置如下参数就可以了： 
    
    DHCPClient='dhclient'
    
###  最简易的 WPAConfigSection 配置

如 [netctl.profile(5) § OPTIONS FOR ‘WIRELESS’ CONNECTIONS](<https://man.archlinux.org/man/netctl.profile.5#OPTIONS_FOR_%E2%80%98WIRELESS%E2%80%99_CONNECTIONS>) 中所述，`WPAConfigSection` 变量是传递给 [wpa_supplicant](<../zh-cn/Wpa_supplicant.html> "Wpa supplicant") 的配置项数组。因此，一个最简单的 WPAConfigSection 将包含： 
    
    Description='A wireless connection using a custom network block configuration'
    Interface=wlan0
    Connection=wireless
    Security=wpa-configsection
    IP=dhcp
    WPAConfigSection=(
        'ssid="University"'
        'psk="very secret passphrase"'
    )
    
**注意：** 如果要连接到具有非 ASCII 字符（unicode、表情符号等）的 SSID，可以将 SSID 指定为十六进制而不是字符串，例如 `ssid=F09F90BA` 表示“🐺”。 当不确定十六进制编码时，可以运行 _wifi-menu_ 命令来查看（确保删除 \ 和 x 字符）。

###  /etc/resolv.conf

如果您在配置文件中使用 `DNS*` 选项， _netctl_ 将调用 [resolvconf](</wzh/index.php?title=Resolvconf&action=edit&redlink=1> "Resolvconf（页面不存在）") 来覆盖 [resolv.conf](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html> "Resolv.conf")。 

##  故障排除

###  Job for netctl@wlan(...).service failed

**警告：** 本节假设在启动 _netctl_ 配置文件或服务之前没有其他网络服务正在运行。有关详细信息，请参阅 [#安装](<#%E5%AE%89%E8%A3%85>)。

有些人在使用 _netctl_ 连接网络时会遇到问题，例如： 
    
    # netctl start wlan0-ssid
    
    Job for netctl@wlan0\x2ssid.service failed. See 'systemctl status netctl@wlan0\x2ssid.service' and 'journalctl -xn' for details.
    
当以 root 身份运行 `journalctl -xn` 查看日志时，可能会看到以下错误： 

1\. 如果您的网络接口（在本例中为 `wlan0`）已启动： 
    
    network[2322]: The interface of network profile 'wlan0-ssid' is already up
    
禁用网络接口可能能够解决这个问题： 
    
    # ip link set wlan0 down
    
然后再重试： 
    
    # netctl start wlan0-ssid
    
2\. 如果错误仍然存在，请在添加 `ForceConnect` 选项后重试： 
    
    /etc/netctl/wlan0-ssid
    
    ...
    ForceConnect=yes
    
保存并尝试再次启动配置文件 : 
    
    # netctl start wlan0-ssid
    
### dhcpcd: ipv4_addroute: File exists

在某些系统上，把 dhcpcd 与 netctl 结合使用会导致唤醒计算机时出现超时问题，特别是在你切换了网络的时候。netctl 将报告称已成功连接，但你仍然会遇到连接超时等问题。这种情况是因为旧的默认路由仍然存在，并且没有被更新。避免这种问题的一个方法是改用 [dhclient](<#%E8%AE%BE%E7%BD%AE%E9%BB%98%E8%AE%A4_DHCP_%E5%AE%A2%E6%88%B7%E7%AB%AF>) 作默认 dhcp 客户端。 有关此问题的更多信息，请[参阅此处](<https://bbs.archlinux.org/viewtopic.php?pid=1399842#p1399842>). 

###  DHCP 超时问题

如果您在通过 DHCP 请求租约时遇到超时问题，则可以将超时值设置得比 netctl 默认的 30 秒长。比如可以在 `/etc/netctl/hooks/` 或 `/etc/netctl/interfaces/` 中创建一个[可执行文件](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Help:阅读")，并向其中添加 `TimeoutDHCP=40` 选项。 

###  调试 dhcpcd

如果 dhcpcd 无法获得一个地址，请将 `-d` 选项添加到 `/usr/lib/netctl/dhcp`，然后以 root 用户身份运行 `journalctl -xe` 来查看调试日志。通过查看调试日志，您可能能发现客户端因为 IP 地址已被使用而拒绝了服务器提供的 IP 地址等错误原因。 

###  连接超时问题

如果您遇到与 DHCP 无关的超时问题 ( 例如在使用静态 IP 的连接上 ) ，并且在启动配置文件时遇到类似下列错误： 
    
    # journalctl _SYSTEMD_UNIT=netctl@_profile_.service
    
    Starting network profile '_profile_ '...
    No connection found on interface 'eth0' (timeout)
    Failed to bring the network up for profile '_profile'_

那么，您应该修改 `TimeoutCarrier=` 和 `TimeoutUp=` 选项来调高检测网线插好和网卡就绪的超时时间。 
    
    /etc/netctl/_profile_
    
    ...
    TimeoutUp=300
    TimeoutCarrier=300
    
别忘了用以下命令重新启用配置文件： 
    
    # netctl reenable _profile_
    
###  唤醒时 netctl-auto 故障

有时，当系统从挂起、休眠或混合休眠恢复时， _netctl-auto_ 无法重新连接。一个简单的解决方案是重新启动 _netctl-auto_ 服务。这可以通过类似 [netctl-auto-resume](<https://aur.archlinux.org/packages/netctl-auto-resume/>)AUR 这样的附加服务实现自动化： 
    
    /etc/systemd/system/netctl-auto-resume@.service
    
    [Unit]
    Description=restart netctl-auto on resume.
    Requisite=netctl-auto@%i.service
    After=sleep.target
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/systemctl restart netctl-auto@%i.service
    
    [Install]
    WantedBy=sleep.target
    
要为您的无线网卡[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")此服务，请以 root 权限启用 `netctl-auto-resume@wlan0.service` 服务，并将其中的 `wlan0` 更改为所需的网络接口。 

如果服务单元启动时，对应的网卡尚未恢复运行，则此操作将失败。您可以通过在 _After_ 选项中添加要依赖的 [Systemd 目标](<../zh-cn/Systemd.html#%E7%9B%AE%E6%A0%87%EF%BC%88target%EF%BC%89> "Systemd")来修复 : 
    
    /etc/systemd/system/netctl-auto-resume@.service
    
    ...
    After=sleep.target sys-subsystem-net-devices-%i.device
    ...
    
###  netctl-auto 无法自动解锁无线网卡

许多笔记本电脑有一个硬件按钮 ( 或开关 ) 来屏蔽无线网卡，但是该卡也可以被内核屏蔽。这可以由 [rfkill](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE/%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#Rfkill_%E8%AF%B4%E6%98%8E> "Rfkill") 处理。 

如果您希望 _netctl-auto_ 自动解禁您的无线卡并连接到特定网络，请参考 [netctl.profile(5)](<https://man.archlinux.org/man/netctl.profile.5>) 为您的无线网络连接设置 `RFKill=++auto++` 选项。 

###  在使用多个网卡时提示 RTNETLINK answers: File exists

这是一个非常具有误导性的报错，这实际上意味着您已经在之前的某个 netctl 控制文件配置了一个默认路由。当 netctl 在启动第 n 个网卡并且尝试设置它的本地路由时，因为已经在启动第 n-1 个网卡时设置过默认路由了，所以该操作会失败。 

把它删掉后就一切正常了，除了因为没有默认路由而无法正常上网以外。而即使用 `ExecUpPost` 也无法解决这个问题，因为他也会为每个网卡执行一遍。 

一种可能的解决方案是创建一个新服务。并将下面的“FIRST_INTERFACE”和“SECOND_INTERFACE”替换为接口名称，将“192.168.xxx.yyy”替换为你的默认网关。 
    
    /etc/systemd/system/defaultrouter.service
    
    [Unit]
    Description="Configure default gateway"
    Requires=netctl@FIRST_INTERFACE.service netctl@SECOND_INTERFACE.service
    After=netctl@FIRST_INTERFACE.service netctl@SECOND_INTERFACE.service
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/ip route add default via 192.168.xxx.yyy
    
    [Install]
    WantedBy=network-online.target
    
###  使用 eduroam 和其他 MSCHAPv2 连接时遇到问题

参见 [wpa_supplicant#Problems with eduroam and other MSCHAPv2 connections](<../zh-cn/Wpa_supplicant.html#Problems_with_eduroam_and_other_MSCHAPv2_connections> "Wpa supplicant")。 

###  在配置文件中使用 .include 指令导致日志警告

仍然使用 systemd 旧的 `.include` 指令的配置文件将生成日志警告，例如： 
    
    systemd[1]: /etc/systemd/system/netctl@<profile>.service:1: .include directives are deprecated, and support for them will be removed in a future version of systemd. Please use drop-in files instead.
    
详见 [FS#59494](<https://bugs.archlinux.org/task/59494>)。 

执行 
    
    netctl reenable _profile_
    
能配置文件更新为新的 [drop-in unit file](</wzh/index.php?title=Drop-in_unit_file&action=edit&redlink=1> "Drop-in unit file（页面不存在）") 格式。 

###  钩子无效

如果在 `/etc/netctl/hooks/` 中有多个钩子，那么像 `ExecUpPost` 和 `ExecDownPre` 这样的变量会被重复覆盖，导致只能执行其中一个文件的。要解决此问题，请如下定义变量： 
    
    /etc/netctl/hooks/test
    
    ExecUpPost="some command ; "$ExecUpPost
    ExecDownPre="some command ; "$ExecDownPre
    
这样可以在其他命令前面附加要执行的命令，防止被重复覆盖。 

##  参阅

  * [初始邮件列表公告](<https://lists.archlinux.org/archives/list/arch-projects@lists.archlinux.org/message/KLCFCAMJQSJBC2UFRXAQZ2YW2JUSHN7O/>)
  * [官方公告帖子](<https://bbs.archlinux.org/viewtopic.php?id=157670>)
  * [官方新闻公告](<https://archlinux.org/news/netctl-is-now-in-core/>)
