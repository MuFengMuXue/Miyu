D-Bus low-level public API

The low-level public API of the D-Bus library. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="modules" class="groupheader"> Modules</h2></td>
</tr>
<tr id="r_group__DBusAddress" class="memitem:group__DBusAddress">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Address parsing</td>
</tr>
<tr class="memdesc:group__DBusAddress">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parsing addresses of D-Bus servers.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusBus" class="memitem:group__DBusBus">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Message bus APIs</td>
</tr>
<tr class="memdesc:group__DBusBus">
<td class="mdescLeft"> </td>
<td class="mdescRight">Functions for communicating with the message bus.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusConnection" class="memitem:group__DBusConnection">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">DBusConnection</td>
</tr>
<tr class="memdesc:group__DBusConnection">
<td class="mdescLeft"> </td>
<td class="mdescRight">Connection to another application.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusErrors" class="memitem:group__DBusErrors">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Error reporting</td>
</tr>
<tr class="memdesc:group__DBusErrors">
<td class="mdescLeft"> </td>
<td class="mdescRight">Error reporting.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusMacros" class="memitem:group__DBusMacros">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Utility macros</td>
</tr>
<tr class="memdesc:group__DBusMacros">
<td class="mdescLeft"> </td>
<td class="mdescRight">TRUE, FALSE, NULL, and so on<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusMemory" class="memitem:group__DBusMemory">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Memory Allocation</td>
</tr>
<tr class="memdesc:group__DBusMemory">
<td class="mdescLeft"> </td>
<td class="mdescRight">dbus_malloc(), dbus_free(), etc.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusMessage" class="memitem:group__DBusMessage">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">DBusMessage</td>
</tr>
<tr class="memdesc:group__DBusMessage">
<td class="mdescLeft"> </td>
<td class="mdescRight">Message to be sent or received over a DBusConnection.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusMisc" class="memitem:group__DBusMisc">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Miscellaneous</td>
</tr>
<tr class="memdesc:group__DBusMisc">
<td class="mdescLeft"> </td>
<td class="mdescRight">Miscellaneous API that doesn't cleanly fit anywhere else.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusPendingCall" class="memitem:group__DBusPendingCall">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">DBusPendingCall</td>
</tr>
<tr class="memdesc:group__DBusPendingCall">
<td class="mdescLeft"> </td>
<td class="mdescRight">Pending reply to a method call message.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusProtocol" class="memitem:group__DBusProtocol">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Protocol constants</td>
</tr>
<tr class="memdesc:group__DBusProtocol">
<td class="mdescLeft"> </td>
<td class="mdescRight">Defines constants which are part of the D-Bus protocol.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusServer" class="memitem:group__DBusServer">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">DBusServer</td>
</tr>
<tr class="memdesc:group__DBusServer">
<td class="mdescLeft"> </td>
<td class="mdescRight">Server that listens for new connections.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusShared" class="memitem:group__DBusShared">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Shared constants</td>
</tr>
<tr class="memdesc:group__DBusShared">
<td class="mdescLeft"> </td>
<td class="mdescRight">Shared header included by both libdbus and C/C++ bindings such as the GLib bindings.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusSignature" class="memitem:group__DBusSignature">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Type signature parsing</td>
</tr>
<tr class="memdesc:group__DBusSignature">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parsing D-Bus type signatures.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusSyntax" class="memitem:group__DBusSyntax">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Utility functions for strings with special syntax</td>
</tr>
<tr class="memdesc:group__DBusSyntax">
<td class="mdescLeft"> </td>
<td class="mdescRight">Parsing D-Bus type signatures.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusThreads" class="memitem:group__DBusThreads">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Thread functions</td>
</tr>
<tr class="memdesc:group__DBusThreads">
<td class="mdescLeft"> </td>
<td class="mdescRight">dbus_threads_init() and dbus_threads_init_default()<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusTimeout" class="memitem:group__DBusTimeout">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">DBusTimeout</td>
</tr>
<tr class="memdesc:group__DBusTimeout">
<td class="mdescLeft"> </td>
<td class="mdescRight">Object representing a timeout.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusTypes" class="memitem:group__DBusTypes">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">Basic types</td>
</tr>
<tr class="memdesc:group__DBusTypes">
<td class="mdescLeft"> </td>
<td class="mdescRight">dbus_bool_t, dbus_int32_t, etc.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_group__DBusWatch" class="memitem:group__DBusWatch">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> </td>
<td class="memItemRight" data-valign="bottom">DBusWatch</td>
</tr>
<tr class="memdesc:group__DBusWatch">
<td class="mdescLeft"> </td>
<td class="mdescRight">Object representing a file descriptor to be watched.<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

The low-level public API of the D-Bus library.

libdbus provides a low-level C API intended primarily for use by bindings to specific object systems and languages. D-Bus is most convenient when used with the GLib bindings, Python bindings, Qt bindings, Mono bindings, and so forth. This low-level API has a lot of complexity useful only for bindings.
