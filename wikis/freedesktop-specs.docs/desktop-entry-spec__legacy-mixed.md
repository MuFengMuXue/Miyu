## D The `Legacy-Mixed` Encoding (Deprecated)

The `Legacy-Mixed` encoding corresponds to the traditional encoding of desktop files in older versions of the GNOME and KDE desktop files. In this encoding, the encoding of each `localestring` key is determined by the locale tag for that key, if any, instead of being UTF-8. For keys without a locale tag, the value must contain only ASCII characters.

If the file specifies an unsupported encoding, the implementation should either ignore the file, or, if the user has requested a direct operation on the file (such as opening it for editing), display an appropriate error indication to the user.

In the absence of an `Encoding` key, the implementation may choose to autodetect the encoding of the file by using such factors as:

- The location of the file on the file system

- Whether the contents of the file are valid UTF-8

If the implementation does not perform such auto-detection, it should treat a file without an `Encoding` key in the same way as a file with an unsupported `Encoding` key.

If the locale tag includes an `.`*`ENCODING`* part, then that determines the encoding for the line. Otherwise, the encoding is determined by the language, or *`lang`*`_`*`COUNTRY`* pair from the locale tag, according to the following table.

| Encoding              | Aliases |
|-----------------------|---------|
| ARMSCII-8 (\*)        |         |
| BIG5                  |         |
| CP1251                |         |
| EUC-CN                | GB2312  |
| EUC-JP                |         |
| EUC-KR                |         |
| GEORGIAN-ACADEMY (\*) |         |
| GEORGIAN-PS (\*)      |         |
| ISO-8859-1            |         |
| ISO-8859-2            |         |
| ISO-8859-3            |         |
| ISO-8859-5            |         |
| ISO-8859-7            |         |
| ISO-8859-9            |         |
| ISO-8859-13           |         |
| ISO-8859-14           |         |
| ISO-8859-15           |         |
| KOI8-R                |         |
| KOI8-U                |         |
| TCVN-5712 (\*)        | TCVN    |
| TIS-620               |         |
| VISCII                |         |

Encoding  
The name given here is listed here is typically the canonical name for the encoding in the GNU C Library's `iconv` facility. Encodings marked with (\*) are not currently supported by the GNU C Library; for this reason, implementations may choose to ignore lines in desktop files that resolve to this encoding. Desktop files with these encodings are currently rare or non-existent.

Aliases  
Other names for the encoding found in existing desktop files.

Tags  
Language tags for which this is the default encoding.

This table above covers all tags and encodings that are known to be currently in use. Implementors may choose to support encodings not in the above set. For tags without defaults listed in the above table, desktop file creators must specify the `.`*`ENCODING`* part of the locale tag.

Matching the `.`*`ENCODING`* part of the locale tag against a locale name or alias should be done by stripping all punctuation characters from both the tag and the name or alias, converting both name and alias to lowercase, and comparing the result. This is necessary because, for example, `Big5` is frequently found instead of `BIG5` and `georgianacademy` instead of `GEORGIAN-ACADEMY`. Desktop files creators should, however, use the name as it appears in the "Encoding" column above.
