# ProtonPlus

A modern compatibility tools manager for Linux.

Source: https://github.com/Vysp3r/ProtonPlus

## Features

- Multi-Launcher Support: Manage tools for Steam, Lutris, Heroic, Bottles, and more.
- Steam Integration: Change compatibility tools and launch options for your Steam games directly.
- Easy Updates: One-click updates for your installed compatibility tools.
- CLI Support: Manage your tools from the terminal.
- Modern UI: Built with GTK4 and Libadwaita for a consistent GNOME experience.
- Tool Management: See which tools are currently in use by your games.

## Supported Launchers

- Steam
- Lutris
- Heroic Games Launcher
- Bottles
- WineZGUI

## Supported Compatibility Tools

### Proton & Wrappers

- Steam Tinker Launch
- Proton-GE
- Proton-GE RTSP
- Proton-CachyOS
- DW-Proton
- Proton-EM
- Proton-Tkg
- Luxtorpeda
- Boxtron
- Roberta

### Wine Builds

- Wine-Vanilla
- Wine-Staging
- Wine-Staging-Tkg
- Wine-Proton

### Graphics Libraries (DXVK & VKD3D)

- DXVK (doitsujin)
- DXVK (Sarek)
- DXVK Async (Sarek)
- DXVK GPL+Async (Ph42oN)
- VKD3D-Proton
- VKD3D-Lutris

## Installation

Main installation method is Flathub: https://flathub.org/apps/com.vysp3r.ProtonPlus

### Community Packages

| Distribution | Repository | Maintainer |
| --- | --- | --- |
| Arch Linux | AUR | yochananmarqos |
| Fedora | Copr | wehagy |
| Fedora | Terra | Owen Zimmerman |
| NixOS | nixpkgs | Seth |
| Ubuntu | Pacstall | Vysp3r |
| openSUSE | OBS | rrahl0 |
| Void Linux | Official repository | xJayMorex |
| Gentoo | Overlay | amielke |

## Building from Source

### Requirements

- git
- ninja
- meson >= 1.0.0
- vala
- gtk4
- libadwaita >= 1.6
- json-glib
- libsoup-3.0
- libarchive
- desktop-file-utils
- libgee

### Native Build

1. Install dependencies (Example for Fedora):
   ```bash
   sudo dnf install git gettext 'meson >= 1.0.0' vala desktop-file-utils libappstream-glib \
     'pkgconfig(gee-0.8)' 'pkgconfig(glib-2.0)' 'pkgconfig(gtk4)' 'pkgconfig(json-glib-1.0)' \
     'pkgconfig(libadwaita-1) >= 1.6' 'pkgconfig(libarchive)' 'pkgconfig(libsoup-3.0)'
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/Vysp3r/ProtonPlus.git
   cd ProtonPlus
   ```

3. Build and run:
   ```bash
   ./scripts/build.sh native run
   ```

4. Install (Optional):
   ```bash
   cd build-native
   sudo ninja install
   ```

### Flatpak Build

1. Install Flatpak and Builder:
   ```bash
   sudo dnf install git flatpak
   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   flatpak install org.flatpak.Builder
   ```

2. Install Runtimes:
   ```bash
   flatpak install runtime/org.gnome.Sdk/x86_64/50 runtime/org.gnome.Platform/x86_64/50 \
     runtime/org.freedesktop.Sdk.Extension.vala/x86_64/25.08
   ```

3. Build and run:
   ```bash
   ./scripts/build.sh local run
   ```

## Translate

Help translate ProtonPlus using Weblate: https://hosted.weblate.org/projects/protonplus/protonplus/
