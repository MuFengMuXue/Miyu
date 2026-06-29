Catalyst can be used to make bootable ISOs.

This guide describes the process used to create an install ISO similar to ones created by [project:RelEng](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng"). A basic understanding of Catalyst will help to follow this guide.

** Important**\
References to *stages* are unique to this LiveCD build process, and reflect stages in the build process, and are not to be confused with [stage files](https://wiki.gentoo.org/wiki/Stage_file "Stage file").

For this process, *stage1* refers to the base image, which is the core of the LiveCD, while *stage2* is the build/packaging process to make that into a bootable ISO.

## Contents

-   [[1] [Build Environment Setup]](#Build_Environment_Setup)
    -   [[1.1] [Installing Catalyst]](#Installing_Catalyst)
    -   [[1.2] [Obtaining RelEng config]](#Obtaining_RelEng_config)
    -   [[1.3] [Generating a Portage Snapshot]](#Generating_a_Portage_Snapshot)
    -   [[1.4] [Obtaining a stage3 seed]](#Obtaining_a_stage3_seed)
    -   [[1.5] [Staging the LiveCD spec files]](#Staging_the_LiveCD_spec_files)
    -   [[1.6] [Optional: Staging the LiveGUI spec files]](#Optional:_Staging_the_LiveGUI_spec_files)
-   [[2] [Template vars]](#Template_vars)
-   [[3] [Stage1]](#Stage1)
    -   [[3.1] [Preparing the Stage1 Spec File]](#Preparing_the_Stage1_Spec_File)
    -   [[3.2] [Adding custom packages]](#Adding_custom_packages)
    -   [[3.3] [Build Stage1]](#Build_Stage1)
-   [[4] [Stage2]](#Stage2)
    -   [[4.1] [Preparing the Stage2 Spec File]](#Preparing_the_Stage2_Spec_File)
    -   [[4.2] [Build Stage2]](#Build_Stage2)
-   [[5] [ISO File]](#ISO_File)

## [Build Environment Setup]

### [Installing Catalyst]

Install [[[dev-util/catalyst]](https://packages.gentoo.org/packages/dev-util/catalyst)[]] making sure the `iso` [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") (enabled by default) is set:

`root `[`#`]`emerge --ask dev-util/catalyst`

### [Obtaining RelEng config]

This build process is based on [RelEng](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng") config which is available by [git](https://wiki.gentoo.org/wiki/Git "Git"):

`/home/larry/gitstuff $``git clone -o upstream `[`https://github.com/gentoo/releng.git`](https://github.com/gentoo/releng.git)

** Important**\
The path of this config repo will be used to substitute *\@REPODIR@* for setting the `portage_confdir` within specs.

### [Generating a Portage Snapshot]

From the Catalyst build directory, a new portage snapshot can be generated with:

`/var/tmp/catalyst #``catalyst -s stable`

    16 Sep 2024 19:04:57 CDT: NOTICE  : Loading configuration file: /etc/catalyst/catalyst.conf
    NOTICE:catalyst:Loading configuration file: /etc/catalyst/catalyst.conf
    16 Sep 2024 19:04:57 CDT: NOTICE  : conf_values[options] = ['autoresume', 'bindist', 'kerncache', 'pkgcache', 'seedcache']
    NOTICE:catalyst:conf_values[options] = ['autoresume', 'bindist', 'kerncache', 'pkgcache', 'seedcache']
    16 Sep 2024 19:04:57 CDT: NOTICE  : >>> /usr/sbin/git clone --quiet --depth=1 --bare -c gc.reflogExpire=0 -c gc.reflogExpireUnreachable=0 -c gc.rerereresolved=0 -c gc.rerereunresolved=0 -c gc.pruneExpire=now --branch=stable https://anongit.gentoo.org/git/repo/sync/gentoo.git /var/tmp/catalyst/repos/gentoo.git
    NOTICE:catalyst:>>> /usr/sbin/git clone --quiet --depth=1 --bare -c gc.reflogExpire=0 -c gc.reflogExpireUnreachable=0 -c gc.rerereresolved=0 -c gc.rerereunresolved=0 -c gc.pruneExpire=now --branch=stable https://anongit.gentoo.org/git/repo/sync/gentoo.git /var/tmp/catalyst/repos/gentoo.git
    16 Sep 2024 19:05:21 CDT: NOTICE  : Creating gentoo tree snapshot 3e5f2241174dbb89608c4766ca949e77cdca7b70 from /var/tmp/catalyst/repos/gentoo.git
    NOTICE:catalyst:Creating gentoo tree snapshot 3e5f2241174dbb89608c4766ca949e77cdca7b70 from /var/tmp/catalyst/repos/gentoo.git
    16 Sep 2024 19:05:21 CDT: NOTICE  : >>> /usr/sbin/git -C /var/tmp/catalyst/repos/gentoo.git archive --format=tar 3e5f2241174dbb89608c4766ca949e77cdca7b70 |
    NOTICE:catalyst:>>> /usr/sbin/git -C /var/tmp/catalyst/repos/gentoo.git archive --format=tar 3e5f2241174dbb89608c4766ca949e77cdca7b70 |
    16 Sep 2024 19:05:21 CDT: NOTICE  :     /usr/sbin/tar2sqfs /var/tmp/catalyst/snapshots/gentoo-3e5f2241174dbb89608c4766ca949e77cdca7b70.sqfs -q -f -j1 -c gzip
    NOTICE:catalyst:    /usr/sbin/tar2sqfs /var/tmp/catalyst/snapshots/gentoo-3e5f2241174dbb89608c4766ca949e77cdca7b70.sqfs -q -f -j1 -c gzip
    16 Sep 2024 19:05:25 CDT: NOTICE  : Wrote snapshot to /var/tmp/catalyst/snapshots/gentoo-3e5f2241174dbb89608c4766ca949e77cdca7b70.sqfs
    NOTICE:catalyst:Wrote snapshot to /var/tmp/catalyst/snapshots/gentoo-3e5f2241174dbb89608c4766ca949e77cdca7b70.sqfs

** Important**\
Pay close attention to the output of this command, looking for *Wrote snapshot to:* . This line contains the `snapshot_treeish` which is required for the stage1 spec.

In this case, the **snapshot_treeish** is `3e5f2241174dbb89608c4766ca949e77cdca7b70`

### [Obtaining a stage3 seed]

Catalyst looks for seed files under [/var/tmp/catalyst/builds/\<stage3\>], a directory must be created for these if not already present:

`root `[`#`]`mkdir -p /var/tmp/catalyst/builds/23.0-default`

** Tip**\
The actual subpath under *builds* can be set arbitrarily, but is set to `23.0-default` to match the one defined in the RelEng spec.

A seed stage3 is needed to build the LiveCD, stage files can be found on the [downloads](https://www.gentoo.org/downloads) page or from [mirrors](https://www.gentoo.org/downloads/mirrors/):

`/var/tmp/catalyst/builds/23.0-default #``wget `[`https://gentoo.osuosl.org/releases/amd64/autobuilds/current-stage3-amd64-openrc/stage3-amd64-openrc-20240915T163400Z.tar.xz`](https://gentoo.osuosl.org/releases/amd64/autobuilds/current-stage3-amd64-openrc/stage3-amd64-openrc-20240915T163400Z.tar.xz)

** Note**\
In this example `stage3-amd64-openrc-20240915T163400Z.tar.xz` is used, but a new release will likely exist. The timestamp `20240915T163400Z` will be used later for *stage 1* spec config.

** Tip**\
If building a LiveGUI, using a `desktop` profile image is preferred.

### [Staging the LiveCD spec files]

Specs for the *stage 1* and *stage 2* are provided in the previously cloned git repo. Specs should be available in the cloned git repo, under [releases/specs/**[\<arch\>]**]:

`releng $``ls releases/specs/amd64/installcd*`

    releases/specs/amd64/installcd-stage1.spec  releases/specs/amd64/installcd-stage2-minimal.spec

These spec files can be copied to [/var/tmp/catalyst] with:

`releng #``cp releases/specs/amd64/installcd* /var/tmp/catalyst`

### [Optional: Staging the LiveGUI spec files]

To use the larger LiveGUI specs, available under [releases/specs/**[\<arch\>]**/livegui]:

`releng #``cp releases/specs/amd64/livegui/*.spec /var/tmp/catalyst`

## [Template vars]

Before being used, RelEng specs must be edited, as a few template vars are present, enclosed in **@\'**s:

-   *TIMESTAMP* - The release timestamp used in the **version_stamp** and **source_subpath**, e.g. `20240915T163400Z`.
-   *DATESTAMP* - The release date, used for the LiveCD volume label, e.g. `2024-09-15`.
-   *TREEISH* - The **snapshot_treeish** hash, e.g. `3e5f2241174dbb89608c4766ca949e77cdca7b70`.
-   *REPO_DIR* - The base path to the releng config for *portage_confdir*, e.g. [/home/larry/gitstuff/releng].

** Note**\
These variables would typically be substituted by catalyst-auto.

## [Stage1]

The first build step is to create the *stage 1* which is built off of the selected *seed stage 3* and based on the provided spec.

### [Preparing the Stage1 Spec File]

When used manually, a few key fields must be edited to make RelEng provided spec files usable, these include:

-   `version_stamp` - The version string used for the catalyst build, can be set arbitrarily.
-   `rel_type` - The release type, used to set the sub-directory under [/var/tmp/catalyst/builds].
-   `snapshot_treeish` - The treeish for the portage snapshot.
-   `source_subpath` - The source for the stage3 seed.
-   `portage_confdir` - The config dir for the build environment.

[FILE] **`/var/tmp/catalyst/installcd-stage1.spec`LiveCD stage 1 base template.**

    subarch: amd64
    version_stamp: @TIMESTAMP@
    target: livecd-stage1
    rel_type: 23.0-default
    profile: default/linux/amd64/23.0/no-multilib
    snapshot_treeish: @TREEISH@
    source_subpath: 23.0-default/stage3-amd64-openrc-@TIMESTAMP@
    compression_mode: pixz
    portage_confdir: @REPO_DIR@/releases/portage/isos

[FILE] **`/var/tmp/catalyst/installcd-stage1.spec`LiveCD stage 1 filled template.**

    subarch: amd64
    version_stamp: custom_livecd
    target: livecd-stage1
    rel_type: 23.0-default
    profile: default/linux/amd64/23.0/no-multilib
    snapshot_treeish: 3e5f2241174dbb89608c4766ca949e77cdca7b70
    source_subpath: 23.0-default/stage3-amd64-openrc-20240915T163400Z
    compression_mode: pixz
    portage_confdir: /home/larry/gitstuff/releng/releases/portage/isos

** Tip**\
Remember to use a **desktop** profile *stage3* for `source_subpath` when building a LiveGUI ISO.

** Note**\
**custom_livecd** is used as the `version_stamp` here, but any unique build identifier can be used.

### [Adding custom packages]

To add a package, such as [[[app-misc/neofetch]](https://packages.gentoo.org/packages/app-misc/neofetch)[]], it can be added to the `livecd/packages` list:

[FILE] **`/var/tmp/catalyst/installcd-stage1.spec`Adding neofetch to the livecd**

    livecd/packages:
        app-accessibility/brltty
        app-accessibility/espeakup
        app-admin/hddtemp
    ...
        sys-libs/glibc
        sys-libs/gpm
        sys-power/acpid
        www-client/links
        #Custom programs
        app-misc/neofetch

### [Build Stage1]

With the *stage1 spec* configured, it can be built with:

`/var/tmp/catalyst #``catalyst -f installcd-stage1.spec`

## [Stage2]

The *stage2* image is built using the *stage1* as a base. This stage adds a kernel and bootloader, then wraps the root environment into a single bootable package.

### [Preparing the Stage2 Spec File]

Similar to the *stage1*, several portions of the RelEng provided spec require edits:

-   `version_stamp` - The version string used for the catalyst build, can be set arbitrarily.
-   `snapshot_treeish` - The treeish for the portage snapshot.
-   `source_subpath` - The stage1 path, sourcing the stage3.
-   `portage_confdir` - The config dir for the build environment.
-   `livecd/iso` The filename for the output ISO.
-   `livecd/volid` The volume label for the output ISO.
-   `boot/kernel/gentoo/config` .config changed for the output kernel.

** Important**\
Be sure to set the `source_subpath` to the path to the built *stage 1*, e.g. `23.0-default/custom_livecd`.

[FILE] **`installcd-stage2-minimal.spec`LiveCD stage 2 base template.**

    subarch: amd64
    version_stamp: @TIMESTAMP@
    target: livecd-stage2
    rel_type: 23.0-default
    profile: default/linux/amd64/23.0/no-multilib
    snapshot_treeish: @TREEISH@
    source_subpath: 23.0-default/livecd-stage1-amd64-@TIMESTAMP@
    portage_confdir: @REPO_DIR@/releases/portage/isos

    livecd/bootargs: dokeymap
    livecd/fstype: squashfs
    livecd/iso: install-amd64-minimal-@TIMESTAMP@.iso
    livecd/type: gentoo-release-minimal
    livecd/volid: Gentoo-amd64-@DATESTAMP@

    boot/kernel: gentoo

    boot/kernel/gentoo/distkernel: yes
    boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a mdraid -o btrfs -o crypt -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -i /lib/keymaps /lib/keymaps -I busybox
    boot/kernel/gentoo/config: @REPO_DIR@/releases/kconfig/amd64/dist-amd64-livecd.config
    boot/kernel/gentoo/packages: net-wireless/broadcom-sta

[FILE] **`installcd-stage2-minimal.spec`LiveCD stage 2 filled template.**

    subarch: amd64
    version_stamp: custom_livecd
    target: livecd-stage2
    rel_type: 23.0-default
    profile: default/linux/amd64/23.0/no-multilib
    snapshot_treeish: 3e5f2241174dbb89608c4766ca949e77cdca7b70
    source_subpath: 23.0-default/livecd-stage1-amd64-custom_livecd
    portage_confdir: /home/larry/gitstuff/releng/releases/portage/isos

    livecd/bootargs: dokeymap
    livecd/fstype: squashfs
    livecd/iso: install-amd64-minimal-custom_livecd.iso
    livecd/type: gentoo-release-minimal
    livecd/volid: Gentoo-amd64-custom_livecd

    boot/kernel: gentoo

    boot/kernel/gentoo/distkernel: yes
    boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a mdraid -o btrfs -o crypt -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -i /lib/keymaps /lib/keymaps -I busybox
    boot/kernel/gentoo/config: /home/larry/gitstuff/releng/releases/kconfig/amd64/dist-amd64-livecd.config
    boot/kernel/gentoo/packages: net-wireless/broadcom-sta

### [Build Stage2]

The ISO can be built with:

`/var/tmp/catalyst #``catalyst -f installcd-stage2-minimal.spec`

## [ISO File]

The ISO will be located in `/var/tmp/catalyst/builds/default` which can be written to a CD, USB or just tested directly in a VM.