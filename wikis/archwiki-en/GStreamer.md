# GStreamer

From Wikipedia:

:GStreamer is a pipeline-based multimedia framework that links together a wide variety of media processing systems to complete complex workflows. For instance, GStreamer can be used to build a system that reads files in one format, processes them, and exports them in another. The formats and processes can be changed in a plug and play fashion.
:GStreamer supports a wide variety of media-handling components, including simple audio playback, audio and video playback, recording, streaming and editing. The pipeline design serves as a base to create many types of multimedia applications such as video editors, transcoders, streaming media broadcasters and media players.

## Installation
Install the  package.

To make GStreamer useful, install the plugins packages you require. See official documentation for list of features in each plugin.

*  - Libav-based plugin containing many decoders and encoders.
*  - Plugins that need more quality, testing or documentation.
*  - Essential exemplary set of elements.
*  - Good-quality plugins under LGPL license.
*  - Good-quality plugins that might pose distribution problems.

## Usage
## Using gst-launch-1.0
A helpful tool of GStreamer is the  command. It is an extremely versatile command line tool to create GStreamer pipelines. It is very similar to and can do many of the things the FFmpeg command can do. Here are some examples:

Convert an MP4 file to MKV:

 $ gst-launch-1.0 filesrc location=source.mp4 ! qtdemux name=demux matroskamux name=mux ! filesink location=dest.mkv  demux.audio_0 ! queue ! aacparse ! queue ! mux.audio_0  demux.video_0 ! queue ! h264parse ! queue ! mux.video_0

## Using gst-discoverer-1.0
Another helpful tool is , which is the GStreamer equivalent of FFmpeg's .

Get info on a video file:

## Integration
## PulseAudio
PulseAudio support is provided by the  package.

## PipeWire
PipeWire support is provided by the  package.

## KDE / Phonon integration
See Phonon.

## Hardware video acceleration
See Hardware video acceleration.

GStreamer will automatically detect and use the correct API Depending on the system install:

*  for VA-API support.
*  and  for NVDECODE/NVENCODE support.

If the new elements do not show up after installing the packages, you may want to delete and rebuild the plugin registry. Usually it suffices to

 $ rm ~/.cache/gstreamer-1.0/registry.*.bin

Gstreamer will then rebuild the registry on the next invocation, which usually takes a few seconds.

## Verify VA-API support
To verify VA-API support:

## Verify NVDECODE/NVENCODE support
To verify NVDECODE/NVENCODE support:

## Set decoder ranks
For some NVIDIA users,  may prioritize the Libav decoder over [https://gstreamer.freedesktop.org/documentation/nvcodec/index.html nvcodec decoders which will inhibit hardware acceleration. The  environment variable can be used to rank decoders and thus alleviate this issue. See "GST_PLUGIN_FEATURE_RANK" in the documentation for more information. For example:

 GST_PLUGIN_FEATURE_RANK=nvmpegvideodec:MAX,nvmpeg2videodec:MAX,nvmpeg4videodec:MAX,nvh264sldec:MAX,nvh264dec:MAX,nvjpegdec:MAX,nvh265sldec:MAX,nvh265dec:MAX,nvvp9dec:MAX

Those without AV1 hardware support may also want to disable AV1 decoders (e.g., for YouTube on -based browsers) by appending  and  to the list above.
