DBusMessage implementation details

D-Bus secret internal implementation details

DBusMessage private implementation details. More...

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
<td class="memItemRight" data-valign="bottom">DBusMessageLoader</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Implementation details of DBusMessageLoader. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusMessage</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusMessage. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusMessageRealIter</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusMessageIter. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusMessageIter_1_10_0</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Layout of a DBusMessageIter on the stack in dbus 1.10.0. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusVariant</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">An opaque data structure containing the serialized form of any single D-Bus message item, whose signature is a single complete type. More...<br />
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
<tr id="r_ga660989658f3be5e403da430f63afd0b7" class="memitem:ga660989658f3be5e403da430f63afd0b7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">CHANGED_STAMP_BITS   21</td>
</tr>
<tr class="memdesc:ga660989658f3be5e403da430f63afd0b7">
<td class="mdescLeft"> </td>
<td class="mdescRight">How many bits are in the changed_stamp used to validate iterators.<br />
</td>
</tr>
<tr class="separator:ga660989658f3be5e403da430f63afd0b7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaea37a18258a4c9fd96f965e35cb13bef" class="memitem:gaea37a18258a4c9fd96f965e35cb13bef">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">_dbus_enable_message_cache()   (TRUE)</td>
</tr>
<tr class="separator:gaea37a18258a4c9fd96f965e35cb13bef">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga81a502b629157877b5123942ff739e05" class="memitem:ga81a502b629157877b5123942ff739e05">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">CHECK_DBUS_1_10_BINARY_COMPATIBILITY   1</td>
</tr>
<tr class="separator:ga81a502b629157877b5123942ff739e05">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1dfae386ef0d4d808584abeafc44e8ca" class="memitem:ga1dfae386ef0d4d808584abeafc44e8ca">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">ensure_byte_order(message)   _dbus_message_byteswap (message)</td>
</tr>
<tr class="memdesc:ga1dfae386ef0d4d808584abeafc44e8ca">
<td class="mdescLeft"> </td>
<td class="mdescRight">byte-swap the message if it doesn't match our byte order.<br />
</td>
</tr>
<tr class="separator:ga1dfae386ef0d4d808584abeafc44e8ca">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2c5c6aef45dd0b5cc10c800f986a7ce7" class="memitem:ga2c5c6aef45dd0b5cc10c800f986a7ce7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">MAX_MESSAGE_SIZE_TO_CACHE   10 * _DBUS_ONE_KILOBYTE</td>
</tr>
<tr class="memdesc:ga2c5c6aef45dd0b5cc10c800f986a7ce7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Avoid caching huge messages.<br />
</td>
</tr>
<tr class="separator:ga2c5c6aef45dd0b5cc10c800f986a7ce7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaeab2038ce58cd314dc1f23103abec5b0" class="memitem:gaeab2038ce58cd314dc1f23103abec5b0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">MAX_MESSAGE_CACHE_SIZE   5</td>
</tr>
<tr class="memdesc:gaeab2038ce58cd314dc1f23103abec5b0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Avoid caching too many messages.<br />
</td>
</tr>
<tr class="separator:gaeab2038ce58cd314dc1f23103abec5b0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacbe0bfe7a9551ab0489a0ec9aba6e94e" class="memitem:gacbe0bfe7a9551ab0489a0ec9aba6e94e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">INITIAL_LOADER_DATA_LEN   32</td>
</tr>
<tr class="memdesc:gacbe0bfe7a9551ab0489a0ec9aba6e94e">
<td class="mdescLeft"> </td>
<td class="mdescRight">The initial buffer size of the message loader.<br />
</td>
</tr>
<tr class="separator:gacbe0bfe7a9551ab0489a0ec9aba6e94e">
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
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_ga84c2bf86d0ab364b236814eafb85e512" class="memitem:ga84c2bf86d0ab364b236814eafb85e512">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusMessageRealIter </td>
<td class="memItemRight" data-valign="bottom">DBusMessageRealIter</td>
</tr>
<tr class="memdesc:ga84c2bf86d0ab364b236814eafb85e512">
<td class="mdescLeft"> </td>
<td class="mdescRight">typedef for internals of message iterator<br />
</td>
</tr>
<tr class="separator:ga84c2bf86d0ab364b236814eafb85e512">
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
<tr id="r_ga61dadd085c1777f559549e05962b2c9e" class="memitem:ga61dadd085c1777f559549e05962b2c9e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">{ <strong>DBUS_MESSAGE_ITER_TYPE_READER</strong> = 3 , <strong>DBUS_MESSAGE_ITER_TYPE_WRITER</strong> = 7 }</td>
</tr>
<tr class="separator:ga61dadd085c1777f559549e05962b2c9e">
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
<tr id="r_ga1ae02a435d19c3363e11c74b08c43ab2" class="memitem:ga1ae02a435d19c3363e11c74b08c43ab2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_iter_get_args_valist (DBusMessageIter *iter, DBusError *error, int first_arg_type, va_list var_args)</td>
</tr>
<tr class="memdesc:ga1ae02a435d19c3363e11c74b08c43ab2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Implementation of the varargs arg-getting functions.<br />
</td>
</tr>
<tr class="separator:ga1ae02a435d19c3363e11c74b08c43ab2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3dd4e06295c6776845dae3c14fecad1d" class="memitem:ga3dd4e06295c6776845dae3c14fecad1d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_get_n_unix_fds (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga3dd4e06295c6776845dae3c14fecad1d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the number of unix fds attached to this message.<br />
</td>
</tr>
<tr class="separator:ga3dd4e06295c6776845dae3c14fecad1d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7e3e6e067d4c4e90cd9e8d30ae09d312" class="memitem:ga7e3e6e067d4c4e90cd9e8d30ae09d312">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_trace_ref (DBusMessage *message, int old_refcount, int new_refcount, const char *why)</td>
</tr>
<tr class="separator:ga7e3e6e067d4c4e90cd9e8d30ae09d312">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac02bd01ebbcdd1c1f9ae4575655e49b2" class="memitem:gac02bd01ebbcdd1c1f9ae4575655e49b2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">  </td>
<td class="memItemRight" data-valign="bottom"><strong>_DBUS_STRING_DEFINE_STATIC</strong> (_dbus_empty_signature_str, "")</td>
</tr>
<tr class="memdesc:gac02bd01ebbcdd1c1f9ae4575655e49b2">
<td class="mdescLeft"> </td>
<td class="mdescRight">An static string representing an empty signature.<br />
</td>
</tr>
<tr class="separator:gac02bd01ebbcdd1c1f9ae4575655e49b2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga617811b117ac5eb31151ffb7dabea7a8" class="memitem:ga617811b117ac5eb31151ffb7dabea7a8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_get_network_data (DBusMessage *message, const DBusString **header, const DBusString **body)</td>
</tr>
<tr class="memdesc:ga617811b117ac5eb31151ffb7dabea7a8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the data to be sent over the network for this message.<br />
</td>
</tr>
<tr class="separator:ga617811b117ac5eb31151ffb7dabea7a8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga577e9d5224c56b9cf2ca2691be2e838c" class="memitem:ga577e9d5224c56b9cf2ca2691be2e838c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_get_unix_fds (DBusMessage *message, const int **fds, unsigned *n_fds)</td>
</tr>
<tr class="memdesc:ga577e9d5224c56b9cf2ca2691be2e838c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the unix fds to be sent over the network for this message.<br />
</td>
</tr>
<tr class="separator:ga577e9d5224c56b9cf2ca2691be2e838c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga19caed6967c6914097050be2f70a5794" class="memitem:ga19caed6967c6914097050be2f70a5794">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_remove_unknown_fields (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga19caed6967c6914097050be2f70a5794">
<td class="mdescLeft"> </td>
<td class="mdescRight">Remove every header field not known to this version of dbus.<br />
</td>
</tr>
<tr class="separator:ga19caed6967c6914097050be2f70a5794">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3dd30a62c63eb9972cc0c564f2a89c3b" class="memitem:ga3dd30a62c63eb9972cc0c564f2a89c3b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_serial (DBusMessage *message, dbus_uint32_t serial)</td>
</tr>
<tr class="memdesc:ga3dd30a62c63eb9972cc0c564f2a89c3b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the serial number of a message.<br />
</td>
</tr>
<tr class="separator:ga3dd30a62c63eb9972cc0c564f2a89c3b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafaed2adc00b2ec54b2827ecb778bbe7e" class="memitem:gafaed2adc00b2ec54b2827ecb778bbe7e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_add_counter_link (DBusMessage *message, DBusList *link)</td>
</tr>
<tr class="memdesc:gafaed2adc00b2ec54b2827ecb778bbe7e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a counter to be incremented immediately with the size/unix fds of this message, and decremented by the size/unix fds of this message when this message if finalized.<br />
</td>
</tr>
<tr class="separator:gafaed2adc00b2ec54b2827ecb778bbe7e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad009d79879d654a009c83627726435d8" class="memitem:gad009d79879d654a009c83627726435d8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_add_counter (DBusMessage *message, DBusCounter *counter)</td>
</tr>
<tr class="memdesc:gad009d79879d654a009c83627726435d8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a counter to be incremented immediately with the size/unix fds of this message, and decremented by the size/unix fds of this message when this message if finalized.<br />
</td>
</tr>
<tr class="separator:gad009d79879d654a009c83627726435d8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac84be3fd98e49409c1245a87c7de6f7d" class="memitem:gac84be3fd98e49409c1245a87c7de6f7d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_remove_counter (DBusMessage *message, DBusCounter *counter)</td>
</tr>
<tr class="memdesc:gac84be3fd98e49409c1245a87c7de6f7d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a counter tracking the size/unix fds of this message, and decrements the counter by the size/unix fds of this message.<br />
</td>
</tr>
<tr class="separator:gac84be3fd98e49409c1245a87c7de6f7d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3ecc9c24381af05289161f477ad6a578" class="memitem:ga3ecc9c24381af05289161f477ad6a578">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_lock (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga3ecc9c24381af05289161f477ad6a578">
<td class="mdescLeft"> </td>
<td class="mdescRight">Locks a message.<br />
</td>
</tr>
<tr class="separator:ga3ecc9c24381af05289161f477ad6a578">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga38435f8ee9846816f3d1c6d25ff45854" class="memitem:ga38435f8ee9846816f3d1c6d25ff45854">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_init_closed (DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:ga38435f8ee9846816f3d1c6d25ff45854">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initialize iter as if with DBUS_MESSAGE_ITER_INIT_CLOSED.<br />
</td>
</tr>
<tr class="separator:ga38435f8ee9846816f3d1c6d25ff45854">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae06a22cdc26e9ba9c815c6ac7e9f6816" class="memitem:gae06a22cdc26e9ba9c815c6ac7e9f6816">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessageLoader * </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_new (void)</td>
</tr>
<tr class="memdesc:gae06a22cdc26e9ba9c815c6ac7e9f6816">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new message loader.<br />
</td>
</tr>
<tr class="separator:gae06a22cdc26e9ba9c815c6ac7e9f6816">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf629b70605c76fc0e5f29105ce36a21c" class="memitem:gaf629b70605c76fc0e5f29105ce36a21c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessageLoader * </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_ref (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:gaf629b70605c76fc0e5f29105ce36a21c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count of the loader.<br />
</td>
</tr>
<tr class="separator:gaf629b70605c76fc0e5f29105ce36a21c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga51299aab1f5e0b2408ab858d3377b20c" class="memitem:ga51299aab1f5e0b2408ab858d3377b20c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_unref (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:ga51299aab1f5e0b2408ab858d3377b20c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count of the loader and finalizes the loader when the count reaches zero.<br />
</td>
</tr>
<tr class="separator:ga51299aab1f5e0b2408ab858d3377b20c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac45e5aedebf982e44c779ae9022254bd" class="memitem:gac45e5aedebf982e44c779ae9022254bd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_get_buffer (DBusMessageLoader *loader, DBusString **buffer, int *max_to_read, dbus_bool_t *may_read_fds)</td>
</tr>
<tr class="memdesc:gac45e5aedebf982e44c779ae9022254bd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the buffer to use for reading data from the network.<br />
</td>
</tr>
<tr class="separator:gac45e5aedebf982e44c779ae9022254bd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf5cb6398adb9fe39560fe6aef69ebb09" class="memitem:gaf5cb6398adb9fe39560fe6aef69ebb09">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_return_buffer (DBusMessageLoader *loader, DBusString *buffer)</td>
</tr>
<tr class="memdesc:gaf5cb6398adb9fe39560fe6aef69ebb09">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns a buffer obtained from _dbus_message_loader_get_buffer(), indicating to the loader how many bytes of the buffer were filled in.<br />
</td>
</tr>
<tr class="separator:gaf5cb6398adb9fe39560fe6aef69ebb09">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf55885371a6d022ec94c79bd7138923f" class="memitem:gaf55885371a6d022ec94c79bd7138923f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_queue_messages (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:gaf55885371a6d022ec94c79bd7138923f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Converts buffered data into messages, if we have enough data.<br />
</td>
</tr>
<tr class="separator:gaf55885371a6d022ec94c79bd7138923f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad2778bdc1817be34e54909e9677e7a8c" class="memitem:gad2778bdc1817be34e54909e9677e7a8c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_peek_message (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:gad2778bdc1817be34e54909e9677e7a8c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Peeks at first loaded message, returns NULL if no messages have been queued.<br />
</td>
</tr>
<tr class="separator:gad2778bdc1817be34e54909e9677e7a8c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5d59b83ee6b4381931c6d2a493cb8c85" class="memitem:ga5d59b83ee6b4381931c6d2a493cb8c85">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_pop_message (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:ga5d59b83ee6b4381931c6d2a493cb8c85">
<td class="mdescLeft"> </td>
<td class="mdescRight">Pops a loaded message (passing ownership of the message to the caller).<br />
</td>
</tr>
<tr class="separator:ga5d59b83ee6b4381931c6d2a493cb8c85">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf4e0a1f34d5703454c4e008401e72ab0" class="memitem:gaf4e0a1f34d5703454c4e008401e72ab0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_pop_message_link (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:gaf4e0a1f34d5703454c4e008401e72ab0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Pops a loaded message inside a list link (passing ownership of the message and link to the caller).<br />
</td>
</tr>
<tr class="separator:gaf4e0a1f34d5703454c4e008401e72ab0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga71b290eb470a55217971fcd6851fc40c" class="memitem:ga71b290eb470a55217971fcd6851fc40c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_putback_message_link (DBusMessageLoader *loader, DBusList *link)</td>
</tr>
<tr class="memdesc:ga71b290eb470a55217971fcd6851fc40c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns a popped message link, used to undo a pop.<br />
</td>
</tr>
<tr class="separator:ga71b290eb470a55217971fcd6851fc40c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga38da52ac9344b00df530098bdd9a3842" class="memitem:ga38da52ac9344b00df530098bdd9a3842">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_get_is_corrupted (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:ga38da52ac9344b00df530098bdd9a3842">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the loader is confused due to bad data.<br />
</td>
</tr>
<tr class="separator:ga38da52ac9344b00df530098bdd9a3842">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafb8c42ed5242274586607812ff6fba10" class="memitem:gafb8c42ed5242274586607812ff6fba10">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusValidity </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_get_corruption_reason (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:gafb8c42ed5242274586607812ff6fba10">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks what kind of bad data confused the loader.<br />
</td>
</tr>
<tr class="separator:gafb8c42ed5242274586607812ff6fba10">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga031623c6235f98801cab3e53f0a5f757" class="memitem:ga031623c6235f98801cab3e53f0a5f757">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_set_max_message_size (DBusMessageLoader *loader, long size)</td>
</tr>
<tr class="memdesc:ga031623c6235f98801cab3e53f0a5f757">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the maximum size message we allow.<br />
</td>
</tr>
<tr class="separator:ga031623c6235f98801cab3e53f0a5f757">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadd76a4b7191465f2dcb8e6b56b717961" class="memitem:gadd76a4b7191465f2dcb8e6b56b717961">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_get_max_message_size (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:gadd76a4b7191465f2dcb8e6b56b717961">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the maximum allowed message size in bytes.<br />
</td>
</tr>
<tr class="separator:gadd76a4b7191465f2dcb8e6b56b717961">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadd6c0fa721b4340df936363fbde912dc" class="memitem:gadd6c0fa721b4340df936363fbde912dc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_set_max_message_unix_fds (DBusMessageLoader *loader, long n)</td>
</tr>
<tr class="memdesc:gadd6c0fa721b4340df936363fbde912dc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the maximum unix fds per message we allow.<br />
</td>
</tr>
<tr class="separator:gadd6c0fa721b4340df936363fbde912dc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf65867d15c7d8adb91f430c483c180be" class="memitem:gaf65867d15c7d8adb91f430c483c180be">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_get_max_message_unix_fds (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:gaf65867d15c7d8adb91f430c483c180be">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the maximum allowed number of unix fds per message.<br />
</td>
</tr>
<tr class="separator:gaf65867d15c7d8adb91f430c483c180be">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8e01aad6af940ec4051703f59330da37" class="memitem:ga8e01aad6af940ec4051703f59330da37">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_get_pending_fds_count (DBusMessageLoader *loader)</td>
</tr>
<tr class="memdesc:ga8e01aad6af940ec4051703f59330da37">
<td class="mdescLeft"> </td>
<td class="mdescRight">Return how many file descriptors are pending in the loader.<br />
</td>
</tr>
<tr class="separator:ga8e01aad6af940ec4051703f59330da37">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga658a91d8efc59934016fae6905bfc4bf" class="memitem:ga658a91d8efc59934016fae6905bfc4bf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_message_loader_set_pending_fds_function (DBusMessageLoader *loader, void(*callback)(void *), void *data)</td>
</tr>
<tr class="memdesc:ga658a91d8efc59934016fae6905bfc4bf">
<td class="mdescLeft"> </td>
<td class="mdescRight">Register a function to be called whenever the number of pending file descriptors in the loader change.<br />
</td>
</tr>
<tr class="separator:ga658a91d8efc59934016fae6905bfc4bf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga537b3456202fdd9f305666504bde98fb" class="memitem:ga537b3456202fdd9f305666504bde98fb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_allocate_data_slot (dbus_int32_t *slot_p)</td>
</tr>
<tr class="memdesc:ga537b3456202fdd9f305666504bde98fb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocates an integer ID to be used for storing application-specific data on any DBusMessage.<br />
</td>
</tr>
<tr class="separator:ga537b3456202fdd9f305666504bde98fb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac7a5ba135e1aec4ad8c7b43752af02e1" class="memitem:gac7a5ba135e1aec4ad8c7b43752af02e1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_free_data_slot (dbus_int32_t *slot_p)</td>
</tr>
<tr class="memdesc:gac7a5ba135e1aec4ad8c7b43752af02e1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deallocates a global ID for message data slots.<br />
</td>
</tr>
<tr class="separator:gac7a5ba135e1aec4ad8c7b43752af02e1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga69d0bc701f9ca935e6de8a3f3e376c0a" class="memitem:ga69d0bc701f9ca935e6de8a3f3e376c0a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_data (DBusMessage *message, dbus_int32_t slot, void *data, DBusFreeFunction free_data_func)</td>
</tr>
<tr class="memdesc:ga69d0bc701f9ca935e6de8a3f3e376c0a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Stores a pointer on a DBusMessage, along with an optional function to be used for freeing the data when the data is set again, or when the message is finalized.<br />
</td>
</tr>
<tr class="separator:ga69d0bc701f9ca935e6de8a3f3e376c0a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7fe2ed3d9f1d4934fea36ad15976d01b" class="memitem:ga7fe2ed3d9f1d4934fea36ad15976d01b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_data (DBusMessage *message, dbus_int32_t slot)</td>
</tr>
<tr class="memdesc:ga7fe2ed3d9f1d4934fea36ad15976d01b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Retrieves data previously set with dbus_message_set_data().<br />
</td>
</tr>
<tr class="separator:ga7fe2ed3d9f1d4934fea36ad15976d01b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga40412bdfc6ba9cf9e167db4c23df0a7e" class="memitem:ga40412bdfc6ba9cf9e167db4c23df0a7e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_message_type_from_string (const char *type_str)</td>
</tr>
<tr class="memdesc:ga40412bdfc6ba9cf9e167db4c23df0a7e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Utility function to convert a machine-readable (not translated) string into a D-Bus message type.<br />
</td>
</tr>
<tr class="separator:ga40412bdfc6ba9cf9e167db4c23df0a7e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga86bdb40ec45e3de86e5ebe3503d443cf" class="memitem:ga86bdb40ec45e3de86e5ebe3503d443cf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_type_to_string (int type)</td>
</tr>
<tr class="memdesc:ga86bdb40ec45e3de86e5ebe3503d443cf">
<td class="mdescLeft"> </td>
<td class="mdescRight">Utility function to convert a D-Bus message type into a machine-readable string (not translated).<br />
</td>
</tr>
<tr class="separator:ga86bdb40ec45e3de86e5ebe3503d443cf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad85c737f9e7d03005d6028d6bbae7e87" class="memitem:gad85c737f9e7d03005d6028d6bbae7e87">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_marshal (DBusMessage *msg, char **marshalled_data_p, int *len_p)</td>
</tr>
<tr class="memdesc:gad85c737f9e7d03005d6028d6bbae7e87">
<td class="mdescLeft"> </td>
<td class="mdescRight">Turn a DBusMessage into the marshalled form as described in the D-Bus specification.<br />
</td>
</tr>
<tr class="separator:gad85c737f9e7d03005d6028d6bbae7e87">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5cbbd33d2d39ac2216fdbff8064be1c8" class="memitem:ga5cbbd33d2d39ac2216fdbff8064be1c8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_demarshal (const char *str, int len, DBusError *error)</td>
</tr>
<tr class="memdesc:ga5cbbd33d2d39ac2216fdbff8064be1c8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Demarshal a D-Bus message from the format described in the D-Bus specification.<br />
</td>
</tr>
<tr class="separator:ga5cbbd33d2d39ac2216fdbff8064be1c8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab0f8d8a640413e7c9b6c8f154acfbd1a" class="memitem:gab0f8d8a640413e7c9b6c8f154acfbd1a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_message_demarshal_bytes_needed (const char *buf, int len)</td>
</tr>
<tr class="memdesc:gab0f8d8a640413e7c9b6c8f154acfbd1a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the number of bytes required to be in the buffer to demarshal a D-Bus message.<br />
</td>
</tr>
<tr class="separator:gab0f8d8a640413e7c9b6c8f154acfbd1a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8955cc5a3fcc905230b9afc05e4b1470" class="memitem:ga8955cc5a3fcc905230b9afc05e4b1470">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_allow_interactive_authorization (DBusMessage *message, dbus_bool_t allow)</td>
</tr>
<tr class="memdesc:ga8955cc5a3fcc905230b9afc05e4b1470">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a flag indicating that the caller of the method is prepared to wait for interactive authorization to take place (for instance via Polkit) before the actual method is processed.<br />
</td>
</tr>
<tr class="separator:ga8955cc5a3fcc905230b9afc05e4b1470">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafc4b23ac32a763afa783b2a07143731b" class="memitem:gafc4b23ac32a763afa783b2a07143731b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_allow_interactive_authorization (DBusMessage *message)</td>
</tr>
<tr class="memdesc:gafc4b23ac32a763afa783b2a07143731b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns whether the flag controlled by dbus_message_set_allow_interactive_authorization() has been set.<br />
</td>
</tr>
<tr class="separator:gafc4b23ac32a763afa783b2a07143731b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1cacd2fff30096f57ea3d2923d92fdb4" class="memitem:ga1cacd2fff30096f57ea3d2923d92fdb4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusVariant * </td>
<td class="memItemRight" data-valign="bottom">_dbus_variant_read (DBusMessageIter *reader)</td>
</tr>
<tr class="memdesc:ga1cacd2fff30096f57ea3d2923d92fdb4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Copy a single D-Bus message item from reader into a newly-allocated DBusVariant.<br />
</td>
</tr>
<tr class="separator:ga1cacd2fff30096f57ea3d2923d92fdb4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9e81fbe246d3b50837c3929f2071612c" class="memitem:ga9e81fbe246d3b50837c3929f2071612c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_variant_get_signature (DBusVariant *self)</td>
</tr>
<tr class="memdesc:ga9e81fbe246d3b50837c3929f2071612c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Return the signature of the item stored in self.<br />
</td>
</tr>
<tr class="separator:ga9e81fbe246d3b50837c3929f2071612c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga308af94ab526dd6206ce94df184f63db" class="memitem:ga308af94ab526dd6206ce94df184f63db">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_variant_write (DBusVariant *self, DBusMessageIter *writer)</td>
</tr>
<tr class="memdesc:ga308af94ab526dd6206ce94df184f63db">
<td class="mdescLeft"> </td>
<td class="mdescRight">Copy the single D-Bus message item from self into writer.<br />
</td>
</tr>
<tr class="separator:ga308af94ab526dd6206ce94df184f63db">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4729ca8b25511ef1f37ec977e1701a62" class="memitem:ga4729ca8b25511ef1f37ec977e1701a62">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_variant_get_length (DBusVariant *self)</td>
</tr>
<tr class="separator:ga4729ca8b25511ef1f37ec977e1701a62">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga65383ff279a66bcf08e2bb4fce31c085" class="memitem:ga65383ff279a66bcf08e2bb4fce31c085">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const DBusString * </td>
<td class="memItemRight" data-valign="bottom">_dbus_variant_peek (DBusVariant *self)</td>
</tr>
<tr class="separator:ga65383ff279a66bcf08e2bb4fce31c085">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga239b8b34c7b60ae047a822b2e4fceb9b" class="memitem:ga239b8b34c7b60ae047a822b2e4fceb9b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_variant_free (DBusVariant *self)</td>
</tr>
<tr class="separator:ga239b8b34c7b60ae047a822b2e4fceb9b">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusMessage private implementation details.

The guts of DBusMessage and its methods.

## Macro Definition Documentation

## ◆ \_dbus_enable_message_cache

|                                      |     |     |     |           |
|--------------------------------------|-----|-----|-----|-----------|
| \#define \_dbus_enable_message_cache | (   |     | )   |    (TRUE) |

Definition at line 90 of file dbus-message.c.

## ◆ CHANGED_STAMP_BITS

|                                  |
|----------------------------------|
| \#define CHANGED_STAMP_BITS   21 |

How many bits are in the changed_stamp used to validate iterators.

Definition at line 92 of file dbus-message-private.h.

## ◆ CHECK_DBUS_1_10_BINARY_COMPATIBILITY

|                                                   |
|---------------------------------------------------|
| \#define CHECK_DBUS_1_10_BINARY_COMPATIBILITY   1 |

Definition at line 149 of file dbus-message.c.

## ◆ ensure_byte_order

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| \#define ensure_byte_order | ( |   | message | ) |    \_dbus_message_byteswap (message) |

byte-swap the message if it doesn't match our byte order.

Called only when we need the message in our own byte order, normally when reading arrays of integers or doubles. Otherwise should not be called since it would do needless work.

Definition at line 230 of file dbus-message.c.

## ◆ INITIAL_LOADER_DATA_LEN

|                                       |
|---------------------------------------|
| \#define INITIAL_LOADER_DATA_LEN   32 |

The initial buffer size of the message loader.

Definition at line 4168 of file dbus-message.c.

## ◆ MAX_MESSAGE_CACHE_SIZE

|                                     |
|-------------------------------------|
| \#define MAX_MESSAGE_CACHE_SIZE   5 |

Avoid caching too many messages.

Definition at line 511 of file dbus-message.c.

## ◆ MAX_MESSAGE_SIZE_TO_CACHE

|                                                                |
|----------------------------------------------------------------|
| \#define MAX_MESSAGE_SIZE_TO_CACHE   10 \* \_DBUS_ONE_KILOBYTE |

Avoid caching huge messages.

Definition at line 508 of file dbus-message.c.

## Typedef Documentation

## ◆ DBusMessageRealIter

|                                                        |
|--------------------------------------------------------|
| typedef struct DBusMessageRealIter DBusMessageRealIter |

typedef for internals of message iterator

Definition at line 121 of file dbus-message.c.

## Enumeration Type Documentation

## ◆ anonymous enum

|                |
|----------------|
| anonymous enum |

Definition at line 115 of file dbus-message.c.

## Function Documentation

## ◆ \_dbus_message_add_counter()

|                                        |     |                 |            |
|----------------------------------------|-----|-----------------|------------|
| dbus_bool_t \_dbus_message_add_counter | (   | DBusMessage \*  | *message*, |
|                                        |     | DBusCounter \*  | *counter*  |
|                                        | )   |                 |            |

Adds a counter to be incremented immediately with the size/unix fds of this message, and decremented by the size/unix fds of this message when this message if finalized.

This function may be called with locks held. As a result, the counter's notify function is not called; the caller is expected to either call \_dbus_counter_notify() on the counter when they are no longer holding locks, or take the same action that would be taken by the notify function.

Parameters  
|         |             |
|---------|-------------|
| message | the message |
| counter | the counter |

<!-- -->

Returns  
FALSE if no memory

Definition at line 376 of file dbus-message.c.

References \_dbus_counter_ref(), \_dbus_list_alloc_link(), \_dbus_message_add_counter_link(), FALSE, NULL, and TRUE.

Referenced by \_dbus_transport_queue_messages().

## ◆ \_dbus_message_add_counter_link()

|                                      |     |                 |            |
|--------------------------------------|-----|-----------------|------------|
| void \_dbus_message_add_counter_link | (   | DBusMessage \*  | *message*, |
|                                      |     | DBusList \*     | *link*     |
|                                      | )   |                 |            |

Adds a counter to be incremented immediately with the size/unix fds of this message, and decremented by the size/unix fds of this message when this message if finalized.

The link contains a counter with its refcount already incremented, but the counter itself not incremented. Ownership of link and counter refcount is passed to the message.

This function may be called with locks held. As a result, the counter's notify function is not called; the caller is expected to either call \_dbus_counter_notify() on the counter when they are no longer holding locks, or take the same action that would be taken by the notify function.

Parameters  
|         |                           |
|---------|---------------------------|
| message | the message               |
| link    | link with counter as data |

Definition at line 327 of file dbus-message.c.

References \_dbus_counter_adjust_size(), \_dbus_counter_adjust_unix_fd(), \_dbus_list_append_link(), \_dbus_string_get_length(), DBusMessage::body, DBusMessage::counters, DBusList::data, DBusHeader::data, DBusMessage::header, NULL, and DBusMessage::size_counter_delta.

Referenced by \_dbus_message_add_counter().

## ◆ \_dbus_message_get_n_unix_fds()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| unsigned int \_dbus_message_get_n_unix_fds | ( | DBusMessage \*  | *message* | ) |  |

Gets the number of unix fds attached to this message.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the number of file descriptors

Definition at line 42 of file dbus-message-util.c.

## ◆ \_dbus_message_get_network_data()

|                                      |     |                        |            |
|--------------------------------------|-----|------------------------|------------|
| void \_dbus_message_get_network_data | (   | DBusMessage \*         | *message*, |
|                                      |     | const DBusString \*\*  | *header*,  |
|                                      |     | const DBusString \*\*  | *body*     |
|                                      | )   |                        |            |

Gets the data to be sent over the network for this message.

The header and then the body should be written out. This function is guaranteed to always return the same data once a message is locked (with dbus_message_lock()).

Parameters  
|         |                                          |
|---------|------------------------------------------|
| message | the message.                             |
| header  | return location for message header data. |
| body    | return location for message body data.   |

Definition at line 243 of file dbus-message.c.

References \_dbus_assert, DBusMessage::body, DBusHeader::data, DBusMessage::header, and DBusMessage::locked.

## ◆ \_dbus_message_get_unix_fds()

|                                  |     |                 |            |
|----------------------------------|-----|-----------------|------------|
| void \_dbus_message_get_unix_fds | (   | DBusMessage \*  | *message*, |
|                                  |     | const int \*\*  | *fds*,     |
|                                  |     | unsigned \*     | *n_fds*    |
|                                  | )   |                 |            |

Gets the unix fds to be sent over the network for this message.

This function is guaranteed to always return the same data once a message is locked (with dbus_message_lock()).

Parameters  
|         |                                   |
|---------|-----------------------------------|
| message | the message.                      |
| fds     | return location of unix fd array  |
| n_fds   | return number of entries in array |

Definition at line 262 of file dbus-message.c.

References \_dbus_assert, DBusMessage::locked, and NULL.

## ◆ \_dbus_message_iter_get_args_valist()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_message_iter_get_args_valist | ( | DBusMessageIter \*  | *iter*, |
|  |  | DBusError \*  | *error*, |
|  |  | int  | *first_arg_type*, |
|  |  | va_list  | *var_args*  |
|  | ) |  |  |

Implementation of the varargs arg-getting functions.

dbus_message_get_args() is the place to go for complete documentation.

See also  
dbus_message_get_args

<!-- -->

Parameters  
|  |  |
|----|----|
| iter | the message iter |
| error | error to be filled in |
| first_arg_type | type of the first argument |
| var_args | return location for first argument, followed by list of type/location pairs |

<!-- -->

Returns  
FALSE if error was set

Definition at line 838 of file dbus-message.c.

References \_dbus_assert, \_dbus_close(), \_dbus_dup(), \_dbus_strdup(), \_dbus_type_reader_get_current_type(), \_dbus_type_reader_get_element_type(), \_dbus_type_reader_next(), \_dbus_type_reader_read_basic(), \_dbus_type_reader_read_fixed_multi(), \_dbus_type_reader_recurse(), \_dbus_type_to_string(), \_dbus_warn(), DBUS_ERROR_INCONSISTENT_MESSAGE, DBUS_ERROR_INVALID_ARGS, DBUS_ERROR_NOT_SUPPORTED, dbus_free_string_array(), dbus_message_iter_get_arg_type(), dbus_new0, dbus_set_error(), DBUS_TYPE_ARRAY, DBUS_TYPE_INVALID, dbus_type_is_basic(), dbus_type_is_fixed(), DBUS_TYPE_UNIX_FD, FALSE, DBusMessageRealIter::message, NULL, DBusMessageRealIter::reader, TRUE, DBusMessageRealIter::u, and DBusBasicValue::u32.

Referenced by dbus_message_get_args_valist().

## ◆ \_dbus_message_loader_get_buffer()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_message_loader_get_buffer | ( | DBusMessageLoader \*  | *loader*, |
|  |  | DBusString \*\*  | *buffer*, |
|  |  | int \*  | *max_to_read*, |
|  |  | dbus_bool_t \*  | *may_read_fds*  |
|  | ) |  |  |

Gets the buffer to use for reading data from the network.

Network data is read directly into an allocated buffer, which is then used in the DBusMessage, to avoid as many extra memcpy's as possible. The buffer must always be returned immediately using \_dbus_message_loader_return_buffer(), even if no bytes are successfully read.

Parameters  
|        |                     |
|--------|---------------------|
| loader | the message loader. |
| buffer | the buffer          |

Definition at line 4274 of file dbus-message.c.

References \_dbus_assert, \_dbus_header_have_message_untrusted(), \_dbus_string_get_length(), DBusMessageLoader::buffer_outstanding, DBusMessageLoader::data, DBUS_MAXIMUM_MESSAGE_LENGTH, DBUS_MINIMUM_HEADER_SIZE, DBUS_VALID, FALSE, DBusMessageLoader::max_message_size, NULL, and TRUE.

Referenced by dbus_message_demarshal().

## ◆ \_dbus_message_loader_get_corruption_reason()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusValidity \_dbus_message_loader_get_corruption_reason | ( | DBusMessageLoader \*  | *loader* | ) |  |

Checks what kind of bad data confused the loader.

Parameters  
|        |            |
|--------|------------|
| loader | the loader |

<!-- -->

Returns  
why the loader is hosed, or DBUS_VALID if it isn't.

Definition at line 4828 of file dbus-message.c.

References \_dbus_assert, DBusMessageLoader::corrupted, DBusMessageLoader::corruption_reason, and DBUS_VALID.

## ◆ \_dbus_message_loader_get_is_corrupted()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_message_loader_get_is_corrupted | ( | DBusMessageLoader \*  | *loader* | ) |  |

Checks whether the loader is confused due to bad data.

If messages are received that are invalid, the loader gets confused and gives up permanently. This state is called "corrupted."

Parameters  
|        |            |
|--------|------------|
| loader | the loader |

<!-- -->

Returns  
TRUE if the loader is hosed.

Definition at line 4814 of file dbus-message.c.

References \_dbus_assert, DBusMessageLoader::corrupted, DBusMessageLoader::corruption_reason, and DBUS_VALID.

Referenced by \_dbus_transport_queue_messages(), and dbus_message_demarshal().

## ◆ \_dbus_message_loader_get_max_message_size()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| long \_dbus_message_loader_get_max_message_size | ( | DBusMessageLoader \*  | *loader* | ) |  |

Gets the maximum allowed message size in bytes.

Parameters  
|        |            |
|--------|------------|
| loader | the loader |

<!-- -->

Returns  
max size in bytes

Definition at line 4862 of file dbus-message.c.

References DBusMessageLoader::max_message_size.

Referenced by \_dbus_transport_get_max_message_size().

## ◆ \_dbus_message_loader_get_max_message_unix_fds()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| long \_dbus_message_loader_get_max_message_unix_fds | ( | DBusMessageLoader \*  | *loader* | ) |  |

Gets the maximum allowed number of unix fds per message.

Parameters  
|        |            |
|--------|------------|
| loader | the loader |

<!-- -->

Returns  
max unix fds

Definition at line 4893 of file dbus-message.c.

References DBusMessageLoader::max_message_unix_fds.

Referenced by \_dbus_transport_get_max_message_unix_fds().

## ◆ \_dbus_message_loader_get_pending_fds_count()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| int \_dbus_message_loader_get_pending_fds_count | ( | DBusMessageLoader \*  | *loader* | ) |  |

Return how many file descriptors are pending in the loader.

Parameters  
|        |            |
|--------|------------|
| loader | the loader |

Definition at line 4904 of file dbus-message.c.

Referenced by \_dbus_transport_get_pending_fds_count().

## ◆ \_dbus_message_loader_new()

|                                                |     |       |     |     |     |
|------------------------------------------------|-----|-------|-----|-----|-----|
| DBusMessageLoader \* \_dbus_message_loader_new | (   | void  |     | )   |     |

Creates a new message loader.

Returns NULL if memory can't be allocated.

Returns  
new loader, or NULL.

Definition at line 4177 of file dbus-message.c.

References \_dbus_string_init(), \_dbus_string_set_length(), DBusMessageLoader::corrupted, DBusMessageLoader::corruption_reason, DBusMessageLoader::data, dbus_free(), DBUS_MAXIMUM_MESSAGE_LENGTH, dbus_new0, DBUS_VALID, FALSE, INITIAL_LOADER_DATA_LEN, DBusMessageLoader::max_message_size, DBusMessageLoader::max_message_unix_fds, NULL, and DBusMessageLoader::refcount.

Referenced by \_dbus_transport_init_base(), and dbus_message_demarshal().

## ◆ \_dbus_message_loader_peek_message()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusMessage \* \_dbus_message_loader_peek_message | ( | DBusMessageLoader \*  | *loader* | ) |  |

Peeks at first loaded message, returns NULL if no messages have been queued.

Parameters  
|        |             |
|--------|-------------|
| loader | the loader. |

<!-- -->

Returns  
the next message, or NULL if none.

Definition at line 4755 of file dbus-message.c.

References DBusList::data, DBusMessageLoader::messages, and NULL.

Referenced by \_dbus_transport_get_dispatch_status().

## ◆ \_dbus_message_loader_pop_message()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusMessage \* \_dbus_message_loader_pop_message | ( | DBusMessageLoader \*  | *loader* | ) |  |

Pops a loaded message (passing ownership of the message to the caller).

Returns NULL if no messages have been queued.

Parameters  
|        |             |
|--------|-------------|
| loader | the loader. |

<!-- -->

Returns  
the next message, or NULL if none.

Definition at line 4772 of file dbus-message.c.

References \_dbus_list_pop_first(), and DBusMessageLoader::messages.

Referenced by dbus_message_demarshal().

## ◆ \_dbus_message_loader_pop_message_link()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusList \* \_dbus_message_loader_pop_message_link | ( | DBusMessageLoader \*  | *loader* | ) |  |

Pops a loaded message inside a list link (passing ownership of the message and link to the caller).

Returns NULL if no messages have been loaded.

Parameters  
|        |             |
|--------|-------------|
| loader | the loader. |

<!-- -->

Returns  
the next message link, or NULL if none.

Definition at line 4786 of file dbus-message.c.

References \_dbus_list_pop_first_link(), and DBusMessageLoader::messages.

Referenced by \_dbus_transport_queue_messages().

## ◆ \_dbus_message_loader_putback_message_link()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_message_loader_putback_message_link | ( | DBusMessageLoader \*  | *loader*, |
|  |  | DBusList \*  | *link*  |
|  | ) |  |  |

Returns a popped message link, used to undo a pop.

Parameters  
|        |                               |
|--------|-------------------------------|
| loader | the loader                    |
| link   | the link with a message in it |

Definition at line 4798 of file dbus-message.c.

References \_dbus_list_prepend_link(), and DBusMessageLoader::messages.

Referenced by \_dbus_transport_queue_messages().

## ◆ \_dbus_message_loader_queue_messages()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_message_loader_queue_messages | ( | DBusMessageLoader \*  | *loader* | ) |  |

Converts buffered data into messages, if we have enough data.

If we don't have enough data, does nothing.

Parameters  
|        |             |
|--------|-------------|
| loader | the loader. |

<!-- -->

Returns  
TRUE if we had enough memory to finish.

Definition at line 4692 of file dbus-message.c.

References \_dbus_assert, \_dbus_header_have_message_untrusted(), \_dbus_list_find_last(), \_dbus_string_get_length(), DBusMessageLoader::corrupted, DBusMessageLoader::corruption_reason, DBusMessageLoader::data, dbus_message_unref(), DBUS_MINIMUM_HEADER_SIZE, DBUS_VALID, FALSE, DBusMessageLoader::max_message_size, DBusMessageLoader::messages, NULL, and TRUE.

Referenced by \_dbus_transport_get_dispatch_status(), and dbus_message_demarshal().

## ◆ \_dbus_message_loader_ref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusMessageLoader \* \_dbus_message_loader_ref | ( | DBusMessageLoader \*  | *loader* | ) |  |

Increments the reference count of the loader.

Parameters  
|        |             |
|--------|-------------|
| loader | the loader. |

<!-- -->

Returns  
the loader

Definition at line 4225 of file dbus-message.c.

References DBusMessageLoader::refcount.

## ◆ \_dbus_message_loader_return_buffer()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_message_loader_return_buffer | ( | DBusMessageLoader \*  | *loader*, |
|  |  | DBusString \*  | *buffer*  |
|  | ) |  |  |

Returns a buffer obtained from \_dbus_message_loader_get_buffer(), indicating to the loader how many bytes of the buffer were filled in.

This function must always be called, even if no bytes were successfully read.

Parameters  
|        |             |
|--------|-------------|
| loader | the loader. |
| buffer | the buffer. |

Definition at line 4380 of file dbus-message.c.

References \_dbus_assert, DBusMessageLoader::buffer_outstanding, DBusMessageLoader::data, and FALSE.

Referenced by dbus_message_demarshal().

## ◆ \_dbus_message_loader_set_max_message_size()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_message_loader_set_max_message_size | ( | DBusMessageLoader \*  | *loader*, |
|  |  | long  | *size*  |
|  | ) |  |  |

Sets the maximum size message we allow.

Parameters  
|        |                               |
|--------|-------------------------------|
| loader | the loader                    |
| size   | the max message size in bytes |

Definition at line 4843 of file dbus-message.c.

References DBUS_MAXIMUM_MESSAGE_LENGTH, and DBusMessageLoader::max_message_size.

Referenced by \_dbus_transport_set_max_message_size().

## ◆ \_dbus_message_loader_set_max_message_unix_fds()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_message_loader_set_max_message_unix_fds | ( | DBusMessageLoader \*  | *loader*, |
|  |  | long  | *n*  |
|  | ) |  |  |

Sets the maximum unix fds per message we allow.

Parameters  
|        |                                         |
|--------|-----------------------------------------|
| loader | the loader                              |
| n      | the max number of unix fds in a message |

Definition at line 4874 of file dbus-message.c.

References DBUS_MAXIMUM_MESSAGE_UNIX_FDS, and DBusMessageLoader::max_message_unix_fds.

Referenced by \_dbus_transport_set_max_message_unix_fds().

## ◆ \_dbus_message_loader_set_pending_fds_function()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_message_loader_set_pending_fds_function | ( | DBusMessageLoader \*  | *loader*, |
|  |  | void(\*)(void \*)  | *callback*, |
|  |  | void \*  | *data*  |
|  | ) |  |  |

Register a function to be called whenever the number of pending file descriptors in the loader change.

Parameters  
|          |                           |
|----------|---------------------------|
| loader   | the loader                |
| callback | the callback              |
| data     | the data for the callback |

Definition at line 4922 of file dbus-message.c.

Referenced by \_dbus_transport_set_pending_fds_function().

## ◆ \_dbus_message_loader_unref()

|                                  |     |                       |          |     |     |
|----------------------------------|-----|-----------------------|----------|-----|-----|
| void \_dbus_message_loader_unref | (   | DBusMessageLoader \*  | *loader* | )   |     |

Decrements the reference count of the loader and finalizes the loader when the count reaches zero.

Parameters  
|        |             |
|--------|-------------|
| loader | the loader. |

Definition at line 4239 of file dbus-message.c.

References \_dbus_list_clear_full(), \_dbus_string_free(), DBusMessageLoader::data, dbus_free(), dbus_message_unref(), DBusMessageLoader::messages, and DBusMessageLoader::refcount.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_init_base(), and dbus_message_demarshal().

## ◆ \_dbus_message_remove_counter()

|                                    |     |                 |            |
|------------------------------------|-----|-----------------|------------|
| void \_dbus_message_remove_counter | (   | DBusMessage \*  | *message*, |
|                                    |     | DBusCounter \*  | *counter*  |
|                                    | )   |                 |            |

Removes a counter tracking the size/unix fds of this message, and decrements the counter by the size/unix fds of this message.

Parameters  
|         |             |
|---------|-------------|
| message | the message |
| counter | the counter |

Definition at line 399 of file dbus-message.c.

References \_dbus_assert, \_dbus_counter_adjust_size(), \_dbus_counter_adjust_unix_fd(), \_dbus_counter_notify(), \_dbus_counter_unref(), \_dbus_list_find_last(), \_dbus_list_remove_link(), DBusMessage::counters, NULL, and DBusMessage::size_counter_delta.

Referenced by \_dbus_connection_message_sent_unlocked().

## ◆ \_dbus_message_remove_unknown_fields()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_message_remove_unknown_fields | ( | DBusMessage \*  | *message* | ) |  |

Remove every header field not known to this version of dbus.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
FALSE if no memory

Definition at line 284 of file dbus-message.c.

References \_dbus_header_remove_unknown_fields(), and DBusMessage::header.

## ◆ \_dbus_message_trace_ref()

|                               |     |                 |                 |
|-------------------------------|-----|-----------------|-----------------|
| void \_dbus_message_trace_ref | (   | DBusMessage \*  | *message*,      |
|                               |     | int             | *old_refcount*, |
|                               |     | int             | *new_refcount*, |
|                               |     | const char \*   | *why*           |
|                               | )   |                 |                 |

Definition at line 95 of file dbus-message.c.

## ◆ \_dbus_variant_free()

|                          |     |                 |        |     |     |
|--------------------------|-----|-----------------|--------|-----|-----|
| void \_dbus_variant_free | (   | DBusVariant \*  | *self* | )   |     |

Definition at line 5565 of file dbus-message.c.

## ◆ \_dbus_variant_get_length()

|                               |     |                 |        |     |     |
|-------------------------------|-----|-----------------|--------|-----|-----|
| int \_dbus_variant_get_length | (   | DBusVariant \*  | *self* | )   |     |

Definition at line 5551 of file dbus-message.c.

## ◆ \_dbus_variant_get_signature()

|                                            |     |                 |        |     |     |
|--------------------------------------------|-----|-----------------|--------|-----|-----|
| const char \* \_dbus_variant_get_signature | (   | DBusVariant \*  | *self* | )   |     |

Return the signature of the item stored in self.

It is a single complete type.

Parameters  
|      |             |
|------|-------------|
| self | the variant |

Definition at line 5485 of file dbus-message.c.

References \_dbus_assert, \_dbus_string_get_byte(), \_dbus_string_get_const_data_len(), and NULL.

## ◆ \_dbus_variant_peek()

|                                         |     |                 |        |     |     |
|-----------------------------------------|-----|-----------------|--------|-----|-----|
| const DBusString \* \_dbus_variant_peek | (   | DBusVariant \*  | *self* | )   |     |

Definition at line 5558 of file dbus-message.c.

## ◆ \_dbus_variant_read()

|                                    |     |                     |          |     |     |
|------------------------------------|-----|---------------------|----------|-----|-----|
| DBusVariant \* \_dbus_variant_read | (   | DBusMessageIter \*  | *reader* | )   |     |

Copy a single D-Bus message item from reader into a newly-allocated DBusVariant.

For example, if a message contains three string arguments, and reader points to the second string, the resulting DBusVariant will have signature DBUS_TYPE_STRING_AS_STRING and contain only that second string.

Parameters  
|        |                                                              |
|--------|--------------------------------------------------------------|
| reader | An iterator over message items, pointing to one item to copy |

<!-- -->

Returns  
The variant, or NULL if out of memory

Definition at line 5349 of file dbus-message.c.

References \_dbus_assert, \_dbus_string_copy_len(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_string_init_const(), \_dbus_type_reader_get_signature(), \_dbus_type_writer_init_values_only(), \_dbus_type_writer_recurse(), \_dbus_type_writer_unrecurse(), \_dbus_type_writer_write_basic(), \_dbus_type_writer_write_reader(), dbus_free(), dbus_message_iter_get_arg_type(), dbus_message_iter_get_basic(), dbus_message_iter_recurse(), dbus_new0, DBUS_TYPE_ARRAY, DBUS_TYPE_DICT_ENTRY, dbus_type_is_basic(), DBUS_TYPE_STRUCT, DBUS_TYPE_VARIANT, DBUS_TYPE_VARIANT_AS_STRING, FALSE, DBusMessageRealIter::iter_type, NULL, DBusMessageRealIter::reader, TRUE, and DBusMessageRealIter::u.

## ◆ \_dbus_variant_write()

|                                  |     |                     |           |
|----------------------------------|-----|---------------------|-----------|
| dbus_bool_t \_dbus_variant_write | (   | DBusVariant \*      | *self*,   |
|                                  |     | DBusMessageIter \*  | *writer*  |
|                                  | )   |                     |           |

Copy the single D-Bus message item from self into writer.

For example, if writer points into the body of an empty message and self has signature DBUS_TYPE_STRING_AS_STRING, then the message will have signature DBUS_TYPE_STRING_AS_STRING after this function returns

Parameters  
|        |                                                |
|--------|------------------------------------------------|
| self   | the variant                                    |
| writer | the place to write the contents of the variant |

<!-- -->

Returns  
TRUE on success, FALSE if out of memory

Definition at line 5516 of file dbus-message.c.

References \_dbus_assert, \_dbus_string_init_const(), \_dbus_type_reader_init(), \_dbus_type_reader_recurse(), \_dbus_type_writer_write_reader(), DBUS_TYPE_VARIANT_AS_STRING, FALSE, DBusMessageRealIter::iter_type, NULL, DBusMessageRealIter::u, and DBusMessageRealIter::writer.

## ◆ dbus_message_allocate_data_slot()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t dbus_message_allocate_data_slot | ( | dbus_int32_t \*  | *slot_p* | ) |  |

Allocates an integer ID to be used for storing application-specific data on any DBusMessage.

The allocated ID may then be used with dbus_message_set_data() and dbus_message_get_data(). The passed-in slot must be initialized to -1, and is filled in with the slot ID. If the passed-in slot is not -1, it's assumed to be already allocated, and its refcount is incremented.

The allocated slot is global, i.e. all DBusMessage objects will have a slot with the given integer ID reserved.

Parameters  
|        |                                               |
|--------|-----------------------------------------------|
| slot_p | address of a global variable storing the slot |

<!-- -->

Returns  
FALSE on failure (no memory)

Definition at line 4950 of file dbus-message.c.

References \_dbus_data_slot_allocator_alloc().

## ◆ dbus_message_demarshal()

|                                       |     |                |          |
|---------------------------------------|-----|----------------|----------|
| DBusMessage \* dbus_message_demarshal | (   | const char \*  | *str*,   |
|                                       |     | int            | *len*,   |
|                                       |     | DBusError \*   | *error*  |
|                                       | )   |                |          |

Demarshal a D-Bus message from the format described in the D-Bus specification.

Generally, this function is only useful for encapsulating D-Bus messages in a different protocol.

Parameters  
|       |                                |
|-------|--------------------------------|
| str   | the marshalled DBusMessage     |
| len   | the length of str              |
| error | the location to save errors to |

<!-- -->

Returns  
NULL if there was an error

Definition at line 5173 of file dbus-message.c.

References \_dbus_message_loader_get_buffer(), \_dbus_message_loader_get_is_corrupted(), \_dbus_message_loader_new(), \_dbus_message_loader_pop_message(), \_dbus_message_loader_queue_messages(), \_dbus_message_loader_return_buffer(), \_dbus_message_loader_unref(), \_dbus_string_append_len(), DBusMessageLoader::corruption_reason, DBUS_ERROR_INVALID_ARGS, dbus_set_error(), DBUS_VALIDITY_UNKNOWN_OOM_ERROR, and NULL.

## ◆ dbus_message_demarshal_bytes_needed()

|                                         |     |                |        |
|-----------------------------------------|-----|----------------|--------|
| int dbus_message_demarshal_bytes_needed | (   | const char \*  | *buf*, |
|                                         |     | int            | *len*  |
|                                         | )   |                |        |

Returns the number of bytes required to be in the buffer to demarshal a D-Bus message.

Generally, this function is only useful for encapsulating D-Bus messages in a different protocol.

Parameters  
|     |                       |
|-----|-----------------------|
| buf | data to be marshalled |
| len | the length of `buf`   |

<!-- -->

Returns  
-1 if there was no valid data to be demarshalled, 0 if there wasn't enough data to determine how much should be demarshalled. Otherwise returns the number of bytes to be demarshalled

Definition at line 5240 of file dbus-message.c.

References \_dbus_assert, \_dbus_header_have_message_untrusted(), \_dbus_string_free(), \_dbus_string_init_const_len(), DBUS_MAXIMUM_MESSAGE_LENGTH, DBUS_MINIMUM_HEADER_SIZE, and DBUS_VALID.

## ◆ dbus_message_free_data_slot()

|                                  |     |                  |          |     |     |
|----------------------------------|-----|------------------|----------|-----|-----|
| void dbus_message_free_data_slot | (   | dbus_int32_t \*  | *slot_p* | )   |     |

Deallocates a global ID for message data slots.

dbus_message_get_data() and dbus_message_set_data() may no longer be used with this slot. Existing data stored on existing DBusMessage objects will be freed when the message is finalized, but may not be retrieved (and may only be replaced if someone else reallocates the slot). When the refcount on the passed-in slot reaches 0, it is set to -1.

Parameters  
|        |                                        |
|--------|----------------------------------------|
| slot_p | address storing the slot to deallocate |

Definition at line 4968 of file dbus-message.c.

References \_dbus_data_slot_allocator_free().

## ◆ dbus_message_get_allow_interactive_authorization()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t dbus_message_get_allow_interactive_authorization | ( | DBusMessage \*  | *message* | ) |  |

Returns whether the flag controlled by dbus_message_set_allow_interactive_authorization() has been set.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

Definition at line 5318 of file dbus-message.c.

References \_dbus_header_get_flag(), DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION, FALSE, DBusMessage::header, and NULL.

## ◆ dbus_message_get_data()

|                               |     |                 |            |
|-------------------------------|-----|-----------------|------------|
| void \* dbus_message_get_data | (   | DBusMessage \*  | *message*, |
|                               |     | dbus_int32_t    | *slot*     |
|                               | )   |                 |            |

Retrieves data previously set with dbus_message_set_data().

The slot must still be allocated (must not have been freed).

Parameters  
|         |                           |
|---------|---------------------------|
| message | the message               |
| slot    | the slot to get data from |

<!-- -->

Returns  
the data, or NULL if not found

Definition at line 5025 of file dbus-message.c.

References \_dbus_data_slot_list_get(), NULL, and DBusMessage::slot_list.

## ◆ dbus_message_iter_init_closed()

|                                    |     |                     |        |     |     |
|------------------------------------|-----|---------------------|--------|-----|-----|
| void dbus_message_iter_init_closed | (   | DBusMessageIter \*  | *iter* | )   |     |

Initialize iter as if with DBUS_MESSAGE_ITER_INIT_CLOSED.

The only valid operation for such an iterator is dbus_message_iter_abandon_container_if_open(), which does nothing.

Definition at line 755 of file dbus-message.c.

References NULL.

## ◆ dbus_message_lock()

|                        |     |                 |           |     |     |
|------------------------|-----|-----------------|-----------|-----|-----|
| void dbus_message_lock | (   | DBusMessage \*  | *message* | )   |     |

Locks a message.

Allows checking that applications don't keep a reference to a message in the outgoing queue and change it underneath us. Messages are locked when they enter the outgoing queue (dbus_connection_send_message()), and the library complains if the message is modified while locked. This function may also called externally, for applications wrapping D-Bus in another protocol.

Parameters  
|         |                      |
|---------|----------------------|
| message | the message to lock. |

Definition at line 431 of file dbus-message.c.

References \_dbus_assert, \_dbus_header_update_lengths(), \_dbus_string_get_length(), DBusMessage::body, dbus_message_get_signature(), DBusMessage::header, DBusMessage::locked, NULL, and TRUE.

Referenced by dbus_message_marshal().

## ◆ dbus_message_marshal()

|                                  |     |                 |                      |
|----------------------------------|-----|-----------------|----------------------|
| dbus_bool_t dbus_message_marshal | (   | DBusMessage \*  | *msg*,               |
|                                  |     | char \*\*       | *marshalled_data_p*, |
|                                  |     | int \*          | *len_p*              |
|                                  | )   |                 |                      |

Turn a DBusMessage into the marshalled form as described in the D-Bus specification.

Generally, this function is only useful for encapsulating D-Bus messages in a different protocol.

Parameters  
|  |  |
|----|----|
| msg | the DBusMessage |
| marshalled_data_p | the location to save the marshalled form to |
| len_p | the location to save the length of the marshalled form to |

<!-- -->

Returns  
FALSE if there was not enough memory

Definition at line 5111 of file dbus-message.c.

References \_dbus_string_copy(), \_dbus_string_free(), \_dbus_string_get_length(), \_dbus_string_init(), \_dbus_string_steal_data(), DBusMessage::body, DBusHeader::data, dbus_message_lock(), FALSE, DBusMessage::header, DBusMessage::locked, NULL, and TRUE.

## ◆ dbus_message_set_allow_interactive_authorization()

|  |  |  |  |
|----|----|----|----|
| void dbus_message_set_allow_interactive_authorization | ( | DBusMessage \*  | *message*, |
|  |  | dbus_bool_t  | *allow*  |
|  | ) |  |  |

Sets a flag indicating that the caller of the method is prepared to wait for interactive authorization to take place (for instance via Polkit) before the actual method is processed.

The flag is FALSE by default; that is, by default the other end is expected to make any authorization decisions non-interactively and promptly. It may use the error DBUS_ERROR_INTERACTIVE_AUTHORIZATION_REQUIRED to signal that authorization failed, but could have succeeded if this flag had been used.

For messages whose type is not DBUS_MESSAGE_TYPE_METHOD_CALL, this flag is meaningless and should not be set.

On the protocol level this toggles DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION.

Parameters  
|         |                                                 |
|---------|-------------------------------------------------|
| message | the message                                     |
| allow   | TRUE if interactive authorization is acceptable |

Definition at line 5300 of file dbus-message.c.

References \_dbus_header_toggle_flag(), DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION, DBusMessage::header, DBusMessage::locked, and NULL.

## ◆ dbus_message_set_data()

|                                   |     |                   |                   |
|-----------------------------------|-----|-------------------|-------------------|
| dbus_bool_t dbus_message_set_data | (   | DBusMessage \*    | *message*,        |
|                                   |     | dbus_int32_t      | *slot*,           |
|                                   |     | void \*           | *data*,           |
|                                   |     | DBusFreeFunction  | *free_data_func*  |
|                                   | )   |                   |                   |

Stores a pointer on a DBusMessage, along with an optional function to be used for freeing the data when the data is set again, or when the message is finalized.

The slot number must have been allocated with dbus_message_allocate_data_slot().

Parameters  
|                |                                 |
|----------------|---------------------------------|
| message        | the message                     |
| slot           | the slot number                 |
| data           | the data to store               |
| free_data_func | finalizer function for the data |

<!-- -->

Returns  
TRUE if there was enough memory to store the data

Definition at line 4989 of file dbus-message.c.

References \_dbus_data_slot_list_set(), FALSE, NULL, and DBusMessage::slot_list.

## ◆ dbus_message_set_serial()

|                              |     |                 |            |
|------------------------------|-----|-----------------|------------|
| void dbus_message_set_serial | (   | DBusMessage \*  | *message*, |
|                              |     | dbus_uint32_t   | *serial*   |
|                              | )   |                 |            |

Sets the serial number of a message.

This can only be done once on a message.

DBusConnection will automatically set the serial to an appropriate value when the message is sent; this function is only needed when encapsulating messages in another protocol, or otherwise bypassing DBusConnection.

Parameters  
|         |             |
|---------|-------------|
| message | the message |
| serial  | the serial  |

Definition at line 301 of file dbus-message.c.

References \_dbus_header_set_serial(), DBusMessage::header, DBusMessage::locked, and NULL.

Referenced by dbus_connection_send_with_reply().

## ◆ dbus_message_type_from_string()

|                                   |     |                |            |     |     |
|-----------------------------------|-----|----------------|------------|-----|-----|
| int dbus_message_type_from_string | (   | const char \*  | *type_str* | )   |     |

Utility function to convert a machine-readable (not translated) string into a D-Bus message type.

"method_call" -\> DBUS_MESSAGE_TYPE_METHOD_CALL

"method_return" -\> DBUS_MESSAGE_TYPE_METHOD_RETURN

"signal" -\> DBUS_MESSAGE_TYPE_SIGNAL

"error" -\> DBUS_MESSAGE_TYPE_ERROR

anything else -\> DBUS_MESSAGE_TYPE_INVALID

DBUS_MESSAGE_TYPE_METHOD_CALL

\#define DBUS_MESSAGE_TYPE_METHOD_CALL

Message type of a method call message, see dbus_message_get_type()

**Definition** dbus-protocol.h:236

DBUS_MESSAGE_TYPE_ERROR

\#define DBUS_MESSAGE_TYPE_ERROR

Message type of an error reply message, see dbus_message_get_type()

**Definition** dbus-protocol.h:240

DBUS_MESSAGE_TYPE_METHOD_RETURN

\#define DBUS_MESSAGE_TYPE_METHOD_RETURN

Message type of a method return message, see dbus_message_get_type()

**Definition** dbus-protocol.h:238

DBUS_MESSAGE_TYPE_SIGNAL

\#define DBUS_MESSAGE_TYPE_SIGNAL

Message type of a signal message, see dbus_message_get_type()

**Definition** dbus-protocol.h:242

DBUS_MESSAGE_TYPE_INVALID

\#define DBUS_MESSAGE_TYPE_INVALID

This value is never a valid message type, see dbus_message_get_type()

**Definition** dbus-protocol.h:234

Definition at line 5053 of file dbus-message.c.

References DBUS_MESSAGE_TYPE_ERROR, DBUS_MESSAGE_TYPE_INVALID, DBUS_MESSAGE_TYPE_METHOD_CALL, DBUS_MESSAGE_TYPE_METHOD_RETURN, and DBUS_MESSAGE_TYPE_SIGNAL.

## ◆ dbus_message_type_to_string()

|                                           |     |      |        |     |     |
|-------------------------------------------|-----|------|--------|-----|-----|
| const char \* dbus_message_type_to_string | (   | int  | *type* | )   |     |

Utility function to convert a D-Bus message type into a machine-readable string (not translated).

DBUS_MESSAGE_TYPE_METHOD_CALL -\> "method_call"

DBUS_MESSAGE_TYPE_METHOD_RETURN -\> "method_return"

DBUS_MESSAGE_TYPE_SIGNAL -\> "signal"

DBUS_MESSAGE_TYPE_ERROR -\> "error"

DBUS_MESSAGE_TYPE_INVALID -\> "invalid"

Definition at line 5081 of file dbus-message.c.

References DBUS_MESSAGE_TYPE_ERROR, DBUS_MESSAGE_TYPE_METHOD_CALL, DBUS_MESSAGE_TYPE_METHOD_RETURN, and DBUS_MESSAGE_TYPE_SIGNAL.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_connection_queue_received_message_link(), and dbus_connection_dispatch().
