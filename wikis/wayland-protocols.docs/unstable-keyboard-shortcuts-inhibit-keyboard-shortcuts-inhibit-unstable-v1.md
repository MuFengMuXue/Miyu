# keyboard_shortcuts_inhibit_unstable_v1

## Protocol for inhibiting the compositor keyboard shortcuts

This protocol specifies a way for a client to request the compositor to ignore its own keyboard shortcuts for a given seat, so that all key events from that seat get forwarded to a surface. Warning! The protocol described in this file is experimental and backward incompatible changes may be made. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes are done by bumping the version number in the protocol and interface names and resetting the interface version. Once the protocol is to be declared stable, the 'z' prefix and the version number in the protocol and interface names are removed and the interface version number is reset.

## Interface `zwp_keyboard_shortcuts_inhibit_manager_v1` version 1

context object for keyboard grab_manager

A global interface used for inhibiting the compositor keyboard shortcuts.

### Requests

- `destroy`: destroy the keyboard shortcuts inhibitor object
  Destroy the keyboard shortcuts inhibitor manager.
- `inhibit_shortcuts`: create a new keyboard shortcuts inhibitor object
  Create a new keyboard shortcuts inhibitor object associated with the given surface for the given seat. If shortcuts are already inhibited for the specified seat and surface, a protocol error "already_inhibited" is raised by the compositor.
  Arguments: `id` (new_id); `surface` (object) - the surface that inhibits the keyboard shortcuts behavior; `seat` (object) - the wl_seat for which keyboard shortcuts should be disabled

### Enums

- `error`

## Interface `zwp_keyboard_shortcuts_inhibitor_v1` version 1

context object for keyboard shortcuts inhibitor

A keyboard shortcuts inhibitor instructs the compositor to ignore its own keyboard shortcuts when the associated surface has keyboard focus. As a result, when the surface has keyboard focus on the given seat, it will receive all key events originating from the specified seat, even those which would normally be caught by the compositor for its own shortcuts. The Wayland compositor is however under no obligation to disable all of its shortcuts, and may keep some special key combo for its own use, including but not limited to one allowing the user to forcibly restore normal keyboard events routing in the case of an unwilling client. The compositor may also use the same key combo to reactivate an existing shortcut inhibitor that was previously deactivated on user request. When the compositor restores its own keyboard shortcuts, an "inactive" event is emitted to notify the client that the keyboard shortcuts inhibitor is not effectively active for the surface and seat any more, and the client should not expect to receive all keyboard events. When the keyboard shortcuts inhibitor is inactive, the client has no way to forcibly reactivate the keyboard shortcuts inhibitor. The user can chose to re-enable a previously deactivated keyboard shortcuts inhibitor using any mechanism the compositor may offer, in which case the compositor will send an "active" event to notify the client. If the surface is destroyed, unmapped, or loses the seat's keyboard focus, the keyboard shortcuts inhibitor becomes irrelevant and the compositor will restore its own keyboard shortcuts but no "inactive" event is emitted in this case.

### Requests

- `destroy`: destroy the keyboard shortcuts inhibitor object
  Remove the keyboard shortcuts inhibitor from the associated wl_surface.

### Events

- `active`: shortcuts are inhibited
  This event indicates that the shortcut inhibitor is active. The compositor sends this event every time compositor shortcuts are inhibited on behalf of the surface. When active, the client may receive input events normally reserved by the compositor (see zwp_keyboard_shortcuts_inhibitor_v1). This occurs typically when the initial request "inhibit_shortcuts" first becomes active or when the user instructs the compositor to re-enable and existing shortcuts inhibitor using any mechanism offered by the compositor.
- `inactive`: shortcuts are restored
  This event indicates that the shortcuts inhibitor is inactive, normal shortcuts processing is restored by the compositor.
