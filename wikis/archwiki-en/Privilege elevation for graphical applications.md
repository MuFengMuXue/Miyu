# Privilege elevation for graphical applications

This article provides methods for using graphical applications to perform privileged tasks such as mounting filesystems, partitioning drives, and editing system files. Running the entire graphical application as root should be avoided because:

* It could inadvertently modify file permissions in your home directory.
* Most of the graphical code has not been audited to run with higher permissions.

## Perform privileged actions in GUI applications
## Privilege elevation with polkit
polkit allows unprivileged GUI applications to perform certain prearranged actions that require special permissions. If the application comes with polkit support, and there is a functioning polkit agent, then you should automatically be prompted for credentials when necessary.

To find applications on your system that support polkit, you can start by seeing what packages require it in . Additionally, each supporting application installs one or more policy into . Some polkit programs are user-facing applications such as , whereas others are shared utilities used by other applications. As an example, many file managers use  or  to mount filesystems upon request.

## File editing
These are application-agnostic methods for editing files not normally accessible and/or writable.

## sudoedit
For one-off edits to system files, sudoedit can be used to edit a temporary unprivileged copy in your editor.

## GVFS
Access to privileged files and directories is possible through GVFS by specifying the  backend in the URI schemee.g.:

 $ nautilus admin:///root/

or

 $ gedit admin:///etc/fstab

## kio-admin
[https://invent.kde.org/system/kio-admin KIO Admin Worker provides an  URI within supported KIO applications such as Dolphin, allowing privileged file operations.

Install  to gain support for this functionality.

## Run GUI applications as root
## Xorg
By default, and for security reasons, root will be unable to connect to a non-root user's X server. There are multiple ways of allowing root to do so however, if necessary.

## Polkit
The proper, recommended way to run GUI applications under X with elevated privileges is to create a Polkit policy, as shown in this forum post.

This should however "only be used for legacy programs", as  reminds. Applications should rather "defer the privileged operations to an auditable, self-contained, minimal piece of code that gets executed after doing a privilege escalation, and gets dropped when not needed"This may be the object of a bug report to the upstream project.

## Punctual methods
These methods wrap the application in an elevation framework and drop the acquired privileges once it exits:

*  (from )
 $ kdesu application

* sudo (must be properly configured)
 $ sudo application

*  (wrapper around su which will transfer your X credentials)
 $ sux root application

## Alternate methods
These methods will allow root to connect to a non-root user's X server, but present varying levels of security risks, especially if you run ssh. If you are behind a firewall, you may consider them to be safe enough for your requirements.

## Xhost
Xhost can be used to temporarily allow root access.

## Permanently allow root access
:Method 1: Add the line

 session         optional        pam_xauth.so

to both  and . Then switch to your root user using  or .

:Method 2: Globally in

Add the following line to :

This will permanently allow root to connect to a non-root user's X server.

Or, merely specify a particular app:

 # XAUTHORITY=/home/username/.Xauthority appname

where  is the name of the particular app. (e.g. kwrite)

## Wayland
Trying to run a graphical application as root via su, sudo or pkexec in a Wayland session (e.g. GParted or Gedit), will fail with an error similar to this:

## Wayland applications
This section pertains only to native Wayland applications which are not running under XWayland.

## Using sudo -E
You can launch an application with:

 $ sudo -E program

which preserves environment variables like WAYLAND_DISPLAY.

If you want the HOME environment variable to be set to the target user, use:

 $ sudo -EH program

See .

## Using pkexec
You can launch a GUI application with:

 $ pkexec env WAYLAND_DISPLAY="$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY" XDG_RUNTIME_DIR=/run/user/0 program

This preserves the WAYLAND_DISPLAY environment variable.

## XWayland
Under XWayland, Xorg workarounds do not work anymore as the default has been made to only allow the user who started the X server to connect clients to it (see the [https://bugzilla.redhat.com/show_bug.cgi?id=1266771 bug report and the upstream commits it refers to).

One workaround is to use xhost to temporarily allow the root user to access the local user's X sessionhttps://bugzilla.redhat.com/show_bug.cgi?id=1274451#c64. To do so, execute the following command as the current (unprivileged) user:

 $ xhost si:localuser:root

To remove this access after the application has been closed:

 $ xhost -si:localuser:root
