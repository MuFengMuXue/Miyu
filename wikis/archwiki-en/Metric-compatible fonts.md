# Metric-compatible fonts

Metric-compatible fonts are fonts that match the metrics (i.e. glyph dimensions) of another font (often generics such as Helvetica, Times or Courier). Due to their matching metrics, replacing a font with a metric-compatible alternative does not change the formatting of the document or a web page. Such fonts are often developed for FOSS systems to display pages correctly.

## List of metric-compatible fonts
In the following table, commonly-specified families are shown in bold. This table is roughly based on fontconfig's 30-metric-aliases.conf and Wikipedia pages for individual fonts.

{| class="wikitable" width="100%"
|+ "Core fonts for the web" compatibilities
! PostScript !! URW !! GUST !! GNU !! Microsoft  !! Liberation !! CrOS !! StarOffice
|-
| Helvetica || Nimbus Sans, A030 || TeX Gyre Heros || FreeSans || Arial || Liberation Sans || Arimo || Albany
|-
| Times || Nimbus Roman || TeX Gyre Termes || FreeSerif || Times New Roman || Liberation Serif || Tinos || Thorndale
|-
| Courier || Nimbus Mono || TeX Gyre Cursor || FreeMono ||  Courier New || Liberation Mono || Cousine || Cumberland
|-
| Helvetica Condensed || Nimbus Sans Narrow || TeX Gyre Heros Cn || ||  Arial Narrow || Liberation Sans Narrow ||  ||
|-
|  || || || || Georgia ||  || Gelasio ||
|-
| Wingdings (PS3) || URWDings, New Dingbats || || ||  Wingdings || || ||
|}

{| class="wikitable" width="100%"
|+ Microsoft Office fonts
! Microsoft !! width="50%"|CrOS
|-
| Cambria || Caladea
|-
| Calibri || Carlito
|-
| Symbol  || SymbolNeu
|}

{| class="wikitable" width="100%"
|+ Microsoft UI fonts
! Microsoft !! width="50%"|FOSS
|-
| Segoe UI || Selawik
|-
| Tahoma  || Wine Tahoma
|}

{| class="wikitable" width="100%"
|+ Fonts with 1884÷2048em top, 514÷2048em bottom, 1126÷2048em width
! Microsoft !! width="50%"| Type Design
|-
| Consolas || DMCA Sans Serif
|}

{| class="wikitable" width="100%"
|+ Fonts with 8×16 glyphs and 16×16 glyphs
! GNU !! width="50%"| Type Design
|-
| Unifont || Kissinger 2
|}

{| class="wikitable" width="100%"
|+ Other PostScript core families
! PostScript !! URW !! GUST !! Windows
|-
| ITC Avant Garde Gothic || URW Gothic || TeX Gyre Adventor || Century Gothic
|-
| ITC Bookman || Bookman URW || TeX Gyre Bonum || Bookman Old Style
|-
| ITC Zapf Chancery || Chancery URW, Z003 || TeX Gyre Chorus || Monotype Corsiva
|-
| Palatino || Palladio URW, P052 || TeX Gyre Pagella || Palatino Linotype, Book Antiqua
|-
| New Century Schoolbook || Century SchoolBook URW, C059 || TeX Gyre Schola || Century Schoolbook
|-
| ITC Zapf Dingbats || Dingbats, D050000L
|}

{| class="wikitable" width="100%"
|+ PostScript 3 Fonts
! PostScript !! width="50%"|URW
|-
| Optima || URW Classico
|-
| Antique Olive || Antique Olive
|-
| Univers || URW Classic Sans, U001
|-
| Clarendon Bold Condensed || Clarendon URW Bold Condensed, C011 Bold Condensed
|-
| Coronet || Coronet
|-
| Letter Gothic || Letter Gothic
|-
| Marigold || Mauritius
|-
| Albertus || Algiers, A028
|-
| Garamond || Garamond No. 8
|}

## Generic Families
## PostScript
The PostScript language defines 35 core fonts in PostScript 2. URW released open-source versions/clones of these 35 fonts for Ghostscript, available as . Projects including GUST's TeX Gyre and GNU FreeFont release enhanced versions of these fonts.

PostScript 3 defines an additional 101 fonts, many of which are made available by URW under the AFPL in GhostPDL. The AFPL bars commercial use. Many of the dual font names are caused by a batch update.

## Garamond
URW's Garamond No.8 only provides one optical size (8pt). You may use EB Garamond for more OpenType features, including the 12pt size. It is, however, not guaranteed to be metric-identical.

## Microsoft
Microsoft bundles a number of fonts with Microsoft Windows and Microsoft Office. While some of these fonts are just a cheaper version (or look-alike) of corresponding PostScript families, Cambria and Calibri (default font since MS Office 2007) are independent from other families. Microsoft used to provide many core fonts in its Core fonts for the Web project. Although this project is later unavailable on Microsoft's site, the license terms that allow these fonts to be distributed from third-party sites make packages like  possible. See also Microsoft fonts.

Prior to the introduction of Arial and Times New Roman, Microsoft used two bitmap fonts called Helv and Tms Rmn in Windows 1.0, each being unlicensed imitations of better-known fonts already covered here. They were later renamed MS Sans Serif and MS Serif starting with Windows 3.1, and MS Sans Serif was eventually vectorized into "Microsoft Sans Serif". Documents using these fonts are rare, but user interfaces that use Microsoft Sans Serif can occasionally be found in Mono libgdiplus applications. It is generally safe to assume these fonts are metric-compatible with Helvetica and Times when trying to replace them.

## Metric-compatible font projects
## TeX Gyre
TeX Gyre () is a remake and extension of the 35 base PostScript fonts distributed with Ghostscript 4.00. The project provides TeX support and also the cross-platform OpenType format of the fonts. A related project, TeX Gyre Math, provides corresponding mathematical OpenType fonts.

## GNU FreeFont
GNU FreeFont () is an outline family intended to cover as much of the Universal Character Set as possible. Most of the Latin characters are from URW (Nimbus) fonts. This set of fonts is released under GPL v3+ + FE. Note that some of the glyphs for non-LGC languages may be considered lower quality.

## Liberation
Liberation fonts provides four families Liberation Sans, Liberation Serif, and Liberation Mono, intended to be metric-compatible with common Microsoft Windows fonts. Since version 2.0.0, this set of fonts is released under SIL OFL, and is based on #Chrome OS core fonts. They are available as . Though metric-compatible, the overall glyph style is rather different from Microsoft and Apple's implementations.

Older, GPL-licensed versions of this font is based on Ascender Corporation's fonts, which is licensed by Red Hat, Inc. These versions of Liberation also includes Liberation Sans Narrow, which corresponds to Arial Narrow. This one font is available as .

## Ume
Ume Fonts (Japanese) () is a font projects which provides metric-compatible fonts with MS Japanese fonts, such as: Ume Gothic (MS Gothic), Ume UI Gothic (MS UI Gothic), Ume P Gothic (MS PGothic), ...

## Google
Google provides a high number of fonts, including different metric-compatible font families.

Gelasio (), the Google alternative for Georgia, can be found on FontLibrary under SIL OFL.

## Chrome OS
Google ships open-source metric-compatible fonts with its operating system, Chrome OS, under the Apache License 2.0. CrOS core (croscore, ) is a collection of Arimo (sans), Tinos (serif) and Cousine (mono), also licensed from Ascender Corporation. A set of extra fonts, CrOS extra (crosextra) provides Carlito () and Caladea () to match default fonts for Microsoft Word.

Since glyph mappings from Symbol are usually implemented in browsers, Google no longer ships SymbolNeu in croscore > 1.23.0. You can get this font from croscorefonts-1.23.0.tar.gz.

## Noto
Google's Noto Fonts are available via . They are licensed under SIL OFL. Noto Fonts are designed to supplement glyph coverage for Roboto (), the standard typeface for Android, and are vertically (i.e. same line height for the same font size) metric-compatible with Roboto.

## Other metric-compatible fonts
## DMCA Sans Serif
DMCA Sans Serif () is a general purpose sans serif alternative to Microsoft's Consolas, it uses the same metric (1884/2048 top, 514/2048 bottom, 1126/2048 width) and is in the public domain. Version 9.0 has 3309 characters, which is the Subset3+ character set.

## Kissinger 2
Kissinger 2 is a public domain competitor of Unifont. Unlike Unifont, Kissinger 2 is split into separate halfwidth (8×16) and fullwidth (16×16) fonts, with some characters having glyphs in both widths. Version dev5 has 26466 halfwidth characters, 38948 fullwidth characters, 63060 total, and 2354 overlap. Kissinger 2 dev5 also includes OpenType features for Arabic/Hebrew/Thai/Vietnamese shaping and proper alignment of combining marks, which may also affect metric compatibility.

## Selawik
Selawik () is Microsoft's open-source alternative to its Segoe UI font. Unfortunately it does not match Segoe UI's kerning parameters. It was developed for use in the WinJS framework, which is now abandoned.

## Wine Tahoma
The Wine project developed a metric-compatible font to replace Microsoft's Tahoma, available as . Its name in TTF data is simply "Tahoma", so there is no configuration needed.

## Example configuration
For font consistency, all applications should be set to use the serif, sans-serif, and monospace aliases, which are mapped to particular fonts by fontconfig. Font configuration#Set default or fallback fonts explains two ways to achieve the configuration, both are covered with an example for metric-compatible fonts below.

## Example for binding method
The following example configuration uses the #Liberation fonts.

## Example for prefer method
The following example configuration uses the #Chrome OS fonts, adding additional aliases for other fonts frequently required to refer.
