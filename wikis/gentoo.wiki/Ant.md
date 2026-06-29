**Resources**

[[]][Home](https://ant.apache.org/)

[[]][Package information](https://packages.gentoo.org/packages/dev-java/ant)

[[]][GitHub](https://github.com/apache/ant)

[[]][Official documentation](https://ant.apache.org/manual/)

eant is a Gentoo wrapper around ant. One should never invoke ant directly in an ebuild but instead call `eant`.

## [Preparing sources for building with ant]

Additionally to what\'s described in [Java_Developer_Guide#Preparing_sources](https://wiki.gentoo.org/wiki/Java_Developer_Guide#Preparing_sources "Java Developer Guide"):

For projects that use ant as build system, any eventually hardcoded `-target` and `-source` attributes must be patched out from any [build.xml] files which are used.

If a project uses ant as a build system, there can be unwanted targets that are always called. Or targets that will download dependencies outside of portage. Other times there might be unwanted classes or resources on the classpath, or it is missing a classpath that will be set/added to the ebuild.

To avoid unwanted targets you can either remove them entirely from the build.xml file, or you can comment out the targets via XML comments, `<!-- •••••• -->`. This can be done via one or more patches and/or sed if minimal. Pay close attention to target dependencies, and dependent targets. At times bypassing one unwanted target can bypass other wanted targets. There are times you might need to change a target\'s dependencies rather than bypassing a target entirely.

## [Compiling with eant]

There are several ebuilds in ::gentoo which can be used as examples, see [the build log](https://gitweb.gentoo.org/repo/gentoo.git/log/?qt=grep&q=without+BSFIX).

[CODE] **Using ant Global Variables**

    inherit java-pkg-2

    ...

        eant jar $(usev doc javadoc) \
            -Dant.build.javac.source="$(java-pkg_get-source)" \
            -Dant.build.javac.target="$(java-pkg_get-target)"

## [Typical examples using eant]

[FILE] **`foo-1.0.ebuild`Example of a Java ant ebuild**

    # Copyright 1999-2024 Gentoo Authors
    # Distributed under the terms of the GNU General Public License v2

    EAPI=8

    # Tests require an existing running SQL server and 'junit.jar.file' property
    JAVA_PKG_IUSE="doc examples source"

    inherit java-pkg-2

    DESCRIPTION="JDBC drivers with JNDI-bindable DataSources"
    HOMEPAGE="https://www.mchange.com/projects/c3p0/"
    SRC_URI="https://downloads.sourceforge.net/project/c3p0/c3p0-src/c3p0-$/$.src.tgz"
    S="$/$.src"

    LICENSE="|| ( EPL-1.0 LGPL-2.1 )"
    SLOT="0"
    KEYWORDS="~amd64 ~ppc64 ~x86 ~amd64-linux ~x86-linux"

    CP_DEPEND="
       dev-java/log4j-12-api:2
       dev-java/mchange-commons:0
    "

    DEPEND="
       >=virtual/jdk-1.8:*
       $
    "

    RDEPEND="
       >=virtual/jre-1.8:*
       $
    "

    PATCHES=( "$/c3p0-0.9.5.5-source-target.patch" )

    src_prepare()

    src_compile()

    src_install() .jar"
        einstalldocs

        use doc && java-pkg_dojavadoc build/apidocs
        use examples && java-pkg_doexamples src/java/com/mchange/v2/c3p0/example
        use source && java-pkg_dosrc src/java/com/mchange/v2
    }