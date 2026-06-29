# Screenshot

## Description

Screenshot portal backend interface

This screenshot portal lets sandboxed applications request a screenshot.

This documentation describes version 3 of this interface.

## Properties

### org.freedesktop.impl.portal.Screenshot:AvailableTargets

    AvailableTargets readable u

A bitmask of available screenshot targets. Available targets are:

- `1`: Screen: The entire screen.

- `2`: Window: A window selected by the user.

- `4`: Area: An area selected by the user.

- `8`: Active Window: The currently active window.

This property was added in version 3 of this interface.

### org.freedesktop.impl.portal.Screenshot:version

    version readable u

## Methods

### org.freedesktop.impl.portal.Screenshot.Screenshot

    Screenshot (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Takes a screenshot.

Supported keys in the `options` vardict include:

- `modal` (`b`)

  Whether the dialog should be modal. Defaults to yes.

- `interactive` (`b`)

  Hint whether the dialog should offer customization before taking a screenshot. Defaults to no.

- `target` (`u`)

  The screenshot target. It is a single target value, not a bitmask, and must be one of the targets advertised in AvailableTargets. If this option is omitted, the backend should preserve the previous Screenshot behavior. Available targets are:

  - `1`: Screen: The entire screen.

  - `2`: Window: A window selected by the user.

  - `4`: Area: An area selected by the user.

  - `8`: Active Window: The currently active window.

  This option was added in version 3 of this interface.

- `permission_store_checked` (`b`)

  Hint whether the screenshot portal has checked the ‘screenshot’ permission for the requesting app. Defaults to no.

  This option was added in version 2 of this interface.

The following results get returned via the `results` vardict:

- `uri` (`s`)

  A string containing the URI of the screenshot.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

app_id  
App id of the application

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.Screenshot.PickColor

    PickColor (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Obtains the value of a pixel.

The following results get returned via the `results` vardict:

- `` color` `` (`(ddd)`)

  The color, RGB values in the range \[0,1\].

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

app_id  
App id of the application

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call
