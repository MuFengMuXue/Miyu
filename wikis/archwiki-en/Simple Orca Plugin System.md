# Simple Orca Plugin System

With the Simple Orca Plugin System (SOPS) you can extend the functionality of the Orca screen reader ().
It offers the possibility to add plug-ins in nearly any programming language in an easy way.
The settings for the plug-ins are controlled via the filename.

## Installation
Install the package .

To setup the plug-in system for the current user, run:

 $ /usr/share/SOPS/install-for-current-user.sh

## Administration
## Basics
* The Installation path. This contains the default plug-ins, the documentation,the plugin loader and the administration tools:
:
* The path for user plug-ins is:
:
* The following path is used for all enabled (active) plug-ins. All plug-ins in that folder will be loaded, if they are valid:
:

## Administration tools
The tools are located in the "tools" folder beneath the installation directory. The following command enables/activates a plug-in, but you have to rename the filename to create a shortcut and pass a command to the plug-in:

 $ ./ensop

The command to disable and unload a plug-in is:

 $ ./dissop

Both commands basically just create or delete links in  and make the plug-ins executable. You have to configure the plug-ins manually.
Restart Orca to reload the plug-ins after changes.
SOPS also provides a plug-in manager, it is available after the installation.
To open the plug-in manager use  while Orca is running.
It can be used to activate, deactivate, install or configure plug-ins.
Orca gets re-started automatically after closing the plug-in manager.

## Plug-ins
## Structure of the filename
The shortcut, plug-in type and preference of a plug-in are controlled by its filename.
The descriptive part of the filename has to be separated from the preferences part with .
The commands, modifier and the key has to be separated by .
 __-____+__command...][__+____+____+__key_.ext

## Run a plug-in
There are two different ways to run a plug-in:

* shortcut (See #Modifiers/ Shortcuts)
* exec run once when the plug-in loads. (See #Commands/ Preferences)

If none of those are present. the plug-in does not load.
There are some more #Commands/ Preferences to control the behaviour of a plug-in.

## Modifiers/ Shortcuts
With modifiers you can set different shortcut combinations for a .
You always have to press the Orca-modifier.
The order of the three modifier keys does not matter:
*  is the modifier for the  key on the keyboard
*  is the modifier for the  key on the keyboard
*  is the modifier for the  key on the keyboard
*  defines the basic shortcut that is used for the plug-in, maybe together with the defined modifiers (example_plugin__-__key_d.sh uses ).

## Valid shortcuts
Only a few combinations of modifiers are valid. Those are predefined by Orca.
Valid combinations are:
*  i.e.
*  i.e.
*  i.e.
*  i.e.
*  i.e.
As  you can use every alphanumerical key.

## Commands/ Preferences
Preferences for plug-ins are called commands. A command defines the action to pass to the plug-in.
With commands you control the behaviour of the plug-ins. You may add more than one command. The order of the commands does not matter.
You can use them mostly for all kinds of plug-ins.
*  announces "start " before the plug-in is executed. It is useful as feedback for plug-ins with longer progress times. (all plug-ins)
*  announces "finish ". This is useful as feedback for plug-ins with no output. (all plugins)
*  do not start the plug-in in a thread. Be careful, as this locks Orca until the plug-in is finished. By default, plug-ins each run in a dedicated thread. (all plug-ins)
*  announces returned errors. (all plug-ins)
*  ignores the output of STDOUT. This is useful for plugins that may have a UI and do not pass output to STDOUT. (sub process plug-in only)
*  passes the parameters to the plug-in. (sub process plug-in only)
*  run the plug-in once while loading it. Mostly useful as advanced-plug-in. (all plug-ins)
*  does not load as a sub process plug-in but loads it as advanced plug-in. (advanced plug-in only)

## Examples
*  Run with  and announce the start of the process.
*  Run with  and announce the finishing. Does also read occurring errors .
*  Run with
*  Run once at starting Orca.

## Types of plug-ins
Basically there are two different types of plugins.

## Sub process plug-ins
Sub process plug-ins are simple plug-ins and the default type.
They may be any type of application or script that writes to STDOUT or STDERR.
Orca executes the plug-in, reads from STDOUT/ STDERR and announces the result to the user, when the defined shortcut is pressed or the plug-in is executed via  while starting screen reader.

## Requirements
* Execution permission
*  or  have to be defined in the filename.

## Example
Say "Hello World when pressing :
Filename:

## Advanced plug-ins
Those type of plug-ins are loaded with the spec.loader.exec_module. you can load them by using  in the filename. They are fully included into Orca as soon as it starts.
Advanced plug-ins are more powerful, because you are able to work in the Orca context. They are mostly similar to the .

## Requirements
* Correct code written in python3
* Fileextension
* Use  in the filename
*  or  have to been defined in filename

## Example
Configure Orca to speak/braille the word "bang" instead of the "!" while loading the plug-in.
Filename:

## Plug-in hosting
You can also host plug-ins, making them available for installation via the plug-in manager.
If you want to Host plug-ins, read:

The default online resource is:
https://stormdragon.tk/orca-plugins/index.php
