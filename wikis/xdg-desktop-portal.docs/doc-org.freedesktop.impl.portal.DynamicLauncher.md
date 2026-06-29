# Dynamic Launcher

## Description

Dynamic launcher portal backend interface

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.impl.portal.DynamicLauncher:SupportedLauncherTypes

    SupportedLauncherTypes readable u

A bitmask of available launcher types. Currently defined types are:

- `1`: Application. A launcher that represents an application.

- `2`: Webapp. A launcher that represents a web app.

### org.freedesktop.impl.portal.DynamicLauncher:version

    version readable u

## Methods

### org.freedesktop.impl.portal.DynamicLauncher.PrepareInstall

    PrepareInstall (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN name s,
      IN icon_v v,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Presents a dialog to the user to allow them to see the icon, potentially change the name, and confirm installation of the launcher.

Supported keys in the `options` vardict:

- `modal` (`b`)

  Whether to make the dialog modal. Defaults to yes.

- `launcher_type` (`u`)

  The type of launcher being created. For supported values see the SupportedLauncherTypes property. Defaults to “Application”.

- `target` (`s`)

  For a launcher of type “Webapp”, this is the URI, as described in RFC 3986, of the web app being installed. This is displayed in the user-facing dialog. For other launcher types, this is not needed.

- `editable_name` (`b`)

  If true, the user will be able to edit the name of the launcher. Defaults to true.

- `editable_icon` (`b`)

  If true, the user will be able to edit the icon of the launcher, if the implementation supports this. Defaults to false.

The following results get returned via the `results` vardict:

- `name` (`s`)

  The name chosen by the user for the launcher (or the default if the editable_name option was false).

- `icon` (`v`)

  The icon chosen by the user for the launcher (or the default if the `editable_icon` option was false).

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

app_id  
App id of the application

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

name  
The default name for the launcher

icon_v  
A \#GBytesIcon as returned by g_icon_serialize()

options  
Vardict with optional further information

response  
Numeric response (0 == success)

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.DynamicLauncher.RequestInstallToken

    RequestInstallToken (
      IN app_id s,
      IN options a{sv},
      OUT response u
    )

The `response` returned by this method is used to determine whether to give an install token to the caller, which can be used to avoid the need for a confirmation dialog; the token can be passed to the [org.freedesktop.portal.DynamicLauncher.Install](doc-org.freedesktop.portal.DynamicLauncher.md#org-freedesktop-portal-dynamiclauncher-install) method just as if it were acquired via the [org.freedesktop.portal.DynamicLauncher.PrepareInstall](doc-org.freedesktop.portal.DynamicLauncher.md#org-freedesktop-portal-dynamiclauncher-prepareinstall) method.

It is up to the portal implementation to decide whether this method is allowed based on the `app_id` of the caller.

The `options` vardict currently has no supported entries.

app_id  
App id of the application

options  
Vardict with optional further information

response  
0 if the caller should be allowed to do non-interactive launcher installation, a nonzero number otherwise
