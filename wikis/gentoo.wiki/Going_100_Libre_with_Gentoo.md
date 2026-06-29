Achieving a computing environment composed entirely of [free software](https://www.gnu.org/philosophy/free-sw.html) presents significant challenges in modern computing. Consequently, few contemporary operating system distributions meet this standard. As of 2025, the GNU Project recognizes [eight GNU/Linux distributions](https://www.gnu.org/distros/free-distros.html) as being completely free. These distributions exclusively include the Linux-libre kernel and do not provide access to non-free software repositories.

However, many of these GNU-endorsed distributions may exhibit limitations, such as a lack of certain modern features, a higher incidence of bugs attributable to smaller user bases, or being primarily binary-based, which can restrict user configurability compared to source-based distributions.

Most other GNU/Linux distributions typically include non-free kernel blobs and provide repositories containing proprietary software. Some distributions also pre-install proprietary applications such as text editors, game launchers, or web browsers.

While Gentoo Linux is not recognized by the GNU Project as a fully free distribution out-of-the-box, primarily due to the inclusion of build recipes for proprietary software in its default overlay, it can be configured to meet the GNU Free System Distribution Guidelines (GNU FSDG) with specific modifications. Gentoo\'s emphasis on user choice and its source-based nature make it a notable non-FSDG distribution that can be tailored to be completely composed of free software.

## Contents

-   [[1] [Boot Firmware]](#Boot_Firmware)
    -   [[1.1] [Libreboot]](#Libreboot)
    -   [[1.2] [GNU Boot and Canoeboot]](#GNU_Boot_and_Canoeboot)
-   [[2] [Configuring Gentoo for Free Software Only]](#Configuring_Gentoo_for_Free_Software_Only)
    -   [[2.1] [Restricting Software Licenses]](#Restricting_Software_Licenses)
    -   [[2.2] [USE Flags for Enhanced Freedom and Privacy]](#USE_Flags_for_Enhanced_Freedom_and_Privacy)
-   [[3] [Kernel and Firmware]](#Kernel_and_Firmware)
-   [[4] [Software Packages with Potential Freedom Issues]](#Software_Packages_with_Potential_Freedom_Issues)
-   [[5] [Web Browsers and Free Software]](#Web_Browsers_and_Free_Software)
    -   [[5.1] [GNU IceCat]](#GNU_IceCat)
    -   [[5.2] [LibreWolf]](#LibreWolf)

## [Boot Firmware]

Most contemporary computers are equipped with proprietary boot firmware. These systems often include embedded subsystems like the [Intel Management Engine (ME)](https://en.wikipedia.org/wiki/Intel_Management_Engine) in [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") processors and the [AMD Platform Security Processor (PSP)](https://en.wikipedia.org/wiki/AMD_Platform_Security_Processor) in [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") processors. Both the Free Software Foundation (FSF) and the Electronic Frontier Foundation (EFF) have raised concerns about these subsystems, characterizing them as potential low-level backdoors.

These embedded subsystems may have the capability to access system memory and can operate autonomously as long as the motherboard receives power, irrespective of the computer\'s power state (on or off). They can potentially access all hardware components, including webcams, microphones, and network interfaces. On many systems, disabling these technologies is not possible without replacing the stock firmware with a fully free boot firmware alternative, such as GNU Boot or Canoeboot.

### [Libreboot]

[Libreboot](https://libreboot.org/) was historically a prominent completely free boot firmware based on [Coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot"). However, its status regarding complete freedom, as defined by strict free software advocates, changed in January 2022. The project\'s maintainer announced a [policy shift](https://libreboot.org/news/policy.html) towards reducing binary blobs in the firmware rather than strictly excluding them. This approach aimed to broaden hardware support for Libreboot, particularly for more recent systems. This decision, however, meant that Libreboot would no longer be considered fully free by the GNU Project. Forks of Libreboot exist that continue to adhere to the goal of being entirely free of proprietary blobs.

### [GNU Boot and Canoeboot]

Following Libreboot\'s policy change, [GNU Boot](https://www.gnu.org/software/gnuboot/web/) was established as a fork, aiming to maintain a version of the firmware that is entirely free of proprietary binary blobs, in line with the GNU Project\'s standards. The maintainer of Libreboot has expressed a negative view of GNU Boot. Subsequently, the maintainer of Libreboot project initiated another version intended to be fully free, named [Canoeboot](https://canoeboot.org/).

Both GNU Boot and Canoeboot are developed to comply with the [GNU Free System Distribution Guidelines (GNU FSDG)](https://www.gnu.org/distros/free-system-distribution-guidelines.html). As such, they are considered fully free software by the GNU Project.

## [Configuring Gentoo for Free Software Only]

To configure a Gentoo system to exclusively use free software, modifications to Portage, Gentoo\'s package manager, are necessary. These are primarily managed through the [make.conf] file and USE flags.

### [Restricting Software Licenses]

The `ACCEPT_LICENSE` variable in [/etc/portage/make.conf] controls which software licenses are permissible on the system. To allow only free software as defined by the GNU Project, the following setting can be used:

[FILE] **`/etc/portage/make.conf`Allowing only free software licenses**

    ACCEPT_LICENSE="-* @FREE"

This configuration permits licenses part of the [\@FREE](https://wiki.gentoo.org/wiki/License_groups#Metasets "License groups") group (which generally aligns with FSF and OSI approved licenses) and explicitly disallows any other license.

Further refinement can be achieved by excluding specific licenses. For instance, some users may choose to disallow:

-   `-`[`Artistic`](https://gitweb.gentoo.org/repo/gentoo.git/plain/licenses/Artistic) (Artistic License 1.0): While considered free by projects like Debian, [the FSF has expressed concerns](https://www.gnu.org/licenses/license-list.html#ArtisticLicense) about the license.
-   `-`[`NPSL-0.95`](https://gitweb.gentoo.org/repo/gentoo.git/plain/licenses/NPSL-0.95) ([Nmap](https://wiki.gentoo.org/wiki/Nmap "Nmap") Public Source License version 0.95): This license is not considered free by some due to its non-commercial clauses.

Gentoo provides various [License groups](https://wiki.gentoo.org/wiki/License_groups "License groups"). The [FSF-APPROVED](https://wiki.gentoo.org/wiki/License_groups/FSF-APPROVED "License groups/FSF-APPROVED") group may also be relevant for users seeking strict adherence to FSF licensing guidelines.

### [USE Flags for Enhanced Freedom and Privacy]

USE flags in Gentoo control compile-time options for packages, enabling fine-grained customization. Several USE flags are pertinent to creating a fully free system and enhancing user privacy:

-   [[[eme-free]](https://packages.gentoo.org/useflags/eme-free)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]: Enabling this flag aims to remove support for Encrypted Media Extensions (EME) related proprietary Digital Rights Management (DRM) blobs from web browsers and email clients like [Mozilla Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") and [Thunderbird](https://wiki.gentoo.org/wiki/Thunderbird "Thunderbird").
-   [[[-proprietary-codecs]](https://packages.gentoo.org/useflags/proprietary-codecs)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]: Disabling this flag globally prevents the inclusion of support for proprietary audio and video codecs in multimedia software like [FFmpeg](https://wiki.gentoo.org/wiki/FFmpeg "FFmpeg"). A list of free codecs is available on [Wikipedia](https://en.wikipedia.org/wiki/List_of_open-source_codecs).
-   [[[-telemetry]](https://packages.gentoo.org/useflags/telemetry)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]: Disabling this flag removes telemetry or data collection features from various programs, which can enhance user privacy.

These USE flags can be set globally in [/etc/portage/make.conf]:

[FILE] **`/etc/portage/make.conf`USE flags for a free system**

    USE="eme-free -proprietary-codecs -telemetry"

It is also possible to set these flags on a per-package basis in [/etc/portage/package.use].

## [Kernel and Firmware]

A standard [Linux kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") contains proprietary binary blobs, often necessary for hardware functionality. To achieve a fully free system, a deblobbed kernel, such as Linux-libre, is required. Instructions for this process within Gentoo are typically available under [Kernel/Deblobbing](https://wiki.gentoo.org/wiki/Kernel/Deblobbing "Kernel/Deblobbing").

Hardware firmware is often managed separately from the kernel. In Gentoo, the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package provides firmware files. By default, this package includes non-free firmware and thus will not install if `ACCEPT_LICENSE="@FREE -*"` is set without further configuration.

For hardware that requires firmware to function, it is crucial to ensure only free firmware is installed. The [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package can be configured to exclude non-free elements using a USE flag. This is done by adding the following line to a file within [/etc/portage/package.use/] (e.g., [/etc/portage/package.use/linux-firmware]):

[FILE] **`/etc/portage/package.use/linux-firmware`Ensuring free firmware for linux-firmware**

    sys-kernel/linux-firmware -redistributable

The [[[-redistributable]](https://packages.gentoo.org/useflags/redistributable)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag for this package is intended to exclude firmware that is non-free or has redistribution restrictions. After this configuration, the package can be installed:

`root `[`#`]`emerge --ask --verbose sys-kernel/linux-firmware`

## [Software Packages with Potential Freedom Issues]

Even when a package is distributed under a free software license, it may contain or link to non-free components, or exhibit behaviors that conflict with the GNU Free System Distribution Guidelines (FSDG). An example is [[[dev-qt/qtwebengine]](https://packages.gentoo.org/packages/dev-qt/qtwebengine)[]], which has been [reported to include proprietary codecs derived from Chromium](https://lists.nongnu.org/archive/html/gnu-linux-libre/2018-04/msg00001.html).

Users aiming for the strictest adherence to free software principles should consult resources that identify such problematic software. Relevant lists include:

-   LibrePlanet\'s [list of software that does not respect the FSDG](https://libreplanet.org/wiki/List_of_software_that_does_not_respect_the_Free_System_Distribution_Guidelines).
-   Parabola GNU/Linux-libre\'s [blacklist of software with freedom issues](https://git.parabola.nu/abslibre/blacklist.git/tree/blacklist.txt).

## [Web Browsers and Free Software]

Web Browsers presents particular challenges regarding non-free software and user privacy. Many websites utilize non-free JavaScript for tracking and other functionalities, which can compromise user freedom and privacy.

While popular web browsers like [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] and [[[www-client/chromium]](https://packages.gentoo.org/packages/www-client/chromium)[]] are themselves licensed under free licenses, concerns are often raised about their default configurations, bundled extensions, or policies regarding user freedom and privacy.

### [GNU IceCat]

[GNU IceCat](https://wiki.gentoo.org/wiki/GNU_Icecat "GNU Icecat") is a web browser recognized by the GNU Project as fully free software. It is a fork of the Firefox Extended Support Release (ESR). GNU IceCat includes privacy-enhancing features and modifications to align with free software principles. However, some users may find its bundled addons, such as LibreJS (which blocks non-free, non-trivial JavaScript), to be restrictive, though alternatives like uBlock Origin can provide different approaches to content blocking. These bundled addons can typically be managed or disabled via the `about:addons` page. GNU IceCat defaults to using [Mozzarella](https://gnuzilla.gnu.org/mozzarella/), a repository of free addons, instead of the standard Mozilla Add-ons store, which hosts non-free addons. While Mozzarella may not be as up-to-date as the main Mozilla store, users can configure IceCat to use the latter if they choose, though this may introduce non-free software.

### [LibreWolf]

[LibreWolf](https://wiki.gentoo.org/wiki/LibreWolf "LibreWolf") is another free web browser, forked from Firefox, designed with a focus on privacy and freedom. It aims to remove DRM blobs and telemetry, and includes tracking protection by default. An official [Gentoo overlay](https://codeberg.org/librewolf/gentoo) is available for LibreWolf. When combined with tools like uBlock Origin and by selectively enabling JavaScript, users can achieve a high degree of free software adherence and privacy. However, the Free Software Foundation (FSF) does not endorse LibreWolf, primarily because it defaults to using the standard Firefox Add-ons store, which contains non-free addons.