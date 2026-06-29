# smb.conf Parameters / misc

### `add share command`

Section: misc; Context: G; Type: string

Samba 2.2.0 introduced the ability to dynamically add and delete shares via the Windows NT 4.0 Server Manager. The add share command is used to define an external program or script which will add a new service definition to smb.conf . In order to successfully execute the add share command , smbd requires that the administrator connects using a root account (i.e. uid == 0) or has the SeDiskOperatorPrivilege . Scripts defined in the add share command parameter are executed as root. When executed, smbd will automatically invoke the add share command with five parameters. configFile - the location of the global smb.conf file. shareName - the name of the new share. pathName - path to an **existing** directory on disk. comment - comment string to associate with the new share. max connections Number of maximum simultaneous connections to this share. This parameter is only used to add file shares. To add printer shares, see the .

### `afs share`

Section: misc; Context: S; Type: boolean; Default: `no`

This parameter controls whether special AFS features are enabled for this share. If enabled, it assumes that the directory exported via the path parameter is a local AFS import. The special AFS features include the attempt to hand-craft an AFS token if you enabled --with-fake-kaserver in configure.

### `afs token lifetime`

Section: misc; Context: G; Type: integer; Default: `604800`

This parameter controls the lifetime of tokens that the AFS fake-kaserver claims. In reality these never expire but this lifetime controls when the afs client will forget the token. Set this parameter to 0 to get NEVERDATE .

### `afs username map`

Section: misc; Context: G; Type: string

If you are using the fake kaserver AFS feature, you might want to hand-craft the usernames you are creating tokens for. For example this is necessary if you have users from several domain in your AFS Protection Database. One possible scheme to code users as DOMAIN+User as it is done by winbind with the + as a separator. The mapped user name must contain the cell name to log into, so without setting this parameter there will be no token.

### `allow insecure wide links`

Section: misc; Context: G; Type: boolean; Default: `no`

In normal operation the option which allows the server to follow symlinks outside of a share path is automatically disabled when are enabled on a Samba server. This is done for security purposes to prevent UNIX clients creating symlinks to areas of the server file system that the administrator does not wish to export. Setting to true disables the link between these two parameters, removing this protection and allowing a site to configure the server to follow symlinks (by setting to "true") even when is turned on. It is not recommended to enable this option unless you fully understand the implications of allowing the server to follow symbolic links created by UNIX clients. For most normal Samba configurations this would be considered a security hole and setting this parameter is not recommended. This option was added at the request of sites who had deliberately set Samba up in this way and needed to continue supporting this functionality without having to patch the Samba code.

### `allow unsafe cluster upgrade`

Section: misc; Context: G; Type: boolean; Default: `no`

If set to no (the default), smbd checks at startup if other smbd versions are running in the cluster and refuses to start if so. This is done to protect data corruption in internal data structures due to incompatible Samba versions running concurrently in the same cluster. Setting this parameter to yes disables this safety check.

### `async smb echo handler`

Section: misc; Context: G; Type: boolean; Default: `no`

This parameter specifies whether Samba should fork the async smb echo handler. It can be beneficial if your file system can block syscalls for a very long time. In some circumstances, it prolongs the timeout that Windows uses to determine whether a connection is dead. This parameter is only for SMB1. For SMB2 and above TCP keepalives can be used instead.

### `auto services`

Section: misc; Context: G; Type: string

This is a list of services that you want to be automatically added to the browse lists. This is most useful for homes and printers services that would otherwise not be visible. Note that if you just want all printers in your printcap file loaded then the option is easier.

### `automount fs types`

Section: misc; Context: G; Type: cmdlist

This parameter specifies a list of additional filesystem magic numbers that should trigger automounting when accessed. The values should be specified as hexadecimal numbers (with or without 0x prefix), separated by spaces or commas. Note: This parameter is only available on Linux systems. To find the filesystem magic number for a mounted filesystem, consult /usr/include/linux/magic.h or call: stat -f -c '0x%t' /path/to/mountpoint Note: autofs (0x187) is always checked and does not need to be included in this list.

### `available`

Section: misc; Context: S; Type: boolean; Default: `yes`

This parameter lets you "turn off" a service. If available = no , then ALL attempts to connect to the service will fail. Such failures are logged.

### `cache directory`

Section: misc; Context: G; Type: string

Usually, most of the TDB files are stored in the lock directory . Since Samba 3.4.0, it is possible to differentiate between TDB files with persistent data and TDB files with non-persistent data using the state directory and the cache directory options. This option specifies the directory for storing TDB files containing non-persistent data that will be kept across service restarts. The directory should be placed on persistent storage, but the data can be safely deleted by an administrator.

### `change notify`

Section: misc; Context: G; Type: boolean; Default: `yes`

This parameter specifies whether Samba should reply to a client's file change notify requests. You should never need to change this parameter

### `change share command`

Section: misc; Context: G; Type: string

Samba 2.2.0 introduced the ability to dynamically add and delete shares via the Windows NT 4.0 Server Manager. The change share command is used to define an external program or script which will modify an existing service definition in smb.conf . In order to successfully execute the change share command , smbd requires that the administrator connects using a root account (i.e. uid == 0) or has the SeDiskOperatorPrivilege . Scripts defined in the change share command parameter are executed as root. When executed, smbd will automatically invoke the change share command with six parameters. configFile - the location of the global smb.conf file. shareName - the name of the new share. pathName - path to an **existing** directory on disk. comment - comment string to associate with the new share. max connections Number of maximum simultaneous connections to this share. CSC policy - client side caching policy in string form. Valid values are: manual, documents, programs, disable. This parameter is only used to modify existing file share definitions. To modify printer shares, use the "Printers..." folder as seen when browsing the Samba host.

### `cluster addresses`

Section: misc; Context: G; Type: cmdlist

With this parameter you can add additional addresses that nmbd will register with a WINS server. Similarly, these addresses will be registered by default when net ads dns register is called with yes configured.

### `clustering`

Section: misc; Context: G; Type: boolean; Default: `no`

This parameter specifies whether Samba should contact ctdb for accessing its tdb files and use ctdb as a backend for its messaging backend. Set this parameter to yes only if you have a cluster setup with ctdb running.

### `config file`

Section: misc; Context: G; Type: string

This allows you to override the config file to use, instead of the default (usually smb.conf ). There is a chicken and egg problem here as this option is set in the config file! For this reason, if the name of the config file has changed when the parameters are loaded then it will reload them from the new config file. This option takes the usual substitutions, which can be very useful. If the config file doesn't exist then it won't be loaded (allowing you to special case the config files of just a few clients).

### `copy`

Section: misc; Context: S; Type: string

This parameter allows you to "clone" service entries. The specified service is simply duplicated under the current service's name. Any parameters specified in the current section will override those in the section being copied. This feature lets you set up a 'template' service and create similar services easily. Note that the service being copied must occur earlier in the configuration file than the service doing the copying.

### `ctdbd socket`

Section: misc; Context: G; Type: string

In a test environment, this parameter can be used when clustering=yes to specify an alternate location for the CTDB Unix domain socket. This parameter should not be set in production environments. If it is not set then the (correct) build-time default is used.

### `ctdb locktime warn threshold`

Section: misc; Context: G; Type: integer; Default: `0`

In a cluster environment using Samba and ctdb it is critical that locks on central ctdb-hosted databases like locking.tdb are not held for long. With the current Samba architecture it happens that Samba takes a lock and while holding that lock makes file system calls into the shared cluster file system. This option makes Samba warn if it detects that it has held locks for the specified number of milliseconds. If this happens, smbd will emit a debug level 0 message into its logs and potentially into syslog. The most likely reason for such a log message is that an operation of the cluster file system Samba exports is taking longer than expected. The messages are meant as a debugging aid for potential cluster problems. The default value of 0 disables this logging.

### `ctdb timeout`

Section: misc; Context: G; Type: integer; Default: `0`

This parameter specifies a timeout in milliseconds for the connection between Samba and ctdb. It is only valid if you have compiled Samba with clustering and if you have set clustering=yes . When something in the cluster blocks, it can happen that we wait indefinitely long for ctdb, just adding to the blocking condition. In a well-running cluster this should never happen, but there are too many components in a cluster that might have hickups. Choosing the right balance for this value is very tricky, because on a busy cluster long service times to transfer something across the cluster might be valid. Setting it too short will degrade the service your cluster presents, setting it too long might make the cluster itself not recover from something severely broken for too long. Be aware that if you set this parameter, this needs to be in the file smb.conf, it is not really helpful to put this into a registry configuration (typical on a cluster), because to access the registry contact to ctdb is required. Setting ctdb timeout to n makes any process waiting longer than n milliseconds for a reply by the cluster panic. Setting it to 0 (the default) makes Samba block forever, which is the highly recommended default.

### `default service`

Section: misc; Context: G; Type: string

This parameter specifies the name of a service which will be connected to if the service actually requested cannot be found. Note that the square brackets are NOT given in the parameter value (see example below). There is no default value for this parameter. If this parameter is not given, attempting to connect to a nonexistent service results in an error. Typically the default service would be a , service. Also note that the apparent service name will be changed to equal that of the requested service, this is very useful as it allows you to use macros like %S to make a wildcard service. Note also that any "_" characters in the name of the service used in the default service will get mapped to a "/". This allows for interesting things.

### `delete readonly`

Section: misc; Context: S; Type: boolean; Default: `no`

This parameter allows readonly files to be deleted. This is not normal DOS semantics, but is allowed by UNIX. This option may be useful for running applications such as rcs, where UNIX file ownership prevents changing file permissions, and DOS semantics prevent deletion of a read only file.

### `delete share command`

Section: misc; Context: G; Type: string

Samba 2.2.0 introduced the ability to dynamically add and delete shares via the Windows NT 4.0 Server Manager. The delete share command is used to define an external program or script which will remove an existing service definition from smb.conf . In order to successfully execute the delete share command , smbd requires that the administrator connects using a root account (i.e. uid == 0) or has the SeDiskOperatorPrivilege . Scripts defined in the delete share command parameter are executed as root. When executed, smbd will automatically invoke the delete share command with two parameters. configFile - the location of the global smb.conf file. shareName - the name of the existing service. This parameter is only used to remove file shares. To delete printer shares, see the .

### `dfree cache time`

Section: misc; Context: S; Type: integer

The dfree cache time should only be used on systems where a problem occurs with the internal disk space calculations. This has been known to happen with Ultrix, but may occur with other operating systems. The symptom that was seen was an error of "Abort Retry Ignore" at the end of each directory listing. This is a new parameter introduced in Samba version 3.0.21. It specifies in seconds the time that smbd will cache the output of a disk free query. If set to zero (the default) no caching is done. This allows a heavily loaded server to prevent rapid spawning of scripts increasing the load. By default this parameter is zero, meaning no caching will be done.

### `dfree command`

Section: misc; Context: S; Type: string

The dfree command setting should only be used on systems where a problem occurs with the internal disk space calculations. This has been known to happen with Ultrix, but may occur with other operating systems. The symptom that was seen was an error of "Abort Retry Ignore" at the end of each directory listing. This setting allows the replacement of the internal routines to calculate the total disk space and amount available with an external routine. The example below gives a possible script that might fulfill this function. In Samba version 3.0.21 this parameter has been changed to be a per-share parameter, and in addition the parameter was added to allow the output of this script to be cached for systems under heavy load. The external program will be passed a single parameter indicating a directory in the filesystem being queried. This will typically consist of the string ./ . The script should return two integers in ASCII. The first should be the total disk space in blocks, and the second should be the number of available blocks. An optional third return value can give the block size in bytes. The default blocksize is 1024 bytes. Note: Your script should NOT be setuid or setgid and should be owned by (and writeable only by) root! Where the script dfree (which must be made executable) could be: #!/bin/sh df "$1" | tail -1 | awk '{print $(NF-4),$(NF-2)}' or perhaps (on Sys V based systems): #!/bin/sh /usr/bin/df -k "$1" | tail -1 | awk '{print $3" "$5}' Note that you may have to replace the command names with full path names on some systems. Also note the arguments passed into the script should be quoted inside the script in case they contain special characters such as spaces or newlines. By default internal routines for determining the disk capacity and remaining space will be used.

### `dmapi support`

Section: misc; Context: S; Type: boolean; Default: `no`

This parameter specifies whether Samba should use DMAPI to determine whether a file is offline or not. This would typically be used in conjunction with a hierarchical storage system that automatically migrates files to tape. Note that Samba infers the status of a file by examining the events that a DMAPI application has registered interest in. This heuristic is satisfactory for a number of hierarchical storage systems, but there may be system for which it will fail. In this case, Samba may erroneously report files to be offline. This parameter is only available if a supported DMAPI implementation was found at compilation time. It will only be used if DMAPI is found to enabled on the system at run time.

### `dns hostname`

Section: misc; Context: G; Type: string; Default: `[netbios name].[realm]`

This value is used: to register DNS record with AD during a join or by calling net ads dns register during Kerberos authentication to create service principal names during keytab creation - see the parameter This is not supported in samba-tool yet.

### `dont descend`

Section: misc; Context: S; Type: string

There are certain directories on some systems (e.g., the /proc tree under Linux) that are either not of interest to clients or are infinitely deep (recursive). This parameter allows you to specify a comma-delimited list of directories that the server should always show as empty. Note that Samba can be very fussy about the exact format of the "dont descend" entries. For example you may need ./proc instead of just /proc . Experimentation is the best policy :-)

### `dos filemode`

Section: misc; Context: S; Type: boolean; Default: `no`

The default behavior in Samba is to provide UNIX-like behavior where only the owner of a file/directory is able to change the permissions on it. However, this behavior is often confusing to DOS/Windows users. Enabling this parameter allows a user who has write access to the file (by whatever means, including an ACL permission) to modify the permissions (including ACL) on it. Note that a user belonging to the group owning the file will not be allowed to change permissions if the group is only granted read access. Ownership of the file/directory may also be changed. Note that using the VFS modules acl_xattr or acl_tdb which store native Windows as meta-data will automatically turn this option on for any share for which they are loaded, as they require this option to emulate Windows ACLs correctly.

### `dos filetime resolution`

Section: misc; Context: S; Type: boolean; Default: `no`

Under the DOS and Windows FAT filesystem, the finest granularity on time resolution is two seconds. Setting this parameter for a share causes Samba to round the reported time down to the nearest two second boundary when a query call that requires one second resolution is made to smbd 8 . This option is mainly used as a compatibility option for Visual C++ when used against Samba shares. If oplocks are enabled on a share, Visual C++ uses two different time reading calls to check if a file has changed since it was last read. One of these calls uses a one-second granularity, the other uses a two second granularity. As the two second call rounds any odd second down, then if the file has a timestamp of an odd number of seconds then the two timestamps will not match and Visual C++ will keep reporting the file has changed. Setting this option causes the two timestamps to match, and Visual C++ is happy.

### `dos filetimes`

Section: misc; Context: S; Type: boolean; Default: `yes`

Under DOS and Windows, if a user can write to a file they can change the timestamp on it. Under POSIX semantics, only the owner of the file or root may change the timestamp. By default, Samba emulates the DOS semantics and allows one to change the timestamp on a file if the user smbd is acting on behalf has write permissions. Due to changes in Microsoft Office 2000 and beyond, the default for this parameter has been changed from "no" to "yes" in Samba 3.0.14 and above. Microsoft Excel will display dialog box warnings about the file being changed by another user if this parameter is not set to "yes" and files are being shared between users.

### `dsdb event notification`

Section: misc; Context: G; Type: boolean; Default: `no`

When enabled, this option causes Samba (acting as an Active Directory Domain Controller) to stream Samba database events across the internal message bus. Scripts built using Samba's python bindings can listen to these events by registering as the service dsdb_event . This is not needed for the audit logging described in . Instead, this should instead be considered a developer option (it assists in the Samba testsuite) rather than a facility for external auditing, as message delivery is not guaranteed (a feature that the testsuite works around). The Samba database events are also logged via the normal logging methods when the is set appropriately, say to dsdb_json_audit:5 .

### `dsdb group change notification`

Section: misc; Context: G; Type: boolean; Default: `no`

When enabled, this option causes Samba (acting as an Active Directory Domain Controller) to stream group membership change events across the internal message bus. Scripts built using Samba's python bindings can listen to these events by registering as the service dsdb_group_event . This is not needed for the audit logging described in . Instead, this should instead be considered a developer option (it assists in the Samba testsuite) rather than a facility for external auditing, as message delivery is not guaranteed (a feature that the testsuite works around). The Samba database events are also logged via the normal logging methods when the is set appropriately, say to dsdb_group_json_audit:5 .

### `dsdb password event notification`

Section: misc; Context: G; Type: boolean; Default: `no`

When enabled, this option causes Samba (acting as an Active Directory Domain Controller) to stream password change and reset events across the internal message bus. Scripts built using Samba's python bindings can listen to these events by registering as the service password_event . This is not needed for the audit logging described in . Instead, this should instead be considered a developer option (it assists in the Samba testsuite) rather than a facility for external auditing, as message delivery is not guaranteed (a feature that the testsuite works around). The Samba database events are also logged via the normal logging methods when the is set appropriately, say to dsdb_password_json_audit:5 .

### `elasticsearch:address`

Section: misc; Context: S; Type: string; Default: `localhost`

Specifies the name of the Elasticsearch server to use for Spotlight queries when using the Elasticsearch backend.

### `elasticsearch:default_fields`

Section: misc; Context: G; Type: string; Default: `"file.filename", "content"`

Default attributes in Elasticsearch to query when receiving a Spotlight query that searches in the special attribute "*". This is the default used by macOS clients when searching from the Finder. This option expects a list of Elasticsearch attributes separated by comma where each attributes must be enclosed in double quotes.

### `elasticsearch:force substring search`

Section: misc; Context: G; Type: boolean; Default: `no`

Force string searches in string attributes likes paths to be prefix searches by prefixing a *. Example: a Spotlight search for '*=="samba*"' would be mapped to "'query': '(*samba*)'" instead of "'query': '(samba*)'".

### `elasticsearch:ignore unknown attribute`

Section: misc; Context: G; Type: boolean; Default: `no`

Ignore unknown Spotlight attributes in search queries. An example query using the unsupported attribute "kMDItemTopic" would be kMDItemTopic=="hotstuff" . By default any query using such a type would completely fail. By enabling this option, if the type match is a subexpression of a larger expression, then this subexpression is just ignored.

### `elasticsearch:ignore unknown type`

Section: misc; Context: G; Type: boolean; Default: `no`

Ignore unknown Spotlight types in search queries. An example query using the unsupported type "public.calendar-event" would be kMDItemContentType=="public.calendar-event" . By default any query using such a type would completely fail. By enabling this option, if the type match is a subexpression of a larger expression, then this subexpression is just ignored.

### `elasticsearch:index`

Section: misc; Context: S; Type: string; Default: `_all`

Specifies the name of the Elasticsearch index to use for Spotlight queries when using the Elasticsearch backend. The default value of "_all" is a special Elasticsearch value that performs the search operation on all indices.

### `elasticsearch:mappings`

Section: misc; Context: G; Type: string; Default: `/elasticsearch_mappings.json`

Path to a file specifying metadata attribute mappings in JSON format. Use by the Elasticsearch backend of the Spotlight RPC service.

### `elasticsearch:max results`

Section: misc; Context: S; Type: integer; Default: `100`

Path to a file specifying metadata attribute mappings in JSON format. Used by the Elasticsearch backend of the Spotlight RPC service. A value of 0 means no limit.

### `elasticsearch:port`

Section: misc; Context: S; Type: integer; Default: `9200`

Specifies the TCP port of the Elasticsearch server to use for Spotlight queries when using the Elasticsearch backend.

### `elasticsearch:use tls`

Section: misc; Context: S; Type: boolean; Default: `no`

Specifies whether to use HTTPS when talking to the Elasticsearch server used for Spotlight queries when using the Elasticsearch backend.

### `fake directory create times`

Section: misc; Context: S; Type: boolean; Default: `no`

NTFS and Windows VFAT file systems keep a create time for all files and directories. This is not the same as the ctime - status change time - that Unix keeps, so Samba by default reports the earliest of the various times Unix does keep. Setting this parameter for a share causes Samba to always report midnight 1-1-1980 as the create time for directories. This option is mainly used as a compatibility option for Visual C++ when used against Samba shares. Visual C++ generated makefiles have the object directory as a dependency for each object file, and a make rule to create the directory. Also, when NMAKE compares timestamps it uses the creation time when examining a directory. Thus the object directory will be created if it does not exist, but once it does exist it will always have an earlier timestamp than the object files it contains. However, Unix time semantics mean that the create time reported by Samba will be updated whenever a file is created or deleted in the directory. NMAKE finds all object files in the object directory. The timestamp of the last one built is then compared to the timestamp of the object directory. If the directory's timestamp if newer, then all object files will be rebuilt. Enabling this option ensures directories always predate their contents and an NMAKE build will proceed as expected.

### `follow symlinks`

Section: misc; Context: S; Type: boolean; Default: `yes`

This parameter allows the Samba administrator to stop smbd 8 from following symbolic links in a particular share. Setting this parameter to no prevents any file or directory that is a symbolic link from being followed (the user will get an error). This option is very useful to stop users from adding a symbolic link to /etc/passwd in their home directory for instance. However it will slow filename lookups down slightly. This option is enabled (i.e. smbd will follow symbolic links) by default.

### `fss: prune stale`

Section: misc; Context: G; Type: boolean; Default: `no`

When enabled, Samba's File Server Remote VSS Protocol (FSRVP) server checks all FSRVP initiated snapshots on startup, and removes any corresponding state (including share definitions) for nonexistent snapshot paths.

### `fss: sequence timeout`

Section: misc; Context: G; Type: integer; Default: `180 or 1800, depending on operation`

The File Server Remote VSS Protocol (FSRVP) server includes a message sequence timer to ensure cleanup on unexpected client disconnect. This parameter overrides the default timeout between FSRVP operations. FSRVP timeouts can be completely disabled via a value of 0.

### `fstype`

Section: misc; Context: S; Type: string; Default: `NTFS`

This parameter allows the administrator to configure the string that specifies the type of filesystem a share is using that is reported by smbd 8 when a client queries the filesystem type for a share. The default type is NTFS for compatibility with Windows NT but this can be changed to other strings such as Samba or FAT if required.

### `honor change notify privilege`

Section: misc; Context: S; Type: boolean; Default: `no`

This option can be used to make use of the change notify privilege. By default notify results are not checked against the file system permissions. If "honor change notify privilege" is enabled, a user will only receive notify results, if he has change notify privilege or sufficient file system permissions. If a user has the change notify privilege, he will receive all requested notify results, even if the user does not have the permissions on the file system.

### `include`

Section: misc; Context: S; Type: string

This allows you to include one config file inside another. The file is included literally, as though typed in place. It takes the standard substitutions, except %u , %P and %S . The parameter include = registry has a special meaning: It does not include a file named registry from the current working directory, but instead reads the global configuration options from the registry. See the section on registry-based configuration for details. Note that this option automatically activates registry shares.

### `kernel change notify`

Section: misc; Context: G; Type: boolean; Default: `yes`

This parameter specifies whether Samba should ask the kernel for change notifications in directories so that SMB clients can refresh whenever the data on the server changes. This parameter is only used when your kernel supports change notification to user programs using the inotify interface.

### `lock directory`

Section: misc; Context: G; Type: string

This option specifies the directory where lock files will be placed. The lock files are used to implement the option. Note: This option can not be set inside registry configurations. The files placed in this directory are not required across service restarts and can be safely placed on volatile storage (e.g. tmpfs in Linux)

### `log writeable files on exit`

Section: misc; Context: G; Type: boolean; Default: `no`

When the network connection between a CIFS client and Samba dies, Samba has no option but to simply shut down the server side of the network connection. If this happens, there is a risk of data corruption because the Windows client did not complete all write operations that the Windows application requested. Setting this option to "yes" makes smbd log with a level 0 message a list of all files that have been opened for writing when the network connection died. Those are the files that are potentially corrupted. It is meant as an aid for the administrator to give him a list of files to do consistency checks on.

### `magic script`

Section: misc; Context: S; Type: string

This parameter specifies the name of a file which, if opened, will be executed by the server when the file is closed. This allows a UNIX script to be sent to the Samba host and executed on behalf of the connected user. Scripts executed in this way will be deleted upon completion assuming that the user has the appropriate level of privilege and the file permissions allow the deletion. If the script generates output, output will be sent to the file specified by the parameter (see above). Note that some shells are unable to interpret scripts containing CR/LF instead of CR as the end-of-line marker. Magic scripts must be executable as is on the host, which for some hosts and some shells will require filtering at the DOS end. Magic scripts are EXPERIMENTAL and should NOT be relied upon.

### `nbt client socket address`

Section: misc; Context: G; Type: string; Default: `0.0.0.0`

This option allows you to control what address Samba will send NBT client packets from, and process replies using, including in nmbd. Setting this option should never be necessary on usual Samba servers running only one nmbd. By default Samba will send UDP packets from the OS default address for the destination, and accept replies on 0.0.0.0. This parameter is deprecated. See Yes and for the previous behaviour of controlling the normal listening sockets.

### `ncalrpc dir`

Section: misc; Context: G; Type: string

This directory will hold a series of named pipes to allow RPC over inter-process communication. This will allow Samba and other unix processes to interact over DCE/RPC without using TCP/IP. Additionally a sub-directory 'np' has restricted permissions, and allows a trusted communication channel between Samba processes

### `nmbd bind explicit broadcast`

Section: misc; Context: G; Type: boolean; Default: `yes`

This option causes nmbd 8 to explicitly bind to the broadcast address of the local subnets. This is needed to make nmbd work correctly in combination with the option. You should not need to unset this option.

### `panic action`

Section: misc; Context: G; Type: string

This is a Samba developer option that allows a system command to be called when either smbd 8 or nmbd 8 crashes. This is usually used to draw attention to the fact that a problem occurred.

### `perfcount module`

Section: misc; Context: G; Type: string

This parameter specifies the perfcount backend to be used when monitoring SMB operations. Only one perfcount module may be used, and it must implement all of the apis contained in the smb_perfcount_handler structure defined in smb.h.

### `pid directory`

Section: misc; Context: G; Type: string

This option specifies the directory where pid files will be placed.

### `postexec`

Section: misc; Context: S; Type: string

This option specifies a command to be run whenever the service is disconnected. It takes the usual substitutions. The command may be run as the root on some systems. An interesting example may be to unmount server resources: postexec = /etc/umount /cdrom

### `preexec close`

Section: misc; Context: S; Type: boolean; Default: `no`

This boolean option controls whether a non-zero return code from should close the service being connected to.

### `registry shares`

Section: misc; Context: G; Type: boolean; Default: `no`

This turns on or off support for share definitions read from registry. Shares defined in smb.conf take precedence over shares with the same name defined in registry. See the section on registry-based configuration for details. Note that this parameter defaults to no , but it is set to yes when config backend is set to registry .

### `remote announce`

Section: misc; Context: G; Type: string

This option allows you to setup nmbd 8 to periodically announce itself to arbitrary IP addresses with an arbitrary workgroup name. This is useful if you want your Samba server to appear in a remote workgroup for which the normal browse propagation rules don't work. The remote workgroup can be anywhere that you can send IP packets to. For example: remote announce = 192.168.2.255/SERVERS 192.168.4.255/STAFF the above line would cause nmbd to announce itself to the two given IP addresses using the given workgroup names. If you leave out the workgroup name, then the one given in the parameter is used instead. The IP addresses you choose would normally be the broadcast addresses of the remote networks, but can also be the IP addresses of known browse masters if your network config is that stable. See the chapter on Network Browsing in the Samba-HOWTO book.

### `remote browse sync`

Section: misc; Context: G; Type: string

This option allows you to setup nmbd 8 to periodically request synchronization of browse lists with the master browser of a Samba server that is on a remote segment. This option will allow you to gain browse lists for multiple workgroups across routed networks. This is done in a manner that does not work with any non-Samba servers. This is useful if you want your Samba server and all local clients to appear in a remote workgroup for which the normal browse propagation rules don't work. The remote workgroup can be anywhere that you can send IP packets to. For example: remote browse sync = 192.168.2.255 192.168.4.255 the above line would cause nmbd to request the master browser on the specified subnets or addresses to synchronize their browse lists with the local server. The IP addresses you choose would normally be the broadcast addresses of the remote networks, but can also be the IP addresses of known browse masters if your network config is that stable. If a machine IP address is given Samba makes NO attempt to validate that the remote machine is available, is listening, nor that it is in fact the browse master on its segment. The may be used on networks where there is no WINS server, and may be used on disjoint networks where each network has its own WINS server.

### `reset on zero vc`

Section: misc; Context: G; Type: boolean; Default: `no`

This boolean option controls whether an incoming SMB1 session setup should kill other connections coming from the same IP. This matches the default Windows 2003 behaviour. Setting this parameter to yes becomes necessary when you have a flaky network and windows decides to reconnect while the old connection still has files with share modes open. These files become inaccessible over the new connection. The client sends a zero VC on the new connection, and Windows 2003 kills all other connections coming from the same IP. This way the locked files are accessible again. Please be aware that enabling this option will kill connections behind a masquerading router, and will not trigger for clients that only use SMB2 or SMB3.

### `root postexec`

Section: misc; Context: S; Type: string

This is the same as the postexec parameter except that the command is run as root. This is useful for unmounting filesystems (such as CDROMs) after a connection is closed.

### `root preexec`

Section: misc; Context: S; Type: string

This is the same as the preexec parameter except that the command is run as root. This is useful for mounting filesystems (such as CDROMs) when a connection is opened.

### `root preexec close`

Section: misc; Context: S; Type: boolean; Default: `no`

This is the same as the preexec close parameter except that the command is run as root.

### `smbd async dosmode`

Section: misc; Context: S; Type: boolean; Default: `no`

This parameter control whether the fileserver will use sync or async methods for fetching the DOS attributes when doing a directory listing. By default sync methods will be used.

### `smbd getinfo ask sharemode`

Section: misc; Context: S; Type: boolean; Default: `yes`

This parameter allows disabling fetching file write time from the open file handle database locking.tdb when a client requests file or directory metadata. It's a performance optimisation at the expense of protocol correctness.

### `smbd max async dosmode`

Section: misc; Context: S; Type: integer; Default: `aio max threads * 2`

This parameter controls how many async operations to fetch the DOS attributes the fileserver will queue when doing directory listings.

### `smbd max xattr size`

Section: misc; Context: S; Type: integer; Default: `65536`

This parameter controls the maximum size of extended attributes that may be written to the server as EAs or as alternate data streams if vfs_streams_xattr is enabled. The maximum size of extended attributes depends on the Samba server's operating system and the underlying filesystem. The Linux VFS currently sets an upper boundary of 64 KiB per extended attribute. FreeBSD does not set a practical upper limit, but since pread() and pwrite() are not possible via the extattr on FreeBSD, it is not recommended to increase this value above a few MiB. If a client attempts to write an overly-large alternate datastream, the Samba server will return STATUS_FILESYSTEM_LIMITATION. If this error is encountered, users may try increasing the maximum size supported for xattr writes. If this is not possible, and writes are from a MacOS client and to an AFP_Resource extended attribute, the user may enable the vfs_fruit module and configure to allow stream writes for AFP_Resource to an alternative storage location. See vfs_fruit documentation for further details.

### `smbd profiling share`

Section: misc; Context: S; Type: boolean; Default: `no`

This parameter allows the administrator to enable per-share profiling support. When enabled, profile counters may be collected with per-share granularity a specific shares. Takes affect only when global option is enabled.

### `smbd profiling level`

Section: misc; Context: G; Type: enum; Default: `off`

This parameter allows the administrator to enable profiling support. Possible values are off , count and on .

### `smbd search ask sharemode`

Section: misc; Context: S; Type: boolean; Default: `yes`

This parameter allows disabling fetching file write time from the open file handle database locking.tdb. It's a performance optimisation at the expense of protocol correctness.

### `spotlight`

Section: misc; Context: S; Type: boolean; Default: `no`

This parameter controls whether Samba allows Spotlight queries on a share. For controlling indexing of filesystems you also have to use Tracker's own configuration system. Spotlight has several prerequisites: Samba must be configured and built with Spotlight support. Tracker integration must be setup and the share must be indexed by Tracker. For a detailed set of instructions please see https://wiki.samba.org/index.php/Spotlight .

### `spotlight backend`

Section: misc; Context: S; Type: enum; Default: `noindex`

Spotlight search backend. Available backends: noindex - a backend that returns no results. tracker - Gnome Tracker. elasticsearch - a backend that uses JSON and REST over HTTP(s) to query an Elasticsearch server.

### `state directory`

Section: misc; Context: G; Type: string

Usually, most of the TDB files are stored in the lock directory . Since Samba 3.4.0, it is possible to differentiate between TDB files with persistent data and TDB files with non-persistent data using the state directory and the cache directory options. This option specifies the directory where TDB files containing important persistent data will be stored.

### `usershare allow guests`

Section: misc; Context: G; Type: boolean; Default: `no`

This parameter controls whether user defined shares are allowed to be accessed by non-authenticated users or not. It is the equivalent of allowing people who can create a share the option of setting guest ok = yes in a share definition. Due to its security sensitive nature, the default is set to off.

### `usershare max shares`

Section: misc; Context: G; Type: integer; Default: `0`

This parameter specifies the number of user defined shares that are allowed to be created by users belonging to the group owning the usershare directory. If set to zero (the default) user defined shares are ignored.

### `usershare owner only`

Section: misc; Context: G; Type: boolean; Default: `yes`

This parameter controls whether the pathname exported by a user defined shares must be owned by the user creating the user defined share or not. If set to True (the default) then smbd checks that the directory path being shared is owned by the user who owns the usershare file defining this share and refuses to create the share if not. If set to False then no such check is performed and any directory path may be exported regardless of who owns it.

### `usershare path`

Section: misc; Context: G; Type: string; Default: `/usershares`

This parameter specifies the absolute path of the directory on the filesystem used to store the user defined share definition files. This directory must be owned by root, and have no access for other, and be writable only by the group owner. In addition the "sticky" bit must also be set, restricting rename and delete to owners of a file (in the same way the /tmp directory is usually configured). Members of the group owner of this directory are the users allowed to create usershares. For example, a valid usershare directory might be /usr/local/samba/lib/usershares, set up as follows. ls -ld /usr/local/samba/lib/usershares/ drwxrwx--T 2 root power_users 4096 2006-05-05 12:27 /usr/local/samba/lib/usershares/ In this case, only members of the group "power_users" can create user defined shares.

### `usershare prefix allow list`

Section: misc; Context: G; Type: cmdlist

This parameter specifies a list of absolute pathnames the root of which are allowed to be exported by user defined share definitions. If the pathname to be exported doesn't start with one of the strings in this list, the user defined share will not be allowed. This allows the Samba administrator to restrict the directories on the system that can be exported by user defined shares. If there is a "usershare prefix deny list" and also a "usershare prefix allow list" the deny list is processed first, followed by the allow list, thus leading to the most restrictive interpretation.

### `usershare prefix deny list`

Section: misc; Context: G; Type: cmdlist

This parameter specifies a list of absolute pathnames the root of which are NOT allowed to be exported by user defined share definitions. If the pathname exported starts with one of the strings in this list the user defined share will not be allowed. Any pathname not starting with one of these strings will be allowed to be exported as a usershare. This allows the Samba administrator to restrict the directories on the system that can be exported by user defined shares. If there is a "usershare prefix deny list" and also a "usershare prefix allow list" the deny list is processed first, followed by the allow list, thus leading to the most restrictive interpretation.

### `usershare template share`

Section: misc; Context: G; Type: string

User defined shares only have limited possible parameters such as path, guest ok, etc. This parameter allows usershares to "cloned" from an existing share. If "usershare template share" is set to the name of an existing share, then all usershares created have their defaults set from the parameters set on this share. The target share may be set to be invalid for real file sharing by setting the parameter "-valid = False" on the template share definition. This causes it not to be seen as a real exported share but to be able to be used as a template for usershares.

### `utmp`

Section: misc; Context: G; Type: boolean; Default: `no`

This boolean parameter is only available if Samba has been configured and compiled with the option --with-utmp . If set to yes then Samba will attempt to add utmp or utmpx records (depending on the UNIX system) whenever a connection is made to a Samba server. Sites may use this to record the user connecting to a Samba share. Due to the requirements of the utmp record, we are required to create a unique identifier for the incoming user. Enabling this option creates an n^2 algorithm to find this number. This may impede performance on large installations.

### `utmp directory`

Section: misc; Context: G; Type: string; Default: `Determined automatically`

This parameter is only available if Samba has been configured and compiled with the option --with-utmp . It specifies a directory pathname that is used to store the utmp or utmpx files (depending on the UNIX system) that record user connections to a Samba server. By default this is not set, meaning the system will use whatever utmp file the native system is set to use (usually /var/run/utmp on Linux).

### `-valid`

Section: misc; Context: S; Type: boolean; Default: `yes`

This parameter indicates whether a share is valid and thus can be used. When this parameter is set to false, the share will be in no way visible nor accessible. This option should not be used by regular users but might be of help to developers. Samba uses this option internally to mark shares as deleted.

### `volume`

Section: misc; Context: S; Type: string; Default: `the name of the share`

This allows you to override the volume label returned for a share. Useful for CDROMs with installation programs that insist on a particular volume label.

### `volume serial number`

Section: misc; Context: S; Type: integer; Default: `-1`

This allows to override the volume serial number (a 32bit value) reported for a share. The special value -1 (default) stands for a unique number that is calculated for each share.

### `wide links`

Section: misc; Context: S; Type: boolean; Default: `no`

This parameter controls whether or not links in the UNIX file system may be followed by the server. Links that point to areas within the directory tree exported by the server are always allowed; this parameter controls access only to areas that are outside the directory tree being exported. Note: Turning this parameter on when UNIX extensions are enabled will allow UNIX clients to create symbolic links on the share that can point to files or directories outside restricted path exported by the share definition. This can cause access to areas outside of the share. Due to this problem, this parameter will be automatically disabled (with a message in the log file) if the option is on. See the parameter if you wish to change this coupling between the two parameters.

### `wsp property file`

Section: misc; Context: G; Type: string

parameter. This parameter specifies the file where additional WSP Windows Search Protocol properties are stored. The format of the file is a csv consisting of 10 comma separated columns. The first 3 columns are required, the other columns are desirable but not necessary. Property Name A property name e.g. System.ItemUrl. GUID A guid that identifies the propertyset the property belongs to. prop ID A number that together with the GUID uniquely identifies the property. inInverted Index Set to TRUE is the property is indexed. isColumn Set to TRUE if the property is one that can be returned in rows returned from WSP query. type One of Boolean , Buffer , Byte , DateTime , Double , Int32 , String , UInt16 , UInt32 , UInt64 MaxSize maximum size when stored. Vector Property TRUE if this is a multivalue property. Description Description of what the property is used for.

### `wtmp directory`

Section: misc; Context: G; Type: string

This parameter is only available if Samba has been configured and compiled with the option --with-utmp . It specifies a directory pathname that is used to store the wtmp or wtmpx files (depending on the UNIX system) that record user connections to a Samba server. The difference with the utmp directory is the fact that user info is kept after a user has logged out. By default this is not set, meaning the system will use whatever utmp file the native system is set to use (usually /var/run/wtmp on Linux).
