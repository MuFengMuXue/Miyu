# Interception-tools

interception-tools is a set of utilities to control and customize the behavior of keyboard input mappings. For most users it is a backend, and would use it with one of its plug-ins.

Interception-tools operates at a lower level compared to older similar tools (,
xmodmap) by using libevdev and
. It thus works across X11, Wayland, and (even though not official documented) the Linux console.

## Installation
Install .

Many plugins are available:

*  to switch  with /
*
*
*  to modify the behavior of a key when held.
*
*
*
*
*
*
*

## Basics
## How it works
Interception-tool makes use of libevdev, which can sit between the kernel and the process handling an event. Schematically it looks like these:

 kernel > libevdev > console
 kernel > libevdev > xf86-input-evdev > X server > X client
 kernel > libevdev > Compositor > Wayland client

 is low level and it does not know any about X/Wayland.

More precisely, input devices are exposed as , and basically X or Wayland for example read them directly. With libevdev, they can be easily "grabbed"—not read by X/Wayland any more—then it creates a new virtual device, again as . Then X/Wayland read them instead.

## Components
Interception-tools provides 4 executables. The two most important ones are  and ; the former  redirects device input events to stdout, and the latter creates a new virtual device, to which redirect events from stdin.

However they are low-level, and usually you don't have to run them manually. Instead  coordinates; users write config files, and accordingly udevmon runs intercept, uinput and plug-ins. When udevmon is killed, all underlying processes are killed too.

There's also  for complex cases, which combines streams of input events. (The word mux stands for multiplexer.)

## Raw example 1: do nothing
This virtually does nothing:

 $ intercept -g DEVNODE | uinput -d DEVNODE

where  is the path to the actual device: e.g.  for a typical laptop keyboard.

Here intercept grabs the device, and redirects to stdout. uinput creates a new virtual device which is almost a copy of DEVNODE, and redirects stdin to that device. The new device has the same name, and the same abilities as the original device.

## Raw example 2: Use a plugin
To actually perform an operation in between the key event and the input, simply pipe it in between  and .

E.g. with the  plugin installed:

 $ intercept -g DEVNODE | caps2esc | uinput -d DEVNODE

If we omitted the  flag, then device event would have been just observed, not grabbed.

## Usage
Configuration is done by yaml files in . Then users can run  from the command line or by starting .

## Notes
This applies only when a user runs udevmon manually. If it is run by systemd, this can be ignored.

Since the tool has to appear to lie almost at the kernel level, ensure  consistent behavior by increasing  priority:

 # nice -n -20 udevmon -c udevmon.yaml > udevmon.log 2> udevmon.err &

Misconfiguration can screw the keyboard so that you won't be able to stop interception-tools. To avoid it, you can test by running udevmon from timeout:

 # timeout 10 udevmon &

This will kill udevmon (consequently intercept and uinput run by udevmon) in 10 seconds.

## Configuration
## Basics
Config files are written in the yaml format. One simplest example is this:

The JOB line designates how it should be run.

The  configuration will match a device with a specific name, but it will accept also a regex option.
This can be combined with multiple job specifications to create a default behavior, in each case only the first matching job is going to be executed:

Save it in e.g. . Then you can activate it by running .

## Combine devices
Beside input emulation, the  tool also serves purpose to print a device's description in YAML format:

 $ uinput -p -d /dev/input/by-id/my-kbd

which itself can be fed back to  as:

 $ uinput -c my-kbd.yaml

It can also merge device and YAML characteristics, which can be used for instance to combine events coming from keyboard and mouse:

e.g. instance  as

 $ uinput -p -d /dev/input/by-id/my-kbd -d /dev/input/by-id/my-mouse -c my-extra.yaml

## Handle multiple jobs
The  is used to combine multiple pipelines into a single one.
A muxer needs to be created first,
and it can later be used as the input or the output of a given pipeline.
In a YAML specification file, the muxer is created using the  key:

In the example above, when the keyboard is connected, it's grabbed and its input events are sent to the  muxer that was initially created. Observed input (not grabbed) from mouse is also sent to the same muxer. The buttons of the mouse generate  events, so  will accept them.
