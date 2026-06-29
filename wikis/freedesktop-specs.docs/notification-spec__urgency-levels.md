## 7 Urgency Levels

Notifications have an urgency level associated with them. This defines the importance of the notification. For example, "Joe Bob signed on" would be a low urgency. "You have new mail" or "A USB device was unplugged" would be a normal urgency. "Your computer is on fire" would be a critical urgency.

Urgency levels are defined as follows:

###### Table 3: Urgency Levels

| Type | Description |
|------|-------------|
| 0    | Low         |
| 1    | Normal      |
| 2    | Critical    |

Developers must use their own judgement when deciding the urgency of a notification. Typically, if the majority of programs are using the same level for a specific type of urgency, other applications should follow them.

For low and normal urgencies, server implementations may display the notifications how they choose. They should, however, have a sane expiration timeout dependent on the urgency level.

Critical notifications should not automatically expire, as they are things that the user will most likely want to know about. They should only be closed when the user dismisses them, for example, by clicking on the notification.
