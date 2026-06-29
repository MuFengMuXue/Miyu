# dbus.lowlevel module

Low-level interface to D-Bus.

*class *dbus.lowlevel.ErrorMessage(*reply_to: Message*, *error_name: str*, *error_message: str or None*)  
Bases: `dbus.lowlevel.Message`

An error message.

append(*\*args*, *\*\*kwargs*)  
Set the message’s arguments from the positional parameter, according to the signature given by the `signature` keyword parameter.

The following type conversions are supported:

| D-Bus (in signature) | Python |
|----|----|
| boolean (b) | any object (via bool()) |
| byte (y) | string of length 1 any integer |
| any integer type | any integer |
| double (d) | any float |
| object path | anything with a \_\_dbus_object_path\_\_ attribute |
| string, signature, object path | str (must be UTF-8) or unicode |
| dict (a{…}) | any mapping |
| array (a…) | any iterable over appropriate objects |
| struct ((…)) | any iterable over appropriate objects |
| variant | any object above (guess type as below) |

Here ‘any integer’ means anything on which int() or long() (as appropriate) will work, except for basestring subclasses. ‘Any float’ means anything on which float() will work, except for basestring subclasses.

If there is no signature, guess from the arguments using the static method Message.guess_signature.

copy(*) -\> Message (or subclass*)  
Deep-copy the message, resetting the serial number to zero.

get_allow_interactive_authorization(*bool*) → None  
Get allow interactive authorization flag.

get_args_list(*\*\*kwargs*) → list  
Return the message’s arguments. Keyword arguments control the translation of D-Bus types to Python:

Keywords  
byte_arraysbool  
If true, convert arrays of byte (signature ‘ay’) into dbus.ByteArray, a str subclass. In practice, this is usually what you want, but it’s off by default for consistency.

If false (default), convert them into a dbus.Array of Bytes.

Most of the type mappings should be fairly obvious:

| D-Bus | Python |
|----|----|
| byte (y) | dbus.Byte (int subclass) |
| bool (b) | dbus.Boolean (int subclass) |
| Signature (g) | dbus.Signature (str subclass) |
| intNN, uintNN | dbus.IntNN, dbus.UIntNN (int or long subclasses) |
| double (d) | dbus.Double |
| string (s) | dbus.String (unicode subclass) (or dbus.UTF8String, bytes subclass, if utf8_strings set) |
| Object path (o) | dbus.ObjectPath (str subclass) |
| dict (a{…}) | dbus.Dictionary |
| array (a…) | dbus.Array (list subclass) containing appropriate types |
| byte array (ay) | dbus.ByteArray (str subclass) if byte_arrays set; or list of Byte |
| struct ((…)) | dbus.Struct (tuple subclass) of appropriate types |
| variant (v) | contained type, but with variant_level \> 0 |

get_auto_start() → bool  
Return true if this message will cause an owner for the destination name to be auto-started.

get_destination() → str or None  
Return the message’s destination bus name, or None if none.

get_error_name() → str or None  

get_interface() → str or None  

get_member() → str or None  

get_no_reply() → bool  
Return true if this message need not be replied to.

get_path() → ObjectPath or None  
Return the message’s destination object path (if it’s a method call) or source object path (if it’s a method reply or a signal) or None (if it has no path).

get_path_decomposed() → list of str, or None  
Return a list of path components (e.g. /foo/bar -\> \[‘foo’,’bar’\], / -\> \[\]) or None if the message has no associated path.

get_reply_serial() → long  
Returns the serial that the message is a reply to or 0 if none.

get_sender() → str or None  
Return the message’s sender unique name, or None if none.

get_serial() → long  
Returns the serial of a message or 0 if none has been specified.

The message’s serial number is provided by the application sending the message and is used to identify replies to this message. All messages received on a connection will have a serial, but messages you haven’t sent yet may return 0.

get_signature() → Signature or None  

get_type() → int  
Returns the type of the message.

*static *guess_signature(*\*args*) → Signature \[static method\]  
Guess a D-Bus signature which should be used to encode the given Python objects.

The signature is constructed as follows:

| Python | D-Bus |
|----|----|
| D-Bus type, variant_level \> 0 | variant (v) |
| D-Bus type, variant_level == 0 | the corresponding type |
| anything with a \_\_dbus_object_path\_\_ attribute | object path |
| bool | boolean (y) |
| any other int subclass | int32 (i) |
| any other long subclass | int64 (x) |
| any other float subclass | double (d) |
| any other str subclass | string (s) |
| any other unicode subclass | string (s) |
| any other tuple subclass | struct ((…)) |
| any other list subclass | array (a…), guess contents’ type according to type of first item |
| any other dict subclass | dict (a{…}), guess key, value type according to types for an arbitrary item |
| anything else | raise TypeError |

has_destination(*bus_name: str*) → bool  

has_interface(*interface: str or None*) → bool  

has_member(*name: str or None*) → bool  

has_path(*name: str or None*) → bool  

has_sender(*unique_name: str*) → bool  

has_signature(*signature: str*) → bool  

is_error(*error: str*) → bool  

is_method_call(*interface: str*, *member: str*) → bool  

is_signal(*interface: str*, *member: str*) → bool  

set_allow_interactive_authorization(*bool*) → None  
Set allow interactive authorization flag to this message.

set_auto_start(*bool*) → None  
Set whether this message will cause an owner for the destination name to be auto-started.

set_destination(*bus_name: str or None*)  

set_error_name(*name: str or None*)  

set_interface(*name: str or None*)  

set_member(*unique_name: str or None*)  

set_no_reply(*bool*) → None  
Set whether no reply to this message is required.

set_path(*name: str or None*)  

set_reply_serial(*bool*) → None  
Set the serial that this message is a reply to.

set_sender(*unique_name: str or None*)  

<!-- -->

*class *dbus.lowlevel.Message  
Bases: `object`

A message to be sent or received over a D-Bus Connection.

append(*\*args*, *\*\*kwargs*)  
Set the message’s arguments from the positional parameter, according to the signature given by the `signature` keyword parameter.

The following type conversions are supported:

| D-Bus (in signature) | Python |
|----|----|
| boolean (b) | any object (via bool()) |
| byte (y) | string of length 1 any integer |
| any integer type | any integer |
| double (d) | any float |
| object path | anything with a \_\_dbus_object_path\_\_ attribute |
| string, signature, object path | str (must be UTF-8) or unicode |
| dict (a{…}) | any mapping |
| array (a…) | any iterable over appropriate objects |
| struct ((…)) | any iterable over appropriate objects |
| variant | any object above (guess type as below) |

Here ‘any integer’ means anything on which int() or long() (as appropriate) will work, except for basestring subclasses. ‘Any float’ means anything on which float() will work, except for basestring subclasses.

If there is no signature, guess from the arguments using the static method Message.guess_signature.

copy(*) -\> Message (or subclass*)  
Deep-copy the message, resetting the serial number to zero.

get_allow_interactive_authorization(*bool*) → None  
Get allow interactive authorization flag.

get_args_list(*\*\*kwargs*) → list  
Return the message’s arguments. Keyword arguments control the translation of D-Bus types to Python:

Keywords  
byte_arraysbool  
If true, convert arrays of byte (signature ‘ay’) into dbus.ByteArray, a str subclass. In practice, this is usually what you want, but it’s off by default for consistency.

If false (default), convert them into a dbus.Array of Bytes.

Most of the type mappings should be fairly obvious:

| D-Bus | Python |
|----|----|
| byte (y) | dbus.Byte (int subclass) |
| bool (b) | dbus.Boolean (int subclass) |
| Signature (g) | dbus.Signature (str subclass) |
| intNN, uintNN | dbus.IntNN, dbus.UIntNN (int or long subclasses) |
| double (d) | dbus.Double |
| string (s) | dbus.String (unicode subclass) (or dbus.UTF8String, bytes subclass, if utf8_strings set) |
| Object path (o) | dbus.ObjectPath (str subclass) |
| dict (a{…}) | dbus.Dictionary |
| array (a…) | dbus.Array (list subclass) containing appropriate types |
| byte array (ay) | dbus.ByteArray (str subclass) if byte_arrays set; or list of Byte |
| struct ((…)) | dbus.Struct (tuple subclass) of appropriate types |
| variant (v) | contained type, but with variant_level \> 0 |

get_auto_start() → bool  
Return true if this message will cause an owner for the destination name to be auto-started.

get_destination() → str or None  
Return the message’s destination bus name, or None if none.

get_error_name() → str or None  

get_interface() → str or None  

get_member() → str or None  

get_no_reply() → bool  
Return true if this message need not be replied to.

get_path() → ObjectPath or None  
Return the message’s destination object path (if it’s a method call) or source object path (if it’s a method reply or a signal) or None (if it has no path).

get_path_decomposed() → list of str, or None  
Return a list of path components (e.g. /foo/bar -\> \[‘foo’,’bar’\], / -\> \[\]) or None if the message has no associated path.

get_reply_serial() → long  
Returns the serial that the message is a reply to or 0 if none.

get_sender() → str or None  
Return the message’s sender unique name, or None if none.

get_serial() → long  
Returns the serial of a message or 0 if none has been specified.

The message’s serial number is provided by the application sending the message and is used to identify replies to this message. All messages received on a connection will have a serial, but messages you haven’t sent yet may return 0.

get_signature() → Signature or None  

get_type() → int  
Returns the type of the message.

*static *guess_signature(*\*args*) → Signature \[static method\]  
Guess a D-Bus signature which should be used to encode the given Python objects.

The signature is constructed as follows:

| Python | D-Bus |
|----|----|
| D-Bus type, variant_level \> 0 | variant (v) |
| D-Bus type, variant_level == 0 | the corresponding type |
| anything with a \_\_dbus_object_path\_\_ attribute | object path |
| bool | boolean (y) |
| any other int subclass | int32 (i) |
| any other long subclass | int64 (x) |
| any other float subclass | double (d) |
| any other str subclass | string (s) |
| any other unicode subclass | string (s) |
| any other tuple subclass | struct ((…)) |
| any other list subclass | array (a…), guess contents’ type according to type of first item |
| any other dict subclass | dict (a{…}), guess key, value type according to types for an arbitrary item |
| anything else | raise TypeError |

has_destination(*bus_name: str*) → bool  

has_interface(*interface: str or None*) → bool  

has_member(*name: str or None*) → bool  

has_path(*name: str or None*) → bool  

has_sender(*unique_name: str*) → bool  

has_signature(*signature: str*) → bool  

is_error(*error: str*) → bool  

is_method_call(*interface: str*, *member: str*) → bool  

is_signal(*interface: str*, *member: str*) → bool  

set_allow_interactive_authorization(*bool*) → None  
Set allow interactive authorization flag to this message.

set_auto_start(*bool*) → None  
Set whether this message will cause an owner for the destination name to be auto-started.

set_destination(*bus_name: str or None*)  

set_error_name(*name: str or None*)  

set_interface(*name: str or None*)  

set_member(*unique_name: str or None*)  

set_no_reply(*bool*) → None  
Set whether no reply to this message is required.

set_path(*name: str or None*)  

set_reply_serial(*bool*) → None  
Set the serial that this message is a reply to.

set_sender(*unique_name: str or None*)  

<!-- -->

*class *dbus.lowlevel.MethodCallMessage(*destination: str or None*, *path: str*, *interface: str or None*, *method: str*)  
Bases: `dbus.lowlevel.Message`

A method-call message.

`destination` is the destination bus name, or None to send the message directly to the peer (usually the bus daemon).

`path` is the object-path of the object whose method is to be called.

`interface` is the interface qualifying the method name, or None to omit the interface from the message header.

`method` is the method name (member name).

append(*\*args*, *\*\*kwargs*)  
Set the message’s arguments from the positional parameter, according to the signature given by the `signature` keyword parameter.

The following type conversions are supported:

| D-Bus (in signature) | Python |
|----|----|
| boolean (b) | any object (via bool()) |
| byte (y) | string of length 1 any integer |
| any integer type | any integer |
| double (d) | any float |
| object path | anything with a \_\_dbus_object_path\_\_ attribute |
| string, signature, object path | str (must be UTF-8) or unicode |
| dict (a{…}) | any mapping |
| array (a…) | any iterable over appropriate objects |
| struct ((…)) | any iterable over appropriate objects |
| variant | any object above (guess type as below) |

Here ‘any integer’ means anything on which int() or long() (as appropriate) will work, except for basestring subclasses. ‘Any float’ means anything on which float() will work, except for basestring subclasses.

If there is no signature, guess from the arguments using the static method Message.guess_signature.

copy(*) -\> Message (or subclass*)  
Deep-copy the message, resetting the serial number to zero.

get_allow_interactive_authorization(*bool*) → None  
Get allow interactive authorization flag.

get_args_list(*\*\*kwargs*) → list  
Return the message’s arguments. Keyword arguments control the translation of D-Bus types to Python:

Keywords  
byte_arraysbool  
If true, convert arrays of byte (signature ‘ay’) into dbus.ByteArray, a str subclass. In practice, this is usually what you want, but it’s off by default for consistency.

If false (default), convert them into a dbus.Array of Bytes.

Most of the type mappings should be fairly obvious:

| D-Bus | Python |
|----|----|
| byte (y) | dbus.Byte (int subclass) |
| bool (b) | dbus.Boolean (int subclass) |
| Signature (g) | dbus.Signature (str subclass) |
| intNN, uintNN | dbus.IntNN, dbus.UIntNN (int or long subclasses) |
| double (d) | dbus.Double |
| string (s) | dbus.String (unicode subclass) (or dbus.UTF8String, bytes subclass, if utf8_strings set) |
| Object path (o) | dbus.ObjectPath (str subclass) |
| dict (a{…}) | dbus.Dictionary |
| array (a…) | dbus.Array (list subclass) containing appropriate types |
| byte array (ay) | dbus.ByteArray (str subclass) if byte_arrays set; or list of Byte |
| struct ((…)) | dbus.Struct (tuple subclass) of appropriate types |
| variant (v) | contained type, but with variant_level \> 0 |

get_auto_start() → bool  
Return true if this message will cause an owner for the destination name to be auto-started.

get_destination() → str or None  
Return the message’s destination bus name, or None if none.

get_error_name() → str or None  

get_interface() → str or None  

get_member() → str or None  

get_no_reply() → bool  
Return true if this message need not be replied to.

get_path() → ObjectPath or None  
Return the message’s destination object path (if it’s a method call) or source object path (if it’s a method reply or a signal) or None (if it has no path).

get_path_decomposed() → list of str, or None  
Return a list of path components (e.g. /foo/bar -\> \[‘foo’,’bar’\], / -\> \[\]) or None if the message has no associated path.

get_reply_serial() → long  
Returns the serial that the message is a reply to or 0 if none.

get_sender() → str or None  
Return the message’s sender unique name, or None if none.

get_serial() → long  
Returns the serial of a message or 0 if none has been specified.

The message’s serial number is provided by the application sending the message and is used to identify replies to this message. All messages received on a connection will have a serial, but messages you haven’t sent yet may return 0.

get_signature() → Signature or None  

get_type() → int  
Returns the type of the message.

*static *guess_signature(*\*args*) → Signature \[static method\]  
Guess a D-Bus signature which should be used to encode the given Python objects.

The signature is constructed as follows:

| Python | D-Bus |
|----|----|
| D-Bus type, variant_level \> 0 | variant (v) |
| D-Bus type, variant_level == 0 | the corresponding type |
| anything with a \_\_dbus_object_path\_\_ attribute | object path |
| bool | boolean (y) |
| any other int subclass | int32 (i) |
| any other long subclass | int64 (x) |
| any other float subclass | double (d) |
| any other str subclass | string (s) |
| any other unicode subclass | string (s) |
| any other tuple subclass | struct ((…)) |
| any other list subclass | array (a…), guess contents’ type according to type of first item |
| any other dict subclass | dict (a{…}), guess key, value type according to types for an arbitrary item |
| anything else | raise TypeError |

has_destination(*bus_name: str*) → bool  

has_interface(*interface: str or None*) → bool  

has_member(*name: str or None*) → bool  

has_path(*name: str or None*) → bool  

has_sender(*unique_name: str*) → bool  

has_signature(*signature: str*) → bool  

is_error(*error: str*) → bool  

is_method_call(*interface: str*, *member: str*) → bool  

is_signal(*interface: str*, *member: str*) → bool  

set_allow_interactive_authorization(*bool*) → None  
Set allow interactive authorization flag to this message.

set_auto_start(*bool*) → None  
Set whether this message will cause an owner for the destination name to be auto-started.

set_destination(*bus_name: str or None*)  

set_error_name(*name: str or None*)  

set_interface(*name: str or None*)  

set_member(*unique_name: str or None*)  

set_no_reply(*bool*) → None  
Set whether no reply to this message is required.

set_path(*name: str or None*)  

set_reply_serial(*bool*) → None  
Set the serial that this message is a reply to.

set_sender(*unique_name: str or None*)  

<!-- -->

*class *dbus.lowlevel.MethodReturnMessage(*method_call: MethodCallMessage*)  
Bases: `dbus.lowlevel.Message`

A method-return message.

append(*\*args*, *\*\*kwargs*)  
Set the message’s arguments from the positional parameter, according to the signature given by the `signature` keyword parameter.

The following type conversions are supported:

| D-Bus (in signature) | Python |
|----|----|
| boolean (b) | any object (via bool()) |
| byte (y) | string of length 1 any integer |
| any integer type | any integer |
| double (d) | any float |
| object path | anything with a \_\_dbus_object_path\_\_ attribute |
| string, signature, object path | str (must be UTF-8) or unicode |
| dict (a{…}) | any mapping |
| array (a…) | any iterable over appropriate objects |
| struct ((…)) | any iterable over appropriate objects |
| variant | any object above (guess type as below) |

Here ‘any integer’ means anything on which int() or long() (as appropriate) will work, except for basestring subclasses. ‘Any float’ means anything on which float() will work, except for basestring subclasses.

If there is no signature, guess from the arguments using the static method Message.guess_signature.

copy(*) -\> Message (or subclass*)  
Deep-copy the message, resetting the serial number to zero.

get_allow_interactive_authorization(*bool*) → None  
Get allow interactive authorization flag.

get_args_list(*\*\*kwargs*) → list  
Return the message’s arguments. Keyword arguments control the translation of D-Bus types to Python:

Keywords  
byte_arraysbool  
If true, convert arrays of byte (signature ‘ay’) into dbus.ByteArray, a str subclass. In practice, this is usually what you want, but it’s off by default for consistency.

If false (default), convert them into a dbus.Array of Bytes.

Most of the type mappings should be fairly obvious:

| D-Bus | Python |
|----|----|
| byte (y) | dbus.Byte (int subclass) |
| bool (b) | dbus.Boolean (int subclass) |
| Signature (g) | dbus.Signature (str subclass) |
| intNN, uintNN | dbus.IntNN, dbus.UIntNN (int or long subclasses) |
| double (d) | dbus.Double |
| string (s) | dbus.String (unicode subclass) (or dbus.UTF8String, bytes subclass, if utf8_strings set) |
| Object path (o) | dbus.ObjectPath (str subclass) |
| dict (a{…}) | dbus.Dictionary |
| array (a…) | dbus.Array (list subclass) containing appropriate types |
| byte array (ay) | dbus.ByteArray (str subclass) if byte_arrays set; or list of Byte |
| struct ((…)) | dbus.Struct (tuple subclass) of appropriate types |
| variant (v) | contained type, but with variant_level \> 0 |

get_auto_start() → bool  
Return true if this message will cause an owner for the destination name to be auto-started.

get_destination() → str or None  
Return the message’s destination bus name, or None if none.

get_error_name() → str or None  

get_interface() → str or None  

get_member() → str or None  

get_no_reply() → bool  
Return true if this message need not be replied to.

get_path() → ObjectPath or None  
Return the message’s destination object path (if it’s a method call) or source object path (if it’s a method reply or a signal) or None (if it has no path).

get_path_decomposed() → list of str, or None  
Return a list of path components (e.g. /foo/bar -\> \[‘foo’,’bar’\], / -\> \[\]) or None if the message has no associated path.

get_reply_serial() → long  
Returns the serial that the message is a reply to or 0 if none.

get_sender() → str or None  
Return the message’s sender unique name, or None if none.

get_serial() → long  
Returns the serial of a message or 0 if none has been specified.

The message’s serial number is provided by the application sending the message and is used to identify replies to this message. All messages received on a connection will have a serial, but messages you haven’t sent yet may return 0.

get_signature() → Signature or None  

get_type() → int  
Returns the type of the message.

*static *guess_signature(*\*args*) → Signature \[static method\]  
Guess a D-Bus signature which should be used to encode the given Python objects.

The signature is constructed as follows:

| Python | D-Bus |
|----|----|
| D-Bus type, variant_level \> 0 | variant (v) |
| D-Bus type, variant_level == 0 | the corresponding type |
| anything with a \_\_dbus_object_path\_\_ attribute | object path |
| bool | boolean (y) |
| any other int subclass | int32 (i) |
| any other long subclass | int64 (x) |
| any other float subclass | double (d) |
| any other str subclass | string (s) |
| any other unicode subclass | string (s) |
| any other tuple subclass | struct ((…)) |
| any other list subclass | array (a…), guess contents’ type according to type of first item |
| any other dict subclass | dict (a{…}), guess key, value type according to types for an arbitrary item |
| anything else | raise TypeError |

has_destination(*bus_name: str*) → bool  

has_interface(*interface: str or None*) → bool  

has_member(*name: str or None*) → bool  

has_path(*name: str or None*) → bool  

has_sender(*unique_name: str*) → bool  

has_signature(*signature: str*) → bool  

is_error(*error: str*) → bool  

is_method_call(*interface: str*, *member: str*) → bool  

is_signal(*interface: str*, *member: str*) → bool  

set_allow_interactive_authorization(*bool*) → None  
Set allow interactive authorization flag to this message.

set_auto_start(*bool*) → None  
Set whether this message will cause an owner for the destination name to be auto-started.

set_destination(*bus_name: str or None*)  

set_error_name(*name: str or None*)  

set_interface(*name: str or None*)  

set_member(*unique_name: str or None*)  

set_no_reply(*bool*) → None  
Set whether no reply to this message is required.

set_path(*name: str or None*)  

set_reply_serial(*bool*) → None  
Set the serial that this message is a reply to.

set_sender(*unique_name: str or None*)  

<!-- -->

*class *dbus.lowlevel.PendingCall  
Bases: `object`

Object representing a pending D-Bus call, returned by Connection.send_message_with_reply(). Cannot be instantiated directly.

block()  
Block until this pending call has completed and the associated reply handler has been called.

This can lead to a deadlock, if the called method tries to make a synchronous call to a method in this application.

cancel()  
Cancel this pending call. Its reply will be ignored and the associated reply handler will never be called.

get_completed() → bool  
Return true if this pending call has completed.

If so, its associated reply handler has been called and it is no longer meaningful to cancel it.

<!-- -->

*class *dbus.lowlevel.SignalMessage(*path: str*, *interface: str*, *method: str*)  
Bases: `dbus.lowlevel.Message`

A signal message.

append(*\*args*, *\*\*kwargs*)  
Set the message’s arguments from the positional parameter, according to the signature given by the `signature` keyword parameter.

The following type conversions are supported:

| D-Bus (in signature) | Python |
|----|----|
| boolean (b) | any object (via bool()) |
| byte (y) | string of length 1 any integer |
| any integer type | any integer |
| double (d) | any float |
| object path | anything with a \_\_dbus_object_path\_\_ attribute |
| string, signature, object path | str (must be UTF-8) or unicode |
| dict (a{…}) | any mapping |
| array (a…) | any iterable over appropriate objects |
| struct ((…)) | any iterable over appropriate objects |
| variant | any object above (guess type as below) |

Here ‘any integer’ means anything on which int() or long() (as appropriate) will work, except for basestring subclasses. ‘Any float’ means anything on which float() will work, except for basestring subclasses.

If there is no signature, guess from the arguments using the static method Message.guess_signature.

copy(*) -\> Message (or subclass*)  
Deep-copy the message, resetting the serial number to zero.

get_allow_interactive_authorization(*bool*) → None  
Get allow interactive authorization flag.

get_args_list(*\*\*kwargs*) → list  
Return the message’s arguments. Keyword arguments control the translation of D-Bus types to Python:

Keywords  
byte_arraysbool  
If true, convert arrays of byte (signature ‘ay’) into dbus.ByteArray, a str subclass. In practice, this is usually what you want, but it’s off by default for consistency.

If false (default), convert them into a dbus.Array of Bytes.

Most of the type mappings should be fairly obvious:

| D-Bus | Python |
|----|----|
| byte (y) | dbus.Byte (int subclass) |
| bool (b) | dbus.Boolean (int subclass) |
| Signature (g) | dbus.Signature (str subclass) |
| intNN, uintNN | dbus.IntNN, dbus.UIntNN (int or long subclasses) |
| double (d) | dbus.Double |
| string (s) | dbus.String (unicode subclass) (or dbus.UTF8String, bytes subclass, if utf8_strings set) |
| Object path (o) | dbus.ObjectPath (str subclass) |
| dict (a{…}) | dbus.Dictionary |
| array (a…) | dbus.Array (list subclass) containing appropriate types |
| byte array (ay) | dbus.ByteArray (str subclass) if byte_arrays set; or list of Byte |
| struct ((…)) | dbus.Struct (tuple subclass) of appropriate types |
| variant (v) | contained type, but with variant_level \> 0 |

get_auto_start() → bool  
Return true if this message will cause an owner for the destination name to be auto-started.

get_destination() → str or None  
Return the message’s destination bus name, or None if none.

get_error_name() → str or None  

get_interface() → str or None  

get_member() → str or None  

get_no_reply() → bool  
Return true if this message need not be replied to.

get_path() → ObjectPath or None  
Return the message’s destination object path (if it’s a method call) or source object path (if it’s a method reply or a signal) or None (if it has no path).

get_path_decomposed() → list of str, or None  
Return a list of path components (e.g. /foo/bar -\> \[‘foo’,’bar’\], / -\> \[\]) or None if the message has no associated path.

get_reply_serial() → long  
Returns the serial that the message is a reply to or 0 if none.

get_sender() → str or None  
Return the message’s sender unique name, or None if none.

get_serial() → long  
Returns the serial of a message or 0 if none has been specified.

The message’s serial number is provided by the application sending the message and is used to identify replies to this message. All messages received on a connection will have a serial, but messages you haven’t sent yet may return 0.

get_signature() → Signature or None  

get_type() → int  
Returns the type of the message.

*static *guess_signature(*\*args*) → Signature \[static method\]  
Guess a D-Bus signature which should be used to encode the given Python objects.

The signature is constructed as follows:

| Python | D-Bus |
|----|----|
| D-Bus type, variant_level \> 0 | variant (v) |
| D-Bus type, variant_level == 0 | the corresponding type |
| anything with a \_\_dbus_object_path\_\_ attribute | object path |
| bool | boolean (y) |
| any other int subclass | int32 (i) |
| any other long subclass | int64 (x) |
| any other float subclass | double (d) |
| any other str subclass | string (s) |
| any other unicode subclass | string (s) |
| any other tuple subclass | struct ((…)) |
| any other list subclass | array (a…), guess contents’ type according to type of first item |
| any other dict subclass | dict (a{…}), guess key, value type according to types for an arbitrary item |
| anything else | raise TypeError |

has_destination(*bus_name: str*) → bool  

has_interface(*interface: str or None*) → bool  

has_member(*name: str or None*) → bool  

has_path(*name: str or None*) → bool  

has_sender(*unique_name: str*) → bool  

has_signature(*signature: str*) → bool  

is_error(*error: str*) → bool  

is_method_call(*interface: str*, *member: str*) → bool  

is_signal(*interface: str*, *member: str*) → bool  

set_allow_interactive_authorization(*bool*) → None  
Set allow interactive authorization flag to this message.

set_auto_start(*bool*) → None  
Set whether this message will cause an owner for the destination name to be auto-started.

set_destination(*bus_name: str or None*)  

set_error_name(*name: str or None*)  

set_interface(*name: str or None*)  

set_member(*unique_name: str or None*)  

set_no_reply(*bool*) → None  
Set whether no reply to this message is required.

set_path(*name: str or None*)  

set_reply_serial(*bool*) → None  
Set the serial that this message is a reply to.

set_sender(*unique_name: str or None*)  
