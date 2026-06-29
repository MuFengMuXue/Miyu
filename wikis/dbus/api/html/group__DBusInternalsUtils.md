Utilities and portability

D-Bus secret internal implementation details

Utility functions (\_dbus_assert(), \_dbus_warn(), etc.) More...

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
<td class="memItemRight" data-valign="bottom">DBusBabysitter</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Babysitter implementation details. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusDirIter</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of directory iterator. More...<br />
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
<tr id="r_ga129c6c03f011cdc171934d5d386cc797" class="memitem:ga129c6c03f011cdc171934d5d386cc797">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_dbus_assert(condition)    _dbus_real_assert ((condition) != 0, #condition, __FILE__, __LINE__, _DBUS_FUNCTION_NAME)</td>
</tr>
<tr class="memdesc:ga129c6c03f011cdc171934d5d386cc797">
<td class="mdescLeft"> </td>
<td class="mdescRight">Aborts with an error message if the condition is false.<br />
</td>
</tr>
<tr class="separator:ga129c6c03f011cdc171934d5d386cc797">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0c4961ec784874f1b1f3aeccea8d3da1" class="memitem:ga0c4961ec784874f1b1f3aeccea8d3da1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_dbus_assert_not_reached(explanation)    _dbus_real_assert_not_reached (explanation, __FILE__, __LINE__)</td>
</tr>
<tr class="memdesc:ga0c4961ec784874f1b1f3aeccea8d3da1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Aborts with an error message if called.<br />
</td>
</tr>
<tr class="separator:ga0c4961ec784874f1b1f3aeccea8d3da1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac153abad46f4eb80999a2b340d29d1f0" class="memitem:gac153abad46f4eb80999a2b340d29d1f0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_N_ELEMENTS(array)   ((int) (sizeof ((array)) / sizeof ((array)[0])))</td>
</tr>
<tr class="memdesc:gac153abad46f4eb80999a2b340d29d1f0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Computes the number of elements in a fixed-size array using sizeof().<br />
</td>
</tr>
<tr class="separator:gac153abad46f4eb80999a2b340d29d1f0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabbd3526a2ecd65da80b9f74ac286273d" class="memitem:gabbd3526a2ecd65da80b9f74ac286273d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_POINTER_TO_INT(pointer)   ((intptr_t)(pointer))</td>
</tr>
<tr class="memdesc:gabbd3526a2ecd65da80b9f74ac286273d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Safely casts a void* to an integer; should only be used on void* that actually contain integers, for example one created with _DBUS_INT_TO_POINTER.<br />
</td>
</tr>
<tr class="separator:gabbd3526a2ecd65da80b9f74ac286273d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga05e902d8504a8a0e0b183fd2e20e329f" class="memitem:ga05e902d8504a8a0e0b183fd2e20e329f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_INT_TO_POINTER(integer)   ((void*)((intptr_t)(integer)))</td>
</tr>
<tr class="memdesc:ga05e902d8504a8a0e0b183fd2e20e329f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Safely stuffs an integer into a pointer, to be extracted later with _DBUS_POINTER_TO_INT.<br />
</td>
</tr>
<tr class="separator:ga05e902d8504a8a0e0b183fd2e20e329f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaec42589166158b1385d5f5439318cda2" class="memitem:gaec42589166158b1385d5f5439318cda2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_ZERO(object)   (memset (&amp;(object), '\0', sizeof ((object))))</td>
</tr>
<tr class="memdesc:gaec42589166158b1385d5f5439318cda2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets all bits in an object to zero.<br />
</td>
</tr>
<tr class="separator:gaec42589166158b1385d5f5439318cda2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga933ce3d9d9b9298b004f2dc5020e9448" class="memitem:ga933ce3d9d9b9298b004f2dc5020e9448">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_INT16_MIN   ((dbus_int16_t) 0x8000)</td>
</tr>
<tr class="memdesc:ga933ce3d9d9b9298b004f2dc5020e9448">
<td class="mdescLeft"> </td>
<td class="mdescRight">Minimum value of type "int16".<br />
</td>
</tr>
<tr class="separator:ga933ce3d9d9b9298b004f2dc5020e9448">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga15a258ca83bb9819775b9f6f7a505bc4" class="memitem:ga15a258ca83bb9819775b9f6f7a505bc4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_INT16_MAX   ((dbus_int16_t) 0x7fff)</td>
</tr>
<tr class="memdesc:ga15a258ca83bb9819775b9f6f7a505bc4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum value of type "int16".<br />
</td>
</tr>
<tr class="separator:ga15a258ca83bb9819775b9f6f7a505bc4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab59f93488de3d91c4e1a2c5e5e116354" class="memitem:gab59f93488de3d91c4e1a2c5e5e116354">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_UINT16_MAX   ((dbus_uint16_t)0xffff)</td>
</tr>
<tr class="memdesc:gab59f93488de3d91c4e1a2c5e5e116354">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum value of type "uint16".<br />
</td>
</tr>
<tr class="separator:gab59f93488de3d91c4e1a2c5e5e116354">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac1f9d5e99c5f797b38b41b66e9c6c4ed" class="memitem:gac1f9d5e99c5f797b38b41b66e9c6c4ed">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_INT32_MIN   ((dbus_int32_t) 0x80000000)</td>
</tr>
<tr class="memdesc:gac1f9d5e99c5f797b38b41b66e9c6c4ed">
<td class="mdescLeft"> </td>
<td class="mdescRight">Minimum value of type "int32".<br />
</td>
</tr>
<tr class="separator:gac1f9d5e99c5f797b38b41b66e9c6c4ed">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafe869e3145b7e32c4fb6a6741c9fc78e" class="memitem:gafe869e3145b7e32c4fb6a6741c9fc78e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_INT32_MAX   ((dbus_int32_t) 0x7fffffff)</td>
</tr>
<tr class="memdesc:gafe869e3145b7e32c4fb6a6741c9fc78e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum value of type "int32".<br />
</td>
</tr>
<tr class="separator:gafe869e3145b7e32c4fb6a6741c9fc78e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac85046b2af0a98c51bb93300f99448da" class="memitem:gac85046b2af0a98c51bb93300f99448da">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_UINT32_MAX   ((dbus_uint32_t)0xffffffff)</td>
</tr>
<tr class="memdesc:gac85046b2af0a98c51bb93300f99448da">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum value of type "uint32".<br />
</td>
</tr>
<tr class="separator:gac85046b2af0a98c51bb93300f99448da">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3bf800f1b6cc23f80006861d7417c8c8" class="memitem:ga3bf800f1b6cc23f80006861d7417c8c8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_INT_MIN   _DBUS_INT32_MIN</td>
</tr>
<tr class="memdesc:ga3bf800f1b6cc23f80006861d7417c8c8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Minimum value of type "int".<br />
</td>
</tr>
<tr class="separator:ga3bf800f1b6cc23f80006861d7417c8c8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5627db5e165848477e620846f6414db1" class="memitem:ga5627db5e165848477e620846f6414db1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_INT_MAX   _DBUS_INT32_MAX</td>
</tr>
<tr class="memdesc:ga5627db5e165848477e620846f6414db1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum value of type "int".<br />
</td>
</tr>
<tr class="separator:ga5627db5e165848477e620846f6414db1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6e9cfa6e6cb608d29fbdc4a50baea051" class="memitem:ga6e9cfa6e6cb608d29fbdc4a50baea051">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_UINT_MAX   _DBUS_UINT32_MAX</td>
</tr>
<tr class="memdesc:ga6e9cfa6e6cb608d29fbdc4a50baea051">
<td class="mdescLeft"> </td>
<td class="mdescRight">Maximum value of type "uint".<br />
</td>
</tr>
<tr class="separator:ga6e9cfa6e6cb608d29fbdc4a50baea051">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gade571435b55fae64217f5142aa78ee8d" class="memitem:gade571435b55fae64217f5142aa78ee8d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_LOCK_NAME(name)   _DBUS_LOCK_##name</td>
</tr>
<tr class="memdesc:gade571435b55fae64217f5142aa78ee8d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Expands to name of a global lock variable.<br />
</td>
</tr>
<tr class="separator:gade571435b55fae64217f5142aa78ee8d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3b56fdb9df58277ee69d9f56a73bf383" class="memitem:ga3b56fdb9df58277ee69d9f56a73bf383">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_LOCK(name)   _dbus_lock (_DBUS_LOCK_##name)</td>
</tr>
<tr class="memdesc:ga3b56fdb9df58277ee69d9f56a73bf383">
<td class="mdescLeft"> </td>
<td class="mdescRight">Locks a global lock, initializing it first if necessary.<br />
</td>
</tr>
<tr class="separator:ga3b56fdb9df58277ee69d9f56a73bf383">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1b7db80a2ea11235768ec8aa698df0a5" class="memitem:ga1b7db80a2ea11235768ec8aa698df0a5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_DBUS_UNLOCK(name)   _dbus_unlock (_DBUS_LOCK_##name)</td>
</tr>
<tr class="memdesc:ga1b7db80a2ea11235768ec8aa698df0a5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unlocks a global lock.<br />
</td>
</tr>
<tr class="separator:ga1b7db80a2ea11235768ec8aa698df0a5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf3ce8172242a1766bdd5cfe4b0a05d1f" class="memitem:gaf3ce8172242a1766bdd5cfe4b0a05d1f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">LIVE_CHILDREN(sitter)   ((sitter)-&gt;socket_to_babysitter.fd &gt;= 0 || (sitter)-&gt;error_pipe_from_child &gt;= 0)</td>
</tr>
<tr class="memdesc:gaf3ce8172242a1766bdd5cfe4b0a05d1f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Macro returns TRUE if the babysitter still has live sockets open to the babysitter child or the grandchild.<br />
</td>
</tr>
<tr class="separator:gaf3ce8172242a1766bdd5cfe4b0a05d1f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2469c53816dc077f9deefb187ffcabf3" class="memitem:ga2469c53816dc077f9deefb187ffcabf3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">READ_END   0</td>
</tr>
<tr class="memdesc:ga2469c53816dc077f9deefb187ffcabf3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Helps remember which end of the pipe is which.<br />
</td>
</tr>
<tr class="separator:ga2469c53816dc077f9deefb187ffcabf3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2efd706d915e621e5e18b3f0803c4ed2" class="memitem:ga2efd706d915e621e5e18b3f0803c4ed2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">WRITE_END   1</td>
</tr>
<tr class="memdesc:ga2efd706d915e621e5e18b3f0803c4ed2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Helps remember which end of the pipe is which.<br />
</td>
</tr>
<tr class="separator:ga2efd706d915e621e5e18b3f0803c4ed2">
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
<td colspan="2"><h2 id="enumerations" class="groupheader"> Enumerations</h2></td>
</tr>
<tr id="r_gaa1d634db87605c2a83f2750ce6052653" class="memitem:gaa1d634db87605c2a83f2750ce6052653">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">ReadStatus { READ_STATUS_OK , READ_STATUS_ERROR , READ_STATUS_EOF }</td>
</tr>
<tr class="memdesc:gaa1d634db87605c2a83f2750ce6052653">
<td class="mdescLeft"> </td>
<td class="mdescRight">Enumeration for status of a read() More...<br />
</td>
</tr>
<tr class="separator:gaa1d634db87605c2a83f2750ce6052653">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabed82baf7f470b522273a3e37c24c600" class="memitem:gabed82baf7f470b522273a3e37c24c600">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">{ <strong>CHILD_EXITED</strong> , <strong>CHILD_FORK_FAILED</strong> , <strong>CHILD_EXEC_FAILED</strong> , <strong>CHILD_PID</strong> }</td>
</tr>
<tr class="separator:gabed82baf7f470b522273a3e37c24c600">
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
<tr id="r_ga6012b11e8d0d6efd90411b8d68f714a3" class="memitem:ga6012b11e8d0d6efd90411b8d68f714a3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>_DBUS_STATIC_ASSERT</strong> (sizeof(void *)==DBUS_SIZEOF_VOID_P)</td>
</tr>
<tr class="separator:ga6012b11e8d0d6efd90411b8d68f714a3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9d691edf6b6712d8744152f6cc4d0c38" class="memitem:ga9d691edf6b6712d8744152f6cc4d0c38">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>_DBUS_STATIC_ASSERT</strong> (_DBUS_ALIGNOF(void *)==_DBUS_ALIGNOF(DBusShutdownFunction))</td>
</tr>
<tr class="separator:ga9d691edf6b6712d8744152f6cc4d0c38">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa8e452efe4e4d61afdc3ef06c964395c" class="memitem:gaa8e452efe4e4d61afdc3ef06c964395c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_check_failed_count (void)</td>
</tr>
<tr class="separator:gaa8e452efe4e4d61afdc3ef06c964395c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabea2c16d6d3fe7c4eb5b9496fc877f84" class="memitem:gabea2c16d6d3fe7c4eb5b9496fc877f84">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_warn (const char *format,...)</td>
</tr>
<tr class="memdesc:gabea2c16d6d3fe7c4eb5b9496fc877f84">
<td class="mdescLeft"> </td>
<td class="mdescRight">Prints a warning message to stderr.<br />
</td>
</tr>
<tr class="separator:gabea2c16d6d3fe7c4eb5b9496fc877f84">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga63f2f8a068454b781f214ba596e313b4" class="memitem:ga63f2f8a068454b781f214ba596e313b4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_warn_check_failed (const char *format,...)</td>
</tr>
<tr class="memdesc:ga63f2f8a068454b781f214ba596e313b4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Prints a "critical" warning to stderr when an assertion fails; differs from _dbus_warn primarily in that it defaults to fatal.<br />
</td>
</tr>
<tr class="separator:ga63f2f8a068454b781f214ba596e313b4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6fb17d1b96d8765766defb83a4ab6e11" class="memitem:ga6fb17d1b96d8765766defb83a4ab6e11">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_strdup (const char *str)</td>
</tr>
<tr class="memdesc:ga6fb17d1b96d8765766defb83a4ab6e11">
<td class="mdescLeft"> </td>
<td class="mdescRight">Duplicates a string.<br />
</td>
</tr>
<tr class="separator:ga6fb17d1b96d8765766defb83a4ab6e11">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaec4637d5c89055a3ab08b5fa75a39709" class="memitem:gaec4637d5c89055a3ab08b5fa75a39709">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_memdup (const void *mem, size_t n_bytes)</td>
</tr>
<tr class="memdesc:gaec4637d5c89055a3ab08b5fa75a39709">
<td class="mdescLeft"> </td>
<td class="mdescRight">Duplicates a block of memory.<br />
</td>
</tr>
<tr class="separator:gaec4637d5c89055a3ab08b5fa75a39709">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf618ca651047be07ea751bf008b4d6d6" class="memitem:gaf618ca651047be07ea751bf008b4d6d6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char ** </td>
<td class="memItemRight" data-valign="bottom">_dbus_dup_string_array (const char **array)</td>
</tr>
<tr class="memdesc:gaf618ca651047be07ea751bf008b4d6d6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Duplicates a string array.<br />
</td>
</tr>
<tr class="separator:gaf618ca651047be07ea751bf008b4d6d6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga751119e7273225a7e59787445b71fcd6" class="memitem:ga751119e7273225a7e59787445b71fcd6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_array_contains (const char **array, const char *str)</td>
</tr>
<tr class="memdesc:ga751119e7273225a7e59787445b71fcd6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether a string array contains the given string.<br />
</td>
</tr>
<tr class="separator:ga751119e7273225a7e59787445b71fcd6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacd276301af0af83f2c9153c15477ac15" class="memitem:gacd276301af0af83f2c9153c15477ac15">
<td class="memItemLeft" style="text-align: right;" data-valign="top">size_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_string_array_length (const char **array)</td>
</tr>
<tr class="memdesc:gacd276301af0af83f2c9153c15477ac15">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the size of a string array.<br />
</td>
</tr>
<tr class="separator:gacd276301af0af83f2c9153c15477ac15">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4dd7c3aad4203b12e9fb2d00c888f085" class="memitem:ga4dd7c3aad4203b12e9fb2d00c888f085">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_generate_uuid (DBusGUID *uuid, DBusError *error)</td>
</tr>
<tr class="memdesc:ga4dd7c3aad4203b12e9fb2d00c888f085">
<td class="mdescLeft"> </td>
<td class="mdescRight">Generates a new UUID.<br />
</td>
</tr>
<tr class="separator:ga4dd7c3aad4203b12e9fb2d00c888f085">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf08364813376bd2d8f455d435d85323e" class="memitem:gaf08364813376bd2d8f455d435d85323e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_uuid_encode (const DBusGUID *uuid, DBusString *encoded)</td>
</tr>
<tr class="memdesc:gaf08364813376bd2d8f455d435d85323e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Hex-encode a UUID.<br />
</td>
</tr>
<tr class="separator:gaf08364813376bd2d8f455d435d85323e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa16de06b33c56323fa33dd96eaab3829" class="memitem:gaa16de06b33c56323fa33dd96eaab3829">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_write_uuid_file (const DBusString *filename, const DBusGUID *uuid, DBusError *error)</td>
</tr>
<tr class="memdesc:gaa16de06b33c56323fa33dd96eaab3829">
<td class="mdescLeft"> </td>
<td class="mdescRight">Write the give UUID to a file.<br />
</td>
</tr>
<tr class="separator:gaa16de06b33c56323fa33dd96eaab3829">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga709fd30e6b940a5952af38efaf24ad51" class="memitem:ga709fd30e6b940a5952af38efaf24ad51">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_read_uuid_file (const DBusString *filename, DBusGUID *uuid, dbus_bool_t create_if_not_found, DBusError *error)</td>
</tr>
<tr class="memdesc:ga709fd30e6b940a5952af38efaf24ad51">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reads (and optionally writes) a uuid to a file.<br />
</td>
</tr>
<tr class="separator:ga709fd30e6b940a5952af38efaf24ad51">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga91f62cbd7b14e0763809aee0be259df7" class="memitem:ga91f62cbd7b14e0763809aee0be259df7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_local_machine_uuid_encoded (DBusString *uuid_str, DBusError *error)</td>
</tr>
<tr class="memdesc:ga91f62cbd7b14e0763809aee0be259df7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the hex-encoded UUID of the machine this function is executed on.<br />
</td>
</tr>
<tr class="separator:ga91f62cbd7b14e0763809aee0be259df7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga450d755e23520bd3543113b0021cc695" class="memitem:ga450d755e23520bd3543113b0021cc695">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_warn_return_if_fail (const char *function, const char *assertion, const char *file, int line)</td>
</tr>
<tr class="separator:ga450d755e23520bd3543113b0021cc695">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9912f2c86e49357eb9729729dd46f50d" class="memitem:ga9912f2c86e49357eb9729729dd46f50d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_real_assert (dbus_bool_t condition, const char *condition_text, const char *file, int line, const char *func)</td>
</tr>
<tr class="memdesc:ga9912f2c86e49357eb9729729dd46f50d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of _dbus_assert(); it's a function rather than a macro with the inline code so that the assertion failure blocks don't show up in test suite coverage, and to shrink code size.<br />
</td>
</tr>
<tr class="separator:ga9912f2c86e49357eb9729729dd46f50d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3de125028afc39ab16e6585add8ad181" class="memitem:ga3de125028afc39ab16e6585add8ad181">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_real_assert_not_reached (const char *explanation, const char *file, int line)</td>
</tr>
<tr class="memdesc:ga3de125028afc39ab16e6585add8ad181">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of _dbus_assert_not_reached(); it's a function rather than a macro with the inline code so that the assertion failure blocks don't show up in test suite coverage, and to shrink code size.<br />
</td>
</tr>
<tr class="separator:ga3de125028afc39ab16e6585add8ad181">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad2007b8c57db70521fa746e8be41f88c" class="memitem:gad2007b8c57db70521fa746e8be41f88c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusBabysitter * </td>
<td class="memItemRight" data-valign="bottom">_dbus_babysitter_ref (DBusBabysitter *sitter)</td>
</tr>
<tr class="memdesc:gad2007b8c57db70521fa746e8be41f88c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increment the reference count on the babysitter object.<br />
</td>
</tr>
<tr class="separator:gad2007b8c57db70521fa746e8be41f88c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3205e9f8672271794aeb9d451e2fcc4a" class="memitem:ga3205e9f8672271794aeb9d451e2fcc4a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_babysitter_unref (DBusBabysitter *sitter)</td>
</tr>
<tr class="memdesc:ga3205e9f8672271794aeb9d451e2fcc4a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrement the reference count on the babysitter object.<br />
</td>
</tr>
<tr class="separator:ga3205e9f8672271794aeb9d451e2fcc4a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacdc9c49735d6ce8364647c1961aa8d2b" class="memitem:gacdc9c49735d6ce8364647c1961aa8d2b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_babysitter_kill_child (DBusBabysitter *sitter)</td>
</tr>
<tr class="memdesc:gacdc9c49735d6ce8364647c1961aa8d2b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Blocks until the babysitter process gives us the PID of the spawned grandchild, then kills the spawned grandchild.<br />
</td>
</tr>
<tr class="separator:gacdc9c49735d6ce8364647c1961aa8d2b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5c463ea356ea62055a35211e8d81f8b9" class="memitem:ga5c463ea356ea62055a35211e8d81f8b9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_babysitter_get_child_exited (DBusBabysitter *sitter)</td>
</tr>
<tr class="memdesc:ga5c463ea356ea62055a35211e8d81f8b9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the child has exited, without blocking.<br />
</td>
</tr>
<tr class="separator:ga5c463ea356ea62055a35211e8d81f8b9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1b17eec3f7915c21251685e16123f299" class="memitem:ga1b17eec3f7915c21251685e16123f299">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_babysitter_get_child_exit_status (DBusBabysitter *sitter, int *status)</td>
</tr>
<tr class="memdesc:ga1b17eec3f7915c21251685e16123f299">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the exit status of the child.<br />
</td>
</tr>
<tr class="separator:ga1b17eec3f7915c21251685e16123f299">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9c6f92a67e41f08d8eb254e294fd0378" class="memitem:ga9c6f92a67e41f08d8eb254e294fd0378">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_babysitter_set_child_exit_error (DBusBabysitter *sitter, DBusError *error)</td>
</tr>
<tr class="memdesc:ga9c6f92a67e41f08d8eb254e294fd0378">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the DBusError with an explanation of why the spawned child process exited (on a signal, or whatever).<br />
</td>
</tr>
<tr class="separator:ga9c6f92a67e41f08d8eb254e294fd0378">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5f467b14f0c2f667e46c4ba786808e5b" class="memitem:ga5f467b14f0c2f667e46c4ba786808e5b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_babysitter_set_watch_functions (DBusBabysitter *sitter, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:ga5f467b14f0c2f667e46c4ba786808e5b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets watch functions to notify us when the babysitter object needs to read/write file descriptors.<br />
</td>
</tr>
<tr class="separator:ga5f467b14f0c2f667e46c4ba786808e5b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf1203033775fda171c95ffc01034cf0a" class="memitem:gaf1203033775fda171c95ffc01034cf0a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_spawn_async_with_babysitter (DBusBabysitter **sitter_p, const char *log_name, char *const *argv, char *const *env, DBusSpawnFlags flags, DBusSpawnChildSetupFunc child_setup, void *user_data, DBusError *error)</td>
</tr>
<tr class="memdesc:gaf1203033775fda171c95ffc01034cf0a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Spawns a new process.<br />
</td>
</tr>
<tr class="separator:gaf1203033775fda171c95ffc01034cf0a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga98cc9642d4e5246804c8611022a68c0e" class="memitem:ga98cc9642d4e5246804c8611022a68c0e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_babysitter_set_result_function (DBusBabysitter *sitter, DBusBabysitterFinishedFunc finished, void *user_data)</td>
</tr>
<tr class="separator:ga98cc9642d4e5246804c8611022a68c0e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaca61af8681a48862835ea8cfd263f5ab" class="memitem:gaca61af8681a48862835ea8cfd263f5ab">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_become_daemon (const DBusString *pidfile, DBusPipe *print_pid_pipe, DBusError *error, dbus_bool_t keep_umask)</td>
</tr>
<tr class="memdesc:gaca61af8681a48862835ea8cfd263f5ab">
<td class="mdescLeft"> </td>
<td class="mdescRight">Does the chdir, fork, setsid, etc.<br />
</td>
</tr>
<tr class="separator:gaca61af8681a48862835ea8cfd263f5ab">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga123620ec5ce2b881786588121d6a03fd" class="memitem:ga123620ec5ce2b881786588121d6a03fd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_write_pid_to_file_and_pipe (const DBusString *pidfile, DBusPipe *print_pid_pipe, dbus_pid_t pid_to_write, DBusError *error)</td>
</tr>
<tr class="memdesc:ga123620ec5ce2b881786588121d6a03fd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Writes the given pid_to_write to a pidfile (if non-NULL) and/or to a pipe (if non-NULL).<br />
</td>
</tr>
<tr class="separator:ga123620ec5ce2b881786588121d6a03fd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga45f661c5a089ed45233a1acabaf31964" class="memitem:ga45f661c5a089ed45233a1acabaf31964">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_verify_daemon_user (const char *user)</td>
</tr>
<tr class="memdesc:ga45f661c5a089ed45233a1acabaf31964">
<td class="mdescLeft"> </td>
<td class="mdescRight">Verify that after the fork we can successfully change to this user.<br />
</td>
</tr>
<tr class="separator:ga45f661c5a089ed45233a1acabaf31964">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga82c920a8c3b5958ba1ecf8e5f5d6373b" class="memitem:ga82c920a8c3b5958ba1ecf8e5f5d6373b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_change_to_daemon_user (const char *user, DBusError *error)</td>
</tr>
<tr class="memdesc:ga82c920a8c3b5958ba1ecf8e5f5d6373b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Changes the user and group the bus is running as.<br />
</td>
</tr>
<tr class="separator:ga82c920a8c3b5958ba1ecf8e5f5d6373b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5573a7a21c60fcd86c43ae51c10ee4d4" class="memitem:ga5573a7a21c60fcd86c43ae51c10ee4d4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRLimit * </td>
<td class="memItemRight" data-valign="bottom">_dbus_rlimit_save_fd_limit (DBusError *error)</td>
</tr>
<tr class="separator:ga5573a7a21c60fcd86c43ae51c10ee4d4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad231dff4b9a9f3912a6e1774ceaddb0f" class="memitem:gad231dff4b9a9f3912a6e1774ceaddb0f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_rlimit_raise_fd_limit (DBusError *error)</td>
</tr>
<tr class="separator:gad231dff4b9a9f3912a6e1774ceaddb0f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab87dbd966b0051b7ff916e06e43fcf2e" class="memitem:gab87dbd966b0051b7ff916e06e43fcf2e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_rlimit_restore_fd_limit (DBusRLimit *saved, DBusError *error)</td>
</tr>
<tr class="separator:gab87dbd966b0051b7ff916e06e43fcf2e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga53db90ef9ed40073f1b0821d1589a024" class="memitem:ga53db90ef9ed40073f1b0821d1589a024">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_rlimit_free (DBusRLimit *lim)</td>
</tr>
<tr class="separator:ga53db90ef9ed40073f1b0821d1589a024">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4aa7500366dad2dd6d3fa97b3aa7165b" class="memitem:ga4aa7500366dad2dd6d3fa97b3aa7165b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_set_signal_handler (int sig, DBusSignalHandler handler)</td>
</tr>
<tr class="memdesc:ga4aa7500366dad2dd6d3fa97b3aa7165b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Installs a UNIX signal handler.<br />
</td>
</tr>
<tr class="separator:ga4aa7500366dad2dd6d3fa97b3aa7165b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga13a527e32c05b63e8b32a63d728e20e8" class="memitem:ga13a527e32c05b63e8b32a63d728e20e8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_file_exists (const char *file)</td>
</tr>
<tr class="memdesc:ga13a527e32c05b63e8b32a63d728e20e8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks if a file exists.<br />
</td>
</tr>
<tr class="separator:ga13a527e32c05b63e8b32a63d728e20e8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6d80876bcae54f47cde79d0bce20321d" class="memitem:ga6d80876bcae54f47cde79d0bce20321d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_path_is_absolute (const DBusString *filename)</td>
</tr>
<tr class="memdesc:ga6d80876bcae54f47cde79d0bce20321d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the filename is an absolute path.<br />
</td>
</tr>
<tr class="separator:ga6d80876bcae54f47cde79d0bce20321d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga04e98ad0e3a181f0a5921a4cbc49cf08" class="memitem:ga04e98ad0e3a181f0a5921a4cbc49cf08">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_stat (const DBusString *filename, DBusStat *statbuf, DBusError *error)</td>
</tr>
<tr class="memdesc:ga04e98ad0e3a181f0a5921a4cbc49cf08">
<td class="mdescLeft"> </td>
<td class="mdescRight">stat() wrapper.<br />
</td>
</tr>
<tr class="separator:ga04e98ad0e3a181f0a5921a4cbc49cf08">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga387d7e6643322c9813b62edf441bf13e" class="memitem:ga387d7e6643322c9813b62edf441bf13e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDirIter * </td>
<td class="memItemRight" data-valign="bottom">_dbus_directory_open (const DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:ga387d7e6643322c9813b62edf441bf13e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Open a directory to iterate over.<br />
</td>
</tr>
<tr class="separator:ga387d7e6643322c9813b62edf441bf13e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab9a2ddb130da035d6186f2d96bf37cb4" class="memitem:gab9a2ddb130da035d6186f2d96bf37cb4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_directory_get_next_file (DBusDirIter *iter, DBusString *filename, DBusError *error)</td>
</tr>
<tr class="memdesc:gab9a2ddb130da035d6186f2d96bf37cb4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get next file in the directory.<br />
</td>
</tr>
<tr class="separator:gab9a2ddb130da035d6186f2d96bf37cb4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1821b64302fe8e12278fa227eb11d393" class="memitem:ga1821b64302fe8e12278fa227eb11d393">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_directory_close (DBusDirIter *iter)</td>
</tr>
<tr class="memdesc:ga1821b64302fe8e12278fa227eb11d393">
<td class="mdescLeft"> </td>
<td class="mdescRight">Closes a directory iteration.<br />
</td>
</tr>
<tr class="separator:ga1821b64302fe8e12278fa227eb11d393">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga23814bdf1859c6aa52da1feab8f1aed4" class="memitem:ga23814bdf1859c6aa52da1feab8f1aed4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_group_info_fill (DBusGroupInfo *info, const DBusString *groupname, DBusError *error)</td>
</tr>
<tr class="memdesc:ga23814bdf1859c6aa52da1feab8f1aed4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes the given DBusGroupInfo struct with information about the given group name.<br />
</td>
</tr>
<tr class="separator:ga23814bdf1859c6aa52da1feab8f1aed4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad235e373b223982b7d3aba8a2b602b58" class="memitem:gad235e373b223982b7d3aba8a2b602b58">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_group_info_fill_gid (DBusGroupInfo *info, dbus_gid_t gid, DBusError *error)</td>
</tr>
<tr class="memdesc:gad235e373b223982b7d3aba8a2b602b58">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes the given DBusGroupInfo struct with information about the given group ID.<br />
</td>
</tr>
<tr class="separator:gad235e373b223982b7d3aba8a2b602b58">
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
<tr id="r_gaffa462e1c2f4e963a15cf3219159f8fe" class="memitem:gaffa462e1c2f4e963a15cf3219159f8fe">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_generate_random_bytes_buffer (char *buffer, int n_bytes, DBusError *error)</td>
</tr>
<tr class="memdesc:gaffa462e1c2f4e963a15cf3219159f8fe">
<td class="mdescLeft"> </td>
<td class="mdescRight">Fills n_bytes of the given buffer with random bytes.<br />
</td>
</tr>
<tr class="separator:gaffa462e1c2f4e963a15cf3219159f8fe">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8969e1311a43f4ff645866f7d6cd579f" class="memitem:ga8969e1311a43f4ff645866f7d6cd579f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_generate_random_ascii (DBusString *str, int n_bytes, DBusError *error)</td>
</tr>
<tr class="memdesc:ga8969e1311a43f4ff645866f7d6cd579f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Generates the given number of random bytes, where the bytes are chosen from the alphanumeric ASCII subset.<br />
</td>
</tr>
<tr class="separator:ga8969e1311a43f4ff645866f7d6cd579f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga466ecb6acf109fa5ff4621d5d09ac2ad" class="memitem:ga466ecb6acf109fa5ff4621d5d09ac2ad">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_error_from_errno (int error_number)</td>
</tr>
<tr class="memdesc:ga466ecb6acf109fa5ff4621d5d09ac2ad">
<td class="mdescLeft"> </td>
<td class="mdescRight">Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.<br />
</td>
</tr>
<tr class="separator:ga466ecb6acf109fa5ff4621d5d09ac2ad">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga993b69bdf270359be792a683b51fbba7" class="memitem:ga993b69bdf270359be792a683b51fbba7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_error_from_system_errno (void)</td>
</tr>
<tr class="memdesc:ga993b69bdf270359be792a683b51fbba7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Converts the current system errno value into a DBusError name.<br />
</td>
</tr>
<tr class="separator:ga993b69bdf270359be792a683b51fbba7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf0f4cb7f145fe1f48f5302277560407a" class="memitem:gaf0f4cb7f145fe1f48f5302277560407a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_set_errno_to_zero (void)</td>
</tr>
<tr class="memdesc:gaf0f4cb7f145fe1f48f5302277560407a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Assign 0 to the global errno variable.<br />
</td>
</tr>
<tr class="separator:gaf0f4cb7f145fe1f48f5302277560407a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf8962f4044a2a8689eb95a0ffd08b837" class="memitem:gaf8962f4044a2a8689eb95a0ffd08b837">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_is_errno_enomem (int e)</td>
</tr>
<tr class="memdesc:gaf8962f4044a2a8689eb95a0ffd08b837">
<td class="mdescLeft"> </td>
<td class="mdescRight">See if errno is ENOMEM.<br />
</td>
</tr>
<tr class="separator:gaf8962f4044a2a8689eb95a0ffd08b837">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae638e92d9bbeef287421a0f2d5837b9a" class="memitem:gae638e92d9bbeef287421a0f2d5837b9a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_is_errno_eintr (int e)</td>
</tr>
<tr class="memdesc:gae638e92d9bbeef287421a0f2d5837b9a">
<td class="mdescLeft"> </td>
<td class="mdescRight">See if errno is EINTR.<br />
</td>
</tr>
<tr class="separator:gae638e92d9bbeef287421a0f2d5837b9a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga07d3d26556b75d728fd1755baddb0792" class="memitem:ga07d3d26556b75d728fd1755baddb0792">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_is_errno_epipe (int e)</td>
</tr>
<tr class="memdesc:ga07d3d26556b75d728fd1755baddb0792">
<td class="mdescLeft"> </td>
<td class="mdescRight">See if errno is EPIPE.<br />
</td>
</tr>
<tr class="separator:ga07d3d26556b75d728fd1755baddb0792">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0e84d22f6cc293eef3c4f4f465ef1d9f" class="memitem:ga0e84d22f6cc293eef3c4f4f465ef1d9f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_is_errno_etoomanyrefs (int e)</td>
</tr>
<tr class="memdesc:ga0e84d22f6cc293eef3c4f4f465ef1d9f">
<td class="mdescLeft"> </td>
<td class="mdescRight">See if errno is ETOOMANYREFS.<br />
</td>
</tr>
<tr class="separator:ga0e84d22f6cc293eef3c4f4f465ef1d9f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa9c663663bb66530e5787c7ee8652a6a" class="memitem:gaa9c663663bb66530e5787c7ee8652a6a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_strerror_from_errno (void)</td>
</tr>
<tr class="memdesc:gaa9c663663bb66530e5787c7ee8652a6a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get error message from errno.<br />
</td>
</tr>
<tr class="separator:gaa9c663663bb66530e5787c7ee8652a6a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga432be9089bad53d3e9eab60cacb69eea" class="memitem:ga432be9089bad53d3e9eab60cacb69eea">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_log (DBusSystemLogSeverity severity, const char *msg,...)</td>
</tr>
<tr class="memdesc:ga432be9089bad53d3e9eab60cacb69eea">
<td class="mdescLeft"> </td>
<td class="mdescRight">Log a message to the system log file (e.g.<br />
</td>
</tr>
<tr class="separator:ga432be9089bad53d3e9eab60cacb69eea">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga052a2867cb74911e28b3055397d73526" class="memitem:ga052a2867cb74911e28b3055397d73526">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_inet_sockaddr_to_string (const void *sockaddr_pointer, size_t len, char *string, size_t string_len, const char **family_name, dbus_uint16_t *port, DBusError *error)</td>
</tr>
<tr class="separator:ga052a2867cb74911e28b3055397d73526">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga176d8ed4425894cf6ebe315b2fa9ce24" class="memitem:ga176d8ed4425894cf6ebe315b2fa9ce24">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_set_error_with_inet_sockaddr (DBusError *error, const void *sockaddr_pointer, size_t len, const char *description, int saved_errno)</td>
</tr>
<tr class="separator:ga176d8ed4425894cf6ebe315b2fa9ce24">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaebe1c886a34697762ca8b213fda28c95" class="memitem:gaebe1c886a34697762ca8b213fda28c95">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_combine_tcp_errors (DBusList **sources, const char *summary, const char *host, const char *port, DBusError *dest)</td>
</tr>
<tr class="separator:gaebe1c886a34697762ca8b213fda28c95">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa504db352a939909051a494d06c5b607" class="memitem:gaa504db352a939909051a494d06c5b607">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_is_console_user (dbus_uid_t uid, DBusError *error)</td>
</tr>
<tr class="memdesc:gaa504db352a939909051a494d06c5b607">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks to see if the UID sent in is the console user.<br />
</td>
</tr>
<tr class="separator:gaa504db352a939909051a494d06c5b607">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf07ee24eddcb3b0f85fa54196bc44fe1" class="memitem:gaf07ee24eddcb3b0f85fa54196bc44fe1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_user_id (const DBusString *username, dbus_uid_t *uid)</td>
</tr>
<tr class="memdesc:gaf07ee24eddcb3b0f85fa54196bc44fe1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets user ID given username.<br />
</td>
</tr>
<tr class="separator:gaf07ee24eddcb3b0f85fa54196bc44fe1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga90657adefa9bbac9b35eee63dd46a854" class="memitem:ga90657adefa9bbac9b35eee63dd46a854">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_group_id (const DBusString *groupname, dbus_gid_t *gid)</td>
</tr>
<tr class="memdesc:ga90657adefa9bbac9b35eee63dd46a854">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets group ID given groupname.<br />
</td>
</tr>
<tr class="separator:ga90657adefa9bbac9b35eee63dd46a854">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac82f42ff83fabbde717cc08569265e6e" class="memitem:gac82f42ff83fabbde717cc08569265e6e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_get_user_id_and_primary_group (const DBusString *username, dbus_uid_t *uid_p, dbus_gid_t *gid_p)</td>
</tr>
<tr class="memdesc:gac82f42ff83fabbde717cc08569265e6e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets user ID and primary group given username.<br />
</td>
</tr>
<tr class="separator:gac82f42ff83fabbde717cc08569265e6e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab347de9428eaf2fddf662fc10b89b08a" class="memitem:gab347de9428eaf2fddf662fc10b89b08a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const DBusGroupInfo * </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_lookup_group (DBusUserDatabase *db, dbus_gid_t gid, const DBusString *groupname, DBusError *error)</td>
</tr>
<tr class="memdesc:gab347de9428eaf2fddf662fc10b89b08a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Looks up a gid or group name in the user database.<br />
</td>
</tr>
<tr class="separator:gab347de9428eaf2fddf662fc10b89b08a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab62250fecd431cbf5722a424429099dd" class="memitem:gab62250fecd431cbf5722a424429099dd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_groups_from_uid (dbus_uid_t uid, dbus_gid_t **group_ids, int *n_group_ids, DBusError *error)</td>
</tr>
<tr class="memdesc:gab62250fecd431cbf5722a424429099dd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets all groups corresponding to the given UID.<br />
</td>
</tr>
<tr class="separator:gab62250fecd431cbf5722a424429099dd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga95fe7aa01f76ddfde7244ddb9d91531d" class="memitem:ga95fe7aa01f76ddfde7244ddb9d91531d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_info_unref (DBusUserInfo *info)</td>
</tr>
<tr class="memdesc:ga95fe7aa01f76ddfde7244ddb9d91531d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count.<br />
</td>
</tr>
<tr class="separator:ga95fe7aa01f76ddfde7244ddb9d91531d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga93fe47adff3f4486f82bcafedcaec21b" class="memitem:ga93fe47adff3f4486f82bcafedcaec21b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_group_info_unref (DBusGroupInfo *info)</td>
</tr>
<tr class="memdesc:ga93fe47adff3f4486f82bcafedcaec21b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count.<br />
</td>
</tr>
<tr class="separator:ga93fe47adff3f4486f82bcafedcaec21b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa40334f7b4f185a437a8bc6d6e0994a1" class="memitem:gaa40334f7b4f185a437a8bc6d6e0994a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_info_free (DBusUserInfo *info)</td>
</tr>
<tr class="memdesc:gaa40334f7b4f185a437a8bc6d6e0994a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees the members of info (but not info itself)<br />
</td>
</tr>
<tr class="separator:gaa40334f7b4f185a437a8bc6d6e0994a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac2d226476e6fff50bdfaace18b897fe9" class="memitem:gac2d226476e6fff50bdfaace18b897fe9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_group_info_free (DBusGroupInfo *info)</td>
</tr>
<tr class="memdesc:gac2d226476e6fff50bdfaace18b897fe9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees the members of info (but not info itself).<br />
</td>
</tr>
<tr class="separator:gac2d226476e6fff50bdfaace18b897fe9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad1c3538c544df91f438a13c9fb4d3a1b" class="memitem:gad1c3538c544df91f438a13c9fb4d3a1b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_is_a_number (const DBusString *str, unsigned long *num)</td>
</tr>
<tr class="memdesc:gad1c3538c544df91f438a13c9fb4d3a1b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks if a given string is actually a number and converts it if it is.<br />
</td>
</tr>
<tr class="separator:gad1c3538c544df91f438a13c9fb4d3a1b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga945d2c702cc31f3b30b8f915a6ff0c4c" class="memitem:ga945d2c702cc31f3b30b8f915a6ff0c4c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const DBusUserInfo * </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_lookup (DBusUserDatabase *db, dbus_uid_t uid, const DBusString *username, DBusError *error)</td>
</tr>
<tr class="memdesc:ga945d2c702cc31f3b30b8f915a6ff0c4c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Looks up a uid or username in the user database.<br />
</td>
</tr>
<tr class="separator:ga945d2c702cc31f3b30b8f915a6ff0c4c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga15df3b3fdaa4946f69ff87f3a9a03fe7" class="memitem:ga15df3b3fdaa4946f69ff87f3a9a03fe7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_lock_system (void)</td>
</tr>
<tr class="memdesc:ga15df3b3fdaa4946f69ff87f3a9a03fe7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Locks global system user database.<br />
</td>
</tr>
<tr class="separator:ga15df3b3fdaa4946f69ff87f3a9a03fe7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga468e1d62e1df24bb699c4a37fdfa274c" class="memitem:ga468e1d62e1df24bb699c4a37fdfa274c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_unlock_system (void)</td>
</tr>
<tr class="memdesc:ga468e1d62e1df24bb699c4a37fdfa274c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unlocks global system user database.<br />
</td>
</tr>
<tr class="separator:ga468e1d62e1df24bb699c4a37fdfa274c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf21860c6e54f3aecbb6f2b5570d62f9a" class="memitem:gaf21860c6e54f3aecbb6f2b5570d62f9a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusUserDatabase * </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_get_system (void)</td>
</tr>
<tr class="memdesc:gaf21860c6e54f3aecbb6f2b5570d62f9a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the system global user database; must be called with lock held (_dbus_user_database_lock_system()).<br />
</td>
</tr>
<tr class="separator:gaf21860c6e54f3aecbb6f2b5570d62f9a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga788ce7775d7f812d28d931e8b87ddfde" class="memitem:ga788ce7775d7f812d28d931e8b87ddfde">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_flush_system (void)</td>
</tr>
<tr class="memdesc:ga788ce7775d7f812d28d931e8b87ddfde">
<td class="mdescLeft"> </td>
<td class="mdescRight">Flushes the system global user database;.<br />
</td>
</tr>
<tr class="separator:ga788ce7775d7f812d28d931e8b87ddfde">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9c4c1850787bfd457107b95fa1878869" class="memitem:ga9c4c1850787bfd457107b95fa1878869">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_username_from_current_process (const DBusString **username)</td>
</tr>
<tr class="memdesc:ga9c4c1850787bfd457107b95fa1878869">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets username of user owning current process.<br />
</td>
</tr>
<tr class="separator:ga9c4c1850787bfd457107b95fa1878869">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga17ce3ab061a3ae2441cd33ece34f5e7a" class="memitem:ga17ce3ab061a3ae2441cd33ece34f5e7a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_homedir_from_current_process (const DBusString **homedir)</td>
</tr>
<tr class="memdesc:ga17ce3ab061a3ae2441cd33ece34f5e7a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets homedir of user owning current process.<br />
</td>
</tr>
<tr class="separator:ga17ce3ab061a3ae2441cd33ece34f5e7a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabdd1dc47f44e3d6702c86c68da9a0173" class="memitem:gabdd1dc47f44e3d6702c86c68da9a0173">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_homedir_from_uid (dbus_uid_t uid, DBusString *homedir)</td>
</tr>
<tr class="memdesc:gabdd1dc47f44e3d6702c86c68da9a0173">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the home directory for the given user.<br />
</td>
</tr>
<tr class="separator:gabdd1dc47f44e3d6702c86c68da9a0173">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5b480c61a00094aad60d0c8bb9126c1e" class="memitem:ga5b480c61a00094aad60d0c8bb9126c1e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_add_from_user (DBusCredentials *credentials, const DBusString *username, DBusCredentialsAddFlags flags, DBusError *error)</td>
</tr>
<tr class="memdesc:ga5b480c61a00094aad60d0c8bb9126c1e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds the credentials corresponding to the given username.<br />
</td>
</tr>
<tr class="separator:ga5b480c61a00094aad60d0c8bb9126c1e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2a5e4b66be4fdcb70146f09da47eb56f" class="memitem:ga2a5e4b66be4fdcb70146f09da47eb56f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusUserDatabase * </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_new (void)</td>
</tr>
<tr class="memdesc:ga2a5e4b66be4fdcb70146f09da47eb56f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new user database object used to look up and cache user information.<br />
</td>
</tr>
<tr class="separator:ga2a5e4b66be4fdcb70146f09da47eb56f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab553751e96f8506d10349fb5fb1eaa82" class="memitem:gab553751e96f8506d10349fb5fb1eaa82">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_flush (DBusUserDatabase *db)</td>
</tr>
<tr class="memdesc:gab553751e96f8506d10349fb5fb1eaa82">
<td class="mdescLeft"> </td>
<td class="mdescRight">Flush all information out of the user database.<br />
</td>
</tr>
<tr class="separator:gab553751e96f8506d10349fb5fb1eaa82">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga55dbb78c415da040037442eca4c4e80e" class="memitem:ga55dbb78c415da040037442eca4c4e80e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_unref (DBusUserDatabase *db)</td>
</tr>
<tr class="memdesc:ga55dbb78c415da040037442eca4c4e80e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements refcount of user database.<br />
</td>
</tr>
<tr class="separator:ga55dbb78c415da040037442eca4c4e80e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6a7e8b8cf3a6968972e9a49726022638" class="memitem:ga6a7e8b8cf3a6968972e9a49726022638">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_get_uid (DBusUserDatabase *db, dbus_uid_t uid, const DBusUserInfo **info, DBusError *error)</td>
</tr>
<tr class="memdesc:ga6a7e8b8cf3a6968972e9a49726022638">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the user information for the given UID, returned user info should not be freed.<br />
</td>
</tr>
<tr class="separator:ga6a7e8b8cf3a6968972e9a49726022638">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaccf1d5b330707a1835dcf4ce49a29c8c" class="memitem:gaccf1d5b330707a1835dcf4ce49a29c8c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_database_get_username (DBusUserDatabase *db, const DBusString *username, const DBusUserInfo **info, DBusError *error)</td>
</tr>
<tr class="memdesc:gaccf1d5b330707a1835dcf4ce49a29c8c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the user information for the given username.<br />
</td>
</tr>
<tr class="separator:gaccf1d5b330707a1835dcf4ce49a29c8c">
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
<td colspan="2"><h2 id="variables" class="groupheader"> Variables</h2></td>
</tr>
<tr id="r_gadb458811a027c9bbae57216a4c33a5f7" class="memitem:gadb458811a027c9bbae57216a4c33a5f7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_no_memory_message = "Not enough memory"</td>
</tr>
<tr class="memdesc:gadb458811a027c9bbae57216a4c33a5f7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Fixed "out of memory" error message, just to avoid making up a different string every time and wasting space.<br />
</td>
</tr>
<tr class="separator:gadb458811a027c9bbae57216a4c33a5f7">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Utility functions (\_dbus_assert(), \_dbus_warn(), etc.)

## Macro Definition Documentation

## ◆ \_dbus_assert

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define \_dbus_assert | ( |   | condition | ) |     \_dbus_real_assert ((condition) != 0, \#condition, \_\_FILE\_\_, \_\_LINE\_\_, \_DBUS_FUNCTION_NAME) |

Aborts with an error message if the condition is false.

Parameters  
|           |                               |
|-----------|-------------------------------|
| condition | condition which must be true. |

Definition at line 153 of file dbus-internals.h.

## ◆ \_dbus_assert_not_reached

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define \_dbus_assert_not_reached | ( |   | explanation | ) |     \_dbus_real_assert_not_reached (explanation, \_\_FILE\_\_, \_\_LINE\_\_) |

Aborts with an error message if called.

The given explanation will be printed.

Parameters  
|             |                                                       |
|-------------|-------------------------------------------------------|
| explanation | explanation of what happened if the code was reached. |

Definition at line 164 of file dbus-internals.h.

## ◆ \_DBUS_INT16_MAX

|                                                     |
|-----------------------------------------------------|
| \#define \_DBUS_INT16_MAX   ((dbus_int16_t) 0x7fff) |

Maximum value of type "int16".

Definition at line 320 of file dbus-internals.h.

## ◆ \_DBUS_INT16_MIN

|                                                     |
|-----------------------------------------------------|
| \#define \_DBUS_INT16_MIN   ((dbus_int16_t) 0x8000) |

Minimum value of type "int16".

Definition at line 319 of file dbus-internals.h.

## ◆ \_DBUS_INT32_MAX

|                                                         |
|---------------------------------------------------------|
| \#define \_DBUS_INT32_MAX   ((dbus_int32_t) 0x7fffffff) |

Maximum value of type "int32".

Definition at line 323 of file dbus-internals.h.

## ◆ \_DBUS_INT32_MIN

|                                                         |
|---------------------------------------------------------|
| \#define \_DBUS_INT32_MIN   ((dbus_int32_t) 0x80000000) |

Minimum value of type "int32".

Definition at line 322 of file dbus-internals.h.

## ◆ \_DBUS_INT_MAX

|                                            |
|--------------------------------------------|
| \#define \_DBUS_INT_MAX   \_DBUS_INT32_MAX |

Maximum value of type "int".

Definition at line 327 of file dbus-internals.h.

## ◆ \_DBUS_INT_MIN

|                                            |
|--------------------------------------------|
| \#define \_DBUS_INT_MIN   \_DBUS_INT32_MIN |

Minimum value of type "int".

Definition at line 326 of file dbus-internals.h.

## ◆ \_DBUS_INT_TO_POINTER

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define \_DBUS_INT_TO_POINTER | ( |   | integer | ) |    ((void\*)((intptr_t)(integer))) |

Safely stuffs an integer into a pointer, to be extracted later with \_DBUS_POINTER_TO_INT.

Only guaranteed to preserve 32 bits.

Parameters  
|         |                                      |
|---------|--------------------------------------|
| integer | the integer to stuff into a pointer. |

Definition at line 192 of file dbus-internals.h.

## ◆ \_DBUS_LOCK

|                      |     |     |      |     |                                      |
|----------------------|-----|-----|------|-----|--------------------------------------|
| \#define \_DBUS_LOCK | (   |     | name | )   |    \_dbus_lock (\_DBUS_LOCK\_##name) |

Locks a global lock, initializing it first if necessary.

Returns  
FALSE if not enough memory

Definition at line 437 of file dbus-internals.h.

## ◆ \_DBUS_LOCK_NAME

|                           |     |     |      |     |                        |
|---------------------------|-----|-----|------|-----|------------------------|
| \#define \_DBUS_LOCK_NAME | (   |     | name | )   |    \_DBUS_LOCK\_##name |

Expands to name of a global lock variable.

Definition at line 436 of file dbus-internals.h.

## ◆ \_DBUS_N_ELEMENTS

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define \_DBUS_N_ELEMENTS | ( |   | array | ) |    ((int) (sizeof ((array)) / sizeof ((array)\[0\]))) |

Computes the number of elements in a fixed-size array using sizeof().

Parameters  
|       |                                 |
|-------|---------------------------------|
| array | the array to count elements in. |

Definition at line 189 of file dbus-internals.h.

## ◆ \_DBUS_POINTER_TO_INT

|                                |     |     |         |     |                          |
|--------------------------------|-----|-----|---------|-----|--------------------------|
| \#define \_DBUS_POINTER_TO_INT | (   |     | pointer | )   |    ((intptr_t)(pointer)) |

Safely casts a void\* to an integer; should only be used on void\* that actually contain integers, for example one created with \_DBUS_INT_TO_POINTER.

Only guaranteed to preserve 32 bits. (i.e. it's used to store 32-bit ints in pointers, but can't be used to store 64-bit pointers in ints.)

Parameters  
|         |                                     |
|---------|-------------------------------------|
| pointer | pointer to extract an integer from. |

Definition at line 191 of file dbus-internals.h.

## ◆ \_DBUS_UINT16_MAX

|                                                      |
|------------------------------------------------------|
| \#define \_DBUS_UINT16_MAX   ((dbus_uint16_t)0xffff) |

Maximum value of type "uint16".

Definition at line 321 of file dbus-internals.h.

## ◆ \_DBUS_UINT32_MAX

|                                                          |
|----------------------------------------------------------|
| \#define \_DBUS_UINT32_MAX   ((dbus_uint32_t)0xffffffff) |

Maximum value of type "uint32".

Definition at line 324 of file dbus-internals.h.

## ◆ \_DBUS_UINT_MAX

|                                              |
|----------------------------------------------|
| \#define \_DBUS_UINT_MAX   \_DBUS_UINT32_MAX |

Maximum value of type "uint".

Definition at line 328 of file dbus-internals.h.

## ◆ \_DBUS_UNLOCK

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define \_DBUS_UNLOCK | ( |   | name | ) |    \_dbus_unlock (\_DBUS_LOCK\_##name) |

Unlocks a global lock.

Definition at line 438 of file dbus-internals.h.

## ◆ \_DBUS_ZERO

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define \_DBUS_ZERO | ( |   | object | ) |    (memset (&(object), '\0', sizeof ((object)))) |

Sets all bits in an object to zero.

Parameters  
|        |                          |
|--------|--------------------------|
| object | the object to be zeroed. |

Definition at line 194 of file dbus-internals.h.

## ◆ LIVE_CHILDREN

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define LIVE_CHILDREN | ( |   | sitter | ) |    ((sitter)-\>socket_to_babysitter.fd \>= 0 \|\| (sitter)-\>error_pipe_from_child \>= 0) |

Macro returns TRUE if the babysitter still has live sockets open to the babysitter child or the grandchild.

Definition at line 697 of file dbus-spawn-unix.c.

## ◆ READ_END

|                       |
|-----------------------|
| \#define READ_END   0 |

Helps remember which end of the pipe is which.

Definition at line 895 of file dbus-spawn-unix.c.

## ◆ WRITE_END

|                        |
|------------------------|
| \#define WRITE_END   1 |

Helps remember which end of the pipe is which.

Definition at line 897 of file dbus-spawn-unix.c.

## Enumeration Type Documentation

## ◆ anonymous enum

|                |
|----------------|
| anonymous enum |

Definition at line 240 of file dbus-spawn-unix.c.

## ◆ ReadStatus

|                 |
|-----------------|
| enum ReadStatus |

Enumeration for status of a read()

| Enumerator         |                     |
|--------------------|---------------------|
| READ_STATUS_OK     | Read succeeded.     |
| READ_STATUS_ERROR  | Some kind of error. |
| READ_STATUS_EOF    | EOF returned.       |

Definition at line 75 of file dbus-spawn-unix.c.

## Function Documentation

## ◆ \_dbus_babysitter_get_child_exit_status()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_babysitter_get_child_exit_status | ( | DBusBabysitter \*  | *sitter*, |
|  |  | int \*  | *status*  |
|  | ) |  |  |

Gets the exit status of the child.

We do this so implementation specific detail is not cluttering up dbus, for example the system launcher code. This can only be called if the child has exited, i.e. call \_dbus_babysitter_get_child_exited(). It returns FALSE if the child did not return a status code, e.g. because the child was signaled or we failed to ever launch the child in the first place.

Parameters  
|        |                          |
|--------|--------------------------|
| sitter | the babysitter           |
| status | the returned status code |

<!-- -->

Returns  
FALSE on failure

Definition at line 753 of file dbus-spawn-unix.c.

References \_dbus_assert_not_reached, \_dbus_babysitter_get_child_exited(), FALSE, DBusBabysitter::have_child_status, DBusBabysitter::status, and TRUE.

## ◆ \_dbus_babysitter_get_child_exited()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_babysitter_get_child_exited | ( | DBusBabysitter \*  | *sitter* | ) |  |

Checks whether the child has exited, without blocking.

Parameters  
|        |                |
|--------|----------------|
| sitter | the babysitter |

Definition at line 728 of file dbus-spawn-unix.c.

References FALSE, LIVE_CHILDREN, and DBusBabysitter::socket_to_babysitter.

Referenced by \_dbus_babysitter_get_child_exit_status(), and \_dbus_babysitter_set_child_exit_error().

## ◆ \_dbus_babysitter_kill_child()

|                                   |     |                    |          |     |     |
|-----------------------------------|-----|--------------------|----------|-----|-----|
| void \_dbus_babysitter_kill_child | (   | DBusBabysitter \*  | *sitter* | )   |     |

Blocks until the babysitter process gives us the PID of the spawned grandchild, then kills the spawned grandchild.

Parameters  
|        |                       |
|--------|-----------------------|
| sitter | the babysitter object |

Definition at line 706 of file dbus-spawn-unix.c.

References DBusBabysitter::grandchild_pid, LIVE_CHILDREN, and TRUE.

## ◆ \_dbus_babysitter_ref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusBabysitter \* \_dbus_babysitter_ref | ( | DBusBabysitter \*  | *sitter* | ) |  |

Increment the reference count on the babysitter object.

Parameters  
|        |                |
|--------|----------------|
| sitter | the babysitter |

<!-- -->

Returns  
the babysitter

Definition at line 314 of file dbus-spawn-unix.c.

References \_dbus_assert, NULL, and DBusBabysitter::refcount.

## ◆ \_dbus_babysitter_set_child_exit_error()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_babysitter_set_child_exit_error | ( | DBusBabysitter \*  | *sitter*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Sets the DBusError with an explanation of why the spawned child process exited (on a signal, or whatever).

If the child process has not exited, does nothing (error will remain unset).

Parameters  
|        |                     |
|--------|---------------------|
| sitter | the babysitter      |
| error  | an error to fill in |

Definition at line 777 of file dbus-spawn-unix.c.

References \_dbus_babysitter_get_child_exited(), DBUS_ERROR_FAILED, DBUS_ERROR_NO_MEMORY, DBUS_ERROR_SPAWN_CHILD_EXITED, DBUS_ERROR_SPAWN_CHILD_SIGNALED, DBUS_ERROR_SPAWN_EXEC_FAILED, dbus_set_error(), DBusBabysitter::errnum, DBusBabysitter::have_child_status, DBusBabysitter::have_exec_errnum, DBusBabysitter::have_fork_errnum, DBusBabysitter::log_name, and DBusBabysitter::status.

## ◆ \_dbus_babysitter_set_result_function()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_babysitter_set_result_function | ( | DBusBabysitter \*  | *sitter*, |
|  |  | DBusBabysitterFinishedFunc  | *finished*, |
|  |  | void \*  | *user_data*  |
|  | ) |  |  |

Definition at line 1535 of file dbus-spawn-unix.c.

## ◆ \_dbus_babysitter_set_watch_functions()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_babysitter_set_watch_functions | ( | DBusBabysitter \*  | *sitter*, |
|  |  | DBusAddWatchFunction  | *add_function*, |
|  |  | DBusRemoveWatchFunction  | *remove_function*, |
|  |  | DBusWatchToggledFunction  | *toggled_function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets watch functions to notify us when the babysitter object needs to read/write file descriptors.

Parameters  
|                    |                                                       |
|--------------------|-------------------------------------------------------|
| sitter             | the babysitter                                        |
| add_function       | function to begin monitoring a new descriptor.        |
| remove_function    | function to stop monitoring a descriptor.             |
| toggled_function   | function to notify when the watch is enabled/disabled |
| data               | data to pass to add_function and remove_function.     |
| free_data_function | function to be called to free the data.               |

<!-- -->

Returns  
FALSE on failure (no memory)

Definition at line 835 of file dbus-spawn-unix.c.

References \_dbus_watch_list_set_functions(), and DBusBabysitter::watches.

## ◆ \_dbus_babysitter_unref()

|                              |     |                    |          |     |     |
|------------------------------|-----|--------------------|----------|-----|-----|
| void \_dbus_babysitter_unref | (   | DBusBabysitter \*  | *sitter* | )   |     |

Decrement the reference count on the babysitter object.

When the reference count of the babysitter object reaches zero, the babysitter is killed and the child that was being babysat gets emancipated.

Parameters  
|        |                |
|--------|----------------|
| sitter | the babysitter |

Definition at line 336 of file dbus-spawn-unix.c.

References \_dbus_assert, \_dbus_warn(), \_dbus_watch_list_free(), dbus_free(), DBusBabysitter::log_name, NULL, DBusBabysitter::refcount, DBusBabysitter::sitter_pid, DBusBabysitter::status, and DBusBabysitter::watches.

Referenced by \_dbus_spawn_async_with_babysitter().

## ◆ \_dbus_become_daemon()

|                                  |     |                      |                   |
|----------------------------------|-----|----------------------|-------------------|
| dbus_bool_t \_dbus_become_daemon | (   | const DBusString \*  | *pidfile*,        |
|                                  |     | DBusPipe \*          | *print_pid_pipe*, |
|                                  |     | DBusError \*         | *error*,          |
|                                  |     | dbus_bool_t          | *keep_umask*      |
|                                  | )   |                      |                   |

Does the chdir, fork, setsid, etc.

to become a daemon process.

Parameters  
|                |                                               |
|----------------|-----------------------------------------------|
| pidfile        | NULL, or pidfile to create                    |
| print_pid_pipe | pipe to print daemon's pid to, or -1 for none |
| error          | return location for errors                    |
| keep_umask     | TRUE to keep the original umask               |

<!-- -->

Returns  
FALSE on failure

Definition at line 86 of file dbus-sysdeps-util-unix.c.

References \_dbus_assert_not_reached, \_dbus_ensure_standard_fds(), \_dbus_error_from_errno(), \_dbus_getenv(), \_dbus_warn(), \_dbus_write_pid_to_file_and_pipe(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, DBusError::message, NULL, and TRUE.

## ◆ \_dbus_change_to_daemon_user()

|                                          |     |                |          |
|------------------------------------------|-----|----------------|----------|
| dbus_bool_t \_dbus_change_to_daemon_user | (   | const char \*  | *user*,  |
|                                          |     | DBusError \*   | *error*  |
|                                          | )   |                |          |

Changes the user and group the bus is running as.

Parameters  
|       |                            |
|-------|----------------------------|
| user  | the user to become         |
| error | return location for errors |

<!-- -->

Returns  
FALSE on failure

Definition at line 333 of file dbus-sysdeps-util-unix.c.

References \_dbus_error_from_errno(), \_dbus_get_user_id_and_primary_group(), \_dbus_string_init_const(), \_dbus_warn(), DBUS_ERROR_FAILED, dbus_set_error(), FALSE, NULL, and TRUE.

## ◆ \_dbus_combine_tcp_errors()

|                                |     |                |            |
|--------------------------------|-----|----------------|------------|
| void \_dbus_combine_tcp_errors | (   | DBusList \*\*  | *sources*, |
|                                |     | const char \*  | *summary*, |
|                                |     | const char \*  | *host*,    |
|                                |     | const char \*  | *port*,    |
|                                |     | DBusError \*   | *dest*     |
|                                | )   |                |            |

Definition at line 877 of file dbus-sysdeps.c.

## ◆ \_dbus_credentials_add_from_user()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_add_from_user | ( | DBusCredentials \*  | *credentials*, |
|  |  | const DBusString \*  | *username*, |
|  |  | DBusCredentialsAddFlags  | *flags*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Adds the credentials corresponding to the given username.

Used among other purposes to parses a desired identity provided from a client in the auth protocol. On UNIX this means parsing a UID, on Windows probably parsing an SID string.

Parameters  
|             |                        |
|-------------|------------------------|
| credentials | credentials to fill in |
| username    | the username           |

<!-- -->

Returns  
TRUE if the username existed and we got some credentials

Definition at line 525 of file dbus-userdb.c.

References \_dbus_credentials_add_unix_uid(), \_dbus_is_a_number(), \_dbus_user_database_get_system(), \_dbus_user_database_get_username(), \_dbus_user_database_lock_system(), \_dbus_user_database_unlock_system(), DBUS_ERROR_INVALID_ARGS, dbus_set_error(), DBUS_UID_UNSET, FALSE, NULL, TRUE, and DBusUserInfo::uid.

## ◆ \_dbus_directory_close()

|                             |     |                 |        |     |     |
|-----------------------------|-----|-----------------|--------|-----|-----|
| void \_dbus_directory_close | (   | DBusDirIter \*  | *iter* | )   |     |

Closes a directory iteration.

Definition at line 737 of file dbus-sysdeps-util-unix.c.

References DBusDirIter::d, and dbus_free().

## ◆ \_dbus_directory_get_next_file()

|                                            |     |                 |             |
|--------------------------------------------|-----|-----------------|-------------|
| dbus_bool_t \_dbus_directory_get_next_file | (   | DBusDirIter \*  | *iter*,     |
|                                            |     | DBusString \*   | *filename*, |
|                                            |     | DBusError \*    | *error*     |
|                                            | )   |                 |             |

Get next file in the directory.

Will not return "." or ".." on UNIX. If an error occurs, the contents of "filename" are undefined. The error is never set if the function succeeds.

This function is not re-entrant, and not necessarily thread-safe. Only use it for test code or single-threaded utilities.

Parameters  
|          |                                              |
|----------|----------------------------------------------|
| iter     | the iterator                                 |
| filename | string to be set to the next file in the dir |
| error    | return location for error                    |

<!-- -->

Returns  
TRUE if filename was filled in with a new filename

Definition at line 689 of file dbus-sysdeps-util-unix.c.

References \_dbus_error_from_errno(), \_dbus_string_append(), \_dbus_string_set_length(), DBusDirIter::d, DBUS_ERROR_NO_MEMORY, dbus_set_error(), FALSE, and TRUE.

## ◆ \_dbus_directory_open()

|                                      |     |                      |             |
|--------------------------------------|-----|----------------------|-------------|
| DBusDirIter \* \_dbus_directory_open | (   | const DBusString \*  | *filename*, |
|                                      |     | DBusError \*         | *error*     |
|                                      | )   |                      |             |

Open a directory to iterate over.

Parameters  
|          |                                 |
|----------|---------------------------------|
| filename | the directory name              |
| error    | exception return object or NULL |

<!-- -->

Returns  
new iterator, or NULL on error

Definition at line 641 of file dbus-sysdeps-util-unix.c.

References \_dbus_error_from_errno(), \_dbus_string_get_const_data(), DBusDirIter::d, DBUS_ERROR_NO_MEMORY, dbus_new0, dbus_set_error(), and NULL.

## ◆ \_dbus_dup_string_array()

|                                   |     |                  |         |     |     |
|-----------------------------------|-----|------------------|---------|-----|-----|
| char \*\* \_dbus_dup_string_array | (   | const char \*\*  | *array* | )   |     |

Duplicates a string array.

Result may be freed with dbus_free_string_array(). Returns NULL if memory allocation fails. If the array to be duplicated is NULL, returns NULL.

Parameters  
|       |                     |
|-------|---------------------|
| array | array to duplicate. |

<!-- -->

Returns  
newly-allocated copy.

Definition at line 672 of file dbus-internals.c.

References \_dbus_strdup(), dbus_free_string_array(), dbus_new0, and NULL.

Referenced by \_dbus_auth_set_mechanisms(), and dbus_server_set_auth_mechanisms().

## ◆ \_dbus_error_from_errno()

|                                       |     |      |                |     |     |
|---------------------------------------|-----|------|----------------|-----|-----|
| const char \* \_dbus_error_from_errno | (   | int  | *error_number* | )   |     |

Converts a UNIX errno, or Windows errno or WinSock error value into a DBusError name.

Parameters  
|              |            |
|--------------|------------|
| error_number | the errno. |

<!-- -->

Returns  
an error name

Definition at line 565 of file dbus-sysdeps.c.

References DBUS_ERROR_ACCESS_DENIED, DBUS_ERROR_ADDRESS_IN_USE, DBUS_ERROR_FAILED, DBUS_ERROR_FILE_EXISTS, DBUS_ERROR_FILE_NOT_FOUND, DBUS_ERROR_LIMITS_EXCEEDED, DBUS_ERROR_NO_MEMORY, DBUS_ERROR_NO_NETWORK, DBUS_ERROR_NO_SERVER, DBUS_ERROR_NOT_SUPPORTED, and DBUS_ERROR_TIMEOUT.

Referenced by \_dbus_append_address_from_socket(), \_dbus_become_daemon(), \_dbus_change_to_daemon_user(), \_dbus_check_dir_is_private_to_user(), \_dbus_close(), \_dbus_close_socket(), \_dbus_command_for_pid(), \_dbus_connect_exec(), \_dbus_connect_unix_socket(), \_dbus_directory_get_next_file(), \_dbus_directory_open(), \_dbus_dup(), \_dbus_error_from_system_errno(), \_dbus_file_get_contents(), \_dbus_generate_random_bytes(), \_dbus_is_console_user(), \_dbus_listen_systemd_sockets(), \_dbus_listen_tcp_socket(), \_dbus_listen_unix_socket(), \_dbus_read_credentials_socket(), \_dbus_send_credentials_socket(), \_dbus_set_socket_nonblocking(), \_dbus_socketpair(), \_dbus_spawn_async_with_babysitter(), \_dbus_stat(), and \_dbus_string_save_to_file().

## ◆ \_dbus_error_from_system_errno()

|                                              |     |       |     |     |     |
|----------------------------------------------|-----|-------|-----|-----|-----|
| const char \* \_dbus_error_from_system_errno | (   | void  |     | )   |     |

Converts the current system errno value into a DBusError name.

Returns  
an error name

Definition at line 657 of file dbus-sysdeps.c.

References \_dbus_error_from_errno().

## ◆ \_dbus_file_exists()

|                                |     |                |        |     |     |
|--------------------------------|-----|----------------|--------|-----|-----|
| dbus_bool_t \_dbus_file_exists | (   | const char \*  | *file* | )   |     |

Checks if a file exists.

File interface.

Parameters  
|      |                       |
|------|-----------------------|
| file | full path to the file |

<!-- -->

Returns  
TRUE if file exists

Definition at line 564 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_generate_random_ascii()

|                                          |     |                |            |
|------------------------------------------|-----|----------------|------------|
| dbus_bool_t \_dbus_generate_random_ascii | (   | DBusString \*  | *str*,     |
|                                          |     | int            | *n_bytes*, |
|                                          |     | DBusError \*   | *error*    |
|                                          | )   |                |            |

Generates the given number of random bytes, where the bytes are chosen from the alphanumeric ASCII subset.

Parameters  
|         |                                                      |
|---------|------------------------------------------------------|
| str     | the string                                           |
| n_bytes | the number of random ASCII bytes to append to string |
| error   | location to store reason for failure                 |

<!-- -->

Returns  
TRUE on success, FALSE if no memory or other failure

Definition at line 525 of file dbus-sysdeps.c.

References \_dbus_assert, \_dbus_generate_random_bytes(), \_dbus_string_get_byte(), \_dbus_string_get_length(), \_dbus_string_set_byte(), \_dbus_string_validate_ascii(), FALSE, and TRUE.

Referenced by \_dbus_string_save_to_file().

## ◆ \_dbus_generate_random_bytes_buffer()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_generate_random_bytes_buffer | ( | char \*  | *buffer*, |
|  |  | int  | *n_bytes*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Fills n_bytes of the given buffer with random bytes.

Random numbers.

Parameters  
|         |                                           |
|---------|-------------------------------------------|
| buffer  | an allocated buffer                       |
| n_bytes | the number of bytes in buffer to write to |
| error   | location to store reason for failure      |

<!-- -->

Returns  
TRUE on success

Definition at line 491 of file dbus-sysdeps.c.

References \_dbus_generate_random_bytes(), \_dbus_string_copy_to_buffer(), \_dbus_string_free(), \_dbus_string_init(), FALSE, and TRUE.

Referenced by \_dbus_generate_uuid().

## ◆ \_dbus_generate_uuid()

|                                  |     |               |          |
|----------------------------------|-----|---------------|----------|
| dbus_bool_t \_dbus_generate_uuid | (   | DBusGUID \*   | *uuid*,  |
|                                  |     | DBusError \*  | *error*  |
|                                  | )   |               |          |

Generates a new UUID.

If you change how this is done, there's some text about it in the spec that should also change.

Parameters  
|       |                                      |
|-------|--------------------------------------|
| uuid  | the uuid to initialize               |
| error | location to store reason for failure |

<!-- -->

Returns  
TRUE on success

Definition at line 752 of file dbus-internals.c.

References \_dbus_generate_random_bytes_buffer(), \_dbus_get_real_time(), DBusGUID::as_bytes, DBusGUID::as_uint32s, dbus_error_free(), dbus_error_init(), dbus_set_error(), FALSE, DBusError::message, DBusError::name, NULL, and TRUE.

Referenced by \_dbus_create_uuid(), \_dbus_read_local_machine_uuid(), \_dbus_read_uuid_file(), and \_dbus_server_init_base().

## ◆ \_dbus_get_check_failed_count()

|                                   |     |       |     |     |     |
|-----------------------------------|-----|-------|-----|-----|-----|
| int \_dbus_get_check_failed_count | (   | void  |     | )   |     |

Definition at line 231 of file dbus-internals.c.

## ◆ \_dbus_get_group_id()

|                                 |     |                      |              |
|---------------------------------|-----|----------------------|--------------|
| dbus_bool_t \_dbus_get_group_id | (   | const DBusString \*  | *groupname*, |
|                                 |     | dbus_gid_t \*        | *gid*        |
|                                 | )   |                      |              |

Gets group ID given groupname.

Parameters  
|           |                         |
|-----------|-------------------------|
| groupname | the groupname           |
| gid       | return location for GID |

<!-- -->

Returns  
TRUE if group name existed and we got the GID

Definition at line 145 of file dbus-userdb-util.c.

References \_dbus_user_database_get_system(), \_dbus_user_database_lock_system(), \_dbus_user_database_lookup_group(), \_dbus_user_database_unlock_system(), DBUS_GID_UNSET, FALSE, DBusGroupInfo::gid, NULL, and TRUE.

Referenced by \_dbus_parse_unix_group_from_config().

## ◆ \_dbus_get_is_errno_eintr()

|                                       |     |      |     |     |     |
|---------------------------------------|-----|------|-----|-----|-----|
| dbus_bool_t \_dbus_get_is_errno_eintr | (   | int  | *e* | )   |     |

See if errno is EINTR.

Returns  
TRUE if e == EINTR

Definition at line 690 of file dbus-sysdeps.c.

## ◆ \_dbus_get_is_errno_enomem()

|                                        |     |      |     |     |     |
|----------------------------------------|-----|------|-----|-----|-----|
| dbus_bool_t \_dbus_get_is_errno_enomem | (   | int  | *e* | )   |     |

See if errno is ENOMEM.

Returns  
TRUE if e == ENOMEM

Definition at line 680 of file dbus-sysdeps.c.

## ◆ \_dbus_get_is_errno_epipe()

|                                       |     |      |     |     |     |
|---------------------------------------|-----|------|-----|-----|-----|
| dbus_bool_t \_dbus_get_is_errno_epipe | (   | int  | *e* | )   |     |

See if errno is EPIPE.

Returns  
TRUE if errno == EPIPE

Definition at line 700 of file dbus-sysdeps.c.

## ◆ \_dbus_get_is_errno_etoomanyrefs()

|                                              |     |      |     |     |     |
|----------------------------------------------|-----|------|-----|-----|-----|
| dbus_bool_t \_dbus_get_is_errno_etoomanyrefs | (   | int  | *e* | )   |     |

See if errno is ETOOMANYREFS.

Returns  
TRUE if errno == ETOOMANYREFS

Definition at line 710 of file dbus-sysdeps.c.

References FALSE.

## ◆ \_dbus_get_local_machine_uuid_encoded()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_get_local_machine_uuid_encoded | ( | DBusString \*  | *uuid_str*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Gets the hex-encoded UUID of the machine this function is executed on.

This UUID is guaranteed to be the same for a given machine at least until it next reboots, though it also makes some effort to be the same forever, it may change if the machine is reconfigured or its hardware is modified.

Parameters  
|          |                                              |
|----------|----------------------------------------------|
| uuid_str | string to append hex-encoded machine uuid to |
| error    | location to store reason for failure         |

<!-- -->

Returns  
TRUE if successful

Definition at line 983 of file dbus-internals.c.

References \_dbus_current_generation, \_DBUS_LOCK, \_dbus_read_local_machine_uuid(), \_DBUS_UNLOCK, \_dbus_uuid_encode(), FALSE, and TRUE.

Referenced by \_dbus_get_autolaunch_address(), and dbus_try_get_local_machine_id().

## ◆ \_dbus_get_user_id()

|                                |     |                      |             |
|--------------------------------|-----|----------------------|-------------|
| dbus_bool_t \_dbus_get_user_id | (   | const DBusString \*  | *username*, |
|                                |     | dbus_uid_t \*        | *uid*       |
|                                | )   |                      |             |

Gets user ID given username.

Parameters  
|          |                         |
|----------|-------------------------|
| username | the username            |
| uid      | return location for UID |

<!-- -->

Returns  
TRUE if username existed and we got the UID

Definition at line 131 of file dbus-userdb-util.c.

References \_dbus_get_user_id_and_primary_group(), and NULL.

Referenced by \_dbus_parse_unix_user_from_config().

## ◆ \_dbus_get_user_id_and_primary_group()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_get_user_id_and_primary_group | ( | const DBusString \*  | *username*, |
|  |  | dbus_uid_t \*  | *uid_p*, |
|  |  | dbus_gid_t \*  | *gid_p*  |
|  | ) |  |  |

Gets user ID and primary group given username.

Parameters  
|          |                         |
|----------|-------------------------|
| username | the username            |
| uid_p    | return location for UID |
| gid_p    | return location for GID |

<!-- -->

Returns  
TRUE if username existed and we got the UID and GID

Definition at line 186 of file dbus-userdb-util.c.

References \_dbus_user_database_get_system(), \_dbus_user_database_get_username(), \_dbus_user_database_lock_system(), \_dbus_user_database_unlock_system(), FALSE, NULL, DBusUserInfo::primary_gid, TRUE, and DBusUserInfo::uid.

Referenced by \_dbus_change_to_daemon_user(), \_dbus_get_user_id(), and \_dbus_verify_daemon_user().

## ◆ \_dbus_group_info_fill()

|                                    |     |                      |              |
|------------------------------------|-----|----------------------|--------------|
| dbus_bool_t \_dbus_group_info_fill | (   | DBusGroupInfo \*     | *info*,      |
|                                    |     | const DBusString \*  | *groupname*, |
|                                    |     | DBusError \*         | *error*      |
|                                    | )   |                      |              |

Initializes the given DBusGroupInfo struct with information about the given group name.

Parameters  
|           |                       |
|-----------|-----------------------|
| info      | the group info struct |
| groupname | name of group         |
| error     | the error return      |

<!-- -->

Returns  
FALSE if error is set

Definition at line 884 of file dbus-sysdeps-util-unix.c.

References DBUS_GID_UNSET.

Referenced by \_dbus_user_database_lookup_group().

## ◆ \_dbus_group_info_fill_gid()

|                                        |     |                   |          |
|----------------------------------------|-----|-------------------|----------|
| dbus_bool_t \_dbus_group_info_fill_gid | (   | DBusGroupInfo \*  | *info*,  |
|                                        |     | dbus_gid_t        | *gid*,   |
|                                        |     | DBusError \*      | *error*  |
|                                        | )   |                   |          |

Initializes the given DBusGroupInfo struct with information about the given group ID.

Parameters  
|       |                       |
|-------|-----------------------|
| info  | the group info struct |
| gid   | group ID              |
| error | the error return      |

<!-- -->

Returns  
FALSE if error is set

Definition at line 903 of file dbus-sysdeps-util-unix.c.

References NULL.

Referenced by \_dbus_user_database_lookup_group().

## ◆ \_dbus_group_info_free()

|                             |     |                   |        |     |     |
|-----------------------------|-----|-------------------|--------|-----|-----|
| void \_dbus_group_info_free | (   | DBusGroupInfo \*  | *info* | )   |     |

Frees the members of info (but not info itself).

Parameters  
|      |                |
|------|----------------|
| info | the group info |

Definition at line 121 of file dbus-userdb.c.

References dbus_free(), and DBusGroupInfo::groupname.

Referenced by \_dbus_group_info_unref().

## ◆ \_dbus_group_info_unref()

|                              |     |                   |        |     |     |
|------------------------------|-----|-------------------|--------|-----|-----|
| void \_dbus_group_info_unref | (   | DBusGroupInfo \*  | *info* | )   |     |

Decrements the reference count.

If it reaches 0, frees the given DBusGroupInfo's members with \_dbus_group_info_free() and also calls dbus_free() on the block itself

Parameters  
|      |          |
|------|----------|
| info | the info |

Definition at line 87 of file dbus-userdb.c.

References \_dbus_assert, \_dbus_group_info_free(), dbus_free(), NULL, and DBusGroupInfo::refcount.

Referenced by \_dbus_user_database_lookup_group(), and \_dbus_user_database_new().

## ◆ \_dbus_groups_from_uid()

|                                    |     |                  |                |
|------------------------------------|-----|------------------|----------------|
| dbus_bool_t \_dbus_groups_from_uid | (   | dbus_uid_t       | *uid*,         |
|                                    |     | dbus_gid_t \*\*  | *group_ids*,   |
|                                    |     | int \*           | *n_group_ids*, |
|                                    |     | DBusError \*     | *error*        |
|                                    | )   |                  |                |

Gets all groups corresponding to the given UID.

Returns FALSE if no memory, or user isn't known, but always initializes group_ids to a NULL array.

Parameters  
|             |                                              |
|-------------|----------------------------------------------|
| uid         | the UID                                      |
| group_ids   | return location for array of group IDs       |
| n_group_ids | return location for length of returned array |
| error       | error to fill in on failure                  |

<!-- -->

Returns  
TRUE if the UID existed and we got some credentials

Definition at line 349 of file dbus-userdb-util.c.

References \_dbus_assert, \_dbus_user_database_get_system(), \_dbus_user_database_get_uid(), \_dbus_user_database_lock_system(), \_dbus_user_database_unlock_system(), dbus_new, FALSE, DBusUserInfo::group_ids, DBusUserInfo::n_group_ids, NULL, TRUE, and DBusUserInfo::uid.

Referenced by \_dbus_unix_groups_from_uid().

## ◆ \_dbus_homedir_from_current_process()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_homedir_from_current_process | ( | const DBusString \*\*  | *homedir* | ) |  |

Gets homedir of user owning current process.

The returned string is valid until dbus_shutdown() is called.

Parameters  
|         |                                   |
|---------|-----------------------------------|
| homedir | place to store pointer to homedir |

<!-- -->

Returns  
FALSE if no memory

Definition at line 442 of file dbus-userdb.c.

References \_dbus_user_database_lock_system(), \_dbus_user_database_unlock_system(), FALSE, and TRUE.

Referenced by \_dbus_get_standard_session_servicedirs().

## ◆ \_dbus_homedir_from_uid()

|                                     |     |                |            |
|-------------------------------------|-----|----------------|------------|
| dbus_bool_t \_dbus_homedir_from_uid | (   | dbus_uid_t     | *uid*,     |
|                                     |     | DBusString \*  | *homedir*  |
|                                     | )   |                |            |

Gets the home directory for the given user.

Parameters  
|         |                                    |
|---------|------------------------------------|
| uid     | the uid                            |
| homedir | string to append home directory to |

<!-- -->

Returns  
TRUE if user existed and we appended their homedir

Definition at line 466 of file dbus-userdb.c.

References \_dbus_getenv(), \_dbus_geteuid(), \_dbus_getuid(), \_dbus_string_append(), \_dbus_user_database_get_system(), \_dbus_user_database_get_uid(), \_dbus_user_database_lock_system(), \_dbus_user_database_unlock_system(), FALSE, DBusUserInfo::homedir, NULL, and TRUE.

Referenced by \_dbus_append_keyring_directory_for_credentials().

## ◆ \_dbus_inet_sockaddr_to_string()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_inet_sockaddr_to_string | ( | const void \*  | *sockaddr_pointer*, |
|  |  | size_t  | *len*, |
|  |  | char \*  | *string*, |
|  |  | size_t  | *string_len*, |
|  |  | const char \*\*  | *family_name*, |
|  |  | dbus_uint16_t \*  | *port*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Definition at line 762 of file dbus-sysdeps.c.

## ◆ \_dbus_is_a_number()

|                                |     |                      |        |
|--------------------------------|-----|----------------------|--------|
| dbus_bool_t \_dbus_is_a_number | (   | const DBusString \*  | *str*, |
|                                |     | unsigned long \*     | *num*  |
|                                | )   |                      |        |

Checks if a given string is actually a number and converts it if it is.

Parameters  
|     |                                                     |
|-----|-----------------------------------------------------|
| str | the string to check                                 |
| num | the memory location of the unsigned long to fill in |

<!-- -->

Returns  
TRUE if str is a number and num is filled in

Definition at line 135 of file dbus-userdb.c.

References \_dbus_string_get_length(), \_dbus_string_parse_uint(), FALSE, and TRUE.

Referenced by \_dbus_credentials_add_from_user(), \_dbus_user_database_lookup(), and \_dbus_user_database_lookup_group().

## ◆ \_dbus_is_console_user()

|                                    |     |               |          |
|------------------------------------|-----|---------------|----------|
| dbus_bool_t \_dbus_is_console_user | (   | dbus_uid_t    | *uid*,   |
|                                    |     | DBusError \*  | *error*  |
|                                    | )   |               |          |

Checks to see if the UID sent in is the console user.

Parameters  
|       |                            |
|-------|----------------------------|
| uid   | UID of person to check     |
| error | return location for errors |

<!-- -->

Returns  
TRUE if the UID is the same as the console user and there are no errors

Definition at line 67 of file dbus-userdb-util.c.

References \_dbus_error_from_errno(), \_dbus_stat(), \_dbus_string_append(), \_dbus_string_free(), \_dbus_string_init(), dbus_set_error(), DBUS_UID_FORMAT, FALSE, NULL, TRUE, and DBusStat::uid.

Referenced by \_dbus_unix_user_is_at_console().

## ◆ \_dbus_log()

|                 |     |                        |             |
|-----------------|-----|------------------------|-------------|
| void \_dbus_log | (   | DBusSystemLogSeverity  | *severity*, |
|                 |     | const char \*          | *msg*,      |
|                 |     |                        | *...*       |
|                 | )   |                        |             |

Log a message to the system log file (e.g.

syslog on Unix) and/or stderr.

Parameters  
|          |                              |
|----------|------------------------------|
| severity | a severity value             |
| msg      | a printf-style format string |

Definition at line 736 of file dbus-sysdeps.c.

References \_dbus_logv().

## ◆ \_dbus_memdup()

|                       |     |                |            |
|-----------------------|-----|----------------|------------|
| void \* \_dbus_memdup | (   | const void \*  | *mem*,     |
|                       |     | size_t         | *n_bytes*  |
|                       | )   |                |            |

Duplicates a block of memory.

Returns NULL on failure.

Parameters  
|         |                         |
|---------|-------------------------|
| mem     | memory to copy          |
| n_bytes | number of bytes to copy |

<!-- -->

Returns  
the copy

Definition at line 649 of file dbus-internals.c.

References dbus_malloc(), and NULL.

Referenced by \_dbus_credentials_add_adt_audit_data(), and \_dbus_decompose_path().

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

Definition at line 935 of file dbus-sysdeps-util-unix.c.

References \_dbus_get_group_id().

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

Definition at line 919 of file dbus-sysdeps-util-unix.c.

References \_dbus_get_user_id().

## ◆ \_dbus_path_is_absolute()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_path_is_absolute | ( | const DBusString \*  | *filename* | ) |  |

Checks whether the filename is an absolute path.

Parameters  
|          |              |
|----------|--------------|
| filename | the filename |

<!-- -->

Returns  
TRUE if an absolute path

Definition at line 576 of file dbus-sysdeps-util-unix.c.

References \_dbus_string_get_byte(), \_dbus_string_get_length(), and FALSE.

## ◆ \_dbus_read_uuid_file()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_read_uuid_file | ( | const DBusString \*  | *filename*, |
|  |  | DBusGUID \*  | *uuid*, |
|  |  | dbus_bool_t  | *create_if_not_found*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Reads (and optionally writes) a uuid to a file.

Initializes the uuid unless an error is returned.

Parameters  
|  |  |
|----|----|
| filename | the name of the file |
| uuid | uuid to be initialized with the loaded uuid |
| create_if_not_found | TRUE to create a new uuid and save it if the file doesn't exist |
| error | the error return |

<!-- -->

Returns  
FALSE if the error is set

Definition at line 931 of file dbus-internals.c.

References \_dbus_generate_uuid(), \_dbus_write_uuid_file(), dbus_error_free(), dbus_error_has_name(), DBUS_ERROR_INIT, DBUS_ERROR_INVALID_FILE_CONTENT, dbus_move_error(), FALSE, and TRUE.

Referenced by \_dbus_get_uuid(), and \_dbus_read_local_machine_uuid().

## ◆ \_dbus_real_assert()

|                         |     |                |                   |
|-------------------------|-----|----------------|-------------------|
| void \_dbus_real_assert | (   | dbus_bool_t    | *condition*,      |
|                         |     | const char \*  | *condition_text*, |
|                         |     | const char \*  | *file*,           |
|                         |     | int            | *line*,           |
|                         |     | const char \*  | *func*            |
|                         | )   |                |                   |

Internals of \_dbus_assert(); it's a function rather than a macro with the inline code so that the assertion failure blocks don't show up in test suite coverage, and to shrink code size.

Parameters  
|                |                              |
|----------------|------------------------------|
| condition      | TRUE if assertion succeeded  |
| condition_text | condition as a string        |
| file           | file the assertion is in     |
| line           | line the assertion is in     |
| func           | function the assertion is in |

Definition at line 1042 of file dbus-internals.c.

References \_dbus_abort(), and \_dbus_warn().

## ◆ \_dbus_real_assert_not_reached()

|                                     |     |                |                |
|-------------------------------------|-----|----------------|----------------|
| void \_dbus_real_assert_not_reached | (   | const char \*  | *explanation*, |
|                                     |     | const char \*  | *file*,        |
|                                     |     | int            | *line*         |
|                                     | )   |                |                |

Internals of \_dbus_assert_not_reached(); it's a function rather than a macro with the inline code so that the assertion failure blocks don't show up in test suite coverage, and to shrink code size.

Parameters  
|             |                                           |
|-------------|-------------------------------------------|
| explanation | what was reached that shouldn't have been |
| file        | file the assertion is in                  |
| line        | line the assertion is in                  |

Definition at line 1067 of file dbus-internals.c.

References \_dbus_abort(), and \_dbus_warn().

## ◆ \_dbus_rlimit_free()

|                         |     |                |       |     |     |
|-------------------------|-----|----------------|-------|-----|-----|
| void \_dbus_rlimit_free | (   | DBusRLimit \*  | *lim* | )   |     |

Definition at line 534 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_rlimit_raise_fd_limit()

|                                          |     |               |         |     |     |
|------------------------------------------|-----|---------------|---------|-----|-----|
| dbus_bool_t \_dbus_rlimit_raise_fd_limit | (   | DBusError \*  | *error* | )   |     |

Definition at line 517 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_rlimit_restore_fd_limit()

|                                            |     |                |          |
|--------------------------------------------|-----|----------------|----------|
| dbus_bool_t \_dbus_rlimit_restore_fd_limit | (   | DBusRLimit \*  | *saved*, |
|                                            |     | DBusError \*   | *error*  |
|                                            | )   |                |          |

Definition at line 524 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_rlimit_save_fd_limit()

|                                           |     |               |         |     |     |
|-------------------------------------------|-----|---------------|---------|-----|-----|
| DBusRLimit \* \_dbus_rlimit_save_fd_limit | (   | DBusError \*  | *error* | )   |     |

Definition at line 510 of file dbus-sysdeps-util-unix.c.

## ◆ \_dbus_set_errno_to_zero()

|                               |     |       |     |     |     |
|-------------------------------|-----|-------|-----|-----|-----|
| void \_dbus_set_errno_to_zero | (   | void  |     | )   |     |

Assign 0 to the global errno variable.

Definition at line 666 of file dbus-sysdeps.c.

Referenced by \_dbus_string_parse_int(), \_dbus_string_parse_int64(), and \_dbus_string_parse_uint().

## ◆ \_dbus_set_error_with_inet_sockaddr()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_set_error_with_inet_sockaddr | ( | DBusError \*  | *error*, |
|  |  | const void \*  | *sockaddr_pointer*, |
|  |  | size_t  | *len*, |
|  |  | const char \*  | *description*, |
|  |  | int  | *saved_errno*  |
|  | ) |  |  |

Definition at line 849 of file dbus-sysdeps.c.

## ◆ \_dbus_set_signal_handler()

|                                |     |                    |            |
|--------------------------------|-----|--------------------|------------|
| void \_dbus_set_signal_handler | (   | int                | *sig*,     |
|                                |     | DBusSignalHandler  | *handler*  |
|                                | )   |                    |            |

Installs a UNIX signal handler.

Parameters  
|         |                      |
|---------|----------------------|
| sig     | the signal to handle |
| handler | the handler          |

Definition at line 545 of file dbus-sysdeps-util-unix.c.

References NULL.

## ◆ \_dbus_spawn_async_with_babysitter()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_spawn_async_with_babysitter | ( | DBusBabysitter \*\*  | *sitter_p*, |
|  |  | const char \*  | *log_name*, |
|  |  | char \*const \*  | *argv*, |
|  |  | char \*const \*  | *env*, |
|  |  | DBusSpawnFlags flags  | *flags*, |
|  |  | DBusSpawnChildSetupFunc child_setup  | *child_setup*, |
|  |  | void \*  | *user_data*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Spawns a new process.

On Unix platforms, the child_setup function is passed the given user_data and is run in the child after fork() but before calling exec(). This can be used to change uid, resource limits and so on. On Windows, this functionality does not fit the multi-processing model (Windows does the equivalent of fork() and exec() in a single API call), and the child_setup function and its user_data are ignored.

Also creates a "babysitter" which tracks the status of the child process, advising the parent if the child exits. If the spawn fails, no babysitter is created. If sitter_p is NULL, no babysitter is kept.

Parameters  
|  |  |
|----|----|
| sitter_p | return location for babysitter or NULL |
| log_name | the name under which to log messages about this process being spawned |
| argv | the executable and arguments |
| env | the environment, or NULL to copy the parent's |
| child_setup | function to call in child pre-exec() |
| user_data | user data for setup function |
| error | error object to be filled in if function fails |

<!-- -->

Returns  
TRUE on success, FALSE if error is filled in

Definition at line 1279 of file dbus-spawn-unix.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_babysitter_unref(), \_dbus_dup(), \_dbus_error_from_errno(), \_dbus_fd_set_close_on_exec(), \_dbus_reset_oom_score_adj(), \_dbus_socketpair(), \_dbus_strdup(), \_dbus_watch_invalidate(), \_dbus_watch_list_add_watch(), \_dbus_watch_new(), \_dbus_watch_unref(), DBUS_ERROR_NO_MEMORY, DBUS_ERROR_SPAWN_FORK_FAILED, dbus_set_error(), DBUS_WATCH_READABLE, DBusBabysitter::error_pipe_from_child, DBusBabysitter::error_watch, FALSE, DBusBabysitter::log_name, NULL, READ_END, DBusBabysitter::sitter_pid, DBusBabysitter::sitter_watch, DBusBabysitter::socket_to_babysitter, TRUE, DBusBabysitter::watches, and WRITE_END.

## ◆ \_dbus_stat()

|                         |     |                      |             |
|-------------------------|-----|----------------------|-------------|
| dbus_bool_t \_dbus_stat | (   | const DBusString \*  | *filename*, |
|                         |     | DBusStat \*          | *statbuf*,  |
|                         |     | DBusError \*         | *error*     |
|                         | )   |                      |             |

stat() wrapper.

Parameters  
|          |                           |
|----------|---------------------------|
| filename | the filename to stat      |
| statbuf  | the stat info to fill in  |
| error    | return location for error |

<!-- -->

Returns  
FALSE if error was set

Definition at line 593 of file dbus-sysdeps-util-unix.c.

References \_dbus_error_from_errno(), \_dbus_string_get_const_data(), DBusStat::atime, DBusStat::ctime, dbus_set_error(), FALSE, DBusStat::gid, DBusStat::mode, DBusStat::mtime, DBusStat::nlink, DBusStat::size, TRUE, and DBusStat::uid.

Referenced by \_dbus_is_console_user().

## ◆ \_dbus_strdup()

|                       |     |                |       |     |     |
|-----------------------|-----|----------------|-------|-----|-----|
| char \* \_dbus_strdup | (   | const char \*  | *str* | )   |     |

Duplicates a string.

Result must be freed with dbus_free(). Returns NULL if memory allocation fails. If the string to be duplicated is NULL, returns NULL.

Parameters  
|     |                      |
|-----|----------------------|
| str | string to duplicate. |

<!-- -->

Returns  
newly-allocated copy.

Definition at line 621 of file dbus-internals.c.

References dbus_malloc(), and NULL.

Referenced by \_dbus_credentials_add_linux_security_label(), \_dbus_credentials_add_windows_sid(), \_dbus_dup_string_array(), \_dbus_get_environment(), \_dbus_message_iter_get_args_valist(), \_dbus_server_new_for_domain_socket(), \_dbus_spawn_async_with_babysitter(), \_dbus_transport_get_windows_user(), \_dbus_transport_open(), dbus_bus_get_id(), dbus_bus_register(), dbus_bus_set_unique_name(), dbus_connection_get_server_id(), and dbus_server_get_address().

## ◆ \_dbus_strerror_from_errno()

|                                          |     |       |     |     |     |
|------------------------------------------|-----|-------|-----|-----|-----|
| const char \* \_dbus_strerror_from_errno | (   | void  |     | )   |     |

Get error message from errno.

Returns  
\_dbus_strerror(errno)

Definition at line 724 of file dbus-sysdeps.c.

Referenced by \_dbus_close_socket(), \_dbus_create_directory(), \_dbus_delete_file(), \_dbus_ensure_directory(), \_dbus_send_credentials_socket(), \_dbus_set_socket_nonblocking(), \_dbus_socketpair(), \_dbus_write_socket(), and \_dbus_write_socket_two().

## ◆ \_dbus_string_array_contains()

|                                          |     |                  |          |
|------------------------------------------|-----|------------------|----------|
| dbus_bool_t \_dbus_string_array_contains | (   | const char \*\*  | *array*, |
|                                          |     | const char \*    | *str*    |
|                                          | )   |                  |          |

Checks whether a string array contains the given string.

Parameters  
|       |                    |
|-------|--------------------|
| array | array to search.   |
| str   | string to look for |

<!-- -->

Returns  
TRUE if array contains string

Definition at line 712 of file dbus-internals.c.

References FALSE, NULL, and TRUE.

## ◆ \_dbus_string_array_length()

|                                   |     |                  |         |     |     |
|-----------------------------------|-----|------------------|---------|-----|-----|
| size_t \_dbus_string_array_length | (   | const char \*\*  | *array* | )   |     |

Returns the size of a string array.

Parameters  
|       |                  |
|-------|------------------|
| array | array to search. |

<!-- -->

Returns  
size of array

Definition at line 735 of file dbus-internals.c.

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

Definition at line 953 of file dbus-sysdeps-util-unix.c.

References \_dbus_groups_from_uid().

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

Definition at line 971 of file dbus-sysdeps-util-unix.c.

References \_dbus_is_console_user().

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

Definition at line 986 of file dbus-sysdeps-util-unix.c.

References \_dbus_geteuid().

## ◆ \_dbus_user_database_flush()

|                                 |     |                      |      |     |     |
|---------------------------------|-----|----------------------|------|-----|-----|
| void \_dbus_user_database_flush | (   | DBusUserDatabase \*  | *db* | )   |     |

Flush all information out of the user database.

Definition at line 641 of file dbus-userdb.c.

References \_dbus_hash_table_remove_all().

Referenced by \_dbus_user_database_flush_system().

## ◆ \_dbus_user_database_flush_system()

|                                        |     |       |     |     |     |
|----------------------------------------|-----|-------|-----|-----|-----|
| void \_dbus_user_database_flush_system | (   | void  |     | )   |     |

Flushes the system global user database;.

Definition at line 396 of file dbus-userdb.c.

References \_dbus_user_database_flush(), \_dbus_user_database_lock_system(), \_dbus_user_database_unlock_system(), and NULL.

Referenced by \_dbus_flush_caches().

## ◆ \_dbus_user_database_get_system()

|                                                     |     |       |     |     |     |
|-----------------------------------------------------|-----|-------|-----|-----|-----|
| DBusUserDatabase \* \_dbus_user_database_get_system | (   | void  |     | )   |     |

Gets the system global user database; must be called with lock held (\_dbus_user_database_lock_system()).

Returns  
the database or NULL if no memory

Definition at line 383 of file dbus-userdb.c.

References \_dbus_assert.

Referenced by \_dbus_credentials_add_from_user(), \_dbus_get_group_id(), \_dbus_get_user_id_and_primary_group(), \_dbus_groups_from_uid(), and \_dbus_homedir_from_uid().

## ◆ \_dbus_user_database_get_uid()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_user_database_get_uid | ( | DBusUserDatabase \*  | *db*, |
|  |  | dbus_uid_t  | *uid*, |
|  |  | const DBusUserInfo \*\*  | *info*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Gets the user information for the given UID, returned user info should not be freed.

Parameters  
|       |                                            |
|-------|--------------------------------------------|
| db    | user database                              |
| uid   | the user ID                                |
| info  | return location for const ref to user info |
| error | error location                             |

<!-- -->

Returns  
FALSE if error is set

Definition at line 705 of file dbus-userdb.c.

References \_dbus_user_database_lookup(), and NULL.

Referenced by \_dbus_groups_from_uid(), and \_dbus_homedir_from_uid().

## ◆ \_dbus_user_database_get_username()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_user_database_get_username | ( | DBusUserDatabase \*  | *db*, |
|  |  | const DBusString \*  | *username*, |
|  |  | const DBusUserInfo \*\*  | *info*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Gets the user information for the given username.

Parameters  
|          |                                            |
|----------|--------------------------------------------|
| db       | user database                              |
| username | the user name                              |
| info     | return location for const ref to user info |
| error    | error location                             |

<!-- -->

Returns  
FALSE if error is set

Definition at line 724 of file dbus-userdb.c.

References \_dbus_user_database_lookup(), DBUS_UID_UNSET, and NULL.

Referenced by \_dbus_credentials_add_from_user(), and \_dbus_get_user_id_and_primary_group().

## ◆ \_dbus_user_database_lock_system()

|                                              |     |       |     |     |     |
|----------------------------------------------|-----|-------|-----|-----|-----|
| dbus_bool_t \_dbus_user_database_lock_system | (   | void  |     | )   |     |

Locks global system user database.

Definition at line 353 of file dbus-userdb.c.

References \_DBUS_LOCK, FALSE, and TRUE.

Referenced by \_dbus_credentials_add_from_user(), \_dbus_get_group_id(), \_dbus_get_user_id_and_primary_group(), \_dbus_groups_from_uid(), \_dbus_homedir_from_current_process(), \_dbus_homedir_from_uid(), \_dbus_user_database_flush_system(), and \_dbus_username_from_current_process().

## ◆ \_dbus_user_database_lookup()

|  |  |  |  |
|----|----|----|----|
| const DBusUserInfo \* \_dbus_user_database_lookup | ( | DBusUserDatabase \*  | *db*, |
|  |  | dbus_uid_t  | *uid*, |
|  |  | const DBusString \*  | *username*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Looks up a uid or username in the user database.

Only one of name or UID can be provided. There are wrapper functions for this that are better to use, this one does no locking or anything on the database and otherwise sort of sucks.

Parameters  
|          |                               |
|----------|-------------------------------|
| db       | the database                  |
| uid      | the user ID or DBUS_UID_UNSET |
| username | username or NULL              |
| error    | error to fill in              |

<!-- -->

Returns  
the entry in the database (borrowed, do not free)

Definition at line 160 of file dbus-userdb.c.

References \_dbus_assert, \_dbus_hash_table_insert_string(), \_dbus_hash_table_insert_uintptr(), \_dbus_hash_table_lookup_string(), \_dbus_hash_table_lookup_uintptr(), \_dbus_hash_table_remove_uintptr(), \_dbus_is_a_number(), \_dbus_string_get_const_data(), \_dbus_user_info_fill(), \_dbus_user_info_fill_uid(), \_dbus_user_info_unref(), DBUS_ERROR_NO_MEMORY, dbus_new0, dbus_set_error(), DBUS_UID_FORMAT, DBUS_UID_UNSET, NULL, DBusUserInfo::refcount, DBusUserInfo::uid, and DBusUserInfo::username.

Referenced by \_dbus_user_database_get_uid(), and \_dbus_user_database_get_username().

## ◆ \_dbus_user_database_lookup_group()

|  |  |  |  |
|----|----|----|----|
| const DBusGroupInfo \* \_dbus_user_database_lookup_group | ( | DBusUserDatabase \*  | *db*, |
|  |  | dbus_gid_t  | *gid*, |
|  |  | const DBusString \*  | *groupname*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Looks up a gid or group name in the user database.

Only one of name or GID can be provided. There are wrapper functions for this that are better to use, this one does no locking or anything on the database and otherwise sort of sucks.

Parameters  
|           |                                |
|-----------|--------------------------------|
| db        | the database                   |
| gid       | the group ID or DBUS_GID_UNSET |
| groupname | group name or NULL             |
| error     | error to fill in               |

<!-- -->

Returns  
the entry in the database (borrowed, do not free)

Definition at line 233 of file dbus-userdb-util.c.

References \_dbus_group_info_fill(), \_dbus_group_info_fill_gid(), \_dbus_group_info_unref(), \_dbus_hash_table_insert_string(), \_dbus_hash_table_insert_uintptr(), \_dbus_hash_table_lookup_string(), \_dbus_hash_table_lookup_uintptr(), \_dbus_hash_table_remove_uintptr(), \_dbus_is_a_number(), \_dbus_string_get_const_data(), DBUS_ERROR_NO_MEMORY, DBUS_GID_FORMAT, DBUS_GID_UNSET, dbus_new0, dbus_set_error(), DBUS_UID_UNSET, DBusGroupInfo::gid, DBusGroupInfo::groupname, NULL, and DBusGroupInfo::refcount.

Referenced by \_dbus_get_group_id().

## ◆ \_dbus_user_database_new()

|                                              |     |       |     |     |     |
|----------------------------------------------|-----|-------|-----|-----|-----|
| DBusUserDatabase \* \_dbus_user_database_new | (   | void  |     | )   |     |

Creates a new user database object used to look up and cache user information.

Returns  
new database, or NULL on out of memory

Definition at line 598 of file dbus-userdb.c.

References \_dbus_group_info_unref(), \_dbus_hash_table_new(), \_dbus_user_database_unref(), \_dbus_user_info_unref(), DBUS_HASH_STRING, DBUS_HASH_UINTPTR, dbus_new0, and NULL.

## ◆ \_dbus_user_database_unlock_system()

|                                         |     |       |     |     |     |
|-----------------------------------------|-----|-------|-----|-----|-----|
| void \_dbus_user_database_unlock_system | (   | void  |     | )   |     |

Unlocks global system user database.

Definition at line 370 of file dbus-userdb.c.

References \_DBUS_UNLOCK, and FALSE.

Referenced by \_dbus_credentials_add_from_user(), \_dbus_get_group_id(), \_dbus_get_user_id_and_primary_group(), \_dbus_groups_from_uid(), \_dbus_homedir_from_current_process(), \_dbus_homedir_from_uid(), \_dbus_user_database_flush_system(), and \_dbus_username_from_current_process().

## ◆ \_dbus_user_database_unref()

|                                 |     |                      |      |     |     |
|---------------------------------|-----|----------------------|------|-----|-----|
| void \_dbus_user_database_unref | (   | DBusUserDatabase \*  | *db* | )   |     |

Decrements refcount of user database.

Parameters  
|     |              |
|-----|--------------|
| db  | the database |

Definition at line 671 of file dbus-userdb.c.

References \_dbus_assert, \_dbus_hash_table_unref(), and dbus_free().

Referenced by \_dbus_user_database_new().

## ◆ \_dbus_user_info_free()

|                            |     |                  |        |     |     |
|----------------------------|-----|------------------|--------|-----|-----|
| void \_dbus_user_info_free | (   | DBusUserInfo \*  | *info* | )   |     |

Frees the members of info (but not info itself)

Parameters  
|      |                      |
|------|----------------------|
| info | the user info struct |

Definition at line 108 of file dbus-userdb.c.

References dbus_free(), DBusUserInfo::group_ids, DBusUserInfo::homedir, and DBusUserInfo::username.

Referenced by \_dbus_user_info_unref().

## ◆ \_dbus_user_info_unref()

|                             |     |                  |        |     |     |
|-----------------------------|-----|------------------|--------|-----|-----|
| void \_dbus_user_info_unref | (   | DBusUserInfo \*  | *info* | )   |     |

Decrements the reference count.

If it reaches 0, frees the given DBusUserInfo's members with \_dbus_user_info_free() and also calls dbus_free() on the block itself

Parameters  
|      |          |
|------|----------|
| info | the info |

Definition at line 64 of file dbus-userdb.c.

References \_dbus_assert, \_dbus_user_info_free(), dbus_free(), NULL, and DBusUserInfo::refcount.

Referenced by \_dbus_user_database_lookup(), and \_dbus_user_database_new().

## ◆ \_dbus_username_from_current_process()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_username_from_current_process | ( | const DBusString \*\*  | *username* | ) |  |

Gets username of user owning current process.

The returned string is valid until dbus_shutdown() is called.

Parameters  
|          |                                    |
|----------|------------------------------------|
| username | place to store pointer to username |

<!-- -->

Returns  
FALSE if no memory

Definition at line 418 of file dbus-userdb.c.

References \_dbus_user_database_lock_system(), \_dbus_user_database_unlock_system(), FALSE, and TRUE.

## ◆ \_dbus_uuid_encode()

|                                |     |                    |            |
|--------------------------------|-----|--------------------|------------|
| dbus_bool_t \_dbus_uuid_encode | (   | const DBusGUID \*  | *uuid*,    |
|                                |     | DBusString \*      | *encoded*  |
|                                | )   |                    |            |

Hex-encode a UUID.

Parameters  
|         |                              |
|---------|------------------------------|
| uuid    | the uuid                     |
| encoded | string to append hex uuid to |

<!-- -->

Returns  
FALSE if no memory

Definition at line 788 of file dbus-internals.c.

References \_dbus_string_get_length(), \_dbus_string_hex_encode(), \_dbus_string_init_const_len(), and DBusGUID::as_bytes.

Referenced by \_dbus_get_local_machine_uuid_encoded(), \_dbus_server_init_base(), and \_dbus_write_uuid_file().

## ◆ \_dbus_verify_daemon_user()

|                                       |     |                |        |     |     |
|---------------------------------------|-----|----------------|--------|-----|-----|
| dbus_bool_t \_dbus_verify_daemon_user | (   | const char \*  | *user* | )   |     |

Verify that after the fork we can successfully change to this user.

Parameters  
|      |                                                |
|------|------------------------------------------------|
| user | the username given in the daemon configuration |

<!-- -->

Returns  
TRUE if username is valid

Definition at line 313 of file dbus-sysdeps-util-unix.c.

References \_dbus_get_user_id_and_primary_group(), \_dbus_string_init_const(), and NULL.

## ◆ \_dbus_warn()

|                  |     |                |           |
|------------------|-----|----------------|-----------|
| void \_dbus_warn | (   | const char \*  | *format*, |
|                  |     |                | *...*     |
|                  | )   |                |           |

Prints a warning message to stderr.

Can optionally be made to exit fatally by setting DBUS_FATAL_WARNINGS, but this is rarely used. This function should be considered pretty much equivalent to fprintf(stderr). \_dbus_warn_check_failed() on the other hand is suitable for use when a programming mistake has been made.

Parameters  
|        |                             |
|--------|-----------------------------|
| format | printf-style format string. |

Definition at line 278 of file dbus-internals.c.

References \_dbus_abort(), and \_dbus_logv().

Referenced by \_dbus_append_keyring_directory_for_credentials(), \_dbus_babysitter_unref(), \_dbus_become_daemon(), \_dbus_change_to_daemon_user(), \_dbus_get_tmpdir(), \_dbus_listen_tcp_socket(), \_dbus_listen_unix_socket(), \_dbus_marshal_skip_basic(), \_dbus_message_iter_get_args_valist(), \_dbus_object_tree_unregister_and_unlock(), \_dbus_real_assert(), \_dbus_real_assert_not_reached(), \_dbus_server_new_for_launchd(), \_dbus_socketpair(), \_dbus_watch_unref(), dbus_connection_register_fallback(), dbus_connection_register_object_path(), dbus_malloc(), dbus_malloc0(), dbus_message_append_args_valist(), and dbus_realloc().

## ◆ \_dbus_warn_check_failed()

|                               |     |                |           |
|-------------------------------|-----|----------------|-----------|
| void \_dbus_warn_check_failed | (   | const char \*  | *format*, |
|                               |     |                | *...*     |
|                               | )   |                |           |

Prints a "critical" warning to stderr when an assertion fails; differs from \_dbus_warn primarily in that it defaults to fatal.

This should be used only when a programming error has been detected. (NOT for unavoidable errors that an app might handle - those should be returned as DBusError.) Calling this means "there is a bug"

Definition at line 310 of file dbus-internals.c.

References \_dbus_abort(), and \_dbus_logv().

Referenced by \_dbus_marshal_read_basic(), \_dbus_transport_handle_watch(), \_dbus_type_reader_recurse(), dbus_connection_close(), dbus_connection_remove_filter(), dbus_connection_unref(), dbus_get_local_machine_id(), dbus_server_set_timeout_functions(), dbus_server_set_watch_functions(), and dbus_watch_handle().

## ◆ \_dbus_warn_return_if_fail()

|                                 |     |                |              |
|---------------------------------|-----|----------------|--------------|
| void \_dbus_warn_return_if_fail | (   | const char \*  | *function*,  |
|                                 |     | const char \*  | *assertion*, |
|                                 |     | const char \*  | *file*,      |
|                                 |     | int            | *line*       |
|                                 | )   |                |              |

Definition at line 1016 of file dbus-internals.c.

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

Definition at line 999 of file dbus-sysdeps-util-unix.c.

References FALSE.

## ◆ \_dbus_write_pid_to_file_and_pipe()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_write_pid_to_file_and_pipe | ( | const DBusString \*  | *pidfile*, |
|  |  | DBusPipe \*  | *print_pid_pipe*, |
|  |  | dbus_pid_t  | *pid_to_write*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Writes the given pid_to_write to a pidfile (if non-NULL) and/or to a pipe (if non-NULL).

Does nothing if pidfile and print_pid_pipe are both NULL.

Parameters  
|                |                              |
|----------------|------------------------------|
| pidfile        | the file to write to or NULL |
| print_pid_pipe | the pipe to write to or NULL |
| pid_to_write   | the pid to write out         |
| error          | error on failure             |

<!-- -->

Returns  
FALSE if error is set

Definition at line 240 of file dbus-sysdeps-util-unix.c.

References \_dbus_string_append_printf(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_get_length(), \_dbus_string_init(), DBUS_ERROR_FAILED, dbus_error_is_set(), DBUS_PID_FORMAT, dbus_set_error(), FALSE, NULL, and TRUE.

Referenced by \_dbus_become_daemon().

## ◆ \_dbus_write_uuid_file()

|                                    |     |                      |             |
|------------------------------------|-----|----------------------|-------------|
| dbus_bool_t \_dbus_write_uuid_file | (   | const DBusString \*  | *filename*, |
|                                    |     | const DBusGUID \*    | *uuid*,     |
|                                    |     | DBusError \*         | *error*     |
|                                    | )   |                      |             |

Write the give UUID to a file.

Parameters  
|          |                        |
|----------|------------------------|
| filename | the file to write      |
| uuid     | the UUID to save       |
| error    | used to raise an error |

<!-- -->

Returns  
FALSE on error

Definition at line 882 of file dbus-internals.c.

References \_dbus_string_append_byte(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_string_save_to_file(), \_dbus_uuid_encode(), FALSE, and TRUE.

Referenced by \_dbus_read_local_machine_uuid(), and \_dbus_read_uuid_file().

## Variable Documentation

## ◆ \_dbus_no_memory_message

|                                                             |
|-------------------------------------------------------------|
| const char\* \_dbus_no_memory_message = "Not enough memory" |

Fixed "out of memory" error message, just to avoid making up a different string every time and wasting space.

Definition at line 216 of file dbus-internals.c.
