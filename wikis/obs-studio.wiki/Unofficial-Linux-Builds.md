## Table of Contents

* [Arch Linux/Manjaro](#arch-linuxmanjaro)
* [Debian](#debian)
* [Fedora](#fedora)
* [Gentoo](#gentoo)
* [NixOS](#nixos)
* [OpenMandriva](#openmandriva)
* [OpenSUSE](#opensuse)
* [snappy](#snappy)
* [Solus](#solus)
* [UnionTechOS/Deepin](#uniontechosdeepin)
* [Void](#void)

***

# About unofficial builds

Please note that the instructions for the following Linux distributions means that they are community provided, and any support for those packages should be directed at the appropriate distro/package maintainers.

For official builds of OBS Studio for Flatpak (all distributions) and Ubuntu, see the [Install Instructions](install-instructions#linux).

# Unofficial builds

## Arch Linux/Manjaro

### Install from AUR

There is OBS packages present in the [AUR](https://wiki.archlinux.org/title/Arch_User_Repository).

Use your favorite AUR helper to install one of those package, but avoid using Pamac (Add/Remove Software) for the first install\*.

* **`obs-studio-browser`** provides OBS Studio with:
  * VST 2 plugins, RIST protocol and AJA device support.
  * Browser module with the same CEF as official builds.
* **`obs-studio-tytan652`** provides OBS Studio with:
  * VST 2 plugins, RIST protocol and AJA device support.
  * Browser module with the same CEF as official builds.
  * Some quality of life patches and fixes.
* **`obs-studio-rc`** provides OBS Studio latest version (including Beta and Release Candidates) with:
  * VST 2 plugins, RIST protocol and AJA device support.
  * Browser module with the same CEF as official builds.

Most of those packages also replace `vlc` with `vlc-luajit` to provide VLC sources and `ffmpeg` with `ffmpeg-obs` to provide RIST protocol support.

* More [AUR](https://aur.archlinux.org/packages/?O=0&K=obs-studio-) packages are also available.

\*Pamac has known issues about managing package replacement leading to being unable to install some AUR Packages.

### Install from Arch Linux/Manjaro official repository

* Graphical: search obs-studio package on Pamac (Add/Remove Software)
* Command Line:
  ```bash
  sudo pacman -S obs-studio
  ```

* **Warning:** Arch based distributions do not respect all `OBS-Studio` Prerequisites for running in the `wayland` Desktop Environment. This can result in random crashes, and/or OBS-Studio not working entirely. If you are installing OBS-Studio on `*Arch` using `wayland`, please ensure you install the `qt6-wayland` Prerequisite.

    ```bash
    sudo pacman -S qt6-wayland
    ```

## Debian

Debian 9.0 "Stretch" or newer is required.  

~~**Also note that as of 2021-06-13, this package is the outdated 0.0.1 version. It should still work, but won't have all new improvements. Build from source to get the newest version.**~~

As of 2023-05-19 Debian 11 "Bullseye" provides 26.1.2.

* First, make sure you have everything up-to-date.

   ```bash
   sudo apt update
   ```

* FFmpeg is required.  If you do not have the FFmpeg installed (if you're not sure, then you probably don't have it), you can get it with the following command (or compile it yourself):

   ```bash
   sudo apt install ffmpeg
   ```

* Finally, install OBS Studio.

   ```bash
   sudo apt install obs-studio
   ```

## Fedora

* OBS Studio is included in Fedora. You can install OBS with the following command:

   ```bash
   sudo dnf install obs-studio
   ```

* Additionally Fedora provides the Browser, VLC, vkcapture and WebKitGTK plugins in separate packages that you can install:

   ```bash
   sudo dnf install obs-studio-plugin-vlc-video obs-studio-plugin-vkcapture obs-studio-plugin-webkitgtk
   ```

* To install the x264 encoding plugin you need to enable the third-party RPM Fusion repository on your system:

   * [Enable RPM Fusion on your system](https://rpmfusion.org/Configuration)

   * Install x264 encoding plugin

      ```bash
      sudo dnf install obs-studio-plugin-x264
      ```

* Support for NVIDIA Hardware accelerated encoding is provided by RPM Fusion

   * [Enable RPM Fusion on your system](https://rpmfusion.org/Configuration)

   * For NVIDIA Hardware accelerated encoding, make sure you have CUDA installed:

      ```bash
      sudo dnf install xorg-x11-drv-nvidia-cuda
      ```

   * If you have an older card, use this command instead:
      ```bash
      sudo dnf install xorg-x11-drv-nvidia-340xx-cuda
      ```

* Support for AMD Hardware accelerated H.264 and H.265 encoding is provided by RPM Fusion as well (AV1 is available without it):

   * [Enable RPM Fusion on your system](https://rpmfusion.org/Configuration)

   * Swap the Fedora Mesa package for the RPM Fusion package:
      ```bash
      sudo dnf swap mesa-va-drivers mesa-va-drivers-freeworld
      ```


## Gentoo

Command-line: can be installed using portage by the following command:

```bash
sudo emerge media-video/obs-studio
```

See https://packages.gentoo.org/packages/media-video/obs-studio for available versions and more information.

## NixOS

Command-line: can be installed by the following command:

```bash
nix-env -i obs-studio
```

## OpenMandriva

* OBS Studio is included in OpenMandriva Lx3 non-free repository and in restricted repository for upcoming Lx4 release - available now as Cooker.

### OpenMandriva Lx3

* Graphical: search and install "obs-studio" on "OpenMandriva Install and Remove Software" (Rpmdrake)
* Command-line: install it as root (su or sudo) via terminal/konsole with the following command:

   ```bash
   urpmi obs-studio
   ```

### OpenMandriva Lx4
* Graphical: search and install "obs-studio" on "OpenMandriva Software Management" (dnfdragora)
* Command-line: install it as root (su or sudo) via terminal/konsole with the following command:

   ```bash
   dnf install obs-studio
   ```

## openSUSE
* The Packman repository contains the obs-studio package since it requires
  the fuller version of FFmpeg which is in Packman for legal reasons. If you
  do not already have the Packman repository add it as shown below.
  * For openSUSE Tumbleweed:

   ```bash
   sudo zypper ar -cfp 90 http://ftp.gwdg.de/pub/linux/misc/packman/suse/openSUSE_Tumbleweed/ packman
   ```

  * For openSUSE Leap 15.2 (If you're using a derivative of Leap, replace $releasever by your leap release number) :

   ```bash
   sudo zypper ar -cfp 90 'https://ftp.gwdg.de/pub/linux/misc/packman/suse/openSUSE_Leap_$releasever/' packman
   ```

* The Packman version of FFmpeg should be used for full codec support. To
  ensure any existing codec packages are switched to Packman versions
  execute the following before installing obs-studio.

   ```bash
   sudo zypper dup --from packman --allow-vendor-change
   ```

* Install the obs-studio package.

   ```bash
   sudo zypper in obs-studio
   ```

Links:
* 1 click install, direct rpm links, and download counts:
    http://packman.links2linux.org/package/obs-studio
* Build information:
    https://pmbs.links2linux.de/package/show/Multimedia/obs-studio

## snappy

* If you haven't already, [install snapd](https://docs.snapcraft.io/core/install) (ignore the Support Overview which is outdated).

* Install OBS Studio.

   ```bash
   sudo snap install obs-studio
   ```

## Solus

* Graphical: search `obs-studio` in Software Center
* Command-line: install it as root (su or sudo) via terminal/konsole with the following command:
   ```bash
   eopkg install obs-studio
   ```

See https://nixos.org/wiki/OBS for further instructions

## UnionTechOS/Deepin

* First, Open the App Store and search for OBS Studio.
   
![image](https://user-images.githubusercontent.com/25455400/189478750-24a6976f-a449-4b77-9482-aa1da988cc5c.png)

* Second, Click Install(安装) and wait for automatic installation to your desktop or dde-applist

* Third, You can find OBS Studio on your desktop or dde-applist

* Let's go to live boardcast it.
* If you need NVIDIA's CUDA to use the NVENC encoder
   ```bash
   sudo apt install nvidia-cuda-toolkit
   ```

## Void

* First make sure your repositories are up-to-date. OBS is available on the `multilib` repos if you need the 32-bit build.

   ```bash
   sudo xbps-install -S
   ```

* Then install OBS Studio. Any missing dependencies will be installed automatically.
  * If it refuses to install, try running `sudo xbps-install -Su` to update everything first.

   ```bash
   sudo xbps-install obs
   ```