** Note**\
**[ECC](https://wiki.gentoo.org/wiki/ECC "ECC") RAM** should not be confused with *Registered Memory*, commonly called [RDIMM](https://wiki.gentoo.org/index.php?title=RDIMM&action=edit&redlink=1 "RDIMM (page does not exist)"); they are different technologies.

**ECC RAM**, short for [Error Correcting Code](https://wiki.gentoo.org/wiki/ECC "ECC") Random Access Memory, is a kind of RAM can detect most common kinds of memory errors and correct a subset of them. ECC RAM is common in enterprise deployments and most server-class hardware. Above a certain scale and memory density, single-bit errors which were up to this point are sufficiently statistically unlikely begin to occur with enough frequency that they can no longer be ignored. At certain scales and densities of memory arbitrary memory errors that are literally \"one in a million chances\" (or more) may in fact occur several times throughout a system\'s operational life.

Mozilla has [written](https://blog.mozilla.org/data/2022/04/13/this-week-in-glean-what-flips-your-bit/) about some of these issues playing out in the wild.

## Contents

-   [[1] [Kernel]](#Kernel)
-   [[2] [Hardware]](#Hardware)
    -   [[2.1] [AMD]](#AMD)
    -   [[2.2] [Intel]](#Intel)
-   [[3] [Software]](#Software)
    -   [[3.1] [Checking]](#Checking)
    -   [[3.2] [Status reports]](#Status_reports)

## [Kernel]

The following kernel drivers are relevant here:

-   `CONFIG_EDAC` --- EDAC (Error Detection And Correction) reporting hardware driver.
-   `CONFIG_EDAC_AMD64` --- Required if running and AMD based system.
-   `CONFIG_EDAC_DEBUG` --- Only required if you plan on doing driver debugging by simulating various classes of error in RAM.

## [Hardware]

### [AMD]

Most [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") hardware, even for consumers, will support ECC RAM. Sometimes ECC RAM will be listed under \"tested RAM\" in a motherboard\'s Qualified Vendor List (QVL); but if it isn\'t, it may still work if using AMD hardware. In such a case, the ECC RAM will function as expected even if the manufacture does not formally provide support for such a configuration.

### [Intel]

This is in contrast with [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") whose hardware will not support ECC unless buying from their server range, notably Xeon, unless the device happens to support DDR5. Unlike previous generations of DDR RAM, all variants of DDR5 RAM support on-die ECC internally, which reduces error rates but isn\'t a replacement for traditional DIMM-wide or side-band ECC.

## [Software]

### [Checking]

** Note**\
If you see ECC errors occurring in your system log on anything like a regular basis, you have one or more failing DIMM\'s and need to replace the RAM immediately; this is a hardware failure in progress.

To verify that ECC RAM is installed and working correctly, first consult [[[sys-apps/dmidecode]](https://packages.gentoo.org/packages/sys-apps/dmidecode)[]]. Running [dmidecode -t memory] should show a \'Total Width\' greater than \'Data Width\' and say \'Error Correction Type: Multi-bit ECC\'.

Verify also that [dmesg \| grep -i EDAC] returns some results.

### [Status reports]

** Warning**\
The [[[sys-apps/edac-utils]](https://packages.gentoo.org/packages/sys-apps/edac-utils)[]] and [[[app-admin/mcelog]](https://packages.gentoo.org/packages/app-admin/mcelog)[]] packages are functionally obsolete. The former [does not report](https://github.com/mchehab/rasdaemon/blob/master/README#L19) all events on modern kernels and the later only works on supported Intel hardware; it will not work on AMD systems.

Use [[[app-admin/rasdaemon]](https://packages.gentoo.org/packages/app-admin/rasdaemon)[]] to receive reports in [syslog/journal](https://wiki.gentoo.org/wiki/Logging "Logging") when an EDAC event (hardware issue like a memory error being detected or corrected) occurs.

Make sure to start the daemon and enable it to run on boot.

Once running, try [ras-mc-ctl \--layout]:

`root `[`#`]`ras-mc-ctl --layout`

              +-------------------------------------------------+
              |                        mc0                      |
              |   csrow0   |   csrow1   |   csrow2   |   csrow3 |
    ----------+-------------------------------------------------+
    channel1: |     0 MB  |     0 MB  |  16384 MB  |  16384 MB  |
    channel0: |     0 MB  |     0 MB  |  16384 MB  |  16384 MB  |
    ----------+-------------------------------------------------+

`root `[`#`]`ras-mc-ctl --status`

    ras-mc-ctl: drivers are loaded.

`root `[`#`]`ras-mc-ctl --summary`

    No Memory errors.

    No PCIe AER errors.

    No ARM processor errors.

    No Extlog errors.

    No devlink errors.
    No disk errors.
    No MCE errors.