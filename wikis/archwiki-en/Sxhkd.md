# Sxhkd

sxhkd is a simple X hotkey daemon, by the developer of bspwm, that reacts to input events by executing commands.

## Installation
Install  or .

## Configuration
sxhkd defaults to  for its configuration file. An alternate configuration file can be specified with the  option.

Each line of the configuration file is interpreted as so:

* If it starts with , it is ignored.
* If it starts with one or more white space commands, it is read as a command.
* Otherwise, it is parsed as a hotkey: each key name is separated by spaces and/or  characters.

General syntax:

 + *COMMAND

Where  is one of the following names: , , , , , , , , , , , , , . If  is added at the beginning of the keysym, the command will be run on key release events, otherwise on key press events. The  names are those you will get from .

Mouse hotkeys can be defined by using one of the following special keysym names: , , , ..., . The hotkey can contain a sequence of the form , ...,}, in which case, the command must also contain a sequence with N elements: the pairing of the two sequences generates N hotkeys. If the command includes curly braces ({{ic|{}}, }) eg. {{ic|awk '{print $1}'}}, escape them with backslash  eg. {{ic|awk '\{print $1\}'}}. In addition, the sequences can contain ranges of the form  where A and Z are alphanumeric characters.

What is actually executed is , which means you can use environment variables in .  will be the content of the first defined environment variable in the following list: , . If sxhkd receives a  signal, it will reload its configuration file.

## Example
## Bind a command to a single press of a key
Some users may wish to bind a command to a single keypress, in the way that the  key opens the Start menu on Windows. In sxhkd, this is accomplished by binding to a chord chain composed of the key press and key release event of a single keysym, as in the following:

This complicated pattern is necessary because without the explicit chord chain (i.e. a single , sxhkd would trigger the binding on any release of the key—even when the key is used in another chord. Furthermore, keysyms must be used instead of modifiers ( as opposed to ) because sxhkd does not support the use of the  symbol (denoting key release) for modifiers.

## Usage
After configuring it, you may wish to set up sxhkd to autostart; see the corresponding article for your desktop environment or window manager for details.

If your desktop environment supports the [https://specifications.freedesktop.org/autostart-spec/latest/ Desktop Application Autostart Specification you can start sxhkd by creating an  file in the appropiate directory:
