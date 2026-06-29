# MEncoder

An overview of MEncoder, the video encoding/decoding tool provided by MPlayer as part of the  package.

## Basics
The basic syntax for a conversion is:

 $ mencoder original_video.mpg -o new_video.avi -ovc output_video_codec -oac output_audio_codec

This is basically how one converts a video. However, there are many more options available.

For input formats, MEncoder can use any format that MPlayer can play, so to verify whether it will work with your video, just try playing it in MPlayer.

To list output video codecs, run:

 $ mencoder -ovc help

Similarly, to list output audio codecs, run:

 $ mencoder -oac help

This information can also be found in the project online documentation where it is better explained, although non-specific.

## Example
This approach allows one to make a .mkv file with an H.264-encoded video and any number of Vorbis-encoded audio tracks.

We will use mencoder for ripping and encoding and mkvmerge (part of ) for making the .mkv file itself.

## Ripping and encoding the video
The H.264 encoder is usually used in two passes: the first reads information about the movie, the second uses that information to encode. We will not extract any audio for now.

Commands follow; remember to replace the variables with the proper values:

First pass: we are just collecting information, so the normal output is thrown away:

Second pass: here we compress the video track using the information from the first step:

This will create a  file containing the video. You can play with the  options and the  filters to improve the quality or reduce the file size. For example, a movie with a black border should be cropped with  with the proper values instead of  and  (see ). You may want to scale down the movie with  the width of the movie will become  (keep  a multiple of 16: 640, 480, or 320 are usually fine), the height will be correctly calculated in order to keep the aspect ratio.

You can also use any other of the filters MEncoder has to offer, like  or you can change the frame rate using . (If you do so, remember to use the same frame rate everywhere including in the commands to rip audio.)

It is important that you use  as the last filter: it will force MEncoder to write every frame (even duplicate ones) in the output. Also, it is necessary to use } with  as  to keep the original width or a new, usually smaller, width: it is necessary since the H.264 codec uses square pixels and DVDs instead use rectangular pixels.

## Ripping and encoding the audio
You can extract audio tracks as needed. Here we compress with the Vorbis algorithm, but you may want to check the MEncoder manual in order to see alternatives.

The command follows (replace the variables with desired values) where we rip and compress the audio:

 $ mencoder -dvd-device "$ISO" dvd://"$TITLE" -alang "$AUDIOLANG" -chapter "$CHAPTER" -ovc frameno \
 -oac lavc -lavcopts acodec=vorbis:abitrate=224 -channels 2 -srate 48000 -o "$AUDIOLANG".avi

You should repeat the command for every audio track you want, so we will have .avi files with the audio track.

You may also want to use  to exact all the channels of a 5.1 DVD or changing the bit rate. As with the video, you can use audio filters via  but it is not necessary.

## Making the final .mkv file
Putting it all together in a single file is simple. Add other audio tracks if needed:

 $ mkvmerge -D audio.avi -A video.avi -o mymovie.mkv

The .mkv file will contain everything, so you can store your movie keeping all the audio track you want. Even if you are not interested in keeping multiple sound tracks, the H.264/Vorbis format pair should ensure great quality.

## Encoding for Nokia 5800 XM and Nokia N97
In 2 passes with small bitrates (640kbps video vbitrate and 96kbps audio abitrate) yields pretty watchable video mp4 for Nokia 5800 xm and Nokia N97 phones' default video player.

## mkv to mp4 (nokia 97, 5800 compatible)
# convert the mkv to mpg ; many mkv files do not directly get converted to mp4:
# convert the mpg file to mp4:
#delete the temporary huge sized mpg file:

Here  is the first audio track in the original mkv.

## avi to mp4 (nokia 97, 5800 compatible) using multipass (2 passes)
# First pass:
# Second pass:

Play around with abitrate, vbitrate, and scale values to get video quality and size of your liking.

 will try to keep the video width to 640 and resize the video height accordingly. Do use the "original" aspect in Nokia's mp4 player Option > aspect for 16:9 and 4:3 aspect ratio videos.

## Encoding a multi audio / multi language MKV video to an MP4 with different audio streams
To encode multi-audio file to mp4 we need to use the  like  in ffmpeg.

# To extract video+audio stream1 (e.g. english) of mkv file:
# To extract video+audio stream2 (e.g. Hindi, French, etc.) of mkv file:

## Adding SubRip subtitles to a file
The following output video codec () options are suggested as very high-quality settings and should suffice for most transcoding, including the addition of subtitles to a stream.

## Two-pass x264 (very high-quality)
*  is a maximum quality  preset option.
*  is the only other major option undefined by  settings.
*  values can be modified to suit desired file size and quality needs.
*  should be set to match the type and content of the media being encoded.

## Single-pass x264 (very high-quality)
* The following example uses the option  to mux the output into a Matroska container which is autodetected from the output file extension .mkv:
*  writes global video headers to extradata, or in front of keyframes and is typically required for .mp4 and .mkv containers.

## Two-pass xvid (very high-quality)
*  where n = physical, or CPU cores.
* Recent versions of mencoder enable  as a default setting.
* Xvid does not accept  settings on the first of multiple-pass encodings.
*  helps with proper sizing with 16:9 format screens.
*  can be set so long as the bitrate is high enough.

## Three-pass lavc (very high-quality mpeg4)
* Introducing  (with n above 1) for  may skew the effects of motion estimation and lead to reduced video quality and compression efficiency.
*  to  can reduce encoding times without incurring much loss in quality.
*  not included as referenced in the official mencoder documentation as the current default setting is to not to use B-frames at all.
*  not included as referenced in the official mencoder documentation for the same reason as above. Else .

## Single-pass lavc (very high-quality mpeg-2)
*  to ensure A/V sync
*  - setting video aspect manually
* subtitle background, subtitle encoding and subtitle scaling

There are as always many options that can be set, this combination ensures that picture looks almost the same as original with slightly smaller file size (great for converting FULL HD videos so that they are playable on older devices).

## Adding VOBsub subtitles to a file
## Two-pass x264 (very high-quality)
* Direct  to the  using the full pathname of the file without extensions (.idx or .sub).
* Select the second subtitle ID language () contained within the VOBsub files (.idx or .sub).

## Testing subtitle muxing results
Avoid passing resource intensive encoding options in order to verify desired results sooner rather than later.

## Single-pass x264 (low quality)
## mp2 vs. mp3lame vs. aac
*  is recommended over FFmpeg lavc (libavcodec) for mp2 encoding.
* mp3lame is recommended over FAAC (not fully developed) encoding at all bitrates.

## Encoding AVI videos in Windows and Mac readable formats
Use these commands:

 $ opt="vbitrate=2160000:mbd=2:keyint=132:vqblur=1.0:cmp=2:subcmp=2:dia=2:mv0:last_pred=3"
 $ mencoder -ovc lavc -lavcopts vcodec=msmpeg4v2:vpass=1:$opt -oac mp3lame -o /dev/null input.avi
 $ mencoder -ovc lavc -lavcopts vcodec=msmpeg4v2:vpass=2:$opt -oac mp3lame -o output.avi input.avi

 is the AVI you made using Linux utilities, and "output.avi" is the AVI you want to make which will be readable by Windows and Mac users.

## GUI frontends
The official MPlayer homepage has a comprehensive list of available front-ends here.

*
*
*
*
