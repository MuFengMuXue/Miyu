*Not to be confused with [the \".bashrc\" Bash configuration file](https://wiki.gentoo.org/wiki/Bash#.bashrc "Bash").*

The **[/etc/portage/bashrc]** file is a global [bashrc] file referenced by Portage. It is similar to the [bashrc] files under [[/etc/portage/env/](https://wiki.gentoo.org/wiki//etc/portage/env "/etc/portage/env")], except that it\'s sourced for every package. It can either be used to setup a global environment common to all ebuilds, or as an alternative to the [/etc/portage/env] files (allowing Portage administrators to handle all the necessary conditional code manually), or to set up ebuild phase hooks (to perform specific actions at various stages of package installation, updates, or removal).

## Contents

-   [[1] [Hooks]](#Hooks)
    -   [[1.1] [Execution order]](#Execution_order)
    -   [[1.2] [Phase names]](#Phase_names)
    -   [[1.3] [Hook functions]](#Hook_functions)
    -   [[1.4] [EBUILD_PHASE_FUNC and EBUILD_PHASE]](#EBUILD_PHASE_FUNC_and_EBUILD_PHASE)
    -   [[1.5] [Available environment variables]](#Available_environment_variables)
-   [[2] [See also]](#See_also)

## [Hooks]

In order to execute manually-specified code during an ebuild, there are two distinct ways to hook into the ebuild process: via hook functions, and via environment variables.

In the context of [/etc/portage/bashrc], hook functions should be used, as this file will be sourced multiple times during the build - at least once per phase, and several other times as well. Importantly:

** Important**\
Do not rely on use of the `EBUILD_PHASE` or `EBUILD_PHASE_FUNC` variables. Their value in global scope is not supposed to be the name of a phase - refer to [[[bug #908552]](https://bugs.gentoo.org/show_bug.cgi?id=908552)[]].

### [Execution order]

The global [bashrc] isn\'t sourced for the first time until after dependency resolution. If run with `--ask`, [bashrc] is sourced for the first time shortly after interactive confirmation. Therefore, it isn\'t a complete replacement for the global [make.conf]. Anything that must be in the environment immediately - such as USE flags, `FEATURES`, etc. - can\'t be set by [bashrc] The Portage documentation doesn\'t provide a complete list of contradictions, so be careful.

### [Phase names]

The phase names used in hook functions and in the `EBUILD_PHASE_FUNC` variable are:

-   `pkg_setup`
-   `src_unpack`
-   `src_prepare`
-   `src_configure`
-   `src_compile`
-   `src_test`
-   `src_install`
-   `pkg_preinst`
-   `pkg_prerm`
-   `pkg_postrm`
-   `pkg_postinst`

### [Hook functions]

Portage automatically calls certain functions inside [/etc/portage/bashrc] if they are present (ditto [/etc/portage/env/app-misc/foo]). In particular, it calls functions with the name structure ``*`stage_name`*: for example, the `pre_pkg_setup` function will get called just before the `pkg_setup` phase:

[FILE] **`/etc/portage/bashrc`**

    pre_pkg_setup()

Two additional hook functions are also available: `register_die_hook`, called when an ebuild fails; and `register_success_hook`, called when an ebuild is successfully merged, whose usages slightly differ from each other:

[FILE] **`/etc/portage/bashrc`**

    register_success_hook mySuccessHook
    mySuccessHook()

    register_die_hook myDieHook
    myDieHook()

Note, however, that only an ebuild that is emerged flawlessly is considered a sufficient success to call the registered \'`success`\' function(s). For example, a file collision during a build is enough for the function(s) not to be called, even though the rest of the emerge process was successful.

** Warning**\
Defining a function *without* a `pre_` or `post_` prefix, e.g. a function named `pkg_postinst`, would **override** the default expected eclass implementations.

### [`EBUILD_PHASE_FUNC` and `EBUILD_PHASE`]

During the ebuild process, the `EBUILD_PHASE_FUNC` variable is set to the phase names described in the \"[Phase names](#Phase_names)\" section above.

Additionally, during the ebuild process, the `EBUILD_PHASE` variable gets set to the following values:

-   `clean`
-   `setup`
-   `unpack`
-   `prepare`
-   `configure`
-   `compile`
-   `test`
-   `install`
-   `instprep`
-   `preinst`
-   `prerm`
-   `cleanrm`
-   `postinst`
-   `clean`

### [Available environment variables]

Portage doesn\'t save the initial environment prior to being mangled by Portage\'s global [make.defaults] and [make.globals]. Therefore, there is no direct way of determining whether an environment variable was supplied by the user (e.g. CFLAGS) or set by Portage, so it can\'t be guaranteed using the environment by [bashrc] to control behavior.

Variables available for reading in the environment of a bashrc script include:

  --------------------------- ------------------------------------------------------------------------------------------------
  Name                        Description
  `CATEGORY`       Package\'s category, e.g. `app-editors`
  `CFLAGS`         Flags for `$`
  `COMMON_FLAGS`   Flags common to `$` and `$`
  `CXXFLAGS`       Flags for `$`
  `D`              Path to the temporary install directory, e.g. `$/image`
  `EBUILD`         Path to the ebuild file, e.g. `/var/db/repos/gentoo/app-editors/vim/vim-6.3.ebuild`
  `LDFLAGS`        Flags for the compiler driver to pass to its linker
  `MAKEOPTS`       Flags for parallel make
  `P`              Package name and version (excluding revision, if any), e.g. `vim-6.3`
  `PF`             Full package name, `$-$`, e.g. `vim-6.3-r1`
  `PN`             Package name, e.g. `vim`
  `PR`             Package revision, or `r0` if no revision exists
  `PV`             Package version (excluding revision, if any), e.g. `6.3`
  `PVR`            Package version and revision (if any), e.g. `6.3`, `6.3-r1`
  `S`              Path to the temporary build directory, used by `src_compile` and `src_install`
  `T`              Path to a temporary directory which may be used by the ebuild, e.g. `$/temp`
  --------------------------- ------------------------------------------------------------------------------------------------

## [See also]

-   [/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage") --- the primary configuration directory for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), Gentoo\'s package manager.
-   [/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env") --- can contain files to be called during the installation of specific packages, or files used to set Portage\'s environment variables on a per-package basis.
-   [/etc/portage/patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches") --- provide a way to apply patches to package source code when sources are extracted before installation
-   [Handbook:AMD64/Portage/Advanced#Using\_.2Fetc.2Fportage.2Fbashrc_and_affiliated_files](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Advanced#Using_.2Fetc.2Fportage.2Fbashrc_and_affiliated_files "Handbook:AMD64/Portage/Advanced")
-   [Handbook:X86/Portage/Advanced#Using /etc/portage/bashrc and affiliated files](https://wiki.gentoo.org/wiki/Handbook:X86/Portage/Advanced#Using_.2Fetc.2Fportage.2Fbashrc_and_affiliated_files "Handbook:X86/Portage/Advanced")
-   [Portage Manpage](https://dev.gentoo.org/~zmedico/portage/doc/man/portage.5.html)
-   [Knowledge Base:Overriding environment variables per package](https://wiki.gentoo.org/wiki/Knowledge_Base:Overriding_environment_variables_per_package "Knowledge Base:Overriding environment variables per package")