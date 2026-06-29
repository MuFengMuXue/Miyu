This page contains [[changes](https://wiki.gentoo.org/index.php?title=PulseAudio&diff=1426969)] which are not marked for translation.

\

**Resources**

[[]][Home](https://www.freedesktop.org/wiki/Software/PulseAudio/)

[[]][Official documentation](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/)

[[]][Package information](https://packages.gentoo.org/packages/media-libs/libpulse)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/pulseaudio-daemon)

[[]][Wikipedia](https://en.wikipedia.org/wiki/PulseAudio "wikipedia:PulseAudio")

[[]][GitWeb](https://cgit.freedesktop.org/pulseaudio/pulseaudio/)

[[]][GitLab](https://gitlab.freedesktop.org/pulseaudio/pulseaudio/)

**PulseAudio** (or **PA** for short) is a multi-platform, open source, *sound server* that provides a number of features on top of the low-level audio interface [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA"), such as:

-   Networking support (P2P and server mode).
-   Per-application volume controls.
-   Better cross-platform support.
-   Dynamic latency adjustment, which can be used to save power.
-   [Plugin modules](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/).

\

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [Kernel]](#Kernel)
    -   [[1.3] [USE flags]](#USE_flags)
        -   [[1.3.1] [Global]](#Global)
        -   [[1.3.2] [Package]](#Package)
    -   [[1.4] [Emerge]](#Emerge)
    -   [[1.5] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Permissions]](#Permissions)
    -   [[2.2] [Configuring other applications]](#Configuring_other_applications)
    -   [[2.3] [Without udev or systemd]](#Without_udev_or_systemd)
    -   [[2.4] [Headless server]](#Headless_server)
        -   [[2.4.1] [Server]](#Server)
        -   [[2.4.2] [Client]](#Client)
    -   [[2.5] [Allow multiple users to use PulseAudio concurrently]](#Allow_multiple_users_to_use_PulseAudio_concurrently)
    -   [[2.6] [Equalizer]](#Equalizer)
        -   [[2.6.1] [Enabling the required modules]](#Enabling_the_required_modules)
        -   [[2.6.2] [Choosing the equalizer sink]](#Choosing_the_equalizer_sink)
        -   [[2.6.3] [Control the equalizer levels]](#Control_the_equalizer_levels)
        -   [[2.6.4] [Known issues]](#Known_issues)
-   [[3] [Running]](#Running)
    -   [[3.1] [systemd]](#systemd)
    -   [[3.2] [OpenRC]](#OpenRC)
    -   [[3.3] [Manually]](#Manually)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [No sound]](#No_sound)
    -   [[4.2] [Corrupted audio]](#Corrupted_audio)
    -   [[4.3] [Enable debug mode]](#Enable_debug_mode)
    -   [[4.4] [Audio/Video out of sync]](#Audio.2FVideo_out_of_sync)
    -   [[4.5] [Dummy output]](#Dummy_output)
    -   [[4.6] [No guarantees on actual latencies]](#No_guarantees_on_actual_latencies)
    -   [[4.7] [In case of buffer under-run latencies are never decreased]](#In_case_of_buffer_under-run_latencies_are_never_decreased)
    -   [[4.8] [Re-sampling using up a lot of CPU time]](#Re-sampling_using_up_a_lot_of_CPU_time)
    -   [[4.9] [grsec and PulseAudio]](#grsec_and_PulseAudio)
    -   [[4.10] [Volume gets randomly louder or reset to 100%]](#Volume_gets_randomly_louder_or_reset_to_100.25)
    -   [[4.11] [In pavucontrol, unable to change output device for applications that use OpenAL]](#In_pavucontrol.2C_unable_to_change_output_device_for_applications_that_use_OpenAL)
    -   [[4.12] [Popping noises before playing a sound]](#Popping_noises_before_playing_a_sound)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [Prerequisites]

PulseAudio can use but does not need any of:

-   [sys-apps/systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") or
-   [sys-auth/elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") (remember to add `elogind -systemd` to global USE flag).

### [Kernel]

For motherboards containing HDA sound cards, use the following kernel option for improved power-saving only on machines that are **not** **[amd64]** or **[x86]** based:

[KERNEL]

    Device Drivers  --->
        <*> Sound card support  --->
            <*> Advanced Linux Sound Architecture  --->
                (2048) Pre-allocated buffer size for HD-audio driver

`CONFIG_HIGH_RES_TIMERS` is needed to avoid `(snd_pcm_recover) underrun` errors and degraded audio when some applications are using pulseaudio:

[KERNEL]

    General setup  --->
        Timers subsystem  --->
            [*] High Resolution Timer Support

** Note**\
Not all applications require `CONFIG_HIGH_RES_TIMERS` to operate properly. However, it is recommended for applications such as [[[media-sound/audacity]](https://packages.gentoo.org/packages/media-sound/audacity)[]], and good practice to enable it to ensure compatibility with other audio applications.

See also the [permissions section](https://wiki.gentoo.org/wiki/PulseAudio#Permissions "PulseAudio") for how to configure the kernel to provide the correct permissions for PA. Also see [ALSA\'s Kernel section](https://wiki.gentoo.org/wiki/ALSA#Kernel "ALSA") for setting the right kernel options for sound card detection.

### [USE flags]

#### [Global]

Several packages are aware of the global [[[pulseaudio]](https://packages.gentoo.org/useflags/pulseaudio)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") to enable support for PulseAudio in other packages. Enabling this USE flag in [make.conf](https://wiki.gentoo.org/wiki/Make.conf "Make.conf") will pull in [[[media-libs/libpulse]](https://packages.gentoo.org/packages/media-libs/libpulse)[]] automatically (after following the [Emerge](https://wiki.gentoo.org/wiki/PulseAudio#Emerge "PulseAudio") section):

[FILE] **`/etc/portage/make.conf`**

    USE="pulseaudio"

#### [Package]

These use flags can be [set for](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use") the package [[[media-libs/libpulse]](https://packages.gentoo.org/packages/media-libs/libpulse)[]] and [[[media-sound/pulseaudio-daemon]](https://packages.gentoo.org/packages/media-sound/pulseaudio-daemon)[]], independently from the global [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio) USE flag in \[\[: make.conf\| make.conf\]\] (which configures other packages on the system that can use Pulseaudio):

### [USE flags for] [media-libs/libpulse](https://packages.gentoo.org/packages/media-libs/libpulse) [[]] [Libraries for PulseAudio clients]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+asyncns`](https://packages.gentoo.org/useflags/+asyncns)   Use libasyncns for asynchronous name resolution.
  [`+glib`](https://packages.gentoo.org/useflags/+glib)         Add support to dev-libs/glib-based mainloop for the libpulse client library, to allow using libpulse on glib-based programs.
  [`X`](https://packages.gentoo.org/useflags/X)                 Add support for X11
  [`dbus`](https://packages.gentoo.org/useflags/dbus)           Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`doc`](https://packages.gentoo.org/useflags/doc)             Build the doxygen-described API documentation.
  [`gtk`](https://packages.gentoo.org/useflags/gtk)             Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)     Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)   Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After setting USE flags be sure to update the system so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

Once you have updated your system, you can emerge the PulseAudio package. Begin the installation by using the following command:

`root `[`#`]`emerge --ask media-libs/libpulse`

`root `[`#`]`emerge --ask media-sound/pulseaudio-daemon`

### [Additional software]

-   [[[media-sound/pavucontrol]](https://packages.gentoo.org/packages/media-sound/pavucontrol)[]] - Pulseaudio Volume Control, a [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") based mixer for PulseAudio. Alternatively, [[[media-sound/pavucontrol-qt]](https://packages.gentoo.org/packages/media-sound/pavucontrol-qt)[]] is the [Qt](https://wiki.gentoo.org/wiki/Qt "Qt") based version.
-   [[[media-sound/pulsemixer]](https://packages.gentoo.org/packages/media-sound/pulsemixer)[]] - CLI and curses mixer for PulseAudio
-   [[[media-sound/paprefs]](https://packages.gentoo.org/packages/media-sound/paprefs)[]] - PulseAudio Preferences, a configuration dialogue for PulseAudio.
-   [[[kde-plasma/plasma-pa]](https://packages.gentoo.org/packages/kde-plasma/plasma-pa)[]] KDE Plasma integrated PulseAudio configuration and mixing, but not as powerful as pavucontrol or paprefs.

## [Configuration]

### [Permissions]

** Note**\
This is the only supported configuration by upstream and Gentoo developers.

PulseAudio uses [udev](https://wiki.gentoo.org/wiki/Udev "Udev") to dynamically give access to the soundcards to the currently \"active\" user.

To make this possible, ACLs (Access Control Lists) are required:

[KERNEL]

    File systems  --->
       Pseudo filesystems  --->
          [*] Tmpfs virtual memory file system support (former shm fs)
          [*]    Tmpfs POSIX Access Control Lists

If a *desktop* [profile](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles") is not being used:

-   for systemd, check that [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] is installed with the `acl` USE flag enabled
-   for OpenRC, check that [[[sys-auth/pambase]](https://packages.gentoo.org/packages/sys-auth/pambase)[]] is installed.

\
When finished, verify the permissions are working correctly:

`user `[`$`]`getfacl /dev/snd/controlC0 | grep -Eo "user:.+:" | cut -d: -f2`

    <YOUR_USERNAME>

** Important**\
For systemd logind managed permissions to be respected, **no one may be part of the *audio* group** (not even even the user pulse). Remove any and all users from the audio group:

`root `[`#`]`gpasswd -d <user> audio`

### [Configuring other applications]

Some applications need to be configured to output to PulseAudio by default. A detailed list of these can be found on the PulseAudio wiki\'s [PerfectSetup page](http://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/PerfectSetup).

ALSA

The [[[media-plugins/alsa-plugins]](https://packages.gentoo.org/packages/media-plugins/alsa-plugins)[]] must be installed with the `pulseaudio` USE flag enabled:

`root `[`#`]`emerge --ask media-plugins/alsa-plugins`

[OSS](https://wiki.gentoo.org/wiki/OSS "OSS")

Enable the following module in [/etc/pulse/default.pa]:

[FILE] **`/etc/pulse/default.pa`**

    load-module module-oss

GStreamer

Several GConf keys must be set:

-   Manual with [gconftool]:

`user `[`$`]`gconftool-2 -t string --set /system/gstreamer/0.10/default/audiosink pulsesink `

`user `[`$`]`gconftool-2 -t string --set /system/gstreamer/0.10/default/audiosrc pulsesrc `

** Note**\
Some programs might still require GStreamer output plugin to be manually set to PulseAudio Audio Sink.

libao

Set the following in [/etc/libao.conf]:

[FILE] **`/etc/libao.conf`**

    default_driver=pulse

OpenAL

Set the following in [/etc/openal/alsoft.conf]:

[FILE] **`/etc/openal/alsoft.conf`**

    drivers = pulse

[MPlayer](https://wiki.gentoo.org/wiki/MPlayer "MPlayer")

Set the following in [/etc/mplayer/mplayer.conf]:

[FILE] **`/etc/mplayer/mplayer.conf`**

    ao=pulse

### [Without udev or systemd]

[] The information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=PulseAudio&action=edit).

** Warning**\
Using PulseAudio without udev or systemd is **not** recommended. This breaks both auto-detection and hot-plugging.

If using ALSA as a PulseAudio sink (output) and routing ALSA apps to PA but not using udev, set a specific device to be used. Otherwise, PulseAudio will use the ALSA device \"default\" as the sink, which may be routed back to PulseAudio, forming a loop. To avoid this, add the parameter *device=hw:0,0* (find the correct IDs by running *aplay -l*). In the following example, we use two soundcards, of which card 0, device 0 is used as a sink (audio output, e.g. speakers) and card 1, device 0 as a source (audio input, e.g. microphone). PulseAudio will still be able to access other cards than these but it needs these settings to avoid looping the *default* device in this setup.

[FILE] **`/etc/pulse/default.pa`Using a specific ALSA device as PulseAudio sink/source**

    load-module module-alsa-sink device=hw:0,0
    load-module module-alsa-source device=hw:1,0

** Note**\
Forgetting to specify this when using the ALSA sink/source modules, problems may only show up on restating PulseAudio (e.g. by logging out and back in or rebooting). There will be with no audio, a slow desktop environment and hanging applications until the loop is resolved, restart alsasound and kill all running pulseaudio processes.

### [Headless server]

[] The information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=PulseAudio&action=edit).

These instructions are for setting up a headless pulse audio server. Meaning a server which has no display on it but does have speakers. This provides the ability to use the remote server\'s speakers for audio output.

There are warnings in good dozen places for doing this, but it is the proper method.

#### [Server]

First configure USE flags and emerge the package. The system-wide USE flag is masked, so we have to unmask it.

`root `[`#`]`mkdir -p /etc/portage/profile`

`root `[`#`]`echo "-system-wide" >> /etc/portage/profile/use.mask`

`root `[`#`]`echo "media-sound/pulseaudio-daemon system-wide" >> /etc/portage/package.use`

`root `[`#`]`emerge --ask --oneshot pulseaudio-daemon`

Add the following two lines somewhere in the system.pa file:

[FILE] **`/etc/pulse/system.pa`**

    load-module module-native-protocol-tcp auth-ip-acl=1.2.3.0/24
    load-module module-alsa-sink

*Replace 1.2.3.0/24 with the network mask for accessing the server.*

** Note**\
With multiple ALSA devices, specify the device to use by adding [device] or [device_id] to the module-alsa-sink module

Tell the init script that we really do want to do this, and then start it up:

`root `[`#`]`echo "PULSEAUDIO_SHOULD_NOT_GO_SYSTEMWIDE=1" >> /etc/conf.d/pulseaudio `

`root `[`#`]`rc-update add pulseaudio default`

`root `[`#`]`rc-service pulseaudio start `

#### [Client]

`user `[`$`]`pacmd load-module module-tunnel-sink server=1.2.3.4`

    server (1.2.3.4) is the IP of the server.

For a more permanent solution, add the following to the default.pa file

[FILE] **`/etc/pulse/default.pa`**

    load-module module-tunnel-sink server=1.2.3.4

Now in the pulse audio volume control, there should be the remote server listed under [Output Devices]. Under playback there should be a button next to the *Mute audio* button that when clicked will switch that audio stream to whichever output required.

### [Allow multiple users to use PulseAudio concurrently]

In some situations, like software isolation, it may be desirable to run some programs as another users and have access to the PulseAudio daemon. By default, the PulseAudio daemon does not accept connections by secondary users.

The following configuration runs PulseAudio daemon using a UNIX socket that accepts connections from other users:

[FILE] **`/etc/pulse/default.pa.d/multi-user.pa`Make the daemon use a UNIX socket**

    load-module module-native-protocol-unix auth-anonymous=1 socket=/tmp/pulse-socket

The following configuration instructs the PulseAudio client library to use the previously defined UNIX socket:

[FILE] **`/etc/pulse/client.conf`Make the clients use the UNIX socket**

    default-server = unix:/tmp/pulse-socket

The above configuration allows different users to access the same sound server. Users do not need to be in the `audio`, `pulse-access`, or `pulse` groups.

** Note**\
PulseAudio server may need to be executed at startup (see section [Running](https://wiki.gentoo.org/wiki/PulseAudio#Running "PulseAudio")).

### [Equalizer]

** Note**\
The equalizer module is considered unstable and might be removed from pulseaudio. For more, see [the mailing list](http://lists.freedesktop.org/archives/pulseaudio-discuss/2014-March/020174.html).

Make sure pulseaudio was installed with the `equalizer` USE flag enabled.

#### [Enabling the required modules]

Add the following two lines somewhere in the default.pa file :

[FILE] **`/etc/pulse/default.pa`**

    load-module module-dbus-protocol
    load-module module-equalizer-sink

Restart the pulseaudio instance. This should be as easy as:

`user `[`$`]`pulseaudio -k `

`user `[`$`]`pulseaudio --start`

#### [Choosing the equalizer sink]

The command should list the index and name of the equalizer sink:

`user `[`$`]`pacmd list-sinks | grep -B1 -e "name:.*equalizer"`

Use [pavucontrol] or a similar program like [[[media-sound/pulsemixer]](https://packages.gentoo.org/packages/media-sound/pulsemixer)[]] to select the equalizer sink for sound output. It may be listed as a device starting with *FFT based equalizer*.

#### [Control the equalizer levels]

The equalizer levels can now be controlled with the Qt GUI called [qpaeq].

\

#### [Known issues]

-   Short sound events (e.g. the terminal bell) distort ongoing sound streams (e.g. music)

## [Running]

This section contains instructions for starting the PulseAudio daemon.

### [systemd]

To enable PulseAudio for the current user run:

`user `[`$`]`systemctl --user enable --now pulseaudio.service pulseaudio.socket`

Root can enable PulseAudio for all users:

`root `[`#`]`systemctl --global enable pulseaudio.service pulseaudio.socket`

### [OpenRC]

Running PulseAudio \"system-wide\" via an init script is strongly discouraged unless there is good reason to do so. It should instead be started by your desktop session; `/etc/xdg/autostart/pulseaudio.desktop` is a good place to start.

### [Manually]

The PulseAudio daemon may be launched as a daemon using:

`user `[`$`]`pulseaudio -D`

For example, if using [i3wm](https://wiki.gentoo.org/wiki/I3 "I3"):

[FILE] **`/home/user/.config/i3/config`**

    exec pulseaudio -D

## [Troubleshooting]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=pulseaudio&order=bug_id%20DESC)[]]
-   [Freedesktop.org bugtracker: known bugs](https://gitlab.freedesktop.org/pulseaudio/pulseaudio/-/issues)

Pulseaudio runtime info can be checked with one command:

`user `[`$`]`pa-info `

It prints useful info about all modules loaded and any error can happen while module loading the bootstrap sequence. When there is an issue with PulseAudio, remember to check [pa-info] output to start troubleshooting.

### [No sound]

-   **After installation**: If there is no sound while using ALSA, consider unmuting the sound card. Launch [alsamixer] and make sure each column has a green `00` under it (use the [m] key to toggle mute/unmute). Install [[[media-sound/pavucontrol]](https://packages.gentoo.org/packages/media-sound/pavucontrol)[]] and check if there is any output on the pavucontrol panel when playing audio.
-   **After installation on Intel Tiger Lake-H HD Audio**: If there is no sound on Intel Tiger Lake or newer platforms, they may need to load additional firmware file(s). These platforms likely need the [[[sys-firmware/sof-firmware]](https://packages.gentoo.org/packages/sys-firmware/sof-firmware)[]] package installed. Then, restart PulseAudio (reboot or relogin to user session).
-   **After upgrading the system**: pulseaudio\'s user configuration files can become corrupt. Deleting [\~/.pulse\*] configuration files and forcing fresh ones to be generated by restarting the daemon may fix no sound condition.

### [Corrupted audio]

Problem: Audio has strange distortion or static when playing an output.

Solution: There is probably an issue with the Pulse server. Kill and restart the server:

`user `[`$`]`pulseaudio --kill `

`user `[`$`]`pulseaudio --start `

Sometimes adding `tsched=0` to the [default.pa] file in order to disable time scheduling may also work:

[FILE] **`/etc/pulse/default.pa`**

    load-module module-udev-detect tsched=0

On some *very* rare occasions, pulseaudio may need [reinstalling](https://wiki.gentoo.org/wiki/Emerge "Emerge") in case of sound issues:

`root `[`#`]`emerge --ask --oneshot pulseaudio`

### [Enable debug mode]

To get more information, set the following in [/etc/pulse/daemon.conf]:

[FILE] **`/etc/pulse/daemon.conf`**

    log-level=debug

Afterward restart the daemon:

`user `[`$`]`pulseaudio -k`

### [][Audio/Video out of sync]

Problem: Out-of-sync problems experienced when using PulseAudio over a local network.

Solution: Add `tsched=0` to the [default.pa] file in order to disables time scheduling:

[FILE] **`/etc/pulse/default.pa`**

    load-module module-udev-detect tsched=0

Restart the daemon:

`user `[`$`]`pulseaudio --kill `

`user `[`$`]`pulseaudio --start `

### [Dummy output]

If the only playback device is the **Dummy Output**, PulseAudio cannot access the system sound devices. Either the user has no permissions (see section [Permissions](https://wiki.gentoo.org/wiki/PulseAudio#Permissions "PulseAudio") or another program is blocking access. Try:

`user `[`$`]`fuser -v /dev/snd/*`

It shows the relevant program. Close the program and reconfigure it to use PulseAudio.

### [No guarantees on actual latencies]

Currently PA provides whatever latency is possible at the moment. This can be be milliseconds to hundreds of a millisecond without regard to what applications require.

### [In case of buffer under-run latencies are never decreased]

Currently, if a buffer under-run occurs, PA buffers for longer increasing latency, but it then never tries to buffer for less until restart.

### [Re-sampling using up a lot of CPU time]

Re-sampling can require quite a lot of computational power, PA defaults are rather conservative but in certain cases can still take a significant toll, in such cases edit [/etc/pulse/daemon.conf] and consider changing *resample-method* to something less CPU intensive, *default-sample-format* and *default-sample-rate* can also affect CPU utilization with higher bit-depth and larger difference in sample-rate generally needing more resources (e.g. re-sampling 44.1 kHz to 48 kHz is faster than re-sampling either to 192 kHz). Since re-sampling is done per each channel per input, channel configuration and number of applications can affect performance as well.

Starting with version 7.0 there is also soxr resamplers made available by enabling the *sox* USE flag. In particular *resample-method = soxr-mq* should provide acceptable quality while even the higher quality and hence slower soxr-hq is still cheaper than the default speex-float-1. But be warned that the soxr resamplers have roughly 5-20 times higher latency than speex-float, in terms of time the worst case for soxr-mq/hq can be as high as 20 ms while soxr-vhq latency can in few specific setups reach over 27 ms. In terms of feeling 20 ms can range from unnoticeable to irritating depending on person and use case (the usual PA latency\'s lower bound is around 20-25 ms and more commonly often around 70-90 ms, for comparison).

** Note**\
Using a version of PA with Orc support can noticeably decrease CPU usage, too. Also PA has the ability, if certain conditions are met, to automatically switch sinks between common sampling rates, this effectively can avoid some re-sampling.

### [grsec and PulseAudio]

** Note**\
Gentoo no longer provides sys-kernel/hardened-sources with the grsecurity patches.^[\[1\]](#cite_note-1)^

Make sure the `CONFIG_GRKERNSEC_SYSFS_RESTRICT` kernel symbol is not enabled when using a grsecurity kernel. PulseAudio's module-udev-detect needs to access [/sys] to discover what cards are available on the system, and that kernel option disallows this for anyone but root.

### [][Volume gets randomly louder or reset to 100%]

This may be caused by misbehaving PulseAudio-enabled programs when PulseAudio has *flat volumes* feature enabled. Disable it in the daemon config:

[FILE] **`/etc/pulse/daemon.conf`**

    flat-volumes = no

### [][In pavucontrol, unable to change output device for applications that use OpenAL]

If changing the output device in pavucontrol has no effect, it could be an application using [[[media-libs/openal]](https://packages.gentoo.org/packages/media-libs/openal)[]], which has a configuration option that inhibits sink changes.

To disable this option, create a configuration file for OpenAL^[\[2\]](#cite_note-2)^:

[![](/images/thumb/3/31/Alsoft-config.png/300px-Alsoft-config.png)](https://wiki.gentoo.org/wiki/File:Alsoft-config.png)

[](https://wiki.gentoo.org/wiki/File:Alsoft-config.png "Enlarge")

[alsoft-config]

[FILE] **`~/.config/alsoft.conf`**

    [pulse]
    allow-moves=yes

Or, from the GUI, by running :

`user `[`$`]`alsoft-config`

### [Popping noises before playing a sound]

Pulseaudio hibernates when no sound is played. If you have a popping noise at boot and each time a sound is played, this is due to pulseaudio (re)starting. A workaround is to disable hibernation by creating [\~/.config/pulse/default.pa] with

[FILE] **`~/.config/pulse/default.pa`**

    .include /etc/pulse/default.pa
    .nofail
    unload-module module-suspend-on-idle
    .fail

## [See also]

-   [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") --- the Linux kernel\'s API for sound cards, together with an associated software framework
-   [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") --- low-latency, graph-based, processing engine and server, for interfacing with audio and video devices.

## [External resources]

-   [Getting DTS 5.1+ sound via S/PDIF or HDMI using PulseAudio](https://blogs.gentoo.org/mgorny/2021/07/25/getting-dts-5-1-sound-via-s-pdif-or-hdmi-using-pulseaudio/)
-   [PulseAudio\'s Frequently Asked Questions](https://www.freedesktop.org/wiki/Software/PulseAudio/FAQ) - official FAQ
-   [PulseAudio: The Perfect Setup](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/PerfectSetup/)
-   [More general troubleshooting tips](https://wiki.archlinux.org/index.php/PulseAudio/Troubleshooting)
-   [Why you should care about PulseAudio (and how to start doing it)](https://www.linux.com/news/why-you-should-care-about-pulseaudio-and-how-start-doing-it/)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://gitweb.gentoo.org/repo/sync/gentoo.git/tree/metadata/news/2017-08-19-hardened-sources-removal/2017-08-19-hardened-sources-removal.en.txt](https://gitweb.gentoo.org/repo/sync/gentoo.git/tree/metadata/news/2017-08-19-hardened-sources-removal/2017-08-19-hardened-sources-removal.en.txt)]]
2.  [[[↑](#cite_ref-2)] [John Allie. [pavucontrol won\'t change output on some apps](https://unix.stackexchange.com/questions/452907/), [stackexchange.com questions](https://unix.stackexchange.com/questions/), July 1, 2018. Retrieved on October 7, 2018.]]