DBusConnection implementation details

D-Bus secret internal implementation details

Implementation details of DBusConnection. More...

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
<td class="memItemRight" data-valign="bottom">DBusMessageFilter</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internal struct representing a message filter function. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusPreallocatedSend</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internals of DBusPreallocatedSend. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusConnection</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Implementation details of DBusConnection. More...<br />
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
<td colspan="2"><h2 id="typedefs" class="groupheader"> Typedefs</h2></td>
</tr>
<tr id="r_gaec8158f55878d1a6459ebdc9950fa783" class="memitem:gaec8158f55878d1a6459ebdc9950fa783">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusMessageFilter </td>
<td class="memItemRight" data-valign="bottom">DBusMessageFilter</td>
</tr>
<tr class="memdesc:gaec8158f55878d1a6459ebdc9950fa783">
<td class="mdescLeft"> </td>
<td class="mdescRight">Internal struct representing a message filter function.<br />
</td>
</tr>
<tr class="separator:gaec8158f55878d1a6459ebdc9950fa783">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacec4220795b4d31e77547dcbcdecdb53" class="memitem:gacec4220795b4d31e77547dcbcdecdb53">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusWatchAddFunction) (DBusWatchList *list, DBusWatch *watch)</td>
</tr>
<tr class="memdesc:gacec4220795b4d31e77547dcbcdecdb53">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_watch() with refcount held.<br />
</td>
</tr>
<tr class="separator:gacec4220795b4d31e77547dcbcdecdb53">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3d3f6c25b94c857059e816dcb1f5629e" class="memitem:ga3d3f6c25b94c857059e816dcb1f5629e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusWatchRemoveFunction) (DBusWatchList *list, DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga3d3f6c25b94c857059e816dcb1f5629e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_watch() with refcount held.<br />
</td>
</tr>
<tr class="separator:ga3d3f6c25b94c857059e816dcb1f5629e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabd9d6416ed2bb1abc881123249d91b9b" class="memitem:gabd9d6416ed2bb1abc881123249d91b9b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusWatchToggleFunction) (DBusWatchList *list, DBusWatch *watch, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:gabd9d6416ed2bb1abc881123249d91b9b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_watch() with refcount held.<br />
</td>
</tr>
<tr class="separator:gabd9d6416ed2bb1abc881123249d91b9b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaaae2977e5da448c2aa90dcf0b8fc6b2f" class="memitem:gaaae2977e5da448c2aa90dcf0b8fc6b2f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusTimeoutAddFunction) (DBusTimeoutList *list, DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:gaaae2977e5da448c2aa90dcf0b8fc6b2f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_timeout() with refcount held.<br />
</td>
</tr>
<tr class="separator:gaaae2977e5da448c2aa90dcf0b8fc6b2f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7d326b67ddbbf2fdb63cdc13f1cbb129" class="memitem:ga7d326b67ddbbf2fdb63cdc13f1cbb129">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusTimeoutRemoveFunction) (DBusTimeoutList *list, DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga7d326b67ddbbf2fdb63cdc13f1cbb129">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_timeout() with refcount held.<br />
</td>
</tr>
<tr class="separator:ga7d326b67ddbbf2fdb63cdc13f1cbb129">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga775e02883191ec762f386d0953fd6308" class="memitem:ga775e02883191ec762f386d0953fd6308">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusTimeoutToggleFunction) (DBusTimeoutList *list, DBusTimeout *timeout, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:ga775e02883191ec762f386d0953fd6308">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to be called in protected_change_timeout() with refcount held.<br />
</td>
</tr>
<tr class="separator:ga775e02883191ec762f386d0953fd6308">
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
<tr id="r_ga4fe0c8f7b72dc89b9e1a3110db2f778e" class="memitem:ga4fe0c8f7b72dc89b9e1a3110db2f778e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_lock (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga4fe0c8f7b72dc89b9e1a3110db2f778e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Acquires the connection lock.<br />
</td>
</tr>
<tr class="separator:ga4fe0c8f7b72dc89b9e1a3110db2f778e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3db10d48ec16e485d5a638aacebd4ad2" class="memitem:ga3db10d48ec16e485d5a638aacebd4ad2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_unlock (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga3db10d48ec16e485d5a638aacebd4ad2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Releases the connection lock.<br />
</td>
</tr>
<tr class="separator:ga3db10d48ec16e485d5a638aacebd4ad2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac1b92eba0aeee294dc28fcc260c9b749" class="memitem:gac1b92eba0aeee294dc28fcc260c9b749">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_queue_received_message_link (DBusConnection *connection, DBusList *link)</td>
</tr>
<tr class="memdesc:gac1b92eba0aeee294dc28fcc260c9b749">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a message-containing list link to the incoming message queue, taking ownership of the link and the message's current refcount.<br />
</td>
</tr>
<tr class="separator:gac1b92eba0aeee294dc28fcc260c9b749">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadb7a525dc6b566b575ee4f9b20028b04" class="memitem:gadb7a525dc6b566b575ee4f9b20028b04">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_queue_synthesized_message_link (DBusConnection *connection, DBusList *link)</td>
</tr>
<tr class="memdesc:gadb7a525dc6b566b575ee4f9b20028b04">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a link + message to the incoming message queue.<br />
</td>
</tr>
<tr class="separator:gadb7a525dc6b566b575ee4f9b20028b04">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3d31a01751860b67f960dcaffb7bb4ef" class="memitem:ga3d31a01751860b67f960dcaffb7bb4ef">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_has_messages_to_send_unlocked (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga3d31a01751860b67f960dcaffb7bb4ef">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether there are messages in the outgoing message queue.<br />
</td>
</tr>
<tr class="separator:ga3d31a01751860b67f960dcaffb7bb4ef">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2210bb5734c1a04d0d654b026f27d94e" class="memitem:ga2210bb5734c1a04d0d654b026f27d94e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_has_messages_to_send (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga2210bb5734c1a04d0d654b026f27d94e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether there are messages in the outgoing message queue.<br />
</td>
</tr>
<tr class="separator:ga2210bb5734c1a04d0d654b026f27d94e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa70037deabe2f362a479d859823918f3" class="memitem:gaa70037deabe2f362a479d859823918f3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_get_message_to_send (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gaa70037deabe2f362a479d859823918f3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the next outgoing message.<br />
</td>
</tr>
<tr class="separator:gaa70037deabe2f362a479d859823918f3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab93fd3666217ee339c4d2e8d4d33e63c" class="memitem:gab93fd3666217ee339c4d2e8d4d33e63c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_message_sent_unlocked (DBusConnection *connection, DBusMessage *message)</td>
</tr>
<tr class="memdesc:gab93fd3666217ee339c4d2e8d4d33e63c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Notifies the connection that a message has been sent, so the message can be removed from the outgoing queue.<br />
</td>
</tr>
<tr class="separator:gab93fd3666217ee339c4d2e8d4d33e63c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga82adef36b4cd583bc1146eae5756c063" class="memitem:ga82adef36b4cd583bc1146eae5756c063">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_add_watch_unlocked (DBusConnection *connection, DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga82adef36b4cd583bc1146eae5756c063">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a watch using the connection's DBusAddWatchFunction if available.<br />
</td>
</tr>
<tr class="separator:ga82adef36b4cd583bc1146eae5756c063">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga65fc02c0756d0c7caaa39cd60922c99b" class="memitem:ga65fc02c0756d0c7caaa39cd60922c99b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_remove_watch_unlocked (DBusConnection *connection, DBusWatch *watch)</td>
</tr>
<tr class="memdesc:ga65fc02c0756d0c7caaa39cd60922c99b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a watch using the connection's DBusRemoveWatchFunction if available.<br />
</td>
</tr>
<tr class="separator:ga65fc02c0756d0c7caaa39cd60922c99b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6c00e2eaf225b154760976af5688d250" class="memitem:ga6c00e2eaf225b154760976af5688d250">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_toggle_watch_unlocked (DBusConnection *connection, DBusWatch *watch, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:ga6c00e2eaf225b154760976af5688d250">
<td class="mdescLeft"> </td>
<td class="mdescRight">Toggles a watch and notifies app via connection's DBusWatchToggledFunction if available.<br />
</td>
</tr>
<tr class="separator:ga6c00e2eaf225b154760976af5688d250">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga69e87e3be94b8c681585ec870e39a64a" class="memitem:ga69e87e3be94b8c681585ec870e39a64a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_add_timeout_unlocked (DBusConnection *connection, DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:ga69e87e3be94b8c681585ec870e39a64a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a timeout using the connection's DBusAddTimeoutFunction if available.<br />
</td>
</tr>
<tr class="separator:ga69e87e3be94b8c681585ec870e39a64a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabaa6d26f6eca30782904af1ceb703bd1" class="memitem:gabaa6d26f6eca30782904af1ceb703bd1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_remove_timeout_unlocked (DBusConnection *connection, DBusTimeout *timeout)</td>
</tr>
<tr class="memdesc:gabaa6d26f6eca30782904af1ceb703bd1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a timeout using the connection's DBusRemoveTimeoutFunction if available.<br />
</td>
</tr>
<tr class="separator:gabaa6d26f6eca30782904af1ceb703bd1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga165dcfd8b995ff0edd19aebcf3e1a61a" class="memitem:ga165dcfd8b995ff0edd19aebcf3e1a61a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_toggle_timeout_unlocked (DBusConnection *connection, DBusTimeout *timeout, dbus_bool_t enabled)</td>
</tr>
<tr class="memdesc:ga165dcfd8b995ff0edd19aebcf3e1a61a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Toggles a timeout and notifies app via connection's DBusTimeoutToggledFunction if available.<br />
</td>
</tr>
<tr class="separator:ga165dcfd8b995ff0edd19aebcf3e1a61a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga968196bee49659e75c54b53d7c85fa51" class="memitem:ga968196bee49659e75c54b53d7c85fa51">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_remove_pending_call (DBusConnection *connection, DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:ga968196bee49659e75c54b53d7c85fa51">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a pending call from the connection, such that the pending reply will be ignored.<br />
</td>
</tr>
<tr class="separator:ga968196bee49659e75c54b53d7c85fa51">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga283f0254537c4bf4453dbed6fad2e21e" class="memitem:ga283f0254537c4bf4453dbed6fad2e21e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_do_iteration_unlocked (DBusConnection *connection, DBusPendingCall *pending, unsigned int flags, int timeout_milliseconds)</td>
</tr>
<tr class="memdesc:ga283f0254537c4bf4453dbed6fad2e21e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Queues incoming messages and sends outgoing messages for this connection, optionally blocking in the process.<br />
</td>
</tr>
<tr class="separator:ga283f0254537c4bf4453dbed6fad2e21e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga349cb271344a906525242681d54f03f5" class="memitem:ga349cb271344a906525242681d54f03f5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_new_for_transport (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:ga349cb271344a906525242681d54f03f5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new connection for the given transport.<br />
</td>
</tr>
<tr class="separator:ga349cb271344a906525242681d54f03f5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae2e4d7af6d1244c1c4c40744253c9cc9" class="memitem:gae2e4d7af6d1244c1c4c40744253c9cc9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_ref_unlocked (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gae2e4d7af6d1244c1c4c40744253c9cc9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count of a DBusConnection.<br />
</td>
</tr>
<tr class="separator:gae2e4d7af6d1244c1c4c40744253c9cc9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9ffbd9aa4f07cb30d92887e956a9fd43" class="memitem:ga9ffbd9aa4f07cb30d92887e956a9fd43">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_unref_unlocked (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga9ffbd9aa4f07cb30d92887e956a9fd43">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count of a DBusConnection.<br />
</td>
</tr>
<tr class="separator:ga9ffbd9aa4f07cb30d92887e956a9fd43">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabca096431c97f163695515707d5ed508" class="memitem:gabca096431c97f163695515707d5ed508">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_get_next_client_serial (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gabca096431c97f163695515707d5ed508">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocate and return the next non-zero serial number for outgoing messages.<br />
</td>
</tr>
<tr class="separator:gabca096431c97f163695515707d5ed508">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga12756797bd5c1918aa065f9c37ed7bba" class="memitem:ga12756797bd5c1918aa065f9c37ed7bba">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_handle_watch (DBusWatch *watch, unsigned int condition, void *data)</td>
</tr>
<tr class="memdesc:ga12756797bd5c1918aa065f9c37ed7bba">
<td class="mdescLeft"> </td>
<td class="mdescRight">A callback for use with dbus_watch_new() to create a DBusWatch.<br />
</td>
</tr>
<tr class="separator:ga12756797bd5c1918aa065f9c37ed7bba">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadc46f7abfe925f9860fc8c64aeb29ad2" class="memitem:gadc46f7abfe925f9860fc8c64aeb29ad2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_close_possibly_shared (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gadc46f7abfe925f9860fc8c64aeb29ad2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Closes a shared OR private connection, while dbus_connection_close() can only be used on private connections.<br />
</td>
</tr>
<tr class="separator:gadc46f7abfe925f9860fc8c64aeb29ad2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2974eb1c261305fafc635e14fc575d03" class="memitem:ga2974eb1c261305fafc635e14fc575d03">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_send_and_unlock (DBusConnection *connection, DBusMessage *message, dbus_uint32_t *client_serial)</td>
</tr>
<tr class="memdesc:ga2974eb1c261305fafc635e14fc575d03">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like dbus_connection_send(), but assumes the connection is already locked on function entry, and unlocks before returning.<br />
</td>
</tr>
<tr class="separator:ga2974eb1c261305fafc635e14fc575d03">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9f9665902c763bd1ddf9d9bc57d7a7ba" class="memitem:ga9f9665902c763bd1ddf9d9bc57d7a7ba">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_close_if_only_one_ref (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga9f9665902c763bd1ddf9d9bc57d7a7ba">
<td class="mdescLeft"> </td>
<td class="mdescRight">Used internally to handle the semantics of dbus_server_set_new_connection_function().<br />
</td>
</tr>
<tr class="separator:ga9f9665902c763bd1ddf9d9bc57d7a7ba">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad5e725e66dc16a411544e25675fb9fba" class="memitem:gad5e725e66dc16a411544e25675fb9fba">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_block_pending_call (DBusPendingCall *pending)</td>
</tr>
<tr class="memdesc:gad5e725e66dc16a411544e25675fb9fba">
<td class="mdescLeft"> </td>
<td class="mdescRight">Blocks until a pending call times out or gets a reply.<br />
</td>
</tr>
<tr class="separator:gad5e725e66dc16a411544e25675fb9fba">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac6dba97d98f486b87468ae8076349a66" class="memitem:gac6dba97d98f486b87468ae8076349a66">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_get_pending_fds_count (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gac6dba97d98f486b87468ae8076349a66">
<td class="mdescLeft"> </td>
<td class="mdescRight">Return how many file descriptors are pending in the loader.<br />
</td>
</tr>
<tr class="separator:gac6dba97d98f486b87468ae8076349a66">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac84ff2ad1060326f8c1f94a171fefa98" class="memitem:gac84ff2ad1060326f8c1f94a171fefa98">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_set_pending_fds_function (DBusConnection *connection, DBusPendingFdsChangeFunction callback, void *data)</td>
</tr>
<tr class="memdesc:gac84ff2ad1060326f8c1f94a171fefa98">
<td class="mdescLeft"> </td>
<td class="mdescRight">Register a function to be called whenever the number of pending file descriptors in the loader change.<br />
</td>
</tr>
<tr class="separator:gac84ff2ad1060326f8c1f94a171fefa98">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusConnection.

## Typedef Documentation

## ◆ DBusMessageFilter

|                                                    |
|----------------------------------------------------|
| typedef struct DBusMessageFilter DBusMessageFilter |

Internal struct representing a message filter function.

Definition at line 225 of file dbus-connection.c.

## ◆ DBusTimeoutAddFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusTimeoutAddFunction) (DBusTimeoutList \*list, DBusTimeout \*timeout) |

Function to be called in protected_change_timeout() with refcount held.

Definition at line 798 of file dbus-connection.c.

## ◆ DBusTimeoutRemoveFunction

|  |
|----|
| typedef void(\* DBusTimeoutRemoveFunction) (DBusTimeoutList \*list, DBusTimeout \*timeout) |

Function to be called in protected_change_timeout() with refcount held.

Definition at line 801 of file dbus-connection.c.

## ◆ DBusTimeoutToggleFunction

|  |
|----|
| typedef void(\* DBusTimeoutToggleFunction) (DBusTimeoutList \*list, DBusTimeout \*timeout, dbus_bool_t enabled) |

Function to be called in protected_change_timeout() with refcount held.

Definition at line 804 of file dbus-connection.c.

## ◆ DBusWatchAddFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusWatchAddFunction) (DBusWatchList \*list, DBusWatch \*watch) |

Function to be called in protected_change_watch() with refcount held.

Definition at line 674 of file dbus-connection.c.

## ◆ DBusWatchRemoveFunction

|  |
|----|
| typedef void(\* DBusWatchRemoveFunction) (DBusWatchList \*list, DBusWatch \*watch) |

Function to be called in protected_change_watch() with refcount held.

Definition at line 677 of file dbus-connection.c.

## ◆ DBusWatchToggleFunction

|  |
|----|
| typedef void(\* DBusWatchToggleFunction) (DBusWatchList \*list, DBusWatch \*watch, dbus_bool_t enabled) |

Function to be called in protected_change_watch() with refcount held.

Definition at line 680 of file dbus-connection.c.

## Function Documentation

## ◆ \_dbus_connection_add_timeout_unlocked()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_connection_add_timeout_unlocked | ( | DBusConnection \*  | *connection*, |
|  |  | DBusTimeout \*  | *timeout*  |
|  | ) |  |  |

Adds a timeout using the connection's DBusAddTimeoutFunction if available.

Otherwise records the timeout to be added when said function is available. Also re-adds the timeout if the DBusAddTimeoutFunction changes. May fail due to lack of memory. The timeout will fire repeatedly until removed. Connection lock should be held when calling this.

Parameters  
|            |                     |
|------------|---------------------|
| connection | the connection.     |
| timeout    | the timeout to add. |

<!-- -->

Returns  
TRUE on success.

Definition at line 871 of file dbus-connection.c.

References \_dbus_timeout_list_add_timeout(), FALSE, and NULL.

## ◆ \_dbus_connection_add_watch_unlocked()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_connection_add_watch_unlocked | ( | DBusConnection \*  | *connection*, |
|  |  | DBusWatch \*  | *watch*  |
|  | ) |  |  |

Adds a watch using the connection's DBusAddWatchFunction if available.

Otherwise records the watch to be added when said function is available. Also re-adds the watch if the DBusAddWatchFunction changes. May fail due to lack of memory. Connection lock should be held when calling this.

Parameters  
|            |                   |
|------------|-------------------|
| connection | the connection.   |
| watch      | the watch to add. |

<!-- -->

Returns  
TRUE on success.

Definition at line 747 of file dbus-connection.c.

References \_dbus_watch_list_add_watch(), FALSE, and NULL.

## ◆ \_dbus_connection_block_pending_call()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_connection_block_pending_call | ( | DBusPendingCall \*  | *pending* | ) |  |

Blocks until a pending call times out or gets a reply.

Does not re-enter the main loop or run filter/path-registered callbacks. The reply to the message will not be seen by filter callbacks.

Returns immediately if pending call already got a reply.

Parameters  
|         |                                          |
|---------|------------------------------------------|
| pending | the pending call we block for a reply on |

Definition at line 2394 of file dbus-connection.c.

References \_dbus_assert, \_dbus_connection_do_iteration_unlocked(), \_dbus_get_monotonic_time(), \_dbus_pending_call_get_completed_unlocked(), \_dbus_pending_call_get_connection_and_lock(), \_dbus_pending_call_get_reply_serial_unlocked(), \_dbus_pending_call_get_timeout_unlocked(), DBUS_DISPATCH_DATA_REMAINS, DBUS_DISPATCH_NEED_MEMORY, DBUS_ERROR_DISCONNECTED, DBUS_INT64_MODIFIER, dbus_message_unref(), dbus_pending_call_get_completed(), dbus_pending_call_ref(), dbus_pending_call_unref(), dbus_timeout_get_interval(), DBusConnection::disconnect_message_link, and NULL.

Referenced by dbus_pending_call_block().

## ◆ \_dbus_connection_close_if_only_one_ref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_connection_close_if_only_one_ref | ( | DBusConnection \*  | *connection* | ) |  |

Used internally to handle the semantics of dbus_server_set_new_connection_function().

If the new connection function does not ref the connection, we want to close it.

A bit of a hack, probably the new connection function should have returned a value for whether to close, or should have had to close the connection itself if it didn't want it.

But, this works OK as long as the new connection function doesn't do anything crazy like keep the connection around without ref'ing it.

We have to lock the connection across refcount check and close in case the new connection function spawns a thread that closes and unrefs. In that case, if the app thread closes and unrefs first, we'll harmlessly close again; if the app thread still has the ref, we'll close and then the app will close harmlessly. If the app unrefs without closing, the app is broken since if the app refs from the new connection function it is supposed to also close.

If we didn't atomically check the refcount and close with the lock held though, we could screw this up.

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

Definition at line 2160 of file dbus-connection.c.

References \_dbus_assert, \_dbus_atomic_get(), and DBusConnection::refcount.

## ◆ \_dbus_connection_close_possibly_shared()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_connection_close_possibly_shared | ( | DBusConnection \*  | *connection* | ) |  |

Closes a shared OR private connection, while dbus_connection_close() can only be used on private connections.

Should only be called by the dbus code that owns the connection - an owner must be known, the open/close state is like malloc/free, not like ref/unref.

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

Definition at line 1962 of file dbus-connection.c.

References \_dbus_assert, \_dbus_current_generation, and NULL.

## ◆ \_dbus_connection_do_iteration_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_connection_do_iteration_unlocked | ( | DBusConnection \*  | *connection*, |
|  |  | DBusPendingCall \*  | *pending*, |
|  |  | unsigned int  | *flags*, |
|  |  | int  | *timeout_milliseconds*  |
|  | ) |  |  |

Queues incoming messages and sends outgoing messages for this connection, optionally blocking in the process.

Each call to \_dbus_connection_do_iteration_unlocked() will call select() or poll() one time and then read or write data if possible.

The purpose of this function is to be able to flush outgoing messages or queue up incoming messages without returning control to the application and causing reentrancy weirdness.

The flags parameter allows you to specify whether to read incoming messages, write outgoing messages, or both, and whether to block if no immediate action is possible.

The timeout_milliseconds parameter does nothing unless the iteration is blocking.

If there are no outgoing messages and DBUS_ITERATION_DO_READING wasn't specified, then it's impossible to block, even if you specify DBUS_ITERATION_BLOCK; in that case the function returns immediately.

If pending is not NULL then a check is made if the pending call is completed after the io path has been required. If the call has been completed nothing is done. This must be done since the \_dbus_connection_acquire_io_path releases the connection lock for a while.

Called with connection lock held.

Parameters  
|                      |                                                 |
|----------------------|-------------------------------------------------|
| connection           | the connection.                                 |
| pending              | the pending call that should be checked or NULL |
| flags                | iteration flags.                                |
| timeout_milliseconds | maximum blocking time, or -1 for no limit.      |

Definition at line 1202 of file dbus-connection.c.

References \_dbus_pending_call_get_completed_unlocked(), \_dbus_pending_call_get_reply_serial_unlocked(), \_dbus_transport_do_iteration(), DBusConnection::n_outgoing, NULL, and DBusConnection::transport.

Referenced by \_dbus_connection_block_pending_call().

## ◆ \_dbus_connection_get_message_to_send()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusMessage \* \_dbus_connection_get_message_to_send | ( | DBusConnection \*  | *connection* | ) |  |

Gets the next outgoing message.

The message remains in the queue, and the caller does not own a reference to it.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

<!-- -->

Returns  
the message to be sent.

Definition at line 613 of file dbus-connection.c.

References \_dbus_list_get_last(), and DBusConnection::outgoing_messages.

## ◆ \_dbus_connection_get_next_client_serial()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_uint32_t \_dbus_connection_get_next_client_serial | ( | DBusConnection \*  | *connection* | ) |  |

Allocate and return the next non-zero serial number for outgoing messages.

This method is only valid to call from single-threaded code, such as the dbus-daemon, or with the connection lock held.

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
A suitable serial number for the next message to be sent on the connection.

Definition at line 1474 of file dbus-connection.c.

References DBusConnection::client_serial.

Referenced by dbus_connection_send_with_reply().

## ◆ \_dbus_connection_get_pending_fds_count()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| int \_dbus_connection_get_pending_fds_count | ( | DBusConnection \*  | *connection* | ) |  |

Return how many file descriptors are pending in the loader.

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

Definition at line 2577 of file dbus-connection.c.

References \_dbus_transport_get_pending_fds_count(), and DBusConnection::transport.

## ◆ \_dbus_connection_handle_watch()

|                                            |     |               |              |
|--------------------------------------------|-----|---------------|--------------|
| dbus_bool_t \_dbus_connection_handle_watch | (   | DBusWatch \*  | *watch*,     |
|                                            |     | unsigned int  | *condition*, |
|                                            |     | void \*       | *data*       |
|                                            | )   |               |              |

A callback for use with dbus_watch_new() to create a DBusWatch.

Parameters  
|           |                                                              |
|-----------|--------------------------------------------------------------|
| watch     | the watch.                                                   |
| condition | the current condition of the file descriptors being watched. |
| data      | must be a pointer to a DBusConnection                        |

<!-- -->

Returns  
FALSE if the IO condition may not have been fully handled due to lack of memory

Definition at line 1500 of file dbus-connection.c.

References \_dbus_transport_handle_watch(), DBusConnection::transport, and TRUE.

## ◆ \_dbus_connection_has_messages_to_send_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_connection_has_messages_to_send_unlocked | ( | DBusConnection \*  | *connection* | ) |  |

Checks whether there are messages in the outgoing message queue.

Called with connection lock held.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

<!-- -->

Returns  
TRUE if the outgoing queue is non-empty.

Definition at line 576 of file dbus-connection.c.

References NULL, and DBusConnection::outgoing_messages.

Referenced by dbus_connection_has_messages_to_send().

## ◆ \_dbus_connection_lock()

|                             |     |                    |              |     |     |
|-----------------------------|-----|--------------------|--------------|-----|-----|
| void \_dbus_connection_lock | (   | DBusConnection \*  | *connection* | )   |     |

Acquires the connection lock.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

Definition at line 392 of file dbus-connection.c.

Referenced by \_dbus_object_tree_dispatch_and_unlock().

## ◆ \_dbus_connection_message_sent_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_connection_message_sent_unlocked | ( | DBusConnection \*  | *connection*, |
|  |  | DBusMessage \*  | *message*  |
|  | ) |  |  |

Notifies the connection that a message has been sent, so the message can be removed from the outgoing queue.

Called with the connection lock held.

Parameters  
|            |                            |
|------------|----------------------------|
| connection | the connection.            |
| message    | the message that was sent. |

Definition at line 629 of file dbus-connection.c.

References \_dbus_assert, \_dbus_list_get_last_link(), \_dbus_list_prepend_link(), \_dbus_list_unlink(), \_dbus_message_remove_counter(), DBusList::data, dbus_message_get_interface(), dbus_message_get_member(), dbus_message_get_path(), dbus_message_get_signature(), dbus_message_get_type(), dbus_message_type_to_string(), DBusConnection::expired_messages, DBusConnection::n_outgoing, NULL, DBusConnection::outgoing_counter, and DBusConnection::outgoing_messages.

## ◆ \_dbus_connection_new_for_transport()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusConnection \* \_dbus_connection_new_for_transport | ( | DBusTransport \*  | *transport* | ) |  |

Creates a new connection for the given transport.

A transport represents a message stream that uses some concrete mechanism, such as UNIX domain sockets. May return NULL if insufficient memory exists to create the connection.

Parameters  
|           |                |
|-----------|----------------|
| transport | the transport. |

<!-- -->

Returns  
the new connection, or NULL on failure.

Definition at line 1253 of file dbus-connection.c.

References \_dbus_atomic_get(), \_dbus_atomic_inc(), \_dbus_cmutex_free_at_location(), \_dbus_cmutex_new_at_location(), \_dbus_condvar_free_at_location(), \_dbus_condvar_new_at_location(), \_dbus_counter_new(), \_dbus_counter_unref(), \_dbus_current_generation, \_dbus_data_slot_list_init(), \_dbus_disable_sigpipe(), \_dbus_hash_table_new(), \_dbus_hash_table_unref(), \_dbus_list_alloc_link(), \_dbus_list_free_link(), \_dbus_object_tree_new(), \_dbus_object_tree_unref(), \_dbus_rmutex_free_at_location(), \_dbus_rmutex_new_at_location(), \_dbus_timeout_list_free(), \_dbus_timeout_list_new(), \_dbus_transport_ref(), \_dbus_transport_set_connection(), \_dbus_watch_list_free(), \_dbus_watch_list_new(), DBusConnection::builtin_filters_enabled, DBusConnection::client_serial, DBUS_DISPATCH_COMPLETE, dbus_free(), DBUS_HASH_INT, DBUS_INTERFACE_LOCAL, dbus_message_new_signal(), dbus_message_unref(), dbus_new0, DBUS_PATH_LOCAL, DBusConnection::disconnect_message_link, DBusConnection::disconnected_message_arrived, DBusConnection::disconnected_message_processed, DBusConnection::dispatch_cond, DBusConnection::dispatch_mutex, DBusConnection::exit_on_disconnect, FALSE, DBusConnection::filter_list, DBusConnection::io_path_cond, DBusConnection::io_path_mutex, DBusConnection::last_dispatch_status, DBusConnection::mutex, NULL, DBusConnection::objects, DBusConnection::outgoing_counter, DBusConnection::pending_replies, DBusConnection::refcount, DBusConnection::route_peer_messages, DBusConnection::shareable, DBusConnection::slot_list, DBusConnection::slot_mutex, DBusConnection::timeouts, DBusConnection::transport, TRUE, and DBusConnection::watches.

## ◆ \_dbus_connection_queue_received_message_link()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_connection_queue_received_message_link | ( | DBusConnection \*  | *connection*, |
|  |  | DBusList \*  | *link*  |
|  | ) |  |  |

Adds a message-containing list link to the incoming message queue, taking ownership of the link and the message's current refcount.

Cannot fail due to lack of memory.

Parameters  
|            |                            |
|------------|----------------------------|
| connection | the connection.            |
| link       | the message link to queue. |

Definition at line 484 of file dbus-connection.c.

References \_dbus_assert, \_dbus_connection_remove_timeout_unlocked(), \_dbus_hash_table_lookup_int(), \_dbus_list_append_link(), \_dbus_pending_call_get_timeout_unlocked(), \_dbus_pending_call_is_timeout_added_unlocked(), \_dbus_pending_call_set_timeout_added_unlocked(), \_dbus_transport_peek_is_authenticated(), DBusList::data, dbus_message_get_interface(), dbus_message_get_member(), dbus_message_get_path(), dbus_message_get_reply_serial(), dbus_message_get_signature(), dbus_message_get_type(), dbus_message_type_to_string(), FALSE, DBusConnection::incoming_messages, DBusConnection::n_incoming, NULL, DBusConnection::pending_replies, and DBusConnection::transport.

Referenced by \_dbus_transport_queue_messages().

## ◆ \_dbus_connection_queue_synthesized_message_link()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_connection_queue_synthesized_message_link | ( | DBusConnection \*  | *connection*, |
|  |  | DBusList \*  | *link*  |
|  | ) |  |  |

Adds a link + message to the incoming message queue.

Can't fail. Takes ownership of both link and message.

Parameters  
|            |                                     |
|------------|-------------------------------------|
| connection | the connection.                     |
| link       | the list node and message to queue. |

Definition at line 549 of file dbus-connection.c.

References \_dbus_list_append_link(), DBusList::data, DBusConnection::incoming_messages, and DBusConnection::n_incoming.

Referenced by \_dbus_pending_call_queue_timeout_error_unlocked().

## ◆ \_dbus_connection_ref_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusConnection \* \_dbus_connection_ref_unlocked | ( | DBusConnection \*  | *connection* | ) |  |

Increments the reference count of a DBusConnection.

Requires that the caller already holds the connection lock.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

<!-- -->

Returns  
the connection.

Definition at line 1424 of file dbus-connection.c.

References \_dbus_assert, \_dbus_atomic_inc(), \_dbus_current_generation, NULL, and DBusConnection::refcount.

Referenced by \_dbus_object_tree_unregister_and_unlock(), \_dbus_pending_call_new_unlocked(), \_dbus_transport_try_to_authenticate(), and dbus_connection_dispatch().

## ◆ \_dbus_connection_remove_pending_call()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_connection_remove_pending_call | ( | DBusConnection \*  | *connection*, |
|  |  | DBusPendingCall \*  | *pending*  |
|  | ) |  |  |

Removes a pending call from the connection, such that the pending reply will be ignored.

May drop the last reference to the pending call.

Parameters  
|            |                  |
|------------|------------------|
| connection | the connection   |
| pending    | the pending call |

Definition at line 1048 of file dbus-connection.c.

Referenced by dbus_pending_call_cancel().

## ◆ \_dbus_connection_remove_timeout_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_connection_remove_timeout_unlocked | ( | DBusConnection \*  | *connection*, |
|  |  | DBusTimeout \*  | *timeout*  |
|  | ) |  |  |

Removes a timeout using the connection's DBusRemoveTimeoutFunction if available.

It's an error to call this function on a timeout that was not previously added. Connection lock should be held when calling this.

Parameters  
|            |                        |
|------------|------------------------|
| connection | the connection.        |
| timeout    | the timeout to remove. |

Definition at line 889 of file dbus-connection.c.

References \_dbus_timeout_list_remove_timeout(), FALSE, and NULL.

Referenced by \_dbus_connection_queue_received_message_link().

## ◆ \_dbus_connection_remove_watch_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_connection_remove_watch_unlocked | ( | DBusConnection \*  | *connection*, |
|  |  | DBusWatch \*  | *watch*  |
|  | ) |  |  |

Removes a watch using the connection's DBusRemoveWatchFunction if available.

It's an error to call this function on a watch that was not previously added. Connection lock should be held when calling this.

Parameters  
|            |                      |
|------------|----------------------|
| connection | the connection.      |
| watch      | the watch to remove. |

Definition at line 765 of file dbus-connection.c.

References \_dbus_watch_list_remove_watch(), FALSE, and NULL.

## ◆ \_dbus_connection_send_and_unlock()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_connection_send_and_unlock | ( | DBusConnection \*  | *connection*, |
|  |  | DBusMessage \*  | *message*, |
|  |  | dbus_uint32_t \*  | *client_serial*  |
|  | ) |  |  |

Like dbus_connection_send(), but assumes the connection is already locked on function entry, and unlocks before returning.

Parameters  
|               |                                                   |
|---------------|---------------------------------------------------|
| connection    | the connection                                    |
| message       | the message to send                               |
| client_serial | return location for client serial of sent message |

<!-- -->

Returns  
FALSE on out-of-memory

Definition at line 2112 of file dbus-connection.c.

References \_dbus_assert, FALSE, NULL, and TRUE.

Referenced by dbus_connection_send().

## ◆ \_dbus_connection_set_pending_fds_function()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_connection_set_pending_fds_function | ( | DBusConnection \*  | *connection*, |
|  |  | DBusPendingFdsChangeFunction  | *callback*, |
|  |  | void \*  | *data*  |
|  | ) |  |  |

Register a function to be called whenever the number of pending file descriptors in the loader change.

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |
| callback   | the callback   |

Definition at line 2590 of file dbus-connection.c.

References \_dbus_transport_set_pending_fds_function(), and DBusConnection::transport.

## ◆ \_dbus_connection_toggle_timeout_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_connection_toggle_timeout_unlocked | ( | DBusConnection \*  | *connection*, |
|  |  | DBusTimeout \*  | *timeout*, |
|  |  | dbus_bool_t  | *enabled*  |
|  | ) |  |  |

Toggles a timeout and notifies app via connection's DBusTimeoutToggledFunction if available.

It's an error to call this function on a timeout that was not previously added. Connection lock should be held when calling this.

Parameters  
|            |                              |
|------------|------------------------------|
| connection | the connection.              |
| timeout    | the timeout to toggle.       |
| enabled    | whether to enable or disable |

Definition at line 909 of file dbus-connection.c.

References \_dbus_timeout_list_toggle_timeout(), and NULL.

## ◆ \_dbus_connection_toggle_watch_unlocked()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_connection_toggle_watch_unlocked | ( | DBusConnection \*  | *connection*, |
|  |  | DBusWatch \*  | *watch*, |
|  |  | dbus_bool_t  | *enabled*  |
|  | ) |  |  |

Toggles a watch and notifies app via connection's DBusWatchToggledFunction if available.

It's an error to call this function on a watch that was not previously added. Connection lock should be held when calling this.

Parameters  
|            |                              |
|------------|------------------------------|
| connection | the connection.              |
| watch      | the watch to toggle.         |
| enabled    | whether to enable or disable |

Definition at line 785 of file dbus-connection.c.

References \_dbus_assert, \_dbus_watch_list_toggle_watch(), and NULL.

## ◆ \_dbus_connection_unlock()

|                               |     |                    |              |     |     |
|-------------------------------|-----|--------------------|--------------|-----|-----|
| void \_dbus_connection_unlock | (   | DBusConnection \*  | *connection* | )   |     |

Releases the connection lock.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

Definition at line 403 of file dbus-connection.c.

References \_dbus_list_free_link(), \_dbus_list_pop_first_link(), \_dbus_rmutex_unlock(), DBusList::data, dbus_message_unref(), DBusConnection::expired_messages, DBusConnection::mutex, and NULL.

Referenced by \_dbus_object_tree_dispatch_and_unlock(), \_dbus_object_tree_list_registered_and_unlock(), and \_dbus_object_tree_unregister_and_unlock().

## ◆ \_dbus_connection_unref_unlocked()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \_dbus_connection_unref_unlocked | ( | DBusConnection \*  | *connection* | ) |  |

Decrements the reference count of a DBusConnection.

Requires that the caller already holds the connection lock.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

Definition at line 1447 of file dbus-connection.c.

References \_dbus_assert, \_dbus_atomic_dec(), NULL, and DBusConnection::refcount.

Referenced by \_dbus_transport_try_to_authenticate().

## ◆ dbus_connection_has_messages_to_send()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t dbus_connection_has_messages_to_send | ( | DBusConnection \*  | *connection* | ) |  |

Checks whether there are messages in the outgoing message queue.

Use dbus_connection_flush() to block until all outgoing messages have been written to the underlying transport (such as a socket).

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

<!-- -->

Returns  
TRUE if the outgoing queue is non-empty.

Definition at line 592 of file dbus-connection.c.

References \_dbus_connection_has_messages_to_send_unlocked(), FALSE, and NULL.
