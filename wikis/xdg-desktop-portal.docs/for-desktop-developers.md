# For Desktop Developers

The separation of the portal infrastructure into frontend and backend is a clean way to provide suitable user interfaces that fit into different desktop environments, while sharing the portal frontend.

The portal backends are focused on providing user interfaces and accessing session- or host-specific APIs and resources. Details of interacting with the containment infrastructure such as checking access, registering files in the Document portal, etc., are handled by the portal frontend.

Portal backends can be layered together. For example, in a GNOME session, most portal backend interfaces are implemented by the GNOME portal backend, but the [org.freedesktop.impl.portal.Access](doc-org.freedesktop.impl.portal.Access.md) interface is implemented by GNOME Shell.

- [](writing-a-new-backend.md) [](writing-a-new-backend.md)

  [Writing a New Backend](writing-a-new-backend.md)

- [](configuration-file.md) [](configuration-file.md)

  [Configuration File](configuration-file.md)

- [](system-integration.md) [](system-integration.md)

  [System Integration](system-integration.md)

## D-Bus Interfaces

Portal backends must implement one or more backend D-Bus interfaces. The list of D-Bus interfaces can be found below:

- [](impl-dbus-interfaces.md) [](impl-dbus-interfaces.md)

  [Backend D-BUS Interfaces](impl-dbus-interfaces.md)

## Background Apps Monitor

In addition to managing the regular interfaces that sandboxed applications use to interface with the host system, XDG Desktop Portal also monitors running applications without an active window - if the portal backend provides an implementation of the Background portal.

This API can be used by host system services to provide rich interfaces to manage background running applications.

- [](doc-org.freedesktop.background.Monitor.md) [](doc-org.freedesktop.background.Monitor.md)

  [Background Apps Monitor](doc-org.freedesktop.background.Monitor.md)
