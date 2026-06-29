*OpenLDAP* is a free implementation of the X.500 directory service standards. LDAP stands for *Lightweight Directory Access Protocol*. The *lightweight* part comes from the fact it does not implement ALL of the standard. X.500 is quite unwieldy, and much of it has been superseded (e.g. the OSI networking stack) or considered impractical (e.g. such as canonical per entry Distinguished Names) or undesirable (e.g. publishing directories of private entities like businesses).

## Contents

-   [[1] [Introduction to LDAP]](#Introduction_to_LDAP)
-   [[2] [Installing OpenLDAP]](#Installing_OpenLDAP)
-   [[3] [Introduction to LDIF files]](#Introduction_to_LDIF_files)
    -   [[3.1] [Add operation]](#Add_operation)
    -   [[3.2] [Delete operation]](#Delete_operation)
    -   [[3.3] [Modify operation]](#Modify_operation)
        -   [[3.3.1] [Add Attribute]](#Add_Attribute)
        -   [[3.3.2] [Delete Attribute]](#Delete_Attribute)
        -   [[3.3.3] [Replace Attribute]](#Replace_Attribute)
        -   [[3.3.4] [Modify multiple attributes on a single DN]](#Modify_multiple_attributes_on_a_single_DN)
    -   [[3.4] [Rename (modrdn)]](#Rename_.28modrdn.29)
    -   [[3.5] [Move (moddn)]](#Move_.28moddn.29)
-   [[4] [LDAP hierarchy and searches]](#LDAP_hierarchy_and_searches)
-   [[5] [Configuring OpenLDAP]](#Configuring_OpenLDAP)
    -   [[5.1] [Quick Start]](#Quick_Start)
    -   [[5.2] [Starting the slapd daemon]](#Starting_the_slapd_daemon)
        -   [[5.2.1] [OpenRC]](#OpenRC)
        -   [[5.2.2] [Systemd]](#Systemd)
    -   [[5.3] [Schemas]](#Schemas)
        -   [[5.3.1] [Add a schema]](#Add_a_schema)
        -   [[5.3.2] [Convert a .schema file to LDIF]](#Convert_a_.schema_file_to_LDIF)
    -   [[5.4] [Modules]](#Modules)
    -   [[5.5] [Security]](#Security)
        -   [[5.5.1] [TLS]](#TLS)
        -   [[5.5.2] [Kerberos]](#Kerberos)
            -   [[5.5.2.1] [OpenRC]](#OpenRC_2)
            -   [[5.5.2.2] [Systemd]](#Systemd_2)
        -   [[5.5.3] [Enforce encryption]](#Enforce_encryption)
        -   [[5.5.4] [Access Control]](#Access_Control)
        -   [[5.5.5] [Limits]](#Limits)
        -   [[5.5.6] [Remote RootDN access]](#Remote_RootDN_access)
    -   [[5.6] [Replication]](#Replication)
        -   [[5.6.1] [Replication considerations]](#Replication_considerations)
        -   [[5.6.2] [Preparing the producer for delta-syncrepl (Optional)]](#Preparing_the_producer_for_delta-syncrepl_.28Optional.29)
        -   [[5.6.3] [Mirroring configuration]](#Mirroring_configuration)
        -   [[5.6.4] [Read-only replicas configuration]](#Read-only_replicas_configuration)
-   [[6] [Populating the directory]](#Populating_the_directory)
    -   [[6.1] [Populating the directory via creation]](#Populating_the_directory_via_creation)
    -   [[6.2] [Populating the directory via import]](#Populating_the_directory_via_import)
-   [[7] [Adminstration]](#Adminstration)
    -   [[7.1] [Backing up the database]](#Backing_up_the_database)
    -   [[7.2] [Clearing all schemas]](#Clearing_all_schemas)
    -   [[7.3] [Open file limits]](#Open_file_limits)
        -   [[7.3.1] [OpenRC]](#OpenRC_3)
        -   [[7.3.2] [Systemd]](#Systemd_3)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [Turning up the log level]](#Turning_up_the_log_level)
-   [[9] [See also]](#See_also)

## [Introduction to LDAP]

LDAP is a directory service. It\'s similar to a database but with different aims. LDAP is hierarchical database, optimized for reading and replication. It does not have same [ACID](https://en.wikipedia.org/wiki/ACID) properties of a standard database.

An LDAP database consists of *branches* called **Distinguished Names** or a **DN**s. Example distinguished names are *uid=johnsmith,ou=people,dc=example,dc=com* and *olcDatabase=config,cn=config*. Each DN may have additional *branches* or more distinguished names. So for the DN *ou=people,dc=example,dc=com*, it is possible to create a new branch, called *uid=johnsmith* and thus a new DN. A DN can also have attributes. What these attributes mean is defined in a **schema**. Schemas define:

-   The [Object Indentifier](https://en.wikipedia.org/wiki/Object_identifier) (OID) of the attribute (every attribute has a unique OID)
-   Matching rules (like case sensitivity)
-   Syntax of the attribute (like its type)
-   Whether the attribute is single-valued or multi-valued
-   One special attribute is the *objectClass*. Object classes:
    -   Can be either STRUCTURAL or AUXILIARY. A DN must have exactly one STRUCTURAL object class, and zero or more AUXILIARY object classes.
    -   What object classes it derives from
    -   Required attributes for the DN.
    -   Optional attributes for the DN.

## [Installing OpenLDAP]

Before installing OpenLDAP, some USE flags need to be set or cleared first.

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

On most profiles the [[[minimal]](https://packages.gentoo.org/useflags/minimal)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is set, which disables installation of the server and supporting files. The [[[sasl]](https://packages.gentoo.org/useflags/sasl)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is recommended for all users, and required for Kerberos users (in addition to the [[[kerberos]](https://packages.gentoo.org/useflags/kerberos)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag).

The [[[debug]](https://packages.gentoo.org/useflags/debug)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] is virtually required for OpenLDAP servers - the server produces no output (diagnostic or otherwise) at all in the syslog and the **olcLogLevel** option has little effect (except for stats), which makes it difficult to troubleshoot. This is different than most users of the flag, where it should normally be turned off

Set the desired flags in [/etc/portage/package.use/openldap], as an example:

[FILE] **`/etc/portage/package.use/openldap`**

    net-nds/openldap debug -minimal overlays sasl

Once installed, there are 2 sets of utilities: the *ldap* ones and the *slap* ones. The *ldap* ones run against a running LDAP server, whereas the *slap* ones operate offline on the server database directly.

## [Introduction to LDIF files]

OpenLDAP uses directory entries itself for configuration, so it necessary to use LDIF for bootstrapping. The initial configuration is created as an LDIF file and loaded on the server with **slapadd**. Once the server is running, the **ldapadd** and **ldapmodify** can be used to make further changes. If the server is unable to start, **slapmodify** can be used to load LDIF files to fix it.

An LDIF file is a plain text file with a particular format. Distinguished names have 5 operations defined on them: *add*, *delete*, *modify*, rename (*modrdn*), and move (*moddn*).

A LDIF file looks like this:

[CODE] **Sample LDIF file**

    dn: uid=ebunny,ou=people,dc=example,dc=com
    changetype: add
    objectClass: inetOrgPerson
    objectClass: posixAccount
    objectClass: shadowAccount
    sn:: QnU6bm55Cg==
    cn: ebunny
    cn: Easter Bunny
    # This is a comment
    uid: ebunny
    uidNumber: 20000
    gidNumber: 20000
    homeDirectory: /home/ebunny
    loginShell: /bin/bash
    gecos: This is a store ab
     out a man named Bunny
    jpegPhoto:< file:///root/ebunny.jpg

    dn: uid=ebunny,ou=people,dc=example,dc=com
    changetype: modify
    replace: sn
    sn: bunny
    -
    delete: jpegPhoto

    dn: uid=sclaus,ou=people,dc=example,dc=com
    changetype: delete

Note the following things:

-   Multiple operations can be done in an LDIF file.
-   All LDIF entries start with \"dn: \" followed by the DN of the entry to operate on.
-   The next line the modification operation requested on the DN.
-   For the *modify* operation, either *add*, *replace*, or *delete* must be specified.
-   Multiple attributes may be updated in a single *modify* operation.
-   Multi-valued attributes may be specified multiple times.
-   Binary attributes can be added by suffixing a another colon to end of *attribute*:.
-   Files may be used as attribute values by suffixing a \< to end of *attribute*:.
-   LDIF lines may continued onto the next line by stating them with a single space.
-   Comments are started by a \# in column 1.

### [Add operation]

To add a DN, start the entry with \"dn: \" followed by the DN to add. The next line must be \"changetype: add\". On each additional line, specify the attributes to add along with their values in the format *attribute*: *value*. The *add* operation will fail if the DN already exists.

[CODE] **Add a DN**

    dn: uid=ebunny,ou=people,dc=example,dc=com
    changetype: add
    objectClass: inetOrgPerson
    objectClass: posixAccount
    objectClass: shadowAccount
    sn: bunny
    cn: ebunny
    cn: Easter Bunny
    uid: ebunny
    uidNumber: 20000
    gidNumber: 20000
    homeDirectory: /home/ebunny
    loginShell: /bin/bash
    gecos: Easter Bunny

Process the file with **ldapmodify**/**slapmodify**:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f filename.ldif`

If the file contains only *add* operations, the **ldapadd**/**slapddd** utilities may be used instead. In that case, the *changetype: add* lines are optional.

`root `[`#`]`ldapadd -H ldapi:/// -Y EXTERNAL -f filename.ldif`

### [Delete operation]

To delete a DN, start the entry with \"dn: \" followed by the DN to delete. The next line must be \"changetype: delete\". The *delete* operation will fail if the DN does not exist.

[CODE] **Delete a DN**

    dn: uid=ebunny,ou=people,dc=example,dc=com
    changetype: delete

Only \"leaf\" DNs can be deleted. Process the file with **ldapmodify**/**slapmodify**.

`root `[`#`]`ldapmodify -H ldapi:// -Y EXTERNAL -f filename.ldif`

The DN can alsp be deleted directly using the **ldapdelete** command

`root `[`#`]`ldapdelete -H ldapi:// -Y EXTERNAL uid=ebunny,ou=people,dc=example,dc=com`

### [Modify operation]

To modify a DN, start the entry with \"dn: \" followed by the DN to modify. The next line must be \"changetype: modify\". There are 3 sub-operations for *modify*, each with its own syntax.

Process the file with **ldapmodify**/**slapmodify**:

`root `[`#`]`ldapmodify -H ldapi:// -Y EXTERNAL -f filename.ldif`

#### [Add Attribute]

To add an attribute to a DN, the next line should be \"add: \" follow by the attribute name to add. The next line is in the format *attribute*: *value*. Multi-valued attributes may be specific multiple times, one of each value. If the attribute doesn\'t exist, it\'s created. If it already exists and it\'s multi-valued, an additional value is added. If it already exists and it\'s not multi-valued, the operation fails.

[CODE] **Add an attribute**

    dn: olcDatabase=mdb,cn=config
    changetype: add
    add: olcLimits
    olcLimits: dn.exact="cn=replicator,dc=example,dc=com"
      time.soft=unlimited time.hard=unlimited
      size.soft=unlimited size.hard=unlimited

#### [Delete Attribute]

To delete an attribute from a DN, the next line should be \"delete: \" follow by the attribute name to delete. If the attribute is multi-valued, ALL values are deleted. The operation fails if the attribute does not exist.

[CODE] **Delete an attribute**

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    delete: olcRootPW

#### [Replace Attribute]

To replace an attribute for a DN, the next line should be \"replace: \" follow by the attribute name to replace. The next line is in the format *attribute*: *value*. The *attribute*: *value* may be specified multiple times but the *attribute* must be the same. If the attribute is multi-valued, ALL values are replaced. If the attribute does not exist, it is created. If multiple values are added to a non-multi-valued attribute, the operation fails.

[CODE] **Replace an attribute**

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    replace: olcAccess
    olcAccess: to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external
     ,cn=auth" manage
      by dn.exact="cn=replicator,dc=example,dc=com" read
      by * break
    olcAccess: to attrs=userPassword
      by self write
      by anonymous auth
      by * none
    olcAccess: to *
      by * read

** Note**\
The *replace* operation is NOT atomic. If an attribute needs to be atomically replaced, do a *delete* then an *add* in the same *modify* statement instead using the section below

#### [Modify multiple attributes on a single DN]

A *modifiy* operation may change several attributes in a single statement. Separate each attribute change on the DN with a dash (-) on its own line:

[CODE] **Add an attribute**

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    replace: olcAccess
    olcAccess: to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external
     ,cn=auth" manage
      by dn.exact="cn=replicator,dc=example,dc=com" read
    olcAccess: to attrs=userPassword
      by self write
      by anonymous auth
      by * none
    olcAccess: to *
      by * read
    -
    changetype: add
    add: olcLimits
    olcLimits: dn.exact="cn=replicator,dc=example,dc=com"
      time.soft=unlimited time.hard=unlimited
      size.soft=unlimited size.hard=unlimited
    -
    delete: olcRootPW

Note this a little different that 3 different *modify* operations: They must all succeed, or none do.

### [][Rename (modrdn)]

To rename a DN, start the entry with \"dn: \" followed by the DN to rename. The next line must be \"changetype: modrdn\" (stands for Modify Relative DN). On the line after, specify \"newrdn: \" and the new name. On the next line, specify \"deleteoldrdn: \" and either 0 or 1, 0 keeps the old entry as an alias; 1 does not.

[CODE] **Rename a DN**

    dn: ou=people,dc=example,dc=com
    changetype: modrdn
    newrdn: ou=aliens
    deleteoldrdn: 1

Process the file with **ldapmodify** (None of the backends current implement the *modrdn* operation for **slapmodify**)

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f filename.ldif`

The DN can also be renamed directly using the **ldapmodrn** utlity:

`root `[`#`]`ldapmodrdn -H ldapi:/// -Y EXTERNAL ou=people,dc=example,dc=com ou=aliens`

### [][Move (moddn)]

To move a DN, start the entry with \"dn: \" followed by the DN to rename. The next line must be \"changetype: moddn\" (stands for Modify DN). On the line after, specify \"newsuperior: \" and the new DN to place this DN under, pruning one part of the tree and grafting onto another . On the next line, specify \"deleteoldrdn: \" and either 0 or 1, 0 keeps the old entry as an alias; 1 does not.

[CODE] **Move a a DN**

    dn: uid=ebunny,ou=people,dc=example,dc=com
    changetype: moddn
    newsuperior: ou=animals,dc=example,dc=com
    deleteoldrdn: 1

Process the file with **ldapmodify**/**slapmodify**:

`root `[`#`]`ldapmodify -H ldapi:// -Y EXTERNAL -f filename.ldif`

## [LDAP hierarchy and searches]

LDAP directories are hierarchical. The OU (organizational unit) typically used to divide up the directory, and an OU can have other OUs under it. Each OU can have its own attribute/value pairs. An OU typically represents a \"resource type\" or \"administrative division\". For the \"resource\" case, \"People\" (ou=People,dc=example,dc=com) represents one resource of a organization, \"Hosts\" (ou=Hosts,dc=example,dc=com) is another resource. For the \"administrative division\" case, the People OU could be further divided in OUs geographically (like ou=EMEA,ou=People,dc=example,dc=com) or divisions of the company (ou=Accounting,ou=People,dc=example,dc=com). OUs may be nested and are limited only by the length of the DN (255 characters).

LDAP searches are done with filters. The filter language is quite extensive: there are [tutorials of the LDAP filter language](//ldap.com/ldap-filters/) or consult [RFC4515](//docs.ldap.com/specs/rfc4515.txt). Normally admins do not need to write complicated filters, however, filters used by the apps will be shown in the logs and are useful for debugging.

Note that while LDAP is hierarchical, the data may not be used that way. For example, [[[sys-auth/sssd]](https://packages.gentoo.org/packages/sys-auth/sssd)[]] searches the entire directory for a user. If there are multiple OUs that user, the search will return the union of them all, no matter where in directory they are. On the other hand, when sudo checks LDAP, it restricts is search to its OU.

** Warning**\
An OU cannot be relied on to be a \"container\". Depending on the search base used the by application - which may be the entire directory - it can return data from multiple OUs. In particular, you cannot have a DN or attribute value that the client expects to be unique (like username or UID) in different OUs under the same search base, even though it\'s valid and the LDAP server allows it.

LDAP searches are unordered: The server may return the results in whatever order it pleases and need to not be consistent between searches. Sorting must be done by client.

## [Configuring OpenLDAP]

Once OpenLDAP is installed with the correct USE flags, The server must be configured.

### [Quick Start]

Neither the configuration or LDIF files that are bundled in OpenLDAP, or the OpenLDAP Quick Start is suitable for a Gentoo installation Instead, using the following file. Call it [slapd.ldif.in]

[FILE] **`slapd.ldif.in`**

    # Config DN
    dn: cn=config
    objectClass: olcGlobal
    cn: config
    # Gentoo locations of files
    olcArgsFile: /run/openldap/slapd.args
    olcPidFile: /run/openldap/slapd.pid
    # Basic logging
    olcLogLevel: 768

    # Schema DN
    dn: cn=schema,cn=config
    objectClass: olcSchemaConfig
    cn: schema

    # Include core schema
    include: file:///etc/openldap/schema/core.ldif

    # Database frontend DN. Any option listed here affects ALL LDAP databases
    dn: olcDatabase=frontend,cn=config
    objectClass: olcDatabaseConfig
    olcDatabase: frontend

    # Config database DN
    dn: olcDatabase=config,cn=config
    objectClass: olcDatabaseConfig
    olcDatabase: config
    olcAccess: to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external
     ,cn=auth" manage by * none

    # Monitoring database DN
    dn: olcDatabase=monitor,cn=config
    objectClass: olcDatabaseConfig
    olcDatabase: monitor
    olcAccess: to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external
     ,cn=auth" read by dn.base="cn=Manager,$" read by * none

    # Database DN for organization directory info
    dn: olcDatabase=mdb,cn=config
    objectClass: olcDatabaseConfig
    objectClass: olcMdbConfig
    olcDatabase: mdb
    # Default database size. If needed, uncomment and increase.
    #olcDbMaxSize: 1073741824
    olcSuffix: $
    olcDbDirectory: /var/lib/openldap-data
    olcRootDN: cn=Manager,$
    olcDbIndex: objectClass eq,pres
    olcDbIndex: ou,cn,mail,surname,givenname eq,pres,sub
    olcAccess: to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external
     ,cn=auth" manage by * break
    olcAccess: to attrs=userPassword
      by self write
      by anonymous auth
      by * none
    olcAccess: to *
      by * read
    olcLimits: dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth"
      time.soft=unlimited time.hard=unlimited
      size.soft=unlimited size.hard=unlimited

Run the following command, replacing **dc=example,dc=com** with your director component information.

`user `[`$`]`sed s/\$/dc=example,dc=com/g < slapd.ldif.in > slapd.ldif`

Create, populate and set the permissions of the [/etc/openldap/slapd.d] directory

`root `[`#`]`( umask 077 && mkdir /etc/openldap/slapd.d ) `

`root `[`#`]`slapadd -n 0 -l slapd.ldif -F /etc/openldap/slapd.d `

`root `[`#`]`chown -R ldap:ldap /etc/openldap/slapd.d`

### [Starting the slapd daemon]

#### [OpenRC]

Edit [/etc/conf.d/slapd] as follows

[FILE] **`/etc/conf.d/slapd`(Excerpt)**

    # Comment this line to disable the old slapd.conf file
    #OPTS_CONF="-f /etc/$/slapd.conf"
    # Uncomment this to use the new slapd.d configuration directory
    OPTS_CONF="-F /etc/$/slapd.d"

Note that OpenRC places the *ldapi* socket file in a nonstandard place. So change any instances of **ldapi:///** to **ldapi://%2frun%2fopenldap%2fslapd.sock** in the subsequent instructions.

Then enable and start the daemon:

`root `[`#`]`rc-config add slapd default `

`root `[`#`]`rc-service slapd start`

#### [Systemd]

Edit [/etc/systemd/system/slapd.service.d/00gentoo.conf] as follows:

[FILE] **`/etc/systemd/system/slapd.service.d/00gentoo.conf`(Excerpt)**

    # Use the classical configuration file:
    #Environment="SLAPD_OPTIONS=-f /etc/openldap/slapd.conf"
    # Use the slapd configuration directory:
    Environment="SLAPD_OPTIONS=-F /etc/openldap/slapd.d"

Then enable start the daemon:

`root `[`#`]`systemctl enable --now slapd`

### [Schemas]

One schema is required: the core schema. Without it, no entries can be added to the directory. Additional schema are usually required. Some schema have dependencies on other schemas. In that case, all the schemas to be added must be included in the same LDIF file.

#### [Add a schema]

To add a schema, create an LDIF file with an \"include: \" statement for each schema to be added, along with its dependencies.

For example. the **nis** schema depends on the **cosine** schema. So both need to included, starting with the dependencies

[FILE] **`addschema.ldif`**

    include: file:///etc/openldap/schema/cosine.ldif

    include: file:///etc/openldap/schema/nis.ldif

Then add it to the server

`root `[`#`]`ldapadd -H ldapi:/// -Y EXTERNAL -f addschema.ldif`

** Warning**\
Schemas cannot be removed while the server is online. Removing schemas usually results in disastrous consequences, so its not something to take lightly!

#### [Convert a .schema file to LDIF]

OpenLDAP has supported .ldif file for schemas since version 2.3 (release year 2005). Some programs and packages, however, still do not ship LDIF files and ship .schema files instead. OpenLDAP has a utility to convert them.

A good example is [[[app-admin/sudo]](https://packages.gentoo.org/packages/app-admin/sudo)[]]. It ships a schema file, not an LDIF file, so it must be converted. To covert:

Create a old-style configuration file that includes the schema. If the schema has dependencies, those must be included before the desired schema in the configuration file.

[FILE] **`sudo-schema.conf`**

    include /etc/openldap/schema/sudo.schema

Create an empty directory:

`user `[`$`]`mkdir myconfig`

Run the **slaptest** command with the proper arguments:

`user `[`$`]`slaptest -f sudo-schema.conf -F myconfig`

Look for the LDIF file in the [myconfig/cn=config/cn=schema] directory. For sudo, this file is called [sudo.ldif]. Clean up the file and rename it:

`user `[`$`]`sed -e '/^#/d' -e '/^dn: /s/$/,cn=schema,cn=config/g' -e 's///g' -e '/^structuralObjectClass/d' -e '/^entryUUID/d' -e '/^creatorsName/d' -e '/^createTimestamp/d' -e '/^entryCSN/d' -e '/^modifiersName/d' -e '/^modifyTimestamp/d' < myconfig/cn\=config/cn\=schema/cn\=\sudo.ldif > sudo.ldif`

The LDIF file may now be added like any other schema.

`root `[`#`]`ldapadd -H ldapi:/// -Y EXTERNAL -f sudo.ldif`

The temporary files can now be cleaned up:

`user `[`$`]`rm -fr myconfig`

### [Modules]

Modules extend the functionality of OpenLDAP. There are modules for different backend type (like mdb), encryption algorithms (like argon2) and overlays (like accesslog). Some modules are compiled in, like the *back_mdb* and *syncrepl* modules, and (if [[[argon2]](https://packages.gentoo.org/useflags/argon2)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] is specified), argon2.

For example, to add the password policy module (assuming [[[overlays]](https://packages.gentoo.org/useflags/overlays)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] has been set, create the following LDIF file:

[FILE] **`add-module.ldif`**

    dn: cn=module,cn=config
    changetype: add
    objectClass: olcModuleList
    cn: module
    olcModulePath: /usr/lib64/openldap/openldap
    olcModuleLoad: ppolicy.so

Add the entries to the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f add-module.ldif`

** Warning**\
Modules cannot be removed while the server is online. Removing modules usually results in disastrous consequences, so its not something to take lightly!

### [Security]

OpenLDAP supports two popular security solutions: TLS (SSL) and Kerberbos (GSSAPI). Both may be used, if desired.

#### [TLS]

A certificate is required to setup TLS. Typically a certificate is obtained either through an in house enterprise certificate authority, or from an external authority, like [Let\'s Encrypt](https://wiki.gentoo.org/wiki/Let%27s_Encrypt "Let's Encrypt"). Since LDAP servers are not usually exposed to the Internet, the former option is preferred.

The TLS server needs the CA certificate, the server certificate, and the key. The certificates and key should be placed [/etc/openldap/ssl] with the proper permissions (444 for the certificates, 400 for the key). Change ownership of the files to the *ldap* user and group. The key should not have a password on it.

Create an LDIF file to add the location of the CA certificate, server certificate, and the key. The exmaple below expects the CA certificate at [/etc/openldap/ssl/ca.crt], the server certificate at [/etc/openldap/ssl/ldap.crt], and they key at [/etc/openldap/ssl/ldap.key]

[FILE] **`ldap-tls.ldif`**

    dn: cn=config
    changetype: modify
    add: olcTLSCACertificateFile
    olcTLSCACertificateFile: /etc/openldap/ssl/ca.crt
    -
    add: olcTLSCertificateFile
    olcTLSCertificateFile: /etc/openldap/ssl/ldap.crt
    -
    add: olcTLSCertificateKeyFile
    olcTLSCertificateKeyFile: /etc/openldap/ssl/ldap.key

Add the entries to the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f ldap-tls.ldif`

The LDAP clients must be configured with the certificate of the CA the server\'s cert in signed with. For each client, copy the CA cert to [/etc/openldap/ca.crt] and set the permissions to 444. Edit [/etc/openldap/ldap.conf] and add the following line:

[FILE] **`/etc/openldap/ldap.conf`**

    TLS_CACERT /etc/openldap/ca.crt

#### [Kerberos]

If OpenLDAP is compiled with [[[Kerberos]](https://packages.gentoo.org/useflags/Kerberos)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] (and [[[sasl]](https://packages.gentoo.org/useflags/sasl)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]) support, no configuration in OpenLDAP is needed for Kerberos. However, the server has to know where to find its keytab. It cannot use the system keytab because it has the wrong permissions. A special keytab must be created for OpenLDAP. An environmental variable, KRB5_KTNAME must be set in the server\'s context to find it. Extract the **ldap** principal for this server (ldap/FQDN@DOMAIN) and save in a keytab to a file called [/etc/openldap/krb5-ldap.keytab]. Set file ownership to the ldap user and group, and set permissions to 400.

##### [OpenRC]

Uncomment the KRB5_KTNAME line

[FILE] **`/etc/conf.d/slapd`(Excerpt)**

    # Specify the kerberos keytab file
    KRB5_KTNAME=/etc/openldap/krb5-ldap.keytab

##### [Systemd]

Edit [/etc/systemd/system/slapd.service.d/00gentoo.conf] and uncomment the KRB5_KTNAME line.

[FILE] **`/etc/systemd/system/slapd.service.d/00gentoo.conf`(Excerpt)**

    # Specify the kerberos keytab file
    Environment=KRB5_KTNAME=/etc/openldap/krb5-ldap.keytab

#### [Enforce encryption]

TLS and Kerberos allow the server to encrypt communications via the client though STARTTLS, but it do not mandate it. The LDAP server can be configure to force use of encryption:

Create this LDIF:

[FILE] **`enforce-encryption.ldif`**

    dn: cn=config
    changetype: modify
    add: olcLocalSSF
    olcLocalSSF: 128

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    replace: olcSecurity
    olcSecurity: update_ssf=128 simple_bind=1

The first rule for **olcLocalSSF** protects against locking out local access. The value must be at least are large as the largest value in olcSecurity. The example above requires encryption to update any entries, but only integrity protection to bind. This is only relevant for Kerberos: if the SSF is not 0, all TLS implementation will always encrypt (and most Kerberos ones will too).

Add the entries to the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f enforce-encryption.ldif`

** Warning**\
Do not specify **tls=1** in olcSecurity, otherwise, local users and non-TLS Kerberos users will be locked out

For increased flexibility, access control rules can be used in addition to, or instead of, mandating security via **olcSecurity**.

#### [Access Control]

Each database has it own access control. The default for the directory databases (like mdb) is to grant read to all, otherwise, the default is no access to anyone. See [Access Control via Dynamic Configuration](//www.openldap.org/doc/admin26/access-control.html#Access%20Control%20via%20Dynamic%20Configuration) for the syntax and examples.

An example access control configuration:

[FILE] **`access-control.ldif`**

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    replace: olcAccess
    olcAccess: to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external
     ,cn=auth" manage by * break
    olcAccess: to attrs=userPassword
      by ssf=128 self write
      by anonymous auth
      by * none
    olcAccess: to *
      by users read
      by * none

The above example allows local root to manage the database, requires encryption when updating the passwords, allows authenticated users read and denies everyone else access. Note the *by \* break* in the first rule OpenLDAP normally stops at the first matching rule, and if the entity isn\'t matched in that rule, access is denied without further evaluating any other rules - unless the break rule is specified.

#### [Limits]

For large directories, an LDAP query can take significant resources (time and bandwidth). Server-side limits on query can be enforced. See [Limits](https://www.openldap.org/doc/admin26/limits.html) for syntax and examples. There are version of the limit: *soft* and *hard*. The *soft* limit is the maximum resources used if the client doesn\'t specify a limit. This is works as a default value for clients. The *hard* limit is the maximum resources the client can request if they do specify a limit. Either or both may be specified in a limit rule. The 2 main resources that can be constrained by limits is *size* and *time*

An example limit configuration:

[FILE] **`limit-control.ldif`**

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    replace: olcLimits
    olcLimits: dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth"
      time.soft=unlimited time.hard=unlimited
      size.soft=unlimited size.hard=unlimited
    olcLimits: dn.exact="cn=replicator,dc=example,dc=com"
      time.soft=unlimited time.hard=unlimited
      size.soft=unlimited size.hard=unlimited
    olcLimits: users
      time=3600
      size=1000
    olcLimits: *
      time.soft=15 time.hard=60
      size.soft=10 size.hard=100

Thew above example gives the local root and replicator users no limits, both hard and soft limits of 3600 seconds and 1000 results per query, and everyone else (like anonymous users) gets a soft limit of 15 seconds and 10 results per query, and a hard limit of 60 seconds an 100 results per query.

#### [Remote RootDN access]

The quick start creates a RootDN that can access anything, however, the RootPW is not set, meaning the RootDN cannot login. The RootPW must be set to login:

[FILE] **`ldap-rootpw.ldif`**

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    add: olcRootPW
    # Use a better password than this!
    olcRootPW: secret

Add the entries to the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f ldap-rootpw.ldif`

When proper access has been set up, remove the root password:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL`

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    delete: olcRootPW

### [Replication]

LDAP uses a push/pull model for replication. The \"pusher\" is called the *producer* and the \"puller\" is called the *consumer*. A server can have both roles (servers that only consume would need to be read-only and forward writes via referrals). There are 2 sync protocols: syncrepl and delta-syncrepl. The former sends all attributes of a DN that has changed, the latter sends only the attributes of the DN that changed. delta-Syncrepl uses less traffic but requires more configuration.

The number of replication scenarios are limited only by the imagination. See [Replication](//www.openldap.org/doc/admin26/replication.html) in the documentation for some examples. Two will be covered here: Mirrors and Read-only replicas.

#### [Replication considerations]

The replication process requires a Bind DN and secret. The Bind DN must have read access to the entire database and not be subject to limits in order to complete its work. Also, unlike the userPassword attribute, the secret must be in the clear. Therefore, the use of TLS is critical.

So there\'s 3 options for replication authentication

1.  Use the RootDN
2.  Use a dedicated replication account
3.  Do something fancy with Kerberos/SASL

Option 1 is the easiest, but least secure.

For option 2, a dedicated replicator DN can created (Note the database need to be populated first: [#Populating the directory](#Populating_the_directory)):

[FILE] **`replicator.ldif.in`**

    dn: cn=replicator,$
    changetype: add
    objectClass: simpleSecurityObject
    objectClass: organizationalRole
    cn: replicator
    description: Replication user
    userPassword: x

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    replace: olcAccess
    olcAccess: to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external
     ,cn=auth" manage
      by dn.exact="cn=replicator,$" read
      by * break
    olcAccess: to attrs=userPassword
      by self write
      by anonymous auth
      by * none
    olcAccess: to *
      by * read
    -
    replace: olcLimits
    olcLimits: dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth"
      time.soft=unlimited time.hard=unlimited
      size.soft=unlimited size.hard=unlimited
    olcLimits: dn.exact="cn=replicator,$"
      time.soft=unlimited time.hard=unlimited
      size.soft=unlimited size.hard=unlimited

The above **olcAccess** rules assumes the quick start configuration is in use. If a different configuration is in use, make sure the **olcAccess** rule giving the replicator user read access is in the first rule, and don\'t forget the *by \* break* to continue evaluating the access control rules for other entities.

Use sed to fill in the blanks, replacing **dc=example,dc=com** with your directory component information.

`user `[`$`]`sed -e 's/$/dc=example,dc=com/g' < replicator.ldif.in > replicator.ldif`

Add it to the server

`root `[`#`]`ldapmodify -c -H ldapi:/// -Y EXTERNAL -f replicator.ldif`

Change the password (substitute your DC)

`root `[`#`]`ldappasswd -H ldapi:/// -Y EXTERNAL -S cn=replicator,dc=example,dc=com`

For option 3, this requires something like Kerberos (GSSAPI) or client certificates (TLS with EXTERNAL). This is the most difficult option. Figuring out how to set this up is a exercise for the reader.

#### [][Preparing the producer for delta-syncrepl (Optional)]

The producer OpenLDAP must have been built with the [[[overlays]](https://packages.gentoo.org/useflags/overlays)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag. The producer also needs the *accesslog* module loaded:

[FILE] **`mod-accesslog.ldif`**

    dn: cn=module,cn=config
    changetype: add
    objectClass: olcModuleList
    cn: module
    olcModulePath: /usr/lib64/openldap/openldap
    olcModuleLoad: accesslog.so

Add the entries to the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f mod-accesslog.ldif`

Create the directories for the access log and fix the owner:

`root `[`#`]`( umask 077 && mkdir /var/lib/openldap-data/accesslog ) `

`root `[`#`]`chown -R ldap:ldap /var/lib/openldap-data/accesslog`

Next, another database needs to be created, along with a syncrepl overlay for it. The accesslog over is also added to the main database:

[FILE] **`deltasync-producer.ldif`**

    dn: olcDatabase=mdb,cn=config
    changetype: add
    objectClass: olcDatabaseConfig
    objectClass: olcMdbConfig
    olcDatabase: mdb
    olcDbDirectory: /var/lib/openldap-data/accesslog
    olcSuffix: cn=accesslog
    olcDbIndex: default eq
    olcDbIndex: entryCSN,objectClass,reqEnd,reqResult,reqStart,reqDN
    olcAccess: to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external
     ,cn=auth" manage
    # Delete this comment and uncomment the next lines if a dedicated replicator account is in use
    #  by dn.exact="cn=replicator,dc=example,dc=com" read
    #olcLimits: dn.exact="cn=replicator,dc=example,dc=com"
    #  time.soft=unlimited time.hard=unlimited
    #  size.soft=unlimited size.hard=unlimited

    dn: olcOverlay=syncprov,olcDatabase=mdb,cn=config
    changetype: add
    objectClass: olcOverlayConfig
    objectClass: olcSyncProvConfig
    olcOverlay: syncprov
    olcSpNoPresent: TRUE
    olcSpReloadHint: TRUE

    dn: olcOverlay=accesslog,olcDatabase=mdb,cn=config
    changetype: add
    objectClass: olcOverlayConfig
    objectCLass: olcAccessLogConfig
    olcOverlay: accesslog
    olcAccessLogDB: cn=accesslog
    olcAccessLogOps: writes
    olcAccessLogSuccess: TRUE
    # Scan the data once a day and purge anything older than a week
    olcAccessLogPurge: 07+00:00 01+00:00

Add the entries to the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f deltasync-producer.ldif`

#### [Mirroring configuration]

Since each server is both a producer and consumer, the configuration is almost exactly the same for each.

First, the producer part. Configure the Server ID and an LDAP overlay:

[FILE] **`mirror-producer.ldif.in`**

    dn: cn=config
    changetype: modify
    add: olcServerID
    # An arbitrary, unique 3 digit hexadecimal value
    olcServerID: $ ldap://$

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    add: olcDbIndex
    olcDbIndex: entryCSN,entryUUID eq
    # If the quick start configuration wasn't used, this may be required too
    # olcDbIndex: objectClass eq

    dn: olcOverlay=syncprov,olcDatabase=mdb,cn=config
    changetype: add
    objectClass: olcOverlayConfig
    objectClass: olcSyncProvConfig
    olcOverlay: syncprov
    olcSpCheckpoint: 100 10
    olcSpSessionlog: 100

Use sed to fill in the blanks, substituting **001** with desired server ID, and **ldap1.example.com** with the producer\'s LDAP FQDN.

`user `[`$`]`sed -e 's/$/001/g' -e 's/$/ldap1.example.com/g' < mirror-producer.ldif.in > mirror-producer.ldif`

Add the entries to the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f mirror-producer.ldif`

Second, the consumer part. Configure replication:

[FILE] **`mirror-consumer.ldif.in`**

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    add: olcSyncrepl
    # The RID value is arbitrary
    olcSyncrepl: rid=001
      provider=ldap://$
      searchbase="$"
      bindmethod=simple
      binddn="cn=replicator,$"
      credentials=secret
      type=refreshAndPersist
      retry="60 +"
      starttls=critical
    # Delete this comment and uncomment out the next 2 lines if using delta-syncrepl
    #  logbase="cn=accesslog"
    #  logfilter="(&(objectClass=auditWriteObject)(reqResult=0))"
    -
    add: olcMultiProvider
    olcMultiProvider: TRUE

Use sed to fill in the blanks, replacing **dc=example,dc=com** with your directory component information, and **ldap.example.com** with the producer\'s LDAP FQDN.

`user `[`$`]`sed -e 's/$/ldap2.example.com/g' -e 's/$/dc=example,dc=com/g' < mirror-consumer.ldif.in > mirror-consumer.ldif`

If using delta-syncrepl, follow the instructions in the LDIF file. Also, substitute the values of **binddn** and **credentials** with the correct values. Load it onto the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f mirror-consumer.ldif`

Then repeat for the other server, choosing a new *olcServerID* and swapping the URLs for the producer and consumer.

It is possible to extend this to multiple mirrors, such a configuration is called \"[N-Way Multi-Provider Replication](//www.openldap.org/doc/admin26/replication.html#N-Way%20Multi-Provider%20Replication)\". Its basically the same as mirroring, except there\'s multiple **olcSyncrepl** entries - one of each other server.

#### [Read-only replicas configuration]

On the producer configure as follows:

[FILE] **`producer.ldif.in`**

    dn: cn=config
    changetype: modify
    add: olcServerID
    # An arbitrary, unique 3 digit hexadecimal value
    olcServerID: $ ldap://$

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    add: olcDbIndex
    olcDbIndex: entryCSN,entryUUID eq
    # If the quick start configuration wasn't used, this may be required too
    # olcDbIndex: objectClass eq

    dn: olcOverlay=syncprov,olcDatabase=mdb,cn=config
    changetype: add
    objectClass: olcOverlayConfig
    objectClass: olcSyncProvConfig
    olcOverlay: syncprov
    olcSpCheckpoint: 100 10
    olcSpSessionlog: 100

Use sed to fill in the blanks, substituting **001** with desired server ID, and **ldap1.example.com** with the producer\'s LDAP FQDN.

`user `[`$`]`sed -e 's/$/001/g' -e 's/$/ldap1.example.com/g' < producer.ldif.in > producer.ldif`

Add the entries to the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f producer.ldif`

On the consumers, configure as follows:

[FILE] **`consumer.ldif.in`**

    dn: olcDatabase=mdb,cn=config
    changetype: modify
    add: olcSyncrepl
    # The RID value is arbitrary
    olcSyncrepl: rid=001
      provider=ldap://$
      searchbase="$"
      bindmethod=simple
      binddn="cn=replicator,$"
      credentials=secret
      type=refreshAndPersist
      retry="60 +"
      starttls=critical
    # Delete this comment and uncomment out the next 2 lines if using delta-syncrepl
    #  logbase="cn=accesslog"
    #  logfilter="(&(objectClass=auditWriteObject)(reqResult=0))"
    -
    add: olcUpdateRef
    olcUpdateRef: ldap://$

Use sed to fill in the blanks, replacing **dc=example,dc=com** with your directory component information, and **ldap.example.com** with the producer\'s LDAP FQDN.

`user `[`$`]`sed -e 's/$/ldap.example.com/g' -e 's/$/dc=example,dc=com/g' < consumer.ldif.in > consumer.ldif`

If using delta-syncrepl, follow the instructions in the LDIF file. Also, substitute the values of binddn and credentials with the correct values. Load it onto the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f consumer.ldif`

This is almost the same as mirroring, but without the **olcMultiProvider** entry and with an added **olcUpdateRef** for the database.

## [Populating the directory]

Unless the server is a replication consumer of an already populated producer, the directory itself is still empty. The initial entry must be created or imported:

### [Populating the directory via creation]

[FILE] **`populate.ldif.in`**

    dn: $
    changetype: add
    objectClass: dcObject
    objectClass: organization
    o: TO FILLED IN BY LDAP ADMIN
    dc: $

    dn: cn=Manager,$
    changetype: add
    objectClass: organizationalRole
    cn: Manager

Use sed to fill in the blanks, replacing **dc=example,dc=com** with your directory component information and **example** with the first part of the domain name.

`user `[`$`]`sed -e 's/$/dc=example,dc=com/g' -e 's/$/example/g' < populate.ldif.in > populate.ldif`

Don\'t forget the change the value of the *o* attribute to something suitable (either the name of the organization, or the FQDN of the domain if nothing in particular is suitable). Load it onto the server:

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL -f populate.ldif`

Once the initial population is done, the directory can be loaded with data.

### [Populating the directory via import]

The old directory needs to be exported with all the internal attributes. For OpenLDAP, the **slapcat** command on the old server will produce a suitable output. Copy the LDIF file to the new server, shut down OpenLDAP if it\'s still running, and import the old database with **slapadd**. The database ownership will need to be updated:

`root `[`#`]`chown -R ldap:ldap /var/lib/openldap-data`

Then start up OpenLDAP.

## [Adminstration]

### [Backing up the database]

To backup the database, use **slapcat** on the main database (if delta-syncrepl is in use, backup the accesslog database as well). Typically this would be run by a cron jon or systemd timer. The backup should be considered sensitive.

### [Clearing all schemas]

Removing schemas is not a simple task. Slapd must be **offline** and the unwanted schemas must be removed with **slapmodify** using a *delete* operation. Sometimes OpenLDAP will refuse to do so. Because the config files should never be changed manually, the best way to continue is to delete all schemas and then re-add the desired ones. To do that, **slapcat** can be used to produce a filtered LDIF, then the LDIF manually edited to re-include the desired schemas.

With slapd **offline**, issue the following **slapcat** command:

`root `[`#`]`slapcat -n 0 -H 'ldap:///???(!(entryDN:dnSubtreeMatch:=cn=schema,cn=config))' > new_schemas.ldif`

Insert the following blocks after the first **cn=config** block

[FILE] **`new_schemas.ldif`(Insert after first *cn=config* block)**

    dn: cn=schema,cn=config
    objectClass: olcSchemaConfig
    cn: schema

    # Required. Note there should be a blank line before and after every include statement
    include: file:///etc/openldap/schema/core.ldif

    # Include schema dependencies first then the desired schema
    include: file:///etc/openldap/schema/cosine.ldif

    include: file:///etc/openldap/schema/nis.ldif

Backup the old directory, create a new empty config directory and add the new LDIF configuration:

`root `[`#`]`mv /etc/openldap/slapd.d/ /etc/openldap/slapd.d.old `

`root `[`#`]`( umask 077 && mkdir /etc/openldap/slapd.d ) `

`root `[`#`]`slapadd -n 0 -l new_schemas.ldif -F /etc/openldap/slapd.d `

`root `[`#`]`chown -R ldap:ldap /etc/openldap/slapd.d `

`root `[`#`]`slaptest `

`root `[`#`]`slapschema -n 2`

If **slaptest** fails be sure the file above was inserted in the to correct place and the required newlines are there. If **slapschema** fails, either add the missing schema. If the schema is to be decommsioned, the incompatible attributes will have to be removed from the directory. The server might not start until the problem is fixed; at the very least the DNs with attributes without a schema will be inaccessible.

### [Open file limits]

By default, processes are soft limited to 1024 descriptors, and hard limited to 4096 descriptors. If slapd starts showing the \"Too many open files\" message, the limit has been exceeded. Increasing the limit depends on the init system:

#### [OpenRC]

**start-stop-daemon** sets the limits for the process using the user listed in pam_limits. Either edit [/etc/security/pam_limits.conf] or add a file in the [/etc/security/limits.d] directory with the following lines, replacing **8192** with the desired value:

[FILE] **`/etc/security/pam_limits.conf`**

    ldap           soft    nofile          8192
    ldap           hard    nofile          8192

Slapd must be restarted for changes to take effect:

`root `[`#`]`rc-service slapd restart`

#### [Systemd]

Systemd itself controls the limits of service, and the limits can be increased by editing the config file. Append the following [/etc/systemd/system/slapd.service.d/00gentoo.conf], replacing **8192** with the desired value:

[FILE] **`/etc/security/pam_limits.conf`**

    [Service]
    LimitNOFILE=8192

Slapd must be restarted for changes to take effect:

`root `[`#`]`systemctl restart slapd`

## [Troubleshooting]

### [Turning up the log level]

To turn up the log level, change the value of **olcLogLevel**. The [admin guide](//www.openldap.org/doc/admin26/slapdconf2.html#cn=config) lists the possible values

`root `[`#`]`ldapmodify -H ldapi:/// -Y EXTERNAL`

    dn: cn=config
    changetype: modify
    replace: olcLogLevel
    olcLogLevel: 1023

Once the problem has been fixed. it can changed back to *768* using the above construction.

## [See also]

-   [OpenLDAP 2.6 Administrator\'s Guide](//www.openldap.org/doc/admin26/index.html)