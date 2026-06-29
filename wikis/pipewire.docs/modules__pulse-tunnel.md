# Pulse Tunnel

The pulse-tunnel module provides a source or sink that tunnels all audio to
a remote PulseAudio connection.

It is usually used with the PulseAudio or module-protocol-pulse on the remote
end to accept the connection.

This module is usually used together with module-zeroconf-discover that will
automatically load the tunnel with the right parameters based on zeroconf
information.

## Module Name

`libpipewire-module-pulse-tunnel`

## Module Options

- `tunnel.mode`: the desired tunnel to create, must be `source` or `sink`.
                 (Default `sink`)
- `pulse.server.address`: the address of the PulseAudio server to tunnel to.
- `pulse.latency`: the latency to end-to-end latency in milliseconds to
                   maintain (Default 200).
- `reconnect.interval.ms`: when the remote connection is broken, retry to connect
                 with this interval in millisconds. A value of 0 disables recovery
                 and will result in a module unload. (Default 0) (Since 1.1.0)
- `stream.props`: Extra properties for the local stream.

## General options

Options with well-known behavior.

- PW_KEY_REMOTE_NAME
- PW_KEY_AUDIO_FORMAT
- PW_KEY_AUDIO_RATE
- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_NODE_LATENCY
- PW_KEY_NODE_NAME
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_NODE_GROUP
- PW_KEY_NODE_VIRTUAL
- PW_KEY_MEDIA_CLASS
- PW_KEY_TARGET_OBJECT to specify the remote node.name or serial.id to link to

## Example configuration of a virtual sink

```
# ~/.config/pipewire/pipewire.conf.d/my-pulse-tunnel.conf

context.modules = [
{   name = libpipewire-module-pulse-tunnel
    args = {
        tunnel.mode = sink
        # Set the remote address to tunnel to
        pulse.server.address = "tcp:192.168.1.126"
        #pulse.latency = 200
        #reconnect.interval.ms = 0
        #audio.rate=<sample rate>
        #audio.channels=<number of channels>
        #audio.position=<channel map>
        #target.object=<remote target name>
        stream.props = {
            # extra sink properties
        }
    }
}
]
```
