# Example Filter

The example filter is a good starting point for writing a custom
filter. We refer to the source code for more information.

## Module Name

`libpipewire-module-example-filter`

## Module Options

- `node.description`: a human readable name for the filter streams
- `capture.props = {}`: properties to be passed to the input stream
- `playback.props = {}`: properties to be passed to the output stream

## General options

Options with well-known behavior. Most options can be added to the global
configuration or the individual streams:

- PW_KEY_REMOTE_NAME
- PW_KEY_AUDIO_RATE
- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_MEDIA_NAME
- PW_KEY_NODE_LATENCY
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_NODE_GROUP
- PW_KEY_NODE_LINK_GROUP
- PW_KEY_NODE_VIRTUAL
- PW_KEY_NODE_NAME : See notes below. If not specified, defaults to
  	'filter-PID-MODULEID'.

Stream only properties:

- PW_KEY_MEDIA_CLASS
- PW_KEY_NODE_NAME :  if not given per stream, the global node.name will be
        prefixed with 'input.' and 'output.' to generate a capture and playback
        stream node.name respectively.

## Example configuration of a virtual source

```
# ~/.config/pipewire/pipewire.conf.d/my-example-filter.conf

context.modules = [
{   name = libpipewire-module-example-filter
    args = {
      node.description = "Example Filter"
      capture.props = {
          audio.position = [ FL FR ]
          node.passive = true
      }
      playback.props = {
          node.name = "Example Filter"
          media.class = "Audio/Source"
          audio.position = [ FL FR ]
      }
    }
}
]
```

```
pw-cli -m lm libpipewire-module-example-filter '{ audio.position=[FL FR] }'
```
