** Note**\
The Raspberry Pi 3 VC4 driver is ***not*** available on 64-bit (ARM64/AARCH64) systems. The Raspberry Pi foundation has stated \"[we are not working on this, and are unlikely to do so in the near future](https://github.com/raspberrypi/linux/issues/2315#issuecomment-383132350)\". Using the open source **vc4-kms-v3d** driver listed below instead is recommended

Using the \"VC4\" driver on the raspberry pi to enable hardware acceleration (in X, Wayland, opengl applications) presents many challenges. There\'s plenty of instructions floating around for Raspbian, but for Gentoo, not so much. This page contains a couple of nuggets of wisdom that may help you get there.

## Contents

-   [[1] [Kernel]](#Kernel)
-   [[2] [Mesa and friends]](#Mesa_and_friends)
    -   [[2.1] [Enabling the VC4 kernel module]](#Enabling_the_VC4_kernel_module)
    -   [[2.2] [Is my module loaded?]](#Is_my_module_loaded.3F)
    -   [[2.3] [Is it working?]](#Is_it_working.3F)

## [Kernel]

To have proper GPU acceleration with VideoCore, you need its kernel module loaded. That module has been integrated in v4.5, but it\'s also present in rpi\'s kernel v4.4.

To get VC4 core working you need to use latest firmware from [[[sys-boot/raspberrypi-firmware]](https://packages.gentoo.org/packages/sys-boot/raspberrypi-firmware)[]] 9999 ebuild. To have installed only firmware files and not kernel - follow [this](https://wiki.gentoo.org/wiki/Raspberry_Pi#Boot_partition "Raspberry Pi") guide modifying ebuild file.

## [Mesa and friends]

Before enabling kernel module and switching RPi to GPU you need to rebuild [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]] with support of VideoCore4 plus in case of a Raspberry Pi 4 VideoCore VI. To do so add following to your [/etc/portage/paxkage.use/00video]:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* v3d vc4

And rebuild [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]].

It is also a good idea to add `egl gles1 gles2` as global use flags.

### [Enabling the VC4 kernel module]

Once you have mesa VC4 support you can enable kernel module and try to switch to VC4 GPU.

To enable the kernel module, you have to enable the optional overlay in your [config.txt] with `dtoverlay=vc4-kms-v3d`. It\'s also recommended to bump your `gpu_mem` to `128` (it\'s what [raspi-config] does when you enable the driver through it).

Make sure that you\'ve installed latest version of [[[sys-boot/raspberrypi-firmware]](https://packages.gentoo.org/packages/sys-boot/raspberrypi-firmware)[]] or you\'ll have a blank screen!

Also, you should know that because that driver is a kernel module, you won\'t have any HDMI output until it\'s loaded, which is somewhere in the middle of your init procedure.

### [][Is my module loaded?]

Once you\'re booted up, you can verify that your module is properly loaded with [lsmod]. You\'re supposed to have a `vc4` module in there. Also, it\'s important to verify that [/dev/dri/card0] exists. If you don\'t have that device, nothing\'s going to work.

### [][Is it working?]

To test your setup, you need to install [[[x11-apps/mesa-progs]](https://packages.gentoo.org/packages/x11-apps/mesa-progs)[]]. This provides [glxgears], which you can run with [glxgears -info]. If you have something like `GL_RENDERER = Gallium 0.4 on VC4` in the output, then it\'s a success! If it\'s using `llvmpipe`, you\'re almost there. If it\'s using the software rasterizer, you\'re not there.

If it is using `llvmpipe` and [/usr/share/X11/xorg.conf.d/99-fbturbo.conf] exists, try to remove `Driver "fbturbo"` from that file.