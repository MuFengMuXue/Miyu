# FFmpeg

From the project home page:
:FFmpeg is a complete, cross-platform solution to record, convert and stream audio and video. It includes libavcodec - the leading audio/video codec library.

## Installation
Install the  package. A notable variant is , which is built with as many optional features enabled as possible.

## Encoding examples
See FFmpeg encoding wiki and .

## Screen capture
FFmpeg includes the x11grab and ALSA virtual devices that enable capturing the entire user display and audio input.

To take a screenshot :

 $ ffmpeg -f x11grab -video_size 1920x1080 -i $DISPLAY -vframes 1 screen.png

where  specifies the size of the area to capture.

To take a screencast  with lossless encoding and without audio:

 $ ffmpeg -f x11grab -video_size 1920x1080 -framerate 25 -i $DISPLAY -c:v ffvhuff screen.mkv

Here, the Huffyuv codec is used, which is fast, but produces huge file sizes.

To take a screencast  with lossy encoding and with audio:

 $ ffmpeg -f x11grab -video_size 1920x1080 -framerate 25 -i $DISPLAY -f alsa -i default -c:v libx264 -preset ultrafast -c:a aac screen.mp4

Here, the x264 codec with the fastest possible encoding speed is used. Other codecs can be used; if writing each frame is too slow (either due to inadequate disk performance or slow encoding), then frames will be dropped and video output will be choppy.

If the video stream should not be saved as a file, but used as a virtual webcam for screen sharing purposes, see v4l2loopback#Casting X11 using FFmpeg.

See also the official documentation.

## Recording webcam
FFmpeg includes the video4linux2 and ALSA input devices that enable capturing webcam and audio input.

The following command will record a video  from the webcam without audio, assuming that the webcam is correctly recognized under :

 $ ffmpeg -f v4l2 -video_size 640x480 -i /dev/video0 -c:v libx264 -preset ultrafast webcam.mp4

where  specifies the largest allowed image size from the webcam.

The above produces a silent video. To record a video  from the webcam with audio:

 $ ffmpeg -f v4l2 -video_size 640x480 -i /dev/video0 -f alsa -i default -c:v libx264 -preset ultrafast -c:a aac webcam.mp4

Here, the x264 codec with the fastest possible encoding speed is used. Other codecs can be used; if writing each frame is too slow (either due to inadequate disk performance or slow encoding), then frames will be dropped and video output will be choppy.

See also the official documentation.

## VOB to any container
Concatenate the desired VOB files into a single stream and mux them to MPEG-2:

 $ cat f0.VOB f1.VOB f2.VOB | ffmpeg -i - out.mp2

## x264
## Lossless
The ultrafast preset will provide the fastest encoding and is useful for quick capturing (such as screencasting):

 $ ffmpeg -i input -c:v libx264 -preset ultrafast -qp 0 -c:a copy output

On the opposite end of the preset spectrum is veryslow and will encode slower than ultrafast but provide a smaller output file size:

 $ ffmpeg -i input -c:v libx264 -preset veryslow -qp 0 -c:a copy output

Both examples will provide the same quality output.

## Constant rate factor
Used when you want a specific quality output. General usage is to use the highest  value that still provides an acceptable quality. Lower values are higher quality; 0 is lossless, 18 is visually lossless, and 23 is the default value. A sane range is between 18 and 28. Use the slowest  you have patience for. See the x264 Encoding Guide for more information.

 $ ffmpeg -i video -c:v libx264 -tune film -preset slow -crf 22 -x264opts fast_pskip=0 -c:a libmp3lame -aq 4 output.mkv

 option can be used to match the type and content of the media being encoded.

## Two-pass (very high-quality)
Audio deactivated as only video statistics are recorded during the first of multiple pass runs:

 $ ffmpeg -i video.VOB -an -vcodec libx264 -pass 1 -preset veryslow \
 -threads 0 -b:v 3000k -x264opts frameref=15:fast_pskip=0 -f rawvideo -y /dev/null

Container format is automatically detected and muxed into from the output file extension ():

 $ ffmpeg -i video.VOB -acodec aac -b:a 256k -ar 96000 -vcodec libx264 \
 -pass 2 -preset veryslow -threads 0 -b:v 3000k -x264opts frameref=15:fast_pskip=0 video.mkv

## Video stabilization
Video stablization using the vid.stab plugin entails two passes.

## First pass
The first pass records stabilization parameters to a file and/or a test video for visual analysis.

* Records stabilization parameters to a file only
* Records stabilization parameters to a file and create test video "output-stab" for visual analysis

## Second pass
The second pass parses the stabilization parameters generated from the first pass and applies them to produce "output-stab_final".  You will want to apply any additional filters at this point so as to avoid subsequent transcoding to preserve as much video quality as possible.  The following example performs the following in addition to video stabilization:

*  is recommended by the author of vid.stab. Here we are simply using the defaults of 5:5:1.0:5:5:1.0
*  fade in from black starting from the beginning of the file for four seconds
*  fade out to black starting from sixty seconds into the video for four seconds
*  XAVC-S codec records in pcm_s16be which is losslessly transcoded to pcm_s16le

 $ ffmpeg -i input -vf vidstabtransform=smoothing=30:interpol=bicubic:input=transforms.trf,unsharp,fade=t=in:st=0:d=4,fade=t=out:st=60:d=4 -c:v libx264 -tune film -preset veryslow -crf 8 -x264opts fast_pskip=0 -c:a pcm_s16le output-stab_final

## x265
Example command showing the defaults when libx265 is invoked without any parameters (Constant Rate Factor encoding):

 $ ffmpeg -i input -c:v libx265 -crf 28 -preset medium -c:a libvorbis output.mp4

See FFmpeg H.265/HEVC Video Encoding Guide for more information.

## Single-pass MPEG-2 (near lossless)
Allow FFmpeg to automatically set DVD standardized parameters. Encode to DVD MPEG-2 at ~30 FPS:

 $ ffmpeg -i video.VOB -target ntsc-dvd output.mpg

Encode to DVD MPEG-2 at ~24 FPS:

 $ ffmpeg -i video.VOB -target film-dvd output.mpg

## Subtitles
## Extracting
Subtitles embedded in container files, such as MPEG-2 and Matroska, can be extracted and converted into SRT, SSA, WebVTT among other subtitle formats * Inspect a file to determine if it contains a subtitle stream:

*  has an embedded SSA subtitle which can be extracted into an independent file:

 $ ffmpeg -i foo.mkv foo.ssa

Add  to save subtitles in desirable format, e.g. SubRip:

 $ ffmpeg -i foo.mkv -c:s srt foo.srt

When dealing with multiple subtitles, you may need to specify the stream that needs to be extracted using the  parameter:

 $ ffmpeg -i foo.mkv -map 0:2 foo.ssa

## Transcribing audio
[https://ffmpeg.org/ffmpeg-filters.html#whisper-1 whisper is not configured in , so we will need either  or  and one of the whisper models from the AUR which install in .

Vad models, used to better detect when someone is talking in a microphone stream, are not currently packaged, so use download-vad-model.sh.

Models are multilingual unless the model name includes . Models ending in  are quantized (require less memory and disk space and depending on the hardware can be processed more efficiently). Models ending in  support local diarization (marking of speaker turns) using tinydiarize. More information about models is available upstream (openai/whisper). $ ffmpeg -i input.mp4 -vn -af "whisper=model=/usr/share/whisper.cpp-model-large-v3/ggml-large-v3.bin\
 :language=en\
 :queue=3\
 :destination=output.srt\
 :format=srt" -f null -

## Hardsubbing
(instructions based on [https://trac.ffmpeg.org/wiki/HowToBurnSubtitlesIntoVideo HowToBurnSubtitlesIntoVideo at the FFmpeg wiki)

Hardsubbing entails merging subtitles with the video. Hardsubs cannot be disabled, nor language switched or the font size customized, therefore considered as discouraged sometimes. In case of doubt use SoftSubs instead of HardSubs.

* Overlay  with the subtitles in :

 $ ffmpeg -i foo.mpg -vf subtitles=foo.ssa out.mpg

## Volume gain
Volume gain can be modified through ffmpegs filter function. First select the audio stream by using  or , then select the volume filter followed by the number that you want to change the stream by. For example:

 $ ffmpeg -i input.flac -af volume=1.5 ouput.flac

Here  provides a 150% volume gain, instead of 1.5 use for example 0.5 to half the volume. The volume filter can also take a decibel measure, use  to increase the volume by 3dB or  to decrease it by 3dB.

## Volume normalization
A given average and peak volume can also be achieved through normalization using the loudnorm filter. To normalize the perceived loudness of a file using fmpegs default values for target average, peak and range loudness (respectively -24 LUFS, -2 dBTP and 7 LU), use:

 $ ffmpeg -i input.flac -af loudnorm output.flac

To obtain a different loudness profile, use the ,  and  parameters of the filter to indicate respectively the integrated, true peak and loudness range. For example for a higher perceived loudness than the default, use:

 $ ffmpeg -i input.flac -af loudnorm=i=-16:tp=-1.5:lra=11:print_format=summary output.flac

In this example,  is also added to display the input and output loudness values of the audio file.

## Extracting audio
Extract the first () AC-3 encoded audio stream exactly as it was multiplexed into the file:

 $ ffmpeg -i video.mpg -map 0:1 -acodec copy -vn video.ac3

Convert the third () DTS audio stream to an AAC file with a bitrate of 192 kb/s and a sampling rate of 96000 Hz:

 $ ffmpeg -i video.mpg -map 0:3 -acodec aac -b:a 192k -ar 96000 -vn output.aac

 disables the processing of the video stream.

Extract audio stream with certain time interval:

 $ ffmpeg -ss 00:01:25 -t 00:00:05 -i video.mpg -map 0:1 -acodec copy -vn output.ac3

 specifies the start point, and  specifies the duration.

## Stripping audio
# Copy the first video stream () along with the second AC-3 audio stream ().
# Convert the AC-3 audio stream to two-channel MP3 with a bitrate of 128 kb/s and a sampling rate of 48000 Hz.

 $ ffmpeg -i video.mpg -map 0:0 -map 0:2 -vcodec copy -acodec libmp3lame \
 -b:a 128k -ar 48000 -ac 2 video.mkv

## Splitting files
You can use the  codec to perform operations on a file without changing the encoding. For example, this allows you to easily split any kind of media file into two:

 $ ffmpeg -i file -t 00:05:30 -c copy part1 -ss 00:05:30 -c copy part2

## Hardware video acceleration
Encoding/decoding performance may be improved by using hardware acceleration API's, however only a specific kind of codec(s) are allowed and/or may not always produce the same result when using software encoding.

## VA-API
VA-API can be used for encoding and decoding on Intel iGPUs and their dedicated Arc GPUs (requires  for newer Intel dedicated GPUs and iGPUs or  for older iGPUs) and on certain AMD GPUs when using the open-source AMDGPU driver (requires ).
See the FFmpeg documentation for information about available parameters and supported platforms.

An example of encoding using the supported H.264 codec:

 $ ffmpeg -threads 1 -i file.ext -vaapi_device /dev/dri/renderD128 -vcodec h264_vaapi -vf format='nv12|vaapi,hwupload' output.mp4

For a quick reference, a constant quality encoding can be achieved with:

 $ ffmpeg -vaapi_device /dev/dri/renderD128 -i input.mp4 -vf 'format=nv12,hwupload' -c:v hevc_vaapi -f mp4 -rc_mode 1 -qp 25 output.mp4

If using hevc_vaapi, tune -qp between 25 (visually identical) and more (28 starts to have very small visual loss). If using h264_vaapi, tune between 18 (visually identical) and more (20 starts to have very small visual loss). Also, hevc_vaapi seems to encode 50% faster than h264_vaapi.

## NVIDIA NVENC/NVDEC
NVENC and NVDEC can be used for encoding/decoding when using the proprietary NVIDIA driver with the  package installed. Minimum supported GPUs are from 600 series, see Hardware video acceleration#NVIDIA for details.

This old gist provides some techniques. NVENC is somewhat similar to CUDA, thus it works even from terminal session. Depending on hardware NVENC is several times faster than Intel's VA-API encoders.

To print available options execute ( may also be available):

 $ ffmpeg -help encoder=h264_nvenc

Example usage:

 $ ffmpeg -i source.ext -c:v h264_nvenc -rc constqp -qp 28 output.mkv

## Intel QuickSync (QSV)
Intel® Quick Sync Video uses media processing capabilities of an Intel GPU to decode and encode fast, enabling the processor to complete other tasks and improving system responsiveness.

This requires a libmfx runtime implementation to be installed. libmfx is a dispatcher library that loads an implementation at runtime based on the underlying hardware platform.

When running under Iron Lake (Gen5) to Ice Lake (Gen10) GPUs, it will load  as the runtime implementation.

When running under Tiger Lake (Gen11) and newer GPUs, libmfx will load . See also the vpl-gpu-rt system-requirements.

The runtime implementation cannot be changed or chosen on systems with a single Intel GPU, and the corresponding implementation should be installed following the hardware where it will run.

Failure to install said runtime will result in errors like the following:

 @ 0x558283838c80 Error initializing an MFX session: -3.
 Device creation failed: -1313558101.

The usage of QuickSync is described in the FFmpeg Wiki. It is recommended to use VA-API with either the iHD or i965 driver instead of using libmfx directly, see the FFmpeg Wiki section Hybrid transcode for encoding examples and Hardware video acceleration#Configuring VA-API for driver instructions.

## AMD AMF
AMD added support for H264 only video encoding on Linux through AMD Video Coding Engine (GPU encoding) with the proprietary additions to the open driver, and ffmpeg added support for AMF video encoding, so in order to encode using the h264_amf video encoder,  is required. You may need to link to the ICD file provided by the proprietary package as a variable or ffmpeg could use the open AMDGPU's ICD file and not be able to use this video encoder. An example of a command for encoding could be as follows:

 $ VK_DRIVER_FILES=/usr/share/vulkan/icd.d/amd_pro_icd64.json ffmpeg -hwaccel auto -vaapi_device /dev/dri/renderD128 -i input.mkv -c:v h264_amf -rc 1 -b:v 8M h264_amf_8M.mp4

For a quick reference, a constant quality encoding can be achieved with:

 $ VK_DRIVER_FILES=/usr/share/vulkan/icd.d/amd_pro_icd64.json ffmpeg -hwaccel auto -vaapi_device /dev/dri/renderD128 -i input.mp4 -c:v h264_amf -f mp4 -rc 0 -qp_b 22 -qp_i 22 -qp_p 22 -quality 2 output.mp4

Tune the three -qp_(b|i|p) together being 18 visually identical and 22 starting to have very small visual loss.

## Animated GIF
Whilst animated GIFs are generally a poor choice of video format due to their poor image quality, relatively large file size and lack of audio support, they are still in frequent use on the web. The following command can be used to turn a video into an animated GIF:

 $ ffmpeg -i input.mp4 -vf "fps=10,split[s0-loop -1 output.gif

See https://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html for more information on using the palette filters to generate high quality GIFs.

## Preset files
Populate  with the default [https://ffmpeg.org/ffmpeg.html#Preset-files preset files:

 $ cp -iR /usr/share/ffmpeg ~/.ffmpeg

Create new and/or modify the default preset files:

## Using preset files
Enable the  option after declaring the desired

## libavcodec-vhq.ffpreset
*  = Name of the vcodec/acodec
*  = Name of specific preset to be called out
*  = FFmpeg preset filetype suffix

## Tips and tricks
## Reduce verbosity
Use a combination of the following options to reduce verbosity to the desired level:

* : prevents ffmpeg from outputting its copyright notice, build options and library versions
* : modulates verbosity (fine-tuning options are available), e.g.
* : disables printing of encoding progress/statistics

The environment variable , which defaults to 3 (, quite verbose), can be used to silence output from  () that is entirely unaffected by any of the above options. Alternatively,  can be used to redirect the output into a separate file if desired.=== Output the duration of a video ===

 $ ffprobe -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 file.ext

## Output stream information as JSON
 $ ffprobe -v quiet -print_format json -show_format -show_streams file.ext

## Create a screen of the video every X frames
 $ ffmpeg -i file.ext -an -s 319x180 -vf fps=1/100 -qscale:v 75 %03d.jpg

## Modify metadata
FFmpeg cannot directly modify metadata in one command, but you can still manually extract and reapply the properties.

Extract existing (global) metadata into a textfile:

 $ ffmpeg -i 'song.mp3' -f ffmetadata song_metadata.txt

Create new file with metadata from a textfile:

 $ ffmpeg -i 'song.mp3' -f ffmetadata -i new_metadata.txt -map_metadata 1 -id3v2_version 4 song_new.mp3

 tells ffmpeg to use the metadata from the 2nd file (index start at 0).

Next to global metadata each stream can have own metadata as well, export e.g. with  and .

ffprobe (from  as well) offers more export formats: default, compact/csv, flat, ini, json and xml.

## Reduce conversion artifacts
Occasionally, when converting video between codecs (e.g h264 to AV1), you may get slight artifacts despite the source file having none. Many codecs have preset options, controlling quality at the cost of higher compute time when encoding.[https://ffmpeg.org/ffmpeg-codecs.html Changing the preset to a value with higher quality may eliminate those artifacts.

For e.g :

 -svtav1-params preset=5
