# OpenPGP

OpenPGP is an open standard for cryptographic operations. It is a system based on well-understood cryptographic building blocks. OpenPGP supports the secure delivery of files and messages between a sender and a recipient. It also addresses identities and their verification.

## Software
## Applications
A number of e-mail clients implement OpenPGP features, such as Thunderbird.

General-purpose OpenPGP commandline tools include  and .

## Stateless OpenPGP (SOP)
Stateless OpenPGP defines a generic stateless command-line interface for dealing with OpenPGP messages, known as SOP. It aims for a minimal, well-structured API covering OpenPGP object security.

For many use-cases SOP offers all required functionality and can be used as a vendor-agnostic, stand-alone alternative to tools such as GnuPG (see the dedicated IETF draft for details).

Many SOP implementations exist and are cross-tested in an interoperability test suite.

## Libraries
A number of libraries exist for various programming languages.

## Hardware security device support
OpenPGP private keys can be securely handled on specialized hardware devices. The OpenPGP card standard defines a smart card application for this purpose. This standard is implemented on many devices, including most models of Nitrokey and YubiKey.

Users can use these smartcards with software such as GnuPG or OpenPGP-card-tools.

## Standardization
The standardization of OpenPGP takes place in the context of the IETF OpenPGP working group.

The most recent and widely adopted IETF ratified standard for OpenPGP is RFC 9580.
This standard defines formats of what is colloquially referred to as "OpenPGP version 4", as well as the new "OpenPGP version 6" format.
RFC 9580 specifies the use of modern cryptographic mechanisms following best practices, including AEAD.

Future work will center around topics such as post-quantum cryptography (PQC) and forward secrecy (see Charter 04 of the IETF OpenPGP working group for details).

## PGP Public Key Infrastructure
The OpenPGP ecosystem has developed several mechanisms to deal with public keys.
This public key infrastructure (aka PGPKI) deals with two separate concerns:

* the distribution and retrieval of certificates for communication peers
* the authentication of identities in certificates

To communicate with a peer, a copy of the peer's certificate is needed. Obtaining a copy can be achieved with one of the distribution models described in the following sections (see #Keyserver and #Web Key Directory).

An OpenPGP certificate contains identity claims. Since OpenPGP is a decentralized system with no central authorities, identity claims are issued by the certificate holder and can be independently verified.
Depending on the threat model, different methods of identity verification (aka authentication) are appropriate.

For some low-risk purposes it may be acceptable to ignore authentication and rely on trust on first use (TOFU).

A slightly higher level of assurance of authenticity is achieved by relying on validating keyservers or Web Key Directory.

One of the highest levels of authenticity assurance can be achieved by explicit authentication, for example by manually verifying the OpenPGP fingerprint of a certificate.

## Keyserver
Key server implementations of the OpenPGP HTTP Keyserver Protocol offer varying feature sets while providing users access to OpenPGP certificates.

Some keyserver instances synchronize OpenPGP certificates amongst each other, forming a pool of hosts that serve the same key material.

Most keyservers accept OpenPGP certificates without authentication or validation. However, some newer implementations enforce the validation of User IDs by sending a verification e-mail to addresses connected to an uploaded certificate.

All keyservers in the below table are GDPR compliant, as they provide a necessary public service for the ecosystem, allow the removal of personal data and/ or enforce opt-in of its publication.

Third-party identity certifications are not distributed by all keyservers.

{| class="wikitable"
|+ OpenPGP keyservers
! Host !! Synchronizing !! Validating !! Identity certifications !! Software
|-
| https://keys.openpgp.org ||  ||  ||  || Hagrid
|-
| https://pgpkeys.eu/ ||  ||  ||  || Hockeypuck
|-
| https://keyserver.ubuntu.com/ ||  ||  ||  || Hockeypuck
|-
| https://keys.mailvelope.com/ ||  ||  ||  || Mailvelope Keyserver
|}

## Web Key Directory
Web Key Directory (WKD) is a mechanism to distribute OpenPGP certificates for a given domain based on well-known URIs.

With WKD a web server provides access to a well-known directory structure with normalized file names which allows lookup by e-mail address.

According to GnuPG's wiki this mechanism is supported by several mail hosting providers.

A WKD directory structure can be created from an OpenPGP public keyring and exposed by a web server.
The setup can be checked for correctness using https://wkd.dp42.dev/.

## Explicit Authentication
Explicit authentication may mean manually verifying the OpenPGP fingerprints of a certificate with its owner over a secure channel (e.g. in person).

A variation on explicit authentication is the Web of Trust, which encodes manual authentication as machine readable artifacts: OpenPGP certifications (aka signatures).
Both direct certifications as well as indirect paths using delegation via trusted introducers can be modeled.

On Arch Linux a set of main signing keys acts as trust anchor for the project. These keys are used to certify the OpenPGP certificates of all package maintainers and developers.
Anyone is able to verify the authenticity of each packager by relying on the main signing keys as trust anchors.
For Arch Linux users this can be achieved by installing  and using .

Alternatively, the OpenPGP fingerprints of the main signing keys can be manually configured as trust anchors by any OpenPGP user, e.g. after verifying them on https://archlinux.org/master-keys/.
All relevant certificates can be obtained either through Arch Linux's own web key directory, releases of the archlinux-keyring project or from keyservers.

## Usage examples
