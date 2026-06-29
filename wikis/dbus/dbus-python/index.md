# dbus-python: Python bindings for D-Bus

dbus-python is a Python binding for `dbus`, the reference implementation of the D-Bus protocol.

## Problems and alternatives

dbus-python might not be the best D-Bus binding for you to use. dbus-python does not follow the principle of “In the face of ambiguity, refuse the temptation to guess”, and can’t be changed to not do so without seriously breaking compatibility.

In addition, it uses libdbus (which has known problems with multi-threaded use) and attempts to be main-loop-agnostic (which means you have to select a suitable main loop for your application).

Alternative ways to get your Python code onto D-Bus include:

- GDBus, part of the GIO module of GLib, via GObject-Introspection and PyGI (uses the GLib main loop and object model)

- QtDBus, part of Qt, via PyQt (uses the Qt main loop and object model)

## Documentation

## Contributing to dbus-python

Please see the Gitlab project.

## Indices and tables

- Index

- Module Index

- Search Page
