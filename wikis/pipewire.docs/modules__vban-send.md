# VBAN sender

The `vban-send` module creates a PipeWire sink that sends
audio and midi [VBAN](https://vb-audio.com) packets.

## Module Name

`libpipewire-module-vban-send`

## Module Options

Options specific to the behavior of this module

- `source.ip =<str>`: source IP address, default "0.0.0.0"
- `destination.ip =<str>`: destination IP address, default "127.0.0.1"
- `destination.port =<int>`: destination port, default 6980
- `local.ifname = <str>`: interface name to use
- `net.mtu = <int>`: MTU to use, default 1500
- `net.ttl = <int>`: TTL to use, default 1
- `net.loop = <bool>`: loopback multicast, default false
- `sess.min-ptime = <int>`: minimum packet time in milliseconds, default 2
- `sess.max-ptime = <int>`: maximum packet time in milliseconds, default 20
- `sess.name = <str>`: a session name
- `sess.media = <string>`: the media type audio|midi, default audio
- `stream.props = {}`: properties to be passed to the stream

## General options

Options with well-known behavior:

- PW_KEY_REMOTE_NAME
- PW_KEY_AUDIO_FORMAT
- PW_KEY_AUDIO_RATE
- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_NODE_NAME
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_MEDIA_NAME
- PW_KEY_NODE_GROUP
- PW_KEY_NODE_LATENCY
- PW_KEY_NODE_VIRTUAL
- PW_KEY_MEDIA_CLASS

## Example configuration
```
# ~/.config/pipewire/pipewire.conf.d/my-vban-send.conf

context.modules = [
{   name = libpipewire-module-vban-send
    args = {
        #local.ifname = "eth0"
        #source.ip = "0.0.0.0"
        #destination.ip = "127.0.0.1"
        #destination.port = 6980
        #net.mtu = 1500
        #net.ttl = 1
        #net.loop = false
        #sess.min-ptime = 2
        #sess.max-ptime = 20
        #sess.name = "PipeWire VBAN stream"
        #sess.media = "audio"
        #audio.format = "S16LE"
        #audio.rate = 44100
        #audio.channels = 2
        #audio.position = [ FL FR ]
        stream.props = {
            node.name = "vban-sender"
        }
    }
}
]
```

 0.3.76
