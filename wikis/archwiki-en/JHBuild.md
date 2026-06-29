# JHBuild

From JHBuild's wiki:
:JHBuild allows you to build and run GNOME platform and applications building the required modules in a sandbox environment, isolating the installation; so there is no need to build and run GNOME inside a virtual machine.

JHBuild is a tool that allows you to automatically download and compile "modules" (i.e. source code packages). It can pull modules from a variety of sources (CVS, Subversion, Git, Bazaar, tarballs, etc.) and handle dependencies. You can also choose which specific modules you want to build, instead of building the whole project.

JHBuild was originally written for building GNOME, but has since been extended to be usable with other projects.

## Installation
Install the  package.

## Configuration
There are two configuration files: the default configuration file installed by  package, and the user-specific configuration file created by the user.

By default JHBuild uses the installed configuration file. Its configuration is overridden by the configuration in the user-specific configuration file if it exists.

These use Python syntax. See JHBuild Manual for more information.

## Default configuration file
The default configuration file is located at . It should have everything you need for start using JHBuild, as it sets the modulesets directory, the default moduleset, autogen/meson/cmake arguments for all modules that use it.

Some default values currently set:
* moduleset =
* modules =
* directory of downloaded tarball =
* buildroot =

If believe you found a Arch-specific setting that should be set, feel free to suggest that in  comments. If not Arch-specific, consider filing an issue in the upstream.

## User-specific configuration file
This configuration file is located at  (e.g. ). It is optional, does not exist by default and overrides values set in the default JHBuild configuration file.

It is very useful for, e.g., set a different moduleset, or to add a compiler flag to debug and try to fix a build failure system.

See examples in .

## Sample configuration
This section shows a non-exhaustive list of key/value pairs that can be set in any of the configuration files.

* Use a local moduleset file instead of downloading it again, making it possible to change something in the file and test it

* Enable a wide-most moduleset, and also force GTK3 for modules that would use GTK2 by default

* Or you may want to enable documentation build for autotools, even though it will slowdown module compilation

* Or you want some debug output from make command

* Or you found out that a module requires a specific automake option (WebKit is already patched, there is no real need for this one)

* Or you want to disable documentation build for a module that use meson build system

## Usage
This topic provides some information and examples on how to use some JHBuild commands, but without intending to exhaust the subject. For a detailed information on each of JHBuild commands, please refer to JHBuild Manual, learn from each command's help output or even read JHBuild's source code.

JHBuild provides a general  which lists all the commands available, and also a help message for each sub-command, e.g. .

## Checking and installing prerequisites
sysdeps can be used to get a detailed list of which dependencies you have installed and which ones you should install. In order to get this information, just run:

 $ jhbuild sysdeps

To install missing dependencies,  run use  parameter:

 $ jhbuild sysdeps --install

For dependencies that the above command is unable install, consider installing the correspondent package from official repositories or the AUR.

## Updating modules
It is possible to simply update the source code of the modules without building them, making it possible build another time without having to wait fetching the source code. There are three ways of simply updating modules:

update, without any arguments, will update all modules available in the moduleset/modules set in configuration file

 $ jhbuild update

update, with one or more modules as arguments, will update all modules that the named modules depends on. e.g.:

 $ jhbuild update gedit

updateone, with one or more modules, will update only the named module(s). e.g.:

 $ jhbuild updateonly gedit

## Building modules
This action will run the whole build process: it will update the source code (unless it is already up-to-date), configure & build, and install it in the proper directory.

Just like update, There are three ways of building modules in JHBuild:

build, without any arguments, will build all modules available in the moduleset/modules set in configuration file

 $ jhbuild build

build, with one or more modules as arguments, will build all modules that the named modules depends on. e.g.:

 $ jhbuild build gedit

buildone, with one or more modules, will build only the named module(s). e.g.:

 $ jhbuild buildone gedit

## Running modules
After a successfully installed application in JHBuild, use run to start the module you just built. e.g.:

 $ jhbuild run gedit

## Creating dependency graph
JHBuild can output graph contents which can by piped into  in order to generate e.g. a PNG or PostScript file.

To generate a PNG file of e.g. gedit, run:

 $ jhbuild dot gedit | dot -Tpng > dependencies.png

## Troubleshooting
## Python issues
A module that depends on  may fail to build as software usually expect the binary filename of python 2.x to be  and python 3.x to be , which is not the case in Arch Linux: python 2.x is  and python 3.x is .

For cases like that, force the modules to run  using the one or more methods below:

* set  with  for this specific module in , as mentioned in the above Configuration section — this will run autogen.sh or configure with this value for variable PYTHON

* if the configure or Makefile does not parse PYTHON variable, one approach is to manually find all lines in configure/Makefile that run python binary and rename python -> python2 — this will hard code python2 in the module's source code.

* if only the above workarounds still do not work for you, consider editing module's .py files in order to replace  with  when the first line matches  or

## pkg-config issues
If you have a malformatted .pc file on your PKG_CONFIG_PATH, JHBuild will not be able to detect all the (valid) .pc files you have installed and will complain that the .pc files are missing. Look at the output of —there should be a message about the problematic .pc files.

## Build failed due to incompatible meson versions
You may come across with a message similar to one of these below.

In the above example, the module was configured with meson 0.40.0 at on time, but a newer version (0.40.1, in the example) is now installed and is not compatible with the old one.

Solution: Run Configure phase again, in order to have this module configured with newer Meson version

## Build failed due to GCC library or object not found
You may come across with a message similar to the one below.

or

where gcc_version is a GCC version older than the current one, and name is the name of the library (.so) or object (.o) that failed to be found.

This may happen if  was updated and the software was previously configured and built with the previous version of gcc.

Solution: Run Configure phase again, in order to have this module configured with newer GCC version

## gst-plugin-bad fails on missing vulkan headers
When building the gst-plugins-bad module, You may come across with a number of messages similar to the one below:

It means gst-plugin-bad was automatically set to build its vulkan extension, but did not find all the dependecies it needs. As of the writing this subsection, ext/vulkan/meson.build looks for the binary glslc provided by , which several packages depend on directly or indirectly. Removing  would solve this error, but this might not be an option if you want to keep those packages depend on it.

Solution: edit your jhbuild user configuration file to disable the vulkan extension:

and run Configure phase again, in order to have the gst-plugins-bad module successfully built.

## Library missing and no known rule to make it
When building a module that uses meson build system you might come across an issue like this:

This happens because the module was previously configured and built in another commit of this module, and in that occasion it was configured to a previous version of the dependency . Since the file  was configured to and expects that missing library to be available, it fails.

Solution: Just run option 7 for the configure phase to reconfigure the module and build it again.

## Building JHBuild from scratch
If you do not want to use the  package, and instead you want build JHBuild from scratch on your own, there are a few things you should pay attention too.

* Make sure to install all the dependencies required by JHBuild and its target modules. Refer to list of dependencies for Arch Linux;

* JHBuild itself used to depend on Python version 2 but it got migrated to python 3, so no specific configuration on python version;

* Some modules might still depend on python2. Make sure to read the #Python issues section;

* For detailed information downloading and building the source code of JHBuild, check JHBuild's "How Do I" at GNOME wiki.
