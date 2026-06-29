**Blu-ray** is the optical media successor to DVD. As a medium, it is designed to hold more storage. For multimedia, it is intended to store higher quality content than DVDs, such as movies and shows in 720p, 1080p video resolution and higher, plus audio tracks with higher bitrates and number of channels, such as DTS-HD Master.

Similar to DVDs, the file storage format for blu-ray discs is UDF. The content on the discs is also protected with DRM, namely AACS (Advanced Access Content System).

There are a number of applications in portage that can be used to access Blu-ray discs and media, including ones to bypass the encryption.

## Contents

-   [[1] [Device access]](#Device_access)
-   [[2] [DRM]](#DRM)
-   [[3] [Disc information]](#Disc_information)
    -   [[3.1] [libbluray]](#libbluray)
    -   [[3.2] [bluray_info]](#bluray_info)
-   [[4] [Ripping Blu-rays]](#Ripping_Blu-rays)
    -   [[4.1] [libbluray]](#libbluray_2)
    -   [[4.2] [ffmpeg]](#ffmpeg)
    -   [[4.3] [MakeMKV]](#MakeMKV)
        -   [[4.3.1] [Command Line]](#Command_Line)
        -   [[4.3.2] [GUI]](#GUI)
-   [[5] [Playback]](#Playback)
    -   [[5.1] [VLC menu support]](#VLC_menu_support)
-   [[6] [Addendum for Region B Blu-ray]](#Addendum_for_Region_B_Blu-ray)
-   [[7] [See also]](#See_also)

## [Device access]

** Important**\
Each user must be added to the **cdrom** group to access a hardware Blu-ray disc drive.

To check if a user has been already in the **cdrom** group:

`user `[`$`]`groups`

    users cdrom

To add a user to the **cdrom** group:

`root `[`#`]`gpasswd -a user cdrom`

As with any time a user is added to a new group, they must either log out and back in as that user, or switch using [su] to gain new group abilities.

`user `[`$`]`su - user `

`user `[`$`]`groups `

    users cdrom

## [DRM]

[[[media-libs/libbluray]](https://packages.gentoo.org/packages/media-libs/libbluray)[]] will use [[[media-libs/libaacs]](https://packages.gentoo.org/packages/media-libs/libaacs)[]] to bypass AACS encryption if compiled with the `aacs` use flag. It requires a [KEYDB.cfg] text file that has the keys necessary for decryption. List can be found in [various](http://fvonline-db.bplaced.net/) [places](https://bluray.beandog.org/keydb/) online.

The key file should be saved to the case sensitive filename at [\~/.config/aacs/KEYDB.cfg]

## [Disc information]

Blu-ray discs have both \"tracks\", similar to DVD tracks, but also \"playlists\" as well. This can make it a bit confusing when trying to get information or rip media from a disc. Generally speaking, ripping a playlist will cover a common use case.

### [libbluray]

** Note**\
media-libs/libbluray needs to be compiled with the `java` USE flag to enable Blu-ray menus.

The package [[[media-libs/libbluray]](https://packages.gentoo.org/packages/media-libs/libbluray)[]] contains a few programs to help display disk information.

Use [bd_info] to list details of a disc:

`user `[`$`]`bd_info /dev/sr0`

    Using libbluray version 1.0.2
    Volume Identifier   : GENTOO_ROCKS
    BluRay detected     : yes
    First Play supported: yes
    Top menu supported  : yes
    HDMV titles         : 4
    BD-J titles         : 5
    UNSUPPORTED titles  : 5

    BD-J detected       : yes
    Java VM found       : no
    BD-J handled        : no
    BD-J organization ID: 7fff8123
    BD-J disc ID        : b484515373b51940820b165b97212b5a

    AACS detected       : yes
    libaacs detected    : yes
    Disc ID             : 1460B1469A66481964B3023486A1945806653567
    AACS MKB version    : 7
    AACS handled        : yes

    BD+ detected        : no

    Application info:
      initial mode preference : 2D
      3D content exists       : No
      video format            : ignored (0x0)
      frame rate              : ignored (0x0)
      provider data           : '                           ZNURT'

    No disc library metadata

Use [bd_list_titles] to get details of each title / track as well as the playlists:

`user `[`$`]`bd_list_titles /dev/sr0`

    Main title: 6
    index:   1 duration: 00:01:57 chapters:   2 angles:  1 clips:   1 (playlist: 00000.mpls) V:1 A:1  PG:6  IG:0  SV:0 SA:0
    index:   2 duration: 00:01:06 chapters:   2 angles:  1 clips:   1 (playlist: 00001.mpls) V:1 A:1  PG:6  IG:0  SV:0 SA:0
    index:   3 duration: 00:02:29 chapters:   2 angles:  1 clips:   1 (playlist: 00002.mpls) V:1 A:1  PG:6  IG:0  SV:0 SA:0
    index:   4 duration: 00:01:13 chapters:   2 angles:  1 clips:   1 (playlist: 00003.mpls) V:1 A:1  PG:1  IG:0  SV:0 SA:0
    index:   5 duration: 00:05:12 chapters:   2 angles:  1 clips:   1 (playlist: 00004.mpls) V:1 A:1  PG:6  IG:0  SV:0 SA:0
    index:   6 duration: 00:14:16 chapters:   2 angles:  1 clips:   1 (playlist: 00005.mpls) V:1 A:1  PG:6  IG:0  SV:0 SA:0
    index:   7 duration: 00:00:23 chapters:   2 angles:  1 clips:   1 (playlist: 00009.mpls) V:1 A:0  PG:0  IG:0  SV:0 SA:0
    index:   8 duration: 00:00:11 chapters:   2 angles:  1 clips:   1 (playlist: 00010.mpls) V:1 A:1  PG:0  IG:0  SV:0 SA:0
    index:   9 duration: 00:00:11 chapters:   2 angles:  1 clips:   1 (playlist: 00014.mpls) V:1 A:0  PG:0  IG:0  SV:0 SA:0

### [bluray_info]

The package [[[media-video/bluray_info]](https://packages.gentoo.org/packages/media-video/bluray_info)[]] displays details about the disc as well, with syntax and output format similar to the old [[[media-video/lsdvd]](https://packages.gentoo.org/packages/media-video/lsdvd)[]] program.

`user `[`$`]`bluray_info /dev/sr0`

    Disc Title: GENTOO_ROCKS
    Title: 001, Playlist: 0000, Length: 00:01:57.11, Chapters: 002, Video streams: 01, Audio streams: 01, Subtitles: 06, Filesize: 00091 MB
    Title: 002, Playlist: 0001, Length: 00:01:06.56, Chapters: 002, Video streams: 01, Audio streams: 01, Subtitles: 06, Filesize: 00053 MB
    Title: 003, Playlist: 0002, Length: 00:02:29.98, Chapters: 002, Video streams: 01, Audio streams: 01, Subtitles: 06, Filesize: 00121 MB
    Title: 004, Playlist: 0003, Length: 00:01:13.10, Chapters: 002, Video streams: 01, Audio streams: 01, Subtitles: 01, Filesize: 00057 MB
    Title: 005, Playlist: 0004, Length: 00:05:12.81, Chapters: 002, Video streams: 01, Audio streams: 01, Subtitles: 06, Filesize: 00251 MB
    Title: 006, Playlist: 0005, Length: 00:14:16.85, Chapters: 002, Video streams: 01, Audio streams: 01, Subtitles: 06, Filesize: 00791 MB
    Title: 007, Playlist: 0009, Length: 00:00:23.27, Chapters: 002, Video streams: 01, Audio streams: 00, Subtitles: 00, Filesize: 00014 MB
    Title: 008, Playlist: 0010, Length: 00:00:11.92, Chapters: 002, Video streams: 01, Audio streams: 01, Subtitles: 00, Filesize: 00010 MB
    Title: 009, Playlist: 0014, Length: 00:00:11.97, Chapters: 002, Video streams: 01, Audio streams: 00, Subtitles: 00, Filesize: 00006 MB
    Main title: 6

## [Ripping Blu-rays]

Two programs in portage can be used to copy Blu-ray titles and playlists to disc: namely, [[[media-libs/libbluray]](https://packages.gentoo.org/packages/media-libs/libbluray)[]] again, which is open source and command line only, and [[[media-video/makemkv]](https://packages.gentoo.org/packages/media-video/makemkv)[]] which is partially open source and has both command line and GUI applications.

### [libbluray]

The [[[media-libs/libbluray]](https://packages.gentoo.org/packages/media-libs/libbluray)[]] package provides the [bd_splice] command in order to copy a title or playlist to disk. The index number from above will be needed, using as examples bd\_**list_titles** or **bluray_info** for references.

The container for multimedia files are MPEG2 transport streams, so it should be saved with an **m2ts** extension. For example:

`user `[`$`]`bd_splice -t 6 /dev/sr0 bluray_title_06.m2ts`

### [ffmpeg]

Blu-rays can be accessed directly with **ffmpeg** if it compiled with the `bluray` USE flag.

Discs or ISOs can be accessed directly using `-playlist # bluray:/device_name` syntax.

For example, to copy playlist 800 (which is often the main feature on movies) on your device `/dev/sr0` to your filesystem:

`user `[`$`]`ffmpeg -playlist 800 -i bluray:/dev/sr0 -codec copy bluray_playlist.mkv`

Scan the disc for the available playlists:

`user `[`$`]`ffprobe bluray:/dev/sr0`

** Note**\
When scanning a disc, ffmpeg lists playlists that have a minimum of 3 minutes. Use **bd_list_titles** or **bluray_info** to see all the playlists.

### [MakeMKV]

MakeMKV is a partially-closed source program, and does not require a [KEYDB.cfg] file to decrypt disc access. It has both a command-line application, **makemkvcon** and a Qt application **MakeMKV**.

MakeMKV is free while in beta mode, and a registration key is needed to activate it. You can always get the latest key published from upstream [here](https://www.makemkv.com/forum/viewtopic.php?f=5&t=1053). A new one is released about every three months.

** Important**\
MakeMKV requires the sg kernel module to operate, SCSI generic support, CONFIG_CHR_DEV_SG.

** Note**\
The title and playlist indexes displayed by MakeMKV and libbluray do not match.

#### [Command Line]

**makemkvcon**, the command line application, can rip content from three sources: a disc in your Blu-ray drive (a character device on your system, such as **/dev/sr0**), a mounted Blu-ray filesytem, and a copied Blu-ray image. Documentation for makemkvcon is located [on their webpage](https://www.makemkv.com/developers/usage.txt). No man page is shipped with the package, but a user-created one is available in HTML format [here](https://bluray.beandog.org/makemkv/man/makemkvcon.html).

Copy the first title from the disc (remember that they are zero indexed) to the current directory:

`user `[`$`]`makemkvcon --minlength=0 mkv dev:/dev/sr0 0 .`

Copy the first title from a mounted directory:

`user `[`$`]`makemkvcon --minlength=0 mkv file:/mnt/bluray 0 .`

Copy the first title from an image:

`user `[`$`]`makemkvcon --minlength=0 mkv iso:bluray_movie.iso 0 .`

#### [GUI]

The program **makemkv** is a Qt application, and quite self-explanatory once started.

## [Playback]

Packages in portage that can playback Blu-rays include [[[media-video/vlc]](https://packages.gentoo.org/packages/media-video/vlc)[]], [[[media-video/mplayer]](https://packages.gentoo.org/packages/media-video/mplayer)[]], ffplay ([[[media-video/ffmpeg]](https://packages.gentoo.org/packages/media-video/ffmpeg)[]]) and [[[media-video/mpv]](https://packages.gentoo.org/packages/media-video/mpv)[]].

### [VLC menu support]

Blu-rays can be played with menu support, if [[[media-libs/libbdplus]](https://packages.gentoo.org/packages/media-libs/libbdplus)[]] and [[[dev-java/openjdk-jre-bin]](https://packages.gentoo.org/packages/dev-java/openjdk-jre-bin)[]] are installed.

** Important**\
Make sure that **user-vm** has been set for the user running the instance of VLC with [eselect java-vm].

Screenshots available [here](https://bluray.beandog.org/vlc/main_menu-rebels.png) and [here](https://bluray.beandog.org/vlc/disc_menu-rebels.png).

## [Addendum for Region B Blu-ray]

Many Blu-rays are localized. That is, the main feature is in at least three parts:

-   The opening credits (in several languages).
-   The closing credits (in several languages).
-   The feature, less the opening and closing credits.

[list_titles] and [bluray_info] may not guess the title needed to rip for the current locale.

Audition the longest/largest titles before making the rip.

## [See also]

-   [CDROM](https://wiki.gentoo.org/wiki/CDROM "CDROM") --- describes the setup of an internal optical drive like CD, DVD, and Blu-Ray drives
-   [CD/DVD/BD writing](https://wiki.gentoo.org/wiki/CD/DVD/BD_writing "CD/DVD/BD writing") --- how to **burn optical disks** on Gentoo from the [command line](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") with the [[[app-cdr/cdrtools]](https://packages.gentoo.org/packages/app-cdr/cdrtools)[]] or [[[app-cdr/dvd+rw-tools]](https://packages.gentoo.org/packages/app-cdr/dvd+rw-tools)[]] packages
-   [Recomended GUI burners](https://wiki.gentoo.org/wiki/Recommended_applications#Optical_disk_burners "Recommended applications")