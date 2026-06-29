# Dtach

From its website, dtach is a tiny program that emulates the detach feature of screen, allowing you to run a program in an environment that is protected from the controlling terminal and attach to it later.

## Installation
Install the  package.

## Usage
## Create a new session
To create a new session running command and attach to it:

 $ dtach -c socket command

For example, to create a new session running bash with the socket located at :

 $ dtach -c /tmp/bashsession bash

To create a new session running command without attaching to it:

 $ dtach -n socket command

## Attach to a session
To attach to an existing session:

 $ dtach -a socket

To attach to an existing session, and if not already existing, create it:

 $ dtach -A socket

## Detach from a session
In an attached session, type . This key combination can be modified with the  flag.

## Tips and tricks
## Share a session
To share a session with another user, simply #Create a new session and change the permissions on the socket file such that the other user can read and write to it. Then the other user should be able to attach to the session.
