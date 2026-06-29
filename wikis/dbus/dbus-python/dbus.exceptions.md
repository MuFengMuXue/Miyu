# dbus.exceptions module

D-Bus exceptions.

*exception *dbus.exceptions.DBusException(*\*args*, *\*\*kwargs*)  
Bases: `Exception`

args  

get_dbus_message()  

get_dbus_name()  

include_traceback* = False*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

with_traceback()  
Exception.with_traceback(tb) – set self.\_\_traceback\_\_ to tb and return self.

<!-- -->

*exception *dbus.exceptions.IntrospectionParserException(*msg=''*)  
Bases: `dbus.exceptions.DBusException`

args  

get_dbus_message()  

get_dbus_name()  

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

with_traceback()  
Exception.with_traceback(tb) – set self.\_\_traceback\_\_ to tb and return self.

<!-- -->

*exception *dbus.exceptions.MissingErrorHandlerException  
Bases: `dbus.exceptions.DBusException`

args  

get_dbus_message()  

get_dbus_name()  

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

with_traceback()  
Exception.with_traceback(tb) – set self.\_\_traceback\_\_ to tb and return self.

<!-- -->

*exception *dbus.exceptions.MissingReplyHandlerException  
Bases: `dbus.exceptions.DBusException`

args  

get_dbus_message()  

get_dbus_name()  

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

with_traceback()  
Exception.with_traceback(tb) – set self.\_\_traceback\_\_ to tb and return self.

<!-- -->

*exception *dbus.exceptions.NameExistsException(*name*)  
Bases: `dbus.exceptions.DBusException`

args  

get_dbus_message()  

get_dbus_name()  

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

with_traceback()  
Exception.with_traceback(tb) – set self.\_\_traceback\_\_ to tb and return self.

<!-- -->

*exception *dbus.exceptions.UnknownMethodException(*method*)  
Bases: `dbus.exceptions.DBusException`

args  

get_dbus_message()  

get_dbus_name()  

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

with_traceback()  
Exception.with_traceback(tb) – set self.\_\_traceback\_\_ to tb and return self.

<!-- -->

*exception *dbus.exceptions.ValidationException(*msg=''*)  
Bases: `dbus.exceptions.DBusException`

args  

get_dbus_message()  

get_dbus_name()  

include_traceback* = True*  
If True, tracebacks will be included in the exception message sent to D-Bus clients.

Exceptions that are not DBusException subclasses always behave as though this is True. Set this to True on DBusException subclasses that represent a programming error, and leave it False on subclasses that represent an expected failure condition (e.g. a network server not responding).

with_traceback()  
Exception.with_traceback(tb) – set self.\_\_traceback\_\_ to tb and return self.
