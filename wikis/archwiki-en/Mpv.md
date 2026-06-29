# Mpv

mpv is a media player based on MPlayer and the now unmaintained mplayer2. It supports a wide variety of video file formats, audio and video codecs, and subtitle types. A detailed (although admittedly incomplete) list of differences between mpv and the aforementioned players can be found in == Installation ==

Install the  package.

## Front ends
See List of applications/Multimedia#mpv-based.

## Configuration
mpv comes with good all-around defaults that should work well on computers with weaker/older video cards. However, if you have a computer with a more modern video card, mpv allows you to do a great deal of configuration to achieve better video quality (limited only by the power of your video card). To do this, one only needs to create a few configuration files (as they do not exist by default).

To help you get started, mpv provides sample configuration files with default settings. Copy them to use as a starting point:

 $ cp -r /usr/share/doc/mpv/ ~/.config/

 contains the majority of mpvs settings,  contains key bindings. Read through both of them to get an idea of how they work and what options are available.

## General settings
Add the following settings to .

## Subtitle configurations
Enable fuzzy searching:

 sub-auto=fuzzy

Change font:

 sub-font="fontName"

Bold the subtitles to increase readability:

 sub-bold=yes

## High quality configurations
By default, mpv utilizes settings that balance quality and performance. Additionally, two predefined profiles are available:  for maximum performance and  for superior rendering quality. You can apply a specific profile using the  option and inspect its contents using .

 profile=high-quality

Live statistics showing how well mpv is performing can be brought up with the  key. It is very useful for making sure that your hardware can keep up with your configuration and for comparing different configurations.

These last two options are a little more complicated.  makes it so that if audio and video go out of sync, then instead of dropping video frames, it will resample the audio (a slight change in audio pitch is often less noticeable than dropped frames). The mpv wiki has an in depth article on it titled [https://github.com/mpv-player/mpv/wiki/Display-synchronization Display Synchronization.  makes motion appear smoother on your display by changing the way that frames are shown so that the source framerate jives better with your display's refresh rate (not to be confused with SVP's technique which actually converts video to 60fps). The mpv wiki has an in depth article on it titled Interpolation though it is also commonly known as smoothmotion.

 profile=high-quality
 video-sync=display-resample
 interpolation

Beyond this, there is still a lot you can do, but things become more complicated, require more powerful video cards, and are in constant development. As a brief overview, it is possible to load special shaders that perform exotic scaling and sharpening techniques including some that actually use deep neural networks trained on images (for both real world and animated content). To learn more about this, take a look around the mpv wiki, particularly the user shader's section.

There are also plenty of other options you may find desirable as well. It is worthwhile taking a look at . It is also helpful to run mpv from the command line to check for error messages about the config.

## Custom profiles
In  it is possible to create profiles which are essentially just "groups of options" with which you can:

* Quickly switch between different configurations without having to rewrite the file.
* Create special profiles for special content.
* nest profiles so that you can make more complicated profiles out of simpler ones.

Creating a profile is easy. The area at the top of  is called the top level, any options you write there will kick into effect once mpv is started. However, once you define a profile by writing its name in brackets, every option you write below it (until you define a new profile) is considered part of that profile. Here is an example :

 profile=myprofile2        #Top level area, load myprofile2
 ontop=yes                 #Always on top

 #A simple profile, top level area ends here
 profile-desc="a profile"  #Optional description for profile
 fs=yes                    #Start in full screen

 [myprofile2              #Another simple profile
 profile=high-quality      #A built in profile that comes with mpv
 log-file=~~/log           #Sets a location for writing a log file, ~~/ translates to ~/.config/mpv

There are only two lines within the top level area and there are two separate profiles defined below it. When mpv starts, it sees the first line, loads the options in  (which means it loads the options in  and ) finally it loads  and finishes starting up. Note,  is never loaded because it is never called in the top level area.

Alternatively, one could call mpv from the command line with:

 $ mpv --profile=myprofile1 video.mkv

and it would ignore all options except the ones for .

## Automatic profiles
Certain types of profiles will be loaded automatically based on either the file extension or the protocol used.

These profiles will be loaded for all files with a matching file extension (for all .mkv and .gif files respectively):

This profile will be loaded automatically whenever any http or https streams are played
(e.g. ):

Run  to see the different protocols supported by mpv.

## Key bindings
Key bindings are fairly straightforward given the examples in  and .

Add the following examples to :

 shift+s         screenshot each-frame
 Shift+UP        seek  600
 Shift+DOWN      seek -600
 =               cycle video-unscaled
 -               cycle-values window-scale 2 3 1 .5
 WHEEL_UP        add volume 5
 WHEEL_DOWN      add volume -5
 WHEEL_LEFT      ignore
 WHEEL_RIGHT     ignore
 Alt+RIGHT       add video-rotate 90
 Alt+LEFT        add video-rotate -90
 Alt+-           add video-zoom -0.25
 Alt+=           add video-zoom 0.25
 Alt+j           add video-pan-x -0.05
 Alt+l           add video-pan-x 0.05
 Alt+i           add video-pan-y 0.05
 Alt+k           add video-pan-y -0.05
 Alt+BS          set video-zoom 0; set video-pan-x 0; set video-pan-y 0

For an attempt to reproduce MPC-HC key bindings in mpv, see === Additional configuration files ===

In addition there are a few more configuration files and directories that can be created, among which:

*  manages the on Screen Controller. See  for more information.
*  for Lua scripts. See [https://github.com/mpv-player/mpv/issues/3500#issuecomment-305646994 for an example.

See  for information on other files and directories.

## Scripts
mpv has a large variety of scripts that extend the functionality of the player. To this end, it has internal bindings for both Lua and JavaScript.

Scripts are typically installed by putting them in the  directory (you may have to create it first). After that they will be automatically loaded when mpv starts (this behavior can be altered with other mpv options). Some scripts come with their own installation and configuration instructions, so make sure to have a look. In addition some scripts are old, broken, and unmaintained.

## JavaScript
JavaScript (ES5 via MuJS) has been supported as an mpv scripting language since 2014. Currently only a few scripts are available, but documentation exists at  for anyone interested in making their own.

To get started, drop a script with a  extension in the mpv  directory, e.g.:

{{hc|~/.config/mpv/scripts/fullscreen-off-on-pause.js|

function onPauseChange (prop, enabled) {
    if (enabled) {
        mp.set_property('fullscreen', 'no')
    }
}

mp.observe_property('pause', 'bool', onPauseChange)

}}

For more details, e.g. on using  to load CommonJS modules, see .

## Lua
The development of mpvs Lua scripts is documented in  with examples in TOOLS/lua, which are installed to .

For example, you can enable the builtin script to automatically crop videos with black bars:

 $ ln -s /usr/share/mpv/scripts/autocrop.lua ~/.config/mpv/scripts

## mpv-ytdlAutoFormat
mpv-ytdlautoformat is a Lua script to auto change ytdl-format for Youtube and Twitch or the domains you desire, to 480p or the quality you desire.

## mpv-webm
mpv-webm (or simply webm) is a very easy to use Lua script that allows one to create WebM files while watching videos. It includes several features and does not have any extra dependencies (relies entirely on mpv).

## ytdl-preload
ytdl-preload is a Lua script to preload the next ytdl-link in your playlist.

## C
## mpv-mpris
The C plugin mpv-mpris allows other applications to integrate with mpv via the MPRIS protocol. For example, with mpv-mpris installed,  can automatically pause video playback in mpv when a phone call arrives. Another example is buttons (play\pause etc) on bluetooth audio-devices.

To use the plugin, install .

## Vapoursynth
Vapoursynth is an alternative to AviSynth that can be used on Linux and allows for Video manipulation via python scripts. Vapoursynths python scripts can be used as video filters for mpv.

The  package now enables Vapoursynth support by default.

## SVP 4 Linux (SmoothVideoProject)
SmoothVideoProject SVP is a program that is primarily known for converting video to 60fps. It is free in beer and full featured for 64bit Linux (costs money for Windows and OS X and is incompatible with 32bit Linux).

It has three main features and each one can be disabled/enabled as one chooses (you are not forced to use motion interpolation).

# Motion interpolation (youtube video) - An algorithm that converts video to 60fps. This creates the somewhat controversial "soap opera effect" that some people love and others hate. Unfortunately, the algorithm is not perfect and it also introduces more than its share of weird artifacts. The algorithm can be tuned (via a slider) for either performance or quality. It also has some artifact reduction settings that interpolate actual frames with the generated frames reducing the noticeability of the artifacts. The framerate detection can be set to automatic or manual (manual seems to resolve performance issues for some users).
# Black bar lighting (youtube video) - If the image has an aspect ratio that produces black bars on your display, SVP will illuminate the black bars with "lights" generated by the content on the screen. It has some amount of customization, but the defaults are pretty close to optimal.
# LED ambient lighting control (youtube video) - Has the ability to control LED ambient lighting attached to your television.

Once you have mpv compiled with Vapoursynth support, it is fairly easy to get SVP working with mpv. Simply install , open the SVP program to let it assess your system performance (you may want to close other programs first so that it gets an accurate reading), and finally add the following mpv profile to your mpv.confThen, in order to use SVP, you must have the SVP program running in the background before opening the file using mpv with that profile. Either do:

 $ mpv --profile=svp video.mkv

or set  in the top-level portion of the mpv configuration.

If you want to use hardware decoding, you must use a copy-back decoder since normal decoders are not compatible with Vapoursynth (choose a  option that ends in ). For instance:

 hwdec=auto-copy
 hwdec-codecs=all

Either way, hardware decoding is discouraged by mpv developers and is not likely to make a significant difference in performance.

## Tips and tricks
## Picture
## Hardware video acceleration
See Hardware video acceleration.

Hardware accelerated video decoding is available via the  option. For a list of all supported APIs and other required options, see .

To make it permanent (for example when playing videos from a desktop environment), add it to the configuration file:

To allow CPU processing with video filters, choose a  API.

Use the keyboard shortcut  while a video is running to toggle hardware decoding.

To troubleshoot hardware acceleration, adjusting the logging levels (see ) may be necessary. For instance,  enables the following:
* Verbose messages from the video decoder () and video output () modules.
* Even more detailed trace messages for the module responsible for video decoding. Here, after running mpv once without any log levels adjusted, the module of interest was empirically determined to be .

## Quickly cycle between aspect ratios
You can cycle between aspect ratios using .

## Ignoring aspect ratio
You can ignore the aspect ratio using . To make the option permanent, add the line  to the configuration file.

## Draw to the root window
Run mpv with . mpv will draw to the window with a window ID of 0.

## Always show the application window
To show the application window even for audio files when launching mpv from the command line, use the  option. To make the option permanent, add the line  to the configuration file.

## Disable video output
To disable video output when launching from command line, use the  option, or its alias, .

## Terminal video
* "Color Unicode art video output driver that works on a text console."
* "Color ASCII art video output driver that works on a text console."  support has been disabled on Arch due to vulnerabilities (see ) and has not been added back in as its upstream is inactive: install .
* "Using Kitty protocol for video output that works on all terminals that support this protocol"

## Audio
## Volume is too low
Set  in your configuration file to a reasonable amount, such as , which then allows you to increase your volume up to 150%, which is more than twice as loud. Increasing your volume too high will result in clipping artefacts. Additionally (or alternatively), you can utilize dynamic range compression with .

## Specify an audio output
Run the following command to get a list of available audio output devices

 $ mpv --audio-device=help

Then add one to . For example:

 audio-device=alsa/hdmi:CARD=NVidia,DEV=1

## HD Audio passthrough
To enable HD audio codecs like TrueHD and DTS-MA to passthrough to an AV receiver, add the following to

 audio-spdif=ac3,eac3,dts-hd,truehd

## Volume normalization
Different sources may have different or inconsistent loudness, so mpv users may need to configure automatic volume normalization. For example:

This binds the key  to cycle the audio filter settings () through the specified values:

* : loudnorm setting with , soft volume, might be suitable for background music
* : louder volume, might be good for the video currently in view
* : reset audio filter to null, i.e., disable the audio filter

Audio filtering in mpv is provided by the FFmpeg backend. See Wikipedia:EBU R 128 and [https://ffmpeg.org/ffmpeg-filters.html#loudnorm ffmpeg loudnorm filter for details.

See also upstream issues and [https://github.com/mpv-player/mpv/issues/2883 which mention different options.

## Improving mpv as a music player with Lua scripts
This blog post introduces the music.lua script, which shows how Lua scripts can be used to improve mpv as a music player.

## Save position on quit
By default, you can save the position and quit by pressing . The shortcut can be changed by setting  in the key bindings configuration file.

To automatically save the current playback position on quit, start mpv with , or add  to the configuration file.

## Save position of a playlist and pause on next file
A playlist could simply be a list of files, see . To play a playlist and remember its position:

 $ mpv --save-position-on-quit --pause --reset-on-next-file=pause --playlist=/path/to/playlist

With the option  mpv will start in paused state and   will reset the pause mode when switching to the next file.

## Play a DVD
mpv does not support DVD menus. To start the main stream with the longest title of a video DVD, use the command:

 $ mpv dvd://

An optional title specifier is a number (starting at 0) which selects between separate video streams on the DVD:

 $ mpv dvd://DVDs which have been copied on to a local file system (by e.g. the dvdbackup tool) are accommodated by specifying the path to the local copy: .

See the following desktop file example for playing DVDs from a local file system:

 [Desktop Entry
 Type=Application
 Name=mpv Media Player DVD
 GenericName=Multimedia player
 Comment=Play movies and songs
 Icon=mpv
 Exec=mpv dvd:// --player-operation-mode=pseudo-gui --force-window --idle --dvd-device=%f
 Terminal=false
 Categories=AudioVideo;Audio;Video;Player;TV;
 # (MimeType and X-KDE-Protocols omitted, see original mpv.desktop file)

By replacing the Exec line with

 Exec=mpv dvd://0 dvd://1 dvd://2 dvd://3 dvd://4 dvd://5 dvd://6 dvd://7 dvd://8 dvd://9  --player-operation-mode=pseudo-gui --force-window --idle --dvd-device=%f

the mpv player will queue DVD title 0 to 9 in the playlist, which allows the user to play the titles consecutively or jump forward and backward in the DVD titles with the mpv GUI.

Install , to fix the error:

 Error getting next block from DVD 1 (Error reading from DVD.)

## Restoring old OSC
Since version 0.21.0, mpv has replaced the on-screen controls by a bottombar. In case you want on-screen controls back, you can edit the mpv configuration [https://github.com/mpv-player/mpv/wiki/FAQ#i-want-the-old-osc-back as described here.

## Reproducible screenshots
The screenshot template option can include the precise timecode (HH:MM:SS.mmm) of the screenshoted frame. The meaningful filename makes it easy to know the origin of the screenshot. It can be set like this:

This expands to . Example result:

 Gunsmith Cats/
 ├── Gunsmith Cats Ep. 01 - (1).jpg
 ├── Gunsmith Cats Ep. 01 - [00:22:55.874 (1).jpg
 ├── Gunsmith Cats Ep. 01 - (2).jpg
 └── Gunsmith Cats Ep. 02 - [00:15:05.778 (1).jpg
A bonus is it sorts nicely because alphabetically, the timecode is sorted within the episode number.

See  for more information.

## Creating a single screenshot
An example of creating a single screenshot, by using a start time ():

 $ mpv --no-audio --start=00:01:30 --frames=1 /path/to/video/file --o=/path/to/screenshot.png

Screenshots will be saved in /path/to/screenshot.png.

## Streaming
## Twitch.tv streaming over mpv
If yt-dlp or  is installed, mpv can directly open a Twitch livestream.

Alternatively, see Streamlink#Twitch.

Another alternative based on Livestreamer is this Lua script: https://gist.github.com/ChrisK2/8701184fe3ea7701c9cc

## youtube-dl and choosing formats
The default  is . For youtube videos that have 4K resolutions available, this may mean that your device will struggle to decode 4K VP9 encoded video in software even if the attached monitor is much lower resolution.

Setting the right youtube-dl format selectors can fix this easily though. In the following configuration example, only videos with a vertical resolution of 1080 pixels or less will be considered.

 ytdl-format="bestvideo# Have mpv output a log file. The log file might be difficult to sift through but if something is broken you might see it there.
# Run mpv without a configuration. If this runs well then the problem is somewhere in your configuration (perhaps your hardware cannot keep up with your settings).

If mpv runs but it just does not run well then a fourth thing that might be worth taking a look at is the live statistics (with ) to see exactly how it is performing.

## Fix jerky playback and tearing
mpv defaults to using the OpenGL video output device setting on hardware that supports it. In cases such as trying to play video back on a 4K display using an Intel HD4XXX series card or similar, you will find video playback unreliable, jerky to the point of stopping entirely at times and with major tearing when using any OpenGL output setting. If you experience any of these issues, using the XV (Xorg only) video output device may help:

It is possible to increase playback performance even more (especially on lower hardware), but this decreases the video quality dramatically in most cases.

The following options may be considered to increase the video playback performance:

## Problems with window compositors
As described in , mpv by default disables any active window compositor while in fullscreen mode. This is done to prevent potential performance issues during playback.

For window compositors such as KWin or Mutter, it can be advantageous to disable window compositing even while in windowed mode. This can be achieved by using setting the  option.

There are two disadvantages to disabling compositing:

* Re-enabling compositing may introduce stutter for a period of time, particularly if using KWin compositing.
* Any effects provided by compositing will be temporarily unavailable (until mpv re-enables it), which in Plasma prevents the default app switcher from working.

To sidestep these issues, you can try keeping your compositor enabled with

## No volume bar, cannot change volume
Spin the mouse wheel over the volume icon.

## GNOME Blank screen (Wayland)
mpv may not suspend GNOME's Power Saving Settings if using Wayland resulting in screen saver turning off the monitor during video playback. A workaround is to add  to the beginning of the  line in .

In order to inhibit the screensaver only during playback, use . Alternatively, a [https://gist.github.com/crazygolem/a7d3a2d3c0cee5d072c0cbbbdee69286 mpv lua script based on  may be used.

## Cursor theme not respected under GNOME Wayland
See GNOME/Troubleshooting#Cursor size or theme issues on Wayland.

## Error message about missing CUDA libraries on AMD GPUs
While using VAAPI hardware acceleration on AMD GPUs on versions v0.34.1 and older, you may see a persistent error message saying . This can be suppressed by setting .

Related bug reports: Github issue #9691, Github issue #8765

This issue has been fixed upstream in pull request #9842.

## Unable to play audio if PipeWire is masked
If mpv crashes or fails to play audio on systems where PipeWire is masked, reporting no outputs or broken pipe, set the  option to match your environment. Set it in  for persistent configuration.

## mpv will not start playing a DVD from file
If mpv will not play a DVD from file in plain VIDEO_TS/VOB structure, there could be a problem with the restore playback position function. Try either cleaning  folder, or start mpv with the  option and/or set the  option.

## Fix stuttering after resuming playback from pause
If video is stuttering with PulseAudio, try the  option discussed at :

## Screen sharing cannot capture audio from mpv
For example, when you share mpv into Discord with Discord's "Share a window" functionality and specify that audio should be shared as well, yet Discord fails to capture mpvs audio.

This has been observed when the system uses PipeWire. Then, by default, mpv uses its  audio output driver, which may cause this issue.

The solution is to switch mpv to its  audio output driver. This should be uncritical as PipeWire also implements PulseAudio's audio API.

When running mpv from the command line this can be done by supplying the  option.

To permanently make mpv use its PulseAudio audio output driver you can put an  text line into an mpv configuration file.
