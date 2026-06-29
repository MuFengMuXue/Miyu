**This page has been [nominated for deletion](https://wiki.gentoo.org/wiki/Help:Deleting_a_page "Help:Deleting a page")**

The given reason is: ***Dead project, not available anywhere***

If there is any reason not to delete this page, *do not remove this notice*, but please open a discussion on the associated [talk page](https://wiki.gentoo.org/wiki/Talk:Yuzu) (this should delay deletion until the discussion is resolved).

\

[   Note to admins] []

Please remember to check [if anything links here](https://wiki.gentoo.org/wiki/Special:WhatLinksHere/Yuzu "Special:WhatLinksHere/Yuzu") and [the page history](https://wiki.gentoo.org/index.php?title=Yuzu&action=history) before deleting.

This notice should remain for a *minimum of 1 month* after it was placed on the page. If discussion is still ongoing it should remain until a consensus is reached (check the talk page), at which time the page may be deleted or this notice may be removed.

If the page has only been edited by the user who nominated it for deletion and/or is in the nominator\'s user space, then more flexibility in the decision may be allowed.

**Check the [help page on deleting](https://wiki.gentoo.org/wiki/Help:Deleting_a_page#For_admins "Help:Deleting a page") for more information.**

**Resources**

[[]][Home](https://yuzu-emu.org/)

[[]][GitHub](https://github.com/yuzu-emu/yuzu)

** Note**\
Yuzu project discontinued due to lawsuit by Nintendo. By that Yuzu is not available on Gentoo repositories and overlays.

tuzu is an experimental open-source emulator for the Nintendo Switch from the creators of Citra. Yuzu enables to play your Nintendo Switch games on your PC. Yuzu recommends you to always use latest build.

## [Add guru ebuild repository]

Visit [Adding the GURU repository](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users#Adding_the_GURU_repository "Project:GURU/Information for End Users") page

Do not forget to sync your repositories

`root `[`#`]`emerge --sync guru`

## [Compile yuzu]

`root `[`#`]`emerge -av '=games-emulation/yuzu-9999'`