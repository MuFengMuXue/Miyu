[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Gradle&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://gradle.org/)

[[]][Package information](https://packages.gentoo.org/packages/dev-java/gradle-bin)

[[]][GitHub](https://github.com/gradle/gradle)

[[]][Official documentation](https://docs.gradle.org/current/userguide/userguide.html)

**Gradle** is a [Java](https://wiki.gentoo.org/wiki/Java "Java")-based build, automation and delivery tool.

## Contents

-   [[1] [Usage]](#Usage)
    -   [[1.1] [Dependency tree]](#Dependency_tree)
    -   [[1.2] [Further command line tasks]](#Further_command_line_tasks)
-   [[2] [Availability]](#Availability)
-   [[3] [Packages waiting for Gradle support]](#Packages_waiting_for_Gradle_support)
-   [[4] [Related links]](#Related_links)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Usage]

### [Dependency tree]

Packagers wanting to see the dependency tree of a package, e.g. [v1.72](https://github.com/bcgit/bc-java/tree/r1rv72/mail) of [[[dev-java/bcmail]](https://packages.gentoo.org/packages/dev-java/bcmail)[]], use:

`user `[`$`]`gradle dependencies | sed -n '/Classpath/,/^$/p'`

    compileClasspath - Compile classpath for source set 'main'.
    +--- project :core
    +--- project :util
    +--- project :pkix
    +--- project :prov
    \--- javax.mail:mail:1.4
         \--- javax.activation:activation:1.1

    runtimeClasspath - Runtime classpath of source set 'main'.
    +--- project :core
    |    \--- org.openjdk.jmh:jmh-core:1.33
    |         +--- net.sf.jopt-simple:jopt-simple:4.6
    |         \--- org.apache.commons:commons-math3:3.2
    +--- project :util
    |    \--- project :core (*)
    +--- project :pkix
    |    +--- project :core (*)
    |    +--- project :util (*)
    |    \--- project :prov
    |         \--- project :core (*)
    +--- project :prov (*)
    \--- javax.mail:mail:1.4
         \--- javax.activation:activation:1.1

    testCompileClasspath - Compile classpath for source set 'test'.
    +--- project :core
    +--- project :util
    +--- project :pkix
    +--- project :prov
    +--- javax.mail:mail:1.4
    |    \--- javax.activation:activation:1.1
    \--- junit:junit:4.11
         \--- org.hamcrest:hamcrest-core:1.3

    testRuntimeClasspath - Runtime classpath of source set 'test'.
    +--- project :core
    |    \--- org.openjdk.jmh:jmh-core:1.33
    |         +--- net.sf.jopt-simple:jopt-simple:4.6
    |         \--- org.apache.commons:commons-math3:3.2
    +--- project :util
    |    \--- project :core (*)
    +--- project :pkix
    |    +--- project :core (*)
    |    +--- project :util (*)
    |    \--- project :prov
    |         \--- project :core (*)
    +--- project :prov (*)
    +--- javax.mail:mail:1.4
    |    \--- javax.activation:activation:1.1
    \--- junit:junit:4.11
         \--- org.hamcrest:hamcrest-core:1.3

For a specific Java classpath, e.g. `runtimeClasspath`, the command is:

`user `[`$`]`gradle dependencies --configuration runtimeClasspath`

In case the above commands give errors it\'s sometimes still possible to run [gradlew]:

`user `[`$`]`./gradlew dependencies`

### [Further command line tasks]

[Command line](https://wiki.gentoo.org/wiki/Shell "Shell") tasks are explained on [https://docs.gradle.org/current/userguide/command_line_interface.html#common_tasks](https://docs.gradle.org/current/userguide/command_line_interface.html#common_tasks)

## [Availability]

An ebuild is available in the [mva-overlay](https://github.com/msva/mva-overlay/tree/master/dev-java/gradle) ebuild repository.

## [Packages waiting for Gradle support]

New packages for the tree which depend on Gradle are organized by the tracker ticket [[[bug #777609]](https://bugs.gentoo.org/show_bug.cgi?id=777609)[]]

## [Related links]

-   [https://github.com/gradle/gradle/issues/16600](https://github.com/gradle/gradle/issues/16600)
-   [https://github.com/gradle/gradle/issues/15992](https://github.com/gradle/gradle/issues/15992)

## [See also]

-   [Gentoo_Java_Packing_Policy#Gradle](https://wiki.gentoo.org/wiki/Gentoo_Java_Packing_Policy#Gradle "Gentoo Java Packing Policy")
-   [Maven](https://wiki.gentoo.org/wiki/Maven "Maven")
-   [[[app-eselect/eselect-gradle]](https://packages.gentoo.org/packages/app-eselect/eselect-gradle)[]]

## [External resources]

-   [https://tomgregory.com/gradle-dependency-tree/](https://tomgregory.com/gradle-dependency-tree/)