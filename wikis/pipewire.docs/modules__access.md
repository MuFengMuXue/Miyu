# Access

The `access` module performs access checks on clients. The access check
is only performed once per client, subsequent checks return the same
resolution.

Permissions assigned to a client are configured as arguments to this
module, see below. Permission management beyond unrestricted access
is delegated to an external agent, usually the session manager.

This module sets the PW_KEY_ACCESS as follows:

- If `access.legacy` module option is not enabled:

  The value defined for the socket in `access.socket` module option, or
  `"default"` if no value is defined.

- If `access.legacy` is enabled, the value is:

    - `"flatpak"`: if client is a Flatpak client
    - `"unrestricted"`: if PW_KEY_CLIENT_ACCESS client property is set to `"allowed"`
    - Value of PW_KEY_CLIENT_ACCESS client property, if set
    - `"unrestricted"`: otherwise

If the resulting PW_KEY_ACCESS value is `"unrestricted"`, this module
will give the client all permissions to access all resources.  Otherwise, the
client will be forced to wait until an external actor, such as the session
manager, updates the client permissions.

For connections from applications running inside Flatpak, and not mediated by
other clients (eg. portal or pipewire-pulse), the
`pipewire.access.portal.app_id` property is to the Flatpak application ID, if
found. In addition, `pipewire.sec.flatpak` is set to `true`.

## Module Name

`libpipewire-module-access`

## Module Options

Options specific to the behavior of this module

- `access.socket = { "socket-name" = "access-value", ... }`:

  Socket-specific access permissions. Has the default value
  `{ "CORENAME-manager": "unrestricted" }`
  where `CORENAME` is the name of the PipeWire core, usually `pipewire-0`.

- `access.legacy = true`: enable backward-compatible access mode.  Cannot be
  enabled when using socket-based permissions.

  If `access.socket` is not specified, has the default value `true`
  otherwise `false`.

  **Warning:** The legacy mode is deprecated. The default value is subject to
           change and the legacy mode may be removed in future PipeWire
           releases.

## General options

Options with well-known behavior:

- PW_KEY_ACCESS
- PW_KEY_CLIENT_ACCESS

## Config override

A `module.access.args` config section can be added
to override the module arguments.

```
# ~/.config/pipewire/pipewire.conf.d/my-access-args.conf

module.access.args = {
     access.socket = {
         pipewire-0 = "default",
         pipewire-0-manager = "unrestricted",
     }
}
```

## Example configuration

```
context.modules = [
 {   name = libpipewire-module-access
     args = {
         # Use separate socket for session manager applications,
         # and pipewire-0 for usual applications.
         access.socket = {
             pipewire-0 = "default",
             pipewire-0-manager = "unrestricted",
         }
     }
 }
]
```

**See:** pw_resource_error
**See:** pw_impl_client_update_permissions
