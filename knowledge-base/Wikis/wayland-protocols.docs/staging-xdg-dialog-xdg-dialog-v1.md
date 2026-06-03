# xdg_dialog_v1

## Interface `xdg_wm_dialog_v1` version 1

create dialogs related to other toplevels

The xdg_wm_dialog_v1 interface is exposed as a global object allowing to register surfaces with a xdg_toplevel role as "dialogs" relative to another toplevel. The compositor may let this relation influence how the surface is placed, displayed or interacted with. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

### Requests

- `destroy`: destroy the dialog manager object
  Destroys the xdg_wm_dialog_v1 object. This does not affect the xdg_dialog_v1 objects generated through it.
- `get_xdg_dialog`: create a dialog object
  Creates a xdg_dialog_v1 object for the given toplevel. See the interface description for more details. Compositors must raise an already_used error if clients attempt to create multiple xdg_dialog_v1 objects for the same xdg_toplevel.
  Arguments: `id` (new_id); `toplevel` (object)

### Enums

- `error`

## Interface `xdg_dialog_v1` version 1

dialog object

A xdg_dialog_v1 object is an ancillary object tied to a xdg_toplevel. Its purpose is hinting the compositor that the toplevel is a "dialog" (e.g. a temporary window) relative to another toplevel (see xdg_toplevel.set_parent). If the xdg_toplevel is destroyed, the xdg_dialog_v1 becomes inert. Through this object, the client may provide additional hints about the purpose of the secondary toplevel. This interface has no effect on toplevels that are not attached to a parent toplevel.

### Requests

- `destroy`: destroy the dialog object
  Destroys the xdg_dialog_v1 object. If this object is destroyed before the related xdg_toplevel, the compositor should unapply its effects.
- `set_modal`: mark dialog as modal
  Hints that the dialog has "modal" behavior. Modal dialogs typically require to be fully addressed by the user (i.e. closed) before resuming interaction with the parent toplevel, and may require a distinct presentation. Clients must implement the logic to filter events in the parent toplevel on their own. Compositors may choose any policy in event delivery to the parent toplevel, from delivering all events unfiltered to using them for internal consumption.
- `unset_modal`: mark dialog as not modal
  Drops the hint that this dialog has "modal" behavior. See xdg_dialog_v1.set_modal for more details.
