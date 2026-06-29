ShutdownClosure Struct Reference

D-Bus secret internal implementation details » Memory allocation implementation details

This struct represents a function to be called on shutdown. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a2152ea3eed35addda2f33eee5fbcdd26" class="memitem:a2152ea3eed35addda2f33eee5fbcdd26">
<td class="memItemLeft" style="text-align: right;" data-valign="top">ShutdownClosure * </td>
<td class="memItemRight" data-valign="bottom">next</td>
</tr>
<tr class="memdesc:a2152ea3eed35addda2f33eee5fbcdd26">
<td class="mdescLeft"> </td>
<td class="mdescRight">Next ShutdownClosure.<br />
</td>
</tr>
<tr class="separator:a2152ea3eed35addda2f33eee5fbcdd26">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8d8d4ad2e646f8643a8044de02cf823f" class="memitem:a8d8d4ad2e646f8643a8044de02cf823f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusShutdownFunction </td>
<td class="memItemRight" data-valign="bottom">func</td>
</tr>
<tr class="memdesc:a8d8d4ad2e646f8643a8044de02cf823f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to call.<br />
</td>
</tr>
<tr class="separator:a8d8d4ad2e646f8643a8044de02cf823f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ab6f70dacffc0aa2376a6c26e1fb17518" class="memitem:ab6f70dacffc0aa2376a6c26e1fb17518">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">data</td>
</tr>
<tr class="memdesc:ab6f70dacffc0aa2376a6c26e1fb17518">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data for function.<br />
</td>
</tr>
<tr class="separator:ab6f70dacffc0aa2376a6c26e1fb17518">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

This struct represents a function to be called on shutdown.

Definition at line 800 of file dbus-memory.c.

## Field Documentation

## ◆ data

|                              |
|------------------------------|
| void\* ShutdownClosure::data |

Data for function.

Definition at line 804 of file dbus-memory.c.

Referenced by dbus_shutdown().

## ◆ func

|                                            |
|--------------------------------------------|
| DBusShutdownFunction ShutdownClosure::func |

Function to call.

Definition at line 803 of file dbus-memory.c.

Referenced by dbus_shutdown().

## ◆ next

|                                         |
|-----------------------------------------|
| ShutdownClosure\* ShutdownClosure::next |

Next ShutdownClosure.

Definition at line 802 of file dbus-memory.c.

Referenced by dbus_shutdown().

The documentation for this struct was generated from the following file:

- dbus-memory.c
