## C Deprecated Items

As this standard is quite old there are some deprecated items that may or may not be used by several implementations.

- `Type=MimeType` is deprecated as there is a new standard for this now, see the [Shared MIME-info Database specification (http://www.freedesktop.org/Standards/shared-mime-info-spec)](http://www.freedesktop.org/Standards/shared-mime-info-spec) for more information. In consequence the Keys `Patterns` (various file name extensions associated with the MIME type) and `DefaultApp` (the default application associated with this MIME type) are also deprecated.

- Using `.kdelnk` instead of `.desktop` as the file extension is deprecated.

- Using `[KDE Desktop Entry]` instead of `[Desktop Entry]` as header is deprecated.

- The `Encoding` key is deprecated. It was used to specify whether keys of type `localestring` were encoded in UTF-8 or in the specified locale. Possible values are `UTF-8` and `Legacy-Mixed`. See [Appendix D, *The `Legacy-Mixed` Encoding (Deprecated)*](legacy-mixed.html "D. The Legacy-Mixed Encoding (Deprecated)") for more details.

- Deprecated `Exec` field codes: `%m` (the mini-icon associated with the desktop entry, this should be expanded as two arguments, `--miniicon` and the content of the `MiniIcon` key, it can also be ignored by expanding it to no arguments), %v (the device as listed in the `Dev` key in the desktop file), %d (the directory of a file), %D (the directories of files), %n (the base name of a file) and %N (the base names of files).

- Deprecated keys: `MiniIcon` (small icon for menus, etc.), `TerminalOptions` (if the program runs in a terminal, any options that should be passed to the terminal emulator before actually executing the program), `Protocols`, `Extensions`, `BinaryPattern`, `MapNotify`.

- The `SwallowTitle` and `SwallowExec` keys are deprecated. The `SwallowTitle` key is of type `localestring` and specifies the title of the window if is swallowed onto the panel. The `SwallowExec` key is of type `string` and specifies the program to exec if swallowed app is clicked.

- The `SortOrder` key is deprecated. It is of type `string(s)` and may be used to specify the order in which to display files. The [Desktop Menu Specification (http://www.freedesktop.org/Standards/menu-spec)](http://www.freedesktop.org/Standards/menu-spec) defines another mechanism for defining the order of menu items.

- The `FilePattern` key is deprecated. The value is a list of regular expressions to match against for a file manager to determine if this entry's icon should be displayed. Usually simply the name of the main executable and friends.

- Historically some booleans have been represented by the numeric entries `0` or `1`. With this version of the standard they are now to be represented as a boolean string. However, if an implementation is reading a pre-1.0 desktop entry, it should interpret `0` and `1` as `false` and `true`, respectively.

- Historically lists have been comma separated. This is inconsistent with other lists which are separated by a semicolon. When reading a pre-1.0 desktop entry, comma separated lists should continue to be supported.
