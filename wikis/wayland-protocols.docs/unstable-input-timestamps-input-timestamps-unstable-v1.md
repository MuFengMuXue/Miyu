# input_timestamps_unstable_v1

## High-resolution timestamps for input events

This protocol specifies a way for a client to request and receive high-resolution timestamps for input events. Warning! The protocol described in this file is experimental and backward incompatible changes may be made. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes are done by bumping the version number in the protocol and interface names and resetting the interface version. Once the protocol is to be declared stable, the 'z' prefix and the version number in the protocol and interface names are removed and the interface version number is reset.

## Interface `zwp_input_timestamps_manager_v1` version 1

context object for high-resolution input timestamps

A global interface used for requesting high-resolution timestamps for input events.

### Requests

- `destroy`: destroy the input timestamps manager object
  Informs the server that the client will no longer be using this protocol object. Existing objects created by this object are not affected.
- `get_keyboard_timestamps`: subscribe to high-resolution keyboard timestamp events
  Creates a new input timestamps object that represents a subscription to high-resolution timestamp events for all wl_keyboard events that carry a timestamp. If the associated wl_keyboard object is invalidated, either through client action (e.g. release) or server-side changes, the input timestamps object becomes inert and the client should destroy it by calling zwp_input_timestamps_v1.destroy.
  Arguments: `id` (new_id); `keyboard` (object) - the wl_keyboard object for which to get timestamp events
- `get_pointer_timestamps`: subscribe to high-resolution pointer timestamp events
  Creates a new input timestamps object that represents a subscription to high-resolution timestamp events for all wl_pointer events that carry a timestamp. If the associated wl_pointer object is invalidated, either through client action (e.g. release) or server-side changes, the input timestamps object becomes inert and the client should destroy it by calling zwp_input_timestamps_v1.destroy.
  Arguments: `id` (new_id); `pointer` (object) - the wl_pointer object for which to get timestamp events
- `get_touch_timestamps`: subscribe to high-resolution touch timestamp events
  Creates a new input timestamps object that represents a subscription to high-resolution timestamp events for all wl_touch events that carry a timestamp. If the associated wl_touch object becomes invalid, either through client action (e.g. release) or server-side changes, the input timestamps object becomes inert and the client should destroy it by calling zwp_input_timestamps_v1.destroy.
  Arguments: `id` (new_id); `touch` (object) - the wl_touch object for which to get timestamp events

## Interface `zwp_input_timestamps_v1` version 1

context object for input timestamps

Provides high-resolution timestamp events for a set of subscribed input events. The set of subscribed input events is determined by the zwp_input_timestamps_manager_v1 request used to create this object.

### Requests

- `destroy`: destroy the input timestamps object
  Informs the server that the client will no longer be using this protocol object. After the server processes the request, no more timestamp events will be emitted.

### Events

- `timestamp`: high-resolution timestamp event
  The timestamp event is associated with the first subsequent input event carrying a timestamp which belongs to the set of input events this object is subscribed to. The timestamp provided by this event is a high-resolution version of the timestamp argument of the associated input event. The provided timestamp is in the same clock domain and is at least as accurate as the associated input event timestamp. The timestamp is expressed as tv_sec_hi, tv_sec_lo, tv_nsec triples, each component being an unsigned 32-bit value. Whole seconds are in tv_sec which is a 64-bit value combined from tv_sec_hi and tv_sec_lo, and the additional fractional part in tv_nsec as nanoseconds. Hence, for valid timestamps tv_nsec must be in [0, 999999999].
  Arguments: `tv_sec_hi` (uint) - high 32 bits of the seconds part of the timestamp; `tv_sec_lo` (uint) - low 32 bits of the seconds part of the timestamp; `tv_nsec` (uint) - nanoseconds part of the timestamp
