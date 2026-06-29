# Fonts

From Wikipedia:Computer font:

: A computer font is implemented as a digital data file containing a set of graphically related glyphs. A computer font is designed and created using a font editor. A computer font specifically designed for the computer screen, and not for printing, is a screen font.

Note that certain font licenses may impose some legal limitations.

## Font formats
Most computer fonts used today are in either bitmap or outline data formats.
;Bitmap fonts: Consist of a matrix of dots or pixels representing the image of each glyph in each face and size.
;Outline or vector fonts: Use Bézier curves, drawing instructions and mathematical formulae to describe each glyph, which make the character outlines scalable to any size.

## Bitmap formats
* Bitmap Distribution Format (BDF) by Adobe
* OpenType Bitmap Fonts (OTB)
* PC Screen Font (PSF) used by the Kernel for console fonts, not supported by Xorg (for Unicode PSF files the extension is )
* Portable Compiled Format (PCF) by Xorg

These formats can also be gzipped. See #Bitmap for the available bitmap fonts.

## Outline formats
* PostScript fonts by Adobe – has various formats, e.g: Printer Font ASCII (PFA) and Printer Font Binary (PFB)
* TrueType by Apple and Microsoft (file extension: )
* OpenType by Microsoft, built on TrueType (file extensions: , )

For most purposes, the technical differences between TrueType and OpenType can be ignored.

## Other formats
The font editing application FontForge () can store fonts in its native text-based format—Spline Font Database ().

The typesetting application TeX Live and its companion font software Metafont traditionally renders characters using its own methods. Some file extensions used for fonts from these two programs are , ,  and . Modern versions can also use TrueType and OpenType fonts.

The SVG format also has its own font description method.

## Installation
There are various methods for installing fonts.

## Pacman
Fonts and font collections in the enabled repositories can be installed using pacman.

Available fonts may be found by querying packages (e.g. for  or ).

## Creating a package
You should give pacman the ability to manage your fonts, which is done by creating an Arch package. These can also be shared with the community in the AUR. The packages to install fonts are particularly similar; see Font packaging guidelines.

The family name of a font file can be acquired with the use of  for example: {{ic|fc-query -f '%{family/path/to/file}}. The formatting is described in .

## Manual installation
The recommended way of adding fonts that are not in the repositories of your system is described in #Creating a package. This gives pacman the ability to remove or update them at a later time.

Alternatively, fonts can be installed manually:

* For a single user, install fonts to .
** In many cases this suffices, unless you run graphical applications as other users.
** In the past  was used, but is now deprecated.
* For system-wide (all users) installation, place your fonts under .
** You may need to create the directory first: .
**  is under the purview of the package manager, and should not be modified manually.

The creation of a subdirectory structure is up to the user, and varies among Linux distributions. For clarity, it is good to keep each font in its own directory. Fontconfig will search its default paths recursively, ensuring nested files get picked up.

An example structure might be:

The font files need to have sufficient read permissions for all users, i.e. at least chmod  for files, and  for directories.

For the Xserver to load fonts directly (as opposed to the use of a font server), the directory for your newly added font must be added with a FontPath entry. This entry is located in the Files section of your Xorg configuration file (e.g.  or ). See #Older applications for more detail.

Finally, update the Fontconfig cache (usually unnecessary as software using the Fontconfig library does this):

 $ fc-cache

## Older applications
With older applications that do not support Fontconfig (e.g. GTK 1.x applications, and ) the index will need to be created in the font directory:

 $ mkfontscale
 $ mkfontdir

Or to include more than one folder with one command:

 $ for dir in /font/dir1/ /font/dir2/; do xset +fp $dir; done && xset fp rehash

Or if fonts were installed in a different sub-folders under the e.g. :

 $ for dir in * ; do if [  -d  "$dir"  ; then cd "$dir";xset +fp "$PWD" ;mkfontscale; mkfontdir;cd .. ;fi; done && xset fp rehash

At times the X server may fail to load the fonts directory and you will need to rescan all the  files:

 # xset +fp /usr/share/fonts/misc # Inform the X server of new directories
 # xset fp rehash                # Forces a new rescan

To check that the font(s) is included:

 $ xlsfonts | grep fontname

This can also be set globally in  or .

Here is an example of the section that must be added to . Add or remove paths based on your particular font requirements.

## Pango warnings
When Pango is in use on your system it will read from Fontconfig to sort out where to source fonts.

 (process:5741): Pango-WARNING **: failed to choose a font, expect ugly output. engine-type='PangoRenderFc', script='common'
 (process:5741): Pango-WARNING **: failed to choose a font, expect ugly output. engine-type='PangoRenderFc', script='latin'

If you are seeing errors similar to this and/or seeing blocks instead of characters in your application then you need to add fonts and update the font cache. This example uses the  fonts to illustrate the solution (after successful installation of the package) and runs as root to enable them system-wide.

You can test for a default font being set like so:

## Font packages
This is a selective list that includes many font packages from the AUR along with those in the official repositories.

## Bitmap
* Default 8×16
* Berry () – 8px
* Dina () – 6pt, 8pt, 9pt, 10pt, monospaced, based on Proggy
* Efont () – 10px, 12px, 14px, 16px, 24px, normal, bold and italic
* GNU Unifont () – 8×16, 16×16 (most extensive Unicode coverage of any font)
* Gohu () – 11px, 14px, normal and bold
* Kissinger 2 – 8×16, 16×16 (Unifont competitor)
* Lime ()
* ProFont () – 10px, 11px, 12px, 15px, 17px, 22px, 29px, normal
* Proggy () – Has different variants
* Tamsyn ()

Works with Pango 1.44 and later:

* Cozette ()
* Gohufont ()
* Misc Fixed ()
* ProFont () – OpenType Bitmap (OTB) variant of ProFont
* Terminus ()
* More OTB fonts on the AUR

## Latin script
## Families
Packages providing a base font set:

* Bitstream Vera () – Includes sans-serif, serif, and monospaced fonts. Bitstream Vera Sans is metrically compatible with Verdana.
* Croscore fonts () – Metric-compatible fonts for Helvetica, Times, Courier and Georgia — named Arimo, Tinos, Cousine and Gelasio respectively, shipped with Chrome OS
* DejaVu fonts () – Bitstream Vera modified for greater Unicode coverage
* Droid () – Default font for older Android versions with wide Unicode coverage including CJK but not symbols and emojis
* GNU FreeFont () – Includes three fonts — FreeSans, FreeSerif and FreeMono — that are clones of Helvetica, Times, and Courier respectively. Most Latin characters are from URW Ghostscript fonts (e.g., Nimbus Roman, Nimbus Sans), non-Latin characters come from many sources with good Unicode coverage, but do not include CJK.
* IBM Plex () – Serif, sans-serif, condensed sans-serif and monospace with true italics
* Input () – Fonts for code from DJR & Font Bureau
*  – Patched font Input containing nerd font symbols
* Liberation fonts () – Metric-compatible fonts for Helvetica, Times, and Courier, but are visually different
* Microsoft fonts () – Windows 11 fonts (Windows 11 installation or installation medium needed)
* Noto fonts () – Google font family with full Unicode coverage if installed with its emoji and CJK optional dependencies
* Roboto () – Default font for newer Android versions where it is complemented by Noto fonts for languages not supported like CJK

Packages not providing a base font set:

* B612 () – Open-source font family (sans and mono) sponsored by Airbus, designed for comfort of reading on aircraft cockpit screens
* Ghostscript () – The Ghostscript fonts donated by URW, includes clones of Helvetica, Times, Courier, and others. GNU FreeFont () and TeX Gyre fonts () are both partially based on the Ghostscript fonts
* Libertinus Fonts () – Forks of Linux Libertine and Linux Biolinum, with extended math support, see #Math
* Luxi fonts () – X.Org font family similar to Lucida
* TeX Gyre fonts () – Created by the Polish GUST association of TeX users, mostly based on URW Ghostscript fonts, includes clones of Helvetica, Times, Courier, and others. Some have their own math companion fonts, see #Math.
* Ubuntu font family ()

Legacy Microsoft font packages:

* Microsoft fonts () – Andalé Mono, Courier New, Arial, Arial Black, Comic Sans, Impact, Lucida Sans, Microsoft Sans Serif, Trebuchet, Verdana, Georgia, Times New Roman
* Vista fonts () – Consolas, Calibri, Candara, Corbel, Cambria, Constantia

## Monospaced
Fonts supporting "programming ligatures" (e.g., the display of the "->" sequence as a double-width "⟶" glyph)  are identified below with a ⟶ sign. For more monospaced fonts, also see #Bitmap and #Families.

* Anonymous Pro (, included in )
* Cascadia Code () ⟶ – Designed to enhance the look of the Windows Terminal, with programming ligatures, released by Microsoft under the Open Font License
* Courier Prime () – Courier alternative which has been supplemented by a sans serif font and a version optimized for programming, released under the Open Font License
* Envy Code R () – Font designed for programmers
* Fantasque Sans Mono (, )
* Fira Mono (, ) – Font optimized for small screens and adopted by Mozilla for the Firefox OS
* Fira Code () ⟶ – Extension of Fira Mono with programming ligatures for common programming multi-character combinations
* Hack () - Open-source monospaced font, used as the default in KDE Plasma
* Hasklig () - A code font with monospaced ligatures
* Hermit () - A font for programmers, by a programmer
* Inconsolata (, included in ) – Designed for source code listing, inspired by Consolas and Letter Gothic
* Inconsolata-g () – Adds some programmer-friendly modifications
* Iosevka () ⟶ – Slender sans-serif and slab-serif typeface inspired by Pragmata Pro, M+ and PF DIN Mono, designed to be the ideal font for programming; it supports programming ligatures and over 2000 latin, greek, cyrillic, phonetic and PowerLine glyphs
* JetBrains Mono () ⟶ – Free and open-source font developed by JetBrains
* Lilex () ⟶ – Free and open-source modern programming font containing a set of ligatures for common programming multi-character combinations
* Lucida Typewriter (included in package )
* Menlo () – Customized version of Apple's Menlo Regular font for OS X with larger vertical gap spacing
* Monaco () – Proprietary font designed by Apple for OS X
* Monofur ()
* Mononoki () – A font for programming and code review
* Roboto Mono () – Based on Roboto ()
* Source Code Pro (, included in )
* Comic Mono () A legible monospace font… the very typeface you’ve been trained to recognize since childhood, ergo Comic Sans

Relevant websites:

* Stack Overflow: Recommended fonts for programming
* Programming Fonts - Test Drive
* Programming Fonts Compare
* Coding Font by Typogram

## Sans-serif
* Adwaita () – Default font supplied with GNOME.
** Cantarell () – Old default font supplied with GNOME until version 48.
* Andika ()
* DMCA Sans Serif () – General purpose sans serif font metric-compatible with Microsoft Consolas
* Fira Sans (, ) – Sans serif font designed by Erik Spiekermann for Mozilla and the Firefox OS. Fira Mono and Fira Code are monospaced companions of Fira Sans (see #Monospaced).
* FreeSans () – Visually similar to Helvetica but metrically different, see #Families
* Inter () – A geometric neo-grotesque font designed for user interfaces
* Jost* () – An open-source typeface based on Futura
* Liberation Sans () – Metric-compatible with Helvetica but visually distinct, see #Families
* Montserrat () – An open-source font that shares similarities with Gotham and Proxima Nova
* Nunito () – An open-source font with rounded terminal, hence shares similarities with Gotham Rounded and Proxima Soft
* Open Sans () – Sans serif font commissioned by Google, based on Droid sans but slightly wider
* PT Sans () – 3 major variations: normal, narrow, and caption - Unicode: Latin, Cyrillic
* Source Sans () – Open-source sans serif font from Adobe with a design based on News Gothic and Franklin Gothic
* Tahoma (Wine Replacement) () – Open-source substitute for Tahoma developed by the Wine project. It was created because many Windows applications expected Tahoma to be available.

## Serif
* Bitstream Charter (, ) – Originally a commercial font designed by Matthew Carter. A version was released under a free license and later converted to modern formats (provided as the aforementioned packages).
* Bodoni* () – An open-source Bodoni revival
* Crimson () – An open-source font that shares similarities with Minion
* EB Garamond () – An open-source Garamond revival, the aforementioned package is the version developed by Octavio Pardo
* FreeSerif () – Visually similar to Times New Roman but metrically different, see #Families
* Gentium (, ) – Unicode, comprehensive support for Latin, Greek, Cyrillic, International Phonetic Alphabet (IPA) characters
* Heuristica () – Based on a version of Utopia that was released under a free license
* Liberation Serif () – Metric-compatible with Times New Roman but visually distinct, see #Families
* Libre Baskerville () – An open-source Baskerville revival designed by Impallari Type
* BaskervilleF () – A PDF-optimized serif font, fork of Libre Baskerville, with added Bold Italic style
* Libre Caslon () – An open-source Caslon revival designed by Impallari Type
* Linux Libertine () – Developed as a substitute of Times New Roman, but different both visually and metrically (the metric differences are more notable for italic and bold fonts). Its fork Libertinus Fonts () is the version that is under active development.
* TeX Gyre Termes () – Visually similar to Times New Roman (but there are some minor metric differences), see #Families
* Tinos () – Metric-compatible with Times New Roman but visually distinct (and looks similar to Liberation Serif), see #Families

## Handwriting
*  – Handwriting of a photographer
*  – Handwriting sans-serif font with bubbly and rounded edges
*  – Brush script handwriting font which was inspired by the 1950s American surf culture and expanded to Cyrillic
*  – Handwriting font inspired from the streets of Sao Paulo, Brazil
*  – Script font based on a reconstruction of Nikola Tesla's handwriting
*  – Font incorporating the graphic, squared look of architectural writing and the natural feel of daily handwriting

## Unsorted
*  – Meta package for all fonts in the official repositories
*  – Font collection from dustismo.com
*  – A huge collection of free fonts (including Ubuntu, Inconsolata, Roboto, etc.)
*  – Junius font containing almost complete medieval Latin script glyphs
*  – Covers full plane 1 and several scripts
*  – OpenDyslexic font for readers with dyslexia
*  – IBM Courier and Adobe Utopia sets of PostScript fonts

## Non-latin scripts
## Ancient Scripts
*  – Font containing Unicode symbols for Aegean, Egyptian, Cuneiform, Anatolian, Maya, and Analecta scripts

## Arabic
See Localization/Arabic#Fonts.

## Bengali
Read Localization/Bengali#Fonts for details.

## Braille
*  – Font containing Unicode symbols for braille

## Chinese, Japanese, Korean, Vietnamese
## Pan-CJK
Adobe Source Han fonts and Noto CJK fonts have identical glyphs and metrics, but with different branding since the project was commissioned by both Adobe and Google.

Both collections comprehensively support Simplified Chinese, Traditional Chinese, Japanese, and Korean, with a consistent design and look. Noto Sans CJK fonts lack localized menu names, that are not required, but may make fonts more user-friendly for customers whose native language is that of the target language of the font.

* Adobe Source Han fonts
** Source Han Sans ()
** Source Han Serif ()
* Noto CJK fonts () – Includes both Noto Sans CJK and Noto Serif CJK

## Chinese
See Localization/Chinese#Fonts.

## Japanese
See Localization/Japanese#Fonts.

## Korean
See Localization/Korean#Fonts.

## Vietnamese
*  – Vietnamese TrueType font for chữ Nôm characters

## Cyrillic
See also #Latin script.

*  – Font family by ParaType: sans, serif, mono, extended cyrillic and latin, OFL license
*  – A free OpenType cursive font for Cyrillic script

## Greek
Almost all Unicode fonts contain the Greek character set (polytonic included). Some additional font packages, which might not contain the complete Unicode set but utilize high quality Greek (and Latin, of course) typefaces are:

*  – Selection of OpenType fonts from the Greek Font Society
*  – Professional TrueType fonts from Magenta
*  – SBL BibLit, includes characters from both SBL Greek and SBL Hebrew

## Hebrew
*  – Large collection of Open-source licensed Hebrew fonts. There are also few Latin, Greek, Cyrillic, Arabic, and Amharic.
*  – Nice collection of free Hebrew fonts
*  – 4 Hebrew fonts (at the moment): the commonly used "David Libre", the handwriting font "Gveret Levin", "Varela Round" and "open-sans"
*  – contains Arial and other fonts
*  – SBL Hebrew, created by the Society of Biblical Literature (SBL)
*  – SBL BibLit, includes characters from both SBL Hebrew and SBL Greek

## Monospaced
* Cousine () – part of the Chrome OS Core Fonts
* Everson Mono () – is lighter and a bit looser than Courier, with wide range of supported Unicode blocks
* FreeMono () – part of the GNU FreeFont

## Indic
See Localization/Indic#Fonts.

## Khmer
*  – Font covering glyphs for Khmer language
* Hanuman ()

## Mongolic and Tungusic
*  – Fonts for Sibe, Manchu and Daur scripts (incomplete, currently in development)

## Persian
Arabic fonts like  also cover Persian letters. A list of Arabic fonts can be checked in Localization/Arabic#Fonts.

*  – Meta package for installing all Persian fonts in AUR
*  – Borna Rayaneh Co. Persian B font series
*  – A free Unicode calligraphic Persian font
*  – Iranian-Sans and Iranian-Serif Persian font family
*  – Iran Supreme Council of Information and Communication Technology (SCICT) standard Persian fonts
*  – A Persian font series derived from X Series 2, Metafont and FarsiTeX fonts with Kashida feature
*  – A Persian font series derived from X Series 2 fonts with Kashida feature
* , , , , , , ,  – Beautiful Persian fonts made by Saber RastiKerdar
*  – The Yas Persian font series (with hollow zero)
*  – Free fonts with support for Persian, Arabic, Urdu, Pashto, Dari, Uzbek, Kurdish, Uighur, old Turkish (Ottoman) and modern Turkish (Roman)

## Tai–Kadai
*  – Collection of scalable Thai fonts
*  – High-quality Thai fonts from Google and new improvement for Thai National Fonts
*  – Lao TTF font (Phetsarath_OT)

## Tibeto-Burman
*  – Tibetan Machine TTFont
*  – Unicode font that supports the many diverse languages that use the Myanmar script

## Emoji and symbols
A section of the Unicode standard is designated for pictographic characters called "emoji".

Emoji fonts come in different formats: CBDT/CBLC (Google), SBIX (Apple), COLR/CPAL (Microsoft), SVG (Mozilla/Adobe).

Emojis should work out of the box once you have at least one emoji font installed of a supported format. However, some of the emoji fonts encode their glyphs as large fixed-size bitmaps and thus, for the purpose of displaying at the intended size, rely on bitmap font downscaling, which is enabled by default.

Emoji font fallback according to the standard requires extra code to handle emoji.

For the discovery and input of Emoji see List of applications/Utilities#Text input.

{| class="wikitable"
|-
! Software !! CBDT/CBLC !! SBIX !! COLR/CPAL !! SVG !! Emoji font fallback
|-
! FreeType
|  ||  ||  ||  ||
|-
! Chromium
| colspan=3  ||
|
|-
! Firefox
| colspan=3  ||
| , see Firefox#Font troubleshooting for workaround.
|-
! Pango
| colspan=3  ||
|
|-
! Qt
| colspan=3  ||
|  [https://bugreports.qt.io/browse/QTBUG-85014 |-
! WebKitGTK
| colspan=3  ||
|
|}

* Font Awesome () – the iconic SVG font
* [https://joypixels.com/emoji JoyPixels () – formerly EmojiOne, part of Emoji as a Service, proprietary
* Nerd Fonts () – developer targeted fonts patched with a high number of icons
* Noto Color Emoji () –  Google open-source emoji font, color
* Noto Emoji  () – Google open-source emoji font, black and white
* OpenMoji () – German University of Design in Schwäbisch Gmünd open-source emoji
* Symbola () – part of Unicode Fonts for Ancient Scripts; version 9 was the last free version, current version is licensed as "pay for any use"
* BabelStone Pseudographica - a font covering various geometric shapes, box drawing shapes, arrows, geometric symbols, and symbol-like punctuation marks defined in the Unicode Standard
* Twemoji (Twitter Emoji) () – emoji for everyone, originally created by Twitter
* Twitter Color Emoji () – SVG-OpenType (SVGinOT) font built from the Twemoji artwork; this font also contains black and white emoji, and the original Twemoji font contains color emoji too

Kaomoji are sometimes referred to as "Japanese emoticons" and are composed of characters from various character sets, including CJK and Indic fonts. The following set of packages covers most of existing kaomoji:
*
*
*

Teranoptia () – is a typeface without letters (an illustrative font), a peculiar contraption that allows you to imagine chimeric creatures just by typing letters with your keyboard.

## Math
* Computer Modern (, )
* Computer Modern (, ) – Improved version used in LaTeX
* Libertinus Math () – A math font based on Libertinus Serif which is a fork of Linux Libertine ()
* STIX fonts () – STIX is designed to be a royalty-free alternative that resembles Times New Roman. The current version is called STIX Two and includes a math companion named STIX Two Math.
* TeX Gyre math fonts () – Math companions of TeX Gyre fonts (see #Families). Notably, TeX Gyre Termes Math is a math companion of Times New Roman.
* Garamond-Math () – An open type math font matching EB Garamond ().
* JuliaMono () – A monospace typeface that has extensive support for mathematical symbols, including calligraphic, blackboard (double-struck), and Fraktur alphanumeric characters.

Additionally,  and  contain many math fonts such as Latin Modern Math and STIX fonts. See TeX Live#Making fonts available to Fontconfig for configuration.

## Other operating system fonts
*  - Apple MacOS TrueType fonts

## Font alias
There are several font aliases which represent other fonts in order that applications may use similar fonts. The most common aliases are:  for a font of the serif type (e.g. DejaVu Serif);  for a font of the sans-serif type (e.g. DejaVu Sans); and  for a monospaced font (e.g. DejaVu Sans Mono). However, the fonts which these aliases represent may vary and the relationship is often not shown in font management tools, such as those found in KDE Plasma and other desktop environments.

To reverse an alias and find which font it is representing, run:

In this case,  is the font represented by the  alias.

## Fallback font order
Fontconfig automatically chooses a font that matches the current requirement. That is to say, if one is looking at a window containing English and Chinese for example, it will switch to another font for the Chinese text if the default one does not support it.

Fontconfig lets every user configure the order they want via .
If you want a particular Chinese font to be selected after your favorite Serif font, your file would look like this:

   serif

     Your favorite Latin Serif font name
     Your Chinese font name

You can add a section for  and  as well.

For more information, have a look at the Fontconfig manual. See also Font configuration#Set default or fallback fonts.

## Tips and tricks
## List installed fonts for a particular language
Applications select and display fonts depending upon Fontconfig preferences and available font glyphs for Unicode text. To list installed fonts for a particular language, issue a command . For instance, to list installed Arabic fonts or fonts supporting Arabic glyphs:

{{hc|1=$ fc-list -f '%{file}\n' :lang=ar|2=
/usr/share/fonts/TTF/FreeMono.ttf
/usr/share/fonts/TTF/DejaVuSansCondensed.ttf
/usr/share/fonts/truetype/custom/DroidKufi-Bold.ttf
/usr/share/fonts/TTF/DejaVuSansMono.ttf
/usr/share/fonts/TTF/FreeSerif.ttf
}}

## List installed fonts for a particular Unicode character
To list all fonts supporting a particular Unicode codepoint—black upwards equilateral arrowhead (⮝) in this case:

 $ fc-list :charset=2B9D

fc-list does not normalize requests, it is going to list fonts which exactly matches. It is not suitable for generic family names (like ) and other ambiguous patterns. To search for monospaced fonts supporting a particular Unicode codepoint you could try the following:

 $ fc-match --sort monospace:charset=2B9D | head

but you have to interpret the result on your own. fc-match by its nature does not guarantee that fonts in the output list are monospaced, nor that they contain the codepoint in question at all.

## Application-specific font cache
Matplotlib () uses its own font cache, so after updating fonts, be sure to remove , , , etc. so it will regenerate its cache and find the new fonts === Bidirectional text support ===

See Bidirectional text for troubleshooting problems related to RTL languages.

## Braille font not displaying correctly inside terminals
If braille characters in terminals exhibit [https://www.reddit.com/r/archlinux/comments/gf2vgb/the_braille_fonts_dont_show_properly_anywhere/ rendering issues, try installing a braille font and uninstalling .

## Application-specific font configuration tips
## Emacs
Emacs calculates sizes differently than standard Linux desktop applications, and Emacs packages do not all use the same config format, so if points or raw pixel size doesn't work, try using the other value.

## Visual Studio Code
Change the setting Editor: Experimental Whitespace Rendering from "svg" to "font" if your monospace fonts have problems scaling certain characters correctly.  This is known to help with "Terminus (TTF)" and "IBM 3270" fonts.
