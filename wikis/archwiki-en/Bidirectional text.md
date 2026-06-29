# Bidirectional text

From Wikipedia:Bidirectional text, is text that contains two text directionalities, right-to-left (RTL) and left-to-right (LTR).

## Concepts
; Text direction: while editing, setting text direction changes the interaction of the editor with the text. It affects text navigation, selection, and insertion.
; Text alignment: a stylized form of presenting text. E.g: English text can be aligned to the right despite being LTR language, but this does not change the direction of the text which is LTR.
; Fake Bidi: a fake locale displaying completely reversed English sentences to mimic a RTL context. This helps who are not familiar with RTL language to visualize RTL issues. For example:
; Poor man's bidi mode: automatic visual text order right-to-left input in normal terminal.
; Logical navigation: words are traversed as they are read.
; Visual navigation: words are traversed as they are displayed. This GIF demonstrates the difference between the two.

Logical navigation is the correct way of navigation that programs should implement to fully support Bidi.
; Unicode support: In Unicode-supported text editors, text direction can be controlled by inserting special formatting characters in front of it: Wikipedia:RLM (U+200F), Wikipedia:LRM (U+200E), which is a workaround for text editors not supporting switching text direction.

; Bidirectional Algorithm: is the set of rules applied to display text in the correct order.

## Support
In order for a program to fully support Bidi text, it must have:

; Text shaping (RTL shaping): correctly apply letter rendering and ligatures. See Wikipedia:HarfBuzz and Wikipedia:Complex text layout.
; Unicode Bidirectional Algorithm (UBA): determine the directionality of text segments and apply the appropriate rendering rules.
; Editing and input (Nav): the ability to force text direction and correct behavior of cursor movement, selection, deletion, and insertion (logical navigation).

Some implementations of UBA and letter-shaping:
*  is an open source implementations of Bidi Algorithm.
*  is a python library for related functions.
* SheenBidi: Improved Unicode Implementation in C.

## Browsers
{| class="wikitable sortable"
! App
! RTL
! UBA
! Nav
! Notes
|-
| chromium
|
|
|
|
|-
| firefox
|
|
|
|
|-
| qtwebbrowser
|
|
|
|
|-
| webkit
|
|
|
|
|}

## Editors
{| class="wikitable sortable"
! App
! RTL
! UBA
! Nav
! Notes
|-
| AbiWord
|
|
|
|
|-
| emacs
|
|
|
| With extension. See also: emacs bidi editing.
|-
| gedit
|
|
|
| For Gedit <= 2.1, workaround by extension.
|-
|
|
|
|
| Qtwebbrowser-based
|-
|
|
|
|
|
|-
| LibreOffice
|
|
|
| See: LibreOffice#Bidirectional support
|-
|
|
|
|
| Blink-based
|-
| neovim
|
|
|
| See Vim#Bidirectional support
|-
|
|
|
|
| Won't fix.
|-
|
|
|
|
|
|-
| vim
|
|
|
| see Vim#Bidirectional support
|-
|
|
|
|
|
|-
| Visual Studio Code
|
|
|
|
|-
|
|
|
|
|
|-
|
|
|
|
|
|-
| GTK
|
|
|
|
|-
|
|
|
|
|
|}

## Terminal
VTE-based terminals support special escape sequences that changes Bidi behavior. For example, to enable UBA support for command output, use . For reading more about Bidi escaping sequences see {| class="wikitable sortable"
! App
! RTL
! UBA
! Nav
! Notes
|-
| alacritty
|
|
|
| Tested with  version 0.13.0-3, the 2024-01-03. Does not support RLO (U+202E).
|-
|
|
|
|
| Tested with  version 0.3.12, the 2024-01-03. Does not support RLO (U+202E).
|-
|
|
|
|
|
|-
| extraterm
|
|
|
| Tested with  version  0.74.0-1, the 2024-01-03. Does not support RLO (U+202E).
|-
| kitty
|
|
|
| Tested with  version 0.31.0-1, the 2024-01-02. Does not support RLO (U+202E).
|-
| konsole
|
|
|
| Tested with  version 23.08.4-2, the 2024-01-02.
|-
| libvte
|
|
|
| including libvte-based like Gnome, sakura, xfce4, terminator... Minor issues: [https://bugs.launchpad.net/ubuntu/+source/gnome-terminal/+bug/2002290 1
|-
|
|
|
|
| Tested with  version 3.9.3-2, the 2024-01-03.
|-
|
|
|
|
|-
| pymux
|
|
|
|
|-
|
|
|
|
| Tested with  version 1.4.0-1, the 2024-01-02. Does not support RLO (U+202E).
|-
|
|
|
|
|
|-
| Terminator
|
|
|
| Tested with  version 2.1.3-3, the 2024-01-02.
|-
| tmux
|
|
|
| Won't fix
|-
| Urxvt
|
|
|
| Tested with  version 9.31-4, the 2024-01-03. Does not support RLO (U+202E).
|-
| wezterm
|
|
|
|
|-
|
|
|
|
|
|-
| less
|
|
|
|
|}

## Other
{| class="wikitable sortable"
! App
! RTL
! UBA
! Notes
|-
| electronjs
|
|
|
|-
| groff
|
|
|
|-
| irssi
|
|
|
|-
| latex
|
|
| Using LuaTeX or XeLaTeX with polyglossia
|-
| Pandoc
|
|
|-
| typst
|
|
|-
| Wikipedia:HTML
|
|
|
|-
| wine
|
|
|
|}

## Troubleshooting
Verify UTF-8 Encoding is properly configured first. Make sure you install the fonts corresponding to your language: Arabic, Persian, Hebrew. For some terminals, () is required to properly display RTL text.

## Internal links
* Locale
* Localization
