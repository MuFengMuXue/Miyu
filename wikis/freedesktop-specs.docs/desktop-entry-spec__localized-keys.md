## 5 Localized values for keys

Keys with type `localestring` and `iconstring` may be postfixed by \[*LOCALE*\], where *LOCALE* is the locale type of the entry. *LOCALE* must be of the form *`lang`*`_`*`COUNTRY`*`.`*`ENCODING`*`@`*`MODIFIER`*, where `_`*`COUNTRY`*, `.`*`ENCODING`*, and `@`*`MODIFIER`* may be omitted. If a postfixed key occurs, the same key must be also present without the postfix.

When reading in the desktop entry file, the value of the key is selected by matching the current POSIX locale for the `LC_MESSAGES` category against the *LOCALE* postfixes of all occurrences of the key, with the `.`*`ENCODING`* part stripped.

The matching is done as follows. If `LC_MESSAGES` is of the form *`lang`*`_`*`COUNTRY`*`.`*`ENCODING`*`@`*`MODIFIER`*, then it will match a key of the form *`lang`*`_`*`COUNTRY`*`@`*`MODIFIER`*. If such a key does not exist, it will attempt to match *`lang`*`_`*`COUNTRY`* followed by *`lang`*`@`*`MODIFIER`*. Then, a match against *lang* by itself will be attempted. Finally, if no matching key is found the required key without a locale specified is used. The encoding from the `LC_MESSAGES` value is ignored when matching.

If `LC_MESSAGES` does not have a *MODIFIER* field, then no key with a modifier will be matched. Similarly, if `LC_MESSAGES` does not have a *COUNTRY* field, then no key with a country specified will be matched. If `LC_MESSAGES` just has a *lang* field, then it will do a straight match to a key with a similar value. The following table lists possible matches of various `LC_MESSAGES` values in the order in which they are matched. Note that the *ENCODING* field isn't shown.

###### Table 1: Locale Matching

| `LC_MESSAGES` value | Possible keys in order of matching |
|----|----|
| *`lang`*`_`*`COUNTRY`*`@`*`MODIFIER`* | *`lang`*`_`*`COUNTRY`*`@`*`MODIFIER`*, *`lang`*`_`*`COUNTRY`*, *`lang`*`@`*`MODIFIER`*, *`lang`*, default value |
| *`lang`*`_`*`COUNTRY`* | *`lang`*`_`*`COUNTRY`*, *lang*, default value |
| *`lang`*`@`*`MODIFIER`* | *`lang`*`@`*`MODIFIER`*, *lang*, default value |
| *lang* | *lang*, default value |

For example, if the current value of the `LC_MESSAGES` category is `sr_YU@Latn` and the desktop file includes:

``` programlisting
 Name=Foo
 Name[sr_YU]=...
 Name[sr@Latn]=...
 Name[sr]=...
```

then the value of the `Name` keyed by `sr_YU` is used.

Although icon names of type `iconstring` are localizable, they are not human-readable strings, so should typically not be handled by translation tools. Most applications are not expected to localize their icons; exceptions might include icons containing text or culture-specific symbology.
