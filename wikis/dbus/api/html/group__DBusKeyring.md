keyring class

D-Bus secret internal implementation details

DBusKeyring data structure. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga9ef32242338798399ef2eaacea5812a6" class="memitem:ga9ef32242338798399ef2eaacea5812a6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusKeyring * </td>
<td class="memItemRight" data-valign="bottom">_dbus_keyring_ref (DBusKeyring *keyring)</td>
</tr>
<tr class="memdesc:ga9ef32242338798399ef2eaacea5812a6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increments reference count of the keyring.<br />
</td>
</tr>
<tr class="separator:ga9ef32242338798399ef2eaacea5812a6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gadd42b029d08dc477b6847e91bdcb23ca" class="memitem:gadd42b029d08dc477b6847e91bdcb23ca">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_keyring_unref (DBusKeyring *keyring)</td>
</tr>
<tr class="memdesc:gadd42b029d08dc477b6847e91bdcb23ca">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrements refcount and finalizes if it reaches zero.<br />
</td>
</tr>
<tr class="separator:gadd42b029d08dc477b6847e91bdcb23ca">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga69c7557fa1cc01b07ab17942b70531c6" class="memitem:ga69c7557fa1cc01b07ab17942b70531c6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusKeyring * </td>
<td class="memItemRight" data-valign="bottom">_dbus_keyring_new_for_credentials (DBusCredentials *credentials, const DBusString *context, DBusError *error)</td>
</tr>
<tr class="memdesc:ga69c7557fa1cc01b07ab17942b70531c6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new keyring that lives in the ~/.dbus-keyrings directory of the user represented by <code>credentials</code>.<br />
</td>
</tr>
<tr class="separator:ga69c7557fa1cc01b07ab17942b70531c6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5bbeeef1ba831a89d7f0f211e886e7c2" class="memitem:ga5bbeeef1ba831a89d7f0f211e886e7c2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_keyring_validate_context (const DBusString *context)</td>
</tr>
<tr class="memdesc:ga5bbeeef1ba831a89d7f0f211e886e7c2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the context is a valid context.<br />
</td>
</tr>
<tr class="separator:ga5bbeeef1ba831a89d7f0f211e886e7c2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0daf16cfb75ab28d67d5dfa881f457a6" class="memitem:ga0daf16cfb75ab28d67d5dfa881f457a6">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_keyring_get_best_key (DBusKeyring *keyring, DBusError *error)</td>
</tr>
<tr class="memdesc:ga0daf16cfb75ab28d67d5dfa881f457a6">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets a recent key to use for authentication.<br />
</td>
</tr>
<tr class="separator:ga0daf16cfb75ab28d67d5dfa881f457a6">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5ef8c7224182f27ff56b3105c6963cfd" class="memitem:ga5ef8c7224182f27ff56b3105c6963cfd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_keyring_is_for_credentials (DBusKeyring *keyring, DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga5ef8c7224182f27ff56b3105c6963cfd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the keyring is for the same user as the given credentials.<br />
</td>
</tr>
<tr class="separator:ga5ef8c7224182f27ff56b3105c6963cfd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6adfb998247ab4d0c1d5652f59c354e4" class="memitem:ga6adfb998247ab4d0c1d5652f59c354e4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_keyring_get_hex_key (DBusKeyring *keyring, int key_id, DBusString *hex_key)</td>
</tr>
<tr class="memdesc:ga6adfb998247ab4d0c1d5652f59c354e4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the hex-encoded secret key for the given ID.<br />
</td>
</tr>
<tr class="separator:ga6adfb998247ab4d0c1d5652f59c354e4">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusKeyring data structure.

Types and functions related to DBusKeyring. DBusKeyring is intended to manage cookies used to authenticate clients to servers. This is essentially the "verify that client can read the user's homedir" authentication mechanism. Both client and server must have access to the homedir.

The secret keys are not kept in locked memory, and are written to a file in the user's homedir. However they are transient (only used by a single server instance for a fixed period of time, then discarded). Also, the keys are not sent over the wire.

## Function Documentation

## ◆ \_dbus_keyring_get_best_key()

|                                 |     |                 |            |
|---------------------------------|-----|-----------------|------------|
| int \_dbus_keyring_get_best_key | (   | DBusKeyring \*  | *keyring*, |
|                                 |     | DBusError \*    | *error*    |
|                                 | )   |                 |            |

Gets a recent key to use for authentication.

If no recent key exists, creates one. Returns the key ID. If a key can't be written to the keyring file so no recent key can be created, returns -1. All valid keys are \> 0.

Parameters  
|         |                  |
|---------|------------------|
| keyring | the keyring      |
| error   | error on failure |

<!-- -->

Returns  
key ID to use for auth, or -1 on failure

Definition at line 934 of file dbus-keyring.c.

References DBUS_ERROR_FAILED, dbus_set_error_const(), DBusKey::id, and TRUE.

## ◆ \_dbus_keyring_get_hex_key()

|                                        |     |                 |            |
|----------------------------------------|-----|-----------------|------------|
| dbus_bool_t \_dbus_keyring_get_hex_key | (   | DBusKeyring \*  | *keyring*, |
|                                        |     | int             | *key_id*,  |
|                                        |     | DBusString \*   | *hex_key*  |
|                                        | )   |                 |            |

Gets the hex-encoded secret key for the given ID.

Returns FALSE if not enough memory. Returns TRUE but empty key on any other error such as unknown key ID.

Parameters  
|         |                                     |
|---------|-------------------------------------|
| keyring | the keyring                         |
| key_id  | the key ID                          |
| hex_key | string to append hex-encoded key to |

<!-- -->

Returns  
TRUE if we had enough memory

Definition at line 992 of file dbus-keyring.c.

References \_dbus_string_get_length(), \_dbus_string_hex_encode(), keys, n_keys, NULL, DBusKey::secret, and TRUE.

## ◆ \_dbus_keyring_is_for_credentials()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_keyring_is_for_credentials | ( | DBusKeyring \*  | *keyring*, |
|  |  | DBusCredentials \*  | *credentials*  |
|  | ) |  |  |

Checks whether the keyring is for the same user as the given credentials.

Parameters  
|             |                          |
|-------------|--------------------------|
| keyring     | the keyring              |
| credentials | the credentials to check |

<!-- -->

Returns  
TRUE if the keyring belongs to the given user

Definition at line 973 of file dbus-keyring.c.

References \_dbus_credentials_same_user(), and credentials.

## ◆ \_dbus_keyring_new_for_credentials()

|  |  |  |  |
|----|----|----|----|
| DBusKeyring \* \_dbus_keyring_new_for_credentials | ( | DBusCredentials \*  | *credentials*, |
|  |  | const DBusString \*  | *context*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Creates a new keyring that lives in the ~/.dbus-keyrings directory of the user represented by `credentials`.

If the `credentials` are NULL or empty, uses those of the current process.

Parameters  
|             |                                                  |
|-------------|--------------------------------------------------|
| credentials | a set of credentials representing a user or NULL |
| context     | which keyring to get                             |
| error       | return location for errors                       |

<!-- -->

Returns  
the keyring or NULL on error

Definition at line 693 of file dbus-keyring.c.

References \_dbus_append_keyring_directory_for_credentials(), \_dbus_assert, \_dbus_check_setuid(), \_dbus_concat_dir_and_file(), \_dbus_credentials_add_from_current_process(), \_dbus_credentials_are_anonymous(), \_dbus_credentials_copy(), \_dbus_credentials_new_from_current_process(), \_dbus_credentials_unref(), \_dbus_ensure_directory(), \_dbus_keyring_unref(), \_dbus_keyring_validate_context(), \_dbus_string_append(), \_dbus_string_copy(), \_dbus_string_free(), \_dbus_string_init(), credentials, DBUS_ERROR_FAILED, dbus_error_free(), dbus_error_init(), DBUS_ERROR_NO_MEMORY, DBUS_ERROR_NOT_SUPPORTED, dbus_set_error(), dbus_set_error_const(), directory, FALSE, filename, filename_lock, DBusError::message, NULL, and TRUE.

## ◆ \_dbus_keyring_ref()

|                                   |     |                 |           |     |     |
|-----------------------------------|-----|-----------------|-----------|-----|-----|
| DBusKeyring \* \_dbus_keyring_ref | (   | DBusKeyring \*  | *keyring* | )   |     |

Increments reference count of the keyring.

Parameters  
|         |             |
|---------|-------------|
| keyring | the keyring |

<!-- -->

Returns  
the keyring

Definition at line 651 of file dbus-keyring.c.

References refcount.

## ◆ \_dbus_keyring_unref()

|                           |     |                 |           |     |     |
|---------------------------|-----|-----------------|-----------|-----|-----|
| void \_dbus_keyring_unref | (   | DBusKeyring \*  | *keyring* | )   |     |

Decrements refcount and finalizes if it reaches zero.

Parameters  
|         |             |
|---------|-------------|
| keyring | the keyring |

Definition at line 665 of file dbus-keyring.c.

References \_dbus_credentials_unref(), \_dbus_string_free(), credentials, dbus_free(), directory, filename, filename_lock, keys, n_keys, and refcount.

Referenced by \_dbus_auth_unref(), and \_dbus_keyring_new_for_credentials().

## ◆ \_dbus_keyring_validate_context()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_keyring_validate_context | ( | const DBusString \*  | *context* | ) |  |

Checks whether the context is a valid context.

Contexts that might cause confusion when used in filenames are not allowed (contexts can't start with a dot or contain dir separators).

Parameters  
|         |             |
|---------|-------------|
| context | the context |

<!-- -->

Returns  
TRUE if valid

Definition at line 837 of file dbus-keyring.c.

References \_dbus_string_find(), \_dbus_string_find_blank(), \_dbus_string_get_length(), \_dbus_string_validate_ascii(), FALSE, NULL, and TRUE.

Referenced by \_dbus_keyring_new_for_credentials().
