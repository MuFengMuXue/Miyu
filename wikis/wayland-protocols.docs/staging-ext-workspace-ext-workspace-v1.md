# ext_workspace_v1

## Interface `ext_workspace_manager_v1` version 1

list and control workspaces

Workspaces, also called virtual desktops, are groups of surfaces. A compositor with a concept of workspaces may only show some such groups of surfaces (those of 'active' workspaces) at a time. 'Activating' a workspace is a request for the compositor to display that workspace's surfaces as normal, whereas the compositor may hide or otherwise de-emphasise surfaces that are associated only with 'inactive' workspaces. Workspaces are grouped by which sets of outputs they correspond to, and may contain surfaces only from those outputs. In this way, it is possible for each output to have its own set of workspaces, or for all outputs (or any other arbitrary grouping) to share workspaces. Compositors may optionally conceptually arrange each group of workspaces in an N-dimensional grid. The purpose of this protocol is to enable the creation of taskbars and docks by providing them with a list of workspaces and their properties, and allowing them to activate and deactivate workspaces. After a client binds the ext_workspace_manager_v1, each workspace will be sent via the workspace event.

### Requests

- `commit`: all requests about the workspaces have been sent
  The client must send this request after it has finished sending other requests. The compositor must process a series of requests preceding a commit request atomically. This allows changes to the workspace properties to be seen as atomic, even if they happen via multiple events, and even if they involve multiple ext_workspace_handle_v1 objects, for example, deactivating one workspace and activating another.
- `stop`: stop sending events
  Indicates the client no longer wishes to receive events for new workspace groups. However the compositor may emit further workspace events, until the finished event is emitted. The compositor is expected to send the finished event eventually once the stop request has been processed. The client must not send any requests after this one, doing so will raise a wl_display invalid_object error.

### Events

- `workspace_group`: a workspace group has been created
  This event is emitted whenever a new workspace group has been created. All initial details of the workspace group (outputs) will be sent immediately after this event via the corresponding events in ext_workspace_group_handle_v1 and ext_workspace_handle_v1.
  Arguments: `workspace_group` (new_id)
- `workspace`: workspace has been created
  This event is emitted whenever a new workspace has been created. All initial details of the workspace (name, coordinates, state) will be sent immediately after this event via the corresponding events in ext_workspace_handle_v1. Workspaces start off unassigned to any workspace group.
  Arguments: `workspace` (new_id)
- `done`: all information about the workspaces and workspace groups has been sent
  This event is sent after all changes in all workspaces and workspace groups have been sent. This allows changes to one or more ext_workspace_group_handle_v1 properties and ext_workspace_handle_v1 properties to be seen as atomic, even if they happen via multiple events. In particular, an output moving from one workspace group to another sends an output_enter event and an output_leave event to the two ext_workspace_group_handle_v1 objects in question. The compositor sends the done event only after updating the output information in both workspace groups.
- `finished`: the compositor has finished with the workspace_manager
  This event indicates that the compositor is done sending events to the ext_workspace_manager_v1. The server will destroy the object immediately after sending this request.

## Interface `ext_workspace_group_handle_v1` version 1

a workspace group assigned to a set of outputs

A ext_workspace_group_handle_v1 object represents a workspace group that is assigned a set of outputs and contains a number of workspaces. The set of outputs assigned to the workspace group is conveyed to the client via output_enter and output_leave events, and its workspaces are conveyed with workspace events. For example, a compositor which has a set of workspaces for each output may advertise a workspace group (and its workspaces) per output, whereas a compositor where a workspace spans all outputs may advertise a single workspace group for all outputs.

### Requests

- `create_workspace`: create a new workspace
  Request that the compositor create a new workspace with the given name and assign it to this group. There is no guarantee that the compositor will create a new workspace, or that the created workspace will have the provided name.
  Arguments: `workspace` (string)
- `destroy`: destroy the ext_workspace_group_handle_v1 object
  Destroys the ext_workspace_group_handle_v1 object. This request should be send either when the client does not want to use the workspace group object any more or after the removed event to finalize the destruction of the object.

### Events

- `capabilities`: compositor capabilities
  This event advertises the capabilities supported by the compositor. If a capability isn't supported, clients should hide or disable the UI elements that expose this functionality. For instance, if the compositor doesn't advertise support for creating workspaces, a button triggering the create_workspace request should not be displayed. The compositor will ignore requests it doesn't support. For instance, a compositor which doesn't advertise support for creating workspaces will ignore create_workspace requests. Compositors must send this event once after creation of an ext_workspace_group_handle_v1. When the capabilities change, compositors must send this event again.
  Arguments: `capabilities` (uint) - capabilities
- `output_enter`: output assigned to workspace group
  This event is emitted whenever an output is assigned to the workspace group or a new `wl_output` object is bound by the client, which was already assigned to this workspace_group.
  Arguments: `output` (object)
- `output_leave`: output removed from workspace group
  This event is emitted whenever an output is removed from the workspace group.
  Arguments: `output` (object)
- `workspace_enter`: workspace added to workspace group
  This event is emitted whenever a workspace is assigned to this group. A workspace may only ever be assigned to a single group at a single point in time, but can be re-assigned during its lifetime.
  Arguments: `workspace` (object)
- `workspace_leave`: workspace removed from workspace group
  This event is emitted whenever a workspace is removed from this group.
  Arguments: `workspace` (object)
- `removed`: this workspace group has been removed
  This event is send when the group associated with the ext_workspace_group_handle_v1 has been removed. After sending this request the compositor will immediately consider the object inert. Any requests will be ignored except the destroy request. It is guaranteed there won't be any more events referencing this ext_workspace_group_handle_v1. The compositor must remove all workspaces belonging to a workspace group via a workspace_leave event before removing the workspace group.

### Enums

- `group_capabilities`

## Interface `ext_workspace_handle_v1` version 1

a workspace handing a group of surfaces

A ext_workspace_handle_v1 object represents a workspace that handles a group of surfaces. Each workspace has: - a name, conveyed to the client with the name event - potentially an id conveyed with the id event - a list of states, conveyed to the client with the state event - and optionally a set of coordinates, conveyed to the client with the coordinates event The client may request that the compositor activate or deactivate the workspace. Each workspace can belong to only a single workspace group. Depending on the compositor policy, there might be workspaces with the same name in different workspace groups, but these workspaces are still separate (e.g. one of them might be active while the other is not).

### Requests

- `destroy`: destroy the ext_workspace_handle_v1 object
  Destroys the ext_workspace_handle_v1 object. This request should be made either when the client does not want to use the workspace object any more or after the remove event to finalize the destruction of the object.
- `activate`: activate the workspace
  Request that this workspace be activated. There is no guarantee the workspace will be actually activated, and behaviour may be compositor-dependent. For example, activating a workspace may or may not deactivate all other workspaces in the same group.
- `deactivate`: deactivate the workspace
  Request that this workspace be deactivated. There is no guarantee the workspace will be actually deactivated.
- `assign`: assign workspace to group
  Requests that this workspace is assigned to the given workspace group. There is no guarantee the workspace will be assigned.
  Arguments: `workspace_group` (object)
- `remove`: remove the workspace
  Request that this workspace be removed. There is no guarantee the workspace will be actually removed.

### Events

- `id`: workspace id
  If this event is emitted, it will be send immediately after the ext_workspace_handle_v1 is created or when an id is assigned to a workspace (at most once during its lifetime). An id will never change during the lifetime of the `ext_workspace_handle_v1` and is guaranteed to be unique during its lifetime. Ids are not human-readable and shouldn't be displayed, use `name` for that purpose. Compositors are expected to only send ids for workspaces likely stable across multiple sessions and can be used by clients to store preferences for workspaces. Workspaces without ids should be considered temporary and any data associated with them should be deleted once the respective object is lost.
  Arguments: `id` (string)
- `name`: workspace name changed
  This event is emitted immediately after the ext_workspace_handle_v1 is created and whenever the name of the workspace changes. A name is meant to be human-readable and can be displayed to a user. Unlike the id it is neither stable nor unique.
  Arguments: `name` (string)
- `coordinates`: workspace coordinates changed
  This event is used to organize workspaces into an N-dimensional grid within a workspace group, and if supported, is emitted immediately after the ext_workspace_handle_v1 is created and whenever the coordinates of the workspace change. Compositors may not send this event if they do not conceptually arrange workspaces in this way. If compositors simply number workspaces, without any geometric interpretation, they may send 1D coordinates, which clients should not interpret as implying any geometry. Sending an empty array means that the compositor no longer orders the workspace geometrically. Coordinates have an arbitrary number of dimensions N with an uint32 position along each dimension. By convention if N > 1, the first dimension is X, the second Y, the third Z, and so on. The compositor may chose to utilize these events for a more novel workspace layout convention, however. No guarantee is made about the grid being filled or bounded; there may be a workspace at coordinate 1 and another at coordinate 1000 and none in between. Within a workspace group, however, workspaces must have unique coordinates of equal dimensionality.
  Arguments: `coordinates` (array)
- `state`: the state of the workspace changed
  This event is emitted immediately after the ext_workspace_handle_v1 is created and each time the workspace state changes, either because of a compositor action or because of a request in this protocol. Missing states convey the opposite meaning, e.g. an unset active bit means the workspace is currently inactive.
  Arguments: `state` (uint)
- `capabilities`: compositor capabilities
  This event advertises the capabilities supported by the compositor. If a capability isn't supported, clients should hide or disable the UI elements that expose this functionality. For instance, if the compositor doesn't advertise support for removing workspaces, a button triggering the remove request should not be displayed. The compositor will ignore requests it doesn't support. For instance, a compositor which doesn't advertise support for remove will ignore remove requests. Compositors must send this event once after creation of an ext_workspace_handle_v1 . When the capabilities change, compositors must send this event again.
  Arguments: `capabilities` (uint) - capabilities
- `removed`: this workspace has been removed
  This event is send when the workspace associated with the ext_workspace_handle_v1 has been removed. After sending this request, the compositor will immediately consider the object inert. Any requests will be ignored except the destroy request. It is guaranteed there won't be any more events referencing this ext_workspace_handle_v1. The compositor must only remove a workspaces not currently belonging to any workspace_group.

### Enums

- `state`: types of states on the workspace
  The different states that a workspace can have.
- `workspace_capabilities`
