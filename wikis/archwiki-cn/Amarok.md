**翻译状态：**

  * 本文（或部分内容）译自 [Amarok](<https://wiki.archlinux.org/title/Amarok> "arch:Amarok")，最近一次同步于 2022-08-09，若英文版本有所[更改](<https://wiki.archlinux.org/title/Amarok?diff=0&oldid=713221>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Amarok_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Amarok](<https://amarok.kde.org/>) 是一个有着直观的 [Qt](<../zh-cn/Qt.html> "Qt") 界面且适用于 Linux 的音乐播放器和管理工具,它与 [KDE](<../zh-cn/KDE.html> "KDE") 集成得很好。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [amarok](<https://aur.archlinux.org/packages/amarok/>)AUR 软件包。 

Amarok 现在依赖于 Phonon ,所以你必须为其选择一个工作后端。请见 [KDE#Phonon](<../zh-cn/KDE.html#Phonon> "KDE") 。你也许还需要为选择的后端安装一些[编解码器](<../zh-cn/Codecs_and_containers.html> "Codecs and containers")。 

##  定制

###  与 GNOME 集成

请见[统一 Qt 和 GTK 应用的外观](<../zh-cn/Uniform_look_for_Qt_and_GTK_applications.html> "Uniform look for Qt and GTK applications")来获得主要 GUI 的外观集成。 

###  脚本与系统托盘

新的脚本和系统托盘可以直接在 Amarok (_工具 > 脚本管理 > 获取更多脚本_) 中找到或在 [store.kde.org](<https://store.kde.org/browse/cat/>) 找到。 

### Moodbar

Moodbar 是一个能将基本的进度条转换为取决于音轨旋律被划分成多个色块的进度条的功能。 

安装 [moodbar](<https://aur.archlinux.org/packages/moodbar/>)AUR. 

然后前往 _设置 > 配置 Amarok_ 勾选 "在进度中显示 moodbar"。 

因为 Amarok 2 **不会** 生成 moodfile ,你可以根据[这篇教程](<https://userbase.kde.org/Amarok/Manual/Various/Moodbar#Moodbar_File_Generation_Script>)自己创造这些文件。 

## SHOUTcast

要想获取 SHOUTcast 使用 "SHOUTcast 服务" 脚本。启动 Amarok,前往 _工具 > 脚本管理 > 获取更多脚本_,搜索 _SHOUTcast_ 安装 _Shoutcast 服务_ ,重启 Amarok。然后你可以在 "互联网" 菜单中找到它。 

另见: [如何使用 Amarok 流式传输到我自己的广播电台?](<https://userbase.kde.org/Amarok/Manual/Various/FAQ/en#How_can_I_use_Amarok_to_stream_to_my_own_radio_station.3F>),这篇文章推荐使用 [Internet DJ Console](<http://idjc.sourceforge.net/>),在AUR([idjc](<https://aur.archlinux.org/packages/idjc/>)AUR)中可用。 

##  Ampache/MP3 流式传输

如果你正在直接或使用 Ampache 插件流式传输 MP3,并且你正用着 [GStreamer](<../zh-cn/GStreamer.html> "GStreamer") 后端,你就无法在查看音轨。安装需要的包:[phonon-qt4-gstreamer](<https://aur.archlinux.org/packages/phonon-qt4-gstreamer/>)AUR [phonon-qt5-gstreamer](<https://archlinux.org/packages/?name=phonon-qt5-gstreamer>)包 [gst-libav](<https://archlinux.org/packages/?name=gst-libav>)包。 然后前往 Amarok 的 _设置 > 配置 Amarok > 回放 > 配置 Phonon>_ 的 _后端_ 标签页。将 Gstreamer 设置为首选后端。 

##  收藏集数据库

Amarok 2.x 可以使用 Sqlite (默认) 或 MySQL 储存收藏集数据库。有着大量收藏集的用户和有着更高的性能表现要求的用户可能更想使用 MySQL。 

### MySQL

对于基础的 MySQL 配置,请参考 [MariaDB](<../zh-cn/MariaDB.html> "MariaDB") 页面。 

当 Amarok 使用 MySQL 时,你需要创建一个可以访问数据库的 MySQL 用户。要想实现,输入下列命令: 
    
    # mysql -p -u root
    # CREATE DATABASE amarokdb;
    # USE amarokdb;
    # GRANT ALL ON amarokdb.* TO amarokuser@localhost IDENTIFIED BY 'password-user';
    # FLUSH PRIVILEGES;
    # quit
    
这会创建一个名为 'amarokdb' 的数据库和一个名为 'amarokuser' ,有着密码 'password-user',可以从本地主机访问所述数据库的用户。如果你想从另一台电脑连接到你的数据库电脑,将命令更改为: 
    
    # GRANT ALL ON amarok.* TO amarokuser@'%' IDENTIFIED BY  'password-user';
    
要想将 Amarok 配置为使用 MySQL,进入 Amarok 配置界面,选择数据库并勾选 "使用外部 MySQL 数据库"。输入服务器(如果是本机数据库通常为 "localhost",否则输入远程主机的名字),用户名(在这个例子中是 "amarokuser" )和你选择的密码用户。不要忘记选择你的音乐收藏集的路径。 

##  音频 CD 回放

如果你没有使用 KDE 桌面环境, Amarok 可能缺少需要的工具来播放音频 CD 。[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [audiocd-kio](<https://archlinux.org/packages/?name=audiocd-kio>)包 来获取这个功能。 

##  Firefly/Daap 共享

要想让 Daap 共享在 Amarok 中可见,在 Amarok 设置中启用 "DAAP 收藏集" 插件。 

安装 [nss-mdns](<https://archlinux.org/packages/?name=nss-mdns>)包 并且在 `/etc` 像这样填写主机名: 
    
    hosts: files mdns4_minimal [NOTFOUND=return] nis dns mdns4
    
[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `avahi-daemon.service`. 

##  另见

[应用列表#音频播放器](<../zh-cn/List_of_applications.html#Audio_players> "List of applications")
