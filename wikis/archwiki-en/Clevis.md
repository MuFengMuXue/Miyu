# Clevis

Clevis allows binding a LUKS volume to a system by creating a key and encrypting it using the TPM, and sealing the key using PCR values which represent the system state at the time of the Clevis pin creation.

Passwords manually entered by a user is a traditional and widely used way to unlock encrypted LUKS partitions. But it has a few disadvantages:

* It requires manual intervention and thus does not work with setups that require automatic boot (e.g. a large server farm).
* An average human brain is capable of remembering relatively simple passwords (~20-30 bits of entropy) that are much weaker than keys used for modern block ciphers (128/256 bits).

A solution for it would be encrypting data with a strong key stored securely somewhere else, for example at your TPM chip or YubiKey or some network service. Clevis is a framework that implements this idea. It allows to encrypt (in terms of clevis bind) data with a pluggable pin. Currently clevis implements 3 pins:

* TPM2 data binding (works only if you have a Trusted Platform Module chip at your computer)
* Network service (called Tang) data binding
* Shamir's Secret Sharing that allows you to combine other pins.
* YubiKey binding using an external plugin.

## Installation
To use clevis install  package.

## Bind some data
Here is an example of data binding with TPM2:

{{hc|$ clevis encrypt tpm2 '{}' <<< 'hello, world'|
eyJhbGciOiJkaXIiLCJjbGV2aXMiOnsicGluIjoidHBtMiIsInRwbTIiOnsiaGFzaCI6InNoYTI1NiIsImp3a19wcml2IjoiQU80QUlJQkxxT3FVenVDU1FmWkprNmdDN2wzMW43V3M2Y2FZd0VZS1BSR3Q0OHJEQUJBV2Z4M3pTUUNUTmtHZE9BM2FZd2RTZk9GcXZWdnVlQ3lPamFsWldCT2R4RlJKSzl5ZVRCM0pkNFktcF9HalhhNmlnLWxxNmtmMHZTWWkzOWMxVEpES1RYRVZTdnlXSlpEbGdxQ0JPMVNxeGJBd2tfSnIyRlRNY3hvNGtpSmNtMEVjbWd5dFdyME00QmcySlg4aVo3MEt1MTVjNzFORU5Ra3RjdGMtREhBVGFQcHJ2VzI2Z3d1YmUxckRfX19aV2tHaG9mX053M0M1OHlOcXF2RUpPZUwzNTZHNXJHNVVtYmUtWWV4Ujl2SEppZWlua3ZaNTJoMFVRYWVNSm9LYjJuNjlVTGZHb2J1NElTN20iLCJqd2tfcHViIjoiQUM0QUNBQUxBQUFFMGdBQUFCQUFJQ2poWDBVeTJKZVpSNU9pRU0ySktSeEtnUElYQ3dGNnRNR09NTDZ0ZnE5aiIsImtleSI6ImVjYyJ9fSwiZW5jIjoiQTI1NkdDTSJ9..1P2Emag_4k-GlhyY.MuQQYPa8QHrysZ74uA.0ddDxfZA3R-cCmaKu5yUZA
}}

This long base64-encoded message is our text encrypted with an internal TPM key. It can be decrypted at the current computer only. Trying to decrypt it from another computer (or rather with another TPM chip) will return an error.

{{hc|$ clevis decrypt tpm2 '{}' <<< 'eyJhbGciOiJkaXIiLCJjbGV2aXMiOnsicGluIjoidHBtMiIsInRwbTIiOnsiaGFzaCI6InNoYTI1NiIsImp3a19wcml2IjoiQU80QUlJQkxxT3FVenVDU1FmWkprNmdDN2wzMW43V3M2Y2FZd0VZS1BSR3Q0OHJEQUJBV2Z4M3pTUUNUTmtHZE9BM2FZd2RTZk9GcXZWdnVlQ3lPamFsWldCT2R4RlJKSzl5ZVRCM0pkNFktcF9HalhhNmlnLWxxNmtmMHZTWWkzOWMxVEpES1RYRVZTdnlXSlpEbGdxQ0JPMVNxeGJBd2tfSnIyRlRNY3hvNGtpSmNtMEVjbWd5dFdyME00QmcySlg4aVo3MEt1MTVjNzFORU5Ra3RjdGMtREhBVGFQcHJ2VzI2Z3d1YmUxckRfX19aV2tHaG9mX053M0M1OHlOcXF2RUpPZUwzNTZHNXJHNVVtYmUtWWV4Ujl2SEppZWlua3ZaNTJoMFVRYWVNSm9LYjJuNjlVTGZHb2J1NElTN20iLCJqd2tfcHViIjoiQUM0QUNBQUxBQUFFMGdBQUFCQUFJQ2poWDBVeTJKZVpSNU9pRU0ySktSeEtnUElYQ3dGNnRNR09NTDZ0ZnE5aiIsImtleSI6ImVjYyJ9fSwiZW5jIjoiQTI1NkdDTSJ9..1P2Emag_4k-GlhyY.MuQQYPa8QHrysZ74uA.0ddDxfZA3R-cCmaKu5yUZA'|
hello, world
}}

## Bind a LUKS volume
To bind a LUKS volume to the TPM, use:

 # clevis luks bind -d /dev/sdX tpm2 '{}'

where {{ic|'{}'|}} contains the configuration: even with no parameters the drive cannot be decrypted from another computer, unless the attacker knows the backup password.

{{Note|To seal the LUKS key against the UEFI settings and the Secure Boot policy, use:

 '{"pcr_ids":"1,7"}'

If the UEFI or Secure Boot settings are modified, the TPM will compute different PCR values and decryption will fail. This gives protection against evil maid attacks.

For a list of parameters, see .

For a simplified explanation of the meaning of PCRs, see Trusted Platform Module#Accessing PCR registers.

For a full explanation of the meanings of PCRs, see the TCG specification (§ 2.3.4).

If this fails with , you should specify a different pcr bank:

 '{"pcr_bank":"sha256","pcr_ids":"1,7"}'

As of August 2022 Clevis only supports sha1 (default) and sha256 banks, so naturally the only different option is sha256 - you can look up available and used banks using .
}}

To generate a new Clevis pin after changes in system configuration that result in different PCR values, for example updating the UEFI when PCR 0 is used, run

to find the slot used for the Clevis pin, then

 # clevis luks regen -d /dev/sdX -s keyslot

To remove the Clevis binding, run:

 # clevis luks unbind -d /dev/sdX -s keyslot

You can unlock a TPM-bound volume using:

 # clevis luks unlock -d /dev/sdX

For automated decryption of volumes in /etc/crypttab, enable .

For automated decryption of the root volume, we should make some changes to our Initramfs generators:

## Mkinitcpio hook
Install the  package. Then enable the clevis hook editing mkinitcpio.conf:

At the end regenerate the initramfs.

## Booster
Luckily Booster automatically decrypts LUKS volumes bound using Clevis out of the box!

Booster is also able to read the LUKS tokens, decode clevis information, reconstruct the password and unlock the partition automatically.

Tang (network binding) pin requires network enabled. Please refer to Booster#Configuration section for more information on network configuration with booster.

## Dracut
Dracut needs the following extra packages:

*
*
*

Followed by an initramfs regeneration:

 # dracut -f

## Tips and tricks
## YubiKey binding
Clevis allows binding a LUKS partition using YubiKey's challenge-response mode. To bind a LUKS partition, run

 # clevis luks bind -d /dev/sdX yubikey '{"slot":1}'

Install . Edit the configuration file and add following option:

Regenerate the booster images. Booster will detect this configuration during boot and use the present YubiKey to unlock the drive.
