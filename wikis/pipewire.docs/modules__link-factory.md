# Link Factory

Allows clients to create links between ports.

This module creates a new factory. Clients that can see the factory
can use the factory name (`link-factory`) to create new link
objects with pw_core_create_object(). It is also possible to create
objects in the config file.

Object of the PW_TYPE_INTERFACE_Link will be created and a proxy
to it will be returned.

As an argument to the create_object call, a set of properties will
control what ports will be linked.

## Module Name

`libpipewire-module-link-factory`

## Module Options

- `allow.link.passive`: if the `link.passive` property is allowed. Default false.
                       By default, the core will decide when a link is passive
                       based on the properties of the node and ports.

## Properties for the create_object call

- `link.output.node`: The output node to use. This can be the node object.id, node.name,
                    node.nick, node.description or object.path of a node. When the
                    property is not given or NULL, the output port should be
                    specified.
- `link.output.port`: The output port to link. This can be a port object.id, port.name,
                    port.alias or object.path. If an output node is specified, the
                    port must belong to the node. Finding a port in a node using the
                    port.id is deprecated and may lead to unexpected results when the
                    port.id also matches an object.id. If no output port is given, an
                    output node must be specified and a random (unlinked) port will
                    be used from the node.
- `link.input.node`: The input node to use. This can be the node object.id, node.name,
                    node.nick, node.description or object.path of a node. When the
                    property is not given or NULL, the input port should be
                    specified.
- `link.input.port`: The input port to link. This can be a port object.id, port.name,
                    port.alias or object.path. If an input node is specified, the
                    port must belong to the node. Finding a port in a node using the
                    port.id is deprecated and may lead to unexpected results when the
                    port.id also matches an object.id. If no input port is given, an
                    input node must be specified and a random (unlinked) port will
                    be used from the node.
- `object.linger`: Keep the link around even when the client that created it is gone.
- `link.passive`: The link is passive, meaning that it will not keep nodes busy.
                By default this property is ignored and the node and port properties
                are used to determine the passive state of the link.

## Example configuration

The module is usually added to the config file of the main pipewire daemon.

```
context.modules = [
{ name = libpipewire-link-factory
  args = {
      #allow.link.passive = false
  }
}
]
```

## Config override

A `module.link-factory.args` config section can be added
to override the module arguments.

```
# ~/.config/pipewire/pipewire.conf.d/my-link-factory-args.conf

module.link-factory.args = {
    #allow.link.passive = false
}
```

## Config objects

To create an object from the factory, one can use the pw_core_create_object()
method or make an object in the `context.objects` section like:

```
context.objects = [
{ factory = link-factory
    args = {
        link.output.node = system
        link.output.port = capture_2
        link.input.node  = my-mic
        link.input.port  = input_FR
    }
}
```

Note that this only works when the ports that need to be linked are available
at the time the config file is parsed.

## See also

- `pw-link`: a tool to manage port links
