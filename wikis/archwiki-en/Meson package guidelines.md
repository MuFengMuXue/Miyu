# Meson package guidelines

From Meson's official website:

:Meson is an open source build system meant to be both extremely fast, and, even more importantly, as user friendly as possible.

Written in Python, Meson features multi-platform support, support for several programming languages, cross compilation, and more.

Meson does not build software directly, but rather sets up a back-end build system. While it is commonly used with , other build systems can be used. It is commonly used to replace GNU Build System.

This document covers standards and guidelines on writing PKGBUILDs for software that uses Meson.

## Usage
## Requirements
 has to be included to the PKGBUILD's makedepends array.

 makedepends(meson other_deps)

## prepare()
Meson has a utility to manage subprojects and can download them all in advance. Running this command in the prepare() stage allows the build() and other stages to be executed completely offline.

Example:

 prepare() {
   meson subprojects download --sourcedir=source
 }

## build()
Configuring and building is normally done using meson binary, but it can also be done by using Arch Linux's arch-meson wrapper script.

Both meson and arch-meson commands include in the usage syntax options, source directory and build directory:

* options: must include at least , but make sure to check other options with ; also check software-specific build options.
* source directory (or "sourcedir"): where the software's source code is stored, e.g. ,  or .
* build directory (or "builddir"): where the build files will stored by Meson; commonly named  or , but it is discretionary.

## Using meson binary directly
This method uses , which is the similar to the  command used by the GNU Build System.

The  command-line flag must always be passed to  because Arch Linux packages must not install files to , according Arch package guidelines#Package etiquette. The  built-in option can be set to another value, if you know what you are doing.

Example:

 build() {
   meson setup --prefix=/usr --buildtype=plain build source
   meson compile -C build
 }

 is a wrapper for supported back-end build systems, which currently defaults to ninja==== Using arch-meson wrapper script ====

arch-meson is a wrapper script included in  package which has the advantage of setting some of Meson built-in options that would probably be used in an Arch package, saving packager's time and code in the PKGBUILD. Quoting the description written in arch-meson, it is a "Highly opinionated wrapper for Arch Linux packaging".

Example:

 build() {
   arch-meson build source
   meson compile -C build
 }

## Setting software-specific build options
While Meson has some [https://mesonbuild.com/Builtin-options.html built-in build options (e.g. ), the software being packaged could have other build options which the packager should consider. Valid software-specific build options, if present, are normally found in a file named  (supported since Meson 1.1) or . Look for  in these files, then read the .

To use a software-specific build option, use the notation , where  is the build option name set in the project and  is a valid value, like e.g. .

For instance,  has the following build options:

So, to build its documentation, one must run Meson appending  build option, resulting in a command line like e.g.

 arch-meson $pkgname-$pkgver build -Dgtk_doc=true

## check()
If the software being packaged provides test suite, consider running it in the PKGBUILD's check() function. This can be accomplished with  command.

Example:

 check() {
   meson test -C build
 }

where  is the same build directory name used in the above #build() step.

See  and Unit tests in Meson docs for more info.

## package()
Packaging normally requires running only , but check if another installation command is required (e.g. an uncommon license). Use the same build directory as above and set the  flag:

 package() {
   meson install -C build --destdir "$pkgdir"
 }

## Troubleshooting
## ERROR: Function does not take positional arguments
Example of error output:

  data/meson.build:21:5: ERROR: Function does not take positional arguments.

Error present since Meson 0.60, which promoted from warning to error the use of positional arguments. One very common example of this error is to add invalid arguments to i18n.merge_file(). For instance,  had:

 i18n.merge_file(
   'sol.metainfo.xml',
   input: desktop_in,
   output: '@BASENAME@',
   type: 'desktop',
   po_dir: po_dir,
   install: true,
   install_dir: desktopdatadir,
 )

where  is the now invalid argument that should be removed. For the fix applied in the upstream, see this commit.

Measures to be taken in this case:

# Patch the meson.build reported in the error to fix the build, and the publish the updated PKGBUILD (if that is case)
# Contribute to the upstream repository with your patch, to fix it for everyone and to avoid having patches in the source array in the next versions.

## Template
To sum up the above instructions and to provide a single copy-and-paste point, see the template below:

{{bc|1=
makedepends=(meson)

build() {
  arch-meson $pkgname-$pkgver build
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

package() {
  meson install -C build --destdir "$pkgdir"
}
}}

## Example packages
This is a small list of packages that use Meson. See other packages in the list "Required by" in  package's page.

*
*
*
*
*
*
