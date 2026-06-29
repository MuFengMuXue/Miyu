**Resources**

[[]][Home](https://www.bowerswilkins.com/en-us/product/headphones/px7)

The Bowers and Wilkins PX7 headphones have bluetooth, USB-C, and 3.5mm TRS connections to audio sources. These are battery-powered high-sensitivity headphones that are known to work well with ALSA using the analog and USB-C connections.

This article describes using a USB-C source with [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA"). See [Bluetooth_headset](https://wiki.gentoo.org/wiki/Bluetooth_headset "Bluetooth headset") for bluetooth connection information. The described configuration and testing use *alsamixer*, *aplay*, and *speaker-test* (from [[[media-sound/alsa-utils]](https://packages.gentoo.org/packages/media-sound/alsa-utils)[]]) for testing, and [[[media-video/smplayer]](https://packages.gentoo.org/packages/media-video/smplayer)[]] and [[[media-video/mplayer]](https://packages.gentoo.org/packages/media-video/mplayer)[]] for audio playback.

** Note**\
The PX7 V2 is a newer model with different connections. It is unknown how well these instructions work for that model.

## Contents

-   [[1] [Software]](#Software)
-   [[2] [Hardware]](#Hardware)
    -   [[2.1] [Standard]](#Standard)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Kernel]](#Kernel)
    -   [[3.2] [Emerge]](#Emerge)
    -   [[3.3] [Testing the hardware]](#Testing_the_hardware)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [ALSA configuration]](#ALSA_configuration)
    -   [[4.2] [Playback using smplayer]](#Playback_using_smplayer)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [No audio output \-- first steps]](#No_audio_output_--_first_steps)
    -   [[5.2] [No audio output in speaker-test]](#No_audio_output_in_speaker-test)
    -   [[5.3] [No audio output in smplayer]](#No_audio_output_in_smplayer)
    -   [[5.4] [Low volume / large variation in volume between sources]](#Low_volume_.2F_large_variation_in_volume_between_sources)
-   [[6] [References]](#References)

## [Software]

-   [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA")
-   [[[media-plugins/alsa-plugins]](https://packages.gentoo.org/packages/media-plugins/alsa-plugins)[]]
-   [[[media-sound/alsa-utils]](https://packages.gentoo.org/packages/media-sound/alsa-utils)[]]
-   [[[media-video/smplayer]](https://packages.gentoo.org/packages/media-video/smplayer)[]]
-   [[[media-video/mplayer]](https://packages.gentoo.org/packages/media-video/mplayer)[]]

\
These USE flags are set:

[FILE] **`/etc/porage/package.use`**

    media-plugins/alsa-plugins ffmpeg mix usb_stream
    media-video/mplayer alsa

## [Hardware]

When the PX7 is plugged in to a *USB* port and powered on, multiple USB devices are created. This article uses this device (trimmed output shown):

`user `[`$`]`lsusb -v -d 19b5:0025`

    Bus 001 Device 010: ID 19b5:0025 B & W Group PX7 Bowers & Wilkins
      bcdUSB               2.00
      bDeviceClass            0
      bDeviceSubClass         0
      bDeviceProtocol         0
      bMaxPacketSize0        64
      idVendor           0x19b5 B & W Group
      idProduct          0x0025
      bcdDevice           14.69
      iManufacturer           1
      iProduct                2 PX7 Bowers & Wilkins
        Interface Descriptor:
          bNumEndpoints           1
          bInterfaceClass         1 Audio
          bInterfaceSubClass      2 Streaming
          AudioStreaming Interface Descriptor:
            wFormatTag         0x0001 PCM
          AudioStreaming Interface Descriptor:
            bSamFreqType            7 Discrete
            tSamFreq[ 0]        96000
            tSamFreq[ 1]        48000
            tSamFreq[ 2]        44100
            tSamFreq[ 3]        32000
            tSamFreq[ 4]        22050
            tSamFreq[ 5]        16000
            tSamFreq[ 6]         8000
    Device Status:     0x0001
      Self Powered

\
The PX7 has proximity sensors that detect when they are being worn. When not being worn there is no audio, so testing while not wearing the headphones will appear to fail. Since these have a high-sensitivity, low-level input signals produce a higher than usual sound-level. Make sure to set the device volume to a lower level using *alsamixer* before starting. A starting value of 20 or so was useful when using *speaker-test*.

The headphone\'s volume controls do not control the volume of audio coming from USB or analog sources.

The PX7 USB connection runs at USB full-speed (480 MBit/s) and uses the USB Streaming protocol with S24_3LE format samples. The hardware reports support for many sample rates (e.g. 44100Hz) via `lsusb`, but the only rate that produced usable audio was 96000Hz.

The headphone drivers appear to always be powered from the battery even when connected via USB. The internal battery charges through the USB connection even when playing audio.

\

** Note**\
Even the though the USB speed is 480 MBit/s, the device must be plugged into a USB 3 port or better.

** Tip**\
The quality of the USB cable may be a safety issue ^[\[1\]](#cite_note-1)^

### [Standard]

  -------------------- ------------------------------------ ----------------------- ------------------------ ---------------------------------------- ---------------- ----------------------------------------------------------------
  Device               Make/model                           Status                  Vendor ID / Product ID   Kernel driver(s)                         Kernel version   Notes
  Wireless Headphone   B & W Group PX7 (Bowers & Wilkins)   Works (USB & Analog)    `19b5:0025`              snd-usb-audio (when built as a module)   5.19.3           Enable kernel option `SND_USB_AUDIO` in the kernel.
  -------------------- ------------------------------------ ----------------------- ------------------------ ---------------------------------------- ---------------- ----------------------------------------------------------------

## [Installation]

The only installation requirements are:

-   USB-3 Port (Type A or C). An extension cable of 6ft (2m) was successfully used.
-   A kernel with approriate modules (esp. usb-audio), no extra firmware required.
-   [[[media-libs/alsa-lib]](https://packages.gentoo.org/packages/media-libs/alsa-lib)[]] and [[[media-plugins/alsa-plugins]](https://packages.gentoo.org/packages/media-plugins/alsa-plugins)[]] with the above mentioned USE flags set.
-   Packages for testing: [[[media-sound/alsa-utils]](https://packages.gentoo.org/packages/media-sound/alsa-utils)[]].
-   Audio/video playback software, in this case [[[media-video/smplayer]](https://packages.gentoo.org/packages/media-video/smplayer)[]] and [[[media-video/mplayer]](https://packages.gentoo.org/packages/media-video/mplayer)[]].

### [Kernel]

[KERNEL]

    Device Drivers ->
      Sound card support ->
        Advanced Linux Sound Architecture ->
          USB sound devices ->
            <*/M> USB Audio/MIDI driver

Note that there have been times where not having all of the sound-related modules configured as modules has caused failures.

### [Emerge]

`root `[`#`]`emerge --ask --verbose media-libs/alsa-lib media-plugins/alsa-plugins media-sound/alsa-utils`

For the playback apps used in these instructions:

`root `[`#`]`emerge --ask --verbose media-video/mplayer media-video/smplayer`

### [Testing the hardware]

Plug the headphones into a USB-3 port and turn them on. Use *aplay -L* to see that the device is seen by ALSA. Use *alsamixer* to unmute and set the device\'s PCM volume control to a low level. Use [F6] to select the device **Bowers & Wilkins PX7**. A suggested starting level is 20. A high-level will produce very loud sound in *speaker-test*.

`user `[`$`]`speaker-test -Dplughw:Wilkins,0 -c2 -r96000`

This selects stereo output (`-c2`) with a 96KHz sample rate (`-r96000`). *speaker-test* appears to produce S16_LE samples which requires conversion to S24_3LE. Additionally the sample stream needs to be converted to the *USB Stream* protocol. Using `plughw` in the device specification makes this happen. Using `plug` or `hw` does not work.

Make sure to wear the headphones so the proximity sensors will enable output. Pink noise should be heard alternating on the left and right sides.

## [Configuration]

### [ALSA configuration]

Since the headphones may not always be plugged in, no configuration for setting the headphones as the default device is suggested. These instructions were all done with no [/etc/asound] or [\~/.asound.rc] present.

### [Playback using smplayer]

*smplayer* needs special configuration to select the correct device and set the sample rate to 96KHz.

Setting the audio output:

[CODE]

    Preferences >> Audio >> Output Driver >> Custom
        alsa:noblock:device=plughw=Wilkins.0

Setting the sample rate using the resample filter (passed to mplayer by smplayer):

[CODE]

    Preferences >> Advanced >> Audio Filter
        resample=96000

** Note**\
The fliter only accepts S16_LE sources. CD\'s, WAV, and MP3 sources are usually output in this format

## [Troubleshooting]

### [No audio output \-- first steps]

-   Make sure the kernel has the usb-audio module configured, and if a module, loaded

`user `[`$`]`lsmod`

-   Make sure [[[media-plugins/alsa-plugins]](https://packages.gentoo.org/packages/media-plugins/alsa-plugins)[]] is installed with the required USE flags

`user `[`$`]`qlist -IC alsa-plugins`

-   Check the connections on the computer and the headphones
-   Make sure the headphones are turned on
-   The headphones must be worn to enable audio output
-   Check the device muting and volume settings

`user `[`$`]`alsamixer`

### [No audio output in speaker-test]

-   Proximity sensors disabled audio

<!-- -->

       make sure of a good fit

-   Sample format issues in speaker-test:

<!-- -->

       Various messages, including no support for s24_3LE -- use an empty /etc/asound
       A short burst of buzzing and then silence -- use a 96KHz sample rate

### [No audio output in smplayer]

Use View \>\> Mplayer/mpv log to see error messages

-   Make sure the output device is custom and uses plughw for the Wilkins device
-   Make sure the resampling filter has been specified for pass through to mplayer
-   Check the application muting and volume level. Gradually increase to the maximum.

### [][Low volume / large variation in volume between sources]

-   Increase the device master volume to 33 in *alsamixer*
-   Set the application volume level to middle to start, then adjust
-   Different sources just have different volume ranges, adjust the volume as needed

## [References]

1.  [[[↑](#cite_ref-1)] [We tested 43 old USB-C to USB-A cables. 1 was great. 10 were dangerous [\[1\]](https://www.pcworld.com/article/1063892/we-tested-43-old-usb-c-to-usb-a-cables-1-was-great-10-were-dangerous.html). Retrieved on September 22nd, 2022.]]