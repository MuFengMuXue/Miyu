# Rxvt-unicode

rxvt-unicode (urxvt) is a terminal emulator forked from rxvt, customizable with source-code patches, #X resources and #Perl extensions.

## Installation
Install one of the following:

* ,
*  — improved font rendering, enhanced glyph support, applied True color support,

or search Arch User Repository for opinionated builds with different patches and configuration options applied.

{| class="wikitable"
|+ Patches
|-
! File name !! Description
|-
|
||
:multiple-char sequence for 7-bit queries — is needed for correct work of color Operating system command (OSC) sequences; merged upstream
|-
|
||
:True Color support
|-
|
||
:256 ~/.Xresources colors
|-
|
||
:fixed opacity (pixbuf-related)
|-
|
||
:Control-L keeps all lines from the screen in the scrollback buffer (VTE-like behavior)
|-
|
||
:enhancing glyph support, required by
|-
|
||
:decreasing space between symbols, incompatible with (replaced by)
|-
|
||
:font rendering improvements
|-
|
||
:vertical spacing improvement, incompatible with (replaced by)
|-
|
||
:solves the #Wrong shell prompt placement after upgrading to 9.31 problem
|-
|
||
:add vi-style (hjkl) keys to matcher extension to mimic deprecated ulr-select behavior
|-
|
||
:no increment resizing—is needed for better Openbox user experience
|-
| osc-110-112-reset.patch
||
: xterm OSC 110—reset VT100 text foreground color, 111—reset VT100 text background color, 112—reset text cursor color; see also #Non-permanent
|-
|
||
:fixing popup Perl extension hanging
|-
|
||
:Digital Equipment Corporation (DEC) Sixel support for expressing character bitmap image via DEC Device Control String (DCS)  Sixel  escape sequence—
|-
|
||
:the same as
|-
|
||
:scrolling in the secondary screen with the mouse wheel
|-
|
||
:commenting out line 397 of  — one of the approaches to the #Wrong shell prompt placement after upgrading to 9.31 problem
|}

{| class="wikitable"
|+ 3rd party Perl extensions
|-
! File name,
link
! Package
! Description
|-
|keyboard-select
|
||
:use keyboard shortcuts to select and copy text
|-
| resize-font
|
||
:use keyboard shortcuts to adjust the font size; fractional intervals—such as —also supported
|}

## Configuration
## X resources
Rxvt-unicode is controlled by command-line arguments or X resources. Command-line arguments override, and take precedence over resource settings.

The first component of a resource is either the class——or an application (instance) name.
Application name can be specified with  command-line option and is set to —a binary —by default. For a given instance, resources defined with an application name override, and take precedence over defined with the class name ones.

See  and  for available settings, X resources and values. Also  prints all available resources to the standard error. Each resource can be used as a long command-line option.

Use —provided by the  package—to apply the configuration: .

## Fonts
Rxvt-unicode does not utilize fontconfig library for font substitution when a font or individual character is not present. I.e. you must provide all font names in the corresponding resources—set the fontsets—for all glyphs you are interested in.

Rxvt-unicode supports both X FreeType (Xft) and X Logical Font Description (XLFD);  supports XLFD only.

## Permanent
## Non-permanent
You can change the fonts of the current instance with Operating System Command (OSC) sequences. Use numeric (Ps) parameters 710–713 followed by corresponding text (Pt) parameter, such as:

 $ printf '\x1b\x5d710;%s\x1b\x5c' "xft:Terminus:pixelsize=22"
 $ printf      '\e]711;%s\a'       "xft:Terminus:pixelsize=22:bold"

See also:

*
*
:

To change font size of the current instance with keyboard shortcuts use  Perl extension.

## Spacing
You may need to tweak the horizontal distance between characters with  and/or the vertical distance between rows with . These needs depend on:
* using rendering improvement patches, like enable-wide-glyphs.patch, improve-font-rendering.patch, font-width-fix.patch or line-spacing-fix.patch,
* using languages with glyphs that are too different from English letters, like Arabian, Chinese, Hebrew, Japanese or Korean,
* your font and its size.

## Scrollback buffer
## Behavior on receiving new output
By default, when shell output appears, the scrollback view will automatically jump to the bottom of the buffer to display new output.

If you want to see previous output (e.g., compiler messages) while pseudo-TTY is still receiving new lines, and jump to the bottom of the scrollback buffer on key press, use the following options:

 URxvt.scrollTtyOutput:   False
 URxvt.scrollWithBuffer:  True
 URxvt.scrollTtyKeypress: True

## Secondary screen
When you scroll a pager in a secondary screen (e.g. using  without the  option), it may be a good idea to disable secondary screen scroll to be able to scroll in the pager itself, instead of the terminal's buffer.

This is default and unchangeable behavior in Konsole and VTE-based terminal emulators. To achieve the same behavior in urxvt, use the following:

 URxvt.secondaryScroll: False

The above configuration works as expected, except when scrolling with a mouse wheel. When you scroll a pager in the secondary screen with the mouse wheel, and there has been something in the scrollback buffer — the scrollback buffer will be scrolled by the mouse wheel, instead of the pager itself.

To solve this issue, it is necessary to introduce a new option into urxvt. Use packages like  or  , or apply . After installing, set the following:

 URxvt.secondaryWheel: True

## Clearance
Reset to Initial State (RIS)  control function empties the screen and the scrollback buffer. You can bind it to your desired keys like so:

 URxvt.keysym.Meta-Control-l: command:\033c

## Keeping the screen content on screen clearance
In urxvt pressing Control-L empties the screen, and the screen content is thrown away — you cannot see it in the scrollback buffer later. This behavior might seems controversial for users with Konsole or VTE-based terminal emulators experience, where Control-L keeps the screen content in the scrollback buffer.

To achieve such VTE-like behavior in urxvt you can use appropriate package like  or , or apply  in your preferred build.

## Scrollbar
Scrollbar look and feel is controlled by a dozen of resources. Look at the manual around  and  resources, and see  section.

You can also change visibility of scrollbar on the fly for the current instance with DEC Private Modes  (). For example, you can bind scrollbar visibility toggling to a keyboard shortcut:

 URxvt.keysym.Meta-Control-s: command:\033==== Saving to a file ====

Ctrl-Print or Shift-Print saves the scrollback buffer content to a file with a setting like so:

 URxvt.print-pipe: cat > ~/Downloads/URxvt_$(date '+%Y-%m-%d_%H:%M:%S').txt

* Print is usually the Print Screen key.
* Print alone saves the screen without the scrollback buffer.

## Clipboard
Rxvt-unicode clipboard behavior might seem controversy for people without xterm background. See  for details.

You can use  with key bindings to setup copying to and pasting from CLIPBOARD:
 URxvt.keysym.Control-Insert:    eval:selection_to_clipboard
 URxvt.keysym.Shift-Insert:      eval:paste_clipboard

 can be used to synchronize CLIPBOARD with PRIMARY selection.

The  extension displays a confirmation dialog when a paste containing control characters (like newlines) is detected. It is part of the  set and is loaded automatically, see  and #Disabling Perl extensions for more info.

## Perl extensions
We can enable Perl extensions by including the following line:

 URxvt.perl-ext-common: extension_name_1,extension_name_2,...

See also:
*  — the resource description
*  — list of available (prepackaged) extensions, do not confuse with  extension set
*  — manual pages for specific prepackaged extensions
*  — embedded Perl interpreter manual

## Clickable URLs
You can make URLs in the terminal clickable using the matcher extension. For example, to open links in the default web browser with the left mouse button, add the following to :

 URxvt.perl-ext-common: default,matcher
 URxvt.url-launcher: /usr/bin/xdg-open
 URxvt.matcher.button: 1

Since rxvt-unicode 9.14, it is also possible to use matcher to open and list recent (currently limited to 10) URLs via keyboard:

 URxvt.keysym.C-Delete: perl:matcher:last
 URxvt.keysym.M-Delete: perl:matcher:list

Matching links can be colored with a chosen foreground or background color (see ), for example blue:

 URxvt.matcher.rend.0: Uline Bold fg4

Alternatively, use  for a #RRGGBB color. This will however color all underlined text, instead of only link matches:

 URxvt.colorUL: #4682B4

## Simple tabs
To add tabs to urxvt, add the following to your :

 URxvt.perl-ext-common: ...,tabbed,...

To control tabs use:

{| class="wikitable"
! Key !! Description
|-
|  || New tab
|-
|  || Go to left tab
|-
|  || Go to right tab
|-
|  || Move tab to the left
|-
|  || Move tab to the right
|-
|  || Close tab
|}

You can change the colors of tabs with the following:

 URxvt.tabbed.tabbar-fg: 2
 URxvt.tabbed.tabbar-bg: 0
 URxvt.tabbed.tab-fg: 3
 URxvt.tabbed.tab-bg: 0

In order to make the tabbar transparent set its value to -1

 URxvt.tabbed.tabbar-bg: -1

If you need to rename the tab, you would probably want to install  instead.

## Fullscreen
You can install the AUR package , and then set a key binding to put urxvt fullscreen.

 URxvt.perl-ext-common:  ...,fullscreen,...
 URxvt.keysym.F11:       perl:fullscreen:switch

## Disabling Perl extensions
If you do not use the Perl extension features, you can improve the security and speed by disabling Perl extensions completely:
 URxvt.perl-ext-common:

To selectively disable an extension, you need to prepend a hyphen before the extension name:
 Urxvt.perl-ext-common: default,-extension

Alternatively, you can explicitly list every extension you need, effectively disabling all others:
 URxvt.perl-ext-common: eval,searchable-scrollback,resize-font

## Troubleshooting
## Wrong shell prompt placement after upgrading to 9.31
Some window managers may have the problem that your prompt appears somewhere in the middle of the window. It may happens on start and/or on window resize. The root cause is update in lines-rewrap algorithm.

To solve the problem you should apply [https://aur.archlinux.org/cgit/aur.git/tree/lines-rewrap.patch?h=rxvt-unicode-truecolor-wide-glyphs lines-rewrap.patch.

You can also play with geometry, but result is environment– and workflow–dependent, there is no "one size fits all" solution:
* Set the real geometry: .
* Set unrealistic geometry: .
* Set rows to ''-1'': .
::This may lead to inability to use some command line options, for example  sometimes opens the terminal for a fraction of second with shell prompt placed in the middle of the first row instead of running Midnight Commander.

Ultimate solution is reverting changes in the source code:
* Comment out one line in  (also see ).
* Fully revert algorithm changes: .

## Remote hosts
If you are logging into a remote host, you may encounter problems when running text-mode programs under rxvt-unicode. This can be fixed by installing  on the remote host or by copying  from your local machine to your host at ; same for .

Some remote systems do not change title automatically unless you specify . To fix the issue add this line to  on the remote machine:

 PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}:${PWD}\007"'

Another fix you can try is to put following in your :

 URxvt.termName: rxvt

This is useful when connecting into remote hosts without admin privileges to install terminfo definition for rxvt-unicode.

## Using rxvt-unicode as gmrun terminal
Unlike some other terminals, urxvt expects the arguments to  to be given separately, rather than grouped together with quotes. This causes trouble with gmrun, which assumes the opposite behavior. This can be worked around by putting an  in front of gmruns  variable in :

 Terminal = eval urxvt
 TermExec = ${Terminal} -e

gmrun uses  to execute commands, so the  is understood here. The  has the side-effect of "breaking up" the argument to  in the same way that  does in Bash, making the command intelligible to urxvt.

## Key combinations do not work
See Get Alt key to work in terminal.

## Very long lines cause slowdown
The  plugin may be the culprit here. It must match a regex against a line every time the line updates, and if you have a large  value this can exacerbate the problem by allowing a very large maximum line length.

There are some simple workarounds:

* Reduce
* Disable the  plugin

If neither of those are palatable options, you can compromise by disabling URL matching past a certain cutoff point:

# Copy  to  (creating the directory if necessary)
# Edit , and find the  line in the  sub. It should be line 270.
# After that line, insert the line . This disables URL matching on any line that starts more than 100 rows behind the top of the terminal.

## No bold text in Midnight Commander
If started under rxvt-unicode with the default  setting, text that is usually bold in many other terminals will not appear so. The root of the issue is because xterm couples bright text color with the bold attribute—thus, bright colors will always appear as bold in xterm.

The solution is to configure Midnight Commander to explicitly use bold colors as desired, e.g. by editing the default skin as follows:

 $ mkdir ~/.local/share/mc/skins
 $ cp /usr/share/mc/skins/default.ini ~/.local/share/mc/skins/
 $ sed -i -E 's/^(.* = (gray|brightred|brightgreen|yellow|brightblue|brightmagenta|brightcyan|white);.*)$/\0;bold/' ~/.local/share/mc/skins/default.ini

The above will create a copy of the default skin, but with all bright colors having an explicit bold attribute added.
