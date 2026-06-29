# Session lock

There are numerous utilities to lock the screen of a session. But it is important to note that the utility to use is highly dependent on the environment you are in, either the virtual console, or a specific display server (Xorg or Wayland).

See List of applications/Security#Screen lockers.

## By environment
## Virtual console
You can use  or  to lock a virtual console.

## Xorg
There are many ways to lock the session under Xorg, so this section is likely to be incomplete. Some methods however include:

* , in the  package -
* , in the  package
*  in the  package
*
* slock in the  package
*
*
*
*

Most desktop environments come with some way to lock the session.

## Wayland
You can lock the session with one of the following methods:

*
*
*
*
*

## Triggering the lock
You can lock a session using different methods:

* from a terminal
* using a GUI:
** from a desktop icon
** using hot corners
** from a menu (mouse or keyboard driven)
* from a shortcut
* from an event:
** inactivity (using systemd, xss-lock or xautolock)
** systemd events (suspend, hibernate, etc.)

The last point (triggering a lock from an event) is the trickiest, because you can do it in one of two ways:

* get the action trigger to execute your lock, then to execute the initial action.
* from the event trigger, add the lock to the event chain. So far this can only be done using systemd.

## Shell triggers
## Zsh
To execute a command after terminal inactivity, you can use the TMOUT environment variable.

You can combine it with a trap on the ALARM signal to execute the lock. Without a trap, it will just terminate the shell.

You might want to detect if you are in a graphical environment, otherwise your GUI terminals might start disappearing without you understanding why.

## Xorg triggers
## xss-lock
 is triggered by one of two things:

* systemd events
* DPMS

The advantage of this is that you can control a lock issued manually, by inactivity, and by a suspend command at the same place.

To execute an action on one of those events:

 $ xss-lock locker-utility

## systemd events
By default, xss-lock subscribes to , , , and  with appropriate actions (run locker and wait for user to unlock or kill locker).

You can prevent xss-lock from being triggered by  and  using .

You can trigger a manual lock using , or lock all current sessions with .

## DPMS
To configure DPMS signaling timeout:

 # Trigger screensaver after 10 minutes of inactivity
 xset s on
 xset s 600

DPMS signaling can also be configured in  in the  section.

Using DPMS signaling, you can set a second timer, for example to notify the user or to dim the screen. For example (from ):

 # Dim the screen after three minutes of inactivity, lock the screen two minutes later using i3lock:
 xset s 180 120
 xss-lock -n dim-screen.sh -- i3lock -n

An example  script can be found in .

## xautolock
Install the  package.

 $ xautolock -time 12 -locker "systemctl suspend" -detectsleep

## Wayland triggers
## swayidle
 listens for idle activity from the Wayland compositor, as well as systemd events, and executes commands accordingly. See Sway#Idle.

## hypridle
 Hyprland's idle daemon. See upstream for configuration.

## D-Bus notification
Using , or the  action in , you can notify the system through DBUS that you want to lock. This notification can then be processed, for example by xss-lock.

## Inactivity
In , you can configure the  to . This will trigger a DBUS notification, that will have to be processed (for example by xsslock) to lock the session.

Note that this is for a global system (so this is not ideal for a multi user environment).

Note also that "this requires that user sessions correctly report the idle status to the system".

## Units
## Before suspend or hibernate
You can use a Sleep hook.

To enable it for a certain user, enable .

## Lid closing
You can use the  action using the related ACPI event.
