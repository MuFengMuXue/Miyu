## Creating New Fonts

Wine, and the free software community in general, currently lacks free
fonts. Windows relies on several standard fonts to be installed and as a
result Wine must also provide them. All of the infrastructure is in
place for Wine to use new fonts, in fact we already have a number of
fonts. However we also need to create other new ones. The most important
fonts to replace are True\`\`Type ones. Working on this project requires
minimal coding skills, most of which will only be needed to hook the new
fonts into the Wine build system.

To get started, you can read about what has been done in the past in
Wine Weekly News issues [\#240](https://www.winehq.com/?issue=240),
[\#241](https://www.winehq.com/?issue=241), and
[\#261](https://www.winehq.com/?issue=261). At this point Wine uses fonts
created with [FontForge](https://fontforge.sourceforge.net). To create
more fonts, you'll first want to figure out a game plan. You'll probably
want to pursue one of three methods after researching them all:

### Getting others to relicense existing fonts

Several [free TrueType
fonts](https://cg.scs.carleton.ca/~luc/originalfonts.html) already exist,
we just need to get them to be licensed under the LGPL. If you contact
the authors and politely explain what you're trying to do you may be
successful. At that point you just need to import the fonts into
FontForge and generate .sfd "spline font database files". This method
might be easiest.

### Tracing glyphs

This method relies on tracing an existing glyph into an image and then
building a new font based on the image. The process is described in
detail on FontForge's website, however the question of the legality
remains to be answered. You'll need to find out how legal that is as
part of the project.

### Doing it all from scratch

This method involves the most work. You are essentially creating new
glyphs from scratch. Again, FontForge has all the information regarding
this.

## What fonts need to be replaced?

With regards to what fonts need to be replaced, we should start with:

- Terminal (bitmap font)
- Microsoft Sans Serif (TrueType and different than MS Sans Serif)

From there, we also need replacements for the following TrueType fonts
(this list may be wrong, you should check whether existing fonts can
replace these):

- Arial
- Comic Sans MS
- Courier
- Georgia
- Impact
- Times New Roman
- Trebuchet MS
- Verdana
- Wingdings \[implemented, but still missing many glyphs\] see bug #7156
- Webdings

- Microsoft's list of Fonts supplied with their products
  [1](https://www.microsoft.com/typography/fonts/)
- (Can vista cleartype fonts be used in wine? -nathan) Vista Cleartype
  Fonts are included with either of the following download free
  [Microsoft Powerpoint 2007
  Viewer](https://www.microsoft.com/downloads/details.aspx?familyid=048DC840-14E1-467D-8DCA-19D2A8FD7485&displaylang=en)
  or the [Microsoft Office Compatibility
  pack](https://www.microsoft.com/downloads/details.aspx?FamilyId=941B3470-3AE9-4AEE-8F43-C6BB74CD1466&displaylang=en).
  [2](https://labnol.blogspot.com/2007/03/download-windows-vista-fonts-legally.html)

## What fonts exist in Wine?

As of wine version 1.0 the following fonts (in the wine/fonts
directory) exist.

### Bitmap Fonts

The following FontForge .sfd's "spline font database files" create the
Bitmap Fonts listed:

- **system.sfd** - "System Bold" (C) 2004 Huw D M Davies, Dmitry
  Timoshkov" - Font\`\`Forge - Created:2004-7-15 Version: 001.000

  Creates **system.ttf**

  ```
  vgasys.fon: /system.ttf 16,1252,7
  vgasyse.fon: /system.ttf 16,1250,7
  vgasysr.fon: /system.ttf 16,1251,7
  vgasysg.fon: /system.ttf 16,1253,7
  vgasyst.fon: /system.ttf 16,1254,7
  vgas1255.fon: /system.ttf 16,1255,7
  vgas1256.fon: /system.ttf 16,1256,7
  vgas1257.fon: /system.ttf 16,1257,7
  vgas874.fon: /system.ttf 16,874,7
  jvgasys.fon: /system.ttf 18,932,8
  svgasys.fon: /system.ttf 16,936,7 16,1252,7
  hvgasys.fon: /system.ttf 16,949,7
  cvgasys.fon: /system.ttf 16,950,7 16,1252,7
  ```

- **small_fonts_jp.sfd** - "Small Fonts Medium" "(C) 2006 Huw D M
  Davies, Dmitry Timoshkov, Aric Stewart" - Font\`\`Forge - Created:
  2006-4-1 Version: 001.000

  Creates **small_fonts_jp.ttf**

  ```
  jsmalle.fon: /small_fonts_jp.ttf 11,932,7
  ```

- **small_fonts.sfd** - "Small Fonts Medium" "(C) 2006 Huw D M Davies,
  Dmitry Timoshkov" - Font\`\`Forge - Created:2006-4-1 Version: 001.000

  Creates **small_fonts.ttf**

  ```
  smalle.fon: /small_fonts.ttf 11,1252,5
  smallee.fon: /small_fonts.ttf 11,1250,5
  smaller.fon: /small_fonts.ttf 11,1251,5
  smalleg.fon: /small_fonts.ttf 11,1253,5
  smallet.fon: /small_fonts.ttf 11,1254,5
  smae1255.fon: /small_fonts.ttf 11,1255,5
  smae1256.fon: /small_fonts.ttf 11,1256,5
  smae1257.fon: /small_fonts.ttf 11,1257,5
  ```

- **ms_sans_serif.sfd** - "MS Sans Serif Medium" "(C) 2004 Huw D M
  Davies, Dmitry Timoshkov" - Font\`\`Forge - Created:2004-6-17 Version:
  001.000

  Creates **ms_sans_serif.ttf**

  ```
  sserife.fon: /ms_sans_serif.ttf 13,1252,5 16,1252,7 20,1252,8
  sserifee.fon: /ms_sans_serif.ttf 13,1250,5 16,1250,7
  sserifer.fon: /ms_sans_serif.ttf 13,1251,5 16,1251,7 20,1251,8
  sserifeg.fon: /ms_sans_serif.ttf 13,1253,5 16,1253,7 20,1253,8
  sserifet.fon: /ms_sans_serif.ttf 13,1254,5 16,1254,7 20,1254,8
  ssee1255.fon: /ms_sans_serif.ttf 13,1255,5 16,1255,7 20,1255,8
  ssee1256.fon: /ms_sans_serif.ttf 13,1256,5 16,1256,7 20,1256,8
  ssee1257.fon: /ms_sans_serif.ttf 13,1257,5 16,1257,7 20,1257,8
  ssee874.fon: /ms_sans_serif.ttf 13,874,5 16,874,7 20,874,8
  ```

- **courier.sfd** - "Courier Medium" "(C) 2004 Huw D M Davies, Dmitry
  Timoshkov" - Font\`\`Forge - Created:2004-8-6 Version: 001.000

  Creates **courier.ttf**

  ```
  coure.fon: /courier.ttf 13,1252,8
  couree.fon: /courier.ttf 13,1250,8
  courer.fon: /courier.ttf 13,1251,8
  coureg.fon: /courier.ttf 13,1253,8
  couret.fon: /courier.ttf 13,1254,8
  coue1255.fon: /courier.ttf 13,1255,8
  coue1256.fon: /courier.ttf 13,1256,8
  coue1257.fon: /courier.ttf 13,1257,8
  ```

### Truetype Fonts

- **marlett.ttf** - "Marlett Regular" Version: 0.2 (C) TransGaming
  Technologies. All rights reserved. GNU Lesser General Public License
  2.1
- **symbol.ttf** - "WineSymbol" Version 1.1 (c) 2009 Jon Parshall for
  CodeWeavers GNU Lesser General Public License 2.1
- **tahoma.ttf** - "Wine Tahoma Regular" Version 0.001 (C) 2004 Larry
  Snyder Based on Bitstream Vera Sans (C) Bitstream Inc GNU Lesser
  General Public License 2.1
- **tahomabd.ttf** - "Wine Tahoma Bold" Version 0.001 (C) 2004 Larry
  Snyder Based on Bitstream Vera Sans (C) Bitstream Inc. GNU Lesser
  General Public License 2.1
- **wingding.ttf** - "WineWingdings" Version 001.000 (C) 2013 Dmitry
  Timoshkov GNU Lesser General Public License 2.1

## See Also

- [Uniscribe](Uniscribe)
