# Trusted Platform Module

Trusted Platform Module (TPM) is an international standard for a secure cryptoprocessor, which is a dedicated microprocessor designed to secure hardware by integrating cryptographic keys into devices.

In practice a TPM can be used for various different security applications such as secure boot, key storage and random number generation.

TPM is naturally supported only on devices that have TPM hardware support. If your hardware has TPM support but it is not showing up, it might need to be enabled in the BIOS settings.

## Checking TPM support
Most modern computers support TPM 2.0, as it has been required for Windows 10 certification since 2016. To check support on your system, use any of the following methods:

* check the logs, e.g., by running  as root
* read the value of , or :

 $ cat /sys/class/tpm/tpm0/device/description
 TPM 2.0 Device

* use  to check for TPM 2.0 and the necessary software dependencies:

TPM 2.0 allows direct access via  (one client at a time), kernel-managed access via , or managed access through the  resource manager daemon. [https://groups.google.com/g/linux.debian.bugs.dist/c/OWBHw40g6Vk/m/rnwwkVapDAAJ According to a systemd project member, using  is no longer recommended. There are two choices of userspace tools,  by Intel and  by IBM.

TPM 2.0 requires UEFI boot; BIOS or Legacy boot systems can only use TPM 1.2.

Some TPM chips can be switched between 2.0 and 1.2 through a firmware upgrade (which can be done only a limited number of times).

## Usage
Many informative resources to learn how to configure and make use of TPM 2.0 services in daily applications are available from the tpm2-software community.

## LUKS encryption
It is possible to encrypt volumes using keys securely stored in the TPM. This approach ensures that your drives remain locked unless the TPM is present and specific conditions are met, such as the integrity of the firmware or Secure Boot state (see #Accessing PCR registers).

This mechanism can be used to automatically decrypt the root volume during the boot process, similarly to how BitLocker works on Windows or FileVault on macOS. While this provides strong protection if the drive is removed from the computer with the TPM, data protection will only rely on basic measures like user passwords and system settings if the entire PC is stolen. To mitigate this, you can:

* Consider encrypting user data, such as individual home folders, with a different mechanism, such as fscrypt or systemd-homed.
* Use a TPM pin to benefit from the security properties of the TPM, while avoiding completely unattended unlocking.

systemd-cryptenroll and Clevis allow locking LUKS volumes with a key stored in the TPM. Additionally, systemd-cryptenroll enables tying the encryption to signed policies instead of static PCR values (See ).

## SSH
For TPM sealed SSH keys, there are two options:

*
:See Store ssh keys inside the TPM: ssh-tpm-agent.
*
:See SSH configuration and Using a TPM for SSH authentication (2020-01).

## systemd-creds
systemd-creds uses TPM to securely store and retrieve credentials used by systemd units.

## GnuPG
GnuPG, since version 2.3, supports moving compatible keys into the TPM. See Using a TPM with GnuPG 2.3 for the instructions.

## OpenSSL
There are OpenSSL providers and OpenSSL engines that implement storing keys in the TPM.

*
*
:See Using the TPM - It's Not Rocket Science (Anymore) - Johannes Holland & Peter Huewe (2020-11, Youtube)

## Other good examples of TPM 2.0 usage
* Configuring Secure Boot + TPM 2 (2018-06, Debian)

## Accessing PCR registers
Platform Configuration Registers (PCR) allow binding of the encryption of secrets to specific software versions and system state via hashes, so that the enrolled key is only accessible (may be "unsealed") if specific trusted software and/or configuration is used.

PCRs are intended to be used for platform hardware and software integrity verification between boots (e.g. protection against Evil Maid attack).

The TCG PC Client Specific Platform Firmware Profile Specification defines the registers in use, and The Linux TPM PCR Registry assigns Linux system components using them.

The registers are:
:

{| class="wikitable"
|-
! scope="col"| PCR
! scope="col"| Description
! scope="col"| Extended by
|-
|PCR0
|Core System Firmware executable code (aka Firmware). May change if you upgrade your UEFI.
|Firmware
|-
|PCR1
|Core System Firmware data (aka UEFI settings; configured boot order, for example)
|Firmware
|-
|PCR2
|Extended or pluggable executable code (aka OpROMs)
|Firmware
|-
|PCR3
|Extended or pluggable firmware data. Set during Boot Device Select UEFI boot phase.
|Firmware
|-
|PCR4
|Boot Manager Code and Boot Attempts. Measures the boot manager and the devices that the firmware tried to boot from.
|Firmware
|-
|PCR5
|Boot Manager Configuration and Data. Can measure configuration of boot loaders; includes the GPT Partition Table.
|Firmware
|-
|PCR6
|Resume from S4 and S5 Power State Events
|Firmware
|-
|PCR7
|Secure Boot State. Contains the full contents of PK/KEK/db, as well as the specific certificates used to validate each boot application|Firmware, shim (adds MokList, MokListX, and MokSBState)
|-
|PCR81
|Hash of the kernel command line
|[https://lists.gnu.org/archive/html/grub-devel/2017-07/msg00003.html GRUB
|-
|PCR91
|Hash of the initramfs and EFI Load Options
|Linux (measures the initramfs and EFI Load Options, essentially the kernel cmdline options)
|-
|PCR101
|Reserved for Future Use
|
|-
|PCR111
|Hash of the Unified kernel image
|
|-
|PCR121
|Overridden kernel command line, Credentials
|
|-
|PCR131
|System Extensions
|
|-
|PCR141
|shim's MokList, MokListX, and MokSBState.|shim
|-
|PCR151
|Hash of the LUKS volume key
|[https://systemd.io/TPM2_PCR_MEASUREMENTS/#pcr-measurements-made-by-systemd-cryptsetup-userspace systemd-cryptsetup
|-
|PCR161
|Debug. May be used and reset at any time. May be absent from an official firmware release.
|
|-
|PCR23
|Application Support. The OS can set and reset this PCR.
|
|}

# Use case defined by the OS and might change between various Linux distros and Windows devices.

On Windows, BitLocker uses PCR8-11 (Legacy) or PCR11-14 (UEFI) for its own purposes.
Documentation from tianocorefacilitates this check with a human observer and dedicated trusted device.

The current PCR values can be listed with :

 $ systemd-analyze pcrs

Or, alternatively with  from :

 # tpm2_pcrread

## PCR policies
With TPM2 it is possible to bind secrets, like the LUKS root decryption key, to a signed policy rather than raw PCR values. These policies add flexibility by allowing PCR values to vary, provided there is a valid PCR signature for these values which matches the public key enrolled with the secret. For instance, rather than simply tying the encryption key to the PCR7 value (which only checks that Secure Boot hasn't been disabled or tampered with) you can bind it to a PCR policy that verifies the booting of a known Unified kernel image (UKI), with all its components measured during the boot process. See .

The example below enables decrypting a root partition during boot, (i.e. in the initramfs stage), without the encryption key being accessible after the system has fully booted up. See  for examples with multiple trust policies for different phases of the boot.

First generate the necessary signing keys:

 # ukify genkey \
         --pcr-private-key=/etc/systemd/tpm2-pcr-private-key.pem \
         --pcr-public-key=/etc/systemd/tpm2-pcr-public-key.pem
 # ukify genkey \
         --pcr-private-key=/etc/systemd/tpm2-pcr-private-key-initrd.pem \
         --pcr-public-key=/etc/systemd/tpm2-pcr-public-key-initrd.pem

Create  or copy the template from . Although PCR policies can be used without Secure Boot, it makes sense to also sign your UKI, so update the following as needed with your keys:

To generate the UKI, use a tool which reads  by default, such as kernel-install or mkinitcpio.

Finally, enroll the TPM2 policy in your LUKS volumes.

 # systemd-cryptenroll --wipe-slot tpm2 --tpm2-device auto \
                       --tpm2-public-key /etc/systemd/tpm2-pcr-public-key-initrd.pem \
                       /dev/disk/by-label/root

Check the UKI with  to make sure it contains the  section.

Also check that the LUKs volume registered the public key:

## Tips and tricks
## Pinning a LUKS volume
Relying solely on pre-boot PCRs (PCRs 0–7) could leave the system vulnerable to rogue operating systems. To mitigate this risk, you can pin the unified kernel image to a specific LUKS volume, as described in dm-crypt/System configuration#Pinning a LUKS volume.

## Using TPM as a FIDO device
See WebAuthn#Using TPM as a FIDO device.

## Verify TPM hardware with trusted vendor Endorsement Key chain
 can be used to verify your TPM's root certificate bundles. Validating the Endorsement Key Certificate's chain allows you to verify that a TPM is genuine by confirming it was manufactured by a trusted vendor.

Once the device's nature has been verified (and typically added to an inventory), you can leverage advanced security capabilities such as:

* Provisioning: securely add secrets or keys to the TPM
* Remote Attestation: verify the integrity and configuration of a remote system
* HMAC Salted Sessions: establish secure, authenticated communication channels with the TPM

Without a trusted root certificate bundle, there is no reliable way to validate the provenance of a TPM device.

## Troubleshooting
## TPM2 LUKS2 unlocking still asking for password
If you followed the instruction described above for automatically unlocking luks2 devices with enrolled keys in a TPM2 hardware module, but still receive a prompt to input a password during the initramfs boot stage. You may need to early load the kernel module (you can obtain its name with ) that is responsible for handling your specific TPM2 module.

## A TPM error (714) occurred attempting to create NULL primary
Starting from Linux Kernel 6.10  was enabled by default and now TPM must support AES-128-CFB for session encryption.
TPMs that do not support this mode, such as older Intel PTT, will fail to initialize the driver, resulting in . Replacing hardware is the only complete solution.
systemd-cryptenroll also requires AES-128-CFB support, so disabling kernel option isn't enough and it will fails producing this error:

## libvirtd failing to start after changing tpm2-pcr key
If the  is changed to a new pair of keys, the libvirtd.service may fail to start. In this case it may be necessary to remove  and restart the service.
