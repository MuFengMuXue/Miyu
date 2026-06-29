# Access

## Description

Interface for presenting an access dialog

This backend can be used by portal implementations that need to ask a direct access question, such as “May xyz use the microphone?”

## Methods

### org.freedesktop.impl.portal.Access.AccessDialog

    AccessDialog (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN title s,
      IN subtitle s,
      IN body s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Presents a “deny/grant” question to the user.

Supported keys in the `options` include:

- `modal` (`b`)

  Whether to make the dialog modal. Defaults to true.

- `deny_label` (`s`)

  Label for the Deny button.

- `grant_label` (`s`)

  Label for the Grant button.

- `icon` (`s`)

  Icon name for an icon to show in the dialog. This should be a symbolic icon name.

- `choices` (`a(ssa(ss)s)`)

  List of serialized choices. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

The following results get returned via the `results` vardict:

- `choices` (`a(ss)`)

  An array of pairs of strings, corresponding to the passed-in choices. See [org.freedesktop.portal.FileChooser.OpenFile](doc-org.freedesktop.portal.FileChooser.md#org-freedesktop-portal-filechooser-openfile) for details.

handle  
Object path to export the Request object at

app_id  
App id of the application

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

title  
Title for the dialog

subtitle  
Subtitle for the dialog

body  
Body text, may be “”

options  
Vardict with optional further information

response  
Numeric response. The values allowed match the values allowed for [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal.

results  
Vardict with the results of the call
