**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

Gentoo\'s gx86-multilib project has a two-fold missionː

1.  Provide a means to build Gentoo packages for multiple ABIs ([multilib](https://wiki.gentoo.org/wiki/Multilib "Multilib")); and
2.  Empower package maintainers to implement multiple ABIs in a consistent manner.

## [Goals]

̇̇̇̇̇

-   Our main goal is to provide a feasible and user-friendly way of supporting applications which are not compatible with the native ABI. This means, we effectively target the following three kinds of applicationsː

1.  Closed-source applications, such as Skype, which are not released for the native ABI or architecture;
2.  Applications interfacing with closed source applications, such as wine; and
3.  Applications which break when compiled for the native ABI.

-   A side goal is to deprecate the various emul-linux packages, replacing them with a better solution.

## [Eclasses]

We provide the following eclasses for multilib-related use:

1.  [multilib-build.eclass](https://devmanual.gentoo.org/eclass-reference/multilib-build.eclass/) provides the raw tools to build packages with multilib support. It sets the necessary USE flags for the package and provides functions to perform the build. It should be used only in meta-packages, as it exclusively affects USE flags.
2.  [autotools-multilib.eclass](http://devmanual.gentoo.org/eclass-reference/autotools-multilib.eclass/) is a very simple wrapper on top of the [autotools-utils.eclass](http://devmanual.gentoo.org/eclass-reference/autotools-utils.eclass/) to be used for all multilib-capable autotools packages. It uses the out-of-source build feature to support multilib builds with almost no need of modifying autotools-utils ebuilds.
3.  [multilib-minimal.eclass](https://devmanual.gentoo.org/eclass-reference/multilib-minimal.eclass/) provides a simple, wrapper to build the packages where no other eclass fits better.

## [USE flags]

Multilib-capable packages request proper package variants and satisfy dependencies through the use of *abi\_\** USE flags. To ensure the consistency of a package\'s IUSE flags, **please define architecture flags in packages**.

By default, *abi\_\** flags are masked and hidden. Architecture-specific profiles unmask the flags and force the native flag (it remains hidden from the user). Multilib profiles may also un-hide the flags to unmask additional variants.

The native ABI flag must always be enabled on multilib libraries to guarantee that plain (non-multilib aware) package dependencies always pull in the native variant. To maintain backwards compatibility and user convenience, multilib support needs to be transparent to non-multilib packages.

Some leaf packages, like [[[app-emulation/wine]](https://packages.gentoo.org/packages/app-emulation/wine)[]] or [[[www-plugins/adobe-flash]](https://packages.gentoo.org/packages/www-plugins/adobe-flash)[]], may need the default *abi̜̞\_\** flags removed. You may edit the profile\'s package.use.force file. However, please note that afterwards non-multilib packages won\'t be able to properly depend on the package in question.

[FILE] **`profiles/arch/amd64/package.use.force`Example of un-forcing abi_x86_64**

    # Michał Górny <mgorny@gentoo.org> (02 Sep 2013)
    # Packages with optional 64-bit variant.
    app-emulation/wine -abi_x86_64
    www-plugins/adobe-flash -abi_x86_64