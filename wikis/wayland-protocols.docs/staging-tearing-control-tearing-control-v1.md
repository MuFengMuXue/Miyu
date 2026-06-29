# tearing_control_v1

## Interface `wp_tearing_control_manager_v1` version 1

protocol for tearing control

For some use cases like games or drawing tablets it can make sense to reduce latency by accepting tearing with the use of asynchronous page flips. This global is a factory interface, allowing clients to inform which type of presentation the content of their surfaces is suitable for. Graphics APIs like EGL or Vulkan, that manage the buffer queue and commits of a wl_surface themselves, are likely to be using this extension internally. If a client is using such an API for a wl_surface, it should not directly use this extension on that surface, to avoid raising a tearing_control_exists protocol error. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: destroy tearing control factory object
  Destroy this tearing control factory object. Other objects, including wp_tearing_control_v1 objects created by this factory, are not affected by this request.
- `get_tearing_control`: extend surface interface for tearing control
  Instantiate an interface extension for the given wl_surface to request asynchronous page flips for presentation. If the given wl_surface already has a wp_tearing_control_v1 object associated, the tearing_control_exists protocol error is raised.
  Arguments: `id` (new_id); `surface` (object)

### Enums

- `error`

## Interface `wp_tearing_control_v1` version 1

per-surface tearing control interface

An additional interface to a wl_surface object, which allows the client to hint to the compositor if the content on the surface is suitable for presentation with tearing. The default presentation hint is vsync. See presentation_hint for more details. If the associated wl_surface is destroyed, this object becomes inert and should be destroyed.

### Requests

- `set_presentation_hint`: set presentation hint
  Set the presentation hint for the associated wl_surface. This state is double-buffered, see wl_surface.commit. The compositor is free to dynamically respect or ignore this hint based on various conditions like hardware capabilities, surface state and user preferences.
  Arguments: `hint` (uint)
- `destroy`: destroy tearing control object
  Destroy this surface tearing object and revert the presentation hint to vsync. The change will be applied on the next wl_surface.commit.

### Enums

- `presentation_hint`: presentation hint values
  This enum provides information for if submitted frames from the client may be presented with tearing.
