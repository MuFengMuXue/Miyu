**翻译状态：**

  * 本文（或部分内容）译自 [TheShell](<https://wiki.archlinux.org/title/TheShell> "arch:TheShell")，最近一次同步于 2020-08-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/TheShell?diff=0&oldid=628138>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/TheShell_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [Qt](<../zh-cn/Qt.html> "Qt")

[theShell](<https://github.com/vicr123/theshell>) 是一个使用 [Qt](<../zh-cn/Qt.html> "Qt") 写成的[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")。 

##  安装

你可以[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")稳定版本： [theshell](<https://aur.archlinux.org/packages/theshell/>)AUR。 

theShell 有一个不稳定且未经充分测试的版本，叫做 “blueprint”，它可以用 [theshell-blueprint](<https://aur.archlinux.org/packages/theshell-blueprint/>)AUR [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")。 

##  开始

在 [X Session](<../zh-cn/X_session.html> "X session") 中用 `ts-startsession` 启动 theShell。或使用[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")并使用“theShell”作为会话。 

##  问题解决

###  按下 “Adjust Screen Resolution” 却没有反应……

请确保 [kscreen](<https://archlinux.org/packages/?name=kscreen>)包 和 [kde-cli-tools](<https://archlinux.org/packages/?name=kde-cli-tools>)包 工具已经安装。[[1]](<https://github.com/vicr123/theshell/issues/53>)

更多问题，参见 [theshell issues](<https://github.com/vicr123/theshell/issues>)。 

##  提示技巧

###  安装稳定版本和 “blueprint” 版本

theShell 和 theShell Blueprint 可以被一起安装。只需重命名二进制和初始化脚本（`theshell-b` 和 `init-theshell-b` 是一对好名字），并将它们放在二进制文件夹中，重命名 `.desktop` 文件，将其更改为启动新的初始化脚本并将其放在 xsessions 文件夹中。 

###  使用另一个窗口管理器

在 theShell 设置中， _Danger_ 类别下，在 _Window Manager Command_ 下输入用于启动窗口管理器的命令。 
