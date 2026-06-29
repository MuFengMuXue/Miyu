# Sessions

Some portal requests are connected to each other and need to be used in sequence. The pattern used in such cases is a [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object. Just like [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request)s, sessions are represented by an object path, that is returned by the initial `CreateSession` call of the respective portal. Subsequent calls take the object path of the session they operate on as an argument.

Sessions can be ended from the application side by calling the `Close()` method on the session. They can also be closed from the service side, in which case the `::Closed` signal is emitted on the Session object to inform the application.
