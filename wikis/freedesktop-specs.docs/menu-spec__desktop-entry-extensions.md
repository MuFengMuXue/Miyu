## 3 Extensions to the desktop entry format

This specification adds three new fields to [desktop entries (http://www.freedesktop.org/Standards/desktop-entry-spec)](http://www.freedesktop.org/Standards/desktop-entry-spec): `Categories`, `OnlyShowIn` and `NotShowIn`.

The `Categories` field is a list of strings used to classify menu items. For example, applications in the `AudioVideo` category might end up in the "Sound & Video" submenu. [Appendix A, *Registered Categories*](category-registry.html "A. Registered Categories") enumerates the standard categories. Categories not in this document must be prefixed by the string "X-" indicating that they are extensions. Categories are case-sensitive.

Desktop entries should list all categories that clearly apply. They should not list categories that only vaguely or possibly apply, because the user will end up seeing the same desktop entry in a half-dozen places. But it's typical that several categories will apply to a given desktop entry.

The `OnlyShowIn` field is a list of strings identifying the environments that should display a given menu item. If an `OnlyShowIn` field is present, a given environment should only display the menu item if the string identifying that environment is present. The strings are case-sensitive. [Appendix B, *Registered OnlyShowIn Environments*](onlyshowin-registry.html "B. Registered OnlyShowIn Environments") enumerates the strings to use for some common environments.

The `NotShowIn` field is a list of strings identifying the environments that should not display a given menu item. If an `NotShowIn` field is present, a given environment should only display the menu item if the string identifying that environment is not present. The strings are case-sensitive. [Appendix B, *Registered OnlyShowIn Environments*](onlyshowin-registry.html "B. Registered OnlyShowIn Environments") enumerates the strings to use for some common environments.

Environments not in this document must be prefixed by the string "X-" indicating that they are extensions. Environments are case-sensitive.

### 3.1 Examples of using `Categories` and `OnlyShowIn`

A desktop entry for a Qt-based image viewer might contain this `Categories` line:

``` programlisting
            Categories=Qt;Graphics;RasterGraphics;Viewer;
          
```

A desktop entry for Octave, a command-line mathematics program (which would also have the field `Terminal=true`), might have:

``` programlisting
            Categories=ConsoleOnly;Math;
          
```

A desktop entry for a GNOME-specific calculator program that should only appear in GNOME might have:

``` programlisting
            Categories=GNOME;Utility;
            OnlyShowIn=GNOME;
          
```

Note that the `OnlyShowIn` field is a *list* and thus ends in a semicolon.
