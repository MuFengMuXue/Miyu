**翻译状态：**

  * 本文（或部分内容）译自 [Vivaldi](<https://wiki.archlinux.org/title/Vivaldi> "arch:Vivaldi")，最近一次同步于 2022-01-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Vivaldi?diff=0&oldid=713634>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Vivaldi_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Vivaldi](<https://vivaldi.com/>) 是由前 [Opera](<../zh-cn/Opera.html> "Opera") 创立者和开发团队成员开发的一款网页浏览器。Vivaldi 基于 [Chromium](<../zh-cn/Chromium.html> "Chromium") 开发，专注于个性化体验。 

##  安装

可以安装Vivaldi的正式版（[vivaldi](<https://archlinux.org/packages/?name=vivaldi>)包）或从AUR安装快照版（[vivaldi-snapshot](<https://aur.archlinux.org/packages/vivaldi-snapshot/>)AUR）。 或者也可以添加 [herecura](<../zh-cn/Unofficial_user_repositories.html#herecura> "Unofficial user repositories") 的非官方源，安装预构建的包。 

正式版与快照版的区别请参阅**[这里](<https://vivaldi.com/blog/snapshot-vs-stable/>)** 。 

若需将 [GTK](<../zh-cn/GTK.html> "GTK") 风格的文件选择对话框替换成 [Qt](<../zh-cn/Qt.html> "Qt") 风格，只要安装 [kdialog](<https://archlinux.org/packages/?name=kdialog>)包 包即可。 

##  扩展程序

Vivaldi 兼容 Chrome 的绝大部分扩展。可以从[Chrome网上商店](<https://https://chrome.google.com/webstore/category/extensions>)直接安装。 

**提示：** Vivaldi支持在命令行附加**代理服务器** 参数，形如`--proxy-server="socks5://127.0.0.1:1080"`。这可能有助于解决某些特定条件下的网络连接问题。

查看已安装或启用的扩展，可访问地址：`vivaldi://extensions`。 另请参阅[维基百科：谷歌Chrome扩展](<https://en.wikipedia.org/wiki/Google_Chrome_Extension> "wikipedia:Google Chrome Extension")

##  媒体播放

启用适当的媒体回放支持（H264，AAC等等）： 

  * 安装[vivaldi-ffmpeg-codecs](<https://archlinux.org/packages/?name=vivaldi-ffmpeg-codecs>)包或[vivaldi-snapshot-ffmpeg-codecs](<https://aur.archlinux.org/packages/vivaldi-snapshot-ffmpeg-codecs/>)AUR。（ _**译者注：前述[herecura](<../zh-cn/Unofficial_user_repositories.html#herecura> "Unofficial user repositories") 的非官方源里同样有预构建的包。**_）
  * 启动Vivaldi刷新（更新或重装之后），关闭再重新打开Vivaldi。
  * 使用AUR中的[vivaldi-update-ffmpeg-hook](<https://aur.archlinux.org/packages/vivaldi-update-ffmpeg-hook/>)AUR。
  * 要播放 flash 媒体文件应当安装 [pepper-flash](<https://aur.archlinux.org/packages/pepper-flash/>)AUR。

## Making flags persistent

**注意：**`vivaldi-stable.conf`文件专用于Arch Linux的[vivaldi](<https://archlinux.org/packages/?name=vivaldi>)包安装包。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 英文版待译。（在 [Talk:Vivaldi#](<../zh-cn/Talk:Vivaldi.html>) 中讨论）

You can put your flags in a `vivaldi-stable.conf` file under `$HOME/.config/` (or under `$XDG_CONFIG_HOME` if you have configured that environment variable). 

No special syntax is used; flags are defined as if they were written in a terminal. 

  * The arguments are split on whitespace and shell quoting rules apply, but no further parsing is performed.
  * Flags can be placed in separate lines for readability, but this is not required.

Below is an example `vivaldi-stable.conf` file that disables hardware media keys for the browser: 
    
    ~/.config/vivaldi-stable.conf
    
    --disable-features=HardwareMediaKeyHandling
    
The [vivaldi-snapshot](<https://aur.archlinux.org/packages/vivaldi-snapshot/>)AUR package can get its flags set with the `vivaldi-snapshot.conf` file. 

##  魔改

Vivaldi可以修改它的`browser.html`文件支持Mod魔改。 

文件位置：`/opt/vivaldi/resources/vivaldi/browser.html`

其它魔改途径可以访问`vivaldi://about/`看看 _可执行文件路径_ 。 

##  提示与技巧

###  将配置文件转换为快照版

如果你为了体验正式版中没有的功能而切换到了快照版，而又希望仍然使用原来的用户配置文件，可以把`~/.config/vivaldi/Default`复制为 `~/.config/vivaldi-snapshot/Default`。（译注：请注意，这里是**“复制为”** 而不是**“复制到”** ） 

###  谷歌搜索建议

Vivaldi发布版本**[不能内置谷歌搜索建议功能](<https://forum.vivaldi.net/topic/28880/google-suggestions-in-address-bar/2>)** 。用户必须在搜索的设置项中手工添加URL：**[https://www.google.com/complete/search?client=chrome&q=%s](<https://www.google.com/complete/search?client=chrome&q=%s>)**。 

##  参阅

  * [官方网站](<https://vivaldi.com/>)
  * [Vivaldi浏览器中文讨论区](<https://vivaldi.club/>)（由前 _Opera中国_ 员工[@Csineneo](<https://twitter.com/csineneo>)创建的非官方中文论坛）
