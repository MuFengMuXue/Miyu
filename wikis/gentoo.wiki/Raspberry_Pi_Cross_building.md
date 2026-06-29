This page contains [[changes](https://wiki.gentoo.org/index.php?title=Raspberry_Pi/Cross_building&diff=1420930)] which are not marked for translation.

\

[]  As of **2025-11-23**, the information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Raspberry_Pi/Cross_building&action=edit).

** Important**\
This guide is largely out of date and been replaced with faster methods such as [Binary_package_guide#Building_for_other_architectures](https://wiki.gentoo.org/wiki/Binary_package_guide#Building_for_other_architectures "Binary package guide").

Building almost any software on embedded SoC computers such as the [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi") can take a very, very long time - especially when many dependencies are involved. Fortunately, it is possible to offload much of the heavy lifting for compilation to a more powerful build system (such as a Gentoo desktop/server with more compute cores and more memory) using [distcc] and [crossdev]. This time saving tactic is only possible for packages that are written in language that require compiling (such as C, C++, etc.).

** Note**\
The following guide does not work for recent versions of crossdev and needs to be updated.

## Contents

-   [[1] [distcc]](#distcc)
    -   [[1.1] [Raspberry Pi and build server(s)]](#Raspberry_Pi_and_build_server.28s.29)
        -   [[1.1.1] [OpenRC]](#OpenRC)
        -   [[1.1.2] [Systemd]](#Systemd)
    -   [[1.2] [Raspberry Pi only]](#Raspberry_Pi_only)
-   [[2] [crossdev]](#crossdev)
    -   [[2.1] [crossdev with musl]](#crossdev_with_musl)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [distcc]

It is also suggested that the first package you build on the Raspberry Pi should be distcc, as it will dramatically speed up subsequent packages that require a lot of compilation.

### [][Raspberry Pi and build server(s)]

On the Raspberry Pi and on all build servers install [[[sys-devel/distcc]](https://packages.gentoo.org/packages/sys-devel/distcc)[]]:

`root `[`#`]`emerge --ask sys-devel/distcc`

#### [OpenRC]

Edit the distcc config file to ensure it is on the right subnet for the network configuration. For example:

[FILE] **`/etc/conf.d/distccd`**

    DISTCCD_OPTS="$ --allow 192.168.1.0/24"

#### [Systemd]

When using systemd edit the config file for the systemd service:

[FILE] **`/etc/systemd/system/distccd.service.d/00gentoo.conf`**

    Environment="ALLOWED_SERVERS=192.168.1.0/24"

Then register and start the distcc daemon:

`root `[`#`]`rc-update add distccd default `

`root `[`#`]`rc-config start distccd `

Or for systemd:

`root `[`#`]`systemctl enable distccd `

`root `[`#`]`systemctl start distccd `

### [Raspberry Pi only]

Tell Portage to use distcc:

[FILE] **`/etc/portage/make.conf`**

    FEATURES="distcc"

(Optional) Also add `buildpkg` to the `FEATURES` variable to tell the Raspberry Pi to build package files for everything it builds (if you want to use the same setup on multiple Raspberry Pis without recompiling).

\
Edit the distcc host file to tell your Raspberry Pi to submit compile jobs to the server:

[FILE] **`/etc/distcc/hosts`**

    # --- /etc/distcc/hosts -----------------------
    # See the "Hosts Specification" section of
    # "man distcc" for the format of this file.
    #
    # By default, just test that it works in loopback mode.
    [YOUR HOSTS HERE - first host is first preference] 127.0.0.1

Now you will need to tell distcc the specific compiler name to use instead of just \"gcc\":^[\[1\]](#cite_note-1)^

`root `[`#`]`cd /usr/lib/distcc/bin `

`root `[`#`]`ls -l`

    total 0
    lrwxrwxrwx  1 root root 15 Dec 23 20:13 c++ -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Dec 23 20:13 cc -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Dec 23 20:13 g++ -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Dec 23 20:13 gcc -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Dec 23 20:13 armv6j-unknown-linux-gnueabihf-c++ -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Dec 23 20:13 armv6j-unknown-linux-gnueabihf-g++ -> /usr/bin/distcc
    lrwxrwxrwx  1 root root 15 Dec 23 20:13 armv6j-unknown-linux-gnueabihf-gcc -> /usr/bin/distcc

We need to replace those symlinks with the following script:

[FILE] **`/usr/lib/distcc/bin/armv6j-unknown-linux-gnueabihf-wrapper`Distcc crossdev wrapper file**

    #!/bin/bash
    exec /usr/lib/distcc/bin/armv6j-unknown-linux-gnueabihf-g$ "$@"

`root `[`#`]`rm c++ g++ gcc cc `

`root `[`#`]`chmod a+x /usr/lib/distcc/bin/armv6j-unknown-linux-gnueabihf-wrapper `

`root `[`#`]`ln -s armv6j-unknown-linux-gnueabihf-wrapper cc `

`root `[`#`]`ln -s armv6j-unknown-linux-gnueabihf-wrapper gcc `

`root `[`#`]`ln -s armv6j-unknown-linux-gnueabihf-wrapper g++ `

`root `[`#`]`ln -s armv6j-unknown-linux-gnueabihf-wrapper c++ `

Double check that you did things right:

`root `[`#`]`ls -l`

    total 4
    lrwxrwxrwx 1 root root 15 Dec  8 00:38 armv6j-unknown-linux-gnueabihf-c++ -> /usr/bin/distcc
    lrwxrwxrwx 1 root root 15 Dec  8 00:38 armv6j-unknown-linux-gnueabihf-g++ -> /usr/bin/distcc
    lrwxrwxrwx 1 root root 15 Dec  8 00:38 armv6j-unknown-linux-gnueabihf-gcc -> /usr/bin/distcc
    -rwxr-xr-x 1 root root 85 Dec  8 01:04 armv6j-unknown-linux-gnueabihf-wrapper
    lrwxrwxrwx 1 root root 38 Dec  8 01:05 c++ -> armv6j-unknown-linux-gnueabihf-wrapper
    lrwxrwxrwx 1 root root 38 Dec  8 01:04 cc -> armv6j-unknown-linux-gnueabihf-wrapper
    lrwxrwxrwx 1 root root 38 Dec  8 01:04 g++ -> armv6j-unknown-linux-gnueabihf-wrapper
    lrwxrwxrwx 1 root root 38 Dec  8 01:04 gcc -> armv6j-unknown-linux-gnueabihf-wrapper

You can now check what is being dispatched to your build machines while doing an emerge operation:

`root `[`#`]`DISTCC_DIR="/var/tmp/portage/.distcc/" distccmon-text 1`

## [crossdev]

This will setup crossdev on your build servers so that they can compile binaries compatible with the Raspberry Pi. Note that you can have multiple compilation nodes - just add them to the list of hosts on the Raspberry Pi. Distcc will decide when to distribute the compilation though, so chances are you will never be able to fully load even a single modern build server with jobs from the Raspberry Pi.

Install [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]]:

`root `[`#`]`emerge --ask sys-devel/crossdev`

You will need to maintain separate portage profiles for the Raspberry Pi and your server\'s default, so you must convert your existing profile files to folders.

Copy the following file to [\~/convert-profile-to-files.sh], and then run it as root:

[FILE] **`~/convert-profile-to-files.sh`Convert profile files to folders**

    #!/bin/bash
    PROFILE_DIR="/etc/portage"

    if [ ! -e $ ]; then
      mkdir $;
    fi;

    for PACK_DIR in package.env package.accept_keywords package.keywords package.use package.unmask package.mask; do
      CUR_DIR="$/$"
      if [ ! -e $ ]; then
        mkdir $
      fi

      if [ -e $ -a ! -d $ ]; then
        mv $ $.moving
        mkdir $
        mv $.moving $/monolithic
      fi
    done

    echo "Completed!"

Create a cross toolchain for ARM: (drop the `-S` option from the command when planning to run an unstable system):

`root `[`#`]`crossdev -S -t armv6j-unknown-linux-gnueabihf`

If the cross toolchain for ARM fail to build try this:

`root `[`#`]`CFLAGS="-O2 -pipe" CXXFLAGS="$" crossdev -S -t armv6j-unknown-linux-gnueabihf`

### [crossdev with musl]

Pie needs to be enabled for gcc on the build-server(s), otherwise the crossbuilt packages will segfault after throwing a `warning: creating DT_TEXTREL in a PIE` during the build phase.

`root `[`#`]`crossdev --genv 'USE="pie ssp"' -S -t armv6j-unknown-linux-musleabihf `

After compilation confirm similar flags of your gcc package on build-server(s) & raspberry pi

`root `[`#`]`/usr/bin/armv6j-unknown-linux-musleabihf-gcc -v `

For testing use the following suggestion from: [the testing section of Distcc wikipage](https://wiki.gentoo.org/wiki/Distcc#Testing "Distcc")

## [See also]

-   [distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") --- a program designed to distribute compiling tasks across a network to participating hosts.
-   [Distcc/Cross-Compiling](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling "Distcc/Cross-Compiling") --- shows the reader how to set up distcc for cross-compiling across different processor architectures.

## [References]

1.  [[[↑](#cite_ref-1)] [See [here](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling#Configuring_distcc_to_cross-compile_correctly "Distcc/Cross-Compiling") for an explanation.]]