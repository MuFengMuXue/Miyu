**Resources**

[[]][Home](https://zoom.us/)

[[]][Package information](https://packages.gentoo.org/packages/net-im/zoom)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Zoom_(software) "wikipedia:Zoom (software)")

**Zoom Meetings** also known as **Zoom** is a proprietary videotelephony software program developed by Zoom Video Communications.

**Zoom** is commonly used in remote work and educational environments.

## [Installation]

Installation is pretty fairly straightforward; just set `USE` flags as appropriate and then emerge the package. See the sections below about `USE` flag requirements for specific features (video and audio).

### [USE flags for] [net-im/zoom](https://packages.gentoo.org/packages/net-im/zoom) [[]] [Video conferencing and web conferencing service]

  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------
  [`+zoom-symlink`](https://packages.gentoo.org/useflags/+zoom-symlink)   Install a zoom symlink in /usr/bin
  [`opencl`](https://packages.gentoo.org/useflags/opencl)                 Use OpenCL for virtual background support (virtual/opencl)
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)         Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)               Enable dev-libs/wayland backend
  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-30 05:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

First, accept the all-rights-reserved license (you can read it at \'/var/db/repos/gentoo/licenses/all-rights-reserved\')

`root `[`#`]`echo "net-im/zoom all-rights-reserved" >> /etc/portage/package.license`

then

`root `[`#`]`emerge --ask net-im/zoom`

### [Enabling audio]

If the system uses Pulseaudio, enable the `pulseaudio` `USE` flag. This should rectify issues of not being able to speak to people.

### [Enabling video]

Normally, if the system has a webcam available, it should just work. If the webcam video feed is not displayed in Zoom, here are some things to try:

1.  Use a different program to make sure that the webcam itself is working (see [Webcam](https://wiki.gentoo.org/wiki/Webcam "Webcam"))
2.  Ensure that Zoom is upgraded to `5.14.10.3738-r1` or later, *or* that the `opencl` `USE` flag is enabled. (see [[[bug #833951]](https://bugs.gentoo.org/show_bug.cgi?id=833951)[]] for the context)
3.  Ensure that the `bundled-libjpeg-turbo` `USE` flag is enabled.