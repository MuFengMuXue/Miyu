# Color output in console

This page was created to consolidate colorization of CLI outputs.

## Background
## Escape sequences
The ANSI escape sequences define a way to put additional information into terminal output, and color is part of this "additional information". Throughout the years the range of terminal colors has been vastly expanded, from the initial eight colors to a full 24-bit truecolor.

The basic color encoding provides 8 normal-brightness colors and 8 brighter versions of these colors. Modern terminal emulators, including the Linux console itself, allows you to specify the precise RGB values that the colors translate to.  This mode is supported by almost all terminal emulators.

With the advent of 256-color displays came the 256-color escape. The 256 colors are the 16 basic colors, the 216 RGB colors (laid out in a 6x6x6 cube), and 24 levels of greyscale. Except for the first 16 colors, the scheme is usually not customizable as it has a well-defined mapping to RGB. This mode is supported by most terminal emulators. (A minority of emulators use a similar but incompatible encoding with only 88 colors. You are very unlikely to use them in practice, but they will appear in the terminfo database.)

Less commonly supported is the truecolor mode, allowing one to use 16.7 million (224) colors in RGB (each value ranging from 0 to 255).

## Termcap and terminfo
Termcap and terminfo, part of , are databases that provide information on the escape sequences terminals (usually specified by the  env-var) understand. The  and  commands can be used to access them from command-line.

## Applications
## diff
diffutils from version 3.4 includes the  option (GNU mailing list).

 $ alias diff='diff --color=auto'

## grep
The  option enables color highlighting. Color codes are emitted only on standard output; not in pipes or redirection.

Color output in grep is also useful with regexp tasks.

Use an alias to permanently enable this option:

 alias grep='grep --color=auto'

The  variable is used to define colors, and it configures various parts of highlighting. To change the colors, find the needed ANSI escape sequence and apply it. See  for more information.

The  option includes file line numbers in the output.

## less
## Environment variables
We can tell less to emit colors when it is meaning to make bold text and other formatting effects using the  and / arguments. We can also add  to enable coloring of the less UI.

As an example, setting the  environment variable to  will set red for bold and blue for underlined.

For more info, see  or ==== Reading from stdin ====

When you run a command and pipe its standard output (stdout) to less for a paged view (e.g. ), you may find that the output is no longer colored. This is usually because the program tries to detect if its stdout is an interactive terminal, in which case it prints colored text, and otherwise prints uncolored text. This is good behaviour when you want to redirect stdout to a file, e.g. , but less suited when you want to view output in .

Some programs provide an option to disable the interactive tty detection:

 # dmesg --color=always | less

In case that the program does not provide any similar option, it is possible to trick the program into thinking its stdout is an interactive terminal with the following utilities:

*
*
:Example:
*
:Example:

Alternatively, using [https://zsh.sourceforge.net/Doc/Release/Zsh-Modules.html#The-zsh_002fzpty-Module zpty module from zsh: {{hc|~/.zshrc|
zmodload zsh/zpty

pty() {
	zpty pty-${UID} ${1+$@}
	if  ! -t 1 ;then
		setopt local_traps
		trap '' INT
	fi
	zpty -r pty-${UID}
	zpty -d pty-${UID}
}

ptyless() {
	pty $@ | less
}
}}

Usage:

 $ ptyless program

To pipe it to other pager (less in this example):

 $ pty program | less

## ls
The  option enables color highlighting. Color codes are emitted only on standard output; not in pipes or redirection.

Use an alias to permanently enable this option:

 alias ls='ls --color=auto'

The  variable is used to define colors, and it configures various parts of highlighting. Use the  command to set it.

An advanced alternative to dircolors that ships with many themes is the  package, see  for usage.

See  for more information.

## man
There is a real color facility in  (which is the default postprocessor used by man), but it is strongly discouraged for man pages. Most of the below options instead fake a colored manpage by replacing the sequences for bold, standout, and underline with spiced ones that contain color.

## Using less
First, either:

* Enable coloring in less everywhere, as in #less.
* Enable coloring in less just with man, by setting the  environment variable to (for example) . The  option is not required, due to the below option.

You then need to disable SGR/OSC escape sequences in the  postprocessor, as they don't work with less. [https://felipec.wordpress.com/2021/06/05/adventures-with-man-color/#comment-47932 This is passed through the  option of , which you can apply by setting the  environment variable to

## Using most
The basic function of 'most' is similar to  and , but it has a smaller feature set. Configuring most to use colors is easier than using less, but additional configuration is necessary to make most behave like less.
Install the  package.

Edit , uncomment the pager definition and change it to:

 DEFINE     pager     most -s

Test the new setup by typing:

 $ man whatever_man_page

Modifying the color values requires editing  (creating the file if it is not present) or editing  for system-wide changes. Example :

 % Color settings
 color normal lightgray black
 color status yellow blue
 color underline yellow black
 color overstrike brightblue black

## Using bat
 can be used as a colorizing pager for man, by setting the  environment variable
as documented here.

## Using X resources
A quick way to add color to manual pages viewed on / or  is to modify .

## xterm
 *VT100.colorBDMode:     true
 *VT100.colorBD:         red
 *VT100.colorULMode:     true
 *VT100.colorUL:         cyan

which replaces the decorations with the colors.  Also add:

 *VT100.veryBoldColors: 6

if you want colors and decorations (bold or underline) at the same time.  See  for more information.

## rxvt-unicode
 URxvt.colorIT:      #87af5f
 URxvt.colorBD:      #d7d7d7
 URxvt.colorUL:      #87afd7

Run:

 $ xrdb -load ~/.Xresources

Launch a new  or  and you should see colorful man pages.

This combination puts colors to bold and underlined words in  or to bold, underlined, and italicized text in . You can play with different combinations of these attributes. See the sources (archived) of this item.

## pacman
Pacman has a color option. Uncomment the  line in .

## Wrappers
## Universal wrappers
(most of them outdated, but still functioning)

They go with multiple preconfigured presets that can be changed, and new ones can be created/contributed.

*
*
*
*
*

## Libraries for colorizing an output
*
*
*
*

## Application specific
## Compilers
*

## diff
Diff has built-in color output, which is reasonable to use. But the following wrappers can be used:

*
*
*

## cat
*

## less
## source-highlight
You can enable code syntax coloring in less. First, install , then add these lines to your shell configuration file:

## lesspipe
Frequent users of the command line interface might want to install .

Users may now list the compressed files inside of an archive using their pager:

lesspipe also grants less the ability of interfacing with files other than archives, serving as an alternative for the specific command associated for that file-type (such as viewing HTML via ).

Re-login after installing lesspipe in order to activate it, or source .

## Make
*

## Ping
*

## Shells
## bash
See Bash/Prompt customization#Colors.

## Fish
See Fish#Web interface.

## xonsh
See Customizing the Prompt.

## zsh
See Zsh#Colors.

## Terminal emulators
## Virtual console
The colors in the Linux virtual console running on the framebuffer can be changed. This is done by writing the escape code , where  is the hexadecimal index of the color from 0-F, and  is a traditional hexadecimal RGB code.

For example, to reuse existing colors defined in , add the following to the shell initialization file (such as ):

 if [ "$TERM" = "linux" ]; then
     _SEDCMD='s/.*\*color\(\2/p'
     for i in $(sed -n "$_SEDCMD" $HOME/.Xresources | awk '$1 &2 2>&1 ) | tee -a /dev/stderr | grep -o '"[^"*"'|
033}}

## Enumerate supported colors
The following command will let you discover all the terminals you have terminfo support for, and the number of colors each terminal supports. The possible values are: 8, 15, 16, 52, 64, 88 and 256.

## Color scheme scripts
See [https://paste.xinu.at/m-dAiJ/ for scripts which display a chart of your current terminal scheme.

## True color support
Some terminals support the full range of 16 million colors (RGB, each with 8 bit resolution): xterm, konsole, st, etc. The corresponding TERM values , , , etc. are supported starting with ncurses version 6.1 For more info about terminal emulators and applications that support true color, see [https://github.com/termstandard/colors/blob/master/README.md.

Note that the Linux kernel supports the SGR (Select Graphic Rendition) escape sequences for true-color, but it is pointless to use it, because the driver maps the 24-bit color specifications to a 256-colors color map in the kernel (see the functions , ). For this reason, there is no terminfo entry .
