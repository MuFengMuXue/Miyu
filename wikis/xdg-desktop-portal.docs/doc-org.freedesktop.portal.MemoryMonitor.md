# Memory Monitor

## Description

Memory monitoring portal

The Memory Monitor interface provides information about low system memory to sandboxed applications. It is not a portal in the strict sense, since it does not involve user interaction. Applications are expected to use this interface indirectly, via a library API such as the GLib GMemoryMonitor interface.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.portal.MemoryMonitor:version

    version readable u

## Signals

### org.freedesktop.portal.MemoryMonitor::LowMemoryWarning

    LowMemoryWarning (
      level y
    )

Signal emitted when a particular low memory situation happens with 0 being the lowest level of memory availability warning, and 255 being the highest. Those levels are defined and documented in [Low Memory Monitor’s documentation](https://hadess.pages.freedesktop.org/low-memory-monitor/).

level  
An integer representing the level of low memory warning.
