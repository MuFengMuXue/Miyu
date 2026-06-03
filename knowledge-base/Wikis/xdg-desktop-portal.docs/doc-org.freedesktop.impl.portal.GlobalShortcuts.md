# Global Shortcuts

## Description

GlobalShortcuts portal backend interface

This portal lets applications register global shortcuts so they can act regardless of the system state upon an input event.

This documentation describes version 2 of this interface.

## Properties

### org.freedesktop.impl.portal.GlobalShortcuts:version

    version readable u

## Methods

### org.freedesktop.impl.portal.GlobalShortcuts.CreateSession

    CreateSession (
      IN handle o,
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Create a global shortcuts session.

There are currently no supported keys in the `results` vardict.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

session_handle  
Object path for the ref:org.freedesktop.impl.portal.Session object representing the session being created

app_id  
App id of the application

options  
Vardict with optional further information. See [org.freedesktop.portal.GlobalShortcuts.CreateSession](doc-org.freedesktop.portal.GlobalShortcuts.md#org-freedesktop-portal-globalshortcuts-createsession)

response  
Numeric Request response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.GlobalShortcuts.BindShortcuts

    BindShortcuts (
      IN handle o,
      IN session_handle o,
      IN shortcuts a(sa{sv}),
      IN parent_window s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Bind the shortcuts of this session. This will typically result the portal presenting a dialog letting the user configure shortcut triggers. Backends might want to only show such a dialog if shortcuts includes shortcuts that were not bound in previous sessions by the application or only include shortcuts in such a dialog that were not used in previous BindShortcuts requests by the application.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

shortcuts  
The identifier of the shortcuts we intend to register, empty for all shortcuts

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options

response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.GlobalShortcuts.ListShortcuts

    ListShortcuts (
      IN handle o,
      IN session_handle o,
      OUT response u,
      OUT results a{sv}
    )

Lists shortcuts of a session.

If BindShortcuts was called for session all active shortcuts for session are returned. Otherwise returns the shortcuts that were sucessfully bound in a previous session by the application.

The following results get returned in the `results` vardict:

- `shortcuts` (`a(sa{sv})`)

  A list of shortcuts.

  See the [org.freedesktop.portal.GlobalShortcuts.BindShortcuts](doc-org.freedesktop.portal.GlobalShortcuts.md#org-freedesktop-portal-globalshortcuts-bindshortcuts) method for the list of supported properties of shortcuts.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.GlobalShortcuts.ConfigureShortcuts

    ConfigureShortcuts (
      IN session_handle o,
      IN parent_window s,
      IN options a{sv}
    )

Request showing a configuration UI so the user is able to configure all shortcuts of this session.

Supported keys in the `options` vardict include:

- `activation_token` (`s`)

  A token that can be used to activate the configuration window.

This method was added in version 2 of this interface.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object representing the session

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

## Signals

### org.freedesktop.impl.portal.GlobalShortcuts::Activated

    Activated (
      session_handle o,
      shortcut_id s,
      timestamp t,
      options a{sv}
    )

Emitted when a shortcut is activated.

Supported keys in the `options` vardict include:

- `activation_token` (`s`)

  A token that can be used to activate a window in response to the shortcut getting activated.

session_handle  
Session that requested the shortcut

shortcut_id  
the application-provided ID for the notification

timestamp  
the time of activation with millisecond granularity, with an undefined base.

options  
Vardict with optional further information

### org.freedesktop.impl.portal.GlobalShortcuts::Deactivated

    Deactivated (
      session_handle o,
      shortcut_id s,
      timestamp t,
      options a{sv}
    )

Emitted when a shortcut is deactivated.

Supported keys in the `options` vardict include:

- `activation_token` (`s`)

  A token that can be used to activate a window in response to the shortcut getting deactivated.

session_handle  
Session that requested the shortcut

shortcut_id  
the application-provided ID for the notification

timestamp  
the time of deactivation with millisecond granularity, with an undefined base.

options  
Vardict with optional further information

### org.freedesktop.impl.portal.GlobalShortcuts::ShortcutsChanged

    ShortcutsChanged (
      session_handle o,
      shortcuts a(sa{sv})
    )

Emitted when shortcuts are changed.

The results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal. See [org.freedesktop.portal.GlobalShortcuts.BindShortcuts](doc-org.freedesktop.portal.GlobalShortcuts.md#org-freedesktop-portal-globalshortcuts-bindshortcuts) for the list of supported properties of shortcuts.

session_handle  
Session that requested the shortcut

shortcuts  
The list of changed shortcuts
