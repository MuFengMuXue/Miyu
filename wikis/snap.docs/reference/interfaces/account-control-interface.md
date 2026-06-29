#  account-control interface

`account-control` allows managing non-system user accounts on [Ubuntu Core](https://ubuntu.com/core/docs) systems.

This interface enables the management of the `extrausers` table in the Name Service Switch (NSS) databases on Ubuntu Core to manage both non-system unprivileged and privileged users and groups.

The interface **does not** allow the management of users and groups for the system NSS databases in */etc*.

Due to the privileged nature of access enabled by this interface, its use is reserved exclusively for "management snaps" from [brand stores](https://ubuntu.com/core/docs/brand-stores).

## Developer details

**Auto-connect**: no

### Code examples

The account-control interface is used in the _usbtop_ snap to help monitor USB traffic: <https://github.com/ogra1/usbtop/blob/master/snap/snapcraft.yaml>

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/account_control.go>
