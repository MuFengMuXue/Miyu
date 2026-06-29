# SRT Live Server

From the SLS README:
:SRT Live Server (SLS) is an open source live streaming server for low latency based on Secure Reliable Tranport (SRT). Normally, the latency of transport by SLS is less than 1 second in internet.

## Installation
Install .

## Configuration
The default configuration file is , edit it to your liking or provide your own. For information on configuration directives see the upstream wiki page.

## Running the server
To run the server you need to provide a configuration file with the  option. To use the default:

 $ sls -c /etc/sls.conf

## Streaming to the server
You can use any solution that can output media in the SRT protocol.

## Using slc
 is a client part of the  package and can be used to push a MPEG-TS formatted file to the server:

 $ slc -r srt://your.sls.ip:8080?streamid=uplive.sls.com/live/test -i filename

## Using FFmpeg
You may use FFmpeg for streaming media to the server by using it as an output file. For example to stream your screen with the x11grab and ALSA virtual devices:

 $ ffmpeg -f x11grab -framerate 30 -i $DISPLAY -f alsa -i default -c:v libx264 -preset ultrafast -c:a aac -flush_packets 0 -f mpegts "srt://your.sls.ip:8080?streamid=uplive.sls.com/live/test"

## Using Open Broadcaster Software
Open Broadcaster Software supports the SRT protocol to publish stream when version is later than v25.0. You can stream to a Custom Service option by setting the URL to your SLS instance (i.e. )

## Consuming the stream
On the client side you can use your favorite client that supports the SRT protocol. Here are a couple examples.

## Using slc
The provided client  can be used to save the stream to a file:

 $ slc -r srt://your.sls.ip:8080?streamid=live.sls.com/live/test -o filename

## Using FFmpeg
You may use  from  to play the stream:

 $ ffplay -fflags nobuffer -i "srt://your.sls.ip:8080?streamid=live.sls.com/live/test"

## Using Open Broadcaster Software
You can use OBS Studio with a Media Source by pointing to the URL of the server. Add a new Media Source, untick the Local file option and set the URL (i.e. ) in the Input field of the Properties dialog.
