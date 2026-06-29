# dbus.server module

*class *dbus.server.Server(*address*, *connection_class=\<class 'dbus.connection.Connection'\>*, *mainloop=None*, *auth_mechanisms=None*)  
Bases: `_dbus_bindings._Server`

An opaque object representing a server that listens for connections from other applications.

This class is not useful to instantiate directly: you must subclass it and either extend the method connection_added, or append to the list on_connection_added.

Since  
0.83

*property *address  
get_address() -\> str

Returns the address of the server.

connection_added(*conn*)  
Respond to the creation of a new Connection.

This base-class implementation just invokes the callbacks in the on_connection_added attribute.

Parameters  
conndbus.connection.Connection  
A D-Bus connection which has just been added.

The type of this parameter is whatever was passed to the Server constructor as the `connection_class`.

connection_removed(*conn*)  
Respond to the disconnection of a Connection.

This base-class implementation just invokes the callbacks in the on_connection_removed attribute.

Parameters  
conndbus.connection.Connection  
A D-Bus connection which has just become disconnected.

The type of this parameter is whatever was passed to the Server constructor as the `connection_class`.

disconnect()  
Releases the server’s address and stops listening for new clients.

If called more than once, only the first call has an effect.

get_address() → str  
Returns the address of the server.

get_id() → str  
Returns the unique ID of the server.

get_is_connected() → bool  
Return true if this Server is still listening for new connections.

*property *id  
get_id() -\> str

Returns the unique ID of the server.

*property *is_connected  
get_is_connected() -\> bool

Return true if this Server is still listening for new connections.

on_connection_added  
A list of callbacks to invoke when a connection is added. They receive two arguments: this Server and the new Connection.

on_connection_removed  
A list of callbacks to invoke when a connection becomes disconnected. They receive two arguments: this Server and the removed Connection.
