**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Catalyst "Project:Catalyst")][Project](https://wiki.gentoo.org/wiki/Project:Catalyst "Project:Catalyst")

[[]][Package information](https://packages.gentoo.org/packages/dev-util/catalyst)

[[]][GitWeb](https://gitweb.gentoo.org/proj/catalyst.git)

*Not to be confused with [AMD Catalyst, the old ATi graphics driver](https://wiki.gentoo.org/wiki/Fglrx "Fglrx").*

**catalyst** is a tool to build [stage files](https://wiki.gentoo.org/wiki/Stage_file "Stage file") and [live-images](https://wiki.gentoo.org/wiki/Live_image "Live image") for Gentoo. [catalyst] allows the creation of made-to-measure Gentoo installation files and is used [internally](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng") to build [official Gentoo Linux releases](https://get.gentoo.org).

[catalyst] can be used to:

-   Build [stage files](https://wiki.gentoo.org/wiki/Stage_file "Stage file")
-   Build bootable [live images](https://wiki.gentoo.org/wiki/Live_image "Live image")
-   Build netboot images
-   Cross-compile for any of the architectures supported by Gentoo Linux

\
Designed with situations when more advanced features are required in mind, [catalyst] makes a powerful and versatile tool. It can be used to save time setting up systems, for example, a user wanting to install the testing branch, could use catalyst to create a stage 3 file for that branch, with any optimizations they might require (e.g. [LTO](https://wiki.gentoo.org/wiki/LTO "LTO")). Another use-case could be to create a stage 3 file for an \"exotic\" system that Gentoo Linux supports but does not release official images for (e.g. a [musl](https://wiki.gentoo.org/wiki/Musl "Musl") stage 3 file for the [m68k](https://en.wikipedia.org/wiki/Motorola_68000_series "wikipedia:Motorola 68000 series") architecture which has a very low number of users even on the standard Gentoo Linux version).

\

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Update]](#Update)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
        -   [[2.1.1] [catalyst.conf file option list]](#catalyst.conf_file_option_list)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Seed file]](#Seed_file)
    -   [[3.2] [Snapshot]](#Snapshot)
        -   [[3.2.1] [Local generation]](#Local_generation)
        -   [[3.2.2] [Older snapshots and manually downloading]](#Older_snapshots_and_manually_downloading)
    -   [[3.3] [Spec files]](#Spec_files)
    -   [[3.4] [Obtaining the spec files]](#Obtaining_the_spec_files)
        -   [[3.4.1] [Inside a stage1.spec file]](#Inside_a_stage1.spec_file)
        -   [[3.4.2] [.spec file option list]](#.spec_file_option_list)
        -   [[3.4.3] [Portage config]](#Portage_config)
        -   [[3.4.4] [Cross Compiling]](#Cross_Compiling)
        -   [[3.4.5] [Custom profiles]](#Custom_profiles)
    -   [[3.5] [Invocation]](#Invocation)
    -   [[3.6] [Building stages]](#Building_stages)
        -   [[3.6.1] [Distfiles directory]](#Distfiles_directory)
        -   [[3.6.2] [Binpkgs directory]](#Binpkgs_directory)
        -   [[3.6.3] [Autoresume]](#Autoresume)
        -   [[3.6.4] [Jobs and load average]](#Jobs_and_load_average)
        -   [[3.6.5] [Start the build]](#Start_the_build)
-   [[4] [Detailed usage examples]](#Detailed_usage_examples)
    -   [[4.1] [Convert QEMU specs to native]](#Convert_QEMU_specs_to_native)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [dev-util/catalyst](https://packages.gentoo.org/packages/dev-util/catalyst) [[]] [Release metatool used for creating releases based on Gentoo Linux]

  ------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`+iso`](https://packages.gentoo.org/useflags/+iso)     Pulls in the depends for building iso images
  [`doc`](https://packages.gentoo.org/useflags/doc)       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`qcow2`](https://packages.gentoo.org/useflags/qcow2)   Pulls in the depends for building qcow2 images
  ------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-06 19:05] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

As [[[dev-util/catalyst]](https://packages.gentoo.org/packages/dev-util/catalyst)[]] is an internal project mostly used for Gentoo needs, RelEng uses [catalyst] built directly from [Git](https://wiki.gentoo.org/wiki/Git "Git").

** Important**\
This is the exception to the rule and not something users should be doing for other packages without good reasons. See [Live ebuilds](https://wiki.gentoo.org/wiki/Live_ebuilds "Live ebuilds") for more information.

[FILE] **`/etc/portage/package.accept_keywords/catalyst`package.accept_keyword/catalyst**

    dev-util/catalyst **

To install [catalyst] run:

`root `[`#`]`emerge --ask dev-util/catalyst`

### [Update]

To update [catalyst], [[[app-portage/smart-live-rebuild]](https://packages.gentoo.org/packages/app-portage/smart-live-rebuild)[]] should be used.

See [Live ebuilds - smart-live-rebuilds](https://wiki.gentoo.org/wiki/Live_ebuilds#Smart_live_rebuild "Live ebuilds")

## [Configuration]

### [Files]

After emerging [catalyst], the first (and probably only) configuration step is to edit [catalyst.conf].

[/etc/catalyst/catalyst.conf]

[/etc/catalyst/catalystrc]

#### [catalyst.conf file option list]

The following table provides a list of [catalyst.conf] file options and their descriptions.

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `digests`              | Creates a .DIGESTS file containing the hash output from each of the selected hashes. Example: `digests = ["blake2b", "sha512"]`                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   | :::::                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                   | ** Note**\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                   | To see the list of the hashes supported by the system, run:                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   | :::: cmd-box                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   | `user `[`$`]`$ python3 -c 'import hashlib; print(hashlib.algorithms_available)'`                                                                                                                                                                                                                                                                                             |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                   | ::::                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   | :::::                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `envscript`            | Environment script sourced by [catalyst] at runtime. Example: `envscript = "/etc/catalyst/catalystrc"`. For more details about this option, please check [Files](https://wiki.gentoo.org/wiki/Catalyst#Files "Catalyst") section above.                                                                                                                                                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `options`              | `options` sets the below listed build-time options for catalyst. Example: `options = ["ccache", "keepwork"]`                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | Item                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | `"autoresume"`         | Attempt to resume a failed build. Autoresume points can be cleared from [[catalyst] command line](https://wiki.gentoo.org/wiki/Catalyst#Invocation "Catalyst") using one of the following parameters:                                                                                                                                                                                      |        |
|                                   | |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |        |
|                                   | |                                   | -   -a(\--clear-autoresume) - just clears autoresume flags                                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                   | |                                   | -   -p(\--purge) - clears autoresume flags as well as your [pkgcache] and [kerncache]                                                                                                                                                                                                                           |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | `"bindist"`            | Enables the `bindist` USE flag. The definition of this flag is package specific, please check for each package separately. However, it is suggested to enable this if resulting build is to be redistributed. This optional USE flag is normally cleaned from the [make.conf] file on completion of the stage. For a non-cleaned version, use also `"sticky-config"` option (see below) |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | `"ccache"`             | Enables [`FEATURES`](https://wiki.gentoo.org/wiki/FEATURES "FEATURES")`=ccache` i.e. compiler cache support. See [man 5 make.conf] for details.                                                                                                                                                                                                                                            |        |
|                                   | |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |        |
|                                   | |                                   | :::                                                                                                                                                                                                                                                                                                                                                                                                      |        |
|                                   | |                                   | ** Warning**\                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |        |
|                                   | |                                   | `ccache` has been known to cause random build failures and bugs reported with `ccache` enabled may be ignored.                                                                                                                                                                                                                                                                                                                                                                        |        |
|                                   | |                                   | :::                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | `"distcc"`             | Enables `FEATURES=`[`distcc`](https://wiki.gentoo.org/wiki/Distcc "Distcc") i.e. tool to distribute compiling tasks across a network of participating hosts. See [man 5 make.conf] for details.                                                                                                                                                                                            |        |
|                                   | |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |        |
|                                   | |                                   | :::                                                                                                                                                                                                                                                                                                                                                                                                     |        |
|                                   | |                                   | ** Important**\                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |        |
|                                   | |                                   | This option requires [`distcc_hosts`](https://wiki.gentoo.org/wiki/Catalyst#.spec_file_option_list "Catalyst") to be set too.                                                                                                                                                                                                                                                                                                                                                         |        |
|                                   | |                                   | :::                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | `"icecream"`           | Enables `FEATURES=icecream` i.e. icecream tool, a distributed compiler with a central scheduler to share build load.                                                                                                                                                                                                                                                                                                                                                                  |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | `"keepwork"`           | Prevents the removal of the working chroot path and any autoresume files or points.                                                                                                                                                                                                                                                                                                                                                                                                   |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | `"kerncache"`          | Keeps a tbz2 file of your built kernel and modules (useful if the build stops in livecd-stage2)                                                                                                                                                                                                                                                                                                                                                                                       |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | `"pkgcache"`           | Build and use binary packages                                                                                                                                                                                                                                                                                                                                                                                                                                                         |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | `"seedcache"`          | Use the build output of a previous target if it exists rather than the tarball                                                                                                                                                                                                                                                                                                                                                                                                        |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
|                                   | | `"sticky-config"`      | Enables the code that will keep any internal \'catalyst_use\' flags added to the USE= for building the stage. These are usually added for legal or specific needs in building the the early stage. Mostly it is the \'bindist\' USE flag option that is used for legal reasons, please see its specific definition. It will also keep any [/etc/portage/package.\*] files or directories.          |        |
|                                   | +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+        |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `port_logdir`          | This directory is where all build logs will be kept; it is automatically cleaned of ALL files over 7 days old. If left undefined the logs will remain in the build directory and get cleaned every time a stage build is restarted. Example: `port_logdir = "/var/tmp/catalyst/logs"`                                                                                                                                                                                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `var_tmpfs_portage`    | This will mount a tmpfs for [/var/tmp/portage] so building takes place in RAM this feature requires a pretty large tmpfs (office needs \~8 GiB to build) WARNING: If you use too much RAM everything will fail horribly and it\'s not going to be our fault. Sets size of [/var/tmp/portage tmpfs] in gigabytes. Example: `var_tmpfs_portage = 16` |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `jobs`                 | Integral value passed to emerge as the parameter to \--jobs and is used to define MAKEOPTS during the target build. Example: `jobs = 4`                                                                                                                                                                                                                                                                                                                                                                                              |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `load-average`         | Floating-point value passed to emerge as the parameter to \--load-average and is used to define MAKEOPTS during the target build. Example: `load-average = 4.0`                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `jobserver-fifo`       | Path to a GNU Make FIFO jobserver, like [Steve](https://wiki.gentoo.org/wiki/Steve "Steve"). Example: `jobserver-fifo = "/dev/steve"/code> `                                                                                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `binhost`              | If you want catalyst to drop a binrepos.conf into [/etc/portage], then define the binhost here. This value is concatenated with the configuration option binrepo_path in the spec file to obtain the src-uri. Example: `binhost = "`[`https://gentoo.osuosl.org/releases/`](https://gentoo.osuosl.org/releases/)`"`                                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## [Usage]

This section is for general reference to explain how [catalyst] is used, to learn how to complete particular tasks see [Detailed usage examples](https://wiki.gentoo.org/wiki/Catalyst#Detailed_usage_examples "Catalyst") section.

### [Seed file]

For creating a stage 3 file a seed file is needed. [catalyst] will [chroot] into the unpacked seed file\'s environment and [emerge] the packages needed for the new stage inside of the [chroot] environment. This way the packages built for new stage file are isolated from the packages on the host system.

Unless the temporary directory location was modified in the [catalyst] configuration, seed stage files should be placed in the following path:

`root `[`#`]`mkdir -p /var/tmp/catalyst/builds/default`

** Important**\
If the temporary directory was modified, put your seed files in the appropriate location, for details see the [configuration section](https://wiki.gentoo.org/wiki/Catalyst#Configuration "Catalyst") above.

Any working stage 3 file can be used as the seed, however it is recommended to use current stage 3 files downloaded from one of the official Gentoo Linux mirrors.

Relatively recent **[amd64]** OpenRC stage files can be found [here](https://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64-openrc/), and their **[x86]** equivalents can be found [here](https://distfiles.gentoo.org/releases/x86/autobuilds/current-stage3-i686-openrc/).

[wget] can be used to download those files from the command line. For example, to download **[amd64]** stage file:

`root `[`#`]`wget https://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64/stage3-openrc-amd64-YYYYMMDDTHHMMSSZ.tar.xz -O /var/tmp/catalyst/builds/default/stage3-amd64-openrc-latest.tar.xz`

### [Snapshot]

#### [Local generation]

From version 4 [catalyst] uses git to clone the current ::gentoo repo and compresses it as a squash file.

The snapshot will be saved to [/var/tmp/catalyst/snapshots/gentoo-\<COMMIT\>.sqfs]

Generally, users would only ever want to use the current repo snapshot, so `--snapshot stable` is all that is needed to be remembered.

`root `[`#`]`catalyst --snapshot stable`

This will create a squash file file with the commit reference name like `17e0dbd98931319735970cdb917f7f8b88f647ed`, take note of this as it is required when editing spec files.

#### [Older snapshots and manually downloading]

Another option is to use one of the ::gentoo squash file repository snapshots available on the mirrors. Current snapshots can be found [here](https://distfiles.gentoo.org/snapshots/squashfs/).

For example, to download a remote snapshot hosted on a HTTP(S) server using [wget]:

`root `[`#`]`wget `[`https://distfiles.gentoo.org/snapshots/squashfs/gentoo-current.xz.sqfs`](https://distfiles.gentoo.org/snapshots/squashfs/gentoo-current.xz.sqfs)

### [Spec files]

*Spec files* define parameters which Catalyst uses to create *stage files* and *boot media*.

** Note**\
A separate *spec file* is needed for each stage. Building a stage 3 requires that the associated stage 1 is built first.

The *spec files* maintained by the Gentoo [Release Engineering](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng") team can be found in the [RelEng git repository](https://gitweb.gentoo.org/proj/releng.git/tree/releases/specs).

The rest of this section will explain how to edit and repurpose a standard (OpenRC-based) **[amd64]** stage 3 file using the spec files provided by RelEng team.

### [Obtaining the spec files]

Spec files can be downloaded with [wget] as follows. OpenRC example:

`root `[`#`]`wget -O stage1.spec "https://gitweb.gentoo.org/proj/releng.git/plain/releases/specs/amd64/stage1-openrc-23.spec" `

`root `[`#`]`wget -O stage3.spec "https://gitweb.gentoo.org/proj/releng.git/plain/releases/specs/amd64/stage3-openrc-23.spec" `

#### [Inside a stage1.spec file]

** Important**\
*Spec files* provided by RelEng contain information wrapped in *@\'*s which must be replaced with the relevant information before being used.

Generally only four parts need to be changed:

-   *version_stamp*
-   *snapshot_treeish*
-   *source_subpath*
-   *portage_confdir*

Here is a quick overview of how a modified spec file should look like for a user:

[FILE] **`stage1.spec`amd64 stage1 spec file from RelEng**

    subarch: amd64
    target: stage1
    version_stamp: openrc-@TIMESTAMP@
    rel_type: 23.0-default
    profile: default/linux/amd64/23.0
    snapshot_treeish: @TREEISH@
    source_subpath: 23.0-default/stage3-amd64-openrc-latest
    compression_mode: pixz
    update_seed: yes
    update_seed_command: --update --deep --newuse @world
    portage_confdir: @REPO_DIR@/releases/portage/stages
    portage_prefix: releng

[FILE] **`stage1.spec`amd64 stage1 spec file modified for use with a specific snapshot and version.**

    subarch: amd64
    target: stage1
    version_stamp: openrc-2024.07.02
    rel_type: 23.0-default
    profile: default/linux/amd64/23.0
    snapshot_treeish: e7b9afdd137f25a545a1f56ce1ca4c1d7be16160
    source_subpath: 23.0-default/stage3-amd64-openrc-latest
    compression_mode: pixz
    update_seed: yes
    update_seed_command: --update --deep --newuse @world
    portage_confdir: /var/tmp/catalyst/releng/releases/portage/stages
    portage_prefix: releng

#### [.spec file option list]

The following table provides a list of [.spec] file options and their descriptions.

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `subarch`              | Sets the `CHOST` and `CFLAGS`/`CXXFLAGS` for the system. Finer tuning can be achieved by looking in the architecture specific [.toml] files located in [/usr/share/catalyst/arch].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `target`               | Specifies what target Catalyst will build. The example above specifies `stage1` as the target to be built. For building a CD, `livecd-stage1` should be defined as the target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `version_stamp`        | An identifier for the build. On the autobuilds the date is used, however it can be anything the user desires. This parameter will be used on the output stage file, (`$`-`$`-`$`.tar.bz2), temporary directories, etc.\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   | \                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   | `@TIMESTAMP@` can be quickly replaced using:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   | ::::: cmd-box                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   | `user `[`$`]`TIMESTAMP=$(date -u +%Y%m%dT%H%M%SZ) `                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   | `user `[`$`]`sed -i -e "s:@TIMESTAMP@:$:g" stage1.spec `                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                   | :::::                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rel_type`             | Defines what kind of build the system will perform. This is merely another identifier that is available to be used in case (more) differentiation of the builds is needed. If a normal, hardened, and musl stages were to be built these could be defined here. Changing it will change the sub-directory inside [/var/tmp/catalyst/builds] from default to whatever has been set for this value.                                                                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `profile`              | The system profile to be used by Catalyst to build this target. It is specified as a relative path and *must be set* to one of the system profiles available at [/usr/portage/profiles]. In the example above the default profile is used (`default/linux/amd64/23.0`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `snapshot_treeish`     | Specifies which snapshot of main Gentoo repository. See the [section above](https://wiki.gentoo.org/wiki/Catalyst#snapshot "Catalyst") on creating a snapshot for more information on snapshots. If 17e0dbd98931319735970cdb917f7f8b88f647ed is used like in the example above, [catalyst] will look for a snapshot available at [/var/tmp/catalyst/snapshots/gentoo-17e0dbd98931319735970cdb917f7f8b88f647ed.sqfs].                                                                                                                                                                                                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `source_subpath`       | A relative path to the seed stage for this target. In the example above, it will use [/var/tmp/catalyst/builds/default/stage3-amd64-latest.tar.xz] as the seed stage. The prefix of this filesystem path ([/var/tmp/catalyst/builds]) is determined by the value contained in the `storedir` variable the [/etc/catalyst/catalyst.conf] file. The suffix ([.tar.bz2]) is automatically generated by [catalyst] at build time. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `distcc_hosts`         | The hosts used as [distcc] slaves when [distcc] is enabled in the [/etc/catalyst/catalyst.conf] file. It follows the same syntax as [distcc-config \--set-hosts] and is entirely optional. This setting is lacking from the example above and generally recommended not to be used.                                                                                                                                                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `portage_confdir`      | An absolute path to a custom Portage configuration directory. This can be used to include unstable (`~`) packages, or a specific [make.conf]. If this line is left out of the [.spec] file, Catalyst will use its default configuration. If this line *is* defined make sure it is defined across *all* targets ([.spec] files) to minimize problems. It is recommended to use the defaults set by RelEng and edit to the desired needs.                                                                                                                                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `repos`                | The location of a Portage overlay to use when building the target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `keep_repos`           | Same as above, however keeps the custom repo enabled in target system permanently.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pkgcache_path`        | An optional directory containing the output packages for [catalyst]. Mainly used as a way for different [.spec] files to access the same cache directory. By default, this location will be auto-generated by [catalyst] based on the [.spec] file.                                                                                                                                                                                                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `kerncache_path`       | An optional directory containing the output packages for kernel builds. Example: `/tmp/kernel`. It is mainly used as a way for different [.spec] files to access the same cache directory. By defaults, this location will be autogenerated under `` `$storedir` `` based on the .spec file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `interpreter`          | Tells [catalyst] to use qemu to emulate a different architecture for cross compiling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `portage_prefix`       | The directory name set inside of the `portage_confdir` which will be wiped after the build is finished so the settings needed to building during Catalyst will be removed from the finished product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

On the [stage3.spec] file, `source_subpath` value needs to reference the stage 1 file respectively. In other words, with exception of the first [.spec] file in the sequence, `source_subpath` value should be set to the stage file previously built. For example, if 2021.04.17 was used as the `version_stamp` value, the `source_subpath` for the stage1 location should be: default/stage1-amd64-2021.04.17.

#### [Portage config]

This is the target\'s [/etc/portage] which is almost always needed to be set by the user. It\'s highly recommended that a user uses the RelEng defaults by cloning them with [Git](https://wiki.gentoo.org/wiki/Git "Git").

`user `[`$`]`git clone -o upstream `[`https://github.com/gentoo/releng.git`](https://github.com/gentoo/releng.git)

Where this is stored doesn\'t matter as long as root can access it, the most common locations are in the user home directory or in [/var/tmp/catalyst/releng].

Then point the `portage_confdir` option to the best defaults for the needed usage, below is listed the different types the RelEng commit hosts and when to use them:

-   [releases/portage/iso](https://github.com/gentoo/releng/tree/master/releases/portage/isos) - For creating livecds based on the [minimal](https://github.com/gentoo/releng/blob/master/releases/specs/x86/i486/installcd-stage1-openrc.spec) and [admincd](https://github.com/gentoo/releng/blob/master/releases/specs/x86/hardened/admincd-stage1-openrc.spec).
-   [releases/portage/iso-qemu](https://github.com/gentoo/releng/tree/master/releases/portage/isos-qemu) - The same as above but for when compiled in QEMU for a different architecture than the host\'s.
-   [releases/portage/livegui](https://github.com/gentoo/releng/tree/master/releases/portage/livegui) - Defaults for creating a working [livegui](https://github.com/gentoo/releng/blob/master/releases/specs/amd64/livegui/livegui-stage1.spec) ISO.
-   [releases/portage/stages](https://github.com/gentoo/releng/tree/master/releases/portage/stages) - Defaults for creating a custom stage 3 or 4 files.
-   [releases/portage/stages-qemu](https://github.com/gentoo/releng/tree/master/releases/portage/stages-qemu) - The same as above but for when compiled in QEMU for a different architecture than the host\'s.

** Note**\
When using the RelEng repo in this way a releng directory is used. This directory is wiped at the end of the build so the end-user\'s install won\'t have the same options set on their own machine. If your project needs this to be set then moving them up one level will mean they will be left for the end-user. If this is needed though, creating a custom profile and forcing options on your project may be the better solution.

#### [Cross Compiling]

One of the more useful and advance features is the `interpreter` option in the spec file. This allows the use of [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU")\'s user mode to emulate a different architect all together (for example, building for a PowerPC on a x86_64 system).

A requirement to use this is to first setup a working qemu-user system, which can be done using the [Embedded Handbook/General/Compiling with qemu user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot") article.

Making use of the [stage-qemu](https://github.com/gentoo/releng/tree/master/releases/portage/stages-qemu) defaults in the RelEng\'s github is also required to set all workarounds needed in portage to allow this to work.

In some configurations, such as multilib stages, multiple interpreters may be required. Interpreters can be listed separated by space. For example, to build amd64 on an arm64 host:

[FILE] **`stage1.spec`amd64 spec interpreter definition.**

    interpreter: /usr/bin/qemu-x86_64 /usr/bin/qemu-i386

#### [Custom profiles]

Custom profiles can also be used with [catalyst] first, a user will need to create the custom profile on their system using the article at [Profile\_(Portage)](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") and have tested it works.

** Note**\
This section will use local as the repository name but any can be used

Inside the spec file, the following will be required:

[FILE] **`stage1-openrc.spec`**

    # Tell catalyst about the repo
    repo: /var/db/repos/local

    # Tell catalyst about the custom profile
    profile: local:my-super-duper-cool-profile

### [Invocation]

Use [`catalyst`]` --help` to see all available command line options (with short explanations)

`root `[`#`]`catalyst --help`

                     usage: catalyst [-h] [-V] [--enter-chroot] [-d] [-v]
                    [--log-level ]
                    [--log-file LOG_FILE] [--color] [--nocolor] [--trace] [--profile] [-a]
                    [-p] [-P] [-T] [--versioned-cachedir] [--unversioned-cachedir] [-F]
                    [-c CONFIGS] [-f FILE] [-s SNAPSHOT]

    options:
      -h, --help            show this help message and exit
      -V, --version         display version information
      --enter-chroot        Enter chroot before starting the build

    Program output options:
      -d, --debug           enable debugging (and default --log-level debug)
      -v, --verbose         verbose output (and default --log-level info)
      --log-level
                            set verbosity of output (default: notice)
      --log-file LOG_FILE   write all output to this file (instead of stdout)
      --color               colorize output all the time (default: detect)
      --nocolor             never colorize output all the time (default: detect)

    Developer options:
      --trace               trace program output (akin to `sh -x`)
      --profile             profile program execution

    Temporary file management:
      -a, --clear-autoresume
                            clear autoresume flags
      -p, --purge           clear tmp dirs, package cache, autoresume flags
      -P, --purgeonly       clear tmp dirs, package cache, autoresume flags and exit
      -T, --purgetmponly    clear tmp dirs and autoresume flags and exit
      --versioned-cachedir  use stage version on cache directory name
      --unversioned-cachedir
                            do not use stage version on cache directory name

    Target/config file management:
      -F, --fetchonly       fetch files only
      -c CONFIGS, --configs CONFIGS
                            use specified configuration files
      -f FILE, --file FILE  read specfile
      -s SNAPSHOT, --snapshot SNAPSHOT
                            Make an ebuild repo snapshot

    Usage examples:

    Using the snapshot option to make a snapshot of the ebuild repo:
    $ catalyst --snapshot <git-treeish>

    Using the specfile option (-f, --file) to build a stage target:
    $ catalyst -f stage1-specfile.spec

### [Building stages]

#### [Distfiles directory]

By default, catalyst will download distfiles into the [/var/cache/distfiles] directory the same way portage does on the host system

#### [Binpkgs directory]

Also by default [catalyst] will create a binary package for each type of build you do (i.e. one for a generic stage3 on amd64 and also one for stage3 tuned for zen3 CPU) on the first build of every new package version, which is very useful to save on build time on the next run. These can be found in [/var/tmp/catalyst/packages] if using the default location.

For those with space issues then it can be turned off by editing [/etc/catalyst/catalyst.conf]and removing the `"pkgcache",` line.

#### [Autoresume]

If a build fails then running [catalyst] again will re-use the existing work directory to continue from where it left off. Sometimes a user may desire to start over; to do so one may use the -`-clear-autoresume` or `-a` flag. This can also be permanently disabled in [/etc/catalyst/catalyst.conf].

#### [Jobs and load average]

Setting how many job running simultaneously is set in `/etc/catalyst.conf`

[FILE] **`/etc/catalyst/catalyst.conf`catalyst.conf**

    # Integral value passed to emerge as the parameter to --jobs and is used to
    # define MAKEOPTS during the target build.
    jobs = 4

    # Floating-point value passed to emerge as the parameter to --load-average and
    # is used to define MAKEOPTS during the target build.
    # load-average = 4.0

#### [Start the build]

Once the specs have been reviewed, start [catalyst] by running the following command:

`root `[`#`]`catalyst -f stage1.spec && catalyst -f stage3.spec`

If everything went as expected a stage3 should be show up in the [/var/tmp/catalyst/builds/default/] directory.

** Note**\
The [.spec] files may have `portage_confdir` value set to specify a list of customizations to emerged packages *inside* the stage files. The directory structure specified by the `portage_confdir` variable is equivalent to the same layout as the [[/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage")] directory. Files inside this directory (i.e. [package.use], [package.unmask], [package.mask], etc.) will need to be manually maintained and occasionally adjusted as gentoo.git continues to be developed. This is the same practice as maintaining a Gentoo installation.

## [Detailed usage examples]

This section contains links to pages that explain how to use [catalyst] for specific tasks.

** Note**\
This section needs help with examples of creating netboot images or livegui images. Please link them back here and create the new pages under the Catalyst directory.

-   [Catalyst/Stage Creation](https://wiki.gentoo.org/wiki/Catalyst/Stage_Creation "Catalyst/Stage Creation") --- detailing how to build stage3 and stage4 systems with explanations of how to tune them to the required needs.
-   [Catalyst/Custom Media Image](https://wiki.gentoo.org/wiki/Catalyst/Custom_Media_Image "Catalyst/Custom Media Image") --- creating custom bootable images with custom applications for a users needs.
-   [Catalyst/New Musl Stages Creation](https://wiki.gentoo.org/wiki/Catalyst/New_Musl_Stages_Creation "Catalyst/New Musl Stages Creation") --- how to create a [musl](https://wiki.gentoo.org/wiki/Musl "Musl") libc stage 3 for unsupported architectures.

### [Convert QEMU specs to native]

Releng use QEMU usermode to build alpha, arm64be, loong, m68k, mips and riscv. If a users wishes to convert these to compile these natively, then all a user would need to do is remove the `interpreter:` line and remove the `-qemu` from the `portage_confdir` line.

** Note**\
This method is untested, however normally poses no issue. if you do run into issues though then help is available when build logs and spec files are provided with the question

## [See also]

-   [Project:RelEng](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng") --- the official Gentoo project focused on coordinating and improving the creation of official media releases of Gentoo Linux and other Gentoo operating systems.
-   [Project:Catalyst/FAQ](https://wiki.gentoo.org/wiki/Project:Catalyst/FAQ "Project:Catalyst/FAQ") --- contains frequently asked questions (FAQs) relating to the Catalyst tool. Note: This should be treated as historic in most cases.
-   [Stage file](https://wiki.gentoo.org/wiki/Stage_file "Stage file") --- an archive that contains all the files to run a minimal Gentoo environment, typically to serve as a seed for a Gentoo installation