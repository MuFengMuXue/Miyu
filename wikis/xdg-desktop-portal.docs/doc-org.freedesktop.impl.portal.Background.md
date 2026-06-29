# Background

## Description

Background portal backend interface

This interface provides APIs related to applications that are running in the background.

## Methods

### org.freedesktop.impl.portal.Background.GetAppState

    GetAppState (
      OUT apps a{sv}
    )

Gets information about running apps. Each entry has an application ID as key. The returned values are of type u and have the following meaning:

- `0`: Background (no open window)

- `1`: Running (at least one open window)

- `2`: Active (in the foreground)

apps  
an array with information about running apps

### org.freedesktop.impl.portal.Background.NotifyBackground

    NotifyBackground (
      IN handle o,
      IN app_id s,
      IN name s,
      OUT response u,
      OUT results a{sv}
    )

Notifies the user that an application is running in the background.

The following results get returned via the `results` vardict:

- `result` (`u`)

  The choice that the user made regarding the background activity:

  - `0`: Forbid background activity by this app

  - `1`: Allow background activity by this app

  - `2`: Allow this instance of background activity

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

app_id  
App id of the application

name  
A display name for the application

response  
Numeric response, not used

results  
Vardict with results of the call

### org.freedesktop.impl.portal.Background.EnableAutostart

    EnableAutostart (
      IN app_id s,
      IN enable b,
      IN commandline as,
      IN flags u,
      OUT result b
    )

This is deprecated! New versions of xdg-desktop-portal will not call this method.

Enables or disables autostart for an application.

The following flags are understood:

- `1`: Use D-Bus activation

app_id  
App id of the application

enable  
TRUE to enable autostart, FALSE to disable it

commandline  
The commandline to use in the autostart file

flags  
Flags influencing the details of the autostarting

result  
TRUE if autostart was enabled, FALSE otherwise

## Signals

### org.freedesktop.impl.portal.Background::RunningApplicationsChanged

    RunningApplicationsChanged ()

This signal gets emitted when applications change their state and it is worth calling GetAppState again.
