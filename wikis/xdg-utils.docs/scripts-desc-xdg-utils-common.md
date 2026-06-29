# Scripts / Desc / Xdg Utils Common

xdg-utils Common Manual


			 2024-04-27


			 Slatian

				 baschdel+xdg-utils@disroot.org


		 xdg-utils 1.2


		 xdg-utils-common
		 7


xdg-utils-common


Shared functionality of the xdg-utils scripts.


Description


			The xdg-utils package is a set of scripts that provide basic desktop integration functions for any Free Desktop on Linux, the BSDs and even partially on MacOS and WSL.


			Available xdg-utils are:


					 xdg-desktop-icon
					 1


					 xdg-desktop-menu
					 1


					 xdg-email
					 1


					 xdg-icon-resource
					 1


					 xdg-mime
					 1


					 xdg-open
					 1


					 xdg-realpath
					 1


					 xdg-screensaver
					 1


					 xdg-settings
					 1


			This manual describes mechanisms that are shared across all or multiple of the xdg-utils.


Exit Codes


All xdg-utils share a common set of exit codes.


0


Success.


1


CLI Syntax error, malformed or missing arguments/options.


2


A file specified on the CLI is missing.


3


An external tool needed to carry out the operation was not found.


4


An external tool used by the xdg-utils failed.


5


Permission problem: A file specified on the CLI couldn't be read.


6


Permission problem: A file specified on the CLI couldn't be written.


For debugging have a look at the environment variables and the tool specific manual.


Exit codes not documented here or in a tool specific manual can be considered bugs.


Mechanisms


This chapter will explain different mechanisms under the hood of the xdg-utils.


Desktop Environment Detection (detectDE)


The xdg-utils often try to delegate tasks to desktop specific tools to make things work, be consistent with the desktops native applications and a slight performance gain over the shell scripts.


To achieve this, they try to figure out which environment they are in by evaluating  XDG_CURRENT_DESKTOP , the output of  uname  and the existence of specific files.


Currently recognized desktop environments are:


 cinnamon


 dde  (Deepin)


 enlightenment


 gnome3


 kde


 lxde


 lxqt


 mate


 xfce


Recognized environments that aren't directly related to a desktop are:


 cygwin


 wsl


 darwin


 flatpak


  toolbx


 generic


Realpath


Turning a relative path into an absolute one in a shellscript seems simple. Until one realizes that the safe way to call gnu realpath is not compatible with busybox realpath and sometimes  readlink -f  is the appropriate tool.


While this mechanism is used by most xdg-utils it is documented in   xdg-realpath  1  .


Environment


These environment variables work across all xdg-utils and are mostly intended for debugging purposes. If you have to set these to work around a problem please file a bug report.


 XDG_UTILS_DEBUG_LEVEL


Integer in the range 1 to 4 to make the xdg-utils output an increasing amount of debug information.


 XDG_UTILS_INSTALL_MODE


For tools that install something this can be set to either  user  or  system .


See   xdg-desktop-icon  1  ,   xdg-icon-resource  1   and   xdg-desktop-menu  1  .


 XDG_UTILS_REALPATH_BACKEND


Which tool the xdg-utils will use to convert relative paths to absolute ones. Documented in   xdg-realpath  1  .


 XDG_CURRENT_DESKTOP


Used for identifying desktop is currently in use. See the  Desktop Entry Specification  for more details.


 XDG_UTILS_OVERRIDE_DE


 XDG_UTILS_ _OVERRIDE_DE


Can be used in tesing and development context to override the output of the Desktop Environment Detection for all xdg-utils or for only a specific tool. See the Desktop Environment Detection section for a list of available values.


To target a specific tool replace     with the upper-cased name of the tools command without the  xdg-  prefix. For
xdg-open
 one would set the variable  XDG_UTILS_OPEN_OVERRIDE_DE .


It is very easy to break the xdg-utils using this feature!


If you are using it outside of testing and development you are probably working around a bug. Please report this as an issue to the developers.


Reporting Issues


The xdg-utils combine multiple other tools that have had bug in the past, before reporting a bug please check if the bug is caused by a tool used in the xdg-utils. (When unsure please report it anyway) The tool specific manuals may contain hints on how to find out.


In case an issue specific to xdg-utils please report it to  https://gitlab.freedesktop.org/xdg/xdg-utils/-/issues  .


Please help the developers with information on how to reproduce the issue, it will increase the chance of a timely fix.


Have a patch? Great, but please don't forget to include information on what behavior you are trying to fix. The xdg-utils have a bad habit of disguising one problem as a different one.
