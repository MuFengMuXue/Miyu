**Resources**

[[]][Home](https://keepassxc.org)

[[]][Official documentation](https://keepassxc.org/docs/)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/keepassxc)

[[]][User Guide](https://keepassxc.org/docs/KeePassXC_UserGuide)

[[]][GitHub](https://github.com/keepassxreboot/keepassxc)

[[]][Bugs (upstream)](https://github.com/keepassxreboot/keepassxc/issues)

[[]][keepassxc(1)](https://github.com/keepassxreboot/keepassxc/blob/develop/docs/man/keepassxc.1.adoc)

[[]][[#keepassxc](ircs://irc.libera.chat/#keepassxc)] ([[webchat](https://web.libera.chat/#keepassxc)])

**KeePassXC** is a modern, secure, open-source, and cross-platform password manager. It is a fork of KeePassX that aims to incorporate stalled pull requests, features, and bug fixes that never made it into the main KeePassX repository.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE Flags]](#USE_Flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Secret Service]](#Secret_Service)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Secret Service]](#Secret_Service_2)
    -   [[3.2] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [KeePassXC cannot detect smart card]](#KeePassXC_cannot_detect_smart_card)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Installation]

### [USE Flags]

### [USE flags for] [app-admin/keepassxc](https://packages.gentoo.org/packages/app-admin/keepassxc) [[]] [KeePassXC - KeePass Cross-platform Community Edition]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+keyring`](https://packages.gentoo.org/useflags/+keyring)       Enable support for use as the the system keyring
  [`+network`](https://packages.gentoo.org/useflags/+network)       Enable network support (e.g. for downloading favicons)
  [`+ssh-agent`](https://packages.gentoo.org/useflags/+ssh-agent)   Use KeePassXC to unlock SSH keys
  [`X`](https://packages.gentoo.org/useflags/X)                     Add support for X11
  [`autotype`](https://packages.gentoo.org/useflags/autotype)       Add support to autotype the passwords into other applications
  [`browser`](https://packages.gentoo.org/useflags/browser)         Enable communication with web browser plugins
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`keeshare`](https://packages.gentoo.org/useflags/keeshare)       Enable KeeShare sharing integration
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`yubikey`](https://packages.gentoo.org/useflags/yubikey)         Enable database unlocking via hardware keys supporting YubiKey-style HMAC-SHA1 protocol
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 20:53] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

To install **KeePassXC**:

`root `[`#`]`emerge --ask app-admin/keepassxc`

## [Configuration]

### [Files]

KeepassXC configuration file containing basic user settings

-   [\~/.config/keepassxc/keepassxc.ini] - Local (per user) configuration file.

### [Secret Service]

KeePassXC also supports the Secret Service API, which allows client applications to securely store secrets in a service running in the user's login session.^[\[1\]](#cite_note-1)^ To enable KeePassXC to handle the Secret Service API, following steps are required:

1.  A new group or database must be created, either via the command-line interface or the graphical user interface. This group or database will be used for integration and can be accessed by applications via libsecret.
2.  The newly created group or database must be exposed to other applications by selecting it in the Database Settings (Database \--\> Database Settings \--\> Secret Service Integration) and confirming the selection.
3.  Now the Secret Service Integration in the settings must be activated, to allow applications to handle their secrets in the created group or database.

If it is not possible to activate the Secret Service Integration of KeePassXC because another Secret Service API is running (e.g. the gnome-secret service) the related secret service must be stopped and removed from auto-start. The [desktop environment documentation](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") (if any, otherwise the [users environment](https://wiki.gentoo.org/wiki/Window_manager "Window manager")) should be referred for guidance on how to do so. A general approach could be to remove the file [/etc/xdg/autostart/gnome-keyring-secrets.desktop] if the blocking service is gnome-keyring. Please make sure to make a backup of the file before removing it.

It is possible that the gnome-keyring secret service or another integration is starting before KeePassXC secret service. This can occur if an application requiring the Secret Service integration, starts before KeePassXC secret service API is running, resulting in KeePassXC\'s integration being blocked and the other service is loaded.

To resolve this, it is possible to simply remove the blocking application. For gnome-keyring for example:

`root `[`#`]`emerge --ask --depclean --verbose gnome-base/gnome-keyring`

## [Usage]

`user `[`$`]`keepassxc`

### [Secret Service]

** Important**\
When using the secret service integration in KeePassXC, it is crucial to ensure that KeePassXC starts before other applications that require the integration, such as web browsers. To achieve this, the autostart option for KeePassXC can be enabled. Moreover, before using applications that need to store secrets, such as browsers, the related group or database for the secret service must be unlocked. Otherwise, if the applications start before an active secret service API is running, they will not be able to store secrets, and users will not stay logged in on websites between browser sessions.

### [Invocation]

`user `[`$`]`keepassxc --help`

    Usage: keepassxc [options] [filename(s)]
    KeePassXC - cross-platform password manager

    Options:
      -h, --help                   Displays help on commandline options.
      --help-all                   Displays help including Qt specific options.
      -v, --version                Displays version information.
      --config <config>            path to a custom config file
      --localconfig <localconfig>  path to a custom local config file
      --lock                       lock all open databases
      --keyfile <keyfile>          key file of the database
      --pw-stdin                   read password of the database from stdin
      --debug-info                 Displays debugging information.
      --allow-screencapture        allow screenshots and app recording
                                   (Windows/macOS)

    Arguments:
      filename(s)                  filenames of the password databases to open (*.kdbx)

## [Troubleshooting]

### [KeePassXC cannot detect smart card]

If KeePassXC cannot detect a hardware key/security key/smart card for Challenge-Response, install [[[app-crypt/ccid]](https://packages.gentoo.org/packages/app-crypt/ccid)[]]; this package contains drivers for various smart cards.

`root `[`#`]`emerge --ask app-crypt/ccid`

\
After the package is installed, restart the [pcscd] service.

`root `[`#`]`rc-service pcscd restart`

\
Now try restarting KeePassXC then re-plugging the smart card; the smart card should be detected. If KeePassXC still cannot detect the smart card, additional steps might need to be taken depending on the manufacturer; a common step is the need to add [udev](https://wiki.gentoo.org/wiki/Udev "Udev") rules for the card; to find the correct rules for the card, see the manufacturer\'s documentation.

\

** Important**\
Installing the stand-alone CCID driver might prevent some applications from reading smart cards depending on certain USE flags.

\
For example, if [[[app-crypt/gnupg]](https://packages.gentoo.org/packages/app-crypt/gnupg)[]] ([GPG](https://wiki.gentoo.org/wiki/GPG "GPG")) is installed with the `smartcard` USE flag, it will include the [scdaemon] service. If the `usb` USE flag is also enabled, [scdaemon] will have the additional functionality of being a smart card reader \-- allowing GPG to read smart cards without any additional dependencies.

\
The issue is that if the stand-alone CCID driver, [[[app-crypt/ccid]](https://packages.gentoo.org/packages/app-crypt/ccid)[]], is installed, it will conflict with the built-in CCID driver for [scdaemon] \-- preventing GPG from reading smart cards. But some packages (such as [KeePassXC]) require the stand-alone driver to use features provided by smart cards. There are two solutions to fix this, both of which make [pcscd] the smart card reader. After a solution has been chosen, see [PCSC-Lite](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite") for additional configuration if needed.

\

-   Solution 1:

Install GPG with the `usb` USE flag disabled then terminate the [gpg-agent] process then restart [pcscd].

[FILE] **`/etc/portage/package.use/gnupg`**

    app-crypt/gnupg -usb

`root `[`#`]`emerge --ask -uND app-crypt/gnupg `

`root `[`#`]`killall gpg-agent `

`root `[`#`]`rc-service pcscd restart `

\

-   Solution 2:

Tell [scdaemon] to not use its built-in CCID driver \-- this has the same affect if we run [scdaemon] with the `--disable-ccid` option; see [man scdaemon].

[FILE] **`~/.gnupg/scdaemon.conf`**

    disable-ccid

Also ensure to terminate the [gpg-agent] process then restart [pcscd].

`root `[`#`]`killall gpg-agent `

`root `[`#`]`rc-service pcscd restart `

## [Removal]

### [Unmerge]

**KeePassXC** can be removed with unmerging it:

`root `[`#`]`emerge --ask --depclean --verbose app-admin/keepassxc`

\

## [See also]

-   [KeePassXC/cli](https://wiki.gentoo.org/wiki/KeePassXC/cli "KeePassXC/cli") --- a command line interface for the KeePassXC password manager.
-   [Password management tools](https://wiki.gentoo.org/wiki/Password_management_tools "Password management tools") --- This meta article is dedicated to secure password generation, auditing of generated passwords for security, and management of existing passwords.
-   [PCSC-Lite](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite") --- implements the PC/SC international standard for PC to smartcard reader communication.

## [External resources]

-   [Documenting KeePass KDBX4 file format](https://palant.info/2023/03/29/documenting-keepass-kdbx4-file-format/)
-   [Discussion on CVE-2023--35866](https://keepassxc.org/blog/2023-06-20-cve-202335866/)
-   [What\'s the difference between KeePass / KeePassX / KeePassXC?](https://superuser.com/questions/878902/whats-the-difference-between-keepass-keepassx-keepassxc)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://specifications.freedesktop.org/secret-service/latest/ch01.html](https://specifications.freedesktop.org/secret-service/latest/ch01.html)]]