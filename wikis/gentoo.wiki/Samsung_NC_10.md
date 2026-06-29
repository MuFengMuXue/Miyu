**This page has been [nominated for deletion](https://wiki.gentoo.org/wiki/Help:Deleting_a_page "Help:Deleting a page")**

The given reason is: ***This page does not provide any useful information, the packages no longer exist, the last edit was 12 years ago.***

If there is any reason not to delete this page, *do not remove this notice*, but please open a discussion on the associated [talk page](https://wiki.gentoo.org/wiki/Talk:Samsung_NC_10) (this should delay deletion until the discussion is resolved).

\

[   Note to admins] []

Please remember to check [if anything links here](https://wiki.gentoo.org/wiki/Special:WhatLinksHere/Samsung_NC_10 "Special:WhatLinksHere/Samsung NC 10") and [the page history](https://wiki.gentoo.org/index.php?title=Samsung_NC_10&action=history) before deleting.

This notice should remain for a *minimum of 1 month* after it was placed on the page. If discussion is still ongoing it should remain until a consensus is reached (check the talk page), at which time the page may be deleted or this notice may be removed.

If the page has only been edited by the user who nominated it for deletion and/or is in the nominator\'s user space, then more flexibility in the decision may be allowed.

**Check the [help page on deleting](https://wiki.gentoo.org/wiki/Help:Deleting_a_page#For_admins "Help:Deleting a page") for more information.**

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Samsung_NC_10&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

This is an article about running Gentoo on an Samsung NC 10 series laptop.

## Contents

-   [[1] [Laptop Specifications]](#Laptop_Specifications)
-   [[2] [Install driver packages]](#Install_driver_packages)
-   [[3] [Problems]](#Problems)
    -   [[3.1] [Problems with kernel 3.2]](#Problems_with_kernel_3.2)
    -   [[3.2] [Problems with kernel 3.4]](#Problems_with_kernel_3.4)

## [Laptop Specifications]

Hardware specs may vary.

## [Install driver packages]

`root `[`#`]`emerge --ask media-libs/libva-intel-driver x11-apps/intel-gpu-tools sys-apps/915resolution x11-drivers/xf86-video-intel`

## [Problems]

The i915 card is really unique in X and boot behaviour.

### [Problems with kernel 3.2]

Use these boot settings for X:

    vga=0x315 acpi=force i915.modeset=1 i915.lvds_use_ssc=0 i915.i915_enable_rc6=1

### [Problems with kernel 3.4]

Use these boot settings for X:

    vga=0x315 acpi=force pcie_aspm=force i915.modeset=1 i915.i915_enable_fbc=1 i915.lvds_use_ssc=0 i915.i915_enable_rc6=1 i915.lvds_downclock=1 drm.vblankoffdelay=1 irqpoll