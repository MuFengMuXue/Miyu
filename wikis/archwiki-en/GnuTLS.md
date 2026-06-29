# GnuTLS

According to Wikipedia:
:GnuTLS (the GNU Transport Layer Security Library) is a free software implementation of the TLS, SSL and DTLS protocols. It offers an application programming interface (API) for applications to enable secure communication over the network transport layer, as well as interfaces to access X.509, PKCS #12 and other structures.

## Installation
Install the  package.

For integration with the Apache HTTP Server install mod_gnutls.

## Usage
See  for the command used in the following sections and the info document for the API documentation.

## Generate a private key
 $ certtool --generate-privkey --outfile private_key

## Generate a certificate signing request
 $ certtool --generate-request --load-privkey private_key --outfile file

## Generate a self-signed certificate
 $ certtool --generate-self-signed --load-privkey private_key --outfile file

## Inspect a certificate
 $ certtool --certificate-info --infile file
