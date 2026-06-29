# File Chooser

## Description

File chooser portal backend interface

The FileChooser portal allows sandboxed applications to ask the user for access to files outside the sandbox. The portal backend will present the user with a file chooser dialog.

Backends must normalize URIs of locations selected by the user into “[file://](file://)” URIs. URIs that cannot be normalized should be discarded.

## Methods

### org.freedesktop.impl.portal.FileChooser.OpenFile

    OpenFile (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN title s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Presents a file chooser dialog to the user to open one or more files.

Supported keys in the `options` vardict include:

- `accept_label` (`s`)

  The label for the accept button. Mnemonic underlines are allowed.

- `modal` (`b`)

  Whether to make the dialog modal. Default is yes.

- `multiple` (`b`)

  Whether to allow selection of multiple files. Default is no.

- `directory` (`b`)

  Whether to select for folders instead of files. Default is to select files.

- `filters` (`a(sa(us))`)

  A list of serialized file filters. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

- `current_filter` (`(sa(us))`)

  Request that this filter be set by default at dialog creation. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

- `choices` (`a(ssa(ss)s)`)

  A list of serialized combo boxes. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

- `current_folder` (`ay`)

  A suggested folder to open the files from. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

The following results get returned via the `results` vardict:

- `uris` (`as`)

  An array of strings containing the uris of the selected files. All URIs must have the `file://` scheme.

- `choices` (`a(ss)`)

  An array of pairs of strings, corresponding to the passed-in choices. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

- `current_filter` (`(sa(us))`)

  The filter that was selected. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

- `writable` (`b`)

  Whether the file is opened with write access. Default is `false`.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

app_id  
App id of the application

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

title  
Title for the file chooser dialog

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.FileChooser.SaveFile

    SaveFile (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN title s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Presents a file chooser dialog to the user to save a file.

Supported keys in the `options` vardict include:

- `accept_label` (`s`)

  The label for the accept button. Mnemonic underlines are allowed.

- `modal` (`b`)

  Whether to make the dialog modal. Default is yes.

- `filters` (`a(sa(us))`)

  A list of serialized file filters. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

- `current_filter` (`(sa(us))`)

  Request that this filter be set by default at dialog creation. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

- `choices` (`a(ssa(ss)s)`)

  A list of serialized combo boxes. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

- `current_name` (`s`)

  A suggested filename.

- `current_folder` (`ay`)

  A suggested folder to save the file in.

- `current_file` (`ay`)

  The current file (when saving an existing file).

The following results get returned via the `results` vardict:

- `uris` (`as`)

  An array of strings containing the uri of the selected file. It must have exactly one element. All URIs must have the “[file://](file://)” scheme.

- `choices` (`a(ss)`)

  An array of pairs of strings, corresponding to the passed-in choices. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

- `current_filter` (`(sa(us))`)

  The filter that was selected. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

app_id  
App id of the application

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

title  
Title for the file chooser dialog

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.FileChooser.SaveFiles

    SaveFiles (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN title s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Asks for a folder as a location to save one or more files. The names of the files will be used as-is and appended to the selected folder’s path in the list of returned files. If the selected folder already contains a file with one of the given names, the portal may prompt or take some other action to construct a unique file name and return that instead.

Supported keys in the `options` vardict include:

- `accept_label` (`s`)

  Label for the accept button. Mnemonic underlines are allowed.

- `modal` (`b`)

  Whether the dialog should be modal. Default is yes.

- `choices` (`a(ssa(ss)s)`)

  List of serialized combo boxes. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

- `current_folder` (`ay`)

  Suggested folder to save the files in. The byte array is expected to be null-terminated.

- `files` (`aay`)

  An array of file names to be saved. The array and byte arrays are expected to be null-terminated.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `uris` (`as`)

  An array of strings containing the uri corresponding to each file given by `options`, in the same order. Note that the file names may have changed, for example if a file with the same name in the selected folder already exists.

  All URIs must have the “[file://](file://)” scheme.

- `choices` (`a(ss)`)

  An array of pairs of strings, corresponding to the passed-in choices. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

app_id

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

title  
Title for the file chooser dialog

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call
