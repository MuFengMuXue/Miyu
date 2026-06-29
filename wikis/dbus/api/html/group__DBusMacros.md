Utility macros

D-Bus low-level public API

TRUE, FALSE, NULL, and so on More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_ga875146b01015e9ced22b25d76d549ab2" class="memitem:ga875146b01015e9ced22b25d76d549ab2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_BEGIN_DECLS</td>
</tr>
<tr class="memdesc:ga875146b01015e9ced22b25d76d549ab2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Macro used prior to declaring functions in the D-Bus header files.<br />
</td>
</tr>
<tr class="separator:ga875146b01015e9ced22b25d76d549ab2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae4a9263a43f8220f6e1c0fd07cf6e59a" class="memitem:gae4a9263a43f8220f6e1c0fd07cf6e59a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_END_DECLS</td>
</tr>
<tr class="memdesc:gae4a9263a43f8220f6e1c0fd07cf6e59a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Macro used after declaring functions in the D-Bus header files.<br />
</td>
</tr>
<tr class="separator:gae4a9263a43f8220f6e1c0fd07cf6e59a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa8cecfc5c5c054d2875c03e77b7be15d" class="memitem:gaa8cecfc5c5c054d2875c03e77b7be15d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">TRUE   1</td>
</tr>
<tr class="memdesc:gaa8cecfc5c5c054d2875c03e77b7be15d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Expands to "1".<br />
</td>
</tr>
<tr class="separator:gaa8cecfc5c5c054d2875c03e77b7be15d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa93f0eb578d23995850d61f7d61c55c1" class="memitem:gaa93f0eb578d23995850d61f7d61c55c1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">FALSE   0</td>
</tr>
<tr class="memdesc:gaa93f0eb578d23995850d61f7d61c55c1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Expands to "0".<br />
</td>
</tr>
<tr class="separator:gaa93f0eb578d23995850d61f7d61c55c1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga070d2ce7b6bb7e5c05602aa8c308d0c4" class="memitem:ga070d2ce7b6bb7e5c05602aa8c308d0c4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">NULL   ((void*) 0)</td>
</tr>
<tr class="memdesc:ga070d2ce7b6bb7e5c05602aa8c308d0c4">
<td class="mdescLeft"> </td>
<td class="mdescRight">A null pointer, defined appropriately for C or C++.<br />
</td>
</tr>
<tr class="separator:ga070d2ce7b6bb7e5c05602aa8c308d0c4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7b014fa99f6ef38c1aa5a9c02468e3a0" class="memitem:ga7b014fa99f6ef38c1aa5a9c02468e3a0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_DEPRECATED</td>
</tr>
<tr class="memdesc:ga7b014fa99f6ef38c1aa5a9c02468e3a0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tells the compiler to warn about a function or type if it's used.<br />
</td>
</tr>
<tr class="separator:ga7b014fa99f6ef38c1aa5a9c02468e3a0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4fa4b760e4b3d14076981ad21407b5c8" class="memitem:ga4fa4b760e4b3d14076981ad21407b5c8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_GNUC_EXTENSION</td>
</tr>
<tr class="memdesc:ga4fa4b760e4b3d14076981ad21407b5c8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tells gcc not to warn about extensions to the C standard in the following expression, even if compiling with -pedantic.<br />
</td>
</tr>
<tr class="separator:ga4fa4b760e4b3d14076981ad21407b5c8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab64386a75b748deb7e3bc41a417d5661" class="memitem:gab64386a75b748deb7e3bc41a417d5661">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_EXPORT</td>
</tr>
<tr class="separator:gab64386a75b748deb7e3bc41a417d5661">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7ef8b5647761490d2e5c225d10665a1c" class="memitem:ga7ef8b5647761490d2e5c225d10665a1c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_dbus_clear_pointer_impl(T, pointer_to_pointer, destroy)</td>
</tr>
<tr class="separator:ga7ef8b5647761490d2e5c225d10665a1c">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

TRUE, FALSE, NULL, and so on

Utility macros.

## Macro Definition Documentation

## ◆ \_dbus_clear_pointer_impl

|                                    |     |     |                     |
|------------------------------------|-----|-----|---------------------|
| \#define \_dbus_clear_pointer_impl | (   |     | T,                  |
|                                    |     |     | pointer_to_pointer, |
|                                    |     |     | destroy             |
|                                    | )   |     |                     |

**Value:**

do { \\

T \*\*\_pp = (pointer_to_pointer); \\

T \*\_value = \*\_pp; \\

\\

\*\_pp = NULL; \\

\\

if (\_value != NULL) \\

destroy (\_value); \\

} while (0)

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

Definition at line 223 of file dbus-macros.h.

## ◆ \_DBUS_GNUC_EXTENSION

|                                |
|--------------------------------|
| \#define \_DBUS_GNUC_EXTENSION |

Tells gcc not to warn about extensions to the C standard in the following expression, even if compiling with -pedantic.

Do not use this macro in your own code; please consider it to be internal to libdbus.

Definition at line 66 of file dbus-macros.h.

## ◆ DBUS_BEGIN_DECLS

|                           |
|---------------------------|
| \#define DBUS_BEGIN_DECLS |

Macro used prior to declaring functions in the D-Bus header files.

Expands to "extern "C"" when using a C++ compiler, and expands to nothing when using a C compiler.

Please don't use this in your own code, consider it D-Bus internal.

Definition at line 36 of file dbus-macros.h.

## ◆ DBUS_DEPRECATED

|                          |
|--------------------------|
| \#define DBUS_DEPRECATED |

Tells the compiler to warn about a function or type if it's used.

Code marked in this way should also be enclosed in

\#ifndef DBUS_DISABLE_DEPRECATED

deprecated stuff here

\#endif

Please don't use this in your own code, consider it D-Bus internal.

Definition at line 60 of file dbus-macros.h.

## ◆ DBUS_END_DECLS

|                         |
|-------------------------|
| \#define DBUS_END_DECLS |

Macro used after declaring functions in the D-Bus header files.

Expands to "}" when using a C++ compiler, and expands to nothing when using a C compiler.

Please don't use this in your own code, consider it D-Bus internal.

Definition at line 37 of file dbus-macros.h.

## ◆ DBUS_EXPORT

|                      |
|----------------------|
| \#define DBUS_EXPORT |

Definition at line 212 of file dbus-macros.h.

## ◆ FALSE

|                    |
|--------------------|
| \#define FALSE   0 |

Expands to "0".

Definition at line 44 of file dbus-macros.h.

## ◆ NULL

|                              |
|------------------------------|
| \#define NULL   ((void\*) 0) |

A null pointer, defined appropriately for C or C++.

Definition at line 51 of file dbus-macros.h.

## ◆ TRUE

|                   |
|-------------------|
| \#define TRUE   1 |

Expands to "1".

Definition at line 41 of file dbus-macros.h.
