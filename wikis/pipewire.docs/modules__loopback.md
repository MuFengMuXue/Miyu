# Loopback

The loopback module passes the output of a capture stream unmodified to a playback stream.
It can be used to construct a link between a source and sink but also to
create new virtual sinks or sources or to remap channel between streams.

Because both ends of the loopback are built with streams, the session manager can
manage the configuration and connection with the sinks and sources.

## Module Name

`libpipewire-module-loopback`

## Module Options

- `node.description`: a human readable name for the loopback streams
- `target.delay.sec`: delay in seconds as float (Since 0.3.60)
- `capture.props = {}`: properties to be passed to the input stream
- `playback.props = {}`: properties to be passed to the output stream

## General options

Options with well-known behavior. Most options can be added to the global
configuration or the individual streams:

- PW_KEY_REMOTE_NAME
- PW_KEY_AUDIO_RATE
- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_MEDIA_NAME
- PW_KEY_NODE_LATENCY
- PW_KEY_NODE_DESCRIPTION
- PW_KEY_NODE_GROUP
- PW_KEY_NODE_LINK_GROUP
- PW_KEY_NODE_VIRTUAL
- PW_KEY_NODE_NAME : See notes below. If not specified, defaults to
  	'loopback-PID-MODULEID'.

Stream only properties:

- PW_KEY_MEDIA_CLASS
- PW_KEY_NODE_NAME :  if not given per stream, the global node.name will be
        prefixed with 'input.' and 'output.' to generate a capture and playback
        stream node.name respectively.

## Channel handling

Channels from the capture stream are copied, in order, to the channels of the
output stream. The remaining streams are ignored (when capture has more channels)
or filled with silence (when playback has more channels).

When a global channel position is set, both capture and playback will be converted
to and from this common channel layout. This can be used to implement up or
downmixing loopback sinks/sources.

## Example configuration of source to sink link

This loopback links a source node to a sink node. You can change the target.object
properties to match your source/sink node.name.

```
# ~/.config/pipewire/pipewire.conf.d/my-loopback-0.conf

context.modules = [
{   name = libpipewire-module-loopback
    args = {
        capture.props = {
            #  if you want to capture sink monitor ports,
            #  uncomment the next line and set the target.object
            #  to the sink name.
            #stream.capture.sink = true
            target.object = "alsa_input.usb-C-Media_Electronics_Inc._TONOR_TC-777_Audio_Device-00.mono-fallback"
            node.passive = true
            node.dont-reconnect = true
        }
        playback.props = {
            target.object = "alsa_output.usb-0d8c_USB_Sound_Device-00.analog-surround-71"
            node.dont-reconnect = true
            node.passive = true
        }
    }
}
]
```

## Example configuration of a virtual sink

This Virtual sink routes stereo input to the rear channels of a 7.1 sink.

```
# ~/.config/pipewire/pipewire.conf.d/my-loopback-1.conf

context.modules = [
{   name = libpipewire-module-loopback
    args = {
        node.description = "CM106 Stereo Pair 2"
        #target.delay.sec = 1.5
        capture.props = {
            node.name = "CM106_stereo_pair_2"
            media.class = "Audio/Sink"
            audio.position = [ FL FR ]
        }
        playback.props = {
            node.name = "playback.CM106_stereo_pair_2"
            audio.position = [ RL RR ]
            target.object = "alsa_output.usb-0d8c_USB_Sound_Device-00.analog-surround-71"
            node.dont-reconnect = true
            stream.dont-remix = true
            node.passive = true
        }
    }
}
]
```

## Example configuration of a virtual source

This Virtual source routes the front-left channel of a multi-channel input to a mono channel.
This is useful for splitting up multi-channel inputs from USB audio interfaces that are not yet fully supported by alsa.

```
# ~/.config/pipewire/pipewire.conf.d/my-loopback-2.conf

context.modules = [
{   name = libpipewire-module-loopback
    args = {
        node.description = "Scarlett Focusrite Line 1"
        capture.props = {
            audio.position = [ FL ]
            stream.dont-remix = true
            node.target = "alsa_input.usb-Focusrite_Scarlett_Solo_USB_Y7ZD17C24495BC-00.analog-stereo"
            node.passive = true
        }
        playback.props = {
            node.name = "SF_mono_in_1"
            media.class = "Audio/Source"
            audio.position = [ MONO ]
        }
    }
}
]
```

## Example configuration of an upmix sink

This Virtual sink has 2 input channels and 6 output channels. It will perform upmixing
using the PSD algorithm on the playback stream.

```
# ~/.config/pipewire/pipewire.conf.d/my-loopback-3.conf

context.modules = [
{   name = libpipewire-module-loopback
    args = {
        node.description = "Upmix Sink"
        audio.position = [ FL FR ]
        capture.props = {
            node.name = "effect_input.upmix"
            media.class = Audio/Sink
        }
        playback.props = {
            node.name = "effect_output.upmix"
            audio.position = [ FL FR RL RR FC LFE ]
            node.passive = true
            stream.dont-remix = true
            channelmix.upmix = true
            channelmix.upmix-method = psd
            channelmix.lfe-cutoff = 150
            channelmix.fc-cutoff = 12000
            channelmix.rear-delay = 12.0
        }
    }
}
]
```

## Example configuration of a downmix source

This Virtual source has 2 input channels and a mono output channel. It will perform
downmixing from the two first AUX channels of a pro-audio device.

```
# ~/.config/pipewire/pipewire.conf.d/my-loopback-4.conf

context.modules = [
{   name = libpipewire-module-loopback
    args = {
        node.description = "Downmix Source"
        audio.position = [ AUX0 AUX1 ]
        capture.props = {
            node.name = "effect_input.downmix"
            target.object = "alsa_input.usb-BEHRINGER_UMC404HD_192k-00.pro-input-0"
            node.passive = true
            stream.dont-remix = true
        }
        playback.props = {
            node.name = "effect_output.downmix"
            media.class = Audio/Source
            audio.position = [ MONO ]
        }
    }
}
]
```

## See also

`pw-loopback` : a tool that loads the loopback module with given parameters.
