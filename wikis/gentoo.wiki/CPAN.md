[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=CPAN&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Perl "Project:Perl")][Project](https://wiki.gentoo.org/wiki/Project:Perl "Project:Perl")

[[]][Home](https://www.cpan.org/)

[[]][Official documentation](https://www.cpan.org/modules/INSTALL.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/CPAN "wikipedia:CPAN")

[[]][[#perl](ircs://irc.libera.chat/#perl)] ([[webchat](https://web.libera.chat/#perl)])

**CPAN** is the *Comprehensive Perl Archive Network*, [Perl](https://wiki.gentoo.org/wiki/Perl "Perl")\'s package ecosystem. The original client for the CPAN network was also called [cpan], though its use is now relatively uncommon in favor of more modern clients.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Caveats]](#Caveats)
    -   [[4.1] [Lack of TLS Support]](#Lack_of_TLS_Support)
-   [[5] [Converting CPAN Version Numbers to Gentoo Package Versions]](#Converting_CPAN_Version_Numbers_to_Gentoo_Package_Versions)
-   [[6] [Tips]](#Tips)
-   [[7] [Troubleshooting]](#Troubleshooting)
    -   [[7.1] [Access to the CPAN package network is blocked by a corporate firewall]](#Access_to_the_CPAN_package_network_is_blocked_by_a_corporate_firewall)
-   [[8] [See also]](#See_also)

## [Installation]

The [[[perl-core/CPAN]](https://packages.gentoo.org/packages/perl-core/CPAN)[]] package is installed by default as [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") is a system package.

## [Configuration]

For most operations there is little to no configuration required to get [cpan] to work correctly. If [cpan] fails to fetch packages from CPAN as expected, see the troubleshooting section.

### [Environment variables]

-   `NONINTERACTIVE_TESTING` --- Skip all package prompts.
-   `PERL_MM_USE_DEFAULT` --- Assume the default response for all prompts.
-   `CPAN_OPTS` --- A string of default options to be passed to [cpan] at runtime.
-   `CPANSCRIPT_LOGLEVEL` --- for use with the system logger.
-   `GIT_COMMAND` --- the path to the [git] binary. By default this value is [/usr/local/bin/git].

## [Usage]

For most cases the cpan module is invoked as: [cpan \]

### [Invocation]

`user `[`$`]`cpan -h`

    NAME
        cpan - easily interact with CPAN from the command line

    SYNOPSIS
                # with arguments and no switches, installs specified modules
                cpan module_name [ module_name ... ]

                # with switches, installs modules with extra behavior
                cpan [-cfFimtTw] module_name [ module_name ... ]

                # use local::lib
                cpan -I module_name [ module_name ... ]

                # one time mirror override for faster mirrors
                cpan -p ...

                # with just the dot, install from the distribution in the
                # current directory
                cpan .

                # without arguments, starts CPAN.pm shell
                cpan

                # without arguments, but some switches
                cpan [-ahpruvACDLOPX]

    DESCRIPTION
        This script provides a command interface (not a shell) to CPAN. At the
        moment it uses CPAN.pm to do the work, but it is not a one-shot command
        runner for CPAN.pm.

      Options
        -a  Creates a CPAN.pm autobundle with CPAN::Shell->autobundle.

        -A module [ module ... ]
            Shows the primary maintainers for the specified modules.

        -c module
            Runs a `make clean` in the specified module's directories.

        -C module [ module ... ]
            Show the Changes files for the specified modules

        -D module [ module ... ]
            Show the module details. This prints one line for each out-of-date
            module (meaning, modules locally installed but have newer versions
            on CPAN). Each line has three columns: module name, local version,
            and CPAN version.

        -f  Force the specified action, when it normally would have failed. Use
            this to install a module even if its tests fail. When you use this
            option, -i is not optional for installing a module when you need to
            force it:

                    % cpan -f -i Module::Foo

        -F  Turn off CPAN.pm's attempts to lock anything. You should be careful
            with this since you might end up with multiple scripts trying to
            muck in the same directory. This isn't so much of a concern if
            you're loading a special config with "-j", and that config sets up
            its own work directories.

        -g module [ module ... ]
            Downloads to the current directory the latest distribution of the
            module.

        -G module [ module ... ]
            UNIMPLEMENTED

            Download to the current directory the latest distribution of the
            modules, unpack each distribution, and create a git repository for
            each distribution.

            If you want this feature, check out Yanick Champoux's
            "Git::CPAN::Patch" distribution.

        -h  Print a help message and exit. When you specify "-h", it ignores all
            of the other options and arguments.

        -i module [ module ... ]
            Install the specified modules. With no other switches, this switch
            is implied.

        -I  Load "local::lib" (think like "-I" for loading lib paths). Too bad
            "-l" was already taken.

        -j Config.pm
            Load the file that has the CPAN configuration data. This should have
            the same format as the standard CPAN/Config.pm file, which defines
            $CPAN::Config as an anonymous hash.

        -J  Dump the configuration in the same format that CPAN.pm uses. This is
            useful for checking the configuration as well as using the dump as a
            starting point for a new, custom configuration.

        -l  List all installed modules with their versions

        -L author [ author ... ]
            List the modules by the specified authors.

        -m  Make the specified modules.

        -M mirror1,mirror2,...
            A comma-separated list of mirrors to use for just this run. The "-P"
            option can find them for you automatically.

        -n  Do a dry run, but don't actually install anything. (unimplemented)

        -O  Show the out-of-date modules.

        -p  Ping the configured mirrors and print a report

        -P  Find the best mirrors you could be using and use them for the
            current session.

        -r  Recompiles dynamically loaded modules with CPAN::Shell->recompile.

        -s  Drop in the CPAN.pm shell. This command does this automatically if
            you don't specify any arguments.

        -t module [ module ... ]
            Run a `make test` on the specified modules.

        -T  Do not test modules. Simply install them.

        -u  Upgrade all installed modules. Blindly doing this can really break
            things, so keep a backup.

        -v  Print the script version and CPAN.pm version then exit.

        -V  Print detailed information about the cpan client.

        -w  UNIMPLEMENTED

            Turn on cpan warnings. This checks various things, like directory
            permissions, and tells you about problems you might have.

        -x module [ module ... ]
            Find close matches to the named modules that you think you might
            have mistyped. This requires the optional installation of
            Text::Levenshtein or Text::Levenshtein::Damerau.

        -X  Dump all the namespaces to standard output.

      Examples
                # print a help message
                cpan -h

                # print the version numbers
                cpan -v

                # create an autobundle
                cpan -a

                # recompile modules
                cpan -r

                # upgrade all installed modules
                cpan -u

                # install modules ( sole -i is optional )
                cpan -i Netscape::Booksmarks Business::ISBN

                # force install modules ( must use -i )
                cpan -fi CGI::Minimal URI

                # install modules but without testing them
                cpan -Ti CGI::Minimal URI

      Environment variables
        There are several components in CPAN.pm that use environment variables.
        The build tools, ExtUtils::MakeMaker and Module::Build use some, while
        others matter to the levels above them. Some of these are specified by
        the Perl Toolchain Gang:

        Lancaster Consensus:
        <https://github.com/Perl-Toolchain-Gang/toolchain-site/blob/master/lanca
        ster-consensus.md>

        Oslo Consensus:
        <https://github.com/Perl-Toolchain-Gang/toolchain-site/blob/master/oslo-
        consensus.md>

        NONINTERACTIVE_TESTING
            Assume no one is paying attention and skips prompts for
            distributions that do that correctly. cpan(1) sets this to 1 unless
            it already has a value (even if that value is false).

        PERL_MM_USE_DEFAULT
            Use the default answer for a prompted questions. cpan(1) sets this
            to 1 unless it already has a value (even if that value is false).

        CPAN_OPTS
            As with "PERL5OPT", a string of additional cpan(1) options to add to
            those you specify on the command line.

        CPANSCRIPT_LOGLEVEL
            The log level to use, with either the embedded, minimal logger or
            Log::Log4perl if it is installed. Possible values are the same as
            the "Log::Log4perl" levels: "TRACE", "DEBUG", "INFO", "WARN",
            "ERROR", and "FATAL". The default is "INFO".

        GIT_COMMAND
            The path to the "git" binary to use for the Git features. The
            default is "/usr/local/bin/git".

    EXIT VALUES
        The script exits with zero if it thinks that everything worked, or a
        positive number if it thinks that something failed. Note, however, that
        in some cases it has to divine a failure by the output of things it does
        not control. For now, the exit codes are vague:

                1       An unknown error

                2       The was an external problem

                4       There was an internal problem with the script

                8       A module failed to install

    TO DO
        * one shot configuration values from the command line

    BUGS
        * none noted

    SEE ALSO
        Most behaviour, including environment variables and configuration, comes
        directly from CPAN.pm.

    SOURCE AVAILABILITY
        This code is in Github in the CPAN.pm repository:

                https://github.com/andk/cpanpm

        The source used to be tracked separately in another GitHub repo, but the
        canonical source is now in the above repo.

    CREDITS
        Japheth Cleaver added the bits to allow a forced install (-f).

        Jim Brandt suggest and provided the initial implementation for the
        up-to-date and Changes features.

        Adam Kennedy pointed out that exit() causes problems on Windows where
        this script ends up with a .bat extension

    AUTHOR
        brian d foy, "<bdfoy@cpan.org>"

    COPYRIGHT
        Copyright (c) 2001-2015, brian d foy, All Rights Reserved.

        You may redistribute this under the same terms as Perl itself.

## [Caveats]

### [Lack of TLS Support]

The original CPAN client [cpan] is limited to `http` and `ftp` only. For most users this fact will not impact functionality. See the Troubleshooting section if this causes issues.

## [Converting CPAN Version Numbers to Gentoo Package Versions]

Perl has several primary formats of versions, the most notable one being \"float\" style versions, in the form \"x.yyyyyyyyyyy\" where the number of \"y\"\'s are arbitrary, and are interpreted as a floating point value.

That is, 1.001 is NOT the same as 1.01 and 1.1

However, Gentoo\'s version scheme sees 1.001 similar to 1.001.000 which is similar to 1.1.0 and thus, similar to 1.1.

Obviously this will not do, because when somebody says they need \"\>=1.05 (g:1.5)\" expecting \"1.06 (g:1.6)\", but instead get \"1.009 (g:1.9)\", things will break.

Hence, detection of these cases and normalizing them is essential:

     1.001 -> 1.1.0
     1.01  -> 1.10.0
     1.1   -> 1.100.0
     1.05  -> 1.50.0
     1.06  -> 1.60.0
     1.009 -> 1.9.0

     1.9.0 < 1.50.0 < 1.60.0

The simplest use of this library is with the tool, `gentoo-perlmod-version.pl`.

You can install this with: `emerge --ask dev-perl/Gentoo-PerlMod-Version`

Now you can use the tool to convert version numbers from CPAN to their Gentoo equivalents:

    $ /usr/bin/gentoo-perlmod-version.pl 0.10
    0.10 => 0.100.0

## [Tips]

## [Troubleshooting]

### [Access to the CPAN package network is blocked by a corporate firewall]

Modern corporate environments now routinely block unencrypted traffic. Unfortunately the original CPAN Network client [cpan] lacks support for TLS, all traffic is `http` and `ftp` only.

The solution is to use a more modern CPAN Network client such as [[[dev-perl/App-cpanminus]](https://packages.gentoo.org/packages/dev-perl/App-cpanminus)[]]. This CPAN client fully supports accessing the CPAN network over `https`.

## [See also]

-   [Application level package management](https://wiki.gentoo.org/wiki/Application_level_package_management "Application level package management") --- provides best practice recommendations on managing the coexistence of operating system and **application level package managers** on Gentoo.
-   [Gem](https://wiki.gentoo.org/wiki/Gem "Gem") --- programs and libraries for the [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby") programming language.
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.
-   [Pip](https://wiki.gentoo.org/wiki/Pip "Pip") --- [Python](https://wiki.gentoo.org/wiki/Python "Python")\'s package management system. It references packages available in the official **Py**thon **P**ackage **I**ndex (PyPI).
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.