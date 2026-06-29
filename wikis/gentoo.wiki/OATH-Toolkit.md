[[]][Home](https://www.nongnu.org/oath-toolkit/)

[[]][Official documentation](https://www.nongnu.org/oath-toolkit/docs.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-auth/oath-toolkit)

[[]][GitLab](https://gitlab.com/oath-toolkit/oath-toolkit)

[[]][Bugs (upstream)](https://gitlab.com/oath-toolkit/oath-toolkit/-/issues)

[[]][Man page](http://man7.org/linux/man-pages/man5/pam.d.5.html)

**OATH-Toolkit** is a free software toolkit for (OTP) One-Time Password authentication using HOTP/TOTP algorithms. The software ships a small set of command line utilities covering most OTP operation related tasks.

This configuration procedure explains OATH-Toolkit PAM authentication using the OpenSSH deamon. Further configuration examples are found in the official documentation.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Client]](#Client)
        -   [[2.1.1] [Generate secret]](#Generate_secret)
        -   [[2.1.2] [Hex secret]](#Hex_secret)
        -   [[2.1.3] [Base32 secret]](#Base32_secret)
    -   [[2.2] [Server]](#Server)
        -   [[2.2.1] [Environment variables]](#Environment_variables)
        -   [[2.2.2] [Files]](#Files)
            -   [[2.2.2.1] [OATH-Toolkit]](#OATH-Toolkit)
            -   [[2.2.2.2] [OpenSSH]](#OpenSSH)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Generate OTP]](#Generate_OTP)
    -   [[3.2] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Debugging authenticaton]](#Debugging_authenticaton)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

Following packages need to be build using PAM authentication support, when configuring authentication on the server:

-   [[[sys-auth/oath-toolkit]](https://packages.gentoo.org/packages/sys-auth/oath-toolkit)[]]
-   [[[net-sys/openssh]](https://packages.gentoo.org/packages/net-sys/openssh)[]]

Create following portage configuration files on the server:

[FILE] **`/etc/portage/package.use/oath-toolkit`Enabling PAM USE flag for oath-toolkit**

    sys-auth/oath-toolkit pam

[FILE] **`/etc/portage/package.use/openssh`Enabling PAM USE flag for openssh**

    net-misc/openssh pam

Rebuild the software listed using `pam` support on the SSH server.

** Note**\
The SSH client does not need `pam` USE flag being enabled using gentoo.

### [USE flags]

### [USE flags for] [sys-auth/oath-toolkit](https://packages.gentoo.org/packages/sys-auth/oath-toolkit) [[]] [Toolkit for using one-time password authentication with HOTP/TOTP algorithms]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`pam`](https://packages.gentoo.org/useflags/pam)                   Build PAM module for pluggable login authentication for OATH
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-13 17:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-auth/oath-toolkit`

### [Additional software]

Install PAM supporting software, the OpenSSH server:

`root `[`#`]`emerge --ask net-misc/openssh`

## [Configuration]

The setup procedure described is taken from the [official website](https://www.nongnu.org/oath-toolkit/pam_oath.html) and applied to gentoo specifics.

### [Client]

Prior to configuration of the OATH-toolkit, each system user needs a secret. The secrets mentioned

-   **Hex secret** [\~/.oath_toolkit] on the target SSH server, as a plain text file, not encrypted.
-   **Base32 secret** in a [password management tools](https://wiki.gentoo.org/wiki/Password_management_tools "Password management tools") on personal computer, mobile, encrypted storage.

#### [Generate secret]

Generating a secret using [oathtool] and the random output of [openssl] library:

`user `[`$`]`oathtool --verbose $(openssl rand -hex 16)`

    Hex secret: c869145915b76907f0bd7e33feacf3bd
    Base32 secret: ZBURIWIVW5UQP4F5PYZ75LHTXU======
    Digits: 6
    Window size: 0
    Start counter: 0x0 (0)

    260781

#### [Hex secret]

** Note**\
This file is stored in the users home directory on the SSH server. It is a plain text file.

Generated Hex secret is stored to [\~/.oath_toolkit] file, using following syntax:

[FILE] **`~/.oath_toolkit`**

    #token         user   PIN  secret
    HOTP/T30       larry  -    c869145915b76907f0bd7e33feacf3bd

The specific entries and the syntax are explained on [the official documentation](https://code.google.com/archive/p/mod-authn-otp/wikis/UsersFile.wiki) website.

Finally restrict the file permissions to be **read** and **write** for to current user only:

`user `[`$`]`chmod go-rw ~/.oath_toolkit`

#### [Base32 secret]

** Tip**\
Use a password managent tool to store secrets and generate OTP one-time passwords.

Use one of the [password management tools](https://wiki.gentoo.org/wiki/Password_management_tools "Password management tools") listed to store the **Base32 secret** encrypted. Password management tools generate the OTP one-time password needed for authentication.

### [Server]

** Warning**\
Keep a login session active during configuration of two-factor authentication and during the authentication verification process, otherwise you might lock out yourself out of the system.

#### [Environment variables]

-   `usersfile` - Specify filename where credentials are stored, f.e. **/etc/users.oath**. The placeholder values **\$** and **\$** may be used to specify the filename on a per-user basis. The values **\$** and **\$** expand to the user\'s username and home directory, respectively.
-   `window` - Specify search depth, an integer typically from **5** to **50** but other values can be useful too.
-   `digits` - Specify number of digits in the one-time password, required when using passwords in usersfile. Supported values are **6** , **7**, and **8**.

#### [Files]

-   [/etc/pam.d/sshd] - OpenSSH\'s PAM module authentication configuration file.
-   [/etc/ssh/sshd_config.d/10_OTP-OATH-toolkit.conf] - Mandatory OpenSSH\'s configuration setting for OATH toolkit.
-   [\$/.oath_toolkit] - Conventional path and filename setting for user credentials.

##### [OATH-Toolkit]

**path** and **filename** variables used for `usersfile:`, can be set to *everything* to match the specific environement needs.

The filename for user credentials is set in this document to [\~/.oath_toolkit]. This is to match the *default naming scheme* of [Google Authenticator](https://wiki.gentoo.org/wiki/Google_Authenticator "Google Authenticator") which creates [\~/.google_authenticator]. It makes both setups easier to compare. Both packages are just different implementations of the same technology.

3 different types of tokens can be configured for the authentication process:

-   **event-based**: `HOTP` - HOTP event-based token with six digit OTP
-   **time-based**: `HOTP/T60/5` - HOTP time-based token with 60 second interval and five digit OTP
-   **mobile**: `MOTP` - Mobile-OTP time-based token 10 second interval and six digit OTP

Further file format and parameter examples are listed in [the official documentation](https://code.google.com/archive/p/mod-authn-otp/wikis/UsersFile.wiki) website.

##### [OpenSSH]

Following steps are mandatory for the PAM authentication to work:

**PAM**

Read the PAM module manual for the configuration parameters set in [/etc/pam.d/sshd]:

`user `[`$`]`man pam.conf`

Further specific module configuration parameters used (*usersfile=, window=,digits=*) for **pam_oath.so** are explained in the [manual for pam_oath on the official website](https://www.nongnu.org/oath-toolkit/pam_oath.html).

Add the first **requisite** configuration line to the [/etc/pam.d/sshd] file, and keep the added rule at the highest position in this file:

[FILE] **`/etc/pam.d/sshd`Set *\$/.oath_toolkit* as default credentials file**

    auth       requisite    pam_oath.so usersfile=$/.oath_toolkit window=20 digits=6
    auth       include      system-remote-login
    account    include      system-remote-login
    password   include      system-remote-login
    session    include      system-remote-login

**Authentication**

Create OATH specific autentication configuration:

[FILE] **`/etc/ssh/sshd_config.d/10_OTP-OATH-toolkit.conf`**

    UsePAM yes
    ChallengeResponseAuthentication yes

After applied configuration settings, restart the openssh daemon:

`root `[`#`]`service sshd restart`

## [Usage]

Demostration of a working 2FA authentication sequence for a example SSH session for [larry](https://wiki.gentoo.org/wiki/Larry "Larry"):

`user `[`$`]`ssh gentoo`

    (larry@gentoo) One-time password (OATH) for `larry':
    (larry@gentoo) Password:
    larry@gentoo ~ $

The authenticating SSH user **larry** will get displayed:

1.  display `` One-time password (OATH) for `larry': `` at the prompt. User OTP authentication.
2.  IF the put in token is found VALID, THEN display `Password:` at the prompt. User keyboard-interactive authentication.

Once a user authentication process has been successfully finished, [\~/.oath_toolkit] will show a added timestamp. Timestamp for the **last** successful authentication, and the used (OTP) one-time password `665004`:

[FILE] **`/home/larry/.oath_toolkit`**

    #token         user   PIN  secret
    HOTP/T30        larry   -       c869145915b76907f0bd7e33feacf3bd  0       665004  2024-01-11T13:37:42L

### [Generate OTP]

** Tip**\
Use a password managent tool to store secrets and generate OTP one-time passwords.

Example how to generate a OTP one-time password token using the [oathtool] and the given secrets.

Generate a one-time password using the Hex secret:`c869145915b76907f0bd7e33feacf3bd`:

`user `[`$`]`oathtool --totp c869145915b76907f0bd7e33feacf3bd`

    665004

Generate a one-time password using the Base32 secret:`ZBURIWIVW5UQP4F5PYZ75LHTXU`:

`user `[`$`]`oathtool --totp -b ZBURIWIVW5UQP4F5PYZ75LHTXU`

    665004

### [Invocation]

`user `[`$`]`oathtool --help`

    Usage: oathtool [OPTION]... [KEY [OTP]]...
    Generate and validate OATH one-time passwords.  KEY and OTP is the string '-'
    to read from standard input, '@FILE' to read from indicated filename, or a hex
    encoded value (not recommended on multi-user systems).

      -h, --help                    Print help and exit
      -V, --version                 Print version and exit
          --hotp                    use event-based HOTP mode  (default=on)
          --totp[=MODE]             use time-variant TOTP mode (values "SHA1",
                                      "SHA256", or "SHA512")  (default=`SHA1')
      -b, --base32                  use base32 encoding of KEY instead of hex
                                      (default=off)
      -c, --counter=COUNTER         HOTP counter value
      -s, --time-step-size=DURATION TOTP time-step duration  (default=`30s')
      -S, --start-time=TIME         when to start counting time steps for TOTP
                                      (default=`1970-01-01 00:00:00 UTC')
      -N, --now=TIME                use this time as current time for TOTP
                                      (default=`now')
      -d, --digits=DIGITS           number of digits in one-time password
      -w, --window=WIDTH            number of additional OTPs to generate or
                                      validate against
      -v, --verbose                 explain what is being done  (default=off)

    Report bugs to: oath-toolkit-help@nongnu.org
    oathtool home page: <https://www.nongnu.org/oath-toolkit/>
    General help using GNU software: <https://www.gnu.org/gethelp/>

## [Troubleshooting]

### [Debugging authenticaton]

To get more verbose debug while troubleshooting authentication configuration, add the **debug** configuraton option to the system PAM module used. In example shown enabling debug on [su] binary.

[FILE] **`/etc/pam.d/su`**

    auth [user_unknown=ignore success=ok] pam_oath.so debug usersfile=/etc/users.oath window=20

Run [su]. At the prompt type anything for the password and the OTP token to get interactive debug output:

`user `[`$`]`su`

    [pam_oath.c:parse_cfg(122)] called.
    [pam_oath.c:parse_cfg(123)] flags 0 argc 4
    [pam_oath.c:parse_cfg(125)] argv[0]=alwaysok
    [pam_oath.c:parse_cfg(125)] argv[1]=debug
    [pam_oath.c:parse_cfg(125)] argv[2]=usersfile=/etc/users.oath
    [pam_oath.c:parse_cfg(125)] argv[3]=window=20
    [pam_oath.c:parse_cfg(126)] debug=1
    [pam_oath.c:parse_cfg(127)] alwaysok=1
    [pam_oath.c:parse_cfg(128)] try_first_pass=0
    [pam_oath.c:parse_cfg(129)] use_first_pass=0
    [pam_oath.c:parse_cfg(130)] usersfile=/etc/users.oath
    [pam_oath.c:parse_cfg(131)] digits=0
    [pam_oath.c:parse_cfg(132)] window=20
    [pam_oath.c:pam_sm_authenticate(162)] get user returned: root
    One-time password (OATH) for `root':
    [pam_oath.c:pam_sm_authenticate(237)] conv returned: 328482
    [pam_oath.c:pam_sm_authenticate(297)] OTP: 328482
    [pam_oath.c:pam_sm_authenticate(308)] authenticate rc 0 last otp Wed Jan  3 19:22:50 2024
    [pam_oath.c:pam_sm_authenticate(329)] done. [Success]
    [pam_oath.c:pam_sm_setcred(341)] called.
    [pam_oath.c:pam_sm_setcred(347)] retval: 0
    [pam_oath.c:pam_sm_setcred(367)] done. [Success]

Applications need to be rebuild using the `debug` portage USE flag to generate more verbose authentication logs.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-auth/oath-toolkit`

## [See also]

-   [Google Authenticator](https://wiki.gentoo.org/wiki/Google_Authenticator "Google Authenticator") --- describes an easy way to setup two-factor authentication on Gentoo.
-   [PAM](https://wiki.gentoo.org/wiki/PAM "PAM") --- allows (third party) services to provide an authentication module for their service which can then be used on PAM enabled systems.
-   [PAM securetty](https://wiki.gentoo.org/wiki/PAM_securetty "PAM securetty") --- restricting [root] authentication with [PAM](https://wiki.gentoo.org/wiki/PAM "PAM").
-   [Password management tools](https://wiki.gentoo.org/wiki/Password_management_tools "Password management tools") --- This meta article is dedicated to secure password generation, auditing of generated passwords for security, and management of existing passwords.
-   [YubiKey](https://wiki.gentoo.org/wiki/YubiKey "YubiKey") --- a hardware security device that can be used to safely store cryptographic keys, OTP tokens, and challenge response seeds

## [External resources]

-   [https://www.nongnu.org/oath-toolkit/pam_oath.html](https://www.nongnu.org/oath-toolkit/pam_oath.html)
-   [OATH Reference Architecture - Specifications and Technical Resources](https://openauthentication.org/specifications-technical-resources/)
-   [users.oath file - Official format description and FAQ](https://code.google.com/archive/p/mod-authn-otp/wikis/UsersFile.wiki)
-   [RFC 4226 - HOTP: An HMAC-Based One-Time Password Algorithm](https://www.rfc-editor.org/rfc/rfc4226.html)
-   [RFC 6238 - TOTP: Time-Based One-Time Password Algorithm](https://www.rfc-editor.org/rfc/rfc6238.html)
-   [RFC 6287 - OCRA: OATH Challenge-Response Algorithm](https://www.rfc-editor.org/rfc/rfc6287.html)