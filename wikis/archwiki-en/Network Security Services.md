# Network Security Services

Network Security Services (NSS) is a set of libraries designed to support cross-platform development of security-enabled client and server applications.

Applications built with NSS can support SSL v2 and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3 certificates, and other security standards.

NSS is required by many packages, including, for example, Chromium and Firefox.

## Installation
Install the  package.

## Usage
NSS is implemented in terms of operations on a dynamically configured list of PKCS #11 modules. Each module provides access to tokens, which can execute cryptographic operations and store cryptographic objects. The configured list of modules is usually stored in an arbitrary directory, provided by a user at initialization of NSS, in the file . The list always contains a built-in module "NSS Internal PKCS #11 Module" with tokens "NSS Generic Crypto Services" and "NSS Certificate DB". The first token provides cryptographic mechanisms such as RSA, SHA256, TLS etc. The second token stores certificates and private keys in the same user-provided directory in the files  and . The files ,  and  are also called "NSS databases". Paths to NSS databases for some applications are listed in the table below. You should provide some path for each operation. Examples below will use .

{| class="wikitable"
! Application !! Path to NSS databases
|-
| ,
|
|-
|
|
|-
|
|
|-
|
| configurable via Options |}

For managing PKCS #11 modules NSS provides the  utility, for managing certificates and private keys — the  utility.

## List certificate DB
To get list of all certificates:

 $ certutil -d ~/.pki/nssdb/ -L

To get details about certificate:

 $ certutil -d ~/.pki/nssdb/ -L -n certificate_nickname

## Generate an RSA private key
 $ certutil -d ~/.pki/nssdb/ -G -g keysize -n nickname

## Generate a certificate signing request
 $ certutil -d ~/.pki/nssdb/ -R -k key-id -s subject -o file

## Generate a self-signed certificate
 $ certutil -d ~/.pki/nssdb/ -S -s subject -n nickname -x -t C,C,C -o file

## Generate a self-signed certificate with the assistance of OpenSSL
Using OpenSSL allows you to have an interactive prompt that's easier to format than using the certutil subject format. Instructions below were adapted from [https://serverfault.com/questions/831394/how-can-i-create-a-pkcs12-file-using-openssl-self-signed-certs and Create a key pair and a certificate (-noenc disables encryption of a private key with a password):
 $ openssl req -x509 -newkey rsa:4096 -keyout myKey.pem -out cert.pem -days 365 -noenc
Create a pkcs12 file:
 $ openssl pkcs12 -export -out keyStore.p12 -inkey myKey.pem -in cert.pem
Create NSS databases if they do not exist yet:
 $ certutil -d ~/.pki/nssdb -N --empty-password
Import your key to the database:
 $ pk12util -d ~/.pki/nssdb -i keyStore.p12

## Import certificate
To add a certificate specify the  option:

 $ certutil -d ~/.pki/nssdb/ -A -t "TRUSTARGS" -n certificate_nickname -i /path/to/cert/filename

The  are three strings of zero or more alphabetic characters, separated by commas, for example: . They define how the certificate should be trusted for SSL, email, and object signing, and are explained in the  manual or [https://meenavyas.medium.com/about-trust-flags-of-certificates-in-nss-database-that-can-be-modified-by-certutil-67e4f33a6d0f Meena's blog post on trust flags.

To add a personal certificate and private key for SSL client authentication use the command:

 $ pk12util -d ~/.pki/nssdb/ -i /path/to/PKCS12/cert/filename.p12

This will import a personal certificate and private key stored in a PKCS #12 file. The  of the personal certificate will be set to .

## Edit certificate
Call certutil with  option to edit the certificate. For example, to edit the :

 $ certutil -d ~/.pki/nssdb/ -M -t "TRUSTARGS" -n certificate_nickname

## Delete certificate
Use  option to remove the certificate:

 $ certutil -d ~/.pki/nssdb/ -D -n certificate_nickname

## Adding a trusted CA certificate
A system-wide trust store  is usually automatically added to the list of PKCS #11 modules. See Transport Layer Security#Trust management for system-wide configuration. For application-specific configuration use such a command to add a CA certificate:

 certutil -d ~/.pki/nssdb/ -A -i /path/to/certificate -n certificate_nickname -t C,,
