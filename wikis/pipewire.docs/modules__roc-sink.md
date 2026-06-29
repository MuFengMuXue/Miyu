# ROC sink

The `roc-sink` module creates a PipeWire sink that sends samples to
a preconfigured receiver address. One can then connect an audio stream
of any running application to that sink or make it the default sink.

## Module Name

`libpipewire-module-roc-sink`

## Module Options

Options specific to the behavior of this module

- `sink.props = {}`: properties to be passed to the sink stream
- `sink.name = <str>`: node.name of the sink
- `remote.ip = <str>`: remote receiver ip
- `remote.source.port = <str>`: remote receiver TCP/UDP port for source packets
- `remote.repair.port = <str>`: remote receiver TCP/UDP port for receiver packets
- `remote.control.port = <str>`: remote receiver TCP/UDP port for control packets
- `fec.code = <str>`: Possible values: `disable`, `rs8m`, `ldpc`
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
# ~/.config/pipewire/pipewire.conf.d/my-roc-sink.conf

context.modules = [
 {   name = libpipewire-module-roc-sink
     args = {
         fec.code = disable
         remote.ip = 192.168.0.244
         remote.source.port = 10001
         remote.repair.port = 10002
         remote.control.port = 10003
         sink.name = "ROC Sink"
         sink.props = {
            node.name = "roc-sink"
         }
         audio.position = [ FL FR ]
         log.level = DEFAULT
     }
 }
]
```
