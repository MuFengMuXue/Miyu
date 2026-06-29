## 2 Secrets

A secret is something an application wishes to store securely. A good example is a password that an application needs to save and use at a later date.

Within this API a secret value is treated as an array of bytes. It is recommended that a secret consist of user-readable text, although this API has no such requirement.

Applications wishing to store multiple values as part of a single secret, may choose to use a textual format to combine these values into one. For example, multiple values may be combined using the 'desktop' key file format, or XML.

Secrets may be [encrypted when transferred](transfer-secrets.html "Chapter 7. Transfer of Secrets") to or from the client application.

The [`Secret` structure](types.md#type-Secret "14.1.1.  Secret") encapsulates a secret value along with its transfer encryption parameters.
