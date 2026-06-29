# Java Runtime Environment fonts

Some users may find the default Java fonts or the display mode of fonts in Java applications to be unpleasant. Several methods to improve the font display in the Java Runtime Environment (JRE) are available. These methods may be used separately, but many users will find they achieve better results by combining them.

TrueType fonts appear to be the best supported format for use with Java.

## Anti-aliasing
Anti-aliasing of fonts is available with Oracle Java 1.6 and OpenJDK on Linux.

## Running an xsettings daemon
Java tries to get the system defaults through xsettings. On GNOME you do not have to do anything,  is already running. Otherwise Xsettingsd is a lightweight alternative.

## Overriding the automatically picked up settings
If you do not want to run an xsettings daemon, or the fonts still look ugly, there is also an environment variable to configure anti-aliasing:

 _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=setting

Where  is one of the values:

{| class="wikitable"
! Setting
! Description
|-
| , ,
| No anti-aliasing
|-
|
| Full anti-aliasing
|-
|
| Use the font's built-in hinting instructions
|-
| ,
| Anti-aliasing tuned for many popular LCD monitors
|-
| , ,
| Alternative LCD monitor setting
|}

The  and  settings work well in many instances.

To optionally to use GTK look and feel, add the following instead:

 _JAVA_OPTIONS='-Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel'

## Font selection
## TrueType fonts
Some Java applications may specify use of a particular TrueType font; these applications must be made aware of the directory path to the desired font. TrueType fonts are installed in the directory . Add the following environment variable:

 JAVA_FONTS=/usr/share/fonts/TTF

## Fixing tofu
Place font files in . Create it if needed.

Substitute the  for the  of the JRE you are actually using. Note that the feature is removed since Oracle Java 9, as Oracle considers it a bug to encourage users to change , moved the configuration files to  and called the fallback functionality a "mis-feature". The specific function providing this behavior is , and OpenJDK seems to still have it.

Doing so makes Java always add the fonts in this directory into the fallback sequence to look for character shapes (glyphs) in. This way, no matter what fonts the application has asked for, these additional fonts will provide the missing glyphs when needed.
