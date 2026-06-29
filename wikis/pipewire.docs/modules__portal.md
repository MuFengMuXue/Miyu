# Portal

The `portal` module performs access control management for clients started
inside an XDG portal.

The module connects to the session DBus and subscribes to
`NameOwnerChanged` signals for the `org.freedesktop.portal.Desktop` name.
The PID of the DBus name owner is the portal.

A client connection from the portal PID to PipeWire gets assigned a  * PW_KEY_ACCESS of `"portal"` and set to permissions ALL - it is the
responsibility of the portal to limit the permissions before passing the
connection on to the client. See Access Control for details on
permissions.

Clients connecting from other PIDs are ignored by this module.

## Module Name

`libpipewire-module-portal`

## Module Options

There are no module-specific options.

## General options

There are no general options for this module.

## Example configuration
```
context.modules = [
 {   name = libpipewire-module-portal }
]
```
