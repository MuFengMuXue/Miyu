# Network Monitor

## Description

Network monitoring portal

The NetworkMonitor interface provides network status information to sandboxed applications. It is not a portal in the strict sense, since it does not involve user interaction. Applications are expected to use this interface indirectly, via a library API such as the GLib GNetworkMonitor interface.

This documentation describes version 3 of this interface.

## Properties

### org.freedesktop.portal.NetworkMonitor:version

    version readable u

## Methods

### org.freedesktop.portal.NetworkMonitor.GetAvailable

    GetAvailable (
      OUT available b
    )

Returns whether the network is considered available. That is, whether the system as a default route for at least one of IPv4 or IPv6.

This method was added in version 2 to replace the available property.

available  
whether the network is available

### org.freedesktop.portal.NetworkMonitor.GetMetered

    GetMetered (
      OUT metered b
    )

Returns whether the network is considered metered. That is, whether the system as traffic flowing through the default connection that is subject ot limitations by service providers.

This method was added in version 2 to replace the metered property.

metered  
whether the network is metered

### org.freedesktop.portal.NetworkMonitor.GetConnectivity

    GetConnectivity (
      OUT connectivity u
    )

Returns more detailed information about the host’s network connectivity. The meaning of the value is:

- `1`: Local only. The host is not configured with a route to the internet.

- `2`: Limited connectivity. The host is connected to a network, but can’t reach the full internet.

- `3`: Captive portal. The host is behind a captive portal and cannot reach the full internet.

- `4`: Full network. The host connected to a network, and can reach the full internet.

This method was added in version 2 to replace the connectivity property.

connectivity  
the level of connectivity

### org.freedesktop.portal.NetworkMonitor.GetStatus

    GetStatus (
      OUT status a{sv}
    )

Returns the three values all at once.

The following results get returned via `status`:

- `available` (`b`)

  Whether the network is available.

- `metered` (`b`)

  Whether the network is metered.

- `connectivity` (`u`)

  The level of connectivity.

This method was added in version 3 to avoid multiple round-trips.

status  
a dictionary with the current values

### org.freedesktop.portal.NetworkMonitor.CanReach

    CanReach (
      IN hostname s,
      IN port u,
      OUT reachable b
    )

Returns whether the given hostname is believed to be reachable. This method was added in version 3.

hostname  
the hostname to reach

port  
the port to reach

reachable  
Whether the hostname:port was reachable

## Signals

### org.freedesktop.portal.NetworkMonitor::changed

    changed ()

Emitted when the network configuration changes.
