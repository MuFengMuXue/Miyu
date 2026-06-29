## 7 The `Exec` key

The `Exec` key must contain a command line. A command line consists of an executable program optionally followed by one or more arguments. The executable program can either be specified with its full path or with the name of the executable only. If no full path is provided the executable is looked up in the \$PATH environment variable used by the desktop environment. The name or path of the executable program may not contain the equal sign ("="). Arguments are separated by a space.

Arguments may be quoted in whole. If an argument contains a reserved character the argument must be quoted. The rules for quoting of arguments is also applicable to the executable name or path of the executable program as provided.

Quoting must be done by enclosing the argument between double quotes and escaping the double quote character, backtick character ("\`"), dollar sign ("\$") and backslash character ("\\) by preceding it with an additional backslash character. Implementations must undo quoting before expanding field codes and before passing the argument to the executable program. Reserved characters are space (" "), tab, newline, double quote, single quote ("'"), backslash character ("\\), greater-than sign ("\>"), less-than sign ("\<"), tilde ("~"), vertical bar ("\|"), ampersand ("&"), semicolon (";"), dollar sign ("\$"), asterisk ("\*"), question mark ("?"), hash mark ("#"), parenthesis ("(") and (")") and backtick character ("\`").

Note that the general escape rule for values of type string states that the backslash character can be escaped as ("\\") as well and that this escape rule is applied before the quoting rule. As such, to unambiguously represent a literal backslash character in a quoted argument in a desktop entry file requires the use of four successive backslash characters ("\\\\"). Likewise, a literal dollar sign in a quoted argument in a desktop entry file is unambiguously represented with ("\\\$").

A number of special field codes have been defined which will be expanded by the file manager or program launcher when encountered in the command line. Field codes consist of the percentage character ("%") followed by an alpha character. Literal percentage characters must be escaped as `%%`. Deprecated field codes should be removed from the command line and ignored. Field codes are expanded only once, the string that is used to replace the field code should not be checked for field codes itself.

Command lines that contain a field code that is not listed in this specification are invalid and must not be processed, in particular implementations may not introduce support for field codes not listed in this specification. Extensions, if any, should be introduced by means of a new key.

Implementations must take care not to expand field codes into multiple arguments unless explicitly instructed by this specification. This means that name fields, filenames and other replacements that can contain spaces must be passed as a single argument to the executable program after expansion.

Although the `Exec` key is defined to have a value of the type string, which is limited to ASCII characters, field code expansion may introduce non-ASCII characters in arguments. Implementations must take care that all characters in arguments passed to the executable program are properly encoded according to the applicable locale setting.

Recognized field codes are as follows:

| Code | Description |
|----|----|
| `%f` | A single file name (including the path), even if multiple files are selected. The system reading the desktop entry should recognize that the program in question cannot handle multiple file arguments, and it should probably spawn and execute multiple copies of a program for each selected file if the program is not able to handle additional file arguments. If files are not on the local file system (i.e. are on HTTP or FTP locations), the files will be copied to the local file system and `%f` will be expanded to point at the temporary file. Used for programs that do not understand the URL syntax. |
| `%F` | A list of files. Use for apps that can open several local files at once. Each file is passed as a separate argument to the executable program. |
| `%u` | A single URL. Local files may either be passed as file: URLs or as file path. |
| `%U` | A list of URLs. Each URL is passed as a separate argument to the executable program. Local files may either be passed as file: URLs or as file path. |
| `%d` | Deprecated. |
| `%D` | Deprecated. |
| `%n` | Deprecated. |
| `%N` | Deprecated. |
| `%i` | The `Icon` key of the desktop entry expanded as two arguments, first `--icon` and then the value of the `Icon` key. Should not expand to any arguments if the `Icon` key is empty or missing. |
| `%c` | The translated name of the application as listed in the appropriate `Name` key in the desktop entry. |
| `%k` | The location of the desktop file as either a URI (if for example gotten from the vfolder system) or a local filename or empty if no location is known. |
| `%v` | Deprecated. |
| `%m` | Deprecated. |

A command line may contain at most one %f, %u, %F or %U field code. If the application should not open any file the %f, %u, %F and %U field codes must be removed from the command line and ignored.

Field codes must not be used inside a quoted argument, the result of field code expansion inside a quoted argument is undefined. The %F, %U and %i field codes may only be used as an argument on their own.
