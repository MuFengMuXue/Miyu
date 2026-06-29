*Not to be confused with [Raku, formerly Perl 6](https://wiki.gentoo.org/wiki/Raku "Raku").*

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Perl "Project:Perl")][Project](https://wiki.gentoo.org/wiki/Project:Perl "Project:Perl")

[[]][Home](https://www.perl.org/)

[[]][Official documentation](https://perldoc.perl.org/)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/perl)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Perl "wikipedia:Perl")

[[]][GitHub](https://github.com/Perl/perl5)

[[]][[#perl](ircs://irc.libera.chat/#perl)] ([[webchat](https://web.libera.chat/#perl)])

[[]][[comp.lang.perl.misc](news:comp.lang.perl.misc) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.lang.perl.misc))]

[[]][r/perl](https://reddit.com/r/perl)

** Warning**\
For nontrivial changes to this page, please ask / propose the changes on the talk page first! [Dilfridge](https://wiki.gentoo.org/wiki/User:Dilfridge "User:Dilfridge") ([talk](https://wiki.gentoo.org/wiki/User_talk:Dilfridge "User talk:Dilfridge")) 14:18, 18 April 2017 (UTC)

**Perl** is a general purpose interpreted programming language with a powerful regular expression engine.

## Contents

-   [[1] [Perl in Context]](#Perl_in_Context)
    -   [[1.1] [Market Niche]](#Market_Niche)
    -   [[1.2] [Pros]](#Pros)
    -   [[1.3] [Cons]](#Cons)
    -   [[1.4] [Complimentary Languages]](#Complimentary_Languages)
-   [[2] [Introduction]](#Introduction)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [USE flags]](#USE_flags)
        -   [[3.1.1] [Global]](#Global)
        -   [[3.1.2] [Package]](#Package)
-   [[4] [Upgrading]](#Upgrading)
    -   [[4.1] [The official way]](#The_official_way)
    -   [[4.2] [Some knowledge]](#Some_knowledge)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [How do I list all Perl modules installed from CPAN?]](#How_do_I_list_all_Perl_modules_installed_from_CPAN.3F)
-   [[6] [See also]](#See_also)
-   [[7] [External Resources]](#External_Resources)
    -   [[7.1] [Learning Modern Perl]](#Learning_Modern_Perl)
        -   [[7.1.1] [Learning Perl Regular Expressions]](#Learning_Perl_Regular_Expressions)
        -   [[7.1.2] [Debugging and Testing]](#Debugging_and_Testing)
        -   [[7.1.3] [Cheat Sheets]](#Cheat_Sheets)
    -   [[7.2] [Modern Perl Tools]](#Modern_Perl_Tools)
        -   [[7.2.1] [Popular Perl Frameworks]](#Popular_Perl_Frameworks)
        -   [[7.2.2] [Code Documentation]](#Code_Documentation)
    -   [[7.3] [Miscellaneous]](#Miscellaneous)
-   [[8] [References]](#References)

## [Perl in Context]

### [Market Niche]

Perl powered almost the entirety of the early world wide web. To some, Perl is a primarily thought of as a glue language. To others, it\'s thought of as the \"Swiss Army Chainsaw\" of languages that allow for quick hacks to solve to complex problems. Because Perl is highly performant compared to most interpreted languages and it has a shell-like syntax. Consequently, it is often easier to maintain than equivalent scripts written in Bash. Additionally, thanks to the Mojolicious framework deploying modern microservices in Perl is almost trivial. This allows for Perl to hold its own in modern DevOps environments.

### [Pros]

-   Perl is multiparadigm: procedural, object oriented, and functional programming styles are supported.
-   Perl makes writing microservices very easy with the Mojolicious web framework.
-   The basic syntax is easy to learn, especially for those already familiar with [C](https://wiki.gentoo.org/wiki/C "C") or a POSIX shell.
-   Modern Perl is as readable as Ruby.
-   For an interpreted language, Perl is quite fast. Perl VM startup time is much faster than [Java](https://wiki.gentoo.org/wiki/Java "Java") and execution times are typically on par with [Python](https://wiki.gentoo.org/wiki/Python "Python").
-   It has a vast library of modules stored in the CPAN library, which is comparable to size and scope to Python\'s Pip.
-   Perl\'s Corinna object system is both low boilerplate and very expressive.
-   Perl deprecates features far less frequently than other languages, thus scripts can run unmodified *much* longer than is typical for most languages, except perhaps C.

### [Cons]

-   While Perl remains a popular choice for some tasks its developer community has shrank considerably from its heyday, having lost a lot of ground to Python. It now has a developer community similar in size to that of PHP.
-   In Perl there is always \"More than one way to do it!\" (TIMTOWTDI). On the one hand this allows for very expressive code, on the other hand this can be confusing to inexperienced developers.
-   Advanced uses of Perl involve a lot of \"magic\" behind the scenes that can be surprising to new developers. This allows for code that can be downright laconic.
-   Perl\'s regular expression syntax, though wildly ported to other languages thanks to the PCRE library, takes a while to get used to.

### [Complimentary Languages]

Perl is closely related to [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") and the two languages do share some syntax. Perl took inspiriation from C, grep, and awk. Both [PHP](https://wiki.gentoo.org/wiki/PHP "PHP") and [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby") took a lot of inspiration from Perl.

## [Introduction]

The Perl language itself is packaged as [dev-lang/perl]. There\'re three Perl-related categories:

1.  [[dev-perl](https://packages.gentoo.org/categories/dev-perl)]: Libraries in / for Perl, corresponding to [dev-java], [dev-python], etc. In most cases the package name directly corresponds to a [CPAN](https://wiki.gentoo.org/wiki/CPAN "CPAN") distribution.
2.  [[perl-core](https://packages.gentoo.org/categories/perl-core)]: Packages in this category are modules included in [dev-lang/perl], which are also independently packaged on CPAN. When modules are installed via [perl-core], they override the counterpart in the core [dev-lang/perl]. This can be used for selective bugfixes. For the details, see below - but please **never manually install any [perl-core] packages with emerge**.
3.  [[virtual/perl-\*](https://packages.gentoo.org/packages/search?q=virtual%2Fperl)]: Virtual packages that allow choosing a module between [perl-core/] packages and the one contained in the core [dev-lang/perl]. If you need a specific version of a core package, emerge the corresponding virtual - and the package manager will figure out if a perl-core/ package is needed or not.

More on perl-core^[\[1\]](#cite_note-1)^:

-   It allows users to have more update versions of some modules that the core ones.
-   It allows package-based installation, without bumping or patching the core perl.
-   Sometimes these modules get deprecated in newer Perl. Such cases are handled by virtual/perl-\*. Search [\[1\]](https://bugs.gentoo.org/show_bug.cgi?id=608168#c1) for \"Module::Build\" for more in-depth stories.

Normally you do not have to care at all about perl-core packages or virtuals; if you need any specifics there they should be pulled in as dependencies.

## [Installation]

### [USE flags]

#### [Global]

Since many packages depend on the perl, Portage is aware of the [[[perl]](https://packages.gentoo.org/useflags/perl)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag"). It can be enabled (or disabled) globally:

[FILE] **`/etc/portage/make.conf`**

    USE="perl"

This is typically only required if carrying out a lot of Perl development locally.

#### [Package]

### [USE flags for] [dev-lang/perl](https://packages.gentoo.org/packages/dev-lang/perl) [[]] [Larry Wall\'s Practical Extraction and Report Language]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------
  [`berkdb`](https://packages.gentoo.org/useflags/berkdb)     Add support for sys-libs/db (Berkeley DB)
  [`doc`](https://packages.gentoo.org/useflags/doc)           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gdbm`](https://packages.gentoo.org/useflags/gdbm)         Add support for sys-libs/gdbm (GNU database libraries)
  [`minimal`](https://packages.gentoo.org/useflags/minimal)   Install a very minimal build (disables, for example, plugins, fonts, most drivers, non-critical features)
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-06 21:41] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

As always, after adjusting USE flags, be sure to tell Portage to apply the changes to installed packages on the system:

`root `[`#`]`emerge --ask --update --changed-use --deep --autounmask-keep-masks=y @world`

In addition, after changing the `ithreads` or `debug` use flag setting, you need to re-build all packages installing perl modules or linking to libperl:

`root `[`#`]`perl-cleaner --reallyall`

## [Upgrading]

The official way of upgrading Perl, e.g. from Perl 5.36 to Perl 5.38, is upgrading your entire world, and upgrading Perl with it. This is because Portage needs to be able to rebuild packages depending on Perl. If you ask Portage to selectively only upgrade the Perl package itself, it can\'t do this and the emerge command will fail.

As in all cases when automatic rebuilds are involved, it helps a lot if you do regular updates and regularly run depclean.

### [The official way]

`root `[`#`]`emerge -uDNav --autounmask-keep-masks=y @world `

`root `[`#`]`perl-cleaner --all `

If this fails, please check your world file for packages which cannot be updated/reinstalled because they\'ve been removed or are in some way masked.

### [Some knowledge]

-   Perl modules are installed under *e.g.,* [/usr/lib/perl5/vendor_perl/5.36/]. Note that the core Perl version number is present. When upgrading Perl by a major version, the packages providing these modules have to be re-emerged, too.
-   The same is valid for all packages linking to libperl.
-   The rebuilds \'should\' be done automatically by emerge. `app-admin/perl-cleaner` exists to do them as well and can catch things missed by emerge (sadly Portage still has some bugs).
-   During Perl upgrade, packages that depend on Perl may become unavailable.
-   **No rebuilds are necessary during a point-release update** (i.e. from 5.36.0 to 5.36.1).

In order to upgrade your Perl installation to unstable (\~arch) version on an otherwise stable system, add the following text to `/etc/portage/package.accept_keywords`:

    # use Perl from ~arch
    dev-lang/perl
    perl-core/*
    virtual/perl-*

Perl itself, the perl-core packages and the Perl virtuals \'must\' have the same, consistent status (either all stable or all \~arch). What setting you use for dev-perl packages does not matter at all.

## [Troubleshooting]

### [][How do I list all Perl modules installed from CPAN?]

The following [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") one-liner can give you a list of all modules:

[CODE] **List Perl CPAN Modules**

    for MODULE in `perldoc -t perllocal | grep Module | sed -e 's/^.*" //'`; do VERSION=`perldoc -t perllocal | awk "/$MODULE/y" | grep VERSION | head -n 1`; printf "%30s %s\n" "$MODULE" "$VERSION"; done | sort

## [See also]

-   [Awk](https://wiki.gentoo.org/wiki/Awk "Awk") --- a scripting language for data extraction
-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [CPAN](https://wiki.gentoo.org/wiki/CPAN "CPAN") --- the *Comprehensive Perl Archive Network*, [Perl]\'s package ecosystem.
-   [Grep](https://wiki.gentoo.org/wiki/Grep "Grep") --- a tool for searching text files with regular expressions
-   [PHP](https://wiki.gentoo.org/wiki/PHP "PHP") --- a general-purpose server-side scripting language to produce dynamic web pages.
-   [Python](https://wiki.gentoo.org/wiki/Python "Python") --- an extremely popular cross-platform object oriented programming language.
-   [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") --- a high-level, general-purpose, and gradually typed programming language with low boilerplate objects, optionally immutable data structures, and an advanced macro system.
-   [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby") --- an interpreted programming language.
-   [Sed](https://wiki.gentoo.org/wiki/Sed "Sed") --- a program that uses regular expressions to programmatically modify streams of text

## [External Resources]

### [Learning Modern Perl]

-   [Why Perl?](https://two-wrongs.com/why-perl.html) --- A detailed but approachable article on the empowering nature of Perl while still remaining honest about its limitations.
-   [Learn X in Y minutes, Where X=Perl](https://learnxinyminutes.com/docs/perl/) --- A quick but well respected Perl primer.
-   [perlsyn](https://perldoc.perl.org/perlsyn) --- A guide to Perl\'s basic syntax.
-   [Modern Perl, 4e](http://modernperlbooks.com/books/modern_perl_2016/index.html) --- An in-depth guide to Perl though v5.22.
-   [Perl Maven](https://perlmaven.com/) --- A large collection of Perl tutorials written by a prominent member of the Perl community.
-   [perlclasstut](https://github.com/Perl-Apollo/Corinna/blob/master/pod/perlclasstut.pod) --- Object-Oriented Programming via the the Corinna object system which debuted in Perl 5.38.
-   [Corinna](https://github.com/Perl-Apollo/Corinna) --- The specification for Perl\'s modern object syntax as of Perl 5.38; very technically in depth, not really a tutorial.
-   [Rosetta Code: Perl](https://rosettacode.org/wiki/Category:Perl) --- examples of common programming tasks in Perl.
-   [Exercism\'s Perl 5 track](https://exercism.org/tracks/perl5) --- free interactive online lessons for learning Perl 5.

#### [Learning Perl Regular Expressions]

-   [perlrequick](https://perldoc.perl.org/perlrequick) --- Perl regular expressions quick start tutorial.
-   [perlretut](https://perldoc.perl.org/perlretut) --- Perl\'s in depth regular expressions tutorial.
-   [Regular Expressions.info](https://www.regular-expressions.info/) --- An extensive collection of regular expression related resources.
-   [RegexOne](https://regexone.com/) --- Learn basic regular expressions with simple interactive exercises.
-   [Regex Crossword](https://regexcrossword.com/) --- A crossword puzzle game with clues written as regular expression patterns.

#### [Debugging and Testing]

-   [perldebug](https://perldoc.perl.org/perldebug) --- A guide to Perl debugging.
-   [perltrap](https://perldoc.perl.org/perltrap) --- Traps and \"foot-guns\" for the unwary.
-   [Test::Tutorial](https://perldoc.perl.org/Test::Tutorial) --- A tutorial for writing basic tests with [Test Anything Protocol](https://testanything.org/) (TAP).

#### [Cheat Sheets]

-   [perlcheat](https://perldoc.perl.org/perlcheat) --- Perl 5\'s cheat sheet.
-   [Regex Cheat Sheet](https://perlmaven.com/regex-cheat-sheet) --- a Perl 5 regex cheat sheet.

### [Modern Perl Tools]

-   [App::cpanminus](https://metacpan.org/pod/App::cpanminus) --- A modern CPAN client.
-   [Perl::Critic](https://metacpan.org/pod/Perl::Critic) --- Critique Perl source code for best-practices.
-   [Perl::Tidy](https://metacpan.org/pod/Perl::Tidy) --- Beautify and enhance the readability of Perl source.
-   [App::opan](https://metacpan.org/pod/App::opan) --- A CPAN overlay with local repository (darkpan) support and module version pinning capability.
-   [Perlbrew](https://perlbrew.pl/) --- An Perl installation management tool allowing programmers to decouple their code from system Perl.
-   [zarn](https://github.com/htrgouvea/zarn) --- A lightweight static analysis tool for modern Perl application security.
-   [(R)?ex](https://www.rexify.org/) --- A user friendly automation framework written in Perl.

#### [Popular Perl Frameworks]

-   [Mojolicious](https://mojolicious.org/) --- Mojolicious is a fresh take on web development.
-   [Catalyst](http://catalyst.perl.org) --- the Elegant MVC web application framework.
-   [Dancer](https://perldancer.org/) --- Dancer is a simple but powerful web application framework.
-   [Template::Toolkit](https://metacpan.org/pod/Template::Toolkit) --- Perl\'s famous Template Processing System.

#### [Code Documentation]

-   [perlpod](https://perldoc.perl.org/perlpod) --- the Plain Old Documentation (POD) format, Perl\'s native documentation format.
-   [perlpodstyle](https://perldoc.perl.org/perlpodstyle) --- Perl\'s Plain Old Documentation (POD) style guide.
-   [podchecker](https://metacpan.org/pod/podchecker) --- A tool for checking the syntax of Plain Old Documentation (POD) documentations.
-   [pod2man](https://perldoc.perl.org/pod2man) --- A tool for converting POD data to roff (man page) format.
-   [pod2html](https://perldoc.perl.org/pod2html) --- A tool for converting POD files to HTML format.
-   [Doxygen::Filter::Perl](https://metacpan.org/pod/Doxygen::Filter::Perl) --- A Perl code pre-filter for [Doxygen](https://en.wikipedia.org/wiki/Doxygen "wikipedia:Doxygen")-style comments.

### [Miscellaneous]

-   [Awesome Perl](https://github.com/uhub/awesome-perl) --- a curated list of Perl frameworks.
-   [Perl Power Tools](https://github.com/briandfoy/PerlPowerTools) --- BSD tools rewritten in Perl.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://bugs.gentoo.org/show_bug.cgi?id=608168#c1](https://bugs.gentoo.org/show_bug.cgi?id=608168#c1)]]