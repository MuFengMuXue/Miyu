# RTP sink

The `rtp-sink` module creates a PipeWire sink that sends audio
RTP packets.

## Module Name

`libpipewire-module-rtp-sink`

## Module Options

Options specific to the behavior of this module

- `source.ip =<str>`: source IP address, default "0.0.0.0"
- `destination.ip =<str>`: destination IP address, default "224.0.0.56"
- `destination.port =<int>`: destination port, default random between 46000 and 47024
- `local.ifname = <str>`: interface name to use
- `net.mtu = <int>`: MTU to use, default 1280
- `net.ttl = <int>`: TTL to use, default 1
- `net.loop = <bool>`: loopback multicast, default false
- `sess.min-ptime = <float>`: minimum packet time in milliseconds, default 2
- `sess.max-ptime = <float>`: maximum packet time in milliseconds, default 20
- `sess.name = <str>`: a session name
- `rtp.ptime = <float>`: size of the packets in milliseconds, default up to MTU but
      between sess.min-ptime and sess.max-ptime
- `rtp.framecount = <int>`: number of samples per packet, default up to MTU but
      between sess.min-ptime and sess.max-ptime
- `sess.latency.msec = <float>`: target node latency in milliseconds, default as rtp.ptime
- `sess.ts-offset = <int>`: an offset to apply to the timestamp, default -1 = random offset
- `sess.ts-refclk = <string>`: the name of a reference clock
- `sess.media = <string>`: the media type audio|midi|opus, default audio
- `stream.props = {}`: properties to be passed to the stream
- `aes67.driver-group = <string>`: for AES67 streams, can be specified in order to allow
      the sink to be driven by a different node than the PTP driver.

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
# ~/.config/pipewire/pipewire.conf.d/my-rtp-sink.conf

context.modules = [
{   name = libpipewire-module-rtp-sink
    args = {
        #local.ifname = "eth0"
        #source.ip = "0.0.0.0"
        #destination.ip = "224.0.0.56"
        #destination.port = 46000
        #net.mtu = 1280
        #net.ttl = 1
        #net.loop = false
        #sess.min-ptime = 2
        #sess.max-ptime = 20
        #sess.name = "PipeWire RTP stream"
        #sess.media = "audio"
        #audio.format = "S16BE"
        #audio.rate = 48000
        #audio.channels = 2
        #audio.position = [ FL FR ]
        stream.props = {
            node.name = "rtp-sink"
        }
    }
}
]
```

 0.3.60
