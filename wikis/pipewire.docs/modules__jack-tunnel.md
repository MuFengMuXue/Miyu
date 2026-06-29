# JACK Tunnel

The jack-tunnel module provides a source or sink that tunnels all audio to
a JACK server.

This module is usually used together with JACK DBus detect that will
automatically load the tunnel with the right parameters based on dbus
information.

## Module Name

`libpipewire-module-jack-tunnel`

## Module Options

- `jack.library`: the libjack to load, by default libjack.so.0 is searched in
			LIBJACK_PATH directories and then some standard library paths.
- `jack.server`: the name of the JACK server to tunnel to.
- `jack.client-name`: the name of the JACK client.
- `jack.connect`: if jack ports should be connected automatically. Can also be
                  placed per stream.
- `jack.connect-audio`: An array of audio ports to connect to. Can also be placed per
                  stream. An empty array will not connect anything, even when
                  jack.connect is true.
- `jack.connect-midi`: An array of midi ports to connect to. Can also be placed per
                  stream. An empty array will not connect anything, even when
                  jack.connect is true.
- `tunnel.mode`: the tunnel mode, sink|source|duplex, default duplex
- `midi.ports`: the number of midi ports. Can also be added to the stream props.
- `source.props`: Extra properties for the source filter.
- `sink.props`: Extra properties for the sink filter.

## General options

Options with well-known behavior.

- PW_KEY_REMOTE_NAME
- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_NODE_NAME
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_NODE_GROUP
- PW_KEY_NODE_VIRTUAL
- PW_KEY_MEDIA_CLASS
- PW_KEY_TARGET_OBJECT to specify the remote node.name or serial.id to link to

## Example configuration of a duplex sink/source

```
# ~/.config/pipewire/pipewire.conf.d/my-jack-tunnel.conf

context.modules = [
{   name = libpipewire-module-jack-tunnel
    args = {
        #jack.library     = libjack.so.0
        #jack.server      = null
        #jack.client-name = PipeWire
        #jack.connect     = true
        #jack.connect-audio = [ playback_1 playback_2 ]
        #jack.connect-midi = [ midi_playback_1 ]
        #tunnel.mode      = duplex
        #midi.ports       = 0
        #audio.channels   = 2
        #audio.position   = [ FL FR ]
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
