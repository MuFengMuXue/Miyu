# Installation from Source

All commands on this page, unless otherwise specified, are expected to be run as an unprivileged user (not root). Whenever root privileges are necessary, `sudo` will be used. If `sudo` is unavailable you may become root using `su -`, at which point you may execute any command as the root user. Use `exit` to become a normal user again.

## Distribution Specifics

### Arch Linux

Arch Linux includes a [package and PKGBUILD](https://archlinux.org/packages/extra/x86_64/easyeffects/) in Extra Repository.

Run `sudo pacman -S easyeffects` to install binary package.


### Fedora

```
sudo dnf builddep easyeffects
```

## GNOME Builder

You can clone the repository, and then easily test builds with GNOME Builder's "build" and "run" buttons. It is recommended to install GNOME Builder from Flathub. 

Note many Plugins do not currently work when running GNOME Builder Flatpak builds due to GNOME Builder limitations/use of Flatpak runtime extensions. To workaround this issue, follow the below instructions to install with `flatpak-builder` manually.

## Flatpak-builder

If you need to fully install a Flatpak for testing, and/or want the plugins to fully work, you can build it without GNOME Builder. Instead you can use `flatpak-builder` directly.

Ensure `flatpak` and `flatpak-builder` are installed and available on your system. If it is not installed, you can find detailed installation instructions at https://flatpak.org/setup/.

First ensure the flathub repo is added to your user flatpak installation:
```
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

Within this repo:
```
flatpak-builder build-dir --install-deps-from=flathub --user --install util/flatpak/com.github.wwmm.easyeffects.Devel.json --force-clean --ccache
```

Important: To use Linux Studio Plugins, Zam Plugins, and MDA Plugins you will have to install the Flatpak plugin packages separately. They are available from Flathub, and are automatically installed when installing the stable Flathub package.

```
flatpak install flathub org.freedesktop.LinuxAudio.Plugins.Calf//25.08 org.freedesktop.LinuxAudio.Plugins.LSP//25.08 org.freedesktop.LinuxAudio.Plugins.ZamPlugins//25.08 org.freedesktop.LinuxAudio.Plugins.MDA//25.08
```

You can run the build with:
```
flatpak run com.github.wwmm.easyeffects.Devel
```

You can remove the Flatpak build and its configurations with:
```
flatpak remove com.github.wwmm.easyeffects.Devel --delete-data
```

Note the canonical copy of the Flatpak manifest is kept at https://github.com/wwmm/easyeffects. The downstream repo https://github.com/flathub/com.github.wwmm.easyeffects contains a slighly modified copy of part of the manifest (needed due to Flathub requiring the manifest in the root directory).

## Download

Clone the git repository.

```
git clone https://github.com/wwmm/easyeffects.git
cd easyeffects
```

**Optional:** Select a release

Substitute `v6.2.0` with the [latest release](https://github.com/wwmm/easyeffects/tags).

```
git checkout v6.2.0
```

## Build & Install

```
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -G Ninja ..
ninja
sudo ninja install
```

See the [official instructions for getting meson](http://mesonbuild.com/Getting-meson.html) for more information.

## Build and run without installing

### Run EasyEffects from build directory

Inside Easyeffects source code folder run the commands below:
```
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -G Ninja ..
ninja
cd src
./easyeffects
```