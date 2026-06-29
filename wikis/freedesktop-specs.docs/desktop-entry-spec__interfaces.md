## 9 Interfaces

The `Implements` key can be used to declare one or more interfaces that a desktop file implements.

Each interface name must follow the rules used for D-Bus interface names, but other than that, they have no particular meaning. For instance, listing an interface here does not necessarily mean that this application implements that D-Bus interface or even that such a D-Bus interface exists. It is entirely up to the entity who defined a particular interface to define what it means to implement it.

Although it is entirely up to the designer of the interface to decide what a given interface name means, here are some recommended "best practices":

- interfaces should require that application is DBusActivatable, including the requirement that the application's desktop file is named using the D-Bus "reverse DNS" convention

- the interface name should correspond to a D-Bus interface that the application exports on the same object path as it exports the org.freedesktop.Application interface

- if the interface wishes to allow for details about the implementation, it should do so by specifying that implementers add a group in their desktop file with the same name as the interface (eg: "\[org.freedesktop.ImageAcquire\]")

Recommendations notwithstanding, interfaces could specify almost any imaginable requirement including such (ridiculous) things as "when launched via the Exec line, the application is expected to present a window with the \_FOO_IDENTIFIER property set, at which point an X client message will be sent to that window". Another example is "all implementations of this interface are expected to be marked NoDisplay and, on launch, will present no windows and will delete all of the user's files without confirmation".

Interface definers should take care to keep issues of backward and forward compatibility in mind when designing their interfaces.
