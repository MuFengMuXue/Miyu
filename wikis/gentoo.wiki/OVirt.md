[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://www.ovirt.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/OVirt "wikipedia:OVirt")

**oVirt** is a complete open sourced virtualization management platform working with [KVM](https://wiki.gentoo.org/wiki/QEMU "QEMU"). The project is made of:

-   The **Engine core**, which is the backend server that does the management.
-   The various **VDSM agents** installed on each host you \'ll use as a hypervisor for VMs
-   A **client side UI** (GWT based) and/or **RESTful API** to control the engine core.

## Contents

-   [[1] [ovirt-engine]](#ovirt-engine)
    -   [[1.1] [Preparations]](#Preparations)
        -   [[1.1.1] [PostgreSQL]](#PostgreSQL)
        -   [[1.1.2] [Database]](#Database)
-   [[2] [Installation]](#Installation)
-   [[3] [Post configuration]](#Post_configuration)
    -   [[3.1] [Apache]](#Apache)
    -   [[3.2] [Testing]](#Testing)
-   [[4] [Install vdsm]](#Install_vdsm)
-   [[5] [How to contribute]](#How_to_contribute)
-   [[6] [Advanced features]](#Advanced_features)
    -   [[6.1] [oVirt Node integration]](#oVirt_Node_integration)
    -   [[6.2] [Troubleshooting JBoss (obsolete)]](#Troubleshooting_JBoss_.28obsolete.29)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [ovirt-engine]

### [Preparations]

#### [PostgreSQL]

-   Install PostgreSQL server:

`root `[`#`]`emerge --ask dev-db/postgresql`

** Note**\
Please ensure that the `server` USE flag is enabled.

-   Configure PostgreSQL server:

`root `[`#`]`emerge --config dev-db/postgresql`

-   Allow network access:

[FILE] **`/etc/postgres-*/pg_hba.conf`**

    host    all             all             127.0.0.1/32            password
    host    all             all             ::1/128                 password

-   Start:

`root `[`#`]`/etc/init.d/postgres* start`

#### [Database]

-   Create user and database for engine:

`root `[`#`]`su - postgres -c "psql -d template1"`

    template1=# create user engine password 'engine';
    template1=# create database engine owner engine template template0
        encoding 'UTF8' lc_collate 'en_US.UTF-8' lc_ctype 'en_US.UTF-8';

-   OPTIONAL: Create user and database for dwh:

`root `[`#`]`su - postgres -c "psql -d template1"`

    template1=# create user ovirt_engine_history password 'ovirt_engine_history';
    template1=# create database ovirt_engine_history owner ovirt_engine_history template template0
        encoding 'UTF8' lc_collate 'en_US.UTF-8' lc_ctype 'en_US.UTF-8';

-   OPTIONAL: Create user and database for reports:

`root `[`#`]`su - postgres -c "psql -d template1"`

    template1=# create user ovirt_engine_reports password 'ovirt_engine_reports';
    template1=# create database ovirt_engine_reports owner ovirt_engine_reports template template0
        encoding 'UTF8' lc_collate 'en_US.UTF-8' lc_ctype 'en_US.UTF-8';

## [Installation]

Portage overlay exists here: [http://github.com/alonbl/ovirt-overlay](https://github.com/alonbl/ovirt-overlay)

Add the overlay, creating [/etc/portage/repos.conf/ovirt-overlay.conf]:

[FILE] **`/etc/portage/repos.conf/ovirt-overlay.conf`oVirt overlay**

    [ovirt-overlay]
    location = /usr/local/portage/ovirt-overlay
    sync-type = git
    sync-uri = https://github.com/alonbl/ovirt-overlay

This can be done automatically with [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]]:

`root `[`#`]`eselect repository add ovirt-overlay git `[`https://github.com/alonbl/ovirt-overlay.git`](https://github.com/alonbl/ovirt-overlay.git)

Sync the repository:

`root `[`#`]`emerge --sync ovirt-overlay`

Install ovirt-engine:

`root `[`#`]`emerge --ask app-emulation/ovirt-engine`

** Note**\
Before reporting any issue, please try to build with `USE="-system-jars"`.

You may need to add unstable keywords to various packages.

OPTIONAL: Emerge ovirt-engine-dwh and/or ovirt-engine-reports:

`root `[`#`]`emerge --ask app-emulation/ovirt-engine-dwh app-emulation/ovirt-engine-reports`

Configure ovirt-engine:

`root `[`#`]`emerge --config app-emulation/ovirt-engine`

Follow instructions.

## [Post configuration]

#### [Apache]

-   Enable mod_proxy, add after APACHE2_OPTS=\"XXX\":

[FILE] **`/etc/conf.d/apache2`**

    APACHE2_OPTS="$ -D PROXY"

-   Restart:

`root `[`#`]`/etc/init.d/apache2 restart`

### [Testing]

Login into [http://localhost/ovirt-engine](http://localhost/ovirt-engine)

Logs are at [/var/log/ovirt-engine]

## [Install vdsm]

** Warning**\
VDSM for now is mostly Fedora/Redhat oriented, trying to set up VDSM on a non-Fedora node takes more than you think. If you succeed however please update this part of the article and notify upstream. Until then I suggest you use an oVirt-node image for your Hypervisors from here [\[1\]](https://ovirt.org/releases/stable/binary/)

-   Install dev-python/pyflakes as it is needed by vdsm:

`root `[`#`]`emerge --ask dev-python/pyflakes`

-   Obtain VDSM source RPM:

`user `[`$`]`wget -c `[`http://fsimonce.fedorapeople.org/vdsm/fedora-16/SRPMS/vdsm-4.9.0-0.200.g2fc4e63.fc16.src.rpm`](https://fsimonce.fedorapeople.org/vdsm/fedora-16/SRPMS/vdsm-4.9.0-0.200.g2fc4e63.fc16.src.rpm)

-   Convert rpm package to tgz:

`user `[`$`]`rpm2tgz vdsm-4.9.0-0.200.g2fc4e63.fc16.src.rpm`

-   Unpack the archive:

`user `[`$`]`tar zxvf vdsm-4.9.0-0.200.g2fc4e63.fc16.src.tgz`

-   Enter the directory and do the configure-make-make install magic (Recommended to use `–prefix` when compiling from source so you can have all files under one directory per package):

`root `[`#`]`cd vdsm-4.9.0-0.200.g2fc4e63.fc16 `

`root `[`#`]`./configure --prefix=/path/to/install/directory && make && make install `

## [How to contribute]

-   oVirt project is working with Gerrit code review for code contribution.
-   In order to register and login to oVirt\'s Gerrit, you\'ll need an OpenID account.
    -   You can use a Google OpenID, or register to some other provider and use it,
-   All other details can be found here: [http://www.ovirt.org/wiki/Working_with_oVirt_Gerrit](https://www.ovirt.org/wiki/Working_with_oVirt_Gerrit)

## [Advanced features]

### [oVirt Node integration]

-   By default development setup works with hosts based on base distro\'s installations.
-   In order to be able to work with oVirt Node (which is a sub-set of the base OS), you\'ll need to setup a Public Key environment.
-   More details on Engine and oVirt Node integration can be found here: [http://www.ovirt.org/wiki/Engine_Node_Integration](https://www.ovirt.org/wiki/Engine_Node_Integration).
    -   Note that by default Gentoo does not have [/etc/pki] folder, and you\'ll need to create it (or write an ebuild which will do that).

### [][Troubleshooting JBoss (obsolete)]

If you\'re being attacked by exceptions, follow this list:

-   Verify jboss folder owner and permissions.
-   If your machine has an SELinux policy installed, make sure it will not block JBoss. Here is a very dirty and insecure jboss.te just to temporarily pass these denials (you\'ll also need selinux-java)

[CODE] **jboss.te**

    module jboss 1.0;

    require ;
            class fd use;
            class capability dac_override;
            class file;
            class dir ;
    }

    #============= java_t ==============
    allow java_t newrole_t:fd use;
    allow java_t bin_t:file ;
    allow java_t self:capability dac_override;
    allow java_t sysfs_t:dir ;
    allow java_t user_tmp_t:dir ;
    allow java_t user_home_dir_t:dir search;
    allow java_t user_tmp_t:file ;
    allow java_t usr_t:dir ;
    allow java_t usr_t:file ;
    allow java_t port_t:tcp_socket name_bind;
    allow java_t self:tcp_socket ;
    allow java_t node_t:tcp_socket node_bind;

-   Used TCP ports: 8702/8083/1090/4457
    -   Since JBoss binds to the hostname, your hostname should be resolvable, or you may add it to [/etc/hosts] for local resolution.

<!-- -->

    127.0.0.1 localhost engine-dev

## [See also]

-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.

## [External resources]

-   [Additional information (including presentations)](https://www.ovirt.org/wiki/Workshop_November_2011)
-   Users list: users@ovirt.org