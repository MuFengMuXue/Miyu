# FFADO firewire audio driver

The ffado-driver module provides a source or sink using the libffado library for
reading and writing to firewire audio devices.

## Module Name

`libpipewire-module-ffado-driver`

## Module Options

- `driver.mode`: the driver mode, sink|source|duplex, default duplex
- `ffado.devices`: array of devices to open, default "hw:0"
- `ffado.period-size`: period size,default 1024. A value of 0 will use the graph duration.
- `ffado.period-num`: period number,default 3
- `ffado.sample-rate`: sample-rate, default 48000. A value of 0 will use the graph rate.
- `ffado.slave-mode`: slave mode
- `ffado.snoop-mode`: snoop mode
- `ffado.verbose`: ffado verbose level
- `ffado.rtprio`: ffado realtime priority, this is by default the PipeWire server
                  priority + 5
- `ffado.realtime`: ffado realtime mode. this requires correctly configured rlimits
                    to acquire FIFO scheduling at the ffado.rtprio priority
- `latency.internal.input`: extra input latency in frames
- `latency.internal.output`: extra output latency in frames
- `source.props`: Extra properties for the source filter
- `sink.props`: Extra properties for the sink filter

## General options

Options with well-known behavior.

- PW_KEY_REMOTE_NAME
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
# ~/.config/pipewire/pipewire.conf.d/my-ffado-driver.conf

context.modules = [
{   name = libpipewire-module-ffado-driver
    args = {
        #driver.mode       = duplex
        #ffado.devices     = [ "hw:0" ]
        #ffado.period-size = 1024
        #ffado.period-num  = 3
        #ffado.sample-rate = 48000
        #ffado.slave-mode  = false
        #ffado.snoop-mode  = false
        #ffado.verbose     = 0
        #ffado.rtprio      = 65
        #ffado.realtime    = true
        #latency.internal.input  = 0
        #latency.internal.output = 0
        #audio.position    = [ FL FR ]
        source.props = {
            # extra sink properties
        }
        sink.props = {
            # extra sink properties
        }
    }
}
]
```
