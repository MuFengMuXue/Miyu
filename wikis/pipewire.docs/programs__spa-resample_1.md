# spa-resample

The PipeWire resampler debugging utility

# SYNOPSIS

*spa-resample** \[*OPTIONS*\] *INFILE* *OUTFILE*

# DESCRIPTION

Use the PipeWire resampler to resample input file to output file,
following the given options.

This is useful only for testing the resampler.

# OPTIONS

 -r RATE | \--rate=RATE
Output sample rate.

 -f FORMAT | \--format=FORMAT
Output sample format (s8 | s16 | s32 | f32 | f64).

 -q QUALITY | \--quality=QUALITY
Resampler output quality (0-14).

 -c FLAGS | \--cpuflags=FLAGS
See spa/support/cpu.h.

 -h
Show help.

 -v
Verbose operation.

# EXAMPLES

*spa-resample** -r 48000 -f s32 in.wav out.wav

# AUTHORS

The PipeWire Developers <$(PACKAGE_BUGREPORT)>;
PipeWire is available from <$(PACKAGE_URL)>

# SEE ALSO

pipewire(1)
