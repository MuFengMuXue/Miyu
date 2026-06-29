# Optical disc drive

From Wikipedia:

:In computing, an optical disc drive (ODD) is a disc drive that uses laser light or electromagnetic waves within or near the visible light spectrum as part of the process of reading or writing data to or from optical discs. Some drives can only read from discs, but recent drives are commonly both readers and recorders, also called burners or writers. Compact discs, DVDs, and Blu-ray discs are common types of optical media which can be read and recorded by such drives. Optical drive is the generic name; drives are usually described as "CD" "DVD", or "Blu-ray", followed by "drive", "writer", etc.

## Burning
The burning process of optical disc drives consists of creating or obtaining an image and writing it to an optical medium. The image may in principle be any data file. If you want to mount the resulting medium, then it is usually an ISO 9660 file system image file. Audio and multi-media CDs are often burned from a .bin file, under control of a .toc file or a .cue file which tell the desired track layout.

## Install burning utilities
If you want to use programs with graphical user interface, then follow #Burning CD/DVD/BD with a GUI.

The programs listed here are command line oriented. They are the back ends which are used by most free GUI programs for CD, DVD, and BD. GUI users might get to them when it comes to troubleshooting or to scripting of burn activities.

You need at least one program for creation of file system images and one program that is able to burn data onto your desired media type.

Available programs for ISO 9660 image creation are:

*  from
*  and  from

The traditional choice is mkisofs, because it is the older one.

Available programs for burning to media are:

*  from  (CD only, TOC/CUE/BIN only)
*  from
*  from
*  from  (DVD and BD only)
*  and  from

The traditional choices are cdrecord for CD and growisofs for DVD and Blu-ray Disc,
because cdrecord was first to offer CD writing without description file and growisofs was
first to offer writing to DVD and BD without artificial restrictions by the burn program.
For writing TOC/CUE/BIN files to CD, install .

The free GUI programs for CD, DVD, and BD burning depend on at least one of the above packages.

xorrisofs supports the mkisofs options which are shown in this document.

cdrskin supports the shown cdrecord options; xorrecord also supports those which do not deal with audio CD.

## Making an ISO image from existing files
The simplest way to create an ISO image is to first copy the needed files to one directory, for example: .

Then generate the image file with mkisofs:

 $ mkisofs -V "ARCHIVE_2013_07_27" -J -r -o isoimage.iso ./for_iso

Each of those options are explained in the following sections.

## Basic options
;: Specifies the name (that is assigned to) of the file system. The ISO 9660 standard specs impose the limitations of 32-character string length, as well as limiting the characters allowed to sets of: "A" to "Z", "0" to "9", and "_". This volume label will probably show up as mount point if the medium is mounted automatically.
;: Enables Joliet extension, which allocates special space to store file names in Unicode (up to 64 UTF-16 characters for each file).
;: Increases maximum length of file names from 64 to 103 UTF-16 characters in Joliet table. Non-compliant to Joliet specs and not commonly supported.
;: Enables Rock Ridge extension, which adds POSIX file system semantics to an image, including support of long 255-character filenames and Unix-style file permissions.
;: Sets the file path for the resulting ISO image.

## graft-points
It is also possible to let mkisofs to collect files and directories from various paths

 $ mkisofs -V "BACKUP_2013_07_27" -J -r -o backup_2013_07_27.iso \
   -graft-points \
   /photos=/home/user/photos \
   /mail=/home/user/mail \
   /photos/holidays=/home/user/holidays/photos

 enables the recognition of pathspecs which consist of a target address in the ISO file system (e.g. ) and a source address (e.g. ). Both are separated by a "=" character.

So this example puts the directories ,  and , respectively in the ISO image as ,  and .

Programs mkisofs and xorrisofs accept the same options. For secure backups, consider using xorrisofs with option , which records eventual ACLs and stores an MD5 checksum for each data file.

See the  and  man pages for more info about their options.

## Mounting an ISO image
You can mount an ISO image if you want to browse its files.
To mount the ISO image, we can use:

 # mount -t iso9660 -o ro,loop /path/to/file.iso /mount-point

Do not forget to unmount the image when your inspection of the image is done:

 # umount /mount-point

See also Mounting images as user for mounting without root privileges.

## Converting img/ccd to an ISO image
To convert an / image, you can use :

 $ ccd2iso ~/image.img ~/image.iso

## Learning the name of your optical drive
For the remainder of this section the name of your recording device is assumed to be .

Check this by

 $ cdrecord dev=/dev/sr0 -checkdrive

which should report  and  fields of the drive.

If no drive is found, check whether any  exist and whether they offer read/write permission () to you or your group.
If no  exists then try loading module  manually.

## Reading the volume label of a CD or DVD
If you want to get the name/label of the media, use dd:

 $ dd if=/dev/sr0 bs=1 skip=32808 count=32

## Creating an ISO image from a CD, DVD, or BD
In order to only copy actual data from the disc and not the empty blocks filling it up, first retrieve its block/sector count and size (2048 most of the time):

or alternatively:

Then use dd to copy the data using the obtained values:

 $ dd if=/dev/sr0 of=discmage.iso bs=sector_size count=sector_count status=progress

If the original medium was bootable, then the copy will be a bootable image. You may use it as a pseudo CD for a virtual machine or burn it onto an optical medium which should then become bootable. === Using dvdisaster to create error recovery data ===

 or  is a tool, that adds error correction data to optical media. This data can help recover content from scratched or damaged discs.

# Insert the CD, DVD, or Blu-ray Disc into your optical drive.
# Make sure the disc is not mounted. You can unmount it using:
# Run dvdisaster from the command line or find it in your application menu.
# In the dvdisaster interface, choose Create error correction data.
# Select the disc type (CD/DVD/BD) from the drop-down menu.
# Click the Load Disc button to scan the contents of your optical media.
# dvdisaster will analyze the disc and display its structure.
# Choose a location where the error recovery (ECC) file will be saved.
# Set the error correction level. Higher levels provide better recovery at the cost of larger ECC file sizes.
# Click Generate to begin creating the error correction data.
# The process may take several minutes depending on the size of your disc.
# Once the ECC file is created, dvdisaster will prompt you to verify the file.
# Save both the original disc image (ISO) and the ECC file for future use.
# It is recommended to store your ISO and ECC files on multiple devices or cloud storage for maximum safety.

To get the best results:

* Use high-quality discs for creating backups.
* Store your ECC files alongside ISO images for easy recovery.
* dvdisaster can work in conjunction with ISO files without needing the original disc.

## Rebuilding damaged discs using dvdisaster
If your optical disc becomes scratched or otherwise damaged, dvdisaster can help recover lost data using an error correction (ECC) file.

# Insert the damaged CD, DVD, or Blu-ray Disc into your optical drive.
# Unmount the disc to avoid conflicts:
# Start dvdisaster
# In the dvdisaster interface, choose Scan and Repair mode.
# Load the damaged disc by selecting the drive from the dropdown menu or using the Load Disc button.
# Click Load ECC to select the corresponding error correction file (usually ) created when you first burned the disc.
# Ensure the ECC file matches the exact disc structure. If you do not have a matching ECC file, this method will not work.
# Click Scan to begin reading the disc and identifying damaged sectors.
# dvdisaster will display a visual representation of the disc’s status, showing good, unreadable, and corrected sectors.
# Once scanning is complete, click Repair to rebuild missing or corrupt data using the ECC file.
# The recovered data will be written to a new ISO image file.
# Choose a destination to save the rebuilt ISO image. Example:
# Click Save to complete the process.
# Mount the ISO to verify that files have been successfully recovered:
# Check the contents at  to ensure data integrity.

To get the best results:

* Use a reliable optical drive that reads damaged discs well.
* Ensure the ECC file is stored safely with your ISO backups.
* If recovery fails, clean the disc and attempt to scan again.

## Erasing CD-RW and DVD-RW
Used CD-RW media need to be erased before you can write over the previously recorded data. This is done by

 $ cdrecord -v dev=/dev/sr0 blank=fast

There are two options for blanking:  and . Full blanking lasts as long as a full write run. It overwrites the payload data on the CD. Nevertheless this should not be considered as securely making those data unreadable. For that purpose, several full write runs with random data are advised.

Alternative commands are:

 $ cdrskin -v dev=/dev/sr0 blank=fast
 $ xorriso -outdev /dev/sr0 -blank as_needed

To erase the DVD-RW use the dvd+rw-format utility from :

 $ dvd+rw-format -blank=fast /dev/sr0

Alternative commands are:

 $ cdrecord -v dev=/dev/sr0 blank=fast
 $ cdrskin -v dev=/dev/sr0 blank=deformat_sequential_quickest
 $ xorriso -outdev /dev/sr0 -blank deformat_quickest

Such fastly blanked DVD-RW are not suitable for multi-session and cannot take input streams of unpredicted length. For that purpose one has to use one of:

 $ cdrecord -v dev=/dev/sr0 blank=all
 $ dvd+rw-format -blank=full /dev/sr0
 $ cdrskin -v dev=/dev/sr0 blank=as_needed
 $ xorriso -outdev /dev/sr0 -blank as_needed

The other media types are either write-once (CD-R, DVD-R, DVD+R, BD-R) or are overwritable without the need for erasing (DVD-RAM, DVD+RW, BD-RE).

## Formatting DVD-RW
Formatted DVD-RW media can be overwritten without previous erasure. So consider to apply once in their life time

 $ dvd+rw-format -force /dev/sr0
 $ cdrskin -v dev=/dev/sr0 blank=format_if_needed
 $ xorriso -outdev /dev/sr0 -format as_needed

Unlike DVD-RAM, DVD+RW, and BD-RE, formatted DVD-RW cannot be used as (slow) hard disk directly, but rather need the mediation of driver pktcdvd. See .

## Formatting BD-RE and BD-R
BD-RE need formatting before first use. This is done automatically by the burn programs when they detect the unformatted state. Nevertheless the size of the payload area can be influenced by expert versions of the format commands shown above for DVD-RW.

BD-R can be used unformatted or formatted. Unformatted they are written with full nominal speed and offer maximum storage capacity. Formatted they get checkread during write operations and bad blocks get replaced by blocks from the Spare Area. This reduces write speed to a half or less of nominal speed. The default sized Spare Area reduces the storage capacity by 768 MiB.

growisofs formats BD-R by default. The others do not. growisofs can be kept from formatting. cdrskin and xorriso can write with full nominal speed on formatted BD-RE or BD-R:

  $ growisofs -use-the-force-luke=spare:none ...growisofs.or.mkisofs.options...
  $ cdrskin stream_recording=on ...cdrecord.options...
  $ xorriso -stream_recording on ...xorriso.commands...

## Burning an ISO image to CD, DVD, or BD
To burn a readily prepared ISO image file  onto an optical medium, run for CD:

 $ cdrecord -v -sao dev=/dev/sr0 isoimage.iso

and for DVD or BD:

 $ growisofs -dvd-compat -Z /dev/sr0=isoimage.iso

and for CD, DVD or BD:

 $ xorriso -as cdrecord -v -sao dev=/dev/sr0 isoimage.iso

## Verifying the burnt ISO image
You can verify the integrity of the burnt medium to make sure it contains no errors. Always eject the medium and reinsert it before verifying; it will guarantee that any kernel cache will not be used to read the data.

First calculate the MD5 checksum of the original ISO image:

Next calculate the MD5 checksum of the ISO file system on the medium.
Although some media types deliver exactly the same amount of data as have been submitted to the burn program, many others append trailing garbage when being read. So you should restrict reading to the size of the ISO image file.

 $ blocks=$(expr $(du -b isoimage.iso | awk '{print $1}') / 2048)

Both runs should yield the same MD5 checksum (here: ). If they do not, you will probably also get an I/O error message from the  run. dmesg might then tell about SCSI errors and block numbers, if you are interested.

## ISO 9660 and burning on-the-fly
It is not necessary to store an emerging ISO file system on hard disk before writing it to optical media. Only very old CD drives in very old computers could suffer failed burns due to an empty drive buffer.

If you omit option  from mkisofs then it writes the ISO image to standard output. This can be piped into the standard input of burn programs.

 $ mkisofs -V "ARCHIVE_2013_07_27" -J -r ./for_iso | \
   cdrecord -v dev=/dev/sr0 -waiti -

Option  is not really needed here. It prevents cdrecord from writing to the medium before mkisofs starts its output. This would allow mkisofs to read the medium without disturbing an already started burn run. See next section about multi-session.

On DVD and BD, you may let growisofs operate mkisofs for you and burn its output on-the-fly:

 $ growisofs -Z /dev/sr0 -V "ARCHIVE_2013_07_27" -r -J ./for_iso

## Multi-session
ISO 9660 multi-session means that a medium with readable file system is still writable at its first unused block address, and that a new ISO directory tree gets written to this unused part. The new tree is accompanied by the content blocks of newly added or overwritten data files. The blocks of data files, which shall stay as in the old ISO tree, will not be written again.

Linux and many other operating systems will mount the directory tree in the last session on the medium. This youngest tree will normally show the files of the older sessions, too.

## Multi-session by cdrecord
CD-R and CD-RW stay writable (aka "appendable") if cdrecord option  was used

 $ cdrecord -v -multi dev=/dev/sr0 isoimage.iso

Then the medium can be inquired for the parameters of the next session

 $ m=$(cdrecord dev=/dev/sr0 -msinfo)

By help of these parameters and of the readable medium in the drive you can produce the add-on ISO session

 $ mkisofs -M /dev/sr0 -C "$m" \
    -V "ARCHIVE_2013_07_28" -J -r -o session2.iso ./more_for_iso

Finally append the session to the medium and keep it appendable again

 $ cdrecord -v -multi dev=/dev/sr0 session2.iso

Programs cdrskin and xorrecord do this too with DVD-R, DVD+R, BD-R and unformatted DVD-RW. Program cdrecord does multi-session with at least DVD-R and DVD-RW. They all do with CD-R and CD-RW, of course.

Most re-usable media types do not record a session history that would be recognizable for a mounting kernel. But with ISO 9660 it is possible to achieve the multi-session effect even on those media.

growisofs and xorriso can do this and hide most of the complexity.

## Multi-session by growisofs
By default, growisofs uses mkisofs as a backend for creating ISO images  forwards most of its program arguments to . See above examples of mkisofs. It bans option  and deprecates option . By default it uses the mkisofs. You may specify to use one of the others compatible backend program by setting environment variable :

 $ export MKISOFS="xorrisofs"

The wish to begin with a new ISO file system on the optical medium is expressed by option

 $ growisofs -Z /dev/sr0 -V "ARCHIVE_2013_07_27" -r -J ./for_iso

The wish to append more files as new session to an existing ISO file system is expressed by option

 $ growisofs -M /dev/sr0 -V "ARCHIVE_2013_07_28" -r -J ./more_for_iso

For details see the  manual and the manuals of mkisofs and xorrisofs.

## Multi-session by xorriso
xorriso learns the wish to begin with a new ISO file system from the blank state of the medium. So it is appropriate to blank it if it contains data. The command  applies to all kinds of re-usable media and even to ISO images in data files on hard disk. It does not cause error if applied to a blank write-once medium.

 $ xorriso -outdev /dev/sr0 -blank as_needed \
           -volid "ARCHIVE_2013_07_27" -joliet on -add ./for_iso --

On non-blank writable media xorriso appends the newly given disc files if command  is used rather than . Of course, no command  should be given here

 $ xorriso -dev /dev/sr0 \
           -volid "ARCHIVE_2013_07_28" -joliet on -add ./more_for_iso --

For details see the  man page and especially its examples.

## BD Defect Management
BD-RE and formatted BD-R media are normally written with enabled Defect Management. This feature reads the written blocks while they are still stored in the drive buffer. In case of poor read quality the blocks get written again or redirected to the Spare Area where the data get stored in replacement blocks.

This checkreading reduces write speed to at most half of the nominal speed of drive and BD medium. Sometimes it is even worse. Heavy use of the Spare Area causes long delays during read operations. So Defect Management is not always desirable.

cdrecord does not format BD-R. It has no means to prevent Defect Management on BD-RE media, though.

growisofs formats BD-R by default. The Defect Management can be prevented by option . It has no means to prevent Defect Management on BD-RE media, though.

cdrskin, xorriso and xorrecord do not format BD-R by default. They do with , resp. , resp. . These three programs can disable Defect Management with BD-RE and already formatted BD-R by , resp. , resp. .

## Burning an audio CD
Create your audio tracks and store them as uncompressed, 16-bit, 44100-Hz, stereo WAV files.

If the files are 24 bit encoded (for example, an online music service only provides 24 bit WAV files), they need to be converted to 16 bit in order to play in RedBook-compliant CD players. To check, ensure  is installed, cd to the directory with your WAV files, and run:

 $ soxi *.wav

If the file have the wrong encoding, convert the files using :

 $ for f in *.wav; do sox "$f" -b 16 output.wav; mv output.wav "$f"; done

To convert MP3 to WAV, ensure  is installed, cd to the directory with your MP3 files, and run:

 $ for FILE in *.mp3; do lame --decode "$FILE" "${FILE%.mp3}.wav"; done

In case you get an error when trying to burn WAV files converted with LAME, try decoding with :

 $ for FILE in *.mp3; do mpg123 --rate 44100 --stereo --buffer 3072 --resync -w "${FILE%.mp3}.wav" "$FILE"; done

To convert AAC to WAV ensure  is installed and run:

 $ for FILE in *.m4a; do faad "$FILE"; done

To fix the bitrate of an already existing WAV file (or many other formats), try using :

 $ for FILE in *.wav; do sox "$FILE" -c 2 -r 44100 "${FILE%.wav}-ok.wav"; done

Name the audio files in a manner that will cause them to be listed in the desired track order when listed alphabetically, such as , , , etc.

With , use the following command to simulate burning the WAV files as an audio CD:

 $ cdrecord -dummy -v -pad speed=X dev=/dev/sr0 -dao -swab *.wav

If everything worked, you can remove the  flag to actually burn the CD.

Alternatively, with , create a "Table of content" file with the following command:

 $ {
     echo "CD_DA"
     printf 'TRACK AUDIO\nFILE "%s" 0\n' *.wav
   } > toc

This will make it so that no gaps exits between tracks. Optionally, if you would like to insert a X-second gap between certain tracks, you can edit the toc file and insert the following line between the TRACK AUDIO and FILE lines for that track:

 PREGAP 00:0X:00

Then, we burn the CD:

 $ cdrdao write --speed X toc

The speed can be adjusted, lower speed producing a higher quality result. This is because the Audio-CD format has less advanced error correction than the data storage format.

To test the new audio CD, use MPlayer:

 $ mplayer cdda://

## Burning a BIN/CUE
To burn a BIN/CUE image run:

 $ cdrdao write --device /dev/sr0 image.cue

## TOC/CUE/BIN for mixed-mode discs
ISO images only store a single data track. If you want to create an image of a mixed-mode disc (data track with multiple audio tracks) then you need to make a TOC/BIN pair:

 $ cdrdao read-cd --read-raw --datafile image.bin --driver generic-mmc:0x20000 --device /dev/cdrom image.toc

Some software only likes CUE/BIN pair, you can make a CUE sheet with toc2cue (part of ):

 $ toc2cue image.toc image.cue

## Burn backend problems
If you are experiencing problems, you may ask for advice at mailing list [mailto:cdwrite@other.debian.org cdwrite@other.debian.org, or try to write to the one of support mail addresses if some are listed near the end of the program's man page.

Tell the command lines you tried, the medium type (e.g. CD-R, DVD+RW, ...), and the symptoms of failure (program messages, disappointed user expectation, ...). You will possibly get asked to obtain the newest release or development version of the affected program and to make test runs. But the answer might as well be, that your drive dislikes the particular medium.

## Burning CD/DVD/BD with a GUI
There are several applications available to burn CDs in a graphical environment.

See also Wikipedia:Comparison of disc authoring software.

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

## Playback
## CD
Playback of audio CDs requires the  package. To enable KDE Applications like Dolphin to read audio CDs install .

## DVD
If you wish to play encrypted DVDs, you must install the libdvd* packages:
*
*
*

Additionally, you must install player software. Popular DVD players are MPlayer, xine and VLC. See the video players list, the specific instructions for MPlayer, and the specific instructions for VLC.

## Blu-ray
See Blu-ray#Playback.

## Ripping
Ripping is the process of copying audio or video content to a hard disk, typically from removable media or media streams.

## Multi-format
*
*

## Audio CD
## Console
*
*
*
*
*
*
*
*

## Graphical
*
*
*
*
* .
*
*
*
*
*
*

## DVD-Video
See also Wikipedia:Comparison of DVD ripper software.

Often, the process of ripping a DVD can be broken down into two subtasks:

# Data extraction — Copying the audio and/or video data to a hard disk,
# Transcoding — Converting the extracted data into a suitable format.

Some utilities perform both tasks, whilst others focus on one aspect or the other.

## Console
*
*
*
*
*
*
*

## Graphical
*
*
*
*

## DVD-Audio
*

## Troubleshooting
## Brasero fails to normalize audio CD
If you try to burn it may stop at the first step called Normalization.

As a workaround you can disable the normalization plugin using the Edit > Plugins menu

## VLC: Error "... could not open the disc /dev/dvd"
If you get an error like

 vlc dvdread could not open the disc "/dev/dvd"

it may be because there is no device node  on your system. Udev no longer creates  and instead uses . To fix this, edit the VLC configuration file ():

 # DVD device (string)
 dvd=/dev/sr0

## DVD drive is noisy
If playing DVD videos causes the system to be very loud, it may be because the disc is spinning faster than it needs to. To temporarily change the speed of the drive, run:

 # eject -x 12 /dev/dvd

Sometimes:

 # hdparm -E12 /dev/dvd

Any speed that is supported by the drive can be used, or 0 for the maximum speed.

Setting CD-ROM and DVD-ROM drive speed

If optical drive is constantly checking for a new disc causing it to make unnecessary noise, consider turning SATA "Hot Plug" on for your optical drive in BIOS.

## Playback does not work with new computer (new DVD-Drive)
If playback does not work and you have a new computer (new DVD-Drive) the reason might be that the region code is not set. You can read and set the region code with the  package.

## None of the above programs are able to rip/encode a DVD to my hard disk!
Make sure the region of your DVD reader is set correctly; otherwise, you will get loads of inexplicable CSS-related errors. Use the  package to do so.

If ripping still does not work with the correct region set, refer to the libdvdcss developer documentation for enabling log messages and setting other relevant options.

## GUI program log indicates problems with backend program
If you use a GUI program and experience problems which the program's log blames on some backend program, then try to reproduce the problem by the logged backend program arguments.
Whether you succeed with reproducing or not, you may report the logged lines and your own findings to the places mentioned in #Burn backend problems section.

## Special case: medium error / write error
Here are some typical messages about the drive disliking the medium. This can only be solved by using a different drive or a different medium. A different program will hardly help.

Brasero with backend growisofs:

 BraseroGrowisofs stderr: :-[ WRITE@LBA=0h failed with SK=3h/ASC=0Ch/ACQ=00h]: Input/output error

Brasero with backend libburn:

 BraseroLibburn Libburn reported an error SCSI error on write(16976,16): 0C 00 Write error

## BD-R DL 50GB errors on trying to burn second layer
Using growisofs from  for burning 50GB BD-R DL discs might result in a fatal error and damaged media, such as:

This happened at the 25GB boundary when starting to write the second layer. Using cdrecord from  works with no problems. Tested with a 'HL-DT-ST BD-RE  WH16NS40' LG burner, and Verbatim BD-R DL 6x discs (#96911).

## Disc tray autocloses
If after ejecting a cd, either by using the  command, or pushing the drive button, the drive disc tray autocloses before being able to remove the disc, try the following command:

 # sysctl -w dev.cdrom.autoclose=0

If that solves the problem, make the change permanent:

If the above does not work and as a last resort measure, you can unload the disc module from the kernel via:

 # rmmod sr_mod

the disc drive should now behave as expected but will not mount disc anymore. After putting a disc into the drive, reactivate the module via:

 # modprobe sr_mod

the disc should now mount.

## External optical drive not recognized
See General troubleshooting#Cannot use some peripherals after kernel upgrade.
