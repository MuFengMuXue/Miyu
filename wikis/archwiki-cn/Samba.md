相关文章

  * [Active Directory Integration](</wzh/index.php?title=Active_Directory_Integration&action=edit&redlink=1> "Active Directory Integration（页面不存在）")
  * [Samba/Active Directory domain controller](<../zh-cn/Samba/Active_Directory_domain_controller.html> "Samba/Active Directory domain controller")
  * [NFS](<../zh-cn/NFS.html> "NFS")

**翻译状态：**

  * 本文（或部分内容）译自 [Samba](<https://wiki.archlinux.org/title/Samba> "arch:Samba")，最近一次同步于 2024-04-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Samba?diff=0&oldid=805891>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Samba_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Samba](<https://www.samba.org/>) 是用于 Linux 和 Unix的标准 Windows 互操作性程序套件。自 1992 年以来，Samba 为所有使用 [SMB/CIFS](<https://en.wikipedia.org/wiki/Server_Message_Block> "wikipedia:Server Message Block") 协议的客户端提供了安全、稳定和快速的文件和打印服务，例如所有版本的 DOS 和 Windows、OS/2、Linux 和许多其他系统。 

要通过 Samba 共享文件，请参阅[#服务器](<#%E6%9C%8D%E5%8A%A1%E5%99%A8>)部分；要访问其他机器上通过 Samba 共享的文件，请参见[#客户端](<#%E5%AE%A2%E6%88%B7%E7%AB%AF>)部分。 

##  服务器

###  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [samba](<https://archlinux.org/packages/?name=samba>)包 软件包。 

Samba 服务的配置文件是 `/etc/samba/smb.conf`，[smb.conf(5)](<https://man.archlinux.org/man/smb.conf.5>)提供了详细的文档。 

[samba](<https://archlinux.org/packages/?name=samba>)包 软件包没有提供此文件，启动 `smb.service` 前需要先创建这个文件。 

从 [Samba 的 Git 仓库](<https://git.samba.org/samba.git/?p=samba.git;a=blob_plain;f=examples/smb.conf.default;hb=HEAD>)可以获取到示例文件 `smb.conf.default`，可参考其配置 `/etc/samba/smb.conf`。 

**注意：**

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 参见 [Talk:Samba#logging to systemd](</wzh/index.php?title=Talk:Samba&action=edit&redlink=1> "Talk:Samba（页面不存在）")。 (在[Talk:Samba](<../zh-cn/Talk:Samba.html>)讨论)

  * 从上面获取的默认配置文件里把日志 `log file` 设置到一个不能写的地方，这会引起错误。下列任一办法可以解决这个问题： 
    * 把日志文件配置到可写的路径：`log file = /var/log/samba/%m.log`
    * 把日志存到非文件后端：`logging = syslog` 配合 `syslog only = yes`，或者使用 `logging = systemd`
  * 如果需要的话；在 `[global]` 部分中指定的 `workgroup` 需要对应 Windows 工作组的名称 (默认是 `WORKGROUP`)。
  * 默认配置会将用户的主目录以可写权限暴露到网络上。如果你担心该操作导致的安全问题，可以考虑将 `[homes]` 一节完全注释掉。详细信息可参考 [smb.conf(5) § The [homes] section](<https://man.archlinux.org/man/smb.conf.5#The_%5Bhomes%5D_section>)。

**提示：** 修改 `smb.conf` 文件后，运行 [testparm(1)](<https://man.archlinux.org/man/testparm.1>) 命令看看有没有语法错误。

####  启用并启动服务

要通过 SMB 提供基础文件共享服务，请[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `smb.service`。详情请参考 [smbd(8)](<https://man.archlinux.org/man/smbd.8>)。 

如果你要让服务器可通过 NetBIOS 主机名访问，需在 `smb.conf` 中的 `netbios name` 选项配置目标名称，并[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `nmb.service`。详情请参考 [smbd(8)](<https://man.archlinux.org/man/smbd.8>)。 

**注意：** 无需用到 `nmb.service`。但对于部分主机，需要该服务才能通过主机名（例如 `smb://hostname/`）访问 Samba 服务器。如果你的网络中只包含运行 Windows 10 及更高版本的设备，可以考虑[同时安装 WSD 守护进程](<#Windows_1709_%E5%8F%8A%E6%9B%B4%E9%AB%98%E7%89%88%E6%9C%AC%E6%97%A0%E6%B3%95%E5%9C%A8%E2%80%9C%E7%BD%91%E7%BB%9C%E2%80%9D%E8%A7%86%E5%9B%BE%E4%B8%AD%E5%8F%91%E7%8E%B0_Samba_%E6%9C%8D%E5%8A%A1%E5%99%A8>)来使你的服务器出现在“网络”视图中。

####  使服务器可被发现

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [avahi](<https://archlinux.org/packages/?name=avahi>)包 软件包， 然后[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `avahi-daemon.service` 以通过 [Zeroconf](</wzh/index.php?title=Zeroconf&action=edit&redlink=1> "Zeroconf（页面不存在）") 使 Samba 服务器可被发现。这应当在多数非 Windows 文件管理器上可用（macOS Finder，Linux 和 BSD 上各种基于 GUI 的文件管理器，等等）。 

如果 `avahi-daemon.service` 尚未运行，服务器仍可被访问，仅不可被发现。也就是说，它不会出现在文件管理器中，但你仍可直接通过 IP 或者域名连接它。 

Windows 资源管理器单独依赖 WS-Directory 协议；参见 [#Windows 1709 及更高版本无法在“网络”视图中发现 Samba 服务器](<#Windows_1709_%E5%8F%8A%E6%9B%B4%E9%AB%98%E7%89%88%E6%9C%AC%E6%97%A0%E6%B3%95%E5%9C%A8%E2%80%9C%E7%BD%91%E7%BB%9C%E2%80%9D%E8%A7%86%E5%9B%BE%E4%B8%AD%E5%8F%91%E7%8E%B0_Samba_%E6%9C%8D%E5%8A%A1%E5%99%A8>)。 

####  配置防火墙

如果使用了[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")，请记得打开需要的端口（通常是 137-139 + 445）。完整列表请查看 [Samba 所需端口](<https://www.samba.org/~tpot/articles/firewall.html>)。 

#####  UFW 规则

SMB/CIFS 的 UFW 应用程序配置文件在安装 [Ufw](<../zh-cn/Uncomplicated_Firewall.html> "Ufw") 时已默认包含在 `/etc/ufw/applications.d/ufw-fileserver` 中。 

使用 root 执行 `ufw allow CIFS` 。 

如果您删除了配置文件，请创建/编辑 /etc/ufw/applications.d/samba 并添加以下内容： 
    
    [Samba]
    title=LanManager-like file and printer server for Unix
    description=The Samba software suite is a collection of programs that implements the SMB/CIFS protocol for unix systems, allowing you to serve files and printers to Windows, NT, OS/2 and DOS clients. This protocol is sometimes also referred to as the LanManager or NetBIOS protocol.
    ports=137,138/udp|139,445/tcp
    
Then load the profile into UFW run `ufw app update Samba` as root. 

Then finally, allow Samba by running `ufw allow Samba` as root. 

#####  firewalld 服务

To configure [firewalld](<../zh-cn/Firewalld.html> "Firewalld") to allow Samba in the **home** zone, run: 
    
    # firewall-cmd --permanent --add-service={samba,samba-client,samba-dc} --zone=home
    
The three services listed are: 

  * `samba`: for sharing files with others.
  * `samba-client`: to browse shares on other machines on the network.
  * `samba-dc`: for [Samba/Active Directory domain controller](<../zh-cn/Samba/Active_Directory_domain_controller.html> "Samba/Active Directory domain controller").

`--permanent` ensures the changes remain after `firewalld.service` is [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart")ed. 

###  基础配置

####  用户管理

下列章节描述了如何创建本地（tdbsam）Samba 用户数据库。出于用户验证及其他用途，Samba 也可以被绑定到一个 Active Directory 域中，或是自己作为 Active Directory 域控制器，或者被用作 LDAP 服务器。 

#####  添加用户

Samba 需要 Linux 账户才能使用 - 可以使用已有账户或[创建新用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86> "用户和用户组")。 

**注意：**[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户")/[用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组") _nobody_ 应已在系统中创建。它被作为默认`来宾账户`，可用于包含 `guest ok = yes` 的共享，使得用户无需登录即可使用该共享。

虽然 Samba 和 Linux 系统共享用户名，但 Samba 使用单独的密码管理。将下面的 `samba_user` 替换为选择的 Samba 用户: 
    
    # smbpasswd -a _samba_user_
    
根据[服务器角色](<https://www.samba.org/samba/docs/man/manpages-3/smb.conf.5.html#SERVERROLE>)的差异，可能需要为 Samba 用户账户修改已有的[文件权限与属性](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "文件权限与属性")。 

要让新创建的用户仅能访问 Samba 远程文件服务器，可以禁用其它登录选项： 

  * 禁用 shell - `usermod --shell /usr/bin/nologin --lock _samba_user_`
  * 禁用 SSH 登录 - 编辑 `/etc/ssh/sshd_config` 文件，修改 `AllowUsers` 选项

另请参阅[安全](<../zh-cn/%E5%AE%89%E5%85%A8.html> "安全")一文来加固系统。 

#####  查询用户

使用 [pdbedit(8)](<https://man.archlinux.org/man/pdbedit.8>) 命令查询现有用户： 
    
    # pdbedit -L -v
    
#####  更改 samba 用户的密码

使用 `smbpasswd` 修改 samba 用户的密码： 
    
    # smbpasswd _samba_user_
    
####  创建匿名共享

1\. 创建新 Linux 用户，匿名 Samba 用户将映射到该用户。 
    
    # useradd guest -s /bin/nologin
    
**注意：** 用户名可以是任意合规 Linux 用户名，不限于“guest”。该用户不需要作为 Samba 用户。

2\. 在 `/etc/samba/smb.conf` 添加下列内容： 
    
    /etc/samba/smb.conf
    
    ...
    [global]
    security = user
    map to guest = bad user
    guest account = guest
    
    [guest_share]
        comment = guest share
        path = /tmp/
        public = yes
        only guest = yes
        writable = yes
        printable = no

现在匿名用户将被映射到 Linux 用户 `guest`，并可以访问 `guest_share.path` 中定义的任何目录，在该例子中为 `/tmp/`。 

**注意：** 共享名称不一定要包含“guest”，它可以是任何合规 Samba 共享名称。

请确保 Linux 用户 `guest` 拥有访问 `guest_share.path` 中文件的相应权限。 

另外，请确保共享已正确按照 [smb.conf.default](<https://git.samba.org/samba.git/?p=samba.git;a=blob_plain;f=examples/smb.conf.default;hb=HEAD>) 中的 _Share Definitions_ 一节进行配置。 

###  高级配置

#### Enable symlink following

**警告：** Enabling the `follow symlinks` option can be a security risk.
    
    /etc/samba/smb.conf
    
    ...
    [global]
       follow symlinks = yes
       wide links = yes
       unix extensions = no

Then, [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `smb.service`. 

**注意：** When using [AppArmor](<../zh-cn/AppArmor.html> "AppArmor"), if the symlink points to a directory outside the user's home or the [usershare](<#Enable_Usershares>) directory, then you need to [modify the AppArmor profile permissions](<#Permission_issues_on_AppArmor>).

####  为 macOS 客户端启用服务端复制

服务端复制使得在服务端复制文件时不需要在服务器及客户端间进行数据传输。该选项默认启用，但在 macOS 客户端下无效。如果你有 macOS 客户端，需要将下面的配置添加到 `smb.conf`，然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `smb.service`。 
    
    /etc/samba/smb.conf
    
    ...
    [global]
       fruit:copyfile = yes

####  启用 Usershare

**注意：** 此为可选功能，如无需要可以跳过。

Usershares 可以让不具有 root 权限的用户拥有进行添加、修改和删除自己的文件夹的操作权限。参见 [smb.conf(5) § USERSHARES](<https://man.archlinux.org/man/smb.conf.5#USERSHARES>)。 

  1. 为 usershares 创建目录：
         
         # mkdir /var/lib/samba/usershares

  2. 创建一个[用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")：
         
         # groupadd -r sambashare

  3. 将目录的所有者修改为 `root`，组修改为 `sambashare`：
         
         # chown root:sambashare /var/lib/samba/usershares

  4. 修改 `usershares` 目录的权限，使 `sambashare` 组中的用户可以创建文件。该命令同时配置了[黏着位](<https://en.wikipedia.org/wiki/Sticky_bit> "wikipedia:Sticky bit")，防止用户删除其他用户的 usershares：
         
         # chmod 1770 /var/lib/samba/usershares

在 `smb.conf` 配置文件中设置如下配置： 
    
    /etc/samba/smb.conf
    
    [global]
      usershare path = /var/lib/samba/usershares
      usershare max shares = 100
      usershare allow guests = yes
      usershare owner only = yes

将用户添加到 _sambashare_ 组，将 `_your_username_` 替换为你用户的名称： 
    
    # gpasswd sambashare -a _your_username_
    
[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `smb.service` 和 `nmb.service` 服务。 

注销并重新登录。 

如果你希望共享主目录下的路径，其必须允许 _others_ 组的用户访问。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 不确定该需求是否正确，也不确定指的是哪个路径：是 smb.conf 的 'usershare path' 选项路径还是共享目录的路径？（在 [Talk:Samba#permissions](</wzh/index.php?title=Talk:Samba&action=edit&redlink=1> "Talk:Samba（页面不存在）") 中讨论）

在 GUI 下，你可以使用 [Thunar](<../zh-cn/Thunar.html> "Thunar") 或 [Dolphin](<../zh-cn/Dolphin.html> "Dolphin") \- 右键点击任何目录，然后通过网络共享。 

在命令行下，使用下列任一命令，替换掉斜体的 _sharename_ ， _user_ ，...： 
    
    # net usershare add _sharename_ _abspath_ [_comment_] [_user_ :{R|D|F}] [guest_ok={y|n}]
    # net usershare delete _sharename_
    # net usershare list _wildcard-sharename_
    # net usershare info _wildcard-sharename_
    
####  设置并强制应用权限

权限可同时应用于服务器和共享： 
    
    /etc/samba/smb.conf
    
    [global]
      ;inherit owner = unix only ; Inherit ownership of the parent directory for new files and directories
      ;inherit permissions = yes ; Inherit permissions of the parent directory for new files and directories
      create mask = 0664
      directory mask = 2755
      force create mode = 0644
      force directory mode = 2755
      ...
    
    [media]
      comment = Media share accessible by _greg_ and _pcusers_
      path = _/path/to/media_
      valid users = _greg @pcusers_
      force group = _+pcusers_
      public = no
      writable = yes
      create mask = 0664
      directory mask = 2775
      force create mode = 0664
      force directory mode = 2775
    
    [public]
      comment = Public share where _archie_ has write access
      path = _/path/to/public_
      public = yes
      read only = yes
      write list = _archie_
      printable = no
    
    [guests]
      comment = Allow all users to read/write
      path = _/path/to/guests_
      public = yes
      only guest = yes
      writable = yes
      printable = no

参见 [smb.conf(5)](<https://man.archlinux.org/man/smb.conf.5>) 查看完整的可用权限标志和设置。 

####  限制协议以增强安全性

**警告：** 默认情况下，4.11 前的 Samba 版本允许使用过时和不安全的 SMB1 协议连接。使用这些版本时，强烈建议设置 `server min protocol = SMB2_02` 以保护自己免遭勒索软件攻击。在 Samba 4.11 及更新版本，SMB2 已是默认最低协议，因此不再需要此更改。

在 `/etc/samba/smb.conf` 中[添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Help:阅读") `server min protocol` 和 `server max protocol` 以强制最低和最高可用协议版本； 
    
    /etc/samba/smb.conf
    
    [global]
      server min protocol = SMB2_10
      ; server max protocol = SMB3

参见 [smb.conf(5)](<https://man.archlinux.org/man/smb.conf.5>) 中的 `server max protocol` 部分以获取所支持协议的概述。 

为了和旧版本的客户端和/或服务器兼容，你或许需要将 `client min protocol` 或 `server min protocol` 设置到旧一点的版本，但请注意你将更易于遭受攻击。 

**提示：** 当客户端只应使用最新的 SMB3 协议连接时，使用 `server min protocol = SMB3`，例如运行 Windows 10 及之后版本的客户端。

使用 `mount.cifs` 的[客户端](<#%E6%89%8B%E5%8A%A8%E6%8C%82%E8%BD%BD>)也许需要指定正确的 `vers=*`，例如： 
    
    # mount -t cifs //_SERVER_ /_sharename_ /mnt/_mountpoint_ -o username=_username_ ,password=_password_ ,iocharset=_utf8_ ,vers=_3.1.1_
    
参见 [mount.cifs(8)](<https://man.archlinux.org/man/mount.cifs.8>) 获取更多信息. 

####  使用原生 SMB 传输加密

原生 SMB 传输加密在 SMB 3.0 及更新版本可用。支持该类型加密的客户端包括 Windows 8 以及更新版本，Windows Server 2012 及更新版本，以及 Samba 4.1 及更新版本的 smbclient。 

为了默认使用原生 SMB 传输加密，需全局和/或按共享设置 `server smb encrypt` 参数。可用的值有`off`，`enabled`（默认值），`desired` 或 `required`： 
    
    /etc/samba/smb.conf
    
    [global]
      server smb encrypt = desired

To configure encryption for on the client side, use the option `client smb encrypt`. 

参见 [smb.conf(5)](<https://man.archlinux.org/man/smb.conf.5>) 获取更多信息，特别是**对 SMB1 的影响** 和**对 SMB2 的影响** 的段落。 

**提示：** 当 [#手动挂载](<#%E6%89%8B%E5%8A%A8%E6%8C%82%E8%BD%BD>) 一个共享时，指定 `seal` 挂载选项以强制使用加密。

####  禁用打印机共享

默认情况下 Samba 会共享由 [CUPS](<../zh-cn/CUPS.html> "CUPS") 设置的打印机。 

如果你不想打印机被共享，使用以下设置： 
    
    /etc/samba/smb.conf
    
    [global]
      load printers = no
      printing = bsd
      printcap name = /dev/null
      disable spoolss = yes
      show add printer wizard = no

####  防止 Samba 共享特定后缀的文件

**注意：** 设置这项参数会影响 Samba 的性能，因为它会被强制要求检查所有扫描到的文件和目录是否匹配要求。

Samba 提供了一个选项以屏蔽满足特定命名模式的文件，比如文件扩展名。该选项可用于防止病毒传播或阻止用户用特定的文件浪费空间。更多关于此选项的信息可在 [smb.conf(5)](<https://man.archlinux.org/man/smb.conf.5>) 找到。 
    
    /etc/samba/smb.conf
    
    ...
    [myshare]
      comment = Private
      path = /mnt/data
      read only = no
      veto files = /*.exe/*.com/*.dll/*.bat/*.vbs/*.tmp/*.mp3/*.avi/*.mp4/*.wmv/*.wma/

####  提高吞吐量

**警告：** 注意，下列操作有可能会造成损坏/连接问题，可能会损坏你的 TCP/IP 栈。

默认设置应满足多数用户的用例。虽然正确配置 'socket options' 可以提升性能，但错误配置也会同比例降低性能。在进行大幅更改前请确保进行了测试。 

在应用下列任何配置前请阅读 [smb.conf(5)](<https://man.archlinux.org/man/smb.conf.5>) 文档。 

下列设置需要[附加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Append")到 `/etc/samba/smb.conf` 的 `[global]` 一节中。 

设置 deadtime 可防止大量非活跃连接消耗系统资源： 
    
    deadtime = 30
    
sendfile 可能会更高效利用 CPU 资源，让 Samba 变得更快： 
    
    use sendfile = yes
    
配置最低 receivefile 大小可以利用零复制直接从网络套接字缓冲区写入到操作系统缓存（如果可用）。这一操作可能会提高性能，但建议用户进行测试： 
    
    min receivefile size = 16384
    
提高接收/发送缓存大小及配置套接字优化标志可能有助于提升吞吐量。由于在某些网络下可能会出现问题，建议对各个标志进行单独测试： 
    
    socket options = IPTOS_LOWDELAY TCP_NODELAY IPTOS_THROUGHPUT SO_RCVBUF=131072 SO_SNDBUF=131072
    
**注意：** 部分选项可能需要调整网络接口，详见 [Sysctl#网络](<../zh-cn/Sysctl.html#%E7%BD%91%E7%BB%9C> "Sysctl")。

####  Enable access for old clients/devices

Latest versions of Samba no longer offer older authentication methods and protocols which are still used by some older clients (IP cameras, etc). These devices usually require Samba server to allow NTMLv1 authentication and NT1 version of the protocol, known as CIFS. For these devices to work with latest Samba, you need to add these two configuration parameters into `[global]` section: 
    
    server min protocol = NT1
    ntlm auth = yes
    
Anonymous/guest access to a share requires just the first parameter. If the old device will access with username and password, you also need the add the second line too. 

#### Enable Spotlight searching

Spotlight allows supporting clients (e.g. MacOS Finder) to quickly search shared files. 

Install and start/enable [OpenSearch](</wzh/index.php?title=OpenSearch&action=edit&redlink=1> "OpenSearch（页面不存在）"). Install [fs2es-indexer](<https://aur.archlinux.org/packages/fs2es-indexer/>)AUR, configure the directories you want to index in `/etc/fs2es-indexer/config.yml`, and start/enable `fs2es-indexer.service` for periodic indexing. 

Edit `smb.conf` as described in the [Samba wiki](<https://wiki.samba.org/index.php/Spotlight_with_Elasticsearch_Backend#Samba>) to enable Spotlight per share, and restart `smb.service` to apply the changes. 

##  客户端配置

要使用类似 `ftp` 的命令行界面，请安装软件包 [smbclient](<https://archlinux.org/packages/?name=smbclient>)包。常用命令请参考 [smbclient(1)](<https://man.archlinux.org/man/smbclient.1>)。 

如需更轻量级的替代品（没有可用共享查询等功能），可[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [cifs-utils](<https://archlinux.org/packages/?name=cifs-utils>)包，其提供了 `/usr/bin/mount.cifs`。 

部分[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")可能提供了图形界面，搭配文件管理器的用法请参考[#文件管理器配置](<#%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E9%85%8D%E7%BD%AE>)。 

**注意：**

  * [smbclient](<https://archlinux.org/packages/?name=smbclient>)包 requires a `/etc/samba/smb.conf` file (see [#Installation](<#Installation>)), which you can create as an empty file using the `touch` utility.
  * 安装 [cifs-utils](<https://archlinux.org/packages/?name=cifs-utils>)包 或 [smbclient](<https://archlinux.org/packages/?name=smbclient>)包 后，请加载 `cifs` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块") 或重启以避免挂载失败。

###  显示可用共享

下面命令会显示服务器上的可用共享: 
    
    $ smbclient -L _hostname_ -U%
    
_smbtree_ 可用显示共享目录树，不建议再有大量计算机的网络上使用此功能。可用它检查共享名是否可用。 

另外，使用 `$ smbtree -N` 会以树状图显示所有可用共享，它使用了广播查询，因此不建议在有大量设备的网络中使用，但有助于检查共享名是否可用。使用 `-N`（`-no-pass`）选项可以忽略密码输入请求。 

**注意：**`smbtree` 使用了 SMB1 和 NetBIOS，意味着它们必须已在服务器上启用，且需要在客户端的 `smb.conf` 文件中设置 `client min protocol = NT1`，否则 `smbtree` 只会显示空输出。

###  NetBIOS/WINS 主机名

Samba clients handle NetBIOS host names automatically by default (the behavior is controlled by the `name resolve order` option in `smb.conf`). Other programs (including `mount.cifs`) typically use [Name Service Switch](</wzh/index.php?title=Name_Service_Switch&action=edit&redlink=1> "Name Service Switch（页面不存在）"), which does not handle NetBIOS by default. 

The [smbclient](<https://archlinux.org/packages/?name=smbclient>)包 package provides a libnss driver to resolve NetBIOS host names. To use it, [install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") it along with the [samba](<https://archlinux.org/packages/?name=samba>)包 package (which provides the _winbindd_ daemon), [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `winbind.service` and add `wins` to the `hosts` line in [nsswitch.conf(5)](<https://man.archlinux.org/man/nsswitch.conf.5>): 
    
    /etc/nsswitch.conf
    
    ...
    hosts: mymachines resolve [!UNAVAIL=return] files myhostname dns **wins**
    ...

**注意：** Due to a current mistake in `winbind.service`, you may have to modify the unit file as described in this [bug-report](<https://bugs.launchpad.net/ubuntu/+source/samba/+bug/1789097>)

Now, during host resolving (e.g. when using `mount.cifs` or just `ping _netbios-name_`), _winbindd_ will resolve the host name by sending queries using NetBIOS Name Service (NBNS, also known as WINS) protocol. 

By default it sends a broadcast query to your local network. If you have a WINS server, you can add `wins server = _wins-server-ip_` to `smb.conf` and [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `winbind.service`, then _winbindd_ and other Samba clients will send unicast queries to the specified IP. 

If you want to resolve your local host name (specified in the `netbios name` option in `smb.conf`), [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `nmb.service`, which will handle incoming queries. 

You can test WINS resolution with `nmblookup`. By default it sends broadcast queries to your local network regardless of the `wins server` option. 

Note that WINS resolution requires incoming traffic originating from port 137. 

####  Disable NetBIOS/WINS support

When not using NetBIOS/WINS host name resolution, it may be preferred to disable this protocol: 
    
    /etc/samba/smb.conf
    
    [global]
      disable netbios = yes
      dns proxy = no

Finally [disable](</wzh/index.php?title=Disable&action=edit&redlink=1> "Disable（页面不存在）")/[stop](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Stop") `winbind.service`. 

###  手动挂载

使用 `mount.cifs` 作为挂载类型 `type`，下面列出的选项并不是全部都需要： 
    
    # mount --mkdir -t cifs //_SERVER_ /_sharename_ /mnt/_mountpoint_ -o username=_username_ ,password=_password_ ,workgroup=_workgroup_ ,iocharset=_utf8_ ,uid=_username_ ,gid=_group_
    
其中 `uid` 和 `gid` 对应了被授予特定路径读写权限的本地（例如客户端）[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户")/[用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")。 

**注意：**

  * If the `uid` and `gid` being used does not match the user of the server, the `forceuid` and `forcegid` options may be helpful. However note permissions assigned to a file when `forceuid` or `forcegid` are in effect may not reflect the real (server) permissions. See the _File And Directory Ownership And Permissions_ section in [mount.cifs(8) § FILE AND DIRECTORY OWNERSHIP AND PERMISSIONS](<https://man.archlinux.org/man/mount.cifs.8#FILE_AND_DIRECTORY_OWNERSHIP_AND_PERMISSIONS>) for more information.
  * To mount a Windows share without authentication, use `"username=*"`.

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Regardless of recommendation, there's no substantial evidence for the claimed I/O error risk. The warning was [added without comment or reference in 2013](<https://wiki.archlinux.org/index.php?title=Samba&diff=prev&oldid=254430>) and challenged without defense in 2018. It's unclear whether it's true at all.（在 [Talk:Samba#Unfounded warning regarding I/O errors and manual mounting?](</wzh/index.php?title=Talk:Samba&action=edit&redlink=1> "Talk:Samba（页面不存在）") 中讨论）

**注意：** 请注意这里有 **s** ,其它文件系统一般用的是 _user_ 。

使用 `uid` 和 `gid` 挂载选项时，请注意[文件权限](<../zh-cn/File_permissions_and_attributes.html> "File permissions and attributes")，否则会出现 I/O 错误。}} 

**注意：** 使用 `uid` 和/或 `gid` 作为挂载选项可能会导致 I/O 错误，建议转而设置并检查 [文件权限与属性](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "文件权限与属性")。

  * `_SERVER_`——服务器名称
  * `_sharename_`——共享目录
  * `_mountpoint_`——本地挂载点
  * `[-o _options_]`——详情请参考 {{man|8|mount.cifs}。

**注意：**

  * 结尾不要加 `/`. `//_SERVER_ /_sharename_**/**` 无法工作.
  * 如果挂载工作不稳定，出现卡顿和掉线问题，请尝试用 `vers=` 设置不同的 SMB 协议版本。例如，挂载 Vista 用 `vers=2.0`。
  * 如果挂载了 cifs 的机器上出现关机超时，请参考 [wpa_supplicant#Problem with mounted network shares (cifs) and shutdown](<../zh-cn/Wpa_supplicant.html#Problem_with_mounted_network_shares_\(cifs\)_and_shutdown> "Wpa supplicant")。

####  保存共享密码

不建议将密码保存在所有人都可读的文件中，一个更安全的方式是创建凭证文件，例如写入到 `/etc/samba/credentials`： 
    
    /etc/samba/credentials/share
    
    username=_myuser_
    password=_mypass_

将挂载命令中的 `username=myuser,password=mypass` 替换为 `credentials=/etc/samba/credentials/share`。 

应仅根用户允许有凭证文件的读写权限： 
    
    # chown root:root /etc/samba/credentials
    # chmod 700 /etc/samba/credentials
    # chmod 600 /etc/samba/credentials/share
    
###  自动挂载

**注意：** You may need to [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `systemd-networkd-wait-online.service` or ` NetworkManager-wait-online.service` (depending on your setup) to proper enable booting on start-up.

####  Using NetworkManager and GIO/gvfs

[NetworkManager](<../zh-cn/NetworkManager.html#Network_services_with_NetworkManager_dispatcher> "NetworkManager") can be configured to run a script on network status change. This script uses the _gio_ command so that it mounts the Samba shares automatically, the same way your file manager does, as explained [below](<#File_manager_configuration>). The script also safely unmounts the Samba shares before the relevant network connection is disabled by listening for the `pre-down` and `vpn-pre-down` events. Make the script is [executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable") after creating it. 
    
    /etc/NetworkManager/dispatcher.d/30-samba.sh
    
    #!/bin/sh
    
    # Find the connection UUID with "nmcli con show" in terminal.
    # All NetworkManager connection types are supported: wireless, VPN, wired...
    WANTED_CON_UUID="CHANGE-ME-NOW-9c7eff15-010a-4b1c-a786-9b4efa218ba9"
    
    # The user the share will be mounted under
    USER="yourusername"
    # The path that appears in your file manager when you manually mount the share you want
    SMB_URL="smb://servername/share"
    
    # Get runtime user directory. If it does not exist, do nothing and just exit
    XDG_RUNTIME_DIR=$(loginctl show-user --property=RuntimePath --value "$USER") || exit 0
    
    if [ "$CONNECTION_UUID" = "$WANTED_CON_UUID" ]; then
        
        # Script parameter $1: network interface name, not used
        # Script parameter $2: dispatched event
        
        case "$2" in
            "up"|"vpn-up")
                su $USER -c "DBUS_SESSION_BUS_ADDRESS=unix:path=$XDG_RUNTIME_DIR/bus gio mount $SMB_URL"
                ;;
            "pre-down"|"vpn-pre-down")
                su $USER -c "DBUS_SESSION_BUS_ADDRESS=unix:path=$XDG_RUNTIME_DIR/bus gio mount -uf $SMB_URL"
                ;;
        esac
    fi
    
Create a symlink inside `/etc/NetworkManager/dispatcher.d/pre-down` to catch the `pre-down` events: 
    
    # ln -s /etc/NetworkManager/dispatcher.d/30-samba.sh /etc/NetworkManager/dispatcher.d/pre-down.d/30-samba.sh
    
**注意：** Since this script uses the user bus, it will only work if the user has active sessions. This means that the share will not mount automatically after boot if the connection is established before you are logged in.

####  作为挂载路径

This is a simple example of a `cifs` [mount entry](<../zh-cn/Fstab.html> "Fstab") that requires authentication: 
    
    /etc/fstab
    
    //_SERVER_ /_sharename_ /mnt/_mountpoint_ cifs _netdev,nofail,username=_myuser_ ,password=_mypass_ 0 0

**注意：**

  * See examples below on better security for authentication credentials
  * Spaces in sharename should be replaced by `\040` (ASCII code for space in octal). For example, `//_SERVER_ /share name` on the command line should be `//_SERVER_ /share\040name` in `/etc/fstab`.
  * To allow users to mount it as long as the mount point resides in a directory controllable by the user; i.e. the user's home, append the `users` mount option. The option is user**s** (plural). For other filesystem types handled by mount, this option is usually _user_ ; sans the "**s** ".

**提示：** Use `x-systemd.automount` if you want them to be mounted only upon access. See [Fstab#Remote file system](<../zh-cn/Fstab.html#Remote_file_system> "Fstab") for details.

####  作为 systemd 单元

在 `/etc/systemd/system` 下创建一个新的 `.mount` 文件，例如：`mnt-myshare.mount`。详细信息请查看 [systemd.mount(5)](<https://man.archlinux.org/man/systemd.mount.5>)。 

**注意：** 请确保文件名与你要使用的挂载点对应。 例如 `mnt-myshare.mount` 只能用于挂载位于 `/mnt/myshare` 下的共享，否则可能会出现像这样的报错：`systemd[1]: mnt-myshare.mount: Where= setting does not match unit name. Refusing`。

`What=` 要使用的共享路径 

`Where=` 将共享挂载到的位置 

`Options=` 共享挂载选项 

**注意：**

  * 网络挂载单元会自动获取 `remote-fs-pre.target`、`network.target` 和 `network-online.target` 中 `After` 部分的依赖，并在没有设置 `nofail` 挂载选项的情况下会获得对 `remote-fs.target` 的 `Before` 依赖。对于后者，还会添加一个 `Wants` 单元。
  * 将 `noauto` [添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "添加")到 `Options` 可以防止在启动阶段自动挂载（除非被其它单元拉起）。
  * 如果你想用主机名而不是 IP 来连接共享服务器，需要在 `After` 中加入 `nss-lookup.target`。这可以避免在测试时正常，但启动时挂载报错的情况出现。

    /etc/systemd/system/mnt-myshare.mount
    
    [Unit]
    Description=Mount Share at boot
    
    [Mount]
    What=//server/share
    Where=/mnt/myshare
    Options=_netdev,credentials=/etc/samba/credentials/myshare,iocharset=utf8,rw
    Type=cifs
    TimeoutSec=30
    
    [Install]
    WantedBy=multi-user.target

**提示：**

  * 遇到无法连通的主机时，将 `ForceUnmount=true` [添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "添加")到 `[Mount]` 以允许强制卸载共享。
  * 如果你的共享使用了只读权限的组，可以[添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "添加") `uid=_username_` 或者 `gid=_group_` 到 `Options=` 来指定拥有写入权限的用户/用户组。

要使用 `mnt-myshare.mount`，需[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")该单元，然后通过[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")使其在系统启动时运行。 

#####  自动化挂载

可以使用如下单元来在访问时自动挂载共享（类似 autofs）： 
    
    /etc/systemd/system/mnt-myshare.automount
    
    [Unit]
    Description=Automount myshare
    
    [Automount]
    Where=/mnt/myshare
    
    [Install]
    WantedBy=multi-user.target

[禁用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "禁用")/[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止") `mnt-myshare.mount`，然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")/[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `mnt-myshare.automount` 来在访问挂载路径时自动挂载共享。 

**提示：**[添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "添加") `TimeoutIdleSec` 以启用自动卸载。详细信息可参考 [systemd.automount(5)](<https://man.archlinux.org/man/systemd.automount.5>)。

#### smbnetfs

**注意：** smbnetfs needs an intact Samba server setup. See above on how to do that.

First, check if you can see all the shares you are interested in mounting: 
    
    $ smbtree -U _remote_user_
    
If that does not work, find and modify the following line in `/etc/samba/smb.conf` accordingly: 
    
    domain master = auto
    
Now [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `smb.service` and `nmb.service`. 

If everything works as expected, [install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [smbnetfs](<https://archlinux.org/packages/?name=smbnetfs>)包. 

Then, add the following line to `/etc/fuse.conf`: 
    
    user_allow_other
    
Now copy the directory `/etc/smbnetfs/.smb` to your home directory: 
    
    $ cp -a /etc/smbnetfs/.smb ~
    
Then create a link to `smb.conf`: 
    
    $ ln -sf /etc/samba/smb.conf ~/.smb/smb.conf
    
If a username and a password are required to access some of the shared folders, edit `~/.smb/smbnetfs.auth` to include one or more entries like this: 
    
    ~/.smb/smbnetfs.auth
    
    auth			"hostname" "username" "password"
    
It is also possible to add entries for specific hosts to be mounted by smbnetfs, if necessary. More details can be found in `~/.smb/smbnetfs.conf`. 

If you are using the [Dolphin](<../zh-cn/Dolphin.html> "Dolphin") or [GNOME Files](<../zh-cn/GNOME_Files.html> "GNOME Files"), you may want to add the following to `~/.smb/smbnetfs.conf` to avoid "Disk full" errors as smbnetfs by default will report 0 bytes of free space: 
    
    ~/.smb/smbnetfs.conf
    
    free_space_size 1073741824
    
When you are done with the configuration, you need to run 
    
    $ chmod 600 ~/.smb/smbnetfs.*
    
Otherwise, smbnetfs complains about 'insecure config file permissions'. 

Finally, to mount your Samba network neighbourhood to a directory of your choice, call 
    
    $ smbnetfs _mount_point_
    
##### Daemon

The Arch Linux package also maintains an additional system-wide operation mode for smbnetfs. To enable it, you need to make the said modifications in the directory `/etc/smbnetfs/.smb`. 

Then, you can start and/or enable the `smbnetfs` [daemon](<../zh-cn/Systemd.html> "Daemon") as usual. The system-wide mount point is at `/mnt/smbnet/`. 

#### autofs

See [Autofs](<../zh-cn/Autofs.html> "Autofs") for information on the kernel-based automounter for Linux. 

###  文件管理器配置

####  GNOME Files、Nemo、Caja、Thunar 和 PCManFM

为了通过 GNOME Files，Nemo，Caja，Thunar 或 PCManFM 访问 samba 共享，需安装 [gvfs-smb](<https://archlinux.org/packages/?name=gvfs-smb>)包 软件包。 

按 `Ctrl+l` 然后在地址栏输入 `smb://_servername_ /_share_` 以访问您的共享。 

共享很可能挂载到了文件系统中的 `/run/user/_your_UID_ /gvfs` 或 `~/.gvfs` 位置下。 

#### KDE

KDE 有内建的浏览 Samba 共享的能力。为了使用 KDE 系统设置的 GUI，你需要安装 [kdenetwork-filesharing](<https://archlinux.org/packages/?name=kdenetwork-filesharing>)包 软件包。 

KDE 应用（例如 Dolphin）自带 Samba 共享浏览功能。在地址栏输入 `smb://_servername_ /_share_`就可以浏览文件。如果你想在非 KDE 应用访问文件，可以安装 [kio-fuse](<https://archlinux.org/packages/?name=kio-fuse>)包。 

To use a GUI in the KDE System Settings, you will need to install the [kdenetwork-filesharing](<https://archlinux.org/packages/?name=kdenetwork-filesharing>)包 package. 

####  其它图形环境

There are a number of useful programs, but they may need to have packages created for them. This can be done with the Arch package build system. The good thing about these others is that they do not require a particular environment to be installed to support them, and so they bring along less baggage. 

  * [pyneighborhood](<https://aur.archlinux.org/packages/pyneighborhood/>)AUR
  * LinNeighborhood, RUmba, xffm-samba plugin for Xffm are not available in the official repositories or the AUR. As they are not officially (or even unofficially supported), they may be obsolete and may not work at all.

##  提示与技巧

### Discovering network shares

If nothing is known about other systems on the local network, and automated tools such as [smbnetfs](<#smbnetfs>) are not available, you can manually probe for Samba shares. 

First, [install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [nmap](<https://archlinux.org/packages/?name=nmap>)包 and [smbclient](<https://archlinux.org/packages/?name=smbclient>)包 packages. 

Use [nmap](</wzh/index.php?title=Nmap&action=edit&redlink=1> "Nmap（页面不存在）") to scan your local network to find systems with TCP port 445 open, which is the port used by the SMB protocol. Note that you may need to use `-Pn` or set a custom [ping scan type](</wzh/index.php?title=Nmap&action=edit&redlink=1> "Nmap（页面不存在）") (e.g. `-PS445`) because Windows systems are usually firewalled. 
    
    $ nmap -p 445 "192.168.1.*"
    
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-13 12:00 UTC
    Nmap scan report for 192.168.1.1
    Host is up (0.0011s latency).
    
    PORT    STATE  SERVICE
    445/tcp open  microsoft-ds
    
    Nmap scan report for 192.168.1.2
    Host is up (0.00011s latency).
    
    PORT    STATE SERVICE
    445/tcp open  microsoft-ds
    
    Nmap done: 256 IP addresses (2 hosts up) scanned in 2.45 seconds
    
The first result is another system; the second happens to be the client from where this scan was performed. 

Now you can connect to their IP addresses directly, but if you want to use NetBIOS host names, you can use [nmblookup(1)](<https://man.archlinux.org/man/nmblookup.1>) to check for NetBIOS names. Note that this will not work if NetBIOS is disabled on the server. 
    
    $ nmblookup -A 192.168.1.1
    
    Looking up status of 192.168.1.1
            PUTER           <00> -         B <ACTIVE>
            HOMENET         <00> - <GROUP> B <ACTIVE>
            PUTER           <03> -         B <ACTIVE>
            **PUTER <20> -         B <ACTIVE>**
            HOMENET         <1e> - <GROUP> B <ACTIVE>
            USERNAME        <03> -         B <ACTIVE>
            HOMENET         <1d> -         B <ACTIVE>
            MSBROWSE        <01> - <GROUP> B <ACTIVE>
    
Regardless of the output, look for **< 20>**, which shows the host with open services. 

Use [smbclient(1)](<https://man.archlinux.org/man/smbclient.1>) to list which services are shared on these systems. You can use NetBIOS host name (`PUTER` in this example) instead of IP when available. If prompted for a password, pressing enter should still display the list: 
    
    $ smbclient -L \\192.168.1.1
    
    Sharename       Type      Comment
    ---------       ----      -------
    MY_MUSIC        Disk
    SHAREDDOCS      Disk
    PRINTER$        Disk
    PRINTER         Printer
    IPC$            IPC       Remote Inter Process Communication
    
    Server               Comment
    ---------            -------
    PUTER
    
    Workgroup            Master
    ---------            -------
    HOMENET               PUTER
    
### Remote control of Windows computer

Samba offers a set of tools for communication with Windows. These can be handy if access to a Windows computer through remote desktop is not an option, as shown by some examples. 

Send shutdown command with a comment: 
    
    $ net rpc shutdown -C "comment" -I IPADDRESS -U USERNAME%PASSWORD
    
A forced shutdown instead can be invoked by changing -C with comment to a single -f. For a restart, only add -r, followed by a -C or -f. 

Stop and start services: 
    
    $ net rpc service stop SERVICENAME -I IPADDRESS -U USERNAME%PASSWORD
    
To see all possible net rpc command: 
    
    $ net rpc
    
##  疑难解答

###  启动 Samba SMB/CIFS 服务器失败

可能的解决方法： 

  * 通过 [testparm(1)](<https://man.archlinux.org/man/testparm.1>) 检查 `smb.conf` 中的配置问题。
  * 在 `/var/cache/samba/` 中配置正确的权限，然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `smb.service`：

    # chmod 0755 /var/cache/samba/msg
    
###  SELinux 权限问题

[SELinux](<../zh-cn/SELinux.html> "SELinux") 默认不允许 samba 访问用户的主目录。要解决此问题，执行： 
    
    # setsebool -P samba_enable_home_dirs 1
    
类似地，`samba_export_all_ro` 和 `samba_export_all_rw` 使 Samba 拥有读取或“读和写”所有文件的能力。 

###  AppArmor 权限问题

如果使用了一个在家目录或用户共享目录之外的[共享路径](<#%E5%88%9B%E5%BB%BA%E5%8C%BF%E5%90%8D%E5%85%B1%E4%BA%AB>)，请在 `/etc/apparmor.d/local/usr.sbin.smbd` 中将其加入白名单。例如： 
    
    /etc/apparmor.d/local/usr.sbin.smbd
    
    "/data/" rk,
    "/data/**" lrwk,
    
### No dialect specified on mount

The client is using an unsupported SMB/CIFS version that is required by the server. 

See [#Restrict protocols for better security](<#Restrict_protocols_for_better_security>) for more information. 

###  Unable to overwrite files, permissions errors

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** An user should set/check for server/client permissions, instead of using incorrect/possible insecure flags.（在 [Talk:Samba](<../zh-cn/Talk:Samba.html>) 中讨论）

Possible solutions: 

  * Append the mount option `nodfs` to the `/etc/fstab` [entry](<#As_mount_entry>).
  * Add `msdfs root = no` to the `[global]` section of the server's `/etc/samba/smb.conf`.

### Windows clients keep asking for password even if Samba shares are created with guest permissions

Set `map to guest` inside the `global` section of `/etc/samba/smb.conf`: 
    
    map to guest = Bad Password
    
If you are still using Samba < 4.10.10, use `Bad User` instead of `Bad Password`. 

###  Windows 10 1709 和更高版本的连接性问题 - "Windows cannot access" 0x80004005

This error affects some machines running Windows 10 version 1709 and later. It is not related to SMB1 being disabled in this version but to the fact that Microsoft disabled insecure logons for guests on this version for some, but not others. 

To fix, open Group Policy Editor (`gpedit.msc`). Navigate to _Computer configuration\administrative templates\network\Lanman Workstation > Enable insecure guest logons_ and enable it. Alternatively,change the following value in the registry: 
    
    [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]
    "AllowInsecureGuestAuth"=dword:1
    
### Error: Failed to retrieve printer list: NT_STATUS_UNSUCCESSFUL

If you are a home user and using samba purely for file sharing from a server or NAS, you are probably not interested in sharing printers through it. If so, you can prevent this error from occurring by adding the following lines to your `/etc/samba/smb.conf`: 
    
    /etc/samba/smb.conf
    
    [global]
      load printers = No
      printing = bsd
      printcap name = /dev/null
      disable spoolss = Yes

[Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") the samba service, `smb.service`, and then check your logs: 
    
    # cat /var/log/samba/smbd.log
    
and the error should now no longer be appearing. 

### Sharing a folder fails

It means that while you are sharing a folder from _Dolphin_ (file manager) and everything seems ok at first, after restarting _Dolphin_ the share icon is gone from the shared folder, and also some output like this in terminal (_Konsole_) output: 
    
    ‘net usershare’ returned error 255: net usershare: usershares are currently disabled
    
To fix it, enable usershare as described in [#启用 Usershares](<#%E5%90%AF%E7%94%A8_Usershares>). 

###  "Browsing" network fails with "Failed to retrieve share list from server"

And you are using a firewall (iptables) because you do not trust your local (school, university, hotel) network. This may be due to the following: When the smbclient is browsing the local network it sends out a broadcast request on udp port 137. The servers on the network then reply to your client but as the source address of this reply is different from the destination address iptables saw when sending the request for the listing out, iptables will not recognize the reply as being "ESTABLISHED" or "RELATED", and hence the packet is dropped. A possible solution is to add: 
    
    iptables -t raw -A OUTPUT -p udp -m udp --dport 137 -j CT --helper netbios-ns
    
to your iptables setup. 

For [Uncomplicated Firewall](<../zh-cn/Uncomplicated_Firewall.html> "Uncomplicated Firewall"), you need to add `nf_conntrack_netbios_ns` to the end of the following line in `/etc/default/ufw`
    
    IPT_MODULES="nf_conntrack_ftp nf_nat_ftp nf_conntrack_irc nf_nat_irc"
    
and then run the following commands as root: 
    
    echo 1 > /proc/sys/net/netfilter/nf_conntrack_helper
    ufw allow CIFS
    ufw reload
    
To make this change persistent across reboots, add the following line at the end of `/etc/ufw/sysctl.conf`: 
    
    net.netfilter.nf_conntrack_helper=1
    
### Protocol negotiation failed: NT_STATUS_INVALID_NETWORK_RESPONSE

The client probably does not have access to shares. Make sure clients' IP address is in `hosts allow =` line in `/etc/samba/smb.conf`. 

Another problem could be, that the client uses an invalid protocol version. To check this try to connect with the `smbclient` where you specify the maximum protocol version manually: 
    
    $ smbclient -U <user name> -L //<server name> -m <protocol version: e. g. SMB2> -W <domain name>
    
If the command was successful then create a configuration file: 
    
    ~/.smb/smb.conf
    
    [global]
      workgroup = <domain name>
      client max protocol = SMB2

###  Connection to SERVER failed: (Error NT_STATUS_UNSUCCESSFUL)

You are probably passing a wrong server name to `smbclient`. To find out the server name, run `hostnamectl` on the server and look at "Transient hostname" line 

###  Connection to SERVER failed: (Error NT_STATUS_CONNECTION_REFUSED)

Make sure that the server has started. The shared directories should exist and be accessible. 

### Protocol negotiation failed: NT_STATUS_CONNECTION_RESET

Probably the server is configured not to accept protocol SMB1. Add option `client max protocol = SMB2` in `/etc/samba/smb.conf`. Or just pass argument `-m SMB2` to `smbclient`. 

###  Password Error when correct credentials are given (error 1326)

[Samba 4.5](<https://www.samba.org/samba/history/samba-4.5.0.html>) has NTLMv1 authentication disabled by default. It is recommend to install the latest available upgrades on clients and deny access for unsupported clients. 

If you still need support for very old clients without NTLMv2 support (e.g. Windows XP), it is possible force enable NTLMv1, although this is **not recommend** for security reasons: 
    
    /etc/samba/smb.conf
    
    [global]
      lanman auth = yes
      ntlm auth = yes

If NTLMv2 clients are unable to authenticate when NTLMv1 has been enabled, create the following file on the client: 
    
    /home/user/.smb/smb.conf
    
    [global]
      sec = ntlmv2
      client ntlmv2 auth = yes

This change also affects samba shares mounted with **mount.cifs**. If after upgrade to Samba 4.5 your mount fails, add the **sec=ntlmssp** option to your mount command, e.g. 
    
    mount.cifs //server/share /mnt/point -o sec=ntlmssp,...
    
See the [mount.cifs(8)](<https://man.archlinux.org/man/mount.cifs.8>) man page: **ntlmssp** \- Use NTLMv2 password hashing encapsulated in Raw NTLMSSP message. The default in mainline kernel versions prior to v3.8 was **sec=ntlm**. In v3.8, the default was changed to **sec=ntlmssp**. 

### Mapping reserved Windows characters

Starting with kernel 3.18, the cifs module uses the ["mapposix" option by default](<https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=2baa2682531ff02928e2d3904800696d9e7193db>). When mounting a share using unix extensions and a default Samba configuration, files and directories containing one of the seven reserved Windows characters `: \ * < > ? ` are listed but cannot be accessed. 

Possible solutions are: 

  * Use the undocumented `nomapposix` mount option for cifs

    # mount.cifs //server/share /mnt/point -o nomapposix
    
  * Configure Samba to remap `mapposix` ("SFM", Services for Mac) style characters to the correct native ones using [fruit](<https://www.mankier.com/8/vfs_fruit>)

    /etc/samba/smb.conf
    
    [global]
      vfs objects = catia fruit
      fruit:encoding = native

  * Manually remap forbidden characters using [catia](<https://www.mankier.com/8/vfs_catia>)

    /etc/samba/smb.conf
    
    [global]
      vfs objects = catia
      catia:mappings = 0x22:0xf022, 0x2a:0xf02a, 0x2f:0xf02f, 0x3a:0xf03a, 0x3c:0xf03c, 0x3e:0xf03e, 0x3f:0xf03f, 0x5c:0xf05c, 0x7c:0xf07c, 0x20:0xf020

The latter approach (using catia or fruit) has the drawback of filtering files with unprintable characters. 

### Folder shared inside graphical environment is not available to guests

This section presupposes: 

  1. Usershares are configured following [previous section](<#Enable_Usershares>)
  2. A shared folder has been created as a non-root user from GUI
  3. Guests access has been set to shared folder during creation
  4. Samba service has been restarted at least once since last `/etc/samba/smb.conf` file modification

For clarification purpose only, in the following sub-sections is assumed: 

  * Shared folder is located inside user home directory path (`/home/yourUser/Shared`)
  * Shared folder name is _MySharedFiles_
  * Guest access is read-only.
  * Windows users will access shared folder content without login prompt

#### Verify correct samba configuration

Run the following command from a terminal to test configuration file correctness: 
    
    $ testparm
    
#### Verify correct shared folder creation

Run the following commands from a terminal: 
    
    $ cd /var/lib/samba/usershares
    $ ls
    
If everything is fine, you will notice a file named `mysharedfiles`

Read the file contents using the following command: 
    
    $ cat mysharedfiles
    
The terminal output should display something like this: 
    
    /var/lib/samba/usershares/mysharedfiles
    
    path=/home/yourUser/Shared
    comment=
    usershare_acl=S-1-1-0:r
    guest_ok=y
    sharename=MySharedFiles

#### Verify folder access by guest

Run the following command from a terminal. If prompted for a password, just press Enter: 
    
    $ smbclient -L localhost
    
If everything is fine, MySharedFiles should be displayed under `Sharename` column 

Run the following command in order to access the shared folder as guest (anonymous login) 
    
    $ smbclient -N //localhost/MySharedFiles
    
If everything is fine samba client prompt will be displayed: 
    
    smb: \>
    
From samba prompt verify guest can list directory contents: 
    
    smb: \> ls
    
If the `NTFS_STATUS_ACCESS_DENIED` error is displayed, the issue is likely to be with Unix directory permissions. Ensure that your samba user has access to the folder and all parent folders. You can test this by sudoing to the user and attempting to list the mount directory, and all of its parents. 

### Mount error: Host is down

This error might be seen when mounting shares of Synology NAS servers. Use the mount option `vers=1.0` to solve it. 

**注意：** SMB version 1 is known to have security vulnerabilities and was used in successful ransomware attacks.

### Software caused connection abort

File managers that utilizes [gvfs-smb](<https://archlinux.org/packages/?name=gvfs-smb>)包 can show the error `Software caused connection abort` when writing a file to a share/server. This may be due to the server running SMB/CIFS version 1, which many routers use for USB drive sharing (e.g. Belkin routers). To write to these shares specify the CIFS version with the option `vers=1.0`. E.g.: 
    
    /etc/fstab
    
    //SERVER/sharename /mnt/mountpoint cifs _netdev,guest,file_mode=0777,dir_mode=0777,vers=1.0 0 0

This can also happen after updating Samba to version 4.11, which deactivates SMB1 as default, and accessing any Samba share. You can reenable it by adding 
    
    /etc/samba/smb.conf
    
    [global]
    client min protocol = CORE

###  Connection problem (due to authentification error)

Be sure that you do not leave any space characters before your username in Samba client configuration file as follows: 
    
    ~/.samba
    
    username= user
    password=pass

The correct format is: 
    
    ~/.samba
    
    username=user
    password=pass

###  Windows 1709 及更高版本无法在“网络”视图中发现 Samba 服务器

随着 Windows 10 1511 版本的推出，对 SMBv1 的支持以及由此的 NetBIOS 设备发现被默认禁用。根据实际版本不同，从1709版本（"秋季创意者更新"）开始的 Windows 版本不允许再安装 SMBv1 客户端。这导致运行 Samba 的主机无法在资源管理器的“网络（网上邻居）”视图中被列出。虽然并无连接问题，而且 Samba 仍然可以正常运行，但用户可能想让他们的 Samba 主机被 Windows 自动列出。[wsdd](<https://aur.archlinux.org/packages/wsdd/>)AUR 实现了一个 Web Service Discovery 宿主守护进程。这使得（Samba）主机，比方说你的本地 NAS 设备，能够被像 Windows 这样的 Web Service Discovery 客户端找到。默认设置应该适用于大多数用例，你要做的就是启用 `wsdd.service`。 

默认配置（在组 "WORKGROUP "中使用机器主机名公示自己）应适用于绝大多数情况。如果有需要，你可以通过在 `/etc/conf.d/wsdd` 中添加额外的参数来改变配置选项（详见wsdd的手册页）。 

[wsdd2](<https://aur.archlinux.org/packages/wsdd2/>)AUR 的功能相同，但它是用 C 语言而不是 Python 编写的。默认情况下，它将在 `smb.conf` 中寻找 `netbios name` 和 `workgroup` 值。 

###  GNOME Files not showing Windows machines (version 1709 or up) with shared folders in Network view

See [GNOME/Files#Windows machines (version 1709 or up) with shared folders don't show up in Network view](<../zh-cn/GNOME/%E6%96%87%E4%BB%B6.html#Windows_machines_\(version_1709_or_up\)_with_shared_folders_don't_show_up_in_Network_view> "GNOME/Files"). 

###  iOS/iPadOS Files can no longer copy-to Samba share on Arch Linux beginning with iOS/iPadOS 14.5

Beginning with iOS/iPadOS 14.5 attempting to transfer from a device running iOS/iPadOS using the "Files" app to a samba share on Arch Linux will result in the error: 
    
    The operation couldn't be completed
    Operation canceled
    
To correct this problem, add add the following to the global section of your `smb.conf` and [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `smb.service`. Comment optional: 
    
    ## addition for iOS/iPadOS 14.5+ Files transfer-to server
    vfs object = fruit streams_xattr
    
See <https://apple.stackexchange.com/q/424681> Apple.Stackexchange.com - "The operation couldn't be completed"/"Operation canceled" error message when saving to a Samba share via Files app. 

### Slow initial connections from certain clients without other performance problems

Some SMB clients, such as Solid Explorer for Android, take significantly longer to connect to Samba if they fail to resolve the NetBIOS name. Enabling `nmb.service` will greatly speed up initial connections if this is the case. Since this is a bug in the client software, please report such cases to the authors of conflicting software. 

###  Windows 复制文件时会随机卡住不动

使用 windows 文件管理器复制 samba 服务器中的文件时，会随机出现卡住不动的情况。原因是复制 linux 的 pipe 特殊文件会占用连接数，当连接数消耗完毕以后， windows 的复制窗口就会一直卡住不动。解决办法是在 `smb.conf` 中添加隐藏特殊文件配置项。 

参考来源：<https://forum.level1techs.com/t/samba-server-and-windows-clients-getting-stuck/161676>
    
    /etc/samba/smb.conf
    
    [global]
       hide special files = yes

##  更多参考

  * [官方网站](<https://www.samba.org/>)
  * [Samba: An Introduction](<https://www.samba.org/samba/docs/SambaIntro.html>)
  * [Samba 3.2.x HOWTO and Reference Guide](<https://www.samba.org/samba/docs/Samba-HOWTO-Collection.pdf>)（已过时，但仍是最详细的文档）
  * [维基百科](<https://en.wikipedia.org/wiki/Samba_\(software\)> "wikipedia:Samba \(software\)")
  * [Gentoo:Samba/Guide](<https://wiki.gentoo.org/wiki/Samba/Guide> "gentoo:Samba/Guide")
  * [Debian:Samba/ServerSimple](<https://wiki.debian.org/Samba/ServerSimple> "debian:Samba/ServerSimple")
  * [KSMBD](<https://docs.kernel.org/filesystems/smb/ksmbd.html>) \- A linux kernel server which implements SMB3 protocol in kernel space for sharing files over network.
