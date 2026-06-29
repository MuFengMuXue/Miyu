# Stunnel

stunnel (“Secure Tunnel”) is a
: cross-platform application used to provide a universal TLS/SSL tunneling service. It is a sort of a proxy designed to add TLS encryption functionality to existing clients and servers without any changes in the programs' code. It is designed for security, portability, and scalability (including load-balancing), making it suitable for large deployments. It uses OpenSSL, and is distributed under GNU GPL version 2 or later with OpenSSL exception.
Stunnel input can only be TCP packets. Its FAQ has some workarounds for UDP. WireGuard also has UDP capabilities. Conceptually, stunnel can be thought of as a generalization of HTTPS, or a lightweight tunnel. Basically, it just wraps/unwraps the data within TLS/SSL. It can be used with traditional network interfaces and TCP/IP stack.

Authentication can also be used by the server to allow access only to approved clients.

## Installation
Install the  package.

Depending on your usage, you might also need to edit the provided systemd units to better handle dependencies. In order for stunnel to start up automatically at system boot you must enable it.

## Configuration
The main configuration file is read from . It is an ini-style file. It is composed from a global section followed by one or more service sections.

A client is one to accept non-TLS encrypted data. Stunnel will encrypt its data with TLS and connect to the stunnel server. The stunnel server accepts TLS encrypted data and decrypts it. It then connects to where the data should be sent to.

The default  value is , which is very verbose. After verifying correct operation, it is worth to explicitly set a lower value in the configuration file.

For better security, it is advised to explicitly set an appropriate uid and gid, other than root, for the global section and the per service sections. The configuration tokens  and  are available for this purpose.

## Byte order mark (BOM)
The configuration file should have a UTF-8 byte order mark (BOM), at the beginning of the file. A BOM is the unicode character U+FEFF. Its UTF-8 representation is the (hexadecimal) byte sequence 0xEF, 0xBB, 0xBF. Creating a file with these bytes at its beginning can be done by

 # echo -e '\xef\xbb\xbf; BOM composed of non printable characters. It is here, before the semicolon!' > /etc/stunnel/stunnel.conf

To test if those bytes appear, one can use

Note that when printing the file to the screen, such as with , or when editing the file with a text editor, the BOM bytes are usually not displayed. They should be there, though. Which is why, after editing is completed, you might want to verify that they are still there with the above  or similar command.

## Pre-shared key
At least one of the client and the server, and optionally both, should be authenticated. Either a pre-shared secret or a key and certificate pair can be used for authentication. A pre-shared secret has to be transferred to all involved machines beforehand by other means, such as SCP and SFTP. When such transfer is acceptable, pre-shared key is the fastest method. Its speed might help to mitigate attacks. A simple configuration for a single server with a single client that are using a pre-shared secret is:

Client:

Server:

where  could be created on one machine by

 # openssl rand -base64 -out /etc/stunnel/psk.txt 180
 # sed --in-place --null-data 's/\n//g;1s/^/psk:/' /etc/stunnel/psk.txt
 # chmod 640 /etc/stunnel/psk.txt

and copied to the other machine by secure means before starting stunnel. The permissions for each  file should be set appropriately, neither world-readable nor world-writable. The psk string from the  command is just a random name for the sake of the example. Do read .

## Certificates
Per the upstream examples, such as those in , there  is an option to get stunnel to run with certificates. With proper stunnel configurations, the certificates used need not be trusted by the system. However, when the certificates chain is not trusted by the system, the clients and optionally the server must approve it before using it, for example, by holding a copy of the whole chain including the root certificates.

Following is an example to allow only a limited number of clients to actually use the traditional TCP version of the echo service. In this example, even if the external TCP port of the echo server on port 12345 portrayed here is open to anyone, the server will deny any client whose certificates it does not have. In effect, with such usage of certificates, the clients' certificates effectively act like pre-shared secrets.

Client:

Server:

The required certificates can be generated as self-signed certificates. For example, by

 # openssl req -new -x509 -subj "/C=GB/ST=LONDON/O=TOWER OF LONDON/CN=DOMAINS" -key <(openssl genpkey -algorithm ED448) -noenc -days 365 -out server_req.pem -keyout server_key.pem

And a similar command can be used to generate the certificate for each client. When it is acceptable for all the clients to share a single certificate, this reduces to

 # openssl req -new -x509 -subj "/C=CA/ST=ONTARIO/O=TOWER OF LONDON ASSOCIATION/CN=CA BRANCH" -key <(openssl genpkey -algorithm ED448) -noenc -days 365 -out clients_req.pem -keyout clients_key.pem

Test it:

 $ echo traditional echo protocol | ncat ::1 54321
 traditional echo protocol
