# WPS Office

WPS Office for Linux is a proprietary alternative for Microsoft Office with a modern UI which supports cross-device file transfer and cloud backup. The suite contains Writer, Presentation and Spreadsheets.

## Installation
Install .

The fonts used by WPS Office are provided by the  package.

The programs in the suite can be run using:

{| class="wikitable"
|- style="font-weight:bold;"
! Command
! Program
|-
|
| WPS Writer
|-
|
| WPS Spreadsheets
|-
|
| WPS Presentation
|-
|
| WPS PDF
|}

## Tips and tricks
## Interface language
Official support is only for English and Chinese ().

Some languages have unofficial translations; you can install them from the AUR packages:

*
*

Then set your language by selecting Review > Spell Check > Set Language to choose your language and restart WPS.

## Modify WPS file icon and file association
After installing WPS, the DOC, XLS, PPT and other files in the icon-theme you use will be replaced with the WPS text, ET form, WPP presentation and other icons that come with WPS Office. If you do not need it, you can modify the relevant mime configuration file yourself:

 /usr/share/mime/packages/wps-office-{wpp,wps,et}.xml
 /usr/share/mime/packages/freedesktop.org.xml #(Belongs to the package shared-mime-info)

And desktop files:

 /usr/share/applications/wps-office-{wpp,wps,et}.desktop

Processing strategy: WPS's own format is defined by {{ic|wps-office-{wpp,wps,et}.xml}}, and others are defined by . Also modify the  item of the  file.

Add the following statement to the  function in the PKGBUILD file:

## Troubleshooting
## WPS Office overriding or breaking mime
Add  before :

Then save the file, and restart WPS Office.

## Zip template compressed packet garbled
Use the parameter  with  when decompressing.

## Formula can not display normally
the display of most Mathematical formula need fonts show below:

 symbol.ttf webdings.ttf wingding.ttf wingdng2.ttf wingdng3.ttf monotypesorts.ttf MTExtra.ttf

 contain all of these fonts except monotypesorts.ttf, you can install it directly.

## Microsoft Office file in KDE Plasma is recognized as Zip
After installing WPS Office, Microsoft Office files will be recognized as zip and cannot open with WPS. You can remove the offending  package.

## WPSPDF functionality unavailable
Functions related to PDF export, opening, and other PDF-related features are all provided by WPSPDF. However, WPSPDF relies on  to support its PDF functionality: install .

## Fonts are too bold
Version 11.1.0.11704-1 doesn't work well with freetype2 versions above 2.13.0. Normally, freetype2 creates a bold variant if the chosen font does not have a bold version. This is called "fakebold", but in this case, wps-office is also making fonts bold on its own, and the result is that the text looks too bold.

To workaround this issue until a long term fix is provided, install .
