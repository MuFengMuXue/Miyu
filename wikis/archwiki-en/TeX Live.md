# TeX Live

According to Wikipedia:

:TeX Live is a free software distribution for the TeX typesetting system that includes major TeX-related programs, macro packages, and fonts.

TeX Live includes:

* many TeX engines, such as:
** pdfTeX
**XeTeX
**LuaTeX
* basic macro packages (called formats in TeX parlance), such as:
** LaTeX
** ConTeXt
* many user-produced packages

Alternatives to TeX Live include MikTex and Tectonic, they come with a minimal install, downloading the necessary packages on the go.

## Arch-packaged TeX Live vs native TeX Live
There are multiple ways to install TeX Live. While a snapshot of TeX Live should be available from the Arch Linux package repositories (as described below), that snapshot is in most cases updated only once a year. In contrast, TeX Live itself is a rolling release distribution, based on the model of the user having to upgrade once a year, but with individual package upgrades available on a sub-daily basis.

The advantages of having a native and up-to-date TeX Live installation include having access to the latest features and bug fixes and to the relevant documentation. While it is possible to upgrade or install an individual package without having native TeX Live (see  and ), this requires extra care - it is necessary to ensure that the versions of all relevant packages are mutually compatible.

## Native TeX Live
## Installation
See the quickinstall documentation, and, if necessary, the full documentation. The process boils down to:

# downloading the netinstall archive
# unpacking the archive and changing to the newly created directory
# running the install script, , which starts an interactive installation procedure within a text interface
## setting the wanted installation path or paths
## optionally, choosing a subset of the package collections provided by TeX Live
## optionally, choosing the Letter paper size as the default, as opposed to A4
## waiting for everything to download
# As the install script will notify you at the end of the process, it's necessary to add the TeX Live installation to the system executable and documentation paths: , , . The install script prints the exact additions that are required before exiting.

Or, alternatively, install the  package and run  while following above procedure.

## Updating
See the tlmgr documentation,  upgrades all packages from the collections chosen during the installation. It will also install any packages that are newly added to an installed TeX Live collection.

Once a year, when there's a new TeX Live release,  will fail and it will be necessary to install TeX Live anew.

## Arch-packaged TeX Live
* The  group contains most TeX Live packages, categorised based on upstream collections (see ** , the core installation, based on the medium upstream install scheme. The package includes pacman hooks to automate mktexlsr, fmtutil and updmap.
**  contains essential LaTeX packages. (For instance, if you intend to use , then you need this package).
**  and  contain many useful LaTeX packages, such as ,  and .
**  contains essential fonts (including the default Latin Modern)
**  contains additional fonts, which can be viewed on the [https://www.tug.org/FontCatalogue/ LaTeX Font Catalogue.
**  and  contain packages for XeTeX and LuaTeX respectively.
**  contains the BibLaTeX package and additional BibTeX styles and bibliography databases.
**  contains essential packages for mathematics, natural sciences and computer science.
**  contains packages for producing graphics, pictures and diagrams
* The  group contains packages providing character sets and features for languages with non-Latin characters.
*  provides an alternative bibliography processing backend for BibLaTeX.

Note that some tools in  have optional dependencies which are not automatically installed. For example, latexindent depends on  and .

Whenever there is a need to install a TeX package available on CTAN, run the following to determine whether it is included in an Arch texlive- package:

 $ tlmgr info ctan_package_name | grep collection

This will potentially list the name of a TeX Live collection which corresponds to an Arch texlive- package (also check the  group to confirm whether such package exists). For instance, an output of  means that TeX package is included in .

Alternatively,  can be used to manually install a single TeX package (see below).

## tllocalmgr
The tllocalmgr utility, provided by , lets you install (and update) packages from CTAN as pacman packages. See its usage () for details.

## tlmgr
With , the  utility should work out of the box.
By default, it requires root privileges to run:

 # tlmgr install package_name

If you want to run it without root privileges, use the built-in user mode feature.
This installs the CTAN packages to  by default.
 must first initialise this directory.
To do this, run:

 $ tlmgr init-usertree

Now, you can use user mode:

 $ tlmgr --usermode install package_name

To change the package install location, change the  environment variable.

 $ export TEXMFHOME="$HOME/.local/texmf"
 $ tlmgr init-usertree
 $ ...

 will guess a good mirror on its own.
If you want, though, you can explicitly set your preferred mirror.
You need to append  to the path of the mirror.
For example:

 $ tlmgr option repository http://mirrors.rit.edu/CTAN/systems/texlive/tlnet

## Package documentation
The packages in the official repositories do not contain the documentation or source files of font/macro packages.

For offline access with , install the whole TeX Live documentation and source files with .

You can also access the documentation online at:

* https://tug.org/texlive/Contents/live/doc.html
* https://ctan.org/ – the central place for all kinds of material around TeX
* https://texdoc.org/ ( directly yields the relevant PDF)

## Usage
See the following resources:

* Wikibooks:LaTeX
* The Not So Short In­tro­duc­tion to LaTeX 2ε
* Getting to Grips with LaTeX – Andrew Roberts
* The TeX FAQ

Some use a TeX editor for creating documents.

## High-level wrappers for compiling documents
It almost always makes more sense to use a higher-level automation tool such as  (used by Overleaf or , instead of calling things like  directly, mostly because lower-level tools need to be run multiple times in general for completely compiling a single document.

## texmf trees and Kpathsea
texmf trees (texmf stands for TeX and Metafont) should follow the [https://tug.org/tds/ TeX Directory Structure, or files may not be found.TeX Live uses the [https://tug.org/texinfohtml/kpathsea.html Kpathsea library to lookup paths by filename across multiple texmf trees and the current working directory.

Kpathsea searches the following variables in the reverse order (later trees override earlier ones).

{| class="wikitable"
! Variables !! Arch default 1) !! Used by |-
|  ||  ||  files of the original distribution
|-
|  ||  || administrators for system-wide installation of additional or updated macros, fonts, etc.
|-
|  ||  ||  updmap and fmtutil (user mode) to store (cached) runtime data
|-
|  ||  || updmap and fmtutil (user mode) to store modified configuration data
|-
|  ||  || users for their own individual installations of additional or updated macros, fonts, etc.
|-
|  ||  || updmap and fmtutil (sys mode) to store (cached) runtime data
|-
|  ||  || updmap and fmtutil (sys mode) to store modified configuration data
|-
|  ||  || ConTeXt MkIV and LuaLaTeX to store (cached) runtime data
|}

Kpathsea provides the  command to lookup paths. When run with the  argument it can also print the values of variables.

Kpathsea uses filename databases () to speed up searches in system-wide texmf trees (configured with the  variable). This means that when system-wide file trees are changed,  or  (a symlink) need to be run as root. Fortunately the  automates this with a pacman hook targeting all default system-wide texmf trees but .[https://gitlab.archlinux.org/archlinux/packaging/packages/texlive-texmf/-/blob/main/70-mktexlsr.hook So as long as you install system-wide packages via pacman you should not need to run mktexlsr or texhash at all.

{{Tip|For setting up a local repository you can create the {{ic|~/texmf/tex/{format}/}} directory structure ({{ic|{format} }} is usually ), where custom classes are located in the root of the {{ic|./{format} }} folder and other local files get placed in a folder with the same name (e.g.  goes to {{ic|./{formats}/mycustompackage/mycustompackage.sty}}), then run  to update the user database.}}

## Tips and tricks
## Changing default paper size
It is currently impossible to set the default page size using the texlive tools, because they do not work with the standard Arch package.

Usually, you would run  or , which are also capable of changing other useful settings.

You can edit the configuration files as follows.

* To set the paper size for the pdftex family of commands (pdftex, pdflatex, etc) edit  file.

which can also be discovered by running . Change the two lines that specify the  and . For example, to use letter size, change

 \pdfpageheight = 297 true mm
 \pdfpagewidth  = 210 true mm

to

 \pdfpageheight = 11 true in
 \pdfpagewidth  = 8.5 true in

Unfortunately, this will not have any effect until the binary .fmt files are rebuilt.  You can do this with . Re-installing  with pacman will also do this for you.

* For dvips, you can use the  option to specify the paper size: . To change the default, edit  file.

which can also be discovered with . The end of this file has sections that list all the paper sizes that dvips knows about.  The first listed paper size will be the default. Just move the one that you want to be the default to the top of the list. The behavior of dvips will be affected as soon as the file file is changed.

## Making fonts available to Fontconfig
By default, the fonts that come with the various TeX Live packages are not automatically available to Fontconfig. If you want to use them with, say XeTeX or LibreOffice, the easiest approach is to create a symlink in the font directory to a subdirectory in your user's font path. Run the following for an OpenType font:

 $ ln -s /usr/share/texmf-dist/fonts/opentype/public/some_fonts_you_want ~/font_path/OTF/

To make them available to fontconfig, run:

 $ fc-cache ~/font_path
 $ mkfontscale ~/font_path/OTF
 $ mkfontdir ~/font_path/OTF

Similar steps follow for TrueType fonts and Type 1 fonts. In the lines above, substitute  with  or  and substitute  with  or .

Alternatively,  contains the file  that contains a list of the font directories used by TeX Live. You can use this file with:

And then update fontconfig:

## Updating babelbib language definitions
If you have the very specific problem of babelbib not having the latest language definitions that you need, and you do not want to recompile everything, you can get them manually from https://www.tug.org/texlive/devsrc/Master/texmf-dist/tex/latex/babelbib/ and put them in . For example:

Afterwards, you need to run  to update the TeX database:

 # texhash

## Troubleshooting
## Mismatched LaTeX support files detected
If you receive the following error when compiling a LaTeX document,

then you probably have outdated  files in your home directory (specifically in ) that are not compatible with the system-wide TeX Live installation.
These files are not managed by  so they have to be removed manually after updating an Arch-packaged TeX Live installation.== See also ==

* [https://tug.org/texlive/doc.html TeX Live documentation
* Question and answer sites
** TeX - LaTeX Stack Exchange
** TopTeX (TeX site on TopAnswers)
* Detexify LaTeX handwritten symbol recognition
