# Client Device

Allow clients to export devices to the PipeWire daemon.

This module creates an export type for the SPA_TYPE_INTERFACE_Device
interface.

With pw_core_export(), objects of this type can be exported to the
PipeWire server. All actions performed on the device locally will be visible
to connecteced clients.

In some cases, it is possible to use this factory directly.
With pw_core_create_object() on the `client-device`
factory will result in a SPA_TYPE_INTERFACE_Device proxy that can be
used to control the server side created pw_impl_device.

Schematically, the client side spa_device is wrapped in the ClientDevice
proxy and unwrapped by the server side resource so that all actions on the client
side device are reflected on the server side device and server side actions are
reflected in the client.

```

  client side proxy                            server side resource
.------------------------------.            .----------------------------------.
| SPA_TYPE_INTERFACE_Device    |            |  PW_TYPE_INTERFACE_Device        |
|                              |  IPC       |.--------------------------------.|
|                              | ----->     || SPA_TYPE_INTERFACE_Device      ||
|                              |            |'--------------------------------'|
'------------------------------'            '----------------------------------'
```

## Module Name

`libpipewire-module-client-device`

## Module Options

This module has no options.

## Properties for the create_object call

All properties are passed directly to the pw_context_create_device() call.

## Example configuration

The module is usually added to the config file of the main PipeWire daemon and the
clients.

```
context.modules = [
{ name = libpipewire-module-client-device }
]
```

## See also

- `module-spa-device-factory`: make nodes from a factory
