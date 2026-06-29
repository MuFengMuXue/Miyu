D-Bus

This manual documents the *low-level* D-Bus C API. **If you use this low-level API directly, you're signing up for some pain.**

Caveats aside, you might get started learning the low-level API by reading about DBusConnection and DBusMessage.

There are several other places to look for D-Bus information, such as the tutorial and the specification; those can be found at the D-Bus website. If you're interested in a sysadmin or package maintainer's perspective on the dbus-daemon itself and its configuration, be sure to check out the man pages as well.

The low-level API documented in this manual deliberately lacks most convenience functions - those are left up to higher-level libraries based on frameworks such as GLib, Qt, Python, Mono, Java, etc. These higher-level libraries (often called "D-Bus bindings") have features such as object systems and main loops that allow a *much* more convenient API.

The low-level API also contains plenty of clutter to support integration with arbitrary object systems, languages, main loops, and so forth. These features add a lot of noise to the API that you probably don't care about unless you're coding a binding.

This manual also contains docs for D-Bus internals, so you can use it to get oriented to the D-Bus source code if you're interested in patching the code. You should also read the file CONTRIBUTING.md which comes with the source code if you plan to contribute to D-Bus.

As you read the code, you can identify internal D-Bus functions because they start with an underscore ('\_') character. Also, any identifier or macro that lacks a DBus, dbus\_, or DBUS\_ namepace prefix is internal, with a couple of exceptions such as NULL, TRUE, and FALSE.
