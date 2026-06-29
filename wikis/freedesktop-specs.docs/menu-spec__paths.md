## 2 File locations

Files involved in this specification are located according to the ["desktop base directory specification" (http://www.freedesktop.org/Standards/basedir-spec)](http://www.freedesktop.org/Standards/basedir-spec).

Here are the files defined by this specification:

`$XDG_CONFIG_DIRS`/menus/`${XDG_MENU_PREFIX}`applications.menu  
This file contains the XML definition of the main application menu layout. The first file found in the search path should be used; other files are ignored. This implies that if the user has their own `${XDG_MENU_PREFIX}`applications.menu, it replaces the system wide one. (Though the user's menu may explicitly merge the system wide one.)

Systems that offer multiple desktop environments and that want to use distinct menu layouts in the different environments can use differently prefixed .menu files. In this case the `$XDG_MENU_PREFIX` environment variable must be set by the system to reflect the .menu file that is being used.

For example if a system contains both the GNOME and the KDE desktop environments it can decide to use gnome-applications.menu as the menu layout in GNOME sessions and kde-applications.menu as the menu layout in KDE sessions. To correctly reflect this, it should set the `$XDG_MENU_PREFIX` environment variable to "gnome-" respectively "kde-".

Implementations may chose to use .menu files with other names for tasks or menus other than the main application menu. Such usage is not covered by this specification.

`$XDG_CONFIG_DIRS`/menus/applications-merged/  
The default merge directories included in the \<DefaultMergeDirs\> element. By convention, third parties may add new \<Menu\> files in this location to create their own sub-menus.

Note that a system that uses either gnome-applications.menu or kde-applications.menu depending on the desktop environment in use must still use applications-merged as the default merge directory in both cases.

Implementations may chose to use .menu files with names other than application.menu for tasks or menus other than the main application menu. In that case the first part of the name of the default merge directory is derived from the name of the .menu file.

For example in a system that uses a preferences.menu file to describe an additional menu, the default merge directories included in the \<DefaultMergeDirs\> element in the preferences.menu file would become `$XDG_CONFIG_DIRS`/menus/preferences-merged/

`$XDG_DATA_DIRS`/applications/  
This directory contains a .desktop file for each possible menu item. Each directory in the `$XDG_DATA_DIRS` search path should be used (i.e. desktop entries are collected from all of them, not just the first one that exists). When two desktop entries have the same name, the one appearing earlier in the path is used.

The \<DefaultAppDirs\> element in a menu file indicates that this default list of desktop entry locations should be scanned at that point. If a menu file does not contain \<DefaultAppDirs\>, then these locations are not scanned.

`$XDG_DATA_DIRS`/desktop-directories/  
This directory contains directory entries which may be associated with folders in the menu layout. Each directory in the search path should be used. Only files ending in .directory are used; other files are ignored.

The \<DefaultDirectoryDirs\> element in a menu file indicates that this default list of directory entry locations should be scanned at that point. If a menu file does not contain \<DefaultDirectoryDirs\>, then these locations are not scanned.
