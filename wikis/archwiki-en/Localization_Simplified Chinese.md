# Localization/Simplified Chinese

According to "The Arch Way": We cannot configure everything for you, because "Preferences and needs are different for everyone", but we will try to ensure the configuration to be convenient and simple. In fact, it is even easier than some Chinese versions of Linux.

This article provides Chinese cultural guidance for various common software as much as possible. But in practical applications, you may encounter all kinds of issues. Do not be discouraged when you are in trouble. Solving problems is a pleasure in itself. You can seek help through various platforms:

* Google and other search engines
* Arch official forum
* Ubuntu Chinese Forum Unix-like OS area
* IRC channel: #archlinux-cn

## Basic Chinese support
To properly display Chinese, you must set the locale correctly and install the appropriate Chinese fonts.

## locale settings
## Install Chinese locale
In Linux, locales are used to set up different environments for running programs. Commonly used Chinese locales are (the most intuitive is the number of words that can be displayed):

 zh_CN.GB2312
 zh_CN.GBK
 zh_CN.GB18030
 zh_CN.UTF-8
 zh_TW.BIG-5
 zh_TW.UTF-8

It is recommended to use UTF-8 locale. You need to modify  to set the locales that can be used in the system (erase the comment symbol "" before the corresponding item):

After executing , the selected locales can be used in the system. You may use  to view the currently used locale(s), and  to view the currently available locales.

## Enable Chinese locales
## Set the global default locale to English (optional)
To avoid the tty garbled text issue mentioned above, globally set the LANG locale to :

## User-specific locales
You may set your own user environment variables.

## Set Chinese locales for graphical interfaces
It is not recommended to set a global Chinese locale in  because it causes any tty to display garbled characters.

As mentioned earlier, Chinese locale can be set separately in startup files. Prepend the following two lines to one of the two files (if you are not sure which file to use, prepend to both):

 export LANG=zh_CN.UTF-8
 export LANGUAGE=zh_CN:en_US

## Chinese fonts
## Install fonts
In addition to locales, Chinese fonts are also required.

Commonly used free (GPL or compatible copyright) Chinese fonts include:

*
*
*
*
*
*
*
*
*

System fonts will be installed to  by default. If you do not have root authority or plan to use certain fonts yourself, you can directly copy these fonts to  (or its subdirectories) and add the path to . For details, go over the following chapters.

See also: ==== Chinese fonts configuration ====

## fontconfig settings
The setting file of fontconfig is  (user) or  (global). It is recommended to modify the former.

For Chinese fonts settings, see Fonts (简体中文) and Font configuration (简体中文).

Font Configuration (简体中文)/Chinese (简体中文) provides a demonstration of Chinese fontconfig.

See also:

* [http://www.chinalinuxpub.com/read.php?wid=634 fontconfig 用户手册
* Debian 中文支持
* Fontconfig wiki page

## Chinese characters displayed as variant (Japanese) glyphs
After installing Noto Sans CJK  (Source Han Sans, lit. Siyuan Bold), or Noto Serif CJK  (Source Han Serif, lit. Siyuan Song), in some cases (framework undefined area), rendered Chinese characters do not match the standard form, such as 门, 关, and 复.

This is because different default fonts can be set in each program, such as Arial or Tahoma, and the attributes of these fonts are controlled by fontconfig. The order of use is based on the regional code and the default order of A-Z. Since  is before {{ic|zh_{CN,HK,SG,TW}}}, Japanese fonts are used first.

You can use the following methods to solve the issue (taking simplified Chinese as an example):

* Make sure your desktop environment is using a correct locale setting. For example, KDE may misconfigure its own locale config file and you should fix that.
* Only install fonts that follows Simplified Chinese standard. For Noto CJK fonts this means to only install the CN variant, which are Noto Sans CJK CN and Noto Serif CJK CN,  and , or .
* Add  to  to set Simplified Chinese as the default language. Since the Locale is defined for CJK priority, the default priority is ignored.
* Manually adjust the priority so that the Chinese fonts are set before the Japanese fonts. Create a file under  or , such as , or modify or create  (only effective for the user):

If  is installed, write:

If you have installed :

Note that if you create an xml file under , for example:

 # ln -s /etc/fonts/conf.avail/64-language-selector-prefer.conf /etc/fonts/conf.d/64-language-selector-prefer.conf

you have to update the font cache to take effect:

 # fc-cache -fv

Execute the following command to check. If  appears, the settings are successfully applied:

 # fc-match -s | grep 'Noto Sans CJK'

## Chinese input method
Commonly used Chinese input method frameworks are IBus, fcitx5 and scim. For specific installation and configuration, please refer to the respective articles.

## Terminal Chinese support
## Boot loader Chinese support
See GRUB2 (简体中文).

## Cultural configuration in software
## Firefox
Simplified Chinese installation: 。

Traditional Chinese installation: 。

## Libreoffice
Simplified Chinese installation:  or .

Traditional Chinese installation:  or .

## PDF reader
Most PDF viewers already support Chinese. However, for -based readers and image processing tools that can handle PDF files,  needs to be installed.

## Java
For Sun Java users, create a  directory under , then link or copy several Chinese fonts to the directory to allow java programs to display Chinese correctly. For example, if  and  have been installed, use the following command:

 # ln -s /usr/share/fonts/TTF/odosung.ttc /opt/java/jre/lib/fonts/fallback/
 # cd /opt/java/jre/lib/fonts/fallback/
 # mkfontdir
 # mkfontscale

## vim
If the locale is utf8-encoded, using vim to open other Chinese encoded files may be garbled. The following settings need to be made in :

## Chinese video subtitles
## MPlayer
To allow MPlayer to display Chinese subtitles correctly, the key is to make sure the encoding of the subtitle file is consistent with the encoding used in mplayer's configurations. If the subtitle file is encoded as gbk, use ; If the subtitle file is encoded as utf-8, use . If the subtitle file is encoded as utf-8 and set to , some garbled characters will appear. Another simpler method is to set to , so that enca is responsible for the encoding and display of subtitles.

Modify :

Use the following command to manually load subtitles:

 $ mplayer xxxxx.avi -sub xxxxx.srt

If a graphical front end (such as SMPlayer) is used, it will work as long as you set the default subtitle encoding and font in the settings dialog box.

## xine
Xine can also display Chinese subtitles, but you need to make your own Chinese fonts. For details, please refer to [https://forum.ubuntu.org.cn/about2760.html.

## gstreamer
In totem 1.4.0, since gstreamer0.10 is used, it should be able to automatically load srt subtitles with the same name.

## LaTeX
You need to install CJK packages and the appropriate fonts. For details, please refer to == Garbled problem ==

The basic principle to avoid garbled characters is to use utf-8 instead of gbk/gb2312.

For troubleshooting instructions see Character encoding#Troubleshooting.

## Translation software
* : StarDict.
* : command line StarDict.
* : Youdao dictionary on the command line.
* : Youdao dictionary (graphic interface), screen word translation.
* GoldenDict: There is no dictionary by default, you can download the corresponding dictionary package (supports Babylon's thesaurus format , StarDict no longer maintained thesaurus format (///), dictd words Library format (/(), ABBYY Lingvo's thesaurus format (//), mdict's thesaurus format, etc. The thesaurus files of these dictionaries can be downloaded and imported on the Internet Use of GoldenDict (may have copyright issues).
* : A multi-platform Chinese dictionary. In addition to Chinese characters, words, idioms, etc., it also contains Hakka, Hokkien, simple foreign language translations, stroke order writing, etc. [https://www.moedict.tw/%E8%90%8C moedict online address
* : An online English-Chinese dictionary that gets results by crawling Youdao translation webpage, some support English-Chinese translation, imitating dmenu to display the results at the top of the screen. It is rather easy to use. The API used by  has expired, and the new API is free to use the frequency limit, so  is a good alternative.
