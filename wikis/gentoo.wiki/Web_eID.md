**Resources (Web eID)**

[[]][Web eID](https://web-eid.eu/)

[[]][id.ee » Web eID](https://www.id.ee/en/article/web-eid/)

[[]][Web eID project](https://github.com/web-eid)

**Resources (Open eID)**

[[]][Open eID project](https://github.com/open-eid)

The **Web eID** is a suite of [browser extension](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions), [native application](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_messaging), and JavaScript library that provides a way to perform cryptographic operations (authentication, signing) using smart cards on the Web. One of the purposes of the project is to replace the legacy architecture of the [Open eID](https://github.com/open-eid) project ^[\[1\]](#cite_note-1)^.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Overlay]](#Overlay)
    -   [[1.2] [Package]](#Package)
        -   [[1.2.1] [Web eID]](#Web_eID)
        -   [[1.2.2] [DigiDoc4]](#DigiDoc4)
            -   [[1.2.2.1] [Portage package]](#Portage_package)
            -   [[1.2.2.2] [Flatpak package]](#Flatpak_package)
    -   [[1.3] [Smart card reader driver]](#Smart_card_reader_driver)
    -   [[1.4] [Testing]](#Testing)
-   [[2] [See also]](#See_also)
-   [[3] [References]](#References)

## [Installation]

### [Overlay]

Gentoo is not officially supported by the Web eID project ^[\[2\]](#cite_note-2)^, and there are no packages in the official Gentoo repository. However, there is an [official community-driven overlay](https://github.com/open-eid/gentoo) in the Open eID project. To enable the overlay, first it is necessary to install [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] and [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]]:

`root `[`#`]`emerge --ask dev-vcs/git app-eselect/eselect-repository`

The overlay can then be enabled as follows:

`root `[`#`]`eselect repository add esteid git `[`https://github.com/open-eid/gentoo.git`](https://github.com/open-eid/gentoo.git)

And the Gentoo ebuild repository needs to updated:

`root `[`#`]`emerge --sync`

As all packages in the overlay are masked with the **[amd64]** keyword, they need to be unmasked (see [/etc/portage/package.accept_keywords](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords") for more information):

[FILE] **`/etc/portage/package.accept_keywords`**

    */*::esteid ~amd64

### [Package]

** Note**\
This section assumes that the overlay described above is enabled.

#### [Web eID]

To install the Web eID package, run the following command:

`root `[`#`]`emerge --ask www-plugins/web-eid`

** Important**\
The compilation of the package may fail due to the lack of `Qt5Svg`. In this case, downgrade the [[[dev-qt/qtsvg]](https://packages.gentoo.org/packages/dev-qt/qtsvg)[]] package:

`root `[`#`]`emerge --ask --oneshot dev-qt/qtsvg:5`

#### [DigiDoc4]

##### [Portage package]

** Important**\
As of 2025-01-17, [qdigidoc4] compiles but crashes at runtime due to [libdigidocpp] on musl-based systems, musl libc users should use the Flatpak package as a workaround.

As of 2024-05-07, [dev-cpp/libcutl](https://github.com/open-eid/gentoo/blob/master/dev-cpp/libcutl) incorrectly defines dependencies, so the dependency needs to be installed manually:

`root `[`#`]`emerge --ask dev-libs/boost`

As of 2024-05-07, [dev-libs/libdigidocpp](https://github.com/open-eid/gentoo/tree/master/dev-libs/libdigidocpp) requires the following patch on a musl-based system (the patch will force the library to compile, but it will still crash at runtime):

[FILE] **`/etc/portage/patches/dev-libs/libdigidocpp-3.16.0/ctime.patch`**

    --- a/src/util/File.h
    +++ b/src/util/File.h
    @@ -22,6 +22,7 @@
     #include "../Exception.h"

     #include <stack>
    +#include <ctime>

     namespace digidoc
     [`#`]`emerge --ask app-crypt/qdigidoc4`

##### [Flatpak package]

** Warning**\
Despite the name of the package, it is maintained by a third party ^[\[3\]](#cite_note-3)^. Audit [the manifest](https://github.com/flathub/ee.ria.qdigidoc4) before installing.

Install DigiDoc4 using [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak"):

`user `[`$`]`flatpak remote-add --user --if-not-exists flathub `[`https://flathub.org/repo/flathub.flatpakrepo`](https://flathub.org/repo/flathub.flatpakrepo)

`user `[`$`]`flatpak install --user flathub ee.ria.qdigidoc4`

To run DigiDoc4 use the following command:

`user `[`$`]`flatpak run --user ee.ria.qdigidoc4`

** Important**\
The package comes with the [libpcsclite.so.1] library, which will communicate with the [pcscd](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite") daemon (which runs outside of Flatpak, on the host system) via its socket ^[\[4\]](#cite_note-4)^. As stated by the author of PCSC-Lite, PCSC-Lite was not designed with the virtual environment in mind ^[\[5\]](#cite_note-5)^. Thus, [libpcsclite.so.1] in the package and the daemon on the host system may be compiled with different versions of the communication protocol, and communication between them will not be possible. This problem can be tracked in the system log on the host system:

    Jan 16 20:21:22 akemi ../pcsc-lite-2.3.0/src/winscard_svc.c:404:ContextThread() Communication protocol mismatch!
    Jan 16 20:21:22 akemi ../pcsc-lite-2.3.0/src/winscard_svc.c:406:ContextThread() Client protocol is 4:4
    Jan 16 20:21:22 akemi ../pcsc-lite-2.3.0/src/winscard_svc.c:408:ContextThread() Server protocol is 4:5

To resolve this issue, the PCSC-Lite version on the host system needs to be downgraded. See [[[bug #946163]](https://bugs.gentoo.org/show_bug.cgi?id=946163)[]]. The version used in the flatpak package can be found in [this file](https://github.com/flathub/ee.ria.qdigidoc4/blob/master/ee.ria.qdigidoc4.yml). Version matching does not have to be one-to-one, as different versions of PCSC-Lite may use the same protocol. The downgrade can be done by masking:

[FILE] **`/etc/portage/package.mask`**

    >sys-apps/pcsc-lite-2.0.1-r1

`root `[`#`]`emerge --ask sys-apps/pcsc-lite`

### [Smart card reader driver]

Follow the instructions provided [here](https://wiki.gentoo.org/wiki/Electronic_identification#Smart_card_reader_driver "Electronic identification").

### [Testing]

The [official website](https://web-eid.eu/) has a button to test authentication and signing.

## [See also]

-   [Electronic identification](https://wiki.gentoo.org/wiki/Electronic_identification "Electronic identification") --- the core part of e-government implementation, providing a way to identify citizens and organizations.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/web-eid/web-eid-system-architecture-doc](https://github.com/web-eid/web-eid-system-architecture-doc)]]
2.  [[[↑](#cite_ref-2)] [[https://github.com/open-eid/gentoo](https://github.com/open-eid/gentoo)]]
3.  [[[↑](#cite_ref-3)] [[https://github.com/open-eid/DigiDoc4-Client/issues/969#issuecomment-2079620448](https://github.com/open-eid/DigiDoc4-Client/issues/969#issuecomment-2079620448)]]
4.  [[[↑](#cite_ref-4)] [[https://ludovicrousseau.blogspot.com/2022/02/accessing-smart-cards-from-inside.html](https://ludovicrousseau.blogspot.com/2022/02/accessing-smart-cards-from-inside.html)]]
5.  [[[↑](#cite_ref-5)] [[https://github.com/flatpak/flatpak/issues/4066#issuecomment-1034040834](https://github.com/flatpak/flatpak/issues/4066#issuecomment-1034040834)]]