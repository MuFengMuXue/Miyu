* Sway is a [Wayland](https://wayland.freedesktop.org/) compositor (duh)
* Sway handles things like output configuration (rather than something like xrandr)
* Sway supports multiple non-modifier keys when assigning key bindings (see [Shortcut handling](Shortcut-handling))
* The default keybindings in sway are different from those in i3. Read your sway config to learn them, or copy over your i3 config to use what you're used to.
* Sway handles your wallpaper
* Sway handles input configuration (man sway-input)
* Sway is documented through man pages, rather than the website
* A few i3 commands only make sense on X11 and aren't present in sway
* You may occasionally run into minor inconsistencies between sway syntax and i3 syntax. Just tweak your commands to be a bit more explicit if necessary
* i3lock forks into the background when run. For swaylock, this behavior has to be explicitly requested via `-f`
* i3 has support to export a layout and to restore it (or parts of it), sway only has export, no import.
* More stuff, some which are listed in [this](https://www.reddit.com/r/swaywm/comments/ciw865/random_differences_from_i3_ive_noted_any_tips/) reddit post.

Not a difference anymore:
* ~~You can use your `floating_modifier` to resize and move tiled windows~~ (since [v4.24](https://i3wm.org/downloads/RELEASE-NOTES-4.24.txt))
