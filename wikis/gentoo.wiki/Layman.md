This page contains [[changes](https://wiki.gentoo.org/index.php?title=Layman&oldid=1240976&diff=1420515)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Layman/hu "Layman (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Layman/zh-cn "Layman (53% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Layman/ja "Layman (89% translated)")

** Warning**\
[[[app-portage/layman]](https://packages.gentoo.org/packages/app-portage/layman)[]] has been removed. The [[eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository")] eselect module supersedes [layman] and is currently the preferred way for managing ebuild repositories.

**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Layman "Project:Layman")][Project](https://wiki.gentoo.org/index.php?title=Project:Layman&action=edit&redlink=1 "Project:Layman (page does not exist)")

[[]][GitWeb](https://gitweb.gentoo.org/proj/layman.git)

[[]][GitHub](https://github.com/gentoo/layman)

**Layman** is a [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") management tool. It offers a single command-line interface to repository management for end users.

Even though most of layman\'s functionality is now integrated into [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") and [eselect-repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository"), [layman] does support some version control systems which Portage does not natively sync (e.g. darcs and g-sorcery).

## Contents

-   [[1] [Features]](#Features)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
    -   [[2.3] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Basic invocations]](#Basic_invocations)
    -   [[3.2] [Mountable repositories with layman-mounter]](#Mountable_repositories_with_layman-mounter)
    -   [[3.3] [Setting repository priorities with Layman]](#Setting_repository_priorities_with_Layman)
    -   [[3.4] [Adding custom repositories]](#Adding_custom_repositories)
        -   [[3.4.1] [Missing repository.xml file]](#Missing_repository.xml_file)
            -   [[3.4.1.1] [Creating repository XML file manually]](#Creating_repository_XML_file_manually)
            -   [[3.4.1.2] [Using layman-overlay-maker utility]](#Using_layman-overlay-maker_utility)
        -   [[3.4.2] [Enabling the repository]](#Enabling_the_repository)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Features]

While the [[eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository")] eselect module supersedes [layman] for listing, configuring, and handling synchronization of ebuild repositories, [[[app-portage/layman]](https://packages.gentoo.org/packages/app-portage/layman)[]] users can manage their ebuild repositories (overlays) in a simple, centralized manner. The [layman] provides an overview of available remote repositories and allows the user to select one or more for the system. Once selected, the user can update (similar to [emerge \--sync]), add, remove, display and information about the overlays.

Versions greater than 2.1.0 are improved with a [plug-in sync system](https://gitweb.gentoo.org/data/gentoo-news.git/plain/2015-02-04-portage-sync-changes/2015-02-04-portage-sync-changes.en.txt?id=2c5c3a82795da5d340bd4ccd3e2c9b14ab25b82d).

** Note**\
Although not all features of **plug-in sync system** of [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") are supported yet from [layman] the [migration of Portage](https://wiki.gentoo.org/wiki/Project:Portage/Sync#Migration "Project:Portage/Sync") is a good step to be prepared for that.

## [Installation]

### [USE flags]

Cannot load package information. Is the atom *app-portage/layman* correct?

The `sync-plugin-portage` and `git` USE flags are especially important in newer versions of [layman].

[FILE] **`/etc/portage/package.use/layman`Add important USE flags**

    app-portage/layman sync-plugin-portage git

Please refer to [portage projects page](https://wiki.gentoo.org/wiki/Project:Portage/Sync#Layman_configuration "Project:Portage/Sync").

### [Emerge]

Next install the [layman] package:

`root `[`#`]`emerge --ask app-portage/layman`

### [Configuration]

Layman will create its configuration file in [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")/].

Configure [layman] to use the [repos.conf] method in [/etc/layman/layman.cfg]. New installations of [layman] will probably have this already set correctly:

[FILE] **`/etc/layman/layman.cfg`**

    # Repository config types used by layman
    # (repos.conf, make.conf)
    conf_type : repos.conf

Create the [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")/] directory if it does not exist yet:

`root `[`#`]`mkdir `[`/etc/portage/repos.conf`](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")

If you have [layman] version 2.3.0 or greater installed, you can force a rebuild of [layman]\'s [repos.conf] files:

`root `[`#`]`layman-updater -R`

## [Usage]

### [Basic invocations]

The [layman] [man page](https://wiki.gentoo.org/wiki/Man_page "Man page") (see [External resources](#External_resources)) provides a full overview of the available functions. However, for most users, the following commands suffice for repository management activities.

To fetch and display a list of all the repositories available through official references:

`root `[`#`]`layman -L`

To add a repository in the list generated by the local list:

`root `[`#`]`layman -a <name>`

To add an unofficial repository:

`root `[`#`]`layman -o <url of repository xml file> -f -a <name>`

To remove a repository from the local list:

`root `[`#`]`layman -d <name>`

To update a specific repository:

`root `[`#`]`layman -s <name>`

To update all repositories:

`root `[`#`]`layman -S`

### [Mountable repositories with layman-mounter]

Since the release of [layman] version 2.2.0, support for [squashfs](https://wiki.gentoo.org/wiki/SquashFS "SquashFS") repository types has been included. [layman] will interact with squashfs repository by mounting them as read-only on the [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem"). On the initial install of the squashfs repository, it will be mounted as read-only. However, after a reboot the repository will no longer be mounted and the ebuilds in that repository will not be accessible by the system.

In order to assist users in handling these mountable repositories, a utility was added that goes by the name of [layman-mounter].

To find all repositories that are currently mounted, type:

`root `[`#`]`layman-mounter -l`

To find all repositories installed by [layman] that can be mounted, type:

`root `[`#`]`layman-mounter -L`

To mount the mountable repositories, type:

`root `[`#`]`layman-mounter -m <name>`

To unmount the repositories, type:

`root `[`#`]`layman-mounter -u <name>`

### [Setting repository priorities with Layman]

As each [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") is assigned a unique priority, [layman] provides a simple way of defining priorities for repositories it manages. For more information about repository priorities see the [ebuild repository priorities](https://wiki.gentoo.org/wiki/Ebuild_repository#Priorities "Ebuild repository").

The file [/var/lib/layman/installed.xml] contains some information about the repositories, among which is the priority attribute in the repo tag. The number there determines only the priority relative to the other repository entries, 50 is the default value. Larger numbers take priority over smaller numbers. Layman then analyses this file and sets the order of the repository entries in the `PORTDIR_OVERLAY` variable defined in [/var/lib/layman/make.conf].

As the file [/var/lib/layman/make.conf] is automatically generated by layman based on the settings in [/var/lib/layman/installed.xml], it is strongly recommended that only [/var/lib/layman/installed.xml] is used to set the priorities.

To add a personal repository, and to ensure that the repository has a higher priority, add the repository *before* [/var/lib/layman/make.conf] is sourced.

[FILE] **`/var/lib/layman/make.conf`Example layman overlays setting**

    PORTDIR_OVERLAY="
    /home/jdoe/gamerlay
    /var/lib/layman/lisp
    /var/lib/layman/Spring
    $" #the variable defined in /etc/portage/make.conf is now expanded
                        #when /var/lib/layman/make.conf is sourced in /etc/portage/make.conf

However, this can be also \"fooled\" by defining the `PORTDIR_OVERLAY` in [/etc/portage/make.conf] *after* [/var/lib/layman/make.conf] has been sourced.

[FILE] **`/etc/portage/make.conf`Custom repository setting**

    source /var/lib/layman/make.conf #this sources the PORTDIR_OVERLAY variable defined by layman.
                                     #however, the variable expanded by layman was empty
    PORTDIR_OVERLAY="/home/user/overlay $ $" #now the layman defined repositories take precedence,
                                                                       #but the user defined repository still has the lowest priority

This \"trick\" is merely an opportunity offered by [shell](https://wiki.gentoo.org/wiki/Shell "Shell") variable expansion.

### [Adding custom repositories]

To add repositories which are not listed when [layman -L] is ran, find their repository XML files and add them using the `-o` option under a name specified by the `-a` option.

Example: [repositories.xml] in [brother-overlay](https://github.com/stefan-langenmaier/brother-overlay)

`root `[`#`]`layman -o `[`https://raw.github.com/stefan-langenmaier/brother-overlay/master/repositories.xml`](https://raw.github.com/stefan-langenmaier/brother-overlay/master/repositories.xml)` -f -a brother-overlay`

#### [Missing repository.xml file]

In some cases the custom repository does not provide a repository XML file.

##### [Creating repository XML file manually]

The XML file can be created manually in the [/etc/layman/overlays] folder.

For example, if [Larry the cow](https://wiki.gentoo.org/wiki/Larry_the_cow "Larry the cow") were to create his repository:

[FILE] **`/etc/layman/overlays/larry.xml`Larry the cow\'s nginx overlay**

    <?xml version="1.0" ?>

    <repositories version="1.0">
        <repo priority="50" quality="experimental" status="unofficial">
            <name>larry</name>
            <description>nginx server for the barn computer from Larry the cow.</description>
            <homepage>https://github.com/gentoo/nginx-overlay</homepage>
            <owner>
                <email>larry@gentoo.org</email>
            </owner>
            <source type="git">https://github.com/gentoo/nginx-overlay.git</source>
        </repo>
    </repositories>

##### [Using layman-overlay-maker utility]

With the addition of [layman] version 2.2.0 a new utility was added to assist users in this process that goes by the name of [layman-overlay-maker]. As long as the overlay information has been properly added via the prompts, [layman-overlay-maker] will create a XML defined overlay and save into [/etc/layman/overlays] or the specified in the layman configuration file for *overlay_defs*.

[layman-overlay-maker] can become a useful tool in assisting users who would like to submit a patch to have their overlays added to the official [repositories.xml] file.

To use the utility simply invoke it by name:

`root `[`#`]`layman-overlay-maker`

and go through its prompts until completion.

#### [Enabling the repository]

When finished rebuild the [repos.conf] using [layman-updater]:

`root `[`#`]`layman-updater -R`

Now you can add the custom repository by:

`root `[`#`]`layman -a <name>`

where `name` is the name of the repository that was created.

## [See also]

-   [Eselect/Repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") --- an [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect") module for configuring [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage").
-   [Overlay user guide](https://wiki.gentoo.org/wiki/Project:Overlays/Overlays_guide "Project:Overlays/Overlays guide")
-   [Ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- a file-structure that can provide packages for installation on a Gentoo system.

## [External resources]

-   The Layman man page locally ([man layman]) or online [at Sourceforge.net](http://layman.sourceforge.net/)