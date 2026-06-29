# Perl

From Wikipedia:
:Perl is a high-level, general-purpose, interpreted, dynamic programming language.
:Perl borrows features from other programming languages including C, sh, AWK, and sed. It provides text processing facilities without the arbitrary data-length limits of many contemporary Unix command line tools.
:Perl gained widespread popularity in the mid-1990s as a CGI scripting language, in part due to its powerful regular expression and string parsing abilities.

## Installation
Install the  package.

## Commands
The Perl language interpreter:

 $ perl

Perl bug reporting:

 $ perlbug

Lookup the Perl documentation in POD format:

 $ perldoc

Send the Perl authors and maintainers a thank you message:

 $ perlthanks

## Package management
The Comprehensive Perl Archive Network (CPAN) is a repository of over 250,000 software modules and accompanying documentation written in the Perl programming language by over 12,000 contributors.

CPAN is also the name of a Perl module, , which is used to download and install Perl software from the CPAN archive.

## pacman and AUR
A number of popular CPAN modules are available as packages in the Arch repositories. There are further modules available in the AUR.

## CPAN.pm
The  module is included with Perl. It can be used interactively from the shell or in Perl scripts.

## Configuring cpan
Before first use, the module needs to be configured. This is done interactively from the shell with (some output omitted):

Automated configuration will suit most users. Answering yes, the configuration will continue with:

If you want  to install modules in your home directory choose . To install them system-wide choose . Choosing  the configuration ends:

Choosing the  option will result in addition modules being installed.

Choosing not to use automated configuration allows the user to set  options interactively in the shell. The table below shows some option names with a brief description and default value. More detailed information is displayed for each option during configuration.

{| class="wikitable"
! Name !! Description !! Default
|-
| cpan_home || CPAN build and cache directory || $HOME/.cpan
|-
| keep_source_where || Download target directory || $HOME/.cpan/sources
|-
| build_dir || Build process directory || $HOME/.cpan/build
|-
| prefs_dir || Customizable modules options directory || $HOME/.cpan/prefs
|-
| build_cache || Cache size for build directory || 100MB
|-
| cleanup_after_install || Remove build directory after successful install || No
|-
| shell || Preferred shell || /bin/bash
|-
| halt_on_failure || Halt on failure || No
|-
| colorize_output || Turn on colored output || No
|-
| histfile || History file location || $HOME/.cpan/histfile
|-
| histsize || History file size || 100 lines
|}

The configuration file  can be edited with your text editor of choice.

## Usage examples
To simply install a modules pass them as parameters to  (multiple module names are separated by spaces):

 $ cpan Acme::MetaSyntactic

The following examples are all in the  interactive shell, started with:

 $ cpan

Display information on a module:

View module :

Install a module:

 cpaninstall Acme::MetaSyntactic

Re-run cpan configuration:

 cpan[1> o conf init

## Widget bindings
The following widget toolkit bindings are available:

*
*
*
*
*

To use these with Perl, you may need to install the associated widget kits.

## IDE support
## Development in JetBrains IDE
If you are using a JetBrains IDE, for example IntelliJ Idea, install . Then install Perl plugin. Then go to the Settings > Languages & Frameworks > Perl5. In the Perl 5 Interpreter field select Add System Perl. Now you can make a run/debug configuration for your project and start debugging.

## Tips and tricks
## Perl development environment
 and  automate the installation and management of multiple perl versions under your home directory, allowing you to install modules locally without conflicting with the system perl.

## Improved module management
## cpanminus
cpanminus extends module management, aims to be zero configuration, and integrates with .

Install the  package.

See the cpanminus documentation for examples.

## ucpan
ucpan is an updater for CPAN modules (especially installed in local-lib). To install, run:

 $ cpan App::ucpan

## Bundle::CPAN
Installing the Bundle::CPAN distribution will add a lot of nice functionality to .

 $ cpan Bundle::CPAN

## Perl
* The Perl Programming Language (Perl homepage)
* Wikipedia:Perl
*
*

## CPAN
* Comprehensive Perl Archive Network
* wikipedia:CPAN
* CPAN / CPAN Shell / CPANPLUS Quick Reference Guide
* List of recommended Perl modules

## Tutorials
* Perl Tutorials
* Tutorials at perldoc
* cpan configuration
* PerlMonks Tutorials
