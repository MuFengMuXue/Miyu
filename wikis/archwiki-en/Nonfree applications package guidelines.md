# Nonfree applications package guidelines

For many applications (most of which are Windows ones) there are neither sources nor tarballs available. Many of such applications can not be freely distributed because of license restrictions and/or lack of legal ways to obtain installer for no fee.

## Rationale
There are multiple reasons for packaging even non-packageable software:

* Simplification of installation/removal process
:This is applicable even to the simplest of applications, which consist of a single script to be installed into . Instead of issuing:
:
:you can just issue
:Most non-free applications are obviously much more complicated, but the burden of downloading an archive/installer from a homepage (often full of advertising), unpacking/decrypting it, hand-writing stereotypical launcher scripts and doing other similar tasks can be effectively lightened by a well-written packaging script.

* Utilizing pacman capabilities
:The ability to track state, perform automatic updates of any installed piece of software, determine ownership of every single file, and store compressed packages in a well-organized cache is what makes GNU/Linux distributions so powerful.

* Sharing code and knowledge
:It is simpler to apply tweaks, fix bugs and seek/provide help in a single public place like the AUR versus submitting patches to proprietary developers who may have ceased support or asking vague questions on general purpose forums.

## Common rules
## Avoid nonfree software when possible
Yes, it is better to leave this guide and spend some time searching (or maybe even creating) alternatives to an application you wanted to package because:

* It is better to support software that is owned by us all than software that is owned by a company
* It is better to support software that is actively maintained
* It is better to support software that can be fixed if just one person out of millions cares enough

## Use open source variants where possible
Many commercial games (some are listed in this Wiki) have open source engines and many old games can be played with emulators such as ScummVM. Using open source engines together with the original game assets gives users access to bug fixes and eliminates several issues caused by binary packages.

## Keep it simple
If the packaging of some program requires more effort and hacks than buying and using the original version, do the simplest thing—it is Arch!

## Package naming
Before naming a package, search the AUR for existing packages of software that you are packaging. Try to use established naming conventions, e.g. do not name your package gish-hb if there are existing packages called aquaria-hib, crayonphysicsdeluxe-hib and uplink-hib.
For non-free software, if the sources are not available, the  suffix should not be used. Existence of  suffixed package in the AUR means that there is the potential to have a corresponding package without  in the AUR or in Official Repositories.
There may be a seldom situation, when the non-free software suddenly opens their sources, and AUR package for that software did exist (which was building from binary deliverables). If this is the case, a user submitting a source-based package of the software would have to ask the maintainer of binary-based (existing) package to orphan it, so that their source-based package could be submitted, and the previous package then can be submitted as a  suffixed package.

## File placement
Again, analyze existing packages (if present) and decide whether or not you want to conflict with them. Do not place things under  unless you want to use some ugly hacks like giving ownership  to the package directory (so users in group  running the game can write files in the game's own folder).

## Missing files
For most commercial games there is no way to (legally) download game files, which is the preferable way to get them for normal packages. Even when it is possible to download files after providing a password (like with all Humble Indie Bundle games) asking user for this password and downloading somewhere in  function is not recommended for a variety of reasons (for example, the user may have no Internet access but have all files downloaded and stored locally).

The subsections below provide recommendations for a few situations you may encounter.

## Files can only be obtained in a distributed archive/installer
The software is only available via that archive/installer file, which must be obtained in order to get the missing files.

Add the required archive/installer to the  array, renaming the source filename so the source's link in the AUR web interface looks different from names of files included in the source tarball:

 source=(... "originalname::local://originalname")

Also add a pinned comment like the one below to the package page in the AUR, and explain the details in the PKGBUILD:

 Need archive/installer to work.

## Scheme to choose
In case you use the local:// scheme in a source array, makepkg behaves as though no scheme were specified, and the file must be manually placed in the same directory as the PKGBUILD.

In case you use the file:// scheme, you can additionally specify DLAGENTS for the file protocol, so it may be obtained in a special way. See examples below.

However, there are still no clear rules which of these schemes you should use.

## Files can only be obtained in an distributed compact-disk or other type of optical disk media
The software is only available via an optical disk media (e.g. CD, DVD, Bluray etc.), which must be inserted into the optical disk drive in order get the missing files.

Add an installer script and an  file to the package contents.

## Files can be obtained from several ways
Copying files from disk, downloading from Net or getting from archive during the  phase may look like a good idea but it is not recommended because it limits the user's possibilities and makes package installation interactive (which is generally discouraged and just annoying). Again, a good installer script and  file can work instead.

Few examples of various strategies for obtaining files required for package:

*  &ndash; dependency on user-provided file

## Advanced topics
## Custom DLAGENTS
Some software authors aggressively protect their software from automatic downloading: ban certain "User-Agent" strings, create temporary links to files etc. You can still conveniently download these files by using  variable in the PKGBUILD (see ). This is used by some packages in official repositories, for example in previous version of .

Please pay attention, if you want to have a customized user-agent string, if the latter contains spaces, parentheses, or slashes in it (or actually anything that can break parsing), this will not work. There is no workaround, this is the nature of arrays in bash and the way DLAGENTS was designed to be consumed in makepkg. The following example will thus not work:

 DLAGENTS=("http::/usr/bin/curl -A 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)' -fLC - --retry 3 --retry-delay 3 -o %o %u")

Shorten it to the following which is working:

 DLAGENTS=("http::/usr/bin/curl -A 'Mozilla' -fLC - --retry 3 --retry-delay 3 -o %o %u")

And the following allows to extract temporary link to file from download page:

 DLAGENTS=("http::/usr/bin/wget -r -np -nd -H %u")

In order to download temporary links to files or get past an interactive download, it is possible to analyze the HTTP request used to create the final download link, and then create a DLAGENTS that emulates this using curl. See for example  or .

Alternatively, the DLAGENTS can be used to provide a more informative error message to the user when a file is missing. See for example .

## Unpacking
Many proprietary programs are shipped in nasty installers which sometimes do not even run in Wine. The following tools may be of some help:

*  contains bsdtar, which can extract  images. It also provides bsdunzip which can be used in place of unzip.  is used for non-UTF-8 zip files.
** libarchive is required by pacman and so it is part of a base install.
*  files can be extracted by launching them with the  flag.
*  and  unpack executable SFX archives, based on these formats
*  can unpack most  files (including ones with  extension)
*  can extract CAB files from InstallShield installers
*  unpacks not only many archive formats but also NSIS-based  installers
** it even can extract single sections from common PE ( & ) files!
*  is sometimes used to compress above-listed executables and can be used for decompressing them as well
*  can unpack  installers created with Inno Setup (used for example by GOG.com games)
In order to determine exact type of file run .

## Getting icons for .desktop files
Proprietary software often have no separate icon files, so there is nothing to use in .desktop file creation. Fortunately,  files can be easily extracted from executables using programs from the  package. You can even do it on the fly during the  phase, for example:

 $ wrestool -x --output=icon.ico -t14 executable.exe

## Auto-bumping your pkgver
Non-free software vendors often don’t include a version number in their download source URL:

 source=('https://downloads.example.com/NonFreePackageWithPoorFileName.exe')

That will likely cause the release upstream package to change without notice, which is an issue for packaging. Just like in VCS packages, you may want to auto-bump your  to handle that.

## From the installer package
For example, some .exe installers have the Product Version field set in their PE. The peres command from the  package may help you extract and use that value to auto-bump your :

{{bc|
pkgver=VERSION
makedepends=('readpe')

pkgver() {
  peres -v -f csv "${srcdir}/NonFreePackageWithPoorFileName.exe" \
    | awk -F , '/^Product Version,/ { print $2 }'
}
}}

## From the main executable
Sometimes the .exe installer doesn’t carry a meaningful value for Product Version but the main executable does. In that case, you can use the  step to extract the nested main executable (see Unpacking for details) and then auto-bump the :

For example:

{{bc|
pkgver=VERSION
makedepends=('p7zip' 'pev')

prepare() {
  mkdir -p "${srcdir}/${pkgname}-unpacked"
  7z x -o"${srcdir}/${pkgname}-unpacked" "${srcdir}/NonFreePackageWithPoorFileName.exe"
}

pkgver() {
  peres -v -f csv "${srcdir}/${pkgname}-unpacked/NonFreeApp.exe" \
    | awk -F , '/^Product Version,/ { print $2 }'
}
}}

## From a Debian (.deb) file
Sometimes a .deb file doesn’t have a version number in its name but in its control file.

You can use  to extract the version directly from the control file inside the .deb package:

{{bc|
pkgver=VERSION
makedepends=('dpkg')
source=('https://example.com/vendor/nonfree-app-latest.deb')

pkgver() {
  # shellcheck disable=SC2016
  dpkg-deb --show --showformat='${Version}' nonfree-app-latest.deb | tr - .
}
}}
