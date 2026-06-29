# Remote Desktop

## Description

Remote desktop portal

The Remote desktop portal allows to create remote desktop sessions.

This documentation describes version 2 of this interface.

## Properties

### org.freedesktop.portal.RemoteDesktop:AvailableDeviceTypes

    AvailableDeviceTypes readable u

A bitmask of available source types. Currently defined types are:

- `1`: KEYBOARD

- `2`: POINTER

- `4`: TOUCHSCREEN

### org.freedesktop.portal.RemoteDesktop:version

    version readable u

## Methods

### org.freedesktop.portal.RemoteDesktop.CreateSession

    CreateSession (
      IN options a{sv},
      OUT handle o
    )

Create a remote desktop session.

A remote desktop session is used to allow remote controlling a desktop session.

A remote desktop session may only be started and stopped with this interface, but you can use the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object created with this method together with certain methods on the [ScreenCast](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast) and [Clipboard](doc-org.freedesktop.portal.Clipboard.md#org-freedesktop-portal-clipboard) interfaces. Specifically, you can call [org.freedesktop.portal.ScreenCast.SelectSources](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast-selectsources) to also get screen content, and [org.freedesktop.portal.ScreenCast.OpenPipeWireRemote](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast-openpipewireremote) to acquire a file descriptor for a PipeWire remote. See [ScreenCast](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast) for more information on how to use those methods. To capture clipboard content, you can call [org.freedesktop.portal.Clipboard.RequestClipboard](doc-org.freedesktop.portal.Clipboard.md#org-freedesktop-portal-clipboard-requestclipboard). See [Clipboard](doc-org.freedesktop.portal.Clipboard.md#org-freedesktop-portal-clipboard) for more information on the clipboard integration.

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

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.RemoteDesktop.SelectDevices

    SelectDevices (
      IN session_handle o,
      IN options a{sv},
      OUT handle o
    )

Select input devices to remote control.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `types` (`u`)

  Bitmask of what device types to request remote controlling of. Default is all.

- `restore_token` (`s`)

  The token to restore a previous session.

  If the stored session cannot be restored, this value is ignored and the user will be prompted normally. This may happen when, for example, the session contains a monitor or a window that is not available anymore, or when the stored permissions are withdrawn.

  The restore token is invalidated after using it once. To restore the same session again, use the new restore token sent in response to starting this session.

  This option was added in version 2 of this interface.

- `persist_mode` (`u`)

  How this session should persist. Default is 0. Accepted values are:

  - `0`: Do not persist (default)

  - `1`: Permissions persist as long as the application is running

  - `2`: Permissions persist until explicitly revoked

  If the permission for the session to persist is granted, a restore token will be returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal of the start method used to start the session.

  This option was added in version 2 of this interface.

For available device types, see the AvailableDeviceTypes property.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.RemoteDesktop.Start

    Start (
      IN session_handle o,
      IN parent_window s,
      IN options a{sv},
      OUT handle o
    )

Start the remote desktop session. This will typically result in the portal presenting a dialog letting the user select what to share, including devices and optionally screen content if screen cast sources was selected.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `devices` (`u`)

  A bitmask of the devices selected by the user.

- `clipboard_enabled` (`b`)

  A boolean for whether the clipboard was enabled (‘true’) or not (‘false’). See the [Clipboard](doc-org.freedesktop.portal.Clipboard.md#org-freedesktop-portal-clipboard) documentation for more information. Since version 2.

- `streams` (`a(ua{sv})`)

  An array of PipeWire streams. Each stream consists of a PipeWire node ID (the first element in the tuple, and a Vardict of properties. See [org.freedesktop.portal.ScreenCast.Start](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast-start) for details.

- `restore_token` (`s`)

  The restore token. This token is a single use token that can later be used to restore a session. See [org.freedesktop.portal.RemoteDesktop.SelectDevices](#org-freedesktop-portal-remotedesktop-selectdevices) for details.

  This response option was added in version 2 of this interface.

If a screen cast source was selected, the results of the [org.freedesktop.portal.ScreenCast.Start](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast-start) response signal may be included.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.RemoteDesktop.NotifyPointerMotion

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

### org.freedesktop.portal.RemoteDesktop.NotifyPointerMotionAbsolute

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

### org.freedesktop.portal.RemoteDesktop.NotifyPointerButton

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

### org.freedesktop.portal.RemoteDesktop.NotifyPointerAxis

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

### org.freedesktop.portal.RemoteDesktop.NotifyPointerAxisDiscrete

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

### org.freedesktop.portal.RemoteDesktop.NotifyKeyboardKeycode

    NotifyKeyboardKeycode (
      IN session_handle o,
      IN options a{sv},
      IN keycode i,
      IN state u
    )

May only be called if KEYBOARD access was provided after starting the session.

Available keyboard keycode states:

- `0`: Released

- `1`: Pressed

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

keycode  
Keyboard code that was pressed or released

state  
New state of keyboard keycode

### org.freedesktop.portal.RemoteDesktop.NotifyKeyboardKeysym

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

### org.freedesktop.portal.RemoteDesktop.NotifyTouchDown

    NotifyTouchDown (
      IN session_handle o,
      IN options a{sv},
      IN stream u,
      IN slot u,
      IN x d,
      IN y d
    )

May only be called if TOUCHSCREEN access was provided after starting the session.

Notify about a new touch down event. The (x, y) position represents the new touch point position in the streams logical coordinate space (see the logical_size stream property in [ScreenCast](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast)).

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

### org.freedesktop.portal.RemoteDesktop.NotifyTouchMotion

    NotifyTouchMotion (
      IN session_handle o,
      IN options a{sv},
      IN stream u,
      IN slot u,
      IN x d,
      IN y d
    )

May only be called if TOUCHSCREEN access was provided after starting the session.

Notify about a new touch motion event. The (x, y) position represents where the touch point position in the streams logical coordinate space moved (see the logical_size stream property in [ScreenCast](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast)).

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

### org.freedesktop.portal.RemoteDesktop.NotifyTouchUp

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

### org.freedesktop.portal.RemoteDesktop.ConnectToEIS

    ConnectToEIS (
      IN session_handle o,
      IN options a{sv},
      OUT fd h
    )

Request a connection to an EIS implementation. The returned handle can be passed to ei_setup_backend_fd() for a libei sender context to complete the connection. All information about available devices and the event flow is subject to libei. Please see the libei documentation for details.

This method may only be called once per session, where the EIS implementation disconnects the session should be closed.

This method must be called after [org.freedesktop.portal.RemoteDesktop.Start](#org-freedesktop-portal-remotedesktop-start)

Once an EIS connection is established, input events must be sent exclusively via the EIS connection. Any events submitted via NotifyPointerMotion, NotifyKeyboardKeycode and other Notify\* methods will return an error.

To see how to pair a PipeWire stream with a libei device region, see the documentation for the `mapping_id` stream property in [org.freedesktop.portal.ScreenCast.Start](doc-org.freedesktop.portal.ScreenCast.md#org-freedesktop-portal-screencast-start).

This method was added in version 2 of this interface.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

fd  
A file descriptor to an EIS implementation that can be passed to a libei sender context
