Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/Discord/fr "Discord (54% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Discord/hu "Discord (54% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Discord/ja "Discord (100% translated)")

**Resources**

[[]][Home](https://discord.com/)

[[]][Package information](https://packages.gentoo.org/packages/net-im/discord)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Discord_(software) "wikipedia:Discord (software)")

[[]][GitHub](https://github.com/Discord)

**Discord** is a proprietary VoIP instant messaging and digital distribution platform for voice, video, and text communication.

Discord is written in JavaScript (with React), [Elixir](https://wiki.gentoo.org/wiki/Elixir "Elixir"), [Python](https://wiki.gentoo.org/wiki/Python "Python"), [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") and [C++](https://wiki.gentoo.org/wiki/C%2B%2B "C++").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Alternative installation possibilities]](#Alternative_installation_possibilities)
        -   [[1.3.1] [Flatpak]](#Flatpak)
        -   [[1.3.2] [Snap]](#Snap)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Discord shows the GTK file picker while using KDE or other QT environment]](#Discord_shows_the_GTK_file_picker_while_using_KDE_or_other_QT_environment)
    -   [[2.2] [Discord doesn\'t start upon a launcher update]](#Discord_doesn.27t_start_upon_a_launcher_update)
        -   [[2.2.1] [Updating the package via portage]](#Updating_the_package_via_portage)
        -   [[2.2.2] [Alternative: disabling the update check]](#Alternative:_disabling_the_update_check)
    -   [[2.3] [Enabling Discord Rich Presence on Flatpak]](#Enabling_Discord_Rich_Presence_on_Flatpak)
    -   [[2.4] [Discord doesn\'t show emojis or other glyphs correctly]](#Discord_doesn.27t_show_emojis_or_other_glyphs_correctly)
    -   [[2.5] [Discord icon in Plasma systray is blurry]](#Discord_icon_in_Plasma_systray_is_blurry)
    -   [[2.6] [Discord screensharing issue with Wayland: zkde_screencast_unstable_v1 does not seem to be available]](#Discord_screensharing_issue_with_Wayland:_zkde_screencast_unstable_v1_does_not_seem_to_be_available)
-   [[3] [See Also]](#See_Also)

## [Installation]

### [USE flags]

### [USE flags for] [net-im/discord](https://packages.gentoo.org/packages/net-im/discord) [[]] [All-in-one voice and text chat for gamers]

  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  [`+seccomp`](https://packages.gentoo.org/useflags/+seccomp)           Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`appindicator`](https://packages.gentoo.org/useflags/appindicator)   Build in support for notifications using the libindicate or libappindicator plugin
  [`wayland`](https://packages.gentoo.org/useflags/wayland)             Enable dev-libs/wayland backend
  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-30 05:57] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Discord has a package in the official Gentoo repository - this is the recommended way to install Discord.

Emerge Discord:

`root `[`#`]`emerge --ask net-im/discord`

### [Alternative installation possibilities]

For users that may have reason to prefer other methods of installing Discord on Gentoo, these alternative options are available.

#### [[] Flatpak]

Discord is available as a [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak") application that can be automatically downloaded and installed from Flathub.

Once Flatpak is available, install Discord from Flathub:

`user `[`$`]`flatpak install flathub com.discordapp.Discord`

After successful installation, Discord may be launched from the command line:

`user `[`$`]`flatpak run com.discordapp.Discord`

#### [[] Snap]

First, install [Snap](https://wiki.gentoo.org/wiki/Snap "Snap"), paying attention to the recommendations from that article.

Once Snap is available, install Discord:

`root `[`#`]`snap connect discord:system-observe`

## [Troubleshooting]

### [Discord shows the GTK file picker while using KDE or other QT environment]

In order to display the correct file picker, Discord reads from the `GTK_USE_PORTAL` environment variable. To use the right file picker from KDE/QT, launch Discord with the following command or edit the shortcut:

[CODE]

    GTK_USE_PORTAL=1 discord

### [][Discord doesn\'t start upon a launcher update]

[![Screenshot from 2022-03-01 13-08-39.png](/images/4/49/Screenshot_from_2022-03-01_13-08-39.png)](https://wiki.gentoo.org/wiki/File:Screenshot_from_2022-03-01_13-08-39.png)

[](https://wiki.gentoo.org/wiki/File:Screenshot_from_2022-03-01_13-08-39.png "Enlarge")

** Note**\
This applies only for the official [[[net-im/discord]](https://packages.gentoo.org/packages/net-im/discord)[]] package. The other package managers should not be affected. If they are, update their repositories.

On GNU/Linux systems, Discord expects the launcher to be always up to date. When a launcher update is available, Discord prompts the user to download the latest `.deb` package from the official website, this of course works only on Debian-based distributions.

#### [Updating the package via portage]

In Gentoo, solve this by syncing the repositories and updating the [[[net-im/discord]](https://packages.gentoo.org/packages/net-im/discord)[]] package.

`root `[`#`]`emerge --sync`

`root `[`#`]`emerge --ask net-im/discord`

There are reasons why the user might not want to use this method. The most common reason is that the package is not yet updated in the Gentoo repository. In that case using [Flatpak](https://wiki.gentoo.org/wiki/Discord#Flatpak "Discord") or [Snap](https://wiki.gentoo.org/wiki/Discord#Snap "Discord") version is advised.

Should the Snap or Flatpak version not be desired by the user, a manual update can be performed. This can be done, by downloading the tar.gz file that Discord offers and moving it to `/opt/discord` manually. It should be noted, that this operation may not always work, since it does not update system level dependencies.

`root `[`#`]`tar -xf discord-*.tar.gz -C /opt/discord --strip-components=1`

#### [Alternative: disabling the update check]

To disable the update check during startup put `"SKIP_HOST_UPDATE": true` into [\~/.config/discord/settings.json].

### [Enabling Discord Rich Presence on Flatpak]

When using the [Flatpak](https://wiki.gentoo.org/wiki/Discord#Flatpak "Discord") version of Discord, Rich Presence will not work out of the box. To make it work, a symlink must be created for the current user session. Run:

`user `[`$`]`ln -sf $XDG_RUNTIME_DIR//discord-ipc-0`

### [][Discord doesn\'t show emojis or other glyphs correctly]

In order to display some characters correctly, [[[media-fonts/noto-emoji]](https://packages.gentoo.org/packages/media-fonts/noto-emoji)[]] and [[[media-fonts/noto-cjk]](https://packages.gentoo.org/packages/media-fonts/noto-cjk)[]] can be merged like this:

`root `[`#`]`emerge --ask media-fonts/noto-emoji media-fonts/noto-cjk`

Should the fonts still fail to display, the user may reload the font information cache by running:

`user `[`$`]`fc-cache -fv`

### [Discord icon in Plasma systray is blurry]

If using [Plasma](https://wiki.gentoo.org/wiki/Plasma "Plasma"), [[[dev-libs/libappindicator]](https://packages.gentoo.org/packages/dev-libs/libappindicator)[]] may be merged, to have a nice icon in the systray instead of a blurry one:

`root `[`#`]`emerge --ask dev-libs/libappindicator`

### [Discord screensharing issue with Wayland: zkde_screencast_unstable_v1 does not seem to be available]

If using [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"), in order to be able to screenshare, enable [[[screencast]](https://packages.gentoo.org/useflags/screencast)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag for [[[kde-plasma/kwin]](https://packages.gentoo.org/packages/kde-plasma/kwin)[]].

## [See Also]

-   [Telegram](https://wiki.gentoo.org/wiki/Telegram "Telegram") --- a freeware, cross-platform, cloud-based instant messaging (IM) system.
-   [Recommended applications](https://wiki.gentoo.org/wiki/Recommended_applications "Recommended applications") --- applications recommended for use in a graphical environment ([X11](https://wiki.gentoo.org/wiki/Xorg "Xorg"), [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"))