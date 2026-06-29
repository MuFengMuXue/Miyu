#  snap-themes-control interface

The `snap-themes-control` interface permits the use of snapd's theme installation API.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Endpoint access permissions
<ul>
<li>/v2/accessories/changes/{id}</li>
<li>/v2/accessories/themes</li>
</ul>

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/snap_themes_control_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/snap_themes_control.go
