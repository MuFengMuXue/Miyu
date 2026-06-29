This guide is intended for those that wish to **build [musl](https://wiki.gentoo.org/wiki/Musl "Musl") stages** on architectures that don\'t have them built by the official Gentoo build server.

Throughout the guide it will be showing the process to build for a MIPS64 target but this can be replaced with the tuple required for that machine.

## Contents

-   [[1] [Create Musl stage 3 files]](#Create_Musl_stage_3_files)
    -   [[1.1] [Crossdev]](#Crossdev)
    -   [[1.2] [Building a stage file]](#Building_a_stage_file)
        -   [[1.2.1] [Set the system profile]](#Set_the_system_profile)
        -   [[1.2.2] [Fixes]](#Fixes)
        -   [[1.2.3] [Emerge the system]](#Emerge_the_system)
        -   [[1.2.4] [Stage file creation]](#Stage_file_creation)
    -   [[1.3] [QEMU user mode]](#QEMU_user_mode)
    -   [[1.4] [Test stage]](#Test_stage)
        -   [[1.4.1] [make.conf]](#make.conf)
        -   [[1.4.2] [Emerge sync]](#Emerge_sync)
        -   [[1.4.3] [Rebuild world]](#Rebuild_world)
    -   [[1.5] [Catalyst]](#Catalyst)
        -   [[1.5.1] [Configure the build]](#Configure_the_build)
        -   [[1.5.2] [Start the build]](#Start_the_build)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Auto-resume]](#Auto-resume)
    -   [[2.2] [MIPS 2GB limit]](#MIPS_2GB_limit)
    -   [[2.3] [qemu: qemu_thread_create: Invalid argument]](#qemu:_qemu_thread_create:_Invalid_argument)
    -   [[2.4] [CHOST changing part way through the build]](#CHOST_changing_part_way_through_the_build)
-   [[3] [See also]](#See_also)

## [Create Musl stage 3 files]

### [Crossdev]

Install [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]] to allow building of MIPS environment:

`root `[`#`]`emerge --ask sys-devel/crossdev`

Now, create the cross compiler:

`root `[`#`]`crossdev --stage4 --target mips64-unknown-linux-musl`

If no errors were reported, move on to the next section.

### [Building a stage file]

#### [Set the system profile]

For this example, the target machine is using profile 18:

`root `[`#`]`PORTAGE_CONFIGROOT=/usr/mips64-unknown-linux-musl eselect profile list`

      [1]   default/linux/mips/17.0/o32 (exp)
      [2]   default/linux/mips/17.0/n32 (exp)
      [3]   default/linux/mips/17.0/n64 (exp)
      [4]   default/linux/mips/17.0/multilib/o32 (exp)
      [5]   default/linux/mips/17.0/multilib/n32 (exp)
      [6]   default/linux/mips/17.0/multilib/n64 (exp)
      [7]   default/linux/mips/17.0/mipsel/o32 (exp)
      [8]   default/linux/mips/17.0/mipsel/n32 (exp)
      [9]   default/linux/mips/17.0/mipsel/n64 (exp)
      [10]  default/linux/mips/17.0/mipsel/n64/systemd (exp)
      [11]  default/linux/mips/17.0/mipsel/n64/systemd/merged-usr (exp)
      [12]  default/linux/mips/17.0/mipsel/multilib/o32 (exp)
      [13]  default/linux/mips/17.0/mipsel/multilib/n32 (exp)
      [14]  default/linux/mips/17.0/mipsel/multilib/n64 (exp)
      [15]  default/linux/mips/17.0/mipsel/multilib/n64/systemd (exp)
      [16]  default/linux/mips/17.0/mipsel/multilib/n64/systemd/merged-usr (exp)
      [17]  default/linux/mips/17.0/musl/o32 (exp)
      [18]  default/linux/mips/17.0/musl/n64 (exp)
      [19]  default/linux/mips/17.0/musl/mipsel/o32 (exp)
      [20]  default/linux/mips/17.0/musl/mipsel/n64 (exp)

Because of the experimental flag, profile 18 in this example must be set with the `--force` flag.

`root `[`#`]`PORTAGE_CONFIGROOT=/usr/mips64-unknown-linux-musl eselect profile set --force 18`

#### [Fixes]

To stop errors, the following `USE` flags and unmask need to be set:

`root `[`#`]`mkdir /usr/mips64-unknown-linux-musl/etc/portage/package.use `

[FILE] **`/usr/mips64-unknown-linux-musl/etc/portage/package.use/system`**

    sys-apps/util-linux -su

#### [Emerge the system]

`root `[`#`]`mips64-unknown-linux-musl-emerge -va1 @system --keep-going`

#### [Stage file creation]

Create a tar.xz of the system files created ready for use later on.

`root `[`#`]`cd /usr/mips64-unknown-musl/ `

`root `[`#`]`tar -cvJf /home/USER/mips64-musl-seed.tar.xz * `

Change the [/home/USER] part to wherever is a suitable location to store this stage file.

### [QEMU user mode]

Use the guide located at [Embedded Handbook/General/Compiling with Buildingemu user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot")

### [Test stage]

This is the time to confirm the stage can rebuild itself to look for early issue, begin by chrooting into the system created setup earlier.

Unpack the stage file into a new directory.

`root `[`#`]`cd /home/user/chroot/mips64-seed `

`root `[`#`]`tar xvf mips64-musl-seed.tar.xz `

Mount the required directories:

`root `[`#`]`mount --types proc none proc `

`root `[`#`]`mount --rbind /dev dev `

`root `[`#`]`mount --rbind /sys sys `

`root `[`#`]`mount --bind /run run `

Copy the resolv.conf so that DNS will work in the chroot:

`root `[`#`]`cp /etc/resolv.conf etc/ `

It\'s now possible to load the qemu binary we built in the previous section to allow chrooting in.

`root `[`#`]`ROOT=$PWD/ emerge --usepkgonly --oneshot --nodeps qemu`

Chroot in:

`root `[`#`]`chroot . /bin/bash --login`

Assuming everything was setup correctly previously then this will allow a working chroot on a different architecture. If this is no the case then return to the previous section and retrace the steps to fix what was missed.

#### [make.conf]

The make.conf will still have crossdev settings applied to it so this needs to be changed to a more standard version as shown below.

[FILE] **`/etc/portage/make.conf`make.conf example**

    COMMON_FLAGS="-Os -march=mips3"
    CFLAGS="$"
    CXXFLAGS="$"
    FCFLAGS="$"
    FFLAGS="$"

    CHOST="mips-unknown-linux-musl"

    LC_MESSAGES=C

Qemu chroot also need some sandbox features disabled, so add these to the make.conf also:

[FILE] **`/etc/portage/make.conf`make.conf example**

    FEATURES="-pid-sandbox -network-sandbox"

#### [Emerge sync]

Run an [emerge \--sync]:

`chroot #``emerge --sync`

#### [Rebuild world]

`chroot #``emerge -e @world --keep-going`

Once this stage is completed then a user can be sure it will work with catalyst so can move on to the next section.

### [Catalyst]

Install catalyst:

`root `[`#`]`emerge --ask catalyst`

#### [Configure the build]

First, create some directories to work in:

`root `[`#`]`mkdir -p /var/tmp/catalyst/builds`

Then, move the seed stage:

`root `[`#`]`mv /home/USER/mips64-musl-seed.tar.xz /var/tmp/catalyst/builds/`

Next, build a portage snapshot:

`root `[`#`]`emerge --sync`

`root `[`#`]`catalyst -s $(date +%Y.%m.%d)`

Next, create the spec files

`root `[`#`]`cd /var/tmp/catalyst`

[FILE] **`stage1-mips64-musl-n64-openrc.spec`**

    subarch: mips64_n64
    target: stage1
    version_stamp: musl-openrc-20221019
    interpreter: /usr/bin/qemu-mips64
    rel_type: default
    profile: default/linux/mips/17.0/musl/n64
    snapshot: 2022.10.19
    source_subpath: mips64-musl-seed
    compression_mode: pixz
    decompressor_search_order: xz bzip2
    update_seed: yes
    update_seed_command: -uDN @world

[FILE] **`stage3-mips64-musl-n64-openrc.spec`**

    subarch: mips64_n64
    target: stage3
    version_stamp: openrc-2022-10-19
    interpreter: /usr/bin/qemu-mips64
    rel_type: default
    profile: default/linux/mips/17.0/musl/n64
    snapshot: 2022.10.19
    source_subpath: default/stage1-mips64_n64-openrc-20221019
    compression_mode: pixz
    decompressor_search_order: xz bzip2

#### [Start the build]

Finally, build the stage:

`root `[`#`]`catalyst -f stage1-mips64-musl-n64-openrc.spec`

`root `[`#`]`catalyst -f stage3-mips64-musl-n64-openrc.spec`

If this builds without error, then the stage 3 file is found at [/var/tmp/catalyst/builds/default]

## [Troubleshooting]

Some hints to push past some issues which can be encountered.

#### [Auto-resume]

The auto-resume function in Catalyst can be a blessing and a curse so removing the line `autoresume` from `options` in [/etc/catalyst/catalyst.conf] can allow to start from a fresh slate at the cost of undoing all previous progress.

#### [MIPS 2GB limit]

When building for a 32bit MIPS environment in QEMU user mode, there is hard limit of 2GB RAM usage. Removing `-pipe` from the build environment\'s [make.conf] will allow big programs like GCC to build.

#### [qemu: qemu_thread_create: Invalid argument]

Add `FEATURES="-pid-sandbox"` to the chroot build environment\'s make.conf.

#### [CHOST changing part way through the build]

The CHOST can be forced inside the spec file by setting something like `chost: mipsel-unknown-linux-musl` if it changed earlier in the build.

## [See also]

-   [Project:RelEng](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng") --- the official Gentoo project focused on coordinating and improving the creation of official media releases of Gentoo Linux and other Gentoo operating systems.
-   [Project:Catalyst/FAQ](https://wiki.gentoo.org/wiki/Project:Catalyst/FAQ "Project:Catalyst/FAQ") --- contains frequently asked questions (FAQs) relating to the Catalyst tool.
-   [Stage file](https://wiki.gentoo.org/wiki/Stage_file "Stage file") --- an archive that contains all the files to run a minimal Gentoo environment, typically to serve as a seed for a Gentoo installation
-   [Catalyst](https://wiki.gentoo.org/wiki/Catalyst "Catalyst") --- a tool to build [stage files](https://wiki.gentoo.org/wiki/Stage_file "Stage file") and [live-images](https://wiki.gentoo.org/wiki/Live_image "Live image") for Gentoo