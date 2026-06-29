# File Transfer

## Description

Portal for transferring files between apps

The [org.freedesktop.portal.FileTransfer](#org-freedesktop-portal-filetransfer) portal operates as a middle-man between apps when transferring files via drag-and-drop or copy-paste, taking care of the necessary exporting of files in the document portal.

Toolkits are expected to use the application/vnd.portal.filetransfer mimetype when using this mechanism for file exchange via copy-paste or drag-and-drop.

The data that is transmitted with this mimetype should be the key returned by the [org.freedesktop.portal.FileTransfer.StartTransfer](#org-freedesktop-portal-filetransfer-starttransfer) method. Upon receiving this mimetype, the target should call [org.freedesktop.portal.FileTransfer.RetrieveFiles](#org-freedesktop-portal-filetransfer-retrievefiles) with the key, to obtain the list of files. The portal will take care of exporting files in the document store as necessary to make them accessible to the target.

Files added to the [Documents portal](doc-org.freedesktop.portal.Documents.md#org-freedesktop-portal-documents) by this portal do not stay accessible across sessions.

The D-Bus interface for the this portal is available under the bus name org.freedesktop.portal.Documents and the object path `/org/freedesktop/portal/documents`.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.portal.FileTransfer:version

    version readable u

## Methods

### org.freedesktop.portal.FileTransfer.StartTransfer

    StartTransfer (
      IN options a{sv},
      OUT key s
    )

Starts a session for a file transfer.

The caller should call [org.freedesktop.portal.FileTransfer.AddFiles](#org-freedesktop-portal-filetransfer-addfiles) at least once, to add files to this session.

Another application can then call [org.freedesktop.portal.FileTransfer.RetrieveFiles](#org-freedesktop-portal-filetransfer-retrievefiles) to obtain them, if it has the `key`.

Supported keys in the `options` vardict include:

- `writable` (`b`)

  Whether to allow the chosen application to write to the files.

  This key only takes effect for files that need to be exported in the document portal for the receiving app. But it does require the passed-in file descriptors to be writable.

  Default: False

- `autostop` (`b`)

  Whether to stop the transfer automatically after the first [org.freedesktop.portal.FileTransfer.RetrieveFiles](#org-freedesktop-portal-filetransfer-retrievefiles) call.

  Default: True

options  
Vardict with optional further information

key  
a key that needs to be passed to [org.freedesktop.portal.FileTransfer.RetrieveFiles](#org-freedesktop-portal-filetransfer-retrievefiles) to obtain the files

### org.freedesktop.portal.FileTransfer.AddFiles

    AddFiles (
      IN key s,
      IN fds ah,
      IN options a{sv}
    )

Adds files or directories to a session. This method can be called multiple times on a given session. Either regular files or directories can be added.

Note that the session bus often has a low limit of file descriptors per message (typically, 16), so you may have to send large lists with multiple [org.freedesktop.portal.FileTransfer.AddFiles](#org-freedesktop-portal-filetransfer-addfiles) calls.

The `options` vardict currently has no supported entries.

key  
A key returned by [org.freedesktop.portal.FileTransfer.StartTransfer](#org-freedesktop-portal-filetransfer-starttransfer)

fds  
File descriptors for the files or directories to register

options  
Vardict with optional further information

### org.freedesktop.portal.FileTransfer.RetrieveFiles

    RetrieveFiles (
      IN key s,
      IN options a{sv},
      OUT files as
    )

Retrieves files or directories that were previously added to the session with [org.freedesktop.portal.FileTransfer.AddFiles](#org-freedesktop-portal-filetransfer-addfiles). The files or directories will be exported in the document portal as-needed for the caller, and they will be writable if the owner of the session allowed it.

After the first [org.freedesktop.portal.FileTransfer.RetrieveFiles](#org-freedesktop-portal-filetransfer-retrievefiles) call, the session will be closed by the portal, unless `autostop` has been set to False.

The `options` vardict currently has no supported entries.

key  
A key returned by [org.freedesktop.portal.FileTransfer.StartTransfer](#org-freedesktop-portal-filetransfer-starttransfer)

options  
Vardict with optional further information

files  
list of paths

### org.freedesktop.portal.FileTransfer.StopTransfer

    StopTransfer (
      IN key s
    )

Ends the transfer. Further calls to [org.freedesktop.portal.FileTransfer.AddFiles](#org-freedesktop-portal-filetransfer-addfiles) or [org.freedesktop.portal.FileTransfer.RetrieveFiles](#org-freedesktop-portal-filetransfer-retrievefiles) for this key will return an error.

key  
A key returned by [org.freedesktop.portal.FileTransfer.StartTransfer](#org-freedesktop-portal-filetransfer-starttransfer)

## Signals

### org.freedesktop.portal.FileTransfer::TransferClosed

    TransferClosed (
      key s
    )

The TransferClosed signal is emitted to the caller of StartTransfer when the transfer is closed.

key  
key returned by StartTransfer
