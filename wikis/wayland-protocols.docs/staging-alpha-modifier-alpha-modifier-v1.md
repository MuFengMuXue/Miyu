# alpha_modifier_v1

## Interface `wp_alpha_modifier_v1` version 1

surface alpha modifier manager

This interface allows a client to set a factor for the alpha values on a surface, which can be used to offload such operations to the compositor, which can in turn for example offload them to KMS. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: destroy the alpha modifier manager object
  Destroy the alpha modifier manager. This doesn't destroy objects created with the manager.
- `get_surface`: create a new alpha modifier surface object
  Create a new alpha modifier surface object associated with the given wl_surface. If there is already such an object associated with the wl_surface, the already_constructed error will be raised.
  Arguments: `id` (new_id); `surface` (object)

### Enums

- `error`

## Interface `wp_alpha_modifier_surface_v1` version 1

alpha modifier object for a surface

This interface allows the client to set a factor for the alpha values on a surface, which can be used to offload such operations to the compositor. The default factor is UINT32_MAX. This object has to be destroyed before the associated wl_surface. Once the wl_surface is destroyed, all request on this object will raise the no_surface error.

### Requests

- `destroy`: destroy the alpha modifier object
  This destroys the object, and is equivalent to set_multiplier with a value of UINT32_MAX, with the same double-buffered semantics as set_multiplier.
- `set_multiplier`: specify the alpha multiplier
  Sets the alpha multiplier for the surface. The alpha multiplier is double-buffered state, see wl_surface.commit for details. This factor is applied in the compositor's blending space, as an additional step after the processing of per-pixel alpha values for the wl_surface. The exact meaning of the factor is thus undefined, unless the blending space is specified in a different extension. This multiplier is applied even if the buffer attached to the wl_surface doesn't have an alpha channel; in that case an alpha value of one is used instead. Zero means completely transparent, UINT32_MAX means completely opaque.
  Arguments: `factor` (uint)

### Enums

- `error`
