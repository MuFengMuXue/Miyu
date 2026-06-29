Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Dolphin/tr "Dolphin (17% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Dolphin/ru "Dolphin (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installing Dolphin]](#Installing_Dolphin)
-   [[3] [Enabling previews]](#Enabling_previews)
    -   [[3.1] [Installing optional dependencies]](#Installing_optional_dependencies)
    -   [[3.2] [Enabling preview thumbnails in Dolphin]](#Enabling_preview_thumbnails_in_Dolphin)

\

[![Dolphin.png](/images/thumb/0/0b/Dolphin.png/400px-Dolphin.png)](//wiki.manjaro.org/index.php?title=File:Dolphin.png)

# [Overview]

Dolphin is the file management application of Plasma Workspace. It is designed to be simple to use, yet powerful.

\

# [Installing Dolphin]

Dolphin can be installed by installing the package **dolphin** in any package manager or with the command:

    pamac install dolphin

\

# [Enabling previews]

[![Dolphinsettings.png](/images/thumb/7/74/Dolphinsettings.png/400px-Dolphinsettings.png)](//wiki.manjaro.org/index.php?title=File:Dolphinsettings.png)

## [Installing optional dependencies]

The following packages enable preview thumbnails in dolphin

-   ffmpegthumbs: video thumbnails
-   kdegraphics-thumbnailers: PDF and PS thumbnails
-   qt5-imageformats: thumbnails for additional image formats
-   kimageformats: thumbnails for additional image formats
-   taglib: audio file thumbnails
-   libappimage: AppImage thumbnails
-   raw-thumbnailer: Raw image files from a camera

To install all of these use:

    pamac install ffmpegthumbs kdegraphics-thumbnailers qt5-imageformats kimageformats taglib libappimage raw-thumbnailer

\

## [Enabling preview thumbnails in Dolphin]

Once the packages needed to generate thumbnails are installed, you need to enable the previews in dolphin in the settings. These can be found in Dolphin under Control-\>Configure Dolphin-\>General under the Previews tab.

Check the boxes for the previews to be enabled. If you don\'t want large remote files to have previews generated, set a maximum size in box next to Skip previews for remote files above: section.