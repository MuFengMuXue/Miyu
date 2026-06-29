# VBAN receiver

The `vban-recv` module creates a PipeWire source that receives audio
and midi [VBAN](https://vb-audio.com) packets.

The receive will listen on a specific port (6980) and create a stream for each
VBAN stream received on the port.

## Module Name

`libpipewire-module-vban-recv`

## Module Options

Options specific to the behavior of this module

- `local.ifname = <str>`: interface name to use
- `source.ip = <str>`: the source ip address to listen on, default 127.0.0.1
- `source.port = <int>`: the source port to listen on, default 6980
- `node.always-process = <bool>`: true to receive even when not running
- `sess.latency.msec = <str>`: target network latency in milliseconds, default 100
- `stream.props = {}`: properties to be passed to all the stream
- `stream.rules` = <rules>: match rules, use create-stream actions.

### stream.rules matches

 - `vban.ip`: the IP address of the VBAN sender
 - `vban.port`: the port of the VBAN sender
 - `sess.name`: the name of the VBAN stream

### stream.rules create-stream

In addition to all the properties that can be passed to a stream,
you can also set:

- `sess.latency.msec = <str>`: target network latency in milliseconds, default 100

## General options

Options with well-known behavior:

- PW_KEY_REMOTE_NAME
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_MEDIA_NAME
- PW_KEY_MEDIA_CLASS
- PW_KEY_NODE_NAME
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_NODE_GROUP
- PW_KEY_NODE_LATENCY
- PW_KEY_NODE_VIRTUAL

## Example configuration
```
# ~/.config/pipewire/pipewire.conf.d/my-vban-recv.conf

context.modules = [
{   name = libpipewire-module-vban-recv
    args = {
        #local.ifname = eth0
        #source.ip = 127.0.0.1
        #source.port = 6980
        sess.latency.msec = 100
        #node.always-process = false
        #audio.position = [ FL FR ]
        stream.props = {
           #media.class = "Audio/Source"
           #node.name = "vban-receiver"
        }
        stream.rules = [
            {   matches = [
                    {    sess.name = "~.*"
                         #sess.media = "audio" | "midi"
                         #vban.ip = ""
                         #vban.port = 1000
                         #audio.channels = 2
                         #audio.format = "U8" | "S16LE" | "S24LE" | "S32LE" | "F32LE" | "F64LE"
                         #audio.rate = 44100
                    }
                ]
                actions = {
                    create-stream = {
                        stream.props = {
                            #sess.latency.msec = 100
                            #target.object = ""
                            #audio.position = [ FL FR ]
                            #media.class = "Audio/Source"
                            #node.name = "vban-receiver"
                        }
                    }
                }
            }
        ]
    }
}
]
```

 0.3.76
