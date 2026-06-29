# Gmrun

Gmrun (Gnome Completion-Run) is an lightweight application launcher similar to GNOME Run, Application Finder, KRunner, etc.

## Installation
Gmrun can be installed with the package .

## Usage
* GUI applications can just be typed in and run by pressing , terminal applications can be run by using . Pressing  with an empty input box will open up a terminal window.
* Gmrun features tab completion: pressing tab will bring up a scrollable list of possible matches.
* Web addresses entered into Gmrun will launch a web browser automatically.
* The same goes for email addresses, using the  prefix e.g. , will launch your email client.
* More shortcuts can be added to  (See #Configuration below) or you can modify the system-wide file at .
* You can enter search mode by entering  as the first letter, the title should change from Run program to Search, letters you input will then automatically come up with suggestions from your command history.
*  will allow you to search backwards through that history.
*  will search forward through the history.
*  will cancel the search.
* If an extension has been defined in the configuration file, files can be launched by the correct program just by typing the file name.
* Press  to close Gmrun, without running anything.

## Configuration
The configuration file is located at  but you can create a per-user configuration (recommended) in . Please note that  is expanded to the full command entered,  is the last part after the shortcut (e.g. if you enter the URL ,  would keep  and  would shorten to . )

Here is an example configuration file.
{{hc|~/.gmrunrc|
# gmrun configuration file
# gmrun is (C) Mihai Bazon,
# GPL v2.0 applies

# Set terminal
Terminal = urxvt
TermExec = ${Terminal} -e
AlwaysInTerm = ssh telnet ftp lynx mc vi vim pine centericq perldoc man

# Set window geometry (except height)
Width = 400
Top = 300
Left = 450

# History size
History = 256

# Shows last history line selected when invoked
ShowLast = 1

# Show files starting with '.'
# Default is 0 (off), set it to 1 if you want "hidden" files to show up
# in the completion window
ShowDotFiles = 0

# Timeout (in milliseconds) after which gmrun will simulate a TAB press
# Set this to NULL if do not like this feature.
TabTimeout = 0

# URL handlers
# If the entered text is "http://www.google.com" then:
#   - %u gets replaced with the whole URL ("http://www.google.com")
#   - %s gets replaced with "//www.google.com".  This is useful for URL-s
#     like "man:printf" --> %s will get replaced with "printf"
URL_http = firefox %u
URL_mailto = firefox -remote "mailto(%s)"
URL_man = ${TermExec} 'man %s'
URL_info = ${TermExec} 'info %s'
URL_pd = ${TermExec} 'perldoc %s'
URL_file = pcmanfm %s
URL_readme = ${TermExec} 'less /usr/doc/%s/README'
URL_info = ${TermExec} 'info %s'
URL_sh = sh -c '%s'
URL_paci = ${TermExec} 'pacman -S %s'
URL_pacs = ${TermExec} 'pacman -Ss %s'

# extension handlers
EXT:doc,rtf = AbiWord %s
EXT:txt,cc,cpp,h,java,html,htm,epl,tex,latex,js,css,xml,xsl,am,php,css,js,py,rb = gedit %s
EXT:mpeg,mpg,avi,mkv,flv = vlc %s
EXT:mp3,ogg,m4a,wmv,wma = deadbeef %s
EXT:ps = gv %s
EXT:pdf = epdfview %s
}}

; ShowDotFiles (1 or 0): whether to show dotfiles (e.g. ) in the auto-complete menu.
; TabTimeout (1 or 0): Whether to show the tab complete menu automatically when something is inputted.
; Terminal: The command to run when  is pressed without other input.
; TermExec: The command to run when running a specific command in the terminal (e.g. ).
; URL_http: The command to run when a web address is entered.
; URL_mailto: The command to run when an email address is entered.
; EXT:extension: The application to open files with a certain extension.
; Top and Left: The placement of the Gmrun window (in pixels from the respective edge).
; Width: The width in pixels of the window.
; History: Length of command history that is stored.

## Adding custom shortcuts
Shortcuts can easily be added. For example, to use g as a shortcut for Google searches, add:

 URL_g = firefox 'https://www.google.com/search?q=%25s'

Which is then used like this:

 g:Arch

## Key bindings
You can use your desktop environment's or window manager's keybinding settings to set one for Gmrun.
