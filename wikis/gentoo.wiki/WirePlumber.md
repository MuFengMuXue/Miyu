[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=WirePlumber&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://gitlab.freedesktop.org/pipewire/wireplumber)

[[]][Official documentation](https://pipewire.pages.freedesktop.org/wireplumber/)

[[]][Package information](https://packages.gentoo.org/packages/media-video/wireplumber)

[[]][GitLab](https://gitlab.com/https://gitlab.freedesktop.org/pipewire/wireplumber)

**WirePlumber** is a modular session / policy manager for [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire"), enabling functionality such as saving and restoring session state. More generally, WirePlumber allows one to:

-   enable devices;
-   configure devices;
-   configure client (e.g. application) access control;
-   configure PipeWire nodes;
-   manage links between PipeWire nodes;
-   manage metadata.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Services]](#Services)
        -   [[2.1.1] [systemd]](#systemd)
        -   [[2.1.2] [OpenRC]](#OpenRC)
        -   [[2.1.3] [User Services]](#User_Services)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Examples]](#Examples)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Stuttering on a VM]](#Stuttering_on_a_VM)
    -   [[4.2] [Disabling or delaying audio sink suspension]](#Disabling_or_delaying_audio_sink_suspension)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [Kernel]

[KERNEL]

    Device Drivers  --->
      <*> Sound card support Search for <code>CONFIG_SOUND</code> to find this item.  --->
        <*> Advanced Linux Sound Architecture Search for <code>CONFIG_SND</code> to find this item.  --->
          -*-  Sound Proc FS Support Search for <code>CONFIG_SND_PROC_FS</code> to find this item.
          [*]    Verbose procfs contents Search for <code>CONFIG_SND_VERBOSE_PROCFS</code> to find this item.

### [USE flags]

### [USE flags for] [media-video/wireplumber](https://packages.gentoo.org/packages/media-video/wireplumber) [[]] [Replacement for pipewire-media-session]

  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+doc`](https://packages.gentoo.org/useflags/+doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`elogind`](https://packages.gentoo.org/useflags/elogind)                 Enable session tracking via sys-auth/elogind
  [`system-service`](https://packages.gentoo.org/useflags/system-service)   Install systemd unit files for running as a system service. Not recommended.
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                 Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-06 10:20] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-video/wireplumber`

## [Configuration]

Generally, WirePlumber should work \"out of the box\", without any need for manual configuration. However, a sample WirePlumber configuration file is available at [/usr/share/wireplumber/wireplumber.conf]; this file can be copied to [\~/.config/wireplumber/] and modified as required. (The [\~/.config/wireplumber/] directory might need to be created manually.)

### [Services]

#### [systemd]

`user `[`$`]`systemctl --user enable --now wireplumber.service`

#### [OpenRC]

OpenRC users should run [gentoo-pipewire-launcher]; refer to [this section of the PipeWire page](https://wiki.gentoo.org/wiki/PipeWire#gentoo-pipewire-launcher "PipeWire") for details.

#### [User Services]

** Warning**\
As of 2025-12-11, this method is still in development. Unless you are an expert or want to experiment, please use the [gentoo-pipewire-launcher] method for OpenRC systems for now. Refer to [[[bug #964059]](https://bugs.gentoo.org/show_bug.cgi?id=964059)[]] for a discussion of pending work.

OpenRC has built-in and enabled by default support for user services since version 0.60 [OpenRC#User_services](https://wiki.gentoo.org/wiki/OpenRC#User_services "OpenRC"). Similarly to systemd, they can be used to automatically launch and stop WirePlumber on login and logout.

To enable the WirePlumber service run:

`user `[`$`]`rc-update add -U wireplumber default `

To start the service without enabling it:

`user `[`$`]`rc-service --user wireplumber start `

## [Usage]

WirePlumber is controlled by [[[wpctl(1)]](https://man.archlinux.org/man/wpctl.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

`user `[`$`]`wpctl -h`

    Usage:
      wpctl [OPTION…] COMMAND [COMMAND_OPTIONS] - WirePlumber Control CLI

    Commands:
      status
      get-volume ID
      inspect ID
      set-default ID
      set-volume ID VOL[%][-/+]
      set-mute ID 1|0|toggle
      set-profile ID INDEX
      set-route ID INDEX
      clear-default [ID]
      settings [KEY] [VAL]
      set-log-level [ID] LEVEL

    Help Options:
      -h, --help       Show help options

    Pass -h after a command to see command-specific options

The special identifiers `@DEFAULT_SINK@`, `@DEFAULT_AUDIO_SINK@`, `@DEFAULT_SOURCE@`, `@DEFAULT_AUDIO_SOURCE@`, and `@DEFAULT_VIDEO_SOURCE@` can be used when an ID is required; refer to the [[[wpctl(1)]](https://man.archlinux.org/man/wpctl.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for details.

### [Examples]

Get volume of current default sink:

`user `[`$`]`wpctl get-volume @DEFAULT_SINK@`

Set volume of current default sink to 90%:

`user `[`$`]`wpctl set-volume @DEFAULT_SINK@ 90%`

Decrease volume of current default audio sink by 5%:

`user `[`$`]`wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-`

Toggle muting of current default audio sink:

`user `[`$`]`wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle`

List details of current WirePlumber settings:

`user `[`$`]`wpctl settings`

List only the `Id` and `Value` fields for current settings:

`user `[`$`]`wpctl settings | sed -n '/Id:/p;/Value:/p'`

## [Troubleshooting]

### [Stuttering on a VM]

Stuttering on a VM may be caused by insufficient headroom for ALSA. By default, on a VM, the headroom is increased to 2048 in [/usr/share/wireplumber/wireplumber.conf.d/alsa-vm.conf].

Stuttering might be eliminated by raising the headroom to 8096: ^[\[1\]](#cite_note-1)^

[FILE] **`/etc/wireplumber/wireplumber.conf.d/30-alsa.conf`**

    monitor.alsa.rules = [

        ]
        actions =
        }
      }
    ]

### [Disabling or delaying audio sink suspension]

By default, audio devices are put into standby after 5 seconds of no audio. This can be annoying, because some devices take a few seconds to start up again. However, the delay can be configured or the functionality can be disabled completely.

To make it simple, the following user config applies to all audio sources and audio sinks.

`session.suspend-timeout-seconds = 0` disables the suspend functionality. Alternatively, the delay can be increased.

[FILE] **`~/.config/wireplumber/wireplumber.conf.d/51-disable-suspension.conf`**

    monitor.alsa.rules = [
      ,

        ]
        actions =
        }
      }
    ]
    # bluetooth devices
    monitor.bluez.rules = [
      ,

        ]
        actions =
        }
      }
    ]

When using `systemd`, restart `pipewire.service` and `pipewire-pulse.service` afterwards for the setting to take effect:

`user `[`$`]`systemctl restart --user pipewire.service pipewire-pulse.service`

Alternatively, reboot.

## [See also]

-   [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") --- low-latency, graph-based, processing engine and server, for interfacing with audio and video devices.

## [External resources]

-   [WirePlumber, the PipeWire session manager](https://www.collabora.com/news-and-blog/blog/2020/05/07/wireplumber-the-pipewire-session-manager/) - General introduction to WirePlumber
-   [WirePlumber](https://wiki.archlinux.org/title/WirePlumber) - ArchWiki page

## [References]

1.  [[[↑](#cite_ref-1)] [[Pipewire troubleshooting instructions](https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Troubleshooting#stuttering-audio-in-virtual-machine). Retrieved on 2024-09-02]]