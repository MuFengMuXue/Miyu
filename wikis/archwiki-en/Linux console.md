# Linux console

According to Wikipedia:

:The Linux console is a system console internal to the Linux kernel. The Linux console provides a way for the kernel and other processes to send text output to the user, and to receive text input from the user. The user typically enters text with a computer keyboard and reads the output text on a computer monitor. The Linux kernel supports virtual consoles — consoles that are logically separate, but which access the same physical keyboard and display.

This article describes the basics of the Linux console and how to configure the font display. Keyboard configuration is described in the /Keyboard configuration subpage. For alternative console solutions offering more features (full Unicode fonts, modern graphics adapters support, better ability to change the font size, etc.), see KMSCON or similar projects.

## Implementation
The console, unlike most services that interact directly with users, is implemented in the kernel. This contrasts with terminal emulation software, such as Xterm, which is implemented in user space as a normal application. The console has always been part of released Linux kernels, but has undergone changes in its history, most notably the transition to using the framebuffer and support for Unicode.

Despite many improvements in the console, its full backward compatibility with legacy hardware means it is limited compared to a graphical terminal emulator.  The main difference between the Linux console and graphical terminal emulators is the shells in the Linux console are attached directly to TTY devices (), whereas the shells in a graphical terminal emulator are attached to pseudo-TTYs ().

Also, graphical terminal emulators can have many more features than the Linux console, including a richer set of available fonts, multiple tabs/windows, split views, scrollback buffers/sliders, background colors/images (optionally with transparency), etc.  Some of these features can be used in the Linux console with terminal multiplexers, such as Tmux or GNU Screen, or in certain text user interface programs (TUI) typically relying on libraries such as ncurses and the like, e.g. Vim, nano, or Emacs.  These can also be used in graphical terminal emulators, if desired.

## Virtual consoles
The console is presented to the user as a series of virtual consoles. These give the impression that several independent terminals are running concurrently; each virtual console can be logged in with different users, run its own shell and have its own font settings. The virtual consoles each use a device , and you can switch between them by pressing  (where  is equal to the virtual console number, beginning with 1). The device  is automatically mapped to the active virtual console.

See also ,  and .

## Text mode
Since Linux originally began as a kernel for PC hardware, the console was developed using standard IBM CGA/EGA/VGA graphics, which all PCs supported at the time. The graphics operated in VGA text mode, which provides a simple 80x25 character display with 16 colours. This legacy mode is similar to the capabilities of dedicated text terminals, such as the DEC VT100 series. It is still possible to boot in text mode (with ) if the system hardware supports it, but almost all modern distributions (including Arch Linux) use the framebuffer console instead.

## Framebuffer console
As Linux was ported to other non-PC architectures, a better solution was required, since other architectures do not use VGA-compatible graphics adapters, and may not support text modes at all. The framebuffer console was implemented to provide a standard console across all platforms, and so presents the same VGA-style interface regardless of the underlying graphics hardware. As such, the Linux console is not a terminal emulator, but a terminal in its own right. It uses the terminal type , and is largely compatible with VT100.

## Keyboard shortcuts
{| class="wikitable"
! Keyboard Shortcut
! Description
|-
|
| Reboots the system (specified by the symlink )
|-
| , , , ...
| Switch to n-th virtual console (not to be confused with  used in Xorg and Wayland)
|-
|
| Switch to previous virtual console
|-
|
| Switch to next virtual console
|-
|
| When Scroll Lock is activated, input/output is locked. Alternatively, use  to lock,  to unlock.
|-
|
| Kills current task
|-
|
| Inserts an EOF
|-
|
| Pauses current Task
|}

See also .

## Fonts
The Linux console uses UTF-8 encoding by default, but because the standard VGA-compatible framebuffer is used, a console font is limited to either a standard 256, or 512 glyphs. If the font has more than 256 glyphs, the number of colours is reduced from 16 to 8. In order to assign correct symbol to be displayed to the given Unicode value, a special translation map, often called unimap, is needed. Nowadays, most of the console fonts have the unimap built-in; historically, it had to be loaded separately.

By default, the virtual console uses the kernel built-in font with a CP437 character setbut this can be easily changed. The kernel offers about 15 built in fonts to choose from, from which the officially supported kernels provide two: VGA 8x16 font () and Terminus 16x32 font (). The kernel chooses the one to use based on its evaluation of the screen resolution. Another builtin font can be forced upon by kernel parameters boot parameter setting such as .

The  package provides tools to override the kernel decision for virtual console font and font mapping. Available fonts are provided in the  directory; those ending with .psfu or .psfu.gz have a Unicode translation map built-in.

Keymaps, the connection between the key pressed and the character used by the computer, are found in the subdirectories of ; see /Keyboard configuration for details.

## Preview and temporary changes
 $ showconsolefont

shows a table of glyphs or letters of a font.

 temporarily changes the font if passed a font name (in ) such as

 $ setfont lat2-16 --consolemap 8859-2

Font names are case-sensitive. With no parameter,  returns the console to the default font.

So to have a small 8x8 font, with that font installed like seen below, use e.g.:

 $ setfont --font-height=8 /usr/share/kbd/consolefonts/drdos8x8.psfu.gz

For larger font size, the Terminus font () offers various sizes, including the particularly large .

You can further enlarge a font using the  flag. Below command turns a 32x32 font into a 64x64 font:

 $ setfont --double ter-132n

## Persistent configuration
The  variable in  is used to set the font at boot, persistently for all consoles. See  for details.

For displaying characters such as Č, ž, đ, š or Ł, ę, ą, ś using the font :

It means that second part of ISO/IEC 8859 characters are used with size 16. You can change font size using other values (e.g. ). For the regions determined by 8859 specification, look at the Wikipedia:ISO/IEC 8859#The parts of ISO/IEC 8859.

Since [https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/blob/v33/mkinitcpio.conf#L52 mkinitcpio v33, the font specified in  gets automatically loaded during early userspace by default via the  hook, which adds the font to the initramfs. See Mkinitcpio#HOOKS for more information.

You may also need to restart  after changing .

If the fonts appear to not change on boot, or change only temporarily, it is most likely that they got reset when graphics driver was initialized and console was switched to framebuffer. By default, all in-tree kernel drivers are loaded early, NVIDIA users should see NVIDIA#Early loading to load their graphics driver before  is applied.

## Cursor appearance
This subject is poorly documented. You should read the following articles first:

* Software cursor for VGA
* Cursor Appearance in the Linux Console
* Disable Cursor Blinking on Linux Console

{| class="wikitable"
|+ Cursor types
|-
! !! Hardware !! Software
|-
! Shape
||
:(0) default
::applies (2) underscore
:(1) invisible
:(2) underscore
:(3) lower third
:(4) lower half
:(5) two thirds
:(6) full block
||
:(16) full block
::the shape can't be changed, but the cursor can effectively be invisible in case of background and foreground colors are equal
|-
! Blinking
||
:blinks
||
:driver-dependent
::the highest bit of background color can be interpreted as "bright" or as "blinking"
|-
! Color
||
:the same as console text color (usually white/gray)
::can't be set independently
||
:can be set by a user
|}

The console cursor can be adjusted with Device Attributes (DA) control function. The sequence of parameters must be preceded by a single question mark (despite  says the opposite).

Here is an example for full block non-blinking green cursor with black symbols under it:

 $ printf "\x1b\x5b?16;$((8+4+2+1));$((32+0+8+4+2+1))\x63"

The same can be expressed with the octal and characters instead of hex codes:

 $ printf '\033The same can be applied as permanent configuration with kernel parameter:

 vt.cur_default=0x2f0f10

## Cursor size
The first parameter, despite its name cursor size, with decimal number 16 (the rightmost two hex digits of the kernel parameter are 10) means use software cursor. If you want to use hardware cursor and change its shape—apply corresponding number (from 0 to 6, see the table Cursor types above).

## Toggle mask
The second parameter, called toggle mask, flips corresponding bits of the color.

{| class="wikitable" style="text-align: center;"
|+ Character attribute bits
|-
! !! colspan=4 | Background
(cursor block)
!! colspan=4 | Foreground
(symbol under the cursor)
|-
!
|| Bright (highlight)
or blinking
|| Red
|| Green
|| Blue
| Bright (highlight)
or blinking
|| Red
|| Green
|| Blue
|-
! Decimals
|| 128 || 64 || 32 || 16 || 8 || 4 || 2 || 1
|-
! Hex
|| 80 || 40 || 20 || 10 || 8 || 4 || 2 || 1
|}

In our case the second parameter is 15 (the middle hex digits of the kernel parameter are 0f), so all four foreground (symbol) bits will be flipped. The most important rule is: toggling (the second parameter) is applied after the setting (the third parameter).

## Set mask
The third parameter is called set mask. It sets corresponding character attribute bits. We use 47 (the leftmost hex digits of the kernel parameter are 2f) in our example, which means two things:

* (32) use pure green color for cursor block
* (8+4+2+1) set all four foreground (symbol color) bits. These bits will be toggled by the second parameter, so the color of the symbol under the cursor will be black ().

## HiDPI
See HiDPI#Linux console (tty).

## Audible tones
See PC speaker#beep.

## Automatic suspend
You can configure the Linux console to blank the screen (and, on many devices, turn off the display power) when unused for some time, similar to the behavior of most desktop environments.

## consoleblank
One way to do so is by the  kernel parameter, where  is the number of seconds before the console should go to sleep. One can examine the current value by . One thing this method differ from the #setterm method below is that it will also blank a login screen if no one logged in at it for more than the value of  seconds.

## setterm
Alternatively, from within a shell prompt, use  with  and/or  flags. For example:

 $ setterm --blank 5 --powerdown 1

 and  values in this command denote time in minutes. To make the settings persist, add the below lines to your shell configuration file (,  etc.), wrapping the command in a condition block as below ensures that it runs only when using the Linux console:

This method does not require root privileges. On the other hand, it requires logging in before it begins counting idle times.
