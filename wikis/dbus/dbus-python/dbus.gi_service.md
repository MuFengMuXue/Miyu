# dbus.gi_service module

Support code for implementing D-Bus services via PyGI.

*class *dbus.gi_service.ExportedGObject(*conn=None*, *object_path=None*, *\*\*kwargs*)  
Bases: `gi.overrides.GObject.Object`, `dbus.service.Object`

A GObject which is exported on D-Bus.

Introspect(*object_path*, *connection*)  
Return a string of XML encoding this object’s supported interfaces, methods and signals.

SUPPORTS_MULTIPLE_CONNECTIONS* = False*  
If True, this object can be made available on more than one connection. If True but SUPPORTS_MULTIPLE_OBJECT_PATHS is False, the object must have the same object path on all its connections.

SUPPORTS_MULTIPLE_OBJECT_PATHS* = False*  
If True, this object can be made available at more than one object path. If True but SUPPORTS_MULTIPLE_CONNECTIONS is False, the object may handle more than one object path, but they must all be on the same connection.

add_to_connection(*connection*, *path*)  
Make this object accessible via the given D-Bus connection and object path.

Parameters  
connectiondbus.connection.Connection  
Export the object on this connection. If the class attribute SUPPORTS_MULTIPLE_CONNECTIONS is False (default), this object can only be made available on one connection; if the class attribute is set True by a subclass, the object can be made available on more than one connection.

pathdbus.ObjectPath or other str  
Place the object at this object path. If the class attribute SUPPORTS_MULTIPLE_OBJECT_PATHS is False (default), this object can only be made available at one object path; if the class attribute is set True by a subclass, the object can be made available with more than one object path.

Raises ValueError  
if the object’s class attributes do not allow the object to be exported in the desired way.

Since  
0.82.0

bind_property(*self*, *source_property: str*, *target: GObject.Object*, *target_property: str*, *flags: GObject.BindingFlags*) → GObject.Binding  

bind_property_full(*self*, *source_property: str*, *target: GObject.Object*, *target_property: str*, *flags: GObject.BindingFlags*, *transform_to: GObject.Closure*, *transform_from: GObject.Closure*) → GObject.Binding  

chain()  

compat_control(*what: int*, *data=None*) → int  

connect()  

connect_after()  

connect_data(*detailed_signal*, *handler*, *\*data*, *\*\*kwargs*)  
Connect a callback to the given signal with optional user data.

Parameters  
- **detailed_signal** (*str*) – A detailed signal to connect to.

- **handler** (*callable*) – Callback handler to connect to the signal.

- **\*data** –

  Variable data which is passed through to the signal handler.

- **connect_flags** (*GObject.ConnectFlags*) – Flags used for connection options.

Returns  
A signal id which can be used with disconnect.

connect_object()  

connect_object_after()  

*property *connection  
The Connection on which this object is available. Access raises AttributeError if there is no Connection, or more than one Connection.

Changed in 0.82.0: AttributeError can be raised.

disconnect  
signal_handler_disconnect(instance:GObject.Object, handler_id:int)

disconnect_by_func()  

emit()  

emit_stop_by_name(*detailed_signal*)  
Deprecated, please use stop_emission_by_name.

find_property* = gi.FunctionInfo(find_property)*  

force_floating(*self*)  

freeze_notify()  
Freezes the object’s property-changed notification queue.

Returns  
A context manager which optionally can be used to automatically thaw notifications.

This will freeze the object so that “notify” signals are blocked until the thaw_notify() method is called.

    with obj.freeze_notify():
        pass

*property *g_type_instance  

get_data(*self*, *key: str*)  

get_properties()  

get_property(*self*, *property_name: str*, *value: GObject.Value*)  

get_qdata(*self*, *quark: int*)  

getv* = gi.FunctionInfo(getv)*  

handler_block(*handler_id*)  
Blocks the signal handler from being invoked until handler_unblock() is called.

Parameters  
- **obj** (*GObject.Object*) – Object instance to block handlers for.

- **handler_id** (*int*) – Id of signal to block.

Returns  
A context manager which optionally can be used to automatically unblock the handler:

    with GObject.signal_handler_block(obj, id):
        pass

handler_block_by_func()  

handler_disconnect  
signal_handler_disconnect(instance:GObject.Object, handler_id:int)

handler_is_connected  
signal_handler_is_connected(instance:GObject.Object, handler_id:int) -\> bool

handler_unblock  
signal_handler_unblock(instance:GObject.Object, handler_id:int)

handler_unblock_by_func()  

install_properties* = gi.FunctionInfo(install_properties)*  

install_property* = gi.FunctionInfo(install_property)*  

interface_find_property(*g_iface: GObject.TypeInterface*, *property_name: str*) → GObject.ParamSpec  

interface_install_property(*g_iface: GObject.TypeInterface*, *pspec: GObject.ParamSpec*)  

interface_list_properties(*g_iface: GObject.TypeInterface*) → list, n_properties_p:int  

is_floating* = gi.FunctionInfo(is_floating)*  

list_properties* = gi.FunctionInfo(list_properties)*  

*property *locations  
An iterable over tuples representing locations at which this object is available.

Each tuple has at least two items, but may have more in future versions of dbus-python, so do not rely on their exact length. The first two items are the dbus.connection.Connection and the object path.

Since  
0.82.0

newv* = gi.FunctionInfo(newv)*  

notify* = gi.FunctionInfo(notify)*  

notify_by_pspec(*self*, *pspec: GObject.ParamSpec*)  

override_property* = gi.FunctionInfo(override_property)*  

props* = \<gi.\_gi.GProps object\>*  

*property *qdata  

ref(*self*) → GObject.Object  

*property *ref_count  

ref_sink(*self*) → GObject.Object  

remove_from_connection(*connection=None*, *path=None*)  
Make this object inaccessible via the given D-Bus connection and object path. If no connection or path is specified, the object ceases to be accessible via any connection or path.

Parameters  
connectiondbus.connection.Connection or None  
Only remove the object from this Connection. If None, remove from all Connections on which it’s exported.

pathdbus.ObjectPath or other str, or None  
Only remove the object from this object path. If None, remove from all object paths.

Raises LookupError  
if the object was not exported on the requested connection or path, or (if both are None) was not exported at all.

Since  
0.81.1

replace_data(*\*args*, *\*\*kargs*)  

replace_qdata(*\*args*, *\*\*kargs*)  

run_dispose* = gi.FunctionInfo(run_dispose)*  

set_data(*self*, *key: str*, *data=None*)  

set_properties()  

set_property(*self*, *property_name: str*, *value: GObject.Value*)  

steal_data(*self*, *key: str*)  

steal_qdata(*self*, *quark: int*)  

stop_emission(*detailed_signal*)  
Deprecated, please use stop_emission_by_name.

stop_emission_by_name  
signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str)

thaw_notify* = gi.FunctionInfo(thaw_notify)*  

unref(*self*)  

watch_closure(*self*, *closure: GObject.Closure*)  

weak_ref()  
