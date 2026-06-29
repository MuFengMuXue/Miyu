**Resources**

[[]][GitHub](https://github.com/ionenwks/iwdevtools)

[[]][Package information](https://packages.gentoo.org/packages/app-portage/iwdevtools)

Iwdevtools is a group of small tools to aid with Gentoo development, primarily intended for QA.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Atomf]](#Atomf)
        -   [[2.1.1] [Invocation]](#Invocation)
        -   [[2.1.2] [Printing a package atom]](#Printing_a_package_atom)
        -   [[2.1.3] [Specific formatting]](#Specific_formatting)
    -   [[2.2] [Eoldnew]](#Eoldnew)
        -   [[2.2.1] [Invocation]](#Invocation_2)
        -   [[2.2.2] [Emerging an older version first]](#Emerging_an_older_version_first)
    -   [[2.3] [Find-unresolved]](#Find-unresolved)
        -   [[2.3.1] [Invocation]](#Invocation_3)
        -   [[2.3.2] [Finding unresolved soname dependencies]](#Finding_unresolved_soname_dependencies)
    -   [[2.4] [Qa-cmp]](#Qa-cmp)
        -   [[2.4.1] [Invocation]](#Invocation_4)
        -   [[2.4.2] [Comparing two packages]](#Comparing_two_packages)
    -   [[2.5] [Qa-openrc]](#Qa-openrc)
        -   [[2.5.1] [Invocation]](#Invocation_5)
        -   [[2.5.2] [Checking a service script]](#Checking_a_service_script)
    -   [[2.6] [Qa-sed]](#Qa-sed)
        -   [[2.6.1] [Invocation]](#Invocation_6)
    -   [[2.7] [Qa-vdb]](#Qa-vdb)
        -   [[2.7.1] [Invocation]](#Invocation_7)
        -   [[2.7.2] [Checking a package]](#Checking_a_package)
    -   [[2.8] [Repo-cd]](#Repo-cd)
        -   [[2.8.1] [Invocation]](#Invocation_8)
        -   [[2.8.2] [Printing information]](#Printing_information)
    -   [[2.9] [Scrub-patch]](#Scrub-patch)
        -   [[2.9.1] [Invocation]](#Invocation_9)
        -   [[2.9.2] [Scrubbing a patch]](#Scrubbing_a_patch)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Portage integration]](#Portage_integration)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-portage/iwdevtools](https://packages.gentoo.org/packages/app-portage/iwdevtools) [[]] [Small tools to aid with Gentoo development, primarily intended for QA]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-portage/iwdevtools`

## [Usage]

### [Atomf]

[atomf] prints package atoms based on the format given as an argument.

#### [Invocation]

`user `[`$`]`atomf --help`

    Usage: atomf [format] <atom(s)...>

    Format <atom> based on [format], or return 9 elements separated by
    spaces if a single atom with no format specified.

    atom can be in dependency-format, or tree-style .ebuild format, e.g.
     *  !!>=cat/name-1.2.3-r1:*/0=[use] ([use] will be discarded)
     *  cat/name/name-1.2.3-r1.ebuild (.ebuild must be present)

    atom can be incomplete, but will return 1 if single elements are seen as
    invalid per the Package Manager Specification (PMS) -- not that this
    should be considered a full atom validator.

    Options:
      -x, --expand        Ignore format and expand multiple atoms to elements
      -s, --unset=STR     When expanding, show STR if unset (default: '?')

      -M, --allow-missing If %c/%n or -%v is specified but atom is missing one
                          of these components, do not exit with error.

      -v, --versplit      Split a version string into elements instead
                          (no characters are dropped for versions)

          --confdir=PATH  Configuration dir to use instead of defaults
                          (/etc/iwdevtools + ~/.config/iwdevtools)
          --dumpconfig    Display config and exit (> atomf.conf)

      -h, --help          Display usage information and exit
          --version       Display version information and exit

    *Format*
     0.  %! Blocker indicator (!, !!, or none)
     1.  %o Version range operator (>=, >, etc... or none)
     2.  %c Category (ending with / if set)
     3.  %n Name
     4.  %v Version (starting with - if set)
     5.  %r Revision (as -rN, or none)
     6.  %s Slot (as :0, or none)
     7.  %u Subslot (as /0, or none)
     8.  %b Binding operator (= or none)
     -.  %% Literal %
    e.g. "%c%n%v%r" = category/name-1.0-r1

     -.  %p Equivalent to %c%n (category/pn)
     -.  %e Equivalent to %v%r (pvr)
     -.  %f Equivalent to %c%n%v%r (category/pf)

    %R,%S,%U alternatively display %r,%s,%u without prefixes, and as 0 if unset.
    %C,%V similarly strip the / and -, and still empty if unset.

    If one of %c, %n, or %v (or equivalent) is requested, but is missing from the
    atom, will report error for that atom and later exit with return status 2
    unless --allow-missing.

    *Notes*
    If need to use this in a bash script extensively, it is recommended to source
    /usr/share/iwdevtools/atomf.bashlib directly rather than call this.
    Its atoma() also allows for, e.g. $, and atomset() for $.

#### [Printing a package atom]

By default, atomf will print all 9 format types if no format is specified:

`user `[`$`]`atomf ">=sys-libs/glibc-2.38-r10"`

    ? >= ? glibc 2.38 10 ? ?

With the following columns denoting:

1.  Blocker indicator
2.  Version range operator
3.  Category
4.  Package name
5.  Version
6.  Revision
7.  Slot
8.  Subslot
9.  Binding operator

#### [Specific formatting]

To print just the package\'s name, pass the format in first:

`user `[`$`]`atomf %n ">=sys-libs/glibc-2.38-r10"`

    glibc

### [Eoldnew]

[eoldnew] is a helper program for [qa-cmp] which emerges the package defined by \<atom\> but by first emerging its previous (visible) version if not already installed.

#### [Invocation]

`user `[`$`]`eoldnew --help`

    Usage: eoldnew [2-9][-] <atom> [emerge option]...

    Helper for using `qa-cmp` which emerges the package defined by <atom> but
    by first emerging its previous (visible) version if not already installed.

    If [2-9] is provided as first argument, go back N versions.

    If `-` is specified (e.g. `eoldnew -` or `eoldnew 2-`), will only
    emerge the previous and not the newest.

    Any options after <atom> are passed to emerge as-is.

    Options:
      -h, --help     Display usage information and exit
          --version  Display version information and exit

    *Note*
    This exports IWDT_ALL=y (see help text of other iwdevtools commands)

    Environment:
      EOLDNEW_EMERGE_CMD=emerge  If need to call something else than emerge(1)
      EOLDNEW_EMERGE_ARGS=       Similar to EMERGE_DEFAULT_OPTS
      EOLDNEW_EMERGE_ARGS_OLD=   Only used when emerging old
      EOLDNEW_EMERGE_ARGS_NEW=   Only used when emerging new
    Note it is possible to set these in portage's make.conf as well, and _ARGS
    environment will replace instances of  by the specified <atom>, e.g.
      EOLDNEW_EMERGE_ARGS_NEW="--usepkg-exclude "

#### [Emerging an older version first]

To emerge an older version of a package, pass the argument in with any other arguments after it being emerge arguments:

`user `[`$`]`eoldnew app-editors/vim --pretend`

### [Find-unresolved]

[find-unresolved] is primarily intended for working with embedded systems and ensuring no needed libraries are missing (normally portage verifies this automatically).

#### [Invocation]

`user `[`$`]`find-unresolved --help`

#### [Finding unresolved soname dependencies]

To scan a directory for unresolved dependencies, pass the directory in as an argument:

`user `[`$`]`find-unresolved /`

     * Scanning / for unresolved soname dependencies...
    scanelf: rpath_security_checks(): Security problem NULL DT_RUNPATH in opt/rust-bin-1.76.0/lib/libLLVM-17-rust-1.76.0-stable.so
     * Seems all good if the following libraries can be found at runtime:
       - libjvm.so
       - libunoidllo.so
       - libmozwayland.so
       - libjli.so
       - libmozsqlite3.so
       - libsystemd-shared-255.so
       - liblgpllibs.so
       - libgkcodecs.so
       - libmozsandbox.so
       - libmozavutil.so
       - libjava.so
       - libmozgtk.so
       - libxul.so
       - libuno_sal.so.3
       - libuno_salhelpergcc3.so.3

### [Qa-cmp]

[qa-cmp] compares the image installation of one atom to another.

#### [Invocation]

`user `[`$`]`qa-cmp --help`

    Usage: qa-cmp <atom|image> [atom2|image2]

    Compares an installation image (i.e. $/[...]/image/),
    with either another image or the currently installed system copy.

    Arguments can either be a path to the image, or an atom representing it.
    If atom is imprecise (i.e. no version), or only one is given, then will
    guess the right versions based on timestamps (older with newest).

    Options:
      -f, --no-filelist     Do not print filelist differences
      -s, --no-soname       Do not print SONAME differences
      -a, --no-abidiff      Do not print per-libraries abidiff
      -z, --no-size         Do not print size differences when above threshold
      -r, --no-report       Do not report statistics at the end
      -x, --no-compare      Short for all of the above (intended for --single-*)
    (unless -r/-x, report will still have statistics for disabled options)

      -T, --size-thres=%    Size difference percentage at which to display it
                            (default: 10.0%, 0 to always display)

      -B, --full-abidiff    Show complete abidiff output
      -d, --quiet-nodebug   Do not warn if missing debug for abidiff (unless -W)
          --timeout=[SECS]  Terminate abidiff after SECS seconds, can be very slow
                            with some C++ libraries (default: 10, unlimited if 0)

      -I, --image-only      When guessing what to compare, ignore system's copy.
                            (simplifies comparing two images)

      -p, --ignore-perms    Do not show file permissions differences in filelist
                            (needed if system has special permission handling)
      -P, --show-perms      Always show file permissions even if no differences
      -K, --ver-keep        Do not replace filelist's versions+slots in names by *
      -O, --ver-dironly     Limit filelist version replacements to directories
    (default is to try to prevent showing uninteresting version-only changes)

          --no-skip-large   Do not abort even if operations would be slow when
                            over 10000 installed files (e.g. gentoo-sources)

      -M, --allow-missing   Do nothing and exit normally if lacking a 2nd image
                            (intended for automated scripts)

      -W, --confirm         Show all statistics even if no changes as confirmation

      -F, --single-filelist Show full filelist for latest
      -S, --single-soname   Show full soname list for latest
      -Z, --single-size     Show size for latest
      -L, --single-all      Short for --single-
      -U, --single-auto     Auto-disable specified --single-* if two images
                            (--single-* options can function with a single image)

      -c, --no-color        Disable use of colors

          --confdir=PATH    Configuration dir to use instead of defaults
                            (/etc/iwdevtools + ~/.config/iwdevtools)
          --dumpconfig      Display config and exit (> qa-cmp.conf)

          --root=PATH       Set ROOT (command-line-only, default: '')
          --eprefix=PATH    Set EPREFIX (likewise, default: '')

      -h, --help            Display usage information and exit
          --version         Display version information and exit

    *Abidiff Notes*
    Requires debug symbols for full report (FEATURES=splitdebug and -g).
    Report showing '[BREAKING]' doesn't necessarily mean it's breaking
    revdeps without rebuilds, but it warrants testing them while built
    against old version. Order matters, downgrading often breaks ABI.

    *Known Limitations*
    May report incorrect changes if pkg_postinst or FEATURES performed live changes
    on files or permissions that are missing from the image (e.g. fcaps.eclass).

    *Portage Integration*
    Can be integrated by using /etc/portage/bashrc, either by using the
    example /usr/share/iwdevtools/bashrc or by manually adding:

        source /usr/share/iwdevtools/qa-cmp.bashrc

        post_pkg_preinst()

    bashrc environment options (export/make.conf/package.env):
      QA_CMP=y | =n         Enable or disable, can also use IWDT_ALL=y | =n
      QA_CMP_CMD=qa-cmp     This script, needs to be changed if not in PATH
      QA_CMP_ARGS=          Extra arguments to pass, see options above
      QA_CMP_LOG=eqawarn    Portage output command, can also use IWDT_LOG=ewarn
    Note: eqawarn post-emerge log needs "qa" in make.conf's PORTAGE_ELOG_CLASSES

#### [Comparing two packages]

First, ensure both have been built with their image directories intact, i.e. by using [ebuild \... clean install]

Next, run [qa-cmp]:

`root `[`#`]`qa-cmp category/package-1.0.0 category/package-2.0.0`

If nothing outputs then there were no differences.

### [Qa-openrc]

Similar to [qa-cmp], this scans an image directory to report issues in OpenRC scripts.

#### [Invocation]

`user `[`$`]`qa-openrc --help`

    Usage: qa-openrc [-O <service-script>...] [<atom|image>]

    Reports common mistakes in OpenRC service scripts. If scripts are not
    given with the -O option, will look for scripts in the given installation
    image (i.e. $/[...]/image/), or the currently installed
    system copy matching the given atom.

    Options:
      -p, --no-perms     Disable file permissions QA check
      -s, --no-ssd-args  Disable start_stop_daemon_args linter

      -O, --openrc       Run checks on given scripts rather than the atom/image

          --confdir=PATH Configuration dir to use instead of defaults
                         (/etc/iwdevtools + ~/.config/iwdevtools)
          --dumpconfig   Display config and exit (> qa-openrc.conf)

          --root=PATH    Set ROOT (command-line-only, default: '')
          --eprefix=PATH Set EPREFIX (likewise, default: '')

      -h, --help         Display usage information and exit
          --version      Display version information and exit

    *Notes*
    This is currently basic with few checks, will be extended as needed and
    is a subject to breaking changes. Note that portage already checks for
    bashisms if have dev-util/checkbashisms.

    *Portage Integration*
    Can be integrated by using /etc/portage/bashrc, either by using the
    example /usr/share/iwdevtools/bashrc or by manually adding:

        source /usr/share/iwdevtools/qa-openrc.bashrc

        post_pkg_preinst()

    bashrc environment options (export/make.conf/package.env):
      QA_OPENRC=y | =n         Enable or disable, can also use IWDT_ALL=y | =n
      QA_OPENRC_CMD=qa-openrc  This script, needs to be changed if not in PATH
      QA_OPENRC_ARGS=          Extra arguments to pass, see options above
      QA_OPENRC_LOG=eqawarn    Portage output command, can also use IWDT_LOG=ewarn
    Note: eqawarn post-emerge log needs "qa" in make.conf's PORTAGE_ELOG_CLASSES

#### [Checking a service script]

`root `[`#`]`qa-openrc category/package-1.0.0`

### [Qa-sed]

** Note**\
[qa-sed]\'s primary purpose is to be used as a Portage integration, although it can be used individually

[qa-sed] reports when all files were unmodified to detect outdated constructs, similar to [patch].

#### [Invocation]

`user `[`$`]`qa-sed --help`

    Usage: qa-sed [sed option]... [--qa-sed-args] [option]...

    sed wrapper that reports when all files were unmodified to help with
    detection of outdated constructs similarly to a failing patch.

    This is primarily meant to be integrated with portage rather than used
    on its own (but still can), see portage integration below.

    Options:
          --qa-sed-args  Allow other options to be used and not passed to sed

      -A, --all          By default (if --func is provided) sed commands not ran
                         directly in defined phase functions are ignored to suppress
                         noise from eclasses, this forces to show everything

          --func=NAME    Function name sed command was called from
          --source=FILE  Path to the source file calling sed
          --lineno=NUM   Line number that called sed (for referencing)

      -X, --error-on-qa  Return exit code >128 if QA issues rather than sed's own
                         (will trigger `|| die` in ebuilds)

          --confdir=PATH Configuration dir to use instead of defaults
                         (/etc/iwdevtools + ~/.config/iwdevtools)
          --dumpconfig   Display config and exit (2> qa-sed.conf)

      -h, --help         Display usage information and exit
          --version      Display version information and exit

    *Caveats*
     *  does not know if a sed only replaces under specific conditions
        e.g. 's|/usr|$/usr|', or 's|lib|$(get_libdir)|'
        consider: use prefix, [[ $(get_libdir) != lib ]], placeholders, etc...
     *  can only verify different sed expressions if passed as separate
        -e arguments rather than a single 's/a/b/; s/c/d/'
     *  can't do detection if stdin is used and isn't a file
        e.g. `cat file | sed` rather than `sed < file` (latter works)
        this is due to a precaution to ensure input will not be mangled
     *  can't handle e/r/w sed commands (will abort with a sandbox error)

    *Portage Integration*
    Can be integrated by using /etc/portage/bashrc, either by using the
    example /usr/share/iwdevtools/bashrc or by manually adding:

        source /usr/share/iwdevtools/qa-sed.bashrc

    Creates a sed() function that most things will use instead. Should, in
    theory, not break anything as it will call sed with same arguments even
    on error -- but use with caution nonetheless, not for production.
    Note that `find . -exec sed  +` bypasses the shell wrapper entirely.

    bashrc environment options (export/make.conf/package.env):
      QA_SED=y | =n         Enable or disable, can also use IWDT_ALL=y | =n
      QA_SED_CMD=qa-sed     This script, needs to be changed if not in PATH
      QA_SED_ARGS=          Extra arguments to pass, see options above
      QA_SED_LOG=eqawarn    Portage output command, can also use IWDT_LOG=ewarn
    Note: eqawarn post-emerge log needs "qa" in make.conf's PORTAGE_ELOG_CLASSES

### [Qa-vdb]

[qa-vdb] performs basic QA checks based on [/var/db/pkg]\'s contents.

#### [Invocation]

`user `[`$`]`qa-vdb --help`

    Usage: qa-vdb [option]... <atom>

    Perform basic QA checks based on vdb's contents (/var/db/pkg). Currently
    supports comparing RDEPEND with DT_NEEDED (i.e. from `scanelf -n`), and
    doing simple verification of binding operators / slots.

    <atom> can be the exact vdb entry, or anything portage accepts
      e.g. sys-devel/gcc:10, portage-utils, ~sys-apps/portage-3.0.20

    Options:
      -s, --no-slot            Exclude slots (e.g. needing :3 on gtk+, or :*)
      -b, --no-bind            Exclude binding operators (implies --no-overbind)
      -o, --no-overbind        Exclude superfluous binds (i.e. for subslot 0)
      -x, --no-extra           Exclude listed dependencies that seem unused
    (using all --no-* or -sbx will limit to entirely missing deps)

      -e, --exclude=LIST       Comma separated list of category/package to
                               exclude, can also be specified multiple times
                               (example: dev-python/*,sys-libs/glibc,*/gcc)
          --exclude-slot=LIST  Like --exclude but to selectively --no-slot
          --exclude-bind=LIST  Like --exclude but to selectively --no-bind
          --exclude-extra=LIST Like --exclude but to selectively --no-extra
          --exclude-lib=LIST   Similar to --exclude but takes .so libraries
                               as arguments and excludes if seen in DT_NEEDED
    (packages that provide no shared libraries are always excluded)

      -D, --depend             Check against DEPEND rather than RDEPEND
                               (virtuals will still use RDEPEND)

      -W, --confirm            Show confirmation if no issues rather than silence

      -u, --ignore-uninstalled Allows to keep going if a dependency that should
                               be in vdb, isn't. In theory this should never
                               happen without package.provided or bugs.

          --ldconf=CONF        ld.so.conf to use (default: /etc/ld.so.conf)
      -p, --no-ldpath          Disable using ld.so.conf to find libraries' path
    (ldpath allows more accurate reports, but may miss rpath-based dependencies)

      -U, --unified            Use `diff -U` for output instead builtin
      -F, --full               When showing differences, display unchanged as well

      -c, --no-color           Disable use of colors

      -r, --no-default-exclude Ignore configuration files for excludes
          --confdir=PATH       Configuration dir to use instead of defaults
                               (/etc/iwdevtools + ~/.config/iwdevtools)
          --dumpconfig         Display config and exit (> qa-vdb.conf)

          --root=PATH          Set ROOT (command-line-only, default: '')
          --eprefix=PATH       Set EPREFIX (likewise, default: '')

      -h, --help               Display usage information and exit
          --version            Display version information and exit

    *Notes*
    Output is not a hard indication that something needs fixing (especially
    with seemingly unused dependencies that may still be using dlopen(),
    executables, or data files) and needs a human to interpret it. Exclusions
    can be used if something is known to be right.

    *Known Limitations*
    Missing slots won't be displayed when a binding operator (:=) is used as
    portage records the slot even if it was missing from the ebuild.

    No warning is given for libraries that are missing entirely or not associated
    with an installed package. For the former, please use portage's default enabled
    FEATURES="qa-unresolved-soname-deps" to be informed.

    *Portage Integration*
    Can be integrated by using /etc/portage/bashrc, either by using the
    example /usr/share/iwdevtools/bashrc or by manually adding:

        source /usr/share/iwdevtools/qa-vdb.bashrc

        post_pkg_postinst()

    bashrc environment options (export/make.conf/package.env):
      QA_VDB=y | =n         Enable or disable, can also use IWDT_ALL=y | =n
      QA_VDB_CMD=qa-vdb     This script, needs to be changed if not in PATH
      QA_VDB_ARGS=          Extra arguments to pass, see options above
      QA_VDB_LOG=eqawarn    Portage output command, can also use IWDT_LOG=ewarn
    Note: eqawarn post-emerge log needs "qa" in make.conf's PORTAGE_ELOG_CLASSES

#### [Checking a package]

To check a package in [/var/db/pkg]:

`user `[`$`]`qa-vdb category/package-1.0.0`

### [Repo-cd]

[repo-cd] prints the directory of an atom and displays useful information relating to the package.

#### [Invocation]

`user `[`$`]`repo-cd --help`

    Usage: repo-cd [option]... [atom]

    Print directory location (or change directory with *Shell Integration*
    below) plus some information corresponding to an atom either using
    /etc/portage/repos.conf or a repo list given using the -P or --path option.

    atom can be partial or missing, e.g. from dev-category/example::repo
     > dev-category : print the category directory location
     > example      : lookup matches in all categories
     > example::repo: limit to a specific repo
     > (nothing)    : print the repository's top level directory
     > .            : run again for current directory
    In all cases, will ask if multiple results unless -1 or --first is specified.

    Options:
      -P, --path=PATH     Colon-separated list of repos to search by priority,
                          special keyword "default" adds all from repos.conf
                          and "." will search current directory if it is a repo
                          (e.g. --path="~/gentoo:default:.", see --dumpconfig
                          or *Shell Integration* below to set permanently)
      -D, --duplicates    Allow multiple repos with the same profiles/repo_name
                          (e.g. keep /var/db/repos/gentoo even if have ~/gentoo)

      -1, --first         Disable interactive prompts and always pick first choice

      -F, --fuzzy         Always enable fuzzy search (e.g. 'gcc' matches both 'gcc'
                          and 'gcc-config'), used by default if no exact name match
      -f, --exact         Do not return fuzzy matches even if no exact name match
                          (this still allows matching in multiple categories)

      -e, --exclude=LIST  Comma-separated list of categories to exclude from
                          searches unless explicitly specified
                          (default: acct-user,acct-group,dev-haskell,virtual)

          --fields=LIST   Comma-separated list of information to display,
                          prefix with - to disable e.g. =all,-pgo
                          (choices: dir,desc,home,remote,maint,pgo,bgo
                          all by default, pgo+bgo are only for the Gentoo repo)
      -q, --quiet         Do not display non-error informational messages
                          (to be further quiet, also set --no-command)

      -R, --run=COMMAND   If atom matches a package, run COMMAND then exit with
                          its status, see *Running Commands* for details
                          (default: ls -1v --color=always)
      -s, --no-capture    Redirect COMMAND's output to stderr rather than capture
      -r, --no-command    Do not run COMMAND even if defined

          --posix=ALIAS   Print posix sh integration, see *Shell Integration* below
          --bash=ALIAS    Print bash integration with atom completion support
          --fish=ALIAS    Print fish integration with atom completion support
          --zsh=ALIAS     Print zsh integration with atom completion support
          --compgen       Print words for completion with a partial [atom] and exit

      -c, --no-color      Disable use of colors

          --confdir=PATH  Configuration dir to use instead of defaults
                          (/etc/iwdevtools + ~/.config/iwdevtools)
          --dumpconfig    Display config and exit (2> repo-cd.conf)

          --root=PATH     Set ROOT (command-line-only, default: '')
          --eprefix=PATH  Set EPREFIX (likewise, default: '')

      -h, --help          Display usage information and exit
          --version       Display version information and exit

    *Known Limitations*
    Some information may be missing if ebuilds rely on eclasses to set DESCRIPTION
    or HOMEPAGE without metadata/md5-cache. cpe-type remote-ids are unsupported.
    Initial invocation may be slow until the system caches the repo directories.

    *Running Commands*
    If match a valid package, --run's COMMAND will be executed inside the directory
    allowing to e.g. show directory contents (default), eshowkw / pkgdev showkw,
    git status/log, pkgcheck, and/or display notes/reminders based on the package
    name for some ideas. The variables RCD_CATEGORY, RCD_PN, RCD_PACKAGE (cat/pn),
    and RCD_REPONAME are exported for use with external scripts.

    For example, to see keywords using app-portage/gentoolkit, try:

        repo-cd --run="eshowkw -C" sys-apps/portage

    Note can set "run = eshowkw -C" in ~/.config/iwdevtools/repo-cd.conf,
    or pass --run= to the eval command in *Shell Integration* below to be permanent.

    *Shell Integration*
    To be able to change the directory of an interactive shell, a higher level
    helper is required, i.e. if repo-cd prints a path, then cd to it.

    For convenience, can use one of the shell integration option, e.g. --bash=rcd
    outputs code to enable `rcd [atom]` with atom tab completion support using
    bash. Intended to be added to ~/.bashrc and/or ~/.bash_profile (can also run
    in current shell to use immediately):

        eval "$(command repo-cd --bash=rcd)"

    Can also pass other options like --path or --run to the above for per-aliases
    effects. The above eval works the same for each supported shells, except e.g.
    swap --bash for --zsh and use ~/.zshrc, or --fish and ~/.config/fish/conf.d

#### [Printing information]

To print the information for a package, pass it as an argument:

`user `[`$`]`repo-cd app-editors/vim`

     > /var/db/repos/gentoo/app-editors/vim
    /var/db/repos/gentoo/app-editors/vim
     D Vim, an improved vi-style text editor (9999)
     H https://www.vim.org (9999)
     H https://github.com/vim/vim/
     G https://packages.gentoo.org/packages/app-editors/vim
     G https://bugs.gentoo.org/buglist.cgi?quicksearch=app-editors%2Fvim
     M xxc3ncoredxx@gmail.com vim@gentoo.org proxy-maint@gentoo.org
     + Manifest
     + files
     + metadata.xml
     + vim-9.0.1503.ebuild
     + vim-9.0.1627.ebuild
     + vim-9.0.1678.ebuild
     + vim-9.0.1777.ebuild
     + vim-9.0.2092.ebuild
     + vim-9.0.2167.ebuild
     + vim-9999.ebuild

### [Scrub-patch]

[scrub-patch] strips patches of any unnecessary data to reduce size and improve readability.

#### [Invocation]

`user `[`$`]`scrub-patch --help`

    Usage: scrub-patch [option]... [patch]...

    Strip patches of typically useless cruft such as "diff --git"
    lines and timestamps to reduce size and improve readability.

    Patches can be passed either as arguments or through stdin,
    and either modified in-place (i.e. sed(1)'s -i) or to stdout.

    Options:
      -e, --edit         Open patch in $EDITOR after scrubbing and before QA
                         (e.g. to add links before unnecessary warnings)

      -g, --git          Convert `leading-1.0/file` to git-style `a/file`
                         rather than warn (do not use if not a -p1 patch)
      -1, --p0p1         Add one directory level to every files (-p0 -> -p1)

      -q, --quiet        Don't nag about possible QA issues
      -n, --dry-run      Don't scrub and only nag about QA instead

      -s, --no-sanity    Disable `file` check for if being misdetected

      -i, --in-place     Force `sed -i`-like behavior (no autodetect)
      -o, --stdout       Always output the modified patch to stdout (no autodetect)

      -c, --no-color     Disable use of colors

          --confdir=PATH Configuration dir to use instead of defaults
                         (/etc/iwdevtools + ~/.config/iwdevtools)
          --dumpconfig   Display config and exit (> scrub-patch.conf)

      -h, --help         Display usage information and exit
          --version      Display version information and exit

#### [Scrubbing a patch]

To scrub a patch, pass it in as the first argument:

`user `[`$`]`scrub-patch fix.patch`

## [Configuration]

### [Portage integration]

Iwdevtools provides hooks into portage via a bashrc file at [/usr/share/iwdevtools/bashrc]. To add these to Portage\'s bashrc for hooks, copy iwdevtools\'s bashrc:

[FILE] **`/etc/portage/bashrc`**

    # Either symlink, copy, or source using /etc/portage/bashrc to load everything.
    # Assumes not already using post_pkg_*(), adjust if needed (just an example).

    if \
        . "/usr/share/iwdevtools/qa-cmp.bashrc" &&
        . "/usr/share/iwdevtools/qa-openrc.bashrc" &&
        . "/usr/share/iwdevtools/qa-sed.bashrc" &&
        . "/usr/share/iwdevtools/qa-vdb.bashrc"; then
        post_pkg_preinst()

        post_pkg_postinst()
    fi

    # vim: ts=4 ft=ebuild

## [See also]

-   [Pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") --- a collection of tools for Gentoo development.