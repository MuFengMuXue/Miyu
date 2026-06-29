# ext_idle_notify_v1

## Interface `ext_idle_notifier_v1` version 2

idle notification manager

This interface allows clients to monitor user idle status. After binding to this global, clients can create ext_idle_notification_v1 objects to get notified when the user is idle for a given amount of time.

### Requests

- `destroy`: destroy the manager
  Destroy the manager object. All objects created via this interface remain valid.
- `get_idle_notification`: create a notification object
  Create a new idle notification object. The notification object has a minimum timeout duration and is tied to a seat. The client will be notified if the seat is inactive for at least the provided timeout. See ext_idle_notification_v1 for more details. A zero timeout is valid and means the client wants to be notified as soon as possible when the seat is inactive.
  Arguments: `id` (new_id); `timeout` (uint) - minimum idle timeout in msec; `seat` (object)
- `get_input_idle_notification` since 2: create a notification object
  Create a new idle notification object to track input from the user, such as keyboard and mouse movement. Because this object is meant to track user input alone, it ignores idle inhibitors. The notification object has a minimum timeout duration and is tied to a seat. The client will be notified if the seat is inactive for at least the provided timeout. See ext_idle_notification_v1 for more details. A zero timeout is valid and means the client wants to be notified as soon as possible when the seat is inactive.
  Arguments: `id` (new_id); `timeout` (uint) - minimum idle timeout in msec; `seat` (object)

## Interface `ext_idle_notification_v1` version 2

idle notification

This interface is used by the compositor to send idle notification events to clients. Initially the notification object is not idle. The notification object becomes idle when no user activity has happened for at least the timeout duration, starting from the creation of the notification object. User activity may include input events or a presence sensor, but is compositor-specific. How this notification responds to idle inhibitors depends on how it was constructed. If constructed from the get_idle_notification request, then if an idle inhibitor is active (e.g. another client has created a zwp_idle_inhibitor_v1 on a visible surface), the compositor must not make the notification object idle. However, if constructed from the get_input_idle_notification request, then idle inhibitors are ignored, and only input from the user, e.g. from a keyboard or mouse, counts as activity. When the notification object becomes idle, an idled event is sent. When user activity starts again, the notification object stops being idle, a resumed event is sent and the timeout is restarted.

### Requests

- `destroy`: destroy the notification object
  Destroy the notification object.

### Events

- `idled`: notification object is idle
  This event is sent when the notification object becomes idle. It's a compositor protocol error to send this event twice without a resumed event in-between.
- `resumed`: notification object is no longer idle
  This event is sent when the notification object stops being idle. It's a compositor protocol error to send this event twice without an idled event in-between. It's a compositor protocol error to send this event prior to any idled event.
