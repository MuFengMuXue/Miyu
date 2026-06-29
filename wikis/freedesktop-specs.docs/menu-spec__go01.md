## Glossary

This glossary defines some of the terms used in this specification.

Desktop entry  
A desktop entry is a file with a name ending in the ".desktop" extension which conforms to the [desktop entry specification (http://www.freedesktop.org/Standards/desktop-entry-spec)](http://www.freedesktop.org/Standards/desktop-entry-spec) with `Type=Application`. It describes a menu item, including a name, an icon, and what to do when the item is selected. Desktop entries are also known as ".desktop files."

Desktop-File Id  
The ID to identify a desktop entry with. For desktop files installed in \$XDG_DATA_DIRS/applications, this is the same as the desktop file ID defined in the Desktop Entry Specification. In addition, if `/opt/ude` is defined as \<LegacyDir prefix="foo-"\> then `/opt/ude/Settings/bar.desktop` has the desktop-file id `foo-bar.desktop`

Directory entry  
A directory entry is a file with a name ending in the ".directory" extension which conforms to the [desktop entry specification (http://www.freedesktop.org/Standards/desktop-entry-spec)](http://www.freedesktop.org/Standards/desktop-entry-spec) with `Type=Directory`. It provides a localized name and an icon for a submenu. Directory entries are also known as ".directory files."

Menu path  
A "menu path" is the path to a particular menu. Menu paths are always "relative" so never start with a slash character. The path to a menu is simply the \<Name\> of each parent of the menu, followed by the \<Name\> of the menu itself. For example, "Foo/Bar/Baz" is a valid menu path.

Relative path  
The canonical path to a directory entry, relative to the \<DirectoryDir\> containing the entry. For example, if `/usr/share/desktop-directories` is specified as an \<DirectoryDir\>, the relative path to `/usr/share/desktop-directories/foo/bar.directory` is `foo/bar.directory`.
