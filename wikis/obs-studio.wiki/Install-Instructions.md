# Table of Contents

* [Building OBS Studio](#building-obs-studio)
* [Windows](#windows)
* [macOS](#macos)
* [Linux](#linux)
  * [Supported builds](#supported-builds)
    * Flatpak
    * Ubuntu
  * [Unofficial builds](#unofficial-builds)
    * Arch Linux
    * Debian
    * Fedora
    * Gentoo
    * Manjaro
    * NixOS
    * OpenMandriva
    * OpenSUSE
    * snappy
    * Solus
    * UOS/Deepin
    * Void
* [FreeBSD](#freebsd)

***

# [Building OBS Studio](Building-OBS-Studio)

Please see the build instructions for:

* [Windows](build-instructions-for-windows)
* [macOS](build-instructions-for-mac)
* [Linux](build-instructions-for-linux)
* [FreeBSD](Build-Instructions-For-FreeBSD)

# Windows

## Installer

* Download the official Windows version of OBS Studio from:
  * the [OBS Studio website](https://obsproject.com/download)
  * the OBS Project's [GitHub releases](https://github.com/obsproject/obs-studio/releases) page
* Run the installer

## Microsoft Store

* Install OBS Studio from the [Microsoft Store](ms-windows-store://pdp/?ProductId=XPFFH613W8V6LV&mode=mini)

## Steam

* Install OBS Studio from [Steam](https://store.steampowered.com/app/1905180/OBS_Studio/)

## Portable version

* Download the official ZIP version of OBS Studio from:
  * the [OBS Studio website](https://obsproject.com/download)
  * the OBS Project's [GitHub releases](https://github.com/obsproject/obs-studio/releases) page
* Unzip the ZIP
* In the folder you unzipped, create a blank .txt file and name it `obs_portable_mode.txt`

# macOS

## Disk image

* Download the official macOS version of OBS Studio from:
  * the [OBS Studio website](https://obsproject.com/download)
  * the OBS Project's [GitHub releases](https://github.com/obsproject/obs-studio/releases) page
* Mount the disk image (`.dmg`) and drag `OBS.app` to the Applications folder

# Linux

## Prerequisites for all versions

* xserver-xorg version 1.18.4 or newer is recommended to avoid potential performance issues with certain features in OBS, such as the fullscreen projector.
* OpenGL 3.3 (or later) support is required to use OBS Studio on Linux. You can check what version of OpenGL is supported by your system by typing `glxinfo | grep "OpenGL"` on Terminal.
* For virtual camera support, you need the `v4l2loopback` kernel module installed. You can install it with the following command: 
  * Debian/Ubuntu-based: 
    ```bash
    sudo apt install v4l2loopback-dkms
    ```
  * Red Hat/Fedora-based (requires [RPM Fusion](https://rpmfusion.org/Configuration) to be enabled):
    ```bash
    sudo dnf install kmod-v4l2loopback
    ```
  * Fedora Silverblue/Kinoite:
    ```bash
    rpm-ostree install kmod-v4l2loopback
    ```
  * Arch Linux-based/Manjaro:
    
    You will need to install the kernel headers package of your actual kernel beforehand or the module will not be completely installed.
    ```bash
    sudo pacman -S v4l2loopback-dkms
    ```
  OBS Studio will normally load the module while starting the virtual camera if the module was not already loaded. This requires a working `polkit` setup.

  Alternatively, you can also load the module manually using `modprobe v4l2loopback exclusive_caps=1 card_label='OBS Virtual Camera'`. You can also use `modprobe.d` conf files to automate this.

  In either case, please refer to your distros documentation on how to do this.

## Supported builds

The OBS Project maintains two official, supported Linux builds of OBS Studio: Flatpak and Ubuntu.

### Flatpak

The Flatpak distribution is recommended for non-Ubuntu distributions.

* Install OBS Studio from [Flathub](https://flathub.org/apps/details/com.obsproject.Studio)

### Ubuntu

* Enable the multiverse repo in Ubuntu's software center
* Install OBS Studio on Ubuntu 18.04 or later using:
  ```
  sudo add-apt-repository ppa:obsproject/obs-studio
  sudo apt update
  sudo apt install obs-studio
  ```

## Unofficial builds

Please note that any install directions/packages for Linux/FreeBSD distributions listed as *unofficial* means that they are community provided, and any support for those packages should be directed at the appropriate distro/package maintainers.

Read the [Unofficial Linux builds](unofficial-linux-builds) guide for installation instructions on other Linux distributions, including:

* Arch Linux
* Debian
* Fedora
* Gentoo
* Manjaro
* NixOS
* OpenMandriva
* OpenSUSE
* snappy
* Solus
* UOS/Deepin
* Void

# FreeBSD

Install OBS Studio:
```sh
pkg install obs-studio
```