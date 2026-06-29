# Dmenu

dmenu is a fast and lightweight dynamic menu for X. It reads arbitrary text from stdin, and creates a menu with one item for each line. The user can then select an item, through the arrow keys or typing a part of the name, and the line is printed to stdout. dmenu_run is a wrapper that ships with the dmenu distribution that allows its use as an application launcher.

## Installation
Install the  package.

Various patched variants exist which extend dmenu's default functionality.

You may run dmenu with:

 $ dmenu_run

## Configuration
Now, you will want to attach the  command to a keystroke combination. This can be done either via your window manager or desktop environment configuration, or with a program like . See the Hotkeys article for more information.

## Displaying custom items
Custom items will be shown by separating them with a new line (\n) and piping them into dmenu. For example:

 $ echo -e "first\nsecond\nthird" | dmenu

## Manually adding items
dmenu will look for executables in the directories defined in your . For information on modifying your  see environment variables.

## Fonts
dmenu can display fonts using XFT. This example will run dmenu using :

 $ dmenu_run -fn 'Droid Sans Mono-9'

## Support for shell aliases
dmenu does not support shell aliases. To have dmenu recognize your aliases, install the  package and run . Your aliases must be in  to be recognized by dmenu-recent-aliases.

## Support for history
To sort commands by recency, download dmenu_run_history to your  and use  instead of .

## Tips and tricks
## Taking input using dmenu
Inside a script (e.g. launched from a shortcut), getting user input is sometimes required. We can use dmenu for this, by passing it an EOF: the selection field will be empty and dmenu can take user input.

Since reading  will return an EOF, this can simply be done by the following command:

 $ dmenu < /dev/null

## Embedding in current terminal
Dmenu can be embeded inside any window using the  option.

To embed it inside the currenctly active window (like for example the terminal it is being run from), use  to get its id:

 $ echo hello | dmenu -w $(xdo id)

## Troubleshooting
## No locale support
Running dmenu_run results in the following error message:

Make sure that the environment variable  is correctly set. See the following for more information: Locale#Troubleshooting

## Missing menu entries
If certain entries are missing from dmenu, the cache may be malformed. Delete it and restart dmenu.

 $ rm ~/.dmenu_cache
 $ rm ~/.cache/dmenu_run

Note that there will most likely be only one cache file, depending on if  is set. See the contents of  for more information.

## Environment variables
Environment variables needed for applications should instead be added to .
