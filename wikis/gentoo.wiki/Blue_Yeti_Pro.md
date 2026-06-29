**Resources**

[[]][Home](http://www.bluemic.com/yetipro/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Blue_Microphones "wikipedia:Blue Microphones")

The Blue Yeti Pro is a high quality, USB condenser microphone. It is popular among streaming.

Getting the Blue Yeti Pro operational in Gentoo requires the USB Audio/MIDI driver to be built-in to the kernel or, at minimum, snd-usb-audio built as a module.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
-   [[3] [Configuration]](#Configuration)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Hardware]

### [Standard]

  ---------------- --------------- -------- ------------- ---------------------------------------- ---------------- ----------------------------------------------------------------
  Device           Make/model      Status   Bus ID        Kernel driver(s)                         Kernel version   Notes
  USB microphone   Blue Yeti Pro   Works    `074d:0002`   snd-usb-audio (when built as a module)   4.4.1            Enable kernel option `SND_USB_AUDIO` in the kernel.
  ---------------- --------------- -------- ------------- ---------------------------------------- ---------------- ----------------------------------------------------------------

## [Installation]

### [Kernel]

[KERNEL] **Enable support for `SND_USB_AUDIO`**

    Device Drivers -->
       Sound card support -->
          Advanced Linux Sound Architecture -->
             USB sound devices -->
                <*> USB Audio/MIDI driver

## [Configuration]

Simply use the application of choice to select the Blue Yeti microphone as the system\'s input device.

## [See also]

-   [[lsusb](https://wiki.gentoo.org/wiki/Usbutils "Usbutils")] - A utility for listing devices attached to system via the USB bus.

## [External resources]

-   [https://forums.gentoo.org/viewtopic-t-797843-start-0.html](https://forums.gentoo.org/viewtopic-t-797843-start-0.html) - A Gentoo Forums post concerning the correct operation of a webcam.
-   [http://www.wolfmanzbytes.com/audio-gear/189-yeti-usb-microphone.html](http://www.wolfmanzbytes.com/audio-gear/189-yeti-usb-microphone.html) - A Yeti USB Microphone review.
-   [http://www.linux-hardware-guide.com/2014-01-06-blue-microphones-yeti-usb-microphone](http://www.linux-hardware-guide.com/2014-01-06-blue-microphones-yeti-usb-microphone)