# xdg_toplevel_drag_v1

## Interface `xdg_toplevel_drag_manager_v1` version 1

Move a window during a drag

This protocol enhances normal drag and drop with the ability to move a window at the same time. This allows having detachable parts of a window that when dragged out of it become a new window and can be dragged over an existing window to be reattached. A typical workflow would be when the user starts dragging on top of a detachable part of a window, the client would create a wl_data_source and a xdg_toplevel_drag_v1 object and start the drag as normal via wl_data_device.start_drag. Once the client determines that the detachable window contents should be detached from the originating window, it creates a new xdg_toplevel with these contents and issues a xdg_toplevel_drag_v1.attach request before mapping it. From now on the new window is moved by the compositor during the drag as if the client called xdg_toplevel.move. Dragging an existing window is similar. The client creates a xdg_toplevel_drag_v1 object and attaches the existing toplevel before starting the drag. Clients use the existing drag and drop mechanism to detect when a window can be docked or undocked. If the client wants to snap a window into a parent window it should delete or unmap the dragged top-level. If the contents should be detached again it attaches a new toplevel as described above. If a drag operation is cancelled without being dropped, clients should revert to the previous state, deleting any newly created windows as appropriate. When a drag operation ends as indicated by wl_data_source.dnd_drop_performed the dragged toplevel window's final position is determined as if a xdg_toplevel_move operation ended. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: destroy the xdg_toplevel_drag_manager_v1 object
  Destroy this xdg_toplevel_drag_manager_v1 object. Other objects, including xdg_toplevel_drag_v1 objects created by this factory, are not affected by this request.
- `get_xdg_toplevel_drag`: get an xdg_toplevel_drag for a wl_data_source
  Create an xdg_toplevel_drag for a drag and drop operation that is going to be started with data_source. This request can only be made on sources used in drag-and-drop, so it must be performed before wl_data_device.start_drag. Attempting to use the source other than for drag-and-drop such as in wl_data_device.set_selection will raise an invalid_source error. Destroying data_source while a toplevel is attached to the xdg_toplevel_drag is undefined.
  Arguments: `id` (new_id); `data_source` (object)

### Enums

- `error`

## Interface `xdg_toplevel_drag_v1` version 1

Object representing a toplevel move during a drag

### Requests

- `destroy`: destroy an xdg_toplevel_drag_v1 object
  Destroy this xdg_toplevel_drag_v1 object. This request must only be called after the underlying wl_data_source drag has ended, as indicated by the dnd_drop_performed or cancelled events. In any other case an ongoing_drag error is raised.
- `attach`: Move a toplevel with the drag operation
  Request that the window will be moved with the cursor during the drag operation. The offset is a hint to the compositor how the toplevel should be positioned relative to the cursor hotspot in surface local coordinates and relative to the geometry of the toplevel being attached. See xdg_surface.set_window_geometry. For example it might only be used when an unmapped window is attached. The attached window does not participate in the selection of the drag target. If the toplevel is unmapped while it is attached, it is automatically detached from the drag. In this case this request has to be called again if the window should be attached after it is remapped. This request can be called multiple times but issuing it while a toplevel with an active role is attached raises a toplevel_attached error.
  Arguments: `toplevel` (object); `x_offset` (int) - dragged surface x offset; `y_offset` (int) - dragged surface y offset

### Enums

- `error`
