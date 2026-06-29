# Font package guidelines

This document covers proposed standards and guidelines on writing PKGBUILDs for Fonts.

## General guidelines
## Package naming
* TTF fonts:
* OTF fonts:

If the font is a variable font, add the suffix .

## Package description
The package description should at least contain the word font and what type of font it is: sans-serif, serif or monospace.

## Architecture
Fonts are architecture-independent. Use .

## Dependencies
Fonts do not depend on anything. Many packages in the repositories, however, include  and  as dependencies. Those were required when font packages needed to use install scripts to update the font cache – a lot of duplicate work now done by pacman hooks. If you install fontconfig or xorg-mkfontscale, all existing fonts in  will be cached making it unnecessary to force people to use fontconfig or mkfontscale.

## Provides
Many applications rely on the virtual package . If your font family meets the criteria, add .

## Source
See whether a font is available from the following sources in this order:

* a code hosting platform like GitHub or an official website
* github.com/google/fonts (you should download individual files instead of cloning the repository, see ttf-roboto-mono for an example)
* Font Squirrel, Font Library, FFonts, 1001 Fonts, 1001 Free Fonts, DaFont

The following sites are not recommended:

* fonts.google.com (it no longer provides stable download URLs)
* FontSpace (checksums change for unknown reasons)

## Package
The following snippet is an example for an OTF font released under the SIL Open Font License 1.1 with Reserved Font Name:

{{bc|
license=('OFL-1.1-RFN')
...
package() {
  install -Dm644 -t "$pkgdir/usr/share/fonts/$pkgname" "path/to/font/*.otf"
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" "path/to/license/OFL.txt"
}
}}

* The OFL is technically a custom license, so each font package's license file  needs to be installed under .
* If the font contains many font files, consider using  instead of  for the destination directory.

## Example packages
*
*  – split package with OTF, TTF and variable version
