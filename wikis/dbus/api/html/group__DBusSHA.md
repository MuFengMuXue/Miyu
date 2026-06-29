SHA implementation

D-Bus secret internal implementation details

SHA-1 hash. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gae7c1a8ad734655b70e67e9a1498465f7" class="memitem:gae7c1a8ad734655b70e67e9a1498465f7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_sha_init (DBusSHAContext *context)</td>
</tr>
<tr class="memdesc:gae7c1a8ad734655b70e67e9a1498465f7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes the SHA context.<br />
</td>
</tr>
<tr class="separator:gae7c1a8ad734655b70e67e9a1498465f7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae9c5e5cd39e2dc151ef1c54819aef3b6" class="memitem:gae9c5e5cd39e2dc151ef1c54819aef3b6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_sha_update (DBusSHAContext *context, const DBusString *data)</td>
</tr>
<tr class="memdesc:gae9c5e5cd39e2dc151ef1c54819aef3b6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Feeds more data into an existing shasum computation.<br />
</td>
</tr>
<tr class="separator:gae9c5e5cd39e2dc151ef1c54819aef3b6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf685311db11cc2e6b38fc62d171311e4" class="memitem:gaf685311db11cc2e6b38fc62d171311e4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_sha_final (DBusSHAContext *context, DBusString *results)</td>
</tr>
<tr class="memdesc:gaf685311db11cc2e6b38fc62d171311e4">
<td class="mdescLeft"> </td>
<td class="mdescRight">SHA finalization.<br />
</td>
</tr>
<tr class="separator:gaf685311db11cc2e6b38fc62d171311e4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4278fb9df967943834c4ad6332f2c28b" class="memitem:ga4278fb9df967943834c4ad6332f2c28b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_sha_compute (const DBusString *data, DBusString *ascii_output)</td>
</tr>
<tr class="memdesc:ga4278fb9df967943834c4ad6332f2c28b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Computes the ASCII hex-encoded shasum of the given data and appends it to the output string.<br />
</td>
</tr>
<tr class="separator:ga4278fb9df967943834c4ad6332f2c28b">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

SHA-1 hash.

Types and functions related to computing SHA-1 hash.

## Function Documentation

## ◆ \_dbus_sha_compute()

|                                |     |                      |                 |
|--------------------------------|-----|----------------------|-----------------|
| dbus_bool_t \_dbus_sha_compute | (   | const DBusString \*  | *data*,         |
|                                |     | DBusString \*        | *ascii_output*  |
|                                | )   |                      |                 |

Computes the ASCII hex-encoded shasum of the given data and appends it to the output string.

Parameters  
|              |                                  |
|--------------|----------------------------------|
| data         | input data to be hashed          |
| ascii_output | string to append ASCII shasum to |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 484 of file dbus-sha.c.

References \_dbus_sha_final(), \_dbus_sha_init(), \_dbus_sha_update(), \_dbus_string_free(), \_dbus_string_get_length(), \_dbus_string_hex_encode(), \_dbus_string_init(), FALSE, and TRUE.

## ◆ \_dbus_sha_final()

|                              |     |                    |            |
|------------------------------|-----|--------------------|------------|
| dbus_bool_t \_dbus_sha_final | (   | DBusSHAContext \*  | *context*, |
|                              |     | DBusString \*      | *results*  |
|                              | )   |                    |            |

SHA finalization.

Ends an SHA message-digest operation, writing the the message digest and zeroing the context. The results are returned as a raw 20-byte digest, not as the ascii-hex-digits string form of the digest.

Parameters  
|         |                                            |
|---------|--------------------------------------------|
| context | the SHA context                            |
| results | string to append the 20-byte SHA digest to |

<!-- -->

Returns  
FALSE if not enough memory to append the digest

Definition at line 457 of file dbus-sha.c.

References \_dbus_string_append_len(), \_DBUS_ZERO, FALSE, and TRUE.

Referenced by \_dbus_sha_compute().

## ◆ \_dbus_sha_init()

|                      |     |                    |           |     |     |
|----------------------|-----|--------------------|-----------|-----|-----|
| void \_dbus_sha_init | (   | DBusSHAContext \*  | *context* | )   |     |

Initializes the SHA context.

Parameters  
|         |                                                   |
|---------|---------------------------------------------------|
| context | an uninitialized context, typically on the stack. |

Definition at line 421 of file dbus-sha.c.

Referenced by \_dbus_sha_compute().

## ◆ \_dbus_sha_update()

|                        |     |                      |            |
|------------------------|-----|----------------------|------------|
| void \_dbus_sha_update | (   | DBusSHAContext \*    | *context*, |
|                        |     | const DBusString \*  | *data*     |
|                        | )   |                      |            |

Feeds more data into an existing shasum computation.

Parameters  
|         |                             |
|---------|-----------------------------|
| context | the SHA context             |
| data    | the additional data to hash |

Definition at line 433 of file dbus-sha.c.

References \_dbus_string_get_const_data(), and \_dbus_string_get_length().

Referenced by \_dbus_sha_compute().
