# Perl package guidelines

This document covers the creation of PKGBUILDs for Perl modules distributed over CPAN, the Comprehensive Perl Authors Network. The target audience of this document is intended to be packagers of Perl modules. For Perl policies see Perl Policy.

## Arch Linux packaging conventions
The following conventions should be used to keep Perl module packages consistent. This section serves as an introduction to the concept of Perl packaging, from the point of view of Arch Linux; that is, package management and system administration. In an effort to please the casual TL;DR reader, the easiest and/or most popular material is at the top.

## Package names
For modules the package name should begin with  and the rest of the name should be constructed from the module name by converting it to lowercase and then replacing colons with hyphens. For example the package name corresponding to  will be . Perl applications should have the same name as that of the application but in lowercase.

## Package file placement
Perl packages should install module files into  (use  in scripts), or . This is done by setting the  command line parameter to  as shown below. No files should be stored in  as that directory is reserved for use by the system administrator to install Perl packages outside the package management system. When a user installs modules system-wide by using the cpan shell, modules end up in the site-perl sub-directories.

The files  and  also should not be present; this is taken care of by the example PKGBUILD described below.

## Architecture
In most cases, the  array should contain  because most Perl packages are architecture independent. XS modules are compiled into dynamically loaded libraries (.so files) and should explicitly set their architecture to  in order to indicate that they are architecture dependent when built. An XS module usually contains one or more .xs files which dynamically generate .c files.

## Automation
A plugin for the second-generation CPAN shell, CPANPLUS, is available in the  package. This plugin packages distributions on the fly as they are installed by CPANPLUS. Online documentation is available at https://metacpan.org/release/CPANPLUS-Dist-Arch

## PKGBUILD examples
An example PKGBUILD can be found at The following two PKGBUILD examples use techniques, introduced in this page, that are intended to make a PKGBUILD more resilient to more sophisticated problems. Because there are two styles of build scripts, there are two example PKGBUILDS. The first PKGBUILD is an example of how to package a distribution that uses . The second PKGBUILD can be used as a starting point for a distribution which uses .

{{hc|PKGBUILD|
# Maintainer: Your Name

_dist=Foo-Bar
pkgname=perl-foo-bar
pkgver=1.0
pkgrel=1
pkgdesc='This packages the Foo-Bar distribution, containing the Foo::Bar module!'
arch=('any')
url="https://metacpan.org/release/$_dist"
license=('Artistic-1.0-Perl OR GPL-1.0-or-later')
depends=('perl')
options=('!emptydirs')
source=("https://cpan.metacpan.org/authors/id/BAZ/$_dist-$pkgver.tar.gz")
sha256sums=(...)

build() {
    cd $_dist-$pkgver

    unset PERL_MM_OPT PERL5LIB PERL_LOCAL_LIB_ROOT
    export PERL_MM_USE_DEFAULT=1 PERL_AUTOINSTALL=--skipdeps

    /usr/bin/perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1
    make
}

check() {
    cd $_dist-$pkgver

    unset PERL5LIB PERL_LOCAL_LIB_ROOT

    make test
}

package() {
    cd $_dist-$pkgver

    unset PERL5LIB PERL_LOCAL_LIB_ROOT

    make install INSTALLDIRS=vendor DESTDIR="$pkgdir"
}
}}

{{hc|PKGBUILD|
# Maintainer: Your Name

_dist=Foo-Bar
pkgname=perl-foo-bar
pkgver=1.0
pkgrel=1
pkgdesc='This packages the Foo-Bar distribution, containing the Foo::Bar module!'
arch=('any')
url="https://metacpan.org/release/$_dist"
license=('Artistic-1.0-Perl OR GPL-1.0-or-later')
depends=('perl')
makedepends=('perl-module-build')
options=('!emptydirs')
source=("https://cpan.metacpan.org/authors/id/BAZ/$_dist-$pkgver.tar.gz")
sha256sums=(...)

build() {
    cd $_dist-$pkgver

    unset PERL_MB_OPT PERL5LIB PERL_LOCAL_LIB_ROOT
    export PERL_MM_USE_DEFAULT=1 MODULEBUILDRC=/dev/null

    /usr/bin/perl Build.PL --create_packlist=0
    ./Build
}

check() {
    cd $_dist-$pkgver

    unset PERL5LIB PERL_LOCAL_LIB_ROOT

    ./Build test
}

package() {
    cd $_dist-$pkgver

    unset PERL5LIB PERL_LOCAL_LIB_ROOT

    ./Build install --installdirs=vendor --destdir="$pkgdir"
}
}}

Justification for the added complexity of these PKGBUILDs is attempted in the latter sections.

## CPAN module mechanics
There are a number of carefully, and not so carefully, designed mechanics that work together to create the module system. When making use of the CPAN, procedures must be followed to fetch the source code of a module, build that fetched module, and insert it into the system software for later execution. In order to understand how modules should be packaged, it helps immensely if one understands how modules work without any involvement from pacman and Arch Linux packages. Our goal in the end is to try to be unobtrusive as possible, while improving organization and consistency in the end product.

## Modules
Modules are declared with the  keyword in Perl. Modules are contained inside a .pm ("dot-pee-em") file. Though it is possible more than one module () is in the file. Modules have namespaces separated with  (double colons), like: . When loading a module, the s are replaced with directory separators. For example:  will be loaded for the module .

Core modules are included with an installation of Perl. Some core modules are only available bundled with Perl. Other modules can still be downloaded and installed separately from CPAN.

## Distributions
(aka dist, package) This is the equivalent of an Arch Linux package in CPAN-lingo. Distributions are .tar.gz archives full of files. These archives contain primarily .pm module files, tests for the included modules, documentation for the modules, and whatever else is deemed necessary.

Usually a distribution contains a primary module with the same name. Sometimes this is not true, like with the Template-Toolkit distribution. The latest package, , for the  dist, contains no  module!

Sometimes because distributions are named after a main module, their names are used interchangeably and they get muddled together. However it is sometimes useful to consider them a separate entity (like in Template-Toolkit's case).

## CPAN
Each CPAN mirror contains indices that list the distributions on CPAN, the modules in the dists, and the name of the author who uploaded the dist. These are simply text files. The most useful index is in the  file available from each CPAN mirror. The term "packages" here refers to the  keyword in the Perl language itself, not something similar to pacman packages. The CPAN shell, referred to as lowercased, italicized cpan, is simply the venerable perl script which navigates indices to find the module you want to install.

Modules are found in the  list. On the same line as the module/package name is the path to the distribution tarball that contains the module. When you ask cpan to install a module, it will look up the module and install the relevant distribution. As the distribution is installing it will generate a list of module dependencies. Cpan will try to load each module dependency into the perl interpreter. If a module of the given version cannot be loaded the process is repeated.

The cpan shell does not have to worry about what version of the required module it is installing. cpan can rely on the fact that the latest version of the module must satisfy the requirements of the original module that it began installing in the first place. Only the latest versions of modules are listed in the packages details file. Unfortunately for the perl package author, we cannot always rely on the fact that our packages offer the most recent version of a Perl distribution and the modules contained within. Pacman dependency checking is much more static and strongly enforced.

## Module dependencies
Perl has a unique way of defining dependencies compared to similar systems like Python eggs and Ruby gems. Eggs define dependencies on other eggs. Gems depend on gems. Perl dists depend on modules. Modules are only available from CPAN distributions, so in a way Perl distributions depend on distributions only indirectly. Modules can define their own versions independent from distributions inside the module source code. This is done by defining a package variable called . When using  and , this is defined with the  keyword. For example:

Modules can change their versions however they like and even have a version distinct from the distribution version. The utility of this is questionable but it is important to keep in mind. Module versions are more difficult to determine from outside of the perl interpreter and require parsing the Perl code itself, and maybe even loading the module into Perl. The advantage is that from inside the perl interpreter, module versions are easy to determine. For example:

## Dependency definition
Where are dependencies defined in Perl distributions? They are "defined" inside of the  or  script. For example, inside of the  script the  function is called to generate the  like this:

{{bc|
use ExtUtils::MakeMaker;
WriteMakeFile(
    'NAME' => 'ArchLinux::Module',
    'VERSION' => '0.01',
    'PREREQ_PM' => { 'POSIX' => '0.01' },
);
}}

This is a contrived example but it is important to understand the dependencies are not final until after the  or  script is run. Dependencies are specified at runtime, which means they can be changed or modified using the full power of Perl. This means the module author can add, remove, or change versions of dependencies right before the distribution is installed. Some modules authors use this to do overly clever things like depend on modules only if they are installed. Some multi-platform dists also depend on system-specific modules when installed on different operating systems.

As an example, the CPANPLUS distribution looks for CPANPLUS::Dist plugins that are currently installed. If any plugins are installed for the currently installed version of CPANPLUS it adds them to the new CPANPLUS's prerequisites. I'm not quite sure why. Luckily for the Perl packager most dependencies are static like in the above example that requires the POSIX module with a minimum version of 0.01.

## Meta information
Meta files are included in recent distributions which contain meta-information about distributions such as the name, author, abstract description, and module requirements. Previously there were  files in the YAML format but more recently the switch has been made to  files in the JSON format. These files can
be edited by hand but more often they are generated automatically by  or  scripts when packaging a distribution for release. The latest specification is described in [https://search.cpan.org/perldoc?CPAN::Meta::Spec CPAN::Meta::Spec's online docs.

Remember that dependencies can be changed at runtime! For this reason another meta file is generated after running the build script. This second meta file is called  and reflects changes the script made at runtime and may be different from the meta file generated when the distribution was packaged for CPAN.

Elderly distributions on the CPAN have no meta file at all. These old releases predate the idea of the META.yml file and only describe their prerequisites in their .

## Installation modules
One of Perl's greatest strengths is the sheer number of modules available on CPAN. Not too surprisingly, there are also several different modules used for installing... well... modules! TMTOWTDI! I am not aware of a standard name for these types of modules, so I just called them "Installation Modules".

These modules are concerned with building the distribution and installing module files wherever the user prefers. This seems straightforward, but considering the number of different systems Perl runs on, this can get complex. Installation modules all place a Perl code file inside the dist tarball. Running this perl script will initiate the build and install process. The script always ends with the .PL suffix and is termed the "Build script" in the below list.

## ExtUtils::MakeMaker
;Build script:
;CPAN link: https://search.cpan.org/dist/ExtUtils-MakeMaker

The original, oldest module for installing modules is . The major downside to this module is that it requires the  program to build and install everything. This may not seem like a big deal to linux users but is a real hassle for Windows people!

## Module::Build
;Build script:
;CPAN link: https://search.cpan.org/dist/Module-Build

The main advantage of Module::Build is that it is pure-perl. This means it does not require a  program to be installed for you to build/install modules. Its adoption was rocky because if  was not already installed, you could not run the bundled  script! This is not a problem with recent versions of Perl because  is a core module. (NOTE As of Perl 5.22, Module::Build will no longer be a core module)

## Module::Build::Tiny
;Build script:
;CPAN link: https://search.cpan.org/dist/Module-Build-Tiny

This is another pure-perl build tool. As an interface it implements a subset of Module::Build's interface, in particular it requires dashes before its arguments (Module::Build accepts with and without) and does not support .

## Module::Install
;Build script:
;CPAN link: https://search.cpan.org/dist/Module-Install

Another modern build/installation module,  still requires the  program be installed to function.  was designed as a drop-in replacement for , to address some of 's shortcomings. Ironically, it depends on  in order to operate. The  files that are generated by  look much different and are implemented using a simple domain specific language.

One very interesting feature is that  bundles a complete copy of itself into the distribution file. Because of this, unlike  or , you do not need  to be installed on your system.

Another very unique feature is auto-install. Though not recommended by 's authors this feature is used quite often. When the module author enables auto-install for their distribution,  will search for and install any pre-requisite modules that are not installed when  is executed. This feature is skipped when  detects it is being run by  or . However, this feature is not skipped when run inside... oh I do not know... a PKGBUILD! I hope you can see how a rogue perl program downloading and installing modules willy-nilly inside a PKGBUILD can be a problem. See the #PERL_AUTOINSTALL environment variable to see how to fix this.

## Environment variables
A number of environment variables can affect the way the modules are built or installed. Some have a very dramatic effect and can cause problems if misunderstood. An advanced user could be using these environment variables. Some of these will break an unsuspecting PKGBUILD or cause unexpected behavior.

## PERL_MM_USE_DEFAULT
When this variable is set to a true value, the installation module will pretend the default answer was given to any question it would normally ask. This does not always work, but all of the installation modules honour it. That does not mean the module author will!

## PERL_AUTOINSTALL
You can pass additional command-line arguments to 's  with this variable. In order to turn off auto-install (highly recommended), assign  to this.

## PERL_MM_OPT
You can pass additional command-line arguments to  with this variable. For example, you can install modules into your home-dir by using:

## PERL_MB_OPT
This is the same thing as  except it is only for . For example, you could install modules into your home-dir by using:

## MODULEBUILDRC
 allows you to override its command-line-arguments with an rcfile. This defaults to . This is considered deprecated within the Perl toolchain. You can override which file it uses by setting the path to the rcfile in . The paranoid might set  to ... just in case.

## PERL5LIB
The directories searched for libraries can be set by the user (particularly if they are using ) by setting . That should be cleared before building.

## PERL_LOCAL_LIB_ROOT
If the user is using  it will set . That should be cleared before building.

## Problems with user-installed perl
A subtle problem is that advanced Perl programmers may like to have multiple versions of perl installed. This is useful for testing backwards-compatibility in created programs. There are also speed benefits to compiling your own custom perl interpreter (i.e. without threads). Another reason for a custom perl is simply because the official perl Arch Linux package sometimes lags behind Perl releases. The user may be trying out the latest perl... who knows?

If the user has the custom perl executable in their , the custom perl will be run when the user types the perl command on the shell. In fact the custom perl will run inside the  as well! This can lead to insidious problems that are difficult to understand.

The problem lies in compiled XS modules. These modules bridge Perl and C. As such they must use Perl's internal C API to accomplish this bridge. Perl's C API changes slightly with different versions of Perl. If the user has a different version of Perl than the system perl () then any XS module compiled with the user's perl will be incompatible with the system-wide perl. When trying to use the compiled XS module with the system perl, the module will fail to load with a link error.

A simple solution is to always use the absolute path of the system-wide perl interpreter () when running perl in the .
