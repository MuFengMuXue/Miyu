**翻译状态：**

  * 本文（或部分内容）译自 [Audacious](<https://wiki.archlinux.org/title/Audacious> "arch:Audacious")，最近一次同步于 2017-09-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/Audacious?diff=0&oldid=473815>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Audacious_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Audacious](<https://audacious-media-player.org/>) 是一款自由且先进的音频播放器。它专注于音频质量，支持各种广泛的音频编解码器，并且可以通过第三方插件轻松扩展。 

##  安装

[安装](<../zh-cn/Pacman.html> "Pacman")软件包 [audacious](<https://archlinux.org/packages/?name=audacious>)包。如果要音频 CD 支持，请安装[libcdio](<https://archlinux.org/packages/?name=libcdio>)包. 

##  配置

###  界面

Audacious有两种不同的界面，可以通过配置进行设置： 

  * Winamp 经典界面
  * GTK+ 界面（默认）

###  加入 Winamp 皮肤

加入 Winamp 面板到 Audacious 很简单，只要复制你的面板(.zip, .wsz, .tgz, .tar.gz, 和 .tar.bz2 档)到 **`/usr/share/audacious/Skins`** 或全局的`/usr/share/audacious/Skins`。然后就能在 主选单 > _Preferences_ > _Skinned Interface_ 选择使用的皮肤。 

##  技巧和问题

### Audtool

Audacious附带有威力强大的管理工具Audtool，可以从播放器取得信息或控制播放器。 

例如，取得目前播放的歌名或歌手： 
    
    audtool current-song
    
    audtool current-song-tuple-data artist
    
其它还有播放控制、编辑播放列表、调整平衡器和主界面等功能。完整的选项列表: 
    
    audtool --help
    
###  MP3 问题

安装 [mpg123](<https://archlinux.org/packages/?name=mpg123>)包. 

###  Audacious 将自己设置为默认文件管理器

请阅读 [File manager functionality#Directories are not opened in the file manager](<../zh-cn/File_manager_functionality.html#Directories_are_not_opened_in_the_file_manager> "File manager functionality"). 
