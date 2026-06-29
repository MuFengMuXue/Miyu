# Meld

## Description
Meld helps you compare files, directories, and version controlled projects. It provides two- and three-way comparison of both files and directories, and has support for many popular version control systems.

Meld helps you review code changes and understand patches. It might even help you to figure out what's going on in that merge you keep avoiding.

## Installation
## Arch
Install the  package for the stable version.

Or the  for the latest commit version.

## Flatpak
Also available as a Flatpak from Flathub.

You can install Meld with:

 $ flatpak install flathub org.gnome.Meld

To run the Flatpak version:

 $ flatpak run org.gnome.Meld

## Usage
Meld can be launched from the terminal or the application menu of your desktop environment.

You can interact with meld via terminal or GUI

## Usage example
Comparing two files via terminal
 $ meld file1.txt file2.txt

Comparing two files via GUI
 New comparison > File > Choose file1.txt and file2.txt > Compare

## Version Control Systems Integration
Meld integrates with many version control systems to let you review local changes and perform simple version control tasks.

## Git configuration
Meld can be set as the default difftool and mergetool for Git.

Run the following commands to configure Git to use Meld:

 git config --global diff.guitool meld
 git config --global merge.tool meld

Or edit your  manually:

## SVN
Is possible to use Meld with Subversion.

Use command:
 svn diff --diff-cmd meld nome_file

## File Managers Integration
## Nautilus
To add "Compare" options to the context menu in Nautilus, install the  package. Restart Nautilus for changes to take effect.

## Thunar
In Thunar, you can set up a custom action.
# Go to Edit > Configure custom actions.
# Add a new action.
# Command:
# Appearance conditions: Check "Directories" and "Text files".

## Tips and tricks
## Color Schemes
Meld supports syntax highlighting for a better visualization.

Specific color preferences can be changed inside Meld via the Preferences menu.

## Troubleshooting
## Missing Context Menu in Nautilus
If the context menu items do not appear after installing , ensure you have restarted the file manager completely:

 $ nautilus -q

Or try rebooting your machine.
