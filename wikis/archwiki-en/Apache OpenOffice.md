# Apache OpenOffice

From Why Apache OpenOffice:

:Apache OpenOffice is the leading open-source office software suite for word processing, spreadsheets, presentations, graphics, databases and more. It is available in many languages and works on all common computers. It stores all your data in an international open standard format and can also read and write files from other common office software packages. It can be downloaded and used completely free of charge for any purpose.

## Installation
Install the  package or compile it from source. It is recommended to also install Java.

## Microsoft fonts
Official Microsoft fonts are useful to prevent pagination problems. Check the Microsoft fonts wiki page.

## Extension management and spell checking
The Arch package is now shipped with some dictionaries. Check Extension manager if your language is already there simply by loading up any OpenOffice program (Writer for example) and access the Extension Manager from the Tools menu. From there enter the following location to install a spell check dictionary:

 /usr/lib/openoffice/share/extension/install/

Alternatively, there are several ways to accomplish this:

* Use the Extension manager from OpenOffice menu for download and installation - installs only for the user into their
* Download the extension and install it using  for the user
* Download the extension and install it using  for every user on the system (requires root permission)

## Spellchecker
For spellchecking you will need  and dictionary for hunspell (like , , etc), for hyphenation rules you will need  (, , etc) and for a thesaurus, .

## Other extensions installed by default
* pdfimport.oxt - Ability to import PDF files in Draw and Impress
* presenter-screen.oxt - When using two displays this plugin provides more control over slideshow
* sun-presentation-minimizer.oxt - Reduce file size of current presentation
* wiki-publisher.oxt - Allows to create Wiki articles on MediaWiki servers without having to know the syntax of the MediaWiki markup language

## Installing macros
In most Linux distributions, the default path for macros is:
 ~/.openoffice.org/3/user/Scripts/
The path for this directory in Arch Linux is:
 ~/.config/.openoffice.org/3/user/Scripts/
Macros are not guaranted to work in both OpenOffice and LibreOffice, but it is possible to choose a common directory for them. Choose the path in Tools > Options > LibreOffice/OpenOffice > Paths
The default path for LibreOffice macros in Arch Linux is:
 ~/.config/libreoffice/4/user/Scripts/

## Install TrueType fonts
To add fonts to those already available in OpenOffice, run .

## Theme
OpenOffice supports to use several toolkits for drawing and integrates into different desktop environments in a clean way. To choose by hand, you need to set the  environment variable. Its possible values are gnome and kde4.

To configure the look for anytime OpenOffice gets started, you can export the  variable in , or in .
Alternatively you can put the variable in any OpenOffice desktop file in  line between  and the command, then copy them to  in order to prevent overwriting on update.

## KDE4/Qt4 look and feel
Check Uniform look for Qt and GTK applications for a broad application, general tips and other methods to achieve it.

## Use different configuration from general theme
Do not select Use my KDE style in GTK applications. Instead choose a native syle and font for GTK 2 applications.

Use a program like  to select a style (in general different from KDE) and a font (may be the same as your KDE general system font). There are also other GTK engine packages available.

There are two relevant parts of the OpenOffice options dialog, View and Fonts:
* View
** Set scale to 100%
** Set use system font OFF (otherwise replacement table will not be used)
** Set antialiasing OFF

* Fonts
** Select Use replacement table
** Replace Andale Sans UI (you must type this in -- it is not in the drop down list) with another font (your KDE system font or another if this looks bad)
** Press the tick symbol to update the list
** Select Always and Screen only
** Press OK

When choosing fonts for OpenOffice note that the poor font rendering engine included in the package may not render a particular font in the same way as other applications on the desktop.

## Speed up OpenOffice
Some settings may improve OpenOffice's loading time and responsiveness. However, some also increase RAM usage, so use them carefully. They can all be accessed under Tools > Options.
* Under Memory:
** Reduce the number of Undo > Number of steps to a figure lower than 100, to something like 40 or 50 steps
** Under Graphics cache, set Use for OpenOffice to 128 MB (up from the original 20MB).
** Set Memory per object to 20MB (up from the default 5MB)
** If you use OpenOffice often, check OpenOffice Quickstarter
* Under Java, uncheck Use a Java runtime environment

## Tips and tricks
## Automated document conversion
Document conversion can also be done by the command line tool , which is a python  automated conversion and styling tool that uses OpenOffice remote access capabilities. Even though it is no longer maintained, as of 2026Q1 it is still very useful. It either starts an OpenOffice instance for its own usage, or connects to an already  running instance. No graphical environment is required for its work.

## Troubleshooting
## Font substitution
These settings can be changed in the OpenOffice options. From the drop-down menu, select Tools > Options > OpenOffice > Fonts. Check the box that says Apply Replacement Table. Type  in the font box and choose your desired font for the Replace with option. When done, click the checkmark. Then choose the Always and Screen only options in the box below. Click OK.
You will then need to go to Tools > Options > OpenOffice > View, and uncheck Use system font for user interface. If you use a non-antialised font, such as Arial, you will also need to uncheck Screen font antialiasing before menu fonts render correctly.

## Anti-aliasing
Execute:
 $ echo "Xft.lcdfilter: lcddefault" | xrdb -merge

To make the change persistent, add  to your  fileIf this does not work, make sure you are running  every time you launch Xorg. If you do not have this file, you will have to create it.

## Spell checking problems
As of OpenOffice 3.0.0-2, various dictionaries may be buggy due to a character encoding problem. To solve this issue, follow the following instructions.

Find where the particular openoffice distribution places its dictionary files; e.g., . Most distibutions follow the convention of installing these to . Once the directory has been found, assign it to a shell variable:
 droot="/usr/lib/openoffice/share/extension/install"

Install  and  packages in order to be able to extract and compress the dictionary files.

For reference, get a list of languages whose dictionary files are packaged with the base distribution:
 cd "$droot" && ls | sed -rn 's,^dict-(..)\.oxt$,\1,p'

Define a list of languages whose dictionary files are to be fixed:
 lang="en es"

Extract the target languages' dictionary files and convert the erroneous encoding to UTF-8:

Finally, use the OpenOffice extension manager (available through the Tools menu) to install the dictionary from the resulting  file(s).

## Dark GTK themes, icons and GTK-Qt Engine
Older OpenOffice/LibreOffice versions would start in High Contrast Mode if you use dark GTK themes. This might prevent you from changing High Contrast Icons or Calc cell background coloring is completely disabled.

In newer version of OpenOffice / LibreOffice ( > 3.2.x), possible solutions may be:

* You could manually configure UI colors via Tools > Options > Appearance, yet Impress and Calc may stay dark.
* Another solution is to disable Automatically detect high-contrast mode of operation system in LibreOffice > Accessibility (> LO 4.1.x).

Now the colors can be configured in Options > Appearance and the selection of another iconset is possible again.

## Hanging when using NFSv3 shares
If OpenOffice hangs when trying to open/save a document located on a NFSv3 share, try prepending the following lines with a  in .:

 SAL_ENABLE_FILE_LOCKING=1
 export SAL_ENABLE_FILE_LOCKING

If you wish to avoid  overwriting on update just copy it in .
Original post [https://web.archive.org/web/20120910162208/http://www.crazysquirrel.com/computing/debian/bugs/openoffice-over-nfs.jspx here.

## Fixing Java framework error
You may get the following error when you try to run OpenOffice:

 framework Error in function createSettingsDocument (elements.cxx).
 javaldx failed!

If so, give yourself ownership of  like so:
 # chown -vR username:users ~/.config

Post on Arch Linux Forums.

## OpenOffice does not detect my certificates
If you cannot see the certificates when trying to sign a document, you will need to have the certificates configured in Firefox (or Thunderbird). If after that OpenOffice still does not show them, set the  environment variable pointing to your Firefox (or Thunderbird) folder.

 export MOZILLA_CERTIFICATE_FOLDER=$HOME/.mozilla/firefox/XXXXXX.default/

See more about certificate detection.
