# Netjack2 driver

The netjack2-driver module provides a source or sink that is following a
netjack2 manager. It is meant to be used over stable (ethernet) network
connections with minimal latency and jitter.

The driver normally decides how many ports it will send and receive from the
manager. By default however, these values are set to -1 so that the manager
decides on the number of ports.

With the global or per stream audio.port and midi.ports properties this
behaviour can be adjusted.

The driver will send out UDP messages on a (typically) multicast address to
inform the manager of the available driver. This will then instruct the manager
to configure and start the driver.

On the driver side, a sink and/or source with the specified numner of audio and
midi ports will be created. On the manager side there will be a corresponding
source and/or sink created respectively.

The driver will be scheduled with exactly the same period as the manager but with
a configurable number of periods of delay (see netjack2.latency, default 2).

## Module Name

`libpipewire-module-netjack2-driver`

## Module Options

- `driver.mode`: the driver mode, sink|source|duplex, default duplex. This set the
   per stream audio.port and midi.ports default from -1 to 0. sink mode defaults to
   no source ports, source mode to no sink ports and duplex leaves the defaults as
   they are.
- `local.ifname = <str>`: interface name to use
- `net.ip =<str>`: multicast IP address, default "225.3.19.154"
- `net.port =<int>`: control port, default 19000
- `net.mtu = <int>`: MTU to use, default 1500
- `net.ttl = <int>`: TTL to use, default 1
- `net.loop = <bool>`: loopback multicast, default false
- `source.ip =<str>`: IP address to bind to, default "0.0.0.0"
- `source.port =<int>`: port to bind to, default 0 (allocate)
- `netjack2.client-name`: the name of the NETJACK2 client.
- `netjack2.latency`: the latency in cycles, default 2
- `audio.ports`: the number of audio ports. Can also be added to the stream props.
     A value of -1 will configure to the number of audio ports on the manager.
- `midi.ports`: the number of midi ports. Can also be added to the stream props.
     A value of -1 will configure to the number of midi ports on the manager.
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
# ~/.config/pipewire/pipewire.conf.d/my-netjack2-driver.conf

context.modules = [
{   name = libpipewire-module-netjack2-driver
    args = {
        #netjack2.client-name = PipeWire
        #netjack2.latency     = 2
        #midi.ports           = 0
        #audio.ports          = -1
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
