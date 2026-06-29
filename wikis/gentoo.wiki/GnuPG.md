This page contains [[changes](https://wiki.gentoo.org/index.php?title=GnuPG&oldid=1422703&diff=1422977)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/GnuPG/es "GnuPG (3% translated)")
-   [français](https://wiki.gentoo.org/wiki/GnuPG/fr "GnuPG (0% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/GnuPG/it "GnuPG (1% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/GnuPG/hu "GnuPG (64% translated)")
-   [polski](https://wiki.gentoo.org/wiki/GnuPG/pl "GnuPG/pl (0% translated)")
-   [русский](https://wiki.gentoo.org/wiki/GnuPG/ru "GnuPG (24% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/GnuPG/zh-cn "GnuPG (2% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/GnuPG/ja "GnuPG (82% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/GnuPG/ko "GnuPG (2% translated)")

**Resources**

[[]][Home](https://gnupg.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_Privacy_Guard "wikipedia:GNU Privacy Guard")

[[]][Official documentation](https://www.gnupg.org/documentation/index.html)

[[]][GitWeb](https://git.gnupg.org/cgi-bin/gitweb.cgi)

**GnuPG (GNU Privacy Guard)**, also known as **GPG**, is a free implementation of the OpenPGP standard (RFC 4880). GPG supports both symmetric and public-key cryptography, and typically operates using both.

GPG can be used for digital signing, authentication, and encryption of data. It is often used to encrypt and sign email messages, but can also be used with files or plaintext.

GPG supports hardware security devices with an OpenPGP module, such as the [YubiKey](https://wiki.gentoo.org/wiki/YubiKey "YubiKey").

[[[app-crypt/gnupg]](https://packages.gentoo.org/packages/app-crypt/gnupg)[]] includes [gpg-agent] which can be used as an ssh-agent.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
        -   [[1.3.1] [GUI]](#GUI)
        -   [[1.3.2] [Mail clients]](#Mail_clients)
        -   [[1.3.3] [Other]](#Other)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [GPG Security]](#GPG_Security)
    -   [[2.2] [Pinentry]](#Pinentry)
        -   [[2.2.1] [pinentry-qt & KWallet]](#pinentry-qt_.26_KWallet)
        -   [[2.2.2] [pinentry-kwallet & KWallet]](#pinentry-kwallet_.26_KWallet)
    -   [[2.3] [Key management]](#Key_management)
        -   [[2.3.1] [Generating keys]](#Generating_keys)
            -   [[2.3.1.1] [Primary key]](#Primary_key)
            -   [[2.3.1.2] [Add a signing key]](#Add_a_signing_key)
            -   [[2.3.1.3] [Add an encryption key]](#Add_an_encryption_key)
            -   [[2.3.1.4] [Add an authentication key]](#Add_an_authentication_key)
        -   [[2.3.2] [Removing the secret primary key for safety]](#Removing_the_secret_primary_key_for_safety)
        -   [[2.3.3] [Exporting keys]](#Exporting_keys)
            -   [[2.3.3.1] [Listing keys]](#Listing_keys)
            -   [[2.3.3.2] [Public keys]](#Public_keys)
            -   [[2.3.3.3] [Private Keys]](#Private_Keys)
        -   [[2.3.4] [Importing keys]](#Importing_keys)
            -   [[2.3.4.1] [Gentoo release keys]](#Gentoo_release_keys)
            -   [[2.3.4.2] [Loading a key from stdin]](#Loading_a_key_from_stdin)
        -   [[2.3.5] [Signing keys]](#Signing_keys)
        -   [[2.3.6] [Exchanging keys with key servers]](#Exchanging_keys_with_key_servers)
            -   [[2.3.6.1] [Configuring a default key server]](#Configuring_a_default_key_server)
            -   [[2.3.6.2] [Sending keys to key servers]](#Sending_keys_to_key_servers)
            -   [[2.3.6.3] [Getting keys from key servers]](#Getting_keys_from_key_servers)
            -   [[2.3.6.4] [Refreshing existing keys]](#Refreshing_existing_keys)
    -   [[2.4] [GPG Agent]](#GPG_Agent)
        -   [[2.4.1] [Smart Card]](#Smart_Card)
    -   [[2.5] [Using gpg-agent for SSH]](#Using_gpg-agent_for_SSH)
        -   [[2.5.1] [Prior v2.3.7]](#Prior_v2.3.7)
        -   [[2.5.2] [From v2.3.7]](#From_v2.3.7)
    -   [[2.6] [Forwarding GPG Agent over SSH]](#Forwarding_GPG_Agent_over_SSH)
    -   [[2.7] [Changing pinentry for SSH logins]](#Changing_pinentry_for_SSH_logins)
    -   [[2.8] [Automatically starting the GPG agent]](#Automatically_starting_the_GPG_agent)
        -   [[2.8.1] [Generic]](#Generic)
        -   [[2.8.2] [KDE]](#KDE)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Signing]](#Signing)
        -   [[3.1.1] [Clear signing]](#Clear_signing)
        -   [[3.1.2] [Detached signature]](#Detached_signature)
    -   [[3.2] [Symmetric Encryption]](#Symmetric_Encryption)
        -   [[3.2.1] [Signed]](#Signed)
    -   [[3.3] [Asymmetric (Public Key) Encryption]](#Asymmetric_.28Public_Key.29_Encryption)
        -   [[3.3.1] [Signed]](#Signed_2)
    -   [[3.4] [Signature verification]](#Signature_verification)
        -   [[3.4.1] [Detached signature]](#Detached_signature_2)
    -   [[3.5] [Decryption]](#Decryption)
-   [[4] [GnuPG interfaces]](#GnuPG_interfaces)
    -   [[4.1] [Seahorse]](#Seahorse)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-crypt/gnupg](https://packages.gentoo.org/packages/app-crypt/gnupg) [[]] [The GNU Privacy Guard, a GPL OpenPGP implementation]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+alternatives`](https://packages.gentoo.org/useflags/+alternatives)   Install renamed, for compatibility with app-alternatives/gpg.
  [`+smartcard`](https://packages.gentoo.org/useflags/+smartcard)         Build scdaemon software. Enables usage of OpenPGP cards. For other type of smartcards, try app-crypt/gnupg-pkcs11-scd. Bring in dev-libs/libusb as a dependency; enable scdaemon.
  [`+tofu`](https://packages.gentoo.org/useflags/+tofu)                   Enable support for Trust on First use trust model; requires dev-db/sqlite.
  [`bzip2`](https://packages.gentoo.org/useflags/bzip2)                   Enable bzip2 compression support
  [`doc`](https://packages.gentoo.org/useflags/doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`ldap`](https://packages.gentoo.org/useflags/ldap)                     Add LDAP support (Lightweight Directory Access Protocol)
  [`nls`](https://packages.gentoo.org/useflags/nls)                       Add Native Language Support (using gettext - GNU locale utilities)
  [`readline`](https://packages.gentoo.org/useflags/readline)             Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                       Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tools`](https://packages.gentoo.org/useflags/tools)                   Install extra tools (including gpgsplit and gpg-zip).
  [`tpm`](https://packages.gentoo.org/useflags/tpm)                       Enable TPM support via app-crypt/tpm2-tss and build tpm2d.
  [`usb`](https://packages.gentoo.org/useflags/usb)                       Build direct CCID access for scdaemon; requires dev-libs/libusb.
  [`user-socket`](https://packages.gentoo.org/useflags/user-socket)       try a socket directory which is not removed by init manager at session end
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)         Verify upstream signatures on distfiles
  [`wks-server`](https://packages.gentoo.org/useflags/wks-server)         Install the wks-server
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 03:25] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-crypt/gnupg`

### [Additional software]

GnuPG can be used alone, but integrates with a wide variety of software.

#### [GUI]

-   KGPG ([[[kde-apps/kgpg]](https://packages.gentoo.org/packages/kde-apps/kgpg)[]]) --- a small program for [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") environment that allows for the generation of key pairs, importing keys from ASCII files, signing imported keys, exporting keys, among a few other nifty features.

#### [Mail clients]

-   PinePGP ([[[mail-client/pinepgp]](https://packages.gentoo.org/packages/mail-client/pinepgp)[]]).
-   [Mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt") ([[[mail-client/mutt]](https://packages.gentoo.org/packages/mail-client/mutt)[]]) --- a small but very powerful text-based mail client.
-   [Claws Mail](https://wiki.gentoo.org/wiki/Claws_Mail "Claws Mail") --- a powerful mail program which supports threading, GPG with GPGME, and automation.
-   Evolution ([[[mail-client/evolution]](https://packages.gentoo.org/packages/mail-client/evolution)[]]) --- a GNOME Microsoft Outlook work alike.
-   KMail ([[[kde-apps/kmail]](https://packages.gentoo.org/packages/kde-apps/kmail)[]]) --- [KDE](https://wiki.gentoo.org/wiki/KDE "KDE")\'s mail client.
-   Thunderbird ([[[mein-client/thunderbird]](https://packages.gentoo.org/packages/mein-client/thunderbird)[]]) --- Mozilla\'s mail client. OpenPGP was enabled by default from Thunderbird 78.2.1, released in August 2020.

#### [Other]

-   [Tor](https://wiki.gentoo.org/wiki/Tor "Tor") ([[[net-vpn/tor]](https://packages.gentoo.org/packages/net-vpn/tor)[]]) - can be used to contact keyservers anonymously.

## [Configuration]

GPG requires very little or no configuration to actually be used, most configuration tends to be centered around how the [gpg-agent] and [pinentry] behave. It is entirely optional, but recommended to adjust the [gpg] configuration at [\~/.gnupg/gpg.conf] to increase security.

### [GPG Security]

The following options are part of [GLEP 63](https://wiki.gentoo.org/wiki/Project:Infrastructure/Generating_GLEP_63_based_OpenPGP_keys#Step_3:_Update_gpg.conf "Project:Infrastructure/Generating GLEP 63 based OpenPGP keys"), some are already defaults:

-   [utf8-strings] - by default, GPG assumes arguments are encoded in the same character set as `display-charset`, setting this option makes GPG interpret arguments at `utf8`.
-   [fixed-list-mode] - default since GnuPG2.0.10 - Do not merge the `user ID` and primary key when using `--with-colon` output mode.
-   [keyid-format] - shows the `key ID` in the specified format, options with *0x* in front add that to the `key ID` to notate that it is hexadecimal.
-   [personal-digest-preferences] - Adjusts digest algorithm selection order, can be utilized to prefer stronger hash types when signing messages.
-   [default-preference-list] - Sets the preference list, used by `setpref` in the edit menu, can be utilized to prefer stronger methods.
-   [verify-options] - `show-uid-validity` is enabled by default, this option is used to adjust which types of validation are shown when keys are verified.
-   [list-option] - `show-uid-validity` is enabled by default, used to adjust which types of validation are shown when keys or signatures are listed.
-   [cert-digest-algo] - The digest algorithm that will be used when signing a key.
-   [s2k-cipher-algo] - The cipher algorithm which will be used by default for symmetric encryption.
-   [s2k-digest-algo] - The digest algorithm which will be used to mangle passphrases used for symmetric encryption.

[FILE] **`~/.gnupg/gpg.conf`Reference GLEP63 configuration**

    # Assume that command line arguments are given as UTF8 strings.
    utf8-strings

    # when outputting certificates, view user IDs distinctly from keys:
    fixed-list-mode

    # long keyids are more collision-resistant than short keyids (it's trivial to make a key
    # with any desired short keyid)
    # NOTE: this breaks kmail gnupg support!
    keyid-format 0xlong

    # when multiple digests are supported by all recipients, choose the strongest one:
    personal-digest-preferences SHA512 SHA384 SHA256 SHA224

    # preferences chosen for new keys should prioritize stronger algorithms:
    default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 BZIP2 ZLIB ZIP Uncompressed

    # You should always know at a glance which User IDs GPG thinks are legitimately bound to
    # the keys in the keyring:
    verify-options show-uid-validity
    list-options show-uid-validity

    # include an unambiguous indicator of which key made a signature:
    # (see http://thread.gmane.org/gmane.mail.notmuch.general/3721/focus=7234)
    # (and http://www.ietf.org/mail-archive/web/openpgp/current/msg00405.html)
    sig-notation issuer-fpr@notations.openpgp.fifthhorseman.net=%g

    # when making an OpenPGP certification, use a stronger digest than the default SHA1:
    cert-digest-algo SHA512
    s2k-cipher-algo AES256
    s2k-digest-algo SHA512

### [Pinentry]

[[[app-crypt/pinentry]](https://packages.gentoo.org/packages/app-crypt/pinentry)[]] is a helper application that [gpg-agent] uses to request the passphrase in a graphical window. It comes in many flavors, including: [gtk3], [qt6], [tty], and [curses].

** Note**\
Building [pinentry-curses] is recommended, as it is typically used as a fallback pinentry.

If [[[app-crypt/pinentry]](https://packages.gentoo.org/packages/app-crypt/pinentry)[]] was installed with more than frontend, it is possible to choose between them with the [eselect pinentry] command:

`root `[`#`]`eselect pinentry list`

    Available pinentry binary implementations:
      [1]   pinentry-gnome3
      [2]   pinentry-qt6 *
      [3]   pinentry-curses
      [4]   pinentry-tty

`root `[`#`]`eselect pinentry set pinentry-qt6`

** Note**\
[eselect pinentry] changes the symlink of [/usr/bin/pinentry] to the selected pinentry helper.

** Note**\
If GPG gives an error like:

`user `[`$`]`gpg -o /dev/null -s /etc/hostname`

    gpg: signing failed: pinentry error
    gpg: signing failed: pinentry error

then it can be fixed either by using one of [pinentry-tty] or [pinentry-curses], or by launching with [dbus-launch].

`user `[`$`]`dbus-launch gpg -o /dev/null -s /etc/hostname`

#### [][pinentry-qt & KWallet]

[pinentry-qt] is capable of storing passwords in KDE\'s [KWallet](https://wiki.gentoo.org/wiki/KDE#KWallet "KDE") (or in any Secret Service compatible keyring.)

Ensure [[[kde-frameworks/kwallet]](https://packages.gentoo.org/packages/kde-frameworks/kwallet)[]] is installed, then in System Settings (provided by [[[kde-plasma/systemsettings]](https://packages.gentoo.org/packages/kde-plasma/systemsettings)[]]), under **KDE Wallet**, make sure the following are checked:

-   Enable the KDE wallet subsystem
-   Use KWallet for the Secret Service interface

Next, configure [pinentry-qt] to use Secret Service by creating this file:

[FILE] **`/etc/profile.d/pinentry.sh`Make pinentry-qt use KWallet**

    export PINENTRY_KDE_USE_WALLET=1

Finally, **logout & restart** to make sure any lingering [gpg-agent] processes get the new configuration.

** Note**\
The instructions above don\'t seem to be working with any release of [KWallet](https://wiki.gentoo.org/wiki/KDE#KWallet "KDE"). The [next section](https://wiki.gentoo.org/wiki/GnuPG#pinentry-kwallet_.26_KWallet "GnuPG") provides an alternative method for storing GPG passphrases in KWallet.

#### [][pinentry-kwallet & KWallet]

[pinentry-kwallet] is also capable of storing passwords in KDE\'s [KWallet](https://wiki.gentoo.org/wiki/KDE#KWallet "KDE").

Ensure [[[kde-frameworks/kwallet]](https://packages.gentoo.org/packages/kde-frameworks/kwallet)[]] is installed, then in System Settings (provided by [[[kde-plasma/systemsettings]](https://packages.gentoo.org/packages/kde-plasma/systemsettings)[]]), under **KDE Wallet**, make sure the following are checked:

-   Enable the KDE wallet subsystem
-   Use KWallet for the Secret Service interface

The [GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") repo must be enabled in order to install [[[kde-apps/kwalletcli]](https://packages.gentoo.org/packages/kde-apps/kwalletcli)[]]. Follow the steps at [this wiki page](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users") to enable and sync the GURU repository.

[[[kde-apps/kwalletcli]](https://packages.gentoo.org/packages/kde-apps/kwalletcli)[]] can then be installed:

`root `[`#`]`emerge --ask --verbose kde-apps/kwalletcli`

To instruct [gpg-agent] to use [pinentry-kwallet], create the following file:

[FILE] **`~/.gnupg/gpg-agent.conf`Attach pinentry-kwallet to gpg-agent**

    pinentry-program /usr/bin/pinentry-kwallet

Finally, **logout & restart** to make sure any lingering [gpg-agent] processes get the new configuration.

** Note**\
[\~/.gnupg/gpg-agent.conf] overrides any settings applied with [eselect pinentry set]. Its contents must be commented out if [pinentry] selection is to be managed by [eselect pinentry] again.

** Warning**\
[[[kde-apps/kwalletcli]](https://packages.gentoo.org/packages/kde-apps/kwalletcli)[]] is not an official [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") package. It is part of the [MirBSD project](http://www.mirbsd.org/). Make sure to carefully assess whether it would be a wise decision to trust them with such an important aspect of system security.

### [Key management]

#### [Generating keys]

** Important**\
Gentoo Developers should follow [Gentoo Infrastructure\'s key generation instructions](https://wiki.gentoo.org/wiki/Project:Infrastructure/Generating_GLEP_63_based_OpenPGP_keys#How_to_generate_the_GLEP_63-compliant_OpenPGP_key "Project:Infrastructure/Generating GLEP 63 based OpenPGP keys").

[gpg \--full-generate-key] can be used to generate a basic keypair, but using [gpg \--expert \--full-generate-key] offers many useful options, such as separate sign/certify certificates.

** Note**\
The first time the **gpg** command is executed, the directory [\~/.gnupg] will be created along with [\~/.gnupg/pubring.kbx]

##### [Primary key]

The GPG key creation process can be started with:

`user `[`$`]`gpg --expert --full-generate-key`

[CODE] **Begin key generation**

    gpg (GnuPG) 2.2.40; Copyright (C) 2022 g10 Code GmbH
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Please select what kind of key you want:
       (1) RSA and RSA (default)
       (2) DSA and Elgamal
       (3) DSA (sign only)
       (4) RSA (sign only)
       (7) DSA (set your own capabilities)
       (8) RSA (set your own capabilities)
       (9) ECC and ECC
      (10) ECC (sign only)
      (11) ECC (set your own capabilities)
      (13) Existing key
      (14) Existing key from card
    Your selection? 11

**(11) ECC (set your own capabilities)** is selected, so this first generated key will only have the **certify** function. Additional subkeys may be created for **encryption**, **sign**, and/or **authentication** capabilities.

By default, the first key should have the **sign** and **certify** options set, remove the **sign** option with **s**:

[CODE] **Remove the **sign** function.**

    Possible actions for a ECDSA/EdDSA key: Sign Certify Authenticate
    Current allowed actions: Sign Certify

       (S) Toggle the sign capability
       (A) Toggle the authenticate capability
       (Q) Finished

    Your selection? s

[CODE] **Finish editing the primary key**

    Possible actions for a ECDSA/EdDSA key: Sign Certify Authenticate
    Current allowed actions: Certify

       (S) Toggle the sign capability
       (A) Toggle the authenticate capability
       (Q) Finished

    Your selection? q

After selecting **q**, **(1) Curve 25519**, or whatever key type is preferred can be selected.

[CODE] **Set key type**

    Please select which elliptic curve you want:
       (1) Curve 25519
       (3) NIST P-256
       (4) NIST P-384
       (5) NIST P-521
       (6) Brainpool P-256
       (7) Brainpool P-384
       (8) Brainpool P-512
       (9) secp256k1
    Your selection? 1

Once the primary key type is selected, there\'s an option to set the expiration date for the primary key. It is important to understand that the meaning of setting the expiration date for the primary key is different from the meaning of setting it for a subkey. In the case of a subkey, setting an expiration date can help with security because if its private key is leaked, the public key will eventually expire, minimizing the possible attack period. But this assumes that the subkey was kept separate from the primary key and the primary key was not compromised. However, as time passes and new attack vectors emerge, old unrevoked expired keys will be renewed and used by attackers. In the case of a primary key, the expiration date does not help with security because if the private key is leaked and its password is compromised, an attacker can renew the expired public key. The GNU Privacy Handbook recommends setting a primary key expiration date only in case the key and revocation certificate are lost (but not compromised). ^[\[1\]](#cite_note-1)^ Therefore, expiration cannot be a substitute for key revocation. An expiration date 3-1 years in the future is reasonable for moderate-high security.

** Important**\
If keys are lost or potentially compromised, the revocation certificate must be shared as expired keys can be renewed.

** Note**\
Setting the expiry to **0** makes the key never expire. ^[\[2\]](#cite_note-2)^

** Tip**\
It is possible to make the key expire on a specific date. This method should be preferred because it allows to keep an eye on expiration renewals. This method also allows to set a single expiration date for all subkeys, even those that will be created in the future.

[CODE] **Set the expiry**

    Please specify how long the key should be valid.
             0 = key does not expire
          <n>  = key expires in n days
          <n>w = key expires in n weeks
          <n>m = key expires in n months
          <n>y = key expires in n years
    Key is valid for? (0) 2026-01-01

Now that the key parameters have been defined, identification information must be provided.

** Note**\
It is possible to use names shorter than 5 characters with GPG by using `--allowfreeform-uid`, but this may cause issues when matching recipient names, requiring the fingerprint to be used instead of the key owner name.

Finally, a passphrase must be added to the key. This passphrase is important, because it is used to protect the private key.

[CODE] **GPG primary key creation output**

    gpg: /root/.gnupg/trustdb.gpg: trustdb created
    gpg: directory '/root/.gnupg/openpgp-revocs.d' created
    gpg: revocation certificate stored as '/root/.gnupg/openpgp-revocs.d/D2A5C10E2F7BAC36DDBC0AFCF980BCF1FADC7479.rev'
    public and secret key created and signed.

    pub   ed25519 2023-04-25 [SC]
          D2A5C10E2F7BAC36DDBC0AFCF980BCF1FADC7479
    uid                      Larry (wiki example key) <larry@gentoo.org>

** Important**\
Take note of where the revocation certificate is located, this can be used to revoke keys in the event of unauthorized key/passphrase access.

** Note**\
At this point, only the primary **\[C\]**ertify (key signing key) key has been created, typically **\[S\]**igning and **\[E\]**ncryption keys are created.

##### [Add a signing key]

To view and edit the created key, [gpg \--expert \--edit-key D2A5C10E2F7BAC36DDBC0AFCF980BCF1FADC7479] can be used. [gpg \--expert \--edit-key Larry] should also work, as long as **Larry** exists as a user in the detected keyrings.

`user `[`$`]`gpg --expert --edit-key D2A5C10E2F7BAC36DDBC0AFCF980BCF1FADC7479`

    gpg (GnuPG) 2.2.40; Copyright (C) 2022 g10 Code GmbH
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Secret key is available.

    sec  ed25519/F980BCF1FADC7479
         created: 2023-04-25  expires: never       usage: C
         trust: ultimate      validity: ultimate
    [ultimate] (1). Larry (wiki example key) <larry@gentoo.org>

[CODE] **Add a signing key**

    gpg> addkey
    Please select what kind of key you want:
       (3) DSA (sign only)
       (4) RSA (sign only)
       (5) Elgamal (encrypt only)
       (6) RSA (encrypt only)
       (7) DSA (set your own capabilities)
       (8) RSA (set your own capabilities)
      (10) ECC (sign only)
      (11) ECC (set your own capabilities)
      (12) ECC (encrypt only)
      (13) Existing key
      (14) Existing key from card
    Your selection? 10

[CODE] **Select key type (Curve25519)**

    Please select which elliptic curve you want:
       (1) Curve 25519
       (3) NIST P-256
       (4) NIST P-384
       (5) NIST P-521
       (6) Brainpool P-256
       (7) Brainpool P-384
       (8) Brainpool P-512
       (9) secp256k1
    Your selection? 1

** Important**\
Keys must be saved with the [save] command in gpg, quitting will not save generated keys.

##### [Add an encryption key]

`user `[`$`]`gpg --expert --edit-key D2A5C10E2F7BAC36DDBC0AFCF980BCF1FADC7479`

    gpg (GnuPG) 2.2.40; Copyright (C) 2022 g10 Code GmbH
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Secret key is available.

    sec  ed25519/F980BCF1FADC7479
         created: 2023-04-25  expires: never       usage: C
         trust: ultimate      validity: ultimate
    [ultimate] (1). Larry (wiki example key) <larry@gentoo.org>

[CODE] **Add an encryption key**

    gpg> addkey
    Please select what kind of key you want:
       (3) DSA (sign only)
       (4) RSA (sign only)
       (5) Elgamal (encrypt only)
       (6) RSA (encrypt only)
       (7) DSA (set your own capabilities)
       (8) RSA (set your own capabilities)
      (10) ECC (sign only)
      (11) ECC (set your own capabilities)
      (12) ECC (encrypt only)
      (13) Existing key
      (14) Existing key from card
    Your selection? 12

[CODE] **Select key type (Curve25519)**

    Please select which elliptic curve you want:
       (1) Curve 25519
       (3) NIST P-256
       (4) NIST P-384
       (5) NIST P-521
       (6) Brainpool P-256
       (7) Brainpool P-384
       (8) Brainpool P-512
       (9) secp256k1
    Your selection? 1

Like with the creation of the **sign** and **certify** key, an expiration date must be set, and GPG will prompt for the key password before adding the key.

** Important**\
Keys must be saved with the [save] command in gpg, quitting will not save generated keys.

##### [Add an authentication key]

An **Authentication** key must be created to use GPG keys for SSH.

The authentication key can be created with:

[CODE] **Create the authentication key**

    gpg> addkey
    Please select what kind of key you want:
       (3) DSA (sign only)
       (4) RSA (sign only)
       (5) Elgamal (encrypt only)
       (6) RSA (encrypt only)
       (7) DSA (set your own capabilities)
       (8) RSA (set your own capabilities)
      (10) ECC (sign only)
      (11) ECC (set your own capabilities)
      (12) ECC (encrypt only)
      (13) Existing key
      (14) Existing key from card
    Your selection? 11

    Possible actions for a ECDSA/EdDSA key: Sign Authenticate
    Current allowed actions: Sign

       (S) Toggle the sign capability
       (A) Toggle the authenticate capability
       (Q) Finished

    Your selection? s

    Possible actions for a ECDSA/EdDSA key: Sign Authenticate
    Current allowed actions:

       (S) Toggle the sign capability
       (A) Toggle the authenticate capability
       (Q) Finished

    Your selection? a

    Possible actions for a ECDSA/EdDSA key: Sign Authenticate
    Current allowed actions: Authenticate

       (S) Toggle the sign capability
       (A) Toggle the authenticate capability
       (Q) Finished

    Your selection? q
    Please select which elliptic curve you want:
       (1) Curve 25519
       (3) NIST P-256
       (4) NIST P-384
       (5) NIST P-521
       (6) Brainpool P-256
       (7) Brainpool P-384
       (8) Brainpool P-512
       (9) secp256k1
    Your selection? 1
    Please specify how long the key should be valid.
             0 = key does not expire
          <n>  = key expires in n days
          <n>w = key expires in n weeks
          <n>m = key expires in n months
          <n>y = key expires in n years
    Key is valid for? (0) 2026-01-01
    Is this correct? (y/N) y
    Really create? (y/N) y

** Important**\
Keys must be saved with the [save] command in gpg, quitting will not save generated keys.

#### [Removing the secret primary key for safety]

In this section, it is assumed that the primary key will only be used for certification and the rest of the operations (signing, authentication) are assumed to be performed using subkeys. Only in this case is it justified to extract the secret primary key and store it separately on another device (e.g. a flash drive). The primary key will only be required to create/renew keys or sign the keys of others. If the device is compromised in the future, only the subkeys will be compromised. This means that all keys that have been certified with the primary key will still be valid, and the damage will be limited to the scope of the subkeys, which will probably expire before the attacker can determine the password (best case scenario).

Extract the secret primary key (should be stored on another device):

`user `[`$`]`gpg --output secret.gpg --armor --export-secret-key D2A5C10E2F7BAC36DDBC0AFCF980BCF1FADC7479`

Extract the secret subkeys:

`user `[`$`]`gpg --output subkeys.gpg --armor --export-secret-subkeys D2A5C10E2F7BAC36DDBC0AFCF980BCF1FADC7479`

Remove all secret keys:

`user `[`$`]`gpg --delete-secret-keys D2A5C10E2F7BAC36DDBC0AFCF980BCF1FADC7479`

Import the extracted secret subkeys:

`user `[`$`]`gpg --import subkeys.gpg`

Ensure that only secret subkeys are present:

`user `[`$`]`gpg --list-secret-keys`

    sec#  ed25519 2024-08-25 [C] [expires: 2026-01-01]
          D2A5C10E2F7BAC36DDBC0AFCF980BCF1FADC7479
    uid           [ unknown] Larry
    ssb   ed25519 2024-08-25 [S] [expires: 2026-01-01]
    ssb   ed25519 2024-08-25 [A] [expires: 2026-01-01]

In the above output the secret primary key must be labeled as `sec#`.

#### [Exporting keys]

##### [Listing keys]

Loaded public keys can be displayed with [gpg -k]:

`user `[`$`]`gpg -k`

    /root/.gnupg/pubring.kbx
    ------------------------
    pub   ed25519 2023-04-25 [SC]
          1080E273CC9C0BF9B3A228EAA562DF903D0BB7F6
    uid           [ultimate] Larry (wiki test key) <larry@gentoo.org>
    sub   cv25519 2023-04-25 [E]
    sub   ed25519 2023-04-25 [A]

Private keys can be listed by using [gpg -K] instead of [gpg -k]:

`user `[`$`]`gpg -K`

    /root/.gnupg/pubring.kbx
    ------------------------
    sec   ed25519 2023-04-25 [SC]
          1080E273CC9C0BF9B3A228EAA562DF903D0BB7F6
    uid           [ultimate] Larry (wiki test key) <larry@gentoo.org>
    ssb   cv25519 2023-04-25 [E]
    ssb   ed25519 2023-04-25 [A]

##### [Public keys]

Public keys can be exported using `--export`, to export keys in armored form to stdout:

`user `[`$`]`gpg --armor --export Larry`

    -----BEGIN PGP PUBLIC KEY BLOCK-----

    mDMEZEfeAhYJKwYBBAHaRw8BAQdArguazSgVcquYvBlx0/Zf59sc/FuPNDCxZ7Ch
    q3FHIQa0K0xhcnJ5ICh3aWtpIGV4YW1wbGUga2V5KSA8bGFycnlAZ2VudG9vLm9y
    Zz6IkAQTFggAOBYhBNKlwQ4ve6w23bwK/PmAvPH63HR5BQJkR94CAhsDBQsJCAcC
    BhUKCQgLAgQWAgMBAh4BAheAAAoJEPmAvPH63HR5KhgBAOUqhecyl7a9srOzR6pV
    aiLIb1piUldUh+WxLTKGGGxSAQD+4mlnhkQDbjhW36yE1XPTzQjkPXfSUKDnk+DC
    4sKOC7g4BGRH4T8SCisGAQQBl1UBBQEBB0CO2YaH9u6TqANovaCUDirs7W2xBZdz
    i3dV28u2bA7rHAMBCAeIfgQYFggAJhYhBNKlwQ4ve6w23bwK/PmAvPH63HR5BQJk
    R+E/AhsMBQkB4TOAAAoJEPmAvPH63HR58UsBAIYFWB3JfmkrSy03Hi/R+D8yapLD
    +dnpbBrvg9arZNPFAPwIklhrFSO+1exgUnIIv/4d6FreEcxNHik6qdU2M3yJBbgz
    BGRH4iIWCSsGAQQB2kcPAQEHQH/4R7RST15/rVFDSYXXvgnjzWe73MwhIZ0ZFtpa
    YWB0iHgEGBYIACAWIQTSpcEOL3usNt28Cvz5gLzx+tx0eQUCZEfiIgIbIAAKCRD5
    gLzx+tx0eS8SAQC27hYFV5C5A5MMI46/vD3eeQQ8pGNIR92YGYBCj7EVhQEAu4ux
    0fxWpQOTeXxu+HJj/vhBioB6G4l25Q+Ry8Gbbwk=
    =UXWK
    -----END PGP PUBLIC KEY BLOCK-----

Or to a file:

`user `[`$`]`gpg --output larry.pub --export 1080E273CC9C0BF9B3A228EAA562DF903D0BB7F6`

** Tip**\
In this case, **Larry** or **1080E273CC9C0BF9B3A228EAA562DF903D0BB7F6** can be used as parameter for `--export`, since both the keygrip and user names are valid ways to reference keys in GPG.

** Note**\
If `--armor` is omitted, binary data will be written to stdout. The `--armor` adds a GPG header and footer to the data and encodes it using Base64, so it can be easily copied or even printed.

##### [Private Keys]

Private keys can be exported with: [gpg \--output .secret.gpg \--export-secret-keys ] and [gpg \--output .secret-sub.gpg \--export-secret-subkeys ] can be used, where `` is the uid or fingerprint associated with the key.

#### [Importing keys]

A key can be imported from a file using: [gpg \--import keyfile.asc], or from stdin using [gpg \--import] where the key can be pasted, and loaded by sending an `EOF` using [Ctrl]+[D].

##### [Gentoo release keys]

[Gentoo\'s GPG keys](https://www.gentoo.org/downloads/signatures/) can be imported by running:

`user `[`$`]`wget -O - https://qa-reports.gentoo.org/output/service-keys.gpg | gpg --import`

or

`user `[`$`]`gpg --import /usr/share/openpgp-keys/gentoo-release.asc`

##### [Loading a key from stdin]

`user `[`$`]`gpg --import`

    -----BEGIN PGP PUBLIC KEY BLOCK-----

    mDMEZEfmDhYJKwYBBAHaRw8BAQdAdor/95lVxt0cDnAh9am37X8svi7khQKWXoqP
    ROBroWi0KExhcnJ5ICh3aWtpIHRlc3Qga2V5KSA8bGFycnlAZ2VudG9vLm9yZz6I
    kAQTFggAOBYhBBCA4nPMnAv5s6Io6qVi35A9C7f2BQJkR+YOAhsDBQsJCAcCBhUK
    CQgLAgQWAgMBAh4BAheAAAoJEKVi35A9C7f2PeEA/3jNAQwngMq4k89wCFBKoKwZ
    fmY+SCjdR6ZE7qi7OsOrAP45o6Yb/MGwpeMO+Zjo4TRAghLBwyLjlfXmidbRozje
    B7g4BGRH5iASCisGAQQBl1UBBQEBB0B0vG919/1fH7wWqgaRryoqwQZJY2/Ga+eY
    Wo0tCWd3UwMBCAeIeAQYFggAIBYhBBCA4nPMnAv5s6Io6qVi35A9C7f2BQJkR+Yg
    AhsMAAoJEKVi35A9C7f2kZoBALcK7qEzwqs3gRF0BDJk8sejA0y4qnR1iZHQsoGp
    MKzJAQDWcR6MSjfkmfMhRKBp+BO0FjtXW5JqK78WHf9+9PWQDrgzBGRH5ioWCSsG
    AQQB2kcPAQEHQO3KCdy134zfo1ii8dxSKFQ3xOhO7X0AJONjNt4358YiiHgEGBYI
    ACAWIQQQgOJzzJwL+bOiKOqlYt+QPQu39gUCZEfmKgIbIAAKCRClYt+QPQu39n4G
    AQCrH85V3y2vH8Cwz+Tnp0lUYil2yZGX87v2aXTOLbfIEgEAn1PAUEhCweoKqlKr
    FVRpfQN4KfmgT8EMTjXfjUQZog8=
    =KXyX
    -----END PGP PUBLIC KEY BLOCK-----
    gpg: key A562DF903D0BB7F6: "Larry (wiki test key) <larry@gentoo.org>" not changed
    gpg: Total number processed: 1
    gpg:              unchanged: 1

If a private key is being loaded, [pinentry] may prompt for the key passwords:

`user `[`$`]`gpg --import larry.secret*`

    gpg: key A562DF903D0BB7F6: "Larry (wiki test key) <larry@gentoo.org>" not changed
    gpg: To migrate 'secring.gpg', with each smartcard, run: gpg --card-status
    gpg: key A562DF903D0BB7F6: secret key imported
    gpg: key A562DF903D0BB7F6: "Larry (wiki test key) <larry@gentoo.org>" not changed
    gpg: key A562DF903D0BB7F6: secret key imported
    gpg: Total number processed: 2
    gpg:              unchanged: 2
    gpg:       secret keys read: 2
    gpg:   secret keys imported: 2
    gpg:  secret keys unchanged: 1

** Warning**\
Be careful when verifying keys. This is one of the weak points of public key cryptography.

When importing key backups, it may make sense to mark the keys as ultimately trusted:

`user `[`$`]`gpg --edit-key Larry`

    Secret key is available.
    gpg> trust
    sec  ed25519/A562DF903D0BB7F6
         created: 2023-04-25  expires: never       usage: SC
         trust: undefined     validity: unknown
    ssb  cv25519/70373C88C49E535A
         created: 2023-04-25  expires: never       usage: E
    ssb  ed25519/9019FBB6586D8EE1
         created: 2023-04-25  expires: never       usage: A
    [ unknown] (1). Larry (wiki test key) <larry@gentoo.org>

    Please decide how far you trust this user to correctly verify other users' keys
    (by looking at passports, checking fingerprints from different sources, etc.)

    1 = I don't know or won't say
      2 = I do NOT trust
      3 = I trust marginally
      4 = I trust fully
      5 = I trust ultimately
      m = back to the main menu

    Your decision? 5
    Do you really want to set this key to ultimate trust? (y/N) y

    sec  ed25519/A562DF903D0BB7F6
         created: 2023-04-25  expires: never       usage: SC
         trust: ultimate      validity: unknown
    ssb  cv25519/70373C88C49E535A
         created: 2023-04-25  expires: never       usage: E
    ssb  ed25519/9019FBB6586D8EE1
         created: 2023-04-25  expires: never       usage: A
    [ unknown] (1). Larry (wiki test key) <larry@gentoo.org>
    Please note that the shown key validity is not necessarily correct
    unless you restart the program.

#### [Signing keys]

An imported key can be signed (certified) once it\'s verified.

Certifying a key implies it is trusted by the signer. The signed key can be sent back to the owner, and and the key could be redistributed, so anyone who trusts the key that was used to sign that key can implicitly trust the signed key.

Here, the repomirror key is being signed by Larry:

`user `[`$`]`gpg --edit-key repomirrorci@gentoo.org`

    gpg (GnuPG) 2.2.40; Copyright (C) 2022 g10 Code GmbH
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    pub  rsa4096/A13D0EF1914E7A72
         created: 2018-05-28  expires: 2024-07-01  usage: C
         trust: unknown       validity: unknown
    sub  rsa2048/7C2AC09CD98F2EDF
         created: 2018-05-28  expires: 2024-07-01  usage: S
    [ unknown] (1). Gentoo repository mirrors (automated git signing key) <repomirrorci@gentoo.org>

    gpg> trust
    pub  rsa4096/A13D0EF1914E7A72
         created: 2018-05-28  expires: 2024-07-01  usage: C
         trust: unknown       validity: unknown
    sub  rsa2048/7C2AC09CD98F2EDF
         created: 2018-05-28  expires: 2024-07-01  usage: S
    [ unknown] (1). Gentoo repository mirrors (automated git signing key) <repomirrorci@gentoo.org>

    Please decide how far you trust this user to correctly verify other users' keys
    (by looking at passports, checking fingerprints from different sources, etc.)

      1 = I don't know or won't say
      2 = I do NOT trust
      3 = I trust marginally
      4 = I trust fully
      5 = I trust ultimately
      m = back to the main menu

    Your decision? 4

    pub  rsa4096/A13D0EF1914E7A72
         created: 2018-05-28  expires: 2024-07-01  usage: C
         trust: full          validity: unknown
    sub  rsa2048/7C2AC09CD98F2EDF
         created: 2018-05-28  expires: 2024-07-01  usage: S
    [ unknown] (1). Gentoo repository mirrors (automated git signing key) <repomirrorci@gentoo.org>
    Please note that the shown key validity is not necessarily correct
    unless you restart the program.

    gpg> sign

    pub  rsa4096/A13D0EF1914E7A72
         created: 2018-05-28  expires: 2024-07-01  usage: C
         trust: full          validity: unknown
     Primary key fingerprint: EF95 38C9 E8E6 4311 A52C  DEDF A13D 0EF1 914E 7A72

    Gentoo repository mirrors (automated git signing key) <repomirrorci@gentoo.org>

    This key is due to expire on 2024-07-01.
    Are you sure that you want to sign this key with your
    key "Larry (wiki test key) <larry@gentoo.org>" (A562DF903D0BB7F6)

    Really sign? (y/N) y

    gpg> save

If Larry sent this signed key to someone, and someone else sent it to someone who knew and trusted Larry, they would have reason to trust the key, even if it was distributed using an insecure method.

When a key is marked as not trusted, signatures can also be used to designate that a certain user does not trust the key.

#### [Exchanging keys with key servers]

##### [Configuring a default key server]

To make [gpg] use *keys.openpgp.org* as the default key server, the following configuration can be used:

[FILE] **`~/.gnupg/gpg.conf`Make GPG use keys.openpgp.org as the default *keyserver***

    keyserver keys.openpgp.org

** Note**\
This configuration is equivalent to adding `--keyserver keys.openpgp.org` to every relevant [gpg] command.

##### [Sending keys to key servers]

** Important**\
Gentoo Developers should follow [Gentoo infrastructure\'s key sending instructions](https://wiki.gentoo.org/wiki/Project:Infrastructure/Generating_GLEP_63_based_OpenPGP_keys#Submit_your_new_key_to_the_keyserver "Project:Infrastructure/Generating GLEP 63 based OpenPGP keys").

Once keys are generated, they can be shared with a keyserver. This makes it easier for others to import the key.

To send the keys to the *openpgp* keyserver:

`user `[`$`]`gpg --keyserver keys.openpgp.org --send-key D2A5C10E2F7BAC36DDBC0AFCF980BCF1FADC7479`

    gpg: sending key 0xF980BCF1FADC7479 to hkp://keys.openpgp.org

** Note**\
Other keys which have been certified may also be sent to a keyserver, this is announces that one key holder trusts (or distrusts) another key.

##### [Getting keys from key servers]

To obtain Larry\'s uploaded keys, the `--search-keys` parameter can be used with identifying information such as the email address:

`user `[`$`]`gpg --keyserver keys.openpgp.org --search-keys larry@gentoo.org`

    gpg: data source: http://keys.openpgp.org:12345
    (1) larry <larry@gentoo.org>
         256 bit EDDSA key 0xF980BCF1FADC7479, created: 2023-04-22
    Keys 1-1 of 1 for "larry@gentoo.org".  Enter number(s), N)ext, or Q)uit > 1
    gpg: /home/larry/.gnupg/trustdb.gpg: trustdb created
    gpg: key 0xF980BCF1FADC7479: public key "larry <larry@gentoo.org>" imported
    gpg: Total number processed: 1
    gpg:               imported: 1

** Important**\
When importing keys from a keyserver, be sure to check the key, as multiple keys may match a search.

##### [Refreshing existing keys]

Existing PGP keys should be refreshed on a regular interval (twice a month is common). To refresh keys, define a key server with which to connect:

`user `[`$`]`gpg --keyserver hkps://keys.gentoo.org --refresh-keys`

This command can be added to a cron job or systemd timer.

### [GPG Agent]

[[[app-crypt/gnupg]](https://packages.gentoo.org/packages/app-crypt/gnupg)[]] is packaged with [gpg-agent] which can be used to cache passphrases and manage unlocked key access.

** Note**\
[[[xfce-base/xfce4-meta]](https://packages.gentoo.org/packages/xfce-base/xfce4-meta)[]] will try to automatically run [gpg-agent] and [ssh-agent]. This can make identity management more confusing.

** Note**\
[gpg-agent] can be configured on a per-user basis with [\~/.gnupg/gpg-agent.conf]

** Tip**\
Options are documented in [man gpg-agent] under `OPTIONS`, simply omit the leading dashes.

[FILE] **`~/.gnupg/gpg-agent.conf`Configure gpg-agent to use /usr/bin/pinentry with a ttl of 30 minutes**

    pinentry-program /usr/bin/pinentry
    no-grab
    default-cache-ttl 1800

[FILE] **`~/.gnupg/gpg-agent.conf`Configure gpg-agent with ssh-agent support**

    enable-ssh-support

GPG must be configured to use [gpg-agent], this can be accomplished with:

[FILE] **`~/.gnupg/gpg.conf`Configuring GnuPG to use a GPG agent**

    use-agent

** Important**\
If the `use-agent` option is not configured, GPG may not prompt for smartcard pinentry.

Configuration changes can be reloaded with:

`user `[`$`]`gpg-connect-agent reloadagent /bye`

#### [Smart Card]

To use GPG with a hardware key/security key/smart card, ensure that the `smartcard` USE flag is enabled \-- this will include the [scdaemon] service; [scdaemon], or \"smart card daemon\", is used by [gpg-agent].

[FILE] **`/etc/portage/package.use/gnupg`**

    app-crypt/gnupg smartcard

`root `[`#`]`emerge --ask -uND app-crypt/gnupg`

To read smart cards, GPG uses the CCID driver, but there are two ways to implement the driver: built-in and stand-alone.

** Important**\
Installing the stand-alone CCID driver might prevent some applications from reading smart cards depending on certain USE flags.

For example, if [[[app-crypt/gnupg]](https://packages.gentoo.org/packages/app-crypt/gnupg)[]] ([GPG](https://wiki.gentoo.org/wiki/GPG "GPG")) is installed with the `smartcard` USE flag, it will include the [scdaemon] service. If the `usb` USE flag is also enabled, [scdaemon] will have the additional functionality of being a smart card reader \-- allowing GPG to read smart cards without any additional dependencies.

The issue is that if the stand-alone CCID driver, [[[app-crypt/ccid]](https://packages.gentoo.org/packages/app-crypt/ccid)[]], is installed, it will conflict with the built-in CCID driver for [scdaemon] \-- preventing GPG from reading smart cards. But some packages (such as [KeePassXC](https://wiki.gentoo.org/wiki/KeePassXC "KeePassXC")) require the stand-alone driver to use features provided by smart cards. There are two solutions to fix this, both of which make [pcscd] the smart card reader. After a solution has been chosen, see [PCSC-Lite](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite") for additional configuration if needed.

-   Solution 1: Install GPG with the `usb` USE flag disabled then terminate the [gpg-agent] process then restart [pcscd].

[FILE] **`/etc/portage/package.use/gnupg`**

    app-crypt/gnupg -usb

`root `[`#`]`emerge --ask -uND app-crypt/gnupg `

`root `[`#`]`killall gpg-agent `

`root `[`#`]`rc-service pcscd restart `

-   Solution 2: Tell [scdaemon] to not use its built-in CCID driver \-- this has the same affect if [scdaemon] started with the `--disable-ccid` option; see [man scdaemon].

[FILE] **`~/.gnupg/scdaemon.conf`**

    disable-ccid

Also ensure to terminate the [gpg-agent] process then restart [pcscd].

`root `[`#`]`killall gpg-agent `

`root `[`#`]`rc-service pcscd restart `

At this point, GPG should be able to read smart cards. To test this, plug in an OpenPGP-compatible smart card and run the following command:

`user `[`$`]`gpg --card-status`

    Reader ...........: <some smart card> [CCID/ICCD Interface] 00 00
    Application ID ...: <some id>
    Application type .: OpenPGP
    Version ..........: 3.4
    Manufacturer .....: unknown
    Serial number ....: <some serial number>
    Name of cardholder: [not set]
    Language prefs ...: [not set]
    Salutation .......:
    URL of public key : [not set]
    Login data .......: [not set]
    Signature PIN ....: not forced
    Key attributes ...: ed25519 cv25519 ed25519
    Max. PIN lengths .: 127 127 127
    PIN retry counter : 3 0 3
    Signature counter : 57
    KDF setting ......: on
    ...

If the output looks similar to the output above, then GPG can read smart cards.

** Important**\
If you had more than one smartcard reader you need to specify the reader-port in [scdaemon] config file

[FILE] **`~/.gnupg/scdaemon.conf`**

    reader-port "<some smart card> [CCID/ICCD Interface]"
    disable-ccid

You can get your reader-port parameter enabling the [scdaemon] log file in the config

[FILE] **`~/.gnupg/scdaemon.conf`**

    reader-port "<some smart card> [CCID/ICCD Interface]"
    card-timeout 1
    debug-level basic
    log-file /home/<USER>/.gnupg/scdaemon.log
    disable-ccid

Ensure to terminate the [scdaemon] process after changing the the [scdaemon] config.

`user `[`$`]`gpgconf --kill scdaemon`

\

`user `[`$`]`tail -f ~/.gnupg/scdaemon.log & gpg --card-status `

    ...
    2026-01-04 15:59:39 scdaemon[12923] detected reader 'Yubico YubiKey OTP+FIDO+CCID 00 00'
    2026-01-04 15:59:39 scdaemon[12923] detected reader 'Alcor Micro AU9540 01 00'
    ...

The valid reader-port are the **detected reader** strings without the final \" 00\" es. **\"Yubico YubiKey OTP+FIDO+CCID 00\"** or **\"Alcor Micro AU9540 01\"**

Finally you will have a config file similar to this

[FILE] **`~/.gnupg/scdaemon.conf`**

    reader-port "Yubico YubiKey OTP+FIDO+CCID 00"
    card-timeout 1
    disable-ccid

Ensure to terminate the [scdaemon] process after changing the [scdaemon] config.

`user `[`$`]`gpgconf --kill scdaemon`

\

### [Using gpg-agent for SSH]

To use [gpg-agent]\'s SSH socket for SSH, some environment variables need to be set. The commands in the following file boxes come from [info gnupg] and [man gpg-agent], where it\'s stated that if ssh agent support is enabled, ssh needs to be told about it by adding the following commands.

`GPG_TTY` is an environment variable that should be set to ensure that the Curses-based Pinentry works correctly^[\[3\]](#cite_note-3)^. If this variable is not set, then [gpg-agent] might error out. For example, the following command will error out when `GPG_TTY` is not set^[\[4\]](#cite_note-4)^:

`user `[`$`]`touch input `

`user `[`$`]`gpg --sign input`

    gpg: signing failed: Inappropriate ioctl for device
    gpg: [stdin]: clear-sign failed: Inappropriate ioctl for device

`GPG_TTY` variable can be set in [\~/.bashrc] file. This ensures that each terminal has a unique value that points to the path of itself.

[FILE] **`~/.bashrc`**

    export GPG_TTY="$(tty)"

Next, `SSH_AGENT_PID` variable must be [unset] because when [ssh-agent] starts, it stores the name of the agent\'s process ID (PID) in this variable. Since using [gpg-agent] instead of [ssh-agent], there is no need of this environment variable. See [man ssh-agent] for more information.

[FILE] **`~/.bashrc`**

    unset SSH_AGENT_PID

Finally, `SSH_AUTH_SOCK` variable need to be set. When [ssh] is used to access a remote host, [gpg-agent] will be used instead of [ssh-agent] \-- this allows use GPG keys to login instead of a simple password. [ssh-agent] uses the `SSH_AUTH_SOCK` environment variable to determine which socket to use; `SSH_AUTH_SOCK` must be changed to point to the socket created by [gpg-agent].

The test involving the `gnupg_SSH_AUTH_SOCK_by` variable is for the case where the agent is started as [gpg-agent \--daemon /bin/sh], in which case the shell inherits the `SSH_AUTH_SOCK` variable from the parent^[\[5\]](#cite_note-5)[\[6\]](#cite_note-6)^.

[FILE] **`~/.bashrc`**

    if [ "$" -ne $$ ]; then
        export SSH_AUTH_SOCK="$(gpgconf --list-dirs agent-ssh-socket)"
    fi

The following alias is needed because SSH will be using [gpg-agent] instead of [ssh-agent]. The problem is that [gpg-agent] only stores the tty of where it was first started; so if user try to [ssh] in another terminal, the Pinentry will pop up in the terminal that started [gpg-agent], not the one that ran [ssh]. To fix this, update the current tty to [gpg-agent] before run [ssh].

[FILE] **`~/.bashrc`**

    alias ssh="gpg-connect-agent updatestartuptty /bye >/dev/null && ssh"

At this point, modifying [\~/.bashrc] file is finished, but GPG need to be aware of which keys should be used for SSH authentication; this can be done by telling GPG the keygrip of the authentication keys.

Keygrips can be obtained by running:

`user `[`$`]`gpg --list-secret-keys --with-keygrip`

    /home/larry/.gnupg/pubring.kbx
    -----------------------------
    pub   rsa4096 2023-04-21 [SC]
          1C1D353237DC641FE85FD636EF388174179C0E55
          Keygrip = D6DC8A04F02651E47835F0148939ABC1A1000389
    uid           [ultimate] larry (test key) <larry@gentoo.org>
    sub   rsa4096 2023-04-21 [E]
          Keygrip = F2B7E9F47E394C21FA5E2A5510047E0A28F45D62
    sub   rsa4096 2023-04-21 [A]
          Keygrip = 0CA0F1710A5837577FB10177355BE575A425D76D

Where the **\[A\] *key is the* Authentication** key, which is used for ssh login.

#### [Prior v2.3.7]

[gpg-agent] only uses auth keys for SSH whose keygrip is present in [\~/.gnupg/sshcontrol].

To allow [gpg-agent] to use the specified GPG key for SSH auth:

[FILE] **`~/.gnupg/sshcontrol`**

    0CA0F1710A5837577FB10177355BE575A425D76D

#### [From v2.3.7]

[gpg-agent] deprecates use of [\~/.gnupg/sshcontrol] file instead recommends setting `Use-for-ssh` attribute in auth key files which should be used for SSH.

Setting `Use-for-ssh` attribute can be done in two ways. One with editor and other using [gpg-connect-agent]:

`user `[`$`]`echo "Use-for-ssh: true" >> ~/.gnupg/private-keys-v1.d/0CA0F1710A5837577FB10177355BE575A425D76D.key`

`user `[`$`]`gpg-connect-agent 'KEYATTR 0CA0F1710A5837577FB10177355BE575A425D76D Use-for-ssh: true' /bye`

It is possible to use different values than \"true\" which behave differently. For more details see the *\--enable-ssh-support* section of [[[gpg-agent(1)]](https://linux.die.net/man/1/gpg-agent)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page") .

** Note**\
There was a [bug](https://dev.gnupg.org/rG68b7aff9ce345c1f73f84d6b1106eab956d75510) which prevented use of above gpg-connect-agent command which has been fixed now.

### [Forwarding GPG Agent over SSH]

** Warning**\
This is potentially dangerous, forwarding the GPG agent socket should only be done in trusted environments.

** Important**\
The remote host must have the corresponding public keys. Keys can be transferred manually, or the remote keyring can be **replaced** with the local one using:

`user `[`$`]`scp ~/.gnupg/pubring.kbx remotehost:.gnupg/pubring.kbx`

First, the remote server\'s SSH daemon must be configured to allow remote forwards to override local files with:

[FILE] **`/etc/ssh/sshd_config`**

    StreamLocalBindUnlink yes

Then, the path for the GPG agent sockets must be obtained on both systems with:

`user `[`$`]`gpgconf --list-dirs`

    sysconfdir:/etc/gnupg
    bindir:/usr/bin
    libexecdir:/usr/libexec
    libdir:/usr/lib64/gnupg
    datadir:/usr/share/gnupg
    localedir:/usr/share/locale
    socketdir:/run/user/1000/gnupg
    dirmngr-socket:/run/user/1000/gnupg/S.dirmngr
    agent-ssh-socket:/run/user/1000/gnupg/S.gpg-agent.ssh
    agent-extra-socket:/run/user/1000/gnupg/S.gpg-agent.extra
    agent-browser-socket:/run/user/1000/gnupg/S.gpg-agent.browser
    agent-socket:/run/user/1000/gnupg/S.gpg-agent
    homedir:/home/larry/.gnupg

** Note**\
The local system\'s *S.gpg-agent.extra* socket will be forwarded to the remote system\'s *S.gpg-agent* socket.

SSH can be configured to automatically forward the GPG agent socket with:

[FILE] **`~/.ssh/config`Automatically forward the GPG agent socket over SSH**

    host remoteHost
        HostName 1.2.3.4
        RemoteForward /run/user/1000/gnupg/S.gpg-agent:/run/user/1000/gnupg/S.gpg-agent.extra

### [Changing pinentry for SSH logins]

If [gpg-agent] is used over SSH, a graphical [pinentry] password prompt will not come up in the login shell. This causes all operations that require a password to fail. The following snippet can be added to [\~/.bash_profile], this tells [gpg-agent] to use a **curses** prompt in the current shell. The snippet does not affect the [pinentry] settings when using local shells.

[FILE] **`~/.bash_profile`Use curses pinentry for SSH logins**

    if [[ -n "$SSH_CONNECTION" ]] ;then
        export PINENTRY_USER_DATA="USE_CURSES=1"
    fi

### [Automatically starting the GPG agent]

#### [Generic]

A generic method to autostart the GPG agent is to add `gpgconf --launch gpg-agent` to a shell\'s rc file.

[FILE] **`~/.bashrc`Autostart gpg-agent on shell init**

    gpgconf --launch gpg-agent

#### [KDE]

[KDE](https://wiki.gentoo.org/wiki/KDE "KDE") manages the GPG agent using the following files:

1.  [/etc/xdg/plasma-workspace/env/10-agent-startup.sh] - System agent startup configuration
2.  [/etc/xdg/plasma-workspace/shutdown/10-agent-shutdown.sh] - System agent shutdown configuration
3.  [\~/.config/plasma-workspace/env/gpg-agent.sh] - User startup configuration
4.  [\~/.config/plasma-workspace/shutdown/gpg-agent.sh] - User shutdown configuration

The system configuration should contain a template for the GPG agent, it can be activated by uncommenting the following. To enable it for a single user, the configuration must be added to the user configuration.

[FILE] **`/etc/xdg/plasma-workspace/env/10-agent-startup.sh`Make Plasma automatically start the GPG agent**

    if [ -x /usr/bin/gpg-agent ]; then
        if [ -x /usr/bin/gpgconf ]; then
            gpgconf --launch gpg-agent >/dev/null 2>&1
            if [ $? = 2 ]; then
                eval "$(/usr/bin/gpg-agent --enable-ssh-support --daemon)"
            fi
        fi
    fi

[FILE] **`/etc/xdg/plasma-workspace/shutdown/10-agent-shutdown.sh`Make Plasma shut down the GPG agent**

    if [ -n "$" ]; then
        kill $(echo $ | cut -d':' -f 2) >/dev/null 2>&1
    fi

## [Usage]

Some parameters that apply to several GPG commands are:

-   [\--armor] - Adds PGP headers and footers to the data encoded as base64, useful when outputting to stdout
-   [\--local-user] or [-u] - Specifies the key to use for signing
-   [\--output] or [-o] - The output file, stdout is used otherwise

** Note**\
The order of the parameters is important, generally `--armor` should be used as the first argument.

### [Signing]

Signing verifies that someone with the private key associated with a known public key signed the data. If user trust that the key holder securely stores their key, then the user can be reasonably certain they sent a message signed with it. It can be used alongside encryption to ensure that a message can only be read by the intended recipients, and can be verified as coming from the correct source.

Data can be signed with `--sign` or `-s`:

`user `[`$`]`gpg --armor --sign --local-user larry`

    pgp signed
    -----BEGIN PGP MESSAGE-----

    owGbwMvMwCG2NOn+BFvu7d8YTwsmMaR4LjMpSC9QKM5Mz0tN4epoZ2EQ42DQF1Nk
    EWh4VHxmDvfPzYs0XsG0sDIB1VsKyuQkFhVVOqSn5pXk5+vlF6UzcHEKwNQ8mc/w
    P1f2StrZVbZqfdX7fKY8XPLrVZ3/vnKmh5r7C+epci2amMnIMHX3/W/CQoW+PDsu
    +B1wPaHWWPiWj+ueWvQVp8IZ1fNq+AE=
    =MWu8
    -----END PGP MESSAGE-----

** Important**\
This alone does not encrypt the data.

#### [Clear signing]

** Warning**\
Clear signing is considered [deprecated and unsafe](https://gnupg.org/blog/20251226-cleartext-signatures.html). Use detached signatures wherever possible.

Plaintext data can be signed, to verify the sender or publisher of the data. Unlike `--sign`, `--clear-sign` will keep the message in plaintext, putting the signature below it:

`user `[`$`]`gpg --clear-sign --local-user Larry`

    clear signed data!
    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA256

    clear signed data!
    -----BEGIN PGP SIGNATURE-----

    iIcEARYIAC8WIQQQgOJzzJwL+bOiKOqlYt+QPQu39gUCZEmlbhEcbGFycnlAZ2Vu
    dG9vLm9yZwAKCRClYt+QPQu39oxbAQDk5mEpEUXv+d9Wk7zOIzHzTMfgomzQvqPf
    XEzq3mjiMAEAm7QpY28vI6xBAJlCebveJ37U5iqhmQKCmDGDRjiMdA4=
    =VAr8
    -----END PGP SIGNATURE-----

** Note**\
`--clear-sign` implies the data should be armored.

#### [Detached signature]

GPG can be used to sign data, keeping the signature separate from the data itself. The signature file can be distributed with the data. This is accomplished by using `--detach-sig`. The following command will output a file named [sign-me.sig] which contains a signature for the file [sign-me]:

`user `[`$`]`gpg --armor --detach-sig --local-user Larry --output sign-me.sig sign-me`

### [Symmetric Encryption]

GPG\'s Symmetric encryption can be used to cipher data to be accessible by anyone who possesses the cipher key.

Available cipher algorithms can be viewed with [gpg \--version] under **Cipher**:

`user `[`$`]`gpg --version`

    gpg (GnuPG) 2.2.40
    libgcrypt 1.10.1
    Copyright (C) 2022 g10 Code GmbH
    License GNU GPL-3.0-or-later <https://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Home: /root/.gnupg
    Supported algorithms:
    Pubkey: RSA, ELG, DSA, ECDH, ECDSA, EDDSA
    Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
            CAMELLIA128, CAMELLIA192, CAMELLIA256
    Hash: SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
    Compression: Uncompressed, ZIP, ZLIB, BZIP2

A cipher type can be selected with `--cipher-algo`, and symmetric encryption can be used with `--symmetric` or `-c`:

`user `[`$`]`gpg --armor --symmetric --cipher-algo AES256`

    aes256 ciphered data
    -----BEGIN PGP MESSAGE-----

    jA0ECQMCKBC2RERjZ1b/0koBrujXapFyEqaNhnLYAdfQz8xNM9IQtTwcahJau6Ri
    DLDSlQJk2UBafpmF0TaiPRyaoGQD8BovK/vRZ9Nw72tTOV0cT7a9eZ1R3w==
    =4hhX
    -----END PGP MESSAGE-----

#### [Signed]

Anyone who decrypts symmetrically encrypted data will not be able to verify the authenticity of it without a signature or external (non-GPG) methods being used. To sign this symmetrically encrypted data, use:

`user `[`$`]`gpg --armor --local-user Larry --sign --symmetric --cipher-algo AES256`

    gpg: AES256 encryption will be used
    aes256 ciphered and signed data
    -----BEGIN PGP MESSAGE-----

    jA0ECQMCwNNr5efDiqr/0sAkAZo1EjWD3rsGERIdttMtxT4jaXGzUMKYNXMFhpbE
    zcmSg6WfvFDFjwp3mbOLPF16WjwXS3tzNVeYPdKeqFNY6/K2FpkCIFFjNIYhnE1d
    MnjaLeavNw2hxi5rtAhiyuPB5uRqjNFqvOgqon26WV7ZMTrbgR5AsJtE+U0+Ag/8
    Yy/gUmNKxMIb4Y4E534oM9Kw2ik0ANnYOBRM4XmH935PBZa/Z/rMQkGLe1vN0GBs
    wDnC/XuSkqK4lWg46AvcyyrXvv7pnNiRd6HpTIBp9DGrllk3+OQNvueJW18QDzkU
    7L/lV3gq
    =2XP9
    -----END PGP MESSAGE-----

### [][Asymmetric (Public Key) Encryption]

GPG is generally used to perform asymmetric cryptography.

To send a message to a recipient, first view available public keys with [gpg -k]:

`user `[`$`]`gpg -k`

    /root/.gnupg/pubring.kbx
    ------------------------
    pub   ed25519 2023-04-25 [SC]
          1080E273CC9C0BF9B3A228EAA562DF903D0BB7F6
    uid           [ultimate] Larry (wiki test key) <larry@gentoo.org>
    sub   cv25519 2023-04-25 [E]
    sub   ed25519 2023-04-25 [A]

    pub   rsa4096 2018-05-28 [C] [expires: 2024-07-01]
          EF9538C9E8E64311A52CDEDFA13D0EF1914E7A72
    uid           [  full  ] Gentoo repository mirrors (automated git signing key) <repomirrorci@gentoo.org>
    sub   rsa2048 2018-05-28 [S] [expires: 2024-07-01]

    pub   rsa4096 2011-11-25 [C] [expires: 2024-07-01]
          DCD05B71EAB94199527F44ACDB6B8C1F96D8BF6D
    uid           [ unknown] Gentoo ebuild repository signing key (Automated Signing Key) <infrastructure@gentoo.org>
    uid           [ unknown] Gentoo Portage Snapshot Signing Key (Automated Signing Key)
    sub   rsa4096 2011-11-25 [S] [expires: 2024-07-01]

    pub   dsa1024 2004-07-20 [SC] [expires: 2024-01-01]
          D99EAC7379A850BCE47DA5F29E6438C817072058
    uid           [ unknown] Gentoo Linux Release Engineering (Gentoo Linux Release Signing Key) <releng@gentoo.org>
    sub   elg2048 2004-07-20 [E] [expires: 2024-01-01]

    pub   rsa2048 2019-04-01 [C] [expires: 2024-07-01]
          ABD00913019D6354BA1D9A132839FE0D796198B1
    uid           [ unknown] Gentoo Authority Key L1 <openpgp-auth+l1@gentoo.org>

    pub   rsa2048 2019-04-01 [C] [expires: 2024-07-01]
          2C13823B8237310FA213034930D132FF0FF50EEB
    uid           [ unknown] Gentoo Authority Key L2 for Developers <openpgp-auth+l2-dev@gentoo.org>

    pub   rsa2048 2019-04-01 [C] [expires: 2024-07-01]
          18F703D702B1B9591373148C55D3238EC050396E
    uid           [ unknown] Gentoo Authority Key L2 for Services <openpgp-auth+l2-srv@gentoo.org>

    pub   rsa4096 2009-08-25 [SC] [expires: 2024-07-01]
          13EBBDBEDE7A12775DFDB1BABB572E0E2D182910
    uid           [ unknown] Gentoo Linux Release Engineering (Automated Weekly Release Key) <releng@gentoo.org>
    sub   rsa2048 2019-02-23 [S] [expires: 2024-07-01]

    pub   rsa4096 2022-07-08 [C] [expires: 2024-07-07]
          BA9A03F6BE9C0CA405C17BFE079BA8929AF1275A
    uid           [ unknown] GLSAMaker <glsamaker@gentoo.org>
    sub   rsa4096 2022-07-08 [S] [expires: 2024-07-07]
    sub   rsa4096 2022-07-08 [E] [expires: 2024-07-07]

To encrypt a message to Larry, use `--encrypt` or `-e` with *Larry* as the recipient:

`user `[`$`]`gpg --armor --recipient Larry --encrypt`

    message for larry
    -----BEGIN PGP MESSAGE-----

    hF4DcDc8iMSeU1oSAQdA41y+LHzG8QyGl5U9gfVB/nywTqcDv2GdvLp/PIXT21Iw
    GRj48Z13SNkkTckl9igbM62u6CFqxyd4OiM8Vl9QCpUfMgIxVRrY4AP4HldBQhyM
    0k0Bbsccx5iesRLQA9DjbVDf3AU1sJ+Y3f2LBx3RsU7umIm6fhH87iY6ktgzUWhj
    1LgJtSN/FBfVFFLh6IaqaN4e1NFrtnLqo9kqplfUQQ==
    =E5ym
    -----END PGP MESSAGE-----

#### [Signed]

This message can also be signed, so the recipient can verify the sender:

`user `[`$`]`gpg --armor --local-user Larry --sign --recipient Larry --encrypt`

    signed message to larry from larry :)
    -----BEGIN PGP MESSAGE-----

    hF4DcDc8iMSeU1oSAQdAVq/Jzu/ckb41+52QQJ74JU0EG6xySBmH/Bgztotv8Rsw
    msrObF+goxNUhmvDmrIhJsovddW0L2s672wcfyxEJurq6hhq5FwZIqNSaj7nTQe/
    0sAqAcILx2edUsx087TOSfoPgxSOIsq/K9G6w6WtYmtYsAInsmrwiDM+vh0x0ZN+
    vvCtgNa6XV3KNEGSFaD0g5X5aJJTUhMleTQdR7IZ6+wT7R0tYvdbtHP7amHiUdrm
    ZXhLPYxjFvh1odYkEL64ESo6AjvPB+7NzgrrXXhrLG2ahypWeVsCJmxmutdfOO36
    eXFVXvUYx5RvspCUBR5tA7A0Yj3yaMjIZQ6pMYeYPnB0bjlYa3DNb4uAlkjuNC7h
    zUxbq6WfUcHzH6wVvsRhTGiRXw3IwDPelo7IfyDitxMQeRMh13A9XRg3kIPY
    =vY0g
    -----END PGP MESSAGE-----

### [Signature verification]

Verifying the signature of signed data is very important, if this is not done, the sender of the data is not validated. Verification is generally done using the `--verify` flag:

`user `[`$`]`gpg --verify`

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA256

    clear signed data!
    -----BEGIN PGP SIGNATURE-----

    iIcEARYIAC8WIQQQgOJzzJwL+bOiKOqlYt+QPQu39gUCZEmlbhEcbGFycnlAZ2Vu
    dG9vLm9yZwAKCRClYt+QPQu39oxbAQDk5mEpEUXv+d9Wk7zOIzHzTMfgomzQvqPf
    XEzq3mjiMAEAm7QpY28vI6xBAJlCebveJ37U5iqhmQKCmDGDRjiMdA4=
    =VAr8
    -----END PGP SIGNATURE-----
    gpg: Signature made Wed Apr 26 22:27:58 2023 UTC
    gpg:                using EDDSA key 1080E273CC9C0BF9B3A228EAA562DF903D0BB7F6
    gpg:                issuer "larry@gentoo.org"
    gpg: Good signature from "Larry (wiki test key) <larry@gentoo.org>" [ultimate]

#### [Detached signature]

Using the detached signing example, the file [sign-me] can be verified by running:

`user `[`$`]`gpg --verify sign-me.sig sign-me`

    gpg: Signature made Wed Apr 26 23:25:43 2023 UTC
    gpg:                using EDDSA key 1080E273CC9C0BF9B3A228EAA562DF903D0BB7F6
    gpg:                issuer "larry@gentoo.org"
    gpg: Good signature from "Larry (wiki test key) <larry@gentoo.org>" [ultimate]

### [Decryption]

The method for decrypting asymmetric or symmetric data is the same in GPG, the `--decrypt` or `-d` flag is used:

Decrypting:

`user `[`$`]`gpg --decrypt`

    -----BEGIN PGP MESSAGE-----

    jA0ECQMCKBC2RERjZ1b/0koBrujXapFyEqaNhnLYAdfQz8xNM9IQtTwcahJau6Ri
    DLDSlQJk2UBafpmF0TaiPRyaoGQD8BovK/vRZ9Nw72tTOV0cT7a9eZ1R3w==
    =4hhX
    -----END PGP MESSAGE-----
    gpg: AES256.CFB encrypted data
    gpg: encrypted with 1 passphrase
    aes256 ciphered data

Decrypting and verifying signature:

`user `[`$`]`gpg --decrypt`

    -----BEGIN PGP MESSAGE-----

    jA0ECQMCwNNr5efDiqr/0sAkAZo1EjWD3rsGERIdttMtxT4jaXGzUMKYNXMFhpbE
    zcmSg6WfvFDFjwp3mbOLPF16WjwXS3tzNVeYPdKeqFNY6/K2FpkCIFFjNIYhnE1d
    MnjaLeavNw2hxi5rtAhiyuPB5uRqjNFqvOgqon26WV7ZMTrbgR5AsJtE+U0+Ag/8
    Yy/gUmNKxMIb4Y4E534oM9Kw2ik0ANnYOBRM4XmH935PBZa/Z/rMQkGLe1vN0GBs
    wDnC/XuSkqK4lWg46AvcyyrXvv7pnNiRd6HpTIBp9DGrllk3+OQNvueJW18QDzkU
    7L/lV3gq
    =2XP9
    -----END PGP MESSAGE-----
    gpg: AES256.CFB encrypted data
    gpg: encrypted with 1 passphrase
    aes256 ciphered and signed data
    gpg: Signature made Wed Apr 26 22:39:14 2023 UTC
    gpg:                using EDDSA key 1080E273CC9C0BF9B3A228EAA562DF903D0BB7F6
    gpg:                issuer "larry@gentoo.org"
    gpg: Good signature from "Larry (wiki test key) <larry@gentoo.org>" [ultimate]

`user `[`$`]`gpg -d`

    -----BEGIN PGP MESSAGE-----

    hF4DcDc8iMSeU1oSAQdAVq/Jzu/ckb41+52QQJ74JU0EG6xySBmH/Bgztotv8Rsw
    msrObF+goxNUhmvDmrIhJsovddW0L2s672wcfyxEJurq6hhq5FwZIqNSaj7nTQe/
    0sAqAcILx2edUsx087TOSfoPgxSOIsq/K9G6w6WtYmtYsAInsmrwiDM+vh0x0ZN+
    vvCtgNa6XV3KNEGSFaD0g5X5aJJTUhMleTQdR7IZ6+wT7R0tYvdbtHP7amHiUdrm
    ZXhLPYxjFvh1odYkEL64ESo6AjvPB+7NzgrrXXhrLG2ahypWeVsCJmxmutdfOO36
    eXFVXvUYx5RvspCUBR5tA7A0Yj3yaMjIZQ6pMYeYPnB0bjlYa3DNb4uAlkjuNC7h
    zUxbq6WfUcHzH6wVvsRhTGiRXw3IwDPelo7IfyDitxMQeRMh13A9XRg3kIPY
    =vY0g
    -----END PGP MESSAGE-----
    gpg: encrypted with 255-bit ECDH key, ID 70373C88C49E535A, created 2023-04-25
          "Larry (wiki test key) <larry@gentoo.org>"
    signed message to larry from larry :)
    gpg: Signature made Wed Apr 26 22:46:11 2023 UTC
    gpg:                using EDDSA key 1080E273CC9C0BF9B3A228EAA562DF903D0BB7F6
    gpg:                issuer "larry@gentoo.org"
    gpg: Good signature from "Larry (wiki test key) <larry@gentoo.org>" [ultimate]

## [GnuPG interfaces]

** Note**\
S/MIME is more commonly used/supported than GPG for emails, but there is no harm in using GPG (other than it not integrating with Microsoft services)

### [Seahorse]

Seahorse ([[[app-crypt/seahorse]](https://packages.gentoo.org/packages/app-crypt/seahorse)[]]) aims to be a GnuPG GUI interface for the GNOME desktop. The software has been evolving fast, but it still lacks many important features that can be found in Kgpg or the command line version.

## [Troubleshooting]

## [See also]

-   [PCSC-Lite](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite") --- implements the PC/SC international standard for PC to smartcard reader communication.
-   [Sequoia](https://wiki.gentoo.org/wiki/Sequoia "Sequoia") --- a complete implementation of OpenPGP as defined by RFC 9580 as well as the deprecated OpenPGP as defined by RFC 4880, and various related standards
-   [YubiKey/GPG](https://wiki.gentoo.org/wiki/YubiKey/GPG "YubiKey/GPG")

## [External resources]

-   [https://www.void.gr/kargig/blog/2013/12/02/creating-a-new-gpg-key-with-subkeys/](https://www.void.gr/kargig/blog/2013/12/02/creating-a-new-gpg-key-with-subkeys/) - An article explaining the creation of subkeys.
-   [https://keys.openpgp.org/](https://keys.openpgp.org/) - OpenPGP.org\'s PGP infrastructure. Key server is running the Hagrid keyserver software. Use hkps://keys.openpgp.org for accessing from [gpg].
-   [https://keys.gentoo.org/](https://keys.gentoo.org/) - Gentoo Infrastructure\'s official PGP key server.
-   [https://www.gnupg.org/gph/en/manual.html](https://www.gnupg.org/gph/en/manual.html) - John Michael Ashley\'s \"The GNU Privacy Handbook\". Very good book for beginners.

## [[] References]

1.  [[[↑](#cite_ref-1)] [[https://www.gnupg.org/gph/en/manual.html#AEN526](https://www.gnupg.org/gph/en/manual.html#AEN526)]]
2.  [[[↑](#cite_ref-2)] [[https://www.rfc-editor.org/rfc/rfc4880#section-5.2.3.6](https://www.rfc-editor.org/rfc/rfc4880#section-5.2.3.6)]]
3.  [[[↑](#cite_ref-3)] [[https://www.gnupg.org/documentation/manuals/gnupg/Common-Problems.html](https://www.gnupg.org/documentation/manuals/gnupg/Common-Problems.html)]]
4.  [[[↑](#cite_ref-4)] [[https://dev.gnupg.org/T1434](https://dev.gnupg.org/T1434)]]
5.  [[[↑](#cite_ref-5)] [[https://wiki.archlinux.org/title/GnuPG#Set_SSH_AUTH_SOCK](https://wiki.archlinux.org/title/GnuPG#Set_SSH_AUTH_SOCK)]]
6.  [[[↑](#cite_ref-6)] [[https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gnupg.git;a=blob;f=agent/gpg-agent.c;hb=7bca3be65e510eda40572327b87922834ebe07eb#l1307](https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gnupg.git;a=blob;f=agent/gpg-agent.c;hb=7bca3be65e510eda40572327b87922834ebe07eb#l1307)]]

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Gustavo Felisberto, John P. Davis, **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*