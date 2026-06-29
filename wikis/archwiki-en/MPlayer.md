# MPlayer

MPlayer is a popular movie player for GNU/Linux. It has support for most video and audio formats and is thus highly versatile, even if it is mostly used for viewing videos.

## Installation
Install the  package.

Some video players can use MPlayer as a backend.

## Configuration
System-wide configuration files are located in the , whereas the user-local settings are stored in  directory.
The default files in the  are:

*  - Contains configuration of codecs.
*  - Is an example of mplayer.conf, which is not automatically created after installation.
*  - Contains configuration of hotkeys.

A file  is created in the  directory by default.

See also: Example MPlayer configuration file, .

## Key bindings
System key bindings are configured via . Personal key bindings are stored in . For a complete list of keyboard shortcuts look at .

See also: LQWiki:XF86 keyboard symbols

## Tips and tricks
## Hardware video acceleration
See Hardware video acceleration.

## Enabling VDPAU
Append the following to either the system-wide () or user-specific () configuration files:

 vo=vdpau,
 vc=ffh264vdpau,ffmpeg12vdpau,ffodivxvdpau,ffwmv3vdpau,ffvc1vdpau,ffhevcvdpau

## Translucent video with Radeon cards and Composite enabled
To get translucent video output in X you have to enable textured video in MPlayer:

 $ mplayer -vo xv:adaptor=1 file

You can use  to check which video modes your graphics card supports.

## Watching streamed video
If you want to play a video stream (e.g an  link) use:

 $ mplayer -playlist link-to-stream.asx

The  option is necessary because these streams are actually playlists and cannot be played without it.

## DVB-T Streaming
See DVB-T for more info.

## DVD playing
To play a DVD with MPlayer:

 $ mplayer dvd://N

where N is the desired title number. Start at 1 and work up if unsure. To start at a specific chapter use the '-chapter' flag. For example, adding '-chapter 5' to the command starts the dvd playing at chapter five of the title.

Mplayer checks  by default. Tell it to use  with the  option at the command line, or the  variable in .

To play a DVD image file:

 $ mplayer -dvd-device movie.iso dvd://N

To enable the DVD menu use:

 $ mplayer dvdnav://

To enable mouse support in DVD menus use:

 $ mplayer -mouse-movements dvdnav://

To find the audio language, start MPlayer with the  switch to output audio IDs. An audio track is selected with . Set a default audio language by editing  and adding the line  for English.

With MPlayer, the DVD could be set to a low volume. To increase the maximum volume to 400%, use  and . The startup volume defaults to 100% of software volume and the global mixer levels will remain untouched. Using the  and  keys, volume can be adjusted between 0 and 400 percent.

 alang=en
 softvol=yes
 softvol-max=400

## JACK support
To have MPlayer audio output directed to JACK:

 $ mplayer -ao jack path/to/file

## Advanced Subtitles
In order to get Advanced SubStation Alpha (ass) or SubStation Alpha (ssa) formatted subtitles to display properly:

 $ mplayer -ass path/to/subtitledVideo.mkv

One possible indication of needing to enable this flag is if you get numbers appearing with your subtitles. This is caused by the positioning information being interpreted as something to be displayed. Mplayer will also complain about subtitles being either too long or having too many lines.

Enabling  also enables any embedded fonts. As per the note in the mplayer's man adding  is unneeded if  is version 2.4.2 or newer. Fontconfig will also be used to select which font to use when there are no embedded fonts. This may result in a different font being used than the OSD subtitle renderer.

## Internet radio
Here is an example of a script for an easy start/stop of playing a predefined radio station. For more details on a running mplayer instance:

 $ ps -eo pcpu,pid,user,comm | grep -i "mplayer"$ | sed  "s/ mplayer$//m"

## Additional binary codecs
If you need to play media encoded with the cook, drvc or sipr codecs, you can install the "essentials" binary codec pack with the  package. See http://www.mplayerhq.hu/design7/dload.html for more information.

## Allow Screensaver/DPMS while playback is paused
MPlayer by default blocks the screensaver what might be undesirable if you forget a paused video. The following configs will keep the screensaver and DPMS enabled but use  to press an inert key every 60 seconds:

 nostop-xscreensaver=1
 heartbeat-interval=60
 heartbeat-cmd="xdotool key VoidSymbol"

## Troubleshooting
## MPlayer fails to open files with spaces
MPlayer can fail to open a file with spaces (e.g. 'The Movie') by saying that it could not open the file  (where all spaces are converted to ). This can be fixed by editing  to changing the following line from:

 Exec=mplayer %U

to:

 Exec=mplayer "%F"

If you use a frontend/GUI for MPlayer, enter its name in .

## MPlayer has black or strange colored font for OSD and Subtitles
There appears to be an issue with OSD and Subtitle colors when using vdpau output, which mplayer may be using by default. You can get around this issue by using xv instead of vdpau:

 $ mplayer -vo xv

See the original [https://bbs.archlinux.org/viewtopic.php?pid=1379141 forums thread for details.

## SMPlayer: No video issue
SMPlayer may have trouble opening some  (and probably ) videos. If it plays only audio without any video, a possible fix is to use MOV as the demuxer:

If problem persists after doing so, it is because SMPlayer is keeping settings for that specific file. Deleting the settings for all the files that SMPlayer is keeping will solve this problem:

 $ rm -rf ~/.config/smplayer/file_settings

## SMPlayer: fail to resume playback after pause
SMPlayer might stop playing a video after pausing it if your audio output driver is incorrectly set. You can fix this by specifically setting your audio driver. For example, if you use PulseAudio, this can be done by starting MPlayer with the .

You can also change this from SMPlayer by going to Options > Preferences > General > Audio and setting the Output Driver option to pulse.

## SMPlayer: no video when using transparency in GNOME
This problem may arise under GNOME when using Compiz to provide transparency: SMPlayer starts with a transparent screen with audio playing, but no video. To fix this, create (as root) a file with the contents:

Make it executable and link it as shown below:

 # ln -sf /usr/local/bin/smplayer.helper /usr/local/bin/smplayer

## SMPlayer: OSD font too big / subtitle text too small
Since SMPlayer 0.8.2.1 (with MPlayer2 20121128-1), the ratio of the subtitle font to the OSD font is very strange. This can result in the OSD text filling the whole screen while the subtitles are very small and unreadable. This problem can be solved by adding:

 -subfont-osd-scale 2

or to the extra options passed to MPlayer from SMPlayer. These options are found in Options > Preferences > Advanced > Options for MPlayer.

## Mplayer shows question marks for some characters on subtitle
If the codepage of the subtitles is utf8, try using:

 -subcp utf8

You can find the codepage of the subtitles with:

 $ file subtitles.srt

See https://www.linuxquestions.org/questions/slackware-14/mplayer-shows-question-marks-for-some-characters-on-subtitle-works-fine-on-xine-906077/.

## Choppy audio CD playback
CDDA playback may be interrupted every few seconds as the CDROM spins down the CD. To get around this you need to cache or buffer in advance using the  option:

 $ mplayer cdda://:1 -cache 1024

The  is to lower the CDROM speed for a constant spin and less noise.
