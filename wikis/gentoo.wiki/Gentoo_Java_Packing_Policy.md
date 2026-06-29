This policy is the official **Gentoo Java Packing Policy** and Guidelines for packaging Java applications and libraries for Gentoo Linux. For details on Java ebuilds syntax, semantics, and examples please refer to the [Developer Guide](https://wiki.gentoo.org/wiki/Project:Java/Developer_Guide "Project:Java/Developer Guide")

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [Why have a Java policy?]](#Why_have_a_Java_policy.3F)
    -   [[1.2] [Build from Source]](#Build_from_Source)
    -   [[1.3] [Dependencies]](#Dependencies)
    -   [[1.4] [Slotting]](#Slotting)
    -   [[1.5] [Package Conventions]](#Package_Conventions)
        -   [[1.5.1] [JDBC Drivers]](#JDBC_Drivers)
-   [[2] [Minimum JRE/JDK Version]](#Minimum_JRE.2FJDK_Version)
    -   [[2.1] [Current Minimum JRE/JDK Version]](#Current_Minimum_JRE.2FJDK_Version)
-   [[3] [Java USE flags]](#Java_USE_flags)
    -   [[3.1] [About USE flags]](#About_USE_flags)
    -   [[3.2] [Java specific USE flags]](#Java_specific_USE_flags)
    -   [[3.3] [Masked gentoo-vm]](#Masked_gentoo-vm)
-   [[4] [Java Eclasses]](#Java_Eclasses)
    -   [[4.1] [About Eclasses]](#About_Eclasses)
    -   [[4.2] [Java specific Eclasses]](#Java_specific_Eclasses)
    -   [[4.3] [Which Eclass to use]](#Which_Eclass_to_use)
-   [[5] [Java build systems]](#Java_build_systems)
    -   [[5.1] [Which build system to use]](#Which_build_system_to_use)
    -   [[5.2] [No build system]](#No_build_system)
    -   [[5.3] [Ant]](#Ant)
    -   [[5.4] [Gant]](#Gant)
    -   [[5.5] [Gradle]](#Gradle)
    -   [[5.6] [Ivy]](#Ivy)
    -   [[5.7] [Maven]](#Maven)
    -   [[5.8] [Non-standard]](#Non-standard)
-   [[6] [Java filesystem layout]](#Java_filesystem_layout)
-   [[7] [Java jar repository]](#Java_jar_repository)

## [Overview]

Packaging Java applications and libraries on Gentoo Linux is not trivial, and is a rather complex process with a bit of a steep learning curve. This policy and guide seeks to standardize Java ebuilds, when to use what [eclass](https://wiki.gentoo.org/wiki/Eclass "Eclass"), build system, etc. This should help anyone seeking to contribute as well as existing Gentoo developers learn about Gentoo Java packaging nuances. For details on Java ebuilds syntax, semantics, and examples please refer to the [Developer Guide](https://wiki.gentoo.org/wiki/Project:Java/Developer_Guide "Project:Java/Developer Guide")

### [][Why have a Java policy?]

This policy is necessary to keep Java ebuilds consistent, to form an official standard, and to reduce the burden of correcting contributed Java ebuilds. Please adhere to this policy when packaging Java applications and libraries for Gentoo Linux.

### [Build from Source]

As is standard practice on Gentoo, all Java applications and libraries are to be built from source. This includes any dependencies which might be [bundled](https://wiki.gentoo.org/wiki/Why_not_bundle_dependencies "Why not bundle dependencies") and/or downloaded during compile. Limited exceptions are made for some applications and almost never for a library, all on a case by case basis. Some complex applications have too many dependencies which are not packaged, sources are not available, and/or the package is not easily built. Those might qualify for exceptions, but by default all Java packages should be built from source. For reasons why, please refer to [Why Build from Source](https://wiki.gentoo.org/wiki/Project:Java/Why_build_from_source "Project:Java/Why build from source").

### [Dependencies]

Dependent packages, anything another package depends on be it a application or library, needs to also be packaged and built from source. Packages are NOT allowed to resolve and/or download their own dependencies outside of portage ever, without exception! Portage should handle any dependencies for the package. Which require dependencies to be packaged. Bundled dependencies should be removed from sources to ensure when the package is built, it is using system dependencies not any provided in the package. There are limited exceptions on a case by case basis. Gentoo Java eclasses will emit warning messages if any bundled binary class or jar files are found.

### [Slotting]

Applications and libraries should be slotted according to the API they provide. If two version have the same API, or if a new version is fully compatible with the previous version, then they should be in the same SLOT.

Java libraries have a tendency to sometimes break API and ABI between minor revisions, ie from 2.1.1 to 2.1.2. As a result, it is necessary to slot early, and slot often. Gentoo developers have made a tool dev-java/java-apicheck that can be used to determine if there are API changes in a package to justify a slot. Anytime there are API changes, there should be a new slot.

For Java applications, it is mostly sufficient to keep only the latest version. If the application comes in series, such as Tomcat, we want to keep the latest revision in each series. Very old series may eventually be dropped completely, even if they are still maintained by upstream.

### [Package Conventions]

Java applications can be quite large. Many have sub-pieces that can be built standalone. It is common for other sub-pieces to depend on another sub-piece as part of the application. On Gentoo such sub-pieces are to be packaged on their own. If need be eclasses can be created to help with common aspects for all sub-pieces. When packaging any Java application on Gentoo, the application should be broken down to the smallest build-able pieces. Creating individual packages for any and all sub-pieces. The package name will start with the application name, followed by the sub-piece name of the application.

For any application that has sub-pieces it is recommended, but not required, to slot the package and all sub-pieces. Slotting will prevent updating a single sub-piece, without updating the rest. That does create extra work, but it will keep an application\'s sources complete without mixing versions of sub-pieces. Which upstream will likely not like mixed versions of sub-pieces, nor address any issues that might arise from such. Slotting prevents such issues, but does come with the drawback of requiring all sub-pieces of an application to be updated to update the application itself.

#### [JDBC Drivers]

JDBC Drivers should always be named with the `jdbc-` prefix added to the package name of the jdbc driver.

## [][Minimum JRE/JDK Version]

All Java ebuilds should set the JRE/JDK to the minimum version unless you need a newer version. One should NEVER set the jre/jdk version less than the current minimum, unless a package will not compile with the current minimum version. This is very rare, and likely any packages are outdated. Most any current Java application and/or library should compile and work just fine with the minimum, or require a newer. It is acceptable to set to a newer/greater version, however please only do so when you actually need a newer/greater version. Otherwise all Java ebuilds should be set to the current minimum JRE/JDK Version.

### [][Current Minimum JRE/JDK Version]

[CODE] **Current Minimum JRE/JDK Version**

    RDEPEND=">=virtual/jre-1.8:*"
    DEPEND=">=virtual/jdk-1.8:*"

## [Java USE flags]

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

## [Java Eclasses]

### [About Eclasses]

For more information regarding Eclasses, refer to the [Eclass writing](https://devmanual.gentoo.org/eclass-writing/) chapter from the Gentoo Development Guide.

### [Java specific Eclasses]

There are several Java Eclasses available as follows:

-   `java-pkg-2.eclass` - Eclass for Java Packages, [reference](https://devmanual.gentoo.org/eclass-reference/java-pkg-2.eclass/index.html)
-   `java-pkg-opt-2.eclass` - Eclass for package with optional Java support, [reference](https://devmanual.gentoo.org/eclass-reference/java-pkg-opt-2.eclass/index.html)
-   `java-pkg-simple.eclass` - Gentoo\'s own Java build system using the commandline tools provided by [[[dev-java/openjdk]](https://packages.gentoo.org/packages/dev-java/openjdk)[]], [reference](https://devmanual.gentoo.org/eclass-reference/java-pkg-simple.eclass/index.html)
-   `java-utils-2.eclass` - Base Eclass for Java packages (never used directly in ebuild), [reference](https://devmanual.gentoo.org/eclass-reference/java-utils-2.eclass/index.html)
-   `java-vm-2.eclass` - Java Virtual Machine Eclass (only used for java vm packages), [reference](https://devmanual.gentoo.org/eclass-reference/java-vm-2.eclass/index.html)

### [Which Eclass to use]

All Java packages will always inherit `java-pkg-2.eclass`. Packages that have optional java support should use `java-pkg-opt-2.eclass`. For either of those, if the package has a Ant build system, you will want to also inherit `java-ant-2.eclass`. If the package lacks a build system, or is using an unsupported build system such as Gradle or Maven, then you will want to inherit and use `java-pkg-simple.eclass`.

The only time you will use `java-vm-2.eclass` is for Java Virtual Machine packages. It is not used for normal Java packages. Do not inherit this class unless the package is for a Java Virtual Machine.

The `java-utils-2.eclass` should not be inherited directly from an ebuild EVER! The other eclasses already inherit this eclass, thus no need to ever inherit it directly.

## [Java build systems]

Java has a few common build systems, the most common are as follows:

-   ant - Full integration with portage, build system can and should be used
-   gant - No integration with portage, build system cannot be used
-   gradle - No integration with portage, build system cannot be used
-   ivy - No integration with portage, can be bypassed and use ant build system ONLY
-   maven - No integration with portage, build system cannot be used

### [Which build system to use]

By default try to always use the build system provided by upstream, which may require modifications and/or patching. In the event that does not work, or it is using an unsupported build system such as Gradle or Maven, move on to the next section No Build System.

### [No build system]

For packages without a build system, or using an unsupported build system. You either need to see about using `java-pkg-simple.eclass`, or you might even have to write your own Ant build.xml file so you can build the package with Ant. Please do not use the `mvn ant:ant` feature of Maven to generate build.xml files for Ant. These generated files are generic.

### [Ant]

**Ant is fully integrated with portage.** Java packages that come with an ant build system should inherit the `java-pkg-2.eclass` and use the `eant()`function instead of calling `ant` directly. Packages that come with an Ant based build system can sometimes easier be packaged using the `java-pkg-simple.eclass` and avoid having [[[dev-java/ant]](https://packages.gentoo.org/packages/dev-java/ant)[]] in the dependency tree. Building with `eant()` can be useful in case there is code generation involved or multiple `jars` built from the same package.

### [Gant]

**Gant is not integrated with portage.** It is not feasible to use Gant to build Java packages on Gentoo at this time. You may attempt such, but will likely run into other issues. At this time there are no plans for Gant integration into portage. Please refer to the No Build System section.

### [Gradle]

**[Gradle](https://wiki.gentoo.org/wiki/Gradle "Gradle") is not integrated with portage.** It is not feasible to use Gradle to build Java packages on Gentoo at this time. You may attempt such, but will likely run into other issues. At this time there are no plans for Gradle integration into portage. Please refer to the No Build System section.

### [Ivy]

**Ivy is not integrated with portage.** it is not feasible to use Ivy to build Java packages on Gentoo at this time. However Ivy being a dependency resolver usually around an Ant build system. Which means you can bypass, comment out or otherwise, the Ivy portions and proceed with using the rest of the Ant build system. However if Ivy is being used for a build tool other than Ant, then you cannot proceed at all. Please refer to the No Build System section.

### [Maven]

**[Maven](https://wiki.gentoo.org/wiki/Maven "Maven") is not integrated with portage.** It is not feasible to use [Maven](https://wiki.gentoo.org/wiki/Maven "Maven") to build Java packages on Gentoo at this time. You may attempt such, but will likely run into other issues. At this time there are plans for Maven integration into portage but no ETA. Several efforts have been made to both building Maven from source (bootstrap) and for building packages with Maven. Unfortunately those efforts and work never made it beyond the Java overlay. It has been quite some time since anyone has worked on Maven integration. Though there have been discussions, and some theoretical plans, but no ETA and no one presently working on it. Thus at this time for Maven based packages, please refer to the No Build System section.

### [Non-standard]

There are many other non-standard build systems such as autoconf, automake, or scripts to build the package. Usually these are for packages where Java parts are optional, and mostly building non-Java based software. However there might be times where software is using Java Native Interface, and might have some non-Java parts to compile. There are others where the package is mostly non-Java but has a part that is Java, and is not using a standard Java build system for the Java portion. Care must be taken in such situations to ensure the Java parts are built correctly. Likely the best thing in such case is to build that Java part with either `java-pkg-simple.eclass` or by making a build.xml file for Ant and using `java-ant-2.eclass`. If you attempt to build Java code without using Gentoo Java Eclasses, the result will likely be incorrect, if usable. Please do not bypass Gentoo Java Eclasses for alternative means of building Java packages, code, or pieces.

## [Java filesystem layout]

In general, the directory policies are handled for you by the helper functions in the java-utils-2 eclass. You may not deviate from this filesystem layout. Do not put jars anywhere else, unless the package requires such!

These functions adhere to the following path name conventions:

-   [/usr/share/\$-\$/package.env] contains information about the package.
-   .jar files created from source code are installed to [/usr/share/\$-\$/lib/]
-   .jar pre-built files not compiled by the ebuild are installed to [/opt/\$-\$/lib]
-   Javadoc documentation is installed to [/usr/share/doc/\$/html/api/]
-   Source archives are installed to [/usr/share/\$-\$/source/]
-   User-executable scripts are installed to [/usr/bin]
-   System-wide environment files are in installed to [/usr/env.d/java]
-   User-specific environment files can be put into [\$/.gentoo/env.d/]

## [Java jar repository]

At this time Gentoo does not have a central jar repository for use with tools such as Maven. There are plans to create a Gentoo jar repository, likely specific to Maven, but could be used by other tools.