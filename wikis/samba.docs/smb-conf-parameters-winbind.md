# smb.conf Parameters / winbind

### `apply group policies`

Section: winbind; Context: G; Type: boolean; Default: `no`

This option controls whether winbind will execute the gpupdate command defined in on the Group Policy update interval. The Group Policy update interval is defined as every 90 minutes, plus a random offset between 0 and 30 minutes. This applies Group Policy Machine polices to the client or KDC and machine policies to a server.

### `client use krb5 netlogon`

Section: winbind; Context: G; Type: enum; Default: `default`

This option is experimental for now! This option controls whether winbindd (and other client tools) try to use ServerAuthenticateKerberos for the netlogon secure channel. The behavior can be controlled per netbios domain by using 'client use krb5 netlogon:NETBIOSDOMAIN = yes|no' as option. This option is over-ridden by the option (if it is effectively on) and lets be yes as well. The 'default' currently maps to 'no'. A meaning of 'auto' depends on the used kerberos library and the trust/domain type. If samba was compiled using '--without-ads' or '--with-system-heimdalkrb5' it is not possible to activate the ServerAuthenticateKerberos feature, as the krb5_init_creds_step() function is not available. This forces 'auto' to behave as 'no'. The value of 'auto' maps to 'yes' if the domain is detected as active directory domain, e.g. with 'SECURITY = ADS' or on an active directory domain controller. WARNING: This option is experimental in this Samba version (see VERSION section below) and should not be used in production!

### `create krb5 conf`

Section: winbind; Context: G; Type: boolean; Default: `yes`

Setting this parameter to no prevents winbind from creating custom krb5.conf files. Winbind normally does this because the krb5 libraries are not AD-site-aware and thus would pick any domain controller out of potentially very many. Winbind is site-aware and makes the krb5 libraries use a local DC by creating its own krb5.conf files. Preventing winbind from doing this might become necessary if you have to add special options into your system-krb5.conf that winbind does not see.

### `idmap backend`

Section: winbind; Context: G; Type: string; Default: `tdb`

The idmap backend provides a plugin interface for Winbind to use varying backends to store SID/uid/gid mapping tables. This option specifies the default backend that is used when no special configuration set, but it is now deprecated in favour of the new spelling .

### `idmap cache time`

Section: winbind; Context: G; Type: integer; Default: `604800`

This parameter specifies the number of seconds that Winbind's idmap interface will cache positive SID/uid/gid query results. By default, Samba will cache these results for one week.

### `idmap config DOMAIN : OPTION`

Section: winbind; Context: G; Type: string

ID mapping in Samba is the mapping between Windows SIDs and Unix user and group IDs. This is performed by Winbindd with a configurable plugin interface. Samba's ID mapping is configured by options starting with the prefix. An idmap option consists of the prefix, followed by a domain name or the asterisk character (*), a colon, and the name of an idmap setting for the chosen domain. The idmap configuration is hence divided into groups, one group for each domain to be configured, and one group with the asterisk instead of a proper domain name, which specifies the default configuration that is used to catch all domains that do not have an explicit idmap configuration of their own. There are three general options available: backend = backend_name This specifies the name of the idmap plugin to use as the SID/uid/gid backend for this domain. The standard backends are tdb ( idmap_tdb 8 ), tdb2 ( idmap_tdb2 8 ), ldap ( idmap_ldap 8 ), rid ( idmap_rid 8 ), hash ( idmap_hash 8 ), autorid ( idmap_autorid 8 ), ad ( idmap_ad 8 ) and nss ( idmap_nss 8 ). The corresponding manual pages contain the details, but here is a summary. The first three of these create mappings of their own using internal unixid counters and store the mappings in a database. These are suitable for use in the default idmap configuration. The rid and hash backends use a pure algorithmic calculation to determine the unixid for a SID. The autorid module is a mixture of the tdb and rid backend. It creates ranges for each domain encountered and then uses the rid algorithm for each of these automatically configured domains individually. The ad backend uses unix ids stored in Active Directory via the standard schema extensions. The nss backend reverses the standard winbindd setup and gets the unix ids via names from nsswitch which can be useful in an ldap setup. range = low - high Defines the available matching uid and gid range for which the backend is authoritative. For allocating backends, this also defines the start and the end of the range for allocating new unique IDs. winbind uses this parameter to find the backend that is authoritative for a unix ID to SID mapping, so it must be set for each individually configured domain and for the default configuration. The configured ranges must be mutually disjoint. Note that the low value interacts with the option! read only = yes|no This option can be used to turn the writing backends tdb, tdb2, and ldap into read only mode. This can be useful e.g. in cases where a pre-filled database exists that should not be extended automatically. The following example illustrates how to configure the idmap_ad 8 backend for the CORP domain and the idmap_tdb 8 backend for all other domains. This configuration assumes that the admin of CORP assigns unix ids below 1000000 via the SFU extensions, and winbind is supposed to use the next million entries for its own mappings from trusted domains and for local groups for example. idmap config * : backend = tdb idmap config * : range = 1000000-1999999 idmap config CORP : backend = ad idmap config CORP : range = 1000-999999

### `idmap gid`

Section: winbind; Context: G; Type: string

The idmap gid parameter specifies the range of group ids for the default idmap configuration. It is now deprecated in favour of . See the option.

### `idmap negative cache time`

Section: winbind; Context: G; Type: integer; Default: `120`

This parameter specifies the number of seconds that Winbind's idmap interface will cache negative SID/uid/gid query results.

### `idmap uid`

Section: winbind; Context: G; Type: string

The idmap uid parameter specifies the range of user ids for the default idmap configuration. It is now deprecated in favour of . See the option.

### `include system krb5 conf`

Section: winbind; Context: G; Type: boolean; Default: `yes`

Setting this parameter to no will prevent winbind to include the system /etc/krb5.conf file into the krb5.conf file it creates. See also . This option only applies to Samba built with MIT Kerberos.

### `neutralize nt4 emulation`

Section: winbind; Context: G; Type: boolean; Default: `no`

This option controls whether winbindd sends the NETLOGON_NEG_NEUTRALIZE_NT4_EMULATION flag in order to bypass the NT4 emulation of a domain controller. Typically you should not need set this. It can be useful for upgrades from NT4 to AD domains. The behavior can be controlled per netbios domain by using 'neutralize nt4 emulation:NETBIOSDOMAIN = yes' as option.

### `reject aes netlogon servers`

Section: winbind; Context: G; Type: boolean; Default: `no`

This option controls whether winbindd requires support for ServerAuthenticateKerberos support for the netlogon secure channel. Support for ServerAuthenticateKerberos was added in Windows starting with Server 2025, it's available in Samba active directory domain controllers starting with 4.22 with the ' yes ' option, which is disabled by default. The following flags will be required: NETLOGON_NEG_PASSWORD_SET2, NETLOGON_NEG_SUPPORTS_KERBEROS_AUTH and NETLOGON_NEG_AUTHENTICATED_RPC. You can set this to yes if all domain controllers support ServerAuthenticateKerberos. This will prevent downgrade attacks. The behavior can be controlled per netbios domain by using 'reject aes netlogon servers:NETBIOSDOMAIN = no' as option. This option overrides the option. This option overrides the option (if it is effectively off).

### `reject md5 servers`

Section: winbind; Context: G; Type: boolean; Default: `yes`

This option controls whether winbindd requires support for aes support for the netlogon secure channel. The following flags will be required NETLOGON_NEG_ARCFOUR, NETLOGON_NEG_SUPPORTS_AES, NETLOGON_NEG_PASSWORD_SET2 and NETLOGON_NEG_AUTHENTICATED_RPC. You can set this to yes if all domain controllers support aes. This will prevent downgrade attacks. The behavior can be controlled per netbios domain by using 'reject md5 servers:NETBIOSDOMAIN = no' as option. The default changed from 'no' to 'yes, with the patches for CVE-2022-38023, see https://bugzilla.samba.org/show_bug.cgi?id=15240 This option is over-ridden by the option. This option overrides the option.

### `require strong key`

Section: winbind; Context: G; Type: boolean; Default: `yes`

This option controls whether winbindd requires support for md5 strong key support for the netlogon secure channel. The following flags will be required NETLOGON_NEG_STRONG_KEYS, NETLOGON_NEG_ARCFOUR and NETLOGON_NEG_AUTHENTICATED_RPC. You can set this to no if some domain controllers only support des. This might allows weak crypto to be negotiated, may via downgrade attacks. The behavior can be controlled per netbios domain by using 'require strong key:NETBIOSDOMAIN = no' as option. Note for active directory domain this option is hardcoded to 'yes' This option is over-ridden by the option. This option overrides the option.

### `template homedir`

Section: winbind; Context: G; Type: string; Default: `/home/%D/%U`

When filling out the user information for a Windows NT user, the winbindd 8 daemon uses this parameter to fill in the home directory for that user. If the string %D is present it is substituted with the user's Windows NT domain name. If the string %U is present it is substituted with the user's Windows NT user name.

### `template shell`

Section: winbind; Context: G; Type: string; Default: `/bin/false`

When filling out the user information for a Windows NT user, the winbindd 8 daemon uses this parameter to fill in the login shell for that user.

### `winbind cache time`

Section: winbind; Context: G; Type: integer; Default: `300`

This parameter specifies the number of seconds the winbindd 8 daemon will cache user and group information before querying a Windows NT server again. This does not apply to authentication requests, these are always evaluated in real time unless the option has been enabled.

### `winbindd socket directory`

Section: winbind; Context: G; Type: string

This setting controls the location of the winbind daemon's socket. Except within automated test scripts, this should not be altered, as the client tools (nss_winbind etc) do not honour this parameter. Client tools must then be advised of the altered path with the WINBINDD_SOCKET_DIR environment variable.

### `winbind enum groups`

Section: winbind; Context: G; Type: boolean; Default: `no`

On large installations using winbindd 8 it may be necessary to suppress the enumeration of groups through the setgrent() , getgrent() and endgrent() group of system calls. If the winbind enum groups parameter is no , calls to the getgrent() system call will not return any data. Turning off group enumeration may cause some programs to behave oddly.

### `winbind enum users`

Section: winbind; Context: G; Type: boolean; Default: `no`

On large installations using winbindd 8 it may be necessary to suppress the enumeration of users through the setpwent() , getpwent() and endpwent() group of system calls. If the winbind enum users parameter is no , calls to the getpwent system call will not return any data. Turning off user enumeration may cause some programs to behave oddly. For example, the finger program relies on having access to the full user list when searching for matching usernames.

### `winbind expand groups`

Section: winbind; Context: G; Type: integer; Default: `0`

This option controls the maximum depth that winbindd will traverse when flattening nested group memberships of Windows domain groups. This is different from the option which implements the Windows NT4 model of local group nesting. The "winbind expand groups" parameter specifically applies to the membership of domain groups. This option also affects the return of non nested group memberships of Windows domain users. With the new default "winbind expand groups = 0" winbind does not query group memberships at all. Be aware that a high value for this parameter can result in system slowdown as the main parent winbindd daemon must perform the group unrolling and will be unable to answer incoming NSS or authentication requests during this time. The default value was changed from 1 to 0 with Samba 4.2. Some broken applications (including some implementations of newgrp and sg) calculate the group memberships of users by traversing groups, such applications will require "winbind expand groups = 1". But the new default makes winbindd more reliable as it doesn't require SAMR access to domain controllers of trusted domains.

### `winbind:ignore domains`

Section: winbind; Context: G; Type: cmdlist

Allows one to enter a list of trusted domains winbind should ignore (untrust). This can avoid the overhead of resources from attempting to login to DCs that should not be communicated with.

### `winbind max clients`

Section: winbind; Context: G; Type: integer; Default: `200`

This parameter specifies the maximum number of clients the winbindd 8 daemon can connect with. The parameter is not a hard limit. The winbindd 8 daemon configures itself to be able to accept at least that many connections, and if the limit is reached, an attempt is made to disconnect idle clients.

### `winbind max domain connections`

Section: winbind; Context: G; Type: integer; Default: `1`

This parameter specifies the maximum number of simultaneous connections that the winbindd 8 daemon should open to the domain controller of one domain. Setting this parameter to a value greater than 1 can improve scalability with many simultaneous winbind requests, some of which might be slow. Changing this value requires a restart of winbindd. Note that if is set to Yes , then only one DC connection is allowed per domain, regardless of this setting.

### `winbind nested groups`

Section: winbind; Context: G; Type: boolean; Default: `yes`

If set to yes, this parameter activates the support for nested groups. Nested groups are also called local groups or aliases. They work like their counterparts in Windows: Nested groups are defined locally on any machine (they are shared between DC's through their SAM) and can contain users and global groups from any trusted SAM. To be able to use nested groups, you need to run nss_winbind.

### `winbind normalize names`

Section: winbind; Context: G; Type: boolean; Default: `no`

This parameter controls whether winbindd will replace whitespace in user and group names with an underscore (_) character. For example, whether the name "Space Kadet" should be replaced with the string "space_kadet". Frequently Unix shell scripts will have difficulty with usernames contains whitespace due to the default field separator in the shell. If your domain possesses names containing the underscore character, this option may cause problems unless the name aliasing feature is supported by your nss_info plugin. This feature also enables the name aliasing API which can be used to make domain user and group names to a non-qualified version. Please refer to the manpage for the configured idmap and nss_info plugin for the specifics on how to configure name aliasing for a specific configuration. Name aliasing takes precedence (and is mutually exclusive) over the whitespace replacement mechanism discussed previously.

### `winbind offline logon`

Section: winbind; Context: G; Type: boolean; Default: `no`

This parameter is designed to control whether Winbind should allow one to login with the pam_winbind module using Cached Credentials. If enabled, winbindd will store user credentials from successful logins encrypted in a local cache.

### `winbind reconnect delay`

Section: winbind; Context: G; Type: integer; Default: `30`

This parameter specifies the number of seconds the winbindd 8 daemon will wait between attempts to ping Domain Controllers for domains that have been marked offline. When a domain is offline, winbindd will periodically attempt to contact Domain Controllers to check if they have become available again. Before attempting to reconnect, winbindd flushes the negative connection cache for the domain. The negative connection cache stores Domain Controllers that have previously been unresponsive, to avoid repeatedly trying to contact them.

### `winbind refresh tickets`

Section: winbind; Context: G; Type: boolean; Default: `no`

This parameter is designed to control whether Winbind should refresh Kerberos Tickets retrieved using the pam_winbind module.

### `winbind request timeout`

Section: winbind; Context: G; Type: integer; Default: `60`

This parameter specifies the number of seconds the winbindd 8 daemon will wait before disconnecting either a client connection with no outstanding requests (idle) or a client connection with a request that has remained outstanding (hung) for longer than this number of seconds. A winbind client is any local program on the system that queries winbindd for user or group information, or to authenticate users. Common examples include wbinfo 1 , smbd 8 , pam_winbind 8 , and nss_winbind 8 .

### `winbind rpc only`

Section: winbind; Context: G; Type: boolean; Default: `no`

Setting this parameter to yes forces winbindd to use RPC instead of LDAP to retrieve information from Domain Controllers.

### `winbind scan trusted domains`

Section: winbind; Context: G; Type: boolean; Default: `no`

This option only takes effect when the option is set to domain or ads . If it is set to yes, winbindd periodically tries to scan for new trusted domains and adds them to a global list inside of winbindd. The list can be extracted with wbinfo --trusted-domains --verbose . Setting it to yes matches the behaviour of Samba 4.7 and older. The construction of that global list is not reliable and often incomplete in complex trust setups. In most situations the list is not needed any more for winbindd to operate correctly. E.g. for plain file serving via SMB using a simple idmap setup with autorid , tdb or ad . However some more complex setups require the list, e.g. if you specify idmap backends for specific domains. Some pam_winbind setups may also require the global list. If you have a setup that doesn't require the global list, you should set no .

### `winbind sealed pipes`

Section: winbind; Context: G; Type: boolean; Default: `yes`

This option controls whether any requests from winbindd to domain controllers pipe will be sealed. Disabling sealing can be useful for debugging purposes. The behavior can be controlled per netbios domain by using 'winbind sealed pipes:NETBIOSDOMAIN = no' as option.

### `winbind separator`

Section: winbind; Context: G; Type: string; Default: `\`

This parameter allows an admin to define the character used when listing a username of the form of DOMAIN \ user . This parameter is only applicable when using the pam_winbind.so and nss_winbind.so modules for UNIX services. Please note that setting this parameter to + causes problems with group membership at least on glibc systems, as the character + is used as a special character for NIS in /etc/group.

### `winbind use default domain`

Section: winbind; Context: G; Type: boolean; Default: `no`

This parameter specifies whether the winbindd 8 daemon should operate on users without domain component in their username. Users without a domain component are treated as is part of the winbindd server's own domain. While this does not benefit Windows users, it makes SSH, FTP and e-mail function in a way much closer to the way they would in a native unix system. This option should be avoided if possible. It can cause confusion about responsibilities for a user or group. In many situations it is not clear whether winbind or /etc/passwd should be seen as authoritative for a user, likewise for groups.

### `winbind use krb5 enterprise principals`

Section: winbind; Context: G; Type: boolean; Default: `yes`

winbindd is able to get kerberos tickets for pam_winbind with krb5_auth or wbinfo -K/--krb5auth=. winbindd (at least on a domain member) is never be able to have a complete picture of the trust topology (which is managed by the DCs). There might be uPNSuffixes and msDS-SPNSuffixes values, which don't belong to any AD domain at all. With no winbindd doesn't even get a complete picture of the topology. It is not really required to know about the trust topology. We can just rely on the [K]DCs of our primary domain (e.g. PRIMARY.A.EXAMPLE.COM) and use enterprise principals e.g. upnfromB@B.EXAMPLE.COM@PRIMARY.A.EXAMPLE.COM and follow the WRONG_REALM referrals in order to find the correct DC. The final principal might be userfromB@INTERNALB.EXAMPLE.PRIVATE. With yes winbindd enterprise principals will be used.

### `winbind varlink service`

Section: winbind; Context: G; Type: boolean; Default: `no`

This setting controls whether winbind 8 will listen for User/Group record lookup from nss-systemd 8 via Varlink, offering an alternative to nss_winbind. For more information about User/Group record lookup via Varlink see https://systemd.io/USER_GROUP_API/ and nss-systemd 8 manpage. Systemd 1 versions prior 253 consider the default '\' an unsafe character in the GetMemberhips reply. To workaround the issue it is recommended to set it to '+' for example. This setting has no effect in platforms or distributions without systemd 1 .
