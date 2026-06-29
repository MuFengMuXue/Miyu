This page contains [[changes](https://wiki.gentoo.org/index.php?title=Troubleshooting&oldid=1281298&diff=1404767)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Troubleshooting/es "Resolución de problemas (39% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Troubleshooting/it "Risoluzione di problemi (4% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Troubleshooting/hu "Hibaelhárítás (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Troubleshooting/pl "Troubleshooting/pl (1% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Troubleshooting/ru "Устранение неполадок (67% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Troubleshooting/zh-cn "故障排除 (4% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Troubleshooting/ja "トラブルシューティング (87% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Troubleshooting/ko "Troubleshooting/ko (27% translated)")

The purpose of this page is to provide users with a set of techniques and tools to troubleshoot and fix problems with their Gentoo setups.

This article assumes that the [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") has been read and that there is a basic understanding of using Gentoo.

** Tip**\
If a solution cannot be found after troubleshooting, see the [support](https://wiki.gentoo.org/wiki/Support "Support") article about asking for help.

## Contents

-   [[1] [Packages that can help with troubleshooting]](#Packages_that_can_help_with_troubleshooting)
    -   [[1.1] [Package management]](#Package_management)
    -   [[1.2] [Hardware]](#Hardware)
    -   [[1.3] [Monitoring]](#Monitoring)
-   [[2] [Identifying a problem]](#Identifying_a_problem)
-   [[3] [Hardware issues]](#Hardware_issues)
    -   [[3.1] [Drivers]](#Drivers)
        -   [[3.1.1] [Determining the proper driver]](#Determining_the_proper_driver)
        -   [[3.1.2] [Verifying the driver is loaded]](#Verifying_the_driver_is_loaded)
        -   [[3.1.3] [Troubleshooting a driver]](#Troubleshooting_a_driver)
-   [[4] [Software issues]](#Software_issues)
    -   [[4.1] [Portage issues]](#Portage_issues)
        -   [[4.1.1] [Dependency graph slot conflicts]](#Dependency_graph_slot_conflicts)
-   [[5] [System limitations prevent a proper build]](#System_limitations_prevent_a_proper_build)
-   [[6] [Debug a binary]](#Debug_a_binary)
-   [[7] [Collecting additional information]](#Collecting_additional_information)
    -   [[7.1] [Wrapping things together]](#Wrapping_things_together)
    -   [[7.2] [Please do not use pastebin services on the gentoo-user mailing list]](#Please_do_not_use_pastebin_services_on_the_gentoo-user_mailing_list)
-   [[8] [Forming a solution]](#Forming_a_solution)
-   [[9] [See also]](#See_also)

## [Packages that can help with troubleshooting]

This is a collection of tools that can help with troubleshooting, and are *highly* recommended.

** Tip**\
[wgetpaste](https://wiki.gentoo.org/wiki/Wgetpaste "Wgetpaste") is a handy tool to share snippets, files, command output etc. when discussing troubleshooting issues online.

### [Package management]

  -------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                              Description
  [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit")   A collection of tools for interacting with Gentoo, includes the valuable [equery](https://wiki.gentoo.org/wiki/Equery "Equery"), [eclean](https://wiki.gentoo.org/wiki/Eclean "Eclean"), [euse](https://wiki.gentoo.org/wiki/Euse "Euse"), etc.
  [eix](https://wiki.gentoo.org/wiki/Eix "Eix")                        A tool for querying portage for packages.
  [Portage File List](https://wiki.gentoo.org/wiki/Pfl "Pfl")          Provides [e-file], a tool for querying what package contains a given file, it also works for packages that aren\'t installed since it uses an online lookup.
  [genlop](https://wiki.gentoo.org/wiki/Genlop "Genlop")               A tool for parsing emerge logs, handy to figure out when certain packages were installed, updated and to see how long they took to compile.
  [elogv](https://wiki.gentoo.org/wiki/Elogv "Elogv")                  An ncurses based interface for browsing emerge logs.
  -------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Hardware]

  -------------------------------------------------------------- -----------------------------------------------------
  Package                                                        Description
  [pciutils](https://wiki.gentoo.org/wiki/Pciutils "Pciutils")   A tool for gathering information about PCI devices.
  [usbutils](https://wiki.gentoo.org/wiki/Usbutils "Usbutils")   A tool for gathering information about USB devices.
  -------------------------------------------------------------- -----------------------------------------------------

### [Monitoring]

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                           Description
  [btop](https://wiki.gentoo.org/wiki/Btop "Btop")                                                                                                                                                                                                                                                                                                                                  A resource monitor that shows usage and stats for processor, memory, disks, network and processes.
  [htop](https://wiki.gentoo.org/wiki/Htop "Htop")                                                                                                                                                                                                                                                                                                                                  A tool for monitoring processes, like [top], but more advanced.
  [iotop](https://wiki.gentoo.org/wiki/Iotop "Iotop")                                                                                                                                                                                                                                                                                                                               A [top]-like tool for monitoring IO activity by process.
  [[[net-analyzer/nettop]](https://packages.gentoo.org/packages/net-analyzer/nettop)[]]   A [top]-like tool for examining network traffic by protocol, port, and process.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Identifying a problem]

In order to shape a problem into a solution, the problem should first be properly identified. An accurate understanding of the problem is more likely to yield a good solution. This may seem like a no-brainer, but without it, troubleshooting will be difficult.

Take note of a few things:

1.  Is this problem related to hardware or software?
2.  What was done or has been changed recently that may have been the cause of this issue?
3.  Can additional information about the problem be collected?

Gathering any information, logs, reports of other people experiencing similar issues, etc., can be valuable to get a good overview.

## [Hardware issues]

### [Drivers]

Driver issues for hardware is one of the more common issues that are reported on IRC.

First and foremost, identify what the hardware is that is causing problems. [lspci] and [lsusb] are great tools for this purpose. Here is the example of an Ethernet card as the troublesome device:

#### [Determining the proper driver]

First look with [lspci] and find the device information:

`root `[`#`]`lspci`

     03:00.0 Ethernet controller: Marvell Technology Group Ltd. 88E8071 PCI-E Gigabit Ethernet Controller (rev 16)

It is also possible to use the `-n` option to give a short-hand notation (which might be easier to search for on the Internet):

`root `[`#`]`lspci -n`

     03:00.0 0200: 11ab:436b (rev 16)

The model name (`0200`) and vendor/model (`11ab:436b`) can be used to look up the device on a place like [WikiDevi](https://wikidevi.com/) or [Debian HCL](https://kmuto.jp/debian/hcl/) to find the right driver to use in Linux.

#### [Verifying the driver is loaded]

Getting the driver is less than half of the battle. Most of the trouble with drivers is making sure that they are loaded and operating correctly.

Relying on [lspci] again, run:

`root `[`#`]`lspci -k`

     03:00.0 Ethernet controller: Marvell Technology Group Ltd. 88E8071 PCI-E Gigabit Ethernet Controller (rev 16)
        Subsystem: Acer Incorporated [ALI] Device 014e
        Kernel driver in use: sky2

Note that here, an indicator is given that a driver is in use. If not, then no driver has claimed responsibility over this hardware. Assuming the driver was built as a module rather than built-in, try [modprobe \<modulename\>] to attempt loading the right module. If the driver was built-in, consider making it a module, because modules can be loaded with [modprobe] and unloaded with [modprobe -r] which saves on number reboots while debugging an issue.

#### [Troubleshooting a driver]

Compile the driver as a module, then capture the output it generates when the module is loaded. Make sure to first remove all modules that depend on the driver (see [loading kernel modules](https://wiki.gentoo.org/wiki/Kernel_Modules#Manual_loading "Kernel Modules")).

The following command will compare the [dmesg] output after removing the module (in this example, `r8169`) with the output after adding the module again, effectively showing the messages that were added (lines starting with +).

`root `[`#`]`diff -u <(modprobe -r r8169; dmesg) <(sleep 1; modprobe r8169; dmesg) | grep ^+`

The most common issue is missing firmware. If a message shows up that informs the administrator about missing firmware, grab either [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] or a specific firmware package from Portage and install it. After the firmware installation, unload and load the kernel module again to see if this fixes the situation.

## [Software issues]

### [Portage issues]

#### [Dependency graph [slot](https://wiki.gentoo.org/wiki/SLOT "SLOT") conflicts]

Occasionally, messages like this occur when trying to emerge a package:

[CODE] **Dependency graph error**

    !!! Multiple package instances within a single package slot have been pulled
    !!! into the dependency graph, resulting in a slot conflict:

Generally, this means that the packages listed have multiple requested versions in the dependency graph. And fortunately most, if not all, cases allow to resolve it by manually upgrading to the highest requested version. So assuming that the following message was received:

[CODE] **Example of dependency graph error**

    app-emulation/emul-linux-x86-xlibs:0
    (app-emulation/emul-linux-x86-xlibs-20120127::gentoo, installed) pulled in by
    ~app-emulation/emul-linux-x86-xlibs-20120127 required by (app-emulation/emul-linux-x86-medialibs-20120127::gentoo, installed)
    (and 2 more with the same problem)

    (app-emulation/emul-linux-x86-xlibs-20120520::gentoo, ebuild scheduled for merge) pulled in by
    >=app-emulation/emul-linux-x86-xlibs-20120520 required by (net-im/skype-2.2.0.35-r99::gentoo, ebuild scheduled for merge)
    ~app-emulation/emul-linux-x86-xlibs-20120520 required by (app-emulation/emul-linux-x86-medialibs-20120520::gentoo, ebuild scheduled for merge)

The most recent version desired is 20120520, so:

`root `[`#`]`emerge --ask --oneshot =app-emulation/emul-linux-x86-xlibs-20120520`

Often, it\'s advantageous to one-shot (`--oneshot` or `-1`) all of the conflicts at once because they sometimes depend on one another.

Here is another example of a block:

[CODE] **Example of a block conflict**

    app-text/poppler:0

     (app-text/poppler-0.24.5::gentoo, installed) pulled in by
       app-text/poppler:0/44=[xpdf-headers(+)] required by (dev-tex/luatex-0.76.0::gentoo, installed)
       app-text/poppler:0/44=[cxx,jpeg,lcms,tiff,xpdf-headers(+)] required by (net-print/cups-filters-1.0.43::gentoo, installed)

     (app-text/poppler-0.24.3::gentoo, ebuild scheduled for merge) pulled in by
       >=app-text/poppler-0.12.3-r3:0/43= required by (app-text/texlive-core-2013-r1::gentoo, installed)
       poppler:0/43

There should be no problem changing poppler versions. Note that [[[app-text/texlive-core]](https://packages.gentoo.org/packages/app-text/texlive-core)[]] does not require a specific version of poppler, but it needs to be rebuild with whatever version is used:

`root `[`#`]`emerge --ask --oneshot =app-text/poppler-0.24.5 app-text/texlive-core`

A possible slot conflict when disabling `gles2-only` for Plasma is:

[CODE] **KDE**

    dev-qt/qtbase:6

      (dev-qt/qtbase-6.7.3-r2:6/6.7.3::gentoo, ebuild scheduled for merge) USE="X accessibility concurrent cups dbus eglfs gui icu libinput libproxy network nls pengl sql sqlite ssl udev vulkan wayland widgets xml (zstd) -brotli -evdev -gles2-only -gssapi -gtk -journald -mysql -oci8 -odbc -postgres -renderdoc -sctp -syslog -test -tslib" pulled in by
        dev-qt/qtbase (Argument)

      (dev-qt/qtbase-6.7.3-r2:6/6.7.3::gentoo, installed) USE="X accessibility concurrent cups dbus eglfs gles2-only gui icu libinput libproxy network nls opengl sql sqlite ssl udev vulkan wayland widgets xml (zstd) -brotli -evdev -gssapi -gtk -journald -mysql -oci8 -odbc -postgres -renderdoc -sctp -syslog -test -tslib" pulled in by
        >=dev-qt/qtbase-6.7.2:6/6.7.3=[dbus,gles2-only,gui,widgets,X] required by (kde-plasma/libplasma-6.1.5:6/6::gentoo, installed) USE="gles2-only -debug -doc -test"
                                            ^^^^^^^^^^
        >=dev-qt/qtbase-6.7.2:6/6.7.3=[accessibility,gles2-only,gui,libinput,opengl,widgets] required by (kde-plasma/kwin-6.1.5:6/6::gentoo, installed) USE="accessibility (caps) gles2-only handbook lock shortcuts -debug -screencast -systemd -test"
                                                     ^^^^^^^^^^
        >=dev-qt/qtbase-6.7.2:6=[accessibility=,gles2-only=,gui,libinput,opengl,widgets] required by (kde-plasma/kwin-6.1.5:6/6::gentoo, installed) USE="accessibility (caps) gles2-only handbook lock shortcuts -debug -screencast -systemd -test"
                                                ^^^^^^^^^^^
        >=dev-qt/qtbase-6.7.2:6[dbus,gles2-only=,gui,widgets] required by (kde-plasma/kinfocenter-6.1.5:6/6::gentoo, installed) USE="gles2-only handbook -debug -usb"
                                     ^^^^^^^^^^^
        >=dev-qt/qtbase-6.7.2:6=[dbus,gles2-only=,gui,widgets,X] required by (kde-plasma/libplasma-6.1.5:6/6::gentoo, installed) USE="gles2-only -debug -doc -test"
                                      ^^^^^^^^^^^

    It might be possible to solve this slot collision
    by applying all of the following changes:
       - dev-qt/qtbase-6.7.3-r2 (Change USE: +gles2-only)

The equals signs denote all the packages must be emerged with matching USE flags. To resolve this, edit [/etc/portage/package.use] to USE `-gles2-only` for each package then issue to the set:

`root `[`#`]`emerge --oneshot kinfocenter kwin libplasma qtbase`

Here is another example that could have resulted in a blockage:

`root `[`#`]`emerge --ask --verbose --update --newuse --deep @world`

[CODE] **Example of an update conflict**

    sys-power/cpupower:0

    These are the packages that would be merged, in order:

    Calculating dependencies... done!

    Total: 0 packages, Size of downloads: 0 KiB

    WARNING: One or more updates/rebuilds have been skipped due to a dependency conflict:

    sys-power/cpupower:0

      (sys-power/cpupower-4.9.0-r1:0/0::gentoo, ebuild scheduled for merge) conflicts with
        <sys-power/cpupower-4.7 required by (mate-base/mate-applets-1.12.1-r4:0/0::gentoo, installed)
        ^                   ^^^

    Nothing to merge; quitting.

Portage warns about an update that can not be performed, however, there is no issue because this update is not required by a package. More precisely, the update must be skipped because mate-base/mate-applets-1.12.1-r4 requires a version of sys-power/cpupower package lower than 4.7.

## [System limitations prevent a proper build]

-   [System limitation insufficient RAM](https://wiki.gentoo.org/wiki/System_limitation_insufficient_RAM "System limitation insufficient RAM")

When compiling with **n** jobs parallel the requirement of RAM grows approximately by a factor **n**. Unfortunately we can not predict the exact amount of RAM needed nor we can predict how much RAM will be consumed by other programs.

## [Debug a binary]

Trouble shoot a compiled binary by [Debugging](https://wiki.gentoo.org/wiki/Debugging "Debugging") with powerful tools.

## [Collecting additional information]

When seeking help, often additional information will be asked, such as the output of a command. Some of these produce dozens or hundreds of lines of text - too much to be suitable for pasting into chat rooms, such as the [Gentoo IRC support channel](https://wiki.gentoo.org/wiki/IRC "IRC").

[Wgetpaste](https://wiki.gentoo.org/wiki/Wgetpaste "Wgetpaste") allows users to post short links to a website that contains long output.

To show the contents of [/etc/conf.d/net]:

`user `[`$`]`wgetpaste /etc/conf.d/net`

If someone needs the detailed output of an [lspci] command is:

`root `[`#`]`wgetpaste -c 'lspci -nnk'`

Sometimes it is necessary to redirect stderr to stdout so that error messages can be pasted as well:

`root `[`#`]`wgetpaste -c 'emerge -pv '`

-   In case of hardware problems or kernel issues:

`user `[`$`]`wgetpaste /usr/src/linux/.config`

-   In case of portage issues:

`root `[`#`]`emerge --verbose --info | wgetpaste`

-   In case of package installation failures:

`root `[`#`]`wgetpaste /var/tmp/portage/<category>/-<version>/temp/build.log`

-   In case of Xorg issues:

`user `[`$`]`wgetpaste /var/log/Xorg.0.log`

-   In case all installed packages on the system needs to be provided:

`root `[`#`]`eix-update && eix-installed all`

### [Wrapping things together]

Below is a shell function that can be used to have several commands executed and their output processed by a single [wgetpaste] command so that only one URL needs to be provided to the user or developer that wants to help out:

`root `[`#`]`wgetpaste -i -c "lspci -nnk" -c "lsusb" -c "cat /usr/src/*$(uname -r)/.config" -c "cat /var/log/Xorg.0.log" -c "dmesg" -c "eix-update" -c "eix-installed all"`

### [Please do not use pastebin services on the gentoo-user mailing list]

Most pastebin services expire old pastes periodically (not to mention that pastebin services are hardly profitable, and close down all the time) whereas mailing list messages are archived in multiple places and are referenced for years. If the relevant output is short, or can be trimmed, then copy and paste it into the body of the email - longer output can be directed into a text file and added as a plain attachment.

## [Forming a solution]

With a good description of the problem, a complete history of actions and all sorts of debugging data (problem details, hardware / software information, logs, backtraces and more) a good set of useful data is available to look for a solution.

In general, repeat the following steps to come to a solution:

-   Get an idea where the problem might be, think about possible causes.
-   If there are no obvious areas to look into, become more acquainted with the related areas or ask an expert more about it.
-   Sometimes it is necessary to make assumptions to proceed. When assumptions are made, put it to the test: false assumptions should not make users and developers blind of other causes.
-   Obtain additional debugging information in the area of a problem, or perform tests.

Often this will lead to multiple possible causes. It is important to test them (to verify it is the actual cause or not) and therefore test them individually; this is also known as \"divide and conquer\".

Let\'s say a problem like \"my browser sometimes displays white pages when I boot\" comes up and a lot of details are already known about it, then there may be number of possible causes:

-   Is this because the browser was improperly closed when the system rebooted?

Verify this by killing the process and pulling the plug several times, each time checking if the pages are white after booting again. If this is a cause, is it the actual cause or are there other causes?

-   Is this the result of a specific browser version being broken?

Try older or newer versions for a few days or reboots and see if they are broken as well.

And so on\...

With the additional information, dare to think about more specific causes:

-   Does a certain pinned tab X that loads plugin Y break the system?

Unpin the tab so it doesn\'t open on launch anymore or disable the plugin, see if this keeps the problem away.

-   Graphical issues were reported as well, might this maybe mean this is caused by the video drivers?

Try a different version for those drivers, or alternative drivers if available.

As each possible cause is investigated, the actual cause of the problem might come closer and closer.

And in the end, if the cause is still not found, see the [support](https://wiki.gentoo.org/wiki/Support "Support") article.

## [See also]

-   [Knowledge Base:Recovering from a kernel boot failure](https://wiki.gentoo.org/wiki/Knowledge_Base:Recovering_from_a_kernel_boot_failure "Knowledge Base:Recovering from a kernel boot failure")
-   [Project:Portage/Fixing broken portage](https://wiki.gentoo.org/wiki/Project:Portage/Fixing_broken_portage "Project:Portage/Fixing broken portage") --- provides guidance on how to manually update or fix a broken Portage installation - particularly in the event [emerge -v1 sys-apps/portage] cannot be run.
-   [Fix my Gentoo](https://wiki.gentoo.org/wiki/Fix_my_Gentoo "Fix my Gentoo") --- rescuing an installation when a chroot is not possible
-   [Project:Portage/FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ")
-   [Recovering from a malfunctioning installation](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks#Recovering_from_a_malfunctioning_installation "Gentoo installation tips and tricks")
-   [Support](https://wiki.gentoo.org/wiki/Support "Support") --- provide **support** for technical issues encountered when installing or using Gentoo Linux