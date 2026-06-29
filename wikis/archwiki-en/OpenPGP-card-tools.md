# OpenPGP-card-tools

Openpgp-card-tools is a software package offering the commandline tool  for interacting with OpenPGP smartcards (using ).

## Installation
Install the  package.

## Configuration
The  tool relies on  and . It requires to enable and start the .

## Interact with OpenPGP cards
The  tool provides several subcommands, which provide functionality related to OpenPGP cards:

*  to list connected cards
*  to show information about data on a card
*  to show technical details about a card
*  to show a card's authentication key as an SSH public key
*  to administer data on a card that require the admin PIN
*  to manage PINs of a card
*  to decrypt data using a card
*  to sign data using a card
*  to attest that keys have been generated on a card (YubiKey only)
*  to interact with low-level card functionality

## Tips and tricks
## Machine readable output
The  tool offers machine readable output format for all subcommands by using the  option.

To list attached cards in JSON output format:

 $ oct --output-format=json list

## Import an OpenPGP private key
With  it is possible to directly import an OpenPGP private key.

To import a private key with the fingerprint  to the card with the identifier :

 $ oct admin --card 0123:01234567 import  hello.txt
 $ oct sign --card 0123:01234567 detached hello.txt 2>/dev/null
 Enter User PIN:
 -----BEGIN PGP MESSAGE-----

 wr0EABYKAG8FgmVcxgQJEHwxCjP5RdJLRxQAAAAAAB4AIHNhbHRAbm90YXRpb25z
 LnNlcXVvaWEtcGdwLm9yZ8BSR6PrXSIRnrQl6r6HEetWVjCVXQtR1Z3PzD9EfbWY
 FiEEuFXqMwYb6iFIyl2ufDEKM/lF0ksAAOY2AQC7+Tuh8Gal+kCCfVChD0VV+GUA
 yd+leLeylIySXV7qVwD9H2x5QBrgyF/vODNp1tdorTvPwieV/Bop9FCkHYbHJg8=
 =cOQ/
 -----END PGP MESSAGE-----

## Decrypt encrypted data
With  it is possible to decrypt data using the encryption slot of a card.

In the below example a message is encrypted using , using the OpenPGP public key .

 $ echo "hey archie" | sq encrypt --recipient-file archie.pub > message.pgp
 $ oct decrypt --card 0123:01234567 message.pgp
 Enter User PIN:
 hey archie

## Switch identities of a Nitrokey Start
The Nitrokey Start offers using three separate identities on a single hardware token, each with their separate signing, encryption and authentication slot. Effectively, this is equal to having three separate OpenPGP smartcards with separate card identifiers.

With  it is possible to switch between these identities.

To switch to the second identity, use:

 $ oct system set-identity --card FFFE:01234567 1

To switch back to the first identity, use:

 $ oct system set-identity --card FF01:01234567 0

## Troubleshooting
## Debug smartcard setup
Use  to list all connected cards that are available to .
If the connected card is not showing up, it is likely that it is blocked by another process, such as scdaemon.
The  can be terminated using

 $ gpgconf --kill scdaemon
