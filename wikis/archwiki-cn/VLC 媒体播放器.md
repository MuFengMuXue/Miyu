**翻译状态：**

  * 本文（或部分内容）译自 [VLC media player](<https://wiki.archlinux.org/title/VLC_media_player> "arch:VLC media player")，最近一次同步于 2025-09-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/VLC_media_player?diff=0&oldid=844699>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/VLC_media_player_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

引自[项目主页](<https://www.videolan.org/vlc/>)： 

    VLC 是一款自由、开源的跨平台多媒体播放器及框架，可播放大多数多媒体文件，以及 DVD、音频 CD、VCD 及各类流媒体协议。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [vlc](<https://archlinux.org/packages/?name=vlc>)包 [拆分包](<../zh-cn/PKGBUILD.html#pkgbase> "拆分包")，该软件包依赖于尽可能少的 VLC 插件。附加功能请参见其可选依赖。 

主要的变体有： 

  * [vlc-git](<https://aur.archlinux.org/packages/vlc-git/>)AUR⸺开发分支版本。
  * [vlc-nox](<https://aur.archlinux.org/packages/vlc-nox/>)AUR⸺移除 GUI 界面的版本。

###  可选依赖

某些媒体格式需要安装额外插件支持。可以首先尝试安装 [vlc-plugin-ffmpeg](<https://archlinux.org/packages/?name=vlc-plugin-ffmpeg>)包。在某些情况下，可能需要安装 [vlc-plugins-all](<https://archlinux.org/packages/?name=vlc-plugins-all>)包。 

##  语言

VLC 没有在其“偏好设置”中提供更改语言的选项，但可通过通过修改[`LANGUAGE` 环境变量](<../zh-cn/Locale.html#LANGUAGE%EF%BC%9A%E5%90%8E%E5%A4%87%E5%8C%BA%E5%9F%9F%E8%AE%BE%E7%BD%AE> "Locale")改变其界面语言。例如，可以把其[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项") `vlc.desktop` 中这一部分： 
    
    Exec=/usr/bin/vlc %U
    
修改为： 
    
    Exec=env LANGUAGE=_zh_CN_ /usr/bin/vlc %U
    
来将界面语言设置为中文（中国）。 

##  皮肤

VLC 支持“皮肤”功能，可更换外观和风格。可以在 [VLC 皮肤网站](<https://www.videolan.org/vlc/skins.php>)下载皮肤。 

要安装皮肤，下载后将其移动到 `~/.local/share/vlc/skins2/`。 

打开 VLC，点击菜单栏中**“工具 > 偏好设置”**。“简明”显示下，皮肤设置位于“界面”选项卡。 

选择“使用自定义皮肤”，然后选择已下载的皮肤资源文件。 

重启 VLC 以使更改生效。 

##  Web 界面

使用参数 `--extraintf=http` 运行 VLC 可同时开启桌面界面和 Web 界面。参数 `--http-host` 用于指定绑定地址，默认是 `localhost`。必须使用 `--http-password` 设置密码，否则 VLC 不允许登录。 
    
    $ vlc --extraintf=http --http-host 0.0.0.0 --http-port 8080 --http-password _密码_
    
在图形界面中，可以通过点击菜单栏中**“视图 > 添加界面 > Web”**启动 Web 界面。通过**“工具 > 偏好设置（显示设置为‘全部’）> 界面 > 主界面 > Lua > Lua HTTP > 密码”**设置密码。登录时用户名留空。 

VLC 默认使用端口 `8080`：<http://localhost:8080>

##  提示与技巧

###  使用 VLC 观看直播

可以使用 [Streamlink](<../zh-cn/Streamlink.html> "Streamlink") 通过 VLC 观看直播。 

###  从本地 DLNA 服务器播放流媒体内容

安装 [vlc-plugin-upnp](<https://archlinux.org/packages/?name=vlc-plugin-upnp>)包 后，通过进入**“视图 > 播放列表 > 本地网络 > 通用即插即播（UPnP）”**可以播放 UPnP DLNA 内容。如果 VLC 无法检测到本地网络中的 DLNA 服务器，请确保防火墙未阻止 UPnP 使用的 UDP 1900 端口，只有开放这一端口才能播放本地 DLNA（使用 UPnP）内容。 

###  使用快捷键或命令行控制

安装 [openbsd-netcat](<https://archlinux.org/packages/?name=openbsd-netcat>)包。 

从 [CrunchBang 论坛的存档界面](<https://web.archive.org/web/20150209150507/http://crunchbang.org/forums/viewtopic.php?pid=112035>)获取脚本。 

按照脚本中的说明为 VLC 设置一个 socket。 

可以从命令行运行该脚本，或者通过桌面环境将其注册为键盘快捷键。 

另外，你也可以使用 [MPRIS](<../zh-cn/MPRIS.html> "MPRIS") 与 VLC 交互。 

也可以使用 ncurses 界面启动 VLC： 
    
    $ vlc -I ncurses
    
详见[官方文档](<https://wiki.videolan.org/Documentation:Modules/ncurses/>)。 

###  保持单实例运行

VLC 的默认设置是每次打开文件就启动一个新的程序实例。如果使用 VLC 来播放音乐收藏之类的内容，这可能会很烦人。可以在文件管理器中多选文件后一起打开，也在菜单中可以关闭此行为：勾选**“工具 > 偏好设置（显示设置为‘简明’）> 界面 > 播放列表与实例管理 > 仅允许一个实例”**，并勾选**“在单实例模式中将项目添加到播放列表队列中”** ，这样新的文件将被添加到当前播放列表中而不会中断当前播放的文件。 

还有一个选项**“从文件管理器启动时，只允许一个实例”** 勾选后，通过文件管理器用 VLC 打开的文件都会在一个实例中播放。**“在单实例模式中将项目添加到播放列表队列中”** 选项对此仍然生效。 

**注意：** 当前 VLC 版本存在以下 [bug](<https://code.videolan.org/videolan/vlc/-/issues/28077>)：勾选**“从文件管理器启动时，只允许一个实例”** 而不勾选**“仅允许一个实例”** 时无法（取消）勾选**“在单实例模式中将项目添加到播放列表队列中”** 选项。

###  硬件视频加速

详见[硬件视频加速](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "硬件视频加速")。 

VLC 会自动尝试使用可用的 API，但也可以手动覆盖设置。在菜单栏中进入：**工具 > 偏好设置（显示设置为“简明”）> 输入/编解码器**，在“硬件加速解码”中选择合适的选项。 

###  systemd 服务

可以通过 [systemd](<../zh-cn/Systemd.html> "Systemd") 自启动 VLC 的 [#Web 界面](<#Web_%E7%95%8C%E9%9D%A2>)。首先，创建一个专用用户： 
    
    # useradd -c "VLC daemon" -d / -G audio -M -p \! -r -s /usr/bin/nologin -U vlcd
    
接着创建 systemd 服务文件： 
    
    /etc/systemd/system/vlc.service
    
    [Unit]
    Description=VideoOnLAN Service
    After=network.target
    
    [Service]
    Type=forking
    User=vlcd
    ExecStart=/usr/bin/vlc --daemon --syslog -I http --http-port 8090 --http-password _密码_
    Restart=on-abort
    
    [Install]
    WantedBy=multi-user.target
    
[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `vlc.service`。登录时用户名留空，密码为以上服务文件中所设。 

###  Chromecast 支持

从 3.0 版本（Vetinari 分支）开始，VLC 可以向同一网络中的 Chromecast 设备进行流媒体投放。 

安装以下软件包： 

  * [libmicrodns](<https://archlinux.org/packages/?name=libmicrodns>)包⸺使 VLC 能发现 Chromecast 设备，并在菜单 “播放 > 渲染器” 中显示。
  * [protobuf](<https://archlinux.org/packages/?name=protobuf>)包⸺使 VLC 能通过“播放 > 渲染器”菜单将内容投放到选定设备。

然后，编辑文件 `/etc/nsswitch.conf`，在 `hosts` 这一行的 `resolve` 和 `dns` 之前加入 `mdns_minimal [NOTFOUND=return]`： 
    
    hosts: ... **mdns_minimal [NOTFOUND=return]** resolve [!UNAVAIL=return] dns ...
    
**注意：**

  * 如果解析 `_主机名_.local` 速度较慢，可以尝试将 `mdns_minimal` 替换为 `mdns4_minimal`，仅解析 IPv4 地址。
  * 更多信息请参阅 [avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）")（英语：[avahi](<https://wiki.archlinux.org/title/avahi> "en:avahi")）。

###  单击自动暂停/恢复插件

安装 [vlc-pause-click-plugin](<https://aur.archlinux.org/packages/vlc-pause-click-plugin/>)AUR，该插件实现了许多人习惯的在直接点击 VLC 播放窗口中的视频时暂停或恢复播放的功能。 

安装后插件不会自动启用，需要按照 <https://github.com/nurupo/vlc-pause-click-plugin#usage> 的说明在设置里手动启用。 

##  问题解决

###  更新后视频异常或其他问题

VLC 的配置在更新时常常会出现问题，即使是小版本更新。在提交错误报告之前，请先删除或重命名位于 `~/.config/vlc` 的配置文件，并确认问题是否仍然存在。 

如果使用了 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中的 [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg") 变种，请确保它也已更新。Pacman 不会自动升级这些包，而版本不匹配可能会导致 VLC 出现故障。 

###  段错误

####  启动 VLC 时出现

在启动 VLC 时，可能会遇到段错误。如果已经排除了诸如[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "微码")等常见因素，可以尝试重新生成 VLC 的插件缓存并重装 VLC，执行： 
    
    # /usr/lib/vlc/vlc-cache-gen /usr/lib/vlc/plugins
    
然后重新安装 VLC。 

####  播放视频时出现

如果 VLC 能正常播放音频文件，但在播放视频时出现段错误，那么可能是[硬件视频加速](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "硬件视频加速")配置不当，导致 VLC 无法访问图形设备。这种情况尤其容易发生在一台电脑使用多个显卡时。 

###  下拉菜单中图标缺失

在 XFCE 桌面环境下，下拉菜单中图标（如 PCI 卡图标）可能会缺失。 

执行以下命令可以重新启用这些图标： 
    
    $ gconftool-2 --type boolean --set /desktop/gnome/interface/buttons_have_icons true
    $ gconftool-2 --type boolean --set /desktop/gnome/interface/menus_have_icons true
    
###  打开 VDPAU 后端失败

参见[硬件视频加速#打开 VDPAU 后端失败](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html#%E6%89%93%E5%BC%80_VDPAU_%E5%90%8E%E7%AB%AF%E5%A4%B1%E8%B4%A5> "硬件视频加速")。 

由于系统可能并不支持 VDPAU，需要让 VLC 使用 VA-API 作为替代，请参见 [#硬件视频加速](<#%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F>)。 

###  无法通过 SFTP 播放媒体文件

如果 VLC 无法通过 SFTP 播放任何视频或音频文件，请确保已安装 [sshfs](<https://archlinux.org/packages/?name=sshfs>)包。 

如果 VLC 拒绝播放任何文件名包含空格的媒体文件而要求身份验证，请修改 `vlc.desktop` 文件中的 Exec 行如下： 
    
    Exec=/usr/bin/vlc --started-from-file %F
    
参见 [[1]](<https://bugs.launchpad.net/ubuntu/+source/vlc/+bug/239431/comments/11>)。 

###  iOS 或 tvOS 上的 VLC 无法通过 SFTP 连接到 Arch

由于 App Store 的许可限制，VLC 的 iOS 与 tvOS 应用使用的是不完整的 SSH 实现。为使其兼容，需修改 [openssh](<https://archlinux.org/packages/?name=openssh>)包 配置。创建配置文件 `/etc/ssh/sshd_config.d/vlc.conf`，内容如下： 
    
    HostKeyAlgorithms +ssh-rsa  
    KexAlgorithms +diffie-hellman-group16-sha512
    
然后运行以下命令重新加载配置： 
    
    systemctl reload sshd
    
###  无法打开 DVD

若希望通过菜单 “媒体 > 打开光盘” 播放 DVD，需安装 VLC 的可选依赖 [vlc-plugin-dvd](<https://archlinux.org/packages/?name=vlc-plugin-dvd>)包 及该插件的可选依赖 [libdvdcss](<https://archlinux.org/packages/?name=libdvdcss>)包（用于解码使用 [CSS](<https://zh.wikipedia.org/wiki/%E5%86%85%E5%AE%B9%E6%89%B0%E4%B9%B1%E7%B3%BB%E7%BB%9F> "zhwp:内容扰乱系统") 加密的 DVD）。 

部分 DVD 还可能需要其它插件，例如 [vlc-plugin-dca](<https://archlinux.org/packages/?name=vlc-plugin-dca>)包。也可以选择安装 [vlc-plugins-extra](<https://archlinux.org/packages/?name=vlc-plugins-extra>)包，该软件包包含上述两个插件及其他额外插件。 

如果已安装上述所有软件包仍无法播放 DVD，可尝试删除 `~/.dvdcss` 文件夹，让 VLC 会重新下载 CSS 密钥，有时可以解决播放问题。 

###  媒体无法加载

若某些 RTP、RTSP、DVB-T 流媒体或蓝光视频出现无限缓冲状态，或在日志中无报错却静默加载失败（例如法国 Free 互联网服务提供商的 IPTV 服务），请安装 [vlc-plugin-aribb24](<https://archlinux.org/packages/?name=vlc-plugin-aribb24>)包 插件。 

###  Wayland 支持

[vlc-git](<https://aur.archlinux.org/packages/vlc-git/>)AUR 默认编译时启用了 Wayland 支持。设置环境变量 `QT_QPA_PLATFORM=wayland` 可启用 Wayland，详见 [Wayland#Qt](<../zh-cn/Wayland.html#Qt> "Wayland")。 

需要注意的是，尽管 [vlc](<https://archlinux.org/packages/?name=vlc>)包 的 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 中使用了 `--enable-wayland` 编译参数（[当前使用的是 VLC 3.0 版本](<https://gitlab.archlinux.org/archlinux/packaging/packages/vlc/-/blob/main/PKGBUILD>)），但实际上仍会通过 [Xwayland](<../zh-cn/Wayland.html#Xwayland> "Xwayland") 运行，因为 VLC 3 的 Wayland 支持尚未完善。如果未安装 [xorg-xwayland](<https://archlinux.org/packages/?name=xorg-xwayland>)包，VLC 的视频输出可能出现裁切或其他异常。 

可使用以下命令让 VLC 3 使用 Wayland 启动： 
    
    $ env -u DISPLAY vlc
    
该命令的原理是：VLC 3 启动时会检查 `DISPLAY` 环境变量，若未设置则尝试使用 Wayland。不推荐在系统范围内移除 `DISPLAY`，因为一些旧应用程序仍依赖该变量。 

###  无法连接到 RTSP 流

如果连接 RTSP 流时出现 `failed to setup rtsp session` 错误，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [vlc-plugin-live555](<https://archlinux.org/packages/?name=vlc-plugin-live555>)包。 

###  通过 Streamlink 观看直播时花屏

请安装可选依赖 [vlc-plugin-aribb24](<https://archlinux.org/packages/?name=vlc-plugin-aribb24>)包。 

###  使用 AMDGPU 播放 HEVC 视频时系统无响应

在播放 HEVC（H265）编码的视频时，系统可能会完全冻结，无法进行任何操作（包括关机）。 

可以通过将**“工具 > 偏好设置（显示设置为“全部”）> 视频 > 输出模块 > OpenGL > Open GL/GLES hardware converter”**从“自动”更改为其他合适选项（例如“VDPAU OpenGL surface converter”或“VA-API OpenGL surface converter for Wayland”）来解决该问题。 

详见 <https://gitlab.freedesktop.org/drm/amd/-/issues/2113#note_1602599>

###  更改播放进度后声音短暂消失

将**“工具 > 偏好设置（显示设置为‘简明’）> 音频 > 输出模块”**设置为目前使用的音频服务器（对于 [PipeWire](<../zh-cn/PipeWire.html> "PipeWire")，需要安装 [vlc-plugin-pipewire](<https://aur.archlinux.org/packages/vlc-plugin-pipewire/>)AUR，否则只能使用兼容层）。 

###  VLC 不显示字幕和屏显信息（OSD）

即使解码字幕的插件已经安装，如果没有安装 [vlc-plugin-freetype](<https://archlinux.org/packages/?name=vlc-plugin-freetype>)包，字幕和屏显信息仍然不会显示（而且“消息”和控制台中也不会报错）。注意，该插件不包含在 [vlc-plugins-base](<https://archlinux.org/packages/?name=vlc-plugins-base>)包 中，但包含在 [vlc-plugins-extra](<https://archlinux.org/packages/?name=vlc-plugins-extra>)包 中。 

##  参见

  * [维基百科页面](<https://zh.wikipedia.org/wiki/VLC%E5%A4%9A%E5%AA%92%E4%BD%93%E6%92%AD%E6%94%BE%E5%99%A8> "zhwp:VLC多媒体播放器")
  * [应用程序列表/多媒体](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%A4%9A%E5%AA%92%E4%BD%93.html> "应用程序列表/多媒体")
  * [VLC 主页](<https://www.videolan.org/vlc/>)
  * [playerctl](<https://github.com/acrisci/playerctl>)：一个用于控制媒体播放器的命令行工具和库
  * [VideoLAN's Wiki：通过浏览器控制 VLC](<https://wiki.videolan.org/Control_VLC_via_a_browser>)（英文）
