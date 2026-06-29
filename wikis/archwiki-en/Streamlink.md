# Streamlink

Streamlink is a command-line utility written in Python which allows you to watch online video streams in popular video players, such as VLC, MPlayer or mpv; see Player compatibility for the full list.

This project was forked from Livestreamer, which is no longer maintained.

Support for various streaming services is provided by plugins, which can be easily added if needed. A lot of popular video streaming services are supported out of the box, including Dailymotion, Livestream, Twitch, UStream, YouTube Live and many more; see Plugins for the full list.

## Installation
Install the  package.

## Usage
The package provides a streamlink command-line utility, which is quite easy to use:

 $ streamlink -p your_player url stream

*  - name of executable of your media player, for example, . You can also specify a full path if needed: . By default, VLC will be used if it can be found in its default location.
*  - URL address of a stream. Usually, the protocol of http(s) URLs can be omitted (https://), depending on the implementation of the plugin being used.
*  - stream to play by given URL. Primarily, you can select the video quality with this option. Use  for highest and  for lowest quality available. Specific plugins may have additional quality options. If it is not provided, a list of all currently available streams will be displayed.

For example:

 $ streamlink -p mpv dailymotion.com/embed/video/x1b1h6o worst

See  for the full list of available options.

To save a stream to your HDD

 $ streamlink -o ~/$current_time.m2t "STREAM URL" best,high

## Twitch
 $ streamlink -p player twitch.tv/name_of_channel quality

For example:

  $ streamlink -p vlc twitch.tv/archlinux medium

Available quality options may include (depending on the source quality): ,  (), , , , and  ().
