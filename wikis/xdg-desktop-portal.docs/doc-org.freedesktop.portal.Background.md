# Background

## Description

Portal for requesting autostart and background activity

This simple interface lets sandboxed applications request that the application is allowed to run in the background or started automatically when the user logs in.

This documentation describes version 2 of this interface.

## Properties

### org.freedesktop.portal.Background:version

    version readable u

## Methods

### org.freedesktop.portal.Background.RequestBackground

    RequestBackground (
      IN parent_window s,
      IN options a{sv},
      OUT handle o
    )

Requests that the application is allowed to run in the background.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `reason` (`s`)

  User-visible reason for the request.

- `autostart` (`b`)

  true if the app also wants to be started automatically at login.

- `commandline` (`as`)

  Commandline to use add when autostarting at login. If this is not specified, the `Exec` key from the desktop file will be used.

- `dbus-activatable` (`b`)

  true to use D-Bus activation for autostart.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `background` (`b`)

  true if the application is allowed to run in the background.

- `autostart` (`b`)

  true if the application will be autostarted.

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.Background.SetStatus

    SetStatus (
      IN options a{sv}
    )

This method was added in version 2 of this interface.

Sets the status of the application running in background.

Supported keys in the `options` vardict include:

- `message` (`s`)

  A string that will be used as the status message of the application. This should be a single line that can be presented to the user in a list, not a full sentence or paragraph. Must be shorter than 96 characters.

options  
Vardict with optional further information
