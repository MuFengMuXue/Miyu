**Resources**

[[]][Home](http://ecryptfs.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/ECryptfs "wikipedia:ECryptfs")

[[]][Package information](https://packages.gentoo.org/packages/sys-fs/ecryptfs-utils)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/eCryptfs)

\

** Note**\
ECryptfs development is stalled. The latest stable release of the userland tools was released in 2016. The kernel code is still actively maintained.

**eCryptfs** is an in-kernel file encryption suite. It supports diffferent symmetric encryption algorithms depending on the Kernel\'s crypto API. In contrast to [LUKS](https://wiki.gentoo.org/wiki/DM-Crypt_LUKS "DM-Crypt LUKS") encryption happens per file. Encryption meta data is added to the file header. ECryptfs consists of a Linux kernel module and a set of userland tools.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [USE flags]](#USE_flags)
    -   [[2.3] [Emerge]](#Emerge)
    -   [[2.4] [Load the eCryptfs module]](#Load_the_eCryptfs_module)
    -   [[2.5] [Verify kernel support for eCryptfs]](#Verify_kernel_support_for_eCryptfs)
-   [[3] [Key management]](#Key_management)
    -   [[3.1] [Creating a passphrase protected keyfile]](#Creating_a_passphrase_protected_keyfile)
    -   [[3.2] [Using a keyfile]](#Using_a_keyfile)
    -   [[3.3] [Changing the passphrase of a keyfile]](#Changing_the_passphrase_of_a_keyfile)
    -   [[3.4] [Working with kernel keys]](#Working_with_kernel_keys)
    -   [[3.5] [Managing the kernel keystore]](#Managing_the_kernel_keystore)
    -   [[3.6] [Using PAM]](#Using_PAM)
-   [[4] [Using fstab]](#Using_fstab)
-   [[5] [Encrypting swap]](#Encrypting_swap)
-   [[6] [Mount Remote Directory]](#Mount_Remote_Directory)
-   [[7] [Hints and Criticism]](#Hints_and_Criticism)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)

## [Introduction]

ECryptfs works with the same concept of a *lower* and an *upper* layer as [OverlayFS](https://wiki.gentoo.org/wiki/OverlayFS "OverlayFS"). The lower layer can be a directory on a mounted file system and will be encrypted. It can be mounted using type *ecryptfs*, onto an empty directory to form the upper layer. The upper layer is read/write: when files are read they are decrypted from the lower layer, and files are written to they are on the fly encrypted on the lower layer. Once the upper layer is unmounted only the encrypted lower layer remains.

An interactive example with an encrypted lower layer [/tmp/enc] and an upper decrypted layer [/tmp/dec] would be:

`root `[`#`]`mkdir /tmp/enc /tmp/dec `

`root `[`#`]`mount -t ecryptfs /tmp/enc /tmp/dec `

    Select key type to use for newly created files:
     1) passphrase
     2) openssl
    Selection: 1
    Passphrase:
    Select cipher:
     1) aes: blocksize = 16; min keysize = 16; max keysize = 32
     2) blowfish: blocksize = 8; min keysize = 16; max keysize = 56
     3) des3_ede: blocksize = 8; min keysize = 24; max keysize = 24
     4) twofish: blocksize = 16; min keysize = 16; max keysize = 32
     5) cast6: blocksize = 16; min keysize = 16; max keysize = 32
     6) cast5: blocksize = 8; min keysize = 5; max keysize = 16
    Selection [aes]: 1
    Select key bytes:
     1) 16
     2) 32
     3) 24
    Selection [16]: 2
    Enable plaintext passthrough (y/n) [n]: y
    Enable filename encryption (y/n) [n]:
    Attempting to mount with the following options:
      ecryptfs_unlink_sigs
      ecryptfs_passthrough
      ecryptfs_key_bytes=32
      ecryptfs_cipher=aes
      ecryptfs_sig=7a1719eb53966dd1
    WARNING: Based on the contents of [/root/.ecryptfs/sig-cache.txt],
    it looks like you have never mounted with this key
    before. This could mean that you have typed your
    passphrase wrong.

    Would you like to proceed with the mount (yes/no)? : yes
    Would you like to append sig [7a1719eb53966dd1] to
    [/root/.ecryptfs/sig-cache.txt]
    in order to avoid this warning in the future (yes/no)? : yes
    Successfully appended new sig to user sig cache file
    Mounted eCryptfs

A quick demo where a small file is being encypted on the fly:

`root `[`#`]`echo "xxx" > /tmp/dec/xxx `

`root `[`#`]`file /tmp/dec/xxx /tmp/enc/xxx `

    /tmp/dec/xxx: ASCII text
    /tmp/enc/xxx: FILE_SIZE=12288

Note that, if *plaintext passthrough* is enabled, anything written to the lower layer will bypass encryption and decryption:

`root `[`#`]`echo "some text" > /tmp/enc/cleartext `

`root `[`#`]`cat /tmp/dec/cleartext /tmp/enc/cleartext`

    some text
    some text

## [Installation]

### [Kernel]

ECryptfs needs its module, key retention, and desired ciphers enabled in the Linux kernel. Currently supported ciphers are aes, blowfish, des3_ede, cast5, cast6, and twofish. Make sure to select appropriate hardware accelerated ciphers for the target computer, e.g. *AES-NI*.

[KERNEL] **Enable eCryptfs support**

    Processor type and features  --->
        Processor family (AMD Zen 3)      (select appropriate target CPU if USE=experimental for gentoo-sources)
    File systems  --->
        [*] Miscellaneous filesystems  --->
            <M> eCrypt filesystem layer support
                [*] Enable notifications for userspace key wrap/unwrap
    Security options  --->
        [*] Enable access key retention support
    Cryptographic API  --->
        *** Block modes ***
        <M> CBC support
        <M> ECB support
        *** Digest ***
        <M> MD5 digest algorithm
        *** Ciphers ***
        <M> AES cipher algorithms
        <M> AES cipher algorithms (AES-NI)
        <M> Blowfish cipher algorithm
        <M> Blowfish cipher algorithm (x86_64)
         CAST5 (CAST-128) cipher algorithm
        <M> CAST5 (CAST-128) cipher algorithm (x86_64/AVX)
         CAST6 (CAST-256) cipher algorithm
        <M> CAST6 (CAST-256) cipher algorithm (x86_64/AVX)
        <M> DES and Triple DES EDE cipher algorithms
        <M> Triple DES EDE cipher algorithm (x86-64)
        <M> Twofish cipher algorithm
         Twofish cipher algorithm (x86_64)
         Twofish cipher algorithm (x86_64, 3-way parallel)
        <M> Twofish cipher algorithm (x86_64/AVX)

### [USE flags]

### [USE flags for] [sys-fs/ecryptfs-utils](https://packages.gentoo.org/packages/sys-fs/ecryptfs-utils) [[]] [eCryptfs userspace utilities]

  ----------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gpg`](https://packages.gentoo.org/useflags/gpg)           Enable app-crypt/gnupg key module
  [`gtk`](https://packages.gentoo.org/useflags/gtk)           Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`nls`](https://packages.gentoo.org/useflags/nls)           Add Native Language Support (using gettext - GNU locale utilities)
  [`openssl`](https://packages.gentoo.org/useflags/openssl)   Enable dev-libs/openssl key module
  [`pam`](https://packages.gentoo.org/useflags/pam)           Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`pkcs11`](https://packages.gentoo.org/useflags/pkcs11)     Enable PKCS#11 (Smartcards) key module
  [`suid`](https://packages.gentoo.org/useflags/suid)         Enable setuid root program(s)
  [`tpm`](https://packages.gentoo.org/useflags/tpm)           Enable support for Trusted Platform Module (TPM) using app-crypt/trousers
  ----------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2024-01-05 14:02] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[sys-fs/ecryptfs-utils]](https://packages.gentoo.org/packages/sys-fs/ecryptfs-utils)[]]:

`root `[`#`]`emerge --ask sys-fs/ecryptfs-utils`

** Note**\
[[[sys-fs/ecryptfs-utils]](https://packages.gentoo.org/packages/sys-fs/ecryptfs-utils)[]] must be compiled with the `suid` USE flag in order to use the auto-mount capabilities of PAM as described below. Getting rid of setuid and/ or fixing general mounts see [[[bug #829576]](https://bugs.gentoo.org/show_bug.cgi?id=829576)[]]. Otherwise mounting arbitrary directories requires user mounts based on [/etc/fstab]. Section Mount Remote Directory shows how to do this.

### [Load the eCryptfs module]

Most of the eCryptfs tools will load the eCryptfs module when needed, but in specific cases it may be necessary to load the module explicitly:

`root `[`#`]`modprobe ecryptfs`

Add ecryptfs to [/etc/modules-load.d/ecryptfs] if the module should be loaded always after booting the system:

`root `[`#`]`echo ecryptfs >> /etc/modules-load.d/ecryptfs`

### [Verify kernel support for eCryptfs]

The Linux kernel maintains a list of supported file systems at [/proc/filesystems]. Verify eCryptfs support as follows:

`user `[`$`]`grep ecryptfs /proc/filesystems`

    nodev   ecryptfs

## [Key management]

Using a passphrase as an encryption key, as was done in the example in the introduction, while practical, has the disadvantage that the passphrase can never be changed. The best practice to regularly change passphrases would not be possible in such a setup. unless the whole contents of a encrypted directory would be re-encrypted with a different encryption key. This is not convenient and may take too much time for larger volumes of data.

In order to cater for changing passphrases for encryption, aka *rekeying*, ECryptfs has the possibility to work with encrypted encryption keys. ECryptfs calls this wrapped passphrases. These wrapped passphrases are stored in a file, a keyfile, and are protected with a passphrase. The passphrase for the keyfile can be changed, and this is how rekeying is possible.

### [Creating a passphrase protected keyfile]

The procedure is to create a safe location for a keyfile, protect it so that only root can access it, and call [ecryptfs-wrap-passphrase]:

`root `[`#`]`mkdir -p /root/.ecryptfs `

`root `[`#`]`chmod 700 /root/.ecryptfs `

`root `[`#`]`ecryptfs-wrap-passphrase /root/.ecryptfs/keyfile.ecryptfs `

    Passphrase to wrap:
    Wrapping passphrase:

The *Passphrase to wrap* is the encryption key. The *Wrapping passphrase* is the passphrase that will be used to protect the encrypted encryption key. The result is stored in [/root/.ecryptfs/keyfile.ecryptfs]

The encryption key can be quite complicated but must be less the 64 characters. It can be completely random and sourced from [/dev/urandom], but needs to be encoded to s string before it can be used by [ecryptfs-wrap-passphrase].

The following python script may be useful to randomize a 50 character encryption key and feed it to [ecryptfs-wrap-passphrase].

[FILE] **`/root/.ecryptfs/gen_keyfile.py`**

    import string, secrets, getpass
    wrapping_passphrase = getpass.getpass("Passphrase:")
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()-_=+[];<>?.'
    encryption_key = ''.join(secrets.choice(alphabet) for i in range(50))
    print(f"\n")

Use it as follows:

`root `[`#`]`cd /root/.ecryptfs `

`root `[`#`]`python gen_keyfile.py | ecryptfs-wrap-passphrase keyfile.ecryptfs`

    Passphrase:
    Passphrase to wrap:
    Wrapping passphrase:

### [Using a keyfile]

The keyfile generated can be used for mounting. To test it out, unmount [/tmp/dec], and [/tmp/dec] and [/tmp/enc], assuming that this was just used for test and that nothing valuable is in there. Then create these directories again, and mount the encrypted [/tmp/enc] on [/tmp/dec] using the keyfile:

`root `[`#`]`umount /tmp/dec `

`root `[`#`]`rm -rf /tmp/dec /tmp/enc `

`root `[`#`]`mkdir /tmp/dec /tmp/enc `

`root `[`#`]`mount -t ecryptfs /tmp/enc /tmp/dec -o key=passphrase:passwd_file=/root/.ecryptfs/keyfile.ecryptfs"`

    Passphrase:
    Select cipher:
     1) aes: blocksize = 16; min keysize = 16; max keysize = 32
     2) blowfish: blocksize = 8; min keysize = 16; max keysize = 56
     3) des3_ede: blocksize = 8; min keysize = 24; max keysize = 24
     4) twofish: blocksize = 16; min keysize = 16; max keysize = 32
     5) cast6: blocksize = 16; min keysize = 16; max keysize = 32
     6) cast5: blocksize = 8; min keysize = 5; max keysize = 16
    Selection [aes]: 1
    Select key bytes:
     1) 16
     2) 32
     3) 24
    Selection [16]: 1
    Enable plaintext passthrough (y/n) [n]: y
    Enable filename encryption (y/n) [n]:
    Attempting to mount with the following options:
      ecryptfs_unlink_sigs
      ecryptfs_passthrough
      ecryptfs_key_bytes=16
      ecryptfs_cipher=aes
      ecryptfs_sig=45d18b267ac3e929
    Mounted eCryptf

### [Changing the passphrase of a keyfile]

Call [ecryptfs-rewrap-passphrase] to update the encryption key to use a new passphrase:

`root `[`#`]`ecryptfs-rewrap-passphrase /root/.ecryptfs/keyfile.ecryptfs`

    Old wrapping passphrase:
    New wrapping passphrase:
    New wrapping passphrase (again):

### [Working with kernel keys]

It is possible to store passphrases in the Linux kernel keystore. Once a key is insterted in the kernel, mounting of en eCryptfs encrypted directory can be done without providing a passphrase. ECryptfs provides a utility called [ecryptfs-add-passphrase] to do this:

`root `[`#`]`ecryptfs-add-passphrase`

    Passphrase:
    Inserted auth tok with sig [45d18b267ac3e929] into the user session keyring

It is also possible to pipe a passphrase into ecryptfs-add-passphrase.

Note the signature *45d18b267ac3e929*, which, when the same passphrase was used, is the same as the signature as seen when the encrypted directory was first mounted.

This signature can now be used for the mount. To demonstrate that:

`root `[`#`]`umount /tmp/dec /tmp/enc `

`root `[`#`]`mount -i -t ecryptfs /tmp/enc /tmp/dec -o ecryptfs_sig=45d18b267ac3e929,ecryptfs_cipher=aes,ecryptfs_key_bytes=16,ecryptfs_unlink_sigs `

`root `[`#`]`echo "xxxxx" > /tmp/dec/xxxxx `

`root `[`#`]`file /tmp/dec/xxxxx /tmp/enc/xxxxx`

    /tmp/dec/xxxxx: ASCII text
    /tmp/enc/xxxxx: FILE_SIZE=12288

ECryptfs retrieved the passphrase from the kernel, and it did not need to be entered interactively. The other required mount parameters were added on the commandline to prevent in interactive dialog. Note the **-i** option for the mount, which prevents the calling of the *helper function*, which would still try to mount interactively.

### [Managing the kernel keystore]

The command [keyctl] can be used to manage the kernel keystore. In the kernel keystore, keys are added to keyrings. ECryptfs keys are added to the *user keyring*, referred to as *\@u*:

`root `[`#`]`keyctl list @u`

    1 key in keyring:
    583211167: --alswrv     0     0 user: 45d18b267ac3e929

If a key is no longer required then it can be removed:

`root `[`#`]`keyctl unlink 583211167 @u `

`root `[`#`]`keyctl list @u`

    keyring is empty

If no keys are required anymore then the complete user keyring can be cleared out with [keyctl clear \@u].

### [Using PAM]

[PAM](https://wiki.gentoo.org/wiki/PAM "PAM") can be used for automatically adding keyphrases to the kernel key store. See the below diff for the [system-auth] file.

`diff -u /etc/pam.d/system-auth.orig /etc/pam.d/system-auth`

    --- /etc/pam.d/system-auth  2021-12-13 02:23:28.094220446 -0500
    +++ /etc/pam.d/system-auth  2021-12-13 02:28:04.886740693 -0500
    @@ -3,6 +3,7 @@
     auth            [success=1 default=ignore]      pam_unix.so nullok  try_first_pass
     auth       [default=die]   pam_faillock.so authfail
     auth       optional    pam_cap.so
    +auth       optional    pam_ecryptfs.so unwrap
     account        required    pam_unix.so
     account         required        pam_faillock.so
     password   required    pam_passwdqc.so config=/etc/security/passwdqc.conf
    @@ -10,3 +11,4 @@
     session        required    pam_limits.so
     session        required    pam_env.so
     session        required    pam_unix.so
    +session        optional    pam_ecryptfs.so unwrap

When a user logs in, PAM will enter the user\'s password to the kernel keyring. ECryptfs can then retrieve the passphrase based on the signature. This will only work if the login password is the same as the eCryptfs passphrase.

## [Using fstab]

An eCryptfs encrypted directory can be added to [/etc/fstab] so that ordinary users can mount them. The procedure is to mount the directory first as root and then capture the mount options from [/etc/mtab]:

`root `[`#`]`grep /home/user/.private /etc/mtab`

    /home/user/.private /home/user/private ecryptfs key=passphrase:passwd_file=/home/user/.ecryptfs/keyfile.ecryptfs,rw,relatime,ecryptfs_sig=45d18b267ac3e929,ecryptfs_cipher=aes,ecryptfs_key_bytes=16 0 0

This can then be added to [/etc/fstab], adding \"noauto\" and \"user\" to the mount options:

[FILE] **`/etc/fstab`**

    ..
    /home/user/.private /home/user/private ecryptfs noauto,user,key=passphrase:passwd_file=/home/user/.ecryptfs/keyfile.ecryptfs,rw,relatime,ecryptfs_sig=45d18b267ac3e929,ecryptfs_cipher=aes,ecryptfs_key_bytes=16 0 0
    ..

A user is then able to mount this directory after adding their passphrase to they kernel keyring. When PAM is used for adding the passphrase to the kernel keyring, the mount could be done automatically after login from a login script (e.g. [\~/.bashrc]) or a desktop autostart facility.

Note that ordinary users are not allowed to provide mount options; Users would have to have the system administrator change the *ecryptfs_sig* mount option when they change their passphrase.

## [Encrypting swap]

Ecryptfs-utils has a utility [ecryptfs-setup-swap] which depends on [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]]. However, this utility is currently Ubuntu centric. To setup an encrypted swap, install [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]] and edit [/etc/conf.d/dmcrypt] which has an example of an encrypted swap in it.

[FILE] **`/etc/conf.d/dmcrypt`crypt-swap example**

    swap=crypt-swap
    source=/dev/sda3
    options='--cipher=aes-xts-plain64 --key-size=512 --key-file=/dev/urandom'

Add dm-crypt to the boot run level with:

`root `[`#`]`rc-config add dmcrypt boot`

For a version of [ecryptfs-setup-swap] which works with gentoo, see [\[1\]](https://github.com/oz123/dude/blob/master/gentoo/bin/ecryptfs-setup-swap).

## [Mount Remote Directory]

** Note**\
Current version of ecryptfs ships with an unusable [mount.ecryptfs]. It will always complain that passwd details cannot be found for uid. Due to a lack of adaption since 2012, this helper is broken. Only direct invocation of [mount] works.

To bind and encrypt a remote directory, two stages are necessary. First, [[[net-fs/sshfs]](https://packages.gentoo.org/packages/net-fs/sshfs)[]] mounts the directory onto the local machine and provides transport encryption. Second, ecryptfs transparently encrypts and decrypts files. [NFS](https://wiki.gentoo.org/wiki/NFS "NFS") is an alternative but must be secured in transport and at rest, too.

1.  on the remote host create an empty directory
2.  on the local machine create a directory [.secret] and a second directory [secret]
3.  on the local machine mount the remote host\'s directory to [.secret]
4.  and add a passphrase to the Kernel\'s (user) keyring with [ecryptfs-add-passphrase]
5.  as root use the signature prompted from the previous command to create an entry in [/etc/fstab] with option user, so that user mount is possible
6.  as normal user [mount -i secret] so that encrypted directory becomes decrypted under [secret]
7.  when done, first [umount secret] which also removes the key from the keyring\...
8.  \... second [umount .secret] to disconnect from remote host

`user `[`$`]`ecryptfs-add-passphrase`

    Passphrase:
    Inserted auth tok with sig [28320aba320b22df] into the user session keyring

[FILE] **`/etc/fstab`**

    #mount with same passphrase for files and meta data
    /home/user/.secret  /home/user/secret   ecryptfs    user,noauto,ecryptfs_sig=28320aba320b22df,ecryptfs_fnek_sig=28320aba320b22df,ecryptfs_cipher=aes,ecryptfs_key_bytes=32,ecryptfs_unlink_sigs 0 0

Use [keyctl] to verify signatures of keys being loaded for current user. After [ecryptfs-add-passphrase], there will be more entries. The sample shows the signature from above plus two others. Also check that after [umount] of ecryptfs layer the signature is gone.

`user `[`$`]`keyctl list @u`

    3 keys in keyring:
    314829634: --alswrv  1000  1000 user: a9d767fe56ef6923
    225345633: --alswrv  1000  1000 user: 28320aba320b22df
    729098673: --alswrv  1000  1000 user: 277ff13fd4e56c3d

** Note**\
It is absolutely valid to mount different ecryptfs overlays with the same signature. It is not a problem when unmounting one of them erases the signature from the keyring. The second overlay stays fully functional.

## [Hints and Criticism]

-   available algorithms depend on Kernel API and configuration, check [/proc/crypto]
-   folder structure, number of files and file size clearly visible

## [See also]

-   [Mount Encrypted Ubuntu Home/Guide](https://wiki.gentoo.org/wiki/Mount_Encrypted_Ubuntu_Home/Guide "Mount Encrypted Ubuntu Home/Guide")

## [External resources]

-   [eCryptfs readme file](https://bazaar.launchpad.net/~ecryptfs/ecryptfs/trunk/view/head:/README)
-   [Linux kernel key retention service](https://docs.kernel.org/security/keys/core.html)
-   [Linux Journal: eCryptfs, a Stacked Cryptographic Filesystem](https://www.linuxjournal.com/article/9400)
-   [Arch Linux wiki, eCryptfs article](https://wiki.archlinux.org/index.php/ECryptfs)