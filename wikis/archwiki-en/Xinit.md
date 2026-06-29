# Xinit

From Wikipedia:
:The xinit program allows a user to manually start an Xorg display server. The  script is a front-end for .

xinit is typically used to start window managers or desktop environments. While you can also use xinit to run GUI applications without a window manager, many graphical applications expect an EWMH compliant window manager. Display managers start Xorg for you and generally source xprofile.

## Installation
Install the  package.

## Configuration
xinit and startx take an optional client program argument, see #Override xinitrc.  If you do not provide one they will look for  to run as a shell script to start up client programs.

## xinitrc
 is handy to run programs depending on X and set environment variables on X server startup. If it is present in a user's home directory, startx and xinit execute it. Otherwise startx will run the default .

This default xinitrc will start a basic environment with Twm,  and Xterm (assuming that the necessary packages are installed). Therefore, to start a different window manager or desktop environment, first create a copy of the default  in your home directory:

 $ cp /etc/X11/xinit/xinitrc ~/.xinitrc

Then edit the file and replace the default programs with desired commands. Remember that lines following a command using  would be ignored. For example, to start  in the background and then start openbox, use the following:

Long-running programs started before the window manager, such as a screensaver and wallpaper application, must either fork themselves or be run in the background by appending an  sign. Otherwise, the script would halt and wait for each program to exit before executing the window manager or desktop environment. Note that some programs should instead not be forked, to avoid race bugs, as is the case of xrdb. Prepending  will replace the script process with the window manager process, so that X does not exit even if this process forks to the background.

## xserverrc
The  file is a shell script responsible for starting up the X server. Both startx and xinit execute  if it exists, startx will use  otherwise.

See  for a list of all command line options.

## Passing virtual terminal number
In order to maintain an authenticated session with logind and to prevent bypassing the screen locker by switching terminals, Xorg has to be started on the same virtual terminal where the login occurred For this purpose, Xorg needs to be passed the number of the current virtual terminal.

If you are invoking startx, nothing more needs to be done – it [https://gitlab.freedesktop.org/xorg/app/xinit/-/commit/44915d6953076849b69a017f6fc8234b0f254362 contains logic to compute and pass the virtual terminal number to Xorg.

In other cases, e.g. if you are running xinit, it is recommended to specify  in the  file:

## Usage
To run Xorg as a regular user, issue:

 $ startx

Or if #xserverrc is configured:

 $ xinit -- :1

Your window manager (or desktop environment) of choice should now start correctly.

To quit X, run your window manager's exit function (assuming it has one). If it lacks such functionality, run:

 $ pkill -15 Xorg

See also .

## Tips and tricks
## Override xinitrc
If you have a working  but just want to try other window manager or desktop environment, you can run it by issuing startx followed by the path to the window manager, for example:

 $ startx /usr/bin/i3

If the binary takes arguments, they need to be quoted to be recognized as part of the first parameter of startx:

 $ startx "/usr/bin/application --key value"

Note that the full path is required. You can also specify custom options for the #xserverrc script by appending them after the double dash  sign:

 $ startx /usr/bin/enlightenment -- -br +bs -dpi 96

See also .

## Autostart X at login
Make sure that startx is properly configured.

Place the following in your login shell initialization file (e.g.  for Bash or  for Zsh):

You can replace the  comparison with one like  (for vt1 to vt3) if you want to use graphical logins on more than one virtual terminal.

Alternative conditions to detect the virtual terminal include , which does not allow comparison with , and , which does not work in serial consoles.

The  command ensures that the user is logged out when the X server exits, crashes or is killed by an attacker. If you want to take the risk and remain logged in when the X session ends, remove .

See also fish#Start X at login.

## Switching between desktop environments/window managers
If you are frequently switching between different desktop environments or window managers, it is convenient to either use a display manager or expand  to make the switching possible.

The following example shows how to start a particular desktop environment or window manager with an argument:

{{hc|~/.xinitrc|
...

# Here Xfce is kept as default
session=${1:-xfce}

case $session in
    i3|i3wm           ) exec i3;;
    kde               ) exec startplasma-x11;;
    xfce|xfce4        ) exec startxfce4;;
    # No known session, try to run it as command
    *                 ) exec $1;;
esac
}}

To pass the argument session:

 $ xinit session

or

 $ startx ~/.xinitrc session

## Starting applications without a window manager
It is possible to start only specific applications without a window manager, although most likely this is only useful with a single application shown in full-screen mode. For example:

Alternatively the binary can be called directly from the command prompt as described in #Override xinitrc.

With this method you need to set each application's window geometry through its own configuration files (if possible at all).

See also Display manager#Starting applications without a window manager.

## Output redirection using startx
See Xorg#Session log redirection for details.

## Running in a virtual server
Useful for running graphical applications:

* Without showing their GUI.
* On testcases.
* Within a system that does not have xorg-server running.
* While building in a clean chroot.

Install , then run .
