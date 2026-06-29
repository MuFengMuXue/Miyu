# Konsole

Konsole is a terminal emulator for the KDE desktop.

## Installation
Install the  package.

## Troubleshooting
## True-color programs do not display correctly
This is because by default, konsole does not set the right  variable. To set it, either edit your konsole profile or make a new one:

## Characters are not aligned / Characters change position when cursor moves
This is caused by the "Word mode" setting in Complex Text Layout. In the word mode, text are aligned at word-level, so individual characters might not be aligned. You can disable word mode to make sure characters are aligned.

You may want to disable word mode for ASCII characters only but enable it for Brahmic scripts characters so that Brahmic words can be connected correctly. However, in this case, the issue may persist for these characters, i.e. the characters may change position when cursor moves.

## Unable to edit bookmarks
Install the  package.
