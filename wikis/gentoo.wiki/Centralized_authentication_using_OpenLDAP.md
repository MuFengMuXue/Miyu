This page contains [[changes](https://wiki.gentoo.org/index.php?title=Centralized_authentication_using_OpenLDAP&oldid=1292492&diff=1404153)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP/es "Autenticación centralizada mediante OpenLDAP (54% translated)")
-   [français](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP/fr "Authentification centralisée avec OpenLDAP (39% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP/it "Autenticazione centralizzata utilizzando OpenLDAP (4% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP/hu "Központilag történő hitelesítés az OpenLDAP használatával (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP/pl "Centralized authentication using OpenLDAP/pl (5% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP/ru "Централизованная аутентификация с использованием OpenLDAP (51% translated)")
-   [中文](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP/zh "使用OpenLDAP实现集中式认证 (24% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP/zh-cn "使用OpenLDAP集中式认证 (24% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP/ja "OpenLDAP を使用した中央集権型認証 (24% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP/ko "OpenLDAP를 활용한 중앙 인증 (67% translated)")

This guide introduces the basics of LDAP and shows readers how to setup [OpenLDAP](https://wiki.gentoo.org/wiki/OpenLDAP "OpenLDAP") for authentication purposes between a group of computers.

## Contents

-   [[1] [Getting started with OpenLDAP]](#Getting_started_with_OpenLDAP)
    -   [[1.1] [What is LDAP?]](#What_is_LDAP.3F)
    -   [[1.2] [What is a directory?]](#What_is_a_directory.3F)
    -   [[1.3] [How is information structured?]](#How_is_information_structured.3F)
    -   [[1.4] [What can it be used for?]](#What_can_it_be_used_for.3F)
-   [[2] [OpenLDAP server setup]](#OpenLDAP_server_setup)
    -   [[2.1] [Common notes]](#Common_notes)
    -   [[2.2] [Base configuration]](#Base_configuration)
    -   [[2.3] [Schemas]](#Schemas)
        -   [[2.3.1] [RFC 2037 Schema]](#RFC_2037_Schema)
        -   [[2.3.2] [RFC 2037bis Schema]](#RFC_2037bis_Schema)
    -   [[2.4] [UID and GID values, uniqueness, and allocation]](#UID_and_GID_values.2C_uniqueness.2C_and_allocation)
    -   [[2.5] [Password policies]](#Password_policies)
        -   [[2.5.1] [Install module and add the ppolicy overlay]](#Install_module_and_add_the_ppolicy_overlay)
        -   [[2.5.2] [Password Policy Configuration]](#Password_Policy_Configuration)
-   [[3] [Configuring the OpenLDAP client tools]](#Configuring_the_OpenLDAP_client_tools)
    -   [[3.1] [Common configuration]](#Common_configuration)
    -   [[3.2] [Configuring SSSD]](#Configuring_SSSD)
    -   [[3.3] [Configuring nss-pam-ldapd]](#Configuring_nss-pam-ldapd)
-   [[4] [Convert file userbase to LDAP]](#Convert_file_userbase_to_LDAP)
    -   [[4.1] [Creating LDIF files by hand]](#Creating_LDIF_files_by_hand)
    -   [[4.2] [Bulk import]](#Bulk_import)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Emerge errors after conversion to LDAP]](#Emerge_errors_after_conversion_to_LDAP)
-   [[6] [Acknowledgements]](#Acknowledgements)

## [Getting started with OpenLDAP]

### [][What is LDAP?]

LDAP stands for *Lightweight Directory Access Protocol*. Based on X.500 it encompasses most of its primary functions, but lacks the more esoteric functions that X.500 has. Now what is this X.500 and why is there an LDAP?

X.500 is a model for Directory Services in the OSI concept. It contains namespace definitions and the protocols for querying and updating the directory. However, X.500 has been found to be overkill in many situations. Enter LDAP. Like X.500 it provides a data/namespace model for the directory and a protocol. However, LDAP is designed to run directly over the TCP/IP stack. See LDAP as a slimmed-down version of X.500.

### [][What is a directory?]

A directory is a specialized database designed for frequent queries but infrequent updates. Unlike general databases they don\'t contain transaction support or roll-back functionality. Directories are easily replicated to increase availability and reliability. When directories are replicated, temporary inconsistencies are allowed as long as they get synchronized eventually.

### [][How is information structured?]

All information inside a directory is structured hierarchically. Even more, to enter data inside a directory, the directory must know how to store this data inside a tree. Let\'s take a look at a fictional company and an Internet-like tree:

[CODE] **Organisational structure for GenFic, a Fictional Gentoo community**

    dc:         org
                 |
    dc:        genfic         ## (Organisation)
              /      \
    ou:   People   servers    ## (Organisational Units)
          /    \     ..
    uid: ..   John            ## (OU-specific data)

Since data is not fed to the database in this ASCII-art like manner, every node of such a tree must be defined. To name such nodes, LDAP uses a naming scheme. Most LDAP distributions (including OpenLDAP) already contain quite a number of predefined (and general approved) schemas, such as the *inetOrgPerson*, or a frequently used schema to define users which Unix/Linux boxes can use, called *posixAccount*

Interested users are encouraged to read the [OpenLDAP Admin Guide](https://www.openldap.org/doc/admin26/).

### [][What can it be used for?]

LDAP can be used for various things. This document focuses on centralized user management, keeping all user accounts in a single LDAP location (which doesn\'t mean that it\'s housed on a single server, LDAP supports high availability and redundancy), yet other goals can be achieved using LDAP as well.

-   Public Key Infrastructure

<!-- -->

-   Shared Calendar

<!-- -->

-   Shared Addressbook

<!-- -->

-   Storage for DHCP, DNS, \...

<!-- -->

-   System Class Configuration Directives (keeping track of several server configurations)

<!-- -->

-   Centralized Authentication (PosixAccount)

<!-- -->

-   \...

## [OpenLDAP server setup]

### [Common notes]

The domain example.com is an example in this guide. The domain can be renamed as suitable to the readers. However, make sure that the top node is an official top level domain (.net, .com, .cc, .be, etc.). Since LDAP does not provide encryption in transfer it is necessary to create TLS server certificates. It is common practice to relate server DNS, certificate CN and LDAP CN. For this example the server will be reachable by ldap.example.com only over ldaps://. The server certificate will be for exactly this host thus CN=ldap.example.com. For TLS see [Certificates](https://wiki.gentoo.org/wiki/Certificates "Certificates") and [Certificates/Become your own CA](https://wiki.gentoo.org/wiki/Certificates/Become_your_own_CA "Certificates/Become your own CA").

### [Base configuration]

Follow [OpenLDAP Server](https://wiki.gentoo.org/wiki/OpenLDAP_Server "OpenLDAP Server") to setup the server. Use the Quick Start and TLS sections (TLS must be configured or passwords will be sent in the clear!). The directory must allows anonymous binds and access control must allow read access to anonymous users.

** Note**\
It is possible to create DN that gives read access to clients, however, those credentials will need to be installed on every client. Because that credential must be so widely distributed, they\'re not going to be much a secret. The password will be virtually impossible to change without breaking every client. Use firewalls and access control rules to restrict access instead of blocking access all anonymous access. If allowing read to anonymous users is unacceptable, either use client certificates or use Kerberos for authentication instead of LDAP

### [Schemas]

There are 2 different schemas to choose from: **rfc2307** and **rfc2307bis**. They are very similar - the only differ in how group membership is represented. In *rfc2307*, groups contain the users who are members (via the group\'s multi-valued **memberUID** attribute), In, *rfc2307bis* groups contain the full DN of users who are members (via the group\'s multi-valued **member** attribute).

To add a user *uid=bertram,ou=People,dc=example,dc=com* to the *cn=IT_admins,ou=groups,dc=example,dc=com* group in *rfc2307* schema:

[CODE] **Add a user to an RFC2307 group**

    dn: cn=IT_admins,ou=groups,dc=example,dc=com
    changetype: modify
    add: memberUID
    memberUID: bertram

To add a user *uid=bertram,ou=People,dc=example,dc=com* to the *cn=IT_admins,ou=groups,dc=example,dc=com* group in *rfc2307bis* schema:

[CODE] **Add a user to a an RFC2307bis group**

    dn: cn=IT_admins,ou=groups,dc=example,dc=com
    changetype: modify
    add: member
    member: uid=bertram,ou=People,dc=example,dc=com

The *rfc2307* schema is more common, and better supported than the *rfc2307bis* schema, but the latter has support for nested groups and back-references in the user to groups they are members of.

#### [RFC 2037 Schema]

To use the *rfc2307* schema: , add the schemas (and its dependency) to the server:

`root `[`#`]`ldapadd -H ldapi:/// -Y EXTERNAL -f /etc/openldap/schema/cosine.ldif `

`root `[`#`]`ldapadd -H ldapi:/// -Y EXTERNAL -f /etc/openldap/schema/nis.ldif`

#### [RFC 2037bis Schema]

To use the *rfc2307bis* schema , it must first be [converted to an LDIF file](https://wiki.gentoo.org/wiki/OpenLDAP_Server#Convert_a_.schema_file_to_LDIF "OpenLDAP Server"):

[FILE] **`rfc2307.conf`**

    # The first 2 schemas are dependencies
    include /etc/openldap/schema/core.schema
    include /etc/openldap/schema/cosine.schema
    include /etc/openldap/schema/rfc2307bis.schema

`user `[`$`]`mkdir myconfig `

`user `[`$`]`slaptest -f rfc2307.conf -F myconfig `

`user `[`$`]`sed -e '/^#/d' -e '/^dn: /s/$/,cn=schema,cn=config/g' -e 's///g' -e '/^structuralObjectClass/d' -e '/^entryUUID/d' -e '/^creatorsName/d' -e '/^createTimestamp/d' -e '/^entryCSN/d' -e '/^modifiersName/d' -e '/^modifyTimestamp/d' < myconfig/cn\=config/cn\=schema/cn\=\rfc2307bis.ldif > rfc2307bis.ldif`

The *cosine* schema needs to be loaded on the server first otherwise next line will spit out an error: *AttributeType not found: \"manager\"*

`root `[`#`]`ldapadd -H ldapi:/// -Y EXTERNAL -f rfc2307bis.ldif`

`user `[`$`]`rm -fr myconfig`

The back-references (**memberOf**) used by this schema cannot be created manually, the combination of the *dyngroups schema*, the *dynlist module* and the *dynlist overlay* are needed. Note that [[[net-nds/openldap]](https://packages.gentoo.org/packages/net-nds/openldap)[]] need to compiled withe the [[[overlays]](https://packages.gentoo.org/useflags/overlays)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag. It can all be configured in a single LDIF file:

[FILE] **`add-memberOf.ldif`**

    include: file:///etc/openldap/schema/dyngroup.ldif

    dn: cn=module,cn=config
    objectClass: olcModuleList
    cn: module
    olcModulePath: /usr/lib64/openldap/openldap
    olcModuleLoad: dynlist.so

    # This assumes the directory database is number 2. Adjust as needed
    dn: olcOverlay=dynlist,olcDatabase=mdb,cn=config
    changetype: add
    objectClass: olcOverlayConfig
    objectClass: olcDynListConfig
    OlcOverlay: dynlist
    olcDynListAttrSet: groupOfURLs memberURL member+memberOf@groupOfMembers

Add the above to the server:

`root `[`#`]`ldapadd -H ldapi:/// -Y EXTERNAL -f add-memberOf.ldif`

Removing a group will remove all back-references to the group, but removing a user will not remove their membership to the group. The **dynlist** overlay works well with the **refint** overlay, which removes \"dangling\" reference to users in the group when the user is removed. Note, however, if the **refint** module and overlay is installed on a replicating server (producer), it must also be installed on all consumers replicating from it.

### [][UID and GID values, uniqueness, and allocation]

The directory will contain \"global users\". The username and ID numbers used on the server must not conflict. \"System\" users should always be local accounts and never in LDAP. Some space should be allocated for local users. By default, the LDAP server does not enforce uniqueness on usernames, UIDs and GIDs, however its possible to use the *unique* module and overlay to do so.

[FILE] **`unique-add.ldif`**

    dn: cn=module,cn=config
    changetype: add
    objectClass: olcModuleList
    cn: module
    olcModulePath: /usr/lib64/openldap/openldap
    olcModuleLoad: unique.so

    # This assumes the directory database is number 2. Adjust as needed
    dn: olcOverlay=unique,olcDatabase=mdb,cn=config
    changetype: add
    objectClass: olcOverlayConfig
    objectClass: olcUniqueConfig
    olcOverlay: unique

Now create filters for the attributes:

[FILE] **`unique-config.ldif`**

    # TThis assumes the directory database is number 2 ad the overlay is number 2. Adjust as needed
    dn: olcOverlay=unique,olcDatabase=mdb,cn=config
    changetype: modify
    replace: olcUniqueURI
    olcUniqueURI: ldap:///?uidNumber,mail?sub
    olcUniqueURI: ldap:///?gidNumber?sub?objectClass=posixGroup

This ensures no 2 DN the the same subtree have the same uidNumber, gidNumber, or mail attribute.

Keeping track of allocation is difficult. [Here\'s Debian\'s solution](//docs.debops.org/en/latest/ansible/roles/ldap/ldap-posix.html#ldap-ref-next-uid-gid).

Note, the if the **unique** module and overlay is installed on a replicating server (producer), it must also be installed on all consumers replicating from it.

### [Password policies]

** Note**\
[Kerberos](https://wiki.gentoo.org/wiki/Kerberos_Server "Kerberos Server") users should skip this section

LDAP simply stores the password hashes, it does not enforce password policies. The password policy overlay can enforce password policies and requires the [[[overlay]](https://packages.gentoo.org/useflags/overlay)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on [[[net-nds/openldap]](https://packages.gentoo.org/packages/net-nds/openldap)[]].

#### [Install module and add the ppolicy overlay]

First, the module must be added and the overlay added

[FILE] **`ppolicy-add.ldif`Install password policy module and overlay**

    # We need this schema because pwdPolicy is AUXILIARY and STRUCTRAL objectClass is needed
    include: /etc/openldap/schema/namedobject.ldif

    dn: cn=module,cn=config
    objectClass: olcModuleList
    cn: module
    olcModulePath: /usr/lib64/openldap/openldap
    olcModuleLoad: ppolicy.so

    # This assumes the directory database is number 2. Adjust as needed
    dn: olcOverlay=ppolicy,olcDatabase=mdb,cn=config
    objectClass: olcOverlayConfig
    objectClass: olcPPolicyConfig
    olcOverlay: ppolicy
    olcPPolicyDefault: cn=default,ou=ppolicies,dc=example,dc=com
    # Uncomment the next line to disclose "account locked" status on binds failed due to account locking
    #olcPPolicyUseLockout: TRUE
    # Uncomment the next line if this is a read-only replica.
    #olcPPolicyForwardUpdates: TRUE

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f ppolicy-add.ldif`

#### [Password Policy Configuration]

Configuration of this module is discussed in [Password Policies](//www.openldap.org/doc/admin26/guide.html#Password%20Policies) and a detailed explanation of each parameter can be found in [[[slapo-ppolicy(5)]](https://man.archlinux.org/man/slapo-ppolicy.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")].

The password policies are stored in the directory itself, so 2 more DNs have to be created: one for the password policies, and another for the default policy:

[FILE] **`ppolicy-create.ldif`Create password policies container and default password policy**

    dn: ou=ppolicies,dc=example,dc=com
    objectClass: organizationalUnit
    objectClass: top
    ou: ppolicies

    dn: cn=default,ou=ppolicies,dc=example,dc=com
    objectClass: namedPolicy
    objectClass: pwdPolicy
    # This attribute is required even though "userPassword" is the only supported value
    pwdAttribute: userPassword
    cn: default

The password policy comprises functionality of the **shadow**, **pwhistory**, **faillock**, and **pwqdc**/**pwquality** modules, except for password complexity, which requires an external module not in Portage.

Options available are:

-   Minimum and maximum password age
-   Password history
-   Minimum and maximum password length
-   Expiration warning
-   Grace logins (both number of uses and duration based)
-   Whether to enable lockout, consecutive failed bind attempts before lockout and lockout timeout
-   Cooldown time between last consecutive failed bind attempts but before lockout
-   Whether the user is required to change their password after an administrative reset
-   Whether the old password must be sent to do a password changes
-   Minimum and maximum delay (implemented as a temporary lockout) between bind attempts
-   Whether to disable idle accounts (*lastbind* functionality needed - set *olcLastBind* attribute on the database in the config)

Not available, but theoretically supported by the *ppolicy* module:

-   Password complexity

Here\'s an example default policy:

[FILE] **`my-ppolicy.ldif`Example password policy**

    dn: cn=default,ou=ppolicies,dc=example,dc=com
    changetype: modify
    add: pwdMinAge
    # 1 day
    pwdMinAge: 3600
    -
    add: pwdMaxAge
    # 42 days
    pwdMaxAge: 151200
    -
    add: pwdInHistory
    pwdInHistory: 24
    -
    add: pwdMinLength
    pwdMinLength: 7
    -
    add: pwdLockout
    pwdLockout: TRUE
    -
    add: pwdLockoutDuration
    # 20 minutes
    pwdLockoutDuration: 1200
    -
    add: pwdMaxFailure
    pwdMaxFailure: 20
    -
    add: pwdFailureCountInterval
    # 30 minutes
    pwdFailureCountInterval: 3600
    -
    add: pwdMustChange
    pwdMustChange: TRUE
    -
    add: pwdSafeModify
    pwdSafeModify: TRUE

This policy requires a minimum password length of 7 characters, limit password changes to once a day, mandates a password change after 42 days, disallows the use of the last 24 passwords, enabled lockout after 20 attempts for 15 minutes, resets the failed counter after 30 minutes,requires the old password to be sent before changing to a new password, and requires a password change after an administrative password reset.

Password policies can be set for individual accounts. Set the **pwdPolicySubentry** to the DN of the policy. Note the *pwdPolicySubentry* aatribute is an operational attribute and will not be shown by *ldapsearch* unless specifically requested.

To exempt an account (for example, the replicator account) from the default password policy, create an empty password policy and set *pwdPolicySubentry* for the account to it:

[FILE] **`empty-ppolicy-replicator.ldif`Empty password policy for replicator**

    dn: cn=empty,ou=ppolicies,dc=example,dc=com
    changetype: add
    objectClass: namedPolicy
    objectClass: pwdPolicy
    pwdAttribute: userPassword
    cn: empty

    dn: cn=replicator,dc=example,dc=com
    changetype: modify
    add: pwdPolicySubentry
    pwdPolicySubentry: dn: cn=empty,ou=ppolicies,dc=example,dc=com

The *RootDN* ignores all password policies.

## [Configuring the OpenLDAP client tools]

There are numerous methods/tools that can be used for remote authentication. Some distributions also have their own easy to use configuration tool. Below there are some in no particular order. It is possible to combine local users and centrally authorized accounts at the same time. This is important because, for instance, if the LDAP server cannot be accessed one can still login as root.

-   [[[sys-auth/sssd]](https://packages.gentoo.org/packages/sys-auth/sssd)[]] . Its primary function is to provide access to identity and authentication remote resource through a common framework that can provide caching and offline support to the system. It provides PAM and NSS modules, and in the future will support D-Bus interfaces for extended user information. It also provides a better database to store local users as well as extended user data.

<!-- -->

-   [[[sys-auth/nss-pam-ldapd]](https://packages.gentoo.org/packages/sys-auth/nss-pam-ldapd)[]] (Name Service Look up Daemon). Similar to SSSD, but older. Less dependencies and lighter, but not as full featured.

Both will be covered below with the minimum necessary configuration options to get working.

### [Common configuration]

Edit the LDAP Client configuration file. This file is read by ldapsearch and other ldap command line tools.

[FILE] **`/etc/openldap/ldap.conf`Add the following**

    BASE         dc=example,dc=com
    URI          ldap://ldap.example.com:389/ ldap://ldap-1.example.com:389/ ldap://ldap-2.example.com:389/
    TLS_CACERT   /etc/openldap/ca.crt

Test the running server with the following command:

`user `[`$`]`ldapsearch -x -D "cn=Manager,dc=example,dc=com" -W`

If errors are received, try adding `-d 1023` to increase the verbosity and solve the issue.

Before starting any change to the client side authentication configuration, make sure that the LDAP server can be reached and presents the correct information. The following steps assume a user Bert Ram was created in the LDAP with login name bertram. Exchange accordingly with a user from the LDAP instance. Use the manager role with caution. But at least check with the LDAP read user role and a user that will logon to the client(s) to be configured:

`user `[`$`]`ldapsearch -H ldaps://ldap.example.com -b "dc=example,dc=com" -x -W -LLL (uid=bertram)`

    Enter LDAP Password:
    dn: uid=bertram,ou=people,dc=example,dc=com
    objectClass: inetOrgPerson
    objectClass: posixAccount
    objectClass: shadowAccount
    sn: bertram
    cn: bertram
    uid: bertram
    uidNumber: 10002
    gidNumber: 10002
    homeDirectory: /home/bertram
    loginShell: /bin/bash
    gecos: bertram

The above command should show the user\'s entry (sans password). The output will vary depending on the schema used. Test the user\'s password and view the initial groups

`user `[`$`]`ldapsearch -ZZ -H ldap://ldap.example.com -b "dc=example,dc=com" -x -LLL '(|(&(objectClass=posixAccount)(uid=bertram))(&(objectClass=posixGroup)(memberUid=bertram))(&(objectClass=posixGroup)(member=uid=bertram,ou=people,dc=example,dc=com)))'`

    dn: uid=bertram,ou=people,dc=example,dc=com
    objectClass: inetOrgPerson
    objectClass: posixAccount
    objectClass: shadowAccount
    sn: bertram
    cn: bertram
    uid: bertram
    uidNumber: 10002
    gidNumber: 10002
    homeDirectory: /home/bertram
    loginShell: /bin/bash
    gecos: bertram

    dn: cn=IT_admins,ou=groups,dc=example,dc=com
    objectClass: posixGroup
    cn: IT_admins
    gidNumber: 10003
    memberUid: bertram

The above command should show the user\'s entry and any global supplementary groups they are in. The output will vary depending on the schema used.

### [Configuring SSSD]

** Note**\
[Kerberos](https://wiki.gentoo.org/wiki/Kerberos_Server "Kerberos Server") users should follow [Configuring SSSD](https://wiki.gentoo.org/wiki/Kerberos_Server#Configuring_SSSD "Kerberos Server") instead

[[[sys-auth/sssd]](https://packages.gentoo.org/packages/sys-auth/sssd)[]] is the preferred LDAP login solution. It has many features, including the ability to cache credentials, so logins are possible even if the LDAP server is offline, so as long as the user logged in successfully at least once. Note that [[[sys-auth/sssd]](https://packages.gentoo.org/packages/sys-auth/sssd)[]] works with Kerberos, IPA, and Active Directory as well.

First, configure sssd:

[FILE] **`/etc/sssd/sssd.conf`**

    [sssd]
    config_file_version = 2
    services = nss, pam
    domains = example

    [domain/example]
    id_provider = ldap
    auth_provider = ldap
    ldap_uri = ldap://ldap.example.com
    # Uncomment out the next line if using rfc2307bis
    # ldap_schema = rfc2307bis
    # This is the default starting in 2.10.0
    ldap_id_use_start_tls = true
    ldap_search_base = dc=example,dc=com
    # If the server disallows anonymous binds, use client certificates or Kerberos instead
    # For legacy setups, uncomment out the next 2 lines and replace their values appropriately
    # ldap_default_bind_dn = cn=sssd,dc=example,gc=org
    # ldap_default_authtok = secret
    # Allows the user to login even if the LDAP server is down, as long as they've logged in at least once
    cache_credentials = true

Then configure nss by appending **sss** to the *passwd*, *shadow* and *group* lines:

[FILE] **`/etc/nsswitch.conf`**

    passwd:     files sss
    shadow:     files sss
    group:      files sss

Test nss:

`user `[`$`]`getent passwd bertram `

`user `[`$`]`getent shadow bertram `

`user `[`$`]`getent group bertram`

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

### [Configuring nss-pam-ldapd]

** Note**\
[Kerberos](https://wiki.gentoo.org/wiki/Kerberos_Server "Kerberos Server") users should follow [Configuring nss-pam-ldap and pam_krb5](https://wiki.gentoo.org/wiki/Kerberos_Server#Configuring_nss-pam-ldap_and_pam_krb5 "Kerberos Server") instead

Emerge [[[sys-auth/nss-pam-ldapd]](https://packages.gentoo.org/packages/sys-auth/nss-pam-ldapd)[]]

`root `[`#`]`emerge --ask sys-auth/nss-pam-ldapd`

Change [/etc/nslcd.conf]. It should contain

-   URI to contact LDAP server.
-   Base (general) to lookup DNs
-   A statement to use TLS, otherwise password will be sent in the clear
-   Base per group, passwd and/ or shadow in case your LDAP tree deviates from defaults (as mentioned in the file\'s comments)

** Note**\
In Gentoo a user has a primary group with a GID matching the user\'s UID. This is absolutely valid in OpenLDAP, too. In addition a user is also part of other groups, e.g. wheel, audio or usb. OpenLDAP or any other LDAP cannot associate this with the user itself. Instead the user becomes a member of the group in LDAP. The membership relation is then mapped on client side so that additional groups (=initgroups) appear after the authentication happened.

** Warning**\
Make sure that [/etc/nslcd.conf] is owned by nslcd and only readable by nslcd through `chmod 400`.

[FILE] **`/etc/nslcd.conf`(excerpt)**

    uid nslcd
    gid nslcd

    # Uncomment the next line to troubleshoot nslcd
    #log syslog debug

    # Enable TLS or passwords will be sent in the clear
    ssl start_tls
    tls_cacertfile /etc/openldap/ca.crt

    # If the server disallows anonymous binds, use client certificates or Kerberos instead
    # For legacy setups, uncomment out the next 2 lines and replace their values appropriately
    #binddn cn=nslcd,dc=example,dc=com
    #bindpw secret

    # Both rfc2307 and rfc2307bis should work "out of the box" with no maps

Test nss:

`user `[`$`]`getent passwd bertram `

`user `[`$`]`getent shadow bertram `

`user `[`$`]`getent group bertram`

Each command should produce one line of output, unless there\'s a local user with the same user/group name, then there should be 2 lines per command. Enable and start [nslcd]:

OpenRC:

`root `[`#`]`rc-service add nslcd default `

`root `[`#`]`rc-service nslcd start`

Systemd:

`root `[`#`]`systemctl enable --now nslcd`

In [/etc/nsswitch.conf] the *passwd*, *group*, and *shadow* lines need to be appended with **ldap**:

[FILE] **`/etc/nsswitch.conf`(excerpt)**

    passwd:         files ldap
    group:          files ldap
    shadow:         files ldap

Next, configure PAM to allow LDAP authorization. PAM configurations (and the PAM configuration format itself) have gotten significantly more complex, and the advice of inserting *pam_ldap* after *pam_unix* no longer works on it own. The configuration cannot be described simply though adds and deletions, so a sample file modeled after the SSSD configuration will be used.

** Warning**\
As with all PAM modifications, make a backup and have at least one logged in root session, before any changes are made - whether by Portage or the user

[FILE] **`/etc/pam.d/system-auth`**

    auth            required    pam_env.so
    auth            [default=1 ignore=ignore success=ok]    pam_usertype.so isregular
    auth            [default=3 ignore=ignore success=ok]    pam_localuser.so
    auth            requisite       pam_faillock.so preauth
    auth            sufficient      pam_unix.so nullok  try_first_pass
    auth            [default=die]   pam_faillock.so authfail
    # This assumes that global users start at 10000. Replace as neeeded.
    auth            required        pam_ldap.so nullok try_first_pass minimum_uid=10000
    auth            optional        pam_cap.so
    account         required        pam_unix.so
    account         required        pam_faillock.so
    account         sufficient      pam_localuser.so
    account         sufficient      pam_usertype.so issystem
    # This assumes that global users start at 10000. Replace as neeeded.
    account         [default=bad success=ok user_unknown=ignore] pam_ldap.so minimum_uid=10000
    password        required        pam_passwdqc.so config=/etc/security/passwdqc.conf
    password        sufficient      pam_unix.so try_first_pass use_authtok nullok sha512 shadow
    # This assumes that global users start at 10000. Replace as neeeded.
    password        sufficient      pam_ldap.so try_use_authtok nullok minimum_uid=10000
    password        required        pam_deny.so
    session         required        pam_limits.so
    session         required        pam_env.so
    session         required        pam_unix.so
    # This assumes that global users start at 10000. Replace as neeeded.
    session         optional        pam_ldap.so minimum_uid=10000

The configuration does not include automated home directory creation,, so no non-local logins will be allowed until a home directory is created. To enable automated home directory creation, append the following to [/etc/pam.d/system-auth] (please read the warning above!):

[FILE] **`/etc/pam.d/system-auth`(excerpt)**

    session         optional        pam_mkhomedir.so

** Note**\
Automated home directory creation does not work correctly on SELinux systems. In that case, install app-misc/oddjob (in GURU), enable and start the *oddjobd* daemon and replace the above line\'s **pam_mkhomedir.so** with **pam_oddjob_mkhomedir.so**

Test the login from another computer (using SSH), another VT (if local), or in a different root window with *login* and verify it succeeds (if automatic home directory creation is enabled, try it once with the directory created and again with the directory not created).

## [Convert file userbase to LDAP]

On the server, [enable the RootDN by setting the RootPW](https://wiki.gentoo.org/wiki/OpenLDAP_Server#Remote_RootDN_access "OpenLDAP Server")

### [Creating LDIF files by hand]

Here\'s a template for adding user along with their group.

[FILE] **`ldap-usergroup-add.ldif.in`**

    dn: uid=$,ou=people,$
    changetype: add
    objectClass: inetOrgPerson
    objectClass: posixAccount
    objectClass: shadowAccount
    sn: $
    cn: $
    userPassword: x
    loginShell: /bin/bash
    uidNumber: $
    gidNumber: $
    homeDirectory: /home/$

    dn: cn=$,ou=groups,$
    changetype: add
    # Uncomment out the next line if using rfc2307bis
    # objectClass: groupOfMembers
    objectClass: posixGroup
    cn: $
    gidNumber: $
    memberUID: $
    # Delete the above line and uncomment out the next line if using rfc2307bis
    # member: uid=$,ou=people,$

Replace the variables with sed:

`user `[`$`]`sed -e 's/$/bertram/g' -e 's/$/dc=example,dc=com/g' -e 's/$/10000/g' -e 's/$/10000/g' < ldap-usergroup-add.ldif.in > ldap-usergroup-add.ldif`

`root `[`#`]`ldapmodify -H ldap://ldap.example.com -D "cn=Manager,dc=example,dc=com" -W -f ldap-usergroup-add.ldif.in`

Don\'t forget the set the user password with slapasswd:

`root `[`#`]`ldappasswd -H ldap://ldap.example.com -D "cn=Manager,dc=example,dc=com" -W -S uid=bertram,ou=people,dc=example,dc=com`

To add just a group:

[FILE] **`ldapgroup-add.ldif.in`**

    dn: cn=$,ou=groups,$
    changetype: add
    # Uncomment out the next line if using rfc2307bis
    # objectClass: groupOfMembers
    objectClass: posixGroup
    cn: $
    gidNumber: $

Replace the variables with sed:

`user `[`$`]`sed -e 's/$/admin/g' -e 's/$/dc=example,dc=com/g' -e 's/$/20000/g' < ldap-group-add.ldif.in > ldap-group-add.ldif`

`root `[`#`]`ldapmodify -H ldap://ldap.example.com -D "cn=Manager,dc=example,dc=com" -W -f ldap-group-add.ldif`

For test purposes, this is doable, however doing this with more than a dozen or so entries gets tedious, and is unworkable with hundreds or thousands for users.

### [Bulk import]

There were scripts that imported users from the passwd/shadow/database into LDAP, but those scripts have bit-rotted. THere isn\'t a widely distributed program to do this. The files with the import data are easy to parse and likewise it is easy to create LDIF file. The following bash shell script will get the job done:

[CODE] **Script to import non-system users and groups from local credential databases**

    #!/bin/bash

    help()

    declare -i LOCAL_UID_START LOCAL_UID_END LOCAL_GID_START LOCAL_GID_END LDAP_UID_START LDAP_GID_START
    declare LDAP_SCHEMA MY_DOMAIN_DC

    LOCAL_UID_START=$(awk '/^UID_MIN/ ' /etc/login.defs)
    LOCAL_GID_START=$(awk '/^GID_MIN/ ' /etc/login.defs)

    LOCAL_UID_END=$(awk '/^UID_MAX/ ' /etc/login.defs)
    LOCAL_GID_END=$(awk '/^GID_MAX/ ' /etc/login.defs)

    if ! OPTS=$(getopt -o s:u:g:h --long schema:,uid-start:,gid-start:,help -n "$0" -- $@)
    then
        exit 1
    fi

    eval set -- "$"
    while true
    do
        case "$1" in
            -h|--help)
                help
                ;;
            -s|--schema)
                if [ "$" = "RFC2307" ]
                then
                    LDAP_SCHEMA="RFC2307"
                elif [ "$" = "RFC2307BIS" ]
                then
                    LDAP_SCHEMA="RFC2307BIS"
                else
                    help
                fi
                shift 2
                ;;
            -u|--uid-start)
                if [ "$2" -eq "$2" ] && [ "$2" -ge "$" ]
                then
                    LDAP_UID_START=$(( "$2" ))
                else
                    printf "Invalid value for --uid-start\n"
                    help
                fi
                shift 2
                ;;
            -g|--gid-start)
                if [ "$2" -eq "$2" ] && [ "$2" -ge "$" ]
                then
                    LDAP_GID_START=$(( "$2" ))
                else
                    printf "Invalid value for --gid-start\n"
                    help
                fi
                shift 2
                ;;
            --)
                shift
                break
                ;;
        esac
    done

    if [ $# -ne 1 ]
    then
        help
    fi

    MY_DOMAIN_DC="$1"

    LDAP_UID_START="$"
    LDAP_GID_START="$"
    LDAP_SCHEMA="$"

    while read F
    do
        declare LOCAL_UID LOCAL_GID LDAP_USERNAME LDAP_PASSWORD LDAP_GECOS \
            LDAP_HOMEDIR LDAP_LOGIN_SHELL
        LOCAL_UID=$(echo "$" | awk 'BEGIN  ')
        if [ "$" -lt "$" ] || \
        [ "$" -gt "$" ]
        then
            continue
        fi
        LOCAL_GID="$(echo "$" | awk 'BEGIN  ')"
        LDAP_USERNAME="$(echo "$" | awk 'BEGIN  ')"
        LDAP_PASSWORD="$(awk "BEGIN  /^$/ \"\$2 } }" /etc/shadow)"
        LDAP_GECOS="$(echo $ | awk "BEGIN   else \" } }")"
        LDAP_HOMEDIR="$(echo "$" | awk 'BEGIN  ')"
        LDAP_LOGIN_SHELL="$(echo "$" | awk 'BEGIN  ')"

        printf "dn: uid=%s,ou=People,$\n" "$"
        printf "changetype: add\n"
        printf "objectClass: inetOrgPerson\n"
        printf "objectClass: posixAccount\n"
        printf "objectClass: shadowAccount\n"
        printf "sn: %s\n" "$(echo $ | awk '')"
        printf "cn: %s\n" "$"
        printf "uid: %s\n" "$"
        printf "uidNumber: %i\n" "$(( $ + $ - $ ))"
        printf "gidNumber: %i\n" "$(( $ + $ - $ ))"
        printf "homeDirectory: %s\n" "$"
        printf "loginShell: %s\n" "$"
        printf "gecos: %s\n" "$"
        if [ -n "$" ]
        then
            printf "userPassword: %s\n" "$"
        fi
        printf "\n"
    done < /etc/passwd

    while read F
    do
        declare LOCAL_GID LDAP_GROUPAME
        declare -a LDAP_MEMBERSHIP
        LOCAL_GID="$(echo "$" | awk 'BEGIN  ')"
        if [ "$" -lt "$" ] || \
        [ "$" -gt "$" ]
        then
            continue
        fi
        LDAP_GROUPNAME="$(echo $ | awk 'BEGIN  ')"
        read -a LDAP_MEMBERSHIP -d, < <(echo $ | awk 'BEGIN  ')
        printf "dn: cn=%s,ou=groups,$\n" "$"
        printf "changetype: add\n"
        if [ "$" = "RFC2307BIS" ]
        then
            printf "objectClass: groupOfMembers\n"
        fi
        printf "objectClass: posixGroup\n"
        printf "cn: %s\n" "$"
        printf "gidNumber: %i\n" "$(( $ + $ - $ ))"
        if  [ -n "$" ]
        then
            for I in "$"
            do
                MEMBER_GROUP_UID=$(getent passwd "$" | awk 'BEGIN  ')
                if [ "$" -ge "$" ] || \
                [ "$" -le "$" ]
                then
                    if [ "$" = "RFC2307" ]
                    then
                        printf "memberUID: %s\n" "$"
                    else
                        printf "member: uid=%s,ou=people,$\n" "$"
                    fi
                fi
            done
        fi
        printf "\n"
    done < /etc/group

The above script must be run as root to import. it generate a LDIF file that can be imported via *ldapmodify* or *slapmodify*. The schema, UID, and GID stating point are optional an be specified via options. The directory component string (dc=example,dc=com) is a required argument.

## [Troubleshooting]

### [Emerge errors after conversion to LDAP]

If for any reasons local user accounts (i.e. /etc/passwd /etc/shadow) or groups (i.e. /etc/group) are deleted after converting the file userbase to LDAP, errors may be encountered relating to missing user (or group) while emerging certain packages.

Example of error while emerging [[[www-servers/apache]](https://packages.gentoo.org/packages/www-servers/apache)[]] due to missing \"apache\" local user account:

`root `[`#`]`emerge -1 www-servers/apache `

    ...
    Installing build system files
    make[1]: Leaving directory '/var/tmp/portage/www-servers/apache-2.4.59-r1/work/httpd-2.4.59'
    chown: invalid user: ‘apache:apache’
     * ERROR: www-servers/apache-2.4.59-r1::gentoo failed (install phase):
     *   fowners failed

In such cases, re-emerge the local group and user package:

`root `[`#`]`emerge -1 acct-group/apache acct-user/apache`

## [Acknowledgements]

We would like to thank Matt Heler for lending us his box for the purpose of this guide. Thanks also go to the cool guys in [[#ldap](ircs://irc.libera.chat/#ldap)] ([[webchat](https://web.libera.chat/#ldap)]) on the Libera Chat IRC network.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Benjamin Coles, [Sven Vermeulen (SwifT)](https://wiki.gentoo.org/wiki/User:SwifT "User:SwifT") , Brandon Hale, Benny Chuang, jokey, **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*