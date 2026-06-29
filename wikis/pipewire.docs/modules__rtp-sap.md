# SAP Announce and create RTP streams

The `rtp-sap` module announces RTP streams that match the rules with the
announce-stream action.

It will create source RTP streams that are announced with SAP when they
match the rule with the create-stream action.

If no stream.rules are given, it will announce all streams with
sess.sap.announce = true and it will create a receiver for all announced
streams.

## Module Name

`libpipewire-module-rtp-sap`

## Module Options

Options specific to the behavior of this module

- `local.ifname = <str>`: interface name to use
- `sap.ip = <str>`: IP address of the SAP messages, default "224.0.0.56"
- `sap.port = <int>`: port of the SAP messages, default 9875
- `sap.cleanup.sec = <int>`: cleanup interval in seconds, default 90 seconds
- `source.ip =<str>`: source IP address, default "0.0.0.0"
- `net.ttl = <int>`: TTL to use, default 1
- `net.loop = <bool>`: loopback multicast, default false
- `stream.rules` = <rules>: match rules, use create-stream and announce-stream actions
- `sap.max-sessions = <int>`: maximum number of concurrent send/receive sessions to track
- `sap.preamble-extra = [strings]`: extra attributes to add to the atomic SDP preamble
- `sap.end-extra = [strings]`: extra attributes to add to the end of the SDP message

## General options

Options with well-known behavior:

- PW_KEY_REMOTE_NAME

## Example configuration
```
# ~/.config/pipewire/pipewire.conf.d/my-rtp-sap.conf

context.modules = [
{   name = libpipewire-module-rtp-sap
    args = {
        #local.ifname = "eth0"
        #sap.ip = "224.0.0.56"
        #sap.port = 9875
        #sap.cleanup.sec = 5
        #source.ip = "0.0.0.0"
        #net.ttl = 1
        #net.loop = false
        stream.rules = [
            {   matches = [
                    # any of the items in matches needs to match, if one does,
                    # actions are emitted.
                    {   # all keys must match the value. ! negates. ~ starts regex.
                        #rtp.origin = "wim 3883629975 0 IN IP4 0.0.0.0"
                        #rtp.payload = "127"
                        #rtp.fmt = "L16/48000/2"
                        #rtp.session = "PipeWire RTP Stream on fedora"
                        #rtp.ts-offset = 0
                        #rtp.ts-refclk = "private"
                        sess.sap.announce = true
                    }
                ]
                actions = {
                    announce-stream = {
                    }
                }
            }
            {   matches = [
                    {   # all keys must match the value. ! negates. ~ starts regex.
                        #rtp.origin = "wim 3883629975 0 IN IP4 0.0.0.0"
                        #rtp.payload = "127"
                        #rtp.fmt = "L16/48000/2"
                        #rtp.session = "PipeWire RTP Stream on fedora"
                        #rtp.ts-offset = 0
                        #rtp.ts-refclk = "private"
                        rtp.session = "~.*"
                    }
                ]
                actions = {
                    create-stream = {
                        #sess.latency.msec = 100
                        #sess.ts-direct = false
                        #target.object = ""
                    }
                }
            }
        ]
    }
}
]
```

 0.3.67
