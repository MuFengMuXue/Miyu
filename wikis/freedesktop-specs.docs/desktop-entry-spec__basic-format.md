## 3 Basic format of the file

Desktop entry files are encoded in UTF-8. A file is interpreted as a series of lines that are separated by linefeed characters. Case is significant everywhere in the file.

Compliant implementations MUST not remove any fields from the file, even if they don't support them. Such fields must be maintained in a list somewhere, and if the file is "rewritten", they will be included. This ensures that any desktop-specific extensions will be preserved even if another system accesses and changes the file.

### 3.1 Comments

Lines beginning with a `#` and blank lines are considered comments and will be ignored, however they should be preserved across reads and writes of the desktop entry file.

Comment lines are uninterpreted and may contain any character (except for LF). However, using UTF-8 for comment lines that contain characters not in ASCII is encouraged.

### 3.2 Group headers

A group header with name `groupname` is a line in the format:

``` programlisting
[groupname]
```

Group names may contain all ASCII characters except for `[` and `]` and control characters.

Multiple groups may not have the same name.

All `{key,value}` pairs following a group header until a new group header belong to the group.

The basic format of the desktop entry file requires that there be a group header named `Desktop Entry`. There may be other groups present in the file, but this is the most important group which explicitly needs to be supported. This group should also be used as the "magic key" for automatic MIME type detection. There should be nothing preceding this group in the desktop entry file but possibly one or more comments.

### 3.3 Entries

Entries in the file are `{key,value}` pairs in the format:

``` programlisting
Key=Value
```

Space before and after the equals sign should be ignored; the `=` sign is the actual delimiter.

Only the characters `A-Za-z0-9-` may be used in key names.

As the case is significant, the keys `Name` and `NAME` are not equivalent.

Multiple keys in the same group may not have the same name. Keys in different groups may have the same name.
