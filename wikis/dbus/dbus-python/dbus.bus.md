# dbus.bus module

*class *dbus.bus.BusConnection(*address_or_type=0*, *mainloop=None*)  
Bases: `dbus.connection.Connection`

A connection to a D-Bus daemon that implements the `org.freedesktop.DBus` pseudo-service.

Since  
0.81.0

ProxyObjectClass  
alias of `dbus.proxies.ProxyObject`

START_REPLY_ALREADY_RUNNING* = 2*  

START_REPLY_SUCCESS* = 1*  

TYPE_SESSION* = 0*  
Represents a session bus (same as the global dbus.BUS_SESSION)

TYPE_STARTER* = 2*  
Represents the bus that started this service by activation (same as the global dbus.BUS_STARTER)

TYPE_SYSTEM* = 1*  
Represents the system bus (same as the global dbus.BUS_SYSTEM)

activate_name_owner(*bus_name*)  
Return the unique name for the given bus name, activating it if necessary and possible.

If the name is already unique or this connection is not to a bus daemon, just return it.

Returns  
a bus name. If the given bus_name exists, the returned name identifies its current owner; otherwise the returned name does not exist.

Raises DBusException  
if the implementation has failed to activate the given bus name.

Since  
0.81.0

add_match_string(*rule*)  
Arrange for this application to receive messages on the bus that match the given rule. This version will block.

Parameters  
rulestr  
The match rule

Raises DBusExceptionDBusException  
on error.

Since  
0.80.0

add_match_string_non_blocking(*rule*)  
Arrange for this application to receive messages on the bus that match the given rule. This version will not block, but any errors will be ignored.

Parameters  
rulestr  
The match rule

Raises DBusExceptionDBusException  
on error.

Since  
0.80.0

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

get_name_owner(*bus_name*)  
Return the unique connection name of the primary owner of the given name.

Raises DBusExceptionDBusException  
if the bus_name has no owner

Since  
0.81.0

get_object(*bus_name*, *object_path*, *introspect=True*, *follow_name_owner_changes=False*, *\*\*kwargs*)  
Return a local proxy for the given remote object.

Method calls on the proxy are translated into method calls on the remote object.

Parameters  
bus_namestr  
A bus name (either the unique name or a well-known name) of the application owning the object. The keyword argument named_service is a deprecated alias for this.

object_pathstr  
The object path of the desired object

introspectbool  
If true (default), attempt to introspect the remote object to find out supported methods and their signatures

follow_name_owner_changesbool  
If the object path is a well-known name and this parameter is false (default), resolve the well-known name to the unique name of its current owner and bind to that instead; if the ownership of the well-known name changes in future, keep communicating with the original owner. This is necessary if the D-Bus API used is stateful.

If the object path is a well-known name and this parameter is true, whenever the well-known name changes ownership in future, bind to the new owner, if any.

If the given object path is a unique name, this parameter has no effect.

Returns  
a dbus.proxies.ProxyObject

Raises DBusExceptionDBusException  
if resolving the well-known name to a unique name fails

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

get_unix_user(*bus_name*)  
Get the numeric uid of the process owning the given bus name.

Parameters  
bus_namestr  
A bus name, either unique or well-known

Returns  
a dbus.UInt32

Since  
0.80.0

list_activatable_names()  
Return a list of all names that can be activated on the bus.

Returns  
a dbus.Array of dbus.UTF8String

Since  
0.81.0

list_exported_child_objects(*path: str*) → list of str  
Return a list of the names of objects exported on this Connection as direct children of the given object path.

Each name returned may be converted to a valid object path using `dbus.ObjectPath('%s%s%s'`` ``%`` ``(path,`` ``(path`` ``!=`` ``'/'`` ``and`` ``'/'`` ``or`` ``''),`` ``name))`. For the purposes of this function, every parent or ancestor of an exported object is considered to be an exported object, even if it’s only an object synthesized by the library to support introspection.

list_names()  
Return a list of all currently-owned names on the bus.

Returns  
a dbus.Array of dbus.UTF8String

Since  
0.81.0

name_has_owner(*bus_name*)  
Return True iff the given bus name has an owner on this bus.

Parameters  
bus_namestr  
The bus name to look up

Returns  
a bool

release_name(*name*)  
Release a bus name.

Parameters  
namestr  
The well-known name to be released

Returns  
RELEASE_NAME_REPLY_RELEASED, RELEASE_NAME_REPLY_NON_EXISTENT or RELEASE_NAME_REPLY_NOT_OWNER

Raises DBusExceptionDBusException  
if the bus daemon cannot be contacted or returns an error.

remove_match_string(*rule*)  
Arrange for this application to receive messages on the bus that match the given rule. This version will block.

Parameters  
rulestr  
The match rule

Raises DBusExceptionDBusException  
on error.

Since  
0.80.0

remove_match_string_non_blocking(*rule*)  
Arrange for this application to receive messages on the bus that match the given rule. This version will not block, but any errors will be ignored.

Parameters  
rulestr  
The match rule

Raises DBusExceptionDBusException  
on error.

Since  
0.80.0

remove_message_filter(*callable*)  
Remove the given message filter (see add_message_filter for details).

Raises LookupError  
The given callable is not among the registered filters

remove_signal_receiver(*handler_or_match*, *signal_name=None*, *dbus_interface=None*, *bus_name=None*, *path=None*, *\*\*keywords*)  

request_name(*name*, *flags=0*)  
Request a bus name.

Parameters  
namestr  
The well-known name to be requested

flagsdbus.UInt32  
A bitwise-OR of 0 or more of the flags NAME_FLAG_ALLOW_REPLACEMENT, NAME_FLAG_REPLACE_EXISTING and NAME_FLAG_DO_NOT_QUEUE

Returns  
REQUEST_NAME_REPLY_PRIMARY_OWNER, REQUEST_NAME_REPLY_IN_QUEUE, REQUEST_NAME_REPLY_EXISTS or REQUEST_NAME_REPLY_ALREADY_OWNER

Raises DBusExceptionDBusException  
if the bus daemon cannot be contacted or returns an error.

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

start_service_by_name(*bus_name*, *flags=0*)  
Start a service which will implement the given bus name on this Bus.

Parameters  
bus_namestr  
The well-known bus name to be activated.

flagsdbus.UInt32  
Flags to pass to StartServiceByName (currently none are defined)

Returns  
A tuple of 2 elements. The first is always True, the second is either START_REPLY_SUCCESS or START_REPLY_ALREADY_RUNNING.

Raises DBusExceptionDBusException  
if the service could not be started.

Since  
0.80.0

watch_name_owner(*bus_name*, *callback*)  
Watch the unique connection name of the primary owner of the given name.

callback will be called with one argument, which is either the unique connection name, or the empty string (meaning the name is not owned).

Since  
0.81.0
