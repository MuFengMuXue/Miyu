## Contents

-   [[1] [Introduction to Kerberos]](#Introduction_to_Kerberos)
-   [[2] [Installing Kerberos]](#Installing_Kerberos)
-   [[3] [Configuring Kerberos server]](#Configuring_Kerberos_server)
    -   [[3.1] [Creating the database]](#Creating_the_database)
        -   [[3.1.1] [Local backend]](#Local_backend)
        -   [[3.1.2] [LDAP backed]](#LDAP_backed)
    -   [[3.2] [Configuring the defaults]](#Configuring_the_defaults)
    -   [[3.3] [Creating policies (optional)]](#Creating_policies_.28optional.29)
-   [[4] [Populating the database]](#Populating_the_database)
    -   [[4.1] [Creating the initial user principal]](#Creating_the_initial_user_principal)
    -   [[4.2] [Creating service principals]](#Creating_service_principals)
-   [[5] [Configuring the clients]](#Configuring_the_clients)
    -   [[5.1] [Creating /etc/krb5.cfg]](#Creating_.2Fetc.2Fkrb5.cfg)
    -   [[5.2] [Extracting service principal credentials for keytabs]](#Extracting_service_principal_credentials_for_keytabs)
    -   [[5.3] [Configuring SSSD]](#Configuring_SSSD)
    -   [[5.4] [Configuring nss-pam-ldap and pam_krb5]](#Configuring_nss-pam-ldap_and_pam_krb5)
-   [[6] [Security]](#Security)
    -   [[6.1] [Hardening tickets against offline dictionary attacks]](#Hardening_tickets_against_offline_dictionary_attacks)
        -   [[6.1.1] [Using SPAKE preauth]](#Using_SPAKE_preauth)
        -   [[6.1.2] [Flexible authentication secure tunneling (FAST)]](#Flexible_authentication_secure_tunneling_.28FAST.29)
        -   [[6.1.3] [Anonymous PKINIT]](#Anonymous_PKINIT)
    -   [[6.2] [Delegation control]](#Delegation_control)
        -   [[6.2.1] [Disabling forwarding privileged users]](#Disabling_forwarding_privileged_users)
        -   [[6.2.2] [Limiting delegation to certain services]](#Limiting_delegation_to_certain_services)
        -   [[6.2.3] [Constrained delegation]](#Constrained_delegation)
        -   [[6.2.4] [Resource based constrained delegation]](#Resource_based_constrained_delegation)
-   [[7] [Troubleshooting]](#Troubleshooting)
    -   [[7.1] [DNS issues]](#DNS_issues)

## [Introduction to Kerberos]

Kerberos is a protocol developed at MIT for authentication. Clients request a special **ticket**, the **Ticket Granting Ticket (TGT)** from a trusted third party, the **Key Distribution center (KDC)**. Once the client completes authentication with the TGT, it gets a ticket that can be used to authenticate to any server in the realm. Kerberos users and services are both referred to as **principals**

## [Installing Kerberos]

There are 2 Kerberos implementation in Gentoo Linux: MIT [[[app-crypt/mit-krb5]](https://packages.gentoo.org/packages/app-crypt/mit-krb5)[]] and Heimdal [[[app-crypt/heimdal]](https://packages.gentoo.org/packages/app-crypt/heimdal)[]]. Only MIT\'s version will be covered here.

MIT Kerberos has a few USE flags:

### [USE flags for] [app-crypt/mit-krb5](https://packages.gentoo.org/packages/app-crypt/mit-krb5) [[]] [MIT Kerberos V]

  --------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------
  [`+keyutils`](https://packages.gentoo.org/useflags/+keyutils)   Enable for the keyring ccache using keyutils
  [`+pkinit`](https://packages.gentoo.org/useflags/+pkinit)       Enable pkinit support for the initial ticket
  [`doc`](https://packages.gentoo.org/useflags/doc)               Creates and installs the API and implementation documentation. This is only useful if you want to develop software which depends on kerberos
  [`lmdb`](https://packages.gentoo.org/useflags/lmdb)             Add support for using dev-db/lmdb for lookup tables
  [`nls`](https://packages.gentoo.org/useflags/nls)               Add Native Language Support (using gettext - GNU locale utilities)
  [`openldap`](https://packages.gentoo.org/useflags/openldap)     Enable support for ldap as a database backend
  [`selinux`](https://packages.gentoo.org/useflags/selinux)       !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`xinetd`](https://packages.gentoo.org/useflags/xinetd)         Add support for the xinetd super-server
  --------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-09 21:59] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Most of the desired ones are preselected. If the LDAP backend will be in use, set the [[[openldap]](https://packages.gentoo.org/useflags/openldap)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag.

Set any desired use flags in [/etc/portage/package.use/mit-krb5]:

[FILE] **`/etc/portage/package.use/mit-krb5`**

    app-crypt/mit-krb5 openldap

Also enable the [[[kerberos]](https://packages.gentoo.org/useflags/kerberos)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag globally:

[FILE] **`/etc/portage/package.use/00kerberos`**

    */* kerberos

Update the system

`root `[`#`]`emerge --ask --update --verbose --changed-use --deep @world`

[[[app-crypt/mit-krb5]](https://packages.gentoo.org/packages/app-crypt/mit-krb5)[]] should be pulled in. To make sure it doesn\'t accidentally get uninstalled by the \'\--depclean\' option:

`root `[`#`]`emerge --ask --noreplace app-crypt/mit-krb5`

## [Configuring Kerberos server]

** Warning**\
Kerberos needs working name resolution and synchronized clocks. Setup DNS and NTP first.

The first thing required for Kerberos is a realm name. This will be the personal or organization domain name in all upper case (e.g. EXAMPLE.COM).

### [Creating the database]

mit-krb5 has 2 backends: A local database file, and an LDAP one. The former is the default and require no special configuration. The later requires special configuration.

#### [Local backend]

Run krb5_util to create the database

`root `[`#`]`kdb5_util -r EXAMPLE.COM create -s`

#### [LDAP backed]

If an LDAP server hasn\'t been set up yet, follow [OpenLDAP Server](https://wiki.gentoo.org/wiki/OpenLDAP_Server "OpenLDAP Server") to provision one. Make sure TLS is enabled. Set the password for **olcRootPW** (this can be skipped if the slapd and the KDC are on the same host. In that case any examples using the RootDN can be changed by dropping the [-D and -W] flags, replacing [-H ldap://ldap.example.com] with [-H ldapi:///] and adding [-Y EXTERNAL]. Don\'t try to configure Kerberos on the LDAP server yet.

Next, add the Kerberos LDAP schema to the server (If the Kerberos and LDAP servers are different set the [[[openldap]](https://packages.gentoo.org/useflags/openldap)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE on [[[app-crypt/mit-krb5]](https://packages.gentoo.org/packages/app-crypt/mit-krb5)[]] on the LDAP server and emerge it to get the schema). Again, list most packages, the .schema file rather than .ldif file is provided. So it must be [converted first](https://wiki.gentoo.org/wiki/OpenLDAP_Server#Convert_a_.schema_file_to_LDIF "OpenLDAP Server").

[FILE] **`kerberos.conf`**

    include /etc/openldap/schema/kerberos.schema

`user `[`$`]`slaptest -f kerberos.conf -F myconfig `

`user `[`$`]`sed -e '/^#/d' -e '/^dn: /s/$/,cn=schema,cn=config/g' -e 's///g' -e '/^structuralObjectClass/d' -e '/^entryUUID/d' -e '/^creatorsName/d' -e '/^createTimestamp/d' -e '/^entryCSN/d' -e '/^modifiersName/d' -e '/^modifyTimestamp/d' < myconfig/cn\=config/cn\=schema/cn\=\kerberos.ldif > kerberos.ldif`

`root `[`#`]`ldapadd -H ldapi:/// -Y EXTERNAL -f kerberos.ldif`

Create a [/var/lib/krb5kdc/krb5.conf] file (The DN names are not important but must be consistent):

[FILE] **`/var/lib/krb5kdc/krb5.conf`**

    [dbmodules]
            EXAMPLE.COM =

    [dbdefaults]
            ldap_kerberos_container_dn = cn=krbcontainer,dc=example,dc=com
            ldap_kdc_dn = cn=kdc-service,dc=example,dc=com
            ldap_kadmind_dn = cn=adm-service,dc=example,dc=com
            ldap_service_password_file = /var/lib/krb5kdc/service.keyfile
    #       Comment out the line above and uncomment the next 2 lines below if the server is running both slapd and the Kerberos servers:
    #       ldap_kdc_sasl_mech = EXTERNAL
    #       ldap_kadmind_sasl_mech = EXTERNAL

Create an LDIF file with users for KDC And kadmin server themselves (the names of the DNs must match what\'s in the config file)

[FILE] **`provision-kerberos.ldif`**

    dn: cn=kdc-service,dc=example,dc=com
    changetype: add
    objectClass: simpleSecurityObject
    objectClass: organizationalRole
    description: KDC server
    userPassword: x

    dn: cn=adm-service,dc=example,dc=com
    changetype: add
    objectClass: simpleSecurityObject
    objectClass: organizationalRole
    description: KAdmin server
    userPassword: x

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f provision-kerberos.ldif`

Set the passwords for the DNs above (they can be randomly generated using a password generator but the password will be needed in the next step)

`root `[`#`]`ldappasswd -ZZ -D "cn=Manager,dc=example,dc=com" cn=kdc-service,dc=example,dc=com -W -S `

`root `[`#`]`ldappasswd -ZZ -D "cn=Manager,dc=example,dc=com" cn=adm-service,dc=example,dc=com -W -S`

Stash the server passwords set above on the KDC. This file contains obfuscated (but plaintext) passwords, so consider this file sensitive.

`root `[`#`]`kdb5_ldap_util stashsrvpw -f /var/lib/krb5kdc/service.keyfile cn=kdc-service,dc=example,dc=com `

`root `[`#`]`kdb5_ldap_util stashsrvpw -f /var/lib/krb5kdc/service.keyfile cn=adm-service,dc=example,dc=com`

On the LDAP server, adjust access controls so the KDC and kadmin users have write access to the needed parts of the tree:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL`

    # Assumes the directory is database number 2. Adjust as needed.
    dn: olcDatabase=mdb,cn=config
    changetype: modify
    replace: olcAccess
    # Assumes the default rules in the Quick Start. The new rules need to come before any restrictions.
    olcAccess: to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external
     ,cn=auth" manage
    olcAccess: to dn.subtree="cn=EXAMPLE.COM,cn=krbcontainer,dc=example,dc=com"
      by dn.exact="cn=kdc-service,dc=example,dc=com" write
      by dn.exact="cn=adm-service,dc=example,dc=com" write
      by * none
    olcAccess: to dn.subtree="ou=people,dc=example,dc=com"
      by dn.exact="cn=kdc-service,dc=example,dc=com" write
      by dn.exact="cn=adm-service,dc=example,dc=com" write
      by * break
    olcAccess: to attrs=userPassword by self write by anonymous auth by * none
    olcAccess: to * by * read

Also setup an equality index on krbPrincipalName:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL`

    # Assumes the directory is database number 2. Adjust as needed.
    dn: olcDatabase=mdb,cn=config
    changetype: modify
    add: olcDbIndex
    olcDbIndex: krbPrincipalName eq

### [Configuring the defaults]

** Note**\
If the default are changed, only subsequently created tickets get the new values. However, prior principals\' tickets will be constrained by these values if the duration in this file is less that what is in the database

The \"default defaults\" are likely unsuitable. So a site-specific default should be set. Edit [/var/lib/krb5kdc/kdc.conf] and enter the defaults in the [\[realm\]] section. For example:

[FILE] **`/var/lib/krb5kdc/kdc.conf (Excerpt)`**

    [realms]
        EXAMPLE.COM =

This set a default ticket life of 10 hours, renewable for 7 days. See [[[kdc.conf(5)]](https://man.archlinux.org/man/kdc.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] for other [\[realm\]] parameters.

There\'s one problem with renewing a ticket: The ticket maximum renewable lifetime is additionally constrained by the maximum renewable ticket lifetime of the **krbtgt/REALM** ticket. So it must be adjusted too:

`root `[`#`]`kadmin.local -r EXAMPLE.COM modprinc -maxrenewlife 7d krbtgt/EXAMPLE.COM`

Next, define who is allowed admin access by creating [/var/lib/krb5kdc/kadm5.acl]

[FILE] **`/var/lib/krb5kdc/kadm5.acl`**

    */admin@EXAMPLE.COM *

Other things can be put in this file, but the above is the most typical, See [[[kadm5.acl(5)]](https://man.archlinux.org/man/kadm5.acl.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] for the syntax.

### [][Creating policies (optional)]

MIT Kerberos support policies. Policies can:

-   Restrict the lifetime of a ticket (either a minimum or maximum)
-   Minimum number of characters in the password
-   Minimum classes of characters in the password
-   Password history length (local only, not applicable to LDAP backend)
-   Maximum consecutive login attempts and lockout time
-   Cooldown time for consecutive login attempts not resulting in a lockout.
-   Allowed key salts

To create a policy to limit some principals to a10 minute lifetime (useful for service):

`root `[`#`]`kadmin.local -r EXAMPLE.COM add_policy -maxlife 10m service`

To create a policy for password requirements similar to what Windows uses:

`root `[`#`]`kadmin.local -r EXAMPLE.COM add_policy -minlength 8 -minclasses 3 -history 24 windows`

If no policy is specified, and there\'s a policy named \"default\", that is one applied, otherwise policy is applied. To explicitly set \"no policy\" use the -clearpolicy flag then creating or modifying the principal. Any policy of than the default must be explicitly added.

## [Populating the database]

### [Creating the initial user principal]

To create a user principal, **kadmin.local** to perform the addprinc operation. *kadmin.local* must be used on the KDC by the local root.

`root `[`#`]`kadmin.local -r EXAMPLE.COM addprinc +requires_preauth -allow_svr jschmoe`

The user principal *jschmoe* is created. It cannot act as service and requires preauthentication.

An admin principal should be created too, if the user is to have Kerberos admin privileges:

`root `[`#`]`kadmin.local -r EXAMPLE.COM addprinc -maxlife 4h +requires_preauth -allow_svr -allow_renewable jschmoe/admin`

In this example, because the ticket is sensitive, the maxlife is reduced to 4 hours and is non-renewable, in addition to requiring preauthentication and not being allowed to act as a service.

It\'s also possible to attach a policy:

`root `[`#`]`kadmin.local -r EXAMPLE.COM addprinc -policy kadmins +requires_preauth -allow_svr -allow_renewable jschmoe/admin`

(assuming the \"kadmins\" policy already exists).

### [Creating service principals]

Each host will have at least one principal followng this template host/\<fqdn\>@\<REALM\>. Some will have more than one, if the host is running multiple services, like LDAP or web server.

Service principals are create the same way user principals are:

`root `[`#`]`kadmin.local -r EXAMPLE.COM addprinc -randkey -maxlife 10m host/kdc.example.com`

This creates a host ticket for \"kdc.example.com\". Because host password do not need to be memorized by humans, random keys are used. The service ticket time is reduced to 10 minutes. Best practices indicate a service ticket should have a shot lifetime, in case access needs to be revoked, as once a session ticket is obtained from the service it remains good until expired, even if access is revoked.

Other services principals are created similarly:

`root `[`#`]`kadmin.local -r EXAMPLE.COM addprinc -randkey -maxlife 10m host/ldap.example.com `

`root `[`#`]`kadmin.local -r EXAMPLE.COM addprinc -randkey -maxlife 10m ldap/ldap.example.com`

This creates 2 service principals: One for the host, and one for the LDAP service on ldap.example.com.

## [Configuring the clients]

### [][Creating /etc/krb5.cfg]

A [/etc/krb5.cfg] should be created. If SRV records in DNS are setup for clients to discover Kerberos servers, the file is option, but at the very least the realm\'s *admin_server* should be provided, as kadmin clients do not support auto-discovery via DNS.

Example starter [/etc/krb5.cfg] ( see [[[krb5.conf(5)]](https://man.archlinux.org/man/krb5.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] for details ):

[FILE] **`/etc/krb5.conf`**

    [libdefaults]
    # The option tells the client to request a forwardable ticket. Default is not to, even the server permits it
        forwardable = true
        default_realm = EXAMPLE.COM

    [realms]
        EXAMPLE.COM =

    [domain_realm]
        .example.com = EXAMPLE.COM
        example.com = EXAMPLE.COM

Every host will need a copy of this file. If the hosts are homogeneous a copy can be distrubuted to all hosts. Otherwise, hosts that differ will need their own version. One way to distribute is to put whatever variants of the file you need on an internal web server, then download the correct variant from it.

Verify both *kinit* and *kadmin* can connect to their respective servers.

### [Extracting service principal credentials for keytabs]

In Kerberos, each service has its own set of credentials. Service principal credentials are stored in a *keytab* (key table). The default keytab file is [/etc/krb5/keytab]. It should be only be accessible to root. Many service run under their own ID and cannot access it, in that a copy will need to be created that is accessible to that user (and only that user). If the service does not allow specifying a keytab location, the **KRB5_KTNAME** environmental variable will need to be set in that service\'s environment. [[[net-nds/gssproxy]](https://packages.gentoo.org/packages/net-nds/gssproxy)[]] is an alternative, however, the **GSS_USE_PROXY=1** will need to be set in that service\'s environment instead. OpenRC has poor support for [[[net-nds/gssproxy]](https://packages.gentoo.org/packages/net-nds/gssproxy)[]], as it not possible to add arbitrary environmental variables via [/etc/conf.d/*servicename*]. Systemd has better support: just create a directory called [/etc/systemd/system/*servicename*.service.d] and add a .conf file in it with the required **Environment=** lines.

For convenience, the extraction is generally done the host rather than the KDC. Kerberos admin permissions are require to extract credentials and create a keytab.

To extract credentials, use the kadmin command (if the principal has not been created, create it first)

`root `[`#`]`kadmin ktadd host/gentoo-ldap.example.com`

    Authenticating as principal jschmoe/admin@EXAMPLE.COM with password.
    Password for jschmoe/admin@EXAMPLE.COM:
    Entry for principal host/gentoo-ldap.example.com with kvno 3, encryption type aes256-cts-hmac-sha1-96 added to keytab FILE:/etc/krb5.keytab.
    Entry for principal host/gentoo-ldap.example.com with kvno 3, encryption type aes128-cts-hmac-sha1-96 added to keytab FILE:/etc/krb5.keytab.

Note that the ktadd operation randomized the key in the database before extracting it. This is to prevent a rogue admin from impersonating a service without breaking the existing one. kadmin.local users (only on the KDC) can extract credentials without invaliding them by specifying **-norandkey** to *ktadd*

To extract credentials, to another location:

`root `[`#`]`kadmin.local ktadd -k /etc/openldap/krb5-ldap.keytab ldap/ldap.example.com`

    Authenticating as principal jschmoe/admin@EXAMPLE.COM with password.
    Password for jschmoe/admin@EXAMPLE.COM:
    Entry for principal ldap/ldap.example.com with kvno 2, encryption type aes256-cts-hmac-sha1-96 added to keytab WRFILE:/etc/openldap/krb5-ldap.keytab.
    Entry for principal ldap/ldap.example.com with kvno 2, encryption type aes128-cts-hmac-sha1-96 added to keytab WRFILE:/etc/openldap/krb5-ldap.keytab.

The permissions should be already be correct, the ownership will be the user who ran kadmin (usually root), so don\'t forget to change ownership if needed afterwards:

`root `[`#`]`chown ldap: /etc/openldap/krb5-ldap.keytab`

### [Configuring SSSD]

[[[sys-auth/sssd]](https://packages.gentoo.org/packages/sys-auth/sssd)[]] is the recomended solution for LDAP+Kerberos (although it be can used for sites using Kerberos alone). It has many features, including the ability to cache credentials, so logins are possible even if the KDC is offline, so as long as the user logged in successfully at least once.

First, configure sssd: (The following assumes LDAP is used for identity purposes)

[FILE] **`/etc/sssd/sssd.conf`**

    [sssd]
    config_file_version = 2
    services = nss, pam
    domains = example

    [domain/example]
    id_provider = ldap
    auth_provider = krb5
    cache_credentials = true
    ldap_uri = ldap://ldap.example.com
    ldap_search_base = dc=example,dc=com
    ldap_sasl_mech = GSSAPI
    krb5_server = kdc.example.com
    krb5_realm = EXAMPLE.COM
    krb5_lifetime = 10h
    krb5_renewable_lifetime = 7d
    krb5_renew_interval = 5h
    # If host principal based FAST or anonymous PKINIT nased FAST is in use, uncomment out the following line
    # krb5_use_fast = try
    # If host principal based FAST is in use, uncomment out the following line and change "client.example.com" to the hosts FQDN.
    # krb5_fast_principal = host/client.example.com
    # If anonymous PKINIT base FAST is in use, uncomment out the following line
    # krb5_fast_use_anonymous_pkinit true

The values above will vary from the site to site. The parameter **krb5_renew_interval** should be half of **krb5_lifetime**. See [[[sssd-krb5(5)]](https://man.archlinux.org/man/sssd-krb5.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] for details about other parameters. Note that, if FAST is in use, each client will need their own individual copy of this file, whereas one copy can be distributed for anonymous PKINIT users.

Then configure nss by appending **sss** to the *passwd*, *shadow* and *group* lines:

[FILE] **`/etc/nsswitch.conf`**

    passwd:     files sss
    shadow:     files sss
    group:      files sss

Test nss:

`user `[`$`]`getent passwd jschmoe `

`user `[`$`]`getent shadow jschmoe `

`user `[`$`]`getent group jschmoe`

Each command should produce one line of output, unless there\'s a local user with the same user/group name, then there should be 2 lines per command. Enable and start the *sssd* service

OpenRC:

`root `[`#`]`rc-config add sssd default `

`root `[`#`]`rc-service sssd enable`

Systemd:

`root `[`#`]`systemctl enable --now sssd`

Add the following to [/etc/portage/package.use/00sssd]:

[FILE] **`/etc/portage/package.use/00sssd`**

    */* sssd

In particular, [[[sys-auth/pambase]](https://packages.gentoo.org/packages/sys-auth/pambase)[]] has an (experimental!) [[[sssd]](https://packages.gentoo.org/useflags/sssd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag which enables SSSD support. Re-emerge the packages with changed USE flags but **don\'t** run *etc-update* or *dispatch-conf* yet.

`root `[`#`]`emerge -auvDU @world`

** Warning**\
As with all PAM modifications, make a backup and have at least one logged in root session, before any changes are made - whether by Portage or the user

The configuration done should work \"out of the box\". The configuration does not include automated home directory creation,, so no non-local logins will be allowed until a home directory is created. To enable automated home directory creation, append the following to [/etc/pam.d/system-auth] (please read the warning above!):

[FILE] **`/etc/pam.d/system-auth`(excerpt)**

    session         optional        pam_mkhomedir.so

** Note**\
Automated home directory creation does not work correctly on SELinux systems. In that case, install app-misc/oddjob (in GURU), enable and start the *oddjobd* daemon and replace the above line\'s **pam_mkhomedir.so** with **pam_oddjob_mkhomedir.so**

Test the login from another computer (using SSH), another VT (if local), or in a different root window with *login* and verify it succeeds (if automatic home directory creation is enabled, try it once with the directory created and again with the directory not created).

*sssd* supports netgroups, *sudo*, and automounting as well. Add the appropriate lines to [/etc/nsswitch.conf] and [/etc/sssd/sssd.conf]. See [[[sssd.conf(5)]](https://man.archlinux.org/man/sssd.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] for *sssd* general configuration and [[[sssd-sudo(5)]](https://man.archlinux.org/man/sssd-sudo.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] for *sudo* configuration.

*sssd* is a **Kerberos Credentials Manager (KCM)** server. KCM is a smarter, container friendly, and UID namespace aware credential cache. MIT kerberos is a KCM client, so any program built with MIT Kerberos can use the KCM server. It be used with things like Flatpak.

** Note**\
Only **systemd** users can use KCM. The service is socket activated, and, although there is an initscript to launch, it won\'t reliably stay alive. This behavior is intentional: upstream considers non-systemd KCM unsupported. See [SSSD bug #5574](https://github.com/SSSD/sssd/issues/5574), where a potential workaround is discussed.

To setup KCM, insert the following into [/etc/krb5.conf]:

[FILE] **`/etc/krb5.conf`(Excerpt}**

    [libdefaults]
            default_ccache_name = KCM:

### [Configuring nss-pam-ldap and pam_krb5]

** Warning**\
[[[sys-auth/sssd]](https://packages.gentoo.org/packages/sys-auth/sssd)[]] is a better choice all-around. It suppports credential caching, automatic renewal of tickets, FAST and anonymous PKINIT. nss-pam-ldap ad pam_krb5 do not support any of that. Neither have had a release since 2021.

The following assumes LDAP is used for identity purposes. If LDAP is not being used, simply skip past the nslcd part and go straight to the PAM part

First, emerge [[[sys-auth/nss-pam-ldapd]](https://packages.gentoo.org/packages/sys-auth/nss-pam-ldapd)[]] with the [[[kerberos]](https://packages.gentoo.org/useflags/kerberos)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[sasl]](https://packages.gentoo.org/useflags/sasl)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags:

[FILE] **`/etc/portage/package.use/nss-pam-ldapd`**

    sys-auth/nss-pam-ldapd kerberos sasl

`root `[`#`]`emerge --ask sys-auth/nss-pam-ldapd`

Configure nslcd as follows:

[FILE] **`/etc/nslcd.conf`**

    uid nslcd
    gid nslcd

    # Uncomment the next line to troubleshoot nslcd
    #log syslog debug

    krb5_ccname /etc/nslcd.ccache

    sasl_mech gssapi
    sasl_authzid dn:uid=host/client.example.com,cn=gssapi,cn=auth

Set the permissions on the file:

`root `[`#`]`chmod 600 /etc/nslcd.conf `

`root `[`#`]`chown nslcd: /etc/nslcd.conf`

** Warning**\
nslcd doesn\'t use a keytab, it is a Kerberos client rather than a Kerberos server, so it needs a credential cache instead. The host keytab can be used to request a ticket. The problem is the ticket will expire after 10 minutes (assuming best practices are being followed). A new ticket needs to be requested using the host service keytab about every 5 minutes. *nslcd* cannot do this itself, but there is a program that can do it on its behalf: **k5start**, which is part of [[[app-crypt/kstart]](https://packages.gentoo.org/packages/app-crypt/kstart)[]]. It is left as an exercise for the reader for set that up. As stated above, [[[sys-auth/sssd]](https://packages.gentoo.org/packages/sys-auth/sssd)[]] is a better choice.

Test nss:

`user `[`$`]`getent passwd jschmoe `

`user `[`$`]`getent shadow jschmoe `

`user `[`$`]`getent group jschmoe`

Each command should produce one line of output. Enable and start [nslcd]:

OpenRC:

`root `[`#`]`rc-service add nslcd default `

`root `[`#`]`rc-service nslcd start`

Systemd:

`root `[`#`]`systemctl enable --now nslcd`

Next, configure PAM to allow Kerberos authorization. Emerge [[[sys-auth/pambase]](https://packages.gentoo.org/packages/sys-auth/pambase)[]] with the [[[pam+\_krb5]](https://packages.gentoo.org/useflags/pam+_krb5)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag should be sufficent for most setups.

Create [/etc/portage/package.use/pambase] and add the following:

[FILE] **`/etc/portage/package.use/pambase`**

    sys-auth/pambase pam_krb5

then re-emerge the world file

`root `[`#`]`emerge --ask -uvDU @world`

** Warning**\
As with all PAM modifications, make a backup and have at least one logged in root session, before any changes are made - whether by Portage or the user

The configuration done should work \"out of the box\". The configuration does not include automated home directory creation,, so no non-local logins will be allowed until a home directory is created. To enable automated home directory creation, append the following to [/etc/pam.d/system-auth] (please read the warning above!):

[FILE] **`/etc/pam.d/system-auth`(excerpt)**

    session         optional        pam_mkhomedir.so

** Note**\
Automated home directory creation does not work correctly on SELinux systems. In that case, install app-misc/oddjob (in GURU), enable and start the *oddjobd* daemon and replace the above line\'s **pam_mkhomedir.so** with **pam_oddjob_mkhomedir.so**

Test the login from another computer (using SSH), another VT (if local), or in a different root window with *login* and verify it succeeds (if automatic home directory creation is enabled, try it once with the directory created and again with the directory not created).

## [Security]

### [Hardening tickets against offline dictionary attacks]

Kerberos never sends cleartext password over the wire, and requires \"pre-authentication\" before issuing a ticket. Because the ticket is encrypted with a function of the user\'s password, [dictionary attacks](//web.mit.edu/kerberos/krb5-latest/doc/admin/dictionary.html%7Coffline) are possible if a bad actor gets the encrypted ticket. To defend against this a extension was created: Flexible Authentication Secure Tunneling (FAST). An existing ticket is used to \"armor\" the request for the \"real\" ticket. Because the request is encrypted and the key for encrypting principal is random, an offline dictionary attack is not possible.

** Note**\
The server cannot mandate these methods be used to obtain a ticket - it just makes them available. Each client will need be configured to use it

#### [Using SPAKE preauth]

Rather than use an encrypted timestamp based preauthentication, Kerberos can use a password authenticated key agreement implementation called SPAKE.

Minimal configuration is needed on the server for this method. Edit [/var/lib/krb5kdc/kdc.conf] and add the following:

[FILE] **`/var/lib/krb5kdc/kdc.conf`(Excerpt)**

    [libdefaults]
        spake_preauth_groups = edwards25519

This will prevent passive attackers from recovering the ticket, but because the server cannot mandate this, an active attacker can force a Kerberos client to fall back to the old timestamp method.

To prevent clients from falling back, the client can be configure to force the new method:

[FILE] **`/etc/krb5.conf`(Excerpt)**

    [realm]
        disable_encrypted_timestamp = true

Windows clients do not support SPAKE preauthentication.

#### [][Flexible authentication secure tunneling (FAST)]

No configuration on the server is needed for this method. Since all hosts will have a host ticket, and the host ticket has a random key, it can be used by FAST for armoring.

The disadvantage of this method is that all user principals need access to the host principals. Since users should never have access to the host principals, a trusted agent is needed to do the FAST request. On Linux, [[[sys-auth/sssd]](https://packages.gentoo.org/packages/sys-auth/sssd)[]] can do this.

#### [Anonymous PKINIT]

Anonymous PKINIT works differently: TLS is used to obtain a anonymous ticket (having a random session key), The session key in that ticket is used to armor the request. A internal PKI is needed for this method, because the certificate that needs to be created has nonstandard attributes. For PKI information see [Certificates](https://wiki.gentoo.org/wiki/Certificates "Certificates") and [Certificates/Become your own CA](https://wiki.gentoo.org/wiki/Certificates/Become_your_own_CA "Certificates/Become your own CA"). Note, however, easy-rsa cannot create this kind of certificate for us on its own, but it can create the necessary dependencies.

First, on the KDC, create a key:

`user `[`$`]`openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out kdckey.pem`

Then create a CSR:

`user `[`$`]`openssl req -new -out kdc.req -key kdckey.pem`

Copy the CSR to the device with the CA keys.

Create this file on the CA machine:

[FILE] **`kdc.extensions`**

    [kdc_cert]
    basicConstraints=CA:FALSE
    keyUsage=nonRepudiation,digitalSignature,keyEncipherment,keyAgreement
    extendedKeyUsage=1.3.6.1.5.2.3.5
    subjectKeyIdentifier=hash
    authorityKeyIdentifier=keyid,issuer
    issuerAltName=issuer:copy
    subjectAltName=otherName:1.3.6.1.5.2.2;SEQUENCE:kdc_princ_name

    [kdc_princ_name]
    realm=EXP:0,GeneralString:$
    principal_name=EXP:1,SEQUENCE:kdc_principal_seq

    [kdc_principal_seq]
    name_type=EXP:0,INTEGER:1
    name_string=EXP:1,SEQUENCE:kdc_principals

    [kdc_principals]
    princ1=GeneralString:krbtgt
    princ2=GeneralString:$

The CA must sign the request specifying the above file for the needed extensions

`user `[`$`]`env REALM=EXAMPLE.COM openssl x509 -req -in kdc.req -CAkey cakey.pem -CA cacert.pem -out kdc.pem -days 365 -extfile extensions.kdc -extensions kdc_cert -CAcreateserial`

This will produce the file *kdc.pem*, which must be copied to the KDC. Move [kdckey.pem] and [kdc.pem] to [/var/lib/krb5kdc]

Edit [/var/lib/krb5kdc/kdc.conf] and merge the follwing to what is already there:

[FILE] **`/var/lib/krb5kdc/kdc.conf`(Excerpt)**

    [realms]
            EXAMPLE.COM =

Create the anonymous user:

`root `[`#`]`kadmin.local addprinc -randkey WELLKNOWN/ANONYMOUS`

Unlike FAST, this requires a lot more configuration and a PKI. However, clients just need the CA certificate an no private data.

### [Delegation control]

Delegation is a powerful tool within Kerberos, but its also dangerous. Standard Kerberos delegation (forwarding) allow the server to impersonate that user for ANY other service. If a service is compromised, all users who delegated their credential to it are compromised. If a privileged user logs in, the attacker may be able to compromised the entire network

#### [Disabling forwarding privileged users]

Privileged users, like \*/admin principals, can have forwarding disablied on the KDC, by specifying \"-allow_forwarding\" flag to the principal in the KDC. This prevents all forwarding and delegation type (including constrained delegation).

#### [Limiting delegation to certain services]

One way to control delegation is to mark services that are allowed in the KDC by settings the ok_to_delegate on the service principal. However, enforcement must be done on the client, and by default, MIT Kerberos will allow delegation to any service that requests it.

To enforce the ok_to_delegate flag, set the following on each client:

[FILE] **`/etc/krb5.conf`(Excerpt)**

    [libdefaults]
    enforce_ok_as_delegate = true

The Kerberos client will then only delegate to services that request it and have that flag in the KDC.

Windows clients enforce the \"ok_as_delegate\" flag.

#### [Constrained delegation]

The only native backend that supports constrained delegation is the LDAP backend. Constrained delegation is a Microsoft extension, consisting of 2 pieces: Services for users to self (s4u2self), which allows an intermediate service obtain a ticket for itself on behalf of a user, and services for users to proxy (s4u2proxy), which allows the intermediate service to request another service ticket to another service on behalf of user. The KDC controls which intermediate services are allowed to request another service ticket to another service on behalf of user, and limit which \"another service\" can be (this is the \"constrained\" part).

A good example is using Kerberostized NFS with cron. If a user needs to run a cronjob, but need to access an NFS mount in it, they normally won\'t be able to, because the NFS client cannot access the user keycache (it doesn\'t have the password). Constrained delegation can allow the NFS client (like host/nfsclient.example.com) to impersonate the user on the NFS server (like nfs/storage.example.com).

To enable constrained delegation the intermediate (host/nfsclient.example.com) service principal needs to have the \"ok_to_auth_as_delegate\" flag set. The service the intermediate service pricipal will be impersonated on (nfs/storage.example.com) should have the \"ok_as_delegate\" flag set.

The LDAP backend needs entries under the intermediate ((host/nfsclient.example.com) service that contain which service its allowed to delegate to. The procedure is undocumented, and none of the Kerberos tools can set this up, It requires an entry be added directly LDAP, as follows (following the same conventions as the LDAP setup):

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL`

    dn: krbPrincipalName=host/nfsclient.example.com@EXAMPLE.COM,cn=EXAMPLE.COM,cn=krbcontainer,dc=example,dc=com
    changetype: modify
    replace: krbAllowedToDelegateTo
    krbAllowedToDelegateTo: nfs/storage.example.com
    modifying entry "krbPrincipalName=host/nfsclient.example.com@EXAMPLE.COM,cn=EXAMPLE.COM,cn=krbcontainer,dc=example,dc=com"

krbAllowedToDelegateTo is multi-valued attribute and can be added multiple times, once for each service its allowed to delegate to.

If the intermediate service is compromised, the service can impersonate any user in KDC that it can get a forwardable ticket for. Users restricted from obtain forwardable tickets cannot be impersonated.

#### [Resource based constrained delegation]

None of the native Kerberos backends support resource based delegation. This is another Microsoft extension. Its similar to constrained delegation, but turns the authorizations \"upside down\". Instead of Kerberos approving a intermediate service to request another service ticket to another service on behalf of user (like the NFS Client above), the service being delegated to (like the NFS server above) decides which intermediate services it will allow to impersonate a user.

If the intermediate service is compromised, the service can impersonate any user in KDC that it can get a forwardable ticket for. Users restricted from obtain forwardable tickets cannot be impersonated.

This type of delegation is needed in cross-domain trusts.

## [Troubleshooting]

### [DNS issues]

THe kerberos client libraries do both DNS and reverse DNS checks against its hosts. If either is is incorrect, this can cause failures. The best solution is to fix the DNS issue. However, sometimes that\'s not possible. Some organization do not have complete control over their reverse DNS, other times its infeasible.

The client DNS checks can be relaxed by editing [/etc/krb5.conf]

[FILE] **`/etc/krb5.conf`(excerpt)**

    [libdefaults]
    # Disable reverse DNS checks for canonicalizing hostname
            rdns = false
    # Hostname canonicalization is only done if not canonicalizing it results in a "principal not found" error
            dns_canonicalize_hostname = fallback
    # Disables qualification of shortnames
            qualify_shortname = ""

Not all the above options are needed in a given site, but any options added need to be added to all hosts.