# Fbterm

Fbterm (Frame buffer terminal emulator) is standalone replacement of Linux kernel terminal that can function outside of graphical environments. It was previously hosted at Google Code, https://code.google.com/archive/p/fbterm/, and it is since 2020 maintained by Debian.

It provides support for fontconfig (and draws text with freetype2, same as Qt/Gtk based GUI applications), up to 10 windows with a scroll-back history for each, auto-detect text encoding with current locale, double width scripts like Chinese, Japanese and more: see https://salsa.debian.org/debian/fbterm/-/blob/master/README.

## Installation
Install the  package. Pay attention to the instructions and minor changes by the included patches.

After installation, to be able to use fbterm as a non-root user add yourself to the  user group.

To enable keyboard shortcuts for non-root users, use setcap to give fbterm the  capability.
 # setcap cap_sys_tty_config+ep /usr/bin/fbterm

## Customization
## Configuration file
The user configuration file is located in . The global  is well commented and serves as a good starting point.

## Fonts
Fbterm uses fontconfig for a list of fonts, trying each sequentially until it is able to render the characters.

To change the fonts that are used, use the  option to select favorites from the list given by .

## Input method support
Fbterm supports diverse input methods by acting as a client for an independent input method framework server. Several such programs are available, see Internationalization#Input method.

## Tips and tricks
## As a non-graphical environment
In the late 2010's, developments in the Linux ecosystem and its framebuffer capabilities, together with cheap and powerful hardware (standard mainstream graphical cards) made things that were difficult in the past possible, and without too much customization or hacking:

* 256 colorschemes support
* display of CJK web pages and documents
* access to a much wider variety of TTF fonts

In addition to the modern capabilities of the framebuffer, for example:

* Watching movies with mpv (e.g. with )
* Screenshots and screencasts with (ex: fbgrab, fbdump)
* PDF and other complex documents display with (ex: fbpdf, jfbview, fbgs)
* Previewing pictures in the ranger file manager (w3mimgdisplay support)
* Running some heavy GUI QT Platform applications (ex: qutebrowser, maps)

Fbterm with other modern text-centric tools make an environment without the concept of windows possible. Combined usage of fbterm with a terminal multiplexer like tmux allows for a very powerful desktop alternative mimicking the use of a window manager. Some examples of this advanced usage from Arch users:

* https://github.com/xlucn/dotfiles - Examples of a dwm alike desktop with fbterm and tmux
* https://github.com/xlucn/fbterm - Some patch examples
* https://github.com/ivanp7/sweet-home - Custom wallpapers, use with tmux and fbi

## Background image
To use a background image, Fbterm can be set to take a screen shot of the frame buffer device when it starts.

The following script (using the  image viewer) is recommended in the man page:

## White font color
By default, fbterm displays the "white" text as a gray color, even using the  switch.
It's possible to get a real white color by doing an echo once inside fbterm, like this:

 echo -en "\e]P7ffffff"
