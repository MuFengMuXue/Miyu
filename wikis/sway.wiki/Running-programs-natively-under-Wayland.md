If your toolkit/library supports this, you can have your apps run natively (without Xwayland) by setting some environment variables (you can add them to your launcher script or a session file if you're using a display manager).

You can disable Xwayland (X clients under Wayland) support by specifying `xwayland disable` in your Sway config.

### About this list

This article is about configuring portable applications to use Wayland natively. For a list of Wayland-native utilities, see [Useful add ons for sway](https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway).

## GTK3

Wayland will be selected by default. Do **not** set `GDK_BACKEND`, it will break apps (e.g. Chromium and Electron).

Starting with version 121, Firefox enables Wayland support by default and you don't need to do anything, for older versions Wayland support in Firefox can be enabled with `MOZ_ENABLE_WAYLAND=1`. Firefox ESR 68 also needs the `--no-remote` flag because of [a bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1555308).

LibreOffice should select Wayland by default. (If not, try `SAL_USE_VCLPLUGIN=gtk3`.)

## Qt5

Wayland is used by default if `XDG_SESSION_TYPE=wayland` is set, which sway does automatically (via [wlroots session.c](https://gitlab.freedesktop.org/wlroots/wlroots/-/blob/master/backend/session/session.c?ref_type=heads)). If not:

```shell
QT_QPA_PLATFORM=wayland-egl
```

To use your monitor's DPI instead of the default of 96 DPI:

```shell
QT_WAYLAND_FORCE_DPI=physical
```

Older versions of Qt always show window decorations. To hide them:

```shell
QT_WAYLAND_DISABLE_WINDOWDECORATION=1
```

NOTE: To enable Wayland support, you might need a package, such as `qtwayland5` for Ubuntu or `qt5-wayland` for Arch Linux.

## Elementary/EFL

```shell
ECORE_EVAS_ENGINE=wayland_egl
ELM_ENGINE=wayland_egl
```

You could set them to `wayland_shm` instead, if you want to use software rendering.

## SDL

SDL3 uses native Wayland [by default](https://github.com/libsdl-org/SDL/commit/f9f7db4e0860).

SDL2 uses [Xwayland by default](https://github.com/libsdl-org/SDL/commit/254fcc90eb22), so use

```shell
SDL_VIDEODRIVER=wayland
```

NOTE: Steam, most games and other (older) binary applications might not work with `wayland` SDL video driver, due to old bundled SDL library. Unset, tweak for specific applications or force newer SDL via

```shell
SDL_DYNAMIC_API=/usr/lib/libSDL2-2.0.so
```

SDL1 doesn't support native Wayland, so use SDL2 via [sdl12-compat](https://github.com/libsdl-org/sdl12-compat).

## Flatpak

```shell
flatpak [--user] run --socket=wayland your-app
```

Or to make it the default socket either for your app or even globally:
```shell
flatpak [--user] override --socket=wayland [your-app]
```

## GLFW

Wayland needs to be selected at compile-time. Arch users can install `glfw-wayland`.

GLFW >= 3.4 adds the ability to support both x11 and wayland and automatically detect & select one at run-time.

## Java under Xwayland

Some Java AWT applications will not display properly unless you set the following.

```shell
_JAVA_AWT_WM_NONREPARENTING=1
```
