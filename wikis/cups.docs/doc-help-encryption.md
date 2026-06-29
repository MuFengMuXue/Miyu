# Managing Encryption

CUPS supports TLS encryption in two ways:

1.  Using HTTPS (always on) as soon as a connection is established, and
2.  Using HTTP Upgrade to TLS (opportunistic) after the connection is established.

CUPS supports self-signed, CA-signed, and enterprise certificates, with configurable certificate validation, cipher suite, and SSL/TLS version policies.

Out of the box, CUPS uses a Trust On First Use ("TOFU") certificate validation policy like the popular Secure Shell (ssh) software, requires TLS/1.0 or higher, only allows secure cipher suites, and automatically creates a "self-signed" certificate and private key for the scheduler so that remote administration operations and printer sharing are encrypted by default.

## Configuring Client TLS Policies

The [`client.conf`](man-client.conf.html) file controls the client TLS policies. The default policy is:

``` command
AllowAnyRoot Yes
AllowExpiredCerts No
Encryption IfRequested
SSLOptions None
TrustOnFirstUse Yes
ValidateCerts No
```

A client can be configured to only communicate with trusted TLS/1.1+ servers and printers by copying the corresponding certificates to the client ([see below](#PLATFORM)) and using the following policy in the `client.conf` file or macOS<sup>®</sup> printing preferences:

``` command
AllowAnyRoot No
AllowExpiredCerts No
Encryption Required
SSLOptions DenyTLS1.0
TrustOnFirstUse No
ValidateCerts Yes
```

Similarly, if a client needs to support an older server that only supports SSL/3.0 and RC4 cipher suites you can use the following policy option:

``` command
SSLOptions AllowRC4 AllowSSL3
```

## Configuring Server TLS Policies

Two directives in the [`cups-files.conf`](man-cups-files.conf.html) file control the server (scheduler) TLS policies - [`CreateSelfSignedCerts`](man-cups-files.conf.html#CreateSelfSignedCerts) and [`ServerKeychain`](man-cups-files.conf.html#ServerKeychain). The default policy creates self-signed certificates as needed.

The [`DefaultEncryption`](man-cupsd.conf.html#DefaultEncryption) and [`Encryption`](man-cupsd.conf.html#Encryption) directives in the [`cupsd.conf`](man-cupsd.conf.html) file control whether encryption is used. The default configuration requires encryption for remote access whenever authentication is required.

## Platform Differences

### macOS<sup>®</sup>

On macOS, client configuration settings for ordinary users are stored in the `$HOME/Library/Preferences/org.cups.PrintingPrefs.plist` file. System-wide and user certificates are stored in the system and login keychains, with private CUPS keychains being used for self-signed and CUPS-managed certificates.

### Windows<sup>®</sup>

On Windows, client configuration settings are controlled by the SSL/TLS Group Policy settings and certificate stores.

### Other Platforms

Other platforms only use the `client.conf` file and PEM-encoded certificates (*hostname*.crt) and private keys (*hostname*.key) in the `/etc/cups/ssl` and `$HOME/.cups/ssl` directories. If present, the `/etc/cups/ssl/site.crt` file defines a site-wide CA certificate that is used to validate server and printer certificates. Certificates for known servers and printers are stored by CUPS in the corresponding `ssl` directory so they can be validated for subsequent connections.

CUPS also supports certificates created and managed by the popular [Let's Encrypt](https://letsencrypt.org/) certificate service, which are stored in the `/etc/letsencrypt/live` directory.
