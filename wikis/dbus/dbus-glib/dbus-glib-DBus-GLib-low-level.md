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
<td data-valign="top"><h2 id="dbus-glib-low-level">DBus GLib low level</h2>
<p>DBus GLib low level — DBus lower level functions</p></td>
<td class="gallery_image" style="text-align: right;" data-valign="top"></td>
</tr>
</tbody>
</table>

## Stability Level

Unstable, unless otherwise indicated

## Functions

|                    |                                      |
|--------------------|--------------------------------------|
| void               | dbus_set_g_error ()                  |
| void               | dbus_connection_setup_with_g_main () |
| DBusGConnection \* | dbus_connection_get_g_connection ()  |
| void               | dbus_server_setup_with_g_main ()     |
| \#define           | DBUS_TYPE_CONNECTION                 |
| \#define           | DBUS_TYPE_MESSAGE                    |

## Includes

``` synopsis
#include <dbus/dbus-glib-lowlevel.h>
```

## Description

These functions can be used to access lower level of DBus.

## Functions

### dbus_set_g_error ()

``` programlisting
void
dbus_set_g_error (GError **gerror,
                  DBusError *derror);
```

`dbus_set_g_error` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. GDBus' error encoding is much simpler and more reliable, and the closest equivalent is `g_dbus_error_new_for_dbus_error()`.

Store the information from a DBus method error return into a GError. For the normal case of an arbitrary remote process, the error code will be DBUS_GERROR_REMOTE_EXCEPTION. Now, DBus errors have two components; a message and a "name". The former is an arbitrary (normally American English) string. The second is a string like com.example.FooFailure which programs can use as a conditional source. Because a GError only has one string, we use a hack to encode both values:

\<human readable string\>\<null\>\<error name\>\<null\>

You can use the following code to retrieve both values:

<table class="listing_frame" data-border="0" data-cellpadding="0" data-cellspacing="0">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="listing_lines" style="text-align: right;"><pre><code>1
2</code></pre></td>
<td class="listing_code"><pre class="programlisting"><code>size_t len = strlen(msg);
const char *error_name = msg+len+1;]|</code></pre></td>
</tr>
</tbody>
</table>

#### Parameters

|        |             |     |
|--------|-------------|-----|
| gerror | an error    |     |
| derror | a DBusError |     |

### dbus_connection_setup_with_g_main ()

``` programlisting
void
dbus_connection_setup_with_g_main (DBusConnection *connection,
                                   GMainContext *context);
```

`dbus_connection_setup_with_g_main` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Sets the watch and timeout functions of a DBusConnection to integrate the connection with the GLib main loop. Pass in `NULL` for the GMainContext unless you're doing something specialized.

If called twice for the same context, does nothing the second time. If called once with context A and once with context B, context B replaces context A as the context monitoring the connection.

#### Parameters

|            |                                                |     |
|------------|------------------------------------------------|-----|
| connection | the connection                                 |     |
| context    | the GMainContext or `NULL` for default context |     |

### dbus_connection_get_g_connection ()

``` programlisting
DBusGConnection *
dbus_connection_get_g_connection (DBusConnection *connection);
```

`dbus_connection_get_g_connection` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Get the DBusGConnection corresponding to this DBusConnection. This only makes sense if the DBusConnection was originally a DBusGConnection that was registered with the GLib main loop. The return value does not have its refcount incremented.

#### Parameters

|            |                  |     |
|------------|------------------|-----|
| connection | a DBusConnection |     |

#### Returns

DBusGConnection

### dbus_server_setup_with_g_main ()

``` programlisting
void
dbus_server_setup_with_g_main (DBusServer *server,
                               GMainContext *context);
```

`dbus_server_setup_with_g_main` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Sets the watch and timeout functions of a DBusServer to integrate the server with the GLib main loop. In most cases the context argument should be `NULL`.

If called twice for the same context, does nothing the second time. If called once with context A and once with context B, context B replaces context A as the context monitoring the connection.

#### Parameters

|         |                                        |     |
|---------|----------------------------------------|-----|
| server  | the server                             |     |
| context | the GMainContext or `NULL` for default |     |

### DBUS_TYPE_CONNECTION

``` programlisting
#define DBUS_TYPE_CONNECTION      (dbus_connection_get_g_type ())
```

`DBUS_TYPE_CONNECTION` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Expands to a function call returning a boxed GType representing a DBusConnection pointer from libdbus. Not to be confused with `DBUS_TYPE_G_CONNECTION`, which you should usually use instead.

#### Returns

the GLib type

### DBUS_TYPE_MESSAGE

``` programlisting
#define DBUS_TYPE_MESSAGE         (dbus_message_get_g_type ())
```

`DBUS_TYPE_MESSAGE` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Expands to a function call returning a boxed GType representing a DBusMessage pointer from libdbus. Not to be confused with `DBUS_TYPE_G_MESSAGE`, which you should usually use instead.

#### Returns

the GLib type

## Types and Values
