Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/de "Gentoo aktualisieren (3% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/es "Actualizar Gentoo (99% translated)")
-   [français](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/fr "Upgrading Gentoo/fr (2% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/it "Aggiornare Gentoo (1% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/hu "Gentoo frissítése (99% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/pt-br "Atualizando o Gentoo (1% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/sv "Uppgradera Gentoo (2% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/ru "Обновление Gentoo (58% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/zh-cn "升级Gentoo (74% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/ja "Gentooのアップグレード (99% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Upgrading_Gentoo/ko "Upgrading Gentoo (25% translated)")

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades] --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

Gentoo has its own approach to updates, this document explains how to **upgrade (update)** Gentoo, as well as how to proceed for a well maintained system.

It is important to keep Gentoo up to date. In addition to the need to have the latest security patches, Gentoo installations can get too out of sync with the current version and sometimes become complex to update.

** Tip**\
Update Gentoo Linux between daily and weekly to keep a Gentoo Linux installation running smoothly with the latest security updates. Waiting more than a few weeks to update may make things a little more complicated when the update is attempted. Please don\'t [synchronize](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository") more than once daily, to avoid strain on the servers.

** Note**\
Any instructions that only affect ten or more year old systems will not be retained here. See [page history](https://wiki.gentoo.org/wiki/Special:PermanentLink/904395 "Special:PermanentLink/904395") for previous versions.

## Contents

-   [[1] [About Gentoo architecture and upgrades]](#About_Gentoo_architecture_and_upgrades)
-   [[2] [Updating packages]](#Updating_packages)
    -   [[2.1] [Cleaning up after an update]](#Cleaning_up_after_an_update)
-   [[3] [Profile updating instructions]](#Profile_updating_instructions)
    -   [[3.1] [General instructions]](#General_instructions)
        -   [[3.1.1] [Switch profiles with eselect]](#Switch_profiles_with_eselect)
        -   [[3.1.2] [Switch profiles manually]](#Switch_profiles_manually)
    -   [[3.2] [Updating to 23.0 profile]](#Updating_to_23.0_profile)
    -   [[3.3] [Updating to 17.1 profile]](#Updating_to_17.1_profile)
    -   [[3.4] [Updating to 17.0 profile]](#Updating_to_17.0_profile)
-   [[4] [Updating old systems]](#Updating_old_systems)
    -   [[4.1] [Synopsis]](#Synopsis)
    -   [[4.2] [Preparing the intermediate build chroot]](#Preparing_the_intermediate_build_chroot)
    -   [[4.3] [Network, chroot, and update]](#Network.2C_chroot.2C_and_update)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [[] About Gentoo architecture and upgrades]

Gentoo differs from most other Linux distributions when it comes to updates. Most distributions have regular releases, every few months or years, which can be anticipated events for some distributions.

Gentoo, by contrast, is a ***[rolling release](https://en.wikipedia.org/wiki/Rolling_release "wikipedia:Rolling release")*** distribution. There is no need to wait for a release to come out in order to get the latest version of packages - software can be installed as soon as it becomes stable. Gentoo was designed from the beginning around this concept of **fast, incremental updates**, and there are frequent updates to Gentoo software, with new and updated packages most days. Further information on Gentoo specifics can be found in the [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ"), about [releases and Gentoo](https://wiki.gentoo.org/wiki/FAQ#Can_I_upgrade_Gentoo_from_one_release_to_another_without_reinstalling.3F "FAQ") and [what makes Gentoo different](https://wiki.gentoo.org/wiki/FAQ#What_makes_Gentoo_different.3F "FAQ").

Once software is installed, **[regular updates]** will keep all packages on the latest available version.

In rare cases, changes made to the core system, to certain packages, [profile changes](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), or certain updates of [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), may require manual intervention during or after an update. A [news item](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base") will be published in such critical cases and/or will be signaled after a [Gentoo repository synchronization](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository"). Always read and follow the news items and Portage messages.

Profiles are central to a Gentoo system because they can define core system functionality, and new profiles are made available when there are fundamental changes to the way Gentoo works. A profile is [selected at install time](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Choosing_the_right_profile "Handbook:AMD64/Installation/Base"), according to the intended use of the system and is usually only changed if necessary, or for an update.

## [[] Updating packages]

The [Handbook](https://wiki.gentoo.org/wiki/Handbook "Handbook") has detailed information on [updating the Gentoo repository](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Portage#Updating_the_Gentoo_repository "Handbook:AMD64/Working/Portage") and on [updating the system](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Portage#Updating_the_system "Handbook:AMD64/Working/Portage"). See [man emerge] for more detailed information. See [repository synchronization](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository") for complete information on how to use [emaint] to synchronize repositories.

** Important**\
It is important to read and follow any and all [news items](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base") that may be listed after performing a repository sync.

To update all installed packages to the latest available versions, first [update the Gentoo repository](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository") with [[emaint]](https://wiki.gentoo.org/wiki/Project:Portage/Sync#Operation "Project:Portage/Sync"):

`root `[`#`]`emaint --auto sync`

Or, for short:

`root `[`#`]`emaint -a sync`

This may output messages that should be read and followed, notably the [news items](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base") previously mentioned. If config file updates are pending from a previous update, it may remind to [update the config files](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf").

Run [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") to update the whole system, with dependencies:

`root `[`#`]`emerge --ask --verbose --update --deep --newuse @world`

Or, with short options:

`root `[`#`]`emerge -avuDN @world`

`--changed-use` may be used in place of `--newuse`, but only if you do not build binary packages. `--changed-use` will not trigger reinstallation when disabled USE flags are added or removed from a package. See the [Binary package guide](https://wiki.gentoo.org/wiki/Binary_package_guide#Updating_packages_on_the_binary_package_host "Binary package guide").

`--with-bdeps=y` can be used to update build time dependencies also.

** Important**\
Pay attention to any information provided by Portage at the end of the update. Some of this information may be available in the [Portage log](https://wiki.gentoo.org/wiki/Portage_log "Portage log").

If Portage reports dependency issues, sometimes using the `--backtrack=30` (or an even higher number) can help. By default, Portage has a relatively low limit on how far it tries to resolve dependencies (for performance reasons), occasionally it is not enough.

When the output of portage contain pages over pages of unresolved dependency issues, in addition to `--backtrack=1000`, it can be useful to try `--emptytree`. When emerge succeed to ask for a package list to update, pay attention to any information about remaining issues like skipped updates. When the output of emerge is fine, as `--emptytree` will be overkill in most cases and take a very long time, refuse the update and run the same command without that option.

Any configuration file changes should be addressed, this can be managed by [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf"):

`root `[`#`]`dispatch-conf`

### [[] Cleaning up after an update]

After the update, Portage recommends running [emerge \--depclean]. Be very careful running [emerge \--depclean], it can remove important packages (e.g. kernel sources or [virtual package](https://wiki.gentoo.org/wiki/Project:Portage/FAQ#Why_does_emerge_--depclean_sometimes_remove_system_packages.3F "Project:Portage/FAQ") optional dependencies when an alternative gets merged).

** See also**\
See [remove orphaned packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Remove_orphaned_packages "Knowledge Base:Remove orphaned packages") for information on how to use [emerge \--depclean] to remove potentially unused packages safely. See also the [Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ#Why_does_emerge_--depclean_sometimes_remove_system_packages.3F "Project:Portage/FAQ").

## [[] Profile updating instructions]

** Important**\
Read [relevant documentation](https://wiki.gentoo.org/wiki/Profile_(Portage)#Changing_profile "Profile (Portage)") before performing any profile changes.

** Warning**\
Read the [[systemd]](https://wiki.gentoo.org/wiki/Systemd "Systemd") documentation before changing to a [systemd] profile.

** Important**\
Make sure the main Gentoo repository (the Portage tree) has been synced before performing any profile changes.

When a new profile is available, Portage will inform the user with a [news item](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base") (recent news items are listed on [the website](https://www.gentoo.org/support/news-items/)).

If a system is too old, it may be non trivial to [get the system up to date](https://wiki.gentoo.org/wiki/Upgrading_Gentoo#Updating_old_systems "Upgrading Gentoo"), it may even be easier to start from scratch.

Generally, it is not mandatory to switch to a new profile when one comes out. Systems can continue to use their old profile, they won\'t stop working by staying on an old profile. However, Gentoo strongly recommends updating the profile if it becomes deprecated, as this means that Gentoo developers no longer plan on supporting it.

Profile updates are executed manually. The way to update may vary significantly from profile to profile; it depends on how deep the modifications introduced in the new profile are. In the simplest case, users only have to use the [eselect] tool to change the [/etc/portage/make.profile] symlink, the worst case could be having to recompile the entire system from scratch, with significant reconfiguration (though changes are usually not too hard, and are well explained - the main thing to remember is to properly follow the instructions).

Exactly what is required to migrate to a new profile is detailed in the relevant news item.

### [[] General instructions]

This is a generic outline of what is done to update a profile. As stated previously, specific instructions will be provided in a [news item](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base"), for each new profile. A profile update often requires manual intervention, beyond just switching the profile version.

** Note**\
There are **desktop** subprofiles for most architectures. Users should examine these profiles carefully, as they may serve their requirements better than the extremely minimal default profiles.

** Important**\
The developer subprofile is specifically for Gentoo Linux development tasks. It is *not* meant to help set up general development environments.

#### [[] Switch profiles with eselect]

Make sure [warnings in parent section](https://wiki.gentoo.org/wiki/Upgrading_Gentoo#General_instructions "Upgrading Gentoo") have been read.

To switch profiles with the automatic tool, [[[app-admin/eselect]](https://packages.gentoo.org/packages/app-admin/eselect)[]] must be installed. The [eselect] utility makes viewing and selecting profiles easy, without needing to create or remove symlinks by hand:

`root `[`#`]`eselect profile list `

`root `[`#`]`eselect profile set <number>`

#### [[] Switch profiles manually]

Make sure [warnings in parent section](https://wiki.gentoo.org/wiki/Upgrading_Gentoo#General_instructions "Upgrading Gentoo") have been read.

Changing profiles manually is still supported:

`root `[`#`]`rm /etc/portage/make.profile `

`root `[`#`]`cd /etc/portage `

`root `[`#`]`ln -s ../../var/db/repos/gentoo/profiles/<selected profile> make.profile `

### [[] Updating to 23.0 profile]

See the appropriate [news item](https://www.gentoo.org/support/news-items/2024-03-22-new-23-profiles.html). At this point all installations should already be using the 23.0 profile, and migration could be difficult.

### [[] Updating to 17.1 profile]

See the appropriate [news item](https://www.gentoo.org/support/news-items/2019-06-05-amd64-17-1-profiles-are-now-stable.html). At this point all installations should already be using the 17.1 profile, and migration could be difficult.

### [[] Updating to 17.0 profile]

See the appropriate [news item](https://www.gentoo.org/support/news-items/2017-11-30-new-17-profiles.html). At this point all installations should be using the 17.1 profile, and migration could be difficult.

## [[] Updating old systems]

Sometimes, systems are too old to easily upgrade. It may be possible to manually update a very old system, but it may be better to start from scratch and copy system configuration and files from the old system to the new one.

Here is a rough guide to updating an old system. Another method can be found [here](https://wiki.gentoo.org/wiki/User:NeddySeagoon/HOWTO_Update_Old_Gentoo "User:NeddySeagoon/HOWTO Update Old Gentoo").

### [[] Synopsis]

The idea with this upgrade approach is that we create an intermediate build chroot in which a recent stage3 is extracted. Then, using the tools available in the stage3 chroot we upgrade the packages on the live system.

** Warning**\
The commands below might be incomplete and serve more as a guidance rather than work instructions. Unless the approach is clear, it might be faster to just backup the important files and re-install Gentoo.

### [[] Preparing the intermediate build chroot]

Let\'s first create the intermediate build chroot location, say [/mnt/build], and extract a recent stage3 archive into it.

`root `[`#`]`mkdir -p /mnt/build `

`root `[`#`]`tar -xf /path/to/stage3-somearch-somedate.tar.bz2 -C /mnt/build `

`root `[`#`]`mount --rbind /dev /mnt/build/dev `

`root `[`#`]`mount --rbind /proc /mnt/build/proc `

`root `[`#`]`mount --rbind /sys /mnt/build/sys `

Next, we create a mount point inside this chroot environment, on which we then bind-mount the live (old) environment.

`root `[`#`]`mkdir -p /mnt/build/mnt/host `

`root `[`#`]`mount --rbind / /mnt/build/mnt/host `

So now the live (old) system is also reachable within [/mnt/build/mnt/host]. This will allow us to reach the live (old) system and update the packages even when chrooted inside the intermediate build chroot.

### [][[] Network, chroot, and update]

The new install needs to access the network, so copy over the network related information:

`root `[`#`]`cp -L /etc/resolv.conf /mnt/build/etc/`

Now chroot into the intermediate build location, and start updating vital packages on the live system, until the live system can be updated from within the live system (rather than through the intermediate build chroot):

`root `[`#`]`chroot /mnt/build `

`root `[`#`]`source /etc/profile `

`root `[`#`]`export PS1="(chroot) $"`

`(chroot) root #``emerge --sync`

It may be a good idea to check that the profile and Portage configuration are compatible between the (old) live system and the chroot.

Now start building packages into the (old) live system. If Portage is old or missing, it is a good idea to start with that:

`(chroot) root #``emerge --root=/mnt/host --config-root=/mnt/host --verbose --oneshot sys-apps/portage`

Keep this chrooted session open and try to update the (old) live system. When failures occur, use this chrooted session to update packages using the build tools available in the intermediate build chroot (which includes recent [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]], [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]], etc.). Tools can be added as needed to the build chroot.

** Important**\
Do not forget to add `--root=/mnt/host --config-root=/mnt/host` to all [emerge] commands executed within the chroot! Otherwise the chroot itself is updated rather than the (old) live system.

For some installations it may be necessary to update configuration files in order to install new software. Make the changes in the chroot environment.

To get the system fully up-to-date before exiting the root, build the `@world` set (all packages) into the (old) live system:

`(chroot) root #``emerge --root=/mnt/host --config-root=/mnt/host --update --newuse --deep --ask @world`

Once finished the system should now be up to date!

## [[] See also]

-   [Updating old Gentoo installations](https://wiki.gentoo.org/wiki/User:NeddySeagoon/HOWTO_Update_Old_Gentoo "User:NeddySeagoon/HOWTO Update Old Gentoo")
-   [Can I upgrade Gentoo from one release to another without reinstalling?](https://wiki.gentoo.org/wiki/FAQ#Can_I_upgrade_Gentoo_from_one_release_to_another_without_reinstalling.3F "FAQ")
-   [Cheat Sheet on updates](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet#Package_upgrades "Gentoo Cheat Sheet")
-   [Handbook on updates](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Portage#Updating_the_system "Handbook:AMD64/Working/Portage")
-   [Installation](https://wiki.gentoo.org/wiki/Installation "Installation") --- an overview of the principles and practices of installing Gentoo on a running system.

## [[] External resources]

-   [Automated Gentoo System Updater](https://blogs.gentoo.org/gsoc/2023/08/27/final-report-automated-gentoo-system-updater/)

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Gregorio Guidi, Chris Gianelloni, Joshua Saddler**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*