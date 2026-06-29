# Filter-Chain

The filter-chain allows you to create an arbitrary processing graph
from LADSPA, LV2, sofa, ffmpeg and builtin filters. This filter can be
made into a virtual sink/source or between any 2 nodes in the graph.

The filter chain is built with 2 streams, a capture stream providing
the input to the filter chain and a playback stream sending out the
filtered stream to the next nodes in the graph.

Because both ends of the filter-chain are built with streams, the session
manager can manage the configuration and connection with the sinks and
sources automatically.

## Module Name

`libpipewire-module-filter-chain`

## Module Options

- `node.description`: a human readable name for the filter chain
- `filter.graph = []`: a description of the filter graph to run, see below
- `capture.props = {}`: properties to be passed to the input stream
- `playback.props = {}`: properties to be passed to the output stream

## Filter graph description

The general structure of the graph description is as follows:

```
    filter.graph = {
        nodes = [
            {
                type = <ladspa | lv2 | builtin | sofa>
                name = <name>
                plugin = <plugin>
                label = <label>
                config = {
                    <configkey> = <value> ...
                }
                control = {
                    <controlname|controlindex> = <value> ...
                }
            }
            ...
        ]
        links = [
            { output = <portname> input = <portname> }
            ...
        ]
        inputs = [ <portname> ... ]
        outputs = [ <portname> ... ]
        capture.volumes = [
            { control = <portname>  min = <value>  max = <value>  scale = <scale> } ...
        ]
        playback.volumes = [
            { control = <portname>  min = <value>  max = <value>  scale = <scale> } ...
        ]
   }
```

### Nodes

Nodes describe the processing filters in the graph. Use a tool like lv2ls
or listplugins to get a list of available plugins, labels and the port names.

- `type` is one of `ladspa`, `lv2`, `builtin`, `sofa`, `ebur128` of `ffmpeg`.
- `name` is the name for this node, you might need this later to refer to this node
   and its ports when setting controls or making links.
- `plugin` is the type specific plugin name.
   - For LADSPA plugins it will append `.so` to find the shared object with that
      name in the LADSPA plugin path ($LADSPA_PATH). If the plugin is an absolute
      path and is inside $LADSPA_PATH, it will be used directly without appending
      `.so`. Note that this makes it impossible to load plugins from outside of the
      $LADSPA_PATH for security reasons.
   - For LV2, this is the plugin URI obtained with lv2ls.
   - For builtin, sofa and ebur128 this is ignored
   - For ffmpeg this should be filtergraph
- `label` is the type specific filter inside the plugin.
   - For LADSPA this is the label
   - For LV2 this is unused
   - For builtin, sofa and ebur128 this is the name of the filter to use
   - For ffmpeg this is an FFMpeg filtergraph description

- `config` contains a filter specific configuration section. Some plugins need
           this. (convolver, sofa, delay, ...)
   - For lv2, the config can contain a set of state key/value pairs. If the lv2
     plugin supports the LV2_STATE__interface, these values will be provided for
     the given keys.
- `control` contains the initial values for the control ports of the filter.
           normally these are given with the port name but it is also possible
           to give the control index as the key.

Some examples ladspa and lv2 plugins:

```
filter.graph = {
    nodes = [
        {
            # an example ladspa plugin
            type = ladspa
            name = pitch
            plugin = "ladspa-rubberband"
            label = "rubberband-r3-pitchshifter-mono"
            control = {
                # controls are using the ladspa port names as seen in analyseplugin
                "Semitones" = -3
            }
        }
        {
            # an example lv2 plugin
            type = lv2
            name = pitch
            plugin = "http://breakfastquay.com/rdf/lv2-rubberband#mono"
            control = {
                # controls are using the lv2 symbol as seen with lv2info
                "semitones" = -3
            }
        }
        {
            # an example lv2 plugin with a state
            type = lv2
            name = neural
            plugin = "http://aidadsp.cc/plugins/aidadsp-bundle/rt-neural-generic"
            control = {
                # use the port symbols as seen with lv2info
                PRESENCE = 1.0
            }
            config = {
                # the config contains state keys and values
                "http://aidadsp.cc/plugins/aidadsp-bundle/rt-neural-generic#json" =
                    "/usr/lib64/lv2/rt-neural-generic.lv2/models/deer ink studios/tw40_blues_solo_deerinkstudios.json"
            }
        }
    }
    ...
}
```

### Links

Links can be made between ports of nodes. The `portname` is given as
`<node_name>:<port_name>`.

You can tee the output of filters to multiple other filters. You need to
use a mixer if you want the output of multiple filters to go into one
filter input port.

links can be omitted when the graph has just 1 filter.

### Inputs and Outputs

These are the entry and exit ports into the graph definition. Their number
defines the number of channels used by the filter-chain.

The `<portname>` can be `null` when a channel is to be ignored.

Each input/output in the graph can only be linked to one filter input/output.
You need to use the copy builtin filter if the stream signal needs to be routed
to multiple filters. You need to use the mixer builtin plugin if multiple graph
outputs need to go to one output stream.

inputs and outputs can be omitted, in which case the filter-chain will use all
inputs from the first filter and all outputs from the last filter node. The
graph will then be duplicated as many times to match the number of input/output
channels of the streams.

If the graph has no inputs and the capture channels is set as 0, only the
playback stream will be created. Likewise, if there are no outputs and the
playback channels is 0, there will be no capture stream created.

### Volumes

Normally the volume of the sink/source is handled by the stream software volume.
With the capture.volumes and playback.volumes properties this can be handled
by a control port in the graph instead. Use capture.volumes for the volume of the
input of the filter (when for example used as a sink). Use playback,volumes for
the volume of the output of the filter (when for example used as a source).

The min and max values (defaults 0.0 and 1.0) respectively can be used to scale
and translate the volume min and max values.

Normally the control values are linear and it is assumed that the plugin does not
perform any scaling to the values. This can be changed with the scale property. By
default this is linear but it can be set to cubic when the control applies a
cubic transformation.

## Builtin filters

There are some useful builtin filters available. The type should be `builtin` and
you select the specific builtin filter with the `label` of the filter node.

### Mixer

Use the `mixer` plugin if you have multiple input signals that need to be mixed together.

The mixer plugin has up to 8 input ports labeled "In 1" to "In 8" and each with
a gain control labeled "Gain 1" to "Gain 8". There is an output port labeled
"Out". Unused input ports will be ignored and not cause overhead.

### Copy

Use the `copy` plugin if you need to copy a stream input signal to multiple filters.

It has one input port "In" and one output port "Out".

### Biquads

Biquads can be used to do all kinds of filtering. They are also used when creating
equalizers.

All biquad filters have an input port "In" and an output port "Out". They have
a "Freq", "Q" and "Gain" control. Their meaning depends on the particular biquad that
is used. The biquads also have "b0", "b1", "b2", "a0", "a1" and "a2" ports that
are read-only except for the bq_raw biquad, which can configure default values
depending on the graph rate and change those at runtime.

We refer to https://arachnoid.com/BiQuadDesigner/index.html for an explanation of
the controls.

The following labels can be used:

- `bq_lowpass` a lowpass filter.
- `bq_highpass` a highpass filter.
- `bq_bandpass` a bandpass filter.
- `bq_lowshelf` a low shelf filter.
- `bq_highshelf` a high shelf filter.
- `bq_peaking` a peaking filter.
- `bq_notch` a notch filter.
- `bq_allpass` an allpass filter.
- `bq_raw` a raw biquad filter. You need a config section to specify coefficients
		per sample rate. The coefficients of the sample rate closest to the
		graph rate are selected:

```
filter.graph = {
    nodes = [
        {
            type   = builtin
            name   = ...
            label  = bq_raw
            config = {
                coefficients = [
                    { rate =  44100, b0=.., b1=.., b2=.., a0=.., a1=.., a2=.. },
                    { rate =  48000, b0=.., b1=.., b2=.., a0=.., a1=.., a2=.. },
                    { rate = 192000, b0=.., b1=.., b2=.., a0=.., a1=.., a2=.. }
                ]
            }
            ...
        }
    }
    ...
}
```

### Parametric EQ

The parametric EQ chains a number of biquads together. It is more efficient than
specifying a number of chained biquads and it can also load configuration from a
file.

The parametric EQ supports multichannel processing and has 8 input and 8 output ports
that don't all need to be connected. The ports are named `In 1` to `In 8` and
`Out 1` to `Out 8`.

```
filter.graph = {
    nodes = [
        {
            type   = builtin
            name   = ...
            label  = param_eq
            config = {
                filename = "..."
                #filename1 = "...", filename2 = "...", ...
                filters = [
                    { type = ..., freq = ..., gain = ..., q = ... },
                    { type = ..., freq = ..., gain = ..., q = ... },
                    ....
                ]
                #filters1 = [ ... ], filters2 = [ ... ], ...
            }
            ...
        }
    }
    ...
}
```

Either a `filename` or a `filters` array can be specified. The configuration
will be used for all channels. Alternatively `filenameX` or `filtersX` where
X is the channel number (between 1 and 8) can be used to load a channel
specific configuration.

The `filename` must point to a parametric equalizer configuration
generated from the AutoEQ project or Squiglink. Both the projects allow
equalizing headphones or an in-ear monitor to a target curve.

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

The `filters` (or channel specific `filtersX` where X is the channel between 1 and
8) can contain an array of filter specification object with the following keys:

  `type` specifies the filter type, choose one from the available biquad labels.
  `freq` is the frequency passed to the biquad.
  `gain` is the gain passed to the biquad.
  `q` is the Q passed to the biquad.

This makes it possible to also use the param eq without a file and with all the
available biquads.

### Convolver

The convolver can be used to apply an impulse response to a signal. It is usually used
for reverbs or virtual surround. The convolver is implemented with a fast FFT
implementation.

The convolver has an input port "In" and an output port "Out". It requires a config
section in the node declaration in this format:

When multiple impulses are applied to one input, use the convolver2, which is more
performant.

Check the documentation for Convolver2 for the parameter meanings.

```
filter.graph = {
    nodes = [
        {
            type   = builtin
            name   = ...
            label  = convolver
            config = {
                blocksize = ...
                tailsize = ...
                gain = ...
                delay = ...
                filename = ...
                offset = ...
                length = ...
                channel = ...
                resample_quality = ...
                latency = ...
            }
            ...
        }
    }
    ...
}

### Convolver2

The convolver2 can be used to apply one or more impulse responses to a signal.
It is usually used for reverbs or virtual surround. The convolver2 is implemented
with a fast FFT implementation.

The convolver2 has an input port "In" and 8 output ports "Out 1" to "Out 8". It
requires a config section in the node declaration in this format:

```
filter.graph = {
    nodes = [
        {
            type   = builtin
            name   = ...
            label  = convolver2
            config = {
                blocksize = ...
                tailsize = ...
                impulses = [
                    {
                        gain = ...
                        delay = ...
                        filename = ...
                        offset = ...
                        length = ...
                        channel = ...
                        resample_quality = ...
                    }
                    ...
                ]
                latency = ...
            }
            ...
        }

```

- `blocksize` specifies the size of the blocks to use in the FFT. It is a value
              between 64 and 256. When not specified, this value is
              computed automatically from the number of samples in the file.
- `tailsize` specifies the size of the tail blocks to use in the FFT.
- `impulses`  An array of objects with the IRs for the outputs "Out 1" to "Out 8".
- `gain`     the overall gain to apply to the IR file. Default 1.0
- `delay`    The extra delay to add to the IR. A float number will be interpreted as seconds,
             and integer as samples. Using the delay in seconds is independent of the graph
             and IR rate and is recommended. Default 0
- `filename` The IR to load or create. Possible values are:
    - `/hilbert` creates a [hilbert function](https://en.wikipedia.org/wiki/Hilbert_transform)
               that can be used to phase shift the signal by +/-90 degrees. The
               `length` will be used as the number of coefficients. The default latency
               if the length/2.
    - `/dirac` creates a [Dirac function](https://en.wikipedia.org/wiki/Dirac_delta_function) that
                can be used as gain. The default latency is 0.
    - A filename to load as the IR. This needs to be a file format supported
              by sndfile or be an inline IR with "/ir:<rate>,<value1>,<value2>". The default
              latency of file IRs is 0.
    - [ filename, ... ] an array of filenames. The file with the closest samplerate match
              with the graph samplerate will be used.
- `offset`  The sample offset in the file as the start of the IR.
- `length`  The number of samples to use as the IR.
- `channel` The channel to use from the file as the IR.
- `resample_quality` The resample quality in case the IR does not match the graph
                     samplerate.
- `latency`  The extra latency in seconds to report. When left unspecified (or < 0.0)
             the default IR latency will be used, depending on the filename argument.

### Delay

The delay can be used to delay a signal in time. With the Feedback and Feedforward
controls it can also be used as a comb and an allpass filter.

The delay has an input port "In" and an output port "Out". It also has
a "Delay (s)" control port and a "Feedback" and "Feedforward" port. It requires a
config section in the node declaration in this format:

```
filter.graph = {
    nodes = [
        {
            type   = builtin
            name   = ...
            label  = delay
            config = {
                "max-delay" = ...
                "latency" = ...
            }
            control = {
                "Delay (s)" = ...
                "Feedback" = ...
                "Feedforward" = ...
            }
            ...
        }
    }
    ...
}
```

- `max-delay` the maximum delay in seconds. The "Delay (s)" parameter will
             be clamped to this value.
- `latency` the latency in seconds. This is 0 by default but in some cases
            the delay can be used to introduce latency with this option.

With the "Feedback" port one can create a comb filter. With the "Feedback"
port and "Feedforward" port set to A and -A respectively, one can create
an allpass filter. These settings can be used to create custom reverb units.

### Invert

The invert plugin can be used to invert the phase of the signal.

It has an input port "In" and an output port "Out".

### Clamp

The clamp plugin can be used to clamp samples between min and max values.

It has an input port "In" and an output port "Out". It also has a "Control"
and "Notify" port for the control values.

The final result is clamped to the "Min" and "Max" control values.

### Linear

The linear plugin can be used to apply a linear transformation on samples
or control values.

It has an input port "In" and an output port "Out". It also has a "Control"
and "Notify" port for the control values.

The control value "Mult" and "Add" are used to configure the linear transform. Each
sample or control value will be calculated as: new = old * Mult + Add.

### Reciprocal

The recip plugin can be used to calculate the reciprocal (1/x) of samples
or control values.

It has an input port "In" and an output port "Out". It also has a "Control"
and "Notify" port for the control values.

### Abs

The abs plugin can be used to calculate the absolute value of samples.

It has an input port "In" and an output port "Out".

### Sqrt

The sqrt plugin can be used to calculate the square root of samples.

It has an input port "In" and an output port "Out".

### Exp

The exp plugin can be used to calculate the exponential (base^x) of samples
or control values.

It has an input port "In" and an output port "Out". It also has a "Control"
and "Notify" port for the control values.

The control value "Base" is used to calculate base ^ x for each sample.

### Log

The log plugin can be used to calculate the logarithm of samples
or control values.

It has an input port "In" and an output port "Out". It also has a "Control"
and "Notify" port for the control values.

The control value "Base", "M1" and "M2" are used to calculate
out = M2 * log2f(fabsf(in * M1)) / log2f(Base) for each sample.

### Multiply

The mult plugin can be used to multiply samples together.

It has 8 input ports named "In 1" to "In 8" and an output port "Out".

All input ports samples are multiplied together into the output. Unused input ports
will be ignored and not cause overhead.

### Sine

The sine plugin generates a sine wave.

It has an output port "Out" and also a control output port "notify".

"Freq", "Ampl", "Offset" and "Phase" can be used to control the sine wave
frequency, amplitude, offset and phase.

### Max

Use the `max` plugin if you need to select the max value of a number of input ports.

It has 8 input ports named "In 1" to "In 8" and one output port "Out".

All input ports samples are checked to find the maximum value per sample. Unused
input ports will be ignored and not cause overhead.

### Min

Use the `min` plugin if you need to select the minimum value of a number of input ports.

It has 8 input ports named "In 1" to "In 8" and one output port "Out".

All input ports samples are checked to find the minimum value per sample. Unused
input ports will be ignored and not cause overhead.

### dcblock

Use the `dcblock` plugin implements a [DC blocker](https://www.dsprelated.com/freebooks/filters/DC_Blocker.html).

It has 8 input ports "In 1" to "In 8" and corresponding output ports "Out 1"
to "Out 8". Not all ports need to be connected.

It also has 1 control input port "R" that controls the DC block R factor.

### Ramp

Use the `ramp` plugin creates a linear ramp from `Start` to `Stop`.

It has 3 input control ports "Start", "Stop" and "Duration (s)". It also has one
output port "Out". A linear ramp will be created from "Start" to "Stop" for a duration
given by the "Duration (s)" control in (fractional) seconds. The current value will
be stored in the output notify port "Current".

The ramp output can, for example, be used as input for the `mult` plugin to create
a volume ramp up or down. For more a more coarse volume ramp, the "Current" value
can be used in the `linear` plugin.

### Debug

The `debug` plugin can be used to debug the audio and control data of other plugins.

It has an "In" input port and an "Out" output data ports. The data from "In" will
be copied to "Out" and the data will be dumped into the INFO log.

There is also a "Control" input port and an "Notify" output control ports. The
control from "Control" will be copied to "Notify" and the control value will be
dumped into the INFO log.

### Zeroramp

The `zeroramp` plugin can be used to detect unnatural silence parts in the audio
stream and ramp the volume down or up when entering or leaving the silent area
respectively.
This can be used to avoid loud pops and clicks that occur when the sample values
suddenly drop to zero or jump from zero to a large value caused by a pause,
resume or an error of the stream. It only detect areas where the sample values
are absolute zero values, such as those inserted when pausing a stream.

It has an "In" input port and an "Out" output data ports.

There are also "Gap (s)" and an "Duration (s)" input control ports. "Gap (s)"
determines how long the silence gap is in seconds (default 0.000666) and
"Duration (s)" determines how long the fade-in and fade-out should last
(default 0.000666).

### Noisegate

The `noisegate` plugin can be used to remove low volume noise.

It has an "In" input port and an "Out" output data ports. Normally the input
data is passed directly to the output.

The "Level" control port can be used to control the measured volume of the "In"
port. When not connected, a simple volume algorithm on the "In" port will be
used.

If the volume drops below "Close threshold", the noisegate will ramp down the
volume to zero for a duration of "Release (s)" seconds. When the volume is above
"Open threshold", the noisegate will ramp up the volume to 1 for a duration
of "Attack (s)" seconds. The noise gate stays open for at least "Hold (s)"
seconds before it can close again.

### Busy

The `busy` plugin has no input or output ports and it can be used to keep the
CPU or graph busy for the given percent of time.

The node requires a `config` section with extra configuration:

```
filter.graph = {
    nodes = [
        {
            type   = builtin
            name   = ...
            label  = busy
            config = {
                wait-percent = 0.0
                cpu-percent = 50.0
            }
            ...
        }
    }
    ...
}
```

- `wait-percent` the percentage of time to wait. This keeps the graph busy but
                 not the CPU. Default 0.0
- `cpu-percent` the percentage of time to keep the CPU busy. This keeps both the
                 graph and CPU busy. Default 0.0

### Null

The `null` plugin has one data input "In" and one control input "Control" that
simply discards the data.

## SOFA filters

There is an optional `sofa` type available (when compiled with `libmysofa`).

### Spatializer

The spatializer can be used to place the sound in a 3D space.

The spatializer has an input port "In" and a stereo pair of output ports
called "Out L" and "Out R". It requires a config section in the node
declaration in this format:

The control can be changed at runtime to move the sounds around in the
3D space.

```
filter.graph = {
    nodes = [
        {
            type   = sofa
            name   = ...
            label  = spatializer
            config = {
                blocksize = ...
                tailsize = ...
                filename = ...
                gain = ...
                latency = ...
            }
            control = {
                "Azimuth" = ...
                "Elevation" = ...
                "Radius" = ...
            }
            ...
        }
    }
    ...
}
```

- `blocksize` specifies the size of the blocks to use in the FFT. It is a value
              between 64 and 256. When not specified, this value is
              computed automatically from the number of samples in the file.
- `tailsize`  specifies the size of the tail blocks to use in the FFT.
- `filename`  The SOFA file to load. SOFA files usually end in the .sofa extension
              and contain the HRTF for the various spatial positions.
- `gain`      the overall gain to apply to the IR file, default 1.0.
- `latency`   the latency introduced by the filter, default 0

- `Azimuth`   controls the azimuth, this is the direction the sound is coming from
              in degrees between 0 and 360. 0 is straight ahead. 90 is left, 180
              behind, 270 right.
- `Elevation` controls the elevation, this is how high/low the signal is in degrees
              between -90 and 90. 0 is straight in front, 90 is directly above
              and -90 directly below.
- `Radius`    controls how far away the signal is as a value between 0 and 100.
              default is 1.0.

## EBUR128 filters

There is an optional EBU R128 plugin available (when compiled with
`libebur128`) selected with the `ebur128` type. Filters in the plugin
can be selected with the `label` field.

### ebur128

The ebur128 filter can be used to measure the loudness of a signal.

It has 7 input ports "In FL", "In FR", "In FC", "In UNUSED", "In SL", "In SR"
and "In DUAL MONO", corresponding to the different input channels for EBUR128.
Not all ports need to be connected for this filter.

The input signal is passed unmodified on the "Out FL", "Out FR", "Out FC",
"Out UNUSED", "Out SL", "Out SR" and "Out DUAL MONO" output ports.

There are 7 output control ports that contain the measured loudness information
and that can be used to control the processing of the audio. Some of these ports
contain values in LUFS, or "Loudness Units relative to Full Scale". These are
negative values, closer to 0 is louder. You can use the lufs2gain plugin to
convert this value to a gain to adjust a volume (See below).

"Momentary LUFS" contains the momentary loudness measurement with a 400ms window
                 and 75% overlap. It works mostly like an R.M.S. meter.

"Shortterm LUFS" contains the shortterm loudness in LUFS over a 3 second window.

"Global LUFS" contains the global integrated loudness in LUFS over the max-history
              window.
"Window LUFS" contains the global integrated loudness in LUFS over the max-window
              window.

"Range LU" contains the loudness range (LRA) in LU units.

"Peak" contains the peak loudness.

"True Peak" contains the true peak loudness oversampling the signal. This can more
            accurately reflect the peak compared to "Peak".

The node also has an optional `config` section with extra configuration:

```
filter.graph = {
    nodes = [
        {
            type   = ebur128
            name   = ...
            label  = ebur128
            config = {
                max-history = ...
                max-window = ...
                use-histogram = ...
            }
            ...
        }
    }
    ...
}
```

- `max-history` the maximum history to keep in (float) seconds. Default to 10.0

- `max-window` the maximum window to keep in (float) seconds. Default to 0.0
               You will need to set this to some value to get "Window LUFS"
               output control values.

- `use-histogram` uses the histogram algorithm to calculate loudness. Defaults
                  to false.

### lufs2gain

The lufs2gain filter can be used to convert LUFS control values to gain. It needs
a target LUFS control input to drive the conversion.

It has 2 input control ports "LUFS" and "Target LUFS" and will produce 1 output
control value "Gain". This gain can be used as input for the builtin `linear`
filter, for example, to adust the gain.

## FFmpeg

There is an optional FFmpeg filter available (when compiled with `libavfilter`)
that can be selected with the `ffmpeg` type. Use the `plugin` field to select
the plugin to use.

### Filtergraph

The filtergraph FFmpeg plugin is selected with the `filtergraph` plugin
field in the node.

The filtergraph filter allows you to specify an set of audio filters using
the FFmpeg filtergraph syntax (https://ffmpeg.org/ffmpeg-filters.html).

The `label` field should be used to describe the filtergraph in use.

FFmpeg filtergraph input and output ports can have multiple channels. The
filter-chain can split those into individual ports to use as input and output
ports. For this, the ports in the filtergraph need to have a specific name
convention, either `<port-name>_<channel-name>` or `<port-name>_<channel-layout>`.

When a single channel is specified, the port can be referenced in inputs and
outputs sections with `<name>:<port-name>_<channel-name>`. When a channel-layout
is specified, each port name gets a `_<number>` appended, starting from 0 and
counting up for each channel in the layout.

The `filtergraph` plugin will automatically add format converters when the input
port channel-layout, format or graph sample-rates don't match.

Note that the FFmpeg filtergraph is not Real-time safe because it might do
allocations from the processing thread. It is advised to run the filter-chain
streams in async mode (`node.async = true`) to avoid interrupting the other
RT threads.

Some examples:

The stereo ports are split into their channels with the `_0` and `_1` suffixes.

```
filter.graph = {
    nodes = [
        {
            type   = ffmpeg
            plugin = filtergraph
            name   = filter
            label = "[in_stereo]loudnorm=I=-18:TP=-3:LRA=4[out_stereo]"
        }
    }
    inputs = [ "filter:in_stereo_0" "filter:in_stereo_1" ]
    outputs = [ "filter:out_stereo_0" "filter:out_stereo_1" ]
    ...
}
```

It is possible to have multiple input and output ports for the filtergraphs.
In the next example, the ports have a single channel name and so don't have
the `_0` suffix to identify them. This can be simplified by removing the `amerge`
and `channelsplit` filters and using the `_stereo` suffix on port names to let
PipeWire do the splitting and merging more efficiently.

```
filter.graph = {
    nodes = [
        {
            type   = ffmpeg
            plugin = filtergraph
            name   = filter
            label = "[in_FL][in_FR]amerge,extrastereo,channelsplit[out_FL][out_FR]"
        }
    }
    inputs = [ "filter:in_FL" "filter:in_FR" ]
    outputs = [ "filter:out_FL" "filter:out_FR" ]
    ...
}
```

Here is a last example of a surround sound upmixer:

```
filter.graph = {
    nodes = [
        {
            type   = ffmpeg
            plugin = filtergraph
            name   = filter
            label = "[in_stereo]surround[out_5.1]"
        }
    }
    inputs = [ "filter:in_FL" "filter:in_FR" ]
    outputs = [ "filter:out_5.1_0" "filter:out_5.1_1" "filter:out_5.1_2"
                "filter:out_5.1_3" "filter:out_5.1_4" "filter:out_5.1_5" ]
    ...
}
```

## ONNX filters

There is an optional ONNX filter available (when compiled with `libonnxruntime`)
that can be selected with the `onnx` type. Use the `label` field to select
the model to use and how to map the tensors to ports.

```
filter.graph = {
    nodes = [
        {
            type   = onnx
            name   = onnx
            label = {
                filename = "..."
                blocksize = 512
                input-tensors = {
                    "<name>" = {
                        dimensions = [ ... ]
                        #retain = 64
                        data = "port:..."|"tensor:..."|"param:..."|"control:..."
                    }
                    ...
                }
                output-tensors = {
                    "<name>" = {
                        dimensions = [ ... ]
                        #retain = 64
                        data = "port:..."|"tensor:..."|"param:..."|"control:..."
                    }
                    ...
                }
            }
        }
    }
    ...
}
```

The label must contain an object with the configuration of the plugin.

- `filename` the ONNX model to load. It must point to an existing onnx file.
- `blocksize` the number of samples to give to the model. This depends on the model
              and the input/output tensor sizes.
- `input-tensors` an object of input tensors of the model and how they should be
                  used. Unlisted tensors will not be used.
- `output-tensors` an object of output tensors of the model and how they should be
                  used. Unlisted tensors will not be used.

The `input-tensors` and `output-tensors` configuration must contain an object with
keys named after the tensors in the model and the value must be an object with the
the following keys:

- `dimensions` and array of dimensions of the tensors.
- `retain` an optional key for input tensors. This will prepend the last `retain` samples
           from the previous block to the input tensor. The size of the tensor should
           therefore at least be blocksize + retain samples large.
- `data` where the data for the tensor is comming from. There are different options
         based on the value of this file, selected with a prefix:
     - `port:<portname>` a new input/output port is created on the plugin with the
                         name <portname> and the data for the tensor will be obtained
                         or copied from/to the port data.
     - `tensor:<tensorname>` the data of this tensor is copied from the given
                             <tensorname>. You can use this to copy output state
                             info to the input state, for example.
     - `param:<paramname>` the data of this tensor is obtained from a parameter with
                           <paramname>. Currently only `rate` is a valid paramname,
                           which has the value of the filter samplerate.
     - `control:<portname>` a new input/output control port is created and the tensor
                            data will be obtained/copied from/to the control data.

Here is an example of the silero VAD model:

```
filter.graph = {
    nodes = [
        {
            type   = onnx
            name = onnx
            label = {
                filename = "/home/wim/src/silero-vad/src/silero_vad/data/silero_vad.onnx"
                blocksize = 512
                input-tensors = {
                    "input" = {
                        dimensions = [ 1, 576 ]
                        retain = 64
                        data = "port:input"
                    }
                    "state" = {
                        dimensions = [ 2, 1, 128 ]
                        data = "tensor:stateN"
                    }
                    "sr" = {
                        dimensions = [ 1 ]
                        data = "param:rate"
                    }
                }
                output-tensors = {
                    "output" = {
                        dimensions = [ 1, 1 ]
                        data = "control:speech"
                    }
                    "stateN" = {
                        dimensions = [ 2, 1, 128 ]
                    }
                }
            }
        }
        ...
   ]
   ....
}
```

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
	'filter-chain-PID-MODULEID'.

Stream only properties:

- PW_KEY_MEDIA_CLASS
- PW_KEY_NODE_NAME :  if not given per stream, the global node.name will be
        prefixed with 'input.' and 'output.' to generate a capture and playback
        stream node.name respectively.

## Example configuration of a virtual source

This example uses the rnnoise LADSPA plugin to create a new
virtual source.

Run with `pipewire -c filter-chain.conf`. The configuration can also
be put under `pipewire.conf.d/` to run it inside the PipeWire server.

```
# ~/.config/pipewire/filter-chain.conf.d/my-filter-chain-1.conf

context.modules = [
{   name = libpipewire-module-filter-chain
    args = {
        node.description =  "Noise Canceling source"
        media.name =  "Noise Canceling source"
        filter.graph = {
            nodes = [
                {
                    type = ladspa
                    name = rnnoise
                    plugin = ladspa/librnnoise_ladspa
                    label = noise_suppressor_stereo
                    control = {
                        "VAD Threshold (%)" 50.0
                    }
                }
            ]
        }
        capture.props = {
            node.name =  "capture.rnnoise_source"
            node.passive = true
        }
        playback.props = {
            node.name =  "rnnoise_source"
            media.class = Audio/Source
        }
    }
}
]
```

## Example configuration of a Dolby Surround encoder virtual Sink

This example uses the ladpsa surround encoder to encode a 5.1 signal
to a stereo Dolby Surround signal.

```
# ~/.config/pipewire/filter-chain.conf.d/my-filter-chain-2.conf

context.modules = [
{   name = libpipewire-module-filter-chain
    args = {
        node.description = "Dolby Surround Sink"
        media.name       = "Dolby Surround Sink"
        filter.graph = {
            nodes = [
                {
                    type  = builtin
                    name  = mixer
                    label = mixer
                    control = { "Gain 1" = 0.5 "Gain 2" = 0.5 }
                }
                {
                    type   = ladspa
                    name   = enc
                    plugin = surround_encoder_1401
                    label  = surroundEncoder
                }
            ]
            links = [
                { output = "mixer:Out" input = "enc:S" }
            ]
            inputs  = [ "enc:L" "enc:R" "enc:C" null "mixer:In 1" "mixer:In 2" ]
            outputs = [ "enc:Lt" "enc:Rt" ]
        }
        capture.props = {
            node.name      = "effect_input.dolby_surround"
            media.class    = Audio/Sink
            audio.channels = 6
            audio.position = [ FL FR FC LFE SL SR ]
        }
        playback.props = {
            node.name      = "effect_output.dolby_surround"
            node.passive   = true
            audio.channels = 2
            audio.position = [ FL FR ]
        }
    }
}
]
```
