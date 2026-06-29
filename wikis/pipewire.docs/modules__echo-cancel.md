# Echo Cancel

The `echo-cancel` module performs echo cancellation. The module creates
virtual `echo-cancel-capture` source and `echo-cancel-playback` sink
nodes and the associated streams.

The echo-cancel module is mostly used in video or audio conference
applications. When the other participants talk and the audio is going out to
the speakers, the signal will be picked up again by the microphone and sent
back to the other participants (along with your talking), resulting in an
echo. This is annoying because the other participants will hear their own
echo from you.

Conceptually the echo-canceler is composed of 4 streams:

```
.--------.     .---------.     .--------.     .----------.     .-------.
|  mic   | --> | capture | --> |        | --> |  source  | --> |  app  |
'--------'     '---------'     | echo   |     '----------'     '-------'
                               | cancel |
.--------.     .---------.     |        |     .----------.     .---------.
|  app   | --> |  sink   | --> |        | --> | playback | --> | speaker |
'--------'     '---------'     '--------'     '----------'     '---------'
```

- A capture stream that captures audio from a microphone.
- A Sink that takes the signal containing the data that should be canceled
  out from the capture stream. This is where the application (video conference
  application) send the audio to and it contains the signal from the other
  participants that are speaking and that needs to be cancelled out.
- A playback stream that just passes the signal from the Sink to the speaker.
  This is so that you can hear the other participants. It is also the signal
  that gets picked up by the microphone and that eventually needs to be
  removed again.
- A Source that exposes the echo-canceled data captured from the capture
  stream. The data from the sink stream and capture stream are correlated and
  the signal from the sink stream is removed from the capture stream data.
  This data then goes into the application (the conference application) and
  does not contain the echo from the other participants anymore.

## Module Name

`libpipewire-module-echo-cancel`

## Module Options

Options specific to the behavior of this module

- `capture.props = {}`: properties to be passed to the capture stream
- `source.props = {}`: properties to be passed to the source stream
- `sink.props = {}`: properties to be passed to the sink stream
- `playback.props = {}`: properties to be passed to the playback stream
- `library.name = <str>`: the echo cancellation library  Currently supported:
`aec/libspa-aec-webrtc`. Leave unset to use the default method (`aec/libspa-aec-webrtc`).
- `aec.args = <str>`: arguments to pass to the echo cancellation method
- `monitor.mode`: Instead of making a sink, make a stream that captures from
                  the monitor ports of the default sink.

## General options

Options with well-known behavior:

- PW_KEY_AUDIO_RATE
- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_MEDIA_CLASS
- PW_KEY_NODE_LATENCY
- PW_KEY_NODE_NAME
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_NODE_GROUP
- PW_KEY_NODE_LINK_GROUP
- PW_KEY_NODE_VIRTUAL
- PW_KEY_NODE_LATENCY
- PW_KEY_REMOTE_NAME

## Example configuration
```
# ~/.config/pipewire/pipewire.conf.d/my-echo-cancel.conf

context.modules = [
 {   name = libpipewire-module-echo-cancel
     args = {
         # library.name  = aec/libspa-aec-webrtc
         # node.latency = 1024/48000
         # monitor.mode = false
         capture.props = {
            node.name = "Echo Cancellation Capture"
         }
         source.props = {
            node.name = "Echo Cancellation Source"
         }
         sink.props = {
            node.name = "Echo Cancellation Sink"
         }
         playback.props = {
            node.name = "Echo Cancellation Playback"
         }
     }
 }
]
```
