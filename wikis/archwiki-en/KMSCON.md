# KMSCON

From the project's git repository:

:Kmscon is a simple terminal emulator based on linux kernel mode setting. It is an attempt to replace the in-kernel VT implementation with a userspace console.

Kmscon can function as a drop-in replacement for the in-kernel linux-console. Features include:

* Full vt220 to vt510 implementation.
* Full internationalization support:
** Kmscon supports printing full Unicode glyphs, including the CJK ones.
** Kmscon provides internationalized keyboard handling through libxkbcommon, thus allowing it to use the full range of keyboard layouts supported in X keyboard.
* Hardware accelerated rendering.
* Scroll support.
* Mouse/Touchscreen support.
* On screen font resize support, including TTF fonts.
* Multi-seat capability.

## Installation
Install the  package.

## Configuration
Despite its name, KMS is not a hard requirement for kmscon. It supports the following video backends:

* drm3d (Linux DRM hardware-rendering backend).
* drm2d (Linux DRM software-rendering backend).
* fbdev (Linux framebuffer).

Make sure one of them is available on your system.

Normally, there is a special systemd configuration for tty1. To be conservative, you can continue to run the traditional agetty on tty1 and only run kmscon on some, or all, the other virtual terminals. In case you want to be less conservative, you can run kmscon on tty1 as well.

To enable kmscon on ttyX, enable . As stated in the previous paragraph, tty1 is unusual in that  is enabled by default. Therefore, it should be disabled before using . Also note  sets  to 6, by default.

To enable kmscon on all virtual terminals, disable  and enable .

This will make systemd to start kmscon instead of agetty on each VT. More precisely, this will make systemd-logind use  instead of  for new VTs. Additionally, all other systemd units that use  will not be affected by this change.

If kmscon cannot start for whatever reason, this unit will cause  to be started instead. Furthermore, if no VTs are available, this unit will not start anything.

## Tips and tricks
## Switching VT
The familiar  key combination will not change into another VT when the current VT is . Only  is working in this circumstances.

## CJK support
Kmscon supports rendering CJK characters through the default font engine . However, fontconfig has to be globally configured to map the monospace font alias to proper CJK fonts. For Chinese users, the following template is provided and proved to result in satisfactory Chinese characters rendering:

Alternatively, we can add the following line to  for globally configuring kmscon using the fonts:

See .

You need to have  and , both available from the official repositories, installed.

## Automatic login
It is possible to login as user username automatically without asking for password by adding this to

Or as user root:

## HiDPI support
You can change font size on the fly with , ,  shortcuts.

## Troubleshooting
## Root cannot login
If you cannot login as root check  files, if you have enabled . You need to disable the  module by removing or commenting out the corresponding line eg. in .

## Window managers cannot be started from KMS console
Use the  wrapper to launch your favourite desktop environment.

## Gnome Session does not start
You need to set the wayland type flag for your terminal. Add type=wayland to the pam_systemd.so line in

## Problems with switching between Xorg and kmscon
You may want to add  to  if you have problems with switching between Xorg and kmscon. Another possibility would be editing the systemd service file.

## No audio control
As version 7, if you cannot control the audio, add your user to the  user group. Be aware of the shortcomings of this choice.

## Vim does not clear terminal output
Vim might open without clearing the terminal output, it is still possible to edit the file but the text will not be visible until it is changed. As a workaround, try setting the environment variable . Alternatively, another vim-like editor like Neovim might work.
