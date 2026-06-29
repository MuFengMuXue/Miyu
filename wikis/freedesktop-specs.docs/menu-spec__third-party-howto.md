## C Integrating your application in the menus

## C.1 Adding menu items

The following steps describe how a third party application can add menu items to the menu system:

- Install desktop entries to *datadir*/applications/ for each menu item. Please namespace the filename, as in "vendor-foo.desktop", or use a subdirectory of *datadir*/applications/ so you have "vendor/foo.desktop." Please be sure all desktop entries are valid (see the [desktop-file-utils (http://www.freedesktop.org/software/desktop-file-utils/)](http://www.freedesktop.org/software/desktop-file-utils/) package for a validation utility).

- Install an XML menu file to *sysconfdir*/menus/applications-merged/ to add any submenus, if your desktop entries aren't already included in some common categories.

- Install any directory entries needed for your submenus to *datadir*/desktop-directories/, taking care to namespace and validate the directory entries.
