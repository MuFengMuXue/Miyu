# content_type_v1

## Interface `wp_content_type_manager_v1` version 1

surface content type manager

This interface allows a client to describe the kind of content a surface will display, to allow the compositor to optimize its behavior for it. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: destroy the content type manager object
  Destroy the content type manager. This doesn't destroy objects created with the manager.
- `get_surface_content_type`: create a new content type object
  Create a new content type object associated with the given surface. Creating a wp_content_type_v1 from a wl_surface which already has one attached is a client error: already_constructed.
  Arguments: `id` (new_id); `surface` (object)

### Enums

- `error`

## Interface `wp_content_type_v1` version 1

content type object for a surface

The content type object allows the compositor to optimize for the kind of content shown on the surface. A compositor may for example use it to set relevant drm properties like "content type". The client may request to switch to another content type at any time. When the associated surface gets destroyed, this object becomes inert and the client should destroy it.

### Requests

- `destroy`: destroy the content type object
  Switch back to not specifying the content type of this surface. This is equivalent to setting the content type to none, including double buffering semantics. See set_content_type for details.
- `set_content_type`: specify the content type
  Set the surface content type. This informs the compositor that the client believes it is displaying buffers matching this content type. This is purely a hint for the compositor, which can be used to adjust its behavior or hardware settings to fit the presented content best. The content type is double-buffered state, see wl_surface.commit for details.
  Arguments: `content_type` (uint) - the content type

### Enums

- `type`: possible content types
  These values describe the available content types for a surface.
