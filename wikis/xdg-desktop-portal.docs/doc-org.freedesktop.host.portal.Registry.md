# Registry

## Description

Interface to associate D-Bus peers with application ids

This simple interface lets unsandboxed applications register their D-Bus connections and associate it with an application ID that will be used in portals.

This interface will not work with applications xdg-desktop-portal identifies as sandboxed.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.host.portal.Registry:version

    version readable u

## Methods

### org.freedesktop.host.portal.Registry.Register

    Register (
      IN app_id s,
      IN options a{sv}
    )

Register a D-Bus peer and associate it with an application ID. The application ID must be able to match the basename of a .desktop file that describes the application.

The application ID will be used in org.freedesktop.portal APIs to associate a portal action with an application.

Registering can only done at most once; any subsequent call will result in an error.

Registering must be done before any portal method call; registering after such a call will result in an error.

Applications should ideally listen for name appeared D-Bus signalling to re-register the peer if the portal service is restarted.

app_id  
Application identifier

options  
Vardict with optional further information
