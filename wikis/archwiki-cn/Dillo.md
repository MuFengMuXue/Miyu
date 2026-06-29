**翻译状态：**

  * 本文（或部分内容）译自 [Dillo](<https://wiki.archlinux.org/title/Dillo> "arch:Dillo")，最近一次同步于 2020-07-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dillo?diff=0&oldid=626449>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dillo_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Dillo](<https://www.Dillo.org>) 是一种多平台图形 Web 浏览器，以其速度快和占用空间小而著称。 

  * Dillo 用 C 和 C++ 编写。
  * Dillo 基于 FLTK2，即 Fast Light Toolkit（默认情况下为静态链接！）。
  * Dillo 是根据 GNU General Public License（GPLv3）分发的自由软件。
  * Dillo 努力对用户和开发人员友好。
  * Dillo 通过使用 Bug Meter 来帮助 Web 作者遵守 Web 标准。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [dillo](<https://archlinux.org/packages/?name=dillo>)包。 

##  配置

###  在 Dillo 中默认情况下启用 cookies

出于隐私原因，默认情况下禁用 cookies。如果要启用它们，请阅读[常见问题解答](<https://www.dillo.org/FAQ.html#q8>)

###  删除 cookies

首先，使用以下命令停止插件（dpi）： 
    
    $ dpidc stop

cookies dpi 会将所有永久（`ACCEPT`）cookies 写入磁盘，而临时 (`ACCEPT_SESSION`）cookies 将在 dpi 退出时丢失。 

其次，通过删除或编辑 `~/.dillo/cookies.txt` 文件来摆脱永久性 cookies。 信息来自于 <https://www.dillo.org/FAQ.html#q8> 。 

##  参见

  * [Dillo 主页](<https://www.dillo.org/>)
