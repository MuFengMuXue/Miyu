# Pkgfile

pkgfile is a tool for searching files from packages in the official repositories.

## Installation
Install the  package.

The pkgfile database can then be synced with:

 # pkgfile -u

## Usage
To search for a package that owns the file :

To list all files provided by :

Latter is comparable to  (see pacman#Querying package databases), except it applies to remote packages.

## Command not found
See Bash#Command not found, Zsh#pkgfile "command not found" handler and Fish#The "command not found" hook.

## Automatic updates
pkgfile ships with a systemd service and timer for automatically synchronizing the pkgfile database. To activate automatic updates enable .

By default, pkgfile will be updated daily. To change this schedule, edit the unit file.
