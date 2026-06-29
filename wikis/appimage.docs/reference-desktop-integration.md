# Desktop integration

This section discusses how we integrate AppImages into the Linux desktops, what technologies are involved and what customizations and additions we implemented to adapt them to work for AppImages.

## Desktop files

A central component of the Linux desktop, so-called *desktop entries* (or, colloquially, *desktop files*) are also relevant for AppImage desktop integration. Every AppImage ships with such a file in its `AppDir`.

The [FreeDesktop](https://www.freedesktop.org/) project maintains the so-called [Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry-spec/latest/). Desktop Entry files are [INI](https://en.wikipedia.org/wiki/INI_file)-style text documents containing key-value pairs, one per line. The file is structured in multiple sections, most notably the `[Desktop Entry]`, where the main information goes into. There's a set of mandatory and optional keys to be set in these documents, and there may be additional sections.

### Custom keys introduced for AppImage purposes

Aside from the standardized mandatory and optional keys, there may be additional, proprietary keys. They're usually prepended with `X-` to differentiate between standard and custom keys.

The AppImage project defined a few custom keys with special meaning that provide information to enhance our desktop integration algorithm.

X-AppImage-Name
Name of the application. Used to relate two AppImages of the same application but different versions.

**Examples:** `Krita`,`Kdenlive`,`Ultimaker Cura`

X-AppImage-Version
Version of the application bundled in the AppImage.

**Examples:** `1.0.0-beta-2`,`2019.1.1`

X-AppImage-Arch
Architecture of the AppImage.

**Examples:** `x86_64`,`i386``appimagetool`and`libappimage`currently make use mostly of`X-AppImage-Version`.

See also:

>
> > - [AppImageKit#59](https://github.com/AppImage/AppImageKit/issues/59)
> > - [AppImageKit#662](https://github.com/AppImage/AppImageKit/issues/662)
