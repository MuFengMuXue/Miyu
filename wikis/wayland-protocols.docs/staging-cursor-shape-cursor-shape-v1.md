# cursor_shape_v1

## Interface `wp_cursor_shape_manager_v1` version 2

cursor shape manager

This global offers an alternative, optional way to set cursor images. This new way uses enumerated cursors instead of a wl_surface like wl_pointer.set_cursor does. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: destroy the manager
  Destroy the cursor shape manager.
- `get_pointer`: manage the cursor shape of a pointer device
  Obtain a wp_cursor_shape_device_v1 for a wl_pointer object. When the pointer capability is removed from the wl_seat, the wp_cursor_shape_device_v1 object becomes inert.
  Arguments: `cursor_shape_device` (new_id); `pointer` (object)
- `get_tablet_tool_v2`: manage the cursor shape of a tablet tool device
  Obtain a wp_cursor_shape_device_v1 for a zwp_tablet_tool_v2 object. When the zwp_tablet_tool_v2 is removed, the wp_cursor_shape_device_v1 object becomes inert.
  Arguments: `cursor_shape_device` (new_id); `tablet_tool` (object)

## Interface `wp_cursor_shape_device_v1` version 2

cursor shape for a device

This interface allows clients to set the cursor shape.

### Requests

- `destroy`: destroy the cursor shape device
  Destroy the cursor shape device. The device cursor shape remains unchanged.
- `set_shape`: set device cursor to the shape
  Sets the device cursor to the specified shape. The compositor will change the cursor image based on the specified shape. The cursor actually changes only if the input device focus is one of the requesting client's surfaces. If any, the previous cursor image (surface or shape) is replaced. The "shape" argument must be a valid enum entry, otherwise the invalid_shape protocol error is raised. This is similar to the wl_pointer.set_cursor and zwp_tablet_tool_v2.set_cursor requests, but this request accepts a shape instead of contents in the form of a surface. Clients can mix set_cursor and set_shape requests. The serial parameter must match the latest wl_pointer.enter or zwp_tablet_tool_v2.proximity_in serial number sent to the client. Otherwise the request will be ignored.
  Arguments: `serial` (uint) - serial number of the enter event; `shape` (uint)

### Enums

- `shape`: cursor shapes
  This enum describes cursor shapes. The names are taken from the CSS W3C specification: https://w3c.github.io/csswg-drafts/css-ui/#cursor with a few additions. Note that there are some groups of cursor shapes that are related: The first group is drag-and-drop cursors which are used to indicate the selected action during dnd operations. The second group is resize cursors which are used to indicate resizing and moving possibilities on window borders. It is recommended that the shapes in these groups should use visually compatible images and metaphors.
- `error`
