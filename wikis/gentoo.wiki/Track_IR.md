[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Track_IR&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Track_IR&action=edit).

TrackIR is head tracking hardware and software for tracking slight head movements to extend display within 3D environments. This solution is most often utilized within flight simulation to increase the experience of the simulation.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Using ltr_pipe]](#Using_ltr_pipe)
-   [[4] [Known issues]](#Known_issues)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

If you do not have a TrackIR device, the most current one sold is the \"TrackIR 5\". All that is needed is a ballcap for the reflective clip device that accompanies the TrackIR device. If you fly simulators quite often, it\'s a really nifty device even if you are pretty good at using a joystick hat for moving your view around.

TrackIR for Linux can be downloaded from [http://linuxtrack.eu/repositories/universal/](http://linuxtrack.eu/repositories/universal/) or SVN at [http://code.google.com/p/linux-track/source/checkout](https://code.google.com/p/linux-track/source/checkout) or github at [https://github.com/uglyDwarf/linuxtrack/wiki/Downloads](https://github.com/uglyDwarf/linuxtrack/wiki/Downloads). Compile and install locally, else wait for an Ebuild to be imported into Portage, and shortly I hope!

Basic compile time dependencies, of which [[[dev-libs/mini-xml]](https://packages.gentoo.org/packages/dev-libs/mini-xml)[]] is missing for the Qt GUI interface. So make sure you have mini-xml installed before compiling the linuxtrack sources. (Bug reported upstream and likely on the TODO list.)

First, unpack the tarball and throw the output folder into /opt. cd into /opt and run

`user `[`$`]`./configure`

If all goes swimmingly run

`user `[`$`]`make`

then

`user `[`$`]`make install`

Note: I will be adding more over the next week.

`user `[`$`]`ltr_pipe`

## [Configuration]

The TrackIR hardware first needs to have it\'s device firmware extracted from the Windows binaries and a configure file needs to be written before simply utilizing the ltr_pipe command line tool.

There is also a run-time dependency of using Wine to extract the firmware. So make sure you have Wine pre-installed prior to running ltr_gui. Once you have compiled & installed linuxtrack, start the ltr_gui and install your device firmware accordingly using the GUI front end. Once completed, initialize the device (start), save and exit. Make sure all your settings are set to your liking, however default seems desirable for most applications.

## [Using ltr_pipe]

The following is all that is really needed to see output once you have performed the previous instructions.

`user `[`$`]`ltr_pipe`

From here, read the [linuxtrack/doc/README.ltr_pipe] on how to further setup with FlightGear.

** Note**\
The developer has just informed that he has linuxtrack working without even using Nasal. An easier method?

## [Known issues]

** Note**\
I\'m within the process of creating a linuxtrack Ebuild file for Gentoo. If for some reason the process stalls, users shall have the information they need to continue or pursue on their own.

See [[[bug #489324]](https://bugs.gentoo.org/show_bug.cgi?id=489324)[]]. Happy Head Tracking!

## [See also]

-   [FlightGear](https://wiki.gentoo.org/wiki/FlightGear "FlightGear") --- an open-source, multi-platform, cooperative flight simulator development project.

## [External resources]