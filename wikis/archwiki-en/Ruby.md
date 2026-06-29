# Ruby

Ruby is a dynamic, interpreted, open source programming language with a focus on simplicity and productivity.

## Installation
To use Ruby, install the  package.

To install IRB, install the  package.

## Multiple versions
If you want to run multiple versions on the same system (e.g. 2.0.0-p0 and 1.9.3-p392),
the easiest way is to use one of RVM, , rbenv, .

## Documentation
To make documentation available through the  command-line tool,
install  and  for the documentation itself.
You can then query the docs with: ,  etc. (much like man-pages)

## JRuby
The Java implementation of Ruby, JRuby can be installed with the  package.

## Standard Library
Part of Ruby's standard library consists of Ruby modules (see RubyGems for more
information about modules.) The  package does not include all of the standard modules
that a Ruby user can assume to be installed on any Ruby system, so some Ruby code may not work
out-of-the-box. More information about the set of standard library modules can be found at
https://stdgems.org/.

The RubyGems section discusses several methods for installing modules. To install
the standard modules system-wide using pacman, one can install the
package. Note that this is not needed for JRuby, as the  package includes the standard
modules.

## RubyGems
RubyGems is a package manager for Ruby modules (called gems),
somewhat comparable to what pacman is to Arch Linux.
It can be installed with the  package, which is a dependency of .

## Configuration
By default in Arch Linux, when running , gems are installed per-user (into ), instead of system-wide (into ). This is considered the best way to manage gems on Arch, because otherwise they might interfere with gems installed by Pacman.

The recommended way to setup that is by manually specifying your , which then can be appended to your  environment variable in order to allow RubyGems binaries to be executed:

This is required for executable gems to work without typing out the full location, although libraries will work without having to modify your path.

Use  to view the current RubyGems environment:

 $ gem env

## Usage
To see what gems are installed:
 $ gem list

To get information about a gem:
 $ gem spec gem_name

By default,  and  use the  option, which forces gem to search only the local system. This can be overridden with the  flag. Thus, to search for the mysql2 gem:
 $ gem list --remote mysql2

To install a gem:
 $ gem install mysql2

The process can be sped up somewhat if you do not need local documentation:
 $ gem install mysql2 --no-document

To update all installed gems:
 $ gem update

## Installing gems system-wide
Gems can be installed system wide by running the  command as root, appended with the  flag. This flag can be set as default by replacing  by  in  (system-wide) or  (per-user, overrides system-wide).

Bundler can be used to avoid system-wide gem installations by packaging gems into your application. See the section below on using bundler.

## Bundler
Bundler allows you to specify which gems your application depends upon, and optionally which version those gems should be. Once this specification is in place, Bundler installs all required gems (including the full gem dependency tree) and logs the results for later inspection. By default, Bundler installs gems into a shared location, but they can also be installed directly into your application. When your application is run, Bundler provides the correct version of each gem, even if multiple versions of each gem have been installed. This requires a little bit of work: applications should be called with , and two lines of boilerplate code must be placed in your application's main executable.

To install Bundler:
 $ gem install bundler

To start a new bundle:
 $ bundle init

Then edit  in the current directory (created by bundle init) and list your required gems:

Run the following to install gems into :
 $ bundle install

Alternatively, run the following to install gems to  in the working directory:
 $ bundle config set --local path '.bundle'

Do not forget to edit your main executable:

Finally, run your program:

 $ bundle exec main_executable_name.rb

## Managing RubyGems using pacman
Instead of managing gems with , you can use pacman, or an AUR helper. Ruby packages follow the naming convention ruby-gemname.

This option provides the following advantages:
* Gems are updated along with the rest of your system.
* Installed gems are available system-wide, instead of being available only to the user who installed them.

## Quarry
Quarry is a tool that allows to maintain a rubygems binary repository for Arch Linux, as an easier alternative to building packages manually from the AUR. The source is hosted at Github.

The repository is maintained by the Arch developer anatolik at https://pkgbuild.com/~anatolik/quarry/. It contains many popular gems and new gems can be added upon request.

See Unofficial user repositories#quarry to enable it.

Then install the required gem. The name of the package is .

General questions can be asked at https://bbs.archlinux.org/viewtopic.php?id=182729.

## Interactive Shell
## Pry
Pry is a powerful alternative to the standard IRB shell for Ruby. It features syntax highlighting, a flexible plugin architecture, runtime invocation and source and documentation browsing.

 $ gem install pry
 $ pry

## Performance Tuning
## Enable JIT
 is built with JIT support which is disabled by default. JIT can optimize hot code paths for long running program (e.g. servers). Enable it with:

 $ ruby --jit

For other commands that doesn't accept , you can pass the argument to Ruby with the environment variable  e.g. .

## jemalloc
Ruby can use  instead of malloc(3) as its default memory allocator. It can reduce memory bloat. To enable it, install  and run Ruby with:

 $ LD_PRELOAD=libjemalloc.so ruby ...

To verify that jemalloc is actually being used:

 $ LD_PRELOAD=libjemalloc.so MALLOC_CONF=stats_print:true ruby -e exit
