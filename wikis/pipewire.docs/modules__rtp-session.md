# RTP session

The `rtp-session` module creates a media session that is announced
with avahi/mDNS/Bonjour.

Other machines on the network that run a compatible session will see
each other and will be able to send audio/midi between each other.

The session setup is based on apple-midi and is compatible with
apple-midi when the session is using midi.

## Module Name

`libpipewire-module-rtp-session`

## Module Options

Options specific to the behavior of this module

- `local.ifname = <str>`: interface name to use
- `control.ip =<str>`: control IP address, default "0.0.0.0"
- `control.port =<int>`: control port, default "0"
- `net.mtu = <int>`: MTU to use, default 1280
- `net.ttl = <int>`: TTL to use, default 1
- `net.loop = <bool>`: loopback multicast, default false
  `sess.discover-local`: discover local services as well, default false
- `sess.min-ptime = <int>`: minimum packet time in milliseconds, default 2
- `sess.max-ptime = <int>`: maximum packet time in milliseconds, default 20
- `sess.latency.msec = <int>`: receiver latency in milliseconds, default 100
- `sess.name = <str>`: a session name
- `sess.ts-offset = <int>`: an offset to apply to the timestamp, default -1 = random offset
- `sess.ts-refclk = <string>`: the name of a reference clock
- `sess.media = <string>`: the media type audio|midi|opus, default midi
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
# ~/.config/pipewire/pipewire.conf.d/my-rtp-session.conf

context.modules = [
{   name = libpipewire-module-rtp-session
    args = {
        #local.ifname = "eth0"
        #control.ip = "0.0.0.0"
        #control.port = 0
        #net.mtu = 1280
        #net.ttl = 1
        #net.loop = false
        #sess.discover-local = false
        #sess.min-ptime = 2
        #sess.max-ptime = 20
        #sess.name = "PipeWire RTP stream"
        #sess.media = "audio"
        stream.props = {
            node.name = "rtp-sink"
            #audio.format = "S16BE"
            #audio.rate = 48000
            #audio.channels = 2
            #audio.position = [ FL FR ]
        }
    }
}
]
```

 0.3.60
