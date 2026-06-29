This article details the necessary system configuration to support **speakers** and **microphones** connected to the system via USB. Laptops commonly include microphones connected to the USB as part of the integrated webcam hardware whereas many USB headsets include both microphones and speakers over USB for sound input and output.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [SND_USB_AUDIO]](#SND_USB_AUDIO)
-   [[2] [Testing]](#Testing)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Extremely high volume]](#Extremely_high_volume)
-   [[4] [See also]](#See_also)

## [Configuration]

### [Kernel]

#### [SND_USB_AUDIO]

The USB audio/MIDI kernel symbol must be enabled for USB speakers and microphones to work properly.

[KERNEL] **Enable support for `SND_USB_AUDIO`**

    Device Drivers -->
       Sound card support -->
          Advanced Linux Sound Architecture -->
             USB sound devices -->
                <*> USB Audio/MIDI driver

## [Testing]

Many desktop suites include a dedicated application for which to test the functionality webcam and/or voice recording software. Systems running the [Gnome](https://wiki.gentoo.org/wiki/Gnome "Gnome") desktop environment can utilize the [[[media-video/cheese]](https://packages.gentoo.org/packages/media-video/cheese)[]] application.

The CLI tool [[[media-sound/sox]](https://packages.gentoo.org/packages/media-sound/sox)[]] can also be used to record and playback sound for users not using Gnome.

## [Troubleshooting]

### [Extremely high volume]

When testing the microphone, it is common for the output to be very loud and grainy. This is often caused by the input volume of the microphone being too high. This can be solved by decreasing the volume using the audio server:

For PulseAudio:

`user `[`$`]`pactl set-source-volume $(pactl get-default-source) 50%`

For Pipewire:

`user `[`$`]`wpctl set-volume @DEFAULT_AUDIO_SOURCE@ 20%`

## [See also]

-   [USB to Ethernet Adapter](https://wiki.gentoo.org/wiki/USB_to_Ethernet_Adapter "USB to Ethernet Adapter")
-   [Kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") --- a central part of the Gentoo [operating system (OS)](https://en.wikipedia.org/wiki/operating_system "wikipedia:operating system")