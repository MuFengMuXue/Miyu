# Protocol Simple

The simple protocol provides a bidirectional audio stream on a network
socket.

It is meant to be used with the `simple protocol player` app, available on
Android to play and record a stream.

Each client that connects will create a capture and/or playback stream,
depending on the configuration options.

You can also use it to feed audio data to other clients such as the snapcast
server.

## Module Name

`libpipewire-module-protocol-simple`

## Module Options

 - `capture`: boolean if capture is enabled. This will create a capture stream or
              sink for each connected client.
 - `playback`: boolean if playback is enabled. This will create a playback or
              source stream for each connected client.
 - `local.ifname = <str>`: interface name to use
 - `local.ifaddress = <str>`: interface address to use
 - `server.address = []`: an array of server addresses to listen on as
                           tcp:(<ip>:)<port>.
 - `capture.props`: optional properties for the capture stream
 - `playback.props`: optional properties for the playback stream

## General options

Options with well-known behavior.

- PW_KEY_REMOTE_NAME
- PW_KEY_AUDIO_RATE
- PW_KEY_AUDIO_FORMAT
- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_NODE_LATENCY
- PW_KEY_NODE_RATE
- PW_KEY_STREAM_CAPTURE_SINK
- PW_KEY_NODE_NAME
- PW_KEY_TARGET_OBJECT

By default the server will work with stereo 16 bits samples at 44.1KHz.

## Example configuration

```
# ~/.config/pipewire/pipewire.conf.d/my-protocol-simple.conf

context.modules = [
{   name = libpipewire-module-protocol-simple
    args = {
        # Provide capture stream, clients can capture data from PipeWire
        capture = true
        #
        # Provide playback stream, client can send data to PipeWire for playback
        playback = true
        #
        #audio.rate = 44100
        #audio.format = S16
        #audio.channels = 2
        #audio.position = [ FL FR ]
        #
        # The addresses this server listens on for new
        # client connections
        server.address = [
            "tcp:4711"
        ]
        capture.props = {
            # The node name or id to use for capture.
            #target.object = null
            #
            # To make the capture stream capture the monitor ports
            #stream.capture.sink = false
            #
            # Make this a sink instead of a capture stream
            #media.class = Audio/Sink
        }
        playback.props = {
            # The node name or id to use for playback.
            #target.object = null
            #
            # Make this a source instead of a playback stream
            #media.class = Audio/Source
        }
    }
}
]
```

## Example configuration for a snapcast server

```
context.modules = [
{   name = libpipewire-module-protocol-simple
    args = {
        # Provide sink
        capture = true
        audio.rate = 48000
        audio.format = S16
        audio.channels = 2
        audio.position = [ FL FR ]

        # The addresses this server listens on for new
        # client connections
        server.address = [
            "tcp:4711"
        ]
        capture.props = {
            # Make this a sink instead of a capture stream
            media.class = Audio/Sink
        }
    }
}
]

On the snapcast server, add the following to the `snapserver.conf` file:

```
[stream]
sampleformat =  48000:16:2
source = tcp://127.0.0.1:4711?name=PipeWireSnapcast&mode=client
```

Snapcast will try to connect to the protocol-simple server and fetch the
samples from it. Snapcast tries to reconnect when the connection is somehow
broken.
