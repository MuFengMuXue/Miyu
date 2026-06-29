# RTP source

The `rtp-source` module creates a PipeWire source that receives audio RTP packets.
These RTP packets may contain raw PCM data, Opus encoded audio, or midi audio.

This module is usually loaded from the SAP Announce and create RTP streams so that the
source.ip and source.port and format parameters matches that of the sender that
is announced via SAP.

## Module Name

`libpipewire-module-rtp-source`

## Module Options

Options specific to the behavior of this module

- `local.ifname = <str>`: interface name to use
- `source.ip = <str>`: the source ip address, default 224.0.0.56. Set this to the IP address
               you want to receive packets from or 0.0.0.0 to receive from any source address.
- `source.port = <int>`: the source port
- `node.always-process = <bool>`: true to receive even when not running
- `sess.latency.msec = <float>`: target network latency in milliseconds, default 100
- `sess.ignore-ssrc = <bool>`: ignore SSRC, default false
- `sess.media = <string>`: the media type audio|midi|opus, default audio
- `sess.ts-direct = <bool>`: use direct timestamp mode, default false
               (see the Buffer Modes section below)
- `stream.may-pause = <bool>`: pause the stream when no data is reveived, default false
- `stream.props = {}`: properties to be passed to the stream

## General options

Options with well-known behavior:

- PW_KEY_REMOTE_NAME
- PW_KEY_AUDIO_FORMAT
- PW_KEY_AUDIO_RATE
- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_MEDIA_NAME
- PW_KEY_MEDIA_CLASS
- PW_KEY_NODE_NAME
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_NODE_GROUP
- PW_KEY_NODE_LATENCY
- PW_KEY_NODE_VIRTUAL

## Example configuration
```
# ~/.config/pipewire/pipewire.conf.d/my-rtp-source.conf

context.modules = [
{   name = libpipewire-module-rtp-source
    args = {
        #local.ifname = eth0
        #source.ip = 224.0.0.56
        #source.port = 0
        sess.latency.msec = 100
        #sess.ignore-ssrc = false
        #node.always-process = false
        #sess.media = "audio"
        #audio.format = "S16BE"
        #audio.rate = 48000
        #audio.channels = 2
        #audio.position = [ FL FR ]
        stream.props = {
           #media.class = "Audio/Source"
           node.name = "rtp-source"
        }
    }
}
]
```

## Buffer modes

RTP source nodes created by this module use an internal ring buffer. Received RTP audio
data is written into this ring buffer. When the node's process callback is run, it reads
from that ring buffer and provides audio data from it to the graph.

The `sess.ts-direct` option controls the _buffer mode_, which defines how this ring buffer
is used. The RTP source nodes created by this module can operate in one of two of these
buffer modes. In both modes, the RTP source node uses the timestamps of incoming RTP
packets to write into the ring buffer (more specifically, at the position
`timestamp + latency from the sess.latency.msec option`). The modes are:

-# *Constant latency mode*: This is the default mode. It is used when `sess.ts-direct`
   is set to false. `sess.latency.msec` then defines the ideal fill level of the ring
   buffer. If the fill level is above or below this, then a DLL is used to adjust the
   consumption of the buffer contents. If the fill level is below a critical value
   (that's the amount of data that is needed in a cycle), or if the fill level equals
   the total buffer size (meaning that no more data can be fed into the buffer), the
   buffer contents are resynchronized, meaning that the existing contents are thrown
   away, and the ring buffer is reset. This buffer mode is useful for when a constant
   latency is desired, and the actual moment playback starts is unimportant (meaning
   that playback is not necessarily in sync with other devices). This mode requires
   no special graph driver.
-# *Direct timestamp mode*: This is an alternate mode, used when `sess.ts-direct` is
   set to true. In this mode, ring buffer over- and underrun and fill level are not
   directly tracked; instead, they are handled implicitly. There is no constant latency
   maintained. The current time (more specifically, the spa_io_clock::position field
   of spa_io_position::clock) is directly used during playback to retrieve audio
   data. This assumes that a graph driver is used whose time is somehow synchronized
   to the sender's. Since the current time is directly used as an offset within the
   ring buffer, the correct data is always pulled from the ring buffer, that is, the
   data that shall be played now, in sync with the sender (and with other receivers).
   This buffer mode is useful for when receivers shall play in sync with each other,
   and shall use one common synchronized time, provided through the spa_io_clock .
   `sess.latency.msec` functions as a configurable assumed maximum transport delay
   instead of a constant latency quantity in this mode. The DLL is not used in this
   mode, since the graph driver is assumed to be synchronized to the sender, as said,
   so any output sinks in the graph will already adjust their consumption pace to
   match the pace of the graph driver.
   AES67 sessions use this mode, for example.

 0.3.60
