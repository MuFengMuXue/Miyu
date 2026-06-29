This page contains [[changes](https://wiki.gentoo.org/index.php?title=CONFIG_PROTECT&oldid=1426103&diff=1441743)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/de "CONFIG PROTECT (25% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/es "CONFIG_PROTECT (La variable) (17% translated)")
-   [français](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/fr "CONFIG_PROTECT (83% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/it "CONFIG_PROTECT (8% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/hu "CONFIG_PROTECT (83% translated)")
-   [polski](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/pl "CONFIG PROTECT (8% translated)")
-   [русский](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/ru "CONFIG_PROTECT (100% translated)")
-   [українська](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/uk "CONFIG PROTECT (17% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/zh-cn "CONFIG PROTECT (17% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/ja "CONFIG_PROTECT (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/CONFIG_PROTECT/ko "CONFIG PROTECT (8% translated)")

The `CONFIG_PROTECT` variable contains a space-delimited list of files and directories that Portage will protect from automatic modification. Proposed changes to protected configuration locations will require manual merges from the system administrator (see [[dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")] or similar merge tools).

A current list of presently protected locations can be displayed with [[portageq](https://wiki.gentoo.org/wiki/Portageq "Portageq")]:

`user `[`$`]`portageq envvar CONFIG_PROTECT`

    /etc /usr/share/config /usr/share/gnupg/qualified.txt

Using [portageq] is a short hand alternative to running a regular expression search on verbose, informational output from the [emerge] command:

`user `[`$`]`emerge --verbose --info | grep -E '^CONFIG_PROTECT='`

    CONFIG_PROTECT="/etc /usr/share/config /usr/share/gnupg/qualified.txt"

Files or subdirectories defined within the `CONFIG_PROTECT` can be *excluded* from protection through the [`CONFIG_PROTECT_MASK`](https://wiki.gentoo.org/wiki/CONFIG_PROTECT_MASK "CONFIG PROTECT MASK") variable. Masking is useful when a parent directory should be protected, but a certain child file or directory beneath it should not.

The variable has a sane default setting handled by the Portage installation and the user\'s Gentoo [profile](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles"). It can be extended through the system environment (which is often used by applications that update the variable through their [/etc/env.d] file) and the user\'s [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] setting.

[FILE] **`/etc/portage/make.conf`Example `CONFIG_PROTECT` definitions**

    CONFIG_PROTECT="/var/bind"

See also the [Environment variables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar "Handbook:AMD64/Working/EnvVar") chapter in the Gentoo Handbook.

## [[] See also]

-   [Configuration file management](https://wiki.gentoo.org/wiki/Configuration_file_management "Configuration file management")
-   [CONFIG_PROTECT_MASK](https://wiki.gentoo.org/wiki/CONFIG_PROTECT_MASK "CONFIG PROTECT MASK") --- contains a list of files or subdirectories which will be *excluded* from the overwrite protection offered by the [`CONFIG_PROTECT`] variable.
-   [savedconfig](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") --- a USE flag that preserves the saved configuration files upon package updates.
-   [/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- the main configuration file used to customize the [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") environment on a global level., the location [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") keeps binary packages.