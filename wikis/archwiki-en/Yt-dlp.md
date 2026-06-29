# Yt-dlp

yt-dlp is a command-line program that lets you easily download videos and audio from more than a thousand websites. See the list of supported sites.

## Installation
Install the  package. See the optional dependencies, a notable one to install is FFmpeg for muxing on some sites.

There are also various graphical frontends to yt-dlp, such as  and .

You can also install  which provides a dummy  executable (that just redirects to yt-dlp) for outdated programs that still look for a youtube-dl executable.

## Configuration
The system-wide configuration file is  and the user-specific configuration file is . The syntax is simply one command-line option per line. Example configuration:

 --ignore-errors
 # --no-playlist

 # Save in ~/Videos
 -o ~/Videos/%(title)s.%(ext)s

 # Prefer 1080p or lower resolutions
 -f bestvideoExample of importing cookies from chromium

 $ yt-dlp --cookies-from-browser chromium URL

## Tips and tricks
## Faster downloads
Some websites throttle transfer speeds. You can often get around this by choosing non DASH streams or by using aria2, an external downloader which supports multi-connection downloads. For example:

 $ yt-dlp --downloader aria2c --downloader-args '-c -j 3 -x 3 -s 3 -k 1M' URL

## Playlist
Using youtube-dl for a playlist usually boils down to the following options:

 $ yt-dlp --ignore-errors --continue --no-overwrites --download-archive progress.txt usual options URL

This set of options allow for the download to effectively continue even after interruption. If you are archiving, add the usual  and  options you may have.

## Trim (partial download)
Parts of videos can be downloaded by using the output of  as ffmpeg input with the  (for input),  and  [https://ffmpeg.org/ffmpeg.html#Main-options options.

## URL from clipboard
A shell alias, a desktop launcher or a keyboard shortcut can be set to download a video (or audio) of a selected (or copied) URL by outputting it from the X selection. See Clipboard#Tools.
