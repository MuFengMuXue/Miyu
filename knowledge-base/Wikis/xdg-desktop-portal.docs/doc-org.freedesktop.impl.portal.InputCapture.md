# Input Capture

## Description

Input Capture portal backend interface

The Input Capture portal allows clients to capture input from local devices. This portal is mostly a 1:1 mapping of the [Input Capture](doc-org.freedesktop.portal.InputCapture.md#org-freedesktop-portal-inputcapture) portal, see that portal’s documentation for details on methods, signals and arguments.

This documentation describes version 2 of this interface.

## Properties

### org.freedesktop.impl.portal.InputCapture:SupportedCapabilities

    SupportedCapabilities readable u

A bitmask of supported capabilities. This list is constant, it is not the list of capabilities currently available but rather which capabilities are implemented by the portal.

Applications must ignore unknown capabilities.

Currently defined types are:

- `1`: KEYBOARD

- `2`: POINTER

- `4`: TOUCHSCREEN

### org.freedesktop.impl.portal.InputCapture:version

    version readable u

## Methods

### org.freedesktop.impl.portal.InputCapture.CreateSession

    CreateSession (
      IN handle o,
      IN session_handle o,
      IN app_id s,
      IN parent_window s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

This method was deprecated in version 2 of this interface and will not be called by the frontend if the implementation indicates support for version 2. See CreateSession2 instead.

Create an input capture session.

Supported keys in the `options` vardict include:

- `capabilities` (`u`)

  Bitmask of requested capabilities, see the SupportedCapabilities property. This value is required.

The following results get returned in the `results` vardict:

- `session_id` (`s`)

  The session id. A string representing the created input capture session.

- `capabilities` (`u`)

  The capabilities available to this session. This is always a subset of the requested capabilities.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session being created

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

### org.freedesktop.impl.portal.InputCapture.CreateSession2

    CreateSession2 (
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      OUT results a{sv}
    )

Create an input capture session. In contrast with CreateSession, the created session is not in the started state.

There are currently no supported keys in the `options` vardict.

There are currently no supported keys in the `results` vardict.

This method was added in version 2 of this interface.

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session being created

app_id  
App id of the application

options  
Vardict with optional further information

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.InputCapture.Start

    Start (
      IN handle o,
      IN session_handle o,
      IN app_id s,
      IN parent_window s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Start the input capture session. This will typically result in the portal presenting a dialog letting the user decide whether they want to allow the input of the session to be captured, and what capabilities to support.

This method may only be called once on a session previously created with CreateSession2. Sessions created by the deprecated CreateSession are immediately started.

Supported keys in the `options` vardict include:

- `capabilities` (`u`)

  Bitmask of requested capabilities, see the SupportedCapabilities property. This value is required and must not be zero.

- `restore_data` (`(suv)`)

  The data to restore from a previous session.

  If the stored session cannot be restored, this value is ignored and the user will be prompted normally. This may happen when, for example, the session contains capabilities that are not available anymore, or when the stored permissions are withdrawn.

  The restore data is composed of the vendor name (e.g. “GNOME” or “KDE”), the version of the implementation-specific private data, and the implementation-specific private data itself.

  This option was added in version 2 of this interface.

- `persist_mode` (`u`)

  How this session should persist. Default is 0. Accepted values are:

  - `0`: Do not persist (default)

  - `1`: Permissions persist as long as the application is running

  - `2`: Permissions persist until explicitly revoked

  If the permission for the session to persist is granted, `restore_data` will be returned in the `results` vardict of the [org.freedesktop.impl.portal.InputCapture.Start](#org-freedesktop-impl-portal-inputcapture-start) method.

  This option was added in version 2 of this interface.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `capabilities` (`u`)

  The capabilities available to this session. This is always a subset of the requested capabilities. See the SupportedCapabilities property for details. Note that while a capability may be available to a session, there is no guarantee a device with that capability is currently available or if one does become available that it will trigger input capture.

  It is best to view this set as a negative confirmation - a capability that was requested but is missing is an indication that this application may not capture events of that capability.

- `clipboard_enabled` (`b`)

  A boolean for whether the clipboard was enabled (‘true’) or not (‘false’). See the [Clipboard](doc-org.freedesktop.portal.Clipboard.md#org-freedesktop-portal-clipboard) documentation for more information.

- `restore_data` (`(suv)`)

  The data for this session to store in the XDG Portal, for a session with a `persist_mode` other than zero. If this session is restored in the future, this data is used as the `restore_data` argument in the `options` vardict.

  This option was added in version 2 of this interface.

This method was added in version 2 of this interface.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

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

### org.freedesktop.impl.portal.InputCapture.GetZones

    GetZones (
      IN handle o,
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Return the current zones for this session.

The following results get returned in the `results` vardict:

- `zones` (`a(uuii)`)

  An array of zones with width, height, x-offset, y-offset.

- `zone_set` (`u`)

  The zone_set ID required in [org.freedesktop.impl.portal.InputCapture.SetPointerBarriers](#org-freedesktop-impl-portal-inputcapture-setpointerbarriers).

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

### org.freedesktop.impl.portal.InputCapture.SetPointerBarriers

    SetPointerBarriers (
      IN handle o,
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      IN barriers aa{sv},
      IN zone_set u,
      OUT response u,
      OUT results a{sv}
    )

Set up zero or more pointer barriers.

Supported keys in the `barriers` vardicts include:

- `barrier_id` (`u`)

  The non-zero id of this barrier. This id is used in the \#org.freedesktop.portal.impl.InputCapture::Activated signal to inform which barrier triggered input capture.

- `position` (`(iiii)`)

  The x1/y1 x2/y2 position of the pointer barrier. A horizontal pointer barrier must have y1 == y2, a vertical pointer barrier must have x1 == x2. Diagonal pointer barriers are not supported.

The following results get returned in the `results` vardict:

- `failed_barriers` (`au`)

  An array of barrier_ids of pointer barriers that have been denied. The id matches the barrier_id of the entries in the `barriers` argument.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

app_id  
App id of the application

options  
Vardict with optional further information

barriers  
An array of vardicts, each specifying one barrier

zone_set  
A unique ID referring to the zone set

response  
Numeric response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.InputCapture.Enable

    Enable (
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Enable input capturing.

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

app_id  
App id of the application

options  
Vardict with optional further information

response

results

### org.freedesktop.impl.portal.InputCapture.Disable

    Disable (
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Disable input capturing.

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

app_id  
App id of the application

options  
Vardict with optional further information

response

results

### org.freedesktop.impl.portal.InputCapture.Release

    Release (
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Release ongoing input capturing.

Supported keys in the `options` vardict include:

- `activation_id` (`u`)

  The same activation_id number as in the [org.freedesktop.impl.portal.InputCapture::Activated](#org-freedesktop-impl-portal-inputcapture-activated) signal.

- `cursor_position` (`(dd)`)

  The suggested cursor position within the Zones available in this session.

  This is a suggestion to the compositor to place the cursor in the correct position to allow for fluent movement between virtual screens. The compositor is not required to honor this suggestion.

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

app_id  
App id of the application

options  
Vardict with optional further information

response

results

### org.freedesktop.impl.portal.InputCapture.ConnectToEIS

    ConnectToEIS (
      IN session_handle o,
      IN app_id s,
      IN options a{sv},
      OUT fd h
    )

Set up the connection to an EIS implementation. Once input capturing starts, input events are sent via the EI protocol between the compositor and the application. This call must be invoked before [org.freedesktop.portal.InputCapture.Enable](doc-org.freedesktop.portal.InputCapture.md#org-freedesktop-portal-inputcapture-enable).

A session only needs to set this up once, the EIS implementation is not affected by calls to Disable() and [org.freedesktop.portal.InputCapture.Enable](doc-org.freedesktop.portal.InputCapture.md#org-freedesktop-portal-inputcapture-enable) - the same context can be re-used until the session is closed.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

app_id  
App id of the application

options  
Vardict with optional further information

fd  
A file descriptor to an EIS implementation that can be passed to a passive libei context

## Signals

### org.freedesktop.impl.portal.InputCapture::Disabled

    Disabled (
      session_handle o,
      options a{sv}
    )

The Disabled signal is emitted when the application will no longer receive captured input. If input capturing is currently ongoing, the [org.freedesktop.impl.portal.InputCapture::Deactivated](#org-freedesktop-impl-portal-inputcapture-deactivated) signal is emitted before this signal.

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

options  
Vardict with optional further information

### org.freedesktop.impl.portal.InputCapture::Activated

    Activated (
      session_handle o,
      options a{sv}
    )

The Activated signal is emitted when input capture starts and input events are about to be sent to the application.

This signal is only emitted after a prior call to [org.freedesktop.impl.portal.InputCapture.Enable](#org-freedesktop-impl-portal-inputcapture-enable).

Supported keys in the `options` vardict include:

- `activation_id` (`u`)

  A number that can be used to synchronize with the transport-layer. This number has no intrinsic meaning but is guaranteed to increase by an unspecified amount on each call.

  In particular: if the compositor sends an activation_id of N as part of this request it will also set the sequence in EIS’ start_emulating event the same value N on the EIS connection before the first event from a device is sent. This allows an application to have a synchronization point and attribute an event sequence to the portal interaction.

  Applications must be able to handle the activation_id number wrapping around. Implementations of this portal must to increase the activation_id number by an sensible amount to allow for wrapping detection.

- `cursor_position` (`(dd)`)

  The current cursor position. Note that this position may be outside the Zones available to this session - this indicates movement larger than a single pixel.

  For example, a fast movement against a barrier on the right edge of a screen may logically put the cursor dozens of pixels into the (non-existing) screen on the other side of the barrier. It is the application’s responsibility to adjust the cursor position as necessary.

- `barrier_id` (`u`)

  The barrier id of the barrier that triggered. If the value is nonzero, it matches the barrier id as specified in [org.freedesktop.impl.portal.InputCapture.SetPointerBarriers](#org-freedesktop-impl-portal-inputcapture-setpointerbarriers).

  If the id is zero, the pointer barrier could be determined. If the id is missing, the input capture was not triggered by a pointer barrier.

  Where more than one pointer barrier are triggered by the same movement it is up to the compositor to choose one barrier (or use a barrier id of zero).

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

options  
Vardict with optional further information

### org.freedesktop.impl.portal.InputCapture::Deactivated

    Deactivated (
      session_handle o,
      options a{sv}
    )

The Deactivated signal is emitted when input capture stopped and input events are no longer sent to the application. To prevent future input capture, an application must call [org.freedesktop.portal.InputCapture.Disable](doc-org.freedesktop.portal.InputCapture.md#org-freedesktop-portal-inputcapture-disable).

Supported keys in the `options` vardict include:

- `activation_id` (`u`)

  The same activation_id as in the corresponding [org.freedesktop.impl.portal.InputCapture::Activated](#org-freedesktop-impl-portal-inputcapture-activated) signal.

- `cursor_position` (`(dd)`)

  The current cursor position. Note that this position may be outside the Zones available to this session - this indicates movement larger than a single pixel.

  For example, a fast movement against a barrier on the right edge of a screen may logically put the cursor dozens of pixels into the (non-existing) screen on the other side of the barrier. It is the application’s responsibility to adjust the cursor position as necessary.

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

options  
Vardict with optional further information

### org.freedesktop.impl.portal.InputCapture::ZonesChanged

    ZonesChanged (
      session_handle o,
      options a{sv}
    )

The ZonesChanged signal is emitted when one or more of the zones available **to this session** change. An application should immediately call [org.freedesktop.portal.InputCapture.GetZones](doc-org.freedesktop.portal.InputCapture.md#org-freedesktop-portal-inputcapture-getzones) to update its state of the zones.

session_handle  
Object path for the [Session](doc-org.freedesktop.impl.portal.Session.md#org-freedesktop-impl-portal-session) object representing the session

options  
Vardict with optional further information
