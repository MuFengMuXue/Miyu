# Parametric-Equalizer

The `parametric-equalizer` module loads parametric equalizer configuration
generated from the AutoEQ project or Squiglink. Both the projects allow
equalizing headphones or an in-ear monitor to a target curve. While these
generate a file for parametric equalization for a given target, but this
is not a format that can be directly given to filter chain module.

A popular example of the above being EQ'ing to the Harman target curve
or EQ'ing one headphone/IEM to another.

For AutoEQ, see https://github.com/jaakkopasanen/AutoEq.
For SquigLink, see https://squig.link/.

Parametric equalizer configuration generated from AutoEQ or Squiglink looks
like below.

```
Preamp: -6.8 dB
Filter 1: ON PK Fc 21 Hz Gain 6.7 dB Q 1.100
Filter 2: ON PK Fc 85 Hz Gain 6.9 dB Q 3.000
Filter 3: ON PK Fc 110 Hz Gain -2.6 dB Q 2.700
Filter 4: ON PK Fc 210 Hz Gain 5.9 dB Q 2.100
Filter 5: ON PK Fc 710 Hz Gain -1.0 dB Q 0.600
Filter 6: ON PK Fc 1600 Hz Gain 2.3 dB Q 2.700
```

Fc, Gain and Q specify the frequency, gain and Q factor respectively.
The fourth column can be one of PK, LSC or HSC specifying peaking, low
shelf and high shelf filter respectively. More often than not only peaking
filters are involved.

This module parses a configuration like above and loads the filter chain
module with the above configuration translated to filter chain arguments.

## Module Name

`libpipewire-module-parametric-equalizer`

## Module Options

Options specific to the behaviour of this module

- `equalizer.filepath = <str>` path of the file with parametric EQ
- `equalizer.description = <str>`: Name which will show up in
- `audio.channels = <int>`: Number of audio channels, default 2
- `audio.position = <str>`: Channel map, default "[FL, FR]"
- `remote.name = <str>`: environment with remote name, default "pipewire-0"
- `capture.props = {}`: properties passed to the input stream, default `{ media.class = "Audio/Sink", node.name = "effect_input.eq<number of nodes>" }`
- `playback.props = {}`: properties passed to the output stream, default `{ node.passive = true, node.name = "effect_output.eq<number of nodes>" }`

## General options

Options with well-known behaviour:

- PW_KEY_AUDIO_CHANNELS
- SPA_KEY_AUDIO_LAYOUT
- SPA_KEY_AUDIO_POSITION
- PW_KEY_REMOTE_NAME

## Example configuration
```
# ~/.config/pipewire/pipewire.conf.d/my-parametric-equalizer.conf

context.modules = [
{   name = libpipewire-module-parametric-equalizer
    args = {
        #remote.name = "pipewire-0"
        #equalizer.filepath = "/a/b/EQ.txt"
        #equalizer.description = "Parametric EQ Sink"
        #audio.channels = 2
        #audio.position = [FL, FR]
        #capture.props = {
        #  node.name = "Parametric EQ input"
        #}
        #playback.props = {
        #  node.name = "Parametric EQ output"
        #}
    }
}
]
```

 1.0.6
