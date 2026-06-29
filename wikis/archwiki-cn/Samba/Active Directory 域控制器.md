相关文章

  * [Active Directory Integration](</wzh/index.php?title=Active_Directory_Integration&action=edit&redlink=1> "Active Directory Integration（页面不存在）")
  * [Samba](<../../zh-cn/Samba.html> "Samba")
  * [SOGo](</wzh/index.php?title=SOGo&action=edit&redlink=1> "SOGo（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [Samba/Active Directory domain controller](<https://wiki.archlinux.org/title/Samba/Active_Directory_domain_controller> "arch:Samba/Active Directory domain controller")，最近一次同步于 2024-05-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Samba/Active_Directory_domain_controller?diff=0&oldid=805451>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Samba_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Active_Directory_domain_controller_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文描述了如何使用 [Samba](<../../zh-cn/Samba.html> "Samba") 搭建 Active Directory 域控制器。它假设所有配置文件都处于安装后的状态，未作任何更改。文章内容已在全新安装系统上验证过，没有（也不需要）除静态 IPv4 地址外的其它网络配置。最后，下面的大多数命令都需要提权。在不考虑操作规范的前提下，使用根用户会话运行命令会比按需提权更方便些。 

##  安装

**注意：** 确保在你的网络上可以通过主机名访问到服务器。详细信息请查看[网络配置#局域网主机名解析](<../../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E5%B1%80%E5%9F%9F%E7%BD%91%E4%B8%BB%E6%9C%BA%E5%90%8D%E8%A7%A3%E6%9E%90> "网络配置")。

除 Samba 的自带程序外，一个完整可用的 samba 域控制器还需要一些其它软件。先从官方仓库[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [krb5](<https://archlinux.org/packages/?name=krb5>)包，[ntp](<https://archlinux.org/packages/?name=ntp>)包，[python-dnspython](<https://archlinux.org/packages/?name=python-dnspython>)包，[python-markdown](<https://archlinux.org/packages/?name=python-markdown>)包,[openresolv](<https://archlinux.org/packages/?name=openresolv>)包 和 [samba](<https://archlinux.org/packages/?name=samba>)包。 

Samba 内置了一个全功能的 DNS 服务器，但如果你需要为外部域名维护 DNS 域，强烈建议换用 [BIND](<../../zh-cn/BIND.html> "BIND")。如果需要共享打印机，同时也要用到 [CUPS](<../../zh-cn/CUPS.html> "CUPS")。如有这些需要，请安装 [bind](<https://archlinux.org/packages/?name=bind>)包 和/或 [cups](<https://archlinux.org/packages/?name=cups>)包。 

##  创建新目录

###  置备

创建 Active Directory 域的第一步是进行置备。这包括配置内部 [LDAP](<../../zh-cn/OpenLDAP.html> "LDAP")、[Kerberos](<../../zh-cn/Kerberos.html> "Kerberos") 和 DNS 服务器，并按目录需求进行基础设置。如果你有配置目录服务器的经验，那你肯定知道多组件协同工作很可能会产生些问题。这也是为什么 Samba 的开发者选择提供内置版本的这些组件，上面安装的服务器包仅作为客户端工具进行安装。为 Samba 进行置备较为简单，只需执行以下命令： 
    
    # samba-tool domain provision --use-rfc2307 --interactive
    
####  参数说明

\--use-rfc2307
    该参数将 POSIX 属性（UID/GID）添加到了 AD Schema 中。如果你需要认证 Linux，BSD 或是 macOS 客户端（包括本地主机），就需用到该参数。

\--interactive
    该参数强制置备脚本以交互模式运行。

你也可以使用 `samba-tool domain provision --help` 查看置备步骤的文档。 

#### Interactive provision explanations

Realm
     **INTERNAL.DOMAIN.COM** \- This should be the same as the DNS domain in all caps. It is common to use an internal-only sub-domain to separate your internal domain from your external DNS domains, but it is not required.

Domain
     **INTERNAL** \- This will be the NetBIOS domain name, usually the leftmost DNS sub-domain but can be anything you like. For example, the name INTERNAL would not be very descriptive. Perhaps company name or initials would be appropriate. This should be entered in all caps, and should have a 15 character maximum length for compatibility with older clients.

Server Role
     **dc** \- This article assumes that your are installing the first DC in a new domain. If you select anything different, the rest of this article will likely be useless to you.

DNS Backend
     **BIND9_DLZ** or **SAMBA_INTERNAL** \- This is down to personal preference of the server admin. Again, if you are hosting DNS for external domains, you are strongly encouraged to use the **BIND9_DLZ** backend so that flat zone files can continue to be used and existing transfer rules can co-exist with the internal DNS server. If unsure, use the **SAMBA_INTERNAL** backend.

DNS forwarder IP address
     **xxx.xxx.xxx.xxx** or **none** \- This option is only presented when using the SAMBA_INTERNAL DNS backend. Supply the IP address of a DNS server for forwarding non local DNS queries, or use the string **none** to always do root lookups.

Administrator password
     **xxxxxxxx** \- You must select a _strong_ password for the administrator account. The minimum requirements are one uppercase letter, one number, and at least eight characters. If you attempt to use a password that does not meet the complexity requirements, provisioning will fail.

###  配置守护进程

#### NTPD

为你网络下的时间服务器创建 NTP 配置文件。相关介绍及额外配置可参考 [Network Time Protocol daemon](<../../zh-cn/Network_Time_Protocol_daemon.html> "Network Time Protocol daemon") 一文。 

按照如下内容修改 `/etc/ntp.conf`： 
    
    /etc/ntp.conf
    
    # Please consider joining the pool:
    #
    #     http://www.pool.ntp.org/join.html
    #
    # For additional information see:
    # - https://wiki.archlinux.org/index.php/Network_Time_Protocol_daemon
    # - http://support.ntp.org/bin/view/Support/GettingStarted
    # - the ntp.conf man page
    
    # 关联到 Arch 的 NTP 池
    server 0.arch.pool.ntp.org
    server 1.arch.pool.ntp.org
    server 2.arch.pool.ntp.org
    server 3.arch.pool.ntp.org
    
    # 限制
    restrict default kod limited nomodify notrap nopeer mssntp
    restrict 127.0.0.1
    restrict ::1
    restrict 0.arch.pool.ntp.org mask 255.255.255.255 nomodify notrap nopeer noquery
    restrict 1.arch.pool.ntp.org mask 255.255.255.255 nomodify notrap nopeer noquery
    restrict 2.arch.pool.ntp.org mask 255.255.255.255 nomodify notrap nopeer noquery
    restrict 3.arch.pool.ntp.org mask 255.255.255.255 nomodify notrap nopeer noquery
    
    # 偏移文件位置
    driftfile /var/lib/ntp/ntpd.drift
    
    # Location of the update directory
    ntpsigndsocket /var/lib/samba/ntp_signd/
    
创建状态目录并配置权限： 
    
    # install -d /var/lib/samba/ntp_signd
    # chown root:ntp /var/lib/samba/ntp_signd
    # chmod 0750 /var/lib/samba/ntp_signd
    
启用并启动 `ntpd.service`。 

#### BIND

如果你选择了 **BIND9_DLZ** 作为 DNS 后端，需要[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [bind](<https://archlinux.org/packages/?name=bind>)包 并创建如下 BIND 配置，相关介绍及额外配置可参考 [BIND](<../../zh-cn/BIND.html> "BIND") 一文。别忘了将 **x** 替换成实际值： 

创建 `/etc/named.conf` 文件： 
    
    /etc/named.conf
    
    // vim:set ts=4 sw=4 et:
    acl local-networks {
        127.0.0.0/8;
        xxx.xxx.xxx.xxx/xx;
    // 如要使用 IPv6，需移除下面的注释
        //::1/128;
        //xxxx:xxxx:xxxx:xxxx::/64;
    };
    
    options {
        directory "/var/named";
        pid-file "/run/named/named.pid";
        session-keyfile "/run/named/session.key";
    
        // 将该行取消注释以启用 IPv6 连接支持
        //  listen-on-v6 { any; };
        // 为无 IPv4 环境添加该行：
        //  listen-on { none; };
    
        // 将允许的子网或主机加入到 local-networks acl 中
        allow-query       { local-networks; };
        allow-recursion   { local-networks; };
        allow-query-cache { local-networks; };
        allow-transfer    { none; };
        allow-update      { none; };
    
        version none;
        hostname none;
        server-id none;
    
        auth-nxdomain yes;
        datasize default;
        empty-zones-enable no;
        tkey-gssapi-keytab "/var/lib/samba/bind-dns/dns.keytab";
    
        // 将该行取消注释以使用 ISP 的转发器
        //  forwarders { xxx.xxx.xxx.xxx; xxx.xxx.xxx.xxx; };
    };
    
    zone "localhost" IN {
        type master;
        file "localhost.zone";
    };
    
    zone "0.0.127.in-addr.arpa" IN {
        type master;
        file "127.0.0.zone";
    };
    
    zone "1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa" {
        type master;
        file "localhost.ip6.zone";
    };
    
    // 加载 AD 内置区域
    include "/var/lib/samba/bind-dns/named.conf";
    
    //zone "example.org" IN {
    //    type slave;
    //    file "example.zone";
    //    masters {
    //        192.168.1.100;
    //    };
    //    allow-query { any; };
    //    allow-transfer { any; };
    //};
    
    logging {
        channel xfer-log {
            file "/var/log/named.log";
                print-category yes;
                print-severity yes;
                severity info;
            };
            category xfer-in { xfer-log; };
            category xfer-out { xfer-log; };
            category notify { xfer-log; };
    };
    
配置权限： 
    
    # chgrp named /var/lib/samba/private/dns.keytab
    # chmod g+r /var/lib/samba/private/dns.keytab
    # touch /var/log/named.log
    # chown root:named /var/log/named.log
    # chmod 664 /var/log/named.log
    
启用并启动 `named.service`。 

转发器值可以选用你的 ISP 的 DNS 服务器，谷歌（8.8.8.8，8.8.4.4，2001:4860:4860::8888 和 2001:4860:4860::8844）及 OpenDNS（208.67.222.222，208.67.220.220，2620:0:ccc::2 和 2620:0:ccd::2）也免费提供了公共 DNS 服务器，具体最佳值取决于你的现有网络。 

####  Kerberos 客户端工具

上面的置备步骤会创建一个可与 Samba 域控制器搭配使用的 krb5.conf 文件。使用如下命令进行安装： 
    
    # mv /etc/krb5.conf{,.default}
    # cp /var/lib/samba/private/krb5.conf /etc
    
#### DNS

你现在需要使用本地 DNS 服务器了，重新配置 resolvconf 以仅使用 localhost 进行 DNS 查询。创建 `/etc/resolv.conf.tail` 文件（不要忘了将 **internal.domain.tld** 替换为你的内部域名）： 
    
    # Samba 配置
    search **internal.domain.tld**
    # 如要使用 IPv6，需移除下行注释
    #nameserver ::1
    nameserver 127.0.0.1
    
配置权限并生成新的 `/etc/resolv.conf` 文件： 
    
    # chmod 644 /etc/resolv.conf.tail
    # resolvconf -u
    
#### Samba

启用并启动 `samba.service`。如果你想使用 LDB 工具，需额外通过创建 `/etc/profile.d/sambaldb.sh` 来设置 **LDB_MODULES_PATH** ： 
    
    export LDB_MODULES_PATH="${LDB_MODULES_PATH}:/usr/lib/samba/ldb"
    
设置权限并对其使用 source： 
    
    # chmod 0755 /etc/profile.d/sambaldb.sh
    # . /etc/profile.d/sambaldb.sh
    
###  测试

#### DNS

首先验证 DNS 是否正常。执行如下命令，将 **internal.domain.com** 和 **server** 替换为对应的值： 
    
    # host -t SRV _ldap._tcp.**internal.domain.com**.
    # host -t SRV _kerberos._udp.**internal.domain.com**.
    # host -t A **server**.**internal.domain.com**.
    
输出应该如下： 
    
    _ldap._tcp.internal.domain.com has SRV record 0 100 389 server.internal.domain.com.
    _kerberos._udp.internal.domain.com has SRV record 0 100 88 server.internal.domain.com.
    server.internal.domain.com has address xxx.xxx.xxx.xxx

####  NT 认证

接着，确认密码认证是否正常工作： 
    
    # smbclient //localhost/netlogon -U Administrator -c 'ls'
    
将会出现提示要求输入密码（即你之前设定的密码），并将出现如下目录列表： 
    
      .                                   D        0  Wed Nov 27 23:59:07 2013
      ..                                  D        0  Wed Nov 27 23:59:12 2013
    
    		50332 blocks of size 2097152. 47185 blocks available

#### Kerberos

现在验证 KDC 是否正常工作。确保替换了 **INTERNAL.DOMAIN.COM** ，并且使用了全大写字符： 
    
    # kinit administrator@**INTERNAL.DOMAIN.COM**
    
将会出现提示要求输入密码，并产生如下输出： 
    
    Warning: Your password will expire in 41 days on Wed 08 Jan 2014 11:59:11 PM CST

检查是否确实拿到了票据： 
    
    # klist
    
输出应该如下： 
    
    Ticket cache: FILE:/tmp/krb5cc_0
    Default principal: administrator@INTERNAL.DOMAIN.COM
    
    Valid starting       Expires              Service principal
    11/28/2013 00:22:17  11/28/2013 10:22:17  krbtgt/INTERNAL.DOMAIN.COM@INTERNAL.DOMAIN.COM
    	renew until 11/29/2013 00:22:14

最后，通过 smbclient 使用刚拿到的票据进行验证。将 **server** 替换为对应的服务器名： 
    
    # smbclient //**server** /netlogon -k -c 'ls'
    
输出应与上述密码认证测试的输出一致。 

### Additional configuration

#### DNS

You will also need to create a reverse lookup zone for each subnet in your environment in DNS. It is important that this is kept in Samba's DNS as opposed to BIND to allow for dynamic updates by cleints. For each subnet, create a reverse lookup zone with the following commands. Replace **server**.**internal**.**domain**.**tld** and **xxx**.**xxx**.**xxx** with appropriate values. For **xxx**.**xxx**.**xxx** , use the first three octets of the subnet in reverse order (for example: 192.168.0.0/24 becomes 0.168.192): 
    
    # samba-tool dns zonecreate **server**.**internal**.**domain**.**tld** **xxx**.**xxx**.**xxx**.in-addr.arpa -U Administrator
    
Now, add a record for you server (if your server is multi-homed, add for each subnet) again substituting appropriate values as above. **zzz** will be replaced by the fourth octet of the IP for the server: 
    
    # samba-tool dns add **server**.**internal**.**domain**.**tld** **xxx**.**xxx**.**xxx**.in-addr.arpa **zzz** PTR **server**.**internal**.**domain**.**tld** -U Administrator
    
Finally, test the lookup. Replace **xxx**.**xxx**.**xxx**.**xxx** with the IP of your server: 
    
    # host -t PTR **xxx**.**xxx**.**xxx**.**xxx**
    
You should get output similar to the following: 
    
    xxx.xxx.xxx.xxx.in-addr.arpa domain name pointer server.internal.domain.tld.
    
#### TLS

默认不启用 TLS，但在初始化 DC 时会创建一个默认证书。从 Samba 4.3.8 和 4.2.2 开始，默认禁用非加密 LDAP 绑定。在不影响安全性的前提下，你必须要配置 TLS 才能将 Samba 作为认证源使用。如要使用默认证书，请将下列内容添加到 `/etc/samba/smb.conf` 的“[global]”部分下： 
    
    /etc/samba/smb.conf
    
    [global]
    tls enabled  = yes
    tls keyfile  = tls/key.pem
    tls certfile = tls/cert.pem
    tls cafile   = tls/ca.pem

如果需要可信证书，请创建一个签名密钥和一个证书请求（详细步骤参见 [OpenSSL](<../../zh-cn/OpenSSL.html> "OpenSSL")）。让你选择的证书机构对请求签名，然后将其放置在配置的文件夹下。如果证书机构要求使用中间证书，可以将证书串在一起（先是服务器证书，然后是中间证书），然后将 **tls cafile** 留空。 

重启 `samba` 以应用更改。 

## Adding a second domain controller to an existing domain

### Prerequisites

As with the provisioning setup when setting up a new domain, you must have [ntp](<https://archlinux.org/packages/?name=ntp>)包 configured per [the above instructions](<#NTPD>). Additionally, some of the arguments and parameters on the original domain setup must be replicated here. 

#### Argument explanations

\--option='idmap_ldb:use rfc2307 = yes'
    this is required if you elected to include Unix UID/GID support on your existing domain (using the **\--use-rfc2307** option for Samba's provision step or applied the RFC 2307 schema extensions).

\--dns-backend=**DNSTYPE**
    replace **DNSTYPE** with **BIND9_DLZ** or **SAMBA_INTERNAL** \- This is again down to personal preference of the server admin. If using **BIND9_DLZ** backend, you will need to configure [bind](<https://archlinux.org/packages/?name=bind>)包 as per [the above instructions](<#BIND>) after joining the domain.

\--option="dns forwarder="**xxx.xxx.xxx.xxx** "
    this is only valid for the SAMBA_INTERNAL DNS backend which allows you to specify a DNS forwarder. Replace **xxx.xxx.xxx.xxx** with appropriate value.

\--site=**SITE**
    if you have multiple sites defined, use this to join directly in that site.

See the output of `samba-tool domain join --help` for additional options. 

### Joining an existing domain as a new DC

Execute the following command (adding any necessary parameters above to the end of the command): 
    
    # samba-tool domain join **internal.domain.tld** DC -U"**INTERNAL** \**administrator** "
    
Now copy the `krb5.conf`: 
    
    # cp /var/lib/samba/private/krb5.conf /etc/krb5.conf
    
If you used the RFC 2307 schema extensions, you need to copy the idmap from an existing DC. If using Samba, execute the following command from another DC: 
    
    # tdbbackup -s .bak /var/lib/samba/private/idmap.ldb
    
This will generate a file `/var/lib/samba/private/idmap.ldb.bak`, transfer this file to the new server in the `/var/lib/samba/private` directory, removing the .bak extension. If you intend to keep multiple DCs, you will need to automate this process going forward using one of the methods listed on the Samba website [here](<https://wiki.samba.org/index.php/Joining_a_Samba_DC_to_an_Existing_Active_Directory#Built-in_User_.26_Group_ID_Mappings>). This also applies to transferring the idmap from Windows DCs. 

Enable and start the `samba.service` unit. 

If using BIND9_DLZ DNS backend, you'll need to follow the [BIND](<#BIND>) section above. Check if the `/var/lib/samba/private/dns` directory is created, and if not, run the following command (ignore warning about updating named.conf): 
    
    # samba_upgradedns --dns-backend=BIND9_DLZ
    
Restart the `named.service` and then update the DNS records with the following command: 
    
    # samba_dnsupdate --all-names --use-samba-tool --verbose
    
Now proceed with LDB configuration and testing as with a new domain [here](<#Samba>). 

### Transferring the FSMO roles

If this is intended to replace an existing domain controller, you will need to transfer the FSMO roles before demoting the existing DC. This is currently outside the scope of this document. See the Samba wiki [here](<https://wiki.samba.org/index.php/Transferring_and_Seizing_FSMO_Roles>). 

##  额外服务

###  打印

作为域控制器的 Samba 服务器默认不会启用打印服务。你需要在 `/etc/samba/smb.conf` 的 global 部分添加下列内容： 
    
    /etc/samba/smb.conf
    
    [global]
    ...
            rpc_server:spoolss = external
            rpc_daemon:spoolssd = fork
            printing = CUPS
    ...
    [printers]
           path = /var/spool/samba/
           printable = yes
    
以上示例会为所有 CUPS 打印队列启用自动共享。如果你只想共享特定打印队列，可以添加如下内容（先将上面的 **[printers]** 共享移除）： 
    
    /etc/samba/smb.conf
    
    [global]
    ...
            load printers = no
    ...
    # 打印共享示例
    [HPDJ3050]
           path = /var/spool/samba/
           printable = yes
           printer name = hpdj3050
    
## Tips and tricks

### DHCP with dynamic DNS updates

It should be noted that using this method will affect functionality of windows clients, as they will still attempt to update DNS on their own. When this occurs, the machine will be denied permission to do so as the record will be owned by the dhcp user rather than the machine account. While this is essentially harmless, it will generate warnings in the system log of the offending machine. You should create a GPO to overcome this, but unfortunately, Samba does not yet have a command line utility to modify GPOs. You will need a Windows PC with the RSAT tools installed. Simply create a dedicated GPO with the Group Policy Editor, and apply only to OUs that contain workstations using DHCP (so that Samba/Windows servers and statically configured Samba/Windows clients can still update using 'ipconfig /registerdns') and configure the following settings: 
    
    Computer Configuration
      Policies
        Administrative Templates
          Network
            DNS Client
              Dynamic Update = Disabled
              Register PTR Records = Disabled

[Install](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [dhcp](<https://archlinux.org/packages/?name=dhcp>)包, [sudo](<https://archlinux.org/packages/?name=sudo>)包, and the [samba-dhcpd-update](<https://aur.archlinux.org/packages/samba-dhcpd-update/>)AUR packages. 

Create an unprivileged user in AD for performing the updates. When prompted for password, use a secure password. 63 random, mixed case, alpha-numeric characters is sufficient. Optionally samba-tool also takes a random argument: 
    
    # samba-tool user create dhcp --description="Unprivileged user for DNS updates via DHCP server"
    
Since this is a service account, disabling password expiration on the user account is recommended, but not required: 
    
    # samba-tool user setexpiry dhcp --noexpiry
    
Give the user privileges to administer DNS: 
    
    # samba-tool group addmembers DnsAdmins dhcp
    
Create an SPN and export the users credentials to a private keytab: 
    
    # samba-tool spn add **server** /**server**.**internal**.**domain**.**tld** @**INTERNAL**.**DOMAIN**.**TLD** dhcp
    # samba-tool domain exportkeytab --principal=dhcp@**INTERNAL**.**DOMAIN**.**TLD** dhcpd.keytab
    # install -vdm 755 /etc/dhcpd
    # mv dhcpd.keytab /etc/dhcpd
    # chown root:root /etc/dhcpd/dhcpd.keytab
    # chmod 400 /etc/dhcpd/dhcpd.keytab
    
Modify the `dhcpd-update-samba-dns.conf` file with the following commands (substituting correct values for **server** , **internal**.**domain**.**tld** , and **INTERNAL**.**DOMAIN**.**TLD**): 
    
    /etc/dhcpd/dhcpd-update-samba-dns.conf
    
    # Variables
    KRB5CC="/tmp/dhcpd4.krb5cc"
    KEYTAB="/etc/dhcpd/dhcpd.keytab"
    DOMAIN="**internal**.**domain**.**tld** "
    REALM="**INTERNAL**.**DOMAIN**.**TLD** "
    PRINCIPAL="dhcp@${REALM}"
    NAMESERVER="**server**.${DOMAIN}"
    ZONE="${DOMAIN}"
    
Grant the dhcp user account permissions to run the update script without a password prompt (replace **server** with the hostname of the server): 
    
    /etc/sudoers.d/dhcp-update
    
    dhcp **server** = (root) NOPASSWD: /usr/bin/dhcpd-update-samba-dns.sh
    
Configure the dhcpd server following the [dhcpd](<../../zh-cn/Dhcpd.html> "Dhcpd") article and add the following to all subnet declarations in the `/etc/dhcpd.conf` file that provide DHCP service: 
    
      on commit {
        set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
        set ClientName = pick-first-value(option host-name, host-decl-name);
        execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "add", ClientIP, ClientName);
      }
    
      on release {
        set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
        set ClientName = pick-first-value(option host-name, host-decl-name);
        execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "delete", ClientIP, ClientName);
      }
    
        on expiry {
        set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
        set ClientName = pick-first-value(option host-name, host-decl-name);
        execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "delete", ClientIP, ClientName);
    
Here is a complete example `/etc/dhcpd.conf` file for reference: 
    
    /etc/dhcpd.conf
    
    subnet **192.168.1.0** netmask **255.255.255.0** {
      range **192.168.1.100** **192.168.1.199** ;
      option subnet-mask **255.255.255.0** ;
      option routers **192.168.1.254** ;
      option domain-name "**internal.domain.tld** ";
      option domain-name-servers **192.168.1.1** ;
      option broadcast-address **192.168.1.255** ;
      default-lease-time 28800;
      max-lease-time 43200;
      authoritative;
    
      on commit {
        set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
        set ClientName = pick-first-value(option host-name, host-decl-name);
        execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "add", ClientIP, ClientName);
      }
    
      on release {
        set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
        set ClientName = pick-first-value(option host-name, host-decl-name);
        execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "delete", ClientIP, ClientName);
      }
    
        on expiry {
        set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
        set ClientName = pick-first-value(option host-name, host-decl-name);
        execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "delete", ClientIP, ClientName);
      }
    }
    
Finally, enable and start (or restart) the `dhcpd4` service. 

### Transferring users from one directory to another

Unfortunately, there is no built-in utility to export users from one directory to another. This is one way, albeit exceptionally ugly, to get the user specific fields out of your existing SAM and into a suitable LDIF format for ldbmodify: 
    
    # ldbsearch -H /var/lib/samba/private/sam.ldb \
        -s sub -b cn=Users,dc=_internal_ ,dc=_domain_ ,dc=_tld_ '(objectClass=user)' | \
        grep -e "^\# record" -e "^accountExpires:" -e "^c:" -e "^cn:" -e "^co:" -e "^codePage:" \
             -e "^comment:" -e "^company:" -e "^countryCode:" -e "^department:" \
             -e "^description:" -e "^displayName" -e "^displayNamePrintable:" \
             -e "^distinguishedName" -e "^division:" -e "^dn:" -e "^employeeID:" \
             -e "^facsimileTelephoneNumber:" -e "^generationQualifier:" \
             -e "^givenName" -e "^homeDirectory:" -e "^homeDrive:" -e "^homePhone:" \
             -e "^homePostalAddress:" -e "^info:" -e "^initials:" \
             -e "^internationalISDNNumber:" -e "^ipPhone:" -e "^l:" -e "^mail:" \
             -e "^manager:" -e "^middleName:" -e "^mobile:" -e "^name:" -e "^o:" \
             -e "^objectClass" -e "^otherFacsimileTelephoneNumber:" \
             -e "^otherHomePhone:" -e "^otherIpPhone:" -e "^otherMailbox:" \
             -e "^otherMobile:" -e "^otherPager:" -e "^otherTelephone:" -e "^pager:" \
             -e "^personalTitle:" -e "^physicalDeliveryOfficeName:" -e "^postalAddress:" \
             -e "^postalCode:" -e "^postOfficeBox:" -e "^proxyAddresses\: SMTP" \
             -e "^proxyAddresses: smtp" -e "^referredDeliveryMethod:" \
             -e "^primaryInternationalISDNNumber:" -e "^primaryTelexNumber:" \
             -e "^profilePath:" -e "^registeredAddress:" -e "^sAMAccountName:" \
             -e "^scriptPath:" -e "^sn:" -e "^st:" -e "^street:" -e "^streetAddress:" \
             -e "^telephoneNumber:" -e "^teletexTerminalIdentifier:" \
             -e "^telexNumber:" -e "^title:" -e "^userAccountControl:" -e "^userPrincipalName:"\
             -e "^url:" -e "^userSharedFolder:" -e "^userSharedFolderOther:" -e "^wWWHomePage:" | \
        sed '/^dn:.*/ a\changetype: add' | sed '/^# record/ i\\n' > user-export.ldif
    
Explanation: Run an ldbsearch in the users container only, using sub-tree search for objectclass=user. If you need the whole directory, you can modify the search base to use the root or some other OU. The output from ldbsearch is then piped into a really long grep command that returns only appropriate attributes to keep in the new directory. This is obviously subjective, and probably should be tailored to your specific use case. Finally, we use sed to insert the changetype line (needed to tell ldbmodify that we are adding a user), and prefix with a blank line (to make it easier to read) for each exported object. 

**注意：** You will need to modify the output file and remove any objects that you do not want transferred. The output file will contain objects (service users, built-ins, etc.) that can break your new directory if you fail to remove them! It will also contain the old domain in both the "dn" and "distinguishedName" attributies that must be changed before import.

To import, after editing the file and transferring to the new server, simply run the following command on your new samba domain controller: 
    
    # ldbmodify -H /var/lib/samba/private/sam.ldb user-export.ldif
    
###  密码复杂度

Samba 默认要求使用强密码。使用以下命令可以禁用复杂度检查： 
    
    # samba-tool domain passwordsettings set --complexity=off
    
详细信息请参考 Samba 维基的[密码设置对象](<https://wiki.samba.org/index.php/Password_Settings_Objects>)一节。 
