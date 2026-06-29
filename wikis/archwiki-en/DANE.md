# DANE

DANE (DNS-based Authentication of Named Entities) is a protocol to allow X.509 certificates, commonly used for Transport Layer Security (TLS), to be bound to DNS names using Domain Name System Security Extensions (DNSSEC) instead of (or in complement of) a pre-defined list of Certificate Authorities (CA).

## TLSA resource record
The TLSA resource record is an own type of DNS record. It consists of port number and protocol of the service secured by it.
An example record for port 25 over tcp could look like .
The TLSA parameters  are explaining the data following it. The first number is the Certificate Usage Field, the second is the Selector Field and the third is named Matching Type Field.

{| class="wikitable"
|+ Certificate Usage Field
! Value !! Name !! Description
|-
| 0 || PKIX trust anchor || Hash contains a public CA from the x509 tree by which your cert has to be signed
|-
| 1 || PKIX end entity || Hash contains your cert which also has to pass x509 validation
|-
| 2 || DANE trust anchor || Hash contains a private CA (unknown to the x509 tree) by which your cert has to be signed
|-
| 3 || DANE end entity || Hash contains your cert which is not matched against any other validation
|}

{| class="wikitable"
|+ Selector Field
! Value !! Name !! Description
|-
| 0 || cert || DATA is based on the full cert
|-
| 1 || SPKI || DATA is based on public key only
|}

{| class="wikitable"
|+ Matching Type Field
! Value !!	Name  !! Description
|-
|0	|| Full || DATA is the full cert or SPKI
|-
|1	|| sha256 || DATA is the sha256 hash of the cert or SPKI
|-
|2	|| sha512 || DATA is the sha512 hash of the cert or SPKI
|}

The RR can also easily be generated with  from .

## SSHFP resource record
See OpenSSH#SSHFP record.

## DANE supporting software
* Postfix
* Exim > 4.85
* Prosody (via )
