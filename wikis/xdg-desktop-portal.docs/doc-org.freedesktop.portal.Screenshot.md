# Screenshot

## Description

Portal for taking screenshots

This simple portal lets sandboxed applications request a screenshot.

The screenshot will be made accessible to the application (which may involve adding it to the [Documents portal](doc-org.freedesktop.portal.Documents.md#org-freedesktop-portal-documents)).

This documentation describes **version 3** of this interface.

## Properties

### org.freedesktop.portal.Screenshot:AvailableTargets

    AvailableTargets readable u

A bitmask of available screenshot targets. Available targets are:

- `1`: Screen: The entire screen.

- `2`: Window: A window selected by the user.

- `4`: Area: An area selected by the user.

- `8`: Active Window: The currently active window.

This property was added in version 3 of this interface.

### org.freedesktop.portal.Screenshot:version

    version readable u

## Methods

### org.freedesktop.portal.Screenshot.Screenshot

    Screenshot (
      IN parent_window s,
      IN options a{sv},
      OUT handle o
    )

Takes a screenshot.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `modal` (`b`)

  Whether the dialog should be modal. Default is yes.

- `interactive` (`b`)

  Hint whether the dialog should offer customization before taking a screenshot. Default is no. **Since version 2.**

- `target` (`u`)

  The screenshot target. It is a single target value, not a bitmask, and must be one of the targets advertised in [org.freedesktop.portal.Screenshot:AvailableTargets](#org-freedesktop-portal-screenshot-availabletargets). If this option is omitted, the portal preserves the previous Screenshot behavior. Available targets are:

  - `1`: Screen: The entire screen.

  - `2`: Window: A window selected by the user.

  - `4`: Area: An area selected by the user.

  - `8`: Active Window: The currently active window.

  This option was added in version 3 of this interface.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `uri` (`s`)

  String containing the uri of the screenshot.

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.Screenshot.PickColor

    PickColor (
      IN parent_window s,
      IN options a{sv},
      OUT handle o
    )

Obtains the color of a single pixel.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `color` (`(ddd)`)

  The color, RGB values in the range \[0,1\], in the sRGB color space.

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call
