# iwd.network

## Network configuration for wireless daemon

Author
Marcel Holtmann \<<marcel@holtmann.org>\>

Author
Denis Kenzior \<<denkenz@gmail.com>\>

Author
Andrew Zaborowski \<<andrew.zaborowski@intel.com>\>

Author
Tim Kourt \<<tim.a.kourt@linux.intel.com>\>

Author
James Prestwood \<<prestwoj@gmail.com>\>

Copyright
2013-2019 Intel Corporation

Version
iwd

Date
22 September 2019

Manual section
5

Manual group
Linux Connectivity

### SYNOPSIS

Network configuration files `.open`, `.psk` and `.8021x`

### DESCRIPTION

**iwd** stores information on known networks, and reads information on pre-provisioned networks, from small text configuration files. Those files live in the state directory specified by the environment variable *\$STATE_DIRECTORY*, which is normally provided by **systemd**. In the absence of such an environment variable it defaults to *\$LIBDIR/iwd*, which normally is set to */var/lib/iwd*. You can create, modify or remove those files. **iwd** monitors the directory for changes and will update its state accordingly. **iwd** will also modify these files in the course of network connections or as a result of D-Bus API invocations.

### FILE FORMAT

The syntax is similar to that of GNOME keyfile syntax (which is based on the format defined in the Desktop Entry Specification, see *http://freedesktop.org/Standards/desktop-entry-spec*). The recognized groups as well as keys and values in each group are documented here. Defaults are written in bold.

For completeness we include the description of the file syntax here. This is the syntax that the ell library's lsettings class implements. The syntax is based on lines and lines are delimited by newline characters.

Empty lines are ignored and whitespace at the beginning of a line is ignored. Comment lines have `#` as their first non-whitespace character.

Key-value lines contain a setting key, an equal sign and the value of the setting. Whitespace preceding the key, the equal sign or the value, is ignored. The key must be a continuous string of alphanumeric and underscore characters and minus signs only. The value starts at the first non-whitespace character after the first equal sign on the line and ends at the end of the line and must be correctly UTF-8-encoded. A boolean value can be `true` or `false` but `0` or `1` are also allowed. Integer values are written in base 10. String values, including file paths and hexstrings, are written as is except for five characters that may be backslash-escaped: space, `\t`, `\r`, `\n` and backslash itself. The latter three must be escaped. A space character must be escaped if it is the first character in the value string and is written as `\s`.

Settings are interpreted depending on the group they are in. A group starts with a group header line and contains all settings until the next group's header line. A group header line contains a `[` character followed by the group name and a `]` character. Whitespace is allowed before the `[` and after the `]`. A group name consists of printable characters other than `[` and `]`.

If a group name starts with the `@` sign, that group's content is handled by a parser extension instead and does not cause the previous non-extension group to end. The initial `@` sign must be followed by a non-empty extension name, another `@` sign and a group name as defined above. The extension name consists of printable characters other than `@`. No whitespace is allowed after the group header in this case. The extension payload syntax and length are determined by the extension name. Normal parsing rules defined in this section resume at the end of the payload and any settings after the end of the payload are handled as part of the previous non-extension group.

Currently the only extension supported is named pem and allows embedding the contents of a single RFC7468 PEM-formatted payload or a sequence of multiple PEM payloads. The payload should start with the `-----BEGIN` string on a line following the group header line and end with an `-----END` line as specified in the RFC. Newline characters before, between and after PEM payloads are included in the extension payload. No other extra characters are allowed.

### NAMING

File names are based on the network's SSID and security type: Open, PSK-protected or 802.1x. The name consist of the encoding of the SSID followed by `.open`, `.psk` or `.8021x`. The SSID appears verbatim in the name if it contains only alphanumeric characters, spaces, underscores or minus signs. Otherwise it is encoded as an equal sign followed by the lower-case hex encoding of the name.

### SETTINGS

The settings below are split into several sections and grouped into broad categories. Each category has a group associated with it which is given at the beginning of each sub-section. Recognized keys and valid values are listed following the group definition.

#### General Settings

The group `[Settings]` contains general settings.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>AutoConnect</p></td>
<td><p>Values: <strong>true</strong>, false</p>
<p>Whether the network can be connected to automatically</p></td>
</tr>
<tr>
<td><p>Hidden</p></td>
<td><p>Values: true, <strong>false</strong></p>
<p>Whether the network is hidden, i.e. its SSID must be included in an active scan request</p></td>
</tr>
<tr>
<td><p>AlwaysRandomizeAddress</p></td>
<td><p>Values: true, <strong>false</strong></p>
<p>If enabled, the MAC address will be fully randomized on each connection. This option is only used if [General].AddressRandomization is set to 'network'. See iwd.config. This setting should not be used with [Settings].AddressOverride, if both are set AddressOverride will be used.</p></td>
</tr>
<tr>
<td><p>AddressOverride</p></td>
<td><p>MAC address string</p>
<p>Override the MAC address used for connecting to this network. This option is only used if [General].AddressRandomization is set to 'network'. See iwd.config. This setting should not be used with [Settings].AlwaysRandomizeAddress, if both are set AddressOverride will be used.</p></td>
</tr>
<tr>
<td><p>TransitionDisable</p></td>
<td><p>Values: true, <strong>false</strong></p>
<p>If enabled, the use of TKIP pairwise cipher and connections without Management Frame Protection are disallowed. This will make certain legacy access points unavailable for use. Additional security hardening can also be applied via the [Settings].DisabledTransitionModes setting.</p>
<p>Properly configured Access Points will typically update this setting appropriately via Transition Disable indications. User customization of this value is thus typically not required.</p></td>
</tr>
<tr>
<td><p>DisabledTransitionModes</p></td>
<td><p>Comma-separated list of disabled transition modes:</p>
<ul>
<li>personal</li>
<li>enterprise</li>
<li>open</li>
</ul>
<p>If 'personal' mode is disabled, then legacy WPA2-Personal access points are no longer available to be connected to or roamed to. Only access points utilizing WPA3-Personal will be considered.</p>
<p>If 'enterprise' mode is disabled, then legacy WPA2-Enterprise access points are no longer available to be connected to or roamed to.</p>
<p>If 'open' mode is disabled, then non-OWE enabled access points will not be connected to.</p>
<p>Properly configured Access Points will typically update this setting appropriately via Transition Disable indications. User customization of this value is thus typically not required.</p></td>
</tr>
<tr>
<td><p>UseDefaultEccGroup</p></td>
<td><p>Values: true, false</p>
<p>Forces the use of the default ECC group (19) for protocols using ECC (WPA3 and OWE) if set true. If unset IWD will learn the capabilities of the network based on its initial association and retain that setting for the duration of its process lifetime.</p></td>
</tr>
</tbody>
</table>

#### Network Authentication Settings

The group `[Security]` contains settings for Wi-Fi security and authentication configuration. This group can be encrypted by enabling `SystemdEncrypt`, see *iwd.config* for details on this option. If this section is encrypted (only contains EncryptedSalt/EncryptedSecurity) it should not be modified. Modifying these values will result in the inability to connect to that network.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>Passphrase</p></td>
<td><p>8..63 character string</p>
<p>Passphrase to be used when connecting to WPA-Personal networks. Required when connecting to WPA3-Personal (SAE) networks. Also required if the <em>PreSharedKey</em> is not provided. If not provided in settings, the agent will be asked for the passphrase at connection time.</p></td>
</tr>
<tr>
<td><p>PasswordIdentifier</p></td>
<td><p>string</p>
<p>An identifier string to be used with the passphrase. This is used for WPA3-Personal (SAE) networks if the security has enabled password identifiers for clients.</p></td>
</tr>
<tr>
<td><p>PreSharedKey</p></td>
<td><p>64 character hex string</p>
<p>Processed passphrase for this network in the form of a hex-encoded 32 byte pre-shared key. Must be provided if <em>Passphrase</em> is omitted.</p></td>
</tr>
<tr>
<td><p>EAP-Method</p></td>
<td><p>one of the following methods:</p>
<p>AKA, AKA', MSCHAPV2, PEAP, PWD, SIM, TLS, TTLS.</p>
<p>The following additional methods are allowed as TTLS/PEAP inner methods:</p>
<p>GTC, MD5.</p></td>
</tr>
<tr>
<td><p>EAP-Identity</p></td>
<td><p>string</p>
<p>Identity string transmitted in plaintext. Depending on the EAP method, this value can be optional or mandatory. GTC, MD5, MSCHAPV2, PWD require an identity, so if not provided, the agent will be asked for it at connection time. TLS based methods (PEAP, TLS, TTLS) might still require an <em>EAP-Identity</em> to be set, depending on the RADIUS server configuration.</p></td>
</tr>
<tr>
<td><p>EAP-Password</p></td>
<td><p>string</p>
<p>Password to be provided for WPA-Enterprise authentication. If not provided, the agent will be asked for the password at connection time. Required by: GTC, MD5, MSCHAPV2, PWD.</p></td>
</tr>
<tr>
<td><p>EAP-Password-Hash</p></td>
<td><p>hex string</p>
<p>Some EAP methods can accept a pre-hashed version of the password. For MSCHAPV2, a MD4 hash of the password can be given here.</p></td>
</tr>
<tr>
<td>EAP-TLS-CACert,<br />
EAP-TTLS-CACert,<br />
EAP-PEAP-CACert</td>
<td><p>absolute file path or embedded pem</p>
<p>Path to a PEM-formatted X.509 root certificate list to use for trust verification of the authenticator. The authenticator's server's certificate chain must be verified by at least one CA in the list for the authentication to succeed. If omitted, then authenticator's certificate chain will not be verified (not recommended.)</p></td>
</tr>
<tr>
<td><p>EAP-TLS-ClientCert</p></td>
<td><p>absolute file path or embedded pem</p>
<p>Path to the client X.509 certificate or certificate chain to send on server request.</p></td>
</tr>
<tr>
<td><p>EAP-TLS-ClientKey</p></td>
<td><p>absolute file path or embedded pem</p>
<p>Path to the client private key corresponding to the public key provided in <em>EAP-TLS-ClientCert</em>. The recommended format is PKCS#8 PEM.</p></td>
</tr>
<tr>
<td><p>EAP-TLS-ClientKeyBundle</p></td>
<td><p>absolute file path</p>
<p>As an alternative to <em>EAP-TLS-ClientCert</em> and <em>EAP-TLS-ClientKey</em> IWD can load both the certificate and the private key from a container file pointed by this setting. The recommended format is PKCS#12 when this is used.</p></td>
</tr>
<tr>
<td>EAP-TLS-<br />
ClientKeyPassphrase</td>
<td><p>string</p>
<p>Decryption key for the client key files. This should be used if the certificate or the private key in the files mentioned above is encrypted. When not given, the agent is asked for the passphrase at connection time.</p></td>
</tr>
<tr>
<td>EAP-TLS-ServerDomainMask,<br />
EAP-TTLS-ServerDomainMask,<br />
EAP-PEAP-ServerDomainMask</td>
<td><p>string</p>
<p>A mask for the domain names contained in the server's certificate. At least one of the domain names present in the certificate's Subject Alternative Name extension's DNS Name fields or the Common Name has to match at least one mask, or authentication will fail. Multiple masks can be given separated by semicolons. The masks are split into segments at the dots. Each segment has to match its corresponding label in the domain name. An asterisk segment in the mask matches any label. An asterisk segment at the beginning of the mask matches one or more consecutive labels from the beginning of the domain string.</p></td>
</tr>
<tr>
<td>EAP-TLS-FastReauthentication,<br />
EAP-TTLS-FastReauthentication,<br />
EAP-PEAP-FastReauthentication,</td>
<td><p>Values: <strong>true</strong>, false</p>
<p>Controls whether TLS session caching for EAP-TLS, EAP-TTLS and EAP-PEAP is used. This allows for faster re-connections to EAP-Enterprise based networks.</p>
<p>Some network authenticators may be misconfigured in a way that TLS session resumption is allowed but actually attempting it will cause the EAP method to fail or time out. In that case, assuming the credentials and other settings are correct, every other connection attempt will fail as sessions are cached and forgotten in alternating attempts. Use this setting to disable caching for this network.</p></td>
</tr>
<tr>
<td>EAP-TTLS-Phase2-Method</td>
<td>The following values are allowed:<br />
   Tunneled-CHAP,<br />
   Tunneled-MSCHAP,<br />
   Tunneled-MSCHAPv2,<br />
   Tunneled-PAP or<br />
   a valid EAP method name (see <em>EAP-Method</em>)
Phase 2 authentication method for EAP-TTLS. Can be either one of the TTLS-specific non-EAP methods (Tunneled-*), or any EAP method documented here. The following two settings are used if any of the non-EAP methods is used.</td>
</tr>
<tr>
<td>EAP-TTLS-Phase2-Identity</td>
<td>The secure identity/username string for the TTLS non-EAP Phase 2 methods. If not provided <strong>iwd</strong> will request a username at connection time.</td>
</tr>
<tr>
<td>EAP-TTLS-Phase2-Password</td>
<td>Password string for the TTLS non-EAP Phase 2 methods. If not provided IWD will request a passphrase at connection time.</td>
</tr>
<tr>
<td>EAP-TTLS-Phase2-*</td>
<td>Any settings to be used for the inner EAP method if one was specified as <em>EAP-TTLS-Phase2-Method</em>, rather than a TTLS-specific method. The prefix <em>EAP-TTLS-Phase2-</em> replaces the <em>EAP-</em> prefix in the setting keys and their usage is unchanged. Since the inner method's negotiation is encrypted, a secure identity string can be provided.</td>
</tr>
<tr>
<td>EAP-PEAP-Phase2-*</td>
<td>Any settings to be used for the inner EAP method with EAP-PEAP as the outer method. The prefix <em>EAP-PEAP-Phase2-</em> replaces the <em>EAP-</em> prefix in the setting keys and their usage is unchanged. Since the inner method's negotiation is encrypted, a secure identity string can be provided.</td>
</tr>
</tbody>
</table>

#### Network Configuration Settings

The group `[Network]` contains general network settings and any network specific overrides for global defaults defined in the main iwd configuration file.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>MulticastDNS</p></td>
<td><p>Values: true, false, resolve</p>
<p>Configures multicast DNS for this network. If not specified, systemd-resolved's default value will remain untouched. See <code>man 5 systemd.network</code> for details.</p>
<p>Only applies when <code>NameResolvingService=systemd</code>.</p></td>
</tr>
</tbody>
</table>

The group `[IPv4]` contains settings for Internet Protocol version 4 (IPv4) network configuration with the static addresses.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>Address</p></td>
<td><p>IPv4 address string</p>
<p>The IPv4 address to assign. This field is required for the static configuration.</p></td>
</tr>
<tr>
<td><p>Gateway</p></td>
<td><p>IPv4 address string</p>
<p>The IPv4 address of the gateway (router). This field is required for the static configuration.</p></td>
</tr>
<tr>
<td><p>DNS</p></td>
<td><p>IPv4 address string list, space delimited</p>
<p>The IPv4 address(es) of the Domain Name System (DNS). This field is optional. DNS setting can be used to override the DNS entries received from the DHCP server.</p></td>
</tr>
<tr>
<td><p>Netmask</p></td>
<td><p>IPv4 address string</p>
<p>The IPv4 address of the subnet. This field is optional. 255.255.255.0 is used as default Netmask.</p></td>
</tr>
<tr>
<td><p>Broadcast</p></td>
<td><p>IPv4 address string</p>
<p>The IPv4 address to be used for the broadcast. This field is optional.</p></td>
</tr>
<tr>
<td><p>DomainName</p></td>
<td><p>string</p>
<p>The DomainName is the name of the local Internet domain. This field is optional. DomainName setting can be used to override the DomainName value obtained from the DHCP server.</p></td>
</tr>
<tr>
<td><p>SendHostname</p></td>
<td><p>Values: true, <strong>false</strong></p>
<p>Configures DHCP to include the hostname in the request. This setting is disabled by default.</p></td>
</tr>
</tbody>
</table>

The group `[IPv6]` contains settings for Internet Protocol version 6 (IPv6) network configuration.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><p>Enabled</p></td>
<td><p>Boolean</p>
<p>Whether IPv6 is enabled for this network. If not provided, then the global default provided by [Network].EnableIPv6 setting will be used. If IPv6 is disabled, then the 'disableipv6' setting in sysfs will be set to 1 and no IPv6 addresses or routes will be created for this network.</p></td>
</tr>
<tr>
<td><p>Address</p></td>
<td><p>IPv6 address string</p>
<p>The IPv6 address to assign. This field is required for the static configuration. The recognized format is according to inetpton followed by '/' and prefix length. If prefix length is omitted, then 128 is assumed.</p></td>
</tr>
<tr>
<td><p>Gateway</p></td>
<td><p>IPv6 address string</p>
<p>The IPv6 address of the gateway (router). This field is required for the static configuration.</p></td>
</tr>
<tr>
<td><p>DNS</p></td>
<td><p>IPv6 address string list, space delimited</p>
<p>The IPv6 address(es) of the Domain Name System (DNS). This field is optional. DNS setting can be used to override the DNS entries received from the DHCPv6 server or via Router Advertisements.</p></td>
</tr>
<tr>
<td><p>DomainName</p></td>
<td><p>string</p>
<p>The DomainName is the name of the local Internet domain. This field is optional. DomainName setting can be used to override the DomainName value obtained from the DHCPv6 server or via Router Advertisements.</p></td>
</tr>
</tbody>
</table>

#### Embedded PEMs

Rather than including an absolute path to a PEM file (for certificates and keys), the PEM itself can be included inside the settings file and referenced directly. This allows IEEE 802.1x network provisioning using a single file without any references to certificates or keys on the system.

An embedded PEM can appear anywhere in the settings file using the following format (in this example the PEM is named 'myca_cert'):

```
[@pem@my_ca_cert]
----- BEGIN CERTIFICATE -----
<PEM data>
----- END CERTIFICATE -----
```

After this special group tag it's as simple as pasting in a PEM file including the BEGIN/END tags. Now 'myca_cert' can be used to reference the certificate elsewhere in the settings file by prefixing the value with 'embed:'

EAP-TLS-CACert=embed:myca_cert

This is not limited to CA Certificates either. Client certificates, client keys (encrypted or not), and certificate chains can be included.

### EXAMPLES

The following are some examples of common configurations

#### Open Network (Hidden)

```
[Settings]
Hidden=true
```

#### Pre-Shared Key (PSK)

```
[Security]
Passphrase=secret123
```

#### PWD

```
[Security]
EAP-Method=PWD
EAP-Identity=user@domain.com
EAP-Password=secret123
```

#### TLS

```
[Security]
EAP-Method=TLS
EAP-TLS-ClientCert=/certs/client-cert.pem
EAP-TLS-ClientKey=/certs/client-key.pem
EAP-TLS-CACert=/certs/ca-cert.pem
EAP-TLS-ServerDomainMask=*.domain.com
```

#### TTLS + PAP

```
[Security]
EAP-Method=TTLS
EAP-Identity=open@identity.com
EAP-TTLS-CACert=/certs/ca-cert.pem
EAP-TTLS-Phase2-Method=Tunneled-PAP
EAP-TTLS-Phase2-Identity=username
EAP-TTLS-Phase2-Password=password
EAP-TTLS-ServerDomainMask=*.domain.com
```

#### PEAP + MSCHAPv2

```
[Security]
EAP-Method=PEAP
EAP-Identity=open@identity.com
EAP-PEAP-CACert=/certs/ca-cert.pem
EAP-PEAP-Phase2-Method=MSCHAPV2
EAP-PEAP-Phase2-Identity=username
EAP-PEAP-Phase2-Password=password
EAP-PEAP-ServerDomainMask=*.domain.com
```

### SEE ALSO

iwd(8), iwd.config(5)
