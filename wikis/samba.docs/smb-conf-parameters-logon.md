# smb.conf Parameters / logon

### `abort shutdown script`

Section: logon; Context: G; Type: string; Default: `""`

This a full path name to a script called by smbd 8 that should stop a shutdown procedure issued by the . If the connected user possesses the SeRemoteShutdownPrivilege , right, this command will be run as root.

### `add group script`

Section: logon; Context: G; Type: string

This is the full pathname to a script that will be run AS ROOT by smbd 8 when a new group is requested. It will expand any %g to the group name passed. This script is only useful for installations using the Windows NT domain administration tools. The script is free to create a group with an arbitrary name to circumvent unix group name restrictions. In that case the script must print the numeric gid of the created group on stdout.

### `add machine script`

Section: logon; Context: G; Type: string

This is the full pathname to a script that will be run by smbd 8 when a machine is added to Samba's domain and a Unix account matching the machine's name appended with a "$" does not already exist. This option is very similar to the , and likewise uses the %u substitution for the account name. Do not use the %m substitution.

### `add user script`

Section: logon; Context: G; Type: string

This is the full pathname to a script that will be run AS ROOT by smbd 8 under special circumstances described below. Normally, a Samba server requires that UNIX users are created for all users accessing files on this server. For sites that use Windows NT account databases as their primary user database creating these users and keeping the user list in sync with the Windows NT PDC is an onerous task. This option allows smbd to create the required UNIX users ON DEMAND when a user accesses the Samba server. When the Windows user attempts to access the Samba server, at login (session setup in the SMB protocol) time, smbd 8 contacts the and attempts to authenticate the given user with the given password. If the authentication succeeds then smbd attempts to find a UNIX user in the UNIX password database to map the Windows user into. If this lookup fails, and is set then smbd will call the specified script AS ROOT , expanding any %u argument to be the user name to create. If this script successfully creates the user then smbd will continue on as though the UNIX user already existed. In this way, UNIX users are dynamically created to match existing Windows NT accounts. See also , , .

### `add user to group script`

Section: logon; Context: G; Type: string

Full path to the script that will be called when a user is added to a group using the Windows NT domain administration tools. It will be run by smbd 8 AS ROOT . Any %g will be replaced with the group name and any %u will be replaced with the user name. Note that the adduser command used in the example below does not support the used syntax on all systems.

### `auth event notification`

Section: logon; Context: G; Type: boolean; Default: `no`

When enabled, this option causes Samba (acting as an Active Directory Domain Controller) to stream authentication events across the internal message bus. Scripts built using Samba's python bindings can listen to these events by registering as the service auth_event . This is not needed for the audit logging described in . Instead, this should instead be considered a developer option (it assists in the Samba testsuite) rather than a facility for external auditing, as message delivery is not guaranteed (a feature that the testsuite works around). The authentication events are also logged via the normal logging methods when the is set appropriately, say to auth_json_audit:3 .

### `delete group script`

Section: logon; Context: G; Type: string

This is the full pathname to a script that will be run AS ROOT by smbd 8 when a group is requested to be deleted. It will expand any %g to the group name passed. This script is only useful for installations using the Windows NT domain administration tools.

### `delete user from group script`

Section: logon; Context: G; Type: string

Full path to the script that will be called when a user is removed from a group using the Windows NT domain administration tools. It will be run by smbd 8 AS ROOT . Any %g will be replaced with the group name and any %u will be replaced with the user name.

### `delete user script`

Section: logon; Context: G; Type: string

This is the full pathname to a script that will be run by smbd 8 when managing users with remote RPC (NT) tools. This script is called when a remote client removes a user from the server, normally using 'User Manager for Domains' or rpcclient . This script should delete the given UNIX username.

### `domain logons`

Section: logon; Context: G; Type: boolean; Default: `no`

This parameter has been deprecated since Samba 4.13 and support for NT4-style domain logons(as distinct from the Samba AD DC) will be removed in a future Samba release. That is, in the future, the current default of domain logons = no will be the enforced behaviour. If set to yes , the Samba server will provide the netlogon service for Windows 9X network logons for the it is in. This will also cause the Samba server to act as a domain controller for NT4 style domain services. For more details on setting up this feature see the Domain Control chapter of the Samba HOWTO Collection.

### `enable privileges`

Section: logon; Context: G; Type: boolean; Default: `yes`

This deprecated parameter controls whether or not smbd will honor privileges assigned to specific SIDs via either net rpc rights or one of the Windows user and group manager tools. This parameter is enabled by default. It can be disabled to prevent members of the Domain Admins group from being able to assign privileges to users or groups which can then result in certain smbd operations running as root that would normally run under the context of the connected user. An example of how privileges can be used is to assign the right to join clients to a Samba controlled domain without providing root access to the server via smbd. Please read the extended description provided in the Samba HOWTO documentation.

### `init logon delay`

Section: logon; Context: G; Type: integer; Default: `100`

This parameter specifies a delay in milliseconds for the hosts configured for delayed initial samlogon with .

### `init logon delayed hosts`

Section: logon; Context: G; Type: cmdlist

This parameter takes a list of host names, addresses or networks for which the initial samlogon reply should be delayed (so other DCs get preferred by XP workstations if there are any). The length of the delay can be specified with the parameter.

### `logon drive`

Section: logon; Context: G; Type: string

This parameter specifies the local path to which the home directory will be connected (see ) and is only used by NT Workstations. Note that this option is only useful if Samba is set up as a logon server.

### `logon home`

Section: logon; Context: G; Type: string; Default: `\\%N\%U`

This parameter specifies the home directory location when a Win95/98 or NT Workstation logs into a Samba PDC. It allows you to do C:\> NET USE H: /HOME from a command prompt, for example. This option takes the standard substitutions, allowing you to have separate logon scripts for each user or machine. This parameter can be used with Win9X workstations to ensure that roaming profiles are stored in a subdirectory of the user's home directory. This is done in the following way: logon home = \\%N\%U\profile This tells Samba to return the above string, with substitutions made when a client requests the info, generally in a NetUserGetInfo request. Win9X clients truncate the info to \\server\share when a user does net use /home but use the whole string when dealing with profiles. Note that in prior versions of Samba, the was returned rather than logon home . This broke net use /home but allowed profiles outside the home directory. The current implementation is correct, and can be used for profiles if you use the above trick. Disable this feature by setting "" - using the empty string. This option is only useful if Samba is set up as a logon server.

### `logon path`

Section: logon; Context: G; Type: string; Default: `\\%N\%U\profile`

This parameter specifies the directory where roaming profiles (Desktop, NTuser.dat, etc) are stored. Contrary to previous versions of these manual pages, it has nothing to do with Win 9X roaming profiles. To find out how to handle roaming profiles for Win 9X system, see the parameter. This option takes the standard substitutions, allowing you to have separate logon scripts for each user or machine. It also specifies the directory from which the "Application Data", desktop , start menu , network neighborhood , programs and other folders, and their contents, are loaded and displayed on your Windows NT client. The share and the path must be readable by the user for the preferences and directories to be loaded onto the Windows NT client. The share must be writeable when the user logs in for the first time, in order that the Windows NT client can create the NTuser.dat and other directories. Thereafter, the directories and any of the contents can, if required, be made read-only. It is not advisable that the NTuser.dat file be made read-only - rename it to NTuser.man to achieve the desired effect (a MAN datory profile). Windows clients can sometimes maintain a connection to the [homes] share, even though there is no user logged in. Therefore, it is vital that the logon path does not include a reference to the homes share (i.e. setting this parameter to \\%N\homes\profile_path will cause problems). This option takes the standard substitutions, allowing you to have separate logon scripts for each user or machine. Do not quote the value. Setting this as \\%N\profile\%U will break profile handling. Where the tdbsam or ldapsam passdb backend is used, at the time the user account is created the value configured for this parameter is written to the passdb backend and that value will over-ride the parameter value present in the smb.conf file. Any error present in the passdb backend account record must be edited using the appropriate tool (pdbedit on the command-line, or any other locally provided system tool). Note that this option is only useful if Samba is set up as a domain controller. Disable the use of roaming profiles by setting the value of this parameter to no value. Take note that even if the default setting in the smb.conf file is the empty string, any value specified in the user account settings in the passdb backend will over-ride the effect of setting this parameter to null. Disabling of all roaming profile use requires that the user account settings must also be blank. An example of use is: logon path = \\PROFILESERVER\PROFILE\%U In this example the use of roaming profiles is disabled (depending also on passdb settings): logon path =

### `logon script`

Section: logon; Context: G; Type: string

This parameter specifies the batch file ( .bat ) or NT command file ( .cmd ) to be downloaded and run on a machine when a user successfully logs in. The file must contain the DOS style CR/LF line endings. Using a DOS-style editor to create the file is recommended. The script must be a relative path to the service. If the [netlogon] service specifies a of /usr/local/samba/netlogon , and STARTUP.BAT , then the file that will be downloaded is: /usr/local/samba/netlogon/STARTUP.BAT The contents of the batch file are entirely your choice. A suggested command would be to add NET TIME \\SERVER /SET /YES , to force every machine to synchronize clocks with the same time server. Another use would be to add NET USE U: \\SERVER\UTILS for commonly used utilities, or NET USE Q: \\SERVER\ISO9001_QA for example. Note that it is particularly important not to allow write access to the [netlogon] share, or to grant users write permission on the batch files in a secure environment, as this would allow the batch files to be arbitrarily modified and security to be breached. This option takes the standard substitutions, allowing you to have separate logon scripts for each user or machine. This option is only useful if Samba is set up as a logon server in a classic domain controller role. If Samba is set up as an Active Directory domain controller, LDAP attribute scriptPath is used instead. For configurations where ldapsam is in use, this option only defines a default value in case LDAP attribute sambaLogonScript is missing.

### `set primary group script`

Section: logon; Context: G; Type: string

Thanks to the Posix subsystem in NT a Windows User has a primary group in addition to the auxiliary groups. This script sets the primary group in the unix user database when an administrator sets the primary group from the windows user manager or when fetching a SAM with net rpc vampire . %u will be replaced with the user whose primary group is to be set. %g will be replaced with the group to set.
