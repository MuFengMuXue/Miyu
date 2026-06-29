When support for signed [kernel modules](https://wiki.gentoo.org/wiki/Kernel_Modules "Kernel Modules") is enabled in enforcing mode, the Linux kernel will only load kernel modules that are digitally signed with the proper key. This allows further hardening of the system by disallowing unsigned kernel modules, or kernel modules signed with the wrong key, to be loaded. Malicious kernel modules are a common method for loading rootkits on a Linux system.

## Contents

-   [[1] [Enabling module signature verification]](#Enabling_module_signature_verification)
    -   [[1.1] [Configuring module signature verification]](#Configuring_module_signature_verification)
    -   [[1.2] [Building the kernel with proper keys]](#Building_the_kernel_with_proper_keys)
        -   [[1.2.1] [Generating keys by default]](#Generating_keys_by_default)
        -   [[1.2.2] [Using Secure Boot keys]](#Using_Secure_Boot_keys)
        -   [[1.2.3] [Generating keys directly]](#Generating_keys_directly)
    -   [[1.3] [Validation]](#Validation)
        -   [[1.3.1] [Kernel certificates]](#Kernel_certificates)
        -   [[1.3.2] [Module signatures]](#Module_signatures)
        -   [[1.3.3] [Kernel taint]](#Kernel_taint)
        -   [[1.3.4] [Directly checking module signatures]](#Directly_checking_module_signatures)
-   [[2] [Administering kernel module signatures]](#Administering_kernel_module_signatures)
    -   [[2.1] [Protecting the private key]](#Protecting_the_private_key)
    -   [[2.2] [Manually signing modules]](#Manually_signing_modules)
    -   [[2.3] [Automatically signing kernel modules (Portage)]](#Automatically_signing_kernel_modules_.28Portage.29)
    -   [[2.4] [Distributing the kernel and modules]](#Distributing_the_kernel_and_modules)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)
-   [[5] [External resources]](#External_resources)

## [Enabling module signature verification]

Enabling support is a matter of toggling a few settings in the Linux kernel configuration. Unless you want to use your own keypair, this is all that has to be done to enable kernel module signature verification support.

The certificates and signing files used to manually sign modules are available at [/usr/src/linux/certs/].

### [Configuring module signature verification]

Module signature verification is a kernel feature, so it has to be enabled through the Linux kernel configuration. You can find the necessary options under *Enable loadable module support*.

[KERNEL] **Enable module signature verification**

    [*] Enable loadable module support  --->
      [*]   Module signature verification
      [*]     Require modules to be validly signed
      [*]     Automatically sign all modules
            Which hash algorithm should modules be signed with? (Sign modules with SHA-512) --->

The option *Module signature verification* (`CONFIG_MODULE_SIG`) enables the module signature verification in the Linux kernel. It supports two approaches on signed module support: a rather permissive one and a strict one. By default, the permissive approach is used, which means that the Linux kernel module either has to have a valid signature, or no signature. With the strict approach, a valid signature must be present. In the above example, the strict approach is used by selecting *Require modules to be validly signed* (`CONFIG_MODULE_SIG_FORCE`). Another way of enabling this strict approach is to set the kernel boot option `module.sig_enforce=1`.

When building the Linux kernel, the kernel modules will not be signed automatically unless you select *Automatically sign all modules* (`CONFIG_MODULE_SIG_ALL`).

Finally, we need to select the hash algorithm to use with the cryptographic signature. In the above example, we use SHA-512.

### [Building the kernel with proper keys]

#### [Generating keys by default]

When the Linux kernel is built with module signature verification support enabled, the Linux kernel build infrastructure will create a set of keys by default. To use these keys, just build the kernel as typical with [make] and [make modules_install]. At the end of the build process, [/certs/signing_key.pem] and [signing_key.x509] will be available on the root of the Linux kernel sources.

#### [Using Secure Boot keys]

On a system using [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot"), the [db private key](https://wiki.gentoo.org/wiki/Secure_Boot#Components "Secure Boot") is used to sign the kernel image, and the firmware uses the public key to verify the kernel image. If the user installed custom Secure Boot keys and has access to the db keys, those keys may be suitable for module signing.

#### [Generating keys directly]

Alternatively, to create custom module-signing keys, use [openssl] to create a key pair (private key and public key). The following command, taken from [kernel/Makefile], creates such a key pair. Currently only RSA keys are supported, but support for ECDSA signature verification was added in 2021.^[\[1\]](#cite_note-ECDSA-1)[\[2\]](#cite_note-ECDSA2-2)^

x509.genkey is located at [/usr/src/linux/certs/x509.genkey].

[FILE] **`x509.genkey`Key generation configuration file**

    [ req ]
    default_bits = 4096
    distinguished_name = req_distinguished_name
    prompt = no
    string_mask = utf8only
    x509_extensions = myexts

    [ req_distinguished_name ]
    CN = Modules

    [ myexts ]
    basicConstraints=critical,CA:FALSE
    keyUsage=digitalSignature
    subjectKeyIdentifier=hash
    authorityKeyIdentifier=keyid

`user `[`$`]`openssl req -new -nodes -utf8 -sha512 -days 36500 -batch -x509 -config x509.genkey -outform DER -out signing_key.x509 -keyout signing_key.priv`

The resulting files need to be stored as [signing_key.x509] and [/certs/signing_key.pem] in the root of the Linux kernel source tree.

The public key part will be built into the Linux kernel. If the kernel is configured to sign modules, signing will take place during the [make modules_install] step.

### [Validation]

#### [Kernel certificates]

Reboot with the newly configured kernel. In the output of [dmesg] you should be able to confirm that the proper certificate is loaded:

`root `[`#`]`dmesg | grep -i 'x.*509'`

    [    1.279874] Asymmetric key parser 'x509' registered
    [    1.286431] Loading compiled-in X.509 certificates
    [    1.292031] Loaded X.509 cert 'Modules: b03b5edb5700f9d5d785eb2d6f3e19d34a20205b'

If `CONFIG_KEYS_DEBUG_PROC_KEYS` is enabled, then root user can view certificate in [/proc/keys] file:

`root `[`#`]`cat /proc/keys`

    011aee9c I------     1 perm 1f030000     0     0 asymmetri Modules: b03b5edb5700f9d5d785eb2d6f3e19d34a20205b: X509.RSA 4a20205b []
    0b5726c7 I--Q---     1 perm 1f3f0000     0 65534 keyring   _uid_ses.0: 1
    0b6539f7 I------     1 perm 1f0b0000     0     0 keyring   .system_keyring: 1
    3b688504 I--Q---     2 perm 1f3f0000     0 65534 keyring   _uid.0: empty

#### [Module signatures]

To confirm that a loaded module is signed, run:

`root `[`#`]`modinfo -F signer modulename`

More fully:

`user `[`$`]`modinfo usbcore | grep '^sig'`

    signer:         Modules
    sig_key:        B0:3B:5E:DB:57:00:F9:D5:D7:85:EB:2D:6F:3E:19:D3:4A:20:20:5B
    sig_hashalgo:   sha512

** Important**\
[modinfo] from the [[[sys-apps/kmod]](https://packages.gentoo.org/packages/sys-apps/kmod)[]] package must be built with the [pkcs7] USE flag to display the module signature.

#### [Kernel taint]

The Linux kernel may report itself to be \"tainted\" for various reasons, most of which are outside the scope of this article. Each reason, when it occurs, sets a flag in [/proc/sys/kernel/tainted], and the user can see all of the flag values by reading this file:

`user `[`$`]`cat /proc/sys/kernel/tainted`

4097

Loading an unsigned kernel module will set the flag at bit 13 with value 8192. If this flag is not set, as in the above example, then no unsigned modules have been loaded.^[\[3\]](#cite_note-3)^

#### [Directly checking module signatures]

The kernel modules have the digital signature appended at the end. A simple [hexdump] can confirm if a signature is present or not:

`user `[`$`]`hexdump -C vxlan.ko | tail`

    00008880  cf 0e e7 cb 10 9e 98 5f  4b 21 d4 03 ba 3d 7e e7  |......._K!...=~.|
    00008890  68 db f9 e3 5f 62 3c c7  d6 6c 84 c7 d6 68 c1 73  |h..._b<..l...h.s|
    000088a0  3d d7 5a 38 66 99 12 b8  84 c9 84 45 dd 68 6d 17  |=.Z8f......E.hm.|
    000088b0  03 24 dc 9c 6f 6d 11 01  e9 74 82 ea b5 5b 46 07  |.$..om...t...[F.|
    000088c0  fe dd 66 97 1a 33 58 3d  6e d0 ac 03 08 16 73 06  |..f..3X=n.....s.|
    000088d0  9f 90 c4 eb b3 82 1d 9f  48 8c 5b 51 01 06 01 1e  |........H.[Q....|
    000088e0  14 00 00 00 00 00 02 02  7e 4d 6f 64 75 6c 65 20  |........~Module |
    000088f0  73 69 67 6e 61 74 75 72  65 20 61 70 70 65 6e 64  |signature append|
    00008900  65 64 7e 0a                                       |ed~.|
    00008904

The string `~Module signature appended~` at the end confirms that *a signature* is present. Of course, it does not confirm that the signature is valid or not.

To remove the signature, we can use the [strip] command:

`root `[`#`]`strip --strip-debug vxlan.ko `

`root `[`#`]`hexdump -C vxlan.ko | tail`

    00097330  6c 5f 67 65 74 5f 73 74  61 74 73 36 34 00 72 63  |l_get_stats64.rc|
    00097340  75 5f 62 61 72 72 69 65  72 00 5f 72 61 77 5f 73  |u_barrier._raw_s|
    00097350  70 69 6e 5f 75 6e 6c 6f  63 6b 00 72 65 67 69 73  |pin_unlock.regis|
    00097360  74 65 72 5f 70 65 72 6e  65 74 5f 64 65 76 69 63  |ter_pernet_devic|
    00097370  65 00 6b 6d 61 6c 6c 6f  63 5f 63 61 63 68 65 73  |e.kmalloc_caches|
    00097380  00 6e 65 74 64 65 76 5f  69 6e 66 6f 00 6e 65 69  |.netdev_info.nei|
    00097390  67 68 5f 6c 6f 6f 6b 75  70 00 72 65 6c 65 61 73  |gh_lookup.releas|
    000973a0  65 5f 73 6f 63 6b 00 72  65 67 69 73 74 65 72 5f  |e_sock.register_|
    000973b0  6e 65 74 64 65 76 69 63  65 00                    |netdevice.|
    000973ba

If we try to load this module now, we get a failure:

`root `[`#`]`modprobe vxlan`

    modprobe: ERROR: could not insert 'vxlan': Required key not available

This confirms that modules without a signature cannot be loaded.

## [Administering kernel module signatures]

Once the kernel boots and we have validated that the signed kernel module support works, it is important to correctly handle the keys themselves.

### [Protecting the private key]

The private key, stored as [/certs/signing_key.pem], needs to be moved to a secure location (unless you will be creating new keys for new kernels, in which case the file can be removed). Do not keep it at [/usr/src/linux] on production systems as malware can then easily use this key to sign the malicious kernel modules (such as rootkits) and compromise the system further.

The best way to do this is to move the key to a USB stick that you will unplug from your computer after it has been moved. That way if you update a driver such as your graphics drivers which do not require a kernel re-compile you can insert the USB stick for that moment to sign your driver modules and unplug it after you have done so.

Other methods include technology such as a TPM yet these are not favored by many as the TPM module is burnt from manufacture with a key that the manufacturer has control over.

### [Manually signing modules]

If you ever need to manually sign a kernel module, you can use the [scripts/sign-file] script available in the Linux kernel source tree. It requires four arguments:

1.  The hash algorithm to use, such as [sha512].
2.  The private key location.
3.  The certificate (which includes the public key) location.
4.  The kernel module to sign.

In this case, the key pair does not need to be named [signing_file.priv] and such, nor do they need to be in the root of the Linux kernel source tree location.

`root `[`#`]`/usr/src/linux/scripts/sign-file sha512 /usr/src/linux/kernel-signkey.priv /usr/src/linux/kernel-signkey.x509 vxlan.ko`

The location of the certificates is [/usr/src/linux/certs] directory.

See command below:

`root `[`#`]`/usr/src/linux/scripts/sign-file sha512 /usr/src/linux/certs/signing_key.pem /usr/src/linux/certs/signing_key.x509 vxlan.ko`

### [][Automatically signing kernel modules (Portage)]

`linux-mod-r1.eclass` as well as the [distribution kernels](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") have native support for signing kernel modules via the [[[modules-sign]](https://packages.gentoo.org/useflags/modules-sign)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag"). The pre-built distribution kernels (e.g. [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]]) contain pre-signed modules as of version 6.4.13. However, enforcing of valid module signatures is not enabled by default for the pre-built kernels, this can be enabled with the `module.sig_enforce=1` kernel command line argument or by enabling [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot").

** Warning**\
When using the pre-built [distribution kernels](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") (e.g. [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]]), the key that was used to sign the in-tree modules will not be available for signing out-of-tree modules. Therefore, if module signatures are enforced on these kernels, any out-of-tree modules must be signed with a different key. The public certificate for these out-of-tree modules must be loaded into the kernel keychain; [keyctl] may be used for this purpose, though the effect is not persistent across reboots. To persistently add additional certificates to the keychain, [Shim](https://wiki.gentoo.org/wiki/Shim "Shim") must be used.

### [Distributing the kernel and modules]

If we create a kernel package through [make tarbz2-pkg], the modules in it will be signed already so we do not need to manually sign them afterwards. The signing keys themselves are not distributed with it.

## [See also]

-   [Kernel Modules](https://wiki.gentoo.org/wiki/Kernel_Modules "Kernel Modules") --- object files that contain code to extend the [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") of an operating system.

## [References]

1.  [[[↑](#cite_ref-ECDSA_1-0)] [[https://lwn.net/Articles/847441/](https://lwn.net/Articles/847441/)]]
2.  [[[↑](#cite_ref-ECDSA2_2-0)] [[https://patchwork.kernel.org/project/linux-integrity/patch/20210215162532.1077098-2-stefanb@linux.ibm.com/](https://patchwork.kernel.org/project/linux-integrity/patch/20210215162532.1077098-2-stefanb@linux.ibm.com/)]]
3.  [[[↑](#cite_ref-3)] [[Tainted kernels](https://docs.kernel.org/admin-guide/tainted-kernels.html), [The Linux Kernel documentation](https://docs.kernel.org/index.html). Retrieved on 2025-05-31.]]

## [External resources]

-   [Kernel module signing facility](https://www.kernel.org/doc/html/latest/admin-guide/module-signing.html) - Linux Kernel documentation on module signing.
-   [Booting a self-signed Linux kernel](http://www.kroah.com/log/blog/2013/09/02/booting-a-self-signed-linux-kernel/) - Greg Kroah-Hartman describes how to boot a self-signed Linux kernel from EFI. As having signed kernel module support is only secure if the Linux kernel is trusted, this is an important (and related) feature to work with.