This page attempts to summarize the **benefits of Gentoo** as viewed by its users, with regards to other Linux distributions.

Gentoo is an exceptionally stable, powerful, and flexible distribution that leverages installing from source code to provide functionality that would be hard to achieve with a binary-based system.

To use Gentoo requires some in-depth knowledge of the system, so be prepared to spend time reading and learning before choosing Gentoo.

** See also**\
[Please note that there are several pages that provide information about Gentoo Linux.] See the page on the website [about Gentoo](https://www.gentoo.org/get-started/about/), the [philosophy of Gentoo](https://www.gentoo.org/get-started/philosophy/), and the [FAQ on what makes Gentoo different](https://wiki.gentoo.org/wiki/FAQ#What_makes_Gentoo_different.3F "FAQ"). The [handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/About "Handbook:AMD64/Installation/About") also has a section about Gentoo.

## Contents

-   [[1] [Community]](#Community)
-   [[2] [Efficiency]](#Efficiency)
-   [[3] [Flexibility]](#Flexibility)
-   [[4] [Extensibility]](#Extensibility)
-   [[5] [Scalability]](#Scalability)
-   [[6] [Security]](#Security)
-   [[7] [Software development]](#Software_development)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)

## [Community]

-   Due to the structure of the Gentoo system, Gentoo\'s user community tends to be relatively knowledgeable about low-level aspects of Linux (build processes, kernel configuration, hardware support).
-   Gentoo has fostered one of the most helpful communities of any Linux distribution: there are almost a thousand users in the [[#gentoo](ircs://irc.libera.chat/#gentoo)] ([[webchat](https://web.libera.chat/#gentoo)]) IRC channel on Libera.Chat at any time.
-   Almost anyone can help with virtually any issue a user may have through the various [support channels](https://wiki.gentoo.org/wiki/Support "Support"). In fact anyone with some knowledge of Gentoo is encouraged to help others and [contribute](https://wiki.gentoo.org/wiki/Contributing_to_Gentoo "Contributing to Gentoo").

## [Efficiency]

-   Gentoo has a well deserved reputation for its community\'s tendency to build optimized code with demonstrable increases in efficiency over binary-based distributions\' \"one size fits all\" model, using things like [PGO](https://en.wikipedia.org/wiki/Profile-guided_optimization "wikipedia:Profile-guided optimization") and [-march=native](https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html#:~:text=This%20selects%20the,selected%20instruction%20set.).
-   Gentoo\'s \"[USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag")\" system allows the user to create an extremely \"bare-bones\" installation, removing unneeded functions from packages (e.g: removing iPod/iOS support, resulting in smaller binaries that load faster and use less memory). It is straightforward to change these compile flags at a later date, for instance when installing new hardware.
-   Not only from source compilation - some big packages are available in binary form too (for faster installing), like [Firefox](https://packages.gentoo.org/packages/www-client/firefox) and [Firefox-bin](https://packages.gentoo.org/packages/www-client/firefox-bin), [LibreOffice](https://packages.gentoo.org/packages/app-office/libreoffice) and [LibreOffice-bin](https://packages.gentoo.org/packages/app-office/libreoffice-bin).
-   Compiling from source does not necessarily imply greater complexity or difficulty of installation - the process of installing packages is similar to using the package managers of other GNU/Linux distributions, such as apt or pacman. The main noticeable difference is simply one of greater upfront installation time, particularly if not a lot of customization is being done. Just because one has the choice to wade into that complexity doesn\'t mean that one has to - the defaults are often sufficient.
-   Dependencies are very granular in Gentoo. Where many other distributions would have one large package, Gentoo will partition dependencies into elemental units. Even if cutting things up means more packages, only the ones for parts that are absolutely necessary will be installed, so this approach takes up less space overall. Dependencies will even be adjusted according to selected USE flags, so everything is always kept tight.
-   Save time when Gentoo allows some things that would require involved processes on other systems to be done easily, such as changing compile time options, or creating packages.

## [Flexibility]

-   Gentoo allows users to configure which software features they wish to install, instead of the \"one size fits all\" approach of many binary-based distributions. Choose even core components, such as the [init system](https://wiki.gentoo.org/wiki/Init_system "Init system"), or [system logger](https://wiki.gentoo.org/wiki/Logging "Logging").
-   Many compile-time options are easily configurable during installation, rather than imposed by a binary package, mainly thanks to the [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") system.
-   Gentoo can run in a wide range of environments, from embedded systems and virtual containers ([LXC](https://wiki.gentoo.org/wiki/LXC "LXC"), [OpenVZ](https://wiki.gentoo.org/wiki/OpenVZ "OpenVZ"), etc.) through to large cluster machines.
-   Gentoo favors incremental [updates](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") (instead of major upgrades every 6 months), so the latest packages are available as soon as they are ready.
-   Rather than impose a specific package, [virtual packages](https://wiki.gentoo.org/wiki/Virtual_packages "Virtual packages") allow key-functionality packages to be switched in or out.
-   Gentoo is available for a large selection of [architectures](https://www.gentoo.org/downloads/), and is particularly easy to port to new systems.
-   For many packages, several versions will be available in the repository, in case a different version is needed.
-   Where it makes sense, several versions of the same package can be installed simultaneously, thanks to [SLOTs](https://wiki.gentoo.org/wiki/SLOT "SLOT").
-   Different [branches](https://wiki.gentoo.org/wiki/Handbook:X86/Portage/Branches "Handbook:X86/Portage/Branches") can easily be mixed, when [specific versions of a package are needed](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package").

## [Extensibility]

-   Gentoo allows the use of extra [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") to provide packages not yet provided by the [main Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"). Examples of such overlays are Gentoo\'s own user repository called [GURU](https://wiki.gentoo.org/wiki/GURU "GURU"), public [third party overlays](https://repos.gentoo.org/), and local repositories on local file systems. This is similar to [PPA on Ubuntu](https://help.launchpad.net/Packaging/PPA) and [AUR on Arch](https://aur.archlinux.org/).
-   Distribution-independent package frameworks like [[[app-containers/snapd]](https://packages.gentoo.org/packages/app-containers/snapd)[]] and [[[sys-apps/flatpak]](https://packages.gentoo.org/packages/sys-apps/flatpak)[]] are available in Gentoo repository.
-   Gentoo allows the user to set up [ebuild phase hooks](https://wiki.gentoo.org/wiki//etc/portage/bashrc "/etc/portage/bashrc") to provide customization of the package installation process with personalized code.
-   It is relatively easy to add new packages to Gentoo by [writing ebuilds](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds "Basic guide to write Gentoo Ebuilds"). It is also easy to share them, as ebuild repositories are basically just a directory of files shared over the internet.

## [Scalability]

-   Due in a large part to Gentoo\'s *portage* tool\'s configurability and its source-based approach to software management, Gentoo is relatively well suited to deployment from tiny embedded systems right up to large cluster machines.
-   Gentoo allows users to easily patch almost any source-based package during build by providing a patch file in the appropriate directory within [[/etc/portage/patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches")].
-   For medium to large scale deployments, a [binhost](https://wiki.gentoo.org/wiki/Binary_package_guide#Setting_up_a_binary_package_host "Binary package guide") may be set up to deploy binary packages to each individual machine, for easy management.
-   Package management is built around a formal standard, called the [EAPI](https://wiki.gentoo.org/wiki/EAPI "EAPI"), so that any software can reliably interact with the package system. This also allows third party package managers to be created.

## [Security]

-   Due to the flexibility inherent in Gentoo\'s *Portage* tool and USE flags, Gentoo encourages users to build software with only the features they need. This decreases code size and complexity, and tends to increase security.
-   The [Hardened Gentoo](https://wiki.gentoo.org/wiki/Hardened_Gentoo "Hardened Gentoo") project focuses on increasing the security of Gentoo Linux through a variety of means.
-   Gentoo is an exceptionally stable distribution, and each package is tested thoroughly before being made available.

## [Software development]

-   Because Gentoo is source based, many software development prerequisites are installed. This includes a C-compiler, Linux kernel header files, a Python interpreter, and much more.
-   Thanks to [slotting](https://wiki.gentoo.org/wiki/SLOT "SLOT"), it is often possible to have multiple versions of packages installed at the same time, which makes testing against multiple versions of compilers, or interpreters, easy.
-   Many Gentoo packages can pull the latest \"head\" version from a [version control system](https://wiki.gentoo.org/wiki/VCS "VCS") such as git, to work on an upstream package, or if the latest version is needed for some reason.

## [See also]

-   [What makes Gentoo different?](https://wiki.gentoo.org/wiki/FAQ#What_makes_Gentoo_different.3F "FAQ") - FAQ entry about Gentoo
-   [Handbook section about Gentoo](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/About "Handbook:AMD64/Installation/About")

## [External resources]

-   [About Gentoo](https://www.gentoo.org/get-started/about/) from the main website
-   [The philosophy of Gentoo](https://www.gentoo.org/get-started/philosophy/)
-   [Gentoo Social Contract](https://www.gentoo.org/get-started/philosophy/social-contract.html)
-   [Why Choose Gentoo](https://docs.google.com/document/d/1ZO8adqz4mZ1yYtggs4Napw957nkXFsaBLgxMJbDGMic/edit) on Google Docs