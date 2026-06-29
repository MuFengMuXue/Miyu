# Zim

From Wikipedia, ZIM is an open file format that stores wiki content for offline usage. It is also the name of a graphical text editor used to edit this format.

## Installation
* : GUI editor
* : latest developer git version.
* Kiwix: offline ZIM viewer designed primarily for reading Wikis installed via . The project includes mobile versions and an online library of free ZIM files.
* Web archives
* : designed for dictionary use.

Console-based:
*
* : CLI reading by server requests instead of downloading the whole ZIM database.

## Usage
Zim can be used to:
* Keep an archive of notes
* Take notes during meetings or lectures
* Organize task lists
* Draft blog entries and emails
* Do brainstorming

This screencast provides an overview about the basic functionality.

## Configuration
Zim uses the XDG base directories.

Besides the configuration there exist the wiki directories which are set up when a new wikis are created. Those folders store all wiki pages in plain txt format.

## Tips
Specific user tricks to accomplish tasks.

## Plugins
Zim provides a lot of useful plugins where many of them are not enabled by default. They can be found at Edit > Preferences > Plugins. That is, there is a plugin which provides a tray icon.

## Spell checker
The requirements for the Spell Checker plugin are as follows:  and .

Change  to your desired language support. Now you can configure the Spell Checker and define the default language, like .  If you do not want Zim to spell-check based on your system default language, go to File > Properties > Spell Checker and enter a language code such as  or .

## Source View
The requirements for Source View are as follows:

## Troubleshooting
## Problems at launch
A common error is at start up resulting in a error message like the following this thread:

 UnboundLocalError: local variable 'i' referenced before assignment

It is often related to a problem with the file path of the wikis stored in . Try to delete or move this file and restart Zim.

## Error: Unable to find or create trash directory
This error message indicates that Zim is not able to find the trash directory as in this thread. This occurs when the wiki is stored on a partition that does not have any trash directory under . Due to that one is not able to delete pages as Zim tries to move them to the trash. Solutions are either the creation of a trash directory or the installation of the developer snapshot instead of the stable version which permanently deletes a page if no trash directory can be found. Thus, the user does not receive this error message anymore.
