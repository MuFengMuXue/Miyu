DBusCondVar Struct Reference

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a1c1e453c6198b5df982ab2a7582c72d6" class="memitem:a1c1e453c6198b5df982ab2a7582c72d6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">pthread_cond_t </td>
<td class="memItemRight" data-valign="bottom">cond</td>
</tr>
<tr class="memdesc:a1c1e453c6198b5df982ab2a7582c72d6">
<td class="mdescLeft"> </td>
<td class="mdescRight">the condition<br />
</td>
</tr>
<tr class="separator:a1c1e453c6198b5df982ab2a7582c72d6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a44acb7f993730cf89d20b6e419f7a61b" class="memitem:a44acb7f993730cf89d20b6e419f7a61b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">list</td>
</tr>
<tr class="memdesc:a44acb7f993730cf89d20b6e419f7a61b">
<td class="mdescLeft"> </td>
<td class="mdescRight">list thread-local-stored events waiting on the cond variable<br />
</td>
</tr>
<tr class="separator:a44acb7f993730cf89d20b6e419f7a61b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a293695c1c540c1d98c2dbbb23ba53d58" class="memitem:a293695c1c540c1d98c2dbbb23ba53d58">
<td class="memItemLeft" style="text-align: right;" data-valign="top">CRITICAL_SECTION </td>
<td class="memItemRight" data-valign="bottom">lock</td>
</tr>
<tr class="memdesc:a293695c1c540c1d98c2dbbb23ba53d58">
<td class="mdescLeft"> </td>
<td class="mdescRight">lock protecting the list<br />
</td>
</tr>
<tr class="separator:a293695c1c540c1d98c2dbbb23ba53d58">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Definition at line 59 of file dbus-sysdeps-pthread.c.

## Field Documentation

## ◆ cond

|                                  |
|----------------------------------|
| pthread_cond_t DBusCondVar::cond |

the condition

Definition at line 60 of file dbus-sysdeps-pthread.c.

## ◆ list

|                              |
|------------------------------|
| DBusList\* DBusCondVar::list |

list thread-local-stored events waiting on the cond variable

Definition at line 67 of file dbus-sysdeps-thread-win.c.

## ◆ lock

|                                    |
|------------------------------------|
| CRITICAL_SECTION DBusCondVar::lock |

lock protecting the list

Definition at line 68 of file dbus-sysdeps-thread-win.c.

The documentation for this struct was generated from the following files:

- dbus-sysdeps-pthread.c
- dbus-sysdeps-thread-win.c
