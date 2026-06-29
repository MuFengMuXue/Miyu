# XDG Autostart

The XDG Autostart specification defines a method for autostarting ordinary desktop entries on desktop environment startup and removable medium mounting, by placing them in specific directories.

## Prerequisites
You need to use either a desktop environment that supports it, or a dedicated implementation, like:

*
*
*
* systemd-xdg-autostart-generator

## Directories
The Autostart directories in order of preference are:

* user-specific:  ( by default)
* system-wide:  ( by default) System-wide desktop entries can be overridden by user-specific entries with the same filename.

For more details, read [https://specifications.freedesktop.org/autostart-spec/latest/ the specification.
