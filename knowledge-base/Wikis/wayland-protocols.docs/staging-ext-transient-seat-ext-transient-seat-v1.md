# ext_transient_seat_v1

## protocol for creating temporary seats

The transient seat protocol can be used by privileged clients to create independent seats that will be removed from the compositor when the client destroys its transient seat. This protocol is intended for use with virtual input protocols such as "virtual_keyboard_unstable_v1" or "wlr_virtual_pointer_unstable_v1", both of which allow the user to select a seat. The "wl_seat" global created by this protocol does not generate input events on its own, or have any capabilities except those assigned to it by other protocol extensions, such as the ones mentioned above. For example, a remote desktop server can create a seat with virtual inputs for each remote user by following these steps for each new connection: * Create a transient seat * Wait for the transient seat to be created * Locate a "wl_seat" global with a matching name * Create virtual inputs using the resulting "wl_seat" global

## Interface `ext_transient_seat_manager_v1` version 1

transient seat manager

The transient seat manager creates short-lived seats.

### Requests

- `create`: create a transient seat
  Create a new seat that is removed when the client side transient seat object is destroyed. The actual seat may be removed sooner, in which case the transient seat object shall become inert.
  Arguments: `seat` (new_id)
- `destroy`: destroy the manager
  Destroy the manager. All objects created by the manager will remain valid until they are destroyed themselves.

## Interface `ext_transient_seat_v1` version 1

transient seat handle

When the transient seat handle is destroyed, the seat itself will also be destroyed.

### Requests

- `destroy`: destroy transient seat
  When the transient seat object is destroyed by the client, the associated seat created by the compositor is also destroyed.

### Events

- `ready`: transient seat is ready
  This event advertises the global name for the wl_seat to be used with wl_registry_bind. It is sent exactly once, immediately after the transient seat is created and the new "wl_seat" global is advertised, if and only if the creation of the transient seat was allowed.
  Arguments: `global_name` (uint)
- `denied`: transient seat creation denied
  The event informs the client that the compositor denied its request to create a transient seat. It is sent exactly once, immediately after the transient seat object is created, if and only if the creation of the transient seat was denied. After receiving this event, the client should destroy the object.
