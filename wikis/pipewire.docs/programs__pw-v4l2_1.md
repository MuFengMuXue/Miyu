# pw-v4l2

Use PipeWire instead of V4L2

# SYNOPSIS

*pw-v4l2** \[*options*\] *COMMAND* \[*ARGUMENTS...*\]

# DESCRIPTION

*pw-v4l2** runs a command using a compatibility layer that maps PipeWire
video devices to be visible to applications using V4L2.

This is implemented by preloading a shared library via LD_PRELOAD,
which translates library calls that try to access V4L2 devices.

# OPTIONS

 -h
Show help.

 -r NAME
The name of the remote instance to connect to. If left unspecified, a
connection is made to the default PipeWire instance.

 -v
Verbose operation.

# EXAMPLES

*pw-v4l2** v4l2-ctl --list-devices

# AUTHORS

The PipeWire Developers <$(PACKAGE_BUGREPORT)>;
PipeWire is available from <$(PACKAGE_URL)>

# SEE ALSO

pipewire(1),
