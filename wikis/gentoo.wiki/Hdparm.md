**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Hdparm "wikipedia:Hdparm")

[[]][Home](https://sourceforge.net/projects/hdparm/)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/hdparm)

[hdparm] is a command-line utility to set and view ATA and SATA [hard disk drive](https://wiki.gentoo.org/wiki/HDD "HDD") hardware parameters.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [OpenRC]](#OpenRC)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [General]](#General)
    -   [[3.2] [Benchmarking drives]](#Benchmarking_drives)
    -   [[3.3] [Get current settings]](#Get_current_settings)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags for] [sys-apps/hdparm](https://packages.gentoo.org/packages/sys-apps/hdparm) [[]] [Utility to change hard drive performance parameters]

  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`static`](https://packages.gentoo.org/useflags/static)   !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[sys-apps/hdparm]](https://packages.gentoo.org/packages/sys-apps/hdparm)[]]:

`root `[`#`]`emerge --ask sys-apps/hdparm`

## [Configuration]

### [Service]

#### [OpenRC]

To set parameters on boot, edit the [/etc/conf.d/hdparm] configuration file:

-   `sdX_args`: Set parameters for the given drive (replace *sdX* with the right device file name).
-   `discX_args`: Set parameters for the given disc drive.
-   `cdromX_args`: Set parameters for the given optical drive.
-   `all_args`: Set parameters for all drives.

For example, to disable power management for all drivers and enable the DMA feature for [/dev/sda]:

[FILE] **`/etc/conf.d/hdparm`**

    all_args="-B 255"
    sda_args="-d1"

When finished modifying the configuration file be sure to add the [hdparm] service to the default runlevel so that it can start at system boot:

`root `[`#`]`rc-update add hdparm default`

## [Usage]

### [General]

Show identification and feature info:

`root `[`#`]`hdparm -I /dev/sdX`

### [Benchmarking drives]

Be sure that no other programs are stressing the drive at the time of testing:

`root `[`#`]`hdparm -tT /dev/sdX`

### [Get current settings]

This is not consistent: for some features the current values can be found in the common info, for other features [hdparm] must be called with the right parameters, but without any value, like `-d`:

`root `[`#`]`hdparm -d /dev/sdX`

Set features by put the value directly behind the parameter (without space), e.g. to enable the DMA mode:

`root `[`#`]`hdparm -d1 /dev/sdX`

** Warning**\
Changing the default values can harm the drive or freeze the system.

The following tables introduces the most common parameters. For a complete list see the *hdparm* [man page](https://wiki.gentoo.org/wiki/Man_page "Man page").

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter                         | Description                                                                                                                                                                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-B`                              | Set the Advanced Power Management feature. The value *1* saves the most energy, the value *255* disables the feature. The values in-between are corresponding steps. Values of *127* and below allow the spin-down of the drive. |
|                                   |                                                                                                                                                                                                                                  |
|                                   | :::                                                                                                                                                 |
|                                   | ** Warning**\                                                                                                                                                                                                                    |
|                                   | Aggressive power management can wear the drive because of often spin-downs.                                                                                                                                                      |
|                                   | :::                                                                                                                                                                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-d`                              | Set the DMA feature for IDE and PATA drives. The value *1* enables the feature, *0* disables the feature.                                                                                                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-E`                              | Set CD / DVD drive speed. Lower speeds can reduces the running noise.                                                                                                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-M`                              | Set the Automatic Acoustic Management feature. The values *0* disables the feature, *128* sets the most quiet mode, *254* is the fastest mode.                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `-S`                              | Set the standby (spin-down after idling) timeout. The value *0* disables the feature, the values from *1* to *240* specifies time steps of 5 seconds, *241* to *251* time steps of 30 minutes.                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## [See also]

-   [HDD](https://wiki.gentoo.org/wiki/HDD "HDD") --- describes the setup of an internal SATA or PATA (IDE) rotational **hard disk drive**.

## [External resources]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=hdparm&order=bug_id%20DESC)[]]