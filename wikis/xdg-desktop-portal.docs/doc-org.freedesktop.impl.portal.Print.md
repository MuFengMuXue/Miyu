# Print

## Description

Print portal backend interface

The Print portal allows sandboxed applications to print.

## Methods

### org.freedesktop.impl.portal.Print.PreparePrint

    PreparePrint (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN title s,
      IN settings a{sv},
      IN page_setup a{sv},
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Presents a print dialog to the user and returns print settings and page setup.

Supported keys in the `options` vardict:

- `modal` (`b`)

  Whether to make the dialog modal. Defaults to yes.

- `accept_label` (`s`)

  Label for the accept button. Mnemonic underlines are allowed.

The following results get returned via the `results` vardict:

- `settings` (`a{sv}`)

  Print settings as set up by the user in the print dialog.

- `page-setup` (`a{sv}`)

  Page setup as set up by the user in the print dialog.

- `token` (`u`)

  Token that can be passed to a subsequent [org.freedesktop.impl.portal.Print.Print](#org-freedesktop-impl-portal-print-print) call to bypass the print dialog.

- `supported_output_file_formats` (`as`)

  File formats supported by the app to use for print-to-file. If not set, all formats are assumed to be supported. The following values are allowed: “pdf”, “ps”, and “svg”.

- `has_current_page` (`b`)

  Whether it makes sense to return “current” for the `print-pages` setting.

- `has_selected_pages` (`b`)

  Whether it makes sense to return “selection” for the `print-pages` setting.

The [org.freedesktop.portal.Print.PreparePrint](doc-org.freedesktop.portal.Print.md#org-freedesktop-portal-print-prepareprint) documentation has details about the supported keys in settings and page-setup.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

app_id  
App id of the application

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

title  
Title for the print dialog

settings  
Serialized print settings

page_setup  
Serialized page setup

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call

### org.freedesktop.impl.portal.Print.Print

    Print (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN title s,
      IN fd h,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Prints a file.

The file is given in the form of a file descriptor open for reading.

If a valid token is present in the `options`, then this call will print with the settings from the Print call that the token refers to. If no token is present, then a print dialog will be presented to the user.

Note that it is up to the portal implementation to determine how long it considers tokens valid.

Supported keys in the `options` vardict:

- `modal` (`b`)

  Whether to make the dialog modal. Defaults to yes.

- `token` (`u`)

  Token that was returned by a previous [org.freedesktop.impl.portal.Print.PreparePrint](#org-freedesktop-impl-portal-print-prepareprint) call.

- `supported_output_file_formats` (`as`)

  File formats supported by the app to use for print-to-file. If not set, all formats are assumed to be supported. The following values are allowed: “pdf”, “ps”, and “svg”.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

app_id  
App id of the application

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

title  
Title for the print dialog

fd  
File descriptor from which to read the content to print

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call
