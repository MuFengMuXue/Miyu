# dbus.connection module

*class *dbus.connection.Connection(*\*args*, *\*\*kwargs*)  
Bases: `_dbus_bindings.Connection`

A connection to another application. In this base class there is assumed to be no bus daemon.

Since  
0.81.0

ProxyObjectClass  
alias of `dbus.proxies.ProxyObject`

activate_name_owner(*bus_name*)  
Return the unique name for the given bus name, activating it if necessary and possible.

If the name is already unique or this connection is not to a bus daemon, just return it.

Returns  
a bus name. If the given bus_name exists, the returned name identifies its current owner; otherwise the returned name does not exist.

Raises DBusException  
if the implementation has failed to activate the given bus name.

Since  
0.81.0

add_message_filter(*callable*)  
Add the given message filter to the internal list.

Filters are handlers that are run on all incoming messages, prior to the objects registered to handle object paths.

Filters are run in the order that they were added. The same handler can be added as a filter more than once, in which case it will be run more than once. Filters added during a filter callback won’t be run on the message being processed.

add_signal_receiver(*handler_function*, *signal_name=None*, *dbus_interface=None*, *bus_name=None*, *path=None*, *\*\*keywords*)  
Arrange for the given function to be called when a signal matching the parameters is received.

Parameters  
handler_functioncallable  
The function to be called. Its positional arguments will be the arguments of the signal. By default it will receive no keyword arguments, but see the description of the optional keyword arguments below.

signal_namestr  
The signal name; None (the default) matches all names

dbus_interfacestr  
The D-Bus interface name with which to qualify the signal; None (the default) matches all interface names

bus_namestr  
A bus name for the sender, which will be resolved to a unique name if it is not already; None (the default) matches any sender.

pathstr  
The object path of the object which must have emitted the signal; None (the default) matches any object path

Keywords  
utf8_stringsbool  
If True, the handler function will receive any string arguments as dbus.UTF8String objects (a subclass of str guaranteed to be UTF-8). If False (default) it will receive any string arguments as dbus.String objects (a subclass of unicode).

byte_arraysbool  
If True, the handler function will receive any byte-array arguments as dbus.ByteArray objects (a subclass of str). If False (default) it will receive any byte-array arguments as a dbus.Array of dbus.Byte (subclasses of: a list of ints).

sender_keywordstr  
If not None (the default), the handler function will receive the unique name of the sending endpoint as a keyword argument with this name.

destination_keywordstr  
If not None (the default), the handler function will receive the bus name of the destination (or None if the signal is a broadcast, as is usual) as a keyword argument with this name.

interface_keywordstr  
If not None (the default), the handler function will receive the signal interface as a keyword argument with this name.

member_keywordstr  
If not None (the default), the handler function will receive the signal name as a keyword argument with this name.

path_keywordstr  
If not None (the default), the handler function will receive the object-path of the sending object as a keyword argument with this name.

message_keywordstr  
If not None (the default), the handler function will receive the dbus.lowlevel.SignalMessage as a keyword argument with this name.

arg…unicode or UTF-8 str  
If there are additional keyword parameters of the form `arg`*n*, match only signals where the *n*th argument is the value given for that keyword parameter. As of this time only string arguments can be matched (in particular, object paths and signatures can’t).

named_servicestr  
A deprecated alias for bus_name.

call_async(*bus_name*, *object_path*, *dbus_interface*, *method*, *signature*, *args*, *reply_handler*, *error_handler*, *timeout=- 1.0*, *byte_arrays=False*, *require_main_loop=True*, *\*\*kwargs*)  
Call the given method, asynchronously.

If the reply_handler is None, successful replies will be ignored. If the error_handler is None, failures will be ignored. If both are None, the implementation may request that no reply is sent.

Returns  
The dbus.lowlevel.PendingCall.

Since  
0.81.0

call_blocking(*bus_name*, *object_path*, *dbus_interface*, *method*, *signature*, *args*, *timeout=- 1.0*, *byte_arrays=False*, *\*\*kwargs*)  
Call the given method, synchronously. :Since: 0.81.0

call_on_disconnection(*callable*)  
Arrange for callable to be called with one argument (this Connection object) when the Connection becomes disconnected.

Since  
0.83.0

close()  
Close the connection.

flush()  
Block until the outgoing message queue is empty.

get_is_authenticated() → bool  
Return true if this Connection was ever authenticated.

get_is_connected() → bool  
Return true if this Connection is connected.

get_object(*bus_name=None*, *object_path=None*, *introspect=True*, *\*\*kwargs*)  
Return a local proxy for the given remote object.

Method calls on the proxy are translated into method calls on the remote object.

Parameters  
bus_namestr  
A bus name (either the unique name or a well-known name) of the application owning the object. The keyword argument named_service is a deprecated alias for this.

object_pathstr  
The object path of the desired object

introspectbool  
If true (default), attempt to introspect the remote object to find out supported methods and their signatures

Returns  
a dbus.proxies.ProxyObject

get_peer_unix_process_id() → long or None  
Get the UNIX process ID at the other end of the connection, if it has been authenticated. Return None if this is a non-UNIX platform or the connection has not been authenticated.

get_peer_unix_user() → long or None  
Get the UNIX user ID at the other end of the connection, if it has been authenticated. Return None if this is a non-UNIX platform or the connection has not been authenticated.

get_unique_name() → str  
Return this application’s unique name on this bus.

Raises DBusException  
if the connection has no unique name yet (for Bus objects this can’t happen, for peer-to-peer connections this means you haven’t called set_unique_name)

get_unix_fd() → int or None  
Get the connection’s UNIX file descriptor, if any.

This can be used for SELinux access control checks with `getpeercon()` for example. **Do not** read or write to the file descriptor, or try to `select()` on it.

list_exported_child_objects(*path: str*) → list of str  
Return a list of the names of objects exported on this Connection as direct children of the given object path.

Each name returned may be converted to a valid object path using `dbus.ObjectPath('%s%s%s'`` ``%`` ``(path,`` ``(path`` ``!=`` ``'/'`` ``and`` ``'/'`` ``or`` ``''),`` ``name))`. For the purposes of this function, every parent or ancestor of an exported object is considered to be an exported object, even if it’s only an object synthesized by the library to support introspection.

remove_message_filter(*callable*)  
Remove the given message filter (see add_message_filter for details).

Raises LookupError  
The given callable is not among the registered filters

remove_signal_receiver(*handler_or_match*, *signal_name=None*, *dbus_interface=None*, *bus_name=None*, *path=None*, *\*\*keywords*)  

send_message(*msg*) → long  
Queue the given message for sending, and return the message serial number.

Parameters  
msgdbus.lowlevel.Message  
The message to be sent.

send_message_with_reply(*msg*, *reply_handler*, *timeout_s=- 1*, *require_main_loop=False*) → dbus.lowlevel.PendingCall  
Queue the message for sending; expect a reply via the returned PendingCall, which can also be used to cancel the pending call.

Parameters  
msgdbus.lowlevel.Message  
The message to be sent

reply_handlercallable  
Asynchronous reply handler: will be called with one positional parameter, a Message instance representing the reply.

timeout_sfloat  
If the reply takes more than this many seconds, a timeout error will be created locally and raised instead. If this timeout is negative (default), a sane default (supplied by libdbus) is used.

require_main_loopbool  
If True, raise RuntimeError if this Connection does not have a main loop configured. If False (default) and there is no main loop, you are responsible for calling block() on the PendingCall.

send_message_with_reply_and_block(*msg*, *timeout_s=- 1*) → dbus.lowlevel.Message  
Send the message and block while waiting for a reply.

This does not re-enter the main loop, so it can lead to a deadlock, if the called method tries to make a synchronous call to a method in this application. As such, it’s probably a bad idea.

Parameters  
msgdbus.lowlevel.Message  
The message to be sent

timeout_sfloat  
If the reply takes more than this many seconds, a timeout error will be created locally and raised instead. If this timeout is negative (default), a sane default (supplied by libdbus) is used.

Returns  
A dbus.lowlevel.Message instance (probably a dbus.lowlevel.MethodReturnMessage) on success

Raises dbus.DBusException  
On error (including if the reply arrives but is an error message)

set_allow_anonymous(*bool*)  
Allows anonymous clients. Call this on the server side of a connection in a on_connection_added callback

set_exit_on_disconnect(*bool*)  
Set whether the C function `_exit` will be called when this Connection becomes disconnected. This will cause the program to exit without calling any cleanup code or exit handlers.

The default is for this feature to be disabled for Connections and enabled for Buses.

set_unique_name(*str*)  
Set this application’s unique name on this bus. Raise ValueError if it has already been set.

<!-- -->

*class *dbus.connection.SignalMatch(*conn*, *sender*, *object_path*, *dbus_interface*, *member*, *handler*, *byte_arrays=False*, *sender_keyword=None*, *path_keyword=None*, *interface_keyword=None*, *member_keyword=None*, *message_keyword=None*, *destination_keyword=None*, *\*\*kwargs*)  
Bases: `object`

matches_removal_spec(*sender*, *object_path*, *dbus_interface*, *member*, *handler*, *\*\*kwargs*)  

maybe_handle_message(*message*)  

remove()  

*property *sender  

set_sender_name_owner(*new_name*)  
