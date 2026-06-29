# Arch package guidelines

When building packages for Arch Linux, adhere to the package guidelines below, especially if the intention is to contribute a new package to Arch Linux. You should also see the  and  man pages.

Important points listed on this page are not repeated on the other package guideline pages. These specific guidelines are intended as an addition to the standards listed below.

See .proto files in the  directory as PKGBUILD examples.

## Package etiquette
* Packages should never be installed to .

* Do not introduce new variables or functions into  build scripts, unless the package cannot be built without doing so, as these could possibly conflict with variables and functions used in makepkg itself.

* If a new variable or a new function is absolutely required, prefix its name with an underscore (), e.g.

* Avoid using  for anything. Use  instead.

* The  field from the package meta file can be customized by the package builder by modifying the appropriate option in the  file, or alternatively override it by creating .

* Do not use makepkg subroutines (e.g. , , , , ) as they might change at any time. To print data, use  or .

* All important messages should be echoed during install using an .install file. For example, if a package needs extra setup to work, directions should be included.

* Dependencies are the most common packaging error. Please take the time to verify them carefully, for example by running ,  and  on dynamic executables, checking tools required by scripts or looking at the documentation of the software. The namcap utility can help you in this regard. This tool can analyze both the  file and the resulting package tarball and will warn you about bad permissions, missing dependencies, redundant dependencies, and other common mistakes.

* Any optional dependencies that are not needed to run the package or have it generally function should not be included in the depends array; instead the information should be added to the optdepends array:
:
:The above example is taken from the  package. The optdepends information is automatically printed out on installation/upgrade so one should not keep this kind of information in  files.

* When creating a package description for a package, do not include the package name in a self-referencing way.  For example, "Nedit is a text editor for X11" could be simplified to "A text editor for X11".  Also try to keep the descriptions to ~80 characters or less.

* Try to keep the line length in the  file below ~100 characters.

* Where possible, remove empty lines from the  (, , etc.)

* It is common practice to preserve the order of the  fields in the same order as given in the PKGBUILD article. However, this is not mandatory, as the only requirement in this context is correct Bash syntax.

* Quote variables which may contain spaces, such as  and .

* To ensure the integrity of packages, make sure that the integrity variables contain correct values. These can be updated using the  tool.

## Package naming
* Package names can contain only alphanumeric characters and any of , , , , . Names are not allowed to start with hyphens or dots. All letters should be lowercase.
* Package names should not be suffixed with the upstream major release version number (e.g. we do not want libfoo2 if upstream calls it libfoo v2.3.4) in case the library and its dependencies are expected to be able to keep using the most recent library version with each respective upstream release. However, for some software or dependencies, this can not be assumed. In the past this has been especially true for widget toolkits such as GTK and Qt. Software that depends on such toolkits can usually not be trivially ported to a new major version. As such, in cases where software can not trivially keep rolling alongside its dependencies, package names should carry the major version suffix (e.g. gtk2, gtk3, qt4, qt5). For cases where most dependencies can keep rolling along the newest release but some cannot (for instance closed source that needs libpng12 or similar), a deprecated version of that package might be called libfoo1 while the current version is just libfoo.

## Package versioning
* Package version —  — should be the same as the version released by the author.
* Versions can include letters if need be, e.g. version could be .
* Version tags may not include hyphens, and may contain letters, numbers, and periods only. If the upstream version contains a hyphen, it must be replaced with an underscore.

* Package releases —  — are specific to Arch Linux packages. These allow users to differentiate between newer and older package builds. When a new package version is first released, the release count starts at 1. Then as fixes and optimizations are made, the package will be re-released to the Arch Linux public and the release number will increment.
* When a new version comes out, the release count resets to 1.
* Package release tags follow the same naming restrictions as version tags.

## Package dependencies
* Do not rely on transitive dependencies in any of the PKGBUILD#Dependencies, as they might break, if one of the dependencies is updated.
* List all direct library dependencies. To identify them  (part of ) can be used.

## Package relations
* Do not add  to PKGBUILD#provides, as it is always implicitly provided by the package.
* Do not add  to PKGBUILD#conflicts, as a package cannot conflict with itself.
* List all external shared libraries of a package in PKGBUILD#provides (e.g. ). To identify them  (part of ) can be used.

## Package sources
* HTTPS sources ( for tarballs,  for git sources) should be used wherever possible
* Sources should be verified using PGP signatures wherever possible (this might entail building from a git tag instead of a source tarball, if upstream signs commits and tags but not the tarballs)

* When building from a git tag, use its object hash obtained from  instead of the tag name:
:{{bc|
_tag=1234567890123456789012345678901234567890 # git rev-parse "v$pkgver"
source=(git+https://$url.git?signed#tag=$_tag)

pkgver() {
    cd "$pkgname"
    git describe
}
}}
:An example for this approach can be found in the  package. The reason for this practice is that tags can be force pushed to change the commit that they are pointing to, which would alter the built package. Using the tag object hash ensures the integrity of the sources because force pushing the tag changes its hash. Using a  function prevents accidentally bumping  without updating  as well.  See VCS package guidelines#VCS sources for more info on the formatting of VCS sources.
* Do not diminish the security or validity of a package (e.g. by removing a checksum check or by removing PGP signature verification), because an upstream release is broken or suddenly lacks a certain feature (e.g. PGP signature missing for a new release)
* Sources have to be unique in  (this might require renaming them when downloading, e.g. {{ic|"${pkgname}-${pkgver}.tar.gz::https://${pkgname}.tld/download/${pkgver}.tar.gz"}})
* Avoid using specific mirrors (e.g. on sourceforge) to download, as they might become unavailable
* Git objects (e.g., tags, commits, etc.) signed by an SSH key can be verified using a git command with  pointing to a file specifying possible signing keys. See for an example.

## Working with upstream
It is considered best-practice to work closely with upstream wherever possible. This entails reporting problems about building and testing a package.

* Report problems to upstream right away.
* Upstream patches wherever possible.
* Add comments with links to relevant (upstream) bug tracker tickets in the PKGBUILD (this is particularly important, as it ensures, that other packagers can understand changes and work with a package as well).

It is recommended to track upstream with tools such as ,  or  to be informed about new stable releases.

## Directories
* Configuration files should be placed in the  directory. If there is more than one configuration file, it is customary to use a subdirectory in order to keep the  area as clean as possible. Use   where  is the name of the package (or a suitable alternative, eg, apache uses ).
* Package files should follow these general directory guidelines:

:{| class="wikitable"
|-
|
| System-essential configuration files
|-
|
| Binaries
|-
|
| Libraries
|-
|
| Header files
|-
|
| Modules, plugins, etc.
|-
|
| Application documentation
|-
|
| GNU Info system files
|-
|
| Application licenses
|-
|
| Manpages
|-
|
| Application data
|-
|
| Persistent application storage
|-
|
| Configuration files for pkg
|-
|
| Large self-contained packages
|}

* Packages should not contain any of the following directories:
**
**
**
**
**
**
**
**
**
**
**
**
**
**

## Makepkg duties
When makepkg is used to build a package, it does the following automatically:

# Checks if package dependencies and makedepends are installed
# Downloads source files from servers
# Checks the integrity of source files
# Unpacks source files
# Does any necessary patching
# Builds the software and installs it in a fake root
# Strips symbols from binaries
# Strips debugging symbols from libraries
# Compresses manual and/or info pages
# Generates the package meta file which is included with each package
# Compresses the fake root into the package file
# Stores the package file in the configured destination directory (i.e. the current working directory by default)

## Architectures
The  array should contain  if the compiled package is architecture-specific. Otherwise, use  for architecture independent packages.

## Licenses
There are two kinds of licenses regarding an Arch package:

## PKGBUILD's license field
The  field of a . It lists the packaged software's upstream license. It is NOT the license of the package source. The licenses in this field must be in the [https://spdx.org/licenses/ SPDX license format. See also PKGBUILD#license for more details.

## Package sources licenses
The license for the package sources themselves. In RFC40, Arch Linux specifies that package sources are to be licensed as BSD Zero Clause License () with RFC52 specifying that REUSE should be used to enforce this.

It boils down to this:

# Have a  file in the sources root with exactly this content. This is Arch Linux's  license for packages.
# Have a  in the sources root. You can use  to generate a reasonable config to get you started.
# Make sure to run  and that it returns no errors.

If you have additional files that you need to license, you need to pick a reasonable license for them. This is usually quite straight forward:

* If the file in question (for example, a launcher script  or a systemd service file ) was created entirely by you or other Arch staff, license it as .
* If the file was taken from upstream (for instance, an icon  or a patch ), then it should carry the upstream license.

See also the Arch Linux Dev blog post introducing .

## Reproducible builds
Arch is working on making all packages reproducible. A packager can check if a package is reproducible with  from  or  from .

 $ makerepropkg $pkgname-1-1-any.pkg.tar.zst

Or

 $ repro -f $pkgname-1-1-any.pkg.tar.zst

If the timestamp is required at build-time, use the environment variable . The format is documented upstream.
