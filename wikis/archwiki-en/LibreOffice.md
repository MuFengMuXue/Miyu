# LibreOffice

From LibreOffice website:

:LibreOffice is a powerful, free and private office suite - the successor project to OpenOffice - used by millions of people around the world. It's compatible with Microsoft Office (365) and is backed by a non-profit organisation, The Document Foundation. LibreOffice includes Writer (word processing), Calc (spreadsheets), Impress (presentations), Draw (vector graphics and flowcharts), Base (databases), and Math (formula editing).== Installation ==

Install one of the following packages:

*  is the stable maintenance branch with relatively rare updates, for conservative users.
*  is the feature branch, with new program enhancements for early adopters or power users.

LibreOffice will be installed with an English user interface. Should a different language be desired, the appropriate language pack has to be installed; for example,  for the French language pack.

After starting or restarting LibreOffice, the user interface should be the same as the system language; if it isn't, either the wrong language pack was installed or it has to be manually set. See [https://help.libreoffice.org/latest/en-US/text/shared/optionen/01140000.html help.libreoffice.org for additional information.

Check the optional dependencies pacman displays. If HSQLDB Embedded is in use for LibreOffice Base, you must install a Java Runtime Environment. You may need  to use some modules in LibreOffice Base.

## Theme
LibreOffice includes support for GTK and Qt theme integration. See also Uniform look for Qt and GTK applications.

LibreOffice will try to auto detect the most suitable VCL interface based on your desktop environment. To force the use of a certain VCL interface, e.g. "gtk4" set the environment variables . For more user interface options see  or , where the variables are listed and can be uncommented.

Log out and back in for the changes to take effect.

## Extension management
The following additional extensions are available:

* , which can create LaTeX mathematical equations (as PNG or SVG images) inside Writer, Impress, and Draw * , which can convert Writer documents to LaTeX files [https://writer2latex.sourceforge.net/

For more extensions, check the AUR, the built-in LibreOffice Extension manager, or libreplanet.

## Fonts
The Document Foundation wiki mentions various fonts that are packaged by default with LibreOffice on Windows and macOS. On Arch, the following packages may be installed for the fonts:

*
*
*
*
*
*
*
*
*
*

Also see Fonts#Font packages.

## Language aids
## Spell checking
For spell checking, make sure hunspell and a language dictionary for it are installed. Then enable the Writing aids by selecting the check-box in Tools > Options > Language Settings > Writing Aids > Hunspell SpellChecker after restarting LibreOffice.

;Finnish
Unlike other languages, Finnish spellchecking and grammar checking are based on Voikko. For LibreOffice  should be installed.

;Greek
Project Orthos provides more complete Greek spell checkers as Libreoffice extensions. Package  provides a Greek-only spelling dictionary, while  provides one that bundles Greek and US English.

## Bidirectional support
To enable Bidi support, select the check-box for Complex Text Layout (CTL) from: Tools > Options... > Languages and Locales > General > Default Languages for Documents, then choose the appropriate language. Language alignment can then be forced by RCtrl + RShift and LCtrl + LShift. There's a known issue that switches text direction when paragraph style changes.

## Hyphenation rules
For hyphenation rules, you will need  and a language hyphen rule set ( for English,  for German, etc).

## Thesaurus
For the thesaurus option, you will need  and a mythes language thesaurus (like  for English,  for German, etc).

;Greek
For Greek, instead of  you may want to try out , which includes more words.

## Grammar checking with LanguageTool
For grammar checking, several tools are available. The most common is . Instructions on how to use it depend on which version of LibreOffice you have.

Since version 7.4, LibreOffice supports LanguageTool natively, no extensions are needed:

# Click on Tools > Options... > Language and Locales > LanguageTool Server.
# Enable LanguageTool by selecting the check-box.
# The URL to use depends on whether you have a remote account (free or premium), or are running a local server:
#* If you have a remote free account, use . Leave the other two text fields blank.
#* If you have a remote premium account, use  as "Base URL", write your email address, and type in the API key.
#* If you have set up a local LanguageTool server, use  as "Base URL". Leave User name and API Key empty.
# Click OK, and open a Writer document if one is not already open.
# Select the check-box Tools > Automatic Spell Checking.

WritingTool offers writing assistance with spelling and grammar (powered by LanguageTool), statistical analysis and AI support: .

See LanguageTool page for more information.

## Offline help
 and  provide the offline help files for en-US. Help files for different locales is provided by the appropriate libreoffice language package, (i.e.,  provides the help files for en-ZA locales).

## Tips and tricks
## Speed up startup
* Disable startup logo: If you prefer to disable the startup logo screen with loading progress, open , find the  line and set it to . Alternatively, use the  CLI option.
* Disable Java Runtime: If you are not using features that rely on Java, consider disabling the Java runtime. Go to Tools > Options > LibreOffice > Advanced and uncheck Use a Java runtime environment.
* Turn off AutoSpellcheck: in Tools > Options > Languages and Locales > Writing Aids uncheck Check spelling as you type and Check grammar as you type.

## Installing macros
If you intend to use macros, you must have a Java Runtime Environment enabled.

The default path for macros in Arch Linux is different from most Linux distributions. Its location is: .

## Base as a database frontend
Base can be used as a frontend to a database like PostgreSQL. It cannot edit the tables but It gives a very nice overview of the columns and rows of a table with the possibility of hiding columns for better overview of the relevant data. It can also filter the data and enables deletion of multiple rows by selecting them and easy editing of single cells.

It can also help construct SQL queries with the help of a query GUI.

## Automated document conversion based on LibreOffice or OpenOffice
Document conversion can be done by libreoffice directly if called with the  command line option. For example, to convert a  into  file, you can issue:

 $ libreoffice --headless --convert-to pdf ./*.odt

One can also

 $ libreoffice --cat ./*.odt

Both of these commands can not open password protected documents. They also require work around when old school window managers are usedAnother option, which does not work with OpenOffice, is the  command line tool, and its companion tool , from the  package.  is an automated conversion and styling tool that, by its  companion, uses LibreOffice remote access capabilities. The package also has a  and  tools. As of LibreOffice 26, circa February 2026, these tools replaced the previous  command[https://gitlab.archlinux.org/archlinux/packaging/packages/unoconv/-/issues/1. Some of the differences between  and  is their outputand the fact that  does work with OpenOffice. There are more details at [https://github.com/unoconv/unoserver#comparison-with-unoconv Comparison with unoconv. There is no need for a graphical environment in order to use any of these tools. And they can open password protected documents.

## Notification sounds
Some user actions like closing LibreOffice with an unsaved document will bring up the "Save Document?" popup window together with a notification sound. Enabling/disabling notification sounds can be tried by changing the GTK configuration option , see GTK#Examples.

## Troubleshooting
A general way to track down problems is the safe mode in LibreOffice:

 $ libreoffice --safe-mode

## Font substitution
In case the document uses a font that is not installed in the system, LibreOffice will use an alternative font to render the document. This is called "font substitution".

LibreOffice uses fontconfig to resolve fonts.

To find out which font is the substitute for a missing font, you can issue:

 $ fc-match "My Font"

If the result is something like , it means the font is correctly installed. If the result is something different, it means that "My Font" is not installed and is being substituted by something else.

Note that LibreOffice will not issue any errors or messages when it substitutes a font with another. It just puts the name of the font on the toolbar in italics, which mean the font is missing and is being substituted.

Substitution proposed by fontconfig can be overridden with LibreOffice. To override a fontconfig substitution, proceed as follows.

From the drop-down menu, select Tools > Options > LibreOffice > Fonts. Check the box that says Apply Replacement Table. Type the name of your font, for example , in the font box and choose your desired font for the Replace with option. When done, click the checkmark. Then choose the Always and Screen only options in the box below. Click OK.

## Anti-aliasing
Execute:

 $ echo "Xft.lcdfilter: lcddefault" | xrdb -merge

To make the change persistent, add  to your  file, and make sure to run  (source). See X resources for more details.

If this does not work, you can also try adding  to your . If you do not have this file, you will have to create it.

## Hanging when using NFSv3 shares
If LibreOffice hangs when trying to open or save a document located on a NFSv3 share, try prepending the following lines with a  in :

 # file locking now enabled by default
 SAL_ENABLE_FILE_LOCKING=1
 export SAL_ENABLE_FILE_LOCKING

To avoid overwriting on update you can copy  in . Original post here.

## LibreOffice does not detect certificates
See the official documentation.

## Run .pps files in edit mode (without slideshow)
The only solution is to rename the  file to .

Add the following script to your home directory and use it to open every  file. Very useful to open  files received by email without the need to save them.

 #!/bin/sh
 f=$(mktemp --suffix .ppt)
 cp "$1" "${f}" && libreoffice "${f}" && rm -f "${f}"

## Media support
If embedded videos are just gray boxes, make sure to have installed the GStreamer plugins required.

## Default paper size in Writer and Draw
If the default paper size in blank Writer and Draw documents is persistently incorrect for your locale, try installing the  optional dependency and either updating  (for a system-wide change) or creating  (for a user change) with your preferred paper size. See  and .

## AutoText expected default behaviour not functional in system locales other than en_US
If expected default AutoText behaviour is not present (for example, typing  in a document in Writer and then pressing the  key does not result in the automatic insertion of a numbered function) when the system locale is not  you need to add the default  AutoText templates to your AutoText path. To do this, go to Tools > AutoText..., then click on Path... and add the following path to the list: . AutoText should now work as expected by default.

## LibreOffice freezes or crashes
Disable OpenCL and/or OpenGL by setting the environment variable  and/or . The LibreOffice safe mode also offers the option to disable both.

If LibreOffice is freezing or failing to start with the message "Application Error" but works fine when OpenCL is disabled, try installing an OpenCL runtime.

## Wayland and HiDPI
To work around issues with scaling UI elements in Wayland on HiDPI screens, try to specify a VCL interface (e.g.,  or ). See #Theme.

Multiple screens with different scaling are affected by a bug preventing proper scaling on all screens. As a workaround start LibreOffice in Xwayland-mode (e.g. ).

## kio-fuse and webdav
To ensure LibreOffice always falls back on  for remote files (instead of its internal webdav implementation and password store), remove  from the  key in all  files.

## KDE Plasma/GNOME + Wayland with or without fractional scaling results in terrible lag when scrolling
Users of KDE Plasma 6 and 5 and some users testing with GNOME have reported issues of terrible lag while scrolling through documents as reported in Running LibreOffice through X11 can solve the issue (There are [https://bugs.documentfoundation.org/show_bug.cgi?id=152911#c28 reports that the issue is not resolved in GNOME when using the GTK3 backend). This can be done individually by the setting the environment variable  while in KDE Plasma (QT) or  while in GNOME (GTK). Each .desktop file can be edited to permanently apply the change until a fix is found. Users can also switch back to X11 to mediate the issue.
