[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Gqrx&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://gqrx.dk/)

[[]][Official documentation](https://www.gqrx.dk/category/doc)

[[]][Package information](https://packages.gentoo.org/packages/net-wireless/gqrx)

[[]][GitHub](https://github.com/gqrx-sdr/gqrx)

**gqrx** is an open source software defined radio (SDR) receiver powered by GNU Radio and the Qt graphical toolkit. It supports multiple SDR hardware devices, including (but not limited to) the RTL-SDR, HackRF, and Airspy. A complete list of supported hardware can be found at [https://gqrx.dk/supported-hardware](https://gqrx.dk/supported-hardware).

Notable features include AM, SSB, CW, and (wide) FM demodulation, spectrum plots and waterfalls, and the ability to record and stream audio output. A more complete list of features can be found on the gqrx website: [https://gqrx.dk/](https://gqrx.dk/)

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Scanning]](#Scanning)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Kernel]

If using an RTL-SDR, the kernel must be configured to blacklist the **rtl2832** module, as the normal DVB-T driver is not compatible for its use as an SDR. More information regarding this can be found on the [RTL-SDR](https://wiki.gentoo.org/wiki/Rtl-sdr "Rtl-sdr") wiki page.

### [USE flags]

USE flags for gqrx itself are as follows:

### [USE flags for] [net-wireless/gqrx](https://packages.gentoo.org/packages/net-wireless/gqrx) [[]] [Software defined radio receiver powered by GNU Radio and Qt]

  ----------------------------------------------------------------- ----------------------------------------------------------------------------------
  [`portaudio`](https://packages.gentoo.org/useflags/portaudio)     Add support for the crossplatform portaudio audio API
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)   Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  ----------------------------------------------------------------- ----------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-07-01 15:06] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

It is important to specify the correct USE flags for the net-wireless/gr-osmosdr dependency, or else gqrx will not find your SDR device:

### [USE flags for] [net-wireless/gr-osmosdr](https://packages.gentoo.org/packages/net-wireless/gr-osmosdr) [[]] [GNU Radio source block for OsmoSDR and rtlsdr and hackrf]

  --------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`airspy`](https://packages.gentoo.org/useflags/airspy)         Build with Airspy support through net-wireless/airspy
  [`bladerf`](https://packages.gentoo.org/useflags/bladerf)       Build with Nuand BladeRF support through net-wireless/bladerf
  [`doc`](https://packages.gentoo.org/useflags/doc)               Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`hackrf`](https://packages.gentoo.org/useflags/hackrf)         Build with Great Scott Gadgets HackRF support through net-libs/libhackrf
  [`iqbalance`](https://packages.gentoo.org/useflags/iqbalance)   Enable support for I/Q balancing using gr-iqbal through net-wireless/gr-iqbal
  [`rtlsdr`](https://packages.gentoo.org/useflags/rtlsdr)         Build with Realtek RTL2832U support through net-wireless/rtl-sdr
  [`sdrplay`](https://packages.gentoo.org/useflags/sdrplay)       Enable support for SDRplay devices through net-wireless/sdrplay
  [`soapy`](https://packages.gentoo.org/useflags/soapy)           Build with SoapySDR support through net-wireless/soapysdr
  [`uhd`](https://packages.gentoo.org/useflags/uhd)               Build with Ettus Research USRP Hardware Driver support through net-wireless/uhd
  [`xtrx`](https://packages.gentoo.org/useflags/xtrx)             Build with xtrx Hardware Driver support through net-wireless/libxtrx
  --------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-19 17:40] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

For example, if one has an RTL-SDR, the following can be used:

[FILE] **`/etc/portage/package.use`Setting USE variable for the RTL-SDR**

    net-wireless/gr-osmosdr rtlsdr

### [Emerge]

`root `[`#`]`emerge --ask net-wireless/gqrx`

## [Configuration]

### [Files]

-   [\~/.config/gqrx/default.conf] - User configuration file for the configured SDR device.

The above file will be created on first launch when selecting the SDR device and associated options. If the supplied config results in an error, gqrx will detect this and let the user re-specify their config on the next launch.

## [Usage]

### [Invocation]

To start gqrx:

`user `[`$`]`gqrx`

Additional options can be seen with -h/\--help:

`user `[`$`]`gqrx --help`

    Controlport disabled
    Gqrx software defined radio receiver 2.12
    Command line options:
      -h [ --help ]         This help message
      -s [ --style ] arg    Use the give style (fusion, windows)
      -l [ --list ]         List existing configurations
      -c [ --conf ] arg     Start with this config file
      -e [ --edit ]         Edit the config file before using it
      -r [ --reset ]        Reset configuration file

### [Scanning]

The [[[net-wireless/gqrx-scanner]](https://packages.gentoo.org/packages/net-wireless/gqrx-scanner)[]] package can be used while gqrx is running to scan a range of frequencies. Refer to [the project page](https://github.com/neural75/gqrx-scanner) for further information.

## [Troubleshooting]

**SDR device not listed**

If the SDR device necessary is not listed, then it is possible that [[[net-wireless/gr-osmosdr]](https://packages.gentoo.org/packages/net-wireless/gr-osmosdr)[]] was not compiled with the correct USE flag(s). Launch gqrx from the command line and look for the following line:

`user `[`$`]`gqrx`

    ...
    built-in source types: ...
    ...

For reference, a build of gr-osmosdr with support for most SDR devices will look like this:

`user `[`$`]`gqrx`

    ...
    built-in source types: file osmosdr fcd rtl rtl_tcp plutosdr miri hackrf bladerf rfspace airspy airspyhf soapy redpitaya
    ...

Check the USE flags that are set for the net-wireless/gr-osmosdr package to ensure the correct one(s) are set for the needed devices.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-wireless/gqrx`

## [External resources]

-   [The gqrx homepage](https://gqrx.dk/)