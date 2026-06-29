# Allow a program to continue after logoff

The  package is built not to kill user process on log out by default. See systemd/User#Kill user processes on logout.

There are several ways to make a program continue after logoff:

* use the  GNU coreutil
* use the  Bash/Zsh shell builtin
* use a terminal multiplexer, also allowing you to reattach to your detached session.
* use /

## X applications
As xmove is dead, you probably want to use something else.

## Secondary X server
Create a script with this content, and make it executable.

Executing this little script will start a new X server. Then you can simply start your application and lock the server with  (you need the  package for using ).

Do not start your application in the first X server. If it is not already started, start the first and start a second one. Use the second one for your applications.

This is important because some features, like AGP mode, works only on one X server and other users of the computer will be annoyed if those feature will be lacking because you started a X server for your own purposes. So just use the second, the first will be full featured for everyone who need.

## xpra
Xpra allows you to start X programs and leave them running after disconnecting to reconnect again at a later time. It is possible to start X programs on a remote machine, connect to the machine over ssh, disconnect and reconnect again while the programs continue running.

## X2Go
X2Go supports suspending of sessions and reconnecting even from different client. While designed for remote access, it can be used even on localhost.
