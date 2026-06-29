[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=XDG/Base_Directories&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Official documentation](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Xdg "wikipedia:Xdg")

The [XDG Base Directories] are standard directories specified by [freedesktop.org](https://freedesktop.org) (formerly the [X Desktop Group](https://wiki.gentoo.org/wiki/XDG "XDG")).

## [Directories]

The [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html) defines:

-   `XDG_DATA_HOME`: the base directory relative to which user-specific data files should be stored. If not set, or empty, assumed to be [\$HOME/.local/share/].

<!-- -->

-   `XDG_DATA_DIRS`: the preference-ordered set of base directories, separated by colons (\':\'), to search for data files in addition to the `XDG_DATA_HOME` base directory. If not set or empty, assumed to be [/usr/local/share/:/usr/share/].

<!-- -->

-   `XDG_CONFIG_HOME`: the base directory relative to which user-specific configuration files should be stored. If not set, or empty, assumed to be [\$HOME/.config/].

<!-- -->

-   `XDG_CONFIG_DIRS`: the preference-ordered set of base directories, separated by colons (\':\'), to search for configuration files in addition to the `XDG_CONFIG_HOME` base directory. If not set or empty, assumed to be [/etc/xdg/].

<!-- -->

-   `XDG_STATE_HOME`: the base directory relative to which user-specific state files should be stored, containing data that should persist between (application) restarts, but that is not important or portable enough to the user that it should be stored in `XDG_DATA_HOME`. If not set, or empty, assumed to be [\$HOME/.local/state/].

<!-- -->

-   `XDG_CACHE_HOME`: the base directory relative to which user-specific non-essential data files should be stored. If not set or empty, assumed to be [\$HOME/.cache/].

<!-- -->

-   `XDG_RUNTIME_DIR`: the base directory relative to which user-specific non-essential runtime files and other file objects (such as sockets, named pipes, \...) should be stored. The directory MUST be owned by the user, who MUST be the only one having read and write access to it; its permissions MUST be 0700.

<!-- -->

-   [\$HOME/.local/bin/]: the directory for user-specific executable files.

Normally, the `XDG_*` variables will be set appropriately by [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") or [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") upon login. On systems not using either, it might be necessary to configure them manually; refer to the [Configuring a system without elogind](https://wiki.gentoo.org/wiki/Configuring_a_system_without_elogind "Configuring a system without elogind") page for further information.