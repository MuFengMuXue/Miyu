This page contains [[changes](https://wiki.gentoo.org/index.php?title=Gentoo_Java_USE_flags&diff=1078013)] which are not marked for translation.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Gentoo_Java_USE_flags&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

#### [About USE flags]

For more information regarding USE flags, refer to the [USE flags](https://devmanual.gentoo.org/general-concepts/use-flags) chapter from the Gentoo Development Guide.

#### [Java specific USE flags]

There are a few specific common USE flags for Java ebuilds as follows. These use flags do not go in the normal `USE` variable but go in `JAVA_PKG_IUSE` instead. Any use flag other than the following would go in the normal `USE` variable. The `JAVA_PKG_IUSE` must precede the [`inherit`](https://devmanual.gentoo.org/ebuild-writing/using-eclasses/) line in an ebuild.

The USE flags that go in `JAVA_PKG_IUSE`

-   If USE FLAG [`binary`](https://packages.gentoo.org/useflags/binary) exists and is set, it will just copy \$ to \$ and skip the rest of src_compile.
-   The `doc` flag will build API documentation using javadoc.
-   The `source` flag installs a zip of the source code of a package. This is traditionally used for IDEs to \'attach\' source to the libraries that are being use;
-   The `test` Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)

#### [Masked gentoo-vm]

The USE flag [`gentoo-vm`](https://packages.gentoo.org/useflags/gentoo-vm) is experimental and currently not needed for regular packages. It is only required to run experiments and forcing eselect to also list newer JVMs. See [[[bug #805008]](https://bugs.gentoo.org/show_bug.cgi?id=805008)[]] for details on [how to unmask](https://wiki.gentoo.org/wiki/User:Sam/Portage_help/Java_unmasking "User:Sam/Portage help/Java unmasking") this USE flag.

\