# Example Sink

The example sink is a good starting point for writing a custom
sink. We refer to the source code for more information.

## Module Name

`libpipewire-module-example-sink`

## Module Options

- `node.name`: a unique name for the stream
- `node.description`: a human readable name for the stream
- `stream.props = {}`: properties to be passed to the stream

## General options

Options with well-known behavior.

- PW_KEY_REMOTE_NAME
- PW_KEY_AUDIO_FORMAT
- PW_KEY_AUDIO_RATE
- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_MEDIA_NAME
- PW_KEY_NODE_LATENCY
- PW_KEY_NODE_NAME
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_NODE_GROUP
- PW_KEY_NODE_VIRTUAL
- PW_KEY_MEDIA_CLASS

## Example configuration

```
# ~/.config/pipewire/pipewire.conf.d/my-example-sink.conf

context.modules = [
{   name = libpipewire-module-example-sink
    args = {
        node.name = "example_sink"
        node.description = "My Example Sink"
        stream.props = {
            audio.position = [ FL FR ]
        }
    }
}
]
```
