**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Licenses "Project:Licenses")][Project](https://wiki.gentoo.org/wiki/Project:Licenses "Project:Licenses")

** Disclaimer:**\
We are programmers, not lawyers. Our evaluation if a particular license is a free software license is only a guideline for Gentoo developers and users. It is *not* a legal statement. There is also no guarantee that a particular `LICENSE` variable in an ebuild reflects reality. So don't rely on it, but check the license that is included with the package itself.

**License groups** enable the system\'s package manager to allow or disallow the installation of certain categories of software based on license compatibility. License groups are generally divided into categories by license compatibility with legal standards. Organizations that advocate software freedom also maintain lists of software that meets certain key criteria.

For example, The Free Software Foundation maintains their own FSF-approved list^[\[1\]](#cite_note-1)^ consisting of GPL-compatible^[\[2\]](#cite_note-2)^, GPL-incompatible^[\[3\]](#cite_note-3)^, and nonfree^[\[4\]](#cite_note-4)^ licenses.

## Contents

-   [[1] [Existing license groups]](#Existing_license_groups)
    -   [[1.1] [Free software]](#Free_software)
    -   [[1.2] [Free documents]](#Free_documents)
    -   [[1.3] [Metasets]](#Metasets)
    -   [[1.4] [Others]](#Others)
-   [[2] [When is a license a *free software license?*]](#When_is_a_license_a_free_software_license.3F)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Existing license groups]

Defined in [profiles/license_groups](https://gitweb.gentoo.org/repo/gentoo.git/tree/profiles/license_groups) (history: [CVS](https://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/profiles/license_groups?view=log), [Git](https://gitweb.gentoo.org/repo/gentoo.git/log/profiles/license_groups)).

### [Free software]

[GPL-COMPATIBLE](https://wiki.gentoo.org/wiki/License_groups/GPL-COMPATIBLE "License groups/GPL-COMPATIBLE")

[FSF-APPROVED](https://wiki.gentoo.org/wiki/License_groups/FSF-APPROVED "License groups/FSF-APPROVED")

[OSI-APPROVED-FREE](https://wiki.gentoo.org/wiki/License_groups/OSI-APPROVED#OSI-APPROVED-FREE "License groups/OSI-APPROVED")

[MISC-FREE](https://wiki.gentoo.org/wiki/License_groups/MISC-FREE "License groups/MISC-FREE")

### [Free documents]

[FSF-APPROVED-OTHER](https://wiki.gentoo.org/wiki/License_groups/FSF-APPROVED-OTHER "License groups/FSF-APPROVED-OTHER")

[MISC-FREE-DOCS](https://wiki.gentoo.org/wiki/License_groups/MISC-FREE-DOCS "License groups/MISC-FREE-DOCS")

### [Metasets]

FREE-SOFTWARE

FREE-DOCUMENTS

FREE

### [Others]

[BINARY-REDISTRIBUTABLE](https://wiki.gentoo.org/wiki/License_groups/BINARY-REDISTRIBUTABLE "License groups/BINARY-REDISTRIBUTABLE")
    -   *MUST* permit redistribution in binary form.
    -   *MUST NOT* require explicit approval (no items from \@EULA).
    -   *MUST NOT* restrict the cost of redistribution.
    -   *MAY* require explicit inclusion of the license with the distribution.
    -   IF (and only if) there is an explicit inclusion requirement, `USE=bindist` *MUST* cause a copy of the license to be installed in a file location compliant with the license.

[OSI-APPROVED-NONFREE](https://wiki.gentoo.org/wiki/License_groups/OSI-APPROVED#OSI-APPROVED-NONFREE "License groups/OSI-APPROVED")

[OSI-APPROVED](https://wiki.gentoo.org/wiki/License_groups/OSI-APPROVED "License groups/OSI-APPROVED")

[EULA](https://wiki.gentoo.org/wiki/License_groups/EULA "License groups/EULA")

[Nonfree](https://wiki.gentoo.org/wiki/License_groups/Nonfree "License groups/Nonfree")

## [][When is a license a *free software license?*]

A free software license must grant the "four freedoms" to the program's users, as described in the [free software definition](https://www.gnu.org/philosophy/free-sw.html):

0.  The freedom to run the program, for any purpose (freedom 0).
1.  The freedom to study how the program works, and change it so it does your computing as you wish (freedom 1). Access to the source code is a precondition for this.
2.  The freedom to redistribute copies so you can help your neighbor (freedom 2).
3.  The freedom to distribute copies of your modified versions to others (freedom 3). By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

[] Some tests to check whether a license is a free software license have been created by Debian (taken from their [DFSG FAQ](https://people.debian.org/~bap/dfsg-faq.html)):

-   The **"Desert island"** test. Imagine a castaway on a desert island with a solar-powered computer. This would make it impossible to fulfill any requirement to make changes publicly available or to send patches to some particular place. This holds even if such requirements are only upon request, as the castaway might be able to receive messages but be unable to send them. To be free, software must be modifiable by this unfortunate castaway, who must also be able to legally share modifications with friends on the island.
-   The **"Dissident"** test. Consider a dissident in a totalitarian state who wishes to share a modified bit of software with fellow dissidents, but does not wish to reveal the identity of the modifier, or directly reveal the modifications themselves, or even possession of the program, to the government. Any requirement for sending source modifications to anyone other than the recipient of the modified binary -- in fact any forced distribution at all, beyond giving source to those who receive a copy of the binary -- would put the dissident in danger. For Debian to consider software free it must not require any such "excess" distribution.
-   The **"Tentacles of evil"** test. Imagine that the author is hired by a large evil corporation and, now in their thrall, attempts to do the worst to the users of the program: to make their lives miserable, to make them stop using the program, to expose them to legal liability, to make the program non-free, to discover their secrets, etc. The same can happen to a corporation bought out by a larger corporation bent on destroying free software in order to maintain its monopoly and extend its evil empire. The license cannot allow even the author to take away the required freedoms!

## [See also]

-   [GLEP 23](https://www.gentoo.org/glep/glep-0023.html)
-   [/etc/portage/license_groups](https://wiki.gentoo.org/wiki//etc/portage/license_groups "/etc/portage/license groups") --- a file containing groups of licenses that may be specified in the [`ACCEPT_LICENSE`](https://wiki.gentoo.org/wiki//etc/portage/make.conf#ACCEPT_LICENSE "/etc/portage/make.conf") variable.

## [External resources]

-   [FSF licenses](https://www.gnu.org/licenses/license-list.html)
-   [OSI licenses](https://opensource.org/licenses)
-   [SPDX open source license registry](https://spdx.org/licenses/)
-   [GNU free software & freedoms definition](https://www.gnu.org/philosophy/free-sw.html)
-   [Open Source Definition](https://opensource.org/osd.html)
-   [Freedoc licenses](https://freedomdefined.org/)

1.  [[[↑](#cite_ref-1)] [[https://www.gnu.org/licenses/license-list.html](https://www.gnu.org/licenses/license-list.html)]]
2.  [[[↑](#cite_ref-2)] [[https://www.gnu.org/licenses/license-list.html#GPLCompatibleLicenses](https://www.gnu.org/licenses/license-list.html#GPLCompatibleLicenses)]]
3.  [[[↑](#cite_ref-3)] [[https://www.gnu.org/licenses/license-list.html#GPLIncompatibleLicenses](https://www.gnu.org/licenses/license-list.html#GPLIncompatibleLicenses)]]
4.  [[[↑](#cite_ref-4)] [[https://www.gnu.org/licenses/license-list.html#NonFreeSoftwareLicenses](https://www.gnu.org/licenses/license-list.html#NonFreeSoftwareLicenses)]]