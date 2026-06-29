**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only. *Page archived as of **2021-10-21**.*

\
TLDR: **Do not use this article!**

** Note**\
Paludis has been removed from the Gentoo tree since nobody maintained it. This page is here for historical context.

** Note**\
An unofficial fork with patches for newer Gentoo ebuild formats (EAPIs) is available [here](https://github.com/MageSlayer/paludis-gentoo-patches).

**Resources**

[[]][Home](http://paludis.exherbolinux.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/List_of_software_package_management_systems#Linux "wikipedia:List of software package management systems")

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/paludis)

[[]][GitLab](https://gitlab.exherbo.org/paludis/paludis/)

[[]][Official documentation](http://paludis.exherbo.org/configuration/index.html)

[[]][Bugs (Gentoo)](https://bugs.gentoo.org/buglist.cgi?quicksearch=sys-apps%2Fpaludis&list_id=2882420)

[[]][Bugs (upstream)](http://paludis.exherbo.org/trac/)

Paludis is a multi-format package manager and an alternative to Portage.

Paludis is the official package manager of Exherbo Linux and was written by former Gentoo developer Ciaran McCreesh.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Basics and installing a package]](#Basics_and_installing_a_package)
    -   [[3.2] [Uninstall a package]](#Uninstall_a_package)
    -   [[3.3] [Update world]](#Update_world)
    -   [[3.4] [Install a repository]](#Install_a_repository)
    -   [[3.5] [Sync all repositories]](#Sync_all_repositories)
    -   [[3.6] [Post-configure a package]](#Post-configure_a_package)
    -   [[3.7] [Tell the resolver how much work it should perform]](#Tell_the_resolver_how_much_work_it_should_perform)
    -   [[3.8] [Keep output logs]](#Keep_output_logs)
    -   [[3.9] [Make Paludis quiet]](#Make_Paludis_quiet)
    -   [[3.10] [Speed up cave-search]](#Speed_up_cave-search)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Subslots]](#Subslots)
    -   [[4.2] [Clang]](#Clang)
    -   [[4.3] [Gentoo rsync mirrors]](#Gentoo_rsync_mirrors)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

Refer to the Paludis guide for instructions on how to install Paludis and set up the basic configuration.

## [Configuration]

This section gives an overview on where to configure various things in Paludis.

-   [Toolchain and environmental package behavior](http://paludis.exherbo.org/configuration/bashrc.html): [/etc/paludis/bashrc]
-   [Keywords](http://paludis.exherbo.org/configuration/keywords.html) (allowing packages from unstable branch): [/etc/paludis/keywords.conf] or [/etc/paludis/keywords.conf.d/\*.conf]
-   [USE flags](http://paludis.exherbo.org/configuration/use.html) (enabling package features): [/etc/paludis/use.conf] or [/etc/paludis/use.conf.d/\*.conf]
-   [Licenses](http://paludis.exherbo.org/configuration/licenses.html): [/etc/paludis/licenses.conf] or [/etc/paludis/licenses.conf.d/\*.conf]
-   [Package (un)masks](http://paludis.exherbo.org/configuration/packagemask.html): [/etc/paludis/package_mask.conf] or [/etc/paludis/package_mask.conf.d/\*.conf] and [/etc/paludis/package_unmask.conf] or [/etc/paludis/package_unmask.conf.d/\*.conf] respectively
-   [Hooks](http://paludis.exherbo.org/configuration/hooks.html): various subdirectories of [/etc/paludis/hooks/]
-   [Output and log behavior](http://paludis.exherbo.org/configuration/output.html): [/etc/paludis/output.conf]

## [Usage]

This section tries to give a concise usage overview and may serve as a quick lookup reference. However, it does not and will not replace the [official documentation](http://paludis.exherbo.org).

### [Basics and installing a package]

The most basic form is:

`root `[`#`]`cave resolve <category>/`

This will try to solve the dependencies and print out the results. It will **not** actually perform the resolution (as in: install the target package). To actually carry out the resolution we would have to pass the `-x` option. You should only do that if you know what you are doing, because paludis is truly non-interactive and will not ask in between. The more common workflow is to save the resolution information in a so called resume file, review the changes that would be performed (like installing and uninstalling packages) and then execute them:

`root `[`#`]`cave resolve --resume-file ~/cave_resume <category>/ `

`root `[`#`]`# review resolution on stdout `

`root `[`#`]`cave resume --resume-file ~/cave_resume `

It may make sense to create aliases for these commands in your favorite shell.

To perform dependency resolution and instantly carry out the results (if possible), you would do:

`root `[`#`]`cave resolve -x <category>/`

It is also possible to pass both `-x` and `--resume-file`.

The resume state also allows us to resume compilations/installations we have aborted or which have failed.

Not only the [resolve] subcommand behaves this way. Refer to the man page of a particular subcommand to get more detailed information.

All further commands in this section will omit the `-x` and the `--resume-file` options (if applicable) and will leave it up to the user which one to choose (or none).

** Note**\
You can omit the `category/` part, in which case Paludis will try to look it up.

### [Uninstall a package]

Either this way:

`root `[`#`]`cave uninstall <category>/`

or the following way, which lets you combine it with installation of packages:

`root `[`#`]`cave resolve \!<category>/`

If you want to uninstall all unneeded packages, do

`root `[`#`]`cave purge`

### [Update world]

`root `[`#`]`cave resolve -c world`

### [Install a repository]

If you have configured unavailable eselect-repository repositories, then you should be able to install repositories just like regular packages.

`root `[`#`]`cave resolve <repository-name>`

If the repository name could be ambiguous with a package name, then you can tell cave explicitly that this is a repository:

`root `[`#`]`cave resolve repository/<repository-name>`

### [Sync all repositories]

`root `[`#`]`cave sync`

### [Post-configure a package]

Some ebuilds have a [pkg_config phase](https://dev.gentoo.org/~ulm/pms/head/pms.html#x1-1080009.1.14) which allows post-install configuration for packages.

A lot of ebuilds might output something like this:

     * In order to update your hddtemp database, run:
     * emerge --config =app-admin/hddtemp-0.3_beta15-r7

Since we don\'t use Portage, we have to do this instead for the above case:

`root `[`#`]`cave config =app-admin/hddtemp-0.3_beta15-r7`

### [Tell the resolver how much work it should perform]

There are three main options that change the default behavior:

  ----------------------- ------------------------------------------------------------------------------------------------------------------------------------------
  Option                  Description
  `-z` (`--lazy`)         Does as little work as possible, typically used when quickly installing a single package only.
  `-c` (`--complete`)     Does all optional work, typically used when updating the \'world\' set.
  `-e` (`--everything`)   Does all optional work and always re-installs, typically used when you want to rebuild everything after a major gcc upgrade for example.
  ----------------------- ------------------------------------------------------------------------------------------------------------------------------------------

If none of the above options are passed, then the default behavior is roughly in between [\--lazy] and [\--complete]. These options are in fact just shorthands for more fine-grained options. Check the man page of [cave-resolve] for additional information on this subject.

### [Keep output logs]

Add the following file:

[FILE] **`/etc/paludis/output.conf`**

    always_keep_output_logs = true

### [Make Paludis quiet]

Add the following file:

[FILE] **`/etc/paludis/output.conf`**

    quiet = true

### [Speed up cave-search]

[cave search] can make use of a search index, similar to what [eix] does. First, we have to generate the index:

`root `[`#`]`cave manage-search-index --create ~/cave-search-index`

And then we can use it:

`root `[`#`]`cave search --index ~/cave-search-index `

## [Troubleshooting]

### [Subslots]

Although subslot handling in Paludis technically meets the spec, it misbehaves from a user perspective. Paludis will not pull in installed packages with mismatched subslots into the depgraph which are not part of the resolution, nor does it allow the user to easily do that. There exist various hacks and scripts to work around that. Another way is to pass [-D dev-libs/foo] if installed dependant packages of foo use an older subslot than the one that is about to be installed. However, that will also reinstall packages that are not affected. Also see the [upstream bug report](http://paludis.exherbo.org/trac/ticket/1312).

### [Clang]

Paludis frequently fails to build with Clang. Your best bet is to use the stable gentoo releases which have a better chance of containing a patch. The live ebuild will most likely fail to build.

### [Gentoo rsync mirrors]

Some rsync gentoo mirrors are out of date and don\'t run rsync-3.1 yet. These [cause trouble](http://paludis.exherbo.org/trac/ticket/1327). You can either overwrite the default rsync syncer with your own [syncer](http://paludis.exherbo.org/configuration/syncers.html) or pick a gentoo mirror that works properly.

## [See also]

-   [Pkgcore](https://wiki.gentoo.org/wiki/Pkgcore "Pkgcore") --- an alternative package manager for Gentoo that aims for high performance, extensibility, and a clean design.
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.

## [External resources]

-   [http://paludis.exherbo.org/faq/howdoi.html](http://paludis.exherbo.org/faq/howdoi.html) - FAQ: How do I \...?
-   [http://exherbo.org/](http://exherbo.org/) - Exherbo Linux.
-   [http://zaufi.github.io/my-paludis-hooks-and-addons.html](http://zaufi.github.io/my-paludis-hooks-and-addons.html)