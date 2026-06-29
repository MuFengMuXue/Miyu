# Combine Stream

The combine stream can make:

- a new virtual sink that forwards audio to other sinks
- a new virtual source that combines audio from other sources
- a new virtual source that combines audio from the monitor ports of all sinks

The sources and sink that need to be combined can be selected using generic match
rules. This makes it possible to combine static nodes or nodes based on certain
properties.

## Module Name

`libpipewire-module-combine-stream`

## Module Options

- `node.name`: a unique name for the stream
- `node.description`: a human readable name for the stream
- `combine.mode` = capture | playback | sink | source | monitor, default sink
- `combine.latency-compensate`: use delay buffers to match stream latencies
- `combine.on-demand-streams`: use metadata to create streams on demand
- `combine.props = {}`: properties to be passed to the sink/source
- `stream.props = {}`: properties to be passed to the streams
- `stream.rules = {}`: rules for matching streams, use create-stream actions

## General options

Options with well-known behavior.

- PW_KEY_REMOTE_NAME
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

## Stream options

- `audio.position`: Set the stream channel map. By default this is the same channel
                    map as the combine stream. You can also use audio.layout
- `combine.audio.position`: map the combine audio positions to the stream positions.
                    combine input channels are mapped one-by-one to stream output channels.
                    You can also use combine.audio.layout.

## Example configuration

```
# ~/.config/pipewire/pipewire.conf.d/my-combine-stream-1.conf

context.modules = [
{   name = libpipewire-module-combine-stream
    args = {
        combine.mode = sink
        node.name = "combine_sink"
        node.description = "My Combine Sink"
        combine.latency-compensate = false
        combine.props = {
            audio.position = [ FL FR ]
        }
        stream.props = {
        }
        stream.rules = [
            {
                matches = [
                    # any of the items in matches needs to match, if one does,
                    # actions are emitted.
                    {
                        # all keys must match the value. ! negates. ~ starts regex.
                        #node.name = "~alsa_input.*"
                        media.class = "Audio/Sink"
                    }
                ]
                actions = {
                    create-stream = {
                        #combine.audio.position = [ FL FR ]
                        #audio.position = [ FL FR ]
                    }
                }
            }
        ]
    }
}
]
```

Below is an example configuration that makes a 5.1 virtual audio sink
from 3 separate stereo sinks.

```
# ~/.config/pipewire/pipewire.conf.d/my-combine-stream-2.conf

context.modules = [
{   name = libpipewire-module-combine-stream
    args = {
        combine.mode = sink
        node.name = "combine_sink_5_1"
        node.description = "My 5.1 Combine Sink"
        combine.latency-compensate = false
        combine.props = {
            audio.position = [ FL FR FC LFE SL SR ]
        }
        stream.props = {
                stream.dont-remix = true      # link matching channels without remixing
        }
        stream.rules = [
            {   matches = [
                    {   media.class = "Audio/Sink"
                        node.name = "alsa_output.usb-Topping_E30-00.analog-stereo"
                    } ]
                actions = { create-stream = {
                        combine.audio.position = [ FL FR ]
                        audio.position = [ FL FR ]
                } } }
            {   matches = [
                    {   media.class = "Audio/Sink"
                        node.name = "alsa_output.usb-BEHRINGER_UMC404HD_192k-00.pro-output-0"
                    } ]
                actions = { create-stream = {
                        combine.audio.position = [ FC LFE ]
                        audio.position = [ AUX0 AUX1 ]
                } } }
            {   matches = [
                    {   media.class = "Audio/Sink"
                        node.name = "alsa_output.pci-0000_00_1b.0.analog-stereo"
                    } ]
                actions = { create-stream = {
                        combine.audio.position = [ SL SR ]
                        audio.position = [ FL FR ]
                } } }
        ]
    }
}
]
```

Below is an example configuration that makes a 4.0 virtual audio source
from 2 separate stereo sources.

```
# ~/.config/pipewire/pipewire.conf.d/my-combine-stream-3.conf

context.modules = [
{   name = libpipewire-module-combine-stream
    args = {
        combine.mode = source
        node.name = "combine_source_4_0"
        node.description = "My 4.0 Combine Source"
        combine.props = {
            audio.position = [ FL FR SL SR ]
        }
        stream.props = {
                stream.dont-remix = true
        }
        stream.rules = [
            {   matches = [
                    {   media.class = "Audio/Source"
                        node.name = "alsa_input.usb-046d_HD_Pro_Webcam_C920_09D53E1F-02.analog-stereo"
                    } ]
                actions = { create-stream = {
                        audio.position = [ FL FR ]
                        combine.audio.position = [ FL FR ]
                } } }
            {   matches = [
                    {   media.class = "Audio/Source"
                        node.name = "alsa_input.usb-046d_0821_9534DE90-00.analog-stereo"
                    } ]
                actions = { create-stream = {
                        audio.position = [ FL FR ]
                        combine.audio.position = [ SL SR ]
                } } }
        ]
    }
}
]
```
