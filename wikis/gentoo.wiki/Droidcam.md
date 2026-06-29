**Resources**

[[]][Home](https://www.dev47apps.com/)

[[]][Package information](https://packages.gentoo.org/packages/media-video/droidcam)

[[]][GitHub](https://github.com/dev47apps/droidcam)

[[]][Official documentation](https://github.com/dev47apps/droidcam/wiki)

\
Droidcam is a tool to use a smartphone\'s cameras as webcam on a computer.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Connect via Wi-Fi/LAN]](#Connect_via_Wi-Fi.2FLAN)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Droidcam/v4l2loopback device not found]](#Droidcam.2Fv4l2loopback_device_not_found)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
    -   [[4.2] [Remove user configuration]](#Remove_user_configuration)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Kernel]

Droidcam brings its own Kernel module. For it to work, the Kernel must be configured appropriately.

[KERNEL] **Enable support for \<Software_title\>**

    Device Drivers --->
      <M> Multimedia support --->
        [*] Cameras/video grabbers support
        [*] Media Controller API

The module is available as `v4l2loopback-dc` and must be loaded before starting Droidcam, for example using `modprobe v4l2loopback-dc`

### [USE flags]

### [USE flags for] [media-video/droidcam](https://packages.gentoo.org/packages/media-video/droidcam) [[]] [Use your phone or tablet as webcam with a v4l device driver and app]

  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------
  [`+strip`](https://packages.gentoo.org/useflags/+strip)                       Allow symbol stripping to be performed by the ebuild for special files
  [`dist-kernel`](https://packages.gentoo.org/useflags/dist-kernel)             Enable subslot rebuilds on Distribution Kernel upgrades
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                             Build the dev-cpp/gtkmm:3.0 client.
  [`modules-compress`](https://packages.gentoo.org/useflags/modules-compress)   Install compressed kernel modules (if kernel config enables module compression)
  [`modules-sign`](https://packages.gentoo.org/useflags/modules-sign)           Cryptographically sign installed kernel modules (requires CONFIG_MODULE_SIG=y in the kernel)
  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-19 17:10] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Usage]

To use Droidcam, a smartphone with the Droidcam app installed is needed. The smartphone and the computer need to be able to reach each other over the network. Alternatively, a USB connection can be used. Depending on the operating system, this might require setting further options on the smartphone (e.g. enabling USB debugging).

### [][Connect via Wi-Fi/LAN]

After starting Droidcam on the smartphone, the smartphone app shows the IP address and port for the computer to connect to. After starting the app on the computer, `WiFi / LAN` needs to be selected and the WiFi IP and port, which are shown on the smartphone, need to be entered in the appropriate field on the computer. After that, the two apps should be able to establish a connection. The phone\'s camera is then available like any other webcam connected to the computer.

## [Troubleshooting]

### [][Droidcam/v4l2loopback device not found]

If droidcam shows a message like this on startup, it is very likely that the kernel hasn\'t been configured properly or that the required modules haven\'t been loaded. Please make sure the kernel is configured properly and `v4l2loopback-dc` been loaded. Note that this module is not the same as `v4l2loopback`.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose media-video/droidcam`

### [Remove user configuration]

User configuration is stored as a simple text file in the user\'s config directory. To remove the configuration:

`user `[`$`]`rm ~/.config/droidcam`

## [External resources]

-   [Droidcam Help & FAQ](https://www.dev47apps.com/droidcam/help/)