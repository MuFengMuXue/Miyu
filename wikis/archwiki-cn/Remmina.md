**翻译状态：**

  * 本文（或部分内容）译自 [Remmina](<https://wiki.archlinux.org/title/Remmina> "arch:Remmina")，最近一次同步于 2021-09-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/Remmina?diff=0&oldid=687390>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Remmina_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Rdesktop](</wzh/index.php?title=Rdesktop&action=edit&redlink=1> "Rdesktop（页面不存在）")
  * [xrdp](<../zh-cn/Xrdp.html> "Xrdp")

[Remmina](<https://remmina.org/>) 是用 [GTK](<../zh-cn/GTK.html> "GTK") 编写的远程桌面客户端，来自 [FreeRDP](<https://www.freerdp.com/>) 项目。 它支持以下协议：SSH、VNC、RDP、NX、XDMCP。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [remmina](<https://archlinux.org/packages/?name=remmina>)包。 

要支持 VNC 请安装 [libvncserver](<https://archlinux.org/packages/?name=libvncserver>)包 软件包。 

要支持 SPICE 请安装 [spice-gtk](<https://archlinux.org/packages/?name=spice-gtk>)包 软件包。 

如果你需要 RDP 支持，还要选择安装 [freerdp](<https://archlinux.org/packages/?name=freerdp>)包 或 [remmina-plugin-rdesktop](<https://aur.archlinux.org/packages/remmina-plugin-rdesktop/>)AUR。有关注意事项如下： 

  * 如果安装 [freerdp](<https://archlinux.org/packages/?name=freerdp>)包 之后 RDP 选项在 Remmina 下拉菜单中不可用，请首先确保完全退出 Remmina：执行 `killall remmina`。当你重启 Remmina 后，RDP 就应该可用了。
  * 对于 Remmina 1.2.0，有些用户报告使用 freerdp 的 RDP 连接存在频繁意外断开连接的问题，但 [rdesktop](</wzh/index.php?title=Rdesktop&action=edit&redlink=1> "Rdesktop（页面不存在）") RDP 连接则更为可靠。
  * 密码保存依赖于 [GNOME Keyring](<../zh-cn/GNOME_Keyring.html> "GNOME Keyring").

##  使用

要打开之前保存的连接配置你可以这样做： 
    
    $ remmina --connect=~/.remmina/file-name.remmina
    
根据你的设置不同，[dirname(1)](<https://man.archlinux.org/man/dirname.1>) 可能为 `~/.config/remmina/`，而不是 `~/.remmina/`。 

下面是脚本内容，它根据 `name=` 属性重命名了连接配置文件以其便于人类理解： 
    
    #!/bin/bash
    cd ~/.remmina/    # or ~/.config/remmina/ if appropriate
    ls -1 *.remmina | while read a; do
           N=`grep '^name=' "$a" | cut -f2 -d=`;
           [ "$a" == "$N.remmina" ] || mv "$a" "$N".remmina;
    done
    
要在启动时最小化到系统托盘，请使用 `-i`/`--icon` 选项。 

##  参考链接

  * [Remmina GitLab Repository](<https://gitlab.com/Remmina/Remmina>)
  * [FreeRDP Wiki](<https://github.com/FreeRDP/FreeRDP/wiki>)
