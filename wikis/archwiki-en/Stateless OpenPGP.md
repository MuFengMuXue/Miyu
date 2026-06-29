# Stateless OpenPGP

Stateless OpenPGP (SOP) is a standard for command line interface (CLI) tools to perform OpenPGP operations. It is defined in a dedicated IETF draft outlining its features and syntax.

SOP is a lean approach to signing/verification and encryption/decryption operations on messages. Certificates and/or keys for all operations must be explicitly specified.

Usually private key operations use software keys. However, private key material on hardware security devices can also be used with some SOP implementations.

Many SOP implementations exist and are cross-tested in an interoperability test suite.

Although implementations provide executables of differing names, they all have the same CLI and the core functionality can be used interchangeably.

## Installation
Several implementations are available for installation:

*
*
*
*

## Features
While SOP offers a uniform interface, implementations are free to support different subsets of the cryptographic mechanisms that OpenPGP specifies. Different versions of the format as well as hardware backed keys may be supported.

{| class="wikitable"
|+ Stateless OpenPGP implementations
! Package !! RFC 4880 (+ RFC 6637) !! draft-koch-librepgp !! RFC 9580 !! Hardware backed keys
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|}

## Hardware device support
When using hardware security devices, SOP parameters that usually specify private key material instead only specify public key material.

This public key material serves as an explicit reference to locate and use a hardware device that provides the corresponding private key material.

## Tips and tricks
The below examples assume, that the name of the SOP executable (e.g. gosop, rsop, rsop-oct or sqop) is stored in the environment variable .

## Create a private key
To create an OpenPGP transferable secret key (aka. private key) with the User ID  use:

 $ $SOP generate-key "" > archie.tsk

## Extract certificate
To extract the certificate (aka. public key) from the created transferable secret key use:

 $ $SOP extract-cert > archie.cert  msg.sig

## Verify detached signature
To verify the detached signature, provide the original message, the signature as well as the OpenPGP certificate:

## Encrypt a message
Messages can be encrypted by providing the message and the OpenPGP certificate of the recipient:

 $ echo "Hello world" | $SOP encrypt archie.cert > encrypted.msg

## Decrypt a message
Recipients of encrypted messages can decrypt them by providing the encrypted message and their transferable secret key:

## Create cleartext signed message
Cleartext signed messages can be created by providing the message and the signer's transferable secret key:
