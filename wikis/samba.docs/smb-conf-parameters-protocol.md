# smb.conf Parameters / protocol

### `acl allow execute always`

Section: protocol; Context: S; Type: boolean; Default: `no`

This boolean parameter controls the behaviour of smbd 8 when receiving a protocol request of "open for execution" from a Windows client. With Samba 3.6 and older, the execution right in the ACL was not checked, so a client could execute a file even if it did not have execute rights on the file. In Samba 4.0, this has been fixed, so that by default, i.e. when this parameter is set to "False", "open for execution" is now denied when execution permissions are not present. If this parameter is set to "True", Samba does not check execute permissions on "open for execution", thus re-establishing the behaviour of Samba 3.6. This can be useful to smoothen upgrades from older Samba versions to 4.0 and newer. This setting is not meant to be used as a permanent setting, but as a temporary relief: It is recommended to fix the permissions in the ACLs and reset this parameter to the default after a certain transition period.

### `acl check permissions`

Section: protocol; Context: S; Type: boolean; Default: `yes`

Please note this parameter is now deprecated in Samba 3.6.2 and will be removed in a future version of Samba. This boolean parameter controls what smbd 8 does on receiving a protocol request of "open for delete" from a Windows client. If a Windows client doesn't have permissions to delete a file then they expect this to be denied at open time. POSIX systems normally only detect restrictions on delete by actually attempting to delete the file or directory. As Windows clients can (and do) "back out" a delete request by unsetting the "delete on close" bit Samba cannot delete the file immediately on "open for delete" request as we cannot restore such a deleted file. With this parameter set to true (the default) then smbd checks the file system permissions directly on "open for delete" and denies the request without actually deleting the file if the file system permissions would seem to deny it. This is not perfect, as it's possible a user could have deleted a file without Samba being able to check the permissions correctly, but it is close enough to Windows semantics for mostly correct behaviour. Samba will correctly check POSIX ACL semantics in this case. If this parameter is set to "false" Samba doesn't check permissions on "open for delete" and allows the open. If the user doesn't have permission to delete the file this will only be discovered at close time, which is too late for the Windows user tools to display an error message to the user. The symptom of this is files that appear to have been deleted "magically" re-appearing on a Windows explorer refresh. This is an extremely advanced protocol option which should not need to be changed. This parameter was introduced in its final form in 3.0.21, an earlier version with slightly different semantics was introduced in 3.0.20. That older version is not documented here.

### `acl map full control`

Section: protocol; Context: S; Type: boolean; Default: `yes`

This boolean parameter controls whether smbd 8 maps a POSIX ACE entry of "rwx" (read/write/execute), the maximum allowed POSIX permission set, into a Windows ACL of "FULL CONTROL". If this parameter is set to true any POSIX ACE entry of "rwx" will be returned in a Windows ACL as "FULL CONTROL", is this parameter is set to false any POSIX ACE entry of "rwx" will be returned as the specific Windows ACL bits representing read, write and execute.

### `ad dc functional level`

Section: protocol; Context: G; Type: enum; Default: `2008_R2`

The value of the parameter (a string) is the Active Directory functional level that this Domain Controller will claim to support. Possible values are : 2008_R2 : Similar to Windows 2008 R2 Functional Level 2012 : Similar to Windows 2012 Functional Level 2012_R2 : Similar to Windows 2012 R2 Functional Level 2016 : Similar to Windows 2016 Functional Level Normally this option should not be set as Samba will operate per the released functionality of the Samba Active Directory Domain Controller. However to access incomplete features in domain functional level 2016 it may be useful to set this value, prior to upgrading the domain functional level. If this is set manually, the protection against mismatching features between domain controllers is reduced, so all domain controllers should be running the same version of Samba, to ensure that behaviour as seen by the client is the same no matter which DC is contacted. Setting this to 2016 will allow raising the domain functional level with samba-tool domain level raise --domain-level=2016 and provide access to Samba's Kerberos Claims and Dynamic Access Control feature. The Samba's Kerberos Claims and Dynamic Access Control features enabled with 2016 are incomplete in Samba 4.19.

### `client ipc max protocol`

Section: protocol; Context: G; Type: enum; Default: `default`

The value of the parameter (a string) is the highest protocol level that will be supported for IPC$ connections as DCERPC transport. Normally this option should not be set as the automatic negotiation phase in the SMB protocol takes care of choosing the appropriate protocol. The value default refers to the latest supported protocol, currently SMB3_11 . See for a full list of available protocols. The values CORE, COREPLUS, LANMAN1, LANMAN2 are silently upgraded to NT1.

### `client ipc min protocol`

Section: protocol; Context: G; Type: enum; Default: `default`

This setting controls the minimum protocol version that the will be attempted to use for IPC$ connections as DCERPC transport. Normally this option should not be set as the automatic negotiation phase in the SMB protocol takes care of choosing the appropriate protocol. The value default refers to the higher value of NT1 and the effective value of . See for a full list of available protocols. The values CORE, COREPLUS, LANMAN1, LANMAN2 are silently upgraded to NT1.

### `client max protocol`

Section: protocol; Context: G; Type: enum; Default: `default`

The value of the parameter (a string) is the highest protocol level that will be supported by the client. Possible values are : CORE : Earliest version. No concept of user names. COREPLUS : Slight improvements on CORE for efficiency. LANMAN1 : First modern version of the protocol. Long filename support. LANMAN2 : Updates to Lanman1 protocol. NT1 : Current up to date version of the protocol. Used by Windows NT. Known as CIFS. SMB2 : Re-implementation of the SMB protocol. Used by Windows Vista and later versions of Windows. SMB2 has sub protocols available. SMB2_02 : The earliest SMB2 version. SMB2_10 : Windows 7 SMB2 version. By default SMB2 selects the SMB2_10 variant. SMB3 : The same as SMB2. Used by Windows 8. SMB3 has sub protocols available. SMB3_00 : Windows 8 SMB3 version. SMB3_02 : Windows 8.1 SMB3 version. SMB3_11 : Windows 10 SMB3 version. By default SMB3 selects the SMB3_11 variant. Normally this option should not be set as the automatic negotiation phase in the SMB protocol takes care of choosing the appropriate protocol. The value default refers to SMB3_11 . IPC$ connections for DCERPC e.g. in winbindd, are handled by the option.

### `client min protocol`

Section: protocol; Context: G; Type: enum; Default: `SMB2_02`

This setting controls the minimum protocol version that the client will attempt to use. Normally this option should not be set as the automatic negotiation phase in the SMB protocol takes care of choosing the appropriate protocol unless you connect to a legacy SMB1-only server. See client max protocol for a full list of available protocols. IPC$ connections for DCERPC e.g. in winbindd, are handled by the option. Note that most command line tools support --option='client min protocol=NT1', so it may not be required to enable SMB1 protocols globally in smb.conf.

### `client smb transports`

Section: protocol; Context: G; Type: list; Default: `tcp, nbt`

Specifies which transports and ports the client should try to connect to for SMB traffic. The order matters as they are tried in order with short delays for the fallbacks. The transport 'tcp' uses raw tcp with a 4 byte length header per SMB PDU. The default port for 'tcp' is 445. Other ports can be specified by adding it after ':', e.g. 'tcp:1445'. The transport 'nbt' uses netbios framing on top of tcp per SMB PDU. The default port for 'nbt' is 139. Other ports can be specified by adding it after ':', e.g. 'nbt:1139'. The transport 'quic' uses the quic protocol on top of udp. The default port for 'quic' is 443. Other ports can be specified by adding it after ':', e.g. 'quic:1443'. The following options are also relevant: , , , , , and . Note: 'quic' requires the quic.ko kernel module for Linux from https://github.com/lxin/quic (tested with Linux 6.14). Future Linux versions may support it natively. Numerical ports are handled as 'tcp' except port '139' is handled as 'nbt'. Note that's currently a limit of 10 unique transports, all others will be ignored.

### `client use spnego`

Section: protocol; Context: G; Type: boolean; Default: `yes`

This parameter has been deprecated since Samba 4.13 and support for NTLMv2, NTLM and LanMan authentication outside NTLMSSP will be removed in a future Samba release. That is, in the future, the current default of client use spnego = yes will be the enforced behaviour. This variable controls whether Samba clients will try to use Simple and Protected NEGOtiation (as specified by rfc2478) with supporting servers (including WindowsXP, Windows2000 and Samba 3.0) to agree upon an authentication mechanism. This enables Kerberos authentication in particular. When is also set to yes extended security (SPNEGO) is required in order to use NTLMv2 only within NTLMSSP. This behavior was introduced with the patches for CVE-2016-2111.

### `dcerpc endpoint servers`

Section: protocol; Context: G; Type: list; Default: `epmapper, samr, netlogon, lsarpc, drsuapi, dssetup, unixinfo, browser, eventlog6, backupkey, dnsserver`

Specifies which DCE/RPC endpoint servers should be run.

### `defer sharing violations`

Section: protocol; Context: G; Type: boolean; Default: `yes`

Windows allows specifying how a file will be shared with other processes when it is opened. Sharing violations occur when a file is opened by a different process using options that violate the share settings specified by other processes. This parameter causes smbd to act as a Windows server does, and defer returning a "sharing violation" error message for up to one second, allowing the client to close the file causing the violation in the meantime. UNIX by default does not have this behaviour. There should be no reason to turn off this parameter, as it is designed to enable Samba to more correctly emulate Windows.

### `dgram port`

Section: protocol; Context: G; Type: integer; Default: `138`

Specifies which ports the server should listen on for NetBIOS datagram traffic.
This parameter is deprecated, as it is not honoured in the majority of the code base.

### `disable netbios`

Section: protocol; Context: G; Type: boolean; Default: `no`

Enabling this parameter will disable netbios support in Samba. Netbios is the only available form of browsing in Windows versions prior to Windows 2000. Clients that only support netbios won't be able to see your samba server when netbios support is disabled.

### `dns port`

Section: protocol; Context: G; Type: integer; Default: `53`

Specifies which ports the server should listen on for DNS traffic. It makes possible to use another DNS server as a front and forward to Samba. Dynamic DNS updates may not be proxied by the front DNS server when forwarding to Samba. Dynamic DNS update proxying depends on the features of the other DNS server used as a front.

### `durable handles`

Section: protocol; Context: S; Type: boolean; Default: `yes`

This boolean parameter controls whether Samba can grant SMB2 durable file handles on a share. Note that durable handles are only enabled if no , no , and no , i.e. if the share is configured for CIFS/SMB2 only access, not supporting interoperability features with local UNIX processes or NFS operations. Also note that, for the time being, durability is not granted for a handle that has the delete on close flag set.

### `ea support`

Section: protocol; Context: S; Type: boolean; Default: `yes`

This boolean parameter controls whether smbd 8 will allow clients to attempt to access extended attributes on a share. In order to enable this parameter on a setup with default VFS modules: Samba must have been built with extended attributes support. The underlying filesystem exposed by the share must support extended attributes (e.g. the getfattr 1 / setfattr 1 utilities must work). Access to extended user attributes must be allowed by the underlying filesystem (e.g. when mounted with a system-dependent option like user_xattr on Linux). This option exposes the "user" attribute namespace from the underlying filesystem to clients. In order to match Windows conventions, the namespace prefix ("user.") is stripped from the attribute name on the client side. The handling of further attribute namespaces (like "security", "system", or "trusted") is not affected by this option. Note that the SMB protocol allows setting attributes whose value is 64K bytes long, and that on NTFS, the maximum storage space for extended attributes per file is 64K. On some filesystem the limits may be lower. Filesystems with too limited EA space may experience unexpected weird effects. The default has changed to yes in Samba release 4.9.0 and above to allow better Windows fileserver compatibility in a default install.

### `enable asu support`

Section: protocol; Context: G; Type: boolean; Default: `no`

Hosts running the "Advanced Server for Unix (ASU)" product require some special accommodations such as creating a builtin [ADMIN$] share that only supports IPC connections. The has been the default behavior in smbd for many years. However, certain Microsoft applications such as the Print Migrator tool require that the remote server support an [ADMIN$] file share. Disabling this parameter allows for creating an [ADMIN$] file share in smb.conf.

### `eventlog list`

Section: protocol; Context: G; Type: cmdlist

This option defines a list of log names that Samba will report to the Microsoft EventViewer utility. The listed eventlogs will be associated with tdb file on disk in the $(statedir)/eventlog . The administrator must use an external process to parse the normal Unix logs such as /var/log/messages and write then entries to the eventlog tdb files. Refer to the eventlogadm(8) utility for how to write eventlog entries.

### `large readwrite`

Section: protocol; Context: G; Type: boolean; Default: `yes`

This parameter determines whether or not smbd 8 supports the new 64k streaming read and write variant SMB requests introduced with Windows 2000. Note that due to Windows 2000 client redirector bugs this requires Samba to be running on a 64-bit capable operating system such as IRIX, Solaris or a Linux 2.4 kernel. Can improve performance by 10% with Windows 2000 clients. Defaults to on. Not as tested as some other Samba code paths.

### `lsa over netlogon`

Section: protocol; Context: G; Type: boolean; Default: `no`

Setting this deprecated option will allow the RPC server in the AD DC to answer the LSARPC interface on the \pipe\netlogon IPC pipe. When enabled, this matches the behaviour of Microsoft's Windows, due to their internal implementation choices. If it is disabled (the default), the AD DC can offer improved performance, as the netlogon server is decoupled and can run as multiple processes.

### `map acl inherit`

Section: protocol; Context: S; Type: boolean; Default: `no`

This boolean parameter is only relevant for systems that do not support standardized NFS4 ACLs but only a POSIX draft implementation of ACLs. Linux is the only common UNIX system which does still not offer standardized NFS4 ACLs actually. On such systems this parameter controls whether smbd 8 will attempt to map the 'protected' (don't inherit) flags of the Windows ACLs into an extended attribute called user.SAMBA_PAI (POSIX draft ACL Inheritance). This parameter requires support for extended attributes on the filesystem and allows the Windows ACL editor to store (non-)inheritance information while NT ACLs are mapped best-effort to the POSIX draft ACLs that the OS and filesystem implements.

### `max mux`

Section: protocol; Context: G; Type: integer; Default: `50`

This option controls the maximum number of outstanding simultaneous SMB operations that Samba tells the client it will allow. You should never need to set this parameter.

### `max ttl`

Section: protocol; Context: G; Type: integer; Default: `259200`

This option tells nmbd 8 what the default 'time to live' of NetBIOS names should be (in seconds) when nmbd is requesting a name using either a broadcast packet or from a WINS server. You should never need to change this parameter. The default is 3 days.

### `max xmit`

Section: protocol; Context: G; Type: bytes; Default: `16644`

This option controls the maximum packet size that will be negotiated by Samba's smbd 8 for the SMB1 protocol. The default is 16644, which matches the behavior of Windows 2000. A value below 2048 is likely to cause problems. You should never need to change this parameter from its default value.

### `min receivefile size`

Section: protocol; Context: G; Type: bytes; Default: `0`

This option changes the behavior of smbd 8 when processing SMBwriteX calls. Any incoming SMBwriteX call on a non-signed SMB/CIFS connection greater than this value will not be processed in the normal way but will be passed to any underlying kernel recvfile or splice system call (if there is no such call Samba will emulate in user space). This allows zero-copy writes directly from network socket buffers into the filesystem buffer cache, if available. It may improve performance but user testing is recommended. If set to zero Samba processes SMBwriteX calls in the normal way. To enable POSIX large write support (SMB/CIFS writes up to 16Mb) this option must be nonzero. The maximum value is 128k. Values greater than 128k will be silently set to 128k. Note this option will have NO EFFECT if set on a SMB signed connection. The default is zero, which disables this option.

### `nbt port`

Section: protocol; Context: G; Type: integer; Default: `137`

Specifies which port the server should use for NetBIOS over IP name services traffic.
This parameter is deprecated, as it is not honoured in the majority of the code base.

### `nt acl support`

Section: protocol; Context: S; Type: boolean; Default: `yes`

This boolean parameter controls whether smbd 8 will attempt to map UNIX permissions into Windows NT access control lists. The UNIX permissions considered are the traditional UNIX owner and group permissions, as well as filesystem ACLs set on any files or directories. This parameter was formally a global parameter in releases prior to 2.2.2.

### `nt pipe support`

Section: protocol; Context: G; Type: boolean; Default: `yes`

This boolean parameter controls whether smbd 8 will allow Windows NT clients to connect to the NT SMB specific IPC$ pipes. This is a developer debugging option and can be left alone.

### `nt status support`

Section: protocol; Context: G; Type: boolean; Default: `yes`

This boolean parameter controls whether smbd 8 will negotiate NT specific status support with Windows NT/2k/XP clients. This is a developer debugging option and should be left alone. If this option is set to no then Samba offers exactly the same DOS error codes that versions prior to Samba 2.2.3 reported. You should not need to ever disable this parameter.

### `read raw`

Section: protocol; Context: G; Type: boolean; Default: `yes`

This is ignored if is set, because this feature is incompatible with raw read SMB requests If enabled, raw reads allow reads of 65535 bytes in one packet. This typically provides a major performance benefit for some very, very old clients. However, some clients either negotiate the allowable block size incorrectly or are incapable of supporting larger block sizes, and for these clients you may need to disable raw reads. In general this parameter should be viewed as a system tuning tool and left severely alone.

### `rpc big endian`

Section: protocol; Context: G; Type: boolean; Default: `no`

Setting this option will force the RPC client and server to transfer data in big endian. If it is disabled, data will be transferred in little endian. The behaviour is independent of the endianness of the host machine.

### `rpc server port`

Section: protocol; Context: G; Type: integer; Default: `0`

Specifies which port the server should listen on for DCE/RPC over TCP/IP traffic. This controls the default port for all protocols, except for NETLOGON. If unset, the first available port from is used, e.g. 49152. The NETLOGON server will use the next available port, e.g. 49153. To change this port use (eg) rpc server port:netlogon = 4000. Furthermore, all RPC servers can have the port they use specified independenty, with (for example) rpc server port:drsuapi = 5000. This option applies currently only when samba 8 runs as an active directory domain controller. The default value 0 causes Samba to select the first available port from .

### `server max protocol`

Section: protocol; Context: G; Type: enum; Default: `SMB3`

The value of the parameter (a string) is the highest protocol level that will be supported by the server. Possible values are : LANMAN1 : First modern version of the protocol. Long filename support. LANMAN2 : Updates to Lanman1 protocol. NT1 : Current up to date version of the protocol. Used by Windows NT. Known as CIFS. SMB2 : Re-implementation of the SMB protocol. Used by Windows Vista and later versions of Windows. SMB2 has sub protocols available. SMB2_02 : The earliest SMB2 version. SMB2_10 : Windows 7 SMB2 version. By default SMB2 selects the SMB2_10 variant. SMB3 : The same as SMB2. Used by Windows 8. SMB3 has sub protocols available. SMB3_00 : Windows 8 SMB3 version. SMB3_02 : Windows 8.1 SMB3 version. SMB3_11 : Windows 10 SMB3 version. By default SMB3 selects the SMB3_11 variant. Normally this option should not be set as the automatic negotiation phase in the SMB protocol takes care of choosing the appropriate protocol.

### `server min protocol`

Section: protocol; Context: G; Type: enum; Default: `SMB2_02`

This setting controls the minimum protocol version that the server will allow the client to use. Normally this option should not be set as the automatic negotiation phase in the SMB protocol takes care of choosing the appropriate protocol unless you have legacy clients which are SMB1 capable only. See server max protocol for a full list of available protocols.

### `server multi channel support`

Section: protocol; Context: G; Type: boolean; Default: `yes`

This boolean parameter controls whether smbd 8 will support SMB3 multi-channel. This parameter was added with version 4.4. Note that this feature was still considered experimental up to 4.14. Due to dependencies to kernel APIs of Linux or FreeBSD, it's only possible to use this feature on Linux and FreeBSD for now. For testing this restriction can be overwritten by specifying force:server multi channel support=yes in addition. This option is enabled by default starting with to 4.15 (on Linux and FreeBSD).

### `share:fake_fscaps`

Section: protocol; Context: S; Type: string; Default: `0`

This is needed to support some special applications that makes use of filesystem specific features like sparse files or block reflink copy. With 64 the SPARSE_FILES (0x40) file system capability flag is set. With 134217728 the SUPPORTS_BLOCK_REFCOUNTING (0x8000000) file system capability flag is set. As of this writing, filesystems that support this feature are BTRFS, XFS and ZFS. The complete list can be found in MS-FSCC 2.5.1 FileFsAttributeInformation. Note that only decimal values can be used in the configuration.

### `smb1 unix extensions`

Section: protocol; Context: G; Type: boolean; Default: `yes`

This boolean parameter controls whether Samba implements the SMB1/CIFS UNIX extensions, as defined by HP. These extensions enable Samba to better serve UNIX SMB1/CIFS clients by supporting features such as symbolic links, hard links, etc... These extensions require a similarly enabled client, and are of no current use to Windows clients. Note if this parameter is turned on, the parameter will automatically be disabled. See the parameter if you wish to change this coupling between the two parameters.

### `smb2 disable lock sequence checking`

Section: protocol; Context: G; Type: boolean; Default: `no`

This boolean parameter controls whether smbd 8 will disable lock sequence checking even for multi-channel connections as well as durable handles. The [MS-SMB2] specification (under 3.3.5.14 Receiving an SMB2 LOCK Request) documents that a server should do lock sequence if Open.IsResilient or Open.IsDurable or Open.IsPersistent is TRUE or if Connection.Dialect belongs to the SMB 3.x dialect family and Connection.ServerCapabilities includes SMB2_GLOBAL_CAP_MULTI_CHANNEL. But Windows Server (at least up to v2004) only does these checks for the Open.IsResilient and Open.IsPersistent. That means they do not implement the behavior specified in [MS-SMB2]. By default Samba behaves according to the specification and implements lock sequence checking when multi-channel is used. Warning: Only enable this option if existing clients can't handle lock sequence checking for handles without Open.IsResilient and Open.IsPersistent. And it turns out that the Windows Server behavior is required. Note: it's likely that this option will be removed again if future Windows versions change their behavior. Note: Samba does not implement Open.IsResilient and Open.IsPersistent yet.

### `smb2 disable oplock break retry`

Section: protocol; Context: G; Type: boolean; Default: `no`

This boolean parameter controls whether smbd 8 will trigger smb2 oplock break notification retries when using yes . The [MS-SMB2] specification documents that a server should send smb2 oplock break notification retries on all available channel to the given client. But Windows Server versions (at least up to 2019) do not send smb2 oplock break notification retries on channel failures. That means they do not implement the behavior specified in [MS-SMB2]. By default Samba behaves according to the specification and send smb2 oplock break notification retries. Warning: Only enable this option if existing clients can't handle possible retries and it turns out that the Windows Server behavior is required. Note: it's likely that this option gets removed again if future Windows versions change their behavior. Note: this only applies to oplocks and not SMB2 leases.

### `smb2 max credits`

Section: protocol; Context: G; Type: integer; Default: `8192`

This option controls the maximum number of outstanding simultaneous SMB2 operations that Samba tells the client it will allow. This is similar to the parameter for SMB1. You should never need to set this parameter. The default is 8192 credits, which is the same as a Windows 2008R2 SMB2 server.

### `smb2 max read`

Section: protocol; Context: G; Type: bytes; Default: `8388608`

This option specifies the protocol value that smbd 8 will return to a client, informing the client of the largest size that may be returned by a single SMB2 read call. The maximum is 8388608 bytes (8MiB), which is the same as a Windows Server 2012 r2. Please note that the default is 8MiB, but it's limit is based on the smb2 dialect (64KiB for SMB == 2.0, 8MiB for SMB >= 2.1 with LargeMTU). Large MTU is not supported over NBT (tcp port 139).

### `smb2 max trans`

Section: protocol; Context: G; Type: bytes; Default: `8388608`

This option specifies the protocol value that smbd 8 will return to a client, informing the client of the largest size of buffer that may be used in querying file meta-data via QUERY_INFO and related SMB2 calls. The maximum is 8388608 bytes (8MiB), which is the same as a Windows Server 2012 r2. Please note that the default is 8MiB, but it's limit is based on the smb2 dialect (64KiB for SMB == 2.0, 1MiB for SMB >= 2.1 with LargeMTU). Large MTU is not supported over NBT (tcp port 139).

### `smb2 max write`

Section: protocol; Context: G; Type: bytes; Default: `8388608`

This option specifies the protocol value that smbd 8 will return to a client, informing the client of the largest size that may be sent to the server by a single SMB2 write call. The maximum is 8388608 bytes (8MiB), which is the same as a Windows Server 2012 r2. Please note that the default is 8MiB, but it's limit is based on the smb2 dialect (64KiB for SMB == 2.0, 8MiB for SMB => 2.1 with LargeMTU). Large MTU is not supported over NBT (tcp port 139).

### `smb3 unix extensions`

Section: protocol; Context: S; Type: boolean; Default: `yes`

Support for SMB 3.1.1 Unix Extensions.

### `svcctl list`

Section: protocol; Context: G; Type: cmdlist

This option defines a list of init scripts that smbd will use for starting and stopping Unix services via the Win32 ServiceControl API. This allows Windows administrators to utilize the MS Management Console plug-ins to manage a Unix server running Samba. The administrator must create a directory name svcctl in Samba's $(libdir) and create symbolic links to the init scripts in /etc/init.d/ . The name of the links must match the names given as part of the svcctl list .

### `time server`

Section: protocol; Context: G; Type: boolean; Default: `no`

This parameter determines if nmbd 8 advertises itself as a time server to Windows clients.

### `unicode`

Section: protocol; Context: G; Type: boolean; Default: `yes`

Specifies whether the server and client should support unicode. If this option is set to false, the use of ASCII will be forced.

### `write raw`

Section: protocol; Context: G; Type: boolean; Default: `yes`

This is ignored if is set, because this feature is incompatible with raw write SMB requests If enabled, raw writes allow writes of 65535 bytes in one packet. This typically provides a major performance benefit for some very, very old clients. However, some clients either negotiate the allowable block size incorrectly or are incapable of supporting larger block sizes, and for these clients you may need to disable raw writes. In general this parameter should be viewed as a system tuning tool and left severely alone.
