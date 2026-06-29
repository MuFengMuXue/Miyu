# Greenclip

Greenclip is a simple clipboard manager designed to be integrated with rofi and written in Haskell.

## Installation
Install the  package.

## Usage
Spawn the daemon with  or start/enable .

Show entries as a list within rofi using: {{ic|rofi -modi "clipboard:greenclip print" -show clipboard -run-command '{cmd}'}}.

The entry that you have selected will be in your clipboard now.

Configuration file is placed in .

To clear all clipboard history, run .

## Troubleshooting
## Unable to record clipboard on i3wm
Put the following in the i3 configuration file. No need to start the service.
greenclip issue #70
