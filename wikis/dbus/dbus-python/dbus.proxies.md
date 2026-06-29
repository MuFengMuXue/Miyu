# dbus.proxies module

*class *dbus.proxies.Interface(*object*, *dbus_interface*)  
Bases: `object`

An interface into a remote object.

An Interface can be used to wrap ProxyObjects so that calls can be routed to their correct D-Bus interface.

*property *bus_name  
The bus name to which the underlying proxy object is bound

connect_to_signal(*signal_name*, *handler_function*, *dbus_interface=None*, *\*\*keywords*)  
Arrange for a function to be called when the given signal is emitted.

The parameters and keyword arguments are the same as for dbus.proxies.ProxyObject.connect_to_signal, except that if dbus_interface is None (the default), the D-Bus interface that was passed to the Interface constructor is used.

*property *dbus_interface  
The D-Bus interface represented

get_dbus_method(*member*, *dbus_interface=None*)  
Return a proxy method representing the given D-Bus method.

This is the same as dbus.proxies.ProxyObject.get_dbus_method except that if dbus_interface is None (the default), the D-Bus interface that was passed to the Interface constructor is used.

*property *object_path  
The D-Bus object path of the underlying object

*property *proxy_object  
The underlying proxy object

*property *requested_bus_name  
The bus name which was requested when the underlying object was created

<!-- -->

*class *dbus.proxies.ProxyObject(*conn=None*, *bus_name=None*, *object_path=None*, *introspect=True*, *follow_name_owner_changes=False*, *\*\*kwargs*)  
Bases: `object`

A proxy to the remote Object.

A ProxyObject is provided by the Bus. ProxyObjects have member functions, and can be called like normal Python objects.

DeferredMethodClass  
alias of `dbus.proxies._DeferredMethod`

INTROSPECT_STATE_DONT_INTROSPECT* = 0*  

INTROSPECT_STATE_INTROSPECT_DONE* = 2*  

INTROSPECT_STATE_INTROSPECT_IN_PROGRESS* = 1*  

ProxyMethodClass  
alias of `dbus.proxies._ProxyMethod`

*property *bus_name  
The bus name to which this proxy is bound. (Read-only, may change.)

If the proxy was instantiated using a unique name, this property is that unique name.

If the proxy was instantiated with a well-known name and with `follow_name_owner_changes` set false (the default), this property is the unique name of the connection that owned that well-known name when the proxy was instantiated, which might not actually own the requested well-known name any more.

If the proxy was instantiated with a well-known name and with `follow_name_owner_changes` set true, this property is that well-known name.

connect_to_signal(*signal_name*, *handler_function*, *dbus_interface=None*, *\*\*keywords*)  
Arrange for the given function to be called when the given signal is received.

Parameters  
signal_namestr  
The name of the signal

handler_functioncallable  
A function to be called when the signal is emitted by the remote object. Its positional arguments will be the arguments of the signal; optionally, it may be given keyword arguments as described below.

dbus_interfacestr  
Optional interface with which to qualify the signal name. If None (the default) the handler will be called whenever a signal of the given member name is received, whatever its interface.

Keywords  
utf8_stringsbool  
If True, the handler function will receive any string arguments as dbus.UTF8String objects (a subclass of str guaranteed to be UTF-8). If False (default) it will receive any string arguments as dbus.String objects (a subclass of unicode).

byte_arraysbool  
If True, the handler function will receive any byte-array arguments as dbus.ByteArray objects (a subclass of str). If False (default) it will receive any byte-array arguments as a dbus.Array of dbus.Byte (subclasses of: a list of ints).

sender_keywordstr  
If not None (the default), the handler function will receive the unique name of the sending endpoint as a keyword argument with this name

destination_keywordstr  
If not None (the default), the handler function will receive the bus name of the destination (or None if the signal is a broadcast, as is usual) as a keyword argument with this name.

interface_keywordstr  
If not None (the default), the handler function will receive the signal interface as a keyword argument with this name.

member_keywordstr  
If not None (the default), the handler function will receive the signal name as a keyword argument with this name.

path_keywordstr  
If not None (the default), the handler function will receive the object-path of the sending object as a keyword argument with this name

message_keywordstr  
If not None (the default), the handler function will receive the dbus.lowlevel.SignalMessage as a keyword argument with this name.

arg…unicode or UTF-8 str  
If there are additional keyword parameters of the form `arg`*n*, match only signals where the *n*th argument is the value given for that keyword parameter. As of this time only string arguments can be matched (in particular, object paths and signatures can’t).

get_dbus_method(*member*, *dbus_interface=None*)  
Return a proxy method representing the given D-Bus method. The returned proxy method can be called in the usual way. For instance,

    proxy.get_dbus_method("Foo", dbus_interface='com.example.Bar')(123)

is equivalent to:

    proxy.Foo(123, dbus_interface='com.example.Bar')

or even:

    getattr(proxy, "Foo")(123, dbus_interface='com.example.Bar')

However, using get_dbus_method is the only way to call D-Bus methods with certain awkward names - if the author of a service implements a method called `connect_to_signal` or even `__getattr__`, you’ll need to use get_dbus_method to call them.

For services which follow the D-Bus convention of CamelCaseMethodNames this won’t be a problem.

*property *object_path  
The object-path of this proxy.

*property *requested_bus_name  
The bus name which was requested when this proxy was instantiated.
