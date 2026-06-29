**翻译状态：**

  * 本文（或部分内容）译自 [OpenSSH](<https://wiki.archlinux.org/title/OpenSSH> "arch:OpenSSH")，最近一次同步于 2025-03-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/OpenSSH?diff=0&oldid=821978>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/OpenSSH_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [SSH 密钥](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html> "SSH 密钥")
  * [Pam abl](</wzh/index.php?title=Pam_abl&action=edit&redlink=1> "Pam abl（页面不存在）")
  * [fail2ban](<../zh-cn/Fail2ban.html> "Fail2ban")
  * [sshguard](<../zh-cn/Sshguard.html> "Sshguard")
  * [Sshfs](</wzh/index.php?title=Sshfs&action=edit&redlink=1> "Sshfs（页面不存在）")
  * [Syslog-ng](</wzh/index.php?title=Syslog-ng&action=edit&redlink=1> "Syslog-ng（页面不存在）")
  * [SFTP chroot](<../zh-cn/SFTP_chroot.html> "SFTP chroot")
  * [SCP and SFTP](<../zh-cn/SCP_and_SFTP.html> "SCP and SFTP")
  * [VPN over SSH](</wzh/index.php?title=VPN_over_SSH&action=edit&redlink=1> "VPN over SSH（页面不存在）")

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:OpenSSH#](<../zh-cn/Talk:OpenSSH.html>) 中讨论）

[OpenSSH](<https://zh.wikipedia.org/wiki/OpenSSH> "zhwp:OpenSSH")（OpenBSD Secure Shell）是使用[安全外壳协议](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "安全外壳协议")（SSH），在计算机网络上提供加密通信会话的软件集。它是 SSH Communications Security 专有 SSH 软件的开源替代方案。OpenSSH 是 OpenBSD 项目的一部分，该项目由 Theo de Raadt 领导。 

OpenSSH 有时候会与名字相似的 OpenSSL 相混淆；然而，它们的目的不同，开发团队也不同，名字相似只因为两者目标相似。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [openssh](<https://archlinux.org/packages/?name=openssh>)包。 

##  客户端用法

连接服务器： 
    
    $ ssh -p _端口_ _用户名_ @_服务器地址_
    
如果服务器只允许公钥认证，参考 [SSH 密钥](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html> "SSH 密钥")。 

###  配置

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：**[openssh](<https://archlinux.org/packages/?name=openssh>)包 9.4p1-2 added `Include /etc/ssh/ssh_config.d/*.conf` to `/etc/ssh/ssh_config`. The instructions can now be made to use drop-in files. (在 [Talk:OpenSSH](<../zh-cn/Talk:OpenSSH.html>) 中讨论)

客户端可以配置一些通用的参数和主机信息。所有的参数都可以全局配置或者限制为特定主机，例如： 
    
    ~/.ssh/config
    
    # 全局选项
    User _用户名_
    
    # 特定于主机的选项
    Host _myserver_
        Hostname _服务器地址_
        Port     _端口_
    
配置之后，下面的两条命令是等价的： 
    
    $ ssh -p _端口_ _用户名_ @_服务器地址_
    $ ssh _myserver_
    
参考 [ssh_config(5)](<https://man.archlinux.org/man/ssh_config.5>) 可以获得更多的信息。 

一些参数没有对应的命令行选项，但你可以在命令行中使用 `-o` 指定配置选项。例如 `-oKexAlgorithms=+diffie-hellman-group1-sha1`。 

##  服务端用法

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：**[openssh](<https://archlinux.org/packages/?name=openssh>)包 9.4p1-2 added `Include /etc/ssh/sshd_config.d/*.conf` to `/etc/ssh/sshd_config`. The instructions can now be made to use drop-in files. (在 [Talk:OpenSSH](<../zh-cn/Talk:OpenSSH.html>) 中讨论)

`sshd` 是 OpenSSH 服务器守护程序，通过 `/etc/ssh/sshd_config` 配置并由 `sshd.service` 管理。每次更改配置后，请在重新启动服务前在测试模式下运行 `sshd` 以确保它能够干净地启动。有效配置将不会产生输出： 
    
    # sshd -t
    
###  配置

要仅允许某些用户访问，请添加以下一行： 
    
    AllowUsers    _用户1 用户2_
    
要仅允许某些用户组访问： 
    
    AllowGroups   _用户组1 用户组2_
    
要添加漂亮的欢迎消息（例如，输出 `/etc/issue` 文件），请配置 `Banner` 选项： 
    
    Banner /etc/issue
    
_sshdgenkeys_ [服务](<#%E7%AE%A1%E7%90%86%E5%AE%88%E6%8A%A4%E7%A8%8B%E5%BA%8F>)会自动在 `/etc/ssh` 中生成缺失的任何算法的公钥和私钥，即使 `sshd_config` 中的 `HostKeyAlgorithms` 选项只允许部分加密算法。OpenSSH 提供了三种基于 [ed25519、ecdsa 和 rsa](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html#%E9%80%89%E6%8B%A9%E8%AE%A4%E8%AF%81%E5%AF%86%E9%92%A5%E7%A7%8D%E7%B1%BB> "SSH 密钥") 算法的密钥对。要让 sshd 使用特定的密钥，请指定以下选项： 
    
    HostKey /etc/ssh/ssh_host_ed25519_key
    
如果服务器要暴露在公网下，建议将默认端口从 22 更改为更高的随机端口，例如： 
    
    Port 39901
    
**提示：**

  * 要选择尚未分配给常见服务的备用端口，请查看 [TCP 和 UDP 端口号列表](<https://zh.wikipedia.org/wiki/TCP/UDP%E7%AB%AF%E5%8F%A3%E5%88%97%E8%A1%A8> "zhwp:TCP/UDP端口列表")，还可以在本地的 `/etc/services` 中查找端口信息。更改 OpenSSH 所使用的端口有助于减少由攻击者使用自动程序尝试通过 SSH 登录你的服务器的情况（但无法彻底解决）。查看 [Port knocking](</wzh/index.php?title=Port_knocking&action=edit&redlink=1> "Port knocking（页面不存在）") 了解相关内容。
  * 建议完全禁用密码登录。这将大大提高安全性，更多信息请参见[#强制公钥认证](<#%E5%BC%BA%E5%88%B6%E5%85%AC%E9%92%A5%E8%AE%A4%E8%AF%81>)。更多推荐的安全方法，请参阅[#保护](<#%E4%BF%9D%E6%8A%A4>)。
  * OpenSSH 可以监听多个端口，只需在配置文件中添加多行 `Port _端口号_`。
  * 可以通过从 `/etc/ssh` 中删除要替换的主机密钥对并以 root 身份运行 `ssh-keygen -A` 来生成新的（或缺失的）主机密钥对。

###  管理守护程序

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `sshd.service`。它将保持 SSH 守护程序始终处于活动状态，并为每个传入连接 fork。 

**注意：** 因易受到拒绝服务攻击的影响，[openssh](<https://archlinux.org/packages/?name=openssh>)包 8.0p1-3删除了 `sshd.socket`，更多信息请参考 [FS#62248](<https://bugs.archlinux.org/task/62248>)。如果在更新到 [openssh](<https://archlinux.org/packages/?name=openssh>)包 8.0p1-3 时启用了 `sshd.socket`，则 `sshd.socket` 和 `sshd@.service` 单元将被复制到 `/etc/systemd/system/` 并重新启用。这样做只是为了不破坏现有设置；仍然建议用户迁移到 `sshd.service`。

**警告：** 如果你继续使用 `sshd.socket`, 请注意下列问题: 

  * `sshd.socket` 单元可能会失败 (例如：在内存耗尽的情况下) 并且 `Restart=always` 不能被用于 socket 单元. 点击 [systemd issue 11553](<https://github.com/systemd/systemd/issues/11553>) 了解更多内容。
  * 使用套接字激活会导致拒绝服务，因为太多的连接会导致拒绝进一步激活服务。见 [FS#62248](<https://bugs.archlinux.org/task/62248>)。

**注意：** `sshd.socket` 使得 `ListenAddress` 设置失效，因此它会允许连接任意地址。为了使 `ListenAddress` 设置起作用，你必须[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `sshd.socket` 来为 `ListenStream` 指定端口 _和_ IP（例如 `ListenStream=192.168.1.100:22`）。你还必须在 `[Socket]` 添加 `FreeBind=true`，否则设置 IP 地址会有 `ListenAddress` 设置一样的缺点：如果网络没有及时启动，套接字会启动失败。

**提示：** 当使用套接字激活时，每个连接都会启动一个 `sshd@.service` 的瞬态实例（实例名称会不同）。因此，不论是 `sshd.socket` 还是守护进程常规的 `sshd.service` 都会不被允许在日志中监控连接尝试。可以通过 root 运行 `journalctl -u "sshd@*"` 或者 `journalctl /usr/bin/sshd` 查看 SSH 套接字激活实例的日志。

###  保护

允许通过 SSH 远程登录有利于管理，但可能会威胁服务器的安全。由于 SSH 访问通常是暴力攻击的目标，因此需要适当限制 SSH 访问以防止第三方访问服务器。 

[ssh-audit](<https://archlinux.org/packages/?name=ssh-audit>)包 提供对服务端和客户端配置的自动分析。关于这个主题，还有其他几个很好的指南和工具，例如： 

  * [Mozilla Infosec 团队的文章](<https://wiki.mozilla.org/Security/Guidelines/OpenSSH> "mozillawiki:Security/Guidelines/OpenSSH")
  * [SSH Hardening Guides](<https://www.ssh-audit.com/hardening_guides.html>)

####  强制公钥认证

如果客户端无法通过公钥进行身份验证，SSH 服务端默认会退回到使用密码进行身份验证，从而允许恶意用户尝试通过[暴力穷举](<#%E9%98%B2%E6%AD%A2%E6%9A%B4%E5%8A%9B%E7%A9%B7%E4%B8%BE%E6%94%BB%E5%87%BB>)密码来获取访问权限。防止这种攻击的最有效方法之一是完全禁用密码登录，并强制使用 [SSH 密钥](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html> "SSH 密钥")。这可以通过在守护程序配置文件中设置以下选项来完成： 
    
    /etc/ssh/sshd_config.d/20-force_publickey_auth.conf
    
    PasswordAuthentication no
    AuthenticationMethods publickey
    
**警告：** 在将此添加到配置之前，请确保所有需要 SSH 访问的帐户都在相应的 `authorized_keys` 文件中设置了公钥身份验证。详细信息请参阅 [SSH 密钥#将公钥复制到远程服务器上](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html#%E5%B0%86%E5%85%AC%E9%92%A5%E5%A4%8D%E5%88%B6%E5%88%B0%E8%BF%9C%E7%A8%8B%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A> "SSH 密钥")。

####  双重身份认证和公钥

SSH 可以被设置成需要多重验证。你可以通过 `AuthenticationMethods` 选项指定使用哪些验证方式，这将同时启用公钥和双重验证。 

#####  身份验证提供程序

设置 Google 身份验证器的方法请查看 [Google 身份验证器](<../zh-cn/Google_%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E5%99%A8.html> "Google 身份验证器")。 

对于 [Duo](<https://duo.com/>)，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")提供 `pam_duo.so` 模块的包 [duo_unix](<https://aur.archlinux.org/packages/duo_unix/>)AUR 。阅读 [Duo Unix 文档](<https://duo.com/docs/duounix>)以了解如何设置 Duo 凭据（Integration Key，密钥和 API 主机名）。 

#####  PAM 设置

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** The distribution defaults to `KbdInteractiveAuthentication no` since [[1]](<https://gitlab.archlinux.org/archlinux/packaging/packages/openssh/-/commit/1d834b1fb688e148797c39cffd95eac3404ef894>). Later, the lexical order of the defaults was adjusted due to [FS#79285](<https://bugs.archlinux.org/task/79285>) to allow for higher priority user snippets, which would match below `20-pam.conf`. However, a [BBS thread](<https://bbs.archlinux.org/viewtopic.php?id=300451>) appears to be resolved by ordering custom after `99-archlinux.conf` defaults only.（在 [Talk:OpenSSH](<../zh-cn/Talk:OpenSSH.html>) 中讨论）

要在 OpenSSH 中使用 [PAM](<../zh-cn/PAM.html> "PAM")，请编辑下列文件： 
    
    /etc/ssh/sshd_config.d/20-pam.conf
    
    KbdInteractiveAuthentication yes
    AuthenticationMethods publickey keyboard-interactive:pam
    
然后你可以通过公钥**或** 在 PAM 中设置的用户身份验证方法登录。 

另一方面，如果您想要根据 PAM 设置的要求使用公钥**和** 用户身份验证对用户进行验证，请使用逗号而不是空格来分隔 AuthenticationMethods： 
    
    /etc/ssh/sshd_config.d/20-pam.conf
    
    KbdInteractiveAuthentication yes
    AuthenticationMethods publickey**,** keyboard-interactive:pam
    
为了要求同时使用公钥和 pam 身份验证，您可能希望禁用密码登录： 
    
    /etc/pam.d/sshd
    
    auth      required  pam_securetty.so     #disable remote root
    #Require google authenticator
    auth      required  pam_google_authenticator.so
    #But not password
    #auth      include   system-remote-login
    account   include   system-remote-login
    password  include   system-remote-login
    session   include   system-remote-login
    
####  防止暴力穷举攻击

暴力攻击的概念非常简单：使用大量随机用户名和密码组合尝试登录网页或类似 SSH 等服务。 

请参考 [ufw#连接速率限制](<../zh-cn/Uncomplicated_Firewall.html#%E8%BF%9E%E6%8E%A5%E9%80%9F%E7%8E%87%E9%99%90%E5%88%B6> "Ufw")，如果使用的是 [iptables](<../zh-cn/Iptables.html> "Iptables")，请参考 [Simple stateful firewall#Bruteforce attacks](<../zh-cn/Simple_stateful_firewall.html#Bruteforce_attacks> "Simple stateful firewall")。 

从 9.8 版本开始，OpenSSH 引入了类似 [fail2ban](<../zh-cn/Fail2ban.html> "Fail2ban") 的基本保护实现：`PerSourcePenalties` 选项默认配置了一个合理值，会对同一地址上的客户端针对各种条件进行惩罚，导致在一段时间内被拒绝连接。 

另外，你也可以使用自动化脚本封禁任何尝试暴力穷举登录的对象。 

  * 只允许可信源地址进行 SSH 连接
  * 使用 [fail2ban](<../zh-cn/Fail2ban.html> "Fail2ban") 或 [sshguard](<../zh-cn/Sshguard.html> "Sshguard") 自动封禁多次密码登录失败的 IP
  * 使用 [pam_shield](<https://github.com/h0tw1r3/pam_shield>) 封禁一段时间内多次尝试登录的 IP。与 [fail2ban](<../zh-cn/Fail2ban.html> "Fail2ban") 或 [sshguard](<../zh-cn/Sshguard.html> "Sshguard") 不同，该程序不会对成功和失败登录请求进行区分。

###  限制root用户登录

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** Root login has been disabled by default upstream in the current version. Unclear to me what parts of this section and subsections are redundant. (在[Talk:OpenSSH](<../zh-cn/Talk:OpenSSH.html>)讨论)

It is generally considered bad practice to allow the root user to log in without restraint over SSH. There are two methods by which SSH root access can be restricted for increased security. 

#####  拒绝

Sudo selectively provides root rights for actions requiring these without requiring authenticating against the root account. This allows locking the root account against access via SSH and potentially functions as a security measure against brute force attacks, since now an attacker must guess the account name in addition to the password. 

SSH can be configured to deny remote logins with the root user by editing the "Authentication" section in the daemon configuration file. Simply set `PermitRootLogin` to `no`: 
    
    /etc/ssh/sshd_config.d/20-deny_root.conf
    
    PermitRootLogin no

Next, [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") the SSH daemon. 

You will now be unable to log in through SSH under root, but will still be able to log in with your normal user and use [su](<../zh-cn/Su.html> "Su") or [sudo](<../zh-cn/Sudo.html> "Sudo") to do system administration. 

#####  限制

Some automated tasks such as remote, full-system backup require full root access. To allow these in a secure way, instead of disabling root login via SSH, it is possible to only allow root logins for selected commands. This can be achieved by editing `~root/.ssh/authorized_keys`, by prefixing the desired key, e.g. as follows: 
    
    command="rrsync -ro /" ssh-ed25519 ...
    
This will allow any login with this specific key only to execute the command specified between the quotes. 

The increased attack surface created by exposing the root user name at login can be compensated by adding the following to `sshd_config`: 
    
    PermitRootLogin forced-commands-only
    
This setting will not only restrict the commands which root may execute via SSH, but it will also disable the use of passwords, forcing use of public key authentication for the root account. 

A slightly less restrictive alternative will allow any command for root, but makes brute force attacks infeasible by enforcing public key authentication. For this option, set: 
    
    PermitRootLogin prohibit-password
    
####  对 authorized_keys 文件加锁

**警告：** Locking this file only protects against user mistakes and a particular naive in-person attack. It **does not** provide any protection against malicious programs or breaches. Use multi-factor authentication, firewalling and practice defence in depth to prevent breaches in the first place.

If, for whatever reason, you think that the user in question should not be able to add or change existing keys, you can prevent them from manipulating the file. 

On the server, make the `authorized_keys` file read-only for the user and deny all other permissions: 
    
    $ chmod 400 ~/.ssh/authorized_keys
    
To prevent the user from simply changing the permissions back, [set the immutable bit](<../zh-cn/File_permissions_and_attributes.html#File_attributes> "File permissions and attributes") on the `authorized_keys` file. To prevent the user from renaming the `~/.ssh` directory and creating a new `~/.ssh` directory and `authorized_keys` file, set the immutable bit on the `~/.ssh` directory too. To add or remove keys, you will have to remove the immutable bit from `authorized_keys` and make it writable temporarily. 

**提示：** It is recommended to log changes to any `authorized_keys` file via e.g [auditd](</wzh/index.php?title=Audit_framework&action=edit&redlink=1> "Audit framework（页面不存在）").

#### SSH certificates

While common SSH keys and manual fingerprint verification may be easy to use with a handful of hosts that are managed by a single administrator, this method of authentication does not scale at all. When a number of servers need to be accessed through SSH by several users, manually verifying ssh public key fingerprints of every host becomes nearly impossible to do securely and reliably. 

The solution for this is to use SSH certificates that provide automatic verification of public key identities through a chain of trust that scales significantly better than the default trust-on-first-use approach of SSH. SSH certificates are basically nothing else than normal public SSH keys, but with an additional signature from a trusted certificate authority that verifies the key identity. 

##### Create a host certificate authority key for your infrastructure
    
    $ ssh-keygen -t ed25519 -f ~/.ssh/ca_host_key -C 'Host certificate authority for *.example.com'
    
The private certificate authority key should be stored securely, ideally on a smartcard or hardware token that prevents key extraction like the [Nitrokey](</wzh/index.php?title=Nitrokey&action=edit&redlink=1> "Nitrokey（页面不存在）") or [YubiKey](<../zh-cn/YubiKey.html> "YubiKey"). 

#####  Sign a server's public SSH host key

Copy the public server key to your local system containing the private certificate authority key to sign it: 
    
    $ ssh-keygen -h -s ~/.ssh/ca_key -I certLabel -n server01.example.com ./ssh_host_ed25519_key.pub
    
##### Move the new certificate and configure sshd to use it

The generated certificate `ssh_host_ed25519_key-cert.pub` should be copied to the server at `/etc/ssh/`. 
    
    /etc/ssh/sshd_config.d/20-ed25519_key.conf
    
    HostCertificate /etc/ssh/ssh_host_ed25519_key-cert.pub
    
##### Configure all clients to trust the certificate authority
    
    ~/.ssh/known_hosts
    
    @cert-authority  *.example.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKL8gB/pjuff005YNazwMCqJpgsXAbQ3r4VStd/CRKwU Host certificate authority for *.example.com
    
**警告：** When a server does not provide a certificate for identification, public key authentication is used as fallback by default.

##### SSH user certificates

Depending on the number of users and method of deployment, SSH User keys can also be used with Certificates. For organizations with many ssh users, this is strongly advised to manage User key deployment securely. 

The deployment of user certificates works basically the same as for server identities. More details and instructions can be found at [Wikibooks:OpenSSH/Cookbook/Certificate-based Authentication](<https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Certificate-based_Authentication> "wikibooks:OpenSSH/Cookbook/Certificate-based Authentication"). 

##### Certificate deployment automation

Automated deployment of SSH certificates can be provided by a number of open source tools. Popular examples are: 

  * [Ansible - openssh_cert module](<https://docs.ansible.com/ansible/latest/collections/community/crypto/openssh_cert_module.html>)
  * [privacyIDEA - authentication server](<https://www.privacyidea.org/>)
  * [Theo App - authorized keys manager](<https://theoapp.readthedocs.io/en/latest/>)

#### SSHFP record

The [Secure Shell fingerprint record (SSHFP)](<https://en.wikipedia.org/wiki/SSHFP_record> "wikipedia:SSHFP record") is an optional resource record in the domain name system that associates SSH keys to a host name. It can be used to verify the SSH fingerprint on public servers by using DNSSEC instead of deploying trusted CA certificates, which allows even unmanaged clients to verify the validity of key fingerprints. 

##### Generate record entry

To generate the required hexadecimal key fingerprint to be stored in the DNS record, create the hash on the target server. 
    
    $ ssh-keygen -r host.example.com
    
This will read all available SSH keys for the specified domain and output valid SSHFP records that can then be stored in the DNS entries of the affected domain. 

##### Client configuration

In order to automatically retrive and trust SSH key fingerprints stored as SSHFP records, add the following to your ssh client configuration file: 
    
    ~/.ssh/config
    
    # global options
    Match all
        VerifyHostKeyDNS yes
    
If the target host has a valid SSHFP record and this record is verified with a valid DNSSEC signature, the fingerprint is automatically accepted without prompting the user to verify the hosts identity. In case the DNS record is not verified by DNSSEC, the user will be prompted to verify the fingerprint instead. 

##### Generate SSHFP records

To determine the SSH fingerprint of a specific domain, use _ssh-keyscan_ to retrieve the ssh fingerprints in a valid DNS record format. (Note that by default fingerprints for every available key type is provided as both SHA1 and SHA256.) 
    
    $ ssh-keyscan -D github.com
    
    ; github.com:22 SSH-2.0-babeld-57ca1323
    ; github.com:22 SSH-2.0-babeld-57ca1323
    github.com IN SSHFP 1 1 6f4c60375018bae0918e37d9162bc15ba40e6365
    github.com IN SSHFP 1 2 b8d895ced92c0ac0e171cd2ef5ef01ba3417554a4a6480d331ccc2be3ded0f6b
    ; github.com:22 SSH-2.0-babeld-57ca1323
    github.com IN SSHFP 3 1 3358ab5dd3e306c461c840f7487e93b697e30600
    github.com IN SSHFP 3 2 a764003173480b54c96167883adb6b55cf7cfd1d415055aedff2e2c8a8147d03
    ; github.com:22 SSH-2.0-babeld-57ca1323
    github.com IN SSHFP 4 1 e9619e2ed56c2f2a71729db80bacc2ce9ccce8d4
    github.com IN SSHFP 4 2 f83898df0bef57a4ee24985ba598ac17fccb0c0d333cc4af1dd92be14bc23aa5
    ; github.com:22 SSH-2.0-babeld-57ca1323
    
Since the SSHFP record stores the key fingerprints as hexadecimal values while the common output for SSH fingerprints is the base64 encoded SHA256 hash of the public key, it is necessary to convert the record back to the base64 format in order to compare it with values in the known_hosts file or other documentation that commonly stores fingerprints as SHA256. 
    
    $ echo "SSHFP-fingerprint" | xxd -r -p | base64
    
Example for github.com using the hex value for the sha256 fingerprint of the key type ed25519 
    
    $ echo "f83898df0bef57a4ee24985ba598ac17fccb0c0d333cc4af1dd92be14bc23aa5" | xxd -r -p | base64
    
    +DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU=

Compare with known_hosts entries: 
    
    $ ssh-keygen -l -f ~/.ssh/known_hosts
    
##### Manually retrieve SSHFP records from DNS
    
    $ dig SSHFP targetdomain.tld +short
    
##  小技巧

###  使用加密的 SOCKS 隧道

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** Written like a blog post.（在[Talk:OpenSSH](<../zh-cn/Talk:OpenSSH.html>)讨论）

这对连接到各种不安全无线连接的笔记本电脑用户非常有用。你唯一需要的是在一个比较安全的位置运行的 SSH 服务器，比如你的家或工作地点。使用动态 DNS 服务可能很有用，如[DynDNS](<https://dyn.com/dns/>)，这样你就不必记住你的 IP 地址。 

####  步骤 1：开始连接

你只需要执行这一条命令就可以开始连接： 
    
    $ ssh -TND 4711 _user_ @_host_
    
其中 `_user_` 是你在 `_host_` 上运行的 SSH 服务器的用户名。它将询问你的密码，然后建立连接。`N` 标志禁用了交互式提示，`D` 标志指定了监听的本地端口（如果你愿意，可以选择任何端口号）。{Ic|T}} 标志禁用伪终端分配。 

可以添加 verbose（`-v`）标志，这样就可以通过输出验证是否成功连接。 

####  步骤 2 (方法 A)：配置你的浏览器（或其它程序）

上述步骤仅与使用新创建的 SOCKS 隧道的网页浏览器或其他程序结合使用时有用。SSH 现在同时支持 SOCKS v4 和 SOCKS v5，你可以选择它们中的任意一种。 

  * 对于火狐浏览器：进入 _首选项 > 通用_，跳到页面底部并点击网络设置项右边的 _设置..._ 按钮。接下来，在打开的二级窗口中，选中 _手动代理配置_ 并在 SOCKS 主机名框内输入 `localhost`，并在旁边的 _端口_ 项输入端口号（上述例子使用 `4711`）。

    火狐不会自动通过 SOCKS 隧道发出 DNS 请求，该潜在隐私问题可通过选中页面下方的 _使用 SOCKS v5 时代理 DNS 查询_ 解决。显然，这只在使用 SOCKS v5 而不是 v4 时有效。
    重启火狐来应用设置。

  * 对于 Chromium，可以将 SOCKS 设置为环境变量或通过命令行选项进行配置。例如，可以在 `.bashrc` 中添加以下函数：

    function secure_chromium {
        port=4711
        export SOCKS_SERVER=localhost:$port
        export SOCKS_VERSION=5
        chromium &
        exit
    }
    
或者是 
    
    function secure_chromium {
        port=4711
        chromium --proxy-server="socks://localhost:$port" &
        exit
    }
    
现在打开终端，然后执行： 
    
    $ secure_chromium
    
就可以使用安全隧道了！ 

####  步骤 2（方法 B）：配置本地 TUN 接口

这种方法在前期稍微复杂，但以后无需手动配置每个应用程序来使用 SOCKS 代理，具体原理是建立一个本地 TUN 接口并通过该接口路由流量。 

具体方法请参考 [VPN over SSH#Set up badvpn and tunnel interface](</wzh/index.php?title=VPN_over_SSH&action=edit&redlink=1> "VPN over SSH（页面不存在）")。 

###  X11 转发

使用 X11 转发可以在本地客户端上显示远程系统运行的 X11 程序图形界面。对于 X11 转发，远程主机不需要安装完整的 X11 环境，但至少要安装 _xauth_ 。 _xauth_ 是维护 `Xauthority` 配置的工具，该配置被服务端和客户端用于认证 X11 会话（[源](<http://xmodulo.com/2012/11/how-to-enable-x11-forwarding-using-ssh.html>)）。 

**警告：** X11 转发在安全方面有很强的影响，需至少要阅读 [ssh(1)](<https://man.archlinux.org/man/ssh.1>)、[sshd_config(5)](<https://man.archlinux.org/man/sshd_config.5>) 和 [ssh_config(5)](<https://man.archlinux.org/man/ssh_config.5>) 手册来了解相关信息。另外也请参考[该 StackExchange 提问](<https://security.stackexchange.com/questions/14815/security-concerns-with-x11-forwarding>)。

####  设置

#####  服务端

  * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xorg-xauth](<https://archlinux.org/packages/?name=xorg-xauth>)包
  * 在 `/etc/ssh/ssh**d** _config` 中： 
    * 设置 `X11Forwarding` 为 _yes_
    * 检查 `AllowTcpForwarding` 和 `X11UseLocalhost` 选项是否已设为 _yes_ ，并且 `X11DisplayOffset` 设为 _10_ （未修改情况下是默认值，参考 [sshd_config(5)](<https://man.archlinux.org/man/sshd_config.5>)）
  * 然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") [_sshd_ daemon](<#%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B%E7%AE%A1%E7%90%86>).

#####  客户端

  * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xorg-xauth](<https://archlinux.org/packages/?name=xorg-xauth>)包
  * 启用 `ForwardX11` 选项，可以在命令行中使用 `-X` 选项，也可以在[客户端配置文件](<#%E9%85%8D%E7%BD%AE>)中设置 `ForwardX11` 为 _yes_ 。

**提示：** 如果 GUI 显示质量不佳或者出现错误，可以启用 `ForwardX11Trusted` 选项（命令行下使用 `-Y`），这会防止 X11 转发受到 [X11 SECURITY extension](<https://www.x.org/wiki/Development/Documentation/Security/>) 的影响。在操作前，确保你已经看过[警告信息](<#X11_%E8%BD%AC%E5%8F%91>)。

####  用法

正常登录到远程机器，如果客户端的配置文件中没有启用 _ForwardX11_ ，则指定 `-X` 开关： 
    
    $ ssh -X _user@host_
    
如果你在试图运行图形应用程序时收到错误，请尝试用 _ForwardX11Trusted_ 代替： 
    
    $ ssh -Y _user@host_
    
如果出现 `X11 forwarding request failed` 报错，则需要为你的远程机器重新进行设置。一旦 X11 转发请求成功，你可以在远程服务器上启动任何 X 程序，它将被转发到你的本地会话： 
    
    $ xclock
    
如果出现了 `Can't open display` 报错，表示 `DISPLAY` 设置有误。 

对一些应用程序要小心，因为它们会检查本地机器上是否有正在运行的实例。[Firefox](<../zh-cn/Firefox.html> "Firefox") 就是一个例子：要么关闭正在运行的 Firefox 实例，要么使用下面的启动参数在本地机器上启动一个远程实例： 
    
    $ firefox --no-remote
    
如果你在连接时出现“X11 forwarding request failed on channel 0”报错（并且服务器 `/var/log/errors.log` 显示“Failed to allocate internet-domain X11 display socket”），请确保已安装 [xorg-xauth](<https://archlinux.org/packages/?name=xorg-xauth>)包。如果安装了也还是不行，可以尝试以下方法之一： 

  * 在 _服务端_ 的 `ssh**d** _config` 中启用 `AddressFamily any` 选项，或者
  * 在 _服务端_ 的 `ssh**d** _config` 中将 `AddressFamily` 选项设置为 inet。

将其设置为 inet 可能会解决 Ubuntu 客户端在 IPv4 上的问题。 

对于在 SSH 服务器上以另一个用户身份运行 X 应用程序，you need to `xauth add` the authentication line taken from `xauth list` of the SSH logged in user. 

**提示：** 关于 `X11 转发` 排障可参考以下链接： 

  * <https://unix.stackexchange.com/a/12772>
  * <https://unix.stackexchange.com/a/46748>
  * <https://superuser.com/a/805060>

###  转发其他端口

除了SSH对X11的内置支持外，它还可以通过本地转发或远程转发使用安全隧道传输任何 TCP 连接。 

本地转发打开本地计算机上的一个端口，连接将被转发到远程主机，并从那里转发到给定的目的地。通常，转发目的地将与远程主机相同，从而为同一机器提供安全外壳，例如安全 [VNC](<../zh-cn/TigerVNC.html> "VNC") 连接。本地转发会使用到 `-L` 选项，后接 `<tunnel port>:<destination address>:<destination port>` 格式的转发规则。 

因此： 
    
    $ ssh -L 1000:mail.google.com:25 192.168.0.100
    
将使用 SSH 进行登录到 `192.168.0.100` 并打开 shell，同时创建本地 TCP 端口 1000 到 mail.google.com 端口 25 的隧道。连接成功后，发送到 `localhost:1000` 的连接会连到 Gmail 的 SMTP 端口。除非使用了其它手段，否则对于谷歌来说，他们会观察到所有这些连接都是从 `192.168.0.100` 发送出来的（但对于连接传送的数据又是另一回事），而不是 `192.168.0.100`。 

类似地: 
    
    $ ssh -L 2000:192.168.0.100:6001 192.168.0.100
    
将允许连接到 `localhost:2000`，然后数据会被透明发送到远程主机的 6001 端口。The preceding example is useful for VNC connections using the vncserver utility--part of the [tightvnc](</wzh/index.php?title=Tightvnc&action=edit&redlink=1> "Tightvnc（页面不存在）") package--which, though very useful, is explicit about its lack of security. 

Remote forwarding allows the remote host to connect to an arbitrary host via the SSH tunnel and the local machine, providing a functional reversal of local forwarding, and is useful for situations where, e.g., the remote host has limited connectivity due to firewalling. It is enabled with the `-R` switch and a forwarding specification in the form of `<tunnel port>:<destination address>:<destination port>`. 

Thus: 
    
    $ ssh -R 3000:irc.libera.chat:6667 192.168.0.200
    
will bring up a shell on `192.168.0.200`, and connections from `192.168.0.200` to itself on port 3000 (the remote host's `localhost:3000`) will be sent over the tunnel to the local machine and then on to irc.libera.chat on port 6667, thus, in this example, allowing the use of IRC programs on the remote host to be used, even if port 6667 would normally be blocked to it. 

Both local and remote forwarding can be used to provide a secure "gateway", allowing other computers to take advantage of an SSH tunnel, without actually running SSH or the SSH daemon by providing a bind-address for the start of the tunnel as part of the forwarding specification, e.g. `<tunnel address>:<tunnel port>:<destination address>:<destination port>`. The `<tunnel address>` can be any address on the machine at the start of the tunnel. The address `localhost` allows connections via the `localhost` or loopback interface, and an empty address or `*` allow connections via any interface. By default, forwarding is limited to connections from the machine at the "beginning" of the tunnel, i.e. the `<tunnel address>` is set to `localhost`. Local forwarding requires no additional configuration; however, remote forwarding is limited by the remote server's SSH daemon configuration. See the `GatewayPorts` option in [sshd_config(5)](<https://man.archlinux.org/man/sshd_config.5>) and `-L address` option in [ssh(1)](<https://man.archlinux.org/man/ssh.1>) for more information about remote forwarding and local forwarding, respectively. 

###  跳板机

有时，可能无法直接连接到目标的 SSH 守护程序，因而需要使用一个跳转服务器（或[堡垒服务器](<https://en.wikipedia.org/wiki/bastion_host> "wikipedia:bastion host")）。为此，我们试图将两个或更多的 SSH 隧道连接在一起，并假设你的本地密钥对链上的每个服务器都有授权。这可以通过 SSH 代理转发（`-A`）和使用伪终端分配（`-t`）转发你的本地密钥实现： 
    
    $ ssh -A -t -l user1 bastion1 \
      ssh -A -t -l user2 intermediate2 \
      ssh -A -t -l user3 target
    
这一流程可以使用 ProxyCommand 选项进行自动化： 
    
    $ ssh -o ProxyCommand="ssh -W %h:%p bastion.example.org" targetserver.example.org
    
一个更简单和更安全的方法是将 ProxyJump 选项结合 `-J` 使用： 
    
    $ ssh -J user1@bastion1,user2@intermediate2 user3@target
    
`-J` 指令中的多个主机可以用逗号隔开，它们将按照列出的顺序被连接。`user...@` 部分不是必须的，但可以使用。The host specifications for `-J` use the ssh configuration file, so specific per-host options can be set there, if needed. 

The main difference between the ProxyCommand and ProxyJump options is that the later does not require a shell on the jumphost. Consequently, this also means that the jumpserver does not require access to the users login credentials or SSH agent forwarding. With the ProxyJump option, the ssh client connects through the jumpserver directly to the target server, establishing an end-to-end encrypted channel between client and target server. 

`-J` 标志相当于配置文件中 `ProxyJump` 选项，相关细节请参考 [ssh_config(5)](<https://man.archlinux.org/man/ssh_config.5>)。 

### Reverse SSH through a relay

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** The idea of SSH tunneling is classic, so some references for detailed explanation would be nice. E.g. [[2]](<https://unix.stackexchange.com/questions/46235/how-does-reverse-ssh-tunneling-work/118650#118650>) which includes other scenarios.（在[Talk:OpenSSH](<../zh-cn/Talk:OpenSSH.html>)讨论）

The idea is that the client connects to the server via another relay while the server is connected to the same relay using a reverse SSH tunnel. This is useful when the server is behind a NAT, and the relay is a publicly accessible SSH server used as a proxy to which the user has access. Therefore, the prerequisite is that the client's keys are authorized against both the relay and the server, and the server needs to be authorized against the relay as well for the reverse SSH connection. 

The following configuration example assumes that user1 is the user account used on client, user2 on relay and user3 on server. First, assuming we will use port 2222, the server needs to establish the reverse tunnel with: 
    
    ssh -R 2222:localhost:22 -N _user2_ @_relay_
    
Which can also be automated with a startup script, systemd service, [autossh](<#Autossh_-_automatically_restarts_SSH_sessions_and_tunnels>) or [sidedoor](<https://aur.archlinux.org/packages/sidedoor/>)AUR. 

At the client side, the connection is established with: 
    
    ssh -t _user2_ @_relay_ ssh _user3_ @localhost -p 2222
    
**注意：**`ssh _user3_ @_relay_ -p 2222` would require you to open this port in the firewall of your relay server, as well as to allow connections to this port from other addresses.

The remote command to establish the connection to reverse tunnel can also be defined in relay's `~/.ssh/authorized_keys` by including the `command` field as follows: 
    
    command="ssh _user3_ @localhost -p 2222" _ssh-ed25519_ _KEY2_ _user1_ @_client_
    
In this case the connection is established with: 
    
    ssh _user2_ @_relay_
    
Alternatively, you can add an entry to your ssh configuration that specifies both `RemoteCommand` and `RequestTTY`: 
    
    ~/.ssh/config
    
    Host _jump-destination_
        Hostname _relay_
        User _user2_
        RemoteCommand ssh _user3_ @localhost -p 2222
        RequestTTY yes
    
Which will reduce connecting to: 
    
    ssh _jump-destination_
    
**注意：** SCP's autocomplete function in client's terminal will not work and even the SCP transfers themselves are not working under some configurations.

###  多路复用

SSH 守护进程通常监听 22 端口。然而，许多公共热点会屏蔽所有不在常规 HTTP/S 端口（80 和 443）的流量，从而阻止了 SSH 连接。最直接解决这个问题的办法是让 `sshd` 额外监听白名单中的一个端口。 
    
    /etc/ssh/sshd_config
    
    Port 22
    Port 443
    
然而，443 端口很可能已经被提供 HTTPS 内容的网页服务器使用，在这种情况下，可以使用类似 [sslh](<https://archlinux.org/packages/?name=sslh>)包 的多路复用器，它会监听多路复用端口，并智能地将数据包转发给多个服务。 

###  SSH 提速

有多个[客户端配置项](<#%E9%85%8D%E7%BD%AE>)可以全局或为指定的主机提升连接性能。关于这些选项的完整描述请参考 [ssh_config(5)](<https://man.archlinux.org/man/ssh_config.5>)。 

  * _使用更快的加密算法_ ：在带有 AESNI 指令集的现代 CPU 上，使用 `aes128-gcm@openssh.com` 和 `aes256-gcm@openssh.com` 替代 openssh 的默认加密方法（通常是 `chacha20-poly1305@openssh.com`）应可以显著提升性能。在命令行中可以通过 `-c` 选项选择加密算法。如果要将配置持久化，可以在 `~/.ssh/config` 中添加 `Ciphers` 选项，然后按照偏好顺序填入加密算法，例如：
        
        Ciphers aes128-gcm@openssh.com,aes256-gcm@openssh.com,chacha20-poly1305@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr

  * _启用或禁用压缩_ ：在低速连接上启用压缩可以提升性能，该功能可通过 `Compression yes` 选项或 `-C` 标志进行启用。但是，该选项使用的压缩算法是 [gzip(1)](<https://man.archlinux.org/man/gzip.1>)，相对较慢，在高速网络上可能会成为瓶颈。为提高性能，在本地或高速网络上应使用 `Compression no` 选项。

  * _共享连接_ ：可以使用以下选项为连到同一主机的所有会话共用一个连接：

    ControlMaster auto
    ControlPersist yes
    ControlPath ~/.ssh/sockets/socket-%r@%h:%p
    
    其中 `~/.ssh/sockets` 可以是任何其他用户不可写的目录。

  * `ControlPersist` 指定了在客户端连接关闭后，需要在后台等待新客户端连接的时间。可选值包括： 
    * `no`：最后一个客户端断开后立即关闭连接
    * 以秒指定的时间
    * `yes`：始终等待，连接永远不会被自动关闭

  * 可以使用 `AddressFamily inet` 选项或 `-4` 标志绕过 IPv6 查找来缩短登录时间。

  * 另外，如果有将 SSH 用于 SFTP 或 SCP 的需求，[高性能 SSH/SCP](<https://www.psc.edu/index.php/hpn-ssh>) 可以通过动态提升 SSH 缓存大小来显著提升传输速度。可以安装 [openssh-hpn](<https://aur.archlinux.org/packages/openssh-hpn/>)AUR 来使用带有该补丁的 OpenSSH。

###  使用 SSHFS 挂载远程文件系统

关于将 SSH 可访问的远程系统挂载到本地目录的内容请查看 [SSHFS](<../zh-cn/SSHFS.html> "SSHFS") 文章。这样您就可以使用任何工具对挂载的文件执行任何操作（复制、重命名、使用 vim 编辑等）。 _sshfs_ 一般优于 _shfs_ ，后者自 2004 年以来一直没有更新。 

###  保活

默认情况下，如果 SSH 会话空闲了一段时间，它将自动注销。为了保持会话，如果在一段时间内没有收到数据，客户端可以向服务器发送保持活动的信号，或者如果服务器没有收到客户端的消息，则可以对称地定期发送消息。 

  * 在**服务端** ，`ClientAliveInterval` 以秒为单位设置超时，如果没有从客户端接收到数据， _sshd_ 将发送响应请求。默认值为 0（不发送消息）。例如，要每 60 秒从客户端请求一次响应，请在[服务器配置](<#%E9%85%8D%E7%BD%AE_2>)中设置 `ClientAliveInterval 60` 选项。另见 `ClientAliveCountMax` 和 `TCPKeepAlive` 选项。

  * 在 '_客户端_ ，`ServerAliveInterval` 控制从客户端发送到服务器的响应请求之间的间隔。例如，要请求服务器每 120 秒响应一次，请将 `ServerAliveInterval 120` 选项添加到[客户端配置](<#%E9%85%8D%E7%BD%AE>)中。另请参见 `ServerAliveCountMax` 和 `TCPKeepAlive` 选项。

**注意：** 为了确保会话保持活动状态，客户机或服务器中只有一个需要发送 keep alive 请求。如果同时控制服务器和客户机，一个合理的选择是只在需要持久会话的客户机上配置 `ServerAliveInterval`，并使其他客户机和服务器保持默认配置。

### Automatically restart SSH tunnels with systemd

[systemd](<../zh-cn/Systemd.html> "Systemd") can automatically start SSH connections on boot/login _and_ restart them when they fail. This makes it a useful tool for maintaining SSH tunnels. 

The following service can start an SSH tunnel on login using the connection settings in your [ssh configuration](<#Configuration>). If the connection closes for any reason, it waits 10 seconds before restarting it: 
    
    ~/.config/systemd/user/tunnel.service
    
    [Unit]
    Description=SSH tunnel to myserver
    
    [Service]
    Type=simple
    Restart=always
    RestartSec=10
    ExecStart=/usr/bin/ssh -F %h/.ssh/config -N myserver
    
Then [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") and [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") the [Systemd/User](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/User") service. See [#Keep alive](<#Keep_alive>) for how to prevent the tunnel from timing out. If you wish to start the tunnel on boot, you might want to [rewrite the unit](<../zh-cn/Systemd.html#Writing_unit_files> "Systemd") as a system service. 

### Autossh - automatically restarts SSH sessions and tunnels

When a session or tunnel cannot be kept alive, for example due to bad network conditions causing client disconnections, you can use [autossh](<https://archlinux.org/packages/?name=autossh>)包 to automatically restart them. 

Usage examples: 
    
    $ autossh -M 0 -o "ServerAliveInterval 45" -o "ServerAliveCountMax 2" username@example.com
    
Combined with [SSHFS](<../zh-cn/SSHFS.html> "SSHFS"): 
    
    $ sshfs -o reconnect,compression=yes,transform_symlinks,ServerAliveInterval=45,ServerAliveCountMax=2,ssh_command='autossh -M 0' username@example.com: /mnt/example 
    
Connecting through a SOCKS-proxy set by [Proxy settings](<../zh-cn/Proxy_settings.html> "Proxy settings"): 
    
    $ autossh -M 0 -o "ServerAliveInterval 45" -o "ServerAliveCountMax 2" -NCD 8080 username@example.com 
    
With the `-f` option autossh can be made to run as a background process. Running it this way however means the passphrase cannot be entered interactively. 

The session will end once you type `exit` in the session, or the autossh process receives a SIGTERM, SIGINT of SIGKILL signal. 

#### Run autossh automatically at boot via systemd

If you want to automatically start autossh, you can create a systemd unit file: 
    
    /etc/systemd/system/autossh.service
    
    [Unit]
    Description=AutoSSH service for port 2222
    After=network.target
    
    [Service]
    Environment="AUTOSSH_GATETIME=0"
    ExecStart=/usr/bin/autossh -M 0 -NL 2222:localhost:2222 -o TCPKeepAlive=yes foo@bar.com
    
    [Install]
    WantedBy=multi-user.target

Here `AUTOSSH_GATETIME=0` is an environment variable specifying how long ssh must be up before autossh considers it a successful connection, setting it to 0 autossh also ignores the first run failure of ssh. This may be useful when running autossh at boot. Other environment variables are available at [autossh(1)](<https://man.archlinux.org/man/autossh.1>). Of course, you can make this unit more complex if necessary (see the systemd documentation for details), and obviously you can use your own options for autossh, but note that the `-f` implying `AUTOSSH_GATETIME=0` does not work with systemd. 

Remember to [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") and/or [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") the service afterwards. 

You may also need to disable ControlMaster e.g. 
    
    ExecStart=/usr/bin/autossh -M 0 -o ControlMaster=no -NL 2222:localhost:2222 -o TCPKeepAlive=yes foo@bar.com
    
**提示：** It is also easy to maintain several autossh processes, to keep several tunnels alive. Just create multiple service files with different names.

### Alternative service should SSH daemon fail

For remote or headless servers which rely exclusively on SSH, a failure to start the SSH daemon (e.g., after a system upgrade) may prevent administration access. [systemd](<../zh-cn/Systemd.html> "Systemd") offers a simple solution via `OnFailure` option. 

Let us suppose the server runs `sshd` and [telnet](<../zh-cn/Telnet.html> "Telnet") is the fail-safe alternative of choice. Create a file as follows. Do **not** [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `telnet.socket`! 
    
    /etc/systemd/system/sshd.service.d/override.conf
    
    [Unit]
    OnFailure=telnet.socket

That's it. Telnet is not available when `sshd` is running. Should `sshd` fail to start, a telnet session can be opened for recovery. 

### Terminal background color based on host

为了更好地区分在不同主机上的情况，可以设置[基于主机类型的不同背景颜色](<https://bryangilbert.com/post/etc/term/dynamic-ssh-terminal-background-colors/>)。 

这种解决方案仅限于 ZSH。 

### Network specific configuration

You can use host configuration specific to the network you are connected to using a `Match exec`. 

For example, when using [nmcli(1)](<https://man.archlinux.org/man/nmcli.1>), and the connection is configured (manually or through DHCP) to use a search-domain: 
    
    Match exec "nmcli | grep domains: | grep example.com"
      CanonicalDomains example.com
      # Should you use a different username on this network
      #User username
      # Use a different known_hosts file (for private network or synchronisation)
      #UserKnownHostsFile <network>_known_hosts

Another example for `Match host ... exec "..."`: Consider that connecting to `internal.example.com` requires a bastion/proxy (via `ProxyJump`) unless you are already connected via VPN. The fragment `!exec "host internal.example.com"` applies only when `internal.example.com` cannot be looked up via DNS. Various alternatives are discussed at [[3]](<https://serverfault.com/q/536043/117525>). 
    
    Match host internal.example.com !exec "host internal.example.com"
      ProxyJump bastion.example.com
    Host internal.example.com
      User foobar

### Private networks hostkeys verification

Because different servers on different networks are likely to share a common private IP address, you might want to handle them differently. 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** The best solution would not need a warning to use something else in practice.（在 [Talk:OpenSSH](<../zh-cn/Talk:OpenSSH.html>) 中讨论）

The best solution is to use the [#Network specific configuration](<#Network_specific_configuration>) to use a different `UserKnownHostsFile` depending on the network you are on. The second solution, best used as default when you are working on new/prototype networks, would be to simply ignore hostkeys for private networks: 
    
    Host 10.* 192.168.*.* 172.31.* 172.30.* 172.2?.* 172.1?.*
        # Disable HostKey verification
        # Trust HostKey automatically
        StrictHostKeyChecking no
        # Do not save the HostKey
        UserKnownHostsFile=/dev/null
        # Do not display: "Warning: Permanently Added ..."
        LogLevel Error

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** The `known_hosts` file records an IP address even when you use hostname to access the server.（在 [Talk:OpenSSH](<../zh-cn/Talk:OpenSSH.html>) 中讨论）

**警告：** In a production environment, make sure to either use the hostname to access the host and/or to use network specific known_hosts files.

###  在登录时运行命令

如果你使用的是交互式会话，有多种方法可以在登录时执行一个命令： 

  * 使用远程主机上的 `authorized_keys` 文件（参见 [sshd(8) § AUTHORIZED_KEYS FILE FORMAT](<https://man.archlinux.org/man/sshd.8#AUTHORIZED_KEYS_FILE_FORMAT>)）
  * 如果服务器启用了 `~/.ssh/rc` 选项，则使用远程主机上的 `PermitUserRC` 选项
  * 使用远程主机上的 shell 配置文件，例如 `.bashrc`。

###  转发代理

SSH 代理转发允许你在连接到一个服务器时使用你的本地密钥。[建议](<https://security.stackexchange.com/questions/7480/risks-of-ssh-to-an-untrusted-host#7504>)只对选定的主机启用代理转发。 
    
    ~/.ssh/config
    
    Host _myserver.com_
        ForwardAgent yes
    
接下来，配置 [SSH 代理](</wzh/index.php?title=SSH_agent&action=edit&redlink=1> "SSH agent（页面不存在）")并使用 _ssh-add_ 添加你的本地密钥。 

如果你现在连接到一个远程服务器，你将能够使用你的本地密钥连接到其他服务。 

###  生成新的密钥对

新的服务器私钥可以通过以下方式生成: 

  1. 删除已有的所有密钥，例如：
         
         # rm /etc/ssh/ssh_host_*_key*

  2. [重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `sshdgenkeys.service` 或者以根用户身份运行 `ssh-keygen -A`

### Run sshd as non-privileged user

You may want to run `sshd` as non-privileged user in containers, or for testing, etc. 

Since non-privileged user cannot read host keys in `/etc/ssh`, new host keys must be generated: 
    
    $ ssh-keygen -q -N "" -t rsa -b 4096 -f _/path/to/host/keys/ssh_host_rsa_key_
    $ ssh-keygen -q -N "" -t ecdsa -f _/path/to/host/keys/ssh_host_ecdsa_key_
    $ ssh-keygen -q -N "" -t ed25519 -f _/path/to/host/keys/ssh_host_ed25519_key_
    
Create an `sshd_config` file. The example below uses a port higher than 1024, provides a new path to the host keys and disables PAM: 
    
    _/path/to/sshd_config_
    
    Port 2022
    HostKey _/path/to/host/keys/ssh_host_rsa_key_
    HostKey _/path/to/host/keys/ssh_host_ecdsa_key_
    HostKey _/path/to/host/keys/ssh/ssh_host_ed25519_key_
    UsePAM no
    
Run _sshd_ with the created config. The `-D` flag disables daemon mode and `-e` redirects output to stderr to allow easy monitoring. 
    
    $ sshd -f _/path/to/sshd_config_ -D -e
    
##  排障

### Checklist

Check these simple issues before you look any further. 

  1. The configuration directory `~/.ssh`, its contents should be accessible only by the user (check this on both the client and the server), and the user's home directory should only be writable by the user: 
         
         $ chmod go-w ~
         $ chmod 700 ~/.ssh
         $ chmod 600 ~/.ssh/*
         $ chown -R $USER ~/.ssh
         
  2. Check that the client's public key (e.g. `id_ed25519.pub`) is in `~/.ssh/authorized_keys` on the server.
  3. Check that you did not limit SSH access with `AllowUsers` or `AllowGroups` in the [server config](<#Configuration_2>).
  4. Check if the user has set a password. Sometimes new users who have not yet logged in to the server do not have a password.
  5. [Append](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Append") `LogLevel DEBUG` to `/etc/ssh/sshd_config`.
  6. Run `journalctl -xe` as root for possible (error) messages.
  7. [Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `sshd` and logout/login on both client and server.

### Connection refused or timeout problem

#### Port forwarding

If you are behind a NAT mode/router (which is likely unless you are on a VPS or publicly addressed host), make sure that your router is forwarding incoming ssh connections to your machine. Find the server's internal IP address with `$ ip addr` and set up your router to forward TCP on your SSH port to that IP. [portforward.com](<https://portforward.com>) can help with that. 

####  Is SSH running and listening?

The [ss](</wzh/index.php?title=Ss&action=edit&redlink=1> "Ss（页面不存在）") utility shows all the processes listening to a TCP port with the following command line: 
    
    $ ss --tcp --listening
    
If the above command do not show the system is listening to the port `ssh`, then SSH is not running: check the [journal](<../zh-cn/Systemd/Journal.html> "Journal") for errors etc. 

####  Are there firewall rules blocking the connection?

[Iptables](<../zh-cn/Iptables.html> "Iptables") may be blocking connections on port `22`. Check this with: 
    
    # iptables -nvL

and look for rules that might be dropping packets on the `INPUT` chain. Then, if necessary, unblock the port with a command like: 
    
    # iptables -I INPUT 1 -p tcp --dport 22 -j ACCEPT
    
For more help configuring firewalls, see [firewalls](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "Firewalls"). 

####  Is the traffic even getting to your computer?

Start a traffic dump on the computer you are having problems with: 
    
    # tcpdump -lnn -i any port ssh and tcp-syn
    
This should show some basic information, then wait for any matching traffic to happen before displaying it. Try your connection now. If you do not see any output when you attempt to connect, then something outside of your computer is blocking the traffic (e. g., hardware firewall, NAT router etc.). 

####  Your ISP or a third party blocking default port?

**注意：** Try this step if you **know** you are not running any firewalls and you know you have configured the router for DMZ or have forwarded the port to your computer and it still does not work. Here you will find diagnostic steps and a possible solution.

In some cases, your ISP might block the default port (SSH port 22) so whatever you try (opening ports, hardening the stack, defending against flood attacks, et al) ends up useless. To confirm this, create a server on all interfaces (0.0.0.0) and connect remotely. 

If you get an error message comparable to this: 
    
    ssh: connect to host www.inet.hr port 22: Connection refused
    
That means the port is **not** being blocked by the ISP, but the server does not run SSH on that port (See [security through obscurity](<https://en.wikipedia.org/wiki/Security_through_obscurity> "wikipedia:Security through obscurity")). 

However, if you get an error message comparable to this: 
    
    ssh: connect to host 111.222.333.444 port 22: Operation timed out 
    
That means that something is rejecting your TCP traffic on port 22. Basically that port is stealth, either by your firewall or 3rd party intervention (like an ISP blocking and/or rejecting incoming traffic on port 22). If you know you are not running any firewall on your computer, and you know that Gremlins are not growing in your routers and switches, then your ISP is blocking the traffic. 

To double check, you can run Wireshark on your server and listen to traffic on port 22. Since Wireshark is a Layer 2 Packet Sniffing utility, and TCP/UDP are Layer 3 and above (see [IP Network stack](<https://en.wikipedia.org/wiki/Internet_protocol_suite> "wikipedia:Internet protocol suite")), if you do not receive anything while connecting remotely, a third party is most likely to be blocking the traffic on that port to your server. 

##### Diagnosis

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") either [tcpdump](<https://archlinux.org/packages/?name=tcpdump>)包 or Wireshark with the [wireshark-cli](<https://archlinux.org/packages/?name=wireshark-cli>)包 package. 

For tcpdump: 
    
    # tcpdump -ni _interface_ "port 22"
    
For Wireshark: 
    
    $ tshark -f "tcp port 22" -i _interface_
    
where `_interface_` is the network interface for a WAN connection (see `ip a` to check). If you are not receiving any packets while trying to connect remotely, you can be very sure that your ISP is blocking the incoming traffic on port 22. 

##### Possible solution

The solution is just to use some other port that the ISP is not blocking. Open the `/etc/ssh/sshd_config` and configure the file to use different ports. For example, add: 
    
    Port 22
    Port 1234
    
Also make sure that other "Port" configuration lines in the file are commented out. Just commenting "Port 22" and putting "Port 1234" will not solve the issue because then sshd will only listen on port 1234. Use both lines to run the SSH server on both ports. 

[Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") the server `sshd.service` and you are almost done. You still have to configure your client(s) to use the other port instead of the default port. There are numerous solutions to that problem, but let us cover two of them here. 

#### Read from socket failed: connection reset by peer

Recent versions of OpenSSH sometimes fail with the above error message when connecting to older ssh servers. This can be worked around by setting various [client options](<#Configuration>) for that host. See [ssh_config(5)](<https://man.archlinux.org/man/ssh_config.5>) for more information about the following options. 

The problem could be the `ecdsa-sha2-nistp*-cert-v01@openssh` elliptical host key algorithms. These can be disabled by setting `HostKeyAlgorithms` to a list excluding those algorithms. On the client side, the `HostKeyAlgorithms` that the client wants to use can also be set by preceding the `HostKeyAlgorithms` list with a `-` to remove the specified algorithms (including wildcards) from the default set (see `ssh_config(5)` man page). You can check the actually used host key algorithm with `ssh -v server_to_connect_to` in the line that contains `kex: host key algorithm:`. 

If that does not work, it could be that the list of ciphers is too long. Set the `Ciphers` option to a shorter list (fewer than 80 characters should be enough). Similarly, you can also try shortening the list of `MACs`. 

See also the [discussion](<https://web.archive.org/web/20161201015151/https://www.gossamer-threads.com/lists/openssh/dev/51339>) on the OpenSSH bug forum. 

###  "[your shell]: No such file or directory" / ssh_exchange_identification problem

One possible cause for this is the need of certain SSH clients to find an absolute path (one returned by `whereis -b [your shell]`, for instance) in `$SHELL`, even if the shell's binary is located in one of the `$PATH` entries. 

###  "Terminal unknown" or "Error opening terminal" error message

If you receive the above errors upon logging in, this means the server does not recognize your terminal. Ncurses applications like nano may fail with the message "Error opening terminal". 

The correct solution is to install the client terminal's terminfo file on the server. This tells console programs on the server how to correctly interact with your terminal. You can get info about current terminfo using `$ infocmp` and then find out [which package owns it](<../zh-cn/Pacman.html#Querying_package_databases> "Pacman"). 

If you cannot [install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") it normally, you can copy your terminfo to your home directory on the server: 
    
    $ ssh myserver mkdir -p  ~/.terminfo/${TERM:0:1}
    $ scp /usr/share/terminfo/${TERM:0:1}/$TERM myserver:~/.terminfo/${TERM:0:1}/
    
After logging in and out from the server the problem should be fixed. 

#### TERM hack

**注意：** This should only be used as a last resort.

Alternatively, you can simply set `TERM=xterm` in your environment on the server (e.g. in `.bash_profile`). This will silence the error and allow ncurses applications to run again, but you may experience strange behavior and graphical glitches unless your terminal's control sequences exactly match xterm's. 

###  Connection closed by x.x.x.x [preauth]

If you are seeing this error in your sshd logs, make sure you have set a valid HostKey 
    
    HostKey /etc/ssh/ssh_host_ed25519_key
    
### subsystem request failed

Since _OpenSSH_ 8.8, _scp_ uses _SFTP_ as the default protocol for data transfers by requesting the subsystem named `sftp`. If you run _scp_ in verbose mode, `scp -v`, you can determine which subsystem your client is using (e.g. `Sending subsystem: <subsystem-name>`). Errors such as `subsystem request failed on channel 0` may be fixed by configuring the server's Subsystem settings: [sshd_config(5) § Subsystem](<https://man.archlinux.org/man/sshd_config.5#Subsystem>). The server configuration should resemble the example below. 
    
    /etc/ssh/sshd_config
    
    ...
    Subsystem subsystem-name /path/to/subsystem-executable
    ...
    
### id_dsa refused

OpenSSH 7.0 deprecated DSA public keys for security reasons and OpenSSH 9.8 is built without support for DSA keys by default. The first OpenSSH release of 2025 will remove DSA support entirely. For now, if you absolutely must use them, you will need to rebuild [openssh](<https://archlinux.org/packages/?name=openssh>)包 while passing `--enable-dsa-keys` to `configure`.[[4]](<https://marc.info/?l=openssh-unix-dev&m=171982945528949&w=2>)

### No matching key exchange method found by OpenSSH 7.0

OpenSSH 7.0 deprecated the diffie-hellman-group1-sha1 key algorithm because it is weak and within theoretical range of the so-called Logjam attack (see <https://www.openssh.com/legacy.html>). If the key algorithm is needed for a particular host, ssh will produce an error message like this: 
    
    Unable to negotiate with 127.0.0.1: no matching key exchange method found.
    Their offer: diffie-hellman-group1-sha1
    
The best resolution for these failures is to upgrade/configure the server to not use deprecated algorithms. If that is not possible, you can force the client to reenable the algorithm with the [client option](<#Configuration>) `KexAlgorithms +diffie-hellman-group1-sha1`. 

###  tmux/screen session killed when disconnecting from SSH

If your processes get killed at the end of the session, it is possible that you are using socket activation and it gets killed by [systemd](<https://archlinux.org/packages/?name=systemd>)包 when it notices that the SSH session process exited. In that case there are two solutions. One is to avoid using socket activation by using `ssh.service` instead of `ssh.socket`. The other is to set `KillMode=process` in the Service section of `ssh@.service`. 

The `KillMode=process` setting may also be useful with the classic `ssh.service`, as it avoids killing the SSH session process or the [screen](<https://archlinux.org/packages/?name=screen>)包 or [tmux](<https://archlinux.org/packages/?name=tmux>)包 processes when the server gets stopped or restarted. 

### SSH session stops responding

SSH responds to [flow control commands](<https://en.wikipedia.org/wiki/Software_flow_control> "wikipedia:Software flow control") `XON` and `XOFF`. It will freeze/hang/stop responding when you hit `Ctrl+s`. Use `Ctrl+q` to resume your session. 

### Broken pipe

If you attempt to create a connection which results in a `Broken pipe` response for `packet_write_wait`, you should reattempt the connection in debug mode and see if the output ends in error: 
    
    debug3: send packet: type 1
    packet_write_wait: Connection to A.B.C.D port 22: Broken pipe

The `send packet` line above indicates that the reply packet was never received. So, it follows that this is a _QoS_ issue. To decrease the likely-hood of a packet being dropped, set `IPQoS`: 
    
    /etc/ssh/ssh_config
    
    Match all
        IPQoS reliability

The `reliability` (`0x04`) type-of-service should resolve the issue, as well as `0x00` and `throughput` (`0x08`). 

### Terminate unresponsive SSH connection

If a client session is no longer responding and cannot be terminated by instructing the running program (e.g. [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell")), you can still terminate the session by pressing `Enter`, `~` and `.` one after another in that order. 

The `~` is a pseudo-terminal escape character (see [ssh(1) § ESCAPE CHARACTERS](<https://man.archlinux.org/man/ssh.1#ESCAPE_CHARACTERS>)), which can be added multiple times depending on the client session to terminate. For example, if you connected from A to B and then from B to C and the session from B to C freezes, you can terminate it by pressing `Enter` and typing `~~.`, which will leave you in a working session on B. 

###  WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!

If the client warns that the key of an ssh server has changed, you should verify that the newly offered key really belongs to the server operator via an authenticated (not necessarily encrypted) channel. Then remove the old key from the `known_hosts` file with `ssh-keygen -R $SSH_HOST` and accept the new key as if it was a new server. 

### Connecting to a remote without the appropriate terminfo entry

When connecting to hosts that do not have a terminfo entry for your terminal, for example, when using a terminal emulator whose terminfo entry is not shipped with [ncurses](<https://archlinux.org/packages/?name=ncurses>)包 (e.g. [kitty](<../zh-cn/Kitty.html> "Kitty") and [rxvt-unicode](<../zh-cn/Rxvt-unicode.html> "Rxvt-unicode")), or when connecting to hosts with a limited terminfo database (e.g. systems running [OpenWrt](<https://en.wikipedia.org/wiki/OpenWrt> "wikipedia:OpenWrt")), various issues will occur with software that relies on [terminfo(5)](<https://man.archlinux.org/man/terminfo.5>). 

A proper solution is to place the appropriate terminfo entry on the host. If that is not feasible, an alternative is to set `TERM` to a value that is both supported by the remote host and compatible with the terminal. 

Since OpenSSH 8.7, a custom `TERM` environment variable can be passed to remote hosts with a simple configuration snippet: 
    
    ~/.ssh/config
    
    Host example.com
      SetEnv TERM=xterm-256color

###  Connection through jump host fails with "bash: No such file or directory"

If you do not have the `SHELL` environment variable set to a full valid path (on the jump server), connection will fail with an error message simmilar to this one: 
    
    bash: No such file or directory
    kex_exchange_identification: Connection closed by remote host
    Connection closed by UNKNOWN port 65535
    
You can simply solve this by setting your `SHELL` to a full path name of a shell that will also be valid on the jump server or by setting a specific `SHELL` variable for each server in your `~/.ssh/config` file. 

##  参见

  * [Wikibooks:OpenSSH](<https://en.wikibooks.org/wiki/OpenSSH> "wikibooks:OpenSSH")
  * [防御暴力 ssh 攻击](<https://www.la-samhna.de/library/brutessh.html>)
  * OpenSSH 密钥管理：[第一部分](<https://www.ibm.com/developerworks/library/l-keyc/index.html>)在 IBM developerWorks 上, [第二部分](<https://www.funtoo.org/OpenSSH_Key_Management,_Part_2> "funtoo:OpenSSH Key Management, Part 2")、[第三部分](<https://www.funtoo.org/OpenSSH_Key_Management,_Part_3> "funtoo:OpenSSH Key Management, Part 3")在 funtoo.org 上
  * [Secure Secure Shell](<https://stribika.github.io/2015/01/04/secure-secure-shell.html>)
