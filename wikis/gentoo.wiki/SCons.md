**Resources**

[[]][Home](http://www.scons.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/SCons "wikipedia:SCons")

**SCons** is an alternate build system often used by science projects. This small guide gives a developer PoV on SCons.

## Contents

-   [[1] [Using SCons in ebuilds]](#Using_SCons_in_ebuilds)
-   [[2] [Common pitfalls]](#Common_pitfalls)
    -   [[2.1] [Partial rebuilds in src_install()]](#Partial_rebuilds_in_src_install.28.29)
    -   [[2.2] [Missing CC, CFLAGS, LDFLAGS]](#Missing_CC.2C_CFLAGS.2C_LDFLAGS)
-   [[3] [Arguments against using SCons for a project]](#Arguments_against_using_SCons_for_a_project)
    -   [[3.1] [Ignorance of compilation environment settings]](#Ignorance_of_compilation_environment_settings)
    -   [[3.2] [No default installation paths/command]](#No_default_installation_paths.2Fcommand)
    -   [[3.3] [No support for library SONAMEs]](#No_support_for_library_SONAMEs)
    -   [[3.4] [No automation possible]](#No_automation_possible)
    -   [[3.5] [Constant reconfiguration]](#Constant_reconfiguration)
    -   [[3.6] [No support for out-of-source builds]](#No_support_for_out-of-source_builds)
-   [[4] [See also]](#See_also)

## [Using SCons in ebuilds]

[CODE] **An example ebuild using SCons**

    EAPI=4

    inherit multilib scons-utils toolchain-funcs

    # ...

    src_compile()

    src_install() " install
    }

The most important part here is inheriting the [*scons-utils* eclass](https://devmanual.gentoo.org/eclass-reference/scons-utils.eclass/) and using *escons* function. The eclass inherit is going to add SCons into *DEPEND*, and *escons* invokes SCons with *\$* stripped down to ones suitable for SCons.

Note the following, however:

1.  SConstruct files are always highly custom and the calling scheme above is just an example. Although using *CC* as variable is pretty common, the installation root may appear as *DESTDIR* or do not appear at all \-- some packages will require hacking *PREFIX* or even patching;
2.  Although aliasing *install* to the install destination is very common, it\'s no rule either. Sometimes *escons \"\$\"* or *escons /* may need to be used. Or the package may require installation if the author didn\'t provide any kind of installation rules;
3.  SCons has a tendency to reconfigure itself on each call. That\'s why we usually don\'t use *src_configure()* and have to copy most of the args from *src_compile()* to *src_install()* \-- otherwise SCons will re-configure and rebuild the package;
4.  Sometimes install destinations have to passed to the *src_compile()* invocation as well so that package could hardcode appropriate paths. Otherwise package will partially rebuild itself during *src_install()*;
5.  The default *libdir* is passed to autotools by *econf* function. As SCons doesn\'t use that, libdir has to passed manually using *get_libdir()* function from *multilib* eclass. And yes, *LIBDIR* is a custom variable name as well.

## [Common pitfalls]

### [][Partial rebuilds in src_install()]

As mentioned above, SCons often requires passing the same arguments both to *src_compile()* and *src_install()* invocation. If a partial package rebuild occurs in *src_install()*, it is likely that either:

-   an argument passed to *src_compile()* was not repeated in *src_install()* and SCons switched it back to the default,
-   a path passed to *src_install()* is being hardcoded in program sources and needs to be passed in *src_compile()* as well.

Of course, this could also be a case of a broken build system in which some target dependencies are always rebuilt.

### [][Missing CC, CFLAGS, LDFLAGS]

It is very common for SConstruct files to ignore variables like *CC*, *CFLAGS* and especially *LDFLAGS*. The first one needs to be always passed explicitly to the build system (that\'s what *econf* does); sometimes exporting it using *tc-export* will work as well. The latter ones are often missed by project developers and need patching to be set.

## [Arguments against using SCons for a project]

SCons lacks many basic features required from a complete build system and thus it is mostly about reimplementing the wheel a dozen times. And doing that means a lot of pain to users and developers which have to adjust to custom solutions and be hit by repeating bugs in custom implementations.

### [Ignorance of compilation environment settings]

Although SCons is aware itself of a few compilers and various kinds of compilation flags, it doesn\'t actually query the environment for those.

Autotools and multiple custom build systems query the environment variables *CC*, *CXX*, *CFLAGS*, *CXXFLAGS*, *LDFLAGS* (some *CPPFLAGS* and *LIBS* as well) to get the compiler and flags being used. Some others (like plain Makefiles) allow user to pass those as command line arguments.

With SCons, those variables must be declared explicitly. This means that naming is free-form, and user is obligated to look up help for every single project to see their names. As long as they are declared at all, which makes users obligated to report bugs and wait for fixes.

### [][No default installation paths/command]

SCons is very poorly suited for installing. Although it is common to create *install* alias for installing programs, that\'s no rule. Thus, users can\'t trust that and once again have to look up which command to use to install a project. As long as project is installable at all\...

SCons doesn\'t define any default installation paths at all. This means that author has to specify them all, and make them adjustable via custom variables. Users once again have to look help up and hope the path they need to adjust is actually there.

It is also quite common that SCons project lack correct *DESTDIR* setting for fake installation root where files should be installed by the *install* alias while keeping non-*DESTDIR* paths within the package itself.

### [No support for library SONAMEs]

SCons is not suited for building \*nix libraries either. It can only build plain static and shared libraries (so-called *modules*) which are not suitable for versioning. Thus, projects have to manually add custom, linker-specific options to set the SONAME and then additional commands to set up the SONAME symlinks.

And once again, building these two types of libraries has to be added manually while libtool uses common rules to build both static and/or shared variant as requested by user.

### [No automation possible]

As shown above, there\'s no single common thing about SCons build systems. Users have to look up help on each project and create per-project build commands. While with autotools, a simple set of build commands can be created which will suit almost all projects.

Simplest autotools ebuild will look like:

[CODE] **Simplest ebuild using autotools**

    EAPI=4

And that\'s all! All *configure* scripts take the same common arguments, and all (automake) projects support *make install DESTDIR=\...* With SCons, all that has to be specified explicitly.

### [Constant reconfiguration]

Calling SCons for almost anything means performing the configure tests. This includes calling *scons \--help* to get the options to adjust performed tests. And yes, if tests fail hard, the help will not be shown.

With autotools, it is easy to pre-configure a package and build it later. With SCons, all the options must be passed on every call or they will be reset to defaults. That involves passing *CC* to separate *install* call, or risk rebuilding the package using the default compiler.

### [No support for out-of-source builds]

An out-of-source build is a build where intermediate and final output files are created in a directory other than the one where sources are contained. Out-of-source builds can be used to keep source directories tidy, build multiple variants of a package from the same source tree (e.g. 32- and 64-bit variants of a library on multilib amd64) or just build a package from a read-only source directory.

SCons provides no way to perform the build in other directory without copying the whole source tree.

## [See also]

-   [Build systems](https://wiki.gentoo.org/wiki/Build_systems "Build systems") --- software that automates the compilation, clean up, and installation stages of the software creation process.