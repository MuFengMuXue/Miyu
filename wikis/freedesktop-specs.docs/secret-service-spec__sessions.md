## 6 Sessions

A session is established between a client application and a service. A session is used to [transfer secrets](transfer-secrets.html "Chapter 7. Transfer of Secrets") between the client application and the service.

A session is established by calling the service's [`OpenSession()`](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.OpenSession "org.freedesktop.Secret.Service.OpenSession") method. Once established, a session is bound to calling application's connection to the DBus session bus.

A session is closed when the client application disconnects from the DBus session bus. Alternatively the client application can call the [`Close()`](org.freedesktop.Secret.Session.md#org.freedesktop.Secret.Session.Close "org.freedesktop.Secret.Session.Close") method on the session interface. Once a session is closed all session specific negotiations will be dropped by the service.

More than one session may opened by a client application, although this is not normally necessary.
