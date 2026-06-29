# Localization/Arabic

This article describes how to set up Arabic language environment.

## Applications
* Locale article explains how to set up system or user locale.
* Bidirectional text article lists Bidi support status in applications.
* Keyboard layout: set it by . Check the article for more info.
* Ayaspell offers spellchecking extensions. Can be installed system-wide by .
* Aspell: install
* Dict: For Arabic dictionaries install , .
* Islamic tools: for Hijri date conversion.
* LibreOffice: set up Bidi support. If you are not using a system-wide Arabic dictionary, Ayaspell extension can be installed from Tools > Language > More Dictionaries Online > Arabic. For language pack, install  for the stable branch and  for Libreoffice fresh.
* : for OCR detection, the default data package  is mostly inaccurate. Try  see * Thunderbird: install  for language pack.
* Firefox: install  for language pack.
* dwm: see Dwm#Arabic Letter-shaping

## Shell and Terminal
* st: see St#Arabic shaping support
* mlterm: see Mlterm#Render Arabic script in Xft and Mlterm#Arabic script rendering when using fixed width fonts
* bash: enables by default "combining characters" ([https://unicode.org/L2/L2014/14109-inline-chars.pdf 1) feature, which merges diacritics with previous character.
* zsh: to properly display diacritics add  to your .

## Vim
* See Vim#Bidirectional support for setting up Bidi support.
* Since Vim does not map Arabic characters given by input method, motion commands do not work. A possible workaround is to set keymap within Vim without changing X11 keymap. This can be done , then switching between layouts via , or by manually set langmap in :
 set langmap=ضصثقفغعهخحجد;qwertyuiop== Fonts ==

Check Font configuration/Examples#Arabic for setting up font configuration. Persian fonts like  also include support for Arabic letters. A list of Persian fonts can be checked from Fonts#Persian.

Multi-script (extended Arabic script) fonts:

*  - Google Noto fonts includes Noto Kufi Arabic, Noto Sans Arabic, and Noto Kufi Arabic. Use  for installing these only.
*
*
*  - Includes the monospace DejaVu Sans Mono font.
*  — Collection of free Arabic fonts that includes:
** [https://fonts.qurancomplex.gov.sa/ KACST fonts
** Thuluth script font
** Thabit: monospace font
** Decorative: AlArabiya, AlBattar, AlHor, and others.

Sans-Serif:

*
*
*
*

Monospace:

*  - A monospaced font by Microsoft that includes programming ligatures.
*  - Persian font with good monospace support for Arabic.
*
*  - Typewriter Naskh font based on Amiri

Bitmap:

* Arabeyes bitmap font

Naskh (~Serif):

*  — Unicode Arabic font from SIL (Alternative for Traditional Arabic font)
*  — A classical Arabic typeface in Naskh style pioneered by Amiria Press. Its Latin characters are based on Crimson () [https://github.com/skosch/Crimson
*  — Fonts by King Fahd Glorious Quran Printing Complex in al-Madinah al-Munawwarah
*  — Unicode Arabic font from SIL

Ruq'ah, Kufic (~Sans-Serif):

*  - Ruq'ah typeface.
*
*
*  - A manuscript Kufic typeface.
*
*

## Kashida justification
Kashida justification could be applied either to single letters or in-between letters. For more information, see * LibreOffice: [https://bugs.documentfoundation.org/show_bug.cgi?id=164522 single-letter Kashida not supported. In-between-letter Kashida is supported by applying paragraph justification.
* LaTeX: single-letter Kashida not supported. In-between-letter Kashida can be applied using  option in Babel package. The following is a sample preamble:

 \usepackage[
 	english,
 	bidi=basic,
 ]{babel}
 \babelprovide[
 	import, main,
 	justification = kashida,
 	transforms = kashida.plain
 ]{arabic}
 \babelfontNew}

* typst: [https://github.com/typst/typst/issues/195 Unsupported

## Tips and tricks
* Disable URL encoding for links containing Arabic characters. See Character encoding#URL encoding.

## Troubleshooting
Common issues may be solved by checking Locale#Troubleshooting and Character encoding#Troubleshooting first. For problems related to letter-shaping or text direction, check Bidi.

## XKB Lam Alif problem
X keyboard layout sends Arabic ligature glyphs as a single glyph. For example, Laa+Alif ligature "لا" (U+0644, U+0627) is sent as "ﻻ" (U+FEFB), and similarly for (ﻷ، ﻵ، ﻹ). This is due to a known limitation in xkb which does not allow mapping a key to more than one character. To solve this problem, run a supported input method. The input method workaround takes advantage of Compose Sequences. For a technical reading on this, check These are confirmed to work:

* IBus: supported since [https://github.com/ibus/ibus/releases/tag/1.5.28 v1.5.28.
* : supported since 2.19.0

For a more lightweight option, you can use Xim. Add the following to your environment variables:

 XIM=none
 XIM_PROGRAM=/bin/true
 XIM_ARGS=
 GTK_IM_MODULE=xim
 QT_IM_MODULE=xim
 SHORT_DESC="X compose table"

Alternatively, you can use IM config wrapper script: .

Since QT-based programs do not have this issue, it is enough to add  to  or . The issue is also fixed for GTK4.

## Fix Arabic legibility when using Noto Fonts
If Arabic characters are rendered in an unexpected font (e.g: Nastaliq, Urdu font, etc.), see Font configuration/Examples#Excluding Arabic script from other languages.
