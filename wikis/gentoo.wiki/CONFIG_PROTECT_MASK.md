The `CONFIG_PROTECT_MASK` variable contains a list of files or subdirectories which will be *excluded* from the overwrite protection offered by the [`CONFIG_PROTECT`](https://wiki.gentoo.org/wiki/CONFIG_PROTECT "CONFIG PROTECT") variable. This is to say that files or subdirectories mentioned in this variable will be *overwritten* by Portage upon (re)installation.

\"Masking\" is useful when locations within a certain *parent* directory are protected from automatic overwrites - *excluded* from the package manager\'s control, but a certain *child* location should be *included* in the package manager\'s control.

## [See also]

-   [CONFIG_PROTECT](https://wiki.gentoo.org/wiki/CONFIG_PROTECT "CONFIG PROTECT") --- contains a space-delimited list of files and directories that Portage will protect from automatic modification.
-   [savedconfig](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") --- a USE flag that preserves the saved configuration files upon package updates.
-   [/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- the main configuration file used to customize the [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") environment on a global level., the location [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") keeps binary packages.