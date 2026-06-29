**Resources**

[[]][Home](https://www.musicpd.org/)

[[]][Official documentation](https://www.musicpd.org/doc/html/user.html)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/mpd)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Music_Player_Daemon "wikipedia:Music Player Daemon")

[[]][[#mpd](ircs://irc.libera.chat/#mpd)] ([[webchat](https://web.libera.chat/#mpd)])(registration required)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/mpd)

**MPD** (**M**usic **P**layer **D**aemon) is a flexible, server-side application for playing music. Through plugins and libraries it can play a variety of sound files while being controlled by a network protocol.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [System-wide configuration]](#System-wide_configuration)
        -   [[2.1.1] [Basic configuration]](#Basic_configuration)
        -   [[2.1.2] [PulseAudio (optional)]](#PulseAudio_.28optional.29)
        -   [[2.1.3] [Pipewire (optional)]](#Pipewire_.28optional.29)
        -   [[2.1.4] [Built-in HTTP streaming server (optional)]](#Built-in_HTTP_streaming_server_.28optional.29)
        -   [[2.1.5] [Bluetooth headset (optional)]](#Bluetooth_headset_.28optional.29)
            -   [[2.1.5.1] [ALSA (non-PulseAudio) setup with BlueZ 5]](#ALSA_.28non-PulseAudio.29_setup_with_BlueZ_5)
        -   [[2.1.6] [FIFO (optional)]](#FIFO_.28optional.29)
        -   [[2.1.7] [Service]](#Service)
            -   [[2.1.7.1] [OpenRC]](#OpenRC)
            -   [[2.1.7.2] [systemd]](#systemd)
    -   [[2.2] [Per-user configuration]](#Per-user_configuration)
        -   [[2.2.1] [Basic configuration]](#Basic_configuration_2)
        -   [[2.2.2] [Service]](#Service_2)
            -   [[2.2.2.1] [systemd]](#systemd_2)
-   [[3] [Clients]](#Clients)
    -   [[3.1] [Commandline/Console]](#Commandline.2FConsole)
    -   [[3.2] [Graphical (GTK)]](#Graphical_.28GTK.29)
    -   [[3.3] [Graphical (Qt)]](#Graphical_.28Qt.29)
    -   [[3.4] [Graphical (other)]](#Graphical_.28other.29)
    -   [[3.5] [Web]](#Web)
    -   [[3.6] [Scrobblers]](#Scrobblers)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [No Audio from PulseAudio]](#No_Audio_from_PulseAudio)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/mpd](https://packages.gentoo.org/packages/media-sound/mpd) [[]] [The Music Player Daemon (mpd)]

  ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+alsa`](https://packages.gentoo.org/useflags/+alsa)                   Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`+audiofile`](https://packages.gentoo.org/useflags/+audiofile)         Add support for libaudiofile where applicable
  [`+curl`](https://packages.gentoo.org/useflags/+curl)                   Enable web stream listening support via net-misc/curl
  [`+dbus`](https://packages.gentoo.org/useflags/+dbus)                   Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`+eventfd`](https://packages.gentoo.org/useflags/+eventfd)             Use the eventfd function in MPD\'s event loop
  [`+ffmpeg`](https://packages.gentoo.org/useflags/+ffmpeg)               Enable ffmpeg/libav-based audio/video codec support
  [`+icu`](https://packages.gentoo.org/useflags/+icu)                     Enable ICU (Internationalization Components for Unicode) support, using dev-libs/icu
  [`+id3tag`](https://packages.gentoo.org/useflags/+id3tag)               Enable support for ID3 tags via media-libs/libid3tag
  [`+inotify`](https://packages.gentoo.org/useflags/+inotify)             Use the Linux kernel inotify subsystem to notice changes to mpd music library
  [`+io-uring`](https://packages.gentoo.org/useflags/+io-uring)           Enable the use of io_uring for efficient asynchronous IO and system requests
  [`+mad`](https://packages.gentoo.org/useflags/+mad)                     Add support for mad (high-quality mp3 decoder library and cli frontend)
  [`+mpg123`](https://packages.gentoo.org/useflags/+mpg123)               Enable support for mp3 decoding over media-sound/mpg123
  [`ao`](https://packages.gentoo.org/useflags/ao)                         Use libao audio output library for sound playback
  [`bzip2`](https://packages.gentoo.org/useflags/bzip2)                   Enable bzip2 compression support
  [`cdio`](https://packages.gentoo.org/useflags/cdio)                     Enable ISO9660 parsing via dev-libs/libcdio-paranoia
  [`chromaprint`](https://packages.gentoo.org/useflags/chromaprint)       Enable ChromaPrint / AcoustID support
  [`doc`](https://packages.gentoo.org/useflags/doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`expat`](https://packages.gentoo.org/useflags/expat)                   Enable the use of dev-libs/expat for XML parsing
  [`faad`](https://packages.gentoo.org/useflags/faad)                     Use media-libs/faad2 for AAC decoding
  [`flac`](https://packages.gentoo.org/useflags/flac)                     Add support for FLAC: Free Lossless Audio Codec
  [`fluidsynth`](https://packages.gentoo.org/useflags/fluidsynth)         Enable MIDI support with media-sound/fluidsynth (discouraged)
  [`gme`](https://packages.gentoo.org/useflags/gme)                       Enable video game music formats support via media-libs/game-music-emu
  [`httpd`](https://packages.gentoo.org/useflags/httpd)                   Enable built-in stream server
  [`jack`](https://packages.gentoo.org/useflags/jack)                     Add support for the JACK Audio Connection Kit
  [`lame`](https://packages.gentoo.org/useflags/lame)                     Support for MP3 streaming via Icecast2
  [`libmpdclient`](https://packages.gentoo.org/useflags/libmpdclient)     Enable support for remote mpd databases
  [`libsamplerate`](https://packages.gentoo.org/useflags/libsamplerate)   Build with support for converting sample rates using libsamplerate
  [`libsoxr`](https://packages.gentoo.org/useflags/libsoxr)               Enable resampling with media-libs/soxr
  [`mikmod`](https://packages.gentoo.org/useflags/mikmod)                 Add libmikmod support to allow playing of SoundTracker-style music files
  [`mms`](https://packages.gentoo.org/useflags/mms)                       Support for Microsoft Media Server (MMS) streams
  [`modplug`](https://packages.gentoo.org/useflags/modplug)               Add libmodplug support for playing SoundTracker-style music files
  [`musepack`](https://packages.gentoo.org/useflags/musepack)             Enable support for the musepack audio codec
  [`nfs`](https://packages.gentoo.org/useflags/nfs)                       Enable support for the Network File System
  [`openal`](https://packages.gentoo.org/useflags/openal)                 Add support for the Open Audio Library
  [`openmpt`](https://packages.gentoo.org/useflags/openmpt)               OpenMPT decoder plugin
  [`opus`](https://packages.gentoo.org/useflags/opus)                     Enable Opus audio codec support
  [`oss`](https://packages.gentoo.org/useflags/oss)                       Add support for OSS (Open Sound System)
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)             Enable support for PipeWire audio backend
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)         Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`qobuz`](https://packages.gentoo.org/useflags/qobuz)                   Build plugin to access qobuz
  [`recorder`](https://packages.gentoo.org/useflags/recorder)             Enables output plugin for recording radio streams
  [`samba`](https://packages.gentoo.org/useflags/samba)                   Add support for SAMBA (Windows File and Printer sharing)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`shout`](https://packages.gentoo.org/useflags/shout)                   Enable ShoutCast/IceCast plugin using media-libs/libshout
  [`sid`](https://packages.gentoo.org/useflags/sid)                       Enable SID (Commodore 64 audio) file support
  [`signalfd`](https://packages.gentoo.org/useflags/signalfd)             Use the signalfd function in MPD\'s event loop
  [`snapcast`](https://packages.gentoo.org/useflags/snapcast)             Snapcast audio plugin
  [`sndfile`](https://packages.gentoo.org/useflags/sndfile)               Add support for libsndfile
  [`sndio`](https://packages.gentoo.org/useflags/sndio)                   Enable support for the media-sound/sndio backend
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)                 Add support for sqlite - embedded sql database
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Enable support for systemd socket activation
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tremor`](https://packages.gentoo.org/useflags/tremor)                 Enable support for media-libs/tremor, a fixed-point version of the Ogg Vorbis decoder
  [`twolame`](https://packages.gentoo.org/useflags/twolame)               Enable MP2 encoding via media-sound/twolame
  [`upnp`](https://packages.gentoo.org/useflags/upnp)                     Enable UPnP port mapping support
  [`vorbis`](https://packages.gentoo.org/useflags/vorbis)                 Add support for the OggVorbis audio codec
  [`wav`](https://packages.gentoo.org/useflags/wav)                       Support WAV encoding
  [`wavpack`](https://packages.gentoo.org/useflags/wavpack)               Add support for wavpack audio compression tools
  [`webdav`](https://packages.gentoo.org/useflags/webdav)                 Enable using music from a WebDAV share
  [`wildmidi`](https://packages.gentoo.org/useflags/wildmidi)             Enable MIDI support via media-sound/wildmidi
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)             Support for DNS Service Discovery (DNS-SD)
  [`zip`](https://packages.gentoo.org/useflags/zip)                       Enable support for ZIP archives
  [`zlib`](https://packages.gentoo.org/useflags/zlib)                     Enable database compression with virtual/zlib
  ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-22 22:05] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
A number of these flags are set by the [desktop profile](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles").

### [Emerge]

`root `[`#`]`emerge --ask media-sound/mpd`

## [Configuration]

After finished installation MPD should be working with the Gentoo shipped default configuration.

A list of supported plugins/features of your MPD can be obtained by issuing:

`user `[`$`]`mpd --version`

MPD can be configured in a system-wide or per-user fashion. The configuration style choice depends on the intended usage.

### [System-wide configuration]

#### [Basic configuration]

Below an example of a simple configuration:

[FILE] **`/etc/mpd.conf`**

    music_directory      "/var/lib/mpd/music"
    playlist_directory   "/var/lib/mpd/playlists"
    db_file              "/var/lib/mpd/database"
    log_file             "/var/lib/mpd/log"
    state_file           "/var/lib/mpd/state"

    user                 "mpd"

    bind_to_address      "localhost"
    bind_to_address      "/var/lib/mpd/socket"

    input

    audio_output

At this point MPD should be able to run as a system daemon with its own user called [mpd], which is the default setting of MPD.

#### [][PulseAudio (optional)]

If MPD was build with [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") support (`pulseaudio` USE flag), add a dedicated `audio_output` section to your [/etc/mpd.conf]:

[FILE] **`/etc/mpd.conf`**

    audio_output

** Note**\
If running pipewire with libpulse, this option will allow a system level MPD daemon to access the user level pipewire server if one of the tcp options is enabled in /etc/pipewire/pipewire-pulse.conf. See \"Adding multi user support\" in the [Pipewire](https://wiki.gentoo.org/wiki/Pipewire "Pipewire") page.

** Note**\
It may be a good practice to [run both PulseAudio and MPD under X11 user instead](#Per-user_configuration).

#### [][Pipewire (optional)]

If MPD was build with [Pipewire](https://wiki.gentoo.org/wiki/Pipewire "Pipewire") support (`pipewire` USE flag), add a dedicated `audio_output` section to your [/etc/mpd.conf]:

[FILE] **`/etc/mpd.conf`**

    audio_output

** Note**\
Pipewire will not let an MPD system daemon access a user level pipewire socket, so this option should only be used if running MPD as a user level daemon.

#### [][Built-in HTTP streaming server (optional)]

If MPD was build with `network` USE flag, add a dedicated `audio_output` section to your [/etc/mpd.conf]:

[FILE] **`/etc/mpd.conf`**

    audio_output

    bind_to_address "0.0.0.0"

Replace `localhost` with `0.0.0.0` or a specific interface IP. Bind to address `0.0.0.0` means here: stream on all local found IP interfaces. You could change it to a specific interface IP address like e.g. `192.168.1.2` then the streaming server is bound to that interface IP only.

** Note**\
Some players require to specify the file format in the URL to be able to connect to the stream. Example: `http://192.168.1.2:8000/mpd.ogg`

#### [][Bluetooth headset (optional)]

Setup a Bluetooth headset first, according to the [Bluetooth headset](https://wiki.gentoo.org/wiki/Bluetooth_headset "Bluetooth headset") article.

##### [][ALSA (non-PulseAudio) setup with BlueZ 5]

Put a user level [\~/.asoundrc] file in MPD\'s `$HOME` directory, which is [/var/lib/mpd] by default. MPD will be able to control the volume of the headset.

[FILE] **`/var/lib/mpd/.asoundrc`**

    # Specify the parameters of the Bluetooth connection
    defaults.bluealsa

To be able to switch between the Bluetooth headset and the default sound card, add these lines to the `audio_output` section in [/etc/mpd.conf]:

[FILE] **`/etc/mpd.conf`**

    audio_output

    audio_output

MPD might crash when switching output \_while\_ playing (if so, pause before switching).

If you experience some issues while trying to play AAC or other files, like:

`user `[`$`]`mpd --no-daemon --stderr`

    ...
    alsa_output: Failed to open "My ALSA Device" [alsa]: Error opening ALSA device "bluealsa" (snd_pcm_hw_params): Invalid argument
    ...

Then add this line to your `audio_output`:

[FILE] **`/etc/mpd.conf`**

    format          "44100:16:2"

#### [][FIFO (optional)]

The FIFO output setup for the visualiser plugin which in the [[[media-sound/ncmpcpp]](https://packages.gentoo.org/packages/media-sound/ncmpcpp)[]] client. Following additional settings enable the FIFO functionality:

[FILE] **`/etc/mpd.conf`**

    audio_output

The `name` and `path` variables values can be set to reflect own needs.

#### [Service]

##### [OpenRC]

To start MPD:

`root `[`#`]`rc-service mpd start`

To start MPD at boot time, add it the default runlevel:

`root `[`#`]`rc-update add mpd default`

##### [systemd]

To start MPD immediately:

`root `[`#`]`systemctl start mpd`

To start MPD at boot time:

`root `[`#`]`systemctl enable mpd`

### [Per-user configuration]

It may be handy to run MPD configured for a specific user.

#### [Basic configuration]

Start with copying [/etc/mpd.conf] to [\$XDG_CONFIG_HOME/mpd/mpd.conf]. Then you need to adjust the configuration to your needs.

Sample configuration using PulseAudio output:

[FILE] **`$XDG_CONFIG_HOME/mpd/mpd.conf`**

    # Recommended location for database
    db_file                 "~/.mpd/database"

    # Input
    input

    # PulseAudio output
    audio_output

Now it should be possible to start MPD simply issuing:

`user `[`$`]`mpd`

#### [Service]

** Note**\
If your [cron](https://wiki.gentoo.org/wiki/Cron "Cron") program supports [\@reboot] you can create a cronjob that has [/usr/bin/mpd] start at boot in place of an init script.

##### [systemd]

It is possible to leverage [systemd] [user services](https://wiki.gentoo.org/wiki/Systemd#User_services "Systemd") to control MPD in a per-user way.

To activate the MPD, start the systemd socket:

`user `[`$`]`systemctl --user enable --now mpd.socket`

## [Clients]

-   [Sorted List of MPD clients](https://www.musicpd.org/clients/)

### [][Commandline/Console]

-   [[[media-sound/mpc]](https://packages.gentoo.org/packages/media-sound/mpc)[]] --- [A commandline client for Music Player Daemon (media-sound/mpd)](https://www.musicpd.org/clients/mpc/) (useful for key-bindings)
-   [[[media-sound/ncmpc]](https://packages.gentoo.org/packages/media-sound/ncmpc)[]] --- [An ncurses client for the Music Player Daemon (MPD)](https://www.musicpd.org/clients/ncmpc/)
-   [Ncmpcpp](https://wiki.gentoo.org/wiki/Ncmpcpp "Ncmpcpp") --- [An ncurses mpd client, ncmpc clone with some new features, written in C++](https://rybczak.net/ncmpcpp/)
-   [[[media-sound/pms]](https://packages.gentoo.org/packages/media-sound/pms)[]] --- [Practical Music Search, another ncurses based mpd client with vi like keys, written in Golang](https://kimtore.no/pms/)
-   [[[media-sound/vimpc]](https://packages.gentoo.org/packages/media-sound/vimpc)[]] --- [An ncurses based mpd client with vi like key bindings](https://github.com/boysetsfrog/vimpc)
-   [Ampc](https://elpa.gnu.org/packages/ampc.html) --- Asynchronous Music Player Controller for [Emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs")
-   [clerk](https://github.com/carnager/clerk) --- mpd client, based on rofi/fzf, written in Perl
-   [vimus](https://hackage.haskell.org/package/vimus) --- An MPD client with vim-like key bindings, written in Haskell

### [][Graphical (GTK)]

-   [[[media-sound/ario]](https://packages.gentoo.org/packages/media-sound/ario)[]]
-   [[[media-sound/gimmix]](https://packages.gentoo.org/packages/media-sound/gimmix)[]]
-   [[[media-sound/glurp]](https://packages.gentoo.org/packages/media-sound/glurp)[]]
-   [[[media-sound/sonata]](https://packages.gentoo.org/packages/media-sound/sonata)[]]
-   [[[media-sound/xfmpc]](https://packages.gentoo.org/packages/media-sound/xfmpc)[]]

### [][Graphical (Qt)]

-   [[[media-sound/cantata]](https://packages.gentoo.org/packages/media-sound/cantata)[]]
-   [[[media-sound/quimup]](https://packages.gentoo.org/packages/media-sound/quimup)[]]

### [][Graphical (other)]

-   [[[x11-plugins/wmmp]](https://packages.gentoo.org/packages/x11-plugins/wmmp)[]]

### [Web]

-   [ympd](https://www.ympd.org/) --- MPD Web GUI - written in C, utilizing Websockets and Bootstrap/JS

### [Scrobblers]

Scrobblers are clients that submit to [Audioscrobbler](https://www.audioscrobbler.net/) --- compatible services (eg. [libre.fm](https://libre.fm) or [last.fm](https://last.fm))

-   [[[media-sound/mpdas]](https://packages.gentoo.org/packages/media-sound/mpdas)[]]
-   [[[media-sound/mpdscribble]](https://packages.gentoo.org/packages/media-sound/mpdscribble)[]]
-   [[[media-sound/scmpc]](https://packages.gentoo.org/packages/media-sound/scmpc)[]]

## [Troubleshooting]

For general troubleshooting refer to the [MPD user manual troubleshooting section](https://mpd.readthedocs.io/en/stable/user.html#troubleshooting)

### [No Audio from PulseAudio]

Running mpd as a system service under the user \"mpd\" causes permissions issues. Change the user in [mpd.conf] to your current user.

[FILE] **`/etc/mpd.conf`**

    user "larry"

## [See also]

-   [Upmpdcli](https://wiki.gentoo.org/wiki/Upmpdcli "Upmpdcli") --- a free and open source UPnP media renderer front-end for Music Player Daemon (MPD).

## [External resources]

-   [MPD Forum](https://forum.musicpd.org/)
-   [MPD on Sourceforge](https://sourceforge.net/projects/musicpd/)
-   [MPD at Arch Wiki](https://wiki.archlinux.org/index.php/Music_Player_Daemon)