# Man / Xdg User Dir

XDG

Developer

Alexander

Larsson

alexl@redhat.com

xdg-user-dir

1

User Commands

xdg-user-dir

Find an XDG user dir

xdg-user-dir

NAME

# Description

`xdg-user-dir` looks up the current path for one of the special XDG user dirs.

This command expects the name of an XDG user dir as argument. The possible names are: DESKTOP, DOCUMENTS, DOWNLOAD, MUSIC, PICTURES, PROJECTS, PUBLICSHARE, TEMPLATES, VIDEOS

# Files

The values are looked up in the `user-dirs.dirs` file. This file is created by the xdg-user-dirs-update utility.

# Environment

The `XDG_CONFIG_HOME` environment variable determines where the `user-dirs.dirs` file is located.

# See Also

`xdg-user-dirs-update(1)`
