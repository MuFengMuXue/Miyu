## Contents

-   [[1] [What is it?]](#What_is_it.3F)
-   [[2] [When should it be done?]](#When_should_it_be_done.3F)
-   [[3] [Why might a profile update instruct this?]](#Why_might_a_profile_update_instruct_this.3F)
    -   [[3.1] [ABI changes]](#ABI_changes)
    -   [[3.2] [Consistency]](#Consistency)
-   [[4] [When should it be considered?]](#When_should_it_be_considered.3F)
    -   [[4.1] [Miscompilations]](#Miscompilations)
    -   [[4.2] [Symbol versioning]](#Symbol_versioning)
    -   [[4.3] [Fortification]](#Fortification)

## [][What is it?]

[emerge \--emptytree] tells Portage to pretend that no packages are installed and to queue all of them for a rebuild.

This is useful when changing CFLAGS or toolchains, or when testing a major change (to smoke out any problems immediately).

## [][When should it be done?]

-   Changing *COMMON_FLAGS* (`CFLAGS`, `CXXFLAGS`, etc), especially when the new target ISA is a subset of the old ISA (e.g. `-march=x86-64-v3` -\> `-march=x86-64-v1`).
-   Changing ABIs in any other way (e.g. time64, IEEE long double)
-   Whenever a news item instructs it
    -   e.g. New profiles often bring in changed toolchain defaults for efficiency, security hardening, or bug fixes.

## [][Why might a profile update instruct this?]

There\'s two reasons.

### [ABI changes]

The profile may involve ABI (binary compatibility) changes (e.g. IEEE long double, [time64](https://wiki.gentoo.org/wiki/Project:Toolchain/time64_migration "Project:Toolchain/time64 migration"), changing to PIE by default, or the [libstdc++ ABI break](https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dual_abi.html) many years ago.

Rebuilding is non-negotiable here and not simply recommended, but hard-required.

### [Consistency]

The profile may set changed toolchain settings which do not break ABI, but could change runtime behavior, or otherwise have a risk of causing problems.

A profile won\'t include a change if it\'s dangerous, but the point remains that a change is a change.

Having this applied **consistently** makes debugging things far easier. For example, if a package appears to be underlinked, but we can assume the system is entirely built with BIND_NOW, then diagnosis might (reasonably) assume its binaries will fail immediately, not at a random point during runtime.

It makes sense to have everybody rebuild for these changes to pick it up immediately, so that problems can be debugged and immediately \"blamed\" on the profile/changed defaults, rather than appearing at random months later when a package gets updated.

Worse still, if a system is rarely updated or rebuilt, and then problems emerge years later, when the common diagnostic techniques and solutions for any problems are long forgotten.

For such cases, rebuilding is broadly recommended rather than required.

## [][When should it be considered?]

There are some cases where it\'s not required, but possibly a good idea. An occasional *\--emptytree* (*-e*) is not a bad thing.

A lot of misinformation and confusion surrounds this topic. Some treat it as purely a way to gain negligible performance increases after upgrading the compiler, which isn\'t exactly right, as this article explores.

If one enjoys testing and reporting bugs, *\--emptytree* after a major change is helpful as issues can be discovered immediately rather than incrementally as packages get updated later.

### [Miscompilations]

All compilers suffer from serious bugs on occasion. Compilers sometimes produce binaries with incorrect runtime behavior, called *miscompilations*. Compiler developers take miscompilations seriously, especially so for miscompilations which are derived from real-world programs (rather than fuzzing).

Many binary distributions rebuild their whole archive on every release, yearly or so. When they do this, there\'s usually a new toolchain included - as well as many other packages, of course. This means the average age of a binary is fairly young. They also do this with a fixed, standard set of `CFLAGS`.

On the other hand, Gentoo is a source-based distribution. Many users build their own binaries locally, and do so with their own `CFLAGS`. In Gentoo, packages will only be rebuilt if their ebuild is updated, or they depend on a package which changed ABI (subslot caused a rebuild). This means the average age of binaries, especially for packages with inactive upstreams, might be far older, depending on the system in question.

Combining this longer-than-average lifespan of a binary on Gentoo with the diverse set of `CFLAGS` across all of Gentoo\'s users, it is not unreasonable to suggest that in the same way Gentoo users benefit from compiler optimizations, they might also occasionally hit compiler bugs - possibly without realizing it.

Doing an occasional rebuild (say, yearly) with the latest toolchain versions is not a bad idea in light of this.

As a compromise, one might want to implement a search based on when a package was last re-emerged, and re-emerge those after say, 1y, 2y.

TL:DR: You get the good from compiling, but you have to live with a somewhat Gentoo-specific tradeoff.

### [Symbol versioning]

[[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] in particular makes heavy use of symbol versioning. This allows preserving ABI while introducing modified versions of functions. For example, binaries linked against an old glibc will use its legacy malloc implementation. Fresh linking against glibc will produce binaries using the current malloc implementation.

While glibc introduces changes to versioned symbols in each release, such major changes to e.g. its malloc implementation are rare. It\'s therefore not necessary to do a major rebuild after every single glibc release, but after every few, it\'s worth considering.

### [Fortification]

This is related to the symbol versioning point, but a bit different.

glibc-2.38 introduced the controversial *strlcpy* and *strlcat* functions. Before then, applications often supplied their own bundled copy which they used if libc didn\'t provide it (e.g. [[[bug #854105]](https://bugs.gentoo.org/show_bug.cgi?id=854105)[]]), or they relied on libbsd for the same.

Nothing will use the glibc implementations until they are built against a glibc providing it. By rebuilding against a newer glibc, not only does one benefit from the optimized and maintained versions of these functions in glibc, but *\_FORTIFY_SOURCE* protection is now provided!

This exposed a real bug in rsync - [[[bug #917517]](https://bugs.gentoo.org/show_bug.cgi?id=917517)[]].