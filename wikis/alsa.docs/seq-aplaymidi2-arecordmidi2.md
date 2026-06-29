# NAME

arecordmidi2 - record a MIDI Clip file

# SYNOPSIS

**arecordmidi2** \[options\] midi2file

# DESCRIPTION

**arecordmidi2** is a command-line utility that records a MIDI Clip file from one or more ALSA sequencer ports.

To stop recording, press Ctrl+C.

When **-** is passed to the MIDI Clip file argument, it's recorded to stdout. It implies *-s* option, too.

# OPTIONS

*-h,--help*
Prints a list of options.


*-V,--version*
Prints the current version.


*-p,--port=client:port,...*
Sets the sequencer port(s) from which events are recorded.

A client can be specified by its number, its name, or a prefix of its name. A port is specified by its number; for port 0 of a client, the ":0" part of the port specification can be omitted.

**arecordmidi2** creates a UMP Endpoint containing the same number of Function Blocks as specified by this option, each of which is connected to the specified port as a source.

When no source ports are specified with *-p* option, **arecordmidi2** creates a UMP Endpoint with full 16 Function Blocks and records from those inputs. User can connect the sequencer ports freely via **aconnect**, for example. This mode can be used together with the interactive mode via *-r* option.


*-b,--bpm=beats*
Sets the musical tempo of the MIDI file, in beats per minute. The default value is 120 BPM.


*-t,--ticks=ticks*
Sets the resolution of timestamps (ticks) in the MIDI file, in ticks per beat. The default value is 384 ticks/beat.


*-i,--timesig=numerator:denominator*
Sets the time signature for the MIDI file.

The time signature is specified as usual with two numbers, representing the numerator and denominator of the time signature as it would be notated. The denominator must be a power of two. Both numbers should be separated by a colon. The time signature is 4:4 by default.


*-n,--num-events=events*
Stops the recording after receiving the given number of events.


*-u,--ump=version*
Sets the UMP MIDI protocol version. Either 1 or 2 has to be given for MIDI 1.0 and MIDI 2.0 protocol, respectively. Default is 1.


*-r,--interactive*
Run in the interactive mode. **arecordmidi2** waits for a RETURN key input from the terminal to start the recording. After starting, the recording ends when another RETURN key is input from the terminal. The received events before the start of recording are discarded.


*-s,--silent*
Don't print messages to stdout.


*-P,--profile=file*
Read the UMP data from the given file and put them into the configuration section of the recorded output. The file must contain only valid UMP data encoded in big-endian.


*--song=text, --clip=text, --copyright=text, --composer=text, --lyricist=text, --arranger=text, --publisher=text, --performer=text --accompany=text, --date=text, --location=text*
Put the given meta data text in the configuration section.

# SEE ALSO

arecordmidi(1)
aplaymidi2(1)

# AUTHOR

Takashi Iwai \<tiwai@suse.de\>
