# Netjack2 manager

The netjack2 manager module listens for new netjack2 driver messages and will
start a communication channel with them.

Messages are received on a (typically) multicast address.

Normally, the driver will specify the number of send and receive channels it
wants to set up with the manager. If the driver however specifies a don't-care
value of -1, the audio.ports and midi.ports configuration values of the manager
are used.

The manager will create the corresponding streams to send and receive data
to/from the drivers. These are usually sink and sources but with the
netjack2.connect property, these will be streams that will be autoconnected to
the default source and sink by the session manager.

## Module Name

`libpipewire-module-netjack2-manager`

## Module Options

- `local.ifname = <str>`: interface name to use
- `net.ip =<str>`: multicast IP address, default "225.3.19.154"
- `net.port =<int>`: control port, default "19000"
- `net.mtu = <int>`: MTU to use, default 1500
- `net.ttl = <int>`: TTL to use, default 1
- `net.loop = <bool>`: loopback multicast, default false
- `netjack2.connect`: if jack ports should be connected automatically. Can also be
                  placed per stream, default false.
- `netjack2.sample-rate`: the sample rate to use, default 48000
- `netjack2.period-size`: the buffer size to use, default 1024
- `netjack2.encoding`: the encoding, float|opus|int, default float
- `netjack2.kbps`: the number of kilobits per second when encoding, default 64
- `netjack2.max-followers`: the maximum number of concurrent followers, default 64
- `audio.ports`: the number of audio ports. Can also be added to the stream props. This
    is the default suggestion for drivers that don't specify any number of audio channels.
- `midi.ports`: the number of midi ports. Can also be added to the stream props. This
    is the default suggestion for drivers that don't specify any number of midi channels.
- `audio.position`: default channel position for the number of audio.ports.
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
# ~/.config/pipewire/pipewire.conf.d/my-netjack2-manager.conf

context.modules = [
{   name = libpipewire-module-netjack2-manager
    args = {
        #netjack2.connect     = true
        #netjack2.sample-rate = 48000
        #netjack2.period-size = 1024
        #netjack2.encoding    = float # float|opus
        #netjack2.kbps        = 64
        #netjack2.max-followers = 64
        #audio.ports          = 0
        #midi.ports           = 0
        #audio.channels       = 2
        #audio.position       = [ FL FR ]
        source.props = {
            # extra source properties
        }
        sink.props = {
            # extra sink properties
        }
    }
}
]
```
