# Man / Gvfsd

gvfs

Developer

Alexander

Larsson

alexl@redhat.com

gvfsd

1

User Commands

gvfsd

Main daemon for gvfs

gvfsd

OPTION

# Description

`gvfsd` is the main daemon for the gvfs virtual filesystem. It provides the *org.gtk.vfs.Daemon* name on the session bus. gvfsd is autostarted by GIO clients if it is not running.

The primary task of `gvfsd` is to act as a mount tracker/manager. It spawns new backends when requested and keeps track of their lifecycle, maintaining a list of active mounts and creates direct connections to them.

Since gvfs backends are running as children of the gvfsd process, it is possible to start gvfsd in a terminal and set environment variables to get debug output from individual backends.

`gvfsd` also starts the `gvfsd-fuse(1)`, and provides it the mount point where the fuse file system should be mounted.

# Options

`-h`, `--help`
Prints a short help text and exits.

`--version`
Shows the version number and exits.

`-r`, `--replace`
Replace the currently running gvfsd instance.

`--no-fuse`
Don't start the fuse filesystem.

`-d`, `--debug`
Enable debug output.

# Environment

`GVFS_DISABLE_FUSE`
If this environment variable is set, gvfsd will not start the fuse filesystem.

# Exit status

On success 0 is returned, a non-zero failure code otherwise.

# See Also

`gvfs(7)`, `gvfsd-fuse(1)`
