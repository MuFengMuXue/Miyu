# Metadata

Allows clients to export a metadata store to the PipeWire server.

Both the client and the server need to load this module for the metadata
to be exported.

This module creates a new factory and a new export type for the
PW_TYPE_INTERFACE_Metadata interface.

A client will first create an implementation of the PW_TYPE_INTERFACE_Metadata
interface with pw_context_create_metadata(), for example. With the
pw_core_export(), this module will create a server side resource to expose
the metadata implementation to other clients. Modifications done by the client
on the local metadata interface will be visible to all PipeWire clients.

It is also possible to use the factory to create metadata in the current
processes using a config file fragment.

As an argument to the create_object call, a set of properties will
control the name of the metadata and some initial values.

## Module Name

`libpipewire-module-metadata`

## Module Options

This module has no options.

## Properties for the create_object call

- `metadata.name`: The name of the new metadata object. If not given, the metadata
                   object name will be `default`.
- `metadata.values`: A JSON array of objects with initial values for the metadata object.

  the `metadata.values` key has the following layout:

 {.unparsed}
  metadata.values = [
     { id = <int>  key = <key>  type = <type> value = <object> }
     ....
  ]

    - `id`: an optional object id for the metadata, default 0
    - `key`: a string, the metadata key
    - `type`: an optional metadata value type
    - `value`: a JSON item, the metadata value.

## Example configuration

The module is usually added to the config file of the main PipeWire daemon and the
clients.

```
context.modules = [
{ name = libpipewire-module-metadata }
]
```

## Config objects

To create an object from the factory, one can use the pw_core_create_object()
method or make an object in the `context.objects` section like in the main PipeWire
daemon config file:

```
context.objects = [
{ factory = metadata
    args = {
        metadata.name = default
        metadata.values = [
           { key = default.audio.sink   value = { name = somesink } }
           { key = default.audio.source value = { name = somesource } }
        ]
    }
}
```

This creates a new default metadata store with 2 key/values.

## See also

- `pw-metadata`: a tool to manage metadata
