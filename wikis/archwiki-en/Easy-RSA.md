# Easy-RSA

The first step when setting up OpenVPN is to create a Public Key Infrastructure (PKI). In summary, this consists of:

* A public master Certificate Authority (CA) certificate and a private key.
* A separate public certificate and private key pair for each server.
* A separate public certificate and private key pair for each client.

One can think of the key-based authentication in terms similar to that of how SSH keys work with the added layer of a signing authority (the CA). OpenVPN relies on a bidirectional authentication strategy, so the client must authenticate the server's certificate and in parallel, the server must authenticate the client's certificate. This is accomplished by the 3rd party's signature (the CA) on both the client and server certificates. Once this is established, further checks are performed before the authentication is complete. For more details, see secure-computing's guide.

## Certificate Authority (CA)
For security purposes, it is recommended that the CA machine be separate from the machine running OpenVPN.

On the CA machine, install , initialize a new PKI and generate a CA keypair that will be used to sign certificates:

 # cd /root
 # export EASYRSA=/etc/easy-rsa
 # easyrsa init-pki
 # easyrsa build-ca

Starting from OpenVPN 2.4, one can also use elliptic curves for TLS connections (e.g. tls-cipher TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384). Elliptic curve cryptography provides more security and eliminates the need for a Diffie-Hellman parameters file. See and [https://www.maths.tcd.ie/~fionn/misc/ec_vpn.php.

Append the following lines to :

For elliptic curve:

or for Twisted Edwards curve:

Now set up PKI and generate a CA certificate:

 # cd /root
 # export EASYRSA=/etc/easy-rsa
 # export EASYRSA_VARS_FILE=/etc/easy-rsa/vars
 # easyrsa init-pki
 # easyrsa build-ca

## OpenVPN server files
A functional OpenVPN server requires the following:

# The CA's public certificate
# The Diffie-Hellman (DH) parameters file (required by TLS mode when not using TLS with elliptic curves).
# The server key pair (a public certificate and a private key).
# The Hash-based Message Authentication Code (HMAC) key.

Upon completing the steps outlined in this article, users will have generated the following files on the server:

#
#  (not when using TLS with elliptic curves)
#  and
#

## CA public certificate
The CA public certificate  generated in the previous step needs to be copied over to the machine that will be running OpenVPN.

On the CA machine:

 # scp /etc/easy-rsa/pki/ca.crt archie@hostname-of-openvpn-server:/tmp/ca.crt

On the OpenVPN server machine:

 # mv /tmp/ca.crt /etc/openvpn/server/
 # chown openvpn:network /etc/openvpn/server/ca.crt

## Server certificate and private key
On the OpenVPN server machine, install  and generate a key pair for the server:

 # cd /etc/easy-rsa
 # easyrsa init-pki
 # easyrsa gen-req servername nopass
 # cp /etc/easy-rsa/pki/private/servername.key /etc/openvpn/server/

This will create two files:

*
*

## Diffie-Hellman (DH) parameters file
On the OpenVPN server machine, create the initial dh.pem file:

 # openssl dhparam -out /etc/openvpn/server/dh.pem 2048

## Hash-based Message Authentication Code (HMAC) key
On the OpenVPN server machine, create the HMAC key:

 # openvpn --genkey secret /etc/openvpn/server/ta.key
 # chown openvpn:network /etc/openvpn/server/ta.key

If elliptic curve is used, the HMAC key is generated with the following command:
 # openvpn --genkey tls-auth /etc/openvpn/server/ta.key
 # chown openvpn:network /etc/openvpn/server/ta.key

This will be used to add an additional HMAC signature to all SSL/TLS handshake packets. In addition any UDP packet not having the correct HMAC signature will be immediately dropped, protecting against:

* Portscanning.
* DOS attacks on the OpenVPN UDP port.
* SSL/TLS handshake initiations from unauthorized machines.
* Any eventual buffer overflow vulnerabilities in the SSL/TLS implementation.

## OpenVPN client files
## Client certificate and private key
Any machine can generate client files provided that  is installed.

If the pki is not initialized, do so via:

 # cd /etc/easy-rsa
 # easyrsa init-pki

Generate the client key and certificate:

 # cd /etc/easy-rsa
 # easyrsa gen-req client1 nopass

This will create two files:

*
*

The gen-req set can be repeated as many times as needed for additional clients.

## Sign the certificates and pass them back to the server and clients
## Obtain and sign the certificates on the CA
The server and client(s) certificates need to be signed by the CA then transferred back to the OpenVPN server/client(s).

On the OpenVPN server (or the box used to generate the certificate/key pairs):

 # cp /etc/easy-rsa/pki/reqs/*.req /tmp
 # chown archie /tmp/*.req

Securely transfer the files to the CA machine for signing:

 $ scp /tmp/*.req archie@hostname-of-CA:/tmp

On the CA machine, import and sign the certificate requests:

 # cd /etc/easy-rsa
 # easyrsa import-req /tmp/servername.req servername
 # easyrsa import-req /tmp/client1.req client1
 # easyrsa sign-req server servername
 # easyrsa sign-req client client1

This will create the following signed certificates which can be transferred back to their respective machines:

*
*

The leftover .req files can be safely deleted:

 # rm -f /tmp/*.req

## Pass the signed certificates back to the server and client(s)
On the CA machine, copy the signed certificates and transfer them to the server/client(s):

 # cp /etc/easy-rsa/pki/issued/*.crt /tmp
 # chown archie /tmp/*.crt
 $ scp /tmp/*.crt archie@hostname-of-openvpn_server:/tmp

On the OpenVPN server, move the certificates in place and reassign ownership.
For the server:

 # mv /tmp/servername.crt /etc/openvpn/server/
 # chown openvpn:network /etc/openvpn/server/servername.crt

For the client:

 # mv /tmp/clientname.crt /etc/openvpn/client/
 # chown openvpn:network /etc/openvpn/client/clientname.crt

That is it. To generate the client profile. See: OpenVPN#ovpngen.

## Revoking certificates and alerting the OpenVPN server
## Revoke a certificate
Over time, it may become necessary to revoke a certificate thus denying access to the affected user(s). This example revokes the "client1" certificate.

On the CA machine:

 # cd /etc/easy-rsa
 # easyrsa revoke client1
 # easyrsa gen-crl

This will produce the CRL file  that needs to be transferred to the OpenVPN server and made active there.

## Alert the OpenVPN server
On the CA machine:

 # cp /etc/easy-rsa/pki/crl.pem /tmp
 # chown archie /tmp/crl.pem

On the OpenVPN machine, copy  and inform the server to read it:

 # mv /tmp/crl.pem /etc/openvpn/server/
 # chown openvpn:network /etc/openvpn/server/crl.pem

Edit  uncommenting the crl-verify directive, then restart openvpn-server@server.service to re-read it:

## Abbreviated example specifically for containerized Openvpn
This section is specifically for users wanting to run Openvpn in a Linux container (LXC). The code below is designed to be pasted into a root shell; the standard hash has been omitted to allow for easy copy/paste operations. It is recommended to have two different shell windows open, one for the host and one for the container.

On the host:

 CONTAINERNAME=foo
 /etc/easy-rsa
 easyrsa init-pki && easyrsa build-ca
 cp /etc/easy-rsa/pki/ca.crt /var/lib/lxc/$CONTAINERNAME/rootfs/etc/openvpn/server/

In the container:

 cd /etc/easy-rsa && easyrsa init-pki
 for i in server client; do easyrsa gen-req $i nopass; done
 cp /etc/easy-rsa/pki/private/server.key /etc/openvpn/server/
 openssl dhparam -out /etc/openvpn/server/dh.pem 2048
 openvpn --genkey secret /etc/openvpn/server/ta.key

Back on the host:

 easyrsa import-req /var/lib/lxc/$CONTAINERNAME/rootfs/etc/easy-rsa/pki/reqs/junk.req junk
 easyrsa import-req /var/lib/lxc/$CONTAINERNAME/rootfs/etc/easy-rsa/pki/reqs/client.req client
 easyrsa sign-req client client
 easyrsa sign-req server server
 mkdir /var/lib/lxc/$CONTAINERNAME/rootfs/etc/easy-rsa/pki/issued/
 mkdir /var/lib/lxc/$CONTAINERNAME/rootfs/etc/easy-rsa/pki/signed/
 cp /etc/easy-rsa/pki/issued/*.crt /var/lib/lxc/$CONTAINERNAME/rootfs/etc/easy-rsa/pki/issued/

That will provide the needed files to make an OpenVPN compatible tunnel profile for the client, and the needed server key files for the server. To generate a client profile, refer to OpenVPN#ovpngen.
