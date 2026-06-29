# smb.conf Parameters / vfs

### `get quota command`

Section: vfs; Context: G; Type: string

The get quota command should only be used whenever there is no operating system API available from the OS that samba can use. This option is only available Samba was compiled with quotas support. This parameter should specify the path to a script that queries the quota information for the specified user/group for the partition that the specified directory is on. Such a script is being given 3 arguments: directory type of query uid of user or gid of group The directory is actually mostly just "." - It needs to be treated relatively to the current working directory that the script can also query. The type of query can be one of: 1 - user quotas 2 - user default quotas (uid = -1) 3 - group quotas 4 - group default quotas (gid = -1) This script should print one line as output with spaces between the columns. The printed columns should be: 1 - quota flags (0 = no quotas, 1 = quotas enabled, 2 = quotas enabled and enforced) 2 - number of currently used blocks 3 - the softlimit number of blocks 4 - the hardlimit number of blocks 5 - currently used number of inodes 6 - the softlimit number of inodes 7 - the hardlimit number of inodes 8 (optional) - the number of bytes in a block(default is 1024)

### `host msdfs`

Section: vfs; Context: G; Type: boolean; Default: `yes`

If set to yes , Samba will act as a Dfs server, and allow Dfs-aware clients to browse Dfs trees hosted on the server. See also the share level parameter. For more information on setting up a Dfs tree on Samba, refer to the MSFDS chapter in the book Samba3-HOWTO.

### `msdfs proxy`

Section: vfs; Context: S; Type: string

This parameter indicates that the share is a stand-in for another CIFS share whose location is specified by the value of the parameter. When clients attempt to connect to this share, they are redirected to one or multiple, comma separated proxied shares using the SMB-Dfs protocol. Only Dfs roots can act as proxy shares. Take a look at the and options to find out how to set up a Dfs root share.

### `msdfs root`

Section: vfs; Context: S; Type: boolean; Default: `no`

If set to yes , Samba treats the share as a Dfs root and allows clients to browse the distributed file system tree rooted at the share directory. Dfs links are specified in the share directory by symbolic links of the form msdfs:serverA\\shareA,serverB\\shareB and so on. For more information on setting up a Dfs tree on Samba, refer to the MSDFS chapter in the Samba3-HOWTO book.
See also

### `msdfs shuffle referrals`

Section: vfs; Context: S; Type: boolean; Default: `no`

If set to yes , Samba will shuffle Dfs referrals for a given Dfs link if multiple are available, allowing for load balancing across clients. For more information on setting up a Dfs tree on Samba, refer to the MSDFS chapter in the Samba3-HOWTO book.

### `ntvfs handler`

Section: vfs; Context: S; Type: list; Default: `unixuid, default`

This specifies the NTVFS handlers for this share. unixuid: Sets up user credentials based on POSIX gid/uid. cifs: Proxies a remote CIFS FS. Mainly useful for testing. nbench: Filter module that saves data useful to the nbench benchmark suite. ipc: Allows using SMB for inter process communication. Only used for the IPC$ share. posix: Maps POSIX FS semantics to NT semantics print: Allows printing over SMB. This is LANMAN-style printing, not the be confused with the spoolss DCE/RPC interface used by later versions of Windows. Note that this option is only used when the NTVFS file server is in use. It is not used with the (default) s3fs file server.

### `set quota command`

Section: vfs; Context: G; Type: string

The set quota command should only be used whenever there is no operating system API available from the OS that samba can use. This option is only available if Samba was compiled with quota support. This parameter should specify the path to a script that can set quota for the specified arguments. The specified script should take the following arguments: 1 - path to where the quota needs to be set. This needs to be interpreted relative to the current working directory that the script may also check for. 2 - quota type 1 - user quotas 2 - user default quotas (uid = -1) 3 - group quotas 4 - group default quotas (gid = -1) 3 - id (uid for user, gid for group, -1 if N/A) 4 - quota state (0 = disable, 1 = enable, 2 = enable and enforce) 5 - block softlimit 6 - block hardlimit 7 - inode softlimit 8 - inode hardlimit 9(optional) - block size, defaults to 1024 The script should output at least one line of data on success. And nothing on failure.

### `vfs mkdir use tmp name`

Section: vfs; Context: S; Type: enum; Default: `Auto`

Creating a new directory for an SMB client is a very complex task! It includes things like inheriting permissions from the parent directory and storing DOS attributes. Other clients should not see the existence of the directory that is in progress of being created! This option is an enumerated type that controls the usage of a temporary directory name. When this is set to yes , the directory name will be prefixed with '.::TMPNAME:D:$SERVERID:' (where $SERVERID is a unique identifier for the current process). When this option is set to Auto (the default), the server uses a temporary directory name if, at least, one of the following options is effectively not set to no : , , , or . Note on OpenBSD Auto (the default) is mapped to no , see https://bugzilla.samba.org/show_bug.cgi?id=15801 . A re-export of an SMB/CIFS mount might one rare case where vfs mkdir use tmp name = no could be useful. In most cases vfs mkdir use tmp name = Auto should be kept.

### `vfs objects`

Section: vfs; Context: S; Type: cmdlist

This parameter specifies the backend names which are used for Samba VFS I/O operations. By default, normal disk I/O operations are used but these can be overloaded with one or more VFS objects. Be aware that the definition of this parameter will overwrite a possible previous definition of the vfs objects parameter.
