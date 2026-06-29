# X11 Bell

The `x11-bell` module intercept the X11 bell events and uses libcanberra to
play a sound.

## Module Name

`libpipewire-module-x11-bell`

## Module Options

- `sink.name = <str>`: node.name of the sink to connect to
- `sample.name = <str>`: the name of the sample to play, default 'bell-window-system'
- `x11.display = <str>`: the X11 display to use
- `x11.xauthority = <str>`: the X11 XAuthority string placed in XAUTHORITY env

## General options

There are no general options for this module.

## Example configuration
```
context.modules = [
 {   name = libpipewire-module-x11-bell }
     args = {
         #sink.name = @DEFAULT_SINK@
         sample.name = "bell-window-system"
         #x11.display = ":1"
         #x11.xauthority = "test"
]
```
