# Protocol Native

The native protocol module implements the PipeWire communication between
a client and a server using unix local sockets.

Normally this module is loaded in both client and server config files
so that they can communicate.

## Module Name

`libpipewire-module-protocol-native`

## Module Options

The module supports the following arguments:

- `sockets`: `[ { name = "socket-name", owner = "owner", group = "group", mode = "mode", selinux.context = "context" }, props = { ... }, ... ]`

  Array of Unix socket names and (optionally) owner/permissions to serve,
  if the context is a server. If not absolute paths, the sockets are created
  in the default runtime directory.

  The props are copied directly to any client that connects through this server
  socket and can be used to configure special permissions.

  Has the default value `[ { name = "CORENAME" }, { name = "CORENAME-manager" } ]`,
  where `CORENAME` is the name of the PipeWire core, usually `pipewire-0`.

  The permissions have no effect for sockets from Systemd socket activation.
  Those should be configured via the systemd.socket(5) mechanism.

## General Options

The name of the core is obtained as:

- PIPEWIRE_CORE : the environment variable with the name of the core
- PW_KEY_CORE_NAME : in the context properties
- a name based on the process id

The context will also become a server if:

- PIPEWIRE_DAEMON : the environment is true
- PW_KEY_CORE_DAEMON : in the context properties is true

The socket will be located in the directory obtained by looking at the
following environment variables:

- PIPEWIRE_RUNTIME_DIR
- XDG_RUNTIME_DIR
- USERPROFILE

The socket address will be written into the notification file descriptor
if the following environment variable is set:

- PIPEWIRE_NOTIFICATION_FD

When a client connect, the connection will be made to:

- PIPEWIRE_REMOTE : the environment with the remote name
- PW_KEY_REMOTE_NAME : the property in the context.
- The default remote named "pipewire-0"

A Special remote named "internal" can be used to make a connection to the
local context. This can be done even when the server is not a daemon. It can
be used to treat a local context as if it was a server.

## Config override

A `module.protocol-native.args` config section can be added
to override the module arguments.

```
# ~/.config/pipewire/pipewire.conf.d/my-protocol-native-args.conf

module.protocol-native.args = {
       sockets = [
           { name = "pipewire-0" }
           { name = "pipewire-0-manager" }
       ]
}
```

## Example configuration

```
context.modules = [
   { name = libpipewire-module-protocol-native }
]
```

```
context.modules = [
 { name = libpipewire-module-protocol-native,
   args = {
       sockets = [
           { name = "pipewire-0" }
           { name = "pipewire-0-manager" }
           { name = "pipewire-1"
             props = { my.connection = "the other one" }
           }
       ]
   }
 }
]
```
