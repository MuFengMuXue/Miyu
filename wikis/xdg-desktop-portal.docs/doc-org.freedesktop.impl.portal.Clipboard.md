# Clipboard

## Description

## Properties

### org.freedesktop.impl.portal.Clipboard:version

    version readable u

## Methods

### org.freedesktop.impl.portal.Clipboard.RequestClipboard

    RequestClipboard (
      IN session_handle o,
      IN options a{sv}
    )

Requests clipboard access for the given portal session. This request must be made before the session starts. The session must be started, before using any other method in this interface which take a session. Note that other interfaces might place restriction on when it’s possible to interact with the clipboard.

This portal does NOT create it’s own session. Instead, it offers existing sessions created from other portals the option to integrate with the clipboard.

For whether this interface is supported for a given session, refer to that portal’s documentation. See [Remote Desktop](doc-org.freedesktop.portal.RemoteDesktop.md#org-freedesktop-portal-remotedesktop) to integrate clipboard with the remote desktop session. See [Input Capture](doc-org.freedesktop.portal.InputCapture.md#org-freedesktop-portal-inputcapture) to integrate clipboard with the input capture session.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

### org.freedesktop.impl.portal.Clipboard.SetSelection

    SetSelection (
      IN session_handle o,
      IN options a{sv}
    )

Sets the owner of the clipboard formats in ‘mime_types’ in `options` to the session, i.e. this session has data for the advertised clipboard formats.

See [File Transfer](doc-org.freedesktop.portal.FileTransfer.md#org-freedesktop-portal-filetransfer) to transfer files using the ‘application/vnd.portal.filetransfer’ mimetype.

May only be called if clipboard access was given after starting the session.

Supported keys in the `options` vardict include:

- `mime_types` (`as`)

  A list of mime types that the session has clipboard content for.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

### org.freedesktop.impl.portal.Clipboard.SelectionWrite

    SelectionWrite (
      IN session_handle o,
      IN serial u,
      OUT fd h
    )

Answer to ‘SelectionTransfer’ signal. Transfers the clipboard content for the given serial to the method callee via a file descriptor. It is the Callee that creates the file descriptor.

May only be called if clipboard access was given after starting the session.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

serial  
The serial of the request where this answer is directed towards

fd  
A UnixFD handle to the contents of the selection being written to

### org.freedesktop.impl.portal.Clipboard.SelectionWriteDone

    SelectionWriteDone (
      IN session_handle o,
      IN serial u,
      IN success b
    )

Notifies that the transfer of the clipboard data has either completed successfully, or failed.

May only be called if clipboard access was given after starting the session.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

serial  
The serial of the request where this answer is directed to

success  
A boolean which indicates whether the transfer of the clipboard data was successful (true’) or not (‘false’)

### org.freedesktop.impl.portal.Clipboard.SelectionRead

    SelectionRead (
      IN session_handle o,
      IN mime_type s,
      OUT fd h
    )

Transfer the clipboard content given the specified mime type to the method caller via a file descriptor. It is the callee that creates the file descriptor.

May only be called if clipboard access was given after starting the session.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

mime_type  
The mime-type string of the requested format

fd  
A UnixFD handle to the contents of the selection being read

## Signals

### org.freedesktop.impl.portal.Clipboard::SelectionOwnerChanged

    SelectionOwnerChanged (
      session_handle o,
      options a{sv}
    )

Notifies the session that the clipboard selection has changed.

Caller will only be notified if clipboard access was given after starting the session.

Supported keys in the `options` vardict include:

- `mime_types` (`as`)

  A list of mime types that the the new clipboard selection has content for.

- `session_is_owner` (`b`)

  A boolean for whether the session is the owner of the clipboard selection (`true`) or not (`false`).

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

options  
Vardict with optional further information

### org.freedesktop.impl.portal.Clipboard::SelectionTransfer

    SelectionTransfer (
      session_handle o,
      mime_type s,
      serial u
    )

Notifies the session of a request for clipboard content of the given mime type. The callee provides a serial to track the request, which any [org.freedesktop.portal.Clipboard.SelectionWrite](doc-org.freedesktop.portal.Clipboard.md#org-freedesktop-portal-clipboard-selectionwrite) responses must use.

Once the caller is done handling the ‘SelectionTransfer’ request, they must call [org.freedesktop.portal.Clipboard.SelectionWriteDone](doc-org.freedesktop.portal.Clipboard.md#org-freedesktop-portal-clipboard-selectionwritedone) with the corresponding request’s serial and whether the request completed successfully. If the request is not handled, the caller should respond by setting ‘success’ to ‘false’.

Caller will only be notified if clipboard access was given after starting the session.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

mime_type  
The mime-type string of the requested format

serial  
The serial used to track this transfer, to which the answer of this request must use
