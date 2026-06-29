# xdg_toplevel_icon_v1

## protocol to assign icons to toplevels

This protocol allows clients to set icons for their toplevel surfaces either via the XDG icon stock (using an icon name), or from pixel data. A toplevel icon represents the individual toplevel (unlike the application or launcher icon, which represents the application as a whole), and may be shown in window switchers, window overviews and taskbars that list individual windows. This document adheres to RFC 2119 when using words like "must", "should", "may", etc. Warning! The protocol described in this file is currently in the testing phase. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes can only be done by creating a new major version of the extension.

## Interface `xdg_toplevel_icon_manager_v1` version 1

interface to manage toplevel icons

This interface allows clients to create toplevel window icons and set them on toplevel windows to be displayed to the user.

### Requests

- `destroy`: destroy the toplevel icon manager
  Destroy the toplevel icon manager. This does not destroy objects created with the manager.
- `create_icon`: create a new icon instance
  Creates a new icon object. This icon can then be attached to a xdg_toplevel via the 'set_icon' request.
  Arguments: `id` (new_id)
- `set_icon`: set an icon on a toplevel window
  This request assigns the icon 'icon' to 'toplevel', or clears the toplevel icon if 'icon' was null. This state is double-buffered and is applied on the next wl_surface.commit of the toplevel. After making this call, the xdg_toplevel_icon_v1 provided as 'icon' can be destroyed by the client without 'toplevel' losing its icon. The xdg_toplevel_icon_v1 is immutable from this point, and any future attempts to change it must raise the 'xdg_toplevel_icon_v1.immutable' protocol error. The compositor must set the toplevel icon from either the pixel data the icon provides, or by loading a stock icon using the icon name. See the description of 'xdg_toplevel_icon_v1' for details. If 'icon' is set to null, the icon of the respective toplevel is reset to its default icon (usually the icon of the application, derived from its desktop-entry file, or a placeholder icon). If this request is passed an icon with no pixel buffers or icon name assigned, the icon must be reset just like if 'icon' was null.
  Arguments: `toplevel` (object) - the toplevel to act on; `icon` (object)

### Events

- `icon_size`: describes a supported & preferred icon size
  This event indicates an icon size the compositor prefers to be available if the client has scalable icons and can render to any size. When the 'xdg_toplevel_icon_manager_v1' object is created, the compositor may send one or more 'icon_size' events to describe the list of preferred icon sizes. If the compositor has no size preference, it may not send any 'icon_size' event, and it is up to the client to decide a suitable icon size. A sequence of 'icon_size' events must be finished with a 'done' event. If the compositor has no size preferences, it must still send the 'done' event, without any preceding 'icon_size' events.
  Arguments: `size` (int) - the edge size of the square icon in surface-local coordinates, e.g. 64
- `done`: all information has been sent
  This event is sent after all 'icon_size' events have been sent.

## Interface `xdg_toplevel_icon_v1` version 1

a toplevel window icon

This interface defines a toplevel icon. An icon can have a name, and multiple buffers. In order to be applied, the icon must have either a name, or at least one buffer assigned. Applying an empty icon (with no buffer or name) to a toplevel should reset its icon to the default icon. It is up to compositor policy whether to prefer using a buffer or loading an icon via its name. See 'set_name' and 'add_buffer' for details.

### Requests

- `destroy`: destroy the icon object
  Destroys the 'xdg_toplevel_icon_v1' object. The icon must still remain set on every toplevel it was assigned to, until the toplevel icon is reset explicitly.
- `set_name`: set an icon name
  This request assigns an icon name to this icon. Any previously set name is overridden. The compositor must resolve 'icon_name' according to the lookup rules described in the XDG icon theme specification[1] using the environment's current icon theme. If the compositor does not support icon names or cannot resolve 'icon_name' according to the XDG icon theme specification it must fall back to using pixel buffer data instead. If this request is made after the icon has been assigned to a toplevel via 'set_icon', an 'immutable' error must be raised. [1]: https://specifications.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html
  Arguments: `icon_name` (string)
- `add_buffer`: add icon data from a pixel buffer
  This request adds pixel data supplied as wl_buffer to the icon. The client should add pixel data for all icon sizes and scales that it can provide, or which are explicitly requested by the compositor via 'icon_size' events on xdg_toplevel_icon_manager_v1. The wl_buffer supplying pixel data as 'buffer' must be backed by wl_shm and must be a square (width and height being equal). If any of these buffer requirements are not fulfilled, a 'invalid_buffer' error must be raised. If this icon instance already has a buffer of the same size and scale from a previous 'add_buffer' request, data from the last request overrides the preexisting pixel data. The wl_buffer must be kept alive for as long as the xdg_toplevel_icon it is associated with is not destroyed, otherwise a 'no_buffer' error is raised. The buffer contents must not be modified after it was assigned to the icon. As a result, the region of the wl_shm_pool's backing storage used for the wl_buffer must not be modified after this request is sent. The wl_buffer.release event is unused. If this request is made after the icon has been assigned to a toplevel via 'set_icon', an 'immutable' error must be raised.
  Arguments: `buffer` (object); `scale` (int) - the scaling factor of the icon, e.g. 1

### Enums

- `error`
