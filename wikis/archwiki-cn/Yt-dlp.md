相关文章

  * [mpv](<../zh-cn/Mpv.html> "Mpv")
  * [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg")

**翻译状态：**

  * 本文（或部分内容）译自 [yt-dlp](<https://wiki.archlinux.org/title/yt-dlp> "arch:yt-dlp")，最近一次同步于 2025-10-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/yt-dlp?diff=0&oldid=847897>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/yt-dlp_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**yt-dlp** 是一款可让您轻松从一千多个网站下载视频和音频的命令行程序。查看[受支持的网站列表](<https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md>)。 

**注意：** yt-dlp 是 [youtube-dl](<https://ytdl-org.github.io/youtube-dl/>) 的一个分支，创建于原项目停滞之后。上游的 youtube-dl 仍可通过 [youtube-dl](<https://aur.archlinux.org/packages/youtube-dl/>)AUR 来[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")；本页的命令通常仍可正常使用，但请参阅[默认行为差异列表](<https://github.com/yt-dlp/yt-dlp#differences-in-default-behavior>)以了解具体区别。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[yt-dlp](<https://archlinux.org/packages/?name=yt-dlp>)包。同时建议安装 [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg")（用来封装部分网站的文件），请参阅可选依赖项。 

yt-dlp 还有各种[图形前端](<https://www.reddit.com/r/youtubedl/wiki/info-guis>)，如 [tartube](<https://aur.archlinux.org/packages/tartube/>)AUR 和 [yt-dlg-git](<https://aur.archlinux.org/packages/yt-dlg-git/>)AUR。 

您还可以安装 [yt-dlp-drop-in](<https://aur.archlinux.org/packages/yt-dlp-drop-in/>)AUR，它提供了一个占位的 `/usr/bin/youtube-dl` 可执行文件（只是重定向到 _yt-dlp_ ），以兼容那些仍在寻找 _youtube-dl_ 可执行文件的过时程序。 

##  配置

系统全局配置文件是 `/etc/yt-dlp.conf`，用户的配置文件为`~/.config/yt-dlp/config`。配置示例： 
    
    --ignore-errors
    # --no-playlist
    
    # 保存至 ~/Videos
    -o ~/Videos/%(title)s.%(ext)s
    
    # 首选1080p或更低的分辨率
    -f bestvideo[height<=?1080]+bestaudio/best
    
更多信息请参见[[1]](<https://github.com/yt-dlp/yt-dlp/blob/master/README.md#configuration>)

自定义配置文件也可以指定： 
    
    $ yt-dlp _URL_ --config-locations _PATH_
    
##  用法

请参见 [yt-dlp(1)](<https://man.archlinux.org/man/yt-dlp.1>) 手册。 
    
    $ yt-dlp [OPTIONS] _URL_
    
**提示：** 在某些情况下（如 YouTube）` _URL_` 可以用视频ID代替。

###  格式选择

当多种格式的视频可用时， _yt-dlp_ 将默认下载最好的格式。 

获取可用格式的列表： 
    
    $ yt-dlp -F _URL_
    
选择一个特定的要下载： 
    
    $ yt-dlp -f _format_ _URL_
    
###  提取音频

使用`-x`下载音频（需要 [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg")）： 
    
    $ yt-dlp -x -f bestaudio _URL_
    
根据可用的源流，这通常可以修正纯音频容器。若无可用的纯音频流，请从上述示例中移除 `-f bestaudio` 参数。此操作会先下载视频文件，并在后续处理中提取其音频。默认情况下会删除已下载的视频文件，添加 `-k` 参数可保留视频文件。 

同时包括专辑封面：（需要[atomicparsley](<https://archlinux.org/packages/?name=atomicparsley>)包）： 
    
    $ yt-dlp -x -f bestaudio[ext=m4a] --add-metadata --embed-thumbnail _URL_
    
###  字幕

查看哪些语言可用： 
    
    $ yt-dlp --list-subs URL
    
下载带有选定字幕（用逗号分隔）的视频： 
    
    $ yt-dlp --write-sub --sub-lang _LANG_ _URL_
    
对于自动生成的字幕： 
    
    $ yt-dlp --write-auto-sub --sub-lang LANG URL
    
添加`--skip-download`仅获取字幕。 

### Cookie

要导入 cookie，添加 `--cookies-from-browser <browser>`。 

例如，从 chromium 导入： 
    
    $ yt-dlp --cookies-from-browser chromium URL
    
##  方法与技巧

###  更快的下载

一些网站限制了传输速度。您通常可以通过选择非DASH流或使用支持多连接下载的外部下载器 [aria2](<../zh-cn/Aria2.html> "Aria2") 来绕过这种限制。例如： 
    
    $ yt-dlp --downloader aria2c --downloader-args '-c -j 3 -x 3 -s 3 -k 1M' _URL_
    
###  播放列表

将 yt-dlp 用于播放列表通常归结为以下选项： 
    
    $ yt-dlp --ignore-errors --continue --no-overwrites --download-archive progress.txt _usual options_ _URL_
    
这组选项允许下载在中断后仍能有效继续。如果您正在进行归档操作，请添加您可能需要的常规选项，例如 `--write-xxx` 和 `--embed-xxx`。 

###  修剪（部分下载）

可以通过将 `yt-dlp -g -f _format_ _URL_` 的输出作为 _ffmpeg_ 的输入，并结合 `-ss`（用于输入）、`-t` 和 `-c copy` [选项](<https://ffmpeg.org/ffmpeg.html#Main-options>)来下载视频片段。 

###  来自剪贴板的URL

可以通过设置一个 [Shell 别名](<../zh-cn/Bash.html#%E5%88%AB%E5%90%8D> "Alias")、[桌面启动器](</wzh/index.php?title=%E6%A1%8C%E9%9D%A2%E5%90%AF%E5%8A%A8%E5%99%A8&action=edit&redlink=1> "桌面启动器（页面不存在）")（英语：[desktop launcher](<https://wiki.archlinux.org/title/desktop_launcher> "en:desktop launcher")）或键盘快捷键，从 [X Window 选区](<https://en.wikipedia.org/wiki/X_Window_selection> "wikipedia:X Window selection")中输出选中（或复制）的 URL 以下载视频或音频。具体方法可参阅[剪贴板工具](<../zh-cn/%E5%89%AA%E8%B4%B4%E6%9D%BF.html#Tools> "Clipboard")。 

##  另请参阅

  * [GitHub 代码仓库](<https://github.com/yt-dlp/yt-dlp>)
