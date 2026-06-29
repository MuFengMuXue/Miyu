# smb.conf Parameters / security

### `access based share enum`

Section: security; Context: S; Type: boolean; Default: `no`

If this parameter is yes for a service, then the share hosted by the service will only be visible to users who have read or write access to the share during share enumeration (for example net view \\sambaserver). The share ACLs which allow or deny the access to the share can be modified using for example the sharesec command or using the appropriate Windows tools. This has parallels to access based enumeration, the main difference being that only share permissions are evaluated, and security descriptors on files contained on the share are not used in computing enumeration access rights.

### `acl claims evaluation`

Section: security; Context: G; Type: enum; Default: `AD DC only`

This option controls the way Samba handles evaluation of security descriptors in Samba, with regards to Active Directory Claims. AD Claims, introduced with Windows 2012, are essentially administrator-defined key-value pairs that can be set both in Active Directory (communicated via the Kerberos PAC) and in the security descriptor themselves. Active Directory claims are new with Samba 4.20. Because the claims are evaluated against a very flexible expression language within the security descriptor, this option provides a mechanism to disable this logic if required by the administrator. This default behaviour is that claims evaluation is enabled in the AD DC only. Additionally, claims evaluation on the AD DC is only enabled if the DC functional level is 2012 or later. See . Possible values are : AD DC only : Enabled for the Samba AD DC (for DC functional level 2012 or higher). never : Disabled in all cases. This option disables some but not all of the Authentication Policies and Authentication Policy Silos features of the Windows 2012R2 functional level in the AD DC.

### `acl flag inherited canonicalization`

Section: security; Context: S; Type: boolean; Default: `yes`

This option controls the way Samba handles client requests setting the Security Descriptor of files and directories and the effect the operation has on the Security Descriptor flag "DACL auto-inherited" (DI). Generally, this flag is set on a file (or directory) upon creation if the parent directory has DI set and also has inheritable ACEs. On the other hand when a Security Descriptor is explicitly set on a file, the DI flag is cleared, unless the flag "DACL Inheritance Required" (DR) is also set in the new Security Descriptor (fwiw, DR is never stored on disk). This is the default behaviour when this option is enabled (the default). When setting this option to no , the resulting value of the DI flag on-disk is directly taken from the DI value of the to-be-set Security Descriptor. This can be used so dump tools like rsync that copy data blobs from xattrs that represent ACLs created by the acl_xattr VFS module will result in copies of the ACL that are identical to the source. Without this option, the copied ACLs would all lose the DI flag if set on the source.

### `acl group control`

Section: security; Context: S; Type: boolean; Default: `no`

In a POSIX filesystem, only the owner of a file or directory and the superuser can modify the permissions and ACLs on a file. If this parameter is set, then Samba overrides this restriction, and also allows the primary group owner of a file or directory to modify the permissions and ACLs on that file. On a Windows server, groups may be the owner of a file or directory - thus allowing anyone in that group to modify the permissions on it. This allows the delegation of security controls on a point in the filesystem to the group owner of a directory and anything below it also owned by that group. This means there are multiple people with permissions to modify ACLs on a file or directory, easing manageability. This parameter allows Samba to also permit delegation of the control over a point in the exported directory hierarchy in much the same way as Windows. This allows all members of a UNIX group to control the permissions on a file or directory they have group ownership on. This parameter is best used with the option and also on a share containing directories with the UNIX setgid bit set on them, which causes new files and directories created within it to inherit the group ownership from the containing directory. This parameter was deprecated in Samba 3.0.23, but re-activated in Samba 3.0.31 and above, as it now only controls permission changes if the user is in the owning primary group. It is now no longer equivalent to the dos filemode option.

### `admin users`

Section: security; Context: S; Type: cmdlist

This is a list of users who will be granted administrative privileges on the share. This means that they will do all file operations as the super-user (root). You should use this option very carefully, as any user in this list will be able to do anything they like on the share, irrespective of file permissions.

### `algorithmic rid base`

Section: security; Context: G; Type: integer; Default: `1000`

This determines how Samba will use its algorithmic mapping from uids/gid to the RIDs needed to construct NT Security Identifiers. Setting this option to a larger value could be useful to sites transitioning from WinNT and Win2k, as existing user and group rids would otherwise clash with system users etc. All UIDs and GIDs must be able to be resolved into SIDs for the correct operation of ACLs on the server. As such the algorithmic mapping can't be 'turned off', but pushing it 'out of the way' should resolve the issues. Users and groups can then be assigned 'low' RIDs in arbitrary-rid supporting backends.

### `allow dcerpc auth level connect`

Section: security; Context: G; Type: boolean; Default: `no`

This option controls whether DCERPC services are allowed to be used with DCERPC_AUTH_LEVEL_CONNECT, which provides authentication, but no per message integrity nor privacy protection. Some interfaces like samr, lsarpc and netlogon have a hard-coded default of no and epmapper, mgmt and rpcecho have a hard-coded default of yes . The behavior can be overwritten per interface name (e.g. lsarpc, netlogon, samr, srvsvc, winreg, wkssvc ...) by using 'allow dcerpc auth level connect:interface = yes' as option. This option is over-ridden by the implementation specific restrictions. E.g. the drsuapi and backupkey protocols require DCERPC_AUTH_LEVEL_PRIVACY. The dnsserver protocol requires DCERPC_AUTH_LEVEL_INTEGRITY. This option should not be used, it's related to CVE-2016-2118. It will be removed in future releases.

### `allow trusted domains`

Section: security; Context: G; Type: boolean; Default: `yes`

This option only takes effect when the option is set to server , domain or ads . If it is set to no, then attempts to connect to a resource from a domain or workgroup other than the one which smbd is running in will fail, even if that domain is trusted by the remote server doing the authentication. This is useful if you only want your Samba server to serve resources to users in the domain it is a member of. As an example, suppose that there are two domains DOMA and DOMB. DOMB is trusted by DOMA, which contains the Samba server. Under normal circumstances, a user with an account in DOMB can then access the resources of a UNIX account with the same account name on the Samba server even if they do not have an account in DOMA. This can make implementing a security boundary difficult.

### `binddns dir`

Section: security; Context: G; Type: string

This parameters defines the directory samba will use to store the configuration files for bind, such as named.conf. NOTE: The bind dns directory needs to be on the same mount point as the private directory!

### `check password script`

Section: security; Context: G; Type: string; Default: `Disabled`

The name of a program that can be used to check password complexity. The password is sent to the program's standard input. The program must return 0 on a good password, or any other value if the password is bad. In case the password is considered weak (the program does not return 0) the user will be notified and the password change will fail. In Samba AD, this script will be run AS ROOT by samba 8 without any substitutions. Note that starting with Samba 4.11 the following environment variables are exported to the script: SAMBA_CPS_ACCOUNT_NAME is always present and contains the sAMAccountName of user, the is the same as the %u substitutions in the none AD DC case. SAMBA_CPS_USER_PRINCIPAL_NAME is optional in the AD DC case if the userPrincipalName is present. SAMBA_CPS_FULL_NAME is optional if the displayName is present. Note: In the example directory is a sample program called crackcheck that uses cracklib to check the password quality.

### `client ipc signing`

Section: security; Context: G; Type: enum; Default: `default`

This controls whether the client is allowed or required to use SMB signing for IPC$ connections as DCERPC transport. Possible values are desired , required and disabled . When set to required or default, SMB signing is mandatory. When set to desired, SMB signing is offered, but not enforced and if set to disabled, SMB signing is not offered either. Connections from winbindd to Active Directory Domain Controllers always enforce signing.

### `client lanman auth`

Section: security; Context: G; Type: boolean; Default: `no`

This parameter has been deprecated since Samba 4.13 and support for LanMan (as distinct from NTLM, NTLMv2 or Kerberos) authentication as a client will be removed in a future Samba release. That is, in the future, the current default of client NTLMv2 auth = yes will be the enforced behaviour. This parameter determines whether or not smbclient 8 and other samba client tools will attempt to authenticate itself to servers using the weaker LANMAN password hash. If disabled, only server which support NT password hashes (e.g. Windows NT/2000, Samba, etc... but not Windows 95/98) will be able to be connected from the Samba client. The LANMAN encrypted response is easily broken, due to its case-insensitive nature, and the choice of algorithm. Clients without Windows 95/98 servers are advised to disable this option. Disabling this option will also disable the client plaintext auth option. Likewise, if the client ntlmv2 auth parameter is enabled, then only NTLMv2 logins will be attempted.

### `client netlogon ping protocol`

Section: security; Context: G; Type: enum; Default: `CLDAP`

This option controls the protocol Samba uses to issue netlogon ping requests. This is normally done via connectionless ldap, but some installations require LDAPS over TCP port 636 for this. Possible values are : CLDAP LDAP LDAPS STARTTLS

### `client plaintext auth`

Section: security; Context: G; Type: boolean; Default: `no`

This parameter has been deprecated since Samba 4.13 and support for plaintext (as distinct from NTLM, NTLMv2 or Kerberos authentication) will be removed in a future Samba release. That is, in the future, the current default of client plaintext auth = no will be the enforced behaviour. Specifies whether a client should send a plaintext password if the server does not support encrypted passwords.

### `client protection`

Section: security; Context: G; Type: enum; Default: `default`

This parameter defines which protection Samba client tools should use by default. Possible client settings are: default - Use the individual default values of the options: client signing client smb encrypt plain - This will send everything just as plaintext, signing or encryption are turned off. sign - This will enable integrity checking. encrypt - This will enable integrity checks and force encryption for privacy.

### `client schannel`

Section: security; Context: G; Type: enum; Default: `yes`

This option is deprecated with Samba 4.8 and will be removed in future. At the same time the default changed to yes, which will be the hardcoded behavior in future. This controls whether the client offers or even demands the use of the netlogon schannel. no does not offer the schannel, auto offers the schannel but does not enforce it, and yes denies access if the server is not able to speak netlogon schannel. Note that for active directory domains this is hardcoded to yes . This option is over-ridden by the option.

### `client signing`

Section: security; Context: G; Type: enum; Default: `default`

This controls whether the client is allowed or required to use SMB signing. Possible values are desired , required and disabled . When set to desired or default, SMB signing is offered, but not enforced. When set to required, SMB signing is mandatory and if set to disabled, SMB signing is not offered either. IPC$ connections for DCERPC e.g. in winbindd, are handled by the option.

### `client smb encrypt`

Section: security; Context: G; Type: enum; Default: `default`

This parameter controls whether a client should try or is required to use SMB encryption. It has different effects depending on whether the connection uses SMB1 or SMB3: If the connection uses SMB1, then this option controls the use of a Samba-specific extension to the SMB protocol introduced in Samba 3.2 that makes use of the Unix extensions. If the connection uses SMB2 or newer, then this option controls the use of the SMB-level encryption that is supported in SMB version 3.0 and above and available in Windows 8 and newer. This parameter can be set globally. Possible values are off , if_required , desired , and required . A special value is default which is the implicit default setting of if_required . Effects for SMB1 The Samba-specific encryption of SMB1 connections is an extension to the SMB protocol negotiated as part of the UNIX extensions. SMB encryption uses the GSSAPI (SSPI on Windows) ability to encrypt and sign every request/response in a SMB protocol stream. When enabled it provides a secure method of SMB/CIFS communication, similar to an ssh protected session, but using SMB/CIFS authentication to negotiate encryption and signing keys. Currently this is only supported smbclient of by Samba 3.2 and newer. Windows does not support this feature. When set to default, SMB encryption is probed, but not enforced. When set to required, SMB encryption is required and if set to disabled, SMB encryption can not be negotiated. Effects for SMB3 and newer Native SMB transport encryption is available in SMB version 3.0 or newer. It is only used by Samba if client max protocol is set to SMB3 or newer. These features can be controlled with settings of client smb encrypt as follows: Leaving it as default, explicitly setting default , or setting it to if_required globally will enable negotiation of encryption but will not turn on data encryption globally. Setting it to desired globally will enable negotiation and will turn on data encryption on sessions and share connections for those servers that support it. Setting it to required globally will enable negotiation and turn on data encryption on sessions and share connections. Clients that do not support encryption will be denied access to the server. Setting it to off globally will completely disable the encryption feature for all connections.

### `client smb3 encryption algorithms`

Section: security; Context: G; Type: list; Default: `AES-128-GCM, AES-128-CCM, AES-256-GCM, AES-256-CCM`

This parameter specifies the availability and order of encryption algorithms which are available for negotiation in the SMB3_11 dialect. It is also possible to remove individual algorithms from the default list, by prefixing them with '-'. This can avoid having to specify a hardcoded list. Note: that the removal of AES-128-CCM from the list will result in SMB3_00 and SMB3_02 being unavailable, as it is the default and only available algorithm for these dialects.

### `client smb encryption over quic`

Section: security; Context: G; Type: boolean; Default: `yes`

This parameter controls whether the client requires SMB level encryption even when the transport is already encrypted via QUIC and thus TLS. client smb encrypt controls the use of the encryption mechanism introduced with SMB3.0. If client smb encryption over quic value is set to no , and the client connects via a validated QUIC (and thus TLS) connection, the client ignores the requirements from the parameter client smb encrypt to avoid double encryption. If client smb encryption over quic is left at its default yes , the client connects over normal TCP, or the tls verify peer was set to anything less than ca_and_name , the requirements from client smb encrypt apply. Note that the QUIC-layer encryption is based on a TLS-level certificate presented by the server. The SMB-layer encryption is based on individual user sessions and as such essentially on initial user credentials such as the user's password or equivalent credentials used for logging on to a Windows session. This might influence your security assessment regarding the client smb encryption over quic parameter.

### `client smb3 signing algorithms`

Section: security; Context: G; Type: list; Default: `AES-128-GMAC, AES-128-CMAC, HMAC-SHA256`

This parameter specifies the availability and order of signing algorithms which are available for negotiation in the SMB3_11 dialect. It is also possible to remove individual algorithms from the default list, by prefixing them with '-'. This can avoid having to specify a hardcoded list. Note: that the removal of AES-128-CMAC from the list will result in SMB3_00 and SMB3_02 being unavailable, and the removal of HMAC-SHA256 will result in SMB2_02 and SMB2_10 being unavailable, as these are the default and only available algorithms for these dialects.

### `client use kerberos`

Section: security; Context: G; Type: enum; Default: `desired`

This parameter determines whether Samba client tools will try to authenticate using Kerberos. For Kerberos authentication you need to use dns names instead of IP addresses when connecting to a service. Possible option settings are: desired - Kerberos authentication will be tried first and if it fails it automatically fallback to NTLM. required - Kerberos authentication will be required. There will be no fallback to NTLM or a different alternative. off - Don't use Kerberos, use NTLM instead or another alternative. In case that weak cryptography is not allowed (e.g. FIPS mode) the default will be forced to required .

### `create mask`

Section: security; Context: S; Type: octal; Default: `0744`

When a file is created, the necessary permissions are calculated according to the mapping from DOS modes to UNIX permissions, and the resulting UNIX mode is then bit-wise 'AND'ed with this parameter. This parameter may be thought of as a bit-wise MASK for the UNIX modes of a file. Any bit not set here will be removed from the modes set on a file when it is created. The default value of this parameter removes the group and other write and execute bits from the UNIX modes. Following this Samba will bit-wise 'OR' the UNIX mode created from this parameter with the value of the parameter which is set to 000 by default. This parameter does not affect directory masks. See the parameter for details.

### `debug encryption`

Section: security; Context: G; Type: boolean; Default: `no`

This option will make the smbd server and client code using libsmb (smbclient, smbget, smbspool, ...) dump the Session Id, the decrypted Session Key, the Signing Key, the Application Key, the Encryption Key and the Decryption Key every time an SMB3+ session is established. This information will be printed in logs at level 0. Warning: access to these values enables the decryption of any encrypted traffic on the dumped sessions. This option should only be enabled for debugging purposes.

### `dedicated keytab file`

Section: security; Context: G; Type: string

Specifies the absolute path to the kerberos keytab file when is set to "dedicated keytab".

### `directory mask`

Section: security; Context: S; Type: octal; Default: `0755`

This parameter is the octal modes which are used when converting DOS modes to UNIX modes when creating UNIX directories. When a directory is created, the necessary permissions are calculated according to the mapping from DOS modes to UNIX permissions, and the resulting UNIX mode is then bit-wise 'AND'ed with this parameter. This parameter may be thought of as a bit-wise MASK for the UNIX modes of a directory. Any bit not set here will be removed from the modes set on a directory when it is created. The default value of this parameter removes the 'group' and 'other' write bits from the UNIX mode, allowing only the user who owns the directory to modify it. Following this Samba will bit-wise 'OR' the UNIX mode created from this parameter with the value of the parameter. This parameter is set to 000 by default (i.e. no extra mode bits are added).

### `directory security mask`

Section: security; Context: S; Type: string

This parameter has been removed for Samba 4.0.0.

### `encrypt passwords`

Section: security; Context: G; Type: boolean; Default: `yes`

This parameter has been deprecated since Samba 4.11 and support for plaintext (as distinct from NTLM, NTLMv2 or Kerberos authentication) will be removed in a future Samba release. That is, in the future, the current default of encrypt passwords = yes will be the enforced behaviour. This boolean controls whether encrypted passwords will be negotiated with the client. Note that Windows NT 4.0 SP3 and above and also Windows 98 will by default expect encrypted passwords unless a registry entry is changed. To use encrypted passwords in Samba see the chapter "User Database" in the Samba HOWTO Collection. MS Windows clients that expect Microsoft encrypted passwords and that do not have plain text password support enabled will be able to connect only to a Samba server that has encrypted password support enabled and for which the user accounts have a valid encrypted password. Refer to the smbpasswd command man page for information regarding the creation of encrypted passwords for user accounts. The use of plain text passwords is NOT advised as support for this feature is no longer maintained in Microsoft Windows products. If you want to use plain text passwords you must set this parameter to no. In order for encrypted passwords to work correctly smbd 8 must either have access to a local smbpasswd 5 file (see the smbpasswd 8 program for information on how to set up and maintain this file), or set the [domain|ads] parameter which causes smbd to authenticate against another server.

### `force create mode`

Section: security; Context: S; Type: octal; Default: `0000`

This parameter specifies a set of UNIX mode bit permissions that will always be set on a file created by Samba. This is done by bitwise 'OR'ing these bits onto the mode bits of a file that is being created. The default for this parameter is (in octal) 000. The modes in this parameter are bitwise 'OR'ed onto the file mode after the mask set in the create mask parameter is applied. The example below would force all newly created files to have read and execute permissions set for 'group' and 'other' as well as the read/write/execute bits set for the 'user'.

### `force directory mode`

Section: security; Context: S; Type: octal; Default: `0000`

This parameter specifies a set of UNIX mode bit permissions that will always be set on a directory created by Samba. This is done by bitwise 'OR'ing these bits onto the mode bits of a directory that is being created. The default for this parameter is (in octal) 0000 which will not add any extra permission bits to a created directory. This operation is done after the mode mask in the parameter directory mask is applied. The example below would force all created directories to have read and execute permissions set for 'group' and 'other' as well as the read/write/execute bits set for the 'user'.

### `force directory security mode`

Section: security; Context: S; Type: string

This parameter has been removed for Samba 4.0.0.

### `force group`

Section: security; Context: S; Type: string

This specifies a UNIX group name that will be assigned as the default primary group for all users connecting to this service. This is useful for sharing files by ensuring that all access to files on service will use the named group for their permissions checking. Thus, by assigning permissions for this group to the files and directories within this service the Samba administrator can restrict or allow sharing of these files. In Samba 2.0.5 and above this parameter has extended functionality in the following way. If the group name listed here has a '+' character prepended to it then the current user accessing the share only has the primary group default assigned to this group if they are already assigned as a member of that group. This allows an administrator to decide that only users who are already in a particular group will create files with group ownership set to that group. This gives a finer granularity of ownership assignment. For example, the setting force group = +sys means that only users who are already in group sys will have their default primary group assigned to sys when accessing this Samba share. All other users will retain their ordinary primary group. If the parameter is also set the group specified in force group will override the primary group set in force user .

### `force security mode`

Section: security; Context: S; Type: string

This parameter has been removed for Samba 4.0.0.

### `force unknown acl user`

Section: security; Context: S; Type: boolean; Default: `no`

If this parameter is set, a Windows NT ACL that contains an unknown SID (security descriptor, or representation of a user or group id) as the owner or group owner of the file will be silently mapped into the current UNIX uid or gid of the currently connected user. This is designed to allow Windows NT clients to copy files and folders containing ACLs that were created locally on the client machine and contain users local to that machine only (no domain users) to be copied to a Samba server (usually with XCOPY /O) and have the unknown userid and groupid of the file owner map to the current connected user. This can only be fixed correctly when winbindd allows arbitrary mapping from any Windows NT SID to a UNIX uid or gid. Try using this parameter when XCOPY /O gives an ACCESS_DENIED error.

### `force user`

Section: security; Context: S; Type: string

This specifies a UNIX user name that will be assigned as the default user for all users connecting to this service. This is useful for sharing files. You should also use it carefully as using it incorrectly can cause security problems. This user name only gets used once a connection is established. Thus clients still need to connect as a valid user and supply a valid password. Once connected, all file operations will be performed as the "forced user", no matter what username the client connected as. This can be very useful. In Samba 2.0.5 and above this parameter also causes the primary group of the forced user to be used as the primary group for all file activity. Prior to 2.0.5 the primary group was left as the primary group of the connecting user (this was a bug).

### `guest account`

Section: security; Context: G; Type: string; Default: `nobody default can be changed at compile-time`

This is a username which will be used for access to services which are specified as (see below). Whatever privileges this user has will be available to any client connecting to the guest service. This user must exist in the password file, but does not require a valid login. The user account "ftp" is often a good choice for this parameter. On some systems the default guest account "nobody" may not be able to print. Use another account in this case. You should test this by trying to log in as your guest user (perhaps by using the su - command) and trying to print using the system print command such as lpr(1) or lp(1) . This parameter does not accept % macros, because many parts of the system require this value to be constant for correct operation.

### `guest ok`

Section: security; Context: S; Type: boolean; Default: `no`

If this parameter is yes for a service, then no password is required to connect to the service. Privileges will be those of the . This parameter nullifies the benefits of setting 2 See the section below on for more information about this option.

### `guest only`

Section: security; Context: S; Type: boolean; Default: `no`

If this parameter is yes for a service, then only guest connections to the service are permitted. This parameter will have no effect if is not set for the service. See the section below on for more information about this option.

### `hosts allow`

Section: security; Context: S; Type: cmdlist; Default: `none (i.e., all hosts permitted access)`

A synonym for this parameter is . This parameter is a comma, space, or tab delimited set of hosts which are permitted to access a service. If specified in the [global] section then it will apply to all services, regardless of whether the individual service has a different setting. You can specify the hosts by name or IP number. For example, you could restrict access to only the hosts on a Class C subnet with something like allow hosts = 150.203.5. . The full syntax of the list is described in the man page hosts_access(5) . Note that this man page may not be present on your system, so a brief description will be given here also. Note that the localhost address 127.0.0.1 will always be allowed access unless specifically denied by a option. You can also specify hosts by network/netmask pairs and by netgroup names if your system supports netgroups. The EXCEPT keyword can also be used to limit a wildcard list. The following examples may provide some help: Example 1: allow all IPs in 150.203.*.*; except one hosts allow = 150.203. EXCEPT 150.203.6.66 Example 2: allow hosts that match the given network/netmask hosts allow = 150.203.15.0/255.255.255.0 Example 3: allow a couple of hosts hosts allow = lapland, arvidsjaur Example 4: allow only hosts in NIS netgroup "foonet", but deny access from one particular host hosts allow = @foonet hosts deny = pirate Note that access still requires suitable user-level passwords. See testparm 1 for a way of testing your host access to see if it does what you expect.

### `hosts deny`

Section: security; Context: S; Type: cmdlist; Default: `none (i.e., no hosts specifically excluded)`

The opposite of hosts allow - hosts listed here are NOT permitted access to services unless the specific services have their own lists to override this one. Where the lists conflict, the allow list takes precedence. In the event that it is necessary to deny all by default, use the keyword ALL (or the netmask 0.0.0.0/0 ) and then explicitly specify to the hosts allow parameter those hosts that should be permitted access.

### `inherit acls`

Section: security; Context: S; Type: boolean; Default: `no`

This parameter is only relevant for filesystems that do not support standardized NFS4 ACLs but only a POSIX draft ACL implementation and which implements default ACLs like most filesystems on Linux. It can be used to ensure that if default ACLs exist on parent directories, they are always honored when creating a new file or subdirectory in these parent directories. The default behavior is to use the unix mode specified when creating the directory. Enabling this option sets the unix mode to 0777, thus guaranteeing that the default directory ACLs are propagated. Note that using the VFS modules acl_xattr or acl_tdb which store native Windows as meta-data will automatically turn this option on for any share for which they are loaded, as they require this option to emulate Windows ACLs correctly.

### `inherit owner`

Section: security; Context: S; Type: enum; Default: `no`

The ownership of new files and directories is normally governed by effective uid of the connected user. This option allows the Samba administrator to specify that the ownership for new files and directories should be controlled by the ownership of the parent directory. Valid options are: no - Both the Windows (SID) owner and the UNIX (uid) owner of the file are governed by the identity of the user that created the file. windows and unix - The Windows (SID) owner and the UNIX (uid) owner of new files and directories are set to the respective owner of the parent directory. yes - a synonym for windows and unix . unix only - Only the UNIX owner is set to the UNIX owner of the parent directory. Common scenarios where this behavior is useful is in implementing drop-boxes, where users can create and edit files but not delete them and ensuring that newly created files in a user's roaming profile directory are actually owned by the user. The unix only option effectively breaks the tie between the Windows owner of a file and the UNIX owner. As a logical consequence, in this mode, setting the Windows owner of a file does not modify the UNIX owner. Using this mode should typically be combined with a backing store that can emulate the full NT ACL model without affecting the POSIX permissions, such as the acl_xattr VFS module, coupled with yes . This can be used to emulate folder quotas, when files are exposed only via SMB (without UNIX extensions). The UNIX owner of a directory is locally set and inherited by all subdirectories and files, and they all consume the same quota.

### `inherit permissions`

Section: security; Context: S; Type: boolean; Default: `no`

The permissions on new files and directories are normally governed by , , and but the boolean inherit permissions parameter overrides this. New directories inherit the mode of the parent directory, including bits such as setgid. New files inherit their read/write bits from the parent directory. Their execute bits continue to be determined by , and as usual. Note that the setuid bit is never set via inheritance (the code explicitly prohibits this). This can be particularly useful on large systems with many users, perhaps several thousand, to allow a single [homes] share to be used flexibly by each user.

### `kdc always include pac`

Section: security; Context: G; Type: boolean; Default: `yes`

This option over-rides the PA-PAC-REQUEST received from the client. When enabled (the default) a PAC will always be included in the kerberos responses. This option currently only applies if the embedded Heimdal KDC is used.

### `certificate backdating compensation`

Section: security; Context: G; Type: integer; Default: `0`

When performing certificate based kerberos authentication (PKINIT) with compatibility This parameter specifies the number of minutes that a certificate's issue date may precede the creation of a user's account. More details can be found at KB5014754: Certificate-based authentication changes on Windows domain controllers

### `kdc default domain supported enctypes`

Section: security; Context: G; Type: integer; Default: `0 maps to what the software supports currently. If AES keys are available (the domain functional level is 2008 or higher), this is aes128-cts-hmac-sha1-96 aes256-cts-hmac-sha1-96. Otherwise it is arcfour-hmac-md5 aes256-cts-hmac-sha1-96-sk.`

Set the default value of msDS-SupportedEncryptionTypes for service accounts in Active Directory that are missing this value or where msDS-SupportedEncryptionTypes is set to 0. This allows Samba administrators to match the configuration flexibility provided by the HKEY_LOCAL_MACHINE\System\CurrentControlSet\services\KDC\DefaultDomainSupportedEncTypes Registry Value on Windows. Unlike the Windows registry key (which only takes an base-10 number), in Samba this may also be expressed in hexadecimal or as a list of Kerberos encryption type names. Specified values are ORed together bitwise, and those currently supported consist of: arcfour-hmac-md5 , rc4-hmac , 0x4 , or 4 Known on Windows as Kerberos RC4 encryption aes128-cts-hmac-sha1-96 , aes128-cts , 0x8 , or 8 Known on Windows as Kerberos AES 128 bit encryption aes256-cts-hmac-sha1-96 , aes256-cts , 0x10 , or 16 Known on Windows as Kerberos AES 256 bit encryption aes256-cts-hmac-sha1-96-sk , aes256-cts-sk , 0x20 , or 32 Allow AES session keys. When this is set, it indicates to the KDC that AES session keys can be used, even when aes256-cts and aes128-cts are not set. This allows use of AES keys against hosts otherwise only configured with RC4 for ticket keys (which is the default).

### `kdc enable fast`

Section: security; Context: G; Type: boolean; Default: `yes`

With the Samba 4.16 the embedded Heimdal KDC brings support for RFC6113 FAST, which wasn't available in older Samba versions. This option is mostly for testing and currently only applies if the embedded Heimdal KDC is used.

### `kdc force enable rc4 weak session keys`

Section: security; Context: G; Type: boolean; Default: `no`

RFC8429 declares that rc4-hmac Kerberos ciphers are weak and there are known attacks on Active Directory use of this cipher suite. However for compatibility with Microsoft Windows this option allows the KDC to assume that regardless of the value set in a service account's msDS-SupportedEncryptionTypes attribute that a rc4-hmac Kerberos session key (as distinct from the ticket key, as found in a service keytab) can be used if the potentially older client requests it.

### `kdc name match implicit dollar without canonicalization`

Section: security; Context: G; Type: boolean; Default: `yes`

This option only affect clients that do not request name canonicalization in an AS request, which generally means traditional unix Kerberos clients and not Windows clients. The KDC may match the name in an AS request inexactly, for example using a case-insensitive comparison or converting it to a User Principal Name, but the client is not informed of the principal it actually matched unless it set the 'canonicalize' option flag. In Active Directory domains, the default behaviour of the KDC is to append a '$' character if the supplied name does not have one and does not already match. That allows 'foo' to match the machine account 'foo$'. An attacker who is able to create arbitrary machine accounts (which can be a low-privilege operation) is sometimes able to get tickets for unix users by mimicking their names. This is known as the 'dollar ticket attack'. With this option set to 'no', the KDC will not try to match using the appended '$' unless the canonicalize flag is set. This will allow AD-aware clients as usual to connect with canonicalization, but not expose traditional unix clients to the dollar ticket attack.

### `kdc require canonicalization`

Section: security; Context: G; Type: boolean; Default: `no`

Require that Kerberos clients use the canonicalization flag. Clients that do not use the Kerberos canonicalization flag (see RFC 6806) will get a TGT for the name they requested, which may not exactly match the name in the Samba database. For example, a client may request a ticket for 'root', and if there is a computer called 'ROOT$' in the database, the KDC will issue a ticket for 'root', using the standard matching rules for AD Kerberos. A member server that is Kerberos-aware but not AD-aware might accept this ticket as valid for the local root user. This option avoids the problem by refusing to honour requests without the canonicalization flag. This is a reasonable option if all expected clients request canonicalization (as Windows clients do), and there are member servers that might be confused by this issue. Typically that means unix servers expecting to be in an MIT Kerberos domain. See also the "kdc name match implicit dollar without canonicalization" option, which is more useful if you expect Kerberos clients that will not use the canonicalize flag.

### `kdc supported enctypes`

Section: security; Context: G; Type: integer; Default: `0 maps to what the software supports currently: arcfour-hmac-md5 aes128-cts-hmac-sha1-96 aes256-cts-hmac-sha1-96`

On an active directory domain controller, this is the list of supported encryption types for the local running kdc. This allows Samba administrators to remove support for weak/unused encryption types, similar the configuration flexibility provided by the Network security: Configure encryption types allowed for Kerberos GPO/Local Policies/Security Options Value, which results in the HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters\SupportedEncryptionTypes Registry Value on Windows. Unlike the Windows registry key (which only takes an base-10 number), in Samba this may also be expressed as hexadecimal or a list of Kerberos encryption type names. Specified values are ORed together bitwise, and those currently supported consist of: arcfour-hmac-md5 , rc4-hmac , 0x4 , or 4 Known on Windows as Kerberos RC4 encryption aes128-cts-hmac-sha1-96 , aes128-cts , 0x8 , or 8 Known on Windows as Kerberos AES 128 bit encryption aes256-cts-hmac-sha1-96 , aes256-cts , 0x10 , or 16 Known on Windows as Kerberos AES 256 bit encryption

### `kerberos encryption types`

Section: security; Context: G; Type: enum; Default: `all`

This parameter determines the encryption types to use when operating as a Kerberos client. Possible values are all , strong , and legacy . Samba uses a Kerberos library (MIT or Heimdal) to obtain Kerberos tickets. This library is normally configured outside of Samba, using the krb5.conf file. This file may also include directives to configure the encryption types to be used. However, Samba implements Active Directory protocols and algorithms to locate a domain controller. In order to force the Kerberos library into using the correct domain controller, some Samba processes, such as winbindd 8 and net 8 , build a private krb5.conf file for use by the Kerberos library while being invoked from Samba. This private file controls all aspects of the Kerberos library operation, and this parameter controls how the encryption types are configured within this generated file, and therefore also controls the encryption types negotiable by Samba. When set to all , all active directory encryption types are allowed. When set to strong , only AES-based encryption types are offered. This can be used in hardened environments to prevent downgrade attacks. When set to legacy , only RC4-HMAC-MD5 is allowed. AVOID using this option, because of CVE-2022-37966 see https://bugzilla.samba.org/show_bug.cgi?id=15237 .

### `kerberos method`

Section: security; Context: G; Type: enum; Default: `default`

Controls how kerberos tickets are verified. Valid options are: secrets only - use only the secrets.tdb for ticket verification (default) system keytab - use only the system keytab for ticket verification dedicated keytab - use a dedicated keytab for ticket verification secrets and keytab - use the secrets.tdb first, then the system keytab The major difference between "system keytab" and "dedicated keytab" is that the latter method relies on kerberos to find the correct keytab entry instead of filtering based on expected principals. When the kerberos method is in "dedicated keytab" mode, must be set to specify the location of the keytab file. Suggested configuration is to use the default value 'secrets only' together with the option.

### `kpasswd port`

Section: security; Context: G; Type: integer; Default: `464`

Specifies which ports the Kerberos server should listen on for password changes.

### `krb5 acceptor report canonical client name`

Section: security; Context: G; Type: boolean; Default: `yes`

This option affects the client name provided to Kerberos acceptors for incoming Kerberos tickets. If set to ‘yes’, the client name in the ticket will be replaced with the canonical client name (the sAMAccountName). Otherwise, it will be left unchanged. This option currently only applies if the embedded Heimdal KDC is used.

### `krb5 port`

Section: security; Context: G; Type: integer; Default: `88`

Specifies which port the KDC should listen on for Kerberos traffic.

### `lanman auth`

Section: security; Context: G; Type: boolean; Default: `no`

This parameter has been deprecated since Samba 4.11 and support for LanMan (as distinct from NTLM, NTLMv2 or Kerberos authentication) will be removed in a future Samba release. That is, in the future, the current default of lanman auth = no will be the enforced behaviour. This parameter determines whether or not smbd 8 will attempt to authenticate users or permit password changes using the LANMAN password hash. If disabled, only clients which support NT password hashes (e.g. Windows NT/2000 clients, smbclient, but not Windows 95/98 or the MS DOS network client) will be able to connect to the Samba host. The LANMAN encrypted response is easily broken, due to its case-insensitive nature, and the choice of algorithm. Servers without Windows 95/98/ME or MS DOS clients are advised to disable this option. When this parameter is set to no this will also result in sambaLMPassword in Samba's passdb being blanked after the next password change. As a result of that lanman clients won't be able to authenticate, even if lanman auth is re-enabled later on. Unlike the encrypt passwords option, this parameter cannot alter client behaviour, and the LANMAN response will still be sent over the network. See the client lanman auth to disable this for Samba's clients (such as smbclient) This parameter is overridden by ntlm auth , so unless that it is also set to ntlmv1-permitted or yes , then only NTLMv2 logins will be permitted and no LM hash will be stored. All modern clients support NTLMv2, and but some older clients require special configuration to use it. This parameter has no impact on the Samba AD DC, LM authentication is always disabled and no LM password is ever stored.

### `log nt token command`

Section: security; Context: G; Type: string

This option can be set to a command that will be called when new nt tokens are created. This is only useful for development purposes.

### `map to guest`

Section: security; Context: G; Type: enum; Default: `Never`

This parameter can take four different values, which tell smbd 8 what to do with user login requests that don't match a valid UNIX user in some way. The four settings are : Never - Means user login requests with an invalid password are rejected. This is the default. Bad User - Means user logins with an invalid password are rejected, unless the username does not exist, in which case it is treated as a guest login and mapped into the . Bad Password - Means user logins with an invalid password are treated as a guest login and mapped into the . Note that this can cause problems as it means that any user incorrectly typing their password will be silently logged on as "guest" - and will not know the reason they cannot access files they think they should - there will have been no message given to them that they got their password wrong. Helpdesk services will hate you if you set the map to guest parameter this way :-). Bad Uid - Is only applicable when Samba is configured in some type of domain mode security (security = {domain|ads}) and means that user logins which are successfully authenticated but which have no valid Unix user account (and smbd is unable to create one) should be mapped to the defined guest account. This was the default behavior of Samba 2.x releases. Note that if a member server is running winbindd, this option should never be required because the nss_winbind library will export the Windows domain users and groups to the underlying OS via the Name Service Switch interface. Note that this parameter is needed to set up "Guest" share services. This is because in these modes the name of the resource being requested is not sent to the server until after the server has successfully authenticated the client so the server cannot make authentication decisions at the correct time (connection to the share) for "Guest" shares.

### `min domain uid`

Section: security; Context: G; Type: integer; Default: `1000`

The integer parameter specifies the minimum uid allowed when mapping a local account to a domain account. Note that this option interacts with the configured idmap ranges !

### `mit kdc command`

Section: security; Context: G; Type: list

This option specifies the path to the MIT kdc binary. If the KDC is not installed in the default location and wasn't correctly detected during build then you should modify this variable and point it to the correct binary.

### `nt hash store`

Section: security; Context: G; Type: enum; Default: `always`

This parameter determines whether or not samba 8 will, as an AD DC, attempt to store the NT password hash used in NTLM and NTLMv2 authentication for users in this domain. If so configured, the Samba Active Directory Domain Controller, will, except for trust accounts (computers, domain controllers and inter-domain trusts), NOT store the NT hash for new and changed accounts in the sam.ldb database. This avoids the storage of an unsalted hash for these user-created passwords. As a consequence the arcfour-hmac-md5 Kerberos key type is also unavailable in the KDC for these users - thankfully modern clients will select an AES based key instead. NOTE: As the password history in Active Directory is stored as an NT hash (and thus unavailable), a workaround is used, relying instead on Kerberos password hash values. This stores three passwords, the current, previous and second previous password. This allows some checking against reuse. However as these values are salted, changing the sAMAccountName, userAccountControl or userPrincipalName of an account will cause the salt to change. After the rare combination of both a rename and a password change only the current password will be recognised for password history purposes. The available settings are: always - Always store the NT hash (as machine accounts will also always store an NT hash, a hash will be stored for all accounts). This setting may be useful if ntlm auth is set to disabled for a trial period never - Never store the NT hash for user accounts, only for machine accounts auto - Store an NT hash if ntlm auth is not set to disabled .

### `ntlm auth`

Section: security; Context: G; Type: enum; Default: `ntlmv2-only`

This parameter determines whether or not smbd 8 will attempt to authenticate users using the NTLM encrypted password response for this local passdb (SAM or account database). If disabled, both NTLM and LanMan authentication against the local passdb is disabled. Note that these settings apply only to local users, authentication will still be forwarded to and NTLM authentication accepted against any domain we are joined to, and any trusted domain, even if disabled or if NTLMv2-only is enforced here. To control NTLM authentication for domain users, this option must be configured on each DC. By default with ntlm auth set to ntlmv2-only only NTLMv2 logins will be permitted. All modern clients support NTLMv2 by default, but some older clients will require special configuration to use it. The primary user of NTLMv1 is MSCHAPv2 for VPNs and 802.1x. The available settings are: ntlmv1-permitted (alias yes ) - Allow NTLMv1 and above for all clients. This is the required setting to enable the lanman auth parameter. ntlmv2-only (alias no ) - Do not allow NTLMv1 to be used, but permit NTLMv2. mschapv2-and-ntlmv2-only - Only allow NTLMv1 when the client promises that it is providing MSCHAPv2 authentication (such as the ntlm_auth tool). disabled - Do not accept NTLM (or LanMan) authentication of any level, nor permit NTLM password changes. WARNING: Both Microsoft Windows and Samba Read Only Domain Controllers (RODCs) convert a plain-text LDAP Simple Bind into an NTLMv2 authentication to forward to a full DC. Setting this option to disabled will cause these forwarded authentications to fail. Additionally, for Samba acting as an Active Directory Domain Controller, for user accounts, if nt hash store is set to the default setting of auto , the NT hash will not be stored in the sam.ldb database for new users and after a password change. The default changed from yes to no with Samba 4.5. The default changed again to ntlmv2-only with Samba 4.7, however the behaviour is unchanged.

### `ntp signd socket directory`

Section: security; Context: G; Type: string

This setting controls the location of the socket that the NTP daemon uses to communicate with Samba for signing packets. If a non-default path is specified here, then it is also necessary to make NTP aware of the new path using the ntpsigndsocket directive in ntp.conf .

### `null passwords`

Section: security; Context: G; Type: boolean; Default: `no`

Allow or disallow client access to accounts that have null passwords. See also smbpasswd 5 .

### `obey pam restrictions`

Section: security; Context: G; Type: boolean; Default: `no`

When Samba 3.0 is configured to enable PAM support (i.e. --with-pam), this parameter will control whether or not Samba should obey PAM's account and session management directives. The default behavior is to use PAM for clear text authentication only and to ignore any account or session management. Note that Samba always ignores PAM for authentication in the case of yes . The reason is that PAM modules cannot support the challenge/response authentication mechanism needed in the presence of SMB password encryption.

### `old password allowed period`

Section: security; Context: G; Type: integer; Default: `60`

Number of minutes to permit an NTLM login after a password change or reset using the old password. This allows the user to re-cache the new password on multiple clients without disrupting a network reconnection in the meantime. This parameter only applies when is set to Active Directory Domain Controller.

### `pam password change`

Section: security; Context: G; Type: boolean; Default: `no`

With the addition of better PAM support in Samba 2.2, this parameter, it is possible to use PAM's password change control flag for Samba. If enabled, then PAM will be used for password changes when requested by an SMB client instead of the program listed in . It should be possible to enable this without changing your parameter for most setups.

### `passdb backend`

Section: security; Context: G; Type: string; Default: `tdbsam`

This option allows the administrator to chose which backend will be used for storing user and possibly group information. This allows you to swap between different storage mechanisms without recompile. The parameter value is divided into two parts, the backend's name, and a 'location' string that has meaning only to that particular backed. These are separated by a : character. Available backends can include: smbpasswd - The old plaintext passdb backend. Some Samba features will not work if this passdb backend is used. Takes a path to the smbpasswd file as an optional argument. tdbsam - The TDB based password storage backend. Takes a path to the TDB as an optional argument (defaults to passdb.tdb in the directory. ldapsam - The LDAP based passdb backend. Takes an LDAP URL as an optional argument (defaults to ldap://localhost ) LDAP connections should be secured where possible. This may be done using either Start-TLS (see ) or by specifying ldaps:// in the URL argument. Multiple servers may also be specified in double-quotes. Whether multiple servers are supported or not and the exact syntax depends on the LDAP library you use. Examples of use are: passdb backend = tdbsam:/etc/samba/private/passdb.tdb or multi server LDAP URL with OpenLDAP library: passdb backend = ldapsam:"ldap://ldap-1.example.com ldap://ldap-2.example.com" or multi server LDAP URL with Netscape based LDAP library: passdb backend = ldapsam:"ldap://ldap-1.example.com ldap-2.example.com"

### `passdb expand explicit`

Section: security; Context: G; Type: boolean; Default: `no`

This parameter controls whether Samba substitutes %-macros in the passdb fields if they are explicitly set. We used to expand macros here, but this turned out to be a bug because the Windows client can expand a variable %G_osver% in which %G would have been substituted by the user's primary group.

### `passwd chat`

Section: security; Context: G; Type: string; Default: `*new*password* %n\n *new*password* %n\n *changed*`

This string controls the "chat" conversation that takes places between smbd 8 and the local password changing program to change the user's password. The string describes a sequence of response-receive pairs that smbd 8 uses to determine what to send to the and what to expect back. If the expected output is not received then the password is not changed. This chat sequence is often quite site specific, depending on what local methods are used for password control. Note that this parameter only is used if the parameter is set to yes . This sequence is then called AS ROOT when the SMB password in the smbpasswd file is being changed, without access to the old password cleartext. This means that root must be able to reset the user's password without knowing the text of the previous password. The string can contain the macro %n which is substituted for the new password. The old password ( %o ) is only available when has been disabled. The chat sequence can also contain the standard macros \n, \r, \t and \s to give line-feed, carriage-return, tab and space. The chat sequence string can also contain a '*' which matches any sequence of characters. Double quotes can be used to collect strings with spaces in them into a single string. If the send string in any part of the chat sequence is a full stop ".", then no string is sent. Similarly, if the expect string is a full stop then no string is expected. If the parameter is set to yes , the chat pairs may be matched in any order, and success is determined by the PAM result, not any particular output. The \n macro is ignored for PAM conversions.

### `passwd chat debug`

Section: security; Context: G; Type: boolean; Default: `no`

This boolean specifies if the passwd chat script parameter is run in debug mode. In this mode the strings passed to and received from the passwd chat are printed in the smbd 8 log with a of 100. This is a dangerous option as it will allow plaintext passwords to be seen in the smbd log. It is available to help Samba admins debug their passwd chat scripts when calling the passwd program and should be turned off after this has been done. This option has no effect if the parameter is set. This parameter is off by default.

### `passwd chat timeout`

Section: security; Context: G; Type: integer; Default: `2`

This integer specifies the number of seconds smbd will wait for an initial answer from a passwd chat script being run. Once the initial answer is received the subsequent answers must be received in one tenth of this time. The default it two seconds.

### `passwd program`

Section: security; Context: G; Type: string

The name of a program that can be used to set UNIX user passwords. Any occurrences of %u will be replaced with the user name. The user name is checked for existence before calling the password changing program. Also note that many passwd programs insist in reasonable passwords, such as a minimum length, or the inclusion of mixed case chars and digits. This can pose a problem as some clients (such as Windows for Workgroups) uppercase the password before sending it. Note that if the unix password sync parameter is set to yes then this program is called AS ROOT before the SMB password in the smbpasswd file is changed. If this UNIX password change fails, then smbd will fail to change the SMB password also (this is by design). If the unix password sync parameter is set this parameter MUST USE ABSOLUTE PATHS for ALL programs called, and must be examined for security implications. Note that by default unix password sync is set to no .

### `password hash gpg key ids`

Section: security; Context: G; Type: cmdlist

If samba is running as an active directory domain controller, it is possible to store the cleartext password of accounts in a PGP/OpenGPG encrypted form. You can specify one or more recipients by key id or user id. Note that 32bit key ids are not allowed, specify at least 64bit. The value is stored as 'Primary:SambaGPG' in the supplementalCredentials attribute. As password changes can occur on any domain controller, you should configure this on each of them. Note that this feature is currently available only on Samba domain controllers. This option is only available if samba was compiled with gpgme support. You may need to export the GNUPGHOME environment variable before starting samba . It is strongly recommended to only store the public key in this location. The private key is not used for encryption and should be only stored where decryption is required. Being able to restore the cleartext password helps, when they need to be imported into other authentication systems later (see samba-tool user getpassword ) or you want to keep the passwords in sync with another system, e.g. an OpenLDAP server (see samba-tool user syncpasswords ). While this option needs to be configured on all domain controllers, the samba-tool user syncpasswords command should run on a single domain controller only (typically the PDC-emulator).

### `password hash userPassword schemes`

Section: security; Context: G; Type: cmdlist

This parameter determines whether or not samba 8 acting as an Active Directory Domain Controller will attempt to store additional passwords hash types for the user The values are stored as 'Primary:userPassword' in the supplementalCredentials attribute. The value of this option is a hash type. The currently supported hash types are: CryptSHA256 CryptSHA512 Multiple instances of a hash type may be computed and stored. The password hashes are calculated using the crypt 3 call. The number of rounds used to compute the hash can be specified by adding ':rounds=xxxx' to the hash type, i.e. CryptSHA512:rounds=4500 would calculate an SHA512 hash using 4500 rounds. If not specified the Operating System defaults for crypt 3 are used. As password changes can occur on any domain controller, you should configure this on each of them. Note that this feature is currently available only on Samba domain controllers. Currently the NT Hash of the password is recorded when these hashes are calculated and stored. When retrieving the hashes the current value of the NT Hash is checked against the stored NT Hash. This detects password changes that have not updated the password hashes. In this case samba-tool user will ignore the stored hash values. Being able to obtain the hashed password helps, when they need to be imported into other authentication systems later (see samba-tool user getpassword ) or you want to keep the passwords in sync with another system, e.g. an OpenLDAP server (see samba-tool user syncpasswords ). unix password sync

### `password server`

Section: security; Context: G; Type: string; Default: `*`

By specifying the name of a domain controller with this option, and using security = [ads|domain] it is possible to get Samba to do all its username/password validation using a specific remote server. Ideally, this option should not be used, as the default '*' indicates to Samba to determine the best DC to contact dynamically, just as all other hosts in an AD domain do. This allows the domain to be maintained (addition and removal of domain controllers) without modification to the smb.conf file. The cryptographic protection on the authenticated RPC calls used to verify passwords ensures that this default is safe. It is strongly recommended that you use the default of '*' , however if in your particular environment you have reason to specify a particular DC list, then the list of machines in this option must be a list of names or IP addresses of Domain controllers for the Domain. If you use the default of '*', or list several hosts in the password server option then smbd will try each in turn till it finds one that responds. This is useful in case your primary server goes down. If the list of servers contains both names/IP's and the '*' character, the list is treated as a list of preferred domain controllers, but an auto lookup of all remaining DC's will be added to the list as well. Samba will not attempt to optimize this list by locating the closest DC. If parameter is a name, it is looked up using the parameter and so may resolved by any method and order described in that parameter.

### `preload modules`

Section: security; Context: G; Type: cmdlist

This is a list of paths to modules that should be loaded into smbd before a client connects. This improves the speed of smbd when reacting to new connections somewhat.

### `private dir`

Section: security; Context: G; Type: string

This parameters defines the directory smbd will use for storing such files as smbpasswd and secrets.tdb .

### `raw NTLMv2 auth`

Section: security; Context: G; Type: boolean; Default: `no`

This parameter has been deprecated since Samba 4.13 and support for NTLMv2 authentication without NTLMSSP will be removed in a future Samba release. That is, in the future, the current default of raw NTLMv2 auth = no will be the enforced behaviour. This parameter determines whether or not smbd 8 will allow SMB1 clients without extended security (without SPNEGO) to use NTLMv2 authentication. If this option, lanman auth and ntlm auth are all disabled, then only clients with SPNEGO support will be permitted. That means NTLMv2 is only supported within NTLMSSP.

### `read list`

Section: security; Context: S; Type: cmdlist

This is a list of users that are given read-only access to a service. If the connecting user is in this list then they will not be given write access, no matter what the option is set to. The list can include group names using the syntax described in the parameter.

### `read only`

Section: security; Context: S; Type: boolean; Default: `yes`

An inverted synonym is . If this parameter is yes , then users of a service may not create or modify files in the service's directory. Note that a printable service ( printable = yes ) will ALWAYS allow writing to the directory (user privileges permitting), but only via spooling operations.

### `rename user script`

Section: security; Context: G; Type: string

This is the full pathname to a script that will be run as root by smbd 8 under special circumstances described below. When a user with admin authority or SeAddUserPrivilege rights renames a user (e.g.: from the NT4 User Manager for Domains), this script will be run to rename the POSIX user. Two variables, %uold and %unew , will be substituted with the old and new usernames, respectively. The script should return 0 upon successful completion, and nonzero otherwise. The script has all responsibility to rename all the necessary data that is accessible in this posix method. This can mean different requirements for different backends. The tdbsam and smbpasswd backends will take care of the contents of their respective files, so the script is responsible only for changing the POSIX username, and other data that may required for your circumstances, such as home directory. Please also consider whether or not you need to rename the actual home directories themselves. The ldapsam backend will not make any changes, because of the potential issues with renaming the LDAP naming attribute. In this case the script is responsible for changing the attribute that samba uses (uid) for locating users, as well as any data that needs to change for other applications using the same directory.

### `restrict anonymous`

Section: security; Context: G; Type: integer; Default: `0`

The setting of this parameter determines whether SAMR and LSA DCERPC services can be accessed anonymously. This corresponds to the following Windows Server registry options: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\RestrictAnonymous The option also affects the browse option which is required by legacy clients which rely on Netbios browsing. While modern Windows version should be fine with restricting the access there could still be applications relying on anonymous access. Setting 1 will disable anonymous SAMR access. Setting 2 will, in addition to restricting SAMR access, disallow anonymous connections to the IPC$ share in general. Setting yes on any share will remove the security advantage.

### `root directory`

Section: security; Context: G; Type: string

The server will chroot() (i.e. Change its root directory) to this directory on startup. This is not strictly necessary for secure operation. Even without it the server will deny access to files not in one of the service entries. It may also check for, and deny access to, soft links to other parts of the filesystem, or attempts to use ".." in file names to access other directories (depending on the setting of the parameter). Adding a root directory entry other than "/" adds an extra level of security, but at a price. It absolutely ensures that no access is given to files not in the sub-tree specified in the root directory option, including some files needed for complete operation of the server. To maintain full operability of the server you will need to mirror some system files into the root directory tree. In particular you will need to mirror /etc/passwd (or a subset of it), and any binaries or configuration files needed for printing (if required). The set of files that must be mirrored is operating system dependent.

### `samba kcc command`

Section: security; Context: G; Type: cmdlist; Default: `/samba_kcc`

This option specifies the path to the Samba KCC command. This script is used for replication topology replication. It should not be necessary to modify this option except for testing purposes or if the samba_kcc was installed in a non-default location.

### `security`

Section: security; Context: G; Type: enum; Default: `AUTO`

This option affects how clients respond to Samba and is one of the most important settings in the smb.conf file. Unless is specified, the default is security = user , as this is the most common setting, used for a standalone file server or a DC. The alternatives to security = user are security = ads or security = domain , which support joining Samba to a Windows domain You should use security = user and if you want to mainly setup shares without a password (guest shares). This is commonly used for a shared printer server. The different settings will now be explained. SECURITY = AUTO This is the default security setting in Samba, and causes Samba to consult the parameter (if set) to determine the security mode. SECURITY = USER If is not specified, this is the default security setting in Samba. With user-level security a client must first "log-on" with a valid username and password (which can be mapped using the parameter). Encrypted passwords (see the parameter) can also be used in this security mode. Parameters such as and if set are then applied and may change the UNIX user to use on this connection, but only after the user has been successfully authenticated. Note that the name of the resource being requested is not sent to the server until after the server has successfully authenticated the client. This is why guest shares don't work in user level security without allowing the server to automatically map unknown users into the . See the parameter for details on doing this. SECURITY = DOMAIN This mode will only work correctly if net 8 has been used to add this machine into a Windows NT Domain. It expects the parameter to be set to yes . In this mode Samba will try to validate the username/password by passing it to a Windows NT Primary or Backup Domain Controller, in exactly the same way that a Windows NT Server would do. Note that a valid UNIX user must still exist as well as the account on the Domain Controller to allow Samba to have a valid UNIX account to map file access to. Note that from the client's point of view security = domain is the same as security = user . It only affects how the server deals with the authentication, it does not in any way affect what the client sees. Note that the name of the resource being requested is not sent to the server until after the server has successfully authenticated the client. This is why guest shares don't work in user level security without allowing the server to automatically map unknown users into the . See the parameter for details on doing this. See also the parameter and the parameter. SECURITY = ADS In this mode, Samba will act as a domain member in an ADS realm. To operate in this mode, the machine running Samba will need to have Kerberos installed and configured and Samba will need to be joined to the ADS realm using the net utility. Note that this mode does NOT make Samba operate as a Active Directory Domain Controller. Note that this forces yes and yes for the primary domain. Read the chapter about Domain Membership in the HOWTO for details.

### `security mask`

Section: security; Context: S; Type: string

This parameter has been removed for Samba 4.0.0.

### `server role`

Section: security; Context: G; Type: enum; Default: `AUTO`

This option determines the basic operating mode of a Samba server and is one of the most important settings in the smb.conf file. The default is server role = auto , as causes Samba to operate according to the setting, or if not specified as a simple file server that is not connected to any domain. The alternatives are server role = standalone or server role = member server , which support joining Samba to a Windows domain, along with server role = domain controller , which run Samba as a Windows domain controller. You should use server role = standalone and if you want to mainly setup shares without a password (guest shares). This is commonly used for a shared printer server. SERVER ROLE = AUTO This is the default server role in Samba, and causes Samba to consult the parameter (if set) to determine the server role, giving compatible behaviours to previous Samba versions. SERVER ROLE = STANDALONE If is also not specified, this is the default security setting in Samba. In standalone operation, a client must first "log-on" with a valid username and password (which can be mapped using the parameter) stored on this machine. Encrypted passwords (see the parameter) are by default used in this security mode. Parameters such as and if set are then applied and may change the UNIX user to use on this connection, but only after the user has been successfully authenticated. SERVER ROLE = MEMBER SERVER This mode will only work correctly if net 8 has been used to add this machine into a Windows Domain. It expects the parameter to be set to yes . In this mode Samba will try to validate the username/password by passing it to a Windows or Samba Domain Controller, in exactly the same way that a Windows Server would do. Note that a valid UNIX user must still exist as well as the account on the Domain Controller to allow Samba to have a valid UNIX account to map file access to. Winbind can provide this. SERVER ROLE = CLASSIC PRIMARY DOMAIN CONTROLLER This mode of operation runs a classic Samba primary domain controller, providing domain logon services to Windows and Samba clients of an NT4-like domain. Clients must be joined to the domain to create a secure, trusted path across the network. There must be only one PDC per NetBIOS scope (typically a broadcast network or clients served by a single WINS server). SERVER ROLE = CLASSIC BACKUP DOMAIN CONTROLLER This mode of operation runs a classic Samba backup domain controller, providing domain logon services to Windows and Samba clients of an NT4-like domain. As a BDC, this allows multiple Samba servers to provide redundant logon services to a single NetBIOS scope. SERVER ROLE = ACTIVE DIRECTORY DOMAIN CONTROLLER This mode of operation runs Samba as an active directory domain controller, providing domain logon services to Windows and Samba clients of the domain. This role requires special configuration, see the Samba4 HOWTO SERVER ROLE = IPA PRIMARY DOMAIN CONTROLLER This mode of operation runs Samba in a hybrid mode for IPA domain controller, providing forest trust to Active Directory. This role requires special configuration performed by IPA installers and should not be used manually by any administrator.

### `server signing`

Section: security; Context: G; Type: enum; Default: `default`

This controls whether the client is allowed or required to use SMB1 and SMB2 signing. Possible values are default , auto , mandatory and disabled . By default, and when smb signing is set to default , smb signing is required when is active directory domain controller and disabled otherwise. When set to auto, SMB1 signing is offered, but not enforced. When set to mandatory, SMB1 signing is required and if set to disabled, SMB signing is not offered either. For the SMB2 protocol, by design, signing cannot be disabled. In the case where SMB2 is negotiated, if this parameter is set to disabled , it will be treated as auto . Setting it to mandatory will still require SMB2 clients to use signing.

### `server smb encrypt`

Section: security; Context: S; Type: enum; Default: `default`

This parameter controls whether a remote client is allowed or required to use SMB encryption. It has different effects depending on whether the connection uses SMB1 or SMB2 and newer: If the connection uses SMB1, then this option controls the use of a Samba-specific extension to the SMB protocol introduced in Samba 3.2 that makes use of the Unix extensions. If the connection uses SMB2 or newer, then this option controls the use of the SMB-level encryption that is supported in SMB version 3.0 and above and available in Windows 8 and newer. This parameter can be set globally and on a per-share bases. Possible values are off , if_required , desired , and required . A special value is default which is the implicit default setting of if_required . Effects for SMB1 The Samba-specific encryption of SMB1 connections is an extension to the SMB protocol negotiated as part of the UNIX extensions. SMB encryption uses the GSSAPI (SSPI on Windows) ability to encrypt and sign every request/response in a SMB protocol stream. When enabled it provides a secure method of SMB/CIFS communication, similar to an ssh protected session, but using SMB/CIFS authentication to negotiate encryption and signing keys. Currently this is only supported smbclient of by Samba 3.2 and newer, and hopefully soon Linux CIFSFS and MacOS/X clients. Windows clients do not support this feature. This may be set on a per-share basis, but clients may chose to encrypt the entire session, not just traffic to a specific share. If this is set to mandatory then all traffic to a share must be encrypted once the connection has been made to the share. The server would return "access denied" to all non-encrypted requests on such a share. Selecting encrypted traffic reduces throughput as smaller packet sizes must be used (no huge UNIX style read/writes allowed) as well as the overhead of encrypting and signing all the data. If SMB encryption is selected, Windows style SMB signing (see the option) is no longer necessary, as the GSSAPI flags use select both signing and sealing of the data. When set to auto or default, SMB encryption is offered, but not enforced. When set to mandatory, SMB encryption is required and if set to disabled, SMB encryption can not be negotiated. Effects for SMB3.0 and newer Native SMB transport encryption is available in SMB version 3.0 or newer. It is only offered by Samba if server max protocol is set to SMB3 or newer. Clients supporting this type of encryption include Windows 8 and newer, Windows server 2012 and newer, and smbclient of Samba 4.1 and newer. The protocol implementation offers various options: The capability to perform SMB encryption can be negotiated during protocol negotiation. Data encryption can be enabled globally. In that case, an encryption-capable connection will have all traffic in all its sessions encrypted. In particular all share connections will be encrypted. Data encryption can also be enabled per share if not enabled globally. For an encryption-capable connection, all connections to an encryption-enabled share will be encrypted. Encryption can be enforced. This means that session setups will be denied on non-encryption-capable connections if data encryption has been enabled globally. And tree connections will be denied for non-encryption capable connections to shares with data encryption enabled. These features can be controlled with settings of server smb encrypt as follows: Leaving it as default, explicitly setting default , or setting it to if_required globally will enable negotiation of encryption but will not turn on data encryption globally or per share. Setting it to desired globally will enable negotiation and will turn on data encryption on sessions and share connections for those clients that support it. Setting it to required globally will enable negotiation and turn on data encryption on sessions and share connections. Clients that do not support encryption will be denied access to the server. Setting it to off globally will completely disable the encryption feature for all connections. Setting server smb encrypt = required for individual shares (while it's globally off) will deny access to this shares for all clients. Setting it to desired on a share will turn on data encryption for this share for clients that support encryption if negotiation has been enabled globally. Setting it to required on a share will enforce data encryption for this share if negotiation has been enabled globally. I.e. clients that do not support encryption will be denied access to the share. Note that this allows per-share enforcing to be controlled in Samba differently from Windows: In Windows, RejectUnencryptedAccess is a global setting, and if it is set, all shares with data encryption turned on are automatically enforcing encryption. In order to achieve the same effect in Samba, one has to globally set server smb encrypt to if_required , and then set all shares that should be encrypted to required . Additionally, it is possible in Samba to have some shares with encryption required and some other shares with encryption only desired , which is not possible in Windows. Setting it to off or if_required for a share has no effect.

### `server smb3 encryption algorithms`

Section: security; Context: G; Type: list; Default: `AES-128-GCM, AES-128-CCM, AES-256-GCM, AES-256-CCM`

This parameter specifies the availability and order of encryption algorithms which are available for negotiation in the SMB3_11 dialect. It is also possible to remove individual algorithms from the default list, by prefixing them with '-'. This can avoid having to specify a hardcoded list. Note: that the removal of AES-128-CCM from the list will result in SMB3_00 and SMB3_02 being unavailable, as it is the default and only available algorithm for these dialects.

### `server smb encryption over quic`

Section: security; Context: G; Type: boolean; Default: `yes`

This parameter controls whether the SMB server requires SMB-level encryption although the transport is encrypted via QUIC. server smb encrypt controls the use of the encryption mechanism introduced with SMB3.0. If server smb encryption over quic value is set to no , and the client connects via a validated QUIC (and thus TLS) connection, the server ignores the requirements from the parameter server smb encrypt and accepts all SMB-level packets inside the QUIC connection as encrypted in a trustworthy way. This avoids costly double-encryption. If server smb encryption over quic is left at its default yes , the client connects over normal TCP, or the client does not indicate that it can trust the QUIC connection it uses, the requirements from server smb encrypt apply. Note that the QUIC-layer encryption is based on a TLS-level certificate presented by the server. The SMB-layer encryption is based on individual user sessions and as such essentially on initial user credentials such as the user's password or equivalent credentials used for logging on to a Windows session. This might influence your security assessment regarding the server smb encryption over quic parameter. Windows has a similar SMB server setting with the DisableSmbEncryptionOnSecureConnection switch in the Set-SmbServerConfiguration PowerShell commandlet.

### `server smb3 signing algorithms`

Section: security; Context: G; Type: list; Default: `AES-128-GMAC, AES-128-CMAC, HMAC-SHA256`

This parameter specifies the availability and order of signing algorithms which are available for negotiation in the SMB3_11 dialect. It is also possible to remove individual algorithms from the default list, by prefixing them with '-'. This can avoid having to specify a hardcoded list. Note: that the removal of AES-128-CMAC from the list will result in SMB3_00 and SMB3_02 being unavailable, and the removal of HMAC-SHA256 will result in SMB2_02 and SMB2_10 being unavailable, as these are the default and only available algorithms for these dialects.

### `server support krb5 netlogon`

Section: security; Context: G; Type: boolean; Default: `no`

This option is experimental for now! This option controls whether the netlogon server (currently only in 'active directory domain controller' mode), will provide support for ServerAuthenticateKerberos. Support for ServerAuthenticateKerberos was added in Windows starting with Server 2025, it's available in Samba starting with 4.22 with the ' yes ' and ' yes ' options, which are disabled by default. This option interacts with the ' yes ' and ' yes ' options.

### `smb encrypt`

Section: security; Context: S; Type: enum; Default: `default`

This is a synonym for .

### `smb passwd file`

Section: security; Context: G; Type: string

This option sets the path to the encrypted smbpasswd file. By default the path to the smbpasswd file is compiled into Samba. An example of use is: smb passwd file = /etc/samba/smbpasswd

### `sync machine password script`

Section: security; Context: G; Type: string

This is the full pathname to a script that will be run by winbindd 8 when a machine account password is updated. If keytabs should be generated in clustered environments it is recommended to update them on all nodes. You can set the config option to /scripts/winbind_ctdb_updatekeytab.sh in clustering case. It is also needed to activate the 46.update-keytabs.script in ctdb, it re-creates the keytab during the ctdb recovered event: onnode all ctdb event script enable legacy 46.update-keytabs.script

### `sync machine password to keytab`

Section: security; Context: G; Type: cmdlist

This option allows you to describe what keytabs and how should be updated when machine account is changed via one of these commands wbinfo --change-secret rpcclient --machine-pass -c change_trust_pw net rpc changetrustpw net ads changetrustpw or by winbindd doing regular updates (see ) The option takes a list of keytab strings to describe how to synchronize content of those keytabs or a single 'disabled' value to disable the synchronization. Each string has this form: absolute_path_to_keytab:spn_spec[:spn_spec]*[:sync_etypes][:sync_kvno][:netbios_aliases][:additional_dns_hostnames][:machine_password] spn_spec can be specified multiple times (separated using ':') and each spn_spec can have exactly one of these forms: account_name sync_account_name sync_upn sync_spns spn_prefixes=value1[,value2[...]] spns=value1[,value2[...]] Every keytab contains principals according the specification below: account_name - COMPUTER$@REALM sync_account_name - uses attribute "sAMAccountName" from AD sync_upn - uses attribute "userPrincipalName" (if exists in AD) sync_spns - uses attribute "servicePrincipalName" (if exists in AD) spn_prefixes - creates these two principals from each prefix. e.g.: prefix/ @REALM prefix/ @REALM with :netbios_aliases for each netbiosalias in prefix/netbiosalias@REALM prefix/netbiosalias.dnsdomain@REALM with :additional_dns_hostnames for each additionaldnshostname in prefix/additionaldnshostname@REALM - 'host' principal should be created using specifier spn_prefixes spns - creates only the principals defined in the list 'account_name' and 'sync_account_name' are the same, just the source differs (secrets.tdb vs. AD). Options: sync_etypes - attribute "msDS-SupportedEncryptionTypes" is read from AD and is used to find the highest common enc type for AD and KRB5 lib. sync_kvno - attribute "msDS-KeyVersionNumber" from AD is used to set KVNO. If this option is missing, KVNO is set to -1. netbios_aliases - evaluated only for spn_prefixes (see details above). additional_dns_hostnames - evaluated only for spn_prefixes (see details above). machine_password - mandatory, if missing the entry is ignored. For future use. Example: "/path/to/keytab0:account_name:machine_password", "/path/to/keytab1:account_name:sync_etypes:sync_kvno:machine_password", "/path/to/keytab2:sync_spns:machine_password", "/path/to/keytab3:sync_spns:sync_kvno:machine_password", "/path/to/keytab4:spn_prefixes=imap,smtp:machine_password", "/path/to/keytab5:spn_prefixes=imap,smtp:netbios_aliases:additional_dns_hostnames:sync_kvno:machine_password", "/path/to/keytab6:spns=wurst/brot@REALM:machine_password", "/path/to/keytab7:spns=wurst/brot@REALM,wurst2/brot@REALM:sync_kvno:machine_password", "/path/to/keytab8:sync_account_name:sync_upn:sync_spns:spn_prefixes=host,cifs,http:spns=wurst/brot@REALM:sync_kvno:machine_password" If sync_etypes or sync_kvno or sync_spns is present then winbind connects to DC. For "offline domain join" it might be useful not to use these options. If no value is present and is different from 'secrets only', the behavior differs between winbind and net utility: winbind uses value /path/to/keytab:host:account_name:sync_spns:sync_kvno:machine_password where the path to the keytab is obtained either from the krb5 library or from . net changesecretpw -f command uses the default 'disabled' value. No other net subcommands use the 'disabled' value. If a single value 'disabled' is present, the synchronization process is disabled. This is required for FreeIPA domain member setup where keytab synchronization uses a protocol not implemented by Samba. Suggested configuration is together with set to the default value 'secrets only'. In clustered environments it is recommended to set to update the machine password on all nodes.

### `tls ca directories`

Section: security; Context: G; Type: list

This option can be set to a list of directories with files (in PEM format) containing CA certificates of root CAs to trust to sign certificates or intermediate CA certificates.

### `tls cafile`

Section: security; Context: G; Type: string; Default: `tls/ca.pem`

This option can be set to a file (PEM format) containing CA certificates of root CAs to trust to sign certificates or intermediate CA certificates. This path is relative to if the path does not start with a /.

### `tls certfile`

Section: security; Context: G; Type: string; Default: `tls/cert.pem`

This option can be set to a file (PEM format) containing the RSA certificate to be used as TLS server certificate. If required it can also contain additional intermediate certificates to be send along during the TLS handshake. This path is relative to if the path does not start with a /.

### `tls crlfile`

Section: security; Context: G; Type: string

This option can be set to a file containing a certificate revocation list (CRL). This path is relative to if the path does not start with a /.

### `tls dh params file`

Section: security; Context: G; Type: string

This option can be set to a file with Diffie-Hellman parameters which will be used with DH ciphers. This path is relative to if the path does not start with a /.

### `tls enabled`

Section: security; Context: G; Type: boolean; Default: `yes`

If this option is set to yes , then Samba will use TLS when possible in communication.

### `tls keyfile`

Section: security; Context: G; Type: string; Default: `tls/key.pem`

This option can be set to a file (PEM format) containing the RSA private key. This file must be accessible without a pass-phrase, i.e. it must not be encrypted. This path is relative to if the path does not start with a /.

### `tls priority`

Section: security; Context: G; Type: string; Default: `NORMAL:-VERS-SSL3.0`

This option can be set to a string describing the TLS protocols to be supported in the parts of Samba that use GnuTLS, specifically the AD DC. The string is appended to the default priority list of GnuTLS. The valid options are described in the GNUTLS Priority-Strings documentation at http://gnutls.org/manual/html_node/Priority-Strings.html The SSL3.0 protocol will be disabled.

### `tls trust system cas`

Section: security; Context: G; Type: boolean; Default: `no`

With this option the system's default trusted CAs are used to trust SSL/TLS connections. Please use this with care, as it really means trusting all CAs installed on the system!

### `tls verify peer`

Section: security; Context: G; Type: enum; Default: `as_strict_as_possible`

This controls if and how strict the client will verify the peer's certificate and name. Possible values are (in increasing order): no_check , ca_only , ca_and_name_if_available , ca_and_name and as_strict_as_possible . When set to no_check the certificate is not verified at all, which allows trivial man in the middle attacks. When set to ca_only the certificate is verified to be signed from a ca specified in the option. As alternative or can be used. Providing at least one valid CA certificate is required. The certificate lifetime is also verified. If the option is configured, the certificate is also verified against the ca crl. When set to ca_and_name_if_available all checks from ca_only are performed. In addition, the peer hostname is verified against the certificate's name, if it is provided by the application layer and not given as an ip address string. When set to ca_and_name all checks from ca_and_name_if_available are performed. In addition the peer hostname needs to be provided and even an ip address is checked against the certificate's name. When set to as_strict_as_possible all checks from ca_and_name are performed. In addition the needs to be configured. Future versions of Samba may implement additional checks.

### `unix password sync`

Section: security; Context: G; Type: boolean; Default: `no`

This boolean parameter controls whether Samba attempts to synchronize the UNIX password with the SMB password when the encrypted SMB password in the smbpasswd file is changed. If this is set to yes the program specified in the passwd program parameter is called AS ROOT - to allow the new UNIX password to be set without access to the old UNIX password (as the SMB password change code has no access to the old password cleartext, only the new). This option has no effect if samba is running as an active directory domain controller, in that case have a look at the option and the samba-tool user syncpasswords command.

### `username level`

Section: security; Context: G; Type: integer; Default: `0`

This option helps Samba to try and 'guess' at the real UNIX username, as many DOS clients send an all-uppercase username. By default Samba tries all lowercase, followed by the username with the first letter capitalized, and fails if the username is not found on the UNIX machine. If this parameter is set to non-zero the behavior changes. This parameter is a number that specifies the number of uppercase combinations to try while trying to determine the UNIX user name. The higher the number the more combinations will be tried, but the slower the discovery of usernames will be. Use this parameter when you have strange usernames on your UNIX machine, such as AstrangeUser . This parameter is needed only on UNIX systems that have case sensitive usernames.

### `username map`

Section: security; Context: G; Type: string; Default: `no username map`

This option allows you to specify a file containing a mapping of usernames from the clients to the server. This can be used for several purposes. The most common is to map usernames that users use on DOS or Windows machines to those that the UNIX box uses. The other is to map multiple users to a single username so that they can more easily share files. Please note that for user mode security, the username map is applied prior to validating the user credentials. Domain member servers (domain or ads) apply the username map after the user has been successfully authenticated by the domain controller and require fully qualified entries in the map table (e.g. biddle = DOMAIN\foo ). The map file is parsed line by line. Each line should contain a single UNIX username on the left then a '=' followed by a list of usernames on the right. The list of usernames on the right may contain names of the form @group in which case they will match any UNIX username in that group. The special client name '*' is a wildcard and matches any name. Each line of the map file may be up to 1023 characters long. The file is processed on each line by taking the supplied username and comparing it with each username on the right hand side of the '=' signs. If the supplied name matches any of the names on the right hand side then it is replaced with the name on the left. Processing then continues with the next line. If any line begins with a '#' or a ';' then it is ignored. If any line begins with an '!' then the processing will stop after that line if a mapping was done by the line. Otherwise mapping continues with every line being processed. Using '!' is most useful when you have a wildcard mapping line later in the file. For example to map from the name admin or administrator to the UNIX name root you would use: root = admin administrator Or to map anyone in the UNIX group system to the UNIX name sys you would use: sys = @system You can have as many mappings as you like in a username map file. If your system supports the NIS NETGROUP option then the netgroup database is checked before the /etc/group database for matching groups. You can map Windows usernames that have spaces in them by using double quotes around the name. For example: tridge = "Andrew Tridgell" would map the windows username "Andrew Tridgell" to the unix username "tridge". The following example would map mary and fred to the unix user sys, and map the rest to guest. Note the use of the '!' to tell Samba to stop processing if it gets a match on that line: !sys = mary fred guest = * Note that the remapping is applied to all occurrences of usernames. Thus if you connect to \\server\fred and fred is remapped to mary then you will actually be connecting to \\server\mary and will need to supply a password suitable for mary not fred . The only exception to this is the username passed to a Domain Controller (if you have one). The DC will receive whatever username the client supplies without modification. Also note that no reverse mapping is done. The main effect this has is with printing. Users who have been mapped may have trouble deleting print jobs as PrintManager under WfWg will think they don't own the print job. Samba versions prior to 3.0.8 would only support reading the fully qualified username (e.g.: DOMAIN\user ) from the username map when performing a kerberos login from a client. However, when looking up a map entry for a user authenticated by NTLM[SSP], only the login name would be used for matches. This resulted in inconsistent behavior sometimes even on the same server. The following functionality is obeyed in version 3.0.8 and later: When performing local authentication, the username map is applied to the login name before attempting to authenticate the connection. When relying upon a external domain controller for validating authentication requests, smbd will apply the username map to the fully qualified username (i.e. DOMAIN\user ) only after the user has been successfully authenticated. An example of use is: username map = /usr/local/samba/lib/users.map

### `username map cache time`

Section: security; Context: G; Type: integer; Default: `0`

Mapping usernames with the or features of Samba can be relatively expensive. During login of a user, the mapping is done several times. In particular, calling the can slow down logins if external databases have to be queried from the script being called. The parameter controls a mapping cache. It specifies the number of seconds a mapping from the username map file or script is to be efficiently cached. The default of 0 means no caching is done.

### `username map script`

Section: security; Context: G; Type: string

This script is a mutually exclusive alternative to the parameter. This parameter specifies an external program or script that must accept a single command line option (the username transmitted in the authentication request) and return a line on standard output (the name to which the account should mapped). In this way, it is possible to store username map tables in an LDAP directory services.

### `writeable`

Section: security; Context: S; Type: boolean-rev; Default: `no`

Inverted synonym for .

### `write list`

Section: security; Context: S; Type: cmdlist

This is a list of users that are given read-write access to a service. If the connecting user is in this list then they will be given write access, no matter what the option is set to. The list can include group names using the @group syntax. Note that if a user is in both the read list and the write list then they will be given write access.
