DBusString implementation details

D-Bus secret internal implementation details

DBusString implementation details. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_ga1e3535c07f25485129d9d17194e303af" class="memitem:ga1e3535c07f25485129d9d17194e303af">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_STRING_MAX_LENGTH   (_DBUS_INT32_MAX - _DBUS_STRING_ALLOCATION_PADDING)</td>
</tr>
<tr class="memdesc:ga1e3535c07f25485129d9d17194e303af">
<td class="mdescLeft"> </td>
<td class="mdescRight">The maximum length of a DBusString.<br />
</td>
</tr>
<tr class="separator:ga1e3535c07f25485129d9d17194e303af">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga862cb88a139179981e1fcd5643165b56" class="memitem:ga862cb88a139179981e1fcd5643165b56">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_GENERIC_STRING_PREAMBLE(real)</td>
</tr>
<tr class="memdesc:ga862cb88a139179981e1fcd5643165b56">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks a bunch of assertions about a string object.<br />
</td>
</tr>
<tr class="separator:ga862cb88a139179981e1fcd5643165b56">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga376570af2af3ebb7e59d45b49b9582b3" class="memitem:ga376570af2af3ebb7e59d45b49b9582b3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_STRING_PREAMBLE(str)</td>
</tr>
<tr class="memdesc:ga376570af2af3ebb7e59d45b49b9582b3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks assertions about a string object that needs to be modifiable - may not be locked or const.<br />
</td>
</tr>
<tr class="separator:ga376570af2af3ebb7e59d45b49b9582b3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad9f957c4027c34a5c330822aa98b9307" class="memitem:gad9f957c4027c34a5c330822aa98b9307">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_LOCKED_STRING_PREAMBLE(str)</td>
</tr>
<tr class="memdesc:gad9f957c4027c34a5c330822aa98b9307">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks assertions about a string object that may be locked but can't be const.<br />
</td>
</tr>
<tr class="separator:gad9f957c4027c34a5c330822aa98b9307">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5cf5f12f6d8f839e9a7c3ad790a83316" class="memitem:ga5cf5f12f6d8f839e9a7c3ad790a83316">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_CONST_STRING_PREAMBLE(str)</td>
</tr>
<tr class="memdesc:ga5cf5f12f6d8f839e9a7c3ad790a83316">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks assertions about a string that may be const or locked.<br />
</td>
</tr>
<tr class="separator:ga5cf5f12f6d8f839e9a7c3ad790a83316">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8f488964e430c0ae6a1a4204e0098dfe" class="memitem:ga8f488964e430c0ae6a1a4204e0098dfe">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_IS_ASCII_BLANK(c)   ((c) == ' ' || (c) == '\t')</td>
</tr>
<tr class="memdesc:ga8f488964e430c0ae6a1a4204e0098dfe">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks for ASCII blank byte.<br />
</td>
</tr>
<tr class="separator:ga8f488964e430c0ae6a1a4204e0098dfe">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9c88845804be152df28b81d7cad5673a" class="memitem:ga9c88845804be152df28b81d7cad5673a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_IS_ASCII_WHITE(c)   ((c) == ' ' || (c) == '\t' || (c) == '\n' || (c) == '\r')</td>
</tr>
<tr class="memdesc:ga9c88845804be152df28b81d7cad5673a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks for ASCII whitespace byte.<br />
</td>
</tr>
<tr class="separator:ga9c88845804be152df28b81d7cad5673a">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusString implementation details.

The guts of DBusString.

## Macro Definition Documentation

## ◆ \_DBUS_STRING_MAX_LENGTH

|  |
|----|
| \#define \_DBUS_STRING_MAX_LENGTH   (\_DBUS_INT32_MAX - \_DBUS_STRING_ALLOCATION_PADDING) |

The maximum length of a DBusString.

Definition at line 71 of file dbus-string-private.h.

## ◆ DBUS_CONST_STRING_PREAMBLE

|                                     |     |     |     |     |     |
|-------------------------------------|-----|-----|-----|-----|-----|
| \#define DBUS_CONST_STRING_PREAMBLE | (   |     | str | )   |     |

**Value:**

const DBusRealString \*real = (DBusRealString\*) str; \\

DBUS_GENERIC_STRING_PREAMBLE (real)

DBusRealString

Internals of DBusString.

**Definition** dbus-string-private.h:46

Checks assertions about a string that may be const or locked.

Also declares the "real" variable pointing to DBusRealString.

Parameters  
|     |             |
|-----|-------------|
| str | the string. |

Definition at line 116 of file dbus-string-private.h.

## ◆ DBUS_GENERIC_STRING_PREAMBLE

|                                       |     |     |      |     |     |
|---------------------------------------|-----|-----|------|-----|-----|
| \#define DBUS_GENERIC_STRING_PREAMBLE | (   |     | real | )   |     |

**Value:**

do { \\

(void) real; /\* might be unused unless asserting \*/ \\

\_dbus_assert ((real) != NULL); \\

\_dbus_assert ((real)-\>valid); \\

\_dbus_assert ((real)-\>len \>= 0); \\

\_dbus_assert ((real)-\>allocated \>= 0); \\

\_dbus_assert ((real)-\>len \<= ((real)-\>allocated - \_DBUS_STRING_ALLOCATION_PADDING)); \\

\_dbus_assert ((real)-\>len \<= \_DBUS_STRING_MAX_LENGTH); \\

} while (0)

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

\_DBUS_STRING_MAX_LENGTH

\#define \_DBUS_STRING_MAX_LENGTH

The maximum length of a DBusString.

**Definition** dbus-string-private.h:71

Checks a bunch of assertions about a string object.

Parameters  
|      |                    |
|------|--------------------|
| real | the DBusRealString |

Definition at line 78 of file dbus-string-private.h.

## ◆ DBUS_IS_ASCII_BLANK

|                              |     |     |     |     |                                  |
|------------------------------|-----|-----|-----|-----|----------------------------------|
| \#define DBUS_IS_ASCII_BLANK | (   |     | c   | )   |    ((c) == ' ' \|\| (c) == '\t') |

Checks for ASCII blank byte.

Parameters  
|     |          |
|-----|----------|
| c   | the byte |

Definition at line 123 of file dbus-string-private.h.

## ◆ DBUS_IS_ASCII_WHITE

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define DBUS_IS_ASCII_WHITE | ( |   | c | ) |    ((c) == ' ' \|\| (c) == '\t' \|\| (c) == '\n' \|\| (c) == '\r') |

Checks for ASCII whitespace byte.

Parameters  
|     |          |
|-----|----------|
| c   | the byte |

Definition at line 129 of file dbus-string-private.h.

## ◆ DBUS_LOCKED_STRING_PREAMBLE

|                                      |     |     |     |     |     |
|--------------------------------------|-----|-----|-----|-----|-----|
| \#define DBUS_LOCKED_STRING_PREAMBLE | (   |     | str | )   |     |

**Value:**

DBusRealString \*real = (DBusRealString\*) str; \\

DBUS_GENERIC_STRING_PREAMBLE (real); \\

\_dbus_assert (!(real)-\>constant)

Checks assertions about a string object that may be locked but can't be const.

i.e. a string object that we can free. Also declares the "real" variable pointing to DBusRealString.

Parameters  
|     |            |
|-----|------------|
| str | the string |

Definition at line 107 of file dbus-string-private.h.

## ◆ DBUS_STRING_PREAMBLE

|                               |     |     |     |     |     |
|-------------------------------|-----|-----|-----|-----|-----|
| \#define DBUS_STRING_PREAMBLE | (   |     | str | )   |     |

**Value:**

DBusRealString \*real = (DBusRealString\*) str; \\

DBUS_GENERIC_STRING_PREAMBLE (real); \\

\_dbus_assert (!(real)-\>constant); \\

\_dbus_assert (!(real)-\>locked)

Checks assertions about a string object that needs to be modifiable - may not be locked or const.

Also declares the "real" variable pointing to DBusRealString.

Parameters  
|     |            |
|-----|------------|
| str | the string |

Definition at line 95 of file dbus-string-private.h.
