Information about whether a device works on Linux or not can sometimes take a little effort to track down, and is sometimes not even available. Hopefully the information here can help people make decisions about purchasing hardware for Linux, and provide a quick reference for Gentoo users. The [first section of this article](#Choosing_Linux_compatible_hardware) has advice on how to choose hardware for use with Gentoo, or indeed for any Linux system.

## Contents

-   [[1] [Choosing Linux compatible hardware]](#Choosing_Linux_compatible_hardware)
-   [[2] [Hardware devices]](#Hardware_devices)
    -   [[2.1] [Audio Interfaces]](#Audio_Interfaces)
    -   [[2.2] [Input peripherals]](#Input_peripherals)
    -   [[2.3] [Printers / AIOs]](#Printers_.2F_AIOs)
    -   [[2.4] [Webcams / image capture / digital cameras]](#Webcams_.2F_image_capture_.2F_digital_cameras)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
    -   [[4.1] [Linux certified hardware]](#Linux_certified_hardware)

## [Choosing Linux compatible hardware]

Like with any Operating System, it is always a good idea to purchase hardware that is supported by Linux. Don\'t forget that the physical system itself must also support new hardware. A PCI card, for example, will often not slot into a modern motherboard, or some USB 3 devices may not work on a USB 2 port.

Nobody would go out and buy an Apple webcam and just expect it to entirely work in Windows, or blindly purchase a graphics board and expect it to work on a Mac. With Linux, things are similar, though Linux has very broad compatibility with many devices.

Linux is particularly good at supporting older hardware - commercial vendors often do not update drivers when a new proprietary OS version is released, and effectively render good hardware obsolete. Open source Linux drivers in the kernel will usually work for years with hardware that has been rendered useless on other operating systems.

The very best way to ensure compatibility is to buy hardware that is supported on Linux by the manufacturer. Unfortunately, many vendors still do not advertise Linux support, even for devices that work perfectly well on Linux. There are some vendors that offer systems with Linux pre-installed, and buying such a machine can provide a high level of confidence in compatibility. Some distributions also certify hardware, see [Linux certified hardware](#Linux_certified_hardware) section.

If no \"official\" information can be found on Linux compatibility, searching the Internet can often turn up useful information, often from other distribution\'s sites, wikis, or forums, and even sometimes from sites like YouTube.

It is usually better to buy hardware for which Open Source drivers exist. Though some manufactures provide binary drivers for Linux, these can be a hassle to set up, and run the risk of becoming unusable when they are not maintained. One notorious example are Nvidia graphics cards, which can often be more complicated to set up than AMD or Intel cards.

Also consider that even if there are Linux drivers in the kernel for a particular piece of hardware, some devices require specific userspace software to function. It is a good idea to look at what software is available on Gentoo to *use* a device - especially for devices with which proprietary software supplied by the vendor is usually required.

** Tip**\
Hardware that works on \"Linux\" in general, usually will work on Gentoo. Basically, for a given device, if there is a working driver and the userspace programs to use the hardware, it should work.

## [Hardware devices]

### [Audio Interfaces]

Sound cards that conform to the [USB audio device class](https://en.wikipedia.org/wiki/USB_audio_device_class "wikipedia:USB audio device class"), should \"just work\". Some high end, \"pro\", interfaces are designed to work only with the manufactures production software, and use proprietary protocols - be sure to check compatibility before buying such devices. There is are lists of recommended audio software on the wiki: [audio players](https://wiki.gentoo.org/wiki/Recommended_applications#Audio_players "Recommended applications"), [audio aquisition](https://wiki.gentoo.org/wiki/Recommended_applications#Audio "Recommended applications"), and [music production](https://wiki.gentoo.org/wiki/Music_production "Music production").

### [Input peripherals]

Many keyboards, pointing devices, game controllers, etc. conform to the [USB human interface device class](https://en.wikipedia.org/wiki/USB_human_interface_device_class "wikipedia:USB human interface device class") (USB HID). These devices should work well, though additional software may be required for advanced functionality on the more specialized devices.

### [][Printers / AIOs]

Lots of printers work very well in Linux, some models may be problematic however, so it can be useful to look up compatibility before purchases. Even manufactures who generally support Linux well can have some models that can be difficult to get working at all.

### [][Webcams / image capture / digital cameras]

Video devices that conform to the [USB video device class](https://en.wikipedia.org/wiki/USB_video_device_class "wikipedia:USB video device class") (UVC) should work well. There is a list of [reccomended software](https://wiki.gentoo.org/wiki/Recommended_applications#Video "Recommended applications") for working with video devices on the wiki.

## [See also]

-   [Category:Hardware](https://wiki.gentoo.org/wiki/Category:Hardware "Category:Hardware") - wiki hardware category, for more in-depth information.
-   [Hardware_detection](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") --- lists and describes utilities used to detect and provide information on hardware.
-   [Recommended_applications#Hardware_management](https://wiki.gentoo.org/wiki/Recommended_applications#Hardware_management "Recommended applications") - software to detect hardware.

## [External resources]

-   [ALSA SoundCard Matrix](https://www.alsa-project.org/main/index.php/Matrix:Main) - ALSA audio interface compatibility.
-   [Hardware resources on Distrowatch](https://distrowatch.com/dwres.php?resource=hardware) - Linux/BSD compatible hardware resources.
-   [Linux hardware on Reddit](https://www.reddit.com/r/linuxhardware/)
-   [Open Printing](https://www.openprinting.org/printers) - Linux printer support database.
-   [SUSE hardware portal](https://en.opensuse.org/Portal:Hardware) - hardware compatibility matrix.
-   [Ubuntu hardware support](https://wiki.ubuntu.com/HardwareSupport) - Ubuntu Wiki has some information on hardware support on that system.

### [Linux certified hardware]

-   [Red Hat certified hardware](https://catalog.redhat.com/hardware)
-   [Ubuntu certified hardware](https://ubuntu.com/certified)