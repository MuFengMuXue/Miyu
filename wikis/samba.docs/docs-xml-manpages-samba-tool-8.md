# Docs Xml / Manpages / Samba tool.8

samba-tool

8

Samba

System Administration tools

samba-tool

Main Samba administration tool.

samba-tool

-h

-W myworkgroup

-U user

-d debuglevel

-V

# DESCRIPTION

This tool is part of the `samba(7)` suite.

# OPTIONS

Samba-tool consists of many sub-commands, each of which have their own set of options. The options listed in this section are common across several sub-commands.

-h\|--help
Show a help message and exit.

-H URL, --URL=URL
LDB URL for database or target server.

The URL can either be a plain file path, or use one of the schemes listed here. If a plain path is used, it is treated as if 'tdb://' was used.

tdb://PATH
PATH is the location of a TDB database.

mdb://PATH
PATH is the location of an LMDB database.

ldb://PATH
PATH is the location of an LDB database, in either LMDB or TDB format. The formats will be tried one after another until one succeeds or all fail. It is safe to use this if you don't know the format of the file.

ldap://HOSTNAME, ldaps://HOSTNAME
The LDB backend is the named ldap server. ldaps:// wraps the connection in TLS.

ldapi://SOCKET
The backend server is a local ldap server using a unix domain socket.

--color=always\|never\|auto
use colour if available (default: auto)

--ipaddress=IPADDRESS
IP address of the server

-s FILE, --configfile=FILE
Use this smb.conf configuration file.

--color=always\|never\|auto
Indicate whether samba-tool should use ANSI colour codes in its output. If 'auto' (the default), samba-tool will use colour when its output is directed toward a terminal, unless the NO_COLOR environment variable is set and non-empty.

The values 'yes' and 'force' are accepted as synonyms for 'always'; 'no' and 'none' for 'never'; and 'tty' and 'if-tty' for 'auto'.

Note that asking for colour doesn't mean samba-tool will necessarily be very colourful. Many commands are very monochrome, particularly when successful.

-V, --version
Display the version number and exit.

# COMMANDS

## computer

Manage computer accounts.

### computer add \<computername\> \[options\]

Add a new computer to the Active Directory Domain.

The new computer name specified on the command is the sAMAccountName, with or without the trailing dollar sign.

--computerou=COMPUTEROU
DN of alternative location (with or without domainDN counterpart) to default CN=Computers in which new computer object will be created. E.g. 'OU=OUname'.

--description=DESCRIPTION
The new computer's description.

--ip-address=IP_ADDRESS_LIST
IPv4 address for the computer's A record, or IPv6 address for AAAA record, can be provided multiple times.

--service-principal-name=SERVICE_PRINCIPAL_NAME_LIST
Computer's Service Principal Name, can be provided multiple times.

--prepare-oldjoin
Prepare enabled machine account for oldjoin mechanism.

### computer create \<computername\> \[options\]

Add a new computer. This is a synonym for the `samba-tool computer add` command and is available for compatibility reasons only. Please use `samba-tool computer add` instead.

### computer delete \<computername\> \[options\]

Delete an existing computer account.

The computer name specified on the command is the sAMAccountName, with or without the trailing dollar sign.

### computer edit \<computername\>

Edit a computer AD object.

The computer name specified on the command is the sAMAccountName, with or without the trailing dollar sign.

--editor=EDITOR
Specifies the editor to use instead of the system default, or 'vi' if no system default is set.

### computer list

List all computers.

### computer move \<computername\> \<new_parent_dn\> \[options\]

This command moves a computer account into the specified organizational unit or container.

The computername specified on the command is the sAMAccountName, with or without the trailing dollar sign.

The name of the organizational unit or container can be specified as a full DN or without the domainDN component.

### computer show \<computername\> \[options\]

Display a computer AD object.

The computer name specified on the command is the sAMAccountName, with or without the trailing dollar sign.

--attributes=USER_ATTRS
Comma separated list of attributes, which will be printed.

## computer keytrust

Manage Key Credential Links for a computer.

This can populate, describe or delete msDS-KeyCredentialLink attributes.

### computer keytrust add \<computername\> \\[options\]

Add a key-credential-link, which is a linked attribute that holds a public key in a binary field.

The second argument is a filename that should refer to a 2048 bit RSA key (or a certificate containing that key) in PEM or DER format. By default the encoding format will be detected automatically, but you can attempt to override this with `--encoding` option. Other types of public key are not supported, though the `--force` option can be used to add a non-2048 bit key.

--link-target=DN
link to this DN (default: the computer's DN)

--encoding=ENCODING
Key format, either `pem`, `der`, or `auto`. The default is `auto`, which is likely to detect the correct format in all circumstances.

--force
proceed with operations that seems ill-fated

### computer keytrust delete \<computername\> \[options\]

Delete a key-credential-link.

The link to be deleted can be selected in a number of ways. `--all` will delete all key credential links for the computer (often there will only be one). The `--link-target` option selects a key credential link based on the DN targeted by the link. The `--fingerprint` option selects a link to delete based on the key fingerprint. This is the SHA256 of the DER-encoded key material, expressed as hex-pairs separated by colons. See `computer keytrust view` to get a list of links and their fingerprints.

If more than one of `--link-target`, `--fingerprint`, and `--all` are used, links matched by any of them will be deleted.

The `--dry-run` option will prevent links from being deleted, and instead indicate what would happen if it was omitted.

--link-target=DN
Delete this key credential link (a DN)

--fingerprint=HH:HH:..
Delete the key credential link with this key fingerprint

--all
Delete all key credential links

-n, --dry-run
Do nothing but print what would happen

### computer keytrust view \<computername\> \[options\]

View a computer's key credential links. This can be used to find a link's fingerprint and target DN for

. The `--verbose` includes more, probably useless, information.

-h, --help
show this help message and exit

-v, --verbose
Be verbose

### computer generate-csr \<computername\> \<subject_name\> \ \<output_filename\> \[options\]

Generate a PEM‐encoded Certificate Signing Request for a computer.

--private-key-encoding
Specify which encoding the private key uses. Default is 'auto'.

--private-key-pass
Provide a password to decrypt the private key.

## contact

Manage contacts.

### contact add \[\<contactname\>\] \[options\]

Add a new contact to the Active Directory Domain.

The name of the new contact can be specified by the first argument 'contactname' or the --given-name, --initial and --surname arguments. If no 'contactname' is given, contact's name will be made up of the given arguments by combining the given-name, initials and surname. Each argument is optional. A dot ('.') will be appended to the initials automatically.

--ou=OU
DN of alternative location (with or without domainDN counterpart) in which the new contact will be created. E.g. 'OU=OUname'. Default is the domain base.

--description=DESCRIPTION
The new contact's description.

--surname=SURNAME
Contact's surname.

--given-name=GIVEN_NAME
Contact's given name.

--initials=INITIALS
Contact's initials.

--display-name=DISPLAY_NAME
Contact's display name.

--job-title=JOB_TITLE
Contact's job title.

--department=DEPARTMENT
Contact's department.

--company=COMPANY
Contact's company.

--mail-address=MAIL_ADDRESS
Contact's email address.

--internet-address=INTERNET_ADDRESS
Contact's home page.

--telephone-number=TELEPHONE_NUMBER
Contact's phone number.

--mobile-number=MOBILE_NUMBER
Contact's mobile phone number.

--physical-delivery-office=PHYSICAL_DELIVERY_OFFICE
Contact's office location.

### contact create \[\<contactname\>\] \[options\]

Add a new contact. This is a synonym for the `samba-tool contact add` command and is available for compatibility reasons only. Please use `samba-tool contact add` instead.

### contact delete \<contactname\> \[options\]

Delete an existing contact.

The contactname specified on the command is the common name or the distinguished name of the contact object. The distinguished name of the contact can be specified with or without the domainDN component.

### contact edit \<contactname\>

Modify a contact AD object.

The contactname specified on the command is the common name or the distinguished name of the contact object. The distinguished name of the contact can be specified with or without the domainDN component.

--editor=EDITOR
Specifies the editor to use instead of the system default, or 'vi' if no system default is set.

### contact list \[options\]

List all contacts.

--full-dn
Display contact's full DN instead of the name.

### contact move \<contactname\> \<new_parent_dn\> \[options\]

This command moves a contact into the specified organizational unit or container.

The contactname specified on the command is the common name or the distinguished name of the contact object. The distinguished name of the contact can be specified with or without the domainDN component.

### contact show \<contactname\> \[options\]

Display a contact AD object.

The contactname specified on the command is the common name or the distinguished name of the contact object. The distinguished name of the contact can be specified with or without the domainDN component.

--attributes=CONTACT_ATTRS
Comma separated list of attributes, which will be printed.

### contact rename \<contactname\> \[options\]

Rename a contact and related attributes.

This command allows to set the contact's name related attributes. The contact's CN will be renamed automatically. The contact's new CN will be made up by combining the given-name, initials and surname. A dot ('.') will be appended to the initials automatically, if required. Use the --force-new-cn option to specify the new CN manually and --reset-cn to reset this change.

Use an empty attribute value to remove the specified attribute.

The contact name specified on the command is the CN.

--surname=SURNAME
New surname.

--given-name=GIVEN_NAME
New given name.

--initials=INITIALS
New initials.

--force-new-cn=NEW_CN
Specify a new CN (RDN) instead of using a combination of the given name, initials and surname.

--reset-cn
Set the CN to the default combination of given name, initials and surname.

--display-name=DISPLAY_NAME
New display name.

--mail-address=MAIL_ADDRESS
New email address.

## dbcheck

Check the local AD database for errors.

## delegation

Manage Delegations.

### delegation add-principal \<accountname\> \ \[options\]

Add a principal to msDS-AllowedToActOnBehalfOfOtherIdentity that may delegate to an account.

### delegation del-principal \<accountname\> \ \[options\]

Delete a principal from msDS-AllowedToActOnBehalfOfOtherIdentity so that it may no longer delegate to an account.

### delegation add-service \<accountname\> \ \[options\]

Add a service principal as msDS-AllowedToDelegateTo.

### delegation del-service \<accountname\> \ \[options\]

Delete a service principal as msDS-AllowedToDelegateTo.

### delegation for-any-protocol \<accountname\> \[(on\|off)\] \[options\]

Set/unset UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION (S4U2Proxy) for an account.

### delegation for-any-service \<accountname\> \[(on\|off)\] \[options\]

Set/unset UF_TRUSTED_FOR_DELEGATION for an account.

### delegation show \<accountname\> \[options\]

Show the delegation setting of an account.

## dns

Manage Domain Name Service (DNS).

### dns add \<server\> \<zone\> \<name\> \<A\|AAAA\|PTR\|CNAME\|NS\|MX\|SRV\|TXT\> \<data\>

Add a DNS record.

--allow-existing
Do not treat an existing record of this name and type as an error. This has no functional change (the new DNS record is not added) but the message and samba-tool return code will not indicate error.

### dns cleanup \<server\> \<name\>

Clean up DNS records for a host, so that DNS queries no longer return results. Usually this works by marking the records as deleted in the database.

Example: `samba-tool dns cleanup dc1 computer.samdom.test.site`

### dns delete \<server\> \<zone\> \<name\> \<A\|AAAA\|PTR\|CNAME\|NS\|MX\|SRV\|TXT\> \<data\>

Delete a DNS record.

### dns query \<server\> \<zone\> \<name\> \<A\|AAAA\|PTR\|CNAME\|NS\|MX\|SRV\|TXT\|ALL\> \[options\] \<data\>

Query a name.

### dns roothints \<server\> \[\<name\>\] \[options\]

Query root hints.

### dns serverinfo \<server\> \[options\]

Query server information.

### dns update \<server\> \<zone\> \<name\> \<A\|AAAA\|PTR\|CNAME\|NS\|MX\|SRV\|TXT\> \<olddata\> \<newdata\>

Update a DNS record.

### dns zonecreate \<server\> \<zone\> \[options\]

Create a zone.

### dns zonedelete \<server\> \<zone\> \[options\]

Delete a zone.

### dns zoneinfo \<server\> \<zone\> \[options\]

Query zone information.

### dns zonelist \<server\> \[options\]

List zones.

### dns zoneoptions \<server\> \<zone\> \[options\]

Manipulate aging options. This is useful in zones using dynamic DNS.

There are options to change records from static to dynamic based on regular expressions or age, which is useful in some cases where the values got mixed up in old versions of Samba.

-n, --dry-run
Do not actually change anything, but show what would happen.

--client-version=w2k\|dotnet\|longhorn
Windows client protocol version. The default is `longhorn`, which is probably what you want.

--mark-old-records-static=YYYY-MM-DD
Mark records older than the specified date as static.

--mark-records-static-regex=REGEXP
Mark records that match the given perl-compatible regular expression as static.

--mark-records-dynamic-regex=REGEXP
Mark records that match the given perl-compatible regular expression as dynamic.

--aging=0\|1
--aging=1 to enable aging for this zone.

--aging=0 to disable aging for this zone.

--norefreshinterval=HOURS
avoid further refreshes for this long after a dynamic update. Set to zero to use the default.

--refreshinterval=HOURS
Dynamic refresh interval in hours (0: use default)


## domain

Manage Domain.

### domain backup

Create or restore a backup of the domain.

### domain backup offline

Backup (with proper locking) local domain directories into a tar file.

### domain backup online

Copy a running DC's current DB into a backup tar file.

### domain backup rename

Copy a running DC's DB to backup file, renaming the domain in the process.

### domain backup restore

Restore the domain's DB from a backup-file.

## domain auth policy

Manage authentication policies.

### domain auth policy list

List authentication policies on the domain.

-H, --URL
LDB URL for database or target server.

--json
View authentication policies as JSON instead of a list.

### domain auth policy view

View an authentication policy on the domain.

-H, --URL
LDB URL for database or target server.

--name
Name of the authentication policy to view (required).

### domain auth policy create

Create authentication policies on the domain.

-H, --URL
LDB URL for database or target server.

--name
Name of the authentication policy (required).

--description
Optional description for the authentication policy.

--protect
Protect authentication policy from accidental deletion.

Cannot be used together with --unprotect.

--unprotect
Unprotect authentication policy from accidental deletion.

Cannot be used together with --protect.

--audit
Only audit authentication policy.

Cannot be used together with --enforce.

--enforce
Enforce authentication policy.

Cannot be used together with --audit.

--strong-ntlm-policy
Strong NTLM Policy (Disabled, Optional, Required).

--user-tgt-lifetime-mins
Ticket-Granting-Ticket lifetime for user accounts.

--user-allow-ntlm-auth
Allow `NTLM` and `Interactive NETLOGON SamLogon` authentication despite the fact that `allowed-to-authenticate-from` is in use, which would otherwise restrict the user to selected devices.

--user-allowed-to-authenticate-from
Conditions a device must meet for users covered by this policy to be allowed to authenticate. While this is a restriction on the device, any conditional ACE rules are expressed as if the device was a user.

Must be a valid SDDL string without reference to Device keywords.

Example: `O:SYG:SYD:(XA;OICI;CR;;;WD;(Member_of {SID(AU)}))`

--user-allowed-to-authenticate-to=SDDL
This policy, applying to a user account that is offering a service, eg a web server with a user account, restricts which accounts may access it.

Must be a valid SDDL string. The SDDL can reference both bare (user) and Device conditions.

SDDL Example: `O:SYG:SYD:(XA;OICI;CR;;;WD;(Member_of {SID(AO)}))`

--service-tgt-lifetime-mins
Ticket-Granting-Ticket lifetime for service accounts.

--service-allow-ntlm-auth
Allow NTLM network authentication when service is restricted to selected devices.

--service-allowed-to-authenticate-from
Conditions a device must meet for service accounts covered by this policy to be allowed to authenticate. While this is a restriction on the device, any conditional ACE rules are expressed as if the device was a user.

Must be a valid SDDL string without reference to Device keywords.

SDDL Example: `O:SYG:SYD:(XA;OICI;CR;;;WD;(Member_of {SID(AU)}))`

--service-allowed-to-authenticate-to=SDDL
This policy, applying to a service account (eg a Managed Service Account, Group Managed Service Account), restricts which accounts may access it.

Must be a valid SDDL string. The SDDL can reference both bare (user) and Device conditions.

SDDL Example: `O:SYG:SYD:(XA;OICI;CR;;;WD;(Member_of {SID(AO)}))`

--computer-tgt-lifetime-mins
Ticket-Granting-Ticket lifetime for computer accounts.

--computer-allowed-to-authenticate-to=SDDL
This policy, applying to a computer account (eg a server or workstation), restricts which accounts may access it.

Must be a valid SDDL string. The SDDL can reference both bare (user) and Device conditions.

SDDL Example: `O:SYG:SYD:(XA;OICI;CR;;;WD;(Member_of {SID(AO)}))`

### domain auth policy modify

Modify authentication policies on the domain. The same options apply as for `domain auth policy create`.

### domain auth policy delete

Delete authentication policies on the domain.

-H, --URL
LDB URL for database or target server.

--name
Name of authentication policy to delete (required).

--force
Force authentication policy delete even if it is protected.

### domain auth policy user-allowed-to-authenticate-from set

Set the user-allowed-to-authenticate-from property by scenario.

-H, --URL
LDB URL for database or target server.

--name
Name of authentication policy.

--by-group=GROUP
User is allowed to authenticate, if the device they authenticate from is assigned and granted membership of a given `GROUP`.

--silo=SILO
User is allowed to authenticate, if the device they authenticate from is assigned and granted membership of a given `SILO`.

### domain auth policy user-allowed-to-authenticate-to set

Set the user-allowed-to-authenticate-to property by scenario.

-H, --URL
LDB URL for database or target server.

--name
Name of authentication policy.

--group=GROUP
The user account, offering a network service, covered by this policy, will only be allowed access from other accounts that are members of the given `GROUP`.

--silo=SILO
The user account, offering a network service, covered by this policy, will only be allowed access from other accounts that are assigned to, granted membership of (and meet any authentication conditions of) the given `SILO`.

### domain auth policy service-allowed-to-authenticate-from set

Set the service-allowed-to-authenticate-from property by scenario.

-H, --URL
LDB URL for database or target server.

--name
Name of authentication policy.

--group=GROUP
The service account (eg a Managed Service Account, Group Managed Service Account) is allowed to authenticate, if the device it authenticates from is a member of the given `GROUP`.

--silo=SILO
The service account (eg a Managed Service Account, Group Managed Service Account) is allowed to authenticate, if the device it authenticates from is assigned and granted membership of a given `SILO`.

### domain auth policy service-allowed-to-authenticate-to set

Set the service-allowed-to-authenticate-to property by scenario.

-H, --URL
LDB URL for database or target server.

--name
Name of authentication policy.

--group=GROUP
The service account (eg a Managed Service Account, Group Managed Service Account), will only be allowed access by other accounts that are members of the given `GROUP`.

--silo=SILO
The service account (eg a Managed Service Account, Group Managed Service Account), will only be allowed access by other accounts that are assigned to, granted membership of (and meet any authentication conditions of) the given `SILO`.

### domain auth policy computer-allowed-to-authenticate-to set

Set the computer-allowed-to-authenticate-to property by scenario.

-H, --URL
LDB URL for database or target server.

--name
Name of authentication policy.

--group=GROUP
The computer account (eg a server or workstation), will only be allowed access by other accounts that are members of the given `GROUP`.

--silo=SILO
The computer account (eg a server or workstation), will only be allowed access by other accounts that are assigned to, granted membership of (and meet any authentication conditions of) the given `SILO`.

## domain auth silo

Manage authentication silos.

### domain auth silo list

List authentication silos on the domain.

-H, --URL
LDB URL for database or target server.

--json
View authentication silos as JSON instead of a list.

### domain auth silo view

View an authentication silo on the domain.

-H, --URL
LDB URL for database or target server.

--name
Name of the authentication silo to view (required).

### domain auth silo create

Create authentication silos on the domain.

-H, --URL
LDB URL for database or target server.

--name
Name of the authentication silo (required).

--description
Optional description for the authentication silo.

--user-authentication-policy
User account authentication policy.

--service-authentication-policy
Managed service account authentication policy.

--computer-authentication-policy
Computer authentication policy.

--protect
Protect authentication silo from accidental deletion.

Cannot be used together with --unprotect.

--unprotect
Unprotect authentication silo from accidental deletion.

Cannot be used together with --protect.

--audit
Only audit silo policies.

Cannot be used together with --enforce.

--enforce
Enforce silo policies.

Cannot be used together with --audit.

### domain auth silo modify

Modify authentication silos on the domain.

-H, --URL
LDB URL for database or target server.

--name
Name of the authentication silo (required).

--description
Optional description for the authentication silo.

--user-authentication-policy
User account authentication policy.

--service-authentication-policy
Managed service account authentication policy.

--computer-authentication-policy
Computer authentication policy.

--protect
Protect authentication silo from accidental deletion.

Cannot be used together with --unprotect.

--unprotect
Unprotect authentication silo from accidental deletion.

Cannot be used together with --protect.

--audit
Only audit silo policies.

Cannot be used together with --enforce.

--enforce
Enforce silo policies.

Cannot be used together with --audit.

### domain auth silo delete

Delete authentication silos on the domain.

-H, --URL
LDB URL for database or target server.

--name
Name of authentication silo to delete (required).

--force
Force authentication silo delete even if it is protected.

### domain auth silo member grant

Grant a member access to an authentication silo.

-H, --URL
LDB URL for database or target server.

--name
Name of authentication silo (required).

--member
Member to grant access to the silo (DN or account name).

### domain auth silo member list

List members in an authentication silo.

-H, --URL
LDB URL for database or target server.

--name
Name of authentication silo (required).

--json
View members as JSON instead of a list.

### domain auth silo member revoke

Revoke a member from an authentication silo.

-H, --URL
LDB URL for database or target server.

--name
Name of authentication silo (required).

--member
Member to revoke from the silo (DN or account name).

### domain claim claim-type list

List claim types on the domain.

-H, --URL
LDB URL for database or target server.

--json
View claim types as JSON instead of a list.

### domain claim claim-type view

View a single claim type on the domain.

-H, --URL
LDB URL for database or target server.

--name
Display name of claim type to view (required).

### domain claim claim-type create

Create claim types on the domain.

-H, --URL
LDB URL for database or target server.

--attribute
Attribute of claim type to create (required).

--class
Object classes to set claim type to.

Example: --class=user --class=computer

--name
Optional display name or use attribute name.

--description
Optional description or use from attribute.

--enable
Enable claim type.

Cannot be used together with --disable.

--disable
Disable claim type.

Cannot be used together with --enable.

--protect
Protect claim type from accidental deletion.

Cannot be used together with --unprotect.

--unprotect
Unprotect claim type from accidental deletion.

Cannot be used together with --protect.

### domain claim claim-type modify

Modify claim types on the domain.

-H, --URL
LDB URL for database or target server.

--name
Display name of claim type to modify (required).

--class
Object classes to set claim type to.

Example: --class=user --class=computer

--description
Set the claim type description.

--enable
Enable claim type.

Cannot be used together with --disable.

--disable
Disable claim type.

Cannot be used together with --enable.

--protect
Protect claim type from accidental deletion.

Cannot be used together with --unprotect.

--unprotect
Unprotect claim type from accidental deletion.

Cannot be used together with --protect.

### domain claim claim-type delete

Delete claim types on the domain.

-H, --URL
LDB URL for database or target server.

--name
Display name of claim type to delete (required).

--force
Force claim type delete even if it is protected.

### domain claim value-type list

List claim value types on the domain.

-H, --URL
LDB URL for database or target server.

--json
View claim value types as JSON instead of a list.

### domain claim value-type view

View a single claim value type on the domain.

-H, --URL
LDB URL for database or target server.

--name
Display name of claim value type to view (required).

### domain classicupgrade \[options\] \<classic_smb_conf\>

Upgrade from Samba classic (NT4-like) database to Samba AD DC database.

### domain dcpromo \<dnsdomain\> \[DC\|RODC\] \[options\]

Promote an existing domain member or NT4 PDC to an AD DC.

### domain demote

Demote ourselves from the role of domain controller.

### domain exportkeytab \<keytab\> \[options\]

Dumps Kerberos keys of the domain into a keytab.

### domain functionalprep \[options\]

Prepare a domain for functional level upgrade. If `--functional-level` is not used, the latest supported version is used (currently 2016).

There are two aspects to this preparation, relating to the forest and the domain. By default both are run. If either of `--forest-prep` or `--domain-prep` are used, only the corresponding preparation is made. If both arguments are used together, all preparation is done, just as when neither is used.

-H, --URL
LDB URL for database or target server.

--functional-level \[2008_R2\|2012\|2012_R2\|2016\]
The functional level to prepare for. The default is 2016.

--forest-prep
Run forest preparation only (unless --domain-prep is also used).

--domain-prep
Run domain preparation only (unless --forest-prep is also used).

### domain info \ \[options\]

Print basic info about a domain and the specified DC.

### domain join \<dnsdomain\> \[DC\|RODC\|MEMBER\|SUBDOMAIN\] \[options\]

Join a domain as either member or backup domain controller.

### domain kds root-key

Manage Key Distribution Service root keys.

### domain kds root-key create \[options\]

Create KDS root keys

-H, --URL
LDB URL for database or target server.

--use-start-time=\["now"\|iso8601 or LDIF time string\]
The key will be valid from this time.

Valid time format are the string "now", the LDIF format `YYYYmmddHHMMSS.0Z`, or the ISO format `YYYY-mm-dd[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]` where the '\*' can be any character, and the optional last '\[+HH:MM\[:SS\[.ffffff\]\]\]' is a timezone offset (e.g. '+00:00' for UTC).

--json
Output results in JSON format.

### domain kds root-key delete --name={GUID}

Delete the named KDS root key. Use `samba-tool domain kds root-key list` to find the name of the key.

-H, --URL
LDB URL for database or target server.

--name=NAME
The name of the key to delete. It will be a GUID.

-v, --verbose
Print all attributes (except secret ones, unless --show secrets is used).

--json
Output results in JSON format.

### domain kds root-key list \[options\]

List KDS root keys. The newest keys are listed first.

-H, --URL
LDB URL for database or target server.

--show-secrets
Print secret or potentially sensitive attributes, namely msKds-RootKeyData and msKds-SecretAgreementParam.

-v, --verbose
Print more attributes (but not secret ones, unless --show secrets is also used).

--json
Output results in JSON format.

### domain kds root-key view \[options\]

View a KDS root key. The default output is similar to that of `samba-tool domain kds root-key list --verbose`, but with only one key show. The key can be selected by using `--latest` for the most recent key, or `--name` to select a key by name.

-H, --URL
LDB URL for database or target server.

--latest
View the most recent root key.

--name=NAME
The name of the key to view. It will be a GUID.

-v, --verbose
Print all attributes (except secret ones, unless --show secrets is used). This includes attributes that are only useful for LDB bookkeeping.

--json
Output results in JSON format.

### domain leave \[options\]

Run on a domain member, this will cause it to leave the domain.

To remove a domain server from the domain, you first need `samba-tool domain demote`.

--keep-account
Disable the machine account instead of deleting it.

### domain level \<show\|raise\> \<options\> \[options\]

Show/raise domain and forest function levels.

### domain passwordsettings set \<options\> \[options\]

Set password settings, including complexity requirements, lockout policy, history length, minimum password length, and minimum and maximum password age on a Samba AD DC server.

Use against a Windows DC is possible, but group policy will override it.

-H URL, --URL=URL
LDB URL for database or target server

-q, --quiet
Be quiet

--complexity=COMPLEXITY
The password complexity (on \| off \| default). Default is 'on'

--store-plaintext=STORE_PLAINTEXT
Store plaintext passwords where account have 'store passwords with reversible encryption' set (on \| off \| default). Default is 'off'

--history-length=HISTORY_LENGTH
The password history length (\ \| default). Default is 24.

--min-pwd-length=MIN_PWD_LENGTH
The minimum password length (\ \| default). Default is 7.

--min-pwd-age=MIN_PWD_AGE
The minimum password age (\<number of days\> \| default). Default is 1.

--max-pwd-age=MAX_PWD_AGE
The maximum password age (\<number of days\> \| default). Default is 43.

--account-lockout-duration=ACCOUNT_LOCKOUT_DURATION
The length of time an account is locked out after exceeding the limit on bad password attempts (\<number of minutes\> \| default). Default is 30 mins.

--account-lockout-threshold=ACCOUNT_LOCKOUT_THRESHOLD
The number of bad password attempts allowed before locking out the account (\ \| default). Default is 0 (never lock out).

--reset-account-lockout-after=RESET_ACCOUNT_LOCKOUT_AFTER
After this time is elapsed, the recorded number of attempts restarts from zero (\ \| default). Default is 30.

### domain passwordsettings show \<options\> \[options\]

Display current password settings for the domain.

-H URL, --URL=URL
LDB URL for database or target server

### domain passwordsettings pso

Manage fine-grained Password Settings Objects (PSOs).

### domain passwordsettings pso apply \ \<user-or-group-name\> \[options\]

Applies a PSO's password policy to a user or group.

### domain passwordsettings pso create \ \ \[options\]

Creates a new Password Settings Object (PSO).

### domain passwordsettings pso delete \ \[options\]

Deletes a Password Settings Object (PSO).

### domain passwordsettings pso list \[options\]

Lists all Password Settings Objects (PSOs).

### domain passwordsettings pso set \ \[options\]

Modifies a Password Settings Object (PSO).

### domain passwordsettings pso show \<user-name\> \[options\]

Displays a Password Settings Object (PSO).

### domain passwordsettings pso show-user \ \[options\]

Displays the Password Settings that apply to a user.

### domain passwordsettings pso unapply \ \<user-or-group-name\> \[options\]

Updates a PSO to no longer apply to a user or group.

### domain provision

Promote an existing domain member or NT4 PDC to an AD DC.

### domain schemaupgrade \[options\]

Upgrade the schema.

-H, --URL
LDB URL for database or target server.

--schema \[2012\|2012_R2\|2016\|2019\]
Upgrade to this Windows schema level. The default is 2019.

--ldf-file
Apply the schema changes in this LDIF file, rather than updating to a standard schema level.

--base-dir
Specify an alternate location to find schema LDIF files.

### domain tombstones expunge NC \[NC \[...\]\] \[options\]

-H URL, --URL=URL
LDB URL for database or target server

--current-time=YYYY-MM-DD
The current time to evaluate the tombstone lifetime from, expressed as YYYY-MM-DD

--tombstone-lifetime=DAYS
Number of days a tombstone should be preserved for

### domain trust

Domain and forest trust management.

### domain trust create \<DOMAIN\> \<options\> \[options\]

Create a domain or forest trust.

### domain trust modify \<DOMAIN\> \<options\> \[options\]

Modify a domain or forest trust.

### domain trust delete \<DOMAIN\> \<options\> \[options\]

Delete a domain trust.

### domain trust list \<options\> \[options\]

List domain trusts.

### domain trust namespaces \[\<DOMAIN\>\] \<options\> \[options\]

Manage forest trust namespaces.

### domain trust show \<DOMAIN\> \<options\> \[options\]

Show trusted domain details.

### domain trust validate \<DOMAIN\> \<options\> \[options\]

Validate a domain trust.

## drs

Manage Directory Replication Services (DRS).

### drs bind

Show DRS capabilities of a server.

### drs clone-dc-database \<dnsdomain\> --targetdir=\<DIR\> \[options\]

Replicate an initial clone of domain, but DO NOT JOIN it.

--server=DC
Clone this DC.

--targetdir=TARGETDIR
where to store provision (required).

-q, --quiet
Be quiet.

--include-secrets
Also replicate secret values.

--backend-store=BACKENDSTORE
Specify the database backend to be used (default is tdb).

--backend-store-size=SIZE
Specify the size of the backend database, currentlyonly supported by lmdb backends (default is 8 GB).

### drs uptodateness \[options\]

Show uptodateness status.

-H URL, --URL=URL
LDB URL for database or target server

-p PARTITION, --partition=PARTITION
restrict to this partition

--json
Print data in json format

--maximum
Print maximum out-of-date-ness only

--median
Print median out-of-date-ness only

--full
Print full out-of-date-ness data

### drs kcc

Trigger knowledge consistency center run.

### drs options

Query or change \<options\> for NTDS Settings object of a domain controller.

### drs replicate \<destination_DC\> \<source_DC\> \<NC\> \[options\]

Replicate a naming context between two DCs.

### drs showrepl

Show replication status. The --json option results in JSON output, and with the --summary option produces very little output when the replication status seems healthy.

## dsacl

Administer DS ACLs

### dsacl delete

Delete an access list entry on a directory object.

### dsacl get

Print access list on a directory object.

### dsacl set

Modify access list on a directory object.

## forest

Manage Forest configuration.

### forest directory_service

Manage directory_service behaviour for the forest.

### forest directory_service dsheuristics \<VALUE\>

Modify dsheuristics directory_service configuration for the forest.

### forest directory_service show

Show current directory_service configuration for the forest.

## fsmo

Manage Flexible Single Master Operations (FSMO).

### fsmo seize \[options\]

Seize the role.

### fsmo show

Show the roles.

### fsmo transfer \[options\]

Transfer the role.

## gpo

Manage Group Policy Objects (GPO).

### gpo aclcheck \[options\]

Create an empty GPO.

Check all GPOs have matching LDAP and DS ACLs.

-H URL, --URL=URL
LDB URL for database or target server

### gpo admxload \[options\]

Loads samba admx files to sysvol

-H URL, --URL=URL
LDB URL for database or target server

--admx-dir=ADMX_DIR
Directory where admx templates are stored

### gpo backup \<gpo\>\[options\]

Backup a GPO.

-H H
LDB URL for database or target server

--tmpdir=TMPDIR
Temporary directory for copying policy files

--generalize
Generalize XML entities to restore

--entities=ENT_FILE
File to export defining XML entities for the restore

### gpo create \<displayname\> \[options\]

Create an empty GPO.

### gpo cse list

List the registered Client Side Extensions (CSEs) on the current host.

### gpo cse register \<cse_file\> \<cse_name\> \[options\]

Register a Client Side Extension (CSE) on the current host.

This command takes a CSE filename as an argument, and registers it for applying policy on the current host. This is not necessary for CSEs which are distributed with the current version of Samba, but is useful for installing experimental CSEs or custom built CSEs.

The \<cse_file\> argument MUST be a permanent location for the CSE. The register command does not copy the file to some other directory. The samba-gpupdate command will execute the CSE from the exact location specified from this command.

--machine
Whether to register the CSE as Machine policy

--user
Whether to register the CSE as User policy

### gpo cse unregister \<GUID\>

Unregister a Client Side Extension (CSE) from the current host.

This command takes a unique GUID as an argument (representing a registered CSE), and unregisters it for applying policy on the current host. Use the \`samba-tool gpo cse list\` command to determine the unique GUIDs of CSEs.

### gpo del \<gpo\> \[options\]

Delete GPO.

### gpo dellink \<container_dn\> \<gpo\> \[options\]

Delete GPO link from a container.

### gpo fetch \<gpo\> \[options\]

Download a GPO.

### gpo getinheritance \<container_dn\> \[options\]

Get inheritance flag for a container.

### gpo getlink \<container_dn\> \[options\]

List GPO Links for a container.

### gpo list \<username\> \[options\]

List GPOs for an account.

### gpo listall

List all GPOs.

### gpo listcontainers \<gpo\> \[options\]

List all linked containers for a GPO.

### gpo load \<gpo\> \[options\]

Load policies onto a GPO.

Reads json from standard input until EOF, unless a json formatted file is provided via --content.

Example json_input:

    [
        {
            "keyname": "Software\Policies\Mozilla\Firefox\Homepage",
            "valuename": "StartPage",
            "class": "USER",
            "type": "REG_SZ",
            "data": "homepage"
        },
        {
            "keyname": "Software\Policies\Mozilla\Firefox\Homepage",
            "valuename": "URL",
            "class": "USER",
            "type": "REG_SZ",
            "data": "google.com"
        },
        {
            "keyname": "Software\Microsoft\Internet Explorer\Toolbar",
            "valuename": "IEToolbar",
            "class": "USER",
            "type": "REG_BINARY",
            "data": [0]
        },
        {
            "keyname": "Software\Policies\Microsoft\InputPersonalization",
            "valuename": "RestrictImplicitTextCollection",
            "class": "USER",
            "type": "REG_DWORD",
            "data": 1
        }
        ]


Valid class attributes: MACHINE\|USER\|BOTH Data arrays are interpreted as bytes.

The --machine-ext-name and --user-ext-name options are multi-value inputs which respectively set the gPCMachineExtensionNames and gPCUserExtensionNames ldap attributes on the GPO. These attributes must be set to the correct GUID names for Windows Group Policy to work correctly. These GUIDs represent the client side extensions to apply on the machine. Linux Group Policy does not enforce this constraint. {35378EAC-683F-11D2-A89A-00C04FBBCFA2} is provided by default, which enables most Registry policies.

-H H
LDB URL for database or target server

--content=CONTENT
JSON file of policy inputs

--machine-ext-name=MACHINE_EXTS
A machine extension name to add to gPCMachineExtensionNames

--user-ext-name=USER_EXTS
A user extension name to add to gPCUserExtensionNames

--replace
Replace the existing Group Policies, rather than merging

### gpo manage security list \<gpo\> \[options\]

List Samba Security Group Policy from the sysvol.

This command lists security settings from the sysvol that will be applied to winbind clients. These settings only apply to the AD DC.

Example:

    samba-tool gpo manage security list {31B2F340-016D-11D2-945F-00C04FB984F9}

-H URL, --URL=URL
LDB URL for database or target server

### gpo manage security set \<gpo\> \[options\]

Set Samba Security Group Policy to the sysvol.

This command sets a security setting to the sysvol for applying to winbind clients. Not providing a value will unset the policy. These settings only apply to the AD DC.

Example:

    samba-tool gpo manage security set {31B2F340-016D-11D2-945F-00C04FB984F9} MaxTicketAge 10

Possible policies:

MaxTicketAge
Maximum lifetime for user ticket (hours).

MaxServiceAge
Maximum lifetime for service ticket in minutes. Defined in minutes

MaxRenewAge
Maximum lifetime for user ticket renewal, in minutes.

MinimumPasswordAge
Minimum password age, in days.

MaximumPasswordAge
Maximum password age, in days.

MinimumPasswordLength
Minimum password length, in characters.

PasswordComplexity
Password must meet complexity requirements. 1 is Enabled, 0 is Disabled.


-H URL, --URL=URL
LDB URL for database or target server

List Samba Security Group Policy from the sysvol.

This command lists security settings from the sysvol that will be applied to winbind clients. These settings only apply to the AD DC.

Example:

    samba-tool gpo manage security list {31B2F340-016D-11D2-945F-00C04FB984F9}

-H URL, --URL=URL
LDB URL for database or target server

### gpo manage smb_conf list

List smb.conf settings from the sysvol that will be applied to winbind clients.

Example:

    samba-tool gpo manage smb_conf list {31B2F340-016D-11D2-945F-00C04FB984F9}

-H URL, --URL=URL
LDB URL for database or target server

### gpo manage smb_conf set \<gpo\> \<\[value\]\> \[options\]

Set or unset an smb.conf setting to the sysvol for applying to winbind clients.

If a value is provided, that is the smb.conf value used; if no value is provided, the policy is removed.

Example:

    samba-tool gpo manage smb_conf set {31B2F340-016D-11D2-945F-00C04FB984F9} 'apply gpo policies' yes

-H URL, --URL=URL
LDB URL for database or target server

### gpo setinheritance \<container_dn\> \ \[options\]

Set inheritance flag on a container.

### gpo setlink \<container_dn\> \<gpo\> \[options\]

Add or Update a GPO link to a container.

### gpo remove\<gpo\> \[options\]

Show information for a GPO.

Remove policies from a GPO.

Reads json from standard input until EOF, unless a json formatted file is provided via --content.

    Example json_input:
    [
        {
            "keyname": "Software\Policies\Mozilla\Firefox\Homepage",
            "valuename": "StartPage",
            "class": "USER",
        },
        {
            "keyname": "Software\Policies\Mozilla\Firefox\Homepage",
            "valuename": "URL",
            "class": "USER",
        },
        {
            "keyname": "Software\Microsoft\Internet Explorer\Toolbar",
            "valuename": "IEToolbar",
            "class": "USER"
        },
        {
            "keyname": "Software\Policies\Microsoft\InputPersonalization",
            "valuename": "RestrictImplicitTextCollection",
            "class": "USER"
        }
    ]

Valid class attributes: MACHINE\|USER\|BOTH

-H H
LDB URL for database or target server

--content=CONTENT
JSON file of policy inputs

--machine-ext-name=MACHINE_EXTS
A machine extension name to remove from gPCMachineExtensionNames

--user-ext-name=USER_EXTS
A user extension name to remove from gPCUserExtensionNames

--color=always\|never\|auto
use colour if available (default: auto)

### gpo restore \<displayname\> \ \[options\]

Restore a GPO to a new container.

-H H
LDB URL for database or target server

--tmpdir=TMPDIR
Temporary directory for copying policy files

--entities=ENTITIES
File defining XML entities to insert into DOCTYPE header

--restore-metadata
Keep the old GPT.INI file and associated version number

### gpo show \<gpo\> \[options\]

Show information for a GPO.

### gpo manage symlink list

List VGP Symbolic Link Group Policy from the sysvol

### gpo manage symlink add

Adds a VGP Symbolic Link Group Policy to the sysvol

### gpo manage symlink remove

Removes a VGP Symbolic Link Group Policy from the sysvol

### gpo manage files list

List VGP Files Group Policy from the sysvol

### gpo manage files add

Add VGP Files Group Policy to the sysvol

### gpo manage files remove

Remove VGP Files Group Policy from the sysvol

### gpo manage openssh list

List VGP OpenSSH Group Policy from the sysvol

### gpo manage openssh set

Sets a VGP OpenSSH Group Policy to the sysvol

### gpo manage sudoers add

Adds a Samba Sudoers Group Policy to the sysvol.

### gpo manage sudoers list

List Samba Sudoers Group Policy from the sysvol.

### gpo manage sudoers remove

Removes a Samba Sudoers Group Policy from the sysvol.

### gpo manage scripts startup list

List VGP Startup Script Group Policy from the sysvol

### gpo manage scripts startup add

Adds VGP Startup Script Group Policy to the sysvol

### gpo manage scripts startup remove

Removes VGP Startup Script Group Policy from the sysvol

### gpo manage motd list

List VGP MOTD Group Policy from the sysvol.

### gpo manage motd set

Sets a VGP MOTD Group Policy to the sysvol

### gpo manage issue list

List VGP Issue Group Policy from the sysvol.

### gpo manage issue set

Sets a VGP Issue Group Policy to the sysvol

### gpo manage access add

Adds a VGP Host Access Group Policy to the sysvol

### gpo manage access list

List VGP Host Access Group Policy from the sysvol

### gpo manage access remove

Remove a VGP Host Access Group Policy from the sysvol

## group

Manage groups.

### group add \<groupname\> \[options\]

Create a new AD group.

### group create \<groupname\> \[options\]

Add a new AD group. This is a synonym for the `samba-tool group add` command and is available for compatibility reasons only. Please use `samba-tool group add` instead.

### group addmembers \<groupname\> \<members\> \[options\]

Add members to an AD group.

### group addunixattrs \<groupname\> \<gidnumber\> \[options\]

Add RFC2307 Unix attributes to a group account in the Active Directory domain. The groupname specified on the command is the sAMaccountName.

Unix (RFC2307) attributes will be added to the group account.

Add 'idmap_ldb:use rfc2307 = Yes' to smb.conf to use these attributes for UID/GID mapping.

The command may be run from the root userid or another authorized userid. The -H or --URL= option can be used to execute the command against a remote server.

Example1:

    samba-tool group addunixattrs Group1 10000

Example1 shows how to add RFC2307 attributes to a domain enabled group account.

The groups Unix ID will be set to '10000', provided this ID isn't already in use.

-H URL, --URL=URL
LDB URL for database or target server

### group delete \<groupname\> \[options\]

Delete an AD group.

### group edit \<groupname\>

Edit a group AD object.

--editor=EDITOR
Specifies the editor to use instead of the system default, or 'vi' if no system default is set.

### group list

List all groups.

### group listmembers \<groupname\> \[options\]

List all members of the specified AD group.

By default the sAMAccountNames are listed. If no sAMAccountName is available, the CN will be used instead.

--full-dn
List the distinguished names instead of the sAMAccountNames.

--hide-expired
Do not list expired group members.

--hide-disabled
Do not list disabled group members.

### group move \<groupname\> \<new_parent_dn\> \[options\]

This command moves a group into the specified organizational unit or container.

The groupname specified on the command is the sAMAccountName.

The name of the organizational unit or container can be specified as a full DN or without the domainDN component.

### group removemembers \<groupname\> \<members\> \[options\]

Remove members from the specified AD group.

### group show \<groupname\> \[options\]

Show group object and it's attributes.

### group stats \[options\]

Show statistics for overall groups and group memberships.

### group rename \<groupname\> \[options\]

Rename a group and related attributes.

This command allows to set the group's name related attributes. The group's CN will be renamed automatically. The group's CN will be the sAMAccountName. Use the --force-new-cn option to specify the new CN manually and the --reset-cn to reset this change.

Use an empty attribute value to remove the specified attribute.

The groupname specified on the command is the sAMAccountName.

--force-new-cn=NEW_CN
Specify a new CN (RDN) instead of using the sAMAccountName.

--reset-cn
Set the CN to the sAMAccountName.

--mail-address=MAIL_ADDRESS
New mail address

--samaccountname=SAMACCOUNTNAME
New account name (sAMAccountName/logon name)

## ldapcmp \<URL1\> \<URL2\> \<domain\|configuration\|schema\|dnsdomain\|dnsforest\> \[options\]

Compare two LDAP databases.

## ntacl

Manage NT ACLs.

### ntacl changedomsid \<original-domain-SID\> \<new-domain-SID\> \<file\> \[options\]

Change the domain SID for ACLs. Can be used to change all entries in acl_xattr when the machine's SID has accidentally changed or the data set has been copied to another machine either via backup/restore or rsync.

--use-ntvfs
Set the ACLs directly to the TDB or xattr. The POSIX permissions will NOT be changed, only the NT ACL will be stored.

--service=SERVICE
Specify the name of the smb.conf service to use. This option is required in combination with the --use-s3fs option.

--use-s3fs
Set the ACLs for use with the default s3fs file server via the VFS layer. This option requires a smb.conf service, specified by the --service=SERVICE option.

--xattr-backend=\[native\|tdb\]
Specify the xattr backend type (native fs or tdb).

--eadb-file=EADB_FILE
Name of the tdb file where attributes are stored.

--recursive
Set the ACLs for directories and their contents recursively.

--follow-symlinks
Follow symlinks when --recursive is specified.

--verbose
Verbosely list files and ACLs which are being processed.

### ntacl getdosinfo \<file\> \[options\]

Get DOS info of a file from xattr.

### ntacl get \<file\> \[options\]

Get ACLs on a file.

### ntacl set \<acl\> \<file\> \[options\]

Set ACLs on a file.

### ntacl sysvolcheck

Check sysvol ACLs match defaults (including correct ACLs on GPOs).

### ntacl sysvolreset

Reset sysvol ACLs to defaults (including correct ACLs on GPOs).

## ou

Manage organizational units (OUs).

### ou add \<ou_dn\> \[options\]

Add a new organizational unit.

The name of the organizational unit can be specified as a full DN or without the domainDN component.

--description=DESCRIPTION
Specify OU's description.

### ou create \<ou_dn\> \[options\]

Add a new organizational unit. This is a synonym for the `samba-tool ou add` command and is available for compatibility reasons only. Please use `samba-tool ou add` instead.

### ou delete \<ou_dn\> \[options\]

Delete an organizational unit.

The name of the organizational unit can be specified as a full DN or without the domainDN component.

--force-subtree-delete
Delete organizational unit and all children recursively.

### ou list \[options\]

List all organizational units.

--full-dn
Display DNs including the base DN.

### ou listobjects \<ou_dn\> \[options\]

List all objects in an organizational unit.

The name of the organizational unit can be specified as a full DN or without the domainDN component.

--full-dn
Display DNs including the base DN.

-r\|--recursive
List objects recursively.

### ou move \<old_ou_dn\> \<new_parent_dn\> \[options\]

Move an organizational unit.

The name of the organizational units can be specified as a full DN or without the domainDN component.

### ou rename \<old_ou_dn\> \<new_ou_dn\> \[options\]

Rename an organizational unit.

The name of the organizational units can be specified as a full DN or without the domainDN component.

## processes

List samba server processes.

If no processes are show, but Samba is running, it is possible that samba-tool has not found the correct smb.conf, and the use of -s/--configfile is required.

--name=NAME
Show processes associated with the given name.

--pid=PID
Show names associated with the PID.

## rodc

Manage Read-Only Domain Controller (RODC).

### rodc preload \<SID\>\|\<DN\>\|\<accountname\> \[options\]

Preload one account for an RODC.

## schema

Manage and query schema.

### schema attribute modify \<attribute\> \[options\]

Modify the behaviour of an attribute in schema.

### schema attribute show \<attribute\> \[options\]

Display an attribute schema definition.

### schema attribute show_oc \<attribute\> \[options\]

Show objectclasses that MAY or MUST contain this attribute.

### schema objectclass show \<objectclass\> \[options\]

Display an objectclass schema definition.

## service-account

Service account management.

### service-account list

List service accounts on the domain.

-H, --URL
LDB URL for database or target server.

--json
View service accounts as JSON instead of a list.

### service-account view

View a single service account on the domain.

-H, --URL
LDB URL for database or target server.

--name
Account name of service account to view (required).

### service-account create

Create a new service account on the domain.

-H, --URL
LDB URL for database or target server.

--name
Account name of service account (required).

--dns-host-name
DNS hostname of this service account (required).

--group-msa-membership
Optional Group MSA Membership SDDL.

--managed-password-interval
Managed password refresh interval in days.

### service-account modify

Modify an existing service account on the domain.

-H, --URL
LDB URL for database or target server.

--name
Account name of service account (required).

--dns-host-name
Update DNS hostname of this service account.

--group-msa-membership
Update Group MSA Membership SDDL.

### service-account delete

Delete a service accounts on the domain.

-H, --URL
LDB URL for database or target server.

--name
Account name of service account to delete.

## service-account group-msa-membership

Service account Group MSA Membership management.

### service-account group-msa-membership show

Display Group MSA Membership for a service account.

-H, --URL
LDB URL for database or target server.

--name
Account name of service account (required).

--json
Return as JSON instead of a list.

### service-account group-msa-membership add

Add a principal to Group MSA Membership for a service account.

-H, --URL
LDB URL for database or target server.

--name
Account name of service account (required).

--principal
Name, DN or SID of principal to add.

### service-account group-msa-membership remove

Remove a principal from Group MSA Membership for a service account.

-H, --URL
LDB URL for database or target server.

--name
Account name of service account (required).

--principal
Name, DN or SID of principal to remove.

## shell

Opens an interactive Samba Python shell.

### shell \[options\]

Opens an interactive Python shell for Samba ldb connection.

-H, --URL
LDB URL for database or target server.

## sites

Manage sites.

### sites list \[options\]

List sites.

--json
Output as JSON instead of a list

### sites view \<site\> \[options\]

View site details.

### sites create \<site\> \[options\]

Create a new site.

### sites remove \<site\> \[options\]

Delete an existing site.

### sites subnet list \<site\> \[options\]

List subnets for a site.

--json
Output as JSON instead of a list

### sites subnet view \<subnet\> \[options\]

View subnet details.

### sites subnet create \<subnet\> \<site-of-subnet\> \[options\]

Create a new subnet.

### sites subnet remove \<subnet\> \[options\]

Delete an existing subnet.

### sites subnet set-site \<subnet\> \<site-of-subnet\> \[options\]

Assign a subnet to a site.

## spn

Manage Service Principal Names (SPN).

### spn add \<name\> \<user\> \[options\]

Create a new SPN.

### spn delete \<name\> \[\<user\>\] \[options\]

Delete an existing SPN.

### spn list \<user\> \[options\]

List SPNs of a given user.

## testparm

Check the syntax of the configuration file.

## time

Retrieve the time on a server.

## user

Manage users.

### user add \<username\> \[\\]

Add a new user to the Active Directory Domain.

### user addunixattrs \<username\> \<uid-number\> \[options\]

Add RFC2307 attributes to a user.

This command adds Unix attributes to a user account in the Active Directory domain.

The username specified on the command is the sAMaccountName.

You must supply a unique uid.

Unix (RFC2307) attributes will be added to the user account.

If you supply a group id with '--gid-number', this will be used for the users Unix 'gidNumber' attribute.

If '--gid-number' is not supplied, the users Unix gidNumber will be set to the one found in 'Domain Users', this means Domain Users must have a gidNumber attribute.

If '--unix-home' is not supplied, the users Unix home directory will be set to /home/DOMAIN/username.

If '--login-shell' is not supplied, the users Unix login shell will be set to '/bin/sh'

If ---gecos' is not supplied, the users Unix gecos field will be set to the user's 'CN' attribute.

Add 'idmap_ldb:use rfc2307 = Yes' to the smb.conf on DCs to use these attributes for UID/GID mapping.

The command may be run from the root userid or another authorised userid. The -H or --URL= option can be used to execute the command against a remote server.

Example1:

    samba-tool user addunixattrs User1 10001

Example1 shows how to add RFC2307 attributes to a domain enabled user account, Domain Users will be set as the users gidNumber.

The users Unix ID will be set to '10001', provided this ID isn't already in use.

Example2:

    samba-tool user addunixattrs User2 10002 --gid-number=10001 --unix-home=/home/User2

Example2 shows how to add RFC2307 attributes to a domain enabled user account.

The users Unix ID will be set to '10002', provided this ID isn't already in use.

The users gidNumber attribute will be set to '10001'

The users Unix home directory will be set to '/home/user2'

Example3:

    samba-tool user addunixattrs User3 10003 --gid-number=10001 --login-shell=/bin/false --gecos='User3 test'

Example3 shows how to add RFC2307 attributes to a domain enabled user account.

The users Unix ID will be set to '10003', provided this ID isn't already in use. The users gidNumber attribute will be set to '10001'. The users Unix login shell will be set to '/bin/false'. The users gecos field will be set to 'User3 test'.

-H URL, --URL=URL
LDB URL for database or target server

--gid-number=GROUP_ID
User's Unix/RFC2307 GID

--unix-home=DIR
User's Unix/RFC2307 home directory

--login-shell=SHELL
User's Unix/RFC2307 login shell

--gecos=GECOS
User's Unix/RFC2307 GECOS field

--uid=USER_ID
User's Unix/RFC2307 user id

### user create \<username\> \[\\]

Add a new user. This is a synonym for the `samba-tool user add` command and is available for compatibility reasons only. Please use `samba-tool user add` instead.

### user delete \<username\> \[options\]

Delete an existing user account.

### user disable \<username\>

Disable a user account.

--remove-supplemental-groups
Remove user from all groups, but keep the primary group.

### user edit \<username\>

Edit a user account AD object.

--editor=EDITOR
Specifies the editor to use instead of the system default, or 'vi' if no system default is set.

### user enable \<username\>

Enable a user account.

### user list

List all users.

By default the user's sAMAccountNames are listed.

--full-dn
List user's distinguished names instead of the sAMAccountNames.

-b BASE_DN\|--base-dn=BASE_DN
Specify base DN to use. Only users under the specified base DN will be listed.

--hide-expired
Do not list expired user accounts.

--hide-disabled
Do not list disabled user accounts.

--locked-only
Only list locked user accounts.

### user setprimarygroup \<username\> \

Set the primary group a user account.

### user getgroups \<username\>

Get the direct group memberships of a user account.

### user show \<username\> \[options\]

Display a user AD object.

--attributes=USER_ATTRS
Comma separated list of attributes, which will be printed.

### user move \<username\> \<new_parent_dn\> \[options\]

This command moves a user account into the specified organizational unit or container.

The username specified on the command is the sAMAccountName.

The name of the organizational unit or container can be specified as a full DN or without the domainDN component.

### user password \[options\]

Change password for a user account (the one provided in authentication).

### user rename \<username\> \[options\]

Rename a user and related attributes.

This command allows to set the user's name related attributes. The user's CN will be renamed automatically. The user's new CN will be made up by combining the given-name, initials and surname. A dot ('.') will be appended to the initials automatically, if required. Use the --force-new-cn option to specify the new CN manually and --reset-cn to reset this change.

Use an empty attribute value to remove the specified attribute.

The username specified on the command is the sAMAccountName.

--surname=SURNAME
New surname

--given-name=GIVEN_NAME
New given name

--initials=INITIALS
New initials

--force-new-cn=NEW_CN
Specify a new CN (RDN) instead of using a combination of the given name, initials and surname.

--reset-cn
Set the CN to the default combination of given name, initials and surname.

--display-name=DISPLAY_NAME
New display name

--mail-address=MAIL_ADDRESS
New email address

--samaccountname=SAMACCOUNTNAME
New account name (sAMAccountName/logon name)

--upn=UPN
New user principal name

### user sensitive \<accountname\> \[show\|on\|off\] \[options\]

Set/unset or show UF_NOT_DELEGATED for an account.

-H URL, --URL=URL
LDB URL for database or target server

### user setexpiry \<username\> \[options\]

Set the expiration of a user account.

### user setpassword \<username\> \[options\]

Sets or resets the password of a user account.

### user unlock \<username\> \[options\]

This command unlocks a user account in the Active Directory domain.

### user getpassword \<username\> \[options\]

Gets the password of a user account.

### user get-kerberos-ticket \<username\> \[options\]

Gets a Kerberos Ticket Granting Ticket as the account.

### user syncpasswords \<--cache-ldb-initialize\> \[options\]

Syncs the passwords of all user accounts, using an optional script.

Note that this command should run on a single domain controller only (typically the PDC-emulator).

### user auth policy assign \<username\> \[options\]

Set assigned authentication policy for user.

--policy
Name of authentication policy to assign or leave empty to remove.

### user auth policy remove \<username\>

Remove assigned authentication policy from user.

### user auth policy view \<username\>

View the assigned authentication policy for user.

### user auth silo assign \<username\> \[options\]

Set assigned authentication silo for user.

--silo
Name of authentication silo to assign or leave empty to remove.

### user auth silo remove \<username\>

Remove assigned authentication silo from user.

### user auth silo view \<username\>

View the assigned authentication silo for user.

## user keytrust

Manage Key Credential Links for a user.

This can populate, describe or delete msDS-KeyCredentialLink attributes.

### user keytrust add \<username\> \\[options\]

Add a key-credential-link, which is a linked attribute that holds a public key in a binary field.

The second argument is a filename that should refer to a 2048 bit RSA key (or a certificate containing that key) in PEM or DER format. By default the encoding format will be detected automatically, but you can attempt to override this with `--encoding` option. Other types of public key are not supported, though the `--force` option can be used to add a non-2048 bit key.

--link-target=DN
link to this DN (default: the user's DN)

--encoding=ENCODING
Key format, either `pem`, `der`, or `auto`. The default is `auto`, which is likely to detect the correct format in all circumstances.

--force
proceed with operations that seems ill-fated

### user keytrust delete \<username\> \[options\]

Delete a key-credential-link.

The link to be deleted can be selected in a number of ways. `--all` will delete all key credential links for the user (often there will only be one). The `--link-target` option selects a key credential link based on the DN targeted by the link. The `--fingerprint` option selects a link to delete based on the key fingerprint. This is the SHA256 of the DER-encoded key material, expressed as hex-pairs separated by colons. See `user keytrust view` to get a list of links and their fingerprints.

If more than one of `--link-target`, `--fingerprint`, and `--all` are used, links matched by any of them will be deleted.

The `--dry-run` option will prevent links from being deleted, and instead indicate what would happen if it was omitted.

--link-target=DN
Delete this key credential link (a DN)

--fingerprint=HH:HH:..
Delete the key credential link with this key fingerprint

--all
Delete all key credential links

-n, --dry-run
Do nothing but print what would happen

### user keytrust view \<username\> \[options\]

View a user's key credential links. This can be used to find a link's fingerprint and target DN for

. The `--verbose` includes more, probably useless, information.

-h, --help
show this help message and exit

-v, --verbose
Be verbose

### user generate-csr \<username\> \<subject_name\> \ \<output_filename\> \[options\]

Generate a PEM‐encoded Certificate Signing Request for a user.

--private-key-encoding
Specify which encoding the private key uses. Default is 'auto'.

--private-key-pass
Provide a password to decrypt the private key.

## vampire \[options\] \<domain\>

Join and synchronise a remote AD domain to the local server. Please note that `samba-tool vampire` is deprecated, please use `samba-tool domain join` instead.

## visualize \[options\] \<subcommand\>

Produce graphical representations of Samba network state. To work out what is happening in a replication graph, it is sometimes helpful to use visualisations.

There are two subcommands, two graphical modes, and (roughly) two modes of operation with respect to the location of authority.

### MODES OF OPERATION

samba-tool visualize ntdsconn

Looks at NTDS connections.

samba-tool visualize reps

Looks at repsTo and repsFrom objects.

samba-tool visualize uptodateness

Looks at replication lag as shown by the uptodateness vectors.

### GRAPHICAL MODES

--distance

Distances between DCs are shown in a matrix in the terminal.

--dot

Generate Graphviz dot output (for ntdsconn and reps modes). When viewed using dot or xdot, this shows the network as a graph with DCs as vertices and connections edges. Certain types of degenerate edges are shown in different colours or line-styles.

--xdot

Generate Graphviz dot output as with --dot and attempt to view it immediately using `/usr/bin/xdot`.

-r

Normally, `samba-tool` talks to one database; with the -r option attempts are made to contact all the DCs known to the first database. This is necessary for `samba-tool visualize uptodateness` and for `samba-tool visualize reps` because the repsFrom/To objects are not replicated, and it can reveal replication issues in other modes.

## help

Gives usage information.

# VERSION

This man page is complete for version of the Samba suite.

# AUTHOR

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
