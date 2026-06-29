# Vifm

From the Vifm home page:

:Vifm is a file manager with curses interface, which provides Vim-like environment for managing objects within file systems, extended with some useful ideas from mutt.
:If you use vi, Vifm gives you complete keyboard control over your files without having to learn a new set of commands.

## Installation
Install the  package.

## Help file
Basic information about Vifm is given in the help file. You can view it by opening Vifm and typing:

 :h

Another good source of information is .

## Customizing Vifm
Vifm creates and populates a  directory in XDG_CONFIG_HOME containing the following:
*  — a well commented configuration file that can be edited to suit your working style.
*  — the help text
*  — bookmarks and trash contents — it is not recommended to edit this file by hand
*  directory — self explanatory — see  in vifm
*  directory — see  in vifm
*  directory — color schemes — see  in vifm
**  — well commented default color scheme — can be copied to create user-created color schemes

To get started, read the information available in:
*
*   or
*   in vifm

## Color schemes
The  directory contains the color schemes.  The format is outlined in the file and follows vi/vim syntax highlight format. It is basically:
 highlight group cterm=attribute ctermfg=color ctermbg=color

An example color scheme looks like this:
 highlight Win cterm=none ctermfg=white ctermbg=black
 highlight Directory cterm=bold ctermfg=cyan ctermbg=none
 highlight Link cterm=bold ctermfg=yellow ctermbg=none
 highlight BrokenLink cterm=bold ctermfg=red ctermbg=none
 highlight Socket cterm=bold ctermfg=magenta ctermbg=none
 highlight Device cterm=bold ctermfg=red ctermbg=none
 highlight Fifo cterm=bold ctermfg=cyan ctermbg=none
 highlight Executable cterm=bold ctermfg=green ctermbg=none
 highlight Selected cterm=bold ctermfg=magenta ctermbg=none
 highlight CurrLine cterm=bold ctermfg=none ctermbg=blue
 highlight TopLine cterm=none ctermfg=black ctermbg=white
 highlight TopLineSel cterm=bold ctermfg=black ctermbg=none
 highlight StatusLine cterm=bold ctermfg=black ctermbg=white
 highlight WildMenu cterm=underline,reverse ctermfg=white ctermbg=black
 highlight CmdLine cterm=none ctermfg=white ctermbg=black
 highlight ErrorMsg cterm=none ctermfg=red ctermbg=black
 highlight Border cterm=none ctermfg=black ctermbg=white

You can also highlight different file types using regular expressions:
 highlight /^.*\.(mp3|ogg|oga|flac|m4a)$/ ctermfg=magenta
 highlight /^.*\.(jpg|jpeg|png|gif|tiff|webp|bmp|svg|svgz)$/ ctermfg=yellow
 highlight /^.*\.(zip|gz|bz2|xz|tar|tgz|tbz2|7z|rar|iso|rpm|deb)$/ ctermfg=red

Other color schemes can be seen here.

## Key mapping
As of 0.6.2, you can customize key bindings in Vifm. These can be set from the command mode using the map command, like so:
 :map ] :s

However, these mappings will not be saved between sessions. To map a key permanently, place them in your .  More sample mappings can be seen at the end of that file.

## Opening files in Vifm
You can assign applications to file types in , e.g.:
 filetype *.jpg,*.jpeg,*.png,*.gif feh %f 2>/dev/null &
 filetype *.md5 md5sum -c %f
Several defaults can be found in .  These can be edited or added following the same format.

## Browse images in current directory with feh
 filetype *.jpg,*.jpeg,*.png,*.gif
        \ {View in feh}
        \ feh -FZ %d --start-at %d/%c 2>/dev/null
This displays your selected image in feh and enables you to browse all other images in the directory as well, in their default order.

## User commands
You can also create custom commands in , e.g.:
 command df df -h %m 2> /dev/null
 command diff vim -d %f %F

## Creating symbolic links
 command link ln -s %d/%f %D
When you call
 :link
a link of the selected file is made in the other directory (if you are in split view). It even works with multiple files selected with visual (v) or tag (t).

## Torrent creation
Make a .torrent of the current file in the other tab's directory:
 command mkt mktorrent -p -a announce url here -o %D/%f.torrent %d/%f

## Marks
Marks can be set the same way as in vi.
To set a mark for current file:
 mGo to a file identified by a mark:
 '[a-zVifm will remember the marks between sessions.

## Previews
Provided  is installed,
putting
 fileviewer *.pdf
   \ pdftotext %c -
into  enables PDF previewing using pdftotext.
The  is a vifm macro for the current file under the cursor.
The preview is activated with
 :view

Neat image previewing can be achieved using img2txt from :
 fileviewer *.png,*.jpeg,*.jpg
  \ img2txt %c
Previewing the contents of tar archives:
 fileviewer *.tar,*.tar.gz
  \ tar -tvf %c
For previewing HTML documents, suitable programs are
text-based browsers including ,  or :
 fileviewer *.html
  \ w3m %c
Previewing office files by converting them to HTML and then rendering that with w3m:
 fileviewer *.odt,*.doc,*.docx,*.ods,*.xls,*.xlsx
  \ libreoffice --convert-to html --outdir /tmp/ %c &>/dev/null && w3m /tmp/%c:r.html
For printing text instead of previewing the file (for binary files for example):
 fileviewer *.exe
  \ echo Binary file: no preview available. %i
 is there because  is implicitly used if no other macro is used. In this case,  is ignored.

For handling filetypes not handled by anything else, put  as the last fileviewer option in your configuration file.

Further useful programs for previews include
*  for directory previews
*  for viewing information about mp3 files
*  for the mediainfo program (audio and video information)
*  for syntax highlighting

## Using vifmimg
It is also possible to clone [https://github.com/cirala/vifmimg vifmimg into your  directory. Than you need to create an alias to run the  script, which will prepare everything for the previews:
 alias v="~/.config/vifm/vifmrun ."
 should start just by typing  in your terminal now.

## Tips and tricks
## Useful key mappings
## Single stroke to access command line
 nmap ; :

## Faster movement
Hold shift to jump five files
 nnoremap J 5j
 nnoremap K 5k

## Panel resizing
Just type  or  to resize the panels
 nnoremap - 55>

## Yanking
Yank the parent directory path by typing

 nnoremap yd :!echo -n %d | xclip -selection clipboard %i:echo expand('%"d') "is yanked to clipboard"

Yank the absolute path to the selected element by typing

 nnoremap yf :!echo -n %c:p | xclip -selection clipboard %i:echo expand('%"c:p') "is yanked to clipboard"

In a Wayland environment replace  with wl-copy.

## Non-vim users
If you use ,  (Neovim), or another editor, you can add , , or equivalent to the bottom of your  file.

## Total size of selected files
To get the total size of selected files change %s to %E in , like so:
 set statusline="  %t%= %A %10u:%-7g %15E %20d  "

## Use output of external program in status line
Here is a status line that calls lsattr, passing it the name of the file currently under the cursor:
 set statusline="%{system('lsattr -l ' . expand('%c'))}"

## Print the currently selected file
If you want to print a file with your printer, then you can create a command with  :
 command! print lp -n 1 -o sides=two-sided-long-edge %f
You just need to select your file which should be printed and type

## Drag and Drop
You will need to install  and add a new command:

 command! dragon dragon-drop -a -x %f

If you want, you can also set a shortcut to this new command:

 nmap  :dragon

So if you press  a window for your currently selected file is created so you can drop it somewhere else. If you want to drag multiple files, just select the files with  and press .

For more information see expression syntax and available functions.
