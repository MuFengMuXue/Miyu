# Haskell

From Wikipedia:

* it is a general-purpose, statically typed, purely functional programming language with type inference and lazy evaluation;
* it has pioneered type classes, which enable type-safe operator overloading.

## Installation
There are several choices for Haskell installation. One is supported by Arch Linux, while others are officially supported by Haskell for any Linux distribution.

Since version 8.0.2-1, the Arch  package and all haskell-* packages in extra provide only dynamically linked libraries.

Using dynamic linking typically results in faster builds and smaller disk and RAM usage (by sharing pages between multiple running Haskell programs), and will free you from troubleshooting cross-GHC mixing errors. For this reason using pacman and the official repositories is preferred for managing end-user applications. But it has its own disadvantage: all tools you install from source will break on every update of ,  or haskell-* packages since libraries compiled with GHC do not provide a stable ABI. When running such broken binary, you will see the usual message:

 error while loading shared libraries: libHS...so: cannot open shared object file: No such file or directory

To fix this, just rebuild and reinstall the broken tool in order to relink it to newer libraries.

On the other hand, static linking is generally easier to maintain, does not force you to rebuild all tools from source after every update of their dependencies and is currently better supported by the GHC. For these reasons, static linking is the preferred and recommended option for local development. Otherwise, if you want dynamic linking, to link successfully one must configure GHC, Cabal and Stack for this, as the default is to use static linking.

* To install Haskell from Arch official repositories using pacman, continue reading #Native installation. Note that this might install several hundred  packages into your system.
* Otherwise, skip to the section #Alternate installations.

If you wish to use  (from the official repositories) with static linking, it is possible, but is more complex to setup, see #Static linking.

## Native installation
To use Haskell, install the following packages:

#  — A Haskell compiler. There are several implementations available, but the one used most (which is now de facto the reference) is the GHC (Glasgow Haskell Compiler).
#  or  — Build tools that rely on GHC to compile Haskell sources. Cabal is the classic build tool focused on dependency resolution and source packages from Hackage (Haskell community's central package archive of open source software). Stack is another build tool focused on curated snapshots and source packages from Stackage (a stable subset of Hackage that provides curated sets (snapshots) of packages known to work well with each other).

## Configuration
## Invoking GHC directly
In order to link successfully one must pass the  flag to GHC. You can try it with the following file:

Compile and run it with:

## Configuring Cabal for dynamic linking
First, run the following command to download the latest list of packages from Hackage and create global configuration file  (or the file  points to):

 $ cabal update

To configure Cabal for dynamic linking, uncomment and edit the following options in :

*  suppresses the creation of static libraries (if your project contains a library).
*  enables the creation of shared libraries (if your project contains a library).
*  causes dynamic linking to be used for executables (if your project contains executables).
*  adds the  flag to every invocation of GHC (e.g. if a package has a non-trivial ).

## Configuring Stack for dynamic linking
You can use  command to initialize Stack and create global configuration file . By default Stack will automatically download its own version of GHC to an isolated location upon first invocation. To force Stack to use system GHC installation instead, run  with  and  flags:

 $ stack setup --system-ghc --resolver resolver

Note that you need to specify a resolver which is compatible with your system GHC. Otherwise Stack will happily ignore  flag and download its own copy of GHC. You can determine the version of system GHC using  command:

Then visit Stackage website and pick a suitable Long Term Support (LTS) or nightly snapshot matching your system GHC version. Use the selected snapshot for  flag on the command line, e.g.  or .

Stackage typically lags behind new GHC releases. It may happen that no Stackage snapshot for your system GHC has yet been released. In this case you might want to choose a snapshot for some earlier minor version of GHC or temporarily downgrade your Haskell installation and wait until support for newer GHC releases finally lands on Stackage.

To configure Stack for dynamic linking, add the following snippet:

## Package management
Most of Haskell libraries and executables are distributed in units of source packages available from Hackage and Stackage. Repositories used by Cabal and Stack respectively.

GHC, the standard compiler for Haskell, generates machine code that can be run natively on Linux. As is common in other compiled languages, a number of popular Haskell packages are available from official Arch repositories in pre-built form.

Some additional packages can be installed from AUR. This packages may need to build from source, building AUR packages or developing software require a compiler and build tools to be installed. Using the #Native installation method is discouraged for this use case, instead see #Alternate installations.

Therefore there are four main sources for Haskell packages: Hackage (Cabal), Stackage (Stack), official repositories and AUR.

The following table summarizes the advantages and disadvantages of different package management styles.

{| class="wikitable"
! Method
! Pros
! Cons
|-
| Official repositories ||
* Easier package management using pacman
* Already compiled dynamically linked
||
* Not all packages available
* Makes difficult compiling from source
|-
| Cabal ||
* All packages available
* Root not required
* Better support for development
||
* Installed in home directory
* Difficult to remove specific packages
|-
| Stack ||
* All packages available (favors Stackage)
* Root not required
* Better support for development
||
* Installed in home directory
* Versions are pinned to snapshot
* Difficult to remove specific packages
|-
| AUR ||
* Additional packages available
||
* Risk of unmaintained or orphaned packages
* Incompatible versions of packages possible
|-
|}

## Cabal
Cabal is "the original" build system for Haskell. Most of libraries and tools you can find on Hackage can be installed via Cabal.

## Installing packages
To run user-wide executables installed by Cabal,  must be added to the  environment variable.

 export PATH="$HOME/.cabal/bin:$PATH"

Run the following command to install a Hackage package and all of its dependencies in a single step:

 $ cabal install package

You can also build and install a Haskell package from source. To do this, run  without specifying any package in the directory with the sources.

Each Cabal package should specify a list of its dependencies and their version constraints in the  file according to the Package Versioning Policy (PVP). During the package installation, Cabal tries to find a set of dependencies that satisfies all the constraints. This process is called dependency resolution.

There are reasons why Stack exists; Cabal is known to generate a lot of friction with beginners, although it has been getting better in the past years. Most of the time dependency resolution works well but sometimes it fails. In this case you will need to figure out the cause of the problem and give Cabal some hints about how to resolve offending dependencies. For example, sometimes it is necessary to add  to allow Cabal to ignore package's PVP-dictated upper bounds on dependency versions, effectively installing package with newer dependencies than the package author has permitted. It gets hairier for less-well maintained packages; for another example, see this thread about installing Idris (another programming language, written in Haskell), where one had to use both  and  command-line flags to get a successful compile.

## Removing packages
There is no easy way to do it. Cabal does not have support for this functionality but there are external tools like cabal-store-gc.

To reinstall the entire user-wide Haskell package system, remove  and  and start from scratch. This is often necessary when GHC is upgraded.

For more precision, it is possible to use  or / directly on the user package database — this makes GHC "forget" about an installed package (or pretend it is not there). However neither of these removes any files.

## Stack
Stack is another tool to manage Haskell packages. It has slightly different goals than Cabal, with a slightly different philosophy. It uses Cabal library under the hood and integrates with Hackage — but maintains its own repositories of packages (snapshots) on Stackage with the promise that snapshots are curated and include packages which work well together.

## Installing packages
In its default configuration, Stack installs compiled executables to . Add this directory to the  environment variable, ideally via your shell configuration file:

 export PATH="$HOME/.local/bin:$PATH"

Run the following command to download, build and install a Stackage package:

 $ stack install package

You can also build and install a Haskell package from source by running the following command from the package directory:

 $ stack install --resolver resolver

Note that you should specify the same resolver as one used for  command.

## Removing packages
Stack does not support the "uninstall" operation.

If you want to reinstall the entire user-wide Haskell package system, remove  directory and start from scratch. This is often necessary when GHC is upgraded.

## Development tools
## Tools
## haskell-language-server
haskell-language-server is a Language Server Protocol (LSP) implementation for Haskell. It provides IDE-like features such as code completion, "goto definition", documentation on hover, linting, formatting or refactoring for any editor integrating with the LSP.

If you are using dynamically linked Haskell packages from pacman, install . Otherwise, if you prefer static linking, install . This package contains statically linked binaries for each supported version of GHC. Alternatively, haskell-language-server can be installed via ghcup or by the Haskell extension for Visual Studio Code.

haskell-language-server will attempt to automatically determine the build configuration when you open your project. If automatic detection fails, you might want to configure it manually using a  file in the project root directory.

## ghcid
ghcid is a GHCi-based tool for Haskell development that provides simple and robust way to display compiler errors and warnings on every source code change. It can be installed via  package.

## hoogle
hoogle allows you to search the Haskell libraries by either function name, or by approximate type signature. It can be installed via  package.

An online version of hoogle is available at https://hoogle.haskell.org.

## Linters
## hlint
hlint suggests possible improvements to Haskell code such as using alternative functions, simplifying code and spotting redundancies. It is available through  package.

## stan
stan is a Haskell static analyzer, complementary to hlint. It is in the beta phase as of December 2025. Available in .

## weeder
weeder is an application to perform whole-program dead-code analysis.

## Formatters
*
*
*
*
*

## Editors
## Visual Studio Code
Visual Studio Code has a Haskell extension powered by haskell-language-server. If you do not have haskell-language-server installed, the Haskell extension will automatically download and install statically linked Linux binaries for you.

## IntelliJ IDEA
IntelliJ IDEA support for Haskell is provided by the Haskell LSP plugin. It works with any edition of IntelliJ IDEA including .

You will need to install Stack in order to create a new project or import an existing one into IntelliJ IDEA. As of June 2021 Cabal-only projects are not supported.

## Vim
Basic syntax highlighting and indentation for Vim can be obtained via the haskell-vim plugin. For better IDE-like experience use one of LSP client plugins (e.g. coc.nvim, ALE, LanguageClient-neovim) together with haskell-language-server.

## Emacs
Basic Emacs support for Haskell is provided by the official haskell-mode. For more advanced features, also use lsp-haskell with haskell-language-server.

## Alternate installations
The methods described in this sections are best suited for Haskell development setups. It is possible to use them along packages from the official repositories, if this is the case, make sure you know which version of the Haskell package you are using, if the one installed by pacman or by one of the following methods.

## ghcup
This is the recommended method for installing Haskell in any Linux distribution. GHCup installs GHC, tools and libraries in your home directory and allows to have multiple versions in parallel and handle them with relative ease. It is similar in scope to rustup, pyenv and jenv.

Install  package. Alternatively, you may follow official installation instructions or manually download ghcup binary and place it somewhere into your .

By default, ghcup will install executables into . You need to add this directory to the  environment variable in your shell configuration file, for instance  for  or  for . If you want to run executables installed by Cabal, add  to  as well:

 export PATH="$HOME/.cabal/bin:$HOME/.ghcup/bin:$PATH"

GHCup provides a convenient TUI which supports most of its functionality:

 $ ghcup tui

Alternatively, you can use the following CLI commands:

List available versions of GHC and Cabal:

 $ ghcup list

Install the recommended version of GHC:

 $ ghcup install ghc

You can also install a specific version of GHC, for example:

 $ ghcup install ghc 8.10.2

The commands above do not automatically make GHC available on the . You need to select which GHC version to use by default:

 $ ghcup set ghc 8.10.2

Install the recommended version of Cabal:

 $ ghcup install cabal

GHCup can install haskell-language-server too, use the following command:

 $ ghcup install hls

For more information, refer to official ghcup and Cabal documentation.

## Using along native installation
In case you decide to use GHCup and Cabal along the native installation you need to specify Cabal which GHC to use specifying the path of the GHC version to use, search for the line  and uncomment it:

Remember that the path of your GHC in case of using GHCup is going to be under . Also GHCup, once you set the GHC version you wish, will link that version to . If you set that path in the Cabal configuration, you can change which version of GHC Cabal uses using GHCup.

## Stack
You can install Stack using the  package or using GHCup (see #ghcup). Alternatively, you may follow official installation instructions or manually download Stack binary and place it somewhere into your .

If you want to run executables installed by Stack, add  directory to the , see Environment variables for more information on how to do this.

Stack will use an isolated version of GHC, so it does not require any additional configuration. Run  to automatically install GHC from the latest Stackage LTS snapshot:

 $ stack setup

You can now use Stack to build and install statically linked Haskell packages without any special configuration or command line flags:

 $ stack install package

For more information, refer to official Stack documentation.

## Nix
A completely different way of installing Haskell is Nix package manager. Nix has a steeper learning curve but offers greater flexibility in managing both Haskell and non-Haskell packages in a reliable and reproducible fashion.

## Tips and tricks
## Static linking
To use static linking, one must, at minimum, install the static boot libraries through the  package. This would allow you to build projects that depend exclusively on the boot libraries as well as on any other libraries that are not installed through the  packages from the official repositories.

Unfortunately, if your project depends on any of dynamically linked  packages that you have installed, Cabal does not take the absence of static libraries into account during dependency resolution. As a result, it will try to use the existing  package and then fail with linker errors when it discovers the static libraries are missing:

 Could not find module ‘SomePackage.SomeModule’
 There are files missing in the ‘somepackage-0.1.0.0’ package,
 try running 'ghc-pkg check'.
 Use -v (or `:set -v` in ghci) to see a list of the files searched for.

Unlike , there are no "" packages available for linkage. There are other ways to work around this issue though, as described in each of the sections below.

## Static global package database
A direct approach is offered by the official  package, which exposes an alternative "static" global package database at . The static database is limited to only the statically linkable boot packages, therefore if Cabal is reconfigured to use the static database instead of the default database, it would behave as though the dynamic-only  packages do not exist.

The precise path of the static database could be determined at build time using a command such as:

Here is how to enable the static database for use:

* When building packages with Cabal, one can pass the following flag to limit the selection of global packages to only the boot packages:

 $ cabal configure --ghc-pkg-option="--global-package-db=$(ghc --print-global-package-db | sed 's/\(package\.conf\.d\)$/static-\1/')"

* When building directly using GHC rather than Cabal, one can pass the following flags to override the global package database:

 $ ghc -clear-package-db -package-db "$(ghc --print-global-package-db | sed 's/\(package\.conf\.d\)$/static-\1/')" -user-package-db ...

## ghc-pristine
Install  package, which wraps over an existing GHC installation to create a separate GHC distribution in , with a package database that contains only boot libraries. This effectively creates a semi-isolated environment without dynamically linked  packages, but still makes use of the GHC compiler from the official repositories. Then, to build software with static linking, one simply needs to invoke the wrapped compiler . For Cabal, this amounts to the following configuration in :

You can also specify the path to the compiler on a per-project basis by running the following command from the project directory:

 $ cabal configure --with-compiler=/usr/share/ghc-pristine/bin/ghc

## stack-static
Install  package. Similarly to  method, make sure that the only other Haskell packages you have installed from the official repositories are ,  and . Then setup Stack to use system GHC as explained in #Configuring Stack for dynamic linking:

 $ stack setup --system-ghc --resolver resolver

To make these options permanent, paste the following snippet to :

This configuration will allow you to build statically linked packages as you would normally do, but using system GHC installation instead of GHC provided by Stack.

## hpack-static-bin
 provides a statically linked (meaning no  dependencies) alternative to . It is precompiled, so no make dependencies are needed.
