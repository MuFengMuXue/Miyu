# Man / Gvfsd Fuse

gvfs

Developer

Alexander

Larsson

alexl@redhat.com

gvfsd-fuse

1

User Commands

gvfsd-fuse

Fuse daemon for gvfs

gvfsd-fuse

PATH

# Description

`gvfsd-fuse` maintains a fuse mount to make gvfs backends available to POSIX applications. The mount point for the fuse filesystem is provided by the PATH argument.

`gvfsd-fuse` is normally started by `gvfsd(1)`. In this case, the mount point is `$XDG_RUNTIME_DIR/gvfs` or `$HOME/.gvfs`.

# Options

`-d`
Enable fuse debug output. This implies `-f`.

`-f`
Run in the foreground.

`-s`
Run single-threaded.

`-o OPTION`
Set a fuse-specific option. See the fuse documentation for a list of these.

# Exit status

On success 0 is returned, a non-zero failure code otherwise.

# See Also

`gvfs(7)`
