# pipewire-pulse

The PipeWire PulseAudio replacement

# SYNOPSIS

*pipewire-pulse** \[*options*\]

# DESCRIPTION

*pipewire-pulse** starts a PulseAudio-compatible daemon that integrates
with the PipeWire media server, by running a pipewire process through a
systemd service. This daemon is a drop-in replacement for the PulseAudio
daemon.

# OPTIONS

 -h | \--help
Show help.

 -v | \--verbose
Increase the verbosity by one level. This option may be specified
multiple times.

 \--version
Show version information.

 -c | \--config=FILE
Load the given config file (Default: pipewire-pulse.conf).

# ENVIRONMENT VARIABLES

The generic pipewire(1) environment variables
are supported.

In addition:

@PAR@ pulse-env  PULSE_RUNTIME_PATH

@PAR@ pulse-env  XDG_RUNTIME_DIR
Directory where to create the native protocol pulseaudio socket.

@PAR@ pulse-env  PULSE_LATENCY_MSEC
Extra buffering latency in milliseconds. This controls buffering
logic in `libpulse` and may be set for PulseAudio client applications
to adjust their buffering. (Setting it on the `pipewire-pulse` server
has no effect.)

# AUTHORS

The PipeWire Developers <$(PACKAGE_BUGREPORT)>;
PipeWire is available from <$(PACKAGE_URL)>

# SEE ALSO

pipewire-pulse.conf(5),
pipewire(1),
pipewire-pulse-modules(7)
