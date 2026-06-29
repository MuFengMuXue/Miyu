**翻译状态：**

  * 本文（或部分内容）译自 [PAM](<https://wiki.archlinux.org/title/PAM> "arch:PAM")，最近一次同步于 2024-02-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/PAM?diff=0&oldid=790245>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PAM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Security](<../zh-cn/%E5%AE%89%E5%85%A8.html> "Security")
  * [pam_mount](</wzh/index.php?title=Pam_mount&action=edit&redlink=1> "Pam mount（页面不存在）")
  * [pam_usb](</wzh/index.php?title=Pam_usb&action=edit&redlink=1> "Pam usb（页面不存在）")
  * [pam_abl](</wzh/index.php?title=Pam_abl&action=edit&redlink=1> "Pam abl（页面不存在）")
  * [pam_oath](<../zh-cn/Pam_oath.html> "Pam oath")
  * [Universal 2nd Factor](<../zh-cn/Universal_2nd_Factor.html> "Universal 2nd Factor")
  * [认证管理](<../zh-cn/%E8%BA%AB%E4%BB%BD%E7%AE%A1%E7%90%86.html> "认证管理")

Linux PAM ([Pluggable Authentication Modules](<https://github.com/linux-pam/linux-pam>)) 是一个系统级用户认证框架。如下描述引用自[项目介绍](<https://web.archive.org/web/20220402070708/http://linux-pam.org/whatispam.html>): 

    PAM 将程序开发与认证方式进行分离，程序在运行时调用附加的“认证”模块完成自己的工作。本地系统管理员通过配置选择要使用哪些认证模块。

本文描述在 Arch Linux 下为本地和远端用户配置 PAM 权限的方式方法。具体的细节配置方法将在专门的文章内展开。 

##  安装

[pam](<https://archlinux.org/packages/?name=pam>)包 包依赖于[base](<https://archlinux.org/packages/?name=base>)包 [meta package](<../zh-cn/Meta_package.html> "Meta package")，默认已经安装在系统。PAM 模块被放置于 `/usr/lib/security` 目录 

软件源中另外还包括其它一些可选的 PAM 包，详见 [#配置方法](<#%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95>)

##  配置

`/etc` 目录有多个子目录与 PAM 相关，使用命令 `pacman --query --list pam | grep /etc` 查看默认创建的配置文件。这些配置与 [#安全性参数](<#%E5%AE%89%E5%85%A8%E6%80%A7%E5%8F%82%E6%95%B0>)或 [#PAM 基础配置](<#PAM_%E5%9F%BA%E7%A1%80%E9%85%8D%E7%BD%AE>)有关。 

###  安全性参数

`/etc/security` 包含了对认证方法参数的系统级配置，安装后的文件与软件开发方默认配置一致。 

注意 Arch Linux 没有对这些文件进行定制。例如 `/etc/security/pwquality.conf` 配置可用于系统级别默认的密码认证方式，但需要手动将 `pam_pwquality.so` 模块加入到 [#PAM 基础配置](<#PAM_%E5%9F%BA%E7%A1%80%E9%85%8D%E7%BD%AE>)内。 

详见 [#安全性参数配置](<#%E5%AE%89%E5%85%A8%E6%80%A7%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE>)。 

###  PAM 基础配置

`/etc/pam.d/` 目录专门用于存放 PAM 配置，用于为具体的应用程序设置独立的认证方式。配置文件由以下安装包提供： 

  * [pambase](<https://archlinux.org/packages/?name=pambase>)包 安装包，提供了 Arch Linux 中为应用程序使用的 PAM 基础配置文件
  * 其它基础安装包。例如 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 添加了为 _login_ 及其它一些应用的认证配置， [shadow](<https://archlinux.org/packages/?name=shadow>)包 安装包为 Arch Linux 提供默认的用户数据库认证方式（参见[Users and groups](<../zh-cn/Users_and_groups.html> "Users and groups")）

不同的安装包的配置文件都被放在该目录，在运行时被不同的应用程序加载。例如，在用户登录时， _login_ 程序将加载 `system-local-login` 策略，具体过程如下： 
    
    /etc/pam.d/
    
    login -> system-local-login -> system-login -> system-auth

不同的应用程序，可能使用不同的配置文件。例如，[openssh](<https://archlinux.org/packages/?name=openssh>)包 安装其 `sshd` PAM 策略，如下所示： 
    
    /etc/pam.d/
    
    sshd -> system-remote-login -> system-login -> system-auth

配置文件的选择与应用程序有关。一种特定的认证方式可能仅用到 `sshd`，远程登录用到 `system-remote-login`，对这两者的修改不用影响到本地登录（local logins）。而对 `system-login` 或 `system-auth` 的修改将同时对 local 和 remote 的登录产生影响。 

如 `sshd` 的例子，任何 **pam-aware** 的应用程序需要将它的认证策略安装到 `/etc/pam.d` 目录下，以更集成和使用 PAM 提供的功能。否则应用程序将使用默认配置 `/etc/pam.d/other`。 

**提示：** PAM 是在运行过程中被动态链接使用的，例如 
    
    $ ldd /usr/bin/login |grep pam
    
    libpam.so.0 => /usr/lib/libpam.so.0 (0x000003d8c32d6000)
    libpam_misc.so.0 => /usr/lib/libpam_misc.so.0 (0x000003d8c30d2000)

_login_ 程序是 pam-aware 的，因此 **必需** 指定一个认证策略。

PAM 手册 _pam(8)_ 和 _pam.d(5)_ 描述了配置文件的标准规范。手册分四部分：账户，认证，密码和会话管理，同时还包括了配置项的可选内容。 

此外，文档 `/usr/share/doc/Linux-PAM/index.html` 包含多种指导文档，包括了每种标准模块的 man 手册。 

**警告：** 对 PAM 配置的修改会影响用户认证。不正确的修改可能导致**没有用户** 可以登录，或**所有用户** 都可以登录。

**提示：** 更改对于已通过身份验证的用户无效；使用 PAM 的一种方法是最好在测试机器上本地登录并进行开发，保持会话不断运行，同时检查另一个控制台上另一个用户的结果。

####  示例

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** (1) the use of nullok (2) the way pam handles optional modules（在 [Talk:PAM#Accuracy of PAM#Examples](</wzh/index.php?title=Talk:PAM&action=edit&redlink=1> "Talk:PAM（页面不存在）") 中讨论）

下所的两个小例子用于**反面示例** : 

首先是下面两行配置： 
    
    /etc/pam.d/system-auth
    
    auth      required  pam_unix.so     try_first_pass nullok
    auth      optional  pam_permit.so

[pam_unix(8)](<https://man.archlinux.org/man/pam_unix.8>) 说明如下：“本认证 （ `pam_unix.so` ）用于检查用户密码作为认证。默认情况不允许密码为空的用户进入”。而 `pam_permit.so` 允许密码为空的情况。如果将 `rerquired` 和 `optional` 交换位置，则两种情况都将允许无密码登录。 

第二种情况恰好相反，在 /etc/pam.d/login 中的`pam_nologin.so` 默认配置创建如下文件： 
    
    # touch /etc/nologin
    
将导致只有 root 用户可以登录（Arch Linux 默认允许 root 用户登录）。要让普通用户可以登录，则需要删除该文件，可能是从创建它的控制台。 

参考 [#PAM stack and module configuration](<#PAM_stack_and_module_configuration>)来对具体使用进行配置。 

##  配置方法

本节简要说明如何修改 PAM 配置，如何添加新的 PAM 模块。具体的模块 man 手册与模块名一致（去掉 `.so` 后缀） 

###  安全性参数配置

下面的章节描述如何修改 PAM 默认参数配置： 

  * [安全#用 pam_pwquality 强制使用强密码](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E7%94%A8_pam_pwquality_%E5%BC%BA%E5%88%B6%E4%BD%BF%E7%94%A8%E5%BC%BA%E5%AF%86%E7%A0%81> "安全")

    展示如何使用 `pam_crackib.so` 强制密码认证。

  * [安全#在三次登录尝试失败后封锁用户](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E5%9C%A8%E4%B8%89%E6%AC%A1%E7%99%BB%E5%BD%95%E5%B0%9D%E8%AF%95%E5%A4%B1%E8%B4%A5%E5%90%8E%E5%B0%81%E9%94%81%E7%94%A8%E6%88%B7> "安全")

    展示如何使用 `pam_tally.so` 限制登录。

  * [安全#仅允许特定用户](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E4%BB%85%E5%85%81%E8%AE%B8%E7%89%B9%E5%AE%9A%E7%94%A8%E6%88%B7> "安全")

    展示使用 `pam_wheel.so` 限制用户登录 。

  * [实时进程管理#配置PAM](<../zh-cn/%E5%AE%9E%E6%97%B6%E8%BF%9B%E7%A8%8B%E7%AE%A1%E7%90%86.html#%E9%85%8D%E7%BD%AEPAM> "实时进程管理") 和[安全#限制进程数量](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E9%99%90%E5%88%B6%E8%BF%9B%E7%A8%8B%E6%95%B0%E9%87%8F> "安全")

    描述如何使用 `pam_limits.so` 来配置系统进程。

  * [环境变量#使用 pam_env](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html#%E4%BD%BF%E7%94%A8_pam_env> "环境变量")

    包含了用 `pam_env.so` 设置环境变量的示例。

### PAM stack and module configuration

下面的章节说明对于具体的模块，如何修改 [#PAM 基础配置](<#PAM_%E5%9F%BA%E7%A1%80%E9%85%8D%E7%BD%AE>)

  * [pam_mount](</wzh/index.php?title=Pam_mount&action=edit&redlink=1> "Pam mount（页面不存在）")

     `pam_mount.so` 在用户登录时自动挂载加密目录

  * [ECryptfs#Auto-mounting](</wzh/index.php?title=ECryptfs&action=edit&redlink=1> "ECryptfs（页面不存在）")

     `pam_ecryptfs.so` 自动挂载加密目录

  * [Dm-crypt/Mounting at login](</wzh/index.php?title=Dm-crypt/Mounting_at_login&action=edit&redlink=1> "Dm-crypt/Mounting at login（页面不存在）")

     `pam_exec.so` 在用户登录时执行自定义脚本

  * [Active Directory integration#Configuring PAM](</wzh/index.php?title=Active_Directory_integration&action=edit&redlink=1> "Active Directory integration（页面不存在）")

    使用 `pam_winbind.so` 和 `pam_krb5.so` 通过 Active Directory ([LDAP](<../zh-cn/OpenLDAP.html> "LDAP"), [Kerberos](<../zh-cn/Kerberos.html> "Kerberos")) 服务进行用户认证

  * [LDAP 认证#PAM 配置](<../zh-cn/LDAP_%E8%AE%A4%E8%AF%81.html#PAM_%E9%85%8D%E7%BD%AE> "LDAP 认证")

     `pam_ldap.so` 介绍集成 LDAP 主对端认证过程

  * [YubiKey#Linux user authentication with PAM](<../zh-cn/YubiKey.html#Linux_user_authentication_with_PAM> "YubiKey")

    描述如何使用 U2F (`pam_u2f.so`) 和 YubiKey 与 PAM 提供的专有 Yubico OTP 实现 (`pam_yubico.so`)

  * [pam_oath](<../zh-cn/Pam_oath.html> "Pam oath")

     `pam_oath.so` 软件方式的 two-factor 认证

  * [fprint](<../zh-cn/Fprint.html> "Fprint")

    使用 `pam_fprintd.so` 进行指纹认证.

  * [pam_autologin](</wzh/index.php?title=Pam_autologin&action=edit&redlink=1> "Pam autologin（页面不存在）") : saves username and password to log in automatically.
  * [pam_usb](</wzh/index.php?title=Pam_usb&action=edit&redlink=1> "Pam usb（页面不存在）")

     `pam_usb.so` 通过 USB 设备进行认证

  * [SSH keys#pam_ssh](<../zh-cn/SSH_keys.html#pam_ssh> "SSH keys")

     `pam_ssh.so` 认证远端用户

  * [pam_abl](</wzh/index.php?title=Pam_abl&action=edit&redlink=1> "Pam abl（页面不存在）")

     `pam_abl.so` 限制通过 ssh 的暴力攻击

  * [EncFS](</wzh/index.php?title=EncFS&action=edit&redlink=1> "EncFS（页面不存在）")

     `pam_encfs.so` 实现自动挂载加密目录

  * [Google Authenticator](<../zh-cn/Google_Authenticator.html> "Google Authenticator")

     `pam_google_authenticator.so` two-factor 认证

  * [Very Secure FTP Daemon#PAM with virtual users](<../zh-cn/Very_Secure_FTP_Daemon.html#PAM_with_virtual_users> "Very Secure FTP Daemon")

     `pam_pwdfile.so` 认证非本地用户的 FTP 登录和 chroot 限制

##  更多 PAM 包

除了上面提到的安装包，[Arch User Repository](<../zh-cn/Arch_User_Repository.html> "Arch User Repository") 包括更多的 PAM 模块和工具。 

PAM 相关的通用工具有： 

  * **[Pamtester](<https://linux.die.net/man/1/pamtester>)** — PAM 测试工具集

     <https://pamtester.sourceforge.net/> || [pamtester](<https://aur.archlinux.org/packages/pamtester/>)AUR

Note the AUR features a keyword tag for [PAM](<https://aur.archlinux.org/packages/?SeB=k&K=pam>), but not all available packages are updated to include it. Hence, searching the [package description](<https://aur.archlinux.org/packages/?K=pam>) may be necessary. 

##  参阅

  * [linux-pam.org](<http://www.linux-pam.org/>) \- The project homepage
  * [Understanding and configuring PAM](<https://web.archive.org/web/20211124031525/https://developer.ibm.com/tutorials/l-pam/>) \- An introductory article
