**These guides are user-contributed and not supported by the Sway team.** Most distributions have a Sway package available in the official repositories. Here's some info for the ones that don't:

## Debian

### Official Repository

Since Debian 11 (bullseye), an older version of sway is available in the official repositories (1.5 at time of writing, latest is 1.6.1). To use this version, simply run:
```
sudo apt install sway
```

### Manual installation

* [Installation guide](https://github.com/swaywm/sway/wiki/Debian-10-(Buster)-Installation) for Debian 10 stable (Buster).

### Unofficial Nightly Packages

There is a [Debian repository](https://apt.quantum2.xyz/sway-utils/) that includes a `sway` package which is compatible with Debian 10 (buster). This is built nightly from the latest sway and wlroots. Run following commands in order to install Sway from the repository:

```bash
curl https://quantum2.xyz/apt.key | sudo apt-key add -
echo 'deb [arch=amd64] https://apt.quantum2.xyz/sway-utils/ buster main' | sudo tee /etc/apt/sources.list.d/sway-utils.list
sudo apt update
sudo apt install sway
```

The same repository also provides latest nightly builds for Debian 11 (bullseye):

```bash
curl https://quantum2.xyz/apt.key | sudo apt-key add -
echo 'deb [arch=amd64] https://apt.quantum2.xyz/sway-utils/ bullseye main' | sudo tee /etc/apt/sources.list.d/sway-utils.list
sudo apt update
sudo apt install sway
```

## Fedora

sway is available in the official repositories:
```
sudo dnf install sway
```
If you want a newer version, enable the sway rolling module:
```
sudo dnf module enable sway:rolling
sudo dnf install sway
```

A [quick guide](https://nationpigeon.com/compiling-sway-on-fedora-29/) is available for building sway from source on Fedora 29. 

There are also various COPRs available, such as https://copr.fedorainfracloud.org/coprs/mhonek/sway/

## Arch

To install sway on Arch Linux run:

```
sudo pacman -S sway
```

There is also extra documentation available that can be found here: https://wiki.archlinux.org/index.php/Sway

An AUR package fetching the latest commit is available: https://aur.archlinux.org/packages/sway-git/. Always upgrade `wlroots-git` when upgrading `sway-git`.