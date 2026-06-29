**Resources**

[[]][Electronic identification](https://en.wikipedia.org/wiki/Electronic_identification "wikipedia:Electronic identification")

An **electronic identification** (**eID**) is the core part of e-government implementation, providing a way to identify citizens and organizations.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Smart card reader driver]](#Smart_card_reader_driver)
    -   [[1.2] [Belgium]](#Belgium)
        -   [[1.2.1] [Firefox support]](#Firefox_support)
    -   [[1.3] [Estonia]](#Estonia)
    -   [[1.4] [Germany]](#Germany)
-   [[2] [External resources]](#External_resources)

## [Installation]

### [Smart card reader driver]

Most likely, the card reader will be covered by the [[[app-crypt/ccid]](https://packages.gentoo.org/packages/app-crypt/ccid)[]] package (if not, check the [driver list](https://wiki.gentoo.org/wiki/PCSC-Lite#Additional_software "PCSC-Lite")):

`root `[`#`]`emerge --ask app-crypt/ccid`

And enable the [PCSC-Lite](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite") service, as described [here](https://wiki.gentoo.org/wiki/PCSC-Lite#Service "PCSC-Lite").

### [Belgium]

Install the [[[app-crypt/eid-mw]](https://packages.gentoo.org/packages/app-crypt/eid-mw)[]] package:

`root `[`#`]`emerge --ask app-crypt/eid-mw`

** Note**\
The package is masked by the **[amd64]** keyword. To unmask the package, follow the steps described [here](https://wiki.gentoo.org/wiki/Knowledge_Base:Unmasking_a_package "Knowledge Base:Unmasking a package").

#### [Firefox support]

In Firefox\'s preferences, under Privacy & Security → Security → Certificates → Security Devices, click Load, choose a name such as \"Belgian eID\", and add [/usr/lib64/libbeidpkcs11.so]. Installing the add-on isn\'t necessary.

When using Firefox in a [Firejail](https://wiki.gentoo.org/wiki/Firejail "Firejail"), add this to [/etc/firejail/firefox-common.local] (create the file if necessary):

[FILE] **`/etc/firejail/firefox-common.local`Firejail whitelisting rules for Belgian eID**

    # Belgian eID
    noblacklist /usr/lib/mozilla/pkcs11-modules
    noblacklist /usr/lib64/libbeidpkcs11.so*
    whitelist /run/pcscd/pcscd.comm

### [Estonia]

See [Web eID](https://wiki.gentoo.org/wiki/Web_eID "Web eID").

### [Germany]

`root `[`#`]`emerge --ask sys-auth/AusweisApp`

See [https://www.ausweisapp.bund.de/en/home](https://www.ausweisapp.bund.de/en/home)

## [External resources]

-   [https://wiki.archlinux.org/title/Electronic_identification](https://wiki.archlinux.org/title/Electronic_identification)