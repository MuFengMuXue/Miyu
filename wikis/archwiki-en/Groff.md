# Groff

According to Wikipedia:

:Groff (GNU troff) is a typesetting system that reads plain text mixed with formatting commands and produces formatted output.

Output may be PostScript or PDF, html, or ASCII/UTF8 for display at the terminal. Formatting commands may be either low-level typesetting requests (“primitives”) or macros from a supplied set. Users may also write their own macros. All three may be combined. Using groff may be a solid alternative to TeX Live due to small size and native language.

## Installation
You may find  already installed on your system as it is a dependency of the  package.
Otherwise install it as usual.

## Package documentation
Detailed documentation and usage examples are available in  or its Info document groff.

You can also access the documentation at https://www.gnu.org/software/groff/groff.html#documentation.

## Usage
Groff is a powerful and yet lightweight easy to use system.

You can see an example of document created with  macros, however, groff has several built-in macros as well.

You may be interested in using  for not complicated tasks or  to produce scientific papers. See  and .

See the following resources for feature information:

* The Groff and Friends HOWTO
* Creating Documents in Groff or LaTeX
* Mom macros examples

## Tips and tricks
## Adding support for cyrillic fonts
If you see inappropriate symbols when outputting documents with cyrillic fonts to ps or pdf, take the following steps:

* Download type1 fonts with cyrillic support (for example from gs-type1_koi8_fonts.tgz Arial, Times, Courier)
* Place your cyrillic type1 fonts into  — this is default folder for ghostscript to find fonts
* Create a copy of the original file before changing it:
  cd
  cp Fontmap.GS Fontmap.GS.backup
* Change ghostscript fontmap file to associate default fonts with cyrillic ones, using '%' to comment lines with default associations. Add new aliases, as follows:

Where '(times8.pfb)' is a name of your copied type1 font.
* From now on you can prepend your default groff command with iconv prefix to print cyrillic symbols in ps files:
 $ iconv -f utf-8 -t koi8-r test.ms | groff -ms -Tps > test.ps && ps2pdf test.ps test.pdf

## Correctly display Polish diacritics
To display Polish diacritics:

 $ groff -Kutf8 -Tdvi -mec -ms test.ms > test.dvi
 $ dvipdfm -cz 9 test.dvi
