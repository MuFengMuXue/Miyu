This page contains [[changes](https://wiki.gentoo.org/index.php?title=Python&oldid=1429669&diff=1434119)] which are not marked for translation.

[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=Python&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

Other languages:

-   [English]

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Python "Project:Python")][Project](https://wiki.gentoo.org/wiki/Project:Python "Project:Python")

[[]][Home](https://www.python.org/)

[[]][Official documentation](https://docs.python.org/)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/python)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language) "wikipedia:Python (programming language)")

[[]][GitHub](https://github.com/python/cpython)

[[]][Official project wiki](https://wiki.python.org/moin/FrontPage)

[[]][[#python](ircs://irc.libera.chat/#python)] ([[webchat](https://web.libera.chat/#python)])

[[]][[comp.lang.python](news:comp.lang.python) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.lang.python))]

[[]][r/Python](https://reddit.com/r/Python)

**Python** is an extremely popular cross-platform object oriented programming language.

Python powers [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect"), [equery](https://wiki.gentoo.org/wiki/Equery "Equery"), and many other tools in Gentoo.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Setting the active interpreter]](#Setting_the_active_interpreter)
-   [[3] [Version upgrade]](#Version_upgrade)
    -   [[3.1] [Profile update]](#Profile_update)
    -   [[3.2] [Elective version upgrade]](#Elective_version_upgrade)
    -   [[3.3] [Cleanup]](#Cleanup)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Invocation]](#Invocation)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

Since Python is so integral to Gentoo there is little chance it is not installed. Doing so would be like removing the heart from Gentoo. There are occasions where Python must be recompiled in order to add new features or to upgrade.

### [USE flags]

### [USE flags for] [dev-lang/python](https://packages.gentoo.org/packages/dev-lang/python) [[]] [An interpreted, interactive, object-oriented programming language]

  ----------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+ensurepip`](https://packages.gentoo.org/useflags/+ensurepip)               Install the ensurepip module that uses bundled wheels to bootstrap pip and setuptools (if disabled, it will be only possible to use venv \`\--without-pip\`)
  [`+ncurses`](https://packages.gentoo.org/useflags/+ncurses)                   Add ncurses support (console display library)
  [`+readline`](https://packages.gentoo.org/useflags/+readline)                 Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`+sqlite`](https://packages.gentoo.org/useflags/+sqlite)                     Add support for sqlite - embedded sql database
  [`+ssl`](https://packages.gentoo.org/useflags/+ssl)                           Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`+xml`](https://packages.gentoo.org/useflags/+xml)                           Add support for XML files
  [`berkdb`](https://packages.gentoo.org/useflags/berkdb)                       Add support for sys-libs/db (Berkeley DB)
  [`bluetooth`](https://packages.gentoo.org/useflags/bluetooth)                 Build Bluetooth protocol support in socket module
  [`debug`](https://packages.gentoo.org/useflags/debug)                         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`examples`](https://packages.gentoo.org/useflags/examples)                   Install examples, usually source code
  [`gdbm`](https://packages.gentoo.org/useflags/gdbm)                           Add support for sys-libs/gdbm (GNU database libraries)
  [`jit`](https://packages.gentoo.org/useflags/jit)                             Enable experimental Just-In-Time compilation support.
  [`libedit`](https://packages.gentoo.org/useflags/libedit)                     Use the libedit library (replacement for readline)
  [`pgo`](https://packages.gentoo.org/useflags/pgo)                             Optimize the build using Profile Guided Optimization (PGO) by running Python\'s test suite and collecting statistics based on its performance. This will take longer to build.
  [`tail-call-interp`](https://packages.gentoo.org/useflags/tail-call-interp)   Enable the tail call interpreter. May lead to better performance but is still new and dependent on latest toolchain versions (Clang 19, GCC 15).
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tk`](https://packages.gentoo.org/useflags/tk)                               Add support for Tk GUI toolkit
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)                   Disable pymalloc when running under dev-debug/valgrind is detected (may incur minor performance penalty even when valgrind is not used)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)               Verify upstream signatures on distfiles
  [`wininst`](https://packages.gentoo.org/useflags/wininst)                     Install Windows executables required to create an executable installer for MS Windows
  ----------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-11 03:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Python is slotted, which means that more than one Python version can be installed on a Gentoo system at the same time. Select the version to install by using an `:` (colon) and the package atom followed by one of the slot numbers:

For example, to install Python 3.8:

`root `[`#`]`emerge --ask dev-lang/python:3.8`

## [Configuration]

### [Setting the active interpreter]

** Note**\
See the news item [Python preference to follow PYTHON_TARGETS](https://gitweb.gentoo.org/data/gentoo-news.git/plain/2021-01-30-python-preference-to-follow-python-targets/2021-01-30-python-preference-to-follow-python-targets.en.txt?id=3acbe0b422cb85f2895c0d825d272e37edae41f1) from 2021-01-30.

There are two ways:

1.  Using [python-exec.conf]
2.  The older [[[app-eselect/eselect-python]](https://packages.gentoo.org/packages/app-eselect/eselect-python)[]] method

The default (non-versioned) active interpreter is controlled through package [[[dev-lang/python-exec]](https://packages.gentoo.org/packages/dev-lang/python-exec)[]]. See [python-exec](https://wiki.gentoo.org/wiki/Project:Python/python-exec "Project:Python/python-exec"). Each time [[[dev-lang/python-exec]](https://packages.gentoo.org/packages/dev-lang/python-exec)[]] is emerged/rebuilt, use [dispatch-conf], [cfg-update] or similar to accept or deny proposed modification to [/etc/python-exec/python-exec.conf] (that control the default Python interpreter)

The older way to change the active Python (non-versioned) interpreter is via [[[app-eselect/eselect-python]](https://packages.gentoo.org/packages/app-eselect/eselect-python)[]]. See [eselect-python](https://wiki.gentoo.org/wiki/Project:Python/python-exec#eselect-python "Project:Python/python-exec"). The [eselect python] command will remain as a wrapper to [python-exec.conf] modification if [[[app-eselect/eselect-python]](https://packages.gentoo.org/packages/app-eselect/eselect-python)[]] is in the `@world` set.

## [Version upgrade]

** Note**\
Python 2.7 has reached its end-of-life by January 1, 2020, as per [this official statement](https://www.python.org/doc/sunset-python-2/).

Version upgrades can be elective, or may have to happen due to a profile update.

### [Profile update]

When a Python version becomes deprecated, or is no longer supported, it may cause a profile update to set the PYTHON_SINGLE_TARGET to a higher version. This may cause emerge conflicts when updating a system.

The easiest way to handle this is to add the new Python version to the PYTHON_TARGETS, e.g. for the transition from python3_7 to python3_8:

[FILE] **`/etc/portage/package.use`**

    */* PYTHON_TARGETS: python3_7 python3_8

Then update the system:

`root `[`#`]`emerge --ask --update --newuse --deep @world`

Remove the support for the previous Python version, by removing the line added to [/etc/portage/package.use] and rebuild the system again.

### [Elective version upgrade]

Users may select to upgrade their Python version also by choice. Before starting ensure that the system is up to date:

`root `[`#`]`emerge --ask --update --newuse --deep @world`

To make system packages be rebuilt using the new Python implementation update the `PYTHON_TARGETS` and `PYTHON_SINGLE_TARGET` variables in [/etc/portage/package.use]. For example, when updating from Python 3.6 to 3.7:

[FILE] **`/etc/portage/package.use`**

    */* PYTHON_TARGETS: python3_7
    */* PYTHON_SINGLE_TARGET: -* python3_7

Then update the system again using the `--changed-use --deep` options:

`root `[`#`]`emerge --ask --changed-use --deep @world`

You may be asked to update any remaining `python_targets_python3_6` USE flags as well.

Note that some popular packages still require `PYTHON_SINGLE_TARGET` variable to be set to `python2_7` due to various dependencies.

### [Cleanup]

[]  As of **Jan 19, 2021**, the information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=Python&action=edit).

Once the upgrade has completed, old Python implementations can be removed from the system using:

`root `[`#`]`emerge --ask --depclean dev-lang/python`

After depclean [eselect python list] will still show old Python versions if they were previously selected, to remove these entries run the following command:

`root `[`#`]`eselect python cleanup`

** Note**\
The old [python-updater] has been removed from the Gentoo ebuild repository by [this commit](https://gitweb.gentoo.org/repo/gentoo.git/commit/app-admin/python-updater?id=34d03159133e33002416659c6a287368f1858288).

## [Usage]

### [Invocation]

`user `[`$`]`python --help`

    usage: python3.9 [option] ... [-c cmd | -m mod | file | -] [arg] ...
    Options and arguments (and corresponding environment variables):
    -b     : issue warnings about str(bytes_instance), str(bytearray_instance)
             and comparing bytes/bytearray with str. (-bb: issue errors)
    -B     : don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
    -c cmd : program passed in as string (terminates option list)
    -d     : turn on parser debugging output (for experts only, only works on
             debug builds); also PYTHONDEBUG=x
    -E     : ignore PYTHON* environment variables (such as PYTHONPATH)
    -h     : print this help message and exit (also --help)
    -i     : inspect interactively after running script; forces a prompt even
             if stdin does not appear to be a terminal; also PYTHONINSPECT=x
    -I     : isolate Python from the user's environment (implies -E and -s)
    -m mod : run library module as a script (terminates option list)
    -O     : remove assert and __debug__-dependent statements; add .opt-1 before
             .pyc extension; also PYTHONOPTIMIZE=x
    -OO    : do -O changes and also discard docstrings; add .opt-2 before
             .pyc extension
    -q     : don't print version and copyright messages on interactive startup
    -s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
    -S     : don't imply 'import site' on initialization
    -u     : force the stdout and stderr streams to be unbuffered;
             this option has no effect on stdin; also PYTHONUNBUFFERED=x
    -v     : verbose (trace import statements); also PYTHONVERBOSE=x
             can be supplied multiple times to increase verbosity
    -V     : print the Python version number and exit (also --version)
             when given twice, print more information about the build
    -W arg : warning control; arg is action:message:category:module:lineno
             also PYTHONWARNINGS=arg
    -x     : skip first line of source, allowing use of non-Unix forms of #!cmd
    -X opt : set implementation-specific option. The following options are available:

             -X faulthandler: enable faulthandler
             -X oldparser: enable the traditional LL(1) parser; also PYTHONOLDPARSER
             -X showrefcount: output the total reference count and number of used
                 memory blocks when the program finishes or after each statement in the
                 interactive interpreter. This only works on debug builds
             -X tracemalloc: start tracing Python memory allocations using the
                 tracemalloc module. By default, only the most recent frame is stored in a
                 traceback of a trace. Use -X tracemalloc=NFRAME to start tracing with a
                 traceback limit of NFRAME frames
             -X importtime: show how long each import takes. It shows module name,
                 cumulative time (including nested imports) and self time (excluding
                 nested imports). Note that its output may be broken in multi-threaded
                 application. Typical usage is python3 -X importtime -c 'import asyncio'
             -X dev: enable CPython's "development mode", introducing additional runtime
                 checks which are too expensive to be enabled by default. Effect of the
                 developer mode:
                    * Add default warning filter, as -W default
                    * Install debug hooks on memory allocators: see the PyMem_SetupDebugHooks() C function
                    * Enable the faulthandler module to dump the Python traceback on a crash
                    * Enable asyncio debug mode
                    * Set the dev_mode attribute of sys.flags to True
                    * io.IOBase destructor logs close() exceptions
             -X utf8: enable UTF-8 mode for operating system interfaces, overriding the default
                 locale-aware mode. -X utf8=0 explicitly disables UTF-8 mode (even when it would
                 otherwise activate automatically)
             -X pycache_prefix=PATH: enable writing .pyc files to a parallel tree rooted at the
                 given directory instead of to the code tree

    --check-hash-based-pycs always|default|never:
        control how Python invalidates hash-based .pyc files
    file   : program read from script file
    -      : program read from stdin (default; interactive mode if a tty)
    arg ...: arguments passed to program in sys.argv[1:]

    Other environment variables:
    PYTHONSTARTUP: file executed on interactive startup (no default)
    PYTHONPATH   : ':'-separated list of directories prefixed to the
                   default module search path.  The result is sys.path.
    PYTHONHOME   : alternate  directory (or :<exec_prefix>).
                   The default module search path uses /lib/pythonX.X.
    PYTHONPLATLIBDIR : override sys.platlibdir.
    PYTHONCASEOK : ignore case in 'import' statements (Windows).
    PYTHONUTF8: if set to 1, enable the UTF-8 mode.
    PYTHONIOENCODING: Encoding[:errors] used for stdin/stdout/stderr.
    PYTHONFAULTHANDLER: dump the Python traceback on fatal errors.
    PYTHONHASHSEED: if this variable is set to 'random', a random value is used
       to seed the hashes of str and bytes objects.  It can also be set to an
       integer in the range [0,4294967295] to get hash values with a
       predictable seed.
    PYTHONMALLOC: set the Python memory allocators and/or install debug hooks
       on Python memory allocators. Use PYTHONMALLOC=debug to install debug
       hooks.
    PYTHONCOERCECLOCALE: if this variable is set to 0, it disables the locale
       coercion behavior. Use PYTHONCOERCECLOCALE=warn to request display of
       locale coercion and locale compatibility warnings on stderr.
    PYTHONBREAKPOINT: if this variable is set to 0, it disables the default
       debugger. It can be set to the callable of your debugger of choice.
    PYTHONDEVMODE: enable the development mode.
    PYTHONPYCACHEPREFIX: root directory for bytecode cache (pyc) files.

A specific version of the Python interpreter can be invoked from the command-line directly by running:

`user `[`$`]`python3.9`

Python can be used to write scripts, with the appropriate [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix) "wikipedia:Shebang (Unix)"). To execute a script with Python 3.10, for example, use the following header:

[FILE] **`testscript.py`**

    #!/usr/bin/env python3.10
    ...

## [See also]

-   [Pip](https://wiki.gentoo.org/wiki/Pip "Pip") --- [Python]\'s package management system. It references packages available in the official **Py**thon **P**ackage **I**ndex (PyPI).
-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [FreeBASIC](https://wiki.gentoo.org/wiki/FreeBASIC "FreeBASIC") --- a modern, self-hosting, object oriented, [BASIC](https://wiki.gentoo.org/wiki/BASIC "BASIC") compiler that is optionally backwards compatible with [QuickBASIC](https://en.wikipedia.org/wiki/QuickBASIC "wikipedia:QuickBASIC")
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.
-   [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby") --- an interpreted programming language.
-   [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") --- a high-level, general-purpose, and gradually typed programming language with low boilerplate objects, optionally immutable data structures, and an advanced macro system.

## [External resources]

-   [Gentoo Python Guide](https://projects.gentoo.org/python/guide/), complete documentation for the Python ecosystem in Gentoo.
-   [News item - Python 3.7 to become the default target](https://gentoo.org/support/news-items/2020-04-22-python3-7.html)
-   [Python preference to follow PYTHON_TARGETS](https://www.gentoo.org/support/news-items/2021-01-30-python-preference-to-follow-python-targets.html)
-   [Status of Python versions](https://devguide.python.org/versions/) to see what versions are supported or end-of-life for keeping `PYTHON_TARGETS` up to date.