# Input remap utilities

In an X or Wayland environment, most remapping tasks can be completed with local XKB configuration, see X keyboard extension#Local XKB folder. For remapping keys in the linux console, see Linux console/Keyboard configuration. For keyboards or devices that report incorrect keycodes, see Map scancodes to keycodes.

Some specialized configurations or behaviors use software daemons to translate input events. This page lists software that you can use to reconfigure input events from keyboards, mice and other hardware.

## Utilities
## evremap
evremap () — A keyboard input remapper for Linux/Wayland systems. This tool can do remap in a following way: remap the  key so that it produces  when held, but  if tapped and remap  keys to  keys. E.g.:  to , and  to .

After installation, create a config file  (example from repo), or edit  to point to your config. Then start the service.

## evdevremapkeys
evdevremapkeys () — A daemon to remap key events on linux input devices. This tool can remap keyboard and mouse events. It can map to repeated actions (for example, do double click) and can generate them while button is pressed (for example, generate wheel up events while holding back button).

It is also possible to remap combo to combo, but this is not yet merged, and is available in pronobis fork. See here.

## evsieve
evsieve () — A low-level utility that can read events from Linux event devices (evdev) and write them to virtual event devices (uinput), performing simple manipulations on the events along the way. Works on Wayland. Evsieve is particularly intended to be used in conjunction with the evdev-passthrough functionality of Qemu.

## kbct
kbct () — Keyboard Customization Tool for Linux. Despite its name, also supports mouse events. This tool allows you to map an event (keyboard or mouse button) to another event. You can define multiple "layers" — lists of maps depending of which modifier you press with an input key. Unfortunately, currently the kbct does not allow you to generate multi-button event. See After installation, edit  as required, then start .

## keyd
[https://github.com/rvaiya/keyd keyd () — A key remapping daemon for Linux using a flexible system-wide daemon which remaps keys using kernel level input primitives (evdev, uinput). Keyd works in both graphical environments, like X11 and Wayland, and the Linux virtual console. Read the project's README for more information about how keyd compared to similar software.

## Input Remapper
Input Remapper () — A utility that provides a GUI and a CLI to configure input devices remappings. Works with both X and Wayland.

## makima
makima () — Linux daemon to remap and create macros for keyboards, mice and controllers. Uses the evdev interface. Configured per device by placing  files in , and also supports per application configuration with  (X11, Sway, Hyprland and Niri only).

## wtype
wtype () — xdotool type for Wayland (requires compositor support for the virtual keyboard protocol).

## Other
* Hawck - A low-level key rebinding daemon
* IMWheel — A tool for X11 that can remap mouse wheel events depending on pressed modifier and individually per application.
* Interception-tools — Yet another versatile tool, using various plug-ins.
* Mouse buttons#User tools — A list of hardware-dependent utilities to configure mouse buttons.
* wayland-mouse-mapper — A small script for mapping mouse buttons to keystrokes on Wayland.
* evmapy — An evdev event mapper written in Python. Not in AUR yet.
* python-evdev — A utility that allows you to read and write input events on Linux. An event can be a key or button press, a mouse movement or a tap on a touchscreen.
* kmonad - advanced keyboard remapping tool daemon
* noinputs () — A utility to list and disable (inhibit) input devices.
* xremap (multiple packages) — Key remapper for X11 and Wayland using evdev and uinput.
* keymapper () - a cross-platform context-aware key remapper (working in both X11 and Wayland)

## Testing
* evtest () — utility that can show you the button names when you press them, which can help when configuring remap utilities.
* wev () — utility to view input events in wayland, similar to xev.

With  you can see all events that are emitted on your computer.

Another approach of testing keyboard buttons is with online websites. Most of such testers cannot distinguish between left and right modifiers. One example that can is: https://stendec.io/
