[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=FreeRADIUS&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.freeradius.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/FreeRADIUS "wikipedia:FreeRADIUS")

[[]][Official documentation](https://freeradius.org/documentation/)

[[]][[#freeradius](ircs://irc.libera.chat/#freeradius)] ([[webchat](https://web.libera.chat/#freeradius)])

**FreeRADIUS** is an implementation of the Remote Authentication Dial-In User Service (RADIUS) protocol.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Certificates]](#Certificates)
        -   [[2.1.1] [Certificate Authority Certificate]](#Certificate_Authority_Certificate)
        -   [[2.1.2] [Server Certificate]](#Server_Certificate)
    -   [[2.2] [EAP]](#EAP)
    -   [[2.3] [Service]](#Service)
-   [[3] [Troubleshooting]](#Troubleshooting)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-dialup/freeradius](https://packages.gentoo.org/packages/net-dialup/freeradius) [[]] [Highly configurable free RADIUS server]

  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`iodbc`](https://packages.gentoo.org/useflags/iodbc)           Add support for iODBC library
  [`kafka`](https://packages.gentoo.org/useflags/kafka)           Include support for kafka
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)     Add kerberos support
  [`ldap`](https://packages.gentoo.org/useflags/ldap)             Add LDAP support (Lightweight Directory Access Protocol)
  [`memcached`](https://packages.gentoo.org/useflags/memcached)   Include dev-libs/libmemcached in caching drivers
  [`mongodb`](https://packages.gentoo.org/useflags/mongodb)       Include support for MongoDB database
  [`mysql`](https://packages.gentoo.org/useflags/mysql)           Add mySQL Database support
  [`odbc`](https://packages.gentoo.org/useflags/odbc)             Add ODBC Support (Open DataBase Connectivity)
  [`oracle`](https://packages.gentoo.org/useflags/oracle)         Enable Oracle Database support
  [`pam`](https://packages.gentoo.org/useflags/pam)               Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`postgres`](https://packages.gentoo.org/useflags/postgres)     Add support for the postgresql database
  [`python`](https://packages.gentoo.org/useflags/python)         Add optional support/bindings for the Python language
  [`readline`](https://packages.gentoo.org/useflags/readline)     Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`redis`](https://packages.gentoo.org/useflags/redis)           Include support for Redis database
  [`samba`](https://packages.gentoo.org/useflags/samba)           Add support for SAMBA (Windows File and Printer sharing)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)       !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)         Add support for sqlite - embedded sql database
  [`ssl`](https://packages.gentoo.org/useflags/ssl)               Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)       Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`yubikey`](https://packages.gentoo.org/useflags/yubikey)       Include support for ubikey
  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-18 14:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install FreeRADIUS:

`root `[`#`]`emerge --ask net-dialup/freeradius`

## [Configuration]

Configuration files are located in [/etc/raddb/] directory.

** See also**\
For general configuration visit the [Basic configuration HOWTO](https://wiki.freeradius.org/guide/Basic-configuration-HOWTO).

### [Certificates]

Before it can be used, FreeRadius needs certificates for EAP.

** See also**\
[/etc/raddb/certs/README.md]

#### [Certificate Authority Certificate]

If a CA does not already exist, FreeRadius can generate a CA cert using configuration in [/etc/raddb/certs/ca.cnf]:

[FILE] **`/etc/raddb/certs/ca.cnf`**

    ...
    [ CA_default ]
    default_days            = 1000
    ...

    [ req ]
    prompt                  = no
    distinguished_name      = certificate_authority
    default_bits            = 2048
    input_password          = !!somesecurepassword!!
    output_password         = !!anothersecurepassword!!
    x509_extensions         = v3_ca

    [certificate_authority]
    countryName             = US
    stateOrProvinceName     = Radius
    localityName            = Wiki
    organizationName        = example
    emailAddress            = larry@example.com
    commonName              = "Example RADIUS cert for gentoo wiki"

** Important**\
Be sure to configure the **input_password** and **output_password**, used to secure key files.

Once configured, the CA cert can be generated by running:

`root `[`#`]`make ca.pem`

    openssl req -new -x509 -keyout ca.key -out ca.pem \
        -days '1000' -config ./ca.cnf \
        -passin pass:'!!somesecurepassword!!' -passout pass:'!!anothersecurepassword!!'
    ........+..+....+.....+.+....................+.+.....+++++++++++++++++++++++++++++++++++++++*...+............+....+...+...........+....+...+..+.+++++++++++++++++++++++++++++++++++++++*.+......+....+...+........+....+..+......+.........+.........+.........+............+.........+.+.....+....+......+........+.......+...........+...+....+...+..+.+......+.....+...+...+............+.+.........+......+...........+..........+.....+.+.....+..................+......+...+............+...................+......+...+......+.....+.........+......+....+..+..........+......+.....+.........+.+..+.+.........+......+......+.........+..+...+.........+.+......+...............+.....+...+...+....+...+..+.+.....+...+.........+.+..............+.+..+...+....+....................+............+......+....+..............+.+.....+.+.....+.......+..+....+.........+..+...+...+............+...+..........+........+......+....+..+.........+.+........+.......++++++
    ....+..............+...+......+.......+...+++++++++++++++++++++++++++++++++++++++*..+...+..........+.....+.+.....+...+...+...+++++++++++++++++++++++++++++++++++++++*........+......+.....+.........+.......+..+...+....+......+........+......+.+.....+.........+.+.........+........+......+.......+..+.......+.....+...+...............+...+.........+.+.........+.....+...............+....+...........+................+..+.+.........+..+....+...........+..........+........+...+..........+...............+.........+.........+............+...+..+........................+.+..+......+......+.............+......+.....+.......+.....+.......+......+..+...+....+...+.....+.......+.....+.......+......+........+......+...+..........+......+.....+.........+................+.........+...........+.+......+..+......+.......+............+..+......+..........++++++
    -----
    chmod g+r ca.key

#### [Server Certificate]

To create a server certificate signed by the previously generated CA:

[FILE] **`/etc/raddb/certs/server.cnf`**

    ...
    [ CA_default ]
    default_days            = 100
    ...

    [ req ]
    prompt                  = no
    distinguished_name      = certificate_authority
    default_bits            = 2048
    input_password          = !!somesecurepassword!!
    output_password         = !!anothersecurepassword!!
    x509_extensions         = v3_ca

    [server]
    countryName             = US
    stateOrProvinceName     = Radius
    localityName            = Wiki
    organizationName        = example
    emailAddress            = larry@example.com
    commonName              = "Example RADIUS Server cert for gentoo wiki"

** Tip**\
The maximum expiry which can be used for FreeRadius server certificates is **825** days.

** Important**\
Be sure to configure the **input_password** and **output_password**, used to secure key files. CA keys will be read from [ca.cnf].

Once configured, the server cert can be generated by running:

`root `[`#`]`make server`

    openssl req -new  -out server.csr -keyout server.key -config ./server.cnf
    ........+...+......+..........+...........+....+...+...+..+.+.....+......+.+++++++++++++++++++++++++++++++++++++++*..+...+..............+.........+....+..+.+...+..+....+.....+++++++++++++++++++++++++++++++++++++++*............+........+.............+..+...+.+...+...+........+......+.+...+...........+....+.........+..+.+........++++++
    .........+.+......+...+......+.........+...+...+..+...+......+.+++++++++++++++++++++++++++++++++++++++*.+...+.......+..+...+...+.......+...+.........+..+++++++++++++++++++++++++++++++++++++++*...+.+.....+...+..........+.........+...............+............+...+......+...........+.++++++
    -----
    chmod g+r server.key
    openssl ca -batch -keyfile ca.key -cert ca.pem -in server.csr  -key '!!anothersecurepassword!!' -out server.crt -extensions xpserver_ext -extfile xpextensions -config ./server.cnf
    Using configuration from ./server.cnf
    Check that the request matches the signature
    Signature ok
    Certificate Details:
            Serial Number: 1 (0x1)
            Validity
                Not Before: Nov 14 13:17:14 2024 GMT
                Not After : Feb 22 13:17:14 2025 GMT
            Subject:
                countryName               = US
                stateOrProvinceName       = Radius
                organizationName          = Wiki
                commonName                = Example RADIUS Server cert for gentoo wiki
                emailAddress              = larry@example.com
            X509v3 extensions:
                X509v3 Extended Key Usage:
                    TLS Web Server Authentication
                X509v3 CRL Distribution Points:
                    Full Name:
                      URI:http://www.example.com/example_ca.crl
                X509v3 Certificate Policies:
                    Policy: 1.3.6.1.4.1.40808.1.3.2
    Certificate is to be certified until Feb 22 13:17:14 2025 GMT (100 days)

    Write out database with 1 new entries
    Database updated
    openssl pkcs12 -export -in server.crt -inkey server.key -out server.p12  -passin pass:'!!anothersecurepassword!!' -passout pass:'!!anothersecurepassword!!'
    chmod g+r server.p12
    openssl pkcs12 -in server.p12 -out server.pem -passin pass:'!!anothersecurepassword!!' -passout pass:'!!anothersecurepassword!!'
    chmod g+r server.pem
    server.pem: OK

### [EAP]

With a server certificate created, the EAP module must be configured:

[FILE] **`/etc/raddb/mods-enabled/eap`**

    eap
    }

### [Service]

To start FreeRADIUS:

`root `[`#`]`rc-service radiusd start`

To add FreeRADIUS to the default runlevel:

`root `[`#`]`rc-update add radiusd default`

## [Troubleshooting]

[FreeRADIUS general Troubleshooting guide](https://wiki.freeradius.org/guide/Troubleshooting)

## [See also]

-   [Tac plus](https://wiki.gentoo.org/wiki/Tac_plus "Tac plus") --- a AAA protocol which provides access control for user Authentication, a protocol for AAA services (Authentication, Authorization, Accounting) similar to RADIUS.

## [External resources]

-   [FreeRADIUS - HOWTO](https://wiki.freeradius.org/guide/HOWTO)
-   [FreeRADIUS - FAQ](https://wiki.freeradius.org/guide/FAQ)
-   [FreeRADIUS - Dialup Admin Web Administration](https://wiki.freeradius.org/guide/Dialup%20admin)
-   [FreeRADIUS - TACACS+ Virtual Server Setup](https://www.freeradius.org/documentation/freeradius-server/4.0.0/reference/raddb/sites-available/tacacs.html)