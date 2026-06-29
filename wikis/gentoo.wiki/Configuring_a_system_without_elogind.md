[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Configuring_a_system_without_elogind&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Various programs require a certain environment in order to provide their functionality, including setting particular environment variables. In particular, some software requires \'seat management\' in order to mediate access to hardware shared by multiple system users (e.g. the display, input devices) without needing root access.

On systemd-based systems, logind ([[[systemd-logind.service(8)]](https://man.archlinux.org/man/systemd-logind.service.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]) is one of the programs used to set up the environment. On OpenRC-based systems, where [logind] isn\'t available, [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") ([[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]], [elogind(8)](https://manpages.debian.org/testing/elogind/elogind.8.en.html)) can be used instead. However, some users might not wish to use elogind; this page describes the options available.

### [seatd]

In some instances, [seatd](https://wiki.gentoo.org/wiki/Seatd "Seatd"), provided by the [[[sys-auth/seatd]](https://packages.gentoo.org/packages/sys-auth/seatd)[]] package, might be a suitable replacement for the seat-management functionality provided by elogind. Refer to the linked wiki page and the [[[seatd(1)]](https://man.archlinux.org/man/seatd.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for further information.

### [Environment variables]

An important environment variable configured by elogind is `XDG_RUNTIME_DIR`, described on the [XDG/Base_Directories](https://wiki.gentoo.org/wiki/XDG/Base_Directories "XDG/Base Directories") page:

> The base directory relative to which user-specific non-essential runtime files and other file objects (such as sockets, named pipes, \...) should be stored. The directory MUST be owned by the user, who MUST be the only one having read and write access to it; its permissions MUST be 0700.

If not set by elogind, this variable needs to be manually set via the appropriate shell configuration file, e.g. [\~/.bash_login]:

[FILE] **`~/.bash_login`**

    if test -z "$"; then
        export XDG_RUNTIME_DIR=$(mktemp -d "$-runtime-dir.XXX")
    fi

However, some applications assume `XDG_RUNTIME_DIR` is set to [/run/user/\$], e.g. gpg assumes this when deciding where to place various sockets. Additionally, the directory should ideally be placed in a directory on a tmpfs mount (like [/run]). So it may be wiser to use [/run/user/\$] like so:

[FILE] **`~/.bash_login`**

    if test -z "$"; then
        export XDG_RUNTIME_DIR=/run/user/$
    fi

    if test -d "$"; then
        perms="$(stat -c '%a %u' "$")"
        if [[ "$" != "700 $" ]]; then
            export -n XDG_RUNTIME_DIR
            echo "WARNING! XDG_RUNTIME_DIR has incorrect permissions"
        fi
    else
        mkdir -p "$"
        chmod 0700 "$"
    fi

However, since [/run/user] might not exist and [/run] is owned by root, the above will fail due to permissions. One possibility is to create [/etc/local.d/create-runuser.start] with contents along the lines of:

[FILE] **`/etc/local.d/create-runuser.start`**

    #!/bin/sh
    mkdir -p /run/user
    chmod 1777 /run/user

** Note**\
Although the sticky bit is set on [/run/user] to stop others from deleting or rename the `XDG_RUNTIME_DIR` created by the user, it will not stop other users creating this user\'s `XDG_RUNTIME_DIR`.

Other environment variables that might also need to be manually set include `XDG_CACHE_HOME`, `XDG_CONFIG_HOME`, `XDG_DATA_HOME`, and `XDG_STATE_HOME`:

[FILE] **`~/.bash_login`**

    export XDG_CACHE_HOME="$/.cache"
    export XDG_CONFIG_HOME="$/.config"
    export XDG_DATA_HOME="$/.local/share"
    export XDG_STATE_HOME="$/.local/state"