# Twm

twm (initially for Tom's Window Manager and now Tab Window Manager) is a window manager for Xorg. It is a small program, being built against Xlib rather than using a widget library, and as such, it is very light on system resources. Though simple, it is highly configurable; fonts, colours, border widths, title bar buttons, etc. can all be set by the user.

twm was written by Tom LaStrange, a developer who was frustrated by the limitations of uwm (Ultrix Window Manager), the only window manager around when X11 was first released: twm supplanted uwm as the default window manager supplied with X11 from the X11R4 release in 1989. == Installation ==

twm is installed through the  package.

## Starting
Run  with xinit.

You can also start twm with a display manager. The  file does not exist so we have to create it at .
In the newly created  file, copy and paste:

## Configuration
By default, twm looks very dated and unintuitive. By creating the file , you can customize twm to make it more friendly.

 gives full details of the commands which can be used in your  file.

## .twmrc examples
Many  files have been posted online. Some examples include:

* [https://web.archive.org/web/20080926032120/http://physics.wm.edu/unix_intro/loginmht/twmrc.html Sample .twmrc file (Physics Department Unix Login Mini-Howto, W&M University through Wayback Machine)
* sample twmrc files (Apple Open Source/X11/X11-0.46.4)
* system.twmrc (Apple Open Source/X11/X11-0.46.4)
* twm configs - 1 (custompc.plus.com)
* twm configs - 2 (custompc.plus.com)

A Google search for "twmrc" can also be used to find new ideas.

## Tips and tricks
## Patched version
There is a patched version, not in the repositories, with updated features such as transparency. A description and build script is available on the xorg mailing list. It can be tried out by installing xcompmgr, running the build script, putting the resulting  and  files in a convenient directory, and editing the  file so that the last two lines are
 xcompmgr -o 0.3  -c -r 8 -t -10 -l -12 &
 /path-to-directory/twm -visual TrueColor -depth 32 -f /path-to-directory/dot.twmrc

## Troubleshooting
## Oversized window titles and menus
You might find that titlebars and menu entries in TWM are extremely large - twice the size that one might typically expect. This is a locale issue with TWM that occurs when a  locale is used. Setting the locale to  fixes the issue. See == See also ==

* [https://www.cpcnw.co.uk/twm/twmrc.htm Graham's TWM Page!
* Graham's TWM Page 2
* TWM -- Revised Edition -- Again
*  man page
* twm official Gitlab
* twm on Wikipedia
* X Window System User's Guide - Ch. 3 Using the twm Window Manager
* X Window System User's Guide - Ch. 10 Customizing the twm Window Manager
