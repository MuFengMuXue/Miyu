# dbus.mainloop package

## Module contents

Base definitions, etc. for main loop integration.

dbus.mainloop.NULL_MAIN_LOOP* = \<dbus.mainloop.NativeMainLoop object\>*  
A null mainloop which doesn’t actually do anything.

For advanced users who want to dispatch events by hand. This is almost certainly a bad idea - if in doubt, use the GLib main loop found in dbus.mainloop.glib.

<!-- -->

*class *dbus.mainloop.NativeMainLoop  
Bases: `object`

Object representing D-Bus main loop integration done in native code. Cannot be instantiated directly.

<!-- -->

dbus.mainloop.WATCH_ERROR* = 4*  
Represents an error condition on a file descriptor. Used to implement file descriptor watches.

<!-- -->

dbus.mainloop.WATCH_HANGUP* = 8*  
Represents a file descriptor reaching end-of-file. Used to implement file descriptor watches.

<!-- -->

dbus.mainloop.WATCH_READABLE* = 1*  
Represents a file descriptor becoming readable. Used to implement file descriptor watches.

<!-- -->

dbus.mainloop.WATCH_WRITABLE* = 2*  
Represents a file descriptor becoming readable. Used to implement file descriptor watches.

## dbus.mainloop.glib module

GLib main loop integration using libdbus-glib.

dbus.mainloop.glib.DBusGMainLoop(\[*set_as_default=False*\]) → NativeMainLoop  
Return a NativeMainLoop object which can be used to represent the default GLib main context in dbus-python.

If the keyword argument set_as_default is given and is true, set the new main loop as the default for all new Connection or Bus instances.

Non-default main contexts are not currently supported.

<!-- -->

dbus.mainloop.glib.threads_init()  
Initialize threads in dbus-glib, if this has not already been done.

This must be called before creating a second thread in a program that uses this module.
