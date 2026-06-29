**Resources**

[[]][Home](https://github.com/badaix/snapcast)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/snapcast)

**Snapcast** (**S**y**n**chronous **a**udio **p**layer) plays audio streams time synchronized on multiple devices over network using a server and a client component. The server picks up an audio stream from a fifo pipe, thus it can be combined with any audio source that is able to write to a pipe. The Snapserver is able to handle multiple streams at once. The assignment of clients to streams and their volume is controlled via a JSON-API.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Basic Configuration]](#Basic_Configuration)
    -   [[2.1] [Server]](#Server)
    -   [[2.2] [Client]](#Client)
        -   [[2.2.1] [Desktop environment/selecting sound card]](#Desktop_environment.2Fselecting_sound_card)
-   [[3] [Audio source]](#Audio_source)
    -   [[3.1] [MPlayer example]](#MPlayer_example)
    -   [[3.2] [MPD example]](#MPD_example)
    -   [[3.3] [Multiple input streams]](#Multiple_input_streams)
-   [[4] [Controlling Snapcast]](#Controlling_Snapcast)
    -   [[4.1] [Snapdroid]](#Snapdroid)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/snapcast](https://packages.gentoo.org/packages/media-sound/snapcast) [[]] [Synchronous multi-room audio player]

  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+client`](https://packages.gentoo.org/useflags/+client)       Build and install Snapcast client component
  [`+expat`](https://packages.gentoo.org/useflags/+expat)         Enable the use of dev-libs/expat for XML parsing
  [`+flac`](https://packages.gentoo.org/useflags/+flac)           Add support for FLAC: Free Lossless Audio Codec
  [`+opus`](https://packages.gentoo.org/useflags/+opus)           Enable Opus audio codec support
  [`+server`](https://packages.gentoo.org/useflags/+server)       Build and install Snapcast server component
  [`+vorbis`](https://packages.gentoo.org/useflags/+vorbis)       Add support for the OggVorbis audio codec
  [`+zeroconf`](https://packages.gentoo.org/useflags/+zeroconf)   Support for DNS Service Discovery (DNS-SD)
  [`alsa`](https://packages.gentoo.org/useflags/alsa)             Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`jack`](https://packages.gentoo.org/useflags/jack)             Add support for the JACK Audio Connection Kit
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)     Build with PipeWire support
  [`python`](https://packages.gentoo.org/useflags/python)         Add optional support/bindings for the Python language
  [`sdl`](https://packages.gentoo.org/useflags/sdl)               Build client with SDL2 support
  [`soxr`](https://packages.gentoo.org/useflags/soxr)             Build with audio resampler support with media-libs/soxr
  [`ssl`](https://packages.gentoo.org/useflags/ssl)               Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tremor`](https://packages.gentoo.org/useflags/tremor)         Build with TREMOR version of vorbis
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-18 16:42] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-sound/snapcast`

## [Basic Configuration]

### [Server]

The Snapcast server should run as its own user:group e.g. [snapserver]:[snapserver] (default created during emerge).

A sample config that makes snapserver pick up an audio stream from the named pipe [/tmp/snapfifo] looks like this:

[FILE] **`/etc/conf.d/snapserver`**

    SNAPSERVER_USER="--user snapserver:snapserver"
    SNAPSERVER_OPTS="-d -s pipe:///tmp/snapfifo?name=default"

To start snapserver now run:

`root `[`#`]`rc-service snapserver start`

To start snapserver at boot time run:

`root `[`#`]`rc-update add snapserver default`

For all snapserver options please see [man snapserver].

### [Client]

The basic configuration for the client looks like this:

[FILE] **`/etc/conf.d/snapclient`**

    SNAPCLIENT_USER="--user snapclient:audio"
    SNAPCLIENT_OPTS="-d"

This will run snapclient as daemon using the default sound card. It will try to find servers on the network using [Avahi](https://wiki.gentoo.org/wiki/Avahi "Avahi"), if avahi-daemon is installed and running.

To start snapclient now run:

`root `[`#`]`rc-service snapclient start`

To start snapclient at boot time run:

`root `[`#`]`rc-update add snapclient default`

#### [][Desktop environment/selecting sound card]

To make use of PulseAudio/use snapclient in your desktop environment (to be able to use snapclient alongside with other audio sources, control its volume, etc.) you would start it as your desktop user instead of letting the init system control it.

To get a list of sound cards, and select the right one, run:

`user `[`$`]`snapclient -l `

0: null Discard all samples (playback) or generate zero samples (capture)

1: pulse PulseAudio Sound Server

\...

To use PulseAudio for example, use `1` with the `-s` command line option:

`user `[`$`]`snapclient -s 1`

Snapclient should now appear in your list of audio playing applications of PulseAudio.

## [Audio source]

To make some testing noise, random bytes can be shoved into the snapservers pipe:

`root `[`#`]`cat /dev/urandom > /tmp/snapfifo`

Snapcast can basically be used with anything that is able to write PCM audio to a fifo.

### [MPlayer example]

To make MPlayer play something over Snapcast use:

`root `[`#`]`mplayer <input> -novideo -channels 2 -srate 48000 -af format=s16le -ao pcm:file=/tmp/snapfifo`

### [MPD example]

To hear music with MPD over Snapcast create a new audio_output in the [mpd.conf] using the fifo module:

[CODE]

    audio_output

The sample rate setting is the default one used by Snapcast. Different sample rates can be used but must be set in the snapserver config file first.

### [Multiple input streams]

Snapcast is able to handle multiple input streams per server instance. The server also assigns the clients dynamically to streams.

Each stream is added with another `-s` option and its own fifo to the snapserver config.

[FILE] **`/etc/conf.d/snapserver`**

    SNAPSERVER_OPTS="-d -s pipe:///tmp/snap_kitchen?name=Kitchen -s pipe:///tmp/snap_livingroom?name=Livingroom"

## [Controlling Snapcast]

Assignment of streams to clients as well as volume, name, and latency of each client is controlled over a JSON-API provided by snapserver. The [API documentation](https://github.com/badaix/snapcast/blob/master/doc/json_rpc_api/v2_0_0.md) can be found on GitHub.

There are some (GUI-) implementations using that API, like

### [Snapdroid]

The developer of Snapcast also made an Android app, [Snapdroid](https://github.com/badaix/snapdroid).

It can connect clients to streams, set volumes, etc. Moreover it implements a Snapcast client on Android, making it possible to play a Snapcast stream on an Android device.