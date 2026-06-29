# commit_timing_v1

## Interface `wp_commit_timing_manager_v1` version 1

commit timing

When a compositor latches on to new content updates it will check for any number of requirements of the available content updates (such as fences of all buffers being signalled) to consider the update ready. This protocol provides a method for adding a time constraint to surface content. This constraint indicates to the compositor that a content update should be presented as closely as possible to, but not before, a specified time. This protocol does not change the Wayland property that content updates are applied in the order they are received, even when some content updates contain timestamps and others do not. To provide timestamps, this global factory interface must be used to acquire a wp_commit_timing_v1 object for a surface, which may then be used to provide timestamp information for commits. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: unbind from the commit timing interface
  Informs the server that the client will no longer be using this protocol object. Existing objects created by this object are not affected.
- `get_timer`: request commit timer interface for surface
  Establish a timing controller for a surface. Only one commit timer can be created for a surface, or a commit_timer_exists protocol error will be generated.
  Arguments: `id` (new_id); `surface` (object)

### Enums

- `error`

## Interface `wp_commit_timer_v1` version 1

Surface commit timer

An object to set a time constraint for a content update on a surface.

### Requests

- `set_timestamp`: Specify time the following commit takes effect
  Provide a timing constraint for a surface content update. A set_timestamp request may be made before a wl_surface.commit to tell the compositor that the content is intended to be presented as closely as possible to, but not before, the specified time. The time is in the domain of the compositor's presentation clock. An invalid_timestamp error will be generated for invalid tv_nsec. If a timestamp already exists on the surface, a timestamp_exists error is generated. Requesting set_timestamp after the commit_timer object's surface is destroyed will generate a "surface_destroyed" error.
  Arguments: `tv_sec_hi` (uint) - high 32 bits of the seconds part of target time; `tv_sec_lo` (uint) - low 32 bits of the seconds part of target time; `tv_nsec` (uint) - nanoseconds part of target time
- `destroy`: Destroy the timer
  Informs the server that the client will no longer be using this protocol object. Existing timing constraints are not affected by the destruction.

### Enums

- `error`
