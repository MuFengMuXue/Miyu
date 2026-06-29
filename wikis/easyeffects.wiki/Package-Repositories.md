# Package Repositories

This page contains information about community and distribution maintained packages and repositories. Here you will find more detailed instructions on how to install a distribution package.

Please note that anyone can create a repository and add the necessary information to this wiki page. The EasyEffects developer(s) cannot guarantee the security of these repositories, or that they are still maintained.

If you are having any issues that you suspect are specific to your installation method, please contact the respective package maintainer, as listed on this page.

## List of packages in repositories

<a href="https://repology.org/project/easyeffects/versions">
    <img src="https://repology.org/badge/vertical-allrepos/easyeffects.svg" alt="Packaging status">
</a>

## Arch Linux

To install [easyeffects](https://archlinux.org/packages/extra/x86_64/easyeffects/) on Arch, run:
```
sudo pacman -S easyeffects
```

## Fedora
EasyEffects is part of the distribution in Fedora 35+, install it with:
```sh
sudo dnf install -y easyeffects
```

For earlier Fedora releases EasyEffects has been made available through Copr, to install run:
```
sudo dnf copr enable -y godsic/EasyEffects 
sudo dnf install -y easyeffects
```


## Flatpak

Provided by [Flathub](https://flathub.org/).

```
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub com.github.wwmm.easyeffects
```

The Flatpak manifest is maintained [in-tree here](https://github.com/wwmm/easyeffects/blob/master/util/flatpak/com.github.wwmm.easyeffects.Devel.json).

## CI Artifacts

Flatpak bundles and Arch packages are produced for every push to master, and every push to PRs. Links are provided by a bot in PRs, and from the actions tab for pushes to master ([or can be viewed here](https://nightly.link/wwmm/easyeffects/workflows/CI.yaml/master)). 

These are meant for development/testing, are not supported and are not automatically updated. 

If you want the supported and stable Flatpak or Arch package experience, install the normal [Flatpak build](https://github.com/wwmm/easyeffects/wiki/Package-Repositories#flatpak) or the [Arch build](https://github.com/wwmm/easyeffects/wiki/Package-Repositories#arch-linux).

## Gentoo

To install [easyeffects](https://packages.gentoo.org/packages/media-sound/easyeffects) on Gentoo, run:
```
emerge media-sound/easyeffects
```
Packages provided by [prometheanfire](https://github.com/prometheanfire).

## NixOS

Add to your [home-manager](https://github.com/nix-community/home-manager) configuration: `services.easyeffects.enable = true;`

And to `configuration.nix`: `programs.dconf.enable = true;`