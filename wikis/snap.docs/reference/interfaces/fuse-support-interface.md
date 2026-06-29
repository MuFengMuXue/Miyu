#  fuse-support interface

`fuse-support` allows access to FUSE filesystems.

**Auto-connect**: no
**NOTE**:
* Unprivileged fuse mounts(i.e. mounting directory outside of the snap-specific writable directories) [are NOT supported by this interface](https://github.com/canonical/snapd/pull/1598#issuecomment-239952977)
* Mount point can only exist in snap-specific writable directories:
    * `SNAP_USER_{DATA,COMMON}`
    * `SNAP_{DATA,COMMON}`

## Corresponding Source

<https://github.com/canonical/snapd/blob/master/interfaces/builtin/fuse_support.go>
