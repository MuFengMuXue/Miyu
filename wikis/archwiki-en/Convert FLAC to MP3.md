# Convert FLAC to MP3

This article outlines different ways to transcode from FLAC to MP3. FLAC is a lossless audio format, so it is better for archival purposes, but it also takes up more disk space. The idea is to compress the files without creating a perceived loss in fidelity.

## Packages
*  - Transcode between different formats and keep tags with , can encode from CDDA with , has an optional Ncurses GUI.
*  - Multi-threaded conversion of flac to 70+ other formats retaining all tags and metadata.
*  - A small Python script that accepts a list of directories containing FLAC files as arguments and converts them to MP3 with the specified options.

## Graphical applications
*
*
*

## Usage
In these two examples, FLAC files in current directory are encoded by the LAME MP3 encoder. Both scripts pass the ID3 tags from the FLAC files to the resulting MP3 files, and encode to MP3 V0. V0 results in a variable bitrate usually between 220-260 kbps. The audio of a V0 file is transparent, meaning one cannot tell the difference between the lossy file and the original source (compact disc/lossless), but yet the file size is significantly reduced. For more information on LAME switches/settings such as V0, visit the Hydrogenaudio LAME Wiki.

The original  files are not modified and the resulting s will be in the same directory. All files with extensions not matching  in the working directory (, images, , etc.) are ignored.

For ease of use, add the script to your . Open up a terminal,  to the directory of FLAC files that you wish to convert, and invoke  (or whatever you named the script). You will see the verbose decoding/encoding process in the terminal which may take a few moments. Done! At this point, it is trivial to  all your new MP3s wherever you wish.

## With FFmpeg
Chances are, your system already has FFmpeg installed, which brings in the  and  packages. FFmpeg has all the encoding and decoding facilities built in to do the job.

## Without FFmpeg
If for some reason FFmpeg is not installed and you do not want to install it, you still need to have  and  installed. Here, the tagging process is more explicit using the metadata utility that comes with  and passing the information to . The process duration will slightly increase since FLACs must first be decoded to WAVE and then fed into the MP3 encoder.

{{bc|
#!/bin/bash

for a in ./*.flac; do
  # give output correct extension
  OUTF="${a@/%flac/mp3}"

  # get the tags
  ARTIST=$(metaflac "$a" --show-tag=ARTIST | sed s/.*=//g)
  TITLE=$(metaflac "$a" --show-tag=TITLE | sed s/.*=//g)
  ALBUM=$(metaflac "$a" --show-tag=ALBUM | sed s/.*=//g)
  GENRE=$(metaflac "$a" --show-tag=GENRE | sed s/.*=//g)
  TRACKNUMBER=$(metaflac "$a" --show-tag=TRACKNUMBER | sed s/.*=//g)
  DATE=$(metaflac "$a" --show-tag=DATE | sed s/.*=//g)

  # stream flac into the lame encoder
  flac -c -d "$a" | lame -V0 --add-id3v2 --pad-id3v2 --ignore-tag-errors \
    --ta "$ARTIST" --tt "$TITLE" --tl "$ALBUM"  --tg "${GENRE:-12}" \
    --tn "${TRACKNUMBER:-0}" --ty "$DATE" - "$OUTF"
done
}}

## Recursively
A useful extension of the above scripts is to let them recurse into all subdirectories of the working directory. To do so, replace the first line () with:

 find -type f -name "*.flac" -print0 | while read -d $'\0' a; do
