## 4 Possible value types

The value types recognized are `string`, `localestring`, `iconstring`, `boolean`, and `numeric`.

- Values of type `string` may contain all ASCII characters except for control characters.

- Values of type `localestring` are user displayable, and are encoded in UTF-8.

- Values of type `iconstring` are the names of icons; these may be absolute paths, or symbolic names for icons located using the algorithm described in the [Icon Theme Specification (http://freedesktop.org/wiki/Standards/icon-theme-spec)](http://freedesktop.org/wiki/Standards/icon-theme-spec). Such values are not user-displayable, and are encoded in UTF-8.

- Values of type `boolean` must either be the string `true` or `false`.

- Values of type `numeric` must be a valid floating point number as recognized by the `%f` specifier for `scanf` in the `C` locale.

The escape sequences `\s`, `\n`, `\t`, `\r`, and `\\` are supported for values of type `string`, `localestring` and `iconstring`, meaning ASCII space, newline, tab, carriage return, and backslash, respectively.

Some keys can have multiple values. In such a case, the value of the key is specified as a plural: for example, `string(s)`. The multiple values should be separated by a semicolon and the value of the key may be optionally terminated by a semicolon. Trailing empty strings must always be terminated with a semicolon. Semicolons in these values need to be escaped using `\;`.
