# Xterm

xterm is the standard terminal emulator for the X Window System. It is highly configurable and has many useful and some unusual features.

## Installation
Install the  package.

## Configuration
## Resource file settings
There are several options you can set in your X resources files that may make this terminal emulator much nicer to use. See  for a complete list.

## TERM environmental variable
Allow xterm to report the  variable correctly. Two usable terminfo names are xterm and xterm-256color. To set the name, use the resource

 XTerm.termName: xterm-256color

You can check the result within xterm using either of these commands:

 $ echo $TERM
 $ tset -q

## UTF-8
Ensure that your locale is set up for UTF-8. If you do not use UTF-8, you may need to force xterm to more strictly follow your locale by setting

 XTerm.vt100.locale: true

To force UTF-8, set

 XTerm.vt100.locale: false
 XTerm.vt100.utf8: true

This is often necessary because XTerm does not support all UTF-8 locales, including .

## Make 'Alt' key behave as on other terminal emulators
The default  key behavior in xterm is a modifier to send eight bit input characters e.g. to insert  by pressing . To make  instead send a  (escape) key (as in gnome-terminal and konsole), set

 XTerm.vt100.metaSendsEscape: true

## Fix the backspace key
On Arch Linux, xterm sends  key when backspace is pressed. This breaks the  key combination on Emacs.
The workaround is to send  when backspace is pressed by setting the resources

 XTerm.vt100.backarrowKey: false
 XTerm.ttyModes: erase ^?

## Key binding
xterm defines a whole suite of "actions" for manipulating the terminal e.g. , , , etc. These actions can be mapped to mouse/key combinations using the  resource. For example, you can map  and  to maximize/restore the window:

 XTerm.vt100.translations: #override \n\
     Ctrl M: maximize() \n\
     Ctrl R: restore()

 indicates that these bindings should override any existing ones (you almost always want this for custom key bindings). Each binding must be separated by the escape sequence . If you want to insert a literal newline, it also needs to be escaped (hence ). See  for the full list of actions and many examples.

## Scrolling
As new lines are written to the bottom of the xterm window, older lines disappear from the top.  To scroll up and down through the off-screen lines one can use the mouse wheel, the key combinations  and , or the scrollbar.

By default, 1024 lines are saved.  You can change the number of saved lines with the  resource:

 XTerm.vt100.saveLines: 4096

Other X resources that affect scrolling are , , and  (all under , see ). To scroll inside an alternate screen, set  to .

## Scrollbar
The scrollbar is not shown by default. It can be enabled and its appearance tweaked through resource settings (note the differing capitalization of "scrollbar"!)

 XTerm.vt100.scrollBar: true
 XTerm.vt100.scrollbar.width: 8

See  for other scrollbar resources.

The scrollbar operates differently from what you may be accustomed to using.

*To scroll down:
** Click on the scrollbar with the left mouse button, or
** Click on the scrollbar below the thumb with the middle mouse button.
*To scroll up:
** Click on the scrollbar with the right mouse button, or
** Click on the scrollbar above the thumb with the middle mouse button.
*To position text, moving in either direction:
** Grab the thumb and use "click-and-drag" with the middle mouse button.

## Menus
 is compiled with the toolbar, or menubar, disabled. The menus are still available as popups when you press  within the xterm window. The actions invoked by the menu items can often be accomplished using command line options or by setting resource values.

Some of the menu options are discussed below.

## Main Options menu
Opens with :

* attempts to ensure only the xterm window, and no other application, receives your keystrokes. The display changes to reverse video when it is invoked. If the display is not in reverse video, the Secure Keyboard mode is not in effect. Please read  for this option's limitations.
* allows other processes to send keypress and mouse events to the xterm window. Because of the security risk, do not enable this unless you are very sure you know what you are doing.
* – The log file will be named . This file will contain all the printed output and all cursor movements. Logging may be a security risk.
*The six  menu items are not often useful, except when your keyboard fails. ,  and  will close the xterm window.  should be avoided, as it does not allow any cleanup code to run.
*The  menu item will also close the xterm window – it is the same as sending a  signal. Most users will use the keyboard combination  or will type  to close an xterm instance.

## VT Options menu
Opens with :

* – Normally, selected text is stored in PRIMARY, to be pasted with  or by using the middle mouse button.  By toggling this option to on selected text will use CLIPBOARD, allowing you to paste the text selected in an xterm window into a GUI application using . The corresponding resource is .
* – When you use a terminal application such as vim, or less, the alternate screen is opened. The main VT window, now hidden, remains in memory. You can view this main window, but not issue any commands in it, by toggling this menu option. You are able to select and copy text from this main window.
* and  – The Tektronix 4014 was a graphics terminal from the 1970s used for CAD and plotting applications. The command line program , from , and the application  can be made to use xterm's Tek emulation; most people will prefer more modern display options for charting data. See the #Tek 4014 demonstration, below.

## VT Fonts menu
Opens with :

*When using XLFD fonts, the first seven menu items will change the font face and the font size used in the current xterm window. If you are using an Xft font, only the font size will change, the font face will not change with the different selections.
*, when using XLFD font names, allows you to switch to the font name stored in the PRIMARY selection (or CLIPBOARD).

## Tek Options menu
Opens from the Tek Window with .

The first section's options allow you to change the Tek window font size. The second set of options are used to move the focus between the Tek emulation window and the main, or VT, window and to close or hide the Tek window.

## Copy and paste
First, highlighting text using the mouse in an xterm (or alternatively another application) will select the text to copy, then clicking the mouse middle-button will paste that highlighted text. The key combination  will paste highlighted text (but not in all applications).

See Clipboard#Selections for the terminology and general information.

## PRIMARY or CLIPBOARD
By default, xterm copies highlighted text into a buffer called the PRIMARY selection where the text is immediately replaced by a new PRIMARY selection as soon as another piece of text is highlighted. The PRIMARY selection can be pasted in xterm by pressing the middle-mouse button or .

The CLIPBOARD selection is used for explicit copy/paste commands, e.g. via the shortcuts , , or .

xterm allows users to switch between using PRIMARY or CLIPBOARD using  on the #VT Options menu, or with the  resource.

## PRIMARY and CLIPBOARD
With the above setting you can select if you want to use PRIMARY or CLIPBOARD, but you can also hack it to add the selection to both. Just override the #Key binding for releasing the left mouse button:

 : select-end(PRIMARY, CLIPBOARD, CUT_BUFFER0)

You can add key bindings similar to other terminals' copy/paste behavior (such as gnome terminal):

 Ctrl Shift C: copy-selection(CLIPBOARD) \n\
 Ctrl Shift V: insert-selection(CLIPBOARD)

## Selecting text
The new user usually discovers that text may be selected using a "click-and-drag" with the left mouse button.  Double-clicking will select a word, where a word is defined as consecutive alphabetic characters plus the underscore, or the Basic Regular Expression (BRE) .  Triple-clicking selects a line, with a "tab" character usually copied as multiple "space" characters.

Another way of selecting text, especially useful when copying more than one full screen, is:

#Left-click at the start of the intended selection.
#Scroll to where the end of the selection is visible.
#Right-click at the end of the selection.
:You do not have to be precise immediately with the right-click – any highlighted selection may be extended or shortened by using a right-click.

You can clear any selected text by left-clicking once, anywhere within the xterm window.

When a character-based application runs inside xterm, it is allowed to receive mouse events. This may be a problem if the program can not communicate with the X11 clipboard. In order to pass these events to the underlying xterm, they must be accompanied by the  key. For example, in  (not ), one can mouse-click on URLs and menu items, but not select or paste with a middle button. To do copy-paste, press the  key and then perform mouse clicks (the key needs to be pressed only during the click, so there is no need to hold it when dragging mouse to select, for instance, a text block).

## Colors
xterm defaults to black text, the foreground color, on a white background.  The foreground and background colors can be reversed by setting the resource

 XTerm.vt100.reverseVideo: true

Alternatively, you can directly change the foreground and background colors (as well as the first sixteen terminal colors) using resources:

 XTerm.vt100.foreground: white
 XTerm.vt100.background: black
 XTerm.vt100.color0: rgb:28/28/28
 ! ...
 XTerm.vt100.color15: rgb:e4/e4/e4

Many suggestions for color schemes can be viewed in the forum thread, Terminal Colour Scheme Screenshots.

## Fonts
## Default fonts
xterm's default font is the bitmap font named by the X Logical Font Description alias , often resolving to

 -misc-fixed-medium-r-semicondensed--13-120-75-75-c-60-iso8859-?

This font, also aliased to the name , has remakably wide coverage for unicode glyphs.  The default "TrueType" font is the 14‑point font matched by the name .  The FreeType font that will be used can be found with this command:

 $ fc-match mono

Fonts can be specified in your resources, depending on whether the font is TrueType or not:

 XTerm.vt100.faceName: Liberation Mono:size=10:antialias=false
 XTerm.vt100.font: 7x13

To test, you can also set the font on the command line:  for ,  for . If you set both kinds of fonts, you can alternate between the two by toggling  from the #VT Fonts menu. You can also choose the default with the following resource

 ! start with TrueType fonts disabled
 XTerm.vt100.renderFont: false

## Bold and underlined fonts
Italic fonts are shown as underlined characters when using XLFD names in xterm. TrueType fonts should use an oblique typeface.

If you do not specify a bold font at the command line, , or through the  resource, xterm will attempt to find a bold font matching the normal font.  If a matching font is not found, the bold font will be created by "overstriking" the normal font.

## CJK Fonts
Many fonts do not contain glyphs for the double width Chinese, Japanese and Korean languages.  Other terminal emulators such as urxvt may be better suited if you frequently work with these languages.

Using bitmapped XLFD fonts with CJK has many pitfalls in xterm.  It is much easier to use TrueType fonts for CJK display, using the  resource.  This example uses DejaVu Sans Mono as the normal font and WenQuanYi WenQuanYi Bitmap Song as the double width font:

 XTerm.vt100.faceName: DejaVu Sans Mono:style=Book:antialias=false
 XTerm.vt100.faceNameDoublesize: WenQuanYi WenQuanYi Bitmap Song
 XTerm.vt100.faceSize: 8

## Tips and tricks
## Automatic transparency
Install a transset package, such as  or , and a composite manager such as Xcompmgr.  Then add the following line to your shell startup file:

 [ -n "$XTERM_VERSION" ] && transset-df --id "$WINDOWID" >/dev/null

Now, each time you launch a shell in an xterm and a composite manager is running, the xterm window will be transparent.
The test in front of  keeps it from executing if  is not defined. Note that your terminal will not be transparent if you launch a program other than a shell this way. It is probably possible to work around this if you want the functionality.

Also see Per-application transparency.

## Enable bell urgency
To make the bell character notify the window manager of urgency, set:

 XTerm.vt100.bellIsUrgent: true

## Font tips
## Use color in place of bold and italics
When using small font sizes, bold or italic characters may be difficult to read.  One solution is to turn off bolding and underlining or italics and use color instead.  This example does just that:

 ! disable bold font faces, instead make text light blue.
 XTerm.vt100.colorBDMode: true
 XTerm.vt100.colorBD: rgb:82/a4/d3
 ! disable underlined text, instead make it white.
 XTerm.vt100.colorULMode: true
 XTerm.vt100.colorUL: rgb:e4/e4/e4
 ! similarly use colorIT for italics

See #Colors for formatting information.

## Adjust line spacing
Lines of text can sometimes be too close together, or they may appear to be too widely spaced.  For one example, using DejaVu Sans Mono, the low underscore glyph may butt against CJK glyphs or the cursor block in the line below.  Line spacing, called leading by typographers, can be adjusted with the following resource, for example to widen the spacing:

 XTerm.vt100.scaleHeight: 1.01

Valid values for range from  to , with  being the default.

## Tek 4014 demonstration
If you have  installed, you can use xterm's Tektronix 4014 emulation to view some of the plotutils package's test files.  Open the Tek window from the #VT Options menu menu item  or start a new xterm instance using this command:

 $ xterm -t -tn tek4014

Your PS1 prompt will not render correctly, if it appears at all.  In the new window, enter the command,

 cat /usr/share/tek2plot/dmerc.tek

A world map will appear in the Tek window.  You can also view other  files from that same directory.  To close the Tek window, one can use the xterm menus.

## Protect against X11 input snooping
It can be inconvenient to activate Secure Keyboard mode from the #Main Options menu. You can instead invoke the  action with a #Key binding:

 Ctrl Alt S: secure()

## Troubleshooting
## Flickering on scroll
Rebuild xterm using ABS and include the  flag:

 ./configure --prefix=/usr \
      ...
      --with-utempter \
      --enable-double-buffer

See Xterm modifications for details.

## Configuration is not applied
Some applications, such as i3, call  wrapper instead of . This can be resolved by adding the same configurations for , such as:

 UXTerm.vt100.reverseVideo: true

If you prefer to not having duplicate entries in the configuration file, wildcard matching can be used:

 *.vt100.reverseVideo: true

## Font size menu does not change font size
If you have issues with changing the font size, install the  package.
