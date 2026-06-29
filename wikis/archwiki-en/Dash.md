# Dash

Dash (Debian Almquist shell) is a modern POSIX-compliant implementation of  (sh, Bourne shell).

Dash is not Bash compatible, but Bash tries to be mostly compatible with POSIX, and thus Dash.

Dash shines in:
* Speed of execution. Roughly 4x times faster than Bash and others.
* Very limited resources (disk space, RAM or CPU). As minimalistic as possible - much smaller (134.1 kB vs 6.5 MB installed, 13 kSLOC vs 176 kSLOC) than Bash and others.
* Security. Dash is a long-established, tiny project with simple and long-established functionality; one that is still very much alive, and with many active developers. Thus, Dash has a much smaller attack surface, while still having many eyes on its code.
* If classic  needed only.

## Installation
Install  or .

## Use Dash as /bin/sh
Most POSIX compliant scripts specify  at the first line of the script, which means it will run  as the shell, which by default in Arch is a symlink to .

You can re-symlink  to , which can improve system performance, but first you must verify that none of the scripts that are not explicitly  require any of Bash's features and that all  scripts are safely POSIX compliant.

## Identifying bashisms
Features of bash that are not included in Dash ('bashisms') will not work without being explicitly pointed to . The following instructions will allow you to find any scripts that may need modification.

Install .

## Common places to check
* All scripts in PATH with a  shebang:
 $ IFS=:; grep -Irl '#!/bin/sh' $PATH |xargs -r checkbashisms

*  can be used to list all pacman-installed files.

## Relinking /bin/sh
Once you have verified that it will not break any functionality, it should be safe to relink . To do so use the following command:
 # ln -sfT dash /usr/bin/sh
Updates of Bash will overwrite  with the default symlink. To prevent this, use the following pacman hook, which will relink  after every affected update:

 Type = Package
 Operation = Install
 Operation = Upgrade
 Target = bash

 [Action
 Description = Re-pointing /bin/sh symlink to dash...
 When = PostTransaction
 Exec = /usr/bin/ln -sfT dash /usr/bin/sh
 Depends = dash

This is provided by .
