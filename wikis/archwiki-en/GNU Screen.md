# GNU Screen

GNU Screen is a full-screen window manager that multiplexes a physical terminal between several processes, typically interactive shells. Programs running in Screen continue to run when their window is currently not visible and even when the whole screen session is detached from the user's terminal.

See the official overview GNU Screen manual for the description of the features.

## Installation
Install the  package.

## Usage
Commands are entered pressing the "escape key"  and then the key binding.

Some users find the default escape key  inconvenient. The escape key can be changed to another key as described in #Change the escape key.

## Common Commands
*   Displays commands and their defaults
*   Enter to the command prompt of screen
*   Window list
*   opens window 0
*   Rename the current window
*   Sends  to the current window
*   Create a new window (with shell)
*   Split current region horizontally into two regions
*   Split current region vertically into two regions
*   Switch the input focus to the next region
*   Toggle between current and previous region
*   Enter Copy Mode (use enter to select a range of text)
*   Paste text
*   Close all regions but the current one
*   Close the current region
*   Detach from the current screen session, and leave it running. Use  to resume

## Command Prompt Commands
*   Closes all windows and closes screen session
*   Reloads screenrc configuration file (can alternatively use )

## Named sessions
To create a named session, run screen with the following command:

 $ screen -S session_name

To (re)name an existing a session, run the following command while screen is running:

To print a list of pid.tty.host strings identifying your screen sessions:

 $ screen -list

To attach to a named screen session, run this command:

 $ screen -x session_name

or

 $ screen -r session_name

## Customizing Screen
You can modify the default settings for Screen according to your preference either through a personal  file which contains commands to be executed at startup (e.g. ) or on the fly in command mode (e.g.  ).

## Tips and tricks
## Autostart with systemd
This service autostarts screen for the specified user (e.g. ). Running this as a system unit is important, because systemd --user instance is not guaranteed to be running and will be killed when the last session for given the user is closed.

## Change the escape key
It can be a good idea to change the default escape key, not only because "a" is usually typed with the left pinky, but also because  is mapped to the common command  in GNU Readline and Bash-like shells.

The escape key can be changed with the  option in , or the  option to .

For example, if you find that you rarely type  in your shell or editor, you could use  to set the escape key to . The second "j" means that a literal  can be sent to the terminal via the sequence  . For Dvorak keyboard users,  () might be more convenient.

More exotic options include  which sets the escape key to , or  which sets it to .

The escape key is also called the "command character" in Screen documentation.

## Start at window 1
By default, the first screen window is 0. If you would rather never have a window 0 and start instead with 1, add the following lines on your configuration:

## Nested Screen Sessions
It is possible to get stuck in a nested screen session. A common scenario: you start an SSH session from within a screen session. Within the SSH session, you start screen. By default, the outer screen session that was launched first responds to  commands. To send a command to the inner screen session, use  , followed by your command. For example:

*    Detaches the inner screen session.
*    Kills the inner screen session.

## Start Screen on every shell
For Bash and Zsh, add the following snippet to your  or  before your aliases:

## Use 256 colors
By default, Screen uses an 8-color terminal emulator. To enable more colors, you need to be using a terminal that supports them and set the correct term value. This will use terminfo to describe how the ANSI escape codes will be interpreted. An entry in the terminfo database structure must exist,  provides many common descriptions stored under .

First try the generic value:

If that does not work, try setting it based on your terminal. When using xterm-based terminal:

When using rxvt-unicode:

As a last resort, try setting termcapinfo instead:

## Informative statusbar
The default statusbar may be a little lacking. You may find this one more helpful:

{{hc|~/.screenrc|
truecolor on
hardstatus off
hardstatus alwayslastline '%{#00ff00}[ %H ]%{7}%?%-Lw%?%{1;0}%{1}(%{15}%n%f%t%?(%u)%?%{1;0}%{1})%{7}%?%+Lw%? %=%{#00ff00}[ %{#00a5ff}%{6}%Y-%m-%d %{#ffffff}%{7}%0c%{#00ff00} ]'
}}

statusbar at top:

## Turn welcome message off
## Turn your hardstatus line into a dynamic urxvt|xterm|aterm window title
This one is pretty simple; just switch your current  line into a  line with notification, and edit accordingly:

{{hc|~/.screenrc|
termcapinfo rxvt* 'hs:ts=\E]2;:fs=\007:ds=\E]2;\007'
hardstatus string "screen (%n: %t)"
caption always '%{= 7;0}%Y-%m-%d %c %-Lw%{+b 2;0}%t%{-}%+Lw%=%{-}'
}}

This will give you something like  in the title of your terminal emulator. The caption supplies the date, current time, and colorizes your screen window collection.

## Use X scrolling mechanism
The scroll buffer of GNU Screen can be accessed with  . However, this is very inconvenient. To use the scroll bar of e.g. xterm or Konsole, add the following line === Attach an existing running program to screen ===

If you started a program outside Screen, but now you would like it to be inside, you can use reptyr to reparent the process from its current TTY to one inside screen.

Install the  package.

Get the PID of the process (you can use  for that). Now just enter the PID as argument to reptyr inside a screen window.

 $ reptyr pid

## Setting a different bash prompt while in screen
If you want a different bash prompt when in a screen session, add the following to your [https://serverfault.com/questions/257975/how-to-check-if-im-in-screen-session:

## Turn off visual bell
With this setting, Screen will not make an ugly screen flash instead of a bell sound.

## Getting rid of the vertical and horizontal bars
To get rid of the vertical bars:

To hide the horizontal bar, set the back and foreground color to default (d) and display a blank (" "):

{{hc|~/.screenrc|
caption string "%{03} "
}}

If this does not work, try {{ic|caption string "%{00} "}} instead. For the default caption in black and white, use {{ic|caption string "%{00}%3n %t"}}.

## Troubleshooting
## Fix for residual editor text
When you open a text editor like nano in screen and then close it, the text may stay visible in your terminal. To fix this, put the following:

## Fix for Name column in windowlist only show "bash"
Add following to :
