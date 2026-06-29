**翻译状态：**

  * 本文（或部分内容）译自 [LibreOffice](<https://wiki.archlinux.org/title/LibreOffice> "arch:LibreOffice")，最近一次同步于 2025-3-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/LibreOffice?diff=0&oldid=826583>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/LibreOffice_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Apache OpenOffice](<../zh-cn/Apache_OpenOffice.html> "Apache OpenOffice")

引自[主页 - LibreOffice](<https://zh-cn.libreoffice.org/>): 

    _LibreOffice是一款功能强大且免费的开源办公软件，它同时支持Windows, Macintosh 和 Linux系统，为你提供六种针对文档编辑和数据处理需求的拥有丰富功能的应用：Writer, Calc, Impress, Draw, Math和Base。_

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")以下[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")软件包的其中之一: 

  * [libreoffice-fresh](<https://archlinux.org/packages/?name=libreoffice-fresh>)包 是一个功能分支，包含新的程序增强功能，适合尝鲜的用户或高级用户。 安装最新版本的简体中文版本：
        
        # pacman -S libreoffice-fresh libreoffice-fresh-zh-cn

  * [libreoffice-still](<https://archlinux.org/packages/?name=libreoffice-still>)包 是一个维护分支。 安装稳定版本的简体中文版本：
        
        # pacman -S libreoffice-still libreoffice-still-zh-cn

**注意：**

  * 安装过程中至少需要安装一种语言包。默认的语言为 Afrikaans (这是因为它是提供的libreoffice语言包的字母排序首位)。简体中文请安装 [libreoffice-fresh-zh-cn](<https://archlinux.org/packages/?name=libreoffice-fresh-zh-cn>)包 或 [libreoffice-still-zh-cn](<https://archlinux.org/packages/?name=libreoffice-still-zh-cn>)包，繁体中文请安装 [libreoffice-fresh-zh-tw](<https://archlinux.org/packages/?name=libreoffice-fresh-zh-tw>)包 或 [libreoffice-still-zh-tw](<https://archlinux.org/packages/?name=libreoffice-still-zh-tw>)包。
  * 对于 SDK - 根据自己安装的 libreoffice 包的情况可以选择 [libreoffice-fresh-sdk](<https://archlinux.org/packages/?name=libreoffice-fresh-sdk>)包 或 [libreoffice-still-sdk](<https://archlinux.org/packages/?name=libreoffice-still-sdk>)包。

  * 对于 Qt 和 GTK+ 可视化工具, 详见 [#主题](<#%E4%B8%BB%E9%A2%98>).

检查一下 pacman 输出的可以选择安装的依赖包。Java Runtime Environment 并不是必须的，除非你想要使用 Libreoffice Base: 详见 [Java](<../zh-cn/Java.html> "Java")。你可能需要 [hsqldb2-java](<https://aur.archlinux.org/packages/hsqldb2-java/>)AUR 来使用 [一些模块](<https://wiki.documentfoundation.org/Base#Java_and_HSQLDB>) （在 Libreoffice Base 当中）。 

##  主题

LibreOffice 包括[GTK](<../zh-cn/GTK.html> "GTK") 和 [Qt](<../zh-cn/Qt.html> "Qt") 主题集合支持。参见[Uniform look for Qt and GTK applications](<../zh-cn/Uniform_look_for_Qt_and_GTK_applications.html> "Uniform look for Qt and GTK applications")。 

LibreOffice 会基于您的桌面环境尝试自动检测最合适的[VCL](<https://github.com/LibreOffice/core/blob/master/vcl/README.md>) 界面。要强制使用某个VCL界面，例如"gtk4"，设置 [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `SAL_USE_VCLPLUGIN=gtk4`。要查看更多用户界面选项，可查看`/etc/profile.d/libreoffice-fresh.sh` 或 `/etc/profile.d/libreoffice-still.sh`, 所有变量已被列出并可取消注释。 

##  管理扩展

以下插件可以通过 [官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库") 获得: 

  * [libreoffice-extension-texmaths](<https://archlinux.org/packages/?name=libreoffice-extension-texmaths>)包，可以创建LaTeX数学公式(PNG 或 SVG 图像)插入到 Writer,Impress,和Draw 中。[[1]](<http://roland65.free.fr/texmaths/>)
  * [libreoffice-extension-writer2latex](<https://archlinux.org/packages/?name=libreoffice-extension-writer2latex>)包，可以将Writer文档转换为LaTeX文件。[[2]](<https://writer2latex.sourceforge.net/>)

要获取更多插件, 可以查看 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR"), 内置的 LibreOffice 扩展插件管理, 或者访问 [libreplanet](<https://libreplanet.org/wiki/Group:OpenOfficeExtensions/List>). 

##  字体

文档基金会 [wiki](<https://wiki.documentfoundation.org/Fonts>) 提到在 Windows 和 macOS 上的 LibreOffice 默认打包的各种字体，在 Arch 上，安装以下包可获得这些字体： 

  * [ttf-caladea](<https://archlinux.org/packages/?name=ttf-caladea>)包
  * [ttf-carlito](<https://archlinux.org/packages/?name=ttf-carlito>)包
  * [ttf-dejavu](<https://archlinux.org/packages/?name=ttf-dejavu>)包
  * [ttf-gentium-basic](<https://aur.archlinux.org/packages/ttf-gentium-basic/>)AUR
  * [ttf-liberation](<https://archlinux.org/packages/?name=ttf-liberation>)包
  * [ttf-linux-libertine-g](<https://archlinux.org/packages/?name=ttf-linux-libertine-g>)包
  * [noto-fonts](<https://archlinux.org/packages/?name=noto-fonts>)包
  * [adobe-source-code-pro-fonts](<https://archlinux.org/packages/?name=adobe-source-code-pro-fonts>)包
  * [adobe-source-sans-fonts](<https://archlinux.org/packages/?name=adobe-source-sans-fonts>)包
  * [adobe-source-serif-fonts](<https://archlinux.org/packages/?name=adobe-source-serif-fonts>)包

参见[Fonts#Font packages](<../zh-cn/%E5%AD%97%E4%BD%93.html#Font_packages> "Fonts"). 

##  语言辅助工具

###  拼写检查

为了开启拼写检查，你首先需要确保安装了 [hunspell](<../zh-cn/%E8%AF%AD%E8%A8%80%E6%A3%80%E6%9F%A5.html> "Hunspell") 和对应语言的 hunspell 词典。比如说英语的[hunspell-en_us](<https://archlinux.org/packages/?name=hunspell-en_us>)包，德语的[hunspell-de](<https://archlinux.org/packages/?name=hunspell-de>)包等等。然后在 LibreOffice 中勾选 _工具 > 选项 > 语言和区域 > 写作辅助 > Hunspell 拼写检查_复选框并重启 LibreOffice。 

芬兰语

与其他语言不同，芬兰语的拼写检查和语法检查基于 [Voikko](<https://voikko.puimula.org/>)。对于 LibreOffice，应安装 [voikko-libreoffice](<https://aur.archlinux.org/packages/voikko-libreoffice/>)AUR。 

希腊语

项目 [Orthos](<https://sourceforge.net/projects/orthos-spell/?source=directory>) 以 Libreoffice 扩展的形式提供了更完整的希腊语拼写检查。软件包 [libreoffice-extension-orthos-greek-dictionary](<https://aur.archlinux.org/packages/libreoffice-extension-orthos-greek-dictionary/>)AUR 提供了纯希腊语拼写词典，而 [libreoffice-extension-orthos-greek-english-dictionary](<https://aur.archlinux.org/packages/libreoffice-extension-orthos-greek-english-dictionary/>)AUR 则提供了希腊语和美式英语词典。 

###  双语言支持

**注意：** 如果你的地区设置为双语言，Libreoffice 应默认启用 CTL，但有可能会 [错误设置成印地语](<https://bugs.documentfoundation.org/show_bug.cgi?id=154495>).

要启用双语言支持，勾选 _工具 > 选项 > 语言和区域 > 通用 > 复杂文本排版_复选框，并选择合适的语言。可以通过 “RCtrl + RShift ”和 “LCtrl + LShift ”进行强制语言对齐。有一个 [已知问题](<https://bugs.documentfoundation.org/show_bug.cgi?id=151857>) 是会在段落样式改变时改变文本方向。 

###  断词换行规则

为了开启换行规则，你需要安装 [hyphen](<https://archlinux.org/packages/?name=hyphen>)包 和与语言对应hyphen规则，比如说 英语的[hyphen-en](<https://archlinux.org/packages/?name=hyphen-en>)包，德语的[hyphen-de](<https://archlinux.org/packages/?name=hyphen-de>)包等等。 

###  词库

对于词库选项, 你需要 [libmythes](<https://archlinux.org/packages/?name=libmythes>)包 和一个 mythes 语言词库 (比如英语的 [mythes-en](<https://archlinux.org/packages/?name=mythes-en>)包 , 德语的 [mythes-de](<https://archlinux.org/packages/?name=mythes-de>)包 , 等等))。 

希腊语

对于希腊语，您可以尝试使用 [libreoffice-extension-orthos-greek-thesaurus](<https://aur.archlinux.org/packages/libreoffice-extension-orthos-greek-thesaurus/>)AUR 替代 [mythes-el](<https://aur.archlinux.org/packages/mythes-el/>)AUR ，前者包含更多单词。 

###  语法检查

语法检查有[多种工具](<../zh-cn/Language_checking.html> "Language checking")可供选择。最常用的是 [languagetool](<https://archlinux.org/packages/?name=languagetool>)包。使用说明取决于您所使用的 LibreOffice 版本。 

从 7.4 版[LibreOffice 开始本地支持 LanguageTool](<https://wiki.documentfoundation.org/ReleaseNotes/7.4#New_remote_grammar_checker:_LanguageTool>)，无需安装扩展： 

  1. 点击 _工具 > 选项... > 语言和区域 > LanguageTool 服务器_。
  2. 勾选 _启用LanguageTool_ 复选框。
  3. 使用的 URL 取决于您是拥有远程账号（免费或高级），还是使用本地服务器： 
     * 如果您使用远程免费账号，请使用 `https://api.languagetool.org/v2` 作为 “基本 URL”。其余文本框留空。
     * 如果您使用远程高级账号，请使用 `https://api.languagetoolplus.com/v2` 作为 “基本 URL”，填写您的电子邮件地址，并输入 API 密钥。
     * 如果已安装 [本地 LanguageTool 服务器](<https://dev.languagetool.org/http-server>)，请使用 `<http://localhost:8081/v2>` 作为 “基本 URL”。用户名 “和 ”API 密钥 "留空。
  4. 点击 _确定_ ，并打开一个未打开文档。
  5. 勾选复选框 _工具 > 自动拼写检查_。

访问 [LanguageTool 页面了解更多信息](<https://languagetool.org/insights/post/product-libreoffice/>). 

###  离线帮助

软件包 [libreoffice-still](<https://archlinux.org/packages/?name=libreoffice-still>)包 和 [libreoffice-fresh](<https://archlinux.org/packages/?name=libreoffice-fresh>)包 提供 en-US 的离线帮助文件。不同语言的离线帮助文件由相应的 libreoffice 语言包提供（例如，[libreoffice-fresh-en-za](<https://archlinux.org/packages/?name=libreoffice-fresh-en-za>)包 提供 en-ZA 地方语言的帮助文件）。 

##  提示和技巧

###  加速启动

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 拼写检查和语法检查可能不会影响 LibreOffice 的启动速度并且关闭会限制它的功能。（在 [Talk:LibreOffice](<../zh-cn/Talk:LibreOffice.html>) 中讨论）

  * **关闭启动LOGO** : 如果你希望开启libreoffice时启动logo不再出现, 可以打开 `/etc/libreoffice/sofficerc`, 找到`Logo=` 那一行并且设置 `Logo=0`。或者使用`--nologo` [CLI](<../zh-cn/Command-line_shell.html> "Command-line shell")选项。

  * **禁用Java runtime** : 如果你不使用依赖 Java 的功能，可以考虑禁用Java runtime。选择 _工具 > 选项 > LibreOffice > 高级_并取消勾选 _使用 Java 运行时环境_ 。

  * **关闭自动拼写检查** : 在 _工具 > 选项 > 语言和区域 > 写作辅助_并取消勾选 _输入时检查拼写_ 和 _输入时检查语法_ 。

###  宏的安装

如果打算使用宏，你必须启用 JAVA Runtime 。 

对于 Arch Linux 而言，LibreOffice 宏的默认路径与大多数 Linux 发行版不同，该路径位于`~/.config/libreoffice/4/user/Scripts/`

###  使用 Base 作为数据库前端

Base 可以作为 PostgreSQL 之类的数据库前端。它不能编辑表但能很好的查看表的属性和字段，还可以隐藏属性，以便更好地概览相关数据。它还可以过滤数据，选择多个字段进行删除，并轻松编辑每个属性值。它还可以帮助用户通过图形界面进行 SQL 查询。 

###  使用 LibreOffice 或 OpenOffice 进行自动文档转换

使用 LibreOffice 的`--headless`命令行选项可以立即完成文档转换。例如，将一个`.odt`文档转换为`.pdf`文件，你可以输入 
    
    $ libreoffice --headless --convert-to pdf ./*.odt
    
另一种方法是使用命令行工具[unoconv](<https://archlinux.org/packages/?name=unoconv>)包，这是一个使用 LibreOffice 进行自动转换和样式工具，尽管它需要更多的工作去完善[[3]](<https://github.com/unoconv/unoconv/issues/511>)，但依然是一个有用的工具。它会连接到运行中的 LibreOffice，或启动一个供自己使用的 LibreOffice，再或者连接到一个运行中的实例，该实例是明确启动供自己使用。而不需要运行 X 显示服务器。 

###  提示音

一些用户喜欢关闭保存未保存文档时“是否保存文档”弹出窗口的提示音。可以通过更改 GTK 配置选项`gtk-enable-event-sounds`来启用/禁用通知声音。参见 [GTK#Examples](<../zh-cn/GTK.html#Examples> "GTK")。 

##  疑难解答

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 翻译已经过期，请阅读英文页面中的内容。（在 [Talk:LibreOffice#](<../zh-cn/Talk:LibreOffice.html>) 中讨论）

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:LibreOffice#](<../zh-cn/Talk:LibreOffice.html>) 中讨论）

###  更改字体

字体可以在LibreOffice的选项里更改。在下拉菜单中，选中 工具 > 选项 > LibreOffice > 字体 。选中 “使用替换表”。在字体框输入 Andale Sans UI 并对于替换选项选择你喜欢的字体。选好后，点击右侧的对勾。然后根据需要在下面的框中选择 _自动_ 或者 _只显示屏幕_ 。选择 OK 。 此外还需要进入 工具 > 选项 > LibreOffice > 视图, 取消选中 "用户界面使用系统字体"。如果你的字体不支持抗锯齿，比如 Arial 字体，你还需要取消选中 "屏幕字体抗锯齿" 。 

###  抗锯齿

执行 
    
    $ echo "Xft.lcdfilter: lcddefault" | xrdb -merge
    
如需使其永久生效，请添加 `Xft.lcdfilter: lcddefault` 到你的 `~/.Xresources` 文件，并且确保执行 `xrdb -merge ~/.Xresources`。 [[4]](<https://bugs.launchpad.net/ubuntu/+source/openoffice.org/+bug/271283/comments/19>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2020-08-02 ⓘ]. 更多信息请查看 [X resources](<../zh-cn/X_resources.html> "X resources")。 

如果这样不起作用的话，你也可以尝试添加 `Xft.lcdfilter: lcddefault` 到你的 `~/.Xdefaults` 文件。如果文件不存在请创建一个。 

###  使用NFSv3共享时突然停止运行

如果在你试图打开或者保存一个位于NFSv3共享的文档的时候 LibreOffice 停止运行，试着在以 `#` 开头在 `/usr/lib/libreoffice/program/soffice` 中添加以下几行: 
    
    # file locking now enabled by default
    SAL_ENABLE_FILE_LOCKING=1
    export SAL_ENABLE_FILE_LOCKING
    
为了避免覆盖更新你可以将 `/usr/lib/libreoffice/program/soffice` 复制到 `/usr/local/bin`. 原始链接为 [点击这里](<https://web.archive.org/web/20120910162208/http://www.crazysquirrel.com/computing/debian/bugs/openoffice-over-nfs.jspx>). 

###  对Java framework错误的修正

当你试图运行Libreoffice时可能会出现以下错误。 
    
    [Java framework] Error in function createSettingsDocument (elements.cxx).
    javaldx failed!
    
如果是这样的话, 将你的权限赋像这样给 `~/.config/` : 
    
    # chown -vR username:users ~/.config
    
[参照 Arch Linux forums 上的这篇帖子](<https://bbs.archlinux.org/viewtopic.php?id=93168>). 

###  LibreOffice无法检测到你的证书

如果在你为一个文档签名的时候无法查看证书, 你需要取得在 Mozilla Firefox (或者 Thunderbird) 中配置的证书。如果在这之后 LibreOffice 仍然无法显示证书, 设置 `MOZILLA_CERTIFICATE_FOLDER` 环境变量指向你的 Mozilla Firefox (或者 Thunderbird) 文件夹: 
    
    export MOZILLA_CERTIFICATE_FOLDER=$HOME/.mozilla/firefox/XXXXXX.default/
    
[证书检测](<https://wiki.openoffice.org/wiki/Certificate_Detection>). 

###  在编辑模式下运行 .pps 文件(没有幻灯片)

针对此问题的唯一解决办法就是 将`.pps` 文件重命名为 `.ppt`. 

添加以下脚本到你的home目录并且使用它来打开每一个 .pps 文件。 对于通过 email 接收到的 `.pps` 文件，在仅仅需要打开而无需保存时是非常有用的。 
    
    #!/bin/bash
    
    f=$(mktemp)
    cp "$1" "${f}.ppt" && libreoffice "${f}.ppt" && rm -f "${f}.ppt"
    
###  参考书目的问题

如果 Writer 在打开 _工具 > 文献数据库_ 时崩掉, 且出现了以下提示语句: 
    
    com::sun::star::loader::CannotActivateFactoryException
    
请安装 [libreoffice-base](<https://archlinux.org/packages/?name=libreoffice-base>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] ，这是对于一个已知bug的解决办法，请参照[解决](<https://cgit.freedesktop.org/libreoffice/core/commit/?id=1889c1af41650576a29c587a0b2cdeaf0d297587>). 

###  多媒体支持

如果插入的videos仅仅显示为灰色的框，请首先确认你是否已经安装了必须的 [GStreamer plugins](<../zh-cn/GStreamer.html#Installation> "GStreamer")。 

###  在 Xfwm4 下内容未按照窗口改变自身大小

如果在 Xfce (或者仅仅使用 Xfwm4) 时你在 LibreOffice 窗口下的内容并未随着窗口变化而改变大小,就类似在这个帖子里描述的: [[5]](<https://bbs.archlinux.org/viewtopic.php?id=133137>)。请安装 [libreoffice-still-gnome](<https://archlinux.org/packages/?name=libreoffice-still-gnome>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 来解决这个问题。 

###  gvfs 映射

如果你需要在 gvfs 映射下打开/保存文档，你需要安装 [libreoffice-still-gnome](<https://archlinux.org/packages/?name=libreoffice-still-gnome>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] . 
