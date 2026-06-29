# xdg_system_bell_v1

## Interface `xdg_system_bell_v1` version 1

system bell

This global interface enables clients to ring the system bell. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: destroy the system bell object
  Notify that the object will no longer be used.
- `ring`: ring the system bell
  This requests rings the system bell on behalf of a client. How ringing the bell is implemented is up to the compositor. It may be an audible sound, a visual feedback of some kind, or any other thing including nothing. The passed surface should correspond to a toplevel like surface role, or be null, meaning the client doesn't have a particular toplevel it wants to associate the bell ringing with. See the xdg-shell protocol extension for a toplevel like surface role.
  Arguments: `surface` (object) - associated surface
