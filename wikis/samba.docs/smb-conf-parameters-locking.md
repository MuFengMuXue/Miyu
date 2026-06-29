# smb.conf Parameters / locking

### `blocking locks`

Section: locking; Context: S; Type: boolean; Default: `yes`

This parameter controls the behavior of smbd 8 when given a request by a client to obtain a byte range lock on a region of an open file, and the request has a time limit associated with it. If this parameter is set and the lock range requested cannot be immediately satisfied, samba will internally queue the lock request, and periodically attempt to obtain the lock until the timeout period expires. If this parameter is set to no , then samba will behave as previous versions of Samba would and will fail the lock request immediately if the lock range cannot be obtained.

### `csc policy`

Section: locking; Context: S; Type: enum; Default: `manual`

This stands for client-side caching policy , and specifies how clients capable of offline caching will cache the files in the share. The valid values are: manual, documents, programs, disable. These values correspond to those used on Windows servers. For example, shares containing roaming profiles can have offline caching disabled using disable .

### `fake oplocks`

Section: locking; Context: S; Type: boolean; Default: `no`

Oplocks are the way that SMB clients get permission from a server to locally cache file operations. If a server grants an oplock (opportunistic lock) then the client is free to assume that it is the only one accessing the file and it will aggressively cache file data. With some oplock types the client may even cache file open/close operations. This can give enormous performance benefits. When you set fake oplocks = yes , smbd 8 will always grant oplock requests no matter how many clients are using the file. It is generally much better to use the real support rather than this parameter. If you enable this option on all read-only shares or shares that you know will only be accessed from one client at a time such as physically read-only media like CDROMs, you will see a big performance improvement on many operations. If you enable this option on shares where multiple clients may be accessing the files read-write at the same time you can get data corruption. Use this option carefully!

### `smbd force process locks`

Section: locking; Context: S; Type: boolean; Default: `no`

This boolean option tells smbd whether to forcefully disable the use of Open File Description locks on Linux. This option should not be changed from the default unless you know what you're doing.

### `kernel oplocks`

Section: locking; Context: S; Type: boolean; Default: `no`

For UNIXes that support kernel based (currently only Linux), this parameter allows the use of them to be turned on or off. However, this disables Level II oplocks for clients as the Linux kernel does not support them properly. Kernel oplocks support allows Samba oplocks to be broken whenever a local UNIX process or NFS operation accesses a file that smbd 8 has oplocked. This allows complete data consistency between SMB/CIFS, NFS and local file access (and is a very cool feature :-). If you do not need this interaction, you should disable the parameter on Linux to get Level II oplocks and the associated performance benefit. This parameter defaults to no and is translated to a no-op on systems that do not have the necessary kernel support.

### `kernel share modes`

Section: locking; Context: S; Type: boolean; Default: `no`

This parameter controls whether SMB share modes are translated into file system specific sharemode calls. Kernel share modes provide a minimal level of interoperability with local UNIX processes and NFS operations by preventing access corresponding to the SMB share modes. This requires a file system specific VFS module with proper support. Note that in order to use SMB2 durable file handles on a share, you have to turn kernel share modes off. This parameter defaults to no . Setting it to yes requires a file system module that supports file system sharemodes, otherwise attempts to access files will fail with a sharing violation.

### `level2 oplocks`

Section: locking; Context: S; Type: boolean; Default: `yes`

This parameter controls whether Samba supports level2 (read-only) oplocks on a share. Level2, or read-only oplocks allow Windows NT clients that have an oplock on a file to downgrade from a read-write oplock to a read-only oplock once a second client opens the file (instead of releasing all oplocks on a second open, as in traditional, exclusive oplocks). This allows all openers of the file that support level2 oplocks to cache the file for read-ahead only (ie. they may not cache writes or lock requests) and increases performance for many accesses of files that are not commonly written (such as application .EXE files). Once one of the clients which have a read-only oplock writes to the file all clients are notified (no reply is needed or waited for) and told to break their oplocks to "none" and delete any read-ahead caches. It is recommended that this parameter be turned on to speed access to shared executables. For more discussions on level2 oplocks see the CIFS spec. Currently, if are supported then level2 oplocks are not granted (even if this parameter is set to yes ). Note also, the parameter must be set to yes on this share in order for this parameter to have any effect.

### `locking`

Section: locking; Context: S; Type: boolean; Default: `yes`

This controls whether or not locking will be performed by the server in response to lock requests from the client. If locking = no , all lock and unlock requests will appear to succeed and all lock queries will report that the file in question is available for locking. If locking = yes , real locking will be performed by the server. This option may be useful for read-only filesystems which may not need locking (such as CDROM drives), although setting this parameter of no is not really recommended even in this case. Be careful about disabling locking either globally or in a specific service, as lack of locking may result in data corruption. You should never need to set this parameter.

### `lock spin time`

Section: locking; Context: G; Type: integer; Default: `200`

The time in milliseconds that smbd should keep waiting to see if a failed lock request can be granted. This parameter has changed in default value from Samba 3.0.23 from 10 to 200. The associated lock spin count parameter is no longer used in Samba 3.0.24. You should not need to change the value of this parameter.

### `oplock break wait time`

Section: locking; Context: G; Type: integer; Default: `0`

This is a tuning parameter added due to bugs in both Windows 9x and WinNT. If Samba responds to a client too quickly when that client issues an SMB that can cause an oplock break request, then the network client can fail and not respond to the break request. This tuning parameter (which is set in milliseconds) is the amount of time Samba will wait before sending an oplock break request to such (broken) clients. DO NOT CHANGE THIS PARAMETER UNLESS YOU HAVE READ AND UNDERSTOOD THE SAMBA OPLOCK CODE.

### `oplocks`

Section: locking; Context: S; Type: boolean; Default: `yes`

This boolean option tells smbd whether to issue oplocks (opportunistic locks) to file open requests on this share. The oplock code can dramatically (approx. 30% or more) improve the speed of access to files on Samba servers. It allows the clients to aggressively cache files locally and you may want to disable this option for unreliable network environments (it is turned on by default in Windows NT Servers). Oplocks may be selectively turned off on certain files with a share. See the parameter. On some systems oplocks are recognized by the underlying operating system. This allows data synchronization between all access to oplocked files, whether it be via Samba or NFS or a local UNIX process. See the parameter for details.

### `posix locking`

Section: locking; Context: S; Type: boolean; Default: `yes`

The smbd 8 daemon maintains an database of file locks obtained by SMB clients. The default behavior is to map this internal database to POSIX locks. This means that file locks obtained by SMB clients are consistent with those seen by POSIX compliant applications accessing the files via a non-SMB method (e.g. NFS or local file access). It is very unlikely that you need to set this parameter to "no", unless you are sharing from an NFS mount, which is not a good idea in the first place.

### `smb2 leases`

Section: locking; Context: G; Type: boolean; Default: `yes`

This boolean option tells smbd whether to globally negotiate SMB2 leases on file open requests. Leasing is an SMB2-only feature which allows clients to aggressively cache files locally above and beyond the caching allowed by SMB1 oplocks. This is only available with yes and no .

### `smb3 directory leases`

Section: locking; Context: G; Type: enum; Default: `auto`

This is an enumerated type that controls smbd whether SMB3 directory leases are enabled. Directory Leasing is an SMB3-only feature which allows clients to cache directories. Possible values for are yes , no and auto , auto being the default. When set to auto , the effective value depends on the option . If is enabled, are disabled and the other way around. are only available with yes , yes and no . Enabling implicitly enables .

### `strict locking`

Section: locking; Context: S; Type: enum; Default: `Auto`

This is an enumerated type that controls the handling of file locking in the server. When this is set to yes , the server will check every read and write access for file locks, and deny access if locks exist. This can be slow on some systems. When strict locking is set to Auto (the default), the server performs file lock checks only on non-oplocked files. As most Windows redirectors perform file locking checks locally on oplocked files this is a good trade off for improved performance. When strict locking is disabled, the server performs file lock checks only when the client explicitly asks for them. Well-behaved clients always ask for lock checks when it is important. So in the vast majority of cases, strict locking = Auto or strict locking = no is acceptable.
