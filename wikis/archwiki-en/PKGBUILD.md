# PKGBUILD

This article discusses variables definable by the maintainer in a . For information on the  functions and creating packages in general, refer to Creating packages. Also read .

A  is a Bash script containing the build information required by Arch Linux packages.

Packages in Arch Linux are built using the makepkg utility. When makepkg is run, it searches for a  file in the current directory and follows the instructions therein to either compile or otherwise acquire the files to build a package archive—. The resulting package contains binary files and installation instructions, readily installable with pacman.

Mandatory variables are , , , and .  is not strictly necessary to build a package, but is recommended for any  shared with others, as makepkg will produce a warning if not present.

It is a common practice to define the variables in the  in the same order as given here. However, it is not mandatory.

See the .proto files in the  directory as examples.

## Package name
## pkgbase
When building regular packages, this variable should not be explicitly declared in the : its value defaults to that of #pkgname.

When building a split package, this variable can be used to explicitly specify the name to be used to refer to the group of packages in the output of makepkg and in the naming of source-only tarballs. The value is not allowed to begin with a hyphen. If not specified, the value will default to the first element in the  array.

All options and directives for split packages default to the global values given in the . Nevertheless, the following ones can be overridden within each split package’s packaging function: #pkgdesc, #arch, #url, #license, #groups, #depends, #optdepends, #provides, #conflicts, #replaces, #backup, #options, #install, and #changelog.

## pkgname
Either the name of the package, e.g. , or, for split packages, an array of names, e.g. . Package names should only consist of lowercase alphanumerics and the following characters:  (at symbol, dot, underscore, plus, hyphen). Names are not allowed to start with hyphens or dots. For the sake of consistency,  should match the name of the source tarball of the software: for instance, if the software is in , use .

## Version
## pkgver
The version of the package.

This should be the same as the version published by the author of the upstream software. It can contain letters, numbers, periods and underscores, but not a hyphen (). If the author of the software uses one, replace it with an underscore (). If the  variable is used later in the , then the underscore can easily be substituted for a hyphen, e.g. {{ic|1=source=("${pkgname}-${pkgver//_/-}.tar.gz")}}.

See also Arch package guidelines#Package versioning.

## pkgrel
The release number. This is usually a positive integer number that allows to differentiate between consecutive builds of the same version of a package. As fixes and additional features are added to the  that influence the resulting package, the  should be incremented by 1. When a new version of the software is released, this value must be reset to 1. In exceptional cases other formats can be found in use, such as major.minor.

See also Arch package guidelines#Package versioning.

## epoch
Used to force the package to be seen as newer than any previous version with a lower epoch. This value is required to be a non-negative integer; the default is 0. It is used when the version numbering scheme of a package changes (or is alphanumeric), breaking normal version comparison logic. For example:

See  for more information on version comparisons.

## Generic
## pkgdesc
The description of the package. This is recommended to be 80 characters or less and should not include the package name in a self-referencing way, unless the application name differs from the package name. For example, use  instead of .

Also it is important to use keywords wisely to increase the chances of appearing in relevant search queries.

## arch
An array of architectures that the  is intended to build and work on. Arch officially supports only , but other projects may support other architectures. For example, Arch Linux 32 provides support for  and , and Arch Linux ARM provides support for  (armv7 hardfloat) and  (armv8 64-bit).

There are two types of values the array can use:

*  indicates the package can be built on any architecture, and once built, is architecture-independent in its compiled state (usually shell scripts, fonts, themes, many types of extensions, Java programs, etc.).
*  with one or more architectures (but not ) indicates the package can be compiled for any of the specified architectures, but is architecture-specific once compiled. For these packages, specify all architectures that the  officially supports. For official repository and AUR packages, this means . Optionally, AUR packages may choose to additionally support other known working architectures.

The target architecture can be accessed with the variable  during a build.

## url
The URL of the official site of the software being packaged.

## license
The license under which the software is distributed. Arch Linux uses SPDX license identifiers. Each license must have a corresponding entry in .

For common licenses (like ), package  delivers all the corresponding files. The package is installed by default, as it is a dependency of  meta package, and the files may be found in . Simply refer to the license using its SPDX license identifier from the list of SPDX identifiers.

License families like BSD or MIT are, strictly speaking, not a single license and each instance requires a separate license file. In  variable refer to them using a common SPDX identifier (e.g.  or ), but then provide the corresponding file as if it was a custom license.

For custom licenses the identifier should be either  or , if they are not covered by the common families mentioned above. The corresponding license text must be placed in directory . To install the file a following code snippet may be used in  section:

 install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"

Combining multiple licenses or adding exceptions should follow the SPDX syntax. For example a package released under either GNU/GPL 2.0 or GNU/LGPL 2.1 could use , a package released under Apache 2.0 with LLVM exception would use  and a package released with part under the BSD 3 clause, others under GNU/LGPL 2.1 and some under GNU/GPL 2.0 would use Note that this must be a single string, so the entire expression has to be enclosed in quotes. As for November 2023 [https://spdx.org/licenses/preview/exceptions-index.html SPDX list of exceptions is limited, so usually the custom license route must be used.

If issues are encountered with SPDX identifiers, during the transitional period using old identifiers —names of the directories in — is acceptable.

See also Nonfree applications package guidelines.

Additional information and perspectives on free and open source software licenses may be found on the following pages:

* Wikipedia:Free software license
* Wikipedia:Comparison of free and open-source software licenses
* A Legal Issues Primer for Open Source and Free Software Projects
* GNU Project - Various Licenses and Comments about Them
* Debian - License information
* Open Source Initiative - Licenses by Name

## groups
The group the package belongs in. For instance, when installing , it installs all packages belonging in that group.

## Dependencies
## depends
An array of packages that must be installed for the software to build and run. Dependencies defined inside the  function are only required to run the software.

Version restrictions can be specified with comparison operators, e.g. ; if multiple restrictions are needed, the dependency can be repeated for each, e.g. ; e.g. {{ic|source=("${pkgname}-${pkgver}.tar.gz::https://github.com/coder/program/archive/v${pkgver}.tar.gz")}}.
}}

{{Tip|
* Additional architecture-specific arrays can be added by appending an underscore and the architecture name, e.g. . There must be a corresponding integrity array with checksums, e.g. .
* Some servers restrict download by filtering the User-Agent string of the client or other types of restrictions, which can be circumvented with DLAGENTS.
* Use  URL to point to a directory or a file in your computer filesystem. For example, a local Git repository can be specified as {{ic|"${pkgname}::git+file:///path/to/repository"}}.
* Magnet link support can be added using  as  and using the  URI prefix instead of the canonical .
* See  and VCS package guidelines#VCS sources for details on VCS specific options, such as targeting a specific Git branch or commit.
}}

## noextract
An array of files listed under , which should not be extracted from their archive format by makepkg. This can be used with archives that cannot be handled by  or those that need to be installed as-is. If an alternative unarchiving tool is used (e.g. ), it should be added in the  array and the first line of the prepare() function should extract the source archive manually; for example:

 prepare() {
   lrzip -d source.tar.lrz
 }

Note that while the  array accepts URLs,  is just the file name portion:

 source=("http://foo.org/bar/foobar.tar.xz")
 noextract=('foobar.tar.xz')

To extract nothing, consider the following:

* If  contains only plain URLs without custom file names, strip the  array before the last slash:
: {{bc|1=noextract=("${source* If  contains only entries with custom file names, strip the  array after the  separator (taken from a previous version of [https://gitlab.archlinux.org/archlinux/packaging/packages/firefox-i18n/-/blob/46492498ef720353cbb84de5096102de694faf90/PKGBUILD#L132 firefox-i18n's PKGBUILD):
: {{bc|1=noextract=("${source@%%::*}")}}

## validpgpkeys
An array of PGP fingerprints. If used, makepkg will only accept signatures from the keys listed here and will ignore the trust values from the keyring. If the source file was signed with a subkey, makepkg will still use the primary key for comparison.

Only full fingerprints are accepted. They must be uppercase and must not contain whitespace characters.

Please read makepkg#Signature checking for more information.

## Integrity
These variables are arrays whose items are checksum strings that will be used to verify the integrity of the respective files in the source array. Insert  for a particular file, and its checksum will not be tested.

The checksum type and values should always be those provided by upstream, such as in release announcements. When multiple types are available, the strongest checksum is to be preferred (in order from most to least preferred): , , , , , , , . This best ensures the integrity of the downloaded files, from upstream announcement to package building.

The values for these variables can be auto-generated by makepkg's / option, then commonly appended with . The  command from  is able to update the variables wherever they are in the . Both tools will use the variable that is already set in the , or fall back to  if none is set.

The file integrity checks to use can be set up with the  option in . See .

## b2sums
An array of BLAKE2b checksums with digest size of 512 bits.

## sha512sums, sha384sums, sha256sums, sha224sums
An array of SHA-2 checksums with digest sizes 512, 384, 256 and 224 bits, respectively.  is the most common of them.

## sha1sums
An array of 160-bit SHA-1 checksums of the files listed in the  array.

## md5sums
An array of 128-bit MD5 checksums of the files listed in the  array.

## cksums
An array CRC32 checksums (from UNIX-standard cksum) of the files listed in the  array.
