# pw-audioconvert

The PipeWire audioconvert utility

# SYNOPSIS

*pw-audioconvert** \[*OPTIONS*\] *INFILE* *OUTFILE*

# DESCRIPTION

Use the PipeWire audioconvert to convert input file to output file,
following the given options.

This is useful only for doing audio conversion but also apply effects
on the audio using a filter-graph.

It understands all audio file formats supported by `libsndfile` for input
and output. The filename extension is used to guess the output file
container and format with the WAV file format as the default.

# OPTIONS

 -r RATE | \--rate=RATE
Output sample rate. Default the same as the input sample rate.

 -f FORMAT | \--format=FORMAT
Output sample format (s8 | s16 | s32 | f32 | f64). Default the same
as the input format.

 -b BLOCKSIZE | \--blocksize=BLOCKSIZE
Number of samples per iteration (default 4096)

 -P PROPERTIES | \--properties=PROPERTIES
Set extra stream properties as a JSON object. One can also use @filename to
read the JSON object with properties from filename.

 -c CHANNELS | \--channels=CHANNELS
The number of output channels, default the same as the input.

 \--channel-map=VALUE
The channelmap. Possible values include are either a predefined channel layout
such as **Mono**, **Stereo**, **2.1**, **Quad**, **2.2**, **5.1**,
or comma separated array of channel names such as **FL,FR**.

 -h
Show help.

 -v
Verbose operation.

# EXAMPLES

*pw-audioconvert** -r 48000 -f s32 in.wav out.wav

# AUTHORS

The PipeWire Developers <$(PACKAGE_BUGREPORT)>;
PipeWire is available from <$(PACKAGE_URL)>

# SEE ALSO

pipewire(1)
