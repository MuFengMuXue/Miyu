## 7 Transfer of Secrets

[7.1 Negotiation of Algorithms](transfer-secrets.md#id-1.2.8.6)

[7.2 Algorithm: plain](ch07s02.md)

[7.3 Algorithm: dh-ietf1024-sha256-aes128-cbc-pkcs7](ch07s03.md)

To access or store secrets, use the [`GetSecret()`](org.freedesktop.Secret.Item.md#org.freedesktop.Secret.Item.GetSecret "org.freedesktop.Secret.Item.GetSecret"), [`SetSecret()`](org.freedesktop.Secret.Item.md#org.freedesktop.Secret.Item.SetSecret "org.freedesktop.Secret.Item.SetSecret") methods on the item interface, or the [`GetSecrets()`](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.GetSecrets "org.freedesktop.Secret.Service.GetSecrets"), method on the service interface.

You must specify a session when retrieving or storing a secret. The session controls how the secret is encoded during transfer. Since this is a D-Bus API, the data in all method calls and other accesses in this API will go through multiple processes, and may be cached arbitrarily by the OS or elsewhere.

The Secrets API has provision to encrypt secrets while in transit between the service and the client application. The encryption is not envisioned to withstand man in the middle attacks, or other active attacks. It is envisioned to minimize storage of plain text secrets in memory and prevent plain text storage of secrets in a swap file or other caching mechanism.

Many client applications may choose not to make use of the provisions to encrypt secrets in transit. In fact for applications unable to prevent their own memory from being paged to disk (eg: Java, C# or Python apps), transferring encrypted secrets would be an exercise of questionable value.

## 7.1 Negotiation of Algorithms

In order to encrypt secrets in transit, the service and the client application must agree on an algorithm, and some algorithm specific parameters (eg: a key).

When the client application opens a [session](sessions.html "Chapter 6. Sessions") with the service, it calls the [` OpenSession()`](org.freedesktop.Secret.Service.md#org.freedesktop.Secret.Service.OpenSession "org.freedesktop.Secret.Service.OpenSession") method on the service. The algorithms argument to the `OpenSession()` method specifies a set of algorithms to be used together for key agreement and encryption. The other arguments are algorithm specific.

If a service does not support a specific set of algorithms, a org.freedesktop.DBus.Error.NotSupported error is returned, and the client is free to try another set of algorithms. The *plain* algorithm is almost always supported.

An algorithm may require that the `OpenSession()` method is called multiple times in succession to be complete. Each iteration transfers algorithm specific data back forth between the service and the client. The object path '/' is returned from `OpenSession()` when session negotiation is incomplete.

None of the algorithms documented in this initial version of the specification require multiple calls to `OpenSession()`.

When `OpenSession()` completes, it returns the session object path along with a valid session object path.

Once a session algorithm has been negotiated, it is used for all transfer of secrets whenever that session is specified along with the [`secret`](types.md#type-Secret "14.1.1.  Secret").
