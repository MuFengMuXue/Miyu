相关文章

  * [LDAP 认证](<../zh-cn/LDAP_%E8%AE%A4%E8%AF%81.html> "LDAP 认证")
  * [LDAP Hosts](</wzh/index.php?title=LDAP_Hosts&action=edit&redlink=1> "LDAP Hosts（页面不存在）")
  * [认证管理](<../zh-cn/%E8%BA%AB%E4%BB%BD%E7%AE%A1%E7%90%86.html> "认证管理")

**翻译状态：**

  * 本文（或部分内容）译自 [openLDAP](<https://wiki.archlinux.org/title/openLDAP> "arch:openLDAP")，最近一次同步于 2024-05-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/openLDAP?diff=0&oldid=805757>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/openLDAP_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[OpenLDAP](<https://www.openldap.org/>) 是 LDAP 协议的一个开源实现。LDAP 服务器本质上是一个为只读访问而优化的非关系型数据库。它主要用做地址簿查询（如 email 客户端）或对各种服务访问做后台认证以及用户数据权限管控。（例如，访问 Samba 时，它可以起到域控制器的作用；或者 [Linux 系统认证](<../zh-cn/LDAP_%E8%AE%A4%E8%AF%81.html> "LDAP 认证")时代替 `/etc/passwd` 的作用。） 

**注意：** 在跟 OpenLDAP 相关的命令中，以 `ldap` 开头的命令（如：`ldapsearch`）是客户端工具，以 `slap` 开头的命令（如：`slapcat`）是服务端工具。

本页面内容仅基于一个基本的 OpenLDAP 安装做简要配置说明。 

**提示：** 目录服务是一个庞大的主题，其配置可以非常复杂。如果你是一个完全的新手，[这里](<https://www.brennan.id.au/20-Shared_Address_Book_LDAP.html>)有一份详尽的介绍文档。该文档通俗易懂，即使你对 LDAP 一窍不通也完全可以引领你入门。

##  安装

OpenLDAP 软件包同时包含了服务器和客户端。请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [openldap](<https://archlinux.org/packages/?name=openldap>)包。 

##  配置

###  服务端

**注意：**

  * 如果你在使用过时的 `slapd.conf` 配置文件，可以使用以下命令将其转换为新的 `cn=config` 数据库：

    $ slaptest -f /etc/openldap/slapd.conf -F /etc/openldap/slapd.d/
    
  * 如果你现在的设备上存在 OpenLDAP 数据库，且想要将其移除，可以清空 `/var/lib/openldap/openldap-data/` 下的所有内容。因此，请备份好 `DB_CONFIG`。

作为服务端，Slapd 将其所有配置保存在其数据库内。因此，我们需要先将配置编写为 LDIF 文件，然后将其导入。 

首先创建 `/var/lib/openldap/openldap-data/` 目录，LDAP 数据库将存放在该位置下（OpenLDAP 将其称为“database 1”）： 
    
    # install -m 0700 -o ldap -g ldap -d /var/lib/openldap/openldap-data/
    
然后为 LDAP 配置数据库（“database 0”）创建新路径： 
    
    # install -m 0670 -o root -g ldap -d /etc/openldap/slapd.d
    
创建 `/etc/openldap/config.ldif`，其中包括如下最小可用配置： 
    
    /etc/openldap/config.ldif
    
    # The root config entry
    dn: cn=config
    objectClass: olcGlobal
    cn: config
    olcArgsFile: /run/openldap/slapd.args
    olcPidFile: /run/openldap/slapd.pid
    
    # Schemas
    dn: cn=schema,cn=config
    objectClass: olcSchemaConfig
    cn: schema
    
    # TODO: Include further schemas as necessary
    include: file:///etc/openldap/schema/core.ldif
    
    # The config database
    dn: olcDatabase=config,cn=config
    objectClass: olcDatabaseConfig
    olcDatabase: config
    olcRootDN: cn=Manager,**$BASEDN**
    
    # The database for our entries
    dn: olcDatabase=mdb,cn=config
    objectClass: olcDatabaseConfig
    objectClass: olcMdbConfig
    olcDatabase: mdb
    olcSuffix: **$BASEDN**
    olcRootDN: cn=Manager,**$BASEDN**
    olcRootPW: **$PASSWD**
    olcDbDirectory: /var/lib/openldap/openldap-data
    # TODO: Create further indexes
    olcDbIndex: objectClass eq

配置中需要根据需要修改部分内容： 

  * 所有 `$BASEDN` 都需要被替换为有效 DN。假设你手上的域名为 `example.com`，那你可以使用 `dc=example,dc=com`。
  * `$PASSWD` 需替换为加盐并哈希化的密码，可通过运行 `slappasswd` 来生成。

另外，你也可以添加更多 [schema](<https://www.openldap.org/doc/admin24/schema.html>)，并创建额外[索引](<https://www.openldap.org/doc/admin24/tuning.html#Indexes>)来提高数据库性能。具体实现取决于用例，但也有几点建议可供参考。对于 [LDAP 认证](<../zh-cn/LDAP_%E8%AE%A4%E8%AF%81.html> "LDAP 认证")，你需要添加下面三个 schema 以使用 `posixAccount` 对象类来储存用户信息。 

**注意：** 额外索引需放置在开头的块中，空行分隔将使配置文件无效。
    
    # TODO: Create further indexes
    olcDbIndex: objectClass eq
    olcDbIndex: uid pres,eq
    olcDbIndex: mail pres,sub,eq
    olcDbIndex: cn,sn pres,sub,eq
    olcDbIndex: dc eq
    
    # Additional schemas
    # RFC1274: Cosine and Internet X.500 schema
    include: file:///etc/openldap/schema/cosine.ldif
    # RFC2307: An Approach for Using LDAP as a Network Information Service
    # Check RFC2307bis for nested groups and an auxiliary posixGroup objectClass (way easier)
    include: file:///etc/openldap/schema/nis.ldif
    # RFC2798: Internet Organizational Person
    include: file:///etc/openldap/schema/inetorgperson.ldif

Allow logins to the `ldap` user account with `chsh`, typically selecting the shell `/bin/bash`. 然后以 `ldap` 用户身份导入设置： 
    
    [ldap]$ slapadd -n 0 -F /etc/openldap/slapd.d/ -l /etc/openldap/config.ldif
    
你也可以直接以 `root` 用户运行该命令。但如果你这么做，请确保 `ldap` 可以查看 `/etc/openldap/slapd.d/` 的内容： 
    
    # slapadd -n 0 -F /etc/openldap/slapd.d/ -l /etc/openldap/config.ldif
    # chown -R ldap:ldap /etc/openldap/*
    
如果一切顺利，你将能看到 `/etc/openldap/slapd.d` 下的目录，名称类似于 `cn=config`。 

默认情况下，OpenLDAP 会不加密监听所有网络接口。如果要使其仅监听本地 IP 接口，可以编辑 `slapd.service` 读取的环境变量文件： 
    
    /etc/conf.d/slapd
    
    SLAPD_URLS="ldap://127.0.0.1/ ldap://[::1]"
    SLAPD_OPTIONS=

最后，通过[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `slapd.service` 来启动 _slapd_ 守护进程。 

**注意：**

  * 如果你想让目录接受来自网络的请求，建议使用 TLS。详细内容请参考[#基于 TLS 的 OpenLDAP](<#%E5%9F%BA%E4%BA%8E_TLS_%E7%9A%84_OpenLDAP>)。
  * 如果你计划使用 LDAP 服务器进行认证，建议查看 [LDAP 认证#服务端配置](<../zh-cn/LDAP_%E8%AE%A4%E8%AF%81.html#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%85%8D%E7%BD%AE> "LDAP 认证") 中的访问控制配置部分。
  * 不应使用 Berkeley DB（BDB）。对于一般的 _slapd_ 数据库，建议使用 [slapd(8)](<https://man.archlinux.org/man/slapd.8>) 的 mdb 后端作为主后端。它使用了 OpenLDAP 自己的轻量内存映射数据库（LMDB）实现来存储数据，被设计用于取代 Berkeley DB 后端。[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")中的 OpenLDAP 包默认使用 mdb。

###  客户端

客户的配置文件位于 `/etc/openldap/ldap.conf`。 

这个配置很简单，只需要将 `BASE` 设置为服务器的前缀，将 `URI` 设置为服务器的地址: 
    
    /etc/openldap/ldap.conf
    
    BASE            dc=example,dc=com
    URI             ldap://localhost

要使用 SSL 的话: 

  * `URI` 的协议 (ldap 或 ldaps) 要和 slapd 配置一致
  * 要使用自签名的证书，在 `ldap.conf` 中添加 `TLS_REQCERT allow` 一行
  * 要使用由认证机构签名的证书，在 `ldap.conf` 中添加 `TLS_CACERTDIR /usr/share/ca-certificates/trust-source` 一行.

###  创建初始项

**注意：** 如果你计划使用 LDAP 服务器进行认证，你应该按照 [LDAP 认证](<../zh-cn/LDAP_%E8%AE%A4%E8%AF%81.html#%E5%AF%BC%E5%85%A5%E5%9F%BA%E6%9C%AC%E7%BB%84%E7%BB%87%E6%9E%B6%E6%9E%84> "LDAP 认证") 一文导入 `base.ldif`，而不是遵循下面的步骤。

配置好客户端后，创建根项和管理员（Manager）角色项： 
    
    $ ldapadd -x -D 'cn=Manager,dc=example,dc=com' -W
    dn: dc=example,dc=com
    objectClass: dcObject
    objectClass: organization
    dc: example
    o: Example
    description: Example directory
    
    dn: cn=Manager,dc=example,dc=com
    objectClass: organizationalRole
    cn: Manager
    description: Directory Manager
    ^D

第一行后的内容是在 stdin 输入的，或者用 `-f` 选项从文件或重定向读入. 

###  安装后测试

运行下面命令： 
    
    $ ldapsearch -x '(objectclass=*)' -b 'dc=example,dc=com'
    
或认证为 rootdn (将 `-x` 替换为 `-D _user_ -W`), 以上面的配置为例： 
    
    $ ldapsearch -D "cn=Manager,dc=example,dc=com" -W '(objectclass=*)' -b 'dc=example,dc=com'
    
应该能看到数据库中的信息. 

###  基于 TLS 的 OpenLDAP

**注意：**[上游文档](<https://www.openldap.org/doc/>)比本节内容更加完整实用。

如果通过网络访问 OpenLDAP 服务器，尤其是当你的服务器上保存有敏感数据时，明文传输这些数据存在被他人嗅探的风险。下面章节将指导你如何设置 LDAP 服务器与客户端之间的 SSL 连接以加密传输数据。 

要使用 TLS，你必须获得一个证书。测试时可以使用 _自签名_ 证书。关于证书的详细信息请参阅 [OpenSSL](<../zh-cn/OpenSSL.html> "OpenSSL")。 

**警告：** OpenLDAP 不能使用关联了口令的证书。

####  创建一个自签名证书

输入下列命令创建一个 _自签署_ 证书： 
    
    $ openssl req -new -x509 -nodes -out slapdcert.pem -keyout slapdkey.pem -days 365
    
You will be prompted for information about your LDAP server. Much of the information can be left blank. The most important information is the common name. This must be set to the DNS name of your LDAP server. If your LDAP server's IP address resolves to example.org but its server certificate shows a CN of bad.example.org, LDAP clients will reject the certificate and will be unable to negotiate TLS connections (apparently the results are wholly unpredictable). 

Now that the certificate files have been created copy them to `/etc/openldap/ssl/` (create this directory if it does not exist) and secure them. `slapdcert.pem` must be world readable because it contains the public key. `slapdkey.pem` on the other hand should only be readable for the ldap user for security reasons: 
    
    # mv slapdcert.pem slapdkey.pem /etc/openldap/ssl/
    # chmod -R 755 /etc/openldap/ssl/
    # chmod 400 /etc/openldap/ssl/slapdkey.pem
    # chmod 444 /etc/openldap/ssl/slapdcert.pem
    # chown ldap /etc/openldap/ssl/slapdkey.pem
    
####  为 slapd 配置 SSL

Edit the configuration to tell LDAP where the certificate files reside by executing the following command: 

**注意：** The latest version of OpenLDAP (2.4.45) uses OpenSSL and _not_ GnuTLS. This means that current versions of OpenLDAP **do** in fact know how to handle the [DEFAULT TLSCipherSuite](<https://www.openssl.org/docs/man1.1.1/man1/ciphers.html#CIPHER-STRINGS>). To prove this one could run `ldd /usr/bin/slapd`.
    
    ldapmodify -D 'cn=Manager,dc=example,dc=com' -W
    
    dn: cn=config
    add: olcTLSCertificateFile
    olcTLSCertificateFile: /etc/openldap/ssl/slapdcert.pem
    -
    add: olcTLSCertificateKeyFile
    olcTLSCertificateKeyFile: /etc/openldap/ssl/slapdkey.pem

If you are using a signed SSL Certificate from a certification authority such as [Let’s Encrypt](</wzh/index.php?title=Let%E2%80%99s_Encrypt&action=edit&redlink=1> "Let’s Encrypt（页面不存在）"), you will also need to specify the path to the root certificates database and your intermediary certificate. You will also need to change ownership of the _.pem_ files and intermediary directories to make them readable to the user `ldap`: 
    
    ldapmodify -D 'cn=Manager,dc=example,dc=com' -W
    
    dn: cn=config
    add: olcTLSCACertificateFile
    olcTLSCACertificateFile: /etc/letsencrypt/live/ldap.my-domain.com/chain.pem
    -
    add: olcTLSCertificateFile
    olcTLSCertificateFile: /etc/letsencrypt/live/ldap.my-domain.com/cert.pem
    -
    add: olcTLSCertificateKeyFile
    olcTLSCertificateKeyFile: /etc/letsencrypt/live/ldap.my-domain.com/privkey.pem
    -
    add: olcTLSCACertificatePath
    olcTLSCACertificatePath: /usr/share/ca-certificates/trust-source

**SSLv2/v3**

Disable SSLv2/v3 and use strong ciphers. 
    
    ldapmodify -D 'cn=Manager,dc=example,dc=com' -W
    
    dn: cn=config
    add: olcTLSProtocolMin
    olcTLSProtocolMin: 3.3
    -
    add: olcTLSCipherSuite
    olcTLSCipherSuite: DEFAULT:!kRSA:!kDHE
    -

TLSProtocolMin specifies the minimum version in wire format, so "3.3" actually means TLSv1.2. 

The TLSCipherSuite specifies a list of OpenSSL ciphers from which slapd will choose when negotiating TLS connections, in decreasing order of preference. In addition to those specific ciphers, you can use any of the wildcards supported by OpenSSL. **Note:** DEFAULT is a wildcard. See [ciphers(1ssl)](<https://man.archlinux.org/man/ciphers.1ssl>) for description of ciphers, wildcards and options supported. 

**注意：** To see which ciphers are supported by your local OpenSSL installation, type the following: `openssl ciphers -v ALL:COMPLEMENTOFALL`. Always test which ciphers will actually be enabled by TLSCipherSuite by providing it to OpenSSL command, like this: `openssl ciphers -v 'DEFAULT'`.

####  启动基于 SSL 的 slapd

**注意：** This is not needed for StartTLS which listens on the same port as unencrypted LDAP.

You will have to edit the environment file read by `slapd.service` to change the protocol _slapd_ listens on: 
    
    /etc/conf.d/slapd
    
    SLAPD_URLS="ldaps:///"
    SLAPD_OPTIONS=

Localhost connections do not need to use SSL. So, if you want to access the server locally you should change the `SLAPD_URLS` line to: 
    
    SLAPD_URLS="ldap://127.0.0.1 ldaps:///"
    
Then [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `slapd.service`. If it was enabled before, reenable it now. 

**注意：** If you created a self-signed certificate above, be sure to add `TLS_REQCERT allow` to `/etc/openldap/ldap.conf` on the client, or it will not be able connect to the server.

##  下一步

You now have a basic LDAP installation. The next step is to design your directory. The design is heavily dependent on what you are using it for. If you are new to LDAP, consider starting with a directory design recommended by the specific client services that will use the directory ([PAM](<../zh-cn/PAM.html> "PAM"), [Postfix](<../zh-cn/Postfix.html> "Postfix"), etc). 

A directory for system authentication is the [LDAP 认证](<../zh-cn/LDAP_%E8%AE%A4%E8%AF%81.html> "LDAP 认证") article. 

一个较好的web客户端实现是[phpLDAPadmin](</wzh/index.php?title=PhpLDAPadmin&action=edit&redlink=1> "PhpLDAPadmin（页面不存在）"). 

###  备份 LDAP

It is imperative that we have a backup of our LDAP database and configuration in case we ever need to restore for any number of reasons. 

####  导出配置
    
    [ldap]$ slapcat -vF /etc/openldap/slapd.d -n 0 -l "$(hostname)-ldap-mdb-config-$(date '+%F').ldif"
    
####  导出数据库
    
    [ldap]$ slapcat -v -n 1 -l "$(hostname)-ldap-database-$(date '+%F').ldif"
    
###  恢复 LDAP

####  导入配置
    
    [ldap]$ slapadd -v -n 0 -F /etc/openldap/slapd.d -l _< filename from config export>_
    
####  导入数据库
    
    [ldap]$ slapadd -v -n 1 -F /etc/openldap/slapd.d -l _< filename from database export>_
    
##  排错

###  检查 slapd 配置

可以使用该命令检查设置： 
    
    $ slaptest -F /etc/openldap/slapd.d/ -v
    
###  检查客户端认证

If you cannot connect to your server for non-secure authentication: 
    
    $ ldapsearch -x -H ldap://ldaservername:389 -D cn=Manager,dc=example,dc=exampledomain
    
and for TLS secured authentication with: 
    
    $ ldapsearch -x -H ldaps://ldaservername:636 -D cn=Manager,dc=example,dc=exampledomain
    
###  LDAP 服务突然停止

如果你发现 _slapd_ 似乎启动后突然停止了，可以尝试： 
    
    # chown -R ldap:ldap /var/lib/openldap
    
来允许 _slapd_ 以“ldap”用户身份对数据目录进行写入。 

###  LDAP 服务未启动

尝试从命令行启动服务器并启用调试输出： 
    
    # slapd -u ldap -g ldap -h ldaps://ldaservername:636 -d Config,Stats
    
##  参阅

  * [OpenLDAP 官方管理员文档](<https://www.openldap.org/doc/>)
  * [phpLDAPadmin](</wzh/index.php?title=PhpLDAPadmin&action=edit&redlink=1> "PhpLDAPadmin（页面不存在）") \- 类似 phpMyAdmin 的网页管理工具。
  * [LDAP authentication](<../zh-cn/LDAP_authentication.html> "LDAP authentication")
  * 来自 [Arch 用户软件仓库 (AUR)](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93_\(AUR\).html> "Arch 用户软件仓库 \(AUR\)") 的 [apachedirectorystudio](<https://aur.archlinux.org/packages/apachedirectorystudio/>)AUR 是一个基于 Eclipse 的 LDAP 查看器，适用于 OpenLDAP。
