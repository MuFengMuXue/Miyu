**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

CrackLib was a follow-up version of the libCrack password checking library and is licensed under the LGPL. With [[[sys-libs/pam]](https://packages.gentoo.org/packages/sys-libs/pam)[]]-1.4.0^[\[1\]](#cite_note-1)^ it has been deprecated in favor of [[[sys-auth/passwdqc]](https://packages.gentoo.org/packages/sys-auth/passwdqc)[]]. See [PAM](https://wiki.gentoo.org/wiki/PAM "PAM") for current configuration.

## Contents

-   [[1] [Passwords policy]](#Passwords_policy)
    -   [[1.1] [CrackLib]](#CrackLib)
    -   [[1.2] [Unix password policy]](#Unix_password_policy)
    -   [[1.3] [SAMBA passwords policy]](#SAMBA_passwords_policy)
        -   [[1.3.1] [Using pdbedit]](#Using_pdbedit)
        -   [[1.3.2] [CrackCheck]](#CrackCheck)
-   [[2] [External resources]](#External_resources)

## [Passwords policy]

### [CrackLib]

Add the `cracklib` **USE** flag to [/etc/portage/make.conf] and re-emerge world to update any package that include support for CrackLib:

`root `[`#`]`emerge --changed-use @world`

Verify these two packages are installed:

`root `[`#`]`emerge --changed-use `[[[`sys-libs/cracklib`]](https://packages.gentoo.org/packages/sys-libs/cracklib)[]]` `[[[`sys-apps/cracklib-words`]](https://packages.gentoo.org/packages/sys-apps/cracklib-words)[]]

Now create a database:

`root `[`#`]`create-cracklib-dict /usr/share/dict/*`

### [Unix password policy]

### [SAMBA passwords policy]

#### [Using pdbedit]

[pdbedit](https://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/passdb.html#pdbeditthing) is a tool that can be used only by root. It is used to manage the passdb backend, as well as domain-wide account policy settings. pdbedit can be used to:

-   Add, remove, or modify user accounts.
-   List user accounts.
-   Migrate user accounts.
-   Migrate group accounts.
-   Manage account policies.
-   Manage domain access policy settings.

Commands will be executed to establish controls for our domain as follows:

1.  Min password length = 8 characters.
2.  Password history = last 4 passwords.
3.  Maximum password age = 90 days.
4.  Minimum password age = 7 days.
5.  Bad lockout attempt = 8 bad log on attempts.
6.  Lockout duration = forever, account must be manually re-enabled.

The following command execution will achieve these settings:

`root `[`#`]`pdbedit -P "min password length" -C 8`

    account policy value for min password length was 5
    account policy value for min password length is now 8

`root `[`#`]`pdbedit -P "password history" -C 4`

    account policy value for password history was 0
    account policy value for password history is now 4

`root `[`#`]`pdbedit -P "maximum password age" -C 7776000`

    account policy value for maximum password age was 4294967295
    account policy value for maximum password age is now 7776000

`root `[`#`]`pdbedit -P "minimum password age" -C 604800`

    account policy value for minimum password age was 0
    account policy value for minimum password age is now 7

`root `[`#`]`pdbedit -P "bad lockout attempt" -C 8`

    account policy value for bad lockout attempt was 0
    account policy value for bad lockout attempt is now 8

`root `[`#`]`pdbedit -P "lockout duration" -C -1`

    account policy value for lockout duration was 30
    account policy value for lockout duration is now 4294967295

#### [CrackCheck]

Next [crackcheck](https://lists.samba.org/archive/samba/2009-December/152634.html) can be used to check complicity of passwords:

Unpack samba-\*.tar.gz and [cd] to [examples/auth/crackcheck]. Then compile it:

`user `[`$`]`make`

Copy this to somewhere more sensible:

`user `[`$`]`cp crackcheck /usr/local/sbin`

Edit Samba\'s configuration file:

[FILE] **`/etc/samba/smb.conf`Samba\'s configuration**

    check password script = /usr/local/sbin/crackcheck -s -d /usr/lib/cracklib-dict

Reload samba configuration:

`root `[`#`]`/etc/init.d/samba reload`

## [External resources]

-   [pdbedit](https://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/passdb.html#pdbeditthing)
-   [crackcheck](https://lists.samba.org/archive/samba/2009-December/152634.html)

1.  [[[↑](#cite_ref-1)] [[News Item](https://www.gentoo.org/support/news-items/2020-06-23-upgrade-to-sys-libs_pam-1_4_0.html)]]