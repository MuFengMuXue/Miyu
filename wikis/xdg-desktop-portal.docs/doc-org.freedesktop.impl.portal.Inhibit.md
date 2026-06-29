# Inhibit

## Description

Inhibit portal backend interface

The inhibit portal lets sandboxed applications inhibit the user session from ending, suspending, idling or getting switched away.

## Methods

### org.freedesktop.impl.portal.Inhibit.Inhibit

    Inhibit (
      IN handle o,
      IN app_id s,
      IN window s,
      IN flags u,
      IN options a{sv}
    )

Inhibits session status changes. As a side-effect of this call, a [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object is exported on the object path `handle`. To end the inhibition, call [org.freedesktop.impl.portal.Request.Close](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request-close) on that object.

The flags determine what changes are inhibited:

- `1`: Logout

- `2`: User Switch

- `4`: Suspend

- `8`: Idle

Supported keys in the `options` vardict include:

- `reason` (`s`)

  User-visible reason for the inhibition.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

app_id  
Application id

window  
Identifier for the window

flags  
Flags identifying what is inhibited

options  
Vardict with optional further information

### org.freedesktop.impl.portal.Inhibit.CreateMonitor

    CreateMonitor (
      IN handle o,
      IN session_handle o,
      IN app_id s,
      IN window s,
      OUT response u
    )

Creates a monitoring session. While this session is active, the caller will receive StateChanged signals with updates on the session state.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

session_handle  
Object path for the created [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object

app_id  
App id of the application

window  
the parent window

response  
the result of the operation (0 == success)

### org.freedesktop.impl.portal.Inhibit.QueryEndResponse

    QueryEndResponse (
      IN session_handle o
    )

Acknowledges that the caller received the [org.freedesktop.impl.portal.Inhibit::StateChanged](#org-freedesktop-impl-portal-inhibit-statechanged) signal. This method should be called within one second or receiving a StateChanged signal with the ‘Query End’ state.

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object

## Signals

### org.freedesktop.impl.portal.Inhibit::StateChanged

    StateChanged (
      session_handle o,
      state a{sv}
    )

The StateChanged signal is sent to active monitoring sessions when the session state changes.

When the session state changes to ‘Query End’, clients with active monitoring sessions are expected to respond by calling [org.freedesktop.impl.portal.Inhibit.QueryEndResponse](#org-freedesktop-impl-portal-inhibit-queryendresponse) within a second of receiving the StateChanged signal.

The following information may get returned in the `state` vardict:

- `screensaver-active` (`b`)

  Whether the screensaver is active.

- `session-state` (`u`)

  The state of the session.

  - `1`: Running

  - `2`: Query End

  - `3`: Ending

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

state  
Vardict with information about the session state
