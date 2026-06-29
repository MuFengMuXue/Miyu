[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Mplayer&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Mplayer "Mplayer (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Mplayer/ru "Mplayer (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [General options]](#General_options)
-   [[3] [Per file/protocol option]](#Per_file.2Fprotocol_option)

## [Overview]

**mplayer** is a media file player which can decode nearly every media file out there. It can also use countless output drivers (like vpdau or pulseaudio) Most of the time mplayer is in the background when you use frontends like gnome-mplayer, smplayer or gmusicbrowser. Those frontend bring their own set of parameters with them but you still can set up mplayer with it\'s config file (\~/.mplayer/config). The vastness of those options scare most people away but with a little bit of help you can set up **mplayer** easily.

\

**Note**

------------------------------------------------------------------------

mplayer has been mostly replaced in common use by **mpv**

\

# [General options]

Default options which i found useful

     [default]
     ao=pulse
     vo=vdpau
     dr=1
     use-filedir-conf=1
     noquiet=1
     msglevel=all=5
     noslices=1
     double=yes
     framedrop=0
     hardframedrop=0
     vsync=1
     ac=ffmpeg,ffmp3,mad,mp3acm,mpg321,
     srate=48000
     format=s16le
     channels=6
     cache=8192
     cache-min=50
     softvol=yes
     volstep=2
     volume=50
     softvol-max=50

\

# [][Per file/protocol option]

Another great feature of mplayer is that it can use different settings according to your media file (extension or protocol) Settings in this sections overrides the default config.

Here\'s an example for mp3 files

     [extension.mp3]
     profile-desc="for .mp3 files"
     af=surround=15,center=4,channels=6,sub=60:5
     ac=ffmp3,mad,nmp3acm,mpg321,a52,
     af-adv=force=5
     lavdopts=threads=4

The notable thing is the audio filter line (af=), This line

     af=surround=15,center=4,channels=6,sub=60:5

decodes matrix encoded surround sound like Dolby Surround. You need a 5.1 speaker set for that to work.

Here\'s the section for mkv files. Using the above line here would mess up the already 5.1 encoded sound.

     [extension.mkv]
     profile-desc="for .mkv files"
     cache=81920

The following is a protocol section for DVD decoding. (Not sure what it acutally does since i don\'t have any DVDs :P)

     [protocol.dvd]
     profile-desc="Profil für dvd://-Streams"
     alang=en
     vo=vdpau,gl:yuv=2:force-pbo,xv,
     vc=ffh264vdpau,ffmpeg12vdpau,ffwmv3vdpau,ffvc1vdpau,

     [protocol.dvdnav]
     profile-desc="Profil für dvdnav://-Streams"
     profile=protocol.dvd
     mouse-movements=yes