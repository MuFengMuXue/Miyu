> 

# PipeWire Proxies

## Proxy

Lua objects that bind a `WpProxy <proxy_api>` contain the following methods:

Proxy.getinterface_type(self)

Binds `wp_proxy_get_interface_type`

param self  
the proxy

returns  
the proxy type, the proxy type version

rtype  
string, integer

## PipeWire Object

Lua objects that bind a `WpPipewireObject <pipewire_object_api>` contain the following methods:

PipewireObject.iterateparams(self, paramname)

Binds `wp_pipewire_object_enum_params_sync`

param self  
the proxy

param string paramname  
the PipeWire param name to enumerate, ex "Props", "Route"

returns  
the available parameters

rtype  
Iterator; the iteration items are Spa Pod objects

PipewireObject.setparam(self, paramname, pod)

Binds `wp_pipewire_object_set_param`

param self  
the proxy

param string paramname  
The PipeWire param name to set, ex "Props", "Route"

param Pod pod  
A Spa Pod object containing the new params

## Global Proxy

Lua objects that bind a `WpGlobalProxy <global_proxy_api>` contain the following methods:

GlobalProxy.requestdestroy(self)

Binds `wp_global_proxy_request_destroy`

param self  
the proxy

## PipeWire Node

Lua objects that bind a `WpNode <node_api>` contain the following methods:

Node.getstate(self)

Binds `wp_node_get_state`

param self  
the proxy

returns  
the current state of the node and an error message, if any

rtype  
string (`WpNodeState`), string (error message)

since  
0.4.2

Node.getn_input_ports(self)

Binds `wp_node_get_n_input_ports`

param self  
the proxy

returns  
the current and max numbers of input ports on the node

rtype  
integer (current), integer (max)

since  
0.4.2

Node.getn_output_ports(self)

Binds `wp_node_get_n_output_ports`

param self  
the proxy

returns  
the current and max numbers of output ports on the node

rtype  
integer (current), integer (max)

since  
0.4.2

Node.getn_ports(self)

Binds `wp_node_get_n_ports`

param self  
the proxy

returns  
the number of ports on the node

since  
0.4.2

Node.iterateports(self, interest)

Binds `wp_node_iterate_ports`

param self  
the proxy

param interest  
an interest to filter objects

type interest  
`Interest <lua_object_interest_api>` or nil or none

returns  
all the ports of this node that that match the interest

rtype  
Iterator; the iteration items are of type `WpPort <port_api>`

since  
0.4.2

Node.lookupport(self, interest)

Binds `wp_node_lookup_port`

param self  
the proxy

param interest  
the interest to use for the lookup

type interest  
`Interest <lua_object_interest_api>` or nil or none

returns  
the first port of this node that matches the interest

rtype  
`WpPort <port_api>`

since  
0.4.2

Node.sendcommand(self, command)

Binds `wp_node_send_command`

param self  
the proxy

param string command  
the command to send to the node (ex "Suspend")

## PipeWire Port

Lua objects that bind a `WpPort <port_api>` contain the following methods:

Port.getdirection(self)

Binds `wp_port_get_direction`

param self  
the port

returns  
the direction of the Port

rtype  
string (`WpDirection`)

since  
0.4.2

## PipeWire Client

Lua objects that bind a `WpClient <client_api>` contain the following methods:

Client.updatepermissions(self, perms)

Binds `wp_client_update_permissions`

Takes a table where the keys are object identifiers and the values are permission strings.

Valid object identifiers are:

- A number, meaning the bound ID of a proxy
- The string "any" or the string "all", which sets the default permissions for this client

The permission strings have a chmod-like syntax (ex. "rwx" or "r-xm"), where:

- "r" means permission to read the object
- "w" means permission to write data to the object
- "x" means permission to call methods on the object
- "m" means permission to set metadata for the object
- "-" is ignored and can be used to make the string more readable when a permission flag is omitted

**Example:**

``` lua
client:update_permissions {
  ["all"] = "r-x",
  [35] = "rwxm",
}
```

param self  
the proxy

param table perms  
the permissions to update for this client

Client.attachpermission_manager(self, pm)

Binds `wp_client_attach_permission_manager`

Attaches a permission manager to handle permissions for this client automatically. The permission manager will manage per-object permissions based on its configured rules and default permissions.

param self  
the client

param WpPermissionManager pm  
the permission manager to attach

Client.getpermission_manager(self)

Binds `wp_client_get_permission_manager`

Returns the permission manager currently attached to this client, or `nil` if no permission manager is attached.

**Example:**

``` lua
local pm = client:get_permission_manager()
if pm then
  local perms = pm:get_default_permissions()
  -- check permission bits
end
```

param self  
the client

returns  
the attached permission manager, or nil

rtype  
WpPermissionManager or nil

## PipeWire Metadata

Lua objects that bind a `WpMetadata <metadata_api>` contain the following methods:

Metadata.iterate(self, subject)

Binds `wp_metadata_new_iterator`

param self  
the proxy

param integer subject  
the subject id

returns  
an iterator

Metadata.find(self, subject, key)

Binds `wp_metadata_find`

param self  
the proxy

param string subject  
the subject id

param string key  
the metadata key to find

returns  
the value for this metadata key, the type of the value

rtype  
string, string

## Permission Manager

The `PermissionManager` object manages per-object permissions for clients. It is created with the global `PermissionManager()` constructor and configured with default permissions, core permissions, and match rules.

PermissionManager()

Creates a new permission manager.

returns  
a new permission manager

rtype  
WpPermissionManager

PermissionManager.setdefault_permissions(self, perms)

Binds `wp_permission_manager_set_default_permissions`

Sets the default permissions applied to all objects that don't match any rule.

param self  
the permission manager

param perms  
a permission string (e.g. "rx") or an integer bitmask (e.g. `Perm.RX`)

PermissionManager.getdefault_permissions(self)

Binds `wp_permission_manager_get_default_permissions`

Returns the default permissions as an integer bitmask. This can be compared against the `Perm` constants using bitwise operators.

**Example:**

``` lua
local pm = client:get_permission_manager()
local perms = pm:get_default_permissions()
if (perms & Perm.RX) == Perm.RX then
  -- client has at least read + execute
end
```

param self  
the permission manager

returns  
the default permissions bitmask

rtype  
integer

PermissionManager.setcore_permissions(self, perms)

Binds `wp_permission_manager_set_core_permissions`

Sets the permissions applied specifically to the PipeWire core object (ID 0). If not set, the core inherits the default permissions.

param self  
the permission manager

param perms  
a permission string or an integer bitmask

PermissionManager.addrules_match(self, rules)

Binds `wp_permission_manager_add_rules_match`

Adds a set of match rules that grant specific permissions to objects matching the given constraints.

param self  
the permission manager

param WpSpaJson rules  
a JSON array of match rules

returns  
the match id (can be used with `remove_match`)

rtype  
integer

PermissionManager.addinterest_match(self, callback, interest)

Binds `wp_permission_manager_add_interest_match_closure`

Adds a dynamic match that calls the given callback to determine permissions for objects matching the given interest.

param self  
the permission manager

param function callback  
a function that returns the permissions for the matched object

param WpObjectInterest interest  
the interest to match

returns  
the match id

rtype  
integer

PermissionManager.addinterest_match_simple(self, perms, interest)

Binds `wp_permission_manager_add_interest_match_simple`

Adds a static match that grants the given permissions to objects matching the given interest.

param self  
the permission manager

param integer perms  
the permissions bitmask to grant

param WpObjectInterest interest  
the interest to match

returns  
the match id

rtype  
integer

PermissionManager.removematch(self, matchid)

Binds `wp_permission_manager_remove_match`

Removes a previously added match.

param self  
the permission manager

param integer matchid  
the match id returned by an `add_*_match` method

PermissionManager.updatepermissions(self)

Binds `wp_permission_manager_update_permissions`

Forces a recalculation and update of permissions on all attached clients.

param self  
the permission manager
