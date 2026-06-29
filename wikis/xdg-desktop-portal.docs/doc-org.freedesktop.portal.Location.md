# Location

## Description

Portal for obtaining information about the location

This simple interface lets sandboxed applications query basic information about the location.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.portal.Location:version

    version readable u

## Methods

### org.freedesktop.portal.Location.CreateSession

    CreateSession (
      IN options a{sv},
      OUT handle o
    )

Create a location session. A successfully created session can at any time be closed using [org.freedesktop.portal.Session.Close](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session-close), or may at any time be closed by the portal implementation, which will be signalled via [org.freedesktop.portal.Session::Closed](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session-closed).

Supported keys in the `options` vardict include:

- `session_handle_token` (`s`)

  > A string that will be used as the last element of the session handle. Must be a valid object path element. See the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) documentation for more information about the session handle.

- `distance-threshold` (`u`)

  Distance threshold in meters. Default is 0.

- `time-threshold` (`u`)

  Time threshold in seconds. Default is 0.

- `accuracy` (`u`)

  Requested accuracy. Default is `EXACT`. Supported values:

  - `NONE`: 0

  - `COUNTRY`: 1

  - `CITY`: 2

  - `NEIGHBORHOOD`: 3

  - `STREET`: 4

  - `EXACT`: 5

options  
Vardict with optional further information

handle  
Object path for the created [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

### org.freedesktop.portal.Location.Start

    Start (
      IN session_handle o,
      IN parent_window s,
      IN options a{sv},
      OUT handle o
    )

Start the location session. An application can only attempt start a session once.

Supported keys in the `options` vardict include:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

## Signals

### org.freedesktop.portal.Location::LocationUpdated

    LocationUpdated (
      session_handle o,
      location a{sv}
    )

The LocationUpdated signal is emitted when the location has changed, as well as when the initial location has been determined.

The following results may get returned via the `location`:

- `Latitude` (`d`)

  The latitude, in degrees.

- `Longitude` (`d`)

  The longitude, in degrees.

- `Altitude` (`d`)

  The altitude, in meters.

- `Accuracy` (`d`)

  The accuracy, in meters.

- `Speed` (`d`)

  The speed, in meters per second.

- `Heading` (`d`)

  The heading, in degrees, going clockwise. North 0, East 90, South 180, West 270.

- `Timestamp` (`(tt)`)

  The timestamp, as seconds and microseconds since the Unix epoch.

session_handle  
Object path for the [Session](doc-org.freedesktop.portal.Session.md#org-freedesktop-portal-session) object

location  
Vardict with the current location data
