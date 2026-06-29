This page is intended as a guide for those who wish to build the HEAD of sway and wlroots for testing or development purposes. This page isn't relevant to end-users.

# Dependencies

You're going to need the following tools to get started:

* [git](https://git-scm.com/)
* [gcc](https://gcc.gnu.org/) or [clang](https://clang.llvm.org/)
* [meson](https://mesonbuild.com/)
* [ninja](https://ninja-build.org/)

You'll also need the dependencies, which you can find in the [README](https://github.com/swaywm/sway/blob/master/README.md). If you don't have recent enough versions of some of the dependencies, you can build them as subprojects (see below).

## Alpine

Look at the package list in [Sway CI manifest](https://github.com/swaywm/sway/blob/master/.builds/alpine.yml).

## Arch Linux

The Arch User Repository (AUR) has the convenient `sway-git` and `wlroots-git` packages, which contain everything you'll need to compile their respective projects. Use your preferred AUR helper to install these.

Alternatively, look at the package list in [Sway CI manifest](https://github.com/swaywm/sway/blob/master/.builds/archlinux.yml).

## Debian

On Debian-based distributions, library packages are commonly suffixed by `-dev`.

You can install most of the packages with
```sh
apt build-dep sway
```

Currently you need:
```sh
apt install glslang-tools libcairo2-dev libcap-dev libdbus-1-dev libdisplay-info-dev libevdev-dev libgdk-pixbuf2.0-dev libinput-dev libjson-c-dev libliftoff-dev libpam0g-dev libpango1.0-dev libpcre2-dev libpixman-1-dev libseat-dev libsystemd-dev libvulkan-dev libwayland-dev libwayland-egl1 libwlroots-dev libxcb-ewmh-dev libxkbcommon-dev meson pkgconf scdoc tree wayland-protocols
```

## Fedora

Fedora requires installing all of the dependencies one-by-one. If a dependency is outdated, build it as a subproject (see below).

```sh
dnf install -y git gcc meson ninja-build wayland-devel mesa-libEGL-devel mesa-libGLES-devel mesa-dri-drivers xorg-x11-server-Xwayland libdrm-devel libgbm-devel libxkbcommon-devel libudev-devel pixman-devel libinput-devel libevdev-devel systemd-devel cairo-devel libpcap-devel json-c-devel pam-devel pango-devel pcre-devel gdk-pixbuf2-devel hwdata-devel
```

## FreeBSD

Look at the package list in [Sway CI manifest](https://github.com/swaywm/sway/blob/master/.builds/freebsd.yml).

## Nix

A simple way to get all the needed packages is to use `nix-shell`. Note that packages should come from `nixpkgs-unstable`, and nix default hardening should be disabled:
```sh
nix-shell -p cairo cmake gdk-pixbuf glslang hwdata json_c lcms libGL libcap libdisplay-info libdrm libevdev libgbm libinput libliftoff libxkbcommon mesa meson ninja pango pcre2 pixman pkg-config scdoc seatd tree vulkan-loader wayland wayland-protocols wayland-scanner xorg.xcbutilerrors xorg.xcbutilrenderutil xorg.xcbutilwm xwayland -I nixpkgs=http://channels.nixos.org/nixpkgs-unstable/nixexprs.tar.xz --command "export NIX_HARDENING_ENABLE=; return"
```

# Compiling as a subproject

You can build and run sway directly without installing it. A subproject allows to easily work on wlroots and sway at the same time.

```sh
# Clone repositories
git clone https://github.com/swaywm/sway.git
cd sway
git clone https://gitlab.freedesktop.org/wlroots/wlroots.git subprojects/wlroots

# Build sway and wlroots
meson setup build/
ninja -C build/

# Start sway
build/sway/sway
```

To enable the address sanitizer (ASan) and the undefined behavior sanitizer (UBSan), add `-Db_sanitize=address,undefined` to the `meson` command.

In order to be able to collect core dumps on ASan failures (to inspect variable state at the point of failure, for instance), you must specify `ASAN_OPTIONS=abort_on_error=1:disable_coredump=0:unmap_shadow_on_exit=1` in the environment that you launch `sway` in.

When pulling from the Sway repo, remember to also pull from the wlroots repo.

The wlroots CI ensures it always builds on Arch Linux, Alpine edge and FreeBSD. If you're using another distribution which doesn't ship new enough dependencies, it's possible to build them as subprojects, for instance:

```sh
git clone https://gitlab.freedesktop.org/wayland/wayland.git subprojects/wayland
git clone https://gitlab.freedesktop.org/wayland/wayland-protocols.git subprojects/wayland-protocols
git clone https://gitlab.freedesktop.org/emersion/libdisplay-info.git subprojects/libdisplay-info
git clone https://gitlab.freedesktop.org/emersion/libliftoff.git subprojects/libliftoff
git clone https://gitlab.freedesktop.org/mesa/drm.git subprojects/libdrm
git clone https://git.sr.ht/~kennylevinsen/seatd subprojects/seatd
```

If you don't have Sway installed on your system or if you want to test swaybar/swaymsg/swaynag changes, you can populate your `PATH` like so:

```sh
export PATH=build/swaybar:build/swaymsg:build/swaynag:$PATH
```

Alternatively, you can also add `swaybar_command`/`swaynag_command`/`swaybar_command` to your config with custom executable paths.

# System-wide installation

This section is relevant if you want to install both wlroots and sway system-wide (not using a subproject).

## Variables

_If you don't want to add the paths below to your `~/.profile`, you can paste these lines into your terminal to set the variables for the current terminal session only._

Ensure that `/usr/local/bin` is in your `PATH` by executing `echo $PATH`. If it isn't, open `~/.profile` and add:

```sh
export PATH=/usr/local/bin:$PATH
```

Ensure that your `PKG_CONFIG_PATH` contains `/usr/local/lib/pkgconfig`, `/usr/local/lib64/pkgconfig`, and `/usr/local/share/pkgconfig` by executing `echo $PKG_CONFIG_PATH`. If it doesn't, open `~/.profile` and add: 

```sh
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
export PKG_CONFIG_PATH=/usr/local/lib64/pkgconfig:$PKG_CONFIG_PATH
export PKG_CONFIG_PATH=/usr/local/share/pkgconfig:$PKG_CONFIG_PATH
```

Ensure that your `LD_LIBRARY_PATH` contains `/usr/local/lib/` and `/usr/local/lib64/` by executing `echo $LD_LIBRARY_PATH`. If it doesn't, open the `~/.profile` file located in your home directory and add: 

```sh
export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/lib64/:$LD_LIBRARY_PATH
```

Execute `source ~/.profile` to update the variables for your current terminal session. You should ensure that your chosen shell sources `~/.profile` on login (you may need to delete `~/.bash_profile` for it to take precedent).

## Compiling

You're now ready to compile wlroots, which is the Wayland compositor library used by sway. 
* Clone the [`wlroots`](https://gitlab.freedesktop.org/wlroots/wlroots/) repository with git
* Execute `meson setup build`, which will create the `build` directory
* Execute `ninja -C build` to build
* Execute `sudo ninja -C build install` to install
* Verify that either `/usr/local/lib` or `/usr/local/lib64` contain `libwlroots.so`

Now that wlroots is built and installed, you can build sway.
* Clone the [`sway`](https://github.com/swaywm/sway) repository with git
* Execute `meson setup build`, which will create the `build` directory
* Execute `ninja -C build` to build 
* Execute `sudo ninja -C build install` to install 
* Verify that `/usr/local/bin` contains the `sway`, `swaybar`, `swaylock`, etc. binaries

Since sway and wlroots development moves fast, it's common to have issues compiling sway if your installed version of wlroots is behind. As a first step of compile error troubleshooting, pull, build, and reinstall wlroots.