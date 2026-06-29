# Libcanberra

Libcanberra is a simple abstract interface for playing event sounds. It implements the XDG Sound Theme and Naming Specifications for generating event sounds on free desktops, such as GNOME. Further description here

## Installation
Libcanberra can be installed with the package . libcanberra no longer requires any backends for ALSA, pulseaudio or gstreamer, as they are now built in to the  package.

It is necessary to have a sound theme installed in order to hear any event sound:

* The default sound theme 'freedesktop' () will be installed as dependency of libcanberra.
* Alternatively, search for "sound-theme" in the official repositories or the Arch User Repository.

## Configuration
By default, the GTK module is loaded automatically when a GTK application launched. You can overwrite the default settings in the user's GtkSettings file:

In GNOME, these settings are managed by gnome-settings-daemon, and the configuration is available in GSettings under the  schema.

## systemd
To enable bootup, shutdown and reboot sounds using canberra, enable .
