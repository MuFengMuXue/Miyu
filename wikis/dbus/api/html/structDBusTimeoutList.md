DBusTimeoutList Struct Reference

D-Bus secret internal implementation details » DBusTimeout implementation details

DBusTimeoutList implementation details. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a56d9070375880b7d931f887564981f80" class="memitem:a56d9070375880b7d931f887564981f80">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">timeouts</td>
</tr>
<tr class="memdesc:a56d9070375880b7d931f887564981f80">
<td class="mdescLeft"> </td>
<td class="mdescRight">Timeout objects.<br />
</td>
</tr>
<tr class="separator:a56d9070375880b7d931f887564981f80">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aab57481c712e47f9157d23bc6731972e" class="memitem:aab57481c712e47f9157d23bc6731972e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAddTimeoutFunction </td>
<td class="memItemRight" data-valign="bottom">add_timeout_function</td>
</tr>
<tr class="memdesc:aab57481c712e47f9157d23bc6731972e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Callback for adding a timeout.<br />
</td>
</tr>
<tr class="separator:aab57481c712e47f9157d23bc6731972e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a51d25b272b950c3f63b3b71926940a55" class="memitem:a51d25b272b950c3f63b3b71926940a55">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRemoveTimeoutFunction </td>
<td class="memItemRight" data-valign="bottom">remove_timeout_function</td>
</tr>
<tr class="memdesc:a51d25b272b950c3f63b3b71926940a55">
<td class="mdescLeft"> </td>
<td class="mdescRight">Callback for removing a timeout.<br />
</td>
</tr>
<tr class="separator:a51d25b272b950c3f63b3b71926940a55">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a198efba668450ebafa97e9d5197fcc2e" class="memitem:a198efba668450ebafa97e9d5197fcc2e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTimeoutToggledFunction </td>
<td class="memItemRight" data-valign="bottom">timeout_toggled_function</td>
</tr>
<tr class="memdesc:a198efba668450ebafa97e9d5197fcc2e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Callback when timeout is enabled/disabled or changes interval.<br />
</td>
</tr>
<tr class="separator:a198efba668450ebafa97e9d5197fcc2e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af26804f9320628b977e7afeeea3750eb" class="memitem:af26804f9320628b977e7afeeea3750eb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">timeout_data</td>
</tr>
<tr class="memdesc:af26804f9320628b977e7afeeea3750eb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data for timeout callbacks.<br />
</td>
</tr>
<tr class="separator:af26804f9320628b977e7afeeea3750eb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac93efcdc11b6e68d19f1e57e0bff72f7" class="memitem:ac93efcdc11b6e68d19f1e57e0bff72f7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">timeout_free_data_function</td>
</tr>
<tr class="memdesc:ac93efcdc11b6e68d19f1e57e0bff72f7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Free function for timeout callback data.<br />
</td>
</tr>
<tr class="separator:ac93efcdc11b6e68d19f1e57e0bff72f7">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusTimeoutList implementation details.

All fields are private.

Definition at line 182 of file dbus-timeout.c.

## Field Documentation

## ◆ add_timeout_function

|                                                              |
|--------------------------------------------------------------|
| DBusAddTimeoutFunction DBusTimeoutList::add_timeout_function |

Callback for adding a timeout.

Definition at line 186 of file dbus-timeout.c.

Referenced by \_dbus_timeout_list_add_timeout(), and \_dbus_timeout_list_set_functions().

## ◆ remove_timeout_function

|                                                                    |
|--------------------------------------------------------------------|
| DBusRemoveTimeoutFunction DBusTimeoutList::remove_timeout_function |

Callback for removing a timeout.

Definition at line 187 of file dbus-timeout.c.

Referenced by \_dbus_timeout_list_remove_timeout(), and \_dbus_timeout_list_set_functions().

## ◆ timeout_data

|                                      |
|--------------------------------------|
| void\* DBusTimeoutList::timeout_data |

Data for timeout callbacks.

Definition at line 189 of file dbus-timeout.c.

Referenced by \_dbus_timeout_list_add_timeout(), \_dbus_timeout_list_remove_timeout(), \_dbus_timeout_list_set_functions(), and \_dbus_timeout_list_toggle_timeout().

## ◆ timeout_free_data_function

|                                                              |
|--------------------------------------------------------------|
| DBusFreeFunction DBusTimeoutList::timeout_free_data_function |

Free function for timeout callback data.

Definition at line 190 of file dbus-timeout.c.

Referenced by \_dbus_timeout_list_set_functions().

## ◆ timeout_toggled_function

|                                                                      |
|----------------------------------------------------------------------|
| DBusTimeoutToggledFunction DBusTimeoutList::timeout_toggled_function |

Callback when timeout is enabled/disabled or changes interval.

Definition at line 188 of file dbus-timeout.c.

Referenced by \_dbus_timeout_list_set_functions(), and \_dbus_timeout_list_toggle_timeout().

## ◆ timeouts

|                                      |
|--------------------------------------|
| DBusList\* DBusTimeoutList::timeouts |

Timeout objects.

Definition at line 184 of file dbus-timeout.c.

Referenced by \_dbus_timeout_list_add_timeout(), \_dbus_timeout_list_free(), \_dbus_timeout_list_remove_timeout(), and \_dbus_timeout_list_set_functions().

The documentation for this struct was generated from the following file:

- dbus-timeout.c
