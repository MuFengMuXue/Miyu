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
<td data-valign="top"><h2 id="dbusgmessage">DBusGMessage</h2>
<p>DBusGMessage — DBus Message</p></td>
<td class="gallery_image" style="text-align: right;" data-valign="top"></td>
</tr>
</tbody>
</table>

## Stability Level

Stable, unless otherwise indicated

## Functions

|                 |                               |
|-----------------|-------------------------------|
| \#define        | DBUS_TYPE_G_MESSAGE           |
| DBusGMessage \* | dbus_g_message_ref ()         |
| void            | dbus_g_message_unref ()       |
| DBusMessage \*  | dbus_g_message_get_message () |

## Types and Values

|     |              |
|-----|--------------|
|     | DBusGMessage |

## Includes

``` synopsis
#include <dbus/dbus-glib.h>
```

## Description

A DBusGMessage is a boxed type abstracting a DBusMessage.

## Functions

### DBUS_TYPE_G_MESSAGE

``` programlisting
#define DBUS_TYPE_G_MESSAGE      (dbus_g_message_get_g_type ())
```

`DBUS_TYPE_G_MESSAGE` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Expands to a function call returning the boxed GType of a DBusGConnection.

#### Returns

the GLib type

### dbus_g_message_ref ()

``` programlisting
DBusGMessage *
dbus_g_message_ref (DBusGMessage *message);
```

`dbus_g_message_ref` is deprecated and should not be used in newly-written code.

New code should use GDBusMessage instead.

Increment refcount on a DBusGMessage

#### Parameters

|         |                    |     |
|---------|--------------------|-----|
| message | the message to ref |     |

#### Returns

the message that was ref'd

### dbus_g_message_unref ()

``` programlisting
void
dbus_g_message_unref (DBusGMessage *message);
```

`dbus_g_message_unref` is deprecated and should not be used in newly-written code.

New code should use GDBusMessage instead.

Decrement refcount on a DBusGMessage

#### Parameters

|         |                      |     |
|---------|----------------------|-----|
| message | the message to unref |     |

### dbus_g_message_get_message ()

``` programlisting
DBusMessage *
dbus_g_message_get_message (DBusGMessage *gmessage);
```

`dbus_g_message_get_message` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Get the DBusMessage corresponding to this DBusGMessage. The return value does not have its refcount incremented.

#### Parameters

|          |                |     |
|----------|----------------|-----|
| gmessage | a DBusGMessage |     |

#### Returns

DBusMessage

## Types and Values

### DBusGMessage

``` programlisting
typedef struct _DBusGMessage DBusGMessage;
```

`DBusGMessage` is deprecated and should not be used in newly-written code.

New code should use GDBusMessage instead.

A DBusGMessage is a boxed type abstracting a DBusMessage from libdbus.

## See Also

DBusMessage
