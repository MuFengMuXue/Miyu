[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Raku&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://raku.org/)

[[]][Official documentation](https://docs.raku.org/)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/rakudo)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Raku_(programming_language) "wikipedia:Raku (programming language)")

[[]][GitHub](https://github.com/rakudo/rakudo)

[[]][Bugs (upstream)](https://github.com/rakudo/rakudo/issues)

[[]][[#raku](ircs://irc.libera.chat/#raku)] ([[webchat](https://web.libera.chat/#raku)])

[[]][[#raku-beginner](ircs://irc.libera.chat/#raku-beginner)] ([[webchat](https://web.libera.chat/#raku-beginner)])

[[]][r/Raku](https://reddit.com/r/Raku)

[[]][Blog](https://planet.raku.org/)

**Raku** is a high-level, general-purpose, and gradually typed programming language with low boilerplate objects, optionally immutable data structures, and an advanced macro system. Raku is not tied to a specific programming paradigm: it supports procedural, object oriented, and functional programming in equal measure.

The reference implementation of the Raku programming language has several major components:

-   The [Rakudo](https://wiki.gentoo.org/wiki/Rakudo "Rakudo") reference compiler [[[dev-lang/rakudo]](https://packages.gentoo.org/packages/dev-lang/rakudo)[]].
-   The [NQP](https://wiki.gentoo.org/wiki/NQP "NQP") compiler toolchain [[[dev-lang/nqp]](https://packages.gentoo.org/packages/dev-lang/nqp)[]].
-   [MoarVM](https://wiki.gentoo.org/wiki/MoarVM "MoarVM") Raku\'s native virtual machine [[[dev-lang/moarvm]](https://packages.gentoo.org/packages/dev-lang/moarvm)[]].
-   [zef](https://wiki.gentoo.org/index.php?title=Zef&action=edit&redlink=1 "Zef (page does not exist)") a module manager for interacting with Raku\'s ecosystem. ([ebuild requested](https://bugs.gentoo.org/827802).)
-   [Rakudo Star](https://wiki.gentoo.org/index.php?title=Rakudo_Star&action=edit&redlink=1 "Rakudo Star (page does not exist)") the Rakudo compiler and a collection of [modules](https://github.com/rakudo/star/blob/master/etc/modules.txt) from the Raku ecosystem ([ebuild requested](https://bugs.gentoo.org/834943).)

** Note**\
In the absence of a Rakudo-Star Gentoo ebuild, it\'s possible to bootstrap Rakudo Star via [Rakubrew](https://rakubrew.org/). See the Troubleshooting section of this article for details. Additionally, it\'s possible to use the official [docker](https://wiki.gentoo.org/wiki/Docker "Docker") container [rakudo-star](https://hub.docker.com/_/rakudo-star) provided by the upstream project.

Raku was created as both a specification and a test suite. Any implementation that passes the test suite [Raku/roast](https://github.com/Raku/roast) is considered to be Raku. Thus, while MoarVM is Raku\'s default virtual machine it\'s not the only virtual machine that Raku supports. Currently, Raku can be run from within the [Java](https://wiki.gentoo.org/wiki/Java "Java") and [JavaScript](https://wiki.gentoo.org/index.php?title=JavaScript&action=edit&redlink=1 "JavaScript (page does not exist)") virtual machines and more virtual machine targets are expected to follow.

## Contents

-   [[1] [Raku in Context]](#Raku_in_Context)
    -   [[1.1] [Market Niche]](#Market_Niche)
    -   [[1.2] [Pros]](#Pros)
    -   [[1.3] [Cons]](#Cons)
    -   [[1.4] [Complimentary Languages]](#Complimentary_Languages)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
    -   [[2.2] [USE flags]](#USE_flags)
    -   [[2.3] [Environment variables]](#Environment_variables)
    -   [[2.4] [Files]](#Files)
-   [[3] [Removal]](#Removal)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Invocation]](#Invocation)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [How do I get the Star Bundle?]](#How_do_I_get_the_Star_Bundle.3F)
    -   [[5.2] [How do I upgrade MoarVM and the Rakudo Star Bundle?]](#How_do_I_upgrade_MoarVM_and_the_Rakudo_Star_Bundle.3F)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
    -   [[7.1] [Learning Raku]](#Learning_Raku)
    -   [[7.2] [Popular Raku Libraries and Frameworks]](#Popular_Raku_Libraries_and_Frameworks)
    -   [[7.3] [Raku\'s Inner Workings]](#Raku.27s_Inner_Workings)

## [Raku in Context]

### [Market Niche]

To some, Raku is primarily a postmodern glue language. To others, it\'s thought of as the \"Swiss Army lightsaber\" owing to its usefulness in situations that require quick hacks, while still maintaining a certain elegance. In practice, it is often used as a shell-like scripting language with objects and robust math support. While not yet a popular choice, Raku\'s concurrency model is helping it slowly carve out a niche in the DevOps space.

### [Pros]

-   Raku is **Multi-paradigm** procedural, object oriented, and functional programming styles are supported.
-   Raku **Grammars** combine named regexes with recursion, human readable rules, and grapheme-level Unicode support to enable advanced text processing capabilities far beyond that of Perl compatible regular expressions.
-   Raku has a **concurrency** and **async** model that ensure that non-linear code is easy to read and maintain.
-   Raku natively supports **rational numbers** which permits direct comparison without concern for any accumulated rounding errors that would occur in other programming languages.
-   **Lazy evaluation** which enables features such as infinite sets.
-   **Low boilerplate** object oriented programming.
-   Raku\'s community has a reputation for being extremely welcoming of beginners.

### [Cons]

-   Raku\'s heavy use of symbolic operators and optional use of non-ASCII characters can confuse novice Raku programmers.
-   In its current iteration, Raku\'s execution speed is slower than [Python](https://wiki.gentoo.org/wiki/Python "Python") for most operations.
-   Initial VM startup is also sluggish, roughly comparable to [Java](https://wiki.gentoo.org/wiki/Java "Java")\'s virtual machine startup time.
-   Raku\'s regular expression syntax is very different from PCRE. This takes some getting used to.
-   Raku\'s Fez package ecosystem is smaller than Python\'s Pip and Perl\'s CPAN making finding an existing module to perform a task a hit-or-miss proposition.

### [Complimentary Languages]

Raku is closely related to [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") and the two languages do share some syntax. Many Perl programmers are at least passingly familiar with Raku. Interestingly, some [Haskell](https://wiki.gentoo.org/wiki/Haskell "Haskell") programmers have taken a liking to Raku as it\'s optionally highly functional. Some [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") programmers have also been known to use Raku for compile-time utility scripts.

## [Installation]

Raku uses the reference compiler Rakudo:

### [Emerge]

`root `[`#`]`emerge --ask dev-lang/rakudo`

### [USE flags]

### [USE flags for] [dev-lang/rakudo](https://packages.gentoo.org/packages/dev-lang/rakudo) [[]] [A compiler for the Raku programming language]

  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+moar`](https://packages.gentoo.org/useflags/+moar)   Use the MoarVM as backend
  [`clang`](https://packages.gentoo.org/useflags/clang)   Use Clang to compile the MoarVM backend
  [`java`](https://packages.gentoo.org/useflags/java)     Add support for Java
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-09 10:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Environment variables]

-   `RAKULIB` --- Modify the module search path.
-   `PERL6LIB` --- Modify the module search path ([DEPRECATED](https://docs.raku.org/programs/03-environment-variables.html#Module_loading)).
-   `RAKUDO_HOME` --- Override the path of the Rakudo runtime files.
-   `NQP_HOME` --- Override the path of the NQP runtime files.

### [Files]

-   [\~/.raku/] --- This directory is where Raku keeps the [rakudo-history] file and some other odds and ends.

## [Removal]

`root `[`#`]`emerge --ask --depclean --verbose dev-lang/rakudo`

## [Usage]

### [Invocation]

`user `[`$`]`rakudo --help`

    perl6.moarvm [switches] [--] [programfile] [arguments]
    With no arguments, enters a REPL (see --repl-mode option).
    With a "[programfile]" or the "-e" option, compiles the given program
    and, by default, also executes the compiled code.

      -                    read program source from STDIN or start REPL if a TTY
      -c                   check syntax only (runs BEGIN and CHECK blocks)
      --rakudoc            extract documentation and print it as text
      --rakudoc=module     use RakuDoc::To::[module] to render inline documentation
      -e program           one line of program, strict is enabled by default
      -h, --help           display this help text
      -n                   run program once for each line of input
      -p                   same as -n, but also print $_ at the end of lines
      -I path              adds the path to the module search path
      -M module            loads the module prior to running the program
      --target=stage       specify compilation stage to emit
      --optimize=level     use the given level of optimization (0..3)
      --rakudo-home=path   Override the path of the Rakudo runtime files
      -o, --output=name    specify name of output file
      -v, --version        display version information
      -V                   print configuration summary
      --stagestats         display time spent in the compilation stages
      --ll-exception       display a low level backtrace on errors
      --doc                extract documentation and print it as text
      --doc=module         use Pod::To::[module] to render inline documentation
      --repl-mode=interactive|non-interactive
                           when running without "-e" or filename arguments,
                           a REPL is started. By default, if STDIN is a TTY,
                           "interactive" REPL is started that shows extra messages
                           and prompts, otherwise a "non-interactive" mode is used
                           where STDIN is read entirely and evaluated as if it were
                           a program, without any extra output (in fact, no REPL
                           machinery is even loaded). This option allows to bypass
                           TTY detection and force one of the REPL modes.
      --profile[=name]     write profile information to a file
                           Extension controls format:
                               .json outputs in JSON
                               .sql  outputs in SQL
                               any other extension outputs in HTML
      --profile-compile[=name]
                           write compile-time profile information to a file
                           Extension controls format:
                             .json outputs in JSON
                             .sql  outputs in SQL
                             any other extension outputs in HTML
      --profile-kind[=name]
                           choose the type of profile to generate
                             instrumented - performance measurements (default)
                             heap - record heap snapshots after every garbage
                             collector run
      --profile-filename=name
                           provide a different filename for profile.
                           Extension controls format:
                             .json outputs in JSON
                             .sql  outputs in SQL
                             any other extension outputs in HTML
                           This option will go away in a future Rakudo release
      --profile-stage=stage
                           write profile information for the given compilation
                           stage to a file. Use --profile-compile to set name
                           and format
      --full-cleanup       try to free all memory and exit cleanly
      --debug-port=port    listen for incoming debugger connections
      --debug-suspend      pause execution at the entry point
      --tracing            output a line to stderr on every interpreter instr
                           (only if enabled in MoarVM)

    Note that only boolean single-letter options may be bundled.

    The following environment variables are respected:

      RAKULIB     Modify the module search path
      PERL6LIB    Modify the module search path (DEPRECATED)
      RAKUDO_HOME Override the path of the Rakudo runtime files
      NQP_HOME    Override the path of the NQP runtime files

## [Troubleshooting]

### [][How do I get the Star Bundle?]

There isn\'t an official Gentoo ebuild of the star bundle just yet. A popular stop-gap approach is to use [Rakubrew](https://rakubrew.org/). There are a few ways to install and configure Rakubrew, but a common way is to leverage [CPAN](https://wiki.gentoo.org/wiki/CPAN "CPAN") to get the job done.

First, install a modern CPAN client, such as CPAN Minus:

`root `[`#`]`emerge --ask dev-perl/App-cpanminus`

Once this is done, install Rakubrew via CPAN:

`user `[`$`]`cpanm App::Rakubrew`

Rakubrew is now installed to [\$HOME/perl5/] but [\~/.bashrc] needs to be updated so that this is in the user\'s path:

[FILE] **`~/.bashrc`Adding Rakubrew to the User\'s Path**

    # Rakubrew
    if [ -d $HOME/perl5/lib/perl5 ]; then
        export PATH="$HOME/perl5/bin/:$PATH"
        PERL5LIB=$$HOME/perl5/lib/perl5
        MANPATH=$$HOME/perl5/man
        export MANPATH PERL5LIB
    fi
    eval "$($HOME/perl5/bin/rakubrew init Bash)"

Now the profile needs to be reloaded in order for these changes to take effect:

`user `[`$`]`source ~/.bashrc`

To build the most recent version of Raku, run the following:

`user `[`$`]`rakubrew build`

That done, the Raku package manger Zef still needs to be built:

`user `[`$`]`rakubrew build-zef`

Zef can now install all of Raku\'s Star Bundle modules with the following [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") script:

[FILE] **`zef-install-star.sh`Install Rakudo Star Modules via Zef**

    #!/usr/bin/env bash

    zef_force_flags="--force-resolve --force-fetch --force-extract --force-build --force-test --force-install"

    star_packages=( 'App::Prove6' 'Config' 'Config::Parser::json'
            'Config::Parser::toml' 'Config::Parser::yaml' 'Config::TOML'
            'Crane' 'DateTime::Format' 'DateTime::Parse' 'DBIish' 'Digest'
            'Digest::MD5' 'Encode' 'File::Directory::Tree' 'File::Find'
            'File::Temp' 'File::Which' 'Getopt::Long' 'Grammar::Debugger'
            'Grammar::Profiler::Simple' 'Hash::Merge' 'HTTP::Easy'
            'HTTP::Status' 'HTTP::UserAgent' 'IO::Capture::Simple'
            'IO::Glob' 'IO::Socket::SSL' 'IO::String' 'JSON::Class'
            'JSON::Fast' 'JSON::Marshal' 'JSON::Name' 'JSON::OptIn'
            'JSON::RPC' 'JSON::Tiny' 'JSON::Unmarshal' 'LibraryCheck'
            'LibraryMake' 'License::SPDX' 'Log' 'Log::Colored'
            'LWP::Simple' 'META6' 'MIME::Base64' 'NativeHelpers::Blob'
            'NativeLibs' 'OO::Monitors' 'OpenSSL' 'Path::Finder'
            'PathTools' 'Pod::Load' 'Pod::To::BigPage' 'Pod::To::HTML'
            'Pod::Usage' 'PSGI' 'Readline' 'Shell::Command' 'sigpipe'
            'SVG' 'SVG::Plot' 'TAP' 'Temp::Path' 'Template::Mojo'
            'Template::Mustache' 'Terminal::ANSIColor'
            'Terminal::ANSIParser' 'Terminal::LineEditor' 'Test::META'
            'Test::Mock' 'Test::Output' 'Test::Util::ServerPort'
            'Test::When' 'Testo' 'URI' 'XML::Writer' 'YAMLish')

    for module in "$"

    do
        zef install $zef_force_flags "$module"
    done

Done.

### [][How do I upgrade MoarVM and the Rakudo Star Bundle?]

Update App::Rakubrew to the current release:

`user `[`$`]`cpanm App::Rakubrew`

Build the latest version of MoarVM:

`user `[`$`]`rakubrew build moar-<NEW_VERSION>`

Once the build process is complete, switch to the new version of Raku:

`user `[`$`]`rakubrew switch moar-<NEW_VERSION>`

Confirm switching to the new version of MoarVM worked as expected:

`user `[`$`]`raku --version`

Install the most recent version of the Zef package manager

`user `[`$`]`rakubrew build-zef`

If you forget the above step, Zef will be missing!

Confirm switching to the new version of Zef worked as expected:

`user `[`$`]`zef --version`

Install the Rakudo Star modules via Zef:

Rerun the [zef-install-star.sh] module installation script. If you forget this step you will not have any of the modules from the Rakudo Star bundle.

Delete the old version of MoarVM, if desired:

`user `[`$`]`rakubrew nuke moar-<OLD_VERSION>`

Upgrade complete.

## [See also]

-   [MoarVM](https://wiki.gentoo.org/wiki/MoarVM "MoarVM") --- [Rakudo](https://wiki.gentoo.org/wiki/Rakudo "Rakudo") compiler\'s virtual machine for the [Raku] Programming Language.
-   [NQP](https://wiki.gentoo.org/wiki/NQP "NQP") --- a lightweight [Raku]-like environment for MoarVM, JVM, and other virtual machines.
-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.
-   [Java](https://wiki.gentoo.org/wiki/Java "Java") --- a programming language, originally developed by [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems "wikipedia:Sun Microsystems"), which uses a platform-independent virtual machine to execute Java bytecode in real-time.

## [External resources]

### [Learning Raku]

-   [Learn Raku in Y Minutes](https://learnxinyminutes.com/docs/raku/) a basic primer on Raku.
-   [Dr. Raku](https://www.youtube.com/@DrRaku-Programming/) a popular [YouTube](https://en.wikipedia.org/wiki/YouTube "wikipedia:YouTube") video series for Raku beginners.
-   [Raku Guide](https://raku.guide/) a high-level overview of the Raku programming language.
-   [A Complete Course of the Raku programming language](https://course.raku.org/) An in-depth five part Raku programming course.
-   [Raku Modules Directory](https://modules.raku.org/) detailing Raku\'s module ecosystem.
-   [Rosetta Code: Raku](https://rosettacode.org/wiki/Category:Raku) Raku specific implementations of common algorithms.
-   [Exercism\'s Raku track](https://exercism.org/tracks/raku/) free interactive online lessons for learning Raku.

### [Popular Raku Libraries and Frameworks]

-   [Sparrow](https://github.com/melezhik/Sparrow6) a versatile automation framework written in Raku.
-   [Cro](https://cro.services/) Cro is a set of libraries for building distributed systems written in Raku.
-   [Red](https://github.com/FCO/Red) an Object-Relational Mapping (ORM) database management tool for Raku.
-   [Raku Roast](https://github.com/Raku/roast) Raku\'s test suite. Any implementation of Raku that passes Roast is a valid implementation.

### [][Raku\'s Inner Workings]

-   [Raku\'s \"core\"](https://gist.github.com/raiph/849a4a9d8875542fb86df2b2eda89296) by [\@raiph](https://github.com/raiph).