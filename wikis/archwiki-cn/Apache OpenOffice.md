**注意：** 官方支持已从 Apache OpenOffice 转向 [LibreOffice](<../zh-cn/LibreOffice.html> "LibreOffice")，这是该项目的“文档基金会”分支，其中还包括增强功能和附加功能。请参阅 [放弃 Oracle OpenOffice (arch-general)](<https://lists.archlinux.org/archives/list/arch-general@lists.archlinux.org/thread/ZLRIS3ET65QSNPTR4XHTQ2KY3H52MWZ6/>)。

来自[为什么选择 Apache OpenOffice](<https://why.openoffice.org/>)： 

    Apache OpenOffice 是领先的开源办公软件套件，用于文字处理、电子表格、演示文稿、图形、数据库等。它支持多种语言，并且可以在所有常见计算机上运行。它将所有数据存储在国际开放标准格式中，并且还可以读写其他常见办公软件包的文件。它可以免费下载并用于任何目的。

## Installation

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [openoffice-bin](<https://aur.archlinux.org/packages/openoffice-bin/>)AUR package or [compile it from source](<https://wiki.openoffice.org/wiki/Documentation/Building_Guide/Building_on_Linux>). It is recommended to also install [Java](<../zh-cn/Java.html> "Java"). 

### Microsoft fonts

Official Microsoft fonts are useful to prevent pagination problems. Check the [Microsoft fonts](<../zh-cn/Microsoft_fonts.html> "Microsoft fonts") wiki page. 

### Extension management and spell checking

The Arch package is now shipped with some dictionaries. Check _Extension manager_ if your language is already there simply by loading up any OpenOffice program (Writer for example) and access the _Extension Manager_ from the Tools menu. From there enter the following location to install a spell check dictionary: 
    
    /usr/lib/openoffice/share/extension/install/
    
**注意：** If you installed LibreOffice, the path will be `/usr/lib/libreoffice/share/extensions/` instead and extensions are currently all already known to the system.

Alternatively, there are several ways to accomplish this: 

  * Use the _Extension manager_ from OpenOffice menu for download and installation - installs only for the user into their `~/.openoffice.org/3/user/uno_packages/cache`
  * Download the extension and install it using `/usr/lib/openoffice/program/unopkg add extension` for the user
  * Download the extension and install it using `/usr/lib/openoffice/program/unopkg add --shared extension` for every user on the system (requires root permission)

#### Spellchecker

For spellchecking you will need [hunspell](<https://archlinux.org/packages/?name=hunspell>)包 and dictionary for hunspell (like [hunspell-en_us](<https://archlinux.org/packages/?name=hunspell-en_us>)包, [hunspell-de](<https://archlinux.org/packages/?name=hunspell-de>)包, etc), for hyphenation rules you will need [hyphen](<https://archlinux.org/packages/?name=hyphen>)包 ([hyphen-en](<https://archlinux.org/packages/?name=hyphen-en>)包, [hyphen-de](<https://archlinux.org/packages/?name=hyphen-de>)包, etc) and for a thesaurus, [libmythes](<https://archlinux.org/packages/?name=libmythes>)包. 

#### Other extensions installed by default

  * **pdfimport.oxt** \- Ability to import PDF files in Draw and Impress
  * **presenter-screen.oxt** \- When using two displays this plugin provides more control over slideshow
  * **sun-presentation-minimizer.oxt** \- Reduce file size of current presentation
  * **wiki-publisher.oxt** \- Allows to create Wiki articles on MediaWiki servers without having to know the syntax of the MediaWiki markup language

### Installing macros

In most Linux distributions, the default path for macros is: 
    
    ~/.openoffice.org/3/user/Scripts/
    
The path for this directory in Arch Linux is: 
    
    ~/.config/.openoffice.org/3/user/Scripts/
    
Macros are not guaranted to work in both OpenOffice and LibreOffice, but it is possible to choose a common directory for them. Choose the path in _Tools > Options > LibreOffice/OpenOffice > Paths_ The default path for LibreOffice macros in Arch Linux is: 
    
    ~/.config/libreoffice/4/user/Scripts/
    
**注意：** If you intend to use macros, you must have a Java Runtime Environment. This behavior is a default, but disabling it [speeds up](<#Speed_up_OpenOffice>) the loading time.

### Install TrueType fonts

To add fonts to those already available in OpenOffice, run `spadmin`. 

## Theme

OpenOffice supports to use several toolkits for drawing and integrates into different desktop environments in a clean way. To choose by hand, you need to set the `OOO_FORCE_DESKTOP` environment variable. Its possible values are _gnome_ and _kde4_. 

To configure the look for anytime OpenOffice gets started, you can export the `OOO_FORCE_DESKTOP` variable in `/etc/profile.d/openoffice.sh`, or in `/usr/bin/soffice`. Alternatively you can put the variable in any OpenOffice desktop file in `Exec` line between `Exec` and the command, then copy them to `$XDG_DATA_HOME/applications` in order to prevent overwriting on update. 

###  KDE4/Qt4 look and feel

Check [Uniform look for Qt and GTK applications](<../zh-cn/Uniform_look_for_Qt_and_GTK_applications.html> "Uniform look for Qt and GTK applications") for a broad application, general tips and other methods to achieve it. 

#### Use different configuration from general theme

Do **not** select _Use my KDE style in GTK applications_. Instead choose a native syle and font for GTK 2 applications. 

Use a program like [gtk-chtheme](<https://archlinux.org/packages/?name=gtk-chtheme>)包 to select a style (in general different from KDE) and a font (may be the same as your KDE general system font). There are also other GTK engine packages available. 

There are two relevant parts of the OpenOffice options dialog, _View_ and _Fonts_ : 

  * **View**
    * Set scale to 100%
    * Set use system font OFF (otherwise replacement table will not be used)
    * Set antialiasing OFF

  * **Fonts**
    * Select _Use replacement table_
    * Replace _Andale Sans UI_ (you **must** type this in -- it is not in the drop down list) with another font (your KDE system font or another if this looks bad)
    * Press the tick symbol to update the list
    * Select _Always_ and _Screen only_
    * Press _OK_

When choosing fonts for OpenOffice note that the poor font rendering engine included in the package may not render a particular font in the same way as other applications on the desktop. 

## Speed up OpenOffice

Some settings may improve OpenOffice's loading time and responsiveness. However, some also increase RAM usage, so use them carefully. They can all be accessed under _Tools > Options_. 

  * Under _Memory_ : 
    * Reduce the number of _Undo > Number of steps_ to a figure lower than 100, to something like 40 or 50 steps
    * Under _Graphics cache_ , set _Use for OpenOffice_ to 128 MB (up from the original 20MB).
    * Set _Memory per object_ to 20MB (up from the default 5MB)
    * If you use OpenOffice often, check _OpenOffice Quickstarter_
  * Under _Java_ , uncheck Use a Java runtime environment

**注意：** For a list of functionality which depends on OpenOffice Java support, see this page: <http://wiki.services.openoffice.org/wiki/Java>.

## Troubleshooting

### Font substitution

These settings can be changed in the OpenOffice options. From the drop-down menu, select _Tools > Options > OpenOffice > Fonts_. Check the box that says _Apply Replacement Table_. Type `Andale Sans UI` in the font box and choose your desired font for the _Replace with_ option. When done, click the _checkmark_. Then choose the _Always_ and _Screen only_ options in the box below. Click OK. You will then need to go to _Tools > Options > OpenOffice > View_, and uncheck _Use system font for user interface_. If you use a non-antialised font, such as Arial, you will also need to uncheck _Screen font antialiasing_ before menu fonts render correctly. 

### Anti-aliasing

Execute: 
    
    $ echo "Xft.lcdfilter: lcddefault" | xrdb -merge
    
To make the change persistent, add `Xft.lcdfilter: lcddefault` to your `~/.Xresources` file[[1]](<https://bugs.launchpad.net/ubuntu/+source/cairo/+bug/271283/comments/23>). 

If this does not work, make sure you are running `$ xrdb -merge ~/.Xresources` every time you launch [Xorg](<../zh-cn/Xorg.html> "Xorg"). If you do not have this file, you will have to create it. 

### Spell checking problems

As of OpenOffice 3.0.0-2, various dictionaries may be buggy due to a character encoding problem. To solve this issue, follow the following instructions. 

Find where the particular openoffice distribution places its dictionary files; e.g., `pacman -Ql openoffice-base`. Most distibutions follow the convention of installing these to `/usr/lib/openoffice/share/extension/install`. Once the directory has been found, assign it to a shell variable: 
    
    droot="/usr/lib/openoffice/share/extension/install"
    
Install [unzip](<https://archlinux.org/packages/?name=unzip>)包 and [zip](<https://archlinux.org/packages/?name=zip>)包 packages in order to be able to extract and compress the dictionary files. 

For reference, get a list of languages whose dictionary files are packaged with the base distribution: 
    
    cd "$droot" && ls | sed -rn 's,^dict-(..)\.oxt$,\1,p'
    
Define a list of languages whose dictionary files are to be fixed: 
    
    lang="en es"
    
Extract the target languages' dictionary files and convert the erroneous encoding to _UTF-8_ : 
    
    tmp="/tmp/dictfix-$USER-$$"
    
    mkdir "$tmp"
    cd "$tmp"
    
    for i in $lang; do
        i="$droot/dict-$i.oxt"
        unzip "$i" -d oxt.tmp
        iconv -f ISO-8859-15 -t UTF-8 oxt.tmp/dictionaries.xcu > dict.tmp
        mv dict.tmp oxt.tmp/dictionaries.xcu
        (cd oxt.tmp && zip -r "$i" .)
    done
    
    rm -rf "$tmp"

Finally, use the OpenOffice extension manager (available through the _Tools_ menu) to install the dictionary from the resulting `dict-_xx_.oxt` file(s). 

###  Dark GTK themes, icons and GTK-Qt Engine

Older OpenOffice/LibreOffice versions would start in _High Contrast Mode_ if you use dark [GTK](<../zh-cn/GTK.html> "GTK") themes. This might prevent you from changing _High Contrast Icons_ or Calc cell background coloring is completely disabled. 

In newer version of OpenOffice / LibreOffice ( > 3.2.x), possible solutions may be: 

  * You could manually configure UI colors via _Tools > Options > Appearance_, yet Impress and Calc may stay dark.
  * Another solution is to disable _Automatically detect high-contrast mode of operation system_ in _LibreOffice > Accessibility_ (> LO 4.1.x).

Now the colors can be configured in _Options > Appearance_ and the selection of another iconset is possible again. 

### Hanging when using NFSv3 shares

If OpenOffice hangs when trying to open/save a document located on a NFSv3 share, try prepending the following lines with a `#` in `/usr/lib/openoffice/program/soffice`.: 
    
    SAL_ENABLE_FILE_LOCKING=1
    export SAL_ENABLE_FILE_LOCKING
    
If you wish to avoid `/usr/lib/openoffice/program/soffice` overwriting on update just copy it in `/usr/local/bin`. Original post [here](<https://web.archive.org/web/20120910162208/http://www.crazysquirrel.com/computing/debian/bugs/openoffice-over-nfs.jspx>). 

### Fixing Java framework error

You may get the following error when you try to run OpenOffice: 
    
    [Java framework] Error in function createSettingsDocument (elements.cxx).
    javaldx failed!
    
If so, give yourself ownership of `~/.config/` like so: 
    
    # chown -vR username:users ~/.config
    
[Post on Arch Linux Forums.](<https://bbs.archlinux.org/viewtopic.php?id=93168>)

### OpenOffice does not detect my certificates

If you cannot see the certificates when trying to sign a document, you will need to have the certificates configured in Firefox (or Thunderbird). If after that OpenOffice still does not show them, set the `MOZILLA_CERTIFICATE_FOLDER` environment variable pointing to your Firefox (or Thunderbird) folder. 
    
    export MOZILLA_CERTIFICATE_FOLDER=$HOME/.mozilla/firefox/XXXXXX.default/
    
See more about [certificate detection](<https://wiki.openoffice.org/wiki/Certificate_Detection>). 
