# dbus.service module

*class *dbus.service.BusName(*name*, *bus=None*, *allow_replacement=False*, *replace_existing=False*, *do_not_queue=False*)  
Bases: `object`

A base class for exporting your own Named Services across the Bus.

When instantiated, objects of this class attempt to claim the given well-known name on the given bus for the current process. The name is released when the BusName object becomes unreferenced.

If a well-known name is requested multiple times, multiple references to the same BusName object will be returned.

Caveats  
- Assumes that named services are only ever requested using this class - if you request names from the bus directly, confusion may occur.

- Does not handle queueing.

get_bus()  
Get the Bus this Service is on

get_name()  
Get the name of this service

<!-- -->

*class *dbus.service.FallbackObject(*conn=None*, *object_path=None*)  
Bases: `dbus.service.Object`

An object that implements an entire subtree of the object-path tree.

Since  
0.82.0

Introspect(*object_path*, *connection*)  
Return a string of XML encoding this object’s supported interfaces, methods and signals.

SUPPORTS_MULTIPLE_CONNECTIONS* = False*  
If True, this object can be made available on more than one connection. If True but SUPPORTS_MULTIPLE_OBJECT_PATHS is False, the object must have the same object path on all its connections.

SUPPORTS_MULTIPLE_OBJECT_PATHS* = True*  
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

*property *connection  
The Connection on which this object is available. Access raises AttributeError if there is no Connection, or more than one Connection.

Changed in 0.82.0: AttributeError can be raised.

*property *locations  
An iterable over tuples representing locations at which this object is available.

Each tuple has at least two items, but may have more in future versions of dbus-python, so do not rely on their exact length. The first two items are the dbus.connection.Connection and the object path.

Since  
0.82.0

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

<!-- -->

*class *dbus.service.Object(*conn=None*, *object_path=None*, *bus_name=None*)  
Bases: `dbus.service.Interface`

A base class for exporting your own Objects across the Bus.

Just inherit from Object and mark exported methods with the @dbus.service.method or @dbus.service.signal decorator.

Example:

    class Example(dbus.service.object):
        def __init__(self, object_path):
            dbus.service.Object.__init__(self, dbus.SessionBus(), path)
            self._last_input = None

        @dbus.service.method(interface='com.example.Sample',
                             in_signature='v', out_signature='s')
        def StringifyVariant(self, var):
            self.LastInputChanged(var)      # emits the signal
            return str(var)

        @dbus.service.signal(interface='com.example.Sample',
                             signature='v')
        def LastInputChanged(self, var):
            # run just before the signal is actually emitted
            # just put "pass" if nothing should happen
            self._last_input = var

        @dbus.service.method(interface='com.example.Sample',
                             in_signature='', out_signature='v')
        def GetLastInput(self):
            return self._last_input

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

*property *connection  
The Connection on which this object is available. Access raises AttributeError if there is no Connection, or more than one Connection.

Changed in 0.82.0: AttributeError can be raised.

*property *locations  
An iterable over tuples representing locations at which this object is available.

Each tuple has at least two items, but may have more in future versions of dbus-python, so do not rely on their exact length. The first two items are the dbus.connection.Connection and the object path.

Since  
0.82.0

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

<!-- -->

dbus.service.method(*dbus_interface*, *in_signature=None*, *out_signature=None*, *async_callbacks=None*, *sender_keyword=None*, *path_keyword=None*, *destination_keyword=None*, *message_keyword=None*, *connection_keyword=None*, *byte_arrays=False*, *rel_path_keyword=None*, *\*\*kwargs*)  
Factory for decorators used to mark methods of a dbus.service.Object to be exported on the D-Bus.

The decorated method will be exported over D-Bus as the method of the same name on the given D-Bus interface.

Parameters  
dbus_interfacestr  
Name of a D-Bus interface

in_signaturestr or None  
If not None, the signature of the method parameters in the usual D-Bus notation

out_signaturestr or None  
If not None, the signature of the return value in the usual D-Bus notation

async_callbackstuple containing (str,str), or None  
If None (default) the decorated method is expected to return values matching the out_signature as usual, or raise an exception on error. If not None, the following applies:

async_callbacks contains the names of two keyword arguments to the decorated function, which will be used to provide a success callback and an error callback (in that order).

When the decorated method is called via the D-Bus, its normal return value will be ignored; instead, a pair of callbacks are passed as keyword arguments, and the decorated method is expected to arrange for one of them to be called.

On success the success callback must be called, passing the results of this method as positional parameters in the format given by the out_signature.

On error the decorated method may either raise an exception before it returns, or arrange for the error callback to be called with an Exception instance as parameter.

sender_keywordstr or None  
If not None, contains the name of a keyword argument to the decorated function, conventionally `'sender'`. When the method is called, the sender’s unique name will be passed as this keyword argument.

path_keywordstr or None  
If not None (the default), the decorated method will receive the destination object path as a keyword argument with this name. Normally you already know the object path, but in the case of “fallback paths” you’ll usually want to use the object path in the method’s implementation.

For fallback objects, rel_path_keyword (new in 0.82.2) is likely to be more useful.

Since  
0.80.0?

rel_path_keywordstr or None  
If not None (the default), the decorated method will receive the destination object path, relative to the path at which the object was exported, as a keyword argument with this name. For non-fallback objects the relative path will always be ‘/’.

Since  
0.82.2

destination_keywordstr or None  
If not None (the default), the decorated method will receive the destination bus name as a keyword argument with this name. Included for completeness - you shouldn’t need this.

Since  
0.80.0?

message_keywordstr or None  
If not None (the default), the decorated method will receive the dbus.lowlevel.MethodCallMessage as a keyword argument with this name.

Since  
0.80.0?

connection_keywordstr or None  
If not None (the default), the decorated method will receive the dbus.connection.Connection as a keyword argument with this name. This is generally only useful for objects that are available on more than one connection.

Since  
0.82.0

utf8_stringsbool  
If False (default), D-Bus strings are passed to the decorated method as objects of class dbus.String, a unicode subclass.

If True, D-Bus strings are passed to the decorated method as objects of class dbus.UTF8String, a str subclass guaranteed to be encoded in UTF-8.

This option does not affect object-paths and signatures, which are always 8-bit strings (str subclass) encoded in ASCII.

Since  
0.80.0

byte_arraysbool  
If False (default), a byte array will be passed to the decorated method as an Array (a list subclass) of Byte objects.

If True, a byte array will be passed to the decorated method as a ByteArray, a str subclass. This is usually what you want, but is switched off by default to keep dbus-python’s API consistent.

Since  
0.80.0

<!-- -->

dbus.service.signal(*dbus_interface*, *signature=None*, *path_keyword=None*, *rel_path_keyword=None*)  
Factory for decorators used to mark methods of a dbus.service.Object to emit signals on the D-Bus.

Whenever the decorated method is called in Python, after the method body is executed, a signal with the same name as the decorated method, with the given D-Bus interface, will be emitted from this object.

Parameters  
dbus_interfacestr  
The D-Bus interface whose signal is emitted

signaturestr  
The signature of the signal in the usual D-Bus notation

path_keywordstr or None  
A keyword argument to the decorated method. If not None, that argument will not be emitted as an argument of the signal, and when the signal is emitted, it will appear to come from the object path given by the keyword argument.

Note that when calling the decorated method, you must always pass in the object path as a keyword argument, not as a positional argument.

This keyword argument cannot be used on objects where the class attribute `SUPPORTS_MULTIPLE_OBJECT_PATHS` is true.

Deprecated  
since 0.82.0. Use rel_path_keyword instead.

rel_path_keywordstr or None  
A keyword argument to the decorated method. If not None, that argument will not be emitted as an argument of the signal.

When the signal is emitted, if the named keyword argument is given, the signal will appear to come from the object path obtained by appending the keyword argument to the object’s object path. This is useful to implement “fallback objects” (objects which own an entire subtree of the object-path tree).

If the object is available at more than one object-path on the same or different connections, the signal will be emitted at an appropriate object-path on each connection - for instance, if the object is exported at /abc on connection 1 and at /def and /x/y/z on connection 2, and the keyword argument is /foo, then signals will be emitted from /abc/foo and /def/foo on connection 1, and /x/y/z/foo on connection 2.

Since  
0.82.0
