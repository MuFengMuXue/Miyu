# Blu-ray

This article is designed to help Linux users to play the Blu-ray discs they have legally purchased on their computers.

## How it works
## Blu-ray DRM
Contrary to the DVD CSS, which was definitely compromised once the unique encryption key had been discovered, Blu-ray uses stronger DRM mechanisms, which makes it a lot more difficult to manage. Firstly, the AACS standard uses a lot more complicated cryptographic process to protect the disc content, but also allows the industry to revoke compromised keys and distribute new keys through new discs. Secondly, Blu-ray may also use another layer of protection: BD+. Although most of commercial discs use AACS, a few of them additionally use BD+. In 2007, the AACS system was compromised and decryption keys were published on the Internet. Many decryption programs were made available, but the interest to Linux users was the capability of playing their discs - legally purchased - on their computers. Although the industry  was able to revoke the first leaked decryption keys, new keys are regularly published in a cat and mouse play.

## AACS
The AACS specification and decryption process are publicly available at Many articles and research papers describe it in detail at [https://forum.doom9.org/showthread.php?t=122363, or [https://www.iis.sinica.edu.tw/papers/lcs/5007-F.pdf.

 is a research project from the VideoLAN developer team to implement the Advanced Access Content System specification, and distributed as an open-source library This project does not offer any key or certificate that could be used to decode encrypted copyrighted material. However, combined with a key database file, it is possible to use it to play Blu-ray discs that use the AACS standard. This file is called  and is accessed by libaacs in . The format of this file is available at [https://code.videolan.org/videolan/libaacs/-/blob/master/KEYDB.cfg.

## AACS decryption process
The AACS decryption process for a protected disc by a licensed player goes through four stages:

# The software/embedded player's Device Keys, together with the disc's Media Key Block (MKB) data are used to retrieve a "Processing Key", and with that (plus another datum from the MKB) to compute the Media Key.
# That Media Key, together with the disc's Volume ID (VID) obtained by the player presenting a valid Host Certificate to the drive is used to compute the Volume Unique Key (VUK).
# This VUK is used to unscramble the disc's scrambled Title Keys.
# Finally those Title Keys unscramble the disc's protected media content.

Note that it is the disc that contains the MKB. MKBs have been renewed since the first commercial Blu-ray release in 2006. The latest MKB is version 78, and many discs actually share the same MKB. The software player provides the Host key and certificate, whereas the drive contains a list of the Host key/certificates that have been revoked. Host key/certification revocation occurs when a newer disc (containing a higher MKB than the previous played disc) is decrypted, or played, or attempted to decrypt or play (the mere insertion of a disc does not update the drive). When this happens, the drive forever loses its capability to use older Host key/certificates.

Using , the decryption process can skip some of these stages to reach the last step, which allows the media player to play the disc. This is either by providing in the  file either (or both):

* a valid (corresponding to the MKB version of the disc) Processing key and a valid (i.e. non revoked by the drive) Host key/certificate
* a valid VUK for the specific disc.

If libaacs finds a valid processing key for the disc MKB version as well as a valid Host key and certificates, it can start the decryption process from step 2. However, the Host key/certificates are regularly revoked through the propagation of new Blu-ray discs. Once revoked, a drive is not able to read both new and older discs. This is usually irreversible and can only be fixed by providing a more recent Host key/certificate (for Windows users, this corresponds to updating their software player). The advantage of this method is that until the Host key/certificate is revoked, and as long as the disc uses an MKB version for which the Processing key is known, libaacs is able to compute the VUK of any disc.

Thankfully, in case no valid Processing key is available and/or the Host certificate has been revoked, libaacs has an alternative way to decrypt a disc: by providing a valid VUK in the  file. This allows libaacs to skip directly to step 3. Contrary to the Processing keys, VUKs are unique and specific to one disc ; however the great advantage is that once computed the VUK cannot be revoked. Note that if libaacs is able to perform step 2 (with a valid Host key/certificate), then it stores the VUK calculated in step 3 in . At subsequent viewings of the same disc, libaacs can reuse the stored VUK. Thus it may be a good idea to backup these VUKs or, even better, share them online.

There have been several efforts to compile VUKs from various sources. Early attempts were provided in various forums, such as Doom9.org. As the community got organised, a centralised VUK database was created at with more than 24,000 published VUKs ; however, this website appears to be no longer maintained. A new initiative by the author of the [https://forum.doom9.org/showthread.php?t=172472 FindVUK tool was then created at http://fvonline-db.bplaced.net/ with more than 150,000 downloadable entries, which makes it the most comprehensive source of public VUKs available.

## BD+
BD+ is an additional but optional component of the Blu-ray DRM. In December 2013, VideoLAN released the long awaited  which provides experimental support for BD+ decryption. The library does not provide keys or certificates required for BD+ decryption, you need to retrieve and install them separately.

BD+ mainly works by adding errors to the video stream, not enough to make it unwatchable but enough to make it unpleasant to watch due to near constant artifacting. These are fixed in official players by using "fixup tables", which are downloaded from the internet and provide a mapping to convert the broken video stream into the correct video stream.

## Playback
## Preparation
# Install  and .
# Download a  file (uppercase matters) from and copy it in the directory  or . This file contains VUK data required for attempting the decryption process described below for more than 90,000 discs. Note that all languages contain the same information to read a disc, only the name of the disc is translated. You may want to update this file regularly, as new versions are provided from time to time.
# Optionally, copy the PK and Host K/C data provided at [https://forum.doom9.org/showpost.php?p=1883655&postcount=3 at the beginning of that  file. This provides PK and Host K/C data for discs up to MKB v68. This is only necessary for discs that may not already be listed in the VUK list, and will only work for drives that have never read a disc using MKB v70 or above.
# If necessary (i.e. if volumes are not mounted automatically on your system), mount the disc to a directory, e.g.:

## Querying your disc
The  tool that comes with  is a useful tool to identify what specific encryption and DRM schemes are used on your target disc and whether it is decryptable with your current setup. For example:

Note the  that indicates this disc is decryptable and playback should not be an issue.

## Decryption process
Launch a Blu-ray software player, such as VLC, and try to play the disc (on VLC, select Media > Open Disc, then in the Disc tab, choose Blu-ray. Be sure No disc Menus is checked.). The software player will then apply the decryption process described below:

# The user starts playing a Blu-ray with a video player having libbluray and libaacs support.
# If the BR disc is not scrambled with AACS, go to 4.1.
# If the BR disc is scrambled with AACS, libaacs will:
## Check if a valid VUK for the disc is already available in . If yes, go to step 4.1, if not continue to next step.
## Read :
### If a valid VUK is available, go to 4.1, if not continue to next step.
### If a valid PK (i.e. corresponding to the disc MKB version) and a valid (non-revoked by drive) Host key/certificate is available, libaacs will attempt to compute the VUK. The VUK is then stored in  for future use. Go to step 4.1. If no valid PK/HKC are available, go to step 4.2.
# Result
## The software player is able to play the disc content.
## The software player fails to read the disc content.

## Decrypting using VUK (step 3.1 or 3.2.1)
Using the VUK specific to your disc will always work, and cannot be revoked by the industry, as it is the most downstream decryption key for a Blu-ray disc. However, there is one unique VUK per disc, corresponding to one VID, making this method rely on VUK lists or databases. The VUK will be known if either of these are true:
* decrypting using PK and Host K/C described below has worked once, and the generated VUK for your disc has been stored in , or
* the valid VUK for your disc has been obtained from a third party (i.e. is available in ). This allows you to read a disc, even if the PK and host key/certificate have been revoked for your disc MKB version.
If none of these are true, then the software player will attempt decrypting the disc using the second method.

## Decrypting using PK and Host K/C (step 3.2.2)
This method uses the Processing keys and a Host Key/Certificate present at the beginning of the  file and will only work if they have not been revoked in your drive.

If this method is successful, after you play the disc, libaacs will store the VUK in . The filename is the disc ID and its content is the VUK itself. VLC will reuse this VUK even if it does not find a valid  file, so it could be a good idea to backup this directory for the future.

## BD+ support
 provides experimental support for BD+ decryption, but if this fails, users will have to use commercial solutions, such as  or DVDFab (under Wine).

Since version 0.2.0, libbdplus supports cached tables that are used to correct the streams, thus circumventing the need to fully emulate the BD+ virtual machine.

In order for libbdplus to work, the following preparation needs to be done:

# Download the BD+ virtual machine files and the archives of the cached tables from the Doom9’s forum # Move the virtual machine files to .
# Extract the cached tables and move them to .

Now, when playing a BD+ protected disc, libbdplus should find the appropriate table and fix the stream.

## Media players
These are media players capable of using libbluray and libaacs to play AACS-scrambled Blu-ray discs.

## mplayer
To play Blu-ray discs in mplayer the basic playback command is:

 $ mplayer br:////bluray/mount/dir

or:

 $ mplayer br://title number -bluray-device /bluray/mount/dir

## Stuttering video
It is likely that you will need to enable hardware acceleration and multi core CPU support for the Blu-ray to play smoothly.

For nvidia cards, enable hardware acceleration by installing libvdpau and using the option  with mplayer. e.g:

 $ mplayer --hwdec=auto br:////bluray/mount/dir

For multi core CPU support use the options , where  is the number of cores, e.g:

 $ mplayer --vd-lavc-threads=4 br:////bluray/mount/dir

## Incorrect audio language
You can scroll through the playback languages using the  key.

## Out-of-sync audio
From your first mplayer output, you must find the codec used for the Blu-ray. It will be at the end of the line "Selected video codec".

For H.264 discs use the option . e.g:

 $ mplayer -vc ffh264vdpau br:////bluray/mount/dir

For VC-1 discs use . e.g:

 $ mplayer -vc ffvc1vdpau br:////bluray/mount/dir

For MPEG discs use . e.g:

 $ mplayer -vc ffmpeg12vdpau br:////bluray/mount/dir

## mpv
Blu-Ray playback can simply be achieved with:

 $ mpv bd://title/device

## VLC
Install . Note that this package is installed by both  and .

Start playback with:

 $ vlc bluray:///bluray/mount/dir

VLC can also play Blu-ray discs without mounting, directly from the block device:

 $ vlc bluray:///dev/sr0

## Blu-ray menus do not load with "Failed to start bluray playback. Please try without menu support."
Some Blu-ray disc menus may not work with Java 18 or above. Installing  and switching to it may allow these menus to function:

 # archlinux-java set java-17-openjdk

Alternatively, start the Blu-ray without menus, by checking the "No disc menus" checkbox in VLC's "Open Media" dialog (VLC > Open Disc).

## VLC loading endlessly
If VLC is endlessly loading the video without giving an error message, see VLC media player#Media does not load.

## xine
Start playback with:

 $ xine bluray:///bluray/mount/dir

## Troubleshooting
## Absent KEYDB.cfg file
If a valid VUK is found in , then libaacs does not need to use  to decrypt the content. However, a  file in  is still required (even if that file is empty).

## Revoked Host key/certificate
Unfortunately, what may happen when trying to play a newer Blu-ray disc is the revocation of host key/certificates (which are keys of licensed software players) by your drive. When this happens,  will return this message:

 The given Host Certficate / Private Key has been revoked by your drive.

This is part of the AACS protection scheme: editors are able to revoke old software player host keys that have leaked on the Internet and distribute the lists on newer commercial disc releases. This is irreversible and cannot be fixed even after reflashing the drive. The only two ways to correct this would be:

* to update the host key/certificate part in  to ones that have not been revoked (yet)
* to add in  the VUK of each specific disc instead, as explained above. VUKs cannot be revoked by the industry.

When a disc (using mplayer or vlc) is successfully decrypted, libaacs will store the VUK in . If the host key/certificate in  is subsequently revoked, VLC will still be able to use the stored VUK, so it could be a good idea to backup the  directory for the future.

## Using aacskeys
Install . You need to run  from a directory that contains valid host key/certificate and processing keys:

 $ cd /usr/share/aacskeys

and run:

 $ aacskeys /bluray/mount/dir

eg:

$ cd /usr/share/aacskeys && aacskeys /media/blurays

If you wish, you may add the Blu-ray to the key database: edit  and add the information output by aacskeys using this syntax:

 0xunit key file hash = Film Title    | V | 0xvolume unique key

## If aacskeys is not able to generate the key
Try , it may give you clearer error messages if nothing else.

If you have a supported drive, you may also look at flashing it with a [https://www.makemkv.com/forum/viewtopic.php?t=19634#p74718 custom firmware which allows the entire disc to be read without verification. This is referred to as enabling "LibreDrive" mode. , which comes with , may work to flash your drive in Linux natively. Options are explained a bit in discussion of the GUI wrapper which may help to determine when options like  are required.

Once flashed the change is persistent and the new firmware should allow media players like VLC to read the disc directly without makemkv's involvement.

## If you have the corresponding VUK but the Blu-ray will not play
Some drives need the sg module loaded.
