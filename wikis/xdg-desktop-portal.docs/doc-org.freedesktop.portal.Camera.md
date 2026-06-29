# Camera

## Description

Camera portal

The camera portal enables applications to access camera devices, such as web cams.

## Properties

### org.freedesktop.portal.Camera:IsCameraPresent

    IsCameraPresent readable b

A boolean stating whether there is any cameras available.

### org.freedesktop.portal.Camera:version

    version readable u

## Methods

### org.freedesktop.portal.Camera.AccessCamera

    AccessCamera (
      IN options a{sv},
      OUT handle o
    )

Request to gain access to the camera.

Supported keys in the `options` vardict include:

- `handle_token` (`s`) A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

Following the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal, if granted, [org.freedesktop.portal.Camera.OpenPipeWireRemote](#org-freedesktop-portal-camera-openpipewireremote) can be used to open a PipeWire remote.

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.Camera.OpenPipeWireRemote

    OpenPipeWireRemote (
      IN options a{sv},
      OUT fd h
    )

Open a file descriptor to the PipeWire remote where the camera nodes are available. The file descriptor should be used to create a `pw_core` object, by using `pw_context_connect_fd()`.

This method will only succeed if the application already has permission to access camera devices.

There are currently no supported keys in the `options` vardict.

options  
Vardict with optional further information

fd  
File descriptor of an open PipeWire remote.
