## C.2 Install Locations

If an application is intended to be installed by root on a system wide basis then /usr/share is recommended to be used as value for *datadir* and /etc/xdg is recommended to be used as value for *sysconfdir*. In case the /usr/share hierarchy is not writable it is recommended to use /usr/local/share as value for *datadir* instead.

If an application is intended to be installed by an unprivileged user for exclusive use by that user only then `$XDG_DATA_HOME` should be used as value for *datadir* and `$XDG_CONFIG_HOME` should be used as value for *sysconfdir*. If `$XDG_DATA_HOME` is not set, the default value of \$HOME/.local/share should be used for it. If `$XDG_CONFIG_HOME` is not set, the default value of \$HOME/.config should be used for it.
