# EXWM

EXWM is a window manager based on Emacs.

## Installation
Make sure you have  installed. You will also need .

Install EXWM from within Emacs: .

Edit xinitrc and add:

 exec emacs

In your emacs init file, add:

 (require 'exwm)
 (require 'exwm-config)
 (exwm-config-example)

to use the default settings. If you want to use your own settings, use  instead of  (and you do not need to ).

It is also possible to start emacs in server mode and to start EXWM from commandline. See
https://github.com/ch11ng/exwm/issues/284.

## Configuration
EXWM is a full X window manager, so Emacs manages X windows such as your browser, vlc, etc. You may use all the normal Emacs window commands to control window placement. In X windows (i.e. not "normal" Emacs buffers), some commands are caught by EXWM and not passed through to the program. These keys are store in . Alternatively, you can set global commands by customizing . If you would rather set  in elisp rather than using the customization feature, be aware that you may have to restart EXWM (and set  before enabling exwm). Alternatively, you could try using the  macro from the "or emacs" blog, which should work for redefining  without restarting EXWM. To use s-& as a keyboard shortcut to launch a program (e.g. firefox), you can do:

## Multi-monitor
EXWM can handle multi-monitor through the (optional)  package. You will need to install xrandr and enable exwm-randr in your emacs configuration file before calling . You will need to adjust the values of "DP-1" and "DP-2" to the values your computer uses; call  at the command line with no arguments to see available outputs.

## System tray
EXWM supports a system tray, but it is not enabled by default. To enable it, put the following before  in your dotemacs file:

You may need to adjust the height afterwards; this can be adjusted with the  variable.

## Embedding within LXDE
EXWM can be used in place of openbox, allowing you to still use LXDE session management tools.

Before doing this, make sure you have your init file for emacs already set up to run EXWM (see above)

lxsession uses the window manager defined in  (Openbox by default). If this file does not exist, it searches in  instead.

Replace  in either file with emacs:

 window_manager=emacs

## lxsession-logout
You can create the following function within emacs to log out, shutdown, or reboot cleanly from within a LXDE session:

 (defun exwm-logout ()
   (interactive)
   (recentf-save-list)
   (save-some-buffers)
   (start-process-shell-command "logout" nil "lxsession-logout"))

This stores your recentf history to disk, prompts you to save, discard, or diff changes within unsaved buffers, then launches the logout manager. You can bind this function to any key within emacs.

## Troubleshooting
## Screen tearing in Firefox
You may experience screen tearing in some programs, particularly Firefox. You can try:

* turning off smooth scrolling in Preferences > Advanced > Use Smooth Scrolling.
* installing (and activating) Compton or another composite manager: Xorg#Composite.

## Confusing Buffer Names
You may see the buffer names being named '*EXWM*'. This makes it confusing while switching between buffers .EXWM allows the buffers to name themself . To allow buffers to name themself put  the following in your dotemacs .
