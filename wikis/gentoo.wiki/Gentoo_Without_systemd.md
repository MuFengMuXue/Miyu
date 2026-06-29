This page contains [[changes](https://wiki.gentoo.org/index.php?title=Gentoo_without_systemd&oldid=1408343&diff=1408833)] which are not marked for translation.

Other languages:

-   [English]

[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=Gentoo_without_systemd&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

This article contains references to the [obsolete *sys-fs/udev* package](https://public-inbox.gentoo.org/gentoo-dev/ZL6xwI9xXAQmupbd@naomi/). Could anyone who knows how to fix this and has the time please bring it up to date?

One of Gentoo\'s distinctive characteristics is the ability to support [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") as an *option*, instead of it being the single available [init system](https://wiki.gentoo.org/wiki/Init_system "Init system") implementation. The distribution offers the choice of having a working Linux, non systemd-based operating system, and this article provides some tips on how to avoid unwanted installation of [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]].

## Contents

-   [[1] [Gentoo\'s init system and service manager setup]](#Gentoo.27s_init_system_and_service_manager_setup)
    -   [[1.1] [So, why is systemd pulled in?]](#So.2C_why_is_systemd_pulled_in.3F)
-   [[2] [Taking explicit measures to avoid installation of systemd]](#Taking_explicit_measures_to_avoid_installation_of_systemd)
    -   [[2.1] [Globally disabling and masking the systemd USE flag]](#Globally_disabling_and_masking_the_systemd_USE_flag)
    -   [[2.2] [Package masking systemd]](#Package_masking_systemd)
-   [[3] [systemd unit files]](#systemd_unit_files)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Packages that unconditionally require systemd]](#Packages_that_unconditionally_require_systemd)
    -   [[4.2] [Checking if systemd is installed or not]](#Checking_if_systemd_is_installed_or_not)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [][Gentoo\'s init system and service manager setup]

Several [Gentoo profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") that select the Linux kernel and the [GNU C library](https://wiki.gentoo.org/wiki/GNU_C_library "GNU C library") (`KERNEL` [USE_EXPAND](https://wiki.gentoo.org/wiki/USE_EXPAND "USE EXPAND") variable set to `linux` and `ELIBC` USE_EXPAND variable set to `glibc`) have [[[virtual/service-manager]](https://packages.gentoo.org/packages/virtual/service-manager)[]] and [[[virtual/dev-manager]](https://packages.gentoo.org/packages/virtual/dev-manager)[]] packages in [the system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), i.e. it is guaranteed to be present in every Gentoo machine. They are a **virtual packages**, that is, it installs no files but has an *any-of* dependency, `|| ( ... )`, on other packages. For these profiles, [[[virtual/service-manager]](https://packages.gentoo.org/packages/virtual/service-manager)[]] can be satisfied by [[[sys-apps/openrc]](https://packages.gentoo.org/packages/sys-apps/openrc)[]] or [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]], and [[[virtual/dev-manager]](https://packages.gentoo.org/packages/virtual/dev-manager)[]] can be satisfied by [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]], and [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] itself.

A Gentoo system installed from a [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit "Sysvinit") + [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") stage3 tarball (i.e. a [stage3-\*.tar.xz] or [stage3-\*.tar.bz2] file that does not contain \"systemd\" in the name) will have [[[sys-apps/openrc]](https://packages.gentoo.org/packages/sys-apps/openrc)[]] and [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]] already installed, so systemd shouldn\'t get installed unless some other package pulls it as a dependency for some reason.

For a refresher on stage3 tarballs and profiles, please review [the Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page").

### [][So, why is systemd pulled in?]

Users of a non-systemd Gentoo system might be occasionally surprised by [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") trying to install systemd in response to an [emerge] command. Systemd is a large software package that implements an init system, but also provides a number of other executables ([systemd-udevd], [systemd-logind], [systemd-resolved], [systemd-networkd], [systemd-tmpfiles], [systemd-localed], [systemd-machined], [systemd-nspawn], etc.), libraries ([libsystemd], [libudev]), a [PAM module](https://wiki.gentoo.org/wiki/PAM "PAM") ([pam_systemd.so]) and a UEFI boot manager ([[systemd-boot](https://wiki.gentoo.org/wiki/Systemd/systemd-boot "Systemd/systemd-boot")]), among other components. So any other package that needs any of these components, even if it is just one, would pull the whole systemd package as a dependency.

Most these packages, however, only have a \"soft dependency\" on systemd, that is, optional functionality that uses a systemd component, and that can be turned on or off at build time. Gentoo, being a source-based distribution, is able to easily take advantage of such package features, and corresponding ebuilds usually expose a `systemd` [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") that can be unset to avoid installing systemd as a dependency. For most (all?) Gentoo profiles except the systemd ones (i.e. those that contain \"systemd\" in their names), this USE flag is unset by default.

A small number of packages have a [\"hard dependency\"](https://wiki.gentoo.org/wiki/Gentoo_without_systemd#harddep "Gentoo without systemd") on systemd, that is, their ebuild unconditionally lists [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] as a dependency, with no regard to the `systemd` USE flag. The most well known example of this used to be the [GNOME desktop environment](https://wiki.gentoo.org/wiki/GNOME "GNOME"), which, for versions 3.28 and earlier, contained components that required [systemd-logind] (among them, notably, its display manager, [GDM](https://wiki.gentoo.org/wiki/GNOME/gdm "GNOME/gdm")). As of version 3.30, though, Gentoo\'s packaging of GNOME allows it to work once again with sysvinit + OpenRC as the init system^[\[1\]](#cite_note-1)^. This is achieved through [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind"); non-systemd GNOME profiles (i.e. those with \"gnome\", but not \"systemd\", in their name) set the `elogind` USE flag so that packages pull [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]] as a dependency instead of sys-apps/systemd.

It might also be necessary to remove lines that set the `systemd` USE flag from files in [/etc/portage/package.use] that could have been added automatically.

## [Taking explicit measures to avoid installation of systemd]

Current profile settings are usually enough to avoid systemd on a Gentoo system installed from a sysvinit + OpenRC stage3 tarball, provided a non-systemd profile has been selected. However, the following explict measures can be easily taken by concerned administrators.

### [Globally disabling and masking the systemd USE flag]

The `systemd` USE flag can be globally unset in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")]:

[FILE] **`/etc/portage/make.conf`**

    # Assuming USE contains more flag settings, represented by ellipsis:
    USE="... -systemd ..."

This is an extra assurance that packages with a soft dependency on systemd will always install without enabling the features that require it.

In addition, the USE flag can be masked in [[/etc/portage/profile/use.mask](https://wiki.gentoo.org/wiki//etc/portage/profile/use.mask "/etc/portage/profile/use.mask")] so that Portage\'s autounmask feature will be unable to suggest enabling it:

[FILE] **`/etc/portage/profile/use.mask/systemd`**

    systemd

### [[] Package masking systemd]

The best assurance that systemd will not be installed is [masking the package](https://wiki.gentoo.org/wiki//etc/portage/package.mask "/etc/portage/package.mask") altogether:

[FILE] **`/etc/portage/package.mask/systemd`package.mask directory example**

    sys-apps/systemd

If an [emerge] command for any reason (including odd USE flag combinations) tries to pull sys-apps/systemd as a dependency, the package mask will cause a blocker that Portage cannot resolve (i.e. the output of [emerge] will show `[blocks B ]`), and make the [emerge] command fail. The administrator can then look at the blocker messages and figure out what to do, which in some cases might mean to just give up and not install [certain packages](https://wiki.gentoo.org/wiki/Gentoo_without_systemd#harddep "Gentoo without systemd").

## [systemd unit files]

** Warning**\
Some packages like [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]] install files to directories with [systemd] in the path and therefore a wide INSTALL_MASK for e.g. [/lib/systemd/\*] is dangerous and may lead to breaking an installation.

Some upstream packages provide systemd unit files, to make them easier to install on systemd-based distributions and try make them work mostly out of the box, but don\'t otherwise have any heavier integration with systemd, or require any systemd-specific functionality. This sort of packages are not considered to have an actual dependency on systemd (neither \"soft\" or \"hard\"), and, according to the [official ebuild policy for systemd](https://wiki.gentoo.org/wiki/Project:Systemd/Ebuild_policy "Project:Systemd/Ebuild policy"), unit files follow the usual guidelines against small text files ([Bash completion](https://wiki.gentoo.org/index.php?title=Bash_completion&action=edit&redlink=1 "Bash completion (page does not exist)"), [logrotate](https://wiki.gentoo.org/wiki/Logrotate "Logrotate") etc.) and ebuilds must not prevent their installation based on the `systemd` USE flag.

Unit files are harmless and do nothing if systemd is not installed, just like OpenRC service scripts do nothing if [[[sys-apps/openrc]](https://packages.gentoo.org/packages/sys-apps/openrc)[]] is not installed. However, users that absolutely do not want systemd unit files on their machines, can add systemd\'s unit file paths to the `INSTALL_MASK` variable in [/etc/portage/make.conf]:

[FILE] **`/etc/portage/make.conf`**

    # Assuming INSTALL_MASK contains more items represented by ellipsis:
    INSTALL_MASK="... /lib/systemd/*/*.service /usr/lib/systemd/*/*.service ..."

Or alternatively, write a Portage postsync hook in [/etc/portage/postsync.d]:

[FILE] **`/etc/portage/postsync.d/10systemd`**

    rm -rf /lib/systemd/*/*.service /usr/lib/systemd/*/*.service

** Note**\
systemd has more search paths than those in [/lib/systemd] (if the `split-usr` USE flag is set) or [/usr/lib/systemd] (if the `split-usr` USE flag is unset), however the package manager *should* restrict itself to installing unit files in those directories, as per systemd\'s convention. The other locations are for unit files that are e.g. dynamically generated ([/run/systemd/system], etc.), installed by the administrator ([/etc/systemd/system], etc.), or from a package that has been installed without using the package manager ([/usr/local/lib/systemd/system], etc.). Users that prefer to also add those paths to `INSTALL_MASK` or the postsync hook can find the complete list [here](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#Unit%20File%20Load%20Path)

For information about `INSTALL_MASK` or postsync hooks, please consult [man make.conf] and [man portage], respectively.

## [Troubleshooting]

### [[] Packages that unconditionally require systemd]

As long as systemd is [package masked](https://wiki.gentoo.org/wiki/Gentoo_without_systemd#pkgmask "Gentoo without systemd"), it\'s impossible to install packages with a \"hard\" dependency on it. Cases like this almost always happen by upstream\'s choice, so there is little Gentoo can do in a packager and distributor role to avoid that, short of developing a Gentoo-specific patch set and committing to its long-term maintenance across upstream\'s releases. So the most advisable course of action for a solution is to try contacting the upstream developer team directly: filing a bug report, contributing a patch, etc. Interested people must be aware that upstream\'s openness to accept such kinds of patches or bug reports may vary widely from project to project.

Sometimes alternative packages with similar functionality and no hard dependency on systemd can be found.

### [Checking if systemd is installed or not]

The [equery] program from [Gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") can be used to check if systemd is installed:

`user `[`$`]`equery list sys-apps/systemd`

     * Searching for systemd in sys-apps ...
    !!! No installed packages matching 'sys-apps/systemd'

Nowadays, getting systemd accidentally installed if the selected profile is a non-systemd one is hard, because of blockers that Portage cannot resolve with [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]] (i.e. the output of [emerge] will show `[blocks B ]`), and with [[[sys-apps/sysvinit]](https://packages.gentoo.org/packages/sys-apps/sysvinit)[]] because of the on-by-default state of the `sysv-utils` USE flag in recent versions of [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]]^[\[2\]](#cite_note-2)^. Turning a Gentoo system installed from a sysvinit + OpenRC stage3 tarball into a systemd-based one requires an [emerge \--newuse \--deep \@world] step with a particular USE flag setup as per [the installation instructions](https://wiki.gentoo.org/wiki/Systemd#Profile "Systemd"), which is facilitated by systemd profiles. And if the package is somehow installed, actually running systemd as the init system requires a machine reboot with a suitable setup to either execute the [systemd] program as process 1 (e.g. an `init=` kernel parameter or a suitable [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") setup), or have [/sbin/init] be a symlink to [systemd].

Nevertheless, if systemd is accidentally installed, it is advised to get in touch with [Gentoo\'s support community](https://www.gentoo.org/support) for help with its removal, because it might be a nontrivial task depending on why package got installed in the first place, and whether it is actually running as the init system, or just installed but inactive.

## [See also]

-   [Hard dependencies on systemd](https://wiki.gentoo.org/wiki/Hard_dependencies_on_systemd "Hard dependencies on systemd") --- a (possibly partial) list of packages in Gentoo\'s repository that unconditionally require [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")

## [External resources]

-   [without-systemd](https://github.com/KenjiBrown/without-systemd) overlay, containing replacements for [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]]
-   [A thread in the Gentoo Forums](https://forums.gentoo.org/viewtopic-t-1074786.html) about using the `INSTALL_MASK` variable to prevent installation of systemd unit files.
-   [Funtoo Linux Optimization Proposal: No-systemd system](https://www.funtoo.org/FLOP:No-systemd_system)

## [References]

1.  [[[↑](#cite_ref-1)] [Gentoo website, News section, [\"Gentoo GNOME 3.30 for all init systems\"](https://www.gentoo.org/news/2019/03/27/gnome-330-openrc.html), March 27th, 2019 .]]
2.  [[[↑](#cite_ref-2)] [News item [\"systemd sysv-utils blocker resolution\"](https://www.gentoo.org/support/news-items/2018-01-23-systemd-blocker.html), January 1st, 2018. Retrieved on September 22nd, 2018.]]