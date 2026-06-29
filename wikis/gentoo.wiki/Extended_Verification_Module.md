With EVM, the Linux kernel can be used to validate security-sensitive extended attributes before allowing operations on the files. In this guide, we will talk you through setting up EVM on Gentoo as well as how to configure it to your needs.

## Contents

-   [[1] [Purpose of EVM]](#Purpose_of_EVM)
    -   [[1.1] [Introduction]](#Introduction)
    -   [[1.2] [Hash or signature?]](#Hash_or_signature.3F)
    -   [[1.3] [The Big Fat Warnings]](#The_Big_Fat_Warnings)
-   [[2] [Setting up EVM]](#Setting_up_EVM)
    -   [[2.1] [Kernel configuration]](#Kernel_configuration)
    -   [[2.2] [Bootloader configuration]](#Bootloader_configuration)
    -   [[2.3] [Enable security file system]](#Enable_security_file_system)
    -   [[2.4] [Setting up the keys (for cryptographic hashing)]](#Setting_up_the_keys_.28for_cryptographic_hashing.29)
    -   [[2.5] [Generating EVM hashes]](#Generating_EVM_hashes)
    -   [[2.6] [Setting up the keys (for digital signatures)]](#Setting_up_the_keys_.28for_digital_signatures.29)
    -   [[2.7] [Generating EVM signatures]](#Generating_EVM_signatures)
-   [[3] [Using the EVM subsystem]](#Using_the_EVM_subsystem)
    -   [[3.1] [Enable EVM]](#Enable_EVM)
-   [[4] [Asked questions with answers]](#Asked_questions_with_answers)
    -   [[4.1] [I ran with evm=fix but when I enabled EVM, it still blocked file accesses]](#I_ran_with_evm.3Dfix_but_when_I_enabled_EVM.2C_it_still_blocked_file_accesses)
    -   [[4.2] [Can I use EVM without IMA to protect SELinux attributes?]](#Can_I_use_EVM_without_IMA_to_protect_SELinux_attributes.3F)

## [Purpose of EVM]

### [Introduction]

** Warning**\
Using EVM on your system is currently only recommended for development purposes.

The Linux kernel offers a security interface that allows new technologies to properly \"hook in\" the Linux kernel and extend its capabilities with more security-related features. This interface is called LSM (Linux Security Modules) and is used by technologies such as SELinux, SMACK and IMA as well as many others.

Many of these security technologies use extended attributes for storing information about the state of resources on the system. SELinux for instance uses the [security.selinux] extended attribute to store the SELinux security context of a file, directory or other resource. The Linux Integrity Measurement Architecture uses the [security.ima] extended attribute to store a valid hash of the file in order to detect and prevent offline tampering of files.

But if all this information is stored in extended attributes, then offline tampering of files (and guest images) allows an attacker to circumvent security rules: he can change the label of a file he wants access to when the guest is operational ([/etc/shadow] is an obvious example to this, say making it `etc_t`). Once done, and the guest boots, none of the technologies in place will detect that the extended attribute has been tampered with: SELinux reads the context and treats the file as a regular [/etc] file. And IMA doesn\'t prevent this either since the file itself has not been tampered with.

Enter EVM, the *Extended Verification Module*. With EVM, the security sensitive extended attributes are verified against offline tampering. To accomplish this, EVM creates a cryptographic hash (actually an HMAC) or a signature of the extended attributes made with a key loaded at boot time. This hash/signature is validated every time the extended attributes of a resource are consulted and the action is only allowed if the hash or signature checks out. A malicious person will need access to this key in order to tamper with the extended attributes (and if IMA is enabled, to tamper with the files). Although the key needs to be loaded at boot time, a couple of mechanisms exist to seal it away:

-   Use TPM to seal the key; this creates what is called a *trusted key* as it cannot be found (unencrypted) on the file system at any time
-   Use encryption with offloaded passphrase protection for the keys, and ask for the passphrase early at boot time. With this we can use regular *user keys* (the terminology will be used later).

Of course, using entire file system encryption thwarts the need for EVM and IMA, but yields additional overhead that not all users can endure. And this is where EVM and IMA can be used.

### [][Hash or signature?]

EVM supports both a hash-based message authentication code or a signature, similar to IMA (which uses a checksum or a signature). The hash is a cryptographic hash based on an encryption key loaded in at boot time and only usable by the EVM subsystem (when using a trusted key) or by root-owned processes with the proper privileges (in which case you can use SELinux to properly restrict access further).

The signature, as with IMA, allows the administrator to digitally sign security extended attributes that are not meant to be changed often (immutable attributes). The public key that is used to verify the signatures is loaded on the [\_evm] keyring while the private key can remain offline.

### [The Big Fat Warnings]

Using EVM on your system is currently only recommended for development purposes. Gentoo Hardened is working on integrating EVM properly, so please be aware that the system might have issues booting if not all files have their hash registered properly; you are easily warned if this is the case through the Linux audit subsystem.

We are working on proper guidelines for enabling and working with EVM.

## [Setting up EVM]

### [Kernel configuration]

First of all, enable the EVM subsystem in the Linux kernel configuration. Also enable support for the kernel keyring with trusted (if using TPM) and encrypted keys.

[KERNEL] **Linux kernel configuration for EVM**

    CONFIG_KEYS=y
    CONFIG_TRUSTED_KEYS=y
    CONFIG_ENCRYPTED_KEYS=y

    CONFIG_INTEGRITY=y
    CONFIG_INTEGRITY_SIGNATURE=y
    CONFIG_EVM=y

    # If you have a TPM
    CONFIG_TCG_TPM=y

### [Bootloader configuration]

Next, configure the bootloader to enable EVM:

[CODE] **Bootloader configuration to enable EVM policy**

    kernel /boot/vmlinuz root=/dev/vda1 ... evm=fix

We currently set `evm=fix` because the extended attributes have not been checked by EVM yet. We will be signing these later, after which the boot parameter can be removed.

Reboot with your freshly built kernel.

### [Enable security file system]

Finally, have the security file system mounted (if this is not already the case):

`root `[`#`]`mount | grep securityfs`

    securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)

### [][Setting up the keys (for cryptographic hashing)]

We will now be creating the key for EVM. Since the key will be used often, it has to be a \"fast\" key to use. As such, we will use a standard user-encrypted key for this. To properly protect the key, a master key will be created first from which the EVM key can then be generated. The security of this master key is important, so if you have a TPM chip that you control, it is wise to use a *trusted* key for the master key. The EVM key remains a *user* key but is generated (and validated) by the master key.

We will store the blobs (binary dumps of the encrypted keys) in [/etc/keys]:

Use this if you have a TPM 1.2 chip that you control:

`root `[`#`]`keyctl add trusted kmk-trusted "new 32" @u `

`root `[`#`]`` keyctl pipe `keyctl search @u trusted kmk-trusted` > /etc/keys/kmk-trusted.blob  ``

`root `[`#`]`keyctl add encrypted evm-key "new trusted:kmk-trusted 32" @u `

`root `[`#`]`` keyctl pipe `keyctl search @u encrypted evm-key` > /etc/keys/evm-trusted.blob ``

Use this if you have a TPM 2.0 chip that you control (this assumes the existence of a suitable key at location 0x81000001, which is recommended location of the TPM 2.0 equivalent of the SRK.)

`root `[`#`]`keyctl add trusted kmk-trusted "new 32 keyhandle=0x81000001" @u `

`root `[`#`]`` keyctl pipe `keyctl search @u trusted kmk-trusted` > /etc/keys/kmk-trusted.blob  ``

`root `[`#`]`keyctl add encrypted evm-key "new trusted:kmk-trusted 32" @u `

`root `[`#`]`` keyctl pipe `keyctl search @u encrypted evm-key` > /etc/keys/evm-trusted.blob ``

Use this if you do not have a TPM chip that you control:

`root `[`#`]`dd if=/dev/urandom bs=1 count=32 status=none | keyctl padd user kmk-user @u `

`root `[`#`]`` keyctl pipe `keyctl search @u user kmk-user` > /etc/keys/kmk-user.blob  ``

`root `[`#`]`keyctl add encrypted evm-key "new user:kmk-user 32" @u `

`root `[`#`]`` keyctl pipe `keyctl search @u encrypted evm-key` > /etc/keys/evm-user.blob ``

** Note**\
If you have a TPM chip, on the fourth command may receive the following error:

    keyctl_read_alloc: Operation not supported

If you do, see [https://bugzilla.kernel.org/show_bug.cgi?id=202577](https://bugzilla.kernel.org/show_bug.cgi?id=202577)

These four commands execute the following tasks:

1.  Create a master key named [kmk-trusted] or [kmk-user]. If we asked for a trusted key, then the key is generated by the TPM and sealed by the TPM (meaning it is encrypted by the TPM itself and can only be decrypted by the TPM). The key is made 256 bits long (32 bytes) and added to the user keyring (`@u`).
2.  Look for the key we generated in the first step, and output the key value into a file. The output is an encrypted value in case of a trusted key, or the key itself in case of the user key.
3.  Next, we generate a user key through the master key. In other words, the master key is used to encrypt (seal) the user key. The generated user key is called `evm-key`.
4.  Finally, we search for the key generated in the third step, and output the value into a file. The output is an encrypted value of the key (encrypted through the master key).

It is important that the key for EVM is called *evm-key* as this is the key searched for by the EVM subsystem on the root\'s keyring (i.e. the user keyring for the root Linux user).

Make sure that the keys are loaded at boot time. This can be done through an initramfs, or through a service script early at boot. The following init script shows you what needs to be done to load the keys.

[CODE] **The security_keys init script**

    #!/sbin/openrc-run
    # Copyright 1999-2012 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2
    # $Header: /var/cvsroot/gentoo/xml/htdocs/proj/en/hardened/integrity/docs/evm-guide.xml,v 1.4 2013/03/09 13:55:21 swift Exp $

    description="Load in the EVM and IMA keys"

    start()

### [Generating EVM hashes]

Now we need to generate the EVM cryptographic hashes. Enable EVM first by echo\'ing 1 into [/sys/kernel/security/evm] after the keys are loaded, and then have IMA regenerate all its [security.ima] attributes (which as a result will have EVM generate its own cryptographic hashes).

Boot with `ima_appraise=fix evm=fix` and run something similar as the following `find` command.

`root `[`#`]`find / \( -fstype rootfs -o -fstype ext4 \) -type f -uid 0 -exec head -c 1 '' > /dev/null \;`

### [][Setting up the keys (for digital signatures)]

To use digital signatures, first create a keypair (public and private) to use.

Unencrypted private key (non-protected):

`root `[`#`]`openssl genrsa -out rsa_private.pem 1024`

Or encrypted private key (password-protected):

`root `[`#`]`openssl genrsa -des3 -out rsa_private.pem 1024`

Public key:

`root `[`#`]`openssl rsa -pubout -in rsa_private.pem -out rsa_public.pem`

Next, we load the public key on the EVM keyring:

`root `[`#`]`` evm_id=`keyctl newring _evm @u`  ``

`root `[`#`]`evmctl import --rsa /etc/keys/rsa_public.pem $evm_id`

Now the EVM sub system is able to validate digital signatures. So let\'s create a few of those shall we?

### [Generating EVM signatures]

Now we need to generate the EVM digital signatures. We use the `evmctl` command provided by *ima-evm-utils* for this. For instance, to generate the digital signatures for all binaries in [/sbin]:

`root `[`#`]`find /sbin -type f -exec evmctl sign --imahash '' --key /etc/keys/rsa_private.pem \;`

If the IMA keys are loaded as well, you can have both digital signatures for EVM as well as for IMA:

`root `[`#`]`find /sbin -type f -exec evmctl sign --imasig '' --key /etc/keys/rsa_private.pem \;`

## [Using the EVM subsystem]

### [Enable EVM]

EVM is by default not enabled until you tell it to start. This is because you need to load in the EVM keys in the keyring so that EVM can start validating the signatures. Once that is done, you can start EVM by echo\'ing 1 into [/sys/kernel/security/evm]

`root `[`#`]`echo 1 > /sys/kernel/security/evm`

## [Asked questions with answers]

### [][I ran with evm=fix but when I enabled EVM, it still blocked file accesses]

If you use `evm=fix` you also need `ima_appraise=fix` . This is because the IMA appraisal code checks the EVM attribute as well and, if the check fails, the IMA appraisal code will refuse access.

### [][Can I use EVM without IMA to protect SELinux attributes?]

Although you can enable EVM to create hashes on the SELinux attributes, you need the IMA appraisal to be enabled in order for the protection to work. EVM by itself does not enforce the hashes and would only register changes if you do not use IMA with the appraisal feature enabled.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Sven Vermeulen**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*