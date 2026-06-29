# Font configuration

Fontconfig is a library designed to provide a list of available fonts to applications, as well as configuration for how fonts get rendered.

The FreeType library renders fonts based on this configuration. The  font rendering package includes the bytecode interpreter (BCI) enabled for better font rendering, especially with an LCD monitor. See #Fontconfig configuration and Font configuration/Examples.

Although Fontconfig is used often in modern Unix and Unix-like operating systems, some applications rely on the original method of font selection and display, the X Logical Font Description (XLFD).

## Font paths
For fonts to be known to applications, they must be cataloged for easy and quick access.

The font paths known to Fontconfig by default are: ,  (and , now deprecated). Fontconfig will scan these directories recursively. For ease of organization and installation, it is recommended to use these font paths when adding fonts.

To see a list of known Fontconfig fonts:

 $ fc-list ':' file

See  for more output formats.

Check for Xorg known font paths by reviewing its log:

 $ grep /fonts ~/.local/share/xorg/Xorg.0.log

Keep in mind that Xorg does not search recursively through the  directory like Fontconfig does.  To add a path, the full path must be used:

 Section "Files"
     FontPath     "/usr/share/fonts/local/"
 EndSection

For more details about Xorg configuration read Xorg#Configuration. If you want font paths to be set on a per-user basis, you can add and remove font paths from the default by adding the following line(s) to :

 xset +fp /usr/share/fonts/local/           # Prepend a custom font path to Xorg list of known font paths
 xset -fp /usr/share/fonts/sucky_fonts/     # Remove the specified font path from Xorg list of known font paths

To see a list of fonts known by Xorg use , from the  package.

## Fontconfig configuration
Fontconfig configuration is documented in the  man page.

Configuration can be done per-user through  (usually ), and globally with .  The settings in the per-user configuration have precedence over the global configuration.  Both these files use the same syntax.

Fontconfig gathers all its configurations in a central file ().  This file is replaced during Fontconfig updates and should not be edited.  Fontconfig-aware applications source this file to know available fonts and how they get rendered; simply restarting such applications is sufficient to load the new configuration.  This file is a conglomeration of rules from the global configuration (), the configured presets in , and the user configuration file ().  can be used to rebuild Fontconfig configuration, although changes will only be visible in newly launched applications.

Fontconfig configuration files use XML format and need these headers:

The configuration examples in this article omit these tags.

## Presets
There are presets installed in the directory . They can be enabled by creating symbolic links to them, both per-user and globally, as described in . These presets will override matching settings in their respective configuration files.

For example, to enable sub-pixel RGB rendering globally:

 # ln -s /usr/share/fontconfig/conf.avail/10-sub-pixel-rgb.conf /etc/fonts/conf.d/

To do the same but instead for a per-user configuration:

 $ mkdir $XDG_CONFIG_HOME/fontconfig/conf.d
 $ ln -s /usr/share/fontconfig/conf.avail/10-sub-pixel-rgb.conf $XDG_CONFIG_HOME/fontconfig/conf.d/

## Anti-aliasing
Font rasterization converts vector font data to bitmap data so that it can be displayed. The result can appear jagged due to aliasing. Anti-aliasing can be used to increase the apparent resolution of font edges. Anti-aliasing is enabled by default. To disable it:

## Hinting
Font hinting (also known as instructing) is the use of mathematical instructions to adjust the display of an outline font so that it lines up with a rasterized grid (i.e. the pixel grid of the display). Its intended effect is to make fonts appear more crisp so that they are more readable. Fonts will line up correctly without hinting when displays have around 300 DPI.

## Byte-Code Interpreter (BCI)
Using BCI hinting, instructions in TrueType fonts are rendered according to FreeTypes's interpreter. BCI hinting works well with fonts with good hinting instructions. Hinting is enabled by default. To disable it:

## Autohinter
The autohinter attempts to do automatic hinting, disregarding any hinting information embedded in the font. Originally, it was the default because TrueType2 fonts were patent-protected, but now that these patents have expired, there is very little reason to use it. It does work better with fonts that have broken or no hinting information, but it will be strongly sub-optimal for fonts with good hinting information. Generally, common fonts are of the latter kind, so the autohinter will not be useful. The autohinter is disabled by default. To enable it:

## Hintstyle
Hintstyle is the amount of font reshaping done to line up to the grid. Hinting values are: , , , and .  will make the font more fuzzy to line up to the grid but will be better in retaining font shape (see while  will be a crisp font that aligns well to the pixel grid but will lose a greater amount of font shape.  implicitly uses the autohinter in a vertical-only mode in favor of font-native information for non-CFF (.otf) fonts.

 is the default setting. To change it:

## Subpixel layout
Fontconfig will need to know your subpixel layout to be able to display your fonts correctly. Use the [http://www.lagom.nl/lcd-test/subpixel.php Subpixel layout monitor test (part of The Lagom LCD monitor test pages) to find out your subpixel arrangement.

Subpixel geometry is configured via the  property, which could be either:

*  — red, green, blue — most common, is used by the most monitors manufactured today
*
*  — vertical
*
*  — no subpixel rendering

There is no support for unusual subpixel layouts such as "Pentile" and "RGBY", occasionally found on TV, OLED and mobile screens. For these devices, it is best to give up subpixel rendering and rely on greyscale by using the  option.

## Subpixel rendering
Subpixel rendering is a technique to improve sharpness of font rendering by effectively tripling the horizontal (or vertical) resolution through the use of subpixels. On Windows machines, this technique is called ClearType.

FreeType2 provides two different types of subpixel rendering, called Harmony and ClearType. The ClearType subpixel rendering is enabled by default.

An LCD filter is recommended when ClearType subpixel rendering is enabled. The Harmony subpixel rendering does not require setting an LCD filter and with default LCD geometry, it is equivalent to ClearType with the  filter See the following section on how to enable an LCD filter and its benefits.

## LCD filter
When using ClearType subpixel rendering, you should enable the LCD filter, which is designed to reduce color fringing.  This is described under [https://www.freetype.org/freetype2/docs/reference/ft2-lcd_rendering.html LCD filtering in the FreeType 2 API reference.  Different options are described under FT_LcdFilter, and are illustrated by this LCD filter test page.

The  filter will work for most users. Other filters are available that can be used in special situations: ; a lighter filter ideal for fonts that look too bold or fuzzy, , the original Cairo filter; and  to disable it entirely.

## Advanced LCD filter specification
If the available built-in LCD filters are not satisfactory, it is possible to tweak the font rendering very specifically by building a custom freetype2 package and modifying the hardcoded filters. The Arch build system can be used to build and install packages from source.

Checkout the  PKGBUILD and download/extract the build files. Arch build system#Retrieve PKGBUILD source lists  some of the methods.

Enable ClearType subpixel rendering by editing the file  and uncommenting the  macro.

Then, edit the file  and look up the definition of the constant :

  static const FT_LcdFiveTapFilter  default_weights =
     { 0x10, 0x40, 0x70, 0x40, 0x10 };

This constant defines a low-pass filter applied to the rendered glyph. Modify it as needed. (reference: freetype list discussion) Save the file, build and install the custom package:

 $ makepkg --noextract
 # pacman --remove --nodeps freetype2
 # pacman --upgrade freetype2-VERSION-ARCH.pkg.tar.zstd

Restart X. The lcddefault filter should now render fonts differently.

## Custom settings for certain fonts or font styles
Some fonts may not look good with BCI hinting. It can be disabled for just those fonts:

 ...

         My Font

         false

 ...

## Set default or fallback fonts
## Match tests
A reliable way to set a default or fallback font is to add an XML fragment to perform a match test. With the "binding" attribute, for example, the following setting will fall back to Gentium in place of Georgia:

In the above, the "compare" attribute can be "eq" (i.e., exactly equal to Georgia), "contains" (e.g., matching either Georgia or Georgia Pro), or other values. See .

## Alias
An alternate approach is to use ' to set the "preferred" font. Fonts matching the ' element are edited to prepend the list of 'ed families before the matching '. The following example will fall back to Bitstream Vera Sans when Helvetica is called:

' can also be used to specify fallback fonts when some glyphs are missing. For example, most versions of Helvetica Neue do not include Greek characters. A user might have Helvetica Neue installed and want to use it for Latin characters, and fall back to FreeSans for Greek characters due to its similarity to Helvetica''. The following will allow this to be achieved:

The above is not needed if the user simply wants to fall back to default fonts whenever glyphs are missing.

## Whitelisting and blacklisting fonts
The element  is used in conjunction with the  and  elements to selectively whitelist or blacklist fonts from the resolve list and match requests. The simplest and most typical use case is to reject a font that the user needs installed, but is getting matched for a generic font query that is causing problems with user interfaces.

First, obtain the Family name as listed in the font itself:

{{hc|1=$ fc-scan .fonts/lklug.ttf --format='%{family}\n'|2=
LKLUG
}}

Then, use that Family name in a  stanza:

Typically, when both elements are combined,  is first used on a more general matching glob to reject a large group (such as a whole directory), then  is used after it to whitelist individual fonts out of the larger blacklisted group.

## Disable bitmap fonts
Bitmap fonts are sometimes used as fallbacks for missing fonts, which may cause text to be rendered pixelated or too large. Use the  preset to disable this behavior.

To disable embedded bitmap for all fonts:

To disable embedded bitmap fonts for a specific font:

     Monaco

     false

If embedded bitmaps are disabled for all fonts, they can still be enabled for a specific font in case it does not function without embedded bitmaps. E.g. for Noto Color Emoji:

## Disable scaling of bitmap fonts
To disable scaling of bitmap fonts (which often makes them blurry), remove .
Note this can break the scaling of emoji fonts such as Segoe UI Emoji, making them huge.

To re-enable scaling of bitmap fonts, re-create the symbolic link:

 # ln -s /usr/share/fontconfig/conf.avail/10-scale-bitmap-fonts.conf /etc/fonts/conf.d/

## Create bold and italic styles for incomplete fonts
FreeType has the ability to automatically create italic and bold styles for fonts that do not have them, but only if explicitly required by the application. Given programs rarely send these requests, this section covers manually forcing generation of missing styles.

Start by editing  as explained below. Store a copy of the modifications on another file, because a font update with  will overwrite .

Assuming the Dupree font is installed:

 "dupree.ttf" 0 "Dupree:style=Regular:slant=0:weight=80:width=100:foundry=unknown:index=0:outline=True:etc...

Duplicate the line, change  to  or any other style. Also change  to  for italic,  to  for bold, or combine them for ''bold italic'':

 "dupree.ttf" 0 "Dupree:style=Bold Italic:slant=100:weight=200:width=100:foundry=unknown:index=0:outline=True:etc...

Now add necessary modifications to :

## Rule priority
Fontconfig processes files in  in numerical order. Therefore, the rules of  and  will have the same effect as a single  file first containing the rules of  then the ones of .

Usually, that means the files with the smaller prefix will have higher precedence. However, the Fontconfig syntax is flexible and allows a new rule to take precedence over an existing rule. Therefore, it is recommended to #Query the current settings to test the result of the rule interactions.

Note that the user's rules defined in  and in the directory  are loaded via the file  and typically take precedence over the rules defined in files starting with a higher number.

## Query the current settings
To find out what settings are in effect, use . eg.

Look up the meaning of the numbers at  Eg. 'hintstyle: 3' means 'hintfull'

## Applications without Fontconfig support
Some applications like URxvt will ignore Fontconfig settings. You can work around this by using , but it is not as flexible as Fontconfig. Example (see #Fontconfig configuration for explanations of the options):

Make sure the settings are loaded properly when X starts with  (see X resources for more information).

## Troubleshooting
## Distorted fonts
See HiDPI for instructions on handling high or mixed DPI displays: using a DPI setting which is not matching the physical hardware can lead to fuzzy font display.

## Calibri, Cambria, Monaco, etc. not rendering properly
Some scalable fonts have embedded bitmap versions which are rendered instead, mainly at smaller sizes. Using Metric-compatible fonts as replacements can improve the rendering in these cases.

You can also force using scalable fonts at all sizes by disabling embedded bitmap, sacrificing some rendering quality.

## Applications overriding hinting
Some applications or desktop environments may override default Fontconfig hinting and anti-aliasing settings. This may happen with GNOME 3, for example while you are using Qt applications like  or . Use the specific configuration program for the application in such cases. For GNOME, try .

## Applications not picking up hinting from GNOME settings
For instance, under GNOME it sometimes happens that Firefox applies full hinting even when it is set to "none" in GNOME's settings, which results in sharp and widened fonts. In this case you would have to add hinting settings to your  file:

In this example, hinting is set to .

## Incorrect hinting in GTK applications
In some desktop environments, especially outside GNOME and Plasma, some GTK applications could not read font configuration properly. In order to solve this issue, install  or  and execute it at every system startup. See also Xsettingsd and xsettingsd wiki for more information. It can be configured with the following common configuration:

If that is not working in some other applications, you could install  and provide the following configuration:

Then you can execute the script  at every system startup to apply the options. See also X resources and #Applications without Fontconfig support.

## Hinting in GTK4 programs
GTK4 and libadwaita programs ignore font hinting settings. To remedy this, create or modify the following configuration:

See also GTK documentation, GTK issue 3787, and this related note.

## Helvetica font problem in generated PDFs
If the following command

 fc-match helvetica

produces

 helvR12-ISO8859-1.pcf.gz: "Helvetica" "Regular"

then the bitmap font provided by  is likely to be embedded into PDFs generated by "Print to File" or "Export" in various applications. The bitmap font was probably installed as a consequence of installing the whole  group (which is usually NOT recommended). To solve the pixelized font problem, you can uninstall the package. Install  (Type 1) or  (OpenType) for corresponding free substitute of Helvetica (and other PostScript/PDF base fonts).

You may also experience similar problem when you open a PDF which requires Helvetica but does not have it embedded for viewing.

## FreeType breaking bitmap fonts
Some users are reporting problems () with bitmap fonts having changed names after upgrading  to version 2.7.1, creating havoc in terminal emulators and several other programs such as dwm or dmenu by falling back to another (different) font. This was caused by the changes to the PCF font family format, which is described in their release notes Users transitioning from the old format might want to create a font alias to remedy the problems, like the solution which is described in [https://forum.manjaro.org/t/terminus-font-name-fix-after-freetype2-update-to-2-7-1-1/15530, given here too:

Assume we want to create an alias for , which was renamed from  to  in the previously described  update:

* Create a configuration file in  for the font alias:

* Create a symbolic link towards it in the  directory. In our example we would link as follows:  to make the change permanent.
Everything should now work as it did before the update, the font alias should not be in effect, but make sure to either reload  or restart the display server first so the affected programs can use the alias.

## Underscores not rendered with DejaVu Monospace
Since Pango 1.44, the underscore characters disappear with certain font sizes when using the DejaVu Sans Mono font. A workaround is to use Liberation Mono as the monospace font, see #Set default or fallback fonts.

## Debugging FreeType fonts
 provides tools for debugging FreeType font configuration.  is a GUI in which you can tweak font rendering settings with a live preview. For example:

 $ ftview -e unic -d 1024x768x24 -r 96 10 /usr/share/fonts/noto/NotoSans-Regular.ttf

## Text is blurry
Some applications (e.g. Chromium/Electron) do not apply gamma correction properly, some have it disabled on certain scenarios (grayscale) which cause small text on dark background to be blurry and unreadable text on <=1080p screens. It is a long standing issue for Chromium/Electron, a workaround is to enable stem darkerning with the  environment variable.

## font-config-info
You can gather your effective font configuration with . It queries information from several GTK sources, X resources, XSETTINGS protocol and .
