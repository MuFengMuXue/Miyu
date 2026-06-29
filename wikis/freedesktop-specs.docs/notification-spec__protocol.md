## 9 D-BUS Protocol

The following messages *must* be supported by all implementations.

### 9.1 Message commands

#### 9.1.1 `org.freedesktop.Notifications.GetCapabilities`

|                                                              |          |     |
|--------------------------------------------------------------|----------|-----|
| `as `**`org.freedesktop.Notifications.GetCapabilities`**` (` | `void)`; |     |

 

This message takes no parameters.

It returns an array of strings. Each string describes an optional capability implemented by the server. The following values are defined by this spec:

###### Table 5: Server Capabilities

|  |  |
|----|----|
| `"action-icons"` | Supports using icons instead of text for displaying actions. Using icons for actions must be enabled on a per-notification basis using the "action-icons" hint. |
| `"actions"` | The server will provide the specified actions to the user. Even if this cap is missing, actions may still be specified by the client, however the server is free to ignore them. |
| `"body"` | Supports body text. Some implementations may only show the summary (for instance, onscreen displays, marquee/scrollers) |
| `"body-hyperlinks"` | The server supports hyperlinks in the notifications. |
| `"body-images"` | The server supports images in the notifications. |
| `"body-markup"` | Supports markup in the body text. If marked up text is sent to a server that does not give this cap, the markup will show through as regular text so must be stripped clientside. |
| `"icon-multi"` | The server will render an animation of all the frames in a given image array. The client may still specify multiple frames even if this cap and/or `"icon-static"` is missing, however the server is free to ignore them and use only the primary frame. |
| `"icon-static"` | Supports display of exactly 1 frame of any given image array. This value is mutually exclusive with `"icon-multi"`, it is a protocol error for the server to specify both. |
| `"persistence"` | The server supports persistence of notifications. Notifications will be retained until they are acknowledged or removed by the user or recalled by the sender. The presence of this capability allows clients to depend on the server to ensure a notification is seen and eliminate the need for the client to display a reminding function (such as a status icon) of its own. |
| `"sound"` | The server supports sounds on notifications. If returned, the server must support the `"sound-file"` and `"suppress-sound"` hints. |

New vendor-specific caps may be specified as long as they start with `"x-`*`vendor`*`"`. For instance, `"x-gnome-foo-cap"`. Capability names must not contain spaces. They are limited to alpha-numeric characters and dashes (`"-"`).

#### 9.1.2 `org.freedesktop.Notifications.Notify`

|  |  |
|----|----|
| `UINT32 `**`org.freedesktop.Notifications.Notify`**` (` | STRING `app_name`, |
|   | UINT32 `replaces_id`, |
|   | STRING `app_icon`, |
|   | STRING `summary`, |
|   | STRING `body`, |
|   | as `actions`, |
|   | a{sv} `hints`, |
|   | INT32 `expire_timeout``)`; |

 

Sends a notification to the notification server.

###### Table 6: Notify Parameters

[TABLE]

If *replaces_id* is 0, the return value is a UINT32 that represent the notification. It is unique, and will not be reused unless a `MAXINT` number of notifications have been generated. An acceptable implementation may just use an incrementing counter for the ID. The returned ID is always greater than zero. Servers must make sure not to return zero as an ID.

If *replaces_id* is not 0, the returned value is the same value as *replaces_id*.

#### 9.1.3 `org.freedesktop.Notifications.CloseNotification`

|  |  |
|----|----|
| `void `**`org.freedesktop.Notifications.CloseNotification`**` (` | UINT32 `id``)`; |

 

Causes a notification to be forcefully closed and removed from the user's view. It can be used, for example, in the event that what the notification pertains to is no longer relevant, or to cancel a notification with no expiration time.

The `NotificationClosed` signal is emitted by this method.

If the notification no longer exists, an empty D-BUS Error message is sent back.

#### 9.1.4 `org.freedesktop.Notifications.GetServerInformation`

|  |  |
|----|----|
| ` void `**`org.freedesktop.Notifications.GetServerInformation`**` (` | out STRING `name`, |
|   | out STRING `vendor`, |
|   | out STRING `version`, |
|   | out STRING `spec_version``)`; |

 

This message returns the information on the server. Specifically, the server name, vendor, and version number.

###### Table 7: GetServerInformation Return Values

| Name           | Type   |
|----------------|--------|
| *name*         | STRING |
| *vendor*       | STRING |
| *version*      | STRING |
| *spec_version* | STRING |

### 9.2 Signals

#### 9.2.1 `org.freedesktop.Notifications.NotificationClosed`

|  |  |
|----|----|
| ` `**`org.freedesktop.Notifications.NotificationClosed`**` (` | UINT32 `id`, |
|   | UINT32 `reason``)`; |

 

A completed notification is one that has timed out, or has been dismissed by the user.

###### Table 8: NotificationClosed Parameters

| Name     | Type   |
|----------|--------|
| *id*     | UINT32 |
| *reason* | UINT32 |

The ID specified in the signal is invalidated *before* the signal is sent and may not be used in any further communications with the server.

#### 9.2.2 `org.freedesktop.Notifications.ActionInvoked`

|  |  |
|----|----|
| ` `**`org.freedesktop.Notifications.ActionInvoked`**` (` | UINT32 `id`, |
|   | STRING `action_key``)`; |

 

This signal is emitted when one of the following occurs:

- The user performs some global "invoking" action upon a notification. For instance, clicking somewhere on the notification itself.

- The user invokes a specific action as specified in the original Notify request. For example, clicking on an action button.

###### Table 9: ActionInvoked Parameters

| Name         | Type   |
|--------------|--------|
| *id*         | UINT32 |
| *action_key* | STRING |

###### Note

Clients should not assume the server will generate this signal. Some servers may not support user interaction at all, or may not support the concept of being able to "invoke" a notification.

#### 9.2.3 `org.freedesktop.Notifications.ActivationToken`

|  |  |
|----|----|
| ` `**`org.freedesktop.Notifications.ActivationToken`**` (` | UINT32 `id`, |
|   | STRING `activation_token``)`; |

 

This signal can be emitted before a `ActionInvoked` signal. It carries an activation token that can be used to activate a toplevel.

###### Table 10: ActivationToken Parameters

| Name               | Type   |
|--------------------|--------|
| *id*               | UINT32 |
| *activation_token* | STRING |

###### Note

Clients should not assume the server will generate this signal. Some servers may not support user interaction at all, or may not support the concept of being able to generate an activation token for a notification.
