[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Mozilla+Firefox&language=en&action=page&filter= "Special:Translate")

Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Mozilla+Firefox&language=de&task=view "Start translation for this language") • ‎[English](//wiki.manjaro.org/index.php?title=Mozilla_Firefox "Mozilla Firefox (100% translated)") • ‎[español](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Mozilla+Firefox&language=es&task=view "Start translation for this language") • ‎[español de América Latina](//wiki.manjaro.org/index.php?title=Mozilla_Firefox/es-419 "Mozilla Firefox/es-419 (5% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Mozilla_Firefox/fr "Mozilla Firefox (34% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Mozilla_Firefox/ru "Mozilla Firefox (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Mozilla_Firefox/fa "موزیلا فایرفاکس (51% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Mozilla_Firefox/zh-cn "Mozilla Firefox (15% translated)")

## Contents

-   [[1] [Installing Firefox]](#Installing_Firefox)
-   [[2] [Other Versions]](#Other_Versions)
-   [[3] [Dealing with dark GTK themes]](#Dealing_with_dark_GTK_themes)
-   [[4] [Plasma Integration]](#Plasma_Integration)
    -   [[4.1] [Installing plasma Browser Integration]](#Installing_plasma_Browser_Integration)
    -   [[4.2] [Using the native file chooser]](#Using_the_native_file_chooser)
-   [[5] [Installing Firefox directly from the Mozilla Website]](#Installing_Firefox_directly_from_the_Mozilla_Website)
    -   [[5.1] [Download Firefox from Mozilla]](#Download_Firefox_from_Mozilla)
    -   [[5.2] [Extract the files]](#Extract_the_files)
    -   [[5.3] [Create an icon]](#Create_an_icon)
-   [[6] [See also]](#See_also)

# [Installing Firefox]

Firefox can be installed using the package **firefox** in your favorite package manager or using the command:

[user \$ ][ pamac install firefox [COPY TO CLIPBOARD]]

\

# [Other Versions]

  --------------------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------
  Package Name                Source   URL                                                                                                                                                                                Description
  firefox-developer-edition   repo     [https://www.mozilla.org/firefox/channel/#developer](https://www.mozilla.org/firefox/channel/#developer)                                           Official Developer Edition builds
  firefox-nightly             aur      [https://www.mozilla.org/en-US/firefox/nightly](https://www.mozilla.org/en-US/firefox/nightly)                                                     Official Nightly builds
  firefox-kde-opensuse        aur      [https://build.opensuse.org/package/show/mozilla:Factory/MozillaFirefox](https://build.opensuse.org/package/show/mozilla:Factory/MozillaFirefox)   OpenSUSE\'s version of Firefox includes appmenu integration and native plasma integration
  firefox-appmenu             aur      [https://aur.archlinux.org/packages/firefox-appmenu/](https://aur.archlinux.org/packages/firefox-appmenu/)                                         Unofficial Firefox build with appmenu patches added
  firefox-esr                 aur      [https://www.mozilla.org/en-US/firefox/organizations/](https://www.mozilla.org/en-US/firefox/organizations/)                                       Official ESR releases. This is the oldest supported version of Firefox
  --------------------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------

# [Dealing with dark GTK themes]

Some pages will be hard to read when using dark gtk themes. There are a few different ways to handle this:

-   The most flexible way is to install the add-on [Text Contrast for Dark Themes](https://addons.mozilla.org/en-US/firefox/addon/text-contrast-for-dark-themes) which will allow you to keep your theming but adjust it on a per page basis as needed

<!-- -->

-   A simpler way is Preferences-\>Language & Appearance-\>Colors and uncheck \"Use System Colors\". The downside of this approach is that Firefox will no longer use a dark theme.

<!-- -->

-   We can use css to force white backgrounds with dark text and controls by editing or creating *\~/.mozilla/profile.default/chrome/userContent.css* with the following content:

<!-- -->

    input:not(.urlbar-input):not(.textbox-input):not(.form-control):not([type='checkbox']):not([type='radio']), textarea, select

    #downloads-indicator-counter

\

# [Plasma Integration]

## [Installing plasma Browser Integration]

The [browser integration package](https://community.kde.org/Plasma/Browser_Integration) provides media controls, notifications and integration with krunner. You can install it with:

[user \$ ][ pamac install plasma-browser-integration [COPY TO CLIPBOARD]]

\

Next install the [plasma integration add-on](https://addons.mozilla.org/en-US/firefox/addon/plasma-integration) in Firefox.

\

## [Using the native file chooser]

It is possible to integrate the file chooser from plasma into Firefox giving you a more seamless experience.

First ensure the packages xdg-desktop-portal and xdg-desktop-portal-kde using the command:

[user \$ ][ pamac install xdg-desktop-portal xdg-desktop-portal-kde [COPY TO CLIPBOARD]]

\

Now we need to create a customized desktop launcher by creating a copy of the distribution file with

[user \$ ][ mkdir -p \~/.local/share/applications [COPY TO CLIPBOARD]]

\

[user \$ ][ cp /usr/share/applications/firefox.desktop \~/.local/share/applications/ [COPY TO CLIPBOARD]]

\

Next we need to edit the newly created file at \~/.local/share/applications/firefox.desktop using a [text editor](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files "Viewing and editing configuration files")

There are 3 edits that need to made to this file.

replace:

    Exec=/usr/lib/firefox/firefox %u

with:

    Exec=/usr/bin/sh -c "GTK_USE_PORTAL=1 /usr/lib/firefox/firefox %u"

replace:

    Exec=/usr/lib/firefox/firefox --new-window %u

with:

    Exec=/usr/bin/sh -c "GTK_USE_PORTAL=1 /usr/lib/firefox/firefox --new-window %u"

replace:

    Exec=/usr/lib/firefox/firefox --private-window %u

with:

    Exec=/usr/bin/sh -c "GTK_USE_PORTAL=1 /usr/lib/firefox/firefox --private-window %u"

Save and enjoy your firefox/plasma integration

\

# [Installing Firefox directly from the Mozilla Website]

Generally it is better to use the version of Firefox that is available in the repos but installing Firefox directly has one advantage: Firefox will update itself automatically as soon as an update is available. This is great for users, who want to get the latest update as soon as possible without waiting for the next Manjaro update.

\

## [Download Firefox from Mozilla]

Download the latest Firefox in your language from here: [https://www.mozilla.org/en-US/firefox/all/](https://www.mozilla.org/en-US/firefox/all/)

Most users will download \"Linux 64-bit\" in your chosen language. If you are using manjaro32, download \"Linux 32-bit\"

\

## [Extract the files]

Ensure that **\~/bin** exists with

[user \$ ][ mkdir -p \~/bin [COPY TO CLIPBOARD]]

\

Unpack/extract the downloaded `firefox-xx.x.tar.bz2` file to *\~/bin/* using a graphical tool or with the *tar* command. Here is an example:

[user \$ ][ tar -xf \~/Downloads/firefox-66.0.5.tar.bz2 \--directory \~/bin [COPY TO CLIPBOARD]]

\

You can now start to use Firefox by double clicking on the file (or executing it in a terminal):

[user \$ ][ \~/bin/firefox/firefox [COPY TO CLIPBOARD]]

\

\

## [Create an icon]

Let\'s create an icon in order to start Firefox much more easily.

Create an empty file

[user \$ ][ mkdir -p \~/.local/share/applications [COPY TO CLIPBOARD]]

\

[user \$ ][ touch \~/.local/share/applications/firefox.desktop [COPY TO CLIPBOARD]]

\

Edit the file *\~/.local/share/applications/firefox.desktop* in your favorite editor. For a list of common editors see [this page](//wiki.manjaro.org/index.php?title=Viewing_and_editing_configuration_files "Viewing and editing configuration files")

Copy and paste the following code into your `firefox.desktop` file and save it:

    [Desktop Entry]
    Name=Firefox
    GenericName=Web Browser
    Icon=~/bin/firefox/browser/icons/mozicon128.png
    Type=Application
    Categories=Application;Network;WebBrowser;
    Exec=~/bin/firefox/firefox
    Terminal=false
    StartupNotify=false

In most Desktop Environments(DEs), Firefox will now be added to the menu. In some DEs you can click on the desktop to launch the application as well.

\

# [See also]

-   [The arch wiki page](https://wiki.archlinux.org/index.php/Firefox)
-   [Internet Browsers wiki page](//wiki.manjaro.org/index.php?title=Internet_Browsers "Internet Browsers")