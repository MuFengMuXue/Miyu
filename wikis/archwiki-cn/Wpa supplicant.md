**翻译状态：**

  * 本文（或部分内容）译自 [WPA supplicant](<https://wiki.archlinux.org/title/WPA_supplicant> "arch:WPA supplicant")，最近一次同步于 2025-01-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/WPA_supplicant?diff=0&oldid=824406>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/WPA_supplicant_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [网络配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")
  * [无线网络配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE/%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置/无线网络配置")
  * [iwd](<../zh-cn/Iwd.html> "Iwd")

[wpa_supplicant](<https://w1.fi/wpa_supplicant/>) 是跨平台的[接入客户端](<https://zh.wikipedia.org/wiki/Supplicant_\(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C\)> "zhwp:Supplicant \(计算机网络\)")，支持 WPA，WPA2 和 WPA3（[IEEE 802.11i](<https://en.wikipedia.org/wiki/IEEE_802.11i-2004> "wikipedia:IEEE 802.11i-2004")），适用于桌面设备、笔记本及嵌入式系统。它是用于客户端的 [IEEE 802.1X](<https://zh.wikipedia.org/wiki/IEEE_802.1X> "zhwp:IEEE 802.1X")/WPA 组件。它实现了与 WPA 验证者交互，控制漫游和无线驱动的 [IEEE 802.11](<https://zh.wikipedia.org/wiki/IEEE_802.11> "zhwp:IEEE 802.11") 验证和关联。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包 软件包。此软件包提供了主程序 _wpa_supplicant_ ，密码工具 _wpa_passphrase_ 和文字界面前端 _wpa_cli_ 。 

还可以额外安装官方的 [wpa_supplicant_gui](<https://aur.archlinux.org/packages/wpa_supplicant_gui/>)AUR，该软件包提供了 _wpa_supplicant_ 的图形界面前端 _wpa_gui_ 。[wpa-cute](<https://aur.archlinux.org/packages/wpa-cute/>)AUR 是 _wpa_gui_ 的一个分支，提供了额外的修正和改进。 

##  概览

连接到加密无线网络的第一步是让 _wpa_supplicant_ 获取 WPA 认证者的认证。为此， _wpa_supplicant_ 必须进行配置以使其能够向认证者提交认证信息。 

完成认证后需要分配一个 IP 地址，具体步骤请参考[网络配置#IP 地址](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#IP_%E5%9C%B0%E5%9D%80> "网络配置")。 

##  使用 wpa_cli 进行连接

这种方法使用了 _wpa_cli_ 命令行工具，可以用其扫描可用网络，并配置 _wpa_supplicant_ 。详细信息可以参考 [wpa_cli(8)](<https://man.archlinux.org/man/wpa_cli.8>) 。 

使用 _wpa_cli_ 前，需要先为 _wpa_supplicant_ 指定一个控制接口，且它需要获得更新配置的权限。先创建一个最小配置： 
    
    /etc/wpa_supplicant/wpa_supplicant.conf
    
    ctrl_interface=/run/wpa_supplicant
    update_config=1

**警告：** 将 `update_config` 设为 `1` 会允许 _wpa_supplicant_ 覆写配置文件。 _wpa_supplicant_ 会在覆写时根据您的默认 [umask](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "文件权限与属性") 重置文件权限，如果您的系统有多用户，可能会意外使任何人能够读取该文件，由此而泄漏密码。

接下来启动 _wpa_supplicant_ ： 
    
    # wpa_supplicant -B -i _interface_ -c /etc/wpa_supplicant/wpa_supplicant.conf
    
**提示：** 可以参考[网络配置#列出网络接口](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E5%88%97%E5%87%BA%E7%BD%91%E7%BB%9C%E6%8E%A5%E5%8F%A3> "网络配置")查看你的无线网卡名称。

完成后，执行： 
    
    # wpa_cli
    
这一步完成后会显示一个交互提示符（`>`），同时带有 tab 补全及命令描述功能，还可以使用 `help` 命令查看帮助。 

**提示：** 控制接口的默认位置为 `/var/run/wpa_supplicant/`，可以使用 `-p` 选项手动指定位置，以与 _wpa_supplicant_ 的配置相符。另外，可以使用 `-i` 选项指定需配置的接口，否则将使用由 _wpa_supplicant_ 管理的第一个网络接口。

**提示：**

  * 控制接口的默认位置为 `/var/run/wpa_supplicant/`，可以使用 `-p` 选项手动指定位置，以与 _wpa_supplicant_ 的配置相符。
  * 可以使用 `-i` 选项指定需配置的接口，否则将使用由 _wpa_supplicant_ 管理的第一个无线网络接口。

使用 `scan` 和 `scan_results` 命令查看可用网络： 
    
    > scan
    OK
    <3>CTRL-EVENT-SCAN-RESULTS
    > scan_results
    bssid / frequency / signal level / flags / ssid
    00:00:00:00:00:00 2462 -49 [WPA2-PSK-CCMP][ESS] _MYSSID_
    11:11:11:11:11:11 2437 -64 [WPA2-PSK-CCMP][ESS] _ANOTHERSSID_
    
要将网络与 `_MYSSID_` 进行关联，先添加网络，配置凭证并启用： 
    
    > add_network
    0
    > set_network 0 ssid "_MYSSID_ "
    > set_network 0 psk "_passphrase_ "
    > enable_network 0
    <2>CTRL-EVENT-CONNECTED - Connection to 00:00:00:00:00:00 completed (reauth) [id=0 id_str=]
    
如果对应的 SSID 无需密码验证，则需要将命令 `set_network 0 psk "_passphrase_ "` 替换为 `set_network 0 key_mgmt NONE`，以将网络指定为无密码。 

**注意：**

  * 可以添加多个网络配置，每个网络都按照数字顺序进行排列，所以第一个网络的索引为 0。
  * If no connection can be established, some information will be printed, and periodic attempts will be made. As part of the periodic attempts, a user prompt will also be given periodically. Issuing the `disable_network 0` command will stop the periodic attempts and return to a steady user prompt.
  * 如果使用 `set_network` 提供了凭证，那么就会由 _引号_ 括起的 "passphrase" 字符串生成 [PSK](<https://en.wikipedia.org/wiki/Pre-shared_key> "wikipedia:Pre-shared key")。另外，你也可以 _不使用引号_ 通过 [wpa_passphrase](<#%E4%BD%BF%E7%94%A8_wpa_passphrase_%E8%BF%9B%E8%A1%8C%E8%BF%9E%E6%8E%A5>) 直接向 `psk` 传入 PSK。

最后，将网络保存到配置文件中，并退出 _wpa_cli_ ： 
    
    > save_config
    OK
    > quit
    
完成后，你需要获取一个 IP 地址，具体步骤请参考[网络配置#网络管理](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E7%AE%A1%E7%90%86> "网络配置")。 

##  使用 wpa_passphrase 进行连接

通过使用命令行工具 _wpa_passphrase_ 生成 _wpa_supplicant_ 所需的最小配置，可以快速连接到已知 SSID 的无线网络。例如： 
    
    $ wpa_passphrase _MYSSID_ _passphrase_
    
    network={
        ssid="_MYSSID_ "
        #psk="_passphrase_ "
        psk=59e0d07fa4c7741797a4e394f38a5c321e3bed51d54ad5fcbd3f84bc7415d73d
    }

上例表明， _wpa_supplicant_ 可以与 _wpa_passphrase_ 协同工作，只需简单地这样做即可： 
    
    # wpa_supplicant -B -i _interface_ -c <(wpa_passphrase _MYSSID_ _passphrase_)
    
**提示：**

  * 上条命令需要使用 [root shell](<../zh-cn/Sudo.html#Login_shell> "Sudo")。
  * 如果输入内容包含空格，请使用引号，例如：`"secret passphrase"`.
  * 要找出无线网卡的名字，请参考[网络配置#列出网络接口](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E5%88%97%E5%87%BA%E7%BD%91%E7%BB%9C%E6%8E%A5%E5%8F%A3> "网络配置")。
  * 某些少见的复杂密码需要从文件导入，例如：`wpa_passphrase _MYSSID_ < passphrase.txt`，或者从命令行输入，例如：`wpa_passphrase _MYSSID_ <<< "_passphrase_ "`。
  * Alternatively, when using special characters in the passphrase, rather than escaping them, simply invoke `wpa_passphrase` without specifying the passphrase. It will then prompt for it to be entered in the standard input where users can paste it even if it contains special characters.

完成后需要获取一个 IP 地址，具体步骤请参考[网络配置#IP 地址](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#IP_%E5%9C%B0%E5%9D%80> "网络配置")。 

##  高级用法

对于各种纷繁复杂的网络，更常见的场景是使用 [EAP](<https://zh.wikipedia.org/wiki/%E6%89%A9%E5%B1%95%E8%AE%A4%E8%AF%81%E5%8D%8F%E8%AE%AE> "zhwp:扩展认证协议") 管理配置文件。各种配置及其范例可参阅手册页 [wpa_supplicant.conf(5)](<https://man.archlinux.org/man/wpa_supplicant.conf.5>)；所有可支持的配置参数可参考范例文件 `/usr/share/doc/wpa_supplicant/wpa_supplicant.conf`。[[1]](<https://w1.fi/cgit/hostap/plain/wpa_supplicant/wpa_supplicant.conf>)。 

###  配置

如上文中[#使用 wpa_passphrase 进行连接](<#%E4%BD%BF%E7%94%A8_wpa_passphrase_%E8%BF%9B%E8%A1%8C%E8%BF%9E%E6%8E%A5>)一节所述，一个基本的配置文件可以这样生成： 
    
    # wpa_passphrase _MYSSID_ _passphrase_ > /etc/wpa_supplicant/example.conf
    
这样仅仅是创建了一个 `network` 网络配置节段。 A configuration file with also the ability of [#使用 wpa_cli 进行连接](<#%E4%BD%BF%E7%94%A8_wpa_cli_%E8%BF%9B%E8%A1%8C%E8%BF%9E%E6%8E%A5>) and some other common options may look like： 
    
    /etc/wpa_supplicant/example.conf
    
    # Giving configuration update rights to wpa_cli
    ctrl_interface=/run/wpa_supplicant
    ctrl_interface_group=wheel
    update_config=1
    
    # AP scanning
    ap_scan=1
    
    # ISO/IEC alpha2 country code in which the device is operating
    country=US
    
    # network section generated by wpa_passphrase
    network={
        ssid="MYSSID"
        psk=59e0d07fa4c7741797a4e394f38a5c321e3bed51d54ad5fcbd3f84bc7415d73d
    }

如果可以不顾及安全问题，`network` 中的通行字可以换成由引号包围的纯文本： 
    
    psk="passphrase"
    
如果网络没有设置通行字，如公共无线网络： 
    
    network={
       ssid="MYSSID"
       key_mgmt=NONE
    }
    
To connect to a WPA-Enterprise network, see [#802.1x/radius](<#802.1x/radius>). 

Further `network` blocks may be added manually, or using _wpa_cli_ as illustrated in [#使用 wpa_cli 进行连接](<#%E4%BD%BF%E7%94%A8_wpa_cli_%E8%BF%9B%E8%A1%8C%E8%BF%9E%E6%8E%A5>). In order to use _wpa_cli_ , a control interface must be set with the `ctrl_interface` option. Setting `ctrl_interface_group=wheel` allows users belonging to such group to execute _wpa_cli_. This setting can be used to enable users without root access (or equivalent via sudo etc) to connect to wireless networks. Also add `update_config=1` so that changes made with _wpa_cli_ to `example.conf` can be saved. Note that any user that is a member of the `ctrl_interface_group` group will be able to make changes to the file if this is turned on. 

`fast_reauth=1` and `ap_scan=1` are the _wpa_supplicant_ options active globally at the time of writing. Whether you need them, or other global options too for that matter, depends on the type of network to connect to. If you need other global options, simply copy them over to the file from `/usr/share/doc/wpa_supplicant/wpa_supplicant.conf`. 

Alternatively, `wpa_cli set` can be used to see options' status or set new ones. Multiple network blocks may be appended to this configuration: the supplicant will handle association to and roaming between all of them. The strongest signal defined with a network block usually is connected to by default, one may define `priority=` to influence behaviour. For example to auto-connect to any unsecured network as a fallback with the lowest priority: 
    
    network={
       key_mgmt=NONE
       priority=-999
    }
    
Once you have finished the configuration file, you can optionally use it as a system-wide or per-interface default configuration by naming it according to the paths listed in [#At boot (systemd)](<#At_boot_\(systemd\)>). This also applies if you use additional network manager tools, which may rely on the paths (for example [Dhcpcd#10-wpa_supplicant](<../zh-cn/Dhcpcd.html#10-wpa_supplicant> "Dhcpcd")). 

**提示：** To configure a network block to a hidden wireless _SSID_ , which by definition will not turn up in a regular scan, the option `scan_ssid=1` has to be defined in the network block.

###  连接

####  手动连接

首先启动 _wpa_supplicant_ 命令，其最常用的参数为： 

  * `-B` \- 在后台运行。
  * `-c _filename_` \- 配置文件的路径。
  * `-i _interface_` \- 要监听的设备。
  * `-D _driver_` \- （可选）指定使用的驱动。运行 `wpa_supplicant -h` 以查看所支持的驱动列表。 
    * `nl80211` 是目前的标准，但是不是所有无线网卡都支持。
    * `wext` 目前已经弃用，但是仍被广泛支持。

见 [wpa_supplicant(8)](<https://man.archlinux.org/man/wpa_supplicant.8>) 获取全部参数的列表。例如： 
    
    # wpa_supplicant -B -i _interface_ -c /etc/wpa_supplicant/example.conf
    
接着是用在[#概览](<#%E6%A6%82%E8%A7%88>)中提到的方法手动获取 IP，例如： 
    
    # dhcpcd _interface_
    
**提示：**

  * _dhcpcd_ has a hook that can launch _wpa_supplicant_ implicitly, see [dhcpcd#10-wpa_supplicant](<../zh-cn/Dhcpcd.html#10-wpa_supplicant> "Dhcpcd").
  * While testing arguments/configuration it may be helpful to launch _wpa_supplicant_ in the foreground (i.e. _without_ the `-B` option) for better debugging messages.

####  引导时连接（systemd）

_wpa_supplicant_ 软件包中提供了多个 [systemd](<../zh-cn/Systemd.html> "Systemd") 服务文件： 

  * `wpa_supplicant.service` \- 使用 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") ，建议 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 用户使用。
  * `wpa_supplicant@_interface_.service` \- 接受网口名作为参数，启动服务于该网口的 _wpa_supplicant_ 守护进程。这个服务将读取 `/etc/wpa_supplicant/wpa_supplicant-_interface_.conf` 这个配置文件，在使用 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 时比较有用。
  * `wpa_supplicant-nl80211@_interface_.service` \- 同样接受网口名作为参数，但明确限定使用 `nl80211` 驱动（详阅下文）。它的配置文件是 `/etc/wpa_supplicant/wpa_supplicant-nl80211-_interface_.conf`。
  * `wpa_supplicant-wired@_interface_.service` \- 同样接受网口名作为参数，使用 `wired`（有线网络）驱动。它的配置文件是 `/etc/wpa_supplicant/wpa_supplicant-wired-_interface_.conf`。

在引导时激活无线网络，就是激活服务于某个无线网络接口的上述服务单元之一，例如[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `wpa_supplicant@_interface_`。 

现在就可以像[概览](<#%E6%A6%82%E8%A7%88>)一节所述，可以选定某个网络接口并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")其服务单元的一个实例，从而获取一个 IP 地址，例如[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `dhcpcd@_interface_`。 

**提示：** _dhcpcd_ 可以后台加载 _wpa_supplicant_ ，参阅 [dhcpcd#10-wpa_supplicant](<../zh-cn/Dhcpcd.html#10-wpa_supplicant> "Dhcpcd")。

#####  802.1x/radius

To connect a wired adapter using 802.1x/[radius](</wzh/index.php?title=Freeradius&action=edit&redlink=1> "Freeradius（页面不存在）") you will need to specify some configurations and enable the necessary service for the adapter. This is useful for headless servers using [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd"). 

You may need to specify the `_wired_` driver with the `_-D wired_` command line option (see [#Manual](<#Manual>)) if the default driver does not support your adapter. 

Replace `_adapter_` with the wired adapter you wish to connect, and adapt the settings to match your 802.1x/radius requirements. 
    
    /etc/wpa_supplicant/wpa_supplicant-wired-_adapter_.conf
    
    ctrl_interface=/run/wpa_supplicant
    ap_scan=0
    network={
      key_mgmt=IEEE8021X
      eap=PEAP
      identity="_user_name_ "
      password="_user_password_ "
      phase2="autheap=MSCHAPV2"
    }

**提示：** The same configuration, but for a wireless adapter, would require changing `IEEE8021X` to `WPA-EAP` and removing the `ap_scan=0` line

Since this file is storing a plaintext password, [chown](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E4%BF%AE%E6%94%B9%E6%89%80%E6%9C%89%E8%80%85> "Chown") it to `root:root` and [chmod](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E4%BF%AE%E6%94%B9%E6%9D%83%E9%99%90> "Chmod") it to `600`. 

To use the hash instead of the plaintext password, you can use the `hash` keyword: 
    
    password=hash:_hash_of_plaintext_password_
    
To hash your password: 
    
    $ iconv -t utf16le | openssl dgst -md4 -provider legacy
    
After invoking the command above, provide your plain password and then press `Ctrl+d`. 

**注意：** Hashing the password does not improve the security nor avoid the risk of exposing secrets.

Before running the `wpa_supplicant-wired@_adapter_.service` service, make sure to set the device down: 
    
    # ip link set _adapter_ down
    
**提示：** This setup can be used during system installation as well, though you may want to run using `dhcpcd@_adapter_.service` to solicit an address.

###  wpa_cli 操作脚本

_wpa_cli_ can run in daemon mode and execute a specified script based on events from _wpa_supplicant_. Two events are supported: `CONNECTED` and `DISCONNECTED`. Some [environment variables](<../zh-cn/Environment_variables.html> "Environment variables") are available to the script, see [wpa_cli(8)](<https://man.archlinux.org/man/wpa_cli.8>) for details. 

The following example will use [notify-send](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%80%9A%E7%9F%A5%E7%A8%8B%E5%BA%8F.html#Libnotify> "Notify-send") to notify the user about the events: 
    
    #!/bin/sh
    
    case "$2" in
        CONNECTED)
            notify-send "WPA supplicant: connection established";
            ;;
        DISCONNECTED)
            notify-send "WPA supplicant: connection lost";
            ;;
    esac
    
Remember to make the script [executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable"), then use the `-a` flag to pass the script path to _wpa_cli_ : 
    
    $ wpa_cli -a _/path/to/script_
    
###  漫游

When connected to a wireless network with multiple access points, _wpa_supplicant_ is typically responsible for roaming between access points. Choosing a new access point requires _wpa_supplicant_ to perform a scan of available networks, which causes a brief interruption in connectivity to the current access point while the wireless radio scans other frequencies. After a scan, if _wpa_supplicant_ detects a closer access point (BSSID) in the current network (SSID), in terms of signal strength (RSSI), it will re-associate to the closer access point. 

The default configuration of _wpa_supplicant_ has relatively timid roaming: it will rescan only when the association to the current access point is lost. This means that, if a client moves far away from its current access point, but not far enough to completely lose signal, the client will keep using the weak signal instead of roaming to a closer access point. 

To make _wpa_supplicant_ more aggressive about roaming, set the `bgscan` parameter in the configuration file, such as: 
    
    bgscan="simple:30:-70:3600"
    
The above example will cause _wpa_supplicant_ to scan every 30 seconds when the signal is weak (below -70), and every 3600 seconds otherwise. `bgscan` can be specified either in specific `network` blocks or globally for all networks. 

##  排错

**警告：** Make sure that you do not have remnant configuration files based on the full documentation example `/usr/share/doc/wpa_supplicant/wpa_supplicant.conf`. It is filled with uncommented network examples that may lead to random errors in practice ([FS#40661](<https://bugs.archlinux.org/task/40661>)).

### Debugging connection failures

In order to determine why you are unable to connect to an access point you can run _wpa_supplicant_ with the `-d` flag for debug messages, wait a couple seconds then look for lines that list SSIDs and the reason they were not connected to. For example: 
    
    # wpa_supplicant -i wlan0 -c /etc/wpa_supplicant/example.conf -d
    
    wlan0: Selecting BSS from priority group 0
    wlan0: 0: d2:93:5b:b7:5d:d2 ssid=_wpa_ie_len=26 rsn_ie_len=24 caps=0x511 level=-54 freq=5180_
    wlan0:    skip - SSID not known
    wlan0: 1: f2:93:5b:b7:5d:d2 ssid=_wpa_ie_len=26 rsn_ie_len=24 caps=0x511 level=-54 freq=5180_
    wlan0:    skip - SSID not known
    wlan0: 2: b2:93:5b:b7:5d:d2 ssid=_wpa_ie_len=26 rsn_ie_len=24 caps=0x511 level=-54 freq=5180_
    wlan0:    skip - SSID not known
    wlan0: 3: b0:93:5b:b7:5d:d2 ssid='Access Point 1' wpa_ie_len=0 rsn_ie_len=20 caps=0x511 level=-55 freq=5180  wps
    wlan0:    skip - SSID mismatch
    wlan0: 4: c4:13:e2:33:42:20 ssid='\x00\x00\x00\x00' wpa_ie_len=22 rsn_ie_len=0 caps=0x111 level=-69 freq=5260
    wlan0:    skip - SSID mismatch
    wlan0: 5: c4:13:e2:33:42:24 ssid='Home' wpa_ie_len=0 rsn_ie_len=26 caps=0x1111 level=-69 freq=5260
    wlan0:    skip RSN IE - no mgmt frame protection enabled but AP requires it
    wlan0:    reject due to mismatch with WPA/WPA2
    ...

In this case we are trying to connect to an access point with the SSID _home_. The reason the connection fails is `skip RSN IE - no mgmt frame protection enabled but AP requires it`, so we need to add `ieee80211w=2` to our configuration file. 

###  某些硬件不支持 nl80211 驱动

On some (especially old) hardware, _wpa_supplicant_ may fail with the following error: 
    
    Successfully initialized wpa_supplicant
    nl80211: Driver does not support authentication/association or connect commands
    wlan0: Failed to initialize driver interface
    
This indicates that the standard `nl80211` driver does not support the given hardware. The deprecated `wext` driver might still support the device: 
    
    # wpa_supplicant -B -i wlan0 **-D wext** -c /etc/wpa_supplicant/example.conf
    
If the command works to connect, and the user wishes to use [systemd](<../zh-cn/Systemd.html> "Systemd") to manage the wireless connection, it is necessary to [edit](<../zh-cn/Systemd.html#Drop-in_files> "Systemd") the `wpa_supplicant@.service` unit provided by the package and modify the `ExecStart` line accordingly: 
    
    /etc/systemd/system/wpa_supplicant@.service.d/wext.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/wpa_supplicant -c/etc/wpa_supplicant/wpa_supplicant-%I.conf -i%I **-Dnl80211,wext**

**注意：** Multiple comma separated driver wrappers in option `-Dnl80211,wext` makes _wpa_supplicant_ use the first driver wrapper that is able to initialize the interface (see [wpa_supplicant(8) § EXAMPLES](<https://man.archlinux.org/man/wpa_supplicant.8#EXAMPLES>)). This is useful when using mutiple or removable (e.g. USB) wireless devices which use different drivers.

###  挂载了网络共享（CIFS）时的关机问题

When you use wireless to connect to network shares you might have the problem that the shutdown takes a very long time. That is because systemd runs against a 3 minute timeout. The reason is that WPA supplicant is shut down too early, i.e. before systemd tries to unmount the share(s). A [bug report](<https://github.com/systemd/systemd/issues/1435>) suggests a work-around by [editing](<../zh-cn/Systemd.html#Drop-in_files> "Systemd") the `wpa_supplicant@.service` as follows: 
    
    /etc/systemd/system/wpa_supplicant.service.d/override.conf
    
    [Unit]
    After=dbus.service

###  口令相关的问题

[wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包 may not work properly if directly passed via stdin particularly long or complex passphrases which include special characters. This may lead to errors such as `failed 4-way WPA handshake, PSK may be wrong` when launching [wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包. 

In order to solve this try using here strings `wpa_passphrase <MYSSID> <<< "<passphrase>"` or passing a file to the `-c` flag instead: 
    
    # wpa_supplicant -i <interface> -c /etc/wpa_supplicant/example.conf
    
In some instances it was found that storing the passphrase cleartext in the `psk` key of the `wpa_supplicant.conf` `network` block gave positive results (see [[2]](<https://www.linuxquestions.org/questions/linux-wireless-networking-41/wpa-4-way-handshake-failed-843394/>)). However, this approach is rather insecure. Using `wpa_cli` to create this file instead of manually writing it gives the best results most of the time and therefore is the recommended way to proceed. 

### Problems with Eduroam

If the institution the user studies or works at did not upgrade their network tunnel's encryption to at least TLS 1.2 yet and still uses TLS 1.0 or 1.1 for network traffic encryption in their Eduroam Wi-Fi infrastructure, OpenSSL 3.x throws an "unsupported protocol" error and the client machine's Wi-Fi backend (either wpa_supplicant or [iwd](<../zh-cn/Iwd.html> "Iwd")) refuses to establish a connection any further. Fortunately, an easy workaround exists for OpenSSL's TLS 1.0 and 1.1 deprecation without making the client computer's whole Wi-Fi connection stack globally vulnerable to attacks, although it only works with [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager"). 

Consult [NetworkManager#WPA Enterprise connections fail to authenticate with OpenSSL "unsupported protocol" error](<../zh-cn/NetworkManager.html#WPA_Enterprise_connections_fail_to_authenticate_with_OpenSSL_"unsupported_protocol"_error> "NetworkManager") for the solution. 

Connman users can visit the [ConnMan#Connecting to eduroam (802.1X)](<../zh-cn/ConnMan.html#Connecting_to_eduroam_\(802.1X\)> "ConnMan") article for their own version of the fix. 

### Connections to pure WPA3-SAE access points

Make sure to define the following within the network block of the configuration to enable connections to pure WPA3 access points: 
    
    ssid="network SSID"
    key_mgmt=SAE
    sae_password="the.literal.wifi.password"
    ieee80211w=2
    
Additionally, Intel Wi-Fi 6 cards may need `sae_pwe=1` in the main (non network) section of the config file. 

###  Connections to mixed WPA2-PSK/WPA3-SAE access points

Mixed WPA2-PSK/WPA3-SAE access points will require an alternative setting for key_mgmt as shown below: 
    
    ssid="network SSID"
    key_mgmt=WPA-PSK-SHA256
    psk=xxx
    ieee80211w=2
    
### Hardware 802.11w support

You can check for hardware support of MFP/PMF (_M_ anagement _F_ rame _P_ rotection / _P_ rotected _M_ anagement _F_ rames) on the interface client by running: 
    
    $ iw phy phy0 info | grep 00-0f-ac:6
    
Most Wi-Fi devices support this standard introduced in 2009, except some limited (aka non x86_64 related) or old hardware. 

##  参阅

  * [wpa_supplicant 主页](<https://w1.fi/wpa_supplicant/>)
  * [wpa_supplicant README](<https://w1.fi/cgit/hostap/plain/wpa_supplicant/README>) \- 项目完整文档，包含了 manpage 未列出的 _wpa_cli_ 命令
  * [wpa_cli 用例](<https://gist.github.com/buhman/7162560>)
  * [wpa_supplicant(8)](<https://man.archlinux.org/man/wpa_supplicant.8>)
  * [wpa_supplicant.conf(5)](<https://man.archlinux.org/man/wpa_supplicant.conf.5>)
  * [wpa_cli(8)](<https://man.archlinux.org/man/wpa_cli.8>)
  * [Kernel.org wpa_supplicant 文档](<https://wireless.wiki.kernel.org/en/users/documentation/wpa_supplicant>)
