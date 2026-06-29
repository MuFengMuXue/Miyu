# Transport Layer Security

According to Wikipedia:
:Transport Layer Security (TLS), and its now-deprecated predecessor, Secure Sockets Layer (SSL), are cryptographic protocols designed to provide communications security over a computer network. Several versions of the protocols find widespread use in applications such as web browsing, email, instant messaging, and voice over IP (VoIP). Websites can use TLS to secure all communications between their servers and web browsers.

## Implementations
There are multiple TLS implementations available. OpenSSL should already be installed on your system as it is an indirect dependency of the  meta package ( >  > ). GnuTLS might already be installed on your system as it is required by many packages.

*
*
*
*
*

## Certificate authorities
With TLS one of a set of certificate authorities (CAs) checks and signs for the authenticity of a public key certificate from a server. A client connecting to the server via TLS may verify its certificate's authenticity by relying on a digital signature of CA. To check the digital signature a client must have a public key of CA, obtained via a separate path and stored as a self-signed certificate. On Arch Linux the default set of CA certificates is provided by the  package.

Arch Linux provides a centralized system-wide interface for managing CA certificates. This interface is the library  from the  package, which provides PKCS #11 API for certificates, stored in  (the token "Default Trust") and  (the token "System Trust").

For using the interface from a command line, the  package provides the  utility.

For libraries, that have not been ported to PKCS #11 and use a custom logic for managing CA certificates, the package  provides the  script. It copies CA certificates obtained through the centralized interface to  and .

## An overview of mechanisms for loading a default set of CA certificates
{| class="wikitable"
! Implementation !! Mechanism !! Arch Linux configuration
|-
| OpenSSL
| Provides API functions that load the certificates from a hardcoded directory or file. .
| A default file is , a default directory is .
|-
| GnuTLS
| Provides an API function that loads the certificates from a hardcoded directory, file, or configured PKCS #11 modules. In the last case, a hardcoded URL allows to load either an arbitrary trusted certificate, or trusted CA certificates on modules, marked with , optionally with additional filtration criteria. [https://gnutls.org/reference/gnutls-gnutls.html#gnutls-certificate-set-x509-system-trust.
| Loads all trusted CA certificates from configured PKCS #11 modules, marked with .
|-
| Network Security Services
| Automatically loads the certificates from a dynamically configured list of PKCS #11 modules, managed with a dedicated API. Configuration can be stored in any directory, pointed by a user. The list always contains the built-in module that stores objects in the same user-provided directory. .
|
|-
| mbed TLS
| A user should load the certificates. [https://tls.mbed.org/kb/how-to/mbedtls-tutorial.
|
|-
| LibreSSL
| Provides an API function that loads the certificates from a hardcoded directory or file. .
| A default file is , a default directory is .
|}

## Trust management
For trust management the  utility is provided. The utility operates on a list of PKCS #11 modules with the  setting, sorted by the  setting. See  for details about configuration of modules.

## List trust store items
 $ trust list

## Add a certificate to a trust store
 # trust anchor certificate.crt

The certificate should be in the persistence, DER or PEM format (including the OpenSSL-specific trusted certificate format). This command stores the certificate in the first writable token found by querying the list of modules.

## Remove a certificate from a trust store
 $ trust anchor --remove 'pkcs11:id=%00%11%22%33%44%55%66%77%88%99%AA%BB%CC%DD%EE%FF%00%11%22%33;type=cert'

## Override default trust
The default trust store  includes a blocklist directory at  and certificates in it will be treated as distrusted for all purposes.

The token representing certificates in  is always write-protected. To distrust a default certificate authority it can be extracted to the system's blocklist:

 $ trust extract --format=pem-bundle --filter='pkcs11:id=%00%11%22%33%44%55%66%77%88%99%AA%BB%CC%DD%EE%FF%00%11%22%33;type=cert' /etc/ca-certificates/trust-source/blocklist/untrusted_authority.pem

Alternatively, an already extracted certificate may also be copied to the blocklist from the  path. See  for further information.

## Obtaining a certificate
The first step is to generate a private key. Before generating the key, set a restrictive file mode creation mask with umask (for example ). This ensures that the keys written by openssl are read-protected.

Keys can use either elliptic curve or RSA algorithms.

Elliptic curves are newer algorithms and are becoming increasingly adopted for modern systems. A 256-bit elliptic curve key is expected to provide sufficient security through the year 2030 Curve25519 is an elliptic curve algorithm which has good security and performance properties.

RSA is an older cryptosystem and has higher compatibility, especially with clients that do not support recent versions of TLS. However, RSA relies on factorization, which is an area of cryptography which may be becoming weaker due to the development  of faster factorization algorithms [https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/.  A 2048-bit RSA private key is expected to provide security through most of the 2020s A 4096-bit RSA private key is expected to provide security for longer (barring major advancements in factorization), but has a very large performance impact. The performance difference can be benchmarked with  [https://webmasters.stackexchange.com/questions/84838/performance-4096-bit-rsa-key-compared-to-2048-bit-rsa-key.

After the key is generated, a certificate can be obtained from a certificate authority with a Certificate Signing Request (CSR), or a certificate may be self-signed. While self-signed certificates can be generated easily, clients will reject them by default, meaning that every client needs to be configured to trust the self-signed certificate.

For the actual generation commands refer to the article of the used implementation:

* OpenSSL#Usage
* GnuTLS#Usage
* Network Security Services#Usage
* mbed TLS#Usage

## Server-side recommendations
Because there are various attacks against TLS the best practices should be considered:

* Disable SSLv3 to prevent the POODLE attack.
* weakdh.org's Guide to Deploying Diffie-Hellman for TLS
* Mozilla's Server Side TLS article
* SSL Labs' SSL and TLS Deployment Best Practices
* Recommended TLS/SSL configurations for popular services

## Checking TLS
Programs to check TLS:

*
* Nmap
* OpenSSL
* cipherscan

Websites to check TLS:

* https://dev.ssllabs.com/ssltest/ (only HTTPS)
* https://www.checktls.com/ (only email)
* https://www.immuniweb.com/ssl/ (any port)
* https://tls.imirhil.fr/tls (any port)

## Miscellaneous
## ACME clients
The Automated Certificate Management Environment (ACME) protocol lets you request valid X.509 certificates from certificate authorities, like Let's Encrypt.

See also List of ACME clients.

*
*
*
*
*
*
*
*
*
*
*

## OCSP
The Online Certificate Status Protocol (OCSP) is supported by Firefox. Chromium has its own mechanismSee also  by GnuTLS and  by OpenSSL.

## HSTS
The HTTP Strict Transport Security (HSTS) mechanism is supported by Firefox, Chromium and wget ().

## DNS CAA
See Wikipedia:DNS Certification Authority Authorization.
