[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 本文档已经长期没有同步，上一次同步工作尚未完成，请参阅英文Wiki相关内容以取得最新信息 (在[Talk:Sendmail](<../zh-cn/Talk:Sendmail.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Sendmail](<https://wiki.archlinux.org/title/Sendmail> "arch:Sendmail")，最近一次同步于 2016-08-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Sendmail?diff=0&oldid=435685>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Sendmail_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Last updated in 2016, out of sync with English page（在 [Talk:Sendmail#](<../zh-cn/Talk:Sendmail.html>) 中讨论）

Sendmail 是来自 UNIX 世界的经典 SMTP 服务器。本篇是基于[邮件服务器](<../zh-cn/%E9%82%AE%E4%BB%B6%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "邮件服务器")构建的。 

本文的目的是为本地用户账户设置 Sendmail，**不使用 mysql 或者其它数据库** ，同时允许建立所谓 _mail-only 账户_ 。 

##  安装

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** sendmail 可以与其他邮件投递代理（MDA）配合使用，而不只是 procmail。 英文Wiki中存在：Talk:Sendmail#MDA_compatibility（在 [Talk:Sendmail](<../zh-cn/Talk:Sendmail.html>) 中讨论）

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [sendmail](<https://aur.archlinux.org/packages/sendmail/>)AUR, [procmail](<https://archlinux.org/packages/?name=procmail>)包 和 [m4](<https://archlinux.org/packages/?name=m4>)包

##  添加用户

为每个需要接收邮件的用户创建 [Linux 用户](<../zh-cn/Users_and_groups.html> "Users and groups")，每个用户会拥有类似 username@your-domain.com 的电子邮件地址。但是如果你想要添加 _mail-only 账户_ ，即仅能处理电子邮件，但不能使用 shell 或 X 进行登录的账户，您可以按如下步骤添加该类账户： 
    
    # useradd -m -s /usr/bin/nologin _username_
    
注：在此之后，您可以随时通过修改 `/etc/passwd` 等方式更改账户类型与属性。 

##  配置

###  创建 SSL 证书

**警告：** 如果你部署了 TLS，请务必遵循 weakdh.org 的指南，并禁用 SSLv3，以防止安全漏洞。更多信息请参阅[服务端SSL（英文Wiki）](<https://wiki.archlinux.org/title/Transport_Layer_Security#Server-side_recommendations>)

创建证书的过程，请阅读 [OpenSSL](<../zh-cn/OpenSSL.html#%E7%94%A8%E6%B3%95> "OpenSSL") 以了解更多信息，[Let's Encrypt](</wzh/index.php?title=Let%27s_Encrypt&action=edit&redlink=1> "Let's Encrypt（页面不存在）") 提供了免费认证。 

**警告：** 使用经过口令加密（具有 passphrase）的服务器的密钥文件可能导致 Sendmail 启用 TLS 失败。如果出现问题，请参考 [这里](<https://mnx.io/blog/removing-a-passphrase-from-an-ssl-key/>) 移除已有密钥文件的口令。

**注意：** 建议将服务器密钥与证书统一放在 ` /etc/mail/certs/ ` 目录下，并移除服务器密钥文件的组可读与其它可读权限。之后 ` sendmailconfig ` 工具可能会自动更改该文件夹下文件的属主、属组与权限。

### sendmail.cf

创建文件 `/etc/mail/sendmail.mc`，并以此为基础使用 [m4](<https://zh.wikipedia.org/wiki/M4_\(%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80\)> "zhwp:M4 \(程式语言\)") 工具生成 ` sendmail.cf ` 文件。 

您可以由 `/usr/share/sendmail-cf/README` 文件了解配置 sendmail 的全部选项。 

**警告：** 无论是从头创建自己的 `sendmail.mc` 文件，还是在已有的 ` sendmail.mc` 文件基础上进行修改，请时刻牢记，在**非 TLS** 情况下使用明文验证是十分危险的行为。除非您明确了解自己行为的意义，请使用以下示例中的方法强制进行 TLS 验证以确保安全性。

下面是在 [TLS](<https://en.wikipedia.org/wiki/Transport_Layer_Security> "wikipedia:Transport Layer Security") 之上进行身份验证的配置文件示例。例子包含了解释工作原理的注释，这些注释以 ` dnl ` 这个单词起始。 
    
    /etc/mail/sendmail.mc
    
    include(`/usr/share/sendmail-cf/m4/cf.m4')
    define(`confDOMAIN_NAME', `your-domain.com')dnl
    FEATURE(use_cw_file)
    dnl  The following allows relaying if the user authenticates,
    dnl  and disallows plaintext authentication (PLAIN/LOGIN) on
    dnl  non-TLS links:
    define(`confAUTH_OPTIONS', `A p y')dnl
    dnl
    dnl  Accept PLAIN and LOGIN authentications:
    TRUST_AUTH_MECH(`LOGIN PLAIN')dnl
    define(`confAUTH_MECHANISMS', `LOGIN PLAIN')dnl
    dnl
    dnl Make sure this paths correctly point to your SSL cert files:
    define(`confCACERT_PATH',`/etc/ssl/certs')
    define(`confCACERT',`/etc/ssl/cacert.pem')
    define(`confSERVER_CERT',`/etc/ssl/certs/server.crt')
    define(`confSERVER_KEY',`/etc/ssl/private/server.key')
    dnl
    FEATURE(`virtusertable', `hash /etc/mail/virtusertable.db')dnl
    OSTYPE(linux)dnl
    MAILER(local)dnl
    MAILER(smtp)dnl
    
然后使用使用 
    
    # m4 /etc/mail/sendmail.mc > /etc/mail/sendmail.cf
    
命令生成 ` sendmail.cf` 文件。 

**注意：** 如果您对 `sendmail.cf ` 语法感兴趣，请参阅 [这篇文章](<https://www.sendmail.org/~ca/email/doc8.12/op-sh-5.html>) 了解详情。

### sendmail.conf

` sendmail.conf ` 文件，如果存在，则也是配置 Sendmail 并最终生成 ` sendmail.cf ` 的一个配置文件。请阅读文件内含的注释了解详细信息。 

### local-host-names

请将您的域名写入 `local-host-names` 文件: 
    
    /etc/mail/local-host-names
    
    localhost
    your-domain.com
    mail.your-domain.com
    localhost.localdomain
    
请确保您的域名可以被 ` /etc/hosts` 文件解析。 

### access.db

创建文件 `/etc/mail/access` 然后写入规则以配置邮件转发、允许收信与拒信。假设你在 `10.5.0.0/24` 有一个 VPN，而且你希望转发来自该 IP 段的所有邮件： 
    
    /etc/mail/access
    
    10.5.0 RELAY
    127.0.0 RELAY
    
然后使用 
    
    # makemap hash /etc/mail/access.db < /etc/mail/access
    
命令处理生成 sendmail 可以使用的配置数据库。 

### aliases.db

编辑文件 `/etc/mail/aliases` ，反注释这一行： `#root: human being here` 并将其修改如下： 
    
    root:         your-username

你可以在此添加用户的别名。例如： 
    
    coolguy:      your-username
    somedude:     your-username

然后使用 
    
    # newaliases
    
命令进行处理。 

### virtusertable.db

创建 `virtusertable` 文件并在其中写入含有域名的别名：（这项功能在您的服务器绑定多域名时十分有用） 
    
    /etc/mail/virtusertable
    
    your-username@your-domain.com         your-username
    joe@my-other.tk                       joenobody
    
然后使用 
    
    # makemap hash /etc/mail/virtusertable.db < /etc/mail/virtusertable
    
命令进行处理。 

###  开机自动启动

启用并启动下列服务。请阅读[守护进程](<../zh-cn/Daemon_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Daemon \(简体中文\)")了解详情。 

  * `saslauthd.service`
  * `sendmail.service`
  * `sm-client.service`

###  SASL 验证

将用户添加至 SASL 数据库并设置用于 SMTP 身份验证的密码。 
    
    # saslpasswd2 -c your-username
    
注：您可以设置使用异于 SASL 的身份验证途径。这需要进一步修改配置文件，这里不赘述。 

##  小窍门

###  将某个域名的全部邮件转发至特定邮箱

若需将 **my-other.tk** 域名下所有用户的电子邮件转发到 **your-username@your-domain.com** ，请在 `/etc/mail/virtusertable` 文件中添加以下一行： 
    
    @my-other.tk        your-username@your-domain.com

不要忘记再次使用如下命令更新配置数据库： 
    
    # makemap hash /etc/mail/virtusertable.db < /etc/mail/virtusertable
    