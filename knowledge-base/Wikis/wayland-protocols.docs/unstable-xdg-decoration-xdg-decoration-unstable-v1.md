# xdg_decoration_unstable_v1

## Interface `zxdg_decoration_manager_v1` version 2

window decoration manager

This interface allows a compositor to announce support for server-side decorations. A window decoration is a set of window controls as deemed appropriate by the party managing them, such as user interface components used to move, resize and change a window's state. A client can use this protocol to request being decorated by a supporting compositor. If compositor and client do not negotiate the use of a server-side decoration using this protocol, clients continue to self-decorate as they see fit. Warning! The protocol described in this file is experimental and backward incompatible changes may be made. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes are done by bumping the version number in the protocol and interface names and resetting the interface version. Once the protocol is to be declared stable, the 'z' prefix and the version number in the protocol and interface names are removed and the interface version number is reset.

### Requests

- `destroy`: destroy the decoration manager object
  Destroy the decoration manager. This doesn't destroy objects created with the manager.
- `get_toplevel_decoration`: create a new toplevel decoration object
  Create a new decoration object associated with the given toplevel. For objects of version 1, creating an xdg_toplevel_decoration from an xdg_toplevel which has a buffer attached or committed is a client error, and any attempts by a client to attach or manipulate a buffer prior to the first xdg_toplevel_decoration.configure event must also be treated as errors. For objects of version 2 or newer, creating an xdg_toplevel_decoration from an xdg_toplevel which has a buffer attached or committed is allowed. The initial decoration mode of the surface if a buffer is already attached depends on whether a xdg_toplevel_decoration object has been associated with the surface or not prior to this request. If an xdg_toplevel_decoration was associated with the surface, then destroyed without a surface commit, the previous decoration mode is retained. If no xdg_toplevel_decoration was associated with the surface prior to this request, or if a surface commit has been performed after a previous xdg_toplevel_decoration object associated with the surface was destroyed, the decoration mode is assumed to be client-side.
  Arguments: `id` (new_id); `toplevel` (object)

## Interface `zxdg_toplevel_decoration_v1` version 2

decoration object for a toplevel surface

The decoration object allows the compositor to toggle server-side window decorations for a toplevel surface. The client can request to switch to another mode. The xdg_toplevel_decoration object must be destroyed before its xdg_toplevel.

### Requests

- `destroy`: destroy the decoration object
  Switch back to a mode without any server-side decorations at the next commit, unless a new xdg_toplevel_decoration is created for the surface first.
- `set_mode`: set the decoration mode
  Set the toplevel surface decoration mode. This informs the compositor that the client prefers the provided decoration mode. After requesting a decoration mode, the compositor will respond by emitting an xdg_surface.configure event. The client should then update its content, drawing it without decorations if the received mode is server-side decorations. The client must also acknowledge the configure when committing the new content (see xdg_surface.ack_configure). The compositor can decide not to use the client's mode and enforce a different mode instead. Clients whose decoration mode depend on the xdg_toplevel state may send a set_mode request in response to an xdg_surface.configure event and wait for the next xdg_surface.configure event to prevent unwanted state. Such clients are responsible for preventing configure loops and must make sure not to send multiple successive set_mode requests with the same decoration mode. If an invalid mode is supplied by the client, the invalid_mode protocol error is raised by the compositor.
  Arguments: `mode` (uint) - the decoration mode
- `unset_mode`: unset the decoration mode
  Unset the toplevel surface decoration mode. This informs the compositor that the client doesn't prefer a particular decoration mode. This request has the same semantics as set_mode.

### Events

- `configure`: notify a decoration mode change
  The configure event configures the effective decoration mode. The configured state should not be applied immediately. Clients must send an ack_configure in response to this event. See xdg_surface.configure and xdg_surface.ack_configure for details. A configure event can be sent at any time. The specified mode must be obeyed by the client.
  Arguments: `mode` (uint) - the decoration mode

### Enums

- `error`
- `mode`: window decoration modes
  These values describe window decoration modes.
