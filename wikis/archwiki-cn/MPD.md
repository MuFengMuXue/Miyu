**翻译状态：**

  * 本文（或部分内容）译自 [Music_Player_Daemon](<https://wiki.archlinux.org/title/Music_Player_Daemon> "arch:Music Player Daemon")，最近一次同步于 2025-11-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Music_Player_Daemon?diff=0&oldid=852739>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Music_Player_Daemon_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [MPD/提示与技巧](<../zh-cn/MPD/%E6%8F%90%E7%A4%BA%E4%B8%8E%E6%8A%80%E5%B7%A7.html> "MPD/提示与技巧")
  * [MPD/故障排除](<../zh-cn/MPD/%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html> "MPD/故障排除")

**[MPD](<https://www.musicpd.org/>)** （Music Player Daemon，音乐播放器守护进程）是一个服务器-客户端架构的音频播放器。占用极少资源的同时有着播放音频、管理播放列表和音乐等功能。与它进行交互需要一个单独的[客户端](<#%E5%AE%A2%E6%88%B7%E7%AB%AF>)。 

使用 Python 编写的 [mopidy](<https://archlinux.org/packages/?name=mopidy>)包 是 MPD 的不完全替代品，它的优势在于提供了可直接播放互联网流媒体服务的插件，支持如 Spotify、SoundCloud 和 Google Play Music。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mpd](<https://archlinux.org/packages/?name=mpd>)包 软件包。 

##  配置

MPD 可以以 [#单用户配置](<#%E5%8D%95%E7%94%A8%E6%88%B7%E9%85%8D%E7%BD%AE>)、[#全系统范围配置](<#%E5%85%A8%E7%B3%BB%E7%BB%9F%E8%8C%83%E5%9B%B4%E9%85%8D%E7%BD%AE>)（即配置应用给所有用户）模式运行，也可以在 [#多 MPD 实例设置](<#%E5%A4%9A_MPD_%E5%AE%9E%E4%BE%8B%E8%AE%BE%E7%BD%AE>)下同时运行多个实例。也可以参考 [#多 MPD 实例设置](<#%E5%A4%9A_MPD_%E5%AE%9E%E4%BE%8B%E8%AE%BE%E7%BD%AE>)运行多个 MPD 实例。 

将 MPD 设置成哪种方式运行取决于使用它的方式：例如，单用户配置更容易设置，也可能更适合桌面系统环境。全系统范围配置则更适合多用户共享单个 MPD 实例的常在线音频服务器。 

为了让 MPD 能够播放音频，须要先设置好 [ALSA](<../zh-cn/ALSA.html> "ALSA") (可选 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio")、[PipeWire](<../zh-cn/PipeWire.html> "PipeWire"))，并让它们正常工作。下文的 [#配置音频](<#%E9%85%8D%E7%BD%AE%E9%9F%B3%E9%A2%91>)小节会说明 _ALSA_ 、 _PulseAudio_ 或者 _PipeWire_ 所需的参数。 

MPD 由 [mpd.conf(5)](<https://man.archlinux.org/man/mpd.conf.5>) 文件进行配置，运行方式不同（单用户或全系统范围），文件的位置也不同。简单来说，有以下两个常用位置： 

  1. `~/.config/mpd/mpd.conf`——单用户配置模式，这是第一个会搜索的位置，
  2. `/etc/mpd.conf`——全系统范围配置。

下面是常用的配置选项: 

  * `pid_file` \- MPD 存储进程 ID（PID）的文件
  * `db_file` \- 音乐数据库
  * `state_file` \- 记录 MPD 当前状态
  * `playlist_directory` \- 播放列表存储文件夹
  * `music_directory` \- MPD 在这个文件夹中扫描音乐
  * `sticker_file` \- 标签数据库

###  单用户配置

MPD 可配置为单用户使用。以普通用户运行它有几点好处： 

  * 在一个文件夹 `~/.config/mpd/` 下 （或任何其他在 `$HOME` 家目录下的文件夹）重新部署（管理）所有 MPD 配置文件。
  * 避免不可预见的文件夹和文件权限错误。

####  配置文件和目录的位置

单用户模式下，MPD 从 `$XDG_CONFIG_HOME/mpd/mpd.conf` 文件中读取配置。 此处假设 `$XDG_CONFIG_HOME` 与 `~/.config` 的[默认值](<https://specifications.freedesktop.org/basedir-spec/latest/>)相同。 

位于软件包内的 [MPD 配置示例](<https://raw.githubusercontent.com/MusicPlayerDaemon/MPD/master/doc/mpdconf.example>)提供了一个创建用户配置的良好案例，使用下面的命令复制该示例文件并创建用户配置： 
    
    $ mkdir -p ~/.config/mpd
    $ cp /usr/share/doc/mpd/mpdconf.example ~/.config/mpd/mpd.conf
    
将这个新创建的 `~/.config/mpd/` 目录用于存放配置文件与其他 MPD 相关的文件（如数据库和播放列表）是一个良好的做法。注意用户必须拥有该目录的读写权限。 

然后编辑配置文件，指定需要和可选的文件以及目录： 
    
    ~/.config/mpd/mpd.conf
    
    # 数据库的建议位置
    db_file            "~/.config/mpd/database"
    
    # 如果使用 systemd 运行 MPD，删除下面这一行，让日志直接写入 systemd。
    log_file           "syslog"
    
    # 音乐目录默认是 XDG 目录，取消注释下面这一行，可以修改并选择不同的目录
    #music_directory    "~/music"
    
    # 取消注释下面这一行，可在音乐目录下的文件变动时自动刷新数据库
    #auto_update "yes"
    
    # 取消注释下列内容以启用这些功能
    #playlist_directory "~/.config/mpd/playlists"
    #pid_file           "~/.config/mpd/pid"
    #state_file         "~/.local/state/mpd/state"
    #sticker_file       "~/.config/mpd/sticker.sql"
    
如果在配置文件中启用了播放列表，则必须创建好配置文件中指定的播放列表目录： 
    
    $ mkdir ~/.config/mpd/playlists
    
如果设置了 `state_file`，则必须创建指定的目录： 
    
    $ mkdir -p ~/.local/state/mpd
    
现在可以用下列命令启动 MPD（可手动指定一个可选的自定义配置文件位置）： 
    
    $ mpd _[config_file]_
    
MPD 需要扫描上述定义的 `music_directory` 目录，才能建立数据库文件。为完成这一任务，需要使用一个 MPD[#客户端](<#%E5%AE%A2%E6%88%B7%E7%AB%AF>)。例如，对于 _mpc_ ，执行命令是： 
    
    $ mpc update
    
或者，在配置文件中将 `auto_update` 选项设置为 `"yes"`，这样，当 `music_directory` 中的文件变动时就会自动刷新数据库。 

####  配置音频

使用 [ALSA](<../zh-cn/ALSA.html> "ALSA") 时，即使无特定设置，**自动检测** 默认设备的功能也应当是开箱即用的。若自动检测没有生效，请参考下面的 ALSA 音频输出定义语法进行配置。`name` 参数指定了一个音频输出的唯一名称。 

可用 `device`（可选）选项指示出 `aplay --list-pcm` 命令（由 [alsa-utils](<https://archlinux.org/packages/?name=alsa-utils>)包 软件包提供）所列出的实际设备。 
    
    ~/.config/mpd/mpd.conf
    
    audio_output {
            type          "alsa"
            name          "_ALSA sound card_ "
            # Optional
            #device        "_iec958:CARD=Intel,DEV=0_ "
            #mixer_control "PCM"
    }

使用 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 的用户需要进行以下的调整： 
    
    ~/.config/mpd/mpd.conf
    
    audio_output {
            type            "pulse"
            name            "_pulse audio_ "
    }

[PipeWire](<../zh-cn/PipeWire.html> "PipeWire") 的输出也可以配置： 
    
    ~/.config/mpd/mpd.conf
    
    audio_output {
            type            "pipewire"
            name            "_PipeWire Sound Server_ "
    }

**注意：** 未配置好 PulseAudio 或 PipeWire 的 audio_output 会导致音量控制无效。

####  监听 Unix domain socket

如果仅在本机使用 MPD，让 MPD 运行于 IPC socket（进程间通信套接字）上会比在 network stack（网络栈）上拥有更好的性能表现和安全性。 

使用变量或绝对路径为 bind_to_address 设置一个值，请勿使用相对路径。以下是示例： 
    
    ~/.config/mpd/mpd.conf
    
    bind_to_address "$XDG_RUNTIME_DIR/mpd/socket"

随后 export 环境变量 `MPD_HOST="$XDG_RUNTIME_DIR/mpd/socket"`。 

####  随 systemd 自启动

[mpd](<https://archlinux.org/packages/?name=mpd>)包 软件包提供了一个[用户服务](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")文件。该服务以用户身份启动，因此无需更改权限或是使用 MPD 配置文件中的 `user` 与 `group` 变量。 

[启动或启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `mpd.service` 用户单元（例如，使用 `--user` 标识）。 

**注意：** 默认的配置文件是 `~/.config/mpd/mpd.conf`，若要指定一个自定义配置文件的路径，请参考 [systemd#修改现存单元文件](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")。

####  在 tty 登录时自启动

要在登录时启动 MPD，请将以下的内容添加至 `~/.profile` 或其他的[自动启动文件](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "自动启动")中： 
    
    # 启动 MPD 守护进程（若其他的用户实例不存在）
    [ ! -s ~/.config/mpd/pid ] && mpd
    
####  脚本配置

[mpd-configure](<https://gitlab.com/sonida/mpd-configure>) 工具使用 ALSA 接口硬件地址（hw:x,y）创建针对 _[bit perfect audio playback](<https://mpd.readthedocs.io/en/stable/user.html#bit-perfect-playback>)_ 的 MPD 优化配置，无需任何重采样或转换。 

###  全系统范围配置

**注意：** 使用 PulseAudio 并且将 MPD 设置为全局配置的用户可能需要[一个小技巧](<../zh-cn/Music_Player_Daemon/%E6%8F%90%E7%A4%BA%E4%B8%8E%E6%8A%80%E5%B7%A7.html#%E6%9C%AC%E5%9C%B0%EF%BC%88%E5%A4%9A%E7%94%A8%E6%88%B7%EF%BC%89> "Music Player Daemon/提示与技巧")来作为自己的用户运行 MPD！

默认的 `/etc/mpd.conf` 将设置保存在 `/var/lib/mpd` 中，并分配给用户以及主要用户组 MPD。 

####  音乐目录

音乐目录需要通过 `/etc/mpd.conf` 文件中的 `music_directory` 参数来设置。 

MPD需要拥有**所有** 音乐收藏父目录的**执行权限** （`+x`）并且可以读包含音乐的目录，这经常与用户的音乐目录的默认设置冲突（通常是存放着音乐的 `~/Music` 目录）。 

有很多方法可以解决这个问题，下列的方法中应该有一个是最实用的： 

  * 改用[单用户配置模式](<#%E5%8D%95%E7%94%A8%E6%88%B7%E9%85%8D%E7%BD%AE>)
  * 将 mpd 用户添加到用户组，并授予用户目录的执行权限。按照下面的命令为 `mpd` 用户授予访问用户目录的权限：

    # gpasswd -a mpd _用户组名称_
    $ chmod 710 /home/_用户目录_
    
  * 采取以下方式将音乐集合放到不同的路径： 
    * 完全移动
    * 绑定挂载
    * 使用 [Btrfs#子卷](<../zh-cn/Btrfs.html#%E5%AD%90%E5%8D%B7> "Btrfs")（需要将这一永久改变写入 `/etc/fstab` ）。

MPD 配置必须仅包含一个目录，如果音乐集包含在多个目录下，请在 `/var/lib/mpd` 的主音乐目录下创建符号链接。记得为被链接的目录设置相应的权限。 

要排除更新的文件，请在父目录中创建一个名为 `.mpdignore` 的文件。文件中每一行所表示的文件都可以包含 shell 的通配符。在当前目录以及所有的子目录中匹配到的文件都会在后续更新中被排除在外。 

**注意：** MPD 能够读取一些归档压缩文件内的音乐文件，若这些归档压缩文件位于音乐目录中，MPD 会在更新时读取这些文件。tar 格式的文件不在读取范围内。

####  通过 systemd 启动

可以使用 [systemd](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd") 来控制 MPD 服务，即 `mpd.service`，第一次启动 MPD 时会花费一些时间，因为 MPD 会扫描音乐目录。 

安装一个客户端程序 ([ncmpc](<https://archlinux.org/packages/?name=ncmpc>)包 是一个轻便易用的客户端程序)，享受音乐吧！ 

#####  套接字启动

[mpd](<https://archlinux.org/packages/?name=mpd>)包 提供了一个 `mpd.socket` 单元。如果启用了 `mpd.socket`，但没有启用 `mpd.service`，systemd 不会立刻启动 MPD，而是会监听相应的套接字。当一个 MPD 客户端试图连接其中的套接字，systemd 将启动 `mpd.service`，然后透明地将端口的控制权交给 MPD 进程。 

如果希望监听不同的 UNIX 套接字或者网络端口（甚至是每个类型的多个套接字），或者完全不希望监听网络端口，请正确[编辑](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd") `mpd.socket` 单元**并且** 修改 `/etc/mpd.conf` 以匹配相应的配置（详情请参考 [mpd.conf(5)](<https://man.archlinux.org/man/mpd.conf.5>)）。 

####  用户 id 启动流程

**不要** 以 _root_ 身份运行 MPD。在配置中使用 `user` 选项可以让 MPD 在完成初始化后更改其用户 id。在以非特权用户启动 MPD 时**请勿使用** 该选项。 

下面列出的是 MPD 正常启动的步骤，用以描述何时 MPD 放弃超级用户权限，而使用配置中用户组的权限： 

  1. 以 _root_ 身份通过 systemd 启动 MPD 后，MPD 首先读取 `/etc/mpd.conf` 文件。
  2. 然后 MPD 读取配置中的 `user` 变量，从 _root_ 切换到该用户。
  3. 最后 MPD 读取配置中的其余设置内容，根据内容配置自己。在配置文件中，可以使用 `~` 指向用户的家目录，而非 root 的目录。

###  多 MPD 实例设置

####  在 Icecast 服务中运行

如果第二个 MPD （例如：通过网络使用 [Icecast](</wzh/index.php?title=Icecast&action=edit&redlink=1> "Icecast（页面不存在）")（英语：[Icecast](<https://wiki.archlinux.org/title/Icecast> "en:Icecast")） 输出来分享音乐）使用和上一个 MPD 相同的音乐和播放列表，只需要复制上一个的配置文件来创建一个新文件（例如：`/home/username/.mpd/config-icecast`），并且更改 `log_file`、`error_file`、`pid_file` 和 `state_file` 的参数（例如：`mpd-icecast.log`、`mpd-icecast.error` 等等）。使用相同的音乐目录路径和播放列表目录将确保第二个 MPD 和第一个 MPD 使用相同的音乐收藏。例如，在第一个 MPD 守护进程下创建和编辑播放列表也会影响第二个守护进程，因此不需要为第二个守护进程创建相同的播放列表。以相同的方式从上述 `~/.xinitrc` 调用第二个守护进程（需要确保使用不同的端口号，避免和第一个 MPD 守护进程冲突）。 

####  卫星模式设置

[#在 Icecast 服务中运行](<#%E5%9C%A8_Icecast_%E6%9C%8D%E5%8A%A1%E4%B8%AD%E8%BF%90%E8%A1%8C>)中所述方法能够使用，但当两个 MPD 实例写相同的数据库文件时，理论上可能导致数据库问题。MPD 有一种[卫星模式](<https://www.musicpd.org/doc/user/advanced_config.html#satellite>)，该模式下，一个实例可以从另一个已经运行的 MPD 实例上接收数据库。 

在 `config-icecast` 中添加以下代码，其中 `host` 和 `port` 表示主 MPD 服务的主机名和端口号： 
    
    database {
        plugin "proxy"
        host "localhost"
        port "6600"
    }
    
##  客户端

需要安装独立客户端才能控制 MPD。较为详细的客户端列表请查阅[这里](<https://www.musicpd.org/clients/>)。常用的有这些： 

###  命令行客户端

  * **mpc** — MPD 服务的命令行用户界面，由 C 语言编写而成。

     <https://www.musicpd.org/clients/mpc/> || [mpc](<https://archlinux.org/packages/?name=mpc>)包

###  终端客户端

  * **clerk** — 使用 [Rofi](<../zh-cn/Rofi.html> "Rofi") 的 MPD 客户端。

     <https://github.com/carnager/clerk> || [clerk-git](<https://aur.archlinux.org/packages/clerk-git/>)AUR

  * **gomp** — 受 ncmpcpp 启发而成的 MPD 客户端，内置音乐集封面视图功能和 LastFM 集成。

     <https://github.com/aditya-K2/gomp> || [gomp-git](<https://aur.archlinux.org/packages/gomp-git/>)AUR

  * **inori** — 一个有着折叠式音乐库视图和高效搜索功能的 MPD 客户端。

     <https://github.com/eshrh/inori> || [inori](<https://aur.archlinux.org/packages/inori/>)AUR

  * **mmtc** — 小型 MPD 终端客户端，精简但可定制性较强。

     <https://github.com/figsoda/mmtc> || [mmtc](<https://aur.archlinux.org/packages/mmtc/>)AUR

  * **ncmpc** — MPD 的 NCursers 客户端，由 C++ 编写而成。

     <https://www.musicpd.org/clients/ncmpc/> || [ncmpc](<https://archlinux.org/packages/?name=ncmpc>)包

  * **[ncmpcpp](<../zh-cn/Ncmpcpp.html> "Ncmpcpp")** — 与 _ncmpc_ 几乎完全相同的客户端，但是有一些用 C++ 写成的新功能（标签编辑器、搜索引擎）。

     <https://rybczak.net/ncmpcpp/> || [ncmpcpp](<https://archlinux.org/packages/?name=ncmpcpp>)包

  * **ncmpy** — 基于 Curses，用 Python 编写而成的 MPD 客户端。

     <https://repo.cykerway.com/ncmpy> || [ncmpy](<https://aur.archlinux.org/packages/ncmpy/>)AUR

  * **nncmpp** — 另一个 MPD 客户端。实际上是 Sonata 的简化 TUI 版本。

     <https://git.janouch.name/p/nncmpp/> || [nncmpp-git](<https://aur.archlinux.org/packages/nncmpp-git/>)AUR

  * **pms** — NCursers 客户端，由 Go 语言编写而成，有着较强的可定制性。

     <https://github.com/kimtore/pms> || [pmus-git](<https://aur.archlinux.org/packages/pmus-git/>)AUR

  * **rmpc** — 受 ncmpcpp 和 ranger 启发的 MPD 客户端，通过使用多种图形协议可支持专辑封面，同时支持自定义配置。

     <https://rmpc.mierak.dev/> || [rmpc](<https://archlinux.org/packages/?name=rmpc>)包

  * **vimpc** — 基于 Curses 的 MPD 客户端，有着类似 vi 的按键绑定。

     <https://github.com/boysetsfrog/vimpc> || [vimpc-git](<https://aur.archlinux.org/packages/vimpc-git/>)AUR

###  图形界面客户端

  * **Ario** — 一个功能非常丰富的 GTK3 界面的客户端，灵感来自于 [Rhythmbox](</wzh/index.php?title=Rhythmbox&action=edit&redlink=1> "Rhythmbox（页面不存在）")（英语：[Rhythmbox](<https://wiki.archlinux.org/title/Rhythmbox> "en:Rhythmbox")）。

     <https://ario-player.sourceforge.net/> || [ario](<https://archlinux.org/packages/?name=ario>)包

  * **Cantata** — Qt5 客户端，已停止维护，具有丰富的功能和可配置的界面。

     <https://github.com/CDrummond/cantata> || [cantata](<https://aur.archlinux.org/packages/cantata/>)AUR

  * **CoverGrid** — GTK3 界面客户端，专注于音乐专辑。

     <https://www.suruatoel.xyz/codes/mcg> || [mcg](<https://aur.archlinux.org/packages/mcg/>)AUR

  * **Euphonica** — Libadwaita MPD 客户端，有可视化、wikis 和歌词同步功能。

     <https://github.com/htkhiem/euphonica> || [euphonica-git](<https://aur.archlinux.org/packages/euphonica-git/>)AUR

  * **myMPD** — 独立小巧、功能强大的 MPD 客户端，基于 web 技术，移动端适配良好。

     <https://github.com/jcorporation/myMPD> || [mympd](<https://archlinux.org/packages/?name=mympd>)包

  * **Plattenalbum** — 小巧而现代化的 GTK4 界面客户端，用 Python 编写而成。

     <https://github.com/SoongNoonien/plattenalbum> || [plattenalbum](<https://aur.archlinux.org/packages/plattenalbum/>)AUR

  * **QMPDClient** — Qt5 界面的客户端。

     <https://bitcheese.net/QMPDClient/> || [qmpdclient](<https://aur.archlinux.org/packages/qmpdclient/>)AUR

  * **Quimup** — 简洁的 Qt5 图形前端，用 C++ 编写而成。

     <https://sourceforge.net/projects/quimup/> || [quimup](<https://aur.archlinux.org/packages/quimup/>)AUR

  * **RompЯ** — MPD 的网页客户端。

     <https://fatg3erman.github.io/RompR/> || [rompr](<https://aur.archlinux.org/packages/rompr/>)AUR

  * **SkyMPC** — 简洁的 Qt5 图形客户端。

     <https://github.com/soramimi/SkyMPC> || [skympc-git](<https://aur.archlinux.org/packages/skympc-git/>)AUR

  * **Sonata** — 一个用 Python 写的客户端，非常优雅。

     <https://www.nongnu.org/sonata/> || [sonata-git](<https://aur.archlinux.org/packages/sonata-git/>)AUR

  * **Xfce MPD Panel Plugin** — [Xfce](<../zh-cn/Xfce.html> "Xfce")4 面板的 MPD 插件。

     <https://goodies.xfce.org/projects/panel-plugins/xfce4-mpc-plugin> || [xfce4-mpc-plugin](<https://archlinux.org/packages/?name=xfce4-mpc-plugin>)包

  * **Xfmpc** — GTK 图形客户端，专注于低占用。

     <https://goodies.xfce.org/projects/applications/xfmpc> || [xfmpc](<https://archlinux.org/packages/?name=xfmpc>)包

  * **ympd** — 使用 Websockets 和 Bootstrap/JS 编写的独立 MPD 网络图形用户界面。

     <https://ympd.org/> || [ympd](<https://aur.archlinux.org/packages/ympd/>)AUR

  * **Ymuse** — 简单、实用且快捷的 GTK 前端（客户端），用 Go 语言编写而成。

     <https://yktoo.com/en/software/ymuse/> || [ymuse](<https://aur.archlinux.org/packages/ymuse/>)AUR

###  其他类型

  * **mpd-mpris** — MPD 的 [MPRIS](<../zh-cn/MPRIS.html> "MPRIS") 实现。

     <https://github.com/natsukagami/mpd-mpris> || [mpd-mpris](<https://archlinux.org/packages/?name=mpd-mpris>)包

  * **mpdris2-rs** — 为 MPD 提供 [MPRIS](<../zh-cn/MPRIS.html> "MPRIS") V2.2 D-Bus 接口。

     <https://github.com/szclsya/mpdris2-rs> || [mpdris2-rs](<https://aur.archlinux.org/packages/mpdris2-rs/>)AUR

##  另见

  * [MPD 论坛](<https://forum.musicpd.org/>)
  * [MPD 用户手册](<https://www.musicpd.org/doc/user/>)
  * [MPD 的相关维基百科文章](<https://en.wikipedia.org/wiki/Music_Player_Daemon> "wikipedia:Music Player Daemon")
  * [MPD 的相关 GitHub 仓库](<https://github.com/MusicPlayerDaemon/MPD>)
