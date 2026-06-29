# Systemd-cryptenroll

From :

:systemd-cryptenroll is a tool for enrolling hardware security tokens and devices into a LUKS2 encrypted volume, which may then be used to unlock the volume during boot.

systemd-cryptenroll allows enrolling smartcards, FIDO2 tokens and Trusted Platform Module security chips into LUKS devices, as well as regular passphrases. These devices are later unlocked by , using the enrolled tokens.

## Installation
systemd-cryptenroll is part of and packaged with . However, extra packages are required to use hardware devices as keys:

* To use PKCS#11 tokens, install , you may also need  and .
* To use FIDO2 tokens, install .
* To use TPM2 devices, install .

## List keyslots
systemd-cryptenroll can list the keyslots in a LUKS device, similar to  luksDump, but in a more user-friendly format.

## Erasing keyslots
 # systemd-cryptenroll /dev/disk --wipe-slot=SLOT

Where SLOT can be:

* A single keyslot index, as represented in #List keyslots
* A type of keyslot, which will erase all keyslots of that type. Valid types are , , , , ,
* A combination of all of the above, separated by commas
* The string , which erases all keyslots on the device. This option can only be used when enrolling another device or passphrase at the same time.

The  operation can be used in combination with all enrollment options, which is useful to update existing device enrollments:

 # systemd-cryptenroll /dev/disk --wipe-slot=fido2 --fido2-device=auto

## Enrolling passphrases
## Regular password
This is equivalent to .

 # systemd-cryptenroll /dev/disk --password

## Recovery key
From :

:Recovery keys are mostly identical to passphrases, but are computer-generated instead of being chosen by a human, and thus have a guaranteed high entropy. The key uses a character set that is easy to type in, and may be scanned off screen via a QR code.

A recovery key is designed to be used as a fallback if the hardware tokens are unavailable, and can be used in place of regular passphrases whenever they are required.

 # systemd-cryptenroll /dev/disk --recovery-key

## Enrolling hardware devices
The  options must point to a valid device path of their respective type. A list of available devices can be obtained by passing the  argument to this option. Alternatively, if you only have a single device of the desired type connected, the  option can be used to automatically select it.

## PKCS#11 tokens or smartcards
The token or smartcard must contain a RSA key pair, which will be used to encrypt the generated key that will be used to unlock the volume.

 # systemd-cryptenroll /dev/disk --pkcs11-token-uri=device

## FIDO2 tokens
Any FIDO2 token that supports the "hmac-secret" extension can be used with systemd-cryptenroll. The following example would enroll a FIDO2 token to an encrypted LUKS2 block device, requiring only user presence as authentication.

 # systemd-cryptenroll /dev/disk --fido2-device=device --fido2-with-client-pin=no

In addition, systemd-cryptenroll supports using the token's built-in user verification methods:

*  defines whether to verify the user presence (i.e. by tapping the token) before unlocking, defaults to yes
*  defines whether to require user verification before unlocking, defaults to no

By default, the cryptographic algorithm used when generating a FIDO2 credential is es256 which denotes Elliptic Curve Digital Signature Algorithm (ECDSA) over NIST P-256 with SHA-256. If desired and provided by the FIDO2 token, a different cryptographic algorithm can be specified during enrollment.

Suppose that a previous FIDO2 token has already been enrolled and the user wishes to enroll another, the following generates an eddsa credential which denotes EdDSA over Curve25519 with SHA-512 and authenticates the device with a previous enrolled token instead of a password.

 # systemd-cryptenroll /dev/disk --fido2-device=device --fido2-credential-algorithm=eddsa --unlock-fido2-device=auto

## Trusted Platform Module
systemd-cryptenroll has native support for enrolling LUKS keys in TPMs. It requires the following:

*  must be installed,
* A LUKS2 device (currently the default type used by cryptsetup),
* If you intend to use this method on your root partition, some tweaks need to be made to the initramfs (see dm-crypt/System configuration#Using systemd-cryptsetup-generator for advanced configuration) :
** mkinitcpio users: enable the  and  hooks.
** dracut users: enable the  module.

To begin, run the following command to list your installed TPMs and the driver in use:

 $ systemd-cryptenroll --tpm2-device=list

A key may be enrolled in both the TPM and the LUKS volume using only one command. The following example generates a new random key, adds it to the volume so it can be used to unlock it in addition to the existing keys, and binds this new key to PCR 7 (Secure Boot state):

 # systemd-cryptenroll --tpm2-device=auto --tpm2-pcrs=7 /dev/sdX

where  is the full path to the encrypted LUKS volume. Use  if the LUKS volume is unlocked by a keyfile instead of a passphrase.

Refer to  and Trusted Platform Module#Accessing PCR registers for common PCR measurements in Linux. Adjust  as necessary (parameters are separated by the  symbol).

The combination of PCRs to bind to depends on the individual case to balance usability and lock-down. For example, you may require UEFI firmware updates without manual intervention to the Secure Boot state, or different boot devices. As another example, Microsoft's Bitlocker prefers PCR , but may also use other PCR combinations.

To check that the new key was enrolled, dump the LUKS configuration and look for a  token entry, as well as an additional entry in the Keyslots section:

 # cryptsetup luksDump /dev/sdX

To test that the key works, run the following command while the LUKS volume is closed:

 # systemd-cryptsetup attach mapping_name /dev/sdX none tpm2-device=auto

where  is your chosen name for the volume once opened.

See dm-crypt/System configuration#crypttab and dm-crypt/System configuration#Trusted Platform Module and FIDO2 keys in order to unlock the volume at boot time.

See  and  for more information and examples.
