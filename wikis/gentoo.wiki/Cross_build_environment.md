** Warning**\
The [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") article replaces this page ([Embedded_Handbook/General/Compiling with qemu user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot") may also be of interest).

**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

\
TLDR: **Do not use this article!**

\

------------------------------------------------------------------------

This article provides instructions on creating a cross build environment using [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev").

Cross build environments are needed for different situations:

-   To cross build software for slow target hosts on a fast build host.
-   To build software with a different toolchain (e.g. different libc versions).
-   When a specialized system environment is needed:
    -   e.g. a separate multilib system for binaries with abnormal dependencies to be kept separate from the main system (like the [Steam](https://wiki.gentoo.org/wiki/Steam "Steam") platform).
    -   e.g. a base image for Docker containers.

Users may find the [Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook "Embedded Handbook") more helpful and possibly [Embedded_Handbook/General/Compiling with qemu user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot") in particular.

## Contents

-   [[1] [Create the cross toolchain]](#Create_the_cross_toolchain)
-   [[2] [Update the target build configuration]](#Update_the_target_build_configuration)
    -   [[2.1] [Raspberry Pi specific]](#Raspberry_Pi_specific)
    -   [[2.2] [Allwinner A20 specific]](#Allwinner_A20_specific)
-   [[3] [Build the base system]](#Build_the_base_system)
    -   [[3.1] [Rust packages]](#Rust_packages)
-   [[4] [Chroot into the target environment]](#Chroot_into_the_target_environment)
-   [[5] [Known bugs and limitations]](#Known_bugs_and_limitations)
    -   [[5.1] [Updating the cross toolchain]](#Updating_the_cross_toolchain)
-   [[6] [Cross building static binaries for closed systems]](#Cross_building_static_binaries_for_closed_systems)
    -   [[6.1] [Cross build toolchain for static binaries]](#Cross_build_toolchain_for_static_binaries)
    -   [[6.2] [Customized glibc]](#Customized_glibc)
        -   [[6.2.1] [(Optional) Create an customized glibc ebuild]](#.28Optional.29_Create_an_customized_glibc_ebuild)
        -   [[6.2.2] [Rebuild a customized glibc]](#Rebuild_a_customized_glibc)
    -   [[6.3] [Build the desired software]](#Build_the_desired_software)
    -   [[6.4] [Example: Use a statically linked privoxy on Android]](#Example:_Use_a_statically_linked_privoxy_on_Android)
-   [[7] [See also]](#See_also)
-   [[8] [References]](#References)

## [Create the cross toolchain]

** Warning**\
LTO users will run into a few issues using crossdev so it\'s recommended to check the Known Bugs Section first to be aware of the workarounds.

-   Install crossdev:

`root `[`#`]`emerge --ask sys-devel/crossdev`

** Important**\
An overlay must be created for crossdev, otherwise it may use any existing overlay to save generated ebuilds. More info: [Crossdev#Crossdev_overlay](https://wiki.gentoo.org/wiki/Crossdev#Crossdev_overlay "Crossdev").

-   Install the toolchain. Target (`-t`) takes a tuple [ARCH-VENDOR-OS-LIBC]; see `crossdev -t help`

`root `[`#`]`crossdev -t arch-vendor-os-libc`

-   Examples for targets:
    -   Bare metal [ARM](https://wiki.gentoo.org/wiki/ARM "ARM") targets: `arm-none-eabi` (see [ARM](https://wiki.gentoo.org/wiki/ARM "ARM") what else is needed for Cortex-R and Cortex-M devices)
    -   For a [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi"):
        -   Raspberry Pi A, A+, B, B+: `armv6j-hardfloat-linux-gnueabi`
        -   Raspberry Pi 2 or 3 B in 32-bit mode: `armv7a-unknown-linux-gnueabihf`
        -   Raspberry Pi 3 64-bit, [Raspberry Pi 4](https://wiki.gentoo.org/wiki/Raspberry_Pi4_64_Bit_Install "Raspberry Pi4 64 Bit Install") `aarch64-unknown-linux-gnu`
    -   For a amd64 multilib environment (when you\'re not in x86_64 natively): `x86_64-multilib-linux-gnu`
    -   And many more combinations, depending on support in gcc, a libc, binutils etc\... It solely depends on the target platform.

** Note**\
If encountering a problem creating the [gcc] stage 2 (for [gcc] v5), see [Known bugs and limitations](#Known_bugs_and_limitations) below (if required, add [\--genv \'EXTRA_ECONF=\"\--disable-libstdc++-v3\"\'] to the [crossdev] command line).

## [Update the target build configuration]

-   The target [make.conf] should be changed according to the installation handbook. For the base system at least, these options should be checked and the rest can be configured later:

[FILE] **`/usr/<TARGET>/etc/portage/make.conf`**

    # Check your target architecture
    ARCH="arm"
    # Remove buildpkg if you don't want all binary packages in $/packages
    FEATURES="buildpkg"
    # Disable 'acl' to build the base system (essential packages may fail cross-compilation otherwise). Enable it later if it's needed.
    USE="$ -pam -acl"
    # Set -j1 for debugging failed compilation if necessary, otherwise set the number of build jobs appropriate to the number of CPU cores
    MAKEOPTS="-j5"
    # You can't use -march=native here if the target has a different CPU. See the following subsections for useful adaptions.
    CFLAGS="..."

-   Set the appropriate [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"). See below for target architecture specific examples.
-   If built on amd64, see the lib64-bug at [#Known_bugs_and_limitations](#Known_bugs_and_limitations)

### [Raspberry Pi specific]

For the original Raspberry Pi

[FILE] **`/usr/<TARGET>/etc/portage/make.conf`**

    ...
    CFLAGS="-mfpu=vfp -mfloat-abi=hard -march=armv6zk -mtune=arm1176jzf-s -O2 -pipe"
    ...

-   Set the appropriate make profile. For the Raspberry Pi, it might be:

`pi #``ARCH=arm PORTAGE_CONFIGROOT=/usr/armv6j-hardfloat-linux-gnueabi eselect profile set default/linux/arm/17.0/armv6j`

### [Allwinner A20 specific]

In addition to the auto-generated file content, the following modifications are necessary for successful cross-compilation:

[FILE] **`/usr/armv7a-hardfloat-linux-gnueabi/etc/portage/make.conf`**

    ...
    # These use flags are required for successful cross-compilation (Aug. 2017)
    # Motivation for "-native-extensions": https://bugs.gentoo.org/628440
    USE="$ -pam -acl -ncurses -xattr -vtv -native-extensions"
    # CFLAGS="-Ofast -fomit-frame-pointer -pipe -fno-stack-protector -U_FORTIFY_SOURCE -march=armv7ve -mtune=cortex-a7 -mfloat-abi=hard -mfpu=neon-vfpv4 -funsafe-math-optimizations"
    # (Above CFLAGS were not helpful (Aug. 2017))
    CFLAGS="-O2 -pipe"
    ...

-   Set the appropriate make profile. For Allwinner A20 based boards it would be:

`sunxi #``cd /usr/armv7a-hardfloat-linux-gnueabi/etc/portage && rm make.profile && ln -s /var/db/repos/gentoo/profiles/default/linux/arm/17.0/armv7a make.profile`

## [Build the base system]

The base system can either be be built from scratch or stage3 tarball can be unpacked into [/usr/\<TARGET\>]. To build it from scratch:

-   Build the system packages:

    :::: cmd-box


    `root `[`#`]`<TARGET>-emerge -uva --keep-going @system`


    ::::

<!-- -->

-   For the Raspberry Pi, it would be:

    :::: cmd-box


    `pi #``armv6j-hardfloat-linux-gnueabi-emerge -uva --keep-going @system`


    ::::

<!-- -->

-   For the Allwinner A20, it would be:

    :::: cmd-box


    `sunxi #``armv7a-hardfloat-linux-gnueabi-emerge -uva --keep-going @system`


    ::::

    :::: cmd-box


    `sunxi #``armv7a-hardfloat-linux-gnueabi-emerge -uva --keep-going dev-util/systemtap # in case the previous command fails due to missing sys/sdt.h`


    ::::

(Do not worry about failed packages, this will be fixed later)

-   Build other essential packages:

`root `[`#`]`<TARGET>-emerge -uva1 --keep-going $(egrep '^[a-z]+' /var/db/repos/gentoo/profiles/default/linux/packages.build)`

-   To build the failed packages, it may be needed to compile them \"natively\", which means in this case, that the packages need to be compiled in the target chroot environment. If the target host has a different architecture a [qemu-chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot") is needed. For targets that the build host CPU can handle directly, the following steps can be skipped, to chroot directly into the target environment.
    -   Install QEMU on the host:

    :::: cmd-box


    `root `[`#`]`emerge --ask app-emulation/qemu`


    ::::

    -   Prepare QEMU for the target (in this case for the ARM architecture):

    :::: cmd-box


    `root `[`#`]`QEMU_USER_TARGETS="arm" QEMU_SOFTMMU_TARGETS="arm" USE="static-user static-libs" emerge --ask --buildpkg --oneshot qemu`


    ::::

    -   Install QEMU to the build environment:

    :::: cmd-box


    `root `[`#`]`cd /usr/<TARGET> && ROOT=$PWD/ emerge --ask --usepkgonly --oneshot --nodeps qemu`


    ::::

    -   A first test:

    :::: cmd-box


    `root `[`#`]`/etc/init.d/qemu-binfmt start && cd /usr/<TARGET> && chroot . /bin/bash --login`


    ::::

If it works, leave the chroot and go on with the next steps.

-   -   Optional: This step is not necessary in most cases. To make the target environment emulation more complete, a wrapper can be used, that passes the correct cpu option to qemu. The following would be an example for the Raspberry Pi cpu option for qemu (-cpu arm1176). Please check if the command at the end (qemu-arm) is present on the build host.

        ::::: gw-box
        ::: box-caption
        [CODE]
        :::

        :::
            #include <string.h>
            #include <unistd.h>

            int main(int argc, char **argv, char **envp)
        :::
        :::::

<!-- -->

-   -   Build it with

        :::: cmd-box


        `pi #``gcc -static qemu-wrapper.c -Ofast -s -o /usr/armv6j-hardfloat-linux-gnueabi/usr/local/bin/qemu-wrapper`


        ::::

### [Rust packages]

Some packages (such as gnome-base/librsvg) depend on a rust cross toolchain. To build the rust cross toolchain first add the \"rust-src\" use flag to dev-lang/rust:

[FILE] **`/etc/portage/package.use`Adding rust-src USE**

    dev-lang/rust rust-src

Next modify make.conf to add the necessary LLVM targets:

[FILE] **`/etc/portage/make.conf`Adding LLVM_TARGETS**

    LLVM_TARGETS="<OTHERS> <TARGET (i.e. AArch64)>"

Then modify the environment for the package dev-lang/rust. Note, this must be done in the following file, package.env does not get parsed the same way as the following file.

** Note**\
RUST_CROSS_TARGETS: ^[\[1\]](#cite_note-1)^

1.  required llvm target,
2.  [rust target](https://doc.rust-lang.org/nightly/rustc/platform-support.html) (one from rustc \--print target-list)
3.  C target (the one you have installed with crossdev)

[FILE] **`/etc/portage/env/dev-lang/rust`Adding LLVM_TARGETS**

    RUST_CROSS_TARGETS=( "<TARGET A>" "TARGET B" "AArch64:aarch64-unknown-linux-gnu:aarch64-unknown-linux-gnu" )

Now, rebuild rust and llvm with the new configuration.

`root `[`#`]`emerge --ask --deep --update --newuse @world`

Next, install the rust standard library for the target architecture. This is accomplished by first adding it to the cross overlay. then installing it.

`root `[`#`]`cd /var/db/repos/crossdev/cross-<TARGET> `

`root `[`#`]`ln -s /var/db/repos/gentoo/sys-devel/rust-std `

Now unmask it:

[FILE] **`/etc/portage/package.accept_keywords`Adding LLVM_TARGETS**

    cross-<TARGET>/rust-std **

And install it:

`root `[`#`]`emerge --ask cross-<TARGET>/rust-std`

Now cross emerging rust packages should work (provided the packages do not have bugs such as accidental using the host linker)

## [Chroot into the target environment]

-   Create a chroot script

[FILE] **`/usr/local/bin/chroot-armv6j`Example for Raspberry Pi 1 (ARMv6j)**

    /etc/init.d/qemu-binfmt start

    # Next two lines are optional.
    # (Activate if the qemu-wrapper is used. Check that the wrapper location corresponds with the call at the end of line 2!)
    #echo '-1' > /proc/sys/fs/binfmt_misc/arm #deregister wrong arm
    #echo ':arm:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x28\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\x00\xff\xfe\xff\xff\xff:/usr/local/bin/qemu-wrapper:' > /proc/sys/fs/binfmt_misc/register

    cd /usr/armv6j-hardfloat-linux-gnueabi
    mount -t proc none proc
    mount -o bind /dev dev
    mount -o bind /var/db/repos/gentoo var/db/repos/gentoo
    mount -o bind /var/db/repos/localrepo-crossdev var/db/repos/localrepo-crossdev
    mount -o bind /usr/src/raspberrypi-sources usr/src/linux
    mount -o bind /lib/modules lib/modules
    mount -o bind /sys sys
    cp /etc/resolv.conf etc/resolv.conf
    #mount -o bind /tmp tmp
    #mount -o bind /dev/pts dev/pts #only for X

    chroot . /bin/bash --login

    #umount dev/pts
    #umount tmp
    umount sys
    umount lib/modules
    umount usr/src/linux
    umount var/db/repos/localrepo-crossdev
    umount var/db/repos/gentoo
    umount dev
    umount proc

-   To chroot into the new environment, run the script

    :::: cmd-box


    `pi #``chroot-armv6j`


    ::::

    and complete the setup of the build environment.
    -   Create the Portage temporary directory:

    :::: cmd-box


    `root `[`#`]`ln -s /tmp /usr/armv6j-hardfloat-linux-gnueabi/tmp`


    ::::

    -   Update [/etc/locale.gen] and [/etc/env.d/02locale] and run:

    :::: cmd-box


    `root `[`#`]`locale-gen`


    ::::

    -   Check/reload config:

    :::: cmd-box


    `root `[`#`]`gcc-config -l;ldconfig -v;ROOT=/ env-update; source /etc/profile`


    ::::

    -   To run [emerge] inside the chroot, it is required that other config variables are passed to Portage. This can be done with an alias:

    :::: cmd-box


    `root `[`#`]`echo 'alias emerge-chroot="ROOT=/ PKGDIR=$var/cache/binpkgs/ CBUILD=$(portageq envvar CHOST) HOSTCC=$CBUILD-gcc emerge"' > /etc/bash/bashrc.d/emerge-chroot.bash && source /etc/profile`


    ::::

    -   Packages that were unable to cross-compile can now be built with:

    :::: cmd-box


    `root `[`#`]`emerge-chroot --ask --update -v --keep-going @system`


    ::::
-   After installation of the base system, the target environment can be finished according to the standard installation handbook for the architecture used.

## [Known bugs and limitations]

-   On amd64 build hosts, some cross-compiled packages end up in the target environment in [/usr/lib64] even if it is not a 64bit target, so set a symlink:

`root `[`#`]`cd /usr/<TARGET>/usr && ln -s lib lib64`

-   Some packages that create new system users fail ([[[bug #734002]](https://bugs.gentoo.org/show_bug.cgi?id=734002)[]]) to create them in the target environment and create them in build host instead (e.g. [[[net-misc/openssh]](https://packages.gentoo.org/packages/net-misc/openssh)[]]). Create the user manually or emerge the package in the chroot again.
-   If the build host is no-multilib and target environment is multilib and [[[sys-apps/sandbox]](https://packages.gentoo.org/packages/sys-apps/sandbox)[]] fails to compile because of missing 32bit support of the cross compiler:
    -   Temporarily remove the dependency on [[[sys-apps/sandbox]](https://packages.gentoo.org/packages/sys-apps/sandbox)[]] in [[[sys-apps/portage]](https://packages.gentoo.org/packages/sys-apps/portage)[]];
    -   Emerge [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] after that in the chroot environment;
    -   Now it is possible to emerge [[[sys-apps/sandbox]](https://packages.gentoo.org/packages/sys-apps/sandbox)[]] in the chroot.
-   If in an arm64 chroot, emerge fails just after the message `qemu: qemu_thread_create: Invalid argument` is printed to the terminal, add `FEATURES="-pid-sandbox"` to [make.conf].
-   LTO users on the host machine can run into issues with autoconf not being able to check for endianess in programs such as Python so it\'s wise to disable your LTO flags in make.conf while running crossdev.
-   Compiling Musl with LTO has a negative effect in most cases. See ([[[bug #877343]](https://bugs.gentoo.org/show_bug.cgi?id=877343)[]]) for more information.

### [Updating the cross toolchain]

-   After creating the cross toolchain for the first time portage will take over managing updates for toolchain components.
-   There are cases where emerging a new version of a toolchain can fail.
    -   In particular this is known to happen for major version updates of gcc.
        -   If you encounter failures when emerging a cross gcc toolchain e.g. when updating as in `[ebuild  NS   ] cross-x86_64-pc-linux-musl/gcc-12.2.1_p20230121-r1 [11.3.1_p20221209]`
            -   Fix by bootstrapping the toolchain using crossdev as in [#Create the cross toolchain](#Create_the_cross_toolchain).

## [Cross building static binaries for closed systems]

Static binaries are not needed often, but there are some occasions where they are useful:

-   When creating (Docker) container images. According to the [container philosophy](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#run-only-one-process-per-container) it is recommended to run only one process per container. It is also recommended to put as little as possible into a container. In this case one statically linked binary is desirable.
-   When a program will run on a closed system like an ARM device with Android. In the case of Android it is possible to either use the Android\'s NDK and/or its libc implementation \"bionic\" or build a statically linked binary, that depends on no system libs and can run standalone.

### [Cross build toolchain for static binaries]

It is pretty much the same as above beside that it is not needed to emerge a full `@system`. The build essentials are enough.

-   If the target is an Android device, the architecture is probably armv7a or arvm8a, so the tuple `ARCH-VENDOR-OS-LIBC` could be `armv7a-android_hardfloat-linux-gnueabi`
-   Compiling the build essentials for an example Android toolchain could look like:

`android #``armv7a-android_hardfloat-linux-gnueabi-emerge -uva1 --keep-going $(egrep '^[a-z]+' /var/db/repos/gentoo/profiles/default/linux/packages.build) portage`

-   `USE=static-libs` should be switched on after installation of the base system (e.g. if the target program needs [[[dev-libs/openssl]](https://packages.gentoo.org/packages/dev-libs/openssl)[]])

### [Customized glibc]

There are some issues with glibc. This does not affect alternative libcs like µclibc or musl. When using glibc, pay attention to the following.

-   Even when a program was built with `-static`, the resulting binaries aren\'t necessary really static. Because of design decisions of glibc, at least the [/lib/libnss\_\*.so] files are looked up dynamically. To force nss linked statically the flag `--enable-static-nss` can be used for compiling glibc.

<!-- -->

-   When a program is linked statically and makes use of glibc\'s NSS features like `getpwnam()` the lookup of user names fails when [nsswitch.conf] is set to \"compat\". Set it to files in this case:

    ::: box-caption
    [FILE] **`nsswitch.conf`nsswitch.conf for the resulting binaries**
    :::

    :::
        #passwd:      compat
        #shadow:      compat
        #group:       compat

        passwd:      files
        shadow:      files
        group:       files
    :::

<!-- -->

-   The glibc has hard-coded absolute paths for some configuration files like the [/etc/resolv.conf] file. On a closed system (like Android) these files doesn\'t necessarily exist and without them DNS lookups will fail. Normally, the files can\'t be written without root privileges. If becoming root is not an option, glibc must be customized to look at a different location for these files. Keep in mind that this is only necessary if the program makes use of glibc functions which require these files. But virtually every program that connects to the internet uses `gethostbyname` and therefore needs a [resolv.conf].

#### [][(Optional) Create an customized glibc ebuild]

This step is only necessary if the glibc config files don\'t reside in [/etc] and the target program makes use of glibc\'s lookup functions (probably when the program does DNS or username lookups)

1.  Copy the content of the [/var/db/repos/gentoo/sys-libs/glibc] directory to a [local ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository") and create a custom glibc ebuild
2.  Make the following changes:
    1.  Remove the KEYWORDS line (to prevent accidental use in other environments).
    2.  If required, change the path to the config files, by adding to the `src_prepare` section

        ::::: gw-box
        ::: box-caption
        [CODE] **Adding to the glibc ebuild**
        :::

        :::
            # Change the location for config files from /etc to /sdcard/etc (fits to an android environment, because it is writable by users)
            sed -i -e 's:/etc/:/sdcard/etc/:' \
                resolv/ \
                nss/ \
                nis/nss_compat/ \
                sysdeps/ || die
        :::
        :::::

#### [Rebuild a customized glibc]

Rebuild glibc with static options. When the default path was changed in the previous step remember to change `--sysconfdir` here, as appropriate.

`root `[`#`]`EXTRA_ECONF='--enable-static --enable-static-nss --sysconfdir=/etc' <TARGET>-emerge -va1 --keep-going sys-libs/glibc`

### [Build the desired software]

-   Chroot into the target environment (e.g. `chroot-armv7a-android`)
-   If the default path for glibc config files was changed, symlink it `mv -i /sdcard/etc/* /etc && rmdir /sdcard/etc && ln -s /etc /sdcard/etc`
-   Build a statically linked package
    -   An example for Android with [[[net-proxy/privoxy]](https://packages.gentoo.org/packages/net-proxy/privoxy)[]] is:

        :::: cmd-box


        `android #``CFLAGS="$(portageq envvar CFLAGS) -static" CXXFLAGS=$CFLAGS LDFLAGS="$(portageq envvar LDFLAGS) -static" PKGDIR=/tmp/ emerge-chroot privoxy --buildpkgonly -va1`


        ::::
    -   An example for a statically linked [[[www-servers/nginx]](https://packages.gentoo.org/packages/www-servers/nginx)[]] is:

        :::: cmd-box


        `container #``NGINX_MODULES_HTTP="gzip" CFLAGS="$(portageq envvar CFLAGS) -static" CXXFLAGS=$CFLAGS LDFLAGS="$(portageq envvar LDFLAGS) -static" PKGDIR=/tmp/ emerge-chroot -va1 --buildpkgonly nginx:mainline`


        ::::

### [Example: Use a statically linked privoxy on Android]

-   Unzip the binary tarball from above to [/sdcard/] on the Android device (e.g. through the ssh server \"sshelper\" via Google Play or \"ftpserver\" via F-Droid)
    -   Change the Privoxy config `/sdcard/etc/privoxy/config`\'s entries with `/etc/` and `/var/` to `/sdcard/etc` and `/sdcard/var/`.

<!-- -->

-   Put a [resolv.conf] in [/sdcard/etc/] (e.g. with nameservers from www.opennicproject.org or the ad blocking nameservers from www.alternate-dns.com `nameserver 8.8.8.8`)
-   Put a Privoxy startscript in [/sdcard/]

[FILE] **`/sdcard/privoxy.start`**

    # sdcard is mounted non-executable, so copy Privoxy to the homedir of the used app
    # homedir of connectbot (change if a different app is used)
    CB_HOME=/data/data/org.connectbot
    # Copy if nonexistent or newer
    [ /sdcard/usr/sbin/privoxy -nt $CB_HOME/privoxy ] && cat /sdcard/usr/sbin/privoxy > $CB_HOME/privoxy && chmod 755 $CB_HOME/privoxy
    # Run Privoxy in foreground
    $CB_HOME/privoxy --no-daemon /sdcard/etc/privoxy/config

-   Install the Android app \"connectbot\" (available via F-Droid)
    -   Open a local connection named \"privoxy\" and close it again
    -   Hold long the \"privoxy\" connection to open the context menu and choose \"edit host\"
    -   Insert as \"automation\"-task: `sh /sdcard/privoxy.start` (a newline is needed at the end)
    -   To start Privoxy, open the connection in connectbot
-   To browse through Privoxy, add as proxy: localhost/8118 to the mobile data APNs (in the Android control panel at \"mobile networks\" → \"APNs\") and WiFis.

## [See also]

-   [Porting](https://wiki.gentoo.org/wiki/Porting "Porting") --- porting Gentoo to new architectures/platforms/etc\...

## [References]

1.  [[[↑](#cite_ref-1)] [[Gentoo Bugzilla - add cross-compile support](https://bugs.gentoo.org/679878#c7)]]