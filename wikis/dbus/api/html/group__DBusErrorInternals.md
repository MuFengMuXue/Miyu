Error reporting internals

D-Bus secret internal implementation details

Error reporting internals. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-structures" class="groupheader"> Data Structures</h2></td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusRealError</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusError. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_ga961cc70e3891282a65205c4c8418d88e" class="memitem:ga961cc70e3891282a65205c4c8418d88e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_ERROR_INIT   { NULL, NULL, TRUE, 0, 0, 0, 0, NULL }</td>
</tr>
<tr class="memdesc:ga961cc70e3891282a65205c4c8418d88e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Expands to a suitable initializer for a DBusError on the stack.<br />
</td>
</tr>
<tr class="separator:ga961cc70e3891282a65205c4c8418d88e">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gaaf2f2b8a3ea393225441540870b9428e" class="memitem:gaaf2f2b8a3ea393225441540870b9428e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>_DBUS_STATIC_ASSERT</strong> (sizeof(DBusRealError)==sizeof(DBusError))</td>
</tr>
<tr class="separator:gaaf2f2b8a3ea393225441540870b9428e">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Error reporting internals.

## Macro Definition Documentation

## ◆ DBUS_ERROR_INIT

|                                                                   |
|-------------------------------------------------------------------|
| \#define DBUS_ERROR_INIT   { NULL, NULL, TRUE, 0, 0, 0, 0, NULL } |

Expands to a suitable initializer for a DBusError on the stack.

Declaring a DBusError with:

DBusError error = DBUS_ERROR_INIT;

do_things_with (&error);

DBUS_ERROR_INIT

\#define DBUS_ERROR_INIT

Expands to a suitable initializer for a DBusError on the stack.

**Definition** dbus-errors.h:64

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

is a more concise form of:

DBusError error;

dbus_error_init (&error);

do_things_with (&error);

dbus_error_init

void dbus_error_init(DBusError \*error)

Initializes a DBusError structure.

**Definition** dbus-errors.c:190

Definition at line 64 of file dbus-errors.h.
