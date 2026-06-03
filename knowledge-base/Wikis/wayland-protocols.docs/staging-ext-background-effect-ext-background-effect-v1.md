# ext_background_effect_v1

## Interface `ext_background_effect_manager_v1` version 1

background effect factory

This protocol provides a way to improve visuals of translucent surfaces by applying effects like blur to the background behind them. The capabilities are send when the global is bound, and every time they change. Note that when the capability goes away, the corresponding effect is no longer applied by the compositor, even if it was set before. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: destroy the background effect manager
  Informs the server that the client will no longer be using this protocol object. Existing objects created by this object are not affected.
- `get_background_effect`: get a background effects object
  Instantiate an interface extension for the given wl_surface to add effects like blur for the background behind it. If the given wl_surface already has a ext_background_effect_surface_v1 object associated, the background_effect_exists protocol error will be raised.
  Arguments: `id` (new_id) - the new ext_background_effect_surface_v1 object; `surface` (object) - the surface

### Events

- `capabilities`: capabilities of the compositor
  Arguments: `flags` (uint)

### Enums

- `error`
- `capability`

## Interface `ext_background_effect_surface_v1` version 1

background effects for a surface

The background effect object provides a way to specify a region behind a surface that should have background effects like blur applied. If the wl_surface associated with the ext_background_effect_surface_v1 object has been destroyed, this object becomes inert.

### Requests

- `destroy`: release the blur object
  Informs the server that the client will no longer be using this protocol object. The effect regions will be removed on the next commit.
- `set_blur_region`: set blur region
  This request sets the region of the surface that will have its background blurred. The blur region is specified in the surface-local coordinates, and clipped by the compositor to the surface size. The initial value for the blur region is empty. Setting the pending blur region has copy semantics, and the wl_region object can be destroyed immediately. A NULL wl_region removes the effect. The blur region is double-buffered state, and will be applied on the next wl_surface.commit. The blur algorithm is subject to compositor policies. If the associated surface has been destroyed, the surface_destroyed error will be raised.
  Arguments: `region` (object) - blur region of the surface

### Enums

- `error`
