Message bus APIs

D-Bus low-level public API

Functions for communicating with the message bus. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga77ba5250adb84620f16007e1b023cf26" class="memitem:ga77ba5250adb84620f16007e1b023cf26">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_get (DBusBusType type, DBusError *error)</td>
</tr>
<tr class="memdesc:ga77ba5250adb84620f16007e1b023cf26">
<td class="mdescLeft"> </td>
<td class="mdescRight">Connects to a bus daemon and registers the client with it.<br />
</td>
</tr>
<tr class="separator:ga77ba5250adb84620f16007e1b023cf26">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9c62186f19cf3bd3c7c604bdcefb4e09" class="memitem:ga9c62186f19cf3bd3c7c604bdcefb4e09">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusConnection * </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_get_private (DBusBusType type, DBusError *error)</td>
</tr>
<tr class="memdesc:ga9c62186f19cf3bd3c7c604bdcefb4e09">
<td class="mdescLeft"> </td>
<td class="mdescRight">Connects to a bus daemon and registers the client with it as with dbus_bus_register().<br />
</td>
</tr>
<tr class="separator:ga9c62186f19cf3bd3c7c604bdcefb4e09">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0c21cf74d05c0bd8003846b56a588a4b" class="memitem:ga0c21cf74d05c0bd8003846b56a588a4b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_register (DBusConnection *connection, DBusError *error)</td>
</tr>
<tr class="memdesc:ga0c21cf74d05c0bd8003846b56a588a4b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Registers a connection with the bus.<br />
</td>
</tr>
<tr class="separator:ga0c21cf74d05c0bd8003846b56a588a4b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0366177076e88bf37771341f32b0551c" class="memitem:ga0366177076e88bf37771341f32b0551c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_set_unique_name (DBusConnection *connection, const char *unique_name)</td>
</tr>
<tr class="memdesc:ga0366177076e88bf37771341f32b0551c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the unique name of the connection, as assigned by the message bus.<br />
</td>
</tr>
<tr class="separator:ga0366177076e88bf37771341f32b0551c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8c10339a1e62f6a2e5752d9c2270d37b" class="memitem:ga8c10339a1e62f6a2e5752d9c2270d37b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_get_unique_name (DBusConnection *connection)</td>
</tr>
<tr class="memdesc:ga8c10339a1e62f6a2e5752d9c2270d37b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the unique name of the connection as assigned by the message bus.<br />
</td>
</tr>
<tr class="separator:ga8c10339a1e62f6a2e5752d9c2270d37b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga24d782c710f3d82caf1b1ed582dcf474" class="memitem:ga24d782c710f3d82caf1b1ed582dcf474">
<td class="memItemLeft" style="text-align: right;" data-valign="top">unsigned long </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_get_unix_user (DBusConnection *connection, const char *name, DBusError *error)</td>
</tr>
<tr class="memdesc:ga24d782c710f3d82caf1b1ed582dcf474">
<td class="mdescLeft"> </td>
<td class="mdescRight">Asks the bus to return the UID the named connection authenticated as, if any.<br />
</td>
</tr>
<tr class="separator:ga24d782c710f3d82caf1b1ed582dcf474">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga18314500e7f6890a79bddbeace5df5f9" class="memitem:ga18314500e7f6890a79bddbeace5df5f9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_get_id (DBusConnection *connection, DBusError *error)</td>
</tr>
<tr class="memdesc:ga18314500e7f6890a79bddbeace5df5f9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Asks the bus to return its globally unique ID, as described in the D-Bus specification.<br />
</td>
</tr>
<tr class="separator:ga18314500e7f6890a79bddbeace5df5f9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8a9024c78c4ea89b6271f19dbc7861b2" class="memitem:ga8a9024c78c4ea89b6271f19dbc7861b2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_request_name (DBusConnection *connection, const char *name, unsigned int flags, DBusError *error)</td>
</tr>
<tr class="memdesc:ga8a9024c78c4ea89b6271f19dbc7861b2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Asks the bus to assign the given name to this connection by invoking the RequestName method on the bus.<br />
</td>
</tr>
<tr class="separator:ga8a9024c78c4ea89b6271f19dbc7861b2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa4aa5ebe51cdbe8c0651609fc72e841a" class="memitem:gaa4aa5ebe51cdbe8c0651609fc72e841a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_release_name (DBusConnection *connection, const char *name, DBusError *error)</td>
</tr>
<tr class="memdesc:gaa4aa5ebe51cdbe8c0651609fc72e841a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Asks the bus to unassign the given name from this connection by invoking the ReleaseName method on the bus.<br />
</td>
</tr>
<tr class="separator:gaa4aa5ebe51cdbe8c0651609fc72e841a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5331b172dd8ed00eec130e894c5c2a0b" class="memitem:ga5331b172dd8ed00eec130e894c5c2a0b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_name_has_owner (DBusConnection *connection, const char *name, DBusError *error)</td>
</tr>
<tr class="memdesc:ga5331b172dd8ed00eec130e894c5c2a0b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Asks the bus whether a certain name has an owner.<br />
</td>
</tr>
<tr class="separator:ga5331b172dd8ed00eec130e894c5c2a0b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga81d303bf29d7c97ad4690ce35071b090" class="memitem:ga81d303bf29d7c97ad4690ce35071b090">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_start_service_by_name (DBusConnection *connection, const char *name, dbus_uint32_t flags, dbus_uint32_t *result, DBusError *error)</td>
</tr>
<tr class="memdesc:ga81d303bf29d7c97ad4690ce35071b090">
<td class="mdescLeft"> </td>
<td class="mdescRight">Starts a service that will request ownership of the given name.<br />
</td>
</tr>
<tr class="separator:ga81d303bf29d7c97ad4690ce35071b090">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4eb6401ba014da3dbe3dc4e2a8e5b3ef" class="memitem:ga4eb6401ba014da3dbe3dc4e2a8e5b3ef">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_add_match (DBusConnection *connection, const char *rule, DBusError *error)</td>
</tr>
<tr class="memdesc:ga4eb6401ba014da3dbe3dc4e2a8e5b3ef">
<td class="mdescLeft"> </td>
<td class="mdescRight">Adds a match rule to match messages going through the message bus.<br />
</td>
</tr>
<tr class="separator:ga4eb6401ba014da3dbe3dc4e2a8e5b3ef">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6e6b98e19fa4400de7ef99c27b866b99" class="memitem:ga6e6b98e19fa4400de7ef99c27b866b99">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_bus_remove_match (DBusConnection *connection, const char *rule, DBusError *error)</td>
</tr>
<tr class="memdesc:ga6e6b98e19fa4400de7ef99c27b866b99">
<td class="mdescLeft"> </td>
<td class="mdescRight">Removes a previously-added match rule "by value" (the most recently-added identical rule gets removed).<br />
</td>
</tr>
<tr class="separator:ga6e6b98e19fa4400de7ef99c27b866b99">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Functions for communicating with the message bus.

dbus_bus_get() allows all modules and libraries in a given process to share the same connection to the bus daemon by storing the connection globally.

All other functions in this module are just convenience functions; most of them invoke methods on the bus daemon, by sending method call messages to DBUS_SERVICE_DBUS. These convenience functions often make blocking method calls. If you don't want to block, you can send the method call messages manually in the same way you would any other method call message.

This module is the only one in libdbus that's specific to communicating with the message bus daemon. The rest of the API can also be used for connecting to another application directly.

## Function Documentation

## ◆ dbus_bus_add_match()

|                                     |     |                    |               |
|-------------------------------------|-----|--------------------|---------------|
| DBUS_EXPORT void dbus_bus_add_match | (   | DBusConnection \*  | *connection*, |
|                                     |     | const char \*      | *rule*,       |
|                                     |     | DBusError \*       | *error*       |
|                                     | )   |                    |               |

Adds a match rule to match messages going through the message bus.

The "rule" argument is the string form of a match rule.

If you pass NULL for the error, this function will not block; the match thus won't be added until you flush the connection, and if there's an error adding the match you won't find out about it. This is generally acceptable, since the possible errors (including a lack of resources in the bus, the connection having exceeded its quota of active match rules, or the match rule being unparseable) are generally unrecoverable.

If you pass non-NULL for the error this function will block until it gets a reply. This may be useful when using match rule keys introduced in recent versions of D-Bus, like 'arg0namespace', to allow the application to fall back to less efficient match rules supported by older versions of the daemon if the running version is not new enough; or when using user-supplied rules rather than rules hard-coded at compile time.

Normal API conventions would have the function return a boolean value indicating whether the error was set, but that would require blocking always to determine the return value.

The AddMatch method is fully documented in the D-Bus specification. For quick reference, the format of the match rules is discussed here, but the specification is the canonical version of this information.

Rules are specified as a string of comma separated key/value pairs. An example is "type='signal',sender='org.freedesktop.DBus', interface='org.freedesktop.DBus',member='Foo', path='/bar/foo',destination=':452345.34'"

Possible keys you can match on are type, sender, interface, member, path, destination and numbered keys to match message args (keys are 'arg0', 'arg1', etc.). Omitting a key from the rule indicates a wildcard match. For instance omitting the member from a match rule but adding a sender would let all messages from that sender through regardless of the member.

Matches are inclusive not exclusive so as long as one rule matches the message will get through. It is important to note this because every time a message is received the application will be paged into memory to process it. This can cause performance problems such as draining batteries on embedded platforms.

If you match message args ('arg0', 'arg1', and so forth) only string arguments will match. That is, arg0='5' means match the string "5" not the integer 5.

Currently there is no way to match against non-string arguments.

A specialised form of wildcard matching on arguments is supported for path-like namespaces. If your argument match has a 'path' suffix (eg: "arg0path='/some/path/'") then it is considered a match if the argument exactly matches the given string or if one of them ends in a '/' and is a prefix of the other.

Matching on interface is tricky because method call messages only optionally specify the interface. If a message omits the interface, then it will NOT match if the rule specifies an interface name. This means match rules on method calls should not usually give an interface.

However, signal messages are required to include the interface so when matching signals usually you should specify the interface in the match rule.

For security reasons, you can match arguments only up to DBUS_MAXIMUM_MATCH_RULE_ARG_NUMBER.

Match rules have a maximum length of DBUS_MAXIMUM_MATCH_RULE_LENGTH bytes.

Both of these maximums are much higher than you're likely to need, they only exist because the D-Bus bus daemon has fixed limits on all resource usage.

Parameters  
|            |                               |
|------------|-------------------------------|
| connection | connection to the message bus |
| rule       | textual form of match rule    |
| error      | location to store any errors  |

Definition at line 1529 of file dbus-bus.c.

References DBUS_INTERFACE_DBUS, dbus_message_append_args(), dbus_message_new_method_call(), dbus_message_unref(), DBUS_PATH_DBUS, DBUS_SERVICE_DBUS, DBUS_TYPE_INVALID, DBUS_TYPE_STRING, and NULL.

## ◆ dbus_bus_get()

|                                            |     |               |          |
|--------------------------------------------|-----|---------------|----------|
| DBUS_EXPORT DBusConnection \* dbus_bus_get | (   | DBusBusType   | *type*,  |
|                                            |     | DBusError \*  | *error*  |
|                                            | )   |               |          |

Connects to a bus daemon and registers the client with it.

If a connection to the bus already exists, then that connection is returned. The caller of this function owns a reference to the bus.

The caller may NOT call dbus_connection_close() on this connection; see dbus_connection_open() and dbus_connection_close() for details on that.

If this function obtains a new connection object never before returned from dbus_bus_get(), it will call dbus_connection_set_exit_on_disconnect(), so the application will exit if the connection closes. You can undo this by calling dbus_connection_set_exit_on_disconnect() yourself after you get the connection.

dbus_bus_get() calls dbus_bus_register() for you.

If returning a newly-created connection, this function will block until authentication and bus registration are complete.

Parameters  
|       |                                         |
|-------|-----------------------------------------|
| type  | bus type                                |
| error | address where an error can be returned. |

<!-- -->

Returns  
a DBusConnection with new ref or NULL on error

Definition at line 561 of file dbus-bus.c.

References FALSE.

## ◆ dbus_bus_get_id()

|                                     |     |                    |               |
|-------------------------------------|-----|--------------------|---------------|
| DBUS_EXPORT char \* dbus_bus_get_id | (   | DBusConnection \*  | *connection*, |
|                                     |     | DBusError \*       | *error*       |
|                                     | )   |                    |               |

Asks the bus to return its globally unique ID, as described in the D-Bus specification.

For the session bus, this is useful as a way to uniquely identify each user session. For the system bus, probably the bus ID is not useful; instead, use the machine ID since it's accessible without necessarily connecting to the bus and may be persistent beyond a single bus instance (across reboots for example). See dbus_try_get_local_machine_id().

In addition to an ID for each bus and an ID for each machine, there is an ID for each address that the bus is listening on; that can be retrieved with dbus_connection_get_server_id(), though it is probably not very useful.

Parameters  
|            |                             |
|------------|-----------------------------|
| connection | the connection              |
| error      | location to store the error |

<!-- -->

Returns  
the bus ID or NULL if error is set

Definition at line 951 of file dbus-bus.c.

References \_dbus_strdup(), dbus_connection_send_with_reply_and_block(), DBUS_INTERFACE_DBUS, dbus_message_get_args(), dbus_message_new_method_call(), dbus_message_unref(), DBUS_PATH_DBUS, DBUS_SERVICE_DBUS, dbus_set_error_from_message(), DBUS_TYPE_INVALID, DBUS_TYPE_STRING, and NULL.

## ◆ dbus_bus_get_private()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT DBusConnection \* dbus_bus_get_private | ( | DBusBusType  | *type*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Connects to a bus daemon and registers the client with it as with dbus_bus_register().

Unlike dbus_bus_get(), always creates a new connection. This connection will not be saved or recycled by libdbus. Caller owns a reference to the bus and must either close it or know it to be closed prior to releasing this reference.

See dbus_connection_open_private() for more details on when to close and unref this connection.

This function calls dbus_connection_set_exit_on_disconnect() on the new connection, so the application will exit if the connection closes. You can undo this by calling dbus_connection_set_exit_on_disconnect() yourself after you get the connection.

dbus_bus_get_private() calls dbus_bus_register() for you.

This function will block until authentication and bus registration are complete.

Parameters  
|       |                                         |
|-------|-----------------------------------------|
| type  | bus type                                |
| error | address where an error can be returned. |

<!-- -->

Returns  
a DBusConnection with new ref

Definition at line 593 of file dbus-bus.c.

References TRUE.

## ◆ dbus_bus_get_unique_name()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT const char \* dbus_bus_get_unique_name | ( | DBusConnection \*  | *connection* | ) |  |

Gets the unique name of the connection as assigned by the message bus.

Only possible after the connection has been registered with the message bus. All connections returned by dbus_bus_get() or dbus_bus_get_private() have been successfully registered.

The name remains valid until the connection is freed, and should not be freed by the caller.

Other than dbus_bus_get(), there are two ways to set the unique name; one is dbus_bus_register(), the other is dbus_bus_set_unique_name(). You are responsible for calling dbus_bus_set_unique_name() if you register by hand instead of using dbus_bus_register().

Parameters  
|            |                |
|------------|----------------|
| connection | the connection |

<!-- -->

Returns  
the unique name or NULL on error

Definition at line 818 of file dbus-bus.c.

References \_DBUS_LOCK, \_DBUS_UNLOCK, NULL, and BusData::unique_name.

## ◆ dbus_bus_get_unix_user()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT unsigned long dbus_bus_get_unix_user | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *name*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Asks the bus to return the UID the named connection authenticated as, if any.

Only works on UNIX; only works for connections on the same machine as the bus. If you are not on the same machine as the bus, then calling this is probably a bad idea, since the UID will mean little to your application.

For the system message bus you're guaranteed to be on the same machine since it only listens on a UNIX domain socket (at least, as shipped by default).

This function only works for connections that authenticated as a UNIX user, right now that includes all bus connections, but it's very possible to have connections with no associated UID. So check for errors and do something sensible if they happen.

This function will always return an error on Windows.

Parameters  
|            |                                |
|------------|--------------------------------|
| connection | the connection                 |
| name       | a name owned by the connection |
| error      | location to store the error    |

<!-- -->

Returns  
the unix user id, or ((unsigned)-1) if error is set

Definition at line 868 of file dbus-bus.c.

References dbus_connection_send_with_reply_and_block(), DBUS_INTERFACE_DBUS, dbus_message_append_args(), dbus_message_get_args(), dbus_message_new_method_call(), dbus_message_unref(), DBUS_PATH_DBUS, DBUS_SERVICE_DBUS, dbus_set_error_from_message(), DBUS_TYPE_INVALID, DBUS_TYPE_STRING, DBUS_TYPE_UINT32, DBUS_UID_UNSET, and NULL.

## ◆ dbus_bus_name_has_owner()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_bus_name_has_owner | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *name*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Asks the bus whether a certain name has an owner.

Using this can easily result in a race condition, since an owner can appear or disappear after you call this.

If you want to request a name, just request it; if you want to avoid replacing a current owner, don't specify DBUS_NAME_FLAG_REPLACE_EXISTING and you will get an error if there's already an owner.

Parameters  
|            |                              |
|------------|------------------------------|
| connection | the connection               |
| name       | the name                     |
| error      | location to store any errors |

<!-- -->

Returns  
TRUE if the name exists, FALSE if not or on error

Definition at line 1283 of file dbus-bus.c.

References dbus_connection_send_with_reply_and_block(), DBUS_INTERFACE_DBUS, dbus_message_append_args(), dbus_message_get_args(), dbus_message_new_method_call(), dbus_message_unref(), DBUS_PATH_DBUS, DBUS_SERVICE_DBUS, DBUS_TYPE_BOOLEAN, DBUS_TYPE_INVALID, DBUS_TYPE_STRING, FALSE, and NULL.

## ◆ dbus_bus_register()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_bus_register | ( | DBusConnection \*  | *connection*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Registers a connection with the bus.

This must be the first thing an application does when connecting to the message bus. If registration succeeds, the unique name will be set, and can be obtained using dbus_bus_get_unique_name().

This function will block until registration is complete.

If the connection has already registered with the bus (determined by checking whether dbus_bus_get_unique_name() returns a non-NULL value), then this function does nothing.

If you use dbus_bus_get() or dbus_bus_get_private() this function will be called for you.

Note  
Just use dbus_bus_get() or dbus_bus_get_private() instead of dbus_bus_register() and save yourself some pain. Using dbus_bus_register() manually is only useful if you have your own custom message bus not found in DBusBusType.

If you open a bus connection with dbus_connection_open() or dbus_connection_open_private() you will have to dbus_bus_register() yourself, or make the appropriate registration method calls yourself. If you send the method calls yourself, call dbus_bus_set_unique_name() with the unique bus name you get from the bus.

For shared connections (created with dbus_connection_open()) in a multithreaded application, you can't really make the registration calls yourself, because you don't know whether some other thread is also registering, and the bus will kick you off if you send two registration messages.

If you use dbus_bus_register() however, there is a lock that keeps both apps from registering at the same time.

The rule in a multithreaded app, then, is that dbus_bus_register() must be used to register, or you need to have your own locks that all threads in the app will respect.

In a single-threaded application you can register by hand instead of using dbus_bus_register(), as long as you check dbus_bus_get_unique_name() to see if a unique name has already been stored by another thread before you send the registration messages.

Parameters  
|            |                       |
|------------|-----------------------|
| connection | the connection        |
| error      | place to store errors |

<!-- -->

Returns  
TRUE on success

Definition at line 649 of file dbus-bus.c.

References \_DBUS_LOCK, \_dbus_strdup(), \_DBUS_UNLOCK, dbus_connection_send_with_reply_and_block(), DBUS_INTERFACE_DBUS, dbus_message_get_args(), dbus_message_new_method_call(), dbus_message_unref(), DBUS_PATH_DBUS, DBUS_SERVICE_DBUS, dbus_set_error_from_message(), DBUS_TYPE_INVALID, DBUS_TYPE_STRING, FALSE, NULL, TRUE, and BusData::unique_name.

## ◆ dbus_bus_release_name()

|                                       |     |                    |               |
|---------------------------------------|-----|--------------------|---------------|
| DBUS_EXPORT int dbus_bus_release_name | (   | DBusConnection \*  | *connection*, |
|                                       |     | const char \*      | *name*,       |
|                                       |     | DBusError \*       | *error*       |
|                                       | )   |                    |               |

Asks the bus to unassign the given name from this connection by invoking the ReleaseName method on the bus.

The "ReleaseName" method is canonically documented in the D-Bus specification.

Possible results are: DBUS_RELEASE_NAME_REPLY_RELEASED which means you owned the name or were in the queue to own it, and and now you don't own it and aren't in the queue. DBUS_RELEASE_NAME_REPLY_NOT_OWNER which means someone else owns the name so you can't release it. DBUS_RELEASE_NAME_REPLY_NON_EXISTENT which means nobody owned the name.

Parameters  
|            |                             |
|------------|-----------------------------|
| connection | the connection              |
| name       | the name to remove          |
| error      | location to store the error |

<!-- -->

Returns  
a result code, -1 if error is set

Definition at line 1201 of file dbus-bus.c.

References dbus_connection_send_with_reply_and_block(), DBUS_INTERFACE_DBUS, dbus_message_append_args(), dbus_message_get_args(), dbus_message_new_method_call(), dbus_message_unref(), DBUS_PATH_DBUS, DBUS_SERVICE_DBUS, dbus_set_error_from_message(), DBUS_TYPE_INVALID, DBUS_TYPE_STRING, DBUS_TYPE_UINT32, and NULL.

## ◆ dbus_bus_remove_match()

|                                        |     |                    |               |
|----------------------------------------|-----|--------------------|---------------|
| DBUS_EXPORT void dbus_bus_remove_match | (   | DBusConnection \*  | *connection*, |
|                                        |     | const char \*      | *rule*,       |
|                                        |     | DBusError \*       | *error*       |
|                                        | )   |                    |               |

Removes a previously-added match rule "by value" (the most recently-added identical rule gets removed).

The "rule" argument is the string form of a match rule.

The bus compares match rules semantically, not textually, so whitespace and ordering don't have to be identical to the rule you passed to dbus_bus_add_match().

If you pass NULL for the error, this function will not block; otherwise it will. See detailed explanation in docs for dbus_bus_add_match().

Parameters  
|            |                               |
|------------|-------------------------------|
| connection | connection to the message bus |
| rule       | textual form of match rule    |
| error      | location to store any errors  |

Definition at line 1579 of file dbus-bus.c.

References DBUS_INTERFACE_DBUS, dbus_message_append_args(), dbus_message_new_method_call(), dbus_message_unref(), DBUS_PATH_DBUS, DBUS_SERVICE_DBUS, DBUS_TYPE_INVALID, DBUS_TYPE_STRING, and NULL.

## ◆ dbus_bus_request_name()

|                                       |     |                    |               |
|---------------------------------------|-----|--------------------|---------------|
| DBUS_EXPORT int dbus_bus_request_name | (   | DBusConnection \*  | *connection*, |
|                                       |     | const char \*      | *name*,       |
|                                       |     | unsigned int       | *flags*,      |
|                                       |     | DBusError \*       | *error*       |
|                                       | )   |                    |               |

Asks the bus to assign the given name to this connection by invoking the RequestName method on the bus.

This method is fully documented in the D-Bus specification. For quick reference, the flags and result codes are discussed here, but the specification is the canonical version of this information.

First you should know that for each bus name, the bus stores a queue of connections that would like to own it. Only one owns it at a time - called the primary owner. If the primary owner releases the name or disconnects, then the next owner in the queue atomically takes over.

So for example if you have an application org.freedesktop.TextEditor and multiple instances of it can be run, you can have all of them sitting in the queue. The first one to start up will receive messages sent to org.freedesktop.TextEditor, but if that one exits another will become the primary owner and receive messages.

The queue means you don't need to manually watch for the current owner to disappear and then request the name again.

When requesting a name, you can specify several flags.

DBUS_NAME_FLAG_ALLOW_REPLACEMENT and DBUS_NAME_FLAG_DO_NOT_QUEUE are properties stored by the bus for this connection with respect to each requested bus name. These properties are stored even if the connection is queued and does not become the primary owner. You can update these flags by calling RequestName again (even if you already own the name).

DBUS_NAME_FLAG_ALLOW_REPLACEMENT means that another requestor of the name can take it away from you by specifying DBUS_NAME_FLAG_REPLACE_EXISTING.

DBUS_NAME_FLAG_DO_NOT_QUEUE means that if you aren't the primary owner, you don't want to be queued up - you only care about being the primary owner.

Unlike the other two flags, DBUS_NAME_FLAG_REPLACE_EXISTING is a property of the individual RequestName call, i.e. the bus does not persistently associate it with the connection-name pair. If a RequestName call includes the DBUS_NAME_FLAG_REPLACE_EXISTING flag, and the current primary owner has DBUS_NAME_FLAG_ALLOW_REPLACEMENT set, then the current primary owner will be kicked off.

If no flags are given, an application will receive the requested name only if the name is currently unowned; and it will NOT give up the name if another application asks to take it over using DBUS_NAME_FLAG_REPLACE_EXISTING.

This function returns a result code. The possible result codes are as follows.

DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER means that the name had no existing owner, and the caller is now the primary owner; or that the name had an owner, and the caller specified DBUS_NAME_FLAG_REPLACE_EXISTING, and the current owner specified DBUS_NAME_FLAG_ALLOW_REPLACEMENT.

DBUS_REQUEST_NAME_REPLY_IN_QUEUE happens only if the caller does NOT specify DBUS_NAME_FLAG_DO_NOT_QUEUE and either the current owner did NOT specify DBUS_NAME_FLAG_ALLOW_REPLACEMENT or the caller did NOT specify DBUS_NAME_FLAG_REPLACE_EXISTING. In this case the caller ends up in a queue to own the name after the current owner gives it up.

DBUS_REQUEST_NAME_REPLY_EXISTS happens if the name has an owner already and the caller specifies DBUS_NAME_FLAG_DO_NOT_QUEUE and either the current owner has NOT specified DBUS_NAME_FLAG_ALLOW_REPLACEMENT or the caller did NOT specify DBUS_NAME_FLAG_REPLACE_EXISTING.

DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER happens if an application requests a name it already owns. (Re-requesting a name is useful if you want to change the DBUS_NAME_FLAG_ALLOW_REPLACEMENT or DBUS_NAME_FLAG_DO_NOT_QUEUE settings.)

When a service represents an application, say "text editor," then it should specify DBUS_NAME_FLAG_ALLOW_REPLACEMENT if it wants the last editor started to be the user's editor vs. the first one started. Then any editor that can be the user's editor should specify DBUS_NAME_FLAG_REPLACE_EXISTING to either take over (last-started-wins) or be queued up (first-started-wins) according to whether DBUS_NAME_FLAG_ALLOW_REPLACEMENT was given.

Conventionally, single-instance applications often offer a command line option called –replace which means to replace the current instance. To implement this, always set DBUS_NAME_FLAG_ALLOW_REPLACEMENT when you request your application's bus name. When you lose ownership of your bus name, you need to exit. Look for the signal "NameLost" from DBUS_SERVICE_DBUS and DBUS_INTERFACE_DBUS (the signal's first argument is the bus name that was lost). If starting up without –replace, do not specify DBUS_NAME_FLAG_REPLACE_EXISTING, and exit if you fail to become the bus name owner. If –replace is given, ask to replace the old owner.

Parameters  
|            |                             |
|------------|-----------------------------|
| connection | the connection              |
| name       | the name to request         |
| flags      | flags                       |
| error      | location to store the error |

<!-- -->

Returns  
a result code, -1 if error is set

Definition at line 1115 of file dbus-bus.c.

References dbus_connection_send_with_reply_and_block(), DBUS_INTERFACE_DBUS, dbus_message_append_args(), dbus_message_get_args(), dbus_message_new_method_call(), dbus_message_unref(), DBUS_PATH_DBUS, DBUS_SERVICE_DBUS, dbus_set_error_from_message(), DBUS_TYPE_INVALID, DBUS_TYPE_STRING, DBUS_TYPE_UINT32, and NULL.

## ◆ dbus_bus_set_unique_name()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_bus_set_unique_name | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *unique_name*  |
|  | ) |  |  |

Sets the unique name of the connection, as assigned by the message bus.

Can only be used if you registered with the bus manually (i.e. if you did not call dbus_bus_register()). Can only be called once per connection. After the unique name is set, you can get it with dbus_bus_get_unique_name().

The only reason to use this function is to re-implement the equivalent of dbus_bus_register() yourself. One (probably unusual) reason to do that might be to do the bus registration call asynchronously instead of synchronously.

Note  
Just use dbus_bus_get() or dbus_bus_get_private(), or worst case dbus_bus_register(), instead of messing with this function. There's really no point creating pain for yourself by doing things manually.

It's hard to use this function safely on shared connections (created by dbus_connection_open()) in a multithreaded application, because only one registration attempt can be sent to the bus. If two threads are both sending the registration message, there is no mechanism in libdbus itself to avoid sending it twice.

Thus, you need a way to coordinate which thread sends the registration attempt; which also means you know which thread will call dbus_bus_set_unique_name(). If you don't know about all threads in the app (for example, if some libraries you're using might start libdbus-using threads), then you need to avoid using this function on shared connections.

Parameters  
|             |                 |
|-------------|-----------------|
| connection  | the connection  |
| unique_name | the unique name |

<!-- -->

Returns  
FALSE if not enough memory

Definition at line 769 of file dbus-bus.c.

References \_dbus_assert, \_DBUS_LOCK, \_dbus_strdup(), \_DBUS_UNLOCK, FALSE, NULL, and BusData::unique_name.

## ◆ dbus_bus_start_service_by_name()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_bus_start_service_by_name | ( | DBusConnection \*  | *connection*, |
|  |  | const char \*  | *name*, |
|  |  | dbus_uint32_t  | *flags*, |
|  |  | dbus_uint32_t \*  | *result*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Starts a service that will request ownership of the given name.

The returned result will be one of be one of DBUS_START_REPLY_SUCCESS or DBUS_START_REPLY_ALREADY_RUNNING if successful. Pass NULL if you don't care about the result.

The flags parameter is for future expansion, currently you should specify 0.

It's often easier to avoid explicitly starting services, and just send a method call to the service's bus name instead. Method calls start a service to handle them by default unless you call dbus_message_set_auto_start() to disable this behavior.

Parameters  
|            |                                             |
|------------|---------------------------------------------|
| connection | the connection                              |
| name       | the name we want the new service to request |
| flags      | the flags (should always be 0 for now)      |
| result     | a place to store the result or NULL         |
| error      | location to store any errors                |

<!-- -->

Returns  
TRUE if the activation succeeded, FALSE if not

Definition at line 1359 of file dbus-bus.c.

References dbus_connection_send_with_reply_and_block(), DBUS_INTERFACE_DBUS, dbus_message_append_args(), dbus_message_get_args(), dbus_message_new_method_call(), dbus_message_unref(), DBUS_PATH_DBUS, DBUS_SERVICE_DBUS, dbus_set_error_from_message(), DBUS_TYPE_INVALID, DBUS_TYPE_STRING, DBUS_TYPE_UINT32, FALSE, NULL, and TRUE.
