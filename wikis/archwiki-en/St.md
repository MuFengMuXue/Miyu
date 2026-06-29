# St

st is a simple terminal implementation for Xorg by suckless. It is intended to serve as a lightweight replacement for xterm or urxvt. It currently supports 256 colors, true colors, most VT10X escape sequences, UTF-8, X11 copy/paste, anti-aliased fonts, fallback fonts, resizing, shortcuts, and line drawing.

## Installation
Install the  package. On Wayland, st uses Xwayland; at this current time there is no active Wayland port available, the Xwayland memory-footprint is unavoidable.

## Configuration
st is configured through its  file which is copied over at compile time. Defaults are stored in  which is included with the source. Consider maintaining your own  and PKGBUILD.

## Shell
To change the default shell for st, edit this line:

 static char *shell = "/bin/sh";

Or start st with the desired shell as last argument:

 $ st options fish

## Term
To change the terminal type, edit this line:

 static char *termname = "st-256color";

st will set the  variable with the value of .

## Font
Edit the following line as you prefer:

 static char *font = "Liberation Mono:pixelsize=12:antialias=false:autohint=false";

You can also pass the value of the font in the command line:

 $ st -f "Liberation Mono:size=12"
 $ st -f 'Liberation Mono-12'

Font names can be found with .

## Cursor
By default, the mouse pointer is  which often can be hard to find. To change it to your cursor theme's normal one, edit the following:

 static unsigned int mouseshape = XC_left_ptr;

## Colors
Edit the following lines to set foreground, background, and cursor colors:

 unsigned int defaultfg = 7;
 unsigned int defaultbg = 0;
 static unsigned int defaultcs = 256;

The values refer to the  array in the configuration file. You can use the default colors or add yours in :

{{bc|1=
static const char *colorname= {
   	/* 8 normal colors */
       "black",
       "red3",
       "green3",
       "yellow3",
       "blue2",
       "magenta3",
       "cyan3",
       "gray90",

       /* 8 bright colors */
       "gray50",
       "red",
       "green",
       "yellow",
       "#5c5cff",
       "magenta",
       "cyan",
       "white",

       [255 = 0,

       /* more colors can be added after 255 to use with DefaultXX */
       "#cccccc",
       "#eeeeee",
       "#111111",
 };

/*
 * Default colors (colorname index)
 * foreground, background, cursor
 */
unsigned int defaultfg = 257;
unsigned int defaultbg = 258;
static unsigned int defaultcs = 256;
}}

Tools exist to facilitate the creation of color palettes. For example, terminal.sexy has a set of pre-made ones and exports directly to sts format (see comment on issue 22).

There is a patch for the Solarized color scheme. See https://st.suckless.org/patches/solarized/ to install it.

## Patches
There are many patches available from the suckless website. To apply a patch, download the diff and apply it with . This alters the default configuration file ; if you are maintaining your own , copy your configs from  into a copy of  and rename it , then .

## Desktop entry
To simplify launching st with a decent font (e.g. ) in a desktop environment, you can also create a desktop entry:

The menu entry will appear as Simple Terminal in the System Tools application list.

## Troubleshooting
## Keyboard
Add the following to  or  if  is not working properly in some applications:

 set enable-keypad on

If the above does not work with some applications such as IPython using bash, instead, turn off  and add the following to your , as mentioned in the st FAQ:

 printf '\033>/dev/tty

## Vim
## The background colour of text in vim will not fill in anything that is not a character
Try setting the value of  in your  to  and recompiling. And do not set the  var in your shell, at least not to  as this seems to cause the issue.

Another solution, perhaps a better one, is to have the following lines in your  file:

 if &term =~ '256color'
     " disable Background Color Erase (BCE) so that color schemes
     " render properly when inside 256-color tmux and GNU screen.
     " see also https://sunaku.github.io/vim-256color-bce.html
     set t_ut=
 endif

## 256color and truecolor support not working in tmux or otherwise
First, make sure you are not setting and exporting the value of  in your  as mentioned in this [https://bbs.archlinux.org/viewtopic.php?pid=1755862#p1755862 thread

Second, make sure the version of  you are using is  ', which is when  was added.

Finally, add the following to :

 set t_8f=^38;2;%lu;%lu;%lum        " set foreground color
 set t_8b=^" set background color
 colorscheme Tomorrow-Night-Eighties
 set t_Co=256                         " Enable 256 colors
 set termguicolors                    " Enable GUI colors for the terminal to get truecolor

## Arabic shaping support
As explained in [[Vim#Bidirectional support, for full Arabic character support, you need a fallback font covering the Unicode entries for Arabic Forms-B. To do that, add font2 patch and edit your config as follows:

 static char *font = "Cascadia Code:size=12:pixelsize=13:antialias=true:autohint=true";
 static char *font2[ = { "DejaVu Sans Mono:size=12:pixelsize=13:antialias=true:autohint=true" };

Then launch  with . This set up covers most Arabic shaping cases: no shaping, italicized no shaping, Forms-B, italicized Forms-B.
