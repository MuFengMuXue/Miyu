# VLC media player

From the project home page:

:VLC is a free and open source cross-platform multimedia player and framework that plays most multimedia files as well as DVD, Audio CD, VCD, and various streaming protocols.

## Installation
Install the  split package, that depends on a subset of VLC plugins. See the optional dependencies for more functionality.

*  provides the basic plugin set that is essential on all systems.
*  provides some additional plugins, including Matroska/WebM demuxer, MPEG Transport Stream demuxer, MPEG I/II video decoder and playback of DVDs and Audio CDs.
*  provides some audio visualization plugins, including Goom and ProjectM effects.
*  provides all available plugins, including FFmpeg audio/video decoder, VA-API video decoder, H.264/AVC encoder, H.265/HEVC encoder and FluidSynth MIDI synthesizer.

Alternative frontends:
*  for the CLI interface (run with  or ).
*  for the ncurses TUI (run with ).
*  for the skins2 GUI (run with ).

## Language
VLC does not offer an option to change language in its Preferences menu. But you can use the LANGUAGE environment variable. For instance, modify the  desktop entry to change:

 Exec=/usr/bin/vlc %U

to:

 Exec=env LANGUAGE=fr /usr/bin/vlc %U

to switch VLC interface to French.

## Skins
VLC can be "skinned" for a different look and feel. You can get skins at the skins website.

To install a skin download it and move it to .

Open up VLC, click Tools > Preferences. When the preferences window opens up you should be in the "Interface" tab

Choose the "Use custom skin" radio button, and select the downloaded skin.

Restart VLC for the change to take effect.

## Web interface
Run VLC with the parameter  to use both the desktop and web interface. The  parameter specifies the address to bind to, which is  by default. To set a password, use , otherwise VLC will not allow you to log in.

 $ vlc --extraintf=http --http-host 0.0.0.0 --http-port 8080 --http-password yourpasswordhere

To enable the web interface from the graphical interface, navigate to View > Add Interface > Web Interface. Set the password via Tools > Preferences > Show settings: All > Interface > Main interfaces > Lua > Lua HTTP > Password.

VLC defaults to port : http://localhost:8080

## Tips and tricks
## Twitch.tv streaming over VLC
See Streamlink#Twitch.

## Playing streamed content from a local DLNA server
If you find that trying to play UPnP/DLNA content (by going to View > Playlist > Local Network > Universal Plug'n'Play), that vlc fails to see the DLNA server on the local network, then make sure that the firewall is not blocking port 1900 UDP. It is essential that this port is open in order to play local UPnP/DLNA content.

## Control using hotkeys or cli
Install .

Get script at the archived CrunchBang forums.

Follow instructions in script to setup a socket for VLC.

Either run the script from the command line or register the script with keyboard shortcuts through your desktop.

Alternatively, you can use MPRIS to interact with VLC.

It is also possible to start vlc with an ncurses interface:

 $ vlc -I ncurses

see the documentation for more information

## Preventing multiple instances
By default, VLC opens a new instance of the program every time it is launched with one or more files. This can be annoying if you use VLC to play something like your music collection. You can open multiple files at once by selecting them in the file manager, or disable this behavior from the menu: check Tools > Preferences (set “Show settings” to “Simple”) > Interface > Playlist and Instances > Allow only one instance, and also check Enqueue items into playlist in one instance mode which keeps current file playing and adds any newly opened files to the current playlist.

There is also an option called Use only one instance when started from file manager — when this is enabled, all files opened via the file manager will be played in a single instance. The Enqueue items into playlist in one instance mode option still applies.

## Hardware video acceleration
See Hardware video acceleration.

VLC automatically tries to use an available API, but you can override it by going to Tools > Preferences > Input & Codecs and choosing the suitable option under Hardware-accelerated decoding, e.g.  for VA-API or  for VDPAU.

## systemd service
VLC's web interface can be started from systemd. First, you need to create a default user:

 # useradd -c "VLC daemon" -d / -G audio -M -p \! -r -s /usr/bin/nologin -U vlcd

Now create the systemd service file:

Start and enable . Log in to http://yourmachine:8090/ with no username and with the password you put in the service file.

## Chromecast support
Starting with 3.0 release (Vetinari branch), VLC can stream to Chromecast devices on the same network.

Install packages:

*  - VLC can find the Chromecast device and it shows up in Playback > Renderer menu
*  - enables streaming to the selected device in Playback > Renderer menu

Then, edit the file  and change the  line to include  before  and :

 hosts: ... '''mdns_minimal resolve [!UNAVAIL=return dns ...

## Pause click plugin
Install , which allows you to click on the video inside VLC's window, and it will be paused or resumed. It is a commonly expected behavior.

It is not activated after installation, you need to manually enable it in settings as described in https://github.com/nurupo/vlc-pause-click-plugin#usage.

## Stream from V4L2 AV capture device
For example, live streaming from an USB webcam or from an USB HDMI capture device.

Find the V4L2 device's video device node:

Usually this ist the first listed  node, here .

Then, find the name of the capture device's PulseAudio source:

That name would here be .

## Using the graphical user interface
Now open VLC media player and in the menu bar at the top select Media > Open Capture Device...

In the Device Selection section, choose  as Video device name.
Leave Audio device name empty.1

At the bottom left check the Show more options checkbox. An Edit Options text field should become visible.
In this text field, append at the end, separated with a blank:

 :input-slave=pulse://alsa_input.usb-XF_HDMI_Capture_20000130041415-02.iec958-stereo

Then click the Play button.

1 This is because this input only offers and accepts ALSA devices, which VLC usually cannot access because they are already in exclusive use by PipeWire or PulseAudio.

## From the command line
Alternatively, run VLC media player from the command line with this command:

 $ vlc --v4l2-standard= --live-caching=300 --input-slave=pulse://alsa_input.usb-XF_HDMI_Capture_20000130041415-02.iec958-stereo -- v4l2:///dev/video2

## Troubleshooting
## Video broken or other issue after upgrade
Now and then VLC will have some issues with configuration even in minor releases. Before making bug reports, remove or rename your configuration located at  and confirm whether the issue is still there.

If using a ffmpeg variant from the AUR, be sure that you have upgraded it as well.  Pacman will not upgrade it when necessary and a mismatch will break VLC.

## Segmentation fault
## Fault when initiating VLC
When starting VLC you can get a segfault, and ruling out general factors such as Microcode, a possible workaround to this is running the following:

 # /usr/lib/vlc/vlc-cache-gen /usr/lib/vlc/plugins

Then reinstall VLC.

## Fault when playing a video
If VLC can open and play audio files, but closes when you play a video with a segfault, then Hardware video acceleration was wrongly configured, making VLC unable to refer to graphics devices. It occurs especially when you are using different graphic cards on one computer.

## Missing icons in dropdown menus
This can happen under XFCE, there will be no more icons in dropdown menus, like the PCI card icon.

Execute these commands to reactivate these icons:

 $ gconftool-2 --type boolean --set /desktop/gnome/interface/buttons_have_icons true
 $ gconftool-2 --type boolean --set /desktop/gnome/interface/menus_have_icons true

## Failed to open VDPAU backend
See Hardware video acceleration#Failed to open VDPAU backend.

Since your system probably does not support VDPAU you should tell VLC to use VA-API instead, see #Hardware video acceleration.

## VLC fails to open a second time after closing
Manually set VLC to use the VA-API acceleration backend in Settings -> Input/Codecs. VLC seems to select VDPAU by default, which is broken for many people.

## No playback via SFTP of media files names containing spaces
If VLC does not play any videos or audio files over SFTP make sure you have  installed.

If it refuses to play any media files containing spaces via SFTP and always asks for authentication change the Exec line in the  file to:

 Exec=/usr/bin/vlc --started-from-file %F

See === VLC on iOS/tvOS cannot connect to Arch via SFTP ===

Due to app store licensing restrictions, VLC's iOS and tvOS apps use an incomplete ssh implementation.  needs a config change to be compatible.  Create a file  with contents:

 HostKeyAlgorithms +ssh-rsa
 KexAlgorithms +diffie-hellman-group16-sha512

Then, reload .

## Cannot open DVD
To be able to play DVDs via Media > Open Disc, VLC optional dependencies  and  need to be installed.

Other plugins such as  may be required for certain DVDs. Alternatively, install , which will install the above two plugins, as well as others.

If you have all of the above packages and still cannot open DVDs, try deleting your  folder. This will force a re-download of your CSS keys, which may fix the problem.

## Cannot open Blu-Ray / Blu-Ray menus do not load
See Blu-ray#VLC

## Media does not load
If some RTP, RTSP, DVB-T streams or Blu-rays look like they are endlessly buffering or silently do not load, without giving an error message in the logs (e.g. IPTV from French FAI Free) install .

## Wayland support
 builds with Wayland support by default. Set the  environment variable to enable Wayland. See Wayland#Qt for more info.

Note that although the  build flag is used in the  PKGBUILD (which [https://gitlab.archlinux.org/archlinux/packaging/packages/vlc/-/blob/main/PKGBUILD currently uses VLC version 3.0), Xwayland is used anyway, as Wayland support on VLC 3 is broken. Video output in VLC may be cropped or otherwise malformed unless  is installed.

With the following command VLC 3 will start using Wayland:
 $ env -u DISPLAY vlc

This works because VLC 3 checks for the environment variable  on startup and will use Wayland if it is not set. Globally removing  from the environment is not recommended, because some older Applications still rely on this variable.

## Failed to connect to RTSP stream
When connection to RTSP stream ends up with the  error, install .

## Random colors when playing streams with Streamlink
Install the optional dependency .

## Unresponsive system when playing HEVC video with AMDGPU
When playing a video encoded with HEVC (H265), users may encounter a total system freeze and are unable to do anything or shutdown.

This can be fixed by changing the settings for Open GL/GLES hardware converter to something other than Automatic (e.g. VDPAU OpenGL surface converter or VA-API OpenGL surface converter for Wayland).

See https://gitlab.freedesktop.org/drm/amd/-/issues/2113#note_1602599

## Sound disappears briefly after changing playback progress
Set Tools > Preferences (with “Simple” view) > Audio > Output module" to the audio server currently in use. (For PipeWire, you need to install , otherwise only compatibility layers can be used.)

## VLC not showing subtitles and OSD
Even if you have the plugin to decode subtitles, you will not see them on the screen (and there will not be any error on the Messages/Console), if you are missing the , which is not included in  but .

## "VLC could not identify the audio or video codec" for subtitles in MKV files
If subtitles display fine when loaded from an external file, but embedded subtitles in an MKV file are not recognized, you are more than likely missing the  package, which is not included in  but .

## KDE Plasma does not apply dark theme to VLC
Read the first item of the tip box in KDE#Themes.
