## 7 Legacy Menu Hierarchies

Traditionally, menus were defined as a filesystem hierarchy, with each filesystem directory corresponding to a submenu. Implementations of this specification must be able to load these old-style hierarchies as specified in this section.

The general approach is: the legacy hierarchy is converted into a \<Menu\>, and then this menu layout is merged with the menu that specified \<LegacyDir\>.

Desktop entries in the legacy hierarchy should be added to the pool of desktop entries as if the \<LegacyDir\> were an \<AppDir\>. Directory entries in the legacy hierarchy should be added to the pool of directory entries as if the \<LegacyDir\> were a \<DirectoryDir\>. This can be trivially implemented by adding appropriate \<AppDir\> and \<DirectoryDir\> statements to the root legacy \<Menu\>. There is one slight complexity, namely the "prefix" attribute of \<LegacyDir\>.

The menu layout corresponds conceptually to the following, though actually generating the XML is not necessary:

- For each directory in the legacy hierarchy, a \<Menu\> is created with the same \<Name\> as the directory on disk.

- This menu then contains an \<Include\> element that includes each desktop entry in the directory. That is, it should have a \<Filename\>*Foo/Bar/foo.desktop*\</Filename\> for each desktop entry in the directory.

  As a special exception, if a desktop entry in a directory contains a `Categories` field, that desktop entry should *not* be included in the legacy menu. That is, no \<Include\> element should be generated for the entry. This allows a desktop entry to be installed in a legacy location but still work optimally with the menu system specified in this document.

- If the legacy directory contains a ".directory" file, then a \<Directory\> element should be generated that points to said ".directory" file.

- Legacy desktop entries should not be assigned any `Categories` fields if they didn't have them already, except that all legacy entries should have the "Legacy" category added to allow menu files to treat them specially. (If the same directory is given as both a \<LegacyDir\> and an \<AppDir\>, its desktop entries should be labeled "Legacy" only if the \<LegacyDir\> appears later in the file than the \<AppDir\>.)

For example, say we have the following legacy directory hierarchy:

``` programlisting
          /usr/share/applnk
              /usr/share/applnk/.directory
              /usr/share/applnk/bar.desktop
              /usr/share/applnk/System
                  /usr/share/applnk/System/.directory
                  /usr/share/applnk/System/foo.desktop
        
```

Conceptually that is converted to the following \<Menu\>:

``` programlisting
          <!DOCTYPE Menu PUBLIC "-//freedesktop//DTD Menu 1.0//EN"
          "http://www.freedesktop.org/standards/menu-spec/menu-1.0.dtd">

          <Menu>
            <Name>Applications</Name>
            <AppDir>/usr/share/applnk</AppDir>
            <DirectoryDir>/usr/share/applnk</DirectoryDir>
            <Directory>.directory</Directory>
            <Include>
              <Filename>bar.desktop</Filename>
            </Include>
            <Menu>
              <Name>System</Name>
              <AppDir>/usr/share/applnk/System</AppDir>
              <DirectoryDir>/usr/share/applnk/System</DirectoryDir>
              <Directory>.directory</Directory>
              <Include>
                <Filename>foo.desktop</Filename>
              </Include>
            </Menu>
          </Menu>
        
```

This \<Menu\> is then merged as if it were in a file and loaded with \<MergeFile\>.
