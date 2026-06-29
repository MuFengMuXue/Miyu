## C.4 Backward Compatibility

For a limited time, installing a directory hierarchy to the old GNOME/KDE specific locations such as /usr/share/applnk and /usr/share/gnome/apps will continue to work as way to add your application to the menu system as well. There are two ways to support both the old and new menu systems at the same time:

- If you add a `Categories` line to the desktop entries in the legacy hierarchy, implementations of this specification will ignore their location in the legacy hierarchy, and arrange them according to `Categories` instead. This allows you to install a single desktop file that works in all cases, though on the down side it's in a legacy location.

- If you add the line `OnlyShowIn=Old;` to a desktop entry, then old legacy implementations that ignore `OnlyShowIn` will still show the desktop entry, but implementations of this specification will not. Thus you can add an "`OnlyShowIn=Old;`" entry to the legacy hierarchy, and a new-style desktop entry to *datadir*/applications/, and still get only one entry in the menus.
