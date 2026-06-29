# Icons

The freedesktop project provides the Icon Theme Specification, which applies to most linux desktop environments and tries to unify the look of a whole bunch of icons in an icon-theme.
Freedesktop also provides the Icon Naming Specification, which defines a standard naming scheme for icons believed to be installed on any system. The default theme hicolor should include them all.

## Installation
## Icon themes
## From a package
* Official repositories — "icon-theme" search.
* AUR — "icon-theme" search.

## Manually
If you cannot find a package for the icon theme you are looking for, you will need to install it manually.

* Firstly, find and download your desired icon pack. Many different icon themes can be downloaded from the following sites: Opendesktop.org and Xfce-look.org.
* Then navigate to the directory which contains the icon pack and extract it. Example .
* Move the extracted folder containing the icons.
**  (system-wide), or:
**  or  (user only).
* Optionally run  on the directory that you chose to update the icon cache.
* Select the icon theme using the appropriate configuration tool for your desktop environment or window manager.

## Customization
A system always has an active theme. For KDE it is called "breeze" and for Gnome "Adwaita", but if nothing is chosen by the system the spec says that "hicolor" is the theme. Themes can also have parent themes; for example, "breeze-dark" inherits from "breeze", which means any icons it doesn't define are searched in "breeze".

Icons are named by short strings, for "checkmark" or "weather-snow-large" or "org.gnome.Showtime" which is passed by an app to the system to load a particular icon. When looking up an icon, if the active theme doesn't have it, its parent(s) are searched, and if none are found then "hicolor" is searched, since it is the fallback of all themes. Also, as a special case, some icons are named '-symbolic'; if these are not found the '-symbolic' is removed and searched again.

Not all files in a theme's folder are part of the theme. An icon-theme is defined by an index.theme file; you can see examples at . Only sub-folders mentioned in that file count as part of the theme.

The subfolders are there to provide organization and, in the case of the numbered, different resolutions for different zoom levels, for example

but ultimately icons are in a flat namespace where the first match by name wins.

Confusingly, this means that looking up an icon has several places it could be, not all the same, but also many places cannot be and will silently be ignored if attempted. For example:

*
*

are both the icon 'text-x-generic-symbolic', even though one is under  in the "Adwaita" theme and the other is under  in the "hicolor" theme. But

*

will never be used by anyone, because  does not define  as part of itself.

## Icons and emblems
If you have deduced the name of an icon you would like to customize,  can be used. This will resize and copy the icon to . With this method, custom emblems can also be added. Examples:

 $ xdg-icon-resource install --size 128 --context emblems archuser-example.png # add as emblem
 $ xdg-icon-resource install --size 128 archuser-example.png # add as normal icon

This only  works for raster icons (.png and .xpm). For vector graphics (.svg), or just to understand better what is going on, the structure under  can be created manually. To replace an icon, search for it in ; most are in  since that is the fallback theme so it is also where apps tend to install their icons. Once you find the image you want to replace, suppose for example , create a local version, swapping  for . That is to say:

 $ mkdir -p ~/.local/share/icons/hicolor/scalable/actions/
 $ cp your-new-symbol.svg ~/.local/share/icons/hicolor/scalable/actions/xsi-edit-find-symbolic.svg

 If you only have one then it does not matter which folder it is in, and your  copy will take precedence so long as it is one of the folders mentioned by the theme's icon.theme file.

You may need to log out to apply the new icon each time you change it, depending on what apps use it.

File naming is extremely precise with icon themes and a mistake will generally not present with any feedback except for the icon not changing, so triple-check spelling if it is not working.

To debug what icon is being loaded currently on your system, at least when loaded via Gtk:

## Mime type icons
File managers do not rely on the traditional mime type which  outputs. Instead definitions from  are used. Calling an icon according to the definition found there and copying it to  will cause the file manager to display the custom mime type icon. This command illustrates the method to create a custom icon for the keepass database files (.kdb):

Rename your icon according to this output:

 $ xdg-icon-resource install --size 128 --context mimetypes application-x-keepass2.png

## Custom Themes
Finally, if you have created a lot of changes to your theme you might consider packaging it as its own theme. To do this, make a folder and add an index.theme to it that _inherits_ from the theme you are customizing; for example, to customize KDE's default dark theme:

Add icons to this, following the structure of the original theme as above.

You can put your theme under , and then it should be available to pick from your desktop environment's appearance settings, or zip it up and share it with other people!

## fstab / gvfs
According to this document file managers using GVFS (like GNOME Files or Thunar) can display icons for custom locations, like NFS shares. All you need are some extended mount options inside  with icon names supported by your selected icon theme:
