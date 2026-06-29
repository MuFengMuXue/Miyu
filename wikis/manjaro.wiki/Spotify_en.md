[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Spotify&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Spotify "Spotify (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Spotify/fr "Spotify (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Spotify/ru "Spotify (100% translated)") • ‎[עברית](//wiki.manjaro.org/index.php?title=Spotify/he "Spotify/he (5% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Spotify/fa "اِسپاتیفای (Spotify) (42% translated)")

## Contents

-   [[1] [Installing Spotify]](#Installing_Spotify)
    -   [[1.1] [Installing from the Arch User Respository(AUR)]](#Installing_from_the_Arch_User_Respository.28AUR.29)
    -   [[1.2] [Installing as Flatpak Application]](#Installing_as_Flatpak_Application)
-   [[2] [Tips & Tricks]](#Tips_.26_Tricks)
    -   [[2.1] [Manual configuration of media keys]](#Manual_configuration_of_media_keys)
    -   [[2.2] [Opening Links from Spotify]](#Opening_Links_from_Spotify)
    -   [[2.3] [PGP signatures could not be verified]](#PGP_signatures_could_not_be_verified)
    -   [[2.4] [Blank Spotify or x-window]](#Blank_Spotify_or_x-window)
-   [[3] [See Also]](#See_Also)

\

[![250px-Spotify.svg.png](/images/a/a1/250px-Spotify.svg.png)](//wiki.manjaro.org/index.php?title=File:250px-Spotify.svg.png)

[Spotify](http://en.wikipedia.org/wiki/Spotify) is a commercial music streaming service providing digital rights management-restricted content from record labels including Sony, EMI, Warner Music Group and Universal.

Spotify operates under a freemium model (basic services are free, while additional features are offered via paid subscriptions). Spotify makes its revenues by selling premium streaming subscriptions to users and advertising placements to third parties.

\

# [Installing Spotify]

Spotify can be installed via a variety of methods based on your personal preferences.

\

## [][Installing from the Arch User Respository(AUR)]

Spotify can be installed from the [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") using your favorite package manager or the command:

    pamac build spotify

\

## [Installing as Flatpak Application]

If you have [flatpak](//wiki.manjaro.org/index.php?title=Flatpak "Flatpak") installed you can install Spotify with:

    flatpak install spotify

\

# [][Tips & Tricks]

## [Manual configuration of media keys]

If your system does not detect the media keys, their names are (in order) XF86AudioPlay, XF86AudioStop, XF86AudioNext, XF86AudioPrevious

    dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause
    dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop
    dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next
    dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous

\

## [Opening Links from Spotify]

Spotify may fail to open links (e.g. for password reset or login via Facebook). To fix this, install **xdg-desktop-portal-gtk** via:

    pamac install xdg-desktop-portal-gtk

\

## [PGP signatures could not be verified]

Import the public key with

    curl -sS https://download.spotify.com/debian/pubkey_5E3C45D7B312C643.gpg | gpg --import -

then try installing it again

    pamac build spotify

## [Blank Spotify or x-window]

the error in the terminal should look like this

    "spotify: /usr/lib/libcurl-gnutls.so.4: no version information available (required by spotify)"

to fix this

    just delete the spotify folder in your /home/<yourusername>/.config/ directory

# [See Also]

[AUR:spotify](https://aur.archlinux.org/packages/spotify/)

[The Spotify Community](https://community.spotify.com/)