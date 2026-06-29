# smb.conf Parameters / base

### `additional dns hostnames`

Section: base; Context: G; Type: cmdlist; Default: `empty string (no additional dns names)`

A list of additional DNS names by which this host can be identified

### `bind interfaces only`

Section: base; Context: G; Type: boolean; Default: `no`

This global parameter allows the Samba admin to limit what interfaces on a machine will serve SMB requests. It affects file service smbd 8 and name service nmbd 8 in a slightly different ways. For name service it causes nmbd to bind to ports 137 and 138 on the interfaces listed in the parameter. nmbd also binds to the "all addresses" interface (0.0.0.0) on ports 137 and 138 for the purposes of reading broadcast messages. If this option is not set then nmbd will service name requests on all of these sockets. If is set then nmbd will check the source address of any packets coming in on the broadcast sockets and discard any that don't match the broadcast addresses of the interfaces in the parameter list. As unicast packets are received on the other sockets it allows nmbd to refuse to serve names to machines that send packets that arrive through any interfaces not listed in the list. IP Source address spoofing does defeat this simple check, however, so it must not be used seriously as a security feature for nmbd . For file service it causes smbd 8 to bind only to the interface list given in the parameter. This restricts the networks that smbd will serve, to packets coming in on those interfaces. Note that you should not use this parameter for machines that are serving PPP or other intermittent or non-broadcast network interfaces as it will not cope with non-permanent interfaces. If is set and the network address 127.0.0.1 is not added to the parameter list smbpasswd 8 may not work as expected due to the reasons covered below. To change a users SMB password, the smbpasswd by default connects to the localhost - 127.0.0.1 address as an SMB client to issue the password change request. If is set then unless the network address 127.0.0.1 is added to the parameter list then smbpasswd will fail to connect in it's default mode. smbpasswd can be forced to use the primary IP interface of the local host by using its smbpasswd 8 -r remote machine parameter, with remote machine set to the IP name of the primary interface of the local host.

### `comment`

Section: base; Context: S; Type: string; Default: `No comment`

This is a text field that is seen next to a share when a client does a queries the server, either via the network neighborhood or via net view to list what shares are available. If you want to set the string that is displayed next to the machine name then see the parameter.

### `config backend`

Section: base; Context: G; Type: enum; Default: `file`

This controls the backend for storing the configuration. Possible values are file (the default) and registry . When registry is encountered while loading smb.conf , the configuration read so far is dropped and the global options are read from registry instead. So this triggers a registry only configuration. Share definitions are not read immediately but instead registry shares is set to yes . Note: This option can not be set inside the registry configuration itself.

### `dos charset`

Section: base; Context: G; Type: string

DOS SMB clients assume the server has the same charset as they do. This option specifies which charset Samba should use to talk to DOS clients. The default depends on which charsets you have installed. Samba tries to use charset 850 but falls back to ASCII in case it is not available. Run testparm 1 to check the default on your system.

### `enable core files`

Section: base; Context: G; Type: boolean; Default: `yes`

This parameter specifies whether core dumps should be written on internal exits. Normally set to yes . You should never need to change this.

### `interfaces`

Section: base; Context: G; Type: cmdlist

This option allows you to override the default network interfaces list that Samba will use for browsing, name registration and other NetBIOS over TCP/IP (NBT) traffic. By default Samba will query the kernel for the list of all active interfaces and use any interfaces except 127.0.0.1 that are broadcast capable. The option takes a list of interface strings. Each string can be in any of the following forms: a network interface name (such as eth0). This may include shell-like wildcards so eth* will match any interface starting with the substring "eth" an IP address. In this case the netmask is determined from the list of interfaces obtained from the kernel an IP/mask pair. a broadcast/mask pair. The "mask" parameters can either be a bit length (such as 24 for a C class network) or a full netmask in dotted decimal form. The "IP" parameters above can either be a full dotted decimal IP address or a hostname which will be looked up via the OS's normal hostname resolution mechanisms. By default Samba enables all active interfaces that are broadcast capable except the loopback adaptor (IP address 127.0.0.1). In order to support SMB3 multi-channel configurations, smbd understands some extra parameters which can be appended after the actual interface with this extended syntax (note that the quoting is important in order to handle the ; and , characters): "interface[;key1=value1[,key2=value2[...]]]" Known keys are speed, capability, if_index and options. Speed is specified in bits per second. Known capabilities are RSS and RDMA. The if_index should be used with care: the values must not coincide with indexes used by the kernel. Note that these options are mainly intended for testing and development rather than for production use. At least on Linux systems, these values should be auto-detected, but the settings can serve as last a resort when autodetection is not working or is not available. The specified values overwrite the auto-detected values. The possible values for options are "dynamic" and "nodynamic". Use this option in combination with setting Use the "dynamic" to have smbd open/close listening sockets on the interface, when IP addresses are added to or removed from the interface. Use the "nodynamic" option to ignore any ip add/remove events for interface. Please note that when an IP address is removed, connections to that IP address are also terminated (traditional behaviour has been to keep the TCP flow alive). Note that dynamically opening/closing listening sockets is only available on some operating systems (currently Linux). The first two example below configures three network interfaces corresponding to the eth0 device and IP addresses 192.168.2.10 and 192.168.3.10. The netmasks of the latter two interfaces would be set to 255.255.255.0. The other examples show how per interface extra parameters can be specified. Notice the possible usage of "," and ";", which makes the double quoting necessary.

### `mdns name`

Section: base; Context: G; Type: enum; Default: `netbios`

This parameter controls the name that multicast DNS support advertises as its' hostname. The default is to use the NETBIOS name which is typically the hostname in all capital letters. A setting of mdns will defer the hostname configuration to the MDNS library that is used.

### `multicast dns register`

Section: base; Context: G; Type: boolean; Default: `yes`

If compiled with proper support for it, Samba will announce itself with multicast DNS services like for example provided by the Avahi daemon. This parameter allows disabling Samba to register itself.

### `netbios aliases`

Section: base; Context: G; Type: cmdlist; Default: `empty string (no additional names)`

This is a list of NetBIOS names that nmbd will advertise as additional names by which the Samba server is known. This allows one machine to appear in browse lists under multiple names. If a machine is acting as a browse server or logon server none of these names will be advertised as either browse server or logon servers, only the primary name of the machine will be advertised with these capabilities.

### `netbios name`

Section: base; Context: G; Type: ustring; Default: `machine DNS name`

This sets the NetBIOS name by which a Samba server is known. By default it is the same as the first component of the host's DNS name. If a machine is a browse server or logon server this name (or the first component of the hosts DNS name) will be the name that these services are advertised under. Note that the maximum length for a NetBIOS name is 15 characters. There is a bug in Samba that breaks operation of browsing and access to shares if the netbios name is set to the literal name PIPE . To avoid this problem, do not name your Samba server PIPE .

### `netbios scope`

Section: base; Context: G; Type: ustring

This sets the NetBIOS scope that Samba will operate under. This should not be set unless every machine on your LAN also sets this value.

### `path`

Section: base; Context: S; Type: string

This parameter specifies a directory to which the user of the service is to be given access. In the case of printable services, this is where print data will spool prior to being submitted to the host for printing. For a printable service offering guest access, the service should be readonly and the path should be world-writeable and have the sticky bit set. This is not mandatory of course, but you probably won't get the results you expect if you do otherwise. Any occurrences of %u in the path will be replaced with the UNIX username that the client is using on this connection. Any occurrences of %m will be replaced by the NetBIOS name of the machine they are connecting from. These replacements are very useful for setting up pseudo home directories for users. Note that this path will be based on if one was specified.

### `prefork backoff increment`

Section: base; Context: G; Type: integer; Default: `10`

This option specifies the number of seconds added to the delay before a prefork master or worker process is restarted. The restart is initially zero, the prefork backoff increment is added to the delay on each restart up to the value specified by "prefork maximum backoff". Additionally set the backoff for an individual service by using "prefork backoff increment: service name" i.e. "prefork backoff increment:ldap = 2" to set the backoff increment to 2. If the backoff increment is 2 and the maximum backoff is 5. There will be a zero second delay for the first restart. A two second delay for the second restart. A four second delay for the third and any subsequent restarts

### `prefork children`

Section: base; Context: G; Type: integer; Default: `4`

This option controls the number of worker processes that are started for each service when prefork process model is enabled (see samba 8 -M) The prefork children are only started for those services that support prefork (currently ldap, kdc and netlogon). For processes that don't support preforking all requests are handled by a single process for that service. This should be set to a small multiple of the number of CPU's available on the server Additionally the number of prefork children can be specified for an individual service by using "prefork children: service name" i.e. "prefork children:ldap = 8" to set the number of ldap worker processes.

### `prefork maximum backoff`

Section: base; Context: G; Type: integer; Default: `120`

This option controls the maximum delay before a failed pre-fork process is restarted.

### `realm`

Section: base; Context: G; Type: string

This option specifies the kerberos realm to use. The realm is used as the ADS equivalent of the NT4 domain . It is usually set to the DNS name of the kerberos server.

### `server services`

Section: base; Context: G; Type: list; Default: `s3fs, rpc, nbt, wrepl, ldap, cldap, kdc, drepl, ft_scanner, winbindd, ntp_signd, kcc, dnsupdate, dns`

This option contains the services that the Samba daemon will run. An entry in the smb.conf file can either override the previous value completely or entries can be removed from or added to it by prefixing them with + or - .

### `server string`

Section: base; Context: G; Type: string; Default: `Samba %v`

This controls what string will show up in the printer comment box in print manager and next to the IPC connection in net view . It can be any string that you wish to show to your users. It also sets what will appear in browse lists next to the machine name. A %v will be replaced with the Samba version number. A %h will be replaced with the hostname.

### `unix charset`

Section: base; Context: G; Type: string; Default: `UTF-8`

Specifies the charset the unix machine Samba runs on uses. Samba needs to know this in order to be able to convert text to the charsets other SMB clients use. This is also the charset Samba will use when specifying arguments to scripts that it invokes.

### `workgroup`

Section: base; Context: G; Type: ustring; Default: `WORKGROUP`

This controls what workgroup your server will appear to be in when queried by clients. Note that this parameter also controls the Domain name used with the domain setting.
