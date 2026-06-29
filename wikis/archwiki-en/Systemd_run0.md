# Systemd/run0

run0 is a privilege elevation tool introduced with systemd v256. It is implemented as an alternative invocation mode of  and is intended as a modern replacement for sudo, without relying on SUID binaries. It uses polkit for authentication.

## Installation
run0 is installed with systemd.

Install , as it is required to handle authorization.

## Usage
To use run0, simply prefix a command and its arguments with  and a space:

 $ run0 cmd

For example, to use pacman:

 $ run0 pacman -Syu

To launch an interactive shell (similar to ), just type .

With the  option, privileged commands are run as the current user, avoiding a full root context. This is useful to run a command with privileges but still have all created files and directories be owned by your current user.

Options for  also apply. See  and .
