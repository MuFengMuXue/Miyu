# pointer_warp_v1

## Interface `wp_pointer_warp_v1` version 1

reposition the pointer to a location on a surface

This global interface allows applications to request the pointer to be moved to a position relative to a wl_surface. Note that if the desired behavior is to constrain the pointer to an area or lock it to a position, this protocol does not provide a reliable way to do that. The pointer constraint and pointer lock protocols should be used for those use cases instead. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: destroy the warp manager
  Destroy the pointer warp manager.
- `warp_pointer`: reposition the pointer
  Request the compositor to move the pointer to a surface-local position. Whether or not the compositor honors the request is implementation defined, but it should - honor it if the surface has pointer focus, including when it has an implicit pointer grab - reject it if the enter serial is incorrect - reject it if the requested position is outside of the surface Note that the enter serial is valid for any surface of the client, and does not have to be from the surface the pointer is warped to.
  Arguments: `surface` (object) - surface to position the pointer on; `pointer` (object) - the pointer that should be repositioned; `x` (fixed); `y` (fixed); `serial` (uint) - serial number of the enter event
