# fractional_scale_v1

## Protocol for requesting fractional surface scales

This protocol allows a compositor to suggest for surfaces to render at fractional scales. A client can submit scaled content by utilizing wp_viewport. This is done by creating a wp_viewport object for the surface and setting the destination rectangle to the surface size before the scale factor is applied. The buffer size is calculated by multiplying the surface size by the intended scale. The wl_surface buffer scale should remain set to 1. If a surface has a surface-local size of 100 px by 50 px and wishes to submit buffers with a scale of 1.5, then a buffer of 150px by 75 px should be used and the wp_viewport destination rectangle should be 100 px by 50 px. For toplevel surfaces, the size is rounded halfway away from zero. The rounding algorithm for subsurface position and size is not defined.

## Interface `wp_fractional_scale_manager_v1` version 1

fractional surface scale information

A global interface for requesting surfaces to use fractional scales.

### Requests

- `destroy`: unbind the fractional surface scale interface
  Informs the server that the client will not be using this protocol object anymore. This does not affect any other objects, wp_fractional_scale_v1 objects included.
- `get_fractional_scale`: extend surface interface for scale information
  Create an add-on object for the the wl_surface to let the compositor request fractional scales. If the given wl_surface already has a wp_fractional_scale_v1 object associated, the fractional_scale_exists protocol error is raised.
  Arguments: `id` (new_id) - the new surface scale info interface id; `surface` (object) - the surface

### Enums

- `error`

## Interface `wp_fractional_scale_v1` version 1

fractional scale interface to a wl_surface

An additional interface to a wl_surface object which allows the compositor to inform the client of the preferred scale.

### Requests

- `destroy`: remove surface scale information for surface
  Destroy the fractional scale object. When this object is destroyed, preferred_scale events will no longer be sent.

### Events

- `preferred_scale`: notify of new preferred scale
  Notification of a new preferred scale for this surface that the compositor suggests that the client should use. The sent scale is the numerator of a fraction with a denominator of 120.
  Arguments: `scale` (uint) - the new preferred scale
