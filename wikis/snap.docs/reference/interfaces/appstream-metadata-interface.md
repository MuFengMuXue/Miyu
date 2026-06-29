#  appstream-metadata interface

[AppStream ](https://www.freedesktop.org/software/appstream/docs/) is a metadata standard used to describe a common set software components. The `appstream-metadata` interface allows access to AppStream metadata from the host system.

## Developer details

**Auto-connect**: no

Requires snapd version _2.41+_.

### Code examples

[External package information](https://documentation.ubuntu.com/snapcraft/stable/reference/external-package-information/) describes how to access AppStream metadata.

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/appstream_metadata.go>
