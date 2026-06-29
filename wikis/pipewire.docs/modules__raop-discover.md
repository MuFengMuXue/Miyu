# RAOP Discover

Automatically creates RAOP (Airplay) sink devices based on zeroconf
information.

This module will load module-raop-sink for each announced stream that matches
the rule with the create-stream action.

If no stream.rules are given, it will create a sink for all announced
streams.

## Module Name

`libpipewire-module-raop-discover`

## Module Options

Options specific to the behavior of this module

- `raop.discover-local` = allow discovery of local services as well.
   false by default.
- `raop.latency.ms` = latency for all streams in microseconds. This
   can be overwritten in the stream rules.
- `stream.rules` = <rules>: match rules, use create-stream actions. See
  AirPlay Sink for module properties.

## Example configuration

```
# ~/.config/pipewire/pipewire.conf.d/my-raop-discover.conf

context.modules = [
{   name = libpipewire-module-raop-discover
    args = {
        #raop.discover-local = false;
        #raop.latency.ms = 1000
        stream.rules = [
            {   matches = [
                    {    raop.ip = "~.*"
                         #raop.port = 1000
                         #raop.name = ""
                         #raop.hostname = ""
                         #raop.domain = ""
                         #raop.device = ""
                         #raop.transport = "udp" | "tcp"
                         #raop.encryption.type = "none" | "RSA" | "auth_setup" | "fp_sap25"
                         #raop.audio.codec = "PCM" | "ALAC" | "AAC" | "AAC-ELD"
                         #audio.channels = 2
                         #audio.format = "S16" | "S24" | "S32"
                         #audio.rate = 44100
                         #device.model = ""
                    }
                ]
                actions = {
                    create-stream = {
                        #raop.password = ""
                        stream.props = {
                            #target.object = ""
                            #media.class = "Audio/Sink"
                        }
                    }
                }
            }
        ]
    }
}
]
```

## See also

AirPlay Sink
