**翻译状态：**

  * 本文（或部分内容）译自 [LilyPond](<https://wiki.archlinux.org/title/LilyPond> "arch:LilyPond")，最近一次同步于 2024-09-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/LilyPond?diff=0&oldid=760918>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/LilyPond_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[LilyPond（荷花池）](<https://lilypond.org/>)是一款自由的制谱软件。 它的输入是 LilyPond 音乐写作格式的纯文本文件，输出是 PostScript 或 PDF。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [lilypond](<https://archlinux.org/packages/?name=lilypond>)包 包。 

###  前端

  * **[Denemo](<https://en.wikipedia.org/wiki/Denemo> "wikipedia:Denemo")** — 支持键盘、MIDI 与音频输入，使用 C 语言编写。

     <http://denemo.org/> || [denemo](<https://aur.archlinux.org/packages/denemo/>)AUR

  * **[Frescobaldi](<https://en.wikipedia.org/wiki/Frescobaldi_\(software\)> "wikipedia:Frescobaldi \(software\)")** — 用 Python 和 PyQt 编写，提供双向点击、MIDI 捕捉和播放的音乐预览。

     <https://www.frescobaldi.org/index.html> || [frescobaldi](<https://archlinux.org/packages/?name=frescobaldi>)包

##  使用方法

创建一个这样的测试文档： 
    
    test.ly
    
    {
     c' e' g' e'
    }
    
若要编译它，请输入: 
    
    $ lilypond test.ly
    
它将创建包含总谱的 `test.pdf` 和 `test.ps` 文件。 

LilyPond 提供 [musicxml2ly(1)](<https://man.archlinux.org/man/musicxml2ly.1>) 来将 [MusicXML](<https://en.wikipedia.org/wiki/MusicXML> "wikipedia:MusicXML") 转换为 LilyPond 格式。 

更多信息，请参阅 `info lilypond`、[lilypond(1)](<https://man.archlinux.org/man/lilypond.1>) 和[文档](<https://lilypond.org/manuals.html>)。 

##  文本编辑器支持

LilyPond 自带 [Emacs](<../zh-cn/Emacs.html> "Emacs") 和 [Vim](<../zh-cn/Vim.html> "Vim") 模式，请参阅[文档](<https://lilypond.org/doc/Documentation/usage/text-editor-support>)。 

关于 Vim，请参见文件类型插件 `/usr/share/vim/vimfiles/ftplugin/lilypond.vim` 以获取可用的按键映射。 

### Emacs lilypond-mode

[lilypond](<https://archlinux.org/packages/?name=lilypond>)包 软件包安装了一些 [Emacs](<../zh-cn/Emacs.html> "Emacs") 文件，包括 `/usr/share/emacs/site-lisp/lilypond-mode.el`。 

要使用 `lilypond-mode` ，首先要 `M-x load-library <RET> lilypond-mode <RET>` 然后再 `M-x lilypond-mode <RET>` 。 

### NeoVim

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 此处翻译可能存在问题。（在 [Talk:LilyPond#](<../zh-cn/Talk:LilyPond.html>) 中讨论）

[nvim-lilypond-suite](<https://github.com/martineausimon/nvim-lilypond-suite>) 是一个用于编写 LilyPond 乐谱的插件，具有 asynchronous make、midi/MP3 播放器、歌词"hyphenation"功能、快速语法高亮等功能。该资源库还包含一个用于 [LaTeX](<../zh-cn/TeX_Live.html> "LaTeX") 文件的 ftplugin（允许嵌入 LilyPond 语法高亮），以及支持 `lilypond-book` 或 [lyluatex-git](<https://aur.archlinux.org/packages/lyluatex-git/>)AUR 软件包的 makeprg。 

##  参见

  * [Wikipedia:LilyPond](<https://en.wikipedia.org/wiki/LilyPond> "wikipedia:LilyPond")
  * [应用程序列表/多媒体#Scorewriters](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%A4%9A%E5%AA%92%E4%BD%93.html#Scorewriters> "应用程序列表/多媒体")
