## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Design]](#Design)
-   [[3] [Packages]](#Packages)
-   [[4] [Database Initialization]](#Database_Initialization)
-   [[5] [Setup Mariadb and Galera]](#Setup_Mariadb_and_Galera)
    -   [[5.1] [Node01]](#Node01)
    -   [[5.2] [Node02]](#Node02)
    -   [[5.3] [Node03]](#Node03)
    -   [[5.4] [Start mariadb on the first node]](#Start_mariadb_on_the_first_node)
    -   [[5.5] [Start mariadb on other nodes]](#Start_mariadb_on_other_nodes)
    -   [[5.6] [Checking if all nodes have joined and are running correctly]](#Checking_if_all_nodes_have_joined_and_are_running_correctly)
    -   [[5.7] [Garbd Arbitrator Configuration]](#Garbd_Arbitrator_Configuration)
-   [[6] [Finalize configuration]](#Finalize_configuration)
    -   [[6.1] [Start mariadb on boot]](#Start_mariadb_on_boot)
-   [[7] [Secure mariadb]](#Secure_mariadb)
-   [[8] [External Reference]](#External_Reference)

# [Introduction]

This is a guide for configuring a 3 node MariaDB Galera Cluster.\
A MariaDB Galera cluster requires a minimal of 3 nodes. However, one of the members of the cluster can be an arbitrator (2 node + 1 arbitrator). Despite not participating in data replication, the arbitrator still needs to be on a 3rd physical node.\
^[\[1\]](#cite_note-arbitrator-1)^

# [Design]

The Maria Galera Cluster is multi master cluster featuring synchronous writes across all nodes. Each node requires a static IP address to function.

If you have a local dns server, you can make use of that. else make use of your hosts file. This will make your system clear about the other nodes and ip address.

[FILE] **`/etc/hosts`add you hostname if you don\'t have it**

    127.0.0.1   localhost
    192.168.10.11   node01
    192.168.10.12   node02
    192.168.10.13   node03

^[\[2\]](#cite_note-2nodeMariaDB-2)^ ^[\[3\]](#cite_note-galeracluster.com-3)^

# [Packages]

Add the galera useflag to MariaDB:

[FILE] **`/etc/portage/package.use`enable galera replication support**

    dev-db/mariadb galera

Add the garbd useflag (only) on the arbitrator. If you have 3 nodes you can skip this useflag.

[FILE] **`/etc/portage/package.use`add this extra useflag**

    sys-cluster/galera garbd

Then, emerge the following packages:

`root `[`#`]`emerge --ask dev-db/mariadb sys-cluster/galera`

### [USE flags for] [dev-db/mariadb](https://packages.gentoo.org/packages/dev-db/mariadb) [[]] [An enhanced, drop-in replacement for MySQL]

  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+backup`](https://packages.gentoo.org/useflags/+backup)                   Build mariadb-backup which supports SST and hot backup of InnoDB, Aria and MyISAM including compression and encryption
  [`+perl`](https://packages.gentoo.org/useflags/+perl)                       Add optional support/bindings for the Perl language
  [`+server`](https://packages.gentoo.org/useflags/+server)                   Build the server program
  [`aws-km`](https://packages.gentoo.org/useflags/aws-km)                     Add support for using the AWS Key Management plugin
  [`bindist`](https://packages.gentoo.org/useflags/bindist)                   Flag to enable or disable options for prebuilt (GRP) packages (eg. due to licensing issues)
  [`columnstore`](https://packages.gentoo.org/useflags/columnstore)           Build the ColumnStore storage engine
  [`cracklib`](https://packages.gentoo.org/useflags/cracklib)                 Support for cracklib strong password checking
  [`debug`](https://packages.gentoo.org/useflags/debug)                       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`extraengine`](https://packages.gentoo.org/useflags/extraengine)           Add support for alternative storage engines (Archive, CSV, Blackhole, Federated(X), Partition)
  [`galera`](https://packages.gentoo.org/useflags/galera)                     Enables galera replication
  [`innodb-lz4`](https://packages.gentoo.org/useflags/innodb-lz4)             Enables lz4 compression methods for InnoDB/XtraDB
  [`innodb-lzo`](https://packages.gentoo.org/useflags/innodb-lzo)             Enables lzo compression methods for InnoDB/XtraDB
  [`innodb-snappy`](https://packages.gentoo.org/useflags/innodb-snappy)       Enables snappy compression methods for InnoDB/XtraDB using app-arch/snappy
  [`jdbc`](https://packages.gentoo.org/useflags/jdbc)                         Enable the CONNECT engine to access foreign databases via JDBC
  [`jemalloc`](https://packages.gentoo.org/useflags/jemalloc)                 Use dev-libs/jemalloc for memory management
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)                 Add kerberos support
  [`latin1`](https://packages.gentoo.org/useflags/latin1)                     Use LATIN1 encoding instead of UTF8
  [`mroonga`](https://packages.gentoo.org/useflags/mroonga)                   Add support for the Mroonga engine for interfacing with the Groonga text search
  [`numa`](https://packages.gentoo.org/useflags/numa)                         Enable NUMA support using sys-process/numactl (NUMA kernel support is also required)
  [`odbc`](https://packages.gentoo.org/useflags/odbc)                         Add ODBC Support (Open DataBase Connectivity)
  [`oqgraph`](https://packages.gentoo.org/useflags/oqgraph)                   Add support for the Open Query GRAPH engine
  [`pam`](https://packages.gentoo.org/useflags/pam)                           Enable the optional PAM authentication plugin for the server
  [`profiling`](https://packages.gentoo.org/useflags/profiling)               Add support for statement profiling (requires USE=community).
  [`rocksdb`](https://packages.gentoo.org/useflags/rocksdb)                   Add support for RocksDB; a key/value, LSM database optimized for flash storage
  [`s3`](https://packages.gentoo.org/useflags/s3)                             Build the S3 storage engine
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sphinx`](https://packages.gentoo.org/useflags/sphinx)                     Add suport for the sphinx full-text search engine
  [`sst-mariabackup`](https://packages.gentoo.org/useflags/sst-mariabackup)   Add tools needed to support the mariabackup SST method
  [`sst-rsync`](https://packages.gentoo.org/useflags/sst-rsync)               Add tools needed to support the rsync SST method
  [`static`](https://packages.gentoo.org/useflags/static)                     !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                   Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`systemtap`](https://packages.gentoo.org/useflags/systemtap)               Build support for profiling and tracing using dev-debug/systemtap
  [`tcmalloc`](https://packages.gentoo.org/useflags/tcmalloc)                 Use the dev-util/google-perftools libraries to replace the malloc() implementation with a possibly faster one
  [`test`](https://packages.gentoo.org/useflags/test)                         Install upstream testsuites for end use.
  [`xml`](https://packages.gentoo.org/useflags/xml)                           Add support for XML files
  [`yassl`](https://packages.gentoo.org/useflags/yassl)                       Enable SSL connections and crypto functions using the bundled yaSSL
  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-07 19:06] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [sys-cluster/galera](https://packages.gentoo.org/packages/sys-cluster/galera) [[]] [Synchronous multi-master replication engine that provides the wsrep API]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------
  [`garbd`](https://packages.gentoo.org/useflags/garbd)   Install Galera Arbitrator - a stateless daemon which acts as a lightweight group member
  [`ssl`](https://packages.gentoo.org/useflags/ssl)       Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  ------------------------------------------------------- -----------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-04 05:39] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

# [Database Initialization]

Run this command and keyin your mariadb root password

`root `[`#`]`emerge --config dev-db/mariadb`

    Configuring pkg...

     * Please provide a password for the mysql 'root' user now
     * or through the /root/.my.cnf file.
     * Avoid ["'\_%] characters in the password
        >
     * Retype the password
        >
     * Creating the mysql database and setting proper
     * permissions on it ...
     * Command: '/usr/share/mysql/scripts/mysql_install_db'                                                                                                                                  [ ok ]
     * Setting root password ...                                                                                                                                           [ ok ]
     * Loading "zoneinfo", this step may require a few seconds ... ...                                                                                                     [ ok ]
     * Stopping the server ...
     * Done

# [Setup Mariadb and Galera]

## [Node01]

[FILE] **`/etc/mysql/my.cnf`Make the change below**

    # Listen on (IPv4) all interfaces
    bind-address                            = 0.0.0.0

    # unique per-node id, greater than 0
    server-id = 1

    wsrep_on
    wsrep_provider=/usr/lib/galera/libgalera_smm.so

    # You should change this name to something meaningful
    wsrep_cluster_name="my_mariadb_cluster"

    # List all nodes of the cluster including this one
    wsrep_cluster_address="gcomm://192.168.10.11,192.168.10.12,192.168.10.13"

    # We will come back to change this again later
    wsrep_sst_method=rsync

    # Galera Node Configuration
    wsrep_node_address="192.168.10.11"
    wsrep_node_name="node01"

## [Node02]

[FILE] **`/etc/mysql/my.cnf`Make the change below**

    # Listen on (IPv4) all interfaces
    bind-address                            = 0.0.0.0

    # unique per-node id, greater than 0
    server-id = 2

    wsrep_on
    wsrep_provider=/usr/lib/galera/libgalera_smm.so

    # You should change this name to something meaningful
    wsrep_cluster_name="my_mariadb_cluster"

    # List all nodes of the cluster including this one
    wsrep_cluster_address="gcomm://192.168.10.11,192.168.10.12,192.168.10.13"

    # We will come back to change this again later
    wsrep_sst_method=rsync

    # Galera Node Configuration
    wsrep_node_address="192.168.10.12"
    wsrep_node_name="node02"

## [Node03]

[FILE] **`/etc/mysql/my.cnf`Make the change below**

    # Listen on (IPv4) all interfaces
    bind-address                            = 0.0.0.0

    # unique per-node id, greater than 0
    server-id = 3

    wsrep_on
    wsrep_provider=/usr/lib/galera/libgalera_smm.so

    # You should change this name to something meaningful
    wsrep_cluster_name="my_mariadb_cluster"

    # List all nodes of the cluster including this one
    wsrep_cluster_address="gcomm://192.168.10.11,192.168.10.12,192.168.10.13"

    # We will come back to change this again later
    wsrep_sst_method=rsync

    # Galera Node Configuration
    wsrep_node_address="192.168.10.13"
    wsrep_node_name="node03"

## [Start mariadb on the first node]

When a node starts, by default it assumes that the cluster is already initialised and tries to join it. If no node is initialised, the cluster will not be able to start since all nodes will just try to join a (non) existing cluster. Therefore, the first node in the cluster to be online needs to be instructed to become a \"new\" cluster (read into [STARTING THE FIRST CLUSTER NODE](http://galeracluster.com/documentation-webpages/startingcluster.html#starting-the-first-cluster-node) for more defaults):

`root `[`#`]`/etc/init.d/mysql bootstrap_galera`

\

## [Start mariadb on other nodes]

`root `[`#`]`/etc/init.d/mysql start`

## [Checking if all nodes have joined and are running correctly]

Try to run this command on node 1:

`root `[`#`]`mysql -u root -p`

    Enter password:
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 1102
    Server version: 10.1.29-MariaDB Source distribution

    Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]> SHOW STATUS LIKE 'wsrep%';
    # Focus on the 2 values below.
    | wsrep_cluster_size           | 3                                     |
    | wsrep_ready                  | ON                                    |

If the cluster size is equal to you node size you are good to go. And wsrep_ready meant the cluster is ON.

## [Garbd Arbitrator Configuration]

** Note**\
This is still a physical 3 node, just not running mariadb.

** Warning**\
While the Galera Arbitrator does not participate in replication, it does receive the same data as all other nodes. You must secure its network connection.^[\[1\]](#cite_note-arbitrator-1)^

** Warning**\
Unless this has been fixed in your installation, [garbd does not work when specifying cluster address without the port](https://bugs.launchpad.net/percona-xtradb-cluster/+bug/1365193). Make sure to include the port numbers as shown below.

[FILE] **`/etc/conf.d/garbd`Make the change below**

    # A space-separated list of node addresses (address[:port]) in the cluster
    GALERA_NODES="192.168.0.10:4567 192.168.0.11:4567"

    # Galera cluster name, should be the same as on the rest of the nodes.
    GALERA_GROUP="my_mariadb_cluster"

** Note**\
Not idea why, but cannot turn on Log or it will not start

`root `[`#`]`/etc/init.d/garbd start`

# [Finalize configuration]

The Mariadb cluster should now be up.

## [Start mariadb on boot]

For openrc, do:

`root `[`#`]`rc-update add mysql default`

     * service mysql added to runlevel default

# [Secure mariadb]

Secure your mariadb for production use

`root `[`#`]`mysql_secure_installation`

# [External Reference]

1.  [[↑ ^[1.0](#cite_ref-arbitrator_1-0)^ ^[1.1](#cite_ref-arbitrator_1-1)^] [[\[1\]](http://galeracluster.com/documentation-webpages/arbitrator.html)[http://galeracluster.com/documentation-webpages/arbitrator.html](http://galeracluster.com/documentation-webpages/arbitrator.html)]]
2.  [[[↑](#cite_ref-2nodeMariaDB_2-0)] [[\[2\]](http://www.sebastien-han.fr/blog/2012/04/01/mysql-multi-master-replication-with-galera/)[http://www.sebastien-han.fr/blog/2012/04/01/mysql-multi-master-replication-with-galera/](http://www.sebastien-han.fr/blog/2012/04/01/mysql-multi-master-replication-with-galera/)]]
3.  [[[↑](#cite_ref-galeracluster.com_3-0)] [[\[3\]](http://galeracluster.com/documentation-webpages/?id=galera_deployment)[http://galeracluster.com/documentation-webpages/?id=galera_deployment](http://galeracluster.com/documentation-webpages/?id=galera_deployment)]]