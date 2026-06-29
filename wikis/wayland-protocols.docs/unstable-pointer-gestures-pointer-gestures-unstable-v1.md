# pointer_gestures_unstable_v1

## Interface `zwp_pointer_gestures_v1` version 3

touchpad gestures

A global interface to provide semantic touchpad gestures for a given pointer. Three gestures are currently supported: swipe, pinch, and hold. Pinch and swipe gestures follow a three-stage cycle: begin, update, end. Hold gestures follow a two-stage cycle: begin and end. All gestures are identified by a unique id. Warning! The protocol described in this file is experimental and backward incompatible changes may be made. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes are done by bumping the version number in the protocol and interface names and resetting the interface version. Once the protocol is to be declared stable, the 'z' prefix and the version number in the protocol and interface names are removed and the interface version number is reset.

### Requests

- `get_swipe_gesture`: get swipe gesture
  Create a swipe gesture object. See the wl_pointer_gesture_swipe interface for details.
  Arguments: `id` (new_id); `pointer` (object)
- `get_pinch_gesture`: get pinch gesture
  Create a pinch gesture object. See the wl_pointer_gesture_pinch interface for details.
  Arguments: `id` (new_id); `pointer` (object)
- `release` since 2: destroy the pointer gesture object
  Destroy the pointer gesture object. Swipe, pinch and hold objects created via this gesture object remain valid.
- `get_hold_gesture` since 3: get hold gesture
  Create a hold gesture object. See the wl_pointer_gesture_hold interface for details.
  Arguments: `id` (new_id); `pointer` (object)

## Interface `zwp_pointer_gesture_swipe_v1` version 3

a swipe gesture object

A swipe gesture object notifies a client about a multi-finger swipe gesture detected on an indirect input device such as a touchpad. The gesture is usually initiated by multiple fingers moving in the same direction but once initiated the direction may change. The precise conditions of when such a gesture is detected are implementation-dependent. A gesture consists of three stages: begin, update (optional) and end. There cannot be multiple simultaneous hold, pinch or swipe gestures on a same pointer/seat, how compositors prevent these situations is implementation-dependent. A gesture may be cancelled by the compositor or the hardware. Clients should not consider performing permanent or irreversible actions until the end of a gesture has been received.

### Requests

- `destroy`: destroy the pointer swipe gesture object

### Events

- `begin`: multi-finger swipe begin
  This event is sent when a multi-finger swipe gesture is detected on the device.
  Arguments: `serial` (uint); `time` (uint) - timestamp with millisecond granularity; `surface` (object); `fingers` (uint) - number of fingers
- `update`: multi-finger swipe motion
  This event is sent when a multi-finger swipe gesture changes the position of the logical center. The dx and dy coordinates are relative coordinates of the logical center of the gesture compared to the previous event.
  Arguments: `time` (uint) - timestamp with millisecond granularity; `dx` (fixed) - delta x coordinate in surface coordinate space; `dy` (fixed) - delta y coordinate in surface coordinate space
- `end`: multi-finger swipe end
  This event is sent when a multi-finger swipe gesture ceases to be valid. This may happen when one or more fingers are lifted or the gesture is cancelled. When a gesture is cancelled, the client should undo state changes caused by this gesture. What causes a gesture to be cancelled is implementation-dependent.
  Arguments: `serial` (uint); `time` (uint) - timestamp with millisecond granularity; `cancelled` (int) - 1 if the gesture was cancelled, 0 otherwise

## Interface `zwp_pointer_gesture_pinch_v1` version 3

a pinch gesture object

A pinch gesture object notifies a client about a multi-finger pinch gesture detected on an indirect input device such as a touchpad. The gesture is usually initiated by multiple fingers moving towards each other or away from each other, or by two or more fingers rotating around a logical center of gravity. The precise conditions of when such a gesture is detected are implementation-dependent. A gesture consists of three stages: begin, update (optional) and end. There cannot be multiple simultaneous hold, pinch or swipe gestures on a same pointer/seat, how compositors prevent these situations is implementation-dependent. A gesture may be cancelled by the compositor or the hardware. Clients should not consider performing permanent or irreversible actions until the end of a gesture has been received.

### Requests

- `destroy`: destroy the pinch gesture object

### Events

- `begin`: multi-finger pinch begin
  This event is sent when a multi-finger pinch gesture is detected on the device.
  Arguments: `serial` (uint); `time` (uint) - timestamp with millisecond granularity; `surface` (object); `fingers` (uint) - number of fingers
- `update`: multi-finger pinch motion
  This event is sent when a multi-finger pinch gesture changes the position of the logical center, the rotation or the relative scale. The dx and dy coordinates are relative coordinates in the surface coordinate space of the logical center of the gesture. The scale factor is an absolute scale compared to the pointer_gesture_pinch.begin event, e.g. a scale of 2 means the fingers are now twice as far apart as on pointer_gesture_pinch.begin. The rotation is the relative angle in degrees clockwise compared to the previous pointer_gesture_pinch.begin or pointer_gesture_pinch.update event.
  Arguments: `time` (uint) - timestamp with millisecond granularity; `dx` (fixed) - delta x coordinate in surface coordinate space; `dy` (fixed) - delta y coordinate in surface coordinate space; `scale` (fixed) - scale relative to the initial finger position; `rotation` (fixed) - angle in degrees cw relative to the previous event
- `end`: multi-finger pinch end
  This event is sent when a multi-finger pinch gesture ceases to be valid. This may happen when one or more fingers are lifted or the gesture is cancelled. When a gesture is cancelled, the client should undo state changes caused by this gesture. What causes a gesture to be cancelled is implementation-dependent.
  Arguments: `serial` (uint); `time` (uint) - timestamp with millisecond granularity; `cancelled` (int) - 1 if the gesture was cancelled, 0 otherwise

## Interface `zwp_pointer_gesture_hold_v1` version 3

a hold gesture object

A hold gesture object notifies a client about a single- or multi-finger hold gesture detected on an indirect input device such as a touchpad. The gesture is usually initiated by one or more fingers being held down without significant movement. The precise conditions of when such a gesture is detected are implementation-dependent. In particular, this gesture may be used to cancel kinetic scrolling. A hold gesture consists of two stages: begin and end. Unlike pinch and swipe there is no update stage. There cannot be multiple simultaneous hold, pinch or swipe gestures on a same pointer/seat, how compositors prevent these situations is implementation-dependent. A gesture may be cancelled by the compositor or the hardware. Clients should not consider performing permanent or irreversible actions until the end of a gesture has been received.

### Requests

- `destroy` since 3: destroy the hold gesture object

### Events

- `begin` since 3: multi-finger hold begin
  This event is sent when a hold gesture is detected on the device.
  Arguments: `serial` (uint); `time` (uint) - timestamp with millisecond granularity; `surface` (object); `fingers` (uint) - number of fingers
- `end` since 3: multi-finger hold end
  This event is sent when a hold gesture ceases to be valid. This may happen when the holding fingers are lifted or the gesture is cancelled, for example if the fingers move past an implementation-defined threshold, the finger count changes or the hold gesture changes into a different type of gesture. When a gesture is cancelled, the client may need to undo state changes caused by this gesture. What causes a gesture to be cancelled is implementation-dependent.
  Arguments: `serial` (uint); `time` (uint) - timestamp with millisecond granularity; `cancelled` (int) - 1 if the gesture was cancelled, 0 otherwise
