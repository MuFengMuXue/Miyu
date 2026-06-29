|                      |     |     |     |     |
|:---------------------|-----|-----|-----|-----|
| Top  \|  Description |     |     |     |     |

<table width="100%">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-valign="top"><h2 id="dbusgproxy">DBusGProxy</h2>
<p>DBusGProxy — DBus Proxy</p></td>
<td class="gallery_image" style="text-align: right;" data-valign="top"></td>
</tr>
</tbody>
</table>

## Stability Level

Stable, unless otherwise indicated

## Functions

|                   |                                         |
|-------------------|-----------------------------------------|
| void              | (\*DBusGProxyCallNotify) ()             |
| DBusGProxy \*     | dbus_g_proxy_new_for_name ()            |
| DBusGProxy \*     | dbus_g_proxy_new_for_name_owner ()      |
| DBusGProxy \*     | dbus_g_proxy_new_from_proxy ()          |
| DBusGProxy \*     | dbus_g_proxy_new_for_peer ()            |
| void              | dbus_g_proxy_set_interface ()           |
| const char \*     | dbus_g_proxy_get_path ()                |
| const char \*     | dbus_g_proxy_get_bus_name ()            |
| const char \*     | dbus_g_proxy_get_interface ()           |
| void              | dbus_g_proxy_add_signal ()              |
| void              | dbus_g_proxy_connect_signal ()          |
| void              | dbus_g_proxy_disconnect_signal ()       |
| void              | dbus_g_proxy_send ()                    |
| gboolean          | dbus_g_proxy_call ()                    |
| gboolean          | dbus_g_proxy_call_with_timeout ()       |
| void              | dbus_g_proxy_call_no_reply ()           |
| DBusGProxyCall \* | dbus_g_proxy_begin_call ()              |
| DBusGProxyCall \* | dbus_g_proxy_begin_call_with_timeout () |
| gboolean          | dbus_g_proxy_end_call ()                |
| void              | dbus_g_proxy_cancel_call ()             |
| void              | dbus_g_proxy_set_default_timeout ()     |

## Types and Values

|        |                |
|--------|----------------|
| struct | DBusGProxy     |
|        | DBusGProxyCall |

## Includes

``` synopsis
#include <dbus/dbus-glib.h>
```

## Description

A DBusGProxy is a GObject representing a remote object in a D-Bus service.

## Functions

### DBusGProxyCallNotify ()

``` programlisting
void
(*DBusGProxyCallNotify) (DBusGProxy *proxy,
                         DBusGProxyCall *call_id,
                         void *user_data);
```

`DBusGProxyCallNotify` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is the standard GAsyncReadyCallback mechanism.

Called when a reply to the call represented by *`call_id`* arrives. Use `dbus_g_proxy_end_call()` to see whether *`call_id`* succeeded or failed, and get the arguments returned (if any) on success.

#### Parameters

|           |                                                       |     |
|-----------|-------------------------------------------------------|-----|
| proxy     | the proxy on which the method was called              |     |
| call_id   | the call in progress                                  |     |
| user_data | data passed to `dbus_g_proxy_begin_call()` or similar |     |

### dbus_g_proxy_new_for_name ()

``` programlisting
DBusGProxy *
dbus_g_proxy_new_for_name (DBusGConnection *connection,
                           const char *name,
                           const char *path,
                           const char *iface);
```

`dbus_g_proxy_new_for_name` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_new_sync()`.

Creates a new proxy for a remote interface exported by a connection on a message bus. Method calls and signal connections over this proxy will go to the name owner; the name's owner is expected to support the given interface name. THE NAME OWNER MAY CHANGE OVER TIME, for example between two different method calls, unless the name is a unique name. If you need a fixed owner, you need to request the current owner and bind a proxy to its unique name rather than to the generic name; see `dbus_g_proxy_new_for_name_owner()`.

A name-associated proxy only makes sense with a message bus, not for app-to-app direct dbus connections.

This proxy will only emit the "destroy" signal if the DBusConnection is disconnected, the proxy has no remaining references, or the name is a unique name and its owner disappears. If a well-known name changes owner, the proxy will still be alive.

#### Parameters

|            |                                                |     |
|------------|------------------------------------------------|-----|
| connection | the connection to the remote bus               |     |
| name       | any name on the message bus                    |     |
| path       | name of the object instance to call methods on |     |
| iface      | name of the interface to call methods on       |     |

#### Returns

new proxy object

### dbus_g_proxy_new_for_name_owner ()

``` programlisting
DBusGProxy *
dbus_g_proxy_new_for_name_owner (DBusGConnection *connection,
                                 const char *name,
                                 const char *path,
                                 const char *iface,
                                 GError **error);
```

`dbus_g_proxy_new_for_name_owner` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_new_sync()` with the name owner's unique name passed as *`name`* .

Similar to `dbus_g_proxy_new_for_name()`, but makes a round-trip request to the message bus to get the current name owner, then binds the proxy to the unique name of the current owner, rather than to the well-known name. As a result, the name owner will not change over time, and the proxy will emit the "destroy" signal when the owner disappears from the message bus.

An example of the difference between `dbus_g_proxy_new_for_name()` and `dbus_g_proxy_new_for_name_owner()`: if you provide the well-known name "org.freedesktop.Database" `dbus_g_proxy_new_for_name()` remains bound to that name as it changes owner. `dbus_g_proxy_new_for_name_owner()` will fail if the name has no owner. If the name has an owner, `dbus_g_proxy_new_for_name_owner()` will bind to the unique name of that owner rather than the generic name.

#### Parameters

|            |                                                          |     |
|------------|----------------------------------------------------------|-----|
| connection | the connection to the remote bus                         |     |
| name       | any name on the message bus                              |     |
| path       | name of the object inside the service to call methods on |     |
| iface      | name of the interface to call methods on                 |     |
| error      | return location for an error                             |     |

#### Returns

new proxy object, or `NULL` on error

### dbus_g_proxy_new_from_proxy ()

``` programlisting
DBusGProxy *
dbus_g_proxy_new_from_proxy (DBusGProxy *proxy,
                             const char *iface,
                             const char *path);
```

`dbus_g_proxy_new_from_proxy` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_new_sync()`.

Creates a proxy using an existing proxy as a template, substituting the specified interface and path. Either or both may be NULL.

#### Parameters

|       |                                                  |     |
|-------|--------------------------------------------------|-----|
| proxy | the proxy to use as a template                   |     |
| iface | name of the interface to call methods on         |     |
| path  | of the object inside the peer to call methods on |     |

#### Returns

new proxy object

### dbus_g_proxy_new_for_peer ()

``` programlisting
DBusGProxy *
dbus_g_proxy_new_for_peer (DBusGConnection *connection,
                           const char *path,
                           const char *iface);
```

`dbus_g_proxy_new_for_peer` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_new_sync()`.

Creates a proxy for an object in peer application (one we're directly connected to). That is, this function is intended for use when there's no message bus involved, we're doing a simple 1-to-1 communication between two applications.

#### Parameters

|            |                                                       |     |
|------------|-------------------------------------------------------|-----|
| connection | the connection to the peer                            |     |
| path       | name of the object inside the peer to call methods on |     |
| iface      | name of the interface to call methods on              |     |

#### Returns

new proxy object

### dbus_g_proxy_set_interface ()

``` programlisting
void
dbus_g_proxy_set_interface (DBusGProxy *proxy,
                            const char *interface_name);
```

`dbus_g_proxy_set_interface` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. There is no direct equivalent for this function: construct a new proxy instead.

Sets the object interface proxy is bound to

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|                |                     |     |
|----------------|---------------------|-----|
| proxy          | the proxy           |     |
| interface_name | an object interface |     |

### dbus_g_proxy_get_path ()

``` programlisting
const char *
dbus_g_proxy_get_path (DBusGProxy *proxy);
```

`dbus_g_proxy_get_path` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_get_object_path()`.

Gets the path this proxy is bound to

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|       |           |     |
|-------|-----------|-----|
| proxy | the proxy |     |

#### Returns

an object path

### dbus_g_proxy_get_bus_name ()

``` programlisting
const char *
dbus_g_proxy_get_bus_name (DBusGProxy *proxy);
```

`dbus_g_proxy_get_bus_name` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_get_name()` or `g_dbus_proxy_get_name_owner()`, depending how the proxy was created.

Gets the bus name a proxy is bound to (may be `NULL` in some cases). If you created the proxy with `dbus_g_proxy_new_for_name()`, then the name you passed to that will be returned. If you created it with `dbus_g_proxy_new_for_name_owner()`, then the unique connection name will be returned. If you created it with `dbus_g_proxy_new_for_peer()` then `NULL` will be returned.

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|       |           |     |
|-------|-----------|-----|
| proxy | the proxy |     |

#### Returns

the bus name the proxy sends messages to

### dbus_g_proxy_get_interface ()

``` programlisting
const char *
dbus_g_proxy_get_interface (DBusGProxy *proxy);
```

`dbus_g_proxy_get_interface` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_get_interface_name()`.

Gets the object interface proxy is bound to (may be `NULL` in some cases).

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|       |           |     |
|-------|-----------|-----|
| proxy | the proxy |     |

#### Returns

an object interface

### dbus_g_proxy_add_signal ()

``` programlisting
void
dbus_g_proxy_add_signal (DBusGProxy *proxy,
                         const char *signal_name,
                         GType first_type,
                         ...);
```

`dbus_g_proxy_add_signal` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Specifies the argument signature of a D-Bus signal. When the signal is emitted by the remote object, if the GTypes corresponding to its arguments' types do not match the types given here, the signal will be ignored.

It is an error to add the same *`signal_name`* to the same *`proxy`* more than once, even if the argument types given are the same.

It is also an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|  |  |  |
|----|----|----|
| proxy | the proxy for a remote interface |   |
| signal_name | the name of the signal |   |
| first_type | the first argument type, or `G_TYPE_INVALID` if none |   |
| ... | any subsequent argument types, followed by `G_TYPE_INVALID` |   |

### dbus_g_proxy_connect_signal ()

``` programlisting
void
dbus_g_proxy_connect_signal (DBusGProxy *proxy,
                             const char *signal_name,
                             GCallback handler,
                             void *data,
                             GClosureNotify free_data_func);
```

`dbus_g_proxy_connect_signal` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_connection_signal_subscribe()`.

Connect a signal handler to a proxy for a remote interface. When the remote interface emits the specified signal, the proxy will emit a corresponding GLib signal.

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|                |                                    |     |
|----------------|------------------------------------|-----|
| proxy          | a proxy for a remote interface     |     |
| signal_name    | the DBus signal name to listen for |     |
| handler        | the handler to connect             |     |
| data           | data to pass to handler            |     |
| free_data_func | callback function to destroy data  |     |

### dbus_g_proxy_disconnect_signal ()

``` programlisting
void
dbus_g_proxy_disconnect_signal (DBusGProxy *proxy,
                                const char *signal_name,
                                GCallback handler,
                                void *data);
```

`dbus_g_proxy_disconnect_signal` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_connection_signal_unsubscribe()`.

Disconnect all signal handlers from a proxy that match the given criteria.

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|             |                                           |     |
|-------------|-------------------------------------------|-----|
| proxy       | a proxy for a remote interface            |     |
| signal_name | the DBus signal name to disconnect        |     |
| handler     | the handler to disconnect                 |     |
| data        | the data that was registered with handler |     |

### dbus_g_proxy_send ()

``` programlisting
void
dbus_g_proxy_send (DBusGProxy *proxy,
                   DBusMessage *message,
                   dbus_uint32_t *client_serial);
```

`dbus_g_proxy_send` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_connection_send_message()`.

Sends a message to the interface we're proxying for. Does not block or wait for a reply. The message is only actually written out when you return to the main loop or block in `dbus_g_connection_flush()`.

The message is modified to be addressed to the target interface. That is, a destination name field or whatever is needed will be added to the message. The basic point of this function is to add the necessary header fields, otherwise it's equivalent to `dbus_connection_send()`.

This function adds a reference to the message, so the caller still owns its original reference.

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|               |                                                 |     |
|---------------|-------------------------------------------------|-----|
| proxy         | a proxy for a remote interface                  |     |
| message       | the message to address and send                 |     |
| client_serial | return location for message's serial, or `NULL` |     |

### dbus_g_proxy_call ()

``` programlisting
gboolean
dbus_g_proxy_call (DBusGProxy *proxy,
                   const char *method,
                   GError **error,
                   GType first_arg_type,
                   ...);
```

`dbus_g_proxy_call` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_call_sync()`.

Function for synchronously invoking a method and receiving reply values. This function is equivalent to dbus_g_proxy_begin_call followed by dbus_g_proxy_end_call. All of the input arguments are specified first, followed by G_TYPE_INVALID, followed by all of the output values, followed by a second G_TYPE_INVALID. Note that this means you must always specify G_TYPE_INVALID twice.

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|  |  |  |
|----|----|----|
| proxy | a proxy for a remote interface |   |
| method | method to invoke |   |
| error | return location for an error |   |
| first_arg_type | type of first "in" argument, or `G_TYPE_INVALID` if none |   |
| ... | value of first "in" argument, any further type/value pairs, `G_TYPE_INVALID`, type/location pairs for "out" arguments, and `G_TYPE_INVALID` again |   |

#### Returns

`TRUE` if the method succeeds, `FALSE` if it fails

### dbus_g_proxy_call_with_timeout ()

``` programlisting
gboolean
dbus_g_proxy_call_with_timeout (DBusGProxy *proxy,
                                const char *method,
                                int timeout,
                                GError **error,
                                GType first_arg_type,
                                ...);
```

`dbus_g_proxy_call_with_timeout` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_call_sync()`.

Function for synchronously invoking a method and receiving reply values. This function is equivalent to dbus_g_proxy_begin_call followed by dbus_g_proxy_end_call. All of the input arguments are specified first, followed by G_TYPE_INVALID, followed by all of the output values, followed by a second G_TYPE_INVALID. Note that this means you must always specify G_TYPE_INVALID twice.

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|                |                                                     |     |
|----------------|-----------------------------------------------------|-----|
| proxy          | a proxy for a remote interface                      |     |
| method         | method to invoke                                    |     |
| timeout        | the timeout in milliseconds, or -1 to use a default |     |
| error          | return location for an error                        |     |
| first_arg_type | type of first "in" argument                         |     |
| ...            | as for `dbus_g_proxy_call()`                        |     |

#### Returns

`TRUE` if the method succeeds, `FALSE` if it fails

### dbus_g_proxy_call_no_reply ()

``` programlisting
void
dbus_g_proxy_call_no_reply (DBusGProxy *proxy,
                            const char *method,
                            GType first_arg_type,
                            ...);
```

`dbus_g_proxy_call_no_reply` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_call()` with *`callback`* = `NULL`.

Sends a method call message as with `dbus_g_proxy_begin_call()`, but does not ask for a reply or allow you to receive one.

It is an error to call this method on a proxy that has emitted the “destroy” signal.

TODO: this particular function shouldn't die on out of memory, since you should be able to do a call with large arguments.

#### Parameters

|  |  |  |
|----|----|----|
| proxy | a proxy for a remote interface |   |
| method | the name of the method to invoke |   |
| first_arg_type | type of the first argument, or `G_TYPE_INVALID` to call the method without arguments |   |
| ... | the first argument and any remaining type/argument pairs, followed by `G_TYPE_INVALID` to terminate the list |   |

### dbus_g_proxy_begin_call ()

``` programlisting
DBusGProxyCall *
dbus_g_proxy_begin_call (DBusGProxy *proxy,
                         const char *method,
                         DBusGProxyCallNotify notify,
                         gpointer user_data,
                         GDestroyNotify destroy,
                         GType first_arg_type,
                         ...);
```

`dbus_g_proxy_begin_call` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_call()`.

Asynchronously invokes a method on a remote interface. The method call will not be sent over the wire until the application returns to the main loop, or blocks in `dbus_g_connection_flush()` to write out pending data. The call will be completed after a timeout, or when a reply is received. When the call returns, the callback specified will be invoked; you can then collect the results of the call (which may be an error, or a reply), use `dbus_g_proxy_end_call()`.

It is an error to call this method on a proxy that has emitted the “destroy” signal.

TODO this particular function shouldn't die on out of memory, since you should be able to do a call with large arguments.

#### Parameters

|  |  |  |
|----|----|----|
| proxy | a proxy for a remote interface |   |
| method | the name of the method to invoke |   |
| notify | callback to be invoked when method returns |   |
| user_data | user data passed to callback |   |
| destroy | function called to destroy user_data |   |
| first_arg_type | type of the first argument, or `G_TYPE_INVALID` if there are no arguments |   |
| ... | first argument, followed by any further type/value pairs, followed by `G_TYPE_INVALID` |   |

#### Returns

call identifier.

### dbus_g_proxy_begin_call_with_timeout ()

``` programlisting
DBusGProxyCall *
dbus_g_proxy_begin_call_with_timeout (DBusGProxy *proxy,
                                      const char *method,
                                      DBusGProxyCallNotify notify,
                                      gpointer user_data,
                                      GDestroyNotify destroy,
                                      int timeout,
                                      GType first_arg_type,
                                      ...);
```

`dbus_g_proxy_begin_call_with_timeout` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_call()`.

Asynchronously invokes a method on a remote interface. The method call will not be sent over the wire until the application returns to the main loop, or blocks in `dbus_g_connection_flush()` to write out pending data. The call will be completed after a timeout, or when a reply is received. When the call returns, the callback specified will be invoked; you can then collect the results of the call (which may be an error, or a reply), use `dbus_g_proxy_end_call()`.

It is an error to call this method on a proxy that has emitted the “destroy” signal.

TODO this particular function shouldn't die on out of memory, since you should be able to do a call with large arguments.

#### Parameters

|  |  |  |
|----|----|----|
| proxy | a proxy for a remote interface |   |
| method | the name of the method to invoke |   |
| notify | callback to be invoked when method returns |   |
| user_data | user data passed to callback |   |
| destroy | function called to destroy user_data |   |
| timeout | the timeout in milliseconds, or -1 to use a default |   |
| first_arg_type | type of the first argument, or `G_TYPE_INVALID` if there are no arguments |   |
| ... | first argument, followed by any further type/value pairs, followed by `G_TYPE_INVALID` |   |

#### Returns

call identifier.

### dbus_g_proxy_end_call ()

``` programlisting
gboolean
dbus_g_proxy_end_call (DBusGProxy *proxy,
                       DBusGProxyCall *call,
                       GError **error,
                       GType first_arg_type,
                       ...);
```

`dbus_g_proxy_end_call` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_proxy_call_finish()`.

Collects the results of a method call. The method call was normally initiated with `dbus_g_proxy_end_call()`. You may use this function outside of the callback given to dbus_g_proxy_begin_call; in that case this function will block if the results haven't yet been received.

All D-Bus method calls can fail with a remote error. If this occurs, the *`error`* will be set and this function will return `FALSE`.

Otherwise, the "out" parameters and return value of the method are stored in the provided varargs list. The list should be terminated with G_TYPE_INVALID.

#### Parameters

|  |  |  |
|----|----|----|
| proxy | a proxy for a remote interface |   |
| call | the pending call ID from `dbus_g_proxy_begin_call()` |   |
| error | return location for an error |   |
| first_arg_type | type of first "out" argument, or `G_TYPE_INVALID` if there are no "out" arguments |   |
| ... | return location for first "out" argument, followed by any further type/location pairs, followed by `G_TYPE_INVALID` |   |

#### Returns

`TRUE` on success

### dbus_g_proxy_cancel_call ()

``` programlisting
void
dbus_g_proxy_cancel_call (DBusGProxy *proxy,
                          DBusGProxyCall *call);
```

`dbus_g_proxy_cancel_call` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_cancellable_cancel()`.

Cancels a pending method call. The method call was normally initiated with `dbus_g_proxy_begin_call()`. This function may not be used on pending calls that have already been ended with dbus_g_proxy_end_call.

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|       |                                                      |     |
|-------|------------------------------------------------------|-----|
| proxy | a proxy for a remote interface                       |     |
| call  | the pending call ID from `dbus_g_proxy_begin_call()` |     |

### dbus_g_proxy_set_default_timeout ()

``` programlisting
void
dbus_g_proxy_set_default_timeout (DBusGProxy *proxy,
                                  int timeout);
```

`dbus_g_proxy_set_default_timeout` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Sets the default timeout to use for a proxy. This timeout will be used in calls where the timeout is not specified, or is specified to be -1. If this timeout is also set to -1, libdbus will use a reasonable default value.

This is useful for long-running operations that takes longer than the default timeout (which is a on the order of magnitude of tens of seconds). For some applications, consider using a pattern where the method returns once the operation is underway (e.g. immediately) and emits a signal when the operation terminates (though beware of leaking information with/in the signal return value).

It is an error to call this method on a proxy that has emitted the “destroy” signal.

#### Parameters

|  |  |  |
|----|----|----|
| proxy | a proxy for a remote interface |   |
| timeout | the timeout in milliseconds, or -1 to reset to the libdbus default |   |

Since 0.75

## Types and Values

### struct DBusGProxy

``` programlisting
struct DBusGProxy {
};
```

`DBusGProxy` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is GDBusProxy.

A GObject representing a remote object in a D-Bus service.

### DBusGProxyCall

``` programlisting
typedef struct _DBusGProxyCall DBusGProxyCall;
```

`DBusGProxyCall` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. There is no direct equivalent in GDBus, but the standard GCancellable mechanism is analogous.

An opaque pointer representing an asynchronous call in progress.

## See Also

DBusGProxy
