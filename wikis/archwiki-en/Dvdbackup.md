# Dvdbackup

There are several ways to backup DVD videos. The quickest and simplest is to copy the ISO image as is. Many other methods are slow, and require several steps to accomplish. dvdbackup provides one of the simpler methods to rip a DVD (with some help from dvdauthor). It is elegant because it does not demux/remux/transcode/reformat the movie. This means the backup process is done in one step. But it can be tricked into copying much more than necessary by a DVD reporting incorrect size data.

## Installation
Install the  package.  is required to read encrypted DVDs.  is only required if backing up specific titles or title sets.

## Examining the DVD
First, determine which title to backup. The following command retrieves information about the DVD:

 $ dvdbackup -i /dev/dvd -I
/dev/dvd can be /dev/sr0 Optical disc drive#Troubleshooting:
After some less useful information, dvdbackup will display something similar to the following:

This indicates that the main feature is in title set 1. Next a list of title sets is displayed:

The main feature in this example is title 1. Sometimes a title set will include more than one title, sometimes not. Title sets can also include menus, which will no longer work if not backing up the entire DVD.

## Ripping the DVD
## A single title
The  option allows you to extract a specific title:

 $ dvdbackup -i /dev/dvd -o ~ -t 1 -p

You will now see a number of VOB files on the hard drive (in ). These files can be played in MPlayer or VLC, but are insufficient to create a DVD copy. This is where dvdauthor is useful.

A title set must now be created (e.g.  and ). Be aware that the following command will make a copy of the entire movie. The original can be deleted right afterwards.

 $ mkdir ~/dvd
 $ cd ~/movie_name/VIDEO_TS
 $ dvdauthor -t -o ~/dvd *.VOB

dvdauthor will create a copy of the movie. If it outputs anything like "SCR moves backwards, remultiplex input" there might be trouble. Before deleting any files, check the file sizes of the original VOB files compared to the copied ones. If all roughly the same size, you may be alright. You can use mplayer to test the affected VOB files to see if anything is missing.

Now, table of contents files must be created (e.g.  and ). This is much less time-consuming, and does not waste hard drive space:

 $ cd ~/dvd/VIDEO_TS
 $ dvdauthor -o ~/dvd -T

## The main feature
The  option automatically detects the main feature (though not always correctly) and copies the entire title set:

 $ dvdbackup -i /dev/dvd -o ~ -F -p

Now, table of contents files must be created (e.g.  and ):

 $ cd ~/movie_name/VIDEO_TS
 $ dvdauthor -o ~/movie_name -T

## The whole DVD
The  option will backup the entire DVD structure, including menus, special features, etc. to the current directory. This requires approximately 7 GB of disk space for most DVDs:

 $ dvdbackup -i /dev/dvd -M -p

## Shrinking the DVD
If the movie needs to fit on a 4.7 GB single layer DVD,  can be used to shrink it down to size. First, rip the main title and concatenate the VOBs into one file.

 $ dvdbackup -t 1
 $ cat ./movie/VIDEO_TS/*.VOB > ./movie.vob

Calculate the shrink factor for vamps. Divide the size of your VOB file by the size of your writable media and round up.

 $ du -BMB movie.vob
 5376MB movie.vob
 $ echo '5376 / 4707' | bc -l

Run vamps,  selects the audio stream. Running  beforehand might help determine which stream to select.

 $ vamps -E 1.15 -a 1  movie.dvd5.vob

Author the dvd with :

 $ dvdauthor -t -o ./author movie.dvd5.vob
 $ dvdauthor -T -o ./author

## Writing to disc
See Optical disc drive#Burning.

## Creating an ISO
The advantage of creating the ISO file is that you can test that everything works fine with mplayer before continuing. The disadvantage is that the ISO consumes hard drive space.

 $ mkisofs -dvd-video -udf -o ~/dvd.iso ~/dvd # if a single title was extracted

or the following if the whole DVD was extracted:

 $ mkisofs -dvd-video -udf -o ~/dvd.iso ~/movie_name

To test the image:

 $ mplayer dvd:// -dvd-device ~/dvd.iso

If everything seems fine, burn the image:

 $ growisofs -Z /dev/dvd=~/dvd.iso

## Burning straight to DVD
Creating and testing an image is a waste of time and hard drive space! Basically, we can merge the mkisofs with the growisofs command:

 $ growisofs -dvd-video -udf -Z /dev/dvd ~/dvd # if a single title was extracted

or

 $ growisofs -dvd-video -udf -Z /dev/dvd ~/movie_name
