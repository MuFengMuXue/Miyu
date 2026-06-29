**翻译状态：**

  * 本文（或部分内容）译自 [Common Desktop Environment](<https://wiki.archlinux.org/title/Common_Desktop_Environment> "arch:Common Desktop Environment")，最近一次同步于 2024-8-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Common_Desktop_Environment?diff=0&oldid=755048>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Common_Desktop_Environment_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Common Desktop Environment](<https://en.wikipedia.org/wiki/Common_Desktop_Environment> "wikipedia:Common Desktop Environment") 是基于 Motif 小部件工具箱的 Unix 和 OpenVMS 桌面环境。 它是 UNIX98 工作站产品标准的一部分，并且长期以来就是与商用 Unix 工作站相关联的“经典” Unix 桌面。 尽管是旧版环境，但它仍然对 Linux 系统提供支持。 

##  安装

基本 CDE 系统是通过 [cdesktopenv-git](<https://aur.archlinux.org/packages/cdesktopenv-git/>)AUR AUR 包安装的。 

##  用法

### dtlogin

[cdesktopenv-git](<https://aur.archlinux.org/packages/cdesktopenv-git/>)AUR 软件包提供了 `dtlogin` systemd 服务，该服务在启动时将启动 CDE [登录管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "登录管理器")。 

### xinit

可以使用 `startx` 直接启动 CDE（安装 [xorg-xinit](<https://archlinux.org/packages/?name=xorg-xinit>)包）： 
    
    $ export PATH=$PATH:/usr/dt/bin
    $ export LANG=C
    $ startx /usr/dt/bin/Xsession
    
##  参考

  * [Common Desktop Environment Wiki](<https://sourceforge.net/p/cdesktopenv/wiki/Home/>)
