# OpenSSL

OpenSSL is an open-source implementation of the SSL and TLS protocols, designed to be as flexible as possible. It is supported on a variety of platforms, including BSD, Linux, OpenVMS, Solaris and Windows.

## Installation
 is installed by default on Arch Linux (as a dependency of ).

There are various OpenSSL library bindings available for developers:

*
*
* , ,
*
*

## Configuration
On Arch Linux the  is .

The OpenSSL configuration file, conventionally placed in , may appear complicated at first. Remember that variables may be expanded in assignments, much like how shell scripts work. For a thorough explanation of the configuration file format, see .

## req section
Settings related to generating keys, requests and self-signed certificates.

The req section is responsible for the DN prompts. A general misconception is the Common Name (CN) prompt, which suggests that it should have the user's proper name as a value. End-user certificates need to have the machine hostname as CN, whereas CA should not have a valid TLD, so that there is no chance that, between the possible combinations of certified end-users' CN and the CA certificate's, there is a match that could be misinterpreted by some software as meaning that the end-user certificate is self-signed. Some CA certificates do not even have a CN, for example:

## Usage
This sections assumes you have read Transport Layer Security#Obtaining a certificate.

## Generate an Ed25519 private key
 $ openssl genpkey -algorithm ed25519 -out filename

## Generate a Curve25519 private key
 $ openssl genpkey -algorithm x25519 -out filename

## Generate an ECDSA private key
 $ openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out filename

## Generate an RSA private key
With , which supersedes genrsa according to :

 $ openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:keysize -out filename

If an encrypted key is desired, use the  option.

## Generate a certificate signing request
Use :

 $ openssl req -new -sha256 -key private_key -out filename

## Show a certificate signing request
Certificate signing requests are stored in an encoded format. To view the request in human readable format:

 $ openssl req -noout -text -in filename

## Generate a self-signed certificate
 $ openssl req -key private_key -x509 -new -days days -out filename

## Generate a self-signed certificate with private key in a single command
You can combine the above command in OpenSSL into a single command which might be convenient in some cases.

ECDSA:

 $ openssl req -x509 -newkey ec -pkeyopt 'ec_paramgen_curve:P-256' -days days -keyout key_filename -out cert_filename

RSA:

 $ openssl req -x509 -newkey rsa:4096 -days days -keyout key_filename -out cert_filename

## Sign a certificate signing request with a CA certificate
 $ openssl x509 -req -in cert_req_filename -days days -CA CA_cert -CAkey CA_cert_private_key -CAserial CA_cert_serial_file -out cert_out

## Generate Diffie–Hellman parameters
DH, Diffie–Hellman, key exchange is a protocol to negotiate a shared secret between two parties, where the negotiation itself is held securely over public networks. (Wikipedia article). The resulted shared secret can be used for secret communication for exchanging data over a public network. The DH protocol establishes a method for both parties to contribute to the eventual shared secret by communicating over public networks in a way a passive listener will not be able to reconstruct the resulted shared secret. The other common way to achieve a shared secret by communicating over public networks is have one party use some long-term asymmetric key to encrypt the secret and send it to the owner of the key (like in an RSA key exchange)Other algorithms are consequently used for encryption itself[https://stackoverflow.com/a/58221273. In order to set demands that will be raised while negotiating, each party can a priory define a set of demands. These demands are the Diffie–Hellman parameters. The common way to define these parameters is by mathematical functions. There are two functions commonly used:  exponentiation modulo prime (forming Finite Field Diffie-Hellman, or FFDH) and point multiplication over elliptic curve, forming Elliptic Curve Diffie-Hellman (ECDH).

Current best practice is to use one of the standard DH groups from RFC:7919, eg. ffdhe2048.

Alternatively you can generate a random group of your own:

 $ openssl dhparam -out filename 2048

## Show certificate information
 $ openssl x509 -text -in cert_filename

To view a server's certificate, use :

 $ openssl s_client -showcerts -connect hostname:port </dev/null | openssl x509 -text

## Show certificate fingerprint
 $ openssl x509 -noout -in cert_filename -fingerprint -digest

 is optional and one of , , , or . See "-digest" in  for when the digest is unspecified.

## Convert certificate format
Use  to convert certificates from binary (DER) format to PEM format (the text format with  headers)：

 $ openssl x509 -inform DER -in myCA.crt -out myCA_pem.crt

## Use third-party providers
OpenSSL 3 introduced providers as a new concept for OpenSSL plugability. It is possible to use algorithms not included in OpenSSL without having to recompile it.

## oqsprovider
To test the NIST Post-Quantum Cryptography algorithms, you can install the Open Quantum Safe provider . As an example, you can generate a quantum-safe self-signed certificate with private key using one of the variants of ML-DSA (formerly CRYSTALS-Dilithium):

 $ openssl req -provider default -provider oqsprovider -x509 -newkey mldsa65 -days days -keyout key -out cert

## tpm2-openssl
To store ECDSA and RSA private keys in the TPM, install . See its README for documentation on how to use it.

## Troubleshooting
## "bad decrypt" while decrypting
OpenSSL 1.1.0 changed the default digest algorithm for the dgst and enc commands from MD5 to SHA256. Therefore if a file has been encrypted using OpenSSL 1.0.2 or older, trying to decrypt it with an up to date version may result in an error like:

 error:06065064:digital envelope routines:EVP_DecryptFinal_ex:bad decrypt:crypto/evp/evp_enc.c:540

Supplying the  option should solve the issue:

 $ openssl enc -d -md md5 -in encrypted -out decrypted

## Python 3.10 and "ca md too weak" errors
In Python 3.10 by default there is a hardcoded list of allowed OpenSSL ciphers. Some of the less secure, like MD5, have been disabled at the  module level, ignoring the system-wide configuration of OpenSSL. It results sometimes in strange errors on older certificates, sometimes even when establishing  connections, like:

 requests.exceptions.SSLError: HTTPSConnectionPool(host='a.kind.of.example.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(398, '[SSL: CA_MD_TOO_WEAK ca md too weak (_ssl.c:3862)')))

To make Python follow the system configuration, you may have to rebuild it, adding  parameter to . The issue has been also reported as .

## Error setting cipher XXX
If you try to use a "retired" cipher, you'll get an error of this type:

 $ openssl bf -d -in cipher_file -K passphrase
 Error setting cipher BF-CBC
 4087A97A8A7F0000:error:0308010C:digital envelope routines:inner_evp_generic_fetch:unsupported:crypto/evp/evp_fetch.c:341:Global default library context, Algorithm (BF-CBC : 12)

Since OpenSSL 3.0, crypto algorithms are supplied through "providers". Oldest or least used algorithms belong to the legacy provider. If you need to use retired algorithms like DES, RC4, Blowfish, etc., you must add the option  in your command line.

Here is a complete example for decoding a Blowfish cipher.
 $ openssl bf -d -in cipher_file -provider legacy -provider default -K passphrase
