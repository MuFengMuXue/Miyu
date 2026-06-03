# wlr_output_management_unstable_v1

## protocol to configure output devices

This protocol exposes interfaces to obtain and modify output device configuration. Warning! The protocol described in this file is experimental and backward incompatible changes may be made. Backward compatible changes may be added together with the corresponding interface version bump. Backward incompatible changes are done by bumping the version number in the protocol and interface names and resetting the interface version. Once the protocol is to be declared stable, the 'z' prefix and the version number in the protocol and interface names are removed and the interface version number is reset.

## Interface `zwlr_output_manager_v1` version 4

output device configuration manager

This interface is a manager that allows reading and writing the current output device configuration. Output devices that display pixels (e.g. a physical monitor or a virtual output in a window) are represented as heads. Heads cannot be created nor destroyed by the client, but they can be enabled or disabled and their properties can be changed. Each head may have one or more available modes. Whenever a head appears (e.g. a monitor is plugged in), it will be advertised via the head event. Immediately after the output manager is bound, all current heads are advertised. Whenever a head's properties change, the relevant wlr_output_head events will be sent. Not all head properties will be sent: only properties that have changed need to. Whenever a head disappears (e.g. a monitor is unplugged), a wlr_output_head.finished event will be sent. After one or more heads appear, change or disappear, the done event will be sent. It carries a serial which can be used in a create_configuration request to update heads properties. The information obtained from this protocol should only be used for output configuration purposes. This protocol is not designed to be a generic output property advertisement protocol for regular clients. Instead, protocols such as xdg-output should be used.

### Requests

- `create_configuration`: create a new output configuration object
  Create a new output configuration object. This allows to update head properties.
  Arguments: `id` (new_id); `serial` (uint)
- `stop`: stop sending events
  Indicates the client no longer wishes to receive events for output configuration changes. However the compositor may emit further events, until the finished event is emitted. The client must not send any more requests after this one.

### Events

- `head`: introduce a new head
  This event introduces a new head. This happens whenever a new head appears (e.g. a monitor is plugged in) or after the output manager is bound.
  Arguments: `head` (new_id)
- `done`: sent all information about current configuration
  This event is sent after all information has been sent after binding to the output manager object and after any subsequent changes. This applies to child head and mode objects as well. In other words, this event is sent whenever a head or mode is created or destroyed and whenever one of their properties has been changed. Not all state is re-sent each time the current configuration changes: only the actual changes are sent. This allows changes to the output configuration to be seen as atomic, even if they happen via multiple events. A serial is sent to be used in a future create_configuration request.
  Arguments: `serial` (uint) - current configuration serial
- `finished`: the compositor has finished with the manager
  This event indicates that the compositor is done sending manager events. The compositor will destroy the object immediately after sending this event, so it will become invalid and the client should release any resources associated with it.

## Interface `zwlr_output_head_v1` version 4

output device

A head is an output device. The difference between a wl_output object and a head is that heads are advertised even if they are turned off. A head object only advertises properties and cannot be used directly to change them. A head has some read-only properties: modes, name, description and physical_size. These cannot be changed by clients. Other properties can be updated via a wlr_output_configuration object. Properties sent via this interface are applied atomically via the wlr_output_manager.done event. No guarantees are made regarding the order in which properties are sent.

### Requests

- `release` since 3: destroy the head object
  This request indicates that the client will no longer use this head object.

### Events

- `name`: head name
  This event describes the head name. The naming convention is compositor defined, but limited to alphanumeric characters and dashes (-). Each name is unique among all wlr_output_head objects, but if a wlr_output_head object is destroyed the same name may be reused later. The names will also remain consistent across sessions with the same hardware and software configuration. Examples of names include 'HDMI-A-1', 'WL-1', 'X11-1', etc. However, do not assume that the name is a reflection of an underlying DRM connector, X11 connection, etc. If the compositor implements the xdg-output protocol and this head is enabled, the xdg_output.name event must report the same name. The name event is sent after a wlr_output_head object is created. This event is only sent once per object, and the name does not change over the lifetime of the wlr_output_head object.
  Arguments: `name` (string)
- `description`: head description
  This event describes a human-readable description of the head. The description is a UTF-8 string with no convention defined for its contents. Examples might include 'Foocorp 11" Display' or 'Virtual X11 output via :1'. However, do not assume that the name is a reflection of the make, model, serial of the underlying DRM connector or the display name of the underlying X11 connection, etc. If the compositor implements xdg-output and this head is enabled, the xdg_output.description must report the same description. The description event is sent after a wlr_output_head object is created. This event is only sent once per object, and the description does not change over the lifetime of the wlr_output_head object.
  Arguments: `description` (string)
- `physical_size`: head physical size
  This event describes the physical size of the head. This event is only sent if the head has a physical size (e.g. is not a projector or a virtual device).
  Arguments: `width` (int) - width in millimeters of the output; `height` (int) - height in millimeters of the output
- `mode`: introduce a mode
  This event introduces a mode for this head. It is sent once per supported mode.
  Arguments: `mode` (new_id)
- `enabled`: head is enabled or disabled
  This event describes whether the head is enabled. A disabled head is not mapped to a region of the global compositor space. When a head is disabled, some properties (current_mode, position, transform and scale) are irrelevant.
  Arguments: `enabled` (int) - zero if disabled, non-zero if enabled
- `current_mode`: current mode
  This event describes the mode currently in use for this head. It is only sent if the output is enabled.
  Arguments: `mode` (object)
- `position`: current position
  This events describes the position of the head in the global compositor space. It is only sent if the output is enabled.
  Arguments: `x` (int) - x position within the global compositor space; `y` (int) - y position within the global compositor space
- `transform`: current transformation
  This event describes the transformation currently applied to the head. It is only sent if the output is enabled.
  Arguments: `transform` (int)
- `scale`: current scale
  This events describes the scale of the head in the global compositor space. It is only sent if the output is enabled.
  Arguments: `scale` (fixed)
- `finished`: the head has disappeared
  This event indicates that the head is no longer available. The head object becomes inert. Clients should send a destroy request and release any resources associated with it.
- `make` since 2: head manufacturer
  This event describes the manufacturer of the head. This must report the same make as the wl_output interface does in its geometry event. Together with the model and serial_number events the purpose is to allow clients to recognize heads from previous sessions and for example load head-specific configurations back. It is not guaranteed this event will be ever sent. A reason for that can be that the compositor does not have information about the make of the head or the definition of a make is not sensible in the current setup, for example in a virtual session. Clients can still try to identify the head by available information from other events but should be aware that there is an increased risk of false positives. It is not recommended to display the make string in UI to users. For that the string provided by the description event should be preferred.
  Arguments: `make` (string)
- `model` since 2: head model
  This event describes the model of the head. This must report the same model as the wl_output interface does in its geometry event. Together with the make and serial_number events the purpose is to allow clients to recognize heads from previous sessions and for example load head-specific configurations back. It is not guaranteed this event will be ever sent. A reason for that can be that the compositor does not have information about the model of the head or the definition of a model is not sensible in the current setup, for example in a virtual session. Clients can still try to identify the head by available information from other events but should be aware that there is an increased risk of false positives. It is not recommended to display the model string in UI to users. For that the string provided by the description event should be preferred.
  Arguments: `model` (string)
- `serial_number` since 2: head serial number
  This event describes the serial number of the head. Together with the make and model events the purpose is to allow clients to recognize heads from previous sessions and for example load head- specific configurations back. It is not guaranteed this event will be ever sent. A reason for that can be that the compositor does not have information about the serial number of the head or the definition of a serial number is not sensible in the current setup. Clients can still try to identify the head by available information from other events but should be aware that there is an increased risk of false positives. It is not recommended to display the serial_number string in UI to users. For that the string provided by the description event should be preferred.
  Arguments: `serial_number` (string)
- `adaptive_sync` since 4: current adaptive sync state
  This event describes whether adaptive sync is currently enabled for the head or not. Adaptive sync is also known as Variable Refresh Rate or VRR.
  Arguments: `state` (uint)

### Enums

- `adaptive_sync_state` since 4

## Interface `zwlr_output_mode_v1` version 3

output mode

This object describes an output mode. Some heads don't support output modes, in which case modes won't be advertised. Properties sent via this interface are applied atomically via the wlr_output_manager.done event. No guarantees are made regarding the order in which properties are sent.

### Requests

- `release` since 3: destroy the mode object
  This request indicates that the client will no longer use this mode object.

### Events

- `size`: mode size
  This event describes the mode size. The size is given in physical hardware units of the output device. This is not necessarily the same as the output size in the global compositor space. For instance, the output may be scaled or transformed.
  Arguments: `width` (int) - width of the mode in hardware units; `height` (int) - height of the mode in hardware units
- `refresh`: mode refresh rate
  This event describes the mode's fixed vertical refresh rate. It is only sent if the mode has a fixed refresh rate.
  Arguments: `refresh` (int) - vertical refresh rate in mHz
- `preferred`: mode is preferred
  This event advertises this mode as preferred.
- `finished`: the mode has disappeared
  This event indicates that the mode is no longer available. The mode object becomes inert. Clients should send a destroy request and release any resources associated with it.

## Interface `zwlr_output_configuration_v1` version 4

output configuration

This object is used by the client to describe a full output configuration. First, the client needs to setup the output configuration. Each head can be either enabled (and configured) or disabled. It is a protocol error to send two enable_head or disable_head requests with the same head. It is a protocol error to omit a head in a configuration. Then, the client can apply or test the configuration. The compositor will then reply with a succeeded, failed or cancelled event. Finally the client should destroy the configuration object.

### Requests

- `enable_head`: enable and configure a head
  Enable a head. This request creates a head configuration object that can be used to change the head's properties.
  Arguments: `id` (new_id) - a new object to configure the head; `head` (object) - the head to be enabled
- `disable_head`: disable a head
  Disable a head.
  Arguments: `head` (object) - the head to be disabled
- `apply`: apply the configuration
  Apply the new output configuration. In case the configuration is successfully applied, there is no guarantee that the new output state matches completely the requested configuration. For instance, a compositor might round the scale if it doesn't support fractional scaling. After this request has been sent, the compositor must respond with an succeeded, failed or cancelled event. Sending a request that isn't the destructor is a protocol error.
- `test`: test the configuration
  Test the new output configuration. The configuration won't be applied, but will only be validated. Even if the compositor succeeds to test a configuration, applying it may fail. After this request has been sent, the compositor must respond with an succeeded, failed or cancelled event. Sending a request that isn't the destructor is a protocol error.
- `destroy`: destroy the output configuration
  Using this request a client can tell the compositor that it is not going to use the configuration object anymore. Any changes to the outputs that have not been applied will be discarded. This request also destroys wlr_output_configuration_head objects created via this object.

### Events

- `succeeded`: configuration changes succeeded
  Sent after the compositor has successfully applied the changes or tested them. Upon receiving this event, the client should destroy this object. If the current configuration has changed, events to describe the changes will be sent followed by a wlr_output_manager.done event.
- `failed`: configuration changes failed
  Sent if the compositor rejects the changes or failed to apply them. The compositor should revert any changes made by the apply request that triggered this event. Upon receiving this event, the client should destroy this object.
- `cancelled`: configuration has been cancelled
  Sent if the compositor cancels the configuration because the state of an output changed and the client has outdated information (e.g. after an output has been hotplugged). The client can create a new configuration with a newer serial and try again. Upon receiving this event, the client should destroy this object.

### Enums

- `error`

## Interface `zwlr_output_configuration_head_v1` version 4

head configuration

This object is used by the client to update a single head's configuration. It is a protocol error to set the same property twice.

### Requests

- `set_mode`: set the mode
  This request sets the head's mode.
  Arguments: `mode` (object)
- `set_custom_mode`: set a custom mode
  This request assigns a custom mode to the head. The size is given in physical hardware units of the output device. If set to zero, the refresh rate is unspecified. It is a protocol error to set both a mode and a custom mode.
  Arguments: `width` (int) - width of the mode in hardware units; `height` (int) - height of the mode in hardware units; `refresh` (int) - vertical refresh rate in mHz or zero
- `set_position`: set the position
  This request sets the head's position in the global compositor space.
  Arguments: `x` (int) - x position in the global compositor space; `y` (int) - y position in the global compositor space
- `set_transform`: set the transform
  This request sets the head's transform.
  Arguments: `transform` (int)
- `set_scale`: set the scale
  This request sets the head's scale.
  Arguments: `scale` (fixed)
- `set_adaptive_sync` since 4: enable/disable adaptive sync
  This request enables/disables adaptive sync. Adaptive sync is also known as Variable Refresh Rate or VRR.
  Arguments: `state` (uint)

### Enums

- `error`
