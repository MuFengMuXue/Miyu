# fifo_v1

## Interface `wp_fifo_manager_v1` version 1

protocol for fifo constraints

When a Wayland compositor considers applying a content update, it must ensure all the update's readiness constraints (fences, etc) are met. This protocol provides a way to use the completion of a display refresh cycle as an additional readiness constraint. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: unbind from the manager interface
  Informs the server that the client will no longer be using this protocol object. Existing objects created by this object are not affected.
- `get_fifo`: request fifo interface for surface
  Establish a fifo object for a surface that may be used to add display refresh constraints to content updates. Only one such object may exist for a surface and attempting to create more than one will result in an already_exists protocol error. If a surface is acted on by multiple software components, general best practice is that only the component performing wl_surface.attach operations should use this protocol.
  Arguments: `id` (new_id); `surface` (object)

### Enums

- `error`: fatal presentation error
  These fatal protocol errors may be emitted in response to illegal requests.

## Interface `wp_fifo_v1` version 1

fifo interface

A fifo object for a surface that may be used to add display refresh constraints to content updates.

### Requests

- `set_barrier`: sets the start point for a fifo constraint
  When the content update containing the "set_barrier" is applied, it sets a "fifo_barrier" condition on the surface associated with the fifo object. The condition is cleared immediately after the following latching deadline for non-tearing presentation. The compositor may clear the condition early if it must do so to ensure client forward progress assumptions. To wait for this condition to clear, use the "wait_barrier" request. "set_barrier" is double-buffered state, see wl_surface.commit. Requesting set_barrier after the fifo object's surface is destroyed will generate a "surface_destroyed" error.
- `wait_barrier`: adds a fifo constraint to a content update
  Indicate that this content update is not ready while a "fifo_barrier" condition is present on the surface. This means that when the content update containing "set_barrier" was made active at a latching deadline, it will be active for at least one refresh cycle. A content update which is allowed to tear might become active after a latching deadline if no content update became active at the deadline. The constraint must be ignored if the surface is a subsurface in synchronized mode. If the surface is not being updated by the compositor (off-screen, occluded) the compositor may ignore the constraint. Clients must use an additional mechanism such as frame callbacks or timestamps to ensure throttling occurs under all conditions. "wait_barrier" is double-buffered state, see wl_surface.commit. Requesting "wait_barrier" after the fifo object's surface is destroyed will generate a "surface_destroyed" error.
- `destroy`: destroy the fifo interface
  Informs the server that the client will no longer be using this protocol object. Surface state changes previously made by this protocol are unaffected by this object's destruction.

### Enums

- `error`: fatal error
  These fatal protocol errors may be emitted in response to illegal requests.
