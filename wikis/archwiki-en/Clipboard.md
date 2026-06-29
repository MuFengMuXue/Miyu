# Clipboard

According to Wikipedia:
:The clipboard is a facility used for short-term data storage and/or data transfer between documents or applications, via copy and paste operations.

## History
In X10 (1985), cut buffers were introduced. These were limited buffers that stored arbitrary text and were used by most applications. However, they were inefficient and implementation of them varied, so selections were introduced. Cut buffers are long deprecated, and although some applications (such as xterm) may have legacy support for them, it is both not likely and not recommended that they be used.

## Selections
Freedesktop.org describes the two main selections as follows:;PRIMARY: Used for the currently selected text, even if it is not explicitly copied, and for middle-mouse-click pasting. In some cases, pasting is also possible with a keyboard shortcut.
;CLIPBOARD: Used for explicit copy/paste commands involving keyboard shortcuts or menu items. Hence, it behaves like the single-clipboard system on Windows. Unlike PRIMARY, it can also handle [https://stackoverflow.com/questions/3571179/how-does-x11-clipboard-handle-multiple-data-formats multiple data formats.

The majority of programs for Xorg, including Qt and GTK applications, follow this behavior. While ICCCM also defines a SECONDARY selection, it does not have a consensually agreed upon purpose. Despite the naming, all three selections are basically "clipboards". Rather than the old "cut buffers" system where arbitrary applications could modify data stored in the cut buffers, only one application may control or "own" a selection at one time. This prevents inconsistencies in the operation of the selections.

See the Keyboard shortcuts page which lists the default shortcuts in many programs.

It is also important to realize that according to the selection protocols, nothing is copied until it is pasted. For example, if you select some word in a terminal window, close the terminal and then want to paste it somewhere else, it will not work because the terminal is gone and the text has not been copied anywhere. If you want the word to be preserved after closing terminal window, consider installing a clipboard manager.

## Disabling middle-click paste
The following disables the middle-click pasting behavior by automatically clearing PRIMARY, without disabling the middle-click button or altering its other functionalities (like opening in a new tab or scrolling).

## Globally
## Using sxhkd
Using sxhkd, add the following to the configuration file:

 ~button2
     ;echo -n | xclip -in

The command makes use of . See sxhkd#Usage for configuring sxhkd to autostart.

## Using xsel
Run the script

 #!/bin/sh
 while true; do
     xsel --follow --input --nodetach  Options > LibreOffice > View > Mouse

## Tools
This section lists command-line tools for X11 to manipulate the clipboards.

*
*
*

## Wayland
The clipboard content in Wayland is maintained by the program that copied it. If the program closes, the copied content becomes unavailable.

To persist clipboard content, use a "clipboard manager", it maintains its own copy of the clipboard content.

For example to use  with Sway and , add the following to your configuration file:

Further command-line tools :
*
*

## Managers
This section lists clipboard managers which provide additional features such as clipboard history or synchronization.

*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
