# Ripcord

Ripcord is a lightweight desktop chat client for group-centric services like Slack and Discord built upon the Qt toolkit. It is proprietary, closed-source software released under a shareware license which allows the Discord module to be used free of charge while locking Slack usage behind purchase.

## Installation
Install the  package.

## Emoji glitch
There is a bug with some emoji fonts (known: , , ) which generates rendering glitches, currently not fixed.

Emoji fonts known to behave well include  and , so it is recommended to use one of them. Otherwise, the Experimental tab of the Preferences window offers an option to override the system font for Ripcord only.

Some users have reported that using system libraries solves the issue.

For further updates and information, see the relevant ticket on the issue tracker.

## Using system libraries
The Ripcord AppImage bundles its own copy of required libraries, which are also used by the AUR package. It is however possible to force the program to load libraries preexisting in the system. The main advantage of this is better integration with the desktop environment and Arch as a whole. The main disadvantage is that system libraries might be incompatible with the Ripcord release in use.

Otherwise, you may proceed as follows:
* Install packages , , , ,  and  (more may be necessary, if you find so please amend this list).
* Reach directory  or, if you would rather not touch managed files, download the AppImage, run it with  and cd to .
* Wipe or better move to a backup location the contents of the  folder you find there, leaving the folder itself intact.
* Run .
* Delete or move to a backup location the whole  folder.
* Set environment variable .

Finally, run the executable.

## IME
If you need to use an input method framework, IBus is known to behave well out of the box, while Fcitx seems to require following the steps in using system libraries.
