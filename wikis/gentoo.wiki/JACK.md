[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=JACK&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

Other languages:

-   [English]

**Resources**

[[]][Home](http://jackaudio.org/)

[[]][Official documentation](https://jackaudio.org/faq/)

[[]][Official documentation](https://github.com/jackaudio/jackaudio.github.com/wiki)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/jack2)

[[]][Wikipedia](https://en.wikipedia.org/wiki/JACK_Audio_Connection_Kit "wikipedia:JACK Audio Connection Kit")

JACK, **J**ACK **A**udio **C**onnection **Kit**, is a sound server for professional audio production that provides low-latency communication for applications that implement the JACK API, such as [Ardour](https://wiki.gentoo.org/wiki/Ardour "Ardour") and [mpv](https://wiki.gentoo.org/wiki/Mpv "Mpv").

** Tip**\
JACK is designed to work with **only one active audio interface** (sound card), because of technical reasons needed to guarantee audio quality, latency, and synchronization. Remember, JACK is designed for studio quality work, not for ease of use. If more, or different, inputs and outputs are needed, use a different audio interface. It may be possible to get multiple interfaces working at the same time with JACK, but it is not trivial, and results may vary.

** Note**\
When the JACK daemon is running, usual system sound may no longer be output. To restore sound there are several options^[\[1\]](#cite_note-1)^, such as configuring applications to output to JACK, using a second soundcard, or [section#Bridging].

## Contents

-   [[1] [Background]](#Background)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
    -   [[2.3] [Global JACK USE flag]](#Global_JACK_USE_flag)
    -   [[2.4] [Additional software]](#Additional_software)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Sound server]](#Sound_server)
    -   [[3.2] [Bridging]](#Bridging)
        -   [[3.2.1] [ALSA]](#ALSA)
            -   [[3.2.1.1] [Loopback device]](#Loopback_device)
                -   [[3.2.1.1.1] [Kernel configuration]](#Kernel_configuration)
                -   [[3.2.1.1.2] [Jack ALSA plugin]](#Jack_ALSA_plugin)
        -   [[3.2.2] [PulseAudio]](#PulseAudio)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [\"Cannot use real-time scheduling\" error]](#.22Cannot_use_real-time_scheduling.22_error)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)

## [Background]

The following is a general introduction to JACK; some parts of it might be outdated.

JACK adds a layer to ALSA that guarantees constant sound latency and synchronous operation to all its clients. JACK can only use one sound card at a time, and will provide separated outputs and inputs for each audio channel of the sound card. JACK further provides the ability to view, manipulate or pipe audio streams, both hardware and software streams, in a similar manner to using cables to interface different audio equipment. For example, [JAMin](https://jamin.sourceforge.net) can intercept an audio stream before exporting the stream to another audio application and/or through analog or S/PDIF outputs. The user-owned JACK daemon is usually started using [[[media-sound/qjackctl]](https://packages.gentoo.org/packages/media-sound/qjackctl)[]], which provides many other functions, including audio stream connections.

JACK does not handle A/52 encoded (AC-3 or Dolby/DTS) material on input. It\'s just a sound server that deals with separated channels of audio streams, with the capability to connect - simultaneously and synchronously - any output stream on any input, and any input to any output stream, on any hardware and software audio component, with a constant latency. This makes JACK an outstanding tool for audio production and creation. The [ac3jack](https://sonosaurus.com/ac3jack/) tool can be used for encoding multiple separated audio channels to AC-3 streams.

When playing A/52 encoded media, the player will request as many outputs from JACK as audio channels in the media; this will fail if the sound card being used doesn\'t have the requested amount of audio outputs. For example, when using [MPlayer](https://wiki.gentoo.org/wiki/MPlayer "MPlayer"), it will need to be configured to output a 5.1 stream on a 7.1 output configuration, or a 7.1 stream on a 2 channel stereo output.

One solution is to configure the kernel and ALSA according to the JACK installation instructions for providing low-latency audio. Since ALSA is said to already be very efficient and low latency, providing very good quality playback with no additional mixing when appropriately configured via an [\~/.asoundrc] and/or [/etc/asoundrc], JACK probably isn\'t needed for most situations. The main audience of JACK is audio producers and musicians (in studio, live performances, DJing, etc). The proaudio-gentoo overlay is available via eselect-repository.

For an older solution using the zita-ajbridge, refer to \"[Using an ALSA Loopback device and zita-ajbridge](https://web.archive.org/web/20220314041206/https://proaudio.tuxfamily.org/wiki/index.php?title=DAW_Digital_Audio_Workstation#Using_an_ALSA_Loopback_device_and_zita-ajbridge)\" on the ProAudio Gentoo overlay wiki.

Using zita-ajbridge, it is also possible to add additional real sound cards into JACK.

Those wanting to try JACK should know that a realtime (RT) kernel and RT operations are only needed when using the computer as a Digital Audio Workstation (DAW). A DAW necessitates something [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") is not able to achieve: synchronous operations, and constant sound latency as low or lower than 20 msec. (PulseAudio is not able to provide constant sound latency at all.) JACK can be an alternative to PulseAudio for users that want a professional solution.

## [Installation]

JACK uses [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") for accessing the sound card hardware, be sure ALSA is working.

There are two implementations of the JACK API, both implementations are considered equivalent. **JACK2 is usually the one to go for**, JACK 1 is no longer under active development.

JACK is the original implementation, it uses a C API and has built-in Linux MIDI integration. JACK2 is a re-implementation in C++ that has support for multiprocessing and [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus"), while MIDI support is handled by ALSA. Visit [what are the differences between JACK 1 and JACK2](https://github.com/jackaudio/jackaudio.github.com/wiki/Differences-between-jack1-and-jack2) for an in-depth comparison.

### [USE flags]

### [USE flags for] [media-sound/jack2](https://packages.gentoo.org/packages/media-sound/jack2) [[]] [Jackdmp jack implemention for multi-processor machine]

  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`+alsa`](https://packages.gentoo.org/useflags/+alsa)                   Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`+classic`](https://packages.gentoo.org/useflags/+classic)             Enable building of jackd
  [`+tools`](https://packages.gentoo.org/useflags/+tools)                 Pull basic tools (e.g. jack_lsp/connect) from media-sound/jack-example-tools
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                     Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`doc`](https://packages.gentoo.org/useflags/doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`ieee1394`](https://packages.gentoo.org/useflags/ieee1394)             Enable FireWire/iLink IEEE1394 support (dv, camera, \...)
  [`libsamplerate`](https://packages.gentoo.org/useflags/libsamplerate)   Build with support for converting sample rates using libsamplerate
  [`metadata`](https://packages.gentoo.org/useflags/metadata)             Enable metadata API
  [`opus`](https://packages.gentoo.org/useflags/opus)                     Enable Opus audio codec support
  [`pam`](https://packages.gentoo.org/useflags/pam)                       Add basic realtime configuration via sys-auth/realtime-base
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Enable use of systemd-specific libraries and features like socket activation or session tracking
  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-03 18:30] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge the sound server:

`root `[`#`]`emerge --ask media-sound/jack2`

** Warning**\
JACK2 will successfully compile with [LTO](https://wiki.gentoo.org/wiki/LTO "LTO") enabled, but incoming connections will suffer a segmentation fault, fail to see ports, or fail to connect to open ports. Be sure to compile without LTO for a functional experience.

The JACK 1 package is [[[media-sound/jack-audio-connection-kit]](https://packages.gentoo.org/packages/media-sound/jack-audio-connection-kit)[]] (link provides a list of JACK 1 USE flags).

### [Global JACK USE flag]

The global [`jack`](https://packages.gentoo.org/useflags/jack) USE flag enables support for JACK in other packages, so they can submit sound to a JACK server:

`root `[`#`]`euse -E jack`

The [euse] command is part of [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]].

After setting this, be sure to update the system so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

### [Additional software]

There is a JACK configuration and control software package [[[media-sound/cadence]](https://packages.gentoo.org/packages/media-sound/cadence)[]]:

`root `[`#`]`emerge --ask media-sound/cadence`

Another alternative is [[[media-sound/qjackctl]](https://packages.gentoo.org/packages/media-sound/qjackctl)[]]:

`root `[`#`]`emerge --ask media-sound/qjackctl`

See the article on [music production](https://wiki.gentoo.org/wiki/Music_production "Music production") for software to use with JACK.

The JACK website has a page on [sofware that uses JACK](https://jackaudio.org/applications/).

## [Configuration]

### [Sound server]

All users that need JACK should be in the **audio** group:

`root `[`#`]`usermod -a -G audio $USERNAME`

JACK can be configured using the [jack_control] utility. A basic configuration script for JACK could look like:

[CODE] **A basic configuration**

    jack_control start
    jack_control ds alsa
    jack_control dps device hw:2,0
    jack_control dps rate 48000
    jack_control dps nperiods 2
    jack_control dps period 64

To determine the appropriate playback device (instead of [hw:2,0]):

`user `[`$`]`aplay -l`

### [[] Bridging]

JACK can route sound which was sent to other sound systems like [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio")^[\[2\]](#cite_note-2)^ and [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") through itself.

#### [ALSA]

To use the ALSA only applications with JACK, you will need 2 things: the snd_aloop module and the jack ALSA plugin.

The snd-aloop is the Loopback virtual sound card. This will be used as the default ALSA sound card. That allow the ALSA applications to use it without the need to change their default configuration, the jack ALSA plugin will then route these applications to the JACK graph.

`ALSA application <=> Loopback <=> ALSA jack plugin <=> JACK`

##### [Loopback device]

###### [Kernel configuration]

Activate the following kernel options:

[KERNEL]

    Device Drivers --->
        <M> Sound card support
            <M> Advanced Linux Sound Architecture --->
                <*> Generic Sound Devices --->
                    <M> Generic loopback driver (PCM)

To configure the Loopback as the default ALSA sound card, we need to create the file [/etc/modprobe.d/alsa.conf]. Example with several sound cards, it\'s probably an overkill due to the evolution of the default ALSA configuration, but it has been working from years on several computers with very minor changes. It can also be used in other cases when the computer have several sound cards and a constancy order between reboot is a must.

Sound card 0 is the Loopback virtual device, sound card 1 and 2 are the built-in audio card which have 2 devices, one being the HDMI, sound card 3 is for an USB card.

[FILE] **`/etc/modprobe.d/alsa.conf`**

    # Alsa kernel modules' configuration file.

    options snd slots=snd-aloop,snd-hda-intel,snd-hda-intel,snd-usb-audio
    options snd-hda-intel index=1,2 model=1002:1637,1022:15e3

The cards index start from 0. For more details about that file, see [Alsa Opensrc Org support page for multiple sound cards configuration](https://alsa.opensrc.org/MultipleCards).

To get the model strings, use [lspci] (or [lsusb] for USB cards):

`root `[`#`]`lspci`

    04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller
    04:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller

`root `[`#`]`lspci -s 04:00.1 -n`

    04:00.1 0403: 1002:1637

`root `[`#`]`lspci -s 04:00.6 -n`

    04:00.6 0403: 1022:15e3

We instruct the kernel to load the virtual sound card:

[FILE] **`/etc/modules-load.d/alsa.conf`**

    snd-aloop

###### [Jack ALSA plugin]

The jack ALSA plugin provide a better and more elegant solution than the previous ones like the zita-ajbridge (see [Using an ALSA Loopback device and zita-ajbridge](https://web.archive.org/web/20220314041206/https://proaudio.tuxfamily.org/wiki/index.php?title=DAW_Digital_Audio_Workstation#Using_an_ALSA_Loopback_device_and_zita-ajbridge) on the ProAudio Gentoo overlay wiki - the author of zita-ajbridge will maybe disagree on that\...).

Installation:

### [USE flags for] [media-plugins/alsa-plugins](https://packages.gentoo.org/packages/media-plugins/alsa-plugins) [[]] [ALSA extra plugins]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+mix`](https://packages.gentoo.org/useflags/+mix)                     Enables upmix and vdownmix plugin
  [`+usb_stream`](https://packages.gentoo.org/useflags/+usb_stream)       Enables usb_stream plugin
  [`arcam_av`](https://packages.gentoo.org/useflags/arcam_av)             Enables Arcam AV control plugin
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`ffmpeg`](https://packages.gentoo.org/useflags/ffmpeg)                 Enable ffmpeg/libav-based audio/video codec support
  [`jack`](https://packages.gentoo.org/useflags/jack)                     Add support for the JACK Audio Connection Kit
  [`libsamplerate`](https://packages.gentoo.org/useflags/libsamplerate)   Build with support for converting sample rates using libsamplerate
  [`oss`](https://packages.gentoo.org/useflags/oss)                       Add support for OSS (Open Sound System)
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)         Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`speex`](https://packages.gentoo.org/useflags/speex)                   Add support for the speex audio codec (used for speech)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)         Verify upstream signatures on distfiles
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-16 00:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

We need at least the jack USE flag.

`root `[`#`]`emerge --ask media-plugins/alsa-plugins`

Configuration:

[FILE] **`~/.asoundrc`**

    pcm.!default
    }

    pcm.jack
        capture_ports
    }

    ctl.mixer0

That file is necessary when using qjackctl or the command line to manage the JACK server. Cadence will manage it for You: On its `System` tab, select `Bridge Type: ALSA -> Jack (Plugin)`.

Now, You can configure JACK to use the wanted and real sound card as usual, and all the ALSA applications will be available as per magic into the JACK graph.

#### [PulseAudio]

To use PulseAudio\'s JACK module [[[media-sound/pulseaudio]](https://packages.gentoo.org/packages/media-sound/pulseaudio)[]] needs to have the `jack` USE flag enabled.

In order to route all audio from PulseAudio to JACK, the JACK sink needs to be configured:

`user `[`$`]`pactl load-module module-jack-sink channels=2`

`user `[`$`]`pactl load-module module-jack-source`

`user `[`$`]`pacmd set-default-sink jack_out`

PulseAudio will recognize that JACK started and will bridge its audio to JACK.

## [Troubleshooting]

### [][\"Cannot use real-time scheduling\" error]

Some applications may show a permission error when trying to connect to Jack, for example:

[CODE] **Error message**

    ERROR: JACK: Cannot create thread res = 1
    ERROR: JACK: JackClient::AcquireSelfRealTime error
    ERROR: JACK: Cannot use real-time scheduling (RR/5) (1: Operation not permitted)

Adding the current user to the [realtime] group should solve this:

`root `[`#`]`usermod -a -G realtime $USERNAME`

Log out and log back in to apply group change.

## [See also]

-   [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") --- the Linux kernel\'s API for sound cards, together with an associated software framework
-   [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") --- low-latency, graph-based, processing engine and server, for interfacing with audio and video devices.
-   [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") --- a multi-platform, open source, *sound server* that provides a number of features on top of the low-level audio interface [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA")

## [References]

1.  [[[↑](#cite_ref-1)] [[https://jackaudio.org/faq/pulseaudio_and_jack.html](https://jackaudio.org/faq/pulseaudio_and_jack.html)]]
2.  [[[↑](#cite_ref-2)] [[https://jackaudio.org/faq/pulseaudio_and_jack.html](https://jackaudio.org/faq/pulseaudio_and_jack.html)]]