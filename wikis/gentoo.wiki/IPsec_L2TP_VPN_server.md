Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/IPsec_L2TP_VPN_server/hu "IPsec L2TP VPN szerver (99% translated)")
-   [русский](https://wiki.gentoo.org/wiki/IPsec_L2TP_VPN_server/ru "IPsec L2TP VPN сервер (63% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/IPsec_L2TP_VPN_server/ja "IPsec L2TP VPN サーバ (90% translated)")

** Important**\
IPsec/L2TP is considered a legacy VPN protocol. For modern clients, (Windows since Windows 7, Android since 11, macOS since 10.11, iOS since 9) consider [IPsec IKEv2 MSCHAPv2 VPN server](https://wiki.gentoo.org/wiki/IPsec_IKEv2_MSCHAPv2_VPN_server "IPsec IKEv2 MSCHAPv2 VPN server") instead. Note strongSwan can simultaneously handle legacy IKEv1/L2TP clients and modern pure IKEv2/MSCHAPv2 clients, if both need to be supported

Many operating systems support an L2TP/IPsec VPN out-of-the-box. By combining the confidentiality- and authentication services of IPsec (Internet Protocol security), the network tunneling of the Layer 2 Tunnel Protocol (L2TP) and the user authentication through pppd, administrators can define VPN networks across multiple, heterogeneous systems. This allows setting up a VPN across Android, Windows, Linux, MacOS and other operating systems without any commercial software requirements.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Assumptions and example settings]](#Assumptions_and_example_settings)
-   [[2] [IPsec]](#IPsec)
    -   [[2.1] [Option 1: LibreSwan]](#Option_1:_LibreSwan)
        -   [[2.1.1] [PSK setup for LibreSwan]](#PSK_setup_for_LibreSwan)
        -   [[2.1.2] [Certificate based setup for LibreSwan]](#Certificate_based_setup_for_LibreSwan)
    -   [[2.2] [Option 2: strongSwan]](#Option_2:_strongSwan)
        -   [[2.2.1] [PSK setup for strongSwan]](#PSK_setup_for_strongSwan)
        -   [[2.2.2] [Certificate based setup for strongSwan]](#Certificate_based_setup_for_strongSwan)
-   [[3] [L2TP]](#L2TP)
    -   [[3.1] [Restricting L2TP to the IPsec tunnel]](#Restricting_L2TP_to_the_IPsec_tunnel)
        -   [[3.1.1] [iptables]](#iptables)
        -   [[3.1.2] [nftables]](#nftables)
        -   [[3.1.3] [firewalld]](#firewalld)
    -   [[3.2] [Using xl2tpd]](#Using_xl2tpd)
-   [[4] [PPP]](#PPP)
    -   [[4.1] [Authentication]](#Authentication)
        -   [[4.1.1] [Authentication via chap.secrets]](#Authentication_via_chap.secrets)
        -   [[4.1.2] [Authentication via Samba]](#Authentication_via_Samba)
        -   [[4.1.3] [Authentication via RADIUS]](#Authentication_via_RADIUS)
        -   [[4.1.4] [Authentication via EAP-TLS]](#Authentication_via_EAP-TLS)
-   [[5] [Server Notes]](#Server_Notes)
    -   [[5.1] [Server behind NAT]](#Server_behind_NAT)
        -   [[5.1.1] [Opening ports]](#Opening_ports)
-   [[6] [Client Notes]](#Client_Notes)
    -   [[6.1] [General]](#General)
        -   [[6.1.1] [Creating the PKCS12 file]](#Creating_the_PKCS12_file)
    -   [[6.2] [Windows]](#Windows)
        -   [[6.2.1] [RRAS Error 809: The network connection between your computer and VPN could not be established because the remote server is not responding\...]](#RRAS_Error_809:_The_network_connection_between_your_computer_and_VPN_could_not_be_established_because_the_remote_server_is_not_responding...)
        -   [[6.2.2] [Weak proposals]](#Weak_proposals)
        -   [[6.2.3] [Enabling split tunneling]](#Enabling_split_tunneling)
            -   [[6.2.3.1] [Enable split tunneling via the GUI]](#Enable_split_tunneling_via_the_GUI)
            -   [[6.2.3.2] [Via PowerShell]](#Via_PowerShell)
        -   [[6.2.4] [Server behind NAT]](#Server_behind_NAT_2)
        -   [[6.2.5] [RRAS Error 835: The L2TP connection attempt failed because the security layer could not authenticate the remote computer\...]](#RRAS_Error_835:_The_L2TP_connection_attempt_failed_because_the_security_layer_could_not_authenticate_the_remote_computer...)
    -   [[6.3] [Mac OS X]](#Mac_OS_X)
    -   [[6.4] [Android]](#Android)
    -   [[6.5] [iOS]](#iOS)
-   [[7] [External resources]](#External_resources)

## [Introduction]

IPsec/L2TP is a commonly used VPN protocol used in Windows and other operating systems. All version of Windows since Windows 2000 have support built-in, not requiring an external client (like [OpenVPN](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN") does) making it very convenient. However, it is significantly harder to set up on the server side on Linux, as there\'s at least 3 layers involved: IPsec, L2TP, and PPP.

1.  The IPsec setup provides the confidentiality of the network communication and the client (system) authentication
2.  With L2TP a tunnel is set up so that the VPN traffic goes over IPsec in a transparent manner
3.  The PPP (Point-to-Point Protocol) setup manages the authentication of the users

This guide will not cover setting up DHCP, RADIUS, Samba or a Public Key Infrastructure (PKI). It also does not really cover how to configure Linux clients, although the step to do so can be derived from the guide pretty easily. It does cover some Windows client configuration for the purpose of troubleshooting the server setup.

### [Assumptions and example settings]

For the purpose of this guide, the following assumptions (or sample settings) are used:

-   Domain is example.com
-   Server name is vpn.example.com
-   CA file is called [ca.crt]
-   Server cert is [vpn.example.com.crt]
-   Server key is [vpn.example.com.key]
-   Client cert is [client.example.com.crt]
-   Client key is [client.example.com.key]

## [IPsec]

The first layer to set up is IPsec. Note IPsec is peer-to-peer, so in IPsec terminology, the *client* is called the **initiator** and the *server* is called the **responder**.

There are 2 implementations of IPsec in Portage: LibreSwan and strongswan. Both have NAT traversal enabled by default, but if the VPN server is behind NAT and the client is Windows, special client configuration is required.

In the next sections, the different configurations are explained. For each option, document

-   how to use PSK for authentication, and
-   how to use certificates for authentication

Make sure to pick one (either PSK or certificates). Note there is no provision within the IKEv1 protocol to negotiate PSKs. The only information available to choose which key to use is based on the source and destination IP addresses. Since, in the usual scenario, the responder won\'t know the initiator\'s IP in advance, *everyone* must use the same pre-shared key. Therefore, certificates (PKI) are highly recommended over pre-shared keys (PSK), even for only a single user. However generating certificates and creating a PKI is a rather complex process and out of scope of this document, but the [[[app-crypt/easy-rsa]](https://packages.gentoo.org/packages/app-crypt/easy-rsa)[]] package can make it less painful.

For this tutorial, when using certificate based authentication, the necessary certificates are already available.

### [Option 1: LibreSwan]

LibreSwan is a fork of Openswan (which itself a fork of FreeS/WAN). It is actually forked by the remaining original developers of Openswan, however after the original developers left Xelerance, a dispute about the \"Openswan\" name escalated to a lawsuit, after which the name LibreSwan was taken.

#### [PSK setup for LibreSwan]

A shared key must be created. It may either be specified by a quoted string or by a hex number. Based on the next example, `PUT_VPN_SERVER_IP` should be replaced by the server\'s IP address. The domain name can be used, but it is not recommended by the LibreSwan developers. The `%any` setting allows any client to use this PSK.

[FILE] **`/etc/ipsec.d/vpn.example.com.secret`**

    PUT_VPN_SERVER_IP %any : PSK 0x87839cfdab5f74bc211de156d2902d128bec3243
    # Or to use a plain text key instead of hex:
    # PUT_VPN_SERVER_IP %any : PSK "password_pass"

Then create [/etc/ipsec.d/vpn.example.com.conf]:

[FILE] **`/etc/ipsec.d/vpn.example.com.conf`**

    conn vpnserver
            type=transport
            authby=secret
            ikev2=no
            pfs=no
            rekey=no
            keyingtries=1
            left=%defaultroute
            leftprotoport=udp/l2tp
            leftid=@vpn.example.com
            right=%any
            rightprotoport=udp/%any
            auto=add

#### [Certificate based setup for LibreSwan]

LibreSwan requires Network Security Services (NSS) to be properly configured and used for the certificate management. To make things easy, a PKCS#12 bundle should be created containing the server\'s secret key, the server\'s certificate and the CA certificate.

`user `[`$`]`openssl pkcs12 -export -certfile ca.crt -inkey vpn.example.com.key -in vpn.example.com.crt -out /etc/ipsec.d/vpn.example.com.p12 -passout pass:`

The bundle can then be imported into the NSS database:

`root `[`#`]`pk12util -i vpn.example.com.p12 -d /var/lib/ipsec/nss`

The LibreSwan configuration files will refer to the nickname for the imported objects. Use [certutil -L -d /var/lib/ipsec/nss] and [certutil -K -d /var/lib/ipsec/nss] to see what they are.

Above, `vpn.example.com` is used for the nickname obtained through the [certutil -K -d .] command.

[FILE] **`/etc/ipsec.d/vpn.example.com.conf`**

    conn vpnserver
            type=transport
            authby=rsasig
            ikev2=no
            pfs=no
            rekey=no
            keyingtries=1
            left=%defaultroute
            leftprotoport=udp/l2tp
            leftcert=vpn.example.com
            leftid=@vpn.example.com
            right=%any
            rightprotoport=udp/%any
            rightrsasigkey=%cert
            auto=add

Here, `vpn.example.com` was the nickname obtained via the [certutil -L -d .] command.

### [Option 2: strongSwan]

strongSwan is a fork of FreeS/WAN (although much code has been replaced).

While strongSwan supports the legacy (stroke) ipsec.conf configuration mechanism, it introduces a new kind of config file for a new interface: the Versatile IKE Control Interface (VICI).

To use it, a few directories need to be defined:

`root `[`#`]`( umask 007 ;\ `

    mkdir /etc/swanctl/;\
    mkdir /etc/swanctl/x509;\
    mkdir /etc/ipsec.d;\
    mkdir /etc/ipsec.d/; )

#### [PSK setup for strongSwan]

A shared key must be created. It may either be specified by a quoted string or by a hex number.

[FILE] **`/etc/swanctl/conf.d/vpn.example.com.conf`**

    connections
            remote-1
            children
            }
        }
    }
    pools
    secrets
    }
    authorities

The [proposals=aes128-sha1-modp1024,default] is for Windows 7 and Android. Without it, they will be unable to connected. See the client notes below.

#### [Certificate based setup for strongSwan]

The files must be copied to the correct place:

`root `[`#`]`cp ca.crt /etc/swanctl/x509ca`

`root `[`#`]`cp server.example.com.crt /etc/swanctl/x509`

`root `[`#`]`cp server.example.com.key /etc/swanctl/private`

Finally update the [/etc/swanctl/conf.d/vpn.example.com.conf] file as follows:

[FILE] **`/etc/swanctl/conf.d/vpn.example.com.conf`**

    connections
            remote-1
            children
            }
        }
    }
    pools
    secrets
    authorities

The [proposals=aes128-sha1-modp1024,default] is for Windows 7 and Android. Without it, they will be unable to connected. See the client notes below.

## [L2TP]

The second layer, Layer 2 Tunneling Protocol (L2TP), is much easier to setup. Like IPsec, L2TP is a peer-to-peer protocol. The client side is called the *L2TP Access Concentrator* or LAC and the server side is called the *L2TP Network Server* or LNS.

### [Restricting L2TP to the IPsec tunnel]

** Warning**\
L2TP is insecure, and should **not** be accessible outside the IPsec connection

#### [iptables]

When using iptables, use the following rules to block all L2TP connection outside the ipsec layer:

`root `[`#`]`iptables -t filter -A INPUT -p udp -m policy --dir in --pol ipsec -m udp --dport l2tp -j ACCEPT `

`root `[`#`]`iptables -t filter -A INPUT -p udp -m udp --dport l2tp -j REJECT --reject-with icmp-port-unreachable `

`root `[`#`]`iptables -t filter -A OUTPUT -p udp -m policy --dir out --pol ipsec -m udp --sport l2tp -j ACCEPT `

`root `[`#`]`iptables -t filter -A OUTPUT -p udp -m udp --sport l2tp -j REJECT --reject-with icmp-port-unreachable `

#### [nftables]

When using nftables, use the following script to block all L2TP connection outside the ipsec layer:

[CODE]

    #!/sbin/nft -f

    table ip l2tp-ipsec

        chain OUTPUT
    }

#### [firewalld]

Firewalld only blocks incoming connection, not outgoing, and even \"rich\" rules are not expressive enough to state what is needed for inbound. However, firewalld is designed to live with nftables tables, so the nftables solution above will work and not interfere with it.

### [Using xl2tpd]

Unlike other L2TP servers, [xl2tpd] can maintain an IP address pool without a DHCP or RADIUS server. This is a layering violation, but for a small setup it is extremely convenient:

[FILE] **`/etc/xl2tpd/xl2tpd.conf`**

    [global]
    port = 1701
    access control = no

    [lns default]
    ip range = 172.21.118.2-172.21.118.254
    local ip = 172.21.118.1
    require authentication = yes
    name = LinuxVPN
    pppoptfile = /etc/ppp/options.xl2tpd

To use a RADIUS or DHCP server, leave off the `ip range` and `local ip` parts.

Create the options file as well:

[FILE] **`/etc/ppp/options.xl2tpd`**

    require-mschap-v2

This line is for Windows\'s benefit. Without it, (at least as of Windows 10) Windows will send EAP probes, which pppd rejects, but Windows will insist, rather then fall back. Manual configuration of the VPN connection will be for Windows to use MSCHAPv2 instead of EAP. By limiting Windows\'s choice, it will work \"out of the box\".

If more flexibility is desired and Windows client configuration is not an issue, this line can be dropped.

## [PPP]

The final layer to configure is the Point-to-Point Protocol (PPP) layer. The package to install here is [[[net-dialup/pppd]](https://packages.gentoo.org/packages/net-dialup/pppd)[]].

`root `[`#`]`emerge --ask net-dialup/pppd`

### [Authentication]

PPP is used to perform authentication. Unlike the certificate based or PSK authentication, the PPP layer is more for authenticating (and authorizing) the end users\' access to the VPN.

#### [Authentication via chap.secrets]

For small users (typically, those wanting to connect their home network from elsewhere), authentication can be done through the [chap.secrets] file:

[FILE] **`/etc/ppp/chap-secrets`**

    # Secrets for authentication using CHAP
    # client        server  secret                  IP addresses
    avatar          *       unontainium              *

** Note**\
When authenticating with domains, the client name will need to be mangled appropriately, in this case, `EXAMPLE\\avatar`.

** Warning**\
[/etc/ppp/chap-secrets] contains unencrypted passwords, so make sure only root can read or write it

#### [Authentication via Samba]

When the machine is part of (or hosting) an MS Domain or AD forest, and the clients are using winbind, then Samba can do the authentication. Add `plugin winbind.so` to the ppp options. Setting up Samba and pppd to do this is beyond the scope of this document.

#### [Authentication via RADIUS]

pppd can use RADIUS. Ensure the `radius` USE flag is set on [[[net-dialup/ppp]](https://packages.gentoo.org/packages/net-dialup/ppp)[]]. Then add `plugin radius.so` and `plugin radattr.so` to the PPP options. Setting up RADIUS is beyond the scope of this document.

#### [Authentication via EAP-TLS]

If individual users have certificates (which is not the same as the machine certificate above), then setup pppd to authenticate via EAP-TLS. Ensure the `eap-tls` USE flag is set on [[[net-dialup/ppp]](https://packages.gentoo.org/packages/net-dialup/ppp)[]]. The `require-eap` option might need to be included in the PPP options file as well. Setting up pppd to do this is beyond the scope of this document.

## [Server Notes]

### [Server behind NAT]

When the server is behind NAT (Network Address Translation), which is usually the case when the server is hosted after a home router, some specific attention pointers can help in ensuring the IPsec connection is stable and working.

#### [Opening ports]

2 ports need to be open:

-   UDP port 500 (for ISAKMP)
-   UDP port 4500 (for NAT Traversal)

Make sure to forward those to the VPN server.

Also the following Internet Protocols (not ports) need to be allowed as well:

-   50 (ESP)
-   51 (AH)

This might need to be configured on the router side if the router has protocol specific settings (most don\'t though).

## [Client Notes]

### [General]

#### [Creating the PKCS12 file]

The certificate should be packaged in a PKCS12 package. This can be done through openssl or gnutls:

`user `[`$`]`openssl pkcs12 -export -certfile ca.crt -inkey client.example.com.key -in client.example.com.crt -out client.example.com.p12`

`user `[`$`]`certtool --load-ca-certificate /home/salahx/easy-rsa/pki/ca.crt --load-certificate /home/salahx/easy-rsa/pki/issued/client.example.com.crt --load-privkey /home/salahx/easy-rsa/pki/private/client.example.com.key --to-p12 --p12-name=client.example.com.crt --outder --outfile client.example.com.p12`

Be sure to set a password. Some clients (like MacOS) will not open a passwordless p12 file. Some legacy clients can only handle DER encoded p12 files (default for openssl, certtool defaults to PEM). Also remember the certificate belongs to the machine/system, not the user.

### [Windows]

#### [RRAS Error 809: The network connection between your computer and VPN could not be established because the remote server is not responding\...]

When importing, it\'s important to choose \"Local Machine\" to import to, NOT \"Current User\". Otherwise, Windows can\'t find the certificate and just times out without ever contacting the IPSec server.

#### [Weak proposals]

Unlike other clients, Windows prefers the weakest proposal. So if 3des-sha1-modp1024 is offered, it will take it over a better option. On strongSwan, the added proposal aes128-sha1-modp1024 is added for the benefit of legacy clients (Windows 7 and earlier). Older version of Windows won\'t offer anything stronger than modp1024 by default. It is possible to allow or force Windows to accept a better proposal through a registry hack. Set **DWORD** `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Rasman\Parameters\NegotiateDH2048_AES256` to [1] to enable Windows to accept aes256-sha1-modp2048, set it to [2] to not allow anything weaker.

If there are no legacy clients (see Android section below), and all Windows clients are at least Windows 10 21H2 (might work with earlier versions) OR have the above registry hack applies, and the server is running strongSwan, the [proposal=aes128-sha1-modp1024] may be removed or adjusted.

#### [Enabling split tunneling]

By default, Windows connects via full tunnel mode (everything is routed over the VPN), however it\'s possible to enable split tunnel in Windows.

##### [Enable split tunneling via the GUI]

Go to \"Change adapter options\" to show the adapters. Right-click the VPN connection, choose Properties, then Networking, then Internet Protocol Version 4 (TCP/IPv4), then Properties, then Advanced, then uncheck \"Use default gateway on remote network\".

##### [Via PowerShell]

[CODE]

    Set-VPNconnection -name vpn.example.com -SplitTunneling $true

Substitute [vpn.example.com] with the given VPN connection name

#### [Server behind NAT]

Windows does not automatically support IPsec/L2TP servers behind NAT. See [Configure a L2TP/IPsec server behind a NAT-T device](https://docs.microsoft.com/en-US/troubleshoot/windows-server/networking/configure-l2tp-ipsec-server-behind-nat-t-device) to enable support.

#### [RRAS Error 835: The L2TP connection attempt failed because the security layer could not authenticate the remote computer\...]

The subjectAltName of the server certificate MUST match the server name being connected to. (When connecting by IP address, Windows skips this check).

### [Mac OS X]

MacOS X client require several steps:

1.  The CA and client certificates must be imported into the System keychain, not the Login keychain.
2.  In the Keychain app, the new CA is untrusted by default, so it must be marked trusted
3.  Also note that if corrected after the VPN connection is created, it is necessary to re-select the certificate under Authentication Settings to clear the error.

The \"Account Name\" should be the PPP username.

Note that Mac OS also checks the subjectAltName vs DNS, if it does not match, it will refuse to connect.

### [Android]

As of Android 12, Android no longer supports IPsec/L2TP. Like Windows, Android won\'t offer anything stronger than modp1024, so strongSwan config has an added proposal of aes128-sha1-modp1024. This works even on very old version of Android (at least 4.2). If there are no Android client or other legacy clients (see Windows above), the [proposal=aes128-sha1-modp1024] may be removed or adjusted.

### [iOS]

iOS does not support certificate-based authentication for IPSec/L2TP, only pre-shared keys (PSK). (It does support certificate for IPSec/XAuth, however).

## [External resources]

-   [Using a Linux L2TP/IPsec VPN server](http://www.jacco2.dds.nl/networking/freeswan-l2tp.html) from Jacco de Leeuw