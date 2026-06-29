# Email

## Description

Email portal backend interface

This Email portal lets sandboxed applications request sending an email.

## Methods

### org.freedesktop.impl.portal.Email.ComposeEmail

    ComposeEmail (
      IN handle o,
      IN app_id s,
      IN parent_window s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Lets the user compose an email.

Supported keys in the `options` vardict include:

- `address` (`s`)

  The email address to send to.

- `addresses` (`as`)

  Email addresses to send to.

- `cc` (`as`)

  Email addresses to cc.

- `bcc` (`as`)

  Email addresses to bcc.

- `subject` (`s`)

  The subject for the email.

- `body` (`s`)

  The body for the email.

- `attachments` (`as`)

  The uris for files to attach.

- `activation_token` (`s`)

  A token that can be used to activate the chosen application.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

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
