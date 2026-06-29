**翻译状态：**

  * 本文（或部分内容）译自 [Plasma Login Manager](<https://wiki.archlinux.org/title/Plasma_Login_Manager> "arch:Plasma Login Manager")，最近一次同步于 2026-02-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Plasma_Login_Manager?diff=0&oldid=866205>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Plasma_Login_Manager_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")
  * [KDE](<../zh-cn/KDE.html> "KDE")

[Plasma Login Manager](<https://invent.kde.org/plasma/plasma-login-manager/>) 是 [SDDM](<../zh-cn/SDDM.html> "SDDM") 的一个分支，拥有全新的提供欢迎界面，壁纸插件集成以及系统设置模块（KCM）的前端。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [plasma-login-manager](<https://archlinux.org/packages/?name=plasma-login-manager>)包，然后根据[显示管理器#加载显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html#%E5%8A%A0%E8%BD%BD%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8> "显示管理器")的说明配置 Plasma Login 在系统引导时启动。 

**提示：** 如果从 SDDM 迁移过来，请先 [禁用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "禁用") sddm.service 。 

迁移完成后，你还可以以 root 用户身份使用命令 userdel -r sddm 清理并删除不再使用的 sddm 用户。

##  配置

默认的配置文件在 `/usr/lib/plasma-login/defaults.conf`。要修改配置，请创建 `/etc/plasmalogin.conf` 或 `/etc/plasmalogin.conf.d/`。 

一切东西都应该开箱即用，自从 Arch Linux 使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 后，Plasma Login 默认使用 systemd-logind 以进行会话管理。 

###  自动登录

Plasma Login 通过它的配置文件来支持自动登录，例如： 
    
    /etc/plasmalogin.conf.d/autologin.conf
    
    [Autologin]
    User=john
    Session=plasma.desktop

此配置使得在系统启动后自动以用户 john 开启一个 KDE Plasma 会话。X 的会话类型位于 `/usr/share/xsessions/`， wayland 的会话类型位于 `/usr/share/wayland-sessions/`。 

要在登录 KDE Plasma 的同时锁定会话，请参阅 [KDE#锁屏](<../zh-cn/KDE.html#%E9%94%81%E5%B1%8F> "KDE")。 

###  无密码登录

可以配置 Plasma Login 以允许在不需要密码的情况下登录到某些账户。与自动登录不同，用户仍需要选择要登录的账户，并且它与简单地将账户密码设置为空字符串不同，因为它只允许交互式用户登录（而不是，例如，通过 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 远程登录的用户）。 

Plasma Login 通过 [PAM](<../zh-cn/PAM.html> "PAM") 运行，因此您必须配置 PAM 的 Plasma Login 配置： 
    
    /etc/pam.d/plasmalogin
    
    #%PAM-1.0
    **auth        sufficient  pam_succeed_if.so user ingroup nopasswdlogin**
    auth        include     system-login
    ...

也是为了能在没有密码的情况下解锁 KDE Plasma 锁屏，同样在/etc/pam.d/kde文件的顶部添加相同的行： 
    
    /etc/pam.d/kde
    
    #%PAM-1.0
    **auth        sufficient  pam_succeed_if.so user ingroup nopasswdlogin**
    auth        include     system-login
    ...

然后，只有 `nopasswdlogin` 组的成员，才能在不输入密码的情况下交互式登录： 
    
    # groupadd -r nopasswdlogin
    # gpasswd -a _username_ nopasswdlogin
    
###  登录后自动解锁 Kwallet

详见 [KDE Wallet#登录时自动解锁 Kwallet](<../zh-cn/KDE_Wallet.html#%E7%99%BB%E5%BD%95%E6%97%B6%E8%87%AA%E5%8A%A8%E8%A7%A3%E9%94%81_Kwallet> "KDE Wallet")。 
