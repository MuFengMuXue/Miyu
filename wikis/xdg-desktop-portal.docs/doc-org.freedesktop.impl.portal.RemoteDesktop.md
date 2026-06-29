# Remote Desktop

## Description

Remote desktop portal backend interface

The Remote desktop portal allows to create remote desktop sessions.

This documentation describes version 2 of this interface.

## Properties

### org.freedesktop.impl.portal.RemoteDesktop:AvailableDeviceTypes

    AvailableDeviceTypes readable u

A bitmask of available source types. Currently defined types are:

- `1`: KEYBOARD

- `2`: POINTER

- `4`: TOUCHSCREEN

### org.freedesktop.impl.portal.RemoteDesktop:version

    version readable u

## Methods

### org.freedesktop.impl.portal.RemoteDesktop.CreateSession

    CreateSession (
      IN handle o,
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Create a remote desktop session.

A remote desktop session is used to allow remote controlling a desktop session. It can also be used together with a screen cast session (see org.freedesktop.portal.ScreenCast), but may only be started and stopped with this interface.

The following results get returned in the `results` vardict:

- `session` (`s`)

  The session id. A string representing the created screen cast session.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

session_handle

app_id  
App id of the application

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.RemoteDesktop.SelectDevices

    SelectDevices (
      IN handle o,
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Configure what the devices remote desktop session should expose.

Supported keys in the `options` vardict include:

- `types` (`u`)

  Bitmask of what device types to request remote controlling of. Default is all.

- `restore_data` (`(suv)`)

  The data to restore from a previous session.

  If the stored session cannot be restored, this value is ignored and the user will be prompted normally. This may happen when, for example, the session contains a monitor or a window that is not available anymore, or when the stored permissions are withdrawn.

  The restore data is composed of the vendor name (e.g. “GNOME” or “KDE”), the version of the implementation-specific private data, and the implementation-specific private data itself.

  This option was added in version 2 of this interface.

- `persist_mode` (`u`)

  How this session should persist. Default is 0. Accepted values are:

  - `0`: Do not persist (default)

  - `1`: Permissions persist as long as the application is running

  - `2`: Permissions persist until explicitly revoked

  If the permission for the session to persist is granted, `restore_data` will be returned in the results of the [org.freedesktop.impl.portal.RemoteDesktop](#org-freedesktop-impl-portal-remotedesktop).Start method.

  This option was added in version 2 of this interface.

For available device types, see the AvailableDeviceTypes property.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

app_id  
App id of the application

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.RemoteDesktop.Start

    Start (
      IN handle o,
      IN session_handle o,
      IN app_id s,
      IN parent_window s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Start the remote desktop session. This will typically result the portal presenting a dialog.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `persist_mode` (`u`)

  How this session should persist. Default is 0. Accepted values are:

  - `0`: Do not persist (default)

  - `1`: Permissions persist as long as the application is running

  - `2`: Permissions persist until explicitly revoked

  If the session should persist, `restore_data` must be returned in the `results` vardict.

  This option was added in version 2 of this interface.

The following results get returned in the `results` vardict:

- `devices` (`u`)

  The device types that can be used for remote control. See the AvailableDeviceTypes property.

- `clipboard_enabled` (`b`)

  A boolean for whether the clipboard was enabled (‘true’) or not (‘false’). See the [Clipboard](doc-org.freedesktop.portal.Clipboard.md#org-freedesktop-portal-clipboard) documentation for more information.

  Since version 2.

- `streams` (`a(ua{sv})`)

  Equivalent to the streams entry documented in [org.freedesktop.impl.portal.ScreenCast.Start](doc-org.freedesktop.impl.portal.ScreenCast.md#org-freedesktop-impl-portal-screencast-start).

- `restore_data` (`(suv)`)

  The data to restore for a future session with a persist_mode other than 0. See the [org.freedesktop.impl.portal.RemoteDesktop](#org-freedesktop-impl-portal-remotedesktop).SelectDevices method for more details.

  This option was added in version 2 of this interface.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

session_handle  
Identifier for the remote desktop session

app_id  
App id of the application

parent_window  
Identifier for the application window

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.RemoteDesktop.NotifyPointerMotion

    NotifyPointerMotion (
      IN session_handle o,
      IN options a{sv},
      IN dx d,
      IN dy d
    )

Notify about a new relative pointer motion event. The (dx, dy) vector represents the new pointer position in the streams logical coordinate space.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

dx  
Relative movement on the x axis

dy  
Relative movement on the y axis

### org.freedesktop.impl.portal.RemoteDesktop.NotifyPointerMotionAbsolute

    NotifyPointerMotionAbsolute (
      IN session_handle o,
      IN options a{sv},
      IN stream u,
      IN x d,
      IN y d
    )

Notify about a new absolute pointer motion event. The (x, y) position represents the new pointer position in the streams logical coordinate space (see the logical_size stream property in [ScreenCast](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast)).

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

stream  
The PipeWire stream node the coordinate is relative to

x  
Pointer motion x coordinate

y  
Pointer motion y coordinate

### org.freedesktop.impl.portal.RemoteDesktop.NotifyPointerButton

    NotifyPointerButton (
      IN session_handle o,
      IN options a{sv},
      IN button i,
      IN state u
    )

The pointer button is encoded according to Linux Evdev button codes.

May only be called if POINTER access was provided after starting the session.

Available button states:

- `0`: Released

- `1`: Pressed

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

button  
The pointer button was pressed or released

state  
The new state of the button

### org.freedesktop.impl.portal.RemoteDesktop.NotifyPointerAxis

    NotifyPointerAxis (
      IN session_handle o,
      IN options a{sv},
      IN dx d,
      IN dy d
    )

The axis movement from a ‘smooth scroll’ device, such as a touchpad. When applicable, the size of the motion delta should be equivalent to the motion vector of a pointer motion done using the same advice.

May only be called if POINTER access was provided after starting the session.

Supported keys in the `options` vardict include:

- `finish` (`b`)

  If set to true, this is the last axis event in a series, for example as a result of the fingers being lifted from a touchpad after a two-finger scroll. Default is false.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

dx  
Relative axis movement on the x axis

dy  
Relative axis movement on the y axis

### org.freedesktop.impl.portal.RemoteDesktop.NotifyPointerAxisDiscrete

    NotifyPointerAxisDiscrete (
      IN session_handle o,
      IN options a{sv},
      IN axis u,
      IN steps i
    )

May only be called if POINTER access was provided after starting the session.

Available axes:

- `0`: Vertical scroll

- `1`: Horizontal scroll

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

axis  
The axis that was scrolled

steps  
The number of steps scrolled

### org.freedesktop.impl.portal.RemoteDesktop.NotifyKeyboardKeycode

    NotifyKeyboardKeycode (
      IN session_handle o,
      IN options a{sv},
      IN keycode i,
      IN state u
    )

May only be called if KEYBOARD access was provided after starting the session.

Available keyboard keysym states:

- `0`: Released

- `1`: Pressed

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

keycode  
Keyboard code that was pressed or released

state  
New state of keyboard keysym

### org.freedesktop.impl.portal.RemoteDesktop.NotifyKeyboardKeysym

    NotifyKeyboardKeysym (
      IN session_handle o,
      IN options a{sv},
      IN keysym i,
      IN state u
    )

May only be called if KEYBOARD access was provided after starting the session.

Available keyboard keysym states:

- `0`: Released

- `1`: Pressed

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

keysym  
Keyboard symbol that was pressed or released

state  
New state of keyboard keysym

### org.freedesktop.impl.portal.RemoteDesktop.NotifyTouchDown

    NotifyTouchDown (
      IN session_handle o,
      IN options a{sv},
      IN stream u,
      IN slot u,
      IN x d,
      IN y d
    )

May only be called if TOUCHSCREEN access was provided after starting the session.

Notify about a new touch down event. The (x, y) position represents the new touch point position in the streams logical coordinate space (see the `logical_size` stream property in [ScreenCast](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast)).

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

stream  
The PipeWire stream node the coordinate is relative to

slot  
Touch slot where touch point appeared

x  
Touch down x coordinate

y  
Touch down y coordinate

### org.freedesktop.impl.portal.RemoteDesktop.NotifyTouchMotion

    NotifyTouchMotion (
      IN session_handle o,
      IN options a{sv},
      IN stream u,
      IN slot u,
      IN x d,
      IN y d
    )

May only be called if TOUCHSCREEN access was provided after starting the session.

Notify about a new touch motion event. The (x, y) position represents where the touch point position in the streams logical coordinate space moved (see the `logical_size` stream property in [ScreenCast](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast)).

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

stream  
The PipeWire stream node the coordinate is relative to

slot  
Touch slot where touch point appeared

x  
Touch motion x coordinate

y  
Touch motion y coordinate

### org.freedesktop.impl.portal.RemoteDesktop.NotifyTouchUp

    NotifyTouchUp (
      IN session_handle o,
      IN options a{sv},
      IN slot u
    )

May only be called if TOUCHSCREEN access was provided after starting the session.

Notify about a new touch up event.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

slot  
Touch slot where touch point appeared

### org.freedesktop.impl.portal.RemoteDesktop.ConnectToEIS

    ConnectToEIS (
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      OUT fd h
    )

sender libei context

Request a connection to an EIS implementation.

This method is available in version 2 of this interface.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

app_id  
App id of the application

options  
Vardict with optional further information

fd  
A file descriptor to an EIS implementation that can be passed to a
