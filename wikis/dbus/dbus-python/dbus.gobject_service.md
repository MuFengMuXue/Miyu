# dbus.gobject_service module

This module is only available when using Python 2, and is deprecated.

*class *gobject_service.ExportedGObjectType(*cls*, *name*, *bases*, *dct*)  
A metaclass which inherits from both GObjectMeta and dbus.service.InterfaceType. Used as the metaclass for ExportedGObject.

<!-- -->

*class *gobject_service.ExportedGObject(*self*, *conn=None*, *object_path=None*, *\*\*kwargs*)  
A GObject which is exported on the D-Bus.

Because GObject and dbus.service.Object both have custom metaclasses, the naive approach using simple multiple inheritance won’t work. This class has ExportedGObjectType as its metaclass, which is sufficient to make it work correctly.

Parameters  
- **conn** (*dbus.connection.Connection*) – The D-Bus connection or bus

- **object_path** (*str*) – The object path at which to register this object.

- **bus_name** (*dbus.service.BusName*) – A bus name to be held on behalf of this object, or None.

- **gobject_properties** (*dict*) –

  GObject properties to be set on the constructed object.

  Any unrecognised keyword arguments will also be interpreted as GObject properties.
