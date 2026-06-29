#  desktop-launch interface

The `desktop-launch` interface allows [strictly confined](https://snapcraft.io/docs/explanation/security/snap-confinement/) snaps to identify and launch desktop applications in (or from) other snaps.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Endpoint access permissions
<ul>
<li>/v2/snaps/{name}</li>
<li>/v2/snaps</li>
<li>/v2/icons/{name}/icon</li>
</ul>

Requires snapd version _2.52+_.

### Code examples

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/desktop_launch.go>
