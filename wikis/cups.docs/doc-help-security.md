# Server Security

In the default "standalone" configuration, there are few potential security risks - the CUPS server does not accept remote connections, and only accepts shared printer information from the local subnet. When you share printers and/or enable remote administration, you expose your system to potential unauthorized access. This help page provides an analysis of possible CUPS security concerns and describes how to better secure your server.

## Authentication Issues

When you enable remote administration, the server will use Basic authentication for administration tasks. The current CUPS server supports Basic, Kerberos, and local certificate authentication:

1.  Basic authentication essentially places the clear text of the username and password on the network.

    Since CUPS uses the system username and password account information, the authentication information could be used to gain access to possibly privileged accounts on the server.

    **Recommendation:** Enable encryption to hide the username and password information - this is the default on macOS and systems with GNU TLS installed.

2.  Local certificate authentication passes 128-bit "certificates" that identify an authenticated user. Certificates are created on-the-fly from random data and stored in files under `/var/run/cups/certs`. They have restricted read permissions: root + system-group(s) for the root certificate, and lp + lp for CGI certificates.

    Because certificates are only available on the local system, the CUPS server does not accept local authentication unless the client is connected to the loopback interface (127.0.0.1 or ::1) or domain socket.

    **Recommendation:** Ensure that unauthorized users are not added to the system group(s).

## Denial of Service Attacks

When printer sharing or remote administration is enabled, the CUPS server, like all Internet services, is vulnerable to a variety of denial of service attacks:

1.  Establishing multiple connections to the server until the server will accept no more.

    This cannot be protected against by any known software. The `MaxClientsPerHost` directive can be used to configure CUPS to limit the number of connections allowed from a single host, however that does not prevent a distributed attack.

    **Recommendation:** Limit access to trusted systems and networks.

2.  Repeatedly opening and closing connections to the server as fast as possible.

    There is no easy way of protecting against this in the CUPS software. If the attack is coming from outside the local network, it may be possible to filter such an attack. However, once the connection request has been received by the server it must at least accept the connection to find out who is connecting.

    **Recommendation:** None.

3.  Sending partial IPP requests; specifically, sending part of an attribute value and then stopping transmission.

    The current code will wait up to 1 second before timing out the partial value and closing the connection. This will slow the server responses to valid requests and may lead to dropped browsing packets, but will otherwise not affect the operation of the server.

    **Recommendation:** Block IPP packets from foreign or untrusted networks using a router or firewall.

4.  Sending large/long print jobs to printers, preventing other users from printing.

    There are limited facilities for protecting against large print jobs (the `MaxRequestSize` attribute), however this will not protect printers from malicious users and print files that generate hundreds or thousands of pages.

    **Recommendation:** Restrict printer access to known hosts or networks, and add user-level access controls as needed for expensive printers.

## Encryption Issues

CUPS supports 128-bit TLS encryption of network connections via the GNU TLS library, macOS Security framework, and Windows Schannel APIs. Secure deployment of TLS depends on proper certificate management and software maintenance.
