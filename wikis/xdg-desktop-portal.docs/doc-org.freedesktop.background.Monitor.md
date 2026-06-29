# Background Apps Monitor

## Description

Background applications monitor

This interface provides APIs related to applications that are running in the background.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.background.Monitor:BackgroundApps

    BackgroundApps readable aa{sv}

The list of applications that are considered to be running in background. The following keys are supported:

- `app_id` (`s`)

  App id of the application.

- `instance` (`s`)

  The Flatpak instance of the application.

- `message` (`s`)

  Status message reported by the application. Optional.

### org.freedesktop.background.Monitor:version

    version readable u
