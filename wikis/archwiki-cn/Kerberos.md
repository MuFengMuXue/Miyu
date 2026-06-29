**翻译状态：**

  * 本文（或部分内容）译自 [Kerberos](<https://wiki.archlinux.org/title/Kerberos> "arch:Kerberos")，最近一次同步于 2021-11-2，若英文版本有所[更改](<https://wiki.archlinux.org/title/Kerberos?diff=0&oldid=710670>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Kerberos_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Active Directory Integration](</wzh/index.php?title=Active_Directory_Integration&action=edit&redlink=1> "Active Directory Integration（页面不存在）")
  * [认证管理](<../zh-cn/%E8%BA%AB%E4%BB%BD%E7%AE%A1%E7%90%86.html> "认证管理")

[Kerberos](<https://en.wikipedia.org/wiki/Kerberos_\(protocol\)> "wikipedia:Kerberos \(protocol\)") 是一个网络认证系统. 见 [krb5 文档](<https://web.mit.edu/kerberos/krb5-latest/doc/>). 

##  安装

在客户端和服务端上[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [krb5](<https://archlinux.org/packages/?name=krb5>)包 软件包. 

**注意：** 强烈建议使用[时钟同步](<../zh-cn/%E7%B3%BB%E7%BB%9F%E6%97%B6%E9%97%B4.html#%E6%97%B6%E9%92%9F%E5%90%8C%E6%AD%A5> "系统时间")守护进程来保持客户端/服务器时钟同步

如果尚未配置主机名解析，则可以手动将客户端和服务器添加到每台计算机的[hosts(5)](<https://man.archlinux.org/man/hosts.5>)文件中。 

**注意：** FQDN（myclient.example.com）必须是hosts文件中IP地址之后的第一个hostname。

##  服务器配置

###  域创建

编辑 `/etc/krb5.conf` 来配置你的域: 
    
    /etc/krb5.conf
    
    [libdefaults]
        default_realm = EXAMPLE.COM
    
    [realms]
        EXAMPLE.COM = {
            admin_server = kerberos.example.com
            # use "kdc = ..." if the kerberos SRV records aren't in DNS (see Advanced section)
            kdc = kerberos.example.com
            # This breaks krb4 compatibility but increases security
            default_principal_flags = +preauth
        }
    
    [domain_realm]
        example.com  = EXAMPLE.COM
        .example.com = EXAMPLE.COM
    
    [logging]
        kdc          = SYSLOG:NOTICE
        admin_server = SYSLOG:NOTICE
        default      = SYSLOG:NOTICE
    
MIT Kerberos中描述了此文件的格式 [documentation](<https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html>)

创建数据库: 
    
    # kdb5_util -r EXAMPLE.COM create -s
    
    Loading random data                                                             
    Initializing database '/var/lib/krb5kdc/principal' for realm 'EXAMPLE.COM',                  
    master key name 'K/M@EXAMPLE.COM'
    You will be prompted for the database Master Password.                          
    It is important that you NOT FORGET this password.                              
    Enter KDC database master key: ***
    Re-enter KDC database master key to verify: ***
    
最后，启用并启动 Kerberos 服务: 
    
    # systemctl enable --now krb5-kdc krb5-kadmind
    
###  添加主体

使用本地身份验证启动Kerberos管理工具 
    
    # kadmin.local
    
    Authenticating as principal root/admin@EXAMPLE.COM with password.
    kadmin.local:

将用户主体添加到Kerberos数据库 : 
    
    kadmin.local: addprinc myuser@EXAMPLE.COM
    
    WARNING: no policy specified for myuser@EXAMPLE.COM; defaulting to no policy
    Enter password for principal "myuser@EXAMPLE.COM": ***
    Re-enter password for principal "myuser@EXAMPLE.COM": ***
    Principal "myuser@EXAMPLE.COM" created.
    
将KDC主体添加到Kerberos数据库: 
    
    kadmin.local: addprinc -randkey host/kerberos.example.com
    
    WARNING: no policy specified for host/kerberos.example.com@EXAMPLE.COM; defaulting to no policy
    Principal "host/kerberos.example.com@EXAMPLE.COM" created.
    
最后，将KDC主体添加到服务器的键表中: 
    
    kadmin.local: ktadd host/kerberos.example.com
    
    Entry for principal host/kerberos.example.com with kvno 2, encryption type aes256-cts-hmac-sha1-96 added to keytab FILE:/etc/krb5.keytab.
    Entry for principal host/kerberos.example.com with kvno 2, encryption type aes128-cts-hmac-sha1-96 added to keytab FILE:/etc/krb5.keytab.
    
退出Kerberos本地验证工具: 
    
    kadmin.local: quit
    
您现在应该能够获得Kerberos凭证了: 
    
    $ kinit
    
    Password for myuser@EXAMPLE.COM: ***
    
    $ klist
    
    Ticket cache: FILE:/tmp/krb5cc_1000
    Default principal: myuser@EXAMPLE.COM
    
    Valid starting       Expires              Service principal
    08/30/2017 14:26:09  08/31/2017 14:26:09  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    
###  防火墙

Add ALLOW rules to your firewall for any applicable ports/protocols: 

  * 88, TCP and UDP for Kerberos v5
  * 749, TCP and UDP for kadmin if you plan to configure it
  * 750, TCP and UDP for Kerberos v4 if you need backwards compatibility

###  DNS记录

**注意：** 如果在每台机器的krb5.conf文件中都指定了kerberos和kadmin服务器，则不需要这样做
    
    db.example.com
    
    kerberos.example.com.           A     1.2.3.4
    _kerberos.example.com.          TXT   "EXAMPLE.COM"
    _kerberos._udp.example.com.     SRV   0 0  88 kerberos.example.com.
    _kerberos-adm._udp.example.com. SRV   0 0 749 kerberos.example.com.
    
**注意：** 不要忘记反向DNS.

##  客户端配置

编辑客户端的 `/etc/krb5.conf` 来适配你服务器的配置. 您可以从服务器复制此文件，或者只设置所需的领域信息. 

###  测试

您现在应该能够在客户端上获得Kerberos凭证: 
    
    $ kinit
    
    Password for myuser@EXAMPLE.COM: ***
    
    $ klist
    
    Ticket cache: FILE:/tmp/krb5cc_1000
    Default principal: myuser@EXAMPLE.COM
    
    Valid starting       Expires              Service principal
    08/30/2017 15:36:10  08/31/2017 15:36:10  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    
##  配置 kadmin

You will need /etc/krb5.conf configured on the kadmin client, and the server's firewall configured for kadmin. 

### Configuring kadmin ACL

Create a principal for administration: 
    
    kadmin.local:  add_principal myuser/admin@EXAMPLE.COM
    
    WARNING: no policy specified for myuser/admin@EXAMPLE.COM; defaulting to no policy
    Enter password for principal "myuser/admin@EXAMPLE.COM": ***
    Re-enter password for principal "myuser/admin@EXAMPLE.COM": ***
    Principal "myuser/admin@EXAMPLE.COM" created.
    
Add the user to the kadmin ACL file: 
    
    /var/lib/krb5kdc/kadm5.acl
    
    myuser/admin@EXAMPLE.COM *

This file's format is described in the MIT Kerberos [documentation](<https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/kadm5_acl.html>)

Configure kdc.conf: 
    
    /var/lib/krb5kdc/kdc.conf
    
    [kdcdefaults]
        kdc_ports = 750,88
    
    [realms]
        EXAMPLE.COM = {
            database_name = /var/lib/krb5kdc/principal
            acl_file = /var/lib/krb5kdc/kadm5.acl
            key_stash_file = /var/lib/krb5kdc/.k5.EXAMPLE.COM
            kdc_ports = 750,88
            max_life = 10h 0m 0s
            max_renewable_life = 7d 0h 0m 0s
        }
    
This file's format is described in the MIT Kerberos [documentation](<https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/kdc_conf.html>)

[Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `krb5-kdc.servce` and `krb5-kadmind`. 

You can now use kadmin as your own user, authenticating with kerberos: 
    
    $ kadmin
    
    Authenticating as principal myuser/admin@EXAMPLE.COM with password.
    Password for myuser/admin@EXAMPLE.COM: ***
    kadmin:
    
## Service principals and keytabs

First, ensure you have configured krb5.conf on all involved machines. 

A kerberos principal has three components, formatted as `primary/instance@REALM`. For user principals, the primary is your username and the instance is omitted or is a role (eg. "admin"): `myuser@EXAMPLE.COM` or `myuser/admin@EXAMPLE.COM`. For hosts, the primary is "host" and the instance is the server FQDN: `host/myserver.example.com@EXAMPLE.COM`. For services, the primary is the service abbreviation and the instance is the FQDN: `nfs/myserver.example.com@EXAMPLE.COM`. The realm can often be omitted, the local computer's default realm is usually assumed. 

### With remote kadmin

This is the easier method, but requires you to have configured [kadmin](<#Configuring_kadmin_ACL>). 

Open kadmin as root (so we can write the keytab) on the client, authenticating with your admin principal: 
    
    client# kadmin -p myuser/admin
    
    Authenticating as principal myuser/admin with password.
    Password for myuser/admin@EXAMPLE.COM:
    kadmin:
    
Add a principal for any services you will be using, eg. "host" for SSH authentication or "nfs" for NFS: 
    
    kadmin: addprinc -randkey host/kbclient.example.com
    
    WARNING: no policy specified for host/kbclient.example.com@EXAMPLE.COM; defaulting to no policy
    Principal "host/kbclient.example.com@EXAMPLE.COM" created.

Save each key to the local keytab: 
    
    kadmin: ktadd host/kbclient.example.com
    
    Entry for principal host/kbclient.example.com with kvno 2, encryption type aes256-cts-hmac-sha1-96 added to keytab FILE:/etc/krb5.keytab.
    Entry for principal host/kbclient.example.com with kvno 2, encryption type aes128-cts-hmac-sha1-96 added to keytab FILE:/etc/krb5.keytab.
    
### Without remote kadmin

Start kadmin on the Kerberos server, using either unix or kerberos authentication: 
    
    # kadmin.local
    
    Authenticating as principal root/admin@EXAMPLE.COM with password.
    kadmin.local:
    
Add a principal for any services you will be using, eg. "host" for SSH authentication or "nfs" for NFS: 
    
    kadmin.local: addprinc -randkey host/kbclient.example.com
    
    WARNING: no policy specified for host/kbclient.example.com@EXAMPLE.COM; defaulting to no policy
    Principal "host/kbclient.example.com@EXAMPLE.COM" created.
    
Save each key to a new keytab to be transferred to the client: 
    
    kadmin.local: ktadd -k kbclient.keytab host/kbclient.example.com
    
    Entry for principal host/kbclient.example.com with kvno 2, encryption type aes256-cts-hmac-sha1-96 added to keytab FILE:/etc/krb5.keytab.
    Entry for principal host/kbclient.example.com with kvno 2, encryption type aes128-cts-hmac-sha1-96 added to keytab FILE:/etc/krb5.keytab.
    
Finally, copy `kbclient.keytab` from the server to the client using SCP or similar, then put it in place with correct permissions: 
    
    # install -b -o root -g root -m 600 kbclient.keytab /etc/krb5.keytab

Finally, delete kbclient.keytab from the server and client. 

## Cross-Realm Trust

Set up a second server as shown above, then create the cross-realm principal on both KDCs. Cross-realm principals must be created with strong passwords, not `-randkey`, and the same password must be used on both KDCs. The principal must have the same key version number (kvno) in both KDCs. 

To grant EXAMPLE.COM principals access to EXAMPLE.ORG resources, you would use the following principal: 
    
    kadmin# addprinc krbtgt/EXAMPLE.ORG@EXAMPLE.COM
    
The `[capaths]` section of `krb5.conf` can be used to further control cross-realm trust relationships. 

## SSH authentication

Use the instructions in [Service principals and keytabs](<#Service_principals_and_keytabs>) to create a principal for the "host" service for both client and server, then put the client's keys in the client's keytab and the server's keys in the server's keytab. 

Modify your [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") server configuration to enable GSSAPI authentication: 
    
    /etc/ssh/sshd_config
    
    # GSSAPI Options
    GSSAPIAuthentication yes
    GSSAPICleanupCredentials yes
    
And modify your client configuration to send GSSAPI requests: 
    
    /etc/ssh/ssh_config
    
    Host *
      GSSAPIAuthentication yes
      GSSAPIDelegateCredentials yes
    
Get a ticket-granting ticket on the client before using ssh: 
    
    $ kinit myuser@EXAMPLE.COM
    
    Password for myuser@EXAMPLE.COM: ***

Pass the -v option to ssh to watch what's happening: 
    
    $ ssh sshserver.example.com -v
    
    debug1: Authentications that can continue: publickey,gssapi-with-mic,password
    debug1: Next authentication method: gssapi-with-mic
    debug1: Delegating credentials
    debug1: Delegating credentials
    debug1: Authentication succeeded (gssapi-with-mic).
    Authenticated to sshserver.example.com ([192.168.100.136]:22).
    debug1: channel 0: new [client-session]
    debug1: Requesting no-more-sessions@openssh.com
    debug1: Entering interactive session.
    debug1: pledge: network
    debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
    Last login: Wed Aug 30 15:52:41 2017 from 192.168.100.1
    
And you should now see a host ticket on the client: 
    
    client$ klist
    
    Ticket cache: FILE:/tmp/krb5cc_1000
    Default principal: myuser@EXAMPLE.COM
    
    Valid starting       Expires              Service principal
    08/30/2017 15:37:40  08/31/2017 15:37:40  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    08/30/2017 15:53:04  08/31/2017 15:37:40  host/sshserver.example.com@EXAMPLE.COM
    
### Authorize other principals

To allow a different kerberos principal to authenticate to a user account, add the principal name to the target account's `.k5login` file. For example, to allow `robert@EXAMPLE.COM` to SSH to alice's account: 
    
    /home/alice/.k5login
    
    robert@EXAMPLE.COM
    
## NFS security

First, configure your [NFS server](<../zh-cn/NFS.html#Server> "NFS") server. Also see [NFS Troubleshooting](</wzh/index.php?title=NFS_Troubleshooting&action=edit&redlink=1> "NFS Troubleshooting（页面不存在）"). Configuring a [时钟同步](<../zh-cn/%E7%B3%BB%E7%BB%9F%E6%97%B6%E9%97%B4.html#%E6%97%B6%E9%92%9F%E5%90%8C%E6%AD%A5> "系统时间") daemon on both the clients and the server is strongly recommended. Clock drift will cause this to break, and the error message will not be helpful. 

Use the instructions in [Service principals and keytabs](<#Service_principals_and_keytabs>) to create a principal for the "nfs" service for both client and server, then put the client's keys in the client's keytab and the server's keys in the server's keytab. 

### NFS server

Add a Kerberos export option. Multiple options can be specified using a colon as a delimiter: 

  * sec=krb5 uses kerberos for authentication only, and transmits the data unauthenticated and unencrypted.
  * sec=krb5i uses kerberos for authentication and integrity checking, but still transmits data unencrypted.
  * sec=krb5p uses kerberos for authentication and encryption.
  * sec=sys does not use kerberos

    /etc/exports
    
    /srv/export *(rw,async,no_subtree_check,no_root_squash,sec=krb5p:krb5)
    
And reload the exports: 
    
    # exportfs -arv
    
### NFS client

Mount the exported directory: 
    
    # mount nfsserver:/srv/export /mnt/
    
You can add -vv for verbose information, and may need -t nfs4 and -o sec=krb5p or your chosen security option. 

Check that it worked with the `mount` command: 
    
    mount | grep krb5
    
    nfsserver:/srv/export on /mnt type nfs4 (rw,relatime,vers=4.1,rsize=131072,wsize=131072,namlen=255,hard,proto=tcp,port=0,timeo=600,retrans=2,sec=krb5,clientaddr=192.168.100.139,local_lock=none,addr=192.168.100.136)
    
## Browsers

Some browsers have support for Kerberos protocol but disable it by default. Here are the instructions how to enable it: 

### Chromium

Chromium needs to be run with a command line parameter that specifies a list of sites where Kerberos authentication is allowed. The easiest way is to add persistent flag to the config file: 
    
    /etc/chromium/policies/managed/test_policy.json
    
    {
      "AuthServerWhitelist": "*.mycompany.com",
      "DisableAuthNegotiateCnameLookup": true
    }
    
### Firefox

To configure Firefox with trusted sites visit `about:config` and set `network.negotiate-auth.trusted-uris` property to FOO.COM (Note: for Firefox there is no "*."; for Chrome, there is). 

## Troubleshooting

### Cannot set GSSAPI authentication names
    
    Cannot set GSSAPI authentication names, aborting
    
Your realm is missing either the `kadmin/admin` or `kadmin/changepw` principal. 

For clients, invalid arguments/options may happen on first setup if rpc-gssd is not loaded. Loading it is usually acomplished by [enabling](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enabling") and [starting](</wzh/index.php?title=Starting&action=edit&redlink=1> "Starting（页面不存在）") `nfs-client.target`, but after first setup this target will need a [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart"). 

### SSH authentication fails while connecting to a server requiring GSSAPI with KeyExchange

If any of the following errors are encountered: 
    
    $ ssh -v -o GSSAPIDelegateCredentials=yes -o GSSAPIAuthentication=yes <user>@<IP address>
    Unable to negotiate with <IP address> port 22: no matching key exchange method found. Their offer: gss-group14-sha1-...
    
    $ ssh -v -o GSSAPIDelegateCredentials=yes -o GSSAPIKeyExchange=yes -o GSSAPIAuthentication=yes <user>@<IP address>
    command-line: line 0: Bad configuration option: gssapikeyexchange
    
it means that package [openssh](<https://archlinux.org/packages/?name=openssh>)包 is not configured with GSSAPI patch for OpenSSH. You can install [openssh-gssapi](<https://aur.archlinux.org/packages/openssh-gssapi/>)AUR or [follow this method](<https://www.pdc.kth.se/support/documents/login/other_linux_login.html>). 

## See also

  * [RHEL7: Configure a Kerberos KDC](<https://www.certdepot.net/rhel7-configure-kerberos-kdc/>)
  * [RHEL7: Configure a system to authenticate using Kerberos](<https://www.certdepot.net/rhel7-configure-system-authenticate-using-kerberos/>)
