# Wallpaper

## Description

Portal for setting the desktop’s Wallpaper

This simple interface lets sandboxed applications set the user’s desktop background picture.

## Methods

### org.freedesktop.impl.portal.Wallpaper.SetWallpaperURI

    SetWallpaperURI (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN uri s,
      IN options a{sv},
      OUT response u
    )

Asks to set a given picture as the desktop background picture.

The following options are supported:

- `show-preview` (`b`)

  Whether to show a preview of the picture. Note that the portal may decide to show a preview even if this option is not set

- `set-on` (`s`)

  Where to set the wallpaper. Possible values are background, lockscreen or both.

handle  
Object path to export the Request object at

app_id  
App id of the application

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

uri  
The picture file URI according to RFC 3986

options  
Options that influence the behavior of the portal

response  
Numberic response
