# ScreenCast

## Description

Screen cast portal

The Screen cast portal allows to create screen cast sessions.

This documentation describes version 6 of this interface.

## Properties

### org.freedesktop.portal.ScreenCast:AvailableSourceTypes

    AvailableSourceTypes readable u

A bitmask of available source types. Currently defined types are:

- `1`: MONITOR: Share existing monitors

- `2`: WINDOW: Share application windows

- `4`: VIRTUAL: Extend with new virtual monitor

### org.freedesktop.portal.ScreenCast:AvailableCursorModes

    AvailableCursorModes readable u

A bitmask of available cursor modes.

Available cursor mode values:

- `1`: Hidden. The cursor is not part of the screen cast stream.

- `2`: Embedded: The cursor is embedded as part of the stream buffers.

- `4`: Metadata: The cursor is not part of the screen cast stream, but sent as PipeWire stream metadata.

This property was added in version 2 of this interface.

### org.freedesktop.portal.ScreenCast:version

    version readable u

## Methods

### org.freedesktop.portal.ScreenCast.CreateSession

    CreateSession (
      IN options a{sv},
      OUT handle o
    )

Create a screen cast session. A successfully created session can at any time be closed using [org.freedesktop.portal.Session.Close](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session-close), or may at any time be closed by the portal implementation, which will be signalled via [org.freedesktop.portal.Session::Closed](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session-closed).

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

### org.freedesktop.portal.ScreenCast.SelectSources

    SelectSources (
      IN session_handle o,
      IN options a{sv},
      OUT handle o
    )

Configure what the screen cast session should record. This method must be called before starting the session.

Passing invalid input to this method will cause the session to be closed. An application may only attempt to select sources once per session.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `types` (`u`)

  Bitmask of what types of content to record. Default is MONITOR.

- `multiple` (`b`)

  Whether to allow selecting multiple sources. Default is no.

- `cursor_mode` (`u`)

  Determines how the cursor will be drawn in the screen cast stream. It must be one of the cursor modes advertised in [org.freedesktop.portal.ScreenCast:AvailableCursorModes](#org-freedesktop-portal-screencast-availablecursormodes). Setting a cursor mode not advertised will cause the screen cast session to be closed. The default cursor mode is ‘Hidden’.

  This option was added in version 2 of this interface.

- `restore_token` (`s`)

  The token to restore a previous session.

  If the stored session cannot be restored, this value is ignored and the user will be prompted normally. This may happen when, for example, the session contains a monitor or a window that is not available anymore, or when the stored permissions are withdrawn.

  The restore token is invalidated after using it once. To restore the same session again, use the new restore token sent in response to starting this session.

  Setting a restore_token is only allowed for screen cast sessions. Persistent remote desktop screen cast sessions can only be handled via the [Remote Desktop](doc-org.freedesktop.portal.RemoteDesktop.md#org-freedesktop-portal-remotedesktop) interface.

  This option was added in version 4 of this interface.

- `persist_mode` (`u`)

  How this session should persist. Default is 0. Accepted values are:

  - `0`: Do not persist (default)

  - `1`: Permissions persist as long as the application is running

  - `2`: Permissions persist until explicitly revoked

  Setting persist_mode is only allowed for screen cast sessions. Persistent remote desktop screen cast sessions can only be handled via the [Remote Desktop](doc-org.freedesktop.portal.RemoteDesktop.md#org-freedesktop-portal-remotedesktop) interface.

  If the permission for the session to persist is granted, a restore token will be returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal of the [org.freedesktop.portal.ScreenCast.Start](#org-freedesktop-portal-screencast-start) method.

  This option was added in version 4 of this interface.

For available source types, see the AvailableSourceTypes property.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.ScreenCast.Start

    Start (
      IN session_handle o,
      IN parent_window s,
      IN options a{sv},
      OUT handle o
    )

Start the screen cast session. This will typically result the portal presenting a dialog letting the user do the selection set up by [org.freedesktop.portal.ScreenCast.SelectSources](#org-freedesktop-portal-screencast-selectsources). An application can only attempt start a session once.

A screen cast session may only be started after having selected sources using [org.freedesktop.portal.ScreenCast.SelectSources](#org-freedesktop-portal-screencast-selectsources).

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `streams` (`a(ua{sv})`)

  An array of PipeWire streams. Each stream consists of a PipeWire node ID (the first element in the tuple, and a Vardict of properties.

  Since version 6 of this interface, the node ID in the stream tuple is deprecated for stream targeting. PipeWire node IDs can be reused after node destruction, so active sessions may misidentify streams across monitor hotplug, resolution or refresh-rate changes, or suspend/resume cycles. Consumers should prefer the `pipewire-serial` property from the stream properties dict and `PW_KEY_TARGET_OBJECT` for connecting to streams. Backends must continue to populate the node ID for compatibility with clients that do not support version 6.

  The array will contain a single stream if ‘multiple’ (see [org.freedesktop.portal.ScreenCast.SelectSources](#org-freedesktop-portal-screencast-selectsources)) was set to ‘false’, or at least one stream if ‘multiple’ was set to ‘true’ as part of the [org.freedesktop.portal.ScreenCast.SelectSources](#org-freedesktop-portal-screencast-selectsources) method.

  Each stream contains the following properties:

  - `id` (`s`)

    Opaque identifier. Will be unique for this stream and local to this session. Will persist with future sessions, if they are restored using a restore token. This property was added in version 4 of this interface. Optional.

  - `position` (`(ii)`)

    A tuple consisting of the position (x, y) in the compositor coordinate space. Note that the position may not be equivalent to a position in a pixel coordinate space. Only available for monitor streams. Optional.

  - `size` (`(ii)`)

    A tuple consisting of (width, height). The size represents the size of the stream as it is displayed in the compositor coordinate space. Note that this size may not be equivalent to a size in a pixel coordinate space. The size may differ from the size of the stream. Optional.

  - `source_type` (`u`)

    The type of the content which is being screen casted. For available source types, see the AvailableSourceTypes property. This property was added in version 3 of this interface.

  - `mapping_id` (`s`)

    An optional identifier used to map different aspects of the resource this stream corresponds to.

    When used in a remote desktop session, the mapping_id can be used to match a libei region of absolute libei devices. There may be multiple absolute libei devices, and each device may have multiple regions, but a mapping_id will only match one of these regions per device.

    This property was added in version 5 of this interface.

  - `pipewire-serial` (`t`)

    The PipeWire `object.serial` for this stream’s node. Unlike the node ID in the stream tuple (which can be reused after node destruction), the serial is a monotonically increasing 64-bit identifier that is never reused. Consumers should prefer the serial for stream targeting via `PW_KEY_TARGET_OBJECT` when available.

    This property was added in version 6 of this interface.

- `restore_token` (`s`)

  The restore token. This token is a single use token that can later be used to restore a session. See [org.freedesktop.portal.ScreenCast.SelectSources](#org-freedesktop-portal-screencast-selectsources) for details.

  This response option was added in version 4 of this interface.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.ScreenCast.OpenPipeWireRemote

    OpenPipeWireRemote (
      IN session_handle o,
      IN options a{sv},
      OUT fd h
    )

Open a file descriptor to the PipeWire remote where the screen cast streams are available. The file descriptor should be used to create a \<classname\>pw_core\</classname\> object, by using \<function\>pw_context_connect_fd\</function\>. Only the screen cast stream nodes will be available from this PipeWire node.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

fd  
File descriptor of an open PipeWire remote.
