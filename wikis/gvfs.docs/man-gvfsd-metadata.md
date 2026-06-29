# Man / Gvfsd Metadata

gvfs

Developer

Alexander

Larsson

alexl@redhat.com

gvfsd-metadata

1

User Commands

gvfsd-metadata

Metadata daemon for gvfs

gvfs-metadata

OPTION

# Description

`gvfsd-metadata` is a daemon acting as a write serialiser to the internal gvfs metadata storage. It is autostarted by GIO clients when they make metadata changes. Read operations are done by client-side GIO code directly, and don't require the daemon to be running.

The gvfs metadata capabilities are used by the nautilus file manager, for example.

# Options

`-h`, `--help`
Prints a short help text and exits.

`--version`
Shows the version number and exits.

`-r`, `--replace`
Replace the currently running instance.

# Exit status

On success 0 is returned, a non-zero failure code otherwise.

# Files

`$XDG_DATA_HOME/gvfs-metadata`
The directory where the gvfs metadata database files are stored

# See Also

`gvfs(7)`, `nautilus(1)`
