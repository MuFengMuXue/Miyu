# dbus.glib module

Deprecated module which sets the default GLib main context as the mainloop implementation within D-Bus, as a side-effect of being imported!

This API is highly non-obvious, so instead of importing this module, new programs which don’t need pre-0.80 compatibility should use this equivalent code:

    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)
