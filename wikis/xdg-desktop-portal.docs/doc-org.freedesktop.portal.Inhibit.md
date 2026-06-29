# Inhibit

## Description

Portal for inhibiting session transitions

This simple interface lets sandboxed applications inhibit the user session from ending, suspending, idling or getting switched away.

This documentation describes version 3 of this interface.

## Properties

### org.freedesktop.portal.Inhibit:version

    version readable u

## Methods

### org.freedesktop.portal.Inhibit.Inhibit

    Inhibit (
      IN window s,
      IN flags u,
      IN options a{sv},
      OUT handle o
    )

Inhibits a session status changes. To remove the inhibition, call [org.freedesktop.portal.Request.Close](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-close) on the returned handle.

The flags determine what changes are inhibited:

- `1`: Logout

- `2`: User Switch

- `4`: Suspend

- `8`: Idle

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `reason` (`s`)

  User-visible reason for the inhibition.

window  
Identifier for the window

flags  
Flags identifying what is inhibited

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.Inhibit.CreateMonitor

    CreateMonitor (
      IN window s,
      IN options a{sv},
      OUT handle o
    )

Creates a monitoring session. While this session is active, the caller will receive StateChanged signals with updates on the session state.

A successfully created session can at any time be closed using org.freedesktop.portal.Session::Close, or may at any time be closed by the portal implementation, which will be signalled via [org.freedesktop.portal.Session::Closed](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session-closed).

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `session_handle_token` (`s`)

  A string that will be used as the last element of the session handle. Must be a valid object path element. See the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) documentation for more information about the session handle.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `session_handle` (`s`)

  The session handle. An object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object representing the created session.

  Note

  The `session_handle` is an object path that was erroneously implemented as `s`. For backwards compatibility it will remain this type.

This method was added in version 2 of this interface.

window  
the parent window

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.Inhibit.QueryEndResponse

    QueryEndResponse (
      IN session_handle o
    )

Acknowledges that the caller received the [org.freedesktop.portal.Inhibit::StateChanged](#org-freedesktop-portal-inhibit-statechanged) signal. This method should be called within one second or receiving a StateChanged signal with the ‘Query End’ state.

Since version 3.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

## Signals

### org.freedesktop.portal.Inhibit::StateChanged

    StateChanged (
      session_handle o,
      state a{sv}
    )

The StateChanged signal is sent to active monitoring sessions when the session state changes.

When the session state changes to ‘Query End’, clients with active monitoring sessions are expected to respond by calling [org.freedesktop.portal.Inhibit.QueryEndResponse](#org-freedesktop-portal-inhibit-queryendresponse) within a second of receiving the StateChanged signal. They may call [org.freedesktop.portal.Inhibit.Inhibit](#org-freedesktop-portal-inhibit-inhibit) first to inhibit logout, to prevent the session from proceeding to the Ending state.

The following information may get returned in the `state` vardict:

- `screensaver-active` (`b`)

  Whether the screensaver is active.

- `session-state` (`u`)

  The state of the session. This member is new in version 3.

  - `1`: Running

  - `2`: Query End

  - `3`: Ending

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

state  
Vardict with information about the session state
