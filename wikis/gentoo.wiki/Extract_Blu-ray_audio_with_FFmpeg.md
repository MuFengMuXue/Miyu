This article covers extracting Blu-Ray audio with [FFmpeg](https://wiki.gentoo.org/wiki/FFmpeg "FFmpeg").

Some music audio only titles are just becoming available on Blu-Ray, and music lovers may need to extract the audio to another portable medium. Since the Blu-Ray audio is usually one big file, the file chapters need to be found and split. Most portable media requires VFAT [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") preventing larger files sizes, and further splitting is essential.

This article will only discuss unencrypted Blu-Ray Audio media, and merrily point users to MakeMKV ([[[media-video/makemkv]](https://packages.gentoo.org/packages/media-video/makemkv)[]]) for handling encrypted Blu-Ray media.

** Important**\
Copying copyrighted material which you have purchased or material to which you do not hold a license is a crime. Some countries may be more strict, and consider simply tampering with encrypted material a crime. Funny things may also occur if when tinker with encrypted Blu-Rays, such as blacklisting. ;-)

** Note**\
Audio ranges greater than 24 bits or 480000 Hz are frequently stated as being indistinguishable to the human ear. As for me, I notice little difference between 16 and 24 bit, or 44100 and 48000 Hz of noisy music.

** Note**\
Encrypted (or commercial) Blu-ray media is extremely difficult to enjoy within Linux, as MPlayer\'s libaacs rarely works when playing encrypted Blu-ray media. Also anything higher than the common 16 bit 44100 Hz (CD Audio Quality), and you will require a Home Theater or 5.1/7.1 Dolby/DTS Audio Receiver with more than five quality speakers to decode and be able to notice a difference above CD audio quality. Receivers also have the ability to copy stereo two channel into five or more channel audio, sounding extremely similar to 5.1 PCM If you\'re an older person and dislike having to always buy additional equipment to be able to enjoy these newer proprietary formats, it has been quite common when considering Blu-ray media, to continue using only the tried and well tested CD and DVD media!

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Guide]](#Guide)
    -   [[2.1] [Mount Blu-Ray disc]](#Mount_Blu-Ray_disc)
    -   [[2.2] [Find available stream types]](#Find_available_stream_types)
    -   [[2.3] [Extract audio streams]](#Extract_audio_streams)
        -   [[2.3.1] [Extract full audio streams]](#Extract_full_audio_streams)
        -   [[2.3.2] [Devices with only 16 Bit Microsoft PCM Audio Support]](#Devices_with_only_16_Bit_Microsoft_PCM_Audio_Support)
        -   [[2.3.3] [Extract individual chapters]](#Extract_individual_chapters)
            -   [[2.3.3.1] [Find chapters]](#Find_chapters)
            -   [[2.3.3.2] [Extract a chapter]](#Extract_a_chapter)
            -   [[2.3.3.3] [Extract multiple chapters]](#Extract_multiple_chapters)
    -   [[2.4] [Tips]](#Tips)
        -   [[2.4.1] [Cover art]](#Cover_art)
        -   [[2.4.2] [MPlayer upmix when 24-bit decoding is not available]](#MPlayer_upmix_when_24-bit_decoding_is_not_available)
        -   [[2.4.3] [No DTS-H Master?]](#No_DTS-H_Master.3F)
        -   [[2.4.4] [Gapless playback]](#Gapless_playback)
        -   [[2.4.5] [Additional tools]](#Additional_tools)
    -   [[2.5] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [media-video/ffmpeg](https://packages.gentoo.org/packages/media-video/ffmpeg) [[]] [Complete solution to record/convert/stream audio and video]

  ------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+dav1d`](https://packages.gentoo.org/useflags/+dav1d)             Enable AV1 decoding support via media-libs/dav1d
  [`+drm`](https://packages.gentoo.org/useflags/+drm)                 Enable use of x11-libs/libdrm for various hardware accelerated functions and Kernel Mode Setting screen capture
  [`+fontconfig`](https://packages.gentoo.org/useflags/+fontconfig)   Support for configuring and customizing font access via media-libs/fontconfig
  [`+gnutls`](https://packages.gentoo.org/useflags/+gnutls)           Enable using net-libs/gnutls for TLS/HTTPS support and other minor functions (has no effect if USE=openssl is set)
  [`+gpl`](https://packages.gentoo.org/useflags/+gpl)                 Enable use of GPL licensed code, should be kept enabled unless LGPL binaries are needed
  [`+libass`](https://packages.gentoo.org/useflags/+libass)           SRT/SSA/ASS (SubRip / SubStation Alpha) subtitle support
  [`+postproc`](https://packages.gentoo.org/useflags/+postproc)       Enable libpostproc video post processing library support (should not disable this unless need to disable USE=gpl)
  [`+truetype`](https://packages.gentoo.org/useflags/+truetype)       Enable drawtext filter support via media-libs/freetype and media-libs/harfbuzz
  [`+xml`](https://packages.gentoo.org/useflags/+xml)                 Enable Dynamic Adaptive Streaming over HTTP (DASH) stream support using dev-libs/libxml2
  [`+zlib`](https://packages.gentoo.org/useflags/+zlib)               Add support for zlib compression
  [`X`](https://packages.gentoo.org/useflags/X)                       Add support for X11
  [`alsa`](https://packages.gentoo.org/useflags/alsa)                 Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`amf`](https://packages.gentoo.org/useflags/amf)                   Enable AMD\'s Advanced Media Framework support via media-video/amdgpu-pro-amf
  [`amr`](https://packages.gentoo.org/useflags/amr)                   Enable Adaptive Multi-Rate Audio support via media-libs/opencore-amr
  [`amrenc`](https://packages.gentoo.org/useflags/amrenc)             Enable Adaptive Multi-Rate Audio encoding support via media-libs/vo-amrwbenc
  [`appkit`](https://packages.gentoo.org/useflags/appkit)             Enable Apple AppKit framework
  [`bluray`](https://packages.gentoo.org/useflags/bluray)             Enable Blu-ray filesystems reading support via media-libs/libbluray
  [`bs2b`](https://packages.gentoo.org/useflags/bs2b)                 Enable Bauer Stereo-to-Binaural filter support via media-libs/libbs2b
  [`bzip2`](https://packages.gentoo.org/useflags/bzip2)               Enable bzip2 compression support
  [`cairo`](https://packages.gentoo.org/useflags/cairo)               Enable support for the cairo graphics library
  [`cdio`](https://packages.gentoo.org/useflags/cdio)                 Enable audio CDs reading via dev-libs/libcdio-paranoia
  [`chromaprint`](https://packages.gentoo.org/useflags/chromaprint)   Enable audio fingerprinting support via media-libs/chromaprint
  [`chromium`](https://packages.gentoo.org/useflags/chromium)         Builds libffmpeg.so to enable media playback in Chromium-based browsers like Opera and Vivaldi.
  [`codec2`](https://packages.gentoo.org/useflags/codec2)             Enable codec2 low bit rate speech codec support via media-libs/codec2
  [`cuda`](https://packages.gentoo.org/useflags/cuda)                 Enable support for various GPU-accelerated filters using NVIDIA PTX compiled with llvm-core/clang
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`dvd`](https://packages.gentoo.org/useflags/dvd)                   Add support for DVDs
  [`fdk`](https://packages.gentoo.org/useflags/fdk)                   Enable AAC (Advanced Audio Coding) encoding support via media-libs/fdk-aac in addition to FFmpeg\'s own implementation (warning: if USE=gpl is enabled, this produces a non-redistributable build)
  [`flite`](https://packages.gentoo.org/useflags/flite)               Enable text-to-speech filter support via app-accessibility/flite
  [`frei0r`](https://packages.gentoo.org/useflags/frei0r)             Enable use of filters through media-plugins/frei0r-plugins
  [`fribidi`](https://packages.gentoo.org/useflags/fribidi)           Enable Bidi support for the drawtext filter via dev-libs/fribidi
  [`gcrypt`](https://packages.gentoo.org/useflags/gcrypt)             Enable using dev-libs/libgcrypt for rtmp(t)e support (not needed if using any of USE=gmp,librtmp,openssl), and for obtaining random bytes (not needed if USE=openssl)
  [`gme`](https://packages.gentoo.org/useflags/gme)                   Enables various game music formats support via media-libs/game-music-emu
  [`gmp`](https://packages.gentoo.org/useflags/gmp)                   Add support for dev-libs/gmp (GNU MP library)
  [`gsm`](https://packages.gentoo.org/useflags/gsm)                   Add support for the gsm lossy speech compression codec
  [`iec61883`](https://packages.gentoo.org/useflags/iec61883)         Enable FireWire DV/HDV input device support via media-libs/libiec61883
  [`ieee1394`](https://packages.gentoo.org/useflags/ieee1394)         Enable FireWire/iLink IEEE1394 support (dv, camera, \...)
  [`jack`](https://packages.gentoo.org/useflags/jack)                 Add support for the JACK Audio Connection Kit
  [`jpeg2k`](https://packages.gentoo.org/useflags/jpeg2k)             Support for JPEG 2000, a wavelet-based image compression format
  [`jpegxl`](https://packages.gentoo.org/useflags/jpegxl)             Add JPEG XL image support
  [`kvazaar`](https://packages.gentoo.org/useflags/kvazaar)           Enable H.265/HEVC encoding support via media-libs/kvazaar
  [`ladspa`](https://packages.gentoo.org/useflags/ladspa)             Enable the ability to support ladspa plugins
  [`lame`](https://packages.gentoo.org/useflags/lame)                 Add support for MP3 encoding using LAME
  [`lcms`](https://packages.gentoo.org/useflags/lcms)                 Enable ICC profile support via media-libs/lcms
  [`libaom`](https://packages.gentoo.org/useflags/libaom)             Enable AV1 de/encoding via media-libs/libaom (warning: this is the reference implementation and is slower than the alternatives)
  [`libaribb24`](https://packages.gentoo.org/useflags/libaribb24)     Enable ARIB text and caption decoding via media-libs/aribb24
  [`libcaca`](https://packages.gentoo.org/useflags/libcaca)           Add support for colored ASCII-art graphics
  [`libilbc`](https://packages.gentoo.org/useflags/libilbc)           Enable internet Low Bitrate Codec de/encoding support via media-libs/libilbc
  [`liblc3`](https://packages.gentoo.org/useflags/liblc3)             Enable Low Complexity Communication Codec de/encoding support via media-sound/liblc3
  [`libplacebo`](https://packages.gentoo.org/useflags/libplacebo)     Enable use of GPU-accelerated filters from media-libs/libplacebo
  [`librtmp`](https://packages.gentoo.org/useflags/librtmp)           Enable Real Time Messaging Protocol support via media-video/rtmpdump in addition to FFmpeg\'s own implementation
  [`libsoxr`](https://packages.gentoo.org/useflags/libsoxr)           Enable use of the audio resampler from media-libs/soxr
  [`lv2`](https://packages.gentoo.org/useflags/lv2)                   Enable use of filters through media-libs/lv2
  [`lzma`](https://packages.gentoo.org/useflags/lzma)                 Support for LZMA compression algorithm
  [`modplug`](https://packages.gentoo.org/useflags/modplug)           Add libmodplug support for playing SoundTracker-style music files
  [`nvenc`](https://packages.gentoo.org/useflags/nvenc)               Add support for NVIDIA Encoder/Decoder (NVENC/NVDEC) API for hardware accelerated encoding and decoding on NVIDIA cards (requires x11-drivers/nvidia-drivers)
  [`ocr`](https://packages.gentoo.org/useflags/ocr)                   Enable Optical Character Recognition (OCR) filter support via app-text/tesseract
  [`openal`](https://packages.gentoo.org/useflags/openal)             Add support for the Open Audio Library
  [`opencl`](https://packages.gentoo.org/useflags/opencl)             Enable OpenCL support (computation on GPU)
  [`opencolorio`](https://packages.gentoo.org/useflags/opencolorio)   Enable use of color management filters via media-libs/opencolorio
  [`opengl`](https://packages.gentoo.org/useflags/opengl)             Add support for OpenGL (3D graphics)
  [`openh264`](https://packages.gentoo.org/useflags/openh264)         Enable H.264 encoding support via media-libs/openh264
  [`openmpt`](https://packages.gentoo.org/useflags/openmpt)           Enable MPTM tracked music files decoding support via media-libs/libopenmpt
  [`openssl`](https://packages.gentoo.org/useflags/openssl)           Enable using dev-libs/openssl for TLS/HTTPS support and other minor functions (USE=gnutls has no effect if set)
  [`opus`](https://packages.gentoo.org/useflags/opus)                 Enable Opus audio codec support
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)     Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`qrcode`](https://packages.gentoo.org/useflags/qrcode)             Enable QR encode generation support via media-gfx/qrencode
  [`qsv`](https://packages.gentoo.org/useflags/qsv)                   Enable Intel Quick Sync Video support via media-libs/libvpl
  [`quirc`](https://packages.gentoo.org/useflags/quirc)               Enable QR decoding support via media-libs/quirc
  [`rabbitmq`](https://packages.gentoo.org/useflags/rabbitmq)         Enable AMQP stream support via net-libs/rabbitmq-c
  [`rav1e`](https://packages.gentoo.org/useflags/rav1e)               Enable AV1 encoding support via media-video/rav1e
  [`rist`](https://packages.gentoo.org/useflags/rist)                 Enable Reliable Internet Stream Transport (RIST) protocol support via net-libs/librist
  [`rubberband`](https://packages.gentoo.org/useflags/rubberband)     Enable time-stretching and pitch-shifting audio filter support via media-libs/rubberband
  [`samba`](https://packages.gentoo.org/useflags/samba)               Add support for SAMBA (Windows File and Printer sharing)
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                   Enable use of the Simple Direct Layer library (required for the ffplay command)
  [`shaderc`](https://packages.gentoo.org/useflags/shaderc)           Enable support for various GPU-accelerated filters using Vulkan compiled with media-libs/shaderc
  [`snappy`](https://packages.gentoo.org/useflags/snappy)             Enable Snappy compression support via app-arch/snappy (required for Vidvox Hap encoder support)
  [`sndio`](https://packages.gentoo.org/useflags/sndio)               Enable audio output support via media-sound/sndio
  [`soc`](https://packages.gentoo.org/useflags/soc)                   Apply additional patches for efficient playback on some SoCs (e.g. ARM, RISC-V)
  [`speex`](https://packages.gentoo.org/useflags/speex)               Add support for the speex audio codec (used for speech)
  [`srt`](https://packages.gentoo.org/useflags/srt)                   Enable Secure Reliable Transport (SRT) support via net-libs/srt
  [`ssh`](https://packages.gentoo.org/useflags/ssh)                   Enable SSH/SFTP support via net-libs/libssh
  [`svg`](https://packages.gentoo.org/useflags/svg)                   Add support for SVG (Scalable Vector Graphics)
  [`svt-av1`](https://packages.gentoo.org/useflags/svt-av1)           Enable AV1 encoding support via media-libs/svt-av1
  [`theora`](https://packages.gentoo.org/useflags/theora)             Add support for the Theora Video Compression Codec
  [`twolame`](https://packages.gentoo.org/useflags/twolame)           Enable MP2 encoding support via media-sound/twolame in addition to FFmpeg\'s own implementation
  [`v4l`](https://packages.gentoo.org/useflags/v4l)                   Enable support for video4linux (using linux-headers or userspace libv4l libraries)
  [`vaapi`](https://packages.gentoo.org/useflags/vaapi)               Enable Video Acceleration API for hardware decoding
  [`vdpau`](https://packages.gentoo.org/useflags/vdpau)               Enable the Video Decode and Presentation API for Unix acceleration interface
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  [`vidstab`](https://packages.gentoo.org/useflags/vidstab)           Enable video stabilization filter support via media-libs/vidstab
  [`vmaf`](https://packages.gentoo.org/useflags/vmaf)                 Enable Netflix\'s perceptual video quality assessment filter support via media-libs/libvmaf
  [`vorbis`](https://packages.gentoo.org/useflags/vorbis)             Add support for the OggVorbis audio codec
  [`vpx`](https://packages.gentoo.org/useflags/vpx)                   Enable VP8 and VP9 de/encoding support via media-libs/libvpx in addition to FFmpeg\'s own implementation (for decoding only)
  [`vulkan`](https://packages.gentoo.org/useflags/vulkan)             Add support for 3D graphics and computing via the Vulkan cross-platform API
  [`webp`](https://packages.gentoo.org/useflags/webp)                 Add support for the WebP image format
  [`x264`](https://packages.gentoo.org/useflags/x264)                 Enable H.264 encoding using x264
  [`x265`](https://packages.gentoo.org/useflags/x265)                 Enable H.265/HEVC encoding support via media-libs/x265
  [`xvid`](https://packages.gentoo.org/useflags/xvid)                 Add support for xvid.org\'s open-source mpeg-4 codec
  [`zeromq`](https://packages.gentoo.org/useflags/zeromq)             Enable ZMQ command receiver filter and streaming support via net-libs/zeromq
  [`zimg`](https://packages.gentoo.org/useflags/zimg)                 Enable zscale filter support using media-libs/zimg
  [`zvbi`](https://packages.gentoo.org/useflags/zvbi)                 Enable teletext decoding support via media-libs/zvbi
  ------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 07:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Although [MPlayer](https://wiki.gentoo.org/wiki/MPlayer "MPlayer") can also be used, FFmpeg seems more refined when dumping or clipping specific audio chapters from DVD or Blu-Ray media.

`root `[`#`]`emerge --ask media-video/ffmpeg`

(If somebody successfully uses MPlayer/MPlayer2 to dump PCM specified chapters, feel free to add it to this Wiki page and retitle appropriately. I\'ve only experienced MPlayer seeking to the beginning chapter and, not recognizing or stopping at the specified end chapter. ie.

`user `[`$`]`mplayer -ao pcm:fast:file=audio.wav -chapter 2-2 -vo null -vc null input_file`

## [Guide]

### [Mount Blu-Ray disc]

Blu-Rays use UDF filesystem format, and require to be mounted as such. Probably best to edit the following file to provide mount points as such. AutoFS can be incorporated as needed.

[FILE] **`/etc/fstab`**

    /dev/sr0       /mnt/dvd        iso9660         noauto,user,ro  0 0
    /dev/sr0       /mnt/dvd-udf    udf             noauto,user,rw  0 0

Or the following will automatically decide with little to no additional access time difference:

[FILE] **`/etc/fstab`**

    /dev/sr0       /mnt/dvd        auto            noauto,user,ro  0 0

Create the mount folders defined previously in the [/etc/fstab] example file:

`root `[`#`]`mkdir /mnt/dvd /mnt/dvd-udf`

Mount the disc:

`root `[`#`]`mount /mnt/dvd-udf`

### [Find available stream types]

The main large media stream file on the Blu-Ray disk, is typically something similar to [./BDMV/STREAM/0000.m2ts].

When using [ffplay], something similar should be seen within stdout:

`user `[`$`]`ffplay ...`

    Stream #0:0[0x1011]: Video: h264 (High) (HDMV / 0x564D4448), yuv420p, 1920x1080 [SAR 1:1 DAR 16:9], 29.97 fps, 29.97 tbr, 90k tbn, 59.94 tbc
    Stream #0:1[0x1100]: Audio: pcm_bluray (HDMV / 0x564D4448), 48000 Hz, stereo, s32, 2304 kb/s
    Stream #0:2[0x1101]: Audio: pcm_bluray (HDMV / 0x564D4448), 48000 Hz, 5.1(side), s32, 6912 kb/s
    Stream #0:3[0x1102]: Audio: dts (DTS-HD MA) ([134][0][0][0] / 0x0086), 48000 Hz, 5.1(side), s16, 1536 kb/s
    ...
    Stream #0 on this audio only Blu-Ray is only a black screen with song titles.  We'll skip this stream since we want audio only PCM WAV
    Stream #1 is the PCM two channel stereo mix.
    Stream #2 is the PCM 5.1 high resolution mix.
    Stream #2 is the DTS mix.

Keep an eye on the Hz, s16/s24/s32 and kb/s, as they\'re indicators of audio quality.

### [Extract audio streams]

#### [Extract full audio streams]

To extract the three individual stream types into one large file, you can use FFmpeg. Although this is likely undesirable due to file size limitations on VFAT filesystems.

`user `[`$`]`ffmpeg -i ./BDMV/STREAM/00000.m2ts -map 0:1 -acodec pcm_s24le music.wav `

`user `[`$`]`ffmpeg -i ./BDMV/STREAM/00000.m2ts -map 0:2 -acodec pcm_s24le music-pcm51.wav `

`user `[`$`]`ffmpeg -i ./BDMV/STREAM/00000.m2ts -map 0:3 -acodec copy music.dts `

Verify the streams have been extracted using [ffplay] or [mplayer]. Monitor the stdout messages to ensure proper drivers and codecs are used for the stream types specified.

For DTS playback using MPlayer, it will be likely necessary to specify `ac=hwdts` to MPlayer for passing through DTS to the HDMI/SPDIF audio receiver. MPlayer uses the following for specifying streams:

`user `[`$`]`mplayer -aid 1 -demuxer lavf ./BDMV/STREAM/00000.m2ts`

#### [Devices with only 16 Bit Microsoft PCM Audio Support]

Some audio receivers and devices will only play 16 bit Microsoft PCM WAV files. If you have 24-bit audio files as indicated above and such hindered devices, you will need to unfortunately down mix in order for the files to be playable on those devices. The above aforementioned conversion provides 24 bit PCM Riff/Aiff files, while the below ffmpeg incantation will provide 16 bit Microsoft PCM WAV files.

`user `[`$`]`ffmpeg -i ./BDMV/STREAM/00000.m2ts -map 0:1 -acodec pcm_s16le music.wav`

Another work around, is to play the 24bit PCM WAV files using a software media player such as FFplay and MPlayer, and route the sound to your audio receiver using HDMI or S/PDIF. One other option, ensure you buy a receiver capable of playing the 24 bit PCM files via USB media!

** Note**\
If this section applies to you, then you will need to augment the further FFmpeg incantations below with the `-acodec pcm_s16le` option.

#### [Extract individual chapters]

##### [Find chapters]

1\) The package media-video/bluray_info will display chapters.

`user `[`$`]`bluray_info -x /dev/sr0`

2\)

`user `[`$`]`ffprobe`

, provided by [[[media-video/ffmpeg]](https://packages.gentoo.org/packages/media-video/ffmpeg)[]] package, will display the chapters to stdout, if they are preserved within the media file.

`user `[`$`]`ffprobe ./music.mkv`

More elaborate or useful examples using [ffprobe]:

`user `[`$`]`ffprobe -i 00.mkv -print_format default -show_chapters -loglevel error > 00.mkv.txt 2>&1`

`user `[`$`]`ffprobe -i 00.mkv -print_format flat -show_chapters -loglevel error > 00.mkv.txt 2>&1`

** Note**\
When using MakeMKV, make sure to extract to a format preserving Chapters with using [makemkvcon mkv]. Using [makemkvcon backup] does not preserve chapter information as of this writing!

For extracting streams including chapter info for use with ffprobe:

`user `[`$`]`makemkvcon -r mkv disc:0 all ./foo_folder/`

(MPlayer can also identify chapters using \"mindentify\", however the chapter times do not appear comptabile with FFmpeg.)

##### [Extract a chapter]

At this point, we\'ll assume we want Stream #1 for standard two stereo PCM WAV files (ie. map 0:1) and the second (#0.2) chapter.

FFprobe\'s snipped output:

`user `[`$`]`ffprobe ...`

    ...
    Chapter #0.2: start 534.934400, end 888.087200

The incantation of FFmpeg we\'ll use for exacting this individual chapter, using seconds for start and duration indicators.

`user `[`$`]`ffmpeg -ss [start] -i in.dts -t [duration] -c:v copy -c:a copy out.wav`

With this example, the start time will be 534.934400 and duration will be 888.087200 minus 534.934400.

For example:

`user `[`$`]`ffmpeg -ss 534.934400 -i ./BDMV/STREAM/00000.m2ts -t 353.152800 -c:v copy -c:a copy out.wav`

##### [Extract multiple chapters]

I have only piped the message stdout of the CLI tools to a series of text files, utilizing [grep] and [bc] (CLI Calculator), along side VI/VIM for line duplication and clipping for creating one time scripts for extracting multiple files at once.

Someday, this will likely be automated and integrated into [abcde.sh].

### [Tips]

#### [Cover art]

Cover art is usually found within the [/mnt/dvd/BDMV/META/DL] folder. For example:

`user `[`$`]`cp /mnt/dvd/BDMV/META/DL/discinfo_640x360.jpg $/Music/My_Album/cover.jpg`

#### [MPlayer upmix when 24-bit decoding is not available]

My receiver is apparently not capable of decoding 24 bit PCM WAV, but will decode 16 and 32 bit PCM WAV through HDMI.

The PCM 5.1 WAV files are encoded at 24 bit PCM 5.1 WAV 48000 Hz.

The work around here is to upmix to 32 bit using sb32le or floatle, since MPlayer by default down mixes to 16 bit or s16le. MPlayer also by default cuts channels to two channels.

`user `[`$`]`mplayer -af format=s32le,channels=8 PCM51-24bit/01.my_music_track.dts `

`user `[`$`]`mplayer2 -af format=s32le,channels=8 PCM51-24bit/01.my_music_track.dts `

#### [][No DTS-H Master?]

My receiver shows it\'s decoding DTS-HD Master stream when bit perfect or high definition audio decoding is selected within my Window\'s player, but my receiver only says it\'s decoding the usual \"DTS\" decoding while playing streams within Linux. From reports on the web, bit perfect or high definition streaming to the receiver isn\'t possible within Linux. Other reports state it is possible using Intel\'s HDMI. (NVidia\'s video card HDMI using Linux binary drivers isn\'t performing DTS-HD Master here.)

#### [Gapless playback]

Split tracks of long streams, it\'s nice to have gapless playback for preventing interruptions between tracks.

FIXME: The following is from Snipplr, but doesn\'t work for me. :-/

`user `[`$`]`mkfifo /tmp/aufifo `

`user `[`$`]`aplay -t raw -c 2 -f S16_LE -r 44100 /tmp/aufifo &> /tmp/aplayfifo.log & `

`user `[`$`]`mplayer -ao pcm:nowaveheader:file=/tmp/aufifo 01.track.wav 02.track.wav 03.track.wav & `

Or use MPlayer2:

`user `[`$`]`mplayer2 -ac hwdts -af channels=8 -ao alsa:device=hw=1.3 -gapless-audio DTS/*.dts`

#### [Additional tools]

Additional tools which might be useful, but not utilized within this wiki:

-   [[[media-sound/shntool]](https://packages.gentoo.org/packages/media-sound/shntool)[]] - A multi-purpose WAVE data processing and reporting utility, ie. splitting WAV files.
-   [MPlayer](https://wiki.gentoo.org/wiki/MPlayer "MPlayer") - Media Player for Linux, as an option to FFmpeg
-   [[[media-video/tsmuxer]](https://packages.gentoo.org/packages/media-video/tsmuxer)[]] - Utility to create and demux TS and M2TS files

### [References]

Properly configure ALSA for [pass-through digital audio](https://alsa.opensrc.org/DigitalOut), including specifying default decoding codecs for hardware digital decoders when using MPlayer.