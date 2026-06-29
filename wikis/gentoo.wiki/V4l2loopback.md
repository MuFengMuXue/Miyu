This page contains [[changes](https://wiki.gentoo.org/index.php?title=V4l2loopback&diff=1290302)] which are not marked for translation.

**Resources**

[[]][GitHub](https://github.com/umlaeute/v4l2loopback)

**v4l2loopback** provides a way for applications to act as a capture card would, looping back video output as input for use in other applications.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Removal]](#Removal)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Module Not Found]](#Module_Not_Found)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Kernel]

[KERNEL] **Enable support for V4L**

    Device Drivers  --->
       Multimedia support --->
          Media drivers --->
             <*> V4L test drivers

### [USE flags]

### [USE flags for] [media-video/v4l2loopback](https://packages.gentoo.org/packages/media-video/v4l2loopback) [[]] [v4l2 loopback device whose output is its own input]

  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------
  [`+strip`](https://packages.gentoo.org/useflags/+strip)                       Allow symbol stripping to be performed by the ebuild for special files
  [`dist-kernel`](https://packages.gentoo.org/useflags/dist-kernel)             Enable subslot rebuilds on Distribution Kernel upgrades
  [`examples`](https://packages.gentoo.org/useflags/examples)                   Install examples, usually source code
  [`modules-compress`](https://packages.gentoo.org/useflags/modules-compress)   Install compressed kernel modules (if kernel config enables module compression)
  [`modules-sign`](https://packages.gentoo.org/useflags/modules-sign)           Cryptographically sign installed kernel modules (requires CONFIG_MODULE_SIG=y in the kernel)
  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-18 07:12] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-video/v4l2loopback`

## [Usage]

### [Invocation]

`user `[`$`]`v4l2loopback-ctl -h`

    usage: v4l2loopback-ctl [general commands]

     general commands
     ================
        -v/--version : print version and exit
        -h/-?/--help : print this help and exit
         add  [<outputdevice> [<capturedevice>]]

         delete <device>

         list

         query  <device>

         set-fps <device> <fps>

         get-fps <device>

         set-caps <device> <caps>

         get-caps <device>

         set-timeout-image  <device> <image>

     adding devices ('add')
     ======================
        v4l2loopback-ctl add  [<outputdevice> [<capturedevice>]]

       <flags>    any of the following flags may be present
         -n/--name <name>        : pretty name for the device
         --min-width <w>         : minimum allowed frame width
         -w/--max-width <w>      : maximum allowed frame width
         --min-height <w>        : minimum allowed frame height
         -h/--max-height <h>     : maximum allowed frame height
         -x/--exclusive-caps <x> : whether to announce OUTPUT/CAPTURE capabilities exclusively
         -b/--buffers <num>      : buffers to queue
         -o/--max-openers <num>  : maximum allowed concurrent openers
         -v/--verbose            : verbose mode (print properties of device after successfully creating it)
         -?/--help               : print this help and exit

      <outputdevice>  if given, create a specific device (otherwise just create a free one).
                either specify a device name (e.g. '/dev/video1') or a device number ('1').
      <capturedevice> if given, use separate output & capture devices (otherwise they are the same).

     deleting devices ('delete')
     ===========================
        v4l2loopback-ctl delete <device>

      <device>    can be given one more more times (to delete multiple devices at once).
                either specify a device name (e.g. '/dev/video1') or a device number ('1').

     listing devices ('list')
     ========================
        v4l2loopback-ctl list

       <flags>    any of the following flags may be present
         -e/--escape             : escape control-characters in (device) names
         -h/--help               : print this help and exit

                list all available loopback-devices

     querying devices ('query')
     ==========================
        v4l2loopback-ctl query  <device>

       <flags>    any of the following flags may be present
         -e/--escape             : escape control-characters in (device) names
         -h/--help               : print this help and exit

      <device>    can be given one more more times (to query multiple devices at once).
                either specify a device name (e.g. '/dev/video1') or a device number ('1').

     setting framerate ('set-fps')
     =============================
        v4l2loopback-ctl set-fps <device> <fps>

      <device>    either specify a device name (e.g. '/dev/video1') or a device number ('1').
         <fps>    frames per second, either as integer ('30') or fraction ('50/2').

     getting framerate ('get-fps')
     =============================
        v4l2loopback-ctl get-fps <device>

     setting capabilities ('set-caps')
     =================================
        v4l2loopback-ctl set-caps <device> <caps>

      <device>    either specify a device name (e.g. '/dev/video1') or a device number ('1').
        <caps>    format specification as '<fourcc>:<width>x<height>@<fps>' (e.g. 'UYVY:1024x768@60/1')

     getting capabilities ('get-caps')
     =================================
        v4l2loopback-ctl get-caps <device>

     setting timeout image ('set-timeout-image')
     ===========================================
        v4l2loopback-ctl set-timeout-image  <device> <image>

       <flags>    any of the following flags may be present
         -t/--timeout <timeout>  : timeout (in ms)
         -v/--verbose            : raise verbosity (print what is being done)
         -h/--help               : print this help and exit

      <device>    either specify a device name (e.g. '/dev/video1') or a device number ('1').
       <image>    image file

## [Removal]

`root `[`#`]`emerge --ask --depclean --verbose media-video/v4l2loopback`

## [Troubleshooting]

### [Module Not Found]

You may see an error message like the one below when loading the module.

`root `[`#`]`modprobe v4l2loopback`

    modprobe: FATAL: Module v4l2loopback not found in directory /lib/modules/6.6.21-gentoo

First, ensure you are booted into the correct kernel.

`user `[`$`]`uname -a`

`user `[`$`]` eselect kernel list`

If these do not match up, you may need to update your bootloader config. For GRUB:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

You may also need to rebuild your kernel modules.

`root `[`#`]`emerge --ask @module-rebuild`

## [External resources]

-   [v4l2loopback](https://wiki.archlinux.org/title/V4l2loopback) (Arch Linux Wiki)