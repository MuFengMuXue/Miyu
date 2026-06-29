DBusMessageFilter Struct Reference

D-Bus secret internal implementation details » DBusConnection implementation details

Internal struct representing a message filter function. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a2d2debd9a708cb7d4f8447c18f7458b9" class="memitem:a2d2debd9a708cb7d4f8447c18f7458b9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAtomic </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a2d2debd9a708cb7d4f8447c18f7458b9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:a2d2debd9a708cb7d4f8447c18f7458b9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a56b3643122277ed5dc3d4f07793617fa" class="memitem:a56b3643122277ed5dc3d4f07793617fa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHandleMessageFunction </td>
<td class="memItemRight" data-valign="bottom">function</td>
</tr>
<tr class="memdesc:a56b3643122277ed5dc3d4f07793617fa">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to call to filter.<br />
</td>
</tr>
<tr class="separator:a56b3643122277ed5dc3d4f07793617fa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a6cf5321325828e39da1cc8fa1b3d7153" class="memitem:a6cf5321325828e39da1cc8fa1b3d7153">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">user_data</td>
</tr>
<tr class="memdesc:a6cf5321325828e39da1cc8fa1b3d7153">
<td class="mdescLeft"> </td>
<td class="mdescRight">User data for the function.<br />
</td>
</tr>
<tr class="separator:a6cf5321325828e39da1cc8fa1b3d7153">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a915f3269a91ee41d963448dcb22d92cd" class="memitem:a915f3269a91ee41d963448dcb22d92cd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_user_data_function</td>
</tr>
<tr class="memdesc:a915f3269a91ee41d963448dcb22d92cd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to free the user data.<br />
</td>
</tr>
<tr class="separator:a915f3269a91ee41d963448dcb22d92cd">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internal struct representing a message filter function.

Definition at line 230 of file dbus-connection.c.

## Field Documentation

## ◆ free_user_data_function

|                                                             |
|-------------------------------------------------------------|
| DBusFreeFunction DBusMessageFilter::free_user_data_function |

Function to free the user data.

Definition at line 235 of file dbus-connection.c.

Referenced by dbus_connection_add_filter(), and dbus_connection_remove_filter().

## ◆ function

|                                                       |
|-------------------------------------------------------|
| DBusHandleMessageFunction DBusMessageFilter::function |

Function to call to filter.

Definition at line 233 of file dbus-connection.c.

Referenced by dbus_connection_add_filter(), dbus_connection_dispatch(), and dbus_connection_remove_filter().

## ◆ refcount

|                                        |
|----------------------------------------|
| DBusAtomic DBusMessageFilter::refcount |

Reference count.

Definition at line 232 of file dbus-connection.c.

Referenced by dbus_connection_add_filter().

## ◆ user_data

|                                     |
|-------------------------------------|
| void\* DBusMessageFilter::user_data |

User data for the function.

Definition at line 234 of file dbus-connection.c.

Referenced by dbus_connection_add_filter(), dbus_connection_dispatch(), and dbus_connection_remove_filter().

The documentation for this struct was generated from the following file:

- dbus-connection.c
