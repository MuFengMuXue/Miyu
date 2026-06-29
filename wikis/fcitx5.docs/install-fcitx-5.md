# Install Fcitx 5

\_\_TOC\_\_

Fcitx package usually come with following parts: the main program, input method modules for applications and the addons (most of them are engines).

## Install Fcitx 5 from Linux distribution

You would need to search the package from your own packages. Usually, the Fcitx 5 package has "fcitx5" in its name.

As of today, fcitx 5 is not yet generally available in distribution repository, except for some of the rolling release distributions.

Following are some examples of search Fcitx 5 packages in your own distributions. You may also use the GUI software center provided by your desktop, for example gnome-software, or plasma-discover.

    yum search fcitx5 #
    dnf search fcitx5 # Fedora
    pacman -Ss fcitx5 # Archlinux
    zypper search fcitx5 # OpenSUSE
    apt-cache search fcitx5 # Debian/Ubuntu

Or [pkgs.org](https://pkgs.org/search/?q=fcitx5) provides an easy way to search packages for different distributions. Please notice that if the version is something like 0.0~git, this version is a extremely old version of Fcitx 5, which is older than the oldest stable release of Fcitx 5. Generally it is not recommended to use it.

pkgs.org also provides distribution specific the command for installing it.

A basic installation of fcitx5 would includes:

- [fcitx5](https://pkgs.org/search/?q=fcitx5), the main program
- [fcitx5-gtk](https://pkgs.org/search/?q=fcitx5-gtk), [fcitx5-qt](https://pkgs.org/search/?q=fcitx5-qt), the im module for the most popular UI toolkit.
- [fcitx5-configtool](https://pkgs.org/search/?q=fcitx5-configtool), the GUI configuration program.
- Input method engines for different languages:
  - See [Input method engines](Special:myLanguage/Input_method_engines "wikilink")

Some additional support addons and themes may includes:

- [fcitx5-lua](https://pkgs.org/search/?q=fcitx5-lua), which provides lua scripting support
- [fcitx5-material-color](https://pkgs.org/search/?q=fcitx5-material-color), a set of colorful theme for Fcitx 5

## Install Fcitx 5 from Flatpak

[Flatpak](https://flatpak.org/) is a utility for software deployment and package management for Linux. There are two flatpak repository that provides fcitx 5, [flathub](https://flathub.org) and fcitx's own unstable repo.

As of today, we are still working on pushing Fcitx 5 packages to flathub. flathub right now only have fcitx5 main program, Chinese addons, Zhuyin, and Mozc.

To Setup the flatpak repo, you will need to execute following command, or do it in GUI.

    # Add flatub repo, fcitx5-unstable also relies on some runtime packages in it.
    flatpak remote-add --user --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
    # Optionally: Add fcitx 5 unstable repo if you want to use the unstable version.
    flatpak remote-add --user --if-not-exists fcitx5-unstable https://flatpak.fcitx-im.org/unstable-repo/fcitx5-unstable.flatpakrepo

To install fcitx from flatpak

    # With older flatpk, you will need to specify the repository name too: flatpak install flathub org.fcitx.Fcitx5
    flatpak install org.fcitx.Fcitx5
    # Install fcitx 5 engines, for example, fcitx5-chinese-addons, or mozc
    flatpak install org.fcitx.Fcitx5.Addon.ChineseAddons
    flatpak install org.fcitx.Fcitx5.Addon.Mozc

Flatpak can not provide the im module you need on your host, so you would still need to install them natively. If your distribution does not have fcitx 5 package, you may use fcitx 4 im module instead (newer than 4.2.9.7), or even ibus im module.

## Install Fcitx 5 from Source code

- [Compiling fcitx5](Special:myLanguage/Compiling_fcitx5 "wikilink")

Please also read [Setup Fcitx 5](Special:MyLanguage/Setup_Fcitx_5 "wikilink") before you start to use Fcitx 5.
