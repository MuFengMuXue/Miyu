**Gem**s are programs and libraries for the [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby") programming language. They are distributed by Ruby\'s package manager, which is called RubyGems, which is accessed by the [gem] command.

This page is meant to be Ruby equivalent of Python\'s [[pip](https://wiki.gentoo.org/wiki/Pip "Pip")] page.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Gem installation]](#Gem_installation)
    -   [[2.3] [View gem\'s environment]](#View_gem.27s_environment)
    -   [[2.4] [Removal]](#Removal)
    -   [[2.5] [Update]](#Update)
    -   [[2.6] [List]](#List)
-   [[3] [See also]](#See_also)

## [Installation]

The [gem] command is installed with the RubyGems package, which will be installed to support the Ruby programming language. It is not advised to install RubyGems to the system\'s world set. See the [Ruby article](https://wiki.gentoo.org/wiki/Ruby "Ruby") for more information.

### [USE flags]

### [USE flags for] [dev-ruby/rubygems](https://packages.gentoo.org/packages/dev-ruby/rubygems) [[]] [Centralized Ruby extension management system]

  --------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`server`](https://packages.gentoo.org/useflags/server)   Install support for the rubygems server
  [`test`](https://packages.gentoo.org/useflags/test)       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-07 19:06] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-ruby/rubygems`

## [Usage]

### [Invocation]

`user `[`$`]`gem --help`

    RubyGems is a sophisticated package manager for Ruby.  This is a
    basic help message containing pointers to more information.

      Usage:
        gem -h/--help
        gem -v/--version
        gem command [arguments...] [options...]

      Examples:
        gem install rake
        gem list --local
        gem build package.gemspec
        gem help install

      Further help:
        gem help commands            list all 'gem' commands
        gem help examples            show some examples of usage
        gem help gem_dependencies    gem dependencies file guide
        gem help platforms           gem platforms guide
        gem help <COMMAND>           show help on COMMAND
                                       (e.g. 'gem help install')
        gem server                   present a web page at
                                     http://localhost:8808/
                                     with info about installed gems
      Further information:
        http://guides.rubygems.org

### [Gem installation]

To install a package using the [gem] command, where `gems` is the desired gems:

`user `[`$`]`gem install <gems>`

### [][View gem\'s environment]

The following command can be used to query gem installation paths and other useful information:

`user `[`$`]`gem env`

See the [Application level package management](https://wiki.gentoo.org/wiki/Application_level_package_management "Application level package management") article for best practices and information on adding gem binaries the user\'s `PATH`.

### [Removal]

`user `[`$`]`gem uninstall <gems>`

### [Update]

`user `[`$`]`gem update <gems>`

### [List]

`user `[`$`]`gem list`

## [See also]

-   [Application level package management](https://wiki.gentoo.org/wiki/Application_level_package_management "Application level package management") --- provides best practice recommendations on managing the coexistence of operating system and **application level package managers** on Gentoo.
-   [pip](https://wiki.gentoo.org/wiki/Pip "Pip") --- [Python](https://wiki.gentoo.org/wiki/Python "Python")\'s package management system. It references packages available in the official **Py**thon **P**ackage **I**ndex (PyPI).
-   [Project:Ruby/Packaging RubyGems](https://wiki.gentoo.org/wiki/Project:Ruby/Packaging_RubyGems "Project:Ruby/Packaging RubyGems")