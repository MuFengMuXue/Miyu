**翻译状态：**

  * 本文（或部分内容）译自 [Slock](<https://wiki.archlinux.org/title/Slock> "arch:Slock")，最近一次同步于 2024-7-5，若英文版本有所[更改](<https://wiki.archlinux.org/title/Slock?diff=0&oldid=811967>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Slock_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [会话锁定](</wzh/index.php?title=%E4%BC%9A%E8%AF%9D%E9%94%81%E5%AE%9A&action=edit&redlink=1> "会话锁定（页面不存在）")
  * [应用程序列表/安全#屏幕锁定](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%AE%89%E5%85%A8.html#%E5%B1%8F%E5%B9%95%E9%94%81%E5%AE%9A> "应用程序列表/安全")

Slock，或 "Simple X display locker"，是用于 [X](<../zh-cn/Xorg.html> "X") 的显示锁定器，其目标是最小、快速和轻量。[[1]](<https://tools.suckless.org/slock/>)。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") the [slock](<https://archlinux.org/packages/?name=slock>)包 或者 [slock-git](<https://aur.archlinux.org/packages/slock-git/>)AUR 软件包。 

##  配置

配置可通过[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑")`config.h`头文件，然后重新编译软件包来完成。配置完成后，您应该[创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")。 

##  用法

只需运行 `slock` 即可锁定屏幕。您还可以提供一个参数，以便在屏幕锁定后运行： 
    
    $ slock _cmd_ _[arg ...]_
    
要解锁屏幕，只需输入密码即可。 

##  提示与窍门

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 您可以参与翻译本节。（在 [Talk:Slock#](<../zh-cn/Talk:Slock.html>) 中讨论）

###  挂起时锁定

[创建](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建")以下服务，关闭显示器并锁定屏幕。 
    
    /etc/systemd/system/slock@.service
    
    [Unit]
    Description=Lock X session using slock for user %i
    Before=sleep.target
    
    [Service]
    User=%i
    Environment=DISPLAY=:0
    ExecStartPre=/usr/bin/xset dpms force suspend
    ExecStart=/usr/bin/slock
    
    [Install]
    WantedBy=sleep.target

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")`slock@_user_.service`systemd 单元，使其对用户名 _user_ 生效。 

### Block VT switching and prevent killing X

_slock_ recommends blocking VT switching so that the screen lock cannot be bypassed. For the same reason, _slock_ recommends preventing users from killing the X server. See [Xorg#Block TTY access](<../zh-cn/Xorg.html#Block_TTY_access> "Xorg") and [Xorg#Prevent a user from killing X](<../zh-cn/Xorg.html#Prevent_a_user_from_killing_X> "Xorg"). 

##  参见

  * [官方主页](<https://tools.suckless.org/slock/>)
