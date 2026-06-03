# Account

## Description

Backend for the portal for obtaining user information

This Account portal lets sandboxed applications query basic information about the user, like their name and avatar photo. The portal backend will present the user with a dialog to confirm which (if any) information to share.

## Methods

### org.freedesktop.impl.portal.Account.GetUserInformation

    GetUserInformation (
      IN handle o,
      IN app_id s,
      IN window s,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Gets information about the user.

Supported keys in the `options` vardict include:

- `reason` (`s`)

  A string that can be shown in the dialog to explain why the information is needed. This should be a complete sentence that explains what the application will do with the returned information, for example: Allows your personal information to be included with recipes you share with your friends.

The following results get returned via the `results` vardict:

- `id` (`s`)

  The user id.

- `name` (`s`)

  The users real name.

- `image` (`s`)

  The URI of an image file for the users avatar photo.

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

app_id  
App id of the application

window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call
