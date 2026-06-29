**Resources**

[[]][Home](https://www.yoctoproject.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Yocto_Project "wikipedia:Yocto Project")

[[]][[#yocto](ircs://irc.libera.chat/#yocto)] ([[webchat](https://web.libera.chat/#yocto)])

The **Yocto Project** is a Linux Foundation workgroup whose goal is to produce tools and processes that will enable the creation of Linux distributions for embedded software that are independent of the underlying architecture of the embedded software itself. The project was announced by the Linux Foundation in 2010 ^[\[1\]](#cite_note-1)^. In March 2011, the project aligned itself with OpenEmbedded, an existing framework with similar goals, with the result being The OpenEmbedded-Core Project.

The *Yocto Project* is an open source project whose focus is on improving the software development process for embedded Linux distributions. The Yocto Project provides interoperable tools, metadata, and processes that enable the rapid, repeatable development of Linux-based embedded systems.^[\[2\]](#cite_note-Yocto_Project_Wikipedia-2)^

Gentoo is not officially supported by the Yocto / OpenEmbedded project, however, Gentoo works perfectly fine as a Yocto/OE build host, with one or two caveats about building on a hardened profile.

-   Some recipes and the final do_rootfs try to spin up an ARM qemu environment and will fail if qemu doesn\'t have the proper PaX markings. The Gentoo package should have the right PaX config, and local.conf has the right place to set qemu and sdl as \"assume_provided\" (meaning use Gentoo package deps instead of building its own native packages).

\

`user `[`$`]`bitbake`

    bitbake [...]
    WARNING: Host distribution "Gentoo" has not been validated with this version of the build system;  you may possibly experience unexpected failures.
    It is recommended that you use a tested distribution.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [Install QEMU and SDL]](#Install_QEMU_and_SDL)
-   [[2] [Install Build Deps]](#Install_Build_Deps)
-   [[3] [Test installation]](#Test_installation)
-   [[4] [Official QuickStart]](#Official_QuickStart)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

[]  As of **2021-01-19**, the information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=Yocto&action=edit).

### [Prerequisites]

### [Install QEMU and SDL]

See [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU"): install QEMU with ARM user targets enabled and make sure the binfmt_misc module is enabled in your kernel.

Install [[[media-libs/libsdl2]](https://packages.gentoo.org/packages/media-libs/libsdl2)[]] with USE=\"X alsa joystick opengl pulseaudio sound video\" and set this in your local.conf:

[FILE] **`~/foss-udoo-bsp/poky/build/conf/local.conf`**

    ASSUME_PROVIDED += "qemu-native libsdl2-native"

## [Install Build Deps]

You should most of these already installed, but this list should pick up anything you don\'t have:

`root `[`#`]` emerge -n patch make sed m4 bison cvs openjade quilt docbook-xml-dtd docbook-dsssl-stylesheets xmlto docbook-sgml-utils libpcre boost subversion texi2html chrpath fakeroot lzop sys-devel/bc net-libs/prcsvc-proto `

## [Test installation]

Many available BSP layers use the same basic (manual) setup in their README file which is shown below.

There are two options:

1.  Build a basic machine image for the handful of machines supported by the Yocto Reference BSP
2.  Use the BSP layer specific to your board (e.g. RPi), plus the Yocto reference distribution BSP data for Poky and the OE meta layers. You can clone them all manually or use a repo manifest. This generally gives better results.

An increasingly common method for obtaining the metadata layers for building a Yocto or OE image is the \"repo\" manifest, e.g. the [Freescale/NXP community BSP](https://github.com/Freescale/fsl-community-bsp-platform).

Either follow the quickstart guide below, or use one of the available repo BSP manifests.

Note that the FSL/NXP community manifest repo (and those derived from it) include layers with proprietary/vendor recipes and the accompanying EULA (which you must accept).

The alternative is a FOSS manifest, or custom build config and layers, that use open source packages only (mainly u-boot, kernel, graphics, and audio). There are several FOSS manifest layers for various machines (eg, BeagleBone, Nitrogen6x, and Altera socfpga) in the VCT Labs github repos, and a new one for Udoo and Udoo Neo nelow. For any of the manifest builds, select a build branch and follow the README file. Also, when using layers with vendor recipes in a FOSS build, you may need to manually exclude the vendor recipes (see BBMASK in Yocto developer docs).

[Udoo Neo manifest builder](https://github.com/sarnold/foss-udoo-neo-platform-bsp.git)

[Udoo Neo Tips](https://gist.github.com/sarnold/2e244fa8580ec715321a515c72535d4f)

## [Official QuickStart]

[Yocto Project Quick Build](https://docs.yoctoproject.org/brief-yoctoprojectqs/index.html)

`user `[`$`]`git clone -b scarthgap `[`https://git.yoctoproject.org/poky`](https://git.yoctoproject.org/poky)` `

`user `[`$`]`cd poky `

`user `[`$`]`source oe-init-build-env `

`user `[`$`]`bitbake -k core-image-minimal `

[Yocto Project Application Development and the Extensible Software Development Kit (eSDK)](https://docs.yoctoproject.org/sdk-manual/index.html)

`user `[`$`]`git clone -b scarthgap `[`https://git.yoctoproject.org/poky`](https://git.yoctoproject.org/poky)` `

`user `[`$`]`cd poky `

`user `[`$`]`source oe-init-build-env `

`user `[`$`]`bitbake meta-ide-support `

`user `[`$`]`bitbake -k core-image-sato-sdk `

`user `[`$`]`runqemu-extract-sdk [...] `

## [External resources]

-   [yoctoproject on Gentoo](https://forums.gentoo.org/viewtopic-t-987684-highlight-.html)
-   [Yocto Current Documentation](https://www.yoctoproject.org/documentation/current)
-   [OpenEmbedded](https://www.openembedded.org)

## [References]

1.  [[[↑](#cite_ref-1)] [The Linux Foundation. [Yocto Project Aligns Technology with OpenEmbedded and Gains Corporate Collaborator](https://www.linuxfoundation.org/press/press-release/yocto-project-aligns-technology-with-openembedded-and-gains-corporate-collaborators), [Linux Foundation Press Releases](https://www.linuxfoundation.org/press), March 2nd, 2011.]]
2.  [[[↑](#cite_ref-Yocto_Project_Wikipedia_2-0)] [[*Yocto Project* -- Wikipedia](https://en.wikipedia.org/wiki/Yocto_Project)]]