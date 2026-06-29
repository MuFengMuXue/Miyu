# Codecs and containers

From Wikipedia:

:A codec is a computer hardware or software component that encodes or decodes a data stream or signal.

In general, codecs are utilized by multimedia applications to encode or decode audio or video streams. In order to play encoded streams, users must ensure an appropriate codec is installed.

This article deals only with codecs and application backends; see List of applications/Multimedia for a list of media players (MPlayer, mpv and VLC are popular choices).

## Requirements
Playing multimedia content requires two components:

* A capable media player
* The appropriate codec

It is not always necessary to explicitly install codecs if you have installed a media player.  For example, MPlayer pulls in a large number of codecs as dependencies, and also has codecs built in.

## List of codecs
## Audio
See also Wikipedia:Comparison of audio coding formats.

## Lossless audio codecs
*
*
*

## Lossy audio codecs
{| class="wikitable" style="text-align:center"
!colspan=2| Format !! Encode !! Decode
|-
|colspan=2| AAC ||colspan=2| #AAC
|-
|colspan=2| ATSC A/52 ||  ||
|-
|colspan=2| CELT ||colspan=2|
|-
|rowspan=2| MPEG-1 || || &nbsp; ||rowspan=2|
|-
| MP3 ||
|-
|colspan=2| Musepack (MPC) ||  1 ||
|-
|colspan=2| Opus ||colspan=2|
|-
|colspan=2| Vorbis ||colspan=2|
|-
!colspan=4| Speech codecs
|-
|colspan=2| AMR ||colspan=2|
|-
|colspan=2| Speex ||colspan=2|
|}

# mppenc is not packaged.

*
*
*
*
*
*
*
*
*
*

## AAC
From Wikipedia:

:Advanced Audio Coding (AAC) is a proprietary audio coding standard for lossy digital audio compression. Designed to be the successor of the MP3 format, AAC generally achieves better sound quality than MP3 at the same bit rate.

*
*
*
*

## Image codecs
*
*
*
*
*
*

## Video codecs
See also Wikipedia:Comparison of video codecs.

{| class="wikitable"
! Format !! Codec Libraries
|-
| AV1 || ,  (decode),  (encode),
|-
| AVS2 ||  (decode)
|-
| Daala ||
|-
| Dirac ||
|-
| DV ||
|-
|rowspan=2| H.265 ||
|-
|
|-
| H.264 ||
|-
| MPEG-1 ||rowspan=2|  (decode)
|-
| MPEG-2
|-
| MPEG-4 || Xvid ()
|-
| Theora ||
|-
| VP8, VP9 ||
|}

*
*
*
*
*
*
*
*
*
*
*

## Container format tools
See also Wikipedia:Comparison of video container formats.

*
*
*

## Backends
## GStreamer
From https://gstreamer.freedesktop.org/:

:GStreamer is a library for constructing graphs of media-handling components. The applications it supports range from simple Ogg/Vorbis playback, audio/video streaming to complex audio (mixing) and video (non-linear editing) processing.

Simply, GStreamer is a backend or framework utilized by many media applications. See GStreamer article.

## xine
From https://sourceforge.net/projects/xine/:

:xine is a free multimedia player. It plays back CDs, DVDs, BluRays and VCDs. It also decodes multimedia files like AVI, MOV, WMV, and MP3 from local disk drives, and displays multimedia streamed over the Internet.

As an alternative to GStreamer, many media players can be configured to utilize the xine backend provided by .

Note that the xine project itself provides a capable video player, .

## libavcodec
libavcodec is part of the FFmpeg project. It includes a large number of video and audio codecs. The libavcodec codecs are included with media players such as MPlayer and VLC, so you may not need to install the  package itself.

## Tips and tricks
## No H264, mpg4 or Musepack (.mpc) in Totem Player
If you see the "The H264 plugin is missing" warning with Totem media player, install .

## No H264 in Parole Player
If you see the "Parole needs H.264 decoder to play this file" warning with Parole media player, install .

## No H.264 in VLC
If you see the warning  install .
