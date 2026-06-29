# ext_image_copy_capture_v1

## image capturing into client buffers

This protocol allows clients to ask the compositor to capture image sources such as outputs and toplevels into user submitted buffers. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

## Interface `ext_image_copy_capture_manager_v1` version 1

manager to inform clients and begin capturing

This object is a manager which offers requests to start capturing from a source.

### Requests

- `create_session`: capture an image capture source
  Create a capturing session for an image capture source. If the paint_cursors option is set, cursors shall be composited onto the captured frame. The cursor must not be composited onto the frame if this flag is not set. If the options bitfield is invalid, the invalid_option protocol error is sent.
  Arguments: `session` (new_id); `source` (object); `options` (uint)
- `create_pointer_cursor_session`: capture the pointer cursor of an image capture source
  Create a cursor capturing session for the pointer of an image capture source.
  Arguments: `session` (new_id); `source` (object); `pointer` (object)
- `destroy`: destroy the manager
  Destroy the manager object. Other objects created via this interface are unaffected.

### Enums

- `error`
- `options`

## Interface `ext_image_copy_capture_session_v1` version 1

image copy capture session

This object represents an active image copy capture session. After a capture session is created, buffer constraint events will be emitted from the compositor to tell the client which buffer types and formats are supported for reading from the session. The compositor may re-send buffer constraint events whenever they change. To advertise buffer constraints, the compositor must send in no particular order: zero or more shm_format and dmabuf_format events, zero or one dmabuf_device event, and exactly one buffer_size event. Then the compositor must send a done event. When the client has received all the buffer constraints, it can create a buffer accordingly, attach it to the capture session using the attach_buffer request, set the buffer damage using the damage_buffer request and then send the capture request.

### Requests

- `create_frame`: create a frame
  Create a capture frame for this session. At most one frame object can exist for a given session at any time. If a client sends a create_frame request before a previous frame object has been destroyed, the duplicate_frame protocol error is raised.
  Arguments: `frame` (new_id)
- `destroy`: delete this object
  Destroys the session. This request can be sent at any time by the client. This request doesn't affect ext_image_copy_capture_frame_v1 objects created by this object.

### Events

- `buffer_size`: image capture source dimensions
  Provides the dimensions of the source image in buffer pixel coordinates. The client must attach buffers that match this size.
  Arguments: `width` (uint) - buffer width; `height` (uint) - buffer height
- `shm_format`: shm buffer format
  Provides the format that must be used for shared-memory buffers. This event may be emitted multiple times, in which case the client may choose any given format.
  Arguments: `format` (uint) - shm format
- `dmabuf_device`: dma-buf device
  This event advertises the device buffers must be allocated on for dma-buf buffers. In general the device is a DRM node. The DRM node type (primary vs. render) is unspecified. Clients must not rely on the compositor sending a particular node type. Clients cannot check two devices for equality by comparing the dev_t value.
  Arguments: `device` (array) - device dev_t value
- `dmabuf_format`: dma-buf format
  Provides the format that must be used for dma-buf buffers. The client may choose any of the modifiers advertised in the array of 64-bit unsigned integers. This event may be emitted multiple times, in which case the client may choose any given format.
  Arguments: `format` (uint) - drm format code; `modifiers` (array) - drm format modifiers
- `done`: all constraints have been sent
  This event is sent once when all buffer constraint events have been sent. The compositor must always end a batch of buffer constraint events with this event, regardless of whether it sends the initial constraints or an update.
- `stopped`: session is no longer available
  This event indicates that the capture session has stopped and is no longer available. This can happen in a number of cases, e.g. when the underlying source is destroyed, if the user decides to end the image capture, or if an unrecoverable runtime error has occurred. The client should destroy the session after receiving this event.

### Enums

- `error`

## Interface `ext_image_copy_capture_frame_v1` version 1

image capture frame

This object represents an image capture frame. The client should attach a buffer, damage the buffer, and then send a capture request. If the capture is successful, the compositor must send the frame metadata (transform, damage, presentation_time in any order) followed by the ready event. If the capture fails, the compositor must send the failed event.

### Requests

- `destroy`: destroy this object
  Destroys the frame. This request can be sent at any time by the client.
- `attach_buffer`: attach buffer to session
  Attach a buffer to the session. The wl_buffer.release request is unused. The new buffer replaces any previously attached buffer. This request must not be sent after capture, or else the already_captured protocol error is raised.
  Arguments: `buffer` (object)
- `damage_buffer`: damage buffer
  Apply damage to the buffer which is to be captured next. This request may be sent multiple times to describe a region. The client indicates the accumulated damage since this wl_buffer was last captured. During capture, the compositor will update the buffer with at least the union of the region passed by the client and the region advertised by ext_image_copy_capture_frame_v1.damage. When a wl_buffer is captured for the first time, or when the client doesn't track damage, the client must damage the whole buffer. This is for optimisation purposes. The compositor may use this information to reduce copying. These coordinates originate from the upper left corner of the buffer. If x or y are strictly negative, or if width or height are negative or zero, the invalid_buffer_damage protocol error is raised. This request must not be sent after capture, or else the already_captured protocol error is raised.
  Arguments: `x` (int) - region x coordinate; `y` (int) - region y coordinate; `width` (int) - region width; `height` (int) - region height
- `capture`: capture a frame
  Capture a frame. Unless this is the first successful captured frame performed in this session, the compositor may wait an indefinite amount of time for the source content to change before performing the copy. This request may only be sent once, or else the already_captured protocol error is raised. A buffer must be attached before this request is sent, or else the no_buffer protocol error is raised.

### Events

- `transform`: buffer transform
  This event is sent before the ready event and holds the transform that the compositor has applied to the buffer contents.
  Arguments: `transform` (uint)
- `damage`: buffer damaged region
  This event is sent before the ready event. It may be generated multiple times to describe a region. The first captured frame in a session will always carry full damage. Subsequent frames' damaged regions describe which parts of the buffer have changed since the last ready event. These coordinates originate in the upper left corner of the buffer.
  Arguments: `x` (int) - damage x coordinate; `y` (int) - damage y coordinate; `width` (int) - damage width; `height` (int) - damage height
- `presentation_time`: presentation time of the frame
  This event indicates the time at which the frame is presented to the output in system monotonic time. This event is sent before the ready event. The timestamp is expressed as tv_sec_hi, tv_sec_lo, tv_nsec triples, each component being an unsigned 32-bit value. Whole seconds are in tv_sec which is a 64-bit value combined from tv_sec_hi and tv_sec_lo, and the additional fractional part in tv_nsec as nanoseconds. Hence, for valid timestamps tv_nsec must be in [0, 999999999].
  Arguments: `tv_sec_hi` (uint) - high 32 bits of the seconds part of the timestamp; `tv_sec_lo` (uint) - low 32 bits of the seconds part of the timestamp; `tv_nsec` (uint) - nanoseconds part of the timestamp
- `ready`: frame is available for reading
  Called as soon as the frame is copied, indicating it is available for reading. The buffer may be re-used by the client after this event. After receiving this event, the client must destroy the object.
- `failed`: capture failed
  This event indicates that the attempted frame copy has failed. After receiving this event, the client must destroy the object.
  Arguments: `reason` (uint)

### Enums

- `error`
- `failure_reason`

## Interface `ext_image_copy_capture_cursor_session_v1` version 1

cursor capture session

This object represents a cursor capture session. It extends the base capture session with cursor-specific metadata.

### Requests

- `destroy`: delete this object
  Destroys the session. This request can be sent at any time by the client. This request doesn't affect ext_image_copy_capture_frame_v1 objects created by this object.
- `get_capture_session`: get image copy capturer session
  Gets the image copy capture session for this cursor session. The session will produce frames of the cursor image. The compositor may pause the session when the cursor leaves the captured area. This request must not be sent more than once, or else the duplicate_session protocol error is raised.
  Arguments: `session` (new_id)

### Events

- `enter`: cursor entered captured area
  Sent when a cursor enters the captured area. It shall be generated before the "position" and "hotspot" events when and only when a cursor enters the area. The cursor enters the captured area when the cursor image intersects with the captured area. Note, this is different from e.g. wl_pointer.enter.
- `leave`: cursor left captured area
  Sent when a cursor leaves the captured area. No "position" or "hotspot" event is generated for the cursor until the cursor enters the captured area again.
- `position`: position changed
  Cursors outside the image capture source do not get captured and no event will be generated for them. The given position is the position of the cursor's hotspot and it is relative to the main buffer's top left corner in transformed buffer pixel coordinates. The coordinates may be negative or greater than the main buffer size.
  Arguments: `x` (int) - position x coordinates; `y` (int) - position y coordinates
- `hotspot`: hotspot changed
  The hotspot describes the offset between the cursor image and the position of the input device. The given coordinates are the hotspot's offset from the origin in buffer coordinates. Clients should not apply the hotspot immediately: the hotspot becomes effective when the next ext_image_copy_capture_frame_v1.ready event is received. Compositors may delay this event until the client captures a new frame.
  Arguments: `x` (int) - hotspot x coordinates; `y` (int) - hotspot y coordinates

### Enums

- `error`
