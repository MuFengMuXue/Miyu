# StrongSwan

IPSec is an encryption and authentication standard that can be used to build secure Virtual Private Networks (VPNs).

It is natively supported by the Linux kernel, but configuration of encryption keys is left to the user. The IKE protocols are therefore used in IPSec VPNs to automatically negotiate key exchanges securely using a variety of means, including certificates, pre-shared keys or both.

They are typically implemented in userspace daemons on the server side. strongSwan is an IKE daemon with full support for
IKEv1 and IKEv2. It is natively supported by most modern clients, including Linux, Windows 7, Apple iOS, Mac OSX, FreeBSD and BlackBerry OS.

## Installation
Install the  package.

## Certificates
The first step is to generate the X.509 certificates, including a certificate
authority (CA), a server certificate, and at least one client certificate.

## Certificate Authority
Let us start by creating a self-signed root CA certificate:

 $ cd /etc/ipsec.d/
 $ ipsec pki --gen --type rsa --size 4096 --outform pem > private/strongswanKey.pem
 $ chmod 600 private/strongswanKey.pem
 $ ipsec pki --self --ca --lifetime 3650 --outform pem \
             --in private/strongswanKey.pem --type rsa \
             --dn "C=CH, O=strongSwan, CN=strongSwan Root CA" \
       > cacerts/strongswanCert.pem

The result is a 4096 bit RSA private key  (line 2) and
a self-signed CA certificate  (line 7) with a
validity of 10 years (3650 days). The files are stored in PEM encoded format.

You can change the Distinguished Name (DN) to more relevant values for country
(C), organization (O), and common name (CN), but you do not have to.

To list the properties of your newly generated certificate, type in the
following command:

## Host Certificate
This certificate will be used to authenticate the VPN server. Run the following
commands:

 $ cd /etc/ipsec.d/
 $ ipsec pki --gen --type rsa --size 2048 --outform pem > private/vpnHostKey.pem
 $ chmod 600 private/vpnHostKey.pem
 $ ipsec pki --pub --in private/vpnHostKey.pem --type rsa | \
       ipsec pki --issue --lifetime 730 --outform pem \
                 --cacert cacerts/strongswanCert.pem \
                 --cakey private/strongswanKey.pem \
                 --dn "C=CH, O=strongSwan, CN=vpn.example.com" \
                 --san vpn.example.com \
                 --flag serverAuth --flag ikeIntermediate \
           > certs/vpnHostCert.pem

The result is a 2048 bit RSA private key  (line 2). In
line 4 we extract its public key and pipe it over to issue
 (line 11), a host certificate signed by your CA. The
certificate has a validity of two years (730 days). It identifies the VPN host
by its Fully Qualified Domain Name (FQDN) (here: ).

Let us take a look at the properties of our newly generated certificate.

## Client Certificate
Any client will require a personal certificate in order to use the VPN. The
process is analogous to generating a host certificate, except that we identify
a client certificate by the client's e-mail address rather than a hostname.

 $ cd /etc/ipsec.d/
 $ ipsec pki --gen --type rsa --size 2048 --outform pem > private/ClientKey.pem
 $ chmod 600 private/ClientKey.pem
 $ ipsec pki --pub --in private/ClientKey.pem --type rsa | \
       ipsec pki --issue --lifetime 730 --outform pem \
                 --cacert cacerts/strongswanCert.pem \
                 --cakey private/strongswanKey.pem \
                 --dn "C=CH, O=strongSwan, CN=myself@example.com" \
                 --san myself@example.com \
           > certs/ClientCert.pem

The result is a 2048 bit RSA private key  (line 2).
In line 6 we extract its public key and pipe it over to issue  (line 10), the first client certificate signed by your CA.
The certificate has a validity of two years (730 days) and identifies the client by its e-mail address (here: ).

Finally we will bundle all needed certificates and keys into a PKCS#12 file with a passphrase, which is the most convenient format for clients.

 $ openssl pkcs12 -export -name "My own VPN client certificate" \
                  -inkey private/ClientKey.pem \
                  -in certs/ClientCert.pem  \
                  -certfile cacerts/strongswanCert.pem \
                  -caname "strongSwan Root CA" \
                  -out Client.p12

## VPN Variants
The easiest configuration to get running with is IPSec in tunnel mode, described below.

## IPSec in tunnel mode
VPN configuration can be found in . The following
contains the necessary options to build a basic, functional VPN server:

## IPSec in transport mode
Compared to tunnel mode, transport mode does not encrypt the original IP header from its point of view.  This is useful if something else (i.e. GRE) has already encapsulated the original packet to be transported through a tunnel, before IPSec gets it.  From the point of view of IPSec, the IP header it thinks is the original is actually the IP header already setup for the tunneling, and it will encrypt what is truly the original IP header as just part of the encapsulated packet payload, without realizing it is doing it.

## IPSec/L2TP
The L2TP/IPsec VPN client setup page describes how to setup a client to connect to an IPSec/L2TP server. This variant of an IPSec VPN has the advantage of allowing to tunnel non-IP packets, contrary to pure IPSec, but at the expense of having to run an additional L2TP daemon.

## Secrets
The server's private key needs to be configured in , like the following example:

Whenever you edit  while strongSwan is running, you must
reload the file:

 $ ipsec rereadsecrets

## Networking
You’re almost done setting up your server. There are a few things left to make
your VPN server properly route the VPN tunnel:

The VPN configuration above automatically assigns an IP address to the client
using DHCP, so you need to have a working DHCP server. If the server is running
on the same host as strongSwan, you may need to edit
 like this:

{{hc|/etc/strongswan.d/charon/dhcp.conf|dhcp {
 force_server_address = yes
 server = 192.168.0.255
}
}}

You may also need to allow the following protocols in your firewall:

* ESP (Encrypted Secure Payload): Standard IPSec traffic
* UDP 4500: IPSec traffic in "NAT Traversal" mode
* UDP 500: Key exchanges (IKE)

## Starting
Finally, you can start and enable .

## Running Strongswan in a Container
For running  in a container like systemd-nspawn you need the following service file:

{{hc|/etc/systemd/system/systemd-nspawn@.service.d/override.conf}|
ExecStart=
ExecStart=/usr/bin/systemd-nspawn --quiet --keep-unit --boot --link-journal=try-guest --settings=override --machine=%I --capability=CAP_NET_ADMIN --network-veth
}}

## Troubleshooting
## Routing issues
If you are having troubles with routing traffic from client (road warrior) to the remote network, try disabling the  plugin on the server. This plugin is enabled by default in the official Arch package since version 5.6.0. See the associated [https://wiki.strongswan.org/issues/2462 issue in strongswan bugtracker.

## SSL Handshake Timeouts
Some users have had intermittent SSL handshake timeouts, such as:

*  getting stuck at "TLSv1.3 (OUT), TLS handshake, Client hello (1):"
* Firefox stalling loading a page, showing "Performing a TLS handshake to www.example.com"

Some users have fixed (or worked around?) this problem by decreasing their network interface mtu to be in the 1422-1438 range, even if they do not need to do so without a VPN or when using OpenVPN. [https://wiki.strongswan.org/projects/strongswan/wiki/ForwardingAndSplitTunneling#MTUMSS-issues

Lowering mtu could potentially cause other problems, so your mileage may vary.  This fix/workaround will likely somewhat decrease internet and internal network performance.  (But, SSL handshakes will stop stalling.)  If you are using jumbo frames, this may significantly decrease internal network performance.

Check your interface's mtu: (The one being used to connect to the VPN)

 $ ip link

Consider this default (probably 1500) bad.

You can efficiently try to find a mtu that prevents an SSL timeout by repeating this process, perhaps starting with a really low ''trial-mtu like 1300, or lower if that still fails: (interface'' is the name shown above by , not a full path like )

 # ip link set dev ''interface mtu trial-mtu''
 $ while(curl -v https://example.com); do
 > sleep 2
 > done

If it succeeds enough times for you to be confident an intermittent failure should have happened, consider this mtu as good, and hit .  Re-run the above commands with a ''trial-mtu'' halfway between this one and your closest known bad mtu.

If it gets stuck on a TLS handshake, consider this as bad, and hit .  Re-run the above with halfway between this one and your closest known good mtu.

## Connection established but no traffic
In certain setups, like KDE, you might get a established connection using  but you cannot reach any outside machine. This could be due to the  package not being installed. It is an optional dependency, but it might be required for your situation.
