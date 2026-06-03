# Usb

## Description

USB portal backend interface

This interface lets sandboxed applications monitor and request access to connected USB devices.

The implementation side allows requesting permission from the user to access USB devices with a GUI.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.impl.portal.Usb:version

    version readable u

## Methods

### org.freedesktop.impl.portal.Usb.AcquireDevices

    AcquireDevices (
      IN handle o,
      IN parent_window s,
      IN app_id s,
      IN devices a(sa{sv}a{sv}),
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Selects the devices to open.

Each element of the `devices` array contains the ID, information and access options for each device the app wants to acquire. The supported keys in the information vardict are the same as the keys in the `devices` vardict of [org.freedesktop.portal.Usb.EnumerateDevices](doc-org.freedesktop.portal.Usb.md#org-freedesktop-portal-usb-enumeratedevices).

The supported keys in the access options vardict are:

- `writable` (`b`)

  Whether the device will be opened in read-write or read-only mode. Default: False

There are no supported keys in the `options` vardict.

The following results get returned via the `results` vardict:

- `devices` (`a(sa{sv})`)

  An array of identifier and access options which is a subset of what was passed in via `devices`.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

app_id  
App id of the application

devices  
Array of identifier, device information, and access options for each device

options  
Vardict with optional further information

response  
Numeric Request response

results  
Vardict with the results of the call
