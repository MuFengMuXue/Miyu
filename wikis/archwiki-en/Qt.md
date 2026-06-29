# Qt

Qt is a cross-platform application and widget toolkit that uses standard C++ but makes extensive use of a special code generator (called the Meta Object Compiler, or moc) together with several macros to enrich the language. Some of its more important features include:

* Running on the major desktop platforms and some of the mobile platforms.
* Extensive internationalization support.
* A complete library that provides SQL database access, XML parsing, thread management, network support, and a unified cross-platform application programming interface (API) for file handling.

The Qt framework is the basis of the KDE software community, as well as other important open source and proprietary applications such as VLC, VirtualBox, Mathematica and many others.

## Installation
Qt 6.x and 5.x are available in the official repositories. Legacy versions of Qt (4.x and 3.x) are available from the AUR. They can be installed with the following packages:

* Qt 6.x is available in the  package, with documentation in the  package.
* Qt 5.x is available in the  package, with documentation in the  package.
* Qt 4.x is available in the  package, with documentation in the  package.
* Qt 3.x is available in the  package, without documentation package.

## Default Qt toolkit
To define the default Qt toolkit, you can create the  environment variable. For example, to use Qt n, set .

## Configuration
## Styles in Qt 5
Qt 5 decides the style to use based on what desktop environment is used:

* In KDE Plasma, it uses the actually selected Qt style. It can be configured using KDE System Settings (systemsettings), the settings can be found in Appearance > Application Style > Widget Style.
* In Cinnamon, GNOME, MATE, LXDE, Xfce, it uses GTK (QGtkStyle).
* In other desktop environments, it uses Fusion.

To force a specific style, you can set the  environment variable. Specifically, set it to  if you want to use the GTK theme (Note: you will need to install the Qt style plugins mentioned below to get the GTK style). Qt 5 applications also support the  flag, which you can use to launch a Qt 5 application with a specific style.

The following styles are included in Qt 5: Fusion, Windows. Others can be installed separately:

*
*
*

*
*
*
*

## Qt Style Sheets
An interesting way of customizing the look and feel of a Qt application is using Style Sheets, which are just simple CSS files. Using Style Sheets, one can modify the appearance of every widget in the application.

To run an application with a different style just execute:

 $ qt_application -stylesheet style.qss

For more information on Qt Style Sheets see the official documentation or other tutorials. As an example Style Sheet see this Dolphin modification.

## GTK and Qt
If you have GTK and Qt applications, their looks might not exactly blend in very well. If you wish to make your GTK styles match your Qt styles please read Uniform look for Qt and GTK applications.

## Configuration of Qt 5/6 applications under environments other than KDE Plasma
Unlike Qt 4, Qt 5 does not ship a qtconfig utility to configure fonts, icons or styles. Instead, it will try to use the settings from the running desktop environment. In KDE Plasma or GNOME this works well, but in other less popular desktop environments or window managers it can lead to missing icons in Qt 5 applications. One way to solve this is to fake the running desktop environment by setting  or , and then using the corresponding configuration application to set the desired icon set.

Another solution is provided by the / packages, which provide a QPA independent of the desktop environment and a configuration utility. After installing package, run / to set an icon theme, and set the environment variable  so that the settings are picked up by Qt applications. Alternatively, use  as argument to the Qt 5 application.

 and  provide patched qt5ct/qt6ct with better integration to KDE applications, including KDE QML applications and can read and apply KColorSchemes.

If the errors below are received, and some icons still do not appear in some of the applications, install  and :

 Icon theme "oxygen" not found.
 Icon theme "oxygen" not found.
 Error: standard icon theme "oxygen" not found!

## Development
## Supported platforms
Qt supports most platforms that are available today, even some of the more obscure ones, with more ports appearing every once in a while. For a more complete list see the Qt Wikipedia article.

## Android
First of all, you need an Android SDK and NDK from AUR or using Android Studio.

SDK requires OpenJDK too. Different Qt versions have different version requirements, check here for detail.

Next you are going to need Qt 5 for Android. You can install it from AUR as described below or build it yourself, you can find build instructions on Qt wiki page.

In case of problems you may want to visit known issues.

*  - armeabi-v7a
*  - aarch64
*  - x86
*  - x86_64

Alternatively, you can use the official Qt installer.

## Tools
The following are official Qt tools:

*
:
*
*
*
*
*
*
*
*
*

## Troubleshooting
## Disable/Change Qt journal logging behaviour
When using KDE and/or any other Qt desktop environment debug info may be frequently logged in the systemd journal.

Set  as environment variable to change this behaviour, e.g. to completely disable logging:

To disable only debug logging, use .

## Icon theme is not applied
Since Qt 5.1 SVG support has moved into a module. Since  does not depend on  it may happen that the  is installed but not . This results in deceptive icon theme behaviour. Since SVG is not supported the icons are silently skipped and the icon theme may seem to be unused. Installing  solves the problem.

## Theme not applied to root applications
As the user theme file (), are not read by other accounts, the selected theme will not apply to X applications run as root. Possible solutions include:

* Create symlinks, e.g
* Configure system-wide theme file:
* Adjust the theme as root

## Qt 4 style not respected
If pure Qt 4 (non-KDE) applications do not stick with your selected Qt 4 style, then you will probably need to tell Qt 4 how to find KDE's styles (Oxygen, Phase etc.). You just need to set the environment variable . E.g.:

 QT_PLUGIN_PATH=$HOME/.kde4/lib/kde4/plugins/:/usr/lib/kde4/plugins/

 should then be able to find your kde styles and everything should look nice again!

Alternatively, you can symlink the Qt 4 styles directory to the KDE4 styles one:

 # ln -s /usr/lib/{kde,qt}4/plugins/styles/theme_name

## All Qt 5-based applications fail to run after Qt 5 update
If you get an error similar to

 Qt FATAL: Cannot mix incompatible Qt library (version 0x50900) with this library (version 0x50901)

then you are most likely using a Qt 5 platform theme or style plugin which has not been recompiled against the latest version of Qt 5. These usually use Qt private headers which means they depend on an exact version of Qt and not just a matching soname. Figure out which theme/style you are using by checking the  and  environment variables, and rebuild the AUR package that provides it.

## QXcbConnection: XCB error: 2 (BadValue)
Create a file with such content === Graphics misaligned or scaled improperly ===

See HiDPI#Qt 5.

## Dead keys not working for Qt apps
If you have set the right keyboard configuration and dead keys are working in GTK apps (or other widget toolkits) but not in KDE or any Qt apps, then you might not have the proper compose file loaded in your Xorg session.

A way to confirm that is to:

# launch a Qt app with  logging rule enabled, eg. launching :
# then try to write a character using a dead key, eg.  for  (LATIN SMALL LETTER E WITH CIRCUMFLEX)
# if you encounter  then you probably have this issue.

To fix this, first identify your locale. Then, if your locale doesn't have its own folder in , eg. , look for it in the  mapping file to find the corresponding compose file (eg. ):

Now create or edit  to include this compose file:

Finally, restart your Qt app, dead keys should be working and  error should have disappeared whenever you debug with .

## File dialog are very slow and crash the related application
The  file has been filled with garbage data and weighs hundreds of MiB: remove it. [https://bbs.archlinux.org/viewtopic.php?id=283703=== Qt 6.7 under Wayland sometimes ignore input method ===

Qt introduced text-input-v3 for Wayland platform. However, the implementation is not perfect and may cause serious issues preventing the usage of input method.

Set the following environment variable globally if your Wayland compositor supports text-input-v2:

## Emojis render as black and white despite a color emoji font being installed
Qt does not support automatically looking up the best font for emojis, and therefore the user must manually add a color emoji font as a fallback. [https://discussion.fedoraproject.org/t/qt-based-apps-use-low-quality-black-and-white-emoji/81017

To do this, save the contents of this gist to . This adds  as a fallback, though "Noto Color Emoji" can be replaced with a different font family if the user desires.

Afterwards, relaunch the Qt applications affected to load the new font settings.

## Crash or wrong scaling under Wayland
Some Qt apps, like , crash or suffer scaling issues [https://gitlab.archlinux.org/archlinux/packaging/packages/keepassxc/-/issues/7 on Wayland.

To fix that, install  as explained in Wayland#Qt.

## KDE Global Menu not working
Some Qt 5 applications like , fails to use the Global Menu of KDE To fix it, install  as explained in KDE#Plasma 6 Global Menu not working with some applications.

Qt 6 applications should not pose a problem since  is pulled by .
