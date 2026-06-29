+:-------------------------------------------------------------------------------:+:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| RelEng GRS                                                                      |                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Description                                                                     | The Gentoo Reference System (GRS) Suite is a set of tools for building and maintaining a well defined Gentoo system in which all choices in building the system are predefined in configuration files housed on a central git repository.                                         |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Project email]                       | [grs@gentoo.org](mailto:grs@gentoo.org)                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [IRC channel] | [[#gentoo-releng](ircs://irc.libera.chat/#gentoo-releng)] ([[webchat](https://web.libera.chat/#gentoo-releng)]) |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lead(s)                                                                         | -   [Anthony G. Basile](https://wiki.gentoo.org/wiki/User:Blueness "User:Blueness") (blueness)\                                                                                                                                                                                   |
|                                                                                 |     *Author*                                                                                                                                                                                                                                                                      |
|                                                                                 |                                                                                                                                                                                                                                                                                   |
|                                                                                 | \                                                                                                                                                                                                                                                                                 |
|                                                                                 | No lead election date set                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member(s)                                                                       |                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Subproject(s)\                                                                  | (none)                                                                                                                                                                                                                                                                            |
| [(and inherited member(s))]                                             |                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parent Project                                                                  | [Release Engineering](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng")                                                                                                                                                                                               |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Project listing](https://wiki.gentoo.org/wiki/Project:Gentoo "Project:Gentoo") |                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\

## Contents

-   [[1] [Description]](#Description)
-   [[2] [How to use the GRS suite]](#How_to_use_the_GRS_suite)
    -   [[2.1] [Quickstart]](#Quickstart)
    -   [[2.2] [Build a release with grsrun]](#Build_a_release_with_grsrun)
    -   [[2.3] [Maintain a release with grsup]](#Maintain_a_release_with_grsup)
-   [[3] [Catalyst-style stage1-stage2-stage3 runs with the GRS suite]](#Catalyst-style_stage1-stage2-stage3_runs_with_the_GRS_suite)

## [Description]

The Gentoo Reference System (GRS) Suite is a set of tools for building and maintaining a well defined Gentoo system in which all choices in building the system are predefined in configuration files housed on a central git repository. All systems built according to a particular GRS spec should be identical. As a \"from source\" distribution, Gentoo allows a large degree of customization. The space of all possible packages and USE flags is vast, not to speak of more radical choices such as different kernels (eg. Linux or FreeBSD), executable formats (eg. ELF or Mach-O), different C Standard Libraries (eg. glibc, uClibc or musl) and different providers of core userland utilities (eg. busybox or coreutils).

In contrast to other distributions where each instance of an installed system is nearly identical to another, the large array of choice in Gentoo means that any two systems are unlikely to be sufficiently similar that executables or libraries from one will \"just work\" on the other, even if the architecture and other hardware factors are the same; assuming, of course, there is no conscious effort to build identical systems. This is where the Gentoo Release System (GRS) Suite comes in. It does precisely this, namely, it provides an automated method for repeatedly and predictably generating identical Gentoo systems.

GRS is designed to work roughly as follows: Periodic release tarballs are generated which are \"polished\". For example, releases can provide pre-configured display managers, windowing systems and desktop themes, even user accounts and home directories. Installation should be as simple as unpacking the release tarball on pre-formated partitions with minimal or no further configuration. There is no need to build any packages or a kernel and everything is ready to go out of the box. A release tarball can be downloaded from some server or alternatively can be built locally. While these may not initially be identical because they were build at different times, after updating, both approaches should yield identical systems.

Updating a GRS system can proceed by either building packages locally, or downloading pre-built binpkgs. As long as one does not deviate from the GRS defined set of USE flags, maskings and other configuration parameters, both approaches should yield identical systems. A GRS system is always a Gentoo system, so at any time, one can elect to part ways from GRS and venture out on one\'s own! The GRS Suite provides a utilities to make sure that configurations in [/etc/portage] are properly maintained in a manner consistent with GRS, but emerge and other Portage utilities will always work. Even if one does deviate from the GRS specs, it should be possible to return to strict GRS using the Suite\'s utilities, provided one has not deviated too far.

GRS is provided by the [app-portage/grs] package. The same package is installed on either a server responsible for building the release tarballs and binpkgs, or on an actual GRS system. On the server, a daemon called [grsrun] will either do a release run, in which case it builds the release tarballs, or it will do an update run where it either builds or updates a bunch of extra binpkgs. For example, for GRS = desktop-amd64-uclibc-hardened, the release run builds a little under 900 packages and produces the polished release tarball, while the update run builds/updates about 5700 packages. The first update run after a new release is time consuming because some 5700 new packages must be built, but subsequent update runs need only build packages which were bumped since the last update run.

On the client, a utility called [grsup] acts as a wrapper to emerge. [grsup] will both manage the configuration files in [/etc/portage] as well as either builds or download the binpkg from a `PORTAGE_BINHOST`. After the initial installation of a GRS system, one need only run grsup to bring it up to date. While releases tarballs will be pushed out periodically, these are not used to update an existing GRS system, only to start new one. Rather, one GRS release should smoothly update to the next; in other words, each GRS release is equivalent to the previous release plus any updates since. The only reason to push out a new release tarball is to avoid having to subsequently push out a large number of updates for each new installation.

CAVEAT: This is work in progress. A few of the above point are marginally working or implemented. This warning will disappear after this whole project moves past being experimental.

Features:

-   The GRS suite does not hard code any steps for the release or update runs. Rather, a build script on the git repository describes the steps for building each particular GRS system. This makes GRS runs highly flexible. One need only transcribe the steps one would manually make in a chroot to build the system into build script directives, and [grsrun] will automatically repeat them.

<!-- -->

-   It is possible to script a GRS system to do the equivalent of catalyst runs.

<!-- -->

-   The use of Linux cgroup make management easy. There is no need to trap or propagate signals when writing the scripts that are to be run in the chroot. A simple SIGTERM to [grsrun] will ensure that all children process no matter how deep are properly terminated and that any bind-mounted filesystems are unmounted.

<!-- -->

-   A GRS system acts as a \"tinderbox lite\" in that build failures are reported. So as a GRS system evolves over time, as package are bumped, any breakages that are introduced will be caught and reported. \[TODO: get these reports automatically into Bugzilla.\]

## [How to use the GRS suite]

### [Quickstart]

tl;dr. This is a long document which tries to cover not only how to maintain a GRS system, but also how to build one from scratch using the GRS suite. If you\'re here because you downloaded one of the currently maintain GRS systems, affectionately called [Bluemoon, Lilblue, and Bluedragon Gentoo Linux](http://releases.freeharbor.net), and you just want a quick start on how to maintain those systems using [grsup] then this section is for you.

First, make sure you\'ve installed your system. There\'s instructions for [Lilblue](https://wiki.gentoo.org/wiki/Project:Hardened_uClibc/Lilblue "Project:Hardened uClibc/Lilblue") and [Bluedragon](https://wiki.gentoo.org/wiki/Project:Hardened_musl/Bluedragon "Project:Hardened musl/Bluedragon") on their home pages. All three systems are installed in a similar fashion and you can follow Lilblue\'s guide for Bluemoon. Once installed, you need to run [emerge \--sync] as root to create a local copy of the portage tree. That\'s sufficient on Bluemoon and Lilblue, but on Bluedragon you also need to update the overlay with [layman -S]. At that point you\'re all sync-ed up with the mirrors and you can run [grsup]. Without any flags, [grsup] will update your system with the latest packages off the BINHOST. Run [grsup -h] to see what other options are possible.

That\'s all there is to it, but keep one thing in mind. If you are an experienced Gentoo user, you may be tempted to edit files in [/etc/portage/] manually. You certainly can do that, and use [emerge] afterwards, but keep in mind that you are then parting ways with the \"Gentoo Reference System\" that you are tracking and if you later run [grsup] your manual editings will be clobbered and you\'ll revert to the GRS system \[TODO: there are some files which are not currently managed by [grsup], but they will be in the near future.\] Only [/etc/portage/make.conf] will be preserved, but it will be moved to a backup and the pristine GRS [make.conf] will be restored.

### [Build a release with grsrun]

The GRS build suite aims to be very flexible, so rather than overwhelm ourselves with possibilities, we\'ll go through one example scenario in detail. In this section, we\'ll be the maintainer of a GRS system and make use of the [grsrun] command to build a fully featured desktop system on a binhost server. Our final product for release will be a tarball of the system, complete with an already compiled kernel, pre-configured windowing system and a polished default user home and desktop, that is ready to run out-of-the-box. Just untar onto pre-formatted filesystems, install the bootloader, and reboot into a pristine and well polished system. In the next section, we\'ll use the [grsup] command to maintain an installed instance of our desktop. Maintaining a GRS system with [grsup] is completely optional and one can just treat it as any old Gentoo system, but if you want to follow the GRS spec as they change upstream, you need to use [grsup]. It\'s a wrapper on [emerge] which makes sure you don\'t deviate from the specs for your GRS system. But we\'re getting ahead of ourselves.

All the information to build a GRS system lives on one branch of a git repository. As of this writing there is only one such repository [https://gitweb.gentoo.org/proj/grs.git/](https://gitweb.gentoo.org/proj/grs.git/) with four branches:

           desktop-amd64-musl-hardened
           desktop-amd64-hardened
           desktop-amd64-uclibc-hardened
           stages-amd64-hardened

Each branch is dedicated to one particular GRS system, so let\'s take the desktop-amd64-musl-hardened system as our example. There\'s nothing special about it, and the fact that it is based on musl rather than glibc is not really relevant. If we check out that branch, we find the following at the top level:

           build
           core/
           README
           scripts/
           TODO

The [build] script is the most important file there since it contains the directives to [grsrun] for what it is supposed to do to build the system. It is the only file at the top level directory that [grsrun] will look at and you are free to put other things there, like a [README] or [TODO], since these will be ignored. They are there for human consumption.

The [core/] directory contains any files that are going to be copied into the new system. They are just copied directly into the GRS root. Any file, anywhere in the filesystem, with any content, can be copied in, clobbering whatever is already there. In our case, that directory contains the following (only partially reproduced here):

           core/
           ├── etc
           │   ├── avahi
           │   │   └── avahi-daemon.conf
           │   ├── conf.d
           │   │   ├── hostname
           │   │   └── xdm
           │   ├── fstab
           │   ├── grs
           │   │   ├── systems.conf
           │   │   └── world.conf
           │   ├── lilo.conf
           │   ├── modprobe.d
           │   │   └── blacklist.conf
           │   ├── portage
           │   │   ├── make.conf.CYCLE.1
           │   │   ├── make.conf.CYCLE.2
           │   │   ├── make.conf.CYCLE.3
           │   │   ├── make.profile -> ../../usr/portage/profiles/hardened/linux/musl/amd64
           │   │   ├── package.accept_keywords
           │   │   │   ├── app-portage_grs_0
           │   │   │   ├── dev-lib_libcgroup_0
           │   │   │   └── sys-libs_fts-standalone_0
           │   │   └── repos.conf
           │   │       └── gentoo.conf
           │   ├── resolv.conf
            ...
           │   ├── slim.conf
           │   ├── sudoers
           │   └── X11
           │       └── xorg.conf
            ...
           ├── usr
           │   └── share
           │       └── slim
           │           └── themes
           │               └── default
           │                   └── background.jpg
            ...
           └── var
               └── lib
                   └── portage
                       ├── world.CYCLE.1
                       ├── world.CYCLE.2
                       ├── world.CYCLE.3
                       └── world.CYCLE.4

You\'ll notice that there are quite a few files in /etc which pre-configure the system to make sure it works out-of-the-box. Eg1. We have /etc/conf.d/xdm configured to use slim as our desktop greeter, we have /etc/slim.conf set up so slim will behave a particular way and present a paricular theme and start up XFCE4 on login, and (not shown in the above listing) we have /etc/skel and one regular user\'s home directory set up with a nicely configured desktop once XFCE4 is running. Eg2. musl doesn\'t have lazy linking, so configuring X is even more painful than usual. We include an xorg.conf which should just work.

You\'ll also notice that there are several copies of make.conf and world. The [grsrun] command allows you to build your system in stages called \"cycles\". When you copy your files from [core/] to the root of your GRS system, you can select which cycle you want. If a file doesn\'t have a cycle number, then it is constant across cycles. But if it ends in .CYCLE.X, then it is copied in only when cycle X is selected. Of course, the .CYCLE.X suffix is removed. Here X must be an integer since there is a particular behavior when you select a cycle higher than your highest X \-\-- this will make more sense when we look at the `populate` directive below.

The [scripts/] directory contains scripts to be run in the GRS root as it is built. Think of these scripts as snippets of what you would type as you grow your stage3 into the system you want, like the steps you taken in the [Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page"). These scripts should be written in either bash or python since all stage3\'s come with these interpreters, but you could use any scripting language like perl if you\'ve already emerged perl at an early point in the build process.

In our example, these scripts are used in conjunction with the cycles we specify in our [core/]directory, but there is no necessary connection between cycles and scripts. So our build process goes something like this: copy and possibly overwrite some files for a particular cycle from [core/] to the GRS root, run one of our scripts, copy and possibly overwrite some other files for a different cycle from [core/] and then run some other scripts. Repeat until userland is done. Let look at this in detail:

At cycle 1, we start with an empty [world] file and a bland [make.conf] which does nothing more than repeat the CFLAGS, CHOST etc from the stage3 seed. Once these are in place, we run [scripts/cycle.1.sh] in the GRS root which basically adds the musl overlay. Of course to do so, you need to emerge layman first since that doesn\'t ship with our stage3, so our script looks like this:

[FILE] **`cycle.1.sh`Add musl overlay**

    #!/bin/bash
    source /etc/profile
    env-update
    emerge -b1q layman
    layman -L
    layman -a musl || true # don't fail if musl overlay has been already added
    layman -S              # update musl overlay if we were added perviously

Its just a few bash commands which achieve one goal: add the musl overlay to the stage3. How we downloaded the stage3, unpacked it, etc., we\'ll see below. Right now, just understand what this little piece accomplishes even if you don\'t see the full context.

At cycle 2, we add a world file of some 65 \"most dependent\" packages (IE packages which depend on other packages, but which are not themselves depended upon). These packages defines our desktop\'s \@world set. We expand our make.conf to define some more portage variables like LINGUAS, source our overlay which we added in the previous step and we rebuild all of \@world. Our [scripts/cycle.2.sh] looks as follows (modulo some details):

[FILE] **`cycle.2.sh`Rebuild the toolchain and world**

    #!/bin/bash
    source /etc/profile
    env-update
    emerge -b1q binutils
    emerge -b1q gcc
    emerge -b1q musl
    emerge -bevq --keep-going --with-bdeps=y @world

In this script, we first rebuild the toolchain. This is probably not necessary, but since musl is experimental we do it just to be sure it works (and we have the cpu cycles to murder!). Then we rebuild all of \@world. By the way, notice the -b flag to emerge because we want to store the .tbz2 files which we\'ll serve out from the binhost. There\'s a bit more to this script which we\'ll come back to in the next section when we discuss [grsup].

Next at cycle 3, we change the world file and update our USE flags slightly. If you\'ve ever build a large system from a stage3, you\'ve probably hit circular dependencies. These can be thorny from a logical point of view and so portage is not able to disentangle them \... yet. We resolve these much the same way you resolve them manually, you build with some set of USE flags that avoids the circular dependency and then add the flags you want back and rebuild. In our case, we need to avoid the old avahi-cups-zeroconf circularity (See [#222601](https://bugs.gentoo.org/show_bug.cgi?id=222601%7Cbug)), so we first build without cups and then rebuild with cups . Modulo some details we\'ll return to, our [scripts/cycle.3.sh\<]only has

[FILE] **`cycle.3.sh`Update world**

    #!/bin/bash
    source /etc/profile
    env-update
    emerge -buvNDq --keep-going --with-bdeps=y @world

to do an update with the new flags. We don\'t need a full \@world rebuild.

At this point you might think that all the scripts in the [scripts/] directory are about emerging components of your system, but this is not case. You can add services to runlevels, set up users and groups and to do any other post installation configurations as would if you were building your own custom system \-\-- except that here it is all scripted are reproduceable. The following are some extra scripts for our desktop-amd64-musl-hardened system:

[FILE] **`initrc.sh`Add services**

    #!/bin/bash
    # We default to classical interface naming.
    ln -sf /etc/init.d/net.lo /etc/init.d/net.eth0
    touch /etc/udev/rules.d/80-net-name-slot.rules

    rc-update add alsasound default
    rc-update add cupsd default
    rc-update add fcron default
    rc-update add net.eth0 default
    rc-update add postfix default
    rc-update add sshd default
    rc-update add xdm default
    rc-update add avahi-daemon default
    rc-update add dbus default
    rc-update add samba default
    rc-update add syslog-ng default

and

[FILE] **`passwd.sh`Add users and groups**

    #!/bin/bash
    echo root:root | chpasswd

    useradd -m gentoo
    gpasswd -a gentoo disk
    gpasswd -a gentoo wheel
    gpasswd -a gentoo audio
    gpasswd -a gentoo video
    gpasswd -a gentoo floppy
    gpasswd -a gentoo tape
    gpasswd -a gentoo cdrom
    gpasswd -a gentoo cdrw
    gpasswd -a gentoo usb

    gpasswd -a portage wheel

    echo gentoo:gentoo | chpasswd

    chown -R gentoo:gentoo /home/gentoo

    groupadd -g 9995 graudit
    groupadd -g 9996 grslink
    groupadd -g 9997 grasock
    groupadd -g 9998 grcsock
    groupadd -g 9999 grssock

and

[FILE] **`clean.sh`Clean up when done**

    #!/bin/bash
    for d in /tmp /var/tmp /var/log; do
        find $ -mindepth 1 -exec rm -rf  +
    done
    rm -rf /etc/resolv.conf

With above techniques, you can build and configure pretty much any userland you want for your GRS system. However, to have a system ready to go out-of-the-box, we\'ll also need a pre-compiled kernel, so [grsrun] is capable of providing that. [grsrun] builds the kernel external to the GRS root using the host\'s toolchain, packs it as a .tar.xz and installs it into the GRS root. The pre-compiled kernel package is stored in the [package/] directory as a file called linux-images/linux-image-\<version\>-\<flavor\>.tar.xz so it can be installed on a remote GRS system using [grsup]. (Note: \<flavor\> means which sources, you\'re using, like \'gentoo\', \'hardened\' or \'vanilla\'.) You\'ll probably want this if you want to provide packages for pre-compiled kernel updates.

Once userland and the kernel are built and installed, the GRS system root is finished. [grsrun] will create the tarball and digests to prepare it for shipping. At the user end, all that needs to be done is to extract the tarball over pre-formatted filesystems, do a quick chroot to install lilo (or whatever bootloader the GRS system comes with), and finally reboot into a pristine, well polished system. This is basically how [Lilblue](https://wiki.gentoo.org/wiki/Project:Hardened_uClibc/Lilblue "Project:Hardened uClibc/Lilblue") and the [Lemote Yeelong Desktop](https://wiki.gentoo.org/wiki/Project:Lemote_Yeeloong_Gentoo_Desktop "Project:Lemote Yeeloong Gentoo Desktop") are installed.

The process, however, doesn\'t have to stop here. If you want to provide additional binpkgs beyond those shipped with your release tarball, you can have [grsrun] continue to use the GRS root to build them. These binpkgs are stored in the [packages/] directory on the binhost and can be installed on local GRS systems either using [emerge] or [grsup].

This completes our overview but we\'re still missing some important details, so let\'s revisit the above from the point of view of the real heart of the GRS specs, the [build] script at the top level of the GRS git repo. It orchestrates the entire process with a very simple set of commands called \'directives\'. Since [grsrun] can install any number of cycles, or run any number of scripts in any order, you might wonder how does it know when to do what. That\'s what the [build] script is for, so let\'s take a look at the build script for desktop-amd64-musl-hardened:

[FILE] **`build`Script for desktop-amd64-musl-hardened**

    +log BEGIN
    log CYCLE_1
    mount
    populate 1
    runscript cycle.1.sh

    log CYCLE_2
    populate 2
    runscript cycle.2.sh

    log CYCLE_3
    populate 3
    runscript cycle.3.sh

    log Configure+Cleanup+Kernel
    runscript initrc.sh
    runscript passwd.sh
    runscript clean.sh
    unmount
    kernel

    log Tar+Hash
    tarit
    hashit

    +log Extras
    +mount
    +populate 4
    +runscript cycle.3.sh
    +unmount
    +kernel
    +log END

The directives here are \'log\', \'mount\', \'umount\', \'populate\', \'runscript\', \'kernel\', \'tarit\' and \'hashit\'. Let\'s describe each:

-   log: The \'log\' directive does exactly that. It places a message and a time stamp in [grsrun]\'s log which is found at [/var/log/grs/desktop-amd64-musl-hardened.log]. The name of the log file follows the name of the GRS system and it records all the output from the scripts run in the GRS root. This is useful for debugging what\'s going on in the chroot as you build the system. However, there is also another log generated called [grs-daemon-\.err] which records any exceptions thrown by the daemon spawned by [grsrun] to handle the build of this particular GRS system. This log is useful for debugging errors in the GRS suite itself. Both logs are auto-rotated on (re)starting up the daemon.

<!-- -->

-   mount: This directive will mount all the necessary directories below the GRS root. Unlike catalyst which creates a snapshot of the portage tree before bind-mounting it under the chroot, [grsrun] will mount the host\'s portage tree directly. This is a lot faster but also dangerous because changes to the portage tree while a run is in progress can adversely affect the system being built. Its recommended that [grsrun] be run on a dedicated server where you can synchronize changes to the portage tree with a run. \[TODO: add an option to mount which allows for snapshotting of the portage tree.\]

<!-- -->

-   umount: This directive does the opposite of \'mount\'. Since [grsrun] sets up its own cgroup [\[1\]](https://en.wikipedia.org/wiki/Cgroups), it tracks all process which might have open file descriptors on mounted filesystems. If any step fails, [grsrun] will clean up and umount itself. So you don\'t need to use \'umount\' defensively, only when you are really done with the mounted filesystems under your chroot. In the above example, we mount before we run scripts [cycle.1.sh], [cycle.2.sh] and [cycle3.sh] because these invoke [emerge] which requires the Portage tree be present. However we \'umount\' before packaging up our system for shipping because we don\'t want the Portage tree in our tarball. And if, say, [cycle.2.sh] fails, [grsrun] will umount everything for you just before it terminates.

<!-- -->

-   populate X: This directive copies the files from the [core/] directory of the GRS git repo into the GRS root, overwriting any files in the chroot. The integer X corresponds to the cycle number to selects the files as described above. If there is a sequence of cycled files, and X is bigger than any of the cycle numbers on the files, then the file with the largest cycle number is used. Eg. if the cycle of files is [make.conf.CYCLE.1], [make.conf.CYCLE.2], [make.conf.CYCLE.3] and X = 4 or greater, then [make.conf.CYCLE.3] is copied in as [make.conf].

<!-- -->

-   runscript X: This directive will run the \'X\' script in the GRS root. The above examples have the .sh suffix to indicate that they are shell scripts, but no suffix is really necessary, just a shebang on the first line. In fact, there is no restriction on the naming of scripts whatsoever. If you are starting with a stage3 tarball, \'X\' can be in either bash or python. If you emerged perl, say, in a previous step, then \'X\' can be in perl.

<!-- -->

-   kernel: This directive looks for a kernel configuration file in the GRS git repo at [scripts/kernel-config] and uses it to build a kernel image and modules. The version of the kernel is obtained from the third line of the config file, so that:

<!-- -->

           # Linux/x86 4.0.6-hardened-r2 Kernel Configuration

would use =sys-kernel/hardened-sources-4.0.6-r2 while

           # Linux/x86 4.0.5-gentoo Kernel Configuration

would use =sys-kernel/gentoo-sources-4.0.5. The kernel is built using the host\'s toolchain, not the GRS\'s toolchain, and the image and modules are bundled as linux-images/linux-image-4.0.6-hardened-r2.tar.xz under the [packages/] directory as well as is installed into the GRS root. Before building the kernel, however, this directive checks to see if the linux-image package for the requested version already exists and skips the build if it already does. This avoids rebuilding the same image repeatedly when doing an update run. If you want to force a rebuild, just remove the linux-image package. Remember, if you want to target a large variety of hardware, you\'ll want to turn on as many modules and features as possible in the kernel.

-   tarit \[ X \]: This directive will tar everything in the GRS root found under the [system] directory. The value \'X\' is optional. Without it, [grsrun] will name the tarball by the GRS system name followed by a time stamp. In our case, this would be something like desktop-amd64-musl-hardened-20150721.tar.xz. However, if X is supplied, the GRS name is replaced by X. For example, if we have \'tarit stage3-amd64-hardened\' then the tarball will be named stage3-amd64-hardened-20150721.tar.xz instead.

<!-- -->

-   hashit: This will create an MD5, SHA1, SHA512 and WHIRLPOOL hash of the tarball and place them in a file whose name is the same as the tarball name plus suffix .DIGESTS. Both the tarball and digest are placed in the GRS\'s work directory found at [/var/tmp/grs/desktop-amd64-musl-hardened] for our example.

So in sum, the [build]script orchestrates the entire build process from the initial seed (usually, but not necessarily, a stage3 tarball) until the final release tarball. However you\'ll notice a few steps after the tarball is mastered and the digest produced. The purpose of these lines is to build the extra binpkgs we want to serve out via our binhost beyond what is bundled in the release tarball, as we mentioned above. So in this case \'populate 4\' copies in the cycle 4 files and expands \@world to include some 5000 new packages and [cycle.3.sh] does an \`emerge -uvNDq \@world\` to build those packages. You\'ll also notice that these lines begin with +\'s. [grsrun] operates in two modes: 1) Without any flag [grsrun] will just do all the steps in the [build] script in order. This is \'release\' mode and it is used when preparing another release of the GRS system. 2) With the -u flag, [grsrun] runs in \'update\' mode and skips all the lines without +\'s. By marking only those lines needed to build updates, this mode is useful for generating binpkgs between releases.

We need to mention that an actual GRS run involves two \'invisible\' directives run before the build script directives are initiated. These are the \'sync\' and \'seed\' step. You don\'t need to, and indeed can\'t, specify them in your [build] script, as they just happen automatically. When [grsrun] is invoked, it reads its configuration file at [/etc/grs/system.conf] which specifies what GRS systems you\'re are going to build. \[TODO: add a flag which allows you to redirect to alt config file.\] Here\'s an example of the file:

[FILE] **`systems.con`Example systems.conf file**

    [desktop-amd64-musl-hardened]
    repo_uri : git://anongit.gentoo.org/proj/grs.git
    stage_uri : http://distfiles.gentoo.org/experimental/amd64/musl/stage3-amd64-musl-hardened-20150609.tar.bz2

    [desktop-amd64-uclibc-hardened]
    repo_uri : git://anongit.gentoo.org/proj/grs.git
    stage_uri : http://distfiles.gentoo.org/pub/gentoo/releases/amd64/autobuilds/current-stage3-amd64-uclibc-hardened/stage3-amd64-uclibc-hardened-20150705.tar.bz2

    [desktop-amd64-hardened]
    repo_uri : git://anongit.gentoo.org/proj/grs.git
    stage_uri : http://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64-hardened/stage3-amd64-hardened-20150702.tar.bz2

    [stages-amd64-hardened]
    repo_uri : git://anongit.gentoo.org/proj/grs.git
    stage_uri : http://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64-hardened/stage3-amd64-hardened-20150702.tar.bz2

Its in configparser format where each section defines a unique GRS system to build. The repo_uri line gives the location of the GRS git repo where a branch matching the section name is to be found. During the \'sync\' step, the git repo is cloned into [/var/lib/grs/desktop-amd64-musl-hardened] and then the desktop-amd64-muls-hardened branch is checked out. The later build directives will look into this directory for files to populate or scripts to run. A similar process takes place for each of the GRS systems specified in the various sections of the config file.

\[TODO: what are the permitted lines for each GRS system and what are the default values if a line is omitted since there are no required lines.\]

The \'seed\' step follows immediately after \'sync\' and it will download the stage tarball specified on the stage_uri line. It will place it at [/var/tmp/grs/desktop-amd64-musl-hardened] and unpack it. If it finds the stage tarball already there, it won\'t download it again. \[TODO: check the MD5 to make sure its not broken.\] \[TODO: allow a wild care in the stage_uri so we don\'t have to keep updating that line each time a new stage3 release comes out.\]

Since multiple GRS systems can be specified in the [systems.conf] file, you may wonder how does [grsrun] juggle multiple runs? When you run [grsrun], it will build each of the specified systems in parallel, spawning a daemon for each and isolating the files and process. So desktop-amd64-musl-hardened will have

  ---------------------------------------------------------- --------------------------------------------------
  File                                                       Purpose
  `/var/lib/grs/desktop-amd64-musl-hardened`                 local GRS git repo
  `/var/log/grs/desktop-amd64-musl-hardened.log`             logs message from chroot
  `/var/log/grs/grs-daemon-.log`                        log messages from daemon
  `/var/tmp/grs/desktop-amd64-musl-hardened/system`          root for this GRS system
  `/var/tmp/grs/desktop-amd64-musl-hardened/packages`        binpkgs for this GRS system
  `/var/tmp/grs/desktop-amd64-musl-hardened/kernel`          scratch directory for the kernel work
  `/var/tmp/grs/desktop-amd64-musl-hardened/work`            scratch directory for running \'populate\'
  `/var/tmp/grs/desktop-amd64-musl-hardened/.completed_XX`   completed directive at line XX of `build` script
  `/var/tmp/grs/desktop-amd64-musl-hardened/`                release tarball and digest are in this directory
  `/run/grs-desktop-amd64-musl-hardened.pid`                 pid file for daemon responsible for this GRS
  ---------------------------------------------------------- --------------------------------------------------

and similarly for desktop-amd64-uclibc-hardened and any other GRS systems specified. The daemons for each GRS system are (hopefully!) well behaved and you cannot spawn two daemons for the same GRS system running at the same time. That would be bad because the build process is assumed to be serial in the [build] script and the two daemons running simultaneoulsy would step over each other.

Once [grsrun] has sync-ed and seeded, it can proceed to build the GRS system according to the directives in the build script. As each step is completed a [.completed_XX] is placed in [/var/tmp/grs/desktop-amd64-musl-hardened/] directory. Here XX is a two digit number referring to the line number of the directive in the build script that completed successfully. The excepiton here is the \'sync\' and \'seed\' steps for which XX = \'sync\' or \'seed\' respectively. This show the progress but also allows you to pick up where you left off if something should go wrong. If [grsrun] is restarted, it will skip any steps for which it sees a [.completed_XX] file. If, for example, you identify the problem to be in the GRS git repo, and fix it there, you delete [.completed_sync], rerun [grsrun] and it will repeat the \'sync\' step, skip everything in between, and go to where you left off. You may, of course, have to also undelete some other steps along with the \'sync\', like the \'mount\' step, to make sure you have the right environment to pick up where you left off properly. \[TODO: change the completed file name from .completed_XX to .completed_XX\_\<directive+arguments\> for for example \'populate 4\' on line 31 would complete with .completed_31_populate_4. This would make it a lot easier to read which .completed files need to be removed on a restart. However, for the steps to skip, just match on .completed_XX because a reshuffling of the directives and their line numbers would cause havoc.\]

### [Maintain a release with grsup]

[grsrun] is used to build Gentoo system in a predictable way according to some GRS specs, so that two independent runs on different build machines should yield \"identical\" systems. But what do we mean by \"identical\"? We expect there to be some trivial differences like time stamps for the exact moment some file is generated, but we would hope for no significant differences \-\-- differences where exchanging files between the two would cause breakage due to, say, a mismatch between the ABI of a library and the executables that consume it.

However, the problem with this idea so far is that systems evolve over time. As changes are made to the Gentoo tree, or to the GRS specs, or both since the two are interrelated, resulting GRS systems will differ. A GRS system built today with some specs may be different from what you get tomorrow because some change was made to either the tree or the specs. Ideally, we\'d like to extend our notion of \"identical\" to include some continuity over time. So a GRS system built today will be identical to a GRS system built tomorrow provided that it is updated \-\-- again \"identical\" being measure in terms of file exchangeability. To update such a system it is not sufficient to just re-sync portage plus any overlays and run [emerge]. You have to also update the local copy of the GRS specs which contain the additional information, like what USE flags changed, and then apply those changes. To do this, the GRS suite provides three utilities, [grsup], [install-worldconf] and [clean-worldconf] which use the same configuration file, [world.conf], which is the heart of the GRS specs. With these, the user can track a GRS system as it evolves over time. It is important to note that a GRS system is still a Gentoo system, and you can use [emerge], modify USE flags, add/remove maskings, etc., as you would any Gentoo system, but if you do, you are departing from the GRS specs. Using [grsup], the user updates the system while tracking the evolution of the GRS specs. In fact, [grsup] is just a wrapper to [emerge] which also manages your configurations in [/etc/portage/] based on the [world.conf] file for the GRS system in question.

Before getting into the details of how [grsup] tracks a GRS system, we need to better understand the relationship between [grsrun] and [grsup]. [grsrun] builds a GRS system in the sense that it builds a system according to some GRS specs found on a branch of a git repo. However a system built in this manner does not necessarily include the GRS suite itself and so cannot track its own GRS specs! I give an example of this below where I illustrate how [grsrun] can be used to do a catalyst-like run to produce a stage3 which is identical to a stage3 produced by catalyst. \[TODO: We need to document the details of how the stages-amd64-hardened branch works.\] But a stage3 tarball doesn\'t include the app-portage/grs package and so doesn\'t contain [grsup] and isn\'t GRS complete \-\-- we will coin the term \"complete\" to refer to any GRS specs which specify a GRS system which is able to track its own specs. The careful reader will have noticed in the previous section that the scripts [cycle.1.sh], [cycle.2.sh], and [cycle.3.sh] are not identical to what one finds on the desktop-amd64-musl-hardened branch of [https://gitweb.gentoo.org/proj/grs.git/](https://gitweb.gentoo.org/proj/grs.git/). What I omitted was the code required to make the system GRS complete \-\-- this would have made those example unnecessarily complex. Once we understand how [grsup] and [world.conf] work we will be able to return to that example.

The driving file behind [grsup], [install-worldconf], and [clean-worldconf] is [world.conf]. It is written in configparser format and it specifies the files that live under [/etc/portage/]. On a GRS complete system, this file is found in both the GRS specs at [core/etc/grs/world.conf]and at [/etc/grs/world.conf]. The first thing that [grsup] does when run, is it syncs the remote git repo and copies that file from the git branch to its canonical location in [/etc/grs/] where it is expected by [grsup] and friends. The next thing [grsup] does is it reads that file and populates [/etc/portage/] accordingly. Let\'s look at a snippet of [world.conf] for desktop-amd64-musl-hardened to see how it works \-\-- there are over 2800 sections but we\'ll consider just three:

[FILE] **`world.conf`Snippet of world.conf for desktop-amd64-musl-hardened**

    [app-crypt/gnupg:0]
    package.use : app-crypt/gnupg:0 -doc -mta -nls -selinux -static -tools -usb bzip2 ldap readline smartcard
    package.accept_keywords : >=app-crypt/gnupg-2.1.6 ~amd64

    [app-crypt/gpa:0]
    package.use : app-crypt/gpa:0 -nls

    [app-crypt/gpgme:1]
    package.use : app-crypt/gpgme:1 -common-lisp static-libs
    package.env : app-crypt/gpgme:1 app-crypt_gpgme_1
    env : LDFLAGS=-largp

The file format should be self explanatory. Each section refers to a package in the usual \<cat\>/\:\<slot\> format. Each line of a section is a key:value pair where the key corresponds to a directory under [/etc/portage/] and the value is the contents of a file that is dropped into that directory. Multiline values are allowed even though none are show here. The package atom is canonicalized into a file name by replacing / and : by \_. So \'app-crypt/gnupg:0\' yields `app-crypt_gnupg_0` and a file by that name is dropped into [package.use/] with contents

           app-crypt/gnupg:0 -doc -mta -nls -selinux -static -tools -usb bzip2 ldap readline smartcard

while another file by the same name is dropped into [package.accept_keywords/] with contents

           >=app-crypt/gnupg-2.1.6 ~amd64

Similarly, the third section shown says to drop a file called `app-crypt_gpgme_1` into `package.use/`, [package.env/] and [env/]. Since the file in [package.env/] must point to the file [env/] (see [man 5 portage]) you\'ll notice that this file is referred to by its canonical name, `app-crypt_gpgme_1`.

Both [grsup] and [install-worldconf] read [world.conf] and populate [/etc/portage/], however it should be noted that this is just one step in a sequence of steps for [grsup], while it is the only thing that `install-worldconf` does. Its useful to isolate this one action for scripts used in building a GRS complete system as we\'ll see below. Populating [/etc/portage/] does take some time as it requires creating thousands of files, but it is necessary for that information to be there when the dependency graph is constructed. \[ASIDE: Implementation detail. Alternatives to copying in the files were considered such as bind mounting a temporary [/etc/portage/] but this was not much of a savings because IO times were eclipsed by much larger processing time. It might also be possible to expand the `_emerge` package to read world.conf directly rather than going through [/etc/portage] as a middle man.\]

Another difference between the two utilities is that [grsup] is designed to have your local system track the GRS specs as they change upstream. So before populating [/etc/portage/], it synchronizes the local GRS specs repo to the remote and replaces the local copies of [/etc/grs/world.conf] and [/etc/portage/make.conf] with the updated ones. It then reads [world.conf] and populates [/etc/portage//], clobbering old files and removing any not specified in [world.conf]. The only exception is [make.conf] which it backs up if it is different from the updated version. Using [grsup]is at odds with a user modified [/etc/portage/], but it always leaves the system in a state where local modifications are possible. A user can make changes and run [emerge] as one does on any old Gentoo system, but upon running [grsup] the system is brought back in line with the GRS specs.

What [grsup] installs at this point depends on what flags are provided. Any package installation or deletion is done with [emerge] behind the scenes. The following table summarizes [grsup]\'s actions:

  ----------------------- ----------------------------------------------------------------------------------
  Flags and Arguments     Action
  No flags or arguments   Update \@world using a BINHOST only.
  One or more pkg(s)      Update those pkg(s) using a BINHOST only.
  -r pkg(s)               Reinstall those pkg(s) using a BINHOST only.
  -l                      In conjunction with any of the previous, don\'t use a BINHOST but build locally.
  -d pkg(s)               Unmerge those pkg(s). No dep checking.
  -D                      Download all \@world pkgs but don\'t install. For later off-line work.
  -k \<version\>          Install linux-image-\<version\>, or latest version if \<version\>=\'latest\'.
  -h                      Print help.
  ----------------------- ----------------------------------------------------------------------------------

The final step taken by [grsup] is to remove those files in [/etc/portage/] that do not reference any installed packages. This is so the user isn\'t left with cruft in [/etc/portage/] should he choose to leave the GRS specs and \"go his own way\". Without cleaning up, the user would be face with sorting through hundreds if not thousands of files manually. Analogous to [install-worldconf], [clean-worldconf] isolates only the clean up step and is useful for scripting. As noted, installing all of [world.conf] is resource intensive, as is cleaning up, so to make life easy, a GRS specs maintainer should construct a [world.conf] which includes only packages that need to deviate from the defaults flags as defined in the Gentoo tree or any other added overlays. We do provide a utility called [make-worldconfig] which attempts to read [/etc/portage/] and construct a corresponding [world.conf] file, but as of this writing, it is \"clunky\" and the resulting file still needs manually editing.

We can now return to the scripts for desktop-amd64-musl-hardened and see how [install-worldconf] and [clean-worldconf] can be used to build a GRS complete system. As an example, we\'ll consider just the [cycle.2.sh] script:

[FILE] **`cycle.2.sh`Emerge \@world**

    #!/bin/bash
    source /etc/profile
    env-update
    ...
    emerge -b1q =app-portage/grs-9999
    ...
    install-worldconf
    emerge -bevq --keep-going --with-bdeps=y @world
    clean-worldconf

Here the reader can see that [[[app-portage/grs]](https://packages.gentoo.org/packages/app-portage/grs)[]] is first emerged to ensure that the GRS suite of utilities is present. Then before fully emerging \@world, we make sure that all of the [world.conf] are installed in [/etc/portage/] to guarantee that the correct flags/maskings/unmaskings/env are applied during the build. When done, we cleanup. In some situations, we could even use [grsup -l]instead of the sequence of [install-worldconf; emerge \...; clean-worldconf], but [grsup] has a much more restrictive scope and so its not recommended. For example here, we want to use the `-b` flag to build the binpkgs which [grsup] cannot do. The latter is focused on consuming, rather than providing, binpkgs.

A few final words about [grsup] are in order. It also reads [/etc/grs/systems.conf] to identify the remote git repo and branch which provide its GRS specs. However, since [systems.conf] may list more than one GRS system, [grsup] expects the first section to be the GRS specs it is supposed to track. This restrictions on order doesn\'t interfere with [grsrun] since the later doesn\'t care about section order. So there is no reason why a GRS complete system can\'t also act as a build machine for GRS systems and run [grsrun]. Finally, [grsup]logs to [/var/log/grs/grsup-desktop-amd64-musl-hardened.log], or similarly named for other GRS systems. Like [grsrun] it autorotates the logs on each invocation. \[TODO: we\'ll make this an option in the future with autorotation is off by default because it can lead to lots of little files in /var/log/grs. That\'s annoying.\]

## [Catalyst-style stage1-stage2-stage3 runs with the GRS suite]

It is possible to build stage1, stage2 and stage3 tarballs with [grsrun] in a manner very similar to catalyst. In fact, at the time of this writing, the stages-amd64-hardened specs at [http://gitweb.gentoo.org/proj/grs.git/](http://gitweb.gentoo.org/proj/grs.git/) produce a file-by-file identical stage3 compared to catalyst. However, it is not recommended that the GRS suite be used as a substitute for catalyst because the latter is a community standard based on mature code and is intentionally inflexible compare to GRS. In contrast GRS thaws certain frozen catalyst features and give the power to define those feature to the maintainer of the GRS specs. So while it is possible to produce identical stage3\'s as catalyst, it is easy, indeed too easy, to deviate from the well established standards of catalyst. Rather, we present the stages-amd64-hardened specs here as an academic exercise. It exposes some features that our earlier example didn\'t and it can serve as a model for similar GRS specs.

The following is the [build] file, minus some logging:

[FILE] **`build`Script for stages-amd64-hardened**

    mount
    populate 1
    runscript cycle.1.sh
    runscript cycle.1.py
    pivot tmp/stage1root
    runscript clean.sh
    unmount
    tarit stage1-amd64-hardened
    hashit

    mount
    populate 2
    runscript cycle.2.sh
    runscript clean.sh
    unmount
    tarit stage2-amd64-hardened
    hashit

    mount
    populate 3
    runscript cycle.3.sh
    runscript clean.sh
    unmount
    tarit stage3-amd64-hardened
    hashit

\
There are a few things to note here:

-   There is a `cycle.1.sh` run after an initial `populate 1`, but there is also a `cycle.1.py`. As stated earlier, the snippets of code run using `runscript` can be in any language for where there is an interpreter present in the GRS system. Since all stage3\'s comes with both bash and python, you can use either.

<!-- -->

-   pivot tmp/stage1root: This is another directive not described above. It exchanges the current GRS system root with the directory `tmp/stage1root` within it. The old root is moved out of the way and will no longer be used, and any further building will continue with the new root. (As an analogy, think of `pivot_root` used in many init script to switch root.) This allows you build a chroot within a chroot and then use it. This is how catalyst builds a stage1 \-\-- roughly speaking, it does `ROOT=/tmp/stage1root emerge @system` within a stage3 from a previous run.

<!-- -->

-   tarit X: This produces a tarball with name X-\<timestamp\>.tar.xz rather than using the GRS specs name in the place of X. During this run we will produce three tarballs, name stage-amd64-hardened-\<timestamp\>.tar.xz, whereas the GRS specs name is stages-amd64-hardened.

<!-- -->

-   There are no leading \'+\' markers to indicate directives for update runs. This [build] has no updates, it is just for releases.

\
That covers the [build] script. Let\'s look at each of the code snippets run by [runscript]:

[FILE] **`cycle.1.sh`Bash script run during cycle 1**

    #!/bin/bash -e
    source /etc/profile
    env-update
    USE="build" emerge -bkNu1q sys-apps/portage

This little snippet just makes sure portage is up to date. [catalyst] does this to be safe and so do we.

[FILE] **`cycle.1.sh`Python script run during cycle 1**

    #!/usr/bin/python3.4
    import os
    import re
    import shutil
    import portage
    from grs.Execute import Execute

    def scan_profile_stack(pfile):
        datoms = []
        for profile in portage.settings.profiles:
            fpath = os.path.join(profile, pfile)
            datoms.append(portage.grabfile_package(fpath))
        atoms = []
        for d in portage.stack_lists(datoms, incremental=1):
            m = re.search('^\*?(.*)', d)
            atoms.append(m.group(1))
        return atoms

    def get_blist():
        plist = scan_profile_stack('packages')
        blist = scan_profile_stack('packages.build')
        for p in plist:
            try:
                i = blist.index(portage.dep_getkey(p))
                blist[i] = p
            except ValueError:
                pass
        return ' '.join(blist)

    use_flags = '-* bindist build %s' % portage.settings['BOOTSTRAP_USE']
    subchroot = '/tmp/stage1root'
    cpu_flags = 'mmx sse sse2'
    emerge_env =

    cmd = 'emerge -bkNu1q sys-apps/baselayout'
    Execute(cmd, timeout=None, extra_env=emerge_env, logfile=None)

    os.makedirs('/tmp/stage1root/etc/portage', mode=0o755, exist_ok=True)
    shutil.copy('/etc/portage/make.conf', '/tmp/stage1root/etc/portage')

    cmd = 'emerge -bkNu1q %s' % get_blist()
    Execute(cmd, timeout=None, extra_env=emerge_env, logfile=None)

    for d in ['info', 'doc', 'man', 'zoneinfo']:
        cmd = 'find /tmp/stage1root/usr/share -type d -iname %s -exec rm -rf  +' % d
        Execute(cmd, timeout=None, extra_env=emerge_env, logfile=None)

This script is a bit long, but it shows a nice technique you can employ if you script in python. You can make use of the portage API. Most of this code is adapted from [catalyst], but its worth reviewing here. The two functions get_blist() and scan_profile_stack() construct the \@system set by looking at all [packages] and [packages.build]files throughout the profile stack. This set is then emerged to ROOT with various USE flags set using GRS\'s Execute() class. Note how environment variables are constructed and passed effectively running `ROOT=/tmp/stage1root emerge @system` (roughly speaking).

[FILE] **`cycle.2.sh`Bash script run during cycle 2**

    #!/bin/bash -e
    /usr/portage/scripts/bootstrap.sh -q

    for d in info doc man zoneinfo; do
        find /usr/share -type d -iname $ -exec rm -rf  +
    done

Again, this is directly lifted from [catalyst]. Once [tmp/stage1root] is pivoted out o the initial seed chroot, the toolchain is rebuilt. This ensures a consistent self-building toolchain which can then be used to rebuild all of \@system in cycle 3 where we run:

[FILE] **`cycle.3.sh`Bash script run during cycle 3**

    #!/bin/bash -e
    emerge -bkNe1q @system
    emerge --depclean

Finally we note that after each cycle, before we unmount and tar our chroot, we run [clean.sh]:

[FILE] **`clean.sh`Clean up at the end of each cycle**

    #!/bin/bash -e
    for d in /tmp /var/tmp /var/log; do
        find $ -mindepth 1 -exec rm -rf  +
    done
    rm -rf /etc/resolv.conf

Various directories are emptied and [/etc/resolv.conf] is removed. Its not a problem that we remove [revolv.conf] even though we still need it, because the GRS repo contains that file and it gets copied back into the GRS system root when we run the `populate` directive at the beginning of a stage cycle. We need to remove it so it doesn\'t end up in the final tarball.

At the end of this build, [/var/tmp/grs/stages-amd64-hardened] should contain three tarballs, stage-amd64-hardened-\<timestamp\>.tar.xz. As already stated, this produced file-by-file identical stage tarballs as [catalyst].