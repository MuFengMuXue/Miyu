**翻译状态：**

  * 本文（或部分内容）译自 [Transmission](<https://wiki.archlinux.org/title/Transmission> "arch:Transmission")，最近一次同步于 2024-01-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Transmission?diff=0&oldid=792454>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Transmission_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Transmission](<https://www.transmissionbt.com/>) 是一个轻量级、跨平台的 BitTorrent 客户端。 

##  安装

有多种可选的软件包： 

  * [transmission-cli](<https://archlinux.org/packages/?name=transmission-cli>)包 \- 包括命令行工具、守护程序和 [#Web 界面](<#Web_%E7%95%8C%E9%9D%A2>)。
  * [transmission-gtk](<https://archlinux.org/packages/?name=transmission-gtk>)包 \- [GTK](<../zh-cn/GTK.html> "GTK")\+ 4 图形界面。
  * [transmission-qt](<https://archlinux.org/packages/?name=transmission-qt>)包 \- [Qt](<../zh-cn/Qt.html> "Qt") 6 图形界面。
  * [tremc](<https://aur.archlinux.org/packages/tremc/>)AUR 或 [tremc-git](<https://aur.archlinux.org/packages/tremc-git/>)AUR \- 用于守护程序的 Curses 界面。
  * [stig](<https://aur.archlinux.org/packages/stig/>)AUR 或 [stig-git](<https://aur.archlinux.org/packages/stig-git/>)AUR – 用于守护程序的 Curses 界面。
  * [transmission-remote-gtk](<https://archlinux.org/packages/?name=transmission-remote-gtk>)包 – 用于守护程序的 GTK+ 3 界面。

##  图形界面的配置

两种带 GUI 的版本 _transmission-gtk_ 和 _transmission-qt_ 都可以在没有后端守护程序的情况下独立运行。 

GUI 版本都被配置为开箱即用，但用户可能仍需要更改一些设置。GUI 配置文件的默认路径是 `~/.config/transmission`。 

在 Transmission 的 Github 上，有一份各种选项如何配置的教程： [https://github.com/transmission/transmission/blob/main/docs/Editing-Configuration-Files.md](<https://github.com/transmission/transmission/blob/main/docs/Editing-Configuration-Files.md>). 

##  Transmission 守护程序和命令行

_transmission-cli_ 支持的命令包括： 

     _transmission-daemon_ : 启动守护程序。
     _transmission-remote_ : 调用本地或远程守护程序的[命令行界面](<https://en.wikipedia.org/wiki/Command-line_interface> "wikipedia:Command-line interface")，后面跟着希望守护程序运行的命令。
     _transmission-show_ : 返回指定种子文件的信息。
     _transmission-create_ : 创建一个新的种子文件。
     _transmission-edit_ : 新增、删除或替换一个 tracker 服务器的 announce URL。
     _transmission-cli_ : ([已弃用](<https://github.com/transmission/transmission/commit/950387ab5a443629598f93c057f41150707866ab>)) 启动一个非守护程序的本地 _transmission_ 实例，用于手动下载一个种子。
     _tremc_ : (需要 [tremc-git](<https://aur.archlinux.org/packages/tremc-git/>)AUR) 为本地或远程守护程序启动一个 [curses](<https://en.wikipedia.org/wiki/curses_\(programming_library\)> "wikipedia:curses \(programming library\)") 界面。

###  守护程序的启动与停止

就像 [#选择一个用户](<#%E9%80%89%E6%8B%A9%E4%B8%80%E4%B8%AA%E7%94%A8%E6%88%B7>)里面的说明那样，transmission 的守护程序可以按以下方式运行： 

  * 作为 _transmission_ 用户运行，只要[用 systemd](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd") start/enable `transmission.service` 服务即可。

    你可以按照 [#选择一个用户](<#%E9%80%89%E6%8B%A9%E4%B8%80%E4%B8%AA%E7%94%A8%E6%88%B7>)里的说明更改默认用户。

  * 用你自己的账户，只要在账户下运行：
        
        $ transmission-daemon

启动守护程序将会创建一个初始的 _transmission_ 配置文件。详情参阅 [#配置守护程序](<#%E9%85%8D%E7%BD%AE%E5%AE%88%E6%8A%A4%E7%A8%8B%E5%BA%8F>)。 

守护程序可以这样来停止：
    
    $ pkill -3 transmission-daemon

另一种停止 transmission 的方法是使用 _transmission-remote_ 命令： 
    
    $ transmission-remote --exit
    
###  减少多余的日志

运行 transmission-daemon 可能会产生许多不需要的日志条目。只要用一个小脚本包装一下再启动就可以过滤日志输出。以下示例可以提供一些启发： 
    
    transwrap.sh
    
    #!/bin/zsh
    killall transmission-daemon 2> /dev/null
    transmission-daemon --foreground --log-info 2>&1 | while read line; do
    	echo $line |
    		grep -v "announcer.c:\|platform.c:\|announce done (tr-dht.c:" |
    		grep -v "Saved.*variant.c:" |
    		while read line; do
    			echo $line | grep -q "Queued for verification (verify.c:" &&
    				notify-send --app-name="Transmission Started" "${line#* * }"
    			echo $line | grep -q "changed from .Incomplete. to .Complete." &&
    				notify-send --app-name="Transmission Complete" "${line#* * }"
    			echo $line | systemd-cat --identifier="TransWrap" --priority=5
    		done 2>&1 > /dev/null
    	done&disown
    
###  仅当连接到网络时运行

#### Netctl

你可能只想在连接某些网络时运行 transmission。下面的脚本会先检查连接是否在授权的网络列表中，是的话再继续启动 transmission-daemon。 
    
    /etc/netctl/hooks/90-transmission.sh
    
    #!/bin/bash
    
    # The SSIDs for which we enable this.
    declare -A ssids=(
        ["network_1"]=y
        ["network_2"]=y
    )
    
    if [[ ${ssids[$SSID]} ]]; then
        case $ACTION in
            CONNECT|REESTABLISHED)
                # Need to wait, otherwise doesn't seem to bind to 9091.
                sleep 30
                systemctl start transmission
                ;;
            *)
                systemctl stop transmission
                ;;
        esac
    fi
    
####  选择一个用户

选择你想如何运行 `transmission`： 

  * 作为独立用户运行，默认用户是 `transmission`（推荐，因为安全性更高）。

默认情况下， _transmission_ 会创建名为 `transmission` 的用户和组（它的主目录的文件位于 `/var/lib/transmission/`），并且用这个“账户”运行。这是一种安全措施，因为这样 _transmission_ 及其下载的文件将无法访问 `/var/lib/transmission/` 目录之外的文件。配置、操作和访问下载的文件需要使用 “root” 权限完成（比如用 [sudo](<../zh-cn/Sudo.html> "Sudo")）。 

  * 在你自己的账户下运行。设置这种方式需要[重写](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")已提供的服务文件并在其中指定你的用户名：

    /etc/systemd/system/transmission.service.d/username.conf
    
    [Service]
    User=_your_username_

###  配置守护程序

[启动守护程序](<#%E5%AE%88%E6%8A%A4%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%90%AF%E5%8A%A8%E4%B8%8E%E5%81%9C%E6%AD%A2>)来创建缺省的配置文件。 

  * 如果用 `transmission` 这个用户来运行 Transmission，配置文件会存放在 `/var/lib/transmission/.config/transmission-daemon/settings.json`。

  * 如果用你自己的账户运行 Transmission，配置文件会存放在 `~/.config/transmission-daemon/settings.json`。

使用一个 Transmission 客户端或者用自带的 web 界面（在支持的浏览器中用 <http://localhost:9091> 来访问）可以自定义守护程序。 

在 Transmission 的网站上，有一份各种选项如何配置的教程：[https://github.com/transmission/transmission/blob/main/docs/Editing-Configuration-Files.md](<https://github.com/transmission/transmission/blob/main/docs/Editing-Configuration-Files.md>)

**注意：**

  * 如果你想用一个文本编辑器手动编辑配置文件，请先 [停止守护程序](<#%E5%AE%88%E6%8A%A4%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%90%AF%E5%8A%A8%E4%B8%8E%E5%81%9C%E6%AD%A2>)；否则当它停止时将会覆盖配置文件。
  * 另一种方式是，可以用 SIGHUP 信号指示守护程序重新加载其配置，运行 `kill -s SIGHUP `pidof transmission-daemon`` 即可。

一个给那些用 `transmission` 账户运行的用户的建议是，用适当的权限创建一个共享的下载目录，这样就能同时允许 `transmission` 账户和其他账户访问下载文件，也能相应地更新配置文件。例如： 
    
    # mkdir /mnt/data/torrents
    # chown -R facade:transmission /mnt/data/torrents
    # chmod -R 775 /mnt/data/torrents
    
现在 `/mnt/data/torrents` 目录可供系统账户 `facade` 和 `transmission` 用户所属的 `transmission` 组访问。非常不鼓励使这个目录可读写（即不要将目录 _chmod_ 到 _777_ ），而是应该将个别用户/组的部分权限授予部分目录。 

**注意：** 如果 `/mnt/data/torrents` 位于一个可移除的设备上，比如这是一个 `/etc/fstab` 条目且带有 `nofail` 选项，那么 Transmission 会报告说没有找到文件。要解决这个问题，可以在 `/etc/systemd/system/transmission.service.d/transmission.conf` 文件的 `[Unit]` 一节中加入 `RequiresMountsFor=/mnt/data/torrents`。

另一种方法是把你的账户加入 `transmission` 用户组 (`#usermod -a -G transmission yourusername`)，然后修改 `/var/lib/transmission` 和 `/var/lib/transmission/Downloads` 目录的权限设置，以允许 `transmission` 组成员对这两个目录的 `rwx` 访问权。 

####  Host 白名单

如果你想用远程主机的主机名来访问位于该主机上的 Transmission 守护程序，你需要把主机名加入 `settings.json` 文件中的 `rpc-host-whitelist` 字段中。 否则你会在连接主机时收到一条 "421 Misdirected Request" 错误。 

如果你用该服务器的 IP 地址来访问守护程序，这一步可以省略。 

####  监视目录

如果你想 _自动添加某个文件夹中的 .torrent 文件_ ，但是配置文件中的 `watch-dir` 和 `watch-dir-enabled` 选项都不起作用，可以带 `-c /path/to/watch/dir` 参数启动 transmission 守护程序。 

如果你在用 systemd，按照 [systemd#修改现存单元文件](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")里面的描述编辑 `transmission.service` 单元文件。 

####  启用 IPv6

默认情况下，守护程序仅监听 IPv4 连接。要同时监听 IPv6 连接，把 `settings.json` 里的 `rpc-bind-address` 选项改为 `"::"`。 

####  CLI 使用示范

如果你想删除所有已完成的种子，可以用下面的命令（用你自己的用户名和密码）： 
    
    # transmission-remote -n 'username:password' -l | grep 100% | awk '{print $1}'| paste -d, -s | xargs -i transmission-remote -t {} -r
    
为已下载的文件做种： 
    
    # transmission-remote [HOST] --torrent=example.torrent -a example.torrent --verify --download-dir=/dir/to/folder --start
    
##  通知

停止 transmission-daemon 并在`.config/transmission-daemon/settings.json` 中添加以下内容： 
    
       "script-torrent-added-enabled": true,
       "script-torrent-added-filename": "path/to/transmission-handler.sh",
       "script-torrent-done-enabled": true,
       "script-torrent-done-filename": "path/to/transmission-handler.sh",
    
    transmission-handler.sh
    
    #!/bin/bash
    
    percentage=$(transmission-remote -t $TR_TORRENT_ID -l | awk -v ID="$TR_TORRENT_ID" '$0 ~ ID{print $2}')
    
    if [ $percentage != "100%" ]
    then
         notify-send --app-name="Transmission Started" "Transmission: started $TR_TORRENT_NAME"
    else
         notify-send --app-name="Transmission Complete" "Transmission: downloaded $TR_TORRENT_NAME"
    fi
    
##  Web 界面

###  GUI 方式

当 Transmission 安装完毕后就可以轻易架起 web 界面。你只需要单击 _edit_ 菜单，选择 _preferences_ 。单击 _Remote_ 选项卡并启用 _Allow remote access_ 。 

此处你可以修改默认的监听端口 9091。 

单击 _Use authentication_ 并填写用户名和密码就可以启用身份认证。 

要提高安全性，可以启用 _**Only allow these IP addresses**_ 限制来自任意 IP 的访问。 

现在你可以单击 _Open web client_ （用你的默认浏览器打开）或手动访问 `http://_TARGET_IP_ADDRESS_ :_PORT_` 来启动 web 界面。 

如果没有修改监听端口，默认是 9091。在这种情况下访问链接是 `<http://localhost:9091>`。 

**注意：** 记住，必须安装 [transmission-cli](<https://archlinux.org/packages/?name=transmission-cli>)包。

###  CLI 方式

设置 web 界面甚至不需要借助图形界面，因为守护程序提供了类似的选项。你无需指定任何参数即可访问 web 界面，可参阅 [#守护程序的启动与停止](<#%E5%AE%88%E6%8A%A4%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%90%AF%E5%8A%A8%E4%B8%8E%E5%81%9C%E6%AD%A2>)。 

不过，你仍然可以指定在前一节中看到的所有选项： 
    
    $ transmission-daemon --auth --username arch --password linux --port 9091 --allowed "127.0.0.1"

等同于 
    
    $ transmission-daemon -t -u arch -v linux -p 9091 -a "127.0.0.1"

**注意：** 如果你设置了用户名和密码，那么所有后续对`transmission-remote`的命令都需要使用`--auth username:password`进行身份验证。请参阅：[transmission-remote commands are erroring with Unauthorized user](<https://stackoverflow.com/a/29712044>)

###  可选的网页 UI 主题

如果觉得 web app 的默认用户界面过时、不好看，试试这个简单CSS主题： <https://git.eigenlab.org/sbiego/transmission-web-soft-theme>

另一个完整替代方案，可以和默认界面共存： <https://github.com/ronggang/transmission-web-control>

##  作为makepkg DLAGENT的用法

Transmission可以连同[transmission-dlagent](<https://aur.archlinux.org/packages/transmission-dlagent/>)AUR下载代理一起，作为[makepkg](<../zh-cn/Makepkg.html> "Makepkg")的磁链下载代理。 

磁链URI需要将其前缀从`magnet:?`更改为`<magnet://>`。 

##  故障排除

###  无法使用网络连接至守护程序

在 `network.service` 初始化后守护程序就会开始运行。但是，如果启用了 `dhcpcd` 服务而不是特定设备的服务（比如 `dhcpcd@enp1s0.service`），可能 Transmission 会因为启动过早而无法绑定到相应的网络接口。于是 web 界面无法访问。一种可能的解决方案是在 systemd 单元的[配置文件](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")里增加 `Requires` 行。 
    
    /etc/systemd/system/transmission.service.d/fixdep.conf
    
    [Unit]
    Requires=network.target

###  无法显示 Web 界面
    
    404: Not Found
    
    Couldn't find Transmission's web interface files!
    
    Users: to tell Transmission where to look, set the TRANSMISSION_WEB_HOME environment variable to the folder where the web interface's index.html is located.
    
    Package Builders: to set a custom default at compile time, #define PACKAGE_DATA_DIR in libtransmission/platform.c or tweak tr_getClutchDir () by hand.

即使你用图形界面，也需要安装 [transmission-cli](<https://archlinux.org/packages/?name=transmission-cli>)包 来支持 web 界面。 

###  接收/发送缓冲区设置失败

在启动时 Transmission 可能会在日志中显示如下的消息： 
    
    UDP Failed to set receive buffer: requested 4194304, got 425984
    UDP Failed to set send buffer: requested 1048576, got 425984
    
通过使用[sysctl](<../zh-cn/Sysctl.html> "Sysctl")设置 `net.core.rmem_max=4194304` 和 `net.core.wmem_max=1048576` 可以解决。 

###  transmission-remote频繁超时或网络界面无响应

Transmission并未异步处理磁盘IO，因此在进行大量写入时，可能会变得无响应，详情参见[[1]](<https://github.com/transmission/transmission/issues/2462>)。建议将Transmission的下载目录放在更快的存储设备上，如SSD而非HDD。 

###  transmission-gtk缺少托盘图标

GTK 4版本的托盘图标[目前无法工作](<https://github.com/transmission/transmission/discussions/5065>)。有一个选择是使用GTK 3版本的[transmission-gtk3](<https://aur.archlinux.org/packages/transmission-gtk3/>)AUR。 

###  401: 未授权

在为web界面设置用户名和密码后，使用`transmission-remote`时可能会出现以下错误：
    
    < h1>401: Unauthorized\Unauthorized User

这种情况是因为设置了用户名和密码。此后，所有来自`transmission-remote`的命令都必须经过身份验证。详情参见：[transmission-remote命令因未授权的用户而出错](<https://stackoverflow.com/a/29712044>)

##  更多信息

  * [Transmission wiki (old)](<https://trac.transmissionbt.com/wiki>)
  * [Transmission documentation on GitHub](<https://github.com/transmission/transmission/blob/main/docs/README.md>)
  * [Headless Usage](<https://github.com/transmission/transmission/blob/main/docs/Headless-Usage.md>)
