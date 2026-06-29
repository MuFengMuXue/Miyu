[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Pass&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.passwordstore.org/)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/pass)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Pass_(software) "wikipedia:Pass (software)")

[[]][GitWeb](https://git.zx2c4.com/password-store/)

[[]][pass(1)](https://linux.die.net/man/1/pass)

[pass] is a command-line password manager that stores, retrieves, generates, and synchronizes passwords securely. It integrates directly with the user\'s [PGP](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") keys to store password in encrypted format on disk. Pass is written in [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") and was created by Gentoo developer [Jason A. Donenfeld (Zx2c4) ](https://wiki.gentoo.org/wiki/User:Zx2c4 "User:Zx2c4").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
        -   [[1.3.1] [Plugins]](#Plugins)
        -   [[1.3.2] [Browser add-ons]](#Browser_add-ons)
        -   [[1.3.3] [Compatible tools]](#Compatible_tools)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
-   [[3] [Initial Setup]](#Initial_Setup)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [pass-otp]](#pass-otp)
    -   [[4.2] [ViM]](#ViM)
    -   [[4.3] [Invocation]](#Invocation)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/pass](https://packages.gentoo.org/packages/app-admin/pass) [[]] [Stores, retrieves, generates, and synchronizes passwords securely]

  --------------------------------------------------------------- -------------------------------------------------------------------------------------------
  [`+git`](https://packages.gentoo.org/useflags/+git)             Use dev-vcs/git for password revisions.
  [`X`](https://packages.gentoo.org/useflags/X)                   Use x11-misc/xclip to copy passwords to the clipboard.
  [`dmenu`](https://packages.gentoo.org/useflags/dmenu)           Add support for x11-misc/dmenu with the \'passmenu\' program.
  [`emacs`](https://packages.gentoo.org/useflags/emacs)           Add support for GNU Emacs
  [`importers`](https://packages.gentoo.org/useflags/importers)   Allow importing passwords from other password managers using various contributed scripts.
  [`wayland`](https://packages.gentoo.org/useflags/wayland)       Enable dev-libs/wayland backend
  --------------------------------------------------------------- -------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-02 05:04] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-admin/pass`

### [Additional software]

#### [Plugins]

-   [[[app-admin/pass-audit::guru]](https://gpo.zugaina.org/Overlays/guru/app-admin/pass-audit)[]] - Audit your password repository.
-   [[[app-admin/pass-otp]](https://packages.gentoo.org/packages/app-admin/pass-otp)[]] - Manage and generate one-time passwords (OTP).
-   [[[app-admin/pass-import]](https://packages.gentoo.org/packages/app-admin/pass-import)[]] - Import passwords from other password managers.
-   [[[app-admin/pass-update]](https://packages.gentoo.org/packages/app-admin/pass-update)[]] - Update your passwords.

#### [Browser add-ons]

-   [[[www-plugins/browserpass]](https://packages.gentoo.org/packages/www-plugins/browserpass)[]]
-   [[[www-plugins/passff-host]](https://packages.gentoo.org/packages/www-plugins/passff-host)[]]

#### [Compatible tools]

-   [[[app-admin/qtpass]](https://packages.gentoo.org/packages/app-admin/qtpass)[]] - [Qt](https://wiki.gentoo.org/wiki/Qt "Qt") GUI for [pass].
-   [[[gui-apps/tessen::guru]](https://gpo.zugaina.org/Overlays/guru/gui-apps/tessen)[]] - Interactive menu to autotype and copy [pass] data.
-   [[[kde-misc/plasma-pass]](https://packages.gentoo.org/packages/kde-misc/plasma-pass)[]] - [Plasma](https://wiki.gentoo.org/wiki/Plasma "Plasma") applet to access passwords from [pass].

## [Configuration]

For initial steps and configuration read the pass man pages:

`user `[`$`]`man pass`

\

### [Environment variables]

-   `PASSWORD_STORE_DIR` --- Overrides the default password storage directory.
-   `PASSWORD_STORE_KEY` --- Overrides the default gpg key identification set by init.
-   `PASSWORD_STORE_GPG_OPTS` --- Additional options to be passed to all invocations of GPG.
-   `PASSWORD_STORE_X_SELECTION` --- Overrides the selection passed to [xclip].
-   `PASSWORD_STORE_CLIP_TIME` --- Specifies the number of seconds to wait before restoring the clipboard, by default 45 seconds.
-   `PASSWORD_STORE_UMASK` --- Sets the umask of all files modified by pass, by default 077.
-   `PASSWORD_STORE_GENERATED_LENGTH` --- The default password length if the pass-length parameter to generate is unspecified.
-   `PASSWORD_STORE_CHARACTER_SET` --- The character set to be used in password generation for generate.
-   `PASSWORD_STORE_CHARACTER_SET_NO_SYMBOLS` --- The character set to be used in no-symbol password generation.
-   `PASSWORD_STORE_ENABLE_EXTENSIONS` --- This environment variable must be set to \"true\" for extensions to be enabled.
-   `PASSWORD_STORE_EXTENSIONS_DIR` --- The location to look for executable extension files, by default [\$PASSWORD_STORE_DIR/.extensions].
-   `PASSWORD_STORE_SIGNING_KEY` --- If this environment variable is set, then all [.gpg-id] files and non-system extension files must be signed using a detached signature using the GPG key specified by the full 40 character uppercase fingerprint in this variable. If multiple fingerprints are specified, each separated by a whitespace character, then signatures must match at least one. The init command will keep signatures of [.gpg-id] files up to date.
-   `EDITOR` --- The location of the text editor used by edit.

### [Files]

-   [\~/.password-store] --- The default password storage directory.
-   [\~/.password-store/.gpg-id] --- Contains the default gpg key identification used for encryption and decryption. Multiple gpg keys may be specified in this file, one per line. If this file exists in any sub directories, passwords inside those sub directories are encrypted using those keys. This should be set using the init command.
-   [\~/.password-store/.extensions] --- The directory containing extension files.

## [Initial Setup]

Most likely when you first invoke [pass] you\'ll get output that looks something like this:

`user `[`$`]`pass`

    Error: password store is empty. Try "pass init".

Without additional configuration, if you run [pass init] as directed, you\'ll get the following output:

`user `[`$`]`pass init`

    Usage: pass init [--path=subfolder,-p subfolder] gpg-id...

To initialize your password store:

`user `[`$`]`pass init <your_gpg_key_id>`

To confirm everything is correct, run [pass] with no arguments and you should see an empty password store:

`user `[`$`]`pass`

    Password Store

pass integrates well with [Git](https://wiki.gentoo.org/wiki/Git "Git") to store changes, even configuring a diff filter so that [git log -p] works automatically to show decrypted secrets. To set that up, just run:

`user `[`$`]`pass git init`

## [Usage]

pass is flexible. Entry names can be URLs, usernames, email addresses. The user chooses the hierarchy, but it can also be relocated later at-will. For example, [pass generate me/calendar/larry@example.com] is valid, as is [pass generate example.com].

Any format can be used within the entries created, but there are some [conventions](https://codeberg.org/PassFF/passff#password-formats) relied upon by e.g. PassFF for autofill to work correctly.

The first line is almost always the password itself. The rest varies: sometimes explicit field names are given and sometimes not.

A common style is as follows:

`user `[`$`]`pass edit gentoo/larry`

    asekritpassword
    username: larry
    url: https://bugs.gentoo.org/

One can also encode the username (or indeed URL) in the path to the entry.

#### [pass-otp]

Adding a [pass] entry for the user larry:

`user `[`$`]`pass edit gentoo/larry`

Example [pass] entry generating (OTP) one-time passwords:

`user `[`$`]`pass show gentoo/larry`

    otpauth://totp/larry@gentoo?secret=ZBURIWIVW5UQP4F5PYZ75LHTXU======

Generating a (OTP) one-time password using [pass otp] command:

`user `[`$`]`pass otp gentoo/larry`

    076884

#### [ViM]

** Tip**\
Users of [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") or [Neovim](https://wiki.gentoo.org/wiki/Neovim "Neovim") should configure the editor not to write the password to disk when using [pass edit] command, which can inadvertently happen with options such as `swapfile` and `undofile`. There is a plugin to set the appropriate options when the editor is editing a password file at [https://dev.sanctum.geek.nz/cgit/vim-redact-pass.git](https://dev.sanctum.geek.nz/cgit/vim-redact-pass.git). Like other Vim plugins, this can be installed using a plugin manager or by placing the files in an appropriate location manually.

### [Invocation]

`user `[`$`]`pass --help`

    ============================================
    = pass: the standard unix password manager =
    =                                          =
    =                  v1.7.4                  =
    =                                          =
    =             Jason A. Donenfeld           =
    =               Jason@zx2c4.com            =
    =                                          =
    =      http://www.passwordstore.org/       =
    ============================================

    Usage:
        pass init [--path=subfolder,-p subfolder] gpg-id...
            Initialize new password storage and use gpg-id for encryption.
            Selectively reencrypt existing passwords using new gpg-id.
        pass [ls] [subfolder]
            List passwords.
        pass find pass-names...
            List passwords that match pass-names.
        pass [show] [--clip[=line-number],-c[line-number]] pass-name
            Show existing password and optionally put it on the clipboard.
            If put on the clipboard, it will be cleared in 45 seconds.
        pass grep [GREPOPTIONS] search-string
            Search for password files containing search-string when decrypted.
        pass insert [--echo,-e | --multiline,-m] [--force,-f] pass-name
            Insert new password. Optionally, echo the password back to the console
            during entry. Or, optionally, the entry may be multiline. Prompt before
            overwriting existing password unless forced.
        pass edit pass-name
            Insert a new password or edit an existing password using /usr/bin/vim.
        pass generate [--no-symbols,-n] [--clip,-c] [--in-place,-i | --force,-f] pass-name [pass-length]
            Generate a new password of pass-length (or 25 if unspecified) with optionally no symbols.
            Optionally put it on the clipboard and clear board after 45 seconds.
            Prompt before overwriting existing password unless forced.
            Optionally replace only the first line of an existing file with a new password.
        pass rm [--recursive,-r] [--force,-f] pass-name
            Remove existing password or directory, optionally forcefully.
        pass mv [--force,-f] old-path new-path
            Renames or moves old-path to new-path, optionally forcefully, selectively reencrypting.
        pass cp [--force,-f] old-path new-path
            Copies old-path to new-path, optionally forcefully, selectively reencrypting.
        pass git git-command-args...
            If the password store is a git repository, execute a git command
            specified by git-command-args.
        pass help
            Show this text.
        pass version
            Show version information.

    More information may be found in the pass(1) man page.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-admin/pass`

## [See also]

-   [KeePassXC/cli](https://wiki.gentoo.org/wiki/KeePassXC/cli "KeePassXC/cli") --- a command line interface for the KeePassXC password manager.
-   [Password management tools](https://wiki.gentoo.org/wiki/Password_management_tools "Password management tools") --- This meta article is dedicated to secure password generation, auditing of generated passwords for security, and management of existing passwords.
-   [Jason A. Donenfeld (Zx2c4) ](https://wiki.gentoo.org/wiki/User:Zx2c4 "User:Zx2c4")\'s wiki page.
-   [Google Authenticator](https://wiki.gentoo.org/wiki/Google_Authenticator "Google Authenticator") --- describes an easy way to setup two-factor authentication on Gentoo.
-   [OATH-Toolkit](https://wiki.gentoo.org/wiki/OATH-Toolkit "OATH-Toolkit") --- toolkit for (OTP) One-Time Password authentication using HOTP/TOTP algorithms.

## [External resources]

-   [List of integrations](https://www.passwordstore.org/#) on project website.
-   [https://vitalyparnas.com/guides/pass/](https://vitalyparnas.com/guides/pass/) - A blog post covering clever uses of pass.