# Microsoft fonts

This article explains how to install TrueType Microsoft fonts and emulate Windows' font rendering.

## Installation
## Automatic installation
The easiest way to install the fonts is by installing one of the following:

*  — Windows 11 fonts
*  — Windows 10 fonts
*  — Vista and Office 2007 fonts

## Current packages
*  /  — Windows 11 fonts
*  /  — Windows 10 fonts
*  — Windows 8.1 fonts
*  — Windows 7 fonts
*  — Office 365 fonts
*  — Office 2007 fonts

## Using fonts from a Windows partition
If there is a Windows partition mounted, its fonts can be used directly. There are a few options on how to do this (assuming the Windows  drive is mounted at ):

* Using a symlink:

 # ln -s /windows/Windows/Fonts /usr/local/share/fonts/WindowsFonts

* Copying the files to :

 # mkdir -p /usr/local/share/fonts/WindowsFonts
 # cp -r /windows/Windows/Fonts/* /usr/local/share/fonts/WindowsFonts/
 # chmod -R 644 /usr/local/share/fonts/WindowsFonts/*

* Using a bind mount:

 # mount --bind /windows/Windows/Fonts /usr/local/share/fonts/WindowsFonts

To make this permanent, edit the fstab file like so:

See  for more details.

Keep in mind that it may be necessary to apply a workaround for system compressed files in order to read the font files.

After choosing one of these options, regenerate the fontconfig cache:

 # fc-cache --force
 # fc-cache-32 --force

## Extracting fonts from a Windows ISO
The fonts can also be found in a Windows ISO file. The format of the image file containing the fonts in the ISO is either WIM (Windows Imaging Format) if the ISO is downloaded online or ESD (Windows Electronic Software Download) if it is built with Windows' Media Creation Tool. Extract the  or the  file from the .iso and look for a  directory within this file. It can be extracted using 7z or wimextract (in ). See an example below using 7z:

 $ 7z e WinXY_YYMM_English_x64.iso sources/install.wim
 $ 7z e install.wim 1/Windows/{Fonts/"*".{ttf,ttc},System32/Licenses/neutral/"*"/"*"/license.rtf} -ofonts/

The fonts and the license will be located in the  directory.

## Legacy packages
 includes:

* Andalé Mono
* Arial
* Arial Black
* Comic Sans
* Courier New
* Georgia
* Impact
* Lucida Sans
* Lucida Console
* Microsoft Sans Serif
* Times New Roman
* Trebuchet
* Verdana
* Webdings

You can also obtain  which, as you might expect, contains Tahoma.

 includes:

* Calibri
* Cambria
* Candara
* Consolas
* Constantia
* Corbel

## Fontconfig rules useful for MS Fonts
## Rule mapping for similar fonts
Often websites specify the fonts using generic names (helvetica, courier, times or times new roman) and a rule in fontconfig maps these names to free fonts (Liberation, Google CrOS, GUST TeX Gyre...). The substitutions are defined in .

To make full use of the Ms Windows fonts it is necessary to create a rule mapping those generic names to the Ms Windows specific fonts contained in the various packages above:

          Helvetica

          Arial

          Times

          Times New Roman

          Courier

          Courier New

It is also useful to associate serif,sans-serif,monospace fonts in your favourite browser to MS fonts.

## Disable embedded bitmap fonts
Some Microsoft TTF fonts such as Calibri and Cambria contain embedded bitmap fonts for specific font sizes, which are not anti-aliased. If embedded bitmaps are enabled, the fonts are not anti-aliased at those specific sizes. Embedded bitmap fonts can be disabled in the font configuration.

## Known issues
## Symbols not displaying properly with Poppler-based PDF readers
The TrueType Microsoft font for Symbol (Wikipedia:Symbol (typeface)) are buggy with Poppler, math symbols may not display correctly in Poppler-based PDF readers.
