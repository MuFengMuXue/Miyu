DBusWatchList Struct Reference

D-Bus secret internal implementation details » DBusWatch implementation details

DBusWatchList implementation details. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_ab4e73fc61203dd03949f0b7d163d456d" class="memitem:ab4e73fc61203dd03949f0b7d163d456d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">watches</td>
</tr>
<tr class="memdesc:ab4e73fc61203dd03949f0b7d163d456d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Watch objects.<br />
</td>
</tr>
<tr class="separator:ab4e73fc61203dd03949f0b7d163d456d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ae515ab01e8d08e6b252e468be7dc7074" class="memitem:ae515ab01e8d08e6b252e468be7dc7074">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAddWatchFunction </td>
<td class="memItemRight" data-valign="bottom">add_watch_function</td>
</tr>
<tr class="memdesc:ae515ab01e8d08e6b252e468be7dc7074">
<td class="mdescLeft"> </td>
<td class="mdescRight">Callback for adding a watch.<br />
</td>
</tr>
<tr class="separator:ae515ab01e8d08e6b252e468be7dc7074">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a3b4b6c6d8aeb77d9b08404575e0b805a" class="memitem:a3b4b6c6d8aeb77d9b08404575e0b805a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRemoveWatchFunction </td>
<td class="memItemRight" data-valign="bottom">remove_watch_function</td>
</tr>
<tr class="memdesc:a3b4b6c6d8aeb77d9b08404575e0b805a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Callback for removing a watch.<br />
</td>
</tr>
<tr class="separator:a3b4b6c6d8aeb77d9b08404575e0b805a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aed21ba690eb810c4c2da581feaed822a" class="memitem:aed21ba690eb810c4c2da581feaed822a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatchToggledFunction </td>
<td class="memItemRight" data-valign="bottom">watch_toggled_function</td>
</tr>
<tr class="memdesc:aed21ba690eb810c4c2da581feaed822a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Callback on toggling enablement.<br />
</td>
</tr>
<tr class="separator:aed21ba690eb810c4c2da581feaed822a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a767770241baf8ddcdb4b5c4b4f2a9727" class="memitem:a767770241baf8ddcdb4b5c4b4f2a9727">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">watch_data</td>
</tr>
<tr class="memdesc:a767770241baf8ddcdb4b5c4b4f2a9727">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data for watch callbacks.<br />
</td>
</tr>
<tr class="separator:a767770241baf8ddcdb4b5c4b4f2a9727">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2308b08f7f4cb858fbcca718f2bef735" class="memitem:a2308b08f7f4cb858fbcca718f2bef735">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">watch_free_data_function</td>
</tr>
<tr class="memdesc:a2308b08f7f4cb858fbcca718f2bef735">
<td class="mdescLeft"> </td>
<td class="mdescRight">Free function for watch callback data.<br />
</td>
</tr>
<tr class="separator:a2308b08f7f4cb858fbcca718f2bef735">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusWatchList implementation details.

All fields are private.

Definition at line 216 of file dbus-watch.c.

## Field Documentation

## ◆ add_watch_function

|                                                        |
|--------------------------------------------------------|
| DBusAddWatchFunction DBusWatchList::add_watch_function |

Callback for adding a watch.

Definition at line 220 of file dbus-watch.c.

Referenced by \_dbus_watch_list_add_watch(), and \_dbus_watch_list_set_functions().

## ◆ remove_watch_function

|                                                              |
|--------------------------------------------------------------|
| DBusRemoveWatchFunction DBusWatchList::remove_watch_function |

Callback for removing a watch.

Definition at line 221 of file dbus-watch.c.

Referenced by \_dbus_watch_list_remove_watch(), and \_dbus_watch_list_set_functions().

## ◆ watch_data

|                                  |
|----------------------------------|
| void\* DBusWatchList::watch_data |

Data for watch callbacks.

Definition at line 223 of file dbus-watch.c.

Referenced by \_dbus_watch_list_add_watch(), \_dbus_watch_list_remove_watch(), \_dbus_watch_list_set_functions(), and \_dbus_watch_list_toggle_watch().

## ◆ watch_free_data_function

|                                                          |
|----------------------------------------------------------|
| DBusFreeFunction DBusWatchList::watch_free_data_function |

Free function for watch callback data.

Definition at line 224 of file dbus-watch.c.

Referenced by \_dbus_watch_list_set_functions().

## ◆ watch_toggled_function

|                                                                |
|----------------------------------------------------------------|
| DBusWatchToggledFunction DBusWatchList::watch_toggled_function |

Callback on toggling enablement.

Definition at line 222 of file dbus-watch.c.

Referenced by \_dbus_watch_list_set_functions(), and \_dbus_watch_list_toggle_watch().

## ◆ watches

|                                   |
|-----------------------------------|
| DBusList\* DBusWatchList::watches |

Watch objects.

Definition at line 218 of file dbus-watch.c.

Referenced by \_dbus_watch_list_add_watch(), \_dbus_watch_list_free(), \_dbus_watch_list_remove_watch(), \_dbus_watch_list_set_functions(), and \_dbus_watch_list_toggle_all_watches().

The documentation for this struct was generated from the following file:

- dbus-watch.c
