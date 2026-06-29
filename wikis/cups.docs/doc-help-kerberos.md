# Using Kerberos Authentication

CUPS allows you to use a Key Distribution Center (KDC) for authentication on your local CUPS server and when printing to a remote authenticated queue. This document describes how to configure CUPS to use Kerberos authentication and provides links to the MIT help pages for configuring Kerberos on your systems and network.

> **Note:** Kerberos authentication is deprecated starting in CUPS 2.4.0. OAuth 2.0 is the recommended SSO replacement.

## System Requirements

The following are required to use Kerberos with CUPS:

1.  Heimdal Kerberos (any version) or MIT Kerberos (1.6.3 or newer)
2.  Properly configured Domain Name System (DNS) infrastructure (for your servers):
    1.  DNS server(s) with static IP addresses for all CUPS servers or configured to allow DHCP updates to the host addresses and
    2.  All CUPS clients and servers configured to use the same DNS server(s).
3.  Properly configured Kerberos infrastructure:
    1.  KDC configured to allow CUPS servers to obtain Service Granting Tickets (SGTs) for the "host" and "HTTP" services/principals,
    2.  LDAP-based user accounts - both OpenDirectory and ActiveDirectory provide this with the KDC, and
    3.  CUPS clients and servers bound to the same KDC and LDAP server(s).

## Configuring Kerberos on Your System

Before you can use Kerberos with CUPS, you will need to configure Kerberos on your system and setup a system as a KDC. Because this configuration is highly system and site-specific, please consult the following on-line resources provided by the creators of Kerberos at the Massachusetts Institute of Technology (MIT):

- <a href="http://web.mit.edu/kerberos/" target="_blank">Kerberos: The Network Authentication Protocol</a>
- <a href="http://web.mit.edu/macdev/KfM/Common/Documentation/faq-osx.html" target="_blank">Kerberos on macOS Frequently Asked Questions</a>

The Linux Documentation Project also has a HOWTO on Kerberos:

- <a href="http://tldp.org/HOWTO/html_single/Kerberos-Infrastructure-HOWTO/" target="_blank">Kerberos Infrastructure HOWTO</a>

## Configuring CUPS to Use Kerberos

Once you have configured Kerberos on your system(s), you can then enable Kerberos authentication by selecting the `Negotiate` authentication type. The simplest way to do this is using the `cupsctl(8)` command on your server(s):

``` command
cupsctl DefaultAuthType=Negotiate
```

You can also enable Kerberos from the web interface by checking the `Use Kerberos Authentication` box and clicking `Change Settings`:

``` command
https://server.example.com:631/admin
```

After you have enabled Kerberos authentication, use the built-in "authenticated" policy or your own custom policies with the printers you will be sharing. See [Managing Operation Policies](policies.html) for more information.

## Implementation Information

CUPS implements Kerberos over HTTP using GSSAPI and the service/principal names "host/server.example.com" for command-line access and "HTTP/server.example.com" for web-based access, where "server.example.com" is replaced by your CUPS server's hostname. Because of limitations in the HTTP GSSAPI protocol extension, only a single domain/KDC is supported for authentication. The (experimental) HTTP extension is described in [RFC 4559](http://tools.ietf.org/html/rfc4559).

When doing printing tasks that require authentication, CUPS requests single-use "tickets" from your login session to authenticate who you are. These tickets give CUPS a username of the form "user@REALM", which is then truncated to just "user" for purposes of user and group checks.

In order to support printing to a shared printer, CUPS runs the IPP or SMB backend as the owner of the print job so it can obtain the necessary credentials when the job is de-spooled to the server.
