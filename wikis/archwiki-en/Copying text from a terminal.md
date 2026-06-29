# Copying text from a terminal

Most mature terminal emulators permit users to copy or save their contents.

## General approach
In graphical terminal emulators, contents are typically selectable by mouse, and can then be copied using the context menu, Edit menu or a key combination such as .

## Terminals without CLIPBOARD selection
## Xorg
Some emulators do not support the CLIPBOARD selection natively, and copy data to the PRIMARY selection. For them  may be used:

 $ xclip -o | xclip -selection clipboard -i

The above command reads data from the PRIMARY selection and writes it to CLIPBOARD selection.

Other clipboard managers such as  provide automatic synchronization between selection buffers.

## Wayland
Utilities like  and  can copy data to the Wayland clipboard:

 $ command 2>&1 | wl-copy --type 'text/plain;charset=utf-8'

## Intercepting commands output
Use tee to intercept the output of a command.

 $ command 2>&1 | tee output-file

After the  is executed,  will contain its output, while having displayed the output at the same time.

## Accessing Linux terminal backlog
The backlog of a native terminal named  may be accessed via .
Hence, if one is working in , the following snippet will let store the backlog in a file :

 # cat /dev/vcs1 > output-file

## Comparison of common emulators
Unless the "Key combination" column states otherwise, the key combination is .

{| class="wikitable sortable"
! rowspan="2" | Emulator !! rowspan="2" | Select to PRIMARY
! colspan="5" |CLIPBOARD
|-
! Key combination !! Context menu !! Window menu !! Select
|-
| Alacritty ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
| foot ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
| Guake ||  ||  ||  ||  ||
|-
| Konsole ||  ||  ||  ||  ||
|-
|  ||  ||   ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
| PuTTY ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
| rxvt-unicode ||  ||   ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
| st ||  ||  ||  ||  ||
|-
| Terminator ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
| Termite ||  ||  ||  ||  ||
|-
| Tilda ||  ||  ||  ||  ||
|-
|  ||  ||  ||  ||  ||
|-
| xterm ||  || https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=588785 ||  ||  ||
|-
| Yakuake ||  ||  ||  ||  ||
|}

## Special cases
## putty
The xclip approach works for putty: one just has to remember that the xclip invocation should be done on the local computer (in another terminal), not on the remote machine to which putty is connected.

## urxvt
Selecting text to CLIPBOARD requires the  perl extension. See rxvt-unicode#Clipboard for details.

## xterm
Access to the CLIPBOARD selection in xterm requires additional steps.

## mlterm
In addition to , you can use  if you do not want to kill processes accidentally.
