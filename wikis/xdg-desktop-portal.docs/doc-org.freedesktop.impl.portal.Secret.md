# Secret

## Description

Secret portal backend interface

The Secret portal allows sandboxed applications to retrieve a per-application master secret.

## Properties

### org.freedesktop.impl.portal.Secret:version

    version readable u

## Methods

### org.freedesktop.impl.portal.Secret.RetrieveSecret

    RetrieveSecret (
      IN handle o,
      IN app_id s,
      IN fd h,
      IN options a{sv},
      OUT response u,
      OUT results a{sv}
    )

Retrieves a master secret for a sandboxed application.

Supported keys in the `options` vardict include:

- `token` (`s`)

  An opaque string associated with the retrieve secret.

handle  
Object path for the [Request](doc-org.freedesktop.impl.portal.Request.md#org-freedesktop-impl-portal-request) object representing this call

app_id  
App id of the application

fd  
Writable file descriptor for transporting the secret

options  
Vardict with optional further information

response  
Numeric response

results  
Vardict with the results of the call
