# smb.conf Parameters / domain

### `allow dns updates`

Section: domain; Context: G; Type: enum; Default: `secure only`

This option determines what kind of updates to the DNS are allowed. DNS updates can either be disallowed completely by setting it to disabled , enabled over secure connections only by setting it to secure only or allowed in all cases by setting it to nonsecure .

### `dns forwarder`

Section: domain; Context: G; Type: cmdlist

This option specifies the list of DNS servers that DNS requests will be forwarded to if they can not be handled by Samba itself. The DNS forwarder is only used if the internal DNS server in Samba is used. Port numbers can be appended by separating them from the address by using a colon (':'). When specifying a port, IPv6 addresses must be enclosed in square brackets ('[' and ']'). IPv6 forwarder addresses with no port specified, don't need the square brackets, and default to port 53.

### `dns update command`

Section: domain; Context: G; Type: cmdlist; Default: `/samba_dnsupdate`

This option sets the command that is called when there are DNS updates. It should update the local machines DNS names using TSIG-GSS.

### `dns zone scavenging`

Section: domain; Context: G; Type: boolean; Default: `no`

When enabled (the default is disabled) unused dynamic dns records are periodically removed. This option should not be enabled for installations created with versions of samba before 4.9. Doing this will result in the loss of static DNS entries. This is due to a bug in previous versions of samba (BUG 12451) which marked dynamic DNS records as static and static records as dynamic. If one record for a DNS name is static (non-aging) then no other record for that DNS name will be scavenged.

### `dns zone transfer clients allow`

Section: domain; Context: G; Type: cmdlist

This option specifies the list of IPs authorized to ask for dns zone transfer from bind DLZ module. The IP list is comma and space separated and specified in the same syntax as used in , specifically including IP address, IP prefixes and IP address masks. As this is a DNS server option, hostnames are naturally not permitted. The default behaviour is to deny any request. A request will be authorized only if the emitting client is identified in this list, and not in

### `dns zone transfer clients deny`

Section: domain; Context: G; Type: cmdlist

This option specifies the list of IPs denied to ask for dns zone transfer from bind DLZ module. The IP list is comma and space separated and specified in the same syntax as used in , specifically including IP address, IP prefixes and IP address masks. As this is a DNS server option, hostnames are naturally not permitted. If a client identified in this list sends a zone transfer request, it will always be denied, even if they are in . This allows the definition of specific denied clients within an authorized subnet.

### `gpo update command`

Section: domain; Context: G; Type: list; Default: `/samba-gpupdate`

This option sets the command that is called to apply GPO policies. The samba-gpupdate script applies System Access and Kerberos Policies to the KDC. System Access policies set minPwdAge, maxPwdAge, minPwdLength, and pwdProperties in the samdb. Kerberos Policies set kdc:service ticket lifetime, kdc:user ticket lifetime, and kdc:renewal lifetime in smb.conf.

### `machine password timeout`

Section: domain; Context: G; Type: integer; Default: `604800`

If a Samba server is a member of a Windows NT or Active Directory Domain (see the domain and ads parameters), then periodically a running winbindd process will try and change the MACHINE ACCOUNT PASSWORD stored in the TDB called secrets.tdb . This parameter specifies how often this password will be changed, in seconds. The default is one week (expressed in seconds), the same as a Windows NT Domain member server. See also smbpasswd 8 , and the domain and ads parameters.

### `nsupdate command`

Section: domain; Context: G; Type: cmdlist; Default: `/usr/bin/nsupdate -g`

This option sets the path to the nsupdate command which is used for GSS-TSIG dynamic DNS updates.

### `spn update command`

Section: domain; Context: G; Type: cmdlist; Default: `/samba_spnupdate`

This option sets the command that for updating servicePrincipalName names from spn_update_list .
