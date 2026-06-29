Linked list

D-Bus secret internal implementation details

DBusList data structure. More...

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
<td class="memItemRight" data-valign="bottom">DBusList</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">A node in a linked list. More...<br />
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
<tr id="r_gaede4ace46d5ee497d75074bfec4490a2" class="memitem:gaede4ace46d5ee497d75074bfec4490a2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_get_next_link(list, link)   ((link)-&gt;next == *(list) ? NULL : (link)-&gt;next)</td>
</tr>
<tr class="memdesc:gaede4ace46d5ee497d75074bfec4490a2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the next link in the list, or NULL if there are no more links.<br />
</td>
</tr>
<tr class="separator:gaede4ace46d5ee497d75074bfec4490a2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6637493bf5fc09bddb44ac295c475cae" class="memitem:ga6637493bf5fc09bddb44ac295c475cae">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_get_prev_link(list, link)   ((link) == *(list) ? NULL : (link)-&gt;prev)</td>
</tr>
<tr class="memdesc:ga6637493bf5fc09bddb44ac295c475cae">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the previous link in the list, or NULL if there are no more links.<br />
</td>
</tr>
<tr class="separator:ga6637493bf5fc09bddb44ac295c475cae">
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
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gac592b0024857d7c1e9b01cee5f8b7f4d" class="memitem:gac592b0024857d7c1e9b01cee5f8b7f4d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_alloc_link (void *data)</td>
</tr>
<tr class="memdesc:gac592b0024857d7c1e9b01cee5f8b7f4d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocates a linked list node.<br />
</td>
</tr>
<tr class="separator:gac592b0024857d7c1e9b01cee5f8b7f4d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6e824f717125ce40c549d5402e32610f" class="memitem:ga6e824f717125ce40c549d5402e32610f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_free_link (DBusList *link)</td>
</tr>
<tr class="memdesc:ga6e824f717125ce40c549d5402e32610f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a linked list node allocated with _dbus_list_alloc_link.<br />
</td>
</tr>
<tr class="separator:ga6e824f717125ce40c549d5402e32610f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad99045e79db46159babe69718f343053" class="memitem:gad99045e79db46159babe69718f343053">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_append (DBusList **list, void *data)</td>
</tr>
<tr class="memdesc:gad99045e79db46159babe69718f343053">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends a value to the list.<br />
</td>
</tr>
<tr class="separator:gad99045e79db46159babe69718f343053">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab4aa60e0466ac7075f3d1751909d6a52" class="memitem:gab4aa60e0466ac7075f3d1751909d6a52">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_prepend (DBusList **list, void *data)</td>
</tr>
<tr class="memdesc:gab4aa60e0466ac7075f3d1751909d6a52">
<td class="mdescLeft"> </td>
<td class="mdescRight">Prepends a value to the list.<br />
</td>
</tr>
<tr class="separator:gab4aa60e0466ac7075f3d1751909d6a52">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga20e549175e2b8f450f907592dc39d953" class="memitem:ga20e549175e2b8f450f907592dc39d953">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_append_link (DBusList **list, DBusList *link)</td>
</tr>
<tr class="memdesc:ga20e549175e2b8f450f907592dc39d953">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends a link to the list.<br />
</td>
</tr>
<tr class="separator:ga20e549175e2b8f450f907592dc39d953">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab3dd068e3bd8a319c0d12150785050a7" class="memitem:gab3dd068e3bd8a319c0d12150785050a7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_prepend_link (DBusList **list, DBusList *link)</td>
</tr>
<tr class="memdesc:gab3dd068e3bd8a319c0d12150785050a7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Prepends a link to the list.<br />
</td>
</tr>
<tr class="separator:gab3dd068e3bd8a319c0d12150785050a7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2dacb82db59f0012951d8245017473c9" class="memitem:ga2dacb82db59f0012951d8245017473c9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_insert_after (DBusList **list, DBusList *after_this_link, void *data)</td>
</tr>
<tr class="memdesc:ga2dacb82db59f0012951d8245017473c9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Inserts data into the list after the given existing link.<br />
</td>
</tr>
<tr class="separator:ga2dacb82db59f0012951d8245017473c9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0d1fde0acf1330cb41a9c290c7ae87b5" class="memitem:ga0d1fde0acf1330cb41a9c290c7ae87b5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_insert_before_link (DBusList **list, DBusList *before_this_link, DBusList *link)</td>
</tr>
<tr class="memdesc:ga0d1fde0acf1330cb41a9c290c7ae87b5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Inserts a link into the list before the given existing link.<br />
</td>
</tr>
<tr class="separator:ga0d1fde0acf1330cb41a9c290c7ae87b5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga20f6b11dd53979b94b6c4822ff6c1141" class="memitem:ga20f6b11dd53979b94b6c4822ff6c1141">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_insert_after_link (DBusList **list, DBusList *after_this_link, DBusList *link)</td>
</tr>
<tr class="memdesc:ga20f6b11dd53979b94b6c4822ff6c1141">
<td class="mdescLeft"> </td>
<td class="mdescRight">Inserts a link into the list after the given existing link.<br />
</td>
</tr>
<tr class="separator:ga20f6b11dd53979b94b6c4822ff6c1141">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga202e6ac8ad3e4a9d4413e0248ffcf3e3" class="memitem:ga202e6ac8ad3e4a9d4413e0248ffcf3e3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_remove (DBusList **list, void *data)</td>
</tr>
<tr class="memdesc:ga202e6ac8ad3e4a9d4413e0248ffcf3e3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a value from the list.<br />
</td>
</tr>
<tr class="separator:ga202e6ac8ad3e4a9d4413e0248ffcf3e3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad93f1fc853914144e94fc7a7dc0945aa" class="memitem:gad93f1fc853914144e94fc7a7dc0945aa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_remove_last (DBusList **list, void *data)</td>
</tr>
<tr class="memdesc:gad93f1fc853914144e94fc7a7dc0945aa">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a value from the list.<br />
</td>
</tr>
<tr class="separator:gad93f1fc853914144e94fc7a7dc0945aa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga59cb22eb98b8dbd3846cd0f40781431a" class="memitem:ga59cb22eb98b8dbd3846cd0f40781431a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_find_last (DBusList **list, void *data)</td>
</tr>
<tr class="memdesc:ga59cb22eb98b8dbd3846cd0f40781431a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Finds a value in the list.<br />
</td>
</tr>
<tr class="separator:ga59cb22eb98b8dbd3846cd0f40781431a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga57f1fc73dc1a4f8a7bf9860e000b1703" class="memitem:ga57f1fc73dc1a4f8a7bf9860e000b1703">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_unlink (DBusList **list, DBusList *link)</td>
</tr>
<tr class="memdesc:ga57f1fc73dc1a4f8a7bf9860e000b1703">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes the given link from the list, but doesn't free it.<br />
</td>
</tr>
<tr class="separator:ga57f1fc73dc1a4f8a7bf9860e000b1703">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga40abea762d9cb44e5ec6b31b1769dc2e" class="memitem:ga40abea762d9cb44e5ec6b31b1769dc2e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_remove_link (DBusList **list, DBusList *link)</td>
</tr>
<tr class="memdesc:ga40abea762d9cb44e5ec6b31b1769dc2e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a link from the list.<br />
</td>
</tr>
<tr class="separator:ga40abea762d9cb44e5ec6b31b1769dc2e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa36d13444a050a923941c53650b72f9d" class="memitem:gaa36d13444a050a923941c53650b72f9d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_clear (DBusList **list)</td>
</tr>
<tr class="memdesc:gaa36d13444a050a923941c53650b72f9d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees all links in the list and sets the list head to NULL.<br />
</td>
</tr>
<tr class="separator:gaa36d13444a050a923941c53650b72f9d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2992b7a9f9d7af283bdf59bc43b618a8" class="memitem:ga2992b7a9f9d7af283bdf59bc43b618a8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_clear_full (DBusList **list, DBusFreeFunction function)</td>
</tr>
<tr class="memdesc:ga2992b7a9f9d7af283bdf59bc43b618a8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Free every link and every element in the list.<br />
</td>
</tr>
<tr class="separator:ga2992b7a9f9d7af283bdf59bc43b618a8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga040637f412790611d9e988588f63875a" class="memitem:ga040637f412790611d9e988588f63875a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_get_first_link (DBusList **list)</td>
</tr>
<tr class="memdesc:ga040637f412790611d9e988588f63875a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the first link in the list.<br />
</td>
</tr>
<tr class="separator:ga040637f412790611d9e988588f63875a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4f70fa9d992f6b03a545ca0deba3f306" class="memitem:ga4f70fa9d992f6b03a545ca0deba3f306">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_get_last_link (DBusList **list)</td>
</tr>
<tr class="memdesc:ga4f70fa9d992f6b03a545ca0deba3f306">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the last link in the list.<br />
</td>
</tr>
<tr class="separator:ga4f70fa9d992f6b03a545ca0deba3f306">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1e7f35f4b11705a69d697a27691909ef" class="memitem:ga1e7f35f4b11705a69d697a27691909ef">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_get_last (DBusList **list)</td>
</tr>
<tr class="memdesc:ga1e7f35f4b11705a69d697a27691909ef">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the last data in the list.<br />
</td>
</tr>
<tr class="separator:ga1e7f35f4b11705a69d697a27691909ef">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4697877bc8b0a264df837dc91cf02d5a" class="memitem:ga4697877bc8b0a264df837dc91cf02d5a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_get_first (DBusList **list)</td>
</tr>
<tr class="memdesc:ga4697877bc8b0a264df837dc91cf02d5a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the first data in the list.<br />
</td>
</tr>
<tr class="separator:ga4697877bc8b0a264df837dc91cf02d5a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1cb03abb47b7c2df27a8fa4d98dbee5f" class="memitem:ga1cb03abb47b7c2df27a8fa4d98dbee5f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_pop_first_link (DBusList **list)</td>
</tr>
<tr class="memdesc:ga1cb03abb47b7c2df27a8fa4d98dbee5f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes the first link in the list and returns it.<br />
</td>
</tr>
<tr class="separator:ga1cb03abb47b7c2df27a8fa4d98dbee5f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6eb9d689c2c9a96c0a132334ecb39245" class="memitem:ga6eb9d689c2c9a96c0a132334ecb39245">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_pop_first (DBusList **list)</td>
</tr>
<tr class="memdesc:ga6eb9d689c2c9a96c0a132334ecb39245">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes the first value in the list and returns it.<br />
</td>
</tr>
<tr class="separator:ga6eb9d689c2c9a96c0a132334ecb39245">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6478afb3d8ff93eb604a25ce67bf29d1" class="memitem:ga6478afb3d8ff93eb604a25ce67bf29d1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_pop_last (DBusList **list)</td>
</tr>
<tr class="memdesc:ga6478afb3d8ff93eb604a25ce67bf29d1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes the last value in the list and returns it.<br />
</td>
</tr>
<tr class="separator:ga6478afb3d8ff93eb604a25ce67bf29d1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1a85785891866750c9438bc10ad0350a" class="memitem:ga1a85785891866750c9438bc10ad0350a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_copy (DBusList **list, DBusList **dest)</td>
</tr>
<tr class="memdesc:ga1a85785891866750c9438bc10ad0350a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Copies a list.<br />
</td>
</tr>
<tr class="separator:ga1a85785891866750c9438bc10ad0350a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa2144a5489bb35b16b2b671488ad597c" class="memitem:gaa2144a5489bb35b16b2b671488ad597c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_get_length (DBusList **list)</td>
</tr>
<tr class="memdesc:gaa2144a5489bb35b16b2b671488ad597c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the length of a list.<br />
</td>
</tr>
<tr class="separator:gaa2144a5489bb35b16b2b671488ad597c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8dd69084b53361803a765e6d53d5b9d1" class="memitem:ga8dd69084b53361803a765e6d53d5b9d1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_foreach (DBusList **list, DBusForeachFunction function, void *data)</td>
</tr>
<tr class="memdesc:ga8dd69084b53361803a765e6d53d5b9d1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Calls the given function for each element in the list.<br />
</td>
</tr>
<tr class="separator:ga8dd69084b53361803a765e6d53d5b9d1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1d0e850f8e151630fa94d3b05e6038d9" class="memitem:ga1d0e850f8e151630fa94d3b05e6038d9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_list_length_is_one (DBusList **list)</td>
</tr>
<tr class="memdesc:ga1d0e850f8e151630fa94d3b05e6038d9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check whether length is exactly one.<br />
</td>
</tr>
<tr class="separator:ga1d0e850f8e151630fa94d3b05e6038d9">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusList data structure.

Types and functions related to DBusList.

## Macro Definition Documentation

## ◆ \_dbus_list_get_next_link

|  |  |  |  |
|----|----|----|----|
| \#define \_dbus_list_get_next_link | ( |   | list, |
|  |  |   | link  |
|  | ) |  |    ((link)-\>next == \*(list) ? NULL : (link)-\>next) |

Gets the next link in the list, or NULL if there are no more links.

Used for iteration.

DBusList \*link;

link = \_dbus_list_get_first_link (&list);

while (link != NULL)

{

printf ("value is %p\n", link-\>data);

link = \_dbus_list_get_next_link (&link);

}

\_dbus_list_get_first_link

DBusList \* \_dbus_list_get_first_link(DBusList \*\*list)

Gets the first link in the list.

**Definition** dbus-list.c:597

\_dbus_list_get_next_link

\#define \_dbus_list_get_next_link(list, link)

Gets the next link in the list, or NULL if there are no more links.

**Definition** dbus-list.h:121

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

DBusList

A node in a linked list.

**Definition** dbus-list.h:37

DBusList::data

void \* data

Data stored at this element.

**Definition** dbus-list.h:40

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |
| link | current link.             |

<!-- -->

Returns  
the next link, or NULL if none.

Definition at line 121 of file dbus-list.h.

## ◆ \_dbus_list_get_prev_link

|  |  |  |  |
|----|----|----|----|
| \#define \_dbus_list_get_prev_link | ( |   | list, |
|  |  |   | link  |
|  | ) |  |    ((link) == \*(list) ? NULL : (link)-\>prev) |

Gets the previous link in the list, or NULL if there are no more links.

Used for iteration.

DBusList \*link;

link = \_dbus_list_get_last_link (&list);

while (link != NULL)

{

printf ("value is %p\n", link-\>data);

link = \_dbus_list_get_prev_link (&link);

}

\_dbus_list_get_last_link

DBusList \* \_dbus_list_get_last_link(DBusList \*\*list)

Gets the last link in the list.

**Definition** dbus-list.c:610

\_dbus_list_get_prev_link

\#define \_dbus_list_get_prev_link(list, link)

Gets the previous link in the list, or NULL if there are no more links.

**Definition** dbus-list.h:122

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |
| link | current link.             |

<!-- -->

Returns  
the previous link, or NULL if none.

Definition at line 122 of file dbus-list.h.

## Function Documentation

## ◆ \_dbus_list_alloc_link()

|                                    |     |          |        |     |     |
|------------------------------------|-----|----------|--------|-----|-----|
| DBusList \* \_dbus_list_alloc_link | (   | void \*  | *data* | )   |     |

Allocates a linked list node.

Useful for preallocating nodes and using \_dbus_list_append_link() to avoid allocations.

Parameters  
|      |                                 |
|------|---------------------------------|
| data | the value to store in the link. |

<!-- -->

Returns  
a newly allocated link.

Definition at line 245 of file dbus-list.c.

Referenced by \_dbus_connection_new_for_transport(), \_dbus_message_add_counter(), \_dbus_pending_call_set_timeout_error_unlocked(), and dbus_connection_dispatch().

## ◆ \_dbus_list_append()

|                                |     |                |         |
|--------------------------------|-----|----------------|---------|
| dbus_bool_t \_dbus_list_append | (   | DBusList \*\*  | *list*, |
|                                |     | void \*        | *data*  |
|                                | )   |                |         |

Appends a value to the list.

May return FALSE if insufficient memory exists to add a list link. This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |
| data | the value to append.      |

<!-- -->

Returns  
TRUE on success.

Definition at line 273 of file dbus-list.c.

References \_dbus_list_prepend(), FALSE, next, and TRUE.

Referenced by \_dbus_list_copy(), \_dbus_listen_tcp_socket(), \_dbus_object_tree_dispatch_and_unlock(), \_dbus_set_up_transient_session_servicedirs(), \_dbus_split_paths_and_append(), \_dbus_timeout_list_add_timeout(), \_dbus_validate_signature_with_reason(), \_dbus_watch_list_add_watch(), dbus_connection_add_filter(), and dbus_parse_address().

## ◆ \_dbus_list_append_link()

|                              |     |                |         |
|------------------------------|-----|----------------|---------|
| void \_dbus_list_append_link | (   | DBusList \*\*  | *list*, |
|                              |     | DBusList \*    | *link*  |
|                              | )   |                |         |

Appends a link to the list.

Cannot fail due to out of memory. This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |
| link | the link to append.       |

Definition at line 318 of file dbus-list.c.

References \_dbus_list_prepend_link(), and next.

Referenced by \_dbus_connection_queue_received_message_link(), \_dbus_connection_queue_synthesized_message_link(), \_dbus_list_insert_before_link(), and \_dbus_message_add_counter_link().

## ◆ \_dbus_list_clear()

|                        |     |                |        |     |     |
|------------------------|-----|----------------|--------|-----|-----|
| void \_dbus_list_clear | (   | DBusList \*\*  | *list* | )   |     |

Frees all links in the list and sets the list head to NULL.

Does not free the data in each link, for obvious reasons. This is a linear-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |

Definition at line 545 of file dbus-list.c.

References \_dbus_list_get_next_link, and NULL.

Referenced by \_dbus_auth_unref(), \_dbus_list_copy(), \_dbus_pending_call_set_reply_unlocked(), \_dbus_validate_signature_with_reason(), and dbus_parse_address().

## ◆ \_dbus_list_clear_full()

|                             |     |                   |             |
|-----------------------------|-----|-------------------|-------------|
| void \_dbus_list_clear_full | (   | DBusList \*\*     | *list*,     |
|                             |     | DBusFreeFunction  | *function*  |
|                             | )   |                   |             |

Free every link and every element in the list.

Parameters  
|          |                                         |
|----------|-----------------------------------------|
| list     | address of the head of the list.        |
| function | free-function to call for each element. |

Definition at line 570 of file dbus-list.c.

References \_dbus_list_get_next_link, data, and NULL.

Referenced by \_dbus_message_loader_unref(), \_dbus_split_paths_and_append(), \_dbus_timeout_list_free(), \_dbus_watch_list_free(), and dbus_connection_dispatch().

## ◆ \_dbus_list_copy()

|                              |     |                |         |
|------------------------------|-----|----------------|---------|
| dbus_bool_t \_dbus_list_copy | (   | DBusList \*\*  | *list*, |
|                              |     | DBusList \*\*  | *dest*  |
|                              | )   |                |         |

Copies a list.

This is a linear-time operation. If there isn't enough memory to copy the entire list, the destination list will be set to NULL.

Parameters  
|      |                                                 |
|------|-------------------------------------------------|
| list | address of the head of the list to copy.        |
| dest | address where the copied list should be placed. |

<!-- -->

Returns  
TRUE on success, FALSE if not enough memory.

Definition at line 727 of file dbus-list.c.

References \_dbus_assert, \_dbus_list_append(), \_dbus_list_clear(), \_dbus_list_get_next_link, data, FALSE, NULL, and TRUE.

Referenced by dbus_connection_dispatch().

## ◆ \_dbus_list_find_last()

|                                   |     |                |         |
|-----------------------------------|-----|----------------|---------|
| DBusList \* \_dbus_list_find_last | (   | DBusList \*\*  | *list*, |
|                                   |     | void \*        | *data*  |
|                                   | )   |                |         |

Finds a value in the list.

Returns the last link with value equal to the given data pointer. This is a linear-time operation. Returns NULL if no value found that matches.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |
| data | the value to find.        |

<!-- -->

Returns  
the link if found

Definition at line 475 of file dbus-list.c.

References \_dbus_list_get_last_link(), \_dbus_list_get_prev_link, data, and NULL.

Referenced by \_dbus_list_remove_last(), \_dbus_message_loader_queue_messages(), and \_dbus_message_remove_counter().

## ◆ \_dbus_list_foreach()

|                          |     |                      |             |
|--------------------------|-----|----------------------|-------------|
| void \_dbus_list_foreach | (   | DBusList \*\*        | *list*,     |
|                          |     | DBusForeachFunction  | *function*, |
|                          |     | void \*              | *data*      |
|                          | )   |                      |             |

Calls the given function for each element in the list.

The function is passed the list element as its first argument, and the given data as its second argument.

Parameters  
|          |                                    |
|----------|------------------------------------|
| list     | address of the head of the list.   |
| function | function to call for each element. |
| data     | extra data for the function.       |

Definition at line 789 of file dbus-list.c.

References \_dbus_list_get_next_link, data, and NULL.

Referenced by \_dbus_timeout_list_set_functions(), and \_dbus_watch_list_set_functions().

## ◆ \_dbus_list_free_link()

|                            |     |              |        |     |     |
|----------------------------|-----|--------------|--------|-----|-----|
| void \_dbus_list_free_link | (   | DBusList \*  | *link* | )   |     |

Frees a linked list node allocated with \_dbus_list_alloc_link.

Does not free the data in the node.

Parameters  
|      |               |
|------|---------------|
| link | the list node |

Definition at line 257 of file dbus-list.c.

Referenced by \_dbus_connection_new_for_transport(), \_dbus_connection_unlock(), dbus_connection_dispatch(), and dbus_connection_free_preallocated_send().

## ◆ \_dbus_list_get_first()

|                               |     |                |        |     |     |
|-------------------------------|-----|----------------|--------|-----|-----|
| void \* \_dbus_list_get_first | (   | DBusList \*\*  | *list* | )   |     |

Gets the first data in the list.

This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |

<!-- -->

Returns  
the first data in the list, or NULL for an empty list.

Definition at line 642 of file dbus-list.c.

References NULL.

Referenced by dbus_connection_borrow_message().

## ◆ \_dbus_list_get_first_link()

|                                        |     |                |        |     |     |
|----------------------------------------|-----|----------------|--------|-----|-----|
| DBusList \* \_dbus_list_get_first_link | (   | DBusList \*\*  | *list* | )   |     |

Gets the first link in the list.

This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |

<!-- -->

Returns  
the first link, or NULL for an empty list.

Definition at line 597 of file dbus-list.c.

Referenced by \_dbus_list_pop_first(), \_dbus_list_pop_first_link(), \_dbus_object_tree_dispatch_and_unlock(), \_dbus_timeout_list_set_functions(), \_dbus_watch_list_set_functions(), \_dbus_watch_list_toggle_all_watches(), dbus_address_entry_get_value(), dbus_connection_dispatch(), and dbus_parse_address().

## ◆ \_dbus_list_get_last()

|                              |     |                |        |     |     |
|------------------------------|-----|----------------|--------|-----|-----|
| void \* \_dbus_list_get_last | (   | DBusList \*\*  | *list* | )   |     |

Gets the last data in the list.

This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |

<!-- -->

Returns  
the last data in the list, or NULL for an empty list.

Definition at line 626 of file dbus-list.c.

References NULL.

Referenced by \_dbus_connection_get_message_to_send().

## ◆ \_dbus_list_get_last_link()

|                                       |     |                |        |     |     |
|---------------------------------------|-----|----------------|--------|-----|-----|
| DBusList \* \_dbus_list_get_last_link | (   | DBusList \*\*  | *list* | )   |     |

Gets the last link in the list.

This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |

<!-- -->

Returns  
the last link, or NULL for an empty list.

Definition at line 610 of file dbus-list.c.

References NULL, and prev.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_list_find_last(), \_dbus_list_pop_last(), and dbus_connection_remove_filter().

## ◆ \_dbus_list_get_length()

|                            |     |                |        |     |     |
|----------------------------|-----|----------------|--------|-----|-----|
| int \_dbus_list_get_length | (   | DBusList \*\*  | *list* | )   |     |

Gets the length of a list.

This is a linear-time operation.

Parameters  
|      |                                 |
|------|---------------------------------|
| list | address of the head of the list |

<!-- -->

Returns  
number of elements in the list.

Definition at line 760 of file dbus-list.c.

References \_dbus_list_get_next_link, and NULL.

Referenced by \_dbus_object_tree_dispatch_and_unlock(), and dbus_parse_address().

## ◆ \_dbus_list_insert_after()

|                                      |     |                |                    |
|--------------------------------------|-----|----------------|--------------------|
| dbus_bool_t \_dbus_list_insert_after | (   | DBusList \*\*  | *list*,            |
|                                      |     | DBusList \*    | *after_this_link*, |
|                                      |     | void \*        | *data*             |
|                                      | )   |                |                    |

Inserts data into the list after the given existing link.

Parameters  
|                 |                                                   |
|-----------------|---------------------------------------------------|
| list            | the list to modify                                |
| after_this_link | existing link to insert after, or NULL to prepend |
| data            | the value to insert                               |

<!-- -->

Returns  
TRUE on success, FALSE if memory allocation fails

Definition at line 351 of file dbus-list.c.

References \_dbus_list_prepend(), FALSE, NULL, and TRUE.

## ◆ \_dbus_list_insert_after_link()

|                                    |     |                |                    |
|------------------------------------|-----|----------------|--------------------|
| void \_dbus_list_insert_after_link | (   | DBusList \*\*  | *list*,            |
|                                    |     | DBusList \*    | *after_this_link*, |
|                                    |     | DBusList \*    | *link*             |
|                                    | )   |                |                    |

Inserts a link into the list after the given existing link.

Parameters  
|                 |                                                   |
|-----------------|---------------------------------------------------|
| list            | the list to modify                                |
| after_this_link | existing link to insert after, or NULL to prepend |
| link            | the link to insert                                |

Definition at line 397 of file dbus-list.c.

References \_dbus_list_prepend_link(), and NULL.

## ◆ \_dbus_list_insert_before_link()

|                                     |     |                |                     |
|-------------------------------------|-----|----------------|---------------------|
| void \_dbus_list_insert_before_link | (   | DBusList \*\*  | *list*,             |
|                                     |     | DBusList \*    | *before_this_link*, |
|                                     |     | DBusList \*    | *link*              |
|                                     | )   |                |                     |

Inserts a link into the list before the given existing link.

Parameters  
|                  |                                                   |
|------------------|---------------------------------------------------|
| list             | the list to modify                                |
| before_this_link | existing link to insert before, or NULL to append |
| link             | the link to insert                                |

Definition at line 379 of file dbus-list.c.

References \_dbus_list_append_link(), and NULL.

## ◆ \_dbus_list_length_is_one()

|                                       |     |                |        |     |     |
|---------------------------------------|-----|----------------|--------|-----|-----|
| dbus_bool_t \_dbus_list_length_is_one | (   | DBusList \*\*  | *list* | )   |     |

Check whether length is exactly one.

Parameters  
|      |          |
|------|----------|
| list | the list |

<!-- -->

Returns  
TRUE if length is exactly one

Definition at line 813 of file dbus-list.c.

References next, and NULL.

## ◆ \_dbus_list_pop_first()

|                               |     |                |        |     |     |
|-------------------------------|-----|----------------|--------|-----|-----|
| void \* \_dbus_list_pop_first | (   | DBusList \*\*  | *list* | )   |     |

Removes the first value in the list and returns it.

This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |

<!-- -->

Returns  
the first data in the list, or NULL for an empty list.

Definition at line 679 of file dbus-list.c.

References \_dbus_list_get_first_link(), \_dbus_list_remove_link(), data, and NULL.

Referenced by \_dbus_listen_tcp_socket(), \_dbus_message_loader_pop_message(), and dbus_connection_steal_borrowed_message().

## ◆ \_dbus_list_pop_first_link()

|                                        |     |                |        |     |     |
|----------------------------------------|-----|----------------|--------|-----|-----|
| DBusList \* \_dbus_list_pop_first_link | (   | DBusList \*\*  | *list* | )   |     |

Removes the first link in the list and returns it.

This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |

<!-- -->

Returns  
the first link in the list, or NULL for an empty list.

Definition at line 658 of file dbus-list.c.

References \_dbus_list_get_first_link(), \_dbus_list_unlink(), and NULL.

Referenced by \_dbus_connection_unlock(), and \_dbus_message_loader_pop_message_link().

## ◆ \_dbus_list_pop_last()

|                              |     |                |        |     |     |
|------------------------------|-----|----------------|--------|-----|-----|
| void \* \_dbus_list_pop_last | (   | DBusList \*\*  | *list* | )   |     |

Removes the last value in the list and returns it.

This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |

<!-- -->

Returns  
the last data in the list, or NULL for an empty list.

Definition at line 702 of file dbus-list.c.

References \_dbus_list_get_last_link(), \_dbus_list_remove_link(), data, and NULL.

Referenced by \_dbus_validate_signature_with_reason().

## ◆ \_dbus_list_prepend()

|                                 |     |                |         |
|---------------------------------|-----|----------------|---------|
| dbus_bool_t \_dbus_list_prepend | (   | DBusList \*\*  | *list*, |
|                                 |     | void \*        | *data*  |
|                                 | )   |                |         |

Prepends a value to the list.

May return FALSE if insufficient memory exists to add a list link. This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |
| data | the value to prepend.     |

<!-- -->

Returns  
TRUE on success.

Definition at line 295 of file dbus-list.c.

References FALSE, NULL, and TRUE.

Referenced by \_dbus_list_append(), and \_dbus_list_insert_after().

## ◆ \_dbus_list_prepend_link()

|                               |     |                |         |
|-------------------------------|-----|----------------|---------|
| void \_dbus_list_prepend_link | (   | DBusList \*\*  | *list*, |
|                               |     | DBusList \*    | *link*  |
|                               | )   |                |         |

Prepends a link to the list.

Cannot fail due to out of memory. This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |
| link | the link to prepend.      |

Definition at line 336 of file dbus-list.c.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_list_append_link(), \_dbus_list_insert_after_link(), \_dbus_message_loader_putback_message_link(), and dbus_connection_dispatch().

## ◆ \_dbus_list_remove()

|                                |     |                |         |
|--------------------------------|-----|----------------|---------|
| dbus_bool_t \_dbus_list_remove | (   | DBusList \*\*  | *list*, |
|                                |     | void \*        | *data*  |
|                                | )   |                |         |

Removes a value from the list.

Only removes the first value equal to the given data pointer, even if multiple values exist which match. This is a linear-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |
| data | the value to remove.      |

<!-- -->

Returns  
TRUE if a value was found to remove.

Definition at line 418 of file dbus-list.c.

References \_dbus_list_get_next_link, \_dbus_list_remove_link(), data, FALSE, NULL, and TRUE.

Referenced by \_dbus_timeout_list_remove_timeout(), and \_dbus_watch_list_remove_watch().

## ◆ \_dbus_list_remove_last()

|                                     |     |                |         |
|-------------------------------------|-----|----------------|---------|
| dbus_bool_t \_dbus_list_remove_last | (   | DBusList \*\*  | *list*, |
|                                     |     | void \*        | *data*  |
|                                     | )   |                |         |

Removes a value from the list.

Only removes the last value equal to the given data pointer, even if multiple values exist which match. This is a linear-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |
| data | the value to remove.      |

<!-- -->

Returns  
TRUE if a value was found to remove.

Definition at line 449 of file dbus-list.c.

References \_dbus_list_find_last(), \_dbus_list_remove_link(), FALSE, and TRUE.

Referenced by \_dbus_timeout_list_add_timeout(), and \_dbus_watch_list_add_watch().

## ◆ \_dbus_list_remove_link()

|                              |     |                |         |
|------------------------------|-----|----------------|---------|
| void \_dbus_list_remove_link | (   | DBusList \*\*  | *list*, |
|                              |     | DBusList \*    | *link*  |
|                              | )   |                |         |

Removes a link from the list.

This is a constant-time operation.

Parameters  
|      |                           |
|------|---------------------------|
| list | address of the list head. |
| link | the list link to remove.  |

Definition at line 530 of file dbus-list.c.

References \_dbus_list_unlink().

Referenced by \_dbus_list_pop_first(), \_dbus_list_pop_last(), \_dbus_list_remove(), \_dbus_list_remove_last(), \_dbus_message_remove_counter(), \_dbus_object_tree_dispatch_and_unlock(), and dbus_connection_remove_filter().

## ◆ \_dbus_list_unlink()

|                         |     |                |         |
|-------------------------|-----|----------------|---------|
| void \_dbus_list_unlink | (   | DBusList \*\*  | *list*, |
|                         |     | DBusList \*    | *link*  |
|                         | )   |                |         |

Removes the given link from the list, but doesn't free it.

\_dbus_list_remove_link() both removes the link and also frees it.

Parameters  
|      |                      |
|------|----------------------|
| list | the list             |
| link | the link in the list |

Definition at line 502 of file dbus-list.c.

References next, NULL, and prev.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_list_pop_first_link(), and \_dbus_list_remove_link().
