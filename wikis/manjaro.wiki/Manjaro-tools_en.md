[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Manjaro-tools&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Manjaro-tools "Manjaro-tools (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Manjaro-tools/ru "Manjaro-tools (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Files]](#Files)
-   [[4] [buildset]](#buildset)
-   [[5] [buildpkg]](#buildpkg)
-   [[6] [buildtree]](#buildtree)
-   [[7] [buildiso]](#buildiso)
    -   [[7.1] [Overview]](#Overview)
    -   [[7.2] [Query Building]](#Query_Building)
    -   [[7.3] [Building]](#Building)
    -   [[7.4] [Building with predownloaded Xorg packages]](#Building_with_predownloaded_Xorg_packages)
    -   [[7.5] [Building with a small config change]](#Building_with_a_small_config_change)
        -   [[7.5.1] [Alternative]](#Alternative)
-   [[8] [See Also]](#See_Also)

# [Introduction]

*manjaro-tools* consists of a lot of different tools aimed at Manjaro developers. It is split into 3 different packages:

-   *manjaro-tools-base* contains basic tools, different chroot tools, and *buildset*
-   *manjaro-tools-pkg* contains small helper tools, *buildpkg*, and *buildtree*
-   *manjaro-tools-iso* contains small helper tools and *buildiso*

\
All of these *manjaro-tools* packages are replacements for **devtools** and **manjaroiso**.

A detailed user manual is available at [gitlab](https://gitlab.manjaro.org/tools/development-tools/manjaro-tools).

\

# [Configuration]

manjaro-tools can be configured by copying the folder */etc/manjaro-tools* to your home in *\~/.config* folder and then edit the file *`~/.config/manjaro-tools/manjaro-tools.conf`*

# [Files]

These are the new names for renamed scripts.

-   mkmanjaroroot \--\> mkchroot
-   manjarobuild \--\> buildpkg
-   mkset \--\> buildset
-   pacstrap \--\> basestrap
-   genfstab \--\> fstabgen
-   arch-chroot \--\> manjaro-chroot

\

# [buildset]

buildset is used to create build lists. Build lists can be defined in `/etc/manjaro-tools/sets/<buildlistname>.set`

The help looks like the following:

\

[\$] [buildset -h]\

     Usage: buildset [options]
         -c <name>   Create set
         -r <name>   Remove set
         -s <name>   Show set
         -i          Iso mode
         -q          Query sets
         -h          This help

\

**Note**

------------------------------------------------------------------------

The set name should be different from a directory name in pkgbuilds dir. Anything else should work, eg adding a date to the name.

# [buildpkg]

buildpkg is used to build a particular package or a set. In the following chapter all functions of buildpkg get explained.

If you want a detailed example how to use buildpkg to build packages for a local repository, please look [here](https://wiki.manjaro.org/index.php?title=Buildiso_with_AUR_packages:_Using_buildpkg).

\
The help looks like the following:

\

[\$] [buildpkg -h]\

    Usage: buildpkg [options]
        -a <arch>          Arch [default: x86_64]
        -b <branch>        Branch [default: stable]
        -c                 Recreate chroot
        -h                 This help
        -i            Install a package into the working copy of the chroot
        -n                 Install and run namcap check
        -p            Build list or pkg [default: default]
        -q                 Query settings and pretend build
        -r <dir>           Chroots directory
                           [default: /var/lib/manjaro-tools/buildpkg]
        -s                 Sign packages
        -w                 Clean up cache and sources

\
To build a single package, go into the directory which is one above the package build directory (which contains the PKGBUILD), and run it as:

[user \$ ][ buildpkg -p package-name [COPY TO CLIPBOARD]]

\

To build a set the name of the set can be used. The current sets can be queried with the `-q` option.

# [buildtree]

buildtree is a little tools to sync arch abs and manjaro packages git repos.

The arguments are:

\

[\$] [buildtree -h]\

     Usage: buildtree [options]
         -s            Sync manjaro tree
         -a            Sync arch abs
         -c            Clean package tree
         -q            Query settings
         -h            This help[/code]

\
To sync Arch and Manjaro trees:

[user \$ ][ buildtree -as [COPY TO CLIPBOARD]]

\

# [buildiso]

buildiso is used to build a particular ISO or a set of ISOs. All functions of buildiso will be explained in the following chapters.

If you want a detailed guide how to use buildiso to build your own Manjaro ISOs from scratch, please look [here](https://wiki.manjaro.org/index.php?title=Build_Manjaro_ISOs_with_buildiso).

\

## [Overview]

The help looks like the following for x86_64:

\

[\$] [buildiso -h]\

     Usage: buildiso [options]
         -p        Buildset or profile [default: default]
         -a <arch>          Arch [default: x86_64]
         -b <branch>        Branch [default: stable]
         -r <dir>           Chroots directory
                            [default: /var/lib/manjaro-tools/buildiso]
         -c                 Disable clean work dir
         -x                 Clean xorg cache
         -l                 Clean lng cache
         -i                 Build images only
         -s                 Generate iso only
                            Requires pre built images (-i)
         -v                 Verbose output, show profies detail (-q)
         -q                 Query settings and pretend build
         -h                 This help

\

## [Query Building]

To query build an ISO (**-q** option), for example the xfce-openbox-openrc profile, the following command can be used:

\

[\$] [buildiso -p xfce -qv]\

    ==> manjaro-tools
      -> version: 0.15.9
      -> config: ~/.config/manjaro-tools/manjaro-tools.conf
    ==> PROFILE:
      -> build_lists: community|default|manjaro|sonar|v17-release
      -> build_list_iso: xfce
      -> is_build_list: false
    ==> OPTIONS:
      -> arch: x86_64
      -> branch: unstable
      -> kernel: linux419
    ==> ARGS:
      -> clean_first: true
      -> images_only: false
      -> iso_only: false
      -> persist: false
    ==> DIST SETTINGS:
      -> dist_name: Manjaro
      -> dist_release: 18.0
      -> dist_codename: Illyria
    ==> ISO INFO:
      -> iso_label: MJRO180
      -> iso_compression: xz
    ==> BUILD QUEUE:
     --> Profile: [xfce]
      -> iso_file: manjaro-xfce-18.0-unstable-minimal-x86_64.iso
      -> autologin: true
      -> nonfree_mhwd: true
      -> multilib: true
      -> extra: false
      -> netinstall: false
      -> chrootcfg: false
      -> geoip: true
      -> efi_boot_loader: grub
      -> hostname: manjaro
      -> username: manjaro
      -> password: manjaro
      -> login_shell: /bin/bash
      -> addgroups: lp,network,power,sys,wheel
      -> enable_systemd: avahi-daemon bluetooth cronie ModemManager NetworkManager org.cups.cupsd tlp tlp-sleep ufw lightdm
      -> enable_systemd_live: manjaro-live mhwd-live pacman-init mirrors-live
      -> disable_systemd: pacman-init

\

## [Building]

To actually build the ISO:

[user \$ ][ buildiso -p xfce -b stable [COPY TO CLIPBOARD]]

\

## [Building with predownloaded Xorg packages]

To build an ISO while retaining the previously downloaded cache of Xorg packages, the **-x** option can be used:

[user \$ ][ buildiso -p xfce-openbox-openrc/ -b stable -x [COPY TO CLIPBOARD]]

\

## [Building with a small config change]

**Note**

------------------------------------------------------------------------

It is to be verified if the procedure given below works or not.

Supposing something only changed in config, like a setting, instead of building the whole ISO from scratch, the ISO build directory can be modified and the ISO can be rebuilt. For example, supposing one changed *xfce-overlay/etc/skel/.conkyrc* in the config, one can go into the work directory, modify the said file, and rebuild the ISO using the **-cs** option.

The work directory can be found using the **-h** option:

\

[\$] [buildiso -h]\

     Usage: buildiso [options]
         -p        Buildset or profile [default: default]
         -a <arch>          Arch [default: x86_64]
         -b <branch>        Branch [default: unstable]
         -r <dir>           Chroots directory
                            [default: '''/var/lib/manjaro-tools/buildiso''']
         -t <dir>           Target directory
                            [default: /home/fh/Data/build/iso]
         -k <name>          Kernel to use
                            [default: linux419]
         -g <key>           The gpg key for sfs signing
                            [default: ]
         -m                 Set SquashFS image mode to persistence
         -c                 Disable clean work dir
         -f                 Build full ISO (extra=true)
         -d <comp>          Compression used for build ISO: xz, gzip, lzma, lzo, lz4
                            [default: xz]
         -x                 Build images only
         -z                 Generate iso only
                            Requires pre built images (-x)
         -v                 Verbose output to log file, show profile detail (-q)
         -q                 Query settings and pretend build
         -h                 This help

\

        -r <dir>           Chroots directory
                           [default: /var/lib/manjaro-tools/buildiso]

(work directory highlighted in bold)

The required file can be edited as root, for example:

[user \$ ][ sudo nano /var/lib/manjaro-tools/buildiso/xfce/x86_64/desktopfs/etc/skel/.conkyrc [COPY TO CLIPBOARD]]

\

There is a catch involved here though; the file one wants to edit may be present in multiple images, like rootfs, livefs, desktopfs), and would need to be edited in the respective image directories.

\
Then the ISO then can be rebuilt as:

[user \$ ][ buildiso -p xfce -cs [COPY TO CLIPBOARD]]

\

### [Alternative]

First only the chroot for the ISO could be created, using the `-i` option, then the changes can be made, and finally an ISO can be built with the `-sc` option.

For example:

\

[\$] [buildiso -p xfce -b stable -x]\

    ==> Start building [xfce]
    ==> Cleaning up ...
      -> Deleting chroot [rootfs] (x86_64) ...
      -> Deleting isoroot [iso] ...
    [..]

\
After this the changes in the work directory can be made, and the ISO can be generated with:

[user \$ ][ buildiso -p xfce/ -cz [COPY TO CLIPBOARD]]

\

# [See Also]

-   [Manjaro Gitlab](https://gitlab.manjaro.org/tools/development-tools/manjaro-tools)
-   [Build Manjaro ISOs with buildiso](//wiki.manjaro.org/index.php?title=Build_Manjaro_ISOs_with_buildiso "Build Manjaro ISOs with buildiso")