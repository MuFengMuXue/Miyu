# CUE Splitting

This article describes how to split audio files using CUE metadata.

## Installation
To split audio files you need . To split CD images in ISO or raw format you need .

The WAV format is supported natively for both input and output. To decode or encode files in other format you need an appropriate decoder. For example: , , or .

To tag audio files you need extra tools, such as , , or . Alternatively,  can be used for more advanced tagging needs, including importing from the MusicBrainz database for example.

## Splitting
To split an audio file accompanied by a CUE sheet into tracks in .wav format, use the shnsplit command:

 $ shnsplit -f file.cue file.wav

To split .bin file with CUE sheet into tracks in .wav format:

 $ bchunk -v -w file.bin file.cue out

Format for output file names can be specified with the  option ( for performer,  for album,  for title, and  for track number):

 $ shnsplit -f file.cue -t "%n %t" file.wav

shnsplit supports on-the-fly encoding to many lossless formats (see  for the full list). For example to encode split tracks in the FLAC format:

 $ shnsplit -f file.cue -o flac file.flac

Encoding options, including the encoder itself, can be specified with the  parameter (see  for details):

 $ shnsplit -f file.cue -o "flac flac -s -8 -o %f -" file.flac

The formats supported by shntool and default encoder options can be view with the  command. If the desired format is not supported by shntool, it can be specified manually. For example, to encode split tracks directly into the Ogg Vorbis format:

 $ shnsplit -f file.cue -o "cust ext=ogg oggenc -b 192 -o %f -" file.ape

This process can be applied to any other encoder, such as  or , by specifying standard input (usually ) as the source and  as the destination. See the encoder's man page for details.

## Tagging
You will need  to use cuetag.sh.

To copy the metadata from a CUE sheet to the split files you can use:

 $ cuetag.sh file.cue *.mp3

or if you need to select only certain files:

 $ cuetag.sh file.cue track01.mp3 track02.mp3 track03.mp3 track04.mp3

cuetag.sh supports id3 tags for .mp3 files and vorbis tags for .ogg and .flac files.

## Alternatives
* This is a script that splits and converts files to tagged FLAC: https://bbs.archlinux.org/viewtopic.php?id=75774.
* You may also use  or , a graphical Qt program that splits, converts and tags album audio files into song audio files. It also features automatic character set detection for CUE files.
* To avoid quality loss from transcoding mp3 files,  or  may be used to directly split mp3 files either manually or automatically with a provided cuesheet. Batch mode processing is also available.
