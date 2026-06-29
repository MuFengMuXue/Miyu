# Client Node

Allow clients to export processing nodes to the PipeWire daemon.

This module creates 2 export types, one for the PW_TYPE_INTERFACE_Node and
another for the SPA_TYPE_INTERFACE_Node interfaces.

With pw_core_export(), objects of these types can be exported to the
PipeWire server. All actions performed on the node locally will be visible
to connecteced clients and scheduling of the Node will be performed.

Objects of the PW_TYPE_INTERFACE_Node interface can be made with
pw_context_create_node(), for example. You would manually need to create
and add an object of the SPA_TYPE_INTERFACE_Node interface. Exporting a
SPA_TYPE_INTERFACE_Node directly will first wrap it in a
PW_TYPE_INTERFACE_Node interface.

Usually this module is not used directly but through the pw_stream and
pw_filter APIs, which provides API to implement the SPA_TYPE_INTERFACE_Node
interface.

In some cases, it is possible to use this factory directly (the PipeWire JACK
implementation does this). With pw_core_create_object() on the `client-node`
factory will result in a PW_TYPE_INTERFACE_ClientNode proxy that can be
used to control the server side created pw_impl_node.

Schematically, the client side pw_impl_node is wrapped in the ClientNode
proxy and unwrapped by the server side resource so that all actions on the client
side node are reflected on the server side node and server side actions are
reflected in the client.

```

  client side proxy                            server side resource
.------------------------------.            .----------------------------------.
| PW_TYPE_INTERFACE_ClientNode |            |  PW_TYPE_INTERFACE_Node          |
|.----------------------------.|  IPC       |.--------------------------------.|
|| PW_TYPE_INTERFACE_Node     || ----->     || SPA_TYPE_INTERFACE_Node        ||
||.--------------------------.||            ||.------------------------------.||
||| SPA_TYPE_INTERFACE_Node  |||            ||| PW_TYPE_INTERFACE_ClientNode |||
|||                          |||            |||                              |||
||'--------------------------'||            ||'------------------------------'||
|'----------------------------'|            |'--------------------------------'|
'------------------------------'            '----------------------------------'
```

## Module Name

`libpipewire-module-client-node`

## Module Options

This module has no options.

## Properties for the create_object call

All properties are passed directly to the pw_context_create_node() call.

## Example configuration

The module is usually added to the config file of the main PipeWire daemon and the
clients.

```
context.modules = [
{ name = libpipewire-module-client-node }
]
```

## See also

- `module-spa-node-factory`: make nodes from a factory
