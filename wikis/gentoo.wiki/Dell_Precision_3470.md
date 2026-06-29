**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/precision-14-3470-laptop/overview)

[[]][Specifications](https://dl.dell.com/content/manual32768888-precision-3470-setup-and-specifications.pdf)

[[]][Hardware Maintenance Manual](https://dl.dell.com/content/manual27374215-precision-3470-service-manual.pdf)

This article is a work in progress as I manage thru the installation and initial setup. Please add from your experience.

\

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Bluetooth]](#Bluetooth)
    -   [[3.2] [Fingerprint Reader]](#Fingerprint_Reader)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Intel video driver with \<=5.15 kernel]](#Intel_video_driver_with_.3C.3D5.15_kernel)
    -   [[4.2] [Xorg fails on boot but works later]](#Xorg_fails_on_boot_but_works_later)
-   [[5] [References]](#References)

## [Hardware]

### [Standard]

  ------------------------- -------------------------------- -------------- ------------------------ -------------------- ---------------- --------------------------------------------------
  Device                    Make/model                       Status         Vendor ID / Product ID   Kernel driver(s)     Kernel version   Notes
  CPU                       12th Gen Intel Core i7-1270p     Works                                   N/A                  6.1.2
  Video card (integrated)   Intel Iris                       Works                                                        6.1.2            Note example.
  Video card                Nvidia T550                      Works                                   nvidia (propriety)   6.1.2            Note example.
  Wifi                                                       Works
  Bluetooth                                                  Works
  Sound
  Camera (RGB)              Microdia Integrated Webcam FHD   Works          0c45:6733
  Camera (IR)                                                Works                                                                         Using v4l2. /dev/video0
  Fingerprint Reader        Broadcom ControlVault 3          Not working    0a5c:5843                                                      Not recognized by fprintd^[\[1\]](#cite_note-1)^

  ------------------------- -------------------------------- -------------- ------------------------ -------------------- ---------------- --------------------------------------------------

\

## [Installation]

Look at the troubleshooting section for info about installation media not loading.

For installation use kernel 6.1 and above (the 5.15) doesn\'t work. In order to do so, it is necessary at this time (January 4th, 2 3) to use the testing package. In order to do so add the \~amd64 keyword to the relevant packages. If using distribution kernel one can do so by creating the following file:

[FILE] **`/etc/portage/package.accept_keywords/gentoo-kernel`**

    ~sys-kernel/gentoo-kernel-6.1.2 ~amd64
    ~sys-kernel/dist-kernel-6.1.2 ~amd64

### [Kernel]

In order to get the framebuffer working at the earliest time possible (necessary for example if using encrypted LUKS root partition), you should enable the EFI framebuffer support:

[KERNEL] **Enable EFI-based Framebuffer Support (CONFIG_FB_EFI)**

    Device Drivers
    ->Graphics support
       ->Frame buffer Devices
          ->Support for frame buffer devices [y]
              ->EFI-based Framebuffer Support [y]

Alternatively, if you use the distribution kernel, you can create the following file to add the option:

[FILE] **`/etc/kernel/config.d/100_framebuffer.config`**

    #EFI framebuffer support
    CONFIG_FB_EFI=y

## [Configuration]

In order to boot the Gentoo installation media, first you need to disable secure boot.

### [Bluetooth]

Make sure to run appropriate service according to [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth"):

`root `[`#`]`rc-service bluetooth start`

`root `[`#`]`rc-update add bluetooth default`

### [Fingerprint Reader]

Fprintd does not recognize the fingerprint reader out of the box.

It seems that Ubuntu has a propriety driver for this fingerprint reader^[\[2\]](#cite_note-2)^.

## [Troubleshooting]

### [][Intel video driver with \<=5.15 kernel]

Using distribution kernel version 5.15 result in video freeze due to incompatible Intel display driver. One should use kernel 6.1 from testing. As long as kernel 6.1 is in testing, this can be done by adding the \~amd64 keyword prior to emerging the kernel. If the Gentoo liveUSB is used for the installation, it also sometimes freezes during loading. If that the case, either try again (for some reason this is not consistent with the liveUSB unlike with the install) or use a different distro liveUSB for the installation.

### [Xorg fails on boot but works later]

This is due to a race condition while loading the kernel modules and Xorg. Please add the i915 driver to the initramsfs.

[FILE] **`/etc/dracut.conf.d/nvidiaoptimus.conf`**

    force_drivers+=" i915 "

Regenerate the initramfs image:

`root `[`#`]`dracut --force`

Please see [NVIDIA/Optimus](https://wiki.gentoo.org/wiki/NVIDIA/Optimus#Xorg "NVIDIA/Optimus").

## [References]

1.  [[[↑](#cite_ref-1)] [[https://gitlab.freedesktop.org/libfprint/wiki/-/wikis/Unsupported-Devices](https://gitlab.freedesktop.org/libfprint/wiki/-/wikis/Unsupported-Devices)]]
2.  [[[↑](#cite_ref-2)] [[https://git.launchpad.net/\~oem-solutions-engineers/libfprint-2-tod1-broadcom/+git/libfprint-2-tod1-broadcom/](https://git.launchpad.net/~oem-solutions-engineers/libfprint-2-tod1-broadcom/+git/libfprint-2-tod1-broadcom/)]]