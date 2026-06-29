# dbus package API reference

## Submodules

## Deprecated submodules

## Module contents

Implements the public API for a D-Bus client. See the dbus.service module to export objects or claim well-known names.

*class *dbus.Array(*\[iterable\]\[, signature\]\[, variant_level\]*)  
Bases: `list`

An array of similar items, implemented as a subtype of list.

As currently implemented, an Array behaves just like a list, but with the addition of a `signature` property set by the constructor; conversion of its items to D-Bus types is only done when it’s sent in a Message. This might change in future so validation is done earlier.

`variant_level` must be non-negative; the default is 0.

`signature` is the D-Bus signature string for a single element of the array, or None. If not None it must represent a single complete type, the type of a single array item; the signature of the whole Array may be obtained by prepending `a` to the given signature.

If None (the default), when the Array is sent over D-Bus, the item signature will be guessed from the first element.

signature  
The D-Bus signature of each element of this Array (a Signature instance)

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an array, this is represented in Python by an Array with variant_level==2.

<!-- -->

*class *dbus.Boolean(*value: bool*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

A boolean, represented as a subtype of `int` (not `bool`, because `bool` cannot be subclassed).

`value` is converted to 0 or 1 as if by `int(bool(value))`.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a boolean, this is represented in Python by a Boolean with variant_level==2.

<!-- -->

*class *dbus.Bus(*bus_type=0*, *private=False*, *mainloop=None*)  
Bases: `dbus.bus.BusConnection`

A connection to one of three possible standard buses, the SESSION, SYSTEM, or STARTER bus. This class manages shared connections to those buses.

If you’re trying to subclass Bus, you may be better off subclassing BusConnection, which doesn’t have all this magic.

close()  
Close the connection.

get_connection()  
Return self, for backwards compatibility with earlier dbus-python versions where Bus was not a subclass of Connection.

Deprecated  
since 0.80.0

*static *get_session(*private=False*)  
Static method that returns a connection to the session bus.

Parameters  
privatebool  
If true, do not return a shared connection.

*static *get_starter(*private=False*)  
Static method that returns a connection to the starter bus.

Parameters  
privatebool  
If true, do not return a shared connection.

*static *get_system(*private=False*)  
Static method that returns a connection to the system bus.

Parameters  
privatebool  
If true, do not return a shared connection.

<!-- -->

*class *dbus.Byte(*integer or bytes of length 1*\[, *variant_level*\])  
Bases: `_dbus_bindings._LongBase`

An unsigned byte: a subtype of int, with range restricted to \[0, 255\].

A Byte b may be converted to a `str` of length 1 via `str(b)`` ``==`` ``chr(b)` (Python 2) or to a `bytes` of length 1 via `bytes([b])` (Python 3).

Most of the time you don’t want to use this class - it mainly exists for symmetry with the other D-Bus types. See dbus.ByteArray for a better way to handle arrays of Byte.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a byte, this is represented in Python by a Byte with variant_level==2.

<!-- -->

*class *dbus.ByteArray(*str*)  
Bases: `_dbus_bindings._BytesBase`

ByteArray is a subtype of `bytes` (an alias for `str` in Python 2 but a distinct type in Python 3) which can be used when you want an efficient immutable representation of a D-Bus byte array (signature `ay`).

By default, when byte arrays are converted from D-Bus to Python, they come out as a dbus.Array of dbus.Byte. This is just for symmetry with the other D-Bus types - in practice, what you usually want is the byte array represented as a string, using this class. To get this, pass the `byte_arrays=True` keyword argument to any of these methods:

- any D-Bus method proxy, or `connect_to_signal`, on the objects returned by Bus.get_object

- any D-Bus method on a dbus.Interface

- dbus.Interface.connect_to_signal

- Bus.add_signal_receiver

Import via:

    from dbus import ByteArray

Constructor:

    ByteArray(str)

<!-- -->

*exception *dbus.DBusException(*\*args*, *\*\*kwargs*)  
Bases: `Exception`

get_dbus_message()  

get_dbus_name()  

include_traceback* = False*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

<!-- -->

*class *dbus.Dictionary(*mapping_or_iterable=()*, *signature=None*, *variant_level=0*)  
Bases: `dict`

An mapping whose keys are similar and whose values are similar, implemented as a subtype of dict.

As currently implemented, a Dictionary behaves just like a dict, but with the addition of a `signature` property set by the constructor; conversion of its items to D-Bus types is only done when it’s sent in a Message. This may change in future so validation is done earlier.

`variant_level` must be non-negative; the default is 0.

`signature` is either a string or None. If a string, it must consist of exactly two complete type signatures, representing the ‘key’ type (which must be a primitive type, i.e. one of “bdginoqstuxy”) and the ‘value’ type. The signature of the whole Dictionary will be `a{xx}` where `xx` is replaced by the given signature.

If it is None (the default), when the Dictionary is sent over D-Bus, the key and value signatures will be guessed from an arbitrary element of the Dictionary.

signature  
The D-Bus signature of each key in this Dictionary, followed by that of each value in this Dictionary, as a Signature instance.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a dictionary, this is represented in Python by a Dictionary with variant_level==2.

<!-- -->

*class *dbus.Double(*x=0*, */*)  
Bases: `_dbus_bindings._FloatBase`

A double-precision floating point number (a subtype of float).

<!-- -->

*class *dbus.Int16(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

A signed 16-bit integer between -0x8000 and +0x7FFF, represented as a subtype of int.

value must be within the allowed range, or OverflowError will be raised.

> variant_level must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an int16, this is represented in Python by an Int16 with variant_level==2.

<!-- -->

*class *dbus.Int32(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

A signed 32-bit integer between -0x8000 0000 and +0x7FFF FFFF, represented as a subtype of `int`.

`value` must be within the allowed range, or OverflowError will be raised.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an int32, this is represented in Python by an Int32 with variant_level==2.

<!-- -->

*class *dbus.Int64(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

A signed 64-bit integer between -0x8000 0000 0000 0000 and +0x7FFF FFFF FFFF FFFF, represented as a subtype of `long` in Python 2 or `int` in Python 3.

Note that this may be changed in future to be a subtype of int on 64-bit platforms; applications should not rely on either behaviour.

`value` must be within the allowed range, or OverflowError will be raised.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an int64, this is represented in Python by an Int64 with variant_level==2.

<!-- -->

*class *dbus.Interface(*object*, *dbus_interface*)  
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

*exception *dbus.IntrospectionParserException(*msg=''*)  
Bases: `dbus.exceptions.DBusException`

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

<!-- -->

*exception *dbus.MissingErrorHandlerException  
Bases: `dbus.exceptions.DBusException`

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

<!-- -->

*exception *dbus.MissingReplyHandlerException  
Bases: `dbus.exceptions.DBusException`

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

<!-- -->

*exception *dbus.NameExistsException(*name*)  
Bases: `dbus.exceptions.DBusException`

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

<!-- -->

*class *dbus.ObjectPath(*path: str*\[, *variant_level: int=0*\])  
Bases: `_dbus_bindings._StrBase`

A D-Bus object path, such as `/com/example/MyApp/Documents/abc`.

ObjectPath is a subtype of `str`, and object-paths behave like strings.

path must be an ASCII string following the syntax of object paths. variant_level must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an object path, this is represented in Python by an ObjectPath with variant_level==2.

<!-- -->

*class *dbus.SessionBus(*private=False*, *mainloop=None*)  
Bases: `dbus._dbus.Bus`

The session (current login) message bus.

<!-- -->

*class *dbus.Signature(*value: str or unicode*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._StrBase`

A string subclass whose values are restricted to valid D-Bus signatures. When iterated over, instead of individual characters it produces Signature instances representing single complete types.

`value` must be a valid D-Bus signature (zero or more single complete types).

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a signature, this is represented in Python by a Signature with variant_level==2.

<!-- -->

*class *dbus.StarterBus(*private=False*, *mainloop=None*)  
Bases: `dbus._dbus.Bus`

The bus that activated this process (only valid if this process was launched by DBus activation).

<!-- -->

*class *dbus.String(*value: str or unicode*\[, *variant_level: int*\])  
Bases: `str`

A string represented using Unicode - a subtype of `unicode` (Python 2) or `str` (Python 3).

All strings on D-Bus are required to be valid Unicode; in the “wire protocol” they’re transported as UTF-8.

By default, when strings are converted from D-Bus to Python, they come out as this class. In Python 2, if you prefer to get UTF-8 strings (as instances of a subtype of str) or you want to avoid the conversion overhead of going from UTF-8 to Python’s internal Unicode representation, see the documentation for dbus.UTF8String.

variant_level must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an array, this is represented in Python by a String or UTF8String with variant_level==2.

<!-- -->

*class *dbus.Struct(*iterable*, *signature=None*, *variant_level=0*)  
Bases: `tuple`

An structure containing items of possibly distinct types.

D-Bus structs may not be empty, so the iterable argument is required and may not be an empty iterable.

`signature` is either None, or a string representing the contents of the struct as one or more complete type signatures. The overall signature of the struct will be the given signature enclosed in parentheses, `()`.

If the signature is None (default) it will be guessed from the types of the items during construction.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a struct, this is represented in Python by a Struct with variant_level==2.

<!-- -->

*class *dbus.SystemBus(*private=False*, *mainloop=None*)  
Bases: `dbus._dbus.Bus`

The system-wide message bus.

<!-- -->

*class *dbus.UInt16(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

An unsigned 16-bit integer between 0 and 0xFFFF, represented as a subtype of `int`.

`value` must be within the allowed range, or OverflowError will be raised.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a uint16, this is represented in Python by a UInt16 with variant_level==2.

<!-- -->

*class *dbus.UInt32(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

An unsigned 32-bit integer between 0 and 0xFFFF FFFF, represented as a subtype of `long` in Python 2 or `int` in Python 3.

`value` must be within the allowed range, or OverflowError will be raised.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a uint32, this is represented in Python by a UInt32 with variant_level==2.

<!-- -->

*class *dbus.UInt64(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

An unsigned 64-bit integer between 0 and 0xFFFF FFFF FFFF FFFF, subtype of `long` in Python 2 or `int` in Python 3.

`value` must be within the allowed range, or OverflowError will be raised.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a uint64, this is represented in Python by a UInt64 with variant_level==2.

<!-- -->

*exception *dbus.UnknownMethodException(*method*)  
Bases: `dbus.exceptions.DBusException`

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

<!-- -->

*exception *dbus.ValidationException(*msg=''*)  
Bases: `dbus.exceptions.DBusException`

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

<!-- -->

dbus.get_default_main_loop() → object  
Return the global default dbus-python main loop wrapper, which is used when no main loop wrapper is passed to the Connection constructor.

If None, there is no default and you should always pass the mainloop parameter to the constructor - if you don’t, then asynchronous calls, connecting to signals and exporting objects will raise an exception. There is no default until set_default_main_loop is called.

<!-- -->

dbus.set_default_main_loop(*object*)  
Change the global default dbus-python main loop wrapper, which is used when no main loop wrapper is passed to the Connection constructor.

If None, return to the initial situation: there is no default, and you must always pass the mainloop parameter to the constructor.

Two types of main loop wrapper are planned in dbus-python. Native main-loop wrappers are instances of dbus.mainloop.NativeMainLoop supplied by extension modules like dbus.mainloop.glib: they have no Python API, but connect themselves to `libdbus` using native code. Python main-loop wrappers are not yet implemented. They will be objects supporting the interface defined by dbus.mainloop.MainLoop, with an API entirely based on Python methods.

<!-- -->

dbus.validate_bus_name(*name*, *allow_unique=True*, *allow_well_known=True*)  
Raise ValueError if the argument is not a valid bus name.

By default both unique and well-known names are accepted.

Parameters  
namestr  
The name to be validated

allow_uniquebool  
If False, unique names of the form :1.123 will be rejected

allow_well_knownbool  
If False, well-known names of the form com.example.Foo will be rejected

Since  
0.80

<!-- -->

dbus.validate_error_name(*name*)  
Raise ValueError if the given string is not a valid error name.

Since  
0.80

<!-- -->

dbus.validate_interface_name(*name*)  
Raise ValueError if the given string is not a valid interface name.

Since  
0.80

<!-- -->

dbus.validate_member_name(*name*)  
Raise ValueError if the argument is not a valid member (signal or method) name.

Since  
0.80

<!-- -->

dbus.validate_object_path(*name*)  
Raise ValueError if the given string is not a valid object path.

Since  
0.80
