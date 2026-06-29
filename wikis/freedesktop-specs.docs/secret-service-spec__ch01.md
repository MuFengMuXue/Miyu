## 1 Introduction

The Secret Service API allows client applications to store secrets securely in a service running in the user's login session.

The secrets are usually stored in an encrypted manner by the service. The service may need to be unlocked by the user before the secrets become available for retrieval by client applications.

The Secret Service stores a secret along with a set of lookup attributes. The attributes can be used to look up and retrieve a secret at a later date. The lookup attributes are not treated as secret material, and the service may choose not to encrypt attributes when storing them to disk.

This API was designed by GNOME and KDE developers with the goal of having a common way to store secrets. Its predecessors are the desktop-specific APIs used by GNOME Keyring and KWallet.
