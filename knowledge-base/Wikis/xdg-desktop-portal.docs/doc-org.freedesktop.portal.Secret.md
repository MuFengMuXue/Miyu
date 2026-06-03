# Secret

## Description

Portal for retrieving application secret

The Secret portal allows sandboxed applications to retrieve a per-application secret. The secret can then be used for encrypting confidential data inside the sandbox.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.portal.Secret:version

    version readable u

## Methods

### org.freedesktop.portal.Secret.RetrieveSecret

    RetrieveSecret (
      IN fd h,
      IN options a{sv},
      OUT handle o
    )

Retrieves a master secret for a sandboxed application.

The master secret is unique per application and does not change as long as the application is installed (once it has been created). In a typical backend implementation, it is stored in the user’s keyring, under the application ID as a key.

While the master secret can be used for encrypting any confidential data in the sandbox, the format is opaque to the application. In particular, the length of the secret might not be sufficient for the use with certain encryption algorithm. In that case, the application is supposed to expand it using a KDF algorithm.

The portal may return an additional identifier associated with the secret in the results vardict of [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal. In the next call of this method, the application shall indicate it through a token element in `options`.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `token` (`s`)

  An opaque string returned by a previous [org.freedesktop.portal.Secret.RetrieveSecret](#org-freedesktop-portal-secret-retrievesecret) call.

fd  
Writable file descriptor for transporting the secret

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call
