[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Sequoia&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://sequoia-pgp.org/)

[[]][Official documentation](https://sequoia-pgp.org/docs/)

[[]][app-crypt/sequoia-sop](https://packages.gentoo.org/packages/app-crypt/sequoia-sop)

[[]][app-crypt/sequoia-sq](https://packages.gentoo.org/packages/app-crypt/sequoia-sq)

[[]][app-crypt/sequoia-sqv](https://packages.gentoo.org/packages/app-crypt/sequoia-sqv)

[[]][GitLab](https://gitlab.com/sequoia-pgp/sequoia)

[[]][[#sequoia](irc://irc.oftc.net/#sequoia) (on [irc://irc.oftc.net](irc://irc.oftc.net)])

[[]][Blog](https://sequoia-pgp.org/blog/)

Sequoia is a complete implementation of OpenPGP as defined by RFC 9580 as well as the deprecated OpenPGP as defined by RFC 4880, and various related standards.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [app-crypt/sequoia-sop]](#app-crypt.2Fsequoia-sop)
        -   [[1.1.1] [USE flags]](#USE_flags)
        -   [[1.1.2] [Emerge]](#Emerge)
    -   [[1.2] [app-crypt/sequoia-sq]](#app-crypt.2Fsequoia-sq)
        -   [[1.2.1] [USE flags]](#USE_flags_2)
        -   [[1.2.2] [Emerge]](#Emerge_2)
    -   [[1.3] [app-crypt/sequoia-sqv]](#app-crypt.2Fsequoia-sqv)
        -   [[1.3.1] [USE flags]](#USE_flags_3)
        -   [[1.3.2] [Emerge]](#Emerge_3)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Generating a private key]](#Generating_a_private_key)
    -   [[2.2] [Exporting a certificate]](#Exporting_a_certificate)
    -   [[2.3] [Publishing a certificate]](#Publishing_a_certificate)
-   [[3] [See also]](#See_also)

## [Installation]

### [][app-crypt/sequoia-sop]

#### [USE flags]

### [USE flags for] [app-crypt/sequoia-sop](https://packages.gentoo.org/packages/app-crypt/sequoia-sop) [[]] [Implementation of the Stateless OpenPGP Command Line Interface using Sequoia]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`botan`](https://packages.gentoo.org/useflags/botan)   Use dev-libs/botan as crypto provider.
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-14 08:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [Emerge]

`root `[`#`]`emerge --ask app-crypt/sequoia-sop`

### [][app-crypt/sequoia-sq]

#### [USE flags]

### [USE flags for] [app-crypt/sequoia-sq](https://packages.gentoo.org/packages/app-crypt/sequoia-sq) [[]] [CLI of the Sequoia OpenPGP implementation]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`botan`](https://packages.gentoo.org/useflags/botan)   Use dev-libs/botan as crypto provider.
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-25 16:46] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [Emerge]

`root `[`#`]`emerge --ask app-crypt/sequoia-sq`

### [][app-crypt/sequoia-sqv]

#### [USE flags]

### [USE flags for] [app-crypt/sequoia-sqv](https://packages.gentoo.org/packages/app-crypt/sequoia-sqv) [[]] [A simple OpenPGP signature verification program]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`botan`](https://packages.gentoo.org/useflags/botan)   Use dev-libs/botan as crypto provider.
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-14 08:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [Emerge]

`root `[`#`]`emerge --ask app-crypt/sequoia-sqv`

## [Usage]

** Tip**\
Sequoia refers to commonly known OpenPGP terms differently. For example, private keys are called, \"keys\", and public keys are referred to as, \"certificates\". For the full list of terminology changes, refer to the official documentation [here](https://book.sequoia-pgp.org/getting_started.html#terminology)

### [Generating a private key]

To generate a key with Sequoia, use [sq]:

`user `[`$`]`sq key generate --own-key --name="Larry the Cow" --email=larry@gentoo.org`

    Please enter the password to protect key (press enter to not use a password):
                                                      Please repeat the password:
     - ┌ CD6FD5384B28BFAD8E3DAAE0ACDF8D7BA1B01D45
       └ Larry the Cow
       - certification created

     - ┌ CD6FD5384B28BFAD8E3DAAE0ACDF8D7BA1B01D45
       └ <larry@gentoo.org>
       - certification created

    Transferable Secret Key.

          Fingerprint: CD6FD5384B28BFAD8E3DAAE0ACDF8D7BA1B01D45
      Public-key algo: EdDSA
      Public-key size: 256 bits
           Secret key: Unencrypted
        Creation time: 2025-12-30 03:07:04 UTC
      Expiration time: 2028-12-29 20:33:25 UTC (creation time + 2years 11months 30days 9h 16m 45s)
            Key flags: certification

               Subkey: 9973D6CA7A958FE5480EA80E1E844D52E76956F2
      Public-key algo: EdDSA
      Public-key size: 256 bits
           Secret key: Unencrypted
        Creation time: 2025-12-30 03:07:04 UTC
      Expiration time: 2028-12-29 20:33:25 UTC (creation time + 2years 11months 30days 9h 16m 45s)
            Key flags: authentication

               Subkey: 38FBC49A9FDD30D9C2B8CC76435C985217FB9A04
      Public-key algo: EdDSA
      Public-key size: 256 bits
           Secret key: Unencrypted
        Creation time: 2025-12-30 03:07:04 UTC
      Expiration time: 2028-12-29 20:33:25 UTC (creation time + 2years 11months 30days 9h 16m 45s)
            Key flags: signing

               Subkey: 83A17D6143D68378BA7200F6A9E1CD39D1245FA0
      Public-key algo: ECDH
      Public-key size: 256 bits
           Secret key: Unencrypted
        Creation time: 2025-12-30 03:07:04 UTC
      Expiration time: 2028-12-29 20:33:25 UTC (creation time + 2years 11months 30days 9h 16m 45s)
            Key flags: transport encryption, data-at-rest encryption

               UserID: <larry@gentoo.org>
       Certifications: 1, use --certifications to list

               UserID: Larry the Cow
       Certifications: 1, use --certifications to list

    Hint: Because you supplied the `--own-key` flag, the user IDs on this key have been marked as authenticated, and this key has been marked as
          a fully trusted introducer.  If that was a mistake, you can undo that with:

      $ sq pki link retract --cert=CD6FD5384B28BFAD8E3DAAE0ACDF8D7BA1B01D45 --all

    Hint: You can export your certificate as follows:

      $ sq cert export --cert=CD6FD5384B28BFAD8E3DAAE0ACDF8D7BA1B01D45

    Hint: Once you are happy you can upload it to public directories using:

      $ sq network keyserver publish --cert=CD6FD5384B28BFAD8E3DAAE0ACDF8D7BA1B01D45

### [Exporting a certificate]

To export the certificate of a key, use [sq cert export]:

`user `[`$`]`sq cert export --cert-email larry@gentoo.org`

### [Publishing a certificate]

To publish a certificate, use [sq network]:

`user `[`$`]`sq network keyserver publish --cert CD6FD5384B28BFAD8E3DAAE0ACDF8D7BA1B01D45`

## [See also]

-   [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") --- a free implementation of the OpenPGP standard (RFC 4880).