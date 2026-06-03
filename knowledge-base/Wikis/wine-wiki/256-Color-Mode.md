256-color displays that used 8 bits per pixel were commonplace in the
1990's. Each of the 256 colors was defined as a 24-bit value, so the
operating system could choose an arbitrary palette of 256 colors from a
selection of 16,777,216 colors. Nowadays, practically everything uses 24
bits per pixel, the video hardware has no palette, and each pixel is
free to be any of the possible 16,777,216 colors. Nevertheless, some
applications insist upon running in 256-color mode and refuse to run
unless you reduce your display settings from 24bpp to 8bpp, which is
rarely possible on modern hardware and software. If your application
says that it needs 8bpp or 256 colors even though you have millions of
colors available, you may be able to get it working with one of the
workarounds below.

## DxWnd

[DxWnd](https://sourceforge.net/projects/dxwnd/) is a remarkable tool
for making old games work on new versions of Windows, and it works on
Wine too! To get started, click Edit, then Add, and put the location of
the misbehaving application's EXE file in the Path textbox. Depending on
the application, some or all of the following settings may be helpful
for forcing 256-color mode:

- Video \> Initial virtual color setting \> 8 BPP
- Video \> Initial virtual color setting \> Lock
- GDI \> Synchronize GDI to ddraw palette
- Hook \> Do hook update

## X in X

It's possible to run an X11 server on top of an X11 server, for example
running an 8bpp server for the misbehaving application on top of the
24bpp server you use for everything else. This solves the color mode
problem, but your application still might not start because 3D
acceleration won't be available in the nested server.

When using this approach, bear in mind:

- **You must use a window manager**, and the window manager must be one
  that supports color palettes (e.g.
  [Openbox](https://openbox.org/wiki/Main_Page)).
- Wherever `:1` is written you may use `:`*`n`* instead, where *n* is an
  unused display number. The default display is usually `:0`.
- If your shell doesn't accept the `DISPLAY=:1 wine explorer` syntax,
  you may need to use something like `env DISPLAY=:1 wine explorer`
  instead.

### Xephyr

Once you have installed
[Xephyr](https://www.freedesktop.org/wiki/Software/Xephyr/) (Ubuntu:
package xserver-xephyr, in universe), you should be able to run
something like the following:

`Xephyr :1 -ac -screen 800x600x8 &`
`DISPLAY=:1 openbox &`
`DISPLAY=:1 wine explorer`

This will create a 800x600 display, in a window, with 8-bit color, and
display a Wine file explorer in it.

In some cases, you may get better results by starting Xephyr with the
parameter `-cc 2` to use the default Xorg palette (StaticColor) instead
of the default Windows palette (PseudoColor).

### Xnest

Once you have installed
[Xnest](https://www.x.org/archive/X11R7.5/doc/man/man1/Xnest.1.html)
(Ubuntu: package xnest, in main), you should be able to run the
following:

`Xnest :1 -depth 8 &`
`DISPLAY=:1 openbox &`
`DISPLAY=:1 wine explorer`

This will create a display in a window, with 8-bit color, and display a
Wine file explorer in it. Xnest depends on the parent X11 server for
various things; in some cases Xnest won't work (`-depth 8` fails on many
systems).

## Native X

Of course you can use just plain ol' X, but that will only work if your
video card and driver still support palettized 8bpp displays.

### xinit

`xinit /usr/bin/xterm -- :1 -ac -depth 8`

Then in xterm:

`openbox &`
`wine explorer`

You can switch between several running X servers and consoles by using
the Ctrl+Alt+F1 ... Ctrl+Alt+F10 keyboard shortcuts. On Ubuntu, the
initial X server is on tty7 (Ctrl+Alt+F7), and the new X server will be
on tty9 (Ctrl+Alt+F9).

Note: You may get a "user not authorized to run the X server, aborting"
error message (this happens on Debian and Ubuntu). To work around this,
either run xinit as root (or with sudo), or change the
`allowed_users=console` line in /etc/X11/Xwrapper.config to read
`allowed_users=anybody`. If you run xinit as root, a root shell will be
running in the xterm, so you need to start another xterm as your normal
user (switch back to your main X server, and run `DISPLAY=:1 xterm` in a
non-root shell). Remember: Don't run Wine as root!

### Mac OS X

The X server that ships with MacOS X has a preferences setting for the
color depth, simply set it where you want it and restart the X server.
Done.
