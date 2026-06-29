DBusSignatureRealIter Struct Reference

Implementation details of DBusSignatureIter, all fields are private. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a88eb8e63ea2550b23ab4e5a2056168c5" class="memitem:a88eb8e63ea2550b23ab4e5a2056168c5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">pos</td>
</tr>
<tr class="memdesc:a88eb8e63ea2550b23ab4e5a2056168c5">
<td class="mdescLeft"> </td>
<td class="mdescRight">current position in the signature string<br />
</td>
</tr>
<tr class="separator:a88eb8e63ea2550b23ab4e5a2056168c5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a54aa77a50490febee5d9b1cbce690639" class="memitem:a54aa77a50490febee5d9b1cbce690639">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">finished: 1</td>
</tr>
<tr class="memdesc:a54aa77a50490febee5d9b1cbce690639">
<td class="mdescLeft"> </td>
<td class="mdescRight">true if we are at the end iter<br />
</td>
</tr>
<tr class="separator:a54aa77a50490febee5d9b1cbce690639">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a575114ffd9f42eb84909ea6c5d912c75" class="memitem:a575114ffd9f42eb84909ea6c5d912c75">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">in_array: 1</td>
</tr>
<tr class="memdesc:a575114ffd9f42eb84909ea6c5d912c75">
<td class="mdescLeft"> </td>
<td class="mdescRight">true if we are a subiterator pointing to an array's element type<br />
</td>
</tr>
<tr class="separator:a575114ffd9f42eb84909ea6c5d912c75">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusSignatureIter, all fields are private.

Definition at line 38 of file dbus-signature.c.

## Field Documentation

## ◆ finished

|                                              |
|----------------------------------------------|
| unsigned int DBusSignatureRealIter::finished |

true if we are at the end iter

Definition at line 41 of file dbus-signature.c.

Referenced by dbus_signature_iter_init(), and dbus_signature_iter_next().

## ◆ in_array

|                                              |
|----------------------------------------------|
| unsigned int DBusSignatureRealIter::in_array |

true if we are a subiterator pointing to an array's element type

Definition at line 42 of file dbus-signature.c.

Referenced by dbus_signature_iter_init(), dbus_signature_iter_next(), and dbus_signature_iter_recurse().

## ◆ pos

|                                         |
|-----------------------------------------|
| const char\* DBusSignatureRealIter::pos |

current position in the signature string

Definition at line 40 of file dbus-signature.c.

Referenced by dbus_signature_iter_get_current_type(), dbus_signature_iter_get_element_type(), dbus_signature_iter_get_signature(), dbus_signature_iter_init(), dbus_signature_iter_next(), and dbus_signature_iter_recurse().

The documentation for this struct was generated from the following file:

- dbus-signature.c
