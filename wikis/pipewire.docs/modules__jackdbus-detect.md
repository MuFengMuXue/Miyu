# JACK DBus detect

Automatically creates a sink/source when a jackdbus server is started
and connect to JACK.

## Module Name

`libpipewire-module-jackdbus-detect`

## Module Options

There are no module-specific options, all arguments are passed to
JACK Tunnel.

## Config override

A `module.jackdbus-detect.args` config section can be added
to override the module arguments.

```
# ~/.config/pipewire/pipewire.conf.d/my-jack-dbus-detect-args.conf

module.jackdbus-detect.args = {
    #tunnel.mode    = duplex
}
```

## Example configuration
```
# ~/.config/pipewire/pipewire.conf.d/my-jack-dbus-detect.conf

context.modules = [
 {   name = libpipewire-module-jackdbus-detect
     args {
        #jack.server    = null
        #tunnel.mode    = duplex
        #audio.channels = 2
        #audio.position = [ FL FR ]
        source.props = {
            # extra sink properties
        }
        sink.props = {
            # extra sink properties
        }
     }
 }
]
```
