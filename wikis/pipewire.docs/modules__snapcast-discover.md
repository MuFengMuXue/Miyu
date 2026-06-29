# Snapcast Discover

Automatically creates a Snapcast sink device based on zeroconf
information.

This module will load module-protocol-simple for each announced stream that matches
the rule with the create-stream action and passes the properties to the module.

If no stream.rules are given, it will create a sink for all announced
snapcast servers.

A new stream will be created on the snapcast server with the given
`snapcast.stream-name` or `PipeWire-<hostname>`. You will need to route this new
stream to clients with the snapcast control application.

## Module Name

`libpipewire-module-snapcast-discover`

## Module Options

Options specific to the behavior of this module

- `snapcast.discover-local` = allow discovery of local services as well.
   false by default.
- `stream.rules` = <rules>: match rules, use create-stream actions. See
  Protocol Simple for module properties.

### stream.rules matches

 - `snapcast.ip`: the IP address of the snapcast server
 - `snapcast.port`: the port of the snapcast server
 - `snapcast.ifindex`: the interface index where the snapcast announcement
                       was received.
 - `snapcast.ifname`: the interface name where the snapcast announcement
                       was received.
 - `snapcast.name`: the name of the snapcast server
 - `snapcast.hostname`: the hostname of the snapcast server
 - `snapcast.domain`: the domain of the snapcast server

### stream.rules create-stream

In addition to all the properties that can be passed to
Protocol Simple, you can also set:

- `snapcast.stream-name`: The name of the stream on a snapcast server.
- `node.name`: The name of the sink that is created on the sender.

## Example configuration

```
# ~/.config/pipewire/pipewire.conf.d/my-snapcast-discover.conf

context.modules = [
{   name = libpipewire-module-snapcast-discover
    args = {
        stream.rules = [
            {   matches = [
                    {    snapcast.ip = "~.*"
                         #snapcast.port = 1000
                         #snapcast.ifindex = 1
                         #snapcast.ifname = eth0
                         #snapcast.name = ""
                         #snapcast.hostname = ""
                         #snapcast.domain = ""
                    }
                ]
                actions = {
                    create-stream = {
                        #audio.rate = 44100
                        #audio.format = S16LE   # S16LE, S24_32LE, S32LE
                        #audio.channels = 2
                        #audio.position = [ FL FR ]
                        #
                        # The stream name as is appears on the snapcast
                        # server:
                        #snapcast.stream-name = "PipeWire"
                        #
                        # The name of the sink on the sender:
                        #node.name = "Snapcast Sink"
                        #
                        #capture = true
                        #server.address = [ "tcp:4711" ]
                        #capture.props = {
                            #target.object = ""
                            #node.latency = 2048/48000
                            #media.class = "Audio/Sink"
                        #}
                    }
                }
            }
        ]
    }
}
]
```

## See also

Protocol Simple
