# libxkbcommon


**libxkbcommon** is a keyboard keymap compiler and support library which
processes keymaps as defined by the [XKB] \(X Keyboard Extension) specification
(minus some legacy features). It also contains a module for handling *Compose*
and dead keys, a separate *registry* library for listing available keyboard
layouts and a fair set of <!--!
@rawHtml --><abbr title="Command-Line Interface">CLI</abbr><!--!
@endRawHtml --> *tools* to support keyboard layouts development.

libxkbcommon is the standard keymap handling library on Wayland and is used by
compositors, toolkits, and applications to handle keyboard state and translate
key events into characters and actions.

[XKB]: doc/introduction-to-xkb.md

## Quick Guide

### Introduction to XKB

See [Introduction to XKB][XKB] for the essentials of XKB concepts and how a
keymap is built.

### Using the library


[Library quick guide](doc/quick-guide.md)

[API Documentation](https://xkbcommon.org/doc/current/topics.html)

[Release notes](doc/release-notes.md)

[FAQ](doc/faq.md#api)

### Developing keyboard layouts


[Custom layouts](doc/custom-configuration.md)

[Keymap format](doc/keymap-text-format-v1-v2.md)

[Tools](./README.md#tools)

[FAQ](doc/faq.md)

## Building

libxkbcommon requires:

- a C compiler supporting C11
- XKB registry (optional): `libxml2`
- X11 features (optional): `libxcb` and `libxcb-xkb`
- Wayland features (optional): `wayland-client`, `wayland-protocols`, `wayland-scanner`

libxkbcommon is built with [Meson](http://mesonbuild.com):

```shell
meson setup build
meson compile -C build
meson test -C build # Run the tests.
```

To build for use with Wayland, you can disable X11 support while still
using the X11 keyboard configuration resource files thusly:

```shell
meson setup build \
      -Denable-x11=false \
      -Dxkb-config-root=/usr/share/X11/xkb \
      -Dx-locale-root=/usr/share/X11/locale
meson compile -C build
```


@include meson.options


## API

While libxkbcommon’s API is somewhat derived from the classic XKB API as found
in `X11/extensions/XKB.h` and friends, it has been substantially reworked to
expose fewer internal details to clients.

See the [API Documentation](https://xkbcommon.org/doc/current/topics.html).

## Tools

Libxkbcommon offers a set of <abbr title="Command-Line Interface">CLI</abbr>
<code>tools</code>, grouped under the <code>xkbcli</code> application:


It may require the installation of the package `libxkbcommon-tools` or similar
name.

## Layouts database

libxkbcommon *does not distribute a keyboard layout dataset itself*, other than
for testing purposes.  The most common dataset is **xkeyboard-config**, which is
used by all current distributions for their XKB data.  Further information
on xkeyboard-config is available at its [homepage][xkeyboard-config-home] and at
its [repository][xkeyboard-config-repo].

The dataset for *Compose* is distributed in [libX11], as part of the X locale
data.

[xkeyboard-config-home]: https://www.freedesktop.org/wiki/Software/XKeyboardConfig
[xkeyboard-config-repo]: https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config
[libX11]: https://gitlab.freedesktop.org/xorg/lib/libx11

## Compatibility with X11

libxkbcommon is compatible with X11, except for some obscure features.

See the [Compatibility](doc/compatibility.md) page for further details.

## License

See the [LICENSE](doc/license.md) file.

## Credits

Many thanks are due to Dan Nicholson for his heroic work in getting xkbcommon
off the ground initially.
