Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/AIDE/de "AIDE (100% translated)")
-   [English]
-   [français](https://wiki.gentoo.org/wiki/AIDE/fr "AIDE (8% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/AIDE/it "AIDE (74% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/AIDE/hu "AIDE (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/AIDE/pl "AIDE (3% translated)")
-   [русский](https://wiki.gentoo.org/wiki/AIDE/ru "AIDE (38% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/AIDE/zh-cn "AIDE (59% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/AIDE/ja "AIDE (67% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/AIDE/ko "AIDE (74% translated)")

\
AIDE (***A**dvanced **I**ntrusion **D**etection **E**nvironment*) is a host-based intrusion detection system. AIDE scans files and other resources and stores information about these files in a database. Stored information includes key file attributes such as file hash output, file size, ownership, modification time, creation time, and more. After the initial database has been created, AIDE then rescans the system and compares new scan results with previously stored values. If values differ then the file has been changed and the change will be reported. The idea behind using AIDE is to create a snapshot of a system then compare the snapshot to another created snapshot to find compromised files.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Overview]](#Overview)
    -   [[2.2] [Detailed options]](#Detailed_options)
    -   [[2.3] [Initialization and frequent scanning]](#Initialization_and_frequent_scanning)
-   [[3] [Best practices]](#Best_practices)
    -   [[3.1] [Be clear on what to scan]](#Be_clear_on_what_to_scan)
    -   [[3.2] [Keep the database offline and read-only]](#Keep_the_database_offline_and_read-only)
    -   [[3.3] [Do offline scanning]](#Do_offline_scanning)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [[] Installation]

### [[] USE flags]

It is easy to install [[[app-forensics/aide]](https://packages.gentoo.org/packages/app-forensics/aide)[]] after setting the USE flags accordingly.

### [USE flags for] [app-forensics/aide](https://packages.gentoo.org/packages/app-forensics/aide) [[]] [AIDE (Advanced Intrusion Detection Environment) is a file integrity checker]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`acl`](https://packages.gentoo.org/useflags/acl)           Add support for Access Control Lists
  [`audit`](https://packages.gentoo.org/useflags/audit)       Enable support for Linux audit subsystem using sys-process/audit
  [`curl`](https://packages.gentoo.org/useflags/curl)         Use curl for http,https and ftp backends
  [`e2fs`](https://packages.gentoo.org/useflags/e2fs)         Enable support for checking file attributes on ext2/ext3/ext4 filesystems
  [`mhash`](https://packages.gentoo.org/useflags/mhash)       Add support for the mhash library
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`xattr`](https://packages.gentoo.org/useflags/xattr)       Add support for extended attributes (filesystem-stored metadata)
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-04 09:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

USE flag changes specific to a certain package should be defined in the [/etc/portage/package.use] file, or a text file inside a directory called [/etc/portage/package.use]. For example, when using a [/etc/portage/package.use] *file*:

[FILE] **`/etc/portage/package.use`Enable zlib support for AIDE**

    app-forensics/aide zlib

### [[] Emerge]

After the USE flags have been set, install the software:

`root `[`#`]`emerge --ask app-forensics/aide`

## [[] Configuration]

### [[] Overview]

The configuration file for [[[app-forensics/aide]](https://packages.gentoo.org/packages/app-forensics/aide)[]] is not as daunting as it might seem at first sight. The default file is stored at [/etc/aide/aide.conf] but administrators can easily create multiple configuration files if necessary. Besides a few variables, the configuration file contains short-hand notations for what aspects of files to scan for (only hashes, or also inode information, etc.) and which files to scan.

Take look at the database variables:

[FILE] **`aide.conf`AIDE database configuration variables**

    database=file:/var/lib/aide/aide.db
    database_out=file:/var/lib/aide/aide.db.new

The first line in the example above (`database`) defines where the location of database that contains the known values. The second line (`database_out`) defines where to store new databases when another is generated. It is generally recommended against having these variables point to the same database (having the same paths for each variable). If one database is to overwrite another, the best method is to *manually copy* over the generated database from one location to the other. For example, to overwrite the first database with the second, this command could be used:

`root `[`#`]`cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db`

For now, leave the database variables as they are; they will be covered in more detail later in the article.

Next, consider the variables which are short-hand notations for what information to record in the database.

[FILE] **`aide.conf`AIDE configuration using shorthand notation**

    Binlib = p+i+n+u+g+s+b+m+c+md5+sha1
    Logs = p+i+n+u+g+S
    ...

** Note**\
It should be obvious that `md5` and `sha1` mean that MD5 and SHA-1 checksums are taken (respectively).

The letters are described in the default [aide.conf] file, but for convenience the following table provides an overview of the most common options:

  ------- ---------------------------------------------------------------------------
  Short   Description
  `p`     Permissions
  `i`     inode number
  `n`     Number of (hard)links
  `u`     User information
  `g`     Group information
  `s`     Size
  `S`     Size (only report when the size is suddenly smaller - growing is allowed)
  `b`     Block count
  `m`     Modification time
  ------- ---------------------------------------------------------------------------

Next is an overview of which directories to scan, and what to scan for. In three line example to follow, AIDE is instructed to scan the [/bin] and [/sbin] directories via the measures identified in the `Binlib` short-hand notation variable. The [/var/log] file will display the scan measures defined in the `Logs` variable defined above.

[FILE] **`aide.conf`Scan target options**

    /bin Binlib
    /sbin Binlib
    /var/log Logs
    ...

AIDE supports regular expressions and users are allowed to \"remove\" matches. For instance, to scan [/var/log] but not [/var/log/portage] then make an exclusion set by using the `!` (exclamation point) before the excluded path(s):

[FILE] **`aide.conf`Other scan targets**

    /var/log Logs
    !/var/log/portage

### [[] Detailed options]

The configuration file is based on regular expressions, macros and rules for files and directories. Users experienced with the [tripwire solution](https://www.tripwire.org/) will have no difficulties dealing with AIDE\'s configuration file. The following macros are available:

  ----------- -------------------------------------------------------------------------- ---------------------------
  Macro       Description                                                                Syntax
  `ifdef`     If defined                                                                 `@@ifdef "name"`
  `ifndef`    If not defined                                                             `@@ifndef "name"`
  `define`    Define a variable                                                          `@@define "name" "value"`
  `undef`     Undefine a variable                                                        `@@undef "name"`
  `ifhost`    if \"hostname\"                                                            `@@ifhost "hostname"`
  `ifnhost`   if not \"hostname\"                                                        `@@ifnhost "hostname"`
  `endif`     Endif must be used after any of the above macros except define and undef   `@@endif`
  ----------- -------------------------------------------------------------------------- ---------------------------

These macros become very handy when dealing with multiple Gentoo boxes, while using the same configuration on all. Not all machines run the same services or even have the same users.

Next we have a set of flags which identify the permissions, file properties, checksums, cryptographic hashes, \... to validate on files and directories.

  ---------- -------------------------------
  Flag       Description
  `p`        permissions
  `i`        inode
  `n`        number of links
  `u`        user
  `g`        group
  `s`        size
  `b`        block count
  `m`        mtime
  `a`        atime
  `c`        ctime
  `S`        check for growing size
  `md5`      md5 checksum
  `sha1`     sha1 checksum
  `rmd160`   rmd160 checksum
  `tiger`    tiger checksum
  `R`        `p+i+n+u+g+s+m+c+md5`
  `L`        `p+i+n+u+g`
  `E`        Empty group
  `>`        Growing logfile `p+u+g+i+n+S`
  ---------- -------------------------------

If AIDE is compiled with mhash support, then the following flags can be used as well:

  --------- ----------------
  Flag      Description
  `haval`   haval checksum
  `gost`    gost checksum
  `crc32`   crc32 checksum
  --------- ----------------

### [[] Initialization and frequent scanning]

For a basic AIDE setup, a database must be initialized. This is performed using the `--init` option. To make sure AIDE uses the configuration settings defined in the sections before, be sure to pass the `--config` option pointed to the correct configuration file:

`root `[`#`]`aide --init --config=/etc/aide/aide.conf`

    AIDE, version 0.14.2

    ### AIDE database at /var/lib/aide/aide.db.new initialized.

Once initialized, any pre-existing database files can be copied over:

`root `[`#`]`cd /var/lib/aide; cp aide.db.new aide.db`

With a new database available, the entries can be scanned again (now or at a later date) using the `--check` option. This will create another database containing any modifications that have made to the file system since the first database has been created. Be sure to use the `--config` option pointed to the same configuration file that the first database was created with:

`root `[`#`]`aide --check --config=/etc/aide/aide.conf`

    AIDE, version 0.14.2

    ### All files match AIDE database. Looks okay!

If file modification(s) occurred, a notification will be sent out, if no initial database exists at all a warning will be presented such as:

`root `[`#`]`aide --init --config=/etc/aide/aide.conf`

    Couldn't open file /var/lib/aide/aide.db.new for writing

This is not a real error and is simply aide stating it cannot find a database so it must create one, this may take several minutes.

`root `[`#`]`aide --check --config=/etc/aide/aide.conf`

    AIDE found differences between database and filesystem!!
    Start timestamp: 2013-04-11 15:31:02

    Summary:
      Total number of files:        318
      Added files:                  0
      Removed files:                0
      Changed files:                2

    ---------------------------------------------------
    Changed files:
    ---------------------------------------------------

    changed: /etc/pam.d
    changed: /etc/pam.d/run_init

    ---------------------------------------------------
    Detailed information about changes:
    ---------------------------------------------------

    Directory: /etc/pam.d
      Mtime    : 2013-04-09 22:11:18              , 2013-04-11 15:31:01
      Ctime    : 2013-04-09 22:11:18              , 2013-04-11 15:31:01

    File: /etc/pam.d/run_init
      Size     : 205                              , 208
      Mtime    : 2013-04-09 22:11:18              , 2013-04-11 15:31:00
      Ctime    : 2013-04-09 22:11:18              , 2013-04-11 15:31:01
      Inode    : 394203                           , 394053
      MD5      : Mm0KPzpPt63eqGClTJ/KaQ==         , eLUrP2BsIq25f3AZX+dlBA==
      SHA1     : NrQtsUeOsXS4RHUq+ejYBne5V6E=     , 5A6ef6VJCcMiqEjKQ7e9xkBNZB8=

## [[] Best practices]

### [[] Be clear on what to scan]

The default AIDE configuration is useful, but it needs to be fine-tuned to suit the users\' needs. It is important to know which files to scan and why.

For instance, to scan for all authentication-related files but not for other files, use a configuration like so:

[FILE] **`aide.conf`authentication-related scan targets**

    # SELinux policy and settings
    /etc/selinux ConfFiles
    # Authentication databases
    /etc/passwd ConfFiles
    /etc/shadow ConfFiles
    /etc/nsswitch.conf ConfFiles
    # Authentication configuration
    /etc/pam.d ConfFiles
    /etc/securetty ConfFiles
    /etc/security ConfFiles
    # PAM libraries
    /lib(64)?/security Binlib

### [[] Keep the database offline and read-only]

A second important aspect is that the result database should be stored offline when *not* needed and should be used in read-only mode when the database *is* needed. This gives some protection against a malicious user that might have compromised the machine to modify the results database. For instance, provide the result database on a read-only NFS mount (for servers) or read-only medium (when physical access to the machine is possible) such as a CD/DVD or a read-only USB drive.

After storing the database on a read-only location, update the [aide.conf] file to have `database` point to this new location.

### [[] Do offline scanning]

If applicable, try using offline scanning methods for the system. In case of virtual platforms, it might be possible to take a snapshot of the system, mount this snapshot (read-only) and then run the aide scan on the mounted file system.

`root `[`#`]`losetup /dev/loop0 /srv/virt/gentoo.img `

`root `[`#`]`vgscan `

`root `[`#`]`vgchange -ay `

`root `[`#`]`mount -o ro /dev/volgrpX/volumeY /mnt/image `

`root `[`#`]`chroot /mnt/image `

`root `[`#`]`aide --check --config=/path/to/aide.conf `

`root `[`#`]`exit `

`root `[`#`]`umount /mnt/image `

`root `[`#`]`vgchange -an /dev/volgrpX `

`root `[`#`]`losetup -d /dev/loop0`

The above approach uses [chroot]. This is only needed when the initial file system has been scanned from the live system and the administrator wants to perform an offline validation. If the initial scan was done offline, then the [aide.conf] file will point to the mount point already and the database will use these paths immediately, so then there is no need for chrooting.

## [[] See also]

-   [Integrity/Concepts](https://wiki.gentoo.org/wiki/Integrity/Concepts "Integrity/Concepts") talks about the concepts related to system integrity

## [[] External resources]

-   [Tutorial on how to use AIDE (Linux.com)](https://archive09.linux.com/articles/113919)
-   [Securing Linux with AIDE article (Symantec.com)](https://www.symantec.com/connect/articles/securing-linux-aide)