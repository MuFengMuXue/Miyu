#  accounts-service interface

`accounts-service` allows communication with the *accounts* service, such as [GNOME Online Accounts](https://wiki.gnome.org/Projects/GnomeOnlineAccounts).

## Example

This interface automatically connected by the [ONLY OFFICE Document Server](https://snapcraft.io/onlyoffice-ds) snap to provide better integration with pre-configured accounts.

## Developer details

**Auto-connect**: no

### Code examples

The snapcraft.yaml for ONLY OFFICE Document Server can be found in the project’s GitHub repository: [https://github.com/ONLYOFFICE/snap-documentserver/blob/master/snap/snapcraft.yaml](https://github.com/ONLYOFFICE/snap-documentserver/blob/d6ab8c34d3601d177b08c2ebaa68eb8fc98b8898/snap/snapcraft.yaml#L52)

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/accounts_service.go>
