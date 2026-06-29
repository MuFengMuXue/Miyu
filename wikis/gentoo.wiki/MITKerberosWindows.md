[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (Use of [2nd person pronouns](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines#Avoid_first_and_second_person_writing "Gentoo Wiki:Guidelines")). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

Kerberos allows single sign and can assist with Windows and Linux interoperability. The basic goal is to get systems attached to an AD domain to be able to access servers using pass through authentication. For example, start up a browser and point it at an Apache webserver. The web server allows access to the browser user because they have been authenticated in the background via Kerberos.

The setup here is designed to use Samba to manage the Kerberos keytab side of things for servers like Squid, Apache and sshd. As is often the case there are other ways to do it but these notes provide an approach that seems to work with minimal maintenance once set up. Winbind will sort out keytabs for server applications and also for workstation apps like Evolution.

Before you start this you must ensure that the clock on your system agrees with the Windows DC that holds the \"PDC Emulator\" FSMO role. Realistically any of them will do not just that one but that DC is the time source for the whole AD. You must also make sure that DNS is set up correctly. If you can resolve the name of the AD domain, then that is a good start. If either time or DNS go astray then you will get some tricky errors to debug. Always check them both first. You can mitigate DNS via the \[realms\] section in krb5.conf but not time.

## Contents

-   [[1] [Kerberos (MIT)]](#Kerberos_.28MIT.29)
-   [[2] [Samba]](#Samba)
-   [[3] [Apache]](#Apache)
-   [[4] [SSHD]](#SSHD)
-   [[5] [Squid]](#Squid)
-   [[6] [Client apps]](#Client_apps)
    -   [[6.1] [setspn.exe]](#setspn.exe)
    -   [[6.2] [net ads keytab]](#net_ads_keytab)
    -   [[6.3] [ktutil and klist]](#ktutil_and_klist)
    -   [[6.4] [Firefox]](#Firefox)
    -   [[6.5] [Chrome(ium)]](#Chrome.28ium.29)
    -   [[6.6] [IE]](#IE)
    -   [[6.7] [ssh]](#ssh)
    -   [[6.8] [Evolution EWS]](#Evolution_EWS)
    -   [[6.9] [PuTTY]](#PuTTY)
-   [[7] [Full Domain Member on a laptop]](#Full_Domain_Member_on_a_laptop)
    -   [[7.1] [Kerberos]](#Kerberos)
    -   [[7.2] [Samba]](#Samba_2)
    -   [[7.3] [Notes]](#Notes)

## [][Kerberos (MIT)]

On Gentoo enabling the `kerberos` USE flag should pull in [[[app-crypt/mit-krb5]](https://packages.gentoo.org/packages/app-crypt/mit-krb5)[]]. Configuration for a simple setup (set your realm):

[FILE] **`/etc/krb5.conf`Main Kerberos config file**

    [libdefaults]
       default_realm = EXAMPLE.CO.UK
       forwardable = true
       proxiable = true
       default_keytab_name = FILE:/etc/krb5.keytab

You may want to create a realm to domain mapping section \[realms\]. This is especially useful for Apache when the system may have a different external domain to its internal one. See [krb5.conf docs](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html#realms)

Do not create the file [/etc/krb5.keytab] - Samba may give an error if it can\'t create the keytab file.

The following command will grab a Kerberos ticket for the currently logged in user. \<user\> can actually be any valid Kerberized user account, if omitted then the current Unix username is used. If the default realm is already specified in [krb5.conf] then it can be also be omitted.

`user `[`$`]`kinit <user>@EXAMPLE.CO.UK`

If the realm is already set and the ticket is for a username that matches the Unix user then simply run kinit and enter a password.

It is not always possible to use supplementary groups with some daemons eg Squid. The following will add additional ACLs to the Kerberos keytab file file to allow the processes to read the keytab. This assumes that you have ACL support on the system. If not then you will need some other method of allowing the daemons to access the single keytab. Failing that you will have to create separate keytabs for each application and get them set up manually - web search for that. Only do this bit after getting Samba to create the file, otherwise you may get errors.

`root `[`#`]`setfacl -m u:squid:r /etc/krb5.keytab`

`root `[`#`]`setfacl -m u:apache:r /etc/krb5.keytab`

`root `[`#`]`getfacl /etc/krb5.keytab`

    file: etc/krb5.keytab
    owner: root
    group: root
    user::rwx
    user:squid:r--
    user:apache:r--
    group::r--
    mask::r--
    other::---

## [Samba]

Make sure you have a reasonably recent Samba release installed (eg 3.5 or 3.6+)

-   Set Samba to allow access via both secrets (winbind and local passwd) and Kerberos. There are many more options that you might want to configure when joining an AD domain but here we only consider Kerberos related ones.

[FILE] **`/etc/samba/smb.conf`Part of Samba config**

    [global]
       realm = EXAMPLE.CO.UK
       kerberos method = secrets and keytab
       winbind refresh tickets = yes

-   Tell winbind to setup a ticket cache for a logged in user.

[FILE] **`/etc/security/pam_winbind.conf`Part of winbind\'s PAM config**

    [global]
       krb5_auth = yes
       krb5_ccache_type = FILE

-   Join the domain

`root `[`#`]`net ads join -U <admin user>`

-   Start or restart Samba. Make sure that [/etc/conf.d/samba] has winbind included in the list of daemons.

## [Apache]

-   emerge [[[www-apache/mod_auth_kerb]](https://packages.gentoo.org/packages/www-apache/mod_auth_kerb)[]]
-   Add `-D AUTH_KERB` to [/etc/conf.d/apache2]

<!-- -->

-   Edit the module config or add it into your vhost configuration

[FILE] **`/etc/apache2/modules.d/11_mod_auth_kerb.conf`Example Apache Kerberos config**

    <IfDefine AUTH_KERB>
    LoadModule auth_kerb_module modules/mod_auth_kerb.so

    #LogLevel Debug

    <Location "/">
           AuthType Kerberos
           AuthName "Kerberos Login"
           Krb5Keytab /etc/krb5.keytab
           KrbAuthRealms EXAMPLE.CO.UK
           KrbMethodNegotiate On
           KrbMethodK5Passwd Off
           Require valid-user
    </Location>
    </IfDefine>

Set `KrbMethodK5Passwd` on to get prompted for authentication. I suggest you only use this over SSL/TLS (https) for obvious reasons.

-   Use Samba to set the service principle(s) for Apache (HTTP):

`root `[`#`]`net ads keytab add HTTP -U <a_domain_admin>`

`root `[`#`]`net ads keytab add HTTP/<another_SPN>@EXAMPLE.CO.UK -U <a_domain_admin>`

`root `[`#`]`net ads keytab list`

Note the format in the second command. This will get non default Service Principle Names into the keytab, eg for externally facing vhosts. Remember to set the \[realms\] section in [krb5.conf] if you need an external domain to map to an internal realm (or AD domain as MS call them!) The second command also seems to need the SPN added to AD using setspn.exe (on a Windows machine with Domain Admin rights and probably an elevated command prompt on server 2008+):

    c:\>setspn.exe -A HTTP/<another SPN> <computer account>

Test it with this [index.php] in the web server\'s htdocs somewhere (assuming you have PHP installed and configured):

[FILE] **`test.php`Test PHP script**

    <?php
     echo "You have logged in as <b>" . $_SERVER['REMOTE_USER'] . "</b>;";
    ?>

Errors like this in errors_log means that the keytab can\'t be read - check the permissions on it for the apache user:

    gss_acquire_cred() failed: Unspecified GSS failure.  Minor code may provide more information (, Permission denied)

## [SSHD]

Use Samba to get the service principle for SSHD - \"host\". Just to spell it out in case of confusion: use the word host in your command. It is not part of an example, only change the bits between \< and \>.

`root `[`#`]`net ads keytab add host -U <a_domain_admin>`

[FILE] **`/etc/ssh/sshd_conf`Part of sshd\'s configuration file**

    KerberosAuthentication yes
    KerberosOrLocalPasswd yes
    KerberosTicketCleanup yes
    GSSAPIAuthentication yes
    GSSAPICleanupCredentials yes
    UsePAM no

When you turn off PAM you obviously won\'t be able to get it to make a home directory for a new user. So another method will be needed to do this. Winbindd can do this - see the docs for it if you need this.

## [Squid]

Squid also seems to use \"HTTP\" as its service name like Apache. This will probably need a Squid 3.1.x release.

[FILE] **`/etc/squid/squid.conf`Part of the Squid configuration**

    auth_param negotiate program /usr/libexec/squid/squid_kerb_auth -d
    auth_param negotiate children 10
    auth_param negotiate keep_alive on

    acl AUTHENTICATED proxy_auth REQUIRED
    http_access allow AUTHENTICATED
    http_access deny all

[FILE] **`/etc/conf.d/squid`Part of Squid RC config file**

    SQUID_KEYTAB="/etc/krb5.keytab"

## [Client apps]

### [setspn.exe]

Check Service Principle Names:

    c:\>setspn.exe -l <account_name>

### [net ads keytab]

Check a Samba maintained keytab like this:

`root `[`#`]`net ads keytab list`

### [ktutil and klist]

Check keytabs like this:

`root `[`#`]`ktutil`

or

`root `[`#`]`klist -ke /etc/krb5.keytab`

### [Firefox]

-   about:config
-   Type `negotiate` into the filter
-   Set `network.negotiate-auth.trusted-uris` to `example.co.uk`
-   Additional domains (eg short names) can be added separated by commas: e.g. `example.co.uk,host1,host2`.
-   (On Linux only) at a user shell prompt type `kinit` and enter your AD password to authenticate and get a ticket from the KDC (This is not needed if you set up [/etc/security/pam_winbind.conf])

### [][Chrome(ium)]

Start Chrome with: `--auth-server-whitelist="*.example.co.uk" --auth-negotiate-delegate-whitelist="*.example.co.uk"`. You can edit [/usr/share/applications/chrome.desktop] to add this or create another launcher.

Another method using policies:

[Chromium docs, see Setup Policies](https://www.chromium.org/administrators/linux-quick-start%7C) and then apply something like [this](https://akasurde.github.io/krb-auth-chrome.html%7C) For example, with Chrome:

`root `[`#`]`mkdir -p /etc/opt/chrome/policies/managed`

Create a .jason file such as my_local_policy.json:



### [IE]

Does single signon out of the box. IE 7+. Don\'t use \<=6!

### [ssh]

For the SSH client on Linux. This can go in the system wide configuration or in a user specific configuration:

[FILE] **`/etc/ssh/ssh_conf`ssh config snippet**

    host *.example.co.uk
      GSSAPIAuthentication yes

### [Evolution EWS]

You can connect to Exchange via Evolution EWS and provided that autodiscover is set up correctly it will work out of the box. I have found that adding additional SPNs to the client access server\'s machine account can assist with getting Kerberos instead of NTLM working. eg:

     c:\>setspn.exe -S HTTP/exchange.example.co.uk EXCHCAS

To determine what names are needed, switch Evolution to using Kerberos and have Wireshark or tcpdump running and look out for the name that Evolution tries to contact the server with. You should see a flurry of DNS lookups followed by Kerberos related packets. One of the fields will show the host name that your client is trying to use.

If everything is in place (winbind etc) then you simply start Evolution up, add a new account, fill in your name and set the type to ews and then press the lookup button after filling in your email address

### [PuTTY]

-   Get hold of a development snapshot until it is in the core release.
-   Connection -\> Data, select Use system username (your name)
-   Connection -\> SSH -\> Auth -\> GSSAPI, make sure Attempt GSSAPI authentication is selected

## [Full Domain Member on a laptop]

Here\'s a quick rundown for a laptop domain member. I use KDE Plasma 5 as my WM with SDDM for login. I changed the theme to one without a user list. The configs provided are direct copies from my working config, I have only changed domain names to EXAMPLE.

-   Samba4
-   systemd
-   \~amd64
-   AD - 2012R2 forest and domain functionality
-   Exchange 2016 (CU2 at the moment)
-   VPN to the AD DCs
-   Time via ntpd and DNS is setup correctly
-   Autodiscover - internal and external domains are the same and all Exchange names are the same ones
-   HA proxy in use which makes things a bit more interesting
    -   setspn.exe used to add more SPNs to the machine account for the Exchange CAS

### [Kerberos]

    app-crypt/mit-krb5 USE=keyutils pkinit threads -doc -libressl -openldap -selinux -test -xinetd

[FILE] **`/etc/krb5.conf`Main Kerberos config file**

    [libdefaults]
       default_realm = EXAMPLE.CO.UK

### [Samba]

    net-fs/samba USE=acl ads client cups gnutls ldap pam syslog system-mitkrb5 systemd winbind -addc -addns -aio -avahi -cluster -dmapi -fam -iprint -quota -selinux -test

[FILE] **`/etc/samba/smb.conf`Samba config**

    [global]
            workgroup             = EXAMPLE
            realm                 = EXAMPLE.CO.UK
            server string         = My laptop
            security              = ADS
            obey pam restrictions = Yes
            guest account         = nobody

            kerberos method         = secrets and keytab
            winbind refresh tickets = true

            client NTLMv2 auth    = Yes
            client lanman auth    = No
            client plaintext auth = No

            lanman auth  = No
            max protocol = SMB2
            min protocol = NT1

            syslog       = 0
            log level    = 0 winbind:6 auth:7
            log file     = /var/log/samba/%m.log
            max log size = 100
            debug uid    = Yes

            socket options = TCP_NODELAY SO_RCVBUF=8192 SO_SNDBUF=8192

            printcap name = cups
            dns proxy     = No

            idmap config * : backend        = tdb
            idmap config * : range          = 1000000-1999999
            idmap config EXAMPLE : backend = rid
            idmap config EXAMPLE : range   = 10000 - 19999

            template shell             = /bin/bash
            winbind enum users         = Yes
            winbind enum groups        = Yes
            winbind use default domain = Yes
            winbind offline logon      = Yes
            winbind expand groups      = 2

            ea support           = Yes
            store dos attributes = Yes
            dos filemode         = Yes

            unix extensions = no
            follow symlinks = yes
            wide links      = yes

            veto files = /.*/

    [homes]
            comment    = Home Directories
            read only  = No
            browseable = No
            veto files = /.*/

    [shared]
            comment   = Shared Files
            path      = /home/shared
            read only = No

[FILE] **`/etc/security/pam_winbind.conf`Winbind PAM config**

    [global]
    # turn on debugging
    debug = yes

    # turn on extended PAM state debugging
    debug_state = yes

    # request a cached login if possible
    # (needs "winbind offline logon = yes" in smb.conf)
    cached_login = yes

    # authenticate using kerberos
    krb5_auth = yes

    # when using kerberos, request a "FILE" krb5 credential cache type
    # (leave empty to just do krb5 authentication but not have a ticket
    # afterwards)
    krb5_ccache_type = file

    # make successful authentication dependend on membership of one SID
    # (can also take a name)
    ;require_membership_of =

    # password expiry warning period in days
    ;warn_pwd_expire = 14

    # omit pam conversations
    ;silent = no

    # create homedirectory on the fly
    mkhomedir = yes

NIS:

[FILE] **`/etc/nsswitch.conf`NIS nsswitch config snippet**

    passwd:      compat winbind
    shadow:      compat
    group:       compat winbind

Make sure that everything is in place, join the domain and then test the join:

    #net ads info
    #net ads join -U AD_username_with_computer_account_create_rights
    #net ads testjoin

Check NIS is working (should spit out a list of local and then AD users):

    # getent passwd

** Warning**\
Be very careful when setting up PAM, make sure that you have a backout plan and at least one root session already running to the box first, ideally on a console and not via ssh (unless you really know what you are doing)

Setup PAM:

[FILE] **`/etc/pam.d/system-auth`PAM config**

    auth        required      pam_env.so
    auth        sufficient    pam_unix.so likeauth nullok try_first_pass
    auth        sufficient    pam_winbind.so use_first_pass
    auth        required      pam_deny.so

    account     sufficient    pam_winbind.so
    account     required      pam_unix.so

    password    required      pam_cracklib.so retry=3
    password    sufficient    pam_unix.so nullok use_authtok md5 shadow
    password    optional      pam_permit.so

    session     required      pam_mkhomedir.so skel=/etc/skel/ umask=0022
    session     required      pam_limits.so
    session     required      pam_unix.so
    session     required      pam_systemd.so debug

Now login as a domain user via a console and make sure all is well.

### [Notes]

This setup enables you to carry on logging into your system even when the AD DCs etc are unavailable via \"cached credentials\". One failure mode I have discovered so far, is that if you are unable to refresh Kerb tickets from your KDCs then EWS will eventually stop working if Kerberos is your only authentication mechanism (although NTLM is the default).