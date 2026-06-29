DBusAuthStateData Struct Reference

D-Bus secret internal implementation details » Authentication implementation details

Information about a auth state. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_ad5e3d100798e1f200c8b7b2277af46af" class="memitem:ad5e3d100798e1f200c8b7b2277af46af">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">name</td>
</tr>
<tr class="memdesc:ad5e3d100798e1f200c8b7b2277af46af">
<td class="mdescLeft"> </td>
<td class="mdescRight">Name of the state.<br />
</td>
</tr>
<tr class="separator:ad5e3d100798e1f200c8b7b2277af46af">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5b22dcc2e9ccfae518d95c14893fa495" class="memitem:a5b22dcc2e9ccfae518d95c14893fa495">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAuthStateFunction </td>
<td class="memItemRight" data-valign="bottom">handler</td>
</tr>
<tr class="memdesc:a5b22dcc2e9ccfae518d95c14893fa495">
<td class="mdescLeft"> </td>
<td class="mdescRight">State function for this state.<br />
</td>
</tr>
<tr class="separator:a5b22dcc2e9ccfae518d95c14893fa495">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Information about a auth state.

Definition at line 146 of file dbus-auth.c.

## Field Documentation

## ◆ handler

|                                                  |
|--------------------------------------------------|
| DBusAuthStateFunction DBusAuthStateData::handler |

State function for this state.

Definition at line 149 of file dbus-auth.c.

## ◆ name

|                                      |
|--------------------------------------|
| const char\* DBusAuthStateData::name |

Name of the state.

Definition at line 148 of file dbus-auth.c.

The documentation for this struct was generated from the following file:

- dbus-auth.c
