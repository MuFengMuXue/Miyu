# ROC source

The `roc-source` module creates a PipeWire source that receives samples
from ROC sender and passes them to the sink it is connected to. One can
then connect it to any audio device.

## Module Name

`libpipewire-module-roc-source`

## Module Options

Options specific to the behavior of this module

- `source.props = {}`: properties to be passed to the source stream
- `source.name = <str>`: node.name of the source
- `local.ip = <str>`: local sender ip
- `local.source.port = <str>`: local receiver TCP/UDP port for source packets
- `local.repair.port = <str>`: local receiver TCP/UDP port for receiver packets
- `local.control.port = <str>`: local receiver TCP/UDP port for control packets
- `sess.latency.msec = <str>`: target network latency in milliseconds
- `roc.resampler.backend = <str>`: Possible values: `default`, `builtin`,
      `speex`, `speexdec`.
- `roc.resampler.profile = <str>`: Possible values: `default`, `high`,
      `medium`, `low`.
- `roc.latency-tuner.backend = <str>`: Possible values: `default`, `niq`
- `roc.latency-tuner.profile = <str>`: Possible values: `default`, `intact`,
      `responsive`, `gradual`
- `fec.code = <str>`: Possible values: `default`, `disable`, `rs8m`, `ldpc`

- `resampler.profile = <str>`: Deprecated, use roc.resampler.profile
- `log.level = <str>`: log level for roc-toolkit. Possible values: `DEFAULT`,
      `NONE`, `ERROR`, `INFO`, `DEBUG`, `TRACE`; `DEFAULT` follows the log
level of the PipeWire context.

## General options

Options with well-known behavior:

- PW_KEY_NODE_NAME
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_NODE_VIRTUAL
- PW_KEY_MEDIA_CLASS
- SPA_KEY_AUDIO_POSITION

## Example configuration
```
# ~/.config/pipewire/pipewire.conf.d/my-roc-source.conf

context.modules = [
 {   name = libpipewire-module-roc-source
     args = {
         local.ip = 0.0.0.0
         #roc.resampler.backend = default
         roc.resampler.profile = medium
         #roc.latency-tuner.backend = default
         #roc.latency-tuner.profile = default
         fec.code = disable
         sess.latency.msec = 5000
         local.source.port = 10001
         local.repair.port = 10002
         local.control.port = 10003
         source.name = "ROC Source"
         source.props = {
            node.name = "roc-source"
         }
         audio.position = [ FL FR ]
         log.level = DEFAULT
     }
 }
]
```
