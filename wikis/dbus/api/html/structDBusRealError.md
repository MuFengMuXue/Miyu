DBusRealError Struct Reference

D-Bus secret internal implementation details » Error reporting internals

Internals of DBusError. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a269069d5d2fc0f33deced317cb435de9" class="memitem:a269069d5d2fc0f33deced317cb435de9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">name</td>
</tr>
<tr class="memdesc:a269069d5d2fc0f33deced317cb435de9">
<td class="mdescLeft"> </td>
<td class="mdescRight">error name<br />
</td>
</tr>
<tr class="separator:a269069d5d2fc0f33deced317cb435de9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_afd09fc7ff565b5f3b410ee1ce985172b" class="memitem:afd09fc7ff565b5f3b410ee1ce985172b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">message</td>
</tr>
<tr class="memdesc:afd09fc7ff565b5f3b410ee1ce985172b">
<td class="mdescLeft"> </td>
<td class="mdescRight">error message<br />
</td>
</tr>
<tr class="separator:afd09fc7ff565b5f3b410ee1ce985172b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a3e95ec02e0320fe0bfccf24fb4b8db8a" class="memitem:a3e95ec02e0320fe0bfccf24fb4b8db8a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">const_message: 1</td>
</tr>
<tr class="memdesc:a3e95ec02e0320fe0bfccf24fb4b8db8a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Message is not owned by DBusError.<br />
</td>
</tr>
<tr class="separator:a3e95ec02e0320fe0bfccf24fb4b8db8a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a1b4f15b6d9a85a37f3ab9e95fff179e1" class="memitem:a1b4f15b6d9a85a37f3ab9e95fff179e1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">dummy2: 1</td>
</tr>
<tr class="memdesc:a1b4f15b6d9a85a37f3ab9e95fff179e1">
<td class="mdescLeft"> </td>
<td class="mdescRight">placeholder<br />
</td>
</tr>
<tr class="separator:a1b4f15b6d9a85a37f3ab9e95fff179e1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a72b752e63b30144ece9dc9a072d58995" class="memitem:a72b752e63b30144ece9dc9a072d58995">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">dummy3: 1</td>
</tr>
<tr class="memdesc:a72b752e63b30144ece9dc9a072d58995">
<td class="mdescLeft"> </td>
<td class="mdescRight">placeholder<br />
</td>
</tr>
<tr class="separator:a72b752e63b30144ece9dc9a072d58995">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a67d03b32ec168e2676a886dc260a08fa" class="memitem:a67d03b32ec168e2676a886dc260a08fa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">dummy4: 1</td>
</tr>
<tr class="memdesc:a67d03b32ec168e2676a886dc260a08fa">
<td class="mdescLeft"> </td>
<td class="mdescRight">placeholder<br />
</td>
</tr>
<tr class="separator:a67d03b32ec168e2676a886dc260a08fa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5beec0e4c6f956795eebe49593878f31" class="memitem:a5beec0e4c6f956795eebe49593878f31">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">dummy5: 1</td>
</tr>
<tr class="memdesc:a5beec0e4c6f956795eebe49593878f31">
<td class="mdescLeft"> </td>
<td class="mdescRight">placeholder<br />
</td>
</tr>
<tr class="separator:a5beec0e4c6f956795eebe49593878f31">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa0aaa5baa7ae43bb669e9b36ffd4a246" class="memitem:aa0aaa5baa7ae43bb669e9b36ffd4a246">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">padding1</td>
</tr>
<tr class="memdesc:aa0aaa5baa7ae43bb669e9b36ffd4a246">
<td class="mdescLeft"> </td>
<td class="mdescRight">placeholder<br />
</td>
</tr>
<tr class="separator:aa0aaa5baa7ae43bb669e9b36ffd4a246">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internals of DBusError.

Definition at line 67 of file dbus-errors.c.

## Field Documentation

## ◆ const_message

|                                           |
|-------------------------------------------|
| unsigned int DBusRealError::const_message |

Message is not owned by DBusError.

Definition at line 72 of file dbus-errors.c.

Referenced by dbus_error_free(), dbus_error_init(), and dbus_set_error_const().

## ◆ dummy2

|                                    |
|------------------------------------|
| unsigned int DBusRealError::dummy2 |

placeholder

Definition at line 74 of file dbus-errors.c.

## ◆ dummy3

|                                    |
|------------------------------------|
| unsigned int DBusRealError::dummy3 |

placeholder

Definition at line 75 of file dbus-errors.c.

## ◆ dummy4

|                                    |
|------------------------------------|
| unsigned int DBusRealError::dummy4 |

placeholder

Definition at line 76 of file dbus-errors.c.

## ◆ dummy5

|                                    |
|------------------------------------|
| unsigned int DBusRealError::dummy5 |

placeholder

Definition at line 77 of file dbus-errors.c.

## ◆ message

|                               |
|-------------------------------|
| char\* DBusRealError::message |

error message

Definition at line 70 of file dbus-errors.c.

Referenced by dbus_error_free(), dbus_error_init(), and dbus_set_error_const().

## ◆ name

|                            |
|----------------------------|
| char\* DBusRealError::name |

error name

Definition at line 69 of file dbus-errors.c.

Referenced by dbus_error_free(), dbus_error_init(), and dbus_set_error_const().

## ◆ padding1

|                                |
|--------------------------------|
| void\* DBusRealError::padding1 |

placeholder

Definition at line 79 of file dbus-errors.c.

The documentation for this struct was generated from the following file:

- dbus-errors.c
