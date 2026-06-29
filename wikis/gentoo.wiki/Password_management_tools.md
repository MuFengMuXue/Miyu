This meta article is dedicated to secure password generation, auditing of generated passwords for security, and management of existing passwords.

## Contents

-   [[1] [Password managers]](#Password_managers)
    -   [[1.1] [fpm2]](#fpm2)
    -   [[1.2] [gorilla]](#gorilla)
    -   [[1.3] [KeePass]](#KeePass)
    -   [[1.4] [KeePassXC]](#KeePassXC)
        -   [[1.4.1] [keepassxc-cli]](#keepassxc-cli)
    -   [[1.5] [kpcli]](#kpcli)
    -   [[1.6] [pass]](#pass)
    -   [[1.7] [pwman3]](#pwman3)
    -   [[1.8] [pwsafe]](#pwsafe)
    -   [[1.9] [Revelation]](#Revelation)
    -   [[1.10] [tkpasman]](#tkpasman)
-   [[2] [Password generators]](#Password_generators)
    -   [[2.1] [Apg]](#Apg)
    -   [[2.2] [keepassxc-cli]](#keepassxc-cli_2)
    -   [[2.3] [makepasswd]](#makepasswd)
    -   [[2.4] [pwgen]](#pwgen)
    -   [[2.5] [pwqgen]](#pwqgen)
    -   [[2.6] [ranpwd]](#ranpwd)
    -   [[2.7] [xkcdpass]](#xkcdpass)

# [Password managers]

Generated passwords are extremely random and difficult to remember, therefore a password manager should be employed.

## [fpm2]

[[[x11-misc/fpm2]](https://packages.gentoo.org/packages/x11-misc/fpm2)[]] is a [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") password manager utility with password generator.

## [gorilla]

[[[app-crypt/gorilla]](https://packages.gentoo.org/packages/app-crypt/gorilla)[]] is a [Password Safe](https://pwsafe.org/) clone for Linux. It stores passwords in secure way with GUI interface.

## [KeePass]

[[[app-admin/keepass]](https://packages.gentoo.org/packages/app-admin/keepass)[]] is a light-weight password management system. KeePass depends on [Mono](https://en.wikipedia.org/wiki/Mono_(software) "wikipedia:Mono (software)").

## [KeePassXC]

[KeePassXC](https://wiki.gentoo.org/wiki/KeePassXC "KeePassXC") is a fork of KeePassX that aims to incorporate stalled pull requests, features, and bug fixes that have never made it into the main KeePassX repository.

### [keepassxc-cli]

[KeePassXC/cli](https://wiki.gentoo.org/wiki/KeePassXC/cli "KeePassXC/cli")- command line interface for the KeePassXC password manager.

## [kpcli]

[[[app-admin/kpcli]](https://packages.gentoo.org/packages/app-admin/kpcli)[]] is a minimal command line interface to KeePass database files, that also supports Password Safe v3 databases.

## [pass]

[pass](https://wiki.gentoo.org/wiki/Pass "Pass") stores, retrieves, generates, and synchronizes passwords securely using [[[app-crypt/gnupg]](https://packages.gentoo.org/packages/app-crypt/gnupg)[]], [[[app-admin/pwgen]](https://packages.gentoo.org/packages/app-admin/pwgen)[]], and [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]].

The password store (or pass) is a simple shell script, which provides commands for conveniently storing passwords in separated PGP encrypted files, temporally copying a password to clipboard, and tracking changes using git. It realizes password management in respect to the Unix philosophy.

There\'s also a [GUI client](https://qtpass.org), a [Firefox plugin](https://github.com/passff/passff), and an [iOS interface](https://mssun.github.io/passforios/).

For further details visit the project\'s [homepage](https://www.passwordstore.org/).

## [pwman3]

[[[app-admin/pwman3]](https://packages.gentoo.org/packages/app-admin/pwman3)[]] is a command-line password manager written in python3 with multiple database backends.

## [pwsafe]

[[[app-misc/pwsafe]](https://packages.gentoo.org/packages/app-misc/pwsafe)[]] is a command-line password manager compatible with [Password Safe](https://pwsafe.org/).

## [Revelation]

[[[x11-misc/revelation]](https://packages.gentoo.org/packages/x11-misc/revelation)[]] is a password management system for GNOME. It is also suitable for non GNOME users.

## [tkpasman]

[[[app-misc/tkpasman]](https://packages.gentoo.org/packages/app-misc/tkpasman)[]] is a useful and reliable personal password manager written in Tcl/Tk.

# [Password generators]

## [Apg]

Apg\'s default settings do not enforce usage of uppercase letters, numbers or symbols. Use to following command to generate `-n 1` one password that must contain:

-   `C` capital symbols
-   `N` numeral symbols
-   `S` special symbols

having a length of minimum `-m 80` chars:

`user `[`$`]`apg -M CNS -m 80 -n 1`

    squahitAbVuipvonnokjorg@keHaisGewkyibgetvudTacPicCozRalikisIbgenByct9WribOk#Twip

## [keepassxc-cli]

Generate password of the lenght `-L 64`:

`user `[`$`]`keepassxc-cli generate -L 64`

    f5SKVfgveA75y743t4owHN5amYMAe4SnUCfNsupYs2MYo7n7MX9d9ZYfYxTNT3yt

Generate diceware with 3 words

`user `[`$`]`keepassxc-cli diceware -W 3`

    platonic blinks camping

## [makepasswd]

[[[app-admin/makepasswd]](https://packages.gentoo.org/packages/app-admin/makepasswd)[]] is a random password generator.

`user `[`$`]`makepasswd --minchars=20 --maxchars=40`

    fWyMUaKeQ5M7RIrWQuKS6B44TF9RjEpoTIt

## [pwgen]

[[[app-admin/pwgen]](https://packages.gentoo.org/packages/app-admin/pwgen)[]] is a password generator. Generate `1` password of the length `32`:

`user `[`$`]`pwgen 32 1`

    Ohn3sheeNgowoghiemie1EeY5taich3e

## [pwqgen]

[[[passwdqc]](https://packages.gentoo.org/packages/passwdqc)[]] ships with the program `pwqgen` and is pulled in by [[[sys-auth/pambase]](https://packages.gentoo.org/packages/sys-auth/pambase)[]] so is already installed on most systems. It will generate an easier to remember passphrase of random words separated by numbers and special characters.

Generate a passphrase using 64 bits of entropy:

`user `[`$`]`pwqgen random=64`

    asylum9wide7defend6flint

## [ranpwd]

[[[app-admin/ranpwd]](https://packages.gentoo.org/packages/app-admin/ranpwd)[]] generates random passwords using the in-kernel cryptographically secure random number generator. Generate password of the length `40`.

`user `[`$`]`ranpwd 40`

    6(+qa7qI/C%DJ<[`$`]`xkcdpass -n 4`

    humorous irritate frozen kitchen