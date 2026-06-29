[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Minimizing_compilation_and_installation_time&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Most packages will install very quickly on reasonably fast modern hardware, but there are heavier packages, and a few very large ones. Here are some tips to minimize compilation and installation times on Gentoo.

Note that not all packages are compiled, in the usual sense: many are written in interpreted langues such as [Python](https://wiki.gentoo.org/wiki/Python "Python") and do not always use a heavy build process. Some packages are installed directly in a precompiled \"binary\" format.

** Tip**\
When installing software, use the `--ask --verbose` (`-av`) options and inspect the dependencies that would be pulled in for any large packages that could be replaced by a -bin version, or may even not be needed at all.

## Contents

-   [[1] [Avoid unneeded packages]](#Avoid_unneeded_packages)
    -   [[1.1] [QtWebEngine]](#QtWebEngine)
-   [[2] [Configure portage to optimize build times]](#Configure_portage_to_optimize_build_times)
-   [[3] [Select compiler options for compilation speed]](#Select_compiler_options_for_compilation_speed)
-   [[4] [Alternative binary packages (\"-bin\" packages)]](#Alternative_binary_packages_.28.22-bin.22_packages.29)
    -   [[4.1] [Substituting a source based dependency for \"-bin\" version]](#Substituting_a_source_based_dependency_for_.22-bin.22_version)
-   [[5] [Make binary packages on a secondary machine]](#Make_binary_packages_on_a_secondary_machine)
-   [[6] [Hardware]](#Hardware)
-   [[7] [Put Portage TMPDIR on tmpfs]](#Put_Portage_TMPDIR_on_tmpfs)
-   [[8] [Tips]](#Tips)
    -   [[8.1] [\--newuse vs \--changed-use]](#--newuse_vs_--changed-use)
-   [[9] [See also]](#See_also)

## [Avoid unneeded packages]

Installing software often pulls in dependencies, and some of these dependencies may be large packages. Inspect what will be installed when [emerging](https://wiki.gentoo.org/wiki/Emerge "Emerge"), and adjust [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") to avoid any unneeded dependencies, if possible.

### [QtWebEngine]

[QtWebEngine](https://wiki.gentoo.org/wiki/QtWebEngine "QtWebEngine") is a particularly large package that takes a long time to compile. Some packages will pull it in as a dependency by default, but this is not always required or desired.

To avoid having to compile [[[dev-qt/qtwebengine]](https://packages.gentoo.org/packages/dev-qt/qtwebengine)[]] as a dependency for certain packages, add `-webengine` to [make.conf]:

[FILE] **`/etc/portage/make.conf`**

    USE="pulseaudio -webengine -bluetooth bash-completion"

For some packages, the `gui, urlpreview, rss, qt5, pyqt5, dictionary-manager` and maybe other USE flags determine QtWebEngine dependency, so it may be useful to watch if theses flags are needed [for certain packages](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use") or not.

If QtWebEngine has already been pulled in as a dependency, and may now be removed, execute the following commands after modifying [make.conf]:

`root `[`#`]`emaint sync --auto`

`root `[`#`]`emerge --ask --verbose --update --deep --newuse @world`

`root `[`#`]`emerge --ask --depclean`

Some packages depend unconditionally on QtWebEngine. If these packages are not needed, simply avoid installing them!

** Tip**\
For anyone wanting to be absolutely certain to avoid emerging QtWebEngine, consider adding it to [/etc/portage/package.mask](https://wiki.gentoo.org/wiki//etc/portage/package.mask "/etc/portage/package.mask").

## [Configure portage to optimize build times]

Portage should be configured to use resources in a reasonable manner, in order to achieve the best possible build times. Generally things will be set up to use all processing threads available, memory capacity permitting.

Portage niceness may be set to allow using the system while Portage is merging packages, while minimally impacting build time.

The main variables to pay attention to are [EMERGE_DEFAULT_OPTS](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS "EMERGE DEFAULT OPTS") and [MAKEOPTS](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS").

See [Portage niceness](https://wiki.gentoo.org/wiki/Portage_niceness "Portage niceness") to set up Portage to let other processes be given priority, to allow full use of the system while installing or updating packages.

## [Select compiler options for compilation speed]

Some [CFLAGS](https://wiki.gentoo.org/wiki/CFLAGS "CFLAGS") such as `-pgo` will result in much longer compile times. The `pgo` USE flag has the same effect.

## [][Alternative binary packages (\"-bin\" packages)]

Some packages have a precompiled alternative, provided by the Gentoo developers. These allow fast installation of packages that otherwise take a particularly long time to compile. Note that the \"-bin\" packages referred to here are precompiled versions of packages available in the [Ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") - there are also binary packages in the repository for other reasons, such as for software that is only available in binary form.

The devs pay great attention to building these versions, there is usually no noticeable performance hit to using them, though usually any difference one way or the other is negligible.

For packages that have [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), the \"-bin\" versions use common defaults. If it is required to change the USE flags for a package, a \"-bin\" version may not be appropriate, though it is uncommon to have to do so.

** Tip**\
These packages are particularly expensive to compile:

-   [Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium")
-   [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox")
-   [LibreOffice](https://wiki.gentoo.org/wiki/LibreOffice "LibreOffice")
-   [Rust](https://wiki.gentoo.org/wiki/Rust "Rust")

### [][Substituting a source based dependency for \"-bin\" version]

When installing a package would pull in a large package that would advantageously be replaced by it\'s \"-bin\" version, it is possible to substitute the former for the latter.

When noticing a large packing being pulled in as a dependency, first abort the merge before starting. Then emerge the \"-bin\" version without adding it to the [world file](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)"):

`root `[`#`]`emerge --oneshot <category>/-bin`

Because dependencies on packages that have a \"-bin\" version are virtual, simply emerge the original package, and the \"-bin\" version will be used as the dependency.

** Important**\
Remember [not to add dependencies to the world file](https://wiki.gentoo.org/wiki/Emerge#Do_not_add_dependencies_to_the_world_file "Emerge").

## [Make binary packages on a secondary machine]

If another, maybe more powerful, machine is available, it could be set up to build [binary packages](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") to be used on the first machine with a [binhost](https://wiki.gentoo.org/wiki/Binary_package_guide#Setting_up_a_binary_package_host "Binary package guide"). Packages built this way may be shared among several machines, if they share the same architecture and use similar [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

## [Hardware]

Of course, more powerful hardware will allow faster compilation times, though it will usually also be the most cumbersome and expensive way to make things faster. Some upgrades may be reasonable though, such as adding RAM on a memory limited machine (it\'s generally advised to have two GB per processor thread). Some systems have cheaper memory sticks available to them than others however.

An [SSD](https://wiki.gentoo.org/wiki/SSD "SSD"), particularly an [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe") SSD, can sometimes be a reasonably cheap way to make installation faster, if coming from a traditional spinning hard drive.

## [Put Portage TMPDIR on tmpfs]

It is possible to have [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") build packages in RAM with [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs") instead of using a [Hard Disk Drive](https://wiki.gentoo.org/wiki/HDD "HDD") (HDD) or [Solid State Drive](https://wiki.gentoo.org/wiki/SSD "SSD") (SSD). This can sometimes speed up emerge times, for those who have enough RAM. See the [Portage TMPDIR on tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs") article.

## [Tips]

### [\--newuse vs \--changed-use]

The `--changed-use` parameter may be used to do less rebuilds while updating. Using the `--newuse` parameter however will let installed packages better reflect the state of the current [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository").

## [See also]

-   [ccache](https://wiki.gentoo.org/wiki/Ccache "Ccache") --- helps avoid repeated recompilation for the same C and C++ object files by fetching the result from a cache directory.
-   [distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") --- a program designed to distribute compiling tasks across a network to participating hosts.
-   [genlop](https://wiki.gentoo.org/wiki/Genlop "Genlop") --- a utility for extracting information about emerged ebuilds from Portage log files - show build times
-   [Portage with Git](https://wiki.gentoo.org/wiki/Portage_with_Git "Portage with Git") --- use [Git](https://wiki.gentoo.org/wiki/Git "Git") to synchronize the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository")
-   [qlop](https://wiki.gentoo.org/wiki/Q_applets#Extracting_information_from_emerge_logs_.28qlop.29 "Q applets") - q applets are fast Portage query utilities written in C, show build times with qlop