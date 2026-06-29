[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-PCmanFM-Qt&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=PCmanFM-Qt "PCmanFM-Qt (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=PCmanFM-Qt/ru "PCmanFM-Qt (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Creating Custom Actions]](#Creating_Custom_Actions)
    -   [[2.1] ["Edit as root" custom action]](#.E2.80.9CEdit_as_root.E2.80.9D_custom_action)
    -   [[2.2] ["Set as wallpaper" custom action]](#.E2.80.9CSet_as_wallpaper.E2.80.9D_custom_action)
    -   [[2.3] ["Compress" custom action]](#.E2.80.9CCompress.E2.80.9D_custom_action)
    -   [[2.4] ["Extract" custom action]](#.E2.80.9CExtract.E2.80.9D_custom_action)
-   [[3] [See also]](#See_also)

# [Overview]

PCManFM-Qt is the Qt port of PCManFM, the file manager of LXDE. It is the official file manager of lxqt but has few dependencies and can be used as a drop-in file manager on any Window Manager or Desktop Environment.

\

# [Creating Custom Actions]

Before creating the actions (which are desktop files), first create its directory/folder by copy-pasting the below command in terminal:

    mkdir -p ~/.local/share/file-manager/actions

The last two directories in the above line have now been created recursively. You can as well create them one inside the other by file manager. If you prefer this method and can't see the first hidden directory (`.local`) in your `Home` (`~/`) press `Ctrl+h` to make it (and all hidden files and directories) appear.

\
Below actions are just examples. You can use them and create your own actions based on them.

\

## []["Edit as root" custom action]

Create and edit the action file (rootedit.desktop) either by using file manager or by issuing these terminal commands one at a time (replace `juffed` with your text editor if it's different):

    touch ~/.local/share/file-manager/actions/rootedit.desktop
    juffed ~/.local/share/file-manager/actions/rootedit.desktop

Paste the below content in `rootedit.desktop`:

    [Desktop Entry]
    Type=Action
    Name=Edit as Root
    Icon=dialog-password
    Profiles=profile-zero;

    [X-Action-Profile profile-zero]
    Exec=gksu juffed %f
    Name=Default profile

Replace `juffed` with your text editor if it's different and replace `gksu` with `kdesu` if you use `kdesu`.

\

## []["Set as wallpaper" custom action]

Create and edit the action file (wallpaper.desktop) either by using file manager or by issuing these terminal commands one at a time (replace `juffed` with your text editor if it's different):

    touch ~/.local/share/file-manager/actions/wallpaper.desktop
    juffed ~/.local/share/file-manager/actions/wallpaper.desktop

Paste the below content in `wallpaper.desktop`:

    [Desktop Entry]
    Type=Action
    Name[en]=Set As Wallpaper
    Icon=user-desktop
    Profiles=profile-zero;

    [X-Action-Profile profile-zero]
    MimeTypes=image/*;
    Exec=pcmanfm-qt -w %f
    Name[en]=Default profile
    SelectionCount==1

\

## []["Compress" custom action]

If you don\'t have one of those archive applications listed in pcmanfm-qt\'s Preferences\>Advanced, you can use a commandline archive utility like `atool` with custom actions. First install `atool` from the repo:

    sudo pacman -S atool

Create and edit the action file (compress.desktop) either by using file manager or by issuing these terminal commands one at a time (replace `juffed` with your text editor if it's different):

    touch ~/.local/share/file-manager/actions/compress.desktop
    juffed ~/.local/share/file-manager/actions/compress.desktop

Paste the below content in `compress.desktop`:

    [Desktop Entry]
    Type=Action
    Name[en]=Compress
    Icon=application-x-compressed-tar
    Profiles=profile-zero;

    [X-Action-Profile profile-zero]
    MimeTypes=all/all;
    Exec=apack %d/%n.tar.gz %F
    Name[en]=Default profile
    SelectionCount==1

This will create a YOUR_USERNAME.tar.gz archive from the selected files/folders in the current directory. (You may need to change the icon in the above code if you don\'t have oxygen icons.)

\

## []["Extract" custom action]

If you don\'t have one of those archive applications listed in pcmanfm-qt\'s Preferences\>Advanced, you can use a commandline archive utility like `atool` with custom actions. First install `atool` from the repo:

    sudo pacman -S atool

Create and edit the action file (extract.desktop) either by using file manager or by issuing these terminal commands one at a time (replace `juffed` with your text editor if it's different):

    touch ~/.local/share/file-manager/actions/extract.desktop
    juffed ~/.local/share/file-manager/actions/extract.desktop

Paste the below content in `extract.desktop`:

    [Desktop Entry]
    Type=Action
    Name[en]=Extract
    Icon=package-x-generic
    Profiles=profile-zero;

    [X-Action-Profile profile-zero]
    MimeTypes=application/x-7z-compressed;application/x-7z-compressed-tar;application/x-ace;application/x-alz;application/x-ar;application/x-arj;application/x-bzip;application/x-bzip-compressed-tar;application/x-bzip1;application/x-bzip1-compressed-tar;application/x-cabinet;application/x-cbr;application/x-cbz;application/x-cd-image;application/x-compress;application/x-compressed-tar;application/x-cpio;application/x-deb;application/x-ear;application/x-ms-dos-executable;application/x-gtar;application/x-gzip;application/x-gzpostscript;application/x-java-archive;application/x-lha;application/x-lhz;application/x-lzip;application/x-lzip-compressed-tar;application/x-lzma;application/x-lzma-compressed-tar;application/x-lzop;application/x-lzop-compressed-tar;application/x-rar;application/x-rar-compressed;application/x-rpm;application/x-rzip;application/x-tar;application/x-tarz;application/x-stuffit;application/x-war;application/x-xz;application/x-xz-compressed-tar;application/x-zip;application/x-zip-compressed;application/x-zoo;application/zip;multipart/x-zip;
    Exec=atool --extract-to=%d %f
    Name[en]=Default profile
    SelectionCount==1

This will uncompress the selected archive into the current directory. (You may need to change the icon in the above code if you don\'t have oxygen icons.)

\

# [See also]

You can find more pages about LXQt in the Manjaro Wiki [here](https://wiki.manjaro.org/index.php?title=Desktop_Environments#LXQt).