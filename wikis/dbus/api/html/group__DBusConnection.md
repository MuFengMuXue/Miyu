DBusConnection

D-Bus low-level public API

Connection to another application. More...

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
<td class="memItemRight" data-valign="bottom">DBusObjectPathVTable</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Virtual table that must be implemented to handle a portion of the object path hierarchy. More...<br />
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
<tr id="r_gae2725c803bf1747fe8524a84383ae911" class="memitem:gae2725c803bf1747fe8524a84383ae911">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusWatch </td>
<td class="memItemRight" data-valign="bottom">DBusWatch</td>
</tr>
<tr class="separator:gae2725c803bf1747fe8524a84383ae911">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaee36600f1d7a916cb981c4cf6195de0a" class="memitem:gaee36600f1d7a916cb981c4cf6195de0a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusTimeout </td>
<td class="memItemRight" data-valign="bottom">DBusTimeout</td>
</tr>
<tr class="separator:gaee36600f1d7a916cb981c4cf6195de0a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaadc8a802cfffb0719d394609d9cd2186" class="memitem:gaadc8a802cfffb0719d394609d9cd2186">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusPreallocatedSend </td>
<td class="memItemRight" data-valign="bottom">DBusPreallocatedSend</td>
</tr>
<tr class="memdesc:gaadc8a802cfffb0719d394609d9cd2186">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque type representing preallocated resources so a message can be sent without further memory allocation.<br />
</td>
</tr>
<tr class="separator:gaadc8a802cfffb0719d394609d9cd2186">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf2d0684d2edd8174819af46060fbf38f" class="memitem:gaf2d0684d2edd8174819af46060fbf38f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusPendingCall </td>
<td class="memItemRight" data-valign="bottom">DBusPendingCall</td>
</tr>
<tr class="memdesc:gaf2d0684d2edd8174819af46060fbf38f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque type representing a method call that has not yet received a reply.<br />
</td>
</tr>
<tr class="separator:gaf2d0684d2edd8174819af46060fbf38f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga168c25556d88c296ebc64f1d7b20f699" class="memitem:ga168c25556d88c296ebc64f1d7b20f699">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusConnection </td>
<td class="memItemRight" data-valign="bottom">DBusConnection</td>
</tr>
<tr class="memdesc:ga168c25556d88c296ebc64f1d7b20f699">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opaque type representing a connection to a remote application and associated incoming/outgoing message queues.<br />
</td>
</tr>
<tr class="separator:ga168c25556d88c296ebc64f1d7b20f699">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4dd10016d1f17d1a2fbf0ad913c90427" class="memitem:ga4dd10016d1f17d1a2fbf0ad913c90427">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusObjectPathVTable </td>
<td class="memItemRight" data-valign="bottom">DBusObjectPathVTable</td>
</tr>
<tr class="memdesc:ga4dd10016d1f17d1a2fbf0ad913c90427">
<td class="mdescLeft"> </td>
<td class="mdescRight">Set of functions that must be implemented to handle messages sent to a particular object path.<br />
</td>
</tr>
<tr class="separator:ga4dd10016d1f17d1a2fbf0ad913c90427">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga632c59364661602111278efd6a10d3aa" class="memitem:ga632c59364661602111278efd6a10d3aa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusAddWatchFunction) (DBusWatch *watch, void *data)</td>
</tr>
<tr class="memdesc:ga632c59364661602111278efd6a10d3aa">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when libdbus needs a new watch to be monitored by the main loop.<br />
</td>
</tr>
<tr class="separator:ga632c59364661602111278efd6a10d3aa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga08cb6a64fbd538ac30a8dd00ba19cd95" class="memitem:ga08cb6a64fbd538ac30a8dd00ba19cd95">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusWatchToggledFunction) (DBusWatch *watch, void *data)</td>
</tr>
<tr class="memdesc:ga08cb6a64fbd538ac30a8dd00ba19cd95">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when dbus_watch_get_enabled() may return a different value than it did before.<br />
</td>
</tr>
<tr class="separator:ga08cb6a64fbd538ac30a8dd00ba19cd95">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab99c5eeb90a30ec49cc2bdbb2e965b75" class="memitem:gab99c5eeb90a30ec49cc2bdbb2e965b75">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusRemoveWatchFunction) (DBusWatch *watch, void *data)</td>
</tr>
<tr class="memdesc:gab99c5eeb90a30ec49cc2bdbb2e965b75">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when libdbus no longer needs a watch to be monitored by the main loop.<br />
</td>
</tr>
<tr class="separator:gab99c5eeb90a30ec49cc2bdbb2e965b75">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7fad164617baf483b39f3e3ea1c30a40" class="memitem:ga7fad164617baf483b39f3e3ea1c30a40">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusAddTimeoutFunction) (DBusTimeout *timeout, void *data)</td>
</tr>
<tr class="memdesc:ga7fad164617baf483b39f3e3ea1c30a40">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when libdbus needs a new timeout to be monitored by the main loop.<br />
</td>
</tr>
<tr class="separator:ga7fad164617baf483b39f3e3ea1c30a40">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga65ee05019d4ee6d7c665ec829cd4414a" class="memitem:ga65ee05019d4ee6d7c665ec829cd4414a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusTimeoutToggledFunction) (DBusTimeout *timeout, void *data)</td>
</tr>
<tr class="memdesc:ga65ee05019d4ee6d7c665ec829cd4414a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when dbus_timeout_get_enabled() may return a different value than it did before.<br />
</td>
</tr>
<tr class="separator:ga65ee05019d4ee6d7c665ec829cd4414a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaed317fe6f12e65586a50e1d1d2ea96b7" class="memitem:gaed317fe6f12e65586a50e1d1d2ea96b7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusRemoveTimeoutFunction) (DBusTimeout *timeout, void *data)</td>
</tr>
<tr class="memdesc:gaed317fe6f12e65586a50e1d1d2ea96b7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when libdbus no longer needs a timeout to be monitored by the main loop.<br />
</td>
</tr>
<tr class="separator:gaed317fe6f12e65586a50e1d1d2ea96b7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3ce642a7bea6a14e030255dcfb25c8bd" class="memitem:ga3ce642a7bea6a14e030255dcfb25c8bd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusDispatchStatusFunction) (DBusConnection *connection, DBusDispatchStatus new_status, void *data)</td>
</tr>
<tr class="memdesc:ga3ce642a7bea6a14e030255dcfb25c8bd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when the return value of dbus_connection_get_dispatch_status() may have changed.<br />
</td>
</tr>
<tr class="separator:ga3ce642a7bea6a14e030255dcfb25c8bd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadbcbd64b9c8b0d40cf3f884e2ee2528c" class="memitem:gadbcbd64b9c8b0d40cf3f884e2ee2528c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusWakeupMainFunction) (void *data)</td>
</tr>
<tr class="memdesc:gadbcbd64b9c8b0d40cf3f884e2ee2528c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when the main loop's thread should be notified that there's now work to do.<br />
</td>
</tr>
<tr class="separator:gadbcbd64b9c8b0d40cf3f884e2ee2528c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabe3c6a8f883cd280c58779080cef234c" class="memitem:gabe3c6a8f883cd280c58779080cef234c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusAllowUnixUserFunction) (DBusConnection *connection, unsigned long uid, void *data)</td>
</tr>
<tr class="memdesc:gabe3c6a8f883cd280c58779080cef234c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called during authentication to check whether the given UNIX user ID is allowed to connect, if the client tried to auth as a UNIX user ID.<br />
</td>
</tr>
<tr class="separator:gabe3c6a8f883cd280c58779080cef234c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae92d8ad407e216c6b5c67c7efbf949dd" class="memitem:gae92d8ad407e216c6b5c67c7efbf949dd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef dbus_bool_t(* </td>
<td class="memItemRight" data-valign="bottom">DBusAllowWindowsUserFunction) (DBusConnection *connection, const char *user_sid, void *data)</td>
</tr>
<tr class="memdesc:gae92d8ad407e216c6b5c67c7efbf949dd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called during authentication to check whether the given Windows user ID is allowed to connect, if the client tried to auth as a Windows user ID.<br />
</td>
</tr>
<tr class="separator:gae92d8ad407e216c6b5c67c7efbf949dd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8209089764f3df09ec6523a24983375d" class="memitem:ga8209089764f3df09ec6523a24983375d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusPendingCallNotifyFunction) (DBusPendingCall *pending, void *user_data)</td>
</tr>
<tr class="memdesc:ga8209089764f3df09ec6523a24983375d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when a pending call now has a reply available.<br />
</td>
</tr>
<tr class="separator:ga8209089764f3df09ec6523a24983375d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5d7721ab952bd87d9a84f26d61709ad6" class="memitem:ga5d7721ab952bd87d9a84f26d61709ad6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef DBusHandlerResult(* </td>
<td class="memItemRight" data-valign="bottom">DBusHandleMessageFunction) (DBusConnection *connection, DBusMessage *message, void *user_data)</td>
</tr>
<tr class="memdesc:ga5d7721ab952bd87d9a84f26d61709ad6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when a message needs to be handled.<br />
</td>
</tr>
<tr class="separator:ga5d7721ab952bd87d9a84f26d61709ad6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga631a3290b2921ca4c45e1a34917eee36" class="memitem:ga631a3290b2921ca4c45e1a34917eee36">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusObjectPathUnregisterFunction) (DBusConnection *connection, void *user_data)</td>
</tr>
<tr class="memdesc:ga631a3290b2921ca4c45e1a34917eee36">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when a DBusObjectPathVTable is unregistered (or its connection is freed).<br />
</td>
</tr>
<tr class="separator:ga631a3290b2921ca4c45e1a34917eee36">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2cc66a1b9aa29d76e99b2fedfaf97126" class="memitem:ga2cc66a1b9aa29d76e99b2fedfaf97126">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef DBusHandlerResult(* </td>
<td class="memItemRight" data-valign="bottom">DBusObjectPathMessageFunction) (DBusConnection *connection, DBusMessage *message, void *user_data)</td>
</tr>
<tr class="memdesc:ga2cc66a1b9aa29d76e99b2fedfaf97126">
<td class="mdescLeft"> </td>
<td class="mdescRight">Called when a message is sent to a registered object path.<br />
</td>
</tr>
<tr class="separator:ga2cc66a1b9aa29d76e99b2fedfaf97126">
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
<tr id="r_ga0556779e61aeb19eb9cf6b6466bd1b98" class="memitem:ga0556779e61aeb19eb9cf6b6466bd1b98">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">DBusWatchFlags { DBUS_WATCH_READABLE = 1 &lt;&lt; 0 , DBUS_WATCH_WRITABLE = 1 &lt;&lt; 1 , DBUS_WATCH_ERROR = 1 &lt;&lt; 2 , DBUS_WATCH_HANGUP = 1 &lt;&lt; 3 }</td>
</tr>
<tr class="memdesc:ga0556779e61aeb19eb9cf6b6466bd1b98">
<td class="mdescLeft"> </td>
<td class="mdescRight">Indicates the status of a DBusWatch. More...<br />
</td>
</tr>
<tr class="separator:ga0556779e61aeb19eb9cf6b6466bd1b98">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabf250a32ff740b2a8c99136e0142d8d2" class="memitem:gabf250a32ff740b2a8c99136e0142d8d2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom">DBusDispatchStatus { DBUS_DISPATCH_DATA_REMAINS , DBUS_DISPATCH_COMPLETE , DBUS_DISPATCH_NEED_MEMORY }</td>
</tr>
<tr class="memdesc:gabf250a32ff740b2a8c99136e0142d8d2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Indicates the status of incoming data on a DBusConnection. More...<br />
</td>
</tr>
<tr class="separator:gabf250a32ff740b2a8c99136e0142d8d2">
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
<tr id="r_gacd32f819820266598c6b6847dfddaf9c" class="memitem:gacd32f819820266598c6b6847dfddaf9c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_open (const char *address, DBusError *error)</td>
</tr>
<tr class="memdesc:gacd32f819820266598c6b6847dfddaf9c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets a connection to a remote address.<br />
</td>
</tr>
<tr class="separator:gacd32f819820266598c6b6847dfddaf9c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga434e3fc7ee420fd30e2f05e57ff26b1d" class="memitem:ga434e3fc7ee420fd30e2f05e57ff26b1d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_open_private (const char *address, DBusError *error)</td>
</tr>
<tr class="memdesc:ga434e3fc7ee420fd30e2f05e57ff26b1d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Opens a new, dedicated connection to a remote address.<br />
</td>
</tr>
<tr class="separator:ga434e3fc7ee420fd30e2f05e57ff26b1d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae34751e15f114217e5ad10c663e2ef2e" class="memitem:gae34751e15f114217e5ad10c663e2ef2e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_ref (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gae34751e15f114217e5ad10c663e2ef2e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments the reference count of a DBusConnection.<br />
</td>
</tr>
<tr class="separator:gae34751e15f114217e5ad10c663e2ef2e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6385ff09bc108238c4429e7c195dab25" class="memitem:ga6385ff09bc108238c4429e7c195dab25">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_unref (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga6385ff09bc108238c4429e7c195dab25">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements the reference count of a DBusConnection, and finalizes it if the count reaches zero.<br />
</td>
</tr>
<tr class="separator:ga6385ff09bc108238c4429e7c195dab25">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2522ac5075dfe0a1535471f6e045e1ee" class="memitem:ga2522ac5075dfe0a1535471f6e045e1ee">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_close (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga2522ac5075dfe0a1535471f6e045e1ee">
<td class="mdescLeft"> </td>
<td class="mdescRight">Closes a private connection, so no further data can be sent or received.<br />
</td>
</tr>
<tr class="separator:ga2522ac5075dfe0a1535471f6e045e1ee">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga611ae94556af36fe30bfb547366ca4e1" class="memitem:ga611ae94556af36fe30bfb547366ca4e1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_is_connected (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga611ae94556af36fe30bfb547366ca4e1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets whether the connection is currently open.<br />
</td>
</tr>
<tr class="separator:ga611ae94556af36fe30bfb547366ca4e1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2f1fa02c9897b6f07f4d33c862de4a1d" class="memitem:ga2f1fa02c9897b6f07f4d33c862de4a1d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_is_authenticated (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga2f1fa02c9897b6f07f4d33c862de4a1d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets whether the connection was authenticated.<br />
</td>
</tr>
<tr class="separator:ga2f1fa02c9897b6f07f4d33c862de4a1d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa6c5d523e16d8a5b9316c92d9ff1ac17" class="memitem:gaa6c5d523e16d8a5b9316c92d9ff1ac17">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_is_anonymous (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gaa6c5d523e16d8a5b9316c92d9ff1ac17">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets whether the connection is not authenticated as a specific user.<br />
</td>
</tr>
<tr class="separator:gaa6c5d523e16d8a5b9316c92d9ff1ac17">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae6c19e146a37f9de6a06c1617874bed9" class="memitem:gae6c19e146a37f9de6a06c1617874bed9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_server_id (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gae6c19e146a37f9de6a06c1617874bed9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the ID of the server address we are authenticated to, if this connection is on the client side.<br />
</td>
</tr>
<tr class="separator:gae6c19e146a37f9de6a06c1617874bed9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3e41509b3afdbc22872bacc5754e85c2" class="memitem:ga3e41509b3afdbc22872bacc5754e85c2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_can_send_type (DBusConnection *connection, int type)</td>
</tr>
<tr class="memdesc:ga3e41509b3afdbc22872bacc5754e85c2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tests whether a certain type can be send via the connection.<br />
</td>
</tr>
<tr class="separator:ga3e41509b3afdbc22872bacc5754e85c2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga19091beb74f1504b0e862a7ad10e71cd" class="memitem:ga19091beb74f1504b0e862a7ad10e71cd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_exit_on_disconnect (DBusConnection *connection, dbus_bool_t exit_on_disconnect)</td>
</tr>
<tr class="memdesc:ga19091beb74f1504b0e862a7ad10e71cd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Set whether _exit() should be called when the connection receives a disconnect signal.<br />
</td>
</tr>
<tr class="separator:ga19091beb74f1504b0e862a7ad10e71cd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6136968eba30e8313e668a622fcfb08d" class="memitem:ga6136968eba30e8313e668a622fcfb08d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusPreallocatedSend * </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_preallocate_send (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga6136968eba30e8313e668a622fcfb08d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Preallocates resources needed to send a message, allowing the message to be sent without the possibility of memory allocation failure.<br />
</td>
</tr>
<tr class="separator:ga6136968eba30e8313e668a622fcfb08d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad0ea06307b418616711131ea7bdae8ac" class="memitem:gad0ea06307b418616711131ea7bdae8ac">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_free_preallocated_send (DBusConnection *connection, DBusPreallocatedSend *preallocated)</td>
</tr>
<tr class="memdesc:gad0ea06307b418616711131ea7bdae8ac">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees preallocated message-sending resources from dbus_connection_preallocate_send().<br />
</td>
</tr>
<tr class="separator:gad0ea06307b418616711131ea7bdae8ac">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2fea5f972d1bfe7bcde8c0ec65ca9e90" class="memitem:ga2fea5f972d1bfe7bcde8c0ec65ca9e90">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_send_preallocated (DBusConnection *connection, DBusPreallocatedSend *preallocated, DBusMessage *message, dbus_uint32_t *client_serial)</td>
</tr>
<tr class="memdesc:ga2fea5f972d1bfe7bcde8c0ec65ca9e90">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sends a message using preallocated resources.<br />
</td>
</tr>
<tr class="separator:ga2fea5f972d1bfe7bcde8c0ec65ca9e90">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae1cb64f4cf550949b23fd3a756b2f7d0" class="memitem:gae1cb64f4cf550949b23fd3a756b2f7d0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_send (DBusConnection *connection, DBusMessage *message, dbus_uint32_t *serial)</td>
</tr>
<tr class="memdesc:gae1cb64f4cf550949b23fd3a756b2f7d0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a message to the outgoing message queue.<br />
</td>
</tr>
<tr class="separator:gae1cb64f4cf550949b23fd3a756b2f7d0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa215df7ab7ca6dce7be153c6b9cc80ba" class="memitem:gaa215df7ab7ca6dce7be153c6b9cc80ba">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_send_with_reply (DBusConnection *connection, DBusMessage *message, DBusPendingCall **pending_return, int timeout_milliseconds)</td>
</tr>
<tr class="memdesc:gaa215df7ab7ca6dce7be153c6b9cc80ba">
<td class="mdescLeft"> </td>
<td class="mdescRight">Queues a message to send, as with dbus_connection_send(), but also returns a DBusPendingCall used to receive a reply to the message.<br />
</td>
</tr>
<tr class="separator:gaa215df7ab7ca6dce7be153c6b9cc80ba">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8d6431f17a9e53c9446d87c2ba8409f0" class="memitem:ga8d6431f17a9e53c9446d87c2ba8409f0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_send_with_reply_and_block (DBusConnection *connection, DBusMessage *message, int timeout_milliseconds, DBusError *error)</td>
</tr>
<tr class="memdesc:ga8d6431f17a9e53c9446d87c2ba8409f0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sends a message and blocks a certain time period while waiting for a reply.<br />
</td>
</tr>
<tr class="separator:ga8d6431f17a9e53c9446d87c2ba8409f0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga10e68d9d2f41d655a4151ddeb807ff54" class="memitem:ga10e68d9d2f41d655a4151ddeb807ff54">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_flush (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga10e68d9d2f41d655a4151ddeb807ff54">
<td class="mdescLeft"> </td>
<td class="mdescRight">Blocks until the outgoing message queue is empty.<br />
</td>
</tr>
<tr class="separator:ga10e68d9d2f41d655a4151ddeb807ff54">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga580d8766c23fe5f49418bc7d87b67dc6" class="memitem:ga580d8766c23fe5f49418bc7d87b67dc6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_read_write_dispatch (DBusConnection *connection, int timeout_milliseconds)</td>
</tr>
<tr class="memdesc:ga580d8766c23fe5f49418bc7d87b67dc6">
<td class="mdescLeft"> </td>
<td class="mdescRight">This function is intended for use with applications that don't want to write a main loop and deal with DBusWatch and DBusTimeout.<br />
</td>
</tr>
<tr class="separator:ga580d8766c23fe5f49418bc7d87b67dc6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga371163b4955a6e0bf0f1f70f38390c14" class="memitem:ga371163b4955a6e0bf0f1f70f38390c14">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_read_write (DBusConnection *connection, int timeout_milliseconds)</td>
</tr>
<tr class="memdesc:ga371163b4955a6e0bf0f1f70f38390c14">
<td class="mdescLeft"> </td>
<td class="mdescRight">This function is intended for use with applications that don't want to write a main loop and deal with DBusWatch and DBusTimeout.<br />
</td>
</tr>
<tr class="separator:ga371163b4955a6e0bf0f1f70f38390c14">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9d07083c520e291591a68adb78f64094" class="memitem:ga9d07083c520e291591a68adb78f64094">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_borrow_message (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga9d07083c520e291591a68adb78f64094">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the first-received message from the incoming message queue, leaving it in the queue.<br />
</td>
</tr>
<tr class="separator:ga9d07083c520e291591a68adb78f64094">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0586da03a01c9c6f332fbea900ef55e3" class="memitem:ga0586da03a01c9c6f332fbea900ef55e3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_return_message (DBusConnection *connection, DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga0586da03a01c9c6f332fbea900ef55e3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Used to return a message after peeking at it using dbus_connection_borrow_message().<br />
</td>
</tr>
<tr class="separator:ga0586da03a01c9c6f332fbea900ef55e3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7125d747575b2f596aceaf7be53eae68" class="memitem:ga7125d747575b2f596aceaf7be53eae68">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_steal_borrowed_message (DBusConnection *connection, DBusMessage *message)</td>
</tr>
<tr class="memdesc:ga7125d747575b2f596aceaf7be53eae68">
<td class="mdescLeft"> </td>
<td class="mdescRight">Used to keep a message after peeking at it using dbus_connection_borrow_message().<br />
</td>
</tr>
<tr class="separator:ga7125d747575b2f596aceaf7be53eae68">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1e40d994ea162ce767e78de1c4988566" class="memitem:ga1e40d994ea162ce767e78de1c4988566">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_pop_message (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga1e40d994ea162ce767e78de1c4988566">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the first-received message from the incoming message queue, removing it from the queue.<br />
</td>
</tr>
<tr class="separator:ga1e40d994ea162ce767e78de1c4988566">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga893d18d8b36ffb371f16d13645071289" class="memitem:ga893d18d8b36ffb371f16d13645071289">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDispatchStatus </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_dispatch_status (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga893d18d8b36ffb371f16d13645071289">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the current state of the incoming message queue.<br />
</td>
</tr>
<tr class="separator:ga893d18d8b36ffb371f16d13645071289">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga66ba7df50d75f4bda6b6e942430b81c7" class="memitem:ga66ba7df50d75f4bda6b6e942430b81c7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDispatchStatus </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_dispatch (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga66ba7df50d75f4bda6b6e942430b81c7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Processes any incoming data.<br />
</td>
</tr>
<tr class="separator:ga66ba7df50d75f4bda6b6e942430b81c7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaebf031eb444b4f847606aa27daa3d8e6" class="memitem:gaebf031eb444b4f847606aa27daa3d8e6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_watch_functions (DBusConnection *connection, DBusAddWatchFunction add_function, DBusRemoveWatchFunction remove_function, DBusWatchToggledFunction toggled_function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:gaebf031eb444b4f847606aa27daa3d8e6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the watch functions for the connection.<br />
</td>
</tr>
<tr class="separator:gaebf031eb444b4f847606aa27daa3d8e6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab3cbc68eec427e9ce1783b25d44fe93c" class="memitem:gab3cbc68eec427e9ce1783b25d44fe93c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_timeout_functions (DBusConnection *connection, DBusAddTimeoutFunction add_function, DBusRemoveTimeoutFunction remove_function, DBusTimeoutToggledFunction toggled_function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:gab3cbc68eec427e9ce1783b25d44fe93c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the timeout functions for the connection.<br />
</td>
</tr>
<tr class="separator:gab3cbc68eec427e9ce1783b25d44fe93c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2b1df13251c7ec348bcba39c0924e881" class="memitem:ga2b1df13251c7ec348bcba39c0924e881">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_wakeup_main_function (DBusConnection *connection, DBusWakeupMainFunction wakeup_main_function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:ga2b1df13251c7ec348bcba39c0924e881">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the mainloop wakeup function for the connection.<br />
</td>
</tr>
<tr class="separator:ga2b1df13251c7ec348bcba39c0924e881">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga55ff88cd22c0672441c7deffbfb68fbf" class="memitem:ga55ff88cd22c0672441c7deffbfb68fbf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_dispatch_status_function (DBusConnection *connection, DBusDispatchStatusFunction function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:ga55ff88cd22c0672441c7deffbfb68fbf">
<td class="mdescLeft"> </td>
<td class="mdescRight">Set a function to be invoked when the dispatch status changes.<br />
</td>
</tr>
<tr class="separator:ga55ff88cd22c0672441c7deffbfb68fbf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga38297f511f4124accdfa68c321e081cc" class="memitem:ga38297f511f4124accdfa68c321e081cc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_unix_fd (DBusConnection *connection, int *fd)</td>
</tr>
<tr class="memdesc:ga38297f511f4124accdfa68c321e081cc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get the UNIX file descriptor of the connection, if any.<br />
</td>
</tr>
<tr class="separator:ga38297f511f4124accdfa68c321e081cc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1c14590d77b148390bde9e82a7544434" class="memitem:ga1c14590d77b148390bde9e82a7544434">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_socket (DBusConnection *connection, int *fd)</td>
</tr>
<tr class="memdesc:ga1c14590d77b148390bde9e82a7544434">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the underlying Windows or UNIX socket file descriptor of the connection, if any.<br />
</td>
</tr>
<tr class="separator:ga1c14590d77b148390bde9e82a7544434">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaef670c3a8170ab9c719ec955252459d0" class="memitem:gaef670c3a8170ab9c719ec955252459d0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_unix_user (DBusConnection *connection, unsigned long *uid)</td>
</tr>
<tr class="memdesc:gaef670c3a8170ab9c719ec955252459d0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the UNIX user ID of the connection if known.<br />
</td>
</tr>
<tr class="separator:gaef670c3a8170ab9c719ec955252459d0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaeebeadcafa87e2d30eed4296f26fb73c" class="memitem:gaeebeadcafa87e2d30eed4296f26fb73c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_unix_process_id (DBusConnection *connection, unsigned long *pid)</td>
</tr>
<tr class="memdesc:gaeebeadcafa87e2d30eed4296f26fb73c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the process ID of the connection if any.<br />
</td>
</tr>
<tr class="separator:gaeebeadcafa87e2d30eed4296f26fb73c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga969b9dafe806c9fe0a54c9d8a565c2e1" class="memitem:ga969b9dafe806c9fe0a54c9d8a565c2e1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_adt_audit_session_data (DBusConnection *connection, void **data, dbus_int32_t *data_size)</td>
</tr>
<tr class="memdesc:ga969b9dafe806c9fe0a54c9d8a565c2e1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the ADT audit data of the connection if any.<br />
</td>
</tr>
<tr class="separator:ga969b9dafe806c9fe0a54c9d8a565c2e1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6b78379badb4c5804344f4f3d87a958a" class="memitem:ga6b78379badb4c5804344f4f3d87a958a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_unix_user_function (DBusConnection *connection, DBusAllowUnixUserFunction function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:ga6b78379badb4c5804344f4f3d87a958a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a predicate function used to determine whether a given user ID is allowed to connect.<br />
</td>
</tr>
<tr class="separator:ga6b78379badb4c5804344f4f3d87a958a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga06378d6ee9a213cea45965288338966a" class="memitem:ga06378d6ee9a213cea45965288338966a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_get_linux_security_label (DBusConnection *connection, char **label_p)</td>
</tr>
<tr class="separator:ga06378d6ee9a213cea45965288338966a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7881fb4f53b0364f8a810a06054dbef5" class="memitem:ga7881fb4f53b0364f8a810a06054dbef5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">_dbus_connection_get_credentials (DBusConnection *connection)</td>
</tr>
<tr class="separator:ga7881fb4f53b0364f8a810a06054dbef5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2b3cb488f1922aeecdeafdcb110e91a8" class="memitem:ga2b3cb488f1922aeecdeafdcb110e91a8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_windows_user (DBusConnection *connection, char **windows_sid_p)</td>
</tr>
<tr class="memdesc:ga2b3cb488f1922aeecdeafdcb110e91a8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the Windows user SID of the connection if known.<br />
</td>
</tr>
<tr class="separator:ga2b3cb488f1922aeecdeafdcb110e91a8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa35ced9ccd29d3366749ae383b120f9c" class="memitem:gaa35ced9ccd29d3366749ae383b120f9c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_windows_user_function (DBusConnection *connection, DBusAllowWindowsUserFunction function, void *data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:gaa35ced9ccd29d3366749ae383b120f9c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets a predicate function used to determine whether a given user ID is allowed to connect.<br />
</td>
</tr>
<tr class="separator:gaa35ced9ccd29d3366749ae383b120f9c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gade349ff04ed548993a8054250e317c12" class="memitem:gade349ff04ed548993a8054250e317c12">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_allow_anonymous (DBusConnection *connection, dbus_bool_t value)</td>
</tr>
<tr class="memdesc:gade349ff04ed548993a8054250e317c12">
<td class="mdescLeft"> </td>
<td class="mdescRight">This function must be called on the server side of a connection when the connection is first seen in the DBusNewConnectionFunction.<br />
</td>
</tr>
<tr class="separator:gade349ff04ed548993a8054250e317c12">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae57ce610b7e88e917b7b2985c9cf32cc" class="memitem:gae57ce610b7e88e917b7b2985c9cf32cc">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_builtin_filters_enabled (DBusConnection *connection, dbus_bool_t value)</td>
</tr>
<tr class="memdesc:gae57ce610b7e88e917b7b2985c9cf32cc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Enables the builtin filtering of messages.<br />
</td>
</tr>
<tr class="separator:gae57ce610b7e88e917b7b2985c9cf32cc">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf58e8cc7b8717db1581459c0c3d34b08" class="memitem:gaf58e8cc7b8717db1581459c0c3d34b08">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_route_peer_messages (DBusConnection *connection, dbus_bool_t value)</td>
</tr>
<tr class="memdesc:gaf58e8cc7b8717db1581459c0c3d34b08">
<td class="mdescLeft"> </td>
<td class="mdescRight">Normally DBusConnection automatically handles all messages to the org.freedesktop.DBus.Peer interface.<br />
</td>
</tr>
<tr class="separator:gaf58e8cc7b8717db1581459c0c3d34b08">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae00f581e5487408cb294bf71826aff86" class="memitem:gae00f581e5487408cb294bf71826aff86">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_add_filter (DBusConnection *connection, DBusHandleMessageFunction function, void *user_data, DBusFreeFunction free_data_function)</td>
</tr>
<tr class="memdesc:gae00f581e5487408cb294bf71826aff86">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a message filter.<br />
</td>
</tr>
<tr class="separator:gae00f581e5487408cb294bf71826aff86">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5e7f1dad410506a8a6f5182c55e7c4fe" class="memitem:ga5e7f1dad410506a8a6f5182c55e7c4fe">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_remove_filter (DBusConnection *connection, DBusHandleMessageFunction function, void *user_data)</td>
</tr>
<tr class="memdesc:ga5e7f1dad410506a8a6f5182c55e7c4fe">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a previously-added message filter.<br />
</td>
</tr>
<tr class="separator:ga5e7f1dad410506a8a6f5182c55e7c4fe">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga708b1e108feed18f5775ff404c9dda4b" class="memitem:ga708b1e108feed18f5775ff404c9dda4b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_try_register_object_path (DBusConnection *connection, const char *path, const DBusObjectPathVTable *vtable, void *user_data, DBusError *error)</td>
</tr>
<tr class="memdesc:ga708b1e108feed18f5775ff404c9dda4b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Registers a handler for a given path in the object hierarchy.<br />
</td>
</tr>
<tr class="separator:ga708b1e108feed18f5775ff404c9dda4b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga24730ca6fd2e9132873962a32df7628c" class="memitem:ga24730ca6fd2e9132873962a32df7628c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_register_object_path (DBusConnection *connection, const char *path, const DBusObjectPathVTable *vtable, void *user_data)</td>
</tr>
<tr class="memdesc:ga24730ca6fd2e9132873962a32df7628c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Registers a handler for a given path in the object hierarchy.<br />
</td>
</tr>
<tr class="separator:ga24730ca6fd2e9132873962a32df7628c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8e9d2d4ff17c3071124e4993d1536ed4" class="memitem:ga8e9d2d4ff17c3071124e4993d1536ed4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_try_register_fallback (DBusConnection *connection, const char *path, const DBusObjectPathVTable *vtable, void *user_data, DBusError *error)</td>
</tr>
<tr class="memdesc:ga8e9d2d4ff17c3071124e4993d1536ed4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Registers a fallback handler for a given subsection of the object hierarchy.<br />
</td>
</tr>
<tr class="separator:ga8e9d2d4ff17c3071124e4993d1536ed4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac4473b37bfa74ccf7459959d27e7bc59" class="memitem:gac4473b37bfa74ccf7459959d27e7bc59">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_register_fallback (DBusConnection *connection, const char *path, const DBusObjectPathVTable *vtable, void *user_data)</td>
</tr>
<tr class="memdesc:gac4473b37bfa74ccf7459959d27e7bc59">
<td class="mdescLeft"> </td>
<td class="mdescRight">Registers a fallback handler for a given subsection of the object hierarchy.<br />
</td>
</tr>
<tr class="separator:gac4473b37bfa74ccf7459959d27e7bc59">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6ae8f005dedf24c5f2df1768795392fb" class="memitem:ga6ae8f005dedf24c5f2df1768795392fb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_unregister_object_path (DBusConnection *connection, const char *path)</td>
</tr>
<tr class="memdesc:ga6ae8f005dedf24c5f2df1768795392fb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Unregisters the handler registered with exactly the given path.<br />
</td>
</tr>
<tr class="separator:ga6ae8f005dedf24c5f2df1768795392fb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga08ee6e70b74c294fe24d0f391f16db24" class="memitem:ga08ee6e70b74c294fe24d0f391f16db24">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_object_path_data (DBusConnection *connection, const char *path, void **data_p)</td>
</tr>
<tr class="memdesc:ga08ee6e70b74c294fe24d0f391f16db24">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the user data passed to dbus_connection_register_object_path() or dbus_connection_register_fallback().<br />
</td>
</tr>
<tr class="separator:ga08ee6e70b74c294fe24d0f391f16db24">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3e9de2067d0eed66ef73230fae8d8be2" class="memitem:ga3e9de2067d0eed66ef73230fae8d8be2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_list_registered (DBusConnection *connection, const char *parent_path, char ***child_entries)</td>
</tr>
<tr class="memdesc:ga3e9de2067d0eed66ef73230fae8d8be2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Lists the registered fallback handlers and object path handlers at the given parent_path.<br />
</td>
</tr>
<tr class="separator:ga3e9de2067d0eed66ef73230fae8d8be2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga728b15c71a492ad244e5a480f1156088" class="memitem:ga728b15c71a492ad244e5a480f1156088">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_allocate_data_slot (dbus_int32_t *slot_p)</td>
</tr>
<tr class="memdesc:ga728b15c71a492ad244e5a480f1156088">
<td class="mdescLeft"> </td>
<td class="mdescRight">Allocates an integer ID to be used for storing application-specific data on any DBusConnection.<br />
</td>
</tr>
<tr class="separator:ga728b15c71a492ad244e5a480f1156088">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7dc8c73d8c3e733f5410d52be84239a0" class="memitem:ga7dc8c73d8c3e733f5410d52be84239a0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_free_data_slot (dbus_int32_t *slot_p)</td>
</tr>
<tr class="memdesc:ga7dc8c73d8c3e733f5410d52be84239a0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Deallocates a global ID for connection data slots.<br />
</td>
</tr>
<tr class="separator:ga7dc8c73d8c3e733f5410d52be84239a0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga845b4942399f43dd4ac644de7cb9e3ff" class="memitem:ga845b4942399f43dd4ac644de7cb9e3ff">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_data (DBusConnection *connection, dbus_int32_t slot, void *data, DBusFreeFunction free_data_func)</td>
</tr>
<tr class="memdesc:ga845b4942399f43dd4ac644de7cb9e3ff">
<td class="mdescLeft"> </td>
<td class="mdescRight">Stores a pointer on a DBusConnection, along with an optional function to be used for freeing the data when the data is set again, or when the connection is finalized.<br />
</td>
</tr>
<tr class="separator:ga845b4942399f43dd4ac644de7cb9e3ff">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga433fae9844a66d9d078d238e6c723b95" class="memitem:ga433fae9844a66d9d078d238e6c723b95">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_data (DBusConnection *connection, dbus_int32_t slot)</td>
</tr>
<tr class="memdesc:ga433fae9844a66d9d078d238e6c723b95">
<td class="mdescLeft"> </td>
<td class="mdescRight">Retrieves data previously set with dbus_connection_set_data().<br />
</td>
</tr>
<tr class="separator:ga433fae9844a66d9d078d238e6c723b95">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga794d0b572e30448fb262618222f76124" class="memitem:ga794d0b572e30448fb262618222f76124">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_change_sigpipe (dbus_bool_t will_modify_sigpipe)</td>
</tr>
<tr class="memdesc:ga794d0b572e30448fb262618222f76124">
<td class="mdescLeft"> </td>
<td class="mdescRight">This function sets a global flag for whether dbus_connection_new() will set SIGPIPE behavior to SIG_IGN.<br />
</td>
</tr>
<tr class="separator:ga794d0b572e30448fb262618222f76124">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0d783462274a6c71d3767f5821c29ce9" class="memitem:ga0d783462274a6c71d3767f5821c29ce9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_max_message_size (DBusConnection *connection, long size)</td>
</tr>
<tr class="memdesc:ga0d783462274a6c71d3767f5821c29ce9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Specifies the maximum size message this connection is allowed to receive.<br />
</td>
</tr>
<tr class="separator:ga0d783462274a6c71d3767f5821c29ce9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7a459e64d7dca7b592136cec0a73422c" class="memitem:ga7a459e64d7dca7b592136cec0a73422c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_max_message_size (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga7a459e64d7dca7b592136cec0a73422c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the value set by dbus_connection_set_max_message_size().<br />
</td>
</tr>
<tr class="separator:ga7a459e64d7dca7b592136cec0a73422c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2aadce7d15c0e11983363912292b3fcd" class="memitem:ga2aadce7d15c0e11983363912292b3fcd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_max_message_unix_fds (DBusConnection *connection, long n)</td>
</tr>
<tr class="memdesc:ga2aadce7d15c0e11983363912292b3fcd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Specifies the maximum number of unix fds a message on this connection is allowed to receive.<br />
</td>
</tr>
<tr class="separator:ga2aadce7d15c0e11983363912292b3fcd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga18abaca9a512dbb7b6f921c3df6875d9" class="memitem:ga18abaca9a512dbb7b6f921c3df6875d9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_max_message_unix_fds (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga18abaca9a512dbb7b6f921c3df6875d9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the value set by dbus_connection_set_max_message_unix_fds().<br />
</td>
</tr>
<tr class="separator:ga18abaca9a512dbb7b6f921c3df6875d9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6565d75f16e6e803372b2ae3d94d991b" class="memitem:ga6565d75f16e6e803372b2ae3d94d991b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_max_received_size (DBusConnection *connection, long size)</td>
</tr>
<tr class="memdesc:ga6565d75f16e6e803372b2ae3d94d991b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the maximum total number of bytes that can be used for all messages received on this connection.<br />
</td>
</tr>
<tr class="separator:ga6565d75f16e6e803372b2ae3d94d991b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga376529acf41d1d34b4f46c0d9d515c85" class="memitem:ga376529acf41d1d34b4f46c0d9d515c85">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_max_received_size (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga376529acf41d1d34b4f46c0d9d515c85">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the value set by dbus_connection_set_max_received_size().<br />
</td>
</tr>
<tr class="separator:ga376529acf41d1d34b4f46c0d9d515c85">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga81e63dc6d9298e8a7f92c0d93d0e80b3" class="memitem:ga81e63dc6d9298e8a7f92c0d93d0e80b3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_set_max_received_unix_fds (DBusConnection *connection, long n)</td>
</tr>
<tr class="memdesc:ga81e63dc6d9298e8a7f92c0d93d0e80b3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the maximum total number of unix fds that can be used for all messages received on this connection.<br />
</td>
</tr>
<tr class="separator:ga81e63dc6d9298e8a7f92c0d93d0e80b3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga219f31132338616f82dc975c070ff418" class="memitem:ga219f31132338616f82dc975c070ff418">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_max_received_unix_fds (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga219f31132338616f82dc975c070ff418">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the value set by dbus_connection_set_max_received_unix_fds().<br />
</td>
</tr>
<tr class="separator:ga219f31132338616f82dc975c070ff418">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga47aff801f586e7116f9c54532bb1baf9" class="memitem:ga47aff801f586e7116f9c54532bb1baf9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_outgoing_size (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga47aff801f586e7116f9c54532bb1baf9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the approximate size in bytes of all messages in the outgoing message queue.<br />
</td>
</tr>
<tr class="separator:ga47aff801f586e7116f9c54532bb1baf9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad218838fdaa8d36c606723c63e96f453" class="memitem:gad218838fdaa8d36c606723c63e96f453">
<td class="memItemLeft" style="text-align: right;" data-valign="top">long </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_get_outgoing_unix_fds (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gad218838fdaa8d36c606723c63e96f453">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the approximate number of uni fds of all messages in the outgoing message queue.<br />
</td>
</tr>
<tr class="separator:gad218838fdaa8d36c606723c63e96f453">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac40563ec4c0e309d936daf3163ba9bb7" class="memitem:gac40563ec4c0e309d936daf3163ba9bb7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_connection_has_messages_to_send (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:gac40563ec4c0e309d936daf3163ba9bb7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether there are messages in the outgoing message queue.<br />
</td>
</tr>
<tr class="separator:gac40563ec4c0e309d936daf3163ba9bb7">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Connection to another application.

A DBusConnection represents a connection to another application. Messages can be sent and received via this connection. The other application may be a message bus; for convenience, the function dbus_bus_get() is provided to automatically open a connection to the well-known message buses.

In brief a DBusConnection is a message queue associated with some message transport mechanism such as a socket. The connection maintains a queue of incoming messages and a queue of outgoing messages.

Several functions use the following terms:

- **read** means to fill the incoming message queue by reading from the socket
- **write** means to drain the outgoing queue by writing to the socket
- **dispatch** means to drain the incoming queue by invoking application-provided message handlers

The function dbus_connection_read_write_dispatch() for example does all three of these things, offering a simple alternative to a main loop.

In an application with a main loop, the read/write/dispatch operations are usually separate.

The connection provides DBusWatch and DBusTimeout objects to the main loop. These are used to know when reading, writing, or dispatching should be performed.

Incoming messages are processed by calling dbus_connection_dispatch(). dbus_connection_dispatch() runs any handlers registered for the topmost message in the message queue, then discards the message, then returns.

dbus_connection_get_dispatch_status() indicates whether messages are currently in the queue that need dispatching. dbus_connection_set_dispatch_status_function() allows you to set a function to be used to monitor the dispatch status.

If you're using GLib or Qt add-on libraries for D-Bus, there are special convenience APIs in those libraries that hide all the details of dispatch and watch/timeout monitoring. For example, dbus_connection_setup_with_g_main().

If you aren't using these add-on libraries, but want to process messages asynchronously, you must manually call dbus_connection_set_dispatch_status_function(), dbus_connection_set_watch_functions(), dbus_connection_set_timeout_functions() providing appropriate functions to integrate the connection with your application's main loop. This can be tricky to get right; main loops are not simple.

If you don't need to be asynchronous, you can ignore DBusWatch, DBusTimeout, and dbus_connection_dispatch(). Instead, dbus_connection_read_write_dispatch() can be used.

Or, in *very* simple applications, dbus_connection_pop_message() may be all you need, allowing you to avoid setting up any handler functions (see dbus_connection_add_filter(), dbus_connection_register_object_path() for more on handlers).

When you use dbus_connection_send() or one of its variants to send a message, the message is added to the outgoing queue. It's actually written to the network later; either in dbus_watch_handle() invoked by your main loop, or in dbus_connection_flush() which blocks until it can write out the entire outgoing queue. The GLib/Qt add-on libraries again handle the details here for you by setting up watch functions.

When a connection is disconnected, you are guaranteed to get a signal "Disconnected" from the interface DBUS_INTERFACE_LOCAL, path DBUS_PATH_LOCAL.

You may not drop the last reference to a DBusConnection until that connection has been disconnected.

You may dispatch the unprocessed incoming message queue even if the connection is disconnected. However, "Disconnected" will always be the last message in the queue (obviously no messages are received after disconnection).

After calling dbus_threads_init(), DBusConnection has thread locks and drops them when invoking user callbacks, so in general is transparently threadsafe. However, DBusMessage does NOT have thread locks; you must not send the same message to multiple DBusConnection if those connections will be used from different threads, for example.

Also, if you dispatch or pop messages from multiple threads, it may work in the sense that it won't crash, but it's tough to imagine sane results; it will be completely unpredictable which messages go to which threads.

It's recommended to dispatch from a single thread.

The most useful function to call from multiple threads at once is dbus_connection_send_with_reply_and_block(). That is, multiple threads can make method calls at the same time.

If you aren't using threads, you can use a main loop and dbus_pending_call_set_notify() to achieve a similar result.

## Typedef Documentation

## ◆ DBusAddTimeoutFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusAddTimeoutFunction) (DBusTimeout \*timeout, void \*data) |

Called when libdbus needs a new timeout to be monitored by the main loop.

Returns FALSE if it lacks enough memory to add the watch. Set by dbus_connection_set_timeout_functions() or dbus_server_set_timeout_functions().

Definition at line 113 of file dbus-connection.h.

## ◆ DBusAddWatchFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusAddWatchFunction) (DBusWatch \*watch, void \*data) |

Called when libdbus needs a new watch to be monitored by the main loop.

Returns FALSE if it lacks enough memory to add the watch. Set by dbus_connection_set_watch_functions() or dbus_server_set_watch_functions().

Definition at line 94 of file dbus-connection.h.

## ◆ DBusAllowUnixUserFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusAllowUnixUserFunction) (DBusConnection \*connection, unsigned long uid, void \*data) |

Called during authentication to check whether the given UNIX user ID is allowed to connect, if the client tried to auth as a UNIX user ID.

Normally on Windows this would never happen. Set with dbus_connection_set_unix_user_function().

Definition at line 146 of file dbus-connection.h.

## ◆ DBusAllowWindowsUserFunction

|  |
|----|
| typedef dbus_bool_t(\* DBusAllowWindowsUserFunction) (DBusConnection \*connection, const char \*user_sid, void \*data) |

Called during authentication to check whether the given Windows user ID is allowed to connect, if the client tried to auth as a Windows user ID.

Normally on UNIX this would never happen. Set with dbus_connection_set_windows_user_function().

Definition at line 156 of file dbus-connection.h.

## ◆ DBusConnection

|                                              |
|----------------------------------------------|
| typedef struct DBusConnection DBusConnection |

Opaque type representing a connection to a remote application and associated incoming/outgoing message queues.

Definition at line 54 of file dbus-connection.h.

## ◆ DBusDispatchStatusFunction

|  |
|----|
| typedef void(\* DBusDispatchStatusFunction) (DBusConnection \*connection, DBusDispatchStatus new_status, void \*data) |

Called when the return value of dbus_connection_get_dispatch_status() may have changed.

Set with dbus_connection_set_dispatch_status_function().

Definition at line 131 of file dbus-connection.h.

## ◆ DBusHandleMessageFunction

|  |
|----|
| typedef DBusHandlerResult(\* DBusHandleMessageFunction) (DBusConnection \*connection, DBusMessage \*message, void \*user_data) |

Called when a message needs to be handled.

The result indicates whether or not more handlers should be run. Set with dbus_connection_add_filter().

Definition at line 172 of file dbus-connection.h.

## ◆ DBusObjectPathMessageFunction

|  |
|----|
| typedef DBusHandlerResult(\* DBusObjectPathMessageFunction) (DBusConnection \*connection, DBusMessage \*message, void \*user_data) |

Called when a message is sent to a registered object path.

Found in DBusObjectPathVTable which is registered with dbus_connection_register_object_path() or dbus_connection_register_fallback().

Definition at line 380 of file dbus-connection.h.

## ◆ DBusObjectPathUnregisterFunction

|  |
|----|
| typedef void(\* DBusObjectPathUnregisterFunction) (DBusConnection \*connection, void \*user_data) |

Called when a DBusObjectPathVTable is unregistered (or its connection is freed).

Found in DBusObjectPathVTable.

Definition at line 373 of file dbus-connection.h.

## ◆ DBusObjectPathVTable

|                                                          |
|----------------------------------------------------------|
| typedef struct DBusObjectPathVTable DBusObjectPathVTable |

Set of functions that must be implemented to handle messages sent to a particular object path.

Definition at line 56 of file dbus-connection.h.

## ◆ DBusPendingCall

|                                                |
|------------------------------------------------|
| typedef struct DBusPendingCall DBusPendingCall |

Opaque type representing a method call that has not yet received a reply.

Definition at line 52 of file dbus-connection.h.

## ◆ DBusPendingCallNotifyFunction

|  |
|----|
| typedef void(\* DBusPendingCallNotifyFunction) (DBusPendingCall \*pending, void \*user_data) |

Called when a pending call now has a reply available.

Set with dbus_pending_call_set_notify().

Definition at line 165 of file dbus-connection.h.

## ◆ DBusPreallocatedSend

|                                                          |
|----------------------------------------------------------|
| typedef struct DBusPreallocatedSend DBusPreallocatedSend |

Opaque type representing preallocated resources so a message can be sent without further memory allocation.

Definition at line 50 of file dbus-connection.h.

## ◆ DBusRemoveTimeoutFunction

|  |
|----|
| typedef void(\* DBusRemoveTimeoutFunction) (DBusTimeout \*timeout, void \*data) |

Called when libdbus no longer needs a timeout to be monitored by the main loop.

Set by dbus_connection_set_timeout_functions() or dbus_server_set_timeout_functions().

Definition at line 126 of file dbus-connection.h.

## ◆ DBusRemoveWatchFunction

|  |
|----|
| typedef void(\* DBusRemoveWatchFunction) (DBusWatch \*watch, void \*data) |

Called when libdbus no longer needs a watch to be monitored by the main loop.

Set by dbus_connection_set_watch_functions() or dbus_server_set_watch_functions().

Definition at line 106 of file dbus-connection.h.

## ◆ DBusTimeout

|                                        |
|----------------------------------------|
| typedef struct DBusTimeout DBusTimeout |

Definition at line 48 of file dbus-connection.h.

## ◆ DBusTimeoutToggledFunction

|  |
|----|
| typedef void(\* DBusTimeoutToggledFunction) (DBusTimeout \*timeout, void \*data) |

Called when dbus_timeout_get_enabled() may return a different value than it did before.

Set by dbus_connection_set_timeout_functions() or dbus_server_set_timeout_functions().

Definition at line 120 of file dbus-connection.h.

## ◆ DBusWakeupMainFunction

|                                                       |
|-------------------------------------------------------|
| typedef void(\* DBusWakeupMainFunction) (void \*data) |

Called when the main loop's thread should be notified that there's now work to do.

Set with dbus_connection_set_wakeup_main_function().

Definition at line 138 of file dbus-connection.h.

## ◆ DBusWatch

|                                    |
|------------------------------------|
| typedef struct DBusWatch DBusWatch |

Definition at line 46 of file dbus-connection.h.

## ◆ DBusWatchToggledFunction

|  |
|----|
| typedef void(\* DBusWatchToggledFunction) (DBusWatch \*watch, void \*data) |

Called when dbus_watch_get_enabled() may return a different value than it did before.

Set by dbus_connection_set_watch_functions() or dbus_server_set_watch_functions().

Definition at line 100 of file dbus-connection.h.

## Enumeration Type Documentation

## ◆ DBusDispatchStatus

|                         |
|-------------------------|
| enum DBusDispatchStatus |

Indicates the status of incoming data on a DBusConnection.

This determines whether dbus_connection_dispatch() needs to be called.

| Enumerator |  |
|----|----|
| DBUS_DISPATCH_DATA_REMAINS  | There is more data to potentially convert to messages. |
| DBUS_DISPATCH_COMPLETE  | All currently available data has been processed. |
| DBUS_DISPATCH_NEED_MEMORY  | More memory is needed to continue. |

Definition at line 82 of file dbus-connection.h.

## ◆ DBusWatchFlags

|                     |
|---------------------|
| enum DBusWatchFlags |

Indicates the status of a DBusWatch.

| Enumerator |  |
|----|----|
| DBUS_WATCH_READABLE  | As in POLLIN. |
| DBUS_WATCH_WRITABLE  | As in POLLOUT. |
| DBUS_WATCH_ERROR  | As in POLLERR (can't watch for this, but can be present in current state passed to dbus_watch_handle()). |
| DBUS_WATCH_HANGUP  | As in POLLHUP (can't watch for it, but can be present in current state passed to dbus_watch_handle()). |

Definition at line 61 of file dbus-connection.h.

## Function Documentation

## ◆ \_dbus_connection_get_credentials()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusCredentials \* \_dbus_connection_get_credentials | ( | DBusConnection \*  | *connection* | ) |  |

Definition at line 5402 of file dbus-connection.c.

## ◆ \_dbus_connection_get_linux_security_label()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_connection_get_linux_security_label | ( | DBusConnection \*  | *connection*, |
|  |  | char \*\*  | *label_p*  |
|  | ) |  |  |

Definition at line 5377 of file dbus-connection.c.

## ◆ dbus_connection_add_filter()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_add_filter | ( | DBusConnection \*  | *connection*, |
|  |  | DBusHandleMessageFunction  | *function*, |
|  |  | void \*  | *user_data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Adds a message filter.

Filters are handlers that are run on all incoming messages, prior to the objects registered with dbus_connection_register_object_path(). Filters are run in the order that they were added. The same handler can be added as a filter more than once, in which case it will be run more than once. Filters added during a filter callback won't be run on the message being processed.

Parameters  
|                    |                                       |
|--------------------|---------------------------------------|
| connection         | the connection                        |
| function           | function to handle messages           |
| user_data          | user data to pass to the function     |
| free_data_function | function to use for freeing user data |

<!-- -->

Returns  
TRUE on success, FALSE if not enough memory.

Definition at line 5638 of file dbus-connection.c.

References \_dbus_atomic_inc(), \_dbus_list_append(), dbus_new0, FALSE, filter_list, DBusMessageFilter::free_user_data_function, DBusMessageFilter::function, NULL, DBusMessageFilter::refcount, TRUE, and DBusMessageFilter::user_data.

## ◆ dbus_connection_allocate_data_slot()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_allocate_data_slot | ( | dbus_int32_t \*  | *slot_p* | ) |  |

Allocates an integer ID to be used for storing application-specific data on any DBusConnection.

The allocated ID may then be used with dbus_connection_set_data() and dbus_connection_get_data(). The passed-in slot must be initialized to -1, and is filled in with the slot ID. If the passed-in slot is not -1, it's assumed to be already allocated, and its refcount is incremented.

The allocated slot is global, i.e. all DBusConnection objects will have a slot with the given integer ID reserved.

Parameters  
|        |                                               |
|--------|-----------------------------------------------|
| slot_p | address of a global variable storing the slot |

<!-- -->

Returns  
FALSE on failure (no memory)

Definition at line 6047 of file dbus-connection.c.

References \_dbus_data_slot_allocator_alloc().

## ◆ dbus_connection_borrow_message()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_connection_borrow_message | ( | DBusConnection \*  | *connection* | ) |  |

Returns the first-received message from the incoming message queue, leaving it in the queue.

If the queue is empty, returns NULL.

The caller does not own a reference to the returned message, and must either return it using dbus_connection_return_message() or keep it after calling dbus_connection_steal_borrowed_message(). No one can get at the message while its borrowed, so return it as quickly as possible and don't keep a reference to it after returning it. If you need to keep the message, make a copy of it.

dbus_connection_dispatch() will block if called while a borrowed message is outstanding; only one piece of code can be playing with the incoming queue at a time. This function will block if called during a dbus_connection_dispatch().

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

<!-- -->

Returns  
next message in the incoming queue.

Definition at line 3866 of file dbus-connection.c.

References \_dbus_assert, \_dbus_list_get_first(), dbus_connection_get_dispatch_status(), DBUS_DISPATCH_DATA_REMAINS, incoming_messages, message_borrowed, and NULL.

## ◆ dbus_connection_can_send_type()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_can_send_type | ( | DBusConnection \*  | *connection*, |
|  |  | int  | *type*  |
|  | ) |  |  |

Tests whether a certain type can be send via the connection.

This will always return TRUE for all types, with the exception of DBUS_TYPE_UNIX_FD. The function will return TRUE for DBUS_TYPE_UNIX_FD only on systems that know Unix file descriptors and can send them via the chosen transport and when the remote side supports this.

This function can be used to do runtime checking for types that might be unknown to the specific D-Bus client implementation version, i.e. it will return FALSE for all types this implementation does not know, including invalid or reserved types.

Parameters  
|            |                   |
|------------|-------------------|
| connection | the connection    |
| type       | the type to check |

<!-- -->

Returns  
TRUE if the type may be send via the connection

Definition at line 3120 of file dbus-connection.c.

References \_dbus_transport_can_pass_unix_fd(), dbus_type_is_valid(), DBUS_TYPE_UNIX_FD, FALSE, NULL, transport, and TRUE.

## ◆ dbus_connection_close()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_connection_close | ( | DBusConnection \*  | *connection* | ) |  |

Closes a private connection, so no further data can be sent or received.

This disconnects the transport (such as a socket) underlying the connection.

Attempts to send messages after closing a connection are safe, but will result in error replies generated locally in libdbus.

This function does not affect the connection's reference count. It's safe to close a connection more than once; all calls after the first do nothing. It's impossible to "reopen" a connection, a new connection must be created. This function may result in a call to the DBusDispatchStatusFunction set with dbus_connection_set_dispatch_status_function(), as the disconnect message it generates needs to be dispatched.

If a connection is dropped by the remote application, it will close itself.

You must close a connection prior to releasing the last reference to the connection. If you dbus_connection_unref() for the last time without closing the connection, the results are undefined; it is a bug in your program and libdbus will try to print a warning.

You may not close a shared connection. Connections created with dbus_connection_open() or dbus_bus_get() are shared. These connections are owned by libdbus, and applications should only unref them, never close them. Applications can know it is safe to unref these connections because libdbus will be holding a reference as long as the connection is open. Thus, either the connection is closed and it is OK to drop the last reference, or the connection is open and the app knows it does not have the last reference.

Connections created with dbus_connection_open_private() or dbus_bus_get_private() are not kept track of or referenced by libdbus. The creator of these connections is responsible for calling dbus_connection_close() prior to releasing the last reference, if the connection is not already disconnected.

Parameters  
|            |                                            |
|------------|--------------------------------------------|
| connection | the private (unshared) connection to close |

Definition at line 2947 of file dbus-connection.c.

References \_dbus_current_generation, \_dbus_warn_check_failed(), NULL, and shareable.

## ◆ dbus_connection_dispatch()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusDispatchStatus dbus_connection_dispatch | ( | DBusConnection \*  | *connection* | ) |  |

Processes any incoming data.

If there's incoming raw data that has not yet been parsed, it is parsed, which may or may not result in adding messages to the incoming queue.

The incoming data buffer is filled when the connection reads from its underlying transport (such as a socket). Reading usually happens in dbus_watch_handle() or dbus_connection_read_write().

If there are complete messages in the incoming queue, dbus_connection_dispatch() removes one message from the queue and processes it. Processing has three steps.

First, any method replies are passed to DBusPendingCall or dbus_connection_send_with_reply_and_block() in order to complete the pending method call.

Second, any filters registered with dbus_connection_add_filter() are run. If any filter returns DBUS_HANDLER_RESULT_HANDLED then processing stops after that filter.

Third, if the message is a method call it is forwarded to any registered object path handlers added with dbus_connection_register_object_path() or dbus_connection_register_fallback().

A single call to dbus_connection_dispatch() will process at most one message; it will not clear the entire message queue.

Be careful about calling dbus_connection_dispatch() from inside a message handler, i.e. calling dbus_connection_dispatch() recursively. If threads have been initialized with a recursive mutex function, then this will not deadlock; however, it can certainly confuse your application.

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
dispatch status, see dbus_connection_get_dispatch_status()

Definition at line 4591 of file dbus-connection.c.

References \_dbus_connection_ref_unlocked(), \_dbus_hash_table_lookup_int(), \_dbus_list_alloc_link(), \_dbus_list_clear_full(), \_dbus_list_copy(), \_dbus_list_free_link(), \_dbus_list_get_first_link(), \_dbus_list_get_next_link, \_dbus_list_prepend_link(), \_dbus_object_tree_dispatch_and_unlock(), \_dbus_string_append_printf(), \_dbus_string_free(), \_dbus_string_get_const_data(), \_dbus_string_init(), builtin_filters_enabled, DBusList::data, dbus_connection_unref(), DBUS_DISPATCH_COMPLETE, DBUS_DISPATCH_DATA_REMAINS, DBUS_DISPATCH_NEED_MEMORY, DBUS_ERROR_UNKNOWN_METHOD, DBUS_ERROR_UNKNOWN_OBJECT, DBUS_HANDLER_RESULT_HANDLED, DBUS_HANDLER_RESULT_NEED_MEMORY, DBUS_HANDLER_RESULT_NOT_YET_HANDLED, dbus_message_get_interface(), dbus_message_get_member(), dbus_message_get_reply_serial(), dbus_message_get_signature(), dbus_message_get_type(), dbus_message_new_error(), DBUS_MESSAGE_TYPE_METHOD_CALL, dbus_message_type_to_string(), dbus_message_unref(), expired_messages, filter_list, DBusMessageFilter::function, NULL, objects, pending_replies, and DBusMessageFilter::user_data.

## ◆ dbus_connection_flush()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_connection_flush | ( | DBusConnection \*  | *connection* | ) |  |

Blocks until the outgoing message queue is empty.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

Definition at line 3657 of file dbus-connection.c.

References NULL.

## ◆ dbus_connection_free_data_slot()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_connection_free_data_slot | ( | dbus_int32_t \*  | *slot_p* | ) |  |

Deallocates a global ID for connection data slots.

dbus_connection_get_data() and dbus_connection_set_data() may no longer be used with this slot. Existing data stored on existing DBusConnection objects will be freed when the connection is finalized, but may not be retrieved (and may only be replaced if someone else reallocates the slot). When the refcount on the passed-in slot reaches 0, it is set to -1.

Parameters  
|        |                                        |
|--------|----------------------------------------|
| slot_p | address storing the slot to deallocate |

Definition at line 6065 of file dbus-connection.c.

References \_dbus_data_slot_allocator_free().

## ◆ dbus_connection_free_preallocated_send()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_free_preallocated_send | ( | DBusConnection \*  | *connection*, |
|  |  | DBusPreallocatedSend \*  | *preallocated*  |
|  | ) |  |  |

Frees preallocated message-sending resources from dbus_connection_preallocate_send().

Should only be called if the preallocated resources are not used to send a message.

Parameters  
|              |                |
|--------------|----------------|
| connection   | the connection |
| preallocated | the resources  |

Definition at line 3206 of file dbus-connection.c.

References \_dbus_counter_unref(), \_dbus_list_free_link(), DBusPreallocatedSend::connection, DBusPreallocatedSend::counter_link, DBusList::data, dbus_free(), NULL, and DBusPreallocatedSend::queue_link.

## ◆ dbus_connection_get_adt_audit_session_data()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_get_adt_audit_session_data | ( | DBusConnection \*  | *connection*, |
|  |  | void \*\*  | *data*, |
|  |  | dbus_int32_t \*  | *data_size*  |
|  | ) |  |  |

Gets the ADT audit data of the connection if any.

Returns TRUE if the structure pointer is returned. Always returns FALSE prior to authenticating the connection.

Parameters  
|            |                                          |
|------------|------------------------------------------|
| connection | the connection                           |
| data       | return location for audit data           |
| data_size  | return location for length of audit data |

<!-- -->

Returns  
TRUE if audit data is filled in with a valid ucred pointer

Definition at line 5309 of file dbus-connection.c.

References \_dbus_transport_get_adt_audit_session_data(), \_dbus_transport_try_to_authenticate(), FALSE, NULL, and transport.

## ◆ dbus_connection_get_data()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void \* dbus_connection_get_data | ( | DBusConnection \*  | *connection*, |
|  |  | dbus_int32_t  | *slot*  |
|  | ) |  |  |

Retrieves data previously set with dbus_connection_set_data().

The slot must still be allocated (must not have been freed).

Note  
This function does not take the main thread lock on DBusConnection, which allows it to be used from inside watch and timeout functions. (See the note in docs for dbus_connection_set_watch_functions().) A side effect of this is that you need to know there's a reference held on the connection while invoking dbus_connection_get_data(), or the connection could be finalized during dbus_connection_get_data().

<!-- -->

Parameters  
|            |                           |
|------------|---------------------------|
| connection | the connection            |
| slot       | the slot to get data from |

<!-- -->

Returns  
the data, or NULL if not found

Definition at line 6144 of file dbus-connection.c.

References \_dbus_data_slot_list_get(), NULL, and slot_list.

## ◆ dbus_connection_get_dispatch_status()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusDispatchStatus dbus_connection_get_dispatch_status | ( | DBusConnection \*  | *connection* | ) |  |

Gets the current state of the incoming message queue.

DBUS_DISPATCH_DATA_REMAINS indicates that the message queue may contain messages. DBUS_DISPATCH_COMPLETE indicates that the incoming queue is empty. DBUS_DISPATCH_NEED_MEMORY indicates that there could be data, but we can't know for sure without more memory.

To process the incoming message queue, use dbus_connection_dispatch() or (in rare cases) dbus_connection_pop_message().

Note, DBUS_DISPATCH_DATA_REMAINS really means that either we have messages in the queue, or we have raw bytes buffered up that need to be parsed. When these bytes are parsed, they may not add up to an entire message. Thus, it's possible to see a status of DBUS_DISPATCH_DATA_REMAINS but not have a message yet.

In particular this happens on initial connection, because all sorts of authentication protocol stuff has to be parsed before the first message arrives.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

<!-- -->

Returns  
current dispatch status

Definition at line 4394 of file dbus-connection.c.

References DBUS_DISPATCH_COMPLETE, and NULL.

Referenced by dbus_connection_borrow_message(), and dbus_connection_pop_message().

## ◆ dbus_connection_get_is_anonymous()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_get_is_anonymous | ( | DBusConnection \*  | *connection* | ) |  |

Gets whether the connection is not authenticated as a specific user.

If the connection is not authenticated, this function returns TRUE, and if it is authenticated but as an anonymous user, it returns TRUE. If it is authenticated as a specific user, then this returns FALSE. (Note that if the connection was authenticated as anonymous then disconnected, this function still returns TRUE.)

If the connection is not anonymous, you can use dbus_connection_get_unix_user() and dbus_connection_get_windows_user() to see who it's authorized as.

If you want to prevent non-anonymous authorization, use dbus_server_set_auth_mechanisms() to remove the mechanisms that allow proving user identity (i.e. only allow the ANONYMOUS mechanism).

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
TRUE if not authenticated or authenticated as anonymous

Definition at line 3044 of file dbus-connection.c.

References \_dbus_transport_get_is_anonymous(), FALSE, NULL, and transport.

## ◆ dbus_connection_get_is_authenticated()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_get_is_authenticated | ( | DBusConnection \*  | *connection* | ) |  |

Gets whether the connection was authenticated.

(Note that if the connection was authenticated then disconnected, this function still returns TRUE)

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
TRUE if the connection was ever authenticated

Definition at line 3010 of file dbus-connection.c.

References \_dbus_transport_try_to_authenticate(), FALSE, NULL, and transport.

## ◆ dbus_connection_get_is_connected()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_get_is_connected | ( | DBusConnection \*  | *connection* | ) |  |

Gets whether the connection is currently open.

A connection may become disconnected when the remote application closes its end, or exits; a connection may also be disconnected with dbus_connection_close().

There are not separate states for "closed" and "disconnected," the two terms are synonymous. This function should really be called get_is_open() but for historical reasons is not.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

<!-- -->

Returns  
TRUE if the connection is still alive.

Definition at line 2988 of file dbus-connection.c.

References FALSE, and NULL.

## ◆ dbus_connection_get_max_message_size()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT long dbus_connection_get_max_message_size | ( | DBusConnection \*  | *connection* | ) |  |

Gets the value set by dbus_connection_set_max_message_size().

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
the max size of a single message

Definition at line 6205 of file dbus-connection.c.

References \_dbus_transport_get_max_message_size(), NULL, and transport.

## ◆ dbus_connection_get_max_message_unix_fds()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT long dbus_connection_get_max_message_unix_fds | ( | DBusConnection \*  | *connection* | ) |  |

Gets the value set by dbus_connection_set_max_message_unix_fds().

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
the max numer of unix fds of a single message

Definition at line 6244 of file dbus-connection.c.

References \_dbus_transport_get_max_message_unix_fds(), NULL, and transport.

## ◆ dbus_connection_get_max_received_size()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT long dbus_connection_get_max_received_size | ( | DBusConnection \*  | *connection* | ) |  |

Gets the value set by dbus_connection_set_max_received_size().

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
the max size of all live messages

Definition at line 6300 of file dbus-connection.c.

References \_dbus_transport_get_max_received_size(), NULL, and transport.

## ◆ dbus_connection_get_max_received_unix_fds()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT long dbus_connection_get_max_received_unix_fds | ( | DBusConnection \*  | *connection* | ) |  |

Gets the value set by dbus_connection_set_max_received_unix_fds().

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
the max unix fds of all live messages

Definition at line 6342 of file dbus-connection.c.

References \_dbus_transport_get_max_received_unix_fds(), NULL, and transport.

## ◆ dbus_connection_get_object_path_data()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_get_object_path_data | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *path*, |
|  |  | void \*\*  | *data_p*  |
|  | ) |  |  |

Gets the user data passed to dbus_connection_register_object_path() or dbus_connection_register_fallback().

If nothing was registered at this path, the data is filled in with NULL.

Parameters  
|            |                                          |
|------------|------------------------------------------|
| connection | the connection                           |
| path       | the path you registered with             |
| data_p     | location to store the user data, or NULL |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 5968 of file dbus-connection.c.

References \_dbus_decompose_path(), \_dbus_object_tree_get_user_data_unlocked(), dbus_free_string_array(), FALSE, NULL, objects, and TRUE.

## ◆ dbus_connection_get_outgoing_size()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT long dbus_connection_get_outgoing_size | ( | DBusConnection \*  | *connection* | ) |  |

Gets the approximate size in bytes of all messages in the outgoing message queue.

The size is approximate in that you shouldn't use it to decide how many bytes to read off the network or anything of that nature, as optimizations may choose to tell small white lies to avoid performance overhead.

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
the number of bytes that have been queued up but not sent

Definition at line 6365 of file dbus-connection.c.

References \_dbus_counter_get_size_value(), NULL, and outgoing_counter.

## ◆ dbus_connection_get_outgoing_unix_fds()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT long dbus_connection_get_outgoing_unix_fds | ( | DBusConnection \*  | *connection* | ) |  |

Gets the approximate number of uni fds of all messages in the outgoing message queue.

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
the number of unix fds that have been queued up but not sent

Definition at line 6426 of file dbus-connection.c.

References \_dbus_counter_get_unix_fd_value(), NULL, and outgoing_counter.

## ◆ dbus_connection_get_server_id()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT char \* dbus_connection_get_server_id | ( | DBusConnection \*  | *connection* | ) |  |

Gets the ID of the server address we are authenticated to, if this connection is on the client side.

If the connection is on the server side, this will always return NULL - use dbus_server_get_id() to get the ID of your own server, if you are the server side.

If a client-side connection is not authenticated yet, the ID may be available if it was included in the server address, but may not be available. The only way to be sure the server ID is available is to wait for authentication to complete.

In general, each mode of connecting to a given server will have its own ID. So for example, if the session bus daemon is listening on UNIX domain sockets and on TCP, then each of those modalities will have its own server ID.

If you want an ID that identifies an entire session bus, look at dbus_bus_get_id() instead (which is just a convenience wrapper around the org.freedesktop.DBus.GetId method invoked on the bus).

You can also get a machine ID; see dbus_try_get_local_machine_id() to get the machine you are on. There isn't a convenience wrapper, but you can invoke org.freedesktop.DBus.Peer.GetMachineId on any peer to get the machine ID on the other end.

The D-Bus specification describes the server ID and other IDs in a bit more detail.

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
the server ID or NULL if no memory or the connection is server-side

Definition at line 3089 of file dbus-connection.c.

References \_dbus_strdup(), \_dbus_transport_get_server_id(), NULL, and transport.

## ◆ dbus_connection_get_socket()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_get_socket | ( | DBusConnection \*  | *connection*, |
|  |  | int \*  | *fd*  |
|  | ) |  |  |

Gets the underlying Windows or UNIX socket file descriptor of the connection, if any.

DO NOT read or write to the file descriptor, or try to select() on it; use DBusWatch for main loop integration. Not all connections will have a socket. So for adding descriptors to the main loop, use dbus_watch_get_socket() and so forth.

If the connection is not socket-based, this function will return FALSE, even if the connection does have a file descriptor of some kind. i.e. this function always returns specifically a socket file descriptor.

Parameters  
|            |                                          |
|------------|------------------------------------------|
| connection | the connection                           |
| fd         | return location for the file descriptor. |

<!-- -->

Returns  
TRUE if fd is successfully obtained.

Definition at line 5193 of file dbus-connection.c.

References \_dbus_transport_get_socket_fd(), FALSE, NULL, and transport.

Referenced by dbus_connection_get_unix_fd().

## ◆ dbus_connection_get_unix_fd()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_get_unix_fd | ( | DBusConnection \*  | *connection*, |
|  |  | int \*  | *fd*  |
|  | ) |  |  |

Get the UNIX file descriptor of the connection, if any.

This can be used for SELinux access control checks with getpeercon() for example. DO NOT read or write to the file descriptor, or try to select() on it; use DBusWatch for main loop integration. Not all connections will have a file descriptor. So for adding descriptors to the main loop, use dbus_watch_get_unix_fd() and so forth.

If the connection is socket-based, you can also use dbus_connection_get_socket(), which will work on Windows too. This function always fails on Windows.

Right now the returned descriptor is always a socket, but that is not guaranteed.

Parameters  
|            |                                          |
|------------|------------------------------------------|
| connection | the connection                           |
| fd         | return location for the file descriptor. |

<!-- -->

Returns  
TRUE if fd is successfully obtained.

Definition at line 5163 of file dbus-connection.c.

References dbus_connection_get_socket(), FALSE, NULL, and transport.

## ◆ dbus_connection_get_unix_process_id()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_get_unix_process_id | ( | DBusConnection \*  | *connection*, |
|  |  | unsigned long \*  | *pid*  |
|  | ) |  |  |

Gets the process ID of the connection if any.

Returns TRUE if the pid is filled in. Always returns FALSE prior to authenticating the connection.

Parameters  
|            |                                    |
|------------|------------------------------------|
| connection | the connection                     |
| pid        | return location for the process ID |

<!-- -->

Returns  
TRUE if uid is filled in with a valid process ID

Definition at line 5276 of file dbus-connection.c.

References \_dbus_transport_get_unix_process_id(), \_dbus_transport_try_to_authenticate(), FALSE, NULL, and transport.

## ◆ dbus_connection_get_unix_user()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_get_unix_user | ( | DBusConnection \*  | *connection*, |
|  |  | unsigned long \*  | *uid*  |
|  | ) |  |  |

Gets the UNIX user ID of the connection if known.

Returns TRUE if the uid is filled in. Always returns FALSE on non-UNIX platforms for now, though in theory someone could hook Windows to NIS or something. Always returns FALSE prior to authenticating the connection.

The UID is only read by servers from clients; clients can't usually get the UID of servers, because servers do not authenticate to clients. The returned UID is the UID the connection authenticated as.

The message bus is a server and the apps connecting to the bus are clients.

You can ask the bus to tell you the UID of another connection though if you like; this is done with dbus_bus_get_unix_user().

Parameters  
|            |                                 |
|------------|---------------------------------|
| connection | the connection                  |
| uid        | return location for the user ID |

<!-- -->

Returns  
TRUE if uid is filled in with a valid user ID

Definition at line 5240 of file dbus-connection.c.

References \_dbus_assert, \_dbus_transport_get_unix_user(), \_dbus_transport_try_to_authenticate(), FALSE, NULL, and transport.

## ◆ dbus_connection_get_windows_user()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_get_windows_user | ( | DBusConnection \*  | *connection*, |
|  |  | char \*\*  | *windows_sid_p*  |
|  | ) |  |  |

Gets the Windows user SID of the connection if known.

Returns TRUE if the ID is filled in. Always returns FALSE on non-Windows platforms for now, though in theory someone could hook UNIX to Active Directory or something. Always returns FALSE prior to authenticating the connection.

The user is only read by servers from clients; clients can't usually get the user of servers, because servers do not authenticate to clients. The returned user is the user the connection authenticated as.

The message bus is a server and the apps connecting to the bus are clients.

The returned user string has to be freed with dbus_free().

The return value indicates whether the user SID is available; if it's available but we don't have the memory to copy it, then the return value is TRUE and NULL is given as the SID.

Parameters  
|  |  |
|----|----|
| connection | the connection |
| windows_sid_p | return location for an allocated copy of the user ID, or NULL if no memory |

<!-- -->

Returns  
TRUE if user is available (returned value may be NULL anyway if no memory)

Definition at line 5452 of file dbus-connection.c.

References \_dbus_assert, \_dbus_transport_get_windows_user(), \_dbus_transport_try_to_authenticate(), FALSE, NULL, and transport.

## ◆ dbus_connection_has_messages_to_send()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_has_messages_to_send | ( | DBusConnection \*  | *connection* | ) |  |

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

## ◆ dbus_connection_list_registered()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_list_registered | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *parent_path*, |
|  |  | char \*\*\*  | *child_entries*  |
|  | ) |  |  |

Lists the registered fallback handlers and object path handlers at the given parent_path.

The returned array should be freed with dbus_free_string_array().

Parameters  
|               |                                           |
|---------------|-------------------------------------------|
| connection    | the connection                            |
| parent_path   | the path to list the child handlers of    |
| child_entries | returns NULL-terminated array of children |

<!-- -->

Returns  
FALSE if no memory to allocate the child entries

Definition at line 6005 of file dbus-connection.c.

References \_dbus_decompose_path(), \_dbus_object_tree_list_registered_and_unlock(), dbus_free_string_array(), FALSE, NULL, and objects.

## ◆ dbus_connection_open()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT DBusConnection \* dbus_connection_open | ( | const char \*  | *address*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Gets a connection to a remote address.

If a connection to the given address already exists, returns the existing connection with its reference count incremented. Otherwise, returns a new connection and saves the new connection for possible re-use if a future call to dbus_connection_open() asks to connect to the same server.

Use dbus_connection_open_private() to get a dedicated connection not shared with other callers of dbus_connection_open().

If the open fails, the function returns NULL, and provides a reason for the failure in the error parameter. Pass NULL for the error parameter if you aren't interested in the reason for failure.

Because this connection is shared, no user of the connection may call dbus_connection_close(). However, when you are done with the connection you should call dbus_connection_unref().

Note  
Prefer dbus_connection_open() to dbus_connection_open_private() unless you have good reason; connections are expensive enough that it's wasteful to create lots of connections to the same server.

<!-- -->

Parameters  
|         |                                         |
|---------|-----------------------------------------|
| address | the address.                            |
| error   | address where an error can be returned. |

<!-- -->

Returns  
new connection, or NULL on failure.

Definition at line 2635 of file dbus-connection.c.

References NULL, and TRUE.

## ◆ dbus_connection_open_private()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT DBusConnection \* dbus_connection_open_private | ( | const char \*  | *address*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Opens a new, dedicated connection to a remote address.

Unlike dbus_connection_open(), always creates a new connection. This connection will not be saved or recycled by libdbus.

If the open fails, the function returns NULL, and provides a reason for the failure in the error parameter. Pass NULL for the error parameter if you aren't interested in the reason for failure.

When you are done with this connection, you must dbus_connection_close() to disconnect it, and dbus_connection_unref() to free the connection object.

(The dbus_connection_close() can be skipped if the connection is already known to be disconnected, for example if you are inside a handler for the Disconnected signal.)

Note  
Prefer dbus_connection_open() to dbus_connection_open_private() unless you have good reason; connections are expensive enough that it's wasteful to create lots of connections to the same server.

<!-- -->

Parameters  
|         |                                         |
|---------|-----------------------------------------|
| address | the address.                            |
| error   | address where an error can be returned. |

<!-- -->

Returns  
new connection, or NULL on failure.

Definition at line 2678 of file dbus-connection.c.

References FALSE, and NULL.

## ◆ dbus_connection_pop_message()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_connection_pop_message | ( | DBusConnection \*  | *connection* | ) |  |

Returns the first-received message from the incoming message queue, removing it from the queue.

The caller owns a reference to the returned message. If the queue is empty, returns NULL.

This function bypasses any message handlers that are registered, and so using it is usually wrong. Instead, let the main loop invoke dbus_connection_dispatch(). Popping messages manually is only useful in very simple programs that don't share a DBusConnection with any libraries or other modules.

There is a lock that covers all ways of accessing the incoming message queue, so dbus_connection_dispatch(), dbus_connection_pop_message(), dbus_connection_borrow_message(), etc. will all block while one of the others in the group is running.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

<!-- -->

Returns  
next message in the incoming queue.

Definition at line 4107 of file dbus-connection.c.

References dbus_connection_get_dispatch_status(), DBUS_DISPATCH_DATA_REMAINS, and NULL.

## ◆ dbus_connection_preallocate_send()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusPreallocatedSend \* dbus_connection_preallocate_send | ( | DBusConnection \*  | *connection* | ) |  |

Preallocates resources needed to send a message, allowing the message to be sent without the possibility of memory allocation failure.

Allows apps to create a future guarantee that they can send a message regardless of memory shortages.

Parameters  
|            |                                         |
|------------|-----------------------------------------|
| connection | the connection we're preallocating for. |

<!-- -->

Returns  
the preallocated resources, or NULL

Definition at line 3180 of file dbus-connection.c.

References NULL.

## ◆ dbus_connection_read_write()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_read_write | ( | DBusConnection \*  | *connection*, |
|  |  | int  | *timeout_milliseconds*  |
|  | ) |  |  |

This function is intended for use with applications that don't want to write a main loop and deal with DBusWatch and DBusTimeout.

See also dbus_connection_read_write_dispatch().

As long as the connection is open, this function will block until it can read or write, then read or write, then return TRUE.

If the connection is closed, the function returns FALSE.

The return value indicates whether reading or writing is still possible, i.e. whether the connection is connected.

Note that even after disconnection, messages may remain in the incoming queue that need to be processed. dbus_connection_read_write_dispatch() dispatches incoming messages for you; with dbus_connection_read_write() you have to arrange to drain the incoming queue yourself.

Parameters  
|                      |                                      |
|----------------------|--------------------------------------|
| connection           | the connection                       |
| timeout_milliseconds | max time to block or -1 for infinite |

<!-- -->

Returns  
TRUE if still connected

Definition at line 3817 of file dbus-connection.c.

References FALSE, and NULL.

## ◆ dbus_connection_read_write_dispatch()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_read_write_dispatch | ( | DBusConnection \*  | *connection*, |
|  |  | int  | *timeout_milliseconds*  |
|  | ) |  |  |

This function is intended for use with applications that don't want to write a main loop and deal with DBusWatch and DBusTimeout.

An example usage would be:

while (dbus_connection_read_write_dispatch (connection, -1))

; // empty loop body

dbus_connection_read_write_dispatch

dbus_bool_t dbus_connection_read_write_dispatch(DBusConnection \*connection, int timeout_milliseconds)

This function is intended for use with applications that don't want to write a main loop and deal wit...

**Definition** dbus-connection.c:3785

In this usage you would normally have set up a filter function to look at each message as it is dispatched. The loop terminates when the last message from the connection (the disconnected signal) is processed.

If there are messages to dispatch, this function will dbus_connection_dispatch() once, and return. If there are no messages to dispatch, this function will block until it can read or write, then read or write, then return.

The way to think of this function is that it either makes some sort of progress, or it blocks. Note that, while it is blocked on I/O, it cannot be interrupted (even by other threads), which makes this function unsuitable for applications that do more than just react to received messages.

The return value indicates whether the disconnect message has been processed, NOT whether the connection is connected. This is important because even after disconnecting, you want to process any messages you received prior to the disconnect.

Parameters  
|                      |                                      |
|----------------------|--------------------------------------|
| connection           | the connection                       |
| timeout_milliseconds | max time to block or -1 for infinite |

<!-- -->

Returns  
TRUE if the disconnect message has not been processed

Definition at line 3785 of file dbus-connection.c.

References FALSE, NULL, and TRUE.

## ◆ dbus_connection_ref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT DBusConnection \* dbus_connection_ref | ( | DBusConnection \*  | *connection* | ) |  |

Increments the reference count of a DBusConnection.

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

<!-- -->

Returns  
the connection.

Definition at line 2700 of file dbus-connection.c.

References \_dbus_atomic_inc(), \_dbus_current_generation, NULL, and refcount.

## ◆ dbus_connection_register_fallback()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_register_fallback | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *path*, |
|  |  | const DBusObjectPathVTable \*  | *vtable*, |
|  |  | void \*  | *user_data*  |
|  | ) |  |  |

Registers a fallback handler for a given subsection of the object hierarchy.

The given vtable handles messages at or below the given path. You can use this to establish a default message handling policy for a whole "subdirectory."

It is a bug to call this function for object paths which already have a handler. Use dbus_connection_try_register_fallback() if this might be the case.

Parameters  
|            |                                         |
|------------|-----------------------------------------|
| connection | the connection                          |
| path       | a '/' delimited string of path elements |
| vtable     | the virtual table                       |
| user_data  | data to pass to functions in the vtable |

<!-- -->

Returns  
FALSE if an error (DBUS_ERROR_NO_MEMORY or DBUS_ERROR_OBJECT_PATH_IN_USE) occured

Definition at line 5901 of file dbus-connection.c.

References \_dbus_warn(), dbus_error_free(), dbus_error_has_name(), DBUS_ERROR_INIT, DBUS_ERROR_OBJECT_PATH_IN_USE, FALSE, DBusError::message, NULL, and TRUE.

## ◆ dbus_connection_register_object_path()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_register_object_path | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *path*, |
|  |  | const DBusObjectPathVTable \*  | *vtable*, |
|  |  | void \*  | *user_data*  |
|  | ) |  |  |

Registers a handler for a given path in the object hierarchy.

The given vtable handles messages sent to exactly the given path.

It is a bug to call this function for object paths which already have a handler. Use dbus_connection_try_register_object_path() if this might be the case.

Parameters  
|            |                                         |
|------------|-----------------------------------------|
| connection | the connection                          |
| path       | a '/' delimited string of path elements |
| vtable     | the virtual table                       |
| user_data  | data to pass to functions in the vtable |

<!-- -->

Returns  
FALSE if an error (DBUS_ERROR_NO_MEMORY or DBUS_ERROR_OBJECT_PATH_IN_USE) ocurred

Definition at line 5829 of file dbus-connection.c.

References \_dbus_warn(), dbus_error_free(), dbus_error_has_name(), DBUS_ERROR_INIT, DBUS_ERROR_OBJECT_PATH_IN_USE, FALSE, DBusError::message, and NULL.

## ◆ dbus_connection_remove_filter()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_remove_filter | ( | DBusConnection \*  | *connection*, |
|  |  | DBusHandleMessageFunction  | *function*, |
|  |  | void \*  | *user_data*  |
|  | ) |  |  |

Removes a previously-added message filter.

It is a programming error to call this function for a handler that has not been added as a filter. If the given handler was added more than once, only one instance of it will be removed (the most recently-added instance).

Parameters  
|            |                                     |
|------------|-------------------------------------|
| connection | the connection                      |
| function   | the handler to remove               |
| user_data  | user data for the handler to remove |

Definition at line 5690 of file dbus-connection.c.

References \_dbus_list_get_last_link(), \_dbus_list_get_prev_link, \_dbus_list_remove_link(), \_dbus_warn_check_failed(), DBusList::data, filter_list, DBusMessageFilter::free_user_data_function, DBusMessageFilter::function, NULL, and DBusMessageFilter::user_data.

## ◆ dbus_connection_return_message()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_return_message | ( | DBusConnection \*  | *connection*, |
|  |  | DBusMessage \*  | *message*  |
|  | ) |  |  |

Used to return a message after peeking at it using dbus_connection_borrow_message().

Only called if message from dbus_connection_borrow_message() was non-NULL.

Parameters  
|            |                                                   |
|------------|---------------------------------------------------|
| connection | the connection                                    |
| message    | the message from dbus_connection_borrow_message() |

Definition at line 3917 of file dbus-connection.c.

References \_dbus_assert, dispatch_acquired, message_borrowed, and NULL.

## ◆ dbus_connection_send()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_send | ( | DBusConnection \*  | *connection*, |
|  |  | DBusMessage \*  | *message*, |
|  |  | dbus_uint32_t \*  | *serial*  |
|  | ) |  |  |

Adds a message to the outgoing message queue.

Does not block to write the message to the network; that happens asynchronously. To force the message to be written, call dbus_connection_flush() however it is not necessary to call dbus_connection_flush() by hand; the message will be sent the next time the main loop is run. dbus_connection_flush() should only be used, for example, if the application was expected to exit before running the main loop.

Because this only queues the message, the only reason it can fail is lack of memory. Even if the connection is disconnected, no error will be returned. If the function fails due to lack of memory, it returns FALSE. The function will never fail for other reasons; even if the connection is disconnected, you can queue an outgoing message, though obviously it won't be sent.

The message serial is used by the remote application to send a reply; see dbus_message_get_serial() or the D-Bus specification.

dbus_message_unref() can be called as soon as this method returns as the message queue will hold its own ref until the message is sent.

Parameters  
|            |                                                               |
|------------|---------------------------------------------------------------|
| connection | the connection.                                               |
| message    | the message to write.                                         |
| serial     | return location for message serial, or NULL if you don't care |

<!-- -->

Returns  
TRUE on success.

Definition at line 3317 of file dbus-connection.c.

References \_dbus_connection_send_and_unlock(), \_dbus_transport_can_pass_unix_fd(), FALSE, NULL, and transport.

## ◆ dbus_connection_send_preallocated()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_send_preallocated | ( | DBusConnection \*  | *connection*, |
|  |  | DBusPreallocatedSend \*  | *preallocated*, |
|  |  | DBusMessage \*  | *message*, |
|  |  | dbus_uint32_t \*  | *client_serial*  |
|  | ) |  |  |

Sends a message using preallocated resources.

This function cannot fail. It works identically to dbus_connection_send() in other respects. Preallocated resources comes from dbus_connection_preallocate_send(). This function "consumes" the preallocated resources, they need not be freed separately.

Parameters  
|               |                                                           |
|---------------|-----------------------------------------------------------|
| connection    | the connection                                            |
| preallocated  | the preallocated resources                                |
| message       | the message to send                                       |
| client_serial | return location for client serial assigned to the message |

Definition at line 3232 of file dbus-connection.c.

References \_dbus_transport_can_pass_unix_fd(), DBusPreallocatedSend::connection, dbus_message_get_interface(), dbus_message_get_member(), dbus_message_get_type(), DBUS_MESSAGE_TYPE_METHOD_CALL, DBUS_MESSAGE_TYPE_SIGNAL, NULL, and transport.

## ◆ dbus_connection_send_with_reply()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_send_with_reply | ( | DBusConnection \*  | *connection*, |
|  |  | DBusMessage \*  | *message*, |
|  |  | DBusPendingCall \*\*  | *pending_return*, |
|  |  | int  | *timeout_milliseconds*  |
|  | ) |  |  |

Queues a message to send, as with dbus_connection_send(), but also returns a DBusPendingCall used to receive a reply to the message.

If no reply is received in the given timeout_milliseconds, this function expires the pending reply and generates a synthetic error reply (generated in-process, not by the remote application) indicating that a timeout occurred.

A DBusPendingCall will see a reply message before any filters or registered object path handlers. See dbus_connection_dispatch() for details on when handlers are run.

A DBusPendingCall will always see exactly one reply message, unless it's cancelled with dbus_pending_call_cancel().

If NULL is passed for the pending_return, the DBusPendingCall will still be generated internally, and used to track the message reply timeout. This means a timeout error will occur if no reply arrives, unlike with dbus_connection_send().

If -1 is passed for the timeout, a sane default timeout is used. -1 is typically the best value for the timeout for this reason, unless you want a very short or very long timeout. If DBUS_TIMEOUT_INFINITE is passed for the timeout, no timeout will be set and the call will block forever.

Warning  
if the connection is disconnected or you try to send Unix file descriptors on a connection that does not support them, the DBusPendingCall will be set to NULL, so be careful with this.

<!-- -->

Parameters  
|  |  |
|----|----|
| connection | the connection |
| message | the message to send |
| pending_return | return location for a DBusPendingCall object, or NULL if connection is disconnected or when you try to send Unix file descriptors on a connection that does not support them. The caller owns this reference, and is responsible for calling dbus_pending_call_unref() when it is no longer needed. |
| timeout_milliseconds | timeout in milliseconds, -1 (or DBUS_TIMEOUT_USE_DEFAULT) for default or DBUS_TIMEOUT_INFINITE for no timeout |

<!-- -->

Returns  
FALSE if no memory, TRUE otherwise.

Definition at line 3415 of file dbus-connection.c.

References \_dbus_connection_get_next_client_serial(), \_dbus_pending_call_new_unlocked(), \_dbus_pending_call_set_timeout_error_unlocked(), \_dbus_transport_can_pass_unix_fd(), dbus_message_get_serial(), dbus_message_set_serial(), dbus_pending_call_unref(), FALSE, NULL, transport, and TRUE.

Referenced by dbus_connection_send_with_reply_and_block().

## ◆ dbus_connection_send_with_reply_and_block()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT DBusMessage \* dbus_connection_send_with_reply_and_block | ( | DBusConnection \*  | *connection*, |
|  |  | DBusMessage \*  | *message*, |
|  |  | int  | *timeout_milliseconds*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Sends a message and blocks a certain time period while waiting for a reply.

This function does not reenter the main loop, i.e. messages other than the reply are queued up but not processed. This function is used to invoke method calls on a remote object.

If a normal reply is received, it is returned, and removed from the incoming message queue. If it is not received, NULL is returned and the error is set to DBUS_ERROR_NO_REPLY. If an error reply is received, it is converted to a DBusError and returned as an error, then the reply message is deleted and NULL is returned. If something else goes wrong, result is set to whatever is appropriate, such as DBUS_ERROR_NO_MEMORY or DBUS_ERROR_DISCONNECTED.

Warning  
While this function blocks the calling thread will not be processing the incoming message queue. This means you can end up deadlocked if the application you're talking to needs you to reply to a method. To solve this, either avoid the situation, block in a separate thread from the main connection-dispatching thread, or use dbus_pending_call_set_notify() to avoid blocking.

<!-- -->

Parameters  
|  |  |
|----|----|
| connection | the connection |
| message | the message to send |
| timeout_milliseconds | timeout in milliseconds, -1 (or DBUS_TIMEOUT_USE_DEFAULT) for default or DBUS_TIMEOUT_INFINITE for no timeout |
| error | return location for error message |

<!-- -->

Returns  
the message that is the reply or NULL with an error code if the function fails.

Definition at line 3551 of file dbus-connection.c.

References \_dbus_assert, \_dbus_transport_can_pass_unix_fd(), dbus_connection_send_with_reply(), DBUS_ERROR_DISCONNECTED, DBUS_ERROR_FAILED, dbus_message_unref(), dbus_pending_call_block(), dbus_pending_call_steal_reply(), dbus_pending_call_unref(), dbus_set_error(), dbus_set_error_from_message(), NULL, and transport.

Referenced by dbus_bus_get_id(), dbus_bus_get_unix_user(), dbus_bus_name_has_owner(), dbus_bus_register(), dbus_bus_release_name(), dbus_bus_request_name(), and dbus_bus_start_service_by_name().

## ◆ dbus_connection_set_allow_anonymous()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_allow_anonymous | ( | DBusConnection \*  | *connection*, |
|  |  | dbus_bool_t  | *value*  |
|  | ) |  |  |

This function must be called on the server side of a connection when the connection is first seen in the DBusNewConnectionFunction.

If set to TRUE (the default is FALSE), then the connection can proceed even if the client does not authenticate as some user identity, i.e. clients can connect anonymously.

This setting interacts with the available authorization mechanisms (see dbus_server_set_auth_mechanisms()). Namely, an auth mechanism such as ANONYMOUS that supports anonymous auth must be included in the list of available mechanisms for anonymous login to work.

This setting also changes the default rule for connections authorized as a user; normally, if a connection authorizes as a user identity, it is permitted if the user identity is root or the user identity matches the user identity of the server process. If anonymous connections are allowed, however, then any user identity is allowed.

You can override the rules for connections authorized as a user identity with dbus_connection_set_unix_user_function() and dbus_connection_set_windows_user_function().

Parameters  
|            |                                                      |
|------------|------------------------------------------------------|
| connection | the connection                                       |
| value      | whether to allow authentication as an anonymous user |

Definition at line 5546 of file dbus-connection.c.

References \_dbus_transport_set_allow_anonymous(), NULL, and transport.

## ◆ dbus_connection_set_builtin_filters_enabled()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_builtin_filters_enabled | ( | DBusConnection \*  | *connection*, |
|  |  | dbus_bool_t  | *value*  |
|  | ) |  |  |

Enables the builtin filtering of messages.

Currently the only filtering implemented by libdbus and mandated by the spec is that of peer messages.

If TRUE, DBusConnection automatically handles all messages to the org.freedesktop.DBus.Peer interface. For monitors this can break the specification if the response is sending a message.

If FALSE, the result is similar to calling dbus_connection_set_route_peer_messages() with argument TRUE, but messages with a NULL destination are also dispatched to the application instead of being passed to the built-in filters.

If a normal application disables this flag, it can break things badly. So only unset this if you are a monitor.

Parameters  
|            |                                                         |
|------------|---------------------------------------------------------|
| connection | the connection                                          |
| value      | TRUE to pass through org.freedesktop.DBus.Peer messages |

Definition at line 5578 of file dbus-connection.c.

References builtin_filters_enabled, and NULL.

## ◆ dbus_connection_set_change_sigpipe()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_change_sigpipe | ( | dbus_bool_t  | *will_modify_sigpipe* | ) |  |

This function sets a global flag for whether dbus_connection_new() will set SIGPIPE behavior to SIG_IGN.

Parameters  
|                     |                                            |
|---------------------|--------------------------------------------|
| will_modify_sigpipe | TRUE to allow sigpipe to be set to SIG_IGN |

Definition at line 6170 of file dbus-connection.c.

References \_dbus_atomic_set_nonzero(), and \_dbus_atomic_set_zero().

## ◆ dbus_connection_set_data()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_set_data | ( | DBusConnection \*  | *connection*, |
|  |  | dbus_int32_t  | *slot*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_func*  |
|  | ) |  |  |

Stores a pointer on a DBusConnection, along with an optional function to be used for freeing the data when the data is set again, or when the connection is finalized.

The slot number must have been allocated with dbus_connection_allocate_data_slot().

Note  
This function does not take the main thread lock on DBusConnection, which allows it to be used from inside watch and timeout functions. (See the note in docs for dbus_connection_set_watch_functions().) A side effect of this is that you need to know there's a reference held on the connection while invoking dbus_connection_set_data(), or the connection could be finalized during dbus_connection_set_data().

<!-- -->

Parameters  
|                |                                 |
|----------------|---------------------------------|
| connection     | the connection                  |
| slot           | the slot number                 |
| data           | the data to store               |
| free_data_func | finalizer function for the data |

<!-- -->

Returns  
TRUE if there was enough memory to store the data

Definition at line 6095 of file dbus-connection.c.

References \_dbus_data_slot_list_set(), FALSE, NULL, and slot_list.

## ◆ dbus_connection_set_dispatch_status_function()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_dispatch_status_function | ( | DBusConnection \*  | *connection*, |
|  |  | DBusDispatchStatusFunction  | *function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Set a function to be invoked when the dispatch status changes.

If the dispatch status is DBUS_DISPATCH_DATA_REMAINS, then dbus_connection_dispatch() needs to be called to process incoming messages. However, dbus_connection_dispatch() MUST NOT BE CALLED from inside the DBusDispatchStatusFunction. Indeed, almost any reentrancy in this function is a bad idea. Instead, the DBusDispatchStatusFunction should simply save an indication that messages should be dispatched later, when the main loop is re-entered.

If you don't set a dispatch status function, you have to be sure to dispatch on every iteration of your main loop, especially if dbus_watch_handle() or dbus_timeout_handle() were called.

Parameters  
|                    |                                             |
|--------------------|---------------------------------------------|
| connection         | the connection                              |
| function           | function to call on dispatch status changes |
| data               | data for function                           |
| free_data_function | free the function data                      |

Definition at line 5118 of file dbus-connection.c.

References dispatch_status_data, dispatch_status_function, free_dispatch_status_data, and NULL.

## ◆ dbus_connection_set_exit_on_disconnect()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_exit_on_disconnect | ( | DBusConnection \*  | *connection*, |
|  |  | dbus_bool_t  | *exit_on_disconnect*  |
|  | ) |  |  |

Set whether \_exit() should be called when the connection receives a disconnect signal.

The call to \_exit() comes after any handlers for the disconnect signal run; handlers can cancel the exit by calling this function.

By default, exit_on_disconnect is FALSE; but for message bus connections returned from dbus_bus_get() it will be toggled on by default.

Parameters  
|  |  |
|----|----|
| connection | the connection |
| exit_on_disconnect | TRUE if \_exit() should be called after a disconnect signal |

Definition at line 3160 of file dbus-connection.c.

References exit_on_disconnect, FALSE, and NULL.

## ◆ dbus_connection_set_max_message_size()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_max_message_size | ( | DBusConnection \*  | *connection*, |
|  |  | long  | *size*  |
|  | ) |  |  |

Specifies the maximum size message this connection is allowed to receive.

Larger messages will result in disconnecting the connection.

Parameters  
|            |                                                           |
|------------|-----------------------------------------------------------|
| connection | a DBusConnection                                          |
| size       | maximum message size the connection can receive, in bytes |

Definition at line 6187 of file dbus-connection.c.

References \_dbus_transport_set_max_message_size(), NULL, and transport.

## ◆ dbus_connection_set_max_message_unix_fds()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_max_message_unix_fds | ( | DBusConnection \*  | *connection*, |
|  |  | long  | *n*  |
|  | ) |  |  |

Specifies the maximum number of unix fds a message on this connection is allowed to receive.

Messages with more unix fds will result in disconnecting the connection.

Parameters  
|            |                                                     |
|------------|-----------------------------------------------------|
| connection | a DBusConnection                                    |
| n          | maximum message unix fds the connection can receive |

Definition at line 6226 of file dbus-connection.c.

References \_dbus_transport_set_max_message_unix_fds(), NULL, and transport.

## ◆ dbus_connection_set_max_received_size()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_max_received_size | ( | DBusConnection \*  | *connection*, |
|  |  | long  | *size*  |
|  | ) |  |  |

Sets the maximum total number of bytes that can be used for all messages received on this connection.

Messages count toward the maximum until they are finalized. When the maximum is reached, the connection will not read more data until some messages are finalized.

The semantics of the maximum are: if outstanding messages are already above the maximum, additional messages will not be read. The semantics are not: if the next message would cause us to exceed the maximum, we don't read it. The reason is that we don't know the size of a message until after we read it.

Thus, the max live messages size can actually be exceeded by up to the maximum size of a single message.

Also, if we read say 1024 bytes off the wire in a single read(), and that contains a half-dozen small messages, we may exceed the size max by that amount. But this should be inconsequential.

This does imply that we can't call read() with a buffer larger than we're willing to exceed this limit by.

Parameters  
|            |                                                       |
|------------|-------------------------------------------------------|
| connection | the connection                                        |
| size       | the maximum size in bytes of all outstanding messages |

Definition at line 6282 of file dbus-connection.c.

References \_dbus_transport_set_max_received_size(), NULL, and transport.

## ◆ dbus_connection_set_max_received_unix_fds()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_max_received_unix_fds | ( | DBusConnection \*  | *connection*, |
|  |  | long  | *n*  |
|  | ) |  |  |

Sets the maximum total number of unix fds that can be used for all messages received on this connection.

Messages count toward the maximum until they are finalized. When the maximum is reached, the connection will not read more data until some messages are finalized.

The semantics are analogous to those of dbus_connection_set_max_received_size().

Parameters  
|            |                                                       |
|------------|-------------------------------------------------------|
| connection | the connection                                        |
| n          | the maximum size in bytes of all outstanding messages |

Definition at line 6324 of file dbus-connection.c.

References \_dbus_transport_set_max_received_unix_fds(), NULL, and transport.

## ◆ dbus_connection_set_route_peer_messages()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_route_peer_messages | ( | DBusConnection \*  | *connection*, |
|  |  | dbus_bool_t  | *value*  |
|  | ) |  |  |

Normally DBusConnection automatically handles all messages to the org.freedesktop.DBus.Peer interface.

However, the message bus wants to be able to route methods on that interface through the bus and to other applications. If routing peer messages is enabled, then messages with the org.freedesktop.DBus.Peer interface that also have a bus destination name set will not be automatically handled by the DBusConnection and instead will be dispatched normally to the application.

If a normal application sets this flag, it can break things badly. So don't set this unless you are the message bus.

Parameters  
|  |  |
|----|----|
| connection | the connection |
| value | TRUE to pass through org.freedesktop.DBus.Peer messages with a bus name set |

Definition at line 5606 of file dbus-connection.c.

References NULL, and route_peer_messages.

## ◆ dbus_connection_set_timeout_functions()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_set_timeout_functions | ( | DBusConnection \*  | *connection*, |
|  |  | DBusAddTimeoutFunction  | *add_function*, |
|  |  | DBusRemoveTimeoutFunction  | *remove_function*, |
|  |  | DBusTimeoutToggledFunction  | *toggled_function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets the timeout functions for the connection.

These functions are responsible for making the application's main loop aware of timeouts. When using Qt, typically the DBusAddTimeoutFunction would create a QTimer. When using GLib, the DBusAddTimeoutFunction would call g_timeout_add.

The DBusTimeoutToggledFunction notifies the application that the timeout has been enabled or disabled. Call dbus_timeout_get_enabled() to check this. A disabled timeout should have no effect, and enabled timeout should be added to the main loop. This feature is used instead of simply adding/removing the timeout because enabling/disabling can be done without memory allocation. With Qt, QTimer::start() and QTimer::stop() can be used to enable and disable. The toggled function may be NULL if a main loop re-queries dbus_timeout_get_enabled() every time anyway. Whenever a timeout is toggled, its interval may change.

The DBusTimeout can be queried for the timer interval using dbus_timeout_get_interval(). dbus_timeout_handle() should be called repeatedly, each time the interval elapses, starting after it has elapsed once. The timeout stops firing when it is removed with the given remove_function. The timer interval may change whenever the timeout is added, removed, or toggled.

Note  
The thread lock on DBusConnection is held while timeout functions are invoked, so inside these functions you may not invoke any methods on DBusConnection or it will deadlock. See the comments in the code or http://lists.freedesktop.org/archives/dbus/2007-July/thread.html#8144 if you encounter this issue and want to attempt writing a patch.

<!-- -->

Parameters  
|                    |                                                   |
|--------------------|---------------------------------------------------|
| connection         | the connection.                                   |
| add_function       | function to add a timeout.                        |
| remove_function    | function to remove a timeout.                     |
| toggled_function   | function to notify of enable/disable              |
| data               | data to pass to add_function and remove_function. |
| free_data_function | function to be called to free the data.           |

<!-- -->

Returns  
FALSE on failure (no memory)

Definition at line 5034 of file dbus-connection.c.

References \_dbus_timeout_list_set_functions(), FALSE, NULL, and timeouts.

## ◆ dbus_connection_set_unix_user_function()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_unix_user_function | ( | DBusConnection \*  | *connection*, |
|  |  | DBusAllowUnixUserFunction  | *function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets a predicate function used to determine whether a given user ID is allowed to connect.

When an incoming connection has authenticated with a particular user ID, this function is called; if it returns TRUE, the connection is allowed to proceed, otherwise the connection is disconnected.

If the function is set to NULL (as it is by default), then only the same UID as the server process will be allowed to connect. Also, root is always allowed to connect.

On Windows, the function will be set and its free_data_function will be invoked when the connection is freed or a new function is set. However, the function will never be called, because there are no UNIX user ids to pass to it, or at least none of the existing auth protocols would allow authenticating as a UNIX user on Windows.

Parameters  
|                    |                               |
|--------------------|-------------------------------|
| connection         | the connection                |
| function           | the predicate                 |
| data               | data to pass to the predicate |
| free_data_function | function to free the data     |

Definition at line 5355 of file dbus-connection.c.

References \_dbus_transport_set_unix_user_function(), NULL, and transport.

## ◆ dbus_connection_set_wakeup_main_function()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_wakeup_main_function | ( | DBusConnection \*  | *connection*, |
|  |  | DBusWakeupMainFunction  | *wakeup_main_function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets the mainloop wakeup function for the connection.

This function is responsible for waking up the main loop (if its sleeping in another thread) when some some change has happened to the connection that the mainloop needs to reconsider (e.g. a message has been queued for writing). When using Qt, this typically results in a call to QEventLoop::wakeUp(). When using GLib, it would call g_main_context_wakeup().

Parameters  
|                      |                                         |
|----------------------|-----------------------------------------|
| connection           | the connection.                         |
| wakeup_main_function | function to wake up the mainloop        |
| data                 | data to pass wakeup_main_function       |
| free_data_function   | function to be called to free the data. |

Definition at line 5072 of file dbus-connection.c.

References free_wakeup_main_data, NULL, wakeup_main_data, and wakeup_main_function.

## ◆ dbus_connection_set_watch_functions()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_set_watch_functions | ( | DBusConnection \*  | *connection*, |
|  |  | DBusAddWatchFunction  | *add_function*, |
|  |  | DBusRemoveWatchFunction  | *remove_function*, |
|  |  | DBusWatchToggledFunction  | *toggled_function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets the watch functions for the connection.

These functions are responsible for making the application's main loop aware of file descriptors that need to be monitored for events, using select() or poll(). When using Qt, typically the DBusAddWatchFunction would create a QSocketNotifier. When using GLib, the DBusAddWatchFunction could call g_io_add_watch(), or could be used as part of a more elaborate GSource. Note that when a watch is added, it may not be enabled.

The DBusWatchToggledFunction notifies the application that the watch has been enabled or disabled. Call dbus_watch_get_enabled() to check this. A disabled watch should have no effect, and enabled watch should be added to the main loop. This feature is used instead of simply adding/removing the watch because enabling/disabling can be done without memory allocation. The toggled function may be NULL if a main loop re-queries dbus_watch_get_enabled() every time anyway.

The DBusWatch can be queried for the file descriptor to watch using dbus_watch_get_unix_fd() or dbus_watch_get_socket(), and for the events to watch for using dbus_watch_get_flags(). The flags returned by dbus_watch_get_flags() will only contain DBUS_WATCH_READABLE and DBUS_WATCH_WRITABLE, never DBUS_WATCH_HANGUP or DBUS_WATCH_ERROR; all watches implicitly include a watch for hangups, errors, and other exceptional conditions.

Once a file descriptor becomes readable or writable, or an exception occurs, dbus_watch_handle() should be called to notify the connection of the file descriptor's condition.

dbus_watch_handle() cannot be called during the DBusAddWatchFunction, as the connection will not be ready to handle that watch yet.

It is not allowed to reference a DBusWatch after it has been passed to remove_function.

If FALSE is returned due to lack of memory, the failure may be due to a FALSE return from the new add_function. If so, the add_function may have been called successfully one or more times, but the remove_function will also have been called to remove any successful adds. i.e. if FALSE is returned the net result should be that dbus_connection_set_watch_functions() has no effect, but the add_function and remove_function may have been called.

Note  
The thread lock on DBusConnection is held while watch functions are invoked, so inside these functions you may not invoke any methods on DBusConnection or it will deadlock. See the comments in the code or http://lists.freedesktop.org/archives/dbus/2007-July/tread.html#8144 if you encounter this issue and want to attempt writing a patch.

<!-- -->

Parameters  
|                    |                                                   |
|--------------------|---------------------------------------------------|
| connection         | the connection.                                   |
| add_function       | function to begin monitoring a new descriptor.    |
| remove_function    | function to stop monitoring a descriptor.         |
| toggled_function   | function to notify of enable/disable              |
| data               | data to pass to add_function and remove_function. |
| free_data_function | function to be called to free the data.           |

<!-- -->

Returns  
FALSE on failure (no memory)

Definition at line 4971 of file dbus-connection.c.

References \_dbus_watch_list_set_functions(), FALSE, NULL, and watches.

## ◆ dbus_connection_set_windows_user_function()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_set_windows_user_function | ( | DBusConnection \*  | *connection*, |
|  |  | DBusAllowWindowsUserFunction  | *function*, |
|  |  | void \*  | *data*, |
|  |  | DBusFreeFunction  | *free_data_function*  |
|  | ) |  |  |

Sets a predicate function used to determine whether a given user ID is allowed to connect.

When an incoming connection has authenticated with a particular user ID, this function is called; if it returns TRUE, the connection is allowed to proceed, otherwise the connection is disconnected.

If the function is set to NULL (as it is by default), then only the same user owning the server process will be allowed to connect.

On UNIX, the function will be set and its free_data_function will be invoked when the connection is freed or a new function is set. However, the function will never be called, because there is no way right now to authenticate as a Windows user on UNIX.

Parameters  
|                    |                               |
|--------------------|-------------------------------|
| connection         | the connection                |
| function           | the predicate                 |
| data               | data to pass to the predicate |
| free_data_function | function to free the data     |

Definition at line 5499 of file dbus-connection.c.

References \_dbus_transport_set_windows_user_function(), NULL, and transport.

## ◆ dbus_connection_steal_borrowed_message()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_connection_steal_borrowed_message | ( | DBusConnection \*  | *connection*, |
|  |  | DBusMessage \*  | *message*  |
|  | ) |  |  |

Used to keep a message after peeking at it using dbus_connection_borrow_message().

Before using this function, see the caveats/warnings in the documentation for dbus_connection_pop_message().

Parameters  
|            |                                                   |
|------------|---------------------------------------------------|
| connection | the connection                                    |
| message    | the message from dbus_connection_borrow_message() |

Definition at line 3951 of file dbus-connection.c.

References \_dbus_assert, \_dbus_list_pop_first(), dispatch_acquired, incoming_messages, message_borrowed, n_incoming, and NULL.

## ◆ dbus_connection_try_register_fallback()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_try_register_fallback | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *path*, |
|  |  | const DBusObjectPathVTable \*  | *vtable*, |
|  |  | void \*  | *user_data*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Registers a fallback handler for a given subsection of the object hierarchy.

The given vtable handles messages at or below the given path. You can use this to establish a default message handling policy for a whole "subdirectory."

Parameters  
|            |                                         |
|------------|-----------------------------------------|
| connection | the connection                          |
| path       | a '/' delimited string of path elements |
| vtable     | the virtual table                       |
| user_data  | data to pass to functions in the vtable |
| error      | address where an error can be returned  |

<!-- -->

Returns  
FALSE if an error (DBUS_ERROR_NO_MEMORY or DBUS_ERROR_OBJECT_PATH_IN_USE) is reported

Definition at line 5869 of file dbus-connection.c.

References FALSE, NULL, and TRUE.

## ◆ dbus_connection_try_register_object_path()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_try_register_object_path | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *path*, |
|  |  | const DBusObjectPathVTable \*  | *vtable*, |
|  |  | void \*  | *user_data*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Registers a handler for a given path in the object hierarchy.

The given vtable handles messages sent to exactly the given path.

Parameters  
|            |                                         |
|------------|-----------------------------------------|
| connection | the connection                          |
| path       | a '/' delimited string of path elements |
| vtable     | the virtual table                       |
| user_data  | data to pass to functions in the vtable |
| error      | address where an error can be returned  |

<!-- -->

Returns  
FALSE if an error (DBUS_ERROR_NO_MEMORY or DBUS_ERROR_OBJECT_PATH_IN_USE) is reported

Definition at line 5799 of file dbus-connection.c.

References FALSE, and NULL.

## ◆ dbus_connection_unref()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT void dbus_connection_unref | ( | DBusConnection \*  | *connection* | ) |  |

Decrements the reference count of a DBusConnection, and finalizes it if the count reaches zero.

Note: it is a bug to drop the last reference to a connection that is still connected.

For shared connections, libdbus will own a reference as long as the connection is connected, so you can know that either you don't have the last reference, or it's OK to drop the last reference. Most connections are shared. dbus_connection_open() and dbus_bus_get() return shared connections.

For private connections, the creator of the connection must arrange for dbus_connection_close() to be called prior to dropping the last reference. Private connections come from dbus_connection_open_private() or dbus_bus_get_private().

Parameters  
|            |                 |
|------------|-----------------|
| connection | the connection. |

Definition at line 2832 of file dbus-connection.c.

References \_dbus_atomic_dec(), \_dbus_current_generation, \_dbus_transport_get_is_connected(), \_dbus_warn_check_failed(), NULL, refcount, shareable, and transport.

Referenced by \_dbus_object_tree_unregister_and_unlock(), and dbus_connection_dispatch().

## ◆ dbus_connection_unregister_object_path()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_connection_unregister_object_path | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *path*  |
|  | ) |  |  |

Unregisters the handler registered with exactly the given path.

It's a bug to call this function for a path that isn't registered. Can unregister both fallback paths and object paths.

Parameters  
|            |                                         |
|------------|-----------------------------------------|
| connection | the connection                          |
| path       | a '/' delimited string of path elements |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 5936 of file dbus-connection.c.

References \_dbus_decompose_path(), \_dbus_object_tree_unregister_and_unlock(), dbus_free_string_array(), FALSE, NULL, objects, and TRUE.
