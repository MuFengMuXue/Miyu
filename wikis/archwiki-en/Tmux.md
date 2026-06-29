# Tmux

tmux is a "terminal multiplexer: it enables a number of terminals (or windows), each running a separate program, to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattached."

tmux is an ISC-licensed alternative to GNU Screen. Although similar, there are many differences between the programs, as noted on the tmux FAQ page.

## Installation
Install the  package.

## Configuration
By default, tmux looks for user-specific configuration at  followed by , as of 3.2. A global configuration file may be provided at  though by default Arch does not ship such a file.

## Key bindings
By default, command key bindings are prefixed by . For example, to vertically split a window type .

After splitting a window into multiple panes, a pane can be resized by hitting the prefix key (e.g. ) and, while continuing to hold , press ///. Swapping panes is achieved in the same manner, but by hitting  instead of a directional key.

Key bindings may be changed with the bind and unbind commands in . For example, the default prefix binding of  can be changed to  by adding the following commands in your configuration file:

To create a new window you can use  and move forward one window with  and backwards one window with .

Additional ways to move between windows include the following:

 Ctrl+b l (Move to the previously selected window)
 Ctrl+b w (List all windows / window numbers)
 Ctrl+b  (Move to the specified window number, the default bindings are from 0 – 9)
 Ctrl+b q  (Show pane numbers, when the numbers show up type the key to go to that pane)

tmux has a find-window option & key binding to ease navigation of many windows:

 Ctrl+b f  (Search for window name)
 Ctrl+b w (Select from interactive list of windows)

## Copy Mode
A tmux window may be in one of several modes. The default permits direct access to the terminal attached to the window; the other is copy mode. Once in copy mode you can navigate the buffer including scrolling the history. Use vi or emacs-style key bindings in copy mode. The default is emacs, unless VISUAL or EDITOR contains ‘vi’

To enter copy mode do the following:

 Ctrl+b [

You can navigate the buffer as you would in your default editor.

To quit copy mode, use one of the following keybindings:

vi mode:
 q
emacs mode:
 Esc

## Browsing URLs
To browse URLs inside tmux you must have  installed and configured.

Inside a new terminal:
 bind-key u capture-pane \; save-buffer /tmp/tmux-buffer \; run-shell "$TERMINAL -e urlview /tmp/tmux-buffer"

Or inside a new tmux window (no new terminal needed):
 bind-key u capture-pane \; save-buffer /tmp/tmux-buffer \; new-window -n "urlview" '$SHELL -c "urlview  /dev/null"
 bind-key C-y run "xclip -o -sel clip | tmux load-buffer - ; tmux paste-buffer"

Vim style:

 bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "xclip -i -sel clip > /dev/null"
 bind-key p run "xclip -o -sel clip | tmux load-buffer - ; tmux paste-buffer"

## On Wayland
Make sure to have  installed.

Emacs style:

 bind-key -T copy-mode y send-keys -X copy-pipe-and-cancel "wl-copy && wl-paste -n | wl-copy -p"
 bind-key C-y run "wl-paste -n | tmux load-buffer - ; tmux paste-buffer"

Vim style:

 bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "wl-copy && wl-paste -n | wl-copy -p"
 bind-key p run "wl-paste -n | tmux load-buffer - ; tmux paste-buffer"

## Urxvt middle click
There is an unofficial perl extension (mentioned in the official FAQ) to enable copying/pasting in and out of urxvt with tmux via Middle Mouse Clicking.

First, you will need to download the perl script and place it into urxvts perl lib:

You will also need to enable that perl script in your .Xdefaults:

Next, you want to tell tmux about the new function and enable mouse support (if you have not already):

That's it. Be sure to end all instances of tmux before trying the new MiddleClick functionality.

While in tmux, Shift+MiddleMouseClick will paste the clipboard selection while just MiddleMouseClick will paste your tmux buffer.
Outside of tmux, just use MiddleMouseClick to paste your tmux buffer and your standard  to copy.

## Tips and tricks
## Start tmux with default session layout
Session managers like tmuxinator and tmuxp make it easy to manage common session configurations.

For tmuxinator, install . Test your installation with

 $ tmuxinator doctor

## Get the default layout values
Start tmux as usual and configure your windows and panes layout as you like. When finished, get the current layout values by executing (while you are still within the current tmux session)

 tmux list-windows

The output may look like this (two windows with 3 panes and 2 panes layout)

 0: default* (3 panes) [layout 20a0,274x83,0,0{137x83,0,0,3,136x83,138,0136x41,138,0,5,136x41,138,42,6} @2 (active)
 1: remote- (2 panes) [layout e3d3,274x83,0,0274x41,0,0,4,274x41,0,42,7 @3

The Interesting part you need to copy for later use begins after and excludes ...  @2 (active). For the first window layout you need to copy e.g. 20a0,274x83,0,0{137x83,0,0,3,136x83,138,0==== Define the default tmux layout ====

Knowing this, you can exit the current tmux session. Following this, you create your default tmux session layout by editing tmuxinator's configuration file (Do not copy the example, get your layout values as described above)

{{hc|~/.tmuxinator/default.yml|
name: default
root: ~/
windows:
  - default:
      layout: 20a0,274x83,0,0{137x83,0,0,3,136x83,138,0[136x41,138,0,5,136x41,138,42,6}
      panes:
        - clear
        - vim
        - clear && emacs -nw
  - remote:
      layout: 24ab,274x83,0,0{137x83,0,0,3,136x83,138,0,4}
      panes:
        -
        -
}}

The example defines two windows named "default" and "remote". With your determined layout values. For each pane you have to use at least one  line. Within the first window panes you start the commandline "clear" in pane one, "vim" in pane two and "clear && emacs -nw" executes two commands in pane three on each tmux start. The second window layout has two panes without defining any start commmands.

Test the new default layout with:

 $ tmuxinator default

## Autostart tmux with default tmux layout
If you like to start your terminal session with your default tmux session layout edit your shell configuration file:

## Alternate approach for default session
Instead of using the above method, one can just write a bash script that when run, will create the default session and attach to it.
Then you can execute it from a terminal to get the pre-designed configuration in that terminal

 #!/bin/bash
 tmux new-session -d -n WindowName Command
 tmux new-window -n NewWindowName
 tmux split-window -v
 tmux selectp -t 1
 tmux split-window -h
 tmux selectw -t 1
 tmux -2 attach-session -d

## Start tmux in urxvt
Use this command to start urxvt with a started tmux session.  I use this with the exec command from my .ratpoisonrc file.

## Start tmux on every shell login
 if [ -x "$(command -v tmux)" ] && [ -n "${DISPLAY}" ] && [ -z "${TMUX}" ]; then
     exec tmux new-session -A -s ${USER} >/dev/null 2>&1
 fi

What the above snippet does is the following:

# test if tmux is executable,
# and if a graphical session is running (remove this condition if you want tmux to start in any login shell, but it might interfere with autostarting X at login),
# and if we are not already inside a tmux session,
# then try to attach, if the attachment fails, start a new session.

If you are using systemd as a user to keep a session alive, you can replace the command inside the if-block with the following commands to attach to that session and detach all the other connected clients:

 if ! systemctl --user is-active --quiet tmux.service; then
     systemctl --user start tmux.service
 fi
 exec tmux attach-session -d -t "${USER}" >/dev/null 2>&1

## Start a non-login shell
tmux starts a login shell by default, which may result in multiple negative side effects:

* Users of fortune may notice that quotes are printed when creating a new panel.
* The configuration files for login shells such as  are interpreted each time a new panel is created, so commands intended to be run on session initialization (e.g. setting audio level) are executed.

To disable this behaviour, add to :

 set -g default-command "${SHELL}"

## Use tmux windows like tabs
The following settings added to  allow to use tmux windows like tabs, such as those provided by the reference of these hotkeys — urxvt's tabbing extensions. An advantage thereof is that these virtual “tabs” are independent of the terminal emulator.

 #urxvt tab like window switching (-n: no prior escape seq)
 bind -n S-down new-window
 bind -n S-left prev
 bind -n S-right next
 bind -n C-left swap-window -t -1
 bind -n C-right swap-window -t +1

Of course, those should not overlap with other applications' hotkeys, such as the terminal's. Given that they substitute terminal tabbing that might as well be deactivated, though.

It can also come handy to supplement the EOT hotkey  with one for tmux's detach:

 bind-key -n C-j detach

## Clients simultaneously interacting with various windows of a session
In Practical Tmux, Brandur Leach writes:

: Screen and tmux's behaviour for when multiple clients are attached to one session differs slightly. In Screen, each client can be connected to the session but view different windows within it, but in tmux, all clients connected to one session must view the same window.
: This problem can be solved in tmux by spawning two separate sessions and synchronizing the second one to the windows of the first, then pointing a second new session to the first.

The  script below implements this — the version here is slightly modified to execute  if  is its second parameter. Invoked as , it launches the base session if necessary. Otherwise a new "client" session linked to the base, optionally add a new window and attach, setting it to kill itself once it turns "zombie". Do not forget to make it executable.

{{hc|~/bin/tmx|2=
#!/bin/bash
# Modified TMUX start script from:
#     http://forums.gentoo.org/viewtopic-t-836006-start-0.html

# Works because bash automatically trims by assigning to variables and by passing arguments
trim() { echo $1; }

if  -z "$1" ; then
    echo "Specify session name as the first argument"
    exit
fi

# Only because I often issue `ls` to this script by accident
if  "$1" == "ls" ; then
    tmux ls
    exit
fi

base_session="$1"
# This actually works without the trim() on all systems except OSX
tmux_nb=$(trim `tmux ls | grep "^$base_session" | wc -l`)
if  "$tmux_nb" == "0" ; then
    echo "Launching tmux base session $base_session ..."
    tmux new-session -s $base_session
else
    # Make sure we are not already in a tmux session
    if  -z "$TMUX" ; then
        echo "Launching copy of base session $base_session ..."
        # Session id is date and time to prevent conflict
        session_id=`date +%Y%m%d%H%M%S`
        # Create a new session (without attaching it) and link to base session
        # to share windows
        tmux new-session -d -t $base_session -s $session_id
        if  "$2" == "1" ; then
		# Create a new window in that session
		tmux new-window
	fi
        # Attach to the new session & kill it once orphaned
	tmux attach-session -t $session_id \; set-option destroy-unattached
    fi
fi
}}

A useful setting for this is

 setw -g aggressive-resize on

added to . It causes tmux to resize a window based on the smallest client actually viewing it, not on the smallest one attached to the entire session.

An alternative is to put the following :

{{hc|~/.bashrc|2=
function rsc() {
  CLIENTID=$1.`date +%S`
  tmux new-session -d -t $1 -s $CLIENTID \; set-option destroy-unattached \; attach-session -t $CLIENTID
}

function mksc() {
  tmux new-session -d -s $1
  rsc $1
}
}}

Citing the author:

: "mksc foo" creates a always detached permanent client named "foo". It also calls "rsc foo" to create a client to newly created session. "rsc foo" creates a new client grouped by "foo" name. It has destroy-unattached turned on so when I leave it, it kills client.
: Therefore, when my computer looses network connectivity, all "foo.something" clients are killed while "foo" remains. I can then call "rsc foo" to continue work from where I stopped.

## Correct the TERM variable according to terminal type
Instead of setting a fixed TERM variable in tmux, it is possible to set the proper TERM (either  or ) according to the type of your terminal emulator:

{{hc|~/.tmux.conf|
## set the default TERM
set -g default-terminal screen

## update the TERM variable of terminal emulator when creating a new session or attaching a existing session
set -g update-environment 'DISPLAY SSH_ASKPASS SSH_AGENT_PID SSH_CONNECTION WINDOWID XAUTHORITY TERM'
## determine if we should enable 256-colour support
if "| ${TERM} == fbterm " 'set -g default-terminal screen-256color'
}}

{{hc|1=~/.zshrc|2=
## workaround for handling TERM variable in multiple tmux sessions properly (by Nicholas Marriott)
if -n ${TMUX} && -n ${commands[tmux} ]];then
        case $(tmux showenv TERM 2>/dev/null) in
                *256color) ;&
                TERM=fbterm)
                        TERM=screen-256color ;;
                *)
                        TERM=screen
        esac
fi
}}

## Reload an updated configuration without restarting tmux
By default tmux reads  only if it was not already running. To have tmux load a configuration file afterwards, execute:

 tmux source-file path

This can be added to  as e.g.:

You can also input : and type:

 source .tmux.conf

## Template script to run program in new session or attach to existing one
This script checks for a program presumed to have been started by a previous run of itself. Unless found it creates a new tmux session and attaches to a window named after and running the program. If however the program was found it merely attaches to the session and selects the window.

 #!/bin/bash

 PID=$(pidof $1)

 if [ -z "$PID" ]; then
     tmux new-session -d -s main ;
     tmux new-window -t main -n $1 "$*" ;
 fi
     tmux attach-session -d -t main ;
     tmux select-window -t $1 ;
 exit 0

A derived version to run irssi with the nicklist plugin can be found on its ArchWiki page.

## Terminal emulator window titles
If you SSH into a host in a tmux window, you will notice the window title of your terminal emulator remains to be  rather than . To allow the title bar to adapt to whatever host you connect to, set the following in

 set -g set-titles on
 set -g set-titles-string "#T"

For ,  will display  and change accordingly as you connect to different hosts.

## Automatic layouting
When creating new splits or destroying older ones the currently selected layout is not applied. To fix that, add following binds which will apply the currently selected layout to new or remaining panes:

 bind-key -n M-c kill-pane \; select-layout
 bind-key -n M-n split-window \; select-layout

## Vim colorscheme not loading
See the following if your vim colorscheme is not loading in tmux: [https://github.com/vim/vim/issues/993#issuecomment-255651605

## Vim friendly configuration
See for a configuration friendly to vim users.

## Friendly pane splitting
The default key-binding for splitting a pane vertically is  and for splitting a pane horizontally is . That can be difficult to type depending of your keyboard layout and it is also hard to remember.

A more friendly key-binding is to use  for splitting horizontally and  for splitting a pane vertically, it is also very convenient to remember.

To make this change, add these lines in :

## Inhibit system suspension
If tmux hangs when connected from another device because the host goes to sleep, run session's shell command with an inhibition lock:

 tmux new-session -A "systemd-inhibit --what=idle $SHELL"

## Troubleshooting
## Scrolling issues
In case of trouble scrolling in the terminal with Shift-Page Up/Down, the following will disable the smcup and rmcup capabilities for any term that reports itself as anything beginning with :

 set -ga terminal-overrides ',xterm*:smcup@:rmcup@'

This tricks the terminal emulator into thinking tmux is a full screen application like pico or mutt[https://superuser.com/questions/310251/use-terminal-scrollbar-with-tmux, which will make the scrollback be recorded properly. Beware however, it will get a bit messed up when switching between windows/panes. Consider using tmux's native scrollback instead.

## Mouse scrolling
If you want to scroll with your mouse wheel, ensure mode-mouse is on in .tmux.conf
 set -g mouse on

You can set scroll History with:
 set -g history-limit 30000

For mouse wheel scrolling as from tmux 2.1 try adding one or both of these to ~/.tmux.conf
 bind -T root WheelUpPane   if-shell -F -t = "#{alternate_on}" "send-keys -M" "select-pane -t =; copy-mode -e; send-keys -M"
 bind -T root WheelDownPane if-shell -F -t = "#{alternate_on}" "send-keys -M" "select-pane -t =; send-keys -M"

Though the above will only scroll one line at a time, add this solution to scroll an entire page instead
 bind -t vi-copy    WheelUpPane   page-up
 bind -t vi-copy    WheelDownPane page-down
 bind -t emacs-copy WheelUpPane   page-up
 bind -t emacs-copy WheelDownPane page-down

## Terminal emulator does not support UTF-8 mouse events
When the terminal emulator does not support the UTF-8 mouse events and the  tmux option is set, left-clicking inside the terminal window might paste strings like  or  into the promt.

To solve this issue set:

 set -g mouse-utf8 off

## Shift+F6 not working in Midnight Commander
See Midnight Commander#Broken shortcuts.
