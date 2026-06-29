# Wallpaper

## Description

Portal for setting the desktop’s Wallpaper

This simple interface lets sandboxed applications set the user’s desktop background picture.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.portal.Wallpaper:version

    version readable u

## Methods

### org.freedesktop.portal.Wallpaper.SetWallpaperURI

    SetWallpaperURI (
      IN parent_window s,
      IN uri s,
      IN options a{sv},
      OUT handle o
    )

Asks to set a given picture as the desktop background picture.

Note that file: uris are explicitly not supported here. To use a local image file as background, use the [org.freedesktop.portal.Wallpaper.SetWallpaperFile](#org-freedesktop-portal-wallpaper-setwallpaperfile) method.

Supported keys in the `options` vardict include:

- `show-preview` (`b`)

  Whether to show a preview of the picture. Note that the portal may decide to show a preview even if this option is not set.

- `set-on` (`s`)

  Where to set the wallpaper. Possible values are `background`, `lockscreen`, or `both`.

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

uri  
The picture file URI according to RFC 3986

options  
Options that influence the behavior of the portal

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.Wallpaper.SetWallpaperFile

    SetWallpaperFile (
      IN parent_window s,
      IN fd h,
      IN options a{sv},
      OUT handle o
    )

Asks to set a given local file as the desktop background picture.

Supported keys in the `options` vardict include:

- `show-preview` (`b`)

  Whether to show a preview of the picture. Note that the portal may decide to show a preview even if this option is not set.

- `set-on` (`s`)

  Where to set the wallpaper. Possible values are `background`, `lockscreen`, or `both`.

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

fd  
File descriptor for the file to open

options  
Options that influence the behavior of the portal

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call
