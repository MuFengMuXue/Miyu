[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=How_to_build_a_toolchain_for_arm_cortex-m_and_cortex-r&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

For up to date information on [ARM](https://wiki.gentoo.org/wiki/ARM "ARM") toolchain building (also for Cortex-R and Cortex-M), please review the main [ARM](https://wiki.gentoo.org/wiki/ARM "ARM") article.

## [Toolchain installation steps]

[Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") can almost build a functioning toolchain for embedded arm development. The toolchain can be created with the following steps:

Step 1:

`root `[`#`]`crossdev --lenv 'USE="nano -nls -threads -unicode"' -s3 -t arm-unknown-eabi`

Step 2:

`root `[`#`]`crossdev --lenv 'USE="nano -nls -threads -unicode"' --genv 'USE="cxx -nls -nptl -pch -pie -ssp" EXTRA_ECONF="--with-multilib-list=rmprofile --disable-decimal-float --disable-libffi --disable-libgomp --disable-libmudflap --disable-libquadmath --disable-shared --disable-threads --disable-tls"' -s4 -t arm-unknown-eabi`

Step 3:

`root `[`#`]`emerge --ask cross-arm-unknown-eabi/newlib`

Step 4:

`root `[`#`]`crossdev --lenv 'USE="nano -nls -threads -unicode"' --genv 'USE="cxx -nls -nptl -pch -pie -ssp" EXTRA_ECONF="--with-multilib-list=rmprofile --disable-decimal-float --disable-libffi --disable-libgomp --disable-libmudflap --disable-libquadmath --disable-shared --disable-threads --disable-tls"' -s4 --ex-gdb -t arm-unknown-eabi`

Now you\'ll have a functioning multilib / multiarch for embedded arm development with small code output size.

Big thanks to the Gentoo forum user **rapsure** who posted this instructions [here](https://forums.gentoo.org/viewtopic-t-1085836.html).

## [Toolchain installation steps with hardware floating point]

You may also want the toolchain to contain support for hardware floating point. In that case, use these instructions instead:

Step 1:

`root `[`#`]`crossdev --lenv 'USE="nano -nls -threads -unicode"' -s3 -t arm-unknown-eabi`

Step 2:

`root `[`#`]`crossdev --lenv 'USE="nano -nls -threads -unicode"' --genv 'USE="cxx -nls -nptl -pch -pie -ssp" EXTRA_ECONF="--with-multilib-list=rmprofile --disable-decimal-float --disable-libffi --disable-libgomp --disable-libmudflap --disable-libquadmath --disable-shared --disable-threads --disable-tls"' -s4 -t arm-unknown-eabi`

Step 3:

`root `[`#`]`emerge --ask cross-arm-unknown-eabi/newlib`

Step 4:

`root `[`#`]`crossdev --lenv 'USE="nano -nls -threads -unicode" EXTRA_ECONF="--enable-newlib-hw-fp"' --genv 'USE="cxx -nls -nptl -pch -pie -ssp" EXTRA_ECONF="--with-multilib-list=rmprofile --disable-decimal-float --disable-libffi --disable-libgomp --disable-libmudflap --disable-libquadmath --disable-shared --disable-threads --disable-tls"' -s4 --ex-gdb -t arm-unknown-eabi`

** Note**\
I left the toolchain named arm-unknown-eabi because it is what the instructions previously used, but in my experience most IDEs expect the naming convention to be arm-none-eabi. It\'s perfectly alright to use these instructions with arm-none-eabi instead of arm-unknown-eabi for convenience.