Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Java/de "Java (78% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Java/es "Java (32% translated)")
-   [français](https://wiki.gentoo.org/wiki/Java/fr "Java (35% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Java/hu "Java (78% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Java/pt-br "Java (68% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/Java/cs "Java/cs (1% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Java/ru "Java (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Java/zh-cn "Java (34% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Java/ja "Java (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Java/ko "Java/ko (18% translated)")

**Resources**

[[]][Home](https://www.java.com/en/)

[[]][Official documentation](https://docs.oracle.com/en/java/)

[[]][Package information](https://packages.gentoo.org/packages/virtual/jdk)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Java_(programming_language) "wikipedia:Java (programming language)")

[[]][GitHub](https://github.com/openjdk/jdk)

[[]][Bugs (upstream)](https://bugreport.java.com/bugreport/)

[[]][[#java](ircs://irc.libera.chat/#java)] ([[webchat](https://web.libera.chat/#java)])

[[]][[comp.lang.java.programmer](news:comp.lang.java.programmer) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.lang.java.programmer))]

[[]][Blog](https://dev.java/news/)

**Java** is a programming language, originally developed by [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems "wikipedia:Sun Microsystems"), which uses a platform-independent virtual machine to execute Java bytecode in real-time. It is a popular choice for developers who want to create cross-platform business applications.

## Contents

-   [[1] [What is Java?]](#What_is_Java.3F)
    -   [[1.1] [Overview]](#Overview)
    -   [[1.2] [JVM languages]](#JVM_languages)
-   [[2] [Installing a virtual machine]](#Installing_a_virtual_machine)
    -   [[2.1] [The choices]](#The_choices)
    -   [[2.2] [Installing a JRE/JDK]](#Installing_a_JRE.2FJDK)
    -   [[2.3] [Setting up a headless JRE]](#Setting_up_a_headless_JRE)
-   [[3] [Configuring the Java Virtual Machine]](#Configuring_the_Java_Virtual_Machine)
    -   [[3.1] [Overview]](#Overview_2)
    -   [[3.2] [Setting a default]](#Setting_a_default)
-   [[4] [Java browser plugins]](#Java_browser_plugins)
-   [[5] [USE flags for use with Java]](#USE_flags_for_use_with_Java)
    -   [[5.1] [Setting USE flags]](#Setting_USE_flags)
    -   [[5.2] [USE flags]](#USE_flags)
-   [[6] [Multiple Java Versions]](#Multiple_Java_Versions)
-   [[7] [Troubleshooting]](#Troubleshooting)
    -   [[7.1] [Java 21 Circular Dependencies]](#Java_21_Circular_Dependencies)
    -   [[7.2] [Minecraft launcher errors]](#Minecraft_launcher_errors)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)
-   [[10] [References]](#References)

## [][What is Java?]

### [Overview]

Java is a programming language developed by Sun Microsystems. The language is object-oriented and designed to run on multiple platforms without the need of recompiling code for each platform. Although Java can be compiled as a native program, much of Java\'s popularity can be attributed to its portability, along with other features such as automatic memory management. To make platform independence possible the Java compiler compiles the Java code to an intermediate representation called [Java bytecode](https://en.wikipedia.org/wiki/Java_bytecode "wikipedia:Java bytecode") that runs on a *JVM* ([Java Virtual Machine](https://en.wikipedia.org/wiki/Java_virtual_machine "wikipedia:Java virtual machine")) and not directly on the operating system.

In order to run Java bytecode, one needs to have a *JRE* (Java Runtime Environment) installed. A *JRE* provides core libraries, a platform dependent *JVM*, plugins for browsers, among other things. A *JDK* (Java Development Kit) adds programming tools, such as a bytecode compiler and a debugger.

### [JVM languages]

The Java virtual machine is not used exclusively by Java programming language. Multiple programming languages use the Java platform and run on the JVM. Examples of such include: [Clojure](https://en.wikipedia.org/wiki/Clojure "wikipedia:Clojure"), [Apache Groovy](https://en.wikipedia.org/wiki/Apache_Groovy "wikipedia:Apache Groovy"), [Kotlin](https://wiki.gentoo.org/wiki/Kotlin "Kotlin") or [Scala](https://en.wikipedia.org/wiki/Scala_(programming_language) "wikipedia:Scala (programming language)").

## [Installing a virtual machine]

### [The choices]

Gentoo provides Java Runtime Environments (JREs) and Java Development Kits (JDKs). The available choices include:

  ------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Vendor                                                                         JDK
  [OpenJDK](https://en.wikipedia.org/wiki/OpenJDK "wikipedia:OpenJDK")   [[[dev-java/openjdk]](https://packages.gentoo.org/packages/dev-java/openjdk)[]]
  [Eclipse Temurin](https://adoptopenjdk.net/)   [[[dev-java/openjdk-bin]](https://packages.gentoo.org/packages/dev-java/openjdk-bin)[]] and [[[dev-java/openjdk-jre-bin]](https://packages.gentoo.org/packages/dev-java/openjdk-jre-bin)[]]
  ------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [][Installing a JRE/JDK]

To install the profile\'s default **JDK** run:

`root `[`#`]`emerge --ask --oneshot virtual/jdk`

To install the profile\'s default **JRE** run:

`root `[`#`]`emerge --ask --oneshot virtual/jre`

** Note**\
Be aware each *JDK* will include a *JRE*; installing a JRE is not necessary if a JDK has been emerged.

### [Setting up a headless JRE]

Sometimes there is no need for a full JRE with all the capabilities of java. Using java on a server often does not require any GUI, graphical, sound or even printer related features. To install a simplified (sometimes also referred to as headless) JRE, a few USE flags need to be changed for the selected JRE flavor.

[FILE] **`/etc/portage/package.use`Required USE flag changes**

    dev-java/openjdk headless-awt -alsa -cups
    dev-java/openjdk-bin headless-awt -alsa -cups

Depending on the current Gentoo profile, this might already be the case. As usual, the USE flag settings that are applicable to a particular package can be checked by running [emerge] in pretend mode:

`user `[`$`]`emerge --pretend --verbose virtual/jre`

## [Configuring the Java Virtual Machine]

### [Overview]

Gentoo has the ability to have multiple JDKs and JREs installed without causing conflicts.

### [[] Setting a default]

The [eselect] command can be used to present a list of installed Java instances (be it JRE or JDK). Here is an example of the output:

`user `[`$`]`eselect java-vm list`

    Available Java Virtual Machines:
      [1]   openjdk-8
      [2]   openjdk-11
      [3]   openjdk-17
      [4]   openjdk-bin-8  system-vm user-vm

The *user-vm* flag indicates the default JVM for the user. The *system-vm* flag indicates the default JVM for the system and the fallback if a user JVM is not set. The number in the brackets (i.e. \[1\]) is the reference for the particular JVM. To set the default system JVM:

`root `[`#`]`eselect java-vm set system 1`

To set a preferred user JVM:

`user `[`$`]`eselect java-vm set user 1`

** Note**\
[source]-ing the profile for existing shell sessions is not usually needed when changing the user or system VM. The only exception is that variables such as `JAVA_HOME` will still point to the old location after setting a user VM for the first time or revert back to the system VM.

## [Java browser plugins]

** Important**\
The Java plugin support had been deprecated in JDK 9^[\[1\]](#cite_note-1)^.

** Note**\
Note that [Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium")-based browsers since version 42 and [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") since version 52 no longer support [NPAPI](https://en.wikipedia.org/wiki/NPAPI "wikipedia:NPAPI")-based plugins^[\[2\]](#cite_note-2)^. This effectively disables the Java plugin on modern browsers.

For those who need a Java-enabled browser for a specific use case, there are [[[www-client/palemoon::palemoon]](https://repos.gentoo.org/#palemoon)[]] or [[[www-clint/palemoon-bin::palemoon]](https://repos.gentoo.org/#palemoon)[]] packages available in the [palemoon overlay](https://github.com/deu/palemoon-overlay), which has long-term support for NPAPI and thus Java plugins up to JDK 8^[\[3\]](#cite_note-3)^.

## [USE flags for use with Java]

### [Setting USE flags]

For more information regarding [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), refer to the USE flags chapter from the [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:X86/Working/USE "Handbook:X86/Working/USE").

### [USE flags]

-   The [`java`](https://packages.gentoo.org/useflags/java) flag adds support for Java in a variety of programs;
-   The [`nsplugin`](https://packages.gentoo.org/useflags/nsplugin) flag is still used by [[[www-plugins/lightspark]](https://packages.gentoo.org/packages/www-plugins/lightspark)[]];

Following USE flags go in JAVA_PKG_IUSE, see [Gentoo Java USE flags](https://wiki.gentoo.org/wiki/Gentoo_Java_USE_flags "Gentoo Java USE flags") for details and other specific USE flags of Java:

-   The [`source`](https://packages.gentoo.org/useflags/source) flag installs a zip of the source code of a package. This is traditionally used for IDEs to \'attach\' source to the libraries that are being use;
-   For Java packages, the [`doc`](https://packages.gentoo.org/useflags/doc) flag will build API documentation using javadoc.

## [Multiple Java Versions]

For those that may need multiple versions of Java, one may use slotted packages.

`root `[`#`]`emerge --ask dev-java/openjdk:8`

`root `[`#`]`emerge --ask dev-java/openjdk:11`

`root `[`#`]`emerge --ask dev-java/openjdk:17`

`root `[`#`]`emerge --ask dev-java/openjdk:21`

The default can then be changed by [setting a default](https://wiki.gentoo.org/wiki/Java#Setting_a_default "Java").

## [Troubleshooting]

### [Java 21 Circular Dependencies]

If you get an error when installing openjdk:21, emerge openjdk-bin:21.

`root `[`#`]`emerge --ask dev-java/openjdk-bin:21`

### [Minecraft launcher errors]

-   A specific error in which [minecraft-launcher] crashed after a few seconds, throwing \"Alarm\" and \"SaveToBuffer failed\" error was solved by setting the [[[threads]](https://packages.gentoo.org/useflags/threads)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag for [[[net-misc/curl]](https://packages.gentoo.org/packages/net-misc/curl)[]].

<!-- -->

-   When executing [minecraft-launcher] the following error was produced:

`user `[`$`]`./minecraft-launcher`

    [0229/184549.183275:ERROR:sandbox_linux.cc(346)] InitializeSandbox() called with multiple threads in process gpu-process.

This was solved by executing [minecraft-launcher] with the following option:

`user `[`$`]`MESA_GLSL_CACHE_DISABLE=true ./minecraft-launcher`

## [See also]

-   [Java Developer Guide](https://wiki.gentoo.org/wiki/Java_Developer_Guide "Java Developer Guide") --- covers specific details on Gentoo Java ebuilds.
-   [Project:Java/Why build from source](https://wiki.gentoo.org/wiki/Project:Java/Why_build_from_source "Project:Java/Why build from source")
-   [Project:Java/Getting Involved](https://wiki.gentoo.org/wiki/Project:Java/Getting_Involved "Project:Java/Getting Involved")

## [External resources]

-   Configuring Java per directory with [jEnv](https://www.jenv.be)
-   [[#gentoo](ircs://irc.libera.chat/#gentoo)] ([[webchat](https://web.libera.chat/#gentoo)]) and [[#gentoo-java](ircs://irc.libera.chat/#gentoo-java)] ([[webchat](https://web.libera.chat/#gentoo-java)]) on IRC

## [References]

1.  [[[↑](#cite_ref-1)] [[JDK 9 and the Java Plugin](https://www.java.com/en/download/faq/jdk9_plugin.xml), java.com. Retrieved on November 30, 2018]]
2.  [[[↑](#cite_ref-2)] [[How do I enable Java in my web browser?](https://java.com/en/download/help/enable_browser.xml), java.com. Retrieved on November 30, 2018]]
3.  [[[↑](#cite_ref-3)] [[Pale Moon future roadmap](https://www.palemoon.org/roadmap.shtml), palemoon.org. Retrieved on June 28, 2019]]

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Joshua Nichols, Karl Trygve Kalleberg, nightmorph**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*