# README


  A smithy for rusty Wayland compositors


## Goals

Smithay aims to provide building blocks to create wayland compositors in Rust. While not
being a full-blown compositor, it'll provide objects and interfaces implementing common
functionalities that pretty much any compositor will need, in a generic fashion.

It supports the [core Wayland protocols](https://gitlab.freedesktop.org/wayland/wayland), the official [protocol extensions](https://gitlab.freedesktop.org/wayland/wayland-protocols), and *some* external extensions, such as those made by and for [wlroots](https://gitlab.freedesktop.org/wlroots/wlr-protocols) and [KDE](https://invent.kde.org/libraries/plasma-wayland-protocols)

Also:

- **Documented:** Smithay strives to maintain a clear and detailed documentation of its API and its
  functionalities. Compiled documentations are available on [docs.rs](https://docs.rs/smithay) for released
  versions, and [here](https://smithay.github.io/smithay) for the master branch.
- **Safety:** Smithay will target to be safe to use, because Rust.
- **Modularity:** Smithay is not a framework, and will not be constraining. If there is a
  part you don't want to use, you should not be forced to use it.
- **High-level:** You should be able to not have to worry about gory low-level stuff (but
  Smithay won't stop you if you really want to dive into it).

## Getting started

If you want to learn how to build a compositor with Smithay, consider this [getting started](https://github.com/Smithay/smithay/blob/master/GETTING_STARTED.md) guide.

## Anvil

Smithay as a compositor library has its own sample compositor: anvil.

To get information about it and how you can run it visit [anvil README](https://github.com/Smithay/smithay/blob/master/anvil/README.md)

## Other compositors that use Smithay

- [Cosmic](https://github.com/pop-os/cosmic-epoch): Next generation Cosmic desktop environment
- [Catacomb](https://github.com/catacombing/catacomb): A Wayland Mobile Compositor
- [emskin](https://github.com/emskin/emskin): A nested Wayland compositor for embedding any app inside Emacs
- [MagmaWM](https://github.com/MagmaWM/MagmaWM): A versatile and customizable Wayland Compositor
- [Niri](https://github.com/YaLTeR/niri): A scrollable-tiling Wayland compositor
- [Strata](https://github.com/StrataWM/strata): A cutting-edge, robust and sleek Wayland compositor
- [Pinnacle](https://github.com/Ottatop/pinnacle): A WIP Wayland compositor, inspired by AwesomeWM
- [Sudbury](https://gitlab.freedesktop.org/bwidawsk/sudbury): Compositor designed for ChromeOS
- [wprs](https://github.com/wayland-transpositor/wprs): Like [xpra](https://en.wikipedia.org/wiki/Xpra), but for Wayland, and written in
Rust.
- [Local Desktop](https://github.com/localdesktop/localdesktop): An Android app for running GUI Linux via PRoot and Wayland.
- [Otto](https://github.com/nongio/otto): A gesture-driven stacking compositor.

## System Dependencies

(This list can depend on features you enable)

- `libwayland`
- `libxkbcommon`
- `libudev`
- `libinput`
- `libgbm`
- [`libseat`](https://git.sr.ht/~kennylevinsen/seatd)
- `xwayland`
