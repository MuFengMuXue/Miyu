# NAME

aseqsend - send arbitrary messages to selected ALSA MIDI seqencer port

# SYNOPSIS

**aseqsend** -p client:port -s file-name
**aseqsend** -p client:port "hex encoded byte-string"

# DESCRIPTION

**aseqsend** is a command-line utility which allows one to send SysEx (system exclusive) data to ALSA MIDI sequencer port. It can also send any other MIDI commands. Messages to be sent can be given in the last argument as hex encoded byte string or can be read from raw binary file. When sending several SysEx messages at once there is a delay of 1ms after each message as default and can be set to different value with option -i.

A client can be specified by its number, its name, or a prefix of its name. A port is specified by its number; for port 0 of a client, the ":0" part of the port specification can be omitted.

**aseqsend** can send UMP packets as MIDI 2.0 device by specifying via -u option as well, while the default operation is the legacy MIDI 1.0 byte stream.

# OPTIONS

*-h, --help*
Prints a list of options.


*-V, --version*
Prints the current version.


*-l, --list*
Prints a list of possible output ports.


*-v, --verbose*
Prints number of bytes actually sent


*-p, --port=client:port*
Target port by number or name


*-s, --file=filename*
Send raw binary data from given file name


*-i, --interval=msec*
Interval between SysEx messages in milliseconds


*-u, --ump=version*
Specify the MIDI version. 0 for the legacy MIDI 1.0 (default), 1 for UMP MIDI 1.0 protocol and 2 for UMP MIDI 2.0 protocol.

When UMP MIDI 1.0 or MIDI 2.0 protocol is specified, **aseqsend** reads the input as raw UMP packets, 4 each byte in big endian.

# EXAMPLES

**aseqsend -p 128:0 "F0 41 10 00 00 64 12 18 00 21 06 59 41 59 4E F7"**

**aseqsend -p 128:0 -s I7BulkDump.syx**

# SEE ALSO

**aseqdump(1)**

# AUTHOR

Miroslav Kovac \<mixxoo@gmail.com\>
