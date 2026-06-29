**翻译状态：**

  * 本文（或部分内容）译自 [LDAP_authentication](<https://wiki.archlinux.org/title/LDAP_authentication> "arch:LDAP authentication")，最近一次同步于 2024-05-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/LDAP_authentication?diff=0&oldid=791431>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/LDAP_authentication_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [OpenLDAP](<../zh-cn/OpenLDAP.html> "OpenLDAP")
  * [认证管理](<../zh-cn/%E8%BA%AB%E4%BB%BD%E7%AE%A1%E7%90%86.html> "认证管理")

这是关于如何配置 Arch Linux 安装以针对 LDAP 目录进行身份验证的指南。LDAP 目录服务可以是本地的（安装在同一台计算机上）或网络中的（例如，在需要集中身份验证的实验环境中）。 

本指南分为两部分。第一部分介绍如何安装和配置 [OpenLDAP](<../zh-cn/OpenLDAP.html> "OpenLDAP") 服务端。第二部分是如何在客户端上配置所需的 NSS 和 PAM 模块。如果您只想将 Arch 加入到已存在的 LDAP 服务器进行身份验证，可以跳到第二部分。 

##  服务端配置

###  安装

服务端实现软件如下： 

  * **389 Directory Server** — 这是一个高性能的开源企业级LDAP服务器，用于存储和管理身份认证、用户、群组、组织结构等信息。

     <https://www.port389.org/> || [389-ds-base](<https://archlinux.org/packages/?name=389-ds-base>)包

  * **[OpenLDAP](<../zh-cn/OpenLDAP.html> "OpenLDAP")** — 这是一个开源的轻量级LDAP服务器，用于存储和管理身份验证、用户、组、服务配置等信息。

     <https://www.openldap.org/> || [openldap](<https://archlinux.org/packages/?name=openldap>)包

  * ApacheDS——这是Apache软件基金会下的一个开源项目，提供LADP服务，用于存储、管理和组织分布式信息如用户、群组、权限的呢个，支持高度安全性和可扩展性。  
<https://directory.apache.org/apacheds/>

本文档使用[OpenLDAP](<../zh-cn/OpenLDAP.html> "OpenLDAP")进行演示，请[安装 OpenLDAP 服务器](<../zh-cn/OpenLDAP.html#%E5%AE%89%E8%A3%85> "OpenLDAP")并配置[服务器](<../zh-cn/OpenLDAP.html#%E6%9C%8D%E5%8A%A1%E7%AB%AF> "OpenLDAP")和[客户端](<../zh-cn/OpenLDAP.html#%E5%AE%A2%E6%88%B7%E7%AB%AF> "OpenLDAP")。完成此操作后，请返回此处。 

###  访问控制

为确保LDAP服务中存储的（已加密）密码不被他人轻易读取，但又允许用户可更改自己的某些属性（例如自己的密码或图片等），需要LDAP配置访问控制策略，请创建临时 LDIF 文件 `allowpwchange.ldif`。 

**注意：** 请根据实际情况将 **exmaple** 和 **org** 修改成对应域名。
    
    allowpwchange.ldif
    
    dn: olcDatabase={1}mdb,cn=config
    changetype: modify
    replace: olcAccess
    olcAccess: {0}to attrs=cn,givenName,sn,userPassword,shadowLastChange,mail,loginShell,photo by self write by anonymous auth by dn.base="cn=Manager,dc=_**example**_ ,dc=_**org**_ " write by * none
    olcAccess: {1}to * by self read by dn.base="cn=Manager,dc=_**example**_ ,dc=_**org**_ " write by * read

在数据库编号 0 （cn=config） 上导入它： 
    
    $ slapmodify -n 0 -l allowpwchange.ldif

然后[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新启动") `slapd.service`。 

###  导入基本组织架构

创建临时文件`base.ldif`
    
    base.ldif
    
    # 域
    dn: dc=_**example**_ ,dc=_**org**_
    dc: example
    o: Example Organization
    objectClass: dcObject
    objectClass: organization
    
    # 域管理员账户
    dn: cn=Manager,dc=_**example**_ ,dc=_**org**_
    cn: Manager
    description: LDAP administrator
    objectClass: organizationalRole
    objectClass: top
    roleOccupant: dc=_**example**_ ,dc=_**org**_
    
    # 用户
    dn: ou=People,dc=_**example**_ ,dc=_**org**_
    ou: People
    objectClass: top
    objectClass: organizationalUnit
    
    # 用户组
    dn: ou=Group,dc=_**example**_ ,dc=_**org**_
    ou: Group
    objectClass: top
    objectClass: organizationalUnit

导入到域服务中 
    
    $ ldapadd -D "cn=Manager,dc=example,dc=org" -W -f base.ldif

使用下面命令检测是否导入成功 
    
    $ ldapsearch -x -b 'dc=example,dc=org' '(objectclass=*)'

###  导入用户信息

按照下面模板创建文件`user_joe.ldif`
    
    user_joe.ldif
    
    dn: uid=johndoe,ou=People,dc=_**example**_ ,dc=_**org**_
    objectClass: top
    objectClass: person
    objectClass: organizationalPerson
    objectClass: inetOrgPerson
    objectClass: posixAccount
    objectClass: shadowAccount
    uid: johndoe
    cn: John Doe
    sn: Doe
    givenName: John
    title: Guinea Pig
    telephoneNumber: +0 000 000 0000
    mobile: +0 000 000 0000
    postalAddress: AddressLine1$AddressLine2$AddressLine3
    userPassword: {CRYPT}_**xxxxxxxxxx**_
    labeledURI: <https://archlinux.org/>
    loginShell: /bin/bash
    uidNumber: 9999
    gidNumber: 9999
    homeDirectory: /home/johndoe/
    description: This is an example user

userPassword 条目中的 `xxxxxxxxxx` 应替换为 `/etc/shadow` 中的值或使用 `slappasswd` 命令。使用下面命令导入用户： 
    
    $ ldapadd -D "cn=Manager,dc=example,dc=org" -W -f user_joe.ldif

添加同名的POISX用户组 
    
    group_joe.ldif
    
    dn: cn=joe,ou=Group,dc=_**example**_ ,dc=_**org**_
    objectClass: top
    objectClass: posixGroup
    cn: joe
    gidNumber: 9999

**提示：** 还可以使用 PADL 软件的 [openldap-migrationtools](<https://aur.archlinux.org/packages/openldap-migrationtools/>)AUR 自动将所有本地帐户（和组等）迁移到 LDAP 服务中。 

##  客户端配置

按照 [OpenLDAP](<../zh-cn/OpenLDAP.html> "OpenLDAP") 中所述安装 OpenLDAP 客户端。确保可以使用 ldapsearch 查询服务。 

根据需求，选择[仅在线](<#%E5%9C%A8%E7%BA%BF%E8%AE%A4%E8%AF%81>)身份验证或[在线和离线](<#%E7%94%A8SSSD%E5%AE%8C%E6%88%90%E5%9C%A8%E7%BA%BF%E5%92%8C%E7%A6%BB%E7%BA%BF%E8%AE%A4%E8%AF%81>)身份验证。 

###  在线认证

####  NSS 配置

NSS[[1]](<#cite_note-1>) 是一种系统工具，它以配置数据库的形式管理不同的源。例如:`/etc/passwd` 是 `passwd` 数据库的文件类型源，用于存储用户帐户。 

[安装](<../zh-cn/Pacman.html#%E5%AE%89%E8%A3%85%E6%8C%87%E5%AE%9A%E7%9A%84%E5%8C%85> "Pacman") [nss-pam-ldapd](<https://archlinux.org/packages/?name=nss-pam-ldapd>)包 软件包。 

修改`/etc/nsswitch.conf`，它是 NSS 的主要配置文件。它定义 NSS 哪些源用于哪些系统数据库。我们需要将`ldap`指令添加到`passwd`、`group`和`shadow`数据库中，请将配置文件修改至如下所示： 
    
    /etc/nsswitch.conf
    
    passwd: files **ldap**
    group: files **ldap**
    shadow: files **ldap**

修改`/etc/nslcd.conf`配置文件，并将`base`和`uri`修改为LDAP服务对应的值。 
    
    /etc/nslcd.conf
    
    ...
    uri **ldap://ldap-server.example.org/**
    base **dc=example,dc=org**
    binddn **cn=Manager,dc=example,dc=org**
    bindpw **YourPassword**
    ...

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启")服务`nslcd.service`。 

若配置正确，在客户端上执行命令:`getent passwd`将会列出LDAP服务上面的用户。 

####  PAM 配置

简单的PAM配置原则是将`pam_ldap.so`配置在任何包含`pam_unix.so`的配置文件中。Arch在使用[pambase](<https://archlinux.org/packages/?name=pambase>)包后有效地减少了编辑量，有关于PAM的更多信息，请查阅[RedHat文档](<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/managing_smart_cards/pam_configuration_files>)，如果需要可查看[nss-pam-ldapd](<https://arthurdejong.org/nss-pam-ldapd/>)官方文档。 

**提示：** 若想防止 UID 与系统上的本地用户发生冲突，需要在`pam_ldap.so`行的末尾配置包含`minimum_uid=10000` 或类似值。并必须确保 LDAP 服务可返回与限制匹配的`uidNumber`字段。

**注意：** 每个阶段（auth、session、password、account）都构成一个独立的链，其顺序至关重要。带有sufficient的行有时会“短路”，会跳过该阶段的其余内容，因此对于 _auth_ 、 _password_ 和 _account_ 阶段来说，需要在 _required_ 行之前添加 _sufficient_ 行，而在 _session_ 阶段则是放在required行之后； _optional_ 几乎是放在最后。添加`pam_ldap.so`行时，请不要无故改变其他行的相对顺序！只需将LDAP插入到现有链中即可。

首先修改`/etc/pam.d/system-auth`。此文件包含在`pam.d`的大多数其他文件中，因此在此处的更改可很好地分发配置。当[pambase](<https://archlinux.org/packages/?name=pambase>)包更新时可能会更改此文件。 

在每个阶段的开始位置添加`pam_ldap.so`，并将其配置为sufficient，但 _session_ 阶段需要配置为optional。 
    
    /etc/pam.d/system-auth
    
    **auth      sufficient pam_ldap.so**
    auth      required  pam_unix.so     try_first_pass nullok
    auth      optional  pam_permit.so
    auth      required  pam_env.so
    
    **account   sufficient pam_ldap.so**
    account   required  pam_unix.so
    account   optional  pam_permit.so
    account   required  pam_time.so
    
    **password  sufficient pam_ldap.so**
    password  required  pam_unix.so     try_first_pass nullok sha512 shadow
    password  optional  pam_permit.so
    
    session   required  pam_limits.so
    session   required  pam_unix.so
    **session   optional  pam_ldap.so**
    session   optional  pam_permit.so

然后以相同的方式修改文件`/etc/pam.d/su`和`/etc/pam.d/su-l`，当用户执行命令:`su --login`时，会用到`su-l`文件。 

在每个阶段开始位置添加`pam_ldap.so`,但不要放在`pam_rootok`的前面，并配置为sufficient，而在auth阶段中的`pam_unix.so`模块后面则需要添加`use_first_pass`。 
    
    /etc/pam.d/su
    
    #%PAM-1.0
    auth      sufficient    pam_rootok.so
    **auth      sufficient    pam_ldap.so**
    # 取消对以下行的注释，以默认信任“wheel”组中的用户。
    #auth     sufficient    pam_wheel.so trust use_uid
    # 取消对以下行的注释，以必须要求用户位于“wheel”组中。
    #auth     required      pam_wheel.so use_uid
    auth      required	pam_unix.so **use_first_pass**
    **account   sufficient    pam_ldap.so**
    account   required	pam_unix.so
    **session   sufficient    pam_ldap.so**
    session   required	pam_unix.so

若要使用户能修改自己密码，需要修改文件`/etc/pam.d/passwd`
    
    /etc/pam.d/passwd
    
    #%PAM-1.0
    **password        sufficient      pam_ldap.so**
    password        required        pam_unix.so sha512 shadow nullok

#####  登录时创建主文件夹

若希望在登录时自动创建主文件夹（注：不打算使用[NFS](<../zh-cn/NFS.html> "NFS")存储主文件夹情况下），请修改文件`/etc/pam.d/system-login`并将`pam_mkhomedir.so`添加到任何session阶段的“sufficient”项目上方。若需从 ssh、xdm、sddm、gdm 等或在 tty 登录时会自动创建主文件夹。请以相同的方式修改其他文件，例如当执行命令:`su`和`su --login`时会使用文件`/etc/pam.d/su`和`/etc/pam.d/su-l`。如果不想在 ssh 登录是执行此操作，请修改文件`system-local-login`，而不是文件`system-login`。 
    
    /etc/pam.d/system-login
    
    ...未显示文件头部...
    session    optional   pam_loginuid.so
    session    include    system-auth
    session    optional   pam_motd.so          motd=/etc/motd
    session    optional   pam_mail.so          dir=/var/spool/mail standard quiet
    -session   optional   pam_systemd.so
    session    required   pam_env.so
    **session    required   pam_mkhomedir.so skel=/etc/skel umask=0077**
    
    /etc/pam.d/su-l
    
    ...未显示文件头部...
    **session         required        pam_mkhomedir.so skel=/etc/skel umask=0077**
    session         sufficient      pam_ldap.so
    session         required        pam_unix.so

#####  启用 sudo

要从 LDAP 用户启用 sudo，请编辑 /etc/pam.d/sudo。并相应地修改 sudoers。 
    
    /etc/pam.d/sudo
    
    #%PAM-1.0
    **auth      sufficient    pam_ldap.so**
    auth      required      pam_unix.so  **try_first_pass**
    auth      required      pam_nologin.so

还需要在`/etc/openldap/ldap.conf`中添加以下内容： 
    
    /etc/openldap/ldap.conf
    
    ...
    sudoers_base ou=sudoers,dc=example,dc=org

###  用SSSD完成在线和离线认证

SSSD 是一个系统守护程序。它的主要功能是通过一个通用框架提供对身份和身份验证以及远程资源的访问，该框架可以为系统提供缓存和离线支持。它提供PAM和NSS模块，未来将提供基于D-BUS的接口，用于扩展用户信息。它还提供了一个数据库来存储本地用户以及扩展用户数据。 

**注意：** 必须为 LDAP 服务器配置TLS加密，否则 SSSD 将不起作用。

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sssd](<https://archlinux.org/packages/?name=sssd>)包 包 

####  配置sssd

修改sssd配置文件`/etc/sssd/sssd.conf`，如果文件不存在请自行创建。 
    
    /etc/sssd/sssd.conf
    
    [sssd]
    config_file_version = 2
    services = nss, pam
    domains = LDAP
    
    [domain/LDAP]
    cache_credentials = true
    enumerate = true
    
    id_provider = ldap
    auth_provider = ldap
    
    ldap_uri = ldap://server1.example.org, ldap://server2.example.org
    ldap_search_base = dc=example,dc=org
    ldap_id_use_start_tls = true
    ldap_tls_reqcert = demand
    ldap_tls_cacert = /etc/openldap/certs/cacerts.pem
    chpass_provider = ldap
    ldap_chpass_uri = ldap://server1.example.org
    entry_cache_timeout = 600
    ldap_network_timeout = 2
    
    # 若 OpenLDAP 支持 posixGroup，可取消注释以下两行
    # 获取用户组成员身份支持（需要注释下面冲突配置）
    #ldap_schema = rfc2307
    #ldap_group_member = memberUid
    
    # 其他 LDAP 服务可能支持的组成员身份功能
    ldap_schema = rfc2307bis
    ldap_group_member = uniqueMember

以上只是一个示例。参见[sssd.conf(5)](<https://man.archlinux.org/man/sssd.conf.5>) 了解完整的细节。 

最后将文件权限`chmod 600 /etc/sssd/sssd.conf`，否则 sssd 将无法启动。 

####  配置 NSS

修改`/etc/nsswitch.conf`配置文件如下： 
    
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

####  配置 PAM

首先配置系统认证`/etc/pam.d/system-auth`，所有与系统相关的流程都会经过当前文件,每当用户登录时，使用sssd模块进行认证。 
    
    /etc/pam.d/system-auth
    
    #%PAM-1.0
    
    **auth      sufficient     pam_sss.so forward_pass**
    auth      required         pam_unix.so try_first_pass nullok
    auth      optional         pam_permit.so
    auth      required         pam_env.so
    
    **account   [default=bad success=ok user_unknown=ignore authinfo_unavail=ignore] pam_sss.so**
    account   required         pam_unix.so
    account   optional         pam_permit.so
    account   required         pam_time.so
    
    **password  sufficient     pam_sss.so**
    password  required         pam_unix.so try_first_pass nullok sha512 shadow
    password  optional         pam_permit.so
    
    **session   required       pam_mkhomedir.so skel=/etc/skel/ umask=0077**
    session   required         pam_limits.so
    session   required         pam_unix.so
    session   optional         pam_sss.so
    session   optional         pam_permit.so

**注意：** 如果在用 GNOME/Keyring，当在 PAM 文件的开头添加 'sufficient' 会导致 Gnome Keyring 无法解锁。有关解决方案，请查看高级 PAM 配置。

若向要使用`su`命令时通过sssd进行认证，则请按照下面示例修改文件`/etc/pam.d/su`。 
    
    /etc/pam.d/su
    
    #%PAM-1.0
    auth            sufficient      pam_rootok.so
    **auth           sufficient      pam_sss.so      forward_pass**
    auth            required        pam_unix.so
    **account        [default=bad success=ok user_unknown=ignore authinfo_unavail=ignore] pam_sss.so**
    account         required        pam_unix.so
    session         required        pam_unix.so
    **session        optional        pam_sss.so**

#####  启用 sudo

按照下面示例修改文件`/etc/pam.d/sudo`
    
    /etc/pam.d/sudo
    
    #%PAM-1.0
    **auth**           **sufficient**     **pam_sss.so**
    auth           required        pam_unix.so try_first_pass
    auth           required        pam_nologin.so

配置`/etc/sssd/sssd.conf`文件，添加sudo服务和sudo用户搜索路径。 
    
    /etc/sssd/sssd.conf
    
    [sssd]
    ...
    services = nss, pam, **sudo**
    ...
    
    [domain/LDAP]
    ...
    ldap_sudo_search_base = **ou=sudoers,dc=example,dc=org**
    ...

或者配置 sudo 以允许所需的 LDAP 用户使用 sudo。 

#####  密码管理

若要在使用`su`登录时能修改用户过期密码，请参照下面示例修改文件`/etc/pam.d/su`。 
    
    /etc/pam.d/su
    
    #%PAM-1.0
    ...
    auth        include     system-auth
    account     include     system-auth
    session     include     system-auth
    **password    include    system-auth**

重启`sshd.service`服务。 

若配置正确，使用命令`getent passwd _LDAP用户名_`或`id _LDAP用户名_`能查看到用户信息。 

使用用户登录后，凭据将被缓存，当 ldap 服务器脱机或不可用时，仍然能够使用缓存的凭据进行登录。 

##  参见

  1. [↑](<#cite_ref-1>) Name Service Switch (NSS) 是类Unix系统中用于配置如何查找用户和组信息的服务。它通过 /etc/nsswitch.conf 配置文件定义了系统应如何查询各种类型的信息，例如用户账户、组账户、主机名解析等。 | 博客园:[Linux NSS简介](<https://www.cnblogs.com/panwenbin-logs/p/16050472.html>)
