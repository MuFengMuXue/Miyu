DBusConnection Struct Reference

D-Bus secret internal implementation details » DBusConnection implementation details

Implementation details of DBusConnection. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-fields" class="groupheader"> Data Fields</h2></td>
</tr>
<tr id="r_a6fbf0227071fc20ffd5b0e79aef58e92" class="memitem:a6fbf0227071fc20ffd5b0e79aef58e92">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusAtomic </td>
<td class="memItemRight" data-valign="bottom">refcount</td>
</tr>
<tr class="memdesc:a6fbf0227071fc20ffd5b0e79aef58e92">
<td class="mdescLeft"> </td>
<td class="mdescRight">Reference count.<br />
</td>
</tr>
<tr class="separator:a6fbf0227071fc20ffd5b0e79aef58e92">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a98e26cfd09ddbf0238f90bf4965641bf" class="memitem:a98e26cfd09ddbf0238f90bf4965641bf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRMutex * </td>
<td class="memItemRight" data-valign="bottom">mutex</td>
</tr>
<tr class="memdesc:a98e26cfd09ddbf0238f90bf4965641bf">
<td class="mdescLeft"> </td>
<td class="mdescRight">Lock on the entire DBusConnection.<br />
</td>
</tr>
<tr class="separator:a98e26cfd09ddbf0238f90bf4965641bf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad9e7bf73a48f4951b24ce8eec7bb7ac5" class="memitem:ad9e7bf73a48f4951b24ce8eec7bb7ac5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCMutex * </td>
<td class="memItemRight" data-valign="bottom">dispatch_mutex</td>
</tr>
<tr class="memdesc:ad9e7bf73a48f4951b24ce8eec7bb7ac5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Protects dispatch_acquired.<br />
</td>
</tr>
<tr class="separator:ad9e7bf73a48f4951b24ce8eec7bb7ac5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a201f92bbc0947b503a36eaff9ae0ede9" class="memitem:a201f92bbc0947b503a36eaff9ae0ede9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCondVar * </td>
<td class="memItemRight" data-valign="bottom">dispatch_cond</td>
</tr>
<tr class="memdesc:a201f92bbc0947b503a36eaff9ae0ede9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Notify when dispatch_acquired is available.<br />
</td>
</tr>
<tr class="separator:a201f92bbc0947b503a36eaff9ae0ede9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aaad1c7d6e6ba3e049ef790f4f9aa35cd" class="memitem:aaad1c7d6e6ba3e049ef790f4f9aa35cd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCMutex * </td>
<td class="memItemRight" data-valign="bottom">io_path_mutex</td>
</tr>
<tr class="memdesc:aaad1c7d6e6ba3e049ef790f4f9aa35cd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Protects io_path_acquired.<br />
</td>
</tr>
<tr class="separator:aaad1c7d6e6ba3e049ef790f4f9aa35cd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a6d87e03eea7aaff53f5574efcfb8c3e4" class="memitem:a6d87e03eea7aaff53f5574efcfb8c3e4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCondVar * </td>
<td class="memItemRight" data-valign="bottom">io_path_cond</td>
</tr>
<tr class="memdesc:a6d87e03eea7aaff53f5574efcfb8c3e4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Notify when io_path_acquired is available.<br />
</td>
</tr>
<tr class="separator:a6d87e03eea7aaff53f5574efcfb8c3e4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a714fd51af8730c367b079594c7f756ae" class="memitem:a714fd51af8730c367b079594c7f756ae">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">outgoing_messages</td>
</tr>
<tr class="memdesc:a714fd51af8730c367b079594c7f756ae">
<td class="mdescLeft"> </td>
<td class="mdescRight">Queue of messages we need to send, send the end of the list first.<br />
</td>
</tr>
<tr class="separator:a714fd51af8730c367b079594c7f756ae">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aacb3a29956aa7712db37916194fde869" class="memitem:aacb3a29956aa7712db37916194fde869">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">incoming_messages</td>
</tr>
<tr class="memdesc:aacb3a29956aa7712db37916194fde869">
<td class="mdescLeft"> </td>
<td class="mdescRight">Queue of messages we have received, end of the list received most recently.<br />
</td>
</tr>
<tr class="separator:aacb3a29956aa7712db37916194fde869">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_afc069c0dc7f29123d432650580aec036" class="memitem:afc069c0dc7f29123d432650580aec036">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">expired_messages</td>
</tr>
<tr class="memdesc:afc069c0dc7f29123d432650580aec036">
<td class="mdescLeft"> </td>
<td class="mdescRight">Messages that will be released when we next unlock.<br />
</td>
</tr>
<tr class="separator:afc069c0dc7f29123d432650580aec036">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aef492b411cd2ebd214f8e4dd15e154af" class="memitem:aef492b411cd2ebd214f8e4dd15e154af">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusMessage * </td>
<td class="memItemRight" data-valign="bottom">message_borrowed</td>
</tr>
<tr class="memdesc:aef492b411cd2ebd214f8e4dd15e154af">
<td class="mdescLeft"> </td>
<td class="mdescRight">Filled in if the first incoming message has been borrowed; dispatch_acquired will be set by the borrower.<br />
</td>
</tr>
<tr class="separator:aef492b411cd2ebd214f8e4dd15e154af">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a07025e177949c5e65d5f983ac5f5e878" class="memitem:a07025e177949c5e65d5f983ac5f5e878">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_outgoing</td>
</tr>
<tr class="memdesc:a07025e177949c5e65d5f983ac5f5e878">
<td class="mdescLeft"> </td>
<td class="mdescRight">Length of outgoing queue.<br />
</td>
</tr>
<tr class="separator:a07025e177949c5e65d5f983ac5f5e878">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a9bda45f2d5c9af5c187fc31d7c98b424" class="memitem:a9bda45f2d5c9af5c187fc31d7c98b424">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">n_incoming</td>
</tr>
<tr class="memdesc:a9bda45f2d5c9af5c187fc31d7c98b424">
<td class="mdescLeft"> </td>
<td class="mdescRight">Length of incoming queue.<br />
</td>
</tr>
<tr class="separator:a9bda45f2d5c9af5c187fc31d7c98b424">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a5dcb660883904035076579c6d2f46501" class="memitem:a5dcb660883904035076579c6d2f46501">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCounter * </td>
<td class="memItemRight" data-valign="bottom">outgoing_counter</td>
</tr>
<tr class="memdesc:a5dcb660883904035076579c6d2f46501">
<td class="mdescLeft"> </td>
<td class="mdescRight">Counts size of outgoing messages.<br />
</td>
</tr>
<tr class="separator:a5dcb660883904035076579c6d2f46501">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a9855f1d7d5404770dd4aa09239c70b3b" class="memitem:a9855f1d7d5404770dd4aa09239c70b3b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTransport * </td>
<td class="memItemRight" data-valign="bottom">transport</td>
</tr>
<tr class="memdesc:a9855f1d7d5404770dd4aa09239c70b3b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Object that sends/receives messages over network.<br />
</td>
</tr>
<tr class="separator:a9855f1d7d5404770dd4aa09239c70b3b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_abdb6a32972d924531fb2cd80c7fd6d37" class="memitem:abdb6a32972d924531fb2cd80c7fd6d37">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWatchList * </td>
<td class="memItemRight" data-valign="bottom">watches</td>
</tr>
<tr class="memdesc:abdb6a32972d924531fb2cd80c7fd6d37">
<td class="mdescLeft"> </td>
<td class="mdescRight">Stores active watches.<br />
</td>
</tr>
<tr class="separator:abdb6a32972d924531fb2cd80c7fd6d37">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af3936ac5c968f2ac09bf05cf36025994" class="memitem:af3936ac5c968f2ac09bf05cf36025994">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusTimeoutList * </td>
<td class="memItemRight" data-valign="bottom">timeouts</td>
</tr>
<tr class="memdesc:af3936ac5c968f2ac09bf05cf36025994">
<td class="mdescLeft"> </td>
<td class="mdescRight">Stores active timeouts.<br />
</td>
</tr>
<tr class="separator:af3936ac5c968f2ac09bf05cf36025994">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a32d14cefcb4daea257544397755d45ed" class="memitem:a32d14cefcb4daea257544397755d45ed">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">filter_list</td>
</tr>
<tr class="memdesc:a32d14cefcb4daea257544397755d45ed">
<td class="mdescLeft"> </td>
<td class="mdescRight">List of filters.<br />
</td>
</tr>
<tr class="separator:a32d14cefcb4daea257544397755d45ed">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a773fb4ecd2738548dbbfbe6d1206da92" class="memitem:a773fb4ecd2738548dbbfbe6d1206da92">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusRMutex * </td>
<td class="memItemRight" data-valign="bottom">slot_mutex</td>
</tr>
<tr class="memdesc:a773fb4ecd2738548dbbfbe6d1206da92">
<td class="mdescLeft"> </td>
<td class="mdescRight">Lock on slot_list so overall connection lock need not be taken.<br />
</td>
</tr>
<tr class="separator:a773fb4ecd2738548dbbfbe6d1206da92">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0f805edcd9c09aaf45974510403dccbd" class="memitem:a0f805edcd9c09aaf45974510403dccbd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDataSlotList </td>
<td class="memItemRight" data-valign="bottom">slot_list</td>
</tr>
<tr class="memdesc:a0f805edcd9c09aaf45974510403dccbd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Data stored by allocated integer ID.<br />
</td>
</tr>
<tr class="separator:a0f805edcd9c09aaf45974510403dccbd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad8fa077f91fe62d0c10862e2ff9e86ca" class="memitem:ad8fa077f91fe62d0c10862e2ff9e86ca">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusHashTable * </td>
<td class="memItemRight" data-valign="bottom">pending_replies</td>
</tr>
<tr class="memdesc:ad8fa077f91fe62d0c10862e2ff9e86ca">
<td class="mdescLeft"> </td>
<td class="mdescRight">Hash of message serials to DBusPendingCall.<br />
</td>
</tr>
<tr class="separator:ad8fa077f91fe62d0c10862e2ff9e86ca">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a43d0bb9401103383e13ed3c99baf0daa" class="memitem:a43d0bb9401103383e13ed3c99baf0daa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uint32_t </td>
<td class="memItemRight" data-valign="bottom">client_serial</td>
</tr>
<tr class="memdesc:a43d0bb9401103383e13ed3c99baf0daa">
<td class="mdescLeft"> </td>
<td class="mdescRight">Client serial.<br />
</td>
</tr>
<tr class="separator:a43d0bb9401103383e13ed3c99baf0daa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aa70afc41f6184604c027e7f71a314d7f" class="memitem:aa70afc41f6184604c027e7f71a314d7f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusList * </td>
<td class="memItemRight" data-valign="bottom">disconnect_message_link</td>
</tr>
<tr class="memdesc:aa70afc41f6184604c027e7f71a314d7f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Preallocated list node for queueing the disconnection message.<br />
</td>
</tr>
<tr class="separator:aa70afc41f6184604c027e7f71a314d7f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a211104e37f65d45ab8fcb149e4bcc84e" class="memitem:a211104e37f65d45ab8fcb149e4bcc84e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusWakeupMainFunction </td>
<td class="memItemRight" data-valign="bottom">wakeup_main_function</td>
</tr>
<tr class="memdesc:a211104e37f65d45ab8fcb149e4bcc84e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function to wake up the mainloop<br />
<br />
</td>
</tr>
<tr class="separator:a211104e37f65d45ab8fcb149e4bcc84e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ac8aff7bafd9ed046d835c5ed80bc218c" class="memitem:ac8aff7bafd9ed046d835c5ed80bc218c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">wakeup_main_data</td>
</tr>
<tr class="memdesc:ac8aff7bafd9ed046d835c5ed80bc218c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Application data for wakeup_main_function.<br />
</td>
</tr>
<tr class="separator:ac8aff7bafd9ed046d835c5ed80bc218c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a8da896126df262503431acd73638c917" class="memitem:a8da896126df262503431acd73638c917">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_wakeup_main_data</td>
</tr>
<tr class="memdesc:a8da896126df262503431acd73638c917">
<td class="mdescLeft"> </td>
<td class="mdescRight">free wakeup_main_data<br />
</td>
</tr>
<tr class="separator:a8da896126df262503431acd73638c917">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af6cbafdf80cd474c654fc226581900a2" class="memitem:af6cbafdf80cd474c654fc226581900a2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDispatchStatusFunction </td>
<td class="memItemRight" data-valign="bottom">dispatch_status_function</td>
</tr>
<tr class="memdesc:af6cbafdf80cd474c654fc226581900a2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Function on dispatch status changes<br />
<br />
</td>
</tr>
<tr class="separator:af6cbafdf80cd474c654fc226581900a2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a0225f7934d1bd118ae2eeacf8a1c6f19" class="memitem:a0225f7934d1bd118ae2eeacf8a1c6f19">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">dispatch_status_data</td>
</tr>
<tr class="memdesc:a0225f7934d1bd118ae2eeacf8a1c6f19">
<td class="mdescLeft"> </td>
<td class="mdescRight">Application data for dispatch_status_function.<br />
</td>
</tr>
<tr class="separator:a0225f7934d1bd118ae2eeacf8a1c6f19">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a71f8b1e2078c4edb98c62de1886dfb2a" class="memitem:a71f8b1e2078c4edb98c62de1886dfb2a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusFreeFunction </td>
<td class="memItemRight" data-valign="bottom">free_dispatch_status_data</td>
</tr>
<tr class="memdesc:a71f8b1e2078c4edb98c62de1886dfb2a">
<td class="mdescLeft"> </td>
<td class="mdescRight">free dispatch_status_data<br />
</td>
</tr>
<tr class="separator:a71f8b1e2078c4edb98c62de1886dfb2a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_af3bbd2ecba171ebb8e952eaa030971d7" class="memitem:af3bbd2ecba171ebb8e952eaa030971d7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusDispatchStatus </td>
<td class="memItemRight" data-valign="bottom">last_dispatch_status</td>
</tr>
<tr class="memdesc:af3bbd2ecba171ebb8e952eaa030971d7">
<td class="mdescLeft"> </td>
<td class="mdescRight">The last dispatch status we reported to the application.<br />
</td>
</tr>
<tr class="separator:af3bbd2ecba171ebb8e952eaa030971d7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_acd289771721a459f4f9cdeaca0fa87c2" class="memitem:acd289771721a459f4f9cdeaca0fa87c2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusObjectTree * </td>
<td class="memItemRight" data-valign="bottom">objects</td>
</tr>
<tr class="memdesc:acd289771721a459f4f9cdeaca0fa87c2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Object path handlers registered with this connection.<br />
</td>
</tr>
<tr class="separator:acd289771721a459f4f9cdeaca0fa87c2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ad1abb7ad98db87f32b4abda22df075bd" class="memitem:ad1abb7ad98db87f32b4abda22df075bd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">server_guid</td>
</tr>
<tr class="memdesc:ad1abb7ad98db87f32b4abda22df075bd">
<td class="mdescLeft"> </td>
<td class="mdescRight">GUID of server if we are in shared_connections, NULL if server GUID is unknown or connection is private.<br />
</td>
</tr>
<tr class="separator:ad1abb7ad98db87f32b4abda22df075bd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a11803a01d74d956ef37e6aa092f0cf17" class="memitem:a11803a01d74d956ef37e6aa092f0cf17">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dispatch_acquired</td>
</tr>
<tr class="memdesc:a11803a01d74d956ef37e6aa092f0cf17">
<td class="mdescLeft"> </td>
<td class="mdescRight">Someone has dispatch path (can drain incoming queue)<br />
</td>
</tr>
<tr class="separator:a11803a01d74d956ef37e6aa092f0cf17">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a9f71e445534a4405075c33b5a075589f" class="memitem:a9f71e445534a4405075c33b5a075589f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">io_path_acquired</td>
</tr>
<tr class="memdesc:a9f71e445534a4405075c33b5a075589f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Someone has transport io path (can use the transport to read/write messages)<br />
</td>
</tr>
<tr class="separator:a9f71e445534a4405075c33b5a075589f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_aae47138b9b2494b65072ff300d631aa8" class="memitem:aae47138b9b2494b65072ff300d631aa8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">shareable: 1</td>
</tr>
<tr class="memdesc:aae47138b9b2494b65072ff300d631aa8">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE if libdbus owns a reference to the connection and can return it from dbus_connection_open() more than once<br />
</td>
</tr>
<tr class="separator:aae47138b9b2494b65072ff300d631aa8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a2a9f22339f90157f308a532462218404" class="memitem:a2a9f22339f90157f308a532462218404">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">exit_on_disconnect: 1</td>
</tr>
<tr class="memdesc:a2a9f22339f90157f308a532462218404">
<td class="mdescLeft"> </td>
<td class="mdescRight">If TRUE, exit after handling disconnect signal.<br />
</td>
</tr>
<tr class="separator:a2a9f22339f90157f308a532462218404">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a609bfcb8035950f7bef2cf24e14a6ef6" class="memitem:a609bfcb8035950f7bef2cf24e14a6ef6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">builtin_filters_enabled: 1</td>
</tr>
<tr class="memdesc:a609bfcb8035950f7bef2cf24e14a6ef6">
<td class="mdescLeft"> </td>
<td class="mdescRight">If TRUE, handle org.freedesktop.DBus.Peer messages automatically, whether they have a bus name or not.<br />
</td>
</tr>
<tr class="separator:a609bfcb8035950f7bef2cf24e14a6ef6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ab13bc36d7e6f91995768277ecbd5482c" class="memitem:ab13bc36d7e6f91995768277ecbd5482c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">route_peer_messages: 1</td>
</tr>
<tr class="memdesc:ab13bc36d7e6f91995768277ecbd5482c">
<td class="mdescLeft"> </td>
<td class="mdescRight">If TRUE, if org.freedesktop.DBus.Peer messages have a bus name, don't handle them automatically.<br />
</td>
</tr>
<tr class="separator:ab13bc36d7e6f91995768277ecbd5482c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a48d141d4311211e921571043bdbaeefb" class="memitem:a48d141d4311211e921571043bdbaeefb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">disconnected_message_arrived: 1</td>
</tr>
<tr class="memdesc:a48d141d4311211e921571043bdbaeefb">
<td class="mdescLeft"> </td>
<td class="mdescRight">We popped or are dispatching the disconnected message.<br />
</td>
</tr>
<tr class="separator:a48d141d4311211e921571043bdbaeefb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a3b2707b9d10d0643f91a8e027ae118b5" class="memitem:a3b2707b9d10d0643f91a8e027ae118b5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">disconnected_message_processed: 1</td>
</tr>
<tr class="memdesc:a3b2707b9d10d0643f91a8e027ae118b5">
<td class="mdescLeft"> </td>
<td class="mdescRight">We did our default handling of the disconnected message, such as closing the connection.<br />
</td>
</tr>
<tr class="separator:a3b2707b9d10d0643f91a8e027ae118b5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_a336a7953a4a28e55f6e6a07acfa11df3" class="memitem:a336a7953a4a28e55f6e6a07acfa11df3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned int </td>
<td class="memItemRight" data-valign="bottom">have_connection_lock: 1</td>
</tr>
<tr class="memdesc:a336a7953a4a28e55f6e6a07acfa11df3">
<td class="mdescLeft"> </td>
<td class="mdescRight">Used to check locking.<br />
</td>
</tr>
<tr class="separator:a336a7953a4a28e55f6e6a07acfa11df3">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Implementation details of DBusConnection.

All fields are private.

Definition at line 258 of file dbus-connection.c.

## Field Documentation

## ◆ builtin_filters_enabled

|                                                      |
|------------------------------------------------------|
| unsigned int DBusConnection::builtin_filters_enabled |

If TRUE, handle org.freedesktop.DBus.Peer messages automatically, whether they have a bus name or not.

Definition at line 321 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), dbus_connection_dispatch(), and dbus_connection_set_builtin_filters_enabled().

## ◆ client_serial

|                                             |
|---------------------------------------------|
| dbus_uint32_t DBusConnection::client_serial |

Client serial.

Increments each time a message is sent  

Definition at line 293 of file dbus-connection.c.

Referenced by \_dbus_connection_get_next_client_serial(), and \_dbus_connection_new_for_transport().

## ◆ disconnect_message_link

|                                                    |
|----------------------------------------------------|
| DBusList\* DBusConnection::disconnect_message_link |

Preallocated list node for queueing the disconnection message.

Definition at line 294 of file dbus-connection.c.

Referenced by \_dbus_connection_block_pending_call(), and \_dbus_connection_new_for_transport().

## ◆ disconnected_message_arrived

|                                                           |
|-----------------------------------------------------------|
| unsigned int DBusConnection::disconnected_message_arrived |

We popped or are dispatching the disconnected message.

if the disconnect_message_link is NULL then we queued it, but this flag is whether it got to the head of the queue.

Definition at line 325 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport().

## ◆ disconnected_message_processed

|                                                             |
|-------------------------------------------------------------|
| unsigned int DBusConnection::disconnected_message_processed |

We did our default handling of the disconnected message, such as closing the connection.

Definition at line 329 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport().

## ◆ dispatch_acquired

|                                               |
|-----------------------------------------------|
| dbus_bool_t DBusConnection::dispatch_acquired |

Someone has dispatch path (can drain incoming queue)

Definition at line 314 of file dbus-connection.c.

Referenced by dbus_connection_return_message(), and dbus_connection_steal_borrowed_message().

## ◆ dispatch_cond

|                                             |
|---------------------------------------------|
| DBusCondVar\* DBusConnection::dispatch_cond |

Notify when dispatch_acquired is available.

Definition at line 265 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport().

## ◆ dispatch_mutex

|                                             |
|---------------------------------------------|
| DBusCMutex\* DBusConnection::dispatch_mutex |

Protects dispatch_acquired.

Definition at line 264 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport().

## ◆ dispatch_status_data

|                                             |
|---------------------------------------------|
| void\* DBusConnection::dispatch_status_data |

Application data for dispatch_status_function.

Definition at line 301 of file dbus-connection.c.

Referenced by dbus_connection_set_dispatch_status_function().

## ◆ dispatch_status_function

|                                                                     |
|---------------------------------------------------------------------|
| DBusDispatchStatusFunction DBusConnection::dispatch_status_function |

Function on dispatch status changes  

Definition at line 300 of file dbus-connection.c.

Referenced by dbus_connection_set_dispatch_status_function().

## ◆ exit_on_disconnect

|                                                 |
|-------------------------------------------------|
| unsigned int DBusConnection::exit_on_disconnect |

If TRUE, exit after handling disconnect signal.

Definition at line 319 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), and dbus_connection_set_exit_on_disconnect().

## ◆ expired_messages

|                                             |
|---------------------------------------------|
| DBusList\* DBusConnection::expired_messages |

Messages that will be released when we next unlock.

Definition at line 271 of file dbus-connection.c.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_connection_unlock(), and dbus_connection_dispatch().

## ◆ filter_list

|                                        |
|----------------------------------------|
| DBusList\* DBusConnection::filter_list |

List of filters.

Definition at line 286 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), dbus_connection_add_filter(), dbus_connection_dispatch(), and dbus_connection_remove_filter().

## ◆ free_dispatch_status_data

|                                                            |
|------------------------------------------------------------|
| DBusFreeFunction DBusConnection::free_dispatch_status_data |

free dispatch_status_data

Definition at line 302 of file dbus-connection.c.

Referenced by dbus_connection_set_dispatch_status_function().

## ◆ free_wakeup_main_data

|                                                        |
|--------------------------------------------------------|
| DBusFreeFunction DBusConnection::free_wakeup_main_data |

free wakeup_main_data

Definition at line 298 of file dbus-connection.c.

Referenced by dbus_connection_set_wakeup_main_function().

## ◆ have_connection_lock

|                                                   |
|---------------------------------------------------|
| unsigned int DBusConnection::have_connection_lock |

Used to check locking.

Definition at line 334 of file dbus-connection.c.

## ◆ incoming_messages

|                                              |
|----------------------------------------------|
| DBusList\* DBusConnection::incoming_messages |

Queue of messages we have received, end of the list received most recently.

Definition at line 270 of file dbus-connection.c.

Referenced by \_dbus_connection_queue_received_message_link(), \_dbus_connection_queue_synthesized_message_link(), dbus_connection_borrow_message(), and dbus_connection_steal_borrowed_message().

## ◆ io_path_acquired

|                                              |
|----------------------------------------------|
| dbus_bool_t DBusConnection::io_path_acquired |

Someone has transport io path (can use the transport to read/write messages)

Definition at line 315 of file dbus-connection.c.

## ◆ io_path_cond

|                                            |
|--------------------------------------------|
| DBusCondVar\* DBusConnection::io_path_cond |

Notify when io_path_acquired is available.

Definition at line 267 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport().

## ◆ io_path_mutex

|                                            |
|--------------------------------------------|
| DBusCMutex\* DBusConnection::io_path_mutex |

Protects io_path_acquired.

Definition at line 266 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport().

## ◆ last_dispatch_status

|                                                         |
|---------------------------------------------------------|
| DBusDispatchStatus DBusConnection::last_dispatch_status |

The last dispatch status we reported to the application.

Definition at line 304 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport().

## ◆ message_borrowed

|                                                |
|------------------------------------------------|
| DBusMessage\* DBusConnection::message_borrowed |

Filled in if the first incoming message has been borrowed; dispatch_acquired will be set by the borrower.

Definition at line 273 of file dbus-connection.c.

Referenced by dbus_connection_borrow_message(), dbus_connection_return_message(), and dbus_connection_steal_borrowed_message().

## ◆ mutex

|                                    |
|------------------------------------|
| DBusRMutex\* DBusConnection::mutex |

Lock on the entire DBusConnection.

Definition at line 262 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), and \_dbus_connection_unlock().

## ◆ n_incoming

|                                |
|--------------------------------|
| int DBusConnection::n_incoming |

Length of incoming queue.

Definition at line 278 of file dbus-connection.c.

Referenced by \_dbus_connection_queue_received_message_link(), \_dbus_connection_queue_synthesized_message_link(), and dbus_connection_steal_borrowed_message().

## ◆ n_outgoing

|                                |
|--------------------------------|
| int DBusConnection::n_outgoing |

Length of outgoing queue.

Definition at line 277 of file dbus-connection.c.

Referenced by \_dbus_connection_do_iteration_unlocked(), and \_dbus_connection_message_sent_unlocked().

## ◆ objects

|                                          |
|------------------------------------------|
| DBusObjectTree\* DBusConnection::objects |

Object path handlers registered with this connection.

Definition at line 306 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), dbus_connection_dispatch(), dbus_connection_get_object_path_data(), dbus_connection_list_registered(), and dbus_connection_unregister_object_path().

## ◆ outgoing_counter

|                                                |
|------------------------------------------------|
| DBusCounter\* DBusConnection::outgoing_counter |

Counts size of outgoing messages.

Definition at line 280 of file dbus-connection.c.

Referenced by \_dbus_connection_message_sent_unlocked(), \_dbus_connection_new_for_transport(), dbus_connection_get_outgoing_size(), and dbus_connection_get_outgoing_unix_fds().

## ◆ outgoing_messages

|                                              |
|----------------------------------------------|
| DBusList\* DBusConnection::outgoing_messages |

Queue of messages we need to send, send the end of the list first.

Definition at line 269 of file dbus-connection.c.

Referenced by \_dbus_connection_get_message_to_send(), \_dbus_connection_has_messages_to_send_unlocked(), and \_dbus_connection_message_sent_unlocked().

## ◆ pending_replies

|                                                 |
|-------------------------------------------------|
| DBusHashTable\* DBusConnection::pending_replies |

Hash of message serials to DBusPendingCall.

Definition at line 291 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), \_dbus_connection_queue_received_message_link(), and dbus_connection_dispatch().

## ◆ refcount

|                                     |
|-------------------------------------|
| DBusAtomic DBusConnection::refcount |

Reference count.

Definition at line 260 of file dbus-connection.c.

Referenced by \_dbus_connection_close_if_only_one_ref(), \_dbus_connection_new_for_transport(), \_dbus_connection_ref_unlocked(), \_dbus_connection_unref_unlocked(), dbus_connection_ref(), and dbus_connection_unref().

## ◆ route_peer_messages

|                                                  |
|--------------------------------------------------|
| unsigned int DBusConnection::route_peer_messages |

If TRUE, if org.freedesktop.DBus.Peer messages have a bus name, don't handle them automatically.

Definition at line 323 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), and dbus_connection_set_route_peer_messages().

## ◆ server_guid

|                                    |
|------------------------------------|
| char\* DBusConnection::server_guid |

GUID of server if we are in shared_connections, NULL if server GUID is unknown or connection is private.

Definition at line 308 of file dbus-connection.c.

## ◆ shareable

|                                        |
|----------------------------------------|
| unsigned int DBusConnection::shareable |

TRUE if libdbus owns a reference to the connection and can return it from dbus_connection_open() more than once

Definition at line 317 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), dbus_connection_close(), and dbus_connection_unref().

## ◆ slot_list

|                                            |
|--------------------------------------------|
| DBusDataSlotList DBusConnection::slot_list |

Data stored by allocated integer ID.

Definition at line 289 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), dbus_connection_get_data(), and dbus_connection_set_data().

## ◆ slot_mutex

|                                         |
|-----------------------------------------|
| DBusRMutex\* DBusConnection::slot_mutex |

Lock on slot_list so overall connection lock need not be taken.

Definition at line 288 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport().

## ◆ timeouts

|                                            |
|--------------------------------------------|
| DBusTimeoutList\* DBusConnection::timeouts |

Stores active timeouts.

Definition at line 284 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), and dbus_connection_set_timeout_functions().

## ◆ transport

|                                           |
|-------------------------------------------|
| DBusTransport\* DBusConnection::transport |

Object that sends/receives messages over network.

Definition at line 282 of file dbus-connection.c.

Referenced by \_dbus_connection_do_iteration_unlocked(), \_dbus_connection_get_pending_fds_count(), \_dbus_connection_handle_watch(), \_dbus_connection_new_for_transport(), \_dbus_connection_queue_received_message_link(), \_dbus_connection_set_pending_fds_function(), dbus_connection_can_send_type(), dbus_connection_get_adt_audit_session_data(), dbus_connection_get_is_anonymous(), dbus_connection_get_is_authenticated(), dbus_connection_get_max_message_size(), dbus_connection_get_max_message_unix_fds(), dbus_connection_get_max_received_size(), dbus_connection_get_max_received_unix_fds(), dbus_connection_get_server_id(), dbus_connection_get_socket(), dbus_connection_get_unix_fd(), dbus_connection_get_unix_process_id(), dbus_connection_get_unix_user(), dbus_connection_get_windows_user(), dbus_connection_send(), dbus_connection_send_preallocated(), dbus_connection_send_with_reply(), dbus_connection_send_with_reply_and_block(), dbus_connection_set_allow_anonymous(), dbus_connection_set_max_message_size(), dbus_connection_set_max_message_unix_fds(), dbus_connection_set_max_received_size(), dbus_connection_set_max_received_unix_fds(), dbus_connection_set_unix_user_function(), dbus_connection_set_windows_user_function(), and dbus_connection_unref().

## ◆ wakeup_main_data

|                                         |
|-----------------------------------------|
| void\* DBusConnection::wakeup_main_data |

Application data for wakeup_main_function.

Definition at line 297 of file dbus-connection.c.

Referenced by dbus_connection_set_wakeup_main_function().

## ◆ wakeup_main_function

|                                                             |
|-------------------------------------------------------------|
| DBusWakeupMainFunction DBusConnection::wakeup_main_function |

Function to wake up the mainloop  

Definition at line 296 of file dbus-connection.c.

Referenced by dbus_connection_set_wakeup_main_function().

## ◆ watches

|                                         |
|-----------------------------------------|
| DBusWatchList\* DBusConnection::watches |

Stores active watches.

Definition at line 283 of file dbus-connection.c.

Referenced by \_dbus_connection_new_for_transport(), and dbus_connection_set_watch_functions().

The documentation for this struct was generated from the following file:

- dbus-connection.c
