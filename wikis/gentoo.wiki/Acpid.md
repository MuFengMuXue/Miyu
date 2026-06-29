This page contains [[changes](https://wiki.gentoo.org/index.php?title=ACPI&oldid=1240872&diff=1421277)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/ACPI/de "ACPI/de (100% translated)")
-   [English]
-   [français](https://wiki.gentoo.org/wiki/ACPI/fr "ACPI/fr (23% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/ACPI/hu "ACPI/hu (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/ACPI/pl "ACPI/pl (30% translated)")
-   [русский](https://wiki.gentoo.org/wiki/ACPI/ru "ACPI/ru (90% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/ACPI/zh-cn "ACPI/zh-cn (57% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/ACPI/ja "ACPI/ja (100% translated)")

**Resources**

[[]][Home](https://uefi.org/acpi/specs)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface "wikipedia:Advanced Configuration and Power Interface")

**ACPI** (**A**dvanced **C**onfiguration and **P**ower Management **I**nterface) is a [power management](https://wiki.gentoo.org/wiki/Power_management "Power management") system that is part of the [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [USE flags]](#USE_flags)
    -   [[1.4] [SELinux]](#SELinux)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Services]](#Services)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [systemd]](#systemd)
    -   [[2.2] [Advanced examples]](#Advanced_examples)
-   [[3] [Userspace utilities]](#Userspace_utilities)
-   [[4] [See also]](#See_also)

## [[] Installation]

### [[] Kernel]

The following kernel options need to be activated for ACPI:

[KERNEL]

    Power management and ACPI options  --->
        [*] Power Management support
            [*] ACPI (Advanced Configuration and Power Interface) Support  --->

  ---------------------------------------------------------------------------------------------------------------------------------------- ---------------------- ----------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Option                                                                                                                                   Module                 Recommend   Description
  Deprecated [/proc/acpi] files                         \-                     No          Creates deprecated files in the [procfs](https://wiki.gentoo.org/wiki/Procfs "Procfs") filesystem, which are now replaced by files in the [sysfs](https://wiki.gentoo.org/wiki/Sysfs "Sysfs") filesystem.
  Deprecated power [/proc/acpi] directories             \-                     No          Creates deprecated files in the procfs filesystem, which are now replaced by files in the sysfs filesystem.
  EC read/write access through [/sys/kernel/debug/ec]   ec-debugfs             No          Debug interface to the Embedded Controller.
  Deprecated [/proc/acpi/event] support                 \-                     No          Creates deprecated files in the procfs filesystem, which are now replaced by the input layer or netlink events.
  AC Adapter                                                                                                                               ac                     Laptops     Creates files to tell if your system is connected to AC.
  Battery                                                                                                                                  battery                Laptops     Creates files to tell if your system is powered by a battery.
  Button                                                                                                                                   button                 \-          Handles events on the power, sleep, and lid buttons.
  Video                                                                                                                                    video                  \-          Supports basic operations for [Video cards](https://wiki.gentoo.org/wiki/Category:Video_cards "Category:Video cards").
  Fan                                                                                                                                      fan                    \-          Supports ACPI fan devices, allowing user-mode applications to perform basic fan control (on, off, status).
  Dock                                                                                                                                     dock                   \-          Supports ACPI-controlled docking stations and removable drive bays, see the [acpi dock](https://wiki.gentoo.org/wiki/Acpi_dock "Acpi dock") article.
  Processor                                                                                                                                processor              \-          Installs ACPI as the idle handler for Linux and uses ACPI C2 and C3 processor states to save power.
  Processor Aggregator                                                                                                                     processor-aggregator   \-          ACPI 4.0 function to perform specific processor configuration and control.
  Thermal Zone                                                                                                                             thermal                Yes         Supports ACPI thermal zones to protect your processor against overheating.
  NUMA support                                                                                                                             \-                     \-
  Debug Statements                                                                                                                         \-                     No
  PCI slot detection driver                                                                                                                pci-slot               No          Helps to correlate PCI bus addresses with physical slots
  Container and Module Devices                                                                                                             container              \-          Supports ACPI Container and Module devices to hotplug nodes, CPUs, and memory.
  Smart Battery System                                                                                                                     sbs, sbshc             \-          Supports another type of access to battery information, found on some laptops.
  Hardware Error Device                                                                                                                    hed                    \-          Supports the Hardware Error Device, which is used to report some hardware errors.
  Allow ACPI methods to be inserted/replaced at run time                                                                                   custom-method          No
  ACPI Platform Error Interface (APEI)                                                                                                     \-                     \-          APEI allows to report errors (for example from the chipset) to the operating system.
  ---------------------------------------------------------------------------------------------------------------------------------------- ---------------------- ----------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : **Optional drivers**

### [[] Emerge]

[Desktop environments](https://wiki.gentoo.org/wiki/Category:Desktop_environment "Category:Desktop environment") react on the common events generated by ACPI. If a desktop environment is not installed or to have the system react on special events the ACPI package can be installed. Install the [[[sys-power/acpid]](https://packages.gentoo.org/packages/sys-power/acpid)[]] package:

`root `[`#`]`emerge --ask sys-power/acpid`

### [[] USE flags]

Several packages know about the global [`acpi`](https://packages.gentoo.org/useflags/acpi) USE flag. There are no use flags available for [[[sys-power/acpid]](https://packages.gentoo.org/packages/sys-power/acpid)[]] at this time.

### [[] SELinux]

For acpid to be able to shutdown a SELinux system, make sure the [[[sec-policy/selinux-shutdown]](https://packages.gentoo.org/packages/sec-policy/selinux-shutdown)[]] package is installed and the [/sbin/shutdown] executable is re-labelled:

`root `[`#`]`emerge --ask sec-policy/selinux-shutdown`

## [[] Configuration]

The scripts found in [/etc/acpi] define how the system reacts on ACPI events. They can be edited as necessary to meet the user\'s needs.

### [[] Services]

#### [[] OpenRC]

The acpid service can now be started. While using OpenRC run:

`root `[`#`]`/etc/init.d/acpid start`

To have the acpid service start at boot time add it to the default runlevel:

`root `[`#`]`rc-update add acpid default`

#### [[] systemd]

If systemd is being used as the [init system](https://wiki.gentoo.org/wiki/Init_system "Init system"), enable the acpid service on system boot by issuing:

`root `[`#`]`systemctl enable acpid.service`

To start the service now:

`root `[`#`]`systemctl start acpid.service`

### [[] Advanced examples]

The default ACPI setup may be satisfactory for some users, however a little extra configuration may be required to get the acpid daemon to treat some basic ACPI events properly (AC power plug in/out, multimedia keys, etc.).

Modifications can be made to [/etc/acpi/default.sh] along with [/etc/acpi/events/default] if necessary. Why not create a complicated setup that makes use of the [/etc/acpi/actions] and [/etc/acpi/events] capabilities? Simply put scripts and event files in those locations for advanced usage.

A basic [default.sh] file will probably be enough for most users, however the following is an example of what *could* be done using [default.sh]:

[FILE] **`/etc/acpi/default.sh`**

    #!/bin/sh
    #
    # $Header: /etc/acpi/default.sh                          Exp $
    # $Author: (c) 2012-2014 -tclover <tokiclover@dotfiles.> Exp $
    # $License: MIT (or 2-clause/new/simplified BSD)         Exp $
    # $Version: 2014/12/24 21:09:26                          Exp $
    #

    log()
    uhd()

    set $*
    group=$
    action=$
    device=$2
    id=$3
    value=$4

    [ -d /dev/snd ] && alsa=true || alsa=false
    [ -d /dev/oss ] && oss=true || oss=false
    amixer="amixer -q set Master"
    ossmix="ossmix -- vmix0-outvol"

    case $group in
        ac_adapter)
            case $value in
                *0) log "switching to power.bat power profile"
                    hprofile power.bat;;
                *1) log "switching to power.adp power profile"
                    hprofile power.adp;;
                *) uhd $*;;
            esac
            ;;
        battery)
            case $value in
                *0) log "switching to power.adp power profile"
                    hprofile power.adp;;
                *1) log "switching to power.adp power profile"
                    hprofile power.adp;;
                *) uhd $*;;
            esac
            ;;
        button)
            case $action in
                lid)
                    case "$id" in
                        close) hibernate-ram;;
                        open) :;;
                        *) uhd $*;;
                    esac
                    ;;
                power) shutdown -H now;;
                sleep) hibernate-ram;;
                mute)
                    $alsa && $amixer toggle;;
                volumeup)
                    $alsa && $amixer 3dB+
                    $oss && $ossmix +3;;
                volumedown)
                    $alsa && $amixer 3dB-
                    $oss && $ossmix -3;;
                *) uhd $*;;
            esac
            ;;
        cd)
            case $action in
                play) :;;
                stop) :;;
                prev) :;;
                next) :;;
                *) uhd $*;;
            esac
            ;;
        jack)
            case $id in
                *plug) :;;
                *) uhd $*;;
            esac
            ;;
        video)
            case $action in
                displayoff) :;;
                *) uhd $*;;
            esac
            ;;
        *) uhd $*;;
    esac

    unset alsa oss amixer ossmix group action device id

    # vim:fenc=utf-8:ft=sh:ci:pi:sts=4:sw=4:ts=4:

** Note**\
Notice that the above script is compatible with [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") and [OSS](https://wiki.gentoo.org/wiki/OSS "OSS"), so no extra actions are needed when switching OSS from ALSA or the opposite. Do not hesitate to edit the script!

** Note**\
The above script also makes use of a power management profile using [hprofile](https://wiki.gentoo.org/wiki/Hprofile "Hprofile"). Refer to the [hprofile](https://wiki.gentoo.org/wiki/Hprofile "Hprofile") article for more information.

## [[] Userspace utilities]

Many packages use ACPI functions. A few are listed here:

-   [[[sys-power/acpi]](https://packages.gentoo.org/packages/sys-power/acpi)[]]: to show information from the /proc filesystem, such as battery status or thermal information
-   [[[sys-power/acpitool]](https://packages.gentoo.org/packages/sys-power/acpitool)[]]: a small command line application, intended to be a replacement for the apm tool
-   [[[sys-power/acpilight]](https://packages.gentoo.org/packages/sys-power/acpilight)[]]: replacement for xbacklight that uses the ACPI interface to set brightness
-   [[[app-laptop/laptop-mode-tools]](https://packages.gentoo.org/packages/app-laptop/laptop-mode-tools)[]]: linux kernel [laptop_mode](https://wiki.gentoo.org/wiki/Power_management/Guide#Using_Laptop_Mode_Tools "Power management/Guide") user-space utilities
-   [[[x11-misc/cbatticon]](https://packages.gentoo.org/packages/x11-misc/cbatticon)[]]: a lightweight and fast battery icon that sits in your system tray
-   [[[app-admin/conky]](https://packages.gentoo.org/packages/app-admin/conky)[]]: an advanced, highly configurable system monitor for X

\

## [[] See also]

-   [ACPI/ThinkPad-special-buttons](https://wiki.gentoo.org/wiki/ACPI/ThinkPad-special-buttons "ACPI/ThinkPad-special-buttons") --- describes how to configure ACPI events and actions for the Lenovo ThinkPad T410 laptop.
-   [Suspend and hibernate](https://wiki.gentoo.org/wiki/Suspend_and_hibernate "Suspend and hibernate") --- describes how to suspend or hibernate a Gentoo system.
-   [Knowledge Base:Disabling ACPI support at boot time](https://wiki.gentoo.org/wiki/Knowledge_Base:Disabling_ACPI_support_at_boot_time "Knowledge Base:Disabling ACPI support at boot time")