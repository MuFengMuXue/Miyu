# smb.conf Parameters / tuning

### `aio max threads`

Section: tuning; Context: G; Type: integer; Default: `100`

The integer parameter specifies the maximum number of threads each smbd process will create when doing parallel asynchronous IO calls. If the number of outstanding calls is greater than this number the requests will not be refused but go onto a queue and will be scheduled in turn as outstanding requests complete. aio read size aio write size

### `aio read size`

Section: tuning; Context: S; Type: bytes; Default: `1`

If this integer parameter is set to a non-zero value, Samba will read from files asynchronously when the request size is bigger than this value. Note that it happens only for non-chained and non-chaining reads. The only reasonable values for this parameter are 0 (no async I/O) and 1 (always do async I/O). aio write size

### `aio write behind`

Section: tuning; Context: S; Type: string

If Samba has been built with asynchronous I/O support, Samba will not wait until write requests are finished before returning the result to the client for files listed in this parameter. Instead, Samba will immediately return that the write request has been finished successfully, no matter if the operation will succeed or not. This might speed up clients without aio support, but is really dangerous, because data could be lost and files could be damaged. The syntax is identical to the parameter.

### `aio write size`

Section: tuning; Context: S; Type: bytes; Default: `1`

If this integer parameter is set to a non-zero value, Samba will write to files asynchronously when the request size is bigger than this value. Note that it happens only for non-chained and non-chaining writes. The only reasonable values for this parameter are 0 (no async I/O) and 1 (always do async I/O). Compared to this parameter has a smaller effect, most writes should end up in the file system cache. Writes that require space allocation might benefit most from going asynchronous. aio read size

### `allocation roundup size`

Section: tuning; Context: S; Type: bytes; Default: `0`

This parameter allows an administrator to tune the allocation size reported to Windows clients. This is only useful for old SMB1 clients because modern SMB dialects eliminated that bottleneck and have better performance by default. Using this parameter may cause difficulties for some applications, e.g. MS Visual Studio. If the MS Visual Studio compiler starts to crash with an internal error, set this parameter to zero for this share. Settings this parameter to a large value can also cause small files to allocate more space on the disk than needed. This parameter is deprecated and will be removed in one of the next Samba releases. The integer parameter specifies the roundup size in bytes.

### `async dns timeout`

Section: tuning; Context: G; Type: integer; Default: `10`

The number of seconds the asynchronous DNS resolver code in Samba will wait for responses. Some of the Samba client library code uses internal asynchronous DNS resolution for A and AAAA records when trying to find Active Directory Domain controllers. This value prevents this name resolution code from waiting for DNS server timeouts. The minimum value of this parameter is clamped at 1 second.

### `block size`

Section: tuning; Context: S; Type: bytes; Default: `1024`

This parameter controls the behavior of smbd 8 when reporting disk free sizes. By default, this reports a disk block size of 1024 bytes. Changing this parameter may have some effect on the efficiency of client writes, this is not yet confirmed. This parameter was added to allow advanced administrators to change it (usually to a higher value) and test the effect it has on client write performance without re-compiling the code. As this is an experimental option it may be removed in a future release. Changing this option does not change the disk free reporting size, just the block size unit reported to the client.

### `check parent directory delete on close`

Section: tuning; Context: S; Type: boolean; Default: `no`

A Windows SMB server prevents the client from creating files in a directory that has the delete-on-close flag set. By default Samba doesn't perform this check as this check is a quite expensive operation in Samba.

### `deadtime`

Section: tuning; Context: G; Type: integer; Default: `10080`

The value of the parameter (a decimal integer) represents the number of minutes of inactivity before a connection is considered dead, and it is disconnected. The deadtime only takes effect if the number of open files is zero. This is useful to stop a server's resources being exhausted by a large number of inactive connections. Most clients have an auto-reconnect feature when a connection is broken so in most cases this parameter should be transparent to users. Using this parameter with a timeout of a few minutes is recommended for most systems. A deadtime of zero indicates that no auto-disconnection should be performed.

### `hostname lookups`

Section: tuning; Context: G; Type: boolean; Default: `no`

Specifies whether samba should use (expensive) hostname lookups or use the ip addresses instead. An example place where hostname lookups are currently used is when checking the hosts deny and hosts allow .

### `keepalive`

Section: tuning; Context: G; Type: integer; Default: `300`

The value of the parameter (an integer) represents the number of seconds between keepalive packets. If this parameter is zero, no keepalive packets will be sent. Keepalive packets, if sent, allow the server to tell whether a client is still present and responding. Keepalives should, in general, not be needed if the socket has the SO_KEEPALIVE attribute set on it by default. (see ). Basically you should only use this option if you strike difficulties. Please note this option only applies to SMB1 client connections, and has no effect on SMB2 clients.

### `max connections`

Section: tuning; Context: S; Type: integer; Default: `0`

This option allows the number of simultaneous connections to a service to be limited. If max connections is greater than 0 then connections will be refused if this number of connections to the service are already open. A value of zero mean an unlimited number of connections may be made. Record lock files are used to implement this feature. The lock files will be stored in the directory specified by the option.

### `max disk size`

Section: tuning; Context: G; Type: bytes; Default: `0`

This option allows you to put an upper limit on the apparent size of disks. If you set this option to 100 then all shares will appear to be not larger than 100 MB in size. Note that this option does not limit the amount of data you can put on the disk. In the above case you could still store much more than 100 MB on the disk, but if a client ever asks for the amount of free disk space or the total disk size then the result will be bounded by the amount specified in max disk size . This option is primarily useful to work around bugs in some pieces of software that can't handle very large disks, particularly disks over 1GB in size. A max disk size of 0 means no limit.

### `max open files`

Section: tuning; Context: G; Type: integer; Default: `16384`

This parameter limits the maximum number of open files that one smbd 8 file serving process may have open for a client at any one time. This parameter can be set very high (16384) as Samba uses only one bit per unopened file. Setting this parameter lower than 16384 will cause Samba to complain and set this value back to the minimum of 16384, as Windows 7 depends on this number of open file handles being available. The limit of the number of open files is usually set by the UNIX per-process file descriptor limit rather than this parameter so you should never need to touch this parameter.

### `max smbd processes`

Section: tuning; Context: G; Type: integer; Default: `0`

This parameter limits the maximum number of smbd 8 processes concurrently running on a system and is intended as a stopgap to prevent degrading service to clients in the event that the server has insufficient resources to handle more than this number of connections. Remember that under normal operating conditions, each user will have an smbd 8 associated with him or her to handle connections to all shares from a given host. For a Samba ADDC running the standard process model this option limits the number of processes forked to handle requests. Currently new processes are only forked for ldap and netlogon requests.

### `min print space`

Section: tuning; Context: S; Type: integer; Default: `0`

This sets the minimum amount of free disk space that must be available before a user will be able to spool a print job. It is specified in kilobytes. The default is 0, which means a user can always spool a print job.

### `name cache timeout`

Section: tuning; Context: G; Type: integer; Default: `660`

Specifies the number of seconds it takes before entries in samba's hostname resolve cache time out. If the timeout is set to 0. the caching is disabled.

### `socket options`

Section: tuning; Context: G; Type: string; Default: `TCP_NODELAY`

Modern server operating systems are tuned for high network performance in the majority of situations; when you set socket options you are overriding those settings. Linux in particular has an auto-tuning mechanism for buffer sizes that will be disabled if you specify a socket buffer size. This can potentially cripple your TCP/IP stack. Getting the socket options correct can make a big difference to your performance, but getting them wrong can degrade it by just as much. As with any other low level setting, if you must make changes to it, make small changes and test the effect before making any large changes. This option allows you to set socket options to be used when talking with the client. Socket options are controls on the networking layer of the operating systems which allow the connection to be tuned. This option will typically be used to tune your Samba server for optimal performance for your local network. There is no way that Samba can know what the optimal parameters are for your net, so you must experiment and choose them yourself. We strongly suggest you read the appropriate documentation for your operating system first (perhaps man setsockopt will help). You may find that on some systems Samba will say "Unknown socket option" when you supply an option. This means you either incorrectly typed it or you need to add an include file to includes.h for your OS. If the latter is the case please send the patch to samba-technical@lists.samba.org . Any of the supported socket options may be combined in any way you like, as long as your OS allows it. This is the list of socket options currently settable using this option: SO_KEEPALIVE SO_REUSEADDR SO_BROADCAST TCP_NODELAY TCP_KEEPCNT * TCP_KEEPIDLE * TCP_KEEPINTVL * IPTOS_LOWDELAY IPTOS_THROUGHPUT SO_REUSEPORT SO_SNDBUF * SO_RCVBUF * SO_SNDLOWAT * SO_RCVLOWAT * SO_SNDTIMEO * SO_RCVTIMEO * TCP_FASTACK * TCP_QUICKACK TCP_NODELAYACK TCP_KEEPALIVE_THRESHOLD * TCP_KEEPALIVE_ABORT_THRESHOLD * TCP_DEFER_ACCEPT * TCP_USER_TIMEOUT * Those marked with a '*' take an integer argument. The others can optionally take a 1 or 0 argument to enable or disable the option, by default they will be enabled if you don't specify 1 or 0. To specify an argument use the syntax SOME_OPTION = VALUE for example SO_SNDBUF = 8192 . Note that you must not have any spaces before or after the = sign. If you are on a local network then a sensible option might be: socket options = IPTOS_LOWDELAY If you have a local network then you could try: socket options = IPTOS_LOWDELAY TCP_NODELAY If you are on a wide area network then perhaps try setting IPTOS_THROUGHPUT. Note that several of the options may cause your Samba server to fail completely. Use these options with caution!

### `strict allocate`

Section: tuning; Context: S; Type: boolean; Default: `no`

This is a boolean that controls the handling of disk space allocation in the server. When this is set to yes the server will change from UNIX behaviour of not committing real disk storage blocks when a file is extended to the Windows behaviour of actually forcing the disk system to allocate real storage blocks when a file is created or extended to be a given size. In UNIX terminology this means that Samba will stop creating sparse files. This option is really designed for file systems that support fast allocation of large numbers of blocks such as extent-based file systems. On file systems that don't support extents (most notably ext3) this can make Samba slower. When you work with large files over >100MB on file systems without extents you may even run into problems with clients running into timeouts. When you have an extent based filesystem it's likely that we can make use of unwritten extents which allows Samba to allocate even large amounts of space very fast and you will not see any timeout problems caused by strict allocate. With strict allocate in use you will also get much better out of quota messages in case you use quotas. Another advantage of activating this setting is that it will help to reduce file fragmentation. To give you an idea on which filesystems this setting might currently be a good option for you: XFS, ext4, btrfs, ocfs2 on Linux and JFS2 on AIX support unwritten extents. On Filesystems that do not support it, preallocation is probably an expensive operation where you will see reduced performance and risk to let clients run into timeouts when creating large files. Examples are ext3, ZFS, HFS+ and most others, so be aware if you activate this setting on those filesystems.

### `strict rename`

Section: tuning; Context: S; Type: boolean; Default: `no`

By default a Windows SMB server prevents directory renames when there are open file or directory handles below it in the filesystem hierarchy. Historically Samba has always allowed this as POSIX filesystem semantics require it. This boolean parameter allows Samba to match the Windows behavior. Setting this to "yes" is a very expensive change, as it forces Samba to travers the entire open file handle database on every directory rename request. In a clustered Samba system the cost is even greater than the non-clustered case. When set to "no" smbd only checks the local process the client is attached to for open files below a directory being renamed, instead of checking for open files across all smbd processes. Because of the expense in fully searching the database, the default is "no", and it is recommended to be left that way unless a specific Windows application requires it to be changed. If the client has requested UNIX extensions (POSIX pathnames) then renames are always allowed and this parameter has no effect. Enabling implicitly enables .

### `strict sync`

Section: tuning; Context: S; Type: boolean; Default: `yes`

This parameter controls whether Samba honors a request from an SMB client to ensure any outstanding operating system buffer contents held in memory are safely written onto stable storage on disk. If set to yes , which is the default, then Windows applications can force the smbd server to synchronize unwritten data onto the disk. If set to no then smbd will ignore client requests to synchronize unwritten data onto stable storage on disk. In Samba 4.7.0, the default for this parameter changed from no to yes to better match the expectations of SMB2/3 clients and improve application safety when running against smbd. The flush request from SMB2/3 clients is handled asynchronously inside smbd, so leaving the parameter as the default value of yes does not block the processing of other requests to the smbd process. Legacy Windows applications (such as the Windows 98 explorer shell) seemed to confuse writing buffer contents to the operating system with synchronously writing outstanding data onto stable storage on disk. Changing this parameter to no means that smbd 8 will ignore the Windows applications request to synchronize unwritten data onto disk. Only consider changing this if smbd is serving obsolete SMB1 Windows clients prior to Windows XP (Windows 98 and below). There should be no need to change this setting for normal operations.

### `sync always`

Section: tuning; Context: S; Type: boolean; Default: `no`

This is a boolean parameter that controls whether writes will always be written to stable storage before the write call returns. If this is no then the server will be guided by the client's request in each write call (clients can set a bit indicating that a particular write should be synchronous). If this is yes then every write will be followed by a fsync() call to ensure the data is written to disk. Note that the strict sync parameter must be set to yes in order for this parameter to have any effect.

### `use mmap`

Section: tuning; Context: G; Type: boolean; Default: `yes`

This global parameter determines if the tdb internals of Samba can depend on mmap working correctly on the running system. Samba requires a coherent mmap/read-write system memory cache. Currently only OpenBSD and HPUX do not have such a coherent cache, and on those platforms this parameter is overridden internally to be effectively no . On all systems this parameter should be left alone. This parameter is provided to help the Samba developers track down problems with the tdb internal code.

### `use sendfile`

Section: tuning; Context: S; Type: boolean; Default: `no`

If this parameter is yes , and the sendfile() system call is supported by the underlying operating system, then some SMB read calls (mainly ReadAndX and ReadRaw) will use the more efficient sendfile system call for files that are exclusively oplocked. This may make more efficient use of the system CPU's and cause Samba to be faster. Samba automatically turns this off for clients that use protocol levels lower than NT LM 0.12 and when it detects a client is Windows 9x (using sendfile from Linux will cause these clients to fail).
