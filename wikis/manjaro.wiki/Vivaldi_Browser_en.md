[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Vivaldi+Browser&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Vivaldi_Browser "Vivaldi Browser (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Vivaldi_Browser/tr "Vivaldi Tarayıcı (12% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Vivaldi_Browser/ru "Браузер Vivaldi (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Vivaldi_Browser/fa "مرورگر ویوالدی (69% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installing Vivaldi]](#Installing_Vivaldi)
-   [[3] [Tips and Tricks]](#Tips_and_Tricks)
    -   [[3.1] [Access Additional Settings]](#Access_Additional_Settings)
    -   [[3.2] [Using the Native File Dialogs on KDE/plasma]](#Using_the_Native_File_Dialogs_on_KDE.2Fplasma)

# [Overview]

[Vivaldi](https://vivaldi.com/) is a chromium based browser which focuses on providing the ability to customize the browser to meet the end-users needs.

\

# [Installing Vivaldi]

Vivaldi is available from the manjaro repo.

To install the base Vivaldi you can use the command:

[user \$ ][ pamac install vivaldi [COPY TO CLIPBOARD]]

\

\
If you want to view DRM protected video content you will also need the proprietary widevine codec. This can be installed with

[user \$ ][ pamac build vivaldi-widevine [COPY TO CLIPBOARD]]

\

\

**note**

------------------------------------------------------------------------

If you also have Google Chrome package installed you can use the widevine plugin bundled with Chrome instead

\
Lastly, if you want to be able to play common media formats you will need the codecs.

You can install the package `vivaldi-ffmpeg-codecs` with the command

[user \$ ][ pamac install vivaldi-ffmpeg-codecs [COPY TO CLIPBOARD]]

\

# [Tips and Tricks]

## [Access Additional Settings]

Vivaldi has a settings menu which offers extensive customization ability. However, not all things supported by Chromium are accessible via the menu. To access the underlying Chromium settings, put this in the address bar:

    chrome://settings

\

## [][Using the Native File Dialogs on KDE/plasma]

By default, Vivaldi will use the GTK file dialogs. If you are using plasma and would prefer native dialogs, you can install the package `kdialog` using your favorite package manager or with the command:

[user \$ ][ pamac install kdialog [COPY TO CLIPBOARD]]

\