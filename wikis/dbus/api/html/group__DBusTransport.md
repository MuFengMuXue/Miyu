DBusTransport object

D-Bus secret internal implementation details

"Backend" for a DBusConnection. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gaa5ece78ea671fe9d9ed17fc6920c9d09" class="memitem:gaa5ece78ea671fe9d9ed17fc6920c9d09">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_init_base (DBusTransport *transport, const DBusTransportVTable *vtable, const DBusString *server_guid, const DBusString *address)</td>
</tr>
<tr class="memdesc:gaa5ece78ea671fe9d9ed17fc6920c9d09">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes the base class members of DBusTransport.<br />
</td>
</tr>
<tr class="separator:gaa5ece78ea671fe9d9ed17fc6920c9d09">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf27a2aceb062921f3915acb1491a646a" class="memitem:gaf27a2aceb062921f3915acb1491a646a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_finalize_base (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:gaf27a2aceb062921f3915acb1491a646a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Finalizes base class members of DBusTransport.<br />
</td>
</tr>
<tr class="separator:gaf27a2aceb062921f3915acb1491a646a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae68c17fdc964c5f2f6348837c83015d1" class="memitem:gae68c17fdc964c5f2f6348837c83015d1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransport * </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_open (DBusAddressEntry *entry, DBusError *error)</td>
</tr>
<tr class="memdesc:gae68c17fdc964c5f2f6348837c83015d1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Try to open a new transport for the given address entry.<br />
</td>
</tr>
<tr class="separator:gae68c17fdc964c5f2f6348837c83015d1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5273234ab54b3b630531e185ec995520" class="memitem:ga5273234ab54b3b630531e185ec995520">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransport * </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_ref (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:ga5273234ab54b3b630531e185ec995520">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count for the transport.<br />
</td>
</tr>
<tr class="separator:ga5273234ab54b3b630531e185ec995520">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab7c53c32a2320c81aae8ce4345762e73" class="memitem:gab7c53c32a2320c81aae8ce4345762e73">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_unref (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:gab7c53c32a2320c81aae8ce4345762e73">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count for the transport.<br />
</td>
</tr>
<tr class="separator:gab7c53c32a2320c81aae8ce4345762e73">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga78444dd8f6c6d6b429433ad81c3e318a" class="memitem:ga78444dd8f6c6d6b429433ad81c3e318a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_disconnect (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:ga78444dd8f6c6d6b429433ad81c3e318a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Closes our end of the connection to a remote application.<br />
</td>
</tr>
<tr class="separator:ga78444dd8f6c6d6b429433ad81c3e318a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaceee4b098b0177870ad934daad90a9c6" class="memitem:gaceee4b098b0177870ad934daad90a9c6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_is_connected (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:gaceee4b098b0177870ad934daad90a9c6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns TRUE if the transport has not been disconnected.<br />
</td>
</tr>
<tr class="separator:gaceee4b098b0177870ad934daad90a9c6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga59ed246ec0ef9c64bc4684fc17726c1d" class="memitem:ga59ed246ec0ef9c64bc4684fc17726c1d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_peek_is_authenticated (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:ga59ed246ec0ef9c64bc4684fc17726c1d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns TRUE if we have been authenticated.<br />
</td>
</tr>
<tr class="separator:ga59ed246ec0ef9c64bc4684fc17726c1d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabe774b134a4bf8c8fc09e6186470874f" class="memitem:gabe774b134a4bf8c8fc09e6186470874f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_try_to_authenticate (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:gabe774b134a4bf8c8fc09e6186470874f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns TRUE if we have been authenticated.<br />
</td>
</tr>
<tr class="separator:gabe774b134a4bf8c8fc09e6186470874f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf0588dd4a6d1c556dd885d4c67622399" class="memitem:gaf0588dd4a6d1c556dd885d4c67622399">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_is_anonymous (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:gaf0588dd4a6d1c556dd885d4c67622399">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_get_is_anonymous().<br />
</td>
</tr>
<tr class="separator:gaf0588dd4a6d1c556dd885d4c67622399">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab98dc7cad59472a4513489628f1393f1" class="memitem:gab98dc7cad59472a4513489628f1393f1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_can_pass_unix_fd (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:gab98dc7cad59472a4513489628f1393f1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns TRUE if the transport supports sending unix fds.<br />
</td>
</tr>
<tr class="separator:gab98dc7cad59472a4513489628f1393f1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga49df85600194f81ae273e569c61df4d3" class="memitem:ga49df85600194f81ae273e569c61df4d3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_address (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:ga49df85600194f81ae273e569c61df4d3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the address of a transport.<br />
</td>
</tr>
<tr class="separator:ga49df85600194f81ae273e569c61df4d3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaee3f3c5c51428cf83d1e08e7c9654dda" class="memitem:gaee3f3c5c51428cf83d1e08e7c9654dda">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_server_id (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:gaee3f3c5c51428cf83d1e08e7c9654dda">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the id of the server we are connected to (see dbus_server_get_id()).<br />
</td>
</tr>
<tr class="separator:gaee3f3c5c51428cf83d1e08e7c9654dda">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4a010098fe079eb6f201ff034d15fdff" class="memitem:ga4a010098fe079eb6f201ff034d15fdff">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_handle_watch (DBusTransport *transport, DBusWatch *watch, unsigned int condition)</td>
</tr>
<tr class="memdesc:ga4a010098fe079eb6f201ff034d15fdff">
<td class="mdescLeft"> </td>
<td class="mdescRight">Handles a watch by reading data, writing data, or disconnecting the transport, as appropriate for the given condition.<br />
</td>
</tr>
<tr class="separator:ga4a010098fe079eb6f201ff034d15fdff">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9aaa3f8bf429c94d4ed180dff36c503c" class="memitem:ga9aaa3f8bf429c94d4ed180dff36c503c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_set_connection (DBusTransport *transport, DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga9aaa3f8bf429c94d4ed180dff36c503c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the connection using this transport.<br />
</td>
</tr>
<tr class="separator:ga9aaa3f8bf429c94d4ed180dff36c503c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga45eb164f4b3bb665f7a094c014b07137" class="memitem:ga45eb164f4b3bb665f7a094c014b07137">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_socket_fd (DBusTransport *transport, DBusSocket *fd_p)</td>
</tr>
<tr class="memdesc:ga45eb164f4b3bb665f7a094c014b07137">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get the socket file descriptor, if any.<br />
</td>
</tr>
<tr class="separator:ga45eb164f4b3bb665f7a094c014b07137">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac5e6d7a01debcf852b8d5a2fbc666fde" class="memitem:gac5e6d7a01debcf852b8d5a2fbc666fde">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_do_iteration (DBusTransport *transport, unsigned int flags, int timeout_milliseconds)</td>
</tr>
<tr class="memdesc:gac5e6d7a01debcf852b8d5a2fbc666fde">
<td class="mdescLeft"> </td>
<td class="mdescRight">Performs a single poll()/select() on the transport's file descriptors and then reads/writes data as appropriate, queueing incoming messages and sending outgoing messages.<br />
</td>
</tr>
<tr class="separator:gac5e6d7a01debcf852b8d5a2fbc666fde">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga32153a834758b5a88d7bde8f7a205c71" class="memitem:ga32153a834758b5a88d7bde8f7a205c71">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDispatchStatus </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_dispatch_status (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:ga32153a834758b5a88d7bde8f7a205c71">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reports our current dispatch status (whether there's buffered data to be queued as messages, or not, or we need memory).<br />
</td>
</tr>
<tr class="separator:ga32153a834758b5a88d7bde8f7a205c71">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4046f36ecbdb75219f2b667f92e75a2b" class="memitem:ga4046f36ecbdb75219f2b667f92e75a2b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_queue_messages (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:ga4046f36ecbdb75219f2b667f92e75a2b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Processes data we've read while handling a watch, potentially converting some of it to messages and queueing those messages on the connection.<br />
</td>
</tr>
<tr class="separator:ga4046f36ecbdb75219f2b667f92e75a2b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga03ea875260e71f59af708146cabf95ab" class="memitem:ga03ea875260e71f59af708146cabf95ab">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_set_max_message_size (DBusTransport *transport, long size)</td>
</tr>
<tr class="memdesc:ga03ea875260e71f59af708146cabf95ab">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_set_max_message_size().<br />
</td>
</tr>
<tr class="separator:ga03ea875260e71f59af708146cabf95ab">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad005fffd646202e74a789765ae82a40f" class="memitem:gad005fffd646202e74a789765ae82a40f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_set_max_message_unix_fds (DBusTransport *transport, long n)</td>
</tr>
<tr class="memdesc:gad005fffd646202e74a789765ae82a40f">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_set_max_message_unix_fds().<br />
</td>
</tr>
<tr class="separator:gad005fffd646202e74a789765ae82a40f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae36d2a90bad6ef13c0379fa9864ff68e" class="memitem:gae36d2a90bad6ef13c0379fa9864ff68e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_max_message_size (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:gae36d2a90bad6ef13c0379fa9864ff68e">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_get_max_message_size().<br />
</td>
</tr>
<tr class="separator:gae36d2a90bad6ef13c0379fa9864ff68e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa28e8edd4d849108b158d95eb7da812d" class="memitem:gaa28e8edd4d849108b158d95eb7da812d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_max_message_unix_fds (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:gaa28e8edd4d849108b158d95eb7da812d">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_get_max_message_unix_fds().<br />
</td>
</tr>
<tr class="separator:gaa28e8edd4d849108b158d95eb7da812d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga08e0368732df5f4e58a2c838fe4484f6" class="memitem:ga08e0368732df5f4e58a2c838fe4484f6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_set_max_received_size (DBusTransport *transport, long size)</td>
</tr>
<tr class="memdesc:ga08e0368732df5f4e58a2c838fe4484f6">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_set_max_received_size().<br />
</td>
</tr>
<tr class="separator:ga08e0368732df5f4e58a2c838fe4484f6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaae297c86eb0b79b6cef4a1f7e4b50356" class="memitem:gaae297c86eb0b79b6cef4a1f7e4b50356">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_set_max_received_unix_fds (DBusTransport *transport, long n)</td>
</tr>
<tr class="memdesc:gaae297c86eb0b79b6cef4a1f7e4b50356">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_set_max_received_unix_fds().<br />
</td>
</tr>
<tr class="separator:gaae297c86eb0b79b6cef4a1f7e4b50356">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8992b33d9060a103bd38705462a0ea96" class="memitem:ga8992b33d9060a103bd38705462a0ea96">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_max_received_size (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:ga8992b33d9060a103bd38705462a0ea96">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_get_max_received_size().<br />
</td>
</tr>
<tr class="separator:ga8992b33d9060a103bd38705462a0ea96">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacd0b2e68c65dc3b0c1cfdf3fb8358a44" class="memitem:gacd0b2e68c65dc3b0c1cfdf3fb8358a44">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_max_received_unix_fds (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:gacd0b2e68c65dc3b0c1cfdf3fb8358a44">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_set_max_received_unix_fds().<br />
</td>
</tr>
<tr class="separator:gacd0b2e68c65dc3b0c1cfdf3fb8358a44">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf3c4a47f73bd584a9fda1e5e7a825da9" class="memitem:gaf3c4a47f73bd584a9fda1e5e7a825da9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_unix_user (DBusTransport *transport, unsigned long *uid)</td>
</tr>
<tr class="memdesc:gaf3c4a47f73bd584a9fda1e5e7a825da9">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_get_unix_user().<br />
</td>
</tr>
<tr class="separator:gaf3c4a47f73bd584a9fda1e5e7a825da9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae66bc81abe904a4b3ab32d8920c8fe1e" class="memitem:gae66bc81abe904a4b3ab32d8920c8fe1e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_unix_process_id (DBusTransport *transport, unsigned long *pid)</td>
</tr>
<tr class="memdesc:gae66bc81abe904a4b3ab32d8920c8fe1e">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_get_unix_process_id().<br />
</td>
</tr>
<tr class="separator:gae66bc81abe904a4b3ab32d8920c8fe1e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga36ccd8321491895ca632e744028eea42" class="memitem:ga36ccd8321491895ca632e744028eea42">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_adt_audit_session_data (DBusTransport *transport, void **data, int *data_size)</td>
</tr>
<tr class="memdesc:ga36ccd8321491895ca632e744028eea42">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_get_adt_audit_session_data().<br />
</td>
</tr>
<tr class="separator:ga36ccd8321491895ca632e744028eea42">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9f0ab472678a107c2ebe7f1da0754c44" class="memitem:ga9f0ab472678a107c2ebe7f1da0754c44">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_set_unix_user_function (DBusTransport *transport, DBusAllowUnixUserFunction function, void *data, DBusFreeFunction free_data_function, void **old_data, DBusFreeFunction *old_free_data_function)</td>
</tr>
<tr class="memdesc:ga9f0ab472678a107c2ebe7f1da0754c44">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_set_unix_user_function().<br />
</td>
</tr>
<tr class="separator:ga9f0ab472678a107c2ebe7f1da0754c44">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9e85485f9e0cdf2241aa07352eca0465" class="memitem:ga9e85485f9e0cdf2241aa07352eca0465">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_linux_security_label (DBusTransport *transport, char **label_p)</td>
</tr>
<tr class="separator:ga9e85485f9e0cdf2241aa07352eca0465">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga92b217ea3d54bd8de725780fd9314d0a" class="memitem:ga92b217ea3d54bd8de725780fd9314d0a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_credentials (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:ga92b217ea3d54bd8de725780fd9314d0a">
<td class="mdescLeft"> </td>
<td class="mdescRight">If the transport has already been authenticated, return its credentials.<br />
</td>
</tr>
<tr class="separator:ga92b217ea3d54bd8de725780fd9314d0a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3f4f4ce9eaef18567fd21f5c6a1fde99" class="memitem:ga3f4f4ce9eaef18567fd21f5c6a1fde99">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_windows_user (DBusTransport *transport, char **windows_sid_p)</td>
</tr>
<tr class="memdesc:ga3f4f4ce9eaef18567fd21f5c6a1fde99">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_get_windows_user().<br />
</td>
</tr>
<tr class="separator:ga3f4f4ce9eaef18567fd21f5c6a1fde99">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadbf528ef41efde73d0bc386d10b7f5b1" class="memitem:gadbf528ef41efde73d0bc386d10b7f5b1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_set_windows_user_function (DBusTransport *transport, DBusAllowWindowsUserFunction function, void *data, DBusFreeFunction free_data_function, void **old_data, DBusFreeFunction *old_free_data_function)</td>
</tr>
<tr class="memdesc:gadbf528ef41efde73d0bc386d10b7f5b1">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_set_windows_user_function().<br />
</td>
</tr>
<tr class="separator:gadbf528ef41efde73d0bc386d10b7f5b1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga345827326824547201e8c517474af135" class="memitem:ga345827326824547201e8c517474af135">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_set_auth_mechanisms (DBusTransport *transport, const char **mechanisms)</td>
</tr>
<tr class="memdesc:ga345827326824547201e8c517474af135">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the SASL authentication mechanisms supported by this transport.<br />
</td>
</tr>
<tr class="separator:ga345827326824547201e8c517474af135">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5f4bd7eb5621003595b75cb8033463cd" class="memitem:ga5f4bd7eb5621003595b75cb8033463cd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_set_allow_anonymous (DBusTransport *transport, dbus_bool_t value)</td>
</tr>
<tr class="memdesc:ga5f4bd7eb5621003595b75cb8033463cd">
<td class="mdescLeft"> </td>
<td class="mdescRight">See dbus_connection_set_allow_anonymous()<br />
</td>
</tr>
<tr class="separator:ga5f4bd7eb5621003595b75cb8033463cd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3545c064545957f73f583bf63d07c40c" class="memitem:ga3545c064545957f73f583bf63d07c40c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_get_pending_fds_count (DBusTransport *transport)</td>
</tr>
<tr class="memdesc:ga3545c064545957f73f583bf63d07c40c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Return how many file descriptors are pending in the loader.<br />
</td>
</tr>
<tr class="separator:ga3545c064545957f73f583bf63d07c40c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad6dccbcdc149e3305101db4b2ebae6d6" class="memitem:gad6dccbcdc149e3305101db4b2ebae6d6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_transport_set_pending_fds_function (DBusTransport *transport, void(*callback)(void *), void *data)</td>
</tr>
<tr class="memdesc:gad6dccbcdc149e3305101db4b2ebae6d6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Register a function to be called whenever the number of pending file descriptors in the loader change.<br />
</td>
</tr>
<tr class="separator:gad6dccbcdc149e3305101db4b2ebae6d6">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

"Backend" for a DBusConnection.

Types and functions related to DBusTransport. A transport is an abstraction that can send and receive data via various kinds of network connections or other IPC mechanisms.

## Function Documentation

## ◆ \_dbus_transport_can_pass_unix_fd()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_transport_can_pass_unix_fd | ( | DBusTransport \*  | *transport* | ) |  |

Returns TRUE if the transport supports sending unix fds.

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
TRUE if TRUE it is possible to send unix fds across the transport.

Definition at line 861 of file dbus-transport.c.

Referenced by dbus_connection_can_send_type(), dbus_connection_send(), dbus_connection_send_preallocated(), dbus_connection_send_with_reply(), and dbus_connection_send_with_reply_and_block().

## ◆ \_dbus_transport_disconnect()

|                                  |     |                   |             |     |     |
|----------------------------------|-----|-------------------|-------------|-----|-----|
| void \_dbus_transport_disconnect | (   | DBusTransport \*  | *transport* | )   |     |

Closes our end of the connection to a remote application.

Further attempts to use this transport will fail. Only the first call to \_dbus_transport_disconnect() will have an effect.

Parameters  
|           |                |
|-----------|----------------|
| transport | the transport. |

Definition at line 511 of file dbus-transport.c.

References \_dbus_assert, DBusTransportVTable::disconnect, disconnected, NULL, TRUE, and vtable.

Referenced by \_dbus_transport_finalize_base(), \_dbus_transport_queue_messages(), and \_dbus_transport_try_to_authenticate().

## ◆ \_dbus_transport_do_iteration()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_transport_do_iteration | ( | DBusTransport \*  | *transport*, |
|  |  | unsigned int  | *flags*, |
|  |  | int  | *timeout_milliseconds*  |
|  | ) |  |  |

Performs a single poll()/select() on the transport's file descriptors and then reads/writes data as appropriate, queueing incoming messages and sending outgoing messages.

This is the backend for \_dbus_connection_do_iteration(). See \_dbus_connection_do_iteration() for full details.

Parameters  
|  |  |
|----|----|
| transport | the transport. |
| flags | indicates whether to read or write, and whether to block. |
| timeout_milliseconds | if blocking, timeout or -1 for no timeout. |

Definition at line 1002 of file dbus-transport.c.

References \_dbus_assert, \_dbus_transport_ref(), \_dbus_transport_unref(), disconnected, DBusTransportVTable::do_iteration, NULL, and vtable.

Referenced by \_dbus_connection_do_iteration_unlocked().

## ◆ \_dbus_transport_finalize_base()

|                                     |     |                   |             |     |     |
|-------------------------------------|-----|-------------------|-------------|-----|-----|
| void \_dbus_transport_finalize_base | (   | DBusTransport \*  | *transport* | )   |     |

Finalizes base class members of DBusTransport.

Chained up to from subclass finalizers.

Parameters  
|           |                |
|-----------|----------------|
| transport | the transport. |

Definition at line 218 of file dbus-transport.c.

References \_dbus_auth_unref(), \_dbus_counter_set_notify(), \_dbus_counter_unref(), \_dbus_credentials_unref(), \_dbus_message_loader_unref(), \_dbus_transport_disconnect(), address, auth, credentials, dbus_free(), disconnected, expected_guid, free_unix_user_data, free_windows_user_data, live_messages, loader, NULL, unix_user_data, and windows_user_data.

## ◆ \_dbus_transport_get_address()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| const char \* \_dbus_transport_get_address | ( | DBusTransport \*  | *transport* | ) |  |

Gets the address of a transport.

It will be NULL for a server-side transport.

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
transport's address

Definition at line 874 of file dbus-transport.c.

References address.

## ◆ \_dbus_transport_get_adt_audit_session_data()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_transport_get_adt_audit_session_data | ( | DBusTransport \*  | *transport*, |
|  |  | void \*\*  | *data*, |
|  |  | int \*  | *data_size*  |
|  | ) |  |  |

See dbus_connection_get_adt_audit_session_data().

Parameters  
|           |                                        |
|-----------|----------------------------------------|
| transport | the transport                          |
| data      | return location for the ADT audit data |
| data_size | return length of audit data            |

<!-- -->

Returns  
TRUE if audit data is filled in with a valid ucred

Definition at line 1403 of file dbus-transport.c.

References \_dbus_auth_get_identity(), \_dbus_credentials_get_adt_audit_data(), \_dbus_credentials_get_adt_audit_data_size(), \_dbus_credentials_include(), auth, authenticated, FALSE, NULL, and TRUE.

Referenced by dbus_connection_get_adt_audit_session_data().

## ◆ \_dbus_transport_get_credentials()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusCredentials \* \_dbus_transport_get_credentials | ( | DBusTransport \*  | *transport* | ) |  |

If the transport has already been authenticated, return its credentials.

If not, return NULL.

The caller must ref the returned credentials object if it wants to keep it.

Definition at line 1489 of file dbus-transport.c.

References \_dbus_auth_get_identity(), auth, authenticated, and FALSE.

## ◆ \_dbus_transport_get_dispatch_status()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusDispatchStatus \_dbus_transport_get_dispatch_status | ( | DBusTransport \*  | *transport* | ) |  |

Reports our current dispatch status (whether there's buffered data to be queued as messages, or not, or we need memory).

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
current status

Definition at line 1127 of file dbus-transport.c.

References \_dbus_auth_do_work(), \_dbus_counter_get_size_value(), \_dbus_counter_get_unix_fd_value(), \_dbus_message_loader_peek_message(), \_dbus_message_loader_queue_messages(), \_dbus_transport_try_to_authenticate(), auth, DBUS_DISPATCH_COMPLETE, DBUS_DISPATCH_DATA_REMAINS, DBUS_DISPATCH_NEED_MEMORY, live_messages, loader, max_live_messages_size, max_live_messages_unix_fds, NULL, TRUE, and unused_bytes_recovered.

Referenced by \_dbus_transport_queue_messages().

## ◆ \_dbus_transport_get_is_anonymous()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_transport_get_is_anonymous | ( | DBusTransport \*  | *transport* | ) |  |

See dbus_connection_get_is_anonymous().

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
TRUE if not authenticated or authenticated as anonymous

Definition at line 839 of file dbus-transport.c.

References \_dbus_auth_get_identity(), \_dbus_credentials_are_anonymous(), auth, authenticated, FALSE, and TRUE.

Referenced by dbus_connection_get_is_anonymous().

## ◆ \_dbus_transport_get_is_connected()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_transport_get_is_connected | ( | DBusTransport \*  | *transport* | ) |  |

Returns TRUE if the transport has not been disconnected.

Disconnection can result from \_dbus_transport_disconnect() or because the server drops its end of the connection.

Parameters  
|           |                |
|-----------|----------------|
| transport | the transport. |

<!-- -->

Returns  
whether we're connected

Definition at line 536 of file dbus-transport.c.

References disconnected.

Referenced by dbus_connection_unref().

## ◆ \_dbus_transport_get_linux_security_label()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_transport_get_linux_security_label | ( | DBusTransport \*  | *transport*, |
|  |  | char \*\*  | *label_p*  |
|  | ) |  |  |

Definition at line 1455 of file dbus-transport.c.

## ◆ \_dbus_transport_get_max_message_size()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| long \_dbus_transport_get_max_message_size | ( | DBusTransport \*  | *transport* | ) |  |

See dbus_connection_get_max_message_size().

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
max message size

Definition at line 1251 of file dbus-transport.c.

References \_dbus_message_loader_get_max_message_size(), and loader.

Referenced by dbus_connection_get_max_message_size().

## ◆ \_dbus_transport_get_max_message_unix_fds()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| long \_dbus_transport_get_max_message_unix_fds | ( | DBusTransport \*  | *transport* | ) |  |

See dbus_connection_get_max_message_unix_fds().

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
max message unix fds

Definition at line 1263 of file dbus-transport.c.

References \_dbus_message_loader_get_max_message_unix_fds(), and loader.

Referenced by dbus_connection_get_max_message_unix_fds().

## ◆ \_dbus_transport_get_max_received_size()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| long \_dbus_transport_get_max_received_size | ( | DBusTransport \*  | *transport* | ) |  |

See dbus_connection_get_max_received_size().

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
max bytes for all live messages

Definition at line 1311 of file dbus-transport.c.

References max_live_messages_size.

Referenced by dbus_connection_get_max_received_size().

## ◆ \_dbus_transport_get_max_received_unix_fds()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| long \_dbus_transport_get_max_received_unix_fds | ( | DBusTransport \*  | *transport* | ) |  |

See dbus_connection_set_max_received_unix_fds().

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
max unix fds for all live messages

Definition at line 1323 of file dbus-transport.c.

References max_live_messages_unix_fds.

Referenced by dbus_connection_get_max_received_unix_fds().

## ◆ \_dbus_transport_get_pending_fds_count()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| int \_dbus_transport_get_pending_fds_count | ( | DBusTransport \*  | *transport* | ) |  |

Return how many file descriptors are pending in the loader.

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

Definition at line 1590 of file dbus-transport.c.

References \_dbus_message_loader_get_pending_fds_count(), and loader.

Referenced by \_dbus_connection_get_pending_fds_count().

## ◆ \_dbus_transport_get_server_id()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| const char \* \_dbus_transport_get_server_id | ( | DBusTransport \*  | *transport* | ) |  |

Gets the id of the server we are connected to (see dbus_server_get_id()).

Only works on client side.

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
transport's server's id or NULL if we are the server side

Definition at line 887 of file dbus-transport.c.

References \_dbus_auth_get_guid_from_server(), auth, authenticated, expected_guid, is_server, and NULL.

Referenced by dbus_connection_get_server_id().

## ◆ \_dbus_transport_get_socket_fd()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_transport_get_socket_fd | ( | DBusTransport \*  | *transport*, |
|  |  | DBusSocket \*  | *fd_p*  |
|  | ) |  |  |

Get the socket file descriptor, if any.

Parameters  
|           |                                        |
|-----------|----------------------------------------|
| transport | the transport                          |
| fd_p      | pointer to fill in with the descriptor |

<!-- -->

Returns  
TRUE if a descriptor was available

Definition at line 969 of file dbus-transport.c.

References \_dbus_transport_ref(), \_dbus_transport_unref(), disconnected, FALSE, DBusTransportVTable::get_socket_fd, NULL, and vtable.

Referenced by dbus_connection_get_socket().

## ◆ \_dbus_transport_get_unix_process_id()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_transport_get_unix_process_id | ( | DBusTransport \*  | *transport*, |
|  |  | unsigned long \*  | *pid*  |
|  | ) |  |  |

See dbus_connection_get_unix_process_id().

Parameters  
|           |                                    |
|-----------|------------------------------------|
| transport | the transport                      |
| pid       | return location for the process ID |

<!-- -->

Returns  
TRUE if uid is filled in with a valid process ID

Definition at line 1369 of file dbus-transport.c.

References \_dbus_auth_get_identity(), \_dbus_credentials_get_pid(), \_dbus_credentials_include(), auth, authenticated, DBUS_PID_UNSET, FALSE, and TRUE.

Referenced by dbus_connection_get_unix_process_id().

## ◆ \_dbus_transport_get_unix_user()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_transport_get_unix_user | ( | DBusTransport \*  | *transport*, |
|  |  | unsigned long \*  | *uid*  |
|  | ) |  |  |

See dbus_connection_get_unix_user().

Parameters  
|           |                                 |
|-----------|---------------------------------|
| transport | the transport                   |
| uid       | return location for the user ID |

<!-- -->

Returns  
TRUE if uid is filled in with a valid user ID

Definition at line 1336 of file dbus-transport.c.

References \_dbus_auth_get_identity(), \_dbus_credentials_get_unix_uid(), \_dbus_credentials_include(), \_DBUS_INT32_MAX, auth, authenticated, FALSE, and TRUE.

Referenced by dbus_connection_get_unix_user().

## ◆ \_dbus_transport_get_windows_user()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_transport_get_windows_user | ( | DBusTransport \*  | *transport*, |
|  |  | char \*\*  | *windows_sid_p*  |
|  | ) |  |  |

See dbus_connection_get_windows_user().

Parameters  
|               |                                 |
|---------------|---------------------------------|
| transport     | the transport                   |
| windows_sid_p | return location for the user ID |

<!-- -->

Returns  
TRUE if user is available; the returned value may still be NULL if no memory to copy it

Definition at line 1505 of file dbus-transport.c.

References \_dbus_auth_get_identity(), \_dbus_credentials_get_windows_sid(), \_dbus_credentials_include(), \_dbus_strdup(), auth, authenticated, FALSE, NULL, and TRUE.

Referenced by dbus_connection_get_windows_user().

## ◆ \_dbus_transport_handle_watch()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_transport_handle_watch | ( | DBusTransport \*  | *transport*, |
|  |  | DBusWatch \*  | *watch*, |
|  |  | unsigned int  | *condition*  |
|  | ) |  |  |

Handles a watch by reading data, writing data, or disconnecting the transport, as appropriate for the given condition.

Parameters  
|           |                                                   |
|-----------|---------------------------------------------------|
| transport | the transport.                                    |
| watch     | the watch.                                        |
| condition | the current state of the watched file descriptor. |

<!-- -->

Returns  
FALSE if not enough memory to fully handle the watch

Definition at line 907 of file dbus-transport.c.

References \_dbus_assert, \_dbus_transport_ref(), \_dbus_transport_unref(), \_dbus_warn_check_failed(), \_dbus_watch_ref(), \_dbus_watch_sanitize_condition(), \_dbus_watch_unref(), dbus_watch_get_socket(), disconnected, DBusTransportVTable::handle_watch, NULL, TRUE, and vtable.

Referenced by \_dbus_connection_handle_watch().

## ◆ \_dbus_transport_init_base()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_transport_init_base | ( | DBusTransport \*  | *transport*, |
|  |  | const DBusTransportVTable \*  | *vtable*, |
|  |  | const DBusString \*  | *server_guid*, |
|  |  | const DBusString \*  | *address*  |
|  | ) |  |  |

Initializes the base class members of DBusTransport.

Chained up to by subclasses in their constructor. The server GUID is the globally unique ID for the server creating this connection and will be NULL for the client side of a connection. The GUID is in hex format.

Parameters  
|  |  |
|----|----|
| transport | the transport being created. |
| vtable | the subclass vtable. |
| server_guid | non-NULL if this transport is on the server side of a connection |
| address | the address of the transport |

<!-- -->

Returns  
TRUE on success.

Definition at line 104 of file dbus-transport.c.

References \_dbus_assert, \_dbus_auth_client_new(), \_dbus_auth_server_new(), \_dbus_auth_unref(), \_dbus_counter_new(), \_dbus_counter_set_notify(), \_dbus_counter_unref(), \_dbus_credentials_new(), \_dbus_credentials_unref(), \_dbus_message_loader_new(), \_dbus_message_loader_unref(), \_dbus_string_copy_data(), address, auth, authenticated, credentials, disconnected, expected_guid, FALSE, free_unix_user_data, free_windows_user_data, is_server, live_messages, loader, max_live_messages_size, max_live_messages_unix_fds, NULL, receive_credentials_pending, refcount, send_credentials_pending, TRUE, unix_user_data, unix_user_function, vtable, windows_user_data, and windows_user_function.

Referenced by \_dbus_transport_new_for_socket().

## ◆ \_dbus_transport_open()

|                                        |     |                      |          |
|----------------------------------------|-----|----------------------|----------|
| DBusTransport \* \_dbus_transport_open | (   | DBusAddressEntry \*  | *entry*, |
|                                        |     | DBusError \*         | *error*  |
|                                        | )   |                      |          |

Try to open a new transport for the given address entry.

(This opens a client-side-of-the-connection transport.)

Parameters  
|       |                                       |
|-------|---------------------------------------|
| entry | the address entry                     |
| error | location to store reason for failure. |

<!-- -->

Returns  
new transport of NULL on failure.

Definition at line 373 of file dbus-transport.c.

References \_dbus_assert_not_reached, \_DBUS_N_ELEMENTS, \_dbus_set_bad_address(), \_dbus_strdup(), dbus_address_entry_get_value(), DBUS_ERROR_INIT, dbus_error_is_set(), dbus_free(), dbus_move_error(), expected_guid, and NULL.

## ◆ \_dbus_transport_peek_is_authenticated()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_transport_peek_is_authenticated | ( | DBusTransport \*  | *transport* | ) |  |

Returns TRUE if we have been authenticated.

It will return TRUE even if the transport is now disconnected, but was ever authenticated before disconnecting.

This replaces the older \_dbus_transport_get_is_authenticated() which had side-effects.

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
whether we're authenticated

Definition at line 710 of file dbus-transport.c.

References authenticated.

Referenced by \_dbus_connection_queue_received_message_link().

## ◆ \_dbus_transport_queue_messages()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_transport_queue_messages | ( | DBusTransport \*  | *transport* | ) |  |

Processes data we've read while handling a watch, potentially converting some of it to messages and queueing those messages on the connection.

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
TRUE if we had enough memory to queue all messages

Definition at line 1166 of file dbus-transport.c.

References \_dbus_assert, \_dbus_connection_queue_received_message_link(), \_dbus_message_add_counter(), \_dbus_message_loader_get_is_corrupted(), \_dbus_message_loader_pop_message_link(), \_dbus_message_loader_putback_message_link(), \_dbus_transport_disconnect(), \_dbus_transport_get_dispatch_status(), connection, DBusList::data, DBUS_DISPATCH_DATA_REMAINS, DBUS_DISPATCH_NEED_MEMORY, live_messages, DBusTransportVTable::live_messages_changed, loader, NULL, and vtable.

## ◆ \_dbus_transport_ref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusTransport \* \_dbus_transport_ref | ( | DBusTransport \*  | *transport* | ) |  |

Increments the reference count for the transport.

Parameters  
|           |                |
|-----------|----------------|
| transport | the transport. |

<!-- -->

Returns  
the transport.

Definition at line 469 of file dbus-transport.c.

References \_dbus_assert, and refcount.

Referenced by \_dbus_connection_new_for_transport(), \_dbus_transport_do_iteration(), \_dbus_transport_get_socket_fd(), \_dbus_transport_handle_watch(), and \_dbus_transport_set_connection().

## ◆ \_dbus_transport_set_allow_anonymous()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_transport_set_allow_anonymous | ( | DBusTransport \*  | *transport*, |
|  |  | dbus_bool_t  | *value*  |
|  | ) |  |  |

See dbus_connection_set_allow_anonymous()

Parameters  
|           |                                    |
|-----------|------------------------------------|
| transport | the transport                      |
| value     | TRUE to allow anonymous connection |

Definition at line 1578 of file dbus-transport.c.

References allow_anonymous, and FALSE.

Referenced by dbus_connection_set_allow_anonymous().

## ◆ \_dbus_transport_set_auth_mechanisms()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_transport_set_auth_mechanisms | ( | DBusTransport \*  | *transport*, |
|  |  | const char \*\*  | *mechanisms*  |
|  | ) |  |  |

Sets the SASL authentication mechanisms supported by this transport.

Parameters  
|            |                                         |
|------------|-----------------------------------------|
| transport  | the transport                           |
| mechanisms | the NULL-terminated array of mechanisms |

<!-- -->

Returns  
FALSE if no memory

Definition at line 1565 of file dbus-transport.c.

References \_dbus_auth_set_mechanisms(), and auth.

## ◆ \_dbus_transport_set_connection()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_transport_set_connection | ( | DBusTransport \*  | *transport*, |
|  |  | DBusConnection \*  | *connection*  |
|  | ) |  |  |

Sets the connection using this transport.

Allows the transport to add watches to the connection, queue incoming messages, and pull outgoing messages.

Parameters  
|            |                 |
|------------|-----------------|
| transport  | the transport.  |
| connection | the connection. |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 945 of file dbus-transport.c.

References \_dbus_assert, \_dbus_transport_ref(), \_dbus_transport_unref(), connection, DBusTransportVTable::connection_set, NULL, and vtable.

Referenced by \_dbus_connection_new_for_transport().

## ◆ \_dbus_transport_set_max_message_size()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_transport_set_max_message_size | ( | DBusTransport \*  | *transport*, |
|  |  | long  | *size*  |
|  | ) |  |  |

See dbus_connection_set_max_message_size().

Parameters  
|           |                                  |
|-----------|----------------------------------|
| transport | the transport                    |
| size      | the max size of a single message |

Definition at line 1225 of file dbus-transport.c.

References \_dbus_message_loader_set_max_message_size(), and loader.

Referenced by dbus_connection_set_max_message_size().

## ◆ \_dbus_transport_set_max_message_unix_fds()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_transport_set_max_message_unix_fds | ( | DBusTransport \*  | *transport*, |
|  |  | long  | *n*  |
|  | ) |  |  |

See dbus_connection_set_max_message_unix_fds().

Parameters  
|           |                                                |
|-----------|------------------------------------------------|
| transport | the transport                                  |
| n         | the max number of unix fds of a single message |

Definition at line 1238 of file dbus-transport.c.

References \_dbus_message_loader_set_max_message_unix_fds(), and loader.

Referenced by dbus_connection_set_max_message_unix_fds().

## ◆ \_dbus_transport_set_max_received_size()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_transport_set_max_received_size | ( | DBusTransport \*  | *transport*, |
|  |  | long  | *size*  |
|  | ) |  |  |

See dbus_connection_set_max_received_size().

Parameters  
|           |                                       |
|-----------|---------------------------------------|
| transport | the transport                         |
| size      | the max size of all incoming messages |

Definition at line 1275 of file dbus-transport.c.

References \_dbus_counter_set_notify(), live_messages, max_live_messages_size, and max_live_messages_unix_fds.

Referenced by dbus_connection_set_max_received_size().

## ◆ \_dbus_transport_set_max_received_unix_fds()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_transport_set_max_received_unix_fds | ( | DBusTransport \*  | *transport*, |
|  |  | long  | *n*  |
|  | ) |  |  |

See dbus_connection_set_max_received_unix_fds().

Parameters  
|           |                                           |
|-----------|-------------------------------------------|
| transport | the transport                             |
| n         | the max unix fds of all incoming messages |

Definition at line 1293 of file dbus-transport.c.

References \_dbus_counter_set_notify(), live_messages, max_live_messages_size, and max_live_messages_unix_fds.

Referenced by dbus_connection_set_max_received_unix_fds().

## ◆ \_dbus_transport_set_pending_fds_function()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_transport_set_pending_fds_function | ( | DBusTransport \*  | *transport*, |
|  |  | void(\*)(void \*)  | *callback*, |
|  |  | void \*  | *data*  |
|  | ) |  |  |

Register a function to be called whenever the number of pending file descriptors in the loader change.

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |
| callback  | the callback  |

Definition at line 1603 of file dbus-transport.c.

References \_dbus_message_loader_set_pending_fds_function(), and loader.

Referenced by \_dbus_connection_set_pending_fds_function().

## ◆ \_dbus_transport_set_unix_user_function()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_transport_set_unix_user_function | ( | DBusTransport \*  | *transport*, |
|  |  | DBusAllowUnixUserFunction  | *function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*, |
|  |  | void \*\*  | *old_data*, |
|  |  | DBusFreeFunction \*  | *old_free_data_function*  |
|  | ) |  |  |

See dbus_connection_set_unix_user_function().

Parameters  
|                        |                                        |
|------------------------|----------------------------------------|
| transport              | the transport                          |
| function               | the predicate                          |
| data                   | data to pass to the predicate          |
| free_data_function     | function to free the data              |
| old_data               | the old user data to be freed          |
| old_free_data_function | old free data function to free it with |

Definition at line 1439 of file dbus-transport.c.

References free_unix_user_data, unix_user_data, and unix_user_function.

Referenced by dbus_connection_set_unix_user_function().

## ◆ \_dbus_transport_set_windows_user_function()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_transport_set_windows_user_function | ( | DBusTransport \*  | *transport*, |
|  |  | DBusAllowWindowsUserFunction  | *function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*, |
|  |  | void \*\*  | *old_data*, |
|  |  | DBusFreeFunction \*  | *old_free_data_function*  |
|  | ) |  |  |

See dbus_connection_set_windows_user_function().

Parameters  
|                        |                                        |
|------------------------|----------------------------------------|
| transport              | the transport                          |
| function               | the predicate                          |
| data                   | data to pass to the predicate          |
| free_data_function     | function to free the data              |
| old_data               | the old user data to be freed          |
| old_free_data_function | old free data function to free it with |

Definition at line 1541 of file dbus-transport.c.

References free_windows_user_data, windows_user_data, and windows_user_function.

Referenced by dbus_connection_set_windows_user_function().

## ◆ \_dbus_transport_try_to_authenticate()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_transport_try_to_authenticate | ( | DBusTransport \*  | *transport* | ) |  |

Returns TRUE if we have been authenticated.

It will return TRUE even if the transport is now disconnected, but was ever authenticated before disconnecting.

If we have not finished authenticating, but we have enough buffered input to finish the job, then this function will do so before it returns.

This used to be called \_dbus_transport_get_is_authenticated(), but that name seems inappropriate for a function with side-effects.

Parameters  
|           |               |
|-----------|---------------|
| transport | the transport |

<!-- -->

Returns  
whether we're authenticated

Definition at line 733 of file dbus-transport.c.

References \_dbus_assert, \_dbus_assert_not_reached, \_dbus_auth_do_work(), \_dbus_auth_get_guid_from_server(), \_dbus_auth_get_identity(), \_dbus_connection_ref_unlocked(), \_dbus_connection_unref_unlocked(), \_dbus_credentials_include(), \_dbus_transport_disconnect(), auth, authenticated, connection, disconnected, expected_guid, FALSE, is_server, NULL, receive_credentials_pending, send_credentials_pending, TRUE, unix_user_function, and windows_user_function.

Referenced by \_dbus_transport_get_dispatch_status(), dbus_connection_get_adt_audit_session_data(), dbus_connection_get_is_authenticated(), dbus_connection_get_unix_process_id(), dbus_connection_get_unix_user(), and dbus_connection_get_windows_user().

## ◆ \_dbus_transport_unref()

|                             |     |                   |             |     |     |
|-----------------------------|-----|-------------------|-------------|-----|-----|
| void \_dbus_transport_unref | (   | DBusTransport \*  | *transport* | )   |     |

Decrements the reference count for the transport.

Disconnects and finalizes the transport if the reference count reaches zero.

Parameters  
|           |                |
|-----------|----------------|
| transport | the transport. |

Definition at line 486 of file dbus-transport.c.

References \_dbus_assert, DBusTransportVTable::finalize, NULL, refcount, and vtable.

Referenced by \_dbus_transport_do_iteration(), \_dbus_transport_get_socket_fd(), \_dbus_transport_handle_watch(), and \_dbus_transport_set_connection().

## Variable Documentation

## ◆ \[\]

|  |
|----|
| DBusTransportOpenResult(\* { ... } ::func) (DBusAddressEntry \*entry, DBusTransport \*\*transport_p, DBusError \*error) |

Definition at line 348 of file dbus-transport.c.
