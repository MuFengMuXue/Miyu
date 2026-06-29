# OpenPGP card

OpenPGP card describes an open standard for an application that runs on hardware security devices. Both open and closed source implementations exist.

The motivation to use OpenPGP card devices, as for all hardware security devices, is to not expose the private key material to the host computer.

With OpenPGP card it is possible to cover all OpenPGP private key operations: Decryption and signing.

## Installation
OpenPGP card devices can either be used with  and the  driver or with  which includes its own, custom CCID driver.

## Key slots
OpenPGP card devices offer three dedicated slots for private key material, one each for signing, decryption and authentication.

## Ssh-agent
Using private key material in an authentication slot SSH logins can be performed by an ssh-agent implementation that can use OpenPGP card devices.
Available options include GnuPG as ssh-agent and openpgp-card-ssh-agent.

## Further use-cases
OpenPGP card devices can be used in a wide range of contexts to perform OpenPGP operations for signing and decryption.
Typical uses include signing commits with git and data-at-rest encryption when integrating Thunderbird with OpenPGP cards or when using pass for passwords.
