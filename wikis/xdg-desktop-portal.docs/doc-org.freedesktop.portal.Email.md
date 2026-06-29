# Email

## Description

Portal for sending email

This simple portal lets sandboxed applications request to send an email, optionally providing an address, subject, body and attachments.

This documentation describes version 4 of this interface.

## Properties

### org.freedesktop.portal.Email:version

    version readable u

## Methods

### org.freedesktop.portal.Email.ComposeEmail

    ComposeEmail (
      IN parent_window s,
      IN options a{sv},
      OUT handle o
    )

Presents a window that lets the user compose an email.

Note that the default email client for the host will need to support mailto: URIs following [RFC 2368](https://tools.ietf.org/html/rfc2368), with “cc”, “bcc”, “subject” and “body” query keys each corresponding to the email header of the same name, and with each attachment being passed as a `file://` URI as a value in an “attachment” query key.

For example:

    mailto:foo``bar``.com,baz``bar``.com?cc=ceo``bar``.com&amp;subject=Test``20e``-mail``20subject``&amp;attachment=file://path/to/full/file.txt

would send a mail to “foo\`\`bar\`\`.com”, “baz\`\`bar\`\`.com”, with a CC: to “ceo\`\`bar\`\`.com”, with the subject “Test e-mail subject” and the file pointed by URI `file://path/to/full/file.txt` as an attachment.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `address` (`s`)

  The email address to send to. Must conform to the HTML5 definition of a [valid email address](https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address).

- `addresses` (`as`)

  Email addresses to send to. This will be used in addition to address and must pass the same validation.

  This option was introduced in version 3 of the interface.

- `cc` (`as`)

  Email addresses to cc.

  This option was introduced in version 3 of the interface.

- `bcc` (`as`)

  Email addresses to bcc.

  This option was introduced in version 3 of the interface.

- `subject` (`s`)

  The subject for the email.

- `body` (`s`)

  The body for the email.

- `attachment_fds` (`ah`)

  File descriptors for files to attach.

- `activation_token` (`s`)

  A token that can be used to activate the chosen application.

  This option was introduced in version 4 of the interface.

All the keys in the `options` vardict are optional.

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call
