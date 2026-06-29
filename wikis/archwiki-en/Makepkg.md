# Makepkg

makepkg is a script to automate the building of packages. The requirements for using the script are a build-capable Unix platform and a PKGBUILD.

makepkg is provided by the  package.

## Configuration
The system configuration is available in , but user-specific changes can be made in  or . Also, system wide changes can be made with a drop-in file . It is recommended to review the configuration prior to building packages.

See  for more information.

## Packager information
Each package is tagged with metadata identifying amongst others also the packager. By default, user-compiled packages are marked with . If multiple users will be compiling packages on a system, or if one is otherwise distributing packages to other users, it is convenient to provide real contact. This can be done by setting the  variable in .

To check this on an installed package:

To automatically produce signed packages, also set the  variable in .

## Package output
By default, makepkg creates the package tarballs in the working directory and downloads source data directly to the  directory. Custom paths can be configured, for example to keep all built packages in  and all sources in .

Configure the following  variables if needed:

*  — directory for storing resulting packages
*  — directory for storing source data (symbolic links will be placed to  if it points elsewhere)
*  — directory for storing resulting source packages (built with )

You can also use relative paths inside each package directory.

## Signature checking
If a signature file in the form of .sig or .asc is part of the PKGBUILD source array, makepkg automatically attempts to verify it. In case the user's keyring does not contain the needed public key for signature verification, makepkg will abort the installation with a message that the PGP key could not be verified.

If a needed public key for a package is missing, the PKGBUILD will most likely contain a validpgpkeys entry with the required key IDs. Import it manually, or find it on a keyserver and import it from there. To temporarily disable signature checking, run makepkg  with the  option.

## Usage
Before continuing, install the  meta package. Dependencies of this package are not required to be listed as build-time dependencies (makedepends) in PKGBUILD files.

To build a package, one must first create a PKGBUILD, or build script, as described in Creating packages. Existing scripts are available from the Arch build system (ABS) tree or the AUR. Once in possession of a , change to the directory where it is saved and run the following command to build the package:

 $ makepkg

If required dependencies are missing, makepkg will issue a warning before failing. To build the package and install needed dependencies, add the flag /:

 $ makepkg --syncdeps

Adding the / flag causes makepkg to remove the make dependencies later, which are no longer needed. If constantly building packages, consider using Pacman/Tips and tricks#Removing unused packages (orphans) once in a while instead.

Once all dependencies are satisfied and the package builds successfully, a package file () will be created in the working directory. To install, use / (same as ):

 $ makepkg --install

To clean up leftover files and directories, such as files extracted to the , add the option /. This is useful for multiple builds of the same package or updating the package version, while using the same build directory. It prevents obsolete and remnant files from carrying over to the new builds:

 $ makepkg --clean

For more, see .

## Optimization
The default options match the options  uses to build packages for the official repositories.As such, end users may realize more or less significant gains by tweaking the following options to match their local environment.

## Building optimized binaries
A performance improvement of the packaged software can be achieved by enabling compiler optimizations for the host machine. The downside is that binaries compiled for a specific processor architecture will not run correctly on other machines. On x86_64 machines, there are rarely significant enough real world performance gains that would warrant investing the time to rebuild official packages.

However, it is very easy to reduce performance by using "nonstandard" compiler flags. Many compiler optimizations are only useful in certain situations and should not be indiscriminately applied to every package. Unless benchmark data are available to prove that something is faster, there is a very good chance it is not! The Gentoo GCC optimization and Safe CFLAGS wiki articles provide more in-depth information about compiler optimization.

## C and C++
The options passed to a C/C++ compiler (e.g.  or ) are controlled by the , , and  environment variables. For use in the Arch build system, makepkg exposes these environment variables as configuration options in . The default values are configured to produce generic binaries that can be installed on a wide range of machines.

GCC can automatically detect and enable safe architecture-specific optimizations. To use this feature, first remove any  and  flags, then add . For example:

{{hc|/etc/makepkg.conf|2=
CFLAGS="-march=native -O2 -pipe ..."
CXXFLAGS="${CFLAGS} ..."
}}

To see what flags this enables, run:

 $ gcc -march=native -v -Q --help=target

Further optimization of binaries can be achieved by enabling optimizations that are considered expensive in terms of memory usage and compile time. This can be achieved by changing the optimization level flag from  to . Using this flag will in most cases improve performance of the binary, although this is not guaranteed and in some cases [https://discourse.ubuntu.com/t/benchmarking-a-distribution-and-some-o3-results/58027 can prove counter-productive. See Gentoo:GCC optimization#-O and GCC optimization options page for details.

## Rust
Starting in  version 5.2.2,  also includes overrides for the  environment variable, for flags given to the Rust compiler. The Rust compiler can also detect and enable architecture-specific optimizations by adding  to the given  value:

To see which CPU features this will enable, run:

 $ rustc -C target-cpu=native --print cfg

Running  without  will print the default configuration.

Additional optimization-related options that may be added to :

* : The value can be changed to , , or  as desired.  is default of release build.
* : Choosing  less than  also optimizes binary, but it increases build time.
*  reduces size of the binary.

See the Rust compiler's documentation for details.

## Improving build times
## Parallel compilation
The  build system uses the  environment variable to specify additional options for make. The variable can also be set in the  file.

Users with multi-core/multi-processor systems can specify the number of jobs to run simultaneously. This can be accomplished with the use of  to determine the number of available processors, e.g. .

Some s specifically override this with , because of race conditions in certain versions or simply because it is not supported in the first place. Packages that fail to build because of this should be reported on the bug tracker (or in the case of AUR packages, to the package maintainer) after making sure that the error is indeed being caused by .

See  for a complete list of available options.

## Building from files in memory
As compiling requires many I/O operations and handling of small files, moving the working directory to a tmpfs may bring improvements in build times.

The  variable can be temporarily exported to makepkg to set the build directory to an existing tmpfs. For example:

 $ BUILDDIR=/tmp/makepkg makepkg

Persistent configuration can be done in  by uncommenting the  option, which is found at the end of the  section in the default  file. Setting its value to e.g.  will make use of the Arch's default  temporary file system.

## Using a compilation cache
The use of ccache can improve build times by caching the results of compilations for successive use.

## Using mold linker
 is a drop-in replacement for ld/lld linkers, which claims to be significantly faster.

To use mold, append  to . For example:

To pass extra options to mold, additionally add those to . For example:

To use mold for Rust packages, append  to . For example:

## Disable debug packages and LTO
Commit 90bf367e included in pacman 6.0.2-9 from February 2024 enabled the  and  options by default.

Building debug packages enables the official repositories to provide more tools to troubleshoot issues for users (), but it is not required when building packages on your own and slows down the build process. See .

Link-time optimization produces more optimized binaries but greatly lengthens the build process (), which might not be a desired tradeoff.

To disable those options, add a  character directly in front of them in the  array, e.g. .

## Compression
## Use other compression algorithms
To speed up both packaging and installation, with the tradeoff of having larger package archives, change .

For example, the following skips compression of the package file, which will in turn have no need to be decompressed on install:

 $ PKGEXT='.pkg.tar' makepkg

As another example, the following uses the LZ4 algorithm, which is focused on speed:

 $ PKGEXT='.pkg.tar.lz4' makepkg

To make one of these settings permanent, set  in .

## Utilizing multiple cores on compression
 supports symmetric multiprocessing (SMP) via the / flag to speed up compression. The  flag is included by default in the  array in , which lets zstd use as many threads as there are physical CPU cores to compress packages. The number of used threads can be further increased by instructing zstd to base it on the logical CPU count using the  flag:

 COMPRESSZST=(zstd -c -T0 --auto-threads=logical -)

 and  are multithreaded by default, so nothing needs to be changed in .

 is a drop-in, parallel implementation for  which by default uses all available CPU cores (the / flag can be used to employ less cores):

 COMPRESSGZ=(pigz -c -f -n)

 is a drop-in, parallel implementation for  which also uses all available CPU cores by default. The  flag can be used to employ less cores (note: no space between the  and number of cores).

 COMPRESSBZ2=(pbzip2 -c -f)

 is another drop-in, parallel implementation for  which also uses all available CPU cores by default. The  flag can be used to employ less cores.

 COMPRESSBZ2=(lbzip2 -c -f)

 is a multithreaded implementation for  which also uses all available CPU cores by default. The / flag can be used to employ less cores.

 COMPRESSLZ=(plzip -c -f)

## Changing compression level
Several compression algorithms (including zstd and xz) support setting a compression level which defines a tradeoff between speed, memory and compression efficiency.

## Tips and tricks
## Reduce source download and extraction times
## Defining the sources location
Make use of , especially when building VCS packages, to save time acquiring and unpacking sources in subsequent rebuilds.

## Custom DLAGENTS
You can use a downloader supporting parallel downloading, e.g. :

See also Nonfree applications package guidelines#Custom DLAGENTS.

## Generate new checksums
Install  and run the following command in the same directory as the PKGBUILD file to generate new checksums:

 $ updpkgsums

 uses  to generate the checksums. See this forum discussion for more details.

The checksums can also be obtained with e.g  and added to the  array by hand.

## Build from local source files
If you want to make changes to the source code you can download the source code without building the package by using the -o, --nobuild    Download and extract files only option.

 $ makepkg -o

You can now make changes to the sources and then build the package by using the -e, --noextract  Do not extract source files (use existing $srcdir/ dir) option. Use the -f option to overwrite already built and existing packages.

 $ makepkg -ef

## Show packages with specific packager
 is a pacman database extraction utility. This command shows all packages installed on the system with the packager named packagername:

 $ expac "%n %p" | grep "packagername" | column -t

This shows all packages installed on the system with the packager set in the  variable . This shows only packages that are in a repository defined in .

 $ . /etc/makepkg.conf; grep -xvFf <(pacman -Qqm) <(expac "%n\t%p" | grep "$PACKAGER$" | cut -f1)

## Build 32-bit packages on a 64-bit system
See 32-bit package guidelines.

## Unattended package signing
A person may not be available to provide the passphrase for the gpg private key used to sign with in automated build environments such as Jenkins. It is ill-advised to store a private gpg key on a system without a passphrase.

A resulting zst package made with makepkg can still be signed after creation:

 $ gpg --detach-sign --pinentry-mode loopback --passphrase --passphrase-fd 0 --output NewlyBuilt.pkg.tar.zst.sig --sign NewlyBuilt.pkg.tar.zst

where the GPG passphrase is securely provided and obscured by your automation suite of choice.

The resulting  and  file can be referenced by pacman clients expecting a valid signature and repositories created with  when hosting your own repo.

## Magnet URIs
Support for magnet URIs resources (with  prefix) in the  field can be added using the  download agent.

## Running makepkg in a systemd control group
If the package you are building takes too many resources to build with your default make flags, which are otherwise set properly for most packages, you can try running it in its own control group.  is a wrapper for makepkg that achieved this via systemd control groups (see ).

## Running with idle scheduling policy
Package build process can lead to high CPU utilization, especially in case of #Parallel compilation. Under heavy CPU load, the system can issue a significant slowdown up to becoming unusable, even with the highest  value. User interface and foreground applications may stutter or even became unresponsive.

This can be worked around by changing the scheduling policy to  before running makepkg. It ensures that package building process does not interfere with regular tasks and only utilizes remaining unused CPU time.

From :

: This policy is intended for running jobs at extremely low priority (lower even than a +19 nice value with the  or  policies).

The  policy can be set by running  command with the  flag, specifying priority 0 (the only valid option for ) and specifying the PID of the current shell.

For most shells:

 $ chrt -iap 0 $$

For the fish shell, where  is not set:

 $ chrt -iap 0 %self

## Relative paths inside each package directory
Instead of using absolute paths for the package output options, you can also configure relative paths inside each package directory.

For example, you can define target paths in your  file as follows. The  variable refers to the directory where a  is located when you build a package.

 PKGDEST="$startdir/build/packages/"
 SRCDEST="$startdir/build/sources/"
 SRCPKGDEST="$startdir/build/srcpackages/"
 LOGDEST="$startdir/logs/"

This will result in:

* Built packages will be stored in:
* All downloaded source files will be stored in:
* Built source packages will be stored in:
* All logs will be stored in:

makepkg will still create  and  directories as usual, so this is expected behaviour.

## Troubleshooting
## Specifying install directory for QMAKE based packages
The makefile generated by qmake uses the environment variable  to specify where the program should be installed. Thus this package function should work:

{{hc|PKGBUILD|2=
...
package() {
	cd "$srcdir/${pkgname%-git}"
	make INSTALL_ROOT="$pkgdir" install
}
...
}}

Note, that qmake also has to be configured appropriately. For example put this in the corresponding .pro file:

## WARNING: Package contains reference to $srcdir
Somehow, the literal strings contained in the variables  or  ended up in one of the installed files in the package. To identify which files, run the following from the makepkg build directory:

 $ grep -R "$PWD/src" pkg/

One possible cause would be from the usage of  macro in C/C++ code with full path passed to compiler.

Dotnet binaries also sometimes contain full paths to the  files in the default config.

## Makepkg fails to download dependencies when behind proxy
When makepkg calls dependencies, it calls pacman to install the packages, which requires administrative privileges via sudo. However, sudo does not pass any environment variables to the privileged environment, and includes the proxy-related variables , , , and .

In order to have makepkg working behind a proxy, invoke one of the following methods.

## Enable proxy by setting its URL in XferCommand
The XferCommand can be set to use the desired proxy URL in .  Add or uncomment the following line in :

## Enable proxy via sudoer's env_keep
Alternatively, one may want to use sudoer's  option, which enables preserving given variables the privileged environment. See Pacman#pacman does not honor proxy settings for more details.

## Makepkg fails, but make succeeds
If something successfully compiles using make, but fails through makepkg, it is almost certainly because  sets an incompatible compilation variable.  Try adding these flags to the PKGBUILD  array:

, to prevent its default , , , and .

, to prevent its default .

, to prevent its default , and , in case the PKGBUILD is a debug build.

If any of these fix the problem, this could warrant an upstream bug report assuming the offending flag has been identified.
