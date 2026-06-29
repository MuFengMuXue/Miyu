**翻译状态：**

  * 本文（或部分内容）译自 [Fail2ban](<https://wiki.archlinux.org/title/Fail2ban> "arch:Fail2ban")，最近一次同步于 2025-03-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/Fail2ban?diff=0&oldid=815458>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Fail2ban_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [sshguard](<../zh-cn/Sshguard.html> "Sshguard")
  * [安全](<../zh-cn/%E5%AE%89%E5%85%A8.html> "安全")

[Fail2ban](<https://www.fail2ban.org/wiki/index.php/Main_Page>) 会检查日志文件（例如 `/var/log/httpd/error_log`）并封禁存在恶意行为的 IP,例如大量身份验证请求，漏洞扫描等。Fail2ban 通常会在[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")规则上将这些 IP 封禁一段时间，但也可以配置像发送邮件等其它操作。 

**警告：**

  * IP 封禁软件可以防止一些简单的攻击，但依赖于额外的守护进程和正确的日志记录配置。
  * 在类似为 [sshd](<../zh-cn/OpenSSH.html> "Sshd") 启用仅接受公钥认证等情况下，没有必要使用 fail2ban。
  * 这不是 [VPN](<../zh-cn/Category:VPN.html> "VPN") 的替代品，请尽量不要将服务暴露到互联网上。
  * 如果攻击者知道你的 IP，他们可以发送修改了源地址头字段的包使你的 IP 被服务器封禁，因此务必将你的 IP 添加到 `ignoreip` 中。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")以下软件包之一： 

  * [fail2ban](<https://archlinux.org/packages/?name=fail2ban>)包 \- 最新的稳定版
  * [fail2ban-git](<https://aur.archlinux.org/packages/fail2ban-git/>)AUR \- 包含添加到代码库的最新更改

##  用法

[配置](<#%E9%85%8D%E7%BD%AE>) Fail2ban 并[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `fail2ban.service`。 

### fail2ban-client

fail2ban-client 可以用于管理 jail 的状态（包括重新加载、重启、查看状态等）。要查看所有可用命令： 
    
    $ fail2ban-client
    
要查看已启用的 jail： 
    
    # fail2ban-client status
    
要查看 jail 的状态（以 _sshd_ 为例）： 
    
    # fail2ban-client status sshd
    
    Status for the jail: sshd
    |- Filter
    |  |- Currently failed: 1
    |  |- Total failed:     9
    |  `- Journal matches:  _SYSTEMD_UNIT=sshd.service + _COMM=sshd
    `- Actions
       |- Currently banned: 1
       |- Total banned:     1
       `- Banned IP list:   0.0.0.0
    
要查看所有 jail 的简略信息（包括已封禁的 IP）： 
    
    # fail2ban-client banned
    
    [{'sshd': ['192.168.100.50']}, {'apache-auth': []}]
    
##  配置

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Add a note about `dbpurgeage`, see [[1]](<https://wiki.meurisse.org/wiki/Fail2Ban#Recidive>). (在 [Talk:Fail2ban](<../zh-cn/Talk:Fail2ban.html>) 中讨论)

[jail.conf(5) § CONFIGURATION FILES FORMAT](<https://man.archlinux.org/man/jail.conf.5#CONFIGURATION_FILES_FORMAT>) 建议用户[创建](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建") `/etc/fail2ban/jail.local` 文件，否则在[更新](</wzh/index.php?title=%E6%9B%B4%E6%96%B0&action=edit&redlink=1> "更新（页面不存在）")时可能会为 `/etc/fail2ban/jail.conf` 创建新的 [Pacnew 和 Pacsave 文件](<../zh-cn/Pacman/pacnew_%E4%B8%8E_pacsave.html> "Pacman/pacnew 与 pacsave")。 

以将默认封禁时间设为一天为例： 
    
    /etc/fail2ban/jail.local
    
    [DEFAULT]
    bantime = 1d

也可以在 `/etc/fail2ban/jail.d` 目录下创建单独的 `_name_.local` 文件（例如 `/etc/fail2ban/jail.d/sshd.local`）。 

[重载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") `fail2ban.service` 以应用配置更改。 

###  启用 jail

所有 jail 默认都是禁用的。要启用 jail，需要在对应项[添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "添加") `enabled = true`。以启用 [OpenSSH](<../zh-cn/OpenSSH.html> "OpenSSH") jail 为例： 
    
    /etc/fail2ban/jail.local
    
    [sshd]
    enabled = true

具体配置请参考 [#配置 SSH jail](<#%E9%85%8D%E7%BD%AE_SSH_jail>)。 

###  接收告警邮件

如果你想在封禁时收到邮件提醒，需要参考下方配置 SMTP 客户端（例如 [msmtp](</wzh/index.php?title=Msmtp&action=edit&redlink=1> "Msmtp（页面不存在）")）并修改默认操作： 
    
    /etc/fail2ban/jail.local
    
    [DEFAULT]
    destemail = yourname@example.com
    sender = yourname@example.com
    
    # to ban & send an e-mail with whois report to the destemail.
    action = %(action_mw)s
    
    # same as action_mw but also send relevant log lines
    #action = %(action_mwl)s

###  防火墙和服务

Fail2ban 默认使用 [iptables](<../zh-cn/Iptables.html> "Iptables")，但要配置大部分[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")和服务也很简单，以 [nftables](<../zh-cn/Nftables.html> "Nftables") 为例： 
    
    /etc/fail2ban/jail.local
    
    [DEFAULT]
    banaction = nftables
    banaction_allports = nftables[type=allports]

其它示例请参考 `/etc/fail2ban/action.d/`，例如 [ufw.conf](<https://github.com/fail2ban/fail2ban/blob/master/config/action.d/ufw.conf>)。 

##  小技巧

###  配置 SSH jail

**警告：** 如果攻击者知道你的 IP，他们可以发送修改了源地址头字段的包使你的 IP 被服务器封禁。[SSH 密钥](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html> "SSH 密钥")为解决暴力攻击提供了简洁的方案，而不会产生这些问题。

编辑 `/etc/fail2ban/jail.d/sshd.local`，添加以下内容，并在 `ignoreip` 中修改可信 IP 清单： 
    
    /etc/fail2ban/jail.d/sshd.local
    
    [sshd]
    enabled   = true
    filter    = sshd
    banaction = iptables
    backend   = systemd
    maxretry  = 5
    findtime  = 1d
    bantime   = 2w
    ignoreip  = 127.0.0.1/8

**注意：**

  * 为使 fail2ban 具有完整监控能力，可能需要在 `/etc/ssh/sshd_config` 中设置 `LogLevel VERBOSE`，否则像密码错误等可能不会被正确记录。
  * Fail2ban 从 0.10 版本开始支持 IPv6，请按需调整[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")（例如[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")/[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `ip6tables.service`）。
  * 在使用 journal 命名空间（即在单元文件中使用 `LogNamespace=_something_`）时，可以像这样配置 `backend` 来让 fail2ban 读取这些日志：`backend = systemd[journalfiles="/var/log/journal/*._something_ /system.journal"]`

**提示：**

  * 如果使用像 [ufw](<../zh-cn/Uncomplicated_Firewall.html> "Ufw") 这样的 [iptables](<../zh-cn/Iptables.html> "Iptables") 前端，可以使用 `banaction = ufw` 替代 iptables。
  * 在使用 [Shorewall](<../zh-cn/Shorewall.html> "Shorewall") 时，可以在 `/etc/shorewall/shorewall.conf` 中使用 `banaction = shorewall`，并将 `BLACKLIST` 设为 `ALL`，否则新的 IP 封禁规则只会影响新连接。

###  Systemd 后端：journald 过滤

When using the _systemd_ backend to improve performance, configure a filter with `journalmatch`. For example, to parse only kernel-level log messages: 
    
    /etc/fail2ban/filter.d/fwdrop.local
    
    [Definition]
    failregex = ^.*DROP_.*SRC=<ADDR> DST=.*$
    journalmatch = _TRANSPORT=kernel

See also [systemd.journal-fields(7)](<https://man.archlinux.org/man/systemd.journal-fields.7>). 

###  服务加固

现在 Fail2ban 只能以 _根用户_ 权限运行。因此，你可能会想使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 加固进程。 

为 `fail2ban.service` [创建](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建")[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "Systemd")文件： 
    
    /etc/systemd/system/fail2ban.service.d/override.conf
    
    [Service]
    PrivateDevices=yes
    PrivateTmp=yes
    ProtectHome=read-only
    ProtectSystem=strict
    ReadWritePaths=-/var/run/fail2ban
    ReadWritePaths=-/var/lib/fail2ban
    ReadWritePaths=-/var/log/fail2ban.log
    ReadWritePaths=-/var/spool/postfix/maildrop
    ReadWritePaths=-/run/xtables.lock
    CapabilityBoundingSet=CAP_AUDIT_READ CAP_DAC_READ_SEARCH CAP_NET_ADMIN CAP_NET_RAW

`CapabilityBoundingSet` 的 `CAP_DAC_READ_SEARCH` 参数会允许 Fail2ban 读取所有目录和文件，`CAP_NET_ADMIN` 和 `CAP_NET_RAW` 会允许 Fail2ban 操作任何具有[命令行解释器](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "命令行解释器")界面的防火墙。具体信息请参考 [capabilities(7)](<https://man.archlinux.org/man/capabilities.7>)。 

使用 `ProtectSystem=strict` 会使[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")层次结构设为只读，`ReadWritePaths` 会允许 Fail2ban 对特定路径具有写入权限。 

最后[重载 systemd 守护进程](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")以应用对单元文件的修改，并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `fail2ban.service`。 

##  参考

  * [使用 Fail2Ban Jail 将用户加入白名单](<https://www.the-art-of-web.com/system/fail2ban-action-whitelist/>)
  * [Fail2Ban 过滤器优化](<https://www.the-art-of-web.com/system/fail2ban-filters/>)
  * [Fail2Ban 与 sendmail](<https://www.the-art-of-web.com/system/fail2ban-sendmail/>)
  * [Fail2Ban 与 iptables](<https://www.the-art-of-web.com/system/fail2ban/>)
  * [Fail2Ban 0.8.3 用法](<https://www.the-art-of-web.com/system/fail2ban-howto/>)
  * [监控 fail2ban 日志](<https://www.the-art-of-web.com/system/fail2ban-log/>)
