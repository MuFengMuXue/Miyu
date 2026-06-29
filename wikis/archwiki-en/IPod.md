# IPod

The iPod is a discontinued series of portable media players created by Apple Inc. Officially, you can only add music to iPods using Apple's iTunes program, but there are several other programs that are able to sync music with an iPod.

## Accessing the storage
Traditional iPods are accessed just like a normal USB storage device containing a vfat or hfsplus file system. See the USB storage devices article for detailed instructions on how to access your device.

## Library management
These tools use the  library:

*
*
*
*
*

## Converting video for devices
## Handbrake
Handbrake is a nifty tool with presets for a variety of iPod versions. CLI and GTK versions are available with the  and  packages respectively.

If you do decide to take the CLI way, a good guide is available at https://handbrake.fr/docs/en/latest/cli/command-line-reference.html.

## Avidemux
Install the  package.

This can convert to mp4 files. If you enforce a hard max of bit rate @ 700ish and keep the video size to 720×480 or 320×240 then it works fine for video file exporting.

## Mencoder
Install the  package.

Has extremely comprehensive configuration support, which will be able to spit out iPod-compatible video files. Check out ; a lot of MPlayer opts will also affect encoding.

A basic guide is also available at MEncoder.

An example command to encode iPhone/iPod Touch-compatible video:

 $ mencoder INPUT -o output.mp4 \
 -vf scale=480:-10,harddup \
 -oac faac -faacopts mpeg=4:object=2:raw:br=128 \
 -of lavf -lavfopts format=mp4 \
 -ovc x264 -x264encopts nocabac:level_idc=30:bframes=0

## FFmpeg
Install the  package.

Another encoder with comprehensive configuration support. Example command to encode for 5G iPod:

 $ ffmpeg -vcodec xvid -b 300 -qmin 3 -qmax 5 -bufsize 4096 \
 -g 300 -acodec aac -ab 96 -i INPUT -s 320x240 \
 -aspect 4:3 output.mp4

or iPod Touch/iPhone compatible video output:

 $ ffmpeg -f mp4 -vcodec mpeg4 -maxrate 1000 -b 700 -qmin 3 -qmax 5\
 -bufsize 4096 -g 300 -acodec aac -ab 192 -s 480×320 -aspect 4:3 -i INPUT output.mp4

## Device specific
## iPhone/iPod Touch
## Generating HashInfo file
If you have never synced your device using iTunes, you will get error messages telling you that the HashInfo file is missing. This can be fixed by syncing once with iTunes in order to create it.
Alternatively one can create this file using the site https://ihash.marcan.st/  Enter the serial number of the iPod on the website. It will generate a file named  which you will place under the  directory. Unplug the iPod device and plug it back.

## Unobfuscating the Database
Since firmware version 2.0, Apple has obfuscated the music database. If you are using recent firmware, the file  can be modified to enable use of the older, non-obfuscated database. If that file does not exist then try to copy from  to  then replace:
 DBVersion
 4
with:
 DBVersion
 2
Then reboot your device.

If syncing fails with , you may need to leave this at 4. libgpod seems to expect a hashed database.

## iPod Classic/Nano (3rd generation)
You need to set up the iPod to make libgpod able to find its Firewire ID. For this, you will need to get your FireWire ID manually

# Mount the iPod as a rw mount point. In the following example, use .
# Find the serial number by typing  this should print a 16 character long string like  (it will have no colons or hyphens)
# Once you have that number, create or edit . Add to that file the line below:  (replace  with the 16 digit string you obtained at the previous step and do not forget the leading  before the string)

Your iPod can now be managed with Amarok or gtkpod.

## iPod Nano 5th generation
Follow the instructions above #Generating HashInfo file in order to set up the hash file, it is needed to write into the device music library.
To be able to use the iPod Nano 5th gen with , a  file is also needed to be placed in the directory . It can be generated using:

 # ipod-read-sysinfo-extended bus device mountpoint

for example:

 # ipod-read-sysinfo-extended 001 011 /mnt/ipod/

## iPod Nano 6th generation
By default libgpod does not seem to be able to synchronize on a iPod Nano 6th generation. It copies data, but as soon as USB is disconnected, everything is as before. The package  fixes this.
Additionally, the  file is also required, and can be generated in the same fashion as in #iPod Nano 5th generation, however a  file is unnecessary on this model.

## iPod Shuffle 1st and 2nd generation
rebuild_db is a Python 2 script that makes it possible to use the iPod Shuffle almost like any other USB flash MP3 player. Download the script from the website, then place it in the iPod's root directory. Copy your MP3 files onto the iPod Shuffle (sub-folders are allowed too) and then run the script:

 $ python2 /mnt/iPod/rebuild_db.py

## iPod Shuffle 4th generation
In order to use this version of the iPod Shuffle under linux, you can use the python based command line tool . It also provides advanced voiceover and (auto)playlist generation support.

## iPod Video (5th and 5.5th generation)
iPods in the mainline series up to and including this model do not support the AAC PNS feature, and will display audible artifacts when encountering it. Disable the feature in  when encoding AAC files for these devices.

 $ ffmpeg -i input.ogg -c:a aac -b:a 256k -aac_pns 0 -movflags +faststart -vn output.m4a

The  options place the moov atom at the start of the file, which helps the iPod parse the file faster.
