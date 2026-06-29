UNIX-specific internal API

D-Bus secret internal implementation details

Internal system-dependent API available on UNIX only. More...

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
<td class="memItemRight" data-valign="bottom">DBusUserInfo</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Information about a UNIX user. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusGroupInfo</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">Information about a UNIX group. More...<br />
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
<tr id="r_gad5b51b2ac2fa9bd8b35442cc242c6605" class="memitem:gad5b51b2ac2fa9bd8b35442cc242c6605">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusUserInfo </td>
<td class="memItemRight" data-valign="bottom">DBusUserInfo</td>
</tr>
<tr class="memdesc:gad5b51b2ac2fa9bd8b35442cc242c6605">
<td class="mdescLeft"> </td>
<td class="mdescRight">Information about a UNIX user.<br />
</td>
</tr>
<tr class="separator:gad5b51b2ac2fa9bd8b35442cc242c6605">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4530e3a5663c77a98ccc208a1fe0ad14" class="memitem:ga4530e3a5663c77a98ccc208a1fe0ad14">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef struct DBusGroupInfo </td>
<td class="memItemRight" data-valign="bottom">DBusGroupInfo</td>
</tr>
<tr class="memdesc:ga4530e3a5663c77a98ccc208a1fe0ad14">
<td class="mdescLeft"> </td>
<td class="mdescRight">Information about a UNIX group.<br />
</td>
</tr>
<tr class="separator:ga4530e3a5663c77a98ccc208a1fe0ad14">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga428bad3bda7b9b06bd79af77f414237f" class="memitem:ga428bad3bda7b9b06bd79af77f414237f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">typedef void(* </td>
<td class="memItemRight" data-valign="bottom">DBusSignalHandler) (int sig)</td>
</tr>
<tr class="memdesc:ga428bad3bda7b9b06bd79af77f414237f">
<td class="mdescLeft"> </td>
<td class="mdescRight">A UNIX signal handler.<br />
</td>
</tr>
<tr class="separator:ga428bad3bda7b9b06bd79af77f414237f">
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
<tr id="r_ga6466776f55547011f184d16641eaa6b5" class="memitem:ga6466776f55547011f184d16641eaa6b5">
<td class="memItemLeft" style="text-align: right;" data-valign="top">enum  </td>
<td class="memItemRight" data-valign="bottom"><strong>DBusEnsureStandardFdsFlags</strong> { <strong>DBUS_FORCE_STDIN_NULL</strong> = (1 &lt;&lt; 0) , <strong>DBUS_FORCE_STDOUT_NULL</strong> = (1 &lt;&lt; 1) , <strong>DBUS_FORCE_STDERR_NULL</strong> = (1 &lt;&lt; 2) }</td>
</tr>
<tr class="separator:ga6466776f55547011f184d16641eaa6b5">
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
<tr id="r_ga36f73ff161a380eb642aa24bba8a8212" class="memitem:ga36f73ff161a380eb642aa24bba8a8212">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_close (int fd, DBusError *error)</td>
</tr>
<tr class="memdesc:ga36f73ff161a380eb642aa24bba8a8212">
<td class="mdescLeft"> </td>
<td class="mdescRight">Closes a file descriptor.<br />
</td>
</tr>
<tr class="separator:ga36f73ff161a380eb642aa24bba8a8212">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad65903da32e790f04249e6b2e6adc04a" class="memitem:gad65903da32e790f04249e6b2e6adc04a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">_dbus_dup (int fd, DBusError *error)</td>
</tr>
<tr class="memdesc:gad65903da32e790f04249e6b2e6adc04a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Duplicates a file descriptor.<br />
</td>
</tr>
<tr class="separator:gad65903da32e790f04249e6b2e6adc04a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gae38f6edfec06c1e8818a588ef86245b2" class="memitem:gae38f6edfec06c1e8818a588ef86245b2">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT int </td>
<td class="memItemRight" data-valign="bottom">_dbus_read (int fd, DBusString *buffer, int count)</td>
</tr>
<tr class="memdesc:gae38f6edfec06c1e8818a588ef86245b2">
<td class="mdescLeft"> </td>
<td class="mdescRight">Thin wrapper around the read() system call that appends the data it reads to the DBusString buffer.<br />
</td>
</tr>
<tr class="separator:gae38f6edfec06c1e8818a588ef86245b2">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga3a789bcdfd3d468c2bf917fa5081b27f" class="memitem:ga3a789bcdfd3d468c2bf917fa5081b27f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_write (int fd, const DBusString *buffer, int start, int len)</td>
</tr>
<tr class="memdesc:ga3a789bcdfd3d468c2bf917fa5081b27f">
<td class="mdescLeft"> </td>
<td class="mdescRight">Thin wrapper around the write() system call that writes a part of a DBusString and handles EINTR for you.<br />
</td>
</tr>
<tr class="separator:ga3a789bcdfd3d468c2bf917fa5081b27f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga506a183b1f6970d1bfca165ab3de4736" class="memitem:ga506a183b1f6970d1bfca165ab3de4736">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_write_two (int fd, const DBusString *buffer1, int start1, int len1, const DBusString *buffer2, int start2, int len2)</td>
</tr>
<tr class="memdesc:ga506a183b1f6970d1bfca165ab3de4736">
<td class="mdescLeft"> </td>
<td class="mdescRight">Like _dbus_write() but will use writev() if possible to write both buffers in sequence.<br />
</td>
</tr>
<tr class="separator:ga506a183b1f6970d1bfca165ab3de4736">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga72b51ab910e7e9a16195a59ff42bb969" class="memitem:ga72b51ab910e7e9a16195a59ff42bb969">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">_dbus_listen_systemd_sockets (DBusSocket **fd, DBusError *error)</td>
</tr>
<tr class="memdesc:ga72b51ab910e7e9a16195a59ff42bb969">
<td class="mdescLeft"> </td>
<td class="mdescRight">Acquires one or more sockets passed in from systemd.<br />
</td>
</tr>
<tr class="separator:ga72b51ab910e7e9a16195a59ff42bb969">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8ce0c309cd13c15fe215b7b72cbc3f48" class="memitem:ga8ce0c309cd13c15fe215b7b72cbc3f48">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom"><strong>_dbus_read_credentials</strong> (int client_fd, DBusCredentials *credentials, DBusError *error)</td>
</tr>
<tr class="separator:ga8ce0c309cd13c15fe215b7b72cbc3f48">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaed5d695b1c0b1f265ef3448c7de1b33a" class="memitem:gaed5d695b1c0b1f265ef3448c7de1b33a">
<td class="memItemLeft" style="text-align: right;" data-valign="top"> dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom"><strong>_dbus_send_credentials</strong> (int server_fd, DBusError *error)</td>
</tr>
<tr class="separator:gaed5d695b1c0b1f265ef3448c7de1b33a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6425e8cf4a38c71a48309b436322d4db" class="memitem:ga6425e8cf4a38c71a48309b436322d4db">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_lookup_launchd_socket (DBusString *socket_path, const char *launchd_env_var, DBusError *error)</td>
</tr>
<tr class="memdesc:ga6425e8cf4a38c71a48309b436322d4db">
<td class="mdescLeft"> </td>
<td class="mdescRight">quries launchd for a specific env var which holds the socket path.<br />
</td>
</tr>
<tr class="separator:ga6425e8cf4a38c71a48309b436322d4db">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga95e9deb9dd2d76aa3a64fdac555d956d" class="memitem:ga95e9deb9dd2d76aa3a64fdac555d956d">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_info_fill (DBusUserInfo *info, const DBusString *username, DBusError *error)</td>
</tr>
<tr class="memdesc:ga95e9deb9dd2d76aa3a64fdac555d956d">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets user info for the given username.<br />
</td>
</tr>
<tr class="separator:ga95e9deb9dd2d76aa3a64fdac555d956d">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gafcc2fbcde2c72f499f04fa43d97dfcec" class="memitem:gafcc2fbcde2c72f499f04fa43d97dfcec">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_info_fill_uid (DBusUserInfo *info, dbus_uid_t uid, DBusError *error)</td>
</tr>
<tr class="memdesc:gafcc2fbcde2c72f499f04fa43d97dfcec">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets user info for the given user ID.<br />
</td>
</tr>
<tr class="separator:gafcc2fbcde2c72f499f04fa43d97dfcec">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa40334f7b4f185a437a8bc6d6e0994a1" class="memitem:gaa40334f7b4f185a437a8bc6d6e0994a1">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_user_info_free (DBusUserInfo *info)</td>
</tr>
<tr class="memdesc:gaa40334f7b4f185a437a8bc6d6e0994a1">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees the members of info (but not info itself)<br />
</td>
</tr>
<tr class="separator:gaa40334f7b4f185a437a8bc6d6e0994a1">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga23814bdf1859c6aa52da1feab8f1aed4" class="memitem:ga23814bdf1859c6aa52da1feab8f1aed4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_group_info_fill (DBusGroupInfo *info, const DBusString *groupname, DBusError *error)</td>
</tr>
<tr class="memdesc:ga23814bdf1859c6aa52da1feab8f1aed4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes the given DBusGroupInfo struct with information about the given group name.<br />
</td>
</tr>
<tr class="separator:ga23814bdf1859c6aa52da1feab8f1aed4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad235e373b223982b7d3aba8a2b602b58" class="memitem:gad235e373b223982b7d3aba8a2b602b58">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_group_info_fill_gid (DBusGroupInfo *info, dbus_gid_t gid, DBusError *error)</td>
</tr>
<tr class="memdesc:gad235e373b223982b7d3aba8a2b602b58">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes the given DBusGroupInfo struct with information about the given group ID.<br />
</td>
</tr>
<tr class="separator:gad235e373b223982b7d3aba8a2b602b58">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac2d226476e6fff50bdfaace18b897fe9" class="memitem:gac2d226476e6fff50bdfaace18b897fe9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_group_info_free (DBusGroupInfo *info)</td>
</tr>
<tr class="memdesc:gac2d226476e6fff50bdfaace18b897fe9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Frees the members of info (but not info itself).<br />
</td>
</tr>
<tr class="separator:gac2d226476e6fff50bdfaace18b897fe9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaf8cb256dce00d24650ff70d6ec05454e" class="memitem:gaf8cb256dce00d24650ff70d6ec05454e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_uid_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_geteuid (void)</td>
</tr>
<tr class="memdesc:gaf8cb256dce00d24650ff70d6ec05454e">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets our effective UID.<br />
</td>
</tr>
<tr class="separator:gaf8cb256dce00d24650ff70d6ec05454e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac6c1781cd5cced0a53286098cf96d5e4" class="memitem:gac6c1781cd5cced0a53286098cf96d5e4">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_close_all (void)</td>
</tr>
<tr class="memdesc:gac6c1781cd5cced0a53286098cf96d5e4">
<td class="mdescLeft"> </td>
<td class="mdescRight">Closes all file descriptors except the first three (i.e.<br />
</td>
</tr>
<tr class="separator:gac6c1781cd5cced0a53286098cf96d5e4">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2d3eb9daa3776388d5e55a52d7bc4215" class="memitem:ga2d3eb9daa3776388d5e55a52d7bc4215">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_fd_set_all_close_on_exec (void)</td>
</tr>
<tr class="memdesc:ga2d3eb9daa3776388d5e55a52d7bc4215">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets all file descriptors except the first three (i.e.<br />
</td>
</tr>
<tr class="separator:ga2d3eb9daa3776388d5e55a52d7bc4215">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga14d3101a00eb7d9f88ed8601fd14ca91" class="memitem:ga14d3101a00eb7d9f88ed8601fd14ca91">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_fd_clear_close_on_exec (int fd)</td>
</tr>
<tr class="memdesc:ga14d3101a00eb7d9f88ed8601fd14ca91">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the file descriptor to <em>not</em> be close-on-exec.<br />
</td>
</tr>
<tr class="separator:ga14d3101a00eb7d9f88ed8601fd14ca91">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga8f8a19df87ef61019da3a36ca2f49226" class="memitem:ga8f8a19df87ef61019da3a36ca2f49226">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_append_address_from_socket (DBusSocket fd, DBusString *address, DBusError *error)</td>
</tr>
<tr class="memdesc:ga8f8a19df87ef61019da3a36ca2f49226">
<td class="mdescLeft"> </td>
<td class="mdescRight">Read the address from the socket and append it to the string.<br />
</td>
</tr>
<tr class="separator:ga8f8a19df87ef61019da3a36ca2f49226">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gad662596af6fbea79f513e9fe90deb426" class="memitem:gad662596af6fbea79f513e9fe90deb426">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT void </td>
<td class="memItemRight" data-valign="bottom">_dbus_fd_set_close_on_exec (int fd)</td>
</tr>
<tr class="memdesc:gad662596af6fbea79f513e9fe90deb426">
<td class="mdescLeft"> </td>
<td class="mdescRight">Sets the file descriptor to be close on exec.<br />
</td>
</tr>
<tr class="separator:gad662596af6fbea79f513e9fe90deb426">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaedd3d6543dba228fef95e09671842d52" class="memitem:gaedd3d6543dba228fef95e09671842d52">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_PRIVATE_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_ensure_standard_fds (DBusEnsureStandardFdsFlags flags, const char **error_str_p)</td>
</tr>
<tr class="memdesc:gaedd3d6543dba228fef95e09671842d52">
<td class="mdescLeft"> </td>
<td class="mdescRight">Ensure that the standard file descriptors stdin, stdout and stderr are open, by opening /dev/null if necessary.<br />
</td>
</tr>
<tr class="separator:gaedd3d6543dba228fef95e09671842d52">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga4aa7500366dad2dd6d3fa97b3aa7165b" class="memitem:ga4aa7500366dad2dd6d3fa97b3aa7165b">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">_dbus_set_signal_handler (int sig, DBusSignalHandler handler)</td>
</tr>
<tr class="memdesc:ga4aa7500366dad2dd6d3fa97b3aa7165b">
<td class="mdescLeft"> </td>
<td class="mdescRight">Installs a UNIX signal handler.<br />
</td>
</tr>
<tr class="separator:ga4aa7500366dad2dd6d3fa97b3aa7165b">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga18c5f06194b303fd3053e91e141849a9" class="memitem:ga18c5f06194b303fd3053e91e141849a9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">_dbus_reset_oom_score_adj (const char **error_str_p)</td>
</tr>
<tr class="memdesc:ga18c5f06194b303fd3053e91e141849a9">
<td class="mdescLeft"> </td>
<td class="mdescRight">If the current process has been protected from the Linux OOM killer (the oom_score_adj process parameter is negative), reset it to the default level of protection from the OOM killer (set oom_score_adj to zero).<br />
</td>
</tr>
<tr class="separator:ga18c5f06194b303fd3053e91e141849a9">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Internal system-dependent API available on UNIX only.

## Typedef Documentation

## ◆ DBusGroupInfo

|                                            |
|--------------------------------------------|
| typedef struct DBusGroupInfo DBusGroupInfo |

Information about a UNIX group.

Definition at line 87 of file dbus-sysdeps-unix.h.

## ◆ DBusSignalHandler

|                                              |
|----------------------------------------------|
| typedef void(\* DBusSignalHandler) (int sig) |

A UNIX signal handler.

Definition at line 158 of file dbus-sysdeps-unix.h.

## ◆ DBusUserInfo

|                                          |
|------------------------------------------|
| typedef struct DBusUserInfo DBusUserInfo |

Information about a UNIX user.

Definition at line 85 of file dbus-sysdeps-unix.h.

## Enumeration Type Documentation

## ◆ DBusEnsureStandardFdsFlags

|                                 |
|---------------------------------|
| enum DBusEnsureStandardFdsFlags |

Definition at line 146 of file dbus-sysdeps-unix.h.

## Function Documentation

## ◆ \_dbus_append_address_from_socket()

|                                               |     |                |            |
|-----------------------------------------------|-----|----------------|------------|
| dbus_bool_t \_dbus_append_address_from_socket | (   | DBusSocket     | *fd*,      |
|                                               |     | DBusString \*  | *address*, |
|                                               |     | DBusError \*   | *error*    |
|                                               | )   |                |            |

Read the address from the socket and append it to the string.

Parameters  
|         |                                |
|---------|--------------------------------|
| fd      | the socket                     |
| address |                                |
| error   | return location for error code |

Definition at line 5055 of file dbus-sysdeps-unix.c.

References \_dbus_address_append_escaped(), \_dbus_error_from_errno(), \_dbus_string_append(), \_dbus_string_append_printf(), \_dbus_string_init_const(), dbus_set_error(), FALSE, NULL, and TRUE.

Referenced by \_dbus_server_listen_platform_specific().

## ◆ \_dbus_close()

|                                              |     |               |          |
|----------------------------------------------|-----|---------------|----------|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_close | (   | int           | *fd*,    |
|                                              |     | DBusError \*  | *error*  |
|                                              | )   |               |          |

Closes a file descriptor.

Parameters  
|       |                     |
|-------|---------------------|
| fd    | the file descriptor |
| error | error object        |

<!-- -->

Returns  
FALSE if error set

Definition at line 3727 of file dbus-sysdeps-unix.c.

References \_dbus_error_from_errno(), dbus_set_error(), FALSE, and TRUE.

Referenced by \_dbus_close_socket(), \_dbus_command_for_pid(), \_dbus_create_file_exclusively(), \_dbus_file_get_contents(), \_dbus_generate_random_bytes(), \_dbus_listen_systemd_sockets(), \_dbus_listen_tcp_socket(), \_dbus_listen_unix_socket(), \_dbus_message_iter_get_args_valist(), \_dbus_reset_oom_score_adj(), \_dbus_socketpair(), \_dbus_string_save_to_file(), and dbus_message_iter_append_basic().

## ◆ \_dbus_close_all()

|                                           |     |       |     |     |     |
|-------------------------------------------|-----|-------|-----|-----|-----|
| DBUS_PRIVATE_EXPORT void \_dbus_close_all | (   | void  |     | )   |     |

Closes all file descriptors except the first three (i.e.

stdin, stdout, stderr).

Definition at line 4963 of file dbus-sysdeps-unix.c.

Referenced by \_dbus_connect_exec().

## ◆ \_dbus_dup()

|                                    |     |               |          |
|------------------------------------|-----|---------------|----------|
| DBUS_PRIVATE_EXPORT int \_dbus_dup | (   | int           | *fd*,    |
|                                    |     | DBusError \*  | *error*  |
|                                    | )   |               |          |

Duplicates a file descriptor.

Makes sure the fd returned is \>= 3 (i.e. avoids stdin/stdout/stderr). Sets O_CLOEXEC.

Parameters  
|       |                                  |
|-------|----------------------------------|
| fd    | the file descriptor to duplicate |
| error | address of error location.       |

<!-- -->

Returns  
duplicated file descriptor

Definition at line 3755 of file dbus-sysdeps-unix.c.

References \_dbus_error_from_errno(), \_dbus_fd_set_close_on_exec(), and dbus_set_error().

Referenced by \_dbus_credentials_add_credential(), \_dbus_message_iter_get_args_valist(), \_dbus_spawn_async_with_babysitter(), dbus_message_copy(), dbus_message_iter_append_basic(), and dbus_message_iter_get_basic().

## ◆ \_dbus_ensure_standard_fds()

|  |  |  |  |
|----|----|----|----|
| DBUS_PRIVATE_EXPORT dbus_bool_t \_dbus_ensure_standard_fds | ( | DBusEnsureStandardFdsFlags  | *flags*, |
|  |  | const char \*\*  | *error_str_p*  |
|  | ) |  |  |

Ensure that the standard file descriptors stdin, stdout and stderr are open, by opening /dev/null if necessary.

This function does not use DBusError, to avoid calling malloc(), so that it can be used in contexts where an async-signal-safe function is required (for example after fork()). Instead, on failure it sets errno and returns something like "Failed to open /dev/null" in \*error_str_p. Callers are expected to combine \*error_str_p with \_dbus_strerror (errno) to get a full error report.

This function can only be called while single-threaded: either during startup of an executable, or after fork().

Definition at line 179 of file dbus-sysdeps-unix.c.

References \_dbus_assert, and NULL.

Referenced by \_dbus_become_daemon().

## ◆ \_dbus_fd_clear_close_on_exec()

|                                                        |     |      |      |     |     |
|--------------------------------------------------------|-----|------|------|-----|-----|
| DBUS_PRIVATE_EXPORT void \_dbus_fd_clear_close_on_exec | (   | int  | *fd* | )   |     |

Sets the file descriptor to *not* be close-on-exec.

This can be called after \_dbus_fd_set_all_close_on_exec() to make exceptions for pipes used to communicate with child processes.

Parameters  
|     |                     |
|-----|---------------------|
| fd  | the file descriptor |

Definition at line 3705 of file dbus-sysdeps-unix.c.

## ◆ \_dbus_fd_set_all_close_on_exec()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_PRIVATE_EXPORT void \_dbus_fd_set_all_close_on_exec | ( | void  |  | ) |  |

Sets all file descriptors except the first three (i.e.

stdin, stdout, stderr) to be close-on-execute.

Definition at line 4982 of file dbus-sysdeps-unix.c.

References \_dbus_fd_set_close_on_exec().

## ◆ \_dbus_fd_set_close_on_exec()

|                                                      |     |      |      |     |     |
|------------------------------------------------------|-----|------|------|-----|-----|
| DBUS_PRIVATE_EXPORT void \_dbus_fd_set_close_on_exec | (   | int  | *fd* | )   |     |

Sets the file descriptor to be close on exec.

Should be called for all file descriptors in D-Bus code.

Parameters  
|     |                     |
|-----|---------------------|
| fd  | the file descriptor |

Definition at line 3683 of file dbus-sysdeps-unix.c.

Referenced by \_dbus_accept(), \_dbus_connect_exec(), \_dbus_dup(), \_dbus_fd_set_all_close_on_exec(), \_dbus_read_socket_with_unix_fds(), \_dbus_reset_oom_score_adj(), \_dbus_server_new_for_launchd(), \_dbus_socketpair(), and \_dbus_spawn_async_with_babysitter().

## ◆ \_dbus_geteuid()

|                                               |     |       |     |     |     |
|-----------------------------------------------|-----|-------|-----|-----|-----|
| DBUS_PRIVATE_EXPORT dbus_uid_t \_dbus_geteuid | (   | void  |     | )   |     |

Gets our effective UID.

Returns  
process effective UID

Definition at line 3145 of file dbus-sysdeps-unix.c.

Referenced by \_dbus_append_user_from_current_process(), \_dbus_credentials_add_from_current_process(), \_dbus_homedir_from_uid(), and \_dbus_unix_user_is_process_owner().

## ◆ \_dbus_group_info_fill()

|                                    |     |                      |              |
|------------------------------------|-----|----------------------|--------------|
| dbus_bool_t \_dbus_group_info_fill | (   | DBusGroupInfo \*     | *info*,      |
|                                    |     | const DBusString \*  | *groupname*, |
|                                    |     | DBusError \*         | *error*      |
|                                    | )   |                      |              |

Initializes the given DBusGroupInfo struct with information about the given group name.

Parameters  
|           |                       |
|-----------|-----------------------|
| info      | the group info struct |
| groupname | name of group         |
| error     | the error return      |

<!-- -->

Returns  
FALSE if error is set

Definition at line 884 of file dbus-sysdeps-util-unix.c.

References DBUS_GID_UNSET.

Referenced by \_dbus_user_database_lookup_group().

## ◆ \_dbus_group_info_fill_gid()

|                                        |     |                   |          |
|----------------------------------------|-----|-------------------|----------|
| dbus_bool_t \_dbus_group_info_fill_gid | (   | DBusGroupInfo \*  | *info*,  |
|                                        |     | dbus_gid_t        | *gid*,   |
|                                        |     | DBusError \*      | *error*  |
|                                        | )   |                   |          |

Initializes the given DBusGroupInfo struct with information about the given group ID.

Parameters  
|       |                       |
|-------|-----------------------|
| info  | the group info struct |
| gid   | group ID              |
| error | the error return      |

<!-- -->

Returns  
FALSE if error is set

Definition at line 903 of file dbus-sysdeps-util-unix.c.

References NULL.

Referenced by \_dbus_user_database_lookup_group().

## ◆ \_dbus_group_info_free()

|                             |     |                   |        |     |     |
|-----------------------------|-----|-------------------|--------|-----|-----|
| void \_dbus_group_info_free | (   | DBusGroupInfo \*  | *info* | )   |     |

Frees the members of info (but not info itself).

Parameters  
|      |                |
|------|----------------|
| info | the group info |

Definition at line 121 of file dbus-userdb.c.

References dbus_free(), and DBusGroupInfo::groupname.

Referenced by \_dbus_group_info_unref().

## ◆ \_dbus_listen_systemd_sockets()

|                                   |     |                  |          |
|-----------------------------------|-----|------------------|----------|
| int \_dbus_listen_systemd_sockets | (   | DBusSocket \*\*  | *fds*,   |
|                                   |     | DBusError \*     | *error*  |
|                                   | )   |                  |          |

Acquires one or more sockets passed in from systemd.

The sockets are set to be nonblocking.

This will set FD_CLOEXEC for the sockets returned.

Parameters  
|       |                            |
|-------|----------------------------|
| fds   | the file descriptors       |
| error | return location for errors |

<!-- -->

Returns  
the number of file descriptors

Definition at line 1299 of file dbus-sysdeps-unix.c.

References \_dbus_close(), \_dbus_error_from_errno(), DBUS_ERROR_BAD_ADDRESS, DBUS_ERROR_NO_MEMORY, DBUS_ERROR_NOT_SUPPORTED, dbus_free(), dbus_new, dbus_set_error(), dbus_set_error_const(), NULL, and TRUE.

Referenced by \_dbus_server_listen_platform_specific().

## ◆ \_dbus_lookup_launchd_socket()

|  |  |  |  |
|----|----|----|----|
| dbus_bool_t \_dbus_lookup_launchd_socket | ( | DBusString \*  | *socket_path*, |
|  |  | const char \*  | *launchd_env_var*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

quries launchd for a specific env var which holds the socket path.

Parameters  
|                 |                                                   |
|-----------------|---------------------------------------------------|
| socket_path     | append the socket path to this DBusString         |
| launchd_env_var | the env var to look up                            |
| error           | a DBusError to store the error in case of failure |

<!-- -->

Returns  
the value of the env var

Definition at line 4486 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_check_setuid(), \_DBUS_N_ELEMENTS, \_dbus_string_get_length(), \_dbus_string_shorten(), DBUS_ERROR_NOT_SUPPORTED, dbus_set_error(), dbus_set_error_const(), FALSE, NULL, and TRUE.

Referenced by \_dbus_transport_open_platform_specific().

## ◆ \_dbus_read()

|                                     |     |                |           |
|-------------------------------------|-----|----------------|-----------|
| DBUS_PRIVATE_EXPORT int \_dbus_read | (   | int            | *fd*,     |
|                                     |     | DBusString \*  | *buffer*, |
|                                     |     | int            | *count*   |
|                                     | )   |                |           |

Thin wrapper around the read() system call that appends the data it reads to the DBusString buffer.

It appends up to the given count, and returns the same value and same errno as read(). The only exception is that \_dbus_read() handles EINTR for you. Also, \_dbus_read() can return ENOMEM, even though regular UNIX read doesn't.

Unlike \_dbus_read_socket(), \_dbus_read() is not available on Windows.

Parameters  
|        |                                  |
|--------|----------------------------------|
| fd     | the file descriptor to read from |
| buffer | the buffer to append data to     |
| count  | the amount of data to read       |

<!-- -->

Returns  
the number of bytes read or -1

Definition at line 767 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_string_get_data_len(), \_dbus_string_get_length(), \_dbus_string_lengthen(), \_dbus_string_set_length(), and \_dbus_verbose_bytes_of_string().

Referenced by \_dbus_command_for_pid(), \_dbus_file_get_contents(), \_dbus_generate_random_bytes(), and \_dbus_read_socket().

## ◆ \_dbus_reset_oom_score_adj()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| dbus_bool_t \_dbus_reset_oom_score_adj | ( | const char \*\*  | *error_str_p* | ) |  |

If the current process has been protected from the Linux OOM killer (the oom_score_adj process parameter is negative), reset it to the default level of protection from the OOM killer (set oom_score_adj to zero).

This function does not use DBusError, to avoid calling malloc(), so that it can be used in contexts where an async-signal-safe function is required (for example after fork()). Instead, on failure it sets errno and returns something like "Failed to open /dev/null" in \*error_str_p. Callers are expected to combine \*error_str_p with \_dbus_strerror (errno) to get a full error report.

Definition at line 1602 of file dbus-sysdeps-util-unix.c.

References \_dbus_close(), \_dbus_fd_set_close_on_exec(), FALSE, NULL, and TRUE.

Referenced by \_dbus_spawn_async_with_babysitter().

## ◆ \_dbus_set_signal_handler()

|                                |     |                    |            |
|--------------------------------|-----|--------------------|------------|
| void \_dbus_set_signal_handler | (   | int                | *sig*,     |
|                                |     | DBusSignalHandler  | *handler*  |
|                                | )   |                    |            |

Installs a UNIX signal handler.

Parameters  
|         |                      |
|---------|----------------------|
| sig     | the signal to handle |
| handler | the handler          |

Definition at line 545 of file dbus-sysdeps-util-unix.c.

References NULL.

## ◆ \_dbus_user_info_fill()

|                                   |     |                      |             |
|-----------------------------------|-----|----------------------|-------------|
| dbus_bool_t \_dbus_user_info_fill | (   | DBusUserInfo \*      | *info*,     |
|                                   |     | const DBusString \*  | *username*, |
|                                   |     | DBusError \*         | *error*     |
|                                   | )   |                      |             |

Gets user info for the given username.

Parameters  
|          |                                |
|----------|--------------------------------|
| info     | user info object to initialize |
| username | the username                   |
| error    | error return                   |

<!-- -->

Returns  
TRUE on success

Definition at line 2966 of file dbus-sysdeps-unix.c.

References DBUS_UID_UNSET.

Referenced by \_dbus_user_database_lookup().

## ◆ \_dbus_user_info_fill_uid()

|                                       |     |                  |          |
|---------------------------------------|-----|------------------|----------|
| dbus_bool_t \_dbus_user_info_fill_uid | (   | DBusUserInfo \*  | *info*,  |
|                                       |     | dbus_uid_t       | *uid*,   |
|                                       |     | DBusError \*     | *error*  |
|                                       | )   |                  |          |

Gets user info for the given user ID.

Parameters  
|       |                                |
|-------|--------------------------------|
| info  | user info object to initialize |
| uid   | the user ID                    |
| error | error return                   |

<!-- -->

Returns  
TRUE on success

Definition at line 2983 of file dbus-sysdeps-unix.c.

References NULL.

Referenced by \_dbus_user_database_lookup().

## ◆ \_dbus_user_info_free()

|                            |     |                  |        |     |     |
|----------------------------|-----|------------------|--------|-----|-----|
| void \_dbus_user_info_free | (   | DBusUserInfo \*  | *info* | )   |     |

Frees the members of info (but not info itself)

Parameters  
|      |                      |
|------|----------------------|
| info | the user info struct |

Definition at line 108 of file dbus-userdb.c.

References dbus_free(), DBusUserInfo::group_ids, DBusUserInfo::homedir, and DBusUserInfo::username.

Referenced by \_dbus_user_info_unref().

## ◆ \_dbus_write()

|                  |     |                      |           |
|------------------|-----|----------------------|-----------|
| int \_dbus_write | (   | int                  | *fd*,     |
|                  |     | const DBusString \*  | *buffer*, |
|                  |     | int                  | *start*,  |
|                  |     | int                  | *len*     |
|                  | )   |                      |           |

Thin wrapper around the write() system call that writes a part of a DBusString and handles EINTR for you.

Parameters  
|        |                                       |
|--------|---------------------------------------|
| fd     | the file descriptor to write          |
| buffer | the buffer to write data from         |
| start  | the first byte in the buffer to write |
| len    | the number of bytes to try to write   |

<!-- -->

Returns  
the number of bytes written or -1 on error

Definition at line 827 of file dbus-sysdeps-unix.c.

References \_dbus_string_get_const_data_len(), and \_dbus_verbose_bytes_of_string().

Referenced by \_dbus_string_save_to_file(), \_dbus_write_socket(), and \_dbus_write_two().

## ◆ \_dbus_write_two()

|                      |     |                      |            |
|----------------------|-----|----------------------|------------|
| int \_dbus_write_two | (   | int                  | *fd*,      |
|                      |     | const DBusString \*  | *buffer1*, |
|                      |     | int                  | *start1*,  |
|                      |     | int                  | *len1*,    |
|                      |     | const DBusString \*  | *buffer2*, |
|                      |     | int                  | *start2*,  |
|                      |     | int                  | *len2*     |
|                      | )   |                      |            |

Like \_dbus_write() but will use writev() if possible to write both buffers in sequence.

The return value is the number of bytes written in the first buffer, plus the number written in the second. If the first buffer is written successfully and an error occurs writing the second, the number of bytes in the first is returned (i.e. the error is ignored), on systems that don't have writev. Handles EINTR for you. The second buffer may be NULL.

Parameters  
|         |                                            |
|---------|--------------------------------------------|
| fd      | the file descriptor                        |
| buffer1 | first buffer                               |
| start1  | first byte to write in first buffer        |
| len1    | number of bytes to write from first buffer |
| buffer2 | second buffer, or NULL                     |
| start2  | first byte to write in second buffer       |
| len2    | number of bytes to write in second buffer  |

<!-- -->

Returns  
total bytes written from both buffers, or -1 on error

Definition at line 873 of file dbus-sysdeps-unix.c.

References \_dbus_assert, \_dbus_string_get_const_data_len(), \_dbus_write(), and NULL.

Referenced by \_dbus_write_socket_two().
