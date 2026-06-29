**翻译状态：**

  * 本文（或部分内容）译自 [Gmrun](<https://wiki.archlinux.org/title/Gmrun> "arch:Gmrun")，最近一次同步于 2024/07/29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Gmrun?diff=0&oldid=813207>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Gmrun_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Gmrun](<https://github.com/wdlkmpx/gmrun>) (Gnome Completion-Run) 是一个和 [GNOME](<../zh-cn/GNOME.html> "GNOME") Run, [Application Finder](<https://docs.xfce.org/xfce/xfce4-appfinder/start>), [KRunner](<https://userbase.kde.org/Plasma/Krunner>) 等相似的轻量应用程序启动器。 

##  安装

可用 [gmrun](<https://archlinux.org/packages/?name=gmrun>)包 [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") Gmrun。 

##  使用

  * 键入并按 `Enter` 运行 GUI 应用程序。键入并按 `Ctrl+Enter` 运行终端程序。 不键入按 `Ctrl+Enter` 则打开终端仿真器。
  * Gmrun tab 补全功能： 按 Tab 键会出现一个可滚动的可能匹配列表。
  * 键入 Gmrun 的 Web 地址会自动启动 Web 浏览器以打开。
  * Email 地址同理：使用 `mailto:` 前缀，例如 `mailto:foo@bar.com`, 会启动您的 Email 客户端。
  * 可添加更多快捷方式到 `~/.gmrunrc`。（见下方 [#配置](<#%E9%85%8D%E7%BD%AE>)），或您可修改系统范围文件： `/etc/gmrunc`。
  * 您可键入 `!` 作为第一字符以启用搜索模式，标题将会由 _Run program_ 变为 _Search_ ，你键入后，Gmrun 将自动根据你的命令历史提出建议。
  * `Ctrl+r` 将允许您在历史记录中向后搜索。
  * `Ctrl+s` 将在历史记录中向前搜索。
  * `Ctrl+g` 将取消搜索。
  * 如果在配置文件中定义了扩展名，那么只需键入文件名，文件就可以被正确的程序启动。
  * 按下 `Esc` 以关闭 Gmrun，不运行任何东西。

##  配置

配置文件位于 `/etc/gmrunrc` 但您可创建每个用户的配置（推荐）于 `~/.gmrunrc`。请注意，`%u` 将被扩展为输入的完整命令。 `%s` 是快捷方式后的最后部分。（例如，如果您键入 URL `https://archlinux.org`，`%u` 将保留 `https://archlinux.org` 而 `%s` 将缩减为 `//archlinux.org`。） 

下面是一个示例配置文件。 
    
    ~/.gmrunrc
    
    # gmrun 配置文件
    # gmrun 由 Mihai Bazon <mishoo@infoiasi.ro> 授权
    # 适用 GPL v2.0
    
    # 设置终端
    Terminal = urxvt
    TermExec = ${Terminal} -e
    AlwaysInTerm = ssh telnet ftp lynx mc vi vim pine centericq perldoc man
    
    # 设置窗口的几何形状（除了高度）。
    Width = 400
    Top = 300
    Left = 450
    
    # 历史记录大小
    History = 256
    
    # 是否显示调用时选择的最后一个历史记录行
    ShowLast = 1
    
    # 显示以“.”开头的文件
    # 默认值为 0（关闭），如果您希望显示“隐藏”文件，请将其设置为 1
    # 在完成窗口中
    ShowDotFiles = 0
    
    # 超时（以毫秒为单位），gmrun 将模拟 TAB 按下
    # 如果不喜欢此功能，请将其设置为 NULL。
    TabTimeout = 0
    
    # URL 处理程序
    # 如果输入的文本是"http://www.baidu.com"，则：
    #   - %u 被整个 URL 替换 ("http://www.baidu.com")
    #   - %s 被替换为"//www.baidu.com"。 这对多 URL 很有用
    #     例如 "man:printf" --> %s 会被替换为 "printf"
    # 译者注：原文为谷歌搜索，如有需要，参见原版界面。
    URL_http = firefox %u
    URL_mailto = firefox -remote "mailto(%s)"
    URL_man = ${TermExec} 'man %s'
    URL_info = ${TermExec} 'info %s'
    URL_pd = ${TermExec} 'perldoc %s'
    URL_file = pcmanfm %s
    URL_readme = ${TermExec} 'less /usr/doc/%s/README'
    URL_info = ${TermExec} 'info %s'
    URL_sh = sh -c '%s'
    URL_paci = ${TermExec} 'pacman -S %s'
    URL_pacs = ${TermExec} 'pacman -Ss %s'
    
    # 扩展名处理程序
    EXT:doc,rtf = AbiWord %s
    EXT:txt,cc,cpp,h,java,html,htm,epl,tex,latex,js,css,xml,xsl,am,php,css,js,py,rb = gedit %s
    EXT:mpeg,mpg,avi,mkv,flv = vlc %s
    EXT:mp3,ogg,m4a,wmv,wma = deadbeef %s
    EXT:ps = gv %s
    EXT:pdf = epdfview %s
    
ShowDotFiles（1 或 0）：是否显示'.'开头文件（例如 `.gmrunrc`）。
TabTimeout（1 或 0）：当输入时，是否自动显示 tab 补全目录。
Terminal：当按下 `Ctrl+Enter` 且无输入时运行的命令。
TermExec：想要在终端运行一个特定的命令时运行的命令 （例如 `ls ~`）。
URL_http：当输入网址时运行的命令。
URL_mailto：当输入 E-mail 地址时运行的命令。
EXT:extension：指定打开特定扩展名文件的程序。
Top and Left：Gmrun 窗口的位置（以相应边缘的像素为单位）。
Width：窗口的宽度（以像素为单位）。
History：存储的命令历史记录的长度。

###  添加自定义快捷方式

可轻松添加快捷方式。例如，使用 **b** 作为百度搜索的快捷方式，则添加： 
    
    URL_b = firefox '<https://www.baidu.com/s?wd=%s'>
    
这样使用： 
    
    b:Arch
    
译者注：谷歌搜索，请见原版 [Gmrun#Adding custom shortcuts](<#Adding_custom_shortcuts>)。 

##  键绑定

您可使用[桌面环境](<../zh-cn/Desktop_environment.html> "Desktop environment")或[窗口管理器](<../zh-cn/Window_manager.html> "Window manager")的键绑定设置来为 Gmrun 设置。 
