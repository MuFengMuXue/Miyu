# Man / User Dirs.defaults

XDG

Developer

Alexander

Larsson

alexl@redhat.com

user-dirs.defaults

5

File Formats

user-dirs.defaults

default settings for XDG user dirs

# Description

The `/etc/xdg/user-dirs.defaults` file is a text file that contains the default values for the XDG user dirs which are used by the xdg-user-dirs-update command.

This file contains lines of the form

    NAME=VALUE

The following names are recognised: DESKTOP, DOCUMENTS, DOWNLOAD, MUSIC, PICTURES, PROJECTS, PUBLICSHARE, TEMPLATES, VIDEOS

The values are relative pathnames from the home directory and will be translated on a per-path-element basis into the users locale.

Lines beginning with a \# character are ignored.

# Environment

`XDG_CONFIG_DIRS`
The `user-dirs.defaults` file is located in this directory. The default is `/etc/xdg`.

# See Also

`xdg-user-dirs-update(1)`
