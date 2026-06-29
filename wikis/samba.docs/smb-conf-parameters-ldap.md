# smb.conf Parameters / ldap

### `client ldap sasl wrapping`

Section: ldap; Context: G; Type: enum; Default: `seal`

The defines whether ldap traffic will be signed or signed and encrypted (sealed). Possible values are plain , sign and seal . The values sign and seal are only available if Samba has been compiled against a modern OpenLDAP version (2.3.x or higher). This option is needed firstly to secure the privacy of administrative connections from samba-tool , including in particular new or reset passwords for users. For this reason the default is seal . Additionally, winbindd and the net tool can use LDAP to communicate with Domain Controllers, so this option also controls the level of privacy for those connections. All supported AD DC versions will enforce the usage of at least signed LDAP connections by default, so a value of at least sign is required in practice. The default value is seal . That implies synchronizing the time with the KDC in the case of using Kerberos . In order to force using LDAP (on port 389) with STARTTLS or LDAPS (on port 636), it is possible to use starttls or ldaps . In that case the NTLMSSP or Kerberos authentication using the TLS channel bindings in order to glue it to the connection.

### `ldap admin dn`

Section: ldap; Context: G; Type: string

The defines the Distinguished Name (DN) name used by Samba to contact the ldap server when retrieving user account information. The is used in conjunction with the admin dn password stored in the private/secrets.tdb file. See the smbpasswd 8 man page for more information on how to accomplish this. The requires a fully specified DN. The is not appended to the .

### `ldap connection timeout`

Section: ldap; Context: G; Type: integer; Default: `2`

This parameter tells the LDAP library calls which timeout in seconds they should honor during initial connection establishments to LDAP servers. It is very useful in failover scenarios in particular. If one or more LDAP servers are not reachable at all, we do not have to wait until TCP timeouts are over. This feature must be supported by your LDAP library. This parameter is different from which affects operations on LDAP servers using an existing connection and not establishing an initial connection.

### `ldap delete dn`

Section: ldap; Context: G; Type: boolean; Default: `no`

This parameter specifies whether a delete operation in the ldapsam deletes the complete entry or only the attributes specific to Samba.

### `ldap deref`

Section: ldap; Context: G; Type: enum; Default: `auto`

This option controls whether Samba should tell the LDAP library to use a certain alias dereferencing method. The default is auto , which means that the default setting of the ldap client library will be kept. Other possible values are never , finding , searching and always . Grab your LDAP manual for more information.

### `ldap follow referral`

Section: ldap; Context: G; Type: enum; Default: `auto`

This option controls whether to follow LDAP referrals or not when searching for entries in the LDAP database. Possible values are on to enable following referrals, off to disable this, and auto , to use the libldap default settings. libldap's choice of following referrals or not is set in /etc/openldap/ldap.conf with the REFERRALS parameter as documented in ldap.conf(5).

### `ldap group suffix`

Section: ldap; Context: G; Type: string

This parameter specifies the suffix that is used for groups when these are added to the LDAP directory. If this parameter is unset, the value of will be used instead. The suffix string is prepended to the string so use a partial DN.

### `ldap idmap suffix`

Section: ldap; Context: G; Type: string

This parameters specifies the suffix that is used when storing idmap mappings. If this parameter is unset, the value of will be used instead. The suffix string is prepended to the string so use a partial DN.

### `ldap machine suffix`

Section: ldap; Context: G; Type: string

It specifies where machines should be added to the ldap tree. If this parameter is unset, the value of will be used instead. The suffix string is prepended to the string so use a partial DN.

### `ldap max anonymous request size`

Section: ldap; Context: G; Type: integer; Default: `256000`

This parameter specifies the maximum permitted size (in bytes) for an LDAP request received on an anonymous connection. If the request size exceeds this limit the request will be rejected.

### `ldap max authenticated request size`

Section: ldap; Context: G; Type: integer; Default: `16777216`

This parameter specifies the maximum permitted size (in bytes) for an LDAP request received on an authenticated connection. If the request size exceeds this limit the request will be rejected.

### `ldap max search request size`

Section: ldap; Context: G; Type: integer; Default: `256000`

This parameter specifies the maximum permitted size (in bytes) for an LDAP search request. If the request size exceeds this limit the request will be rejected.

### `ldap page size`

Section: ldap; Context: G; Type: integer; Default: `1000`

This parameter specifies the number of entries per page. If the LDAP server supports paged results, clients can request subsets of search results (pages) instead of the entire list. This parameter specifies the size of these pages.

### `ldap passwd sync`

Section: ldap; Context: G; Type: enum; Default: `no`

This option is used to define whether or not Samba should sync the LDAP password with the NT and LM hashes for normal accounts (NOT for workstation, server or domain trusts) on a password change via SAMBA. The can be set to one of three values: Yes = Try to update the LDAP, NT and LM passwords and update the pwdLastSet time. No = Update NT and LM passwords and update the pwdLastSet time. Only = Only update the LDAP password and let the LDAP server do the rest.

### `ldap replication sleep`

Section: ldap; Context: G; Type: integer; Default: `1000`

When Samba is asked to write to a read-only LDAP replica, we are redirected to talk to the read-write master server. This server then replicates our changes back to the 'local' server, however the replication might take some seconds, especially over slow links. Certain client activities, particularly domain joins, can become confused by the 'success' that does not immediately change the LDAP back-end's data. This option simply causes Samba to wait a short time, to allow the LDAP server to catch up. If you have a particularly high-latency network, you may wish to time the LDAP replication with a network sniffer, and increase this value accordingly. Be aware that no checking is performed that the data has actually replicated. The value is specified in milliseconds, the maximum value is 5000 (5 seconds).

### `ldapsam:editposix`

Section: ldap; Context: G; Type: string; Default: `no`

Editposix is an option that leverages ldapsam:trusted to make it simpler to manage a domain controller eliminating the need to set up custom scripts to add and manage the posix users and groups. This option will instead directly manipulate the ldap tree to create, remove and modify user and group entries. This option also requires a running winbindd as it is used to allocate new uids/gids on user/group creation. The allocation range must be therefore configured. To use this option, a basic ldap tree must be provided and the ldap suffix parameters must be properly configured. On virgin servers the default users and groups (Administrator, Guest, Domain Users, Domain Admins, Domain Guests) can be precreated with the command net sam provision . To run this command the ldap server must be running, Winbindd must be running and the smb.conf ldap options must be properly configured. The typical ldap setup used with the yes option is usually sufficient to use yes as well. An example configuration can be the following: encrypt passwords = true passdb backend = ldapsam ldapsam:trusted=yes ldapsam:editposix=yes ldap admin dn = cn=admin,dc=samba,dc=org ldap delete dn = yes ldap group suffix = ou=groups ldap idmap suffix = ou=idmap ldap machine suffix = ou=computers ldap user suffix = ou=users ldap suffix = dc=samba,dc=org idmap backend = ldap:"ldap://localhost" idmap uid = 5000-50000 idmap gid = 5000-50000 This configuration assumes a directory layout like described in the following ldif: dn: dc=samba,dc=org objectClass: top objectClass: dcObject objectClass: organization o: samba.org dc: samba dn: cn=admin,dc=samba,dc=org objectClass: simpleSecurityObject objectClass: organizationalRole cn: admin description: LDAP administrator userPassword: secret dn: ou=users,dc=samba,dc=org objectClass: top objectClass: organizationalUnit ou: users dn: ou=groups,dc=samba,dc=org objectClass: top objectClass: organizationalUnit ou: groups dn: ou=idmap,dc=samba,dc=org objectClass: top objectClass: organizationalUnit ou: idmap dn: ou=computers,dc=samba,dc=org objectClass: top objectClass: organizationalUnit ou: computers

### `ldapsam:trusted`

Section: ldap; Context: G; Type: string; Default: `no`

By default, Samba as a Domain Controller with an LDAP backend needs to use the Unix-style NSS subsystem to access user and group information. Due to the way Unix stores user information in /etc/passwd and /etc/group this inevitably leads to inefficiencies. One important question a user needs to know is the list of groups he is member of. The plain UNIX model involves a complete enumeration of the file /etc/group and its NSS counterparts in LDAP. UNIX has optimized functions to enumerate group membership. Sadly, other functions that are used to deal with user and group attributes lack such optimization. To make Samba scale well in large environments, the yes option assumes that the complete user and group database that is relevant to Samba is stored in LDAP with the standard posixAccount/posixGroup attributes. It further assumes that the Samba auxiliary object classes are stored together with the POSIX data in the same LDAP object. If these assumptions are met, yes can be activated and Samba can bypass the NSS system to query user group memberships. Optimized LDAP queries can greatly speed up domain logon and administration tasks. Depending on the size of the LDAP database a factor of 100 or more for common queries is easily achieved.

### `ldap server require strong auth`

Section: ldap; Context: G; Type: enum; Default: `yes`

The defines whether the ldap server requires ldap traffic to be signed or signed and encrypted (sealed). Possible values are no , allow_sasl_without_tls_channel_bindings and yes . Windows has LdapEnforceChannelBinding under HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters\ . A value of no allows simple and sasl binds over all transports. This matches LdapEnforceChannelBinding=0. A value of allow_sasl_without_tls_channel_bindings allows simple and sasl binds (without sign or seal) over TLS encrypted connections. Missing tls channel bindings are ignored, so only use this if a value of yes is not possible. Unencrypted connections only allow sasl binds with sign or seal. This matches LdapEnforceChannelBinding=1. Before support for tls channel bindings existed in Samba, a value of allow_sasl_over_tls was possible in order to allow sasl binds without tls channel bindings. This is now misleading as a value of yes will now allow sasl binds with tls channel bindings. Configurations should be changed to yes instead or allow_sasl_without_tls_channel_bindings if really required. Currently allow_sasl_over_tls is just an alias of allow_sasl_without_tls_channel_bindings , but it will be removed in future versions. A value of yes allows only simple binds and sasl binds with correct tls channel bindings over TLS encrypted connections. sasl binds without tls channel bindings are not allowed. Unencrypted connections only allow sasl binds with sign or seal. This matches LdapEnforceChannelBinding=2.

### `ldap ssl`

Section: ldap; Context: G; Type: enum; Default: `start tls`

This option is used to define whether or not Samba should use SSL when connecting to the ldap server This is NOT related to Samba's previous SSL support which was enabled by specifying the --with-ssl option to the configure script. LDAP connections should be secured where possible. This may be done setting either this parameter to start tls or by specifying ldaps:// in the URL argument of . The can be set to one of two values: Off = Never use SSL when querying the directory. start tls = Use the LDAPv3 StartTLS extended operation (RFC2830) for communicating with the directory server. Please note that this parameter does only affect rpc methods.

### `ldap suffix`

Section: ldap; Context: G; Type: string

Specifies the base for all ldap suffixes and for storing the sambaDomain object. The ldap suffix will be appended to the values specified for the , , , and the . Each of these should be given only a DN relative to the .

### `ldap timeout`

Section: ldap; Context: G; Type: integer; Default: `15`

This parameter defines the number of seconds that Samba should use as timeout for LDAP operations.

### `ldap user suffix`

Section: ldap; Context: G; Type: string

This parameter specifies where users are added to the tree. If this parameter is unset, the value of will be used instead. The suffix string is prepended to the string so use a partial DN.
