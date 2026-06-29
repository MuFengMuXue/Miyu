# NAME

Xwayland - an X server for running X clients under Wayland.

# SYNOPSIS

**Xwayland** \[option ...\]

# DESCRIPTION

*Xwayland* is an X server and a Wayland client. It plays the role of a proxy between legacy X clients which do not support the Wayland protocols and the Wayland server.

Usually, *Xwayland* is spawned automatically by the Wayland server and runs rootless so that X clients integrate seamlessly with the rest of the Wayland desktop. It is however possible for a user to launch Xwayland non-rootless, mainly for testing purposes.

Like all of the X servers, *Xwayland* accepts the command line options described in the **Xserver**(7) manual page. The following additional arguments are supported as well.

**-decorate**  
Add decorations to the Xwayland root window when running rootful.

This option has no effect when *Xwayland* is built without libdecor support (optional).

This option is not compatible with rootless mode (*-rootless*).

**-enable-ei-portal**  
Enable support for the XDG portal for input emulation.

A Wayland compositor running nested should not use that command line option with Xwayland.

This option has no effect if the compositor doesn't support the relevant XDG portal or if Xwayland was not compiled with EI and OEFFIS support.

**-clipboard**  
Enable the Xwayland clipboard selection bridge, syncing the X11 CLIPBOARD and PRIMARY selections with the Wayland clipboard and primary selection.

The Xwayland clipboard selection bridge is not enabled by default.

**-fullscreen**  
Set the Xwayland window fullscreen when running rootful.

This option is not compatible with rootless mode (*-rootless*).

**-geometry *WxH***  
Sets the geometry of the *Xwayland* window to *WxH* when running rootful.

This option is not compatible with rootless mode (*-rootless*).

**-glamor \[*gl\|es\|off*\]**  
Use given rendering API for Glamor acceleration. Possible options are *gl* and *es*. If *Xwayland* was compiled with Glamor support, this option will instruct *Xwayland* to use only requested API for Glamor. If this set to *off*, effect is equal to *-shm* option. Without this option and without *-shm* option, *Xwayland* tries the OpenGL rendering API first, and fallback to GL ES if GL version is less than 2.1.

This option is not compatible with *-shm* option.

**-hidpi**  
Adjust to the scale of the outputs when running rootful in windowing mode.

This option is not compatible with rootless mode (*-rootless*).

**-host-grab**  
Disable host keyboard shortcuts and confine the pointer when running rootful.

This feature relies on the protocol for inhibiting the compositor keyboard shortcuts and on the protocol for pointer locking and confinement and may have no effect if the Wayland compositor in use does not support these protocols.

Use the keys \[CTRL\]+\[SHIFT\] simultaneously to release the keyboard and pointer devices.

This option is not compatible with rootless mode (*-rootless*).

**-initfd *fd***  
Add the given *fd* as a listen socket for initialization of X clients. This options is aimed at *Wayland* servers which run *Xwayland* on-demand, to be able to spawn specific X clients which need to complete before other regular X clients can connect to *Xwayland*, like *xrdb*.

**-listen *fd***  
deprecated, use *-listenfd* instead.

**-listenfd *fd***  
Add given fd as a listen socket. This option is used by the *Wayland* server to pass *Xwayland the socket where X clients connect.*

**-noTouchPointerEmulation**  
Disable touch pointer emulation. This allows the Wayland compositor to implement its own pointer emulation mechanism for X11 clients that don't support touch input.

**-force-xrandr-emulation**  
Force additional non-native modes to be exposed when viewporter is not supported by the Wayland compositor.

**-nokeymap**  
Instructs *Xwayland to ignore the keymap set by the Wayland compositor.*

By default, *Xwayland (as any Wayland client) uses the keymap set by the* Wayland compositor using the standard Wayland protocol.

This option is meant for some specific use cases where it may be desirable to let the X11 clients control the keymap used in Xwayland, ignoring the keymap specified by the Wayland compositor. **-output *name*** Specifies on which output *Xwayland fullscreen rootful should be placed.* The name must match the name of an existing Wayland output (output names can be found using wayland-info).

If no matching output can be found, the Wayland compositor will decide on which output the fullscreen rootful *Xwayland window will be placed.*

This option has no effect if *Xwayland is not running fullscreen rootful.*

**-rootless**  
Run *Xwayland rootless, so that X clients integrate seamlessly with* Wayland clients in a Wayland desktop. That requires the Wayland server to be an X window manager as well.

**-shm**  
Force the shared memory backend instead of glamor (if available) for passing buffers to the Wayland server.

This option is not compatible with *-glamor option.*

**-version**  
Show the server version and exit.

**-wm *fd***  
This option is used by the *Wayland server to pass Xwayland* the socket where the X window manager client connects, when *Xwayland* is running with *-rootless.*

# ENVIRONMENT

**WAYLAND_DISPLAY**  
the name of the display of the Wayland server.

**XWAYLAND_NO_GLAMOR**  
disable glamor and DRI3 support in *Xwayland, for testing purposes.*

# SEE ALSO

General information: **X**(7), **wayland-info**(7)
