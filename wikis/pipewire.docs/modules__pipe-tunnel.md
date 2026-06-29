# Unix Pipe Tunnel

The pipe-tunnel module provides a source or sink that tunnels all audio to
or from a unix pipe respectively.

## Module Name

`libpipewire-module-pipe-tunnel`

## Module Options

- `tunnel.mode`: the desired tunnel to create. (Default `playback`)
- `tunnel.may-pause`: if the tunnel stream is allowed to pause on xrun
- `pipe.filename`: the filename of the pipe.
- `stream.props`: Extra properties for the local stream.

When `tunnel.mode` is `capture`, a capture stream on the default source is
created. The samples captured from the source will be written to the pipe.

When `tunnel.mode` is `sink`, a sink node is created. Samples played on the
sink will be written to the pipe.

When `tunnel.mode` is `playback`, a playback stream on the default sink is
created. The samples read from the pipe will be played on the sink.

When `tunnel.mode` is `source`, a source node is created. Samples read from
the the pipe will be made available on the source.

`tunnel.may-pause` allows the tunnel stream to become inactive (paused) when
there is no data in the fifo or when the fifo is full. For `capture` and
`playback` `tunnel.mode` this is by default true. For `source` and `sink`
`tunnel.mode`, this is by default false. A paused stream will consume no
CPU and will resume when the fifo becomes readable or writable again.

When `pipe.filename` is not given, a default fifo in `/tmp/fifo_input` or
`/tmp/fifo_output` will be created that can be written and read respectively,
depending on the selected `tunnel.mode`.

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
- PW_KEY_TARGET_OBJECT to specify the remote name or serial id to link to

When not otherwise specified, the pipe will accept or produce a
16 bits, stereo, 48KHz sample stream.

## Example configuration of a pipe playback stream

```
# ~/.config/pipewire/pipewire.conf.d/my-pipe-tunnel.conf

context.modules = [
{   name = libpipewire-module-pipe-tunnel
    args = {
        tunnel.mode = playback
        #tunnel.may-pause = true
        # Set the pipe name to tunnel to
        pipe.filename = "/tmp/fifo_output"
        #audio.format=<sample format>
        #audio.rate=<sample rate>
        #audio.channels=<number of channels>
        #audio.position=<channel map>
        #target.object=<remote target node>
        stream.props = {
            # extra sink properties
        }
    }
}
]
```
