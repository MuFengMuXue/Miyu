#  packagekit-control interface

`packagekit-control` allows control of the [PackageKit](https://www.freedesktop.org/software/PackageKit/) service, giving privileged access to native package management on the system.

This interface is intended to work in tandem with [the AppStream interface](https://snapcraft.io/docs/reference/interfaces/appstream-metadata-interface/). Snaps distributed via the public [Snap store](https://snapcraft.io/store) are not typically granted auto-connection for this interface.

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

Requires snapd version _2.41+_.`
