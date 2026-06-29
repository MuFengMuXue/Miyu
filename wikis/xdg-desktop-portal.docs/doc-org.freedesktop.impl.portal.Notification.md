# Notification

## Description

Notification portal backend interface

This notification interface lets sandboxed applications send and withdraw notifications.

This documentation describes version 2 of this interface.

## Properties

### org.freedesktop.impl.portal.Notification:SupportedOptions

    SupportedOptions readable a{sv}

Some properties in [org.freedesktop.impl.portal.Notification.AddNotification](#org-freedesktop-impl-portal-notification-addnotification) may have options advertised by the notification server.

The format is the same as for `SupportedOptions` property of [Notification](doc-org.freedesktop.portal.Notification.md#org-freedesktop-portal-notification).

### org.freedesktop.impl.portal.Notification:version

    version readable u

## Methods

### org.freedesktop.impl.portal.Notification.AddNotification

    AddNotification (
      IN app_id s,
      IN id s,
      IN notification a{sv}
    )

Sends a notification.

The ID can be used to later withdraw the notification. If the application reuses the same ID without withdrawing, the notification is updated with the new one. It’s possible to set `show-as-new` hint in the `display-hint` property to animate replacing the notification instead of updating it.

The format of the `notification` is the same as for [org.freedesktop.portal.Notification.AddNotification](doc-org.freedesktop.portal.Notification.md#org-freedesktop-portal-notification-addnotification).

Since version 2, the icon property never uses the `bytes` option.

app_id  
App id of the application

id  
Application-provided ID for this notification

notification  
Vardict with the serialized notification

### org.freedesktop.impl.portal.Notification.RemoveNotification

    RemoveNotification (
      IN app_id s,
      IN id s
    )

Withdraws a notification.

app_id  
App id of the application

id  
Application-provided ID for this notification

## Signals

### org.freedesktop.impl.portal.Notification::ActionInvoked

    ActionInvoked (
      app_id s,
      id s,
      action s,
      parameter av
    )

Send to the application when a non-exported action is activated.

The `parameter` contains the following values in order:

1.  The target for the action, if one was specified.

2.  The platform-data as vardict containing an `activation-token` (`s`) for [XDG Activation](https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/staging/xdg-activation/xdg-activation-v1.xml)

app_id  
App id of the application

id  
the application-provided ID for the notification

action  
the name of the action

parameter  
an array containing additional information
