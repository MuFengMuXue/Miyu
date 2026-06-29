# Sequoia PGP

Sequoia PGP is a complete implementation of OpenPGP as defined by the (deprecated)  RFC 4880 and the new RFC 9580, and various related standards.

Sequoia consists also of several crates, providing both a low-level and a higher-level API for dealing with OpenPGP data. Moreover, Sequoia provides a detailed implementation of its Web of Trust which may be different (but largely compatible) from the one implemented by other tools like GnuPG, because OpenPGP does not specify how a web of trust implementation should work.

## Installation
You should install the  package, and optionally  for the Stateless OpenPGP implementation of Sequoia.

## Configuration
Configuration file is a TOML formatted file placed at one of the following locations:
*  if  environment variable is set;
*  if  is not set or it is set to .

You can query, inspect, and create the configuration file through the  subcommand. The  command for example generates on stdout a configuration template with all the keys, which you can customize to fit your needs.

## Web of Trust
In order to efficiently use Sequoia it is important to understand its trust model. In order to communicate securely with someone you need to know his OpenPGP certificate in order to both encrypt messages for him and verify his signatures. Since you can not start a secure channel without certificates, the best way to get them is to meet him in person and exchange your respective certificates. However, it is not always possible to meet someone in person. Moreover, a key/certificate may change in future (it could be leaked, lost or just as the computation power increases he needs to generate a new one with more bits in order to avoid decreasing its security). Therefore, it is important to both send and receive certificate modifications as soon as possible and to as many people as possible.

The biggest problem of sending certificates through an insecure channel to start and end-to-end encrypted channel is that a malicious actor can replace both certificate and perform a main-in-the-middle attack without the other parties could notice it. A possible countermeasure to this kind of attack is to associate a certificate with an identity (which in OpenPGP corresponds to a UserID) which no malicious actor can modify without breaking the cryptographic algorithms.

The act of binding a certificate to an UserID is called in OpenPGP a certification, and can be performed by either the certificate owner (in which case is called self certification) or a third-part actor called in Sequoia trust introducer. Instead, the verification performed by an end-user about a certificate-UserID binding is called authentication.

There are several way to organize a authentication scheme, some of them are:
* Trust on First Use (TOFU): the first time a certificate-UserID binding appears they are both printed and shown to the end user, which should decide to accept it or not. This scheme is very simple and widely adopted in several systems;
* Centralized authentication: there are a certain number of trust introducers, called certification authorities (CAs), which are known to everyone and everyone must fully trust their certifications. TLS/HTTPS uses this scheme with the X.509 protocol for example;
* Decentralized authentication: everyone can be a trust introducer and certify any certificate-UserID binding, however the end user is free to choose which trust introducer to trust and decide how much trust put on each introducer. Therefore, trust is no more a zero/one choice, and intermediate amounts are possible. Sequoia, GnuPG and several other OpenPGP implementations use this scheme.

In Sequoia each certification of a certificate-UserID binding also specifies the following quantities:
* the trust amount (how much trust is put on that certification) is a number between 1 and 120 which states "how much trust" we put in this association, with 1 the least trust and 120 full trust. Usually, you can express partial trust by setting the trust amount to 60;
* the trust depth (how far is that certification) instead can be used to certificate trust introducers: a 0 trust depth only certificate the target binding, instead a 1 trust depth in addition states that the target is also a trust introducer and can certificate other bindings with depth at most 0, a 2 trust depth additionally allows the target to issue certifications with depth at most 1, and so on.

A certificate-UserID binding is said to be (locally for an end-user) authenticated if and only if there is one or more valid chains of third-part certifications from your local trust authority key (which is automatically generated the first time you execute ) to the target. For these chains of certifications to be valid it is needed that:
* all the trust depths limitations are honored;
* the maximum flow value of the trust amount graph is at least 120 (if there is a single path then the flow value is exactly the minimum of all the trust amounts of each certification).

Additional information about Sequoia Web of Trust can be found  in the RFC specification and in the Sequoia book.

## Usage
Sequoia's command-line utility  uses subcommands to separate all its functionalities and provide a more user-friendly interface. The generic invocation format is , and some options are global and shared between all subcommands:
# ,  uses the provided certifications/keys store instead of the default ones;
#  uses the provided command-line-interface version of  (which is different from the underlying Sequoia library version);
#  looks up certificates also in the provided keyring without importing them in the certificate store;
#  use the provided certificate as the "local trust root" for authentication purposes in the Web of Trust;
# / be more quiet or verbose respectively.

Some options in  (sub)commands requires a certification identifier. We use the notation  to denote that option opt needs a certificate and must be used in one of the following forms:
# ;
# ;
# ;
# .

## Keys and certificates
Sequoia uses the term key to refer private keys and in general all the private material that you should keep secret to anyone. Instead, it uses the terms certificate and cert to refer both public keys and key certificates in general.

## Create a key pair
Generate a key pair with

 $ sq key generate --own-key --name "Alice Example" --email alice@example.com

The  tells sq to promote the new key as an "unconstrained trust introducer" allowing it to be used to authenticate any certificate-UserID binding.

* The default cipher suite that sq uses when generating a key is . To select a specific suite, use ;
* the default expiration time is set to 3 years, you can change it with the  option;
* it also automatically generate a revocation certificate, which is your only way to revoke a certificate if you lose access to corresponding private material, by default it is saved at .

The command also prompts you to choose a password for securing private material, take a look at Security#Choosing secure passwords for tips about passwords.

## Subkeys
Just like GnuPG, you can generate subkeys with SequoiaPGP. By default  generates the following subkeys:
* a signing capable subkey, unless the  option is passed;
* an authentication capable subkey, unless the  option is passed;
* an universal encryption capable subkey, unless  option is passed or you explicitly set  where PURPOSE is one the the followings:  (suitable for encrypt data-at-rest);  (suitable for transport encryption);  (all the previous, default).

You can always add new subkeys later with .

## Change expiration date
You can change the expiration date of a certificate with the command

## Key rotation
Rotate a key means replace an old certificate and (sub)keys with a new one with the same capabilities. Additionally, a revocation certificate for the old certificate is issued indicating that the retirement of the old certificate will occur in, by default, 182 days. This period can be changed with the  option.

Key rotation is performed with the  command.

## Revoking a certificate
Revocation is done by creating a revocation certificate, that warns to not use this certificate anymore, and publishing it. Since an expired cert is automatically revoked, you need to issue a revocation certificate only if you want to revoke it before expiration date.

There are two kinds of revocations:
# soft revocations are issued just when you want to notice that the key has been superseded, and the private key material is still in the sole control of the owner and has not been leaked. Therefore, other people can still trust older signatures and encrypted data sent by the certificate owner.
# hard revocations notice instead a critical situation where the private material has been leaked. Other users should immediately stop use and trust the old certificate and every already checked signature and encrypted data should be audited (attackers with private keys can always backdate encryptions and signatures).

The difference between a soft and an hard revocation is given by the  option with REASON one of the followings: , , , .

To generate a new revocation certificate and store it in FILE use the following command:

On the converse, you can revoke a certificate by just importing the corresponding revocation certificate just like a key:

You can make the revocation public by either publishing the already-revoked certification

or by publishing the revocation certification file generated by

## List certificates and keys
To list certificates that matches the provided ,  or :

if you don't provide an argument then all stored certificates are printed.

You can use additional filtering rules with the , , , , ,  options.

To list (private) keys use instead:

## Export and import certificates
You can export multiple certificates on stdout (or a designated file is you provide the  option) with the command

 $ sq cert export $QUERY

where  filter exported certificate(s) and can consist of:
*  for only the certificate designated by its fingerprint ;
*  for all certificates containing a user id;
*  for user id matching ;
*  for user id with an email address from domain ;
*  for user id matching a pattern (case insensitive).

To import certificates from a file use instead the following command:

 $ sq cert import FILE

By default Sequoia does not authenticate certificate-UserID bindings on imported certificates unless it founds a valid certification path from the "local trust authority" to the imported certificates with a trust amount of at least 120.

## Certification and authentication
You can issue local-only binding certification (with your local trust authority) by either using  (which only allows you to set the trust amount) or  (which in addition sets the trust depth). Instead, if you want to export your binding certification then you should instead use  or  and provide a certificator with the  option.

Third-part local certifications of bindings can be revoked with the  command.

You can test if a binding is authenticated through the  command.

## Certification replaying
After rotating one or more keys with , you would like to (re)create all the certifications made by the old key using the new one. This operation to take all certifications made by A and re-certify them with B is called certification replay and can be done with the following command(s):

 $ sq pki vouch replay --source-* A --target-* B

## Keyservers
## Sending keys
You can register your key with a public PGP key server with the command

 $ sq network keyserver publish --cert FINGERPRINT

## Receiving keys
To import certificates from a keyserver use:

## Web Key Directory (WKD)
Web Key Directory (WKD) is a way of distributing certificates through domain names and webservers.

Sequoia can create the required directory structure with the command

 $ sq network wkd publish --create --domain DOMAIN.NAME /webserver/root

Once the WKD file directory is created you can publish your certificates with the command

 $ sq network wkd publish --cert-* ... --domain DOMAIN.NAME /webserver/root

You can also publish all stored fully authenticated certificates with UserID matching DOMAIN.NAME with the command

 $ sq network wkd publish --all --domain DOMAIN.NAME /webserver/root

## Certificates via DNSSEC (DANE)
Sequoia support publishing certificates through DNSSEC according to the DANE specification.

The following command generate a  record you should put in yous DNS configuration:

 $ sq network dane generate --cert-* ... --domain DOMAIN.NAME

You can also use the  option as in the previous section.

## Encrypt and decrypt
Subcommands  and  can be used to encrypt and decrypt data respectively. The encrypted output is automatically ASCII-armored (unless you use the  option) and both commands print the result to stdout (unless you specify a destination file with )

## Symmetric ciphers and passwords
The  option can be used to prompt a password, which is used to securely generate a symmetric cypher key which is then used to encrypt/decrypt the passed file. To encrypt:

where PROFILE is either  (older but compatible with every OpenPGP implementation) or  (newer but only compatible with newest OpenPGP implementations).

To decrypt:

which automatically detect if the file has been encrypted with a password and asks you to provide it if needed.

you can also use  instead of  to use an entire file instead a password to generate a file

## Asymmetric ciphers
You can encrypt a file with an asymmetric key in the following way:

You can use  to decrypt just like asymmetric encrypted files.

## Signatures
## Sign a file
To sign a file you can use the  command with any  option to sign a file. Use  instead of  to create a detached signature instead of an in-lined one.

## Verify a signature
A signature can be verified with . By default any stored authenticated certificate is used to verify a signature, but you can use  options to restrict verification to the selected certificates.

You can add the  to require at least  valid signatures to consider the file verified.

## Inspect OpenPGP packages
May happen that you want to inspect OpenPGP data stored in a file for debugging reasons. The  subcommand prints a human-readable description of an OpenPGP file:

 $ sq inspect 'FILE

If you want to get a description of each OpenPGP packet stored in an OpenPGP file then use

 $ sq packet dump [OPTIONS FILE

Look at the manpages of  and  for a comprehensive list of options.

## Tips and tricks
## Troubleshooting
