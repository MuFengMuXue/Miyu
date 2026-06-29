**Resources**

[[]][Home](https://www.openldap.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/OpenLDAP "wikipedia:OpenLDAP")

**OpenLDAP** is a free LDAP server implementation offering an X.500 directory service. The directory service enables user or service lookup, permission management, centralized login, key infrastructure and much more. It includes a suite of LDAP utilities and a standalone LDAP server daemon.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [LDIF Files]](#LDIF_Files)
    -   [[2.2] [Creating slapd.d]](#Creating_slapd.d)
    -   [[2.3] [Running the daemon]](#Running_the_daemon)
        -   [[2.3.1] [OpenRC]](#OpenRC)
        -   [[2.3.2] [Systemd]](#Systemd)
-   [[3] [Management]](#Management)
    -   [[3.1] [Creating the first entry]](#Creating_the_first_entry)
    -   [[3.2] [Modifying the tree]](#Modifying_the_tree)
        -   [[3.2.1] [Change records]](#Change_records)
    -   [[3.3] [Managing Passwords]](#Managing_Passwords)
-   [[4] [Advanced configuration]](#Advanced_configuration)
    -   [[4.1] [TLS]](#TLS)
    -   [[4.2] [Modules]](#Modules)
    -   [[4.3] [Schema]](#Schema)
-   [[5] [Security]](#Security)
    -   [[5.1] [Access Control]](#Access_Control)
    -   [[5.2] [SASL bind]](#SASL_bind)
    -   [[5.3] [Attacks on LDAP servers]](#Attacks_on_LDAP_servers)
-   [[6] [Troubleshooting]](#Troubleshooting)
-   [[7] [See also]](#See_also)
-   [[8] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [net-nds/openldap](https://packages.gentoo.org/packages/net-nds/openldap) [[]] [LDAP suite of application and development tools]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+cleartext`](https://packages.gentoo.org/useflags/+cleartext)         Enable use of cleartext passwords
  [`+syslog`](https://packages.gentoo.org/useflags/+syslog)               Enable support for syslog
  [`argon2`](https://packages.gentoo.org/useflags/argon2)                 Enable password hashing algorithm from app-crypt/argon2
  [`autoca`](https://packages.gentoo.org/useflags/autoca)                 Automatic Certificate Authority overlay
  [`crypt`](https://packages.gentoo.org/useflags/crypt)                   Add support for encryption \-- using mcrypt or gpg where applicable
  [`cxx`](https://packages.gentoo.org/useflags/cxx)                       Build support for C++ (bindings, extra libraries, code generation, \...)
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`experimental`](https://packages.gentoo.org/useflags/experimental)     Enable experimental backend options
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)                 Prefer net-libs/gnutls as SSL/TLS provider (ineffective with USE=-ssl)
  [`iodbc`](https://packages.gentoo.org/useflags/iodbc)                   Add support for iODBC library
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)                     Add support for IP version 6
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)             Add kerberos support
  [`kinit`](https://packages.gentoo.org/useflags/kinit)                   Enable support for kerberos init
  [`minimal`](https://packages.gentoo.org/useflags/minimal)               Build libraries & userspace tools only. Does not install any server code
  [`odbc`](https://packages.gentoo.org/useflags/odbc)                     Enable ODBC and SQL backend options
  [`overlays`](https://packages.gentoo.org/useflags/overlays)             Enable contributed OpenLDAP overlays
  [`pbkdf2`](https://packages.gentoo.org/useflags/pbkdf2)                 Enable support for pbkdf2 passwords
  [`perl`](https://packages.gentoo.org/useflags/perl)                     Add optional support/bindings for the Perl language
  [`samba`](https://packages.gentoo.org/useflags/samba)                   Add support for SAMBA (Windows File and Printer sharing)
  [`sasl`](https://packages.gentoo.org/useflags/sasl)                     Add support for the Simple Authentication and Security Layer
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sha2`](https://packages.gentoo.org/useflags/sha2)                     Enable support for pw-sha2 password hashes
  [`smbkrb5passwd`](https://packages.gentoo.org/useflags/smbkrb5passwd)   Enable overlay for syncing ldap, unix and lanman passwords
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                       Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)       Build static versions of dynamic libraries as well
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`tcpd`](https://packages.gentoo.org/useflags/tcpd)                     Add support for TCP wrappers
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)         Verify upstream signatures on distfiles
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-19 13:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Recommended `USE` flags:

-   any of `argon2`, `pbkdf2`, or `sha2` to provide modern algorithms for secure hashing of passwords.
-   `sasl` to bootstrap configuration through Simple Authentication and Security Layer.
-   `ssl` to encrypt traffic over the network so that passwords stay safe.
-   `syslog` to log events, e.g. failed login attempts.
-   `debug` to enable use of `-d` flag.

\

** Tip**\
The utilities installed by OpenLDAP do not always provide helpful error messages. It is recommended that the `debug` `USE` flag is enabled during the initial setup. Later, it can be disabled and OpenLDAP rebuilt without it, if desired.

`root `[`#`]`emerge --ask net-nds/openldap`

\
In addition to the **S**tandalone **L**D**AP** **D**aemon (`slapd`), OpenLDAP installs two sets of utilities. Those prefixed with `ldap*` (ldapadd, ldapmodify, ldapsearch, \...) and those prefixed with `slap*` (slapadd, slapmodify, slaptest, \...).

-   The `ldap*` commands open a connection to a running ldap server (`slapd` or otherwise) and perform LDAP operations. They will not work if the LDAP server is not running.

<!-- -->

-   The `slap*` commands operate on an OpenLDAP database stored somewhere on the filesystem. **They should not be used to modify a database that is in use by a running instance of `slapd`.** Even though the `slap*` commands may sometimes appear to succeed if they are run on a live database, they can actually interfere with normal `slapd` operation and potentially cause data corruption!

## [Configuration]

Prior to OpenLDAP 2.3, `slapd` and all of the `slap*` utilities were configured from a single file [/etc/openldap/slapd.conf]. Since version 2.3, a new method of configuration was added and the old file was deprecated. The configuration is now stored inside an LDAP directory which (by default) is stored at [/etc/openldap/slapd.d/]. On a fresh install this directory will not yet exist and must be created before `slapd` can be used.

The `ldap*` utilities were and still are configured from a single file [/etc/openldap/ldap.conf]. This file may need to be edited before the `ldap*` utilities can connect to an LDAP server secured with TLS. See the note in the [TLS section](https://wiki.gentoo.org/wiki/OpenLDAP#TLS "OpenLDAP").

** Note**\
As of OpenLDAP version 2.6, the `slapd.conf` file can still be used, but since it is deprecated, its use will not be covered by this wiki page. See `man 5 slapd.conf` for details.

### [LDIF Files]

The configuration directory must be initialized from an **L**DAP **D**ata **I**interchange **F**ormat (LDIF) file. A few files are provided by the package: [/etc/openldap/slapd.ldif] and [/etc/openldap/slapd.default.ldif]. These files will be used as a starting point to configure the daemon.

Because the configuration of `slapd` is itself an LDAP directory, the configuration data is arranged into a **D**irectory **I**nformation **T**ree (**DIT**) just like a \"real\" LDAP directory. The \"path\" of an entry in the tree is called its \"Distinguished Name\" abbreviated `dn`. In a DIT, the paths can branch out similar to the paths of a filesystem except the root of the tree is on the right instead of on the left. For Example, the hypothetical Distinguished Name [uid=Larry,ou=Users,dc=gentoo,dc=org] would correspond to hypothetical filesystem path [/org/gentoo/Users/Larry]. In an LDIF file, entries are defined by a line stating the `dn` followed by lines describing its attributes and their values. Here is an example entry for Larry the cow:

[FILE] **larry.ldif**

    # Entry for Larry the Cow!
    dn: uid=larry25,ou=Users,dc=gentoo,dc=org
    uid: larry25
    cn: Larry the Cow
    givenName: Larry
    sn: Cow
    objectClass: inetOrgPerson
    objectClass: organizationalPerson
    objectClass: person

Each entry in the DIT can contain any number of attribute/value pairs. It can also have the same attribute listed multiple times with different values if the schema allows it. This is known as a multi-valued attribute. The special attribute `objectClass` defines the schema the entry must follow. It is possible for an entry to have more than one `objectClass` but only if they satisfy certain conditions. See section [Schema](https://wiki.gentoo.org/wiki/OpenLDAP#Schema "OpenLDAP").

** Note**\
A single LDIF file can contain several entries. Entries must be separated by at least one blank line. If a blank line were to be inserted in the middle of an entry to improve readability, it may cause a parsing error. Comment lines (lines starting with #) don\'t count, so they can be freely inserted in the middle of an entry, but care should be taken to ensure that two separate entries are not accidentally connected by comment lines.

For more information about LDIF files, see `man 5 ldif`.

### [Creating slapd.d]

In the provided `slapd.ldif`, the config tree is defined with default entries containing default attributes and values. The different entries are as follows:

-   [dn: cn=config] This entry contains global configuration of the daemon
-   [dn: cn=module,cn=config] This entry contains the configuration of the daemon\'s loadable modules
-   [dn: cn=schema,cn=config] This entry is followed by include directives which define the schemas loaded by the daemon
-   [dn: olcDatabase=frontend,cn=config] This entry contains database settings which are applied to all databases served by the daemon
-   [dn: olcDatabase=config,cn=config] This entry represents the config database itself. Settings can be changed here that allow access to the config database so that the daemon\'s configuration can be changed while it is running.
-   [dn: olcDatabase=mdb,cn=config] This entry contains the settings for the primary database served by the daemon. It is possible to define additional entries like this so that the daemon hosts more than one database, but that is beyond the scope of this document.

\
The configuration of the entries is determined by the attributes that begin with \"olc\" e.g. `olcAccess:` The different configuration options and what they mean are described in the `slapd-config(5)` manpage.

Firstly, the `olcPidFile` and `olcArgsFile` attributes need to be changed. This is because the daemon is not run as root on Gentoo (by default). The daemon needs to access the pid and args files after it drops privileges and for that it needs a directory under [/run]. Start by opening `slapd.ldif` in a text editor.

[FILE] **`/etc/openldap/slapd.ldif`(Excerpt)**

    #
    # Change these from their defaults!
    olcArgsFile: /run/openldap/slapd.args
    olcPidFile: /run/openldap/slapd.pid

Next, the [dn: olcDatabase=mdb,cn=config] entry needs to be edited. Change the `olcSuffix` to match the domain that the LDAP server will be accessible at. In theory, the suffix does not need to be a domain name. It is possible to have an organization as a suffix e.g. `olcSuffix: o=Larry Cow Corp`, but that will not be covered here.

[FILE] **`/etc/openldap/slapd.ldif`(Excerpt)**

    dn: olcDatabase=mdb,cn=config
    objectClass: olcDatabaseConfig
    objectClass: olcMdbConfig
    olcDatabase: mdb
    #
    # The max size of the DB is not super important now, but it must be defined
    olcDbMaxSize: 1073741824
    #
    # Edit the Domain Components (dc) to match your domain. e.g. www.example.com -> dc=www,dc=example,dc=com
    olcSuffix: dc=my-domain,dc=com
    #
    # The 'RootDN' is like the root account of your database.
    # Change the Common Name (cn) here to change the name of that account (optional)
    # Change the Domain Components (dc) to match your domain.
    olcRootDN: cn=Manager,dc=my-domain,dc=com
    #
    # The 'RootPW' is the password for the RootDN.
    # By default, the word "secret" is literally the password.
    # This can be changed to a hashed password later on.
    olcRootPW: secret
    #
    # Set this to where you would like to store your database files
    # The database directory MUST exist prior to running slapd AND
    # should only be accessible by the slapd and slap tools.
    # Mode 700 recommended.
    olcDbDirectory: /var/openldap-data

As the comments in the ldif file state, the database directory must be created before proceeding. Changing the mode is also recommended

`root `[`#`]`mkdir /var/openldap-data`

`root `[`#`]`chown ldap:ldap $_`

`root `[`#`]`chmod 0700 $_`

This is the minimum config needed to run the daemon. However, if you would like to take advantage of the feature that allows you to change the daemon configuration at runtime, then the config database must be defined in the LDIF file and made accessible by adding a RootDN and password to it. **The order that the entries appear in this ldif file is important.** The following excerpt, if it is to be used, must be inserted *before* the primary database entry described in the previous excerpt. Normally order does not matter in LDAP data, but this data is special because it is the OpenLDAP config.

[FILE] **`/etc/openldap/slapd.ldif`(Excerpt)**

    #
    # This entry does not exist in the default slapd.ldif.
    # You must create it if you want to access and modify the config during runtime.
    # This is optional, but without it the daemon will have to be shutdown to change config
    dn: olcDatabase=config,cn=config
    objectClass: olcDatabaseConfig
    olcDatabase: config
    #
    # Define the root account of the config database
    olcRootDN: cn=Manager,cn=config
    olcRootPW: secret
    #
    # The olcAccess rules do not apply to the rootDN.
    # This line means that ONLY the rootDN will be allowed to connect to the database.
    olcAccess: to * by * none

Now it is time to initialize the config database on the filesystem. The `slapadd` tool will be used for this purpose. The flag [-F] must point to the desired location of the slapd.d directory. Since it is possible for a `slapd` instance to host more than one database at once, the database that will be edited must be specified using the [-n 0] flag. The databases are given indices starting at -1 and the config database being created in this step is always index 0. The flags [-v] verbose and [-u] dry-run are recommended to ensure there are no errors in the LDIF files before the tool actually writes to the directory. If a partial write occurs because of an error, then all the files in the slapd.d directory will have to be removed before trying again.

`root `[`#`]`slapadd -v -n 0 -F /etc/openldap/slapd.d -l /etc/openldap/slapd.ldif`

The files created by slapadd will have the ownership of the user that invoked it (usually root). This MUST be changed before starting the daemon.

`root `[`#`]`chown -R ldap:ldap /etc/openldap/slapd.d`

** Tip**\
The OpenLDAP utilities are very strict about formatting and schema. If you are receiving a vague error message when trying to parse an LDIF file, try adding the debug flag `-d 1`. This flag is not usable unless OpenLDAP was merged with the `debug` `USE` flag.

### [Running the daemon]

#### [OpenRC]

Before starting the daemon, edit the file [/etc/conf.d/slapd]. Comment and uncomment the lines defining OPTS_CONF so that the daemon is passed the capital [-F] option with the path to the directory instead of the lowercase [-f].

[FILE] **`/etc/conf.d/slapd`(Excerpt)**

    # Comment this line to disable the old slapd.conf file
    #OPTS_CONF="-f /etc/$/slapd.conf"
    # Uncomment this to use the new slapd.d configuration directory
    OPTS_CONF="-F /etc/$/slapd.d"

The daemon can now be started.

`root `[`#`]`rc-service slapd start`

If it launches successfully, it can be added to the default runlevel so that it will start with the system if desired.

`root `[`#`]`rc-update slapd default`

If the daemon does not start because of an error, it can be run manually with the debug flags enabled to diagnose the problem.

`root `[`#`]`/usr/lib64/openldap/slapd -d 1 -h ldap:// -F /etc/openldap/slapd.d/ -u ldap -g ldap `

\

#### [Systemd]

Systemd needs to have a similar configuration change to the one for OpenRC before starting the daemon.

Use systemctl to edit the file [/etc/systemd/system/slapd.service.d/00gentoo.conf] to enable the slapd.d configuration directory that you just created.

`root `[`#`]`systemctl edit slapd.service --drop-in 00gentoo.conf`

Doing this instead of directly editing the file will save you from needing to run systemctl daemon-reload as well as providing syntax checking that will prevent an ill-formed file from being committed.

Uncomment the Environment entry for SLAPD_OPTIONS to enable the slapd configuration directory. Make sure that the entry for [/etc/openldap/slapd.conf] is commented out.

[FILE] **`/etc/systemd/system/slapd.service.d/00gentoo.conf`(Excerpt)**

    [Service]
    # Use the classical configuration file:
    # Environment="SLAPD_OPTIONS=-f /etc/openldap/slapd.conf"
    # Use the slapd configuration directory:
    Environment="SLAPD_OPTIONS=-F /etc/openldap/slapd.d"

    Environment="SLAPD_URLS=ldaps:/// ldap:/// ldapi:///"

The daemon can now be started.

`root `[`#`]`systemctl start slapd.service`

Then you can make sure that it is running without any problems.

`root `[`#`]`systemctl status slapd.service`

If it started up and is working, then you can enable the service so that it will start during normal system startup.

`root `[`#`]`systemctl enable slapd.service`

As with OpenRC, if the daemon does not start because of an error, then it can be run manually with debug flags enabled to diagnose the problem.

`root `[`#`]`/usr/lib64/openldap/slapd -d 1 -h ldap:// -F /etc/openldap/slapd.d/ -u ldap -g ldap `

Note that this action requires the debug flag to be set on [[[net-nds/openldap]](https://packages.gentoo.org/packages/net-nds/openldap)[]].

## [Management]

### [Creating the first entry]

The top-most entry in an LDAP database is called the Root DSE (Not to be confused with the Root DN). This entry is special in the LDAP protocol and its attributes provide information about the server to any clients that connect. The root DSE is not meant to hold any directory data, just metadata. It cannot be changed at the protocol level and should be ignored for most purposes. Immediately below the root DSE is the DIT (or DITs, there can be more than one) which is where the first \"real\" entry lives. All of the entries in the tree are descendants of this first entry. `slapd` does not create this entry by default, and most LDAP tools will be confused if it doesn\'t exist so it should be created now.

First, a new ldif file must be created with a single entry. The `dn` of the entry must match the `olcSuffix` which was set earlier in [/etc/openldap/slapd.ldif]. The attributes of the entry can be set to almost anything according to the needs of the database administrator, but the entry must have a `STRUCTURAL` `objectClass` defined, and it must satisfy the schema of that object class. Schemas and the different types of object classes are discussed later in the [schema section](https://wiki.gentoo.org/wiki/OpenLDAP#Schema "OpenLDAP"). Here is an example first entry that will work:

[FILE] **`first.ldif`Example First Entry**

    # Change the Domain Components (dc) to match your domain from earlier
    dn: dc=example,dc=com
    objectclass: dcObject
    objectclass: organization
    #
    # In this example, Organization (o) is used as the STRUCTURAL objectClass.
    # The value of the o attribute can be anything
    o: Larry the Cow Example Organization
    #
    # This dc must match the first dc in the list above.
    # The rest of the dc's in the list can be omitted
    dc: example

With [first.ldif] saved to the working directory and `slapd` already running, the utility `ldapadd` can be used to create the first entry. It does not need to be run as root. After the [-D] option, the RootDN must be specified. This is the root account name from [slapd.ldif] when the database was created. Running the command will prompt for the password which was also set in [slapd.ldif].

`user `[`$`]`ldapadd -v -D "cn=Manager,dc=example,dc=com" -W -H ldap://localhost -f dse.ldif`

### [Modifying the tree]

At this point, the `slapd` server is running and configured well enough that further changes to the database can be made using a tool like [Apache Directory Studio](https://directory.apache.org/studio/), [[[net-nds/shelldap]](https://packages.gentoo.org/packages/net-nds/shelldap)[]], or [[[net-nds/phpldapadmin]](https://packages.gentoo.org/packages/net-nds/phpldapadmin)[]]. **Using tools like these is highly recommended**, because editing ldif files by hand and parsing them with command line tools is tedious and error-prone. Nevertheless, it may become necessary to use the command line tools from OpenLDAP for one reason or another, so this section will discuss using them.

In general there are two methods of editing an OpenLDAP database:

-   Using the `ldap*` tools to upload an ldif file to a running instance of `slapd`.
-   Shutting down `slapd` and using the `slap*` tools to apply an ldif file directly on the database files.

The latter method has some disadvantages. If the database resides in a secure location (as it should), then the change commands must be run as root. After changes are made, it is important to ensure the permissions of the database files are correct. When `slapadd` and `slapmodify` are run as root, they may change the ownership of the database files to root. After the permissions are corrected, `slaptest` can be used to check the database.

Both methods require the creation of LDIF-formatted text. It can be generated and piped to the commands, or saved to a file that is passed as a command argument.

#### [Change records]

Adding a new entry is simple and requires exactly the same process as adding the [first entry](https://wiki.gentoo.org/wiki/OpenLDAP#Creating_the_first_entry "OpenLDAP"). Editing an *existing* entry requires creating an LDIF Change Record. Change records are almost exactly the same as the LDIF records used previously, but they have a few additional special attributes.

[FILE] **`change.ldif`Example Change Record**

    # DN of the entry to be changed
    dn: uid=larry,dc=example,dc=com
    #
    # What type of change is happening: (modify)
    changeType: modify
    #
    # Which attribute(s) are being modified: (givenName)
    replace: givenName
    #
    # New definitiion(s) of the specified attribute
    givenName: Lawrence

The valid `changeType`\'s and their behavior are described further in the `LDIF(5)` manpage. The change can be applied with `ldapmodify` or `slapmodify`.

`user `[`$`]`ldapmodify -v -D "cn=Manager,dc=example,dc=com" -W -H ldap://localhost -f change.ldif`

OR

`root `[`#`]`<service manager> stop slapd`

`root `[`#`]`slapmodify -v -n 1 -l change.ldif `

`root `[`#`]`chown -R ldap:ldap /var/openldap-data`

`root `[`#`]`slaptest`

`root `[`#`]`<service manager> start slapd`

### [Managing Passwords]

In LDAP, the act of authentication is known as binding. Almost any entry in the tree can be bound to, not just users. Typically, all an entry needs to be bound is an attribute called `userPassword` which stores the password used during the bind (The schema must also allow the entry to have this attribute). If the `cleartext` `USE` flag was enabled, then OpenLDAP will allow the `userPassword` to store the password literally, but this is highly insecure and should only be used for testing. Instead, a password hashing algorithm should be used.

OpenLDAP supports several password hashing algorithms out-of-the-box, and more can be enabled through modules which are installed by `USE` flags.

** Warning**\
Even if a strong password hashing & salting scheme is used, it will still not offer perfect protection against any attempts at password cracking. Care must be taken to prevent anyone or anything from reading the LDAP database files. These files should have the most restrictive permissions possible while still allowing the daemon to function.

An entry with a hashed password looks like this:

[FILE] **`hashed_password.ldif`Example Hashed Password**

    dn: uid=larry,ou=users,dc=example,dc=com
    objectClass: person
    objectClass: posixAccount
    objectClass: top
    homeDirectory: /home/larry
    cn: Larry the Cow
    sn: Cow
    uid: larry
    uidNumber: 1001
    gidNumber: 1000
    # Typical textual representation of a hashed password
    userPassword: LryXSzUzmhjvY99K9wWC1iPE6TyRTeme

    # Sometimes the entry will be displayed as hexadecimal.
    # In this case the attribute will have two colons
    # userPassword:: 61615d61a81556ab82c8f4ea0573eb03c048cf33

The value inside the braces, `SSHA` in this case, is the hashing/salting algorithm. The text immediately following is the hashed data. In order to generate the `userPassword` value, the `slappasswd` tool can be used. [-h] specifies the desired hashing algorithm.

`user `[`$`]`slappasswd -h ''`

    New password:
    Re-enter new password:
    McNjDs0vQlBpfR8NKFttwTBBb0awnOJR

This output can be saved to a file, or piped to another command to change a password. Here is an example script that prompts for a password, and then generates a new LDIF record which is piped to slapmodify to change the password of the Root DN.

[CODE] **Example script for changing the RootDN password of an offline database**

    #!/bin/bash

    # This example uses the ARGON2 algorithm which must be loaded from a module
    # If a different builtin algorithm is used, the "-o module-path=..." and "-o module-load=..." options can be removed
    HASH_ALGO=''
    HASH_MODULE='argon2.so'

    mdb,cn=config'

            # Generate an LDIF change record
            echo   'changeType: modify'
            echo   'replace: olcRootPW'
            printf "olcRootPW: %s\n" \
                  $(slappasswd -o module-path=/usr/lib64/openldap/openldap -o module-load="$" -h "$")

    # Pipe the change record with the new hashed password into slapmodify
    # Use "-n 0" because this is a modification to the config database
    } | slapmodify -v -n 0

In the previous example, a hash algorithm is used which is not built into OpenLDAP. It must first be enabled by a `USE` flag and then loaded as a module. The module can be loaded by `slappasswd` on the command line, but in order for `slapd` to understand the format of the entry, it must have the module added to its configuration database. See TODO (Advanced Config/Modules).

## [Advanced configuration]

### [TLS]

Transport Layer Security (TLS) can be enabled on `slapd` to ensure that communication between clients and the daemon is encrypted and safe from eavesdropping. **This is absolutely necessary if the LDAP server is going to store any personal or security-sensitive information, including passwords.**

`slapd` supports implicit (`ldaps://`) and explicit (`STARTTLS`) TLS.

-   Implicit TLS can only be enabled by passing the [-h] `ldaps://` command line argument to `slapd` when it is started. The Gentoo init scripts do this by default, but this can be changed by editing [/etc/conf.d/slapd]. When implicit TLS is enabled, `slapd` will listen for connections on port 636 by default.
-   Explicit TLS is always an option by default. Its use must be initiated by the client. It works when clients connect to the normally unencrypted LDAP port 389 and issue the `STARTTLS` command to upgrade the connection to an encrypted channel. Explicit TLS will not be used if unencrypted connections are completely disabled in [/etc/conf.d/slapd]. For more information on this behavior, see `man 8 slapd`.

Before TLS will work, `slapd` must be configured with a certificate and private key. For information on creating and managing certificates, see [Certificates](https://wiki.gentoo.org/wiki/Certificates "Certificates") and [Certificates/Become your own CA](https://wiki.gentoo.org/wiki/Certificates/Become_your_own_CA "Certificates/Become your own CA"). Once a certificate and key are stored in a safe place on the filesystem, `slapd` can be configured to use them by adding a few options to the configuration database. It does not seem to be possible to add these entries while the daemon is running. A few different methods of updating the config database have already been demonstrated in this article. One of the previous methods could be used, but a different method using bash scripting will be demonstrated here:

[CODE] **Example script to add or update TLS certificates**

    #!/bin/bash

    # Set these variables to the paths of your certificate and key
    CERT_PATH="/path/to/domainCert.pem"
    PRIVKEY_PATH="/path/to/private.key.pem"

    # To set the attributes for the first time, use 'add'
    # To update the attributes later, use 'replace'
    OP='add'

    make_rec()

    rc-service slapd stop && \
    make_rec $OP 'olcTLSCertificateFile' $CERT_PATH | slapmodify -v -n 0 && \
    make_rec $OP 'olcTLSCertificateKeyFile' $PRIVKEY_PATH | slapmodify -v -n 0 && \
    chown -R ldap:ldap /etc/openldap/slapd.d && \
    rc-service slapd start

The script can be simply edited according to the comments. Systemd users should also change the `rc-service slapd` start/stop lines to `systemctl` start/stop `slapd`. If the daemon does not come back up after running the script, the most likely problem is permissions of the certificate/key files. Recall that `slapd` is running as user [ldap]. If the [ldap] user does not have permission to access the files or their parent directories, then the daemon will not be able to read the files and will refuse to start. If necessary, the permissions should be changed, but **care should be taken to ensure the private key is inaccessible by any user that does not strictly require access.**

** Important**\
The `ldap*` utilities included with OpenLDAP do not trust any certificate authorities by default. If they are to be used to connect to an LDAP server using any kind of TLS, the connection will fail unless they are configured to recognize the CA that signed the server\'s certificate. If the server has a certificate signed by a public certificate authority, then the trust can be established by adding the line `TLS_CACERTDIR /etc/ssl/certs` to the file [/etc/openldap/ldap.conf].

### [Modules]

The modules loaded by the daemon are stored in entries of the config tree. The first module entry ([cn=module,cn=config]) was added when the config database was initialized. Additional modules can be loaded at runtime by creating new module entries in LDIF files and adding them to the tree with `ldapadd`. It does not appear to be possible to remove modules once loaded without first taking the daemon offline.

[FILE] **`new_mods.ldif`Example Module Entry**

    # It may be necessary to increment the index number after the module name if module entries have already been added
    #             v
    dn: cn=module,cn=config
    objectClass: olcModuleList
    #
    # Add as many modules here as desired
    olcModuleLoad: back_relay.so
    olcModuleLoad: back_null.so
    olcModuleLoad: argon2.so
    #
    # The default path where modules are stored.
    # If there is an error, check to make sure the module file is actually there
    # Some modules are not present unless their USE flag was enabled
    olcModulePath: /usr/lib64/openldap/openldap

`user `[`$`]`ldapadd -v -D "cn=Manager,cn=config" -W -H ldap://localhost -f new_mods.ldif`

### [Schema]

Throughout this document, examples of DIT/LDIF entries have been presented with arbitrary attributes like [cn], [sn], and [homeDirectory]. LDAP and X.500 directories in general do not require entries to follow any particular pattern or structure. However, having a set of rules regarding the structure of an entry makes it much easier for people and software accessing the directory to understand the data and make changes. These rule sets are called schemas. Schemas can rigorously define which entries may/should/must have which attributes. They can also define a set of legal values that an attribute can have.

When a schema is loaded by `slapd`, it will be enforced, and any attempt to change an entry that violates the schema will be refused with an error message. System administrators can create arbitrary schemas and use them with `slapd`, but OpenLDAP also ships with a set of widely recognized schemas stored in [/etc/openldap/schema/]. This section will focus on the included schemas.

When in use, schemas are stored in the configuration database as child entries of the [cn=schema,cn=config] entry. Each schema entry contains dozens of attributes that actually describe the schema. It is possible to create schema entries by hand that will work, but this is tedious and error prone. Instead, the [.ldif] files in the schema directory schould be used.

The schema directory includes a [README] file which provides a description for each of the included schemas. Additionally, each of the [.schema] and [.ldif] files in the directory contain a header with commentary about the schema file. The [.schema] and [.ldif] files with the same prefix generally contain the same schema information. For example, [msuser.schema] and [msuser.ldif] both contain the Microsoft schema. The only difference is that the [.schema] files are formatted for inclusion in the legacy [slapd.conf] configuration file, and the [.ldif] files are formatted for use in the newer configuration database.

** Note**\
Some schema files are dependent on each other and must be added in a certain order. Most, if not all, of the schemas included with OpenLDAP depend on the [core.ldif] schema, so it should be added first.

If all that is desired is adding new schemas, then the [.ldif] files in the schema directory can be fed directly into `ldapadd` or `slapadd`.

`user `[`$`]`ldapadd -v -D "cn=Manager,cn=config" -W -H ldaps://example.com < core.ldif `

If schemas need to be changed or removed, then the process is a little more involved. It does not appear to be possible to remove or edit schemas while the daemon is running.

`root `[`#`]`sytemctl stop slapd`

Once the daemon is stopped, the schemas can be changed with `slapmodify`. Keep in mind that removing or replacing the schema of a database that already has entries in it may cause errors if the existing entries fail to conform to the new schema.

If it is desired to **completely remove all schema information from the database** and \"start from scratch\", then the `slapcat` tool can be used. The purpose of this tool is to read an existing OpenLDAP database on the filesystem and output a new LDIF file containing all of its entries.

In the next example, the `slapcat` command will read the entire contents of the config database, except it will filter out all the schema information.

`root `[`#`]`slapcat -n 0 -H "ldap:///???(!(entryDN:dnSubtreeMatch:=cn=schema,cn=config))" > new_schemas.ldif`

The output file from the previous command can then be opened and the **new** schema information appended:

[FILE] **`new_schemas.ldif`(Add to the end of the file)**

    # This entry is the parent of all other schema entries
    # and it needs to come before them in the file
    dn: cn=schema,cn=config
    objectClass: olcSchemaConfig
    cn: schema

    # Use the include directive to copy the contents of the LDIF
    # files in the schema directory into this file
    include: file:///etc/openldap/schema/core.ldif

    # Make sure blank lines are kept in-between entries
    include: file:///etc/openldap/schema/cosine.ldif

    include: file:///etc/openldap/schema/inetorgperson.ldif

Now that the new LDIF file is prepared with the correct schemas, it can be written back to the [slapd.d/] directory. This file already includes all of the content of that directory minus the old schemas which were filtered out. First, create a backup of [slapd.d/] directory in case anything goes awry, then overwrite it with `slapadd`:

`root `[`#`]`mv /etc/openldap/slapd.d/ /etc/openldap/slapd.d.old`

`root `[`#`]`mkdir /etc/openldap/slapd.d`

`root `[`#`]`slapadd -n 0 -F /etc/openldap/slapd.d/ -l new_schemas.ldif`

`root `[`#`]`chown -R ldap:ldap /etc/openldap/slapd.d`

`root `[`#`]`slaptest`

If the `slapadd` command fails with an error, it may be because the schemas added have an unsatisfied dependency. If everything succeeds without errors, then the daemon can now be restarted.

`root `[`#`]`sytemctl start slapd`

Beware, if the main database was not empty when the schema was changed, the daemon may refuse to start or emit lots of errors if the old entries do not conform to the new schema.

## [Security]

** Warning**\
This entire page does not provide a very secure LDAP service, and this section is still under construction.

-   access control and directory information tree could enable at least guessing entries by receiving different error codes (not found vs. invalid privileges) even without proper authentication or permission
-   ACLs allow to hide attributes, mind the defaults that often allow unauthenticated world readable attributes, sometimes they are omitted in simple queries but are visible if selected explicitely
-   unique identifiers must be really unique, never re-assigned, unrelated to a real person\'s personal data and immutable over the entire lifespan, last names not only change but names in general are not limited to 2 words containing only US-ASCII characters^[\[1\]](#cite_note-1)^
-   make regular backups and check their usability

### [Access Control]

TODO

### [SASL bind]

TODO

### [Attacks on LDAP servers]

TODO

## [Troubleshooting]

-   `` kill -INT `cat /run/openldap/slapd.pid` `` -- Graceful shutdown if regular service script fails or a daemonized test run does not stop^[\[2\]](#cite_note-2)^

## [See also]

-   [OpenLDAP 2.6 Administrator\'s Guide](https://www.openldap.org/doc/admin26/index.html)
-   [The LDAP Wiki hosted by services.cisus.com](https://ldapwiki.com/wiki/)
-   [Neil Wilson\'s Website for learning about LDAP](https://ldap.com/)
-   [Lightweight Directory Access Protocol on Wikipedia](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol)
-   [Centralized authentication using OpenLDAP](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP "Centralized authentication using OpenLDAP")
-   [BIND](https://wiki.gentoo.org/wiki/BIND "BIND"), DNS server

\
Useful manpages

-   [slapd(8)]
-   [slapd.conf(5)]
-   [slapd-config(5)]
-   [LDIF(5)]
-   [slapmodify(8)]
-   [ldapmodify(1)]
-   [ldap.conf(5)]

\
Packages supporting LDAP-authentication/ user management:

-   [[[net-nds/jxplorer]](https://packages.gentoo.org/packages/net-nds/jxplorer)[]]
-   [[[net-nds/phpldapadmin]](https://packages.gentoo.org/packages/net-nds/phpldapadmin)[]]
-   [[[www-apps/dokuwiki]](https://packages.gentoo.org/packages/www-apps/dokuwiki)[]]
-   [[[www-apps/icingaweb2]](https://packages.gentoo.org/packages/www-apps/icingaweb2)[]], also provides monitoring

## [References]

1.  [[[↑](#cite_ref-1)] [[\[1\]](https://ldapwiki.com/wiki/Best%20Practices%20For%20Unique%20Identifiers)Best Practices For Unique Identifiers]]
2.  [[[↑](#cite_ref-2)] [[\[2\]](https://openldap.org/doc/admin26/runningslapd.html)OpenLDAP Software 2.6 Administrator\'s Guide]]