# sendspin sender

The `sendspin-send` module creates a PipeWire sink that sends audio
packets using the sendspin protocol to a client.

The sender will listen on a specific port (8927) and create a stream for
each connection.

In combination with a virtual sink, each of the client streams can be sent
the same data in the client specific format.

## Module Name

`libpipewire-module-sendspin-send`

## Module Options

Options specific to the behavior of this module

- `local.ifname = <str>`: interface name to use
- `local.ifaddress = <str>`: interface address to use
- `source.ip = <str>`: the source ip address to listen on, default "127.0.0.1"
- `source.port = <int>`: the source port to listen on, default 8927
- `source.path = <str>`: comma separated list of paths to listen on,
                 default "/sendspin"
- `sendspin.ip`: an array of IP addresses of sendspin clients to connect to
- `sendspin.port`: the port of the sendspin client to connect to, default 8928
- `sendspin.path`: the path of the sendspin client to connect to, default "/sendspin"
- `sendspin.group-id`: the group-id of the server, default random
- `sendspin.group-name`: the group-name of the server, default "PipeWire"
- `sendspin.delay`: the delay to add to clients in seconds. Default 5.0
- `node.always-process = <bool>`: true to send silence even when not connected.
- `stream.props = {}`: properties to be passed to all the stream
- `stream.rules` = <rules>: match rules, use the create-stream action to
                   make a stream for the client.

## General options

Options with well-known behavior:

- PW_KEY_REMOTE_NAME
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
# ~/.config/pipewire/pipewire.conf.d/my-sendspin-send.conf

context.modules = [
{   name = libpipewire-module-sendspin-send
    args = {
        #local.ifname = eth0
        #source.ip = 127.0.0.1
        #source.port = 8927
        #source.path = "/sendspin"
        #sendspin.ip = [ 127.0.0.1 ]
        #sendspin.port = 8928
        #sendspin.path = "/sendspin"
        #sendspin.group-id = "abcded"
        #sendspin.group-name = "PipeWire"
        #sendspin.delay = 5.0
        #node.always-process = false
        #audio.position = [ FL FR ]
        stream.props = {
           #media.class = "Audio/sink"
           #node.name = "sendspin-send"
        }
        stream.rules = [
            {   matches = [
                    {    sendspin.ip = "~.*"
                         #sendspin.port = 8928
                         #sendspin.path = "/sendspin"
                         #zeroconf.ifindex = 0
                         #zeroconf.name = ""
                         #zeroconf.type = "_sendspin._tcp"
                         #zeroconf.domain = "local"
                         #zeroconf.hostname = ""
                    }
                ]
                actions = {
                    create-stream = {
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

 1.6.0
