#  snap-refresh-observe interface

The `snap-refresh-observe` interface permits tracking snap refreshes and their inhibition.

It is intended to be used _only_ to mark the existence of a refresh awareness client, such as [snapd-desktop-integration](https://snapcraft.io/install/snapd-desktop-integration/ubuntu) snap.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

### Endpoint access permissions
<ul>
<li>/v2/changes</li>
<li>/v2/changes/{id}</li>
<li>/v2/icons/{name}/icon</li>
<li>/v2/notices</li>
<li>/v2/notices/{id}</li>
<li>/v2/snaps</li>
<li>/v2/snaps/{name}</li>
</ul>

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/snap_refresh_observe_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/snap_refresh_observe.go
