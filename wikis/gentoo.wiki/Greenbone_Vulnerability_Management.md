**Resources**

[[]][Home (Greenbone)](https://www.greenbone.net/en/)

[[]][Home (OpenVAS)](https://www.openvas.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-analyzer/gvm)

[[]][Wikipedia](https://en.wikipedia.org/wiki/OpenVAS "wikipedia:OpenVAS")

[[]][GitHub](https://github.com/greenbone/openvas)

[[]][Greenbone Community Edition -- Documentation](https://greenbone.github.io/docs/latest/index.html)

**G**reenbone **V**ulnerability **M**anagement (GVM) is a network security scanner with associated tools like a graphical user front-end. The core component is a server with a set of network vulnerability tests (NVTs) to detect security problems in remote systems and applications. It is used by both offensive and defensive security experts to determine attack surfaces.

GVM was previously known as **O**pen **V**ulnerability **A**ssessment **S**ystem (OpenVAS). OpenVAS was a fork of Nessus, the popular corporate security scanner maintained by [Tenable](https://www.tenable.com). Both OpenVAS and Nessus were originally built from the [nmap](https://wiki.gentoo.org/wiki/Nmap "Nmap") port scanner.

This guide provides instructions on installing a complete server solution for vulnerability scanning and vulnerability management.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Redis]](#Redis)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [systemd]](#systemd)
    -   [[2.2] [PostgreSQL backend]](#PostgreSQL_backend)
    -   [[2.3] [Sync the Greenbone Community Feed]](#Sync_the_Greenbone_Community_Feed)
    -   [[2.4] [gvmd certificate generation]](#gvmd_certificate_generation)
-   [[3] [Starting Greenbone daemons]](#Starting_Greenbone_daemons)
    -   [[3.1] [Notus Scanner]](#Notus_Scanner)
        -   [[3.1.1] [OpenRC]](#OpenRC_2)
        -   [[3.1.2] [systemd]](#systemd_2)
    -   [[3.2] [OpenVAS Scanner]](#OpenVAS_Scanner)
        -   [[3.2.1] [OpenRC]](#OpenRC_3)
        -   [[3.2.2] [systemd]](#systemd_3)
    -   [[3.3] [Greenbone Vulnerability Manager (gvmd)]](#Greenbone_Vulnerability_Manager_.28gvmd.29)
        -   [[3.3.1] [OpenRC]](#OpenRC_4)
        -   [[3.3.2] [systemd]](#systemd_4)
    -   [[3.4] [Set the Feed Import Owner]](#Set_the_Feed_Import_Owner)
    -   [[3.5] [Greenbone Vulnerability Assistant WebUI (gsad)]](#Greenbone_Vulnerability_Assistant_WebUI_.28gsad.29)
        -   [[3.5.1] [OpenRC]](#OpenRC_5)
        -   [[3.5.2] [systemd]](#systemd_5)
-   [[4] [Misc]](#Misc)
    -   [[4.1] [Updating gvmd version]](#Updating_gvmd_version)
        -   [[4.1.1] [Migrating the database]](#Migrating_the_database)
    -   [[4.2] [Configure trusted NVTs]](#Configure_trusted_NVTs)
        -   [[4.2.1] [Create key]](#Create_key)
        -   [[4.2.2] [Add a certificate to OpenVAS Scanner keyring]](#Add_a_certificate_to_OpenVAS_Scanner_keyring)
        -   [[4.2.3] [Set trust]](#Set_trust)
    -   [[4.3] [Fixing collation version mismatch]](#Fixing_collation_version_mismatch)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [See Also]](#See_Also)

## [Installation]

[[[net-analyzer/gvm]](https://packages.gentoo.org/packages/net-analyzer/gvm)[]] is the resolver package of core GVM components and has several USE flags that may be desired for certain bigger setups. As this article aims at installing and configuring a *basic* GVM setup.

### [USE flags]

### [USE flags for] [net-analyzer/gvm](https://packages.gentoo.org/packages/net-analyzer/gvm) [[]] [Greenbone Vulnerability Management, previously named OpenVAS]

  --------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`+gsa`](https://packages.gentoo.org/useflags/+gsa)       Greenbone Security Assistant (WebUI)
  [`cli`](https://packages.gentoo.org/useflags/cli)         Command Line Interface for OpenVAS Scanner
  [`doc`](https://packages.gentoo.org/useflags/doc)         Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`ldap`](https://packages.gentoo.org/useflags/ldap)       Add LDAP support (Lightweight Directory Access Protocol)
  [`ospd`](https://packages.gentoo.org/useflags/ospd)       Enable support for scanner wrappers
  [`radius`](https://packages.gentoo.org/useflags/radius)   Add support for RADIUS authentication
  [`snmp`](https://packages.gentoo.org/useflags/snmp)       Add support for the Simple Network Management Protocol if available
  --------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-03 22:11] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

The [[[net-analyzer/gvm]](https://packages.gentoo.org/packages/net-analyzer/gvm)[]] is a meta-package in essence. You should install the last available version (22.4 at time of writing). It depends upon the command-line interface, libraries, manager, scanner, and tools. Do not be surprised if the dependency list is a little long:

`root `[`#`]`emerge --ask net-analyzer/gvm`

[[[net-analyzer/gvm]](https://packages.gentoo.org/packages/net-analyzer/gvm)[]] emerges the following packages: [[[net-analyzer/gvm-libs]](https://packages.gentoo.org/packages/net-analyzer/gvm-libs)[]], [[[net-analyzer/gvmd]](https://packages.gentoo.org/packages/net-analyzer/gvmd)[]], [[[net-analyzer/openvas-scanner]](https://packages.gentoo.org/packages/net-analyzer/openvas-scanner)[]], [[[net-analyzer/greenbone-feed-sync]](https://packages.gentoo.org/packages/net-analyzer/greenbone-feed-sync)[]], [[[dev-db/pg-gvm]](https://packages.gentoo.org/packages/dev-db/pg-gvm)[]], [[[dev-libs/paho-mqtt-c]](https://packages.gentoo.org/packages/dev-libs/paho-mqtt-c)[]].

To perform a complete installation add these use flags to [[[net-analyzer/gvm]](https://packages.gentoo.org/packages/net-analyzer/gvm)[]] : **+cli, +gsa, +ospd**. This will install: [[[net-analyzer/gvm-tools]](https://packages.gentoo.org/packages/net-analyzer/gvm-tools)[]], [[[net-analyzer/gsad]](https://packages.gentoo.org/packages/net-analyzer/gsad)[]] (that will require [[[net-analyzer/gsa]](https://packages.gentoo.org/packages/net-analyzer/gsa)[]]), [[[net-analyzer/ospd-openvas]](https://packages.gentoo.org/packages/net-analyzer/ospd-openvas)[]] (that will require [[[net-analyzer/notus-scanner]](https://packages.gentoo.org/packages/net-analyzer/notus-scanner)[]]).

### [Additional software]

Additional support for extra scanning checks can be gained from emerging the following software:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                 Description
  [net-analyzer/nmap](https://packages.gentoo.org/packages/net-analyzer/nmap)                                                                                                                                                                                                                                                                             For nmap --- to add port scanning and service detection based on nmap
  [[[net-analyzer/ike-scan]](https://packages.gentoo.org/packages/net-analyzer/ike-scan)[]]   For ike-scan --- an IPsec VPN scanning, fingerprinting and testing tool.
  [[[net-analyzer/nikto]](https://packages.gentoo.org/packages/net-analyzer/nikto)[]]            For Nikto --- a web server scanning and testing tool.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------

## [Configuration]

### [Redis]

Openvas-scanner relies on Redis, which is an in-memory data structure storage system. Redis should be configured to listen to a socket.

Starting with openvas-scanner-22.7.2 a separate redis instance is configured for GVM by gentoo portage. The configuration file is /etc/gvm/redis-openvas.conf

If you need, you can edit /etc/gvm/redis-openvas.conf or stay with default settings.

[FILE] **`/etc/gvm/redis-openvas.conf`**

    unixsocket /run/redis-openvas/redis.sock
    unixsocketperm 770
    port 0

Note that this configuration will only allow the \'redis\' user and users in \'redis\' group to access the socket. We will later fix that by setting a filesystem ACL on the socket, allowing the \'gvm\' user, i.e., the user OpenVAS runs under, to access it.

Then enable and start the redis service:

#### [OpenRC]

`root `[`#`]`rc-update add redis-openvas default`

`root `[`#`]`rc-service redis-openvas start`

#### [systemd]

Note that the systemd service of Redis may require setting RuntimeDirectory=redis so that /run/redis, under which the socket configured, is created.

`root `[`#`]`systemctl enable --now redis-openvas.service`

Starting from gvm-22.4 a gvm.target is created to start all gvm related services. We will illustrate this later.

### [PostgreSQL backend]

Keep in mind that GVM is run under user and group \'gvm\'. So create a database-user named \'gvm\' and database named \'gvmd\'.

To run psql, PostgreSQL has to be running. Refer to the [PostgreSQL/QuickStart](https://wiki.gentoo.org/wiki/PostgreSQL/QuickStart "PostgreSQL/QuickStart") and to the section [PostgreSQL/QuickStart#Starting the server](https://wiki.gentoo.org/wiki/PostgreSQL/QuickStart#Starting_the_server "PostgreSQL/QuickStart")

`root `[`#`]`sudo -u postgres psql`

[CODE] **PostgreSQL setup**

    create database gvmd;
    create role dba with superuser noinherit;
    create user gvm;
    grant all privileges on database gvmd to gvm;
    grant dba to gvm;
    \q

Note the last command, where we grant the \'gvm\' user the \'dba\' role, which is essentially \'superuser\', the highest privileged role of postgres. This means that the \'gvm\' user has access to all database in postgres. You may do not want to use the postgres database with other applications besides GVM due to this. The \'dba\' role is required, as it is used, and hence expected by gvmd to install GVM-specific postgres plugins.

Workaround for **PostgreSQL version 15** (released [October, 2022](https://www.postgresql.org/docs/current/release-15.html#id-1.11.6.6.4)), give the gvm user permission to modify the public schema:

`root `[`#`]`sudo -u postgres psql`

[CODE] **If using PostgreSQL 15 or higher**

    postgres=# \c gvmd
    You are now connected to database "gvmd" as user "postgres".
    gvmd=# grant ALL on SCHEMA public TO gvm;
    GRANT
    gvmd=# \q

gvm-22.4 requires a pgsql extension to be installed in the gvmd database. This extension contains functionality for ical object manipulation and it is provided by dev-db/pg-gvm.

To use the extension in a database create the extension using: CREATE EXTENSION \"pg-gvm\";

`root `[`#`]`sudo -u postgres psql gvmd`

[CODE] **CREATE EXTENSION \"pg-gvm\"**

    gvmd=>   CREATE EXTENSION "pg-gvm";
    gvmd=>   \q

### [Sync the Greenbone Community Feed]

Upgrade the Greenbone Community Feed data:

** Note**\
Verify RSYNC (TCP/873) has been enabled without NAT and Proxy to greenbone IPv6/IPv4 feed server \[feed.community.greenbone.net\]. SSH port 24 or 443 is only supported through the GSF (Paying Greenbone Customer) service level. Troubleshoot by checking the firewall for active connections. Due note systems sharing an external IP address many encounter issues, since one feed-sync per IP is the limit for the GCF. This can be verified by telneting to the Port 873 to test communication.

`user `[`$`]`sudo -u gvm greenbone-feed-sync`

To download only a specific feed content the `--type` argument can be used

`user `[`$`]`sudo -u gvm greenbone-feed-sync --type nvt`

Possible values for the \--type argument are: `all`, `nvt`/`nvts`, `gvmd-data`, `scap`, `cert`, `notus`, `nasl`, `report-format`/`report-formats`, `scan-config`/`scan-configs` or `port-list`/`port-lists`. Default value: `all`

** Warning**\
The greenbone-feed-sync must be executed as the **gvm** user.

### [gvmd certificate generation]

Now, generate the certificate for gvmd.

The certificate infrastructure enables GVM daemons to communicate in a secure manner and is used for authentication and authorization before establishing TLS connections between the daemons.

Setup the certificate automatically by running:

`user `[`$`]`sudo -u gvm gvm-manage-certs -a`

## [Starting Greenbone daemons]

After redis configuration and GVM feed rsync tasks are completed, the daemons will need to be started in the following order.

-   notus-scanner -\> ospd-openvas \> gvmd \> gsad
-   ospd-openvas will start redis-openvas and mosquitto.

\
If your system uses [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]], you can use the **gvm.target** to start all services at once:

`root `[`#`]`systemctl start gvm.target`

### [Notus Scanner]

#### [OpenRC]

`root `[`#`]`rc-service notus-scanner start`

`root `[`#`]`rc-update add notus-scanner default`

#### [systemd]

`root `[`#`]`systemctl enable --now ospd-openvas.service`

For validating the feed content, a GnuPG keychain with the *Greenbone Community Feed integrity key* needs to be created.

`user `[`$`]`curl -f -L `[`https://www.greenbone.net/GBCommunitySigningKey.asc`](https://www.greenbone.net/GBCommunitySigningKey.asc)` -o /tmp/GBCommunitySigningKey.asc`

`user `[`$`]`export GNUPGHOME=/tmp/openvas-gnupg`

`user `[`$`]`mkdir -p $GNUPGHOME`

`user `[`$`]`gpg --import /tmp/GBCommunitySigningKey.asc`

`user `[`$`]`echo "8AE4BE429B60A59B311C2E739823FAA60ED1E580:6:" | gpg --import-ownertrust`

`user `[`$`]`export OPENVAS_GNUPG_HOME=/etc/openvas/gnupg`

`user `[`$`]`sudo mkdir -p $OPENVAS_GNUPG_HOME`

`user `[`$`]`sudo cp -r /tmp/openvas-gnupg/* $OPENVAS_GNUPG_HOME/`

`user `[`$`]`sudo chown -R gvm:gvm $OPENVAS_GNUPG_HOME`

To enable feed validation, you can edit /etc/gvm/notus-scanner.toml and set the variable disable-hashsum-verification = **false**

[FILE] **`/etc/gvm/notus-scanner.toml`notus-scanner.toml**

    [notus-scanner]
    mqtt-broker-address = "localhost"
    mqtt-broker-port = "1883"
    products-directory = "/var/lib/notus/products"
    pid-file = "/run/notus-scanner/notus-scanner.pid"
    log-file = "/var/log/gvm/notus-scanner.log"
    log-level = "INFO"
    disable-hashsum-verification = false

### [OpenVAS Scanner]

With ospd-openvas-22.5.1.ebuild a custom override for the service is provided in **/etc/systemd/system/ospd-openvas.service.d/00gentoo.conf**

You can edit this file if you need to customize ospd-openvas service.

The service uses **/etc/gvm/ospd-openvas.conf** as ospd-openvas conf file.

Start OSDP OpenVAS scanner daemon:

#### [OpenRC]

`root `[`#`]`rc-service ospd-openvas start`

`root `[`#`]`rc-update add ospd-openvas default`

#### [systemd]

`root `[`#`]`systemctl enable --now ospd-openvas.service`

This will take a while, since OpenVAS here is loading all NVT definition downloaded. Check the status of openvas that completed loading NVTs before starting gvmd:

`root `[`#`]`ps aux | grep openvas`

    /usr/sbin/redis-server unixsocket:/run/redis-openvas/redis.sock
    /usr/bin/python3.11 /usr/lib/python-exec/python3.11/ospd-openvas --config /etc/gvm/ospd-openvas.conf --log-config /etc/gvm/ospd-logging.conf --lock-file-dir /var/lib/openvas --socket-mode 0o770 --mqtt-broker-address localhost --mqtt-broker-port 1883 --notus-feed-dir /var/lib/notus/advisories
    openvas: openvas: Reloaded 70200 of 86149 NVTs (81% / ETA: 00:08)
    ...

### [][Greenbone Vulnerability Manager (gvmd)]

Start Greenbone Vulnerability Manager daemon:

#### [OpenRC]

`root `[`#`]`rc-service gvmd start`

`root `[`#`]`rc-update add gvmd default`

#### [systemd]

`root `[`#`]`systemctl enable --now gvmd.service`

This will take a while, since \'gvmd\' here is rebuilding his database with all NVT definition downloaded. You will see with \`\`\`ps aux\`\`\` the gvmd process in \"Syncing SCAP\" state. Don\'t worry, after a while gvmd will load scapdata. This is normal to take long time.

Create a new user with Admin role, and take note of the generated password under user gvm:

`root `[`#`]`sudo -u gvm bash`

`user `[`$`]`gvmd --create-user=admin --role=Admin`

    User created with password '18664575-7101-4ceb-8a94-429a376824e6

** Tip**\
To change the password, substitute `MyNewVeryStrongPassword` with a new password:

`user `[`$`]`gvmd --user=admin --new-password=MyNewVeryStrongPassword `

### [Set the Feed Import Owner]

Now obtain the UUID of the created admin user via

`user `[`$`]`gvmd --get-users --verbose`

and set it [as feed owner](https://github.com/greenbone/gvmd/blob/main/INSTALL.md#set-the-feed-import-owner)

`user `[`$`]`gvmd --modify-setting 78eceaec-3385-11ea-b237-28d24461215b --value <uuid_of_user>`

### [][Greenbone Vulnerability Assistant WebUI (gsad)]

Greenbone Security Assistant (GSA) WebUI listens port 9392 default on localhost. If you wish you can configure Greenbone Security Assistant (GSAD) to listen to other interfaces rather than localhost only, so it is reachable from other hosts.

[FILE] **`/etc/conf.d/gsad`OpenRC**

    GSAD_LISTEN_ADDRESS="--listen=0.0.0.0"

[FILE] **`/etc/gvm/sysconfig/gsad-daemon.conf`systemd**

    GSAD_LISTEN_ADDRESS="--listen=0.0.0.0"

Or, in one shot:

[CODE] **OpenRC**

    sed -i -e "s/127\.0\.0\.1/0\.0\.0\.0/g" /etc/conf.d/gsad

[CODE] **systemd**

    sed -i -e "s/127\.0\.0\.1/0\.0\.0\.0/g" /etc/gvm/sysconfig/gsad-daemon.conf

** Tip**\
If you prefer reverse proxying with NGINX check out the following file: [/etc/openvas/gsa.nginx.reverse.proxy.example].

Start greenbone vulnerability assistant daemon:

#### [OpenRC]

`root `[`#`]`rc-service gsad start`

`root `[`#`]`rc-update add gsad default`

#### [systemd]

`root `[`#`]`systemctl enable --now gsad.service`

Open the browser at the IP address or domain name where GSAD is running, on port 9392, and login with the credentials previously created.

Happy vulnerability assessment!

## [Misc]

### [Updating gvmd version]

#### [Migrating the database]

When updating to a previous gvmd version you need to migrate the database to the new version or gvmd would not start.

if this is the case you can migrate the database issuing the following commands:

`root `[`#`]`mkdir /run/gvmd`

`root `[`#`]`setfacl -m u:gvm:rwx /run/gvmd/`

`root `[`#`]`sudo -u gvm gvmd --migrate`

### [Configure trusted NVTs]

** Note**\
This section is left here to avoid broken links. The same information are reported under Notus_Scanner section

Sum-up: [https://community.greenbone.net/t/gcf-managing-the-digital-signatures/101](https://community.greenbone.net/t/gcf-managing-the-digital-signatures/101) :

[Trusted NVTs]

\

    "Signed NVTs are usually provided by NVT Feed Services. For example, the NVTs contained in the OpenVAS NVT Feed are signed by the "OpenVAS Transfer Integrity" key which you can find at the bottom of this page. If you have already installed OpenVAS, you can use the "greenbone-nvt-sync" command to synchronize your NVT collection with the OpenVAS NVT Feed and receive signatures for all NVTs."

For updated instrucions, refer to: [https://greenbone.github.io/docs/latest/22.4/source-build/index.html#feed-validation](https://greenbone.github.io/docs/latest/22.4/source-build/index.html#feed-validation)

#### [Create key]

You need to choose Realname, Email and a Password. Example:

`root `[`#`]`gpg --homedir=/etc/openvas/gnupg --gen-key`

    Realname: openvas
    Email: openvas@localhost
    Password: admin

#### [Add a certificate to OpenVAS Scanner keyring]

Add the OpenVAS scanner Integrity Key:

`root `[`#`]`wget https://www.greenbone.net/GBCommunitySigningKey.asc `

`root `[`#`]`gpg --homedir=/etc/openvas/gnupg --import GBCommunitySigningKey.asc `

#### [Set trust]

To mark a certificate as trusted for your purpose, you have to sign it. The preferred way is to use local signatures that remain only in the keyring of your OpenVAS Scanner installation.

To finally sign a certificate you need to know its KEY_ID. You either get it from the table at the bottom or via a \"list-keys\" command.

Then you can locally sign:

`root `[`#`]`gpg --homedir=/etc/openvas/gnupg --list-keys `

`root `[`#`]`gpg --homedir=/etc/openvas/gnupg --lsign-key KEY_ID `

For example, to express your trust in the OpenVAS Transfer Integrity you imported above, you could use the following command:

`root `[`#`]`gpg --homedir=/etc/openvas/gnupg --lsign-key 0ED1E580`

Before signing you should be absolutely sure that you are signing the correct certificate. You may use its fingerprint and other methods to convince yourself.

To enable NVT signing on openvassd:

[CODE] **enable NVT signing**

    sed -i -e "s/disable-hashsum-verification*/disable-hashsum-verification = false/g" /etc/gvm/notus-scanner.toml

As last step, restart openvas service:

`root `[`#`]`rc-service ospd-openvas restart`

### [Fixing collation version mismatch]

After a postgres update it is possible that the database will issue a warning as

[CODE]

    The database was created using collation version 2.40, but the operating system provides version 2.41.

This warning is described in PostgreSQL\'s manual under [ALTER COLLATION](https://www.postgresql.org/docs/current/sql-altercollation.html#SQL-ALTERCOLLATION-NOTES) where is reported:

    When a collation object is created, the provider-specific version of the collation is recorded in the system catalog. When the collation is used, the current version is checked against the recorded version, and a warning is issued when there is a mismatch [...]
    A change in collation definitions can lead to corrupt indexes and other problems because the database system relies on stored objects having a certain sort order. Generally, this should be avoided, but it can happen in legitimate circumstances, such as when upgrading the operating system to a new major version or when using pg_upgrade to upgrade to server binaries linked with a newer version of ICU. When this happens, all objects depending on the collation should be rebuilt, for example, using REINDEX. When that is done, the collation version can be refreshed using the command ALTER COLLATION ... REFRESH VERSION. This will update the system catalog to record the current collation version and will make the warning go away. Note that this does not actually check whether all affected objects have been rebuilt correctly.

To do this, log into postgres:

`root `[`#`]`sudo -u postgres psql `

then, connect to the gvmd database:

`postgres=#`}}; user-select: none; font-weight: bold;"}`\c gvmd`

reindex the database:

`gvmd=#`}}; user-select: none; font-weight: bold;"}`REINDEX DATABASE gvmd;`

refresh the collation version:

`gvmd=#`}}; user-select: none; font-weight: bold;"}`ALTER DATABASE gvmd REFRESH COLLATION VERSION;`

exit postgres prompt:

`gvmd=#`}}; user-select: none; font-weight: bold;"}`\q`

## [Troubleshooting]

If you encounter a problem on fresh installation , first stop greenbone daemons (notus-scanner, ospd-openvas, gvmd and gsad) and clear redis cache:

`root `[`#`]`redis-cli -s /var/run/redis-openvas/redis.sock FLUSHDB`

`root `[`#`]`redis-cli -s /var/run/redis-openvas/redis.sock FLUSHALL`

Clean pre-generated NVTs and database;

`root `[`#`]`rm -rf /var/lib/gvm/*`

Then follow the instructions again.

## [See Also]

-   [Building 22.4 from Source](https://greenbone.github.io/docs/latest/22.4/source-build/index.html) - A comprehensive guide to build and configure GVM from sources.
-   [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL") --- a free and open source relational database management system (RDBMS).
-   [Nmap](https://wiki.gentoo.org/wiki/Nmap "Nmap") --- an open source recon tool used to check for open ports, what is running on those ports, and metadata about the daemons servicing those ports.
-   [Security Handbook](https://wiki.gentoo.org/wiki/Security_Handbook "Security Handbook") --- valuable guidance on Gentoo Linux security and cybersecurity in general.