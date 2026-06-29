[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=WxFormBuilder&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](http://wxformbuilder.org)

**wxFormBuilder** is an application that can literally speed up GUI development, being Python either C++ the programming language of choice.

## [Installation]

To install it, first add the *gentoo-zh* [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"):

`root `[`#`]`eselect repository enable gentoo-zh`

`root `[`#`]`emerge --sync gentoo-zh`

Then, since premake-3.7 is currently an ebuild prerequisite, though the core system is already providing premake-4, you have to directly specify it:

`root `[`#`]`emerge --ask dev-util/premake:3`

You may now proceed and install [[[dev-util/wxFormBuilder]](https://packages.gentoo.org/packages/dev-util/wxFormBuilder)[]] itself:

`root `[`#`]`emerge --ask wxformbuilder`

## [External resources]

-   [http://wxformbuilder.org](http://wxformbuilder.org)