# sendspin receiver

The `sendspin-recv` module creates a PipeWire source that receives audio
packets using the sendspin protocol.

The receive will listen on a specific port (8928) and create a stream for the
data on the port.

## Module Name

`libpipewire-module-sendspin-recv`

## Module Options

Options specific to the behavior of this module

- `local.ifname = <str>`: interface name to use
- `source.ip = <str>`: the source ip address to listen on, default 127.0.0.1
- `source.port = <int>`: the source port to listen on, default 8928
- `source.path = <str>`: the path to listen on, default "/sendspin"
- `sendspin.ip`: the IP address of the sendspin server
- `sendspin.port`: the port of the sendspin server, default 8927
- `sendspin.path`: the path on the sendspin server, default "/sendspin"
- `sendspin.client-id`: the client id, default "pipewire-$(hostname)"
- `sendspin.client-name`: the client name, default "$(hostname)"
- `sendspin.autoconnect`: Use zeroconf to connect to an available server, default false.
- `sendspin.announce`: Use zeroconf to announce the client, default true unless
                     sendspin.autoconnect or sendspin.ip is given.
- `sendspin.single-server`: Allow only a single server to connect, default true
- `node.always-process = <bool>`: true to receive even when not running
- `stream.props = {}`: properties to be passed to all the stream

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
# ~/.config/pipewire/pipewire.conf.d/my-sendspin-recv.conf

context.modules = [
{   name = libpipewire-module-sendspin-recv
    args = {
        #local.ifname = eth0
        #source.ip = 127.0.0.1
        #source.port = 8928
        #source.path = "/sendspin"
        #sendspin.ip = 127.0.0.1
        #sendspin.port = 8927
        #sendspin.path = "/sendspin"
        #sendspin.client-id = "pipewire-test"
        #sendspin.client-name = "PipeWire Test"
        #sendspin.autoconnect = false
        #sendspin.announce = true
        #sendspin.single-server = true
        #node.always-process = false
        #audio.position = [ FL FR ]
        stream.props = {
           #media.class = "Audio/Source"
           #node.name = "sendspin-receiver"
        }
    }
}
]
```

 1.6.0
