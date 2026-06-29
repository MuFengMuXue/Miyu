# Usb

## Description

Portal for USB device access

This interface lets sandboxed applications monitor and request access to connected USB devices.

Applications should prefer specialized portals for specific device types, such as the Camera portal for cameras.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.portal.Usb:version

    version readable u

## Methods

### org.freedesktop.portal.Usb.CreateSession

    CreateSession (
      IN options a{sv},
      OUT session_handle o
    )

Creates an USB monitoring session. This is only necessary to receive device events, like device being plugged or unplugged.

Supported keys in the `options` vardict include:

- `session_handle_token` (`s`)

  A string that will be used as the last element of the session handle. Must be a valid object path element. See the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) documentation for more information about the session handle.

options  
Vardict with optional further information

session_handle  
Object path for the session.

### org.freedesktop.portal.Usb.EnumerateDevices

    EnumerateDevices (
      IN options a{sv},
      OUT devices a(sa{sv})
    )

no option supported.

Enumerates all connected USB devices that this application has permission to see.

The following results are returned in the `device` vardict:

- `id` (`s`)

  Each element of the `devices` array contains the device ID, and a device information vardict with the following keys:

- `parent` (`s`)

  Device ID of the parent device.

- `readable` (`b`)

  Whether the device can be opened for reading with [org.freedesktop.portal.Usb.AcquireDevices](#org-freedesktop-portal-usb-acquiredevices). If not present, then it should be assumed to be false.

- `writable` (`b`)

  Whether the device can be opened for writing with [org.freedesktop.portal.Usb.AcquireDevices](#org-freedesktop-portal-usb-acquiredevices). If not present, then it should be assumed to be false.

- `device-file` (`s`)

  A string path to the device node inside the /dev filesystem.

- `properties` (`a{sv}`)

  A list of udev properties that this device has. These properties are not parsed in any way by the portal, it is up to apps to parse them.

options  
Vardict with optional further information. There is currently

devices

### org.freedesktop.portal.Usb.AcquireDevices

    AcquireDevices (
      IN parent_window s,
      IN devices a(sa{sv}),
      IN options a{sv},
      OUT handle o
    )

Request to acquires (i.e. open) the given device nodes. The process of acquiring is finished by calling FinishAcquireDevices after the request emitted a Success response.

Each element of the `devices` array contains the device ID, and an access option vardict with the following keys:

- `writable` (`b`)

  Whether the device will be opened in read-write or read-only mode. Default: False

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

The [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal is emitted without any extra information.

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

devices  
Array of device identifiers and access options

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.Usb.FinishAcquireDevices

    FinishAcquireDevices (
      IN handle o,
      IN options a{sv},
      OUT results a(sa{sv}),
      OUT finished b
    )

Retrieves the file descriptors of the devices requested during [org.freedesktop.portal.Usb.AcquireDevices](#org-freedesktop-portal-usb-acquiredevices). The file descriptors remain usable until the underlying device is removed, they are released with ReleaseDevices, the D-Bus connections is closed, or the portal revokes the file descriptor which can happen at any point. Devices which are not needed anymore should be passed to ReleaseDevices.

If not all devices could be send, `finished` will be false and org.freedesktop.portal.Usb.FinishAcquireDevices must be called again until `finished` is true, before calling org.freedesktop.portal.Usb.AcquireDevices again.

This method can only be called once for a given token, and only after calling [org.freedesktop.portal.Usb.AcquireDevices](#org-freedesktop-portal-usb-acquiredevices).

Each element of the `results` array contains the device ID, and a vardict with the following keys:

- `success` (`b`)

  Whether the device access was successful or not.

- `fd` (`h`)

  The file descriptor representing the device. The file descriptor is meant to be passed on to the USB library.

  Only present if this was a successful device access.

- `error` (`s`)

  Error message describing why accessing the device was not successful. Only present if this was an failed device access.

There are no supported keys in the `options` vardict.

handle  
The request object path for the acquisition to finish

options  
Vardict with optional further information

results  
Array of device ids, and the result of the access

finished  
Whether all device results were reported

### org.freedesktop.portal.Usb.ReleaseDevices

    ReleaseDevices (
      IN devices as,
      IN options a{sv}
    )

Releases previously acquired devices. The file descriptors of those devices might become unusable as a result of this.

Each element of the `devices` array contains the device ID of the device.

There are no supported keys in the `options` vardict.

devices  
Array of device identifiers

options  
Vardict with optional further information

## Signals

### org.freedesktop.portal.Usb::DeviceEvents

    DeviceEvents (
      session_handle o,
      events a(ssa{sv})
    )

The DeviceEvents signal is emitted when one or more USB devices have been added, changed, or removed. This signal is only emitted for active sessions created with [org.freedesktop.portal.Usb.CreateSession](#org-freedesktop-portal-usb-createsession).

Each element of the `events` array is composed of the following fields:

- `action` (`s`)

  Type of event that occurred. One of “add”, “change”, or “remove”.

- `id` (`s`)

  Device ID that the event occurred on.

- `device` (`a{sv}`)

  Device properties attached to the ID. See [org.freedesktop.portal.Usb.EnumerateDevices](#org-freedesktop-portal-usb-enumeratedevices) for a list of all the properties that may be present in the vardict.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

events  
A list of events which occurred.
