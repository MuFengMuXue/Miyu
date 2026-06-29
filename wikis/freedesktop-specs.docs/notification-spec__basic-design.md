## 2 Basic Design

In order to ensure that multiple notifications can easily be displayed at once, and to provide a convenient implementation, all notifications are controlled by a single session-scoped service which exposes a D-BUS interface.

On startup, a conforming implementation should take the `org.freedesktop.Notifications` service on the session bus. This service will be referred to as the "notification server" or just "the server" in this document. It can optionally be activated automatically by the bus process, however this is not required and notification server clients must not assume that it is available.

The server should implement the `org.freedesktop.Notifications` interface on an object with the path `"/org/freedesktop/Notifications"`. This is the only interface required by this version of the specification.

A notification has the following components:

###### Table 1: Notification Components

[TABLE]

Each notification displayed is allocated a unique ID by the server. This is unique within the session. While the notification server is running, the ID will not be recycled unless the capacity of a uint32 is exceeded.

This can be used to hide the notification before the expiration timeout is reached. It can also be used to atomically replace the notification with another. This allows you to (for instance) modify the contents of a notification while it's on-screen.
