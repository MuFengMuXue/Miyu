## 2 File naming

Desktop entry files should have the `.desktop` extension, except for files of `Type` `Directory` which should have the `.directory` extension. Determining file type on basis of extension makes determining the file type very easy and quick. When no file extension is present, the desktop system should fall back to recognition via "magic detection".

For applications, the part of the name of the desktop file before the `.desktop` extension should be a valid [D-Bus well-known name (https://dbus.freedesktop.org/doc/dbus-specification.html#message-protocol-names)](https://dbus.freedesktop.org/doc/dbus-specification.md#message-protocol-names). This means that it is a sequence of non-empty elements separated by dots (U+002E FULL STOP), none of which starts with a digit, and each of which contains only characters from the set `[A-Za-z0-9-_]`: ASCII letters, digits, dash (U+002D HYPHEN-MINUS) and underscore (U+005F LOW LINE).

The name of the desktop entry should follow the "reverse DNS" convention: it should start with a reversed DNS domain name controlled by the author of the application, in lower case. The domain name should be followed by the name of the application, which is conventionally written with words run together and initial capital letters (CamelCase). For example, if the owner of `example.org` writes "Foo Viewer", they might choose the name `org.example.FooViewer`, resulting in a file named `org.example.FooViewer.desktop`.

Well-known names containing the dash are allowed but not recommended, because the dash is not allowed in some related uses of reversed DNS names, such as D-Bus object paths and interface names, and Flatpak app IDs. If the author's domain name contains a dash, replacing it with an underscore is recommended: this cannot cause ambiguity, because underscores are not allowed in DNS domain names.

If the author's domain name contains a label starting with a digit, (which is not allowed in D-Bus well-known names), prepending an underscore to that element of the desktop entry name is recommended. For example, 7-zip.org might release an application named `org._7_zip.Archiver`.

### 2.1 Desktop File ID

Each desktop entry representing an application is identified by its *desktop file ID*, which is based on its filename.

To determine the ID of a desktop file, make its full path relative to the `$XDG_DATA_DIRS` component in which the desktop file is installed, remove the "applications/" prefix, and turn '/' into '-'.

For example `/usr/share/applications/foo/bar.desktop` has the desktop file ID `foo-bar.desktop`.

If multiple files have the same desktop file ID, the first one in the \$XDG_DATA_DIRS precedence order is used.

For example, if `$XDG_DATA_DIRS` contains the default paths /usr/local/share:/usr/share, then `/usr/local/share/applications/org.foo.bar.desktop` and `/usr/share/applications/org.foo.bar.desktop` both have the same desktop file ID `org.foo.bar.desktop`, but only the first one will be used.

If both `foo-bar.desktop` and `foo/bar.desktop` exist, it is undefined which is selected.

If the desktop file is not installed in an `applications` subdirectory of one of the \$XDG_DATA_DIRS components, it does not have an ID.
