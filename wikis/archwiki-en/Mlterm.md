# Mlterm

mlterm is a very fast low latency terminal emulator that has many unique features such as rendering variable width fonts, proper bidirectional support out of the box, a daemon mode, multiple XIM as well as true background transparency.

## Installation
Install the  package.

## Configuration
Settings are stored permanently in plain text files under .

Most are defined in

All settings can be set through command line options.

A GUI configuration wizard can be opened with  and assist in experimenting with different settings.

## Padding
Padding can be enabled by setting the  in the main configuration file  or using the  option.

## Fonts
Fonts are defined separately in two different files  (monospace) and  (non-monospace).

 ENCODING = FONT NAME, SIZE

Each encoding can use a different font. Check the man page for a complete list of encodings.

Mlterm is provided with a tool called  that populates  with a list of Unicode blocks-Font pairs that can assist you further down with choosing which fonts to use for specific languages.

## Using variable width fonts
 can properly display variable width fonts. First, define them in

 DEFAULT = Latin Modern Roman, 12

And enable the option in

 use_variable_column_width = true

Alternatively, you can pass it on the command line  or check the Variable column width option in the Font dialog of the configuration window.
Antialiasing needs to be enabled otherwise it will fallback to monospace.

 use_anti_alias = true

Depending on the font, adjust Screen size ratio against font size in order to fit the window to the new variable width of its cells.
Use the  option or save it permanently in the main configuration file:

 screen_width_ratio = percentage

## Custom colors
You can define your custom colors in  file with the following color names :

 black=#48483e
 red=#dc2566
 green=#8fc029
 yellow=#d4c96e
 blue=#55bcce
 magenta=#9358fe
 cyan=#56b7a5
 white=#acada1
 hl_black=#76715e
 hl_red=#fa2772
 hl_green=#a7e22e
 hl_yellow=#e7db75
 hl_blue=#66d9ee
 hl_magenta=#ae82ff
 hl_cyan=#66efd5
 hl_white=#cfd0c2

In addition, foreground and background color values need to be specified separately either with  and  arguments or permanently stored in  :

 fg_color = #f1ebeb
 bg_color = #272822

Values for the previous examples correspond to the .Xresources monokai color theme.== Usage ==

You can access the backscroll mode to scroll the buffer by pressing  or  keys or using the mouse wheel.

To enter buffer selection mode, press  and use arrow keys to navigate. Begin and end your selection by pressing the space  key. The selected text will be copied to your clipboard.

Both modes support vi movement using  and  keys to navigate the screen.

## Troubleshooting
## Backspace key sequence
By default,  sends .
Because some programs don't recognize this key sequence, you can add the following to your  file :
 BackSpace="\x7f"

## Fix dots appearing outside the text drawing area
Some fonts have glyphs (e.g. arabic letters, diacritic marks, brackets etc.) that overflow the text drawing area. They can produce dots that stick on the terminal and accumulate over time.
Similar to xterms  setting, enable clipping either with the  option or by adding
 use_clipping = true
to your main configuration file.

## Render CJK characters when using Xft
If you see empty glyph boxes when rendering CJK characters, that is because the font you are using does not support them, and unlike using cairo, mlterm with Xft does not look for a fallback fonts as an alternative (as explained by the author in [https://github.com/arakiken/mlterm/issues/18#issuecomment-841337016 GitHub issue#18).

If your default font does not support CJK glyphs, you can specify such font (such as ) as a fallback font besides your default font in  :

 DEFAULT = Fantasque Sans Mono 12
 ISO10646_UCS4_1_FULLWIDTH = Noto Sans Mono CJK JP 10

## Render Arabic script in Xft
If your main font is not supporting Arabic unicode ranges, you can specifically instruct mlterm to use a font with proper support for Arabic characters (such as DejaVu Sans Mono) by providing an exhaustive list of all unicode ranges for the Arabic script :

 U+10a60-10a7f = DejaVu Sans Mono, 10
 U+10a80-10a9f = DejaVu Sans Mono, 10
 U+600-6ffj    = DejaVu Sans Mono, 10
 U+750-77f     = DejaVu Sans Mono, 10
 U+8a0-8ff     = DejaVu Sans Mono, 10
 U+1ee00-1eeff = DejaVu Sans Mono, 10
 U+10e60-10e7f = DejaVu Sans Mono, 10
 U+fe70-feff   = DejaVu Sans Mono, 10
 U+fb50-fdff   = DejaVu Sans Mono, 10

## Arabic script rendering when using fixed width fonts
When entering in Arabic on a R-to-L line, proper rendering of ligatures might need a screen refresh when using fixed width fonts. One workaround is to enable the  option and set your vaafont to the fixed width font. follow this issue on github.
