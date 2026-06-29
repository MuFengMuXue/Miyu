DBusString class

D-Bus secret internal implementation details

DBusString data structure for safer string handling. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_gaacbbd102b66aa34dd13f792e7f08c205" class="memitem:gaacbbd102b66aa34dd13f792e7f08c205">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_STRING_COPY_PREAMBLE(source, start, dest, insert_at)</td>
</tr>
<tr class="memdesc:gaacbbd102b66aa34dd13f792e7f08c205">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks assertions for two strings we're copying a segment between, and declares real_source/real_dest variables.<br />
</td>
</tr>
<tr class="separator:gaacbbd102b66aa34dd13f792e7f08c205">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga30614080229a4fb63460ffdc8ab484fb" class="memitem:ga30614080229a4fb63460ffdc8ab484fb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">UTF8_COMPUTE(Char, Mask, Len)</td>
</tr>
<tr class="memdesc:ga30614080229a4fb63460ffdc8ab484fb">
<td class="mdescLeft"> </td>
<td class="mdescRight">computes length and mask of a unicode character<br />
</td>
</tr>
<tr class="separator:ga30614080229a4fb63460ffdc8ab484fb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9691ff5386e218870299de1d9e77ceea" class="memitem:ga9691ff5386e218870299de1d9e77ceea">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">UTF8_LENGTH(Char)</td>
</tr>
<tr class="memdesc:ga9691ff5386e218870299de1d9e77ceea">
<td class="mdescLeft"> </td>
<td class="mdescRight">computes length of a unicode character in UTF-8<br />
</td>
</tr>
<tr class="separator:ga9691ff5386e218870299de1d9e77ceea">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab5b4b316a69f78611a14e6b1fd091992" class="memitem:gab5b4b316a69f78611a14e6b1fd091992">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">UTF8_GET(Result, Chars, Count, Mask, Len)</td>
</tr>
<tr class="memdesc:gab5b4b316a69f78611a14e6b1fd091992">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets a UTF-8 value.<br />
</td>
</tr>
<tr class="separator:gab5b4b316a69f78611a14e6b1fd091992">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga25f0a93fc023fa0eec07ac1e32011e89" class="memitem:ga25f0a93fc023fa0eec07ac1e32011e89">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">UNICODE_VALID(Char)</td>
</tr>
<tr class="memdesc:ga25f0a93fc023fa0eec07ac1e32011e89">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check whether a Unicode (5.2) char is in a valid range.<br />
</td>
</tr>
<tr class="separator:ga25f0a93fc023fa0eec07ac1e32011e89">
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
<tr id="r_ga4701fa3fabccad3ba64b7bf17c4ae14c" class="memitem:ga4701fa3fabccad3ba64b7bf17c4ae14c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_ends_with_c_str (const DBusString *a, const char *c_str)</td>
</tr>
<tr class="memdesc:ga4701fa3fabccad3ba64b7bf17c4ae14c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns whether a string ends with the given suffix.<br />
</td>
</tr>
<tr class="separator:ga4701fa3fabccad3ba64b7bf17c4ae14c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga89d458f4f530ee82dbb45f9dcbc9c637" class="memitem:ga89d458f4f530ee82dbb45f9dcbc9c637">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_find_byte_backward (const DBusString *str, int start, unsigned char byte, int *found)</td>
</tr>
<tr class="memdesc:ga89d458f4f530ee82dbb45f9dcbc9c637">
<td class="mdescLeft"> </td>
<td class="mdescRight">Find the given byte scanning backward from the given start.<br />
</td>
</tr>
<tr class="separator:ga89d458f4f530ee82dbb45f9dcbc9c637">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga569b784beea1b4fa98f05d27e6dd0e72" class="memitem:ga569b784beea1b4fa98f05d27e6dd0e72">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_init_preallocated (DBusString *str, int allocate_size)</td>
</tr>
<tr class="memdesc:ga569b784beea1b4fa98f05d27e6dd0e72">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a string that can be up to the given allocation size before it has to realloc.<br />
</td>
</tr>
<tr class="separator:ga569b784beea1b4fa98f05d27e6dd0e72">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga348252317f7bb8ac43529972945830ae" class="memitem:ga348252317f7bb8ac43529972945830ae">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_init (DBusString *str)</td>
</tr>
<tr class="memdesc:ga348252317f7bb8ac43529972945830ae">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a string.<br />
</td>
</tr>
<tr class="separator:ga348252317f7bb8ac43529972945830ae">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga374640ddfa2f0b27a8356e2379ba8043" class="memitem:ga374640ddfa2f0b27a8356e2379ba8043">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_init_const (DBusString *str, const char *value)</td>
</tr>
<tr class="memdesc:ga374640ddfa2f0b27a8356e2379ba8043">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a constant string.<br />
</td>
</tr>
<tr class="separator:ga374640ddfa2f0b27a8356e2379ba8043">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6792a5c1725faa9d635d95f7a3b5bfae" class="memitem:ga6792a5c1725faa9d635d95f7a3b5bfae">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_init_const_len (DBusString *str, const char *value, int len)</td>
</tr>
<tr class="memdesc:ga6792a5c1725faa9d635d95f7a3b5bfae">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a constant string with a length.<br />
</td>
</tr>
<tr class="separator:ga6792a5c1725faa9d635d95f7a3b5bfae">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5c5faea5fac79aad0de9fb1cf6da0393" class="memitem:ga5c5faea5fac79aad0de9fb1cf6da0393">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_init_from_string (DBusString *str, const DBusString *from)</td>
</tr>
<tr class="memdesc:ga5c5faea5fac79aad0de9fb1cf6da0393">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a string from another string.<br />
</td>
</tr>
<tr class="separator:ga5c5faea5fac79aad0de9fb1cf6da0393">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga781ca91acda49a834dce7d0ed0eef212" class="memitem:ga781ca91acda49a834dce7d0ed0eef212">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_free (DBusString *str)</td>
</tr>
<tr class="memdesc:ga781ca91acda49a834dce7d0ed0eef212">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees a string created by _dbus_string_init(), and fills it with the same contents as _DBUS_STRING_INIT_INVALID.<br />
</td>
</tr>
<tr class="separator:ga781ca91acda49a834dce7d0ed0eef212">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac49ec5782ca606029c096124b5e43ffc" class="memitem:gac49ec5782ca606029c096124b5e43ffc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_compact (DBusString *str, int max_waste)</td>
</tr>
<tr class="memdesc:gac49ec5782ca606029c096124b5e43ffc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Compacts the string to avoid wasted memory.<br />
</td>
</tr>
<tr class="separator:gac49ec5782ca606029c096124b5e43ffc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac19368c67f90be0850525d3e2fcabe22" class="memitem:gac19368c67f90be0850525d3e2fcabe22">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_get_allocated_size (const DBusString *str)</td>
</tr>
<tr class="memdesc:gac19368c67f90be0850525d3e2fcabe22">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the allocated size of the string.<br />
</td>
</tr>
<tr class="separator:gac19368c67f90be0850525d3e2fcabe22">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga75877b21c801913cf47c9547eceeb31f" class="memitem:ga75877b21c801913cf47c9547eceeb31f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_get_data (DBusString *str)</td>
</tr>
<tr class="memdesc:ga75877b21c801913cf47c9547eceeb31f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the raw character buffer from the string.<br />
</td>
</tr>
<tr class="separator:ga75877b21c801913cf47c9547eceeb31f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac173778f3b28e130209b4bd77a819307" class="memitem:gac173778f3b28e130209b4bd77a819307">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_get_const_data (const DBusString *str)</td>
</tr>
<tr class="memdesc:gac173778f3b28e130209b4bd77a819307">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the raw character buffer from a const string.<br />
</td>
</tr>
<tr class="separator:gac173778f3b28e130209b4bd77a819307">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga631229603797a2ce68a597d05ebf55ab" class="memitem:ga631229603797a2ce68a597d05ebf55ab">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_get_data_len (DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga631229603797a2ce68a597d05ebf55ab">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets a sub-portion of the raw character buffer from the string.<br />
</td>
</tr>
<tr class="separator:ga631229603797a2ce68a597d05ebf55ab">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab5c9f831782e39c8e8c77b91d452352c" class="memitem:gab5c9f831782e39c8e8c77b91d452352c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_get_const_data_len (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:gab5c9f831782e39c8e8c77b91d452352c">
<td class="mdescLeft"> </td>
<td class="mdescRight">const version of _dbus_string_get_data_len().<br />
</td>
</tr>
<tr class="separator:gab5c9f831782e39c8e8c77b91d452352c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab6c823e9406208363fcb5e96d580e738" class="memitem:gab6c823e9406208363fcb5e96d580e738">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_set_byte (DBusString *str, int i, unsigned char byte)</td>
</tr>
<tr class="memdesc:gab6c823e9406208363fcb5e96d580e738">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the value of the byte at the given position.<br />
</td>
</tr>
<tr class="separator:gab6c823e9406208363fcb5e96d580e738">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac1cb7b207eac3c6527a5d42fbc5449b1" class="memitem:gac1cb7b207eac3c6527a5d42fbc5449b1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned char </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_get_byte (const DBusString *str, int start)</td>
</tr>
<tr class="memdesc:gac1cb7b207eac3c6527a5d42fbc5449b1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the byte at the given position.<br />
</td>
</tr>
<tr class="separator:gac1cb7b207eac3c6527a5d42fbc5449b1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa0964d662ad17c58eb044c1b153017a6" class="memitem:gaa0964d662ad17c58eb044c1b153017a6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_insert_bytes (DBusString *str, int i, int n_bytes, unsigned char byte)</td>
</tr>
<tr class="memdesc:gaa0964d662ad17c58eb044c1b153017a6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Inserts a number of bytes of a given value at the given position.<br />
</td>
</tr>
<tr class="separator:gaa0964d662ad17c58eb044c1b153017a6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab0770800dce6df97e5d246105a44e7b4" class="memitem:gab0770800dce6df97e5d246105a44e7b4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_insert_byte (DBusString *str, int i, unsigned char byte)</td>
</tr>
<tr class="memdesc:gab0770800dce6df97e5d246105a44e7b4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Inserts a single byte at the given position.<br />
</td>
</tr>
<tr class="separator:gab0770800dce6df97e5d246105a44e7b4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga556cc30c3ab032dbc63e217119f0d1f5" class="memitem:ga556cc30c3ab032dbc63e217119f0d1f5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_steal_data (DBusString *str, char **data_return)</td>
</tr>
<tr class="memdesc:ga556cc30c3ab032dbc63e217119f0d1f5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_string_get_data(), but removes the gotten data from the original string.<br />
</td>
</tr>
<tr class="separator:ga556cc30c3ab032dbc63e217119f0d1f5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7e509d4f959d19d96f83250e62287b06" class="memitem:ga7e509d4f959d19d96f83250e62287b06">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_copy_data (const DBusString *str, char **data_return)</td>
</tr>
<tr class="memdesc:ga7e509d4f959d19d96f83250e62287b06">
<td class="mdescLeft"> </td>
<td class="mdescRight">Copies the data from the string into a char*.<br />
</td>
</tr>
<tr class="separator:ga7e509d4f959d19d96f83250e62287b06">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf97b18e419678dbf967d9b9ad1112ca6" class="memitem:gaf97b18e419678dbf967d9b9ad1112ca6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_copy_to_buffer (const DBusString *str, char *buffer, int avail_len)</td>
</tr>
<tr class="memdesc:gaf97b18e419678dbf967d9b9ad1112ca6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Copies the contents of a DBusString into a different buffer.<br />
</td>
</tr>
<tr class="separator:gaf97b18e419678dbf967d9b9ad1112ca6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac42891d26084a4da0f63038d93b63828" class="memitem:gac42891d26084a4da0f63038d93b63828">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_copy_to_buffer_with_nul (const DBusString *str, char *buffer, int avail_len)</td>
</tr>
<tr class="memdesc:gac42891d26084a4da0f63038d93b63828">
<td class="mdescLeft"> </td>
<td class="mdescRight">Copies the contents of a DBusString into a different buffer.<br />
</td>
</tr>
<tr class="separator:gac42891d26084a4da0f63038d93b63828">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa5136e6fd2c5188f4b88de7863369c6d" class="memitem:gaa5136e6fd2c5188f4b88de7863369c6d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_get_length (const DBusString *str)</td>
</tr>
<tr class="memdesc:gaa5136e6fd2c5188f4b88de7863369c6d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the length of a string (not including nul termination).<br />
</td>
</tr>
<tr class="separator:gaa5136e6fd2c5188f4b88de7863369c6d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8f13997d90ceed2f437706e6b7804d9b" class="memitem:ga8f13997d90ceed2f437706e6b7804d9b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_lengthen (DBusString *str, int additional_length)</td>
</tr>
<tr class="memdesc:ga8f13997d90ceed2f437706e6b7804d9b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Makes a string longer by the given number of bytes.<br />
</td>
</tr>
<tr class="separator:ga8f13997d90ceed2f437706e6b7804d9b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7af1cbfa905f26d972ab644d890548b8" class="memitem:ga7af1cbfa905f26d972ab644d890548b8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_shorten (DBusString *str, int length_to_remove)</td>
</tr>
<tr class="memdesc:ga7af1cbfa905f26d972ab644d890548b8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Makes a string shorter by the given number of bytes.<br />
</td>
</tr>
<tr class="separator:ga7af1cbfa905f26d972ab644d890548b8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga08c423b93c28dd746dcb93e0461ab95c" class="memitem:ga08c423b93c28dd746dcb93e0461ab95c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_set_length (DBusString *str, int length)</td>
</tr>
<tr class="memdesc:ga08c423b93c28dd746dcb93e0461ab95c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the length of a string.<br />
</td>
</tr>
<tr class="separator:ga08c423b93c28dd746dcb93e0461ab95c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaeadfb67c4e796131610499c91d0d7813" class="memitem:gaeadfb67c4e796131610499c91d0d7813">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_align_length (DBusString *str, int alignment)</td>
</tr>
<tr class="memdesc:gaeadfb67c4e796131610499c91d0d7813">
<td class="mdescLeft"> </td>
<td class="mdescRight">Align the length of a string to a specific alignment (typically 4 or 8) by appending nul bytes to the string.<br />
</td>
</tr>
<tr class="separator:gaeadfb67c4e796131610499c91d0d7813">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4764e75c464356408fc1a12df93177c1" class="memitem:ga4764e75c464356408fc1a12df93177c1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_alloc_space (DBusString *str, int extra_bytes)</td>
</tr>
<tr class="memdesc:ga4764e75c464356408fc1a12df93177c1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Preallocate extra_bytes such that a future lengthening of the string by extra_bytes is guaranteed to succeed without an out of memory error.<br />
</td>
</tr>
<tr class="separator:ga4764e75c464356408fc1a12df93177c1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga100c5ce0696822c5a4cfbdfaba674d96" class="memitem:ga100c5ce0696822c5a4cfbdfaba674d96">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_append (DBusString *str, const char *buffer)</td>
</tr>
<tr class="memdesc:ga100c5ce0696822c5a4cfbdfaba674d96">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends a nul-terminated C-style string to a DBusString.<br />
</td>
</tr>
<tr class="separator:ga100c5ce0696822c5a4cfbdfaba674d96">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae7770fdabda32f3e8d9dd50b083dbf1e" class="memitem:gae7770fdabda32f3e8d9dd50b083dbf1e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_insert_2_aligned (DBusString *str, int insert_at, const unsigned char octets[2])</td>
</tr>
<tr class="memdesc:gae7770fdabda32f3e8d9dd50b083dbf1e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Inserts 2 bytes aligned on a 2 byte boundary with any alignment padding initialized to 0.<br />
</td>
</tr>
<tr class="separator:gae7770fdabda32f3e8d9dd50b083dbf1e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadd296cf1e6af18cb5bec438e9d353b4e" class="memitem:gadd296cf1e6af18cb5bec438e9d353b4e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_insert_4_aligned (DBusString *str, int insert_at, const unsigned char octets[4])</td>
</tr>
<tr class="memdesc:gadd296cf1e6af18cb5bec438e9d353b4e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Inserts 4 bytes aligned on a 4 byte boundary with any alignment padding initialized to 0.<br />
</td>
</tr>
<tr class="separator:gadd296cf1e6af18cb5bec438e9d353b4e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga108d7d64fb88fffca31e33181cefa232" class="memitem:ga108d7d64fb88fffca31e33181cefa232">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_insert_8_aligned (DBusString *str, int insert_at, const unsigned char octets[8])</td>
</tr>
<tr class="memdesc:ga108d7d64fb88fffca31e33181cefa232">
<td class="mdescLeft"> </td>
<td class="mdescRight">Inserts 8 bytes aligned on an 8 byte boundary with any alignment padding initialized to 0.<br />
</td>
</tr>
<tr class="separator:ga108d7d64fb88fffca31e33181cefa232">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga267217e412c74c74dc3a3e412da5c600" class="memitem:ga267217e412c74c74dc3a3e412da5c600">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_insert_alignment (DBusString *str, int *insert_at, int alignment)</td>
</tr>
<tr class="memdesc:ga267217e412c74c74dc3a3e412da5c600">
<td class="mdescLeft"> </td>
<td class="mdescRight">Inserts padding at *insert_at such to align it to the given boundary.<br />
</td>
</tr>
<tr class="separator:ga267217e412c74c74dc3a3e412da5c600">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8d794f292831d1a7edeb971b13a2c641" class="memitem:ga8d794f292831d1a7edeb971b13a2c641">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_append_printf_valist (DBusString *str, const char *format, va_list args)</td>
</tr>
<tr class="memdesc:ga8d794f292831d1a7edeb971b13a2c641">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends a printf-style formatted string to the DBusString.<br />
</td>
</tr>
<tr class="separator:ga8d794f292831d1a7edeb971b13a2c641">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab0078cf7e0e5bd784ec6d6e0cc3923a2" class="memitem:gab0078cf7e0e5bd784ec6d6e0cc3923a2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_append_printf (DBusString *str, const char *format,...)</td>
</tr>
<tr class="memdesc:gab0078cf7e0e5bd784ec6d6e0cc3923a2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends a printf-style formatted string to the DBusString.<br />
</td>
</tr>
<tr class="separator:gab0078cf7e0e5bd784ec6d6e0cc3923a2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga724656b7091b910965bd1af42d0b7bab" class="memitem:ga724656b7091b910965bd1af42d0b7bab">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_append_len (DBusString *str, const char *buffer, int len)</td>
</tr>
<tr class="memdesc:ga724656b7091b910965bd1af42d0b7bab">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends block of bytes with the given length to a DBusString.<br />
</td>
</tr>
<tr class="separator:ga724656b7091b910965bd1af42d0b7bab">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa6ecf36e70263659f921a4ef0335db12" class="memitem:gaa6ecf36e70263659f921a4ef0335db12">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_append_byte (DBusString *str, unsigned char byte)</td>
</tr>
<tr class="memdesc:gaa6ecf36e70263659f921a4ef0335db12">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends a single byte to the string, returning FALSE if not enough memory.<br />
</td>
</tr>
<tr class="separator:gaa6ecf36e70263659f921a4ef0335db12">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga35c2099d5ce2475ea6fe786be6572908" class="memitem:ga35c2099d5ce2475ea6fe786be6572908">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_append_strings (DBusString *str, char **strings, char separator)</td>
</tr>
<tr class="memdesc:ga35c2099d5ce2475ea6fe786be6572908">
<td class="mdescLeft"> </td>
<td class="mdescRight">Append vector with <code>strings</code> connected by <code>separator</code>.<br />
</td>
</tr>
<tr class="separator:ga35c2099d5ce2475ea6fe786be6572908">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7e0e164ad5bb094e5ccad9edc7ae4235" class="memitem:ga7e0e164ad5bb094e5ccad9edc7ae4235">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_delete (DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga7e0e164ad5bb094e5ccad9edc7ae4235">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deletes a segment of a DBusString with length len starting at start.<br />
</td>
</tr>
<tr class="separator:ga7e0e164ad5bb094e5ccad9edc7ae4235">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad379fce8d4ef4f7e28f81f50b46ee4c9" class="memitem:gad379fce8d4ef4f7e28f81f50b46ee4c9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_move (DBusString *source, int start, DBusString *dest, int insert_at)</td>
</tr>
<tr class="memdesc:gad379fce8d4ef4f7e28f81f50b46ee4c9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Moves the end of one string into another string.<br />
</td>
</tr>
<tr class="separator:gad379fce8d4ef4f7e28f81f50b46ee4c9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3c10f0d1bcaa3b450025b9c6a8b901d7" class="memitem:ga3c10f0d1bcaa3b450025b9c6a8b901d7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_copy (const DBusString *source, int start, DBusString *dest, int insert_at)</td>
</tr>
<tr class="memdesc:ga3c10f0d1bcaa3b450025b9c6a8b901d7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_string_move(), but does not delete the section of the source string that's copied to the dest string.<br />
</td>
</tr>
<tr class="separator:ga3c10f0d1bcaa3b450025b9c6a8b901d7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab8e2dcb2dc71bf225da0827c6086a727" class="memitem:gab8e2dcb2dc71bf225da0827c6086a727">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_move_len (DBusString *source, int start, int len, DBusString *dest, int insert_at)</td>
</tr>
<tr class="memdesc:gab8e2dcb2dc71bf225da0827c6086a727">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_string_move(), but can move a segment from the middle of the source string.<br />
</td>
</tr>
<tr class="separator:gab8e2dcb2dc71bf225da0827c6086a727">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf5f13bc7ac7a623516930d26ae2589bf" class="memitem:gaf5f13bc7ac7a623516930d26ae2589bf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_copy_len (const DBusString *source, int start, int len, DBusString *dest, int insert_at)</td>
</tr>
<tr class="memdesc:gaf5f13bc7ac7a623516930d26ae2589bf">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_string_copy(), but can copy a segment from the middle of the source string.<br />
</td>
</tr>
<tr class="separator:gaf5f13bc7ac7a623516930d26ae2589bf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafe7921a92467cdefaa0a7829d6cf260b" class="memitem:gafe7921a92467cdefaa0a7829d6cf260b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_replace_len (const DBusString *source, int start, int len, DBusString *dest, int replace_at, int replace_len)</td>
</tr>
<tr class="memdesc:gafe7921a92467cdefaa0a7829d6cf260b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Replaces a segment of dest string with a segment of source string.<br />
</td>
</tr>
<tr class="separator:gafe7921a92467cdefaa0a7829d6cf260b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5d293b49b6afbbd74069d0823acce6b5" class="memitem:ga5d293b49b6afbbd74069d0823acce6b5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_split_on_byte (DBusString *source, unsigned char byte, DBusString *tail)</td>
</tr>
<tr class="memdesc:ga5d293b49b6afbbd74069d0823acce6b5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Looks for the first occurance of a byte, deletes that byte, and moves everything after the byte to the beginning of a separate string.<br />
</td>
</tr>
<tr class="separator:ga5d293b49b6afbbd74069d0823acce6b5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5fe47873b2838339107c3e1f03d1a703" class="memitem:ga5fe47873b2838339107c3e1f03d1a703">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_find (const DBusString *str, int start, const char *substr, int *found)</td>
</tr>
<tr class="memdesc:ga5fe47873b2838339107c3e1f03d1a703">
<td class="mdescLeft"> </td>
<td class="mdescRight">Finds the given substring in the string, returning TRUE and filling in the byte index where the substring was found, if it was found.<br />
</td>
</tr>
<tr class="separator:ga5fe47873b2838339107c3e1f03d1a703">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3c98d1913e3ba4deb8eda60b2e262fdb" class="memitem:ga3c98d1913e3ba4deb8eda60b2e262fdb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_find_eol (const DBusString *str, int start, int *found, int *found_len)</td>
</tr>
<tr class="memdesc:ga3c98d1913e3ba4deb8eda60b2e262fdb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Finds end of line ("\r\n" or "\n") in the string, returning TRUE and filling in the byte index where the eol string was found, if it was found.<br />
</td>
</tr>
<tr class="separator:ga3c98d1913e3ba4deb8eda60b2e262fdb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf2281731c3119f946726680242a5ae02" class="memitem:gaf2281731c3119f946726680242a5ae02">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_find_to (const DBusString *str, int start, int end, const char *substr, int *found)</td>
</tr>
<tr class="memdesc:gaf2281731c3119f946726680242a5ae02">
<td class="mdescLeft"> </td>
<td class="mdescRight">Finds the given substring in the string, up to a certain position, returning TRUE and filling in the byte index where the substring was found, if it was found.<br />
</td>
</tr>
<tr class="separator:gaf2281731c3119f946726680242a5ae02">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga677ddb4246c7e7f67ed3145dc3c1c96b" class="memitem:ga677ddb4246c7e7f67ed3145dc3c1c96b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_find_blank (const DBusString *str, int start, int *found)</td>
</tr>
<tr class="memdesc:ga677ddb4246c7e7f67ed3145dc3c1c96b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Finds a blank (space or tab) in the string.<br />
</td>
</tr>
<tr class="separator:ga677ddb4246c7e7f67ed3145dc3c1c96b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5698b163289be0066cf10c0f1caf877a" class="memitem:ga5698b163289be0066cf10c0f1caf877a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_skip_blank (const DBusString *str, int start, int *end)</td>
</tr>
<tr class="memdesc:ga5698b163289be0066cf10c0f1caf877a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Skips blanks from start, storing the first non-blank in *end (blank is space or tab).<br />
</td>
</tr>
<tr class="separator:ga5698b163289be0066cf10c0f1caf877a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8600259d71a4adc14ab4558a9d2a0f7d" class="memitem:ga8600259d71a4adc14ab4558a9d2a0f7d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_skip_white (const DBusString *str, int start, int *end)</td>
</tr>
<tr class="memdesc:ga8600259d71a4adc14ab4558a9d2a0f7d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Skips whitespace from start, storing the first non-whitespace in *end.<br />
</td>
</tr>
<tr class="separator:ga8600259d71a4adc14ab4558a9d2a0f7d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga578bb88acec5520825f2ba792cad7938" class="memitem:ga578bb88acec5520825f2ba792cad7938">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_skip_white_reverse (const DBusString *str, int end, int *start)</td>
</tr>
<tr class="memdesc:ga578bb88acec5520825f2ba792cad7938">
<td class="mdescLeft"> </td>
<td class="mdescRight">Skips whitespace from end, storing the start index of the trailing whitespace in *start.<br />
</td>
</tr>
<tr class="separator:ga578bb88acec5520825f2ba792cad7938">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8b7fc22e6738173e1b2cef4b91b9c3c1" class="memitem:ga8b7fc22e6738173e1b2cef4b91b9c3c1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_pop_line (DBusString *source, DBusString *dest)</td>
</tr>
<tr class="memdesc:ga8b7fc22e6738173e1b2cef4b91b9c3c1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Assigns a newline-terminated or \r\n-terminated line from the front of the string to the given dest string.<br />
</td>
</tr>
<tr class="separator:ga8b7fc22e6738173e1b2cef4b91b9c3c1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa92c6ab2c5e24cbefef0a3f3fc76f98b" class="memitem:gaa92c6ab2c5e24cbefef0a3f3fc76f98b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_chop_white (DBusString *str)</td>
</tr>
<tr class="memdesc:gaa92c6ab2c5e24cbefef0a3f3fc76f98b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deletes leading and trailing whitespace.<br />
</td>
</tr>
<tr class="separator:gaa92c6ab2c5e24cbefef0a3f3fc76f98b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad79c34af55b58f0e8b81ecf11b8694bb" class="memitem:gad79c34af55b58f0e8b81ecf11b8694bb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_equal (const DBusString *a, const DBusString *b)</td>
</tr>
<tr class="memdesc:gad79c34af55b58f0e8b81ecf11b8694bb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tests two DBusString for equality.<br />
</td>
</tr>
<tr class="separator:gad79c34af55b58f0e8b81ecf11b8694bb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacf39727ae9eb411b0c4cb3b891588fb0" class="memitem:gacf39727ae9eb411b0c4cb3b891588fb0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_equal_len (const DBusString *a, const DBusString *b, int len)</td>
</tr>
<tr class="memdesc:gacf39727ae9eb411b0c4cb3b891588fb0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tests two DBusString for equality up to the given length.<br />
</td>
</tr>
<tr class="separator:gacf39727ae9eb411b0c4cb3b891588fb0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2095c2a797ae245521a7588b32279110" class="memitem:ga2095c2a797ae245521a7588b32279110">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_equal_substring (const DBusString *a, int a_start, int a_len, const DBusString *b, int b_start)</td>
</tr>
<tr class="memdesc:ga2095c2a797ae245521a7588b32279110">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tests two sub-parts of two DBusString for equality.<br />
</td>
</tr>
<tr class="separator:ga2095c2a797ae245521a7588b32279110">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga84f39f1bf398697920637d2982248c72" class="memitem:ga84f39f1bf398697920637d2982248c72">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_equal_c_str (const DBusString *a, const char *c_str)</td>
</tr>
<tr class="memdesc:ga84f39f1bf398697920637d2982248c72">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether a string is equal to a C string.<br />
</td>
</tr>
<tr class="separator:ga84f39f1bf398697920637d2982248c72">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4763d06a65cca36986bff030b404c90d" class="memitem:ga4763d06a65cca36986bff030b404c90d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_starts_with_c_str (const DBusString *a, const char *c_str)</td>
</tr>
<tr class="memdesc:ga4763d06a65cca36986bff030b404c90d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether a string starts with the given C string.<br />
</td>
</tr>
<tr class="separator:ga4763d06a65cca36986bff030b404c90d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaaa0154941c9182090fb32cc20af48fde" class="memitem:gaaa0154941c9182090fb32cc20af48fde">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_starts_with_words_c_str (const DBusString *a, const char *c_str, char word_separator)</td>
</tr>
<tr class="memdesc:gaaa0154941c9182090fb32cc20af48fde">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether a string starts with the given C string, after which it ends or is separated from the rest by a given separator character.<br />
</td>
</tr>
<tr class="separator:gaaa0154941c9182090fb32cc20af48fde">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae99a331d4e5b7758652b78dc9c89de84" class="memitem:gae99a331d4e5b7758652b78dc9c89de84">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_append_byte_as_hex (DBusString *str, unsigned char byte)</td>
</tr>
<tr class="memdesc:gae99a331d4e5b7758652b78dc9c89de84">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends a two-character hex digit to a string, where the hex digit has the value of the given byte.<br />
</td>
</tr>
<tr class="separator:gae99a331d4e5b7758652b78dc9c89de84">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaabb4873f436e015944a33cd1e3815cc9" class="memitem:gaabb4873f436e015944a33cd1e3815cc9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_hex_encode (const DBusString *source, int start, DBusString *dest, int insert_at)</td>
</tr>
<tr class="memdesc:gaabb4873f436e015944a33cd1e3815cc9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Encodes a string in hex, the way MD5 and SHA-1 are usually encoded.<br />
</td>
</tr>
<tr class="separator:gaabb4873f436e015944a33cd1e3815cc9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0a8c20d855f9ddc05718b9e2ac0e33d8" class="memitem:ga0a8c20d855f9ddc05718b9e2ac0e33d8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_hex_decode (const DBusString *source, int start, int *end_return, DBusString *dest, int insert_at)</td>
</tr>
<tr class="memdesc:ga0a8c20d855f9ddc05718b9e2ac0e33d8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decodes a string from hex encoding.<br />
</td>
</tr>
<tr class="separator:ga0a8c20d855f9ddc05718b9e2ac0e33d8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa4324cd667e21beb31a5481cb0c12b6d" class="memitem:gaa4324cd667e21beb31a5481cb0c12b6d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_validate_ascii (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:gaa4324cd667e21beb31a5481cb0c12b6d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks that the given range of the string is valid ASCII with no nul bytes.<br />
</td>
</tr>
<tr class="separator:gaa4324cd667e21beb31a5481cb0c12b6d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga698f4b0299e6c6a707fd7e9c14915f00" class="memitem:ga698f4b0299e6c6a707fd7e9c14915f00">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_tolower_ascii (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga698f4b0299e6c6a707fd7e9c14915f00">
<td class="mdescLeft"> </td>
<td class="mdescRight">Converts the given range of the string to lower case.<br />
</td>
</tr>
<tr class="separator:ga698f4b0299e6c6a707fd7e9c14915f00">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9c959f7d18ff21c5ae51846c6ba065f1" class="memitem:ga9c959f7d18ff21c5ae51846c6ba065f1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_toupper_ascii (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga9c959f7d18ff21c5ae51846c6ba065f1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Converts the given range of the string to upper case.<br />
</td>
</tr>
<tr class="separator:ga9c959f7d18ff21c5ae51846c6ba065f1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga65f0f04b7c9371406fc87343f691e8da" class="memitem:ga65f0f04b7c9371406fc87343f691e8da">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_validate_utf8 (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga65f0f04b7c9371406fc87343f691e8da">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks that the given range of the string is valid UTF-8.<br />
</td>
</tr>
<tr class="separator:ga65f0f04b7c9371406fc87343f691e8da">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga199d0fc00ee3cd0300a1b3870d7986a3" class="memitem:ga199d0fc00ee3cd0300a1b3870d7986a3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_validate_nul (const DBusString *str, int start, int len)</td>
</tr>
<tr class="memdesc:ga199d0fc00ee3cd0300a1b3870d7986a3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks that the given range of the string is all nul bytes.<br />
</td>
</tr>
<tr class="separator:ga199d0fc00ee3cd0300a1b3870d7986a3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9385fd0de31b3f5f4f8baa96bad3fac6" class="memitem:ga9385fd0de31b3f5f4f8baa96bad3fac6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_zero (DBusString *str)</td>
</tr>
<tr class="memdesc:ga9385fd0de31b3f5f4f8baa96bad3fac6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Clears all allocated bytes in the string to zero.<br />
</td>
</tr>
<tr class="separator:ga9385fd0de31b3f5f4f8baa96bad3fac6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafa79c1113fa75419dcc5ee4290e06608" class="memitem:gafa79c1113fa75419dcc5ee4290e06608">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_get_dirname (const DBusString *filename, DBusString *dirname)</td>
</tr>
<tr class="memdesc:gafa79c1113fa75419dcc5ee4290e06608">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get the directory name from a complete filename.<br />
</td>
</tr>
<tr class="separator:gafa79c1113fa75419dcc5ee4290e06608">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga849177164bc5e73435104f57c631ed7e" class="memitem:ga849177164bc5e73435104f57c631ed7e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_unix_user_is_process_owner (dbus_uid_t uid)</td>
</tr>
<tr class="memdesc:ga849177164bc5e73435104f57c631ed7e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks to see if the UNIX user ID matches the UID of the process.<br />
</td>
</tr>
<tr class="separator:ga849177164bc5e73435104f57c631ed7e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga912d34a7e40b3a57864972e6d6ab65ba" class="memitem:ga912d34a7e40b3a57864972e6d6ab65ba">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_windows_user_is_process_owner (const char *windows_sid)</td>
</tr>
<tr class="memdesc:ga912d34a7e40b3a57864972e6d6ab65ba">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks to see if the Windows user SID matches the owner of the process.<br />
</td>
</tr>
<tr class="separator:ga912d34a7e40b3a57864972e6d6ab65ba">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaed2e025454364fbe31cd9b6538c9a936" class="memitem:gaed2e025454364fbe31cd9b6538c9a936">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_unix_user_is_at_console (dbus_uid_t uid, DBusError *error)</td>
</tr>
<tr class="memdesc:gaed2e025454364fbe31cd9b6538c9a936">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks to see if the UNIX user ID is at the console.<br />
</td>
</tr>
<tr class="separator:gaed2e025454364fbe31cd9b6538c9a936">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga96da816095ec7fec07136a6019745bcb" class="memitem:ga96da816095ec7fec07136a6019745bcb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_parse_unix_group_from_config (const DBusString *groupname, dbus_gid_t *gid_p)</td>
</tr>
<tr class="memdesc:ga96da816095ec7fec07136a6019745bcb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parse a UNIX group from the bus config file.<br />
</td>
</tr>
<tr class="separator:ga96da816095ec7fec07136a6019745bcb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga437470fc327b0169fc14a0b66a6e5278" class="memitem:ga437470fc327b0169fc14a0b66a6e5278">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_parse_unix_user_from_config (const DBusString *username, dbus_uid_t *uid_p)</td>
</tr>
<tr class="memdesc:ga437470fc327b0169fc14a0b66a6e5278">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parse a UNIX user from the bus config file.<br />
</td>
</tr>
<tr class="separator:ga437470fc327b0169fc14a0b66a6e5278">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9abae6dadad0773206dca0519c5b3c9c" class="memitem:ga9abae6dadad0773206dca0519c5b3c9c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_unix_groups_from_uid (dbus_uid_t uid, dbus_gid_t **group_ids, int *n_group_ids, DBusError *error)</td>
</tr>
<tr class="memdesc:ga9abae6dadad0773206dca0519c5b3c9c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets all groups corresponding to the given UNIX user ID.<br />
</td>
</tr>
<tr class="separator:ga9abae6dadad0773206dca0519c5b3c9c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga93e22894a5e2e0d65c179c7d36a8b1c8" class="memitem:ga93e22894a5e2e0d65c179c7d36a8b1c8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_parse_int (const DBusString *str, int start, long *value_return, int *end_return)</td>
</tr>
<tr class="memdesc:ga93e22894a5e2e0d65c179c7d36a8b1c8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parses an integer contained in a DBusString.<br />
</td>
</tr>
<tr class="separator:ga93e22894a5e2e0d65c179c7d36a8b1c8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga84cc8d08bb48b7915d673f7cc7886f97" class="memitem:ga84cc8d08bb48b7915d673f7cc7886f97">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_parse_uint (const DBusString *str, int start, unsigned long *value_return, int *end_return)</td>
</tr>
<tr class="memdesc:ga84cc8d08bb48b7915d673f7cc7886f97">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parses an unsigned integer contained in a DBusString.<br />
</td>
</tr>
<tr class="separator:ga84cc8d08bb48b7915d673f7cc7886f97">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3c44a3b6dbd1605dc2931ad835029206" class="memitem:ga3c44a3b6dbd1605dc2931ad835029206">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_parse_int64 (const DBusString *str, int start, dbus_int64_t *value_return, int *end_return)</td>
</tr>
<tr class="memdesc:ga3c44a3b6dbd1605dc2931ad835029206">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parses a dbus_int64_t integer contained in a DBusString.<br />
</td>
</tr>
<tr class="separator:ga3c44a3b6dbd1605dc2931ad835029206">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusString data structure for safer string handling.

Types and functions related to DBusString. DBusString is intended to be a string class that makes it hard to mess up security issues (and just in general harder to write buggy code). It should be used (or extended and then used) rather than the libc stuff in string.h. The string class is a bit inconvenient at spots because it handles out-of-memory failures and tries to be extra-robust.

A DBusString has a maximum length set at initialization time; this can be used to ensure that a buffer doesn't get too big. The \_dbus_string_lengthen() method checks for overflow, and for max length being exceeded.

Try to avoid conversion to a plain C string, i.e. add methods on the string object instead, only convert to C string when passing things out to the public API. In particular, no sprintf, strcpy, strcat, any of that should be used. The GString feature of accepting negative numbers for "length of string" is also absent, because it could keep us from detecting bogus huge lengths. i.e. if we passed in some bogus huge length it would be taken to mean "current length of string" instead of "broken crack"

## Macro Definition Documentation

## ◆ DBUS_STRING_COPY_PREAMBLE

|                                    |     |     |            |
|------------------------------------|-----|-----|------------|
| \#define DBUS_STRING_COPY_PREAMBLE | (   |     | source,    |
|                                    |     |     | start,     |
|                                    |     |     | dest,      |
|                                    |     |     | insert_at  |
|                                    | )   |     |            |

**Value:**

DBusRealString \*real_source = (DBusRealString\*) source; \\

DBusRealString \*real_dest = (DBusRealString\*) dest; \\

\_dbus_assert ((source) != (dest)); \\

DBUS_GENERIC_STRING_PREAMBLE (real_source); \\

DBUS_GENERIC_STRING_PREAMBLE (real_dest); \\

\_dbus_assert (!real_dest-\>constant); \\

\_dbus_assert (!real_dest-\>locked); \\

\_dbus_assert ((start) \>= 0); \\

\_dbus_assert ((start) \<= real_source-\>len); \\

\_dbus_assert ((insert_at) \>= 0); \\

\_dbus_assert ((insert_at) \<= real_dest-\>len)

DBusRealString

Internals of DBusString.

**Definition** dbus-string-private.h:46

DBusRealString::constant

unsigned int constant

String data is not owned by DBusString.

**Definition** dbus-string-private.h:50

DBusRealString::locked

unsigned int locked

DBusString has been locked and can't be changed.

**Definition** dbus-string-private.h:51

DBusRealString::len

int len

Length without nul.

**Definition** dbus-string-private.h:48

Checks assertions for two strings we're copying a segment between, and declares real_source/real_dest variables.

Parameters  
|           |                                      |
|-----------|--------------------------------------|
| source    | the source string                    |
| start     | the starting offset                  |
| dest      | the dest string                      |
| insert_at | where the copied segment is inserted |

Definition at line 1297 of file dbus-string.c.

## ◆ UNICODE_VALID

|                        |     |     |      |     |     |
|------------------------|-----|-----|------|-----|-----|
| \#define UNICODE_VALID | (   |     | Char | )   |     |

**Value:**

((Char) \< 0x110000 && \\

(((Char) & 0xFFFFF800) != 0xD800))

Check whether a Unicode (5.2) char is in a valid range.

The first check comes from the Unicode guarantee to never encode a point above 0x0010ffff, since UTF-16 couldn't represent it.

The second check covers surrogate pairs (category Cs).

Parameters  
|      |               |
|------|---------------|
| Char | the character |

Definition at line 1647 of file dbus-string.c.

## ◆ UTF8_COMPUTE

|                       |     |     |       |
|-----------------------|-----|-----|-------|
| \#define UTF8_COMPUTE | (   |     | Char, |
|                       |     |     | Mask, |
|                       |     |     | Len   |
|                       | )   |     |       |

computes length and mask of a unicode character

Parameters  
|      |                                  |
|------|----------------------------------|
| Char | the char                         |
| Mask | the mask variable to assign to   |
| Len  | the length variable to assign to |

Definition at line 1567 of file dbus-string.c.

## ◆ UTF8_GET

|                   |     |     |         |
|-------------------|-----|-----|---------|
| \#define UTF8_GET | (   |     | Result, |
|                   |     |     | Chars,  |
|                   |     |     | Count,  |
|                   |     |     | Mask,   |
|                   |     |     | Len     |
|                   | )   |     |         |

**Value:**

(Result) = (Chars)\[0\] & (Mask); \\

for ((Count) = 1; (Count) \< (Len); ++(Count)) \\

{ \\

if (((Chars)\[(Count)\] & 0xc0) != 0x80) \\

{ \\

(Result) = -1; \\

break; \\

} \\

(Result) \<\<= 6; \\

(Result) \|= ((Chars)\[(Count)\] & 0x3f); \\

}

Gets a UTF-8 value.

Parameters  
|        |                                      |
|--------|--------------------------------------|
| Result | variable for extracted unicode char. |
| Chars  | the bytes to decode                  |
| Count  | counter variable                     |
| Mask   | mask for this char                   |
| Len    | length for this char in bytes        |

Definition at line 1624 of file dbus-string.c.

## ◆ UTF8_LENGTH

|                      |     |     |      |     |     |
|----------------------|-----|-----|------|-----|-----|
| \#define UTF8_LENGTH | (   |     | Char | )   |     |

**Value:**

((Char) \< 0x80 ? 1 : \\

((Char) \< 0x800 ? 2 : \\

((Char) \< 0x10000 ? 3 : \\

((Char) \< 0x200000 ? 4 : \\

((Char) \< 0x4000000 ? 5 : 6)))))

computes length of a unicode character in UTF-8

Parameters  
|      |          |
|------|----------|
| Char | the char |

Definition at line 1608 of file dbus-string.c.

## Function Documentation

## ◆ \_dbus_parse_unix_group_from_config()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_parse_unix_group_from_config | ( | const DBusString \*  | *groupname*, |
|  |  | dbus_gid_t \*  | *gid_p*  |
|  | ) |  |  |

Parse a UNIX group from the bus config file.

On Windows, this should simply always fail (just return FALSE).

Parameters  
|           |                         |
|-----------|-------------------------|
| groupname | the groupname text      |
| gid_p     | place to return the gid |

<!-- -->

Returns  
TRUE on success

Definition at line 687 of file dbus-sysdeps-util-win.c.

References FALSE.

## ◆ \_dbus_parse_unix_user_from_config()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_parse_unix_user_from_config | ( | const DBusString \*  | *username*, |
|  |  | dbus_uid_t \*  | *uid_p*  |
|  | ) |  |  |

Parse a UNIX user from the bus config file.

On Windows, this should simply always fail (just return FALSE).

Parameters  
|          |                         |
|----------|-------------------------|
| username | the username text       |
| uid_p    | place to return the uid |

<!-- -->

Returns  
TRUE on success

Definition at line 702 of file dbus-sysdeps-util-win.c.

References FALSE.

## ◆ \_dbus_string_align_length()

|                                        |     |                |              |
|----------------------------------------|-----|----------------|--------------|
| dbus_bool_t \_dbus_string_align_length | (   | DBusString \*  | *str*,       |
|                                        |     | int            | *alignment*  |
|                                        | )   |                |              |

Align the length of a string to a specific alignment (typically 4 or 8) by appending nul bytes to the string.

Parameters  
|           |               |
|-----------|---------------|
| str       | a string      |
| alignment | the alignment |

<!-- -->

Returns  
FALSE if no memory

Definition at line 928 of file dbus-string.c.

## ◆ \_dbus_string_alloc_space()

|                                       |     |                |                |
|---------------------------------------|-----|----------------|----------------|
| dbus_bool_t \_dbus_string_alloc_space | (   | DBusString \*  | *str*,         |
|                                       |     | int            | *extra_bytes*  |
|                                       | )   |                |                |

Preallocate extra_bytes such that a future lengthening of the string by extra_bytes is guaranteed to succeed without an out of memory error.

Parameters  
|             |                |
|-------------|----------------|
| str         | a string       |
| extra_bytes | bytes to alloc |

<!-- -->

Returns  
FALSE if no memory

Definition at line 944 of file dbus-string.c.

References \_dbus_string_lengthen(), \_dbus_string_shorten(), FALSE, and TRUE.

Referenced by \_dbus_type_writer_write_basic().

## ◆ \_dbus_string_append()

|                                  |     |                |           |
|----------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_string_append | (   | DBusString \*  | *str*,    |
|                                  |     | const char \*  | *buffer*  |
|                                  | )   |                |           |

Appends a nul-terminated C-style string to a DBusString.

Parameters  
|        |                                         |
|--------|-----------------------------------------|
| str    | the DBusString                          |
| buffer | the nul-terminated characters to append |

<!-- -->

Returns  
FALSE if not enough memory.

Definition at line 980 of file dbus-string.c.

References \_dbus_assert, \_DBUS_STRING_MAX_LENGTH, DBUS_STRING_PREAMBLE, FALSE, and NULL.

Referenced by \_dbus_append_address_from_socket(), \_dbus_append_keyring_directory_for_credentials(), \_dbus_append_user_from_current_process(), \_dbus_auth_dump_supported_mechanisms(), \_dbus_directory_get_next_file(), \_dbus_directory_open(), \_dbus_get_session_config_file(), \_dbus_get_standard_session_servicedirs(), \_dbus_get_system_config_file(), \_dbus_hash_table_from_array(), \_dbus_homedir_from_uid(), \_dbus_is_console_user(), \_dbus_keyring_new_for_credentials(), \_dbus_listen_tcp_socket(), \_dbus_server_listen_platform_specific(), \_dbus_server_listen_unix_socket(), \_dbus_server_new_for_domain_socket(), \_dbus_server_new_for_launchd(), \_dbus_server_new_for_tcp_socket(), \_dbus_set_up_transient_session_servicedirs(), \_dbus_string_append_strings(), \_dbus_string_get_dirname(), \_dbus_string_init_from_string(), \_dbus_string_save_to_file(), \_dbus_transport_new_for_domain_socket(), and \_dbus_transport_new_for_tcp_socket().

## ◆ \_dbus_string_append_byte()

|                                       |     |                |         |
|---------------------------------------|-----|----------------|---------|
| dbus_bool_t \_dbus_string_append_byte | (   | DBusString \*  | *str*,  |
|                                       |     | unsigned char  | *byte*  |
|                                       | )   |                |         |

Appends a single byte to the string, returning FALSE if not enough memory.

Parameters  
|      |                    |
|------|--------------------|
| str  | the string         |
| byte | the byte to append |

<!-- -->

Returns  
TRUE on success

Definition at line 1190 of file dbus-string.c.

References DBUS_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::str, and TRUE.

Referenced by \_dbus_address_append_escaped(), \_dbus_concat_dir_and_file(), \_dbus_string_append_byte_as_hex(), \_dbus_string_append_strings(), \_dbus_string_hex_decode(), and \_dbus_write_uuid_file().

## ◆ \_dbus_string_append_byte_as_hex()

|                                              |     |                |         |
|----------------------------------------------|-----|----------------|---------|
| dbus_bool_t \_dbus_string_append_byte_as_hex | (   | DBusString \*  | *str*,  |
|                                              |     | unsigned char  | *byte*  |
|                                              | )   |                |         |

Appends a two-character hex digit to a string, where the hex digit has the value of the given byte.

Parameters  
|      |            |
|------|------------|
| str  | the string |
| byte | the byte   |

<!-- -->

Returns  
FALSE if no memory

Definition at line 2313 of file dbus-string.c.

References \_dbus_string_append_byte(), \_dbus_string_get_length(), \_dbus_string_set_length(), FALSE, and TRUE.

Referenced by \_dbus_address_append_escaped(), and \_dbus_string_hex_encode().

## ◆ \_dbus_string_append_len()

|                                      |     |                |           |
|--------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_string_append_len | (   | DBusString \*  | *str*,    |
|                                      |     | const char \*  | *buffer*, |
|                                      |     | int            | *len*     |
|                                      | )   |                |           |

Appends block of bytes with the given length to a DBusString.

Parameters  
|        |                               |
|--------|-------------------------------|
| str    | the DBusString                |
| buffer | the bytes to append           |
| len    | the number of bytes to append |

<!-- -->

Returns  
FALSE if not enough memory.

Definition at line 1170 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_PREAMBLE, and NULL.

Referenced by \_dbus_sha_final(), dbus_message_demarshal(), dbus_message_iter_get_signature(), and dbus_signature_iter_get_signature().

## ◆ \_dbus_string_append_printf()

|                                         |     |                |           |
|-----------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_string_append_printf | (   | DBusString \*  | *str*,    |
|                                         |     | const char \*  | *format*, |
|                                         |     |                | *...*     |
|                                         | )   |                |           |

Appends a printf-style formatted string to the DBusString.

Parameters  
|        |               |
|--------|---------------|
| str    | the string    |
| format | printf format |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1147 of file dbus-string.c.

References \_dbus_string_append_printf_valist().

Referenced by \_dbus_append_address_from_socket(), \_dbus_append_user_from_current_process(), \_dbus_command_for_pid(), \_dbus_credentials_to_string_append(), \_dbus_get_autolaunch_address(), \_dbus_hash_table_to_array(), \_dbus_logv(), \_dbus_resolve_pid_fd(), \_dbus_set_up_transient_session_servicedirs(), \_dbus_write_pid_to_file_and_pipe(), and dbus_connection_dispatch().

## ◆ \_dbus_string_append_printf_valist()

|                                                |     |                |           |
|------------------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_string_append_printf_valist | (   | DBusString \*  | *str*,    |
|                                                |     | const char \*  | *format*, |
|                                                |     | va_list        | *args*    |
|                                                | )   |                |           |

Appends a printf-style formatted string to the DBusString.

Parameters  
|        |                        |
|--------|------------------------|
| str    | the string             |
| format | printf format          |
| args   | variable argument list |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1105 of file dbus-string.c.

References \_dbus_printf_string_upper_bound(), \_dbus_string_lengthen(), DBUS_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::str, and TRUE.

Referenced by \_dbus_logv(), \_dbus_string_append_printf(), and dbus_message_new_error_printf().

## ◆ \_dbus_string_append_strings()

|                                          |     |                |              |
|------------------------------------------|-----|----------------|--------------|
| dbus_bool_t \_dbus_string_append_strings | (   | DBusString \*  | *str*,       |
|                                          |     | char \*\*      | *strings*,   |
|                                          |     | char           | *separator*  |
|                                          | )   |                |              |

Append vector with `strings` connected by `separator`.

Parameters  
|           |                                        |
|-----------|----------------------------------------|
| str       | the string                             |
| strings   | vector with char\* pointer for merging |
| separator | separator to merge the vector          |

<!-- -->

Returns  
FALSE if not enough memory

TRUE success or empty string vector

Definition at line 1213 of file dbus-string.c.

References \_dbus_string_append(), \_dbus_string_append_byte(), FALSE, NULL, and TRUE.

## ◆ \_dbus_string_chop_white()

|                               |     |                |       |     |     |
|-------------------------------|-----|----------------|-------|-----|-----|
| void \_dbus_string_chop_white | (   | DBusString \*  | *str* | )   |     |

Deletes leading and trailing whitespace.

Parameters  
|     |            |
|-----|------------|
| str | the string |

Definition at line 2051 of file dbus-string.c.

References \_dbus_string_delete(), \_dbus_string_get_length(), \_dbus_string_set_length(), \_dbus_string_skip_white(), and \_dbus_string_skip_white_reverse().

Referenced by \_dbus_split_paths_and_append().

## ◆ \_dbus_string_compact()

|                                   |     |                |              |
|-----------------------------------|-----|----------------|--------------|
| dbus_bool_t \_dbus_string_compact | (   | DBusString \*  | *str*,       |
|                                   |     | int            | *max_waste*  |
|                                   | )   |                |              |

Compacts the string to avoid wasted memory.

Wasted memory is memory that is allocated but not actually required to store the current length of the string. The compact is only done if more than the given amount of memory is being wasted (otherwise the waste is ignored and the call does nothing).

Parameters  
|           |                                       |
|-----------|---------------------------------------|
| str       | the string                            |
| max_waste | the maximum amount of waste to ignore |

<!-- -->

Returns  
FALSE if the compact failed due to realloc failure

Definition at line 420 of file dbus-string.c.

References DBUS_STRING_PREAMBLE.

## ◆ \_dbus_string_copy()

|                                |     |                      |              |
|--------------------------------|-----|----------------------|--------------|
| dbus_bool_t \_dbus_string_copy | (   | const DBusString \*  | *source*,    |
|                                |     | int                  | *start*,     |
|                                |     | DBusString \*        | *dest*,      |
|                                |     | int                  | *insert_at*  |
|                                | )   |                      |              |

Like \_dbus_string_move(), but does not delete the section of the source string that's copied to the dest string.

Parameters  
|           |                                                 |
|-----------|-------------------------------------------------|
| source    | the source string                               |
| start     | where to start copying the source string        |
| dest      | the destination string                          |
| insert_at | where to place the copied part of source string |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 1345 of file dbus-string.c.

References DBUS_STRING_COPY_PREAMBLE.

Referenced by \_dbus_append_keyring_directory_for_credentials(), \_dbus_auth_decode_data(), \_dbus_auth_encode_data(), \_dbus_auth_server_new(), \_dbus_command_for_pid(), \_dbus_concat_dir_and_file(), \_dbus_header_copy(), \_dbus_keyring_new_for_credentials(), \_dbus_string_save_to_file(), dbus_message_copy(), and dbus_message_marshal().

## ◆ \_dbus_string_copy_data()

|                                     |     |                      |                |
|-------------------------------------|-----|----------------------|----------------|
| dbus_bool_t \_dbus_string_copy_data | (   | const DBusString \*  | *str*,         |
|                                     |     | char \*\*            | *data_return*  |
|                                     | )   |                      |                |

Copies the data from the string into a char\*.

Parameters  
|             |                          |
|-------------|--------------------------|
| str         | the string               |
| data_return | place to return the data |

<!-- -->

Returns  
TRUE on success, FALSE on no memory

Definition at line 717 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, dbus_malloc(), FALSE, DBusRealString::len, NULL, DBusRealString::str, and TRUE.

Referenced by \_dbus_split_paths_and_append(), \_dbus_transport_init_base(), and dbus_server_get_id().

## ◆ \_dbus_string_copy_len()

|                                    |     |                      |              |
|------------------------------------|-----|----------------------|--------------|
| dbus_bool_t \_dbus_string_copy_len | (   | const DBusString \*  | *source*,    |
|                                    |     | int                  | *start*,     |
|                                    |     | int                  | *len*,       |
|                                    |     | DBusString \*        | *dest*,      |
|                                    |     | int                  | *insert_at*  |
|                                    | )   |                      |              |

Like \_dbus_string_copy(), but can copy a segment from the middle of the source string.

Parameters  
|           |                                                    |
|-----------|----------------------------------------------------|
| source    | the source string                                  |
| start     | where to start copying the source string           |
| len       | length of segment to copy                          |
| dest      | the destination string                             |
| insert_at | where to place the copied segment of source string |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 1437 of file dbus-string.c.

References \_dbus_assert, and DBUS_STRING_COPY_PREAMBLE.

Referenced by \_dbus_header_load(), \_dbus_split_paths_and_append(), \_dbus_string_get_dirname(), \_dbus_variant_read(), and dbus_parse_address().

## ◆ \_dbus_string_copy_to_buffer()

|                                   |     |                      |              |
|-----------------------------------|-----|----------------------|--------------|
| void \_dbus_string_copy_to_buffer | (   | const DBusString \*  | *str*,       |
|                                   |     | char \*              | *buffer*,    |
|                                   |     | int                  | *avail_len*  |
|                                   | )   |                      |              |

Copies the contents of a DBusString into a different buffer.

It is a bug if avail_len is too short to hold the string contents. nul termination is not copied, just the supplied bytes.

Parameters  
|           |                            |
|-----------|----------------------------|
| str       | a string                   |
| buffer    | a C buffer to copy data to |
| avail_len | maximum length of C buffer |

Definition at line 742 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, DBusRealString::len, and DBusRealString::str.

Referenced by \_dbus_generate_random_bytes_buffer().

## ◆ \_dbus_string_copy_to_buffer_with_nul()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_string_copy_to_buffer_with_nul | ( | const DBusString \*  | *str*, |
|  |  | char \*  | *buffer*, |
|  |  | int  | *avail_len*  |
|  | ) |  |  |

Copies the contents of a DBusString into a different buffer.

It is a bug if avail_len is too short to hold the string contents plus a nul byte.

Parameters  
|           |                            |
|-----------|----------------------------|
| str       | a string                   |
| buffer    | a C buffer to copy data to |
| avail_len | maximum length of C buffer |

Definition at line 764 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, DBusRealString::len, and DBusRealString::str.

## ◆ \_dbus_string_delete()

|                           |     |                |          |
|---------------------------|-----|----------------|----------|
| void \_dbus_string_delete | (   | DBusString \*  | *str*,   |
|                           |     | int            | *start*, |
|                           |     | int            | *len*    |
|                           | )   |                |          |

Deletes a segment of a DBusString with length len starting at start.

(Hint: to clear an entire string, setting length to 0 with \_dbus_string_set_length() is easier.)

Parameters  
|       |                               |
|-------|-------------------------------|
| str   | the DBusString                |
| start | where to start deleting       |
| len   | the number of bytes to delete |

Definition at line 1255 of file dbus-string.c.

References \_dbus_assert, and DBUS_STRING_PREAMBLE.

Referenced by \_dbus_auth_bytes_sent(), \_dbus_header_create(), and \_dbus_string_chop_white().

## ◆ \_dbus_string_ends_with_c_str()

|                                           |     |                      |          |
|-------------------------------------------|-----|----------------------|----------|
| dbus_bool_t \_dbus_string_ends_with_c_str | (   | const DBusString \*  | *a*,     |
|                                           |     | const char \*        | *c_str*  |
|                                           | )   |                      |          |

Returns whether a string ends with the given suffix.

Parameters  
|       |                    |
|-------|--------------------|
| a     | the string         |
| c_str | the C-style string |

<!-- -->

Returns  
TRUE if the string ends with the suffix

Definition at line 54 of file dbus-string-util.c.

References \_dbus_assert, DBUS_GENERIC_STRING_PREAMBLE, FALSE, DBusRealString::len, NULL, DBusRealString::str, and TRUE.

Referenced by \_dbus_directory_open().

## ◆ \_dbus_string_equal()

|                                 |     |                      |      |
|---------------------------------|-----|----------------------|------|
| dbus_bool_t \_dbus_string_equal | (   | const DBusString \*  | *a*, |
|                                 |     | const DBusString \*  | *b*  |
|                                 | )   |                      |      |

Tests two DBusString for equality.

Parameters  
|     |               |
|-----|---------------|
| a   | first string  |
| b   | second string |

<!-- -->

Returns  
TRUE if equal

Definition at line 2075 of file dbus-string.c.

References DBUS_GENERIC_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::str, and TRUE.

Referenced by dbus_error_has_name().

## ◆ \_dbus_string_equal_c_str()

|                                       |     |                      |          |
|---------------------------------------|-----|----------------------|----------|
| dbus_bool_t \_dbus_string_equal_c_str | (   | const DBusString \*  | *a*,     |
|                                       |     | const char \*        | *c_str*  |
|                                       | )   |                      |          |

Checks whether a string is equal to a C string.

Parameters  
|       |              |
|-------|--------------|
| a     | the string   |
| c_str | the C string |

<!-- -->

Returns  
TRUE if equal

Definition at line 2214 of file dbus-string.c.

References \_dbus_assert, DBUS_GENERIC_STRING_PREAMBLE, FALSE, DBusRealString::len, NULL, DBusRealString::str, and TRUE.

Referenced by dbus_address_entry_get_value().

## ◆ \_dbus_string_equal_len()

|                                     |     |                      |        |
|-------------------------------------|-----|----------------------|--------|
| dbus_bool_t \_dbus_string_equal_len | (   | const DBusString \*  | *a*,   |
|                                     |     | const DBusString \*  | *b*,   |
|                                     |     | int                  | *len*  |
|                                     | )   |                      |        |

Tests two DBusString for equality up to the given length.

The strings may be shorter than the given length.

Parameters  
|     |                               |
|-----|-------------------------------|
| a   | first string                  |
| b   | second string                 |
| len | the maximum length to look at |

<!-- -->

Returns  
TRUE if equal for the given number of bytes

Definition at line 2118 of file dbus-string.c.

References DBUS_GENERIC_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::str, and TRUE.

## ◆ \_dbus_string_equal_substring()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_equal_substring | ( | const DBusString \*  | *a*, |
|  |  | int  | *a_start*, |
|  |  | int  | *a_len*, |
|  |  | const DBusString \*  | *b*, |
|  |  | int  | *b_start*  |
|  | ) |  |  |

Tests two sub-parts of two DBusString for equality.

The specified range of the first string must exist; the specified start position of the second string must exist.

Parameters  
|         |                                           |
|---------|-------------------------------------------|
| a       | first string                              |
| a_start | where to start substring in first string  |
| a_len   | length of substring in first string       |
| b       | second string                             |
| b_start | where to start substring in second string |

<!-- -->

Returns  
TRUE if the two substrings are equal

Definition at line 2166 of file dbus-string.c.

References \_dbus_assert, DBUS_GENERIC_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::str, and TRUE.

## ◆ \_dbus_string_find()

|                                |     |                      |           |
|--------------------------------|-----|----------------------|-----------|
| dbus_bool_t \_dbus_string_find | (   | const DBusString \*  | *str*,    |
|                                |     | int                  | *start*,  |
|                                |     | const char \*        | *substr*, |
|                                |     | int \*               | *found*   |
|                                | )   |                      |           |

Finds the given substring in the string, returning TRUE and filling in the byte index where the substring was found, if it was found.

Returns FALSE if the substring wasn't found. Sets \*start to the length of the string if the substring is not found.

Parameters  
|        |                                                 |
|--------|-------------------------------------------------|
| str    | the string                                      |
| start  | where to start looking                          |
| substr | the substring                                   |
| found  | return location for where it was found, or NULL |

<!-- -->

Returns  
TRUE if found

Definition at line 1666 of file dbus-string.c.

References \_dbus_string_find_to().

Referenced by \_dbus_keyring_validate_context(), \_dbus_resolve_pid_fd(), \_dbus_split_paths_and_append(), \_dbus_string_split_on_byte(), and dbus_parse_address().

## ◆ \_dbus_string_find_blank()

|                                      |     |                      |          |
|--------------------------------------|-----|----------------------|----------|
| dbus_bool_t \_dbus_string_find_blank | (   | const DBusString \*  | *str*,   |
|                                      |     | int                  | *start*, |
|                                      |     | int \*               | *found*  |
|                                      | )   |                      |          |

Finds a blank (space or tab) in the string.

Returns TRUE if found, FALSE otherwise. If a blank is not found sets \*found to the length of the string.

Parameters  
|       |                                                |
|-------|------------------------------------------------|
| str   | the string                                     |
| start | byte index to start looking                    |
| found | place to store the location of the first blank |

<!-- -->

Returns  
TRUE if a blank was found

Definition at line 1827 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::str, and TRUE.

Referenced by \_dbus_keyring_validate_context().

## ◆ \_dbus_string_find_byte_backward()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_find_byte_backward | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | unsigned char  | *byte*, |
|  |  | int \*  | *found*  |
|  | ) |  |  |

Find the given byte scanning backward from the given start.

Sets \*found to -1 if the byte is not found.

Parameters  
|       |                                                                    |
|-------|--------------------------------------------------------------------|
| str   | the string                                                         |
| start | the place to start scanning (will not find the byte at this point) |
| byte  | the byte to find                                                   |
| found | return location for where it was found                             |

<!-- -->

Returns  
TRUE if found

Definition at line 98 of file dbus-string-util.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, and NULL.

Referenced by \_dbus_string_get_dirname().

## ◆ \_dbus_string_find_eol()

|                                    |     |                      |              |
|------------------------------------|-----|----------------------|--------------|
| dbus_bool_t \_dbus_string_find_eol | (   | const DBusString \*  | *str*,       |
|                                    |     | int                  | *start*,     |
|                                    |     | int \*               | *found*,     |
|                                    |     | int \*               | *found_len*  |
|                                    | )   |                      |              |

Finds end of line ("\r\n" or "\n") in the string, returning TRUE and filling in the byte index where the eol string was found, if it was found.

Returns FALSE if eol wasn't found.

Parameters  
|  |  |
|----|----|
| str | the string |
| start | where to start looking |
| found | return location for where eol was found or string length otherwise |
| found_len | return length of found eol string or zero otherwise |

<!-- -->

Returns  
TRUE if found

Definition at line 1689 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::str, and TRUE.

Referenced by \_dbus_string_pop_line().

## ◆ \_dbus_string_find_to()

|                                   |     |                      |           |
|-----------------------------------|-----|----------------------|-----------|
| dbus_bool_t \_dbus_string_find_to | (   | const DBusString \*  | *str*,    |
|                                   |     | int                  | *start*,  |
|                                   |     | int                  | *end*,    |
|                                   |     | const char \*        | *substr*, |
|                                   |     | int \*               | *found*   |
|                                   | )   |                      |           |

Finds the given substring in the string, up to a certain position, returning TRUE and filling in the byte index where the substring was found, if it was found.

Returns FALSE if the substring wasn't found. Sets \*start to the length of the string if the substring is not found.

Parameters  
|        |                                                 |
|--------|-------------------------------------------------|
| str    | the string                                      |
| start  | where to start looking                          |
| end    | where to stop looking                           |
| substr | the substring                                   |
| found  | return location for where it was found, or NULL |

<!-- -->

Returns  
TRUE if found

Definition at line 1759 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, FALSE, NULL, DBusRealString::str, and TRUE.

Referenced by \_dbus_string_find(), and dbus_parse_address().

## ◆ \_dbus_string_free()

|                         |     |                |       |     |     |
|-------------------------|-----|----------------|-------|-----|-----|
| void \_dbus_string_free | (   | DBusString \*  | *str* | )   |     |

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_INIT_INVALID.

Unlike all other DBusString API, it is also valid to call this function for a string that was filled with \_DBUS_STRING_INIT_INVALID. This is convenient for error rollback.

Parameters  
|     |                                    |
|-----|------------------------------------|
| str | memory where the string is stored. |

Definition at line 278 of file dbus-string.c.

References DBusRealString::align_offset, DBusRealString::allocated, DBusRealString::constant, dbus_free(), DBUS_GENERIC_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::locked, NULL, DBusRealString::str, and DBusRealString::valid.

Referenced by \_dbus_append_keyring_directory_for_credentials(), \_dbus_auth_client_new(), \_dbus_auth_server_new(), \_dbus_auth_unref(), \_dbus_command_for_pid(), \_dbus_directory_open(), \_dbus_generate_random_bytes_buffer(), \_dbus_get_autolaunch_address(), \_dbus_get_standard_session_servicedirs(), \_dbus_hash_table_from_array(), \_dbus_hash_table_to_array(), \_dbus_header_copy(), \_dbus_header_free(), \_dbus_is_console_user(), \_dbus_keyring_new_for_credentials(), \_dbus_keyring_unref(), \_dbus_logv(), \_dbus_message_loader_unref(), \_dbus_read_credentials_socket(), \_dbus_replace_install_prefix(), \_dbus_resolve_pid_fd(), \_dbus_server_finalize_base(), \_dbus_server_init_base(), \_dbus_server_listen_platform_specific(), \_dbus_server_listen_unix_socket(), \_dbus_server_new_for_domain_socket(), \_dbus_server_new_for_launchd(), \_dbus_server_new_for_tcp_socket(), \_dbus_set_up_transient_session_servicedirs(), \_dbus_sha_compute(), \_dbus_split_paths_and_append(), \_dbus_string_hex_decode(), \_dbus_string_hex_encode(), \_dbus_string_init_from_string(), \_dbus_string_save_to_file(), \_dbus_transport_new_for_domain_socket(), \_dbus_transport_new_for_socket(), \_dbus_transport_new_for_tcp_socket(), \_dbus_transport_open_platform_specific(), \_dbus_variant_read(), \_dbus_write_pid_to_file_and_pipe(), \_dbus_write_uuid_file(), dbus_address_escape_value(), dbus_address_unescape_value(), dbus_connection_dispatch(), dbus_message_copy(), dbus_message_demarshal_bytes_needed(), dbus_message_iter_get_signature(), dbus_message_marshal(), dbus_message_new_error_printf(), dbus_parse_address(), dbus_signature_iter_get_signature(), and dbus_try_get_local_machine_id().

## ◆ \_dbus_string_get_allocated_size()

|                                      |     |                      |       |     |     |
|--------------------------------------|-----|----------------------|-------|-----|-----|
| int \_dbus_string_get_allocated_size | (   | const DBusString \*  | *str* | )   |     |

Returns the allocated size of the string.

Parameters  
|     |            |
|-----|------------|
| str | the string |

<!-- -->

Returns  
the allocated size

Definition at line 476 of file dbus-string.c.

References DBusRealString::allocated, and DBUS_CONST_STRING_PREAMBLE.

## ◆ \_dbus_string_get_byte()

|                                      |     |                      |          |
|--------------------------------------|-----|----------------------|----------|
| unsigned char \_dbus_string_get_byte | (   | const DBusString \*  | *str*,   |
|                                      |     | int                  | *start*  |
|                                      | )   |                      |          |

Gets the byte at the given position.

It is allowed to ask for the nul byte at the end of the string.

Parameters  
|       |              |
|-------|--------------|
| str   | the string   |
| start | the position |

<!-- -->

Returns  
the byte at that position

Definition at line 607 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, and DBusRealString::str.

Referenced by \_dbus_concat_dir_and_file(), \_dbus_first_type_in_signature(), \_dbus_generate_random_ascii(), \_dbus_header_get_byte_order(), \_dbus_header_get_message_type(), \_dbus_header_have_message_untrusted(), \_dbus_marshal_read_basic(), \_dbus_marshal_skip_basic(), \_dbus_path_is_absolute(), \_dbus_replace_install_prefix(), \_dbus_resolve_pid_fd(), \_dbus_string_get_dirname(), \_dbus_string_hex_decode(), and \_dbus_variant_get_signature().

## ◆ \_dbus_string_get_const_data()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| const char \* \_dbus_string_get_const_data | ( | const DBusString \*  | *str* | ) |  |

Gets the raw character buffer from a const string.

Parameters  
|     |            |
|-----|------------|
| str | the string |

<!-- -->

Returns  
the string data

Definition at line 513 of file dbus-string.c.

References DBUS_CONST_STRING_PREAMBLE, and DBusRealString::str.

Referenced by \_dbus_append_keyring_directory_for_credentials(), \_dbus_auth_bytes_sent(), \_dbus_auth_get_guid_from_server(), \_dbus_check_dir_is_private_to_user(), \_dbus_command_for_pid(), \_dbus_create_directory(), \_dbus_create_file_exclusively(), \_dbus_credentials_add_from_user(), \_dbus_delete_directory(), \_dbus_delete_file(), \_dbus_directory_open(), \_dbus_ensure_directory(), \_dbus_file_get_contents(), \_dbus_get_autolaunch_address(), \_dbus_get_standard_session_servicedirs(), \_dbus_listen_tcp_socket(), \_dbus_logv(), \_dbus_make_file_world_readable(), \_dbus_marshal_read_basic(), \_dbus_server_listen_unix_socket(), \_dbus_server_new_for_tcp_socket(), \_dbus_sha_update(), \_dbus_stat(), \_dbus_string_hex_decode(), \_dbus_string_hex_encode(), \_dbus_string_init_from_string(), \_dbus_string_save_to_file(), \_dbus_string_starts_with_words_c_str(), \_dbus_transport_open_platform_specific(), \_dbus_user_database_lookup(), \_dbus_user_database_lookup_group(), \_dbus_write_pid_to_file_and_pipe(), dbus_address_entry_get_method(), dbus_address_entry_get_value(), dbus_connection_dispatch(), dbus_message_iter_get_signature(), and dbus_message_new_error_printf().

## ◆ \_dbus_string_get_const_data_len()

|  |  |  |  |
|----|----|----|----|
| const char \* \_dbus_string_get_const_data_len | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | int  | *len*  |
|  | ) |  |  |

const version of \_dbus_string_get_data_len().

Parameters  
|       |                             |
|-------|-----------------------------|
| str   | the string                  |
| start | byte offset to return       |
| len   | length of segment to return |

<!-- -->

Returns  
the string data

Definition at line 559 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, and DBusRealString::str.

Referenced by \_dbus_string_parse_int(), \_dbus_string_parse_int64(), \_dbus_string_parse_uint(), \_dbus_type_reader_init(), \_dbus_type_reader_init_types_only(), \_dbus_type_reader_next(), \_dbus_type_reader_read_basic(), \_dbus_type_reader_read_fixed_multi(), \_dbus_type_reader_recurse(), \_dbus_type_reader_set_basic(), \_dbus_type_writer_init(), \_dbus_type_writer_unrecurse(), \_dbus_validate_body_with_reason(), \_dbus_variant_get_signature(), \_dbus_verbose_bytes_of_string(), \_dbus_write(), \_dbus_write_socket(), \_dbus_write_socket_two(), \_dbus_write_two(), and dbus_message_get_signature().

## ◆ \_dbus_string_get_data()

|                                |     |                |       |     |     |
|--------------------------------|-----|----------------|-------|-----|-----|
| char \* \_dbus_string_get_data | (   | DBusString \*  | *str* | )   |     |

Gets the raw character buffer from the string.

The returned buffer will be nul-terminated, but note that strings may contain binary data so there may be extra nul characters prior to the termination. This function should be little-used, extend DBusString or add stuff to dbus-sysdeps.c instead. It's an error to use this function on a const string.

Parameters  
|     |            |
|-----|------------|
| str | the string |

<!-- -->

Returns  
the data

Definition at line 496 of file dbus-string.c.

References DBUS_STRING_PREAMBLE, and DBusRealString::str.

Referenced by \_dbus_get_autolaunch_address().

## ◆ \_dbus_string_get_data_len()

|                                    |     |                |          |
|------------------------------------|-----|----------------|----------|
| char \* \_dbus_string_get_data_len | (   | DBusString \*  | *str*,   |
|                                    |     | int            | *start*, |
|                                    |     | int            | *len*    |
|                                    | )   |                |          |

Gets a sub-portion of the raw character buffer from the string.

The "len" field is required simply for error checking, to be sure you don't try to use more string than exists. The nul termination of the returned buffer remains at the end of the entire string, not at start + len.

Parameters  
|       |                             |
|-------|-----------------------------|
| str   | the string                  |
| start | byte offset to return       |
| len   | length of segment to return |

<!-- -->

Returns  
the string data

Definition at line 535 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_PREAMBLE, and DBusRealString::str.

Referenced by \_dbus_generate_random_bytes(), \_dbus_read(), \_dbus_read_socket(), and \_dbus_read_socket_with_unix_fds().

## ◆ \_dbus_string_get_dirname()

|                                       |     |                      |             |
|---------------------------------------|-----|----------------------|-------------|
| dbus_bool_t \_dbus_string_get_dirname | (   | const DBusString \*  | *filename*, |
|                                       |     | DBusString \*        | *dirname*   |
|                                       | )   |                      |             |

Get the directory name from a complete filename.

Parameters  
|          |                                    |
|----------|------------------------------------|
| filename | the filename                       |
| dirname  | string to append directory name to |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1018 of file dbus-sysdeps-util-unix.c.

References \_dbus_assert, \_dbus_string_append(), \_dbus_string_copy_len(), \_dbus_string_find_byte_backward(), \_dbus_string_get_byte(), \_dbus_string_get_length(), and NULL.

## ◆ \_dbus_string_get_length()

|                              |     |                      |       |     |     |
|------------------------------|-----|----------------------|-------|-----|-----|
| int \_dbus_string_get_length | (   | const DBusString \*  | *str* | )   |     |

Gets the length of a string (not including nul termination).

Returns  
the length.

Definition at line 784 of file dbus-string.c.

References DBUS_CONST_STRING_PREAMBLE, and DBusRealString::len.

Referenced by \_dbus_address_append_escaped(), \_dbus_append_keyring_directory_for_credentials(), \_dbus_auth_decode_data(), \_dbus_auth_do_work(), \_dbus_auth_encode_data(), \_dbus_auth_get_bytes_to_send(), \_dbus_auth_set_context(), \_dbus_command_for_pid(), \_dbus_concat_dir_and_file(), \_dbus_file_get_contents(), \_dbus_generate_random_ascii(), \_dbus_generate_random_bytes(), \_dbus_get_autolaunch_address(), \_dbus_get_session_config_file(), \_dbus_get_system_config_file(), \_dbus_header_copy(), \_dbus_header_create(), \_dbus_header_get_byte_order(), \_dbus_header_load(), \_dbus_is_a_number(), \_dbus_keyring_get_hex_key(), \_dbus_keyring_validate_context(), \_dbus_listen_tcp_socket(), \_dbus_lookup_launchd_socket(), \_dbus_marshal_byteswap(), \_dbus_marshal_read_uint32(), \_dbus_marshal_skip_array(), \_dbus_marshal_skip_basic(), \_dbus_message_add_counter_link(), \_dbus_message_loader_get_buffer(), \_dbus_message_loader_queue_messages(), \_dbus_path_is_absolute(), \_dbus_read(), \_dbus_read_socket(), \_dbus_read_socket_with_unix_fds(), \_dbus_replace_install_prefix(), \_dbus_sha_compute(), \_dbus_sha_update(), \_dbus_split_paths_and_append(), \_dbus_string_append_byte_as_hex(), \_dbus_string_chop_white(), \_dbus_string_get_dirname(), \_dbus_string_hex_decode(), \_dbus_string_hex_encode(), \_dbus_string_parse_int(), \_dbus_string_parse_int64(), \_dbus_string_parse_uint(), \_dbus_string_pop_line(), \_dbus_string_save_to_file(), \_dbus_string_split_on_byte(), \_dbus_type_reader_set_basic(), \_dbus_uuid_encode(), \_dbus_validate_body_with_reason(), \_dbus_validate_interface(), \_dbus_validate_member(), \_dbus_validate_path(), \_dbus_verbose_bytes_of_string(), \_dbus_write_pid_to_file_and_pipe(), dbus_address_unescape_value(), dbus_message_copy(), dbus_message_iter_append_basic(), dbus_message_iter_init_append(), dbus_message_iter_open_container(), dbus_message_lock(), dbus_message_marshal(), dbus_parse_address(), dbus_signature_validate(), dbus_validate_bus_name(), dbus_validate_error_name(), dbus_validate_interface(), dbus_validate_member(), dbus_validate_path(), and dbus_validate_utf8().

## ◆ \_dbus_string_hex_decode()

|                                      |     |                      |               |
|--------------------------------------|-----|----------------------|---------------|
| dbus_bool_t \_dbus_string_hex_decode | (   | const DBusString \*  | *source*,     |
|                                      |     | int                  | *start*,      |
|                                      |     | int \*               | *end_return*, |
|                                      |     | DBusString \*        | *dest*,       |
|                                      |     | int                  | *insert_at*   |
|                                      | )   |                      |               |

Decodes a string from hex encoding.

Parameters  
|            |                                                     |
|------------|-----------------------------------------------------|
| source     | the string to decode                                |
| start      | byte index to start decode                          |
| end_return | return location of the end of the hex data, or NULL |
| dest       | string where decoded data should be placed          |
| insert_at  | where to place decoded data                         |

<!-- -->

Returns  
TRUE if decoding was successful, FALSE if no memory.

Definition at line 2432 of file dbus-string.c.

References \_dbus_assert, \_dbus_string_append_byte(), \_dbus_string_free(), \_dbus_string_get_byte(), \_dbus_string_get_const_data(), \_dbus_string_get_length(), \_dbus_string_init(), \_dbus_string_move(), \_dbus_string_set_byte(), FALSE, and TRUE.

## ◆ \_dbus_string_hex_encode()

|                                      |     |                      |              |
|--------------------------------------|-----|----------------------|--------------|
| dbus_bool_t \_dbus_string_hex_encode | (   | const DBusString \*  | *source*,    |
|                                      |     | int                  | *start*,     |
|                                      |     | DBusString \*        | *dest*,      |
|                                      |     | int                  | *insert_at*  |
|                                      | )   |                      |              |

Encodes a string in hex, the way MD5 and SHA-1 are usually encoded.

(Each byte is two hex digits.)

Parameters  
|           |                                            |
|-----------|--------------------------------------------|
| source    | the string to encode                       |
| start     | byte index to start encoding               |
| dest      | string where encoded data should be placed |
| insert_at | where to place encoded data                |

<!-- -->

Returns  
TRUE if encoding was successful, FALSE if no memory etc.

Definition at line 2382 of file dbus-string.c.

References \_dbus_assert, \_dbus_string_append_byte_as_hex(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_get_length(), \_dbus_string_init(), \_dbus_string_move(), FALSE, and TRUE.

Referenced by \_dbus_keyring_get_hex_key(), \_dbus_sha_compute(), and \_dbus_uuid_encode().

## ◆ \_dbus_string_init()

|                                |     |                |       |     |     |
|--------------------------------|-----|----------------|-------|-----|-----|
| dbus_bool_t \_dbus_string_init | (   | DBusString \*  | *str* | )   |     |

Initializes a string.

The string starts life with zero length. The string must eventually be freed with \_dbus_string_free().

Parameters  
|     |                           |
|-----|---------------------------|
| str | memory to hold the string |

<!-- -->

Returns  
TRUE on success, FALSE if no memory

Definition at line 182 of file dbus-string.c.

References \_dbus_string_init_preallocated().

Referenced by \_dbus_append_keyring_directory_for_credentials(), \_dbus_auth_client_new(), \_dbus_auth_server_new(), \_dbus_command_for_pid(), \_dbus_generate_random_bytes_buffer(), \_dbus_get_autolaunch_address(), \_dbus_get_standard_session_servicedirs(), \_dbus_hash_table_from_array(), \_dbus_hash_table_to_array(), \_dbus_is_console_user(), \_dbus_keyring_new_for_credentials(), \_dbus_logv(), \_dbus_message_loader_new(), \_dbus_read_credentials_socket(), \_dbus_replace_install_prefix(), \_dbus_resolve_pid_fd(), \_dbus_server_init_base(), \_dbus_server_listen_platform_specific(), \_dbus_server_listen_unix_socket(), \_dbus_server_new_for_domain_socket(), \_dbus_server_new_for_launchd(), \_dbus_server_new_for_tcp_socket(), \_dbus_set_up_transient_session_servicedirs(), \_dbus_sha_compute(), \_dbus_split_paths_and_append(), \_dbus_string_hex_decode(), \_dbus_string_hex_encode(), \_dbus_string_init_from_string(), \_dbus_string_save_to_file(), \_dbus_string_steal_data(), \_dbus_transport_new_for_domain_socket(), \_dbus_transport_new_for_socket(), \_dbus_transport_new_for_tcp_socket(), \_dbus_transport_open_platform_specific(), \_dbus_variant_read(), \_dbus_write_pid_to_file_and_pipe(), \_dbus_write_uuid_file(), dbus_address_escape_value(), dbus_address_unescape_value(), dbus_connection_dispatch(), dbus_message_iter_get_signature(), dbus_message_marshal(), dbus_message_new_error_printf(), dbus_parse_address(), dbus_signature_iter_get_signature(), and dbus_try_get_local_machine_id().

## ◆ \_dbus_string_init_const()

|                               |     |                |          |
|-------------------------------|-----|----------------|----------|
| void \_dbus_string_init_const | (   | DBusString \*  | *str*,   |
|                               |     | const char \*  | *value*  |
|                               | )   |                |          |

Initializes a constant string.

The value parameter is not copied (should be static), and the string may never be modified. It is safe but not necessary to call \_dbus_string_free() on a const string. The string has a length limit of MAXINT - 8.

Parameters  
|       |                                              |
|-------|----------------------------------------------|
| str   | memory to use for the string                 |
| value | a string to be stored in str (not copied!!!) |

Definition at line 197 of file dbus-string.c.

References \_dbus_assert, \_dbus_string_init_const_len(), and NULL.

Referenced by \_dbus_append_address_from_socket(), \_dbus_append_keyring_directory_for_credentials(), \_dbus_change_to_daemon_user(), \_dbus_get_local_system_servicedirs(), \_dbus_get_standard_session_servicedirs(), \_dbus_get_standard_system_servicedirs(), \_dbus_get_uuid(), \_dbus_read_local_machine_uuid(), \_dbus_server_listen_unix_socket(), \_dbus_server_new_for_domain_socket(), \_dbus_server_new_for_tcp_socket(), \_dbus_split_paths_and_append(), \_dbus_transport_new_for_domain_socket(), \_dbus_variant_read(), \_dbus_variant_write(), \_dbus_verify_daemon_user(), dbus_address_escape_value(), dbus_address_unescape_value(), dbus_error_has_name(), dbus_message_iter_append_basic(), dbus_message_iter_open_container(), dbus_parse_address(), dbus_signature_validate(), dbus_validate_bus_name(), dbus_validate_error_name(), dbus_validate_interface(), dbus_validate_member(), dbus_validate_path(), and dbus_validate_utf8().

## ◆ \_dbus_string_init_const_len()

|                                   |     |                |          |
|-----------------------------------|-----|----------------|----------|
| void \_dbus_string_init_const_len | (   | DBusString \*  | *str*,   |
|                                   |     | const char \*  | *value*, |
|                                   |     | int            | *len*    |
|                                   | )   |                |          |

Initializes a constant string with a length.

The value parameter is not copied (should be static), and the string may never be modified. It is safe but not necessary to call \_dbus_string_free() on a const string.

Parameters  
|       |                                              |
|-------|----------------------------------------------|
| str   | memory to use for the string                 |
| value | a string to be stored in str (not copied!!!) |
| len   | the length to use                            |

Definition at line 217 of file dbus-string.c.

References \_dbus_assert, \_DBUS_STRING_MAX_LENGTH, DBusRealString::align_offset, DBusRealString::allocated, DBusRealString::constant, DBusRealString::len, DBusRealString::locked, NULL, DBusRealString::str, TRUE, and DBusRealString::valid.

Referenced by \_dbus_send_credentials_socket(), \_dbus_string_init_const(), \_dbus_uuid_encode(), and dbus_message_demarshal_bytes_needed().

## ◆ \_dbus_string_init_from_string()

|                                            |     |                      |         |
|--------------------------------------------|-----|----------------------|---------|
| dbus_bool_t \_dbus_string_init_from_string | (   | DBusString \*        | *str*,  |
|                                            |     | const DBusString \*  | *from*  |
|                                            | )   |                      |         |

Initializes a string from another string.

The string must be freed with \_dbus_string_free() in case of success. In case of error the string is freed by this function itself.

Parameters  
|      |                                               |
|------|-----------------------------------------------|
| str  | memory to hold the string                     |
| from | instance from which the string is initialized |

<!-- -->

Returns  
TRUE on success, FALSE if no memory

Definition at line 254 of file dbus-string.c.

References \_dbus_string_append(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_init(), FALSE, and TRUE.

Referenced by \_dbus_directory_open().

## ◆ \_dbus_string_init_preallocated()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_init_preallocated | ( | DBusString \*  | *str*, |
|  |  | int  | *allocate_size*  |
|  | ) |  |  |

Initializes a string that can be up to the given allocation size before it has to realloc.

The string starts life with zero length. The string must eventually be freed with \_dbus_string_free().

Parameters  
|               |                           |
|---------------|---------------------------|
| str           | memory to hold the string |
| allocate_size | amount to preallocate     |

<!-- -->

Returns  
TRUE on success, FALSE if no memory

Definition at line 139 of file dbus-string.c.

References \_dbus_assert, DBusRealString::align_offset, DBusRealString::allocated, DBusRealString::constant, dbus_malloc(), FALSE, DBusRealString::len, DBusRealString::locked, NULL, DBusRealString::str, TRUE, and DBusRealString::valid.

Referenced by \_dbus_header_copy(), \_dbus_header_init(), \_dbus_string_init(), and dbus_message_copy().

## ◆ \_dbus_string_insert_2_aligned()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_insert_2_aligned | ( | DBusString \*  | *str*, |
|  |  | int  | *insert_at*, |
|  |  | const unsigned char  | *octets*\[2\]  |
|  | ) |  |  |

Inserts 2 bytes aligned on a 2 byte boundary with any alignment padding initialized to 0.

Parameters  
|           |                   |
|-----------|-------------------|
| str       | the DBusString    |
| insert_at | where to insert   |
| octets    | 2 bytes to insert |

<!-- -->

Returns  
FALSE if not enough memory.

Definition at line 1005 of file dbus-string.c.

References DBUS_STRING_PREAMBLE, FALSE, DBusRealString::str, and TRUE.

## ◆ \_dbus_string_insert_4_aligned()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_insert_4_aligned | ( | DBusString \*  | *str*, |
|  |  | int  | *insert_at*, |
|  |  | const unsigned char  | *octets*\[4\]  |
|  | ) |  |  |

Inserts 4 bytes aligned on a 4 byte boundary with any alignment padding initialized to 0.

Parameters  
|           |                   |
|-----------|-------------------|
| str       | the DBusString    |
| insert_at | where to insert   |
| octets    | 4 bytes to insert |

<!-- -->

Returns  
FALSE if not enough memory.

Definition at line 1029 of file dbus-string.c.

References DBUS_STRING_PREAMBLE, FALSE, DBusRealString::str, and TRUE.

## ◆ \_dbus_string_insert_8_aligned()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_insert_8_aligned | ( | DBusString \*  | *str*, |
|  |  | int  | *insert_at*, |
|  |  | const unsigned char  | *octets*\[8\]  |
|  | ) |  |  |

Inserts 8 bytes aligned on an 8 byte boundary with any alignment padding initialized to 0.

Parameters  
|           |                   |
|-----------|-------------------|
| str       | the DBusString    |
| insert_at | where to insert   |
| octets    | 8 bytes to insert |

<!-- -->

Returns  
FALSE if not enough memory.

Definition at line 1053 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_PREAMBLE, FALSE, DBusRealString::str, and TRUE.

## ◆ \_dbus_string_insert_alignment()

|                                            |     |                |              |
|--------------------------------------------|-----|----------------|--------------|
| dbus_bool_t \_dbus_string_insert_alignment | (   | DBusString \*  | *str*,       |
|                                            |     | int \*         | *insert_at*, |
|                                            |     | int            | *alignment*  |
|                                            | )   |                |              |

Inserts padding at \*insert_at such to align it to the given boundary.

Initializes the padding to nul bytes. Sets \*insert_at to the aligned position.

Parameters  
|           |                                    |
|-----------|------------------------------------|
| str       | the DBusString                     |
| insert_at | location to be aligned             |
| alignment | alignment boundary (1, 2, 4, or 8) |

<!-- -->

Returns  
FALSE if not enough memory.

Definition at line 1081 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_PREAMBLE, FALSE, and TRUE.

## ◆ \_dbus_string_insert_byte()

|                                       |     |                |         |
|---------------------------------------|-----|----------------|---------|
| dbus_bool_t \_dbus_string_insert_byte | (   | DBusString \*  | *str*,  |
|                                       |     | int            | *i*,    |
|                                       |     | unsigned char  | *byte*  |
|                                       | )   |                |         |

Inserts a single byte at the given position.

Parameters  
|      |                     |
|------|---------------------|
| str  | the string          |
| i    | the position        |
| byte | the value to insert |

<!-- -->

Returns  
TRUE on success

Definition at line 659 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_PREAMBLE, FALSE, DBusRealString::str, and TRUE.

Referenced by \_dbus_marshal_write_basic().

## ◆ \_dbus_string_insert_bytes()

|                                        |     |                |            |
|----------------------------------------|-----|----------------|------------|
| dbus_bool_t \_dbus_string_insert_bytes | (   | DBusString \*  | *str*,     |
|                                        |     | int            | *i*,       |
|                                        |     | int            | *n_bytes*, |
|                                        |     | unsigned char  | *byte*     |
|                                        | )   |                |            |

Inserts a number of bytes of a given value at the given position.

Parameters  
|         |                     |
|---------|---------------------|
| str     | the string          |
| i       | the position        |
| n_bytes | number of bytes     |
| byte    | the value to insert |

<!-- -->

Returns  
TRUE on success

Definition at line 629 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_PREAMBLE, FALSE, DBusRealString::str, and TRUE.

## ◆ \_dbus_string_lengthen()

|                                    |     |                |                      |
|------------------------------------|-----|----------------|----------------------|
| dbus_bool_t \_dbus_string_lengthen | (   | DBusString \*  | *str*,               |
|                                    |     | int            | *additional_length*  |
|                                    | )   |                |                      |

Makes a string longer by the given number of bytes.

Checks whether adding additional_length to the current length would overflow an integer, and checks for exceeding a string's max length. The new bytes are not initialized, other than nul-terminating the end of the string. The uninitialized bytes may contain nul bytes or other junk.

Parameters  
|                   |                              |
|-------------------|------------------------------|
| str               | a string                     |
| additional_length | length to add to the string. |

<!-- -->

Returns  
TRUE on success.

Definition at line 805 of file dbus-string.c.

References \_dbus_assert, \_DBUS_STRING_MAX_LENGTH, DBUS_STRING_PREAMBLE, FALSE, and DBusRealString::len.

Referenced by \_dbus_generate_random_bytes(), \_dbus_read(), \_dbus_read_socket(), \_dbus_read_socket_with_unix_fds(), \_dbus_string_alloc_space(), and \_dbus_string_append_printf_valist().

## ◆ \_dbus_string_move()

|                                |     |                |              |
|--------------------------------|-----|----------------|--------------|
| dbus_bool_t \_dbus_string_move | (   | DBusString \*  | *source*,    |
|                                |     | int            | *start*,     |
|                                |     | DBusString \*  | *dest*,      |
|                                |     | int            | *insert_at*  |
|                                | )   |                |              |

Moves the end of one string into another string.

Both strings must be initialized, valid strings.

Parameters  
|           |                                                     |
|-----------|-----------------------------------------------------|
| source    | the source string                                   |
| start     | where to chop off the source string                 |
| dest      | the destination string                              |
| insert_at | where to move the chopped-off part of source string |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 1321 of file dbus-string.c.

References \_dbus_assert, \_dbus_string_move_len(), and DBusRealString::len.

Referenced by \_dbus_string_hex_decode(), and \_dbus_string_hex_encode().

## ◆ \_dbus_string_move_len()

|                                    |     |                |              |
|------------------------------------|-----|----------------|--------------|
| dbus_bool_t \_dbus_string_move_len | (   | DBusString \*  | *source*,    |
|                                    |     | int            | *start*,     |
|                                    |     | int            | *len*,       |
|                                    |     | DBusString \*  | *dest*,      |
|                                    |     | int            | *insert_at*  |
|                                    | )   |                |              |

Like \_dbus_string_move(), but can move a segment from the middle of the source string.

Parameters  
|           |                                                |
|-----------|------------------------------------------------|
| source    | the source string                              |
| start     | first byte of source string to move            |
| len       | length of segment to move                      |
| dest      | the destination string                         |
| insert_at | where to move the bytes from the source string |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 1370 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_COPY_PREAMBLE, FALSE, and TRUE.

Referenced by \_dbus_string_move(), \_dbus_string_pop_line(), and \_dbus_string_split_on_byte().

## ◆ \_dbus_string_parse_int()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_parse_int | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | long \*  | *value_return*, |
|  |  | int \*  | *end_return*  |
|  | ) |  |  |

Parses an integer contained in a DBusString.

Either return parameter may be NULL if you aren't interested in it. The integer is parsed and stored in value_return. Return parameters are not initialized if the function returns FALSE.

Parameters  
|              |                                                    |
|--------------|----------------------------------------------------|
| str          | the string                                         |
| start        | the byte index of the start of the integer         |
| value_return | return location of the integer value or NULL       |
| end_return   | return location of the end of the integer, or NULL |

<!-- -->

Returns  
TRUE on success

Definition at line 371 of file dbus-sysdeps.c.

References \_dbus_set_errno_to_zero(), \_dbus_string_get_const_data_len(), \_dbus_string_get_length(), FALSE, NULL, and TRUE.

## ◆ \_dbus_string_parse_int64()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_parse_int64 | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | dbus_int64_t \*  | *value_return*, |
|  |  | int \*  | *end_return*  |
|  | ) |  |  |

Parses a dbus_int64_t integer contained in a DBusString.

Either return parameter may be NULL if you aren't interested in it. The integer is parsed and stored in value_return. Return parameters are not initialized if the function returns FALSE.

Parameters  
|              |                                                    |
|--------------|----------------------------------------------------|
| str          | the string                                         |
| start        | the byte index of the start of the integer         |
| value_return | return location of the integer value or NULL       |
| end_return   | return location of the end of the integer, or NULL |

<!-- -->

Returns  
TRUE on success

Definition at line 449 of file dbus-sysdeps.c.

References \_dbus_set_errno_to_zero(), \_dbus_string_get_const_data_len(), \_dbus_string_get_length(), FALSE, NULL, and TRUE.

## ◆ \_dbus_string_parse_uint()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_parse_uint | ( | const DBusString \*  | *str*, |
|  |  | int  | *start*, |
|  |  | unsigned long \*  | *value_return*, |
|  |  | int \*  | *end_return*  |
|  | ) |  |  |

Parses an unsigned integer contained in a DBusString.

Either return parameter may be NULL if you aren't interested in it. The integer is parsed and stored in value_return. Return parameters are not initialized if the function returns FALSE.

Parameters  
|              |                                                    |
|--------------|----------------------------------------------------|
| str          | the string                                         |
| start        | the byte index of the start of the integer         |
| value_return | return location of the integer value or NULL       |
| end_return   | return location of the end of the integer, or NULL |

<!-- -->

Returns  
TRUE on success

Definition at line 410 of file dbus-sysdeps.c.

References \_dbus_set_errno_to_zero(), \_dbus_string_get_const_data_len(), \_dbus_string_get_length(), FALSE, NULL, and TRUE.

Referenced by \_dbus_is_a_number(), and \_dbus_resolve_pid_fd().

## ◆ \_dbus_string_pop_line()

|                                    |     |                |           |
|------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_string_pop_line | (   | DBusString \*  | *source*, |
|                                    |     | DBusString \*  | *dest*    |
|                                    | )   |                |           |

Assigns a newline-terminated or \r\n-terminated line from the front of the string to the given dest string.

The dest string's previous contents are deleted. If the source string contains no newline, moves the entire source string to the dest string.

Parameters  
|        |                                                |
|--------|------------------------------------------------|
| source | the source string                              |
| dest   | the destination string (contents are replaced) |

<!-- -->

Returns  
FALSE if no memory, or source has length 0

Definition at line 1971 of file dbus-string.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_string_find_eol(), \_dbus_string_get_length(), \_dbus_string_move_len(), \_dbus_string_set_length(), FALSE, and TRUE.

## ◆ \_dbus_string_replace_len()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_replace_len | ( | const DBusString \*  | *source*, |
|  |  | int  | *start*, |
|  |  | int  | *len*, |
|  |  | DBusString \*  | *dest*, |
|  |  | int  | *replace_at*, |
|  |  | int  | *replace_len*  |
|  | ) |  |  |

Replaces a segment of dest string with a segment of source string.

Parameters  
|             |                                             |
|-------------|---------------------------------------------|
| source      | the source string                           |
| start       | where to start copying the source string    |
| len         | length of segment to copy                   |
| dest        | the destination string                      |
| replace_at  | start of segment of dest string to replace  |
| replace_len | length of segment of dest string to replace |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 1466 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_COPY_PREAMBLE, FALSE, and TRUE.

Referenced by \_dbus_auth_set_context(), and \_dbus_replace_install_prefix().

## ◆ \_dbus_string_set_byte()

|                             |     |                |         |
|-----------------------------|-----|----------------|---------|
| void \_dbus_string_set_byte | (   | DBusString \*  | *str*,  |
|                             |     | int            | *i*,    |
|                             |     | unsigned char  | *byte*  |
|                             | )   |                |         |

Sets the value of the byte at the given position.

Parameters  
|      |               |
|------|---------------|
| str  | the string    |
| i    | the position  |
| byte | the new value |

Definition at line 583 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_PREAMBLE, and DBusRealString::str.

Referenced by \_dbus_generate_random_ascii(), \_dbus_header_byteswap(), \_dbus_marshal_set_basic(), \_dbus_replace_install_prefix(), and \_dbus_string_hex_decode().

## ◆ \_dbus_string_set_length()

|                                      |     |                |           |
|--------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_string_set_length | (   | DBusString \*  | *str*,    |
|                                      |     | int            | *length*  |
|                                      | )   |                |           |

Sets the length of a string.

Can be used to truncate or lengthen the string. If the string is lengthened, the function may fail and return FALSE. Newly-added bytes are not initialized, as with \_dbus_string_lengthen().

Parameters  
|        |                           |
|--------|---------------------------|
| str    | a string                  |
| length | new length of the string. |

<!-- -->

Returns  
FALSE on failure.

Definition at line 847 of file dbus-string.c.

References \_dbus_assert, and DBUS_STRING_PREAMBLE.

Referenced by \_dbus_address_append_escaped(), \_dbus_append_keyring_directory_for_credentials(), \_dbus_auth_delete_unused_bytes(), \_dbus_directory_get_next_file(), \_dbus_file_get_contents(), \_dbus_generate_random_bytes(), \_dbus_hash_table_from_array(), \_dbus_header_load(), \_dbus_header_reinit(), \_dbus_message_loader_new(), \_dbus_read(), \_dbus_read_socket(), \_dbus_read_socket_with_unix_fds(), \_dbus_string_append_byte_as_hex(), \_dbus_string_chop_white(), \_dbus_string_pop_line(), and \_dbus_string_split_on_byte().

## ◆ \_dbus_string_shorten()

|                            |     |                |                     |
|----------------------------|-----|----------------|---------------------|
| void \_dbus_string_shorten | (   | DBusString \*  | *str*,              |
|                            |     | int            | *length_to_remove*  |
|                            | )   |                |                     |

Makes a string shorter by the given number of bytes.

Parameters  
|                  |                                   |
|------------------|-----------------------------------|
| str              | a string                          |
| length_to_remove | length to remove from the string. |

Definition at line 825 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_PREAMBLE, and DBusRealString::len.

Referenced by \_dbus_concat_dir_and_file(), \_dbus_lookup_launchd_socket(), and \_dbus_string_alloc_space().

## ◆ \_dbus_string_skip_blank()

|                               |     |                      |          |
|-------------------------------|-----|----------------------|----------|
| void \_dbus_string_skip_blank | (   | const DBusString \*  | *str*,   |
|                               |     | int                  | *start*, |
|                               |     | int \*               | *end*    |
|                               | )   |                      |          |

Skips blanks from start, storing the first non-blank in \*end (blank is space or tab).

Parameters  
|       |                                               |
|-------|-----------------------------------------------|
| str   | the string                                    |
| start | where to start                                |
| end   | where to store the first non-blank byte index |

Definition at line 1865 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, DBUS_IS_ASCII_BLANK, DBusRealString::len, and DBusRealString::str.

## ◆ \_dbus_string_skip_white()

|                               |     |                      |          |
|-------------------------------|-----|----------------------|----------|
| void \_dbus_string_skip_white | (   | const DBusString \*  | *str*,   |
|                               |     | int                  | *start*, |
|                               |     | int \*               | *end*    |
|                               | )   |                      |          |

Skips whitespace from start, storing the first non-whitespace in \*end.

(whitespace is space, tab, newline, CR).

Parameters  
|       |                                                    |
|-------|----------------------------------------------------|
| str   | the string                                         |
| start | where to start                                     |
| end   | where to store the first non-whitespace byte index |

Definition at line 1899 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, DBUS_IS_ASCII_WHITE, DBusRealString::len, and DBusRealString::str.

Referenced by \_dbus_string_chop_white().

## ◆ \_dbus_string_skip_white_reverse()

|                                       |     |                      |          |
|---------------------------------------|-----|----------------------|----------|
| void \_dbus_string_skip_white_reverse | (   | const DBusString \*  | *str*,   |
|                                       |     | int                  | *end*,   |
|                                       |     | int \*               | *start*  |
|                                       | )   |                      |          |

Skips whitespace from end, storing the start index of the trailing whitespace in \*start.

(whitespace is space, tab, newline, CR).

Parameters  
|       |                                              |
|-------|----------------------------------------------|
| str   | the string                                   |
| end   | where to start scanning backward             |
| start | where to store the start of whitespace chars |

Definition at line 1932 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, DBUS_IS_ASCII_WHITE, and DBusRealString::str.

Referenced by \_dbus_string_chop_white().

## ◆ \_dbus_string_split_on_byte()

|                                         |     |                |           |
|-----------------------------------------|-----|----------------|-----------|
| dbus_bool_t \_dbus_string_split_on_byte | (   | DBusString \*  | *source*, |
|                                         |     | unsigned char  | *byte*,   |
|                                         |     | DBusString \*  | *tail*    |
|                                         | )   |                |           |

Looks for the first occurance of a byte, deletes that byte, and moves everything after the byte to the beginning of a separate string.

Both strings must be initialized, valid strings.

Parameters  
|        |                                            |
|--------|--------------------------------------------|
| source | the source string                          |
| byte   | the byte to remove and split the string at |
| tail   | the split off string                       |

<!-- -->

Returns  
FALSE if not enough memory or if byte could not be found

Definition at line 1529 of file dbus-string.c.

References \_dbus_string_find(), \_dbus_string_get_length(), \_dbus_string_move_len(), \_dbus_string_set_length(), FALSE, and TRUE.

Referenced by \_dbus_hash_table_from_array().

## ◆ \_dbus_string_starts_with_c_str()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_starts_with_c_str | ( | const DBusString \*  | *a*, |
|  |  | const char \*  | *c_str*  |
|  | ) |  |  |

Checks whether a string starts with the given C string.

Parameters  
|       |              |
|-------|--------------|
| a     | the string   |
| c_str | the C string |

<!-- -->

Returns  
TRUE if string starts with it

Definition at line 2250 of file dbus-string.c.

References \_dbus_assert, DBUS_GENERIC_STRING_PREAMBLE, FALSE, DBusRealString::len, NULL, DBusRealString::str, and TRUE.

Referenced by \_dbus_replace_install_prefix(), and \_dbus_string_starts_with_words_c_str().

## ◆ \_dbus_string_starts_with_words_c_str()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_string_starts_with_words_c_str | ( | const DBusString \*  | *a*, |
|  |  | const char \*  | *c_str*, |
|  |  | char  | *word_separator*  |
|  | ) |  |  |

Checks whether a string starts with the given C string, after which it ends or is separated from the rest by a given separator character.

Parameters  
|                |               |
|----------------|---------------|
| a              | the string    |
| c_str          | the C string  |
| word_separator | the separator |

<!-- -->

Returns  
TRUE if string starts with it

Definition at line 2288 of file dbus-string.c.

References \_dbus_assert, \_dbus_string_get_const_data(), \_dbus_string_starts_with_c_str(), FALSE, and NULL.

## ◆ \_dbus_string_steal_data()

|                                      |     |                |                |
|--------------------------------------|-----|----------------|----------------|
| dbus_bool_t \_dbus_string_steal_data | (   | DBusString \*  | *str*,         |
|                                      |     | char \*\*      | *data_return*  |
|                                      | )   |                |                |

Like \_dbus_string_get_data(), but removes the gotten data from the original string.

The caller must free the data returned. This function may fail due to lack of memory, and return FALSE.

Parameters  
|             |                               |
|-------------|-------------------------------|
| str         | the string                    |
| data_return | location to return the buffer |

<!-- -->

Returns  
TRUE on success

Definition at line 686 of file dbus-string.c.

References \_dbus_assert, \_dbus_string_init(), DBUS_STRING_PREAMBLE, FALSE, NULL, DBusRealString::str, and TRUE.

Referenced by \_dbus_hash_table_from_array(), \_dbus_hash_table_to_array(), \_dbus_set_up_transient_session_servicedirs(), dbus_address_escape_value(), dbus_address_unescape_value(), dbus_message_iter_get_signature(), dbus_message_marshal(), dbus_signature_iter_get_signature(), and dbus_try_get_local_machine_id().

## ◆ \_dbus_string_tolower_ascii()

|                                  |     |                      |          |
|----------------------------------|-----|----------------------|----------|
| void \_dbus_string_tolower_ascii | (   | const DBusString \*  | *str*,   |
|                                  |     | int                  | *start*, |
|                                  |     | int                  | *len*    |
|                                  | )   |                      |          |

Converts the given range of the string to lower case.

Parameters  
|       |                             |
|-------|-----------------------------|
| str   | the string                  |
| start | first byte index to convert |
| len   | number of bytes to convert  |

Definition at line 2608 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_PREAMBLE, and DBusRealString::str.

## ◆ \_dbus_string_toupper_ascii()

|                                  |     |                      |          |
|----------------------------------|-----|----------------------|----------|
| void \_dbus_string_toupper_ascii | (   | const DBusString \*  | *str*,   |
|                                  |     | int                  | *start*, |
|                                  |     | int                  | *len*    |
|                                  | )   |                      |          |

Converts the given range of the string to upper case.

Parameters  
|       |                             |
|-------|-----------------------------|
| str   | the string                  |
| start | first byte index to convert |
| len   | number of bytes to convert  |

Definition at line 2639 of file dbus-string.c.

References \_dbus_assert, DBUS_STRING_PREAMBLE, and DBusRealString::str.

## ◆ \_dbus_string_validate_ascii()

|                                          |     |                      |          |
|------------------------------------------|-----|----------------------|----------|
| dbus_bool_t \_dbus_string_validate_ascii | (   | const DBusString \*  | *str*,   |
|                                          |     | int                  | *start*, |
|                                          |     | int                  | *len*    |
|                                          | )   |                      |          |

Checks that the given range of the string is valid ASCII with no nul bytes.

If the given range is not entirely contained in the string, returns FALSE.

Parameters  
|       |                           |
|-------|---------------------------|
| str   | the string                |
| start | first byte index to check |
| len   | number of bytes to check  |

<!-- -->

Returns  
TRUE if the byte range exists and is all valid ASCII

Definition at line 2573 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::str, and TRUE.

Referenced by \_dbus_generate_random_ascii(), and \_dbus_keyring_validate_context().

## ◆ \_dbus_string_validate_nul()

|                                        |     |                      |          |
|----------------------------------------|-----|----------------------|----------|
| dbus_bool_t \_dbus_string_validate_nul | (   | const DBusString \*  | *str*,   |
|                                        |     | int                  | *start*, |
|                                        |     | int                  | *len*    |
|                                        | )   |                      |          |

Checks that the given range of the string is all nul bytes.

If the given range is not entirely contained in the string, returns FALSE.

Parameters  
|       |                           |
|-------|---------------------------|
| str   | the string                |
| start | first byte index to check |
| len   | number of bytes to check  |

<!-- -->

Returns  
TRUE if the byte range exists and is all nul bytes

Definition at line 2776 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::str, and TRUE.

Referenced by \_dbus_header_load().

## ◆ \_dbus_string_validate_utf8()

|                                         |     |                      |          |
|-----------------------------------------|-----|----------------------|----------|
| dbus_bool_t \_dbus_string_validate_utf8 | (   | const DBusString \*  | *str*,   |
|                                         |     | int                  | *start*, |
|                                         |     | int                  | *len*    |
|                                         | )   |                      |          |

Checks that the given range of the string is valid UTF-8.

If the given range is not entirely contained in the string, returns FALSE. If the string contains any nul bytes in the given range, returns FALSE. If the start and start+len are not on character boundaries, returns FALSE.

Parameters  
|       |                           |
|-------|---------------------------|
| str   | the string                |
| start | first byte index to check |
| len   | number of bytes to check  |

<!-- -->

Returns  
TRUE if the byte range exists and is all valid UTF-8

Definition at line 2678 of file dbus-string.c.

References \_dbus_assert, DBUS_CONST_STRING_PREAMBLE, FALSE, DBusRealString::len, DBusRealString::str, TRUE, UNICODE_VALID, UTF8_COMPUTE, UTF8_GET, and UTF8_LENGTH.

Referenced by dbus_validate_bus_name(), dbus_validate_error_name(), dbus_validate_interface(), dbus_validate_member(), dbus_validate_path(), and dbus_validate_utf8().

## ◆ \_dbus_string_zero()

|                         |     |                |       |     |     |
|-------------------------|-----|----------------|-------|-----|-----|
| void \_dbus_string_zero | (   | DBusString \*  | *str* | )   |     |

Clears all allocated bytes in the string to zero.

Parameters  
|     |            |
|-----|------------|
| str | the string |

Definition at line 2808 of file dbus-string.c.

References DBusRealString::align_offset, DBusRealString::allocated, DBUS_STRING_PREAMBLE, and DBusRealString::str.

## ◆ \_dbus_unix_groups_from_uid()

|                                         |     |                  |                |
|-----------------------------------------|-----|------------------|----------------|
| dbus_bool_t \_dbus_unix_groups_from_uid | (   | dbus_uid_t       | *uid*,         |
|                                         |     | dbus_gid_t \*\*  | *group_ids*,   |
|                                         |     | int \*           | *n_group_ids*, |
|                                         |     | DBusError \*     | *error*        |
|                                         | )   |                  |                |

Gets all groups corresponding to the given UNIX user ID.

On UNIX, just calls \_dbus_groups_from_uid(). On Windows, should always fail since we don't know any UNIX groups.

Parameters  
|             |                                              |
|-------------|----------------------------------------------|
| uid         | the UID                                      |
| group_ids   | return location for array of group IDs       |
| n_group_ids | return location for length of returned array |
| error       | error location                               |

<!-- -->

Returns  
TRUE if the UID existed and we got some credentials

Definition at line 721 of file dbus-sysdeps-util-win.c.

References FALSE.

## ◆ \_dbus_unix_user_is_at_console()

|                                            |     |               |          |
|--------------------------------------------|-----|---------------|----------|
| dbus_bool_t \_dbus_unix_user_is_at_console | (   | dbus_uid_t    | *uid*,   |
|                                            |     | DBusError \*  | *error*  |
|                                            | )   |               |          |

Checks to see if the UNIX user ID is at the console.

Should always fail on Windows (set the error to DBUS_ERROR_NOT_SUPPORTED).

Parameters  
|       |                            |
|-------|----------------------------|
| uid   | UID of person to check     |
| error | return location for errors |

<!-- -->

Returns  
TRUE if the UID is the same as the console user and there are no errors

Definition at line 670 of file dbus-sysdeps-util-win.c.

References FALSE.

## ◆ \_dbus_unix_user_is_process_owner()

|                                               |     |             |       |     |     |
|-----------------------------------------------|-----|-------------|-------|-----|-----|
| dbus_bool_t \_dbus_unix_user_is_process_owner | (   | dbus_uid_t  | *uid* | )   |     |

Checks to see if the UNIX user ID matches the UID of the process.

Should always return FALSE on Windows.

Parameters  
|     |                  |
|-----|------------------|
| uid | the UNIX user ID |

<!-- -->

Returns  
TRUE if this uid owns the process.

Definition at line 639 of file dbus-sysdeps-util-win.c.

References FALSE.

## ◆ \_dbus_windows_user_is_process_owner()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_windows_user_is_process_owner | ( | const char \*  | *windows_sid* | ) |  |

Checks to see if the Windows user SID matches the owner of the process.

Should always return FALSE on UNIX.

Parameters  
|             |                      |
|-------------|----------------------|
| windows_sid | the Windows user SID |

<!-- -->

Returns  
TRUE if this user owns the process.

Definition at line 644 of file dbus-sysdeps-util-win.c.

References TRUE.
