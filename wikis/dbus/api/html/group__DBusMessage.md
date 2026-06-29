DBusMessage

D-Bus low-level public API

Message to be sent or received over a DBusConnection. More...

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
<td class="memItemRight" data-valign="bottom">DBusMessageIter</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBusMessageIter struct; contains no public fields. More...<br />
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
<tr id="r_ga28e188fd38c65ea73e9aeedf30132d26" class="memitem:ga28e188fd38c65ea73e9aeedf30132d26">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MESSAGE_ITER_INIT_CLOSED</td>
</tr>
<tr class="memdesc:ga28e188fd38c65ea73e9aeedf30132d26">
<td class="mdescLeft"> </td>
<td class="mdescRight">A message iterator for which dbus_message_iter_abandon_container_if_open() is the only valid operation.<br />
</td>
</tr>
<tr class="separator:ga28e188fd38c65ea73e9aeedf30132d26">
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
<tr id="r_ga1c4e61fd8bcfe1160354cb578dc1731a" class="memitem:ga1c4e61fd8bcfe1160354cb578dc1731a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusMessage </td>
<td class="memItemRight" data-valign="bottom">DBusMessage</td>
</tr>
<tr class="memdesc:ga1c4e61fd8bcfe1160354cb578dc1731a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque data type representing a message received from or to be sent to another application.<br />
</td>
</tr>
<tr class="separator:ga1c4e61fd8bcfe1160354cb578dc1731a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3c1fed733a5a3fd2a4376ce4f645b5ff" class="memitem:ga3c1fed733a5a3fd2a4376ce4f645b5ff">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusMessageIter </td>
<td class="memItemRight" data-valign="bottom">DBusMessageIter</td>
</tr>
<tr class="memdesc:ga3c1fed733a5a3fd2a4376ce4f645b5ff">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque type representing a message iterator.<br />
</td>
</tr>
<tr class="separator:ga3c1fed733a5a3fd2a4376ce4f645b5ff">
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
<tr id="r_ga390710c25564c80025a006c376da2030" class="memitem:ga390710c25564c80025a006c376da2030">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_serial (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga390710c25564c80025a006c376da2030">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the serial of a message or 0 if none has been specified.<br />
</td>
</tr>
<tr class="separator:ga390710c25564c80025a006c376da2030">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaec08603ff3d49bbcded67d25188a23f1" class="memitem:gaec08603ff3d49bbcded67d25188a23f1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_reply_serial (DBusMessage *message, dbus_uint32_t reply_serial)</td>
</tr>
<tr class="memdesc:gaec08603ff3d49bbcded67d25188a23f1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the reply serial of a message (the serial of the message this is a reply to).<br />
</td>
</tr>
<tr class="separator:gaec08603ff3d49bbcded67d25188a23f1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga94c43b2b237d842a6b91da6f94818d47" class="memitem:ga94c43b2b237d842a6b91da6f94818d47">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_reply_serial (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga94c43b2b237d842a6b91da6f94818d47">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the serial that the message is a reply to or 0 if none.<br />
</td>
</tr>
<tr class="separator:ga94c43b2b237d842a6b91da6f94818d47">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab9e5bf8d87a95c5ca7026a791148ebd4" class="memitem:gab9e5bf8d87a95c5ca7026a791148ebd4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_new (int message_type)</td>
</tr>
<tr class="memdesc:gab9e5bf8d87a95c5ca7026a791148ebd4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Constructs a new message of the given message type.<br />
</td>
</tr>
<tr class="separator:gab9e5bf8d87a95c5ca7026a791148ebd4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga98ddc82450d818138ef326a284201ee0" class="memitem:ga98ddc82450d818138ef326a284201ee0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_new_method_call (const char *destination, const char *path, const char *iface, const char *method)</td>
</tr>
<tr class="memdesc:ga98ddc82450d818138ef326a284201ee0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Constructs a new message to invoke a method on a remote object.<br />
</td>
</tr>
<tr class="separator:ga98ddc82450d818138ef326a284201ee0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga95142bd8288f397194ee0eefb1d27125" class="memitem:ga95142bd8288f397194ee0eefb1d27125">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_new_method_return (DBusMessage *method_call)</td>
</tr>
<tr class="memdesc:ga95142bd8288f397194ee0eefb1d27125">
<td class="mdescLeft"> </td>
<td class="mdescRight">Constructs a message that is a reply to a method call.<br />
</td>
</tr>
<tr class="separator:ga95142bd8288f397194ee0eefb1d27125">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6ce3213dfb17be7956affba40207a5a0" class="memitem:ga6ce3213dfb17be7956affba40207a5a0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_new_signal (const char *path, const char *iface, const char *name)</td>
</tr>
<tr class="memdesc:ga6ce3213dfb17be7956affba40207a5a0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Constructs a new message representing a signal emission.<br />
</td>
</tr>
<tr class="separator:ga6ce3213dfb17be7956affba40207a5a0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2ab896965aec97fb21293affeed36232" class="memitem:ga2ab896965aec97fb21293affeed36232">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_new_error (DBusMessage *reply_to, const char *error_name, const char *error_message)</td>
</tr>
<tr class="memdesc:ga2ab896965aec97fb21293affeed36232">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new message that is an error reply to another message.<br />
</td>
</tr>
<tr class="separator:ga2ab896965aec97fb21293affeed36232">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga707a27881820f964e3606bc906a47978" class="memitem:ga707a27881820f964e3606bc906a47978">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_new_error_printf (DBusMessage *reply_to, const char *error_name, const char *error_format,...)</td>
</tr>
<tr class="memdesc:ga707a27881820f964e3606bc906a47978">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new message that is an error reply to another message, allowing you to use printf formatting.<br />
</td>
</tr>
<tr class="separator:ga707a27881820f964e3606bc906a47978">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4bed3858b3b48ec7c86d9fc56a6ce372" class="memitem:ga4bed3858b3b48ec7c86d9fc56a6ce372">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_copy (const DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga4bed3858b3b48ec7c86d9fc56a6ce372">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new message that is an exact replica of the message specified, except that its refcount is set to 1, its message serial is reset to 0, and if the original message was "locked" (in the outgoing message queue and thus not modifiable) the new message will not be locked.<br />
</td>
</tr>
<tr class="separator:ga4bed3858b3b48ec7c86d9fc56a6ce372">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga834035e4817acd64adc8ca584bdf3982" class="memitem:ga834035e4817acd64adc8ca584bdf3982">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_ref (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga834035e4817acd64adc8ca584bdf3982">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count of a DBusMessage.<br />
</td>
</tr>
<tr class="separator:ga834035e4817acd64adc8ca584bdf3982">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab69441efe683918f6a82469c8763f464" class="memitem:gab69441efe683918f6a82469c8763f464">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_unref (DBusMessage *message)</td>
</tr>
<tr class="memdesc:gab69441efe683918f6a82469c8763f464">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count of a DBusMessage, freeing the message if the count reaches 0.<br />
</td>
</tr>
<tr class="separator:gab69441efe683918f6a82469c8763f464">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga41cace31999105137772b6257ea540f9" class="memitem:ga41cace31999105137772b6257ea540f9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_type (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga41cace31999105137772b6257ea540f9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the type of a message.<br />
</td>
</tr>
<tr class="separator:ga41cace31999105137772b6257ea540f9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga591f3aab5dd2c87e56e05423c2a671d9" class="memitem:ga591f3aab5dd2c87e56e05423c2a671d9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_append_args (DBusMessage *message, int first_arg_type,...)</td>
</tr>
<tr class="memdesc:ga591f3aab5dd2c87e56e05423c2a671d9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends fields to a message given a variable argument list.<br />
</td>
</tr>
<tr class="separator:ga591f3aab5dd2c87e56e05423c2a671d9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga106e541001d6b884d1c3cea6044693ab" class="memitem:ga106e541001d6b884d1c3cea6044693ab">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_append_args_valist (DBusMessage *message, int first_arg_type, va_list var_args)</td>
</tr>
<tr class="memdesc:ga106e541001d6b884d1c3cea6044693ab">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like dbus_message_append_args() but takes a va_list for use by language bindings.<br />
</td>
</tr>
<tr class="separator:ga106e541001d6b884d1c3cea6044693ab">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad8953f53ceea7de81cde792e3edd0230" class="memitem:gad8953f53ceea7de81cde792e3edd0230">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_args (DBusMessage *message, DBusError *error, int first_arg_type,...)</td>
</tr>
<tr class="memdesc:gad8953f53ceea7de81cde792e3edd0230">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets arguments from a message given a variable argument list.<br />
</td>
</tr>
<tr class="separator:gad8953f53ceea7de81cde792e3edd0230">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab0f9bbe4f3d26bc9b5cf4f243c268aaa" class="memitem:gab0f9bbe4f3d26bc9b5cf4f243c268aaa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_args_valist (DBusMessage *message, DBusError *error, int first_arg_type, va_list var_args)</td>
</tr>
<tr class="memdesc:gab0f9bbe4f3d26bc9b5cf4f243c268aaa">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like dbus_message_get_args but takes a va_list for use by language bindings.<br />
</td>
</tr>
<tr class="separator:gab0f9bbe4f3d26bc9b5cf4f243c268aaa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9f98b47c84f0e401ea985e681de4e963" class="memitem:ga9f98b47c84f0e401ea985e681de4e963">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_init (DBusMessage *message, DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:ga9f98b47c84f0e401ea985e681de4e963">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a DBusMessageIter for reading the arguments of the message passed in.<br />
</td>
</tr>
<tr class="separator:ga9f98b47c84f0e401ea985e681de4e963">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaaffc75a699c96ff6197287f166df2149" class="memitem:gaaffc75a699c96ff6197287f166df2149">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_has_next (DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:gaaffc75a699c96ff6197287f166df2149">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks if an iterator has any more fields.<br />
</td>
</tr>
<tr class="separator:gaaffc75a699c96ff6197287f166df2149">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga554e9fafd4dcc84cebe9da9344846a82" class="memitem:ga554e9fafd4dcc84cebe9da9344846a82">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_next (DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:ga554e9fafd4dcc84cebe9da9344846a82">
<td class="mdescLeft"> </td>
<td class="mdescRight">Moves the iterator to the next field, if any.<br />
</td>
</tr>
<tr class="separator:ga554e9fafd4dcc84cebe9da9344846a82">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5aae3c882a75aed953d8b3d489e9b271" class="memitem:ga5aae3c882a75aed953d8b3d489e9b271">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_get_arg_type (DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:ga5aae3c882a75aed953d8b3d489e9b271">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the argument type of the argument that the message iterator points to.<br />
</td>
</tr>
<tr class="separator:ga5aae3c882a75aed953d8b3d489e9b271">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga868a7aeddb9b54b2805776b512f68cb4" class="memitem:ga868a7aeddb9b54b2805776b512f68cb4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_get_element_type (DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:ga868a7aeddb9b54b2805776b512f68cb4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the element type of the array that the message iterator points to.<br />
</td>
</tr>
<tr class="separator:ga868a7aeddb9b54b2805776b512f68cb4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7652e1208743da5dd4ecc5aef07bf207" class="memitem:ga7652e1208743da5dd4ecc5aef07bf207">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_recurse (DBusMessageIter *iter, DBusMessageIter *sub)</td>
</tr>
<tr class="memdesc:ga7652e1208743da5dd4ecc5aef07bf207">
<td class="mdescLeft"> </td>
<td class="mdescRight">Recurses into a container value when reading values from a message, initializing a sub-iterator to use for traversing the child values of the container.<br />
</td>
</tr>
<tr class="separator:ga7652e1208743da5dd4ecc5aef07bf207">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab4579a88a1a7eaf648350466f585ef8b" class="memitem:gab4579a88a1a7eaf648350466f585ef8b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_get_signature (DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:gab4579a88a1a7eaf648350466f585ef8b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the current signature of a message iterator.<br />
</td>
</tr>
<tr class="separator:gab4579a88a1a7eaf648350466f585ef8b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga41c23a05e552d0574d0444d4693d18ab" class="memitem:ga41c23a05e552d0574d0444d4693d18ab">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_get_basic (DBusMessageIter *iter, void *value)</td>
</tr>
<tr class="memdesc:ga41c23a05e552d0574d0444d4693d18ab">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reads a basic-typed value from the message iterator.<br />
</td>
</tr>
<tr class="separator:ga41c23a05e552d0574d0444d4693d18ab">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabe60e5d5c3f06f90254eef3e72b5cf49" class="memitem:gabe60e5d5c3f06f90254eef3e72b5cf49">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_get_element_count (DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:gabe60e5d5c3f06f90254eef3e72b5cf49">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the number of elements in the array-typed value pointed to by the iterator.<br />
</td>
</tr>
<tr class="separator:gabe60e5d5c3f06f90254eef3e72b5cf49">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab8ff47649497b3e0b93a2289f5d3eb23" class="memitem:gab8ff47649497b3e0b93a2289f5d3eb23">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_get_array_len (DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:gab8ff47649497b3e0b93a2289f5d3eb23">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the number of bytes in the array as marshaled in the wire protocol.<br />
</td>
</tr>
<tr class="separator:gab8ff47649497b3e0b93a2289f5d3eb23">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae195a3312ae445e7ef0196854f3523f8" class="memitem:gae195a3312ae445e7ef0196854f3523f8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_get_fixed_array (DBusMessageIter *iter, void *value, int *n_elements)</td>
</tr>
<tr class="memdesc:gae195a3312ae445e7ef0196854f3523f8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reads a block of fixed-length values from the message iterator.<br />
</td>
</tr>
<tr class="separator:gae195a3312ae445e7ef0196854f3523f8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf733047c467ce21f4a53b65a388f1e9d" class="memitem:gaf733047c467ce21f4a53b65a388f1e9d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_init_append (DBusMessage *message, DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:gaf733047c467ce21f4a53b65a388f1e9d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a DBusMessageIter for appending arguments to the end of a message.<br />
</td>
</tr>
<tr class="separator:gaf733047c467ce21f4a53b65a388f1e9d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga17491f3b75b3203f6fc47dcc2e3b221b" class="memitem:ga17491f3b75b3203f6fc47dcc2e3b221b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_append_basic (DBusMessageIter *iter, int type, const void *value)</td>
</tr>
<tr class="memdesc:ga17491f3b75b3203f6fc47dcc2e3b221b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends a basic-typed value to the message.<br />
</td>
</tr>
<tr class="separator:ga17491f3b75b3203f6fc47dcc2e3b221b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6e2d1e936c3c61fe00d80a3f22fd5e76" class="memitem:ga6e2d1e936c3c61fe00d80a3f22fd5e76">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_append_fixed_array (DBusMessageIter *iter, int element_type, const void *value, int n_elements)</td>
</tr>
<tr class="memdesc:ga6e2d1e936c3c61fe00d80a3f22fd5e76">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends a block of fixed-length values to an array.<br />
</td>
</tr>
<tr class="separator:ga6e2d1e936c3c61fe00d80a3f22fd5e76">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga943150f4e87fd8507da224d22c266100" class="memitem:ga943150f4e87fd8507da224d22c266100">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_open_container (DBusMessageIter *iter, int type, const char *contained_signature, DBusMessageIter *sub)</td>
</tr>
<tr class="memdesc:ga943150f4e87fd8507da224d22c266100">
<td class="mdescLeft"> </td>
<td class="mdescRight">Appends a container-typed value to the message.<br />
</td>
</tr>
<tr class="separator:ga943150f4e87fd8507da224d22c266100">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf00482f63d4af88b7851621d1f24087a" class="memitem:gaf00482f63d4af88b7851621d1f24087a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_close_container (DBusMessageIter *iter, DBusMessageIter *sub)</td>
</tr>
<tr class="memdesc:gaf00482f63d4af88b7851621d1f24087a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Closes a container-typed value appended to the message; may write out more information to the message known only after the entire container is written, and may free resources created by dbus_message_iter_open_container().<br />
</td>
</tr>
<tr class="separator:gaf00482f63d4af88b7851621d1f24087a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6e62697ca11f0a57dbecc93d5721612c" class="memitem:ga6e62697ca11f0a57dbecc93d5721612c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_abandon_container (DBusMessageIter *iter, DBusMessageIter *sub)</td>
</tr>
<tr class="memdesc:ga6e62697ca11f0a57dbecc93d5721612c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Abandons creation of a contained-typed value and frees resources created by dbus_message_iter_open_container().<br />
</td>
</tr>
<tr class="separator:ga6e62697ca11f0a57dbecc93d5721612c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa30e15654e13111a48b66b01ae62aff3" class="memitem:gaa30e15654e13111a48b66b01ae62aff3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_abandon_container_if_open (DBusMessageIter *iter, DBusMessageIter *sub)</td>
</tr>
<tr class="memdesc:gaa30e15654e13111a48b66b01ae62aff3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Abandons creation of a contained-typed value and frees resources created by dbus_message_iter_open_container().<br />
</td>
</tr>
<tr class="separator:gaa30e15654e13111a48b66b01ae62aff3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0e86aeb2dc6831ccc9a21fcbf8cc16f7" class="memitem:ga0e86aeb2dc6831ccc9a21fcbf8cc16f7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_no_reply (DBusMessage *message, dbus_bool_t no_reply)</td>
</tr>
<tr class="memdesc:ga0e86aeb2dc6831ccc9a21fcbf8cc16f7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a flag indicating that the message does not want a reply; if this flag is set, the other end of the connection may (but is not required to) optimize by not sending method return or error replies.<br />
</td>
</tr>
<tr class="separator:ga0e86aeb2dc6831ccc9a21fcbf8cc16f7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga622d051a2e5f578814116a958b240aa4" class="memitem:ga622d051a2e5f578814116a958b240aa4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_no_reply (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga622d051a2e5f578814116a958b240aa4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns TRUE if the message does not expect a reply.<br />
</td>
</tr>
<tr class="separator:ga622d051a2e5f578814116a958b240aa4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1596d92a8d604f954b48c7410263d2f0" class="memitem:ga1596d92a8d604f954b48c7410263d2f0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_auto_start (DBusMessage *message, dbus_bool_t auto_start)</td>
</tr>
<tr class="memdesc:ga1596d92a8d604f954b48c7410263d2f0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a flag indicating that an owner for the destination name will be automatically started before the message is delivered.<br />
</td>
</tr>
<tr class="separator:ga1596d92a8d604f954b48c7410263d2f0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga85d396a3a774e15c3dbb7704aa173384" class="memitem:ga85d396a3a774e15c3dbb7704aa173384">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_auto_start (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga85d396a3a774e15c3dbb7704aa173384">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns TRUE if the message will cause an owner for destination name to be auto-started.<br />
</td>
</tr>
<tr class="separator:ga85d396a3a774e15c3dbb7704aa173384">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaaf25da0ba1482266293d329314c21786" class="memitem:gaaf25da0ba1482266293d329314c21786">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_path (DBusMessage *message, const char *object_path)</td>
</tr>
<tr class="memdesc:gaaf25da0ba1482266293d329314c21786">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or the one a signal is being emitted from (for DBUS_MESSAGE_TYPE_SIGNAL).<br />
</td>
</tr>
<tr class="separator:gaaf25da0ba1482266293d329314c21786">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga18adf731bb42d324fe2624407319e4af" class="memitem:ga18adf731bb42d324fe2624407319e4af">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_path (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga18adf731bb42d324fe2624407319e4af">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitted from (for DBUS_MESSAGE_TYPE_SIGNAL).<br />
</td>
</tr>
<tr class="separator:ga18adf731bb42d324fe2624407319e4af">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad2c87d3472bd3bfa8eca8a97f2db026b" class="memitem:gad2c87d3472bd3bfa8eca8a97f2db026b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_has_path (DBusMessage *message, const char *path)</td>
</tr>
<tr class="memdesc:gad2c87d3472bd3bfa8eca8a97f2db026b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks if the message has a particular object path.<br />
</td>
</tr>
<tr class="separator:gad2c87d3472bd3bfa8eca8a97f2db026b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf2b5b3319da838b1f1b360c04a33f153" class="memitem:gaf2b5b3319da838b1f1b360c04a33f153">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_path_decomposed (DBusMessage *message, char ***path)</td>
</tr>
<tr class="memdesc:gaf2b5b3319da838b1f1b360c04a33f153">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitted from (for DBUS_MESSAGE_TYPE_SIGNAL) in a decomposed format (one array element per path component).<br />
</td>
</tr>
<tr class="separator:gaf2b5b3319da838b1f1b360c04a33f153">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga02b754855e4d9a1cade8e4fc17a3f5c7" class="memitem:ga02b754855e4d9a1cade8e4fc17a3f5c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_interface (DBusMessage *message, const char *iface)</td>
</tr>
<tr class="memdesc:ga02b754855e4d9a1cade8e4fc17a3f5c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the interface this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or the interface a signal is being emitted from (for DBUS_MESSAGE_TYPE_SIGNAL).<br />
</td>
</tr>
<tr class="separator:ga02b754855e4d9a1cade8e4fc17a3f5c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1ad192bd4538cae556121a71b4e09d42" class="memitem:ga1ad192bd4538cae556121a71b4e09d42">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_interface (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga1ad192bd4538cae556121a71b4e09d42">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the interface this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitted from (for DBUS_MESSAGE_TYPE_SIGNAL).<br />
</td>
</tr>
<tr class="separator:ga1ad192bd4538cae556121a71b4e09d42">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0d1debd1c101a80c386d6ec92cdb1d93" class="memitem:ga0d1debd1c101a80c386d6ec92cdb1d93">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_has_interface (DBusMessage *message, const char *iface)</td>
</tr>
<tr class="memdesc:ga0d1debd1c101a80c386d6ec92cdb1d93">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks if the message has an interface.<br />
</td>
</tr>
<tr class="separator:ga0d1debd1c101a80c386d6ec92cdb1d93">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3afdda6016816cc70b451d8657065208" class="memitem:ga3afdda6016816cc70b451d8657065208">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_member (DBusMessage *message, const char *member)</td>
</tr>
<tr class="memdesc:ga3afdda6016816cc70b451d8657065208">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the interface member being invoked (DBUS_MESSAGE_TYPE_METHOD_CALL) or emitted (DBUS_MESSAGE_TYPE_SIGNAL).<br />
</td>
</tr>
<tr class="separator:ga3afdda6016816cc70b451d8657065208">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf5c6b705c53db07a5ae2c6b76f230cf9" class="memitem:gaf5c6b705c53db07a5ae2c6b76f230cf9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_member (DBusMessage *message)</td>
</tr>
<tr class="memdesc:gaf5c6b705c53db07a5ae2c6b76f230cf9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the interface member being invoked (DBUS_MESSAGE_TYPE_METHOD_CALL) or emitted (DBUS_MESSAGE_TYPE_SIGNAL).<br />
</td>
</tr>
<tr class="separator:gaf5c6b705c53db07a5ae2c6b76f230cf9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad7021a30bf930f8090bc38f862f19adb" class="memitem:gad7021a30bf930f8090bc38f862f19adb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_has_member (DBusMessage *message, const char *member)</td>
</tr>
<tr class="memdesc:gad7021a30bf930f8090bc38f862f19adb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks if the message has an interface member.<br />
</td>
</tr>
<tr class="separator:gad7021a30bf930f8090bc38f862f19adb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga892f9857707371c2a53cec6b54c843c7" class="memitem:ga892f9857707371c2a53cec6b54c843c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_error_name (DBusMessage *message, const char *error_name)</td>
</tr>
<tr class="memdesc:ga892f9857707371c2a53cec6b54c843c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the name of the error (DBUS_MESSAGE_TYPE_ERROR).<br />
</td>
</tr>
<tr class="separator:ga892f9857707371c2a53cec6b54c843c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4e98b2283707a8e0313fc7c6fe3b1b5f" class="memitem:ga4e98b2283707a8e0313fc7c6fe3b1b5f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_error_name (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga4e98b2283707a8e0313fc7c6fe3b1b5f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the error name (DBUS_MESSAGE_TYPE_ERROR only) or NULL if none.<br />
</td>
</tr>
<tr class="separator:ga4e98b2283707a8e0313fc7c6fe3b1b5f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacc47c1af23addfc4198b70084ba068fc" class="memitem:gacc47c1af23addfc4198b70084ba068fc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_destination (DBusMessage *message, const char *destination)</td>
</tr>
<tr class="memdesc:gacc47c1af23addfc4198b70084ba068fc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the message's destination.<br />
</td>
</tr>
<tr class="separator:gacc47c1af23addfc4198b70084ba068fc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaac65c926e6253e49aa689b4f032fad45" class="memitem:gaac65c926e6253e49aa689b4f032fad45">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_destination (DBusMessage *message)</td>
</tr>
<tr class="memdesc:gaac65c926e6253e49aa689b4f032fad45">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the destination of a message or NULL if there is none set.<br />
</td>
</tr>
<tr class="separator:gaac65c926e6253e49aa689b4f032fad45">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa2170744c2c19217d9df02551f16bc92" class="memitem:gaa2170744c2c19217d9df02551f16bc92">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_sender (DBusMessage *message, const char *sender)</td>
</tr>
<tr class="memdesc:gaa2170744c2c19217d9df02551f16bc92">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the message sender.<br />
</td>
</tr>
<tr class="separator:gaa2170744c2c19217d9df02551f16bc92">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga13ce514ceb2d1598751f3a7760cf1375" class="memitem:ga13ce514ceb2d1598751f3a7760cf1375">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_sender (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga13ce514ceb2d1598751f3a7760cf1375">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the unique name of the connection which originated this message, or NULL if unknown or inapplicable.<br />
</td>
</tr>
<tr class="separator:ga13ce514ceb2d1598751f3a7760cf1375">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaed63e4c2baaa50d782e8ebb7643def19" class="memitem:gaed63e4c2baaa50d782e8ebb7643def19">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_signature (DBusMessage *message)</td>
</tr>
<tr class="memdesc:gaed63e4c2baaa50d782e8ebb7643def19">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the type signature of the message, i.e.<br />
</td>
</tr>
<tr class="separator:gaed63e4c2baaa50d782e8ebb7643def19">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad8bd4730941af47d8d0f9c9b00562a44" class="memitem:gad8bd4730941af47d8d0f9c9b00562a44">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_is_method_call (DBusMessage *message, const char *iface, const char *method)</td>
</tr>
<tr class="memdesc:gad8bd4730941af47d8d0f9c9b00562a44">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the message is a method call with the given interface and member fields.<br />
</td>
</tr>
<tr class="separator:gad8bd4730941af47d8d0f9c9b00562a44">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaed0e32329f142cc246662227c81d5d1f" class="memitem:gaed0e32329f142cc246662227c81d5d1f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_is_signal (DBusMessage *message, const char *iface, const char *signal_name)</td>
</tr>
<tr class="memdesc:gaed0e32329f142cc246662227c81d5d1f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the message is a signal with the given interface and member fields.<br />
</td>
</tr>
<tr class="separator:gaed0e32329f142cc246662227c81d5d1f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga70ef9d7fad409666a0b5f3a8d4f0dd92" class="memitem:ga70ef9d7fad409666a0b5f3a8d4f0dd92">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_is_error (DBusMessage *message, const char *error_name)</td>
</tr>
<tr class="memdesc:ga70ef9d7fad409666a0b5f3a8d4f0dd92">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the message is an error reply with the given error name.<br />
</td>
</tr>
<tr class="separator:ga70ef9d7fad409666a0b5f3a8d4f0dd92">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga017cb8d960d4c360cb6b30ded5292509" class="memitem:ga017cb8d960d4c360cb6b30ded5292509">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_has_destination (DBusMessage *message, const char *name)</td>
</tr>
<tr class="memdesc:ga017cb8d960d4c360cb6b30ded5292509">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the message was sent to the given name.<br />
</td>
</tr>
<tr class="separator:ga017cb8d960d4c360cb6b30ded5292509">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga332fb0c71efcd1e9ef43ebdf2a25350c" class="memitem:ga332fb0c71efcd1e9ef43ebdf2a25350c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_has_sender (DBusMessage *message, const char *name)</td>
</tr>
<tr class="memdesc:ga332fb0c71efcd1e9ef43ebdf2a25350c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the message has the given unique name as its sender.<br />
</td>
</tr>
<tr class="separator:ga332fb0c71efcd1e9ef43ebdf2a25350c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8d563a936b6147f12dce7f24df3557b7" class="memitem:ga8d563a936b6147f12dce7f24df3557b7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_has_signature (DBusMessage *message, const char *signature)</td>
</tr>
<tr class="memdesc:ga8d563a936b6147f12dce7f24df3557b7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the message has the given signature; see dbus_message_get_signature() for more details on what the signature looks like.<br />
</td>
</tr>
<tr class="separator:ga8d563a936b6147f12dce7f24df3557b7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaba5e49e956e6bbd1f857ffd21c289276" class="memitem:gaba5e49e956e6bbd1f857ffd21c289276">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_set_error_from_message (DBusError *error, DBusMessage *message)</td>
</tr>
<tr class="memdesc:gaba5e49e956e6bbd1f857ffd21c289276">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a DBusError based on the contents of the given message.<br />
</td>
</tr>
<tr class="separator:gaba5e49e956e6bbd1f857ffd21c289276">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7436b74471eb3642f81fd456f8f2b69c" class="memitem:ga7436b74471eb3642f81fd456f8f2b69c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_contains_unix_fds (DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga7436b74471eb3642f81fd456f8f2b69c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether a message contains unix fds.<br />
</td>
</tr>
<tr class="separator:ga7436b74471eb3642f81fd456f8f2b69c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaee19f8494867ced1de067a5f25a4dd97" class="memitem:gaee19f8494867ced1de067a5f25a4dd97">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_container_instance (DBusMessage *message, const char *object_path)</td>
</tr>
<tr class="memdesc:gaee19f8494867ced1de067a5f25a4dd97">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the container instance this message was sent from.<br />
</td>
</tr>
<tr class="separator:gaee19f8494867ced1de067a5f25a4dd97">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafe70aec67e6da6590e502927b7299966" class="memitem:gafe70aec67e6da6590e502927b7299966">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_container_instance (DBusMessage *message)</td>
</tr>
<tr class="memdesc:gafe70aec67e6da6590e502927b7299966">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the container instance this message was sent from, or NULL if none.<br />
</td>
</tr>
<tr class="separator:gafe70aec67e6da6590e502927b7299966">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa35c17742d8fe091aa039cbd29961c52" class="memitem:gaa35c17742d8fe091aa039cbd29961c52">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_serial (DBusMessage *message, dbus_uint32_t serial)</td>
</tr>
<tr class="memdesc:gaa35c17742d8fe091aa039cbd29961c52">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the serial number of a message.<br />
</td>
</tr>
<tr class="separator:gaa35c17742d8fe091aa039cbd29961c52">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf2e47bea26730710340dbd22755c86e2" class="memitem:gaf2e47bea26730710340dbd22755c86e2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_iter_init_closed (DBusMessageIter *iter)</td>
</tr>
<tr class="memdesc:gaf2e47bea26730710340dbd22755c86e2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initialize iter as if with DBUS_MESSAGE_ITER_INIT_CLOSED.<br />
</td>
</tr>
<tr class="separator:gaf2e47bea26730710340dbd22755c86e2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad3d6b8ec4745ec19f57cae07621f3a47" class="memitem:gad3d6b8ec4745ec19f57cae07621f3a47">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_lock (DBusMessage *message)</td>
</tr>
<tr class="memdesc:gad3d6b8ec4745ec19f57cae07621f3a47">
<td class="mdescLeft"> </td>
<td class="mdescRight">Locks a message.<br />
</td>
</tr>
<tr class="separator:gad3d6b8ec4745ec19f57cae07621f3a47">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafdde8db1152649d37c9f7e316ca59e56" class="memitem:gafdde8db1152649d37c9f7e316ca59e56">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_allocate_data_slot (dbus_int32_t *slot_p)</td>
</tr>
<tr class="memdesc:gafdde8db1152649d37c9f7e316ca59e56">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocates an integer ID to be used for storing application-specific data on any DBusMessage.<br />
</td>
</tr>
<tr class="separator:gafdde8db1152649d37c9f7e316ca59e56">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga23227ce2bd5c52d05581d3fe1232ae66" class="memitem:ga23227ce2bd5c52d05581d3fe1232ae66">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_free_data_slot (dbus_int32_t *slot_p)</td>
</tr>
<tr class="memdesc:ga23227ce2bd5c52d05581d3fe1232ae66">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deallocates a global ID for message data slots.<br />
</td>
</tr>
<tr class="separator:ga23227ce2bd5c52d05581d3fe1232ae66">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga29331c4e9c2d53cbe60382056f6495a1" class="memitem:ga29331c4e9c2d53cbe60382056f6495a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_data (DBusMessage *message, dbus_int32_t slot, void *data, DBusFreeFunction free_data_func)</td>
</tr>
<tr class="memdesc:ga29331c4e9c2d53cbe60382056f6495a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Stores a pointer on a DBusMessage, along with an optional function to be used for freeing the data when the data is set again, or when the message is finalized.<br />
</td>
</tr>
<tr class="separator:ga29331c4e9c2d53cbe60382056f6495a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafb2fcbb95e1e274a28e893f5d17c0b61" class="memitem:gafb2fcbb95e1e274a28e893f5d17c0b61">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT void * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_data (DBusMessage *message, dbus_int32_t slot)</td>
</tr>
<tr class="memdesc:gafb2fcbb95e1e274a28e893f5d17c0b61">
<td class="mdescLeft"> </td>
<td class="mdescRight">Retrieves data previously set with dbus_message_set_data().<br />
</td>
</tr>
<tr class="separator:gafb2fcbb95e1e274a28e893f5d17c0b61">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabc69747028f1e5adedc68f5ffd538c74" class="memitem:gabc69747028f1e5adedc68f5ffd538c74">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">dbus_message_type_from_string (const char *type_str)</td>
</tr>
<tr class="memdesc:gabc69747028f1e5adedc68f5ffd538c74">
<td class="mdescLeft"> </td>
<td class="mdescRight">Utility function to convert a machine-readable (not translated) string into a D-Bus message type.<br />
</td>
</tr>
<tr class="separator:gabc69747028f1e5adedc68f5ffd538c74">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga30c3cf672781da89cf9714e5ba761033" class="memitem:ga30c3cf672781da89cf9714e5ba761033">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_type_to_string (int type)</td>
</tr>
<tr class="memdesc:ga30c3cf672781da89cf9714e5ba761033">
<td class="mdescLeft"> </td>
<td class="mdescRight">Utility function to convert a D-Bus message type into a machine-readable string (not translated).<br />
</td>
</tr>
<tr class="separator:ga30c3cf672781da89cf9714e5ba761033">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3f90a918ada328450fcfe9ac403b8807" class="memitem:ga3f90a918ada328450fcfe9ac403b8807">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_marshal (DBusMessage *msg, char **marshalled_data_p, int *len_p)</td>
</tr>
<tr class="memdesc:ga3f90a918ada328450fcfe9ac403b8807">
<td class="mdescLeft"> </td>
<td class="mdescRight">Turn a DBusMessage into the marshalled form as described in the D-Bus specification.<br />
</td>
</tr>
<tr class="separator:ga3f90a918ada328450fcfe9ac403b8807">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf16661bb2fdee8d3e468d1faa311067d" class="memitem:gaf16661bb2fdee8d3e468d1faa311067d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_message_demarshal (const char *str, int len, DBusError *error)</td>
</tr>
<tr class="memdesc:gaf16661bb2fdee8d3e468d1faa311067d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Demarshal a D-Bus message from the format described in the D-Bus specification.<br />
</td>
</tr>
<tr class="separator:gaf16661bb2fdee8d3e468d1faa311067d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga67b26fd2c8e3305f3a467a5f3e36b24a" class="memitem:ga67b26fd2c8e3305f3a467a5f3e36b24a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">dbus_message_demarshal_bytes_needed (const char *str, int len)</td>
</tr>
<tr class="memdesc:ga67b26fd2c8e3305f3a467a5f3e36b24a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the number of bytes required to be in the buffer to demarshal a D-Bus message.<br />
</td>
</tr>
<tr class="separator:ga67b26fd2c8e3305f3a467a5f3e36b24a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae734e7f4079375a0256d9e7f855ec4e4" class="memitem:gae734e7f4079375a0256d9e7f855ec4e4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">dbus_message_set_allow_interactive_authorization (DBusMessage *message, dbus_bool_t allow)</td>
</tr>
<tr class="memdesc:gae734e7f4079375a0256d9e7f855ec4e4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a flag indicating that the caller of the method is prepared to wait for interactive authorization to take place (for instance via Polkit) before the actual method is processed.<br />
</td>
</tr>
<tr class="separator:gae734e7f4079375a0256d9e7f855ec4e4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae9daa615b732c27d690399cc32e1f5b9" class="memitem:gae9daa615b732c27d690399cc32e1f5b9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_message_get_allow_interactive_authorization (DBusMessage *message)</td>
</tr>
<tr class="memdesc:gae9daa615b732c27d690399cc32e1f5b9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns whether the flag controlled by dbus_message_set_allow_interactive_authorization() has been set.<br />
</td>
</tr>
<tr class="separator:gae9daa615b732c27d690399cc32e1f5b9">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Message to be sent or received over a DBusConnection.

A DBusMessage is the most basic unit of communication over a DBusConnection. A DBusConnection represents a stream of messages received from a remote application, and a stream of messages sent to a remote application.

A message has a message type, returned from dbus_message_get_type(). This indicates whether the message is a method call, a reply to a method call, a signal, or an error reply.

A message has header fields such as the sender, destination, method or signal name, and so forth. DBusMessage has accessor functions for these, such as dbus_message_get_member().

Convenience functions dbus_message_is_method_call(), dbus_message_is_signal(), and dbus_message_is_error() check several header fields at once and are slightly more efficient than checking the header fields with individual accessor functions.

Finally, a message has arguments. The number and types of arguments are in the message's signature header field (accessed with dbus_message_get_signature()). Simple argument values are usually retrieved with dbus_message_get_args() but more complex values such as structs may require the use of DBusMessageIter.

The D-Bus specification goes into some more detail about header fields and message types.

## Macro Definition Documentation

## ◆ DBUS_MESSAGE_ITER_INIT_CLOSED

|                                        |
|----------------------------------------|
| \#define DBUS_MESSAGE_ITER_INIT_CLOSED |

**Value:**

{ \\

NULL, /\* dummy1 \*/ \\

NULL, /\* dummy2 \*/ \\

0, /\* dummy3 \*/ \\

0, /\* dummy4 \*/ \\

0, /\* dummy5 \*/ \\

0, /\* dummy6 \*/ \\

0, /\* dummy7 \*/ \\

0, /\* dummy8 \*/ \\

0, /\* dummy9 \*/ \\

0, /\* dummy10 \*/ \\

0, /\* dummy11 \*/ \\

0, /\* pad1 \*/ \\

NULL, /\* pad2 \*/ \\

NULL /\* pad3 \*/ \\

}

NULL

\#define NULL

A null pointer, defined appropriately for C or C++.

**Definition** dbus-macros.h:51

A message iterator for which dbus_message_iter_abandon_container_if_open() is the only valid operation.

Definition at line 100 of file dbus-message.h.

## Typedef Documentation

## ◆ DBusMessage

|             |
|-------------|
| DBusMessage |

Opaque data type representing a message received from or to be sent to another application.

Definition at line 46 of file dbus-message.h.

## ◆ DBusMessageIter

|                                                |
|------------------------------------------------|
| typedef struct DBusMessageIter DBusMessageIter |

Opaque type representing a message iterator.

Can be copied by value and allocated on the stack.

A DBusMessageIter usually contains no allocated memory. However, there is one special case: after a successful call to dbus_message_iter_open_container(), the caller is responsible for calling either dbus_message_iter_close_container() or dbus_message_iter_abandon_container() exactly once, with the same pair of iterators.

Definition at line 58 of file dbus-message.h.

## Function Documentation

## ◆ dbus_message_allocate_data_slot()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_allocate_data_slot | ( | dbus_int32_t \*  | *slot_p* | ) |  |

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

## ◆ dbus_message_append_args()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_append_args | ( | DBusMessage \*  | *message*, |
|  |  | int  | *first_arg_type*, |
|  |  |   | *...*  |
|  | ) |  |  |

Appends fields to a message given a variable argument list.

The variable argument list should contain the type of each argument followed by the value to append. Appendable types are basic types, and arrays of fixed-length basic types (except arrays of Unix file descriptors). To append variable-length basic types, or any more complex value, you have to use an iterator rather than this function.

To append a basic type, specify its type code followed by the address of the value. For example:

dbus_int32_t v_INT32 = 42;

const char \*v_STRING = "Hello World";

dbus_message_append_args (message,

DBUS_TYPE_INT32, &v_INT32,

DBUS_TYPE_STRING, &v_STRING,

DBUS_TYPE_INVALID);

dbus_message_append_args

dbus_bool_t dbus_message_append_args(DBusMessage \*message, int first_arg_type,...)

Appends fields to a message given a variable argument list.

**Definition** dbus-message.c:1843

DBUS_TYPE_INT32

\#define DBUS_TYPE_INT32

Type code marking a 32-bit signed integer.

**Definition** dbus-protocol.h:84

DBUS_TYPE_STRING

\#define DBUS_TYPE_STRING

Type code marking a UTF-8 encoded, nul-terminated Unicode string.

**Definition** dbus-protocol.h:104

DBUS_TYPE_INVALID

\#define DBUS_TYPE_INVALID

Type code that is never equal to a legitimate type code.

**Definition** dbus-protocol.h:62

To append an array of fixed-length basic types (except Unix file descriptors), pass in the DBUS_TYPE_ARRAY typecode, the element typecode, the address of the array pointer, and a 32-bit integer giving the number of elements in the array. So for example:

const dbus_int32_t array\[\] = { 1, 2, 3 };

const dbus_int32_t \*v_ARRAY = array;

dbus_message_append_args (message,

DBUS_TYPE_ARRAY, DBUS_TYPE_INT32, &v_ARRAY, 3,

DBUS_TYPE_INVALID);

DBUS_TYPE_ARRAY

\#define DBUS_TYPE_ARRAY

Type code marking a D-Bus array type.

**Definition** dbus-protocol.h:122

This function does not support arrays of Unix file descriptors. If you need those you need to manually recurse into the array.

For Unix file descriptors this function will internally duplicate the descriptor you passed in. Hence you may close the descriptor immediately after this call.

Warning  
in C, given "int array\[\]", "&array == array" (the comp.lang.c FAQ says otherwise, but gcc and the FAQ don't agree). So if you're using an array instead of a pointer you have to create a pointer variable, assign the array to it, then take the address of the pointer variable. For strings it works to write const char \*array = "Hello" and then use &array though.

The last argument to this function must be DBUS_TYPE_INVALID, marking the end of the argument list. If you don't do this then libdbus won't know to stop and will read invalid memory.

String/signature/path arrays should be passed in as "const char\*\*\* address_of_array" and "int n_elements"

Parameters  
|  |  |
|----|----|
| message | the message |
| first_arg_type | type of the first argument |
| ... | value of first argument, list of additional type-value pairs |

<!-- -->

Returns  
TRUE on success

Definition at line 1843 of file dbus-message.c.

References dbus_message_append_args_valist(), FALSE, and NULL.

Referenced by dbus_bus_add_match(), dbus_bus_get_unix_user(), dbus_bus_name_has_owner(), dbus_bus_release_name(), dbus_bus_remove_match(), dbus_bus_request_name(), and dbus_bus_start_service_by_name().

## ◆ dbus_message_append_args_valist()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_append_args_valist | ( | DBusMessage \*  | *message*, |
|  |  | int  | *first_arg_type*, |
|  |  | va_list  | *var_args*  |
|  | ) |  |  |

Like dbus_message_append_args() but takes a va_list for use by language bindings.

See also  
dbus_message_append_args.

<!-- -->

Parameters  
|                |                                                        |
|----------------|--------------------------------------------------------|
| message        | the message                                            |
| first_arg_type | type of first argument                                 |
| var_args       | value of first argument, then list of type/value pairs |

<!-- -->

Returns  
TRUE on success

Definition at line 1875 of file dbus-message.c.

References \_dbus_type_to_string(), \_dbus_warn(), dbus_message_iter_abandon_container(), dbus_message_iter_append_basic(), dbus_message_iter_append_fixed_array(), dbus_message_iter_close_container(), dbus_message_iter_init_append(), dbus_message_iter_open_container(), DBUS_TYPE_ARRAY, DBUS_TYPE_INVALID, dbus_type_is_basic(), dbus_type_is_fixed(), DBUS_TYPE_UNIX_FD, FALSE, NULL, and TRUE.

Referenced by dbus_message_append_args().

## ◆ dbus_message_contains_unix_fds()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_contains_unix_fds | ( | DBusMessage \*  | *message* | ) |  |

Checks whether a message contains unix fds.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
TRUE if the message contains unix fds

Definition at line 4088 of file dbus-message.c.

References \_dbus_assert, and FALSE.

## ◆ dbus_message_copy()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_message_copy | ( | const DBusMessage \*  | *message* | ) |  |

Creates a new message that is an exact replica of the message specified, except that its refcount is set to 1, its message serial is reset to 0, and if the original message was "locked" (in the outgoing message queue and thus not modifiable) the new message will not be locked.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the new message.or NULL if not enough memory or Unix file descriptors (in case the message to copy includes Unix file descriptors) can be allocated.

Definition at line 1632 of file dbus-message.c.

References \_dbus_atomic_inc(), \_dbus_dup(), \_dbus_header_copy(), \_dbus_header_free(), \_dbus_string_copy(), \_dbus_string_free(), \_dbus_string_get_length(), \_dbus_string_init_preallocated(), body, dbus_free(), dbus_new, dbus_new0, FALSE, generation, header, locked, NULL, and refcount.

## ◆ dbus_message_demarshal()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_message_demarshal | ( | const char \*  | *str*, |
|  |  | int  | *len*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

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

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT int dbus_message_demarshal_bytes_needed | ( | const char \*  | *buf*, |
|  |  | int  | *len*  |
|  | ) |  |  |

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

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_message_free_data_slot | ( | dbus_int32_t \*  | *slot_p* | ) |  |

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
| DBUS_EXPORT dbus_bool_t dbus_message_get_allow_interactive_authorization | ( | DBusMessage \*  | *message* | ) |  |

Returns whether the flag controlled by dbus_message_set_allow_interactive_authorization() has been set.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

Definition at line 5318 of file dbus-message.c.

References \_dbus_header_get_flag(), DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION, FALSE, header, and NULL.

## ◆ dbus_message_get_args()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_get_args | ( | DBusMessage \*  | *message*, |
|  |  | DBusError \*  | *error*, |
|  |  | int  | *first_arg_type*, |
|  |  |   | *...*  |
|  | ) |  |  |

Gets arguments from a message given a variable argument list.

The supported types include those supported by dbus_message_append_args(); that is, basic types and arrays of fixed-length basic types. The arguments are the same as they would be for dbus_message_iter_get_basic() or dbus_message_iter_get_fixed_array().

In addition to those types, arrays of string, object path, and signature are supported; but these are returned as allocated memory and must be freed with dbus_free_string_array(), while the other types are returned as const references. To get a string array pass in "char \*\*\*array_location" and "int \*n_elements".

Similar to dbus_message_get_fixed_array() this function does not support arrays of type DBUS_TYPE_UNIX_FD. If you need to parse messages with arrays of Unix file descriptors you need to recurse into the array manually.

Unix file descriptors that are read with this function will have the FD_CLOEXEC flag set. If you need them without this flag set, make sure to unset it with fcntl().

The variable argument list should contain the type of the argument followed by a pointer to where the value should be stored. The list is terminated with DBUS_TYPE_INVALID.

Except for string arrays, the returned values are constant; do not free them. They point into the DBusMessage.

If the requested arguments are not present, or do not have the requested types, then an error will be set.

If more arguments than requested are present, the requested arguments are returned and the extra arguments are ignored.

Parameters  
|  |  |
|----|----|
| message | the message |
| error | error to be filled in on failure |
| first_arg_type | the first argument type |
| ... | location for first argument value, then list of type-location pairs |

<!-- -->

Returns  
FALSE if the error was set

Definition at line 2032 of file dbus-message.c.

References dbus_message_get_args_valist(), FALSE, and NULL.

Referenced by dbus_bus_get_id(), dbus_bus_get_unix_user(), dbus_bus_name_has_owner(), dbus_bus_register(), dbus_bus_release_name(), dbus_bus_request_name(), dbus_bus_start_service_by_name(), and dbus_set_error_from_message().

## ◆ dbus_message_get_args_valist()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_get_args_valist | ( | DBusMessage \*  | *message*, |
|  |  | DBusError \*  | *error*, |
|  |  | int  | *first_arg_type*, |
|  |  | va_list  | *var_args*  |
|  | ) |  |  |

Like dbus_message_get_args but takes a va_list for use by language bindings.

See also  
dbus_message_get_args

<!-- -->

Parameters  
|  |  |
|----|----|
| message | the message |
| error | error to be filled in |
| first_arg_type | type of the first argument |
| var_args | return location for first argument, followed by list of type/location pairs |

<!-- -->

Returns  
FALSE if error was set

Definition at line 2061 of file dbus-message.c.

References \_dbus_message_iter_get_args_valist(), dbus_message_iter_init(), FALSE, and NULL.

Referenced by dbus_message_get_args().

## ◆ dbus_message_get_auto_start()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_get_auto_start | ( | DBusMessage \*  | *message* | ) |  |

Returns TRUE if the message will cause an owner for destination name to be auto-started.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
TRUE if the message will use auto-start

Definition at line 3308 of file dbus-message.c.

References \_dbus_header_get_flag(), DBUS_HEADER_FLAG_NO_AUTO_START, FALSE, header, and NULL.

## ◆ dbus_message_get_container_instance()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT const char \* dbus_message_get_container_instance | ( | DBusMessage \*  | *message* | ) |  |

Gets the container instance this message was sent from, or NULL if none.

The returned string becomes invalid if the message is modified, since it points into the wire-marshaled message data.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the path (should not be freed) or NULL

Definition at line 4136 of file dbus-message.c.

References \_dbus_header_get_field_basic(), DBUS_HEADER_FIELD_CONTAINER_INSTANCE, DBUS_TYPE_OBJECT_PATH, header, and NULL.

## ◆ dbus_message_get_data()

|                                           |     |                 |            |
|-------------------------------------------|-----|-----------------|------------|
| DBUS_EXPORT void \* dbus_message_get_data | (   | DBusMessage \*  | *message*, |
|                                           |     | dbus_int32_t    | *slot*     |
|                                           | )   |                 |            |

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

References \_dbus_data_slot_list_get(), NULL, and slot_list.

## ◆ dbus_message_get_destination()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT const char \* dbus_message_get_destination | ( | DBusMessage \*  | *message* | ) |  |

Gets the destination of a message or NULL if there is none set.

The returned string becomes invalid if the message is modified, since it points into the wire-marshaled message data.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the message destination (should not be freed) or NULL

Definition at line 3713 of file dbus-message.c.

References \_dbus_header_get_field_basic(), DBUS_HEADER_FIELD_DESTINATION, DBUS_TYPE_STRING, header, and NULL.

Referenced by dbus_message_has_destination().

## ◆ dbus_message_get_error_name()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT const char \* dbus_message_get_error_name | ( | DBusMessage \*  | *message* | ) |  |

Gets the error name (DBUS_MESSAGE_TYPE_ERROR only) or NULL if none.

The returned string becomes invalid if the message is modified, since it points into the wire-marshaled message data.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the error name (should not be freed) or NULL

Definition at line 3660 of file dbus-message.c.

References \_dbus_header_get_field_basic(), DBUS_HEADER_FIELD_ERROR_NAME, DBUS_TYPE_STRING, header, and NULL.

Referenced by dbus_message_is_error(), and dbus_set_error_from_message().

## ◆ dbus_message_get_interface()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT const char \* dbus_message_get_interface | ( | DBusMessage \*  | *message* | ) |  |

Gets the interface this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitted from (for DBUS_MESSAGE_TYPE_SIGNAL).

The interface name is fully-qualified (namespaced). Returns NULL if none.

The returned string becomes invalid if the message is modified, since it points into the wire-marshaled message data.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the message interface (should not be freed) or NULL

Definition at line 3490 of file dbus-message.c.

References \_dbus_header_get_field_basic(), DBUS_HEADER_FIELD_INTERFACE, DBUS_TYPE_STRING, header, and NULL.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_connection_queue_received_message_link(), dbus_connection_dispatch(), dbus_connection_send_preallocated(), and dbus_message_has_interface().

## ◆ dbus_message_get_member()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT const char \* dbus_message_get_member | ( | DBusMessage \*  | *message* | ) |  |

Gets the interface member being invoked (DBUS_MESSAGE_TYPE_METHOD_CALL) or emitted (DBUS_MESSAGE_TYPE_SIGNAL).

Returns NULL if none.

The returned string becomes invalid if the message is modified, since it points into the wire-marshaled message data.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the member name (should not be freed) or NULL

Definition at line 3576 of file dbus-message.c.

References \_dbus_header_get_field_basic(), DBUS_HEADER_FIELD_MEMBER, DBUS_TYPE_STRING, header, and NULL.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_connection_queue_received_message_link(), dbus_connection_dispatch(), dbus_connection_send_preallocated(), and dbus_message_has_member().

## ◆ dbus_message_get_no_reply()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_get_no_reply | ( | DBusMessage \*  | *message* | ) |  |

Returns TRUE if the message does not expect a reply.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
TRUE if the message sender isn't waiting for a reply

Definition at line 3266 of file dbus-message.c.

References \_dbus_header_get_flag(), DBUS_HEADER_FLAG_NO_REPLY_EXPECTED, FALSE, header, and NULL.

## ◆ dbus_message_get_path()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT const char \* dbus_message_get_path | ( | DBusMessage \*  | *message* | ) |  |

Gets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitted from (for DBUS_MESSAGE_TYPE_SIGNAL).

Returns NULL if none.

See also dbus_message_get_path_decomposed().

The returned string becomes invalid if the message is modified, since it points into the wire-marshaled message data.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the path (should not be freed) or NULL

Definition at line 3359 of file dbus-message.c.

References \_dbus_header_get_field_basic(), DBUS_HEADER_FIELD_PATH, DBUS_TYPE_OBJECT_PATH, header, and NULL.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_connection_queue_received_message_link(), dbus_message_get_path_decomposed(), and dbus_message_has_path().

## ◆ dbus_message_get_path_decomposed()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_get_path_decomposed | ( | DBusMessage \*  | *message*, |
|  |  | char \*\*\*  | *path*  |
|  | ) |  |  |

Gets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or being emitted from (for DBUS_MESSAGE_TYPE_SIGNAL) in a decomposed format (one array element per path component).

Free the returned array with dbus_free_string_array().

An empty but non-NULL path array means the path "/". So the path "/foo/bar" becomes { "foo", "bar", NULL } and the path "/" becomes { NULL }.

See also dbus_message_get_path().

Parameters  
|  |  |
|----|----|
| message | the message |
| path | place to store allocated array of path components; NULL set here if no path field exists |

<!-- -->

Returns  
FALSE if no memory to allocate the array

Definition at line 3427 of file dbus-message.c.

References \_dbus_decompose_path(), dbus_message_get_path(), FALSE, NULL, and TRUE.

Referenced by \_dbus_object_tree_dispatch_and_unlock().

## ◆ dbus_message_get_reply_serial()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_uint32_t dbus_message_get_reply_serial | ( | DBusMessage \*  | *message* | ) |  |

Returns the serial that the message is a reply to or 0 if none.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the reply serial

Definition at line 1208 of file dbus-message.c.

References \_dbus_header_get_field_basic(), DBUS_HEADER_FIELD_REPLY_SERIAL, DBUS_TYPE_UINT32, header, and NULL.

Referenced by \_dbus_connection_queue_received_message_link(), \_dbus_pending_call_set_reply_unlocked(), and dbus_connection_dispatch().

## ◆ dbus_message_get_sender()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT const char \* dbus_message_get_sender | ( | DBusMessage \*  | *message* | ) |  |

Gets the unique name of the connection which originated this message, or NULL if unknown or inapplicable.

The sender is filled in by the message bus.

Note, the returned sender is always the unique bus name. Connections may own multiple other bus names, but those are not found in the sender field.

The returned string becomes invalid if the message is modified, since it points into the wire-marshaled message data.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the unique name of the sender or NULL

Definition at line 3773 of file dbus-message.c.

References \_dbus_header_get_field_basic(), DBUS_HEADER_FIELD_SENDER, DBUS_TYPE_STRING, header, and NULL.

Referenced by dbus_message_has_sender(), dbus_message_new_error(), and dbus_message_new_method_return().

## ◆ dbus_message_get_serial()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_uint32_t dbus_message_get_serial | ( | DBusMessage \*  | *message* | ) |  |

Returns the serial of a message or 0 if none has been specified.

The message's serial number is provided by the application sending the message and is used to identify replies to this message.

All messages received on a connection will have a serial provided by the remote application.

For messages you're sending, dbus_connection_send() will assign a serial and return it to you.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the serial

Definition at line 1168 of file dbus-message.c.

References \_dbus_header_get_serial(), header, and NULL.

Referenced by dbus_connection_send_with_reply(), dbus_message_new_error(), and dbus_message_new_method_return().

## ◆ dbus_message_get_signature()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT const char \* dbus_message_get_signature | ( | DBusMessage \*  | *message* | ) |  |

Gets the type signature of the message, i.e.

the arguments in the message payload. The signature includes only "in" arguments for DBUS_MESSAGE_TYPE_METHOD_CALL and only "out" arguments for DBUS_MESSAGE_TYPE_METHOD_RETURN, so is slightly different from what you might expect (that is, it does not include the signature of the entire C++-style method).

The signature is a string made up of type codes such as DBUS_TYPE_INT32. The string is terminated with nul (nul is also the value of DBUS_TYPE_INVALID).

The returned string becomes invalid if the message is modified, since it points into the wire-marshaled message data.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the type signature

Definition at line 3806 of file dbus-message.c.

References \_dbus_string_get_const_data_len(), header, and NULL.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_connection_queue_received_message_link(), dbus_connection_dispatch(), dbus_message_has_signature(), and dbus_message_lock().

## ◆ dbus_message_get_type()

|                                       |     |                 |           |     |     |
|---------------------------------------|-----|-----------------|-----------|-----|-----|
| DBUS_EXPORT int dbus_message_get_type | (   | DBusMessage \*  | *message* | )   |     |

Gets the type of a message.

Types include DBUS_MESSAGE_TYPE_METHOD_CALL, DBUS_MESSAGE_TYPE_METHOD_RETURN, DBUS_MESSAGE_TYPE_ERROR, DBUS_MESSAGE_TYPE_SIGNAL, but other types are allowed and all code must silently ignore messages of unknown type. DBUS_MESSAGE_TYPE_INVALID will never be returned.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the type of the message

Definition at line 1767 of file dbus-message.c.

References \_dbus_header_get_message_type(), DBUS_MESSAGE_TYPE_INVALID, header, and NULL.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_connection_queue_received_message_link(), \_dbus_pending_call_set_reply_unlocked(), dbus_connection_dispatch(), dbus_connection_send_preallocated(), dbus_message_is_error(), and dbus_set_error_from_message().

## ◆ dbus_message_has_destination()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_has_destination | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *name*  |
|  | ) |  |  |

Checks whether the message was sent to the given name.

If the message has no destination specified or has a different destination, returns FALSE.

Parameters  
|         |                                      |
|---------|--------------------------------------|
| message | the message                          |
| name    | the name to check (must not be NULL) |

<!-- -->

Returns  
TRUE if the message has the given destination name

Definition at line 3953 of file dbus-message.c.

References dbus_message_get_destination(), FALSE, NULL, and TRUE.

## ◆ dbus_message_has_interface()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_has_interface | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *iface*  |
|  | ) |  |  |

Checks if the message has an interface.

Parameters  
|         |                    |
|---------|--------------------|
| message | the message        |
| iface   | the interface name |

<!-- -->

Returns  
TRUE if the interface field in the header matches

Definition at line 3512 of file dbus-message.c.

References dbus_message_get_interface(), FALSE, NULL, and TRUE.

## ◆ dbus_message_has_member()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_has_member | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *member*  |
|  | ) |  |  |

Checks if the message has an interface member.

Parameters  
|         |                 |
|---------|-----------------|
| message | the message     |
| member  | the member name |

<!-- -->

Returns  
TRUE if there is a member field in the header

Definition at line 3598 of file dbus-message.c.

References dbus_message_get_member(), FALSE, NULL, and TRUE.

## ◆ dbus_message_has_path()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_has_path | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *path*  |
|  | ) |  |  |

Checks if the message has a particular object path.

The object path is the destination object for a method call or the emitting object for a signal.

Parameters  
|         |               |
|---------|---------------|
| message | the message   |
| path    | the path name |

<!-- -->

Returns  
TRUE if there is a path field in the header

Definition at line 3383 of file dbus-message.c.

References dbus_message_get_path(), FALSE, NULL, and TRUE.

## ◆ dbus_message_has_sender()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_has_sender | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *name*  |
|  | ) |  |  |

Checks whether the message has the given unique name as its sender.

If the message has no sender specified or has a different sender, returns FALSE. Note that a peer application will always have the unique name of the connection as the sender. So you can't use this function to see whether a sender owned a well-known name.

Messages from the bus itself will have DBUS_SERVICE_DBUS as the sender.

Parameters  
|         |                                      |
|---------|--------------------------------------|
| message | the message                          |
| name    | the name to check (must not be NULL) |

<!-- -->

Returns  
TRUE if the message has the given sender

Definition at line 3988 of file dbus-message.c.

References dbus_message_get_sender(), FALSE, NULL, and TRUE.

## ◆ dbus_message_has_signature()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_has_signature | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *signature*  |
|  | ) |  |  |

Checks whether the message has the given signature; see dbus_message_get_signature() for more details on what the signature looks like.

Parameters  
|           |                |
|-----------|----------------|
| message   | the message    |
| signature | typecode array |

<!-- -->

Returns  
TRUE if message has the given signature

Definition at line 4017 of file dbus-message.c.

References dbus_message_get_signature(), FALSE, NULL, and TRUE.

## ◆ dbus_message_is_error()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_is_error | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *error_name*  |
|  | ) |  |  |

Checks whether the message is an error reply with the given error name.

If the message is not DBUS_MESSAGE_TYPE_ERROR, or has a different name, returns FALSE.

Parameters  
|            |                                      |
|------------|--------------------------------------|
| message    | the message                          |
| error_name | the name to check (must not be NULL) |

<!-- -->

Returns  
TRUE if the message is the specified error

Definition at line 3920 of file dbus-message.c.

References dbus_message_get_error_name(), dbus_message_get_type(), DBUS_MESSAGE_TYPE_ERROR, FALSE, NULL, and TRUE.

## ◆ dbus_message_is_method_call()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_is_method_call | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *iface*, |
|  |  | const char \*  | *method*  |
|  | ) |  |  |

Checks whether the message is a method call with the given interface and member fields.

If the message is not DBUS_MESSAGE_TYPE_METHOD_CALL, or has a different interface or member field, returns FALSE. If the interface field is missing, then it will be assumed equal to the provided interface. The D-Bus protocol allows method callers to leave out the interface name.

Parameters  
|         |                                      |
|---------|--------------------------------------|
| message | the message                          |
| iface   | the name to check (must not be NULL) |
| method  | the name to check (must not be NULL) |

<!-- -->

Returns  
TRUE if the message is the specified method call

Definition at line 3865 of file dbus-message.c.

References DBUS_MESSAGE_TYPE_METHOD_CALL, FALSE, and NULL.

## ◆ dbus_message_is_signal()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_is_signal | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *iface*, |
|  |  | const char \*  | *signal_name*  |
|  | ) |  |  |

Checks whether the message is a signal with the given interface and member fields.

If the message is not DBUS_MESSAGE_TYPE_SIGNAL, or has a different interface or member field, returns FALSE.

Parameters  
|             |                                      |
|-------------|--------------------------------------|
| message     | the message                          |
| iface       | the name to check (must not be NULL) |
| signal_name | the name to check (must not be NULL) |

<!-- -->

Returns  
TRUE if the message is the specified signal

Definition at line 3893 of file dbus-message.c.

References DBUS_MESSAGE_TYPE_SIGNAL, FALSE, and NULL.

## ◆ dbus_message_iter_abandon_container()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_message_iter_abandon_container | ( | DBusMessageIter \*  | *iter*, |
|  |  | DBusMessageIter \*  | *sub*  |
|  | ) |  |  |

Abandons creation of a contained-typed value and frees resources created by dbus_message_iter_open_container().

Once this returns, the message is hosed and you have to start over building the whole message.

This should only be used to abandon creation of a message when you have open containers.

Parameters  
|      |                       |
|------|-----------------------|
| iter | the append iterator   |
| sub  | sub-iterator to close |

Definition at line 3123 of file dbus-message.c.

References DBusMessageRealIter::iter_type.

Referenced by dbus_message_append_args_valist().

## ◆ dbus_message_iter_abandon_container_if_open()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_message_iter_abandon_container_if_open | ( | DBusMessageIter \*  | *iter*, |
|  |  | DBusMessageIter \*  | *sub*  |
|  | ) |  |  |

Abandons creation of a contained-typed value and frees resources created by dbus_message_iter_open_container().

Once this returns, the message is hosed and you have to start over building the whole message.

Unlike dbus_message_iter_abandon_container(), it is valid to call this function on an iterator that was initialized with DBUS_MESSAGE_ITER_INIT_CLOSED, or an iterator that was already closed or abandoned. However, it is not valid to call this function on uninitialized memory. This is intended to be used in error cleanup code paths, similar to this pattern:

``` fragment
  DBusMessageIter outer = DBUS_MESSAGE_ITER_INIT_CLOSED;
  DBusMessageIter inner = DBUS_MESSAGE_ITER_INIT_CLOSED;
  dbus_bool_t result = FALSE;

  if (!dbus_message_iter_open_container (iter, ..., &outer))
    goto out;

  if (!dbus_message_iter_open_container (&outer, ..., &inner))
    goto out;

  if (!dbus_message_iter_append_basic (&inner, ...))
    goto out;

  if (!dbus_message_iter_close_container (&outer, ..., &inner))
    goto out;

  if (!dbus_message_iter_close_container (iter, ..., &outer))
    goto out;

  result = TRUE;

out:
  dbus_message_iter_abandon_container_if_open (&outer, &inner);
  dbus_message_iter_abandon_container_if_open (iter, &outer);
  return result;
```

Parameters  
|      |                       |
|------|-----------------------|
| iter | the append iterator   |
| sub  | sub-iterator to close |

Definition at line 3182 of file dbus-message.c.

References DBusMessageRealIter::iter_type.

## ◆ dbus_message_iter_append_basic()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_iter_append_basic | ( | DBusMessageIter \*  | *iter*, |
|  |  | int  | *type*, |
|  |  | const void \*  | *value*  |
|  | ) |  |  |

Appends a basic-typed value to the message.

The basic types are the non-container types such as integer and string.

The "value" argument should be the address of a basic-typed value. So for string, const char\*\*. For integer, dbus_int32_t\*.

For Unix file descriptors this function will internally duplicate the descriptor you passed in. Hence you may close the descriptor immediately after this call.

Parameters  
|       |                          |
|-------|--------------------------|
| iter  | the append iterator      |
| type  | the type of the value    |
| value | the address of the value |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 2771 of file dbus-message.c.

References \_dbus_close(), \_dbus_dup(), \_dbus_header_set_field_basic(), \_dbus_string_get_length(), \_dbus_string_init_const(), \_dbus_type_writer_write_basic(), \_dbus_validate_signature_with_reason(), DBUS_HEADER_FIELD_UNIX_FDS, DBUS_TYPE_BOOLEAN, dbus_type_is_basic(), DBUS_TYPE_OBJECT_PATH, DBUS_TYPE_SIGNATURE, DBUS_TYPE_STRING, DBUS_TYPE_UINT32, DBUS_TYPE_UNIX_FD, DBUS_VALID, DBUS_VALIDITY_UNKNOWN_OOM_ERROR, FALSE, header, DBusMessageRealIter::iter_type, DBusMessageRealIter::message, NULL, DBusMessageRealIter::u, and DBusMessageRealIter::writer.

Referenced by dbus_message_append_args_valist(), and dbus_message_new_error().

## ◆ dbus_message_iter_append_fixed_array()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_iter_append_fixed_array | ( | DBusMessageIter \*  | *iter*, |
|  |  | int  | *element_type*, |
|  |  | const void \*  | *value*, |
|  |  | int  | *n_elements*  |
|  | ) |  |  |

Appends a block of fixed-length values to an array.

The fixed-length types are all basic types that are not string-like. So int32, double, bool, etc. (Unix file descriptors however are not supported.) You must call dbus_message_iter_open_container() to open an array of values before calling this function. You may call this function multiple times (and intermixed with calls to dbus_message_iter_append_basic()) for the same array.

The "value" argument should be the address of the array. So for integer, "dbus_int32_t\*\*" is expected for example.

Warning  
in C, given "int array\[\]", "&array == array" (the comp.lang.c FAQ says otherwise, but gcc and the FAQ don't agree). So if you're using an array instead of a pointer you have to create a pointer variable, assign the array to it, then take the address of the pointer variable.

const dbus_int32_t array\[\] = { 1, 2, 3 };

const dbus_int32_t \*v_ARRAY = array;

if (!dbus_message_iter_append_fixed_array (&iter, DBUS_TYPE_INT32, &v_ARRAY, 3))

fprintf (stderr, "No memory!\n");

dbus_message_iter_append_fixed_array

dbus_bool_t dbus_message_iter_append_fixed_array(DBusMessageIter \*iter, int element_type, const void \*value, int n_elements)

Appends a block of fixed-length values to an array.

**Definition** dbus-message.c:2922

For strings it works to write const char \*array = "Hello" and then use &array though.

<!-- -->

Parameters  
|              |                                  |
|--------------|----------------------------------|
| iter         | the append iterator              |
| element_type | the type of the array elements   |
| value        | the address of the array         |
| n_elements   | the number of elements to append |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 2922 of file dbus-message.c.

References \_dbus_type_get_alignment(), \_dbus_type_writer_write_fixed_multi(), DBusTypeWriter::container_type, DBUS_MAXIMUM_ARRAY_LENGTH, DBUS_TYPE_ARRAY, DBUS_TYPE_BOOLEAN, dbus_type_is_fixed(), DBUS_TYPE_UNIX_FD, FALSE, DBusMessageRealIter::iter_type, NULL, DBusMessageRealIter::u, and DBusMessageRealIter::writer.

Referenced by dbus_message_append_args_valist().

## ◆ dbus_message_iter_close_container()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_iter_close_container | ( | DBusMessageIter \*  | *iter*, |
|  |  | DBusMessageIter \*  | *sub*  |
|  | ) |  |  |

Closes a container-typed value appended to the message; may write out more information to the message known only after the entire container is written, and may free resources created by dbus_message_iter_open_container().

Even if this function fails due to lack of memory, the sub-iterator sub has been closed and invalidated. It must not be closed again with this function, or abandoned with dbus_message_iter_abandon_container(). However, it remains valid to call dbus_message_iter_abandon_container_if_open().

Parameters  
|      |                       |
|------|-----------------------|
| iter | the append iterator   |
| sub  | sub-iterator to close |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 3089 of file dbus-message.c.

References \_dbus_type_writer_unrecurse(), FALSE, DBusMessageRealIter::iter_type, DBusMessageRealIter::u, and DBusMessageRealIter::writer.

Referenced by dbus_message_append_args_valist().

## ◆ dbus_message_iter_get_arg_type()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT int dbus_message_iter_get_arg_type | ( | DBusMessageIter \*  | *iter* | ) |  |

Returns the argument type of the argument that the message iterator points to.

If the iterator is at the end of the message, returns DBUS_TYPE_INVALID. You can thus write a loop as follows:

dbus_message_iter_init (message, &iter);

while ((current_type = dbus_message_iter_get_arg_type (&iter)) != DBUS_TYPE_INVALID)

dbus_message_iter_next (&iter);

dbus_message_iter_next

dbus_bool_t dbus_message_iter_next(DBusMessageIter \*iter)

Moves the iterator to the next field, if any.

**Definition** dbus-message.c:2186

dbus_message_iter_get_arg_type

int dbus_message_iter_get_arg_type(DBusMessageIter \*iter)

Returns the argument type of the argument that the message iterator points to.

**Definition** dbus-message.c:2211

dbus_message_iter_init

dbus_bool_t dbus_message_iter_init(DBusMessage \*message, DBusMessageIter \*iter)

Initializes a DBusMessageIter for reading the arguments of the message passed in.

**Definition** dbus-message.c:2136

Parameters  
|      |                  |
|------|------------------|
| iter | the message iter |

<!-- -->

Returns  
the argument type

Definition at line 2211 of file dbus-message.c.

References \_dbus_type_reader_get_current_type(), DBUS_TYPE_INVALID, FALSE, DBusMessageRealIter::iter_type, DBusMessageRealIter::reader, and DBusMessageRealIter::u.

Referenced by \_dbus_message_iter_get_args_valist(), \_dbus_variant_read(), dbus_message_iter_get_basic(), and dbus_message_iter_get_element_type().

## ◆ dbus_message_iter_get_array_len()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBUS_DEPRECATED int dbus_message_iter_get_array_len | ( | DBusMessageIter \*  | *iter* | ) |  |

Returns the number of bytes in the array as marshaled in the wire protocol.

The iterator must currently be inside an array-typed value.

This function is deprecated on the grounds that it is stupid. Why would you want to know how many bytes are in the array as marshaled in the wire protocol? Use dbus_message_iter_get_element_count() instead.

Parameters  
|      |              |
|------|--------------|
| iter | the iterator |

<!-- -->

Returns  
the number of bytes in the array

Definition at line 2458 of file dbus-message.c.

References \_dbus_type_reader_get_array_length(), DBusMessageRealIter::reader, and DBusMessageRealIter::u.

## ◆ dbus_message_iter_get_basic()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_message_iter_get_basic | ( | DBusMessageIter \*  | *iter*, |
|  |  | void \*  | *value*  |
|  | ) |  |  |

Reads a basic-typed value from the message iterator.

Basic types are the non-containers such as integer and string.

The value argument should be the address of a location to store the returned value. So for int32 it should be a "dbus_int32_t\*" and for string a "const char\*\*". The returned value is by reference and should not be freed.

This call duplicates Unix file descriptors when reading them. It is your job to close them when you don't need them anymore.

Unix file descriptors that are read with this function will have the FD_CLOEXEC flag set. If you need them without this flag set, make sure to unset it with fcntl().

Be sure you have somehow checked that dbus_message_iter_get_arg_type() matches the type you are expecting, or you'll crash when you try to use an integer as a string or something.

To read any container type (array, struct, dict) you will need to recurse into the container with dbus_message_iter_recurse(). If the container is an array of fixed-length values (except Unix file descriptors), you can get all the array elements at once with dbus_message_iter_get_fixed_array(). Otherwise, you have to iterate over the container's contents one value at a time.

All basic-typed values are guaranteed to fit in a DBusBasicValue, so in versions of libdbus that have that type, you can write code like this:

DBusBasicValue value;

int type;

dbus_message_iter_get_basic (&read_iter, &value);

type = dbus_message_iter_get_arg_type (&read_iter);

dbus_message_iter_append_basic (&write_iter, type, &value);

dbus_message_iter_append_basic

dbus_bool_t dbus_message_iter_append_basic(DBusMessageIter \*iter, int type, const void \*value)

Appends a basic-typed value to the message.

**Definition** dbus-message.c:2771

dbus_message_iter_get_basic

void dbus_message_iter_get_basic(DBusMessageIter \*iter, void \*value)

Reads a basic-typed value from the message iterator.

**Definition** dbus-message.c:2369

DBusBasicValue

A simple value union that lets you access bytes as if they were various types; useful when dealing wi...

**Definition** dbus-types.h:161

(All D-Bus basic types are either numeric and 8 bytes or smaller, or behave like a string; so in older versions of libdbus, DBusBasicValue can be replaced with union { char \*string; unsigned char bytes\[8\]; }, for instance.)

Parameters  
|       |                             |
|-------|-----------------------------|
| iter  | the iterator                |
| value | location to store the value |

Definition at line 2369 of file dbus-message.c.

References \_dbus_dup(), \_dbus_type_reader_read_basic(), dbus_message_iter_get_arg_type(), DBUS_TYPE_UNIX_FD, DBusMessageRealIter::message, NULL, DBusMessageRealIter::reader, DBusMessageRealIter::u, and DBusBasicValue::u32.

Referenced by \_dbus_variant_read().

## ◆ dbus_message_iter_get_element_count()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT int dbus_message_iter_get_element_count | ( | DBusMessageIter \*  | *iter* | ) |  |

Returns the number of elements in the array-typed value pointed to by the iterator.

Note that this function is O(1) for arrays of fixed-size types but O(n) for arrays of variable-length types such as strings, so it may be a bad idea to use it.

Parameters  
|      |              |
|------|--------------|
| iter | the iterator |

<!-- -->

Returns  
the number of elements in the array

Definition at line 2414 of file dbus-message.c.

References \_dbus_type_get_alignment(), \_dbus_type_reader_get_array_length(), \_dbus_type_reader_get_current_type(), \_dbus_type_reader_get_element_type(), \_dbus_type_reader_next(), \_dbus_type_reader_recurse(), DBUS_TYPE_ARRAY, DBUS_TYPE_INVALID, dbus_type_is_fixed(), DBusMessageRealIter::reader, and DBusMessageRealIter::u.

## ◆ dbus_message_iter_get_element_type()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT int dbus_message_iter_get_element_type | ( | DBusMessageIter \*  | *iter* | ) |  |

Returns the element type of the array that the message iterator points to.

Note that you need to check that the iterator points to an array prior to using this function.

Parameters  
|      |                  |
|------|------------------|
| iter | the message iter |

<!-- -->

Returns  
the array element type

Definition at line 2230 of file dbus-message.c.

References \_dbus_type_reader_get_element_type(), dbus_message_iter_get_arg_type(), DBUS_TYPE_ARRAY, DBUS_TYPE_INVALID, DBusMessageRealIter::iter_type, DBusMessageRealIter::reader, and DBusMessageRealIter::u.

## ◆ dbus_message_iter_get_fixed_array()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_message_iter_get_fixed_array | ( | DBusMessageIter \*  | *iter*, |
|  |  | void \*  | *value*, |
|  |  | int \*  | *n_elements*  |
|  | ) |  |  |

Reads a block of fixed-length values from the message iterator.

Fixed-length values are those basic types that are not string-like, such as integers, bool, double. The returned block will be from the current position in the array until the end of the array.

There is one exception here: although DBUS_TYPE_UNIX_FD is considered a 'fixed' type arrays of this type may not be read with this function.

The message iter should be "in" the array (that is, you recurse into the array, and then you call dbus_message_iter_get_fixed_array() on the "sub-iterator" created by dbus_message_iter_recurse()).

The value argument should be the address of a location to store the returned array. So for int32 it should be a "const dbus_int32_t\*\*" The returned value is by reference and should not be freed.

This function should only be used if dbus_type_is_fixed() returns TRUE for the element type.

If an array's elements are not fixed in size, you have to recurse into the array with dbus_message_iter_recurse() and read the elements one by one.

Because the array is not copied, this function runs in constant time and is fast; it's much preferred over walking the entire array with an iterator. (However, you can always use dbus_message_iter_recurse(), even for fixed-length types; dbus_message_iter_get_fixed_array() is just an optimization.)

Parameters  
|            |                                 |
|------------|---------------------------------|
| iter       | the iterator                    |
| value      | location to store the block     |
| n_elements | number of elements in the block |

Definition at line 2503 of file dbus-message.c.

References \_dbus_type_reader_get_current_type(), \_dbus_type_reader_read_fixed_multi(), DBUS_TYPE_INVALID, dbus_type_is_fixed(), DBUS_TYPE_UNIX_FD, NULL, DBusMessageRealIter::reader, and DBusMessageRealIter::u.

## ◆ dbus_message_iter_get_signature()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT char \* dbus_message_iter_get_signature | ( | DBusMessageIter \*  | *iter* | ) |  |

Returns the current signature of a message iterator.

This is useful primarily for dealing with variants; one can recurse into a variant and determine the signature of the variant's value.

The returned string must be freed with dbus_free().

Parameters  
|      |                      |
|------|----------------------|
| iter | the message iterator |

<!-- -->

Returns  
the contained signature, or NULL if out of memory

Definition at line 2292 of file dbus-message.c.

References \_dbus_string_append_len(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_init(), \_dbus_string_steal_data(), \_dbus_type_reader_get_signature(), NULL, DBusMessageRealIter::reader, and DBusMessageRealIter::u.

## ◆ dbus_message_iter_has_next()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_iter_has_next | ( | DBusMessageIter \*  | *iter* | ) |  |

Checks if an iterator has any more fields.

Parameters  
|      |                  |
|------|------------------|
| iter | the message iter |

<!-- -->

Returns  
TRUE if there are more fields following

Definition at line 2167 of file dbus-message.c.

References \_dbus_type_reader_has_next(), FALSE, DBusMessageRealIter::iter_type, DBusMessageRealIter::reader, and DBusMessageRealIter::u.

## ◆ dbus_message_iter_init()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_iter_init | ( | DBusMessage \*  | *message*, |
|  |  | DBusMessageIter \*  | *iter*  |
|  | ) |  |  |

Initializes a DBusMessageIter for reading the arguments of the message passed in.

When possible, dbus_message_get_args() is much more convenient. Some types of argument can only be read with DBusMessageIter however.

The easiest way to iterate is like this:

dbus_message_iter_init (message, &iter);

while ((current_type = dbus_message_iter_get_arg_type (&iter)) != DBUS_TYPE_INVALID)

dbus_message_iter_next (&iter);

DBusMessageIter contains no allocated memory; it need not be freed, and can be copied by assignment or memcpy().

Parameters  
|         |                                      |
|---------|--------------------------------------|
| message | the message                          |
| iter    | pointer to an iterator to initialize |

<!-- -->

Returns  
FALSE if the message has no arguments

Definition at line 2136 of file dbus-message.c.

References \_dbus_header_get_byte_order(), \_dbus_type_reader_get_current_type(), \_dbus_type_reader_init(), body, DBUS_TYPE_INVALID, FALSE, header, NULL, DBusMessageRealIter::reader, and DBusMessageRealIter::u.

Referenced by dbus_message_get_args_valist().

## ◆ dbus_message_iter_init_append()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_message_iter_init_append | ( | DBusMessage \*  | *message*, |
|  |  | DBusMessageIter \*  | *iter*  |
|  | ) |  |  |

Initializes a DBusMessageIter for appending arguments to the end of a message.

Parameters  
|         |                                      |
|---------|--------------------------------------|
| message | the message                          |
| iter    | pointer to an iterator to initialize |

Definition at line 2533 of file dbus-message.c.

References \_dbus_header_get_byte_order(), \_dbus_string_get_length(), \_dbus_type_writer_init_types_delayed(), body, header, NULL, DBusMessageRealIter::u, and DBusMessageRealIter::writer.

Referenced by dbus_message_append_args_valist(), and dbus_message_new_error().

## ◆ dbus_message_iter_init_closed()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_message_iter_init_closed | ( | DBusMessageIter \*  | *iter* | ) |  |

Initialize iter as if with DBUS_MESSAGE_ITER_INIT_CLOSED.

The only valid operation for such an iterator is dbus_message_iter_abandon_container_if_open(), which does nothing.

Definition at line 755 of file dbus-message.c.

References NULL.

## ◆ dbus_message_iter_next()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_iter_next | ( | DBusMessageIter \*  | *iter* | ) |  |

Moves the iterator to the next field, if any.

If there's no next field, returns FALSE. If the iterator moves forward, returns TRUE.

Parameters  
|      |                  |
|------|------------------|
| iter | the message iter |

<!-- -->

Returns  
TRUE if the iterator was moved to the next field

Definition at line 2186 of file dbus-message.c.

References \_dbus_type_reader_next(), FALSE, DBusMessageRealIter::iter_type, DBusMessageRealIter::reader, and DBusMessageRealIter::u.

## ◆ dbus_message_iter_open_container()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_iter_open_container | ( | DBusMessageIter \*  | *iter*, |
|  |  | int  | *type*, |
|  |  | const char \*  | *contained_signature*, |
|  |  | DBusMessageIter \*  | *sub*  |
|  | ) |  |  |

Appends a container-typed value to the message.

On success, you are required to append the contents of the container using the returned sub-iterator, and then call dbus_message_iter_close_container(). Container types are for example struct, variant, and array. For variants, the contained_signature should be the type of the single value inside the variant. For structs and dict entries, contained_signature should be NULL; it will be set to whatever types you write into the struct. For arrays, contained_signature should be the type of the array elements.

If this function fails, the sub-iterator remains invalid, and must not be closed with dbus_message_iter_close_container() or abandoned with dbus_message_iter_abandon_container(). However, after this function has either succeeded or failed, it is valid to call dbus_message_iter_abandon_container_if_open().

Parameters  
|                     |                                |
|---------------------|--------------------------------|
| iter                | the append iterator            |
| type                | the type of the value          |
| contained_signature | the type of container contents |
| sub                 | sub-iterator to initialize     |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 2986 of file dbus-message.c.

References \_dbus_string_get_length(), \_dbus_string_init_const(), \_dbus_type_writer_recurse(), \_dbus_validate_signature_with_reason(), DBUS_DICT_ENTRY_BEGIN_CHAR, DBUS_TYPE_ARRAY, DBUS_TYPE_DICT_ENTRY, dbus_type_is_container(), DBUS_TYPE_STRUCT, DBUS_TYPE_VARIANT, DBUS_VALID, DBUS_VALIDITY_UNKNOWN_OOM_ERROR, FALSE, DBusMessageRealIter::iter_type, NULL, DBusMessageRealIter::u, and DBusMessageRealIter::writer.

Referenced by dbus_message_append_args_valist().

## ◆ dbus_message_iter_recurse()

|                                            |     |                     |         |
|--------------------------------------------|-----|---------------------|---------|
| DBUS_EXPORT void dbus_message_iter_recurse | (   | DBusMessageIter \*  | *iter*, |
|                                            |     | DBusMessageIter \*  | *sub*   |
|                                            | )   |                     |         |

Recurses into a container value when reading values from a message, initializing a sub-iterator to use for traversing the child values of the container.

Note that this recurses into a value, not a type, so you can only recurse if the value exists. The main implication of this is that if you have for example an empty array of array of int32, you can recurse into the outermost array, but it will have no values, so you won't be able to recurse further. There's no array of int32 to recurse into.

If a container is an array of fixed-length types (except Unix file descriptors), it is much more efficient to use dbus_message_iter_get_fixed_array() to get the whole array in one shot, rather than individually walking over the array elements.

Be sure you have somehow checked that dbus_message_iter_get_arg_type() matches the type you are expecting to recurse into. Results of this function are undefined if there is no container to recurse into at the current iterator position.

Parameters  
|      |                                |
|------|--------------------------------|
| iter | the message iterator           |
| sub  | the sub-iterator to initialize |

Definition at line 2267 of file dbus-message.c.

References \_dbus_type_reader_recurse(), NULL, DBusMessageRealIter::reader, and DBusMessageRealIter::u.

Referenced by \_dbus_variant_read().

## ◆ dbus_message_lock()

|                                    |     |                 |           |     |     |
|------------------------------------|-----|-----------------|-----------|-----|-----|
| DBUS_EXPORT void dbus_message_lock | (   | DBusMessage \*  | *message* | )   |     |

Locks a message.

Allows checking that applications don't keep a reference to a message in the outgoing queue and change it underneath us. Messages are locked when they enter the outgoing queue (dbus_connection_send_message()), and the library complains if the message is modified while locked. This function may also called externally, for applications wrapping D-Bus in another protocol.

Parameters  
|         |                      |
|---------|----------------------|
| message | the message to lock. |

Definition at line 431 of file dbus-message.c.

References \_dbus_assert, \_dbus_header_update_lengths(), \_dbus_string_get_length(), body, dbus_message_get_signature(), header, locked, NULL, and TRUE.

Referenced by dbus_message_marshal().

## ◆ dbus_message_marshal()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_marshal | ( | DBusMessage \*  | *msg*, |
|  |  | char \*\*  | *marshalled_data_p*, |
|  |  | int \*  | *len_p*  |
|  | ) |  |  |

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

References \_dbus_string_copy(), \_dbus_string_free(), \_dbus_string_get_length(), \_dbus_string_init(), \_dbus_string_steal_data(), body, DBusHeader::data, dbus_message_lock(), FALSE, header, locked, NULL, and TRUE.

## ◆ dbus_message_new()

|                                             |     |      |                |     |     |
|---------------------------------------------|-----|------|----------------|-----|-----|
| DBUS_EXPORT DBusMessage \* dbus_message_new | (   | int  | *message_type* | )   |     |

Constructs a new message of the given message type.

Types include DBUS_MESSAGE_TYPE_METHOD_CALL, DBUS_MESSAGE_TYPE_SIGNAL, and so forth.

Usually you want to use dbus_message_new_method_call(), dbus_message_new_method_return(), dbus_message_new_signal(), or dbus_message_new_error() instead.

Parameters  
|              |                 |
|--------------|-----------------|
| message_type | type of message |

<!-- -->

Returns  
new message or NULL if no memory

Definition at line 1334 of file dbus-message.c.

References \_dbus_header_create(), DBUS_MESSAGE_TYPE_INVALID, dbus_message_unref(), header, and NULL.

## ◆ dbus_message_new_error()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_message_new_error | ( | DBusMessage \*  | *reply_to*, |
|  |  | const char \*  | *error_name*, |
|  |  | const char \*  | *error_message*  |
|  | ) |  |  |

Creates a new message that is an error reply to another message.

Error replies are most common in response to method calls, but can be returned in reply to any message.

The error name must be a valid error name according to the syntax given in the D-Bus specification. If you don't want to make up an error name just use DBUS_ERROR_FAILED.

Parameters  
|  |  |
|----|----|
| reply_to | the message we're replying to |
| error_name | the error name |
| error_message | the error message string (or NULL for none, but please give a message) |

<!-- -->

Returns  
a new error message object, free with dbus_message_unref()

Definition at line 1515 of file dbus-message.c.

References \_dbus_header_create(), dbus_message_get_sender(), dbus_message_get_serial(), dbus_message_iter_append_basic(), dbus_message_iter_init_append(), dbus_message_set_no_reply(), dbus_message_set_reply_serial(), DBUS_MESSAGE_TYPE_ERROR, dbus_message_unref(), DBUS_TYPE_STRING, header, NULL, and TRUE.

Referenced by \_dbus_pending_call_set_timeout_error_unlocked(), dbus_connection_dispatch(), and dbus_message_new_error_printf().

## ◆ dbus_message_new_error_printf()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_message_new_error_printf | ( | DBusMessage \*  | *reply_to*, |
|  |  | const char \*  | *error_name*, |
|  |  | const char \*  | *error_format*, |
|  |  |   | *...*  |
|  | ) |  |  |

Creates a new message that is an error reply to another message, allowing you to use printf formatting.

See dbus_message_new_error() for details - this function is the same aside from the printf formatting.

Parameters  
|              |                                         |
|--------------|-----------------------------------------|
| reply_to     | the original message                    |
| error_name   | the error name                          |
| error_format | the error message format as with printf |
| ...          | format string arguments                 |

<!-- -->

Returns  
a new error message

Definition at line 1587 of file dbus-message.c.

References \_dbus_string_append_printf_valist(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_init(), dbus_message_new_error(), and NULL.

## ◆ dbus_message_new_method_call()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_message_new_method_call | ( | const char \*  | *destination*, |
|  |  | const char \*  | *path*, |
|  |  | const char \*  | *iface*, |
|  |  | const char \*  | *method*  |
|  | ) |  |  |

Constructs a new message to invoke a method on a remote object.

Returns NULL if memory can't be allocated for the message. The destination may be NULL in which case no destination is set; this is appropriate when using D-Bus in a peer-to-peer context (no message bus). The interface may be NULL, which means that if multiple methods with the given name exist it is undefined which one will be invoked.

The path and method names may not be NULL.

Destination, path, interface, and method name can't contain any invalid characters (see the D-Bus specification).

Parameters  
|             |                                                 |
|-------------|-------------------------------------------------|
| destination | name that the message should be sent to or NULL |
| path        | object path the message should be sent to       |
| iface       | interface to invoke method on, or NULL          |
| method      | method to invoke                                |

<!-- -->

Returns  
a new DBusMessage, free with dbus_message_unref()

Definition at line 1378 of file dbus-message.c.

References \_dbus_header_create(), DBUS_MESSAGE_TYPE_METHOD_CALL, dbus_message_unref(), header, and NULL.

Referenced by dbus_bus_add_match(), dbus_bus_get_id(), dbus_bus_get_unix_user(), dbus_bus_name_has_owner(), dbus_bus_register(), dbus_bus_release_name(), dbus_bus_remove_match(), dbus_bus_request_name(), and dbus_bus_start_service_by_name().

## ◆ dbus_message_new_method_return()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_message_new_method_return | ( | DBusMessage \*  | *method_call* | ) |  |

Constructs a message that is a reply to a method call.

Returns NULL if memory can't be allocated for the message.

Parameters  
|             |                              |
|-------------|------------------------------|
| method_call | the message being replied to |

<!-- -->

Returns  
a new DBusMessage, free with dbus_message_unref()

Definition at line 1418 of file dbus-message.c.

References \_dbus_header_create(), dbus_message_get_sender(), dbus_message_get_serial(), dbus_message_set_no_reply(), dbus_message_set_reply_serial(), DBUS_MESSAGE_TYPE_METHOD_RETURN, dbus_message_unref(), header, NULL, and TRUE.

## ◆ dbus_message_new_signal()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_message_new_signal | ( | const char \*  | *path*, |
|  |  | const char \*  | *iface*, |
|  |  | const char \*  | *name*  |
|  | ) |  |  |

Constructs a new message representing a signal emission.

Returns NULL if memory can't be allocated for the message. A signal is identified by its originating object path, interface, and the name of the signal.

Path, interface, and signal name must all be valid (the D-Bus specification defines the syntax of these fields).

Parameters  
|       |                                            |
|-------|--------------------------------------------|
| path  | the path to the object emitting the signal |
| iface | the interface the signal is emitted from   |
| name  | name of the signal                         |

<!-- -->

Returns  
a new DBusMessage, free with dbus_message_unref()

Definition at line 1469 of file dbus-message.c.

References \_dbus_header_create(), dbus_message_set_no_reply(), DBUS_MESSAGE_TYPE_SIGNAL, dbus_message_unref(), header, NULL, and TRUE.

Referenced by \_dbus_connection_new_for_transport().

## ◆ dbus_message_ref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_message_ref | ( | DBusMessage \*  | *message* | ) |  |

Increments the reference count of a DBusMessage.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

Returns  
the message

<!-- -->

See also  
dbus_message_unref

Definition at line 1712 of file dbus-message.c.

References \_dbus_assert, \_dbus_atomic_inc(), \_dbus_current_generation, generation, in_cache, NULL, and refcount.

Referenced by \_dbus_pending_call_set_reply_unlocked().

## ◆ dbus_message_set_allow_interactive_authorization()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_message_set_allow_interactive_authorization | ( | DBusMessage \*  | *message*, |
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

References \_dbus_header_toggle_flag(), DBUS_HEADER_FLAG_ALLOW_INTERACTIVE_AUTHORIZATION, header, locked, and NULL.

## ◆ dbus_message_set_auto_start()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_message_set_auto_start | ( | DBusMessage \*  | *message*, |
|  |  | dbus_bool_t  | *auto_start*  |
|  | ) |  |  |

Sets a flag indicating that an owner for the destination name will be automatically started before the message is delivered.

When this flag is set, the message is held until a name owner finishes starting up, or fails to start up. In case of failure, the reply will be an error.

The flag is set to TRUE by default, i.e. auto starting is the default.

On the protocol level this toggles DBUS_HEADER_FLAG_NO_AUTO_START

Parameters  
|            |                                  |
|------------|----------------------------------|
| message    | the message                      |
| auto_start | TRUE if auto-starting is desired |

Definition at line 3289 of file dbus-message.c.

References \_dbus_header_toggle_flag(), DBUS_HEADER_FLAG_NO_AUTO_START, header, locked, and NULL.

## ◆ dbus_message_set_container_instance()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_set_container_instance | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *object_path*  |
|  | ) |  |  |

Sets the container instance this message was sent from.

The path must contain only valid characters for an object path as defined in the D-Bus specification.

Parameters  
|             |                           |
|-------------|---------------------------|
| message     | the message               |
| object_path | the path or NULL to unset |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 4110 of file dbus-message.c.

References DBUS_HEADER_FIELD_CONTAINER_INSTANCE, DBUS_TYPE_OBJECT_PATH, FALSE, locked, and NULL.

## ◆ dbus_message_set_data()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_set_data | ( | DBusMessage \*  | *message*, |
|  |  | dbus_int32_t  | *slot*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_func*  |
|  | ) |  |  |

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

References \_dbus_data_slot_list_set(), FALSE, NULL, and slot_list.

## ◆ dbus_message_set_destination()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_set_destination | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *destination*  |
|  | ) |  |  |

Sets the message's destination.

The destination is the name of another connection on the bus and may be either the unique name assigned by the bus to each connection, or a well-known name specified in advance.

The destination name must contain only valid characters as defined in the D-Bus specification.

Parameters  
|             |                                       |
|-------------|---------------------------------------|
| message     | the message                           |
| destination | the destination name or NULL to unset |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 3688 of file dbus-message.c.

References DBUS_HEADER_FIELD_DESTINATION, DBUS_TYPE_STRING, FALSE, locked, and NULL.

## ◆ dbus_message_set_error_name()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_set_error_name | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *error_name*  |
|  | ) |  |  |

Sets the name of the error (DBUS_MESSAGE_TYPE_ERROR).

The name is fully-qualified (namespaced).

The error name must contain only valid characters as defined in the D-Bus specification.

Parameters  
|            |                           |
|------------|---------------------------|
| message    | the message               |
| error_name | the name or NULL to unset |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 3634 of file dbus-message.c.

References DBUS_HEADER_FIELD_ERROR_NAME, DBUS_TYPE_STRING, FALSE, locked, and NULL.

## ◆ dbus_message_set_interface()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_set_interface | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *iface*  |
|  | ) |  |  |

Sets the interface this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or the interface a signal is being emitted from (for DBUS_MESSAGE_TYPE_SIGNAL).

The interface name must contain only valid characters as defined in the D-Bus specification.

Parameters  
|         |                                |
|---------|--------------------------------|
| message | the message                    |
| iface   | the interface or NULL to unset |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 3461 of file dbus-message.c.

References DBUS_HEADER_FIELD_INTERFACE, DBUS_TYPE_STRING, FALSE, locked, and NULL.

## ◆ dbus_message_set_member()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_set_member | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *member*  |
|  | ) |  |  |

Sets the interface member being invoked (DBUS_MESSAGE_TYPE_METHOD_CALL) or emitted (DBUS_MESSAGE_TYPE_SIGNAL).

The member name must contain only valid characters as defined in the D-Bus specification.

Parameters  
|         |                             |
|---------|-----------------------------|
| message | the message                 |
| member  | the member or NULL to unset |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 3549 of file dbus-message.c.

References DBUS_HEADER_FIELD_MEMBER, DBUS_TYPE_STRING, FALSE, locked, and NULL.

## ◆ dbus_message_set_no_reply()

|                                            |     |                 |             |
|--------------------------------------------|-----|-----------------|-------------|
| DBUS_EXPORT void dbus_message_set_no_reply | (   | DBusMessage \*  | *message*,  |
|                                            |     | dbus_bool_t     | *no_reply*  |
|                                            | )   |                 |             |

Sets a flag indicating that the message does not want a reply; if this flag is set, the other end of the connection may (but is not required to) optimize by not sending method return or error replies.

If this flag is set, there is no way to know whether the message successfully arrived at the remote end. Normally you know a message was received when you receive the reply to it.

The flag is FALSE by default, that is by default the other end is required to reply.

On the protocol level this toggles DBUS_HEADER_FLAG_NO_REPLY_EXPECTED

Parameters  
|          |                             |
|----------|-----------------------------|
| message  | the message                 |
| no_reply | TRUE if no reply is desired |

Definition at line 3247 of file dbus-message.c.

References \_dbus_header_toggle_flag(), DBUS_HEADER_FLAG_NO_REPLY_EXPECTED, header, locked, and NULL.

Referenced by dbus_message_new_error(), dbus_message_new_method_return(), and dbus_message_new_signal().

## ◆ dbus_message_set_path()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_set_path | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *object_path*  |
|  | ) |  |  |

Sets the object path this message is being sent to (for DBUS_MESSAGE_TYPE_METHOD_CALL) or the one a signal is being emitted from (for DBUS_MESSAGE_TYPE_SIGNAL).

The path must contain only valid characters as defined in the D-Bus specification.

Parameters  
|             |                           |
|-------------|---------------------------|
| message     | the message               |
| object_path | the path or NULL to unset |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 3330 of file dbus-message.c.

References DBUS_HEADER_FIELD_PATH, DBUS_TYPE_OBJECT_PATH, FALSE, locked, and NULL.

## ◆ dbus_message_set_reply_serial()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_set_reply_serial | ( | DBusMessage \*  | *message*, |
|  |  | dbus_uint32_t  | *reply_serial*  |
|  | ) |  |  |

Sets the reply serial of a message (the serial of the message this is a reply to).

Parameters  
|              |                              |
|--------------|------------------------------|
| message      | the message                  |
| reply_serial | the serial we're replying to |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 1184 of file dbus-message.c.

References \_dbus_header_set_field_basic(), DBUS_HEADER_FIELD_REPLY_SERIAL, DBUS_TYPE_UINT32, FALSE, header, locked, NULL, and DBusBasicValue::u32.

Referenced by dbus_message_new_error(), and dbus_message_new_method_return().

## ◆ dbus_message_set_sender()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_message_set_sender | ( | DBusMessage \*  | *message*, |
|  |  | const char \*  | *sender*  |
|  | ) |  |  |

Sets the message sender.

The sender must be a valid bus name as defined in the D-Bus specification.

Usually you don't want to call this. The message bus daemon will call it to set the origin of each message. If you aren't implementing a message bus daemon you shouldn't need to set the sender.

Parameters  
|         |                             |
|---------|-----------------------------|
| message | the message                 |
| sender  | the sender or NULL to unset |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 3742 of file dbus-message.c.

References DBUS_HEADER_FIELD_SENDER, DBUS_TYPE_STRING, FALSE, locked, and NULL.

## ◆ dbus_message_set_serial()

|                                          |     |                 |            |
|------------------------------------------|-----|-----------------|------------|
| DBUS_EXPORT void dbus_message_set_serial | (   | DBusMessage \*  | *message*, |
|                                          |     | dbus_uint32_t   | *serial*   |
|                                          | )   |                 |            |

Sets the serial number of a message.

This can only be done once on a message.

DBusConnection will automatically set the serial to an appropriate value when the message is sent; this function is only needed when encapsulating messages in another protocol, or otherwise bypassing DBusConnection.

Parameters  
|         |             |
|---------|-------------|
| message | the message |
| serial  | the serial  |

Definition at line 301 of file dbus-message.c.

References \_dbus_header_set_serial(), header, locked, and NULL.

Referenced by dbus_connection_send_with_reply().

## ◆ dbus_message_type_from_string()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT int dbus_message_type_from_string | ( | const char \*  | *type_str* | ) |  |

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

|                                                       |     |      |        |     |     |
|-------------------------------------------------------|-----|------|--------|-----|-----|
| DBUS_EXPORT const char \* dbus_message_type_to_string | (   | int  | *type* | )   |     |

Utility function to convert a D-Bus message type into a machine-readable string (not translated).

DBUS_MESSAGE_TYPE_METHOD_CALL -\> "method_call"

DBUS_MESSAGE_TYPE_METHOD_RETURN -\> "method_return"

DBUS_MESSAGE_TYPE_SIGNAL -\> "signal"

DBUS_MESSAGE_TYPE_ERROR -\> "error"

DBUS_MESSAGE_TYPE_INVALID -\> "invalid"

Definition at line 5081 of file dbus-message.c.

References DBUS_MESSAGE_TYPE_ERROR, DBUS_MESSAGE_TYPE_METHOD_CALL, DBUS_MESSAGE_TYPE_METHOD_RETURN, and DBUS_MESSAGE_TYPE_SIGNAL.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_connection_queue_received_message_link(), and dbus_connection_dispatch().

## ◆ dbus_message_unref()

|                                     |     |                 |           |     |     |
|-------------------------------------|-----|-----------------|-----------|-----|-----|
| DBUS_EXPORT void dbus_message_unref | (   | DBusMessage \*  | *message* | )   |     |

Decrements the reference count of a DBusMessage, freeing the message if the count reaches 0.

Parameters  
|         |             |
|---------|-------------|
| message | the message |

<!-- -->

See also  
dbus_message_ref

Definition at line 1735 of file dbus-message.c.

References \_dbus_assert, \_dbus_atomic_dec(), \_dbus_current_generation, generation, in_cache, NULL, and refcount.

Referenced by \_dbus_connection_block_pending_call(), \_dbus_connection_new_for_transport(), \_dbus_connection_unlock(), \_dbus_message_loader_queue_messages(), \_dbus_message_loader_unref(), \_dbus_pending_call_set_timeout_error_unlocked(), dbus_bus_add_match(), dbus_bus_get_id(), dbus_bus_get_unix_user(), dbus_bus_name_has_owner(), dbus_bus_register(), dbus_bus_release_name(), dbus_bus_remove_match(), dbus_bus_request_name(), dbus_bus_start_service_by_name(), dbus_connection_dispatch(), dbus_connection_send_with_reply_and_block(), dbus_message_new(), dbus_message_new_error(), dbus_message_new_method_call(), dbus_message_new_method_return(), and dbus_message_new_signal().

## ◆ dbus_set_error_from_message()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_set_error_from_message | ( | DBusError \*  | *error*, |
|  |  | DBusMessage \*  | *message*  |
|  | ) |  |  |

Sets a DBusError based on the contents of the given message.

The error is only set if the message is an error message, as in DBUS_MESSAGE_TYPE_ERROR. The name of the error is set to the name of the message, and the error message is set to the first argument if the argument exists and is a string.

The return value indicates whether the error was set (the error is set if and only if the message is an error message). So you can check for an error reply and convert it to DBusError in one go:

if (dbus_set_error_from_message (error, reply))

return error;

else

process reply;

dbus_set_error_from_message

dbus_bool_t dbus_set_error_from_message(DBusError \*error, DBusMessage \*message)

Sets a DBusError based on the contents of the given message.

**Definition** dbus-message.c:4059

Parameters  
|         |                            |
|---------|----------------------------|
| error   | the error to set           |
| message | the message to set it from |

<!-- -->

Returns  
TRUE if the message had type DBUS_MESSAGE_TYPE_ERROR

Definition at line 4059 of file dbus-message.c.

References dbus_message_get_args(), dbus_message_get_error_name(), dbus_message_get_type(), DBUS_MESSAGE_TYPE_ERROR, dbus_set_error(), DBUS_TYPE_INVALID, DBUS_TYPE_STRING, FALSE, NULL, and TRUE.

Referenced by dbus_bus_get_id(), dbus_bus_get_unix_user(), dbus_bus_register(), dbus_bus_release_name(), dbus_bus_request_name(), dbus_bus_start_service_by_name(), and dbus_connection_send_with_reply_and_block().
