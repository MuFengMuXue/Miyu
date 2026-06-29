Credentials provable through authentication

D-Bus secret internal implementation details

DBusCredentials object. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga5a905d38011acfe359627701166647d7" class="memitem:ga5a905d38011acfe359627701166647d7">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_new (void)</td>
</tr>
<tr class="memdesc:ga5a905d38011acfe359627701166647d7">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new credentials object.<br />
</td>
</tr>
<tr class="separator:ga5a905d38011acfe359627701166647d7">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4b9b8a8fd06fd5bd559981c96a5d30ed" class="memitem:ga4b9b8a8fd06fd5bd559981c96a5d30ed">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_new_from_current_process (void)</td>
</tr>
<tr class="memdesc:ga4b9b8a8fd06fd5bd559981c96a5d30ed">
<td class="mdescLeft"> </td>
<td class="mdescRight">Creates a new object with the most important credentials (user ID and process ID) from the current process.<br />
</td>
</tr>
<tr class="separator:ga4b9b8a8fd06fd5bd559981c96a5d30ed">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga09d375f124bddbbaa1aac62ef49078ac" class="memitem:ga09d375f124bddbbaa1aac62ef49078ac">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_ref (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga09d375f124bddbbaa1aac62ef49078ac">
<td class="mdescLeft"> </td>
<td class="mdescRight">Increment refcount on credentials.<br />
</td>
</tr>
<tr class="separator:ga09d375f124bddbbaa1aac62ef49078ac">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga89913c830c3627cd006a50ca693af580" class="memitem:ga89913c830c3627cd006a50ca693af580">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_unref (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga89913c830c3627cd006a50ca693af580">
<td class="mdescLeft"> </td>
<td class="mdescRight">Decrement refcount on credentials.<br />
</td>
</tr>
<tr class="separator:ga89913c830c3627cd006a50ca693af580">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaad133a8d06af2a447307266a8425a9f8" class="memitem:gaad133a8d06af2a447307266a8425a9f8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_add_pid (DBusCredentials *credentials, dbus_pid_t pid)</td>
</tr>
<tr class="memdesc:gaad133a8d06af2a447307266a8425a9f8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Add a UNIX process ID to the credentials.<br />
</td>
</tr>
<tr class="separator:gaad133a8d06af2a447307266a8425a9f8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5d0862a16a940d223033003f951b45cf" class="memitem:ga5d0862a16a940d223033003f951b45cf">
<td class="memItemLeft" style="text-align: right;" data-valign="top">_DBUS_GNUC_NORETURN void </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_take_pid_fd (DBusCredentials *credentials, int pid_fd)</td>
</tr>
<tr class="memdesc:ga5d0862a16a940d223033003f951b45cf">
<td class="mdescLeft"> </td>
<td class="mdescRight">Add a UNIX process ID FD to the credentials.<br />
</td>
</tr>
<tr class="separator:ga5d0862a16a940d223033003f951b45cf">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9cec6da43e4be233d44f5bd60b071624" class="memitem:ga9cec6da43e4be233d44f5bd60b071624">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_add_unix_uid (DBusCredentials *credentials, dbus_uid_t uid)</td>
</tr>
<tr class="memdesc:ga9cec6da43e4be233d44f5bd60b071624">
<td class="mdescLeft"> </td>
<td class="mdescRight">Add a UNIX user ID to the credentials.<br />
</td>
</tr>
<tr class="separator:ga9cec6da43e4be233d44f5bd60b071624">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7fbd21a2ab041256ee17a5a8222403ee" class="memitem:ga7fbd21a2ab041256ee17a5a8222403ee">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_take_unix_gids (DBusCredentials *credentials, dbus_gid_t *gids, size_t n_gids)</td>
</tr>
<tr class="memdesc:ga7fbd21a2ab041256ee17a5a8222403ee">
<td class="mdescLeft"> </td>
<td class="mdescRight">Add UNIX group IDs to the credentials, replacing any group IDs that might already have been present.<br />
</td>
</tr>
<tr class="separator:ga7fbd21a2ab041256ee17a5a8222403ee">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9242c7d06b19a0e374164172e6ab35d5" class="memitem:ga9242c7d06b19a0e374164172e6ab35d5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_get_unix_gids (DBusCredentials *credentials, const dbus_gid_t **gids, size_t *n_gids)</td>
</tr>
<tr class="memdesc:ga9242c7d06b19a0e374164172e6ab35d5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Get the Unix group IDs.<br />
</td>
</tr>
<tr class="separator:ga9242c7d06b19a0e374164172e6ab35d5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9d2186a4cfa8a421c552ae4592b400f5" class="memitem:ga9d2186a4cfa8a421c552ae4592b400f5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_add_windows_sid (DBusCredentials *credentials, const char *windows_sid)</td>
</tr>
<tr class="memdesc:ga9d2186a4cfa8a421c552ae4592b400f5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Add a Windows user SID to the credentials.<br />
</td>
</tr>
<tr class="separator:ga9d2186a4cfa8a421c552ae4592b400f5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga644603125ecf8627444ba29f02653473" class="memitem:ga644603125ecf8627444ba29f02653473">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_add_linux_security_label (DBusCredentials *credentials, const char *label)</td>
</tr>
<tr class="memdesc:ga644603125ecf8627444ba29f02653473">
<td class="mdescLeft"> </td>
<td class="mdescRight">Add a Linux security label, as used by LSMs such as SELinux, Smack and AppArmor, to the credentials.<br />
</td>
</tr>
<tr class="separator:ga644603125ecf8627444ba29f02653473">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab26eb5cb8d05139806cf06e99c4ec5b0" class="memitem:gab26eb5cb8d05139806cf06e99c4ec5b0">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_add_adt_audit_data (DBusCredentials *credentials, void *audit_data, dbus_int32_t size)</td>
</tr>
<tr class="memdesc:gab26eb5cb8d05139806cf06e99c4ec5b0">
<td class="mdescLeft"> </td>
<td class="mdescRight">Add ADT audit data to the credentials.<br />
</td>
</tr>
<tr class="separator:gab26eb5cb8d05139806cf06e99c4ec5b0">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0fb8d13878e126ccc243c4a30fd8598c" class="memitem:ga0fb8d13878e126ccc243c4a30fd8598c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_include (DBusCredentials *credentials, DBusCredentialType type)</td>
</tr>
<tr class="memdesc:ga0fb8d13878e126ccc243c4a30fd8598c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the given credential is present.<br />
</td>
</tr>
<tr class="separator:ga0fb8d13878e126ccc243c4a30fd8598c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaafde142353288854a8a3969949d2e548" class="memitem:gaafde142353288854a8a3969949d2e548">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_pid_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_get_pid (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:gaafde142353288854a8a3969949d2e548">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the UNIX process ID in the credentials, or DBUS_PID_UNSET if the credentials object doesn't contain a process ID.<br />
</td>
</tr>
<tr class="separator:gaafde142353288854a8a3969949d2e548">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf2c2c5f042bba008152eb8b475534df2" class="memitem:gaf2c2c5f042bba008152eb8b475534df2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_get_pid_fd (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:gaf2c2c5f042bba008152eb8b475534df2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the UNIX process ID FD in the credentials as obtained by 'safe' means (e.g.: Linux's SO_PEERPIDFD), or -1 if the credentials object doesn't contain a process ID FD.<br />
</td>
</tr>
<tr class="separator:gaf2c2c5f042bba008152eb8b475534df2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga462892f995f2932bf0eb3b843407e6d5" class="memitem:ga462892f995f2932bf0eb3b843407e6d5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_uid_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_get_unix_uid (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga462892f995f2932bf0eb3b843407e6d5">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the UNIX user ID in the credentials, or DBUS_UID_UNSET if the credentials object doesn't contain a user ID.<br />
</td>
</tr>
<tr class="separator:ga462892f995f2932bf0eb3b843407e6d5">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab8b640d36ad65d3b845412770cbce8fb" class="memitem:gab8b640d36ad65d3b845412770cbce8fb">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_get_windows_sid (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:gab8b640d36ad65d3b845412770cbce8fb">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the Windows user SID in the credentials, or NULL if the credentials object doesn't contain a Windows user SID.<br />
</td>
</tr>
<tr class="separator:gab8b640d36ad65d3b845412770cbce8fb">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7abdd90eb93a8f059071d8068d256056" class="memitem:ga7abdd90eb93a8f059071d8068d256056">
<td class="memItemLeft" style="text-align: right;" data-valign="top">const char * </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_get_linux_security_label (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga7abdd90eb93a8f059071d8068d256056">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the Linux security label (as used by LSMs) from the credentials, or NULL if the credentials object doesn't contain a security label.<br />
</td>
</tr>
<tr class="separator:ga7abdd90eb93a8f059071d8068d256056">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga5aa78a9fbb107650b6be283018e3768d" class="memitem:ga5aa78a9fbb107650b6be283018e3768d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void * </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_get_adt_audit_data (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga5aa78a9fbb107650b6be283018e3768d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the ADT audit data in the credentials, or NULL if the credentials object doesn't contain ADT audit data.<br />
</td>
</tr>
<tr class="separator:ga5aa78a9fbb107650b6be283018e3768d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gab3f338ba37ed9bfa1531e00b3a8a10ce" class="memitem:gab3f338ba37ed9bfa1531e00b3a8a10ce">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_int32_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_get_adt_audit_data_size (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:gab3f338ba37ed9bfa1531e00b3a8a10ce">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the ADT audit data size in the credentials, or 0 if the credentials object doesn't contain ADT audit data.<br />
</td>
</tr>
<tr class="separator:gab3f338ba37ed9bfa1531e00b3a8a10ce">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga1c6090c76e5151ae8a1efe9e84382934" class="memitem:ga1c6090c76e5151ae8a1efe9e84382934">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_are_superset (DBusCredentials *credentials, DBusCredentials *possible_subset)</td>
</tr>
<tr class="memdesc:ga1c6090c76e5151ae8a1efe9e84382934">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether the first credentials object contains all the credentials found in the second credentials object.<br />
</td>
</tr>
<tr class="separator:ga1c6090c76e5151ae8a1efe9e84382934">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga9aea1a288097b0820d1cd05c2448501d" class="memitem:ga9aea1a288097b0820d1cd05c2448501d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_are_empty (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga9aea1a288097b0820d1cd05c2448501d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether a credentials object contains anything.<br />
</td>
</tr>
<tr class="separator:ga9aea1a288097b0820d1cd05c2448501d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabfd7a1f681a91b45ba2f4e7461131827" class="memitem:gabfd7a1f681a91b45ba2f4e7461131827">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_are_anonymous (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:gabfd7a1f681a91b45ba2f4e7461131827">
<td class="mdescLeft"> </td>
<td class="mdescRight">Checks whether a credentials object contains a user identity.<br />
</td>
</tr>
<tr class="separator:gabfd7a1f681a91b45ba2f4e7461131827">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6b6cab83ecaa05e765967c188f62dd05" class="memitem:ga6b6cab83ecaa05e765967c188f62dd05">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_add_credentials (DBusCredentials *credentials, DBusCredentials *other_credentials)</td>
</tr>
<tr class="memdesc:ga6b6cab83ecaa05e765967c188f62dd05">
<td class="mdescLeft"> </td>
<td class="mdescRight">Merge all credentials found in the second object into the first object, overwriting the first object if there are any overlaps.<br />
</td>
</tr>
<tr class="separator:ga6b6cab83ecaa05e765967c188f62dd05">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gabd5a6d038f1d35fd23af8b2e73bb7ef8" class="memitem:gabd5a6d038f1d35fd23af8b2e73bb7ef8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_add_credential (DBusCredentials *credentials, DBusCredentialType which, DBusCredentials *other_credentials)</td>
</tr>
<tr class="memdesc:gabd5a6d038f1d35fd23af8b2e73bb7ef8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Merge the given credential found in the second object into the first object, overwriting the first object's value for that credential.<br />
</td>
</tr>
<tr class="separator:gabd5a6d038f1d35fd23af8b2e73bb7ef8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga40a5c7e37b10419e233a473dc7173f3c" class="memitem:ga40a5c7e37b10419e233a473dc7173f3c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_clear (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga40a5c7e37b10419e233a473dc7173f3c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Clear all credentials in the object.<br />
</td>
</tr>
<tr class="separator:ga40a5c7e37b10419e233a473dc7173f3c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga490ac596c7c9cbaef5be8ba064f55f16" class="memitem:ga490ac596c7c9cbaef5be8ba064f55f16">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBusCredentials * </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_copy (DBusCredentials *credentials)</td>
</tr>
<tr class="memdesc:ga490ac596c7c9cbaef5be8ba064f55f16">
<td class="mdescLeft"> </td>
<td class="mdescRight">Copy a credentials object.<br />
</td>
</tr>
<tr class="separator:ga490ac596c7c9cbaef5be8ba064f55f16">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2f10263b80ff6611c15a78e8f6823dfa" class="memitem:ga2f10263b80ff6611c15a78e8f6823dfa">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_same_user (DBusCredentials *credentials, DBusCredentials *other_credentials)</td>
</tr>
<tr class="memdesc:ga2f10263b80ff6611c15a78e8f6823dfa">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check whether the user-identifying credentials in two credentials objects are identical.<br />
</td>
</tr>
<tr class="separator:ga2f10263b80ff6611c15a78e8f6823dfa">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga50047ecf44c85ecb0878a370592c1576" class="memitem:ga50047ecf44c85ecb0878a370592c1576">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_credentials_to_string_append (DBusCredentials *credentials, DBusString *string)</td>
</tr>
<tr class="memdesc:ga50047ecf44c85ecb0878a370592c1576">
<td class="mdescLeft"> </td>
<td class="mdescRight">Convert the credentials in this object to a human-readable string format, and append to the given string.<br />
</td>
</tr>
<tr class="separator:ga50047ecf44c85ecb0878a370592c1576">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

DBusCredentials object.

Credentials are what you have to prove you have in order to authenticate. The main credentials right now are a unix user account, a Windows user account, or a UNIX process ID.

## Function Documentation

## ◆ \_dbus_credentials_add_adt_audit_data()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_add_adt_audit_data | ( | DBusCredentials \*  | *credentials*, |
|  |  | void \*  | *audit_data*, |
|  |  | dbus_int32_t  | *size*  |
|  | ) |  |  |

Add ADT audit data to the credentials.

Parameters  
|             |                          |
|-------------|--------------------------|
| credentials | the object               |
| audit_data  | the audit data           |
| size        | the length of audit data |

<!-- -->

Returns  
FALSE if no memory

Definition at line 341 of file dbus-credentials.c.

References \_dbus_memdup(), dbus_free(), FALSE, NULL, and TRUE.

Referenced by \_dbus_credentials_add_credential(), and \_dbus_read_credentials_socket().

## ◆ \_dbus_credentials_add_credential()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_add_credential | ( | DBusCredentials \*  | *credentials*, |
|  |  | DBusCredentialType  | *which*, |
|  |  | DBusCredentials \*  | *other_credentials*  |
|  | ) |  |  |

Merge the given credential found in the second object into the first object, overwriting the first object's value for that credential.

Does nothing if the second object does not contain the specified credential. i.e., will never delete a credential from the first object.

Parameters  
|                   |                             |
|-------------------|-----------------------------|
| credentials       | the object                  |
| which             | the credential to overwrite |
| other_credentials | credentials to merge        |

<!-- -->

Returns  
FALSE if no memory

Definition at line 614 of file dbus-credentials.c.

References \_dbus_credentials_add_adt_audit_data(), \_dbus_credentials_add_linux_security_label(), \_dbus_credentials_add_pid(), \_dbus_credentials_add_unix_uid(), \_dbus_credentials_add_windows_sid(), \_dbus_credentials_take_pid_fd(), \_dbus_credentials_take_unix_gids(), \_dbus_dup(), dbus_new, DBUS_PID_UNSET, DBUS_UID_UNSET, FALSE, NULL, and TRUE.

Referenced by \_dbus_credentials_add_credentials().

## ◆ \_dbus_credentials_add_credentials()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_add_credentials | ( | DBusCredentials \*  | *credentials*, |
|  |  | DBusCredentials \*  | *other_credentials*  |
|  | ) |  |  |

Merge all credentials found in the second object into the first object, overwriting the first object if there are any overlaps.

Parameters  
|                   |                      |
|-------------------|----------------------|
| credentials       | the object           |
| other_credentials | credentials to merge |

<!-- -->

Returns  
FALSE if no memory

Definition at line 574 of file dbus-credentials.c.

References \_dbus_credentials_add_credential().

Referenced by \_dbus_auth_set_credentials(), and \_dbus_credentials_copy().

## ◆ \_dbus_credentials_add_linux_security_label()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_add_linux_security_label | ( | DBusCredentials \*  | *credentials*, |
|  |  | const char \*  | *label*  |
|  | ) |  |  |

Add a Linux security label, as used by LSMs such as SELinux, Smack and AppArmor, to the credentials.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |
| label       | the label  |

<!-- -->

Returns  
FALSE if no memory

Definition at line 317 of file dbus-credentials.c.

References \_dbus_strdup(), dbus_free(), FALSE, NULL, and TRUE.

Referenced by \_dbus_credentials_add_credential().

## ◆ \_dbus_credentials_add_pid()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_add_pid | ( | DBusCredentials \*  | *credentials*, |
|  |  | dbus_pid_t  | *pid*  |
|  | ) |  |  |

Add a UNIX process ID to the credentials.

If the process ID FD is set, it will always take precendence when querying the PID of this credential.

Parameters  
|             |                |
|-------------|----------------|
| credentials | the object     |
| pid         | the process ID |

<!-- -->

Returns  
FALSE if no memory

Definition at line 181 of file dbus-credentials.c.

References TRUE.

Referenced by \_dbus_credentials_add_credential(), \_dbus_credentials_add_from_current_process(), \_dbus_read_credentials_socket(), and \_dbus_read_credentials_socket().

## ◆ \_dbus_credentials_add_unix_uid()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_add_unix_uid | ( | DBusCredentials \*  | *credentials*, |
|  |  | dbus_uid_t  | *uid*  |
|  | ) |  |  |

Add a UNIX user ID to the credentials.

Parameters  
|             |             |
|-------------|-------------|
| credentials | the object  |
| uid         | the user ID |

<!-- -->

Returns  
FALSE if no memory

Definition at line 220 of file dbus-credentials.c.

References TRUE.

Referenced by \_dbus_credentials_add_credential(), \_dbus_credentials_add_from_current_process(), \_dbus_credentials_add_from_user(), and \_dbus_read_credentials_socket().

## ◆ \_dbus_credentials_add_windows_sid()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_add_windows_sid | ( | DBusCredentials \*  | *credentials*, |
|  |  | const char \*  | *windows_sid*  |
|  | ) |  |  |

Add a Windows user SID to the credentials.

Parameters  
|             |              |
|-------------|--------------|
| credentials | the object   |
| windows_sid | the user SID |

<!-- -->

Returns  
FALSE if no memory

Definition at line 293 of file dbus-credentials.c.

References \_dbus_strdup(), dbus_free(), FALSE, NULL, and TRUE.

Referenced by \_dbus_credentials_add_credential(), \_dbus_credentials_add_from_current_process(), \_dbus_credentials_add_from_user(), and \_dbus_read_credentials_socket().

## ◆ \_dbus_credentials_are_anonymous()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_credentials_are_anonymous | ( | DBusCredentials \*  | *credentials* | ) |  |

Checks whether a credentials object contains a user identity.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

<!-- -->

Returns  
TRUE if there are no user identities in the object

Definition at line 558 of file dbus-credentials.c.

References DBUS_UID_UNSET, and NULL.

Referenced by \_dbus_append_keyring_directory_for_credentials(), \_dbus_keyring_new_for_credentials(), and \_dbus_transport_get_is_anonymous().

## ◆ \_dbus_credentials_are_empty()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_credentials_are_empty | ( | DBusCredentials \*  | *credentials* | ) |  |

Checks whether a credentials object contains anything.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

<!-- -->

Returns  
TRUE if there are no credentials in the object

Definition at line 538 of file dbus-credentials.c.

References DBUS_PID_UNSET, DBUS_UID_UNSET, and NULL.

Referenced by \_dbus_auth_get_identity().

## ◆ \_dbus_credentials_are_superset()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_are_superset | ( | DBusCredentials \*  | *credentials*, |
|  |  | DBusCredentials \*  | *possible_subset*  |
|  | ) |  |  |

Checks whether the first credentials object contains all the credentials found in the second credentials object.

Parameters  
|                 |                                                      |
|-----------------|------------------------------------------------------|
| credentials     | the object                                           |
| possible_subset | see if credentials in here are also in the first arg |

<!-- -->

Returns  
TRUE if second arg is contained in first

Definition at line 506 of file dbus-credentials.c.

References DBUS_PID_UNSET, DBUS_UID_UNSET, and NULL.

## ◆ \_dbus_credentials_clear()

|                               |     |                     |               |     |     |
|-------------------------------|-----|---------------------|---------------|-----|-----|
| void \_dbus_credentials_clear | (   | DBusCredentials \*  | *credentials* | )   |     |

Clear all credentials in the object.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

Definition at line 688 of file dbus-credentials.c.

References dbus_free(), DBUS_PID_UNSET, DBUS_UID_UNSET, and NULL.

Referenced by \_dbus_auth_set_credentials(), and \_dbus_read_credentials_socket().

## ◆ \_dbus_credentials_copy()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusCredentials \* \_dbus_credentials_copy | ( | DBusCredentials \*  | *credentials* | ) |  |

Copy a credentials object.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

<!-- -->

Returns  
the copy or NULL

Definition at line 718 of file dbus-credentials.c.

References \_dbus_credentials_add_credentials(), \_dbus_credentials_new(), \_dbus_credentials_unref(), and NULL.

Referenced by \_dbus_keyring_new_for_credentials().

## ◆ \_dbus_credentials_get_adt_audit_data()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| void \* \_dbus_credentials_get_adt_audit_data | ( | DBusCredentials \*  | *credentials* | ) |  |

Gets the ADT audit data in the credentials, or NULL if the credentials object doesn't contain ADT audit data.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

<!-- -->

Returns  
Solaris ADT audit data

Definition at line 479 of file dbus-credentials.c.

Referenced by \_dbus_transport_get_adt_audit_session_data().

## ◆ \_dbus_credentials_get_adt_audit_data_size()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_int32_t \_dbus_credentials_get_adt_audit_data_size | ( | DBusCredentials \*  | *credentials* | ) |  |

Gets the ADT audit data size in the credentials, or 0 if the credentials object doesn't contain ADT audit data.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

<!-- -->

Returns  
Solaris ADT audit data size

Definition at line 492 of file dbus-credentials.c.

Referenced by \_dbus_transport_get_adt_audit_session_data().

## ◆ \_dbus_credentials_get_linux_security_label()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| const char \* \_dbus_credentials_get_linux_security_label | ( | DBusCredentials \*  | *credentials* | ) |  |

Gets the Linux security label (as used by LSMs) from the credentials, or NULL if the credentials object doesn't contain a security label.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

<!-- -->

Returns  
the security label

Definition at line 466 of file dbus-credentials.c.

## ◆ \_dbus_credentials_get_pid()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_pid_t \_dbus_credentials_get_pid | ( | DBusCredentials \*  | *credentials* | ) |  |

Gets the UNIX process ID in the credentials, or DBUS_PID_UNSET if the credentials object doesn't contain a process ID.

If the PID FD is set, it will first try to resolve from it, and only return the stored PID if that fails.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

<!-- -->

Returns  
UNIX process ID

Definition at line 401 of file dbus-credentials.c.

References \_dbus_resolve_pid_fd().

Referenced by \_dbus_credentials_to_string_append(), and \_dbus_transport_get_unix_process_id().

## ◆ \_dbus_credentials_get_pid_fd()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| int \_dbus_credentials_get_pid_fd | ( | DBusCredentials \*  | *credentials* | ) |  |

Gets the UNIX process ID FD in the credentials as obtained by 'safe' means (e.g.: Linux's SO_PEERPIDFD), or -1 if the credentials object doesn't contain a process ID FD.

The file FD is owned by the credentials object and must not be closed by the caller.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

<!-- -->

Returns  
UNIX process ID FD

Definition at line 427 of file dbus-credentials.c.

## ◆ \_dbus_credentials_get_unix_gids()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_get_unix_gids | ( | DBusCredentials \*  | *credentials*, |
|  |  | const dbus_gid_t \*\*  | *gids*, |
|  |  | size_t \*  | *n_gids*  |
|  | ) |  |  |

Get the Unix group IDs.

Parameters  
|  |  |
|----|----|
| credentials | the object |
| gids | the group IDs, which will be freed by the DBusCredentials object |
| n_gids | the number of group IDs |

Definition at line 272 of file dbus-credentials.c.

References NULL.

## ◆ \_dbus_credentials_get_unix_uid()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_uid_t \_dbus_credentials_get_unix_uid | ( | DBusCredentials \*  | *credentials* | ) |  |

Gets the UNIX user ID in the credentials, or DBUS_UID_UNSET if the credentials object doesn't contain a user ID.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

<!-- -->

Returns  
UNIX user ID

Definition at line 440 of file dbus-credentials.c.

Referenced by \_dbus_append_keyring_directory_for_credentials(), and \_dbus_transport_get_unix_user().

## ◆ \_dbus_credentials_get_windows_sid()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| const char \* \_dbus_credentials_get_windows_sid | ( | DBusCredentials \*  | *credentials* | ) |  |

Gets the Windows user SID in the credentials, or NULL if the credentials object doesn't contain a Windows user SID.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

<!-- -->

Returns  
Windows user SID

Definition at line 453 of file dbus-credentials.c.

Referenced by \_dbus_transport_get_windows_user().

## ◆ \_dbus_credentials_include()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_include | ( | DBusCredentials \*  | *credentials*, |
|  |  | DBusCredentialType  | *type*  |
|  | ) |  |  |

Checks whether the given credential is present.

Parameters  
|             |                             |
|-------------|-----------------------------|
| credentials | the object                  |
| type        | the credential to check for |

<!-- -->

Returns  
TRUE if the credential is present

Definition at line 365 of file dbus-credentials.c.

References \_dbus_assert_not_reached, DBUS_PID_UNSET, DBUS_UID_UNSET, FALSE, and NULL.

Referenced by \_dbus_transport_get_adt_audit_session_data(), \_dbus_transport_get_unix_process_id(), \_dbus_transport_get_unix_user(), \_dbus_transport_get_windows_user(), and \_dbus_transport_try_to_authenticate().

## ◆ \_dbus_credentials_new()

|                                           |     |       |     |     |     |
|-------------------------------------------|-----|-------|-----|-----|-----|
| DBusCredentials \* \_dbus_credentials_new | (   | void  |     | )   |     |

Creates a new credentials object.

Returns  
the new object or NULL if no memory

Definition at line 86 of file dbus-credentials.c.

References dbus_new, DBUS_PID_UNSET, DBUS_UID_UNSET, and NULL.

Referenced by \_dbus_credentials_copy(), \_dbus_credentials_new_from_current_process(), and \_dbus_transport_init_base().

## ◆ \_dbus_credentials_new_from_current_process()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBusCredentials \* \_dbus_credentials_new_from_current_process | ( | void  |  | ) |  |

Creates a new object with the most important credentials (user ID and process ID) from the current process.

Returns  
the new object or NULL if no memory

Definition at line 113 of file dbus-credentials.c.

References \_dbus_credentials_add_from_current_process(), \_dbus_credentials_new(), \_dbus_credentials_unref(), and NULL.

Referenced by \_dbus_keyring_new_for_credentials().

## ◆ \_dbus_credentials_ref()

|                             |     |                     |               |     |     |
|-----------------------------|-----|---------------------|---------------|-----|-----|
| void \_dbus_credentials_ref | (   | DBusCredentials \*  | *credentials* | )   |     |

Increment refcount on credentials.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

Definition at line 136 of file dbus-credentials.c.

References \_dbus_assert.

## ◆ \_dbus_credentials_same_user()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_same_user | ( | DBusCredentials \*  | *credentials*, |
|  |  | DBusCredentials \*  | *other_credentials*  |
|  | ) |  |  |

Check whether the user-identifying credentials in two credentials objects are identical.

Credentials that are not related to the user are ignored, but any kind of user ID credentials must be the same (UNIX user ID, Windows user SID, etc.) and present in both objects for the function to return TRUE.

Parameters  
|                   |                        |
|-------------------|------------------------|
| credentials       | the object             |
| other_credentials | credentials to compare |

<!-- -->

Returns  
TRUE if the two credentials refer to the same user

Definition at line 747 of file dbus-credentials.c.

Referenced by \_dbus_keyring_is_for_credentials().

## ◆ \_dbus_credentials_take_pid_fd()

|  |  |  |  |
|----|----|----|----|
| \_DBUS_GNUC_NORETURN void \_dbus_credentials_take_pid_fd | ( | DBusCredentials \*  | *credentials*, |
|  |  | int  | *pid_fd*  |
|  | ) |  |  |

Add a UNIX process ID FD to the credentials.

The FD is now owned by the credentials object.

Parameters  
|             |                   |
|-------------|-------------------|
| credentials | the object        |
| pid_fd      | the process ID FD |

<!-- -->

Returns  
FALSE if no memory

Definition at line 200 of file dbus-credentials.c.

References \_dbus_assert_not_reached.

Referenced by \_dbus_credentials_add_credential(), \_dbus_credentials_add_from_current_process(), and \_dbus_read_credentials_socket().

## ◆ \_dbus_credentials_take_unix_gids()

|  |  |  |  |
|----|----|----|----|
| void \_dbus_credentials_take_unix_gids | ( | DBusCredentials \*  | *credentials*, |
|  |  | dbus_gid_t \*  | *gids*, |
|  |  | size_t  | *n_gids*  |
|  | ) |  |  |

Add UNIX group IDs to the credentials, replacing any group IDs that might already have been present.

Parameters  
|  |  |
|----|----|
| credentials | the object |
| gids | the group IDs, which will be freed by the DBusCredentials object |
| n_gids | the number of group IDs |

Definition at line 252 of file dbus-credentials.c.

References dbus_free().

Referenced by \_dbus_credentials_add_credential().

## ◆ \_dbus_credentials_to_string_append()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_credentials_to_string_append | ( | DBusCredentials \*  | *credentials*, |
|  |  | DBusString \*  | *string*  |
|  | ) |  |  |

Convert the credentials in this object to a human-readable string format, and append to the given string.

Parameters  
|             |                       |
|-------------|-----------------------|
| credentials | the object            |
| string      | append to this string |

<!-- -->

Returns  
FALSE if no memory

Definition at line 768 of file dbus-credentials.c.

References \_dbus_credentials_get_pid(), \_dbus_string_append_printf(), DBUS_GID_FORMAT, DBUS_PID_FORMAT, DBUS_PID_UNSET, DBUS_UID_FORMAT, DBUS_UID_UNSET, FALSE, NULL, and TRUE.

## ◆ \_dbus_credentials_unref()

|                               |     |                     |               |     |     |
|-------------------------------|-----|---------------------|---------------|-----|-----|
| void \_dbus_credentials_unref | (   | DBusCredentials \*  | *credentials* | )   |     |

Decrement refcount on credentials.

Parameters  
|             |            |
|-------------|------------|
| credentials | the object |

Definition at line 148 of file dbus-credentials.c.

References \_dbus_assert, and dbus_free().

Referenced by \_dbus_auth_unref(), \_dbus_credentials_copy(), \_dbus_credentials_new_from_current_process(), \_dbus_keyring_new_for_credentials(), \_dbus_keyring_unref(), \_dbus_transport_finalize_base(), and \_dbus_transport_init_base().
