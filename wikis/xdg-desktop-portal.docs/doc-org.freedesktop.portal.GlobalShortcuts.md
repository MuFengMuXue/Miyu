# Global Shortcuts

## Description

Portal for managing global shortcuts

This portal lets applications create global shortcuts sessions, and register shortcuts to them. These shortcuts are activated regardless of the focused state of the application window.

To use this portal, applications have to create a session under which its actions will be collected. Then shortcuts can be bound (see org.freedesktop.portal.GlobalShortcuts.Bind), and listed (see org.freedesktop.portal.GlobalShortcuts.ListShortcuts).

All global shortcuts are bound to a session, and all sessions are bound to the application that created them.

The [org.freedesktop.portal.GlobalShortcuts::Activated](#org-freedesktop-portal-globalshortcuts-activated) and [org.freedesktop.portal.GlobalShortcuts::Deactivated](#org-freedesktop-portal-globalshortcuts-deactivated) signals are emitted, respectively, whenever a shortcut is activated and deactivated.

This documentation describes version 2 of this interface.

## Properties

### org.freedesktop.portal.GlobalShortcuts:version

    version readable u

## Methods

### org.freedesktop.portal.GlobalShortcuts.CreateSession

    CreateSession (
      IN options a{sv},
      OUT handle o
    )

Creates a global shortcuts session.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the org.freedesktop.portal.Request documentation for more information about the `handle`.

- `session_handle_token` (`s`)

  A string that will be used as the last element of the session handle. Must be a valid object path element. See the org.freedesktop.portal.Session documentation for more information about the session handle.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `session_handle` (`s`)

  The session handle. An object path for the org.freedesktop.portal.Session object representing the created session.

  Note

  The `session_handle` is an object path that was erroneously implemented as `s`. For backwards compatibility it will remain this type.

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.GlobalShortcuts.BindShortcuts

    BindShortcuts (
      IN session_handle o,
      IN shortcuts a(sa{sv}),
      IN parent_window s,
      IN options a{sv},
      OUT request_handle o
    )

Bind the shortcuts. This will typically result the portal presenting a dialog showing the shortcuts and allowing users to configure the shortcuts. An application can only attempt bind shortcuts of a session once.

Each element of the `shortcuts` array is a tuple composed of a shortcut id, and a vardict with the following keys:

- `description` (`s`)

  User-readable text describing what the shortcut does.

- `preferred_trigger` (`s`)

  The preferred shortcut trigger, defined as described by the [shortcuts XDG specification](https://specifications.freedesktop.org/shortcuts-spec/latest/). Optional.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

The following results get returned via the ref::org.freedesktop.portal.Request::Response signal:

- `shortcuts` (`a(sa{sv})`)

  The list of shortcuts which were bound. This is a subset of the shortcuts which were passed in from the `shortcuts` variable of this method (this includes the set of all shortcuts and the empty set). The keys they may contain are described below, and are different from the keys in the `shortcuts` variable of this method.

Each element of the `shortcuts` array returned by the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal is a tuple composed of a shortcut id, and a vardict with the following keys:

- `description` (`s`)

  User-readable text describing what the shortcut does.

- `trigger_description` (`s`)

  User-readable text describing how to trigger the shortcut for the client to render.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object representing the session

shortcuts  
The list of shortcuts to bind

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

request_handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.GlobalShortcuts.ListShortcuts

    ListShortcuts (
      IN session_handle o,
      IN options a{sv},
      OUT request_handle o
    )

Lists shortcuts of a session.

If BindShortcuts was called for session all active shortcuts for session are returned. Otherwise returns the shortcuts that were sucessfully bound in a previous session by this application.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `shortcuts` (`a(sa{sv})`)

  A list of shortcuts.

  See the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal of the [org.freedesktop.portal.GlobalShortcuts.BindShortcuts](#org-freedesktop-portal-globalshortcuts-bindshortcuts) method for the list of supported properties of shortcuts.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object representing the session

options  
Vardict with optional further information

request_handle

### org.freedesktop.portal.GlobalShortcuts.ConfigureShortcuts

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

### org.freedesktop.portal.GlobalShortcuts::Activated

    Activated (
      session_handle o,
      shortcut_id s,
      timestamp t,
      options a{sv}
    )

Notifies about a shortcut becoming active.

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

### org.freedesktop.portal.GlobalShortcuts::Deactivated

    Deactivated (
      session_handle o,
      shortcut_id s,
      timestamp t,
      options a{sv}
    )

Notifies that a shortcut is not active anymore.

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

### org.freedesktop.portal.GlobalShortcuts::ShortcutsChanged

    ShortcutsChanged (
      session_handle o,
      shortcuts a(sa{sv})
    )

Indicates that the information associated with some of the shortcuts has changed.

See the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal of the [org.freedesktop.portal.GlobalShortcuts.BindShortcuts](#org-freedesktop-portal-globalshortcuts-bindshortcuts) method for the list of supported properties of shortcuts.

session_handle  
Session that requested the shortcut

shortcuts  
The different shortcuts that have been registered. See org.freedesktop.portal.GlobalShortcuts.
