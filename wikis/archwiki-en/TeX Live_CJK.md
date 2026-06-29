# TeX Live/CJK

A guide for typesetting Chinese, Japanese, and Korean documents with TeX Live.

## Installation
Language-specific fonts and macro packages are made available by installing the appropriate package(s) from the  group:

*
*
*

Other fonts can be installed through methods outlined in Fonts#Installation. You may also be interested in making Tex Live fonts available to Fontconfig (but this is not strictly necessary).

Users of -based PDF viewers like Evince should install poppler-data as an additional dependency to properly display PDF documents containing CJK characters. (This appears unnecessary if CJK fonts from  are used.)

Needless to say, your locale should have a character encoding that can deal with special characters (such as UTF-8) and you should also have an input method editor installed. The (Simplified/Traditional) Chinese, Japanese, and Korean subpages of Localization also contain information pertaining to locales and fonts.

## Typesetting
Overleaf's online documentation has articles covering different methods for CJK typesetting that are also applicable to TeX Live installations on Arch Linux:

* https://overleaf.com/learn/latex/Chinese
* https://overleaf.com/learn/latex/Japanese
* https://overleaf.com/learn/latex/Korean

## Fonts
A table of some font families/files mentioned in the Overleaf articles, and their respective packages can be found below:

{| class="wikitable"
! scope="col" | Language !! scope="col" | Font family/file !! scope="col" | Package
|-
! scope="row" | Chinese
| BabelStone Han ||
|-
! scope="row" rowspan="4" | Japanese
| IPAMincho || rowspan="2" |
|-
| IPAGothic
|-
| TakaoMincho || rowspan="2" |
|-
| TakaoGothic
|-
! scope="row" rowspan="2" | Korean
|  || rowspan="2" |
|-
|
|}

You can set fonts with {{ic|\setCJKtypefont{font}}} when using ctex or xeCJK. ({{ic|\settypejfont{font}}} can be used with the pTeX engine.)  can take on the values of , , and .  is the font family for user/system fonts and the font file for TeX Live fonts.

## pTeX engine
Overleaf's Japanese#The pTeX engine provides a  file that is meant to be used with the latemk utility from . Running  on Arch Linux without any arguments will only produce a DVI file from the example document. Use the  option to also produce a PDF file from the DVI file. See  or  for more information.

As briefly mentioned in the Overleaf article, upLaTeX (similarly to pLaTeX) "provides pLaTeX2ε macros for upTeX", a "Unicode version of pTeX".

## Troubleshooting
## CTeX-kit
Solutions to common problems when using a CTeX-kit collection/package like  or .

## ctexhook.sty not found
The following error may be encountered when compiling a Japanese or Korean document:

 ! LaTeX Error: File `ctexhook.sty' not found.

Install the  package to obtain . This is required even for non-Chinese typeset documents.

## Missing or inconsistent fonts
Japanese or Korean PDF documents may have missing characters or inconsistent font weights. When no CJK font is specified, the default font Fandol will be used. However, Fandol is "designed for Chinese typesetting" and thus unsuitable for Japanese and Korean. Explicitly set a Japanese or Korean font to avoid this issue.

## LuaLaTeX
Solutions to common problems when using LuaLaTeX to compile documents.

## luatexja.sty not found
The following error may be encountered when compiling a Chinese or Korean document with a  document class:

 ! LaTeX Error: File `luatexja.sty' not found.

Install the  package to obtain . This is required even for non-Japanese typeset documents.

## Resource problems with large fonts
When using large fonts like those from , document compilation can be resource intensive and time consuming due to font cache generation. Subsequent compilations should be much quicker though. One possible workaround (besides using a smaller font) is to trim the font by removing glyph names. Bear in mind that doing this may have consequences.
