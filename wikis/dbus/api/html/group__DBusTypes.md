Basic types

D-Bus low-level public API

dbus_bool_t, dbus_int32_t, etc. More...

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
<td class="memItemRight" data-valign="bottom">DBus8ByteStruct</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">An 8-byte struct you could use to access int64 without having int64 support. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">union  </td>
<td class="memItemRight" data-valign="bottom">DBusBasicValue</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">A simple value union that lets you access bytes as if they were various types; useful when dealing with basic types via void pointers and varargs. More...<br />
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
<tr id="r_gae974c1b29f5fecef13e54edd065abcef" class="memitem:gae974c1b29f5fecef13e54edd065abcef">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_HAVE_INT64   1</td>
</tr>
<tr class="memdesc:gae974c1b29f5fecef13e54edd065abcef">
<td class="mdescLeft"> </td>
<td class="mdescRight">Always defined.<br />
</td>
</tr>
<tr class="separator:gae974c1b29f5fecef13e54edd065abcef">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8deac39e1bf9fcca44854afeaaaf6199" class="memitem:ga8deac39e1bf9fcca44854afeaaaf6199">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INT64_CONSTANT(val)   (_DBUS_GNUC_EXTENSION (val##L))</td>
</tr>
<tr class="memdesc:ga8deac39e1bf9fcca44854afeaaaf6199">
<td class="mdescLeft"> </td>
<td class="mdescRight">Declare a 64-bit signed integer constant.<br />
</td>
</tr>
<tr class="separator:ga8deac39e1bf9fcca44854afeaaaf6199">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga20f58889c3ab16344378449148264f6d" class="memitem:ga20f58889c3ab16344378449148264f6d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_UINT64_CONSTANT(val)   (_DBUS_GNUC_EXTENSION (val##UL))</td>
</tr>
<tr class="memdesc:ga20f58889c3ab16344378449148264f6d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Declare a 64-bit unsigned integer constant.<br />
</td>
</tr>
<tr class="separator:ga20f58889c3ab16344378449148264f6d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga75f95022ddb575eb714d7f809af4768c" class="memitem:ga75f95022ddb575eb714d7f809af4768c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_INT64_MODIFIER   "l"</td>
</tr>
<tr class="memdesc:ga75f95022ddb575eb714d7f809af4768c">
<td class="mdescLeft"> </td>
<td class="mdescRight">A string literal for a length modifier that is appropriate to print the dbus_int64_t and dbus_uint64_t types.<br />
</td>
</tr>
<tr class="separator:ga75f95022ddb575eb714d7f809af4768c">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

dbus_bool_t, dbus_int32_t, etc.

Typedefs for common primitive types.

## Macro Definition Documentation

## ◆ DBUS_HAVE_INT64

|                              |
|------------------------------|
| \#define DBUS_HAVE_INT64   1 |

Always defined.

In older libdbus versions, this would be undefined if there was no 64-bit integer type on that platform. libdbus no longer supports such platforms.

Definition at line 36 of file dbus-arch-deps.h.

## ◆ DBUS_INT64_CONSTANT

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define DBUS_INT64_CONSTANT | ( |   | val | ) |    (\_DBUS_GNUC_EXTENSION (val##L)) |

Declare a 64-bit signed integer constant.

The macro adds the necessary "LL" or whatever after the integer, giving a literal such as "325145246765LL"

Definition at line 41 of file dbus-arch-deps.h.

## ◆ DBUS_INT64_MODIFIER

|                                    |
|------------------------------------|
| \#define DBUS_INT64_MODIFIER   "l" |

A string literal for a length modifier that is appropriate to print the dbus_int64_t and dbus_uint64_t types.

For example, it might be an empty string, "l", "ll", or "I64".

This modifier needs to be concatenated with a literal "%" and a conversion specifier that can print signed or unsigned integers, for example:

dbus_int64_t i = -123;

dbus_uint64_t u = 456;

printf ("signed: %" DBUS_INT64_MODIFIER "d\n", i);

printf ("unsigned decimal: %" DBUS_INT64_MODIFIER "u\n", u);

printf ("unsigned hex: 0x%" DBUS_INT64_MODIFIER "x\n", x);

DBUS_INT64_MODIFIER

\#define DBUS_INT64_MODIFIER

A string literal for a length modifier that is appropriate to print the dbus_int64_t and dbus_uint64\_...

**Definition** dbus-arch-deps.h:39

Definition at line 39 of file dbus-arch-deps.h.

## ◆ DBUS_UINT64_CONSTANT

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define DBUS_UINT64_CONSTANT | ( |   | val | ) |    (\_DBUS_GNUC_EXTENSION (val##UL)) |

Declare a 64-bit unsigned integer constant.

The macro adds the necessary "ULL" or whatever after the integer, giving a literal such as "325145246765ULL"

Definition at line 42 of file dbus-arch-deps.h.
