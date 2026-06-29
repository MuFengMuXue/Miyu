# AirPlay Sink

Creates a new Sink to stream to an Airplay device.

Normally this sink is automatically created with RAOP Discover
with the right parameters but it is possible to manually create a RAOP sink
as well.

## Module Name

`libpipewire-module-raop-sink`

## Module Options

Options specific to the behavior of this module

- `raop.ip`: The ip address of the remote end.
- `raop.port`: The port of the remote end.
- `raop.name`: The name of the remote end.
- `raop.hostname`: The hostname of the remote end.
- `raop.transport`: The data transport to use, one of "udp" or "tcp". Defaults
                   to "udp".
- `raop.encryption.type`: The encryption type to use. One of "none", "RSA" or
                   "auth_setup". Default is "none".
- `raop.audio.codec`: The audio codec to use. Needs to be "PCM". Defaults to "PCM".
- `raop.password`: The password to use.
- `stream.props = {}`: properties to be passed to the sink stream

Options with well-known behavior.

- PW_KEY_REMOTE_NAME
- PW_KEY_AUDIO_FORMAT
- PW_KEY_AUDIO_RATE
- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_NODE_NAME
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_NODE_GROUP
- PW_KEY_NODE_LATENCY
- PW_KEY_NODE_VIRTUAL
- PW_KEY_MEDIA_CLASS

## Example configuration

```
# ~/.config/pipewire/pipewire.conf.d/my-raop-sink.conf

context.modules = [
{   name = libpipewire-module-raop-sink
    args = {
        # Set the remote address to tunnel to
        raop.ip = "127.0.0.1"
        raop.port = 8190
        raop.name = "my-raop-device"
        raop.hostname = "My Service"
        #raop.transport = "udp"
        raop.encryption.type = "RSA"
        #raop.audio.codec = "PCM"
        #raop.password = "****"
        #audio.format = "S16"
        #audio.rate = 44100
        #audio.channels = 2
        #audio.position = [ FL FR ]
        stream.props = {
            # extra sink properties
        }
    }
}
]
```

## See also

RAOP Discover
