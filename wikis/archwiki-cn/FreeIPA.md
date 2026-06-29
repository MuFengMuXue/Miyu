**翻译状态：**

  * 本文（或部分内容）译自 [FreeIPA](<https://wiki.archlinux.org/title/FreeIPA> "arch:FreeIPA")，最近一次同步于 2024-04-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/FreeIPA?diff=0&oldid=805318>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/FreeIPA_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [OpenLDAP](<../zh-cn/OpenLDAP.html> "OpenLDAP")
  * [Kerberos](<../zh-cn/Kerberos.html> "Kerberos")
  * [认证管理](<../zh-cn/%E8%BA%AB%E4%BB%BD%E7%AE%A1%E7%90%86.html> "认证管理")

[FreeIPA](<https://www.freeipa.org/>) 是一个基于Linux开源身份认证、身份管理、授权和审计解决方案，旨在为组织提供集中式身份和策略管理服务。 

这是一个类似于微软 Active Directory 域服务，整合了 LDAP、Kerberos、DNS、NTP、Dogtag Certificate System、389 Directory Syrver、SSSD 和 Apache HTTPServer，由红帽提供支持。 

##  安装

FreeIPA 分为服务端和客户端，目前(截至本文档创建:日期2024年4月) Arch Linux 官方并不提供 FreeIPA 的服务端和客户端的软件包，若想安装服务端，建议参照[官方文档](<https://www.freeipa.org/>)使用红帽系列发行版（如：[Fedora](<https://getfedora.org/>) \ [Red Hat Enterprise Linux](<https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux>) \ [CentOS](<https://www.centos.org/>) \ [Debian](<https://www.debian.org/>) ）或使用[容器](<https://hub.docker.com/r/freeipa/freeipa-server/>)进行安装和部署。本文档仅提供客户端简要配置说明。 

客户端版本可使用[安装](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html#%E5%AE%89%E8%A3%85%E4%B8%8E%E6%9B%B4%E6%96%B0%E8%BD%AF%E4%BB%B6%E5%8C%85> "AUR") [freeipa-client](<https://aur.archlinux.org/packages/freeipa-client/>)AUR，当然也可以不使用安装包，而使用手动配置与 FreeIPA 服务端进行连接，可以根据自己所需选择对应功能模块进行安装配置。 

下面是将当前客户端注册到 FreeIPA 服务端指定的域和领域。 
    
    # ipa-client-install --server=_ipa.example.org_ --domain=_example.org_ --realm=_EXAMPLE.ORG_

###  手动安装客户端

freeipa客户端 安装时已经默认将下列软件作为依赖进行安装，手动仅为满足某些设备仅实现部分功能。为了确保能与服务端进行连接，可根据需求安装下面软件包。 

  * **[Kerberos](<../zh-cn/Kerberos.html> "Kerberos")** — 用于Kerberos身份认证（必选项）。

     <http://web.mit.edu/kerberos/> || [krb5](<https://archlinux.org/packages/?name=krb5>)包

  * **SSSD** — 用于LADP和Kerberos认证的代理客户端（必选项）。

     <https://sssd.io/> || [sssd](<https://archlinux.org/packages/?name=sssd>)包

  * [NTP](<../zh-cn/Category:NTP.html> "NTP")——用于客户端与服务端时间同步（**强烈** 建议安装，若主机时间不一致将导致验证无法进行）。
  * **[Autofs](<../zh-cn/Autofs.html> "Autofs")** — 用于自动挂载目标文件系统，常见的用法如挂载漫游用户的家目录（可选项）。

     <https://www.kernel.org/doc/html/latest/filesystems/autofs.html> || [autofs](<https://aur.archlinux.org/packages/autofs/>)AUR

  * **certmonger** — 证书管理服务,实现于 FreeIPA 服务端自动化证书颁发和续定（可选项）。

     <https://www.pagure.io/certmonger> || [certmonger](<https://aur.archlinux.org/packages/certmonger/>)AUR

##  配置

###  手动配置客户端

#### SSSD

在目录`/etc/sssd/conf.d/`下添加配置文件。 
    
    /etc/sssd/conf.d/80-freeipa-_example_.conf
    
    [sssd]
    config_file_version = 2
    services = nss, pam, sudo, ssh
    domains = _EXAMPLE.ORG_
    #debug_level = 9
    
    [domain/_EXAMPLE.ORG_]
    #debug_level = 9
    cache_credentials = true
    krb5_store_password_if_offline = true
    id_provider = ipa
    auth_provider = ipa
    access_provider = ipa
    chpass_provider = ipa
    #ipa_domain=_example.org_            # **可选项**
    #ipa_server=_ipaserver.example.org_  # **可选项**
    ipa_hostname=_client.example.org_

**提示：** 若在已DNS中添加了相关 SRV 记录，以上所标识的 **可选项** 可不作配置。

NSCD 使用 [sssd](</wzh/index.php?title=Sssd&action=edit&redlink=1> "Sssd（页面不存在）")（英语：[SSSD](<https://wiki.archlinux.org/title/SSSD> "en:SSSD")） 认证代理，修改文件 /etc/nsswitch.conf。 
    
    /etc/nsswitch.conf
    
    passwd: files systemd **sss**
    group: files [SUCCESS=merge] systemd **sss**
    shadow: files systemd **sss**
    gshadow: files systemd
    **sudoers: files sss**
    
    publickey: files
    
    hosts: mymachines resolve [!UNAVAIL=return] files myhostname dns
    networks: files
    
    protocols: files
    services: files
    ethers: files
    rpc: files
    
    netgroup: files

使用下面命令查询或验证 sssd 与 FreeIPA 的连接信息。 
    
    sssctl domain-status _example.org_
    
#### krb5

修改文件`/ect/krb5.conf`,添加域 
    
    /ect/krb5.conf
    
    [libdefaults]
            default_realm = EXAMPLE.ORG
            dns_lookup_realm = false
            dns_lookup_kdc = false
            rdns = false
            ticket_lifetime = 24h
            forwardable = yes
            #allow_weak_crypto = yes  # Only if absolutely necessary. Currently FreeIPA supports strong crypto.
    
    [realms]
            EXAMPLE.ORG = {
                    admin_server = freeipaserver.example.org
                    kdc = freeipaserver.example.org:749
                    default_admin = example.org
            }
    
    [domain_realm]
            example.org = EXAMPLE.ORG
            .example.org = EXAMPLE.ORG
    
    [logging]
            default = FILE:/var/log/krb5libs.log
            kdc = FILE:/var/log/krb5kdc.log
            admin_server = FILE:/var/log/kadmin.log

###  注册客户端

现在服务端上注册客户端主机，下面操作请在服务端上执行； 

  1. 登录到管理员会话
         
         $ kinit admin

  2. 创建客户端记录
         
         $ ipa host-add --force --ip-address=_192.168.1.100_ _client.example.org_

**提示：** 需要根据您的实际情况修改对应的地址和域名，若您的主机没有固定的IP地址，可使用下列命令创建。
         
         $ ipa host-add _client.example.org_

  3. 授权主机 ipaserver 允许管理客户端 client 
         
         $ ipa host-add-managedby --hosts=_ipaserver.example.org_ _client.example.org_

  4. 为客户端生成密钥
         
         # ipa-getkeytab -s _ipaserver.example.org_  -p host/_client.example.org_ -k /tmp/client1.keytab

将刚生成的密钥下载到客户端，下面操作请在客户端上执行； 
    
    $ scp _user_ @_ipaserver.example.org_ :/tmp/client1.keytab /tmp/krb5.keytab
    # mv /tmp/krb5.keytab /etc/krb5.keytab
    
###  SSH整合

####  私钥认证

您可配置 SSHD 从 LDAP 服务上拉取用户 SSH 公钥，以此完成私钥认证。只需在`/etc/ssh/sshd_config.d/`目录下创建一个sshd的配置文件。 
    
    /etc/ssh/sshd_config.d/80-freeipa-example.conf
    
    AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys
    AuthorizedKeysCommandUser nobody

然后再[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `sshd.service` 服务。 

**提示：** 以下操作请在服务端上进行。

接下来添加公钥。您可用使用freeipa管理页面端进行添加，操作步骤：“身份” -> 选择 "用户类别" -> 选择对应 "用户名" -> 在 "账户设置" 中找到 ‘SSH公钥’，点击"添加",将您的 公钥文本 粘贴到出的对话框中，点击 “设置” 后完成操作。 

除了网页端添加还可使用命令行进行添加，示例如下： 

  * 创建用户时指定公钥信息。
        
        ipa user-add --sshpubkey="ssh-rsa AAAA..." _用户名_

  * 修改已有用户公钥信息。
        
        ipa user-mod --sshpubkey="ssh-rsa AAAA..." _用户名_

验证配置：
    
    $ sudo -u nobody sss_ssh_authorizedkeys _用户名_

如果配置正确，执行过程中应无报错信息。 

####  主机信任

您可配置 SSHD 从 sssd 服务上获取主机 SSH 公钥信息，以此完成主机指纹信任。只需在`/etc/ssh/sshd_config.d/`目录下创建一个sshd的配置文件。 
    
    /etc/ssh/sshd_config.d/81-sssd-knownHosts.conf
    
    GlobalKnownHostsFile /var/lib/sss/pubconf/known_hosts
    ProxyCommand /usr/bin/sss_ssh_knownhostsproxy -p %p %h

####  Kerberos 认证

SSH 客户端启用 Kerberos 认证。需在`/etc/ssh/sshd_config.d/`目录下创建一个sshd的配置文件。 
    
    /etc/ssh/sshd_config.d/82-kerberos-gssApiAuth.conf
    
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials yes

##  参考

  * [FreeIPA:项目官方页](<https://www.freeipa.org/>)
  * [维基百科:FreeIPA](<https://en.wikipedia.org/wiki/FreeIPA> "wikipedia:FreeIPA")
  * [红帽:Linux 域身份、身份验证和策略指南](<https://access.redhat.com/documentation/zh-cn/red_hat_enterprise_linux/7/html-single/linux_domain_identity_authentication_and_policy_guide/index>)
  * [GtiHub:sssd和OpenSSH集成.pdf](<https://github.com/freeipa/freeipa.github.io/blob/main/src/page/Freeipa30_SSSD_OpenSSH_integration.pdf>)
