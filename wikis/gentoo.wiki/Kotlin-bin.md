**Resources**

[[]][Home](https://kotlinlang.org/)

[[]][Official documentation](https://kotlinlang.org/docs/home.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Kotlin_(programming_language) "wikipedia:Kotlin (programming language)")

[[]][GitHub](https://github.com/JetBrains/kotlin)

[[]][[#kotlin](ircs://irc.libera.chat/#kotlin)] ([[webchat](https://web.libera.chat/#kotlin)])(registration required)

**Kotlin** is a programming language developed by [JetBrains](https://www.jetbrains.com/). Originally shaped as a programming language based on the Java platform and JVM, Kotlin was designed with Java interoperability in mind, meaning that a Kotlin program can use not just the [Kotlin Standard Library](https://kotlinlang.org/api/latest/jvm/stdlib/) but the Java SE API and all Java libraries too, and Java programs can call useful helpers in the Kotlin Standard Library and all sorts of other Kotlin code as well. Later, Kotlin has been expanded with Android support, JavaScript support through Kotlin/JS, and support for native machine code as compiler target via Kotlin/Native.

Like virtually all other GNU/Linux distributions, Gentoo does not provide Kotlin in its official ebuild repository yet. A few users\' personal ebuild repositories may contain an ebuild for Kotlin that unpacks the compiler Zip archive made by the upstream to the file system. During [Google Summer of Code 2021](https://summerofcode.withgoogle.com/projects/#5063497366372352), ebuilds that can build the [Kotlin core libraries](https://github.com/JetBrains/kotlin/tree/master/libraries#kotlin-libraries) were created, so Gentoo users can install the Kotlin libraries from source instead of binaries pre-compiled by the upstream. [A blog post](https://leo3418.github.io/2021/07/05/gentoo-build-kt-src.html) documenting how the ebuilds were created is available.

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [Available packages]](#Available_packages)
    -   [[1.2] [Versioning and package slotting]](#Versioning_and_package_slotting)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Ebuild repository]](#Ebuild_repository)
    -   [[2.2] [USE flags]](#USE_flags)
        -   [[2.2.1] [dev-java/kotlin-\* packages]](#dev-java.2Fkotlin-.2A_packages)
    -   [[2.3] [Emerge]](#Emerge)
    -   [[2.4] [Using the upstream\'s pre-built binaries]](#Using_the_upstream.27s_pre-built_binaries)
    -   [[2.5] [Kotlin/JS]](#Kotlin.2FJS)
    -   [[2.6] [Installing an old feature release]](#Installing_an_old_feature_release)
-   [[3] [Managing multiple versions of Kotlin]](#Managing_multiple_versions_of_Kotlin)
    -   [[3.1] [Finding the Kotlin tools\' version]](#Finding_the_Kotlin_tools.27_version)
    -   [[3.2] [Eselect]](#Eselect)
        -   [[3.2.1] [Getting information for installed Kotlin compiler packages]](#Getting_information_for_installed_Kotlin_compiler_packages)
        -   [[3.2.2] [Setting a default Kotlin compiler for the user or the system]](#Setting_a_default_Kotlin_compiler_for_the_user_or_the_system)
        -   [[3.2.3] [Setting a default Kotlin compiler for a feature release]](#Setting_a_default_Kotlin_compiler_for_a_feature_release)
    -   [[3.3] [Selecting Kotlin feature release used to build a Kotlin package]](#Selecting_Kotlin_feature_release_used_to_build_a_Kotlin_package)
    -   [[3.4] [Versioned Kotlin tool executables]](#Versioned_Kotlin_tool_executables)
    -   [[3.5] [Tools that are not available]](#Tools_that_are_not_available)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Compile and run the most simple \"hello, world\" program]](#Compile_and_run_the_most_simple_.22hello.2C_world.22_program)
    -   [[4.2] [Compile and run a \"hello, world\" program which uses the Kotlin Standard Library]](#Compile_and_run_a_.22hello.2C_world.22_program_which_uses_the_Kotlin_Standard_Library)
    -   [[4.3] [Compile and run a \"hello, world\" program which uses additional libraries]](#Compile_and_run_a_.22hello.2C_world.22_program_which_uses_additional_libraries)
    -   [[4.4] [Compile and run a Java program which uses the Kotlin Standard Library]](#Compile_and_run_a_Java_program_which_uses_the_Kotlin_Standard_Library)
    -   [[4.5] [Compile and run programs with libraries for a newer feature release]](#Compile_and_run_programs_with_libraries_for_a_newer_feature_release)
    -   [[4.6] [Compile and run programs with libraries for an older feature release]](#Compile_and_run_programs_with_libraries_for_an_older_feature_release)
-   [[5] [Version upgrade]](#Version_upgrade)
    -   [[5.1] [New incremental or bug fix release]](#New_incremental_or_bug_fix_release)
    -   [[5.2] [New feature release]](#New_feature_release)
        -   [[5.2.1] [Staying on a feature release]](#Staying_on_a_feature_release)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Overview]

### [Available packages]

The following packages for Kotlin are available:

  --------------------------------- --------------------------------------------- ----------------------------------------- -------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                           Maven Central Artifact                        Description                               Status         Comments

  Kotlin Standard Library

  dev-java/kotlin-stdlib            org.jetbrains.kotlin:kotlin-stdlib\           Kotlin Standard Library for JVM           Works
                                    org.jetbrains.kotlin:kotlin-stdlib-common

  dev-java/kotlin-stdlib-jdk7       org.jetbrains.kotlin:kotlin-stdlib-jdk7       Kotlin Standard Library JDK 7 extension   Works

  dev-java/kotlin-stdlib-jdk8       org.jetbrains.kotlin:kotlin-stdlib-jdk8       Kotlin Standard Library JDK 8 extension   Works

  dev-java/kotlin-stdlib-js         org.jetbrains.kotlin:kotlin-stdlib-js         Kotlin Standard Library for JavaScript    Unchecked      There is not a known method to reproduce a JAR that is equivalent to the upstream\'s pre-built JAR from Portage. The upstream provides a [Mocha](https://mochajs.org/) test suite, which is yet to be integrated with the ebuild.

  kotlin.test

  dev-java/kotlin-test              org.jetbrains.kotlin:kotlin-test\             Kotlin Test Multiplatform library         Works
                                    org.jetbrains.kotlin:kotlin-test-common

  dev-java/kotlin-test-junit        org.jetbrains.kotlin:kotlin-test-junit        Kotlin Test Support for JUnit 4           Works

  dev-java/kotlin-test-js           org.jetbrains.kotlin:kotlin-test-js           Kotlin Test for JavaScript                Unchecked      There is not a known method to reproduce a JAR that is equivalent to the upstream\'s pre-built JAR from Portage, and the upstream does not have a test suite that can be used to test this package.

  Other Library Components

  dev-java/kotlin-reflect           org.jetbrains.kotlin:kotlin-reflect           Kotlin Full Reflection Library            Should Work    There is not a known method to reproduce a JAR that is structurally identical to the upstream\'s pre-built JAR from Portage, and the upstream does not have a test suite that can be used to test this package. However, when this package is used with the Kotlin compiler, no undesired or unexpected behavior would be exhibited.

  dev-java/kotlin-annotations-jvm   org.jetbrains.kotlin:kotlin-annotations-jvm   Kotlin annotations for JVM                Works

  Compiler

  dev-lang/kotlin-bin               org.jetbrains.kotlin:kotlin-compiler          Binary package for the Kotlin compiler    Works
  --------------------------------- --------------------------------------------- ----------------------------------------- -------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Versioning and package slotting]

The Kotlin packages strive to stay consistent with [the upstream\'s versioning scheme](https://kotlinlang.org/docs/releases.html). Here is the glossary of terms the upstream uses to define the versioning scheme and describe different kinds of Kotlin releases:

Feature releases

Incremental releases

Bug fix releases

All Kotlin packages are slotted based on the *feature releases*, so users can specify to install Kotlin 1.4.x, 1.5.x, etc. to use multiple feature releases in parallel.

## [Installation]

### [Ebuild repository]

The Kotlin ebuilds are currently located in [the Spark overlay](https://github.com/6-6-6/spark-overlay). Before installing the Kotlin ebuilds, please add the Spark overlay to the system using [the instructions in the overlay\'s README](https://github.com/6-6-6/spark-overlay#initial-configuration).

### [USE flags]

#### [][dev-java/kotlin-\* packages]

Each of the Kotlin library packages provides some or all of the `USE` flags listed below:

-   [`binary`](https://packages.gentoo.org/useflags/binary): Use the binary JAR pre-built by the upstream instead of compile the package from source
-   [`source`](https://packages.gentoo.org/useflags/source): Install an archive of the source files under [/usr/share/\$-\$/sources], so the package\'s source files can be viewed from some IDEs
-   [`test`](https://packages.gentoo.org/useflags/test): Enable dependencies to run the package\'s tests, which are controlled by `FEATURES=test`

### [Emerge]

The first step to install **any** Kotlin packages - both the Kotlin library packages and third-party Kotlin packages - is to install the Kotlin compiler, which is provided by dev-lang/kotlin-bin.

`root `[`#`]`emerge --ask dev-lang/kotlin-bin`

If this is the first time dev-lang/kotlin-bin is being installed, bootstrap packages for Kotlin libraries required by the Kotlin compiler will be pulled as dependencies. After the Kotlin compiler is installed, these libraries can be rebuilt from source using it, and the bootstrap packages will be replaced:

`root `[`#`]`emerge --ask --oneshot dev-java/kotlin-stdlib dev-java/kotlin-reflect`

** Note**\
The process described here is applicable only to **Kotlin 1.4 and above**. A set of packages for Kotlin 1.3 are offered, but these packages do not build the Kotlin libraries from source, so they can be merged directly without bootstrapping:

`root `[`#`]`emerge --ask dev-lang/kotlin-bin:1.3`

The Kotlin 1.3 packages are considered **legacy** and will not receive the same level of support as the packages for the latest Kotlin feature releases.

### [][Using the upstream\'s pre-built binaries]

If use of the upstream\'s pre-built binaries is acceptable for some or all of the Kotlin library packages, the `binary` `USE` flag can be enabled for them so they will not be built from source. The following example demonstrates how to enable the `USE` flag for select Kotlin packages:

[FILE] **`/etc/portage/package.use`Use the pre-built binary for dev-java/kotlin-reflect and dev-java/kotlin-stdlib-js**

    dev-java/kotlin-reflect binary
    dev-java/kotlin-stdlib-js binary

### [][Kotlin/JS]

** Important**\
There is not a known way to reproduce a package for kotlin-stdlib-js that is identical to the upstream\'s pre-built artifact from Portage, and no adequate testing on the ebuild has been conducted yet. Therefore, the dev-java/kotlin-stdlib-js package built from source might have issues or might not work at all. Should any problem arises, please fall back to the binary pre-built by the upstream with the method described above.

For Kotlin/JS support, please install dev-java/kotlin-stdlib-js.

`root `[`#`]`emerge --ask dev-java/kotlin-stdlib-js`

### [Installing an old feature release]

The steps listed above install the latest version of Kotlin available in the Spark overlay. The overlay might provide packages for multiple feature releases of Kotlin, and an older release can be installed using instructions in this section.

If no versions of dev-java/kotlin-stdlib and dev-java/kotlin-reflect are installed on the system, an older release of the Kotlin compiler can be installed directly by specifying the feature release\'s version as the slot of dev-lang/kotlin-bin. Bootstrap packages for kotlin-stdlib and kotlin-reflect for the same release will be pulled together, and they can be rebuilt after the Kotlin compiler is installed:

`root `[`#`]`emerge --ask dev-lang/kotlin-bin:1.4`

`root `[`#`]`emerge --ask --oneshot dev-java/kotlin-stdlib:1.4 dev-java/kotlin-reflect:1.4`

If any version of dev-java/kotlin-stdlib or dev-java/kotlin-reflect is already installed on the system, the above commands would not work. Portage would attempt to install dev-java/kotlin-stdlib and dev-java/kotlin-reflect for the older feature release directly, but these Kotlin libraries must be re-bootstrapped for the release using the same version of the Kotlin compiler.

`root `[`#`]`emerge --ask dev-lang/kotlin-bin:1.4`

     * Error: circular dependencies:

    (dev-java/kotlin-stdlib-1.4.32:1.4/1.4::spark-overlay, ebuild scheduled for merge) depends on
     (virtual/kotlin-1.4:1.4/1.4::spark-overlay, ebuild scheduled for merge) (buildtime)
      (dev-lang/kotlin-bin-1.4.32:1.4/1.4::spark-overlay, ebuild scheduled for merge) (runtime)
       (dev-java/kotlin-stdlib-1.4.32:1.4/1.4::spark-overlay, ebuild scheduled for merge) (buildtime)

In this case, please explicitly request the bootstrap packages for kotlin-stdlib and kotlin-reflect for the older release to be installed before running the commands above:

`root `[`#`]`emerge --ask --oneshot dev-java/kotlin-stdlib-bootstrap:1.4 dev-java/kotlin-reflect-bootstrap:1.4`

## [Managing multiple versions of Kotlin]

The slotting of Kotlin packages makes it possible to install and use more than one version of Kotlin on a single system without conflicts. To facilitate use of multiple Kotlin versions, an [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect") module for Kotlin, app-eselect/eselect-kotlin, is provided with the Kotlin packages for selecting the default Kotlin version backing the [kotlin], [kotlinc] and [kapt] tools. For each of those Kotlin tools, versioned executables like [kotlinc1.4], [kotlinc1.5], etc. are provided too for users who want to use a different Kotlin version without changing the default settings.

### [][Finding the Kotlin tools\' version]

The option recognized by various Kotlin tools for querying their version is `-version`.

`user `[`$`]`kotlinc -version`

    info: kotlinc-jvm 1.5.20 (JRE 1.8.0_292-b10)

### [Eselect]

Similar to the java-vm eselect module, the Kotlin eselect module supports independent Kotlin compiler version selection for both the user and the system. Additionally, if multiple packages of the Kotlin compiler are installed for the same Kotlin feature release, then the Kotlin eselect module provides the functionality to choose the package to use for the feature release.

#### [Getting information for installed Kotlin compiler packages]

Like common eselect modules, the `list` action is used for printing a list of installed Kotlin compilers:

`user `[`$`]`eselect kotlin list`

    Available Kotlin compilers:
      [1]   kotlin-bin-1.4 1.4 user
      [2]   kotlin-1.5 system
      [3]   kotlin-bin-1.5 1.5

Next to each compiler package\'s name are indicators showing if the package has been chosen as the default compiler for **the user**, **the system**, or **a Kotlin feature release**. The default version selections can be obtained with the `show` action as well:

`user `[`$`]`eselect kotlin show`

    Current Kotlin compiler for 1.4
      kotlin-bin-1.4
    Current Kotlin compiler for 1.5
      kotlin-bin-1.5
    Current Kotlin compiler for system
      kotlin-1.5
    Current Kotlin compiler for user
      kotlin-bin-1.4

#### [Setting a default Kotlin compiler for the user or the system]

The `set` action of the Kotlin eselect module changes the Kotlin compiler preferences. Like most other eselect modules, the target Kotlin compiler can be specified using either its full name or its ordinal in the list returned by `eselect kotlin list`.

For example, if `eselect kotlin list` prints the list shown in the previous section, then both of these commands can set the default Kotlin compiler for the *user* to `kotlin-bin-1.5`:

`user `[`$`]`eselect kotlin set user kotlin-bin-1.5`

`user `[`$`]`eselect kotlin set user 3`

The default Kotlin compiler for the *system* can be set similarly:

`root `[`#`]`eselect kotlin set system kotlin-bin-1.5`

`root `[`#`]`eselect kotlin set system 3`

#### [Setting a default Kotlin compiler for a feature release]

** Note**\
The feature described in this section is provisioned for addition of alternative Kotlin compiler packages like dev-lang/kotlin in the future. Since there is only one Kotlin compiler package available currently, this feature does not have any use cases yet.

A default Kotlin compiler package can also be set for each Kotlin feature release. This will link the versioned Kotlin tool executables like [kotlin1.5] and [kotlinc1.5] to the executables for that package and cause any ebuilds depending on that feature release to use that package for compilation.

To find all Kotlin compiler packages for a specific feature release, specify the feature release number as an argument to `eselect kotlin list`:

`user `[`$`]`eselect kotlin list 1.5`

    Available Kotlin compilers for Kotlin 1.5:
      [1]   kotlin-1.5 system
      [2]   kotlin-bin-1.5 1.5

The default compiler preference for a feature release can be changed with `eselect kotlin set` too, but please note that if an ordinal is being used to specify the compiler package, then the ordinal needs to come from **the list of compilers for the feature release**. For example, the same `kotlin-bin-1.5` package\'s ordinal should be 2 instead of 3:

`root `[`#`]`eselect kotlin set 1.5 kotlin-bin-1.5`

`root `[`#`]`eselect kotlin set 1.5 2`

### [Selecting Kotlin feature release used to build a Kotlin package]

Every Kotlin package has a set of `KOTLIN_SINGLE_TARGET` [`USE_EXPAND`](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE_EXPAND "/etc/portage/make.conf") flags that can be used to select the Kotlin feature release used to build it. The format of values in `KOTLIN_SINGLE_TARGET` is `kotlin1-x` for Kotlin 1.`x`.

A global default value of `KOTLIN_SINGLE_TARGET` is set for all Kotlin packages that support more than one Kotlin feature release. It can be overridden both globally and on a per-package basis in [/etc/portage/package.use].

[FILE] **`/etc/portage/package.use`Overriding `KOTLIN_SINGLE_TARGET`**

    # Unset any global default value, then choose Kotlin 1.5 for all Kotlin packages
    # Only one value can be set for KOTLIN_SINGLE_TARGET, hence '-*'
    */* KOTLIN_SINGLE_TARGET: -* kotlin1-5

    # KOTLIN_SINGLE_TARGET for Kotlin library packages would be affected by the
    # above line too, which will prevent Kotlin library packages not for Kotlin
    # 1.5 from being installed, so the proper KOTLIN_SINGLE_TARGET value for any
    # other Kotlin feature release that is needed must be re-enabled explicitly
    dev-java/kotlin-*:1.4 KOTLIN_SINGLE_TARGET: -* kotlin1-4
    dev-java/kotlin-*:1.6 KOTLIN_SINGLE_TARGET: -* kotlin1-6

    # Per-package settings should be applied after any global settings;
    # otherwise, they will be overridden by the global settings

    # Use Kotlin 1.4 to build dev-java/okio
    dev-java/okio KOTLIN_SINGLE_TARGET: -* kotlin1-4
    # Use Kotlin 1.6 to build dev-java/kotlinx-cli
    dev-java/kotlinx-cli KOTLIN_SINGLE_TARGET: -* kotlin1-6

** Important**\
After adjusting `KOTLIN_SINGLE_TARGET`, and **before** performing a world update, please remember to **manually** install additional slots of dev-lang/kotlin-bin for every Kotlin release that has been selected for at least one package by following the instructions in [#Installing an old feature release](#Installing_an_old_feature_release) (which are also applicable to the case where a newer feature release needs to be installed).

### [Versioned Kotlin tool executables]

To run a Kotlin tool for a specific feature release without changing the preferences via the Kotlin eselect module, the versioned Kotlin tool executables can be used.

`user `[`$`]`kotlinc1.4 -version`

    info: kotlinc-jvm 1.4.32 (JRE 1.8.0_292-b10)

`user `[`$`]`kotlinc1.5 -version`

    info: kotlinc-jvm 1.5.20 (JRE 1.8.0_292-b10)

** Important**\
The versioned executables are exclusive on Gentoo (at least as of now); they are non-standard in the upstream\'s Kotlin compiler distribution. Therefore, the versioned executables should not be used in programs or scripts that are intended to be run on other GNU/Linux distributions or operating systems.

### [Tools that are not available]

If the default Kotlin compiler package does not provide all Kotlin tools, then calling the executable for an absent tool will result in an error message like the following:

`user `[`$`]`kotlinc-js`

     * kotlinc-js is not available in /opt/kotlin-bin-1.4/bin

In this case, users may either temporarily use the [versioned Kotlin tool executable](#Versioned_Kotlin_tool_executables) for a Kotlin feature release that provides the tool (e.g. [kotlinc-js1.5]) or permanently change the default package to another one that provides [kotlinc-js].

## [Usage]

### [][Compile and run the most simple \"hello, world\" program]

A simple Kotlin \"hello, world\" program can be written as follows:

[CODE] **A \"hello, world\" program for Kotlin**

    fun main()

Assuming this program\'s source file is saved to [hello.kt], it can be compiled with [kotlinc], the main executable for the Kotlin compiler:

`user `[`$`]`kotlinc hello.kt`

In this case, the compiled Java class file\'s name will be [HelloKt.class], which can be launched with [kotlin]:

`user `[`$`]`kotlin HelloKt`

    hello, world

If the Kotlin program does not use any class or method from the Kotlin Standard Library, which is true for this version of \"hello, world\" for Kotlin, it can also be run with [java]:

`user `[`$`]`java HelloKt`

    hello, world

### [][Compile and run a \"hello, world\" program which uses the Kotlin Standard Library]

Consider a fancy version of the Kotlin \"hello, world\" program, which creates a list for all the words in the phrase with the [`listOf`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/list-of.html) method and generates the phrase from the list with the [`joinToString`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/join-to-string.html) method, both of which are members of the Kotlin Standard Library:

[CODE] **A \"hello, world\" program for Kotlin which uses the Kotlin Standard Library**

    fun main()

This program can be compiled with [kotlinc] and run with [kotlin] as normal. However, it cannot be run directly with [java]:

`user `[`$`]`kotlinc hello.kt`

`user `[`$`]`kotlin HelloKt`

    hello, world

`user `[`$`]`java HelloKt`

    Exception in thread "main" java.lang.NoClassDefFoundError: kotlin/collections/CollectionsKt
        at HelloKt.main(hello.kt:2)
        at HelloKt.main(hello.kt)
    Caused by: java.lang.ClassNotFoundException: kotlin.collections.CollectionsKt
        at java.net.URLClassLoader.findClass(URLClassLoader.java:382)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:418)
        at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:352)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:351)
        ... 2 more

This is because [kotlin] adds the Kotlin Standard Library to the classpath automatically, whereas [java] does not. The program can still be run with [java] if the classpath is manually set. The Kotlin Standard Library\'s classpath can be obtained through the [java-config] tool. For example, the following command can be used to run the program with [java] and Kotlin Standard Library 1.5:

`user `[`$`]`java -classpath ".:$(java-config -dp kotlin-stdlib-1.5)" HelloKt`

    hello, world

### [][Compile and run a \"hello, world\" program which uses additional libraries]

Consider an even fancier version of the Kotlin \"hello, world\" program, which first creates a stream of words using the [`Stream.of(T...)`](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html#of-T...-) method from Java, then converts the stream to a list with the [`kotlin.streams.toList`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.streams/java.util.stream.-stream/to-list.html) method in **kotlin-stdlib-jdk8**, and finally joins the elements in the list into a string.

[CODE] **A \"hello, world\" program for Kotlin which uses methods from kotlin-stdlib-jdk8**

    import java.util.stream.Stream
    import kotlin.streams.toList

    fun main()

If this program is compiled directly using [kotlinc], there will be errors suggesting that the `kotlin.streams.toList` method cannot be found:

`user `[`$`]`kotlinc hello.kt`

    hello.kt:2:15: error: unresolved reference: streams
    import kotlin.streams.toList
                  ^
    hello.kt:6:24: error: unresolved reference. None of the following candidates is applicable because of receiver type mismatch:
    public inline fun <T> Enumeration<TypeVariable(T)>.toList(): List<TypeVariable(T)> defined in kotlin.collections
    public fun <T> Array<out TypeVariable(T)>.toList(): List<TypeVariable(T)> defined in kotlin.collections
    public fun BooleanArray.toList(): List<Boolean> defined in kotlin.collections
    public fun ByteArray.toList(): List<Byte> defined in kotlin.collections
    public fun CharArray.toList(): List<Char> defined in kotlin.collections
    public fun CharSequence.toList(): List<Char> defined in kotlin.text
    public fun DoubleArray.toList(): List<Double> defined in kotlin.collections
    public fun FloatArray.toList(): List<Float> defined in kotlin.collections
    public fun IntArray.toList(): List<Int> defined in kotlin.collections
    public fun LongArray.toList(): List<Long> defined in kotlin.collections
    public fun <T> Pair<TypeVariable(T), TypeVariable(T)>.toList(): List<TypeVariable(T)> defined in kotlin
    public fun ShortArray.toList(): List<Short> defined in kotlin.collections
    public fun <T> Triple<TypeVariable(T), TypeVariable(T), TypeVariable(T)>.toList(): List<TypeVariable(T)> defined in kotlin
    public fun <T> Iterable<TypeVariable(T)>.toList(): List<TypeVariable(T)> defined in kotlin.collections
    public fun <K, V> Map<out TypeVariable(K), TypeVariable(V)>.toList(): List<Pair<TypeVariable(K), TypeVariable(V)>> defined in kotlin.collections
    public fun <T> Sequence<TypeVariable(T)>.toList(): List<TypeVariable(T)> defined in kotlin.sequences
        var words = stream.toList()

This is caused by [kotlinc] not automatically including [kotlin-stdlib-jdk8.jar] in the classpath. Again, it can be added manually:

`user `[`$`]`kotlinc -classpath "$(java-config -dp kotlin-stdlib-jdk8-1.5)" hello.kt`

`user `[`$`]`kotlin -classpath ".:$(java-config -dp kotlin-stdlib-jdk8-1.5)" HelloKt`

    hello, world

### [Compile and run a Java program which uses the Kotlin Standard Library]

Kotlin code can be called from Java programs, so it is possible to use Kotlin libraries within Java. For example, the following program is the Java equivalent for the Kotlin \"hello, world\" program which uses the Kotlin Standard Library shown in [a previous section](#Compile_and_run_a_.22hello.2C_world.22_program_which_uses_the_Kotlin_Standard_Library).

[CODE] **A \"hello, world\" program for Java which uses the Kotlin Standard Library**

    import java.util.List;

    import static kotlin.collections.CollectionsKt.listOf;
    import static kotlin.collections.CollectionsKt.joinToString;

    public final class Hello

        public static void main(String[] args)
    }

This program can be compiled with [javac] and run with [java], provided that the Kotlin Standard Library is in the classpath:

`user `[`$`]`javac -classpath "$(java-config -dp kotlin-stdlib-1.5)" Hello.java`

`user `[`$`]`java -classpath ".:$(java-config -dp kotlin-stdlib-1.5)" Hello`

    hello, world

### [Compile and run programs with libraries for a newer feature release]

The Kotlin compiler will emit a warning if the classpath contains a library for a newer feature release. For example, the following messages would given by Kotlin compiler 1.4 when Kotlin Standard Library 1.5 is used:

`user `[`$`]`kotlinc1.4 -classpath "$(java-config -dp kotlin-stdlib-1.5)" hello.kt`

    warning: runtime JAR files in the classpath should have the same version. These files were found in the classpath:
        /usr/share/kotlin-stdlib-1.5/lib/kotlin-stdlib.jar (version 1.5)
        /opt/kotlin-bin/lib/kotlin-stdlib.jar (version 1.4)
        /opt/kotlin-bin/lib/kotlin-script-runtime.jar (version 1.4)
        /opt/kotlin-bin/lib/kotlin-reflect.jar (version 1.4)
    warning: consider providing an explicit dependency on kotlin-reflect 1.5 to prevent strange errors
    warning: some runtime JAR files in the classpath have an incompatible version. Consider removing them from the classpath

The warning can be eliminated by not letting [kotlinc] include [kotlin-stdlib.jar] and [kotlin-reflect.jar] it depends on in the classpath for compilation. This is controlled by the `-no-stdlib` option.

`user `[`$`]`kotlinc1.4 -no-stdlib -classpath "$(java-config -dp kotlin-stdlib-1.5)" hello.kt`

### [Compile and run programs with libraries for an older feature release]

If libraries for a feature release older than the compiler\'s version is used, then [kotlinc] will emit an additional warning even if the `-no-stdlib` option is enabled. The following warning would appear when Kotlin compiler 1.5 is used with Kotlin Standard Library 1.4:

`user `[`$`]`kotlinc1.5 -no-stdlib -classpath "$(java-config -dp kotlin-stdlib-1.4)" hello.kt`

    warning: runtime JAR files in the classpath have the version 1.4, which is older than the API version 1.5. Consider using the runtime of version 1.5, or pass '-api-version 1.4' explicitly to restrict the available APIs to the runtime of version 1.4. You can also pass '-language-version 1.4' instead, which will restrict not only the APIs to the specified version, but also the language features
    /usr/share/kotlin-stdlib-1.4/lib/kotlin-stdlib.jar: warning: runtime JAR file has version 1.4 which is older than required for API version 1.5

Specifying the library\'s version with the `-api-version` option, as instructed by the warning, is sufficient to eliminate it.

`user `[`$`]`kotlinc1.5 -api-version 1.4 -no-stdlib -classpath "$(java-config -dp kotlin-stdlib-1.4)" hello.kt`

## [Version upgrade]

### [New incremental or bug fix release]

All small updates that do not involve migration to a new feature release should be installable with [the normal system update method](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Portage#Updating_the_system "Handbook:AMD64/Working/Portage") without any issues.

### [New feature release]

To upgrade to a newer Kotlin feature release, kotlin-stdlib and kotlin-reflect must be re-bootstrapped before the remaining components for the new release can be updated. This is necessary because the upstream bootstraps each new feature release with an RC version of that release instead of the latest version in the previous feature release series. For example, Kotlin 1.5.0 is bootstrapped with version 1.5.0-RC-556^[\[3\]](#cite_note-3)^ instead of 1.4.32.

`root `[`#`]`emerge --ask --oneshot dev-java/kotlin-stdlib-bootstrap dev-java/kotlin-reflect-bootstrap`

`root `[`#`]`emerge --ask --update --deep --newuse @world`

`root `[`#`]`emerge --ask --oneshot dev-java/kotlin-stdlib dev-java/kotlin-reflect`

`root `[`#`]`emerge --ask --depclean`

#### [Staying on a feature release]

Users who installed the Kotlin packages without specifying the slot but would like to stay on the installed feature release of Kotlin can re-add dev-lang/kotlin-bin with a slot to the \"world\" favorites file. If the current installed feature release is 1.4, then please run the following commands:

`root `[`#`]`emerge --deselect dev-lang/kotlin-bin`

`root `[`#`]`emerge --ask --noreplace dev-lang/kotlin-bin:1.4`

## [See also]

-   [Kotlin/Package Maintainer Guide](https://wiki.gentoo.org/wiki/Kotlin/Package_Maintainer_Guide "Kotlin/Package Maintainer Guide")
-   [Kotlin/Library Package Maintainer Guide](https://wiki.gentoo.org/wiki/Kotlin/Library_Package_Maintainer_Guide "Kotlin/Library Package Maintainer Guide") --- useful information for any maintainers of the [Kotlin library packages](https://wiki.gentoo.org/wiki/Kotlin#Available_packages "Kotlin")\' ebuilds.
-   [Kotlin/Open Challenges and Room for Improvement](https://wiki.gentoo.org/wiki/Kotlin/Open_Challenges_and_Room_for_Improvement "Kotlin/Open Challenges and Room for Improvement")

## [External resources]

-   [Kotlin compiler options﻿ reference](https://kotlinlang.org/docs/compiler-reference.html)
-   [Kotlin Standard Library API reference](https://kotlinlang.org/api/latest/jvm/stdlib/)
-   [kotlin.test API reference](https://kotlinlang.org/api/latest/kotlin.test/)

## [References]

1.  [[[↑](#cite_ref-1)] [JetBrains. [Compatibility guide for Kotlin 1.5](https://kotlinlang.org/docs/compatibility-guide-15.html), [Kotlin docs](https://kotlinlang.org/docs/home.html), July 7th, 2021. Retrieved on July 7th, 2021.]]
2.  [[[↑](#cite_ref-2)] [Yuan Liao. [dev-lang/kotlin-bin-1.5.20: Add new JAR to compiler library list](https://github.com/Leo3418/spark-overlay/commit/fb93eb50c856d319cf0e0c483587d08a1268b3a0) (Git commit), July 4th, 2021. Retrieved on July 7th, 2021.]]
3.  [[[↑](#cite_ref-3)] [[gradle.properties](https://github.com/JetBrains/kotlin/blob/v1.5.0/gradle.properties#L20), [JetBrains/kotlin GitHub repository](https://github.com/JetBrains/kotlin), April 4th, 2021. Retrieved on July 7th, 2021. ]]