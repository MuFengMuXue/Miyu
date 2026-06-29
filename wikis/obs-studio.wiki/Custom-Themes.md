OBS Studio has the ability to load different themes based on your needs. The option is available in Settings -> General or Settings -> Appearance in OBS 30.2 and onwards.

The default themes included with OBS include:

* Yami - Current primary theme of OBS Studio, designed by [Warchamp7](https://obsproject.com/forum/members/warchamp7.1/)
* Acri - Designed by [Warchamp7](https://obsproject.com/forum/members/warchamp7.1/)
* Dark - The old theme since OBS 21.0
* Grey - A greyscale version of Yami
* Light - A light version of Yami
* Rachni - Designed by [Fenrir](https://obsproject.com/forum/members/fenrir.6800/)

The files for the default themes can be found in the OBS Studio installation directory, specifically /data/obs-studio/themes/

# Installing custom themes

The best place to install custom themes is in your user directory - the same place where profiles and scenes are stored, so that if you ever reinstall OBS Studio, you don't lose your custom themes.

* **Windows:** WinKey+R > %APPDATA%\obs-studio\themes\
* **macOS:** Cmd+Shift+G > ~/Library/Application Support/obs-studio/themes/
* **Linux:** ~/.config/obs-studio/themes/

**You may have to create the themes directory yourself.** 
You can find themes created by members of the community [at this link](https://obsproject.com/forum/resources/categories/themes.10/).

# Designing your own theme

Themes use a combination of something called QSS and a folder of custom images.

QSS is based on a subset of CSS2, and its documentation is all over the place. 
It's recommended to open one of the default themes and use it as a reference.

Documentation for QSS is split up quite heavily, but here are the links you will need:

* [The Style Sheet Syntax](http://doc.qt.io/qt/stylesheet-syntax.html) - covers the basics on how to write QSS
* [Qt Style Sheets Reference](http://doc.qt.io/qt/stylesheet-reference.html) - lengthy documentation on which widgets can be customized, and how, including pseudo-states and sub-controls


# OBS Composable Themes System

As of version 30.2 of OBS Studio, we have added a pre-processing step to QSS to add additional functionality to themes. Learn more about the [OBS Studio Theme System](https://github.com/obsproject/obs-studio/wiki/OBS-Studio-Theme-System)