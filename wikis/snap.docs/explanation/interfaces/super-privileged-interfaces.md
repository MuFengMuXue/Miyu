# Super-privileged interfaces

[Interfaces](https://snapcraft.io/docs/explanation/interfaces/all-about-interfaces/) allow (or deny) access to a resource outside of a snap’s confinement and, generally, any snap can declare any [supported interface](https://snapcraft.io/docs/reference/interfaces/).

However, there is a limited set of interfaces that require extra scrutiny when their _plugs_ are included in a snap. This is due to their permissive nature and the control and impact they potentially have over a system.

These interfaces are called **super-privileged**, and snaps that include plugs for super-privileged interfaces require specific [approval from the Store](https://forum.snapcraft.io/t/process-for-aliases-auto-connections-and-tracks/455) before they can be distributed and installed.
