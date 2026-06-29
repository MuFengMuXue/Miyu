[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Trim-Slice "wikipedia:Trim-Slice")

Consult the Embedded Handbook for supplementary information on the [Trimslice hardware](https://wiki.gentoo.org/wiki/Embedded_Handbook/Boards/TrimSlice "Embedded Handbook/Boards/TrimSlice"). The wiki also provides instructions for [installing Gentoo on the Trimslice](https://wiki.gentoo.org/wiki/TrimSlice "TrimSlice").

## [Revive a Trimslice with mainline U-Boot]

** Note**\
The fix for flashing mainline U-Boot on the Trimslice has been in for a while now, so the upstream tools and docs should Just Work\...

Follow RCN wiki steps for extlinux.conf (no more boot.scr needed).

Example: [https://eewiki.net/display/linuxonarm/A20-OLinuXino-LIME](https://eewiki.net/display/linuxonarm/A20-OLinuXino-LIME)

Tegra has \"special\" boot magic so the best way is to follow the readmes for each of the NVIDIA tools or use the manifest builder. Note the README files are required reading either way\...

[flasher README files](https://github.com/sarnold/tegra-uboot-flasher-scripts)

[sarnold/tegra-uboot-flasher-manifest](https://github.com/sarnold/tegra-uboot-flasher-manifests)

If you can install the required tegra tool packages, then you can ignore the build-tools script. Otherwise use the full build script and let it put all of them in a local build output directory. By default it will build all the Tegra boards, so if you just want one, use the argument below. Note that it must come **after** the [./build] command and **before** the actual \"build\" argument:

`user `[`$`]`export ARCH=arm `

`user `[`$`]`export CROSS_COMPILE=armv7a-hardfloat-linux-gnueabi- `

`user `[`$`]`./build --boards trimslice build `

Once everything is built (check the \_out dir above the scripts dir) you can either make an SD card or test the SPI flash build on the Trimslice. Note that any DTC warnings in the u-boot build output are the result of parallel make and can be safely ignored.

Using the manifest build, from the scripts directory:

Make a bootable card:

    1) Follow the RCN wiki example above, but for the u-boot deploy step do:

`user `[`$`]`sudo dd if=../_out/trimslice/trimslice-mmc.img of=/dev/sdb`

Test it in SPI flash:

    1) Connect your serial cable to the front port, and connect a micro USB
       cable to the other port on the front.  Bring up a serial console program.
       Open the tiny door where the microSD slot is, and press the "boot" button
       while powering up (this is Tegra, so it uses fastboot mode).

    2) following the README-user.txt, run the download tool:

`user `[`$`]`sudo python tegra-uboot-flasher exec trimslice`

You should see the console load and execute the u-boot you just downloaded. It will still fallback to the old boot.scr if it can\'t find extlinux.conf (but the latter is now easier and preferred).

When ready, run the same command (after booting into fastboot mode again) with \"flash\" instead of \"exec\":

`user `[`$`]`sudo python tegra-uboot-flasher flash trimslice`

You can use any kernel source, from gentoo-sources to armv7-multiplatform.

## [See also]

-   [TrimSlice](https://wiki.gentoo.org/wiki/TrimSlice "TrimSlice")